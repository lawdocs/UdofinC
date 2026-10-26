-- =====================================================================
-- Equator Resolution — Financial & Loan Dispute Platform
-- PostgreSQL schema (draft for engineering; settle with security & counsel)
-- Principles: DPDP-aware (masked IDs), auditable (immutable events),
-- money-safe (escrow + reconciliation). Confirm before build.
-- =====================================================================
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ---------- Enumerated types ----------
CREATE TYPE party_role      AS ENUM ('borrower','guarantor','co_borrower','lender_rep');
CREATE TYPE lender_type     AS ENUM ('bank','nbfc','hfc','mfi','fintech_lsp','arc','p2p','card_issuer');
CREATE TYPE loan_type       AS ENUM ('personal','vehicle','home','gold','education','business_msme','credit_card','bnpl','microfinance','p2p');
CREATE TYPE dispute_type    AS ENUM ('loan_default_ots','cheque_138','wrong_charges','digital_lending','recovery_harassment','credit_bureau','guarantee','secured_debt');
CREATE TYPE case_status     AS ENUM ('intake','triaged','notice_served','response','neutral_appointed','in_session','settlement','escrow','closed','withdrawn','signposted');
CREATE TYPE route_type      AS ENUM ('mediation_ots','ni138','ombudsman','drt_sarfaesi','consumer','lok_adalat','msme_samadhaan');
CREATE TYPE neutral_grade   AS ENUM ('A','B','C');
CREATE TYPE kyc_status      AS ENUM ('pending','verified','failed');
CREATE TYPE bureau_name     AS ENUM ('cibil','crif','experian','equifax');
CREATE TYPE bureau_status   AS ENUM ('settled','closed');
CREATE TYPE escrow_state    AS ENUM ('created','funded','partially_released','released','refunded');

-- ---------- Core parties ----------
CREATE TABLE party (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  role          party_role NOT NULL,
  full_name     TEXT NOT NULL,
  masked_gov_id TEXT,                     -- store masked/tokenised; never raw
  email_hash    TEXT,
  phone_hash    TEXT,
  kyc_status    kyc_status NOT NULL DEFAULT 'pending',
  is_vulnerable BOOLEAN DEFAULT FALSE,    -- flagged for extra care
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE lender (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name          TEXT NOT NULL,
  type          lender_type NOT NULL,
  sla_config    JSONB DEFAULT '{}'::jsonb,
  panel_active  BOOLEAN DEFAULT TRUE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE lender_authorised_officer (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lender_id     UUID NOT NULL REFERENCES lender(id),
  party_id      UUID NOT NULL REFERENCES party(id),
  settlement_limit NUMERIC(16,2),         -- board-policy delegated authority
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- Neutrals ----------
CREATE TABLE neutral (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  party_id      UUID REFERENCES party(id),
  full_name     TEXT NOT NULL,
  grade         neutral_grade NOT NULL,
  expertise     TEXT[],                   -- e.g. {'banking','sarfaesi','ni138'}
  languages     TEXT[],
  rubric_score  INT CHECK (rubric_score BETWEEN 0 AND 100),
  code_signed   BOOLEAN DEFAULT FALSE,
  active        BOOLEAN DEFAULT TRUE
);

-- ---------- Case ----------
CREATE TABLE dispute_case (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_number       TEXT UNIQUE NOT NULL,
  initiator_role    party_role NOT NULL,
  dispute_type      dispute_type NOT NULL,
  loan_type         loan_type,
  lender_id         UUID REFERENCES lender(id),
  borrower_id       UUID REFERENCES party(id),
  amount_in_dispute NUMERIC(16,2),
  secured           BOOLEAN DEFAULT FALSE,
  status            case_status NOT NULL DEFAULT 'intake',
  recommended_route route_type,
  neutral_id        UUID REFERENCES neutral(id),
  facts             TEXT,
  relief_sought     TEXT[],
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  closed_at         TIMESTAMPTZ
);
CREATE INDEX idx_case_status ON dispute_case(status);
CREATE INDEX idx_case_lender ON dispute_case(lender_id);
CREATE INDEX idx_case_type   ON dispute_case(dispute_type);

CREATE TABLE case_party (
  case_id  UUID NOT NULL REFERENCES dispute_case(id),
  party_id UUID NOT NULL REFERENCES party(id),
  role     party_role NOT NULL,
  PRIMARY KEY (case_id, party_id)
);

CREATE TABLE case_triage (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id        UUID NOT NULL REFERENCES dispute_case(id),
  route          route_type NOT NULL,
  non_mediable   BOOLEAN DEFAULT FALSE,
  parallel_med   BOOLEAN DEFAULT FALSE,
  rationale      TEXT,
  created_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- Appointment & disclosure ----------
CREATE TABLE appointment (
  id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id          UUID NOT NULL REFERENCES dispute_case(id),
  neutral_id       UUID NOT NULL REFERENCES neutral(id),
  conflict_checked BOOLEAN DEFAULT FALSE,
  disclosure_signed BOOLEAN DEFAULT FALSE,
  appointed_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- OTS estimate & settlement ----------
CREATE TABLE ots_estimate (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id            UUID NOT NULL REFERENCES dispute_case(id),
  principal          NUMERIC(16,2),
  accrued_interest   NUMERIC(16,2),
  penal_charges      NUMERIC(16,2),
  interest_waiver_pct NUMERIC(5,4),
  penal_waiver_pct   NUMERIC(5,4),
  discount_pct       NUMERIC(5,4),
  suggested_ots      NUMERIC(16,2),
  recovery_pct       NUMERIC(5,4),
  created_at         TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE settlement (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id             UUID NOT NULL REFERENCES dispute_case(id),
  settled_amount      NUMERIC(16,2) NOT NULL,
  interest_waiver     NUMERIC(16,2) DEFAULT 0,
  penal_waiver        NUMERIC(16,2) DEFAULT 0,
  noc_on_final        BOOLEAN DEFAULT TRUE,
  bureau_status       bureau_status,
  enforceable_decree  BOOLEAN DEFAULT TRUE,
  is_ni138_compounded BOOLEAN DEFAULT FALSE,
  lok_adalat_recorded BOOLEAN DEFAULT FALSE,
  signed_at           TIMESTAMPTZ,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE settlement_instalment (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  settlement_id UUID NOT NULL REFERENCES settlement(id),
  due_date      DATE NOT NULL,
  amount        NUMERIC(16,2) NOT NULL,
  paid          BOOLEAN DEFAULT FALSE,
  paid_at       TIMESTAMPTZ
);

-- ---------- Escrow & payments ----------
CREATE TABLE escrow (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES dispute_case(id),
  escrow_bank   TEXT NOT NULL,
  amount        NUMERIC(16,2) NOT NULL,
  state         escrow_state NOT NULL DEFAULT 'created',
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE escrow_milestone (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  escrow_id     UUID NOT NULL REFERENCES escrow(id),
  name          TEXT NOT NULL,
  condition     TEXT,
  amount        NUMERIC(16,2) NOT NULL,
  released      BOOLEAN DEFAULT FALSE,
  released_at   TIMESTAMPTZ
);

CREATE TABLE payment_txn (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES dispute_case(id),
  escrow_id     UUID REFERENCES escrow(id),
  method        TEXT,                     -- enach|upi|imps|rtgs|neft
  direction     TEXT,                     -- in|out
  amount        NUMERIC(16,2) NOT NULL,
  reference     TEXT,
  reconciled    BOOLEAN DEFAULT FALSE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- Documents / e-Sign / e-Stamp ----------
CREATE TABLE document (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES dispute_case(id),
  form_ref      TEXT,                     -- e.g. F-L07, F-L12
  kind          TEXT,
  storage_uri   TEXT,
  sha256        TEXT,                     -- integrity
  esigned       BOOLEAN DEFAULT FALSE,
  estamped      BOOLEAN DEFAULT FALSE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- Grievance / forum handoff ----------
CREATE TABLE grievance (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES dispute_case(id),
  kind          TEXT,                     -- harassment|digital_lending|charges
  detail        TEXT,
  escalated     BOOLEAN DEFAULT FALSE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE forum_handoff (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES dispute_case(id),
  forum         route_type NOT NULL,
  reference     TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE bureau_update (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES dispute_case(id),
  bureau        bureau_name NOT NULL,
  status        bureau_status NOT NULL,
  filed_at      TIMESTAMPTZ,
  confirmed     BOOLEAN DEFAULT FALSE
);

-- ---------- AI interactions (guardrailed) ----------
CREATE TABLE ai_interaction (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID REFERENCES dispute_case(id),
  query         TEXT,
  route_recommended route_type,
  is_advice     BOOLEAN DEFAULT FALSE,
  guardrail_flags TEXT[],
  escalation_offered BOOLEAN DEFAULT FALSE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- Immutable audit log ----------
CREATE TABLE audit_event (
  id            BIGSERIAL PRIMARY KEY,
  actor_id      UUID,
  actor_type    TEXT,                     -- staff|neutral|party|system
  case_id       UUID,
  action        TEXT NOT NULL,
  detail        JSONB,
  prev_hash     TEXT,                     -- tamper-evident chaining
  row_hash      TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_audit_case ON audit_event(case_id);

-- ---------- SLA tracking ----------
CREATE TABLE case_sla (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES dispute_case(id),
  milestone     TEXT NOT NULL,            -- acknowledge|notice|appoint|session|settle|close
  due_at        TIMESTAMPTZ,
  met_at        TIMESTAMPTZ,
  breached      BOOLEAN DEFAULT FALSE
);

-- 21 tables, 11 enum types. Retention & purge jobs enforce the DPDP schedule (not shown).
