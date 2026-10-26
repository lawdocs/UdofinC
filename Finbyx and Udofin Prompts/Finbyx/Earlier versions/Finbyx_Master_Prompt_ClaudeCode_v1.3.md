# FINBYX — Master Build Prompt for Claude Code

**Web-based Loan Origination (LOS), Loan Management (LMS), Accounting, Collections & Recovery, Risk and Compliance System for NBFCs, HFCs, Banks and other Regulated Lenders**

Version 1.3 · Revised 18 October 2026 (33 RBI Directions and 1 guidance note supplied by the project owner incorporated in Part 8A; revision log in Appendix E; drafting slips in Appendix F) · Derived from the Udofin mobile-app master prompt and rewritten for Finbyx

---

## HOW TO USE THIS PROMPT (for the project owner — do not paste this box)

1. **Before Session 1:** Commit this entire file to the Finbyx repository as `docs/00-master-prompt.md`. That means Parts 1–13, Appendices A–F and the Sources — everything below this box. Do not paste only Parts 1–13, because Phase 0 depends on the appendices.
2. **Session 1:** Open Claude Code on the repository and type: *"Read docs/00-master-prompt.md in full, then execute Part 13 (Phase 0 only)."* Claude Code will audit and propose, then stop for your approval.
3. **After approval:** Claude Code commits `CLAUDE.md` (Appendix A), which points every later session to the master prompt.
4. **Every later session:** Copy the matching phase instruction from Part 12 ("Instruction to Claude"), one phase or sub-module at a time. Approve each specification before code is written.
5. **Items marked [VERIFY]** are regulatory or vendor facts that need re-checking against the primary source before the related module is built. Claude Code is instructed to do this check and to record the result in the regulatory register.
6. **Data residency:** Railway has no India region. Use synthetic data only until India-region hosting is in place (Part 10.1).
7. **RBI source texts:** commit the official RBI Direction PDFs you supplied to `docs/regulations/rbi/` (Part 8A.0). Part 8A cites them paragraph by paragraph; Part 8A.36 lists the v1.3 build additions by module, return, product and phase.

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
| J | Risk | CRO office | Credit, concentration, liquidity/ALM and operational risk (RCSA, loss events, KRIs, critical operations and impact tolerances, dependency map); EWS; ICAAP inputs; model inventory; third-party register; CRO product vetting (GOV 23) |
| K | Compliance and Regulatory Reporting | CCO office, Principal Officer (PMLA), Grievance Redressal Officer, Internal Ombudsman | Regulatory register, controls testing, returns, CIC reporting, FIU-IND, grievance oversight |
| L | Internal Audit and Auditors (read-only) | Internal, concurrent and statutory auditors, RBI inspection support | Sampling, audit trails, evidence packs for the Auditor's Report Directions (PBC test, NOF, IRACP/CRAR lineage, DNBS10, exception-report register; Part 8A.15), fraud closure files; RBIA module with tenant-wide read-only access for the HIA and IA staff (IAF paras 32–40; Part 8A.32); statutory-auditor register, Form A/B and branch-coverage report (SA paras 13, 30; Part 8A.33) |
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

- a tenant cannot set NPA at more than 90 DPD (IRACP paras 44, 51, 56); HFCs and the NBFC-MFI microfinance portfolio follow their own Directions [VERIFY: HFC and MFI Directions not supplied];
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
  - Closed: obligations met / foreclosed / settled (OTS paid within 3 months; a longer or part settlement is restructuring until paid — RSA 89–90) / fully written-off with no further recovery pursued / restructured-closed / transferred (assignment/novation; a loan participation keeps the account open with the tenant as lender of record, TDCR para 12(5));
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

- Delinquency buckets and ranges, configurable, with defaults of SMA-0 (1–30), SMA-1 (31–60), SMA-2 (61–90) and NPA (>90) (RSA para 18; IRACP paras 44, 51, 56).
- Installment-level delinquency.
- Delinquency history.
- Pause and resume (Fineract 1.15.0), plus reset as a Finbyx addition — **only under maker-checker and a policy reason**, because pausing can be misused for evergreening.
- DPD = COB date − oldest unpaid due date + 1, so the due date's own day-end is DPD 1. Golden test (IRACP para 19, Illustration I): due 31 Mar → SMA-1 on 30 Apr, SMA-2 on 30 May, NPA on 29 Jun.
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
    6. Borrower-level SMA/NPA classification and upgrade check across all facilities of the borrower with the tenant, including all of the borrower's securities held as investments (NPA/NPI) (IRACP para 23). Upgrade only when all arrears on all facilities are paid (paras 24–25); restructured/DCCO accounts follow RSA (para 26). Co-lending sync per M11; IRACP requires no cross-group-entity classification
  - **Pass B (per loan, partitioned):**
    7. Income recognition: accrue for standard accounts; for NPA accounts derecognise and reverse unrealised interest, fees, penal and other charges, and keep memorandum interest only (IRACP para 38); interest capitalised under a moratorium permitted at sanction is not reversed (para 40)
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
- Post-dated cheques — migration/legacy only: no fresh or additional PDCs/EMI cheques alongside NACH; CTS-2010 cheques only where NACH is unavailable (MISC paras 22–23; para 23 not applicable to HFCs).
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
   - rounding of all customer transactions (instalments, interest charged, charges, receipts, refunds, deposit interest) to the nearest rupee: 50 paise and above rounded up, below 50 paise ignored; customer cheques containing paise are never rejected. Accruals stay at NUMERIC(20,4) internally and are rounded at billing/posting. Applies to all layers, HFCs and CICs (RBC para 103; MISC para 27).
4. **Ind AS 109 compliance:**
   - EIR computed by IRR (Newton-Raphson with bisection fallback) over contractual cash flows, including fees and directly attributable costs;
   - amortisation of deferred fee and cost at EIR;
   - Stage 1/2/3 ECL (PD × LGD × EAD, SICR at >30 DPD rebuttable, credit-impaired at >90 DPD);
   - interest on net carrying amount in Stage 3;
   - **parallel IRACP computation**, with the shortfall appropriated to an Impairment Reserve where Ind AS ECL is lower than the prudential floor (IRACP paras 34–36).
5. **Indian GST:**
   - exclusive GST added on top of fees, with a CGST/SGST/IGST split by place of supply;
   - **no GST on penal charges** (CBIC Circular No. 245/02/2025-GST dated 28 Jan 2025, para 2.5);
   - a configurable flag for bounce charges, which become GST-free only if the lender's Board policy treats them as penal charges [VERIFY];
   - GST on processing, foreclosure (where levied), bounce and documentation charges as configured;
   - interest is exempt.
6. **TDS receivable** on interest paid by corporate borrowers, with Form 26AS/AIS reconciliation.
7. **KFS/APR engine** compliant with para 29 and Annex I of the Responsible Business Conduct Directions, including the APR golden test in Part 8A.19 (₹20,000 / 24 months / 15% / ₹400 fees → APR 17.07%).
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
| LSP → Finbyx | `ApplicationSubmitted` | Application, KYC results with evidence references (evidence only: the KYC decision stays with the lender, KYC 13; OTP-e-KYC NFTF limits of KYC 25 apply), bureau/AA references, documents, consent artefacts |
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
- Asset classification and provisioning of the underlying loans follow the IRACP Directions (CF para 25(1)). ECL may reflect DLG cover only where it is integral to the loan contract and not recognised separately, and is recomputed after every invocation (IRACP paras 36A–36C).
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
| 8 | **Gold Loan** (and silver where offered) | Pledge | Assay capture (karat, gross/net weight), **Lending terms (CF Ch IV, paras 32–50).** Eligible collateral is only gold/silver jewellery, ornaments and coins. Primary gold/silver, bullion, gold/silver-backed financial assets, and loans to buy gold are blocked (para 35). An ownership declaration is required on every loan (para 36); no re-pledge (para 37). Valuation at actual purity: the lower of the 30-day average closing price and the previous day's close, from IBJA or a SEBI-regulated exchange, with nearest-purity adjustment and intrinsic metal value only (paras 40–42). Consumption-loan LTV is 85% / 80% / 75%, by **total consumption loan per borrower** (≤ ₹2.5 lakh / > ₹2.5–5 lakh / > ₹5 lakh); for bullet loans, both LTV and slab use the total repayable at maturity; LTV is maintained daily for the whole tenor (paras 43–44). A detailed credit assessment is required above ₹2.5 lakh (para 33). Consumption bullet loans are capped at 12 months (para 38). Renewal or top-up only on a formal request, within LTV, on a standard account; bullet renewals only after accrued interest is paid; renewals and top-ups flagged in the system (para 34). Weight caps per borrower: gold ornaments 1 kg, silver ornaments 10 kg, gold coins 50 g, silver coins 500 g (para 39). AML alert on multiple or frequent loans; multiple-loan internal-audit report (paras 36, 48). Disbursal and repayment rules of para 10 apply on every channel (para 47). **Release and auction (RBC Ch III.G, paras 43–75; para 42 deleted w.e.f. 1 Apr 2026):** assay certificate with image, borrower present at assay (paras 46, 50); release on the same day and in any case within 7 working days (para 58), with ₹5,000 per day of delay attributable to the lender (para 69); auction with notice, two newspapers, and a reserve price of ≥ 90% of current value, which may fall to 85% after two failed auctions (paras 60–66); first auction physical in the lending branch's district; no bidding by the lender or its related parties; surplus refunded within 7 working days of receipt of full proceeds (paras 64–66); collateral unclaimed 2 years after closure, with a half-yearly report to the Customer Service Committee or Board (paras 71–72) |
| 9 | **Education Loan** | Either | Disbursement to institution, moratorium during course plus grace, co-borrower |
| 10 | **Consumer Durable / Point-of-sale Loan** | Unsecured | Merchant/dealer onboarding, subvention (buy-down fee), zero-cost EMI accounting, merchant refund |
| 11 | **Microfinance (JLG/SHG and individual)** | Collateral-free (no deposit lien, no hypothecation) | Household = husband, wife and unmarried children, with annual income ≤ ₹3,00,000. **Every** collateral-free loan to such a household is a microfinance loan, whatever the product or channel (CF para 51). Board-policy income assessment over ≥ 1 year (para 52); household income reported to CICs (para 54). Repayment obligations of all household loans plus the proposed loan ≤ 50% of monthly household income, with no new loans while above it (paras 55–57). Flexible periodicity (para 59). Pricing policy with a ceiling on the rate and all charges (paras 60–61). centre meetings, weekly/fortnightly collections, effective-dated MFI recovery-contact window (09:00–18:00 under RBC para 91(2) until 31 Dec 2026; from 1 Jan 2027 per the RBC Third Amendment [VERIFY: amendment text not supplied; whether a separate MFI window survives]), no prepayment charge and delayed-payment charges only on the overdue amount (RBC para 81); loan card (paras 78–80); minimum/maximum/average rate display (para 82); collection at the designated place, residence or workplace only after two or more successive non-appearances (para 90). **NBFC-MFI tenants:** qualifying assets ≥ 60% monitor (MFI paras 8(3), 12); NPA > 90 days and provision floor on overdue instalments (paras 24–25); channelising-agent loans segregated and CIC-reported (para 13). **Non-MFI NBFCs:** microfinance loans ≤ 25% of total assets (MFI para 49) |
| 12 | **Supply-chain / Invoice / Channel Finance** | Either | Anchor programmes, invoice validation, TReDS. **Revolving-credit restriction on NBFCs under the August 2026 draft Credit Facilities amendment** [VERIFY final status before building any revolving line] |
| 13 | **Medical and Insurance Finance** | Either | Hospital/insurer institutional partnerships, direct payment to provider where permitted, pre-authorisation linkage, insurance-claim offset. **Feasibility pilot only** |
| 14 | **Legal Expense and Award-Enforcement Finance** | Either | Ordinary repayable loans only through the regulated lender. Non-recourse or litigation-funding cases are **referred out to specialist funders, not booked**. Requires a legal feasibility assessment first |
| 15 | **Resolution Finance** (linked to Equator settlements) | Either | Funds the borrower's settlement with an existing lender; disbursement direct to the creditor; settlement evidence from Equator; affordability test; measurement of qualification rates. Where the creditor being settled is the tenant itself, the loan is restructuring and is blocked as evergreening without a viability assessment (RSA 10(12), 169). The tenant's own settlement through Equator: payment over more than 3 months = restructuring (RSA 89); consent decree where proceedings are pending (RSA 100); cooling period of at least 12 months before fresh exposure (RSA 95). **Pilot** |
| 16 | **Debt Reset / Consolidation** | Either | Rigorous affordability and debt-closure model before refinancing stressed borrowers; direct payoff to existing lenders; refinancing the tenant's own account in financial difficulty is restructuring (additional credit to an account in default, or roll-over: RSA 10(12), 159(3)): downgrade to sub-standard (RSA 53, 189), and no upgrade merely by rescheduling (IRACP 22); refinancing without a cash-flow viability assessment is evergreening (RSA 169, 188; enforcement under RSA 22, 26); restructuring flags. **Pilot** |
| 17 | **Co-lending products** | Any | Each NBFC party retains ≥ 10% of each loan (TDCR 102), funding-share-weighted blended rate (108), bank escrow for all flows (117), partner share booked within 15 calendar days or the loan stays with the originator (113, 115), originator-only DLG ≤ 5% of CLA outstanding (123), next-working-day classification sync (124), borrower-level classification sync (Part 7, M11) |
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
- **Third-party and outsourcing register** (OUT 36, 64(2), 82; ORM 74(5)): every DSA/DMA, LSP, recovery agency, IT provider (including Finbyx itself and its sub-processors) and other vendor, with Ch III / Ch IV / CYB-117 classification, materiality score (OUT 14, 58(2)), due diligence (30, 71) and annual (38) or risk-based (80) re-review, para 34/74 clause checklist, ownership/conflict check (18(vi), 59), audits and certifications (37, 76–79), SLAs and KRIs (64(4), 75), supply chain (82), exit plan (84–86) and critical operations supported (ORM 69). Half-yearly Board/RMC review pack (OUT 12(1)(vii), 36). Termination-publicity workflow (44, 89). See Part 8A.29.

## M3. Customer (CIF), KYC and AML

- **Single Customer Information File** across products and entities, where permitted. Individual and non-individual customers, with relationships to co-borrowers, guarantors, directors, partners and beneficial owners.
- **Related-party register and connected-counterparty groups** (CRM paras 13A–13Q; CON para 4(3)), LEI records (CRM paras 18–24), and the fraud-debarment register with associated entities (FRM para 35). See Part 8A.3, 8A.4 and 8A.14.
- **De-duplication:** internal match on PAN, Aadhaar reference/token, mobile, name + DOB, address and bank account; fuzzy matching; negative and blacklist checks; wilful-defaulter (LWD) and large-defaulter check on the borrower, guarantors, directors (DIN) and persons in charge (PAN), with identical names resolved through independent sources, never a borrower declaration (WD para 19(1)). A borrower on the LWD, or an entity associated with a wilful defaulter, cannot be restructured (RSA 83, 85). The WD 7(3) bars and the FRM para 35 debarment are separate registers, checked separately. One **UCIC** per individual customer; CDD is done once at UCIC level (KYC 17(6), 66).
- **KYC per RBI (NBFC – Know Your Customer) Directions, 2025 (RBI/DOR/2025-26/361, updated as on 29 Dec 2025); full detail in Part 8A.21:**
  - CKYC search, download and upload. Upload within **10 days** of commencement (KYC 63(1)); furnish updated information within **7 days** and pull CKYCR-notified updates (63(7)); communicate the KYC Identifier (63(6)); flag OTP-e-KYC accounts (25(8)). Retrieve by KYC Identifier first and do not re-collect documents except in the 63(9)(i)–(iv) cases; under the 29 Dec 2025 Explanation, records relied on need no re-verification of identity/address, but all other CDD remains the tenant's. Download needs the customer's explicit consent (23(4)); the OTP mechanism is CERSAI's operational design [VERIFY: CKYCRR 2.0 specifications]. Build for CKYCRR 2.0 real-time APIs: search, download with OTP consent, upload.
  - Aadhaar offline e-KYC (XML/QR) and DigiLocker. Aadhaar e-KYC authentication (OTP/biometric, incl. Face Authentication) only where the lender is notified under the first proviso to s.11A(1) PML Act (KYC 23 proviso (i), Expl 2); offline verification for proof of possession (proviso (ii)); e-documents: digital-signature check plus live photo (proviso (iii)); physical OVDs: para 24 digital KYC (proviso (iv)); Aadhaar number redacted where authentication is not required (Expl 1); Aadhaar never mandatory (Expl 4).
  - V-CIP per KYC 26–27 (Part 8A.21): India-only IPs, liveness and face match, 3-working-day XML/QR and video windows, fresh session on call drop, reject on prompting, PAN image/e-PAN check, no printed e-documents, account live only after concurrent audit, data in India on tenant-owned/leased storage with the vendor retaining no data, CERT-In VAPT before go-live.
  - OVDs and deemed OVDs (KYC 5(1)(xiv)), with a 3-month clock for a current-address OVD; PAN/e-PAN or Form 60 mandatory (23(5)), verified with the issuing authority (17(10)); GSTIN verified where available (17(12)). PAN–Aadhaar link status is an Income-tax check, not a KYC requirement: tenant policy option.
  - Periodic updation at least every **2/8/10 years** (H/M/L) (KYC 42(1)); low-risk individuals: transactions continue, update within 1 year of due date or by 30 Jun 2026, whichever later (42(2)); **≥ 3 advance intimations and ≥ 3 post-due reminders, each with ≥ 1 letter, logged** (42(7)); acknowledgement and updation-date intimation (42(5)(iii)); address change: positive confirmation within 2 months (42(3)(ii)).
  - Risk categorisation (low, medium, high) with re-categorisation triggers, reviewed **at least every 6 months** (KYC 41(1)), never disclosed to the customer (20(4)); NFTF-onboarded customers high-risk until face-to-face/V-CIP verification (44(6)).
- **Aadhaar Data Vault: UIDAI Circular No. 14 of 2025 (4 Nov 2025), which supersedes Circular 8 of 2025.**
  - The vault may be hosted only on-premises, on a MeitY-empanelled Government Community Cloud, or through ADV-as-a-service.
  - It needs an HSM certified FIPS 140-2 Level 3 or higher, and non-reversible reference keys. Hashing the Aadhaar number is not permitted.
  - A commercial cloud region with CloudHSM may therefore not qualify. Record the hosting choice in an ADR.
  - If full Aadhaar numbers are ever stored, use a separate vault service with HSM-backed encryption and reference tokens.
  - Prefer OKYC/DigiLocker flows that avoid storing them.
  - Never log Aadhaar, PAN or OTP.
- **AML/CFT:**
  - daily screening against the UNSC 1267/1988 lists, 2007 Order Schedules and UNSCR 1718 (KYC 54(2), 56); UAPA Schedules 1 and 4 (57); WMD s.12A list at onboarding and periodically (55(3)); match → block, report to CNO/FIU-IND/MHA/RBI, implement freeze, forward unfreeze applications within 2 working days (54–55, Annexes I–II); PEP screening (foreign PEPs, family, close associates) with senior-management approval to open and to continue (45);
  - transaction monitoring rules;
  - alert management;
  - FIU-IND reporting of PML Rule 3 transactions per Rule 7, in FIU-IND formats (KYC 49–50): STR, CTR, NTR, CCR [VERIFY: timelines in PML Rules r.8; the KYC Directions do not state them]; each day of delay is a separate violation, and no account restriction merely because an STR is filed (51); alerts on transactions inconsistent with risk profile (53).
  - record retention under PMLA §12 and KYC 47: transactions ≥ 5 years from transaction date; identification records ≥ 5 years after relationship ends; DARPAN registration for NPO customers (48).

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
   - **KFS validity period (RBC para 29(2)):** the lender is bound by the KFS terms for at least 3 working days (tenor ≥ 7 days) or 1 working day (tenor < 7 days), and the borrower may accept at any time within it. This is **not** a waiting period, so do not block same-day execution. Store the unique proposal number (para 29(2)), the KFS issue time, validity expiry, acceptance time and the borrower's acknowledgement that the contents were explained (para 29(1)). Scope: all retail and MSME term loans; credit-card receivables exempt (para 29).
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
    - **Interest starts from the actual date of disbursement or cheque handover, never from sanction or agreement date** (RBI (NBFC – Miscellaneous) Supervisory Directions, 2026, para 7(1), (4), (5): no interest from sanction/agreement date, or from the cheque date where the cheque is handed over later; no full-month interest where disbursal or repayment is mid-month; no advance instalments with interest charged on the full amount. Applies to HFCs and MFIs too (para 3)).
    - EMI computed only on the amount actually disbursed, never on the sanctioned amount (MSD para 7(2)); on each part-disbursement, regenerate the amortisation schedule and send the revised schedule against the KFS to the borrower (para 7(3)); prefer online transfer to cheques (para 9).
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
  - Property documents: RBC paras 35–41, which apply to personal loans (para 6(11)); ₹5,000/day only where the delay is attributable to the lender, with reasons communicated otherwise (para 39); for lost or damaged documents the lender bears the cost of duplicates and the penalty runs after 60 days (para 40); borrower's choice of collection office (para 36); legal-heir procedure on the website (para 38). Apply the same SLA to other products by policy.
  - Gold/silver: same day, and in any case within 7 working days (RBC para 58); ₹5,000/day beyond that where attributable to the lender (para 69).

## M6. Loan Management / Servicing (LMS)

- **Loan account (360° view):** schedule, ledger, balances by component, DPD history, classification history, mandates, collateral, documents, communications, complaints, collections activity, legal cases.
- **Schedules:** all Part 4.2A options. Regenerate the schedule with a full audit trail and keep previous versions.
- **Accruals:** daily interest accrual; penal charges as **charges, never penal interest, never capitalised** (RBC para 30(1)): levied only on the amount under default and never on earlier penal charges (para 30(1) Notes (ii)–(iii)); interest on unpaid interest/EMI only at the contracted rate; individual non-business penal charges never above non-individual (para 30(5)); the applicable penal charge shown in every reminder and each levy communicated with its reason (para 30(7)).
- **Floating-rate resets:**
  - benchmark change propagation;
  - borrower option to raise the EMI, extend the tenor or both, and to prepay in part or full at any time (para 31(3)); switch to a fixed rate where the lender's Board policy offers it, with a cap on the number of switches (para 31(2)); switch charges in the sanction letter and on the website (para 31(4));
  - no negative amortisation;
  - quarterly statement with principal and interest recovered to date, EMI, EMIs left and annualised rate/APR for the full tenor (para 31(6)); any EMI/tenor increase communicated immediately (para 31(1)).
  - Basis: RBC paras 31–32: EMI-based floating-rate personal loans (XBRL definition, para 6(11)), extended to equated-instalment loans of any periodicity on external or internal benchmarks, but not to other loan types; benchmark-transmission monitoring for EBLR loans (para 32). Extend the same controls to other floating products by policy.
- **Repayments:**
  - all channels (M7);
  - allocation per the product's strategy;
  - excess and advance handling;
  - unapplied/suspense receipts with resolution workflow.
- **Part-prepayment and foreclosure:**
  - quote generation valid to a date;
  - choice between reducing EMI and reducing tenure;
  - **prepayment-charge engine**, per RBC paras 33–34 and 81 (the 2 Jul 2025 Pre-payment Charges Directions are a legacy reference):
    - Scope: RBC para 34 for loans sanctioned or renewed on or after 1 Jan 2026; para 33 for earlier loans (term loans only; para 34 covers term and demand loans).
    - All NBFCs: no charge on floating-rate loans to individuals for non-business purposes.
    - Upper Layer: no charge on floating-rate business loans to individuals and MSEs.
    - Middle Layer: the same where the sanctioned amount is up to ₹50 lakh.
    - No lock-in period, whatever the source of funds (para 34(3)).
    - Dual/special-rate loans: tested on the rate type on the prepayment date (para 34(4)).
    - Other cases per Board policy: term loans charged on the amount prepaid; CC/OD closure before the due date on no more than the sanctioned limit (para 34(5)); CC/OD free if non-renewal was intimated in time and the facility closes on the due date (para 34(6)).
    - No charge where the lender initiates the prepayment (para 34(7)); undisclosed charges cannot be levied (para 34(8)); no retrospective levy of charges waived earlier (para 34(9)).
    - Microfinance: no prepayment charge (para 81).
    - Inputs: sanction/renewal date, facility type (term/demand/CC/OD), rate type on the prepayment date, borrower type (individual/MSE/other), purpose, NBFC layer, sanctioned amount/limit, initiator (borrower/lender), microfinance flag, disclosure flags, waiver history.
    - Disclose any permitted charge in the KFS, sanction letter and agreement.
- **Restructuring and rescheduling:**
  - per the RBI (NBFC – Resolution of Stressed Assets) Directions, 2025;
  - restructuring flag;
  - asset-classification impact: standard → sub-standard on restructuring, NPA keeps its class (RSA 53–54, 189–190); no upgrade merely because of rescheduling (IRACP 22);
  - monitoring and specified periods: Part A until 10% / 20% of post-plan principal debt is repaid (RSA 10(8), 10(16)); Part B one year from the first payment on the longest-moratorium facility (RSA 159(5)); Part A/B resolver from the entity profile (RSA 7–8);
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
- **Write-off:** technical write-off (no waiver; recovery continues: RSA 10(18), 91) and full write-off; approver at least one level above the sanctioning authority, sanctioning official excluded (RSA 16(5)); partial technical write-off classified and provisioned on the original gross exposure (RSA 92); quarterly reporting to the next higher authority (RSA 93–94); post-write-off recovery ledger.
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
    - microfinance 09:00–18:00 (para 91(2)); para 100 does not apply to microfinance loans;
    - agent details to the borrower when recovery starts; agent carries the notice, authorisation letter and ID; borrower notified on a change of agency (paras 95–96); agency list on the website (para 97); antecedent and police verification of agents (para 94). Paras 93–97 sit in the microfinance section (H): apply them to all products by policy.
  - **From 1 Jan 2027:** the RBI (NBFC – Responsible Business Conduct) Third Amendment Directions, 2026 (6 Aug 2026; RBI/2026-27/230) delete paras 89–100 and insert Section J (paras 100A–100AB) [VERIFY: amendment text not supplied; the supplied RBC copy is updated only to 1 Apr 2026]. Under the new rules:
    - recovery contact only between 08:00 and 19:00 (para 100Y(4)) [VERIFY whether a separate MFI window survives];
    - **record every recovery call**: all outbound calls, and inbound calls to the number the NBFC provided. Inform the borrower, and keep recordings for 6 months, or until disposal if the matter is sub judice (para 100P);
    - every agent must hold the **IIBF debt-recovery-agent certificate**; existing agents have one year to obtain it (para 100I);
    - give the borrower the assigned agency's details at least 1 day before the first visit (para 100L);
    - visit the residence or workplace only where no meeting place was chosen, or where the borrower failed to appear at the chosen place on two or more successive occasions (para 100Y(5); para 100Y(7) for microfinance centre collection);
    - include grievance-officer details on recovery communications;
    - device-lock rules for financed devices (paras 100S–100U: DPD gates, prompt unlock, compensation for delayed unlock) [VERIFY figures].
  - **Sales/marketing contact window:** 09:00–19:00 under the RBC Second Amendment (para 101N(4)) [VERIFY: amendment text not supplied]. Keep it separate from the recovery window.
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
  - **Wilful defaulter and large defaulter identification and reporting:** RBI (NBFC – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 (Part 8A.20; ML and above; HFCs and CICs included): screen NPAs ≥ ₹25 lakh and complete classification within 6 months of the NPA date (para 6); Identification Committee, show-cause reply within 21 days, representation within 15 days, personal hearing without lawyers, reasoned order by the Review Committee (para 5); monthly Annex I (large defaulters ≥ ₹1 crore) and Annex II (LWD) files to all CICs, with removal within 30 days (paras 11–12); wilful-default check and LWD reporting before any transfer of a defaulted loan ≥ ₹25 lakh (para 14).
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
  - an approval matrix, with related-party recusal (CRM para 13J), with the approver at least one level above the sanctioning authority and the sanctioning official excluded (RSA 16(5)(i)). Settlements with fraud or wilful-defaulter borrowers are permitted but need Board approval in every case, without prejudice to criminal proceedings and penal measures (RSA 16(5)(ii), 97–98; WD 13(3)); restructuring of such borrowers is barred (RSA 83–85; WD 7(3)(iv)). A wilful defaulter stays on the LWD until the compromise amount is fully paid, even below ₹25 lakh, and a cancelled settlement is reported at the revised amount (WD 13(1)–(2), 13(4)). A settlement paid over more than 3 months, or a part settlement, is restructuring until paid (RSA 89–90); a consent decree is required where judicial recovery proceedings are pending (RSA 100); a cooling period of at least 12 months applies before fresh exposure (RSA 95); quarterly reporting goes to the next higher authority, and to the Board for MD & CEO / Board-committee approvals (RSA 93–94). Settling a fraud account starts the 5-year debarment clock (FRM para 35);
  - settlement letter;
  - payment plan tracking;
  - **CIC reporting of settlements:** "settled" only where principal or interest was waived for financial inability, reported with the reason and the settlement amount; wrong debits and contested charges are reported as "disputed" (CIR paras 12(2), 12(4)). IBC-admitted cases are reported as suit-filed (para 12(7));
  - **SARFAESI possessed-asset website feed:** assets possessed under s.13(4) on or after 25 Sep 2023, in the Annex IV columns; updated monthly; removed on sale or full settlement (CIR para 21);
  - no sale to other lenders or ARCs while a fraud investigation is open (FRM para 54); fraud accounts otherwise transferable under Board policy, and to ARCs only with reporting, monitoring and complaint responsibilities passed on (TDCR paras 28, 78).
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
   - parallel **IRACP** with income derecognition on NPA, standard-asset provisioning by layer, and sub-standard, doubtful and loss provisioning (IRACP paras 30–33, 37–40, 48, 55, 58–60; Part 8A.17);
   - Impairment Reserve, appropriated from profit after tax where the Ind AS 109 allowance is below IRACP. It is not regulatory capital and cannot be withdrawn without DoS permission (IRACP paras 34–35; FS para 12(2)). The appropriation counts toward the prudential floor but not for net NPA (IRACP para 36).
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

- **Co-lending:** Part B of the RBI (NBFC – Transfer and Distribution of Credit Risk) Directions, 2025 (TDCR paras 95–127; in force 1 Jan 2026 or an earlier date set by internal policy; CLAs entered into before that date stay under the earlier rules, paras 2, 95–96). Not applicable to multiple banking, consortium or syndication (para 99). Eligible partners: SCBs excluding SFBs/LABs/RRBs, AIFIs, NBFCs incl. HFCs (para 97). The engine must handle:
  - partner master and agreements;
  - minimum 10% of each individual loan retained by each NBFC party to the CLA (TDCR para 102); the partner's back-to-back commitment is irrevocable (para 112); separate borrower account per lender for its share (para 116);
  - both books reflect the shares within 15 calendar days of disbursement; otherwise the loan stays with the originator and may be sold only under TDCR Part A (paras 113, 115); transfer only to the partner named in the agreement and the KFS (para 114);
  - an escrow account with a bank (which may be one of the co-lenders) for all disbursements and repayments, between the lenders and with the borrower, with appropriation rules in the agreement (TDCR para 117), controlled only by the co-lenders (CF para 10, Note);
  - a single blended rate to the borrower: the funding-share-weighted average of each lender's rate, with any other fees reflected in the APR and KFS (TDCR paras 108–110); any partner rate change recomputes the blended rate and is communicated to the borrower (para 109); lending-service fees on objective criteria with no credit-enhancement or DLG element (para 111);
  - partner-level income splits per the agreement;
  - **borrower-level SMA/NPA sync across partners, near-real time and by the end of the next working day at the latest** (TDCR para 124);
  - each lender reports its own share to CICs (TDCR para 122);
  - DLG only by the originating NBFC, up to 5% of loans outstanding under the CLA, governed mutatis mutandis by CF paras 19–29 (TDCR para 123; DLG defined in para 111, Explanation (2)). The cap base is loans outstanding under the CLA, not CF para 24's amount disbursed; keep a separate CLA DLG ledger;
  - the list of active co-lending partners published on the website (TDCR para 126; FS para 21(4)); annual aggregate CLA notes to accounts (TDCR para 127);
  - co-lending disclosures in the KFS and the loan agreement: roles, single point of customer interface, change only after prior intimation (TDCR paras 105–106); unrealised CLA profit deducted from CET1/NOF (para 107); BCP on CLA termination (para 119); onward transfer only under Part A with mutual consent (para 125);
  - partner reconciliation and servicer reports.
- **Direct assignment, loan participation and stressed-loan sales** (TDCR Part A, paras 6–94) **and securitisation** (SEC, RBI/DOR/2025-26/353):
  - pool selection with eligibility filters: standard loans only; no synthetic or re-securitisation; no revolving, bullet (except the agri and trade-receivable proviso), residual maturity < 365 days, restructured-in-specified-period or lender exposures (SEC paras 5–6); no default or SMA for DA (TDCR paras 12(11), 33);
  - MHP checks (TDCR para 43; for securitised mortgages, from the later of full disbursement and CERSAI registration, SEC para 7); 10% DA retention where portfolio-level due diligence is used (TDCR para 40); securitisation MRR 5% (≤ 24 months, and RMBS) or 10% (> 24 months, and bullet loans), in the prescribed form, unhedged and maintained for life (SEC paras 10–14); originator retained exposure ≤ 20% (SEC para 23);
  - pool tagging;
  - sale accounting: cash only, with consideration received at transfer (TDCR para 38; SEC para 31); Ind AS NBFCs follow Ind AS 109 and ICAI advisories (TDCR para 72; SEC para 32); unrealised profit deducted from CET1/NOF (TDCR para 45), or for non-Ind AS securitisation held in "Unrealised Gain on Loan Transfer Transactions" (SEC para 34);
  - servicing of sold pools: collections held in trust, no commingling, remit only after collection (TDCR para 30; SEC para 95); CE, liquidity and underwriting facility conditions (SEC paras 80–94);
  - collection waterfalls;
  - investor and trustee reports incl. Annex I MHP/MRR disclosure at origination, half-yearly and on breach (SEC paras 112–113); 14-day risk-profile notice (SEC para 22); quarterly RBI report (SEC para 115); STC checker (SEC paras 35–79);
  - no buy-back: re-acquisition only under a resolution plan (TDCR para 17); replacement for breach of reps and warranties within 30 days for DA (TDCR para 52(4)) and 120 days for securitisation (SEC para 30(5)), each notified to RBI DoS (TDCR para 24; SEC para 30(7)); clean-up call as defined in SEC para 4(2) [VERIFY: conditions not in SEC; see Capital Adequacy Directions];
  - stressed-loan sales: Board NPA review (TDCR para 56), two external valuations ≥ ₹100 crore (57), Swiss challenge (60, 89–92), 12-month cooling (61), ARC transfer accounting and SR valuation (78–86); acquired stressed loans classified and provisioned per paras 69–71 and held ≥ 6 months (74);
  - loan-transfer trade reporting; database until the platform is notified (TDCR para 94).

## M12. Risk management

- **Credit risk:**
  - portfolio quality: vintage curves, roll rates, flow rates, PAR/DPD buckets;
  - **exposure engine and concentration limits** (CON Directions, Part 8A.4):
    - BL Board limits, plus unsecured consumer-credit sub-limits monitored by the RMC (paras 6–9);
    - ML single/group 25% / 40% of Tier 1, IFC 30% / 50%, plus 5% / 10% for infrastructure (paras 13–14);
    - exposure computation, CRT offsets and exemptions (paras 17, 20–23);
    - sensitive-sector limits (para 24);
    - group-of-connected-counterparties logic (para 4(3));
  - **UL only — Large Exposure Framework:** single 20% (25% hard cap; 30% for IFC), group 25% (IFC 35%; +10% infrastructure); immediate breach report to RBI and an automatic block on new exposure (paras 33–46); Return on Large Exposures (para 48; filed quarterly per SR para 21 item 12);
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
- **Capital** (CAP Directions, Part 8A.24): RWA engine — on-balance RW master (18(1)), CCF (18(4)), guarantee-scheme 0% up to the maximum permissible claim (18(2)(iv)), CEM (18(8)), SEC-ERBA (29–51), CDS (53); owned fund incl. quarterly EPt (9), CET1 and deductions (7–8), Tier 1 (10–11), Tier 2 with sub-debt discounting and 50% cap (13), DTA (14), AIF/co-lending/DLG deductions (15), Ind AS filters incl. Stage 1 ECL to Tier 2 and lifetime ECL netted from RWAs (16); minimums by profile — gold-primary Tier 1 12%/CRAR 15%, ML+ Tier 1 10%/CRAR 15%, UL CET1 9%, Tier 2 ≤ Tier 1 (6); BL leverage ≤ 7 (17). No CCB and no Pillar 1 operational/market-risk charge.
- **ICAAP data mart** (ML and above; CAP para 54 — Board-approved, proportionate; Pillar 2 capital not insisted upon): inputs for credit, concentration, operational, market/IRRBB, liquidity, reputational, strategic, ESG and cyber risk assessments; stress scenarios; RAG (traffic-light) indicators against the Risk Appetite Statement.
- **Operational risk:**
  - loss-event database;
  - RCSA (risk and control self-assessment);
  - KRIs (key risk indicators);
  - aligned with the RBI Guidance Note on Operational Risk Management and Operational Resilience (DOR.ORG.REC.301/14.10.001/2025-26, 28 Nov 2025; guidance, not a binding Direction; applies to NBFC-BL/ML/UL): taxonomy and control library, loss events with occurrence/discovery/accounting dates and near misses, Board-approved critical operations and impact tolerances, dependency mapping, scenario testing, third-party register and lessons-learned workflow (Part 8A.30).
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
| **CRILC and DNBS09 (weekly defaulted borrowers)** | **Filing catalogue (SR para 21 items 5–6):** UL and ML (except CICs); BL ICCs (except those with no public funds and no customer interface), BL MFIs, and BL Factors with assets ≥ ₹500 crore [VERIFY whether the ₹500 crore qualifier also covers ICCs and MFIs]. **Reporting obligation (RSA paras 7, 20–21, 158):** NBFC-D, NBFC-ND ≥ ₹500 crore and any NBFC-Factor. **Build:** applicability = union of the two tests, with a tenant toggle until verified. **CRILC:** monthly, borrowers with aggregate fund-based plus non-fund-based exposure ≥ ₹5 crore, including SMA status (RSA 20), within 15 days, NIL return if none (SR 21–22); project credit events weekly and in CRILC-Main (RSA 106). **DNBS09 / weekly default report:** as on close of business every Friday (or the preceding working day), due by Wednesday of the following week; move-in and move-out sections (PAN, name, date of default, funded, non-funded and total outstanding); NIL return if none (RSA 21; SR 21–22) |
| **RBI supervisory returns (online portals / CIMS)** | Data-driven catalogue per the RBI (NBFC – Supervisory Returns) Directions, 2026 (RBI/DoS/2026-27/466; HFCs excluded, they file NHB returns), para 21: DNBS01, DNBS02, DNBS03, DNBS04A, DNBS04B, CRILC, DNBS09, DNBS10, DNBS11/12 (CICs), DNBS13 (all NBFCs, NIL return), DNBS14 (P2P), Large Exposure Framework, PDR III/IV, Stress Test and IRS Test (SPDs), FMR, FUA, FMR4/RBR, Form A; full table with applicability in Part 8A.34. Due (para 22): weekly by Wednesday of the following week; monthly within 15 days; quarterly and yearly within 21 days; audited returns within 5 working days of signing of the auditor's report; exceptions in para 23. Online submission only; email only as an RBI-advised contingency, then resubmit online (para 18). Each return reconciled with accounting data, with recorded aggregation rules (paras 14–15). DNBS04A (quarterly) and DNBS04B (monthly): UL, ML (except SPDs) and BL ≥ ₹100 crore solely or at group level, excluding NBFCs with no public funds and no customer interface, NOFHCs, P2Ps, AAs and MGCs (para 21 item 4); Annex IV formats (ALM paras 57, 59). No XBRL requirement in the Directions; formats per return spec on the portal [VERIFY per return] |
| **Fraud Monitoring Returns (FMR)** | Per case, from the fraud module, irrespective of amount, immediately and not later than 14 days from classification; updates via FUA; group-entity frauds by email to fmgconbfc@rbi.org.in (FRM paras 42–45); FUA immediately; applicability UL, ML, BL ≥ ₹500 crore (SR para 21 items 17–19, para 23). HFCs report to NHB |
| **RBR (theft, burglary, dacoity, robbery)** | Incident report by email within 7 days; quarterly return (FMR4/RBR) within 15 days of quarter-end (FRM paras 57–58; SR para 23 item 5) |
| **Large Exposure Framework return (UL)** | Quarterly, within 21 days (SR para 21 item 12, para 22): 20 largest exposures, exposures ≥ 10% of Tier 1, other and exempted exposures; CON Annex I format (headed "Return for the Month"; para 48(4) says 10 largest). Periodicity and N configurable; default quarterly filing with monthly internal computation [VERIFY periodicity: SR para 21 vs CON Annex I]. Breach intimation immediately (CON para 45) |
| **CDS / CRT excess-exposure report** | Quarterly to the DoS Regional Office (CRM para 17(7)) |
| **IRF data** | Half-yearly, within 1 month (INV para 29) |
| **Pledged-shares report** | Quarterly to stock exchanges, Annex-III format (CF para 106) |
| **Public liquidity disclosure** | Quarterly on the website and in the notes (ALM para 15, Annex I; FS 21(13)) |
| **LCR disclosure** | Quarterly, from daily LCR values (FS C.2(32)) |
| **DNBS10 Statutory Auditor's Certificate** | Enable the auditor to file within 5 working days of signing, and by 31 December at the latest (AUD para 6; SR para 21 item 7, para 23). The auditor compiles and files on CIMS with login credentials the NBFC creates |
| **Branch-closure intimation (deposit-taking)** | To the RBI/NHB Regional Office within 7 days of the notice (BR para 12) |
| **FIU-IND** | STR, CTR, CCR, NTR in FIU-IND formats/utilities (KYC 49–53) [VERIFY: timelines in PML Rules r.8]; UAPA/WMD match reports immediately and unfreeze forwarding within 2 working days (KYC 54–55); Designated Director and Principal Officer details to FIU-IND and RBI (14–15) |
| **DLA/LSP reporting on CIMS** | Annex-I format, one line per DLA per platform; updated on addition or cessation; CCO or Board-designated certification of the four para 18(4) points (CF para 18). No "RBI-approved" wording in DLA marketing (para 18(6)) |
| **NHB returns** (HFCs) | As applicable |
| **Co-lending, loan-transfer and securitisation disclosures and reports** | Website CLA partner list (TDCR 126; FS 21(4)); annual CLA notes (TDCR 127); FS 21(5) STC/non-STC and 21(6) loan-transfer disclosures (TDCR 93; SEC 114); Annex I MHP/MRR disclosure per transaction at origination, half-yearly (Sep/Mar) and on breach (SEC 112–113); quarterly securitisation report to RBI, format awaited (SEC 115); loan-transfer trade reporting, database until platform notified (TDCR 94); DoS notice of rep/warranty replacements or damages (TDCR 24; SEC 30(7)); material risk-profile change to investors and CRAs within 14 calendar days (SEC 22) |
| **Board and committee packs** | Audit, Risk, NRC, ALCO, IT Strategy and Customer Service committees; half-yearly material-outsourcing review (OUT 12(1)(vii), 36); ACB outsourced-audit and vendor-reconciliation ageing (OUT 12(2)); risk-management and governance reviews (GOV 15); operational-risk appetite, critical operations, impact tolerances and post-incident reports (ORM 31–32, 55, 102) |
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
  - CKYC uploads within 10 days and updates within 7 days (KYC 63(1), 63(7));
  - CIC files on time;
  - NPA tagging correct;
  - interest from disbursement date, EMI on disbursed amount only, schedule revision communicated on each tranche, no full-month interest for part months, advance instalments reduce the interest base (MSD para 7(1)–(5)).
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
  - sales feedback within 30 days of sale under the RBC Second Amendment (para 101Y, effective 1 Jan 2027) [VERIFY: amendment text not supplied].

## M16. Document management system (DMS)

- Private, encrypted object storage with short-lived signed URLs.
- Document types and metadata; versions; hashes (SHA-256) for integrity; verification status; uploader; timestamps.
- Retention schedule by document class:
  - PMLA/KYC: identification records 5 years after relationship end; transaction records 5 years from transaction (KYC 47);
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
- **Consent, preference and DND management**, honouring the **RBI (NBFC – Responsible Business Conduct) Second Amendment Directions, 2026** (15 Jun 2026; Chapter IIIA on sales and marketing; effective 1 Jan 2027) [VERIFY: amendment text not supplied]:
  - explicit consent with "No" as the default (para 101I);
  - ban on the listed dark patterns (para 101X, Annex III);
  - no compulsory bundling (para 101V);
  - marketing contact only 09:00–19:00 (para 101N(4));
  - consent records retained;
  - under the current text: DoT/TRAI-registered telemarketers only, with the list and registered numbers furnished to TRAI (RBC para 101); DSA/DMA training on soliciting, calling hours and privacy, and code-of-conduct undertakings (RBC paras 98–99).

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
| Scale-based regulation | RBI (NBFC – Registration, Exemptions and Framework for Scale Based Regulation) Directions, 2025 (RBI/DOR/2025-26/339; original 28 Nov 2025 text). Any 2026 amendment (reported ₹1 lakh crore UL threshold; "Unregistered Type I NBFC") is not in the supplied copy [VERIFY: 2026 amendment] | Entity profile drives applicability of every rule: layers (10–16); group consolidation and auditor certificate (17–20); ML from the date of crossing ₹1,000 crore (22–23); UL by RBI advice, 3/24-month transition, 5-year floor (24–30); PBC 50/50 (38); NOF ₹10 crore / ₹2 crore / ₹300 crore and glide path to 31 Mar 2027 (39–43); NOF deductions and AIF look-through (45–46); FATF < 20% (47); exemptions (49–67) |
| Digital lending | RBI (NBFC – Credit Facilities) Directions, 2025 (RBI/DOR/2025-26/347), Chapter III (paras 6–30; DLG paras 19–29) | Direct disbursal and repayment (para 10); KFS; Board-set cooling-off of at least 1 day (para 11); DLA/LSP lists; consent; India-only storage; DLG ≤ 5% of amount disbursed out of the covered portfolio (para 24), invoked within 120 days overdue (para 27) |
| Gold and silver loans | Credit Facilities Directions, Ch IV (paras 32–50; para 31 deleted w.e.f. 1 Apr 2026: eligibility, valuation, LTV, caps, bullet loans, disclosure); RBC Ch III.G (paras 43–75; para 42 deleted w.e.f. 1 Apr 2026: assay 44–51, custody 52–57, release 58–59, auction 60–66, compensation 67–70, unclaimed 71–72) | LTV slabs, quantity caps, valuation, assay certificate, auction, release, ₹5,000/day release compensation, unclaimed register |
| Loans against securities | Credit Facilities Directions, Chapter VIII (paras 104–106, Annex-III) | Loans against listed shares by NBFCs ≥ ₹100 crore: 50% LTV, 7-working-day cure, Group 1 where applicable, quarterly pledge reporting; no loans against own shares; IPO cap ₹1 crore |
| Interest, FPC, KFS, penal charges, prepayment, resets, document release, gold/silver and microfinance conduct, recovery agents | RBI (NBFC – Responsible Business Conduct) Directions, 2025 (RBI/DOR/2025-26/362; updated as on 1 Apr 2026): FPC 10–21, 26–28; interest 22–24; KFS 29 + Annex I; penal charges 30; resets 31–32; prepayment 33–34, 81; document release 35–41; gold/silver 43–75; microfinance 76–92; recovery agents, DSA/DMA and telemarketers 93–101; branch closure 102; rounding 103. RBC Second Amendment Directions, 2026 (15 Jun 2026; Chapter IIIA sales and marketing; effective 1 Jan 2027) and Third Amendment Directions, 2026 (6 Aug 2026; Section J, paras 100A–100AB; effective 1 Jan 2027) [VERIFY: amendment texts not supplied] | Vernacular templates; prospective-only rate and charge changes; KFS/APR engine with proposal number and validity period; penal-charge rules; prepayment-charge engine; reset options and quarterly statement; release SLA and ₹5,000/day compensation (documents and gold); assay certificate, auction and unclaimed register; MFI loan card; contact-policy guard-rails; agent register; nearest-rupee rounding |
| Interest computation; CFSS; nomination; PCA | RBI (NBFC – Miscellaneous) Supervisory Directions, 2026 (RBI/DoS/2026-27/467; 31 Jul 2026) | Interest only from actual disbursement or cheque handover; EMI only on the disbursed amount; revised schedule communicated on each part-disbursement; no full-month interest for part months; advance instalments reduce the interest base (para 7(1)–(5); also HFCs and MFIs, para 3). **CFSS:** mandatory for UL/ML with ≥ 10 fixed point service delivery units (including units manned by outsourced agents); digital customer interface, integrated functions, centralised database and accounting, regulatory MIS; quarterly progress report to the SSM (paras 5–6). Nomination coverage for NBFC-D deposits, quarterly DAKSH report (10–14). **PCA** monitor for NBFC-D and ML/UL/TL NBFC-ND: CRAR/Tier 1/NNPA (CIC: ANW/RWA, leverage, NNPA) risk thresholds and mandatory restrictions (16–19) |
| IRACP | RBI (NBFC – Income Recognition, Asset Classification and Provisioning) Directions, 2025 (RBI/DOR/2025-26/356; updated 13 Feb 2026) — Part 8A.17 | Agreement SMA/NPA examples (15); day-end tagging (18–19); borrower-wise NPA/NPI (23); upgrade (22, 24–26); NPA at 90 days (43–44, 51); sub-standard/doubtful ageing 18/12 months (45–46, 52–53); project-finance rates (30); NPA provisions (32); HP/lease (33); Ind AS floor and Impairment Reserve (34–36); DLG in ECL (36A–36C); income (38–40); standard rates BL/ML/UL (48, 55, 58–60) |
| Stressed assets | RBI (NBFC – Resolution of Stressed Assets) Directions, 2025 (RBI/DOR/2025-26/357) — Part 8A.18; Part A ≥ ₹500 crore or deposit-taking, Part B < ₹500 crore; HFCs paras 86–138 only | Financial-difficulty indicators (13–15); SMA bands (18–19); CRILC monthly and weekly (20–21); accelerated provisioning (22–23); review period and ICA (27–33); ICE (36–41); delayed-resolution provisions ≥ ₹1,500 crore (47–51); restructuring classification, upgrade, income (53–81, 189–195); fraud/WD restructuring bar (83–85); settlements and technical write-offs (16, 86–100); DCCO (111–119); DRS (123–137); FITL/Sundry Liabilities (152–153, 223–227); Part B viability, promoter contribution, 120 days, fair-value diminution (168–211) |
| Board credit policy | CF Ch II para 5 | Policy registry linking every product to the approved credit-policy version |
| Microfinance; project finance; demand/call; CRE; PCE | CF Ch V (51–62), Ch VI (63–79), paras 107–111, Ch VII (80–103) | Products 11, 20, 21; housing/CRE classification; PCE limits for ML+ |
| NBFC-MFI prudential | RBI (NBFC – Microfinance Institution) Directions, 2025 (RBI/DOR/2025-26/371; 28 Nov 2025) | Qualifying assets ≥ 60% of total assets net of intangibles; 4 consecutive quarters below → remediation plan to RBI (8(3), 12); channelising-agent loans a separate segment excluded from the test, separate books, CIC reporting (13); CRAR ≥ 15%, Tier 2 ≤ Tier 1 (16–17); NPA > 90 days; provision floor = higher of 1% of portfolio or 50%/100% of instalments overdue 90–180 / ≥ 180 days (24–25); geographic exposure limits (10); SRO membership (46); **non-MFI NBFCs: microfinance loans ≤ 25% of total assets (49)** |
| Internal audit | RBI (NBFC – Internal Audit Function) Directions, 2026 (RBI/DoS/2026-27/464); NBFC-D, HFC-D, and NBFC-ND/HFC-ND ≥ ₹5,000 crore | RBIA module: audit universe with maximum exclusion period (14); annual risk assessment (inherent × control, level and trend, 10 parameters) (25–31); magnitude × frequency plan (32); assignments and reports (33–35); observation tracking and Board/ACB reporting of pending high/medium paras (36–37); IT Committee routing of system-audit findings (34); no outsourcing (39); HIA access, tenure, quarterly ACB meeting, no business targets (40–43) |
| Statutory audit | RBI (NBFC – Statutory Audit) Directions, 2026 (RBI/DoS/2026-27/465); all NBFCs incl. HFCs (NBFC-ND < ₹1,000 crore may keep extant procedure) | Auditor register: joint audit ≥ ₹15,000 crore (11); eligibility tables (14–16); independence and 1-year non-audit gap (17–20); 3-year term, 6-year cooling-off, 8-NBFC cap (23–26); Form A within 1 month, Form B (30); early-removal intimation within 1 month (23); lapse report within 2 months (8); top-20 / 15%-of-advances branch-coverage report (13) |
| Credit risk | RBI (NBFC – Credit Risk Management) Directions, 2025 (RBI/DOR/2025-26/350; amended 5 Jan 2026, effective 1 Apr 2026) | Related-party register, threshold-based sanction and recusal (13A–13Q); own-share/own-debenture blocks (14–15); Notified-NBFC appraisal (6–8); CDS (16–17); LEI gate (19–24); CERSAI (25–28) |
| Concentration risk | RBI (NBFC – Concentration Risk Management) Directions, 2025 (RBI/DOR/2025-26/351; amended 1 Jan and 10 Mar 2026) | BL limits, consumer sub-limits, vehicle top-ups as unsecured, IPO cap (6–11); ML 25/40 and IFC 30/50 of Tier 1, exemptions, CRT, SSE (13–24); UL LEF, LE return (quarterly per SR para 21), breach block (25–49) |
| Investments | RBI (NBFC – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 (RBI/DOR/2025-26/354) | Classification per accounting standard; non-Ind AS valuation and transfer rules; AIF look-through; trade reporting (7–34) |
| Branches | RBI (NBFC – Branch Authorisation) Directions, 2025 (RBI/DOR/2025-26/342; amended 15 Apr 2026) | Deposit-taking state gate (6); no overseas branch (10); 3-month closure notice (11); 7-day intimation (12); representative office via PRAVAAH (13–15) |
| KYC/AML | RBI (NBFC – Know Your Customer) Directions, 2025 (RBI/DOR/2025-26/361; updated as on 29 Dec 2025); PMLA 2002 and PML Rules 2005 (reporting timelines, r.8 [VERIFY]); UAPA s.51A Order (Annex I); WMD s.12A Order (Annex II) | KYC policy and annual ML/TF assessment (6, 10); PO ≠ DD (14–15); CAP, UCIC, rejection reasons (17–18); risk categories, confidential, 6-monthly review (20, 41); CDD modes and s.11A Aadhaar (23); digital KYC app (24); OTP-e-KYC limits (25); V-CIP (26–27); proprietorship/LE/BO (30–38); updation 2/8/10 years and notices (42); PAN cessation (43); NFTF EDD, PEP (44–45); records 5 years (47); DARPAN (48); FIU-IND (49–53); sanctions (54–60); CKYCR 10/7 days and reliance (63); FATCA/CRS (64); new-tech assessment (68); wire transfer (69); third-party products (71); KYE/training (72) |
| Credit information | RBI (NBFC – Credit Information Reporting) Directions, 2025 (RBI/DOR/2025-26/349), as amended by RBI/DOR/2025-26/117 (4 Dec 2025; effective 1 Jul 2026: paras 10(2), 12(10), 15, Annex VI) | Membership of all 4 CICs (6); UCRF Annex I (9); effective-dated reference dates (10(2)); settled/disputed (12(4)); IBC = suit-filed (12(7)); CKYC (12(10)); rejections (15); DQI (17); correction at source (18–19); CIRs in credit policy (20); SARFAESI website display (21); alerts while reporting (34(1)); CIC nodal officer (34(2)); RCA (34(4)); compensation (35); no auto-rejection of new-to-credit (38(5)) |
| Loan transfers and co-lending | RBI (NBFC – Transfer and Distribution of Credit Risk) Directions, 2025 (RBI/DOR/2025-26/352): Part A loan transfers (paras 6–94); Part B co-lending (paras 95–127, effective 1 Jan 2026) | Permitted transferors/transferees (12(4), 12(8)); no CE/liquidity facility (16); no re-acquisition (17); cash, arm's length (38); one-third loan-level DD or 10% retention (40); MHP 3/6 months (43); unrealised profit off CET1/NOF (45); reps replacement within 30 days (52); stressed: 2 valuations ≥ ₹100 crore (57), Swiss challenge ≥ ₹100 crore (60, 89–92), 12-month cooling (61), classification and NPV provisioning with 3% premium floor (69–71), 6-month hold (74); ARC and SR valuation (78–86); trade-reporting database (94). CLA: 10% retention (102), blended rate (108), 15-day booking (113), bank escrow (117), own-share CIC reporting (122), originator DLG ≤ 5% (123), next-working-day classification sync (124), website partner list (126) |
| Securitisation | RBI (NBFC – Securitisation Transactions) Directions, 2025 (RBI/DOR/2025-26/353) | Prohibited structures and assets incl. synthetic (5); standard loans only (6); MHP (7–8); MRR 5%/10%, RMBS 5%, form and ongoing (10–14); 14-day risk-change notice (22); 20% retained cap (23); ₹1 crore ticket, listing if ≥ 50 investors (26–27); SPE conditions (28–29); reps replacement within 120 days, DoS notice (30); ≤ 30-day issuance gap (31); non-Ind AS unrealised-gain account (34); STC (35–79); CE/reset/liquidity/underwriting/servicing (80–96); investor DD and stress tests (97–107); Annex I MHP/MRR disclosure half-yearly (112–113); quarterly RBI report (115) |
| Outsourcing | RBI (NBFC – Managing Risks in Outsourcing) Directions, 2025 (RBI/DOR/2025-26/363); existing IT agreements compliant by renewal or 10 Apr 2026 (para 2); BL excludes Ch IV | Non-outsourceable functions incl. sanction, KYC decisions, internal audit and compliance (15); ownership bar (18(vi), 59); materiality (14, 58(2)); due diligence (30, 71); clauses (34, 74, 87–88); half-yearly Board/RMC review of the central record (12, 36); IT inventory with supply chain (64(2), 82); breach notice to RBI (28, 69); 6-hour incident clock from provider detection (61); multi-tenant isolation (70); group (45–51, 90–92); offshore (52–53, 93–94); SOC (95); cloud, incl. NBFC-controlled keys, MFA, SOC log integration and exit (97); termination publicity (44, 89); MFI accountability declaration (56) |
| ALM | RBI (NBFC – Asset Liability Management) Directions, 2025 (RBI/DoR/2025-26/355) | Ch II for assets ≥ ₹100 crore; buckets (32, 49); tolerance limits (39–40); stock ratios (43); IRS (45–53); behavioural assumptions (54–55); DNBS04A/04B (57–59); LCR (Ch III, 60–78); public disclosure (15, Annex I) |
| Capital | RBI (NBFC – Prudential Norms on Capital Adequacy) Directions, 2025 (RBI/DOR/2025-26/345; updated 1 Apr 2026; Amendments of 1 Jan and 10 Mar 2026) | M12 RWA/CRAR engine: minimums (6); owned fund with quarterly EPt (9); CET1/Tier 1/Tier 2 and deductions (7–15); Ind AS filters and ECL (16); BL leverage ≤ 7 (17); RW and CCF tables, guarantee schemes, CEM (18); securitisation SEC-ERBA (19–51); CDS (52–53); ICAAP ML+ (54) |
| Dividends | RBI (NBFC – Prudential Norms on Declaration of Dividends) Directions, 2025 (RBI/DOR/2025-26/360) | Eligibility checker: 3-year capital compliance and NNPA < 6% (8); payout ≤ 50% (CIC/SPD 60%; none for no-public-funds entities) after exceptional-profit adjustment (9); 10% fallback with NNPA < 4% (11); Annex I report within a fortnight (13–15) |
| Miscellaneous (DoR) | RBI (NBFC – Miscellaneous) Directions, 2025 (RBI/DOR/2025-26/373; updated 26 Feb 2026); distinct from the DoS Miscellaneous Supervisory Directions, 2026 | 1-month intimations (6–7); NCD private placement (9–13); no partnership/LLP/AOP (16–19); 15-day rating-change report (20); FDs outside PBC (21); no fresh PDCs/EMI cheques (23); ss.269SS/269T (24); rupee rounding (27); locker disclosure (28); AD-II (32–34); factoring (35–54); IDF-NBFC (55–63) |
| Green deposits | RBI (NBFC – Climate Finance and Management of Climate Change Risks) Directions, 2025 (RBI/DOR/2025-26/364); NBFC-D and deposit-taking HFCs only | Deposits module (later): green-deposit flag, taxonomy tags, HQLA parking, allocation ledger, verification and impact reports, Board review within 3 months (paras 6–18) |
| Wilful and large defaulters | RBI (NBFC – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 (RBI/DOR/2025-26/358); ML and above incl. HFC and CIC; the bar on further finance and the large-defaulter provisions apply to all REs (para 2) | NPA screening ≥ ₹25 lakh and 6-month deadline (6); two committees, show-cause reply 21 days, representation 15 days, personal hearing, reasoned order (5); 1-year/5-year bars and board covenant (7); guarantors (10, 17); monthly Annex I (≥ ₹1 crore) and Annex II files to all CICs, removal within 30 days, DIN (11–12, 18); compromise settlements (13); pre-transfer gate (14); IBC/resolution removal (15); DIN/PAN appraisal check and end-use monitoring (19); auditor and third-party reporting to IBA (20–21) |
| Financial statements | RBI (NBFC – Financial Statements: Presentation and Disclosures) Directions, 2025 (RBI/DOR/2025-26/359; updated 1 Apr 2026) | Ind AS governance registers (12(1)); Impairment Reserve (12(2)); Annex I Schedule (20); C.1 21(1)–(15) incl. (9A); C.2 for ML/UL incl. LCR disclosure; C.3 for UL; consolidation (Ch IV) |
| HFC | RBI (Housing Finance Companies) Directions, 2025, plus NHB requirements | HFC product rules and returns |
| Account Aggregator | RBI (NBFC – Account Aggregator) Directions, 2025 (RBI/DoR/2025-26/368; governs NBFC-AAs); ReBIT specifications as updated (para 33) | Tenant is the FIU: consent artefact (17), revocation (20), auditable logs (21), use only per artefact (28), FIP obligation for deposit-takers (29) |
| Cyber and IT | **RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 (31 Jul 2026; RBI/DoS/2026-27/461)**, which repeal the existing NBFC IT Framework and IT Governance instructions listed in circular DoS.CO.PPG.66/11.01.005/2026-27 (para 155; the 2023 MD is not named [VERIFY]) | Ch II all; Ch III for BL < ₹500 crore and all CICs; Ch IV for BL ≥ ₹500 crore; Ch V for TL/UL/ML excluding CICs. Audit trails (21(8); 109–111; vendor admin logs 62(2)(i)); MFA for privileged users and critical activities (115); STP without manual edits (119); RBI read-only MIS access and audit-mode access (46, 57); for Ch V entities, VA 6-monthly and PT annually for critical systems (para 121) and half-yearly DR drills (para 129); incident reporting within 6 hours (paras 28/141); source code or escrow (para 105) and vendor no-vulnerability certificate (para 106); ITSC every 6 months (Ch IV) or quarterly (Ch V) |
| Digital payment security | RBI (NBFC – Digital Payment Security Controls) Directions, 2026 (RBI/DoS/2026-27/462); **credit-card-issuing NBFCs only** | MFA with a dynamic factor (41); alerts on all debits and credits and on detail/limit changes (46); lockout (50–51); fraud rules (52–53); reconciliation within 24 hours (57); secure-usage guidance (58); in-app fraud flag (66); web and mobile controls (67–68); card data (69); VA/PT and escrow (31–32). Voluntary baseline for all other tenants |
| Fraud | RBI (NBFC – Fraud Risk Management) Directions, 2026 (31 Jul 2026; RBI/DoS/2026-27/463) | Applies to UL, ML, and BL ≥ ₹500 crore; three dates (4); show-cause ≥ 21 days and reasoned order (6); SCBMF/CoE (8); EWS for UL/ML (13–23); debarment (35); law enforcement (40); FMR within 14 days (43); closure (50–52); legal audit ≥ ₹1 crore (53); transfer gate (54); RBR (57–58) |
| Supervisory returns | RBI (NBFC – Supervisory Returns) Directions, 2026 (31 Jul 2026; RBI/DoS/2026-27/466; HFCs excluded) | Data-quality and aggregation governance, reconciliation to GL, recorded aggregation rules, DQ escalation, ad-hoc subsets (6–17); online-only filing with portal maker-checker (18–19); 20-item return catalogue (21; Part 8A.34); timelines and exceptions (22–23); new returns by notice (25) |
| Compliance function | RBI (NBFC – Compliance Function) Directions, 2026 (RBI/DoS/2026-27/460); **ML/UL only** | Annual compliance risk assessment and review (6–7); product/process approval (9(7), 31); 6-month monitoring (15(2)); compliance testing (15(3)); RMP/MAP tracker (15(4)); CCO tenure, SoD and SSM intimation (21–29); workflow tool with deviation approvals and unified dashboard (32). No CCO certification is prescribed here |
| Governance | RBI (NBFC – Governance) Directions, 2025 (RBI/DOR/2025-26/344) | Bank/NBFC-experienced director (8); RMC (9); >30% director change approval via PRAVAAH (10–11); F&P policy, Annex II declarations, 31 March declaration, Annex III deed (12–13); quarterly change-of-directors statement + MD/CEO certificate within 15 days, March auditor-certified (14); ACB/NRC (17–18); CRO for assets > ₹5,000 crore with product vetting and sanction-committee rules (19–24); KMP and independent-director directorship limits (26–27); whistle-blower (38); CG guidelines on website (40); UL independent-director exit report and listing (42–43) |
| Operational risk | RBI Guidance Note on Operational Risk Management and Operational Resilience (DOR.ORG.REC.301/14.10.001/2025-26, 28 Nov 2025; guidance, not a Direction) | Three lines (12); ORMF taxonomy and control library (24); RCSA, loss-event dataset with three dates, KRIs, scenario analysis (42); Board-approved critical-operations criteria and impact tolerances, annually (31–33); dependency mapping (69–72); third-party register (74); BCP/RTO/RPO (78–82); incident severity and communication (85); lessons learned to the Board (101–102); disclosure policy (97) |
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

The project owner supplied the official RBI PDFs for the 33 Directions and 1 guidance note listed in 8A.0.2 (15 in v1.2, 18 Directions and the ORM guidance note in v1.3). Each was read in full, and the paragraph citations in this Part come from that text. Sections 8A.1–8A.16 date from v1.2; 8A.17–8A.36 were added in v1.3.

### 8A.0.1 Rules for Claude Code

1. **Store the source texts.** Save the supplied PDFs in the repository under `docs/regulations/rbi/` (file name = RBI number, e.g. `RBI-DOR-2025-26-347.pdf`). Record a SHA-256 hash and the "updated as on" date of each in `docs/regulations/index.md`.
2. **Give every requirement an ID.** Load each requirement below into the regulatory register (M14) with the ID format `REQ-<code>-<para>`, for example `REQ-CF-10(1)`, `REQ-CIR-35(2)` or `REQ-CYB-121`.
   - Codes: CF, CIR, CRM, CON, INV, BR, ALM, FS, CLM, AA, CMP, CYB, DPS, FRM, AUD (v1.2); IRACP, RSA, RBC, WD, KYC, TDCR, SEC, CAP, SBR, DIV, MISC, GOV, OUT, ORM, MFI, IAF, SA, SR, MSD (v1.3).
   - ORM is a guidance note, not a Direction. Its IDs (`REQ-ORM-<para>`) carry the register strength flag "guidance" and are never reported as statutory breaches.
   - MISC (DOR Miscellaneous Directions 373) and MSD (DoS Miscellaneous Supervisory Directions 467) are separate instruments; keep them apart.
   - Every rule pack, control test and golden test must reference these IDs.
3. **Status of [VERIFY] items.**
   - These paragraphs are **verified** for the copies supplied.
   - Remove any [VERIFY] elsewhere in this prompt that a citation here resolves.
   - **Do not** treat amendments issued after a copy's "updated as on" date as verified; check them separately.
4. **More Directions will follow.** Still to be supplied: the HFC Directions; the Internal Ombudsman Directions and RB-IOS 2026; the repeal circular DoS.CO.PPG.66/11.01.005/2026-27; the RBC Second and Third Amendment Directions, 2026; a later SBR copy (the supplied 339 copy does not contain the ₹1 lakh crore UL threshold or the "Type I NBFC" category). Add each one to this Part in the same format.
5. **Drafting slips.** Where the official text contains a drafting slip, implement the evident intent, document the slip in `docs/regulations/errata.md`, and never "fix" it silently in code. Appendix F lists every slip found so far; seed `errata.md` from it. Examples:
   - CF definition 4(1)(xix) refers to "Chapter IV" for LSPs; digital lending is Chapter III.
   - CF definitions (xxiii) and (xxiv) refer to "Chapter VII" for project finance; it is Chapter VI.
   - The FS Directions restart numbering after para 21.
   - The CIR Annex I state catalogue is misaligned.

### 8A.0.2 Directions and guidance covered

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
| IRACP | Income Recognition, Asset Classification and Provisioning, 2025 | RBI/DOR/2025-26/356; DOR.STR.REC.No.275/21.04.048/2025-26 | 28 Nov 2025, updated as on 13 Feb 2026 (paras 36A–36C inserted) | NBFC-D, ICC, Factor, IFC, IDF (para 3); HFC, MFI, MGC, CIC subject to their own Directions, which prevail (paras 4–7); not P2P, AA, SPD, NOFHC or the two no-public-funds categories (para 10) |
| RSA | Resolution of Stressed Assets, 2025 | RBI/DOR/2025-26/357; DOR.STR.REC.276/21.04.048/2025-26 | 28 Nov 2025 (original; no "updated as on" date) | NBFC-D, ICC, Factor, MFI, IFC, IDF (para 3). Part A: NBFC-D and ND ≥ ₹500 crore; Part B: ND < ₹500 crore (paras 7–8, 157–158). HFC paras 86–138 only; MGC 86–100; not CIC, P2P, AA, SPD, NOFHC or the no-public-funds categories (paras 4–6) |
| RBC | Responsible Business Conduct, 2025 | RBI/DOR/2025-26/362; DOR.MCS.REC.No.281/01-01-039/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 (para 42 and Annex II deleted w.e.f. 1 Apr 2026). Second Amendment (15 Jun 2026, Ch IIIA) and Third Amendment (6 Aug 2026, paras 100A–100AB) not in the supplied copy [VERIFY] | NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, all layers; P2P paras 98–100 only; not MGC, CIC, AA, SPD, NOFHC or NBFCs without customer interface (paras 3–5) |
| WD | Treatment of Wilful Defaulters and Large Defaulters, 2025 | RBI/DOR/2025-26/358; DOR.FIN.REC.No.277/20-16-003/2025-26 | 28 Nov 2025 (original text; immediate effect) | **ML and above:** NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, CIC; not MGC, P2P, AA, SPD, NOFHC, or NBFCs without public funds and customer interface. The bar on further finance and the large-defaulter provisions apply to all REs (para 2) |
| KYC | Know Your Customer, 2025 | RBI/DOR/2025-26/361; DOR.AML.REC.No.280/14.01.003/2025-26 | 28 Nov 2025, updated as on 29 Dec 2025 (Explanation to para 63(9), CKYCR reliance, inserted w.e.f. 29 Dec 2025) | All NBFC categories and layers; not NBFCs without customer interface (para 3); overseas branches and subsidiaries (para 4). Aadhaar e-KYC authentication only for NBFCs notified under PML Act s.11A |
| TDCR | Transfer and Distribution of Credit Risk, 2025 | RBI/DOR/2025-26/352; DOR.STR.REC.271/21.04.048/2025-26 | 28 Nov 2025 (original text; no "updated as on" date) | NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, all layers. Not MGC, P2P, AA, CIC, SPD, NOFHC or non-public-fund NBFCs (para 3). Part B (co-lending) from 1 Jan 2026 or an earlier date set by internal policy (paras 2, 95) |
| SEC | Securitisation Transactions, 2025 | RBI/DOR/2025-26/353; DOR.STR.REC.272/21.04.177/2025-26 | 28 Nov 2025 (original text; no "updated as on" date) | As TDCR (para 3). NBFCs as originators, investors and facility providers |
| CAP | Prudential Norms on Capital Adequacy, 2025 | RBI/DOR/2025-26/345; DOR.CAP.REC.264/21-01-002/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 (Amendments of 1 Jan 2026, effective 1 Apr 2026, and 10 Mar 2026) | NBFC-D, ICC, Factor, IFC, IDF, MFI by layer; HFC, MGC, CIC and SPD for listed paras only; not P2P, AA, NOFHC or no-public-funds NBFCs (para 3) |
| SBR | Registration, Exemptions and Framework for Scale Based Regulation, 2025 | RBI/DOR/2025-26/339; DOR.FIN.REC.No.258/03.10.119/2025-26 | 28 Nov 2025 (original text; no "updated as on" date; any 2026 amendment not in the copy) | All registered NBFCs incl. Government companies; Ch IV exemptions for specified non-banking institutions |
| DIV | Prudential Norms on Declaration of Dividends, 2025 | RBI/DOR/2025-26/360; DOR.ACC.REC.279/21.02.067/2025-26 | 28 Nov 2025 | All layers incl. HFC, MGC, SPD, CIC, P2P, AA; not NOFHC |
| MISC | Miscellaneous, 2025 | RBI/DOR/2025-26/373; DOR.FIN.REC.No.292/03-10-119/2025-26 | 28 Nov 2025, updated as on 26 Feb 2026 | Ch II all layers; Ch III ML+; Ch IV Factors; Ch V IDF; HFC, MGC, SPD, P2P, AA and CIC per para 3(1); not NOFHC |
| GOV | Governance, 2025 | RBI/DOR/2025-26/344; DOR.GOV.REC.No.263/18-10-013/2025-26 | 28 Nov 2025 (original text; no "updated as on" date) | BL Ch III; ML Ch II–IV; UL Ch II–V, incl. HFC; CIC/MGC/SPD/AA/P2P partial (para 3); not NOFHC; paras 29–37 not for government-owned NBFCs |
| OUT | Managing Risks in Outsourcing, 2025 | RBI/DOR/2025-26/363; DOR.ORG.REC.No.282/21-04-158/2025-26 | 28 Nov 2025 (original text; no "updated as on" date); existing IT agreements compliant by renewal or 10 Apr 2026 (para 2) | NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, SPD, CIC, P2P, AA; BL excludes Ch IV and the IT parts of Ch II; MGC (ML+) Ch IV; not NOFHC |
| ORM | Guidance Note on Operational Risk Management and Operational Resilience, 2025 (**guidance, not a Direction**) | RBI/2025-26/[number blank in supplied copy]; DOR.ORG.REC.301/14.10.001/2025-26 | 28 Nov 2025 | Banks (incl. SFB, PB, LAB), RRBs, UCBs, RCBs, AIFIs (incl. NHB), NBFC-BL/ML/UL (para 8); HFCs by implication (9(14)(iii)); BL = "smaller RE" (12(2)) |
| MFI | Microfinance Institution, 2025 | RBI/DOR/2025-26/371; DOR.FIN.REC.290/03-10-038/2025-26 | 28 Nov 2025 (original text; no "updated as on" date) | Every NBFC-MFI (non-deposit-taking; ≥ 60% qualifying assets) (paras 3, 8(3)); para 49 (25% cap on microfinance loans) binds all NBFCs |
| IAF | Internal Audit Function, 2026 | RBI/DoS/2026-27/464; DoS.CO.PPG.58/11.01.005/2026-27 | 31 Jul 2026, immediate effect | All NBFC-D and HFC-D; NBFC-ND and HFC-ND with assets ≥ ₹5,000 crore (para 3) |
| SA | Statutory Audit, 2026 | RBI/DoS/2026-27/465; DoS.CO.ARG.59/08.91.001/2026-27 | 31 Jul 2026, immediate effect | All NBFCs incl. HFCs for SCA/SA appointment; NBFC-ND < ₹1,000 crore may continue extant procedure (para 3) |
| SR | Supervisory Returns, 2026 | RBI/DoS/2026-27/466; DoS.CO.DSG.60/33.01.001/2026-27 | 31 Jul 2026, immediate effect | All NBFCs, all layers, **HFCs excluded** (para 3); return-wise applicability in para 21 |
| MSD | Miscellaneous Supervisory, 2026 | RBI/DoS/2026-27/467; DoS.CO.PPG.61/11.01.005/2026-27 | 31 Jul 2026, immediate effect | NBFCs and HFCs (para 3); Ch II UL/ML with ≥ 10 fixed point service delivery units; Ch III incl. HFCs and MFIs; Ch IV NBFC-D excl. HFCs; Ch V NBFC-D and ML/UL/TL NBFC-ND excl. no-public-funds NBFCs, PDs, HFCs |

The DoS Directions of 31 Jul 2026 (CMP, CYB, DPS, FRM; IAF para 44, SA para 31, SR para 27, MSD para 22) repeal earlier instructions through circular DoS.CO.PPG.66/11.01.005/2026-27. The repeal list in that circular is not in the supplied texts [VERIFY].

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
  - Asset classification and provisioning follow the IRACP Directions (para 25(1), substituted 13 Feb 2026). ECL may reflect DLG cover only where integral to the loan contract; recompute after every invocation (IRACP paras 36A–36C).
  - Invoked DLG is not set off against individual loans (para 25(2)).
  - Recoveries may be shared (para 25(3)).
  - Invoked DLG is **never reinstated**, including through recovery (para 25(4)).
- An NBFC that provides DLG deducts it from capital (para 26(2)).
- Invoke within a maximum of 120 days overdue, unless dues are made good (para 27(1)). The DLG agreement runs at least as long as the longest loan tenor (para 27(2)).
- The LSP publishes portfolio counts and amounts monthly, within 7 working days of month-end, and the NBFC ensures it does (para 28).
- Not DLG: CGTMSE, CRGFTLIH, NCGTC; BIS, IMF and MDB guarantees (para 29).
- DLG is not synthetic securitisation (para 30(2)). Synthetic securitisation is prohibited (SEC paras 4(25), 5(3)).

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
- **Not settled by this copy:** the revolving-credit restriction (August 2026 draft amendment) is not in the 1 Apr 2026 text, so its [VERIFY] stays. Para 62(2) cites a "Management of Third-Party Dependencies" Directions, 2025; no Direction of that name exists. The applicable text is the "Managing Risks in Outsourcing" Directions, 2025 (OUT para 1), cited correctly in para 6(6); its para 56 holds the microfinance outsourced-staff accountability declaration. Record the slip in errata.md.

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
- **"Return on Large Exposures"** (Annex I, sections A–D) (para 48); filed **quarterly** within 21 days per SR para 21 item 12 (20 largest exposures) [VERIFY against the Annex I "Return for the Month" heading]. Annex I has 20 rows in section A while para 48 says 10; build for at least 20.
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
- Para 58 cites the "Filing of Supervisory Returns" Directions, 2024; apply the RBI (NBFC – Supervisory Returns) Directions, 2026 (paras 21–22): DNBS04A within 21 days of quarter-end, DNBS04B within 15 days of month-end; applicability per SR para 21 item 4 (UL; ML except SPDs; BL ≥ ₹100 crore solely or at group level, with exclusions). The repeal list in circular DoS.CO.PPG.66 is not supplied (SR para 27).

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
  - For ML/UL tenants, the OUT Ch IV regime applies instead (Part 8A.29).

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

**Not prescribed in CYB:** numeric RTO, log-retention period, data localisation, MFA in Ch III/IV, or DAKSH reporting for Ch III. (OUT 74(vi) requires an India-storage clause "as applicable"; OUT 97(viii)(d) requires MFA for cloud applications of ML+ tenants; OUT 61 sets a 6-hour clock from detection by the service provider.) Finbyx's controls exceed these minimums by design.

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

The module specifications in Part 7 must include the items below and the v1.3 items in 8A.36.1. Where a module text and Part 8A differ, **Part 8A prevails** for these Directions.

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
| M11 | Co-lending escrow controlled only by the co-lenders (CF 10 note) and held with a bank for all flows (TDCR 117). Website list of active co-lending partners (TDCR 126; FS 21(4)). **CLA engine:** NBFC share ≥ 10% (TDCR 102), 15-day booking clock with fall-back to originator (113, 115), dual borrower accounts (116), blended rate (108–109), next-working-day classification sync (124), originator-only DLG ≤ 5% of CLA outstanding (123). **Loan-transfer engine:** MHP calculator (TDCR 43–44), default/SMA gate (33), one-third DD test and 10% retention (40), 30-day replacement (52), no re-acquisition (17, 87), stressed-loan sale with valuation and Swiss challenge (57, 60, 89–92), trade-reporting database (94). **Securitisation engine:** eligibility (SEC 5–8), MRR (10–14), 20% cap (23), ₹1 crore ticket (26), SPE checks (28), 30-day issuance gap (31), CE reset calculator (84–87), STC checker (35–79), Annex I generator (112–113) |
| M12 | Exposure engine and limits for BL, ML and UL, LEF and breach block (CON). ALM and daily LCR engine (ALM). EWS and fraud lifecycle (FRM). CDS register (CRM 16–17) |
| M13 | New or corrected returns: DNBS04A/04B (ALM 57); Large Exposure return, quarterly (SR 21 item 12; CON 48); LE breach intimation (CON 45); CDS excess report, quarterly (CRM 17(7)); IRF data, half-yearly (INV 29); per-case FMR and FUA (FRM 43); RBR within 7 days and quarterly (FRM 57–58); DNBS10 SAC support (AUD 6); CIMS DLA Annex-I (CF 18); LAS Annex-III pledge report (CF 106); public liquidity disclosure, quarterly (ALM 15; FS 21(13)); LCR disclosure from daily values (FS C.2(32)); branch-closure intimation (BR 12) |
| M14 | **Compliance Function workflow suite** (CMP 6–33): annual compliance risk assessment and Board review generator, product/process approval gate, 6-month new-product monitoring, compliance testing, RMP/MAP tracker, CCO governance register and SSM intimations, deviation approvals, unified dashboard. **Applicability engine** driven by the entity profile |
| M15 | **Credit-information complaint workflow** with 21/30-day clocks, ₹100/day compensation, apportionment and 5-day payout (CIR 34–35). Digital-lending grievance escalation text (CF 12) |
| M17 | Board/committee packs: annual compliance review (CMP 7), compliance testing (CMP 15(3)), SCBMF fraud review (FRM 8), EWS effectiveness (FRM 14, 21), DQI and RCA reviews (CIR 17, 34(4)), ALCO pack (ALM), LE return (CON) |
| M19 / M21 / M22 / M23 | **Read-only "RBI Supervisor" and "Auditor (audit-mode)" roles** (CYB 46, 57). MFA for privileged and critical actions (CYB 115). Delegated authority for parameter changes such as interest rates (CYB 21(3)). STP with no manual edits of inter-system files (CYB 119). **DLA permission and biometric limits** (CF 13–14). DPS controls for payments, mobile and web (DPS 41–68) |
| Workspace L | **Auditor evidence packs** (AUD 6–8): PBC test and NOF computation, Board resolution on deposits, IRACP/investment/concentration compliance, CRAR with DNBS03 lineage, MFI qualifying-asset test (≥ 60% of total assets net of intangibles; 4-quarter breach rule; MFI paras 8(3), 12), exception-report register (AUD 11), fraud closure files (FRM 52) |


---

## 8A.17 IRACP — Income Recognition, Asset Classification and Provisioning Directions (356)

**Applicability (paras 3–10).** NBFC-D, ICC, Factor, IFC, IDF. HFC, NBFC-MFI, MGC and CIC apply it subject to their own Directions, which prevail on conflict (paras 4–7). Not P2P, AA, SPD, NOFHC, NBFCs with no public funds and no customer interface, or BL with customer interface but no public funds (para 10). Ind AS/ICAI prevail on inconsistency (para 8). Restructured accounts also follow RSA (para 9; Part 8A.18). Supplied text updated as on 13 Feb 2026; later amendments are not verified.

**Loan agreement and borrower education (paras 15–17):**

- Loans sanctioned on or after 31 Dec 2021: the agreement states exact due dates, repayment frequency, principal/interest break-up, **worked examples of SMA/NPA dates**, and for moratorium loans the exact repayment start date (paras 15(1), 15(3)).
- The borrower is told at sanction and at every later change to sanction terms until full repayment (para 15(2)). Older loans: at renewal or review (para 16).
- Website literature explaining overdue, SMA, NPA and upgrade with reference to the day-end process; branch posters optional; front-line staff explain at sanction, disbursal and renewal (para 17).
- *Build:* the agreement/KFS generator computes the illustrative SMA-0/1/2 and NPA dates from the actual first due date and regenerates them on any change to terms.

**Day-end tagging (paras 11(2), 18–19):**

- "Overdue" = not paid on the due date fixed by the NBFC (para 11(2)).
- Flag overdue in the day-end process for the due date, **irrespective of the time the process runs** (para 18).
- SMA/NPA classification runs in the day-end process; **the classification date is the calendar date for which day-end is run** (para 19).
- **Illustration I (golden test):** due 31 Mar, unpaid → overdue 31 Mar; SMA-1 on 30 Apr; SMA-2 on 30 May; NPA on 29 Jun. The due date is overdue day 1: **DPD = COB date − oldest unpaid due date + 1**.
- SMA bands are in RSA para 18 (Part 8A.18).

**Asset classes and NPA (paras 11(1), 20–27, 42–46, 50–53, 56):**

- Four classes: standard, sub-standard, doubtful, loss (para 21). Loss asset definition (para 11(1)).
- **NPA threshold:**
  - ML and UL: **> 90 days** (paras 51, 56).
  - BL: 180 days with glide path > 150 days by 31 Mar 2024, > 120 days by 31 Mar 2025, **> 90 days by 31 Mar 2026** (paras 43–44).
  - *Build:* > 90 days for every layer now; keep the effective-dated BL rule pack for back-dated replay.
- **Triggers:** overdue interest; term-loan instalment; demand/call loan from date of demand; bills; other current-asset receivables; dues from sale of assets or services or reimbursements; lease rentals and HP instalments (paras 43(1)–(7), 51(1)–(7)). Lease/HP accounts are classified on their record of recovery (provisos).
- **Borrower-wise, not facility-wise:** all facilities **and all securities of the borrower held as investments** become NPA/NPI (paras 23, 43(8), 51(8)).
- **Sub-standard:** NPA for ≤ **18 months (BL)** / ≤ **12 months (ML/UL)**; or terms renegotiated, rescheduled or restructured after commencement of operations, until one year of satisfactory performance (paras 45, 52).
- **Doubtful:** sub-standard for more than 18 / 12 months (paras 46, 53).
- **Upgrade:**
  - **only when all arrears of interest and principal on all facilities are paid** (paras 24–25);
  - never merely because of rescheduling (para 22);
  - restructured and DCCO accounts follow RSA (para 26).
- Transferred loans follow the TDCR Directions (para 27).
- The NBFC-MFI microfinance portfolio is outside paras 21–27, 29 and 32 (paras 20, 29, 32); use the MFI Directions [VERIFY: not supplied].

**Provisioning (paras 28–36C, 47–49, 54–55, 57–60):**

- Standard-asset provision is not netted; it is shown as **"Contingent Provisions against Standard Assets"** (para 28) and is not reckoned for net NPA (paras 48, 55).
- **Standard assets:** BL **0.25%** (para 48); ML **0.40%**, including microfinance loans (para 55); UL by category (para 58):

  | UL category | Rate |
  |---|---|
  | Individual housing; loans to small and micro enterprises | 0.25% |
  | Teaser-rate housing | **2.00%**, falling to 0.40% one year after the rate resets (if standard) |
  | CRE-RH | 0.75% |
  | CRE | 1.00% |
  | Restructured | Per RSA |
  | All other, including medium enterprises | 0.40% |

  MSE definitions per FIDD circular of 2 Jul 2020 (para 12).
- **UL derivatives:** current credit exposure (gross positive MTM per counterparty, no netting) attracts the counterparty's standard-asset rate (paras 59–60).
- **Project finance general provision (para 30(1)),** on funded outstanding, portfolio basis:

  | Phase | CRE | CRE-RH | Others |
  |---|---|---|---|
  | Construction | 1.25% | 1.00% | 1.00% |
  | Operational (after repayment starts) | 1.00% | 0.75% | 0.40% |

  - Not for projects with financial closure achieved by 1 Oct 2025 (old norms), unless a fresh credit event or material change occurs after that date (paras 30(3)–(4)).
  - Standard DCCO-deferred accounts also carry the RSA para 118 provision (para 30(2)).
  - [Interpretation, record in the interpretation log: the para 30 rate replaces the layer rate for project-finance exposures.]
- **NPA (para 32):**
  - sub-standard **10%** of total outstanding;
  - doubtful **100% of the portion not covered by realisable security**, plus on the secured portion **20% (doubtful ≤ 1 year) / 30% (1–3 years) / 50% (> 3 years)**;
  - loss: write off, or **100%** if retained.
- **Securitisation liquidity facility** drawn and outstanding > 90 days: **100%** (para 31).
- **HP and leases (para 33):**
  - total dues less unmatured finance charges and notional depreciated value (20% p.a. straight-line on original cost; actual cost for second-hand) (paras 33(1)–(2));
  - additional provision on NBV by months overdue: ≤ 12 nil; 12–24 **10%**; 24–36 **40%**; 36–48 **70%**; > 48 **100%** (para 33(3));
  - full NBV 12 months after the last instalment's due date (para 33(4));
  - deposit and security set-off rules (paras 33(5)–(7));
  - provision required even where income is not recognised (para 33(8));
  - financial leases written from 1 Apr 2001 treated as HP (para 33(9));
  - BL: renegotiated HP/lease stays sub-standard or its prior class until upgraded (para 49).
- **Ind AS (paras 34–36):**
  - Hold the Ind AS 109 allowance and, in parallel, IRACP classification and provisions (standard, restructured, NPA ageing) as the **prudential floor** (para 34).
  - Shortfall appropriated from net profit after tax to an **Impairment Reserve**; not regulatory capital; **no withdrawal without DoS approval** (para 35).
  - The appropriation counts toward the floor but **not for net NPA** (para 36).
- **DLG (paras 36A–36C, from 13 Feb 2026):**
  - DLG under CF Ch III / TDCR Part B may be reflected in ECL across all stages, only where integral to the loan's contractual terms and not recognised separately (para 36A).
  - Ind AS 1 disclosures (para 36B).
  - **Recompute ECL after every invocation** for the reduced cover (para 36C).

**Income recognition (paras 37–40):**

- On NPAs, interest, discount, hire charges, lease rentals and **any other charges** are recognised only on realisation; income recognised earlier and still unrealised is reversed (para 38).
- Interest moratorium: accrual allowed while standard, tested against the RSA restructuring definition (para 39).
- Interest capitalised during a moratorium permitted at sanction is **not reversed** if the loan later becomes NPA (para 40).

**Disclosures:** per FS (para 41; Part 8A.8).

---

---

## 8A.18 RSA — Resolution of Stressed Assets Directions (357)

**Applicability (paras 3–9).** NBFC-D, ICC, Factor, MFI, IFC, IDF, all layers; not CIC, P2P, AA, SPD, NOFHC or the two no-public-funds categories (paras 3, 6). **HFCs: only paras 86–138** (settlements, write-offs, natural calamities, projects, DRS) (para 5); HFC restructuring norms come from the HFC Directions [VERIFY: not supplied]. MGC: paras 86–100 (para 4). Supplied text is the original of 28 Nov 2025 (no "updated as on" date); later amendments are not verified.

- **Part A:** NBFC-D, or NBFC-ND with assets ≥ ₹500 crore (para 7).
- **Part B:** NBFC-ND < ₹500 crore (para 8). Part A paras 13–19, 24–26 and 83–138 also apply to Part B (para 157). Paras 20, 22 and 23 also apply to any NBFC-Factor (para 158).
- *Build:* a Part A/B resolver on the entity profile.
- Ind AS/ICAI prevail on inconsistency (para 9).

**Board policies (paras 13–17):**

- **Resolution policy** with timelines and quantitative and qualitative **financial-difficulty indicators** (paras 13, 15). Indicative list (para 14):
  - any default;
  - probable default without the concession;
  - delisting;
  - cash flows insufficient for contractual servicing;
  - NPA, or NPA but for the concession;
  - internal-rating evidence.
  - Difficulty can exist without arrears (para 15).
- **Settlement and technical write-off policy** (para 16):
  - process and conditions precedent (minimum ageing, collateral deterioration);
  - graded staff-accountability framework;
  - permissible sacrifice by category after realisable value;
  - realisable-value methodology;
  - **approver at least one level above the sanctioning authority; anyone who sanctioned the loan is excluded; fraud and wilful-defaulter settlements need Board approval in all cases** (para 16(5)).

**SMA and reporting (paras 18–26):**

- **SMA bands** (principal, interest or any other amount wholly or partly overdue) (para 18):
  - **SMA-0 up to 30 days;**
  - **SMA-1 more than 30 and up to 60 days;**
  - **SMA-2 more than 60 and up to 90 days.**
- **All loans, including retail, irrespective of size** (para 19).
- **CRILC monthly** for borrowers with aggregate exposure **≥ ₹5 crore**, including SMA status (para 20).
- **Weekly default report by close of business every Friday** (or the preceding working day) (para 21).
- **Accelerated provisioning** for non-reporting, concealment or evergreening (paras 22–23):
  - secured sub-standard, 6–18 months (BL) / 6–12 months (others): 25%;
  - unsecured-ab-initio sub-standard: 25% (≤ 6 months), 40% (thereafter);
  - Doubtful I and II, secured portion: 40%;
  - Doubtful III: 100%.
- Information-utility submissions under IBC (para 24).
- Disclosures per FS (para 25).
- Evergreening or concealment invites enforcement action (para 26).

**Definitions and resolution process (Part A, paras 10, 27–51):**

- **Definitions:**
  - Default = non-payment of debt when any part is due (para 10(4)).
  - **Restructuring** = concessions for reasons of financial difficulty. It includes changes to period, amount, instalment or rate; roll-over; **additional credit to an account in default to cure it**; and **settlements paid over more than 3 months** (para 10(12)).
  - **Review period** = 30 days (para 10(13)).
  - **Satisfactory performance** = no default with any specified lender **at any time** (para 10(14)).
  - **Monitoring period** = until 10% of post-plan principal debt plus capitalised interest is repaid (para 10(8)).
  - **Specified period** = until 20% is repaid (para 10(16)).
- **Review and ICA:**
  - Specified lenders review jointly within the review period (paras 27–28).
  - The ICA binds all signatories at **75% by value and 60% by number**; dissenters receive at least liquidation value (paras 31–33).
- **Resolution plan:**
  - Documented even when no terms change (para 35).
  - ICE needed for restructuring or change of ownership at aggregate exposure **≥ ₹100 crore**: one evaluation, two at ≥ ₹500 crore, all **RP4 or better** (paras 36–41).
  - Normal classification continues while a plan is considered (para 42).
  - Tests for "implemented" (paras 43–44).
  - Implementation within 180 days after the review period ends: ≥ ₹2,000 crore (reference date 7 Jun 2019); ₹1,500–2,000 crore (1 Jan 2020) (paras 45–46).
- **Additional provisions, only at ≥ ₹1,500 crore** (para 47):
  - **20%** if not implemented within 180 days of the end of the review period;
  - **+15%** at 365 days (para 48);
  - over the higher of provisions held or required, capped at 100% (para 49);
  - reversal rules (para 51).

**Restructuring norms (Part A, paras 52–81):**

- Apply to all restructurings, including under IBC (para 52).
- **Classification on restructuring:** standard → **sub-standard immediately**; an NPA keeps its class; ageing continues (paras 53–55).
- **Additional finance:** standard during the monitoring period if performance is satisfactory, otherwise it takes the restructured debt's class (paras 56–57). IBC interim finance is standard during CIRP (para 58).
- **Upgrade:**
  - all facilities perform satisfactorily with all specified lenders during the monitoring period, and **not before one year from the first payment on the facility with the longest moratorium** (para 59);
  - at ≥ ₹100 crore, also investment-grade rating(s), two at ≥ ₹500 crore (para 60);
  - failure needs a fresh restructuring or change of ownership (para 61);
  - default after upgrade but before the specified period ends needs a fresh plan (para 62) and a **15% additional provision**, reversible on upgrade (paras 64–65).
- Provisions follow the IRACP class (para 63). IBC provision freeze (paras 69–73).
- **Income:** accrual if standard, cash if NPA; additional finance in a previously-NPA account on cash basis unless there is a change of ownership (paras 74–75).
- **Change-of-ownership upgrade** (paras 76–80):
  - IBC s.29A check;
  - acquirer not from the existing promoter group;
  - **≥ 26% and the single largest shareholder**;
  - control;
  - provisions released only after the monitoring period.

**Special cases (paras 82–101):**

- **Sale-and-leaseback** = restructuring when all three hold: the seller is in difficulty; > 50% of the buyer's revenue from the asset depends on the seller; ≥ 25% of the buyer's loans for the purchase come from the seller's lenders (para 82).
- **Fraud, malfeasance and wilful default:** these borrowers and associated entities are **ineligible for restructuring** (para 83). Exceptions:
  - new promoters meeting paras 77(1)–(4), with full delinking (para 84);
  - after removal from the wilful-defaulter list (para 85).
- **Compromise settlements and technical write-offs (paras 86–100):**
  - Settlement is not a right (para 87).
  - Future contingent claims must stay off balance sheet, otherwise the arrangement becomes restructuring (para 88).
  - **A settlement paid over more than 3 months, or any part settlement, is restructuring** (paras 89–90).
  - A technical write-off waives nothing and recovery continues (paras 10(18), 91).
  - Partial technical write-off: classified and provisioned on the original gross exposure (para 92).
  - **Reporting:** quarterly to the next higher authority; MD & CEO / Board-committee approvals reported to the Board (para 93).
  - Minimum report content (para 94): q-o-q and y-o-y trend; fraud, red-flagged, wilful-default and quick-mortality split; split by authority, segment and asset class; recovery on written-off accounts.
  - **Cooling period before fresh exposure after a compromise settlement: Board-set, floor 12 months** (para 95). After a technical write-off: per Board policy (para 96).
  - Settlements with fraud or wilful-defaulter borrowers are allowed, without prejudice to criminal proceedings and to FRM/WD penal measures (paras 97–98).
  - **A consent decree is required where recovery proceedings are pending before a judicial forum** (para 100).
- **Natural calamities:** RBI Relief Measures Directions, 2018 apply mutatis mutandis (para 101) [VERIFY: not supplied].

**Projects under implementation (paras 102–122):**

- Apply to financial closure after 1 Oct 2025, or a fresh credit event or material change after it (paras 102–103).
- Credit event (para 10(3)) triggers collective resolution (para 105).
- Report it to CRILC weekly and in CRILC-Main (para 106), and to all consortium members (para 107).
- **Standard is retained** (paras 111–112) for:
  - DCCO deferment of **up to 3 years (infrastructure) or 2 years (non-infrastructure, including CRE/CRE-RH)**;
  - cost overrun ≤ 10%;
  - scope change ≥ 25%, allowed once in the project's life.
- Implementation within 180 days (para 113), otherwise **immediate NPA** (para 114). Upgrade rules: paras 115–116.
- **Additional provision of 0.375% (infrastructure) / 0.5625% (non-infrastructure) per quarter of deferment**, reversed at COD (paras 118–119).

**Government DRS (paras 123–137):**

- Explicit borrower consent, with the cooling period and credit-score impact disclosed (para 127).
- Any waiver counts as a compromise settlement (para 128).
- Residual exposure is tested against the restructuring definition (para 130).
- **No receivable against the Government; IRACP continues until funds are received** (paras 133–134).
- **Relief announced before 31 Dec 2024 with dues pending > 90 days: 100% provision** (para 137).

**Instruments acquired in restructuring (paras 139–156; Part B paras 212–227):**

- FITL, debt and equity take the advance's class (paras 140–141, 212–213, 220–221).
- Provision = higher of the class-based and fair-value provision (para 142); valuation (paras 143–151).
- **Unrealised income is credited to "Sundry Liabilities Account (Interest Capitalisation)"** and recognised only on sale, redemption or upgrade (paras 152–153, 223–225). Depreciation is charged to that account (para 227).

**Part B restructuring (paras 159–211):**

- **Definitions (para 159):**
  - repeatedly restructured account;
  - **specified period = one year from the first payment on the facility with the longest moratorium**;
  - satisfactory performance = no instalment overdue beyond the NPA days, and **no overdues at the end of the specified period**.
- **Eligibility:**
  - standard, sub-standard and doubtful accounts only (para 161);
  - **no retrospective restructuring** (para 163);
  - class fixed as on the approval date (para 165);
  - borrower consent (para 167).
- **Viability and anti-evergreening:**
  - restructuring without a viability and cash-flow assessment is **evergreening** (paras 168–169, 188);
  - benchmarks: ROCE ≥ 5-year G-sec + 2%; DSCR > 1.25 within 5 years and > 1 every year; IRR – cost of funds ≥ 1%; LLR 1.4 (para 171).
- **Package terms:**
  - right to recompense: at least 75% recovered, 100% where below the bare lending rate (para 176);
  - **promoters' personal guarantee** (para 177);
  - **implemented within 120 days of the application** (para 178);
  - **promoter contribution ≥ higher of 20% of the sacrifice or 2% of the restructured debt, brought upfront** (paras 179–180);
  - conversion to equity/preference shares capped (around 10%); equity only for listed companies (para 174).
- **Housing loans:** extend tenure only where repayment capacity holds; offer a higher-EMI option (paras 185–187).
- **Classification and income:**
  - standard → sub-standard; an NPA keeps its class and slips on the **pre-restructuring schedule** (paras 189–190);
  - upgrade after a satisfactory specified period (paras 191–192);
  - additional finance (para 193);
  - repeat restructuring (para 194);
  - income: accrual if standard, cash if NPA (para 195).
- **Provisions:**
  - IRACP class (para 196);
  - higher provision in the first year after upgrade "as prescribed" (para 197) [VERIFY: no rate in the text];
  - **diminution in fair value** = PV before − PV after, both at the bare lending rate, held in a separate account and recomputed every balance-sheet date (paras 198–209);
  - **notional 5% option where total dues are < ₹1 crore** (para 210);
  - total capped at 100% (para 211).

**Trade relief:** Trade Relief Measures Directions of 14 Nov 2025, with a sunset clause (para 228) [VERIFY: not supplied].

---

## 8A.19 RBC — Responsible Business Conduct Directions (362)

**Applicability (paras 3–5).** NBFC-D, ICC, Factor, MFI, IFC, IDF-NBFC and HFC, all layers. NBFC-P2P: paras 98–100 only. Not MGC, CIC, NBFC-AA, SPD, NOFHC, or NBFCs without customer interface. Copy updated as on 1 Apr 2026 (para 42 and Annex II deleted w.e.f. 1 Apr 2026). **Not in this copy:** the Second Amendment (15 Jun 2026, Ch IIIA sales and marketing) and the Third Amendment (6 Aug 2026, Section J, paras 100A–100AB) [VERIFY: amendment text not supplied].

**Board policies (paras 7–8):**

- FPC (preferably vernacular); grievance redressal, with disputes heard and disposed of at least at the next higher level (7(2)); principles for interest, processing, penal and other charges (7(3)); gold/silver lending; microfinance FPC; floating-rate reset incl. fixed/floating switch; engagement of recovery agents; DSA/DMA/RA code of conduct (7(1)–(8)).
- Periodic review of FPC compliance and the grievance machinery, with a consolidated report to the Board at regular intervals (para 8).
- *Build:* policy-registry entries; Board-pack generator for the para 8 report.

**Fair Practices Code (paras 9–21, 26–28):**

- All communications in the vernacular or a language the borrower understands (para 10). *Build:* language preference on the customer; dispatch blocked if no approved template exists in that language.
- Application form carries comparison information and lists required documents (para 11). Acknowledgement of every application, preferably with the disposal timeline (para 12).
- Sanction letter in the vernacular: amount, T&C, **annualised rate and method of application**; acceptance kept on record. **Late-payment penalties in bold** in the loan agreement (para 13).
- Copy of the loan agreement and **every enclosure** to all borrowers at sanction/disbursement (paras 14, 27).
- Notice of any change (disbursement schedule, rates, service or prepayment charges) in the vernacular; rate and charge changes **prospective only**, with a clause in the agreement (para 15). *Build:* no back-dated rate or charge change.
- Recall/acceleration only per the agreement (para 16).
- Release all securities on repayment, subject to lien; set-off needs notice with full particulars of the remaining claims and retention conditions (para 17).
- No interference except per the agreement (para 18).
- Borrower request to transfer the borrowal account: consent or objection **within 21 days** of receipt (para 19). *Build:* service-request type with a 21-day SLA.
- No harassment at odd hours or use of muscle power; staff trained (para 20). FPC on the website (para 21).
- **Vehicle loans:** an enforceable repossession clause covering notice period, waiver circumstances, possession procedure, a final chance to repay before sale/auction, return procedure and sale/auction procedure; copy to the borrower (paras 26–27).
- No disability discrimination; PwD rights module in staff training; PwD grievances through the GRM (para 28).

**Interest (paras 22–25):**

- Board-adopted interest-rate model (cost of funds, margin, risk premium). Rate, risk-gradation approach and rationale disclosed in the application form and explicitly in the sanction letter (22).
- Rates and gradation approach on the website (or in newspapers), updated on every change (23).
- **Rate always annualised** (24).
- *Build:* pricing grid linked to the model version; risk grade stored per loan; website rate feed regenerated on every grid change.

**KFS (para 29; Annex I).** Scope: all retail and MSME term loans; credit-card receivables exempt.

- Annex I format, in a language the borrower understands; contents explained; **acknowledgement of understanding** obtained (29(1)).
- **Unique proposal number.** Validity **≥ 3 working days (tenor ≥ 7 days) / 1 working day (tenor < 7 days)**; the NBFC is bound by the KFS terms if the borrower agrees within it. It is not a waiting period (29(2)).
- APR computation sheet and amortisation schedule; **APR includes all charges levied by the NBFC** (29(3)) and third-party charges recovered at actuals (insurance, legal), disclosed separately; receipts for each third-party payment within a reasonable time (29(4)).
- **No fee or charge outside the KFS at any stage without explicit consent** (29(5)). KFS reproduced as a summary box in the loan agreement (29(6)).
- **Annex I Part 1:**
  - (1) proposal/account no., loan type; (2) sanctioned amount; (3) disbursal schedule (100% upfront or staged, with the agreement clause); (4) term; (5) instalment type, no. of EPIs, EPI ₹, commencement post-sanction; (6) rate % and type (fixed/floating/hybrid);
  - (7) floating: reference benchmark, B %, spread S %, R = B + S, reset periodicity in months (fixed reset other than on credit-profile change), and the impact of a **25 bps change in R** on EPI ₹ and no. of EPIs;
  - (8) fees, split A (payable to the NBFC) / B (third party through the NBFC), each one-time/recurring and ₹ or % with frequency: processing, insurance, valuation, any other (may be shown net of GST);
  - (9) APR %; (10) contingent charges: penal for delayed payment, other penal, foreclosure, floating↔fixed switch, any other.
- **Annex I Part 2:** (1) recovery-agent clause of the agreement; (2) GRM clause; (3) nodal GRO phone and email (a generic email only if the response comes **within 1 working day**); (4) whether the loan is or may be transferred/securitised (Y/N); (5) collaborative lending (co-lending/outsourcing): originating RE and its funding share, partner RE and its share, **blended rate**; (6) digital loans: cooling-off/look-up period with no prepayment penalty, and the LSP acting as recovery agent.
- **APR rule (29(3) illustration):** net disbursed = sanctioned amount − all fees (NBFC + third party). APR = periodic IRR on the net disbursed amount (reducing balance) × periods per year. Charges not determinable before sanction may be shown as an upper ceiling.
  - **Golden test:** ₹20,000, 24 monthly EPIs, 15% fixed, fees ₹400 (₹240 NBFC + ₹160 third party). EPI ₹969.73 (₹970 in the schedule), total interest ₹3,274, net disbursed ₹19,600, **APR 17.07%** (recomputed: monthly IRR × 12 on the unrounded EPI; ₹970 gives 17.10%).

**Penal charges (para 30).** Scope: all credit facilities except credit cards, ECBs, trade credits, structured obligations and other FX loans.

- Penalty for breach of material terms (incl. payment default) **only as penal charges, never penal interest; no capitalisation**; interest on unpaid interest/EMI only at the contracted rate till remediation (30(1)).
- Levied **only on the amount under default**, non-discriminatory, per Board policy (30(1) Note (ii)); **no penal charge on earlier penal charges** (Note (iii)); GST per CBIC (Note (iv)).
- No added rate component (30(2)); Board policy (30(3)); reasonable, uniform within a product irrespective of the borrower's constitution, may vary by loan amount, not a revenue tool (30(4)).
- **Individual non-business ≤ non-individual** for similar non-compliance (30(5)).
- Quantum and reason disclosed in the agreement, MITC/KFS and on the website ("Interest rates and Service Charges"); a website reference alone does not suffice (30(6)).
- Applicable penal charges shown in every non-compliance reminder; each levy and its reason communicated (30(7)). Existing loans switch at the next review/renewal (30(8)).
- *Build:* penal base = overdue amount only; excluded from the interest base; cross-schedule validator for 30(5).

**Floating-rate reset (paras 31–32).** EMI-based floating-rate personal loans ("personal loans" per XBRL, para 6(11)); mutatis mutandis to equated-instalment loans of any periodicity, on external or internal benchmarks; **not other loan types** (32).

- At sanction, disclose the EMI/tenor impact of benchmark changes; any increase communicated **immediately** (31(1)).
- Switch to fixed **at the NBFC's option** per Board policy, which may cap the number of switches (31(2)).
- Borrower chooses higher EMI, longer tenor or both, and may prepay in part or full at any time (31(3)).
- Switch and incidental charges in the sanction letter and on revision; Board-approved; on the website (31(4)).
- **No negative amortisation** (31(5)).
- **Quarterly statement:** principal and interest recovered to date, EMI, EMIs left, annualised rate/APR for the full tenor (31(6)).
- EBLR loans: information systems to monitor transmission (32).

**Pre-payment charges (paras 33–34, 81):**

- Sanctioned/renewed **on or before 31 Dec 2025**: none on floating-rate **term** loans to individuals for non-business purposes, with or without co-obligants (33).
- Term **and demand** loans sanctioned/renewed **on or after 1 Jan 2026**:
  - floating, individual, non-business: none, all layers (34(1));
  - floating, business purpose, individuals and MSEs (MSMED Act): **UL none; ML none if the sanctioned amount/limit is ≤ ₹50 lakh** (34(2)); BL per policy.
- Any source of funds; **no lock-in** (34(3)). Dual/special-rate loans: rate type at the time of prepayment decides (34(4)).
- Other cases per policy; term loans on the amount prepaid; CC/OD closure before the due date on ≤ sanctioned limit (34(5)). CC/OD: none if non-renewal was intimated within the agreed period and the facility closes on the due date (34(6)).
- **None where the NBFC initiates the prepayment** (34(7)). Disclosed in the sanction letter, agreement and KFS; **undisclosed = not chargeable** (34(8)). No retrospective levy of earlier waived charges (34(9)).
- **Microfinance: none** (81).

**Release of property documents (paras 35–41), personal loans:**

- All original movable/immovable property documents released and **registered charges removed within 30 days** of full repayment/settlement (35). Borrower chooses the collection office (36). Timeline and place stated in sanction letters from 1 Dec 2023 (37).
- Legal-heir procedure displayed on the website (38).
- Reasons for delay communicated; **₹5,000 per day** where the delay is attributable to the NBFC (39).
- Lost/damaged documents: assist with duplicates/certified copies at the NBFC's cost, plus compensation; penalty runs only **after 60 days** (40). Without prejudice to other law (41).
- *Build:* release clock from the closure date; attribution flag; compensation auto-computed; 30/60-day clocks.

**Gold and silver collateral conduct (Ch III.G, paras 43–75):**

- **Policy and assay (43–47):** policy/SOP covers assay, assayer criteria, auction trigger, notice timeline, mode, notice period, auctioneer empanelment, and the loss/discrepancy procedure with compensation timelines (43). One assay procedure across all branches (44). Net-weight and price methodology on the website (45). **Borrower present at assay**; deductions explained (46). Loss or discrepancy recorded and communicated, with the compensation process (47).
- **Documents (48–51):** standard documentation (48). Agreement covers the collateral, its value, auction triggers and procedure, pre-auction notice period, release timeline and surplus refund; assay and auction charges in the agreement **and KFS** (49). **Assay certificate** (paper or e-, in duplicate, on letterhead): carats, gross weight, net metal weight and deductions, damage/defects, **image**, value at sanction; one copy to the borrower against acknowledgement (50). Illiterate borrower: terms explained before a **non-employee witness** (51).
- **Custody (52–57):** handling and storage only in employee-manned branches with vaults (52–54); transfers only per para 64, branch shifting/closure, or policy exception (55); review, training and internal audit (56); **periodic surprise verification** with records and a consent clause in the agreement (57).
- **Release (58–59):** **same day, and in any case within 7 working days** of full repayment/settlement (58); verified against the certificate (59).
- **Auction (60–66):**
  - notice to repay before auction, with copy and acknowledgement kept; untraceable borrower: public notice **+ 1 month** (60);
  - advertisements in **at least 2 newspapers** (one regional-language, one national daily) (61);
  - employee with experience/training or empanelled auctioneer, with safeguards (62);
  - **reserve price ≥ 90% of current value; ≥ 85% after two failed auctions** (63);
  - first auction physical in the lending branch's district; after failure, adjoining district or online (64);
  - NBFC and its related parties barred from bidding (65);
  - full details of value fetched and dues adjusted; **surplus refunded within 7 working days** of receiving the full proceeds; shortfall per the agreement (66).
- **Compensation (67–70):** repair cost borne by the NBFC (67); loss/discrepancy compensated (68); **₹5,000 per day beyond the para 58 timeline** if attributable to the NBFC, otherwise reasons communicated; periodic reminders to borrowers who have not collected (69); without prejudice (70).
- **Unclaimed (71–72):** after **2 years** from full repayment/settlement, with special drives (71); **half-yearly report** to the Customer Service Committee or Board (72).
- **Other (73–75):** no misleading advertisements (73); sourcing and recovery arrangements comply with outsourcing and recovery rules (74); prudential rules in CF Ch IV (75).

**Microfinance conduct (paras 76–92):**

- Board-approved FPC displayed in offices and on the website, in the borrower's language (76); standard vernacular loan agreement (77).
- **Loan card:** borrower identity, simplified pricing factsheet, all other T&C, acknowledgement of every repayment and the final discharge, nodal officer name and number (78); entries in the borrower's language (79). Non-credit products only with full consent, fees shown in the loan card (80).
- **No prepayment charge**; delayed-payment charges **on the overdue amount only** (81).
- Minimum, maximum and average rates displayed in offices, literature and website, and included in supervisory returns (82). Rate/charge changes notified well in advance, prospective only (83).
- Staff conduct policy, recruitment and training (86); field staff enquire into household income and existing debt (87); borrower training free (88).
- Identify and engage borrowers facing repayment difficulty (89).
- Recovery at the mutually agreed designated place; residence/workplace only after **two or more successive** non-appearances (90).
- **Harsh methods banned:** threatening/abusive language; persistent calls or calls **before 09:00 or after 18:00**; harassing relatives, friends or co-workers; publishing names; violence; misleading statements on the debt or its consequences (91).
- Dedicated recovery-grievance mechanism, with details given at disbursal (92).

**Recovery agents, DSA/DMA, telemarketers (paras 93–101).** Paras 93–97 sit in Section H (microfinance); paras 98–100 are general and also bind NBFC-P2P (para 4).

- Agent due diligence covering individuals; agency to do antecedent and **police verification**; re-verification periodicity set by the NBFC (94).
- Agent details to the borrower when recovery starts; agent carries the notice, authorisation letter and ID; borrower notified on a change of agency and the new agent carries the same (95). Notice and authorisation include contact details of the agency and the NBFC (96). Up-to-date agency list on the website (97).
- DSA/DMA/RA training on soliciting, calling hours, privacy and correct T&C (98). Code-of-conduct undertaking; RAs follow the FPC and the NBFC's collection/repossession code; confidentiality (99).
- **No intimidation or harassment**: public humiliation, intrusion on family/referees/friends, inappropriate mobile or social-media messages, threatening or anonymous calls, persistent calls, **calls before 08:00 or after 19:00** for overdue recovery, false representations. **Not applicable to microfinance loans** (100).
- Only DoT/TRAI-registered telemarketers; list with registered numbers to TRAI; existing agents to register (101).
- Third Amendment (Section J, paras 100A–100AB, from 1 Jan 2027) and Second Amendment (Ch IIIA) are not in this copy [VERIFY: amendment text not supplied].

**Miscellaneous (paras 102–105):**

- Branch/office closure: **at least 3 months'** public notice in a national and a local vernacular newspaper (102).
- **All transactions rounded to the nearest rupee** (50 paise and above up, below 50 paise ignored); cheques with paise not rejected (103). *Build:* round each posted transaction; accrual precision kept internally (design rule).
- Locker facility: disclose that it is not regulated by RBI (104).
- Comply with the Supreme Court order of 30 Apr 2025 (Pragya Prasun; Amar Jain) (105) [VERIFY: order content not reproduced in the text].

**Not in this text:** GRO appointment/display rules, NOC format, insurance-bundling rules (beyond 29(4) and 80), co-lending conduct beyond Annex I Part 2 item 5. Keep M15 and related controls on their other sources.

---

---

## 8A.20 WD — Treatment of Wilful Defaulters and Large Defaulters Directions (358)

**Applicability (para 2).** NBFC-ML and above: NBFC-D, ICC, Factor, MFI, IFC, IDF-NBFC, HFC, CIC. Not MGC, P2P, AA, SPD, NOFHC, or NBFCs without public funds and customer interface. **Proviso:** the bar on further finance to wilful defaulters and the large-defaulter provisions apply to **all RBI-regulated entities**, so Base Layer tenants get the screening and penal gates. Original text, 28 Nov 2025, immediate effect.

**Definitions (para 3(1)):**

- **Wilful default by a borrower** ((xviii)(A)): a default plus any one of: capacity to pay; diversion; siphoning; disposal of security without approval; failed equity commitment despite ability where loans or concessions relied on it.
- **By a guarantor** ((xviii)(B)): invoked guarantee not honoured despite sufficient means; disposal of security; failed equity commitment.
- **Diversion** ((vii)(a)–(f)): short-term WC used for long-term purposes; other assets; transfers to subsidiaries/group entities without approval; routing through other lenders without permission; investment in other companies without approval; unexplained deployment shortfall. **Siphoning** ((xvi)): use unrelated to the borrower's operations.
- **Wilful defaulter** ((xix)): outstanding **≥ ₹25 lakh** (or as notified), plus, for a company, its promoters and directors (subject to 5(14)); for other entities, persons in charge.
- **Large defaulter** ((xi)): outstanding **≥ ₹1 crore** and suit filed, or classified doubtful/loss.
- **Suit-filed** ((xvii)): includes IBC, SARFAESI, pending appeals or execution, and resolution or liquidation proceedings.
- **Director** ((v)): associated at the time of the acts leading to default.
- **Identification Committee** ((ix)): chair not more than one rank below MD/CEO + two senior officials not more than two ranks below the chair.
- **Review Committee** ((xv)): MD/CEO as chair + two independent/non-executive directors or equivalent officials; **no overlap** with the IC.

**Board policy (para 4):** rank of the designated official serving notices and orders; re-examination periodicity; non-discriminatory photo-publication criteria; end-use measures; forensic-audit threshold (20(6)).

**Process (paras 5–6):**

- Examine all **NPAs with outstanding ≥ ₹25 lakh** (6(1)), on the track record and not isolated incidents; the default must be intentional, deliberate and calculated (5(1)–(2)).
- If observed in preliminary screening: **complete classification within 6 months of the NPA date** (6(2)). If not: re-examine at the Board-set periodicity (6(3)).
- IC examines the evidence (5(3)) → **show-cause notice** to the borrower, guarantor, promoters, directors and persons in charge, disclosing all material; **submissions within 21 days** (5(4)).
- IC proposal to the RC with written reasons; no referral if not wilful (5(5)); persons advised of the proposal with reasons (5(6)); **written representation to the RC within 15 days** (5(7)).
- RC considers the proposal and representation (5(8)); **personal hearing offered**; if not availed, decided on record (5(9)); **no right to be represented by a lawyer** (5(10)).
- **Reasoned order** communicated (5(11)); notice and order served by the designated official, stating the committee's approval and **naming its members** (5(12)–(13)).
- Non-whole-time, independent or nominee directors are classified only on consent/connivance, or on awareness minuted without objection (5(14)); if classified, they are reported in Annex II flagged as such (5(15)).
- *Build:* case state machine with 21-day and 15-day timers and a 6-month deadline alert; committee-composition validator (rank, independence, no overlap); evidence vault; no advocate attendee role.

**Penal measures (para 7)**, for any person classified by **any** lender:

- **No additional credit facility** to the wilful defaulter or associated entities, continuing **1 year after removal from the LWD** (7(3)(i)–(ii)).
- **No finance for new ventures for 5 years after removal** (7(3)(iii)).
- Restructuring per the RSA Directions (7(3)(iv)).
- Bars cease for entities no longer associated. Associated = subsidiary/JV/associate (Cos Act s.2(87), 2(6)) of a company, or entities where an individual is promoter, director or in charge (Expl. 1–2). Delinked new promoters under RSA: restructuring may be considered (Expl. 3).
- Criminal proceedings considered case by case; they survive LWD removal (7(1)). Photo publication per Board policy (7(2)).
- **Covenant** in every credit agreement: no LWD person on the borrower's board or in its management, with expeditious removal; **no renewal, enhancement, fresh facility or restructuring** while such a person remains (7(4)). Legal action for recovery where warranted (7(5)).
- *Build:* screening gate at application, renewal, enhancement, top-up and restructuring; removal date with 1-year and 5-year clocks; new-venture purpose flag.

**Governance and guarantors (paras 8–10):**

- Transparent mechanism (8). Internal auditors check adherence; Audit Committee periodically reviews cases and root causes (9).
- Guarantor liability is co-extensive and immediate on claim; the NBFC may proceed without exhausting remedies against the principal debtor; a refusing guarantor is considered for classification (10(1)–(4)). Group companies not honouring invoked guarantees are also considered (10(5)).

**Reporting (paras 11–18; Annexes I–II):**

- **Large defaulters, monthly, to all CICs** (Annex I): suit-filed list; non-suit-filed doubtful/loss list (11(1)). The ₹1 crore threshold includes unapplied interest; for suit-filed accounts, the suit amount (11(2)).
- **LWD, monthly, to all CICs** (Annex II): suit-filed and non-suit-filed lists (12(1)); separate files; **SFTP**.
- **Removal intimated within 30 days** of the outstanding falling below ₹25 lakh, subject to 13(2) (12(2)). An ML NBFC reclassified as BL stops classifying but keeps updating historical data (12(3)).
- **Compromise settlement:** removed from the LWD **only when the compromise amount is fully paid**; the name stays despite part-payment below ₹25 lakh (13(1)–(2)); the settlement must meet the RSA Directions (13(3)); a cancelled settlement is reported at the revised amount (13(4)).
- **Transfer of defaulted loans ≥ ₹25 lakh (NPA or not):** comprehensive wilful-default investigation first (two-stage committee not required); if observed, classify and report in the LWD **before transfer**; details passed to the transferee, who then reports (14(1)–(3)). Transfer is not recovery for the threshold (14(4)). The transferee reports until balance + transferor write-off falls below ₹25 lakh (14(5)).
- **IBC/RBI resolution with change of management/control, or liquidation:** removed from the LWD after implementation; 7(3) measures not applied to the entity, but 7(3)(ii)–(iii) continue for erstwhile promoters, directors, guarantors and persons in charge, and their associated entities (15).
- Accuracy is the reporting NBFC's responsibility; director particulars cross-checked with ROC (16); guarantors failing to honour reported (17); directors' full names and **DIN** reported (18).
- **Annex I fields:** reporting cycle (MMMYY); member ID, name, branch, state; borrower name, PAN, address; outstanding (₹ lakh); suit status 01/02; asset class (non-suit DOUBT/LOSS; suit also SUBST/STD); asset-class date (MMMYY); other lenders; director/promoter name, DIN, PAN; guarantor name, CIN, PAN. Row-level, multiple directors/guarantors; **non-whole-time/independent/nominee directors excluded**; legend for Government undertakings; separate suit/non-suit files.
- **Annex II fields:** as Annex I but without the asset-class fields; submitted through SFTP.

**Prevention (paras 19–21):**

- At appraisal, check directors, guarantors and persons in charge against the large-defaulter list and LWD by **DIN/PAN**; resolve identical names through **independent sources, not a borrower declaration** (19(1)).
- End-use monitoring: borrower end-use certificates (legal action for false certification); illustrative measures in the loan policy: quarterly progress reports, asset inspections, scrutiny of books and no-lien accounts, unit visits, stock audit for WC, management audit of the credit function (19(2)); project finance: CA certification plus own due diligence (19(2)(iii)).
- Auditors: complaint to NFRA/ICAI if negligent; forwarded to RBI (DoS, CO) and IBA after a hearing (20(1)–(2)); loan covenant enabling a separate mandate to the borrower's auditor (20(4)); own auditors permitted (20(5)); forensic audit above the Board threshold (20(6)).
- Negligent or facilitating third parties: details to IBA after an opportunity of hearing (21).
- *Build:* end-use certificate tracker; auditor and third-party complaint register with hearing record.

---

## 8A.21 KYC — Know Your Customer Directions (361)

**Metadata and applicability.**
- RBI/DOR/2025-26/361; DOR.AML.REC.No.280/14.01.003/2025-26; 28 Nov 2025, updated as on 29 Dec 2025.
- Takes effect when placed on the RBI website (para 2).
- Applies to all NBFC categories and layers, except NBFCs with no customer interface (para 3).
- Also applies to overseas branches and majority-owned subsidiaries; where standards differ, the stricter one applies (para 4).
- Annex I is the MHA UAPA s.51A Order. Annex II is the MoF WMD s.12A Order (1 Sep 2023).

**Governance (paras 6–15):**
- **KYC policy.** Approved by the Board or a committee. It covers the customer acceptance policy, risk management, CIP and transaction monitoring. It also covers periodic updation, exceptional measures, any-branch updation, and change of the registered mobile for non-face-to-face (NFTF) accounts (para 6).
- **Group-wide AML/CFT programme**, with safeguards against tipping-off (para 8).
- **ML/TF risk assessment:** documented and **reviewed at least annually**; the outcome goes to the Board or committee (para 10).
- **Audit:** concurrent/internal audit of KYC, with **quarterly audit notes to the Audit Committee** (para 12(4)–(5)).
- **No outsourcing of KYC decision-making** (para 13).
  - *Build:* LSP and vendor KYC results are evidence only. A tenant user records the "KYC complete" decision.
- **Designated Director and Principal Officer.**
  - The Designated Director is an MD or WTD authorised by the Board (para 5(1)(vii)).
  - Name, designation, address and contact details of both go to FIU-IND and RBI.
  - **The Principal Officer must not be the Designated Director** (paras 14–15).
  - *Build:* role register with a block that enforces this separation.

**Customer acceptance (paras 16–19):**
- No anonymous or benami accounts. No account or transaction without CDD. Consider an STR when CDD cannot be completed (para 17(1)–(3)).
- KYC fields are set by policy. Extra information is collected only with explicit consent (para 17(4)–(5)).
- **CDD is done at UCIC level**, so an existing customer needs no fresh identification for a new product (para 17(6)).
- CDD for every joint holder (para 17(7)).
- A system to match customers against the sanctions lists (para 17(9)).
- **Verification:**
  - PAN against the issuing authority (para 17(10));
  - the digital signature on e-documents (para 17(11));
  - GSTIN, where available (para 17(12)).
- **No rejection of onboarding or periodic updation without application of mind; the reason is recorded** (para 18).
- If CDD would tip off the customer, stop CDD and file an STR (para 19).

**Risk categorisation (paras 20, 41):**
- Low, medium or high, based on identity, status, business, geography, product, channel and transaction type (para 20(1)–(3)).
- **The category and the reasons for it are never shown to the customer** (para 20(4)).
- **Categorisation is reviewed at least once every six months** (para 41(1)).
- Monitoring intensity follows the category. Marketing and MLM firms get close monitoring (para 41(2)).

**When to identify (paras 21–22):**
- Triggers (para 21):
  - start of an account-based relationship;
  - doubt about the identification data;
  - walk-in, own-product or third-party-product transactions of **₹50,000 or more**, single or connected;
  - suspected structuring below that threshold.
- Introductions are not sought (para 21(7)).
- **Relying on a third party's CDD** requires all of the following (para 22):
  - the records are obtained immediately from the third party or from CKYCR;
  - the third party is regulated;
  - it is not in a high-risk jurisdiction;
  - the NBFC keeps final responsibility.

**CDD for individuals (para 23).** This also covers beneficial owners, authorised signatories and PoA holders of legal entities.
- **What to collect:** one or more of the following, **plus PAN or Form 60** (para 23(1)–(5)):
  - the Aadhaar number, only where the customer seeks an Aadhaar Act s.7 benefit, or volunteers it to an NBFC **notified under the first proviso to s.11A(1) of the PML Act**;
  - proof of possession of Aadhaar;
  - an OVD or its e-document;
  - the KYC Identifier, with explicit consent to download from CKYCR.
- **How to verify, by mode** (provisos (i)–(v)):

  | Document submitted | Verification method |
  |---|---|
  | Aadhaar number (notified NBFCs only) | UIDAI **e-KYC authentication**; a different current address by self-declaration |
  | Proof of possession of Aadhaar | **Offline verification** |
  | E-document | **Digital-signature check plus a live photo** |
  | Physical OVD, or Aadhaar where offline verification is not possible | **Digital KYC (para 24)**. A certified copy plus a photo is allowed only until a date the Government notifies |
  | KYC Identifier | CKYCR download |

- **Redact the Aadhaar number** where authentication is not required (Expl 1).
- An official may use biometric e-KYC, including **Aadhaar Face Authentication** (Expl 2).
- **Aadhaar is not mandatory** (Expl 4).
- **OVDs and deemed OVDs** (para 5(1)(xiv)):
  - OVDs are the passport, driving licence, proof of possession of Aadhaar, Voter ID, NREGA job card and NPR letter.
  - Deemed OVDs prove address only: a utility bill no more than 2 months old, a property-tax receipt, a PPO, or an employer allotment letter.
  - **An OVD with the current address is due within 3 months.**

**Digital KYC application (para 24).** *Build:* in M22.
- The NBFC's authenticated app only. Access by login and password, or by a live or time-based OTP (para 24(1)–(2)).
- **Customer photo** (para 24(4)–(5)):
  - **live capture only**, with a white background and no other person in frame;
  - embedded in the CAF;
  - **watermarked with the CAF number, GPS coordinates, the official's name and employee code, the date (DD:MM:YYYY) and the time (HH:MM:SS)**.
- **OVD photo:** taken flat from above with no tilt, with the same watermark (para 24(6)–(7)). QR auto-fill is allowed (para 24(8)).
- **Customer signature** is an OTP whose message reads exactly **"Please verify the details filled in form before sharing OTP"**. A family member's number is allowed if it is noted on the CAF. **The system must reject the officer's own registered mobile** (para 24(9)).
- **Officer declaration:** OTP to the officer's registered mobile, with a live photo of the officer (para 24(10)).
- The app generates a reference ID for the customer (para 24(11)). The officer runs the para 24(12) checks.
- **Final step:** the officer digitally signs the CAF; it is printed, signed or thumb-marked by the customer, scanned and uploaded (para 24(13)).

**Aadhaar OTP e-KYC in non-face-to-face mode (para 25):**
- Specific consent to OTP authentication (para 25(1)).
- **Alerts and OTPs go only to the Aadhaar-registered mobile.** A Board policy governs mobile changes (para 25(2)).
- **Loan accounts: term loans only, with total sanctions of no more than ₹60,000 a year** (para 25(5)).
- **Full CDD is due within one year.** It can be done under para 23 or by V-CIP, which needs a fresh Aadhaar OTP. Without it, **no further debits are allowed on the loan account** (para 25(6)–(7)).
- The customer declares no other OTP-e-KYC account with any RE. The CKYCR upload is flagged as OTP e-KYC (para 25(8)).
- **Violation alerts** (para 25(9)).
- These limits do not apply to updation done by OTP e-KYC (para 42(3)(v)).

**V-CIP (paras 26–27):**
- **Uses (para 26):**
  - new individuals, proprietors (plus e-documents of the activity proofs), authorised signatories and BOs;
  - converting para 25 accounts;
  - updation.
- **Infrastructure (para 27(1)):**
  - Hosted on the NBFC's premises, and sessions start from its own secured network.
  - **Cloud is allowed only if all data and recordings move immediately to servers the NBFC exclusively owns or leases, and the provider keeps nothing.**
  - End-to-end encryption, and consent recorded in an alteration-proof way.
  - **Block IP addresses outside India and spoofed IPs.**
  - The video carries a geo-tag and a timestamp.
  - Liveness/spoof detection and face match. Gestures are not mandatory, and special needs are accommodated.
  - Forged-identity cases are reported as cyber events.
  - **VAPT and security audit by a CERT-In-empanelled auditor, plus functional and performance tests, before go-live and periodically.**
- **Procedure (para 27(2)):**
  - Only specially trained officials run sessions.
  - A pause must not create multiple files. **A dropped call means a fresh session.**
  - Question order varies. **Reject the session if the customer is being prompted.**
  - Check whether the customer is existing, previously rejected or on a negative list.
  - Identification sources: OTP e-KYC, offline Aadhaar, CKYCR, or an e-OVD/DigiLocker document. Redact the Aadhaar number.
  - **The Aadhaar XML/QR must be no more than 3 working days old. The video must happen within 3 working days of obtaining the identification data.**
  - Record the current address and confirm the economic and financial profile.
  - Capture a clear image of the PAN card unless e-PAN is given, and verify PAN with the issuer.
  - **Printed e-documents are invalid.**
  - **The account becomes operational only after concurrent audit.**
- **Records (para 27(3)):**
  - stored in India, with searchable timestamps;
  - an activity log with the credentials of the official who ran the session.

**Other CDD (paras 28–38):**
- **Simplified accounts** (para 28): 12 months, with caps of ₹50,000 balance and ₹1 lakh credits a year, and alerts at ₹40,000 and ₹80,000. *Build:* configurable, off by default.
- KYC carries over on a branch transfer (para 29).
- **Proprietorships:** CDD of the proprietor plus **two** activity proofs, such as Udyam, GST or a full ITR. One proof is enough only with contact-point verification (paras 30–32).
- **Document checklists** for companies, partnerships, trusts, unincorporated associations/BOIs and other juridical persons (paras 33–37).
- **BO thresholds** (para 5(1)(iv)):
  - company: **more than 10%** of shares, capital or profits, or control;
  - partnership: **more than 10%** of capital or profits;
  - unincorporated association or BOI: **more than 15%**;
  - trust: author, trustees, beneficiaries with **10% or more**, and controllers;
  - otherwise, the senior managing official.
- Listed entities and their subsidiaries are exempt from BO identification (para 38(1)).

**Monitoring and updation (paras 39–43):**
- **Monitoring typologies:** large or complex transactions, threshold breaches, high turnover, and third-party cheques followed by cash. AI/ML is permitted (para 40).
- **Periodic updation at least every 2, 8 and 10 years** for high, medium and low risk (para 42(1)).
- **Low-risk individuals: transactions continue, with updation due within 1 year of the due date or by 30 Jun 2026, whichever is later** (para 42(2)).
- **Individuals (para 42(3)):**
  - no change: self-declaration through the registered channels;
  - change of address: self-declaration plus **positive confirmation within 2 months**;
  - minors turning major: fresh photo and current-standard CDD;
  - OTP e-KYC: the Aadhaar mobile must match the one on the profile.
- **Legal entities:** self-declaration and a BO refresh. Any change triggers onboarding-equivalent KYC (para 42(4)).
- **Every updation:**
  - documents meet current CDD standards; expired documents mean fresh KYC;
  - PAN is re-verified;
  - **the customer gets an acknowledgement with the date of receipt, and an intimation of the updation date** (paras 42(5), 63(8)).
- Customers submit document changes **within 30 days** (para 42(6)).
- **Notices:** at least **3 advance intimations and at least 3 post-due reminders, each set including at least one letter, logged per customer. Required by 1 Jan 2026** (para 42(7)).
- **No PAN or Form 60 by the notified date** (para 43):
  - notice and a hearing first;
  - then temporary cessation, under which **loan accounts accept credits only**;
  - relaxation for infirmity, with enhanced monitoring;
  - a customer's written refusal leads to closure.

**EDD and PEPs (paras 44–46, 59):**
- **Non-face-to-face onboarding** (CKYCR, DigiLocker or e-documents; other than para 25) (para 44):
  - **offer V-CIP first**;
  - no alternate mobile number;
  - **positive address confirmation before the account operates**;
  - PAN verified;
  - **the first transaction is a credit from the customer's own KYC-compliant bank account**;
  - **the customer is high-risk until verified face to face or by V-CIP**.
- **PEPs** (para 45):
  - The definition covers foreign prominent public functions only, and extends to family and close associates.
  - A detection system, and the source of funds or wealth.
  - **Senior-management approval to open, and again to continue when an existing customer or BO becomes a PEP.**
  - Enhanced monitoring.
- **FATF-listed jurisdictions:** EDD, with **written findings kept** (para 59).

**Records (paras 47–48):**
- Transaction records: **at least 5 years from the transaction date**.
- Identification records, including files, correspondence and analysis results: **at least 5 years after the relationship ends**.
- Each transaction can be reconstructed (nature, amount, currency, date, parties), and records are retrievable quickly (para 47).
- **NPO customers** are registered on **NITI Aayog DARPAN**; records kept for 5 years after the end of the relationship or the account closure, whichever is later (para 48).

**FIU-IND reporting (paras 49–53, 65):**
- Reports under Rules 3 and 7 of the PML Rules, in FIU-IND formats and utilities (paras 49–50). **The Directions set no CTR or STR deadlines** [VERIFY: PML Rules r.8].
- **Each day of delay is a separate violation. An STR alone must not restrict account operations** (para 51).
- Reporting is confidential (para 52).
- **Software must raise alerts when transactions do not fit the risk category or profile** (para 53).
- An established money-mule account with no STR filed counts as non-compliance (para 65).

**Sanctions (paras 54–57; Annexes I–II):**
- **Daily checks** of:
  - the UNSC ISIL/Al-Qaida and Taliban lists and the 2007 Order Schedules (para 54(2));
  - **the UNSCR 1718 list (DPRK)** (para 56).
- Also check UAPA Schedules 1 and 4 and other UNSCRs (para 57), and the WMD list on the FIU-India portal at onboarding and periodically (para 55(3), (6)).
- **On a UAPA match:**
  - report to FIU-IND and MHA (para 54(3));
  - inform the UAPA central nodal officer immediately, with copies to the State nodal officer, RBI and FIU-IND;
  - **block transactions if the match is beyond doubt**;
  - file an STR covering every transaction;
  - implement freeze orders (Annex I 5.1).
- **On a WMD match:** **do not transact**; inform the CNO (Director, FIU-IND) immediately, with copies to the State Nodal Officer and RBI; freeze without delay on order (para 55(2)–(8)).
- **Forward unfreeze applications within 2 working days** (para 55(9); Annex I 11.2).
- Frozen accounts may receive interest and payments due under pre-listing contracts (Annex I 10.2; Annex II 6.2).

**Other (paras 61–72):**
- **Secrecy:** no use of account-opening data for cross-selling without the customer's express permission (para 61).
- **CKYCR (para 63):**
  - **Upload within 10 days** of the relationship starting (para 63(1)).
  - **Send updated information within 7 days.** When CKYCR notifies an update, retrieve the records and update the tenant's copy (para 63(7)).
  - Give the KYC Identifier to the customer (para 63(6)).
  - Use the KYC Identifier first. Ask for documents again only if they have changed, are incomplete or expired, or are needed for EDD or the risk profile (para 63(9)).
  - **29 Dec 2025 Explanation:** the RE that last uploaded the record is responsible for identity and address verification. **A downloader relying on current, compliant records need not re-verify identity or address**, but stays responsible for all other CDD.
- **FATCA/CRS:** if the NBFC is a Reporting FI under IT Rule 114F, it files Form 61B or a NIL report with the Designated Director's DSC, and needs an IT framework, an audit and a High-Level Monitoring Committee (para 64).
- **UCIC for every individual customer**, new and existing (paras 66–67).
- **ML/TF risk assessment before any new product or technology is launched** (para 68).
- **Wire transfers:**
  - Cross-border and qualifying domestic transfers carry originator and beneficiary data. Domestic transfers qualify where the originator holds an account with the ordering NBFC, or is a non-account-holder sending ₹50,000 or more.
  - Requested information is supplied within 3 working days.
  - A transfer that cannot comply is not executed (para 69).
  - *Build:* only where the tenant is the ordering, intermediary or beneficiary institution.
- **Sales of third-party or own products of ₹50,000 or more:** **paid only by account debit or cheque, with PAN verified**, plus AML alerts (para 71).
- Know-Your-Employee screening and role-specific AML training (para 72).

---

## 8A.22 TDCR — Transfer and Distribution of Credit Risk Directions (352)

**Applicability (para 3).** NBFC-D, ICC, Factor, MFI, IFC, IDF-NBFC and HFCs, all layers. Not MGC, P2P, AA, CIC, SPD, NOFHC, NBFCs with neither public funds nor customer interface, or Base Layer NBFCs with customer interface but no public funds. Part A in force on issue; **Part B from 1 Jan 2026** or an earlier date set by internal policy (paras 2, 95).

**Structure:** Ch I paras 1–5; Part A Transfer of loan exposures (scope/definitions 6–12; general 13–30; loans not in default 31–52; stressed loans, ARCs, Swiss challenge, reporting 53–94); Part B Co-lending 95–127; Part C 128–131.

### Part A — Transfer of loan exposures

**Scope and parties (paras 7–12):**

- Acquire only from a "lender" in para 12(4) (para 7). No transfer or acquisition outside Part A, other than securitisation (SEC), guarantees or explicitly permitted products (para 8).
- Covers assignment, novation and loan participation. Except for participation, **legal ownership must pass** to the extent of economic interest transferred (para 9).
- **Lenders (para 12(4)):** SCBs, RRBs, LABs, UCBs, StCBs/CCBs, AIFIs (NABARD, NHB, EXIM, SIDBI, NaBFID), SFBs, NBFCs incl. HFCs. **RRBs, LABs and co-operative banks may only transfer stressed loans** (proviso).
- **Permitted transferees:** SCBs, AIFIs, SFBs, NBFCs incl. HFCs (para 12(8)).
- Transferee must not be IBC s.29A-disqualified. For fraud borrowers, it must not be in the promoter group or its related parties. **The transferor verifies this** (para 12(14), Expl. III).
- **Loan participation:** the transferor stays lender of record; the transferee's exposure is to the underlying borrower; capital and provisioning follow each party's economic interest (para 12(5)).
- Stressed loan = NPA or SMA (para 12(11)). NBV = funded outstanding less specific provisions (para 12(7)). A portfolio agreement lists each loan (para 12(10)).

*Build:* counterparty master with lender-type, permitted-transferee and ARC flags. s.29A and promoter-group declarations are a pre-approval gate.

**General conditions, all transfers (paras 13–30):**

- Board policy covers due diligence, valuation, IT systems for data, risk management and Board oversight. **The transfer/acquisition unit is independent of origination** (para 13).
- No change to loan terms on transfer. Any change is tested against restructuring (paras 14, 23).
- **No credit enhancement or liquidity facility by any lender** (para 16). Retained interest is never credit enhancement; the agreement sets the principal/interest split (para 18).
- **No re-acquisition of a previously transferred loan, except under a resolution plan (RSA Directions or IBC)** (para 17). No obligation to re-acquire, substitute or fund, except for breach of reps and warranties; the transferee acknowledges this in writing (para 20).
- The transferee may freely on-transfer and has no recourse. Neither party needs the other's consent to resolve or recover its own share (para 19).
- Obligor consents (para 22). **Notify RBI DoS of every loan replacement or damages paid for reps and warranties** (para 24). The transferee checks MHP (para 25). Outsourcing and KYC Directions apply (para 26).
- **Non-compliant transfer:** the transferee holds capital equal to the exposure. **The transferor keeps the loan on its books in full and books the consideration as an advance** (para 27).
- Fraud accounts may be transferred under Board policy, subject to para 78 (para 28). Also apply FRM para 54.
- **Transferor as servicer (para 30):**
  - written agreement, at arm's length;
  - no fee deferral or waiver;
  - limited duration, and the transferee may replace the servicer;
  - remits only after collection;
  - **holds collections in trust with no commingling**.
  - If any condition fails, the transferor holds capital as if the loans were on its books.

**Loans not in default (Ch III, paras 31–52):**

- Excludes whole-business-exit portfolio sales, stressed loans and RBI-exempted transactions (para 31). Ch II still applies (para 32).
- **No loan in default may be transferred**, and the gap between the due-diligence cut-off and transfer must be minimal (para 33). Default = any due amount unpaid (para 12(2)).
- Single loan, part of a loan, or portfolio, by assignment, novation or participation (para 34). A change of lender of record needs a borrower-consent clause (para 35).
- Retained interest is documented, with a legal opinion on the para 36 points (para 36). Same underwriting for transferred and retained loans (para 37).
- **Cash only; consideration received no later than transfer; arm's-length price** (para 38).
- **Transferee due diligence** is done by its own staff, not outsourced, at loan level (para 39).
  - If loan-level due diligence covers **≥ one-third of the portfolio by value and number**, the rest may be portfolio-level. **The transferor then retains ≥ 10% of the entire transfer** (para 40, Expl. 1).
- Ongoing monitoring, stress tests, certified servicer data and audit rights (paras 41–42).
- **MHP (para 43)**, counted from CERSAI registration:
  - **3 months** for tenor ≤ 2 years; **6 months** for tenor > 2 years;
  - unsecured or not CERSAI-registrable: from **first repayment**;
  - project loans: from **COD**;
  - loans the transferor itself acquired: **6 months from booking**;
  - factoring receivables are exempt if residual maturity is **≤ 90 days** and the drawee is appraised.
  - Not applicable to an arranger's syndication sell-down (para 44).
- **Accounting and capital:**
  - realised profit or loss goes to P&L; **unrealised profit is deducted from CET1/NOF until maturity** (para 45);
  - borrower-wise accounts; IRACP and exposure norms per obligor (paras 46, 49–50);
  - capital as for originated loans (para 47);
  - any external rating comes only after own due diligence (para 48);
  - acquired loans carried at cost; premium over outstanding principal amortised by SLM or EIR, and not deducted from capital (para 51).
- **Reps and warranties (para 52):**
  - written, about existing verifiable facts, not open-ended;
  - **replacement within 30 days** on the original terms, reclassified as if never transferred;
  - damages only with the onus on the claimant, a written Notice of Claim, and direct losses only.

**Stressed loans (Ch IV, paras 53–77):**

- **Assignment or novation only; no participation** (para 54).
- Board policy covers norms, valuation, delegation, objectives and risk premium (para 55). Identification is top-down. **The Board or a committee periodically reviews NPAs above a threshold, with documented rationale** (para 56).
- **Valuation (para 57):** discount rate floor = contracted rate. **Two external valuations where the exposure (gross of provisions) is ≥ ₹100 crore.** The transferor bears the cost.
- Sales go only to permitted transferees and ARCs (para 58). E-auctions are permitted (para 59).
- **Swiss challenge is mandatory after bilateral negotiation** where aggregate lender exposure to the borrower (incl. investments) is **≥ ₹100 crore**. It is also mandatory for any ICA-approved exit (**75% by value, 60% by number**), regardless of size (para 60).
- The transferor keeps no residual risk. **Cooling period ≥ 12 months before fresh exposure to the borrower** (para 61).
- **Resolution-plan exit of all lenders** (para 62) widens the transferee classes, incl. Companies Act companies. For a transferee that is neither an ARC nor a permitted transferee (para 62(3)):
  - incorporated in India or registered with an Indian financial-sector regulator;
  - not NPA, and not funded by lenders;
  - **3-year bar** on lender exposure to the borrower (except working capital from non-transferors), and to the transferee for the borrower's operations.
- Adequate due-diligence time (para 63). The transferee signs the ICA (para 64). **No contingent price** (para 65).
- **Cash only to non-ARCs; derecognise only on receipt of the full consideration** (para 66).
- An acquired pool is a single asset only for homogeneous personal loans (para 67). The transferee, if a credit institution, reports to CICs (para 68).
- **Transferee classification:** no existing exposure → "Standard", then by recovery against the cash flows estimated at acquisition (para 69). Existing exposure → the borrower's existing class, incl. after IBC acquisition (para 70).
- **Provisioning (para 71):**
  - provision per asset class;
  - plus the shortfall where the NPV of estimated cash flows is below the consideration;
  - discount rate = contract rate + Board risk premium, **floor 3%**;
  - Ind AS NBFCs compute this alongside Ind AS for the prudential floor.
- **Hold acquired stressed loans ≥ 6 months before transfer.** No acquisition of loans that another lender transferred as stressed within 6 months. ARC and ICA-resolution transfers are exempt (para 74).
- **NPAs:**
  - staff accountability continues (para 75);
  - collections amortise the acquisition cost first (para 76);
  - **100% risk weight while classified standard** (para 77).

**ARCs (paras 78–88):**

- Any stressed loan in default may go to an ARC. Fraud accounts qualify only if reporting, monitoring and complaint responsibilities pass to the ARC (para 78).
- Surplus sharing is permitted; profit is booked only when realised (para 79).
- **Price < NBV:** shortfall to P&L in the year of transfer; countercyclical or floating provisions may be used (para 80).
- **Price > NBV:** reverse the excess provision only as cash received (incl. SR/PTC redemptions) exceeds NBV (para 81).
  - Full reversal is allowed where the consideration is cash plus GoI-guaranteed SRs. The non-cash part is deducted from CET1/NOF and is not distributable (para 81(1)).
- **SR valuation:**
  - NAV based on recovery ratings; the transferor carries its SRs at the lower of that value and NBV (para 82);
  - if the transferor holds **> 10%** of the SRs, also cap at face value less the notional provision (para 83);
  - GoI-guaranteed SRs: valued at NAV, unrealised gains deducted, **₹1 after the guarantee ends** (para 84);
  - **SRs unredeemed at the end of the 5/8-year resolution period are loss, fully provided** (para 85);
  - non-SLR norms apply (para 86).
- Standard accounts may be taken over from ARCs after the monitoring period, under Board policy. **Never re-acquire your own transferred exposures** (para 87). With an ARC as recovery agent, the loan stays on the books (para 88).

**Swiss challenge (paras 89–92):**

- Board policy. **Minimum mark-up 5%–15% of the base bid**; for an ICA exit, set by the 75%/60% vote (paras 89–90).
- Maintain an authenticated list of loans for sale (para 91).
- Sequence: base bid → public counter-bids → challenger bid → the base bidder may match (para 92(1)–(4)).
- **If the winning bid is declined: immediate provision at the higher of the challenger-bid discount and the IRACP provision** (para 92(5)).

**Disclosure and reporting:**

- Disclosures follow the FS Directions (para 93).
- **Report every transfer to an RBI-notified trade reporting platform. Until the platform is notified, keep a loan-transfer database with transaction MIS** (para 94).

### Part B — Co-lending arrangements (CLA)

**Scope (paras 95–101):**

- Partners: SCBs (excluding SFBs, LABs, RRBs), AIFIs, NBFCs incl. HFCs (para 97).
- Digital co-lending must comply with both CF and Part B (para 98). Excludes multiple banking, consortium and syndication (para 99). No non-compliant CLA (para 100).
- CLA = ex-ante agreement to jointly fund a portfolio in a pre-agreed proportion, with revenue and risk sharing (para 101).
- CLAs entered into before the effective date stay under the earlier rules (paras 2, 96).

**Prudential and contractual (paras 102–107):**

- **Each NBFC in a CLA retains ≥ 10% of each individual loan** (para 102).
- Credit policy sets the CLA portfolio limit, target segments, partner due diligence and grievance handling (para 103).
- **The agreement covers:**
  - borrower criteria, products and areas;
  - lending-service fees and segregation of responsibilities;
  - **time-frame for exchanging critical information**;
  - customer interface and grievance redressal (para 104).
- The loan agreement names **the single point of customer interface. Any change only after prior intimation to the borrower** (para 105). CLA details go in the **KFS** (para 106).
- Unrealised profit is deducted from CET1/NOF until maturity (para 107).

**Pricing (paras 108–111):**

- **Blended rate = average of each RE's rate, weighted by funding share** (para 108). Any partner rate change updates the blended rate and is communicated to the borrower (para 109).
- Other fees go into APR and KFS (para 110).
- Lending-service fees follow objective criteria, with **no credit-enhancement or DLG element** (para 111).

**Operations (paras 112–121):**

- **The partner's commitment to book its share back-to-back is irrevocable** (para 112).
- **Both books show the shares within 15 calendar days of disbursement** (para 113).
- Transfer only to the partner named in the agreement and the KFS (para 114). If the 15 days are missed, the loan stays with the originator and is saleable only under Part A (para 115).
- **Separate borrower account per RE for its share** (para 116).
- **All disbursements and repayments, between REs and with the borrower, go through a bank escrow** (which may be one of the REs). Appropriation rules are in the agreement (para 117).
- CLA loans are in audit scope (para 118). **BCP to keep servicing until repayment if the CLA ends** (para 119).
- KYC: the partner may rely on the originator's CIP (para 120). FPC and grievance rules apply (para 121).

**CIC reporting, DLG, classification and onward transfer (paras 122–125):**

- Each NBFC reports **its own share** to CICs (para 122).
- **The originating NBFC may give DLG up to 5% of loans outstanding under the CLA**, governed mutatis mutandis by CF (para 123). DLG is defined in para 111, Expl. (2).
- **Borrower-level classification:** SMA/NPA at one RE applies to the other. Share it near-real time, **and by the end of the next working day at the latest** (para 124).
- Onward or inter-se transfers only under Part A, **with mutual consent** (para 125).

**Disclosure (paras 126–127):**

- **Website list of all active CLA partners** (para 126).
- Annual aggregate notes to accounts: quantum, weighted average rate, fees, sectors, performance, DLG (para 127).

*Build:* CLA engine with:

- NBFC share validator (≥ 10%);
- 15-day booking clock with fall-back to the originator and a Part A flag;
- escrow appropriation waterfall;
- dual borrower sub-accounts;
- blended-rate recomputation and borrower notice;
- classification sync with a next-working-day breach alert;
- DLG ledger in the originator role only, with a 5%-of-CLA-outstanding cap;
- website partner-list feed.

---

---

## 8A.23 SEC — Securitisation Transactions Directions (353)

**Applicability (para 3).** As TDCR: NBFC-D, ICC, Factor, MFI, IFC, IDF-NBFC and HFCs, all layers. Excludes MGC, P2P, AA, CIC, SPD, NOFHC and non-public-fund NBFCs. In force on issue (para 2).

**Structure:** Ch I paras 1–4; Ch II 5–34 general; Ch III 35–79 STC; Ch IV 80–96 facilities; Ch V 97–107 investors; Ch VI 108–115 capital and disclosure; Ch VII 116–119; Annex I disclosure format.

**Definitions (para 4):**

- Securitisation needs **≥ 2 tranches with different credit risk**. Single-asset pools and tranches of different maturity are allowed (4(19)).
- Also defined: synthetic securitisation (4(25)), re-securitisation (4(16)), clean-up call (4(2)), I/O strip (4(9)), first and second loss facilities (4(7), 4(18)), senior tranche (4(22)), SPE (4(23)).
- Lenders: SCBs (excl. RRBs), AIFIs (NABARD, NHB, EXIM, SIDBI), SFBs, NBFCs incl. HFCs (4(10)).

**Prohibited (para 5):**

- re-securitisation;
- structures that roll over CP-type instruments against long-term assets;
- **synthetic securitisation**;
- underlying assets that are revolving credit (cards, cash credit), restructured loans within the specified period, exposures to lending institutions, AIFI refinance, **bullet loans**, or loans with **residual maturity < 365 days**.
- **Exception:** agri bullet loans to individuals ≤ 24 months, and trade receivables ≤ 12 months, are eligible if the borrower or drawee fully repaid the last two (one for agri > 1 year) within 90 days of the due date. Investors must be able to verify this.

**Eligibility and MHP (paras 6–9):**

- Only on-balance-sheet **standard** loans (para 6).
- MHP as in TDCR para 43. For real-estate mortgages, it runs **from the later of full disbursement and CERSAI registration** (para 7).
- MHP applies loan by loan, and not to para 5 proviso loans (para 8). Obligor consents apply (para 9).

**MRR (paras 10–15):**

| Underlying loans | MRR (% of book value securitised) |
|---|---|
| Original maturity ≤ 24 months | **5%** (para 10(1)) |
| Original maturity > 24 months; para 5 proviso bullet loans | **10%** (para 10(2)) |
| RMBS, any maturity | **5%** (para 11) |

- **Form (para 12):**
  - first 5%: first loss facility, then equity tranche, then pari passu in the sold tranches;
  - above 5%: any combination;
  - overcollateralisation is not a first loss facility.
- I/O strips do not count (para 13).
- **No hedging, sale or encumbrance.** Held by the originator itself, not a group entity. **Form unchanged for life.** Maintained as a % of unamortised principal, and also at the end of any replenishment period (para 14). Documented (para 15).

**Structure conditions (paras 16–29):**

- Underwriting no weaker than for retained loans; disclose changes (paras 16–17).
- Payment priorities fixed. All waterfall triggers disclosed, with breach status in investor reports. Early-amortisation triggers for replenishment structures (paras 18–21).
- **Material change in risk profile: notify investors, CRAs and service providers within 14 calendar days** (para 22).
- **Originator's total retained exposure ≤ 20% of the scheme's securitisation exposures.** Excludes credit-enhancing I/O strips and IRS/CCS with the SPE. A breach caused by amortisation does not count (paras 23–25).
- **Minimum ticket ₹1 crore per investor** (para 26). **Listing required if offered to ≥ 50 persons** (SEBI SDI Regulations, 2008) (para 27).
- **SPE (para 28):**
  - arm's length; no name resemblance to the originator;
  - **no share capital or beneficial interest held by the originator**;
  - at most 1 non-veto board seat, where the board has ≥ 4 members and an independent majority;
  - trust: the originator does not settle or control it; bankruptcy-remote; non-discretionary trustee; investors may change the trustee;
  - no loss support or recurring expenses from the originator;
  - investors are told the notes are not insured and are not deposits.
  - Also applies to the lender the loans were bought from (para 29).

**Reps and warranties (para 30):**

- Capital is required unless they are written, backed by due diligence, about existing verifiable facts, and not open-ended.
- **Replacement within 120 days** on the original terms. Damages only on the stated conditions.
- **Notify RBI DoS of every replacement or damages payment.**

**Accounting (paras 31–34):**

- **Cash sale; consideration no later than transfer; ≤ 30 days between asset transfer and note issuance** (para 31).
- Ind AS NBFCs follow Ind AS and ICAI advisories (para 32).
- **Others (paras 33–34):**
  - realised P&L in the period of sale;
  - unrealised gains (incl. future margin income) are held in **"Unrealised Gain on Loan Transfer Transactions"** and recognised only on cash redemption;
  - a credit-enhancing I/O strip balance acts as a provision;
  - write-off mechanics for amortising and non-amortising CE I/O strips.

**STC (Ch III, paras 35–79).** Optional label; it unlocks the alternative capital treatment in the Capital Adequacy Directions (para 35).

- Homogeneous assets, periodic payment streams, external benchmark rates (paras 36–37).
- **Performance history ≥ 7 years (non-retail) / ≥ 5 years (retail)** (para 40).
- No defaulted, delinquent, monitoring-period, high-risk-score or disputed claims. **Assess no earlier than 45 days before the securitisation takes effect** (paras 41–44).
- No discretionary selection (paras 47–48). True sale backed by an independent legal opinion (para 49).
- Loan-level or stratified data before pricing and **at least quarterly** (paras 51–52). Independent third-party review of the pool (para 53).
- Genuine hedging only (para 55). **Sequential amortisation after a trigger or default** (para 57). Liability cash-flow model (para 58).
- Replacement of servicers and counterparties (para 70). Itemised investor reporting (para 71).
- **Risk-weight caps at cut-off:** 40% value-weighted (residential); 50% (CRE mortgage); 75% (retail); 100% (other) (para 72).
- **Single obligor ≤ 1% of the pool**, or 2% if the originator retains subordinated tranches covering the first 10% of losses (para 73).
- The investor self-assesses. The originator decides for retained positions where significant credit risk transfer (SRT) is achieved. Compliance is checked continuously, and dynamically on additions. RBI may deny the treatment or apply Pillar 2 (paras 74–79).

**Facilities (Ch IV, paras 80–96):**

- Providers must be regulated by a financial-sector regulator (para 80).
- **Common conditions (para 81):** separate written agreement disclosed in the offer document; arm's length; fee not subordinated or deferred; capped amount and term; no recourse or recurring expenses; legal opinion; the provider can be replaced.
- **Credit enhancement (para 83):** only at initiation; available for the life of the notes; **drawdowns written off to P&L immediately**. Otherwise, capital = full securitised value.
- **CE reset (paras 84–88):**
  - external CE only;
  - re-rated by the original CRA, with no downgrade;
  - investor consent;
  - delinquency triggers;
  - no reset of the equity tranche;
  - **non-RMBS: first reset after ≥ 50% amortisation, then at 60/70/80%; RMBS: after 25%, then every 10%;**
  - **≥ 6 months between resets;**
  - **floor 30% (non-RMBS) / 20% (RMBS) of the initial CE;**
  - **release ≤ 60% of the excess;**
  - never below MRR.
- **Liquidity facility (paras 89–91):**
  - drawable only against non-defaulted assets;
  - not for CE, losses, permanent funding, expenses, buying assets, final repayment or warranty breaches;
  - provided to the SPE only;
  - **ranks senior to the senior tranche**;
  - otherwise treated as CE;
  - **drawn > 90 days = NPA, fully provided**.
- **Underwriting (paras 92–94):**
  - the originator may underwrite only **investment-grade senior notes**;
  - devolved notes sit outside the 20% cap if **sold within 3 months**, with on-book capital in the meantime.
- **Servicing (paras 95–96):**
  - no loss support beyond its own default, negligence or fraud;
  - remit only after collection;
  - **trust, with no commingling**;
  - remit all collections.
  - Otherwise treated as a liquidity facility.

**Investor NBFC (Ch V, paras 97–107):**

- **Invest only on the originator's explicit disclosure of MHP, ongoing MRR and KYC compliance** (paras 97–98).
- Pool and structure analysis; originator track record (paras 99–102).
- Own stress tests, with extra capital where needed (para 103). Board valuation policy (para 104).
- Counterparty = the underlying obligors (para 105).
- Monitoring of 30/60/90 DPD, defaults, prepayments, LTV, scores and geography, using Annex I (paras 106–107).

**Capital and disclosure (Ch VI, paras 108–115):**

- Capital on all securitisation exposures per the Capital Adequacy Directions (para 108) [VERIFY: Capital Adequacy Directions not yet supplied].
- Third-party servicer data **certified by auditors, preferably at least annually** (para 109).
- Disclose the weighted average holding period and MRR level (para 110). Loan-level data access for investors (para 111).
- **Public MHP/MRR disclosure at origination, confirmed half-yearly (September and March) and on any breach, per transaction, in servicer, investor or trustee reports, in Annex I format** (paras 112–113).
- Notes to accounts per FS (para 114). **Quarterly securitisation report to RBI; format to be advised** (para 115).

*Build:* Annex I generator per transaction:

- maturity profile, MHP, MRR (required, actual, form, breaches);
- overdue buckets, security cover, rating distribution;
- 5-year default and recovery rates;
- LTV and DTI bands, prepayment, industry and state mix.

---

## 8A.24 CAP — Prudential Norms on Capital Adequacy Directions (345)

*RBI/DOR/2025-26/345; 28 Nov 2025, updated as on 1 Apr 2026. NBFC-D, ICC, Factor, IFC, IDF-NBFC, MFI by layer (para 3(1)); NBFC-MFI exempt from 6(1), 6(2), 17. HFC: only 6(4), 7, 8, 11, 15, 16, 18(2)(iv), 18(3)–(11), 19–54 (3(2)) — HFC on-balance-sheet RWs and CRAR minimum come from the HFC Directions. MGC: 6(4), 7, 8, 11, 15, 16, 54. CIC: 15, 16, 54. SPD: 16, 54. Not P2P, AA, NOFHC, NBFC without public funds and customer interface, or BL with customer interface but no public funds (3(6)).*

**Structure:** Ch I paras 1–5; Ch II capital 6–17; Ch III RWAs 18 and securitisation 19–51; Ch IV CDS 52–53; Ch V ICAAP 54; Ch VI 55–58. Para 9(iii) inserted 10 Mar 2026; Sr (2)(e) amended w.e.f. 1 Apr 2026 (Amendment of 1 Jan 2026).

**Minimums, maintained on an ongoing basis (para 6):**

- **Gold-primary NBFC** (gold loans ≥ 50% of financial assets, 4(8)), any layer: **Tier 1 ≥ 12%, CRAR ≥ 15%**; Tier 2 ≤ 100% of Tier 1 (6(1)).
- **ML and above:** **Tier 1 ≥ 10%** (6(2)); **CRAR ≥ 15%**; Tier 2 ≤ 100% of Tier 1 (6(3)).
- **UL:** additionally **CET1 ≥ 9%** (6(4)).
- **TL:** higher charge as communicated by RBI (6(5)).
- **BL (not gold-primary):** no CRAR in this text; **leverage ≤ 7 at all times** (17). Leverage = total outside liabilities ÷ owned fund (4(7)).
- **NBFC-MFI:** a BL MFI's minimum comes from the MFI Directions [VERIFY: not supplied].
- **No capital conservation buffer, no countercyclical buffer and no Pillar 1 operational- or market-risk charge** in this text. Pillar 1 covers credit risk only, including counterparty credit risk on derivatives.

**Owned fund (para 9):**

- Components: paid-up equity, CCPS, free reserves (including quarterly profits), share premium, capital reserves from asset sale proceeds (excluding revaluation reserves).
- Deductions: accumulated losses, intangibles, deferred revenue expenditure. ROU assets on tangible leases are not deducted.
- **Quarterly profits (9(iii), from 10 Mar 2026):** only after quarterly limited review or audit; **EPt = NPt − 0.25 × D × t** (D = average dividend for the last 3 FYs; t = 1–4). Current-year losses deducted in full.

**CET1 (UL; paras 7–8):**

- Components: equity, share premium, capital reserves from sale proceeds, statutory reserves, other free reserves, retained earnings. Revaluation reserves may count as CET1 at a **55% discount** if conditions (a)–(g) are met, including two independent valuers every 3 years (7(v)). Current-year profit uses the same EPt formula (7(viii)).
- **Deductions (para 8):**
  - goodwill and intangibles (net of associated DTL), current and brought-forward losses;
  - DTAs on losses in full, and other DTAs net of DTL (excess DTL not added back);
  - **investments in other NBFCs' shares plus group exposures (shares, debentures, loans, HP/lease, deposits incl. margin money) above 10% of owned fund**, at the lower of cost and fair value;
  - defined-benefit pension assets; treasury stock.
- The Impairment Reserve is not recognised (8(4)).

**Tier 1:**

- **BL gold-primary and ML (10):** owned fund less NBFC-share and group exposures above 10% of owned fund, plus PDI up to **15% of Tier 1 as on the previous 31 March**. **A BL NBFC may not include PDI.**
- **UL (11):** CET1 + CCPS + PDI (same 15% cap).

**PDI terms (para 12):**

- INR only; minimum **₹5 lakh** per investor per tranche; perpetual.
- Call option only after **10 years**, with prior RBI approval. One step-up of at most **100 bps**, after 10 years.
- **Interest lock-in** when CRAR is below the minimum or the payment would take it below (12(8)); each invocation notified to the DoS RO.
- No advances against own PDI (12(14)). FII investment needs RBI approval.
- Report to the DoS RO with the offer document soon after issue (12(12)). Annual-report disclosures (12(15)).

**Tier 2 (para 13):**

- Preference shares that are not compulsorily convertible.
- Revaluation reserves at a 55% discount.
- General provisions and loss reserves up to **1.25% of RWAs**.
- Hybrid debt.
- Subordinated debt, discounted by remaining maturity (≤ 1 year 100%; 1–2 years 80%; 2–3 years 60%; 3–4 years 40%; 4–5 years 20%), capped at **50% of Tier 1**.
- PDI above the Tier 1 cap. **A BL NBFC may not include PDI in Tier 2.**

**DTA/DTL (para 14):** DTA treated as an intangible and deducted from Tier 1 (14(1)–(3)); DTL balance excluded from both tiers (14(5)).

**Other deductions (para 15):**

- Subordinated AIF units: whole investment deducted, proportionately from Tier 1 and Tier 2 (15(1)).
- Unrealised co-lending profit deducted from CET1/NOF until loan maturity (15(2)).
- **Full outstanding DLG deducted from capital** (15(3)).

**Ind AS filters (para 16):**

- Net unrealised fair-value gains excluded from owned fund and CET1; losses counted. Two netting buckets — (i) NBFC/group investments, (ii) others — with no cross-offset, net of tax (16(1)).
- Bucket (ii) gains excluded from capital are also deducted from RWAs (16(2)).
- Own-credit and cash-flow-hedge reserves derecognised (16(3)); hedge offset allowed (16(4)).
- Deemed-cost PPE gains count as Tier 2 at a 55% discount (16(5)).
- **Stage 1 (12-month) ECL counts as Tier 2 within the 1.25% cap; lifetime ECL is excluded from capital and deducted from RWAs** (16(6)).
- Securitised assets not derecognised because of originator credit enhancement: **0% RW**; the CE is deducted 50% from Tier 1 and 50% from Tier 2 (16(7)).
- Impairment Reserve not reckoned (16(8)).

**On-balance-sheet risk weights (18(1)).** Load as a versioned `rw_class` master.

| Sr | Item | RW % |
|---|---|---|
| (1) | Cash and bank balances, including FDs/CDs with banks | 0 |
| (2)(a) | Approved securities | 0 |
| (2)(b) | Bonds of public sector banks | 20 |
| (2)(c) | FDs/CDs/bonds of public FIs | 100 |
| (2)(d) | Shares, debentures, bonds and CP of all companies; MF units | 100 |
| (2)(e)(i) | High-quality infrastructure project loans (CON definition), ≥ 2% of sanctioned project debt repaid | 75 |
| (2)(e)(ii) | The same, ≥ 5% repaid | 50 |
| (3)(a) | Stock on hire (net book value) | 100 |
| (3)(b) | Inter-corporate loans and deposits | 100 |
| (3)(c) | Loans fully secured against deposits held | 0 |
| (3)(d) | Loans to staff | 0 |
| (3)(e) | Other secured loans and advances considered good | 100 |
| (3)(e)(i) | Retail consumer credit, excluding housing, education, vehicle, gold-jewellery and microfinance/SHG loans | **125** |
| (3)(e)(ii) | Credit card receivables | **125** |
| (3)(f) | Bills purchased or discounted | 100 |
| (3)(g) | Others | 100 |
| (4)(a)–(c) | Leased assets (net book value), premises, furniture | 100 |
| (5)(a)–(c) | TDS and advance tax (net of provision); interest due on G-secs | 0 |
| (5)(d) | Other assets, including ROU assets | 100 |
| (6)(a)–(c) | Central Government claims; State Government securities and loans; Central Government-guaranteed claims | 0 |
| (6)(d) | State Government-guaranteed, not in default or in default ≤ 90 days | 20 |
| (6)(e) | State Government-guaranteed, in default > 90 days | 100 |

- **Infrastructure 75% / 50% (from 1 Apr 2026):** threshold measured on sanctioned project debt, including takeover debt; a project that stops qualifying reverts to Sr (3)(e) or (g); an exposure with a lower RW under the rules up to 31 Mar 2026 keeps it until the next review or renewal, or **31 Mar 2027**, whichever is earlier.
- **No separate weights** exist for gold, NBFC housing, vehicle, education, MFI, LAP, MSME, CRE or loans to NBFCs: all take **100%**, unless the 125% consumer-credit row applies (gold, housing, vehicle, education and MFI are expressly excluded from it). "Consumer credit" is not defined in this text; classify per product at sanction [VERIFY: tenant policy for LAP/LAS to individuals].
- **Exposure adjustments (18(2)):** net only where a provision or depreciation is held; items deducted from owned fund take 0%; net off cash margin, caution money and security deposits held with a right of set-off.
- **Credit guarantee schemes (18(2)(iv)):** CGTMSE, CRGFTLIH and NCGTC cover takes **0% up to the maximum permissible claim** (coverage, first loss, payout cap); residual at the counterparty RW. Portfolio guarantees: first-loss portion fully deducted from capital, total charge capped at the unguaranteed charge. Future schemes must settle within 30 days and allow lodgement within 60 days. Load scheme rules (CGFSF, CGFSD, CGFMU, CGTMSE micro) as configuration; apply only where the tenant is an eligible MLI.

**Off-balance-sheet items (18(3)–(6)):**

- Credit equivalent = notional × CCF (or CEM for derivatives). RW: 0% Government, 20% banks, 100% others. Cash margins deducted before the CCF. Undrawn amount = the maximum unused portion drawable over the remaining maturity.

| Sr | Instrument | CCF % |
|---|---|---|
| 1 | Financial and other guarantees | 100 |
| 2 | Share/debenture underwriting | 50 |
| 3, 4, 5 | Partly paid shares; bills discounted/rediscounted; lease contracts entered but not executed | 100 |
| 6, 7, 8 | Repo or asset sales with recourse; forward asset purchases; lending or posting of securities | 100 |
| 9 | Other commitments (standby facilities, credit lines): original maturity ≤ 1 year / > 1 year | **20 / 50** |
| 10 | Commitments unconditionally cancellable without notice | **0** |
| 11 | Take-out finance: unconditional / conditional | 100 / 50 |
| 12, 13 | Securitisation liquidity facility; third-party second-loss credit enhancement | 100 |
| 14 | Other contingent liabilities | 50 |

- **PCE (18(6)):** drawn = advance; undrawn = contingent; capital at least at the issuance level while the bond outstanding exceeds the aggregate PCE; full capital if the pre-enhanced rating falls below BBB−; capped at the PCE amount.
- **Derivatives — CEM (18(7)–(9)):** exposure = positive MTM + PFE; add-ons interest rate 0.5 / 1.0 / 3.0%, FX and gold 2 / 10 / 15% (≤ 1 year / 1–5 years / > 5 years); netting ANet = 0.4·AGross + 0.6·NGR·AGross, only with legal opinions and no walkaway clause; QCCP exposures 0; collateral posted with CCIL 20%, other CCPs 50%.
- **Repo and CDS:** repo in corporate debt (18(10)); CDS on bonds — 80% recognised for non-HTM, full substitution for HTM (18(11)).
- *Build:* sanctioned-but-undisbursed amounts (tranches, lines) go to Sr 9 or 10 using the original maturity and an `unconditionally_cancellable` flag from the sanction terms.

**Securitisation (paras 19–51):**

- Capital on every securitisation exposure; gain on sale deducted from CET1/NOF until maturity (19).
- Derecognition requires the para 27 conditions, including a clean-up call ≤ 10%, plus a legal opinion (28).
- **SEC-ERBA only; for an unrated exposure, capital = the exposure amount** (29). Capital capped at the exposure (30) and, for an originator, at the pre-securitisation charge (31). Implicit support → capital on the whole pool (32).
- Inputs: attachment/detachment points A and D, tranche maturity MT (floor 1, cap 5 years), thickness T (33–40, 45). RW tables short-term and long-term (42, 44); STC tables (49–50). Floors 15% (non-STC); 10% senior / 15% non-senior (STC) (47, 51).
- *Build:* golden test = the para 48 illustration (total RWA ₹790.315 crore).

**CDS (paras 52–53):**

- User only: buy protection on corporate bonds held; no selling, no short positions (52).
- Restructuring not covered → 60% of the hedge recognised (53(1)(v)(d)). Materiality threshold → **667% RW** (53(2)).
- Maturity mismatch: Pa = P × (t − 0.25) ÷ (T − 0.25); nothing recognised below 3 months (53(5)(iii)).
- Exposure above the single/group limit because of CDS cover → 667% (53(5)(iv)). **Quarterly report** to the DoS RO (53(7)).

**ICAAP (para 54; ML and above, plus HFC, MGC, CIC, SPD):** Board-approved, proportionate internal assessment of credit, market, operational and residual risks. Pillar 2 capital is not insisted upon.

**Reporting:** this text names no CRAR return format; the DNBS series comes from the Supervisory Returns Directions.

*Build:* the RWA engine (M12) works in seven steps:
1. **Exposure snapshot** from LMS, GL and investments, with rw_class, provisions, margins and guarantee cover.
2. **Off-balance-sheet** amounts from sanctions, guarantees and commitments, with CCFs.
3. **Securitisation and derivatives** modules.
4. **Capital numerator** from GL capital-component tags, including EPt (needs dividend history), ECL stages and deductions.
5. **Ratios** against thresholds from the entity profile.
6. **Lineage** to every loan and journal.
7. **What-if** impact of a proposed sanction.

---

---

## 8A.25 SBR — Registration, Exemptions and Framework for Scale Based Regulation Directions (339)

*RBI/DOR/2025-26/339; 28 Nov 2025; original text, no "updated as on" date. All registered NBFCs by layer (3(2)), including Government companies (3(3)); Ch IV for specified non-banking institutions (3(1)). The ₹1 lakh crore UL threshold and "Unregistered Type I NBFC" are **absent** from this copy [VERIFY: any 2026 amendment].*

**Layers (paras 8–16):**

- **BL:** non-deposit NBFCs with assets below ₹1,000 crore, plus P2P, AA, NOFHC and NBFCs with no public funds and no customer interface (10). Those four always stay BL (15(1)).
- **ML:** all NBFC-D; non-deposit NBFCs with assets ≥ ₹1,000 crore; SPD, IDF-NBFC, CIC, HFC, IFC (11). NBFC-D, CIC, IFC and HFC are never BL; SPD and IDF always ML (15(2)).
- **Any layer:** ICC, MFI, Factor, MGC (15(3)).
- **UL:** identified by RBI (12). **Government NBFCs are not placed in UL until further notice** (15(4)).
- **TL:** ideally empty; higher capital as communicated (13–14, 36).
- **Legacy terms:** NBFC-ND = BL; NBFC-D and NBFC-ND-SI = ML or UL; ND-SI with assets of ₹500–1,000 crore = BL (16).
- Rules cascade upward through the layers (32–35).

**Middle Layer classification (paras 17–23):**

- **Group consolidation:** total assets of every CoR-holding NBFC in the group or under common promoters, including always-BL entities and any unregistered CIC below ₹100 crore that has accessed public funds. If **≥ ₹1,000 crore**, every ICC, MFI, Factor and MGC in the group is ML (17–19).
- The statutory auditor certifies group asset size as on 31 March **every year**; certificate to DoS (20). The group rule is not used for UL (21).
- **ML rules apply from the date assets reach ₹1,000 crore, not the balance-sheet date** (22).
- After a temporary dip, the NBFC stays ML until its next audited balance sheet **and** a specific RBI dispensation (23).
- Definitions: public funds exclude instruments compulsorily convertible into equity within 5 years (6(18)); customer interface (6(4)); companies in the group (6(3)); IFC = ≥ 75% of total assets in infrastructure lending (6(13)).

**Upper Layer (paras 24–31):**

- **Scoring set:** top 50 by total exposure, excluding the **top 10 by asset size, which are always UL**; last year's UL; supervisory additions (24, 26). Annual, as on 31 March (25).
- Weights: quantitative 70 (size and leverage 35, interconnectedness 25, complexity 10); qualitative 30 (liabilities 10, group structure 10, segment penetration 10) (25).
- **Transition (27):** Board policy and implementation plan within **3 months** of RBI advice; full compliance within **24 months**; roadmap submitted to RBI.
- Stays UL for at least **5 years** (28), unless it scales down voluntarily under a Board policy (29). RBI warns NBFCs near the criteria (30).
- *Build:* UL status is an RBI-advised flag with an advice date, never computed. Milestones become calendar items.

**Registration and NOF (paras 37–48):**

- **PBC (38):** financial assets **> 50%** of total assets (net of intangibles) **and** income from financial assets **> 50%** of gross income, on the last audited balance sheet. Bank FDs excluded (MISC 21).
- **NOF:** ICC, MFI, Factor **₹10 crore** (39); P2P, AA, NBFC without public funds and customer interface **₹2 crore** (40); IFC and IDF **₹300 crore** (41).
- **Glide path (42):** ICC ₹2 crore → ₹5 crore by 31 Mar 2025 → **₹10 crore by 31 Mar 2027**; MFI ₹5 crore (NE ₹2 crore) → ₹7 crore (NE ₹5 crore) → ₹10 crore; Factor ₹5 → ₹7 → ₹10 crore. Failure → ineligible to hold CoR (43). Other entity types follow their own Directions (44).
- **NOF deductions:** exposures to subsidiaries, group companies and other NBFCs above 10% of paid-up equity plus free reserves (45); look-through for group investments via an AIF where ≥ 50% of its funds came from the NBFC (46).
- **FATF:** new investors from non-compliant jurisdictions together hold **< 20%** of voting power, including potential voting power (47); existing investments grandfathered (48).
- **Not in this Direction:** CoR application procedure and change-in-control/management approvals (Acquisition of Shareholding or Control Directions, para 5(3)) [VERIFY: not supplied].

**Exemptions (Ch IV, paras 49–67):** PPI issuers for PPI money (49–50); Section 8 microfinance companies — microfinance only, household obligations ≤ 50% of income, no deposits, assets below ₹100 crore (51); SCs/RCs, Nidhis, mutual benefit, chit funds, merchant bankers (52–56); MGCs, housing finance institutions (58–59); insurers, stock exchanges, brokers (60–62); AIF companies (64); unregistered CICs from s.45-IA (66); CICs from s.45-IA(1)(b) (67).

**Reporting:** as prescribed by DoS (68).

**The entity regulatory profile must hold:**

- **Category and status:** NBFC category (ICC, MFI, Factor, ICC registered under the FRA, IFC, IDF, HFC, CIC, SPD, P2P, AA, NOFHC, MGC); deposit-taking flag; Government-company flag.
- **Public funds and customer interface:** both flags, with evidence and an as-of date.
- **Assets:** monthly standalone assets; last-audited assets; date ₹1,000 crore was first crossed; any dispensation reference.
- **Group:** group ID; member NBFCs with CoR status and assets; unregistered CICs below ₹100 crore using public funds; consolidated assets; annual auditor certificate.
- **Layer:** layer and source (computed for BL/ML; RBI advice reference and date for UL/TL); UL transition milestones and 5-year floor date; any RBI-specified TL capital (CAP 6(5)).
- **NOF and PBC:** current NOF, requirement and glide-path milestone; PBC result per audited balance sheet.
- **Flags:** gold-primary (CAP 4(8)); Ind AS; FRA registration and commencement date.
- **Investors and ratings:** FATF-jurisdiction voting share; product ratings history.
- **Officers and offices:** directors, principal officers, auditors, addresses (MISC 6–7).

---

---

## 8A.26 DIV — Prudential Norms on Declaration of Dividends Directions (360)

*RBI/DOR/2025-26/360; DOR.ACC.REC.279/21.02.067/2025-26; 28 Nov 2025. All layers: NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, MGC, SPD, CIC, P2P, AA (3). Not NOFHC.*

**Definitions (para 4):** dividend includes interim; **payout ratio** = dividend payable in the year (including interim) ÷ net profit for that year per audited financial statements; **NNPA ratio** = NNPA ÷ net advances.

**Board (6–7):** considers RBI/NHB divergence findings, audit qualifications and long-term growth plans; ensures the ceilings are not exceeded.

**Eligibility (8, Table 1):**

- **Capital:** met the applicable capital requirement (CRAR, Tier 1, Tier 2, leverage, ANW as applicable) **in each of the last 3 FYs, including the dividend year** (since registration if younger).
- **SPD:** CRAR ≥ 20% in all four quarters.
- **NNPA < 6%** in each of the last 3 years, including the dividend year.
- s.45-IC reserve fund complied with (HFC: NHB Act s.29C); compliant with regulations; no explicit RBI/NHB restriction.

**Quantum (para 9):**

- Includes dividend on CCPS eligible for Tier 1 / owned fund.
- Exceptional or extraordinary profits, and any overstatement indicated by an audit qualification (including emphasis of matter), deducted from net profit.
- **Ceilings:** none for NBFCs without public funds and customer interface, or BL with customer interface but no public funds; CIC and SPD **60%**; **all others 50%**. No ad hoc dispensation.

**Fallback (para 11; not SPD):** an NBFC that fails Table 1 Sr (1) or (2) in an earlier year may pay up to **10%**, if it meets the capital requirement at FY close and **NNPA < 4%** at FY close.

**SPD (para 12):** CRAR below 15% in any quarter → no dividend; 15–20% → payout ≤ **33.3%**.

**Other:** reversed provisions and unrealised transfer profits follow the TDCR Directions (10).

**Reporting (13–15):** Annex I to the DoS RO **within a fortnight of declaration** (HFC to NHB); SPD Annex II with the Board resolution to IDMD; interim dividends included.

*Build:* eligibility checker (M10/M17) reading the 3-year history of CAP capital runs and IRACP NNPA ratios; adjusted-profit worksheet; Board pack blocked on failure, with the 10% fallback path; Annex I generator. Dividend history feeds D in the CAP EPt formula.

---

---

## 8A.27 MISC — Miscellaneous Directions (373)

*RBI/DOR/2025-26/373; DOR.FIN.REC.No.292/03-10-119/2025-26; 28 Nov 2025, updated as on 26 Feb 2026 (paras 13A–13B inserted). Ch II all layers; Ch III ML and above; Ch IV Factors and ICCs registered under the FRA; Ch V IDF-NBFCs (3(1)). HFC: 6–22, 24–27. MGC, P2P: 6, 7, 14, 15, 25, 26. SPD: 6, 7, 8, 14, 15, 25, 26. AA: 6, 7, 25, 26. CIC: 6, 7, 9–20, 25–27. Not NOFHC. Separate from the DoS Miscellaneous Supervisory Directions, 2026. Contains no provisions on nomination, display of information, director KYC or unclaimed deposits.*

**Intimations to RBI:**

- Change of registered/corporate office address, phone or fax: **within 1 month** to the DoS RO and DoR Central Office (6).
- Change of directors' names or residential addresses, principal officers, auditors, or specimen signatures of authorised signatories: **within 1 month** to the DoS RO (7).
- Rating upgrade or downgrade of any financial product (assets ≥ **₹100 crore**): **within 15 days** to the RO (20).
- *Build:* any change to these master fields opens a dated intimation task with its deadline (M1/M14).

**Auditors (8):** SCA/SA appointment per the 27 Apr 2021 guidelines; non-deposit NBFCs below ₹1,000 crore may keep their existing procedure.

**NCD private placement, maturity > 1 year (9–13):**

- Board resource-planning policy (10).
- Minimum subscription **₹20,000**; two categories (maximum < ₹1 crore; minimum ≥ ₹1 crore).
- Below ₹1 crore: **≤ 200 subscribers per FY, fully secured**. ₹1 crore and above: no subscriber limit; security optional; unsecured issues are not public deposits.
- Funds only for the NBFC's own balance sheet, not group entities. **No loans against own debentures** (11(1)–(6)).
- Tax-exempt bonds exempt (12); NCDs up to 1 year follow the FMRD CP/NCD Directions, 2024 (13). Paras 13A–13B (NUCFDC) not relevant to tenants.

**Account Aggregator (14–15):** FIPs and FIUs adopt the ReBIT specifications as updated.

**Partnerships (16–19):** no capital contribution to, or partnership in, a partnership firm, LLP or AOP; exit any existing one.

**PBC and bank FDs (21):** bank FDs are not financial assets, and FD interest is not income from financial assets; FDs only for idle funds or NOF parking before commencement.
- *Build:* the PBC test (SBR 38) excludes GL accounts tagged `bank_fd`. Feeds AUD 6(2).

**Payments (22–24):**

- Move to electronic payments; eliminate PDCs (22).
- **No fresh or additional PDCs/EMI cheques** alongside NACH mandates; CTS-2010 cheques only where NACH is unavailable (23; not applicable to HFCs).
- Cash disbursal per Income-tax Act ss.269SS and 269T (24).

**Virtual currencies (25–26):** do not cite the set-aside 2018 circular; apply KYC/AML/FEMA due diligence.

**Rounding (27):** **all transactions**, including interest on deposits and loans, rounded to the nearest rupee — 50 paise and above up, below 50 paise ignored. Customer cheques with paise are never rejected.

**Lockers (28):** fee-based; disclose that the activity is not regulated by RBI.

**Fake bank guarantees (29–31):** due caution.
- *Build:* confirm every BG with the issuing bank before acceptance.

**AD Category II (Ch III, 32–34):** non-deposit ICCs in ML and above; investment-grade rating; Board policies on risk and grievances; monthly monitoring; application to FED.

**Factoring (Ch IV, 35–54):**

- **Registration:** CoR under FRA s.3 (36). An existing ICC is eligible if it takes no deposits, has assets ≥ ₹1,000 crore, meets NOF and is compliant (37); otherwise it converts through PRAVAAH with CoR surrender (38–39). Commence **within 6 months** of the CoR (41).
- **PBC:** factoring assets ≥ 50% of total assets and factoring income ≥ 50% of gross income (42).
- **NPA:** overdue **> 90 days** (Factors ≥ ₹500 crore and FRA-registered ICCs) or **> 180 days** (Factors < ₹500 crore, moving to 90 days on the IRACP para 44 glide path), with or without recourse (44–45); booked on the entity of exposure (46).
- **Exposure:** on the assignor (with recourse) or the debtor (without recourse), except international factoring with import-factor cover (47).
- **Controls:** debtor appraisal; genuine trade invoices only; Board limit for without-recourse underwriting (48–51); share limits and factored-debt details with banks and NBFCs (52); FEMA authorisation for export/import factoring (53–54).

**IDF-NBFC (Ch V, 55–63):**

- Funding: rupee or dollar bonds ≥ 5 years; shorter bonds and CP ≤ 10% of borrowings; ECB ≥ 5 years, not from foreign branches of Indian banks (58–61).
- Sponsoring an IDF-MF: NOF ≥ ₹300 crore, CRAR ≥ 15%, NNPA < 3%, 5 years in existence, 3 years of profits, CRAR and NOF maintained after investment, application via PRAVAAH (62–63).

---

## 8A.28 GOV — Governance Directions (344)

**Applicability (paras 2–4):**

- Immediate effect.
- **BL: Ch III (paras 8–11). ML: Ch II–IV. UL: Ch II–V** (3(1)).
- Paras 7–43 apply, layer-wise, to ICC, Factor, MFI, IFC, IDF and **HFCs** (3(2)).
- Partial application:
  - CIC: 7–15, 18–39, 41–43 (3(3));
  - MGC: 7(2), 7(3), 8, 9, 16–18, 25–39, 41–43 (3(4));
  - SPD: 7–9, 12–18, 25–40 (3(5));
  - NBFC-AA: 8, 10–13, 17(1), 18, with 12, 13, 17(1) and 18 applying despite BL (3(6));
  - P2P: 8–13, with 12–13 applying despite BL (3(7)).
- Not NOFHCs (4).
- **Government-owned NBFCs:** paras 29–37 do not apply (3(1) proviso); a Nomination Committee replaces the NRC (18(1)(ii)).
- *Build:* applicability keys are layer, NBFC type, government-owned flag, listed flag and asset size (CRO).

**All NBFCs (Ch III):**

- At least one director with bank or NBFC experience (para 8).
- **RMC** at Board or executive level; evaluates overall risks including liquidity; reports to the Board (para 9).
- **Prior written RBI approval for a change in management that changes more than 30% of the directors, excluding independent directors.** Re-election on retirement by rotation is excluded (para 10).
  - Application via **PRAVAAH**, on letterhead, with Annex I for each proposed director (para 11).
  - Every change in directors or management is still informed to RBI (NHB for HFCs) (para 10 Explanation; no timeline in the text).
- *Build:* change-of-management calculator over non-independent directors against the last approved baseline (the look-back window is a tenant parameter; the text sets none). A director appointment cannot become effective until the approval is attached.

**Board-approved policies (ML/UL, para 7):**

- fit and proper (12);
- CCO role (25(2));
- compensation (29);
- periodic reviews to the Board (15).

Also required:

- a whistle-blower mechanism (38);
- internal corporate-governance guidelines **published on the website** (40);
- for UL, a disclosure policy (43).

*Build:* policy-registry entries with approval date and review due date.

**Fit and proper (paras 12–14; ML/UL):**

- A Board policy plus an internal process for continuing due diligence (12). RBI may examine any director (12 proviso).
- Annex II declaration from proposed and existing directors (13(1)).
- NRC (or Nomination Committee) scrutiny with a recorded decision (13(2)).
- **Annual declaration as on 31 March**; changes furnished forthwith (13(3)).
- **Deed of Covenants in Annex III** (13(4)).
- **Quarterly statement on change of directors, with an MD/CEO certificate that fit-and-proper criteria were followed, to the RBI DoS Regional Office (NHB for HFCs) within 15 days of quarter-end. The March statement is auditor-certified** (14).
- *Build:*
  - director master: DIN, PAN, relatives, interested entities, substantial interest > 10% (5(10)), other directorships with the entity's layer, and facilities availed;
  - Annex I, II and III e-forms with eSign;
  - NRC decision log;
  - 31 March declaration campaign;
  - deed tracker;
  - auto-generated quarterly statement;
  - Annex II items II(a)–(f) feed the CRM 13K related-party register;
  - director default checks against bureau and wilful-defaulter data.

**Committees (paras 16–18):**

- The Board delineates committee roles (16).
- **Audit Committee of at least 3 Board members**, with s.177 powers (17(1)).
- The ACB ensures an IS audit "at the periodicity in the Outsourcing Directions" (17(2)). This is a drafting slip: OUT sets no periodicity. Use CYB para 56 (at least annually).
- **NRC** under s.178 (18).
  - It oversees the compensation policy (30).
  - It may align pay with the RMC and ICAAP, and ensure fit-and-proper status and the absence of conflicts (31).
- No IT Strategy Committee or customer-service committee is prescribed here. The ITSC comes from CYB paras 15 and 71–72.

**CRO (paras 19–24; ML/UL with assets above ₹5,000 crore):**

- Senior and qualified (20).
- **Reporting:**
  - direct reporting to the MD&CEO or the RMCB (21(1));
  - if the CRO reports to the MD&CEO, the **RMC or Board meets the CRO without the MD&CEO at least quarterly** (21(2));
  - **no business reporting line and no business targets** (21(3));
  - **no dual hatting** (21(4)).
- **Tenure and removal (22):**
  - fixed tenure, with Board approval;
  - premature transfer or removal only with Board approval, **reported to the DoS Regional Office (NHB for HFCs)**;
  - a listed NBFC also reports any change to the stock exchanges.
- **The CRO vets every credit product, retail or wholesale, for inherent and control risks** (23).
- On credit proposals the CRO is an adviser only. If the CRO is a voting member of a sanction committee, all members are individually and severally liable (24).
- *Build:*
  - a "CRO vetting" step in the product-approval gate;
  - sanction-committee configuration with the CRO as adviser (no vote) or voter (vote recorded);
  - SoD: the CRO user cannot hold business or target roles;
  - a tracker for the quarterly closed session.

**CCO (para 25; ML/UL):** sufficiently senior; a Board policy sets the role. Detail is in CMP (8A.11).

**KMP and independent directors (paras 26–28):**

- A KMP holds no office in another ML/UL NBFC, except a directorship in a subsidiary. BL directorships are allowed (26).
- **An independent director sits on at most 3 ML/UL NBFC boards at a time**; BL boards are excluded (27).
- The Board ensures there is no conflict (28).
- *Build:* directorship-limit check driven by the layer of each other entity.

**Compensation (paras 29–37; not government-owned):**

- Policy covers fixed and variable pay principles and malus/clawback (29).
- Variable pay can be reduced to zero; deferral is set by the Board (35).
- Control-function staff get a higher fixed share (35(4)).
- No guaranteed bonus, except a joining bonus (36).
- The malus/clawback period covers at least the deferral and retention periods (37).
- *Build:* policy registry only.

**Other (paras 38–43):**

- Whistle-blower mechanism for directors and employees (38).
- Governance of subsidiaries (39).
- Corporate-governance guidelines on the website (40).
- **UL only:**
  - Board skill mix (41);
  - **report the premature exit of an independent director to supervisors** (42);
  - **listing within 3 years of UL identification**, with listed-company disclosures before listing (43).
- Repeal is by DOR.RRC.REC.302/33-01-010/2025-26 (44).

---

---

## 8A.29 OUT — Managing Risks in Outsourcing Directions (363)

**Title (para 1):** "Reserve Bank of India (Non-Banking Financial Companies – Managing Risks in Outsourcing) Directions, 2025". No "Management of Third-Party Dependencies" Direction exists; CF para 62(2) misnames it (errata).

**Commencement (para 2):**

- Immediate effect.
- **Existing IT outsourcing agreements comply at renewal or by 10 Apr 2026, whichever is earlier.** New IT agreements comply from the agreement date.
- *Both dates have passed: every Finbyx tenant contract must comply now.*

**Applicability (para 3):**

- Covers NBFC-D, ICC, Factor, MFI, IFC, IDF, **HFC**, SPD, CIC, P2P and AA. Not NOFHCs.
- **BL: all provisions except Ch IV and the IT-specific parts of Ch II. ML and above: all** (3(2)).
- MGC in ML or above: Ch IV and the IT parts of Ch II (3(3)).
- **BL IT outsourcing falls under CYB Ch III/IV** (CYB 60–64 for BL with assets of ₹500 crore or more).
- CYB 117 covers IT third parties outside this Direction.

**Scope of Ch III (financial services; paras 4, 14):**

- Covers *material* outsourcing (14) of (4(1)):
  - application processing (loan origination);
  - document processing;
  - marketing and research;
  - loan supervision;
  - data processing;
  - back office.
- Excludes IT services and non-financial services (4(2)).

**Scope of Ch IV (IT; paras 5, 58):**

- Covers *material* IT outsourcing (5(1)):
  - infrastructure;
  - network and security;
  - **ASP application development and maintenance**;
  - **data-centre services**;
  - **cloud computing**;
  - managed security;
  - payment-ecosystem IT.
- Excludes (5(2)):
  - **licensed or subscription software acquisition**, including vendor enhancements;
  - OEM maintenance;
  - SMS gateways;
  - VA/PT and IS audit;
  - BC services, payroll and statement printing;
  - off-the-shelf products.
- Not "service providers" under Ch IV (58(3)):
  - BCs;
  - PSOs;
  - co-branding fintechs (these fall under Ch III);
  - **data retrieval and verification fintechs, digital document execution, data entry and call centres**;
  - telecom providers;
  - independent auditors.
- **Material IT** = disruption would significantly impact operations, **or** unauthorised access, loss or theft could materially affect customers (58(2)).
- *Build:* materiality questionnaire per arrangement, covering 14(i)–(vi) and 58(2).

**Board and senior management (paras 9–13, 20–21, 62–64):**

- Outsourcing never diminishes the obligations of the NBFC, its Board or senior management (9, 17).
- **Board-approved policies:**
  - financial outsourcing policy (10, 20);
  - IT outsourcing policy (62), covering roles, selection, materiality, delegation, BCP/DR, monitoring and **exit strategies**.
- **The Board or RMC reviews the records of all material outsourcing half-yearly; delegation goes only to the RMC** (12(1)(vii), 36).
- **The ACB monitors internal audit of outsourced activities and the ageing of entries pending reconciliation with vendors** (12(2)).
- The Board ensures there is no conflict of interest and approves any ownership-bar exception (13(iv), 59).
- **The IT function (64):**
  - keeps a **central database of all IT outsourcing arrangements**, accessible to the Board, auditors and supervisors;
  - monitors SLAs;
  - documents KRIs and vendor risk classes.

**Prohibitions and conditions:**

- **Never outsourced** (15):
  - core management functions, including **internal audit**;
  - strategic and **compliance** functions;
  - **KYC-compliance decisions**;
  - **loan sanction (including retail)**;
  - **investment-portfolio management**.
- These functions may be outsourced within a group under paras 45–51. Internal auditors may be on contract.
- No prior RBI approval is needed; RBI may inspect (16).
- The NBFC is responsible for **DSAs/DMAs and recovery agents** and for customer confidentiality (17).
- **Ownership bar:**
  - a non-group provider may not be owned or controlled by a director or relative (18(vi));
  - **for IT, the bar extends to KMP, the arrangement approver and their relatives**, unless the Board grants an exception with disclosure (59).
- The NBFC remains responsible for CTR/STR on provider-performed activities (19).

**Risk and confidentiality:**

- Ten key risks (22).
- Need-to-know access (24, 69(i)).
- Security review and breach disclosure (25).
- No commingling of data (26).
- The provider can isolate the NBFC's data (27).
- **Immediate notice to RBI of any breach or leakage of customer data; the NBFC is liable to customers** (28, 69(iii)).
- **The provider reports cyber incidents to the NBFC without undue delay, so that RBI is notified within 6 hours of detection *by the service provider*** (61).
- In a multi-tenant architecture, clear separation and isolation of data suffice (70).
- Concentration risk across providers (67).

**Due diligence:**

- At selection and at renewal, on the heads in 30(i)–(viii) (29–30).
- Independent reviews (31); system compatibility (32).
- IT additions (71): technology and DR, conflicts, data segregation, regulatory capability, cyber risk assessment, data access and enforceability. Risk-based approach (72).
- Re-review:
  - **annually** for financial services (38);
  - risk-based for IT (80).

**Agreement:** written, vetted by counsel, and stating the legal relationship (33, 73).

**Para 34 clauses (all arrangements):**

| Clause | Requirement |
|---|---|
| 34(i) | Activity and service standards |
| 34(ii) | Access to books and records |
| 34(iii) | Continuous monitoring |
| 34(iv) | **Prior consent for subcontractors** |
| 34(v) | Confidentiality, and provider liability for breaches |
| 34(vi) | Contingency plans |
| 34(vii) | Audit rights and copies of audit reports |
| 34(viii) | RBI access to records |
| 34(ix) | RBI inspection of the provider |
| 34(x) | Termination clause and notice period |
| 34(xi) | Confidentiality survives termination |
| 34(xii) | Preservation of documents, including after termination |

**Para 74 clauses (IT; added to 34(i)–(vii)):**

| Clause | Requirement |
|---|---|
| 74(i) | Subcontractors' service standards and audit |
| 74(ii) | Access to data, logs, alerts and premises |
| 74(iii) | Material adverse events to be reported |
| 74(iv) | IT Act compliance |
| 74(v) | SLAs |
| 74(vi) | **India-only data storage, as applicable** |
| 74(vii) | Details of data captured, processed and stored |
| 74(viii) | Data the vendor may share |
| 74(ix) | Resolution, defaults, indemnities and remedies |
| 74(x) | Contingency testing |
| 74(xi) | Supply-chain information |
| 74(xii) | **RBI inspection of the provider and its subcontractors, and access to infrastructure and data** |
| 74(xiii) | Provider liable for its subcontractors |
| 74(xiv) | **Compliance with RBI directions** |
| 74(xv) | Orderly transfer to another provider |
| 74(xvi) | Cooperation in the NBFC's insolvency or resolution |
| 74(xvii) | "Essential personnel" on site during exigencies |
| 74(xviii) | Back-to-back arrangements with OEMs |
| 74(xix) | NDA |

**Further IT agreement terms:**

- safe removal or destruction of data;
- **no erasing or altering of data during the transition** (87);
- the provider cooperates fully with the incoming provider (88).

*Build:* clause checklist per arrangement, pass/fail by clause ID.

**Monitoring:**

- Management structure covering performance, uptime, SLAs and incident response (35, 75).
- **Central record of material financial outsourcing, updated promptly, reviewed half-yearly by the Board or RMC** (36).
- **Audits:**
  - regular audits of providers and subcontractors (37, 76);
  - **pooled audits** allowed (77);
  - global certifications may be relied on, by risk (79).
- Timely reconciliation (39).
- Unrestricted access for the NBFC, its auditors and RBI (81).
- **Inventory of IT services, including supply-chain entities, with a dependency map** (82).

**BCP and exit:**

- Provider BCP documented and tested, with joint tests (40).
- Alternatives or insourcing assessed (41).
- Provider able to isolate, return or destroy the NBFC's data (42).
- The NBFC's right to intervene (43).
- IT exit strategy covers scenarios, minimum periods and alternatives (84–86).
- **Termination publicity:** notice at the branch and on the website, and customers informed (44, 89).

**Group outsourcing (45–51, 90–92):**

- Board policy and SLAs (45, 90).
- Customers told which entity offers the product (46).
- Documented agreements, with a clause binding the provider to RBI directions (47).
- Cross-sell identification (49).
- No implied guarantee of group obligations (50).
- **Identical risk management and arm's length dealing** (51, 91–92).

**Offshore outsourcing (52–53, 93–94):**

- Only jurisdictions that uphold confidentiality (52, 93).
- Governing law specified.
- Records available even on the provider's liquidation.
- No access to the data by the foreign regulator.
- **Original records kept in India** (53).
- Audit and inspection rights (94).

**Outsourced SOC (95):**

- Asset ownership defined.
- The NBFC owns the rules, logs and metadata.
- Integrated with the NBFC's incident process.

**Cloud (para 97):**

- (i) cost and risk assessment;
- (ii) data lifecycle up to permanent erasure;
- (iii) multi-tenancy risk;
- (iv) shared-responsibility model;
- (v) cloud adoption policy;
- (vi) CSPs only in enforceable jurisdictions;
- (vii) architecture: container and release tooling, **encryption keys and HSMs under the NBFC's control**, no commingling, resilience;
- (viii) **IAM with RBAC, SoD and a role-conflict matrix, least privilege and MFA**;
- (ix) controls at least as strong as on-premises;
- (x) CSP security capability;
- (xi) **CSP logs integrated into the NBFC's SOC and retained**;
- (xii) patching;
- (xiii) threat intelligence;
- (xiv)–(xv) BCP and DR drills;
- (xvi) **exit: data return, portability, secure purge and independent assurance**;
- (xvii) audit and certification scope.

**Grievances (54–57, 98–99):**

- Customer rights against the NBFC are unaffected.
- Product literature states that service providers may be used (55).
- **Microfinance:** the loan agreement and the FPC carry a declaration that the NBFC is accountable for inappropriate behaviour by the provider's staff and will redress grievances in time (56).
- GRO contact details displayed, covering outsourced services (57(2)).
- Ombudsman after 30 days (57(4)). The text cites IOS 2021; use RB-IOS 2026 logic (M15).

**Recovery agents:** covered here only by para 17 (responsibility). Conduct rules stay in RBC.

---

---

## 8A.30 ORM — Operational Risk Management and Operational Resilience Guidance Note (DOR.ORG.REC.301)

**Status and applicability:**

- This is **guidance, not a Direction**: principle-based and proportionate, and its tools are "indicative" (paras 6–7). RBI instructions prevail where inconsistent (7).
- Some items are still worded as mandatory:
  - "shall" for the three lines (12), self-assessment (42(1)), the event dataset (42(2)) and metrics (42(5));
  - "must" for scenario analysis (42(6)) and group risks (72).
- **Applies to** (para 8):
  - commercial banks, including SFB, PB and LAB;
  - RRBs, UCBs and RCBs;
  - AIFIs, including NHB;
  - **NBFC-BL, ML and UL**.
- HFCs are not listed separately, but NHB is named as their supervisor (9(14)(iii)), so treat HFCs as covered [interpretation].
- NBFC-BL is a "smaller RE": the first and second lines may be combined, with separation of duties and an independent review (12(2)).
- Repeals the earlier guidance note (108).
- **17 principles under three pillars** (10).

**Definitions (para 9):**

- critical operations, including supporting assets: people, technology, information and facilities (9(2));
- incident (9(4));
- mapping (9(6));
- operational resilience (9(7));
- operational risk: includes legal risk; excludes strategic and reputational risk (9(8));
- impact tolerance (9(15)).

**Three lines of defence (paras 11–14):**

- **First line (12(1)):** identifies and assesses risks; sets controls; reports residual risk, loss events and tolerance breaches.
- **Second line (12(2)):** an independent OORF.
  - It challenges the first line with evidence, owns policy, monitors and trains.
  - In larger REs it reports independently of business units.
  - It includes compliance.
- **Third line (12(3)):** audit validation and verification.
- Every line has defined roles, resources and training (13).

**Governance (Principles 1–5; paras 15–40):**

- Board code of conduct, **attested by employees and publicly available** (16).
- Risk-aligned compensation (18); training (19).
- **Board-approved ORMF** with definitions of operational risk and operational loss (23).
- **ORMF documentation (24):**
  - governance and committees;
  - tools;
  - **appetite and tolerance thresholds**;
  - **control library**;
  - MIS;
  - **a common taxonomy** of event types, causes, materiality and business units, with flags for legal, conduct, model and ICT/cyber exposures and the credit/market boundary.
- **The Board approves:**
  - the ORMF (25);
  - the resilience approach (27);
  - the **operational-risk appetite and tolerance statement** (29–30);
  - the **criteria for critical operations, annually or on material change** (31);
  - **impact tolerances for each critical operation, at least annually or after a disruption** (32).
- **At least one impact-tolerance metric per critical operation (33):**
  - at minimum: time-based, quantity (data loss) and service-level metrics;
  - optional: customers affected, number of transactions affected and value affected.
- Issue tracking and escalation (35).
- A smaller RE may oversee operational risk through the Board RMC (39).

**Identification and assessment (Principle 6; paras 41–44):**

- **RCSA** (42(1)):
  - inherent risk, control effectiveness and residual risk;
  - quantitative and qualitative elements;
  - enough detail for an independent reviewer;
  - a **risk register**.
- **Operational-risk event dataset** of all material events (42(2)):
  - internal losses and **near misses**;
  - taxonomy-classified;
  - **occurrence, discovery and accounting dates**;
  - financial impact and root cause;
  - external data encouraged.
- Event management (42(3)).
- Control monitoring and testing (42(4)).
- **KRIs against thresholds** (42(5)).
- **Regular scenario analysis for each critical service against impact tolerance** (42(6)).
- Benchmarking (42(7)).
- OORF-monitored action plans (43(3)).
- Reassessment on change and after incidents (44).

**Change management (Principle 7; paras 45–50):**

- New products, processes and systems reviewed on the 47(i)–(vi) heads (47).
- Monitoring after implementation (48).
- **Central record of products and services, including third-party arrangements** (49).

**Monitoring, reporting and control (Principles 8–9; paras 51–65):**

- Reporting to the Board, senior management and business units, consistent with BCBS 239 and able to run under stress (51–53).
- Resilience reports to the Board (55).
- **Tracking of approved exceptions, overrides and deviations** (57).
- SoD and dual control (59).
- **Example controls (para 60 table):**
  - approval authorities;
  - limit monitoring;
  - safeguards over assets and records;
  - **regular reconciliation**;
  - **mandatory leave in sensitive positions: one spell a year, with an element of surprise**.
- Third-party concentration and downstream dependencies (63).
- **Annual review of the insurance and risk-transfer programme; the Board sets the maximum loss exposure** (64).

**Operational resilience (Principles 10–14; paras 66–94):**

- **Mapping (69–72):**
  - people, technology, processes, information, facilities, and third-party and intragroup dependencies for each critical operation (69);
  - identifies concentration, **single points of failure** and substitutability (71);
  - covers group risks (72).
- **Third parties (73–76):**
  - risk assessment and due diligence, **including resilience at least equivalent to the RE's** (73);
  - a Board-approved third-party policy with a **register of third-party relationships showing criticality**, metrics, contracts and supervisor access (74);
  - exit plans and substitutability in the BCP (75);
  - nth-party supply chain, **with the provider contractually liable for its subcontractors** (76).
- **BCP (77–83):**
  - regular Board review (77);
  - scenario-based BIA, maximum-tolerable-outage triggers, **RTO/RPO** and communication plans (78);
  - exercises that include third parties (79);
  - succession of authority and invocation triggers (80);
  - test results to senior management and the Board (82);
  - a pandemic plan (83).
- **Incidents (84–87):**
  - inventory of response resources (84);
  - **severity classification**, procedures and internal/external communication plans with metrics (85);
  - RCA (86);
  - lessons from near misses and third-party incidents (87).
- **ICT (90–94):**
  - an ICT policy (90);
  - Board oversight (91);
  - privileged-user management (93(ii));
  - **offline immutable backups of critical data** (94).

**Learn and adapt (Principles 15–17; paras 95–107):**

- Public disclosure of the ORMF and **significant operational loss events** (96), under a **Board-approved disclosure policy** (97).
- **Lessons-learned exercise with RCA after any disruption, including one at a third party** (99).
- **Minimum questions (101):**
  - how and why the incident happened;
  - the impact on critical operations;
  - speed and extent of recovery;
  - whether communication channels were followed;
  - whether impact tolerances were held;
  - whether controls, decisions and communications were appropriate and timely.
- **Post-incident report to the Board** (102).
- Feedback loop (104–107).

---

## 8A.31 MFI — Microfinance Institution Directions (371)

**Applicability (paras 3–5, 7–8).** Every NBFC-MFI, in addition to (not in substitution of) the Directions listed in para 4, by layer (para 5). Original text of 28 Nov 2025; no "updated as on" date.

- **NBFC-MFI** = a non-deposit-taking NBFC with **≥ 60% of total assets (netted off by intangible assets) deployed in "microfinance loans" on an ongoing basis** (para 8(3)).
- "Microfinance loan" has the CF meaning (para 8(2); CF para 51).
- An NBFC-MFI may sit in any SBR layer (para 7).
- **Para 49 binds every NBFC** (see below).

**Qualifying assets (para 12):**

- Qualifying assets = microfinance loans, **minimum 60%** of total assets net of intangibles, on an ongoing basis.
- **Four consecutive quarters** below 60%: the NBFC-MFI approaches RBI with a remediation plan.
- **There is no 75% test in this Direction.**
- Build: quarterly qualifying-asset test (M12) with a 4-quarter breach counter. Quarters 1–3 raise an M14 alert; quarter 4 opens a remediation-plan task. The result feeds the Workspace L evidence pack (AUD para 8, MFI classification).

**Non-MFI NBFCs (para 49):**

- Microfinance loans of all NBFCs are governed by CF, RBC and Outsourcing.
- **An NBFC that is not an NBFC-MFI may hold microfinance loans of at most 25% of its total assets, in aggregate.**
- Build: M12 limit plus an M4 pre-sanction gate on every loan the CF 51 classifier marks as microfinance.

**Channelising agent for Central/State Government schemes (para 13):**

- These loans are a **separate business segment**, excluded from **both** the numerator and the denominator of the 60% test (13(1)).
- Separate accounts and records, including funds received or receivable from the agency; shown as a separate segment in the financials (13(2)(i)).
- IRACP and prudential norms apply unless the MFI bears no credit risk (13(2)(ii)).
- **All such loans are reported to CICs** (13(2)(iii)).
- Build: `channelising_scheme` flag on product and loan; segment GL; "credit risk borne" flag driving IRACP; CIC reporting cannot be switched off.

**Board (para 10).** Board-approved internal exposure limits to avoid geographical concentration (10(1)). Build: state- and district-level limits in M12.

**Capital (paras 16–21):**

- **CRAR ≥ 15%** of aggregate RWA, made up of Tier 1 and Tier 2 (16).
- **Tier 2 ≤ 100% of Tier 1** at any time (17).
- The Capital Adequacy Directions govern:
  - on- and off-balance-sheet treatment;
  - DTA/DTL;
  - risk weights for CGTMSE/CRGFTLIH/NCGTC-guaranteed loans (18–20).
- The rest of the Capital Adequacy Directions applies, except paras 6(1), 6(2) and 17 (21).

**Asset classification and provisioning: the NBFC-MFI's microfinance loans (paras 22–28):**

- Standard asset as defined (23).
- **NPA: interest or principal overdue for more than 90 days** (24).
- **Aggregate provision floor, at any point of time, is the higher of (25(1)):**
  - (i) **1% of the outstanding loan portfolio**; or
  - (ii) **50% of instalments overdue > 90 and < 180 days, plus 100% of instalments overdue ≥ 180 days**.
- Build: compute (ii) on **overdue instalment amounts, not loan outstanding**, at portfolio level, at every COB and at period end. Any shortfall against the IRACP/ECL result is booked.
- CRGFTLIH-guaranteed NPAs: no provision on the guaranteed portion; the excess follows IRACP (26).
- Standard-asset provisioning follows IRACP for the MFI's layer (27). Other IRACP provisions apply where not contradictory (28).

**Other Directions applied (paras 4, 29–45).**

- The NBFC-MFI also follows:
  - Stressed Assets, INV, ALM, Dividends;
  - Acquisition (except 6(3)–(4)) and Governance;
  - CRM, Transfer of Credit Risk, CON, Outsourcing;
  - CF and Undertaking of Financial Services (paras 6–19, 23–33, 50–57);
  - Credit Cards, RBC, KYC, Securitisation, CIR, Wilful Defaulters;
  - Miscellaneous Directions Ch II–III, FS, and BR paras 10, 11, 13–15.
- Build: the applicability engine maps `type = MFI` to this list.
- **Pricing:** 371 sets no pricing, interest-cap or conduct rules of its own. Pricing stays under CF paras 60–61.

**SRO (para 46).** Membership of at least one RBI-recognised SRO for NBFC-MFIs, and compliance with its Code of Conduct. Build: `sro_membership` on the entity profile; the SRO Code of Conduct is loaded as an M14 obligation set.

**Not-for-profit microfinance companies (paras 14–15).** Those with assets ≥ ₹100 crore must register as NBFC-MFIs. No software impact.

---

---

## 8A.32 IAF — Internal Audit Function Directions (464)

**Applicability (para 3).** In scope:

- all deposit-taking NBFCs;
- **non-deposit-taking NBFCs with assets ≥ ₹5,000 crore**;
- all deposit-taking HFCs;
- non-deposit-taking HFCs with assets ≥ ₹5,000 crore.

No reference date for asset size is given. Build: test last-audited assets from the entity profile; offer the module to every tenant.

**Board/ACB (paras 5–8):**

- Approves the **RBIA plan**, prioritised by the level and direction of risk (5).
- Reviews RBIA performance and keeps a quality assurance and improvement programme, which may include an assessment of the IA function **at least once a year** (6).
- Promotes audit tools that reduce manual monitoring and transaction testing (7).
- Sets a minimum period of service for IA staff (8).

**Senior management (paras 9–11):**

- Ensures action on IA findings **within given timelines**; **closure status goes to the Board/ACB** (9).
- Presents a consolidated position of major risks, drawn from all forms of audit, **at least annually** (11).

**Policy (paras 13–15):**

- Board-approved, with the Risk Management and RBIA roles demarcated (13).
- **Sets the maximum period beyond which even low-risk activities or locations cannot remain excluded from audit** (14).
- Reviewed periodically (15).
- Build: an audit universe with a last-audited date per unit and a hard alert when the policy maximum is reached.

**Scope (paras 18–20, 23):**

- Selective transaction testing **plus** evaluation of risk management systems and controls (18).
- **The IA function is kept informed of new products, changes in reporting lines and changes in accounting practices or policies** (23).
- Build: product-approval, organisation-change and accounting-policy events in M14/M19 auto-notify the IA role.

**Risk assessment (paras 25–31):**

- Independent, **at least annual**, and updated periodically. Covers corporate and branch levels, portfolios, individual transactions and processes (25).
- **Every activity or location, including Risk Management and Compliance**, is assessed (26). The results focus audit on material risks (27).
- Matrix of **inherent business risk × control risk** (28).
- **Level (high/medium/low) and trend (increasing/stable/decreasing)**, with the basis documented (29). Quantitative and qualitative inputs (30).
- **Ten mandatory parameters (31):**
  - previous IA reports and compliance;
  - business-line changes;
  - change in management or key personnel;
  - regulatory examination results;
  - external auditors' reports;
  - industry trends;
  - **time since last audit**;
  - volume and complexity;
  - budget variances;
  - strategy versus risk appetite.
- Build: Finbyx pre-fills these parameters from its own data (volumes, DPD, fraud, complaints, variances).

**Audit plan and assignments (paras 32–35):**

- Risk Audit Matrix of magnitude × frequency. **Priority order:** H/H, H/M, H/L, M/H, M/M, L/H (32).
- Plan, scope, objectives, timelines and resources are set before each assignment (33).
- Scope is defined for **low, medium, high, very high and extremely high** risk areas (34). This 5-level scale differs from the 3 levels in para 29, so make the scale configurable.
- **System and process audits of all critical processes; system-audit findings also go to the IT Committee of the Board** (34).
- Report covers objectives, scope, results, recommendations and action plans (35).

**Compliance monitoring (paras 36–38):**

- A system to monitor compliance with IA observations; compliance status is part of every Board/ACB report (36).
- **All pending high- and medium-risk paras and persisting irregularities are reported to the Board/ACB** (37).
- **RBIA must have proper MIS and data-integrity arrangements** (38).

**Outsourcing (para 39):**

- **The IA function may not be outsourced.**
- Contract experts, including former employees, only where the Board/ACB is assured the expertise is not available in-house. Conflicts of interest must be addressed.
- **Ownership of audit reports stays with regular IA staff.**
- Build: Finbyx supplies tooling only. The report-owner field accepts only IA employees; external experts get a restricted contributor role.

**Head of Internal Audit (paras 40–43):**

- A senior executive. **The HIA and IA staff may communicate with any staff member and access all records** (40).
  - Build: an audit role with tenant-wide read-only access and an access trail.
- Tenure preferably **at least 3 years**, except where IA is run by career internal auditors (41).
- Reports to the Board, ACB, MD & CEO or a WTD. Where the MD & CEO or a WTD is the reporting authority, the **ACB/Board meets the HIA at least quarterly without senior management** (42).
- **No reporting line to business verticals and no business targets** (43).
- Build: HIA register and quarterly meeting tracker.

**Repeal (para 44).** Through circular DoS.CO.PPG.66/11.01.005/2026-27 (31 Jul 2026). The repeal list is not supplied.

---

---

## 8A.33 SA — Statutory Audit Directions (465)

**Applicability (para 3).** All NBFCs, including HFCs, for the appointment and reappointment of SCAs/SAs.

- **Non-deposit-taking NBFCs with assets < ₹1,000 crore may continue their extant procedure.**
- "SCA" applies where separate Statutory Branch Auditors are appointed; otherwise "SA".

**Governance (paras 6–10):**

- Board policy on the number of auditors (6).
- The ACB (or the Board) monitors auditor independence and flags concerns to the Board **and the RBI SSM** (7).
- **Annual performance review. Serious lapses are reported to DoS within two months of completion of the annual audit**, with Board/ACB approval and full details of the firm (8).
- Fee recommendation (9).
- **Appointment policy hosted on the website** (10).

**Number of auditors and branch coverage (paras 11–13):**

- **Assets ≥ ₹15,000 crore at the end of the previous year: joint audit by at least two firms.** Other NBFCs: at least one firm.
- Joint auditors may have no common partners and no shared network (Rule 6(3), Companies (Audit and Auditors) Rules, 2014). Work allocation is finalised before the audit starts (11).
- **Maximum number of SCAs/SAs, by asset size (12):**
  - up to ₹5,00,000 crore: 4;
  - up to ₹10,00,000 crore: 6;
  - up to ₹20,00,000 crore: 8;
  - above that: 12.
- **Branch visits (13; not CICs):** at least the top 20 branches, or the top 20% where there are fewer than 100 branches. Branches are ranked by outstanding advances and must **cover ≥ 15% of total gross advances**. Plus Companies Act s.143(8) for all branches.
- Build: branch-coverage report (M17) ranking branches by advances, with cumulative coverage %.

**Eligibility (paras 14–16):**

| Assets on 31 March of previous year | FTPs (3 yrs) | FCA partners (3 yrs) | CISA/ISA partners or paid CAs | Firm audit experience (yrs) | Professional staff |
|---|---|---|---|---|---|
| > ₹15,000 crore | 5 | 4 | 2 | 15 | 18 |
| > ₹1,000–15,000 crore | 3 | 2 | 1 | 8 | 12 |
| ≤ ₹1,000 crore | 2 | 1 | 1 (not mandatory) | 6 | 8 |

- **Notes 1–4:**
  - FTPs need 1-year continuous association.
  - Above ₹1,000 crore: two partners with 10 years' association, and the "exclusive association" tests (1)–(4).
  - CISA/ISA, audit-experience and professional-staff definitions; a merger takes effect after 2 years, a demerger immediately.
- **Additional conditions (15):**
  - qualified under Companies Act s.141;
  - not debarred;
  - ICAI ethics;
  - **no appointment where a partner is a director of an RBI-regulated group entity**;
  - CAATs/GAS capability preferred above ₹1,000 crore (15(5)).
- **Continued eligibility (16):** the firm reports any lapse, and must comply before the annual audit starts and until it is complete.

**Independence (paras 17–20):**

- Management non-cooperation goes to the Board/ACB, with intimation to the SSM (17).
- **Concurrent auditors are not eligible as SCA/SA.** Audit of any entity with a Large Exposure to the NBFC is factored into the independence assessment (18).
- **Non-audit work (s.144, internal or special assignments) needs a 1-year gap either side of the SA tenure**, including work for RBI-regulated group entities. Permitted during tenure: tax audit, interim audit, regulatory certificates and segment reporting (19).
- These restrictions extend to network firms and firms with common partners (20).

**Tenure and rotation (paras 23–27):**

- **Continuous 3-year term**, subject to eligibility each year.
- **Removal before 3 years: intimate the SSM/RO with reasons within one month** (23).
- **Six-year cooling-off** (two tenures) after a full or part term (24).
- One firm may concurrently audit at most **8 NBFCs**, with separate bank/UCB/StCB-CCB caps (25).
- A network counts as one entity. Sub-contracting is barred. An incoming firm may not be associated with the outgoing one (26).
- CAG-appointed auditors of government companies follow CAG rules (27).

**Fees (paras 28–29).** As per statutory and regulatory provisions, commensurate with the scope of the audit.

**Procedure (para 30):**

- No prior RBI approval is needed.
- **Form A (Annex I) within one month of appointment:** Mumbai Region NBFCs to DoS CO; others to the RO for their Head Office (30(1)).
- **At least two firms shortlisted per vacancy** (30(2)).
- **Form B (Annex II) eligibility certificate from the firm**, with Part B items (i)–(v) and a wilful-defaulter declaration (30(3)).
- The NBFC verifies eligibility before appointing (30(4)).
- Build: M14 auditor register covering term number, tenure dates, cooling-off end date, group/network conflict check against the related-party register, non-audit services log, Form A/Form B generation, and a performance-review task. Form A is also a supervisory return (SR para 21 item 20).

---

---

## 8A.34 SR — Supervisory Returns Directions (466)

**Applicability (para 3).** All NBFCs, all layers, **excluding HFCs**, unless specified otherwise.

- **Supervisory Returns** = all periodic or ad-hoc data submitted to RBI, whatever the platform or mode (para 4(2)).
- **CIMS** = RBI's online platform for return submission (para 4(1)).

**Data governance: build requirements (paras 6–17):**

- Data-quality risk is part of the risk framework, with standards for in-house and outsourced data processes (6).
- **Risk data aggregation and reporting practices are documented and independently validated by IT, data and reporting staff** (7).
- **Data can be aggregated at consolidated or any other level, unhindered by group structure** (8).
- The reporting impact of acquisitions, new products and IT changes is assessed (9).
- **The data architecture delivers complete, accurate and timely aggregation in stress or crisis** (10), within the BCP and business impact analysis (11).
- Data owners are defined (12).
- **On-demand ad-hoc subsets**, for example "exposure for a period for a specific industry cluster in a district" (13).
  - Build: a governed query service over the exposure mart with industry, geography and period dimensions.
- **Every return is reconciled with own sources, including accounting data** (14).
- **Records of sources and aggregation rules** are kept (15). This is M13's cell-level lineage.
- Maximum automation (16).
- **Data accuracy is measured, with escalation and rectification plans** (17).
  - Build: DQ metrics and an issue register.

**Filing mode (paras 18–20):**

- **Online only**, through RBI portals, in the formats communicated.
- **Hard copy or email is not accepted** unless prescribed. Email only as a contingency RBI advises, **then resubmit online** (18).
- A super-user credential creates maker and checker users. Formats, validation rules and guidance notes are on the portals (19).
- Domestic and overseas operations are both reported (20).
- **The Directions do not mention XBRL.** Build: a portal format adapter per return, defined in the return spec.

**Return catalogue (para 21; due dates from paras 22–23):**

| # | Return (code) | Periodicity | Reference date | Due | Applicability | Finbyx priority |
|---|---|---|---|---|---|---|
| 1 | DNBS01 – Important Financial Parameters – Quarterly | Quarterly | 31 Mar / 30 Jun / 30 Sep / 31 Dec | 21 days | UL (excl. CICs); ML (excl. CICs) | Core |
| 2 | DNBS02 – Important Financial Parameters | Quarterly | Quarter-end | 21 days | BL (excl. P2Ps) | Core |
| 3 | DNBS03 – Important Prudential Parameters (CRAR, provisioning) | Quarterly | Quarter-end | 21 days | UL (excl. CICs); ML (excl. CICs and SPDs) | Core |
| 4a | DNBS04A – Short Term Dynamic Liquidity | Quarterly | Quarter-end | 21 days | UL; ML (excl. SPDs); **BL ≥ ₹100 crore solely or at group level**, excluding NBFCs with no public funds and no customer interface, NOFHCs, P2Ps, AAs and MGCs | Core |
| 4b | DNBS04B – Structural Liquidity and Interest Rate Sensitivity | Monthly | Month-end | 15 days | As 4a | Core |
| 5 | CRILC – NBFCs (borrowers with aggregate FB + NFB exposure ≥ ₹5 crore; **NIL return** if none) | Monthly | Month-end | 15 days | UL (excl. CICs); ML (excl. CICs); BL: (a) ICCs (excl. no-public-funds and no-customer-interface), (b) MFIs, (c) Factors with assets ≥ ₹500 crore [VERIFY whether the ₹500 crore qualifier also covers (a)–(b)] | Core |
| 6 | DNBS09 – Return on Defaulted Borrowers (move-in and move-out sections: PAN, name, date of default, funded, non-funded and total outstanding; **NIL return** if none) | Weekly | Friday (or preceding working day) | **Wednesday of the following week** | As CRILC (merged cell) | Core |
| 7 | DNBS10 – Statutory Auditor Certificate | Yearly | 31 Mar | **5 working days from signing of the auditor's report (s.134), and not later than 31 Dec** (para 23) | All NBFCs | Core (the auditor files on CIMS with a login the NBFC creates) |
| 8 | DNBS11 – CICs Important Financial Parameters | Quarterly | Quarter-end | 21 days | CICs | Not targeted |
| 9 | DNBS12 – CICs Important Prudential Parameters | Quarterly | Quarter-end | 21 days | CICs | Not targeted |
| 10 | DNBS13 – Overseas Investment Details (**NIL return** if none) | Quarterly | Quarter-end | 21 days | **All NBFCs** | Core |
| 11 | DNBS14 – P2Ps Financial and Prudential Parameters | Quarterly | Quarter-end | 21 days | P2Ps | Later (P2P) |
| 12 | Large Exposure Framework (20 largest exposures; exposures ≥ 10% of Tier 1; other and exempted exposures) | **Quarterly** | Quarter-end | 21 days | UL | Core (UL) |
| 13 | PDR III – Statement on Capital Adequacy | Quarterly | Quarter-end | 21 days | SPDs | Not targeted |
| 14 | PDR IV – Select Financial and Balance Sheet Indicators | Quarterly | Quarter-end | 21 days | SPDs | Not targeted |
| 15 | Stress Test | Monthly | Month-end | 15 days | SPDs | Not targeted |
| 16 | IRS Test | Monthly | Month-end | 15 days | SPDs | Not targeted |
| 17 | FMR – NBFCs | Per event | Fraud classification date | **14 days** | UL; ML; BL ≥ ₹500 crore | Core |
| 18 | FMR Update Application (FUA) | On any development | Update / progress date | **Immediate** | As FMR (merged cell) | Core |
| 19 | FMR4 / RBR (dacoity, robbery, theft, burglary) | Quarterly | Quarter-end | **15 days** | As FMR (merged cell) | Core |
| 20 | Form A Certificate (SCA/SA appointment) | Yearly | 31 Mar | **1 month from appointment** | **All NBFCs** | Core |

**Timeline rules (paras 22–26):**

- **Default due dates (para 22):**
  - weekly: by Wednesday of the following week;
  - monthly: within 15 days;
  - quarterly: within 21 days;
  - yearly: within 21 days.
- **Audited returns:** within **5 working days from signing of the auditor's report**, solo or group level as applicable (Note 1).
- **Ad-hoc returns:** within the timeline in RBI's communication (Note 2).
- **Penalties (24):** RBI Act action for false information or delay.
- **RBI may add or withdraw returns (25).** Build: the return catalogue is data-driven, not hard-coded.
- **Returns under other Directions are not affected (26).** Examples: CIMS DLA (CF 18), RBR incident emails (FRM 57), IRF (INV 29), CDS (CRM 17(7)), LE breach intimation (CON 45), branch closure (BR 12).
- **Not in the para 21 list:** a "branch info" return, a separate "sectoral" return, and any XBRL requirement.

---

---

## 8A.35 MSD — Miscellaneous Supervisory Directions (467)

**Applicability (para 3).** NBFCs and HFCs, all layers, unless specified otherwise.

- **Ch III also applies to HFCs and MFIs.**
- **Ch IV applies only to NBFC-D, excluding HFCs.**
- **Ch V applies to NBFC-D, and to NBFC-ND in the ML, UL and TL** (ICC, CIC, IDF, IFC, MFI, Factors).
  - **Excluded:** NBFCs not accepting or intending to accept public funds, Primary Dealers, and HFCs.

**Ch II: CFSS (paras 5–6):**

- **UL and ML NBFCs with 10 or more "fixed point service delivery units" must implement a Core Financial Services Solution**, akin to a bank's CBS. Others may adopt it voluntarily (5).
- **Required capabilities (5):**
  - seamless digital customer interface, available anywhere and anytime;
  - integration of the NBFC's functions;
  - **centralised database and accounting records**;
  - MIS for internal purposes and regulatory reporting.
- **Fixed point unit** = a place where non-banking financial intermediation business is carried out:
  - staffed by own staff **or outsourced agents**;
  - with uniform NBFC signage;
  - under the NBFC's administrative control.
  - Administrative and back offices with no customer interface are excluded (5, Explanation).
- **Quarterly CFSS implementation progress report to the SSM** (6).
- No HFC exclusion is made for Ch II.
- Build:
  - `fixed_point_unit` flag on the branch master (M1); a count of ≥ 10 for UL/ML raises an M14 obligation;
  - CFSS capability conformance document per tenant;
  - quarterly progress-report template.

**Ch III: Fair Practices Code, charging of interest (paras 7–9).** Review practices and make system-level changes against these unfair practices (7):

- **(1) Wrong interest start date:**
  - interest from the sanction or agreement date instead of actual disbursement;
  - **interest from the cheque date when the cheque is handed over later**.
- **(2) EMIs on the sanctioned amount rather than the actual disbursed amount**, without the borrower's knowledge or consent.
- **(3) Changes to the KFS amortisation schedule with each part-disbursement not communicated to the borrower.**
- **(4) Full-month interest where disbursal or repayment happens during a month**, instead of interest for the period outstanding.
- **(5) Instalments collected in advance while interest is still charged on the full loan amount.**

Such practices are "matters of serious concern" (8). Online transfers may replace cheques (9).

Build:

- accrual starts from the disbursement value date (UTR) or the cheque handover date;
- EMI is computed on the disbursed principal only;
- each tranche auto-pushes a revised schedule and KFS annex;
- broken periods accrue at day level;
- advance instalments reduce the interest-bearing principal from the date of receipt;
- one M14 control test per sub-para.

**Ch IV: Nomination for NBFC-D deposits (paras 10–14):**

- Nomination obtained for all existing and new eligible deposit accounts (10).
- Board/CSC reviews nomination coverage periodically (11).
- **Quarterly coverage report to the SSM via DAKSH** (12).
- Account-opening forms let the customer opt in or out (13).
- Publicity drives to reach full coverage (14).
- Build (deposits module, later): nomination record, opt-out flag, coverage MIS.

**Ch V: Prompt Corrective Action (paras 15–21):**

- **Indicators (16):**
  - NBFC-D and NBFC-ND: **CRAR, Tier 1 ratio and NNPA ratio (incl. NPIs)**;
  - CICs: **ANW/RWA, leverage and NNPA**.
- Placement is generally based on audited annual results or supervisory assessment, but RBI may act at any time (17).

| Indicator | Risk Threshold 1 | Risk Threshold 2 | Risk Threshold 3 |
|---|---|---|---|
| CRAR | ≤ 300 bps below minimum (currently < 15%, ≥ 12%) | 300–600 bps below (< 12%, ≥ 9%) | > 600 bps below (< 9%) |
| Tier 1 | ≤ 200 bps below (< 10%, ≥ 8%) | 200–400 bps below (< 8%, ≥ 6%) | > 400 bps below (< 6%) |
| NNPA (incl. NPIs) | > 6%, ≤ 9% | > 9%, ≤ 12% | > 12% |
| CIC ANW/RWA | ≤ 600 bps below (< 30%, ≥ 24%) | 600–1,200 bps below (< 24%, ≥ 18%) | > 1,200 bps below (< 18%) |
| CIC leverage | ≥ 2.5x, < 3x | ≥ 3x, < 3.5x | ≥ 3.5x |

- **Exit (18):** no breach in four continuous quarterly financial statements, one of them annual audited, plus RBI's supervisory comfort.
- **Mandatory actions (19):**
  - **RT1:**
    - dividend restriction;
    - equity infusion and reduction in leverage;
    - for CICs, a restriction on guarantees.
  - **RT2:** adds a **branch expansion restriction**.
  - **RT3:** adds:
    - a capex restriction, except Board-approved technology upgrades;
    - cuts in variable operating costs.
- Discretionary menu (20). RBI press release on placement and withdrawal (21).
- Build:
  - M12 PCA monitor that projects threshold positions from quarterly results and flags proximity;
  - `pca_status` on the entity profile, blocking or warning on branch opening (M1) and dividends;
  - restriction register in M14.

---

## 8A.36 v1.3 build additions (consolidated)

These tables collect the build items from 8A.17–8A.35 by target. They carry the same weight as 8A.16: the related module, product, return or phase specification must include them, and **Part 8A prevails** over any conflicting text elsewhere.

### 8A.36.1 Cross-module additions (Part 7)

| Module | Directions | Additions |
|---|---|---|
| COB (Part 4) | TDCR / SEC | **Job-level:** CLA 15-day booking-clock check and escrow appropriation (TDCR 113, 117). Classification sync file sent by the end of the next working day (TDCR 124) |
| M1 | IRACP / RSA | Part A/B resolver: NBFC-D or ND ≥ ₹500 crore = Part A, else Part B (RSA 7–8, 157–158); HFC RSA scope limited to paras 86–138 (RSA 5) |
| M1 | KYC | Entity profile flags: `s11a_notified` (gates Aadhaar e-KYC authentication; KYC 23 proviso (i)), `vcip_enabled`, `fatca_reporting_fi` (KYC 64), `customer_interface` (KYC 3). Designated Director / Principal Officer register with FIU-IND/RBI intimation and a block on the same person holding both roles (KYC 14–15) |
| M1 | CAP / SBR / DIV / MISC | Entity-profile fields listed at the end of 8A.25 (SBR 6, 10–30, 38–47; CAP 4(8), 6(5)). Group master with members' CoR status and assets (SBR 17–20). Master-data change triggers for 1-month intimations (MISC 6–7) |
| M1 | GOV / OUT / ORM | Entity profile flags: government_owned (GOV 3(1), 18(1)(ii)); listed (GOV 22); assets_above_5000cr for the CRO rule (GOV 19); ul_identification_date (GOV 43). Website publication of the corporate-governance guidelines (GOV 40) |
| M1 | MFI / IAF / SA / SR / MSD | Entity profile flags: nbfc_mfi, cic, p2p, spd, factor, aa, mgc (SR 21); group_asset_size (SR 21 item 4); sro_membership (MFI 46); pca_status (MSD 17); mumbai_region for Form A routing (SA 30(1)); ia_applicable (IAF 3); sa_extant_option (SA 3). Branch master: `fixed_point_unit` flag and count (MSD 5). Branch opening blocked or warned under PCA Risk Threshold 2+ (MSD 19) |
| M2 | RBC / WD | DSA/DMA/recovery-agent training and code-of-conduct undertakings (RBC 98–99); telemarketer DoT/TRAI registration register (RBC 101) |
| M2 | GOV / OUT / ORM | Third-party and outsourcing register (OUT 36, 64(2), 82; ORM 74(5)). DSA/LSP/agency termination publicity: website notice plus notices to affected customers (OUT 44, 89). Product-literature clause stating that service providers may be used (OUT 55) |
| M3 | RBC / WD | Language preference driving all communications (RBC 10); PwD flag and assistance (RBC 28); LWD and large-defaulter screening of borrower, guarantors, directors (DIN) and persons in charge (PAN), identical names resolved through independent sources (WD 19(1)) |
| M3 | KYC | KYC mode engine (KYC 23); OVD/deemed-OVD 3-month clock (5(1)(xiv)); BO calculator with company >10%, partnership >10%, unincorporated association/BOI >15%, trust ≥10% thresholds and listed-entity exemption (5(1)(iv), 38); proprietorship 2-of-8 activity proofs (31–32); UCIC (17(6), 66); risk engine with 6-monthly review and reasons hidden from the customer (20(4), 41(1)); updation scheduler with 2/8/10 years, 30 Jun 2026 low-risk grace and 3+3 notice log (42); NFTF EDD state (44); PEP approval workflow (45); para 25 OTP-e-KYC account tracker with 1-year expiry (25); CKYCR 10/7-day clocks and inbound-update handler (63); V-CIP module with concurrent-audit hold (27); daily sanctions batch plus screening at onboarding and in real time, match-case workflow, freeze, 2-working-day unfreeze forwarding (54–57, Annexes I–II); AML alert engine with para 40 typologies and profile-inconsistency rules (40, 53); centralised KYC exception database (23 proviso); rejection-reason capture (18) |
| M3 | TDCR / SEC | **Counterparty master:** lender type, permitted transferee, ARC and regulated facility-provider flags (TDCR 12(4), 12(8); SEC 80). s.29A and promoter-group declarations for transferees, verified by the transferor (TDCR 12(14)) |
| M4 | IRACP / RSA | Agreement clause with computed SMA/NPA example dates and moratorium start date, regenerated on any change of terms (IRACP 15). **Cooling-period gate:** no fresh exposure for at least 12 months after a compromise settlement, and per policy after a technical write-off (RSA 95–96). **Restructuring-definition test:** any change of terms, roll-over or additional credit for a borrower flagged with financial difficulty is routed as restructuring (RSA 10(12), 13–15). Fraud/WD restructuring block (RSA 83–85) |
| M4 | RBC / WD | Application acknowledgement with disposal timeline (RBC 12); vernacular sanction letter with annualised rate, method of application and risk-gradation rationale (RBC 13, 22, 24); late-payment penalties in bold in the agreement (RBC 13); agreement and all enclosures delivered (RBC 14); KFS Part 1/Part 2 with proposal number, validity and acknowledgement, and the APR engine (RBC 29, Annex I); vehicle repossession clause contents (RBC 26); wilful-defaulter penal gate at application, renewal, enhancement, top-up and restructuring, with 1-year/5-year clocks and new-venture flag (WD 7(3)); LWD board/management covenant in every credit agreement (WD 7(4)); auditor-mandate covenant (WD 20(4)) |
| M4 | KYC | Pre-sanction gate: CDD complete and the KYC decision taken by a tenant user (KYC 13, 17(3)); OTP-e-KYC NFTF customer → term loan only, ≤ ₹60,000 aggregate sanction a year (25(5)); PEP senior-management approval (45); sanctions clear (17(9), 55(2)) |
| M4 | TDCR / SEC | **CLA origination:** KFS and loan agreement name the partner, roles and single point of customer interface (TDCR 105–106, 114); blended-rate pricing (108); objective lending-service fees with no CE/DLG element (111) |
| M4 | CAP / SBR / DIV / MISC | **rw_class assigned at sanction**, incl. the consumer-credit 125% classifier (CAP 18(1) Sr (3)(e)(i)). Guarantee-cover capture: scheme, coverage %, first loss, payout cap (CAP 18(2)(iv)). FD-lien and staff-loan flags at 0% (CAP 18(1) Sr (3)(c)–(d)). `unconditionally_cancellable` flag and original maturity of undrawn limits (CAP 18(4)). HQ-infrastructure flag with sanctioned project debt (CAP Sr (2)(e)). Blocks on loans against own PDI or NCDs (CAP 12(14); MISC 11(6)). Cash-disbursal block per ss.269SS/269T (MISC 24). Factoring: invoice genuineness, debtor appraisal, without-recourse Board limit (MISC 49–51) |
| M4 | GOV / OUT / ORM | Sanction-committee configuration with the CRO as adviser or voter, with votes recorded (GOV 23–24). BRE decisions attributed only to tenant-approved rule versions; no Finbyx or LSP role can sanction (OUT 15) |
| M4 | MFI / IAF / SA / SR / MSD | Gate enforcing the 25% microfinance cap for non-MFI NBFCs (MFI 49). Channelising-scheme loans tagged (MFI 13) |
| M5 | RBC / WD | Gold assay certificate (paper or e-) with image, borrower present at assay, non-employee witness for illiterate borrowers (RBC 46, 50–51); surprise-verification register with consent clause (RBC 57); release clocks: 30/60 days for property documents and same day/7 working days for gold, with attribution flag and ₹5,000/day compensation (RBC 35–40, 58, 69); legal-heir release (RBC 38); gold auction (notice, public notice + 1 month, two newspapers, 90%/85% reserve, district rule, related-party bar, 7-working-day surplus refund) (RBC 60–66); unclaimed-collateral register after 2 years (RBC 71–72) |
| M5 | CAP / SBR / DIV / MISC | BG confirmation with the issuing bank before acceptance (MISC 29–31). Gold share of financial assets feeds the gold_primary flag (CAP 4(8)) |
| M6 | IRACP / RSA | Classification history per borrower, dated by COB calendar date (IRACP 19); NPI flag pushed to investments (IRACP 23); HP/lease contract type classified on recovery record (IRACP 43(7), 51(7)). Restructuring workbench: plan record (RSA 35); Part B viability benchmarks (171), promoter contribution (179–180), personal guarantee (177), recompense clause (176), 120-day clock from application (178), no back-dating (163), housing tenor/EMI option (185–187); monitoring/specified-period tracker with Part A zero-default test (RSA 10(14)); repeat-restructuring counter (159(4), 194); additional-finance tagging (56–57, 193); FITL creation (RSA 140, 220) |
| M6 | RBC / WD | Penal-charge engine (base = overdue amount, no penal on penal, individual ≤ non-individual check) (RBC 30); reset election workflow, negative-amortisation guard and quarterly statement (RBC 31–32); prepayment engine (RBC 33–34, 81); prospective-only change guard with vernacular notice (RBC 15, 83); account-transfer request with 21-day SLA (RBC 19); set-off notice on retention of securities (RBC 17); nearest-rupee rounding at posting (RBC 103); end-use certificate tracker (WD 19(2)) |
| M6 / M7 | KYC | Account modes: **credits-only** (no PAN/Form 60, KYC 43; OTP-e-KYC expiry, 25(7)); sanctions freeze, allowing interest and pre-listing contractual credits (Annex I 10.2; Annex II 6.2); NFTF first-credit check from the customer's own KYC-compliant bank account (44(5)); third-party or own-product sales of ₹50,000 or more only by account debit or cheque, with PAN (71) |
| M6 | TDCR / SEC | **Servicing of sold, participated and securitised loans:** collections held in trust, no commingling, remit only after collection (TDCR 30; SEC 95). Dual borrower sub-accounts for CLAs (TDCR 116). CLA escrow appropriation (TDCR 117) |
| M6 | CAP / SBR / DIV / MISC | Rupee rounding at billing and posting (MISC 27). Repayment % of sanctioned project debt for the infrastructure RW step-down and 31 Mar 2027 grandfathering (CAP Sr (2)(e)). Factoring NPA at 90/180 days on the exposure entity (MISC 44–46) |
| M6 / Part 4 schedule engine | MFI / IAF / SA / SR / MSD | Interest accrual from the disbursement UTR or cheque handover date; EMI on disbursed principal only; schedule and KFS revision pushed on each tranche; day-level broken-period interest; advance instalments reduce the interest base (MSD 7(1)–(5)) |
| M7 | CAP / SBR / DIV / MISC | PDC capture blocked where NACH is available; CTS-2010 cheques only (MISC 22–23; not HFCs) |
| M7 / M10 | GOV / OUT / ORM | Vendor reconciliation and ageing report for the ACB, covering collection agencies, aggregators and DSA payouts (OUT 12(2)(ii), 39) |
| M8 | RBC / WD | Current contact rules: 08:00–19:00 general (RBC 100), 09:00–18:00 and harsh-practice list for microfinance (RBC 91); microfinance designated-place collection rule (RBC 90); agent notice, authorisation letter and ID before contact; notice of agency change (RBC 95–96); agent antecedent/police-verification register (RBC 94); penal charge shown in every reminder (RBC 30(7)); identification of borrowers in difficulty (RBC 89) |
| M9 | IRACP / RSA | Settlement policy engine (RSA 16); > 3-month or part settlement switches to restructuring (RSA 89–90); consent-decree checkpoint where a legal_case is pending (RSA 100); fraud/WD Board-approval route (RSA 16(5)(ii)); DRS claim tracker, no Government receivable (RSA 133) |
| M9 | RBC / WD | Wilful-defaulter case management: IC/RC composition validator, 21-day and 15-day timers, 6-month deadline, hearing record, reasoned order naming members (WD 5–6); guarantor and group-company cases (WD 10); penal-bar register (WD 7(3)); LWD logic for compromise settlements (WD 13); IBC/resolution removal (WD 15); pre-transfer wilful-default gate (WD 14); auditor and third-party complaint register with hearing (WD 20–21) |
| M9 | TDCR / SEC | **Stressed-loan sale workflow:** Board NPA review (TDCR 56); valuation, with 2 external reports ≥ ₹100 crore (57); Swiss challenge with 5–15% mark-up and the para 92(5) provision (60, 89–92); 12-month cooling block (61); 3-year exposure block (62(3)(iv)–(v)); no contingent price (65); fraud-to-ARC hand-over (78) together with FRM 54 |
| M10 | IRACP / RSA | Provision engine: layer and UL category rates (IRACP 48, 55, 58); project-finance phase rates (IRACP 30); teaser-rate reset clock (58); doubtful-age tiers on the secured portion (32(2)); HP/lease NBV engine (33); 100% on liquidity facility > 90 days (31); "Contingent Provisions against Standard Assets" line (28); DLG-aware ECL recomputed on invocation (36A–36C). Fair-value diminution engine with separate account, recomputed every balance-sheet date, 5% option below ₹1 crore (RSA 198–211); Sundry Liabilities (Interest Capitalisation) (RSA 152–153, 223–227); additional provisions 20% / 15% / 15% (RSA 48, 64); DCCO 0.375% / 0.5625% per quarter (RSA 118); accelerated-provisioning table (RSA 23); DRS 100% after 90 days (RSA 137); 100% cap (RSA 49, 211) |
| M10 | TDCR / SEC | Unrealised-profit CET1/NOF deduction (TDCR 45, 107). Premium amortisation (51). ARC shortfall and excess provisioning (80–81). SR valuation incl. ₹1 and 5/8-year loss rule (82–85). Acquired stressed-loan NPV provision (71). Acquired-NPA cash amortisation (76). "Unrealised Gain on Loan Transfer Transactions" account (SEC 34). CE drawdown write-off (SEC 83(4)). Liquidity draw NPA after 90 days (SEC 91) |
| M10 | CAP / SBR / DIV / MISC | GL capital-component tags; owned fund, NOF, CET1, Tier 1/2 and EPt with a limited-review flag (CAP 7–16; SBR 45–46). Dividend register and eligibility checker (DIV 8–13). PBC test with bank FDs excluded (SBR 38; MISC 21). **Borrowings:** PDI (15% cap, call/step-up/lock-in) and sub-debt discount schedule (CAP 12–13); NCD private-placement controls — ₹20,000 minimum, ≤ 200 subscribers per FY below ₹1 crore and fully secured, own-balance-sheet use (MISC 10–11) |
| M10 | MFI / IAF / SA / SR / MSD | MFI provision floor computed on overdue instalments (MFI 25); CRGFTLIH carve-out (MFI 26); channelising-agent segment GL and disclosure (MFI 13(2)(i)) |
| M11 | RBC / WD | Co-lending block in KFS Part 2 item 5 (originating and partner RE, funding shares, blended rate) (RBC Annex I); transferee LWD reporting (WD 14(3), 14(5)) |
| M11 | CAP / SBR / DIV / MISC | Securitisation tranches, ratings, A/D/T/MT and derecognition test (CAP 19–51). Gain-on-sale deduction (CAP 19). Co-lending unrealised-profit deduction (CAP 15(2)). DLG deduction (CAP 15(3)) |
| M12 | IRACP / RSA | UL derivative CCE provisioning (IRACP 59–60). Financial-difficulty indicator register (RSA 13–15); ICA/consortium register with 75% value / 60% number voting (RSA 31–33); ICE and rating tracker (RSA 36–41, 60) |
| M12 | TDCR / SEC | 100% risk weight on acquired NPAs while standard (TDCR 77). Capital fallbacks (TDCR 27, 30; SEC 83, 90, 93, 96). Transferee and investor stress tests (TDCR 41; SEC 103). Securitisation valuation policy (SEC 104). 20% retained-exposure cap (SEC 23) |
| M12 | CAP / SBR / DIV / MISC | **RWA/CRAR engine** (Part 8A.24): versioned RW/CCF/add-on/ERBA masters; ratios by profile; BL leverage ≤ 7 (CAP 17); what-if per sanction; lineage; para 48 golden test. CDS mismatch and 667% logic (CAP 53). ICAAP for ML+ (CAP 54) |
| M12 | GOV / OUT / ORM | **ORM suite:** taxonomy and control library (ORM 24); RCSA (42(1)); loss-event database with occurrence/discovery/accounting dates, near misses and root cause (42(2)); KRIs with thresholds (42(5)); scenario analysis per critical operation (42(6)); critical-operations register with Board-approved criteria (31); impact tolerances with time, data-loss and service-level metrics (32–33); dependency map with single points of failure (69–72); action plans (43(3)); annual insurance review (64); lessons-learned workflow with the para 101 questions and a Board report (99–102). Outsourcing concentration risk (OUT 67) |
| M12 | MFI / IAF / SA / SR / MSD | MFI qualifying-asset monitor with 4-quarter breach counter (MFI 12); geographic exposure limits (MFI 10); PCA indicator monitor and threshold-proximity alerts (MSD 16–17); ad-hoc exposure-subset query service (SR 13) |
| M13 | MFI / IAF / SA / SR / MSD | Data-driven return catalogue (SR 21, 25); due-date engine (SR 22–23); portal maker-checker log (SR 19); GL reconciliation per return (SR 14); aggregation-rule registry (SR 15); DQ metrics and escalation (SR 17); NIL-return generation for CRILC, DNBS09 and DNBS13 (SR 21) |
| M14 | RBC / WD | Control tests: no charge outside the KFS (RBC 29(5)); no penal on penal or capitalisation (RBC 30); KFS acknowledgement captured (RBC 29(1)); release within 30 days / 7 working days (RBC 35, 58); reminder shows penal charge (RBC 30(7)); no back-dated rate change (RBC 15); WD 6-month completion (WD 6(2)); LWD gate applied (WD 7). Applicability engine: classification only for ML and above; every RE gets the screening gate and large-defaulter provisions (WD 2); stop classifying but keep updating CIC history on reclassification to BL (WD 12(3)). Policy library: RBC 7(1)–(8); WD 4 |
| M14 | KYC | KYC policy registry with the para 6 elements (KYC 6); annual ML/TF risk assessment (10); ML/TF assessment step in the product-approval gate (68); control tests: CKYC 10/7 days (63), daily sanctions run (54(2), 56), 6-monthly risk review (41(1)), 3+3 notices (42(7)), V-CIP concurrent audit before activation (27(2)(xiv)) |
| M14 | TDCR / SEC | **Policy registry:** transfer/acquisition policy (TDCR 13), stressed-loan policy (55), Swiss challenge (89), ARC take-over (87), CLA credit policy (103), securitisation valuation (SEC 104) |
| M14 | CAP / SBR / DIV / MISC | Applicability engine loads the CAP para 3 and MISC para 3(1) paragraph lists per entity type. FATF investor register (SBR 47). Partnership/LLP/AOP prohibition control (MISC 16–19). UL milestones and NOF glide-path calendar (SBR 27–29, 42–43) |
| M14 | GOV / OUT / ORM | **Governance register:** directors, KMP, CRO and CCO; Annex I/II/III e-forms; NRC decisions; 31 March declarations; 30% change calculator and PRAVAAH pack; independent-director and KMP directorship-limit checks; CRO tenure and closed-session tracker (GOV 10–14, 19–28). **Policy registry** for GOV 7, 38, 40, 43; OUT 10, 20, 45, 62, 97(v); ORM 16, 23, 30, 74, 97, with approval and review dates. Whistle-blower case module (GOV 38; FRM 10). Code-of-conduct attestation (ORM 16). Mandatory-leave register for sensitive positions (ORM 60). The product-approval gate adds CRO vetting (GOV 23) and the ORM 47 risk heads |
| M14 | MFI / IAF / SA / SR / MSD | RBIA suite (IAF 5–43); statutory-auditor register with Form A/B, tenure, cooling-off and non-audit-services log (SA 6–30); CFSS obligation and quarterly SSM report (MSD 5–6); PCA restriction register (MSD 19); SRO Code of Conduct obligations (MFI 46); control tests for MSD 7(1)–(5) |
| M15 / portal | IRACP / RSA | Consumer-education web page on overdue, SMA, NPA and upgrade with the day-end process (IRACP 17) |
| M15 | RBC / WD | Disputes decided at least at the next higher level (RBC 7(2)); generic GRO email only with a 1-working-day response (RBC Annex I Part 2(3)); microfinance recovery-grievance details given at disbursal (RBC 92); PwD grievances (RBC 28) |
| M15 | GOV / OUT / ORM | GRO display text covering outsourced agencies (OUT 57(2)). MFI accountability declaration in the loan agreement and FPC (OUT 56). Complaints received by Finbyx or Udofin are routed to the tenant's GRO (OUT 54, 98) |
| M16 | KYC | Retention: transactions 5 years from date; ID records 5 years after relationship end (KYC 47); V-CIP recordings in India with timestamps and official credentials (27(3)); DARPAN records (48) |
| M17 | IRACP / RSA | Quarterly settlement/technical write-off report with the RSA 94 cuts; Board report for MD & CEO / Board-committee approvals (RSA 93) |
| M17 | RBC / WD | Board/committee packs: FPC and grievance-redressal consolidated review (RBC 8); half-yearly unclaimed gold/silver report (RBC 72); Audit Committee wilful-default review with root causes (WD 9(2)) |
| M17 | KYC | Quarterly KYC audit notes to the Audit Committee (KYC 12(5)); annual ML/TF assessment to the Board (10(4)) |
| M17 | TDCR / SEC | Board/committee periodic review of NPAs above the threshold, with documented transfer rationale (TDCR 56) |
| M17 | CAP / SBR / DIV / MISC | Board packs: capital adequacy; dividend proposal with eligibility test (DIV 6–9); UL transition roadmap (SBR 27); ICAAP (CAP 54); NCD resource-planning policy (MISC 10); PDI policy and disclosures (CAP 12(15)) |
| M17 | GOV / OUT / ORM | Half-yearly material-outsourcing review (OUT 12(1)(vii), 36); GOV 15 reviews; ORM Board reports (ORM 31–32, 55, 82, 102) |
| M17 | MFI / IAF / SA / SR / MSD | Board/ACB packs: RBIA plan approval and annual QA (IAF 5–6); closure status and pending high/medium paras (IAF 9, 37); annual consolidated risk position (IAF 11); system-audit findings to the IT Committee (IAF 34); HIA quarterly meeting (IAF 42); auditor annual performance review (SA 8). Branch-coverage report (SA 13). PCA dashboard (MSD 16–19) |
| M18 | RBC / WD | Vernacular template coverage with dispatch block (RBC 10); website disclosure publisher: FPC, rates and risk gradation, penal-charge schedule, reset/switch charges, gold valuation methodology, legal-heir procedure, recovery-agency list, microfinance min/max/average rates (RBC 21, 23, 30(6), 31(4), 38, 45, 82, 97); branch-closure notices (RBC 102) |
| M18 | KYC | Periodic-updation letters and reminders; acknowledgement and updation intimation (KYC 42(5)(iii), 42(7)); KYC Identifier communication (63(6)) |
| M19 | GOV / OUT / ORM | SoD: the CRO and CCO cannot hold business or target roles (GOV 21(3)–(4); CMP 27). Finbyx-staff break-glass access provisioned by the tenant, with logs visible to the tenant (OUT 24, 70). MFA and a role-conflict matrix for cloud access (OUT 97(viii)) |
| M21 | GOV / OUT / ORM | Per-tenant SIEM/SOC log feed (OUT 97(xi)). Full tenant export API covering ledger, loans, documents, audit trail and configuration (OUT 42, 97(xvi)) |
| M22 | KYC | Para 24 digital KYC: live-only capture, watermark fields, white-background guidance, QR auto-fill, customer OTP with the fixed text, officer-mobile block, officer OTP declaration with photo, digitally signed CAF upload (KYC 24) |
| M23 / Udofin | KYC | NFTF EDD (KYC 44); Aadhaar OTP alerts only to the Aadhaar mobile (25(2)); registered-mobile change process (6(3)(v), 44(2)) |
| Website / M15 | TDCR / SEC | Active CLA partner list (TDCR 126). CLA grievance under the FPC (TDCR 121) |
| Workspace L | CAP / SBR / DIV / MISC | Group asset-size certificate (SBR 20); PBC/NOF workings (SBR 38–46; MISC 21); CRAR lineage (CAP) |
| Workspace L | MFI / IAF / SA / SR / MSD | IA role with tenant-wide read-only access and an access trail (IAF 40); external-expert contributor role; report ownership limited to IA staff (IAF 39); CAATs/GAS data export (SA 15(5)) |

### 8A.36.2 New and corrected returns and reports (M13)

Add these to the M13 return catalogue. Applicability is resolved from the entity regulatory profile (M1). Where SR and an earlier Direction differ on periodicity, the Large Exposures return defaults to **quarterly** per SR, with a [VERIFY] against CON Annex I ("Return for the Month").

| Return / report | Timeline | Source |
|---|---|---|
| CRILC credit information incl. SMA status, borrowers with aggregate exposure ≥ ₹5 crore | Monthly | RSA 20, 158 |
| Weekly default report (borrowers ≥ ₹5 crore) | Close of business every Friday (or preceding working day) | RSA 21 |
| Project credit-event reporting to CRILC; intimation to consortium members | Weekly and CRILC-Main; on occurrence | RSA 106–107 |
| Information-utility (NeSL) financial-information submission | Per IBC and IU Regulations | RSA 24 |
| Settlement / technical write-off report to next higher authority; Board for MD & CEO / BLC approvals | At least quarterly | RSA 93–94 |
| List of large defaulters (≥ ₹1 crore), Annex I, to all CICs | Monthly; separate suit-filed and non-suit-filed files | WD 11, Annex I |
| List of wilful defaulters (LWD), Annex II, to all CICs | Monthly; separate files; SFTP | WD 12(1), Annex II |
| LWD removal intimation to all CICs | Within 30 days of the outstanding falling below ₹25 lakh; for settlements, only after full payment | WD 12(2), 13 |
| LWD reporting before transfer of a defaulted loan; details to the transferee | Before transfer | WD 14(2)–(3) |
| Auditor complaint to NFRA/ICAI, forwarded to RBI (DoS, CO) and IBA | Event-based, after a hearing | WD 20(1)–(2) |
| Third-party details to IBA | Event-based, after a hearing | WD 21(2) |
| Microfinance minimum/maximum/average interest rates in supervisory returns | Per the Supervisory Returns Directions | RBC 82 |
| Telemarketer list with registered numbers to TRAI | On engagement or change | RBC 101(2) |
| Unclaimed gold/silver collateral report to the Customer Service Committee/Board | Half-yearly | RBC 72 |
| FPC and grievance-redressal consolidated review to the Board | At regular intervals | RBC 8 |
| FIU-IND STR / CTR / NTR / CCR | Per PML Rules r.8 [VERIFY: not stated in the KYC Directions] | KYC 49–51 |
| UAPA match report (CNO-UAPA, FIU-IND, MHA, State nodal officer, RBI) | Immediately / without delay | KYC 54(3); Annex I 5.1 |
| WMD match report (CNO = Director FIU-IND; copy to State Nodal Officer and RBI) | Immediately | KYC 55(4) |
| Forwarding of unfreeze applications | Within 2 working days | KYC 55(9); Annex I 11.2, 11A |
| CKYCR upload / update | 10 days from commencement / 7 days from receipt of updated information | KYC 63(1), 63(7) |
| Designated Director and Principal Officer details to FIU-IND and RBI | On appointment or change | KYC 14(2), 15(2) |
| FATCA/CRS Form 61B or NIL (Reporting FIs only) | Per IT Rules [VERIFY] | KYC 64 |
| V-CIP forged-identity case reported as a cyber event | Per CYB incident rules | KYC 27(1)(vii) |
| Quarterly KYC audit notes to the Audit Committee | Quarterly | KYC 12(5) |
| Loan-transfer trade report | Each transaction, to the RBI-notified platform; keep a transaction database until it is notified | TDCR 94 |
| Notice to RBI DoS of replacement or damages under reps and warranties | Each instance | TDCR 24; SEC 30(7) |
| CLA classification sharing with partner RE | Near-real time; end of the next working day at the latest | TDCR 124 |
| CLA disclosure in notes to accounts | Annual | TDCR 127 |
| Website list of active CLA partners | Ongoing | TDCR 126 |
| Securitisation transaction report to RBI | Quarterly; format to be advised [VERIFY: format not issued] | SEC 115 |
| MHP/MRR disclosure per transaction (Annex I) | At origination, half-yearly (September and March), and on any breach | SEC 112–113 |
| Material risk-profile change notice to investors, CRAs and service providers | Within 14 calendar days | SEC 22 |
| STC investor data (loan-level or stratified) | At least quarterly | SEC 52 |
| Third-party servicer data certified by auditors | Preferably at least annually | SEC 109 |
| Dividend declaration (Annex I; HFC to NHB; SPD Annex II with Board resolution to IDMD) | Within a fortnight of declaration | DIV 13–15 |
| PDI issue report with offer document | Soon after issue | CAP 12(12) |
| PDI interest lock-in notification | On each invocation | CAP 12(8)(iv) |
| Exposures above single/group limits due to CDS/CRT | Quarterly | CAP 53(7) (= CRM 17(7)) |
| Group asset-size statutory auditor certificate | Annually, as on 31 March | SBR 20 |
| UL Board policy, implementation plan and roadmap | Within 3 months of RBI advice | SBR 27 |
| Change of registered/corporate office address, phone, fax | Within 1 month | MISC 6 |
| Change in directors, principal officers, auditors, specimen signatures | Within 1 month | MISC 7 |
| Rating upgrade/downgrade of any financial product (assets ≥ ₹100 crore) | Within 15 days | MISC 20 |
| Statement on change of directors + MD/CEO fit-and-proper certificate (ML/UL) | Quarterly, within 15 days of quarter-end, to the RBI DoS Regional Office (NHB for HFCs); the March statement is auditor-certified | GOV 14 |
| Prior-approval application for a change of more than 30% of directors (excl. IDs) | Before the change, via PRAVAAH with Annex I | GOV 10–11 |
| Intimation of any change in directors or management | Event-driven; no timeline in the text | GOV 10 Explanation |
| CRO premature transfer or removal | Event-driven, to the DoS Regional Office (NHB for HFCs); any CRO change to the stock exchanges if listed | GOV 22 |
| Premature exit of an independent director (UL) | Event-driven, to supervisors | GOV 42 |
| Security breach or leakage of customer data at a service provider | Immediately, to RBI | OUT 28, 69(iii) |
| Cyber incident at a service provider | To RBI within 6 hours of detection by the service provider | OUT 61 |
| DNBS01 (UL/ML excl. CICs) | Quarterly, within 21 days | SR 21 item 1, 22 |
| DNBS02 (BL excl. P2Ps) | Quarterly, within 21 days | SR 21 item 2, 22 |
| DNBS03 (UL excl. CICs; ML excl. CICs/SPDs) | Quarterly, within 21 days | SR 21 item 3, 22 |
| DNBS04A / DNBS04B | Quarterly within 21 days / monthly within 15 days | SR 21 item 4, 22; ALM 57 |
| CRILC (≥ ₹5 crore borrowers; NIL return) | Monthly, within 15 days | SR 21 item 5, 22 |
| DNBS09 Defaulted Borrowers (NIL return) | Weekly as on Friday; by Wednesday of the following week | SR 21 item 6, 22 |
| DNBS10 SAC | 5 working days from auditor's report; by 31 Dec | SR 21 item 7, 23 |
| DNBS13 Overseas Investment (all NBFCs; NIL return) | Quarterly, within 21 days | SR 21 item 10, 22 |
| Large Exposure Framework (UL) | Quarterly, within 21 days | SR 21 item 12, 22 |
| FMR / FUA / FMR4-RBR (UL, ML, BL ≥ ₹500 crore) | 14 days / immediate / quarterly within 15 days | SR 21 items 17–19, 23 |
| Form A Certificate (all NBFCs) | Within 1 month of SCA/SA appointment | SR 21 item 20, 23; SA 30(1) |
| Audited returns (generic) | Within 5 working days of signing of auditor's report | SR 22 Note 1 |
| Ad-hoc returns | As per RBI communication | SR 22 Note 2, 25 |
| CFSS implementation progress report to SSM | Quarterly | MSD 6 |
| Nomination coverage via DAKSH (NBFC-D) | Quarterly | MSD 12 |
| Serious auditor lapses report to DoS | Within 2 months of completion of annual audit | SA 8 |
| Early removal of SCA/SA to SSM/RO | Within 1 month of decision | SA 23 |
| MFI remediation plan to RBI | After 4 consecutive quarters below 60% | MFI 12 |
| DNBS11/12 (CICs), DNBS14 (P2P), PDR III/IV, Stress Test, IRS Test (SPDs) | Catalogue entries only (not targeted) | SR 21 items 8–9, 11, 13–16 |

### 8A.36.3 Product rules (Part 6)

| Product | Directions | Rule (cite) |
|---|---|---|
| All products (Part 6 item 4, "KYC level") | KYC | OTP-e-KYC NFTF onboarding is permitted only for term loans, with ≤ ₹60,000 aggregate sanction a year and full CDD within 1 year, after which no further debits are allowed (KYC 25(5)–(7)) |
| All | TDCR / SEC | Computed flags `securitisation_eligible` (SEC 5–8) and `transfer_eligible_from`, the MHP date (TDCR 43) |
| All products | CAP / SBR / DIV / MISC | Loans fully secured by deposits held 0% (CAP Sr (3)(c)); rupee rounding (MISC 27); cash disbursal per ss.269SS/269T (MISC 24); no fresh PDCs (MISC 23) |
| All products | GOV / OUT / ORM | Literature states that service providers (including for sales and marketing) may be used (OUT 55). Group cross-sell discloses the offering entity (OUT 46, 49). Tenants with a CRO: every product version needs CRO vetting before activation (GOV 23) |
| All products | MFI / IAF / SA / SR / MSD | Interest from actual disbursement or cheque handover; no full-month interest for part months; advance instalments reduce the interest base (MSD 7(1), (4), (5)); online transfer preferred to cheques (MSD 9) |
| 1, 3, 7, 12 (revolving / credit-line structures) | KYC | Must not be offered to customers onboarded through OTP-e-KYC in non-face-to-face mode (KYC 25(5)) |
| 1 Personal Loan; 2 Payday; 10 Consumer Durable | CAP / SBR / DIV / MISC | 125% RW as retail consumer credit (CAP 18(1) Sr (3)(e)(i)) |
| 2 Payday / Short-tenure | RBC / WD | KFS validity ≥ 1 working day for tenor < 7 days; APR on net disbursed amount by IRR (RBC 29(2)–(3)) |
| 2 Payday / Short-tenure | TDCR / SEC | Not securitisable: bullet repayment and residual maturity < 365 days (SEC 5(4)(v)–(vi)) |
| 3 Business / MSME Term Loan | RBC / WD | Floating-rate business loans to individuals and MSEs: no prepayment charge for UL, or for ML up to ₹50 lakh; BL per policy (RBC 34(2)); director/guarantor LWD check and covenant (WD 7(4), 19(1)) |
| 3 Business / MSME Term Loan | CAP / SBR / DIV / MISC | CGTMSE/NCGTC-guaranteed portion 0% up to the maximum permissible claim; residual at counterparty RW (CAP 18(2)(iv)) |
| 4 LAP / 5 Home Loan | RBC / WD | Document release in 30 days with ₹5,000/day and the 60-day lost-document clock; reset rules (RBC 31–32, 35–41) apply where the loan is a personal loan (para 6(11)); otherwise apply by policy |
| 4 LAP; 7 LAS | CAP / SBR / DIV / MISC | 100% by default; consumer-credit classification for loans to individuals per tenant policy [VERIFY: "consumer credit" undefined in CAP] (CAP 18(1)). No loans against own PDI or NCDs (CAP 12(14); MISC 11(6)) |
| 5 Home Loan | IRACP / RSA | UL teaser-rate housing 2% standard provision, falling to 0.40% one year after reset (IRACP 58); tenure extension to keep EMI unchanged only where repayment capacity holds; offer higher-EMI option (RSA 185–187) |
| 5 Home Loan | TDCR / SEC | RMBS MRR 5% (SEC 11). Securitisation MHP from the later of full disbursement and CERSAI registration (SEC 7) |
| 5 Home Loan | CAP / SBR / DIV / MISC | NBFC tenants 100% (excluded from 125%); HFC tenants use HFC Directions RWs (CAP 3(2)). Undrawn tranches: CCF 20% / 50% / 0% (CAP 18(4) Sr 9–10) |
| 5 Home Loan, 21 Project Finance, all multi-tranche products | MFI / IAF / SA / SR / MSD | EMI on disbursed amount only; revised amortisation schedule communicated on every part-disbursement (MSD 7(2)–(3)) |
| 6 Vehicle Loan | IRACP / RSA | If written as HP or lease, IRACP para 33 provisioning and recovery-record classification apply (IRACP 33, 43(7), 51(7)) |
| 6 Vehicle Loan | RBC / WD | Repossession clause: notice period, waiver, procedure, final chance to repay, return, sale/auction; copy to borrower (RBC 26–27) |
| 6 Vehicle; 9 Education; 11 Microfinance | CAP / SBR / DIV / MISC | 100% (excluded from 125%) (CAP 18(1) Sr (3)(e)(i)) |
| 8 Gold Loan | RBC / WD | Full RBC Ch III.G conduct (paras 43–75): assay certificate, custody, release, auction, compensation, unclaimed |
| 8 Gold Loan (bullet) | TDCR / SEC | Not securitisable (SEC 5(4)(v)) |
| 8 Gold Loan | CAP / SBR / DIV / MISC | 100%. Gold loans ≥ 50% of financial assets → gold_primary: Tier 1 ≥ 12%, CRAR ≥ 15% (CAP 4(8), 6(1)) |
| 11 Microfinance | RBC / WD | FPC display, loan card, no prepayment charge, overdue-only delay charges, rate display, designated-place collection, 09:00–18:00 window, harsh-practice list, recovery-grievance details (RBC 76–92) |
| 11 Microfinance | GOV / OUT / ORM | The loan agreement and the FPC (office, branch, website) carry a declaration that the NBFC is accountable for inappropriate behaviour of the service provider's staff and will provide timely grievance redressal (OUT 56) |
| 11 Microfinance | MFI / IAF / SA / SR / MSD | NBFC-MFI tenants: qualifying assets ≥ 60% of total assets net of intangibles, 4-quarter rule (MFI 8(3), 12); NPA > 90 days; provision floor = higher of 1% of portfolio, or 50% of instalments overdue 90–180 days plus 100% of instalments overdue ≥ 180 days (MFI 24–25); channelising-agent loans segregated, excluded from the test, CIC-reported (MFI 13). Non-MFI NBFCs: microfinance ≤ 25% of total assets (MFI 49). No pricing rules in 371; pricing stays under CF 60–61 |
| 12 Supply-chain / Invoice | TDCR / SEC | Revolving lines not securitisable (SEC 5(4)(i)). Trade receivables ≤ 12 months are eligible if the drawee repaid the last two within 90 days of due date (SEC 5 proviso). Factoring receivables are MHP-exempt for transfer if residual maturity ≤ 90 days (TDCR 43) |
| 12 Supply-chain / Channel; 20 Demand / Call | CAP / SBR / DIV / MISC | Undrawn limits CCF 20% (≤ 1 year) / 50% (> 1 year) / 0% if unconditionally cancellable (CAP 18(4)); bills discounted 100% (CAP 18(1) Sr (3)(f)). Factoring tenants follow MISC Ch IV (35–54) |
| 15 Resolution Finance | IRACP / RSA | See correction: tenant's own account = restructuring/evergreening (RSA 10(12), 169); own settlement > 3 months = restructuring (89); consent decree (100); cooling period ≥ 12 months (95) |
| 16 Debt Reset / Consolidation | IRACP / RSA | See correction: refinancing own stressed account = restructuring, sub-standard (RSA 10(12), 53, 189); viability test or evergreening (169, 188) |
| 17 Co-lending | RBC / WD | KFS Part 2 item 5: originating and partner RE, funding shares, blended rate (RBC Annex I) |
| 17 Co-lending | TDCR / SEC | NBFC share ≥ 10% (TDCR 102); blended rate (108); bank escrow (117); 15-day booking (113, 115); originator-only DLG ≤ 5% of CLA outstanding (123); next-working-day sync (124) |
| 17 Co-lending | CAP / SBR / DIV / MISC | Unrealised profit deducted from CET1/NOF until maturity (CAP 15(2)) |
| 18 Loans to entities | RBC / WD | Penal bars and new-venture bar (WD 7(3)); LWD board covenant (WD 7(4)); end-use monitoring measures (WD 19(2)) |
| 18 Loans to NBFCs / corporates | CAP / SBR / DIV / MISC | 100% (CAP 18(1) Sr (3)(b), (e), (g)); NBFC-share and group exposures above 10% of owned fund deducted (CAP 8(3), 10(i)) |
| 19 Staff loans | CAP / SBR / DIV / MISC | 0% RW (CAP 18(1) Sr (3)(d)) |
| 20 Demand / Call Loan; CC/OD variants | RBC / WD | Prepayment rules cover demand loans (RBC 34); CC/OD charge base ≤ sanctioned limit; no charge on intimated non-renewal (RBC 34(5)–(6)) |
| 21 Project Finance | IRACP / RSA | General provision by phase (IRACP 30); DCCO deferment ≤ 3 years infra / 2 years non-infra, cost overrun ≤ 10%, scope change ≥ 25% once, implementation within 180 days or immediate NPA, 0.375% / 0.5625% per quarter (RSA 111–119); credit-event CRILC reporting (RSA 106) |
| 21 Project Finance | RBC / WD | End-use certification by CAs plus own due diligence (WD 19(2)(iii)) |
| 21 Project Finance | TDCR / SEC | Transfer MHP runs from COD (TDCR 43) |
| 21 Project Finance | CAP / SBR / DIV / MISC | High-quality infrastructure: 75% after 2% / 50% after 5% of sanctioned project debt repaid, from 1 Apr 2026; grandfathering to next review/renewal or 31 Mar 2027 (CAP Sr (2)(e)) |
| MSME / business loans to proprietorships | KYC | Proprietor CDD plus two activity proofs, or one with contact-point verification (KYC 30–32) |

### 8A.36.4 Phase additions (Part 12)

| Phase | Directions | Addition |
|---|---|---|
| 0 | KYC | ADR on V-CIP hosting: tenant-exclusive owned/leased storage (cloud allowed), immediate transfer of recordings, vendor retains no data (KYC 27(1)(i)). Add the tenant's s.11A PML Act notification status (Aadhaar e-KYC authentication) to the Appendix B item 4 decision |
| 0 | GOV / OUT / ORM | ADR classifying Finbyx under OUT for each deployment model and each tenant layer (BL → CYB Ch III/IV; CYB 117 residual) (OUT 3(2), 5, 58). Standard MSA/DPA clause matrix against OUT 34, 74, 87–88 and 97(xvi). Add GOV, OUT and ORM to regulatory register v1, with ORM marked "guidance" |
| 2 | CAP / SBR / DIV / MISC | Extended entity_regulatory_profile and group tables (Part 8A.25) |
| 2 | GOV / OUT / ORM | Tenant-controlled keys (BYOK/HYOK, KMS/HSM) (OUT 97(vii)(b)). Break-glass access workflow with tenant-visible logs (OUT 24, 70). Tenant-isolation test suite (OUT 70, 97(vii)(c)). MFA and role-conflict matrix (OUT 97(viii)) |
| 3 | GOV / OUT / ORM | CRO vetting step in the product factory (GOV 23). ORM 47 heads in product approval. Service-provider and MFI declarations in templates (OUT 55–56) |
| 3b | RBC / WD | Language preference store; block dispatch when no approved vernacular template exists (RBC 10) |
| 4 | CAP / SBR / DIV / MISC | Capital-component tags in the chart of accounts (CAP 7–16) |
| 5 | CAP / SBR / DIV / MISC | Rupee-rounding policy at billing/posting (MISC 27) |
| 5 | MFI / IAF / SA / SR / MSD | Golden cases for each MSD para 7(1)–(5) scenario: cheque handover later than cheque date, EMI on a partially disbursed tranche, mid-month disbursal and repayment, advance EMI |
| 6 | KYC | *Applied in the Phase 6 instruction.* KYC flows per Part 8A.21; KYC REQ-IDs loaded into the register |
| 7 | RBC / WD | KFS unique proposal number, acknowledgement, Annex I Part 2 disclosures and the APR golden test (₹20,000 / 24 months / 15% / ₹400 fees → 17.07%) (RBC 29); vernacular sanction letter (RBC 13); LWD/large-defaulter gate (WD 7, 19) |
| 7 | CAP / SBR / DIV / MISC | rw_class, guarantee cover, cancellability flag and HQ-infrastructure data captured at sanction (CAP 18) |
| 8b | KYC | *Applied in the Phase 8b instruction.* Digital-KYC flow under KYC para 24 |
| 9 | IRACP / RSA | Illustration I golden test and +1 DPD convention (IRACP 19); Part A/B restructuring workbench and monitoring/specified-period tests (RSA 53–62, 159, 189–194) |
| 9 | RBC / WD | Prepayment engine incl. RBC 34(3)–(9) and 81; penal rules RBC 30; reset elections and quarterly statement (RBC 31); account-transfer request (RBC 19); rounding (RBC 103); release clocks 30/60 days (RBC 35–40) |
| 10 | CAP / SBR / DIV / MISC | PDC capture block where NACH is available (MISC 23) |
| 11 | RBC / WD | Contact engine for current RBC paras 89–100 (microfinance window under 91(2); para 100 excludes microfinance); Third Amendment rules behind [VERIFY: amendment text not supplied] |
| 12 | IRACP / RSA | Settlement rules (RSA 16, 86–100), cooling-period gate (95), consent decree (100), fraud/WD Board approval (16(5)(ii)) |
| 12 | RBC / WD | Wilful-defaulter workflow per WD paras 5–7, 10, 13–15, gated to ML+ tenants; pre-transfer gate (WD 14) |
| 13 | IRACP / RSA | IRACP rate tables (30, 32, 33, 48, 55, 58) and DLG ECL recompute (36A–36C); fair-value diminution, Sundry Liabilities account and RSA provisions (RSA 23, 48, 64, 118, 137, 198–211) |
| 13 | CAP / SBR / DIV / MISC | Owned fund / NOF / EPt computation; dividend eligibility checker; PDI, sub-debt and NCD private-placement controls (CAP 9–13; DIV; MISC 9–11) |
| 14 | IRACP / RSA | *Applied in the Phase 14 instruction.* CRILC monthly and the weekly Friday default report (RSA 20–21, 106) |
| 14 | RBC / WD | Monthly Annex I and Annex II CIC files with 30-day removal logic (WD 11–13, 18) |
| 14 | KYC | *Applied in the Phase 14 instruction.* FIU-IND, transaction-monitoring and sanctions-match reporting |
| 14 | CAP / SBR / DIV / MISC | "the RWA/CRAR and leverage engine (Part 8A.24) with lineage and the para 48 golden test; SBR applicability and group/UL calendar (Part 8A.25); MISC intimation clocks (Part 8A.27)" |
| 14 | GOV / OUT / ORM | Governance register and its returns (8A.28). Third-party and outsourcing register with half-yearly Board/RMC packs and ACB vendor-reconciliation ageing (8A.29). ORM suite (8A.30) |
| 14 | MFI / IAF / SA / SR / MSD | *Applied in the Phase 14 instruction.* Supervisory-return framework driven by the Part 8A.34 catalogue (SR 13–19) |
| 14 | MFI / IAF / SA / SR / MSD | *Applied in the Phase 14 instruction.* Applicability, periodicity and due dates from Part 8A.34 |
| 14 | MFI / IAF / SA / SR / MSD | Add bullets: the RBIA module (Part 8A.32); statutory-auditor register with Form A/B and branch-coverage report (Part 8A.33); PCA monitor and CFSS progress reporting (Part 8A.35); MFI qualifying-asset monitor and provision floor (Part 8A.31) |
| 15 | RBC / WD | Next-higher-level grievance disposal (RBC 7(2)); Second Amendment para 101Y feedback behind [VERIFY: amendment text not supplied] |
| P | GOV / OUT / ORM | *Incident-drill timing applied in the Phase P instruction (OUT para 61).* Add: an exit drill (full tenant export, re-import into a clean instance, purge certificate) (OUT 87–88, 97(xvi)); vendor assurance pack issued (OUT 30, 71; ORM 73); SOC log feed live (OUT 97(xi)) |
| 16 | TDCR / SEC | *Applied in the Phase 16 instruction.* Phase renamed "Partner connectors, co-lending, loan transfers and securitisation" |
| 16 | TDCR / SEC | *Applied in the Phase 16 instruction.* Originator-only DLG ≤ 5% of CLA outstanding (TDCR 123); website partner list (TDCR 126) |
| 16 | TDCR / SEC | *Applied in the Phase 16 instruction.* Loan-transfer engine (TDCR Part A) |
| 16 | TDCR / SEC | *Applied in the Phase 16 instruction.* Securitisation engine (SEC) |
| 16 | TDCR / SEC | *Applied in the Phase 16 instruction.* Investor-side securitisation module (SEC Ch V, 97–107) |
| 16 | CAP / SBR / DIV / MISC | Securitisation SEC-ERBA capital; DLG and co-lending capital deductions (CAP 15, 19–51) |
| 17 | RBC / WD | Gold conduct module (RBC 43–75), not only paras 60–66; vehicle repossession clause (RBC 26–27) |

### 8A.36.5 Decisions taken in v1.3 where the texts conflict or are silent

- **CRILC / DNBS09 applicability:** union of SR para 21 and RSA paras 7, 20–21 and 158, with a tenant toggle (M13 row).
- **Form A certificate:** mandatory for all NBFCs (SR para 21 item 20), even where SA para 3 lets NBFC-ND < ₹1,000 crore keep their extant auditor-appointment procedure.
- **CFSS:** MSD para 3 includes HFCs and Chapter II makes no HFC exclusion, so CFSS is built for UL/ML HFCs with ≥ 10 units unless the HFC Directions say otherwise [VERIFY].
- **Debarment registers:** WD 7(3) bars (1 year and 5 years after LWD removal) and FRM para 35 (5 years from full repayment) are evaluated separately at the M4 gate.
- **Loan transfer of fraud accounts:** TDCR paras 28 and 78 and FRM para 54 apply as cumulative gates.
- **DLG caps:** TDCR para 123 (CLA loans outstanding) and CF para 24 (amount disbursed) use different bases; keep separate ledgers.
- **IT outsourcing:** BL tenants with assets ≥ ₹500 crore follow CYB paras 60–64 (OUT Chapter IV does not apply to BL, OUT 3(2)); ML/UL tenants follow OUT Chapter IV alongside CYB Chapter V.
- **Grievance timelines:** OUT 57(3)–(4) cites the superseded 2021 scheme; M15 follows RBC and RB-IOS 2026.
- **KYC interpretations (label as interpretation in the register):** KYC 44(5) (first credit from the customer's own KYC-compliant account) is a configurable check for loan accounts, e.g. the first fee or EMI credit or penny-drop proof; KYC 71(5) (₹50,000 and above only by debit or cheque) is not read as covering loan-repayment collections, so cash EMI receipts are not blocked on that basis.
- **V-CIP hosting:** KYC 27(1)(i) ("own premises / own secured network") must be addressed by a Phase 0 ADR describing how tenant-exclusive storage on Finbyx SaaS hosting meets it.
- **Capital charges for securitisation:** SEC capital charges, the SRT test and clean-up call conditions rely on CAP; HFC risk weights come from the HFC Directions (not supplied) [VERIFY].


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
| Security | OWASP ASVS Level 2 baseline. VA at least every 6 months and PT at least every 12 months on production by an independent CERT-In-empanelled firm, plus pre- and post-go-live and after major change (CYB paras 121–124; DPS para 32). Incident notice to the tenant fast enough for its DAKSH filing within 6 hours of detection by Finbyx (CYB paras 28, 141; OUT para 61) |
| Accessibility | WCAG 2.2 AA for portals |
| Localisation | English + Hindi at launch; framework for regional languages; INR formatting (lakh/crore), DD-MM-YYYY |

## 10.4 Security and cyber controls (map to the 2026 Cyber Directions)

- **Encryption:** TLS 1.2+ (prefer 1.3) in transit; AES-256 at rest; field-level encryption for PAN, Aadhaar reference, bank account and DOB; KMS envelope keys per tenant; HSM for vault and signing keys. **Tenant-controlled keys (BYOK/HYOK: tenant-owned KMS key or HSM partition, with revocation) available to every ML/UL tenant**, because OUT para 97(vii)(b) requires encryption keys and HSMs under the NBFC's control for cloud services.
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

1. **Contract clauses** (OUT paras 33–34, 74(i)–(xix), 87–88, 97(xvi); CYB para 62 for BL tenants ≥ ₹500 crore). The standard Finbyx MSA/DPA carries all of them, with a clause matrix per tenant:
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
6. **Incidents:** the tenant's 6-hour RBI clock runs from **detection by Finbyx** (OUT para 61). Notify the tenant without undue delay (target ≤ 2 hours from Finbyx detection) for the contractually listed material adverse events (OUT 74(iii)); support forensics and RCA; take part in crisis drills; supply lessons-learned input (CYB paras 28, 140–146; ORM 99–101).
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
12. **Certifications:** keep ISO 27001 and SOC 2 Type II. They are not mandated, but a tenant may rely on globally recognised third-party certifications instead of its own audit, subject to its risk assessment (OUT para 79). Their scope must cover the OUT 97(xvii) heads. Offer pooled audits (OUT para 77).

**Finbyx's status under the Outsourcing Directions.** Hosted multi-tenant Finbyx is a cloud SaaS (OUT 96(1)(i)(c)) that delivers ASP, data-centre and cloud services (5(1)(iii)–(v)) and holds borrower data. For ML/UL tenants it is therefore **material IT outsourcing** (58(2)(i)–(ii)). The licence/subscription and OEM-maintenance exclusions (5(2)(v)–(vi)) can at most cover a dedicated deployment in the tenant's own account where Finbyx neither operates the system nor accesses its data; the tenant decides that (62(iii)) [interpretation]. BL tenants fall under CYB Ch III/IV instead of OUT Ch IV, and CYB 117 covers what OUT does not. **Design every deployment to the in-scope standard.** Existing contracts had to comply by renewal or 10 Apr 2026 (OUT 2), so all tenant contracts must comply now.

13. **Ownership/conflict declaration:**
   - Finbyx is not owned or controlled by a tenant's director, KMP, arrangement approver or their relatives, unless it is a group company or the tenant's Board grants an exception with disclosure (OUT 59, 13(iv)).
   - Infrabyx group tenants: Board policy, SLA, objective selection, arm's length and identical risk practice (90–92).
14. **Vendor assurance pack**, refreshed at least annually (OUT 30, 38, 71, 80):
   - financials, track record, reputation, litigation and complaints;
   - staff and subcontractor vetting;
   - security and internal controls, audit coverage and BCM;
   - infrastructure and DR;
   - conflicts and data-segregation capability;
   - cyber risk assessment;
   - enforceability;
   - evidence of operational resilience at least equivalent to the tenant's (ORM 73).
15. **Sub-processors and supply chain:**
   - tenant prior consent before appointing or changing a sub-processor, with the full supply-chain list (OUT 34(iv), 74(xi), 82);
   - Finbyx contractually liable for subcontractors and nth parties (74(xiii); ORM 76);
   - back-to-back terms with cloud providers and OEMs (74(xviii));
   - CIA assessment of subcontractors (97(x)(d)).
16. **Access:** unrestricted access to data, logs, alerts and premises, including subcontractors, for the tenant, its auditors, RBI and competent authorities (OUT 34(ii), (vii), 74(ii), (xii), 81). Support pooled audits (77).
17. **Data:**
   - India-only storage (OUT 74(vi));
   - data inventory of what is captured, processed and stored (74(vii));
   - permitted-sharing list (74(viii));
   - lifecycle through to permanent erasure (97(ii));
   - NDA, with confidentiality surviving termination (34(xi), 74(xix));
   - preservation per the tenant's legal obligations (34(xii)).
18. **Multi-tenant isolation:** only tenant-authorised personnel access tenant data (OUT 26–27, 70, 97(vii)(c)). Finbyx staff use break-glass, need-to-know access only, every access logged and visible to the tenant (24, 69(i)).
19. **Keys and access:**
   - tenant-controlled keys/HSM (OUT 97(vii)(b));
   - IAM with RBAC for user and privileged access, an SoD role-conflict matrix and least privilege;
   - **MFA** (97(viii)).
20. **SOC:** log and event export to the tenant's SOC (SIEM feed), with log retention (OUT 97(xi)). If Infrabyx offers a SOC service, meet para 95.
21. **SLAs:** a monitoring dashboard covering uptime, availability, performance and incident response, plus KRIs (OUT 74(v), 75, 64(4)).
22. **Incidents:** contractual list of material adverse events (OUT 74(iii)); notice measured from Finbyx detection (61); breach/leakage disclosure (25, 28, 69(iii)).
23. **BCP/DR:**
   - documented and tested, with joint tests (OUT 40, 83; ORM 79, 82);
   - CSP-level DR drills (97(xv));
   - "essential personnel" on site during exigencies (74(xvii)).
24. **Exit:**
   - orderly transfer (OUT 74(xv)) and full cooperation with the incoming provider (88);
   - **no erasure or alteration of data during the transition** (87);
   - **complete export in documented formats** (ledger, loans, documents, audit trail, configuration) within agreed turnaround times;
   - secure purge with an independent-assurance certificate (42, 97(xvi)).
25. **Continuity:** cooperation in the tenant's insolvency or resolution (OUT 74(xvi)). Records stay available even if Finbyx is liquidated (43, 53(iii); CYB 105 escrow).
26. **RBI directions:** comply with RBI directions on the outsourced service (OUT 74(xiv), 47(v)).
27. **No core management functions for tenants** (OUT 15):
   - no Finbyx-staff role can sanction loans, decide KYC compliance, perform internal audit or compliance, or manage investments;
   - BRE and auto-decisions run only on tenant-approved rule versions, attributed to the tenant's authority;
   - Udofin is bound by the same limits.
28. **Grievances:** Finbyx and Udofin route customer complaints to the tenant's GRO and never close them (OUT 54–57, 98–99).
29. **ORM inputs for tenants:**
   - RTO, RPO, data-loss and service-level metrics for each Finbyx-supported critical operation (ORM 33);
   - Finbyx RCSA;
   - post-incident lessons-learned reports (ORM 99–101).
30. **Certification scope** covers OUT 97(xvii) (OUT 79).

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

Maintain a **golden test-case library**, approved by me and our finance/compliance reviewers, of worked numerical examples (EMI, broken-period interest, prepayment, bounce, IRACP Illustration I day-end dates, NPA upgrade, borrower-level contagion, HP/lease provisioning, restructuring downgrade/upgrade, EIR, GST). Every release must pass it.

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
- Each phase also includes the v1.3 additions listed for it in **Part 8A.36.4**. Add them to the phase specification before approval.

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
| 14. Regulatory reporting, risk and compliance | CIC UCRF, CIMS returns (SR return catalogue), CRILC/DNBS09/FMR as applicable, FIU-IND, ALM, concentration, ICAAP mart, compliance module, LawDocsComply bridge | 9, 13 |
| 15. Grievance, borrower portal and feedback | Complaints, Internal Ombudsman, RB-IOS 2026, Equator referral (re-using the Phase 12 ODR adapter), borrower portal, feedback | 3b, 9, 12 |
| **P. MVP hardening and pilot go-live** | E2E, independent VAPT, COB load test, DR restore drill, India-region production cut-over for the two MVP products | 0–15 (Phase 14 only for the returns that apply to the pilot's layer) |
| 16. Partner connectors, co-lending, loan transfers and securitisation | Full LSP framework, DLG ledger, co-lending/DA/securitisation engine, partner portals | 8c, 9, 10, 13, 14 |
| 17. Secured products expansion | LAP/Home, Vehicle, Gold, LAS/LAMF templates; collateral flows; SARFAESI; repossession and auction | P, 12 |
| 18. Analytics, AI layer and MCP | MIS catalogue, BI embedding, governed AI copilots, read-only MCP server | P |
| 19. Migration tooling | Legacy loan boarding and reconciliation sign-off | 9, 13 |
| 20. Scale hardening and AWS migration | Multi-tenant scale tests, AWS ap-south-1 / ap-south-2 migration, DR at scale, performance tuning | P, 16–19 |

### Phase 0 — Repository audit and architecture

> **Instruction to Claude:** "Read docs/00-master-prompt.md in full (Parts 1–13, Appendices A–F and Sources). Inspect the connected repository, branch, files, Git status and tooling, and report them. Do not write application code and do not modify the repository yet. Produce:
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
> - KYC flows per Part 8A.21 (CKYC search/download/upload with 10/7-day clocks, Aadhaar mode selection by s.11A status, OKYC/DigiLocker, PAN/Form 60, V-CIP, OVD and deemed-OVD capture, BO thresholds, NFTF EDD, para 25 limits);
> - sanctions and PEP screening;
> - the periodic-updation scheduler.
>
> Adapters: mock first, then a Surepass sandbox adapter behind `KycProvider`. Never store the full Aadhaar number unless the vault design approved in Phase 0 meets UIDAI Circular No. 14 of 2025. Prefer OKYC/DigiLocker flows that avoid storage. Load the KYC REQ-IDs from Part 8A.21 into the register."

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
> - the KFS/APR engine per RBC para 29 and Annex I, with the KFS **validity period** (≥ 3 working days, or ≥ 1 for tenor < 7 days). This is not a waiting period. Include the unique proposal number, the Part 2 disclosures and the APR golden test (₹20,000 / 24 months / 15% / ₹400 fees → 17.07%; RBC para 29(3)).
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
> - assisted KYC and document capture, including the KYC para 24 digital-KYC flow (live photo with watermark, officer-mobile block, dual OTP; Part 8A.21);
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
> - part-prepayment and foreclosure quotes with the prepayment-charge engine (RBC paras 33–34, 81);
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
> - the effective-dated contact-policy engine from Phase 3b (current RBC paras 89–100; paras 100A–100AB from 1 Jan 2027 [VERIFY: Third Amendment text not supplied]);
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
> - the wilful-defaulter workflow (WD paras 5–7, 10, 13–15; Part 8A.20), with monthly Annex I/II CIC files, penal-measure clocks and the pre-transfer wilful-default gate;
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
> - the supervisory-return framework (online portal/CIMS formats per return spec), driven by the data-driven return catalogue in Part 8A.34, with reconciliation to GL, recorded aggregation rules, DQ metrics and ad-hoc subset queries (SR paras 13–19); start with the returns that apply to the pilot tenant's layer;
> - CRILC monthly and the weekly Friday default report / DNBS09 (RSA 20–21, 106; SR 21–22; M13 row);
> - the fraud module's per-case FMR/FUA, law-enforcement reporting, closure and RBR (Part 8A.14);
> - FIU-IND reports, transaction-monitoring alerts and sanctions-match reporting (Part 8A.21);
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
> Take return applicability, periodicity and due dates from Part 8A.34; take formats and validation rules from the RBI portal for each return."

### Phase 15 — Grievance, borrower portal and feedback

> **Instruction to Claude:** "Build:
>
> - the complaint management system, with automated Internal Ombudsman escalation where applicable, and RB-IOS 2026 support;
> - Equator referral, re-using the Phase 12 ODR adapter;
> - the AI support assistant, restricted to approved sources;
> - the optional borrower self-service portal;
> - feedback (CSAT/NPS, plus sales feedback within 30 days under RBC para 101Y [VERIFY: amendment text not supplied]).
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
> - an incident drill proving that tenant notification fits a 6-hour RBI/DAKSH filing measured from Finbyx's own detection timestamp (CYB paras 28, 141, 146; OUT para 61);
> - a data-residency check of every environment and sub-processor;
> - a production runbook;
> - a migration and cut-over plan;
> - a controlled go-live checklist for my approval.
>
> Do not deploy to production without my explicit authorisation."

### Phase 16 — Partner connectors, co-lending, loan transfers and securitisation

> **Instruction to Claude:** "Extend the Phase 8c connector into the full LSP/channel-partner framework (Part 5). Add:
>
> - the DLG ledger (≤ 5% of the amount disbursed out of the covered portfolio, invoked within 120 days overdue);
> - the collection-agent appointment model, kept separate from DLG;
> - the CIMS DLA register;
> - the co-lending engine (10% retention, 15-day booking, bank escrow, blended rate, next-working-day classification sync, each lender's own CIC reporting, originator-only DLG ≤ 5% of CLA outstanding (TDCR 123), website partner list (TDCR 126));
> - the loan-transfer engine (TDCR Part A): MHP, one-third DD/10% retention, no re-acquisition, 30-day replacement, stressed-loan sale with valuation and Swiss challenge, ARC/SR accounting, trade-reporting database;
> - the securitisation engine (SEC): eligibility, MRR, 20% cap, SPE checks, CE/liquidity/servicing facilities, STC checker, Annex I and quarterly RBI report;
> - the investor-side securitisation module (SEC Ch V, paras 97–107);
> - partner portals."

### Phase 17 — Secured products expansion

> **Instruction to Claude:** "For each secured product (LAP/Home, Vehicle, Gold, LAS/LAMF):
>
> 1. produce the product spec and feasibility notes;
> 2. implement the collateral workflows (M5), integrations and regulatory checks;
> 3. build SARFAESI (with the NBFC eligibility gate), repossession and auction, including the gold release, auction, compensation and unclaimed-collateral rules (RBC paras 58–72) and the vehicle repossession clause contents (RBC paras 26–27)."

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
- Commit only `CLAUDE.md` (from Appendix A), the ADRs, `docs/`, the registers and `docs/regulations/errata.md` (seeded from Appendix F). Application scaffolding belongs to Phase 1.
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
  over any other citation. ORM IDs are guidance, not Directions. Drafting slips: docs/regulations/errata.md.

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
  - tenant, legal_entity, entity_regulatory_profile (category, layer and source, standalone/last-audited/group assets, ₹1,000 crore crossing date, public_funds, customer_interface, government_company, gold_primary, UL advice and milestones, NOF and glide path, PBC result, Ind AS flag; Part 8A.25);
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
- **Added in v1.3 (Part 8A.17–8A.36):**
  - IRACP: classification_event (borrower, COB date, from/to class), npi_flag, impairment_reserve_appropriation, hp_lease_nbv_snapshot, teaser_reset_record
  - RSA: resolution_plan, ica_record, ice_rating, monitoring_period_tracker, financial_difficulty_flag, fair_value_diminution, fitl_instrument, sundry_liability_interest_cap, settlement_policy_version, cooling_period, technical_write_off, consent_decree, dcco_deferment, drs_claim
  - RBC: kfs_version (proposal_no, validity_expiry, acknowledgement), kfs_charge_line, apr_computation, penal_levy, rate_reset_event, reset_election, quarterly_statement, prepayment_decision, document_release_case, gold_assay_certificate, surprise_verification, auction_notice, gold_auction, unclaimed_collateral, mfi_loan_card, agent_authorisation, agent_verification, telemarketer_registration, account_transfer_request, language_preference
  - WD: wd_case, wd_committee, wd_committee_member, wd_notice (show-cause / proposal / order), wd_hearing, lwd_entry, large_defaulter_entry, wd_cic_file, wd_penal_bar, end_use_certificate, auditor_complaint, third_party_report
  - KYC: ucic, kyc_mode_evidence, digital_kyc_session, vcip_session (recording ref, geo, IP check, auditor sign-off), beneficial_owner_link, pep_approval, kyc_exception, periodic_updation_notice, ckycr_upload_job, ckycr_inbound_update, sanctions_list_version, sanctions_match_case, asset_freeze_order, aml_alert, fiu_report, ml_tf_risk_assessment, pmla_officer_register, darpan_registration, fatca_crs_status
  - **TDCR:** loan_transfer (assignment/novation/participation, stressed flag), transfer_item, retained_interest, mhp_check, dd_record (loan-level/portfolio-level), transferee_declaration, rep_warranty_claim, regulator_notice, valuation_report, swiss_challenge, bid, arc_transfer, security_receipt, sr_valuation, trade_report, cla_agreement, cla_share, cla_booking_clock, cla_escrow, cla_classification_sync, cla_dlg
  - **SEC:** securitisation_txn, spe, tranche, mrr_position, credit_enhancement, ce_reset, liquidity_draw, underwriting_devolvement, investor_report, annex1_disclosure, securitisation_investment
  - **CAP:** capital_component_map, capital_run, rwa_exposure_line, rw_class_master, ccf_master, guarantee_scheme_cover, offbs_commitment, securitisation_tranche, tranche_rating, derivative_contract, netting_set, cds_position, pdi_instrument, subdebt_instrument
  - **SBR:** group_entity, group_asset_certificate, ul_classification_event, nof_glidepath_check, pbc_test_run, fatf_investor_holding; entity_regulatory_profile fields per 8A.25 (category, layer and source, standalone/last-audited/group assets, ₹1,000 crore crossing date, public_funds, customer_interface, government_company, gold_primary, UL advice and milestones, NOF and glide path, PBC result)
  - **DIV:** dividend_declaration, dividend_eligibility_check
  - **MISC:** regulatory_intimation, rating_event, ncd_issue, ncd_subscriber, factoring_receivable
  - **GOV:** director, director_declaration (annex_i / annex_ii / annual), deed_of_covenant, nrc_decision, director_change_event, management_change_application, kmp_record, cro_appointment, governance_return, policy_document, whistleblower_case
  - **OUT:** third_party, outsourcing_arrangement, materiality_assessment, due_diligence_review, contract_clause_check, sp_audit, sp_certification, sp_incident, supply_chain_entity, exit_plan, termination_notice, conflict_declaration
  - **ORM:** orm_taxonomy, risk, control, rcsa, kri, kri_observation, op_loss_event, critical_operation, impact_tolerance, dependency_node, dependency_edge, scenario_test, bcp_plan, bcp_exercise, incident, lessons_learned, action_plan, sensitive_position_leave, conduct_attestation
  - MFI: mfi_qualifying_asset_test, channelising_scheme, sro_membership
  - IAF: audit_universe_unit, ia_risk_assessment (inherent, control, level, trend, parameters), audit_plan, audit_assignment, audit_report, audit_observation, observation_compliance, hia_register, acb_hia_meeting
  - SA: audit_firm, auditor_appointment (term_no, start, end, cooling_off_until), auditor_eligibility_check, form_a_certificate, form_b_certificate, non_audit_service_log, auditor_performance_review, branch_coverage_run
  - SR: return_catalogue_entry (code, periodicity, reference_rule, due_rule, applicability_rule, mode), return_due_instance, return_submission, return_reconciliation, aggregation_rule, dq_metric, dq_issue, adhoc_data_request
  - MSD: pca_indicator_snapshot, pca_restriction, cfss_progress_report, deposit_nomination; entity_regulatory_profile flags nbfc_mfi, cic, p2p, spd, factor, aa, mgc, group_asset_size, pca_status, sro_membership, mumbai_region; branch flag fixed_point_unit

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

## E.3 v1.2 → v1.3 (18 October 2026): further official RBI texts supplied by the project owner

v1.3 checks the prompt against the official text of 18 further Directions and 1 guidance note: IRACP 356, RSA 357, RBC 362, WD 358, KYC 361, TDCR 352, SEC 353, CAP 345, SBR 339, DIV 360, MISC 373, GOV 344, OUT 363, ORM (guidance note), MFI 371, IAF 464, SA 465, SR 466 and MSD 467. Part 8A.17–8A.35 hold the paragraph-level requirements; 8A.36 holds the consolidated build additions; Appendix F lists the drafting slips. The corrections to earlier text are:

| # | Area | v1.2 statement (withdrawn) | v1.3 correction (source) |
|---|---|---|---|
| 1 | DPD | DPD = business date − oldest overdue due date | DPD = COB date − oldest unpaid due date + 1 (IRACP 19, Illustration I) |
| 2 | COB classification | Borrower-level classification across co-lending partners and group entities | Borrower-wise within the tenant, including NPI; co-lending sync per M11 (IRACP 23) |
| 3 | Settlements with wilful defaulters | "Settlement restrictions for wilful defaulters" [VERIFY] | Permitted, with Board approval in every case; criminal proceedings and penal measures continue; restructuring is barred (RSA 16(5)(ii), 83–85, 97–98) |
| 4 | CRILC scope | UL/ML and BL ICC/MFI/Factor ≥ ₹500 crore | NBFC-D and NBFC-ND ≥ ₹500 crore, and any NBFC-Factor; monthly ≥ ₹5 crore plus weekly Friday report (RSA 7, 20–21, 158) |
| 5 | HFC scope | Restructuring for all tenants per RSA | HFCs: only RSA paras 86–138; HFC restructuring per HFC Directions [VERIFY] (RSA 5) |
| 6 | OTS closure | "Closed: settled (OTS)" | Settlement paid over more than 3 months, or part settlement, is restructuring until paid (RSA 89–90) |
| 7 | Gold release compensation | "delay compensation [VERIFY amount and para]"; Ch III.G "paras 42–75" | ₹5,000/day beyond the 7-working-day timeline if attributable to the lender (RBC 69); para 42 deleted w.e.f. 1 Apr 2026; assay certificate, auction district rule, related-party bar, surplus refund within 7 working days, unclaimed after 2 years (RBC 43–75) |
| 8 | Penal charges | "RBC para 30 [VERIFY]" | Verified: only on the amount under default, no penal on penal, individual ≤ non-individual, shown in reminders (RBC 30) |
| 9 | Resets | Applies to EMI personal loans only | Also equated-instalment loans of any periodicity, external or internal benchmark; switch to fixed only where the Board policy offers it; quarterly statement contents (RBC 31–32) |
| 10 | Prepayment | Based on the 2 Jul 2025 Pre-payment Charges Directions; layer rules only | RBC 33–34 and 81 incl. source of funds, dual-rate, CC/OD, lender-initiated, undisclosed and waived charges |
| 11 | Document release | 30 days and ₹5,000/day for all loans | Personal loans (RBC 6(11)); 60-day clock for lost documents; choice of office; legal-heir procedure (RBC 35–41) |
| 12 | Recovery agents | Paras 89–100 shown as one general set | Para 100 excludes microfinance; paras 93–97 sit in the microfinance section; paras 98–100 bind P2P too (RBC 4, 93–100) |
| 13 | RBC amendments | Second and Third Amendment cited as verified | Not in the supplied copy (updated to 1 Apr 2026) [VERIFY: amendment text not supplied] |
| 14 | Wilful defaulters | "Directions, 2025 [VERIFY]"; generic workflow | Verified: ML+ only, all-RE gate, ₹25 lakh/₹1 crore thresholds, 6-month deadline, 21/15-day windows, hearing without lawyers, monthly Annex I/II, 30-day removal, settlements, transfer gate (WD 2–21) |
| 15 | Wilful-defaulter settlements | "settlement restrictions … [VERIFY]" | LWD removal only on full payment of the compromise amount; RSA conditions apply (WD 13) [VERIFY RSA text] |
| 16 | KYC/AML | "KYC Directions and 29 Dec 2025 amendment [VERIFY]"; "STR within 7 working days; CTR/CCR/NTR monthly"; generic V-CIP, CKYC and updation bullets; "PMLA: 5 years after relationship end" | Paragraph-level KYC requirements (Part 8A.21): CKYCR upload in 10 days, updates in 7 days, and the reliance Explanation (KYC 63); 2/8/10-year updation with 3+3 notices (42); 6-monthly risk review (41); OTP-e-KYC NFTF loans: term loans only, ≤ ₹60,000 a year (25); full V-CIP standard (27); daily sanctions screening and freeze (54–57); retention split between transaction and identification records (47). FIU-IND timelines are in the PML Rules, not the Directions [VERIFY] |
| 17 | M11 co-lending DLG | "DLG only by the originator, capped at 5% [VERIFY …]" | Originating NBFC only, ≤ 5% of loans outstanding under the CLA, mutatis mutandis CF (TDCR 123) |
| 18 | M11 / Product 17 retention | "minimum 10% retention by each lender" | Each NBFC party retains ≥ 10% of each individual loan (TDCR 102) |
| 19 | M11 DA | "buy-back and clean-up" | No re-acquisition except under a resolution plan; replacement only for reps/warranties within 30 days (DA) or 120 days (securitisation) (TDCR 17, 52; SEC 30) |
| 20 | M11 DA source | "Securitisation Transactions Directions … and the transfer provisions [VERIFY]" | DA is under TDCR Part A (352); securitisation under SEC (353) |
| 21 | M11 accounting | "de-recognition tests under Ind AS 109" | Cash sale; Ind AS and ICAI advisories; unrealised profit off CET1/NOF; non-Ind AS unrealised-gain account (TDCR 38, 45, 72; SEC 31–34) |
| 22 | Part 8.2 | Co-lending row citing the 6 Aug 2025 Directions only | Full TDCR Part A + Part B row (352) |
| 23 | Part 8.2 | Securitisation row "MHP/MRR, pools, servicing" | Full SEC control list (353) |
| 24 | Scale-based regulation | "as amended 2026 (Upper Layer threshold of ₹1 lakh crore assets; Unregistered Type I NBFC category)" | Supplied copy is the original 28 Nov 2025 text: UL by parametric scoring plus top-10 rule; no Type I category. Any 2026 amendment [VERIFY] (SBR 24–26) |
| 25 | Capital | CRAR, Tier 1/Tier 2 and RWAs "[VERIFY — not yet supplied]" | Full RWA/CRAR engine: minimums by profile, capital elements and deductions, RW/CCF tables, guarantee schemes, CEM, SEC-ERBA, BL leverage ≤ 7; no CCB or Pillar 1 op/market risk charge (CAP 6–54) |
| 26 | ICAAP | Generic ICAAP mart | ML and above only; Pillar 2 capital not insisted upon (CAP 54) |
| 27 | Post-dated cheques | Fineract PDC pattern unqualified | No fresh PDCs/EMI cheques alongside NACH; CTS-2010 only where NACH is unavailable (MISC 23) |
| 28 | Rounding | Nearest-rupee rounding "where RBC para 103 requires it [VERIFY scope]" | All transactions, all layers incl. HFC and CIC (MISC 27; RBC 103) |
| 29 | Dividends; Miscellaneous | Not covered | DIV and MISC added (Parts 8A.26–8A.27) |
| 30 | Outsourcing | Register "as required by the Outsourcing Directions [VERIFY]"; contract clauses "[VERIFY]" | OUT 363 verified: 10 Apr 2026 deadline for existing IT contracts; non-outsourceable functions; clause lists 34/74; 6-hour clock from provider detection; NBFC-controlled keys; exit and purge; Finbyx obligations (Part 10.6 items 13–30) (OUT 2, 15, 34, 61, 74, 97) |
| 31 | CF third-party reference | "[VERIFY which is current]" (CF 6(6) vs 62(2)) | No "Third-Party Dependencies" Direction; 62(2) is a slip; OUT 363 applies (OUT 1) |
| 32 | Governance | Not covered | GOV 344: director fit and proper, quarterly statement, 30% change approval, CRO, KMP and independent-director limits, governance register (GOV 8–43) |
| 33 | Operational risk | "Guidance Note … [VERIFY 2025 version]" | Guidance Note of 28 Nov 2025 (DOR.ORG.REC.301), guidance status: critical operations, impact tolerances, mapping, scenario testing, lessons learned (ORM 31–33, 42, 69, 101) |
| 34 | Incident notice | Tenant notice "fast enough for its DAKSH filing within 6 hours" | The 6-hour clock runs from detection by the service provider (Finbyx) (OUT 61) |
| 35 | Supervisory returns | "CIMS / XBRL returns … sectoral, branch info … [VERIFY the full return list]" | 20-item catalogue from SR para 21, no branch-info or sectoral return, no XBRL in the Directions; due dates per paras 22–23 (SR) |
| 36 | ALM returns | "para 58 still cites the 2024 Directions [VERIFY against 2026]" | SR 2026 timelines apply: DNBS04A 21 days, DNBS04B 15 days (SR 21–22) |
| 37 | DNBS04A/04B applicability | "the ₹100 crore test applies to every layer" | UL; ML except SPDs; BL ≥ ₹100 crore solely or at group level, excluding no-public-funds/no-customer-interface NBFCs, NOFHCs, P2Ps, AAs, MGCs (SR 21 item 4) |
| 38 | Large Exposure return | "monthly Return on Large Exposures" | Quarterly within 21 days (SR 21 item 12) [VERIFY vs CON Annex I] |
| 39 | Interest charging | "No EMI on undisbursed amounts (Finbyx design rule)"; "Design rules beyond para 7" | Regulatory requirements: MSD para 7(2) (EMI on disbursed amount) and 7(3) (schedule change communicated on each part-disbursement) |
| 40 | MFI | No NBFC-MFI prudential rules | 60% qualifying assets, 4-quarter rule, CRAR 15%, provision floor, 25% cap for non-MFIs (MFI 8(3), 12, 16–17, 24–25, 49) |
| 41 | Internal and statutory audit, PCA | Not covered | IAF, SA and MSD Ch V added (Parts 8A.32, 8A.33, 8A.35) |

**Still unverified after v1.3:**

- RBC Second and Third Amendment Directions, 2026 (including paras 100A–100AB, 100P, 100Y(5), 101N(4) and 101Y cited in E.1 row 6 and Part 12): the supplied RBC copy is dated 1 Apr 2026, so these remain [VERIFY].
- SBR: the ₹1 lakh crore UL threshold and the "Type I NBFC" category are not in the supplied 339 copy.
- HFC Directions, Internal Ombudsman Directions, RB-IOS 2026, the PPG.66 repeal circular and PML Rules rule 8 (FIU-IND timelines) have not been supplied.

---

# APPENDIX F — DRAFTING SLIPS FOUND IN THE SUPPLIED RBI TEXTS

Seed `docs/regulations/errata.md` from this list (Part 8A.0.1 rule 5). For each slip, implement the evident intent, record the interpretation, and re-check it when RBI issues a corrected or amended text. The v1.2 examples are in Part 8A.0.1 rule 5.

**IRACP / RSA**

- IRACP para 32(2)(i) says "NBFC-BL" in a Chapter II (all-NBFC) rule.
- IRACP para 5 repeats "with these Directions".
- RSA para 23 table: the last row repeats "secured portion" (evidently "unsecured portion").
- RSA para 66 cites para 63 for the additional specific provisions (evidently para 64).
- RSA para 72 cites para 70 for the freeze period, which is set in para 69.
- RSA para 84 contains the artefact "_bookmark20".
- RSA para 108 says CRILC instructions "as per paragraph 107", which covers consortium intimation.
- RSA para 138 is truncated in the official PDF (text reads only "A").
- RSA Part B uses "compromise settlement" without defining it (definition is Part A para 10(2), not applied by para 157).

**RBC / WD**

- RBC para 37: "sanction letters issued on or December 1, 2023" (word "after" missing).
- RBC para 31(3) Note: "where such an option is provided by the bank" (should read NBFC).
- RBC para 43: unclosed parenthesis "(and timeline for serving an auction notice…".
- RBC para 6(9): defines microfinance loan by reference to an "NBFC – Microfinance Institution Directions, 2025", whereas microfinance rules sit in CF Ch V [VERIFY].
- RBC paras 89–97 (recovery and agent rules) sit under Section H (microfinance), while para 100 excludes microfinance loans; the general agent rules are in paras 98–100 only.
- WD Annex I field 10: valid values list "01 - Suit filed" and "– Non-Suit Filed" without the code "02" (Annex II shows 02).
- WD Annex I: field 11 uses "SUBST" and field 12 uses "SUBSTD".
- WD Annex II: field numbering skips 17 (16 → 18).
- WD para 5(15) requires non-whole-time/independent/nominee directors to be flagged in Annex II, but Annex II has no such field, and the Annex I note excludes them.
- WD para 3(1)(xii)(e): cites the SBR "Guidelines, 2025" (the instrument is a Directions).
- WD para 21(1): cites the "Fraud Risk Management in NBFCs Directions, 2024" (now RBI/DoS/2026-27/463, 2026).

**KYC**

- KYC para 23 proviso (v) and para 27(2)(vi)(c) refer to "paragraph 62" for CKYCR. CKYCR is para 63; para 62 is FCRA.
- KYC para 63(7) refers to "clauses (5) and (6)" for the 1 Apr 2017 / 1 Apr 2021 cut-off dates; they are in clauses (4) and (5). It also cites a "clause (10)" that does not exist (para 63 has nine clauses).
- KYC para 28(vi)–(vii) say "Directions (4) and (5)" where they mean clauses (iv) and (v) of para 28.
- Annex I (MHA UAPA Order) numbering skips para 3.3; the Order also cites "Para 4(i)" and "Paragraph 5 (i)", which do not exist in that form. These are reproduced Government text; no software impact.

**TDCR / SEC**

- **TDCR para 2, second proviso vs para 96:** para 2 defines existing CLAs as those "executed before August 06, 2025"; para 96 says "executed before the date of issuance of these Directions" (28 Nov 2025). Implement: CLAs entered into before the effective date follow the earlier rules, and record both dates.
- **TDCR para 83 proviso:** cross-refers to "sub-clause (a)", but the items are numbered (i)–(iv). It is a legacy 2021 transition running to FY 2025-26.
- **TDCR:** paras 1–2 read "Reserve Bank of India of India"; para 95 refers to "a RE"; para 92(2) has "perspective buyers".
- **SEC para 84(3):** reads "rest" for "reset".
- **SEC para 114:** omits "2025" from the FS Directions title.
- **SEC para 4(10) vs TDCR para 12(4):** the SEC AIFI list omits NaBFID; TDCR includes it. Treat as intended; do not harmonise.

**CAP / SBR / DIV / MISC**

- CAP 12(8)(iii) refers to "paragraph 8(i)" (para 8 is CET1 deductions); the intended cross-reference is within 12(8).
- CAP 18(9)(iii) refers to "8(i) and 8(ii)"; it means 18(9)(i)–(ii).
- CAP 50 refers to "paragraph 44" for the thickness adjustment; the formula is in para 45.
- CAP 18(1) places the Sr (2)(e) infrastructure loans under the "Investments" heading.
- DIV para 3 numbers item (x) twice; para 11 numbers item (i) twice; para 7 says "this Master Direction".

**GOV / OUT / ORM**

- CF para 62(2) cites a "Reserve Bank of India (NBFCs – Management of Third-Party Dependencies) Directions, 2025". No such Direction exists; the correct reference is OUT 363 ("Managing Risks in Outsourcing"; para 1), which CF para 6(6) cites correctly.
- GOV para 17(2) takes the IS audit periodicity from the Outsourcing Directions, which prescribe none. Use CYB para 56 for BL ≥ ₹500 crore (at least once a year, preferably before the statutory audit); ML and above set the periodicity in their IS Audit Policy (CYB para 150).
- OUT para 4(2)(i) and para 5(1) cross-refer to para 58(1)/(2) "above"; para 58 comes later.
- OUT para 6(2) defines "Group" by reference to the Reserve Bank of India (Commercial Banks – Concentration Risk Management) Directions, 2025, not the NBFC Directions. NBFC CON 351 contains no "group" definition [VERIFY the Commercial Banks text].
- OUT para 57(4) cites the RBI Integrated Ombudsman Scheme, 2021, which RB-IOS 2026 has superseded (effective 1 Jul 2026) [VERIFY: RB-IOS 2026 text not supplied].
- The ORM Guidance Note's RBI number is printed blank ("RBI/2025-26/") in the supplied copy.

**MFI / IAF / SA / SR / MSD**

- SA para 23: "the outgoing SCAs / SAs **of the bank**" in NBFC Directions.
- IAF para 29 uses a 3-level risk scale (high, medium, low). Para 34 uses 5 levels (low, medium, high, very high, extremely high). Make the scale configurable.
- ALM para 58 cites the "Reserve Bank of India (Filing of Supervisory Returns) Directions, 2024". Use SR 2026 instead.
- CON Annex I is headed "Return for the Month" and para 48(4) says "10 largest exposures". SR para 21 item 12 lists the LE Framework return as quarterly, with the "20 largest exposures".
- SR para 21 table: DNBS09 shares CRILC's merged applicability cell, and FUA and FMR4/RBR share FMR's merged cell. Plain-text extraction loses this; confirmed from the PDF (pp. 8, 10–11).

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
  - Official texts of the 33 Directions and 1 guidance note in Part 8A, supplied by the project owner: docs/regulations/rbi/
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
