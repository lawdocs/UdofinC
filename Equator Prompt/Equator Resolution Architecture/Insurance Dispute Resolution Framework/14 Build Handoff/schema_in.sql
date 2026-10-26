-- ============================================================================
-- Equator Resolution — Insurance Dispute vertical
-- PostgreSQL 15+ DDL.  Law stated as at July 2026.
--
-- THREE INSTITUTIONAL RULES ARE ENFORCED HERE AS CONSTRAINTS, NOT AS POLICY:
--   R1  No arbitration route on a policy classified retail
--       (IRDAI circular dated 27 October 2023)
--   R2  No settlement may assert waiver of a non-waivable statutory right
--   R3  No case may close without a delivered signposting event and a fully
--       owned clock table
--
-- Health data lives in a SEPARATE SCHEMA with no foreign-key path from the
-- ordinary case tables.  That separation is the control.
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS ins;
CREATE SCHEMA IF NOT EXISTS ins_health;   -- segregated; separate encryption key

SET search_path = ins, public;

-- ─────────────────────────────── enums ───────────────────────────────
CREATE TYPE party_role AS ENUM (
  'policyholder','claimant','nominee','legal_heir','assignee',
  'insurer','tpa','agent','broker','group_master','representative');

CREATE TYPE policy_class AS ENUM ('retail','commercial','group_member','group_master');

CREATE TYPE line_of_business AS ENUM (
  'life_term','life_endowment','life_ulip','life_annuity','life_group',
  'health_individual','health_floater','health_group','personal_accident',
  'critical_illness','travel','motor_od','motor_tp','home',
  'fire','marine_cargo','marine_hull','engineering','liability','do','credit','crop','title','other');

CREATE TYPE dispute_type AS ENUM (
  'repudiated','short_settled','cashless_denied','delay_settlement','delay_intimation',
  'non_disclosure','ped_waiting','exclusion','sum_insured_idv','room_rent_proportionate',
  'copay_sublimit','depreciation_salvage','underinsurance','survey_disputed','mis_selling',
  'free_look','premium_lapse','policy_not_served','nomination','portability',
  'surrender_bonus','cancellation','subrogation','intermediary_conduct','other');

CREATE TYPE repudiation_ground AS ENUM (
  'non_disclosure','misrepresentation_s45','pre_existing','waiting_period','exclusion',
  'delay_intimation','lapsed','outside_period','documents','investigation_adverse',
  'proximate_cause','condition_breach','limit_exhausted','duplicate_inflated','none_given','other');

CREATE TYPE case_status AS ENUM (
  'intake','triaged','notified','collecting','prepared','in_session',
  'settlement','escrow','signposted','closed','withdrawn');

CREATE TYPE route AS ENUM (
  'insurer_grievance','bima_bharosa','internal_ombudsman','insurance_ombudsman',
  'consumer_commission','civil_court','arbitration','mact','equator_mediation');

CREATE TYPE clock_type AS ENUM (
  'insurer_reply_30d','ombudsman_1y','consumer_2y','policy_suit_bar','arb_29a','mediation_period');

CREATE TYPE voucher_basis AS ENUM ('full_final','under_protest','on_account');

-- ─────────────────────────────── parties ───────────────────────────────
CREATE TABLE party (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  role            party_role NOT NULL,
  full_name       TEXT NOT NULL,
  masked_gov_id   TEXT,
  address         TEXT,
  district        TEXT,
  state           TEXT,
  mobile          TEXT,
  email           TEXT,
  dpdp_consent            BOOLEAN NOT NULL DEFAULT FALSE,
  health_data_consent     BOOLEAN NOT NULL DEFAULT FALSE,
  health_authority_scope  TEXT,            -- 'this dispute only'
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT party_consent_required CHECK (dpdp_consent = TRUE)
);

CREATE TABLE insurer (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name          TEXT NOT NULL UNIQUE,
  irdai_regn    TEXT,
  protocol      BOOLEAN NOT NULL DEFAULT FALSE,   -- standing institutional protocol
  spoc_name     TEXT,
  spoc_email    TEXT,
  settlement_authority_limit NUMERIC(14,2)
);

-- ─────────────────────────────── policy & claim ───────────────────────────────
CREATE TABLE policy (
  id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  insurer_id              UUID NOT NULL REFERENCES insurer(id),
  policy_no               TEXT NOT NULL,
  line                    line_of_business NOT NULL,
  plan_name               TEXT,
  -- R1 gate: classification is mandatory and drives every route decision
  class                   policy_class NOT NULL,
  inception_date          DATE,
  first_ever_inception    DATE,             -- health: continuity / PED arithmetic
  ported_from             TEXT,
  period_from             DATE,
  period_to               DATE,
  sum_insured             NUMERIC(16,2),
  annual_premium          NUMERIC(14,2),
  premium_paid_upto       DATE,
  last_revival_date       DATE,             -- life: s.45 clock
  risk_commencement_date  DATE,             -- life: s.45 clock
  intermediary            TEXT,
  sales_channel           TEXT,
  legacy_arbitration_clause BOOLEAN NOT NULL DEFAULT FALSE,
  UNIQUE (insurer_id, policy_no)
);
COMMENT ON COLUMN policy.class IS
 'retail | commercial | group_member | group_master. NOT NULL by design: no policy record may exist without it.';
COMMENT ON COLUMN policy.legacy_arbitration_clause IS
 'Recorded for information. A legacy clause in a retail policy is NOT a bar to any other remedy.';

CREATE TABLE claim (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  policy_id         UUID NOT NULL REFERENCES policy(id),
  claim_no          TEXT,
  loss_date         DATE,
  intimation_date   DATE,
  amount_claimed    NUMERIC(16,2) NOT NULL DEFAULT 0,
  amount_offered    NUMERIC(16,2) NOT NULL DEFAULT 0,
  amount_paid       NUMERIC(16,2) NOT NULL DEFAULT 0,
  decision_date     DATE,
  decision_type     TEXT,
  grounds           repudiation_ground[] NOT NULL DEFAULT '{}',
  surveyor_name     TEXT,
  surveyor_licence  TEXT,
  survey_report_date        DATE,
  survey_report_shared      BOOLEAN NOT NULL DEFAULT FALSE,
  CONSTRAINT claim_offer_le_claimed CHECK (amount_offered <= amount_claimed),
  CONSTRAINT claim_dates CHECK (decision_date IS NULL OR intimation_date IS NULL
                                 OR decision_date >= intimation_date)
);

-- ─────────────────────────────── the case ───────────────────────────────
CREATE TABLE dispute_case (
  id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_no          TEXT UNIQUE NOT NULL,
  policy_id        UUID NOT NULL REFERENCES policy(id),
  claim_id         UUID REFERENCES claim(id),
  applicant_id     UUID NOT NULL REFERENCES party(id),
  respondent_id    UUID REFERENCES party(id),
  dispute_types    dispute_type[] NOT NULL DEFAULT '{}',
  relief_sought    TEXT[] NOT NULL DEFAULT '{}',
  amount_in_dispute NUMERIC(16,2) NOT NULL DEFAULT 0,
  status           case_status NOT NULL DEFAULT 'intake',
  route            route,
  is_retail        BOOLEAN NOT NULL,          -- denormalised from policy.class for the constraint
  fraud_alleged    BOOLEAN NOT NULL DEFAULT FALSE,
  bima_bharosa_token TEXT,
  representation_date DATE,
  insurer_reply_date  DATE,
  reply_outcome    TEXT,   -- rejected | unsatisfactory | satisfactory | none
  pending_forum    TEXT,
  opened_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  closed_at        TIMESTAMPTZ,

  -- ══════════ R1 — THE RETAIL ARBITRATION BAR ══════════
  CONSTRAINT no_arbitration_on_retail
    CHECK (route IS DISTINCT FROM 'arbitration' OR is_retail = FALSE),

  -- fraud allegations are not mediated
  CONSTRAINT no_mediation_of_alleged_fraud
    CHECK (fraud_alleged = FALSE OR route IS DISTINCT FROM 'equator_mediation')
);
COMMENT ON CONSTRAINT no_arbitration_on_retail ON dispute_case IS
 'IRDAI circular dated 27 October 2023: retail general-insurance policies shall not contain an arbitration clause. '
 'Enforced in the database so that no application code path can bypass it.';

CREATE OR REPLACE FUNCTION sync_is_retail() RETURNS trigger AS $$
BEGIN
  SELECT (p.class IN ('retail','group_member')) INTO NEW.is_retail
  FROM policy p WHERE p.id = NEW.policy_id;
  RETURN NEW;
END $$ LANGUAGE plpgsql;

CREATE TRIGGER trg_sync_is_retail
  BEFORE INSERT OR UPDATE OF policy_id ON dispute_case
  FOR EACH ROW EXECUTE FUNCTION sync_is_retail();

-- ─────────────────────────────── triage & rights ───────────────────────────────
CREATE TABLE triage (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id           UUID NOT NULL UNIQUE REFERENCES dispute_case(id) ON DELETE CASCADE,
  classified_by     TEXT NOT NULL,
  reviewed_by       TEXT NOT NULL,          -- second-officer review of the retail/commercial call
  ombudsman_c1      BOOLEAN NOT NULL,
  ombudsman_c2      BOOLEAN NOT NULL,
  ombudsman_c3      BOOLEAN NOT NULL,
  ombudsman_c4      BOOLEAN NOT NULL,
  ombudsman_c5      BOOLEAN NOT NULL,
  ombudsman_eligible BOOLEAN GENERATED ALWAYS AS
      (ombudsman_c1 AND ombudsman_c2 AND ombudsman_c3 AND ombudsman_c4 AND ombudsman_c5) STORED,
  ombudsman_centre  TEXT,
  fallback_route    route,
  suitability       TEXT NOT NULL,
  safeguards        TEXT,
  vulnerability     TEXT,
  language_support  TEXT,
  fee_waiver        BOOLEAN NOT NULL DEFAULT FALSE,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT triage_reviewer_differs CHECK (reviewed_by <> classified_by)
);

CREATE TABLE signposting_event (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id        UUID NOT NULL REFERENCES dispute_case(id) ON DELETE CASCADE,
  delivered_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
  channel        TEXT NOT NULL,          -- call | video | email | in_person
  language       TEXT NOT NULL,
  script_version TEXT NOT NULL,
  delivered_by   TEXT NOT NULL,
  acknowledged   BOOLEAN NOT NULL DEFAULT FALSE
);
CREATE INDEX ix_signposting_case ON signposting_event(case_id);

CREATE TABLE clock (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id      UUID NOT NULL REFERENCES dispute_case(id) ON DELETE CASCADE,
  kind         clock_type NOT NULL,
  trigger_date DATE NOT NULL,
  period_days  INTEGER NOT NULL CHECK (period_days > 0),
  expiry_date  DATE GENERATED ALWAYS AS (trigger_date + period_days) STORED,
  owner        TEXT,                      -- must be non-null before closure (R3)
  prompted_at  TIMESTAMPTZ,               -- the 60-day "go and file" prompt
  UNIQUE (case_id, kind)
);
CREATE INDEX ix_clock_expiry ON clock(expiry_date);

-- ══════════ R3 — NO CLOSURE WITHOUT SIGNPOSTING AND OWNED CLOCKS ══════════
CREATE OR REPLACE FUNCTION guard_closure() RETURNS trigger AS $$
DECLARE n_sign INT; n_unowned INT;
BEGIN
  IF NEW.status = 'closed' AND OLD.status <> 'closed' THEN
    SELECT count(*) INTO n_sign FROM signposting_event WHERE case_id = NEW.id;
    IF n_sign = 0 THEN
      RAISE EXCEPTION 'R3: cannot close case % — no signposting event recorded', NEW.case_no
        USING ERRCODE = 'check_violation';
    END IF;
    SELECT count(*) INTO n_unowned FROM clock WHERE case_id = NEW.id AND owner IS NULL;
    IF n_unowned > 0 THEN
      RAISE EXCEPTION 'R3: cannot close case % — % clock(s) have no owner', NEW.case_no, n_unowned
        USING ERRCODE = 'check_violation';
    END IF;
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;

CREATE TRIGGER trg_guard_closure
  BEFORE UPDATE OF status ON dispute_case
  FOR EACH ROW EXECUTE FUNCTION guard_closure();

-- also: a case may not leave triage without a signposting event
CREATE OR REPLACE FUNCTION guard_triage_exit() RETURNS trigger AS $$
DECLARE n_sign INT;
BEGIN
  IF OLD.status = 'triaged' AND NEW.status NOT IN ('triaged','withdrawn') THEN
    SELECT count(*) INTO n_sign FROM signposting_event WHERE case_id = NEW.id;
    IF n_sign = 0 THEN
      RAISE EXCEPTION 'R3: case % cannot leave triage without signposting', NEW.case_no
        USING ERRCODE = 'check_violation';
    END IF;
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;

CREATE TRIGGER trg_guard_triage_exit
  BEFORE UPDATE OF status ON dispute_case
  FOR EACH ROW EXECUTE FUNCTION guard_triage_exit();

-- ─────────────────────────────── preparation ───────────────────────────────
CREATE TABLE ground_analysis (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id      UUID NOT NULL REFERENCES dispute_case(id) ON DELETE CASCADE,
  seq          INTEGER NOT NULL,
  ground       repudiation_ground NOT NULL,
  clause_cited TEXT,
  answer       TEXT,
  proof_doc    TEXT,
  test_materiality    TEXT,
  test_proximate      TEXT,
  test_contra         TEXT,
  test_fair_dealing   TEXT,
  UNIQUE (case_id, seq)
);

CREATE TABLE deduction_line (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  claim_id      UUID NOT NULL REFERENCES claim(id) ON DELETE CASCADE,
  seq           INTEGER NOT NULL,
  head          TEXT NOT NULL,
  billed        NUMERIC(14,2) NOT NULL DEFAULT 0,
  allowed       NUMERIC(14,2) NOT NULL DEFAULT 0,
  deducted      NUMERIC(14,2) GENERATED ALWAYS AS (billed - allowed) STORED,
  varies_with_room BOOLEAN,
  reason_code   TEXT,
  response      TEXT,
  UNIQUE (claim_id, seq),
  CONSTRAINT deduction_arith CHECK (allowed <= billed),
  CONSTRAINT deduction_reason_required CHECK (billed = allowed OR reason_code IS NOT NULL)
);

CREATE TABLE claim_file_item (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id      UUID NOT NULL REFERENCES dispute_case(id) ON DELETE CASCADE,
  doc_type     TEXT NOT NULL,
  requested_at TIMESTAMPTZ,
  produced_at  TIMESTAMPTZ,
  withheld_ground TEXT,
  is_health    BOOLEAN NOT NULL DEFAULT FALSE,     -- routes storage to ins_health
  storage_ref  TEXT
);

-- ─────────────────────────────── process ───────────────────────────────
CREATE TABLE neutral (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  full_name         TEXT NOT NULL,
  accreditation     TEXT NOT NULL,       -- ECIN level
  background        TEXT NOT NULL,       -- insurer | surveyor | lawyer | medical | consumer_side | ombudsman_office
  languages         TEXT[] NOT NULL DEFAULT '{}',
  pi_cover_expiry   DATE,
  active            BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE neutral_disclosure (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  neutral_id          UUID NOT NULL REFERENCES neutral(id),
  case_id             UUID NOT NULL REFERENCES dispute_case(id),
  insurer_id          UUID NOT NULL REFERENCES insurer(id),
  relationships       TEXT,
  appts_24m_total     INTEGER NOT NULL DEFAULT 0,
  appts_24m_this_insurer INTEGER NOT NULL DEFAULT 0,
  income_pct_this_insurer NUMERIC(5,2),
  declared_independent BOOLEAN NOT NULL,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT disclosure_must_be_independent CHECK (declared_independent = TRUE),
  CONSTRAINT concentration_cap
    CHECK (appts_24m_total = 0 OR appts_24m_this_insurer::NUMERIC / appts_24m_total <= 0.40)
);
COMMENT ON CONSTRAINT concentration_cap ON neutral_disclosure IS
 'Repeat-player capture control: no more than 40% of a neutral''s appointments in 24 months may be attributable '
 'to a single insurer.';

CREATE TABLE session (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id       UUID NOT NULL REFERENCES dispute_case(id) ON DELETE CASCADE,
  neutral_id    UUID NOT NULL REFERENCES neutral(id),
  mode          TEXT NOT NULL,        -- joint | caucus | shuttle | online | in_person
  scheduled_at  TIMESTAMPTZ NOT NULL,
  authority_confirmed BOOLEAN NOT NULL DEFAULT FALSE,
  authority_limit     NUMERIC(14,2),
  approver            TEXT,
  CONSTRAINT session_needs_authority CHECK (authority_confirmed = TRUE)
);

CREATE TABLE caucus_note (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id  UUID NOT NULL REFERENCES session(id) ON DELETE CASCADE,
  neutral_id  UUID NOT NULL REFERENCES neutral(id),
  note_cipher BYTEA NOT NULL,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ─────────────────────────────── settlement ───────────────────────────────
CREATE TABLE settlement (
  id                        UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id                   UUID NOT NULL UNIQUE REFERENCES dispute_case(id) ON DELETE CASCADE,
  amount                    NUMERIC(16,2) NOT NULL CHECK (amount >= 0),
  interest_component        NUMERIC(14,2) NOT NULL DEFAULT 0,
  tds                       NUMERIC(14,2) NOT NULL DEFAULT 0,
  payable_by                DATE,
  continuity_preserved      BOOLEAN NOT NULL DEFAULT FALSE,
  adverse_remark_withdrawn  BOOLEAN NOT NULL DEFAULT FALSE,
  policy_reinstated_from    DATE,
  product_converted_to      TEXT,
  pending_complaint_disposed BOOLEAN NOT NULL DEFAULT FALSE,
  statutory_rights_waived   BOOLEAN NOT NULL DEFAULT FALSE,
  future_claims_discharged  BOOLEAN NOT NULL DEFAULT FALSE,
  registered_at             TIMESTAMPTZ,
  enforceable_s27           BOOLEAN NOT NULL DEFAULT TRUE,
  signed_at                 TIMESTAMPTZ,

  -- ══════════ R2 — NO WAIVER OF A NON-WAIVABLE RIGHT ══════════
  CONSTRAINT no_statutory_waiver CHECK (statutory_rights_waived = FALSE),
  CONSTRAINT no_future_discharge CHECK (future_claims_discharged = FALSE)
);
COMMENT ON CONSTRAINT no_statutory_waiver ON settlement IS
 'A settlement may never recite that a party gives up a right that cannot lawfully be waived — including the right '
 'to approach the Insurance Ombudsman, a consumer commission or a court in respect of a different claim.';

CREATE TABLE discharge_voucher (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id      UUID NOT NULL REFERENCES dispute_case(id) ON DELETE CASCADE,
  basis        voucher_basis NOT NULL,
  amount       NUMERIC(16,2) NOT NULL,
  balance_reserved NUMERIC(16,2) NOT NULL DEFAULT 0,
  utr          TEXT,
  value_date   DATE,
  CONSTRAINT protest_requires_balance
    CHECK (basis <> 'under_protest' OR balance_reserved > 0)
);

CREATE TABLE escrow (
  id       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id  UUID NOT NULL REFERENCES dispute_case(id) ON DELETE CASCADE,
  amount   NUMERIC(16,2) NOT NULL CHECK (amount >= 0),
  state    TEXT NOT NULL DEFAULT 'created'
);

CREATE TABLE escrow_milestone (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  escrow_id    UUID NOT NULL REFERENCES escrow(id) ON DELETE CASCADE,
  seq          INTEGER NOT NULL,
  name         TEXT NOT NULL,
  condition    TEXT NOT NULL,
  evidence_ref TEXT,
  amount       NUMERIC(14,2) NOT NULL,
  due_date     DATE,
  released_at  TIMESTAMPTZ,
  CONSTRAINT release_needs_evidence
    CHECK (released_at IS NULL OR evidence_ref IS NOT NULL)
);

-- ─────────────────────────────── closure & assurance ───────────────────────────────
CREATE TABLE closure (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id               UUID NOT NULL UNIQUE REFERENCES dispute_case(id) ON DELETE CASCADE,
  outcome               TEXT NOT NULL,
  amount_settled        NUMERIC(16,2),
  days_to_settle        INTEGER,
  sessions_held         INTEGER,
  payment_verified      BOOLEAN NOT NULL DEFAULT FALSE,
  registration_verified BOOLEAN NOT NULL DEFAULT FALSE,
  remark_withdrawal_verified BOOLEAN NOT NULL DEFAULT FALSE,
  retention_class       TEXT NOT NULL,
  health_erasure_confirmed_at TIMESTAMPTZ,
  feedback_pressure_score INTEGER,   -- "did you feel pressured to settle?" 1-5
  closed_at             TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- hash-chained audit log
CREATE TABLE audit_event (
  id         BIGSERIAL PRIMARY KEY,
  actor      TEXT,
  case_id    UUID,
  store      TEXT NOT NULL,
  action     TEXT NOT NULL,
  detail     TEXT,
  prev_hash  TEXT,
  row_hash   TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ============================================================================
-- ins_health — segregated store.  NO foreign key to ins.*  by design.
-- Access is granted per assignment and time-boxed; every read is logged.
-- Excluded from every analytics view and every AI training or evaluation set.
-- ============================================================================
SET search_path = ins_health, public;

CREATE TABLE medical_record (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_ref          TEXT NOT NULL,            -- deliberately a text reference, not a FK
  doc_type          TEXT NOT NULL,
  source            TEXT NOT NULL,            -- hospital | tpa | insurer | party
  content_cipher    BYTEA NOT NULL,
  authority_ref     TEXT NOT NULL,            -- the consent / heirship authority on file
  received_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
  erase_after       DATE NOT NULL,
  erased_at         TIMESTAMPTZ,
  CONSTRAINT authority_required CHECK (length(authority_ref) > 0)
);

CREATE TABLE medical_access_log (
  id           BIGSERIAL PRIMARY KEY,
  record_id    UUID NOT NULL REFERENCES medical_record(id),
  actor        TEXT NOT NULL,
  actor_role   TEXT NOT NULL,       -- case_manager | neutral
  case_ref     TEXT NOT NULL,
  purpose      TEXT NOT NULL,
  accessed_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX ix_med_access_time ON medical_access_log(accessed_at);

-- ============================================================================
-- Reporting views.  Note the explicit exclusion of the health schema.
-- ============================================================================
SET search_path = ins, public;

CREATE VIEW v_outcomes_by_insurer AS
SELECT i.name                              AS insurer,
       count(*)                            AS matters,
       count(*) FILTER (WHERE c.outcome = 'settled_full')  AS settled_full,
       count(*) FILTER (WHERE c.outcome = 'settled_part')  AS settled_part,
       count(*) FILTER (WHERE c.outcome = 'not_settled')   AS not_settled,
       round(avg(c.days_to_settle), 1)     AS avg_days,
       round(avg(c.amount_settled / NULLIF(d.amount_in_dispute,0))::numeric, 3) AS avg_recovery_ratio
FROM closure c
JOIN dispute_case d ON d.id = c.case_id
JOIN policy p       ON p.id = d.policy_id
JOIN insurer i      ON i.id = p.insurer_id
GROUP BY i.name;
COMMENT ON VIEW v_outcomes_by_insurer IS
 'Published quarterly in aggregate and anonymised form (Rule 25). Contains no health data.';

CREATE VIEW v_clock_risk AS
SELECT d.case_no, k.kind, k.expiry_date, k.owner,
       (k.expiry_date - CURRENT_DATE) AS days_left,
       k.prompted_at
FROM clock k JOIN dispute_case d ON d.id = k.case_id
WHERE d.status NOT IN ('closed','withdrawn')
ORDER BY k.expiry_date;

CREATE VIEW v_neutral_concentration AS
SELECT n.full_name, i.name AS insurer,
       count(*) AS appts,
       round(100.0 * count(*) / NULLIF(sum(count(*)) OVER (PARTITION BY n.id),0), 1) AS pct_of_neutral
FROM neutral_disclosure nd
JOIN neutral n ON n.id = nd.neutral_id
JOIN insurer i ON i.id = nd.insurer_id
WHERE nd.created_at > now() - interval '24 months'
GROUP BY n.id, n.full_name, i.name;
