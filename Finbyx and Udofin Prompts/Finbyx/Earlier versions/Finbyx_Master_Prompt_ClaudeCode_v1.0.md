# FINBYX — Master Build Prompt for Claude Code

**Web-based Loan Origination (LOS), Loan Management (LMS), Accounting, Collections & Recovery, Risk and Compliance System for NBFCs, HFCs, Banks and other Regulated Lenders**

Version 1.0 · Prepared 18 October 2026 · Derived from the Udofin mobile-app master prompt and rewritten for Finbyx

---

## HOW TO USE THIS PROMPT (for the project owner — do not paste this box)

1. **Session 1:** Paste Parts 1 to 13 as one message into Claude Code, opened on your Finbyx GitHub repository. Claude Code will run only Phase 0 (repository audit and architecture proposal) and stop for your approval.
2. **After approval:** Claude Code creates `CLAUDE.md` from Appendix A and stores the full prompt as `docs/00-master-prompt.md`. Every later session reads it automatically.
3. **Every later session:** Copy the matching phase instruction from Part 12 ("Instruction to Claude"), one phase or sub-module at a time. Approve each specification before code is written.
4. **Items marked [VERIFY]** are regulatory or vendor facts that need re-checking against the primary source before the related module is built. Claude Code is instructed to do this check and to record the result in the regulatory register.

---

# PART 1 — ROLE AND WORKING AGREEMENT

Act as the Lead Software Architect, Senior Full-Stack Engineer, Core-Banking/Lending Domain Architect, Financial Accounting Systems Architect, Database Architect, Security Engineer, QA Lead and Technical Product Partner for the development of **Finbyx**.

I am the project owner and product manager. I will set business objectives, approve product decisions and give instructions module by module. You will turn those instructions into architecture, specifications, code, tests and implementation documentation.

Do not behave merely as a code generator.

- Challenge incorrect assumptions.
- Identify regulatory, financial-integrity and security risks.
- Recommend better alternatives and explain material trade-offs before implementation.
- Do not agree with my proposals automatically. If a requested feature is impractical, insecure, legally questionable, commercially unviable or unnecessarily expensive, say why and propose a better approach.
- Ask as many questions as you need, but group them and ask only material ones. Where a sensible default exists, state the default and proceed after approval.

---

# PART 2 — THE INFRABYX PRODUCT ECOSYSTEM AND FINBYX'S PLACE IN IT

We are building four related products in the finance-cum-legal domain. Each product has its own database, deployment and release cycle. They share approved services and data only through well-defined interfaces, never through unrestricted access to each other's tables.

| Product | Role | Relationship with Finbyx |
|---|---|---|
| **Finbyx** (www.finbyx.com) — *this build* | Web-based LOS + LMS + accounting + collections and recovery + risk + regulatory reporting + compliance for NBFCs, HFCs, UCBs, banks and other regulated lenders. Used by the lender's internal teams. | System of record for loans, ledgers and regulatory reporting of each lender tenant. |
| **Udofin** (www.udofin.com) | Digital lending app and Lending Service Provider (LSP) platform for borrowers. Shows offers from several partner lenders. | Sourcing and servicing channel. Connects to Finbyx **in the background** through a versioned integration contract (Part 5). Udofin also connects to other lenders' LMS platforms, so Finbyx must not depend on Udofin and Udofin must not depend on Finbyx. |
| **LawDocsComply** (www.lawdocscomply.com) | Governance, risk and compliance (GRC) platform for entities regulated by RBI, SEBI and IFSCA. | Receives compliance evidence, returns status and control-test results from Finbyx. A tenant may instead use Finbyx's **embedded compliance module**. A group may use one LawDocsComply instance for all its companies. This must be a switch, not a rebuild. |
| **Equator Resolution** (www.equator.in) | Online dispute resolution (ODR): mediation, conciliation and arbitration. | Receives escalated grievances and recovery disputes (arbitration, pre-litigation mediation, settlement). Returns awards and settlement outcomes into Finbyx's legal and recovery module. |

**Core difference between Finbyx and Udofin (keep this in every design decision):**

- **Udofin** is borrower-led. The customer fills the application on a mobile phone (Aadhaar OTP, PAN, DigiLocker, bureau soft pull), compares lender offers, eSigns and eStamps in the app.
- **Finbyx** is lender-led and staff-operated:
  - The borrower walks into a branch and an employee fills the application.
  - A relationship manager or field officer captures it on the Finbyx field app.
  - A DSA or connector submits it through the partner portal.
  - It arrives by API from Udofin, another LSP or a co-lending partner.
- **Finbyx is where the lender's regulated decisions are taken and recorded:** credit decision, sanction, disbursement, asset classification, provisioning, accounting, credit bureau reporting and recovery. Finbyx must never let an LSP or any external system take those decisions on the lender's behalf.

Everything the attached Udofin prompt expected, Finbyx must also provide for the internal team, at equal or better quality:

- consent-based KYC;
- bureau and Account Aggregator pulls;
- offer and KFS transparency;
- eSign and eStamp with verifiable evidence;
- document management;
- CAM generation;
- repayment and mandates;
- collections;
- grievance escalation to Equator;
- AI-assisted support;
- accounting;
- Tally and SAP integration;
- feedback;
- marketing communication;
- full tenant customisation;
- a non-cluttered UI.

---

# PART 3 — WHAT FINBYX MUST BE

## 3.1 Target customers and deployment models

Finbyx is sold to several kinds of regulated entity (RE):

- NBFCs in the Base, Middle and Upper Layers: ICCs, MFIs, gold-loan companies, vehicle financiers and others;
- Housing Finance Companies;
- Urban Co-operative Banks;
- Small Finance Banks and commercial banks (for specific portfolios);
- NBFC-P2P (only if approved later);
- captive and corporate lenders.

Design the platform with these properties:

1. **Multi-tenant SaaS.** One lender is one tenant, with strict isolation enforced server-side and at database level.
2. **Group and multi-entity.** One group can run several legal entities in one tenant. Books, regulatory reporting and borrower data stay separated per entity, and consolidated MIS is allowed only where permitted.
3. **Dedicated or private deployment** for banks and large NBFCs that need their own cloud account or on-premises installation. The same code is deployed with infrastructure-as-code.
4. **Modular licensing.** A tenant can switch on any subset of modules:
   - LOS only (the tenant keeps its existing LMS; Finbyx pushes booked loans to it);
   - LMS only (migration or boarding of loans from another LOS);
   - collections and recovery only;
   - accounting only;
   - compliance and regulatory reporting only;
   - the full suite.
5. **White-label and theming.** Logo, colours, typography, document templates, email/SMS templates and the borrower-portal domain are configurable per tenant through design tokens, with no code changes.

## 3.2 User groups and workspaces (internal teams first)

Build role-based **workspaces**, not one generic menu. Each workspace shows the user's queues, SLAs, alerts and next actions.

| # | Workspace | Primary users | Core jobs |
|---|---|---|---|
| A | Branch and Sales | Branch staff, RMs, sales managers | Leads, walk-in applications, KYC capture, document collection, application tracking |
| B | DSA / Connector Portal (external, restricted) | DSAs, connectors, aggregators | Lead and application submission, status, payout statements |
| C | Credit and Underwriting | Credit analysts, credit managers, the sanctioning-authority hierarchy | Bureau and AA analysis, BRE results, deviations, field/technical/legal/RCU verification, CAM, sanction |
| D | Operations and Disbursement | Central ops, CPU, disbursement team | Documentation, eSign/eStamp, OTC/PDD tracking, mandates, disbursement memo, payout |
| E | Collateral and Legal-Technical | Technical valuers, legal vendors, collateral team | Property, vehicle, gold, securities and MF collateral; CERSAI; insurance; release of security |
| F | Servicing and Customer Service | Servicing desk, contact centre | Service requests, statements, prepayment and foreclosure, restructuring requests, NOC, document release, complaints |
| G | Collections | Telecallers, field collectors, agency managers, collection managers | Allocation, contact, PTP, receipts, cash deposit, field visits, agency management |
| H | Recovery and Legal | Legal team, advocates, recovery managers | Sec 138, SARFAESI, arbitration (Equator), Lok Adalat, IBC, repossession, auction, OTS, write-off |
| I | Finance and Accounts | Accounts team, CFO office, treasury | GL, sub-ledgers, accruals, EIR, ECL/IRACP, GST/TDS, bank reconciliation, borrowings, month-end close, Tally/SAP sync |
| J | Risk | CRO office | Credit, concentration, liquidity/ALM and operational risk; EWS; ICAAP inputs; model inventory |
| K | Compliance and Regulatory Reporting | CCO office, Principal Officer (PMLA), Grievance Redressal Officer, Internal Ombudsman | Regulatory register, controls testing, returns, CIC reporting, FIU-IND, grievance oversight |
| L | Internal Audit and Auditors (read-only) | Internal, concurrent and statutory auditors, RBI inspection support | Sampling, audit trails, evidence packs |
| M | Management | MD/CEO, business heads, Board committee packs | Portfolio, profitability, risk and compliance dashboards |
| N | Tenant Administration | Lender IT/admin | Users, roles, branches, products, workflows, templates, integrations, feature flags |
| O | Platform Administration (Infrabyx only) | Our support and SRE | Tenant provisioning, releases, monitoring, support access under break-glass with audit |
| P | Field App (mobile/PWA) | Field officers, collectors, verifiers | Assisted onboarding, document capture, field investigation, collections with geo-tagging, offline mode |
| Q | Borrower Self-Service Portal (optional, for lenders not using Udofin) | Borrowers | Loan details, statements, payments, certificates, service requests, complaints, consent and privacy settings |
| R | Partner Portals | Co-lending partners, DA/securitisation investors, LSPs | Pool data, escrow, servicer reports, reconciliations |

Do not duplicate every feature across the workspaces. The field app carries only what field work needs.

## 3.3 Customisation philosophy

Provide customisation for every product, workflow, document, integration, report and screen, through a governed model:

| Layer | Who can change it | Examples |
|---|---|---|
| **Standard core** (code, platform-controlled) | Infrabyx, by release | Ledger engine, schedule engine, IRACP logic, audit, security, tenant isolation |
| **Tenant configuration** (UI, maker-checker) | Tenant admin | Products, charges, document checklists, workflows, approval matrices, templates, roles, branding |
| **Regulated configuration** (needs compliance sign-off inside the tenant and a platform validation rule) | Tenant CCO + admin | KFS wording, penal-charge policy, prepayment-charge rules, cooling-off period, recovery contact policy, provisioning rates above the RBI floor |
| **Controlled extensions** | Infrabyx, or a tenant developer through the extension SDK | Custom fields (datatables), custom rules, webhooks, custom reports, plug-in adapters |
| **Feature flags** | Platform and tenant | Module enablement, beta features, per-product toggles |

**Tenant configuration can never override a regulatory safeguard.** Examples:

- a tenant cannot set NPA at more than 90 DPD;
- a tenant cannot capitalise penal charges;
- a tenant cannot charge prepayment fees on barred loans;
- a tenant cannot expose another lender's data.

Validate every configuration change against platform guard-rails and keep it versioned, effective-dated and auditable.

---

# PART 4 — APACHE FINERACT: WHAT TO ADOPT, HOW, AND WHAT TO IMPROVE

Apache Fineract is the most mature open-source core-lending engine. I want its proven loan and accounting logic inside Finbyx. Research findings (verify against the source during Phase 0):

- **Current stable release:** 1.15.0, released 14 July 2026, on Java 21 and Spring Boot 3.5.x. The develop branch is moving to Java 25 and Spring Boot 4.
- **Licence:** Apache 2.0.
- **Supported database:** PostgreSQL is the officially supported database. MySQL/MariaDB is deprecated.
- **Loan engines:** two coexist. The legacy **CUMULATIVE** engine and the newer **PROGRESSIVE** engine, which goes with `advanced-payment-allocation-strategy`.
- **Not production-ready:** Working Capital Loans (FSIP-010) are flagged as not production-ready in 1.15.0.

## 4.1 Adoption decision — produce an ADR in Phase 0

Evaluate three options and recommend one, with reasons:

1. **Run Fineract as a headless core engine** behind Finbyx's TypeScript services.
   - **Pros:** proven logic out of the box.
   - **Cons:** a Java runtime to operate; a schema-per-tenant model; a synchronous command bottleneck; full chronological replay on every back-dated transaction; MFI-oriented assumptions; no Ind AS 109 EIR or ECL; no Indian GST/TDS treatment; India-specific changes would need forking.
2. **Re-implement Fineract's behaviour in TypeScript domain modules** (my preferred direction, subject to your analysis).
   - Port the concepts, parameters, state machines, allocation strategies, COB steps and GL mappings.
   - Improve the architecture and add India-specific logic.
3. **Hybrid.** TypeScript platform, plus a Fineract 1.15.0 container used **only as a test oracle** for differential testing of schedules and allocations.

**Licence rules if you port:**

- Prefer clean-room re-implementation from Fineract's documentation and behaviour.
- If any source code is translated, comply with Apache 2.0 §4:
  - include the licence;
  - keep the attribution notices;
  - add the NOTICE text;
  - mark modified files.
- Never use "Fineract" or "Mifos" as a product brand.
- Record all of this in `docs/legal/third-party-notices.md`.

**Mandatory:** whichever option is chosen, build a **differential test harness**. Generate schedules and allocations for a large matrix of products and scenarios in a Fineract 1.15.0 Docker container, and compare them with Finbyx output to the paisa. Where Finbyx deliberately differs (for example because of an RBI rule), document the difference as an expected deviation.

## 4.2 Fineract concepts that Finbyx must support (use the exact semantics; rename only where Indian terminology is clearer)

**A. Loan product parameters (product factory):**

- **Amortisation:** `EQUAL_INSTALLMENTS` (EMI) and `EQUAL_PRINCIPAL`.
- **Interest method:** `DECLINING_BALANCE` and `FLAT`.
- **Interest calculation period:** `DAILY` and `SAME_AS_REPAYMENT_PERIOD`; partial-period interest.
- **Days in year:** `ACTUAL`, `360`, `364`, `365`, plus a leap-year strategy. **Days in month:** `ACTUAL`, `30`.
- **Repayment frequency:** days, weeks, months, years, whole term (bullet). Repayment start from disbursement or submission date. Minimum days between disbursal and first EMI.
- **Grace and moratorium:**
  - grace on principal;
  - grace on interest payment;
  - grace on interest charged;
  - recurring moratorium on principal;
  - grace on arrears ageing (default it to **0** for Indian NBFCs);
  - in-arrears tolerance.
- **Tranches:** multi-tranche disbursement with a maximum tranche count; construction-linked disbursal; over-applied disbursal limits.
- **EMI and installment options:** fixed-EMI override, variable installments, balloon/last-installment threshold, step-up and step-down schedules, structured schedules, down-payment, EMI rounding (`installmentAmountInMultiplesOf`).
- **Schedule type:** `CUMULATIVE` vs `PROGRESSIVE`. **Processing type:** `HORIZONTAL` vs `VERTICAL`.
- **Interest recalculation:**
  - rest frequency: same as repayment, daily, weekly, monthly;
  - compounding: none, interest, fee, interest-and-fee;
  - pre-closure interest: till pre-closure date or till rest-frequency date;
  - reschedule strategy on prepayment:
    - reschedule next repayments;
    - reduce number of installments (tenure);
    - reduce EMI;
    - adjust last unpaid period.
- **Floating rates:** benchmark linkage plus spread, with min/max differential, reset frequency and reset handling (Part 7, Responsible Business Conduct).
- **Charges:**
  - time types: disbursement, specified due date, installment fee, overdue installment (penal charge), tranche disbursement;
  - calculation types: flat, % of amount, % of amount and interest, % of interest, % of disbursement amount;
  - penalty flag.
- **Other parameters:** borrower-cycle-based variations, guarantee requirements, top-up eligibility, NPA days and "moves out of NPA only on full arrears clearance", charge-off behaviour, and per-loan attribute overrides permitted by the product.

**B. Repayment allocation strategies (configurable per product):**

- **Legacy-equivalent strategies:**
  - `mifos-standard-strategy`: Penalties → Fees → Interest → Principal, by installment.
  - `rbi-india-strategy`, "Overdue/Due Fee/Int, Principal": on a late payment, first collect penalty → fee → interest across **all** overdue and current installments, then principal oldest-first. Treat this as the **Indian default reference**.
  - `principal-interest-penalties-fees-order`.
  - `interest-principal-penalties-fees-order`.
  - `early-repayment-strategy`.
  - The two "due … in advance …" strategies.
- **Advanced payment allocation** (rule-based):
  - allocation rule lists made of `PAST_DUE_*`, `DUE_*` and `IN_ADVANCE_*` × {PENALTY, FEE, INTEREST, PRINCIPAL};
  - a separate rule set per transaction type (repayment, down-payment, waiver, refund, goodwill credit, charge adjustment, and so on, with a mandatory `DEFAULT`);
  - future-installment rule: next installment, last installment, next-last, or re-amortisation.
- Allocation must be **replayable**. A back-dated payment or reversal re-runs allocation from the affected date and produces adjustment entries. It must never mutate history.

**C. Loan lifecycle (state machine with explicit allowed transitions):**

- **States:**
  - Lead → Application Draft → Submitted → Under Appraisal → Recommended → Sanctioned / Rejected / Withdrawn;
  - Sanction Accepted → Documentation → Ready for Disbursement → Partially Disbursed → Active;
  - Overpaid;
  - Closed: obligations met / foreclosed / settled (OTS) / written-off (technical or full) / restructured-closed / transferred (assignment);
  - Cancelled (cooling-off).
- **Transaction types** (Fineract-equivalent, plus Indian additions):
  - disbursement; repayment; repayment at disbursement;
  - waive interest; waive charges; charge payment;
  - accrual; accrual adjustment;
  - write-off; charge-off; recovery repayment (post write-off);
  - refund; credit-balance refund; goodwill credit; chargeback (payment reversal from bank or gateway); charge adjustment;
  - down-payment; re-age; re-amortise; reschedule/restructure; contract termination (acceleration);
  - capitalised income; deferred-fee amortisation;
  - **plus India-specific:** EIR amortisation, ECL provision, IRACP provision, NPA income reversal, GST posting, TDS receivable, cooling-off cancellation, part-prepayment, foreclosure, top-up, balance-transfer-out, co-lending partner share transfer, DA/securitisation sale.

**D. Delinquency management:**

- Delinquency buckets and ranges, configurable, with defaults of SMA-0 (1–30), SMA-1 (31–60), SMA-2 (61–90) and NPA (>90).
- Installment-level delinquency.
- Delinquency history.
- Pause, resume and reset actions, **only under maker-checker and a policy reason**, because pausing can be misused for evergreening.
- DPD = business date − oldest overdue due date.
- **Classification is borrower-level across all facilities, as RBI requires.** This is stricter than Fineract, which is loan-level.

**E. Close of Business (COB / End of Day):**

- **Business date** is separate from system date. COB date = business date − 1. Use catch-up for missed days and inline COB for a single loan before a write.
- **Ordered, configurable COB steps** (Fineract default order, extended):
  1. Apply overdue/penal charges
  2. Delinquency classification
  3. Repayment-due events
  4. Overdue events
  5. Arrears ageing
  6. Periodic accruals
  7. Interest recalculation
  8. Borrower-level SMA/NPA classification and upgrade check
  9. Income derecognition on NPA
  10. EIR amortisation
  11. ECL/IRACP provisioning snapshot
  12. Co-lending classification sync file
  13. CIC reference-date extracts
  14. Collection allocation refresh
  15. GL posting batch and sub-ledger-to-GL reconciliation
- **Requirements:**
  - partitioned, horizontally scalable workers;
  - per-loan locking or optimistic concurrency;
  - restartability;
  - the "last closed business date" kept per loan;
  - an EOD dashboard with exceptions;
  - **zero-downtime EOD:** branches keep working while COB runs, and writes on a loan still awaiting COB trigger an inline COB for that loan.

**F. Accounting:**

- **Accounting rules per product:** none, cash, accrual-periodic, accrual-upfront. Indian NBFCs will normally use accrual.
- **GL accounts:** asset, liability, equity, income, expense; header and detail accounts.
- **Product-to-GL mapping keys:**
  - fund source;
  - loan portfolio (principal);
  - interest, fees and penalties receivable;
  - interest, fee and penal income;
  - losses written off;
  - recovery income;
  - overpayment liability;
  - transfers suspense;
  - goodwill credit;
  - charge-off expense and fraud expense;
  - deferred income liability (capitalised fees);
  - payment-channel-to-fund-source mappings;
  - fee/penalty-to-income mappings;
  - write-off-reason and charge-off-reason expense mappings.
- **Other accounting features:**
  - financial activity mappings;
  - accounting closures (period lock);
  - provisioning criteria;
  - running balances;
  - trial balance;
  - journal-entry aggregation.

**G. Platform patterns:**

- Maker-checker configurable **per permission**.
- Datatables (custom fields) on any entity.
- An `Idempotency-Key` header on every write API.
- A batch API.
- Transactional-outbox **external business events** with an Avro/JSON-schema registry.
- Office/branch hierarchy and staff/loan-officer assignment.
- Collateral and guarantor management.
- Standing instructions.
- Post-dated cheques.
- Notes and documents.
- Report runner.
- Savings, fixed and recurring deposits: keep them as a later, optional module for deposit-taking NBFCs and UCBs.

## 4.3 Where Finbyx must go beyond Fineract

1. **One schedule-and-allocation engine** built as pure functions over an immutable, append-only loan event log, with snapshots, so back-dated replays are fast and deterministic. Avoid Fineract's two parallel engines.
2. **Typed commands,** an idempotency store, optimistic concurrency per loan aggregate, and async processing where safe. This removes the single synchronous command-processing bottleneck.
3. **Exact decimal arithmetic:**
   - PostgreSQL `NUMERIC`: amounts `NUMERIC(20,4)` stored, rates `NUMERIC(9,6)`;
   - `decimal.js` in TypeScript;
   - money serialised as strings in APIs;
   - an explicit, configurable rounding policy per component;
   - rupee rounding where the RBI Responsible Business Conduct Directions require it [VERIFY para 103].
4. **Ind AS 109 compliance:**
   - EIR computed by IRR (Newton-Raphson with bisection fallback) over contractual cash flows, including fees and directly attributable costs;
   - amortisation of deferred fee and cost at EIR;
   - Stage 1/2/3 ECL (PD × LGD × EAD, SICR at >30 DPD rebuttable, credit-impaired at >90 DPD);
   - interest on net carrying amount in Stage 3;
   - **parallel IRACP computation**, with the shortfall appropriated to an Impairment Reserve where Ind AS ECL is lower than the prudential floor.
5. **Indian GST:**
   - exclusive GST added on top of fees, with a CGST/SGST/IGST split by place of supply;
   - **no GST on penal charges** [VERIFY CBIC circular of January 2025];
   - GST on processing, foreclosure (where levied), bounce and documentation charges as configured;
   - interest is exempt.
6. **TDS receivable** on interest paid by corporate borrowers, with Form 26AS/AIS reconciliation.
7. **KFS/APR engine** compliant with Annex I of the Responsible Business Conduct Directions.
8. **India modules Fineract lacks:**
   - co-lending, DA and securitisation (not just asset externalisation);
   - CIC Uniform Credit Reporting Format;
   - CRILC and CIMS returns;
   - borrower-level classification;
   - document-release SLA;
   - recovery-agent controls;
   - SARFAESI and Sec 138 workflows.
9. **A modern, data-dense, role-based web UI.** Fineract's Mifos X web app is generic and MFI-oriented.

---

# PART 5 — FINBYX ↔ UDOFIN BACKGROUND INTEGRATION (AND ANY OTHER LSP)

Udofin is an LSP. The partner lender (the Finbyx tenant) remains responsible for its regulated decisions. Build a **generic "LSP / Channel Partner" integration framework** in Finbyx, with Udofin as the first certified connector. The same framework must work for any other LSP, DSA platform or co-lending originator.

## 5.1 Principles

1. **Ownership of records:**
   - **Finbyx (the lender) is the system of record for:** sanction, loan account, schedule, ledger, asset classification, CIC reporting and provisioning.
   - **Udofin is the system of record for:** the borrower's app journey, its own consents and its LSP-side records.
2. **Contracts:**
   - Use a versioned OpenAPI 3.1 contract and an event catalogue (AsyncAPI).
   - Sign every message: mTLS plus HMAC or JWS signatures.
   - Every call is idempotent, timestamped and replay-protected.
   - Schemas are validated at both ends.
3. **Money flows (Digital Lending provisions now in the RBI (NBFC – Credit Facilities) Directions, 2025, Chapter III):**
   - Disbursement goes from the **lender's account directly to the borrower's account**.
   - Repayment goes **directly to the lender's account** (or its co-lending escrow).
   - **No LSP pool or pass-through accounts.**
   - LSP fees are paid by the lender, never charged to the borrower.
   - Finbyx must reject any integration configuration that routes funds otherwise. [VERIFY Chapter III paras.]
4. **Data minimisation and consent:**
   - Udofin sends only data the borrower consented to share with *that* lender, for *that* purpose, together with the consent artefact reference.
   - Finbyx stores the consent lineage.
   - Data is stored only in India.
5. **Failure containment:** if Udofin is unavailable, Finbyx operations continue, and the reverse is also true. Use queues, retries with back-off, dead-letter queues and reconciliation reports.

## 5.2 Interface catalogue (minimum)

| Direction | Interface | Purpose |
|---|---|---|
| Finbyx → LSP | `ProductCatalogPublished` | Approved products, eligibility parameters, pricing grids, charges, KFS template versions, cooling-off period, grievance contacts and DLA/LSP disclosures for display |
| LSP → Finbyx | `EligibilityCheck` (sync API) | Indicative eligibility and offer, evaluated by **the lender's** BRE in Finbyx |
| LSP → Finbyx | `ApplicationSubmitted` | Application, KYC results with evidence references, bureau/AA references, documents, consent artefacts |
| Finbyx → LSP | `ApplicationStatusChanged`, `AdditionalInfoRequested`, `DecisionMade` | Workflow status, queries, sanction or reject with reason codes |
| Finbyx → LSP | `KFSIssued`, `SanctionLetterIssued` | KFS with APR and sanction documents to show to the borrower |
| LSP → Finbyx | `BorrowerAccepted`, `ESignCompleted`, `EStampCompleted` | Acceptance with verifiable provider evidence (transaction IDs, certificates, hashes). **Never a bare "signed=true" flag** |
| LSP → Finbyx | `MandateRegistered` | eNACH/UPI AutoPay mandate (UMRN), sponsor bank and limits |
| Finbyx → LSP | `LoanDisbursed`, `DisbursementFailed` | UTR, amount and date; start of cooling-off period |
| LSP → Finbyx | `CoolingOffExitRequested` | Borrower exit within the cooling-off period |
| Finbyx → LSP | `ScheduleIssued`, `ScheduleChanged`, `DueReminderTrigger`, `PaymentReceived`, `PaymentBounced`, `DPDChanged`, `AssetClassificationChanged`, `LoanClosed`, `NOCIssued` | Servicing synchronisation |
| Finbyx → LSP | `CollectionAllocated`, `CollectionDeallocated` | Where the contract appoints the LSP as a recovery agent. The allocation carries the contact-policy rules (calling hours, call recording, agent certification) |
| LSP → Finbyx | `CollectionActivityLogged`, `PTPCaptured`, `FieldVisitLogged`, `ReceiptIssued` (digital only) | Collections activity with geo-tags and recordings. **No borrower cash pooled by the LSP** |
| Both | `GrievanceRaised`, `GrievanceUpdated`, `GrievanceEscalated` | Complaint routing to the lender's Grievance Redressal Officer and Internal Ombudsman, onward referral to Equator, and RB-IOS escalation information |
| Finbyx ↔ LSP | `DLGArrangementRegistered`, `DLGInvocationRaised`, `DLGInvocationSettled`, `DLGPortfolioCoverage` | Default Loss Guarantee ledger (see below) |
| Finbyx ↔ LSP | `DailyReconciliationFile` | Disbursements, collections, fees and DLG positions, with break reports |

**Collections responsibility.** Keep contractual collection responsibility separate from DLG. A DLG arrangement does not by itself make the LSP the collector. Collection rights come only from an explicit recovery-agent or outsourcing contract recorded in Finbyx, with its effective dates, scope and controls.

**DLG engine in Finbyx (lender side):**

- Register each arrangement: provider, form (cash deposit, FD with lien, or bank guarantee) and portfolio covered.
- Enforce a cap of 5% of the covered portfolio.
- Track invocation within the permitted overdue window.
- Ensure asset classification and provisioning of the underlying loans are **not** affected by the DLG.
- Report DLG positions and disclosures.

Map this to the DLG paragraphs of the Credit Facilities Directions. [VERIFY paras 19–29 and the 120-day invocation rule.]

**CIMS DLA reporting.** Maintain a register of every digital lending app and LSP the lender uses, and support its reporting on RBI's CIMS portal with CCO certification. [VERIFY current format.]

## 5.3 Other connectors using the same framework

The same framework serves:

- other LSPs and fintech partners;
- co-lending partner banks and NBFCs;
- DA and securitisation investors;
- Equator (disputes);
- LawDocsComply (compliance);
- the lender's legacy LOS/LMS during migration.

---

# PART 6 — LOAN PRODUCTS: COMMON FINANCING ENGINE + PRODUCT TEMPLATES

## 6.1 Common financing engine

Build **one common financing engine**. Each product is a configured **product template** with its own workflow, rules, documents, integrations, accounting mapping and reports. A product template is made up of:

- a product factory record (Part 4.2A parameters);
- a BRE ruleset;
- a deviation matrix;
- a delegation-of-authority (DoA) matrix;
- a document checklist;
- a verification plan (FI, PD, technical, legal, RCU);
- a collateral type;
- a charges and GST profile;
- a KFS template;
- an accounting map;
- a collection strategy;
- a CIC reporting mapping;
- product-level analytics.

**Every product must define the following.** Store these as a versioned product specification under `docs/products/<code>.md`:

1. Borrower, co-borrower and beneficiary eligibility; and purpose with end-use verification.
2. Loan amount, tenure, pricing model (fixed/floating, benchmark plus spread), charges and penal charges.
3. Security and collateral requirements, LTV rules and margin calls.
4. Documentation and verification steps, and the KYC level.
5. Credit appraisal, scorecards, deviations and the sanctioning authority.
6. Offer presentation and disclosures (KFS, APR, MITC).
7. Sanction, agreement, eSign/eStamp and registration workflows.
8. Permitted disbursement routing: borrower account, seller/dealer/builder, or hospital/service provider where the regulations allow direct payment to the beneficiary [VERIFY for digital loans].
9. Repayment schedule, mandates and servicing events.
10. Delinquency, collection and recovery workflows, including legal remedies available for that collateral.
11. Closure, settlement, NOC and release of security within the regulatory timeline.
12. Product-specific regulatory reports and the CIC account type.
13. Profitability metrics: yield, cost of funds, credit cost, opex, verification cost per file, and RoA.

## 6.2 Products to template

Launch narrow first (Part 12), then expand.

| # | Product | Secured? | Key specifics the template must handle |
|---|---|---|---|
| 1 | **Personal Loan** (salaried / self-employed) | Unsecured | AA and bank-statement income, FOIR, employer category, bureau rules |
| 2 | **Payday / Short-tenure Loan** | Unsecured | Bullet repayment and APR display for tenors under 7 days; KFS consideration period (1 working day for tenor < 7 days [VERIFY]); cooling-off; strict affordability and repeat-borrowing limits; **heightened conduct risk, so the CCO must approve the template** |
| 3 | **Business / MSME Term Loan** | Either | GST and AA cash flows, Udyam, MCA data, banking analysis, CGTMSE/guarantee cover; prepayment-charge rule for floating-rate MSE loans |
| 4 | **Loan Against Property (LAP)** | Mortgage | Technical and legal verification, title search, valuation (2 valuers above threshold), equitable or registered mortgage, CERSAI, property insurance, SARFAESI eligibility, release of documents within 30 days |
| 5 | **Home Loan** (purchase / construction / renovation / plot + construction / balance transfer / top-up) | Mortgage | Construction-linked multi-tranche disbursement, PEMI vs full EMI, builder APF projects, PMAY-type subsidy handling, Sec 24(b)/80C certificates, HFC-specific regulation (RBI HFC Directions; NHB returns) |
| 6 | **Vehicle Loan** (new/used car, two-wheeler, CV, tractor, equipment) | Hypothecation | Dealer/manufacturer disbursement, Vahan RC check, hypothecation endorsement (Form 34) and termination (Form 35), insurance tracking, repossession under the RBI recovery norms, used-vehicle valuation |
| 7 | **Loan Against Securities (LAS): shares, bonds, MF units** | Pledge/lien | NSDL/CDSL pledge, unpledge and invocation APIs; MF lien through RTA/MF Central or depository; approved-securities list; haircut master; daily LTV and margin-call engine on bhavcopy/NAV feeds; 50% LTV and Group 1 rules for NBFCs (Credit Facilities Directions Ch VIII paras 104–106 [VERIFY]); IPO-funding cap |
| 8 | **Gold Loan** (and silver where offered) | Pledge | Assay capture (karat, gross/net weight), rate feed, slab-wise LTV across the full tenor, bullet-loan 12-month cap, quantity caps, auction workflow with reserve price and notice rules, same-day / 7-working-day release with compensation (Lending against Gold and Silver Collateral provisions, Credit Facilities Directions Ch IV [VERIFY paras 31–50]) |
| 9 | **Education Loan** | Either | Disbursement to institution, moratorium during course plus grace, co-borrower |
| 10 | **Consumer Durable / Point-of-sale Loan** | Unsecured | Merchant/dealer onboarding, subvention (buy-down fee), zero-cost EMI accounting, merchant refund |
| 11 | **Microfinance (JLG/SHG)** | Unsecured | Household income assessment, indebtedness cap, centre meetings, weekly/fortnightly collections, MFI calling hours 9:00–18:00, no prepayment penalty (NBFC-MFI Directions [VERIFY]) |
| 12 | **Supply-chain / Invoice / Channel Finance** | Either | Anchor programmes, invoice validation, TReDS. **Revolving-credit restriction on NBFCs under the August 2026 draft Credit Facilities amendment** [VERIFY final status before building any revolving line] |
| 13 | **Medical and Insurance Finance** | Either | Hospital/insurer institutional partnerships, direct payment to provider where permitted, pre-authorisation linkage, insurance-claim offset. **Feasibility pilot only** |
| 14 | **Legal Expense and Award-Enforcement Finance** | Either | Ordinary repayable loans only through the regulated lender. Non-recourse or litigation-funding cases are **referred out to specialist funders, not booked**. Requires a legal feasibility assessment first |
| 15 | **Resolution Finance** (linked to Equator settlements) | Either | Funds the borrower's settlement with an existing lender; disbursement direct to the creditor; settlement evidence from Equator; affordability test; measurement of qualification rates. **Pilot** |
| 16 | **Debt Reset / Consolidation** | Either | Rigorous affordability and debt-closure model before refinancing stressed borrowers; direct payoff to existing lenders; no evergreening of the lender's own NPAs (Resolution of Stressed Assets Directions [VERIFY]); restructuring flags. **Pilot** |
| 17 | **Co-lending products** | Any | Partner share (minimum 10% retention by each lender), blended rate, escrow, partner share booked within 15 days, borrower-level classification sync (Part 7, M11) |
| 18 | **Loans to entities / Term lending to NBFCs and corporates** | Either | Covenants, security cover, ratings, sanction terms, CRILC reporting |
| 19 | **Staff loans** | Either | Payroll deduction, perquisite valuation report |

**Products 13–16 are proposed products.** For each, produce a feasibility note before building any workflow:

- legal permissibility under the current RBI Directions and other law;
- the commercial model;
- risks;
- a pilot design.

Do not assume viability.

---

# PART 7 — FUNCTIONAL MODULE SPECIFICATION

Each module below is a domain module in the modular monolith. Each one owns its tables and publishes events. Build each one only after its specification is approved (Part 11).

## M1. Organisation, masters and calendar

- Tenant → legal entity → zone → region → branch → hub hierarchy, with GSTIN per state and cost centres.
- Holiday calendars (national, state, branch) and working-day rules for due-date shifting: same day, next or previous working day.
- Business-date management.
- Master data:
  - pincode and geography;
  - banks and IFSC;
  - occupations and industries (with RBI sector codes for reporting);
  - purpose codes;
  - CIC account types;
  - reason codes;
  - NACH return codes (configurable from the sponsor-bank specification; never hard-coded).
- Benchmark rate master (repo, MCLR or internal benchmark) with effective dates.

## M2. Lead, sourcing and partner management

- **Lead capture:** web, branch, field app, DSA portal, API (Udofin/LSPs), campaigns and bulk upload. Lead de-dupe; allocation by pincode, product and branch; TAT tracking; lead scoring.
- **DSA, connector and dealer master:** KYC, agreement, code, empanelment and renewal, blacklist, and quality scoring (early-default and RCU-hit rate by DSA).
- **Payout and commission engine:**
  - slab, volume and product-based payouts;
  - clawback on early foreclosure or default;
  - GST and TDS on payouts;
  - maker-checker;
  - payout statements.
- **Outsourcing register:** every DSA, LSP, recovery agency and vendor is recorded with due diligence, contract, risk rating and reviews, as required by the RBI (NBFC – Managing Risks in Outsourcing) Directions, 2025 [VERIFY].

## M3. Customer (CIF), KYC and AML

- **Single Customer Information File** across products and entities, where permitted. Individual and non-individual customers, with relationships to co-borrowers, guarantors, directors, partners and beneficial owners.
- **De-duplication:** internal match on PAN, Aadhaar reference/token, mobile, name + DOB, address and bank account; fuzzy matching; negative and blacklist checks; wilful-defaulter list check.
- **KYC per RBI (NBFC – Know Your Customer) Directions, 2025 (28 Nov 2025) and the amendment of 29 Dec 2025 [VERIFY]:**
  - CKYC search, download and upload. Upload within the prescribed period, and push updates when data changes. Build for CKYCRR 2.0 real-time APIs: search, download with OTP consent, upload.
  - Aadhaar offline e-KYC (XML/QR) and DigiLocker. Full Aadhaar e-KYC authentication only where the lender is a notified entity.
  - V-CIP (video KYC): live official, liveness, geo-tagging, recording stored in India, and the audit trail.
  - OVDs (officially valid documents); PAN verification and the PAN–Aadhaar link status.
  - Periodic updation by risk category, with reminders.
  - Risk categorisation (low, medium, high) with re-categorisation triggers.
- **Aadhaar Data Vault (UIDAI Circular 8 of 2025 [VERIFY]):**
  - If full Aadhaar numbers are ever stored, use a separate vault service with HSM-backed encryption and reference tokens.
  - Prefer OKYC/DigiLocker flows that avoid storing them.
  - Never log Aadhaar, PAN or OTP.
- **AML/CFT:**
  - sanctions and UN list screening (UNSC, UAPA lists), PEP screening;
  - transaction monitoring rules;
  - alert management;
  - FIU-IND reporting: STR within 7 working days of the suspicion conclusion; CTR/CCR/NTR monthly [VERIFY under the PML Rules].
  - record retention of 5 years under PMLA §12.

## M4. Loan Origination (LOS)

1. **Application capture:**
   - Product-specific dynamic forms built from the product template.
   - Applicant, co-applicants and guarantors; income, employment and business details; bank details; references.
   - Save-and-resume.
   - Pre-fill from KYC, bureau, AA, GST and MCA data so nothing is entered twice.
   - Mobile-friendly assisted mode for the field app.
2. **Consent management:**
   - Purpose-specific consent for each data pull and each data share: bureau, AA, CKYC, DigiLocker, sharing with co-lender, sharing with LSP.
   - Record the exact notice/consent text version, language, timestamp, channel, IP/device and the artefact ID.
   - Withdrawal handling.
3. **Data pulls (adapters, Part 9):**
   - Bureau: multi-bureau, with soft/hard enquiry distinction and consolidated tradeline view.
   - Account Aggregator: FIU consent flow; ReBIT schema version-aware parsing.
   - Bank-statement analyser; GST returns; ITR/AIS; EPFO/UAN; MCA; Udyam; Vahan; land records; eCourts; CERSAI.
4. **BRE and scorecards:**
   - Versioned, effective-dated decision tables and graphs.
   - Simulation and back-testing on historical files.
   - Explainable outputs with every rule hit logged.
   - Champion/challenger.
   - Policy parameters editable by credit-policy users under maker-checker.
5. **Fraud and risk checks:**
   - RCU sampling by rule.
   - Document tamper and AI-generated-document detection.
   - Face match against KYC photo.
   - Velocity checks; device and geo checks for field capture.
   - Negative-area pincodes.
   - EWS and red-flag indicators per the Fraud Risk Management Directions [VERIFY 31 Jul 2026 version].
6. **Verification management:**
   - Field investigation (residence and office), personal discussion, technical valuation, legal title search and vetting, RCU.
   - Vendor allocation by rule.
   - Mobile reports with geo-tag and photos.
   - TAT and SLA; vendor billing and quality scoring.
7. **Deviations and delegation of authority:**
   - Deviation matrix by amount × product × deviation type × LTV/FOIR × risk grade.
   - Routes the file to the right sanctioning authority (a hierarchical committee where needed).
   - Every approval records the authority, the limit it used and the reasons.
8. **Credit Appraisal Memo (CAM):**
   - Template-driven CAM covering applicant profile, income and cash-flow analysis, banking summary, bureau summary, eligibility (FOIR/LTV/DSCR), collateral, risk assessment, deviations, terms and conditions, and recommendation.
   - **AI-assisted narrative drafting** with source citations to the underlying documents and data. It is editable and always reviewed by a human. The final CAM is versioned and locked at sanction.
9. **Sanction and offer:**
   - Sanction letter.
   - **KFS with APR** generated by the KFS engine. Show all charges and the repayment schedule. Use the standard RBI format and the borrower's language.
   - Consideration period before execution: 3 working days for tenor ≥ 7 days, 1 working day for tenor < 7 days [VERIFY RBC para 29 / Annex I].
   - MITC; co-lending blended rate disclosure; recovery-agent and grievance-officer details.
   - Charges not disclosed in the KFS cannot be levied without explicit consent; enforce this in the charges engine.
10. **Documentation and execution:**
    - Document checklist by product.
    - Loan agreement, sanction acceptance, guarantee deed, DP note, hypothecation deed, MoD/mortgage deed workflow, end-use undertaking.
    - eSign: Aadhaar OTP eSign or DSC.
    - eStamp and NeSL Digital Document Execution (DDE).
    - Physical signing path for documents the IT Act First Schedule excludes from electronic execution, such as instruments creating interests in immovable property.
    - Store signing evidence: provider transaction ID, certificate, signed hash, timestamp, signer identity and IP.
    - Automatic delivery of digitally signed documents to the borrower's verified email or phone.
    - **OTC/PDD tracking:** deferral approval, ageing and escalation.
11. **Disbursement:**
    - Disbursement memo with pre-disbursement conditions checklist.
    - Penny-drop name match on the beneficiary account.
    - Multi-tranche disbursement with stage/inspection reports.
    - Deductions at disbursement (fees, GST, insurance, BT payoff) shown transparently.
    - Payout through the bank API or payout provider, with UTR capture.
    - **Interest starts from the actual date of disbursement or cheque handover, never from sanction or agreement date** (Miscellaneous Supervisory Directions, 2026, para 7 [VERIFY]).
    - No EMI on undisbursed amounts.
    - Cooling-off period handling for digital loans.
12. **Hand-off to LMS:** atomic loan-account creation with the schedule, opening GL entries, mandate link and welcome kit. For LOS-only tenants, use an export API to an external LMS.

## M5. Collateral management

- **Collateral types:** residential, commercial and industrial property; vehicles; gold and silver; listed shares and bonds; MF units; FDs and deposits; book debts and receivables; plant and machinery; guarantees (personal, corporate, CGTMSE/CGFMU-type).
- **Collateral lifecycle:**
  - acquisition;
  - ownership verification;
  - valuation and periodic revaluation;
  - charge creation (mortgage, hypothecation, pledge, lien);
  - **CERSAI registration within the statutory period** [VERIFY: 30 days];
  - insurance with lender endorsement and renewal tracking;
  - custody (vault/storage register for original title documents and gold packets, with dual control);
  - substitution, partial release, invocation and sale;
  - final release.
- **LTV monitoring:** real-time for securities, gold-price-linked for gold, periodic for property. Margin-call workflow with cure period and auto-invocation rules (for example the 7-working-day cure for LAS [VERIFY]).
- **Release of documents:**
  - Return original documents and clear charges (CERSAI satisfaction, depository unpledge, RTO Form 35 trigger) within **30 days** of full repayment or settlement.
  - Compensation calculator of **₹5,000 per day** of delay attributable to the lender.
  - Lost-document procedure.
  - Gold: same day, and in any case within 7 working days.
  - (RBI (NBFC – Responsible Business Conduct) Directions, 2025, paras 35–41 [VERIFY].)

## M6. Loan Management / Servicing (LMS)

- **Loan account (360° view):** schedule, ledger, balances by component, DPD history, classification history, mandates, collateral, documents, communications, complaints, collections activity, legal cases.
- **Schedules:** all Part 4.2A options. Regenerate the schedule with a full audit trail and keep previous versions.
- **Accruals:** daily interest accrual; penal charges as **charges, never penal interest, never capitalised** (RBC para 30 [VERIFY]).
- **Floating-rate resets:**
  - benchmark change propagation;
  - borrower option to change EMI or tenure, or to switch to a fixed rate;
  - no negative amortisation;
  - quarterly statements and communication (RBC paras 31–32 [VERIFY]).
- **Repayments:**
  - all channels (Part M7);
  - allocation per the product's strategy;
  - excess and advance handling;
  - unapplied/suspense receipts with resolution workflow.
- **Part-prepayment and foreclosure:**
  - quote generation valid to a date;
  - choice between reducing EMI and reducing tenure;
  - **prepayment-charge engine** applying the RBI (Pre-payment Charges on Loans) Directions, 2025 (now RBC para 34) for loans sanctioned or renewed on or after 1 Jan 2026. Inputs: rate type, borrower type, purpose, NBFC layer and amount threshold. Disclose the charge in the KFS and sanction letter [VERIFY].
- **Restructuring and rescheduling:**
  - per the RBI (NBFC – Resolution of Stressed Assets) Directions, 2025;
  - restructuring flag;
  - asset-classification impact: no upgrade merely because of rescheduling;
  - specified-period monitoring;
  - resolution-plan approval workflow.
- **Moratorium and payment holiday** under policy.
- **Other loan changes:** top-up; balance-transfer-in (payoff to the other lender); balance-transfer-out (foreclosure letter); tenure and EMI changes; due-date change; mandate change; co-borrower addition or removal (with re-KYC).
- **Charges engine:**
  - all fees with GST;
  - waivers within the delegated authority;
  - reversal with mandatory reason.
- **Service requests:** catalogue with SLA: statement of account, repayment schedule, interest certificate (provisional and final for Sec 24(b)/80C), foreclosure letter, NOC, list of documents, document retrieval, contact-detail change.
- **Closure:**
  - NOC generation;
  - charge-release triggers;
  - document-release SLA (M5);
  - CIC closure reporting;
  - excess refund.
- **Write-off:** technical write-off and full write-off with approval matrix; post-write-off recovery ledger.
- **Loan boarding/migration tool:**
  - Import active loans from legacy systems with their history and opening balances.
  - Reconcile principal outstanding, overdue, accrued and DPD against the legacy system before go-live.
  - Produce reconciliation sign-off reports.

## M7. Payments, mandates and reconciliation

- **Mandates:**
  - eNACH (net banking, debit card, Aadhaar);
  - physical NACH;
  - UPI AutoPay (note the AFA threshold for recurring debits [VERIFY applicability to EMIs]).
  - Mandate lifecycle covers registration, amendment, suspension, revocation and expiry. Map each mandate to its UMRN.
- **Presentation engine:**
  - debit file or API generation per sponsor bank, with T-1 cut-off rules;
  - re-presentation policy with minimum gaps;
  - bounce processing with configurable return-code master;
  - bounce charges with GST rules and borrower notification.
- **Collection channels:**
  - UPI intent, QR and collect;
  - payment links;
  - **virtual accounts per loan** (VAN/VPA) settling into the lender's own account;
  - Bharat Connect (BBPS) biller integration for loan repayment;
  - branch cash and cheque with deposit tracking;
  - field digital receipts;
  - NEFT/RTGS/IMPS credits with auto-matching.
- **Payment gateways:** Razorpay, Cashfree, PayU and Juspay behind one `PaymentGateway` interface.
  - **Stripe and PayPal:** keep the adapter interfaces you requested, but research shows Stripe is invite-only in India and PayPal has exited domestic Indian payments. Use them only for cross-border or SaaS-subscription billing, not domestic EMI collection. Record this decision in an ADR.
- **Disbursement rails:** bank corporate APIs (ICICI, HDFC, Axis, Yes, IDFC First and others) and payout providers (RazorpayX, Cashfree Payouts), with maker-checker, beneficiary validation, duplicate-payment prevention and UTR reconciliation.
- **Reconciliation:**
  - Three-way: provider/bank statement ↔ payment record ↔ loan ledger.
  - Auto-match rules, exception queue, suspense ageing.
  - **Never treat an API "success" response as final without settlement confirmation.**
  - Daily reconciliation with each sponsor bank, gateway, LSP and co-lender.

## M8. Collections (pre-due to 90+ DPD)

- **Segmentation and strategy:**
  - risk and propensity scoring;
  - pre-due nudges;
  - bucket-wise strategies (X, 1–30, 31–60, 61–90, NPA);
  - champion/challenger.
  - DPD changes in COB automatically trigger strategy actions, so flags always lead to action.
- **Allocation:** rule-based allocation to digital channels, telecallers, field staff and agencies by pincode, bucket, product, ticket size and performance. Includes re-allocation and capacity limits.
- **Contact channels:** SMS (TRAI DLT-registered templates and headers), WhatsApp Business (Meta Cloud API templates), email, IVR/voicebot, predictive dialer, field visits.
- **Contact-policy guard-rails enforced by the system:**
  - Calls only between 08:00 and 19:00 (09:00–18:00 for microfinance).
  - Frequency caps.
  - No contact with unrelated third parties.
  - Language and respect rules.
  - Record grievance-officer details in every recovery communication.
- **Recovery-agent amendments of 6 Aug 2026 (effective 1 Jan 2027) [VERIFY]:**
  - **record every recovery call** (inbound and outbound), tell the borrower it is recorded, and keep recordings at least 6 months;
  - **IIBF debt-recovery-agent certificate register** for every agent;
  - tell the borrower the assigned agency before visits;
  - visits only after the required failed contact attempts.
- **Field collections app:**
  - offline mode;
  - geo-tagged visits and photos;
  - PTP capture;
  - digital receipts only, or cash receipts with per-agent cash limits and same-day deposit tracking;
  - route planning;
  - panic/safety features.
- **PTP and dispositions:** standard disposition codes, PTP tracking, broken-PTP escalation, skip-tracing (lawful sources only).
- **Agency management:** empanelment, due diligence, agreements, agent IDs and authorisation letters, publication of agency lists on the lender website, performance and commission, audits.
- **AI in collections (governed):**
  - voicebot reminders with disclosure that it is AI;
  - next-best-action;
  - call-quality scoring;
  - sentiment detection;
  - automated QA against conduct rules.
  - **AI never threatens, never misrepresents, and never agrees binding settlements without human approval.**
- **Borrower communications at default:** SMS/email intimation before reporting default to CICs, as the CIR Directions require [VERIFY para 34].

## M9. Recovery and legal

- **Legal case management:** case master, advocate empanelment and fees, hearing calendar, eCourts CNR sync, documents and orders, cost tracking, outcomes.
- **Statutory workflows with timelines and templates:**
  - **Sec 138 NI Act / Sec 25 PSS Act:** cheque or mandate dishonour → demand notice within 30 days → 15-day wait → complaint within the limitation period.
  - **SARFAESI 2002:** eligibility gate (for NBFCs, asset size ≥ ₹100 crore and secured debt ≥ ₹20 lakh) → NPA check → 13(2) notice (60 days) → representation handling within the prescribed time → 13(4) possession notice and publication → Sec 14 CMM/DM application → possession → valuation → sale notice (Rule 8(6)/9) → e-auction → sale certificate → surplus refund.
  - **Arbitration and conciliation through Equator Resolution:** referral, notice, appointment, hearings, award, enforcement (Sec 36).
  - **Lok Adalat and pre-litigation settlement.**
  - **IBC:** NeSL Information Utility record-of-default filing; claims in CIRP/liquidation; personal-guarantor proceedings.
  - **DRT/civil suits and execution.**
  - **Wilful defaulter and large defaulter identification and reporting:** RBI (NBFC – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 [VERIFY], with identification committee, show-cause, review committee and reporting to CICs.
- **Repossession and auction (vehicles, equipment, gold):**
  - pre-repossession notice;
  - repossession kit and evidence;
  - inventory at yard;
  - valuation;
  - redemption window;
  - auction with reserve price;
  - sale proceeds allocation;
  - surplus refund;
  - deficiency recovery.
- **Settlement / OTS / compromise:**
  - NPV-based settlement calculator;
  - board-approved policy parameters;
  - approval matrix (with the restrictions on settlement with wilful defaulters or fraud cases [VERIFY]);
  - settlement letter;
  - payment plan tracking;
  - **settlement closure must report "settled" correctly to CICs.**
- **Write-off and post-write-off recovery** with accounting (M10).

## M10. Accounting, finance and treasury (double-entry core)

Treat Tally Prime, SAP and Zoho Books as integration and export targets. **They do not replace Finbyx's own books.** Finbyx must be able to run the lender's books end to end with no external accounting software.

1. **Chart of accounts:**
   - multi-entity;
   - Schedule III / Ind AS-aligned default CoA templates for NBFCs and HFCs;
   - an alternative template for non-Ind AS (Indian GAAP) entities;
   - cost centres and branch dimensions.
2. **Ledger engine:**
   - **append-only journal**;
   - every entry balanced (the database enforces zero-sum per journal);
   - corrections only by reversal plus re-posting;
   - a business date and a posting date on every entry;
   - immutable audit;
   - period locks;
   - materialised balances;
   - trial balance at any date.
3. **Sub-ledgers:**
   - loans (by component);
   - receivables and payables (vendors, DSAs, agencies);
   - borrowings;
   - fixed assets (basic register and depreciation, or integration);
   - bank;
   - GST;
   - TDS;
   - suspense.
   - **Continuous sub-ledger-to-GL reconciliation with break alerts.**
4. **Event-driven accounting templates:** every loan, payment and collection event maps through configurable accounting rules to journal entries. Re-use the Fineract mapping keys and extend them for EIR, ECL, IRACP, GST, TDS, co-lending and DA.
5. **Ind AS 109:**
   - EIR calculation at origination and on modification;
   - amortisation of fees and costs;
   - staging;
   - ECL model plug-in (PD/LGD/EAD from the tenant's model, or a simple provision-matrix default);
   - Stage 3 interest on net carrying amount;
   - write-off;
   - modification gain/loss;
   - parallel **IRACP** with income derecognition on NPA, standard-asset provisioning by layer, and sub-standard, doubtful and loss provisioning (RBI (NBFC – IRACP) Directions, 2025 [VERIFY paras]);
   - Impairment Reserve appropriation.
   - **For banks:** the RBI (Commercial Banks – Asset Classification, Provisioning and Income Recognition) Directions, 2026, effective 1 Apr 2027, with ECL stages and floors [VERIFY].
6. **Taxes:**
   - GST invoices and credit notes for fee income, with HSN/SAC and place of supply;
   - GSTR-1 data extract;
   - e-invoicing **only if applicable** (check the financial-services exemption [VERIFY]);
   - TDS on vendor/DSA payments with 26Q/24Q extracts;
   - TDS receivable on interest.
7. **Bank and treasury:**
   - bank accounts master;
   - automated bank reconciliation (statement import, H2H and API feeds);
   - cash and vault management for branches;
   - fund transfers between accounts with maker-checker.
8. **Borrowings and liabilities management** (an NBFC's funding side):
   - term loans from banks, NCDs, CPs, ECBs, sub-debt, inter-corporate deposits, securitisation liabilities;
   - repayment and interest schedules, accruals, covenants, security cover and asset-cover certificates;
   - drawdown and repayment workflow;
   - lender-wise MIS;
   - book-debt hypothecation statements.
9. **Month-end and year-end close:**
   - close checklist;
   - accrual and provision runs;
   - reconciliations;
   - lock;
   - financial statements (Balance Sheet, P&L, Cash Flow) per the RBI (NBFC – Financial Statements: Presentation and Disclosures) Directions, 2025 [VERIFY] and Schedule III Division III;
   - notes-to-accounts data packs (NPA movement, restructured accounts, sectoral exposure and similar).
10. **Accounting integrations:**
    - **TallyPrime** (7.x supports native JSON import/export; XML over HTTP also supported): through a **local connector agent** on the client's Tally machine, because Tally has no built-in API authentication. Push vouchers, ledgers and masters; reconcile.
    - **SAP S/4HANA** (OData Journal Entry APIs) and SAP Business One (Service Layer).
    - **Zoho Books.**
    - Configurable export formats (Excel/CSV/XML/JSON) for any other system.

## M11. Co-lending, direct assignment and securitisation

- **Co-lending:** RBI Co-Lending Arrangements Directions, 2025 (6 Aug 2025, effective 1 Jan 2026), now within the RBI (NBFC – Transfer and Distribution of Credit Risk) Directions, 2025 [VERIFY]. The engine must handle:
  - partner master and agreements;
  - minimum 10% retention by each lender;
  - partner share booked within 15 calendar days, otherwise it stays with the originator;
  - escrow for all flows;
  - blended rate to the borrower;
  - interest split by each partner's hurdle rate;
  - **borrower-level SMA/NPA sync across partners by the next working day**;
  - each lender's own CIC reporting;
  - DLG only by the originator, capped at 5%;
  - co-lending disclosures in the KFS;
  - partner reconciliation and servicer reports.
- **Direct assignment and securitisation** (RBI (NBFC – Securitisation Transactions) Directions, 2025 and the transfer provisions [VERIFY]):
  - pool selection with eligibility filters;
  - MHP and MRR checks;
  - pool tagging;
  - sale accounting (de-recognition tests under Ind AS 109);
  - servicing of sold pools;
  - collection waterfalls;
  - investor and trustee reports;
  - buy-back and clean-up.

## M12. Risk management

- **Credit risk:**
  - portfolio quality: vintage curves, roll rates, flow rates, PAR/DPD buckets;
  - concentration by borrower, group, sector, geography and product, against the RBI (NBFC – Concentration Risk Management) Directions, 2025 limits and Board limits [VERIFY];
  - large-exposure tracking;
  - EWS (bureau refresh triggers, bounce patterns, GST-filing gaps, adverse news).
- **Liquidity and ALM:**
  - structural liquidity statement and interest-rate sensitivity buckets;
  - LCR inputs where applicable;
  - stock ratios;
  - behavioural assumptions;
  - stress tests;
  - against the RBI (NBFC – Asset Liability Management) Directions, 2025 [VERIFY].
- **Capital:** CRAR, Tier 1/Tier 2 and risk-weighted assets per the RBI (NBFC – Prudential Norms on Capital Adequacy) Directions, 2025 [VERIFY]; leverage.
- **ICAAP data mart:** inputs for credit, concentration, operational, market/IRRBB, liquidity, reputational, strategic, ESG and cyber risk assessments; stress scenarios; RAG (traffic-light) indicators against the Risk Appetite Statement.
- **Operational risk:**
  - loss-event database;
  - RCSA (risk and control self-assessment);
  - KRIs (key risk indicators);
  - aligned with the RBI Guidance Note on Operational Risk Management and Operational Resilience [VERIFY 2025 version].
- **Fraud risk management:**
  - EWS/RFA framework;
  - fraud case lifecycle with a show-cause notice and reasoned order before classification;
  - FMR reporting within the regulatory timeline;
  - per the **RBI (NBFC – Fraud Risk Management) Directions, 2026 (31 Jul 2026)** [VERIFY applicability threshold and paras].
- **Model risk:** inventory of all scorecards, ECL, BRE and AI models, with owner, validation date, tier, performance monitoring and change log, aligned to the RBI draft Guidance on Model Risk Management (June 2026) [VERIFY final status] and the FREE-AI framework (Aug 2025).
- Basel/BCBS concepts are used **as reference methodology only** (for example PD/LGD/EAD, RWA, IRRBB, BCBS 239 data-aggregation principles). RBI Directions prevail for NBFCs.

## M13. Regulatory reporting

All returns are generated as **code, not ad-hoc BI**. Each return has:

- a versioned specification;
- validation rules;
- cell-level lineage back to GL and loan data;
- maker-checker;
- CCO/authorised-signatory certification;
- a submission log;
- an evidence archive.

| Return / report | Notes |
|---|---|
| **CIC data submission** (TransUnion CIBIL, Experian, Equifax, CRIF High Mark) in the Uniform Credit Reporting Format (consumer, commercial, MFI) | Frequency per the RBI (NBFC – Credit Information Reporting) Directions, 2025 as amended. Research indicates reference dates of the 9th, 16th and 23rd (incremental, within 4 days) plus month-end (full file, by the 5th), from 1 Jul 2026 [VERIFY]. Rejection rework within 7 days; correction-request tracking with the ₹100/day compensation clock; borrower intimation before default reporting |
| **CRILC** | Large-credit reporting where applicable [VERIFY NBFC layer applicability] |
| **CIMS / XBRL returns** | DNBS series (financial, prudential, ALM (DNBS4A/4B), sectoral, branch info, statutory auditor certificate and others), per the RBI (NBFC – Supervisory Returns) Directions, 2026 (31 Jul 2026) [VERIFY list, periodicity, due dates] |
| **Fraud Monitoring Returns (FMR)** | Within the regulatory timeline after classification |
| **FIU-IND** | STR, CTR, CCR, NTR (FINnet 2.0 formats) |
| **DLA/LSP reporting on CIMS** | Register and certification |
| **NHB returns** (HFCs) | As applicable |
| **Co-lending, DA and securitisation disclosures** | As applicable |
| **Board and committee packs** | Audit, Risk, ALCO, IT Strategy and Customer Service committees |
| **Statutory and tax** | GST, TDS, Form 26AS reconciliation |

## M14. Compliance module (embedded) and LawDocsComply bridge

- **Mode switch per tenant or group:**
  - (a) embedded compliance inside Finbyx;
  - (b) LawDocsComply as the GRC system, with Finbyx pushing evidence and pulling obligations;
  - (c) group-level LawDocsComply covering several Finbyx entities.
- **Regulatory register:**
  - dated, versioned instrument records;
  - paragraph-level obligations;
  - applicability per entity (layer, asset size, products, deposit-taking status, customer interface);
  - responsible function;
  - system control;
  - evidence;
  - test case;
  - status;
  - unresolved questions.
- Start the register with the RBI 28 Nov 2025 consolidated Directions and the 31 Jul 2026 Supervision Directions, then keep it current through a **regulatory change management** workflow (impact assessment across products, configurations, templates, workflows and tests).
- **Compliance calendar:** returns, Board/committee reviews, policy reviews, audits, VAPT, DR drills, certifications.
- **Automated control tests that run inside Finbyx and produce evidence.** Examples:
  - KFS issued before execution;
  - no penal interest;
  - prepayment charges suppressed where barred;
  - document release within 30 days;
  - recovery calls within permitted hours;
  - CKYC uploads on time;
  - CIC files on time;
  - NPA tagging correct;
  - interest from disbursement date.
- **Policy library** with Board approval dates, and **product-approval workflow** (new-product evaluation by the Compliance Function under the RBI (NBFC – Compliance Function) Directions, 2026 [VERIFY]).

## M15. Customer service, grievance redressal and Equator

- **Omnichannel complaints:** branch, phone, email, web portal, Udofin/LSP API, social media, RBI CMS references.
- **Complaint handling:**
  - unique reference number;
  - acknowledgement;
  - classification (AI-assisted, human-confirmed);
  - routing to the Grievance Redressal Officer or Nodal Officer;
  - SLA clocks;
  - communication history;
  - attachments;
  - root-cause tagging.
- **Internal Ombudsman (where applicable)** under the **RBI (NBFC – Internal Ombudsman) Directions, 2026 (14 Jan 2026)** [VERIFY]: automatic escalation of wholly or partly rejected complaints to the IO within the prescribed days, and the final response within 30 days. The complaint system must be fully automated.
- **RBI Integrated Ombudsman Scheme, 2026** (effective 1 Jul 2026) [VERIFY]:
  - display the Principal Nodal Officer's details;
  - give the borrower escalation information when no reply arrives within 30 days or they are dissatisfied;
  - track RBI Ombudsman references with response deadlines.
- **Equator Resolution referral:**
  - when a dispute remains unresolved and both parties consent, or when the contract provides for ODR/arbitration;
  - create the Equator case through the API with the agreed data set;
  - the borrower accesses mediation or arbitration through a secure link, with no separate app;
  - outcomes flow back to the loan and legal module.
- **AI support assistant** for staff and the optional borrower portal:
  - answers only from approved knowledge sources and the customer's own data;
  - discloses that it is AI;
  - never invents regulatory rights;
  - never rejects complaints;
  - always offers a human.
- **Feedback:**
  - CSAT/NPS after service events and closure;
  - feedback analytics;
  - feedback obligations under the RBC Second Amendment on sales and marketing (effective 1 Jan 2027 [VERIFY]).

## M16. Document management system (DMS)

- Private, encrypted object storage with short-lived signed URLs.
- Document types and metadata; versions; hashes (SHA-256) for integrity; verification status; uploader; timestamps.
- Retention schedule by document class:
  - PMLA: 5 years after relationship end;
  - loan documents: Board policy;
  - legal hold.
- Access logging. Watermarking on view and download.
- OCR and AI classification with human verification.
- **Signed documents** (sanction letter, KFS, application form, CAM, guarantee agreement, loan agreement, KYC, mortgage and hypothecation documents) are viewable after eSign, together with their signing evidence.
- **A document is never marked "signed" because a workflow stage was reached.**
- Physical document custody register (file barcode, location, movement and retrieval requests).

## M17. Reports, MIS, analytics and dashboards

- **Report catalogue (200+ standard reports over time).** Each report has filters, saved views, scheduling, and export to Excel/CSV/PDF:
  - sourcing funnel and TAT;
  - sanction/disbursement registers;
  - portfolio cuts;
  - DPD/SMA/NPA movement;
  - collections efficiency;
  - roll rates;
  - legal status;
  - profitability by product, branch and DSA;
  - yield and cost of funds;
  - ECL/IRACP;
  - ALM;
  - concentration;
  - compliance status;
  - grievance analytics;
  - unit economics (cost per file for verification, bureau, eSign, messaging and cloud).
- **Dashboards per workspace and for the Board.** Self-service BI through an embedded semantic layer, with row-level tenant/branch security.
- **Natural-language analytics copilot** over governed, read-only data, which cites the query it ran.

## M18. Communications and marketing

- **Template management:** multilingual (English, Hindi and major regional languages), versioned, approval workflow, DLT template IDs.
- **Channels:** SMS, WhatsApp, email, push (borrower portal/app) and letters (print and dispatch with India Post tracking for legal notices).
- **Campaigns:** cross-sell, top-up, renewals.
- **Consent, preference and DND management**, honouring the **RBC Second Amendment Directions, 2026 (Chapter IIIA on sales and marketing, effective 1 Jan 2027)** [VERIFY]:
  - explicit consent with "No" as the default;
  - ban on listed dark patterns;
  - no compulsory bundling;
  - permitted contact hours;
  - consent records retained.

## M19. Administration, configuration and workflow

- **Users and roles:** RBAC plus ABAC (attribute-based: amount limits, branch scope, product scope); segregation-of-duties checks; maker-checker per permission.
- **Access security:** MFA; session policies; IP allow-lists; device binding for the field app; delegation and leave substitution; break-glass access with audit.
- **Visual workflow designer for tenant workflows**, within guard-rails, with versioned deployment.
- **Configurable forms, fields, checklists, templates and notifications.**
- **Feature flags; integration credential vault** (per tenant, encrypted, rotation reminders).
- **Audit trail:**
  - immutable, tamper-evident (hash-chained);
  - who, what, when, where, before/after values;
  - searchable by auditors;
  - in line with the audit-trail and logging requirements of the RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 (31 Jul 2026) [VERIFY paras].

## M20. AI layer (governed)

**Use AI for:**

- document classification and extraction (with verification);
- application completeness checks;
- CAM narrative drafting;
- bank-statement and GST insight summaries;
- complaint classification and routing;
- staff copilot over policies and SOPs (RAG);
- collections QA and next-best-action;
- report drafting;
- natural-language MIS;
- anomaly detection in reconciliation;
- regulatory-change summarisation feeding M14.

**AI must never:**

- independently approve, reject or price a loan;
- execute financial transactions;
- alter contractual terms;
- bypass authorisation;
- reject a complaint;
- make binding legal decisions;
- send unapproved borrower communications.

All consequential actions pass deterministic rules, authorisation checks and human approval.

**Governance aligned with the RBI FREE-AI framework (Aug 2025) and model-risk guidance:**

- AI model inventory;
- prompt and output logging (PII-redacted);
- explainability records;
- bias testing for any credit-adjacent model;
- AI disclosure to customers;
- an India-region inference endpoint (for example AWS Bedrock in ap-south-1) or approved providers with a data-processing agreement.

**MCP server (later phase):** a read-only, tenant-scoped MCP server exposing loan-360, DPD and ledger queries to internal AI agents under RLS-scoped tokens.

## M21. Integration hub and public APIs

- An API gateway with an OpenAPI 3.1 catalogue.
- OAuth2 client credentials and mTLS for partners.
- Rate limits.
- Webhooks with signatures and retries.
- A developer sandbox per tenant.
- Event streaming (outbox → queue/stream).
- Bulk file interfaces (SFTP) for banks and CICs.
- An integration monitor with health, latency, error rates and per-call cost.

## M22. Field application

Evaluate Expo React Native vs a PWA. Recommend Expo if offline mode, camera, GPS and device binding are needed (they are).

**Scope:**

- assisted onboarding and KYC capture;
- document scan with edge detection and compression;
- FI/PD/valuation reports;
- collections;
- receipts;
- route plan;
- offline sync with conflict resolution.

**Device controls:**

- request only necessary permissions at the moment they are needed;
- no access to contacts, SMS or call logs;
- remote wipe of app data.

## M23. Borrower self-service portal (optional per tenant)

A lean, mobile-first web portal for lenders that do not use Udofin:

- loan summary;
- schedule;
- payments;
- statements and certificates;
- service requests;
- complaints with escalation path;
- consent and privacy dashboard (view, withdraw, data-rights requests);
- a "books of account" view of the borrower's payments and charges, for transparency.

---

# PART 8 — REGULATORY BASELINE (STARTING REGISTER — VERIFY BEFORE EACH MODULE)

## 8.1 Rules for handling regulation

Before implementing any regulated workflow:

1. Research the current authoritative source: rbi.org.in, the official gazette, MeitY, UIDAI, NPCI, CERSAI and NeSL.
2. Record in `docs/compliance/requirements-to-controls.md`:
   - instrument;
   - paragraph;
   - date;
   - applicability conditions;
   - responsible party (lender / LSP / Infrabyx / vendor);
   - system control;
   - evidence produced;
   - test case;
   - open questions.
3. Keep confirmed legal requirements separate from interpretations, recommendations and assumptions. Never claim regulatory compliance merely because a feature exists.
4. Never assume one obligation applies identically to every lender. Applicability depends on:
   - entity type (NBFC / HFC / UCB / SFB / commercial bank);
   - layer and asset size;
   - deposit-taking status;
   - customer interface;
   - product;
   - channel (digital or physical).
5. RBI consolidated about 9,000 circulars into 244 entity-wise Master Directions on **28 November 2025**, and issued **64 Department of Supervision Directions on 31 July 2026**. Older circular references are legacy. Cite the new Directions, and keep the legacy reference only for traceability.

## 8.2 Starting register

All items need confirmation against the primary text.

| Area | Instrument (NBFC version; use the bank/UCB/HFC counterpart per tenant) | Software controls |
|---|---|---|
| Scale-based regulation | RBI (NBFC – Registration, Exemptions and Framework for Scale Based Regulation) Directions, 2025, as amended 2026 (Upper Layer threshold of ₹1 lakh crore assets; Unregistered Type I NBFC category) | Entity profile drives applicability of every rule |
| Digital lending | RBI (NBFC – Credit Facilities) Directions, 2025, Chapter III (paras 6–29: LSP, conduct, data, DLA reporting, DLG) | Direct disbursal and repayment; KFS; cooling-off ≥ 1 day; DLA/LSP lists; consent; India-only storage; DLG cap 5% |
| Gold and silver loans | Credit Facilities Directions, Chapter IV (paras 31–50) | LTV slabs, quantity caps, valuation, auction, release |
| Loans against securities | Credit Facilities Directions, Chapter VIII (paras 104–106) | 50% LTV, approved securities, margin calls, IPO-funding cap |
| Interest, KFS, penal charges, prepayment, resets, document release, recovery agents | RBI (NBFC – Responsible Business Conduct) Directions, 2025 (paras 22–24, 29 + Annex I, 30, 31–32, 34, 35–41, 89–100, 103); RBC Second Amendment 2026 (sales and marketing, effective 1 Jan 2027); recovery-agent amendment of 6 Aug 2026 (effective 1 Jan 2027) | KFS/APR engine; penal-charge rules; prepayment-charge engine; reset options; release SLA and ₹5,000/day compensation; contact-policy guard-rails; call recording; agent certification |
| Interest computation and FPC | RBI (NBFC – Miscellaneous Supervisory) Directions, 2026 (para 7) | Interest from actual disbursement; no full-month interest for part months; no advance-EMI-on-full-principal; no EMI on undisbursed amount; no undisclosed schedule change |
| IRACP | RBI (NBFC – Income Recognition, Asset Classification and Provisioning) Directions, 2025 (paras 18–19 day-end tagging; 22–25 upgrade rules; 32 doubtful; 34–35 Ind AS / Impairment Reserve; 38 income; 48/55/58 standard-asset provisions) | COB classification engine; borrower-level NPA; provisioning engine |
| Stressed assets | RBI (NBFC – Resolution of Stressed Assets) Directions, 2025 | Restructuring flags, resolution plans, compromise settlements, technical write-off |
| Credit risk and concentration | RBI (NBFC – Credit Risk Management) and (Concentration Risk Management) Directions, 2025 | Limits, exposure aggregation, large exposures |
| KYC/AML | RBI (NBFC – Know Your Customer) Directions, 2025, as amended 29 Dec 2025; PMLA 2002 and PML Rules 2005 | CKYC, V-CIP, periodic updation, screening, FIU-IND, 5-year retention |
| Credit information | RBI (NBFC – Credit Information Reporting) Directions, 2025 (paras 9, 10, 15, 34, 35), as amended (reporting dates from 1 Jul 2026) | UCRF files, rejection rework, borrower intimation, correction/compensation clock |
| Co-lending and loan transfers | RBI (NBFC – Transfer and Distribution of Credit Risk) Directions, 2025 (absorbing the Co-Lending Arrangements Directions of 6 Aug 2025) | M11 co-lending engine |
| Securitisation | RBI (NBFC – Securitisation Transactions) Directions, 2025 | MHP/MRR, pools, servicing |
| Outsourcing | RBI (NBFC – Managing Risks in Outsourcing) Directions, 2025 | Outsourcing register, due diligence, contracts, audit rights |
| Capital, ALM | RBI (NBFC – Prudential Norms on Capital Adequacy) and (Asset Liability Management) Directions, 2025 | M12 |
| Wilful defaulters | RBI (NBFC – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 | M9 workflow and reporting |
| Financial statements | RBI (NBFC – Financial Statements: Presentation and Disclosures) Directions, 2025 | M10 statements and disclosures |
| HFC | RBI (Housing Finance Companies) Directions, 2025, plus NHB requirements | HFC product rules and returns |
| Account Aggregator | RBI (NBFC – Account Aggregator) Directions, 2025; ReBIT specs v2.x | FIU integration |
| Cyber and IT | **RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 (31 Jul 2026)**, which repeal the 2023 IT Governance Master Direction | Audit trails, MFA for privileged access, VAPT (VA 6-monthly, PT annually for critical systems), incident reporting within 6 hours, BCP/DR drills, vendor source-code escrow, IT Strategy Committee reporting |
| Fraud | RBI (NBFC – Fraud Risk Management) Directions, 2026 (31 Jul 2026) | EWS/RFA, natural-justice process, FMR |
| Supervisory returns | RBI (NBFC – Supervisory Returns) Directions, 2026 (31 Jul 2026) | M13 returns |
| Compliance function | RBI (NBFC – Compliance Function) Directions, 2026 (31 Jul 2026) | M14 product approval, CCO certification |
| Grievances | RBI (NBFC – Internal Ombudsman) Directions, 2026 (14 Jan 2026); RB-Integrated Ombudsman Scheme, 2026 (effective 1 Jul 2026) | M15 |
| Bank ECL (bank tenants) | RBI (Commercial Banks – Asset Classification, Provisioning and Income Recognition) Directions, 2026 (effective 1 Apr 2027) | Bank ECL engine |
| Data protection | Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025 (notified Nov 2025; Consent Manager provisions from Nov 2026; most obligations from May 2027) | Notice and itemised consent, withdrawal, consent-manager integration, breach notice (Board within 72 hours), security safeguards, 1-year log retention, erasure when purpose ends unless law requires retention, data-principal rights within the prescribed time, retention-rules engine resolving conflicts with PMLA/RBI/CIC retention |
| Aadhaar | Aadhaar Act and Regulations; UIDAI Circular 8 of 2025 (Aadhaar Data Vault) | Vault, tokenisation, masking |
| Electronic records | Information Technology Act, 2000 (s.3A eSign, Second Schedule; First Schedule exclusions); state stamp Acts (e-stamping through SHCIL); NeSL DDE and IU under IBC s.215 | Signing evidence; physical paths for excluded instruments; stamp-duty by state |
| Recovery law | SARFAESI Act 2002 and Security Interest (Enforcement) Rules 2002 (NBFC eligibility: assets ≥ ₹100 crore and debt ≥ ₹20 lakh); NI Act s.138; Arbitration and Conciliation Act 1996; IBC 2016; Legal Services Authorities Act (Lok Adalat) | M9 workflows |
| Accounting | Ind AS 109, 107, 115, 24 and others; Schedule III Division III of the Companies Act, 2013; ICAI guidance | M10 |
| AI | RBI FREE-AI Framework (Aug 2025); draft Guidance on Model Risk Management (Jun 2026) | M20 governance |

---

# PART 9 — INTEGRATIONS (PROVIDER ADAPTERS)

## 9.1 Design rules

- Keep provider-specific operations behind domain interfaces, for example:
  - `KycProvider`, `BureauProvider`, `AccountAggregatorFIU`, `BankStatementAnalyser`;
  - `ESignProvider`, `EStampProvider`;
  - `MandateProvider`, `PaymentGateway`, `PayoutProvider`;
  - `DepositoryPledgeProvider`, `MfLienProvider`;
  - `NotificationProvider`, `AccountingSink`;
  - `LspConnector`, `OdrProvider`, `GrcSink`;
  - `StorageProvider`, `LlmProvider`.
- Do not try to make every infrastructure component interchangeable from day one.
- Build mock and sandbox adapters first. Clearly label mock/sandbox vs production in the UI, in logs and in config.
- For each adapter, document:
  - authentication;
  - request validation;
  - response mapping;
  - timeouts;
  - retries with idempotency;
  - duplicate handling;
  - error taxonomy;
  - reconciliation;
  - credential rotation;
  - cost per call (feeds the unit-economics reports).
- Do not assume every named provider offers an API or that access is automatically available. Verify current documentation, eligibility, commercial terms and authorisation requirements, and record them in `docs/integrations/register.md`.
- **I (the project owner) will procure and connect live credentials.** These include Surepass (already contacted, for PAN, Aadhaar OKYC, DigiLocker, CKYC, bank verification, multi-bureau, GST, MCA, Udyam, Vahan, face match, V-CIP, eSign/eStamp and other APIs), the bureaus, eSign/eStamp providers, NSDL/CDSL, payment gateways, sponsor banks and Tally/SAP. You build the adapters, contract tests and sandbox mocks.

## 9.2 Integration catalogue

| Category | Candidates to support (verify each) |
|---|---|
| KYC and identity | Surepass (primary), Signzy, IDfy, HyperVerge, Digio, Decentro; CKYCR (CERSAI / CKYCRR 2.0); DigiLocker; UIDAI OKYC; NSDL/UTI PAN; V-CIP |
| Credit bureaus | TransUnion CIBIL, Experian, Equifax, CRIF High Mark (pull APIs and UCRF submission) |
| Financial data | Account Aggregator through a TSP (Finvu, Setu, Perfios/Anumati, FinBox and others); bank-statement analysers (Perfios, FinBox, Scoreme); GSTN; ITR/AIS; EPFO; MCA; Udyam; ULI (RBIH Unified Lending Interface) where the tenant is onboarded |
| Collateral | NSDL and CDSL pledge/eLAS APIs; CAMS/KFintech/MF Central lien (verify current access terms); Vahan; CERSAI; state land records (through ULI or vendors); gold-rate feeds; valuer and legal-vendor portals |
| eSign and eStamp | Leegality, Digio, eMudhra, NSDL e-Gov eSign, Surepass; SHCIL e-stamping; NeSL DDE |
| Mandates and payments | NPCI eNACH through sponsor banks or aggregators (Razorpay, Cashfree, Digio, Decentro, PayU); UPI AutoPay; Bharat Connect (BBPS) through a BBPOU; virtual accounts (Razorpay Smart Collect, Cashfree, bank VANs); payouts (RazorpayX, Cashfree, bank corporate APIs); Stripe/PayPal adapters for cross-border/SaaS billing only |
| Communications | DLT-compliant SMS gateways; WhatsApp Business Cloud API; email (SES/SendGrid/Resend); push (FCM/APNs); IVR/dialer; India Post tracking |
| Accounting | TallyPrime (JSON/XML through a local connector); SAP S/4HANA, SAP B1; Zoho Books; generic CSV/Excel/XML |
| Legal | eCourts; Equator Resolution API; e-auction service providers |
| Ecosystem | Udofin (LSP connector), LawDocsComply (GRC sink), Equator (ODR), legacy LOS/LMS (migration) |

---

# PART 10 — TECHNOLOGY, ARCHITECTURE AND NON-FUNCTIONAL REQUIREMENTS

## 10.1 Recommended stack

Validate current versions in Phase 0. Propose changes through an ADR.

| Layer | Recommendation | Reason |
|---|---|---|
| Monorepo | pnpm workspaces + Turborepo; TypeScript strict | Shared types, contracts and design system |
| Internal web app (all workspaces) | Next.js 16 (App Router) + React 19 + TypeScript; shadcn/ui + Tailwind with design tokens; TanStack Query; **AG Grid** (or TanStack Table v9) for data-dense grids | Complex workflows, large tables, theming |
| Backend | Node.js LTS + TypeScript; **NestJS 11 modular monolith** (or Fastify with explicit modules), with strict domain boundaries; OpenAPI 3.1 via Zod schemas | Business rules, integrations, controlled access |
| Database | PostgreSQL 16+ (Supabase now; Amazon RDS/Aurora PostgreSQL later); **Drizzle ORM or Kysely** for SQL control; versioned SQL migrations | Relational, transactional ledger; portable |
| Money and maths | `NUMERIC` columns; `decimal.js`; property-based tests (fast-check) for schedule/allocation invariants | Paisa-exact accuracy |
| Workflow orchestration | **Temporal** (TypeScript SDK; Temporal Cloud has AWS Mumbai/Hyderabad regions, or self-host) for long-running sagas: origination, disbursement, mandate presentation and retries, legal timelines, COB orchestration. pg-boss or Graphile Worker for simple jobs | Durable, retry-safe, auditable workflows |
| Rules / BRE | **GoRules ZEN engine** (JDM decision tables/graphs; MIT licence; Node bindings) with versioned rules stored in Postgres and a business-user editor | Credit policy, pricing grids, deviations, eligibility |
| Events | Transactional outbox → queue/stream (start with Postgres-backed queue or Redis Streams; move to Amazon MSK/Redpanda + Debezium CDC on AWS) | Reliable integration events |
| Authentication | Supabase Auth now, **behind an OIDC abstraction**; Keycloak or Amazon Cognito later; SSO/SAML for bank tenants; MFA mandatory for staff | Portability |
| Authorisation | Server-side policy layer: RBAC + ABAC (Cedar or OpenFGA for hierarchy/amount limits) **plus Postgres Row-Level Security** as defence-in-depth for tenant/entity/branch isolation | Least privilege; Supabase must not be the only security boundary |
| Documents | S3-compatible private storage (Supabase Storage → Amazon S3) with SSE-KMS; docxtemplater/Handlebars templates → Gotenberg (HTML/DOCX → PDF) | Agreements, KFS, CAM, letters |
| Search | PostgreSQL FTS + pg_trgm first; OpenSearch later | Customer and loan search |
| Reporting/BI | Regulatory returns in code; Metabase or Apache Superset (embedded, with RLS) for MIS; Cube semantic layer optional | Self-service MIS |
| Observability | OpenTelemetry → Grafana (Loki/Tempo/Mimir) or AWS-native; Sentry; PII-scrubbing log processors; security audit events | Production support and traceability |
| Infrastructure | Docker; initial hosting on Railway (API and workers) + Supabase (DB/Auth/Storage), Mumbai region; later AWS ap-south-1 primary and ap-south-2 DR on ECS/EKS, provisioned with OpenTofu/Terraform or AWS CDK; KMS, CloudHSM (Aadhaar vault, signing keys), Secrets Manager, WAF | Data localisation, scalable, portable |
| Testing | Vitest/Jest, Testcontainers (Postgres), Playwright (E2E), Pact (contract tests with Udofin/partners), k6 (load), OWASP ZAP and Semgrep/CodeQL (security), Fineract differential harness | Release gates |
| Field app | Expo React Native + TypeScript (offline-first, SQLite + sync) | Field ops |

## 10.2 Architecture principles

These are mandatory. Principles 1–17 are carried over from the Udofin prompt, and 18–30 are added for a core-lending system.

1. Use a modular architecture with explicit domain boundaries. Start with a modular monolith, not microservices.
2. Define an owner for every important data entity.
3. Enforce tenant and legal-entity isolation in the API, the service layer and the database (RLS), and test it.
4. Apply least-privilege access control.
5. Validate all sensitive operations on trusted backend services. The browser and the mobile app never hold privileged keys.
6. Use database transactions for operations that must be atomic.
7. Make financial operations idempotent and safely retryable (idempotency keys stored and enforced).
8. Keep traceable state transitions for leads, applications, loans, payments, mandates, collateral, collections, legal cases and complaints. Use explicit state machines with allowed transitions, failure states, retries and human overrides. For example, an application must not move to "disbursed" just because it was sanctioned.
9. Record critical operations as immutable or tamper-evident (hash-chained) audit events.
10. Keep configuration separate from code.
11. Keep secrets outside source control.
12. Keep database migrations versioned and reviewed for locking, data loss, backward compatibility and rollback/forward recovery.
13. Use asynchronous processing for suitable long-running tasks.
14. Implement structured logging, monitoring, error handling and alerting, with **no Aadhaar, PAN, OTP, account numbers or sensitive personal data in logs.**
15. Document API contracts, data models and material architecture decisions (ADRs).
16. Avoid unnecessary duplication between web, field-app and backend.
17. Build reusable components only when their behaviour is clear.
18. **Single authoritative financial record.** The loan ledger and the GL are the only sources of financial truth. Balances are derived, never edited.
19. **No hard deletes of financial or regulatory data.** Use reversals, cancellations and legal-hold-aware retention.
20. **Business date ≠ system date.** Every financial posting carries a value date, a business date and a system timestamp.
21. **Back-dated transactions** replay deterministically from the affected date. Period locks block posting into closed periods, except through an authorised adjustment workflow.
22. **Duplicate prevention.** Prevent duplicate disbursements, duplicate receipt allocation and duplicate mandate presentation (unique constraints + idempotency + reconciliation).
23. **Reconcile provider records against internal records.** Never trust a successful API response alone.
24. **Regulation as configuration.** Regulatory parameters (classification days, provision rates, contact hours, cooling-off, KFS rules, prepayment rules) live in versioned, effective-dated rule packs with platform guard-rails and tests.
25. **Explainability.** Every credit decision, deviation approval, charge, waiver and classification stores the inputs, rule version and approver.
26. **Maker-checker** on every configurable sensitive action.
27. **Data localisation.** All production data, backups and logs stay in India.
28. **Privacy by design.** Consent lineage, purpose limitation, minimisation, masking in UI by role, and a retention engine.
29. **Scalability.** Design for at least 100 lender tenants, 10 million+ loan accounts and tens of millions of ledger entries a month, with partitioned tables (by tenant and date), read replicas for reporting, and horizontally scalable COB workers.
30. **Portability.** Containerised, environment-based config, storage and auth abstractions, IaC. Do not build an elaborate cloud-neutral platform before the product is validated.

## 10.3 Non-functional targets (initial — confirm in Phase 0)

| Area | Target |
|---|---|
| Availability (production) | 99.9% monthly for staff app and APIs; COB must not block branch operations |
| Latency | p95 < 300 ms for reads, < 800 ms for standard writes, excluding third-party calls |
| COB | 1 million active loans processed in < 60 minutes on reference infrastructure, with linear scale-out |
| RPO / RTO | Near-zero RPO for the ledger (synchronous replica / PITR); RTO ≤ 4 hours (tighten for Middle Layer+ per the Cyber Directions DR requirements [VERIFY]) |
| DR drills | Half-yearly for critical systems where the Cyber Directions require it; restore tests at least quarterly |
| Security | OWASP ASVS Level 2 baseline; VAPT before go-live and per the regulatory cadence; incident reporting runbook supporting 6-hour regulatory reporting |
| Accessibility | WCAG 2.2 AA for portals |
| Localisation | English + Hindi at launch; framework for regional languages; INR formatting (lakh/crore), DD-MM-YYYY |

## 10.4 Security and cyber controls (map to the 2026 Cyber Directions)

- **Encryption:** TLS 1.2+ (prefer 1.3) in transit; AES-256 at rest; field-level encryption for PAN, Aadhaar reference, bank account and DOB; KMS envelope keys per tenant; HSM for vault and signing keys.
- **Identity and access:**
  - MFA for all staff and privileged users;
  - privileged access management;
  - session timeouts;
  - IP and device restrictions;
  - quarterly access reviews (system-generated);
  - joiner-mover-leaver automation.
- **Application security:**
  - input validation (Zod);
  - output encoding;
  - CSRF protection;
  - rate limiting;
  - signed short-lived document URLs;
  - IDOR/BOLA tests on every endpoint;
  - webhook signature verification and replay protection;
  - file-upload scanning (antivirus, type and size checks).
- **Supply chain:**
  - SBOM;
  - dependency scanning;
  - signed builds;
  - pinned versions;
  - secret scanning in CI;
  - vendor source-code escrow readiness, since lenders will ask for it under the Cyber Directions.
- **Monitoring:**
  - SIEM-ready security audit stream;
  - anomaly alerts (bulk export, off-hours privileged access, mass status changes);
  - an incident response runbook with severity matrix and regulatory/CERT-In reporting templates.
- **Independent security review:** in each phase, try to break your own implementation, not merely confirm that it works. Test:
  - cross-tenant and cross-entity access;
  - cross-branch access;
  - privilege escalation;
  - insecure document links;
  - IDOR;
  - replayed requests;
  - webhook forgery;
  - mass assignment;
  - unauthorised admin actions;
  - maker-checker bypass;
  - back-dated posting into closed periods.

## 10.5 UI/UX principles for internal teams

- Clean, professional, non-cluttered, **data-dense without visual noise**.
- Role-based workspaces with:
  - **My Queue** (SLA-sorted);
  - global search (customer, loan, PAN-masked, mobile, application ID);
  - a 360° customer/loan view with tabs;
  - keyboard shortcuts for power users;
  - bulk actions with maker-checker;
  - saved filters;
  - export controls by permission;
  - inline explanations of why data is requested;
  - clear error messages and recovery steps;
  - timeline views of every account.
- **Theming and white-labelling** through design tokens (colours, typography, spacing, radius, logo, density). I must be able to change the look without code changes.
- Maximum automation:
  - pre-fill from data pulls;
  - auto-generated documents;
  - auto-allocation;
  - auto-reconciliation;
  - auto-reminders;
  - auto-escalation;
  - straight-through processing where rules allow, with human review where rules or regulation require it.
- **Consistent component library and Storybook. Every screen must have** empty, loading, error and permission-denied states.

---

# PART 11 — WORKING METHOD, GIT DISCIPLINE AND DEFINITION OF DONE

## 11.1 For each module or sub-module

Work through these steps in order:

1. Explain the business objective in plain English.
2. Identify assumptions and ask only material unresolved questions.
3. Research the relevant legal, provider and technical requirements, and update the regulatory register and integration register.
4. Produce the functional specification and acceptance criteria (Given/When/Then), including negative cases. Save it to `docs/specs/<module>.md`.
5. Describe the data model, APIs, events, permissions, state machine and workflows.
6. Identify security, privacy, failure, performance and migration risks.
7. **Stop for my approval.**
8. Explain the logic in plain English, then implement only the approved scope, in small, reviewable commits.
9. Write and run the tests that apply:
   - unit;
   - property-based (money);
   - integration;
   - contract;
   - E2E;
   - tenant-isolation;
   - security;
   - Fineract differential tests.
10. Run linting, type checks, build checks, migration validation and security scans.
11. Review the diff for unrelated changes, secrets, PII in logs and security defects.
12. Update the docs: setup, configuration, migration, deployment and runbooks.
13. Summarise:
    - what changed;
    - the actual test results;
    - known limitations;
    - mock vs live integrations;
    - next steps.
14. Commit with a meaningful message on the feature branch, open a pull request, and merge only after my approval.

## 11.2 Financial integrity before financial features

Do not implement live financial operations until their transaction rules and acceptance tests are approved. This covers:

- schedules;
- allocation;
- accruals;
- reversals;
- reconciliation;
- accounting entries;
- classification;
- provisioning.

Maintain a **golden test-case library**, approved by me and our finance/compliance reviewers, of worked numerical examples (EMI, broken-period interest, prepayment, bounce, NPA upgrade, EIR, GST). Every release must pass it.

## 11.3 Git and environment rules

- First inspect the connected repository: current branch, existing files, Git status and available tooling.
- Do not overwrite existing work without understanding its purpose.
- Work on feature branches. **Never push directly to `main`.** Never deploy to production, rotate live credentials or modify production data without my explicit authorisation.
  - The original Udofin prompt asked for a direct commit to main in one place. For Finbyx we use pull requests only. Branch protection on `main` must be enabled.
- Never commit API keys, service-role secrets, private certificates, production credentials or real borrower data. Use `.env.example` files with placeholders. Keep local, test, staging and production configuration separate. Use synthetic test data only.
- If repository write access or commit capability is unavailable, provide the exact files and commands. Do not claim to have committed.
- Do not claim a test passed unless it was actually run and its output is available.
- Do not implement large unapproved features or silently expand scope. Do not create placeholder business logic that pretends to work. Mark mocks clearly.

## 11.4 Project documents to maintain

Keep these documents current:

- `README.md`
- `CLAUDE.md` (concise, stable; links to detail)
- `docs/00-master-prompt.md`
- `docs/architecture/` (system context, C4 diagrams, module map, data ownership)
- `docs/adr/`
- `docs/specs/`
- `docs/products/`
- `docs/data-model/` (ERD, migrations log)
- `docs/api/` (OpenAPI, AsyncAPI)
- `docs/integrations/register.md`
- `docs/compliance/requirements-to-controls.md` and `docs/compliance/regulatory-register.md` (dated)
- `docs/security/threat-model.md` and `docs/security/checklist.md`
- `docs/testing/strategy.md` and `docs/testing/golden-cases/`
- `docs/ops/` (deployment, rollback, DR, runbooks, SLOs)
- `docs/legal/third-party-notices.md` (including Apache Fineract attribution if any code is derived)
- `docs/status/modules.md` (module status and outstanding decisions)
- `docs/economics/unit-costs.md`

## 11.5 Definition of done

1. A module is not complete just because its screen renders.
2. It is complete only when all of the following are true:
   - its approved acceptance criteria are met;
   - the relevant tests (including negative and tenant-isolation tests) have passed and their output is recorded;
   - authorisation and maker-checker have been checked;
   - failures, retries and reconciliation are handled;
   - accounting entries balance and reconcile;
   - audit events are emitted;
   - documentation and registers are updated;
   - the change is reviewable.
3. A mock or sandbox integration is always clearly distinguished from a production integration.
4. Our goal is a secure, maintainable, configurable, regulator-ready and commercially viable lending platform, not the largest number of features or files.

## 11.6 Additional quality gates

These come from the Udofin prompt and are extended here:

- **Independent security review** each phase (see 10.4).
- **Borrower consent and data lifecycle:** record what was consented to, why, when, for which lender and purpose, and the exact wording shown. Handle withdrawal, retention, deletion, correction and access logging, with legally required exceptions.
- **Disaster recovery:** test restoration of the database, documents, queues/workflows, and post-outage reconciliation. A backup is not proven useful until a restore has been tested.
- **Change and migration safety:** no deployment may leave web, field app, workers and database on incompatible versions. Use expand-and-contract migrations.
- **Regulatory change management:** keep a dated register. When a rule changes, assess the affected products, configurations, disclosures, workflows, tests and evidence.
- **Production monitoring:** SLOs for availability, latency, integration failure rates, queue delays, COB duration, reconciliation breaks and recovery. Alerts carry no sensitive data.
- **Commercial viability:** track per-application costs (verification, bureau, AA, eSign/eStamp, messaging, cloud, support) and revenue per tenant. A technically working product may still be commercially unviable.

---

# PART 12 — PHASED ROADMAP WITH CLAUDE CODE INSTRUCTIONS

Build a common platform first, then launch a **narrow MVP** before expanding:

- **MVP product scope:** an unsecured Personal Loan + an MSME Term Loan (unsecured), branch-assisted, single NBFC tenant on Supabase/Railway staging.
- **Next:** LAP/Home (secured property), Vehicle, Gold, LAS, co-lending.
- **Last:** the specialist products (13–16) after feasibility approval.

Each phase below ends with a review gate. Copy the **"Instruction to Claude"** text into Claude Code when you start that phase. Split large phases into sub-modules.

| Phase | Primary outcome | Depends on |
|---|---|---|
| 0. Repository audit and architecture | Verified repo facts, architecture proposal, ADRs, Fineract adoption decision, regulatory register v1 | — |
| 1. Platform foundation | Monorepo, CI/CD, environments, auth abstraction, design system, observability | 0 |
| 2. Database, tenancy and security foundation | Tenant/entity/branch model, RBAC/ABAC, RLS, audit events, maker-checker framework, tests | 1 |
| 3. Masters, configuration and product factory | Org hierarchy, calendars, masters, product factory, charges, rule packs, workflow designer v1 | 2 |
| 4. Ledger and accounting core | CoA, journal engine, posting rules, period close, trial balance — **before** any loan money moves | 2 |
| 5. Schedule and allocation engine | Fineract-equivalent schedules, allocation strategies, replay, differential harness, golden cases | 3, 4 |
| 6. Customer, KYC and consent | CIF, de-dupe, KYC adapters (mock → Surepass sandbox), consent ledger, AML screening | 2 |
| 7. Origination (LOS) | Leads, applications, bureau/AA, BRE, verifications, deviations/DoA, CAM, sanction, KFS | 5, 6 |
| 8. Documentation, eSign/eStamp, DMS, disbursement | Templates, signing evidence, OTC/PDD, mandate registration, payout, loan booking | 7 |
| 9. Servicing (LMS) and COB | Accruals, repayments, prepayment/foreclosure, resets, restructuring, service requests, COB with classification | 5, 8 |
| 10. Payments and reconciliation | eNACH/UPI AutoPay presentation, bounces, VAs, BBPS, PG links, 3-way reco | 9 |
| 11. Collections | Strategies, allocation, telecalling, field app, agencies, contact-policy guard-rails, call recording | 9, 10 |
| 12. Recovery and legal + Equator | Sec 138, SARFAESI, arbitration via Equator, repossession/auction, OTS, write-off | 11 |
| 13. Finance: Ind AS 109, IRACP, GST/TDS, borrowings, Tally/SAP | EIR, ECL, provisioning, tax, liabilities, accounting integrations, financial statements | 4, 9 |
| 14. Regulatory reporting, risk and compliance | CIC UCRF, CIMS returns, FMR, FIU-IND, ALM, concentration, ICAAP mart, compliance module and LawDocsComply bridge | 9, 13 |
| 15. Grievance, communications, borrower portal | Complaints/IO/RB-IOS, templates/DLT/WhatsApp, borrower portal, feedback | 9 |
| 16. Udofin and partner connectors | LSP framework, Udofin connector, DLG ledger, co-lending/DA engine, partner portals | 7–10 |
| 17. Secured products expansion | LAP/Home, Vehicle, Gold, LAS/LAMF templates and collateral flows | 8–12 |
| 18. Analytics, AI layer and MCP | MIS catalogue, BI embedding, AI copilots under governance, MCP server | 9–14 |
| 19. Migration tooling | Legacy loan boarding, reconciliation sign-off | 9, 13 |
| 20. Hardening and launch | E2E, VAPT, performance/COB load tests, DR drill, AWS migration plan, controlled rollout | all |

### Phase 0 — Repository audit and architecture

> **Instruction to Claude:** "Inspect the connected repository, branch, files, Git status and tooling, and report them. Read docs/00-master-prompt.md (this prompt). Do not write application code yet. Produce:
> (1) the architecture proposal: system context, modular-monolith module map with data ownership, tenancy and authorisation strategy (API + service + RLS);
> (2) the Apache Fineract adoption ADR comparing headless-Fineract, TypeScript re-implementation and hybrid-oracle, with a recommendation and the licence approach;
> (3) technology ADRs after checking current stable versions of each proposed tool;
> (4) the proposed repository structure (Appendix C as a starting point);
> (5) the initial entity model (Appendix D);
> (6) API boundaries and the Udofin/LSP integration contract outline;
> (7) regulatory register v1, verifying every [VERIFY] item in Part 8 against primary sources and listing those still unverified;
> (8) the phased roadmap with dependencies and acceptance criteria;
> (9) minimum security, testing and code-review gates;
> (10) the list of business decisions you need from me.
> Present all of this for approval before modifying the repository."

### Phase 1 — Platform foundation

> **Instruction to Claude:** "On branch `feat/platform-foundation`, initialise the approved monorepo:
>
> - pnpm + Turborepo, TypeScript strict, ESLint/Prettier;
> - the `apps/web` (Next.js), `apps/api` (NestJS) and `apps/worker` skeletons;
> - the `packages/` for contracts, domain-kernel (money, dates, IDs), ui (design tokens + shadcn), config and testing;
> - Docker Compose for local Postgres/Temporal/Gotenberg;
> - GitHub Actions CI (lint, typecheck, test, build, secret scan, dependency scan);
> - `.env.example` files;
> - an OpenTelemetry/Sentry baseline;
> - Storybook.
> Implement the domain-kernel `Money` type on decimal.js with rounding policies and property-based tests. No business features yet. Open a PR with test output."

### Phase 2 — Database, tenancy and security

> **Instruction to Claude:** "Design and create the migrations for:
>
> - tenants, legal_entities, branches (hierarchy), users, roles, permissions, role_permissions, user_scopes (entity/branch/product/amount limits);
> - maker_checker_requests;
> - audit_events (hash-chained);
> - consent_records;
> - idempotency_keys;
> - outbox_events.
>
> Implement:
>
> - server-side authorisation (RBAC + ABAC) and Postgres RLS on every tenant-scoped table;
> - the auth abstraction over Supabase Auth with MFA for staff;
> - the generic maker-checker framework.
>
> Write tenant-isolation and privilege-escalation tests that try to read and write across tenants, entities and branches, and prove they fail. Report results."

### Phase 3 — Masters, configuration and product factory

> **Instruction to Claude:** "Build:
>
> - org hierarchy, holiday calendars and business-date management;
> - masters (pincode, IFSC, purpose and sector codes, reason codes, NACH return codes as configurable data);
> - the product factory implementing every Fineract-equivalent parameter in Part 4.2A, with validation guard-rails from the regulatory rule packs (Part 10.2 #24);
> - the charges engine with GST profiles;
> - effective-dated versioning and maker-checker for all configuration.
>
> Produce the product specification template `docs/products/_template.md` and the first two product specs (Personal Loan, MSME Term Loan) for my approval."

### Phase 4 — Ledger and accounting core

> **Instruction to Claude:** "Before any loan money moves, build the double-entry ledger:
>
> - chart of accounts with the NBFC Ind AS template;
> - append-only journals with DB-enforced balance;
> - reversal-only corrections;
> - value/business/system dates;
> - period locks;
> - materialised balances;
> - trial balance;
> - accounting rule mapping (Fineract mapping keys + India extensions);
> - sub-ledger framework;
> - reconciliation checks.
>
> Write golden test cases for every posting rule and property tests that the ledger always balances. Show me the posting matrix for approval."

### Phase 5 — Schedule and allocation engine

> **Instruction to Claude:** "Implement the loan calculation engine as pure functions over an immutable loan event log:
>
> - EMI/equal-principal;
> - declining/flat;
> - daily/period interest;
> - day-count conventions;
> - broken period;
> - grace and moratorium;
> - tranches;
> - step-up/down and balloon;
> - interest recalculation and prepayment strategies;
> - all allocation strategies including `rbi-india-strategy` and advanced payment allocation;
> - back-dated replay with snapshots.
>
> Stand up a Fineract 1.15.0 container in CI as a test oracle and build the differential harness across a scenario matrix. Report paisa-level differences and classify each as a bug or an approved deviation."

### Phase 6 — Customer, KYC and consent

> **Instruction to Claude:** "Build:
>
> - the CIF with relationships;
> - de-dupe;
> - risk categorisation;
> - the consent ledger with exact notice versions;
> - KYC flows (CKYC search/download/upload, OKYC/DigiLocker, PAN, V-CIP hooks, OVD capture);
> - sanctions/PEP screening;
> - periodic-updation scheduler.
>
> Adapters: mock first, then a Surepass sandbox adapter behind `KycProvider`. Aadhaar is never stored in full outside the vault design approved in Phase 0. Verify the current KYC Directions paragraphs and record them in the register."

### Phase 7 — Origination (LOS)

> **Instruction to Claude:** "Implement:
>
> - leads and DSA/connector management with payouts;
> - dynamic application forms from product templates;
> - bureau and AA adapters (mock + sandbox);
> - the GoRules-based BRE with simulation;
> - verification management (FI/PD/technical/legal/RCU) with vendor allocation;
> - deviation matrix and DoA routing;
> - the CAM generator (template + AI-drafted narrative with citations, human-edited, locked at sanction);
> - sanction;
> - the KFS/APR engine per the RBC Directions Annex I with the consideration period.
>
> Model the application state machine explicitly. Include a full E2E test from lead to sanction for the two MVP products."

### Phase 8 — Documentation, execution, DMS and disbursement

> **Instruction to Claude:** "Build:
>
> - document templates and generation (Gotenberg);
> - eSign/eStamp/NeSL DDE adapters storing verifiable signing evidence;
> - physical-execution paths for excluded instruments;
> - the DMS with hashes, versions, retention and access logs;
> - OTC/PDD tracking;
> - mandate registration (eNACH/UPI AutoPay);
> - the disbursement memo with pre-disbursement checks, penny-drop and payout adapters with duplicate-payment prevention;
> - atomic loan booking with opening entries.
>
> Interest starts from the actual disbursement date. Cooling-off handling for digital loans."

### Phase 9 — Servicing (LMS) and COB

> **Instruction to Claude:** "Build:
>
> - the loan 360 view;
> - daily accrual;
> - penal charges as charges;
> - repayments with allocation;
> - part-prepayment and foreclosure quotes with the prepayment-charge engine;
> - floating-rate resets with borrower options;
> - restructuring/rescheduling with classification impact;
> - top-up/BT;
> - service requests and certificates;
> - closure, NOC and the document-release SLA with compensation;
> - write-off.
>
> Build the COB orchestrator with ordered configurable steps, borrower-level SMA/NPA classification and upgrade rules, income derecognition, catch-up, inline COB, partitioned workers and the EOD exceptions dashboard. Load-test COB at 1 million loans."

### Phase 10 — Payments and reconciliation

> **Instruction to Claude:** "Build:
>
> - the mandate lifecycle;
> - the presentation engine per sponsor bank with cut-offs;
> - re-presentation and bounce processing with charges;
> - UPI intent/QR/payment links;
> - virtual accounts;
> - the BBPS biller adapter;
> - branch cash/cheque deposit tracking;
> - three-way reconciliation with exception queues and suspense ageing.
>
> Provider success never finalises a payment without settlement confirmation. Add Stripe/PayPal adapters only for cross-border/SaaS billing, with an ADR."

### Phase 11 — Collections

> **Instruction to Claude:** "Build:
>
> - segmentation and bucket strategies triggered by COB DPD changes;
> - rule-based allocation;
> - telecalling workspace with dispositions/PTP;
> - field collections in the Expo field app (offline, geo-tag, digital receipts, cash limits and deposits);
> - agency management with the IIBF certification register;
> - contact-policy guard-rails (08:00–19:00, MFI 09:00–18:00, frequency caps);
> - mandatory call recording with 6-month retention per the August 2026 amendment;
> - pre-visit intimation;
> - borrower default intimation before CIC reporting.
>
> Verify the amendment text first."

### Phase 12 — Recovery, legal and Equator

> **Instruction to Claude:** "Build:
>
> - legal case management;
> - the Sec 138 and SARFAESI workflows with statutory timelines and templates (including the NBFC SARFAESI eligibility gate);
> - arbitration/mediation referral to Equator through the ODR adapter, with outcomes flowing back;
> - Lok Adalat;
> - the IBC/NeSL IU filing workflow;
> - repossession and auction;
> - the OTS/settlement calculator with approval matrix;
> - wilful-defaulter workflow;
> - write-off and post-write-off recovery accounting."

### Phase 13 — Finance, Ind AS 109 and accounting integrations

> **Instruction to Claude:** "Implement:
>
> - EIR (IRR-based) and amortisation;
> - ECL staging with a pluggable model and a default provision matrix;
> - parallel IRACP provisioning by layer with Impairment Reserve logic;
> - GST invoicing and extracts, and TDS;
> - bank reconciliation;
> - the borrowings/liabilities module;
> - month-end close;
> - financial statements per Schedule III Div III and the RBI disclosure Directions;
> - TallyPrime (local connector, JSON), SAP and Zoho adapters with reconciliation.
>
> Golden cases must be approved by our finance reviewer."

### Phase 14 — Regulatory reporting, risk and compliance

> **Instruction to Claude:** "Build:
>
> - CIC UCRF generation on the current reference dates with rejection handling;
> - the CIMS/XBRL return framework with lineage and certification (start with the returns applicable to the MVP tenant's layer);
> - FMR and FIU-IND reports;
> - ALM and concentration reports;
> - the ICAAP data mart;
> - the model inventory;
> - the embedded compliance module (register, controls testing, calendar, product approval);
> - the LawDocsComply bridge with mode switch.
>
> Verify every return specification against the 31 Jul 2026 Supervisory Returns Directions."

### Phase 15 — Grievance, communications and borrower portal

> **Instruction to Claude:** "Build:
>
> - the complaint management system with automated IO escalation and RB-IOS 2026 support;
> - Equator referral;
> - the AI support assistant restricted to approved sources;
> - template and communications management with DLT/WhatsApp, consent and dark-pattern checks;
> - the optional borrower self-service portal;
> - feedback (CSAT/NPS)."

### Phase 16 — Udofin and partner connectors

> **Instruction to Claude:** "Implement the LSP/channel-partner framework and the Udofin connector per Part 5:
>
> - OpenAPI/AsyncAPI contracts;
> - Pact contract tests;
> - signed webhooks;
> - reconciliation files;
> - the DLG ledger with the 5% cap;
> - the collection-agent appointment model separate from DLG;
> - the CIMS DLA register;
> - the co-lending engine (10% retention, 15-day booking, escrow, blended rate, classification sync);
> - DA/securitisation pools and partner portals.
>
> Prove that Finbyx runs normally when Udofin is unavailable."

### Phases 17–20

> **Instruction to Claude:** "For each secured product (LAP/Home, Vehicle, Gold, LAS/LAMF), produce the product spec and feasibility notes, then implement the collateral workflows, integrations and regulatory checks.
> Then deliver:
>
> - the MIS catalogue;
> - BI embedding;
> - governed AI copilots;
> - the read-only MCP server;
> - the legacy migration toolkit;
> - finally, hardening: full E2E, independent VAPT, COB/performance load tests, a DR restore drill, the AWS (ap-south-1 / ap-south-2) migration runbook and a controlled production rollout plan."

---

# PART 13 — START NOW

I have connected my GitHub repository for Finbyx. Do **not** begin by implementing the complete lending system.

First, execute **Phase 0 only**:

1. Inspect the repository and report its current state (files, branch, tooling, constraints).
2. Identify missing business decisions and major architecture, regulatory and financial-integrity risks.
3. Propose the repository structure, tenancy and authorisation strategy, Fineract adoption approach and technology choices (with current versions) as ADRs.
4. Prepare the initial entity model and API/integration boundaries, including the Udofin contract outline.
5. Prepare regulatory register v1, verifying the [VERIFY] items.
6. Prepare the phased roadmap with dependencies and acceptance criteria, and the minimum security, testing and review gates.
7. Present the proposed baseline changes and your questions for my approval **before** modifying the repository.

After approval, create the `feat/repo-baseline` branch, add `CLAUDE.md` (Appendix A), save this prompt as `docs/00-master-prompt.md`, initialise the approved baseline, and open a pull request.

Throughout development you may ask me as many questions as you need. I will act as project manager; you will architect and build Finbyx.

---

# APPENDIX A — CLAUDE.md SEED (keep concise and stable)

```markdown
# Finbyx — Claude Code Project Instructions

## What this is
Finbyx: multi-tenant web LOS + LMS + accounting + collections/recovery + risk +
regulatory reporting + compliance for Indian regulated lenders (NBFC/HFC/UCB/banks).
Part of the Infrabyx ecosystem (Udofin LSP, LawDocsComply GRC, Equator ODR) — integrate
only via versioned contracts. Full brief: docs/00-master-prompt.md.

## Non-negotiables

- Feature branches + PRs only. Never push to main, deploy to prod, touch prod data or
  rotate live credentials without explicit owner approval.
- Spec → approval → code. Explain logic in plain English before code. Small commits.
- Never claim a test passed unless run; paste results. Mark mocks vs live clearly.
- No secrets, real borrower data, Aadhaar/PAN/OTP/account numbers in code, logs or fixtures.
- Money: NUMERIC in DB, decimal.js in TS, strings in APIs. Never floats.
- Ledger is append-only and always balanced; corrections by reversal only.
- Every financial write is idempotent; state machines govern all lifecycle changes.
- Tenant/entity/branch isolation enforced in API, services AND Postgres RLS — and tested.
- Regulatory parameters live in versioned rule packs with guard-rails; tenants cannot
  override regulatory safeguards.
- Before any regulated workflow: verify the current RBI/other source and update
  docs/compliance/requirements-to-controls.md. Distinguish law vs interpretation.
- AI never approves/rejects/prices loans, moves money, rejects complaints or alters terms.
- Data stays in India (prod data, backups, logs).

## Commands
(pnpm install / dev / test / lint / typecheck / db:migrate / db:test — fill in Phase 1)

## Where things live
docs/architecture, docs/adr, docs/specs, docs/products, docs/api, docs/integrations,
docs/compliance, docs/security, docs/testing (golden-cases), docs/ops, docs/status.

## Definition of done
Acceptance criteria met; unit/integration/E2E/tenant-isolation/security tests run and
passed; ledger balances & reconciles; audit events emitted; docs and registers updated;
diff reviewed for secrets/PII/unrelated changes.
```

---

# APPENDIX B — BUSINESS DECISIONS THE PROJECT OWNER MUST TAKE

Claude Code should confirm these in Phase 0:

1. **First pilot tenant profile:** entity type, layer, Ind AS or not, products, branch count, existing systems to migrate from.
2. **MVP product set and launch geography** (state stamp duty and e-stamp coverage).
3. **Fineract approach:** port vs headless engine vs hybrid oracle, after the ADR.
4. **Hosting and data:** Supabase/Railway region for staging; AWS timeline; dedicated-deployment offer for banks.
5. **Commercial model:** per-loan, per-user, per-module or AUM-based pricing. This affects metering design.
6. **Vendor shortlist and contracts:** Surepass scope; bureau memberships (the lender's); eSign/eStamp; sponsor bank for NACH; payout bank; WhatsApp BSP; SMS DLT entity (the lender's).
7. **Field app:** Expo native vs PWA.
8. **Compliance mode default:** embedded vs LawDocsComply.
9. **Borrower portal:** included for non-Udofin lenders or not.
10. **Specialist products (13–16):** who owns the feasibility notes, and the legal-review budget.
11. **Reviewers:** finance reviewer (CA) for golden accounting cases; compliance reviewer for the regulatory register; independent VAPT firm (CERT-In empanelled).
12. **Data retention periods by document class** (Board-policy inputs from pilot lenders).

---

# APPENDIX C — STARTING REPOSITORY STRUCTURE (to be refined in Phase 0)

```
finbyx/
├─ apps/
│  ├─ web/                 # Next.js internal workspaces + tenant admin + partner portals
│  ├─ borrower-portal/     # optional lean borrower portal (Next.js)
│  ├─ field/               # Expo React Native field app
│  ├─ api/                 # NestJS modular monolith (HTTP + webhooks)
│  └─ worker/              # Temporal workers, COB, schedulers, outbox relay
├─ modules/                # domain modules (each: domain/, application/, infra/, api/, tests/)
│  ├─ identity-access/  ├─ organisation/   ├─ configuration/  ├─ product-factory/
│  ├─ customer-kyc/     ├─ consent/        ├─ origination/    ├─ decisioning-bre/
│  ├─ verification/     ├─ collateral/     ├─ documents-dms/  ├─ loan-servicing/
│  ├─ schedule-engine/  ├─ cob/            ├─ payments/       ├─ mandates/
│  ├─ reconciliation/   ├─ collections/    ├─ recovery-legal/ ├─ ledger-gl/
│  ├─ indas-ecl-iracp/  ├─ tax-gst-tds/    ├─ treasury-borrowings/
│  ├─ colending-da/     ├─ risk/           ├─ regulatory-reporting/
│  ├─ compliance/       ├─ grievance/      ├─ communications/ ├─ partners-lsp/
│  ├─ analytics/        └─ ai-assist/
├─ packages/
│  ├─ contracts/  (OpenAPI, AsyncAPI, zod schemas, event catalogue)
│  ├─ domain-kernel/ (Money, Rate, BusinessDate, IDs, Result types)
│  ├─ adapters/  (kyc, bureau, aa, esign, estamp, nach, pg, payout, depository, tally, sap, odr, grc, llm …)
│  ├─ rule-packs/ (regulatory parameters, versioned)
│  ├─ ui/  (design tokens, components, Storybook)
│  ├─ config/  ├─ observability/  └─ testing/ (fixtures, synthetic data, fineract-oracle harness)
├─ db/
│  ├─ migrations/  ├─ rls-policies/  └─ seeds/ (synthetic only)
├─ infra/ (docker, compose, opentofu/terraform, railway, aws)
├─ docs/ (see Part 11.4)
└─ CLAUDE.md
```

---

# APPENDIX D — INITIAL ENTITY MODEL (starting list)

- **Platform and organisation:**
  - tenant, legal_entity, entity_regulatory_profile (type, layer, asset size, Ind AS flag);
  - branch/hierarchy_node, holiday_calendar, business_date;
  - user, role, permission, user_scope, maker_checker_request, audit_event, feature_flag, config_version.
- **Parties:** customer (individual/non-individual), customer_relationship, kyc_record, ckyc_record, consent_record, consent_artefact, screening_result, risk_category_history.
- **Origination:**
  - lead, dsa/connector, payout_rule, payout_statement;
  - application, applicant_role, data_pull (bureau/AA/GST/…), bre_decision (inputs, rule version, outputs);
  - deviation, approval (authority, limit used), verification_task/report, cam_version;
  - sanction, kfs_version, offer.
- **Products and pricing:** product, product_version, charge_definition, gst_profile, rule_pack_version, accounting_rule_map, benchmark_rate.
- **Collateral:** collateral, collateral_owner, valuation, charge_registration (CERSAI/RTO/depository), insurance_policy, custody_record, ltv_snapshot, release_record.
- **Loans:** loan_account, tranche, loan_event (immutable), schedule_version, installment, loan_balance_snapshot, classification_history, restructuring_record, mandate, presentation, payment, receipt_allocation, suspense_item.
- **Collections and legal:** strategy, allocation, contact_attempt (recording ref), ptp, field_visit, agency, agent (IIBF cert), legal_case, legal_event, repossession, auction, settlement.
- **Accounting:** gl_account, journal, posting, sub_ledger_account, period, reconciliation_run/break, gst_invoice, tds_entry, borrowing, borrowing_schedule, ecl_run, provision_run.
- **Risk and compliance:** exposure_snapshot, limit, ews_signal, fraud_case, model_inventory, regulatory_obligation, control, control_test, evidence, return_definition, return_run, cic_submission.
- **Service:** service_request, complaint, complaint_escalation, odr_referral, communication, template_version, feedback.
- **Integration:** integration_config, provider_call_log (redacted, with cost), webhook_delivery, outbox_event, idempotency_key, partner (LSP/co-lender/investor), dlg_arrangement, dlg_invocation, colending_split, pool.

---

## SOURCES CONSULTED FOR THIS PROMPT (for Claude Code to re-verify)

- **RBI:**
  - Press release on the 244 consolidated Master Directions (28 Nov 2025): https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=61705
  - Master Directions index: https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx
  - NBFC Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions, 2026: https://rbi.org.in/scripts/NotificationUser.aspx?Mode=0&Id=13592
  - NBFC Miscellaneous Supervisory Directions, 2026: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13586
  - RBC Second Amendment Directions, 2026: https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=13493
  - FREE-AI report: https://www.rbi.org.in/scripts/PublicationReportDetails.aspx?ID=1306
- **Secondary reproductions and summaries** (verify against RBI):
  - TaxGuru texts of the NBFC Credit Facilities, Responsible Business Conduct, IRACP and Credit Information Reporting Directions, 2025; the Internal Ombudsman Directions 2026; RB-IOS 2026; the commercial-bank ECL Directions 2026.
  - CAalley list of the 64 Supervision Directions (31 Jul 2026).
  - CARE Ratings note on the Co-Lending Directions 2025.
  - CorpLawUpdates on the recovery-agent amendments (6 Aug 2026).
- **Apache Fineract:**
  - Project site: https://fineract.apache.org/
  - Source: https://github.com/apache/fineract (1.15.0)
  - 1.15.0 release notes: https://cwiki.apache.org/confluence/display/FINERACT/1.15.0+-+Apache+Fineract
- **Technology and integrations:**
  - ReBIT AA specifications: https://api.rebit.org.in/spec/aa
  - NSDL APIs: https://nsdl.co.in/API-BP/api_brief.html
  - CDSL APIs: https://www.cdslindia.com/DP/APIs.html
  - TallyPrime JSON integration: https://help.tallysolutions.com/tally-prime-integration-using-json-1/
  - Surepass API catalogue: https://surepass.io/surepass-id-verification-apis/
  - Temporal regions: https://docs.temporal.io/cloud/regions
  - GoRules ZEN: https://docs.gorules.io/reference/nodejs
  - UIDAI Aadhaar Data Vault FAQs: https://www.uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf

*End of master prompt.*
