# Appendix X — Operations Hub Addendum for LawDocsComply

**LawDocsComply Build Prompt Pack v1.0 · 25 October 2026 · Addressed to the Infrabyx Operations Hub (OH) build (Master Prompt v1.0, 24 Oct 2026) · Implements decision D-03 (CRM, marketing, brand/social/PR, staff HRMS, payroll, appraisal, internal controls and group billing live in OH; LawDocsComply builds a Service Delivery Console)**

> **How to use.** Commit this appendix to the OH repository as `docs/ecosystem/ldc-addendum.md` and raise each "OH change" below through the Integration Specification change process (Ecosystem Spec §14.2) where it adds or alters a cross-product contract. Items marked **Confirm** are already in OH v1.0 and need only LDC-specific configuration. Items marked **Add** are new requirements. Items marked **Decide** need an owner decision.

## X.0 Summary of changes requested

| # | Area | Type | Summary | OH module | LDC phase |
|---|---|---|---|---|---|
| X.1 | Legal entity and workspace | Confirm / Decide | LDC selling entity, GSTINs, workspace N for LDC staff, merchant of record for LDC services | OH1, OH8 | P20, P21 |
| X.2 | CRM objects and APIs | Add | LDC-specific account/lead fields, health-check lead source, CRM activity API for the delivery console | OH3 | P20, P22, P23 |
| X.3 | Self-serve provisioning and trials | Add / Decide | `TenantSelfServeCreated` event; production-grade LDC trials with click-wrap DPA (deviation from OH8.9) | OH4, OH8 | P20 |
| X.4 | Onboarding factory playbooks | Add | LDC implementation templates, migration datasets, milestone codes | OH4 | P20, P22 |
| X.5 | Customer-success signals | Add | `ClientHealthSignal` aggregates; LDC confidentiality filter | OH5, OH2 | P22 |
| X.6 | Support routing | Confirm / Add | LDC ticket categories, regulatory-impact rules, billing disputes | OH6 | P20, P22 |
| X.7 | Marketing and growth | Confirm / Add | Health-check nurture, webinar programmes, Academy cross-promotion, claims gate for savings statistics | OH7, OH14 | P20, P23 |
| X.8 | Revenue catalogue and billing | Add | LDC SKUs, meters, stream codes incl. `MARKETPLACE_COMMISSION`, catalogue change-request API, trial-extension sync, marketplace first-party SKUs | OH8 | P20, P21 |
| X.9 | Professional directory | Confirm / Add | Marketplace provider categories beyond OH9 v1.0; profession modes; aggregator restrictions | OH9 | P21 |
| X.10 | Staff roles, timesheets, utilisation | Add | Delivery job roles, SCIM to LDC realm, `TimesheetAggregated` | OH10, OH11, OH12 | P22 |
| X.11 | Cross-company roles | Confirm | RMs serving Finbyx/Udofin/Equator clients; Equator separation | OH1 | P22 |
| X.12 | Interfaces and events (register) | Add | Full list of new/used contracts | Part 6 | All |
| X.13 | Acceptance tests | Add | OH-side tests for the above | — | — |
| X.14 | Open items | — | Decisions and verifications | — | — |

## X.1 Legal entity, workspace and merchant of record

1. **Confirm** an OH1 `legal_entity` for the company that sells LawDocsComply and LawDocs services (`is_group_operator = true`), with GSTIN per State, PAN, Udyam status, invoice series, e-invoice flag (AATO test), revenue framework (AS 9 or Ind AS 115 — OH Appendix B decision 3) and Razorpay account (OH8.7).
2. **Decide** whether one entity sells both the SaaS (LawDocsComply) and the services (marketplace M1), or two entities (e.g., LawDocsComply SaaS company and LawDocs services company). Consequences: separate GSTINs/invoice series; marketplace bundles across entities become two invoices; intra-group cost recharges under OH Part 4.1 (OI-X-01).
3. **Confirm** Workspace N (group-company users) for LDC staff: sales, onboarding, CS, support, marketing, finance within the LDC entity scope; delivery staff use OH for HR/timesheets and LDC `apps/delivery` for client work.
4. **Add** to OH8 `selling_entity`: `products = [LDC]`, `service_lines = [SAAS, MARKETPLACE_FIRST_PARTY, TRAINING_CORPORATE]`; Academy individual courses remain with the Academy merchant unless the owner moves them (OI-P21-07).

## X.2 CRM objects and APIs (OH3)

1. **Add** account fields (custom object fields per OH3.1, JSON Schema): `ldc_entity_family` (template family codes from Appendix E, e.g., `RBI-NBFC`, `SEBI-LISTED`, `COOP-CCS`), `ldc_regulators[]`, `ldc_layer_or_tier` (NBFC layer, UCB tier), `ldc_size_band`, `ldc_package`, `ldc_components[]`, `ldc_tenant_state` (TRIAL, ACTIVE, …), `ldc_trial_end_at`, `ldc_rm_staff_id`, `ldc_retainer_codes[]`.
2. **Add** lead source `LDC_HEALTH_CHECK` with fields: `health_check_id`, `entity_family`, `indicative_band` (A/B/C/D only — **not** answers or scores per question), `consent_marketing` (from the health-check consent screen), `consent_reuse_for_trial`. The health-check answers stay in LDC (`web` module) and are never copied to OH (OH Part 4.5 extended to prospects) [REC].
3. **Add** API `POST /v1/crm/activities` (product → OH3): `org_id`, `tenantid`, `type` (MEETING, CALL, EMAIL_LOGGED, NOTE_COMMERCIAL, QBR), `occurred_at`, `participants` (business contacts), `summary` (≤ 500 chars, commercial only — validated by an LDC-side classifier and a regex block-list for compliance terms such as obligation ids, "overdue", "breach"; an RM must tick "commercial only"), `next_step`, `staff_id`. Idempotency-Key required. Rejects payloads containing PAN/Aadhaar patterns.
4. **Confirm** `POST /v1/crm/requests` (Ecosystem Spec §6.29) for "Talk to sales", enterprise quote requests, and marketplace quote requests from non-subscribers (with consent).
5. **Rule (Add):** LDC compliance insights are never used to target Finbyx/Udofin/Equator offers; OH3.8 cross-group rules apply; an LDC account's CRM record carries `cross_group_authorisation_ref` (null by default) — cross-group campaigns exclude accounts without it.

## X.3 Self-serve provisioning and trials

1. **Add event** `TenantSelfServeCreated` (LDC → OH; CloudEvents type `in.infrabyx.ops.TenantSelfServeCreated.v1` per X-01 — cross-product events use the Ecosystem Spec namespace; source `urn:infrabyx:ldc:<tenantid>`; signed): `tenantid`, `org_id` (from PAN/CIN/LLPIN/GSTIN resolution), `legal_name`, `constitution`, `entity_family`, `regulators[]`, `origin` (HEALTH_CHECK, PRICING, MARKETPLACE, RM_INVITE), `trial_plan`, `trial_end_at`, `first_admin_work_email` (`legalbasis = CONTRACT_PERFORMANCE_VENDOR`), `clickwrap_refs` (ToS, DPA, RE Addendum versions and hashes), `created_at`. Idempotency: `tenantid`. SLA: ≤ 5 min.
2. **OH behaviour (Add):** create or match the CRM account and contact; create an OH4 `onboarding_case` of type `SELF_SERVE` in state `PROVISIONING` with a synthetic provisioning order record (`origin = PRODUCT_SELF_SERVE`, no `TenantProvisioned` emitted); assign an onboarding coordinator per routing rules (segment, region); start the trial nurture sequence only if marketing consent is present.
3. **Decide (deviation from OH8.9):** LDC trials are **production-grade tenants** holding the client's own compliance data under click-wrap ToS + DPA (+ RE Addendum for regulated entities), not sandbox tenants with synthetic data. Rationale: LDC stores the client's own governance/compliance records (no borrower data), and a meaningful trial requires the client's real obligations. Safeguards: India residency, full security baseline, no auto-conversion, deletion after retention window with certificate, RE Addendum before first personal-data upload (P20 FR-P20-24). OH8.9's sandbox rule continues to apply to Finbyx/Udofin (OI-X-02).
4. **Add** trial-extension sync: `POST /v1/trials/extensions` (LDC → OH8) or event `TrialExtended` so OH CS and billing see the current trial end; OH must not send renewal/dunning communications for trial tenants.
5. **Add** conversion: on `TrialConverted` (LDC event) OH4 moves the case to `KICKED_OFF` once the subscription is `ACTIVE`; contract gates for self-serve are satisfied by click-wrap refs; Enterprise and RE clients who require a signed MSA follow the normal `CONTRACT_GATES` path (OH8.4).
6. **RE Addendum clause matrix (content to be drafted by counsel)** — minimum clauses: scope of services and data; data location in India; confidentiality; RE's and RBI's audit, inspection and access rights (incl. direct RBI access); business continuity and exit (no erasure or alteration during transition; full export); sub-processor disclosure and approval; incident notification timelines (to the RE without undue delay, enabling its regulatory reporting); right to terminate; grievance handling responsibility stays with the RE; compliance with the RE's IT and outsourcing directions [VERIFY current RBI outsourcing/IT outsourcing master directions and paragraph numbers].

## X.4 Onboarding factory playbooks (OH4)

1. **Add** methodology template `LDC_STANDARD` (Essentials/Professional) and `LDC_ENTERPRISE`: `DISCOVERY` (entity profile, regulator packs, departments, users) → `DESIGN` (configuration workbook: departments/functions, maker-checker levels, calendar sources, templates) → `BUILD_AND_CONFIGURE` → `MIGRATION` (datasets below) → `UAT` → `TRAINING` → `CUTOVER` → `HYPERCARE` (30 days) → `CLOSED`.
2. **Add** migration dataset types for the data-migration factory: `LDC_QUESTION_BANK` (LDC Excel templates; Appendix E), `LDC_LEGACY_TRACKER` (client Excel trackers mapped to templates), `LDC_POLICY_LIBRARY` (DOCX/PDF with metadata), `LDC_REGISTERS` (statutory registers), `LDC_USERS_ORG` (users, departments, roles, from HRMS/AD export), `LDC_DOCUMENT_FOLDERS` (folder intake, P19), `LDC_RISK_REGISTER`, `LDC_AUDIT_FINDINGS`. Each run reports counts and control totals only (OH4.1 `migration_run`).
3. **Confirm** milestone codes (Ecosystem Spec §6.29): DISCOVERY, CONFIGURATION, MIGRATION, INTEGRATIONS, TRAINING, GO_LIVE; LDC emits `ImplementationMilestoneReached` acceptance from in-product approvals where the client accepts in LDC.
4. **Add** RM assignment step at `KICKED_OFF` for retainer clients (creates the P22 assignment through an LDC API `POST /v1/delivery/assignments` called by OH4 with staff ids; LDC then proposes grants to the client admin).

## X.5 Customer-success signals (OH5, OH2)

1. **Add event** `ClientHealthSignal` (LDC → OH; daily; `in.infrabyx.ops.ClientHealthSignal.v1`, X-01): `tenantid`, `date`, `active_users`, `entitled_seats`, `modules_in_use`, `modules_licensed`, `logins_30d`, `sla_breaches_30d` (delivery SLAs), `open_change_requests`, `retainer_hours_used_pct`, `last_meeting_at`, `renewal_risk_flag` (RM-raised, with reason code from a fixed list: BUDGET, CHAMPION_LEFT, LOW_ADOPTION, SERVICE_ISSUE, PRICE, OTHER). **Excluded by contract:** any compliance metric (on-time %, overdue counts, risk findings), obligation ids, document metadata, credential metadata, message content (OH Part 4.5; LDC contract test `NN-23_no_compliance_content_to_oh`).
2. **Confirm** OH2.3 health score weights; map adoption = active_users ÷ entitled_seats and modules_in_use ÷ modules_licensed; delivery = open change requests and delivery SLA breaches.
3. **Add** QBR data pack for LDC accounts: adoption, SLA, support, commercial; the **Savings & Value** report is attached only if the client allowed `bil.savings.share_with_rm` and uploaded/shared it through the delivery console (the document stays an LDC artefact; OH stores the link and hash only).

## X.6 Support routing (OH6)

1. **Add** LDC ticket categories: `LDC_ACCESS_LOGIN`, `LDC_CONFIGURATION`, `LDC_CONTENT_QUESTION` (regulatory content accuracy — routed to the LDC content team, P03/P05), `LDC_IMPORT_TEMPLATE` (Excel import errors), `LDC_RETURN_STUDIO`, `LDC_INTEGRATION`, `LDC_AI_VIDHI`, `LDC_BILLING_DISPUTE`, `LDC_DATA_EXPORT`, `LDC_SECURITY_REPORT`, `LDC_SERVICE_DELIVERY` (marketplace/retainer service issues).
2. **Confirm** `regulatory_impact` uplift (OH6.3) for LDC tickets where a statutory deadline is at risk (e.g., return due within 3 working days, board meeting notice period running).
3. **Add** routing rule: `LDC_CONTENT_QUESTION` tickets create a content-review task in LDC (`chg` module) via API callback; content corrections follow LDC's maker-checker publishing (NN-03, NN-04), never an OH-side edit.
4. **Confirm** OH6.5 complaint ownership: complaints about LawDocs services (marketplace M1, retainers) are OH `client_complaint`; complaints by a client's customers handled in the client's LDC Grievance Desk (P14) are the client's own and never reach OH.
5. **Add** billing-dispute pause: `LDC_BILLING_DISPUTE` with invoice ref pauses dunning for that invoice (OH8.7) and is mirrored to LDC billing history.

## X.7 Marketing and growth (OH7, OH14)

1. **Add** nurture programmes (consent-gated, OH3.4 send gate): *Health-check follow-up* (D+1 report recap, D+3 "what your score means for your entity type", D+7 webinar invite, D+14 case study), *Trial journey* (Day 1 checklist, Day 3 feature tour by role, Day 5 RM office-hours invite; no countdown or urgency language), *Regulatory change digest* (weekly public summary of Updates — only titles and links to official sources; marketing consent required), *Academy cross-promotion* (course calendars by audience).
2. **Add** content pillars and calendar entries for LDC (social calendar in OH7): regulatory-change explainers (with citation), "how-to" feature videos from P23 tutorials, FAQs, webinars, customer stories (consented), Academy batches. All posts pass the claims gate (OH14.6) — in particular: no "RBI-approved", "100% compliant", "guaranteed penalty-free", certification claims without registry evidence; savings statistics only as P20 FR-P20-69 permits (≥ 20 tenants, method disclosed).
3. **Confirm** OH8.9 funnel restrictions apply to LDC landing pages (no countdowns, anchor prices, unverifiable testimonials); the owner's reference page (ptstdm.co.in) is not a model.
4. **Add** webinar/event registration integration: registrations captured in OH3 with consent; attendance certificates (CPE-style) only if the issuing body permits — no professional CPE claims without the body's recognition [VERIFY ICAI/ICSI CPE rules].

## X.8 Revenue catalogue and billing (OH8)

1. **Add** LDC SKUs to the catalogue from Appendix N §N.2–§N.3 (packages, components `ADD-*`, standalone SKUs, bundles) and marketplace first-party services from Appendix O §O.2 (codes `SVC-*`), each mapped to: LDC module keys (for SKU→module checks, OH8.1 `sku`), stream code, SAC candidate for tax review, refund code, price model.
2. **Add** meters (Appendix N §N.5): `AI_CREDITS`, `STORAGE_GB_MONTH`, `ESIGN_PASS_THROUGH`, `KYC_VERIFICATION_PASS_THROUGH`, `SMS_WHATSAPP_PASS_THROUGH`, `API_CALLS`, `RETURN_RUNS`, `EXTRA_USERS_PEAK`, `EXTRA_ENTITIES` — all `meter_kind = USAGE`.
3. **Add** stream code `MARKETPLACE_COMMISSION` (Basis: percentage of a third-party provider's fee collected through Razorpay Route; Conditions: provider profession cleared by counsel; never advocates/CAs/CSs/CMAs in practice by default; TCS s.52 handling; E-Commerce Rules duties) — default `DRAFT`; and `MARKETPLACE_LISTING` (provider subscription for listing; same profession conditions; distinct from the OH8 deny-list item "advocate listing or referral fees", which stays a hard deny).
4. **Add API** `POST /v1/catalogue/change-requests` (LDC console → OH8): `product = LDC`, `changes[]` (type: PRICE, NEW_SKU, RETIRE_SKU, COUPON, TRIAL_POLICY, STREAM_GATE, TAX_HINT, BUNDLE), `effective_from`, `rationale`, `maker` (LDC `plt_super_admin` id), `presentation_version_ref`, `attachments` (impact analysis). OH8 runs its legality gate and pricing-committee approval; returns `request_id`; status via `GET /v1/catalogue/change-requests/{id}` (`SUBMITTED, IN_REVIEW, RETURNED, APPROVED, PUBLISHED, REJECTED`) and event `CatalogueChangeRequestUpdated`. **Decide** the checker for LDC catalogue change requests. Master D-28 requires that the owner never approves a draft he made: either a second person drafts in the LDC Pricing Studio and the owner approves in OH8, or the owner drafts and a nominated second approver (CFO/Head of LDC) approves (OI-X-03).
5. **Add** event `CatalogueVersionPublished` (OH8 → products) or confirm that `PlanChanged`/daily fetch suffices; LDC needs a push to bind presentation versions promptly (P20 FR-P20-62).
6. **Add** coupon types needed by LDC (P20 FR-P20-63): extended trial, free component for n months, first-term discount, partner code, segment discount with evidence requirement (co-operative, NGO/Section 8, DPIIT startup).
7. **Confirm** quote/order/invoice APIs (Ecosystem Spec §6.27) for LDC and for marketplace M1 orders; add `order_context = MARKETPLACE_ENGAGEMENT` with `engagement_id` so invoices reference engagements.
8. **Add** credit-note requests for retainer SLA credits: event `ServiceCreditIssued` (LDC → OH8) with `engagement_id`, `period`, `metric`, `credit_minor`, `basis_ref`; OH8 issues the credit note (OH8.6) and returns `InvoiceIssued` (credit note).
9. **Add** buyer accounts without tenants: OH8 must invoice an `org_id` that has **no** LDC tenant (marketplace buyers); recipient GST details come from the LDC buyer profile via the order call.
10. **Interim LOCAL adapter (Decide):** if OH8 is not live when LDC P20 ships, LDC may run a local billing adapter on an LDC-owned Razorpay account, migrating to OH8 later (P20 §4L). OH must accept the migration file format (customers, subscriptions, price-book history, historical invoices as documents, mandates) — OI-X-04.

## X.9 Professional directory (OH9) and the marketplace

1. **Confirm** OH9 as the credential source for regulated professionals; LDC consumes `ProfessionalEmpanelled` and `ProfessionalSuspended` and refuses any listing for a suspended professional within 1 hour.
2. **Add** categories needed by the marketplace but not in OH9.1: `CYBERSECURITY_FIRM` (CERT-In empanelment evidence), `CERTIFICATION_BODY` (accreditation; referral only), `SOC_AUDIT_FIRM` (referral only), `CONSULTING_FIRM` (non-attest), `TRAINER`, `POSH_EXTERNAL_MEMBER`. These are not "professions" under OH9's Rule 36 logic; OH9 may host them in a separate partition `mkp_providers` or LDC may verify them in `mkp` directly — **Decide** (OI-X-05).
3. **Confirm** OH9 "free to professionals: no listing, empanelment or allocation fee and no referral fee or share of fees" for regulated professions — consistent with LDC D-06 defaults; LDC's `MARKETPLACE_LISTING` stream applies only to non-regulated providers unless counsel clears otherwise.
4. **Add** ICAI aggregator restriction (ESB announcement, 23 Oct 2019) to OH9.4 public-listing rules: CAs in practice are not shown on any group marketplace page with commerce features; directory display only under Code of Ethics directory conditions, if at all [VERIFY 2026 position].

## X.10 Staff roles, identity, timesheets and utilisation (OH10, OH11, OH12)

1. **Add** job architecture entries for LDC delivery: Relationship Manager (RM), Senior RM, Compliance Analyst, Company Secretarial Executive, Risk Analyst, Audit Associate, Data/Returns Analyst, Delivery Reviewer, Delivery Lead; each mapped to LDC role codes (`dlv_rm`, `dlv_professional`, `dlv_reviewer`, `dlv_lead`).
2. **Add** SCIM provisioning from the group IdP to LDC's Keycloak realm `ldc-staff` (OH12.2/OH12.3): joiner → account with job role; mover → role change event; leaver → `EmployeeOffboarded` triggers LDC leaver sweep within 15 minutes (P22 FR-P22-53). Phishing-resistant MFA required (FIDO2) for LDC delivery users.
3. **Add event** `TimesheetAggregated` (LDC → OH4/OH11; daily): `staff_id`, `date`, `client_org_id`, `tenantid`, `category` (RETAINER, ENGAGEMENT, IMPLEMENTATION, PRESALES, INTERNAL), `engagement_id?`, `hours`, `billable`. No task titles or compliance content. OH11 uses it for utilisation and staff ROI (team-level, OH11.6); OH10 appraisal uses output metrics from LDC (`DeliveryMetricsMonthly`: tasks completed, SLA attainment, first-time-right deliverables, CSAT — per staff, shared with the staff member and manager).
4. **Confirm** NN-25 (no covert monitoring) and OH4.7 staff monitoring rules: no keystroke, screenshot or webcam monitoring; work measured by outputs.
5. **Add** M365 usage for delivery (OH12): SharePoint site per client for working drafts (`LDC-Clients/<client-code>`; retention label per OH12.5), Teams channel per retainer client, mailbox rules unchanged; documents delivered to clients are filed in the client's LDC DMS (P22 FR-P22-30). Office plan: confirm the actual Microsoft 365 SKU (owner said "Business Starter", which is a Google Workspace edition name; OH prompt item 7).

## X.11 Cross-company roles (OH1)

1. **Confirm** one staff identity with separate product roles; LDC delivery grants are tenant-level and approved by the client (not OH `group_grant`); OH `group_grant` covers cross-entity staffing (e.g., an Infrabyx staff member seconded to LDC delivery) with purpose `IMPLEMENTATION_DELIVERY` or `CUSTOMER_SUCCESS` and the 90-day maximum.
2. **Confirm** Equator separation (OH1.6; Ecosystem Spec §8.6): before LDC activates a delivery grant for a staff member, LDC calls `POST /v1/conflicts/check` with the client `org_id`; staff with Equator case-level roles are blocked for lender clients with Equator matters.
3. **Add** visibility rule: an LDC RM who also serves the same client in Finbyx sees the two products separately; no LDC data is shown to the Finbyx-side workspace or vice versa through OH.

## X.12 Interface and event register (LDC ↔ OH)

| Contract | Direction | Status | Notes |
|---|---|---|---|
| `TenantProvisioned` / `PUT /v1/provisioning-requests/{id}` / status poll | OH ↔ LDC | Existing (§6.29) | Sales-led tenants |
| `TenantSelfServeCreated` | LDC → OH | **New** | X.3 |
| `TrialExtended`, `TrialConverted`, `TrialExpired` | LDC → OH | **New** | X.3 |
| `POST /v1/trials/extensions` | LDC → OH8 | **New** | X.3.4 (alternative to the `TrialExtended` event; one of the two is chosen in the change request) |
| `GET /v1/catalogue/versions/{v}` | LDC → OH8 | Existing | Signed catalogue |
| `CatalogueVersionPublished` | OH8 → LDC | **New (or confirm alternative)** | X.8.5 |
| `POST /v1/catalogue/change-requests`, `GET …/{id}`, `CatalogueChangeRequestUpdated` | LDC ↔ OH8 | **New** | X.8.4 |
| `POST /v1/billing/quotes`, `POST /v1/billing/orders`, `GET /v1/billing/invoices`, `POST /v1/usage-disputes`, `GET /v1/entitlements` | LDC ↔ OH8 | Existing | + `order_context` (X.8.7) |
| `PlanChanged`, `EntitlementChanged`, `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`, `SubscriptionCancelled` | OH8 → LDC | Existing | — |
| `UsageRecorded`, `ModuleAttached`, `ModuleDetached`, `ReconciliationBreakRaised` | LDC → OH8 | Existing | — |
| `ServiceCreditIssued` | LDC → OH8 | **New** | X.8.8 |
| `POST /v1/support/tickets`, `SupportTicketOpened`, `SupportTicketResolved` | LDC ↔ OH6 | Existing | X.6 categories |
| `POST /v1/crm/requests` | LDC → OH3 | Existing | — |
| `POST /v1/crm/activities` | LDC → OH3 | **New** | X.2.3 |
| `ClientHealthSignal` | LDC → OH5 | **New** | X.5 |
| `TimesheetAggregated`, `DeliveryMetricsMonthly` | LDC → OH4/OH11/OH10 | **New** | X.10 |
| `POST /v1/delivery/assignments` | OH4 → LDC | **New** | X.4.4 |
| `ImplementationMilestoneReached` | OH4 ↔ LDC | Existing | — |
| `ProfessionalEmpanelled`, `ProfessionalSuspended` | OH9 → LDC | Existing | — |
| `POST /v1/conflicts/check` | LDC → OH1.6 | Existing (EQ only) — **extend** to LDC | X.11.2 |
| `GET /v1/claims-gate/check` | LDC → OH14 | Existing | Pricing copy, offerings, savings stats |
| `ReleasePublished`, `ChangeApproved`, `ControlEvidenceCollected`, `BackupCompleted`, `RestoreTested` | LDC ↔ OH13/OH14 | Existing | P24 |
| SCIM 2.0 users/groups | Group IdP → LDC `ldc-staff` | **New for LDC** | X.10.2 |
| `EmployeeOffboarded` (oh scope) | OH10 → LDC | **New consumer** | X.10.2 |

Event types for every contract in this register use the Ecosystem Spec pattern `in.infrabyx.<domain>.<EventName>.v<major>` (domain `ops` for X.2–X.5 and X.10, `billing` for X.8 — final domains fixed in the Spec v1.2 change request; master §19 item 7). All new contracts follow Ecosystem Spec §3 (CloudEvents 1.0, JWS signatures for financial and entitlement events, Idempotency-Key, outbox/inbox, India residency, no personal data beyond business contacts with a recorded legal basis).

**Contracts added in v1.1** *(v1.1)*

| Contract | Direction | Status | Notes |
|---|---|---|---|
| `PartnerOnboarded`, `PartnerSuspended`, `PartnerScorecardPublished` | OH (PRM) ↔ LDC `mkp`/`prt` | **New** | X.15.1 |
| `POST /v1/conflicts/check` with `jurisdiction`, `opposing_party` | LDC → OH1.6 | **Extend** | Foreign delivery partners |
| `PracticeLinkCreated`, `PracticeLinkRevoked` | LDC → OH3 | **New** | Firm ↔ client links (aggregates; no compliance content) |
| `CostToServeRecorded` | LDC → OH8/finance | **New** | P20 FR-P20-96 |
| `AgentSeatChanged`, `AiCreditsConsumed` (daily aggregate) | LDC → OH8 | **New** | Agent seats and credits (P20 §4R) |
| `ProductSuggestionLogged` | LDC → OH5 | **New** | Feedback loop (P22 FR-P22-76) |
| `SupportChatHandedOff` | LDC → OH6 | **New** | With consented context bundle |

## X.13 Acceptance tests (OH side)

1. A `TenantSelfServeCreated` with an `org_id` already matched to an account creates no duplicate account and opens one `SELF_SERVE` onboarding case.
2. An LDC catalogue change request with a price change is not published until the OH8 pricing committee approves; the requester cannot approve their own request.
3. A `POST /v1/crm/activities` payload containing "overdue" plus an obligation id pattern is rejected with a reason.
4. A `ClientHealthSignal` containing an unknown field (e.g., `on_time_pct`) is rejected by schema.
5. A `ServiceCreditIssued` for a retainer produces exactly one credit note referencing the original invoice.
6. An `EmployeeOffboarded` for an LDC RM is delivered to LDC within 5 minutes; LDC acknowledges the leaver sweep.
7. A marketplace M1 order for a buyer `org_id` without an LDC tenant produces a GST invoice with the buyer's GSTIN and place of supply.
8. An advocate profile can never be returned by any OH API with a price, rating or listing fee attribute, including through the new `mkp_providers` partition.
9. A stream `MARKETPLACE_COMMISSION` cannot move beyond `LEGAL_REVIEW` without counsel and tax review references.
10. A trial tenant receives no renewal or dunning communication from OH.

## X.15 Additions for v1.1 *(v1.1)*

### X.15.1 Partner relationship management (OH3/OH9)

OH gains PRM objects for the foreign partner network (Appendix Y §Y.5; P21 §4N): `partner_firm` (jurisdictions, professions, partner types, tier, PI cover, licences with expiry), `partner_agreement` (framework, DPA, SLA, commercial model per country with counsel reference), `partner_scorecard` (quarterly metrics), `partner_pipeline` (prospective firms by corridor, Appendix Y §Y.12). OH9's professional directory remains the group shared service; LDC `mkp`/`prt` hold the product-side profiles and portal access.

### X.15.2 Global CRM fields (OH3)

Accounts and opportunities gain `country`, `home_cell`, `contract_currency`, `selling_entity`, `tax_id_type`, `jurisdictions_of_interest`, `group_structure_size` (number of entities by country). Lead routing by corridor (India, GCC, Singapore, UK/EU, US). Health-check leads carry the jurisdiction variant (P23 §4R).

### X.15.3 Practitioner firms as customers (OH3/OH8)

Firm accounts are a distinct account type with client links (counts only), practitioner-plan subscriptions and firm-paid vs client-paid billing per link (P20 FR-P20-79). Firms are never shown in OH marketing audiences as "LawDocs partners" unless a partner agreement exists.

### X.15.4 Catalogue and streams (OH8)

Add components ADD-LIT, ADD-LIT-S, ADD-ESG, ADD-ESG-S, ADD-AIG, ADD-GEM, ADD-GLB-<cc>, ADD-QRY, ADD-RPT-PRO, ADD-CELL-<cell>, ADD-ESC-D, ADD-ESC-S, ADD-AGT-<agent>, practitioner plans, and price books in INR, USD, AED, SGD, EUR, GBP; streams RS-LDC-31–RS-LDC-42 (Appendix N §N.15–§N.19). OH8 must support multiple selling entities and cross-border tax treatments (Appendix Y §Y.10) before RS-LDC-41 is switched on.

### X.15.5 Customer community and feedback loop (OH5, OH7; G5 TM-455/460)

A moderated customer community (Q&A, templates shared by customers with permission, product announcements) run by OH7 with LDC SSO; product suggestions from clients and RMs (`ProductSuggestionLogged`) land in an OH5 feedback board with votes, status and links to LDC backlog items; quarterly "you asked, we built" release notes (claims-gated, NN-19).

### X.15.6 Baseline GTM material to port (OH7/OH8; G5)

The owner's Architecture Part 2 §11 material — per-regulator ideal customer profiles and buyer personas, positioning one-liners and proof points, advisory SKU rate cards, time-and-material rate card, platform + advisory bundles, partner programme tiers and channel map, 90-day launch plan, year-1 to year-3 financial targets and GTM risks — belongs in OH7 (marketing) and OH8 (catalogue) workspaces. OH ports it and links each item to the LDC catalogue codes; LDC keeps only product-facing copy (Appendix P).

### X.15.7 Agent workforce metrics (OH5/OH11)

LDC sends daily aggregates of agent usage (agents active, missions run, outputs accepted, credits consumed) per tenant for CS health and capacity planning; never task content (D-03).

## X.14 Open items

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-X-01 | One or two selling entities for SaaS vs services | Company Secretary | Single entity with two invoice series |
| OI-X-02 | Production-grade trials for LDC (deviation from OH8.9) | Owner + OH product head | Sandbox trial with synthetic sample tenant |
| OI-X-03 | Second pricing approver so the owner never approves his own draft (D-28) | Owner | Second approver (CFO/Head of LDC) |
| OI-X-04 | LOCAL billing adapter and migration to OH8 | CTO | Delay P20 exit until OH8 sandbox available |
| OI-X-05 | Where non-profession providers (cyber firms, CBs, trainers) are verified (OH9 partition vs LDC `mkp`) | Head of legal | LDC `mkp` verification |
| OI-X-06 | ICAI/ICSI CPE recognition for webinars | Owner | No CPE claims |
| OI-X-07 | Microsoft 365 SKU actually held (Business Basic/Standard/Premium) | Company Secretary | Design for Business Standard features without Intune |


**v1.1 changes (25 October 2026)** *(v1.1)*

- New §X.15 additions for v1.1: partner network management in OH (PRM objects), global CRM fields (country, cell, currency, selling entity), practitioner-firm accounts, new catalogue items and streams (Appendix N §N.16–§N.19), customer community and feedback-to-backlog loop (G5 TM-455/460), baseline GTM material to port into OH7/OH8, agent-workforce metrics, and new contracts for the interface register.

---

**Master integration note (pack lead, 25 October 2026).** This appendix is read with master §4 and §18, in particular D-03, X-02, X-15, D-26–D-28; master §19 lists the change requests this addendum requires. Where text above conflicts with them, the master prevails.

## X.16 Additions for v1.3 — Operations Hub v1.1 alignment under the IPB *(v1.3; D-67, D-70, D-75)*

| Area | What LDC now expects from the Operations Hub v1.1 | OH module | Contract |
|---|---|---|---|
| Vendor Assurance Room | OH14.6 is the system of record for every IPB-08 document type; LDC mirrors through `TRUST_PORT` and the event `in.infrabyx.trust.VendorAssuranceDocumentPublished.v1`; per-tenant releases (`vapt_report`, `financial_statements`, `affidavit_undertaking`, `incident_notice_tenant`, `questionnaire_response`, `vendor_file`) are authorised in OH and delivered in LDC; the acknowledgement log is reported back to OH monthly | OH14.6 | IPB-08 §08.4.6; P24 FR-P24-51 |
| Staff scope | OH10 provisions `ldc-staff` identities with `product_scope = LDC` in addition to legal entity; cross-scope access only by purpose-bound, time-boxed group grant (IPB-D-12) | OH1, OH10 | IPB-02-11 |
| CRM and HR intake | Public forms (contact, partners, careers, resource gates, health-check hand-off) post through `CRM_PORT` / `HR_PORT` with consent text version and ledger receipt id; `in.infrabyx.crm.LeadCaptured.v1` replaces the v1.0 ad-hoc payload | OH3, OH10 | IPB-04-67; P23 FR-P23-217–218 |
| Feedback and beta | `in.infrabyx.feedback.FeedbackSubmitted.v1` feeds the OH product backlog and support; beta-ring tenants and their feedback are visible to account managers | OH5, OH6 | IPB-09-46; P24 FR-P24-56 |
| Release communication | `in.infrabyx.eng.ReleaseNotePublished.v1` → group changelog, account-manager digests, status page | OH5, OH7 | IPB-09-42 |
| Policies | `in.infrabyx.grc.PolicyEffective.v1` and `PolicyReviewDue` → OH compliance calendar; OH holds the master instances of Templates 3, 4 (selling entities), 15 (intra-group) and 17 (registry) | OH8, OH14 | IPB-05 §05.7 |
| Marketing consent | `in.infrabyx.consent.MarketingConsentUpdated.v1` within 60 s both ways; OH marketing never contacts a lead without a current LDC-captured consent | OH7 | IPB-02-26 |
| WhatsApp templates | One WABA per brand; template registry in OH; `in.infrabyx.messaging.WhatsAppTemplateApproved.v1` | OH16 | IPB-10 §10.6.2 |
| White-label | `in.infrabyx.tenancy.WhiteLabelTenantProvisioned.v1` triggers host verification, certificates and billing set-up for the LDC white-label add-on | OH8, OH3 | IPB-D-10 |
| Billing | Unchanged (X-02): OH8 catalogue, prices, GST, invoices; LDC Pricing Studio shows the catalogue read-only | OH8 | Appendix N |

Open item: OI-X-08 *(v1.3)* — OH14.6 to confirm the IPB-08 catalogue seed and cadences for LDC's document set before P24 Wave-1 exit (owner: OH lead; fallback: LDC publishes a product-local list labelled "pending OH confirmation").
