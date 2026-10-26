# FINBYX — Master Build Prompt for Claude Code

**Web-based Loan Origination (LOS), Loan Management (LMS), Accounting, Collections & Recovery, Risk and Compliance System for NBFCs, HFCs, Banks and other Regulated Lenders**

Version 1.2 · Revised 18 October 2026 (RBI Directions supplied by the project owner incorporated in Part 8A; revision log in Appendix E) · Derived from the Udofin mobile-app master prompt and rewritten for Finbyx

---

## HOW TO USE THIS PROMPT (for the project owner — do not paste this box)

1. **Before Session 1:** Commit this entire file to the Finbyx repository as `docs/00-master-prompt.md`. That means Parts 1–13, Appendices A–E and the Sources — everything below this box. Do not paste only Parts 1–13, because Phase 0 depends on the appendices.
2. **Session 1:** Open Claude Code on the repository and type: *"Read docs/00-master-prompt.md in full, then execute Part 13 (Phase 0 only)."* Claude Code will audit and propose, then stop for your approval.
3. **After approval:** Claude Code commits `CLAUDE.md` (Appendix A), which points every later session to the master prompt.
4. **Every later session:** Copy the matching phase instruction from Part 12 ("Instruction to Claude"), one phase or sub-module at a time. Approve each specification before code is written.
5. **Items marked [VERIFY]** are regulatory or vendor facts that need re-checking against the primary source before the related module is built. Claude Code is instructed to do this check and to record the result in the regulatory register.
6. **Data residency:** Railway has no India region. Use synthetic data only until India-region hosting is in place (Part 10.1).
7. **RBI source texts:** commit the official RBI Direction PDFs you supplied to `docs/regulations/rbi/` (Part 8A.0). Part 8A cites them paragraph by paragraph.

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
| L | Internal Audit and Auditors (read-only) | Internal, concurrent and statutory auditors, RBI inspection support | Sampling, audit trails, evidence packs for the Auditor's Report Directions (PBC test, NOF, IRACP/CRAR lineage, DNBS10, exception-report register; Part 8A.15), fraud closure files |
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

- **Current stable release:** 1.15.0, released 14 July 2026, on Java 21 and Spring Boot 3.5.x. The develop branch has already moved to Java 25 and Spring Boot 4.
- **Licence:** Apache 2.0.
- **Supported database:** PostgreSQL is the officially supported database (1.15.0 expects PostgreSQL 18 and recommends about 16 GB RAM and 8 cores). MySQL/MariaDB is deprecated.
- **Loan engines:** two coexist. The legacy **CUMULATIVE** engine and the newer **PROGRESSIVE** engine, which goes with `advanced-payment-allocation-strategy`.
- **Not production-ready:** Working Capital Loans (FSIP-010) are flagged as not production-ready in 1.15.0 [VERIFY in the release notes].

## 4.1 Adoption decision — produce an ADR in Phase 0

Evaluate three options and recommend one, with reasons:

1. **Run Fineract as a headless core engine** behind Finbyx's TypeScript services.
   - **Pros:** proven logic out of the box.
   - **Cons:** a Java runtime to operate; a database-per-tenant model; a synchronous command bottleneck; full chronological replay on every back-dated transaction; MFI-oriented assumptions; no Ind AS 109 EIR or ECL; no Indian GST/TDS treatment; India-specific changes would need forking.
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
  - **Engine constraint (Fineract 1.15.0):**
    - The first three strategies work only on CUMULATIVE.
    - PROGRESSIVE accepts only *adjust last unpaid period*.
    - On progressive loans, reduce-EMI and reduce-tenure come from the future-installment rule: `REAMORTIZATION` ≈ reduce EMI; `LAST_INSTALLMENT` / `NEXT_LAST_INSTALLMENT` ≈ shorter tenure.
    - Finbyx's single engine must offer all four outcomes on every product.
    - The oracle scenario matrix must pick the right Fineract engine for each scenario.
- **Floating rates:** benchmark linkage plus spread, with min/max differential, reset frequency and reset handling (M6; Part 8.2, Responsible Business Conduct row).
- **Charges:**
  - time types: disbursement, specified due date, installment fee, overdue installment (penal charge), tranche disbursement;
  - calculation types: flat, % of amount, % of amount and interest, % of interest, % of disbursement amount;
  - penalty flag.
- **Other parameters:** borrower-cycle-based variations, guarantee requirements, top-up eligibility, NPA days and "moves out of NPA only on full arrears clearance", charge-off behaviour, and per-loan attribute overrides permitted by the product.

**B. Repayment allocation strategies (configurable per product):**

- **Legacy-equivalent strategies:**
  - `mifos-standard-strategy`: Penalties → Fees → Interest → Principal, by installment.
  - `rbi-india-strategy`, "Overdue/Due Fee/Int,Principal":
    - On a late payment, for each overdue and current installment in date order, pay penalty → fee → interest; then pay principal, oldest first.
    - In-advance payments are treated like on-time payments.
    - Use it as the **Indian reference behaviour**.
    - **It exists only on Fineract's CUMULATIVE engine.** Finbyx must therefore also express this "RBI order" as an advanced-allocation rule set (VERTICAL processing):
      1. `PAST_DUE_PENALTY`, `PAST_DUE_FEE`, `PAST_DUE_INTEREST`
      2. `DUE_PENALTY`, `DUE_FEE`, `DUE_INTEREST`
      3. `PAST_DUE_PRINCIPAL`, `DUE_PRINCIPAL`
      4. `IN_ADVANCE_*`
    - Differential-test it against both oracles and record any differences.
  - `principal-interest-penalties-fees-order-strategy`.
  - `interest-principal-penalties-fees-order-strategy`.
  - `early-repayment-strategy`.
  - `due-penalty-fee-interest-principal-in-advance-principal-penalty-fee-interest-strategy`.
  - `due-penalty-interest-principal-fee-in-advance-penalty-interest-principal-fee-strategy`.
  - Also `heavensfamily-strategy` and `creocore-strategy` (legacy; reference only).
- **Advanced payment allocation** (rule-based):
  - allocation rule lists made of `PAST_DUE_*`, `DUE_*` and `IN_ADVANCE_*` × {PENALTY, FEE, INTEREST, PRINCIPAL};
  - a separate rule set per transaction type (repayment, down-payment, waiver, refund, goodwill credit, charge adjustment, and so on, with a mandatory `DEFAULT`);
  - future-installment rule: next installment, last installment, next-last, or re-amortisation.
- **PROGRESSIVE-only features in Fineract 1.15.0:** re-age, re-amortise, charge-off behaviour, capitalised income, buy-down fee, interest refund, the custom leap-year strategy, and "no interest on past due". Finbyx's single engine supports them for every product where policy allows.
- Allocation must be **replayable**. A back-dated payment or reversal re-runs allocation from the affected date and produces adjustment entries. It must never mutate history.

**C. Loan lifecycle (state machine with explicit allowed transitions):**

- **States:**
  - Lead → Application Draft → Submitted → Under Appraisal → Recommended → Sanctioned / Rejected / Withdrawn;
  - Sanction Accepted → Documentation → Ready for Disbursement → Active. The first disbursement makes the loan Active, with accrual and DPD running. Sub-status: partially disbursed / fully disbursed.
  - Overpaid;
  - Active – Charged-off / Technically written-off. The account stays open: recovery continues and CIC reports the written-off status with the outstanding balance.
  - Closed: obligations met / foreclosed / settled (OTS) / fully written-off with no further recovery pursued / restructured-closed / transferred (assignment);
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
- Pause and resume (Fineract 1.15.0), plus reset as a Finbyx addition — **only under maker-checker and a policy reason**, because pausing can be misused for evergreening.
- DPD = business date − oldest overdue due date.
- **Classification is borrower-level across all facilities, as RBI requires.** This is stricter than Fineract, which is loan-level.

**E. Close of Business (COB / End of Day):**

- **Business date** is separate from system date. COB date = business date − 1. Use catch-up for missed days and inline COB for a single loan before a write.
- **Ordered, configurable COB steps.** Fineract's six default steps are: apply overdue charges, delinquency classification, repayment-due check, repayment-overdue check, arrears ageing, periodic accruals. Finbyx reorders and extends them for IRACP. Income must never be accrued on an account that becomes NPA that day.
  - **Pass A (per loan, partitioned):**
    1. Apply overdue/penal charges
    2. Interest recalculation (where the product uses it)
    3. Repayment-due and overdue events
    4. Arrears ageing
    5. Loan-level DPD/delinquency
  - **Barrier (cross-loan):**
    6. Borrower-level SMA/NPA classification and upgrade check across all facilities of the borrower (and across co-lending partners and group entities where permitted)
  - **Pass B (per loan, partitioned):**
    7. Income recognition: accrue for standard accounts; for NPA accounts derecognise and reverse unrealised income, and keep memorandum interest only
    8. EIR amortisation (Stage 3 on net carrying amount)
    9. ECL/IRACP provisioning snapshot
  - **Job-level:**
    10. Co-lending classification sync file
    11. CIC reference-date extracts
    12. Collection allocation refresh
    13. GL posting batch and sub-ledger-to-GL reconciliation
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
  - income from charge-off (interest, fees, penalty) and income from goodwill credit (interest, fees, penalty);
  - income from capitalisation, buy-down expense and income from buy-down;
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
   - PostgreSQL `NUMERIC`: amounts `NUMERIC(20,4)`; rates `NUMERIC(12,8)`; APR/EIR `NUMERIC(14,10)` (payday APRs can exceed 999%);
   - `decimal.js` in TypeScript, configured with at least 40 significant digits (`Decimal.set({ precision: 40 })`);
   - money serialised as strings in APIs;
   - an explicit, configurable rounding policy per component;
   - rounding of transactions to the nearest rupee where RBC para 103 requires it (50 paise and above rounded up) [VERIFY scope].
4. **Ind AS 109 compliance:**
   - EIR computed by IRR (Newton-Raphson with bisection fallback) over contractual cash flows, including fees and directly attributable costs;
   - amortisation of deferred fee and cost at EIR;
   - Stage 1/2/3 ECL (PD × LGD × EAD, SICR at >30 DPD rebuttable, credit-impaired at >90 DPD);
   - interest on net carrying amount in Stage 3;
   - **parallel IRACP computation**, with the shortfall appropriated to an Impairment Reserve where Ind AS ECL is lower than the prudential floor.
5. **Indian GST:**
   - exclusive GST added on top of fees, with a CGST/SGST/IGST split by place of supply;
   - **no GST on penal charges** (CBIC Circular No. 245/02/2025-GST dated 28 Jan 2025, para 2.5);
   - a configurable flag for bounce charges, which become GST-free only if the lender's Board policy treats them as penal charges [VERIFY];
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
   - Repayment goes **directly to the lender's account** (or a co-lending escrow controlled only by the co-lenders — CF para 10(1), Note).
   - **No LSP pool or pass-through accounts.**
   - LSP fees are paid by the lender, never charged to the borrower.
   - Finbyx must reject any integration configuration that routes funds otherwise.
   - Basis: CF para 10(1)–(4). Third-party disbursal is allowed only (i) exclusively under a statutory or regulatory mandate, (ii) for co-lending flows between lenders, or (iii) for a specific end use, paid directly into the end-beneficiary's bank account — never into an LSP account. A salary advance may be repaid by the employer by salary deduction, directly from the employer's bank account (para 10(1) proviso).
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
| Finbyx → LSP | `CollectionAllocated`, `CollectionDeallocated` | Where the contract appoints the LSP as a recovery agent. The allocation carries the contact-policy rules (calling hours, call recording, agent certification). Allocation on a digital loan triggers the email/SMS of the agent's particulars to the borrower before first contact (CF para 9(6)) |
| LSP → Finbyx | `CollectionActivityLogged`, `PTPCaptured`, `FieldVisitLogged`, `ReceiptIssued` | Collections activity with geo-tags and recordings. **No pooling of borrower money by the LSP.** Cash recovered on a delinquent loan must be reflected in full in the borrower's loan account on the day of collection, and no LSP fee may be deducted from it (CF para 10(5)) |
| Both | `GrievanceRaised`, `GrievanceUpdated`, `GrievanceEscalated` | Complaint routing to the lender's Grievance Redressal Officer and Internal Ombudsman, onward referral to Equator, and RB-IOS escalation information |
| Finbyx ↔ LSP | `DLGArrangementRegistered`, `DLGInvocationRaised`, `DLGInvocationSettled`, `DLGPortfolioCoverage` | Default Loss Guarantee ledger (see below) |
| Finbyx ↔ LSP | `DailyReconciliationFile` | Disbursements, collections, fees and DLG positions, with break reports |

**Collections responsibility.** Keep contractual collection responsibility separate from DLG. A DLG arrangement does not by itself make the LSP the collector. Collection rights come only from an explicit recovery-agent or outsourcing contract recorded in Finbyx, with its effective dates, scope and controls.

**DLG engine in Finbyx (lender side):**

- Register each arrangement:
  - the provider: an LSP, or another lender engaged as LSP, incorporated under the Companies Act, 2013 (CF para 19);
  - the form: cash deposited with the NBFC, an FD with a Scheduled Commercial Bank with lien in favour of the NBFC, or a bank guarantee in favour of the NBFC (para 23);
  - the fixed DLG set of loans (para 24(2));
  - the provider's statutory-auditor-certified declaration, on every entry or renewal (para 20(3)).
- Enforce the cap: total DLG cover ≤ 5% of the amount disbursed out of the covered loan portfolio (CF para 24).
- The DLG term must be at least the longest loan tenor in the portfolio.
- Track invocation within the permitted overdue window.
- Asset classification and provisioning of the underlying loans follow the IRACP Directions (CF para 25(1)).
- Invoked DLG is never set off against individual loans (para 25(2)) and is never reinstated, including through recovery (para 25(4)).
- Block DLG on loans under trust-fund credit-guarantee schemes (para 21(1)).
- The BRE must not use DLG cover as an underwriting input (para 20(2)).
- Track the LSP's monthly portfolio disclosure, due within 7 working days of month-end (para 28).
- If the tenant is itself a DLG provider, deduct the DLG from capital (para 26(2)).
- Report DLG positions and disclosures.

Map this to CF paras 19–29. Invocation must happen within 120 days overdue (para 27).

**CIMS DLA reporting (CF para 18, Annex-I).**
- Maintain a register of every DLA, own or LSP, with one line per DLA per platform.
- Fields: name, owner, platform, link, GRO name/email/telephone/mobile, RE website.
- Update the register when a DLA is added or ceases.
- Support certification of the four para 18(4) points by the CCO or a Board-designated official.
- **Multi-lender offer view (CF para 7):**
  - each offer shows lender name, amount, tenor, APR, monthly repayment obligation, penal charges and a KFS link;
  - the names of unmatched lenders are disclosed;
  - the matching approach is documented and consistent;
  - offers are ranked only on a publicly pre-disclosed metric, with no dark patterns.
  - Finbyx stores the LSP's attestation and the version of its matching mechanism.

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
8. Permitted disbursement routing: borrower account, seller/dealer/builder, or hospital/service provider where permitted (for digital loans, CF para 10(1) allows third-party disbursal only for statutory/regulatory mandates, co-lending flows or a specified end-use beneficiary).
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
| 2 | **Payday / Short-tenure Loan** | Unsecured | Bullet repayment and APR display for tenors under 7 days; KFS validity period of at least 1 working day for tenor < 7 days (RBC para 29(2)); cooling-off (CF para 11); strict affordability and repeat-borrowing limits; **heightened conduct risk**. Compliance Department approval before launch and 6 months of intensive monitoring are mandatory for ML/UL tenants (CMP paras 9(7), 15(2), 31); Finbyx applies this gate to every tenant by default. A collateral-free loan to a household with income ≤ ₹3 lakh is a microfinance loan (CF para 51) |
| 3 | **Business / MSME Term Loan** | Either | GST and AA cash flows, Udyam, MCA data, banking analysis, CGTMSE/guarantee cover; prepayment-charge rule for floating-rate MSE loans |
| 4 | **Loan Against Property (LAP)** | Mortgage | Technical and legal verification, title search, valuation (2 valuers above threshold), equitable or registered mortgage, CERSAI, property insurance, SARFAESI eligibility, release of documents within 30 days |
| 5 | **Home Loan** (purchase / construction / renovation / plot + construction / balance transfer / top-up) | Mortgage | Construction-linked multi-tranche disbursement, PEMI vs full EMI, builder APF projects, PMAY-type subsidy handling, Sec 24(b)/80C certificates, HFC-specific regulation (RBI HFC Directions; NHB returns) |
| 6 | **Vehicle Loan** (new/used car, two-wheeler, CV, tractor, equipment) | Hypothecation | Dealer/manufacturer disbursement, Vahan RC check, hypothecation endorsement (Form 34) and termination (Form 35), insurance tracking, repossession under the RBI recovery norms, used-vehicle valuation |
| 7 | **Loan Against Securities (LAS): shares, bonds, MF units** | Pledge/lien | NSDL/CDSL pledge, unpledge and invocation APIs; MF lien through RTA/MF Central or depository; approved-securities list; haircut master; daily LTV and margin-call engine on bhavcopy/NAV feeds. **Loans against listed shares by NBFCs with assets ≥ ₹100 crore (CF para 106):** 50% LTV at all times; shortfall cured within 7 working days; only Group 1 securities where the loan is for capital-market investment and exceeds ₹5 lakh; quarterly online reporting of pledged shares to the stock exchanges in the Annex-III format. No lending against the NBFC's own shares (para 105). IPO-funding cap of ₹1 crore per borrower (para 104). Bonds and MF units follow Board-approved haircuts (CF prescribes no LTV for them). Units of gold/silver ETFs or MFs backed by primary gold/silver are blocked as collateral (CF para 35(2)) |
| 8 | **Gold Loan** (and silver where offered) | Pledge | Assay capture (karat, gross/net weight), **Lending terms (CF Ch IV, paras 32–50).** Eligible collateral is only gold/silver jewellery, ornaments and coins. Primary gold/silver, bullion, gold/silver-backed financial assets, and loans to buy gold are blocked (para 35). An ownership declaration is required on every loan (para 36); no re-pledge (para 37). Valuation at actual purity: the lower of the 30-day average closing price and the previous day's close, from IBJA or a SEBI-regulated exchange, with nearest-purity adjustment and intrinsic metal value only (paras 40–42). Consumption-loan LTV is 85% / 80% / 75%, by **total consumption loan per borrower** (≤ ₹2.5 lakh / > ₹2.5–5 lakh / > ₹5 lakh); for bullet loans, both LTV and slab use the total repayable at maturity; LTV is maintained daily for the whole tenor (paras 43–44). A detailed credit assessment is required above ₹2.5 lakh (para 33). Consumption bullet loans are capped at 12 months (para 38). Renewal or top-up only on a formal request, within LTV, on a standard account; bullet renewals only after accrued interest is paid; renewals and top-ups flagged in the system (para 34). Weight caps per borrower: gold ornaments 1 kg, silver ornaments 10 kg, gold coins 50 g, silver coins 500 g (para 39). AML alert on multiple or frequent loans; multiple-loan internal-audit report (paras 36, 48). Disbursal and repayment rules of para 10 apply on every channel (para 47). **Release and auction (RBC Ch III.G, paras 42–75):** release on the same day and in any case within 7 working days (para 58), with delay compensation [VERIFY amount and para]; auction with notice, two newspapers, and a reserve price of ≥ 90% of current value, which may fall to 85% after two failed auctions (paras 60–66); unclaimed collateral (paras 71–72) |
| 9 | **Education Loan** | Either | Disbursement to institution, moratorium during course plus grace, co-borrower |
| 10 | **Consumer Durable / Point-of-sale Loan** | Unsecured | Merchant/dealer onboarding, subvention (buy-down fee), zero-cost EMI accounting, merchant refund |
| 11 | **Microfinance (JLG/SHG and individual)** | Collateral-free (no deposit lien, no hypothecation) | Household = husband, wife and unmarried children, with annual income ≤ ₹3,00,000. **Every** collateral-free loan to such a household is a microfinance loan, whatever the product or channel (CF para 51). Board-policy income assessment over ≥ 1 year (para 52); household income reported to CICs (para 54). Repayment obligations of all household loans plus the proposed loan ≤ 50% of monthly household income, with no new loans while above it (paras 55–57). Flexible periodicity (para 59). Pricing policy with a ceiling on the rate and all charges (paras 60–61). centre meetings, weekly/fortnightly collections, effective-dated MFI recovery-contact window (09:00–18:00 under RBC para 91(2) until 31 Dec 2026; from 1 Jan 2027 per the RBC Third Amendment [VERIFY whether a separate MFI window survives]), no prepayment penalty (RBC para 81) |
| 12 | **Supply-chain / Invoice / Channel Finance** | Either | Anchor programmes, invoice validation, TReDS. **Revolving-credit restriction on NBFCs under the August 2026 draft Credit Facilities amendment** [VERIFY final status before building any revolving line] |
| 13 | **Medical and Insurance Finance** | Either | Hospital/insurer institutional partnerships, direct payment to provider where permitted, pre-authorisation linkage, insurance-claim offset. **Feasibility pilot only** |
| 14 | **Legal Expense and Award-Enforcement Finance** | Either | Ordinary repayable loans only through the regulated lender. Non-recourse or litigation-funding cases are **referred out to specialist funders, not booked**. Requires a legal feasibility assessment first |
| 15 | **Resolution Finance** (linked to Equator settlements) | Either | Funds the borrower's settlement with an existing lender; disbursement direct to the creditor; settlement evidence from Equator; affordability test; measurement of qualification rates. **Pilot** |
| 16 | **Debt Reset / Consolidation** | Either | Rigorous affordability and debt-closure model before refinancing stressed borrowers; direct payoff to existing lenders; no evergreening of the lender's own NPAs (Resolution of Stressed Assets Directions [VERIFY]); restructuring flags. **Pilot** |
| 17 | **Co-lending products** | Any | Partner share (minimum 10% retention by each lender), blended rate, escrow, partner share booked within 15 days, borrower-level classification sync (Part 7, M11) |
| 18 | **Loans to entities / Term lending to NBFCs and corporates** | Either | Covenants, security cover, ratings, sanction terms, CRILC reporting. LEI gate for non-individuals with aggregate bank/FI exposure ≥ ₹5 crore (CRM paras 19–20). Notified-NBFC appraisal pack: independent appraisal, sensitivity tests, promoter-equity source, director DIN/PAN defaulter check (CRM paras 6–8) |
| 19 | **Staff loans** | Either | Payroll deduction, perquisite valuation report. Specified-employee and relative tagging, policy limits, recusal, and an annual Board report (CRM paras 13D, 13J, 13L) |
| 20 | **Demand / Call Loan** | Either | Mandatory recall cut-off date (reasons recorded if beyond 1 year); stated rate with interest payable monthly or quarterly (reasons recorded if none or moratorium); review within 6 months of sanction; renewal blocked unless the review is satisfactory (CF para 107) |
| 21 | **Project Finance** (infrastructure / non-infrastructure / CRE / CRE-RH) | Either | Qualifies only with ≥ 51% repayment from project cash flows and a common agreement among lenders (CF para 4(1)(xxiv)); applies where financial closure is after 1 Oct 2025 (para 64). Pre-disbursement gates: financial closure, original DCCO and approvals (paras 67, 70–71); land or right of way 50% PPP / 75% others (para 72); PPP Appointed Date (para 73); TEV study if aggregate exposure ≥ ₹100 crore (para 74). Tenor including moratorium ≤ 85% of economic life (para 67(3)); common DCCO (para 68); minimum exposure floors (para 69); stage-linked, LIE-certified disbursal (para 75); project database updated within 15 days of any change (paras 77–78) |

**Draft revolving-credit restriction (6 Aug 2026 draft CF amendment; comments closed 28 Aug 2026).** If finalised, NBFCs other than credit-card NBFCs would be confined to term loans [VERIFY final status]. The CF text updated to 1 Apr 2026 does not contain this restriction. Today only para 8(2) (no automatic limit increase on digital loans) and para 107 (demand/call loans) apply. This affects:

- flexi/OD-style personal and business loans (Products 1 and 3);
- LAS drawing-power or overdraft lines (Product 7);
- channel and working-capital lines (Product 12).

Build these as term-loan structures by default, and keep any revolving variant behind a feature flag until the final text is known.

**Housing finance and CRE classification (Products 4, 5 and 21; CF paras 4(1)(xiv), 108–111):**

- A plot loan counts as housing finance only with a declaration to construct within 3 years.
- LAP and furnishing loans are not housing finance.
- A loan for an individual's third dwelling unit onwards is CRE.
- Commercial area above 10% of FSI makes the whole loan CRE.
- Builder/project loans: funds are held until the mortgagee disclosure and NOC conditions are met.
- Real-estate loans are disbursed only after statutory clearances.

**Top-ups against depreciating movable assets** such as vehicles (Product 6) are treated as unsecured for appraisal, limits and exposure (CON para 10).

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
- **Branch/office regulatory master and closure workflow** (BR Directions, Part 8A.6), and the **entity regulatory profile** that drives the applicability of every rule (Part 8A.16, M1).
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
- **Related-party register and connected-counterparty groups** (CRM paras 13A–13Q; CON para 4(3)), LEI records (CRM paras 18–24), and the fraud-debarment register with associated entities (FRM para 35). See Part 8A.3, 8A.4 and 8A.14.
- **De-duplication:** internal match on PAN, Aadhaar reference/token, mobile, name + DOB, address and bank account; fuzzy matching; negative and blacklist checks; wilful-defaulter list check.
- **KYC per RBI (NBFC – Know Your Customer) Directions, 2025 (28 Nov 2025) and the amendment of 29 Dec 2025 [VERIFY]:**
  - CKYC search, download and upload. Upload within the prescribed period, and push updates when data changes. Build for CKYCRR 2.0 real-time APIs: search, download with OTP consent, upload.
  - Aadhaar offline e-KYC (XML/QR) and DigiLocker. Full Aadhaar e-KYC authentication only where the lender is a notified entity.
  - V-CIP (video KYC): live official, liveness, geo-tagging, recording stored in India, and the audit trail.
  - OVDs (officially valid documents); PAN verification and the PAN–Aadhaar link status.
  - Periodic updation by risk category, with reminders.
  - Risk categorisation (low, medium, high) with re-categorisation triggers.
- **Aadhaar Data Vault: UIDAI Circular No. 14 of 2025 (4 Nov 2025), which supersedes Circular 8 of 2025.**
  - The vault may be hosted only on-premises, on a MeitY-empanelled Government Community Cloud, or through ADV-as-a-service.
  - It needs an HSM certified FIPS 140-2 Level 3 or higher, and non-reversible reference keys. Hashing the Aadhaar number is not permitted.
  - A commercial cloud region with CloudHSM may therefore not qualify. Record the hosting choice in an ADR.
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
   - Pre-sanction fraud and EWS checks. For UL/ML tenants these feed the statutory EWS framework (FRM paras 13–23, Part 8A.14), which prescribes no indicator list, so indicators are tenant-defined.
   - Fraud-debarment gate (FRM paras 35–39).
6. **Verification management:**
   - Field investigation (residence and office), personal discussion, technical valuation, legal title search and vetting, RCU.
   - Vendor allocation by rule.
   - Mobile reports with geo-tag and photos.
   - TAT and SLA; vendor billing and quality scoring.
7. **Deviations and delegation of authority:**
   - Deviation matrix by amount × product × deviation type × LTV/FOIR × risk grade.
   - Routes the file to the right sanctioning authority (a hierarchical committee where needed).
   - Every approval records the authority, the limit it used and the reasons.
   - The pre-sanction regulatory gates in Part 8A.16 (M4):
     - related-party routing and recusal (CRM paras 13G–13J);
     - exposure limits (CON);
     - own-share, own-debenture and IPO blocks;
     - LEI;
     - fraud debarment;
     - the microfinance classifier (CF para 51);
     - capture of age, occupation and income on digital loans, with no automatic limit increase (CF para 8);
     - a new-to-credit path, so no applicant is rejected only for lack of credit history (CIR para 38(5)).
8. **Credit Appraisal Memo (CAM):**
   - Template-driven CAM covering applicant profile, income and cash-flow analysis, banking summary, bureau summary, eligibility (FOIR/LTV/DSCR), collateral, risk assessment, deviations, terms and conditions, and recommendation.
   - **AI-assisted narrative drafting** with source citations to the underlying documents and data. It is editable and always reviewed by a human. The final CAM is versioned and locked at sanction.
9. **Sanction and offer:**
   - Sanction letter.
   - **KFS with APR** generated by the KFS engine. Show all charges and the repayment schedule. Use the standard RBI format and the borrower's language.
   - **KFS validity period (RBC para 29(2)):** the lender is bound by the KFS terms for at least 3 working days (tenor ≥ 7 days) or 1 working day (tenor < 7 days), and the borrower may accept at any time within it. This is **not** a waiting period, so do not block same-day execution. Store the KFS issue time, validity expiry and acceptance time.
   - MITC; co-lending blended rate disclosure; recovery-agent and grievance-officer details.
   - Charges not disclosed in the KFS cannot be levied without explicit consent; enforce this in the charges engine.
10. **Documentation and execution:**
    - Document checklist by product.
    - Loan agreement, sanction acceptance, guarantee deed, hypothecation deed, end-use undertaking (eSign-capable); DP note, power of attorney and MoD/mortgage deed (physical execution path).
    - eSign: Aadhaar OTP eSign or DSC.
    - eStamp and NeSL Digital Document Execution (DDE).
    - Physical signing path for documents the IT Act First Schedule excludes from electronic execution: negotiable instruments other than cheques (so **DP notes/promissory notes**), powers of attorney, trusts, wills, and contracts for the sale or conveyance of immovable property. Mortgage documentation follows state registration law.
    - Store signing evidence: provider transaction ID, certificate, signed hash, timestamp, signer identity and IP.
    - Automatic delivery of digitally signed documents to the borrower's verified email or phone. For digital loans this covers the KFS, product summary, sanction letter, T&C, account statements and privacy policies, on NBFC letterhead (CF para 9(3)).
    - Every loan agreement template includes the lender's right to commission an audit (FRM para 27).
    - **OTC/PDD tracking:** deferral approval, ageing and escalation.
11. **Disbursement:**
    - Disbursement memo with pre-disbursement conditions checklist.
    - Penny-drop name match on the beneficiary account.
    - Multi-tranche disbursement with stage/inspection reports.
    - Deductions at disbursement (fees, GST, insurance, BT payoff) shown transparently.
    - Payout through the bank API or payout provider, with UTR capture.
    - **Interest starts from the actual date of disbursement or cheque handover, never from sanction or agreement date** (RBI (NBFC – Miscellaneous) Supervisory Directions, 2026, para 7: no interest from sanction/agreement date or cheque date, no full-month interest for part months, and no advance instalments with interest charged on the full amount).
    - No EMI on undisbursed amounts (Finbyx design rule, consistent with para 7).
    - Cooling-off period handling for digital loans.
12. **Hand-off to LMS:** atomic loan-account creation with the schedule, opening GL entries, mandate link and welcome kit. For LOS-only tenants, use an export API to an external LMS.

## M5. Collateral management

- **Collateral types:** residential, commercial and industrial property; vehicles; gold and silver; listed shares and bonds; MF units; FDs and deposits; book debts and receivables; plant and machinery; guarantees (personal, corporate, CGTMSE/CGFMU-type).
- **Collateral lifecycle:**
  - acquisition;
  - ownership verification;
  - valuation and periodic revaluation;
  - charge creation (mortgage, hypothecation, pledge, lien);
  - **CERSAI filing** of creation, modification and satisfaction for every charge type in CRM para 27 (non-MODT mortgage; hypothecation of plant and machinery, stocks, book debts and receivables; intangibles; under-construction property agreements), on an ongoing basis (CRM para 28), within 30 days of creation under SARFAESI s.23 and the CERSAI Rules [VERIFY];
  - legal audit of title documents for facilities ≥ ₹1 crore until repaid (FRM para 53);
  - insurance with lender endorsement and renewal tracking;
  - custody (vault/storage register for original title documents and gold packets, with dual control);
  - substitution, partial release, invocation and sale;
  - final release.
- **LTV monitoring:** real-time for securities, gold-price-linked for gold, periodic for property. Margin-call workflow with cure period and auto-invocation rules (for example the 7-working-day cure for NBFC loans against shares, CF para 106).
- **Release of documents:**
  - Return original documents and clear charges (CERSAI satisfaction, depository unpledge, RTO Form 35 trigger) within **30 days** of full repayment or settlement.
  - Compensation calculator of **₹5,000 per day** of delay attributable to the lender.
  - Lost-document procedure.
  - Property documents: RBC paras 35–41 (₹5,000/day under para 39).
  - Gold/silver: same day, and in any case within 7 working days (RBC para 58).

## M6. Loan Management / Servicing (LMS)

- **Loan account (360° view):** schedule, ledger, balances by component, DPD history, classification history, mandates, collateral, documents, communications, complaints, collections activity, legal cases.
- **Schedules:** all Part 4.2A options. Regenerate the schedule with a full audit trail and keep previous versions.
- **Accruals:** daily interest accrual; penal charges as **charges, never penal interest, never capitalised** (RBC para 30 [VERIFY]).
- **Floating-rate resets:**
  - benchmark change propagation;
  - borrower option to change EMI or tenure, or to switch to a fixed rate;
  - no negative amortisation;
  - quarterly statements and communication.
  - Basis: RBC paras 31–32, which apply to EMI-based floating-rate personal loans. Extend the same controls to other floating products by policy.
- **Repayments:**
  - all channels (M7);
  - allocation per the product's strategy;
  - excess and advance handling;
  - unapplied/suspense receipts with resolution workflow.
- **Part-prepayment and foreclosure:**
  - quote generation valid to a date;
  - choice between reducing EMI and reducing tenure;
  - **prepayment-charge engine**, based on the RBI (Pre-payment Charges on Loans) Directions, 2025 (2 Jul 2025):
    - Scope: RBC para 34 for loans sanctioned or renewed on or after 1 Jan 2026; para 33 for earlier loans.
    - All NBFCs: no charge on floating-rate loans to individuals for non-business purposes.
    - Upper Layer: no charge on floating-rate business loans to individuals and MSEs.
    - Middle Layer: the same where the sanctioned amount is up to ₹50 lakh.
    - No lock-in period.
    - Inputs: rate type, borrower type, purpose, NBFC layer, sanction date and amount.
    - Disclose any permitted charge in the KFS, sanction letter and agreement.
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
- **Payment gateways:** Razorpay, Cashfree and PayU behind one `PaymentGateway` interface (Juspay as an optional orchestration layer).
  - **Stripe and PayPal:** keep the adapter interfaces you requested, but research shows Stripe is invite-only in India and PayPal has exited domestic Indian payments. Use them only for cross-border or SaaS-subscription billing, not domestic EMI collection. Record this decision in an ADR.
- **Disbursement rails:** bank corporate APIs (ICICI, HDFC, Axis, Yes, IDFC First and others) and payout providers (RazorpayX, Cashfree Payouts), with maker-checker, beneficiary validation, duplicate-payment prevention and UTR reconciliation.
- **Reconciliation:**
  - Three-way: provider/bank statement ↔ payment record ↔ loan ledger.
  - Auto-match rules, exception queue, suspense ageing.
  - **Never treat an API "success" response as final without settlement confirmation.**
  - Daily reconciliation with each sponsor bank, gateway, LSP and co-lender; payment-network, gateway and aggregator reconciliation within 24 hours of receiving the settlement file (DPS para 57 baseline).
  - Payment fraud rules: velocity, new account, geo/IP, mule VPA, declined transactions (DPS para 53 baseline). Card data stored only in tokenised form (DPS para 69(4)(v)).

## M8. Collections (pre-due to 90+ DPD)

- **Segmentation and strategy:**
  - risk and propensity scoring;
  - pre-due nudges;
  - bucket-wise strategies (X, 1–30, 31–60, 61–90, NPA);
  - champion/challenger.
  - DPD changes in COB automatically trigger strategy actions, so flags always lead to action.
- **Allocation:** rule-based allocation to digital channels, telecallers, field staff and agencies by pincode, bucket, product, ticket size and performance. Includes re-allocation and capacity limits.
- **Contact channels:** SMS (TRAI DLT-registered templates and headers), WhatsApp Business (Meta Cloud API templates), email, IVR/voicebot, predictive dialer, field visits.
- **Contact-policy engine** (effective-dated rule pack, with separate windows for recovery and for sales/marketing):
  - **Until 31 Dec 2026 (RBC paras 89–100):**
    - recovery calls only between 08:00 and 19:00 (para 100);
    - microfinance 09:00–18:00 (para 91(2)).
  - **From 1 Jan 2027:** the RBI (NBFC – Responsible Business Conduct) Third Amendment Directions, 2026 (6 Aug 2026; RBI/2026-27/230) delete paras 89–100 and insert Section J (paras 100A–100AB). Under the new rules:
    - recovery contact only between 08:00 and 19:00 (para 100Y(4)) [VERIFY whether a separate MFI window survives];
    - **record every recovery call**: all outbound calls, and inbound calls to the number the NBFC provided. Inform the borrower, and keep recordings for 6 months, or until disposal if the matter is sub judice (para 100P);
    - every agent must hold the **IIBF debt-recovery-agent certificate**; existing agents have one year to obtain it (para 100I);
    - give the borrower the assigned agency's details at least 1 day before the first visit (para 100L);
    - visit the residence or workplace only where no meeting place was chosen, or where the borrower failed to appear at the chosen place on two or more successive occasions (para 100Y(5); para 100Y(7) for microfinance centre collection);
    - include grievance-officer details on recovery communications;
    - device-lock rules for financed devices (paras 100S–100U: DPD gates, prompt unlock, compensation for delayed unlock) [VERIFY figures].
  - **Sales/marketing contact window:** 09:00–19:00 under the RBC Second Amendment (para 101N(4)). Keep it separate from the recovery window.
  - **Always:** frequency caps; no contact with unrelated third parties; language and respect rules.
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
- **Borrower communications at default:**
  - Send SMS/email alerts to the borrower **while** default/DPD data is submitted to CICs — with each reference-date file, wherever mobile/email is available (CIR para 34(1)(i)).
  - Log each alert against the CIC submission record.
  - On digital loans, send the recovery agent's particulars before first contact (CF para 9(6)).
  - Post cash recoveries in full to the borrower's account the same day (CF para 10(5)).

## M9. Recovery and legal

- **Legal case management:** case master, advocate empanelment and fees, hearing calendar, eCourts CNR sync, documents and orders, cost tracking, outcomes.
- **Statutory workflows with timelines and templates:**
  - **Sec 138 NI Act / Sec 25 PSS Act:** cheque or mandate dishonour → demand notice within 30 days → 15-day wait → complaint within the limitation period.
  - **SARFAESI 2002 (built with the secured products in Phase 17):** eligibility gate (for NBFCs, asset size ≥ ₹100 crore and secured debt ≥ ₹20 lakh) → NPA check → 13(2) notice (60 days) → representation handling within the prescribed time → 13(4) possession notice and publication → Sec 14 CMM/DM application → possession → valuation → sale notice (Rule 8(6)/9) → e-auction → sale certificate → surplus refund.
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
  - an approval matrix, with related-party recusal (CRM para 13J), and the settlement restrictions for wilful defaulters from the Resolution of Stressed Assets / Wilful Defaulters Directions [VERIFY]. Settling a fraud account starts the 5-year debarment clock (FRM para 35);
  - settlement letter;
  - payment plan tracking;
  - **CIC reporting of settlements:** "settled" only where principal or interest was waived for financial inability, reported with the reason and the settlement amount; wrong debits and contested charges are reported as "disputed" (CIR paras 12(2), 12(4)). IBC-admitted cases are reported as suit-filed (para 12(7));
  - **SARFAESI possessed-asset website feed:** assets possessed under s.13(4) on or after 25 Sep 2023, in the Annex IV columns; updated monthly; removed on sale or full settlement (CIR para 21);
  - no sale to other lenders or ARCs while a fraud investigation is open (FRM para 54).
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
   - Impairment Reserve, appropriated from profit after tax where the Ind AS 109 allowance is below IRACP. It is not regulatory capital and cannot be withdrawn without DoS permission (FS para 12(2)).
   - IRACP-vs-Ind AS table (FS 21(15)).
   - Register of > 90 DPD accounts not treated as impaired, and of SICR rebuttals (never beyond 60 DPD), with Audit Committee approvals (FS 12(1)).
   - **For banks:** the RBI (Commercial Banks – Asset Classification, Provisioning and Income Recognition) Directions, 2026, effective 1 Apr 2027, with ECL stages and floors [VERIFY].
6. **Taxes:**
   - GST invoices and credit notes for fee income, with HSN/SAC and place of supply;
   - GSTR-1 data extract;
   - e-invoicing: banks, NBFCs and other financial institutions are exempt under Notification 13/2020-Central Tax (21 Mar 2020, as amended). Keep the IRP adapter optional for non-exempt group entities;
   - TDS on vendor/DSA payments with 26Q/24Q extracts;
   - TDS receivable on interest.
7. **Bank and treasury:**
   - bank accounts master;
   - automated bank reconciliation (statement import, H2H and API feeds);
   - cash and vault management for branches;
   - fund transfers between accounts with maker-checker.
7A. **Investment portfolio** (INV Directions, Part 8A.5):
    - security master;
    - classification at acquisition per the accounting standard;
    - non-Ind AS valuation, and inter-class transfers only on 1 April / 1 October;
    - income recognition;
    - AIF look-through, with a 30-day exit or 100% provision;
    - OTC bond trade reporting within 15 minutes;
    - hedge-only flags;
    - every investment feeds the exposure engine.
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
   - financial statements (Balance Sheet, P&L, Cash Flow) per the RBI (NBFC – Financial Statements: Presentation and Disclosures) Directions, 2025 and Schedule III to the Companies Act, 2013 (Division III for Ind AS NBFCs; Division I for non-Ind AS NBFCs);
   - the disclosure engine under the FS Directions (Part 8A.8): Annex I Schedule; C.1 items for all NBFCs; C.2 for ML/UL; C.3 for UL; versioned templates with comparatives and nil-line suppression; quarterly website publications as scheduled jobs with evidence;
   - other notes: gold/silver loans as % of total assets (CF para 50); fraud amount (FRM para 12); loans to directors, senior officers and relatives (CRM Annex I; FS 21(11)); related-party loans (FS 21(9A)).
10. **Accounting integrations:**
    - **TallyPrime** (native JSON import/export since TallyPrime 7.0, Dec 2025; XML over HTTP remains supported): through a **local connector agent** on the client's Tally machine, because Tally has no built-in API authentication. Push vouchers, ledgers and masters; reconcile.
    - **SAP S/4HANA** (OData Journal Entry APIs) and SAP Business One (Service Layer).
    - **Zoho Books.**
    - Configurable export formats (Excel/CSV/XML/JSON) for any other system.

## M11. Co-lending, direct assignment and securitisation

- **Co-lending:** Co-Lending Arrangements Directions, 2025 (6 Aug 2025, effective 1 Jan 2026), now Part B of the RBI (NBFC – Transfer and Distribution of Credit Risk) Directions, 2025. The engine must handle:
  - partner master and agreements;
  - minimum 10% retention by each lender;
  - partner share booked within 15 calendar days, otherwise it stays with the originator;
  - an escrow account with a bank for all flows, controlled only by the co-lenders (CF para 10, Note);
  - a single blended rate to the borrower: the funding-share-weighted average of each lender's rate, with any other fees reflected in the APR and KFS;
  - partner-level income splits per the agreement;
  - **borrower-level SMA/NPA sync across partners by the next working day**;
  - each lender's own CIC reporting;
  - DLG only by the originator, capped at 5% [VERIFY in the Transfer and Distribution of Credit Risk Directions; CF para 19 permits DLG only from an LSP, or a lender engaged as LSP];
  - the list of active co-lending partners published on the website (FS para 21(4));
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
  - **exposure engine and concentration limits** (CON Directions, Part 8A.4):
    - BL Board limits, plus unsecured consumer-credit sub-limits monitored by the RMC (paras 6–9);
    - ML single/group 25% / 40% of Tier 1, IFC 30% / 50%, plus 5% / 10% for infrastructure (paras 13–14);
    - exposure computation, CRT offsets and exemptions (paras 17, 20–23);
    - sensitive-sector limits (para 24);
    - group-of-connected-counterparties logic (para 4(3));
  - **UL only — Large Exposure Framework:** single 20% (25% hard cap; 30% for IFC), group 25% (IFC 35%; +10% infrastructure); immediate breach report to RBI and an automatic block on new exposure (paras 33–46); monthly Return on Large Exposures (para 48);
  - CDS hedge register (CRM paras 16–17);
  - EWS (bureau refresh triggers, bounce patterns, GST-filing gaps, adverse news).
- **Liquidity and ALM** (ALM Directions, Part 8A.7):
  - applicability resolver: Ch II if assets ≥ ₹100 crore; LCR for NBFC-D and NBFC-ND ≥ ₹5,000 crore; never CICs;
  - the 10-bucket master, and a versioned slotting engine for every Annex II/III rule;
  - tolerance limits on net cumulative negative mismatch: 10% (1–7 days), 10% (8–14 days), 20% (15–30 days), plus Board limits to 1 year, with breach alerts;
  - STDL; stock ratios; funding-concentration tables; IRS gap and earnings-at-risk;
  - behavioural assumptions approved by ALCO/Board;
  - stress tests; contingency funding plan; encumbrance register; FTP;
  - a **daily** LCR engine (HQLA haircuts 0% / 15% / 50%; outflows × 115%; inflows × 75% capped at 75% of outflows; ≥ 100%), with an immediate report to DoS if HQLA is used under stress.
- **Capital:** CRAR, Tier 1/Tier 2 and risk-weighted assets per the RBI (NBFC – Prudential Norms on Capital Adequacy) Directions, 2025 [VERIFY]; leverage.
- **ICAAP data mart:** inputs for credit, concentration, operational, market/IRRBB, liquidity, reputational, strategic, ESG and cyber risk assessments; stress scenarios; RAG (traffic-light) indicators against the Risk Appetite Statement.
- **Operational risk:**
  - loss-event database;
  - RCSA (risk and control self-assessment);
  - KRIs (key risk indicators);
  - aligned with the RBI Guidance Note on Operational Risk Management and Operational Resilience [VERIFY 2025 version].
- **Fraud risk management** (FRM Directions, Part 8A.14; UL, ML, and BL ≥ ₹500 crore on the audited 31 March balance sheet; HFC reporting goes to NHB):
  - **EWS (UL/ML only):** tenant-defined indicators; integrated with COB and real-time events; every alert gets a recorded decision; effectiveness reports to the RMC. The NBFC Directions have **no RFA category** — do not build one for NBFC/HFC tenants.
  - **Case lifecycle:** suspected → investigation (internal or external audit, with auditor timelines) → show-cause notice → at least 21 days' response window (system-enforced) → examination → reasoned order → classified / not fraud → FMR → FUA → closure or withdrawal.
  - Occurrence, detection and classification dates are captured separately.
  - **Clocks:** FMR within 14 days of classification, irrespective of amount; law-enforcement report immediately, mandatory at ₹1 lakh or more; staff accountability opened for every case.
  - **Routing:** SCBMF or Committee of Executives; ACB track with recusal for senior executives; ABBFF flag for Government NBFCs at ₹3 crore or more; examination of group companies.
  - **Withdrawal:** director-rank approval or a court direction.
  - **Closure:** after disposal and staff accountability, or the ₹25 lakh / 3-year statistical rule; closure files kept for auditors.
  - **Debarment register:** 5 years from full repayment or settlement, covering associated entities.
  - **Transfer gate:** no transfer while an investigation is open.
  - **RBR:** theft, burglary, dacoity and robbery reports (7 days; quarterly).
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
| **CIC data submission** (TransUnion CIBIL, Experian, Equifax, CRIF High Mark) in the Uniform Credit Reporting Format (consumer, commercial, MFI) | Effective-dated calendar (CIR para 10(2)): fortnightly as on the 15th and month-end, within 7 days, until 30 Jun 2026. From 1 Jul 2026 (RBI/DOR/2025-26/117): the 9th, 16th and 23rd (incremental, within 4 calendar days) and month-end (full file by the 5th); a DPD change alone triggers an incremental record. Rejections: within 7 days until 30 Jun 2026; afterwards before or along with the next reference-date file (para 15). Last-instalment repayments and closures always reported (para 10(3)). CKYC number reported where available (para 12(10)). DLA loans of every tenor reported (CF para 17). MFI household income reported (CF para 54). Pre-submission validation of mandatory fields; catalogues per CIC; DQI half-yearly (CIR 15–17). Alerts to borrowers while reporting default (para 34(1)(i)). Full detail in Part 8A.2 |
| **CRILC** | Upper and Middle Layer NBFCs, and Base Layer ICC/MFI/Factor NBFCs with assets ≥ ₹500 crore (Supervisory Returns Directions, 2026) |
| **CIMS / XBRL returns** | DNBS series (financial, prudential, ALM (DNBS4A/4B), sectoral, branch info, statutory auditor certificate and others), per the RBI (NBFC – Supervisory Returns) Directions, 2026 (31 Jul 2026; RBI/DoS/2026-27/466). HFCs are excluded (they file NHB returns). Monthly returns are due within 15 days and quarterly returns within 21 days. DNBS04A (quarterly) and DNBS04B (monthly) apply to every in-scope NBFC with assets ≥ ₹100 crore, in the Annex IV formats (ALM paras 57–59) [VERIFY the full return list against the Supervisory Returns Directions] |
| **Fraud Monitoring Returns (FMR)** | Per case, from the fraud module, irrespective of amount, immediately and not later than 14 days from classification; updates via FUA; group-entity frauds by email to fmgconbfc@rbi.org.in (FRM paras 42–45). HFCs report to NHB |
| **RBR (theft, burglary, dacoity, robbery)** | Incident report by email within 7 days; quarterly return within 15 days of quarter-end (FRM paras 57–58) |
| **Return on Large Exposures (UL)** | Monthly, Annex I sections A–D (CON para 48); breach intimation immediately (para 45) |
| **CDS / CRT excess-exposure report** | Quarterly to the DoS Regional Office (CRM para 17(7)) |
| **IRF data** | Half-yearly, within 1 month (INV para 29) |
| **Pledged-shares report** | Quarterly to stock exchanges, Annex-III format (CF para 106) |
| **Public liquidity disclosure** | Quarterly on the website and in the notes (ALM para 15, Annex I; FS 21(13)) |
| **LCR disclosure** | Quarterly, from daily LCR values (FS C.2(32)) |
| **DNBS10 Statutory Auditor's Certificate** | Enable the auditor to file within 5 working days of signing, and by 31 December at the latest (AUD para 6) |
| **Branch-closure intimation (deposit-taking)** | To the RBI/NHB Regional Office within 7 days of the notice (BR para 12) |
| **FIU-IND** | STR, CTR, CCR, NTR (FINnet 2.0 formats) |
| **DLA/LSP reporting on CIMS** | Annex-I format, one line per DLA per platform; updated on addition or cessation; CCO or Board-designated certification of the four para 18(4) points (CF para 18). No "RBI-approved" wording in DLA marketing (para 18(6)) |
| **NHB returns** (HFCs) | As applicable |
| **Co-lending, DA and securitisation disclosures** | FS 21(4) (website list of active co-lending partners, plus notes), 21(5) (STC / non-STC), 21(6) (quarterly loan-transfer disclosures) |
| **Board and committee packs** | Audit, Risk, ALCO, IT Strategy and Customer Service committees |
| **Statutory and tax** | GST, TDS, Form 26AS reconciliation |

## M14. Compliance module (embedded) and LawDocsComply bridge

- **Mode switch per tenant or group:**
  - (a) embedded compliance inside Finbyx;
  - (b) LawDocsComply as the GRC system, with Finbyx pushing evidence and pulling obligations;
  - (c) group-level LawDocsComply covering several Finbyx entities;
  - (d) separately, a grievance-module host switch: Finbyx M15 or LawDocsComply, with Equator referral available from either.
- **Compliance Function workflow suite** for ML/UL tenants (CMP paras 6–33; Part 8A.11), offered to all tenants:
  - annual compliance risk assessment and Board review generator;
  - product and process approval gate, with 6-month new-product monitoring;
  - compliance testing;
  - RMP/MAP tracker;
  - CCO governance register and SSM intimations;
  - recorded deviation approvals;
  - unified dashboard.
- **Applicability engine** driven by the entity regulatory profile (Part 8A.16).
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
- **Credit-information complaints** (CIR paras 18–19, 34–35; Part 8A.2):
  - two clocks: the lender's 21 days to send corrected data, and 30 days overall;
  - ₹100 per calendar day compensation, apportioned between the parties;
  - payout within 5 working days;
  - rejection reasons taken from the CIC list;
  - correction at source;
  - half-yearly root-cause analysis.
- **Digital-loan grievance text** (CF para 12): nodal officers at the lender and LSP; escalation to CMS or CRPC after 30 days or on rejection.
- **Internal Ombudsman (where applicable; HFCs excluded)** under the **RBI (NBFC – Internal Ombudsman) Directions, 2026 (14 Jan 2026)**: automatic escalation of wholly or partly rejected complaints to the IO within 20 days, and the final response within 30 days. The complaint system must be fully automated.
- **Reserve Bank – Integrated Ombudsman Scheme, 2026 (RB-IOS 2026)** (effective 1 Jul 2026, replacing the 2021 Scheme):
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
  - sales feedback within 30 days of sale under the RBC Second Amendment (para 101Y, effective 1 Jan 2027).

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
- **Consent, preference and DND management**, honouring the **RBI (NBFC – Responsible Business Conduct) Second Amendment Directions, 2026** (15 Jun 2026; Chapter IIIA on sales and marketing; effective 1 Jan 2027):
  - explicit consent with "No" as the default (para 101I);
  - ban on the listed dark patterns (para 101X, Annex III);
  - no compulsory bundling (para 101V);
  - marketing contact only 09:00–19:00 (para 101N(4));
  - consent records retained.

## M19. Administration, configuration and workflow

- **Users and roles:** RBAC plus ABAC (attribute-based: amount limits, branch scope, product scope); segregation-of-duties checks; maker-checker per permission.
- **Access security:** MFA; session policies; IP allow-lists; device binding for the field app; delegation and leave substitution; break-glass access with audit.
- **Visual workflow designer for tenant workflows**, within guard-rails, with versioned deployment.
- **Regulator and auditor access:** read-only "RBI Supervisor" and "Auditor (audit-mode)" roles over MIS, audit trails and evidence; time-boxed; provisioned by maker-checker (CYB paras 46, 57).
- **Critical-action controls:** MFA (CYB para 115); delegated authority for key-parameter changes such as interest rates (CYB para 21(3)); unauthorised-activity logging (CYB para 21(8)).
- **Ecosystem SSO (optional):** one Infrabyx OIDC identity across Finbyx, Udofin portals, LawDocsComply and Equator for users who need several products. Authorisation stays per product.
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
- an India-region inference endpoint, for example AWS Bedrock in ap-south-1 using in-region models only (no cross-region inference profiles), or an approved provider with a data-processing agreement and India residency [VERIFY per provider].

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
- remote wipe of app data;
- distribution through managed Play Store/App Store or MDM, with a forced-update policy for incompatible versions;
- DPS para 68 mobile controls as the baseline: server-side version check; one live version, with older versions disabled within 6 months; root/jailbreak and remote-access detection; device binding with device register and new-device alerts; re-authentication at launch and after idle; no credentials or keys on the device; encrypted local database; certificate pinning; obfuscation.

## M23. Borrower self-service portal (optional per tenant)

A lean, mobile-first web portal for lenders that do not use Udofin:

- loan summary;
- schedule;
- payments;
- statements and certificates;
- service requests;
- complaints with escalation path;
- consent and privacy dashboard (view, withdraw, data-rights requests);
- a "books of account" view of the borrower's payments and charges, for transparency;
- **payment-security profile** (mandatory for card-issuing tenants, default-on for others; DPS paras 41–67):
  - MFA with one dynamic factor for payments and for bank/mobile/email changes;
  - alerts on every debit and credit;
  - lockout after failed attempts;
  - session-termination handling;
  - inactivity timeout;
  - non-skippable secure-usage guidance;
  - an in-app "report as fraud" button;
- **DLA data limits** (CF paras 13–14): no access to files, contacts or call logs; one-time camera/microphone/location access for KYC only; no biometric storage unless statute allows; data processed abroad deleted and repatriated within 24 hours.

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
5. On **28 November 2025**, RBI repealed 9,445 circulars and issued 244 entity-wise Master Directions. On **31 July 2026** it issued **64 Department of Supervision Directions**, repealing a further 628 circulars. Older circular references are legacy. Cite the new Directions, and keep the legacy reference only for traceability.

## 8.2 Starting register

All items need confirmation against the primary text.

| Area | Instrument (NBFC version; use the bank/UCB counterpart per tenant. CF, CIR, CRM, CON, INV, ALM, FS, CYB and FRM apply to HFCs directly) | Software controls |
|---|---|---|
| Scale-based regulation | RBI (NBFC – Registration, Exemptions and Framework for Scale Based Regulation) Directions, 2025, as amended 2026 (Upper Layer threshold of ₹1 lakh crore assets; Unregistered Type I NBFC category) | Entity profile drives applicability of every rule |
| Digital lending | RBI (NBFC – Credit Facilities) Directions, 2025 (RBI/DOR/2025-26/347), Chapter III (paras 6–30; DLG paras 19–29) | Direct disbursal and repayment (para 10); KFS; Board-set cooling-off of at least 1 day (para 11); DLA/LSP lists; consent; India-only storage; DLG ≤ 5% of amount disbursed out of the covered portfolio (para 24), invoked within 120 days overdue (para 27) |
| Gold and silver loans | Credit Facilities Directions, Ch IV (paras 32–50; para 31 deleted w.e.f. 1 Apr 2026: eligibility, valuation, LTV, caps, bullet loans, disclosure); RBC Ch III.G (paras 42–75: release para 58, auction paras 60–66) | LTV slabs, quantity caps, valuation, auction, release |
| Loans against securities | Credit Facilities Directions, Chapter VIII (paras 104–106, Annex-III) | Loans against listed shares by NBFCs ≥ ₹100 crore: 50% LTV, 7-working-day cure, Group 1 where applicable, quarterly pledge reporting; no loans against own shares; IPO cap ₹1 crore |
| Interest, KFS, penal charges, prepayment, resets, document release, recovery agents | RBI (NBFC – Responsible Business Conduct) Directions, 2025 (paras 22–24, 29 + Annex I, 30, 31–32, 33–34, 35–41, 42–75 gold/silver, 81, 89–100, 103); RBC Second Amendment Directions, 2026 (15 Jun 2026; Chapter IIIA sales and marketing; effective 1 Jan 2027); RBC Third Amendment Directions, 2026 (6 Aug 2026; Section J, paras 100A–100AB replacing paras 89–100; effective 1 Jan 2027) | KFS/APR engine with validity period; penal-charge rules; prepayment-charge engine; reset options; release SLA and ₹5,000/day compensation; contact-policy guard-rails; call recording; agent certification |
| Interest computation; Core Financial Services Solution | RBI (NBFC – Miscellaneous) Supervisory Directions, 2026 (para 7; Chapter II) | Interest only from actual disbursement or cheque handover; no full-month interest for part months; no advance instalments with interest on the full amount (para 7). Design rules beyond para 7: no EMI on undisbursed amount; no undisclosed schedule change. **CFSS:** mandatory for UL and ML NBFCs with ≥ 10 fixed-point service delivery units. Finbyx must provide the CFSS features — digital customer interface, integrated functions, centralised database and accounting, regulatory MIS — and support quarterly progress reporting to the SSM |
| IRACP | RBI (NBFC – Income Recognition, Asset Classification and Provisioning) Directions, 2025 (paras 18–19 day-end tagging; 22–25 upgrade rules; 32 doubtful; 34–35 Ind AS / Impairment Reserve; 38 income; 48/55/58 standard-asset provisions) | COB classification engine; borrower-level NPA; provisioning engine |
| Stressed assets | RBI (NBFC – Resolution of Stressed Assets) Directions, 2025 | Restructuring flags, resolution plans, compromise settlements, technical write-off |
| Board credit policy | CF Ch II para 5 | Policy registry linking every product to the approved credit-policy version |
| Microfinance; project finance; demand/call; CRE; PCE | CF Ch V (51–62), Ch VI (63–79), paras 107–111, Ch VII (80–103) | Products 11, 20, 21; housing/CRE classification; PCE limits for ML+ |
| Credit risk | RBI (NBFC – Credit Risk Management) Directions, 2025 (RBI/DOR/2025-26/350; amended 5 Jan 2026, effective 1 Apr 2026) | Related-party register, threshold-based sanction and recusal (13A–13Q); own-share/own-debenture blocks (14–15); Notified-NBFC appraisal (6–8); CDS (16–17); LEI gate (19–24); CERSAI (25–28) |
| Concentration risk | RBI (NBFC – Concentration Risk Management) Directions, 2025 (RBI/DOR/2025-26/351; amended 1 Jan and 10 Mar 2026) | BL limits, consumer sub-limits, vehicle top-ups as unsecured, IPO cap (6–11); ML 25/40 and IFC 30/50 of Tier 1, exemptions, CRT, SSE (13–24); UL LEF, monthly return, breach block (25–49) |
| Investments | RBI (NBFC – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 (RBI/DOR/2025-26/354) | Classification per accounting standard; non-Ind AS valuation and transfer rules; AIF look-through; trade reporting (7–34) |
| Branches | RBI (NBFC – Branch Authorisation) Directions, 2025 (RBI/DOR/2025-26/342; amended 15 Apr 2026) | Deposit-taking state gate (6); no overseas branch (10); 3-month closure notice (11); 7-day intimation (12); representative office via PRAVAAH (13–15) |
| KYC/AML | RBI (NBFC – Know Your Customer) Directions, 2025, as amended 29 Dec 2025; PMLA 2002 and PML Rules 2005 | CKYC, V-CIP, periodic updation, screening, FIU-IND, 5-year retention |
| Credit information | RBI (NBFC – Credit Information Reporting) Directions, 2025 (RBI/DOR/2025-26/349), as amended by RBI/DOR/2025-26/117 (4 Dec 2025; effective 1 Jul 2026: paras 10(2), 12(10), 15, Annex VI) | Membership of all 4 CICs (6); UCRF Annex I (9); effective-dated reference dates (10(2)); settled/disputed (12(4)); IBC = suit-filed (12(7)); CKYC (12(10)); rejections (15); DQI (17); correction at source (18–19); CIRs in credit policy (20); SARFAESI website display (21); alerts while reporting (34(1)); CIC nodal officer (34(2)); RCA (34(4)); compensation (35); no auto-rejection of new-to-credit (38(5)) |
| Co-lending and loan transfers | RBI (NBFC – Transfer and Distribution of Credit Risk) Directions, 2025 (Part B: Co-Lending Arrangements, originally issued 6 Aug 2025, effective 1 Jan 2026) | M11 co-lending engine |
| Securitisation | RBI (NBFC – Securitisation Transactions) Directions, 2025 | MHP/MRR, pools, servicing |
| Outsourcing | RBI (NBFC – Managing Risks in Outsourcing) Directions, 2025 | Outsourcing register, due diligence, contracts, audit rights |
| ALM | RBI (NBFC – Asset Liability Management) Directions, 2025 (RBI/DoR/2025-26/355) | Ch II for assets ≥ ₹100 crore; buckets (32, 49); tolerance limits (39–40); stock ratios (43); IRS (45–53); behavioural assumptions (54–55); DNBS04A/04B (57–59); LCR (Ch III, 60–78); public disclosure (15, Annex I) |
| Capital | RBI (NBFC – Prudential Norms on Capital Adequacy) Directions, 2025 [VERIFY — not yet supplied] | M12 |
| Green deposits | RBI (NBFC – Climate Finance and Management of Climate Change Risks) Directions, 2025 (RBI/DOR/2025-26/364); NBFC-D and deposit-taking HFCs only | Deposits module (later): green-deposit flag, taxonomy tags, HQLA parking, allocation ledger, verification and impact reports, Board review within 3 months (paras 6–18) |
| Wilful defaulters | RBI (NBFC – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 | M9 workflow and reporting |
| Financial statements | RBI (NBFC – Financial Statements: Presentation and Disclosures) Directions, 2025 (RBI/DOR/2025-26/359; updated 1 Apr 2026) | Ind AS governance registers (12(1)); Impairment Reserve (12(2)); Annex I Schedule (20); C.1 21(1)–(15) incl. (9A); C.2 for ML/UL incl. LCR disclosure; C.3 for UL; consolidation (Ch IV) |
| HFC | RBI (Housing Finance Companies) Directions, 2025, plus NHB requirements | HFC product rules and returns |
| Account Aggregator | RBI (NBFC – Account Aggregator) Directions, 2025 (RBI/DoR/2025-26/368; governs NBFC-AAs); ReBIT specifications as updated (para 33) | Tenant is the FIU: consent artefact (17), revocation (20), auditable logs (21), use only per artefact (28), FIP obligation for deposit-takers (29) |
| Cyber and IT | **RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 (31 Jul 2026; RBI/DoS/2026-27/461)**, which repeal the existing NBFC IT Framework and IT Governance instructions listed in circular DoS.CO.PPG.66/11.01.005/2026-27 (para 155; the 2023 MD is not named [VERIFY]) | Ch II all; Ch III for BL < ₹500 crore and all CICs; Ch IV for BL ≥ ₹500 crore; Ch V for TL/UL/ML excluding CICs. Audit trails (21(8); 109–111; vendor admin logs 62(2)(i)); MFA for privileged users and critical activities (115); STP without manual edits (119); RBI read-only MIS access and audit-mode access (46, 57); for Ch V entities, VA 6-monthly and PT annually for critical systems (para 121) and half-yearly DR drills (para 129); incident reporting within 6 hours (paras 28/141); source code or escrow (para 105) and vendor no-vulnerability certificate (para 106); ITSC every 6 months (Ch IV) or quarterly (Ch V) |
| Digital payment security | RBI (NBFC – Digital Payment Security Controls) Directions, 2026 (RBI/DoS/2026-27/462); **credit-card-issuing NBFCs only** | MFA with a dynamic factor (41); alerts on all debits and credits and on detail/limit changes (46); lockout (50–51); fraud rules (52–53); reconciliation within 24 hours (57); secure-usage guidance (58); in-app fraud flag (66); web and mobile controls (67–68); card data (69); VA/PT and escrow (31–32). Voluntary baseline for all other tenants |
| Fraud | RBI (NBFC – Fraud Risk Management) Directions, 2026 (31 Jul 2026; RBI/DoS/2026-27/463) | Applies to UL, ML, and BL ≥ ₹500 crore; three dates (4); show-cause ≥ 21 days and reasoned order (6); SCBMF/CoE (8); EWS for UL/ML (13–23); debarment (35); law enforcement (40); FMR within 14 days (43); closure (50–52); legal audit ≥ ₹1 crore (53); transfer gate (54); RBR (57–58) |
| Supervisory returns | RBI (NBFC – Supervisory Returns) Directions, 2026 (31 Jul 2026; RBI/DoS/2026-27/466; HFCs excluded) | M13 returns |
| Compliance function | RBI (NBFC – Compliance Function) Directions, 2026 (RBI/DoS/2026-27/460); **ML/UL only** | Annual compliance risk assessment and review (6–7); product/process approval (9(7), 31); 6-month monitoring (15(2)); compliance testing (15(3)); RMP/MAP tracker (15(4)); CCO tenure, SoD and SSM intimation (21–29); workflow tool with deviation approvals and unified dashboard (32). No CCO certification is prescribed here |
| Auditor's report | RBI (NBFC – Auditor's Report) Directions, 2026 (RBI/DoS/2026-27/468); FY ending on or after 31 Jul 2026; HFC auditors excluded | Evidence packs for paras 6–8 (PBC, NOF, deposits, CRAR/DNBS03, IRACP, MFI classification); DNBS10 support; exception-report register (11) |
| Grievances | RBI (NBFC – Internal Ombudsman) Directions, 2026 (14 Jan 2026); Reserve Bank – Integrated Ombudsman Scheme, 2026 (RB-IOS 2026; effective 1 Jul 2026) | M15 |
| Bank ECL (bank tenants) | RBI (Commercial Banks – Asset Classification, Provisioning and Income Recognition) Directions, 2026 (effective 1 Apr 2027) | Bank ECL engine |
| Data protection | Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025 (notified Nov 2025; Consent Manager provisions from Nov 2026; most obligations from May 2027) | Notice and itemised consent, withdrawal, consent-manager integration, breach intimation to the Board and affected principals without delay, then a detailed report to the Board within 72 hours, security safeguards, 1-year log retention, erasure when purpose ends unless law requires retention, data-principal rights within the prescribed time, retention-rules engine resolving conflicts with PMLA/RBI/CIC retention |
| Aadhaar | Aadhaar Act and Regulations; UIDAI Circular No. 14 of 2025 (Aadhaar Data Vault; supersedes Circular 8 of 2025) | Vault hosted on-premises, on GCC, or as ADV-as-a-service; FIPS 140-2 L3+ HSM; reference keys; masking |
| Electronic records | Information Technology Act, 2000 (s.3A eSign, Second Schedule; the First Schedule excludes negotiable instruments other than cheques (for example DP notes), powers of attorney, trusts, wills, and contracts for the sale or conveyance of immovable property); state stamp Acts (e-stamping through SHCIL); NeSL DDE and IU under IBC s.215 | Signing evidence; physical paths for excluded instruments; stamp-duty by state |
| Recovery law | SARFAESI Act 2002 and Security Interest (Enforcement) Rules 2002 (NBFC eligibility: assets ≥ ₹100 crore and debt ≥ ₹20 lakh); NI Act s.138; Arbitration and Conciliation Act 1996; IBC 2016; Legal Services Authorities Act (Lok Adalat) | M9 workflows |
| Accounting | Ind AS 109, 107, 115, 24 and others; Schedule III to the Companies Act, 2013 (Division III for Ind AS NBFCs; Division I otherwise); ICAI guidance | M10 |
| AI | RBI FREE-AI Framework (Aug 2025); draft Guidance on Model Risk Management (Jun 2026) | M20 governance |

---

# PART 8A — REQUIREMENTS FROM THE RBI DIRECTIONS SUPPLIED BY THE PROJECT OWNER (verified against the official text)

## 8A.0 How to use this Part

The project owner supplied the official RBI PDFs for the 15 Directions listed in 8A.0.2. Each was read in full, and the paragraph citations in this Part come from that text.

### 8A.0.1 Rules for Claude Code

1. **Store the source texts.** Save the supplied PDFs in the repository under `docs/regulations/rbi/` (file name = RBI number, e.g. `RBI-DOR-2025-26-347.pdf`). Record a SHA-256 hash and the "updated as on" date of each in `docs/regulations/index.md`.
2. **Give every requirement an ID.** Load each requirement below into the regulatory register (M14) with the ID format `REQ-<code>-<para>`, for example `REQ-CF-10(1)`, `REQ-CIR-35(2)` or `REQ-CYB-121`.
   - Codes: CF, CIR, CRM, CON, INV, BR, ALM, FS, CLM, AA, CMP, CYB, DPS, FRM, AUD.
   - Every rule pack, control test and golden test must reference these IDs.
3. **Status of [VERIFY] items.**
   - These paragraphs are **verified** for the copies supplied.
   - Remove any [VERIFY] elsewhere in this prompt that a citation here resolves.
   - **Do not** treat amendments issued after a copy's "updated as on" date as verified; check them separately.
4. **More Directions will follow.** The project owner will supply the remaining Directions (IRACP, RBC, KYC, Resolution of Stressed Assets, Capital Adequacy, Transfer and Distribution of Credit Risk, Securitisation, Outsourcing, Wilful Defaulters, Supervisory Returns, Miscellaneous Supervisory, Scale Based Regulation, HFC and others). Add each one to this Part in the same format.
5. **Drafting slips.** Where the official text contains a drafting slip, implement the evident intent, document the slip in `docs/regulations/errata.md`, and never "fix" it silently in code. Examples:
   - CF definition 4(1)(xix) refers to "Chapter IV" for LSPs; digital lending is Chapter III.
   - CF definitions (xxiii) and (xxiv) refer to "Chapter VII" for project finance; it is Chapter VI.
   - The FS Directions restart numbering after para 21.
   - The CIR Annex I state catalogue is misaligned.

### 8A.0.2 Directions covered

| Code | Direction (all "Reserve Bank of India (Non-Banking Financial Companies – …) Directions") | RBI number and reference | Date / version supplied | Applies to (summary) |
|---|---|---|---|---|
| CF | Credit Facilities, 2025 | RBI/DOR/2025-26/347; DOR.CRE.REC.No.266/07-01-008/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 | NBFC-D, ICC, Factor, MFI, IFC, IDF-NBFC and **HFCs** (para 3(1)); partial for BL with customer interface but no public funds, CICs, P2P (para 3(2)) |
| CIR | Credit Information Reporting, 2025 | RBI/DOR/2025-26/349; DOR.FIN.REC.No.268/20.16.056/2025-26 | 28 Nov 2025 (original text). Amended by RBI/DOR/2025-26/117 (DOR.FIN.REC.No.324/20.16.056/2025-26, 4 Dec 2025, effective 1 Jul 2026), which substitutes paras 10(2) and 15, inserts para 12(10) and adds Annex VI; the amendment is not in the supplied copy | All lending NBFCs including HFC, P2P and CIC; not MGC, AA, SPD, NOFHC, or NBFCs without customer interface (para 3) |
| CRM | Credit Risk Management, 2025 | RBI/DOR/2025-26/350; DOR.CRE.REC.No.269/07-02-008/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 (Amendment of 5 Jan 2026) | NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC; paras 6–8 only for "Notified NBFCs" (NBFC-Factor, NBFC-D, non-deposit NBFCs ≥ ₹500 crore) |
| CON | Concentration Risk Management, 2025 | RBI/DOR/2025-26/351; DOR.CRE.REC.270/07-03-008/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 (Amendments of 1 Jan and 10 Mar 2026) | NBFC-D, ICC, Factor, MFI, IFC, IDF; HFCs except paras 7, 14, 16, 19, 22, 23 |
| INV | Classification, Valuation and Operation of Investment Portfolio, 2025 | RBI/DOR/2025-26/354; DOR.MRG.REC.No.273/00-00-014/2025-26 | 28 Nov 2025 | NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, CIC |
| BR | Branch Authorisation, 2025 | RBI/DOR/2025-26/342; DOR.RAUG.REC.No.261/23-27-013/2025-26 | 28 Nov 2025, updated as on 15 Apr 2026 | NBFCs and HFCs (paras 6 and 12 deposit-taking only); CICs paras 10, 13–15 |
| ALM | Asset Liability Management, 2025 | RBI/DoR/2025-26/355; DoR.LRG.REC.No.274/13-10-004/2025-26 | 28 Nov 2025 | All layers incl. HFC; CICs except Ch III. Ch II only if assets ≥ ₹100 crore; Ch III (LCR) only for NBFC-D and NBFC-ND ≥ ₹5,000 crore |
| FS | Financial Statements: Presentation and Disclosures, 2025 | RBI/DOR/2025-26/359; DOR.ACC.REC.No.278/21.04.018/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 (para 21(9A) inserted 5 Jan 2026) | All incl. HFC, CIC; C.1 all, C.2 ML/UL, C.3 UL |
| CLM | Climate Finance and Management of Climate Change Risks, 2025 | RBI/DOR/2025-26/364; DOR.SFG.REC.No.283/30.01.021/2025-26 | 28 Nov 2025 | **Only NBFC-D and deposit-taking HFCs.** In substance a green-deposit framework |
| AA | Account Aggregator, 2025 | RBI/DoR/2025-26/368; DoR.FIN.REC.No.287/03-10-123/2025-26 | 28 Nov 2025 | NBFC-AAs only; FIU-side obligations derived |
| CMP | Compliance Function, 2026 | RBI/DoS/2026-27/460; DoS.CO.PPG.54/11.01.005/2026-27 | 31 Jul 2026 | **Middle and Upper Layer only** |
| CYB | Cybersecurity, Technology: Risk, Resilience and Assurance Framework, 2026 | RBI/DoS/2026-27/461; DoS.CO.CSITEG.55/31.01.015/2026-27 | 31 Jul 2026, immediate effect | All NBFCs incl. HFC: Ch II all; Ch III BL < ₹500 crore and all CICs; Ch IV BL ≥ ₹500 crore; Ch V TL/UL/ML excluding CICs |
| DPS | Digital Payment Security Controls, 2026 | RBI/DoS/2026-27/462; DoS.CO.CSITEG.56/31.01.015/2026-27 | 31 Jul 2026 | **Credit-card-issuing NBFCs only** |
| FRM | Fraud Risk Management, 2026 | RBI/DoS/2026-27/463; DoS.CO.FMG.57/23.04.001/2026-27 | 31 Jul 2026 | UL, ML, and BL with assets ≥ ₹500 crore (audited 31 March balance sheet), incl. HFCs (HFC reporting to NHB) |
| AUD | Auditor's Report, 2026 | RBI/DoS/2026-27/468; DoS.CO.ARG.62/08.91.001/2026-27 | 31 Jul 2026; first applies to FY ending on or after that date | Every NBFC auditor (HFC auditors excluded) |

The four DoS Directions of 31 Jul 2026 (CMP, CYB, DPS, FRM) repeal earlier instructions through circular DoS.CO.PPG.66/11.01.005/2026-27. The repeal list in that circular is not in the supplied texts [VERIFY].

---

## 8A.1 CF — Credit Facilities Directions (347)

**Structure:**

- Ch I paras 1–4
- Ch II para 5
- Ch III Digital Lending paras 6–30
- Ch IV Gold & Silver paras 32–50 (para 31 deleted w.e.f. 1 Apr 2026)
- Ch V Microfinance paras 51–62
- Ch VI Project Finance paras 63–79
- Ch VII Partial Credit Enhancement paras 80–103
- Ch VIII Other restrictions paras 104–108
- Ch IX Real estate / CRE paras 109–111
- Ch X Repeal paras 112–115
- Annex-I: CIMS DLA data. Annex-II: deleted. Annex-III: pledged-securities data.
- Para 25(1) was substituted w.e.f. 13 Feb 2026.

**Board credit policy (para 5).** The Board-approved credit policy must cover:

- digital lending including DLG;
- gold and silver;
- microfinance;
- project finance;
- demand/call loans;
- housing finance.

*Build:* a policy registry. Every product template links to the approved credit-policy version.

### Digital lending (Ch III)

**LSP arrangements (para 6):**

- a contract with each LSP;
- enhanced due diligence covering technical capability, data privacy, conduct, past record and compliance;
- periodic conduct review;
- policy-based monitoring of portfolios originated through LSPs;
- guidance to an LSP acting as recovery agent;
- the NBFC is "fully responsible and liable for all acts and omissions of the LSP" (para 6(7)).

**Multi-lender LSPs (para 7):**

- show all matching offers, and disclose the names of unmatched lenders;
- use a documented, consistent matching approach for similarly placed borrowers;
- each offer shows lender name, amount, tenor, APR, monthly repayment obligation, penal charges, and a KFS link;
- no promotion of any lender and no dark patterns;
- ranking only on a publicly pre-disclosed metric.

**Creditworthiness (para 8):**

- at minimum, capture age, occupation and income, and keep them for audit;
- no automatic increase in credit limit without an explicit, evaluated and recorded borrower request.

**Disclosures (para 9):**

- KFS and penal charges per RBC.
- Digitally signed documents on NBFC letterhead flow automatically to the registered and verified email/SMS on execution. These are: KFS, product summary, sanction letter, T&C, account statements, and the NBFC/LSP privacy policies (para 9(3)).
- The website shows at one prominent place (para 9(4)):
  - digital lending products and DLAs;
  - LSPs, their DLAs and the activities they perform;
  - customer care and grievance redressal;
  - CMS and Sachet links;
  - privacy policies.
- DLAs and LSPs link to that website (para 9(5)).
- When a recovery agent is assigned or changed, send the agent's particulars by email/SMS **before** the agent contacts the borrower (para 9(6)).

**Money flows (para 10):**

- **Disbursal:** always to the borrower's bank account. Exceptions:
  - disbursal exclusively under a statutory or regulatory mandate;
  - co-lending flows between lenders;
  - a specific end-use, paid directly into the end-beneficiary's bank account.
  - Never to a third-party or LSP account (para 10(1)).
- **Salary-advance proviso:** the employer may repay by salary deduction directly from the employer's bank account.
- **Co-lending:** no third party other than the lenders may control the flows.
- **Repayment:** directly to the NBFC's account, with no pass-through or pool account (para 10(2)); no third-party control (para 10(3)).
- **LSP fees:** paid by the NBFC (para 10(4)).
- **Cash recovery on delinquent loans:** allowed, but "duly reflected in full in the borrower's account on the same day"; LSP fees are not deducted from recoveries (para 10(5)).

**Cooling-off (para 11):**

- The borrower can exit by paying principal and proportionate APR, without penalty.
- The period is set in the Board-approved credit policy and is not less than one day.
- A reasonable one-time processing fee may be retained only if disclosed upfront in the KFS.

**Grievances (para 12):**

- nodal grievance officers at the NBFC and at each borrower-facing LSP;
- their contacts on the NBFC website, LSP website, DLA and KFS;
- complaints can be lodged on the DLA and website;
- after 30 days without reply, or on rejection, escalation to CMS (cms.rbi.org.in) or CRPC, RBI Chandigarh, which must be communicated to the borrower.

**Data (paras 13–16):**

- Need-based collection, explicit consent, audit trail.
- No access to files/media, contacts, call logs or telephony.
- Camera, microphone and location only as one-time access for onboarding/KYC (para 13(1)).
- Borrowers can deny, restrict, revoke and request deletion (para 13(2)).
- Purpose disclosed at each stage (para 13(3)).
- Explicit consent before any third-party sharing (para 13(4)).
- The LSP holds only minimal data (para 14(1)).
- A storage, retention and destruction policy is published (para 14(2)).
- **No biometric storage unless statute allows** (para 14(3)).
- Data stored in India only; anything processed abroad is deleted there and repatriated within 24 hours (para 14(4)).
- Privacy policy (para 15); cybersecurity standards (para 16).

**CIC and CIMS (paras 17–18):**

- Report all DLA lending to CICs irrespective of nature or tenor, including merchant-platform deferred-payment credit (para 17).
- Report every DLA (own or LSP) on CIMS in the Annex-I format, one line per DLA per platform. Fields: name, owner (self/LSP), "available on", link, GRO name/email/telephone/mobile, RE website. Update on addition or cessation.
- The CCO or a Board-designated official certifies four points (para 18(3)–(4)):
  - the website link;
  - the LSP-DLA nodal officer;
  - data compliance with paras 13–14;
  - website disclosure under para 9(4).
- The CIMS listing is not an RBI endorsement (para 18(6)).

### DLG (paras 19–29)

- DLG only from an LSP, or another lender engaged as LSP, incorporated under the Companies Act, 2013 (para 19).
- Board policy; DLG is no substitute for underwriting (para 20(1)–(2)).
- Statutory-auditor-certified provider declaration on every entry or renewal (para 20(3)).
- No DLG on loans covered by trust-fund credit-guarantee schemes (para 21(1)).
- Contract terms: extent, form, invocation timeline, disclosures (para 22).
- **Forms (para 23):** cash with the NBFC; FD with a Scheduled Commercial Bank with lien to the NBFC; or bank guarantee in favour of the NBFC.
- **Cap (para 24):** ≤ 5% of the total amount disbursed out of the loan portfolio at any time. For implicit guarantees, performance risk ≤ 5%.
  - The **DLG set is fixed**, not dynamic.
  - Cover activates pro rata as loans are disbursed.
  - Loans leave the set only by repayment or write-off.
- **Treatment (para 25):**
  - Asset classification and provisioning follow the IRACP Directions (para 25(1), substituted 13 Feb 2026).
  - Invoked DLG is not set off against individual loans (para 25(2)).
  - Recoveries may be shared (para 25(3)).
  - Invoked DLG is **never reinstated**, including through recovery (para 25(4)).
- An NBFC that provides DLG deducts it from capital (para 26(2)).
- Invoke within a maximum of 120 days overdue, unless dues are made good (para 27(1)). The DLG agreement runs at least as long as the longest loan tenor (para 27(2)).
- The LSP publishes portfolio counts and amounts monthly, within 7 working days of month-end, and the NBFC ensures it does (para 28).
- Not DLG: CGTMSE, CRGFTLIH, NCGTC; BIS, IMF and MDB guarantees (para 29).
- DLG is not synthetic securitisation (para 30(2)).

### Gold and silver (Ch IV)

Eligible collateral is gold/silver jewellery, ornaments and coins only.

- **Policy (para 32).**
- **Detailed credit assessment** where the total loan is above ₹2.5 lakh; for bullet loans, use the amount payable at maturity (para 33).
- **Renewal or top-up (para 34):**
  - only on a formal request;
  - with assessment;
  - within LTV;
  - on a standard account;
  - for bullet loans, only after accrued interest is paid;
  - renewals and top-ups clearly flagged in the system.
- **Prohibitions (para 35):** no loans to buy gold in any form, or gold ETF/MF units; no loans against primary gold or silver, or financial assets backed by them.
- **Ownership (para 36):** no loan where ownership is doubtful; ownership document or declaration in all cases; AML monitoring of multiple or frequent loans above a threshold.
- No re-pledge (para 37).
- **Consumption bullet loans:** ≤ 12 months (para 38).
- **Weight caps per borrower (para 39):** gold ornaments 1 kg; silver ornaments 10 kg; gold coins 50 g; silver coins 500 g.
- **Valuation (paras 40–42):**
  - at actual purity;
  - the lower of the 30-day average closing price and the previous day's close, from IBJA or a SEBI-regulated commodity exchange;
  - nearest-purity adjustment where needed;
  - intrinsic metal value only.
- **LTV for consumption loans, on total consumption loan per borrower (para 43):**
  - ≤ ₹2.5 lakh: 85%;
  - > ₹2.5 lakh to ₹5 lakh: 80%;
  - > ₹5 lakh: 75%.
  - LTV = outstanding ÷ collateral value. For bullet loans, both the LTV and the slab use the total repayable at maturity.
- LTV maintained throughout the tenor (para 44).
- Conduct and collateral management per RBC (para 45).
- KYC; disbursal to bank account; Income-tax Act ss.269SS/269T (para 46).
- **Para 47 applies the para 10(1) disbursal and para 10(2) repayment rules to all gold/silver loans on every channel.**
- Stricter internal audit of multiple loans to one borrower or related borrowers (para 48).
- Balance-sheet disclosure: gold-collateral and silver-collateral loans as % of total assets, separately (para 50).

### Microfinance (Ch V)

- **Definition (para 51):** a collateral-free loan (no deposit lien, no hypothecation) to a household with annual income ≤ ₹3,00,000, where household = husband, wife and unmarried children. It covers **all** collateral-free loans to such households, irrespective of end use or channel.
- **Income assessment (para 52):** Board policy, covering all earning members and sources, assessed over a minimum of one year and corroborated.
- Household income is mandatorily reported to CICs, with the reason for any divergence captured (para 54).
- **Repayment cap (paras 55–56):** ≤ 50% of monthly household income. It covers principal and interest of **all** household loans, secured and unsecured, plus the proposed loan, and excludes future income from the financed activity.
- **No new loans** while the household is above 50% (para 57).
- Use CIC data, declarations, bank statements and local enquiries (para 58).
- Flexible repayment periodicity (para 59).
- **Pricing policy (paras 60–61):** interest-rate model, components, spread range, and a ceiling on the rate and all charges; never usurious.

### Project finance (Ch VI; for projects reaching financial closure after 1 Oct 2025, para 64)

- **Definition:** ≥ 51% of repayment from project cash flows, plus a common agreement among lenders (para 4(1)(xxiv)).
- **Before disbursement (para 67):** financial closure and original DCCO documented; stage-linked disbursement schedule; tenor including moratorium ≤ 85% of the project's economic life.
- Common DCCO across lenders (para 68).
- **Minimum exposure while under construction (para 69):** where aggregate exposure ≤ ₹1,500 crore, each lender ≥ 10%; otherwise the higher of 5% or ₹150 crore.
- Approvals before financial closure (paras 70–71).
- **Land or right of way before disbursal (para 72):** PPP 50%; others 75%.
- PPP disbursal only after the Appointed Date (para 73).
- TEV study where aggregate exposure ≥ ₹100 crore (para 74).
- Disbursal proportionate to completion and equity, certified by the LIE or architect (para 75).
- **Project database (para 77):** debtor profile, original profile, DCCO changes, credit events, current specification. Update within 15 days of any change (para 78).
- Notes to Accounts (para 79).

### Partial credit enhancement (Ch VII; Middle Layer and above)

- ≤ 50% of the issue (para 85);
- irrevocable, not a guarantee (para 86);
- pre-enhanced rating ≥ BBB-, rated by two ECAIs (paras 88–89);
- a drawn tranche is repaid within 30 days, and becomes NPA at 90 days (para 94);
- aggregate ≤ 20% of Tier 1 (para 95(2));
- for bonds issued by NBFCs: tenor ≥ 3 years, refinancing only, ≤ 1% of capital funds per issuer (paras 96–98).

### Other restrictions (Ch VIII–IX)

- **IPO financing:** ≤ ₹1 crore per borrower (para 104).
- **Own shares:** no lending against the NBFC's own shares (para 105).
- **Loans against listed shares by NBFCs with assets ≥ ₹100 crore (para 106):**
  - 50% LTV at all times, with any shortfall made good within 7 working days;
  - Group 1 securities only where the loan is for capital-market investment and exceeds ₹5 lakh;
  - quarterly online reporting to the stock exchanges in Annex-III format: lender name, PAN, date; and per row company, ISIN, number of shares, borrower type (promoter/non-promoter), borrower name, borrower PAN.
- **Demand/call loans (para 107):**
  - a recall cut-off date, with reasons recorded if beyond one year;
  - a stated rate, with interest payable monthly or quarterly, and reasons recorded if there is none or a moratorium;
  - a review within 6 months of sanction;
  - no renewal unless the review is satisfactory.
- **Housing projects (para 108):** the builder discloses the mortgagee in brochures and advertisements and provides NOC; no release of funds until then.
- **Real estate (para 109):** disbursal only after statutory clearances.
- **CRE (para 110):** includes loans for an individual's third dwelling unit onwards.
- **CRE-RH (para 111):** commercial area ≤ 10% of FSI; otherwise the whole loan is CRE.
- **Housing finance definition (para 4(1)(xiv)):** a plot loan needs a declaration to construct within 3 years; commercial space ≤ 10% of FSI; LAP and furnishing loans are not housing finance.
- **Not settled by this copy:** the revolving-credit restriction (August 2026 draft amendment) is not in the 1 Apr 2026 text, so its [VERIFY] stays. Para 6(6) cites the "Managing Risks in Outsourcing" Directions, while para 62(2) cites "Management of Third-Party Dependencies" Directions, 2025 [VERIFY which is current].

---

## 8A.2 CIR — Credit Information Reporting Directions (349, as amended by 117)

**Membership (paras 6–8):**

- Membership of **all four** CICs (CRIF High Mark, Equifax, Experian, TransUnion CIBIL) is mandatory (para 6).
- Fees are capped at ₹10,000 one-time and ₹5,000 annual per CIC (paras 7–8).

**Formats (para 9; Annex I).** UCRF Form 1 Consumer, Form 2 Commercial, Form 3 MFI (including SHG).

- **Consumer:**
  - "High Credit/Sanctioned Amount" is mandatory;
  - written-off amounts (total and principal) and settlement amount;
  - Credit Facility Status values include Restructured and Closed, Post Write Off Closed, Auctioned and Settled, Repossessed and Settled, and Guarantee Invoked;
  - ID type CKYC.
- **Commercial:**
  - Sanction Date is mandatory;
  - CIN, Udyam, DIN;
  - wilful-default status and date;
  - suit-filed status, reference, amount and date;
  - settled amount;
  - reasons for restructuring;
  - guarantor and security segments;
  - Relationship segment with CKYC.
  - "SMA" and "Doubtful" are removed from the asset-classification values.
- **MFI:**
  - fixed-length HDR and TRL records;
  - separate files for SHG and for JLG + individual loans;
  - HDR System Vendor Identifier and Version (Finbyx populates these);
  - account status codes S01–S15;
  - write-off reasons X01–X10 (fields 90–92 required if status is S06);
  - **records are rejected if field 49 (total monthly family income), 84, 85 or 86 is missing**;
  - field 87 = principal outstanding only;
  - the Unique Account Reference stays stable across branch splits;
  - an individual MF loan goes in either the MFI or the consumer format, never both.
- **Annex V:** email ID replaces fax (commercial) and the dummy field (MFI).
- **Catalogues** (states, codes) are versioned per CIC specification and never hard-coded. The published state catalogue is misaligned.

**Frequency (para 10).** Effective-dated:

- **Until 30 Jun 2026:** fortnightly as on the 15th and month-end, within 7 calendar days.
- **From 1 Jul 2026** (para 10(2) as substituted):
  - reference dates 9th, 16th, 23rd (incremental, within 4 calendar days) and month-end (full file by the 5th);
  - incremental files cover new accounts, closures, borrower-action changes, overdue accounts, and DPD-only changes.
- **No repayment may go unreported, including the last instalment** (para 10(3)).

**Reporting rules (paras 11–14):**

- No borrower consent is needed to report to CICs (para 11).
- Commercial reports carry CIN and directors' DIN (para 12(1)).
- Compromise settlements are reported with the reason (para 12(2)).
- A partly overdue instalment is reported as is (para 12(3)).
- **"Settled"** only where principal or interest was waived for financial inability. Wrong debits and contested charges are reported as **"disputed"** (para 12(4)).
- IBC-admitted cases are reported as suit-filed (para 12(7)).
- The Relationship Segment is mandatory for accounts opened on or after 1 Jul 2018, with shareholders reported only if they are beneficial owners (para 12(8)).
- Cross-reporting: consumer and commercial co-borrowers each go in their own format (para 12(9)).
- **CKYC number reported where available, or once issued** (para 12(10), from 1 Jul 2026).
- SHG member data per Annex III, with the ₹30,000, ₹1,00,000 and ₹20,000 thresholds (para 13).
- After CoR cancellation, keep reporting until the loans run off (para 14).

**Rejections and data quality (paras 15–17):**

- **Rejections:** within 7 days until 30 Jun 2026; from 1 Jul 2026, "before or along with the data for the next reporting reference date" (para 15).
- **DQI:** reviewed half-yearly, with a report to top management within 2 months (paras 16–17).

**Correction (paras 18–20):**

- Follow the CICRA and CIC Rules 20/21 timelines, and report deviations to the Board or Customer Service Committee (para 18).
- Correct errors at source (para 19).
- The credit policy requires CIRs from one or more CICs (para 20).

**SARFAESI website display (para 21; Annex IV):**

- Secured assets possessed under s.13(4) (symbolic or physical) on or after 25 Sep 2023, shown in the Annex IV columns.
- Updated monthly; removed on sale or full settlement.
- Consortium members display individually.

**Customer service (para 34):**

- **SMS/email alerts sent while submitting default/DPD data to CICs**, wherever contact details exist (para 34(1)(i)). This is *not* a pre-reporting notice.
- A CIC nodal officer; changes notified to the CICs within 5 calendar days (para 34(2)).
- Rejection reasons taken from the CIC-circulated list (para 34(3)).
- Root-cause analysis half-yearly, with an annual top-management review (para 34(4)).

**Compensation (para 35):**

- ₹100 per calendar day if a complaint is unresolved after 30 calendar days. The CI has 21 days and the CIC 9 (para 35(1)).
- The CI pays if it fails to send corrected data within 21 days (para 35(2)).
- Proportionate apportionment (para 35(4)).
- Multi-CI complaints go to the CIC (para 35(5)).
- Notify the delay split (para 35(6)).
- The resolution date is the date the rectified CIR is sent (para 35(7)).
- Complaint forms capture email and bank account/UPI (para 35(8)).
- Pay within 5 working days (para 35(9)).
- Exclusions (para 35(12)).

**Best practices (para 38):**

- centralised NOCs linked to CIC closure;
- credit-information grievances integrated with grievance management;
- **first-time borrowers not rejected merely for having no credit history** (para 38(5)).

---

## 8A.3 CRM — Credit Risk Management Directions (350)

**Notified NBFCs (paras 6–8):**

- independent credit appraisal, with no reliance on the borrower's consultants;
- sensitivity and scenario tests, especially for infrastructure;
- check the source of promoter equity, and that parent debt is not infused as SPV equity;
- check directors against defaulter lists by DIN/PAN, confirming name matches independently;
- end-use certification (the NBFC may use its own auditors).

**Related-party lending (paras 4(1)(va)–(vb), 13A–13Q):**

- **Definitions:** related persons and related parties; relatives per Companies Act s.2(77); specified employees (up to two levels below the Board, plus policy designees); major shareholder (≥ 10% or ₹5 crore of paid-up shares).
- **Limits:** aggregate, single-party and group limits within prudential exposure limits (para 13F).
- **Materiality threshold** per transaction, set by the layer in the last audited balance sheet (para 13G):
  - UL / Top Layer: ≤ ₹10 crore;
  - ML: ≤ ₹5 crore;
  - BL: ≤ ₹1 crore.
- **Sanction:** loans above the threshold are sanctioned by the Board, or a Board committee **other than the Audit Committee** (para 13I).
- **Recusal:** interested directors, KMP and specified employees recuse, including for OTS, write-off, waiver, enforcement and resolution plans (para 13J).
- **Records and reporting:**
  - a maintained related-party list (para 13K);
  - annual Board report on loans to specified employees (para 13L);
  - quarterly internal-audit review (para 13M);
  - deviations reported to the Audit Committee (para 13N);
  - reciprocal arrangements treated as related-party lending (para 13O).

**Prohibitions:**

- no lending against own shares (para 14);
- no lending against own debentures, except tax-exempt bonds (para 15).

**CDS (paras 16–17):**

- user only, for hedging;
- excess over single/group limits risk-weighted at 667%;
- no MTM netting;
- quarterly report to the DoS Regional Office of exposures above limits.

**LEI (paras 18–24):**

- Non-individual borrowers with aggregate bank/FI exposure ≥ ₹5 crore need an LEI. Exposure is the higher of limit and outstanding, sourced from own data, CRILC or a declaration.
- **No new, renewed or enhanced exposure without a valid LEI**; government departments are exempt.
- The LEI must be kept renewed.

**CERSAI (paras 25–28):**

- File every current transaction on an ongoing basis.
- Four types:
  - non-MODT mortgage;
  - hypothecation of plant and machinery, stocks, book debts and receivables;
  - intangibles;
  - under-construction property agreements.
- The 30-day period comes from SARFAESI s.23 and the CERSAI Rules, not from this Direction [VERIFY].

**Annex I:** disclosure table of loans to directors, senior officers and their relatives.

---

## 8A.4 CON — Concentration Risk Management Directions (351)

**Definitions (para 4):**

- **Eligible capital base:** Tier 1 (para 4(2)).
- **Group of connected counterparties** (para 4(3)):
  - control: > 50% of voting rights is automatic;
  - economic interdependence: criteria (a)–(g), assessed mandatorily where exposure exceeds 5% of Tier 1.
- **Infrastructure lending and "high-quality infrastructure projects"** (para 4(4)).
- **Large Exposure (UL):** ≥ 10% of eligible capital base (para 4(5)).
- **Tier 1 for concentration purposes:** capital augmentation counts only after the external auditor's certificate is submitted to DoS (para 4(8)).

**Base Layer (paras 6–11):**

- Board limits for single/group credit and investment, computed by the ML method (paras 6, 8).
- An NBFC held by an NOFHC has no exposure to its promoter group or the NOFHC (para 7).
- Sub-limits for consumer credit, especially unsecured, monitored by the RMC (para 9).
- **Top-up loans against depreciating movable assets such as vehicles are treated as unsecured** (para 10).
- IPO funding ≤ ₹1 crore per borrower (para 11).

**Middle Layer (paras 12–24):**

- **Limits:** single 25% / group 40% of Tier 1; IFC 30% / 50%; plus 5% / 10% where the additional exposure is infrastructure (paras 13–14).
- Tier 1 from the latest audited or limited-review statements (para 14(3)).
- **Exemptions (para 17):** exposures deducted from Owned Fund, zero-risk-weight exposure to GoI/State, and exposure fully guaranteed by GoI.
- **Exposure computation (para 20):**
  - on-balance-sheet at outstanding amount, netted only where provisions are held;
  - off-balance-sheet × CCF;
  - CRT offsets: cash margin, Central/State Government guarantees, CGTMSE/CRGFTLIH/NCGTC; guarantees must be "direct, explicit, irrevocable and unconditional".
- Limits apply to both the NBFC's own group and the borrower's group (para 21).
- **Factoring:** with recourse, exposure is on the assignor; without recourse, on the debtor (paras 22–23).
- **Sensitive-sector exposure** (capital market and CRE): Board limits, a land-acquisition sub-limit, and the IPO cap (para 24).

**Upper Layer — Large Exposure Framework (paras 25–49):**

- Solo and consolidated (para 27).
- **Single counterparty:** 20%, with +5% by Board policy for recorded exceptional reasons; IFC +5%; infrastructure +5%; hard caps 25% (non-IFC) and 30% (IFC) (paras 33–34).
- **Group:** 25%; IFC 35%; infrastructure +10% (paras 35, 39).
- CCP treatment (paras 42–44).
- **A breach is reported immediately, and no further exposure is allowed until cured** (paras 45–46).
- **Monthly "Return on Large Exposures"** (Annex I, sections A–D) (para 48). Annex I has 20 rows in section A while para 48 says 10; build for at least 20.
- Internal sector limits, including exposure to NBFCs (para 49).

---

## 8A.5 INV — Investment Portfolio Directions (354)

- **Classification** follows the applicable accounting standard at the time of each investment (para 9). The Board investment policy states the criteria (paras 7–8).
  - **Ind AS:** amortised cost / FVOCI / FVTPL.
  - **Non-Ind AS:** current or long-term (para 4).
- **Non-Ind AS inter-class transfers (para 10):** never ad hoc; only on 1 April or 1 October, with Board approval; scrip-wise, at the lower of book and market value; full depreciation provided, appreciation ignored.
- **Non-Ind AS valuation (paras 14–21):**
  - quoted current investments in six categories, each at the lower of cost and market, with no set-off across categories;
  - unquoted equity: lower of cost and break-up value, or ₹1 if the investee's balance sheet is unavailable for 2 years;
  - unquoted preference shares: lower of cost and face value;
  - unquoted G-Secs and government-guaranteed bonds: carrying cost;
  - MF units: NAV;
  - commercial paper: carrying cost;
  - unquoted debentures follow IRAC as loans.
- **Income recognition (paras 22–24).**
- **AIF schemes (paras 25–27):**
  - no investment in an AIF scheme with downstream investment in a debtor company (any company with loan or investment exposure in the preceding 12 months);
  - exit within 30 days, or provide 100% on the look-through portion;
  - subordinated/sponsor units deducted from capital.
- **Trading and hedging:**
  - G-Sec trades through a gilt or demat account (paras 11–12);
  - OTC corporate-bond trades reported within 15 minutes (para 13);
  - currency futures and IRF for hedging only, with half-yearly IRF data within 1 month (paras 28–29);
  - ML/UL repo and options (paras 31–34).

---

## 8A.6 BR — Branch Authorisation Directions (342)

- No prior RBI approval is needed to open branches unless specifically restricted (para 5).
- **Deposit-taking NBFCs (para 6):** branches or agents only within the registered-office state, unless NOF > ₹50 crore **and** rating ≥ AA.
- **No branches abroad** (para 10).
- **Closure (para 11):** at least 3 months' public notice in one leading national newspaper and one local vernacular newspaper, stating the purpose and the servicing arrangements.
- **Deposit-taking (para 12):** intimation with a copy of the notice to the RBI/NHB Regional Office within 7 days of publication.
- **Representative office abroad (paras 13–15):** prior approval through PRAVAAH; liaison only, with no outlay and no credit; periodic reports.

---

## 8A.7 ALM — Asset Liability Management Directions (355)

**Applicability:**

- Ch II applies only where assets ≥ ₹100 crore (last audited balance sheet).
- Ch III (LCR) applies to all NBFC-D and to NBFC-ND ≥ ₹5,000 crore, never to CICs (paras 3–5).

**Governance:**

- Board responsibility; ALCO headed by CEO/MD/ED (paras 8, 17).
- Internal limits (paras 10–11); CRO involvement (para 16); independent review (para 19).
- Forward-looking MIS, entity and group, normal and stress (para 14).

**Public disclosure (para 15; Annex I):** published quarterly on the website and annually in the notes. It covers:

- funding concentration by significant counterparty;
- top 20 deposits;
- top 10 borrowings;
- concentration by instrument or product;
- stock ratios;
- institutional set-up.

**Framework:**

- Liquidity framework contents (para 22).
- Liquidity cost in pricing and new-product approval (para 24).
- Off-balance-sheet flows (para 25).
- Encumbrance register (para 27).
- **Stress tests:** NBFC-specific and market-wide, short and protracted, individually and combined (para 28).
- **Contingency funding plan:** sources, amounts, triggers, lead times (para 29).
- Group liquidity (para 30).

**Time buckets (paras 32, 49):** 1–7 days; 8–14 days; 15–30/31 days; > 1–2 months; > 2–3 months; > 3–6 months; > 6 months–1 year; > 1–3 years; > 3–5 years; > 5 years. The IRS statement adds "non-sensitive".

**Securities:**

- mandatory vs non-mandatory slotting by defeasance period;
- MTM;
- optional trading book with holding period ≤ 90 days (paras 33–38).

**Tolerance limits (paras 39–40).** Net cumulative negative mismatch must not exceed:

- 10% in 1–7 days;
- 10% in 8–14 days;
- 20% in 15–30 days;

measured on cumulative outflows. Board limits apply up to 1 year, and the same limits apply to the consolidated statement.

**Other requirements:**

- Statement of structural liquidity on expected timing (para 41); short-term dynamic liquidity, 1 day to 6 months (para 42).
- **Stock ratios (para 43):**
  - short-term liabilities / total assets;
  - short-term liabilities / long-term assets;
  - CP / total assets;
  - NCDs (original maturity < 1 year) / total assets;
  - short-term liabilities / total liabilities;
  - long-term assets / total assets.
- Currency risk (para 44).
- **IRS (paras 45–53):** traditional gap analysis first; gap limits on total assets, earning assets or equity; optional earnings-at-risk.
- **Behavioural assumptions (paras 54–55):** approved by ALCO/Board, with a copy to the DoS Regional Office.
- Funds transfer pricing (para 56).

**Annex II slotting rules.** Encode each one in a versioned slotting engine. Examples:

- NPAs: sub-standard dues within 3 years in the 3–5 year bucket, otherwise > 5 years; doubtful and loss in > 5 years;
- overdue receivables, by age;
- current-account minimum balance in 6–12 months, the excess in 1–7 days;
- loan commitments per the disbursement schedule;
- AIF units > 5 years.

**Annex III:** floating-rate advances are slotted by reset lag.

**Returns (paras 57–59):**

- DNBS04A (short-term dynamic liquidity) quarterly; DNBS04B (structural liquidity + IRS) monthly; Annex IV formats.
- Timelines per the Supervisory Returns Directions; para 58 still cites the 2024 Directions [VERIFY against 2026].

**LCR (Ch III, paras 60–78):**

- Minimum 100% on an ongoing basis. Use of HQLA under stress is reported immediately to DoS (para 62).
- **HQLA haircuts:**
  - 0%: cash, SCB demand deposits, G-Secs (para 68);
  - ≥ 15%: 20%-risk-weight sovereign/PSE/MDB, AA- and above corporate bonds and CP (para 69);
  - ≥ 50%: 20–50%-risk-weight sovereign, Nifty/Sensex equities, A+ to BBB- corporate debt (para 70);
  - bank, FI and NBFC issuers excluded.
- s.45IB securities count up to 80% of the requirement (para 71).
- Operational tests and monetisation (paras 72–73); 30-day grace on downgrade (para 74).
- **Net outflows = stressed outflows × 115% − min(stressed inflows × 75%; 75% of stressed outflows)** (para 76).
- No double counting (para 77).
- Intraday liquidity is not addressed.

---

## 8A.8 FS — Financial Statements: Presentation and Disclosures Directions (359)

> **Numbering defect.** The official text restarts numbering after para 21. Cite C.1 items as "FS 21(n)" and C.2 items as "FS C.2(n)".

**General:**

- Balance-sheet date is 31 March, finalised within 3 months (para 9).
- Ind AS or the Companies (Accounting Standards) Rules, 2021 as applicable (para 10).
- **The Schedule III division follows the Companies Act**; this Direction does not name it.

**Ind AS governance (para 12(1)):**

- Board-approved business-model policy, and a policy on sales out of amortised cost, both disclosed.
- Board-approved ECL methodology; overlays approved by the Audit Committee.
- Accounts > 90 DPD not treated as impaired need Audit Committee approval, with disclosure of the number, outstanding and overdue amounts.
- SICR rebuttal beyond 30 DPD goes to the Audit Committee, and never beyond 60 DPD.

**Impairment Reserve (para 12(2)):**

- IRACP runs in parallel.
- Any shortfall of the Ind AS 109 allowance against IRACP is appropriated from profit after tax to an Impairment Reserve.
- The reserve is not regulatory capital; no withdrawal without DoS permission.

**Presentation:**

- Provisions shown separately, never netted (paras 13–15).
- Nil lines omitted (para 17); comparatives shown (para 19).

**Annex I Schedule (para 20):**

- borrowings, including overdue;
- public deposits;
- secured/unsecured loans;
- leased and hire assets;
- investments;
- borrower group-wise (related parties);
- GNPA/NNPA by related and other parties;
- assets acquired in satisfaction of debt.

**C.1, all NBFCs (para 21):**

1. Gold and silver loans and auctions.
2. Project finance, quarterly from 1 Oct 2025.
3. Non-fund-based facilities.
4. **Co-lending:** active partner list on the website, plus notes.
5. Securitisation, STC and non-STC.
6. Transfer of loan exposures, quarterly.
7. Restructuring and resolution plans.
8. Exposures: real estate, capital market, sectoral (sub-sector > 10% of Tier 1 separately), intra-group, unhedged foreign currency.
9. Related-party transactions.
   - **(9A)** Loans to and contracts with related parties under CRM, including SMA/NPA status, from 1 Apr 2026.
10. Complaints.
11. Loans to directors, senior officers and their relatives.
12. Currency futures.
13. **Liquidity:** quarterly website + notes, for NBFC-ND ≥ ₹100 crore, CICs and all NBFC-D.
14. CDS.
15. **IRACP vs Ind AS 109 comparison** by stage and asset class.

**C.2, ML and UL:**

10. Accounting policies.
11. Capital.
12. Investments.
13. Derivatives.
14. **ALM maturity pattern** in the 10 buckets.
15. Parent-company products; single/group limits exceeded; unsecured advances against intangibles.
16. Corporate governance, including penalties and strictures.
17. Breach of covenant.
18. Divergence.
19. Registrations with other regulators.
20. Area of operation.
21. Ratings and their migration.
22. Non-executive directors' pecuniary relationships.
23. Prior-period items.
24. Revenue recognition postponed.
25. Provisions and contingencies.
26. Drawdown from reserves.
27. Concentration: top 20 deposits, advances and exposures; top 4 NPA accounts.
28. NPA movement.
29. Overseas assets.
30. Off-balance-sheet SPVs.
31. Off-balance-sheet and structured products.
32. **LCR disclosure:** quarterly, simple average of **daily** LCR over the previous quarter, 15-row template plus HQLA components. Excludes NBFC-ND below ₹5,000 crore, CICs and SPDs.
33. Currency options.

**C.3, UL:** listing within 3 years, with a roadmap.

**Ch IV:** consolidate all subsidiaries, with reasons for any exclusion.

---

## 8A.9 CLM — Climate Finance Directions (364)

**Applicability:** only NBFC-D and deposit-taking HFCs; green deposits are optional (para 9). The Direction prescribes no climate-risk disclosures, no scenario analysis and no financed emissions.

**If a tenant raises green deposits:**

- Board Green Deposit policy, published, and a Financing Framework (paras 6, 8, 10).
- No financing green activities first and raising green deposits afterwards (para 8).
- INR only (para 9).
- **Unallocated proceeds only in 0%-haircut HQLA with original tenure ≤ 1 year** (para 10(4)).
- External review of the framework (paras 11–12).
- **Allocation by green taxonomy (para 13):** eligible categories and exclusions — fossil fuels, nuclear, direct incineration, alcohol/weapons/tobacco/gaming/palm oil, landfill, hydro > 25 MW.
- Annual third-party verification of allocation (paras 14–15).
- Annual impact assessment, with indicators such as MWh and tCO2e avoided (para 16).
- Reports on the website (para 17).
- **Board review within 3 months of FY-end** (para 18).
- Climate and ESG in the ICAAP remain an internal risk input, not a requirement of this Direction.

---

## 8A.10 AA — Account Aggregator Directions (368)

**Finbyx is never an AA.**

- An AA needs a CoR and NOF ≥ ₹2 crore (para 11).
- It may undertake no other business (para 14(6)).
- It holds no financial information (para 14(7)) and uses no third-party service providers (para 14(8)).
- **The lender tenant is the FIU** (para 8(12)).

**Information covered (para 8(9)):** deposits, securities, MF, insurance, NPS, InvIT/REIT, and **GSTR-1 and GSTR-3B**. Loan accounts are not in the list as issued.

**Consent artefact (para 17).** Fields:

- customer identity;
- nature of information;
- purpose;
- recipients;
- notification URL;
- creation and expiry dates;
- AA identity and signature.

The artefact may be revoked, including partially (para 20), and must be loggable and auditable (para 21).

**Data handling:**

- Providers sign the data (para 24).
- Where an AA statement and the provider's books differ, the **provider's record prevails** (para 14(11)).
- **The FIU uses or discloses the data only as the artefact specifies** (para 28).
- **An RE that joins as FIU must also join as FIP if it holds specified information** (para 29). Deposit-taking tenants therefore need an FIP endpoint for deposits.
- Adopt the ReBIT specifications (para 33).
- Purpose codes, data life and fetch frequency come from ReBIT, not this Direction [VERIFY current ReBIT version].

---

## 8A.11 CMP — Compliance Function Directions (460; ML/UL only)

**Governance (paras 6–9):**

- Board/ACB approves the compliance policy and sets the review periodicity for compliance risk (para 6).
- **Annual compliance risk assessment and detailed annual review to the Board/ACB (para 7):**
  - compliance failures, losses, regulatory action and remedies;
  - the major regulatory guidelines issued in the year and the action taken;
  - fair practices code, SRO and accounting-standard compliance;
  - progress on audit and RBI inspection findings.
- Policy reviewed at least annually (para 8).
- **Policy contents (para 9):**
  - independence;
  - compliance-testing monitoring;
  - change-in-risk-profile reporting;
  - access to information;
  - dissemination of regulatory requirements and updating of operational manuals;
  - **Compliance Department approval of every new process and product before introduction** (para 9(7)).

**Scope and function (paras 10–17):**

- Scope includes conduct, conflicts of interest, fair treatment and suitability (para 10).
- **New products** are intensively monitored for at least the first six months (para 15(2)).
- **Compliance testing:**
  - sufficient and representative testing, with results to senior management;
  - compliance failures circulated with preventive instructions;
  - staff accountability examined for major failures (para 15(3)).
- **Risk Mitigation Plan / Monitorable Action Plan** points complied with on time; inspection compliance submitted to RBI only through the Compliance function (para 15(4)).
- Other regulators' discomfort and law-enforcement actions reported to RBI (para 15(5)).
- The function is the reference point for interpretation (para 16).
- The CCO is informed of compliance-related audit findings (para 17).

**CCO (paras 18–31):**

- Selected through a committee (para 18).
- Minimum tenure 3 years, relaxable by 1 year (para 21); premature transfer only with prior Board/ACB approval (para 22).
- No lower than two levels below the CEO (para 23).
- Quarterly one-to-one with the Board/ACB where the CCO reports to the MD & CEO (para 25).
- No business reporting line (para 26).
- **No dual hatting; on sanction or purchase committees, advisory role only** (para 27).
- Access to all records (para 28).
- **Prior intimation to the RBI SSM** for appointment, transfer, resignation or removal, with profile and the MD & CEO's Fit and Proper certificate (para 29).
- Nodal point for regulators (para 30).
- Member of the new-product committee, or evaluates each product (para 31).

**Technology (para 32).** A comprehensive, integrated, enterprise-wide, workflow-based solution that:

- supports collaboration;
- identifies, assesses, monitors and manages compliance requirements;
- escalates non-compliance;
- **records competent-authority approval for any deviation or delay in compliance submission**;
- gives senior management a **unified dashboard**.

Proportionality applies (para 33). *Finbyx's compliance module (M14) is designed to be this solution.*

---

## 8A.12 CYB — Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions (461)

**Applicability and repeal (paras 2–3, 155–156):**

- Immediate effect (para 2).
- Ch III: BL < ₹500 crore and all CICs. Ch IV: BL ≥ ₹500 crore. Ch V: TL/UL/ML, excluding CICs. Ch II para 6 applies to all.
- **The only asset threshold in the text is ₹500 crore.**
- Para 155 repeals the existing NBFC IT Framework and IT Governance instructions listed in circular DoS.CO.PPG.66/11.01.005/2026-27. The 2023 IT Governance MD is not named [VERIFY against the PPG.66 list].

**Board (para 6):** approves the technology and cybersecurity strategies and policies; reviews them at least annually.

**Chapter III baseline (para 8):**

- password and access control;
- defined roles;
- maker-checker;
- DSC, mobile financial services and social-media controls;
- **system-generated MIS** (revenue, expenses, segment cost-benefit, cost of funds);
- adequacy to file regulatory returns;
- BCP with annual Board reporting;
- backup with periodic testing.

**Chapter IV (BL ≥ ₹500 crore):**

- **ITSC:** independent-director chair; CIO/CTO members; ≤ 6 months between meetings (para 15).
- IT, InfoSec and Cyber policies (paras 18–22); CIO (para 18(2)); public-facing infrastructure **IPv6-capable** (para 18(4)).
- Asset inventory (para 21(1)).
- **SoD:** sysadmin vs DBA vs transaction processing (para 21(2)).
- **Delegated authority for changing key business parameters such as interest rates** (para 21(3)).
- Maker-checker by at least two individuals (para 21(6)).
- **Audit trails** sufficient for audit, forensics and dispute resolution, including unauthorised activity (para 21(8)).
- PKI (para 21(9)).
- Vulnerability management (para 23).
- CCMP covering detection, response, recovery and containment (para 25).
- **Incidents reported on DAKSH within 6 hours of detection** (para 28).
- DSC (para 31); mobile financial services with end-to-end encryption (para 33); training records (paras 35–36).
- Secure SDLC (para 39); change management (paras 41–42).
- **System-generated MIS** including system-driven SMA/NPA identification and system-driven fraud reporting (para 44).
- **System-driven returns, and read-only MIS access for RBI supervisors** (para 46).
- IS audit annually, preferably before the statutory audit (para 56); **audit-mode access for auditors and regulators** (para 57); CAATs (para 58).
- BCP tested at least annually and on significant change, using worst-case scenarios (para 59(4)); vendor cyber-resilience testing (para 59(5)).
- **Outsourcing (paras 60–64):**
  - risk assessment;
  - counsel-vetted contract with monitoring, data protection, access to records, **vendor retention of admin logs**, audit rights, copies of audit reports and RBI access (para 62);
  - vendor BCP assurance (para 64).

**Chapter V (ML/UL/TL):**

- **ITSC:** ≥ 3 directors, independent chair with ≥ 7 years' IT experience, quarterly (paras 71–72); approves the need-based access standard (para 73(8)).
- IT Steering Committee quarterly (para 75).
- **CISO** with no IT reporting line, manages the SOC, quarterly review (paras 81–82).
- CIA classification (para 91); EOS/AMC tracking and refresh plan (paras 92–93).
- **Data migration** audit trails and sign-offs (para 99); enterprise data dictionary (para 100).
- **DC and DR geographically separated** (para 102).
- **Vendor obligations (paras 104–106):**
  - support by agreement (para 104);
  - **source code of critical applications, or escrow including all updates and fixes** (para 105);
  - **certificate that the software is free of known vulnerabilities, malware and covert channels, at onboarding and on each material change** (para 106).
- Annual capacity review (paras 107–108).
- **Audit logging and logs (paras 109–114):**
  - audit logging in every application affecting critical data, with non-repudiation (paras 109–110);
  - regular log monitoring (para 111);
  - change and patch policy (para 112);
  - need-based access (para 113);
  - privileged activity logged and reviewed (para 114).
- **MFA for privileged users of critical systems and for critical activities**, risk-based (para 115); MFA for teleworking (para 116).
- Vendor risk assessment outside outsourcing (para 117); strong cryptography (para 118).
- **No manual intervention in data transferred between critical applications** (para 119); STP with authentication and audit trail (para 120).
- **VA/PT:**
  - VA at least every 6 months and PT every 12 months for critical and DMZ systems, plus pre- and post-implementation and after change, by independent experts (paras 121–122);
  - post-implementation tests on production (para 124);
  - time-bound fixes with no recurring CVEs (para 125);
  - CVSS scoring, including cloud (para 126).
- **BCP and DR:**
  - ISO 22301 (para 127);
  - **DR drills at least half-yearly** (para 129);
  - re-test of failures (para 130);
  - **DR as primary for at least one full working day, BOD to EOD** (para 131);
  - backup restore tests (para 133);
  - **minimal RTO approved by the ITSC and near-zero RPO for critical systems** (paras 134–135);
  - reconciliation method where RPO ≠ 0 (para 136);
  - identical DC/DR configuration (para 137);
  - **collaborative resilience testing with vendors against the NBFC's RTO** (para 138).
- **Incidents:** response policy (para 139); forensics and RCA (para 140); **DAKSH within 6 hours plus CERT-In (HFCs to NHB)** (para 141); vendor staff roles (para 142); communication (para 143); lessons learnt (para 145); drills with service providers (para 146); RTO/RPO metrics (para 147).
- **IS audit:** policy (para 150); risk-based (para 153); continuous auditing (para 154).

**Not prescribed:** numeric RTO, log-retention period, data localisation, MFA in Ch III/IV, or DAKSH reporting for Ch III. Finbyx's controls exceed these minimums by design.

---

## 8A.13 DPS — Digital Payment Security Controls Directions (462)

**Applicability:** only credit-card-issuing NBFCs. Scope covers every digital payment product and its non-financial functions (para 4(1)). For all other tenants, Finbyx adopts these controls as its voluntary baseline for M7, M22 and M23. Whether a loan-repayment app of a card-issuing tenant is in scope is a tenant-specific interpretation [VERIFY].

**Governance (paras 8–20):**

- Board policy on functionality, security and performance; multi-stage UAT (paras 8–10).
- External assessment (para 11); product-level risk limits (para 13); RCSA and vendor RCSA (para 16); capacity planning (para 19).
- **Half-yearly recovery test of backups and applications, without loss of transactions or audit trails** (para 20).

**Generic (paras 21–26):**

- secure protocols;
- no sensitive data in HTML hidden fields, cookies or client storage;
- **WAF and DDoS mitigation**;
- strong cryptography and certificate renewal;
- activity logging.

**AppSec (paras 27–40):**

- multi-tier, secure by design, threat modelling;
- **escrow for third-party payment applications** (para 31);
- **source review plus VA/PT covering OWASP; developer certificate; VA half-yearly, PT annually; penal clauses in vendor contracts** (para 32);
- continuous and **authenticated** scanning (paras 33–35);
- rogue-app monitoring (para 37);
- server-side authentication (para 38);
- APIs per OWASP (para 39);
- **masked account and card numbers in SMS/email** (para 40).

**Authentication (paras 41–51):**

- **MFA with at least one dynamic or non-replicable factor for payments** (para 41); adaptive authentication (para 43).
- **Alerts and MFA for all debits and credits, account-detail changes and limit changes** (para 46); merchant name in alerts (para 47).
- MITM/MITB protection (para 48); session termination with transaction resolution (para 49).
- **Lockout after failed attempts, with secure reactivation and alerts** (paras 50–51).

**Fraud and reconciliation:**

- Fraud rules for velocity, new accounts, geo/IP, mule VPAs and declined transactions (paras 52–56).
- **Reconciliation with all PSOs, gateways and aggregators within 24 hours of receiving the settlement file** (para 57).

**Customer protection (paras 58–66):**

- **non-skippable secure-usage guidance in the preferred language, recorded** (para 58);
- in-app grievance and ODR (paras 59–60);
- terms inside the product, no bundling, opt-in (paras 62, 65);
- **in-app "mark as fraudulent"** (para 66).

**Web (para 67):**

- CAPTCHA or adaptive authentication;
- secure cookies;
- virtual keyboard;
- inactivity timeout;
- forced change of system-issued passwords.

**Mobile (para 68):**

- server-side app-version check;
- **one live version, with older versions disabled within 6 months**;
- root/jailbreak and remote-access-app detection;
- published checksum or authorised store link;
- **device binding by hardware + software + SIM/service, with a device register and new-device alerts**;
- re-authentication at launch and after idle;
- unsecured-network detection;
- no credentials or keys on the device;
- encrypted local database;
- certificate validation;
- obfuscation.

**Card (para 69):**

- PCI-PIN/PTS/HSM/P2PE;
- card limits at card, BIN and NBFC level;
- **no plain-text card data at the NBFC or its vendors**.

---

## 8A.14 FRM — Fraud Risk Management Directions (463)

**Applicability (para 3).** Assessed on the audited balance sheet as on 31 March of the preceding year.

- HFC reporting under Chapters VI and VIII goes to NHB.
- The text has **no RFA category, no red-flag annex, no CIC reporting of fraud, and no provisioning rates**.

**Dates (para 4).** Capture all three:

- **Date of Occurrence**;
- **Date of Detection**;
- **Date of Classification**: the date the reasoned order is passed with competent-authority approval.

**Policy and natural justice (paras 5–7):**

- Policy reviewed at least once in three years.
- Detailed show-cause notice with transaction particulars, served on persons and entities, including third-party professionals (valuers, CAs, advocates, architects), promoters and whole-time/executive directors.
- **Not less than 21 days to respond.**
- A **reasoned order** stating the facts relied on, the submissions and the reasons.
- No statutory deadline for classification; it is time-bound per policy.

**Governance (paras 8–12):**

- **SCBMF:** ≥ 3 Board members incl. CEO/MD and 2 independent directors. ML and BL may use a Committee of Executives (≥ 3, incl. one whole-time director). A Board-set threshold decides which cases reach it.
- Periodic Board/ACB review (para 9).
- Whistle-blower mechanism (para 10).
- Senior official responsible (para 11).
- **Fraud amount disclosed in the Notes to Accounts** (para 12).

**EWS (Ch III, UL/ML only, paras 13–23):**

- policy-based, overseen by the RMC;
- tenant-defined quantitative and qualitative indicators for loan and non-loan transactions;
- validated;
- **integrated with the core system**;
- **every alert requires an examination decision**;
- real-time or minimum-lag monitoring, focusing on non-KYC and mule accounts;
- MIS and analytics unit.
- **No indicator list is prescribed.**

**Investigation (paras 24–31):**

- External or internal audit (para 25), with auditor timelines (para 26).
- **The loan agreement allows the lender to commission an audit**; if the audit is inconclusive or delayed by the borrower, the lender concludes on available material (para 27).
- Group companies with common promoters or whole-time directors are examined (para 29).
- The para 6 process also applies to suo-motu law-enforcement action (para 30).
- Third-party accountability clauses in contracts (para 31).

**Staff accountability (paras 32–34, 46):**

- Time-bound, in every case.
- Government NBFCs refer cases of ₹3 crore and above to ABBFF.
- Senior executives go through the ACB with recusal.
- Accountability also covers delays in detection or reporting.

**Penal measures (paras 35–39):**

- **Debarment** from raising funds or new credit from REs for **5 years from full repayment of the defrauded or settlement amount**, covering the person and associated entities (para 35).
- Lending after that is discretionary (para 36).
- After a resolution with change in control, the debarment lifts for the entity but not for the erstwhile promoters (paras 37–39).

**Reporting:**

- **Law enforcement:** immediately; mandatory at ₹1 lakh or more (para 40, footnote); nodal officer (para 41).
- **RBI:** 11 categories (para 42). **FMR irrespective of amount, immediately and not later than 14 days from classification**; updates via FUA (para 43).
- Frauds in unregulated group entities: by email to fmgconbfc@rbi.org.in (para 45).
- No naming of uninvolved persons (para 47).
- **Withdrawal** needs director-rank approval (para 48), or a court direction (para 49).

**Closure (paras 50–52):**

- Through the RBI closure module, after disposal of the law-enforcement/court case **and** completion of staff accountability (para 50).
- Statistical closure for cases ≤ ₹25 lakh pending more than 3 years from FIR (para 51).
- Closure records kept for auditors (para 52).

**Other (paras 53–58):**

- **Legal audit of title documents for facilities ≥ ₹1 crore until repaid** (para 53).
- **No sale to lenders or ARCs before the fraud investigation is complete; report to RBI before sale** (para 54).
- Auditors flag suspected fraud (para 55).
- Internal audit covers the fraud lifecycle (para 56).
- **Theft, burglary, dacoity and robbery (RBR):**
  - incident report by email within 7 days (para 57);
  - quarterly return on the portal within 15 days of quarter-end (para 58).

---

## 8A.15 AUD — Auditor's Report Directions (468)

**What the auditor reports, and therefore what Finbyx must evidence:**

- **All NBFCs (para 6):**
  - CoR held and the Principal Business Criteria met, with bank FDs excluded from financial assets (paras 6(1)–(2));
  - NOF as required (para 6(3));
  - **DNBS10 Statutory Auditor's Certificate** filed on CIMS within 5 working days of signing, and by 31 December at the latest.
- **Deposit-taking (para 7):**
  - deposit limits, rating, acceptance and defaults;
  - CRAR;
  - IRACP, investment valuation, concentration and accounting standards;
  - liquid assets and designated bank (DNBS03);
  - DNBS01/DNBS03 filed on time;
  - branch rules.
- **Non-deposit-taking (para 8):**
  - Board resolution on non-acceptance of public deposits;
  - no deposits accepted;
  - IRACP, investment and accounting standards;
  - **ML and above:** CRAR in DNBS03 correct and filed on time;
  - correct NBFC-MFI classification.
- **Other paras:**
  - para 9: conditions for companies advised that no CoR is needed;
  - para 10: reasons for any qualified statement;
  - **paras 11–12: exception report to the RBI SSM/RO** on any adverse para 6 item, or any non-compliance with Ch IIIB of the RBI Act or applicable Directions.

---

## 8A.16 Cross-module build list from Part 8A

The module specifications in Part 7 must include the items below. Where a module text and Part 8A differ, **Part 8A prevails** for these Directions.

| Module | Additions |
|---|---|
| M1 | **Branch/office regulatory master** (type, state, registered-office-state flag, NOF and rating snapshot for deposit-taking) with the BR para 6 gate. **Closure workflow:** two newspaper notices, closure ≥ notice + 3 months, customer re-mapping, 7-day RBI/NHB intimation (BR paras 10–15). **Entity regulatory profile flags:** layer, asset size (last audited), deposit-taking, public funds, customer interface, notified NBFC, IFC, NOFHC-held, credit-card issuer, Ind AS, cyber chapter |
| M3 | **Related-party register:** promoters, directors, KMP, major shareholders, specified employees and relatives, auto-matched on PAN/DIN (CRM 13K). **Connected-counterparty groups**, with control and economic-interdependence evidence (CON 4(3)). LEI record with expiry (CRM 19–24). CKYC number on customer and related parties (CIR 12(10)). Fraud register with associated entities (FRM 35) |
| M4 | **Pre-sanction gates:** related-party routing above the CRM 13G threshold to the Board or non-Audit Board committee, with recusal (13I–13J); exposure-limit check (CON); own-shares/own-debentures/IPO blocks (CF 104–105; CRM 14–15); LEI gate (CRM 20); fraud-debarment gate (FRM 35–39); **microfinance classifier** for any collateral-free loan to a household ≤ ₹3 lakh (CF 51); digital-loan capture of age, occupation and income, and no auto limit increase (CF 8); new-to-credit path, never auto-rejected for no history (CIR 38(5)); Notified-NBFC appraisal pack (CRM 6–8). **AA consent artefact** store, revocation and purpose limitation (AA 17, 20, 28). **Loan agreement clause:** the lender's right to commission a forensic audit (FRM 27) |
| M5 | CERSAI for all four CRM para 27 types; gold valuation (CF 40–42); LAS Annex-III reporting (CF 106); legal audit of titles for facilities ≥ ₹1 crore (FRM 53) |
| M6 | Gold renewal/top-up controls (CF 34). Demand/call recall and review dates (CF 107). Top-ups against depreciating movables treated as unsecured (CON 10). Closure feeds CIC closure reporting and centralised NOC (CIR 10(3), 38(1)) |
| M7 | Reconciliation within 24 hours of the settlement file; fraud rules engine; tokenised card data only (DPS 53, 57, 69) |
| M8 | **Recovery-agent particulars sent to the borrower before first contact on digital loans, with contact blocked until sent** (CF 9(6)). **Default/DPD alerts sent with each CIC submission** (CIR 34(1)(i)). Cash recovery posted in full to the borrower's account the same day (CF 10(5)) |
| M9 | **"Settled" vs "disputed" CIC logic and settlement reason** (CIR 12(2), 12(4)). IBC-admitted cases = suit-filed (12(7)). Related-party recusal on OTS, write-off, waiver and enforcement (CRM 13J). **SARFAESI possessed-asset website feed** (CIR 21, Annex IV). Fraud-account transfer gate (FRM 54) |
| M10 | **Investment portfolio module** (INV) and **disclosure engine** (FS 20–21, C.2, C.3). Impairment Reserve (FS 12(2)). SICR-rebuttal and > 90 DPD-not-impaired registers (FS 12(1)). Gold/silver % of assets (CF 50). Fraud amount note (FRM 12). Related-party loans note (FS 21(9A); CRM Annex I) |
| M11 | Co-lending escrow controlled only by the co-lenders (CF 10 note). Website list of active co-lending partners (FS 21(4)) |
| M12 | Exposure engine and limits for BL, ML and UL, LEF and breach block (CON). ALM and daily LCR engine (ALM). EWS and fraud lifecycle (FRM). CDS register (CRM 16–17) |
| M13 | New or corrected returns: DNBS04A/04B (ALM 57); Return on Large Exposures, monthly (CON 48); LE breach intimation (CON 45); CDS excess report, quarterly (CRM 17(7)); IRF data, half-yearly (INV 29); per-case FMR and FUA (FRM 43); RBR within 7 days and quarterly (FRM 57–58); DNBS10 SAC support (AUD 6); CIMS DLA Annex-I (CF 18); LAS Annex-III pledge report (CF 106); public liquidity disclosure, quarterly (ALM 15; FS 21(13)); LCR disclosure from daily values (FS C.2(32)); branch-closure intimation (BR 12) |
| M14 | **Compliance Function workflow suite** (CMP 6–33): annual compliance risk assessment and Board review generator, product/process approval gate, 6-month new-product monitoring, compliance testing, RMP/MAP tracker, CCO governance register and SSM intimations, deviation approvals, unified dashboard. **Applicability engine** driven by the entity profile |
| M15 | **Credit-information complaint workflow** with 21/30-day clocks, ₹100/day compensation, apportionment and 5-day payout (CIR 34–35). Digital-lending grievance escalation text (CF 12) |
| M17 | Board/committee packs: annual compliance review (CMP 7), compliance testing (CMP 15(3)), SCBMF fraud review (FRM 8), EWS effectiveness (FRM 14, 21), DQI and RCA reviews (CIR 17, 34(4)), ALCO pack (ALM), LE return (CON) |
| M19 / M21 / M22 / M23 | **Read-only "RBI Supervisor" and "Auditor (audit-mode)" roles** (CYB 46, 57). MFA for privileged and critical actions (CYB 115). Delegated authority for parameter changes such as interest rates (CYB 21(3)). STP with no manual edits of inter-system files (CYB 119). **DLA permission and biometric limits** (CF 13–14). DPS controls for payments, mobile and web (DPS 41–68) |
| Workspace L | **Auditor evidence packs** (AUD 6–8): PBC test and NOF computation, Board resolution on deposits, IRACP/investment/concentration compliance, CRAR with DNBS03 lineage, MFI qualifying-asset test, exception-report register (AUD 11), fraud closure files (FRM 52) |


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
| KYC and identity | Surepass (primary), Signzy, IDfy, HyperVerge, Digio, Decentro; CKYCR (CERSAI / CKYCRR 2.0); DigiLocker; UIDAI OKYC; Protean (formerly NSDL e-Gov) / UTIITSL PAN; V-CIP |
| Credit bureaus | TransUnion CIBIL, Experian, Equifax, CRIF High Mark (pull APIs and UCRF submission) |
| Financial data | Account Aggregator: the tenant (FIU) connects to licensed NBFC-AAs (e.g. Finvu, Anumati) directly or through an FIU gateway/technology provider (e.g. Setu, FinBox). Record the AA and the gateway separately [VERIFY licences]. Deposit-taking tenants also need an FIP endpoint (AA para 29); bank-statement analysers (Perfios, FinBox, Scoreme); GSTN; ITR/AIS; EPFO; MCA; Udyam; ULI (RBIH Unified Lending Interface) where the tenant is onboarded |
| Collateral | NSDL and CDSL pledge/eLAS APIs; CAMS/KFintech/MF Central lien (verify current access terms); Vahan; CERSAI; state land records (through ULI or vendors); gold-rate feeds; valuer and legal-vendor portals |
| eSign and eStamp | Leegality, Digio, eMudhra, Protean eSign, Surepass; SHCIL e-stamping; NeSL DDE |
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
| Internal web app (all workspaces) | Next.js 16 (App Router) + React 19 + TypeScript; shadcn/ui + Tailwind with design tokens; TanStack Query; TanStack Table v9 or AG Grid Community (MIT) for data-dense grids. AG Grid Enterprise (paid: grouping, server-side row model, Excel export) only after a licence ADR | Complex workflows, large tables, theming |
| Backend | Node.js LTS + TypeScript; **NestJS 11 modular monolith** (or Fastify with explicit modules), with strict domain boundaries; OpenAPI 3.1 via Zod schemas | Business rules, integrations, controlled access |
| Database | PostgreSQL 16+ (Supabase now; Amazon RDS/Aurora PostgreSQL later); **Drizzle ORM or Kysely** for SQL control; versioned SQL migrations | Relational, transactional ledger; portable |
| Money and maths | `NUMERIC` columns; `decimal.js` (precision ≥ 40); property-based tests (fast-check) for schedule/allocation invariants | Paisa-exact accuracy |
| Workflow orchestration | **Temporal** (TypeScript SDK; Temporal Cloud has AWS Mumbai/Hyderabad regions, or self-host) for long-running sagas: origination, disbursement, mandate presentation and retries, legal timelines, COB orchestration. Encrypt workflow payloads with a client-side codec so no PII sits in Temporal history. pg-boss or Graphile Worker for simple jobs | Durable, retry-safe, auditable workflows |
| Rules / BRE | **GoRules ZEN engine** (JDM decision tables/graphs; MIT licence; Node bindings) with versioned rules stored in Postgres and the open-source JDM editor component for business users (the hosted GoRules BRMS is commercial) | Credit policy, pricing grids, deviations, eligibility |
| Events | Transactional outbox → queue/stream (start with Postgres-backed queue or Redis Streams; move to Amazon MSK/Redpanda + Debezium CDC on AWS) | Reliable integration events |
| Authentication | Supabase Auth now, **behind an OIDC abstraction**; Keycloak or Amazon Cognito later; SSO/SAML for bank tenants; MFA mandatory for staff | Portability |
| Authorisation | Server-side policy layer: RBAC + ABAC (Cedar or OpenFGA for hierarchy/amount limits) **plus Postgres Row-Level Security** as defence-in-depth for tenant/entity/branch isolation | Least privilege; Supabase must not be the only security boundary |
| Documents | S3-compatible private storage (Supabase Storage → Amazon S3) with SSE-KMS; docxtemplater/Handlebars templates → Gotenberg (HTML/DOCX → PDF) | Agreements, KFS, CAM, letters |
| Search | PostgreSQL FTS + pg_trgm first; OpenSearch later | Customer and loan search |
| Reporting/BI | Regulatory returns in code. Apache Superset (Apache-2.0; guest-token row-level security) for embedded MIS. Metabase only if its paid embedding/sandboxing tier is licensed. Cube semantic layer optional | Self-service MIS |
| Observability | OpenTelemetry → Grafana (Loki/Tempo/Mimir, self-hosted in India) or AWS-native; Sentry self-hosted, or SaaS with no PII (Sentry SaaS stores data in the US/EU); PII-scrubbing log processors; security audit events | Production support and traceability |
| Infrastructure | Docker. **Development and staging (synthetic data only):** Railway (no India region; nearest is Singapore) + Supabase. **Any environment holding real borrower data:** India-region hosting only — Supabase ap-south-1 with an India-region compute host, or directly AWS ap-south-1 (primary) and ap-south-2 (DR) on ECS/EKS — provisioned with OpenTofu/Terraform or AWS CDK. KMS/CloudHSM for signing and field-encryption keys. Aadhaar vault per UIDAI Circular 14 of 2025. Secrets Manager; WAF | Data localisation, scalable, portable |
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
27. **Data localisation.** All production data, backups and logs stay in India. For digital lending, data processed abroad must be deleted there and repatriated within 24 hours (CF para 14(4)). The Cyber Directions themselves contain no localisation clause. Every SaaS sub-processor must be confirmed India-resident in an ADR; otherwise, self-host it or send it no personal data. This covers Supabase, the compute host, Temporal Cloud, Sentry/Grafana, LLM endpoints, and email/SMS/WhatsApp vendors.
28. **Privacy by design.** Consent lineage, purpose limitation, minimisation, masking in UI by role, and a retention engine.
29. **Scalability.** Design for at least 100 lender tenants, 10 million+ loan accounts and tens of millions of ledger entries a month, with partitioned tables (by tenant and date), read replicas for reporting, and horizontally scalable COB workers.
30. **Portability.** Containerised, environment-based config, storage and auth abstractions, IaC. Do not build an elaborate cloud-neutral platform before the product is validated.
31. **Straight-through processing.** No manual editing of data passed between Finbyx and other applications: CIC/CIMS files, GL/Tally, co-lender files, payment files. Generated files are hashed and signed, and the hash is verified on upload. Exceptions go through maker-checker with an audit trail (CYB paras 119–120).
32. **Regulator and auditor access.** Built-in, time-boxed, read-only roles over MIS, audit trails and evidence (CYB paras 46, 57).
33. **IPv6.** All public endpoints are dual-stack IPv4/IPv6 (CYB para 18(4)).
34. **System-driven regulatory outputs.** SMA/NPA identification, fraud reporting and returns are system-generated, never spreadsheet-compiled (CYB paras 44, 46).

## 10.3 Non-functional targets (initial — confirm in Phase 0)

| Area | Target |
|---|---|
| Availability (production) | 99.9% monthly for staff app and APIs; COB must not block branch operations |
| Latency | p95 < 300 ms for reads, < 800 ms for standard writes, excluding third-party calls |
| COB | 1 million active loans processed in < 60 minutes on reference infrastructure, with linear scale-out |
| RPO / RTO | Near-zero RPO for the ledger (synchronous replica / PITR). The Cyber Directions set no numeric RTO: Ch V requires a minimal RTO approved by each NBFC's ITSC, a near-zero RPO for critical systems, and a reconciliation method where RPO ≠ 0 (CYB paras 134–136). Finbyx default RTO ≤ 4 hours, with a tighter per-tenant tier so each ML+ tenant's ITSC-approved RTO is met contractually (para 138) |
| DR drills | Half-yearly for critical systems for Chapter V entities (Cyber Directions para 129); annual BCP test for Chapter IV; restore tests at least quarterly |
| DR architecture | DC and DR geographically separated, e.g. ap-south-1 / ap-south-2 (CYB para 102); identical configuration and patches through IaC, with a drift check (para 137). A single-region deployment is not acceptable for Ch V tenants in production |
| DR switchover | Half-yearly platform drill running production on DR for one full business day, BOD to EOD including COB, with a tenant evidence pack; failures re-tested (CYB paras 129–131, 138) |
| Backup | Encrypted, immutable backups; quarterly restore test; half-yearly recovery test without loss of transactions or audit trails (DPS para 20 baseline) |
| Log retention | Configurable per tenant; the longest of the applicable legal and tenant-policy periods [VERIFY each]. The Cyber Directions prescribe none (CYB para 110) |
| Concurrency | 1 million+ borrower-portal users; 50,000 concurrent staff and field sessions across tenants (validate in Phase 0) |
| Security | OWASP ASVS Level 2 baseline. VA at least every 6 months and PT at least every 12 months on production by an independent CERT-In-empanelled firm, plus pre- and post-go-live and after major change (CYB paras 121–124; DPS para 32). Incident notice to the tenant fast enough for its DAKSH filing within 6 hours of detection (CYB paras 28, 141) |
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
  - joiner-mover-leaver automation;
  - MFA mandatory for privileged users and critical actions — disbursement approval, rate/parameter change, user-rights change, bulk export (CYB para 115);
  - PAM with session recording;
  - monthly review of elevated-user activity (CYB para 114);
  - SoD between sysadmin, DBA and transaction roles (CYB para 21(2)).
- **Application security:**
  - input validation (Zod);
  - output encoding;
  - CSRF protection;
  - rate limiting;
  - signed short-lived document URLs;
  - IDOR/BOLA tests on every endpoint;
  - webhook signature verification and replay protection;
  - file-upload scanning (antivirus, type and size checks);
  - WAF and DDoS protection on every internet endpoint (DPS para 23);
  - no sensitive data in cookies, hidden fields or client storage (DPS para 22);
  - masked account and card numbers in SMS/email (DPS para 40);
  - threat model per module; SAST and source review per release; authenticated scanning (DPS paras 29–35);
  - CVSS-based remediation SLAs, with no recurrence of known CVEs (CYB paras 125–126).
- **Supply chain:**
  - SBOM;
  - dependency scanning;
  - signed builds;
  - pinned versions;
  - secret scanning in CI;
  - a source-code-escrow deposit of every production release (CYB para 105; DPS para 31);
  - a signed certificate per material change that the software is free of known vulnerabilities, malware and covert channels (CYB para 106);
  - an EOS register and technology refresh plan (CYB paras 92–93).
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

## 10.6 Vendor obligations Finbyx must meet as a service provider to regulated lenders

Finbyx is an IT service provider to its tenants. Build these obligations into the product, the contracts and the evidence packs:

1. **Contract clauses** (CYB para 62; the Outsourcing Directions [VERIFY]):
   - continuous monitoring by the NBFC;
   - data-protection systems;
   - access to books, records and information;
   - **retention of administrative audit trails and logs**, accessible on approved request;
   - audit rights for internal or external auditors;
   - copies of Finbyx's audit reports;
   - RBI access to data within reasonable time.
2. Maintenance and support under a formal agreement and SLA (CYB para 104).
3. **Source code of critical applications, or source-code escrow** with an independent agent. Deposit every release including fixes, with a verified build (CYB para 105; DPS para 31).
4. **Security certificate:** a written certificate that the software is free of known vulnerabilities, malware and covert channels.
   - Issue it at onboarding and on each material change, using an agreed materiality definition (CYB para 106).
   - For card issuers, issue it annually if the application changed.
   - Accept penal clauses (DPS para 32).
5. **Testing:** independent VA every 6 months and PT annually, and on major change. Share the reports and remediation status (CYB paras 121–126).
6. **Incidents:** notify the tenant fast enough for its DAKSH filing within 6 hours; support forensics and RCA; take part in crisis drills (CYB paras 28, 140–146).
7. **BCP and DR:** geographically separated sites; half-yearly full-day DR drills; collaborative resilience tests against each tenant's RTO; proactive BCP assurance (CYB paras 59(5), 64, 102, 129–138).
8. **Staff and policy:** comply with tenant InfoSec and acceptable-use policies; background-screen privileged staff (CYB paras 21(4), 97).
9. **Disclosures to tenants:**
   - RCSA;
   - sub-processor list for concentration and supply-chain assessment;
   - SBOM;
   - EOS dates;
   - asset inventory and CIA classification for Finbyx-hosted assets (CYB paras 21(1), 91–92, 117; DPS para 16).
10. **Card data:** none stored in plain text; PCI confirmations where in scope (DPS para 69).
11. **Regulator and auditor access:** read-only RBI and auditor access to tenant data and MIS on request (CYB paras 46, 57, 62).
12. **Certifications:** keep ISO 27001 and SOC 2 Type II. Lenders expect these, though the Directions do not mandate them.

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

Build a common platform first, then launch a **narrow MVP pilot** before expanding:

- **MVP product scope:** an unsecured Personal Loan + an unsecured MSME Term Loan, branch-assisted, for a single NBFC pilot tenant.
  - Development and staging use synthetic data only.
  - The pilot goes live only on India-region hosting (Part 10.1).
- **Next:** LAP/Home (secured property), Vehicle, Gold, LAS and co-lending.
- **Last:** the specialist products (13–16), after feasibility approval.

How to run the phases:

- Each phase ends with a review gate.
- Copy one **"Instruction to Claude"** block into Claude Code when you start that phase. Do not paste several phases at once.
- Split large phases into sub-modules.
- **Phase P (pilot go-live)** comes before the expansion phases (17–20).

| Phase | Primary outcome | Depends on |
|---|---|---|
| 0. Repository audit and architecture | Verified repo facts; audit of the current Finbyx product; competitor benchmark; architecture proposal; ADRs; Fineract adoption decision; regulatory register v1 | — |
| 1. Platform foundation | Monorepo, CI/CD, environments, auth abstraction, design system, observability | 0 |
| 2. Database, tenancy and security foundation | Tenant/entity/branch model, RBAC/ABAC, enforced RLS, audit events, maker-checker framework, isolation tests | 1 |
| 3. Masters, configuration and product factory | Org hierarchy, calendars, masters, product factory, charges, rule packs, workflow designer v1 | 2 |
| 3b. Communications foundation | M18 templates, DLT/WhatsApp/email channels, consent and preference store, contact-policy engine skeleton | 2 |
| 4. Ledger and accounting core | CoA, journal engine, posting rules (including Ind AS deferred-fee postings), period close, trial balance — **before** any loan money moves | 2 |
| 5. Schedule and allocation engine | Fineract-equivalent schedules and allocation strategies, replay, Fineract oracle fixtures, golden cases | 3, 4 |
| 6. Customer, KYC and consent | CIF, de-dupe, KYC adapters (mock → Surepass sandbox), consent ledger, AML screening | 2 |
| 7. Origination (LOS) | Leads, applications, bureau/AA, BRE, verifications, deviations/DoA, CAM, sanction, KFS | 3b, 5, 6 |
| 8. Documentation, eSign/eStamp, DMS, disbursement | Templates, signing evidence, physical-execution path, OTC/PDD, mandate registration, payout, loan booking | 7 |
| 8b. Field app foundation | Expo app shell, offline sync, device binding, assisted KYC/document capture | 2, 6 |
| 8c. Udofin / LSP inbound connector (minimal) | LSP contract v1, application intake, status callbacks, signing-evidence intake, disbursement and repayment events | 7, 8 |
| 9. Servicing (LMS) and COB | Accruals, EIR amortisation stub, repayments, prepayment/foreclosure, resets, restructuring, service requests, COB with classification | 5, 8 |
| 10. Payments and reconciliation | eNACH/UPI AutoPay presentation, bounces, virtual accounts, BBPS, payment-gateway links, three-way reconciliation | 9 |
| 11. Collections | Strategies, allocation, telecalling, field collections, agencies, contact-policy engine, call recording | 3b, 8b, 9, 10 |
| 12. Recovery and legal (unsecured) + Equator | Sec 138 / Sec 25 PSS Act, arbitration and mediation via Equator, Lok Adalat, IBC/NeSL, OTS, write-off, wilful defaulters | 11 |
| 13. Finance: Ind AS 109, IRACP, GST/TDS, borrowings, Tally/SAP | EIR, ECL, provisioning, tax, liabilities, accounting integrations, financial statements | 4, 9 |
| 14. Regulatory reporting, risk and compliance | CIC UCRF, CIMS returns, CRILC/FMR as applicable, FIU-IND, ALM, concentration, ICAAP mart, compliance module, LawDocsComply bridge | 9, 13 |
| 15. Grievance, borrower portal and feedback | Complaints, Internal Ombudsman, RB-IOS 2026, Equator referral (re-using the Phase 12 ODR adapter), borrower portal, feedback | 3b, 9, 12 |
| **P. MVP hardening and pilot go-live** | E2E, independent VAPT, COB load test, DR restore drill, India-region production cut-over for the two MVP products | 0–15 (Phase 14 only for the returns that apply to the pilot's layer) |
| 16. Partner connectors, co-lending and DA | Full LSP framework, DLG ledger, co-lending/DA/securitisation engine, partner portals | 8c, 9, 10, 13, 14 |
| 17. Secured products expansion | LAP/Home, Vehicle, Gold, LAS/LAMF templates; collateral flows; SARFAESI; repossession and auction | P, 12 |
| 18. Analytics, AI layer and MCP | MIS catalogue, BI embedding, governed AI copilots, read-only MCP server | P |
| 19. Migration tooling | Legacy loan boarding and reconciliation sign-off | 9, 13 |
| 20. Scale hardening and AWS migration | Multi-tenant scale tests, AWS ap-south-1 / ap-south-2 migration, DR at scale, performance tuning | P, 16–19 |

### Phase 0 — Repository audit and architecture

> **Instruction to Claude:** "Read docs/00-master-prompt.md in full (Parts 1–13, Appendices A–E and Sources). Inspect the connected repository, branch, files, Git status and tooling, and report them. Do not write application code and do not modify the repository yet. Produce:
>
> 0. An audit of the **current Finbyx product and website**: features, data model, known defects and loopholes, and the customers or data that will need migration.
> 1. The architecture proposal: system context, the modular-monolith module map with data ownership, and the tenancy and authorisation strategy (API + service + enforced RLS).
> 2. The Apache Fineract adoption ADR, comparing headless Fineract, a TypeScript re-implementation, and a hybrid with Fineract as test oracle. Give a recommendation and the licence approach.
> 3. Technology ADRs, after checking the current stable version and licence of each proposed tool. Include an **India data-residency check for every hosting and SaaS sub-processor**.
> 4. The proposed repository structure, using Appendix C as the starting point.
> 5. The initial entity model, using Appendix D.
> 6. API boundaries and the outline of the Udofin/LSP integration contract.
> 7. Regulatory register v1:
>    - load every Part 8A requirement with its REQ-ID (these paragraphs are already verified against the official texts in docs/regulations/rbi/);
>    - confirm that every other instrument in Part 8.2 exists, with its title, number, date and current status;
>    - list every [VERIFY] item in Parts 4–10, with the phase in which it will be verified in depth;
>    - fully verify now only the items that Phases 1–5 depend on.
> 8. The phased roadmap, with dependencies and acceptance criteria.
> 9. The minimum security, testing and code-review gates.
> 10. The list of business decisions you need from me (Appendix B).
> 11. A competitor benchmark of Indian and global LOS/LMS/collections platforms (features, UX, pricing signals), with the gaps Finbyx should close.
>
> Present all of this for my approval before modifying the repository."

### Phase 1 — Platform foundation

> **Instruction to Claude:** "On branch `feat/platform-foundation`, initialise the approved monorepo. Set up:
>
> - pnpm + Turborepo, TypeScript strict, ESLint/Prettier;
> - the `apps/web` (Next.js), `apps/api` (NestJS) and `apps/worker` skeletons;
> - the `packages/` for contracts, domain-kernel (money, dates, IDs), ui (design tokens + shadcn), config and testing;
> - Docker Compose for local Postgres, Temporal and Gotenberg;
> - GitHub Actions CI (lint, typecheck, test, build, secret scan, dependency scan);
> - `.env.example` files;
> - an OpenTelemetry baseline, with PII scrubbing and India-resident error tracking per the ADR;
> - Storybook.
>
> Implement the domain-kernel `Money` and `Rate` types on decimal.js (precision ≥ 40, explicit rounding policies), with property-based tests. Build no business features yet. Open a PR with the test output."

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
> - server-side authorisation (RBAC + ABAC);
> - Postgres RLS on every tenant-scoped table, **enforced**:
>   - the API connects as a non-owner role without BYPASSRLS;
>   - every tenant table uses `ALTER TABLE … FORCE ROW LEVEL SECURITY`;
>   - tenant, entity and branch context is set with `SET LOCAL` / `set_config(…, true)` inside every transaction, so it works with transaction pooling;
> - the auth abstraction over Supabase Auth, with MFA for staff;
> - the generic maker-checker framework.
>
> Write tenant-isolation and privilege-escalation tests that try to read and write across tenants, entities and branches, and prove they fail. Include a test proving that a query run without tenant context returns zero rows. Report results."

### Phase 3 — Masters, configuration and product factory

> **Instruction to Claude:** "Build:
>
> - org hierarchy, holiday calendars and business-date management;
> - masters (pincode, IFSC, purpose and sector codes, reason codes, NACH return codes as configurable data);
> - the product factory implementing every Fineract-equivalent parameter in Part 4.2A, with validation guard-rails from the regulatory rule packs (Part 10.2 #24);
> - the charges engine with GST profiles, including the penal-charge GST flag;
> - effective-dated versioning and maker-checker for all configuration.
>
> Produce the product specification template `docs/products/_template.md` and the first two product specs (Personal Loan, MSME Term Loan) for my approval."

### Phase 3b — Communications foundation

> **Instruction to Claude:** "Build the M18 foundation:
>
> - multilingual, versioned template management with approval workflow and DLT template IDs;
> - SMS (DLT), WhatsApp Business Cloud API and email adapters (mock + sandbox);
> - consent, preference and DND store;
> - the effective-dated **contact-policy engine**, with separate recovery and sales/marketing windows (Part 7, M8 and M18).
>
> Later phases (KFS delivery, reminders, default intimation, collections) must use this module, not their own messaging code."

### Phase 4 — Ledger and accounting core

> **Instruction to Claude:** "Before any loan money moves, build the double-entry ledger:
>
> - chart of accounts with the NBFC Ind AS template;
> - append-only journals with database-enforced balance;
> - reversal-only corrections;
> - value, business and system dates;
> - period locks;
> - materialised balances;
> - trial balance;
> - accounting rule mapping (Fineract mapping keys + India extensions);
> - sub-ledger framework;
> - reconciliation checks.
>
> For Ind AS entities, the posting matrix must defer processing fees and directly attributable costs at disbursement (deferred-fee/cost accounts), so nothing has to be re-posted when EIR amortisation arrives. Write golden test cases for every posting rule, and property tests proving the ledger always balances. Show me the posting matrix for approval."

### Phase 5 — Schedule and allocation engine

> **Instruction to Claude:** "Implement the loan calculation engine as pure functions over an immutable loan event log. Cover:
>
> - EMI and equal-principal;
> - declining and flat;
> - daily and period interest;
> - day-count conventions;
> - broken period;
> - grace and moratorium;
> - tranches;
> - step-up/down and balloon;
> - interest recalculation and all four prepayment outcomes;
> - all allocation strategies, including the RBI-order rule set (Part 4.2B);
> - back-dated replay with snapshots.
>
> Run Fineract 1.15.0 (PostgreSQL 18, large runner) as a **nightly or on-demand oracle job**, not on every PR. Generate versioned golden fixtures (JSON) across a scenario matrix that uses the correct Fineract engine (CUMULATIVE or PROGRESSIVE) for each scenario. PR CI compares Finbyx output against these fixtures. Report paisa-level differences and classify each as a bug or an approved deviation."

### Phase 6 — Customer, KYC and consent

> **Instruction to Claude:** "Build:
>
> - the CIF with relationships;
> - de-dupe;
> - risk categorisation;
> - the consent ledger with exact notice versions;
> - KYC flows (CKYC search/download/upload, OKYC/DigiLocker, PAN, V-CIP hooks, OVD capture);
> - sanctions and PEP screening;
> - the periodic-updation scheduler.
>
> Adapters: mock first, then a Surepass sandbox adapter behind `KycProvider`. Never store the full Aadhaar number unless the vault design approved in Phase 0 meets UIDAI Circular No. 14 of 2025. Prefer OKYC/DigiLocker flows that avoid storage. Verify the current KYC Directions paragraphs and record them in the register."

### Phase 7 — Origination (LOS)

> **Instruction to Claude:** "Implement:
>
> - leads, and DSA/connector management with payouts;
> - dynamic application forms from product templates;
> - bureau and AA adapters (mock + sandbox);
> - the GoRules-based BRE with simulation;
> - verification management (FI/PD/technical/legal/RCU) with vendor allocation;
> - the deviation matrix and DoA routing;
> - the CAM generator (template + AI-drafted narrative with citations, edited by a human, locked at sanction);
> - sanction;
> - the KFS/APR engine per RBC para 29 and Annex I, with the KFS **validity period** (≥ 3 working days, or ≥ 1 for tenor < 7 days). This is not a waiting period.
>
> Model the application state machine explicitly. Include a full E2E test from lead to sanction for the two MVP products."

### Phase 8 — Documentation, execution, DMS and disbursement

> **Instruction to Claude:** "Build:
>
> - document templates and generation (Gotenberg);
> - eSign, eStamp and NeSL DDE adapters that store verifiable signing evidence;
> - the physical-execution path for instruments the IT Act First Schedule excludes (DP notes and other negotiable instruments except cheques, powers of attorney, immovable-property conveyances);
> - the DMS with hashes, versions, retention and access logs;
> - OTC/PDD tracking;
> - mandate registration (eNACH/UPI AutoPay);
> - the disbursement memo with pre-disbursement checks;
> - penny-drop and payout adapters with duplicate-payment prevention;
> - atomic loan booking with opening entries, including Ind AS deferred fees.
>
> Interest starts from the actual disbursement date. Include cooling-off handling for digital loans."

### Phase 8b — Field app foundation

> **Instruction to Claude:** "Scaffold `apps/field` (Expo React Native + TypeScript). Build:
>
> - offline-first storage and sync with conflict resolution;
> - device binding and remote wipe;
> - just-in-time permissions (camera and location only when needed; never contacts, SMS or call logs);
> - assisted KYC and document capture;
> - FI/PD report capture.
>
> Plan distribution through managed Play Store/App Store or MDM, with a forced-update policy for incompatible versions."

### Phase 8c — Udofin / LSP inbound connector (minimal)

> **Instruction to Claude:** "Implement LSP contract v1 per Part 5:
>
> - OpenAPI/AsyncAPI;
> - signed webhooks;
> - idempotency;
> - application intake with consent artefacts;
> - status and decision callbacks;
> - KFS and sanction publication;
> - intake of signing evidence;
> - disbursement and repayment events;
> - daily reconciliation file.
>
> Add Pact contract tests with Udofin. Prove that Finbyx keeps operating when Udofin is unavailable."

### Phase 9 — Servicing (LMS) and COB

> **Instruction to Claude:** "Build:
>
> - the loan 360 view;
> - daily accrual;
> - an EIR amortisation stub driven by the Phase 4 rules;
> - penal charges as charges;
> - repayments with allocation;
> - part-prepayment and foreclosure quotes with the prepayment-charge engine (RBC paras 33–34);
> - floating-rate resets with borrower options;
> - restructuring and rescheduling with classification impact;
> - top-up and balance transfer;
> - service requests and certificates;
> - closure, NOC, and the document-release SLA with compensation;
> - write-off.
>
> Build the COB orchestrator using the two-pass design in Part 4.2E:
>
> - per-loan pass A;
> - a cross-loan barrier for borrower-level SMA/NPA classification and upgrade;
> - per-loan pass B for income recognition and derecognition, EIR and provisioning.
>
> Add catch-up, inline COB, partitioned workers and the EOD exceptions dashboard. Load-test COB at 1 million loans."

### Phase 10 — Payments and reconciliation

> **Instruction to Claude:** "Build:
>
> - the mandate lifecycle;
> - the presentation engine per sponsor bank, with cut-offs;
> - re-presentation, and bounce processing with charges;
> - UPI intent, QR and payment links;
> - virtual accounts;
> - the BBPS biller adapter;
> - branch cash and cheque deposit tracking;
> - three-way reconciliation with exception queues and suspense ageing.
>
> A provider success response never finalises a payment without settlement confirmation. Add Stripe/PayPal adapters only for cross-border or SaaS billing, with an ADR."

### Phase 11 — Collections

> **Instruction to Claude:** "Verify the RBC Third Amendment Directions, 2026 text first. Then build:
>
> - segmentation and bucket strategies triggered by COB DPD changes;
> - rule-based allocation;
> - the telecalling workspace with dispositions and PTP;
> - field collections in the field app (offline, geo-tag, digital receipts, cash limits, same-day deposit);
> - agency management with the IIBF certification register;
> - the effective-dated contact-policy engine from Phase 3b (current RBC paras 89–100; paras 100A–100AB from 1 Jan 2027);
> - mandatory call recording and retention (para 100P);
> - pre-visit intimation (para 100L) and visit conditions (para 100Y(5));
> - borrower default/DPD alerts sent with each CIC submission (CIR para 34(1)(i)), and recovery-agent particulars sent before first contact on digital loans (CF para 9(6))."

### Phase 12 — Recovery and legal (unsecured) + Equator

> **Instruction to Claude:** "Build:
>
> - legal case management;
> - the Sec 138 NI Act and Sec 25 PSS Act workflows, with statutory timelines and templates;
> - arbitration and mediation referral to Equator through the ODR adapter, with outcomes flowing back;
> - Lok Adalat;
> - the IBC/NeSL IU filing workflow;
> - the OTS/settlement calculator with approval matrix;
> - the wilful-defaulter workflow;
> - write-off and post-write-off recovery accounting.
>
> SARFAESI, repossession and auction are built in Phase 17, with the secured products."

### Phase 13 — Finance, Ind AS 109 and accounting integrations

> **Instruction to Claude:** "Implement:
>
> - EIR (IRR-based) and amortisation;
> - ECL staging with a pluggable model and a default provision matrix;
> - parallel IRACP provisioning by layer, with Impairment Reserve logic;
> - GST invoicing and extracts (NBFCs are exempt from e-invoicing), and TDS;
> - bank reconciliation;
> - the borrowings/liabilities module;
> - month-end close;
> - financial statements per Schedule III (Division III for Ind AS, Division I otherwise) and the FS Directions disclosure engine (Part 8A.8), including the Impairment Reserve, the IRACP-vs-Ind AS table, and the SICR-rebuttal and > 90 DPD-not-impaired registers;
> - the investment portfolio module (Part 8A.5);
> - TallyPrime (local connector, JSON), SAP and Zoho adapters, with reconciliation.
>
> Our finance reviewer must approve the golden cases."

### Phase 14 — Regulatory reporting, risk and compliance

> **Instruction to Claude:** "Build:
>
> - CIC UCRF generation on the current reference dates, with rejection handling;
> - the CIMS/XBRL return framework with lineage and certification (start with the returns that apply to the pilot tenant's layer);
> - CRILC where applicable;
> - the fraud module's per-case FMR/FUA, law-enforcement reporting, closure and RBR (Part 8A.14);
> - FIU-IND reports;
> - the ALM engine and daily LCR (Part 8A.7), with DNBS04A/04B and the public liquidity disclosure;
> - the exposure engine, Large Exposure return and breach block (Part 8A.4);
> - the Compliance Function suite (Part 8A.11);
> - Auditor's Report evidence packs and DNBS10 (Part 8A.15);
> - the AA consent-artefact store (Part 8A.10);
> - the ICAAP data mart;
> - the model inventory;
> - the embedded compliance module (register, controls testing, calendar, product approval);
> - the LawDocsComply bridge, with the compliance-mode and grievance-host switches.
>
> Verify every return specification against the RBI (NBFC – Supervisory Returns) Directions, 2026."

### Phase 15 — Grievance, borrower portal and feedback

> **Instruction to Claude:** "Build:
>
> - the complaint management system, with automated Internal Ombudsman escalation where applicable, and RB-IOS 2026 support;
> - Equator referral, re-using the Phase 12 ODR adapter;
> - the AI support assistant, restricted to approved sources;
> - the optional borrower self-service portal;
> - feedback (CSAT/NPS, plus sales feedback within 30 days under RBC para 101Y).
>
> Use the Phase 3b communications module for all messages."

### Phase P — MVP hardening and pilot go-live

> **Instruction to Claude:** "For the two MVP products and the pilot tenant, deliver:
>
> - a full E2E regression;
> - independent VA and PT on production by a CERT-In-empanelled firm, CVSS-scored, with all Critical/High findings closed and re-tested (CYB paras 121–126);
> - a source-code-escrow deposit and the vendor security certificate for the release (CYB paras 105–106);
> - a COB load test;
> - a DR switchover drill running production on the DR site for one full business day including COB, with post-drill reconciliation (CYB paras 129–137);
> - an incident drill proving that tenant notification fits a 6-hour DAKSH filing (CYB paras 28, 141, 146);
> - a data-residency check of every environment and sub-processor;
> - a production runbook;
> - a migration and cut-over plan;
> - a controlled go-live checklist for my approval.
>
> Do not deploy to production without my explicit authorisation."

### Phase 16 — Partner connectors, co-lending and DA

> **Instruction to Claude:** "Extend the Phase 8c connector into the full LSP/channel-partner framework (Part 5). Add:
>
> - the DLG ledger (≤ 5% of the amount disbursed out of the covered portfolio, invoked within 120 days overdue);
> - the collection-agent appointment model, kept separate from DLG;
> - the CIMS DLA register;
> - the co-lending engine (10% retention, 15-day booking, bank escrow, blended rate, next-working-day classification sync, each lender's own CIC reporting);
> - DA/securitisation pools;
> - partner portals."

### Phase 17 — Secured products expansion

> **Instruction to Claude:** "For each secured product (LAP/Home, Vehicle, Gold, LAS/LAMF):
>
> 1. produce the product spec and feasibility notes;
> 2. implement the collateral workflows (M5), integrations and regulatory checks;
> 3. build SARFAESI (with the NBFC eligibility gate), repossession and auction, including the gold auction rules in RBC paras 60–66."

### Phase 18 — Analytics, AI layer and MCP

> **Instruction to Claude:** "Build:
>
> - the MIS catalogue;
> - embedded BI with row-level security;
> - governed AI copilots (M20), with an AI model inventory;
> - the read-only, tenant-scoped MCP server."

### Phase 19 — Migration tooling

> **Instruction to Claude:** "Build the legacy loan-boarding toolkit, with history, opening balances, DPD reconstruction and reconciliation sign-off reports."

### Phase 20 — Scale hardening and AWS migration

> **Instruction to Claude:** "Run multi-tenant scale tests. Then:
>
> - write and rehearse the AWS ap-south-1 / ap-south-2 migration runbook;
> - run DR at scale;
> - do performance tuning;
> - repeat independent VAPT.
>
> Present a controlled migration plan for my approval."

---

# PART 13 — START NOW

I have connected my GitHub repository for Finbyx, and this file is committed at `docs/00-master-prompt.md`. Do **not** begin by implementing the complete lending system.

First, execute **Phase 0 only**:

1. Read this whole file, including the appendices.
2. Inspect the repository and report its current state: files, branch, tooling and constraints.
3. Audit the current Finbyx product.
4. Identify missing business decisions and the major architecture, regulatory, data-residency and financial-integrity risks.
5. Propose, as ADRs:
   - the repository structure;
   - the tenancy and authorisation strategy;
   - the Fineract adoption approach;
   - the technology choices, with current versions.
6. Prepare the initial entity model and the API/integration boundaries, including the outline of the Udofin contract.
7. Prepare regulatory register v1, as described in the Phase 0 instruction, item 7.
8. Prepare:
   - the phased roadmap, with dependencies and acceptance criteria;
   - the minimum security, testing and review gates;
   - the competitor benchmark.
9. Present the proposed baseline and your questions for my approval **before** modifying the repository.

After approval:

- Create the `feat/repo-baseline` branch.
- Commit only `CLAUDE.md` (from Appendix A), the ADRs, `docs/` and the registers. Application scaffolding belongs to Phase 1.
- Open a pull request.

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
- Data stays in India (prod data, backups, logs, SaaS sub-processors). Railway or any non-India host:
  synthetic data only.
- KFS validity is not a waiting period; COB never accrues income on an account turning NPA.
- Part 8A citations are verified against the official RBI texts in docs/regulations/rbi/; prefer them
  over any other citation.

## Commands
(pnpm install / dev / test / lint / typecheck / db:migrate / db:test — fill in Phase 1)

## Where things live
docs/00-master-prompt.md (full brief), docs/architecture, docs/adr, docs/specs, docs/products,
docs/data-model, docs/api, docs/integrations, docs/compliance, docs/security,
docs/testing (golden-cases), docs/ops, docs/legal, docs/economics, docs/status.

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
4. **Hosting and data:** the India-region host for any environment holding real data (Railway has no India region); AWS timeline; dedicated-deployment offer for banks; Aadhaar vault route (ADV-as-a-service vs OKYC/DigiLocker only).
5. **Commercial model:** per-loan, per-user, per-module or AUM-based pricing. This affects metering design.
6. **Vendor shortlist and contracts:** Surepass scope; membership of all four CICs (mandatory under CIR para 6); eSign/eStamp; sponsor bank for NACH; payout bank; WhatsApp BSP; SMS DLT entity (the lender's).
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
- **Added in v1.2 (Part 8A):** entity_regulatory_profile flags (layer, last-audited assets, deposit_taking, public_funds, customer_interface, notified_nbfc, ifc, nofhc_held, card_issuer, ind_as, cyber_chapter); branch_regulatory_event; related_party, related_party_link, counterparty_group, group_assessment, lei_record; investment_security, investment_holding, investment_valuation, interclass_transfer, aif_lookthrough; large_exposure_return; alm_bucket, alm_slotting_rule, behavioural_assumption, liquidity_run, lcr_daily, hqla_holding, cfp_source, stress_scenario; disclosure_template, disclosure_run; dlg_set, dla_register; cic_reference_calendar, cic_rejection, cic_dqi_review, cic_nodal_contact, cir_complaint_compensation, sarfaesi_display_entry; fraud_case, show_cause_notice, fraud_debarment, rbr_report; compliance_risk_assessment, product_approval, rmp_map_item, cco_register; aa_consent_artefact; green_allocation.

---

# APPENDIX E — REVISION LOG

## E.1 v1.0 → v1.1 (18 October 2026)

v1.1 corrects the errors found in an independent regulatory and technical review of v1.0. Claude Code must follow v1.1. The v1.0 statements listed below are withdrawn.

| # | Area | v1.0 statement (withdrawn) | v1.1 correction |
|---|---|---|---|
| 1 | Usage | Paste Parts 1–13; save the prompt after approval | Commit the whole file (including the appendices) as `docs/00-master-prompt.md` before Session 1. Phase 0 reads it from the repository |
| 2 | KFS | 3/1 working-day "consideration period before execution" | KFS **validity** period under RBC para 29(2): the lender is bound for ≥ 3 working days (≥ 1 if tenor < 7 days). It is not a waiting period |
| 3 | COB | Accruals before borrower-level NPA classification; interest recalculation after accruals | Two-pass COB with a cross-loan classification barrier. Income derecognition happens before accrual on accounts that turn NPA |
| 4 | Hosting | Railway "Mumbai region" | Railway has no India region: synthetic data only. Real data only on India-region hosts. All SaaS sub-processors must pass a residency check |
| 5 | Aadhaar vault | UIDAI Circular 8 of 2025 | UIDAI Circular No. 14 of 2025 (4 Nov 2025): on-premises, GCC or ADV-as-a-service only; FIPS 140-2 L3+ HSM |
| 6 | Recovery agents | "Recovery-agent amendment"; visits only after failed contact attempts; MFI window 09:00–18:00 shown as permanent | RBC Third Amendment Directions, 2026 (paras 100A–100AB, from 1 Jan 2027). Visit conditions per para 100Y(5). Call recording per para 100P. Effective-dated MFI window. Separate marketing window 09:00–19:00 (para 101N(4)) |
| 7 | Gold loans | Release and auction cited to Credit Facilities Ch IV; release cited to RBC 35–41 | LTV, caps and bullet loans: CF Ch IV. Release and auction: RBC Ch III.G (paras 58, 60–66) |
| 8 | Loans against securities | 50% LTV and Group 1 for all NBFC LAS (shares, bonds, MF) | Applies only to loans against shares by NBFCs with assets ≥ ₹100 crore (CF para 106), with conditions. Para 105 prohibits loans against own shares |
| 9 | CIC | Rework rejected data "within 7 days"; dates marked as unverified | Effective-dated: fortnightly with 7-day rejection rework until 30 Jun 2026; reference dates 9/16/23/month-end and rework by the next submission from 1 Jul 2026 (RBI/DOR/2025-26/117). ₹100/day after 30 days, with a 21-day lender leg |
| 10 | eSign | DP note listed as eSign-capable | DP notes (negotiable instruments) and powers of attorney go to the physical-execution path (IT Act First Schedule) |
| 11 | GST | Penal charges "CBIC circular Jan 2025 [VERIFY]"; e-invoicing unclear | No GST on penal charges: CBIC Circular 245/02/2025-GST, 28 Jan 2025. NBFCs are exempt from e-invoicing (Notification 13/2020-CT) |
| 12 | Fraud | "EWS/RFA" | NBFC Directions use EWS (UL/ML) and have no RFA. Applies to UL, ML and BL ≥ ₹500 crore. Show-cause ≥ 21 days. FMR within 14 days |
| 13 | CFSS | Not mentioned | Core Financial Services Solution mandate (Misc. Supervisory Directions 2026, Ch II) added as a product requirement |
| 14 | Revolving credit | Flagged for Product 12 only | The Aug 2026 draft affects Products 1, 3, 7 and 12. Build term-loan structures by default |
| 15 | Co-lending | "Interest split by hurdle rate"; escrow unspecified | Single blended (funding-share-weighted) rate. Escrow held with a bank |
| 16 | Prepayment | Para 34 only; layer rules unspecified | Paras 33–34, with rules for all NBFCs, the Upper Layer and the Middle Layer (₹50 lakh) |
| 17 | DLG | 5% "of covered portfolio"; paras unverified | ≤ 5% of the amount disbursed out of the portfolio (para 24). Invocation within 120 days (para 27). DLG term ≥ longest tenor |
| 18 | Fineract | Wrong strategy codes; `rbi-india-strategy` as universal default; all reschedule strategies on all engines; partially disbursed ≠ Active; technical write-off = Closed; "reset" delinquency action; schema-per-tenant | Codes corrected. RBI order also expressed as an advanced-allocation rule set. Engine constraints stated. Lifecycle corrected. Database-per-tenant. PostgreSQL 18 |
| 19 | Fineract oracle | Run in CI on every PR | Nightly or on-demand on a large runner. PR CI uses golden fixtures |
| 20 | Money precision | `NUMERIC(9,6)` rates; decimal.js defaults | Rates `NUMERIC(12,8)`; APR/EIR `NUMERIC(14,10)`; decimal.js precision ≥ 40 |
| 21 | RLS | RLS stated without enforcement details | Non-owner role, `FORCE ROW LEVEL SECURITY`, `SET LOCAL` context, zero-rows test |
| 22 | Roadmap | Pilot launch depended on all 20 phases; field app and communications had no phase; Udofin connector late; SARFAESI before secured products | Added Phases 3b, 8b, 8c and P (pilot go-live). SARFAESI, repossession and auction moved to Phase 17. Phases 17–20 split into separate instructions |
| 23 | Licences | AG Grid and Metabase embedding unqualified | AG Grid Community or TanStack by default; Superset for embedded MIS; open-source JDM editor (not the GoRules BRMS) |
| 24 | Coverage | No audit of the current Finbyx product; no competitor benchmark; grievance host switch missing; no SSO or app distribution | Added to Phase 0, M14, M19 and M22, with a concurrency target |
| 25 | Other | DPDP breach "Board within 72 hours"; Schedule III Div III only; Cyber VAPT/DR shown for all NBFCs; NSDL e-Gov naming | Intimation without delay, then the 72-hour report. Division I for non-Ind AS entities. Cyber obligations by chapter. Protean naming |

---

## E.2 v1.1 → v1.2 (18 October 2026): official RBI texts supplied by the project owner

v1.2 checks the prompt against the official text of 15 Directions: CF 347, CIR 349, CRM 350, CON 351, INV 354, BR 342, ALM 355, FS 359, CLM 364, AA 368, CMP 460, CYB 461, DPS 462, FRM 463 and AUD 468. Part 8A is new and holds the paragraph-level requirements. The corrections to earlier text are:

| # | Area | v1.1 statement (withdrawn) | v1.2 correction (source) |
|---|---|---|---|
| 1 | Cash recovery | Cash "must reach the lender's account the same day" | Must be reflected in full **in the borrower's loan account** on the same day, with no LSP fee deducted (CF 10(5)) |
| 2 | CIC default alerts | "Intimation **before** reporting default to CICs" | SMS/email alerts sent **while submitting** default/DPD data (CIR 34(1)(i)) |
| 3 | CIC timelines | Single regime | Effective-dated: fortnightly and 7-day rejection rework until 30 Jun 2026; 9/16/23/month-end and next-file rework from 1 Jul 2026 (CIR 10(2), 15). Sources link corrected to Id=13187 |
| 4 | Compliance function | "CCO certification"; CCO approval only for the payday template | No CCO certification is prescribed. Approval before launch applies to **every** new product and process for ML/UL, with 6-month monitoring (CMP 9(7), 15(2), 31). Applies to ML/UL only |
| 5 | Fraud | Summary only | Full lifecycle: three dates, natural justice, SCBMF, EWS (UL/ML), FMR per case, debarment, closure, legal audit, transfer gate, RBR (FRM 4–58). No RFA, no red-flag annex, no CIC reporting of fraud |
| 6 | DLG | Generic forms; "classification not affected" | Provider eligibility, precise forms, fixed DLG set, auditor-certified declaration, IRACP treatment, no set-off, no reinstatement, monthly LSP disclosure (CF 19–29) |
| 7 | Gold loans | Partial rules | Eligible collateral, prohibitions, valuation source and purity, slab basis, renewal/top-up, weight caps, para 47 money flows (CF 32–50) |
| 8 | Microfinance | "Unsecured" product | Every collateral-free loan to a household with income ≤ ₹3 lakh is microfinance, with a 50% household repayment cap and a block on new loans while above it (CF 51–62) |
| 9 | LAS | "Shares" | Listed shares only; Annex-III reporting; block on gold/silver ETF/MF collateral (CF 35(2), 106) |
| 10 | Products | No project finance or demand/call loans | Products 20 and 21 added; housing/CRE classification; PCE rules (CF 63–111) |
| 11 | Concentration | Generic limits [VERIFY] | Layer-wise limits, exposure computation, UL LEF with breach block and monthly return (CON) |
| 12 | Credit risk | Absent | Related-party lending (thresholds, routing, recusal), LEI gate, CDS, CERSAI types, own-debenture block (CRM) |
| 13 | CERSAI | "Within 30 days (s.23)" only | Four charge types filed on an ongoing basis (CRM 27–28); the 30-day period comes from SARFAESI/CERSAI Rules [VERIFY] |
| 14 | ALM | Generic | Buckets, tolerance limits, slotting rules, stock ratios, IRS, DNBS04A (quarterly) / 04B (monthly), daily LCR engine (ALM). "DNBS04A for BL ≥ ₹100 crore" withdrawn: the ₹100 crore test applies to every layer |
| 15 | Financial statements | Generic notes-to-accounts packs | FS disclosure engine (C.1/C.2/C.3), Impairment Reserve rules, Ind AS governance registers, LCR disclosure from daily values |
| 16 | Climate | Not covered | CLM is a green-deposit framework for NBFC-D and deposit-taking HFCs only |
| 17 | Investments; branches | Not covered | INV and BR requirements added (M10 item 7A; M1) |
| 18 | Cyber | Chapter thresholds partly right; repeal of the 2023 MD asserted | Ch III also covers all CICs; Ch V excludes CICs. Para 155 repeals via PPG.66 without naming the 2023 MD. Numeric RTO not prescribed. Vendor obligations (new Part 10.6), STP, regulator/auditor access, IPv6 |
| 19 | Digital payments | Not covered | DPS applies only to card-issuing NBFCs; adopted as the voluntary baseline for M7/M22/M23 |
| 20 | Account Aggregator | "TSP" list | Tenant is the FIU; AA and gateway recorded separately; FIP obligation for deposit-takers (AA 29); Finbyx is never an AA |
| 21 | Auditor's report | Not covered | Auditor evidence packs and DNBS10 support (AUD 6–11) |

---

## SOURCES CONSULTED FOR THIS PROMPT (for Claude Code to re-verify)

- **RBI:**
  - Press release on the 244 consolidated Master Directions (28 Nov 2025): https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=61705
  - Master Directions index: https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx
  - NBFC Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions, 2026: https://rbi.org.in/scripts/NotificationUser.aspx?Mode=0&Id=13592
  - NBFC Miscellaneous Supervisory Directions, 2026: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13586
  - RBC Second Amendment Directions, 2026: https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=13493
  - FREE-AI report: https://www.rbi.org.in/scripts/PublicationReportDetails.aspx?ID=1306
  - NBFC Credit Facilities Directions, 2025: https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12957
  - NBFC Responsible Business Conduct Directions, 2025: https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12942
  - NBFC Credit Information Reporting Amendment Directions (RBI/DOR/2025-26/117, 4 Dec 2025): https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=13187 (Id=13180 is the commercial-bank version)
  - Official texts of the 15 Directions in Part 8A, supplied by the project owner: docs/regulations/rbi/
  - NBFC Fraud Risk Management Directions, 2026: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13590
  - NBFC Supervisory Returns Directions, 2026: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13587
  - 31 Jul 2026 Supervision Directions press release: https://rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=63265
  - KYC amendment (29 Dec 2025): https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=13236
- **Other primary sources:**
  - UIDAI Circular No. 14 of 2025 (Aadhaar Data Vault): https://www.uidai.gov.in/images/Circular-No.14_of-2025.pdf
  - CBIC Circular 245/02/2025-GST (penal charges): verify on cbic-gst.gov.in
  - Railway deployment regions: https://docs.railway.com/reference/deployment-regions
- **Secondary reproductions and summaries** (verify against RBI):
  - TaxGuru texts of the NBFC Credit Facilities, Responsible Business Conduct, IRACP and Credit Information Reporting Directions, 2025; the Internal Ombudsman Directions 2026; RB-IOS 2026; the commercial-bank ECL Directions 2026.
  - CAalley list of the 64 Supervision Directions (31 Jul 2026).
  - CARE Ratings note on the Co-Lending Directions 2025.
  - TaxGuru text of the RBC Third Amendment Directions, 2026 (recovery agents, 6 Aug 2026): https://taxguru.in/?p=1066749
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
