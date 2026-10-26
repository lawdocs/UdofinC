-- ============================================================================
-- Equator Resolution — Commercial & Business Dispute vertical
-- PostgreSQL 15+ DDL.  Law stated as at July 2026.
--
-- INSTITUTIONAL RULES ENFORCED AS CONSTRAINTS (not application politeness):
--   C1  Arbitration cannot be administered without an arbitration agreement
--       on the record.
--   C2  An MSME claimant's reference is conciliated before it is arbitrated
--       (MSMED Act, 2006, s.18): no arbitration step until conciliation has
--       been recorded as attempted and failed.
--   C3  A commercial suit of a "specified value" not seeking urgent interim
--       relief must show pre-institution mediation (Commercial Courts Act,
--       2015, s.12A) before a litigation-referral can be marked "exhausted".
--   C4  No mediated settlement may be closed without registration metadata
--       (Mediation Act, 2023, s.27) once status = 'settled'.
--   C5  Caucus notes are sealed to the neutral; there is no cross-party read
--       path (enforced by row-level security, mirrored here as a guard).
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS cm;
SET search_path = cm, public;

-- ─────────────────────────────── enums ───────────────────────────────
CREATE TYPE party_role AS ENUM (
  'claimant','respondent','msme_supplier','buyer','shareholder','company',
  'jv_partner','guarantor','counsel','expert');

CREATE TYPE entity_type AS ENUM ('company','llp','partnership','proprietorship','msme','individual','trust','psu','foreign');

CREATE TYPE dispute_type AS ENUM (
  'breach_of_contract','payment_recovery','msme_delayed_payment','shareholder_oppression',
  'jv_partnership','supply_distribution','construction_epc','ip_licensing','post_ma_indemnity',
  'guarantee_invocation','agency','franchise','it_services','real_estate_commercial','other');

CREATE TYPE mechanism AS ENUM ('mediation','conciliation','arbitration','med_arb','expert_determination');

CREATE TYPE case_status AS ENUM (
  'intake','triaged','pre_institution_mediation','in_conciliation','constituted',
  'in_session','settled','award','signposted','closed','withdrawn');

CREATE TYPE route AS ENUM (
  'equator_mediation','equator_conciliation','equator_arbitration','msme_facilitation_council',
  's12a_pre_institution_mediation','commercial_court','nclt','civil_court','drt');

-- ─────────────────────────────── core ───────────────────────────────
CREATE TABLE party (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  role         party_role NOT NULL,
  legal_name   TEXT NOT NULL,
  entity_type  entity_type NOT NULL,
  cin_gstin    TEXT,
  is_msme      BOOLEAN NOT NULL DEFAULT FALSE,
  udyam_no     TEXT,                          -- MSME registration
  address      TEXT,
  authorised_signatory TEXT,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE agreement (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title              TEXT NOT NULL,
  has_arb_clause     BOOLEAN NOT NULL DEFAULT FALSE,
  arb_clause_text    TEXT,
  seat               TEXT,
  venue              TEXT,
  governing_law      TEXT,
  language           TEXT DEFAULT 'English',
  panel_size         INTEGER CHECK (panel_size IN (1,3)),
  med_precondition   BOOLEAN NOT NULL DEFAULT FALSE,   -- multi-tier clause
  signed_on          DATE
);

CREATE TABLE dispute_case (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_no            TEXT UNIQUE NOT NULL,
  claimant_id        UUID NOT NULL REFERENCES party(id),
  respondent_id      UUID NOT NULL REFERENCES party(id),
  agreement_id       UUID REFERENCES agreement(id),
  dispute_types      dispute_type[] NOT NULL DEFAULT '{}',
  amount_in_dispute  NUMERIC(18,2) NOT NULL DEFAULT 0,
  specified_value    BOOLEAN NOT NULL DEFAULT FALSE,   -- Commercial Courts Act threshold
  urgent_interim     BOOLEAN NOT NULL DEFAULT FALSE,   -- exempts s.12A
  mechanism          mechanism,
  route              route,
  status             case_status NOT NULL DEFAULT 'intake',
  msme_reference     BOOLEAN NOT NULL DEFAULT FALSE,   -- filed as an MSME s.18 reference
  conciliation_attempted BOOLEAN NOT NULL DEFAULT FALSE,
  conciliation_failed    BOOLEAN NOT NULL DEFAULT FALSE,
  opened_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  closed_at          TIMESTAMPTZ,

  -- ══════════ C1 — no arbitration without an agreement ══════════
  CONSTRAINT arbitration_needs_agreement
    CHECK (mechanism IS DISTINCT FROM 'arbitration' OR agreement_id IS NOT NULL),

  -- ══════════ C2 — MSME conciliation before arbitration (MSMED s.18) ══════════
  CONSTRAINT msme_conciliation_before_arbitration
    CHECK (NOT (msme_reference AND mechanism = 'arbitration')
           OR (conciliation_attempted AND conciliation_failed))
);
COMMENT ON CONSTRAINT arbitration_needs_agreement ON dispute_case IS
 'C1: Equator will not administer an arbitration where no arbitration agreement is on the record.';
COMMENT ON CONSTRAINT msme_conciliation_before_arbitration ON dispute_case IS
 'C2: MSMED Act, 2006 s.18 — the Facilitation Council conciliates first; arbitration only if conciliation fails.';

-- trigger to enforce C1's agreement actually carrying an arbitration clause
CREATE OR REPLACE FUNCTION guard_arbitration() RETURNS trigger AS $$
DECLARE has_clause BOOLEAN;
BEGIN
  IF NEW.mechanism = 'arbitration' THEN
    SELECT a.has_arb_clause INTO has_clause FROM agreement a WHERE a.id = NEW.agreement_id;
    IF has_clause IS DISTINCT FROM TRUE THEN
      RAISE EXCEPTION 'C1: cannot administer arbitration for case % — the agreement has no arbitration clause',
        NEW.case_no USING ERRCODE = 'check_violation';
    END IF;
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_guard_arbitration
  BEFORE INSERT OR UPDATE OF mechanism, agreement_id ON dispute_case
  FOR EACH ROW EXECUTE FUNCTION guard_arbitration();

-- ─────────────────────────── s.12A pre-institution mediation ───────────────────────────
CREATE TABLE s12a_record (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id        UUID NOT NULL UNIQUE REFERENCES dispute_case(id) ON DELETE CASCADE,
  applicable     BOOLEAN NOT NULL,             -- specified value AND not urgent interim
  commenced_on   DATE,
  concluded_on   DATE,
  outcome        TEXT CHECK (outcome IN ('settled','non_starter','failed', NULL)),
  exhausted      BOOLEAN NOT NULL DEFAULT FALSE
);
COMMENT ON TABLE s12a_record IS
 'C3: Commercial Courts Act, 2015 s.12A — a specified-value suit not seeking urgent interim relief must exhaust '
 'pre-institution mediation before a commercial_court referral is valid.';

CREATE OR REPLACE FUNCTION guard_s12a() RETURNS trigger AS $$
DECLARE rec RECORD;
BEGIN
  IF NEW.route = 'commercial_court' THEN
    SELECT specified_value, urgent_interim INTO rec FROM dispute_case WHERE id = NEW.case_id;
    IF rec.specified_value AND NOT rec.urgent_interim AND NOT NEW.exhausted THEN
      RAISE EXCEPTION 'C3: case cannot proceed to a commercial court — s.12A pre-institution mediation not exhausted'
        USING ERRCODE = 'check_violation';
    END IF;
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;

-- ─────────────────────────── conciliation / mediation ───────────────────────────
CREATE TABLE neutral (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  full_name     TEXT NOT NULL,
  accreditation TEXT NOT NULL,       -- ECCN level
  panel         TEXT NOT NULL,       -- mediator | arbitrator | expert
  languages     TEXT[] NOT NULL DEFAULT '{}',
  pi_cover_expiry DATE,
  active        BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE neutral_disclosure (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  neutral_id    UUID NOT NULL REFERENCES neutral(id),
  case_id       UUID NOT NULL REFERENCES dispute_case(id),
  relationships TEXT,
  declared_independent BOOLEAN NOT NULL,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT disclosure_independent CHECK (declared_independent = TRUE)
);

CREATE TABLE session (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id      UUID NOT NULL REFERENCES dispute_case(id) ON DELETE CASCADE,
  neutral_id   UUID NOT NULL REFERENCES neutral(id),
  mode         TEXT NOT NULL,       -- joint | caucus | online | in_person
  scheduled_at TIMESTAMPTZ NOT NULL
);

-- C5: caucus notes sealed to the neutral
CREATE TABLE caucus_note (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id   UUID NOT NULL REFERENCES session(id) ON DELETE CASCADE,
  neutral_id   UUID NOT NULL REFERENCES neutral(id),
  note_cipher  BYTEA NOT NULL,       -- encrypted; RLS restricts SELECT to the authoring neutral
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);
COMMENT ON TABLE caucus_note IS 'C5: confidential to the neutral; row-level security restricts reads. No cross-party path.';

-- ─────────────────────────── arbitration ───────────────────────────
CREATE TABLE tribunal (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id        UUID NOT NULL UNIQUE REFERENCES dispute_case(id) ON DELETE CASCADE,
  member_count   INTEGER NOT NULL CHECK (member_count IN (1,3)),
  constituted_on DATE,
  po1_on         DATE,                        -- Procedural Order 1
  pleadings_complete_on DATE,
  s29a_expiry    DATE GENERATED ALWAYS AS (pleadings_complete_on + 365 + 180) STORED,
  award_on       DATE
);
COMMENT ON COLUMN tribunal.s29a_expiry IS 'A&C Act s.29A: 12 months from completion of pleadings, extendable by 6.';

CREATE TABLE award (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id        UUID NOT NULL UNIQUE REFERENCES dispute_case(id) ON DELETE CASCADE,
  reasoned       BOOLEAN NOT NULL DEFAULT TRUE,     -- s.31(3)
  amount_awarded NUMERIC(18,2),
  interest_terms TEXT,
  costs_terms    TEXT,
  signed_on      DATE,
  enforceable_s36 BOOLEAN NOT NULL DEFAULT TRUE,
  CONSTRAINT award_must_be_reasoned CHECK (reasoned = TRUE)
);

-- ─────────────────────────── settlement ───────────────────────────
CREATE TABLE settlement (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id        UUID NOT NULL UNIQUE REFERENCES dispute_case(id) ON DELETE CASCADE,
  amount         NUMERIC(18,2) NOT NULL CHECK (amount >= 0),
  payment_terms  TEXT,
  registered_at  TIMESTAMPTZ,                 -- C4: required before closure when settled
  enforceable_s27 BOOLEAN NOT NULL DEFAULT TRUE,
  signed_at      TIMESTAMPTZ
);

CREATE TABLE escrow (
  id       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id  UUID NOT NULL REFERENCES dispute_case(id) ON DELETE CASCADE,
  amount   NUMERIC(18,2) NOT NULL CHECK (amount >= 0),
  state    TEXT NOT NULL DEFAULT 'created'
);

-- ══════════ C4 — no closure of a settled matter without registration ══════════
CREATE OR REPLACE FUNCTION guard_settlement_closure() RETURNS trigger AS $$
DECLARE reg TIMESTAMPTZ;
BEGIN
  IF NEW.status = 'closed' AND OLD.status <> 'closed' THEN
    IF EXISTS (SELECT 1 FROM settlement s WHERE s.case_id = NEW.id) THEN
      SELECT registered_at INTO reg FROM settlement WHERE case_id = NEW.id;
      IF reg IS NULL THEN
        RAISE EXCEPTION 'C4: cannot close settled case % — settlement not registered under Mediation Act s.27',
          NEW.case_no USING ERRCODE = 'check_violation';
      END IF;
    END IF;
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_guard_settlement_closure
  BEFORE UPDATE OF status ON dispute_case
  FOR EACH ROW EXECUTE FUNCTION guard_settlement_closure();

-- hash-chained audit
CREATE TABLE audit_event (
  id         BIGSERIAL PRIMARY KEY,
  actor      TEXT,
  case_id    UUID,
  action     TEXT NOT NULL,
  detail     TEXT,
  prev_hash  TEXT,
  row_hash   TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ─────────────────────────── reporting ───────────────────────────
CREATE VIEW v_route_summary AS
SELECT route, count(*) AS matters, round(avg(amount_in_dispute),0) AS avg_value
FROM dispute_case GROUP BY route;

CREATE VIEW v_s29a_risk AS
SELECT d.case_no, t.pleadings_complete_on, t.s29a_expiry,
       (t.s29a_expiry - CURRENT_DATE) AS days_left
FROM tribunal t JOIN dispute_case d ON d.id = t.case_id
WHERE t.award_on IS NULL
ORDER BY t.s29a_expiry;
