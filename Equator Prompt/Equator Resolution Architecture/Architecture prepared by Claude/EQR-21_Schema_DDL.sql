-- EQR-21 · Equator Resolution — Core Schema DDL (PostgreSQL)
-- v1.0 · 9 July 2026 · Confidential. Starting point; full schema per EQR-12.
-- Conventions: ULID text PKs, tenant_id scoping, timestamptz UTC, snake_case, CHECK enums.

CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- ---------- Tenancy & config ----------
CREATE TABLE tenants (
  tenant_id      text PRIMARY KEY,
  brand          text NOT NULL,
  kind           text NOT NULL CHECK (kind IN ('EDRS','PrivateCourt','Enterprise')),
  created_at     timestamptz NOT NULL DEFAULT now(),
  updated_at     timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE ruleset_versions (
  ruleset_version_id text PRIMARY KEY,
  pillar         text NOT NULL,
  version        text NOT NULL,
  effective_from timestamptz NOT NULL,
  config         jsonb NOT NULL
);

-- ---------- Parties & identity ----------
CREATE TABLE parties (
  party_id       text PRIMARY KEY,
  full_name      text NOT NULL,
  dob            date,
  gender         text CHECK (gender IN ('Male','Female','Other','Undisclosed')),
  mobile         text NOT NULL,
  email          text NOT NULL,
  address        text,
  language       text DEFAULT 'English',
  created_at     timestamptz NOT NULL DEFAULT now(),
  updated_at     timestamptz NOT NULL DEFAULT now(),
  deleted_at     timestamptz
);

CREATE TABLE entities (
  entity_id      text PRIMARY KEY,
  legal_name     text NOT NULL,
  entity_type    text NOT NULL CHECK (entity_type IN
                   ('PrivateLtd','PublicLtd','LLP','NBFC','Bank','UCB','Partnership','Proprietor')),
  cin            text, gstin text,
  pan_enc        bytea,                 -- application-encrypted (sensitive)
  signatory_name text,
  bank_account_enc bytea, ifsc text,
  created_at     timestamptz NOT NULL DEFAULT now(),
  updated_at     timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE kyc_records (
  kyc_id         text PRIMARY KEY,
  subject_id     text NOT NULL,         -- party_id or entity_id
  subject_kind   text NOT NULL CHECK (subject_kind IN ('party','entity')),
  id_type        text NOT NULL CHECK (id_type IN ('Aadhaar','PAN','Passport','VoterID','DL')),
  id_number_enc  bytea NOT NULL,        -- sensitive, encrypted
  method         text NOT NULL CHECK (method IN ('VideoKYC','DigiLocker','Manual')),
  verified_at    timestamptz
);

-- ---------- Cases ----------
CREATE TABLE cases (
  case_id            text PRIMARY KEY,
  tenant_id          text NOT NULL REFERENCES tenants(tenant_id),
  pillar             text NOT NULL CHECK (pillar IN
                       ('Family','NBFC','Commercial','MSME','Grievance','POSH','Consumer','Securities','International')),
  mechanism          text NOT NULL CHECK (mechanism IN ('Negotiation','Conciliation','Mediation','Arbitration')),
  track              text,
  status             text NOT NULL DEFAULT 'Draft',
  confidentiality_tier text NOT NULL DEFAULT 'Standard'
                       CHECK (confidentiality_tier IN ('Standard','High','POSH/Marital')),
  ruleset_version_id text REFERENCES ruleset_versions(ruleset_version_id),
  claim_value        numeric(14,2), currency text DEFAULT 'INR',
  seat               text, governing_law text, language text DEFAULT 'English',
  is_cross_border    boolean DEFAULT false,
  explorer_ref       text,
  parent_case_id     text REFERENCES cases(case_id),
  filed_at           timestamptz, closed_at timestamptz,
  created_at         timestamptz NOT NULL DEFAULT now(),
  updated_at         timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX idx_cases_tenant_status ON cases(tenant_id, status);
CREATE INDEX idx_cases_pillar ON cases(pillar);

CREATE TABLE case_parties (
  case_id  text NOT NULL REFERENCES cases(case_id),
  party_id text NOT NULL REFERENCES parties(party_id),
  role     text NOT NULL CHECK (role IN ('Claimant','Respondent','Advocate','AuthRep')),
  PRIMARY KEY (case_id, party_id, role)
);
CREATE INDEX idx_caseparties_party ON case_parties(party_id);

-- ---------- Neutrals ----------
CREATE TABLE neutrals (
  neutral_id  text PRIMARY KEY,
  full_name   text NOT NULL,
  type        text NOT NULL CHECK (type IN ('Arbitrator','Mediator','Conciliator','CaseManager')),
  accreditation text[], experience_years int, fee_band text, languages text[],
  status      text NOT NULL DEFAULT 'active',
  created_at  timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE allocations (
  allocation_id text PRIMARY KEY,
  case_id    text NOT NULL REFERENCES cases(case_id),
  neutral_id text NOT NULL REFERENCES neutrals(neutral_id),
  method     text NOT NULL CHECK (method IN ('RoundRobin','LoadBalanced','RulesBased','Nomination','Manual')),
  decision   text CHECK (decision IN ('Accept','Decline')),
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX idx_alloc_neutral ON allocations(neutral_id);

-- ---------- Evidence, notice, outcomes ----------
CREATE TABLE evidence_items (
  evidence_id text PRIMARY KEY,
  case_id  text NOT NULL REFERENCES cases(case_id),
  sha256   text NOT NULL, admitted boolean DEFAULT false, tier text,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE custody_log (
  log_id text PRIMARY KEY, evidence_id text NOT NULL REFERENCES evidence_items(evidence_id),
  actor text NOT NULL, action text NOT NULL, at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE service_certificates (
  cert_id text PRIMARY KEY, case_id text NOT NULL REFERENCES cases(case_id),
  summary jsonb NOT NULL, ack boolean DEFAULT false, at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE settlements (
  settlement_id text PRIMARY KEY, case_id text NOT NULL REFERENCES cases(case_id),
  terms jsonb NOT NULL, authentication jsonb, signed boolean DEFAULT false, stamped boolean DEFAULT false,
  enforceable_basis text DEFAULT 's.27 Mediation Act 2023', created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE awards (
  award_id text PRIMARY KEY, case_id text NOT NULL REFERENCES cases(case_id),
  findings text, reasoning text, relief text, signed boolean DEFAULT false,
  enforceable_basis text DEFAULT 's.36 A&C Act 1996', s29a_due_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE execution_bundles (
  bundle_id text PRIMARY KEY, case_id text NOT NULL REFERENCES cases(case_id),
  items jsonb NOT NULL, format text DEFAULT 'e-Courts', generated_at timestamptz NOT NULL DEFAULT now()
);

-- ---------- Money ----------
CREATE TABLE rate_cards (rate_card_id text PRIMARY KEY, scope text, version text, published_at timestamptz);
CREATE TABLE invoices (
  invoice_id text PRIMARY KEY, case_id text REFERENCES cases(case_id),
  rate_card_id text REFERENCES rate_cards(rate_card_id),
  amount numeric(14,2) NOT NULL CHECK (amount >= 0), currency text DEFAULT 'INR',
  status text DEFAULT 'raised', created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE payments (
  payment_id text PRIMARY KEY, invoice_id text NOT NULL REFERENCES invoices(invoice_id),
  payer text, rail text CHECK (rail IN ('Razorpay','PayPal')), split jsonb,
  status text DEFAULT 'created', created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE escrow_ledger (
  entry_id text PRIMARY KEY, case_id text REFERENCES cases(case_id),
  direction text CHECK (direction IN ('in','out')), amount numeric(14,2), status text,
  at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE payouts (
  payout_id text PRIMARY KEY, neutral_id text REFERENCES neutrals(neutral_id),
  amount numeric(14,2), rail text, status text, at timestamptz NOT NULL DEFAULT now()
);

-- ---------- Enterprise & grievance ----------
CREATE TABLE escalation_contracts (
  escalation_id text PRIMARY KEY, source_system text NOT NULL, ticket_ref text NOT NULL,
  consent_ref text NOT NULL, pillar text, payload jsonb, confidentiality_tier text,
  callback text, case_id text REFERENCES cases(case_id), created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE grievances (
  grievance_id text PRIMARY KEY, entity_id text REFERENCES entities(entity_id),
  category text, narrative_enc bytea, tier text DEFAULT 'High', respondent text,
  anonymous boolean DEFAULT false, created_at timestamptz NOT NULL DEFAULT now()
);

-- ---------- AI ----------
CREATE TABLE explorer_sessions (
  session_id text PRIMARY KEY, input_min jsonb, category text, method text,
  viability text CHECK (viability IN ('Weak','Mixed','Reasonable','Strong')),
  model_ref text, created_at timestamptz NOT NULL DEFAULT now()
);

-- ---------- Audit & event store (append-only, partition by month) ----------
CREATE TABLE audit_log (
  event_id text PRIMARY KEY, actor text NOT NULL, action text NOT NULL,
  case_id text, at timestamptz NOT NULL DEFAULT now(), hash_prev text
) PARTITION BY RANGE (at);

CREATE TABLE domain_events (
  event_id text PRIMARY KEY, type text NOT NULL, occurred_at timestamptz NOT NULL DEFAULT now(),
  tenant_id text, actor text, case_id text, version int NOT NULL DEFAULT 1,
  correlation_id text, payload jsonb NOT NULL
) PARTITION BY RANGE (occurred_at);
CREATE INDEX idx_events_case ON domain_events(case_id);
CREATE INDEX idx_events_type ON domain_events(type);

-- Row-level security stub (enable + policy per tenant-scoped table)
ALTER TABLE cases ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY tenant_isolation ON cases USING (tenant_id = current_setting('app.tenant_id'));

-- End of EQR-21 core DDL.
