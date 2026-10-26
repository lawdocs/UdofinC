-- Equator Resolution — Commercial ADR Platform : indicative database schema (PostgreSQL)
-- Design artifact. Add tenancy, soft-deletes, encryption-at-rest and row-level security in implementation.

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Parties (businesses / individuals)
CREATE TABLE party (
    party_id        UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name            TEXT NOT NULL,
    entity_type     TEXT,                    -- PvtLtd/LLP/Partnership/Proprietor/Individual
    cin             TEXT,
    gstin           TEXT,
    pan             TEXT,
    address         TEXT,
    auth_signatory  TEXT,
    kyb_status      TEXT DEFAULT 'pending',  -- pending/verified/failed
    created_at      TIMESTAMPTZ DEFAULT now()
);

-- Neutrals (arbitrators / mediators)
CREATE TABLE neutral (
    neutral_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name       TEXT NOT NULL,
    role            TEXT,                    -- arbitrator/mediator/both
    grade           TEXT,                    -- A/B/C
    sectors         TEXT[],
    languages       TEXT[],
    seats           TEXT[],
    aci_accredited  TEXT,                    -- yes/no/pending
    years_exp       INT,
    rating          NUMERIC(2,1),
    status          TEXT DEFAULT 'empanelled'
);

-- Cases
CREATE TABLE arb_case (
    case_id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_no         TEXT UNIQUE NOT NULL,    -- EQ/COM/<CITY>/<YYYY>/<NNNNN>
    mechanism       TEXT NOT NULL,           -- arbitration/mediation/s12a/msme
    dispute_types   TEXT[],
    sector          TEXT,
    claim_value     NUMERIC(18,2),
    has_clause      BOOLEAN,
    seat            TEXT,
    governing_law   TEXT,
    language        TEXT,
    num_arbitrators INT,
    status          TEXT DEFAULT 'submitted',
    clock_starts_at TIMESTAMPTZ,             -- s.29A basis
    created_at      TIMESTAMPTZ DEFAULT now()
);

-- Case ↔ Party (claimant / respondent / additional)
CREATE TABLE case_party (
    case_id     UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    party_id    UUID REFERENCES party(party_id),
    role        TEXT NOT NULL,               -- claimant/respondent/additional
    PRIMARY KEY (case_id, party_id, role)
);

-- Arbitration agreement
CREATE TABLE arbitration_agreement (
    agreement_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id      UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    contract_ref TEXT,
    clause_text  TEXT,
    seat         TEXT,
    rules        TEXT DEFAULT 'Equator Rules of Arbitration'
);

-- Appointment & tribunal
CREATE TABLE appointment (
    appointment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id        UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    neutral_id     UUID REFERENCES neutral(neutral_id),
    tribunal_role  TEXT,                     -- sole/presiding/co-arbitrator/mediator
    method         TEXT,                     -- party/institutional/s11
    confirmed_at   TIMESTAMPTZ
);

-- Disclosure (s.12)
CREATE TABLE disclosure (
    disclosure_id  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    appointment_id UUID REFERENCES appointment(appointment_id) ON DELETE CASCADE,
    fifth_schedule TEXT,                     -- disclosed circumstances
    seventh_ok     BOOLEAN,                  -- not ineligible
    signed_at      TIMESTAMPTZ
);

-- Pleadings
CREATE TABLE pleading (
    pleading_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id     UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    type        TEXT,                        -- SoC/SoD/counterclaim/reply
    party_id    UUID REFERENCES party(party_id),
    filed_at    TIMESTAMPTZ,
    ai_assisted BOOLEAN DEFAULT false
);

-- Hearings & orders
CREATE TABLE hearing (
    hearing_id  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id     UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    kind        TEXT,                        -- procedural/evidentiary/final
    mode        TEXT,                        -- in-person/video/hybrid
    scheduled_at TIMESTAMPTZ,
    attendance  JSONB
);
CREATE TABLE procedural_order (
    order_id    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id     UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    number      INT,
    content     TEXT,
    issued_at   TIMESTAMPTZ
);

-- Documents (evidence, forms, awards)
CREATE TABLE document (
    doc_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id     UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    form_ref    TEXT,                        -- e.g. F-C09
    title       TEXT,
    version     INT DEFAULT 1,
    hash        TEXT,                        -- tamper-evidence
    access      TEXT,                        -- confidentiality ring
    esigned     BOOLEAN DEFAULT false,
    uploaded_at TIMESTAMPTZ DEFAULT now()
);

-- Award / consent award / MSA
CREATE TABLE award (
    award_id    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id     UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    type        TEXT,                        -- award/consent-award/msa
    terms       TEXT,
    interest    TEXT,
    costs       TEXT,
    signed_at   TIMESTAMPTZ,
    registered_at TIMESTAMPTZ,               -- MSA s.20
    stamp_ref   TEXT,
    scrutiny_ok BOOLEAN
);

-- Escrow
CREATE TABLE escrow_account (
    escrow_id   UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id     UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    agent_bank  TEXT,
    amount      NUMERIC(18,2),
    status      TEXT DEFAULT 'open'
);
CREATE TABLE escrow_release (
    release_id  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    escrow_id   UUID REFERENCES escrow_account(escrow_id) ON DELETE CASCADE,
    tranche     INT,
    amount      NUMERIC(18,2),
    trigger     TEXT,
    released_at TIMESTAMPTZ,
    status      TEXT DEFAULT 'pending'
);

-- MSME reference
CREATE TABLE msme_reference (
    ref_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id     UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    udyam_no    TEXT,
    invoice_refs TEXT,
    due_date    DATE,
    amount_due  NUMERIC(18,2),
    interest_claimed NUMERIC(18,2)
);

-- DPDP consent & audit
CREATE TABLE consent_record (
    consent_id  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    party_id    UUID REFERENCES party(party_id),
    purpose     TEXT,
    version     TEXT,
    granted_at  TIMESTAMPTZ DEFAULT now(),
    withdrawn_at TIMESTAMPTZ
);
CREATE TABLE audit_log (
    log_id      BIGSERIAL PRIMARY KEY,
    actor_id    UUID,
    action      TEXT,
    entity      TEXT,
    entity_id   UUID,
    at          TIMESTAMPTZ DEFAULT now(),
    detail      JSONB
);
CREATE TABLE notification (
    notif_id    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id     UUID REFERENCES arb_case(case_id) ON DELETE CASCADE,
    event       TEXT,
    channel     TEXT,                        -- email/sms/whatsapp
    template_id TEXT,
    recipient   TEXT,
    sent_at     TIMESTAMPTZ
);

CREATE INDEX idx_case_status   ON arb_case(status);
CREATE INDEX idx_case_mechanism ON arb_case(mechanism);
CREATE INDEX idx_caseparty_case ON case_party(case_id);
CREATE INDEX idx_doc_case       ON document(case_id);
CREATE INDEX idx_audit_entity   ON audit_log(entity, entity_id);
