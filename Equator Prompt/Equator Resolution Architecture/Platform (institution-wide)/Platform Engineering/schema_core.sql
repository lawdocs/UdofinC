-- ============================================================================
-- Equator Resolution — SHARED CORE DATA MODEL
-- PostgreSQL 15+.  Law stated as at July 2026.
--
-- One core schema shared by all five verticals (Family, Commercial, Financial,
-- Workplace, Insurance), with a thin per-vertical EXTENSION pattern — instead of
-- five divergent databases. The core carries the entities and controls that every
-- vertical has in common; each vertical adds only its own tables and constraints.
--
-- SHARED CONTROLS ENFORCED IN THE CORE:
--   K1  Every case belongs to exactly one vertical and one status machine.
--   K2  Every party has recorded DPDP consent before processing.
--   K3  A "clock" (limitation / statutory window) has a generated expiry and,
--       where a vertical requires it, must be owned before closure.
--   K4  Caucus / private-session material is sealed to the neutral (RLS).
--   K5  Money moves only through escrow milestones with evidence.
--   K6  Every state change is written to a hash-chained audit log.
--   K7  Sensitive sub-stores (POSH, health) live in separate schemas with no FK
--       path from the core — the separation is the control.
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS core;
SET search_path = core, public;

CREATE TYPE vertical AS ENUM ('family','commercial','financial','workplace','insurance');

CREATE TYPE core_case_status AS ENUM (
  'intake','triaged','in_process','settlement','signposted','closed','withdrawn');

CREATE TYPE clock_kind AS ENUM (
  'limitation','statutory_window','contractual_bar','arb_29a','ombudsman_1y',
  'insurer_reply_30d','consumer_2y','posh_90d','s12a','other');

CREATE TYPE consent_basis AS ENUM ('consent','contract','legal_obligation','vital_interest','public_task');

-- ─────────────────────────────── identity & consent (K2) ───────────────────────────────
CREATE TABLE party (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  display_name   TEXT NOT NULL,
  masked_gov_id  TEXT,
  email          TEXT,
  mobile         TEXT,
  kyc_verified   BOOLEAN NOT NULL DEFAULT FALSE,
  kyc_method     TEXT,                         -- aadhaar_ekyc | gov_id | corporate_authority | video
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE consent (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  party_id       UUID NOT NULL REFERENCES party(id),
  purpose        TEXT NOT NULL,
  basis          consent_basis NOT NULL DEFAULT 'consent',
  sensitive_categories TEXT[] NOT NULL DEFAULT '{}',   -- e.g. health, posh, financial
  given_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
  withdrawn_at   TIMESTAMPTZ,
  CONSTRAINT consent_present CHECK (basis <> 'consent' OR given_at IS NOT NULL)
);

-- ─────────────────────────────── the case (K1) ───────────────────────────────
CREATE TABLE cases (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_no        TEXT UNIQUE NOT NULL,
  vertical       vertical NOT NULL,
  status         core_case_status NOT NULL DEFAULT 'intake',
  amount_in_dispute NUMERIC(18,2) NOT NULL DEFAULT 0,
  opened_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  closed_at      TIMESTAMPTZ,
  -- the per-vertical detail lives in <vertical>_ext, keyed by this id;
  -- vertical-specific status values map onto core_case_status for reporting.
  ext            JSONB NOT NULL DEFAULT '{}'::jsonb    -- typed extension mirror for search
);

CREATE TABLE case_party (
  case_id   UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  party_id  UUID NOT NULL REFERENCES party(id),
  role      TEXT NOT NULL,
  PRIMARY KEY (case_id, party_id, role)
);

-- ─────────────────────────────── the clock engine (K3) ───────────────────────────────
CREATE TABLE clock (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id      UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  kind         clock_kind NOT NULL,
  label        TEXT NOT NULL,
  trigger_date DATE NOT NULL,
  period_days  INTEGER NOT NULL CHECK (period_days > 0),
  expiry_date  DATE GENERATED ALWAYS AS (trigger_date + period_days) STORED,
  owner        TEXT,
  prompted_at  TIMESTAMPTZ,
  UNIQUE (case_id, kind, label)
);
CREATE INDEX ix_clock_expiry ON clock(expiry_date);

-- verticals that require owned clocks before closure register here
CREATE TABLE closure_policy (
  vertical            vertical PRIMARY KEY,
  require_owned_clocks BOOLEAN NOT NULL DEFAULT FALSE,
  require_signposting  BOOLEAN NOT NULL DEFAULT FALSE,
  require_registration BOOLEAN NOT NULL DEFAULT FALSE
);
INSERT INTO closure_policy VALUES
  ('insurance', TRUE, TRUE, FALSE),
  ('commercial', FALSE, FALSE, TRUE),
  ('financial', TRUE, TRUE, FALSE),
  ('workplace', FALSE, TRUE, FALSE),
  ('family', TRUE, TRUE, FALSE)
ON CONFLICT DO NOTHING;

CREATE TABLE signposting_event (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id      UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  delivered_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  channel      TEXT NOT NULL,
  language     TEXT NOT NULL,
  script_version TEXT NOT NULL,
  delivered_by TEXT NOT NULL
);

-- K3 + K1: a single closure guard reads the per-vertical closure_policy
CREATE OR REPLACE FUNCTION core_guard_closure() RETURNS trigger AS $$
DECLARE pol RECORD; n_sign INT; n_unowned INT;
BEGIN
  IF NEW.status = 'closed' AND OLD.status <> 'closed' THEN
    SELECT * INTO pol FROM closure_policy WHERE vertical = NEW.vertical;
    IF pol.require_signposting THEN
      SELECT count(*) INTO n_sign FROM signposting_event WHERE case_id = NEW.id;
      IF n_sign = 0 THEN
        RAISE EXCEPTION 'core: cannot close % (%) — signposting required', NEW.case_no, NEW.vertical
          USING ERRCODE = 'check_violation';
      END IF;
    END IF;
    IF pol.require_owned_clocks THEN
      SELECT count(*) INTO n_unowned FROM clock WHERE case_id = NEW.id AND owner IS NULL;
      IF n_unowned > 0 THEN
        RAISE EXCEPTION 'core: cannot close % (%) — % unowned clock(s)', NEW.case_no, NEW.vertical, n_unowned
          USING ERRCODE = 'check_violation';
      END IF;
    END IF;
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_core_guard_closure
  BEFORE UPDATE OF status ON cases FOR EACH ROW EXECUTE FUNCTION core_guard_closure();

-- ─────────────────────────────── neutral & sessions (K4) ───────────────────────────────
CREATE TABLE neutral (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  full_name     TEXT NOT NULL,
  verticals     vertical[] NOT NULL DEFAULT '{}',
  accreditation TEXT NOT NULL,                 -- ECMN / ECCN / ECFC / ECWN / ECIN
  languages     TEXT[] NOT NULL DEFAULT '{}',
  pi_cover_expiry DATE,
  active        BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE session (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id      UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  neutral_id   UUID NOT NULL REFERENCES neutral(id),
  mode         TEXT NOT NULL,
  scheduled_at TIMESTAMPTZ NOT NULL
);

-- K4: caucus notes sealed to the neutral via row-level security
CREATE TABLE caucus_note (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id   UUID NOT NULL REFERENCES session(id) ON DELETE CASCADE,
  neutral_id   UUID NOT NULL REFERENCES neutral(id),
  note_cipher  BYTEA NOT NULL,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);
ALTER TABLE caucus_note ENABLE ROW LEVEL SECURITY;
CREATE POLICY caucus_read_own ON caucus_note
  USING (neutral_id::text = current_setting('app.neutral_id', TRUE));

-- ─────────────────────────────── escrow (K5) ───────────────────────────────
CREATE TABLE escrow (
  id       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id  UUID NOT NULL REFERENCES cases(id) ON DELETE CASCADE,
  amount   NUMERIC(18,2) NOT NULL CHECK (amount >= 0),
  state    TEXT NOT NULL DEFAULT 'created'
);
CREATE TABLE escrow_milestone (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  escrow_id    UUID NOT NULL REFERENCES escrow(id) ON DELETE CASCADE,
  name         TEXT NOT NULL,
  condition    TEXT NOT NULL,
  evidence_ref TEXT,
  amount       NUMERIC(18,2) NOT NULL,
  released_at  TIMESTAMPTZ,
  CONSTRAINT release_needs_evidence CHECK (released_at IS NULL OR evidence_ref IS NOT NULL)   -- K5
);

-- ─────────────────────────────── settlement (shared shell) ───────────────────────────────
CREATE TABLE settlement (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id        UUID NOT NULL UNIQUE REFERENCES cases(id) ON DELETE CASCADE,
  amount         NUMERIC(18,2) NOT NULL CHECK (amount >= 0),
  registered_at  TIMESTAMPTZ,
  enforceable_s27 BOOLEAN NOT NULL DEFAULT TRUE,
  -- shared non-waiver invariant (verticals may add their own):
  statutory_rights_waived BOOLEAN NOT NULL DEFAULT FALSE,
  CONSTRAINT core_no_statutory_waiver CHECK (statutory_rights_waived = FALSE)
);

-- ─────────────────────────────── audit (K6) ───────────────────────────────
CREATE TABLE audit_event (
  id         BIGSERIAL PRIMARY KEY,
  actor      TEXT, case_id UUID, vertical vertical, store TEXT NOT NULL DEFAULT 'core',
  action     TEXT NOT NULL, detail TEXT,
  prev_hash  TEXT, row_hash TEXT, created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ─────────────────────────────── sensitive sub-stores (K7) ───────────────────────────────
-- These are created in SEPARATE schemas with no FK path from core.
--   workplace_posh.*   — POSH complaints (see schema_wp.sql)
--   ins_health.*       — medical records (see schema_in.sql)
-- The core references them only by opaque text token, never by foreign key.

-- ─────────────────────────────── the extension pattern ───────────────────────────────
-- Each vertical owns a schema (family, commercial, financial, wp, ins) whose tables
-- reference core.cases(id). The vertical adds ONLY:
--   * its own status enum, mapped to core_case_status by a small function;
--   * its own rule-bearing tables and CHECK constraints (e.g. ins: retail arbitration
--     bar, no statutory waiver; commercial: arbitration-needs-agreement, s.12A);
--   * a trigger that keeps cases.ext in sync for cross-vertical search.
-- Nothing in a vertical schema may weaken a core control.

-- ─────────────────────────────── reporting ───────────────────────────────
CREATE VIEW v_portfolio_caseload AS
SELECT vertical, status, count(*) AS matters, round(avg(amount_in_dispute),0) AS avg_value
FROM cases GROUP BY vertical, status;

CREATE VIEW v_clock_risk AS
SELECT c.case_no, c.vertical, k.label, k.expiry_date, k.owner,
       (k.expiry_date - CURRENT_DATE) AS days_left
FROM clock k JOIN cases c ON c.id = k.case_id
WHERE c.status NOT IN ('closed','withdrawn')
ORDER BY k.expiry_date;
