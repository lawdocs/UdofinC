# LAWDOCSCOMPLY — REQUIREMENTS MAP AND DECISION LOG (v1.1, 25 October 2026; supersedes v1.0)

> Paste after `01_MASTER_PROMPT.md` at the start of every phase session. This file records what management asked for (R-IDs), what was decided (D-IDs), where the brief was challenged and why, what is still open, and where each requirement is built.

---

## 1. Purpose and sources

The management brief of 25 October 2026 (the "brief") asked for a build prompt for LawDocsComply as a complete GRC SaaS within the Infrabyx ecosystem, in two parts: Part 1, the tool; Part 2, Excel question sheets produced separately and uploaded into the tool. This log converts the brief into 102 numbered requirements (§8), records the owner's answers to the eight planning questions asked the same day (D-01–D-08), the defaults adopted for unanswered points (D-09–D-21), the decisions this pack adds after research (D-22–D-33), and the challenges to the brief (§3).

---

## 2. Decisions

### 2.1 Decisions taken by the owner on 25 October 2026 (planning questions)

| ID | Question | Owner's choice | Notes and later amendments |
|---|---|---|---|
| D-01 | Technology base | Ecosystem stack: Next.js 16 + NestJS 11 modular monolith + PostgreSQL with RLS, India region; migrate the live MongoDB app by script | Amended by **X-05**: production on AWS RDS/Aurora ap-south-1 with ap-south-2 DR and S3 Object Lock; Supabase PostgreSQL for non-production/beta only (no Hyderabad region, no Object Lock); Railway decommissioned |
| D-02 | Super-admin edits to audit trail, dates and proof | Correction entries: overrides allowed only as reason-coded, dual-approved Correction Entries; originals sealed, tenant-visible | Implemented in P00 (`core.correction_entries`), P02 §4O, Appendix A §A.5; NN-02 |
| D-03 | Operations platform | Group Operations Hub for CRM, marketing, staff HRMS/payroll/appraisal, controls, billing; LDC Service Delivery Console for RMs | Appendix X (OH addendum); P22 |
| D-04 | Client portal credentials | Encrypted vault in the client tenant, client-owned, per-credential grants, MFA reveal, logs, RBI portals client-only by default | NN-17; P22 |
| D-05 | Return engine location | Shared returns kernel; LDC Return Studio for non-Finbyx clients; consume Finbyx return runs for Finbyx clients | Named `@infrabyx/returns-kernel` + `infrabyx-returns-packs`; extended to accounting-framework resolver and Schedule III maps; NN-39 |
| D-06 | Marketplace monetisation | Per-profession switches; listing/subscription fees; disclosed platform fee for LawDocs-run services; % commission OFF by default for advocates, CAs, CSs, CMAs | NN-20; Appendix O |
| D-07 | Pack format | Both: Equator-style pack and Finbyx-style Master Prompt + Phase Runbook (md + docx) | This pack |
| D-08 | Excel template strictness | Same 30 columns (A–AD), rows 1–2 unchanged, `Rough` lists with named ranges, family-specific dropdowns, protected `_Template_Info` sheet | NN-35; Appendix E; 24 templates in v1.0, 27 in v1.1 (X-51) |

### 2.2 Defaults adopted for points the owner did not decide (reversible)

| ID | Default |
|---|---|
| D-09 | References in the brief to "Udofin" (role statement), "Equator CRM", "dispute resolution platform", "petition/claim" and "neutrals" are carried over from earlier briefs and read as LawDocsComply equivalents (evidence, grievances, regulator correspondence, clients). |
| D-10 | "Microsoft 365 Business Starter" is not a Microsoft plan (Business Starter is a Google Workspace edition). LDC is suite-neutral (`WORKSPACE_PORT`), Microsoft 365 first (Business Basic/Standard/Premium), Google Workspace later; features that depend on the plan (Teams transcripts, `Sites.Selected`, retention labels, Intune device checks for vault reveals) are gated by a capability matrix. **Owner to confirm the plan held.** |
| D-11 | Client payroll computes, approves and produces bank bulk-payment files or payout-partner instructions; LDC never holds salary money. |
| D-12 | Regulator/supervisor read-only view as a tenant-initiated, time-boxed grant (NN-18). |
| D-13 | Portal filings prepared and validated in LDC, submitted by a human (NN-08). Extended to DPB, CERT-In, DAKSH incident module, IFSCA cyber mailbox, SEBI incident reporting, EPFO/ESIC/State labour portals, SCORES and Bima Bharosa. |
| D-14 | AI via provider adapter; Claude primary; Jio and others as adapters; no training on tenant data. **Amended by X-03:** Claude via Amazon Bedrock India geographic cross-Region inference for regulated data; Anthropic API (global) for non-personal content only. |
| D-15 | Health check is an indicative self-assessment. |
| D-16 | Co-operative credit operations in Finbyx; LDC runs governance, membership, elections support, meetings, complaints, registers, returns and GRC. Extended by D-23. |
| D-17 | AI output never auto-publishes. |
| D-18 | Regulatory scan at 20:00 IST daily plus intraday feeds; regulatory digest 20:30 IST. |
| D-19 | Jurisdiction-pack framework; India first; international packs only with a sourced pack and a named in-country reviewer. |
| D-20 | eSign through licensed providers and DSC. **Amended by X-04** (ESP vs ASP terminology). |
| D-21 | Pricing data-driven and editable in super admin. **Amended by X-02** (OH8 is the billing system of record). |

### 2.3 Decisions added by this pack (25 October 2026)

| ID | Decision | Why |
|---|---|---|
| D-22 | Shared `infrabyx-risk-kernel` (metric formulas, capital rule packs, ALM maths, PCA thresholds, stress primitives) in `infrabyx-contracts`, version-pinned per run | Prevents Finbyx and LDC computing the same ratio differently; mirrors D-05 |
| D-23 | `coop.sor.members` ∈ {FINBYX, LDC, EXTERNAL_LOS}; for non-credit societies LDC is the member/share register and emits the Ecosystem §6.24 contracts | Non-credit co-operatives have no Finbyx book but need registers |
| D-24 | Billing ownership per X-02 (OH8 system of record; LDC presentation, entitlements, meters, trials, savings, UI; Pricing Studio change requests) | Ecosystem Spec §6.27 and OH v1.0 already make OH8 the single revenue ledger |
| D-25 | No credit-bureau pulls by LDC for onboarding, profiling or the health check (X-07) | LDC is not a specified user under CICRA 2005 for this purpose [INTERP; counsel to confirm] |
| D-26 | **Proposed:** trials are real production tenants under click-wrap terms + DPA (+ RE addendum), deleted 30 days after expiry unless converted or exported | The owner wants users to "experience the tool"; a sandbox cannot hold their own data. Needs owner and OH acceptance (OH8.9 assumes sandbox trials) |
| D-27 | **Open:** one or two selling entities (SaaS vs services) and merchant of record for marketplace services | Tax, invoicing and liability depend on it |
| D-28 | **Open:** nominate a second pricing approver so the owner never approves his own Pricing Studio draft | Maker ≠ checker (NN-05) |
| D-29 | LDC does not register as a DPDP Consent Manager (Rule 4 requires an Indian company with ≥ ₹2 crore net worth acting solely for Data Principals, which conflicts with serving REs); integration readiness only | Conflict of role |
| D-30 | Hindi is the second locale for the health check, glossary, solution pages and help [REC] | Co-operative and small-NBFC market reach |
| D-31 | AI-crawler policy default `ALLOW_PUBLIC_MARKETING` [REC; owner may change] | GEO visibility without exposing product content |
| D-32 | LawDocs (a company) does not supply reserved advocacy or attest services (legal representation/advice as advocates; statutory, secretarial, tax or IS audit; certifications) in its own name; eligible practitioners contract directly; CA listing OFF by default (ICAI announcement of 23 Oct 2019 on aggregators) [INTERP; counsel to confirm] | Advocates Act/BCI Rules and professional-body codes |
| D-33 | No bulk approval of maker-checker items with legal effect, money or access (NN-46), replacing the owner baseline's "bulk approve" | A bulk click is not a review; regulators test maker-checker evidence |


### 2.4 Decisions added in v1.1 (25 October 2026)

| ID | Decision | Why |
|---|---|---|
| D-34 | Vidhi agent workforce of role agents; every agent at autonomy L2 or above has a named human sponsor | Future-ready AI with accountability (Appendix AA) |
| D-35 | LDC MCP server first (read and draft tools under user permissions), MCP client second; A2A after Ecosystem Spec v1.2 approval | Lets clients' own AI assistants use LDC safely; protocol-native |
| D-36 | AI governance overlay `OV_AI` built in P12 with template family AI-GOV | Regulated clients now face AI governance expectations (RBI FREE-AI, MeitY, EU AI Act, ISO 42001) |
| D-37 | Sovereign/on-prem AI route (open models) as an adapter, OFF by default | Future data-sovereignty demands |
| D-38 | LDC applies `OV_AI` to itself and publishes a vendor AI assurance pack | Trust and procurement readiness |
| D-39 | The RBI content base is the 28 Nov 2025 consolidated directions (238 press-release count / 244 serials, 240 live) with later amendments, plus the DoS set of 31 Jul 2026, the CEPD Internal Ombudsman directions and RB-IOS 2026; the 320-row catalogue is pre-seeded with placeholder items until sheets are uploaded | Owner's instruction: only these directions are uploaded |
| D-40 | One question sheet per direction per entity category, with sibling links and category-specific applicability for shared checkpoints | Common directions across RE categories |
| D-41 | LDC owns legal matters, litigation, regulator inspections and observations, contracts, licences and ethics registers (P26); Finbyx Recovery Suite/Udolex owns lender debt recovery | Baseline litigation module was missing |
| D-42 | Regional cells: India live; EU, GCC/UAE, Singapore, US on demand; home region chosen at onboarding; linked tenants for cross-cell entities | Global expansion with residency |
| D-43 | Global rollout stages G0–G5 (Appendix Y) | Sequenced, evidence-led expansion |
| D-44 | Partner network for foreign content and delivery; fee, referral and revenue-share models switched on per country only after local counsel | Lawrbit-style coverage without professional-rule breaches |
| D-45 | Pack lifecycle DRAFT → PILOT → PUBLISHED → DEPRECATED | Safe introduction of new jurisdictions |
| D-46 | Saudi personal data deferred; China limited to non-personal entity calendars | Data-transfer and localisation risk |
| D-47 | New phases P26, P27, P28; P28 owns `rpt`; P06 related-party naming `gov.rpt_txn_*` | Missing modules from the baseline audit (Appendix AC) |
| D-48 | New module codes `gem`, `prt`, `lit`, `esg`, `aig` and the new roles listed in master §1.4 | Ownership clarity |

---

## 3. Challenges to the brief (R-001)

### 3.1 Where the brief was changed, narrowed or corrected

| # | Brief asked | What the pack does instead | Reason |
|---|---|---|---|
| C-01 | Super admin can edit the audit trail, change dates and replace a client's proof | Correction Entries (D-02) | Editable trails lose evidentiary value (BSA 2023 s.63; Companies (Accounts) Rules r.3(1) edit log; SOC 2 CC7/ISO 27001 A.8.15); RBI inspections test audit trails |
| C-02 | Shared password tracker page for MCA, GST, CERSAI, CIC and RBI portals | Client-owned encrypted vault, per-credential grants, logged reveals; RBI portals client-only by default (D-04) | RBI portal IDs belong to named RE officers; shared passwords fail access-control tests and create liability |
| C-03 | CIBIL API for user registration | No bureau pulls; P11 prepares the client's own CIC submissions (D-25) | CICRA 2005 purpose limits |
| C-04 | Percentage share for CAs, CSs, lawyers on the marketplace | Per-profession switches, % OFF for regulated professions (D-06, D-32) | BCI Rules (fee-sharing, r.36), ICAI/ICSI codes |
| C-05 | Supervisory-returns directions "issued on 28 Nov 2025" | Cite the DoS directions of 31 Jul 2026 (X-12) | Factual correction |
| C-06 | Automated filing on CIMS, DAKSH, PRAVAAH | Prepare, validate, export, capture acknowledgement; human submits (NN-08) | No authorised filing API |
| C-07 | Separate LDC operations platform with its own CRM, marketing, HRMS | Group Operations Hub + LDC delivery console (D-03) | The Hub is already specified for all group companies; duplication splits CRM and revenue |
| C-08 | Board bulk approvals (owner baseline) | Sequential "Review next" (NN-46) | Evidence of review |
| C-09 | Embedded Office editing | Graph co-authoring in the tenant's SharePoint/OneDrive; optional self-hosted editor (X-06) | WOPI requires Microsoft partner programme |
| C-10 | Jio "agentic AI, research and drafting" | Jio as channel and voice adapters (JioCX, SIP, Haptik); LLM adapter OFF until an enterprise API with India residency and no-training terms exists | No public Jio LLM API found (25 Oct 2026) |
| C-11 | Tax functionality for borrowers at Udofin from LDC | Borrower certificates remain the RE's through Finbyx/Udofin; LDC prepares GST/TDS for tenant entities (X-31) | RE is the issuer |
| C-12 | Employee monitoring to "make sure the employee cannot cheat" | Transparent, notified measurement; maker-checker, SoD and approval controls; no covert surveillance (NN-25; OH10–OH11) | DPDP s.7(i) legitimate use is narrow; controls reduce fraud, they do not eliminate it |
| C-13 | Full regulator returns for every regulator in v1 | NBFC, ARC, co-operative first; others `ACTIVE_UNVERIFIED` until a pilot verifies cell maps (X-32) | Unverified cell maps produce wrong returns |
| C-14 | LDC to "integrate" Consent Manager functions | Readiness only (D-29) | Role conflict |
| C-15 | LDC to run co-operative elections | Support and records; authority conducts (X-34) | Statutory elections are conducted by the election authority |

### 3.2 Corrections to the owner's baseline documents

MBP-1 is a disclosure form, not a register; the register of contracts in which directors are interested is MBP-4 (X-37). DPT-3 is a return; the register of deposits is under Acceptance of Deposits Rules r.14. The baseline's "31-column schema" is 30 columns (A–AD) plus system fields. Gold #C9A961 and amber #D97706 fail WCAG text contrast (X-20). "ISO 27001 certified" must not appear until certified (X-22). The live site's SEO/GEO markup is invisible to crawlers because the site is client-rendered (X-21).

### 3.3 Consolidation of new non-negotiable rules proposed by the streams

| Final NN | Proposals merged (stream) |
|---|---|
| NN-33 Statutory clocks computed, earliest start, never pause | S1 (due dates never edited), S6 (earliest legally relevant start), S12 (clocks never pause) |
| NN-34 Reviewed release only; code never changes content | S1 (unreviewed intelligence labelled), S11 (releases never modify content) |
| NN-35 Template contract | S2 (rows 1–2/columns A–AD immutable; base vocabulary never renamed) |
| NN-36 Sealed governance records | S3 |
| NN-37 Deterministic documents and numbers | S3 (AI never writes OOXML), S5 (no AI figures) |
| NN-38 Regulatory floors and supervisory status | S4 (floors; never PCA), S7 (VERIFY advisory only; no auto-classification needing RBI advice) |
| NN-39 One owner per computed output | S5 (never recompute Finbyx returns), S4 (Finbyx-certified metrics) |
| NN-40 Internal Ombudsman independence | S6 |
| NN-41 AI data-class routing; no standing AI permissions | S8 |
| NN-42 Never-block list | S8, S9 |
| NN-43 Delivery staff never check | S9 |
| NN-44 Honest public surface (SSR; no dark patterns) | S10 |
| NN-45 Audit in same transaction; export taxonomy contract | S11 |
| NN-46 No bulk approval with legal effect | S12 |
| (folded into NN-20) Professional-conduct render allow-lists | S9 |


### 3.4 Non-negotiable rules added in v1.1

| Final NN | Source |
|---|---|
| NN-24 amended (home-region residency, linked tenants) | G1 global stream |
| NN-47 AI never decides a conclusion | G2 feedback stream |
| NN-48 Three dates per instance; timeliness on act date | G2 |
| NN-49 Undo for imports and bulk changes | G2 |
| NN-50 Bounded autonomy | G3 AI stream |
| NN-51 AI kill switches | G3 |
| NN-52 Protocol edge, contract core | G3 |
| NN-53 Jurisdiction-pack gate | G1 |
| NN-54 Official language preserved | G1 |
| NN-55 No stale citations | G4 RBI catalogue stream |

### 3.5 Further corrections found in v1.1

- RBI direction counts reconciled (238 press release / 244 serials / 240 live) and the NBFC set is 35 consolidated directions, not 30 (X-52).
- NBFC Internal Ombudsman Directions: /383 or /384 [VERIFY]; v1.0 stated /384 as fact.
- IFSCA entity types are 40, not 33 (X-56).
- Ind AS 37 fixed probability bands and the BRSR "75% value-chain boundary" in the owner baseline are corrected (X-57).
- `rpt` was used by ten phases but owned by none; P28 now owns it, and P06's related-party use of `rpt` is renamed (X-43, X-44).
- P18 routed litigation events to a register no phase built; P26 now owns `lit.matters`.
- Stale RBI citations superseded by the 28 Nov 2025 directions (the 2023 SBR Master Direction, the 2022 UCB circular, the 2023 IT governance direction) are re-cited to the consolidated or DoS directions with [VERIFY] numbers.
- Three different "scores" are now four named measures (X-46).
- AuditBoard is now Optro (March 2026).

---

## 4. Owner decisions pending (needed before the phase named)

| # | Decision | Owner | Blocks |
|---|---|---|---|
| 1 | Confirm Microsoft 365 plan (D-10) and whether any group company uses Google Workspace | Company Secretary | P18 workspace connectors, P22 vault device checks |
| 2 | Trials as real tenants (D-26) — accept, and obtain OH acceptance | Owner + OH lead | P20 trial lifecycle |
| 3 | Selling entity(ies) and merchant of record (D-27) | Board / CFO | P20, P21 invoices |
| 4 | Second pricing approver (D-28) | Owner | Pricing Studio go-live |
| 5 | Package names, base prices, add-on prices, trial length, discounts (Appendix N seeds marked [OWNER TO SET]) | Owner / CFO | P20, P23 pricing page |
| 6 | Product names: Vidhi vs Nidhi AI; FinLegal Academy vs LawDocs Trainings; package names vs live Basic/Pro/Custom (X-18) | Owner | P17, P21, P23 |
| 7 | `_LDC_System` export sheet (X-28) | Owner | P03 exports |
| 8 | Revenue-stream registry waves and kill-switch approvers; advertising/sponsored listings ON or OFF | Board | P20, P21 |
| 9 | Hindi second locale and further languages (D-30); AI-crawler policy (D-31) | Owner | P23 |
| 10 | Entity particulars of the LDC operating company (CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer) for invoices, notices and the trust centre | Company Secretary | P20, P23, P24 |
| 11 | Policy set for certification readiness (information security, access control, incident response, vendor risk, retention, privacy, cookie, AI use, BCP) | Company Secretary / CISO | P24 |
| 12 | Vendor contracts (candidates only): AWS, Bedrock, Keycloak hosting, Temporal, OpenSearch, Razorpay via OH8, eSign ASPs, company-data provider, DigiLocker partner, PAN/GSTIN provider, SMS/WhatsApp/JioCX, translation/speech, CERT-In empanelled VAPT auditor | CTO / Procurement | P01, P07, P17, P18, P24 |
| 13 | Content team and reviewer roster (CS, CA, advocate) for packs and Part-2 sheets; in-country reviewers before any international pack | Owner | P03, P05, P15 |
| 14 | Retire the live site's certification claim and old Railway hosting after migration | Owner / CTO | P00, P23 |
| 15 | *(v1.1)* Approve the RBI content base and catalogue (D-39) and the Part-2 wave plan (Appendix AB); confirm reference numbers as sheets are written | Owner / content team | P03 catalogue pre-seed, Part 2 |
| 16 | *(v1.1)* Default AI autonomy ceilings per plan and the human sponsors for agents at L2+ | Owner / CTO | P17 |
| 17 | *(v1.1)* First regional cell and corridor after India (recommended UAE then Singapore), and the first content partners | Owner | P25 |
| 18 | *(v1.1)* ESG-BRSR as a separate Part-2 family (built) or merged into SEBI-LISTED/MCA-CO | Owner | P27, Part 2 |
| 19 | *(v1.1)* Delete or keep archived v1.0 files in `_Archive (older versions)` (deletion needs your approval on the computer) | Owner | — |

---

## 5. Questions for counsel

1. CICRA 2005: may LDC obtain any credit-information report for its own customer onboarding? (Pack assumes no.)
2. Advocates Act 1961, BCI Rules Part VI (r.36, fee-sharing), ICAI, ICSI and ICMAI codes: permitted marketplace models, listing formats, platform fees and whether LawDocs may invoice for practitioners' services.
3. LODR Reg 24A: may an Infrabyx-linked practising CS act as secretarial auditor of a listed client that uses LDC or LawDocs retainers?
4. RBI outsourcing directions (banks, NBFCs, UCBs, RCBs): which "virtual CCO / internal audit / compliance" services may be supplied to REs and in what form?
5. DPDP Act: LDC's role as processor for tenants and fiduciary for its own users; s.16 cross-border position for Bedrock routing; employee-monitoring notice text (s.7(i)).
6. Trials as production tenants (D-26): click-wrap enforceability for regulated entities and the minimum RE addendum.
7. Savings dashboard: wording of penalty-avoidance estimates so they are not misleading (Consumer Protection Act 2019; dark-patterns guidelines).
8. eSign: documents in the IT Act First Schedule that the policy and agreement workflows must route to wet signature or registration.
9. Co-operative societies: State-by-State limits on electronic meetings, e-voting and digital registers for the first ten States.
10. Health check lookups: provider terms that allow anonymous company look-ups for lead generation.
11. *(v1.1)* For each corridor country: whether partner referral fees, revenue share or platform fees with local lawyers and accountants are permitted; local data-transfer mechanism; whether the product's compliance content is "legal advice" there.
12. *(v1.1)* Wording of AI-governance and "AI assurance pack" claims so they are not read as certification.

---

## 6. Assumptions

- The live LawDocsComply repository (TypeScript/React/Node/MongoDB/Prisma on Railway, 21 modules, RBI and Companies Act question banks, beta with Branch International) is available to the coding agent in P00 with read access to production data for migration.
- Finbyx, Udofin and the Operations Hub are built to their current prompts; where they are not yet live, LDC ships the stated fallbacks (interim billing adapter, CSV/SFTP intake, local computation for non-Finbyx tenants).
- The owner's content team produces Part-2 sheets for the first four families (RBI-NBFC, MCA-CO, DATA-PRIV, IFSCA-GEN) before Wave 1 GA.
- All prices and plan names are placeholders until the owner sets them.

---

## 7. External dependencies

AWS India regions and Bedrock India route; Keycloak; Temporal; OpenSearch; Microsoft Graph permissions and tenant admin consent from each client; licensed company-data and PAN/GSTIN providers; DigiLocker partner; eSign ASPs; SMS DLT registration; WhatsApp Business account; Razorpay via OH8; CERT-In empanelled auditor; translation and speech providers for Indian languages; FinLegal Academy LMS API; Ecosystem Spec v1.2 change requests (master §19).

---

## 8. Requirements coverage map

Coverage below was compiled from each stream's requirement map (`_contrib/S*_req_map.md`); the phase file sections named there hold the detail.

| R-ID | Requirement (management brief, 25 Oct 2026) | Covered in | Note |
|---|---|---|---|
| R-001 | Working agreement (challenge assumptions) | Master §0, P00, P24 |  |
| R-002 | Ecosystem integration boundaries/APIs/gateways, easy onboarding | P00, P01, P18, App B, App L |  |
| R-003 | Use owner's architecture docs as baseline + deep research | P00, P01, P03, App R |  |
| R-004 | Part 1 tool / Part 2 Excel questionnaires; Excel import & display | P03, P04, P05, App E |  |
| R-005 | Coverage RBI/SEBI/IFSCA/IRDAI/co-op/companies/LLPs + data & cyber (DPDP, GDPR, CCPA, IT Act, MeitY, CERT-In) | P03, P12, P15, App F, App G |  |
| R-006 | Change management with previous vs new actionable, audit trail, updates feed | P05, App E |  |
| R-007 | Separate logic/workflows per entity type | P02, P03, P15, P16, App E, App U |  |
| R-008 | Competitor research (Lexplosion, Lawrbit, LexComply, ManuComply, Simpliance, Aparajitha, data/cyber GRC, Big 4) | App R |  |
| R-009 | Internal governance (Companies Act, LLP Act, Societies Registration Act, regulators) | P06, P15, P16, App G |  |
| R-010 | Risk management incl. Basel Pillar 2/3 risks, all risk types, all entity types | P08, P09, P12, P13, P15, App H |  |
| R-011 | Risk assessment: stress testing, scenario analysis, scenario library, exports | P09, App H |  |
| R-012 | CRO dashboard, customisable | P08, P10, P15 |  |
| R-013 | Complete compliance tool (features, workflows, reports, exports, maker-checker) | P02, P04, P06, P07, P08, P10, P11, P12, P14, App A, App D, App E |  |
| R-014 | Labour codes, registers, POSH IC, other committees, employment agreement eSign, standalone SKU | P13, P20, App N, App T |  |
| R-015 | Client HRMS (payroll, leave, salary), people-risk data sharing | P08, P13, App H | Salary disbursal by bank file/payout partner (D-11) |
| R-016 | Free ~50-question health check with PAN/name API fetch, graphs, shareable report, lead generation | P01, P20, P23, App P, App X |  |
| R-017 | Tenant edits/adds questions, audit-trailed | P03, P07, App A, App D, App E |  |
| R-018 | Roles (maker, checker, dept head/VP, auditor, external auditor, board/management, RBI supervisor read-only) linked to HRMS | P01, P04, P06, P07, P10, P11, P13 |  |
| R-019 | Agentic AI | P17, App K |  |
| R-020 | "i" help, tutorials with text/images/diagrams/screenshots/videos (social-ready) | P02, P20, P23, App C, App N, App P |  |
| R-021 | Data preservation, exit export folder tree, BYO storage, structure stable across releases/infra moves, ecosystem sharing, folder intake | P00, P07, P08, P09, P12, P13, P19, P21, P22, P24, App M |  |
| R-022 | Accessibility | P23, App C, App P, App R |  |
| R-023 | Faster cross-team workflows | P08 |  |
| R-024 | Extensive settings | P08, P09, P12, P13, P14, P20, P21, P22 |  |
| R-025 | User types: super admin, operations, client admin, client users | P01, P22 |  |
| R-026 | Jio AI services | P17, P18, App L | No public Jio LLM API; channel adapters (§7) |
| R-027 | AI policy drafting, NotebookLM-style Q&A, reads documents/screenshots/WhatsApp/PDF/letters/email, eSign | P07, P17, App K |  |
| R-028 | Customisable UI/UX, fewer clicks, automation | P08, P09, P23 |  |
| R-029 | Aadhaar/PAN/DigiLocker/MCA/CIBIL onboarding APIs | P01, P18 | Challenged: no CIBIL pull at onboarding (X-07, D-25) |
| R-030 | Web-based, role dashboards | P01, P08, P09, P23, App C |  |
| R-031 | Platform privacy-law compliance (GDPR, CCPA, DPDP, IT Act) | P01, P12, App Q |  |
| R-032 | SEO/GEO/AI-search, clean modern UI | P23, App P, App R |  |
| R-033 | PCI DSS, SOC 2 Type 1/2, ISO readiness; Razorpay | P12, P20, P24, App Q | Readiness only; no claim until certified (NN-19) |
| R-034 | Transparent subscription, 7-day trial, plans, upgrade/downgrade, billing in settings, business-model research | P01, P20, P23, App N, App P |  |
| R-035 | Marketplace (LawDocs + third-party professionals, virtual CXOs, drafting, ICAAP, stress testing, retainers, SLA eSign, services without SaaS, GST invoices, Razorpay, email invoices) | P09, P21, App O | % commission OFF for regulated professions (D-06, NN-20) |
| R-036 | FinLegal Academy (trainings.lawdocs.in) in marketplace; public marketplace without login; categories | P21, P23, App O, App P |  |
| R-037 | Recurring revenue architecture; benefit explanations; detailed billing/membership settings | P20, App N, App P |  |
| R-038 | Advanced DMS (sharing, eSign, search, filter, selective share, OCR type copy of handwriting/WhatsApp, editable, translation from UN + major Indian languages to English; Claude API) | P07, P12, P14, P17, App K |  |
| R-039 | Configurable open/interim/waiting items; non-static rule engine; settings without super admin | P03, P04, P05, P08, P09 |  |
| R-040 | Operations (delivery, after-sales, marketing, brand, CS, social, PR, collaborations, CRM, onboarding, grievance, tickets; Brevo-open) | P22, App X | Group Operations Hub + delivery console (D-03) |
| R-041 | Staff appraisal, lifecycle, email IDs, anti-fraud, maker-checker | P22, App X | Operations Hub OH10–OH11; LDC addendum App X |
| R-042 | Staff leave/salary, WFH, login/logoff, work measurement, ROI | App X | Operations Hub OH10; LDC addendum App X |
| R-043 | M365 now / Google Workspace later; Office-openable; standard folder export | P07, P18, P19, P22, App J, App M, App X | "Business Starter" is not a Microsoft plan (D-10) |
| R-044 | Switchable revenue streams | P20, App N |  |
| R-045 | Business autopilot, funnels, marketing architecture, Brevo, Adobe Express, social calendar | P23, App P, App R, App X | Operations Hub OH7; ethical funnels (NN-44) |
| R-046 | Patch/change management, GitHub branches, backups, VAPT, IS/internal/external audit | P19, P24 |  |
| R-047 | Cross-functional group roles and data sharing | P01, P18, P19, P22, P24, App X |  |
| R-048 | RBI returns: CIMS, DAKSH, PRAVAAH; all applicable returns; data definitions; RBI supervisory-returns directions of 28 Nov 2025 | P11, App I | Erratum: supervisory-returns directions dated 31 Jul 2026 (X-12) |
| R-049 | CIC submissions (CIBIL, CRIF, Experian, Equifax; consumer & commercial) | P11, P18, App I, App L |  |
| R-050 | Import Tally Prime/Excel and convert to return formats | P11, P18, App L |  |
| R-051 | Ind AS/AS applicability by entity, ICAI resources, exports follow accounting/audit standards | P11, App J |  |
| R-052 | Draw data from Finbyx/Udofin/other LMS/Tally/Excel; export return-ready data | P09, P11, P18, App L |  |
| R-053 | Finbyx/Udofin data to generate agreements, annual reports, minutes; AI data-prep agents | P06, P11, P17, P18 |  |
| R-054 | ICSI secretarial standards | P06, P10, App J |  |
| R-055 | Audit (internal, secretarial, RBIA, IS, external, IT), ICAI guidance, AI draft reports, exports | P10, App J |  |
| R-056 | Client HRMS for KMPs/directors/departments; departmental structure of finance companies; Companies Act + RBI governance; task assignment | P01, P02, P06, P08, P09, P13, P15, P16, App D |  |
| R-057 | RBI supervisor read-only | P01, P04, P06, P10, P18 | Time-boxed tenant grant (D-12, NN-18) |
| R-058 | Risk function per RBI, supports Finbyx/Udofin data | P08, P09, P12, P13, P18 |  |
| R-059 | Basel Pillar 2/3; RBI/Basel ratios; KMP dashboards (CFO, CCrO, CEO, MD, CRO, IA, Board), customisable | P09, App H |  |
| R-060 | Capital adequacy prudential norms; ICAAP data from Finbyx | P09 |  |
| R-061 | CFO ratio dashboard from accounts, balance sheets, loan data | P09 |  |
| R-062 | Credit co-operative societies (MSCS Act, state Acts), modus operandi, all co-op types | P13, P14 | Credit operations in Finbyx (D-16) |
| R-063 | Jio Business services for clients and ops | P18, App L | JioCX channels, Haptik optional (§11) |
| R-064 | NBFC-ICC/investment entities: investments in equities, AIFs, REITs, IPOs; caps; accounting; ratios | P09, P15, App G, App H |  |
| R-065 | ARCs | P08, P09, P15, App G, App H |  |
| R-066 | Listed companies (SEBI LODR etc.) | P06, P14, P15, App G |  |
| R-067 | Savings page (money, hours, penalties avoided) | P04, P05, P20, App N |  |
| R-068 | Super admin override (→ D-02) | P00, P02, App A, App B | Met by Correction Entries (D-02, NN-02) |
| R-069 | Self-onboarding: health check → 7-day trial → PAN → API fetch → choose sections → computed price | P01, P20, P23 |  |
| R-070 | Pricing page: 3 packages (small, large, enterprise custom), base + add-ons, fully configurable (prices, components, discounts, promo codes, trial extension per company, features, comparison), Apple-style configurator, services-only checkout | P20, P23, App N, App P |  |
| R-071 | Super admin changes components/settings/documents/pricing/audit annotations/dates per client (→ D-02) | P06, P07, P20 | Met by Correction Entries (D-02) |
| R-072 | Retainer RM acts as maker, client employee as checker; multiple makers; both sides create makers | P01, P02, P03, P04, P21, P22, App A, App D |  |
| R-073 | Per-client delivery section: credential tracker, billing sync, messaging, shared drive link, file delivery | P22 | Credential vault design (D-04, NN-17) |
| R-074 | Super admin edits crucial client master data; ops serves | P00, P22 |  |
| R-075 | Event audit trail | P00, P06, P07, P08, P09, P10, P11, P20, P22 |  |
| R-076 | User data download | P07, P19, P20 |  |
| R-077 | Return-ready data for RBI/SEBI/IFSCA/GST/tax portals with agentic AI | P09, P11, P17 |  |
| R-078 | Import balance sheets, annual reports, books, dumps, Tally for ratios/risk/audit/annual report drafts | P09, P11 |  |
| R-079 | GST/tax exports (financial companies via Finbyx, borrowers via Udofin) | P11 | Narrowed: borrower certificates stay with Finbyx/Udofin (X-31) |
| R-080 | Grievance redressal: help & support → GRO → escalation/IO → Ombudsman; GRO workspace in LDC; client support closes tickets in LDC; website link | P14 |  |
| R-081 | Full tenant download; BYO servers/backups | P07, P19, P24 |  |
| R-082 | Client HRMS with M365/Google; OneDrive/SharePoint/Drive; own DC/disks | P07, P18, P19 |  |
| R-083 | Internal team dashboards apart from super admin | P00, P01, P22, App C, App X |  |
| R-084 | Excel templates per entity family with family-specific dropdowns | P03, App E |  |
| R-085 | AI questionnaire generation from an uploaded instrument (super admin global; client admin tenant-only) with export → verify → re-upload → confirm | P05, P17, App E, App K |  |
| R-086 | Customisation hierarchy regulator → company → department → function; renameable departments/functions | P02, P03, P06, P08, P13, App E, App U |  |
| R-087 | Instrument catalogue with name, date, update date, applicability, add/remove checkboxes; tenant edits tenant-only; audit trail | P03, P15, App E |  |
| R-088 | Audit trails for super-admin content changes, tenant changes, maker/checker actions, status changes; what changed vs previous direction | P02, P08, App A, App E |  |
| R-089 | 20:00 IST scan of RBI, SEBI, IRDAI, IFSCA, co-op departments, news; push, email, calendar | P05, App F | 20:00 IST scan + intraday feeds (D-18) |
| R-090 | Updates vs Notifications | P04, P05, App A, App C |  |
| R-091 | Policy management (versions, owner, board approval date, next review, model templates, Word, Vidhi drafts with track changes, upload approved PDF) | P07, P17 |  |
| R-092 | Committee management (HRMS-linked members, AI agenda/minutes, calendar, committee pages, custom names) | P06, P17 |  |
| R-093 | Governance hierarchy MCA/ROC → Companies Act → regulator; fit & proper docs; co-op elections and office bearers | P06, P13, P15, P16 |  |
| R-094 | Calendar sync (M365, Google, Outlook.com, Gmail, Apple via ICS/CalDAV); role-scoped visibility | P04, P06, P18, App C |  |
| R-095 | Tasks by hierarchy; tasks to Vidhi; scheduled/recurring tasks | P04, P06, P07, P17, App A |  |
| R-096 | Co-op societies end-to-end affairs | P16, App S | Elections conducted by authority (X-34) |
| R-097 | Vidhi AI employee (Viktor-like), knowledge notebooks per regulator | P10, P11, P17, App K |  |
| R-098 | Website/app/LMS/LOS/recovery/LSP integration; grievance link on client site | P14, P18 |  |
| R-099 | Company secretary assistance, board-portal features incl. listed companies | P06, App C |  |
| R-100 | Marketplace certification services (SOC 2, ISO), extra offerings, memorable client experience | P21, P23, App O, App R |  |
| R-101 | Final review, verify Excel templates, fix errors, deliver to folder | P00, P23, P24, App I |  |
| R-102 | Data-compliance Excel sheets (DPDP, GDPR, CCPA, cyber) in the same format (Part 2) | P05, P12, P13 |  |
| R-103 | *(v1.1)* Re-read all attached files; improve logic and workflow; add details | All phases and appendices (v1.1 markers), App AC | Traceability matrix of 1,069 rows |
| R-104 | *(v1.1)* Archive or delete previous and older versions | Delivery folder `_Archive (older versions)` | Deletion needs owner approval |
| R-105 | *(v1.1)* Future-ready system using AI developments | P17, App AA, App K, P18 (MCP/A2A), P12 (`OV_AI`) | D-34–D-38, NN-50–NN-52 |
| R-106 | *(v1.1)* Faster workflows and customisations wherever possible | App Z backlog, App C §C.11 click budgets, P02, P04 and all phases | NN-49 |
| R-107 | *(v1.1)* Find and fix errors and mistakes | `02` §3.5, `_review/` logs | — |
| R-108 | *(v1.1)* Only the 28 Nov 2025 consolidated RBI directions are uploaded for RBI families | `catalogue/`, App AB, P03, P05, P15, part2_prompts 00–06 | D-39, D-40, NN-55 |
| R-109 | *(v1.1)* Explore other GRC platforms and client feedback; reverse-engineer existing products | App Z, App R §R.15 | IMP-001–IMP-142 |
| R-110 | *(v1.1)* Take the product global; support global compliances later | P25, App Y, INTL-GEN template, P20/P21/P23 global hooks | D-42–D-46, NN-53, NN-54 |
| R-111 | *(v1.1)* Study how Lawrbit serves companies abroad | App Y §Y.2 (delivery-model analysis) | — |

---

## 9. Review log (v1.0)

| Step | What was done |
|---|---|
| Planning | Eight planning questions answered by the owner (D-01–D-08). Reference corpus read: owner's Architecture Parts 1–3, earlier Master Build Prompt, two Excel samples, 43 finished IFSCA sheets, Finbyx v1.5, Udofin v1.2, Operations Hub v1.0, Ecosystem Spec v1.1, Equator v3.1. |
| Research and drafting | Twelve parallel streams (S1–S12) researched primary sources and wrote 25 phase files, 22 appendices, 24 Excel templates with a validator, 26 Part-2 prompt files and contribution registers. |
| Integration (lead) | Twenty-seven stream NN proposals consolidated into fourteen rules, NN-33–NN-46 (§3.3); 41 cross-file resolutions recorded (master §18); template and data-template codes harmonised across files (X-09); 53 department names mapped to codes (Appendix U §U.9.0); event naming rule (X-01) and billing ownership (X-02) fixed; screen, settings, event, error, test and open-item registers compiled into Appendices B §B.9, C §C.9, U §U.9, V and W. |
| Verification | Load-bearing facts re-checked on 25 Oct 2026 (RBI 28 Nov 2025 consolidation, RBI DoS 31 Jul 2026 set, SEBI MF Regulations 2026, Bedrock India availability). 1,154 [VERIFY] markers remain, each a flag for the build (Appendix W §W.2). |
| v1.1 (25 Oct 2026) | Five research streams (global expansion and Lawrbit; client feedback and reverse engineering; future-ready AI; RBI consolidated-directions catalogue; baseline traceability audit), six improvement editors (every phase and appendix improved in place, marked *(v1.1)*), one cross-file resolution pass and a lead integration. Added P25–P28, Appendices Y, Z, AA, AB, AC, the RBI catalogue workbook, three template families (27 total, 27/27 validator PASS with both owner samples), NN-47–NN-55, D-34–D-48, X-42–X-60, R-103–R-111. Appendix AC re-audit after the merge: 938 covered, 77 partial, 12 missing, 42 changed by decision (open rows listed in §AC.0). |
