-- =====================================================================
-- Equator Resolution — Family & Marital Mediation Platform
-- PostgreSQL schema (DDL). Draft for engineering; settle with security & counsel.
-- Principles: DPDP-aware (masked identifiers), safety-first (screening & flags),
-- confidentiality (sealed caucus notes), auditable (tamper-evident event log).
-- Statutory anchors: Mediation Act 2023 (s.20 registration, s.22 confidentiality,
-- s.27 enforceability), Family Courts Act 1984, BNSS s.528/s.359, DPDP Act 2023.
-- =====================================================================
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ---------- Enumerated types ----------
CREATE TYPE party_role        AS ENUM ('spouse_a','spouse_b','child','guardian','counsel','relative','other');
CREATE TYPE marriage_regime   AS ENUM ('hindu','special_marriage','muslim','christian','parsi','inter_faith','foreign_nri','live_in','unspecified');
CREATE TYPE dispute_type      AS ENUM ('divorce_mutual','divorce_contested','judicial_separation','maintenance','custody','visitation','property_division','stridhan','domestic_violence','dowry_harassment','restitution','guardianship','nri_cross_border','other');
CREATE TYPE case_status       AS ENUM ('intake','screening','triaged','notice_served','response','mediator_appointed','in_session','settlement','escrow','court_referral','closed','withdrawn','not_suitable');
CREATE TYPE route_type        AS ENUM ('mediation','court_referral','safety_pathway','not_suitable','lok_adalat');
CREATE TYPE screening_outcome AS ENUM ('suitable','suitable_with_safeguards','shuttle_only','not_suitable_safety','not_suitable_capacity');
CREATE TYPE session_mode      AS ENUM ('joint','caucus','shuttle','child_inclusive','online','in_person');
CREATE TYPE neutral_grade     AS ENUM ('A','B','C');
CREATE TYPE doc_kind          AS ENUM ('form','agreement','msa','affidavit','petition','order','evidence','certificate','report');
CREATE TYPE escrow_state      AS ENUM ('created','funded','partially_released','released','refunded');
CREATE TYPE consent_basis     AS ENUM ('dpdp_consent','legal_obligation','legitimate_use');

-- ---------- Parties & identity ----------
CREATE TABLE party (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  role              party_role NOT NULL,
  full_name         TEXT NOT NULL,
  masked_gov_id     TEXT,                       -- tokenised; never store raw Aadhaar/PAN
  email_hash        TEXT,
  phone_hash        TEXT,
  preferred_language TEXT DEFAULT 'en',
  is_minor          BOOLEAN DEFAULT FALSE,
  needs_support     BOOLEAN DEFAULT FALSE,      -- accessibility / vulnerability
  kyc_verified      BOOLEAN DEFAULT FALSE,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);
COMMENT ON COLUMN party.masked_gov_id IS 'DPDP: store tokenised reference only';

CREATE TABLE consent_record (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  party_id      UUID NOT NULL REFERENCES party(id),
  purpose       TEXT NOT NULL,
  basis         consent_basis NOT NULL DEFAULT 'dpdp_consent',
  granted_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  withdrawn_at  TIMESTAMPTZ,
  notice_version TEXT NOT NULL
);

-- ---------- Case ----------
CREATE TABLE mediation_case (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_number       TEXT UNIQUE NOT NULL,
  dispute_types     dispute_type[] NOT NULL,
  regime            marriage_regime NOT NULL DEFAULT 'unspecified',
  status            case_status NOT NULL DEFAULT 'intake',
  route             route_type,
  initiator_id      UUID REFERENCES party(id),
  amount_in_dispute NUMERIC(16,2),
  has_children      BOOLEAN DEFAULT FALSE,
  safety_flag       BOOLEAN DEFAULT FALSE,      -- set by screening; gates joint sessions
  court_linked      BOOLEAN DEFAULT FALSE,
  jurisdiction_state TEXT,
  opened_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  closed_at         TIMESTAMPTZ,
  CONSTRAINT chk_close CHECK (closed_at IS NULL OR closed_at >= opened_at)
);
CREATE INDEX idx_case_status ON mediation_case(status);
CREATE INDEX idx_case_safety ON mediation_case(safety_flag) WHERE safety_flag;

CREATE TABLE case_party (
  case_id  UUID NOT NULL REFERENCES mediation_case(id) ON DELETE CASCADE,
  party_id UUID NOT NULL REFERENCES party(id),
  role     party_role NOT NULL,
  PRIMARY KEY (case_id, party_id)
);

CREATE TABLE child (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES mediation_case(id) ON DELETE CASCADE,
  initials      TEXT,                            -- minimise: initials, not full name
  age_years     INT CHECK (age_years BETWEEN 0 AND 25),
  living_with   TEXT,
  special_needs BOOLEAN DEFAULT FALSE,
  ci_mediation_consent BOOLEAN DEFAULT FALSE     -- child-inclusive mediation consent
);

-- ---------- Safety & suitability screening (MIAM / MASIC analogue) ----------
CREATE TABLE screening (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id           UUID NOT NULL REFERENCES mediation_case(id) ON DELETE CASCADE,
  party_id          UUID NOT NULL REFERENCES party(id),
  screened_by       UUID,
  dv_indicators     BOOLEAN DEFAULT FALSE,
  power_imbalance   BOOLEAN DEFAULT FALSE,
  capacity_concern  BOOLEAN DEFAULT FALSE,
  coercion_concern  BOOLEAN DEFAULT FALSE,
  outcome           screening_outcome NOT NULL,
  safeguards        TEXT,                        -- shuttle, separate timings, support person
  screened_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);
COMMENT ON TABLE screening IS 'Screening is conducted separately and confidentially with each party.';

-- ---------- Panel & appointment ----------
CREATE TABLE neutral (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  full_name     TEXT NOT NULL,
  grade         neutral_grade NOT NULL,
  expertise     TEXT[],
  languages     TEXT[],
  gender        TEXT,
  certified_ref TEXT,                            -- Equator certification / MCI reference
  rubric_score  INT CHECK (rubric_score BETWEEN 0 AND 100),
  code_signed   BOOLEAN DEFAULT FALSE,
  active        BOOLEAN DEFAULT TRUE
);

CREATE TABLE appointment (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id           UUID NOT NULL REFERENCES mediation_case(id) ON DELETE CASCADE,
  neutral_id        UUID NOT NULL REFERENCES neutral(id),
  conflict_checked  BOOLEAN DEFAULT FALSE,
  disclosure_signed BOOLEAN DEFAULT FALSE,
  challenged        BOOLEAN DEFAULT FALSE,
  challenge_outcome TEXT,
  appointed_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  ended_at          TIMESTAMPTZ
);

-- ---------- Sessions & sealed notes ----------
CREATE TABLE session (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES mediation_case(id) ON DELETE CASCADE,
  mode          session_mode NOT NULL,
  scheduled_at  TIMESTAMPTZ NOT NULL,
  duration_min  INT,
  attended      BOOLEAN DEFAULT FALSE,
  recording_ref TEXT,                            -- only if BOTH parties consent
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE caucus_note (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id    UUID NOT NULL REFERENCES session(id) ON DELETE CASCADE,
  neutral_id    UUID NOT NULL REFERENCES neutral(id),
  party_id      UUID REFERENCES party(id),
  note_cipher   BYTEA NOT NULL,                  -- encrypted; sealed to the mediator
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);
COMMENT ON TABLE caucus_note IS 'Sealed: never disclosed across parties; Mediation Act s.22 confidentiality.';

-- ---------- Documents, e-Sign & e-Stamp ----------
CREATE TABLE document (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES mediation_case(id) ON DELETE CASCADE,
  form_ref      TEXT,                            -- e.g. F-01 .. F-29
  kind          doc_kind NOT NULL,
  storage_uri   TEXT NOT NULL,
  sha256        TEXT NOT NULL,
  esigned       BOOLEAN DEFAULT FALSE,
  esign_ref     TEXT,
  estamped      BOOLEAN DEFAULT FALSE,
  estamp_ref    TEXT,
  estamp_state  TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- Settlement (MSA) ----------
CREATE TABLE settlement (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id            UUID NOT NULL REFERENCES mediation_case(id) ON DELETE CASCADE,
  document_id        UUID REFERENCES document(id),
  total_value        NUMERIC(16,2),
  maintenance_amount NUMERIC(16,2),
  maintenance_freq   TEXT,
  custody_terms      TEXT,
  property_terms     TEXT,
  registered_s20     BOOLEAN DEFAULT FALSE,      -- Mediation Act s.20 registration
  enforceable_s27    BOOLEAN DEFAULT TRUE,       -- enforceable as a decree
  signed_at          TIMESTAMPTZ,
  created_at         TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE settlement_obligation (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  settlement_id UUID NOT NULL REFERENCES settlement(id) ON DELETE CASCADE,
  description   TEXT NOT NULL,
  due_date      DATE,
  amount        NUMERIC(16,2),
  obligor_id    UUID REFERENCES party(id),
  complied      BOOLEAN DEFAULT FALSE,
  complied_at   TIMESTAMPTZ
);

-- ---------- Escrow & payments ----------
CREATE TABLE escrow (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES mediation_case(id) ON DELETE CASCADE,
  escrow_bank   TEXT NOT NULL,
  amount        NUMERIC(16,2) NOT NULL CHECK (amount >= 0),
  state         escrow_state NOT NULL DEFAULT 'created',
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE escrow_milestone (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  escrow_id     UUID NOT NULL REFERENCES escrow(id) ON DELETE CASCADE,
  name          TEXT NOT NULL,
  condition     TEXT,
  amount        NUMERIC(16,2) NOT NULL,
  released      BOOLEAN DEFAULT FALSE,
  released_at   TIMESTAMPTZ
);

CREATE TABLE payment_txn (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES mediation_case(id),
  escrow_id     UUID REFERENCES escrow(id),
  method        TEXT,                             -- upi|imps|neft|rtgs
  direction     TEXT CHECK (direction IN ('in','out')),
  amount        NUMERIC(16,2) NOT NULL,
  reference     TEXT,
  reconciled    BOOLEAN DEFAULT FALSE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- Court interface ----------
CREATE TABLE court_referral (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES mediation_case(id) ON DELETE CASCADE,
  court_name    TEXT NOT NULL,
  court_case_no TEXT,
  referred_under TEXT,                            -- e.g. s.89 CPC / Family Courts Act s.9
  referred_at   TIMESTAMPTZ,
  report_filed  BOOLEAN DEFAULT FALSE,
  outcome       TEXT
);

-- ---------- AI interactions (guardrailed) ----------
CREATE TABLE ai_interaction (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id            UUID REFERENCES mediation_case(id),
  query_redacted     TEXT,
  route_recommended  route_type,
  retrieved_doc_ids  TEXT[],                      -- RAG provenance
  is_advice          BOOLEAN DEFAULT FALSE,
  guardrail_flags    TEXT[],
  safety_triggered   BOOLEAN DEFAULT FALSE,
  human_escalated    BOOLEAN DEFAULT FALSE,
  model_version      TEXT,
  prompt_version     TEXT,
  created_at         TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- Immutable audit log ----------
CREATE TABLE audit_event (
  id            BIGSERIAL PRIMARY KEY,
  actor_id      UUID,
  actor_type    TEXT,                             -- party|neutral|staff|system
  case_id       UUID,
  action        TEXT NOT NULL,
  detail        JSONB,
  prev_hash     TEXT,
  row_hash      TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_audit_case ON audit_event(case_id);

-- ---------- SLA tracking ----------
CREATE TABLE case_sla (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES mediation_case(id) ON DELETE CASCADE,
  milestone     TEXT NOT NULL,
  due_at        TIMESTAMPTZ,
  met_at        TIMESTAMPTZ,
  breached      BOOLEAN DEFAULT FALSE
);

-- ---------- Retention (DPDP) ----------
CREATE TABLE retention_policy (
  entity        TEXT PRIMARY KEY,
  retain_months INT NOT NULL,
  legal_basis   TEXT
);
INSERT INTO retention_policy(entity,retain_months,legal_basis) VALUES
 ('mediation_case',84,'Mediation Act record-keeping'),
 ('caucus_note',12,'Confidential; minimal retention'),
 ('ai_interaction',12,'Model governance & audit'),
 ('audit_event',120,'Evidentiary integrity');

-- 21 tables, 11 enum types. Purge jobs enforce retention_policy (not shown).
