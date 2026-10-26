# INFRABYX ECOSYSTEM INTEGRATION SPECIFICATION

**Canonical contract for events, APIs, data ownership, identity and connectors across Finbyx, Udofin, Equator Resolution, LawDocsComply, the Recovery Suite (future Udolex), future ecosystem apps and third parties**

Version 1.0 · 19 October 2026 · Companion to the Finbyx Master Build Prompt v1.4 and the Udofin Master Build Prompt v1.1, whose Part 5 tables remain as summaries and point here as canonical

---

## HOW TO USE THIS SPECIFICATION

**Project owner.** (1) Commit this file unchanged to every product repository as `docs/ecosystem/infrabyx-integration-spec.md`; edit it only in `infrabyx-contracts` (Part 3.3); CI fails if a copy's SHA-256 differs from the tagged version. (2) Approve changes once per affected product. (3) `[VERIFY: …]` marks a fact to re-check against the primary source before the related connector goes live; **[LAW]** = statute or RBI text, **[INTERP]** = our reading, **[REC]** = recommendation.

**Claude Code (any repository).** (1) Read this file before designing or changing any cross-product event, API, file, identity flow or connector; it overrides conflicting product text, ADRs or code: raise conflicts, never resolve them silently. (2) Never invent or rename an event, add a field to a published schema version, or move ownership of an entity: write a proposal (Part 14.2) and stop for approval. (3) Generate types and validators from the registry; no hand-written duplicates. (4) No connector touches real data before certification (Part 14.3). (5) Refuse any design letting Udofin, Equator, an agency or a vendor take a credit, KYC, classification, settlement, referral or enforcement decision for the RE.

**Change-control rule.** The specification changes only by a merged pull request to `infrabyx-contracts` carrying an impact note (products, events, APIs, schemas, tests), approved by the owner of every affected product, with a version bump (Part 14.1), propagated to every repository within 10 working days. Published schemas are never broken in place: a new major version runs in parallel for at least 90 days. Emergency security changes may be applied first and ratified within 5 working days.

---

# 1 — PURPOSE, SCOPE AND PRODUCTS

The single source for cross-product events, APIs, data ownership, identity, connectors, export formats and integration security, written so that a conforming producer, consumer or connector can be built without reading another product's code. Internal module boundaries, commercial terms and legal advice are out of scope.

| Product or party | Role | Regulatory position | System of record for |
|---|---|---|---|
| **Finbyx** | Staff-operated LOS, LMS, accounting, collections, Recovery Suite, risk, returns, embedded compliance | IT service provider to each RE; material outsourcing for ML/UL [INTERP] (Finbyx Part 10.6) | The RE's sanction, KFS, loan, ledger, classification, provisioning, CIC reporting, collateral and pledge book, DLG ledger, recovery, notices, litigation, settlements |
| **Udofin** | Borrower-facing platform of an LSP serving several REs | LSP and agent of each RE (CF para 4(1)(xix)); RE fully liable (para 6(7)) | Borrower journey, its consents and captured evidence, DLA register, LSP grievances, its DLG records and accounts; never a loan |
| **Equator Resolution** | ODR institution: conciliation, mediation, arbitration, Lok Adalat facilitation | Independent institution [INTERP] | Docket, panel and selection log, disclosures, hearings, orders, original awards and settlements, service logs, fees |
| **LawDocsComply** | GRC platform for RBI, SEBI and IFSCA regulated entities | Technology service provider | Obligations, calendar, policies, issues, attestations (external or group mode) |
| **Recovery Suite** | Attachable pack in Finbyx (full) and Udofin (LSP subset); later standalone **Udolex** | Runs in the RE's tenancy | Recovery cases, notices, settlements, litigation, asset sales |
| **Field-investigation app** (future) | Field verification, skip tracing | Service provider (OUT Ch III) | Visit evidence |
| **Third parties** | Other LOS/LMS (incl. Fineract-based), accounting, GRC tools, legal-tech and court data, e-auction, agencies and diallers, ODR providers, KYC, bureau, AA, eSign, eStamp, depository, RTA, payments | Own regulation and contract | Their own records; never RE decisions |

---

# 2 — PRINCIPLES

1. **Separate databases; contracts only.** No product touches another's tables, stores or queues; every interaction is a registered event, API or file layout with a versioned JSON Schema.
2. **Data ownership.** One owner per canonical entity per tenant (Part 5); copies are projections with source and as-of time, never edited, reconciled daily; on conflict the owner wins and `ReconciliationBreakRaised` is opened.
3. **Regulated decisions stay with the RE:** credit and KYC decisions, sanction, pricing, KFS, disbursement, classification, provisioning, CIC reporting, settlement and write-off approval, ADR referral, legal notices, enforcement, grievance closure (OUT para 15; KYC para 13; CF paras 6(7), 12; RSA para 16).
4. **Money never through the LSP.** RE account to borrower or permitted end-beneficiary; repayment to the RE or a co-lender-controlled escrow; no LSP pool or merchant account; LSP fees paid by the RE, never deducted from recoveries (CF para 10(1)–(5)). Equator, agencies and connectors are bound equally; validators reject any other account.
5. **Consent and purpose limitation.** Personal data travels only with a `consentref` (purpose, named RE, categories, expiry) or a `legalbasis` code (CF para 13(4); DPDP Act ss.7, 17(1)(a) [VERIFY: wording and commencement]), only to the RE the borrower chose.
6. **India-only residency** of data, backups, logs, event logs, DLQs and sub-processors; anything processed abroad repatriated within 24 hours (CF para 14(4); OUT para 74(vi)).
7. **Least privilege** by scope (Part 4.5); recovery and litigation data reach Udofin only as the RE-permitted LSP projection (OUT paras 15, 24).
8. **Failure containment:** each product keeps working when another fails (queues, circuit breakers, DLQs, replay, reconciliation).
9. **Versioning** of schemas, events, APIs, mappings and connectors; breaking changes get a new major with ≥ 90 days' parallel run.
10. **Auditability:** every message signed, correlated, stored with its hash at both ends and producible to the RE, auditors and RBI (OUT paras 34, 81; CYB paras 46, 57).

---

# 3 — INTEGRATION ARCHITECTURE

## 3.1 Topology and transports

Each product exposes partner APIs through its own gateway (TLS 1.3, mTLS for machines, token and schema validation, rate limits, WAF). Events travel by **HTTP push** (default): CloudEvents structured JSON as Standard Webhooks with RFC 9421 signatures; or by **streaming** between Infrabyx products on the same AWS ap-south-1 estate (MSK or Redpanda, CloudEvents Kafka binding, one topic per domain per producer). Every producer serves `GET /v1/events?after=[cursor]&types=[list]` for catch-up; files are the fallback (3.11).

## 3.2 CloudEvents 1.0 envelope

| Attribute | Rule |
|---|---|
| `id` | UUIDv7 (RFC 9562); with `source`, the de-duplication key |
| `source` | `urn:infrabyx:[product]:[tenantid]` (finbyx, udofin, equator, ldc, udolex, fiapp) or `urn:ext:[connector-id]:[tenantid]` |
| `type` | `in.infrabyx.[domain].[EventName].v[major]`, `[EventName]` exactly as Part 6 |
| `subject` | Aggregate id; ordering and partition key |
| `time`, `dataschema`, `data` | RFC 3339 (IST); `[registry-base]/schemas/[domain]/[EventName]/[semver].json`; payload |
| `tenantid`, `reid` | Producer tenant (Part 4.1); ecosystem RE id (`none` only for platform events) |
| `productfamily` | PL, PDL, MSME, LAP, HL, VL, GOLD, LAS, LAMF, CD, MFI, SCF, MED, LEF, RF, DR, CORP, STAFF, DCL, EDU, PF (codes as Finbyx Part 6.3.3); co-lent loans `CLN-[base]` (e.g. `CLN-PL`); `na` for non-loan events |
| `correlationid`, `causationid` | Journey id; id of the causing event or request |
| `consentref` or `legalbasis` | Required with personal data; `legalbasis` ∈ STATUTORY_REPORTING, LEGAL_CLAIM, CONTRACT_PERFORMANCE_RE, REGULATOR_REQUEST |
| `dataclass`, `schemaver`, `seq`, `traceparent` | Highest class (13.2); full schema semver; per-subject sequence; W3C Trace Context |

`specversion` 1.0 (spec 1.0.2), JSON content. Consumers reject invalid events, personal data without `consentref` or `legalbasis`, and unmapped `reid`s.

## 3.3 Contracts and registry

`infrabyx-contracts` holds this specification, JSON Schema 2020-12 documents, OpenAPI 3.1 (3.2 only for streaming after an ADR) and AsyncAPI 3.0 documents, code tables, mapping packs and the certification suite. An India-hosted registry serves immutable versions; compatibility is **BACKWARD** (minors add optional fields or `x-extensible-enum` values only). Paths `/v[major]/`, `snake_case` fields, `UPPER_SNAKE_CASE` enums, prefixed opaque ids, cursor pagination (`limit` ≤ 500), `updated_since` on reconciliation lists. Products pin versions in `contracts.lock`; Pact consumer-driven tests gate every deployment.

## 3.4 Webhooks and idempotency

- **Standard Webhooks:** `webhook-id` (= `id`), `webhook-timestamp`, `webhook-signature` (HMAC-SHA256 over `id.timestamp.body`, `whsec_` secret); Infrabyx-to-Infrabyx deliveries add RFC 9421. Timestamps more than 5 minutes off are rejected.
- **At-least-once:** `2xx` only after durable inbox write; exponential back-off with jitter for 72 hours, then DLQ and alert to both sides.
- **Idempotency-Key** (UUIDv7) on every state-changing request (`draft-ietf-httpapi-idempotency-key-header`, still a draft [VERIFY: status]); stored with body hash and response ≥ 24 hours (7 days for money); same key with a different body returns 422 and a retry while the original is still processing returns 409, as the draft specifies.
- **Business keys** (Part 6) are unique constraints at the consumer.

## 3.5 Outbox, inbox, ordering and replay

Producers write to a transactional outbox with the state change; consumers store `(source, id)` and the business key before processing. Order is guaranteed per `subject` by `seq`; gaps are parked 15 minutes, then replayed, else `ReconciliationBreakRaised`. Replay retention ≥ 90 days (365 for collateral, recovery, ADR, litigation and DLG); owners expose `GET /v1/[aggregate]/{id}` snapshots with the last `seq`.

## 3.6 Tokens, signatures and documents

- **Machine clients:** OAuth client credentials profiled to the OAuth 2.1 draft [VERIFY: status] and RFC 9700; certificate-bound (RFC 8705) or `private_key_jwt` (RFC 7523); tokens ≤ 10 minutes, audience-restricted.
- **Borrower-delegated access** (an LSP or app acting for a borrower against RE APIs, e.g. drawdowns): **FAPI 2.0 Security Profile** (Final, Feb 2025) with PAR (RFC 9126), PKCE, mTLS or DPoP (RFC 9449), passing `acr` and `auth_time`. **Token exchange** (RFC 8693) for Equator launch (4.4).
- **mTLS** with Infrabyx Ecosystem PKI certificates (separate sandbox and production CAs, ≤ 397 days, automated rotation).
- **RFC 9421** (`ed25519`) on Infrabyx-to-Infrabyx calls, webhooks and regulated messages, covering the components `@method`, `@target-uri`, `content-digest` (RFC 9530), `content-type` and `idempotency-key`, with the signature parameters `created`, `keyid` and `alg`; keys in India KMS or HSM, JWKS per product and environment.
- **Regulated messages** (signature mandatory and retained: RFC 9421 in transit plus a detached JWS over the CloudEvent, stored with it so the proof can be re-verified after the HTTP exchange): `DecisionMade`, `KFSIssued`, `SanctionLetterIssued`, `ESignCompleted`, `EStampCompleted`, `LoanDisbursed`, `CollateralPledgeCreated`, `MarginCallRaised`, `CollateralInvoked`, `CollateralReleased`, `ClassificationSynced`, `SettlementApproved`, `SettlementOfferIssued`, `LegalNoticeIssued`, `ADRReferralCreated`, `ADRConsentRecorded`, `ADROutcomeRecorded`, `OrderRecorded`, `RecoveryReceiptPosted`.
- **Documents** travel by reference (`document_id`, `sha256`) with a **detached JWS** (RFC 7515, 7797) for transfer integrity; legal effect rests on the document's own eSign, DSC or PAdES signature and e-stamp.

## 3.7 Sandbox and certification

Per-counterparty sandbox: synthetic data, rail mocks, personas per product and recovery path, a time-travel clock for statutory deadlines. Real data only after the suite (14.3) passes and `ConnectorCertified` is emitted; recertify on schema, hosting, key or sub-processor change and annually.

## 3.8 Service levels

| Measure | Target | Basis |
|---|---|---|
| Event delivery ("std") | Outbox lag p95 ≤ 30 s; delivery p95 ≤ 5 min; retries 72 h then DLQ | [REC] |
| Synchronous APIs | p95 ≤ 800 ms excluding third parties; `EligibilityCheck` ≤ 3 s | Finbyx Part 10.3 |
| Availability | Finbyx, Udofin 99.9%; Equator, LawDocsComply 99.5% monthly | [REC] |
| Co-lender classification sync | By 23:59 IST next working day | TDCR para 124 |
| Agent cash posting | Same day | CF para 10(5) |
| Provider incident to RE | ≤ 2 h, so the RE reports within 6 h of provider detection | OUT para 61 |
| Daily reconciliation file | By 06:00 IST | [REC] |

## 3.9 Error model

RFC 9457 problem details: `type` `[registry-base]/problems/[code]`, `title`, `status`, `detail` (no personal data), `instance`, `code`, `correlation_id`, `retryable`, `errors[]` (JSON Pointers). Codes: `schema-validation-failed` 422, `consent-missing` 403, `scope-insufficient` 403, `tenant-unknown` 404, `idempotency-key-reuse` 422, `request-in-progress` 409, `state-transition-invalid` 409, `regulatory-guard` 422 (names rule and citation, e.g. LSP-controlled account, un-notified NBFC attempting SARFAESI, referral without arbitration basis), `rate-limited` 429, `dependency-unavailable` 503.

## 3.10 Rate limits and observability

Token buckets per client, tenant and operation class, advertised in `RateLimit` headers [VERIFY: draft header names]; regulated commands never share a bucket with bulk reads. OpenTelemetry to India collectors without personal data; integration monitors (Finbyx M21, Udofin U21) show health, latency, errors, DLQ depth and certification status.

## 3.11 File-transfer fallback

SFTP from allow-listed Indian IPs or signed-URL upload; CloudEvents batches (`application/cloudevents-batch+json`), NDJSON or registered CSV/XML layouts (Part 12); a manifest (layout, version, count, control totals, period, SHA-256) signed by detached JWS; an acknowledgement file of accepted and rejected records. Name: `[producer]_[reid]_[layoutid]_v[major]_[yyyymmdd]_[seq].[ext]`.

---

# 4 — IDENTITY, TENANCY AND ACCESS ACROSS PRODUCTS

## 4.1 Organisations, tenants and RE identifiers

- **Organisation registry:** one `org_id` per legal organisation (name, constitution, CIN, masked PAN, GSTIN, LEI, `group_id`, role flags `is_re`, `is_lsp`, `is_odr_institution`, `is_service_provider`). Groups drive LawDocsComply group mode and group-outsourcing controls (OUT paras 45–51, 90–92).
- **Tenant map:** each product maps its `tenantid` to `org_id` (with environment, status and effective dates), served by `GET /v1/tenant-map` to authorised counterparts only.
- **Links** are explicit, dated and authorise every message between two parties: `re_lsp_link` (products, territories, recovery-agent appointment, DLG flag), `re_odr_link` (rules, fees, clause refs), `re_grc_link` (compliance mode), `cla_link` (co-lenders), `re_sp_link` (service provider or agency appointment under OUT Ch III: services, territories, recovery-agent appointment, scopes, dates; used by agencies, AGY connectors and the field-investigation app).
- **RE identifiers:** `reid` (`re_` + ULID, stable); `rbi_cor_no` verified at onboarding [VERIFY: source for automated checks]; `re_category` and `sbr_layer` from Finbyx `entity_regulatory_profile`; `sarfaesi_notified` (NBFC only with assets ≥ ₹100 crore and debt ≥ ₹20 lakh: S.O. 856(E) of 24 Feb 2020 as amended by S.O. 652(E) of 12 Feb 2021) and `rdb_notified` (false for NBFCs and HFCs unless notified under RDB s.2(h)(ii)) with gazette refs (research A F1, F15); `lsp_id`; one `dla_id` per DLA per platform per RE (CF para 18).

## 4.2 Service accounts and staff access

- One OAuth client per (product, counterparty, environment, purpose), certificate-bound or `private_key_jwt`, secrets never stored in clear and rotated ≤ 90 days, with owner, scopes, authorising link and expiry; an expired link disables the client.
- Staff use OIDC (preferred) or SAML 2.0 against their organisation's IdP with MFA; **SCIM 2.0** (RFC 7643, 7644) provisions users and groups; leavers removed within 4 hours (privileged within 1 hour) [REC]. An optional Infrabyx IdP serves Infrabyx staff; authorisation stays per product.
- Roles are product-specific. Neutrals exist only in Equator and counsel only in Finbyx's counsel portal; no Finbyx or Udofin user may be a neutral for the same RE (Part 8.6).

## 4.3 Borrower identity

Borrower identities are not shared across products without consent (Udofin Part 2). Each product keeps its own account; links use **pairwise pseudonymous `party_ref`s** unique per product pair and RE, so no product can correlate a borrower across REs.

## 4.4 Udofin → Equator without a separate app

1. Equator emits `ADRCaseStatusChanged` with `borrower_action_required` for a case whose RE permits Udofin presentation.
2. On tap, Udofin's backend calls Equator's token-exchange endpoint (RFC 8693) with a signed subject token: pairwise `sub`, `reid`, `adr_case_id`, `acr`, `auth_time`, `consentref`.
3. Equator returns a single-use launch URL valid ≤ 10 minutes, opened in an in-app browser tab.
4. Equator binds the session to the referral's party record and requires **OTP step-up to the RE-registered mobile** before any consent, statement, acceptance or signature (Aadhaar eSign or DSC).
5. Udofin never receives hearing content, the RE's mandate, the selection log or other parties' documents.

Borrowers not on Udofin get a signed magic link from Equator by SMS and email to RE-supplied contacts (never WhatsApp: its Business Messaging Policy bars debt-collection use; Finbyx 7A.0.6, Udofin UR3), valid ≤ 72 hours, with the same step-up. The Finbyx borrower portal follows the Udofin pattern.

## 4.5 Authorisation scopes

Scopes are `[domain].[resource]:[action]`; producers filter fields, and LSP projections are separate registry subjects (`[EventName].lsp`).

| Scope | Granted to |
|---|---|
| `origination.application:write`, `origination.decision:read` | LSPs, DSAs, co-lending originators (own applications) |
| `servicing.loan:read.lsp`, `payments.mandate:write` | LSPs (loans they sourced or service) |
| `collateral.pledge:orchestrate`, `collateral.position:read.lsp` | LSPs as the RE's technology provider (OTP steps, display; never accept, invoke or release) |
| `collateral.position:write`, `recovery.case:write`, `adr.referral:create` | RE system only |
| `colending.share:write` | Co-lender RE systems |
| `collections.allocation:read`, `collections.activity:write` | Appointed agents and LSPs while the appointment is active |
| `origination.verification:read`, `origination.verification:write` | Field-investigation apps and verification agencies with an active `re_sp_link` (own tasks only: `VerificationRequested`, `VerificationCompleted`, `RiskSignalRaised`) |
| `recovery.case:read.lsp`, `litigation.case:read.lsp` | LSPs, if the RE permits (`legal_stage`, RE wording, next action) |
| `recovery.settlement:request` | LSPs and borrower portals (relay only) |
| `adr.case:read.party`, `adr.case:write.institution` | Borrower-facing products; ODR institutions |
| `grc.obligation:read`, `grc.evidence:write`, `privacy.request:write` | Products in a GRC link; every product |
| `platform.module:admin`, `platform.connector:certify` | Entitlement and certification services |

---

# 5 — CANONICAL DATA MODEL

## 5.1 Conventions

Every entity has `id` (prefix + ULID), `reid`, `tenantid`, `owner_system`, `version`, `created_at`, `updated_at`, `source_refs[]`; every schema field carries `x-dataclass`. Money `{"amount": "125000.00", "currency": "INR"}`; rates as percent per annum with day count. PAN and bank accounts travel masked plus keyed token; Aadhaar numbers never; clear identifiers (`SPI`) only to the RE. Owners: **FX** Finbyx or the RE's certified LMS; **UD** Udofin; **EQ** Equator or another ODR institution; **LDC** LawDocsComply or the RE's GRC tool; **RS** Recovery Suite (in FX or standalone Udolex); **EXT** external provider.

## 5.2 Entity catalogue and owners

| # | Entity | Owner | Key fields (beyond 5.1) | Copies |
|---|---|---|---|---|
| 1 | `party` | Onboarding product; FX CIF for the RE | type, name, DOB, pan_token, contacts and addresses with source, is_deceased, legal_heirs | UD, EQ, RS |
| 2 | `borrower` | FX | party, loans, ucic, household income (CF para 51), udyam, fraud and WD flags, ibc_state | UD, EQ, RS |
| 3 | `guarantor` | FX | party, loan, type, amount, invoked_at, is_pg_to_corporate_debtor | RS, EQ |
| 4 | `regulated_entity`, `lsp` | Ecosystem registry | category, layer, SARFAESI and RDB flags, GRO; LSP is_company (CF para 19), nodal officer (CF para 12), DLAs | All |
| 5 | `product` | FX | family, version, collateral types, rate model, charges, KFS template, cooling-off, recovery playbook, LAS haircut table | UD |
| 6 | `application` | UD journey; FX once submitted | product, amount, tenor, purpose, applicants, consents, KYC, bureau and AA refs, documents, collateral offers, dla_id, status | Both |
| 7 | `offer`, `kfs` | FX | APR, EMI, penal charges, proposal_no, validity (RBC para 29), KFS Part 2 items 1, 4, 5, 6(ii), hash | UD |
| 8 | `loan` | FX | lender of record, co-lenders and shares, outstanding by component, dpd, asset_class, npa_date, restructured, technical write-off, servicer, transferred interests | UD, RS, EQ |
| 9 | `schedule` | FX | version, instalments, moratorium, tranches | UD |
| 10 | `payment` | FX | utr, rail, value date, amount, allocation by component and co-lender share, collected_by (RE, APPOINTED_AGENT, LSP_AS_AGENT) | UD, RS, EQ |
| 11 | `mandate` | FX; UD evidence | umrn, type, sponsor bank, limits, beneficiary (must be RE) | UD |
| 12 | `collateral` | FX | collateral_type (5.3), owners, valuations, charge {type, registry, registry_ref, satisfied_at}, insurance, custody, release status | UD, RS |
| 13 | `securities_position` | FX; depository or RTA external truth | ISIN or scheme, folio or BOID token, units, pledge_ref, provider, status (7.3), price and as_of, haircut, eligible value | UD |
| 14 | `drawing_power_snapshot` | FX | eligible value, haircut version, DP, limit, utilised, reservations, available, LTV, breach and stale flags | UD |
| 15 | `margin_call` | FX | LTV, shortfall, cure options, cure_deadline (working days), basis (CF para 106(1) or Board policy), status | UD |
| 16 | `dlg_arrangement` | FX ledger; UD own records | form (CF para 23), fixed set, cap base (amount disbursed, CF para 24; CLA outstanding, TDCR para 123), cap, invocations, recovery shares | UD |
| 17 | `colending_arrangement` | Each co-lender for its share | cla_regime, shares (NBFC ≥ 10%, TDCR para 102), blended rate, escrow (REs only), appropriation, customer-interface and servicer RE, recovery matrix, DLG provider | Partner, UD (disclosure) |
| 18 | `loan_transfer` | Transferor, transferee | mode (ASSIGNMENT, NOVATION, PARTICIPATION, SECURITISATION, ARC_SALE), transferee, share, servicer, payment instructions, trade-report ref (TDCR para 94) | UD, EQ |
| 19 | `recovery_case` | RS | trigger, strategy {permitted, blocked with reasons, selected, rule version}, limitation dates, stage, officer, agency, counsel, holds | UD (projection), EQ, LDC |
| 20 | `notice` | RS | instrument (e.g. LRN, S13_2, S13_4, RULE_8_6, S138, S25_PSS, ARB_S21, CONCILIATION_S62, IBC_DEMAND, AGENT_INTIMATION, GOLD_AUCTION, OTS_OFFER), statute ref, template version, language, addressees, dues snapshot, signer | UD, EQ |
| 21 | `service_proof` | RS (EQ for its notices) | per party per mode: booking or message id, status, evidence hashes, deemed service date and rule, deadlines | EQ, courts |
| 22 | `settlement` | RS; EQ holds ADR instruments | origin (DIRECT, LSP_REQUEST, ADR, LOK_ADALAT, COURT), sacrifice, approver level (RSA para 16(5)), Board ref, schedule, restructuring (para 89), consent decree (para 100), cooling end (para 95) | UD, EQ |
| 23 | `adr_case` | EQ docket; RS referral | process, basis (PRE_NAMED_INSTITUTION, POST_DISPUTE_CONSENT, CONCILIATION_INVITATION, COURT_REFERRAL), clause ref, seat, claim, parties, state (8.3), neutral, clocks | RS, UD |
| 24 | `litigation_case` | RS | role, mechanism, forum, case no, CNR, claim, stage, next date, counsel, linked matters, stay, outcome | UD, LDC |
| 25 | `hearing`, `order` | RS (courts); EQ (ADR) | date, mode, purpose, attendance, next date; order type (INTERIM, FINAL, DECREE, AWARD, RECOVERY_CERTIFICATE, STAY), directions with due dates | UD (date), LDC |
| 26 | `asset_sale` | RS | mode, platform, reserve and basis, notices, H1, 25% deposit and balance dates (SARFAESI Rules 9(3)–(4)), certificate, proceeds, surplus or shortfall | UD |
| 27 | `compliance_obligation`, `control`, `evidence` | LDC (obligations); operating product (controls, evidence in its India store) | obligation_ref (e.g. `RBI/DOR/2025-26/352#124`), paragraph, applicability; control component and frequency; evidence hashes, masked sample, hash-chain pointer | All |
| 28 | `document` | Producing product | type, version, sha256, signed URI, signatures (eSign, DSC, PAdES), e-stamp, retention class, legal hold | Per permission |
| 29 | `consent_artefact` | Capturer (UD, FX, AA, EQ) | consentref, party_ref, named recipients, purpose, categories, notice version, method (OTP, ESIGN, AA_ARTEFACT, WRITTEN), expiry, withdrawal, evidence hash | Recipients |

## 5.3 Code tables

- **`collateral_type`:** RESIDENTIAL_PROPERTY, COMMERCIAL_PROPERTY, PLOT, UNDER_CONSTRUCTION_AGREEMENT, VEHICLE, EQUIPMENT, STOCK, BOOK_DEBTS, RECEIVABLE_INVOICE, TREDS_FACTORING_UNIT, GOLD_JEWELLERY, SILVER_JEWELLERY, GOLD_COIN, LISTED_SHARE_DEMAT, BOND_DEMAT, MF_UNIT_SOA, MF_UNIT_DEMAT, FIXED_DEPOSIT, INSURANCE_POLICY, PERSONAL_GUARANTEE, CORPORATE_GUARANTEE, CREDIT_GUARANTEE_CGTMSE. Barred collateral is blocked by rule pack (primary-gold-backed units, CF para 35(2); own shares, para 105).
- **`recovery_mechanism`:** NEGOTIATION_OTS, CONCILIATION, MEDIATION, ARBITRATION, LOK_ADALAT, PERMANENT_LOK_ADALAT, S138_NI, S25_PSS, SARFAESI_S13, SARFAESI_S14, PLEDGE_SALE, CONTRACTUAL_REPOSSESSION, CIVIL_SUIT, ORDER_XXXVII, COMMERCIAL_S12A_MEDIATION, DRT_OA, IBC_S7, IBC_PG_S95, IBC_CLAIM, REVENUE_RECOVERY, SET_OFF, CGTMSE_CLAIM, DLG_INVOCATION, LOAN_SALE_ARC, WRITE_OFF; litigation adds SARFAESI_S17, DRAT_APPEAL, S9_INTERIM, S11_APPOINTMENT, S34_CHALLENGE, S36_EXECUTION, CONSUMER_COMPLAINT, WRIT_226, RBIOS (offensive and defensive).
- **`legal_stage`** (LSP projection): NONE, PRE_LEGAL, NOTICE_ISSUED, ADR_IN_PROGRESS, SETTLEMENT_IN_PROGRESS, ENFORCEMENT_IN_PROGRESS, LITIGATION_PENDING, DECREE_OR_AWARD, CLOSED; the RE approves borrower wording per stage.

---

# 6 — EVENT AND API CATALOGUE v2

## 6.1 Reading the tables

**Tags:** **(E)** existing Finbyx Part 5.2 interface, unchanged; **(A)** one of the six Udofin Part 5.2 proposals, **adopted in v1.0 of this specification subject to approval by both the Finbyx and Udofin product owners** (until both approvals are recorded, send through the RE's agreed manual channel and log); **(N)** new canonical name fixed by the v1.4/v1.1 drafting brief; **(N+)** added by this specification. **Signed** = regulated message (3.6); **API** = synchronous. Parties as Part 5.1 plus **AGY** agency or dialler, **FIA** field-investigation app, **CL** co-lender, **DSP** dispatch adapter, **CDA** court-data adapter; an RE on another LMS takes the FX role, and FIA working for an appointed agent takes the AGY role in 6.7 (allocations, activity, PTP, visits, receipts). The idempotency key is the consumer's business unique constraint (besides `(source, id)`). **std** = delivery p95 ≤ 5 minutes (3.8). LSP consumers receive `.lsp` projections; scopes in 4.5.

## 6.2 Origination (`origination`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `ProductCatalogPublished` (E) | FX → UD, other LSPs | RE approves a product version | product_code, version, eligibility, pricing grid, charges, KFS template, cooling-off days, grievance contacts, DLA disclosures, LAS haircut-table version | FX | (product_code, version) | Before effective date; UD live after RE approval (CMP paras 15(2), 31) |
| `EligibilityCheck` (E) API `POST /v1/eligibility-checks` | UD → FX | Borrower asks for offers | minimum consented fields, consentref | FX (RE BRE, rule version) | Idempotency-Key | ≤ 3 s; timeout = "lender unavailable" |
| `ApplicationSubmitted` (E) | UD → FX | Borrower submits | applicants, KYC evidence refs (KYC para 13), OTP e-KYC declaration (para 25(8)), bureau and AA refs, documents, consents, household data (CF para 51) | UD; FX once submitted | lsp_application_ref | Ack ≤ 5 min |
| `ApplicationStatusChanged` (E) | FX → UD | State change | from, to, reason_code | FX | (application_id, seq) | std |
| `AdditionalInfoRequested` (E) | FX → UD | RE query | request_id, items, due date | FX | request_id | std |
| `DecisionMade` (E) signed | FX → UD | Sanction or rejection | decision, reason codes, rule version, offers | FX | (application_id, decision_version) | std |
| `KFSIssued` (E) signed | FX → UD | KFS generated | proposal_no, validity_expiry, APR, document hash | FX | (kfs_id, version) | Before acceptance |
| `SanctionLetterIssued` (E) signed | FX → UD | Sanction letter generated | sanction_id, terms, document hash | FX | (sanction_id, version) | std |
| `BorrowerAccepted` (E) | UD → FX | Acceptance within KFS validity | accepted_at, explanation acknowledgement | UD evidence | kfs_id | Rejected after validity |
| `ESignCompleted` (E) signed | UD → FX | ESP confirms | ESP txn id, certificate, signed hash; never a bare flag | UD evidence | (document_id, esp_txn_id) | std |
| `EStampCompleted` (E) signed | UD → FX | Stamp certificate issued | certificate_no, state, duty | UD evidence | (document_id, certificate_no) | std |
| `RiskSignalRaised` (A) | UD, FIA → FX | Fraud or EWS signal, any stage | type, score, evidence; signals, not determinations (FRM paras 15, 19–23) | Signal UD or FIA; decision FX | signal_id | ≤ 15 min pre-disbursal |
| `VerificationRequested` (N+) | FX → FIA, AGY | FI, PD, RCU, legal, technical or skip-trace task | type, address token, due, consentref or legalbasis | FX | task_id | std |
| `VerificationCompleted` (N+) | FIA, AGY → FX | Task done or failed | findings, geo, time, evidence hash, agent police verification (RBC para 94) | FIA | (task_id, attempt) | ≤ 15 min |

## 6.3 Servicing (`servicing`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `LoanDisbursed` (E) signed | FX → UD, CL | Bank confirms settlement | utr, amount, value date, beneficiary type, kind (INITIAL, TRANCHE, DRAWDOWN), cooling-off end | FX | (loan_id, utr) | std |
| `DisbursementFailed` (E) | FX → UD | Payout failed or returned | attempt, reason, next step | FX | (loan_id, attempt) | std |
| `DrawdownRequested` (N+) API `POST /v1/facilities/{loan_id}/drawdowns` | UD → FX (FAPI 2.0) | Borrower requests a drawdown | amount, acr, auth_time | FX decides; executes as `LoanDisbursed` | Idempotency-Key | Accept or reject ≤ 2 s |
| `CoolingOffExitRequested` (E) | UD → FX | Exit within cooling-off (CF para 11) | requested_at, evidence | UD request; FX payable | loan_id | std |
| `ScheduleIssued` (E) | FX → UD | Loan booked | schedule_version, instalments | FX | (loan_id, schedule_version) | std |
| `ScheduleChanged` (E) | FX → UD, CL | Reset, tranche, restructuring, moratorium end, settlement | schedule_version, reason, effective date | FX | (loan_id, schedule_version) | std |
| `DueReminderTrigger` (E) | FX → UD | Reminder due under RE policy | due date, amount, template_id | FX | (loan_id, due_date, seq) | Within contact window |
| `DPDChanged` (E) | FX → UD, CL, AGY | Day-end | dpd, as_of | FX | (loan_id, as_of) | By 06:00 IST |
| `AssetClassificationChanged` (E) | FX → UD, CL | Day-end, borrower-level (IRACP para 23) | from, to, as_of (borrower wording RE-approved) | FX | (loan_id, as_of) | By 06:00 IST |
| `LoanClosed` (E) | FX → UD, CL | Zero dues | closed_on, closure type | FX | loan_id | std |
| `NOCIssued` (E) | FX → UD | NOC generated | document hash, pending release actions | FX | loan_id | ≤ 1 working day [REC] |
| API `GET /v1/facilities/{loan_id}/summary` | UD → FX | Display | limit, utilised, DP, available, as_of | FX | n/a | p95 ≤ 800 ms |

## 6.4 Payments and mandates (`payments`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `MandateRegistered` (E) | UD → FX | Mandate confirmed | umrn, type, sponsor bank, limits, validity, beneficiary = RE | FX; UD evidence | umrn | std |
| `PaymentReceived` (E) | FX → UD, CL, EQ (under settlement) | Receipt allocated | utr, rail, amount, allocation by component and share, collected_by | FX | (loan_id, utr) | Same day; agent cash same day (CF para 10(5)) |
| `PaymentBounced` (E) | FX → UD, RS | Mandate, cheque or UPI return | instrument, return reason (feeds s.138 and s.25 PSS checks) | FX | (loan_id, instrument_ref, presentation_no) | ≤ 1 h of return file |
| `DailyReconciliationFile` (E) file | FX ↔ UD, CL | Day close | all flows with control totals | Each side | (producer, business_date) | By 06:00 IST |

## 6.5 Collateral (`collateral`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `CollateralHoldingsShared` (N+) | UD → FX | Holdings fetched with consent (CDSL LAS, NSDL, RTA or MF Central) | ISIN or scheme, units, source, as_of | Depository or RTA data; FX stores | (application_id, snapshot_id) | std |
| API `POST /v1/collateral/eligibility-quotes` | UD → FX | Indicative value | returns indicative eligible value and DP | FX | Idempotency-Key | ≤ 2 s |
| `CollateralPledgeRequested` (N) | FX → UD (or provider) | Sanction requires pledge or lien | securities, quantities, pledgee DP or RTA, agreement no, deadline | FX | pledge_request_id | std |
| `CollateralPledgeCreated` (N) signed | FX → UD, CL | Provider confirms encumbrance (NSDL, CDSL, RTA, sealed gold packet) | pledge_ref, units or weight, provider, evidence hash | FX; provider is external truth | (provider, pledge_ref) | std; disbursement gate |
| `CollateralPledgeFailed` (N+) | FX → UD | Rejection, OTP failure, expiry | reason, retry allowed | FX | (pledge_request_id, attempt) | std |
| `CollateralChargeRegistered` (N+) | FX → UD, CL | Mortgage, hypothecation, assignment or guarantee cover registered | charge type, registry (CERSAI, VAHAN, TREDS, CGTMSE), registry_ref | FX; registry external | (registry, registry_ref) | Per SARFAESI s.23 and CERSAI Rules [VERIFY: filing window] |
| `CollateralValuationUpdated` (N) | FX → UD, CL | Valuation run, revaluation, gold assay | value, price source and as_of, haircut version, DP, LTV, freeze flag | FX | (loan_id, valuation_run_id) | LAS daily by 09:30 IST [REC] |
| `MarginCallRaised` (N) signed | FX → UD | LTV above permitted level | LTV, shortfall, cure options, cure_deadline, basis | FX | margin_call_id | ≤ 15 min; borrower told same day |
| API `POST /v1/margin-calls/{id}/cure-intents` | UD → FX | Borrower chooses a cure | top-up, part payment or sell-to-cure | FX decides | Idempotency-Key | ≤ 2 s |
| `MarginCallCured` (N) | FX → UD | Shortfall cleared | method, cured_at, post-cure LTV | FX | margin_call_id | ≤ 15 min |
| `MarginCallLapsed` (N+) | FX → UD, RS | Deadline passed uncured | shortfall, next step, freeze status | FX | margin_call_id | At deadline |
| `CollateralInvoked` (N) signed | FX → UD, CL, RS | Pledge invoked, guarantee claimed, deposit set off | quantity, proceeds, notice ref | FX | (provider, invocation_ref) | std |
| `CollateralReleased` (N) signed | FX → UD, CL | Pledge closed, lien revoked, CERSAI satisfied, Vahan NOC, gold or documents returned | release type, registry_ref, delay days, compensation (RBC paras 39, 69) | FX | (collateral_id, release_ref) | Gold ≤ 7 working days (RBC para 58); documents ≤ 30 days (RBC para 35) |

## 6.6 Co-lending, transfers and consortium (`colending`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `CoLendingSplitConfirmed` (N) | CL partner → originator | Partner books its share | share_pct, booked_on | Each RE for its share | (cla_id, loan_id) | ≤ 15 calendar days of disbursement (TDCR paras 113, 115) |
| `CoLendingReceiptAllocated` (N+) | Escrow-managing RE → other CL | Escrow receipt appropriated | utr, allocation by component and share | Escrow-managing RE | (cla_id, utr) | Same day [REC]; escrow routing and appropriation per TDCR para 117 |
| `ClassificationSynced` (N) signed | Either CL → other | CLA exposure moves to SMA or NPA, or upgrades | borrower ref, class, as_of, dpd, reason | Classifying RE | (cla_id, borrower, as_of) | By 23:59 IST next working day (TDCR para 124) |
| `LoanTransferred` (N) | FX → transferee, UD (if servicing or mirroring), RS, EQ | Transfer effective | mode, transferee, share, servicer, payment instructions, notice ref (TPA s.131) | Transferor | (loan_id, transfer_id) | ≤ 1 working day |
| `ServicerChanged` (N) | FX → UD, CL, transferee | Servicer appointed or replaced (TDCR para 30; SEC para 70) | new servicer, date, borrower notice ref | Transferor or SPE | (loan_id, change_id) | Borrower told before effect [REC] |
| API `POST /v1/ica/{ica_id}/votes` | Lenders → ICA lead | ICA decision | resolution id, lender, value, vote | ICA lead | Idempotency-Key | Passes at 75% by value and 60% by number (RSA para 32) |

## 6.7 Collections (`collections`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `CollectionAllocated` (E) | FX → UD, AGY | Allocation under an active appointment | bucket, contact rules, agents, territory | FX | allocation_id | Receiver rejects without matching appointment |
| `CollectionDeallocated` (E) | FX → UD, AGY | Recall, cure, settlement, hold, appointment end | reason | FX | allocation_id | Contact stops immediately |
| `RecoveryAgentNoticeSent` (N+) | FX → UD, AGY | Agent particulars sent to borrower by email or SMS | agent details, delivery evidence | FX | (allocation_id, borrower) | Before first contact (CF para 9(6); RBC paras 95–96) |
| `CollectionActivityLogged` (E) | UD, AGY → FX | Call, message or visit attempt | channel, outcome, recording ref, policy check id | UD or AGY | attempt_id | ≤ 15 min |
| `PTPCaptured` (E) | UD, AGY → FX | Promise to pay | amount, date, evidence | UD or AGY | ptp_id | ≤ 15 min |
| `FieldVisitLogged` (E) | UD, AGY, FIA → FX | Field visit | geo, time, premises photo, outcome | Visiting system | visit_id | ≤ 15 min |
| `ReceiptIssued` (E) | UD, AGY → FX | Cash or instrument collected by appointed agent | receipt_no, amount, deposit ref into RE account | FX posting | receipt_no | Posted same day, no fee deducted (CF para 10(5)) |

## 6.8 Recovery (`recovery`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `RecoveryCaseOpened` (N) | RS → UD (projection), LDC | Rule trigger (DPD, NPA, bounce, fraud, death) or manual | trigger, permitted and blocked mechanisms, limitation dates, legal_stage | RS | recovery_case_id | ≤ 15 min |
| `RecoveryStrategyChanged` (N) | RS → UD (projection), AGY | Re-evaluation on a material event | mechanisms, rule version, approver, legal_stage | RS | (case_id, strategy_version) | ≤ 15 min |
| `LegalNoticeIssued` (N) signed | RS → DSP, UD (copy if permitted), EQ (ADR notices) | Notice approved and signed | instrument, statute ref, template version, addressees, dues, document hash, signer | RS | notice_id | Dispatch same day [REC] |
| `NoticeServiceUpdated` (N) | DSP, EQ, UD (own in-app, SMS-link or email delivery only) → RS; RS → UD (projection, if the RE permits) | Delivery event per party per mode | channel (dispatch mode, EQUATOR or UDOFIN_APP), status, evidence, deemed service date (never set from a UD channel event), deadlines | Provider event; RS register | (notice_id, party_id, mode, provider_event_id) | ≤ 1 h |
| `SettlementRequested` (A) API `POST /v1/recovery-cases/{id}/settlement-requests` | UD, borrower portal → RS | Borrower asks to settle | proposal, reason, documents | UD request; RS decision | request_id | Ack ≤ 1 working day [REC] |
| `SettlementApproved` (N) signed | RS → UD (projection), EQ | Approval at required level | terms, approver level (RSA para 16(5)), Board ref (fraud, WD), restructuring (para 89), consent decree (para 100), cooling end (para 95) | RS | (settlement_id, approval_version) | ≤ 15 min |
| `SettlementOfferIssued` (N) signed | RS → UD, EQ | Offer within approval or approved band | document, validity, RE-account payment instructions | RS | (settlement_id, offer_version) | ≤ 15 min |
| `SettlementOfferAccepted` (N+) | UD, EQ, portal → RS | Borrower accepts by eSign or OTP | acceptance evidence | Capturer evidence; RS record | (settlement_id, offer_version) | std |
| `SettlementBreached` (N) | RS → UD, EQ | Instalment unpaid beyond grace | breach details, consequence | RS | (settlement_id, breach_seq) | ≤ 1 working day |
| `AssetRepossessed` (N) | RS → UD (projection) | Repossession or SARFAESI possession | mode, date, possession memo or panchnama, inventory | RS | (collateral_id, repossession_id) | ≤ 1 h |
| `AuctionScheduled` (N) | RS → UD (projection), auction adapter | Sale notice published | platform, reserve, date, notice refs | RS | (asset_sale_id, attempt) | ≥ 30 days after sale notice (SARFAESI Rule 9(1)); gold RBC paras 60–66 |
| `AuctionConcluded` (N) | RS, auction adapter → UD (projection) | Auction closed | result, price, deposit and balance dates | RS | (asset_sale_id, attempt) | 25% by next working day; balance ≤ 15 days (Rule 9(3)–(4)) |
| `RecoveryReceiptPosted` (N) signed | RS (FX ledger) → UD, EQ, CL, DLG provider | Recovery receipt appropriated | source, amount, appropriation (s.13(7) for SARFAESI), shares | FX | (loan_id, receipt_ref) | Same day |
| `SurplusRefunded` (N+) | RS → UD | Surplus paid to borrower or persons entitled | amount, utr, days from receipt | RS | asset_sale_id | Gold ≤ 7 working days (RBC para 66) |
| `RecoveryCaseClosed` (N) | RS → UD, LDC | Case ends | closure reason | RS | recovery_case_id | ≤ 15 min |
| API `GET /v1/recovery-cases/{id}` | UD, EQ → RS | Display or referral | projection by scope | RS | n/a | p95 ≤ 800 ms |

## 6.9 ADR — Equator or another provider (`adr`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `ADRReferralCreated` (N) signed; API `POST /v1/adr/referrals` at EQ | RS → EQ, UD (projection), LDC | RE referral after Part 8.2 gates | process, basis, clause ref, stamp proof, claim, parties, pack hashes, sealed mandate ref | RS referral; EQ docket | referral_id | Sync ack; screening ≤ 2 business days |
| `ADRConsentRecorded` (N) signed | EQ (or RS) → RS, UD | Consent, decline or deemed decline | consent type, decision, method, evidence hash | Capturer | (adr_case_id, party_id, consent_type) | std |
| `ADRNeutralAppointed` (N) | EQ → RS, UD (name only) | Appointment accepted after disclosure | neutral, selection-log ref, Sixth Schedule disclosure, challenge end | EQ | (adr_case_id, appointment_seq) | ≤ 7 days [REC] |
| `ADRHearingScheduled` (N) | EQ → RS, UD | Hearing or session fixed | date, mode; party link via launch flow (4.4) | EQ | (adr_case_id, hearing_id) | ≥ 3 days before [REC] |
| `ADRCaseStatusChanged` (N) | EQ → RS, UD (projection) | Transition (Part 8.3) | from, to, reason, clocks, borrower_action_required | EQ | (adr_case_id, seq) | std |
| `ADROutcomeRecorded` (N) signed | EQ → RS, UD (summary) | Award or settlement signed and stamped; non-settlement; withdrawal | outcome type, terms, document hash, e-stamp, served_at, s.34 window | EQ instrument; RS loan effect | (adr_case_id, outcome_seq) | Stamp at signing; certified copy ≤ 2 business days [REC] |
| `ADROutcomeComplianceUpdated` (N) | RS → EQ, UD | Payment or breach against schedule | status, amounts | RS | (adr_case_id, compliance_seq) | ≤ 1 working day |
| API `PUT /v1/adr/cases/{id}/settlement-mandate` | RS → EQ | Set or change settlement band | floor, tenor, waiver limit, approver, expiry | RS | Idempotency-Key | Never visible to borrower or UD |
| API `POST /v1/adr/cases/{id}/withdrawal` | RS → EQ | RE withdraws | reason | RS | Idempotency-Key | ≤ 1 working day |

## 6.10 Litigation (`litigation`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `LitigationCaseOpened` (N) | RS → LDC, UD (if permitted) | RE filing, or borrower-initiated proceeding received (s.17, consumer, writ, PLA) | role, mechanism, forum, CNR, claim, linked ids | RS | lit_case_id | ≤ 1 working day |
| `LitigationCaseUpdated` (N) | RS (from CDA and counsel) → LDC, UD (projection) | Stage, stay, substitution, counsel change | stage, stay, substitution, legal_stage | RS | (lit_case_id, seq) | ≤ 1 working day |
| `HearingScheduled` (N) | RS → counsel portal, LDC, UD (date only) | Next date or cause-list match | date, bench, item, purpose | RS | (lit_case_id, date, item) | Same day |
| `OrderRecorded` (N) signed | RS → LDC | Order or decree verified | order type, directions with due dates, document hash | RS | (lit_case_id, order_id) | ≤ 1 working day |
| `LitigationCaseClosed` (N) | RS → LDC, UD | Disposal, withdrawal, consent decree | outcome, amount, date | RS | lit_case_id | ≤ 1 working day |

## 6.11 DLG (`dlg`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `DLGArrangementRegistered` (E) | FX ↔ UD | Entered or renewed | form (CF para 23), fixed set, cap, tenor, auditor declaration (para 20(3)) | FX ledger; UD own records | (dlg_id, version) | Before reliance |
| `DLGInvocationRaised` (E) | FX → UD | RE invokes | loans, amount, overdue days | FX | invocation_id | Within 120 days overdue (CF para 27(1)) |
| `DLGInvocationSettled` (E) | FX ↔ UD | Cover appropriated | amount, method | FX | invocation_id | ≤ 1 working day |
| `DLGPortfolioCoverage` (E) | FX → UD | Month end | disbursed, cap, cover, invoked, remaining | FX | (dlg_set_id, month) | ≤ 3 working days |
| `DLGDisclosurePublished` (A) | UD → FX, LDC | Monthly disclosure published | month, URL, document hash | UD | (lsp_id, month) | ≤ 7 working days of month end (CF para 28) |
| `DLGRecoveryShared` (N+) | FX → UD | Post-invocation recovery shared per contract (CF para 25(3)); never credited to the loan (25(2)) | loan, receipt_ref, share | FX | (dlg_id, receipt_ref) | Per contract |

## 6.12 Grievance (`grievance`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `GrievanceRaised` (E) | UD, FX, EQ → grievance host | Complaint on any channel | channel, category, description, attachments | Host (FX, UD lender portal or LDC) | grievance_id | Ack same day |
| `GrievanceUpdated` (E) | Host → UD, FX | Status or response | status, response | Host | (grievance_id, seq) | RE clock (CF para 12; IO rules) |
| `GrievanceEscalated` (E) | Host → UD, FX | Escalation to IO, RB-IOS information, or ADR suggested | level, reason, ADR-suggested flag (only the RE refers) | Host | (grievance_id, level) | Per IO and RB-IOS rules |

## 6.13 Documents (`documents`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `DocumentShared` (N+) | Any → permitted consumer | Document made available | type, sha256, JWS, retention class, legal hold | Producer | (document_id, version) | std |
| API `GET /v1/documents/{id}` | Consumer → producer | Retrieve | signed India-hosted URL valid ≤ 15 min, sha256, JWS | Producer | n/a | p95 ≤ 800 ms |

## 6.14 Consent and privacy (`privacy`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `ConsentRecorded` (N+) | Capturer → named recipients | Consent captured after the application (holdings, ADR sharing) | consent artefact (Part 5.2 row 29) | Capturer | consentref | std |
| `ConsentWithdrawn` (A) | Capturer → every recipient | Withdrawal | scope, withdrawn_at; processing stops except legal retention | Capturer | (consentref, withdrawn_at) | ≤ 1 h [REC] |
| `DataPrincipalRequest` (A) | Any ↔ any | Access, correction, erasure, grievance, nomination; status | type, party_ref, scope, status, due | Receiving fiduciary | (request_id, status) | Forward ≤ 1 working day [REC]; DPDP Rules timelines [VERIFY] |
| `LegalHoldChanged` (N+) | RS, FX → every holder | Hold applied or released | scope (party, loan, case), reason, start, end | RS or FX | (hold_id, version) | ≤ 1 h; deletion suspended |

## 6.15 Compliance and GRC (`grc`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `ObligationPublished` (N) | LDC (or FX embedded) → products | Obligation added, amended, repealed (change feed) | obligation_ref, change type, dates, applicability | LDC | (obligation_ref, version) | ≤ 1 working day |
| `ControlTestResultPublished` (N) | FX, UD, EQ, RS → LDC | Control test run | result, population, masked sample, evidence | Operating product | (control_id, run_id) | ≤ 1 h |
| `EvidenceSubmitted` (N) | Any → LDC | Evidence artefact | control, URIs, sha256, signer | Producer | evidence_id | ≤ 1 h |
| `ComplianceIssueRaised` (N) | Any → LDC, RE | Test failure, audit or RBI observation, breach | source, severity, owner, due | Raiser; LDC tracks | issue_id | ≤ 15 min (severity 1) |
| `ReturnStatusUpdated` (N) | FX → LDC | Return generated, validated, filed, acknowledged | return_code, period, status, ack ref | FX | (return_code, period, status) | Same day |
| `PolicyAttested` (N) | Any → LDC | User attests a policy version | policy, version, user ref | Attesting product | (policy_id, version, user) | ≤ 1 h |
| `SecurityIncidentNotified` (A) | Any service provider → RE system, LDC | Cyber or data incident detected | detected_at, class, affected data, status | Notifier | (incident_id, update_seq) | ≤ 2 h target; RE to RBI within 6 h of provider detection (OUT para 61); data breach notified immediately by the RE (OUT para 28) |

## 6.16 Platform and module lifecycle (`platform`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `ModuleAttached` (N) | Entitlement service → product services, LDC | Module enabled for a tenant | version, capabilities, SKU, approvers | Entitlement service | (tenantid, module_id, version) | On publication |
| `ModuleDetached` (N) | Entitlement service → product services, LDC, counterparties | Module detached to read-only | mode READ_ONLY, export-pack hash, records on hold | Entitlement service | (tenantid, module_id, detached_at) | Writes stop at once; export ≤ 5 working days [REC] |
| `ConnectorCertified` (N) | Certification service → LDC, counterparties | Suite passed or certification revoked | suite version, result, report hash, valid_to | Certification service | (connector_id, version, suite_version) | Before production |
| `ReconciliationBreakRaised` (N+) | Any → owner, counterpart, LDC | Reconciliation or ordering break | run, break type, records, amount, owner | Detector | (recon_run_id, break_id) | ≤ 15 min |

## 6.17 Superseded names

Non-canonical names in the research notes, the Equator draft and `las.txt` are never published; they map to the names above (for example CollateralPledgeConfirmed → `CollateralPledgeCreated`, MarginCallIssued → `MarginCallRaised`, MarginCallExpired → `MarginCallLapsed`, CoLendingClassificationChanged → `ClassificationSynced`, LegalStageChanged → `legal_stage` in LSP projections, EquatorCaseOpened → `ADRReferralCreated`, EquatorOutcome → `ADROutcomeRecorded`; Equator native names per Part 8.9).
---

# 7 — PRODUCT LIFECYCLE DATA-SHARING MATRIX

## 7.1 Common rules

Origination flows Udofin → RE; decisions, documents and servicing flow back to Udofin's read-only mirror. Collateral authority is always the RE's: Udofin orchestrates borrower steps and displays RE values, never accepts, invokes or releases. Recovery data reaches Udofin only as the RE-permitted LSP projection; Udofin relays `SettlementRequested` and captures `SettlementOfferAccepted` evidence but never approves, refers, issues notices in its own name or holds funds. Project finance, loans to entities (CORP), staff loans (STAFF) and demand loans (DCL) are not Udofin products; consumer durable (CD) follows the Personal row with DISB-E to the merchant.

## 7.2 Matrix

| Product | Origination (UD → FX) | Decision and documents | Collateral creation | Disbursement | Servicing | Collections | Recovery and ADR | Reconciliation |
|---|---|---|---|---|---|---|---|---|
| Personal, payday | AA income ref, CF para 8 data, household (para 51), OTP e-KYC declaration | KFS validity at least 3 working days, or 1 working day if tenor under 7 days (RBC para 29(2)) | None | To borrower; cooling-off exit | Standard | If appointed: agent notice, 08:00–19:00 (RBC para 100) | LRN; s.25 PSS or s.138; conciliation, Lok Adalat; arbitration only with valid basis (8.2) | Cooling-off exits; DLG |
| MSME, business | GST, AA, Udyam refs; guarantor KYC; CGTMSE flag (blocks DLG, CF para 21(1)) | Covenants | `CollateralChargeRegistered` (CERSAI, CGTMSE) | Borrower or supplier | Covenants in FX | Standard | SARFAESI if eligible; suit after s.12A mediation (≥ ₹3 lakh); IBC s.7 (≥ ₹1 crore), PG s.95; CGTMSE claim as `CollateralInvoked` | CGTMSE fees and claims |
| LAP | Property refs | Legal, technical, valuation via `VerificationRequested`; physical mortgage | Mortgage, CERSAI | Borrower or prior lender | Standard | Standard | SARFAESI for notified NBFCs, CERSAI-registered (s.26D); auction events; arbitration for money claims only (*Booz Allen*) | CERSAI vs register; release ≤ 30 days (RBC para 35) |
| Home | Stage documents; builder or seller as beneficiary | As LAP; housing tests (CF para 4(1)(xiv)) | Mortgage, CERSAI | TRANCHE vs stage | Interest certificates | Standard | As LAP; HFCs are notified FIs without the ₹20 lakh floor (research A F2) | Tranches vs stage |
| Vehicle | Dealer invoice, Vahan refs | Standard | `CollateralChargeRegistered` (VAHAN) | Dealer | Insurance reminders | Standard | Repossession only after notice period with signed possession memo (RBC para 26; *Hari Dutta Sharma v State of UP*, SC, 16 Sep 2026); Form 36 (MV Act s.51(5)); auction | Vahan NOC on closure |
| Gold | Leads and branch-appointment scheduling only (gold handled and stored only in RE branches by RE staff: RBC paras 53–54) | Branch assay | `CollateralValuationUpdated` (ASSAY), `CollateralPledgeCreated` | Borrower | Daily LTV (CF paras 43–44) | Standard | Notice; reserve ≥ 90% (85% after two failures); first auction physical in district; no lender bids (RBC paras 60–66); surplus ≤ 7 working days | Vault vs pledge book; release ≤ 7 working days, ₹5,000/day after (RBC paras 58, 69) |
| LAS, LAMF | `CollateralHoldingsShared`, OTP evidence | DP and haircuts from FX | Pledge requested → created (gate) | INITIAL, then DRAWDOWN | Daily valuation; margin calls | Standard | `CollateralInvoked` by RE only | Pledge book vs depository or RTA (7.3) |
| Microfinance | Household, income, obligations (CF paras 51–57) | 50% household cap; loan card (RBC paras 78–80) | None | Borrower | Meeting schedule | 09:00–18:00 until 31 Dec 2026 (RBC para 91(2)); visits after two missed appointments (para 90); then per RBC Third Amendment [VERIFY: MFI window] | Conciliation, Lok Adalat | Household-cap breaches; income to CICs (CF para 54) |
| Supply chain, TReDS | Anchor, invoice, factoring-unit ids | Programme limit | Receivable assignment (platform files with CERSAI) | Seller | Buyer pays on due date | Against buyer | TReDS units without recourse to the MSME; no buyer set-off (TReDS Directions 2026, RBI/DPSS/2026-27/406) | Settlement vs due date; revolving behind flag [VERIFY: August 2026 draft] |
| Education | Institution, course dates, co-borrower | Standard | Optional | TRANCHE to institution | Moratorium via `ScheduleChanged` | Co-borrower rules | s.25 PSS or s.138, suit, conciliation | Disbursals vs fees |
| Specialist (RF, MED, LEF, DR; feasibility-gated) | As Personal plus end-use evidence; RF and DR: settlement evidence (`ADROutcomeRecorded`) or payoff letter | Feasibility note first; same-RE refinance is restructuring and needs a viability assessment (RSA paras 89, 169) | None, or as refinanced facility | End-beneficiary only: provider, counsel, settled creditor or existing lenders (CF para 10(1)) | Standard | Standard | As Personal; RF and DR carry the restructuring flag | Payoffs vs creditor confirmations |
| Project finance | Not Udofin | Gates (CF paras 67–75) | Common security | LIE-certified stages (para 75) | DCCO via `ScheduleChanged`; database ≤ 15 days (paras 77–78) | Lead lender | ICA votes (RSA paras 31–33); credit events to consortium (para 107); SARFAESI needs 60% by value (s.13(9)); IBC | Shares vs common agreement |
| Co-lent (any) | KFS item 5; single point of interface (TDCR paras 105–106) | Irrevocable back-to-back (para 112) | Joint security | Escrow only (para 117); split ≤ 15 days | Receipt allocation; classification T+1; own-share CIC reporting (para 122) | Servicer RE per CLA | Each RE settles its share (RSA para 16); SARFAESI 60% by value; transfer only under Part A with mutual consent (para 125); no LSP escrow role | Escrow three-way daily |

## 7.3 LAS and LAMF lifecycle

**Authority.** Finbyx (or the RE's certified LMS) owns the security master, haircuts, DP, LTV, margin calls, freezes, invocation and release; the depository or RTA is external truth for the encumbrance. Udofin shows indicative eligibility, orchestrates consent and OTP, displays RE values and captures cure intents. The RE (pledgee) contracts with the DPs, CDSL LAS API, NSDL e-pledge and the RTA or MF Central [VERIFY: direct or via aggregator]; Udofin runs borrower steps under the RE's credentials.

**Correction to `las.txt` (15 Oct 2026).** The proposal puts an "LAS risk / DP engine" (BE-11) in Udofin to compute eligible collateral, DP, shortfalls and the drawable amount. Not adopted: DP, LTV and margin actions are RE credit-risk decisions that cannot be outsourced to an LSP (OUT para 15; CF para 6(7)), so the engine runs in Finbyx; Udofin's BE-09 to BE-11 become a cached RE haircut table, a pledge-OTP orchestrator and a margin-call presenter, and the drawable amount comes from `GET /v1/facilities/{loan_id}/summary`. Its other controls (no shadow ledger, settlement proof before posting, idempotent money commands, three-way reconciliation) are adopted.

**States.** Pledge: `REQUESTED → PENDING_BORROWER_OTP → PENDING_DP_APPROVAL → ACCEPTED → CONFIRMED`, then `CLOSURE_REQUESTED → CLOSED` or `INVOCATION_REQUESTED → INVOKED`; failures `REJECTED`, `EXPIRED`, `FAILED`. Margin call: `OPEN → CURED`, or `OPEN → LAPSED → INVOCATION_REVIEW → INVOKED or WAIVED_BY_RE_AUTHORITY`.

| Step | Events and APIs | Rule and clock |
|---|---|---|
| 1. Holdings from CDSL LAS (eSign consent), NSDL statement, RTA or MF Central (OTP) | `ConsentRecorded`, `CollateralHoldingsShared` | Consent names RE and purpose (CF para 13) |
| 2. Indicative value = Σ units × price × (1 − haircut), capped | Haircut version in `ProductCatalogPublished`; eligibility-quote API | Labelled indicative; Group 1 only for capital-market loans above ₹5 lakh; no own shares; IPO ≤ ₹1 crore; no primary-gold-backed units (CF paras 104, 105, 106(2)(i), 35(2)) |
| 3. Application, sanction, KFS, signing | `ApplicationSubmitted`, `DecisionMade`, `KFSIssued`, `ESignCompleted` | RE decision (OUT para 15) |
| 4. Pledge or lien: borrower OTP; CDSL DP approval same day with reasons for rejection (CDSL/OPS/DP/POLICY/2026/468, 15 Jul 2026); NSDL pledgee acceptance; RTA lien for SOA units; depository pledge for demat units | `CollateralPledgeRequested`, `CollateralPledgeCreated` or `CollateralPledgeFailed` | Accepted NSDL pledge cannot be cancelled by pledgor; SEBI margin pledge (25 Feb 2020) is not an LAS rail |
| 5. Disbursement after sanction, documents, verified account, CONFIRMED pledge, sufficient DP | `LoanDisbursed` (INITIAL) | RE account to borrower (CF para 10(1)) |
| 6. Daily valuation on T-1 bhavcopy or AMFI NAV: DP = min(limit, eligible value after haircuts and caps); available = max(0, DP − utilised − reservations − dues); regulatory LTV = outstanding (principal, accrued interest and charges due) ÷ market value of pledged securities, tested separately from DP | `CollateralValuationUpdated` | Freeze drawdowns if prices > 1 business day old [REC] |
| 7. Drawdown via Udofin (FAPI 2.0) | `DrawdownRequested`, `LoanDisbursed` (DRAWDOWN) | Default term loan with DP-capped tranches; OD only behind `mod.las.revolving` pending the August 2026 draft CF amendment [VERIFY]; no automatic limit increase (CF para 8(2)) |
| 8. Margin call | `MarginCallRaised`, cure-intent API, `MarginCallCured` or `MarginCallLapsed` | Listed shares, NBFC assets ≥ ₹100 crore: 50% LTV at all times, cure in 7 working days (CF para 106(1)); others Board policy |
| 9. Invocation by RE after pre-invocation notice (ICA ss.176–177; SEBI circular 5 Feb 2026 [VERIFY]); DP invokes or RTA redeems to RE | `LegalNoticeIssued`, `CollateralInvoked`, `RecoveryReceiptPosted`, `SurplusRefunded` | Locked-in securities excluded; takeover and insider disclosures where triggered [VERIFY]; surplus to borrower |
| 10. Release on zero dues, no hold | `CollateralReleased`, `NOCIssued`, `LoanClosed` | ≤ 2 working days [REC] |
| 11. Corporate actions; quarterly pledged-share report to exchanges (CF para 106(2)(ii)); daily pledge reconciliation | `ReconciliationBreakRaised` | Quarterly; daily |

## 7.4 Daily reconciliation points

Applications sent vs acknowledged; KFS issued vs accepted in validity; disbursement UTRs (bank, Finbyx, mirror); RE collections vs allocation vs Udofin and agency receipts; collateral registers vs depository, RTA, Vahan, CERSAI, TReDS, vault; co-lending escrow three-way; DLG cover, invocations, shares and disclosure (CF para 28); LSP fees paid by the RE (CF para 10(4)); classification-sync timestamps; servicer remittances per transferee (TDCR paras 29–30, 41); legal status vs Equator and court feeds; settlements vs consent decrees (RSA para 100).

---

# 8 — EQUATOR RESOLUTION (AND OTHER ODR/ADR PROVIDERS) INTEGRATION

## 8.1 Role and principles

Equator is an **independent ODR institution**, not an agent of the RE or Udofin; common Infrabyx ownership is disclosed in every case and Equator is structurally separate (company, staff, panel, database, fee ledger) [VERIFY: legal opinion on Fifth Schedule justifiable doubts]. The integration is **provider-neutral** through `OdrProvider` (8.9); no other surveyed provider publishes a lender API (research B), so file and portal fallbacks exist. **Only the RE refers:** `adr.referral:create` is never issued to an LSP, agency or borrower product; Udofin may suggest ADR and relay requests.

## 8.2 Referral rules and gates

**[LAW] Arbitration basis.** Refer only where the loan agreement names Equator or another independent institution, or the borrower gives written post-dispute consent (A&C Act s.7; electronic form, s.7(4)(b)). The RE never appoints, nominates or offers a curated list (*Perkins Eastman v HSCC* (2020) 20 SCC 760; *CORE v ECI-SPIC-SMO-MCML (JV)*, SC Constitution Bench, 8 Nov 2024). Referral to a non-agreed ODR institution with the borrower silent made the award a nullity (*L&T Finance v Jai Paras Material Store*, Cal HC, 14 May 2026); a named institution is not unilateral (*Sundaram Finance v Hanuman Prasad*, Raj HC, 2026); repeated appointment of one arbitrator breached s.12 and Fifth Schedule items 22 and 24 (*Shikha Ghosh v Axis Bank*, Del HC DB, 30 Sep 2026; next date 17 Nov 2026) [VERIFY: outcome and any RBI direction].

| Gate (RS, before `ADRReferralCreated`; logged) | Result | Source |
|---|---|---|
| Bank or notified FI, claim ≥ ₹20 lakh | Arbitration blocked; other ADR allowed | *Vidya Drolia* (SC, 14 Dec 2020) |
| Mortgage enforcement in rem | Arbitration blocked for that relief | *Booz Allen* (2011) 5 SCC 532 |
| IBC moratorium (ss.14, 96, 101) | All ADR on hold | IBC |
| Fraud or wilful defaulter | Board approval; criminal track continues | RSA paras 16(5)(ii), 97 |
| Proceeding pending | Settlement needs consent decree | RSA para 100 |
| Consumer complaint pending | Cannot compel arbitration | *Emaar MGF v Aftab Singh* (2019) 12 SCC 751 |
| Clause absent, unilateral or no institution | Post-dispute e-signed consent or s.11 petition; never auto-refer | *L&T Finance* |
| s.21 notice lacks service evidence at known addresses and email | Blocked | *Sedhram Nilkanth Muglikar v M.R. Makhare* (Bom HC, 2026) |
| Suit route ≥ ₹3 lakh, no urgent relief | s.12A mediation (3 + 2 months) first | Commercial Courts Act s.12A; *Dhanbad Fuels* (SC, 15 May 2025) |
| Retail, contactable | Conciliation or Lok Adalat first [REC] | A&C Act Part III; LSA Act |

**Process status (19 Oct 2026).** **Conciliation** is the default enforceable route: a s.73 settlement authenticated by the conciliator has arbitral-award status (s.74, s.30), enforceable under s.36; 30 days' silence rejects an invitation (s.62(4)). **Mediation Act 2023:** only ss.1, 3, 26, 31–38, 45–47, 50–54, 56–57 in force (S.O. 4384(E), 9 Oct 2023); Mediation Council established 27 Aug 2026; ss.4–25, 27–30 and 39–44 (incl. s.27 enforcement, s.30 online mediation) not in force (s.26 is in force), so a private mediated settlement is only a contract [VERIFY: e-Gazette each release]. **Lok Adalat** awards are deemed decrees, final (LSA Act s.21); Permanent Lok Adalat covers financial services only where notified, up to ₹1 crore [VERIFY: per state]; next National Lok Adalat 12 Dec 2026 [VERIFY]. **Arbitration:** pleadings ≤ 6 months (s.23(4)); award ≤ 12 months from pleadings + 6 by consent (s.29A); fast track 6 months (s.29B).

## 8.3 Case state machine

```
DRAFT(RE) → REFERRED → SCREENING → {RETURNED_FOR_INFO | SCREEN_REJECTED | ACCEPTED}
ACCEPTED → NOTICE_ISSUED → {SERVED | SERVICE_FAILED → RE_SERVICE(n) → COURT_SUBSTITUTED_SERVICE}
SERVED → TRACK{NEGOTIATION | CONCILIATION | MEDIATION | ARBITRATION | LOK_ADALAT_HANDOFF}
CONC/MED: INVITED → {CONSENTED | DECLINED | DEEMED_DECLINED(30d)} → NEUTRAL_APPOINTED → SESSIONS
          → {SETTLEMENT_PROPOSED → SETTLED | NON_SETTLEMENT}
ARB: APPOINTMENT_PENDING → DISCLOSURE_FILED → CHALLENGE_WINDOW → CONSTITUTED → PLEADINGS(6m)
     → HEARING | DOCS_ONLY → AWARD_SIGNED → AWARD_STAMPED → AWARD_SERVED → CORRECTION(30d)
     → CHALLENGE_WINDOW(3m+30d) → {FINAL | CHALLENGED}
SETTLED | FINAL → COMPLIANCE → {PAID → CLOSED | BREACH → ENFORCEMENT_REFERRED → CLOSED}
any → WITHDRAWN | TERMINATED | STAYED | MANDATE_EXPIRED → MANDATE_EXTENDED(s.29A)
```

Transitions emit `ADRCaseStatusChanged`; consents `ADRConsentRecorded`; appointments `ADRNeutralAppointed`; hearings `ADRHearingScheduled`; deliveries `NoticeServiceUpdated`; outcomes `ADROutcomeRecorded`. A `SETTLEMENT_PROPOSED` outside the RE's mandate needs `SettlementApproved` before signing.

## 8.4 Data ownership and evidence pack

- **RE (FX, RS):** loan, KYC, contacts, statement of account, claim, agreement with clause and stamp proof, recall and s.21 notices, mandate and approvals, accounting, classification, CIC reporting, execution litigation. **Equator:** docket, panel, selection log, disclosures, orders, hearing records, original instruments and certified copies, service logs, fees. **Udofin:** presentation, grievance intake, relay only. DPDP: RE is fiduciary for loan data; Equator processes referral data and is fiduciary for case records [INTERP] [VERIFY: s.17(1)(a)].
- **Referral pack** (hash and JWS each): agreement with clause and stamp certificate, KFS, sanction letter, certified statement with electronic-record certificate (Bharatiya Sakshya Adhiniyam 2023 [VERIFY: section]), recall and s.21 notices with proofs, claim, authority letter, sealed settlement band. **Outputs:** notices, orders (no mediation record), s.73 or s.19 settlement, award (eSigned, e-stamped, PDF/A-2b), certified copies, non-settlement report.

## 8.5 Onboarding, hearings, outcomes and payment

- Borrowers enter per Part 4.4; staff and counsel by SCIM. Udofin shows only status, next action, hearing launch, RE payment instructions and outcome summary.
- Video, documents-only and witness sessions; venue distinct from seat (s.20(3)) [REC: borrower-proximate seat]; links ≥ 3 days ahead; **mediation and conciliation never recorded** (A&C Act s.75; Mediation Act ss.22–23 once in force).
- Instruments are eSigned and **e-stamped at signing**; late stamping needs impounding and penalty (*URC Construction v AAI*, Del HC, 1 Sep 2026) [VERIFY: article per state for s.73 settlements].
- RS starts s.33 (30 days) and s.34(3) (3 months + 30 days) clocks from each party's receipt and maps the outcome to the RE's settlement record (RSA paras 16(5), 89, 95, 100) or award execution; CIC "Settled" only for waivers for financial inability (CIR para 12(4)); Lok Adalat awards import as `OrderRecorded`.
- Payments go only to the RE via RE-issued links (CF para 10); receipts reach Equator as `RecoveryReceiptPosted`; a provider configuration that collects borrower money fails certification.

## 8.6 Independence controls

Random allocation from the provider's panel filtered by language, region and conflicts; the RE cannot pick, rank or veto. Per-lender concentration caps with a 3-year count against Fifth Schedule item 22 [VERIFY: defensible cap]; selection log (pool, exclusions, seed, counts). Sixth Schedule disclosure before acceptance; Seventh Schedule conflicts flagged; challenge within 15 days (s.13(2)). No outcome-linked fees, no neutral paid through RE counsel, no Finbyx or Udofin user as neutral; published rules, fees and code; annual independence audit.

## 8.7 Compliance monitoring, enforcement and fees

RS emits `ADROutcomeComplianceUpdated` from its ledger; Equator assembles the enforcement pack (certified instrument, stamp and service proofs, s.34 status). On breach RS emits `SettlementBreached` and opens `LitigationCaseOpened` (S36_EXECUTION) where assets lie (*Sundaram Finance v Abdul Samad* (2018) 3 SCC 622); High Courts split on executing unilateral-appointment awards, hence the gates. The referring RE pays published fees; debiting costs to the borrower depends on contract and RBC fair-practice rules [VERIFY]; GST on arbitral tribunal services is reverse charge (Notification 13/2017-CT(Rate), Sl. 3) [VERIFY].

## 8.8 Clocks and audit evidence

`ADRCaseStatusChanged.clocks` carries: s.62(4) 30 days; s.13(2) 15 days; s.23(4) 6 months; s.29A 12 + 6 months; s.29B 6 months; s.33 30/60 days; s.34(3) 3 months + 30 days; s.11 petition 3 years after failure to appoint on a valid s.21 notice (*Arif Azim v Aptech*, 2024); s.12A 3 + 2 months; Mediation Act s.18 120 + 60 days once in force. Evidence kept ≥ 12 years after closure [REC]: notice template hash, address source, per-channel delivery proof, selection log, disclosures, consent artefacts, attendance, eSign and e-stamp ids, fee receipts; no "deemed served" without evidence.

## 8.9 Provider-neutral adapter (`OdrProvider`)

Each capability (referral, withdrawal, mandate, documents, status, delivery, consent, appointment, hearing, outcome, party launch, Lok Adalat lists and awards) is declared as API, WEBHOOK, FILE or PORTAL_MANUAL. Equator native names map: case.refer → `ADRReferralCreated`; settlement.mandate → mandate API; case.screening_result, notice.dispatched, party.joined, tribunal.constituted, hearing.held, deadline.warning, challenge.notified, case.closed → `ADRCaseStatusChanged`; notice.delivery → `NoticeServiceUpdated`; consent.recorded → `ADRConsentRecorded`; neutral.appointed → `ADRNeutralAppointed`; hearing.scheduled → `ADRHearingScheduled`; settlement.proposed → `ADRCaseStatusChanged` (SETTLEMENT_PROPOSED) answered by `SettlementApproved`; settlement.executed and award.issued, stamped or served → `ADROutcomeRecorded`; payment.received → `RecoveryReceiptPosted`. Providers without APIs use `adr_referral_v1`, `adr_status_v1`, `adr_outcome_v1` (Part 12); Lok Adalat lists use registered DLSA formats [VERIFY: per DLSA].

---

# 9 — COMPLIANCE AND GRC INTEGRATION

## 9.1 Compliance-mode switch

Per RE tenant (and for Udofin's own compliance), recorded in `re_grc_link` and changed by configuration with maker-checker (Finbyx M14; Udofin Part 2): **EMBEDDED** (Finbyx compliance module), **LDC_EXTERNAL** (LawDocsComply; products push evidence and pull obligations), **LDC_GROUP** (one instance per `group_id`, every record tagged by `reid`, group roll-ups), **THIRD_PARTY_GRC** (RE's tool via certified adapter), **EXPORT_ONLY** (evidence packs and OSCAL; Udofin default until a bridge exists). A switch never loses data: the outgoing system exports obligations, controls, open issues and the evidence index with hash-chain heads; the incoming system imports before the effective date; producers dual-publish for one compliance period. The grievance-host switch is separate.

## 9.2 Generic GRC connector contract

REST (JSON Schema 2020-12, cursor pagination) plus event push and periodic OSCAL; `Idempotency-Key` on every POST; users by SCIM with OIDC or SAML; machines by mTLS-bound client credentials. Evidence is hash-chained, stored in India in the producing product, with aggregate counts and masked sample ids, never raw personal data; GRC systems hold references and hashes.

| Resource | Key fields | Event | OSCAL |
|---|---|---|---|
| `Obligation` | obligation_ref, paragraph, text hash, applicability, dates, owner, status | `ObligationPublished` | catalog, profile |
| `Control` | obligation_refs, component, frequency, automated | — | component-definition |
| `ControlTestResult`, `Evidence` | run, period, result, population, masked sample, artefact hashes, signer | `ControlTestResultPublished`, `EvidenceSubmitted` | assessment-results |
| `Issue` | source (TEST, AUDIT, RBI, INCIDENT), severity, owner, due | `ComplianceIssueRaised` | plan-of-action-and-milestones |
| `Incident` | detected_at, notified_re_at, rbi_reported_at | `SecurityIncidentNotified` | — |
| `RegulatoryReturn`, `PolicyAttestation` | code, period, status, ack; policy, version, Board date, user | `ReturnStatusUpdated`, `PolicyAttested` | — |
| `OutsourcingArrangement`, `KRI`, `RegulatoryChange` | provider, materiality, group flag (OUT paras 45–51, 90–92), data location; metric, threshold; impacted obligations | `ObligationPublished` (changes) | — |

**Minimum control feed:** classification sync T+1 (TDCR para 124); agent notice before contact (CF para 9(6)); contact windows (RBC paras 90, 91(2), 100); same-day agent cash posting (CF para 10(5)); no LSP-controlled account (CF para 10); KFS before execution (RBC para 29); DLG cap, window and disclosure (CF paras 24, 27, 28); release timelines (RBC paras 35, 58, 69); settlement approval and cooling (RSA paras 16(5), 95); ADR basis (A&C Act ss.7, 12); consentref (CF para 13); incident notice (OUT para 61).

## 9.3 LawDocsComply native connector

Checkpoint banks → `Obligation` (each checkpoint carries the canonical `obligation_ref`); questionnaire responses and product tests → `ControlTestResult`; calendar → returns and policy reviews; litigation module → consumer of the five litigation events. LawDocsComply (Node, TypeScript, MongoDB) builds the connector in its own repository against this specification and certifies it like any other [VERIFY: public API; one-to-one mapping of questionnaire rows to OSCAL controls].

## 9.4 OSCAL and third-party GRC adapters

On request, a JWS-signed OSCAL JSON package (NIST OSCAL v1.2.x: catalog, profile, component-definition, system-security-plan, assessment-results, plan-of-action-and-milestones). Adapters are versioned mapping packs (10.3): **MetricStream** (OpenAPI REST, REST or Kafka connectors, bulk loads); **ServiceNow IRM** (Policy and Compliance staging tables; roles `sn_compliance.admin`, `sn_grc_cim.admin`; never core tables); **Archer** (REST, Content and GRC APIs); **IBM OpenPages** (GRC REST, App Connect, regulatory-content connectors); **Komrisk, Komply360, Compfie, TeamLease RegTech, Lawrbit, OnFinance** (REST where available, else CSV or OSCAL) [VERIFY: APIs per tool]; others through 9.2.

---

# 10 — THIRD-PARTY INTEGRATION FRAMEWORK

## 10.1 Connector SPI and certification

Every connector implements `@infrabyx/connector-sdk` and runs out of process with APIs and events only:

```ts
interface Connector {
  manifest(): ConnectorManifest;            // id, version, counterparty, capabilities, schemas, scopes, residency
  capabilities(): CapabilityDeclaration[];  // API, WEBHOOK, POLL, FILE or PORTAL_MANUAL per capability
  healthCheck(ctx: TenantContext): Promise<Health>;
  send(ctx: TenantContext, event: CloudEvent): Promise<DeliveryResult>;     // canonical → counterparty
  receive(ctx: TenantContext, raw: InboundMessage): Promise<CloudEvent[]>;  // counterparty → canonical
  call(ctx: TenantContext, op: OperationId, body: unknown, idemKey: string): Promise<OperationResult>;
  reconcile(ctx: TenantContext, businessDate: string): Promise<ReconciliationReport>;
}
```

`TenantContext` carries `tenantid`, `reid`, a vault handle, mapping version and environment; calls without RE context fail. Third-party connectors also need residency and sub-processor review, VAPT ≤ 12 months old, and the outsourcing clauses in the counterparty contract (OUT paras 33–34, 74).

## 10.2 Adapter catalogue

| Category | Examples | Pattern and rules |
|---|---|---|
| LOS/LMS in place of Finbyx | Apache Fineract and Fineract-based cores (`/fineract-provider/api/v1/`), vendor cores | Certified lender connector, generic REST or webhook, or SFTP; that LMS becomes system of record [VERIFY: Fineract external events in deployed version] |
| Accounting | TallyPrime (XML over HTTP port 9000 or file), SAP S/4HANA (OData, BAPI_ACC_DOCUMENT_POST, ACC_DOCUMENT IDoc), SAP Business One, Zoho Books, CSV | `AccountingSink` from the RE ledger; hashed, signed, no manual edits (CYB paras 119–120) [VERIFY: SAP per release] |
| Legal-tech, court data | eCourts CNR [VERIFY: NBFC API eligibility], aggregators, e-DRT (no API found), NCLT, e-Jagriti, LawDocs | CNR polling, cause-list match, orders; counsel updates prevail |
| E-auction | BAANKNET (mandatory for IBC liquidation auctions noticed from 1 Apr 2025), C1 India, auctiontiger, MSTC, Shriram Automall | `AuctionPlatformAdapter`: listing, EMD and bidder KYC, bid log, result [VERIFY: NBFC access and APIs] |
| Agencies, diallers | Agency portals, Credgenics, Spocto, 1600-series voice vendors | Allocations in, activity out; police verification (RBC paras 93–99); IIBF from 1 Jan 2027 [VERIFY] |
| Notice dispatch | India Post bulk API (CEPT onboarding), couriers, DLT SMS, email, print-to-post | → `NoticeServiceUpdated`; Registered Post merged into Speed Post (1 Sep 2025); WhatsApp never used for collection, recovery or legal notices (WhatsApp Business Messaging Policy bars debt collection; Finbyx 7A.0.6 guard-rail, Udofin UR3) |
| ODR providers | Equator, Presolv360, Sama, Jupitice, CADRE, Webnyay | `OdrProvider` (8.9) |
| Depository, RTA, registries, KYC, bureau, AA, eSign, payments | NSDL, CDSL, CAMS, KFintech, MF Central, CERSAI, Vahan, TReDS, CGTMSE; Finbyx and Udofin Part 9.2 | RE contracts where law requires; no LSP account in money flows [VERIFY: Vahan financier API] |

## 10.3 Data-mapping configuration

Each adapter ships a semantically versioned mapping pack (`infrabyx-contracts/mappings/[connector-id]/[version]/mapping.yaml`): canonical JSON Pointer ↔ counterparty field maps, code-table maps, approved transformations, defaults, validation rules and golden fixtures run in CI. Tenants override only `x-tenant-overridable` fields by maker-checker, creating a patch version (`1.4.0+re_01J…`); meaning-changing edits need recertification.

---

# 11 — EXTENSIBILITY AND NEW PRODUCTS

## 11.1 Module registry, entitlement and lifecycle

- **`module.yaml`** per attachable module (Recovery Suite modules, product templates, connectors, apps): `id` (`namespace.module`), `version`, `product`, `requires`, `capabilities`, `events_produced`, `events_consumed`, `apis`, `permissions`, `data_categories`, `regulatory_refs`, `retention_class`, `licence_sku`, `ui_slots`, `migrations`.
- **Entitlement** is checked server-side on every call and handler through an OpenFeature-compatible provider (SKU, tenant, entity, product family, branch, role); flag keys `mod.[id].[capability]` (e.g. `mod.recovery.adr.referral`, `mod.las.revolving`).
- **Lifecycle:** `AVAILABLE → LICENSED → INSTALLED → CONFIGURED (maker-checker) → CERTIFIED → ENABLED → READ_ONLY → DETACHED`; `ModuleAttached` on ENABLED, `ModuleDetached` on entering READ_ONLY (writes stop); the export pack is produced before DETACHED. **Detaching never deletes regulated records:** recovery, litigation and ADR files stay on legal hold until closure plus retention; KYC and transaction records follow PMLA and the KYC Directions [VERIFY: periods]. Detachment is blocked while statutory clocks are open (s.34 window, SARFAESI balance deadline, s.138 complaint deadline) unless each is transferred with acknowledgement.

## 11.2 Extension points and SDK

Extension points: event subscriptions, gateway APIs, external task workers claiming named queues (`fi.visit`, `notice.print`, `valuation.report`, `counsel.update`) through a task API with tenant-scoped tokens (Finbyx 7A.0.7), GoRules JDM rule tables per tenant and product, document template packs, Temporal workflow hooks, UI slots, mapping packs, export layouts. The SDK provides envelope validation, registry client, Standard Webhooks and RFC 9421 signing, idempotency, outbox and inbox helpers, mapping runtime, simulators and the certification runner.

## 11.3 Onboarding a new ecosystem app

Checklist: (1) legal role per RE (OUT Ch III or IV), materiality, group policy (OUT paras 45–51, 90–92), OUT paras 34 and 74 clauses; (2) DPIA, India-only, need-to-know (OUT para 24), `x-dataclass` per field, no phone-resource access in borrower components (CF para 13(1)); (3) OIDC, SCIM, product roles, MFA; (4) registered events, APIs and files with AsyncAPI, OpenAPI and Pact; (5) mTLS, RFC 9421 keys, VAPT, SBOM, SIEM feed, incident notice enabling the RE's 6-hour report (OUT para 61); (6) manifest, SKU, flags; (7) BCP and DR tests, exit plan, RE outsourcing-register entry; (8) for recovery use, agent authorisation and ID, contact-policy engine, grievance routing; (9) certification, `ConnectorCertified`, evidence to GRC.

**Worked example — field-investigation app:** service provider to the RE (OUT Ch III), not an LSP unless it performs digital lending functions. Consumes `VerificationRequested`, `CollectionAllocated` and `CollectionDeallocated` (where the RE appoints its agents), `LegalHoldChanged`, `ConsentWithdrawn`. Produces `VerificationCompleted`, `FieldVisitLogged`, `CollectionActivityLogged`, `PTPCaptured`, `ReceiptIssued`, `RiskSignalRaised`, `SecurityIncidentNotified`. Address token resolved only at visit time; premises photos only; geo, time and evidence hashes; scopes `collections.allocation:read`, `collections.activity:write`; contact-policy check before each visit; findings feed Finbyx R2 and the service-proof register (affixation, hand delivery); certification adds offline-sync idempotency tests.

## 11.4 Naming rules and standalone Udolex

Event names PascalCase, past tense, unique, never product-prefixed; API paths plural with action sub-resources; schema subjects `[domain]/[EventName]` and `.lsp`; connector ids `[counterparty]-[capability]-[product]`; identifiers prefix + ULID, never reused. **Udolex** changes only `source` (`urn:infrabyx:udolex:[tenantid]`); the ledger stays in the RE's LMS and `RecoveryReceiptPosted` becomes a posting request confirmed by the LMS's `PaymentReceived`.

---

# 12 — DATA EXPORT AND INTEROPERABILITY FORMATS

| Format | Use | Specification |
|---|---|---|
| CSV, XLSX, JSON, NDJSON, XML | Registers, lists, bulk and counterparty layouts | RFC 4180 UTF-8 CSV; JSON Schema 2020-12 or XSD per layout |
| PDF/A | Notices, awards, orders, statements, evidence packs | PDF/A-2b; XMP block with document_id and source hash; eSign, DSC or PAdES |
| Tally XML | Journals to TallyPrime | ENVELOPE, HEADER (Import Data), BODY, IMPORTDATA, REQUESTDESC, REQUESTDATA, TALLYMESSAGE; port 9000 or file |
| SAP | Journals to S/4HANA or ECC | ACC_DOCUMENT IDoc, BAPI_ACC_DOCUMENT_POST or OData [VERIFY: per release] |
| XBRL | Where a regulator requires it (e.g. MCA) | Filing taxonomy; RBI returns moving to CIMS templates [VERIFY: NBFC returns] |
| CloudEvents batch | Replay and file fallback | `application/cloudevents-batch+json` or NDJSON |

**Registered layouts (minimum):** `loan_master_v1`, `schedule_v1`, `payment_v1`, `collateral_register_v1`, `pledge_position_v1`, `dlg_position_v1`, `colending_escrow_v1`, `recovery_case_v1`, `notice_register_v1`, `service_proof_v1`, `litigation_register_v1`, `settlement_register_v1`, `adr_referral_v1`, `adr_status_v1`, `adr_outcome_v1`, `asset_sale_v1`, `possessed_assets_web_v1` (monthly website list, CIR para 21), `agency_list_web_v1`, `gl_journal_v1`, `grc_evidence_index_v1`, `reconciliation_breaks_v1`.

**Dictionaries and checksums.** Each layout's dictionary gives field, canonical JSON Pointer, type, length, mandatory flag, `x-dataclass` and code table; each file has a JWS-signed manifest with counts, control totals and SHA-256 (3.11). Detached-module and tenant-exit exports (Finbyx Part 10.6 item 24) use these layouts.

---

# 13 — SECURITY, PRIVACY AND AUDIT

## 13.1 Legal baseline

DPDP Act 2023 and Rules 2025 (notified 14 Nov 2025, phased over 12–18 months) apply alongside RBI rules, the stricter prevailing [VERIFY: commencement per provision]; each product records its fiduciary or processor role per purpose. RBI digital-lending data rules (CF paras 13–15) and outsourcing and cyber rules (OUT paras 28, 34, 61, 74, 81, 97(vii)(b); CYB paras 119–120) are implemented through Parts 2, 3 and 6; each product also meets its own CERT-In reporting duties [VERIFY: timelines].

## 13.2 Data classification per field

| Class | Examples | Handling |
|---|---|---|
| `PUBLIC`, `INTERNAL` | Disclosures; configuration, aggregates | None; authenticated |
| `CONFIDENTIAL` | Settlement mandates, selection logs, commercial terms | Need-to-know, encrypted |
| `PII` | Name, contact, address, masked ids | Consent or legal basis; role masking; never logged |
| `SPI` | Clear PAN or account, KYC images, V-CIP recordings, health data | Field encryption; RE-scoped vault; RE only |
| `FINANCIAL` | Balances, payments, classification | RE and authorised projections |
| `LEGAL` | Notices, pleadings, orders, awards, privileged advice | Legal-hold aware; privileged material leaves RS only with counsel approval |

The envelope `dataclass` is the highest field class; gateways reject messages above the consumer's scope.

## 13.3 Keys, logging, retention, incidents and audit

- **Keys:** per-tenant envelope keys in India KMS; BYOK or HYOK for ML/UL tenants; signing keys HSM-backed, rotated annually with overlapping JWKS; webhook secrets every 90 days.
- **Logging:** no Aadhaar, PAN, OTP, account numbers, bureau data or images in logs, traces, analytics, push payloads or DLQ metadata.
- **Retention:** KYC and transaction records 5 years after relationship or transaction (PMLA s.12; KYC para 47); call recordings ≥ 6 months, longer if sub judice (RBC Third Amendment para 100P [VERIFY]); recovery and litigation records until proceedings close plus the 12-year execution period (Limitation Act Art. 136) [REC]; ADR records ≥ 12 years [REC]; event replay per 3.5; security logs ≥ 180 days in India [VERIFY: CERT-In]. `LegalHoldChanged` suspends deletion across all copies; DPDP erasure applies only where no retention or hold applies, and the requester is told what was kept and why.
- **Incidents:** detection → triage (≤ 30 minutes, severity 1) → `SecurityIncidentNotified` to each affected RE (≤ 2 hours) → updates by `update_seq` → RCA → lessons learned (ORM paras 99–101) → closure; the RE, never the provider, files with RBI.
- **Audit:** message hashes, retained signatures, hash-chained decision events, time-boxed read-only access for RE auditors and RBI.

---

# 14 — VERSIONING, CHANGE CONTROL AND CERTIFICATION

## 14.1 Versions

Specification: **major** for breaking meaning, ownership or mandatory fields; **minor** for new events, APIs, optional fields, codes or connectors; **patch** for clarifications; a revision-log appendix starts at v1.1. Schemas are BACKWARD-compatible within a major; a breaking change publishes `v[major+1]` and both run ≥ 90 days. Superseded API majors return `Deprecation` (RFC 9745) and `Sunset` (RFC 8594) headers. Connectors recertify when a field they use changes.

## 14.2 Change process

Proposal `infrabyx-contracts/proposals/[date]-[slug].md` (motivation, regulatory basis, affected products, events, APIs, schemas, mappings, tests, rollout, rollback) → impact review by each product lead → approval by every affected owner in the pull request → registry, SDK and Pact publication → parallel run and recertification → propagation within 10 working days.

## 14.3 Certification suite

| Group | Tests |
|---|---|
| Contract | Messages validate; required attributes; projections carry no forbidden fields |
| Security | mTLS enforced; RFC 9421 verified; tampered body, wrong key, stale timestamp rejected; scope, audience and tenant isolation enforced |
| Idempotency and ordering | Duplicates harmless; key reuse with new body gives 422; concurrent retry gives 409; out-of-order resolved; replay reproduces state |
| Resilience | 4-hour outage; slow and partial failures; DLQ replay under maker-checker; per-tenant circuit breakers |
| Regulatory guards | LSP-controlled account rejected; referral without basis rejected; Udofin cannot refer, approve, issue notices or invoke; personal data without consentref rejected; contact before agent notice blocked |
| Reconciliation and privacy | Synthetic month reconciles; injected breaks caught; withdrawal stops processing; legal hold blocks erasure; no personal data in logs |
| Operations | Health, metrics, traces, monitor visibility |

Results emit `ConnectorCertified` and `ControlTestResultPublished`.

---

# 15 — ROLLOUT PLAN ACROSS PRODUCTS

| Phase | Implements | Exit evidence |
|---|---|---|
| Finbyx 8c | Part 3 core; 6.2–6.4; consentref | Pact with Udofin; Finbyx runs with Udofin down |
| Udofin 9 | LSP side of 8c; generic LOS/LMS connector; certification runner | Finbyx connector certified |
| Finbyx 12 — Recovery Suite core | 6.7 (`RecoveryAgentNoticeSent`); 6.8 case, strategy, notice, service, receipt and closure events (settlement events in 12b; repossession, auction and surplus in 17b); 6.10; `LegalHoldChanged`; dispatch and court-data adapters; module registry, attach and detach (11.1); recovery layouts | Attach and detach with export pack |
| Finbyx 12b — Settlement and ADR with Equator | 6.9; Part 8 gates and `OdrProvider`; settlement events | Equator certified; referral to compliance on sandbox |
| Udofin 12b — Recovery support, notices, ADR access | LSP projections; settlement relay and acceptance; agent-notice gate; Equator launch (4.4) | Guard tests pass |
| Udofin 13 — DLG | DLG domain (6.11) | Disclosure and ledger reconciliation |
| Finbyx 16 | 6.6; RE-side DLG | T+1 sync; three-way escrow |
| Finbyx 16b — Ecosystem integration hub v2 | Part 7 lifecycles incl. LAS; Parts 9, 10, 12; certification service; privacy and incident events | All connectors certified; OSCAL package |
| Udofin 16b — Ecosystem integration v2 | Part 7 incl. LAS event contracts; Equator; GRC; privacy and incident events (first built in Udofin Phases 3b and 16) | Recertified; Pact suite passes per product lifecycle |
| Finbyx 17 — Secured products | Collateral domain (6.5); LAS engine (7.3) | Pledge, valuation, margin call, release on sandbox rails |
| Finbyx 17b — Secured enforcement and shared-exposure recovery | Repossession, auction, surplus, invocation; e-auction listings through the 16b adapter; ICA votes; shared-exposure rules | Statutory-clock tests pass |
| Udofin 18, 18b | LAS, Home, LAP, Vehicle; then Gold, MSME, Microfinance, Supply-chain and TReDS, Education (Products 11–15) | Per-product fixtures pass; LAS journey end to end on the Finbyx 17 sandbox |
| LawDocsComply | 9.3 connector | Certified against both 16b phases |

**Sequencing:** Udofin 16b needs the Finbyx 16b sandbox; Udofin LAS needs Finbyx 17; Finbyx 12b production needs Equator certification.

---

# APPENDIX A — EXAMPLE PAYLOADS

Illustrative: identifiers, hosts and values are synthetic; `registry.infrabyx.example` stands for the registry host fixed by ADR. A.1 shows the full envelope; A.2–A.5 abbreviate the common attributes as `"…"`.

**A.1 `ApplicationSubmitted` (Udofin → Finbyx)**

```json
{"specversion": "1.0", "id": "01a152c9-ead8-7b2e-9a1d-3f6c2b8e4d10",
 "source": "urn:infrabyx:udofin:ten_01J9ZQ8K7H", "type": "in.infrabyx.origination.ApplicationSubmitted.v1",
 "subject": "app_01J9ZQB3W4X6", "time": "2026-10-19T11:42:07+05:30", "datacontenttype": "application/json",
 "dataschema": "https://registry.infrabyx.example/schemas/origination/ApplicationSubmitted/1.2.0.json",
 "tenantid": "ten_01J9ZQ8K7H", "reid": "re_01J8Y2M0PQ", "productfamily": "PL",
 "correlationid": "app_01J9ZQB3W4X6", "consentref": "cns_01J9ZQA9R2T5", "dataclass": "PII",
 "schemaver": "1.2.0", "seq": 1, "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
 "data": {"lsp_application_ref": "UDF-APP-2026-000184321", "product_code": "PL-SAL-01", "dla_id": "dla_01J5UDFANDR",
  "requested_amount": {"amount": "250000.00", "currency": "INR"}, "tenor_months": 24,
  "applicants": [{"role": "PRIMARY", "party_ref": "pty_ud_fx_01J9ZQC0MN", "pan_masked": "XXXXX1234X",
    "pan_token": "tok_pan_6f1c9e", "household": {"members": 3, "annual_income": "1020000.00"}}],
  "kyc_evidence_refs": [{"type": "DIGILOCKER_AADHAAR_XML", "evidence_id": "evd_01J9ZQ9ABC", "sha256": "9d3f…a5d7f9"}],
  "environment": "PRODUCTION"}}
```

**A.2 `CollateralPledgeCreated` for LAS (Finbyx → Udofin)**

```json
{"…": "…", "source": "urn:infrabyx:finbyx:ten_01J8Y2M0PQ", "type": "in.infrabyx.collateral.CollateralPledgeCreated.v1",
 "subject": "col_01J9ZTR5KQ2M", "productfamily": "LAS", "consentref": "cns_01J9ZT90QW", "dataclass": "FINANCIAL", "seq": 3,
 "data": {"pledge_request_id": "plr_01J9ZTQ0HH", "application_id": "app_01J9ZT8P1A2B", "collateral_type": "LISTED_SHARE_DEMAT",
  "provider": "CDSL", "pledge_ref": "PLG-2026101900045871", "pledgor_boid_token": "tok_boid_44a1c0", "status": "CONFIRMED",
  "securities": [{"isin": "INE000A01019", "units": "1200", "price": "1530.25", "price_source": "NSE_BHAVCOPY",
    "price_as_of": "2026-10-16", "haircut_pct": "50.00", "eligible_value": {"amount": "918150.00", "currency": "INR"}}],
  "haircut_table_version": "LAS-HC-2026.10.1", "regulatory_basis": "CF para 106(1)",
  "confirmed_at": "2026-10-19T15:07:58+05:30", "provider_evidence": {"provider_txn_id": "CDSL-LAS-7781202", "sha256": "e3b0…b855"},
  "disbursement_gate_satisfied": true}}
```

**A.3 `LegalNoticeIssued` (Recovery Suite → dispatch adapters)**

```json
{"…": "…", "type": "in.infrabyx.recovery.LegalNoticeIssued.v1", "subject": "rc_01J9ZW1F4K7P", "productfamily": "LAP",
 "legalbasis": "LEGAL_CLAIM", "dataclass": "LEGAL", "seq": 7,
 "data": {"notice_id": "ntc_01J9ZW8Q2R5T", "instrument": "S13_2",
  "statute_ref": "SARFAESI Act s.13(2); Security Interest (Enforcement) Rules r.3",
  "eligibility_checks": {"sarfaesi_notified": true, "cersai_ref": "CERSAI-SI-400012345678", "time_barred": false},
  "template": {"template_id": "tpl_s13_2", "version": "3.1.0"},
  "addressees": [{"party_ref": "pty_fx_01J7MORTGAGOR", "role": "BORROWER"}],
  "dues_snapshot": {"as_of": "2026-10-19", "total": {"amount": "3710810.40", "currency": "INR"}}, "cure_period_days": 60,
  "document": {"document_id": "doc_01J9ZW8Z0Y", "sha256": "4f2a…4f6a", "pdfa": "PDF/A-2b"},
  "signer": {"role": "AUTHORISED_OFFICER", "signature_type": "DSC"}, "dispatch_modes": ["SPEED_POST_POD", "COURIER", "EMAIL"]}}
```

**A.4 `ADRReferralCreated` (Recovery Suite → Equator)**

```json
{"…": "…", "type": "in.infrabyx.adr.ADRReferralCreated.v1", "subject": "adrref_01J9ZX4M8N2Q", "productfamily": "PL",
 "correlationid": "rc_01J9ZX0A1B2C", "legalbasis": "LEGAL_CLAIM", "dataclass": "LEGAL", "seq": 1,
 "data": {"provider": "EQUATOR", "process": "CONCILIATION", "basis": "CONCILIATION_INVITATION",
  "clause": {"names_institution": "EQUATOR", "clause_ref": "LA-PL-2025-v4 cl.21", "stamp_certificate": "IN-DL-2025-0091812"},
  "gate_result": {"rule_version": "ADR-GATES-2026.10", "blocked": []},
  "claim": {"as_of": "2026-10-19", "total": {"amount": "158711.55", "currency": "INR"}},
  "parties": [{"party_ref": "pty_fx_eq_01J9ZX5P", "role": "RESPONDENT", "contact_tokens": ["tok_mob_19ab", "tok_eml_77cd"]}],
  "referral_pack": [{"type": "LOAN_AGREEMENT", "document_id": "doc_01J5LA0001", "sha256": "aa11…dd66"}],
  "settlement_mandate_ref": "mdt_01J9ZX4SEAL", "udofin_presentation_permitted": true,
  "approval_ref": "apr_01J9ZX49QQ"}}
```

**A.5 `ADROutcomeRecorded` (Equator → Recovery Suite)**

```json
{"…": "…", "source": "urn:infrabyx:equator:ten_eq_01J8Y2RE", "type": "in.infrabyx.adr.ADROutcomeRecorded.v1",
 "subject": "adr_01J9ZX7C3D4E", "reid": "re_01J8Y2M0PQ", "legalbasis": "LEGAL_CLAIM", "dataclass": "LEGAL", "seq": 14,
 "data": {"outcome_seq": 1, "outcome_type": "CONCILIATION_SETTLEMENT_S73",
  "legal_effect": "Arbitral award on agreed terms (A&C Act ss.74, 30); enforceable under s.36",
  "within_re_mandate": true, "settlement_approval_ref": "stl_01J9ZY0APP",
  "terms": {"amount": {"amount": "132000.00", "currency": "INR"}, "instalments": [{"due_date": "2026-12-05", "amount": "66000.00"},
    {"due_date": "2027-01-05", "amount": "66000.00"}], "payee": "re_01J8Y2M0PQ", "restructuring_flag": false},
  "instrument": {"document_id": "doc_eq_01J9ZZ1SET", "sha256": "5a6b…5a6b", "pdfa": "PDF/A-2b",
    "signatures": ["ESIGN_PARTY", "DSC_RE", "DSC_CONCILIATOR"]},
  "e_stamp": {"certificate_no": "IN-DL-2026-11-0041771", "state": "DL", "stamped_at": "2026-11-21T16:40:02+05:30"},
  "served_at": "2026-11-21T18:05:11+05:30", "clocks": {"s33_correction_end": "2026-12-21", "s34_challenge_end": "2027-02-21", "s34_outer_limit": "2027-03-23"}}}
```

---

# APPENDIX B — GLOSSARY

**A&C Act** Arbitration and Conciliation Act 1996 · **AA** Account Aggregator · **ADR** negotiation, conciliation, mediation, arbitration, Lok Adalat · **CERSAI** Central Registry of Securitisation Asset Reconstruction and Security Interest of India · **CF** NBFC Credit Facilities Directions 2025 (RBI/DOR/2025-26/347) · **CIR** Credit Information Reporting Directions (349) · **CYB** Cybersecurity, Technology Risk, Resilience and Assurance Directions (461) · **CLA** co-lending arrangement · **DLA** digital lending app · **DLG** default loss guarantee · **DP** drawing power (or depository participant) · **DPDP** Digital Personal Data Protection Act 2023 and Rules 2025 · **FAPI 2.0** OpenID Financial-grade API Security Profile · **ICA** inter-creditor agreement · **IRACP** Income Recognition, Asset Classification and Provisioning Directions (356) · **KFS** Key Facts Statement · **LAS, LAMF** loans against securities and mutual funds · **LSP** lending service provider · **ODR** online dispute resolution · **OSCAL** NIST Open Security Controls Assessment Language · **OUT** Managing Risks in Outsourcing Directions (363) · **RBC** Responsible Business Conduct Directions (362) · **RE** regulated entity · **RS** Recovery, Litigation and ADR Suite · **RSA** Resolution of Stressed Assets Directions (357) · **RTA** registrar and transfer agent · **SEC** Securitisation Transactions Directions (353) · **TDCR** Transfer and Distribution of Credit Risk Directions (352) · **TReDS** Trade Receivables Discounting System · **Udolex** standalone Recovery Suite.

---

## SOURCES

**RBI Directions supplied by the project owner** (paragraphs checked against the texts in `md/` and `md2/`): CF 347; CIR 349; TDCR 352; SEC 353; IRACP 356; RSA 357; RBC 362; OUT 363; KYC 361; CYB 461; FRM 463; CMP 460.

**Research notes (19 Oct 2026):** `v14/research_A_recovery_law.md`, `v14/research_B_adr_odr.md`, `v14/research_C_recovery_tech.md`, `v14/research_D_integration.md` (full case citations and URLs). **Owner files:** `v14in/las.txt` (LAS proposal, 15 Oct 2026; corrected in 7.3); Finbyx Master Prompt v1.3 (Parts 2, 5, 6, 9, 10, M14, M15, M21); Udofin Master Prompt v1.0 (Parts 2, 4, 5, 6, 9, 10, U18, U21).

**Standards:** CloudEvents 1.0.2; OpenAPI 3.1.1 and 3.2.0; AsyncAPI 3.0; JSON Schema 2020-12; Standard Webhooks; draft-ietf-httpapi-idempotency-key-header-07; RFC 9421, 9530, 9457, 9562, 7515, 7797, 8705, 7523, 9126, 9449, 8693, 9700, 7643, 7644, 8594, 9745; OAuth 2.1 draft; FAPI 2.0 Security Profile (Final, Feb 2025); NIST OSCAL v1.2.x; W3C Trace Context; OpenFeature.

**Market infrastructure:** NSDL pledge services; CDSL LAS and communiqué CDSL/OPS/DP/POLICY/2026/468; TReDS Directions 2026 (RBI/DPSS/2026-27/406); India Post CEPT SOP v6.1; TallyPrime XML reference; MetricStream, IBM OpenPages, ServiceNow IRM and Archer documentation; IBBI BAANKNET circulars; WhatsApp Business Messaging Policy.
