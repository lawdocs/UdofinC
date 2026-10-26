-- EQR-32 · Schema DDL Supplement (PostgreSQL) — extends EQR-21_Schema_DDL.sql
-- v1.0 · 9 July 2026 · Confidential.

CREATE TABLE users (
  user_id text PRIMARY KEY, subject_id text, kind text CHECK (kind IN ('party','neutral','staff','machine')),
  mfa_enabled boolean DEFAULT false, created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE consents (
  consent_id text PRIMARY KEY, subject_id text NOT NULL, purpose text NOT NULL,
  granted boolean NOT NULL, granted_at timestamptz, withdrawn_at timestamptz
);
CREATE TABLE empanelments (
  empanelment_id text PRIMARY KEY, neutral_id text NOT NULL REFERENCES neutrals(neutral_id),
  panels text[] NOT NULL, grade text, status text DEFAULT 'active', cert_ref text
);
CREATE TABLE conflict_graph (
  node_id text PRIMARY KEY, kind text, ref_id text
);
CREATE TABLE conflict_checks (
  check_id text PRIMARY KEY, case_id text NOT NULL REFERENCES cases(case_id),
  neutral_id text NOT NULL REFERENCES neutrals(neutral_id),
  result text CHECK (result IN ('Clear','Conflict')), declaration text, at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE scorecards (
  scorecard_id text PRIMARY KEY, neutral_id text NOT NULL REFERENCES neutrals(neutral_id),
  timeliness numeric(5,2), upheld_rate numeric(5,2), feedback numeric(3,2), period text
);
CREATE TABLE complaints (
  complaint_id text PRIMARY KEY, neutral_id text NOT NULL REFERENCES neutrals(neutral_id),
  case_id text, category text CHECK (category IN ('Misconduct','Bias','Delay','Conflict','Fees')),
  details text, status text DEFAULT 'open', created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE discipline_actions (
  action_id text PRIMARY KEY, complaint_id text NOT NULL REFERENCES complaints(complaint_id),
  outcome text CHECK (outcome IN ('Dismiss','Counsel','Warning','Suspension','De-empanel')),
  at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE proceedings (
  proceeding_id text PRIMARY KEY, case_id text NOT NULL REFERENCES cases(case_id),
  type text CHECK (type IN ('Negotiation','Conciliation','Mediation','Arbitration')),
  reply text, counter_claims text, created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE sessions (
  session_id text PRIMARY KEY, case_id text NOT NULL REFERENCES cases(case_id),
  kind text CHECK (kind IN ('joint','caucus','async')), datetime timestamptz, recorded boolean DEFAULT false
);
CREATE TABLE hearings (
  hearing_id text PRIMARY KEY, case_id text NOT NULL REFERENCES cases(case_id),
  datetime timestamptz NOT NULL, mode text CHECK (mode IN ('Video','Audio','In-person')), attendees jsonb
);
CREATE TABLE orders (
  order_id text PRIMARY KEY, case_id text NOT NULL REFERENCES cases(case_id),
  kind text, content text, served boolean DEFAULT false, at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE documents (
  document_id text PRIMARY KEY, case_id text REFERENCES cases(case_id),
  kind text, sha256 text NOT NULL, storage_uri text, legal_hold boolean DEFAULT false,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE service_attempts (
  attempt_id text PRIMARY KEY, case_id text NOT NULL REFERENCES cases(case_id),
  channel text, at timestamptz NOT NULL DEFAULT now(), result text, failure_reason text
);
CREATE TABLE signatures (
  signature_id text PRIMARY KEY, document_id text NOT NULL REFERENCES documents(document_id),
  party_id text, method text CHECK (method IN ('AadhaarESign','DSC','ClickToSign')), at timestamptz
);
CREATE TABLE stamps (
  stamp_id text PRIMARY KEY, document_id text NOT NULL REFERENCES documents(document_id),
  provider text CHECK (provider IN ('SHCIL','NeSL')), duty numeric(12,2), at timestamptz
);
CREATE TABLE rate_card_items (
  item_id text PRIMARY KEY, rate_card_id text NOT NULL REFERENCES rate_cards(rate_card_id),
  stage text, basis text, amount numeric(12,2), payer text
);
CREATE TABLE ic_committees (
  ic_id text PRIMARY KEY, entity_id text NOT NULL REFERENCES entities(entity_id),
  members jsonb NOT NULL, external_member text, tenure jsonb
);
CREATE TABLE ai_outputs (
  output_id text PRIMARY KEY, session_ref text, case_id text,
  model_ref text NOT NULL, rationale text, created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE model_registry (
  model_ref text PRIMARY KEY, provider text, version text, prompt_template_version text,
  approved_by text, approved_at timestamptz
);
CREATE TABLE sector_rulebooks (
  rulebook_id text PRIMARY KEY, sector text, ruleset_version_id text REFERENCES ruleset_versions(ruleset_version_id)
);
CREATE TABLE feature_flags (
  flag text PRIMARY KEY, enabled boolean DEFAULT false, rollout jsonb
);
-- End of EQR-32 supplement.
