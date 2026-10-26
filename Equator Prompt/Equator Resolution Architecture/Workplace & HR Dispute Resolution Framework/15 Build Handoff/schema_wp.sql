-- =====================================================================
-- Equator Resolution — Workplace & HR Dispute Platform
-- PostgreSQL schema (DDL). Draft for engineering; settle with security & counsel.
-- Principles: SEALED POSH mode (physically separate, access-controlled),
-- statutory dues never waived, DPDP-aware, auditable.
-- Statutory anchors: POSH Act 2013 (s.4 IC incl. external member, s.10 conciliation,
-- 90-day inquiry, s.16 confidentiality); the four Labour Codes (in force 21 Nov 2025);
-- Mediation Act 2023 (s.27); DPDP Act 2023.
-- =====================================================================
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ---------- Enumerated types ----------
CREATE TYPE wp_party_role    AS ENUM ('employee','ex_employee','employer','hr_rep','contractor','gig_worker','union_rep','counsel');
CREATE TYPE wp_dispute_type  AS ENUM ('wage_dues','full_and_final','wrongful_termination','notice_bond','benefits_gratuity_pf_esi','leave_attendance','non_compete','harassment_non_posh','posh','discrimination','grievance','retrenchment_layoff','contractor_gig');
CREATE TYPE wp_case_status   AS ENUM ('intake','triaged','posh_sealed','notice_served','response','neutral_appointed','in_session','settlement','escrow','signposted','closed','withdrawn');
CREATE TYPE wp_route         AS ENUM ('mediation','posh_internal_committee','grc_ir_code','statutory_forum','police','not_suitable');
CREATE TYPE wp_estab_size    AS ENUM ('lt_10','10_49','50_99','100_299','300_plus');
CREATE TYPE wp_neutral_grade AS ENUM ('A','B','C');
CREATE TYPE wp_escrow_state  AS ENUM ('created','funded','partially_released','released','refunded');
CREATE TYPE posh_stage       AS ENUM ('received','conciliation_requested','conciliation_recorded','inquiry','report_issued','employer_action','appeal','closed');
CREATE TYPE posh_finding     AS ENUM ('proved','not_proved','malicious');

-- ---------- Parties & employers ----------
CREATE TABLE wp_party (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  role            wp_party_role NOT NULL,
  full_name       TEXT NOT NULL,
  masked_gov_id   TEXT,
  email_hash      TEXT,
  phone_hash      TEXT,
  preferred_language TEXT DEFAULT 'en',
  needs_support   BOOLEAN DEFAULT FALSE,
  kyc_verified    BOOLEAN DEFAULT FALSE,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE employer (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name              TEXT NOT NULL,
  estab_size        wp_estab_size NOT NULL,
  sector            TEXT,
  posh_subscriber   BOOLEAN DEFAULT FALSE,
  ic_constituted    BOOLEAN DEFAULT FALSE,       -- POSH s.4 compliance flag
  grc_constituted   BOOLEAN DEFAULT FALSE,       -- IR Code grievance committee
  panel_sla         JSONB DEFAULT '{}'::jsonb,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);
COMMENT ON COLUMN employer.ic_constituted IS 'POSH s.4: mandatory where 10 or more workers';

CREATE TABLE employment_record (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  party_id        UUID NOT NULL REFERENCES wp_party(id),
  employer_id     UUID NOT NULL REFERENCES employer(id),
  designation     TEXT,
  date_of_joining DATE,
  date_of_exit    DATE,
  monthly_wages   NUMERIC(14,2),                  -- Code on Wages definition
  wages_pct_of_ctc NUMERIC(5,4),                  -- must be >= 0.50 for statutory computation
  appointment_letter_on_file BOOLEAN DEFAULT FALSE,
  CONSTRAINT chk_exit CHECK (date_of_exit IS NULL OR date_of_joining IS NULL OR date_of_exit >= date_of_joining)
);
COMMENT ON COLUMN employment_record.wages_pct_of_ctc IS 'Code on Wages 2019: where excluded components exceed 50%, excess is added back';

-- ---------- Case (NON-POSH matters live here) ----------
CREATE TABLE wp_case (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_number       TEXT UNIQUE NOT NULL,
  dispute_types     wp_dispute_type[] NOT NULL,
  status            wp_case_status NOT NULL DEFAULT 'intake',
  route             wp_route,
  employer_id       UUID REFERENCES employer(id),
  employee_id       UUID REFERENCES wp_party(id),
  initiator_role    wp_party_role NOT NULL,
  amount_in_dispute NUMERIC(16,2),
  is_posh           BOOLEAN DEFAULT FALSE,        -- if true, substantive data lives ONLY in posh schema
  opened_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
  closed_at         TIMESTAMPTZ,
  CONSTRAINT chk_posh_sealed CHECK (NOT is_posh OR status IN ('posh_sealed','signposted','closed'))
);
CREATE INDEX idx_wp_case_status ON wp_case(status);
CREATE INDEX idx_wp_case_employer ON wp_case(employer_id);
COMMENT ON CONSTRAINT chk_posh_sealed ON wp_case IS 'A POSH matter may never sit in an ordinary mediation state';

-- ---------- Triage ----------
CREATE TABLE wp_triage (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES wp_case(id) ON DELETE CASCADE,
  route         wp_route NOT NULL,
  rationale     TEXT,
  safety_flag   BOOLEAN DEFAULT FALSE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- Panel & appointment ----------
CREATE TABLE wp_neutral (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  full_name       TEXT NOT NULL,
  grade           wp_neutral_grade NOT NULL,
  expertise       TEXT[],
  languages       TEXT[],
  gender          TEXT,
  posh_endorsed   BOOLEAN DEFAULT FALSE,          -- required to serve as external IC member
  rubric_score    INT CHECK (rubric_score BETWEEN 0 AND 100),
  code_signed     BOOLEAN DEFAULT FALSE,
  active          BOOLEAN DEFAULT TRUE
);

CREATE TABLE wp_appointment (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id           UUID NOT NULL REFERENCES wp_case(id) ON DELETE CASCADE,
  neutral_id        UUID NOT NULL REFERENCES wp_neutral(id),
  conflict_checked  BOOLEAN DEFAULT FALSE,
  disclosure_signed BOOLEAN DEFAULT FALSE,
  structural_conflict_disclosed BOOLEAN DEFAULT FALSE,  -- Rule 7: employer also a POSH subscriber
  appointed_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
COMMENT ON COLUMN wp_appointment.structural_conflict_disclosed IS 'Set where Equator also supplies an external IC member to this employer';

-- ---------- Sessions & sealed notes ----------
CREATE TABLE wp_session (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES wp_case(id) ON DELETE CASCADE,
  mode          TEXT CHECK (mode IN ('joint','caucus','shuttle','online','in_person')),
  scheduled_at  TIMESTAMPTZ NOT NULL,
  attended      BOOLEAN DEFAULT FALSE
);

CREATE TABLE wp_caucus_note (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id    UUID NOT NULL REFERENCES wp_session(id) ON DELETE CASCADE,
  neutral_id    UUID NOT NULL REFERENCES wp_neutral(id),
  note_cipher   BYTEA NOT NULL,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- Settlement & full-and-final ----------
CREATE TABLE wp_settlement (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id               UUID NOT NULL REFERENCES wp_case(id) ON DELETE CASCADE,
  gross_earnings        NUMERIC(16,2),
  total_deductions      NUMERIC(16,2),
  net_payable           NUMERIC(16,2),
  gratuity_amount       NUMERIC(16,2) DEFAULT 0,
  pf_settled            BOOLEAN DEFAULT FALSE,
  statutory_dues_waived BOOLEAN DEFAULT FALSE,
  relieving_letter      BOOLEAN DEFAULT FALSE,
  experience_letter     BOOLEAN DEFAULT FALSE,
  assets_returned       BOOLEAN DEFAULT FALSE,
  enforceable_s27       BOOLEAN DEFAULT TRUE,
  signed_at             TIMESTAMPTZ,
  CONSTRAINT chk_no_waiver CHECK (statutory_dues_waived = FALSE)
);
COMMENT ON CONSTRAINT chk_no_waiver ON wp_settlement IS 'Statutory dues (gratuity/PF/ESI) are paid, never waived — enforced at the database';

CREATE TABLE wp_settlement_instalment (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  settlement_id UUID NOT NULL REFERENCES wp_settlement(id) ON DELETE CASCADE,
  due_date      DATE NOT NULL,
  amount        NUMERIC(16,2) NOT NULL,
  paid          BOOLEAN DEFAULT FALSE,
  paid_at       TIMESTAMPTZ
);

-- ---------- Escrow ----------
CREATE TABLE wp_escrow (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES wp_case(id) ON DELETE CASCADE,
  escrow_bank   TEXT NOT NULL,
  amount        NUMERIC(16,2) NOT NULL CHECK (amount >= 0),
  state         wp_escrow_state NOT NULL DEFAULT 'created'
);

CREATE TABLE wp_escrow_milestone (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  escrow_id     UUID NOT NULL REFERENCES wp_escrow(id) ON DELETE CASCADE,
  name          TEXT NOT NULL,
  condition     TEXT,
  amount        NUMERIC(16,2) NOT NULL,
  released      BOOLEAN DEFAULT FALSE,
  released_at   TIMESTAMPTZ
);

-- ---------- Documents ----------
CREATE TABLE wp_document (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES wp_case(id) ON DELETE CASCADE,
  form_ref      TEXT,                              -- F-W01 .. F-W20
  kind          TEXT,
  storage_uri   TEXT NOT NULL,
  sha256        TEXT NOT NULL,
  esigned       BOOLEAN DEFAULT FALSE,
  estamped      BOOLEAN DEFAULT FALSE,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- =====================================================================
-- SEALED POSH SCHEMA — physically separated; access via a distinct role only.
-- No foreign key exposes complainant identity to the ordinary case tables.
-- =====================================================================
CREATE SCHEMA IF NOT EXISTS posh;
COMMENT ON SCHEMA posh IS 'POSH Act s.16 confidentiality: separate schema, separate DB role, no cross-schema joins to wp_case detail';

CREATE TABLE posh.complaint (
  id                   UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  complaint_number     TEXT UNIQUE NOT NULL,
  employer_id          UUID NOT NULL,             -- deliberately NOT a FK: no join path from ordinary schema
  received_on          DATE NOT NULL,
  incident_last_on     DATE,
  within_3_months      BOOLEAN,
  extension_granted    BOOLEAN DEFAULT FALSE,
  stage                posh_stage NOT NULL DEFAULT 'received',
  complainant_cipher   BYTEA NOT NULL,            -- encrypted identity
  respondent_cipher    BYTEA NOT NULL,
  particulars_cipher   BYTEA NOT NULL,
  created_at           TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE posh.internal_committee (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  employer_id       UUID NOT NULL,
  presiding_officer TEXT NOT NULL,
  member_count      INT NOT NULL CHECK (member_count >= 2),
  women_members     INT NOT NULL,
  external_member_id UUID,                        -- Equator-supplied where applicable
  constituted_on    DATE NOT NULL,
  term_expires_on   DATE,
  CONSTRAINT chk_external CHECK (external_member_id IS NOT NULL),
  CONSTRAINT chk_women_half CHECK (women_members * 2 >= member_count + 1)
);
COMMENT ON CONSTRAINT chk_external ON posh.internal_committee IS 'POSH s.4: at least one external member is mandatory';
COMMENT ON CONSTRAINT chk_women_half ON posh.internal_committee IS 'POSH s.4: at least half the members shall be women (incl. Presiding Officer)';

CREATE TABLE posh.conciliation (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  complaint_id          UUID NOT NULL REFERENCES posh.complaint(id) ON DELETE CASCADE,
  requested_by_woman    BOOLEAN NOT NULL,
  monetary_basis        BOOLEAN NOT NULL DEFAULT FALSE,
  terms_cipher          BYTEA,
  recorded_on           DATE,
  forwarded_to_employer BOOLEAN DEFAULT FALSE,
  respondent_complied   BOOLEAN,
  CONSTRAINT chk_woman_request CHECK (requested_by_woman = TRUE),
  CONSTRAINT chk_no_money CHECK (monetary_basis = FALSE)
);
COMMENT ON CONSTRAINT chk_woman_request ON posh.conciliation IS 'POSH s.10: only at the aggrieved womans request — never IC-initiated or respondent-requested';
COMMENT ON CONSTRAINT chk_no_money ON posh.conciliation IS 'POSH s.10: no monetary settlement may be the basis of conciliation';

CREATE TABLE posh.inquiry (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  complaint_id      UUID NOT NULL REFERENCES posh.complaint(id) ON DELETE CASCADE,
  commenced_on      DATE NOT NULL,
  due_on            DATE GENERATED ALWAYS AS (commenced_on + INTERVAL '90 days') STORED,
  respondent_reply_due DATE,
  concluded_on      DATE,
  report_due_on     DATE,
  report_issued_on  DATE,
  finding           posh_finding,
  reasons_cipher    BYTEA,
  interim_relief    TEXT,
  CONSTRAINT chk_within_90 CHECK (concluded_on IS NULL OR concluded_on <= commenced_on + INTERVAL '90 days')
);
COMMENT ON CONSTRAINT chk_within_90 ON posh.inquiry IS 'POSH: inquiry to be completed within 90 days';

CREATE TABLE posh.employer_action (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  complaint_id   UUID NOT NULL REFERENCES posh.complaint(id) ON DELETE CASCADE,
  report_date    DATE NOT NULL,
  action_due_on  DATE GENERATED ALWAYS AS (report_date + INTERVAL '60 days') STORED,
  action_taken   TEXT,
  compensation   NUMERIC(16,2),
  actioned_on    DATE,
  appeal_filed   BOOLEAN DEFAULT FALSE
);
COMMENT ON TABLE posh.employer_action IS 'Employer must act within 60 days; appeal window 90 days';

CREATE TABLE posh.annual_report (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  employer_id        UUID NOT NULL,
  calendar_year      INT NOT NULL,
  complaints_received INT DEFAULT 0,
  complaints_disposed INT DEFAULT 0,
  pending_over_90d   INT DEFAULT 0,
  awareness_sessions INT DEFAULT 0,
  filed_with_employer BOOLEAN DEFAULT FALSE,
  filed_with_district_officer BOOLEAN DEFAULT FALSE,
  UNIQUE (employer_id, calendar_year)
);

-- ---------- Governance ----------
CREATE TABLE wp_ai_interaction (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id           UUID REFERENCES wp_case(id),
  query_redacted    TEXT,
  route_recommended wp_route,
  posh_detected     BOOLEAN DEFAULT FALSE,
  is_advice         BOOLEAN DEFAULT FALSE,
  guardrail_flags   TEXT[],
  human_escalated   BOOLEAN DEFAULT FALSE,
  model_version     TEXT,
  prompt_version    TEXT,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE wp_audit_event (
  id            BIGSERIAL PRIMARY KEY,
  actor_id      UUID,
  actor_type    TEXT,
  case_id       UUID,
  schema_touched TEXT,                             -- 'public' | 'posh'
  action        TEXT NOT NULL,
  detail        JSONB,
  prev_hash     TEXT,
  row_hash      TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_wp_audit_case ON wp_audit_event(case_id);

CREATE TABLE wp_retention_policy (
  entity        TEXT PRIMARY KEY,
  retain_months INT NOT NULL,
  legal_basis   TEXT
);
INSERT INTO wp_retention_policy(entity,retain_months,legal_basis) VALUES
 ('wp_case',84,'Mediation Act record-keeping'),
 ('posh.complaint',84,'POSH records & annual reporting'),
 ('wp_caucus_note',12,'Confidentiality — minimal retention'),
 ('wp_ai_interaction',12,'Model governance'),
 ('wp_audit_event',120,'Evidentiary integrity');

-- 21 tables (14 public + 6 posh + retention), 9 enum types.
-- Access control: grant the 'posh_role' SELECT/INSERT on schema posh only;
-- ordinary application roles must have NO privileges on schema posh.
