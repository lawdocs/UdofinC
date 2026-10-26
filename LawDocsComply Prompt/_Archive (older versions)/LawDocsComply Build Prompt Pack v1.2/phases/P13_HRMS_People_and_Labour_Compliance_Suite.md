# Phase P13 — HRMS, People and Labour Compliance Suite

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, ledger, Object Lock), P01 (identity, SCIM, step-up), P02 (settings registry and rule-pack engine — payroll and labour parameters are rule packs, NN-26), P03/P04 (labour-law obligations as content packs and compliance instances), P06 (directors, KMP, committees — the people records are shared), P07 (DMS, eSign envelopes, policy acknowledgements).
>
> **Sequencing:** P13 starts after P06 sprint 2 (shared people model). Sub-iterations: **P13a** People core (org, employees, KMP/director link, lifecycle, documents, user provisioning) → **P13b** Time, attendance and leave → **P13c** Payroll on rule packs and statutory outputs → **P13d** Labour compliance (registers, returns, committees, POSH sealed module, employment agreements) → **P13e** People-risk metrics and ecosystem sharing. P13a must precede P04's role-assignment UX finishing (roles are assigned to employees). The suite is sold as a **standalone SKU** ("LawDocsComply People & Labour") and as an add-on inside the GRC subscription (P20 entitlements).
>
> **Binding appendices:** T (Labour Codes, registers, payroll parameters — the parameter seed), D (roles, SoD), A (state machines), B (data model), G (`LR-MOLE-*` rules), M (export), U (settings).
>
> **Requirements covered:** R-014, R-015, R-018, R-024, R-025, R-030, R-043, R-056, R-082, R-086, R-094, R-095, R-102 (labour questionnaires as Part 2 content), and the client-side parts of R-041/R-042 (staff HRMS for LawDocs staff itself is in the Infrabyx Operations Hub OH10, D-03).
>
> **Estimated effort:** 12 two-week sprints, squad of 9 (people core 3, time & leave 2, payroll 3, labour compliance 1 + content analyst). Payroll go-live for any tenant is gated on Appendix T parameter verification for that tenant's States.

>
> **v1.1 changes (25 October 2026)**
> - **CHRO** added as `ten_kmp` sub-type with HR approval authority and the People dashboard (D-48); approval matrix by value/grade (§3).
> - New **§4M fast self-service and approvals**: one-tap leave with live balance projection, auto-approval rules for low-impact requests, conflict warnings, bulk attendance regularisation with undo (NN-49), letters on demand, HR help desk (FR-P13-53–FR-P13-58).
> - New **§4N payroll what-if simulator** and design-time wage-definition (Code on Wages s.2(y) 50 %) test in the CTC builder (FR-P13-59–FR-P13-61).
> - New **§4O contractor self-service portal** (G2 IMP-113), **§4P apprenticeship workflow** (G5 TM-787), **§4Q employee conflict-of-interest and gift declarations** feeding the P26 ethics registers (G5), **§4R record-retention and penalty-exposure engine** (G5 TM-807), **§4S establishment/branch register shared with P15** (G2 IMP-093).
> - New **§4T global workforce readiness** (foreign-subsidiary employees as a later jurisdiction pack via P25; records in home-region cell, NN-24) and **§4U customisation catalogue**.
> - Registers: G2 IMP-114 acceptance measure added (every Appendix T register reproducible from HRMS data); NN-48 three dates applied to labour filings and challans.
> - External references standardised to 'Equator v3.1 App Z' (G5 E-15) to avoid confusion with this pack's new Appendix Z.
---

## 1. Objective and business outcome

Regulated finance companies, co-operatives and ordinary companies must run their people function under Companies Act governance (KMP, directors, committees), regulator expectations (fit and proper, CISO independence, Chief Compliance Officer tenure, Internal Ombudsman tenure), the four Labour Codes in force from 21 November 2025, State Shops and Establishments laws, the POSH Act and the Income-tax Act 2025. P13 delivers an HRMS that is (a) **the single people master for every other module** (users and roles are employees; committees and KMP come from here), (b) a **labour-compliance engine** producing registers, returns, wage slips and statutory clocks from signed rule packs, and (c) a **payroll engine** that computes and approves pay while disbursal goes out by bank file or a licensed payout partner (D-11).

| Outcome | Exit-gate measure |
|---|---|
| One people master | A new employee created in P13 can be given a platform role, appointed to a committee (P06) and assigned compliance tasks (P04) without re-entering data; leaver revocation removes all LDC access within 15 minutes and pushes M365/Google suspension where connected |
| Finance-company org out of the box | The onboarding wizard proposes a default department structure for the tenant's entity family (NBFC, bank, UCB, credit co-op, ARC, insurance intermediary, AIF manager, listed company, private company, LLP) which the admin can rename, merge or extend; departments map to the compliance "Department" vocabulary of the tenant's Excel templates (Appendix E column `department` (v1.0: M)) |
| Labour compliance generated, not typed | For a 150-employee NBFC in Delhi and Uttar Pradesh: unified registers, wage slips, appointment letters, leave records, overtime records, POSH annual report, EPF ECR data file, ESI contribution data, PT/LWF (where applicable) and the Labour Codes obligations calendar are produced from transactions; every output cites its rule-pack version |
| Payroll that an auditor can reproduce | A finalised pay run re-computes bit-for-bit from its stored inputs and parameter versions (NN-22); maker, checker and approver are three different people; bank file hash matches the approved register |
| POSH handled with sealing | POSH complaints are in a sealed store with separate keys; only IC members see case content; 90-day inquiry clock owned and escalated; annual report and Board-report disclosure generated without exposing identities (NN-13) |
| Employment agreements signed in-tool | Offer, appointment letter and employment agreement assembled from templates, signed by Aadhaar eSign/DSC through the P07 eSign port, stored with audit trail |
| People-risk to the risk function | Aggregated people-risk KRIs (attrition, key-person vacancy, training completion, concentration of approvals, overdue mandatory leave for sensitive roles) flow to P08 and, by tenant consent, to Finbyx/Udofin as aggregates only |

---

## 2. Scope (in / out)

**In scope**
- **Organisation**: legal entities (from P01), establishments (registered office, branches, units — each with State, address, Labour Code registration numbers, S&E registration), departments, functions, cost centres, positions, grades, reporting lines (solid/dotted), committees link (P06), delegation of powers link (P02 authority matrix).
- **People**: employees (permanent, probationer, fixed-term employee under IR Code s.2(o) / OSH, contract labour via contractor, apprentice, intern, consultant/retainer — non-employee), directors and KMP (shared with P06 `gov.persons`; an individual may be both), POSH IC external member (non-employee, sealed), worker classification (worker vs non-worker under the Codes; supervisory wage cap), documents (with DMS), emergency contacts (minimal), bank details (tokenised, used only for payroll file generation), nominations (gratuity Form, PF nomination).
- **Lifecycle**: requisition → recruitment (light ATS) → offer → background-verification tracking (external vendor results only) → joining → probation → confirmation → transfers/promotions/secondments (incl. group-company secondment for Infrabyx-style groups) → separation → full and final → alumni.
- **Time**: attendance capture (web check-in, mobile PWA geo-optional with consent, biometric/door-access import, Microsoft Teams/Google presence is **not** used as attendance — NN-25), shifts, weekly offs, overtime with consent, work-from-home declarations, regularisation.
- **Leave**: statutory floors (OSH Code s.32, State S&E acts, CoSS maternity) + tenant policies; accrual, carry-forward, encashment; holidays by State; mandatory/forced leave for sensitive positions (bank and NBFC good practice for fraud prevention — "mandatory leave" for staff in sensitive positions [VERIFY current RBI instrument]).
- **Payroll**: salary structures, CTC → components, statutory wage base (Code on Wages s.2(y) 50 % rule), EPF/EPS/EDLI, ESI, PT, LWF, gratuity provision, bonus, overtime, arrears, loans/advances, reimbursements, TDS on salary (Income-tax Act 2025 s.392; companion pack `ita25-salary-tds`), payslips, pay registers, bank/payout file, accounting journal export to `acc` (P11) / Tally / Finbyx.
- **Labour compliance**: Labour Codes obligations (content packs), unified registers and forms, returns (EPF ECR, ESIC, PT returns, LWF, annual returns under the Codes when portals publish formats), establishment registration tracking, inspection-scheme readiness, notices display, committees (Works Committee, Grievance Redressal Committee, Safety Committee where applicable, POSH IC), standing orders/model standing orders for ≥ 300 workers, contract-labour licensing and principal-employer obligations, POSH module.
- **Engagement & development**: policy acknowledgements, training records (mandatory training: KYC/AML, POSH, information security, code of conduct, DPDP), FinLegal Academy course links (P21), performance goals and reviews (light; full appraisal for LawDocs staff is OH10/OH11), disciplinary records (restricted).
- **Fit and proper and regulatory people controls**: fit-and-proper declarations and Board/NRC assessments for directors and specified senior management, CCO/CISO/IO tenure and independence checks, staff accountability (RBI fraud-risk staff accountability [VERIFY]), key-person register.
- **User provisioning**: employee → LDC user (SCIM to Keycloak), and optionally → M365/Google account creation/suspension via `WORKSPACE_PORT` (R-082).
- **Task allocation**: managers assign tasks to reports (P04 tasks engine) — hierarchy from P13 reporting lines.
- **People-risk metrics** to P08 and the ecosystem (aggregates only).

**Out of scope**
- Holding or moving salary money (D-11): LDC generates the bank file / payout instruction; the tenant's bank or a licensed payout partner executes.
- Statutory return **submission** to EPFO/ESIC/State portals: LDC prepares the upload files and records acknowledgement (D-13).
- Recruitment marketing, job boards at scale (integrate via P18 if needed).
- Infrabyx's own staff HRMS, payroll, appraisal, anti-fraud scorecards → Infrabyx Operations Hub OH10–OH11 (D-03). The shared `infrabyx-labour-rulepack` keeps computations identical.
- Biometric template storage: LDC imports attendance punches only, never biometric templates.

---

## 3. Personas and permissions touched

| Role | P13 rights |
|---|---|
| `ten_hr_admin` | Org setup, employee records, lifecycle, leave policy configuration (T tier), registers, labour compliance; cannot finalise payroll alone |
| `ten_payroll_maker` | Prepares pay run, inputs, arrears; cannot approve own run |
| `ten_payroll_checker` | Reviews variances, approves register (≠ maker, NN-05) |
| `ten_kmp` (CFO) | Final payroll approval and bank-file release authorisation (third actor) |
| `ten_kmp` (CS) | Director/KMP register link, fit-and-proper workflow, Board disclosures (POSH, gratuity, CSR staff) |
| `ten_dept_head` | Approves leave, attendance regularisation, requisitions; assigns tasks; sees own department |
| `ten_employee` | Self-service: profile, documents, attendance, leave, payslips, tax declarations, policy acknowledgements, training, grievance (IR Code GRC and P14 links), POSH complaint (sealed route) |
| `ten_ic_member` | POSH IC case workspace (sealed); cannot see payroll or other HR data by this role |
| `ten_admin` | Assigns HR roles; cannot read POSH cases or individual pay unless also holding the role |
| `ten_internal_auditor`, `ten_external_auditor` | Read registers, pay registers (masked bank details), controls evidence |
| `ten_supervisor_view` / labour inspector view | Time-boxed read-only grant to registers (D-12 pattern; the Codes' inspector-cum-facilitator may ask for registers — export bundle preferred) |
| `dlv_professional` | Retainer payroll/labour-compliance services under tenant grant (maker role only; never checker for the same run) |
| `svc_vidhi` | Drafts letters, policies, POSH annual report narrative from counts, explains payslip lines; never decides hiring, pay, discipline (NN-14; OH principle "People decisions stay human") |
| `ten_kmp` (CHRO) *(v1.1)* | Owns people policies and the People dashboard; approves policy exceptions, grade changes and HR approval-matrix values within the Board-approved delegation; cannot approve own pay or a run they prepared; sees aggregate POSH counts only (NN-13) |

SoD rules (Appendix D): payroll maker ≠ checker ≠ releaser; a person cannot approve their own salary change, leave or reimbursement; HR admin cannot change their own bank details without a second HR approver plus employee re-confirmation by OTP; bank-detail changes in the 5 days before a pay run are held for checker review [REC anti-fraud]; the IC Presiding Officer cannot be the respondent's line manager (conflict check).

---

## 4. Functional requirements

### 4A. Organisation model and default structures

**FR-P13-01 — Establishments.** Each legal entity has establishments with: type (registered office, head office, branch, regional office, back office, call centre, warehouse), State and district, address, headcount (computed), worker/non-worker counts (computed from classification), registration numbers (OSH Code registration where ≥ 10 workers, S&E registration, EPF establishment code, ESIC code, PT registration/enrolment per State, LWF), applicable State rule pack, holiday calendar, working-hours profile. Thresholds in Appendix T §T.2 are evaluated monthly on actual headcount; crossing a threshold opens the corresponding obligation and task (e.g., ESI at 10, EPF at 20, Bonus at 20, GRC at 20, crèche at 50, standing orders at 300, POSH IC at 10).

**FR-P13-02 — Departments and functions.** Department → function (sub-department) → team, renameable (R-086). Each department has a head, optional deputy, and **compliance-department mapping** to the controlled vocabulary used in the tenant's Excel question templates (column `department` (v1.0: M) — e.g., IFSCA family: Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management). Renaming a department never breaks the mapping (mapping is by id).

**FR-P13-03 — Default structure by entity family.** Seed templates (T tier, editable before and after adoption):

| Family | Default departments (functions in brackets) |
|---|---|
| NBFC (all layers) | Board & Secretarial (Company Secretary, Board office); Executive Management (MD/CEO office); Credit (Credit underwriting, Credit policy, Credit monitoring); Business / Sales (Branch network, Partnerships & co-lending, DSA/DMA management, Digital lending/LSP management); Operations (Disbursement, Loan servicing, Customer service, Document custody); Collections & Recovery (Pre-delinquency, Field collections, Legal recovery, SARFAESI/IBC desk); Finance & Accounts (Accounting, Treasury & ALM, Taxation, Investor relations for listed/debt-listed); Risk Management (ERM, Credit risk, Market & liquidity risk, Operational risk, Model risk); Compliance (Regulatory compliance, KYC/AML & FIU reporting, Grievance redressal — GRO/PNO/IO); Internal Audit (reports to Audit Committee); Information Technology (IT operations, Applications, Data); Information Security (CISO office — independent of IT); Human Resources & Administration; Legal; Fraud Risk Management (where applicable) |
| NBFC-ICC / investment company | Board & Secretarial; Investments (Equity, Debt, AIF/REIT/InvIT, Treasury); Finance & Accounts; Risk; Compliance; Internal Audit; IT & InfoSec; Admin |
| Commercial bank / SFB | As NBFC plus Treasury (front/mid/back office separation), Retail banking, Corporate banking, Payments & cards, Branch banking, Inspection & audit, Vigilance, Customer service committee support, Data & MIS |
| UCB / credit co-op | Board of Directors / Managing Committee & Secretarial; CEO/Secretary office; Loans & Advances; Deposits; Accounts; Recovery; Compliance & Returns; Audit (statutory/concurrent liaison); IT; Admin & HR; Member services (share capital, membership) |
| ARC | Acquisition (due diligence, bidding); Resolution & Recovery; Trusteeship / Trust management (SR schemes); Valuation; Finance & Accounts; Risk; Compliance; Internal Audit; Legal; IT; HR & Admin |
| Insurance intermediary | Placement/Broking, Claims support, Operations, Compliance (Principal Officer), Finance, IT & InfoSec, HR |
| AIF manager / AMC | Investment management, Operations & fund accounting, Investor relations, Risk, Compliance, Legal, Finance, IT & cyber (CSCRF), HR |
| Listed company / private company / LLP | Secretarial, Finance, Legal, HR, Operations, Sales, IT, Compliance (as needed) |

**FR-P13-04 — Positions and grades.** Positions (approved headcount, budget, grade band, reporting position, location, sensitive-position flag for mandatory leave / rotation, regulated-role flag e.g., CCO, CRO, CISO, PNO, GRO, Principal Officer (PMLA), Designated Director (PMLA), DPO, Internal Ombudsman). Regulated-role flags drive validations: CISO not reporting directly to Head of IT and no business targets (RBI NBFC Cyber Directions 2026 paras 81–82); CCO tenure and reporting under the applicable compliance-function instrument (e.g., RBI NBFC Compliance Function directions — pack `RBI-NBFC-COMPLIANCE`) [VERIFY para]; Internal Ombudsman tenure ≥ 3 years and ≤ 5 years total and age < 70 at end of tenure (RBI NBFC IO Directions 2026 cl.5, 8(4)) — validations are warnings that create compliance exceptions, not hard blocks.

**FR-P13-05 — Org chart.** Auto-generated from reporting lines; accessible list view; export (PDF/PNG/XLSX); "as of" date (bitemporal, NN-07) for Board and inspection use.

### 4B. Employee master and person model

**FR-P13-06 — Person vs employment.** `hr.persons` (identity, shared with `gov.persons` from P06 — a director is a person who may or may not be an employee) and `hr.employments` (one person can have several employments over time or concurrently in group companies; secondment is an assignment on an employment). Fields minimised (NN-12): legal name, preferred name, date of birth (needed for statutory computations), gender (only where needed for statutory purposes such as maternity/POSH/women night-work rules; option "prefer not to say" otherwise), contact, address, PAN (tokenised + masked), UAN, ESIC IP number, Aadhaar **not stored** (only "verified via DigiLocker on <date>" flag and last 4 digits if an employer must quote it on a statutory form [VERIFY need]), bank account (tokenised; last 4 visible), nominee details (for statutory nominations), emergency contact, educational/professional qualifications (for fit-and-proper and KMP eligibility), disability status (optional, self-declared, sealed health-adjacent class; used only for accessibility accommodations and statutory benefits).

**FR-P13-07 — Worker classification.** Record per employment: employee vs worker (Codes' definitions; supervisory capacity wage cap per Appendix T), managerial/administrative status, fixed-term employment, contract labour (through contractor), apprentice; classification drives which entitlements and registers apply. Classification changes are maker-checker and versioned.

**FR-P13-08 — Documents.** Per employee DMS folder (P07) with the Appendix M folder taxonomy: `People/<Year>/<Department>/<Employee code - Name>/{01 Appointment, 02 KYC & Statutory, 03 Payroll, 04 Leave & Attendance, 05 Performance & Training, 06 Policies Acknowledged, 07 Exit}`; retention classes per document type (Appendix T §T.6).

### 4C. Lifecycle

**FR-P13-09 — Requisition.** Position-based request with budget check, approval chain (department head → HR → CFO for unbudgeted), auto-creates a job posting draft.

**FR-P13-10 — Recruitment (light ATS).** Candidate records with consent notice (DPDP notice for applicants — P12 notice designer), stages, interview scorecards, offer approval; deletion of unsuccessful candidates' data after the tenant's retention period (default 6 months [REC]) by `RetentionSweepWorkflow`.

**FR-P13-11 — Offer and appointment letter.** Templates (P07) with merge fields; appointment letter is mandatory for every employee under OSH Code s.6(1)(f) (existing employees within 3 months — Appendix T clock); offer → acceptance by eSign (P07 `ESIGN_PORT`: Aadhaar eSign via licensed ESP, or click-wrap acceptance where the tenant chooses and the document is not an IT Act First Schedule exclusion).

**FR-P13-12 — Employment agreement.** Clause library (P07): appointment terms, probation, duties, confidentiality, data-protection obligations (DPDP employee-processing notice), IP assignment, conflict of interest, code of conduct, non-solicitation (post-employment non-compete is generally void under Indian Contract Act s.27 — the clause library flags it [LAW] and offers a garden-leave alternative [REC]), notice period, termination, governing law. Stamp duty: State-specific e-stamping via eStamp adapter where the agreement requires stamping (P18; [VERIFY per State]). Signing order configurable (employer signatory → employee or vice versa); signed PDF with certificate and audit trail stored; counterparts emailed.

**FR-P13-13 — Pre-joining and joining.** Checklist per department template: documents (PAN, address proof, educational certificates, prior employment relieving letters, Form 11/EPF declaration, ESI declaration, nomination forms, gratuity nomination), background verification (vendor results uploaded; vendor via `tpr`), policy acknowledgements, assets issued, system access requests (P01), M365/Google account creation (§4J), training enrolments (P21 Academy links).

**FR-P13-14 — Probation and confirmation.** Review due tasks, manager assessment, confirmation letter, extension with reason.

**FR-P13-15 — Movements.** Transfers (establishment change re-evaluates State rule pack, PT, LWF, holidays), promotions, re-designations, role changes (regulated-role flags re-checked; KMP change triggers P06 MCA filing obligation, e.g., DIR-12 within 30 days for KMP/director changes [LAW Companies Act s.170/s.203 read with rules; VERIFY form timing]), secondment to group companies (records host entity, cost recharge reference — no shared tenant data unless a group grant exists, NN-23/NN-30).

**FR-P13-16 — Separation.** Resignation / termination / retirement / death / end of fixed term / retrenchment (IR Code Ch. IX/X conditions and compensation per Appendix T), exit checklist (assets, access revocation, knowledge transfer, handover of compliance tasks — P04 re-assignment wizard that lists every open task, approval and committee seat held by the leaver), full and final settlement within 2 working days of separation for wages (Code on Wages s.17(2)) and leave encashment per OSH s.32(1)(vi) timelines, gratuity within 30 days of becoming payable (CoSS s.56), service certificate, relieving letter, PF/ESI exit updates, Form 16-equivalent under Income-tax Act 2025 (Form 130 [VERIFY form numbering]).

### 4D. Attendance, work time and remote work

**FR-P13-17 — Capture methods.** Web/PWA check-in-out; geo-tagging optional per tenant with explicit notice and consent and only at check-in/out moments (no continuous tracking); IP-range or Wi-Fi SSID attestation for office; biometric/door-access imports (CSV/API — eSSL, Matrix, ZKTeco connectors via P18); manual attendance by supervisor for field staff with photo-less GPS optional. Monitoring notice (NN-25) must be published and acknowledged before any capture method that records location or device data is enabled.

**FR-P13-18 — Shifts and hours.** Shift patterns, weekly off, spread-over, rest intervals, daily and weekly hour caps per Code + State (Appendix T §T.3), overtime with worker consent and 2× rate (Code on Wages s.14 read with OSH), quarterly overtime caps per State where notified; women night-work rules with consent and safeguards per State; alerts when rostering would breach a cap.

**FR-P13-19 — WFH declarations.** Employee declares WFH days and location State (affects PT/LWF and holiday calendar where the tenant's policy follows work location [VERIFY remote-employee PT position — Equator D3-31 open]); manager approval; equipment and data-security acknowledgement (links P12 policies).

**FR-P13-20 — Regularisation and disputes.** Missed punch requests, on-duty, comp-off; employee can dispute an attendance entry; every change has reason and approver; registers keep original and corrected values (NN-02).

### 4E. Leave

**FR-P13-21 — Two-layer leave model.** Layer 1: statutory floors from rule packs (OSH s.32 annual leave with wages: 1 day per 20 days worked after 180 days in a calendar year, carry-forward cap 30, encashment rules; State S&E earned/casual/sick leave; CoSS maternity 26 weeks / eligibility 80 days; paternity/adoption only if tenant policy grants; national and festival holidays per State). Layer 2: tenant policy (may only be more generous; validator rejects a policy below the floor — `LDC-HR-021`). The engine computes per employee per day the most favourable entitlement among applicable floors (MoLE FAQ approach; Appendix T §T.1).

**FR-P13-22 — Leave operations.** Apply/approve/cancel, half-days, hourly leave (policy), team calendar (visible to department head; respects privacy — leave type hidden for sensitive types such as medical where policy says), delegation of approvals when approver is on leave (never to the applicant), balance projections, encashment on separation, year-end processing with preview, sync to calendars (P04 calendar; M365/Google via P18 — "Out of office" event only, no reason).

**FR-P13-23 — Mandatory leave for sensitive positions.** Positions flagged sensitive (treasury dealers, cash/vault custodians, credit sanctioning, payments, IT privileged admins) require a block of consecutive leave per year (default 10 working days, T tier [REC]); during the block, privileged access is suspended (P01 access-suspension hook) and the deputy acts; compliance instance generated; exceptions need CRO approval.

### 4F. Payroll engine (rule-pack driven, NN-22, NN-26)

**FR-P13-24 — Components.** Component register with statutory class (basic, dearness allowance, retaining allowance — counted in wages; HRA, conveyance, overtime, commission, bonus, gratuity, retrenchment compensation, employer PF/pension contributions, statutory bonus etc. — exclusions per Code on Wages s.2(y)); taxable/exempt mapping under Income-tax Act 2025 (rule pack `ita25-salary-tds`); PF/ESI applicability flags; pro-ration rules; rounding rules.

**FR-P13-25 — Statutory wage base.** Pure function `wage_code_base(components, params)`: if excluded components exceed 50 % of total remuneration, the excess is added back to wages (s.2(y) proviso) — used for PF (where the scheme uses Code wages [VERIFY scheme definition]), gratuity, bonus eligibility, retrenchment compensation; tested with golden fixtures from the shared rule pack (Ecosystem Spec §12.3 conformance — Finbyx GV6 and OH10 must compute identically).

**FR-P13-26 — Structures and CTC.** Salary structures by grade; CTC builder that shows the statutory wage base and employer costs; offer simulation; revision workflow with effective date and arrears computation.

**FR-P13-27 — Monthly cycle (`PayRunWorkflow`).**
1. Lock inputs (attendance, leave, overtime, new joiners, leavers, revisions, one-time earnings/deductions, loans, reimbursements, tax declarations and proofs) — cut-off date configurable.
2. Compute gross → statutory deductions (EPF employee share, ESI employee share, PT, LWF) → TDS on salary (projected annual tax under chosen regime, Income-tax Act 2025 s.392) → other deductions (capped at 50 % of wages per Code on Wages s.18 read with Wages (Central) Rules; excess carried forward [VERIFY rule ref]) → net pay.
3. Employer costs: EPF/EPS/EDLI/admin charges, ESI employer share, LWF employer share, gratuity provision, bonus provision.
4. Variance report vs previous month (by employee and component); exceptions (negative net, net < floor, minimum-wage check against applicable State/central minimum wage, PF ceiling changes such as the ₹25,000 ceiling from 17 Sep 2026 with split-month pro-ration [VERIFY gazette]).
5. Maker submits → checker approves register → CFO (or delegate) authorises release (three distinct people).
6. Output: payslips (published to self-service; wage slip in the format required under the Code on Wages rules [VERIFY form]), pay register (statutory register format), bank/payout file (bank-specific layouts: SBI CMP, HDFC ENet, ICICI CIB, Axis, Kotak, YES; NEFT/RTGS bulk CSV; RazorpayX Payroll/Payouts API adapter behind flag), journal voucher export (P11 `acc`, Tally XML, Finbyx GL), EPF ECR text file, ESIC contribution file, PT and LWF challan data, TDS data for quarterly salary-TDS statement (Income-tax Rules 2026 form [VERIFY form numbers: Form 138 per Equator research]).
7. Disbursal confirmation (bank response file import or payout webhook) — reconciliation; unpaid/failed credits create tasks.
8. Statutory payment deadlines tracked: wages before the 7th of the following month (Code on Wages s.17(1)); EPF ECR by the 15th; ESIC by the 15th [VERIFY]; PT per State; TDS deposit per Income-tax Rules 2026.

Run gate (Locked): a run cannot be finalised if any parameter it uses is `NOT_CONFIRMED` (`LDC-HR-040`); `SECONDARY_ONLY` parameters require the named Payroll Compliance Officer's acknowledgement per run (Appendix T §T.4).

**FR-P13-28 — Off-cycle runs.** Full and final, bonus, arrears, corrections (as Correction Entries referencing the original run — the original run is never edited, NN-02).

**FR-P13-29 — Tax.** Regime choice (default regime unless employee opts), investment declarations and proofs (where old regime), perquisite valuation (rule pack), employer NPS contribution limits, previous-employer income, annual Form 130 equivalent [VERIFY], quarterly statement data; employee tax projection view.

**FR-P13-30 — Loans and advances.** Salary advances and staff loans (with interest/perquisite valuation), EMI deduction respecting the deduction cap; for NBFC/bank tenants, staff-loan policy approvals and related-party/insider-lending checks are flagged to P04 compliance obligations [VERIFY applicable RBI staff-loan norms].

**FR-P13-31 — Reimbursements.** Claims with bill upload (OCR via P07), policy limits, approval, payroll or separate payout.

### 4G. Labour Codes compliance engine

**FR-P13-32 — Obligations content.** Labour pack families (Appendix E family `LAB`) loaded via P03: Code on Wages 2019, Industrial Relations Code 2020, Code on Social Security 2020, Occupational Safety, Health and Working Conditions Code 2020, the Central Rules (8 May 2026) and each State's rules as they are notified (`state_rule_status` per State and Code from the shared rule pack), State Shops and Establishments Acts (continuing), POSH Act 2013 and Rules, Maternity provisions (now in CoSS), Apprentices Act 1961, Equal Remuneration (subsumed in CoW), Child and Adolescent Labour Act (prohibition checks at hiring — date-of-birth validation), Contract labour (OSH Code Ch. XI), Inter-State migrant workers (OSH), Employees' Compensation (CoSS), PMLA staff obligations (Principal Officer appointment etc. for REs — via the sector pack). Each obligation becomes a P04 compliance instance with owner = HR (or Payroll, Compliance).

**FR-P13-33 — Registers.** Generated from transactions in the formats prescribed by the Central/State rules (unified electronic registers where the Rules provide — Appendix T §T.5 lists registers by Code with source rule and status): register of employees/workers, wages register (with deductions, fines, advances), attendance/muster roll, overtime register, leave register, register of fines and deductions, register of accidents/dangerous occurrences (where applicable), contractor and contract-labour registers (principal employer), bonus register, maternity benefit register, gratuity nomination register, register of complaints (GRC), POSH register (sealed, counts only outside the IC). Each register is a view over source data with: version, generated_at, rule-pack version, signatory, hash; printable PDF and XLSX; electronic maintenance attestation.

**FR-P13-34 — Returns.** Monthly/annual returns as forms become available on Shram Suvidha/State portals (OSH Code annual return; CoW returns; CoSS returns) — the engine maintains a "return definition" record per form with status `FORMAT_PUBLISHED / FORMAT_PENDING` [VERIFY current portal formats]; EPF ECR monthly; ESIC half-yearly/monthly contributions; PT returns per State; LWF returns per State; Bonus annual return; POSH annual report to the District Officer (POSH Rules r.14 contents). Return preparation produces upload-ready files plus a review checklist; submission is human (D-13).

**FR-P13-35 — Notices and displays.** Statutory notices/abstracts required to be displayed (Code abstracts, working hours, holidays, wage periods, IC composition and contact, GRC composition) generated as printable PDFs and as an intranet page; displayed-on date recorded with photo evidence.

**FR-P13-36 — Registrations and licences.** OSH establishment registration (≥ 10 workers), S&E registration/renewal, contract-labour licence/registration as principal employer, EPF/ESIC codes, PT registration/enrolment, LWF; expiry and renewal reminders; inspection-scheme notes (Codes' web-based inspection, inspector-cum-facilitator) [VERIFY].

**FR-P13-37 — Contract labour and contractors.** Contractor master (from `tpr`), contract-labour deployment by establishment, principal-employer duties (ensure wage payment; verify contractor's PF/ESI challans — monthly evidence requests to the contractor via the vendor portal of P12 §4M), canteen/welfare thresholds where applicable.

**FR-P13-38 — Committees.** As P06 committees with HR-specific templates: **Grievance Redressal Committee** (IR Code s.4 — establishments with ≥ 20 workers; equal employer/worker representation, adequate women representation; resolution timelines per Code and rules [VERIFY 30-day]); **Works Committee** (IR Code s.3 — ≥ 100 workers where appropriate Government orders); **Safety Committee** (OSH Code where notified for the establishment class); **POSH Internal Committee** (§4H); **Canteen/welfare committees** where applicable. Meetings, minutes (AI draft from notes, P06), decisions, member terms, worker-representative elections (simple ballot records).

**FR-P13-39 — Standing orders.** For ≥ 300 workers: certification of standing orders under IR Code s.28–30 or adoption of model standing orders; below 300, model standing orders (services) used as policy template (Appendix T).

### 4H. POSH module (sealed, NN-13)

**FR-P13-40 — IC constitution.** Required for every workplace with ≥ 10 employees (POSH Act s.4; at each office/administrative unit located at different places); composition: Presiding Officer — a woman employed at a senior level; ≥ 2 members from employees committed to the cause of women or with social work experience or legal knowledge; 1 external member from an NGO/association committed to the cause of women or familiar with sexual-harassment issues; at least one-half of members women; term ≤ 3 years (s.4(3)); fees to external member per rules. Composition validator (hard block on saving an IC that has < 50 % women or no external member; warning on term expiry 60 days ahead). Below 10 employees: Local Committee route information (s.6) and the employer still runs awareness obligations.

**FR-P13-41 — Complaint intake.** Channels: self-service sealed form ("Report sexual harassment" — no line-manager visibility), email to the IC mailbox (ingested into sealed store), offline complaint uploaded by IC member; complaint within 3 months of the incident (last incident in a series), extendable by 3 months for reasons recorded (s.9(1)); assistance to write a complaint (s.9(1) proviso). Complainant can track status in self-service. Link to SHe-Box (shebox.wcd.gov.in) shown in help.

**FR-P13-42 — Case workflow.** Conciliation at the aggrieved woman's request only, no monetary settlement (s.10); inquiry per service rules or POSH Rules r.7 [VERIFY rule number]; interim relief requests (s.12) to employer; inquiry to be completed within 90 days (s.11(4)) — clock owned by Presiding Officer with escalations; findings report to employer within 10 days of completion (s.13(1)); employer acts on recommendations within 60 days (s.13(4)); appeal within 90 days (s.18) — info only; false/malicious complaint findings (s.14) handled with caution messaging. Confidentiality (s.16): no publication of identities; penalty for breach (s.17).

**FR-P13-43 — Sealing.** Separate schema `lab_posh` with its own KMS key, row access only for IC members of that IC and the designated employer action officer (outcome actions only); excluded from search index, analytics, Vidhi notebooks and training, exports other than the IC's own case export, and from Supervisor/auditor views by default (counts only); every access logged and visible to the Presiding Officer.

**FR-P13-44 — Annual report and disclosures.** IC annual report (s.21; POSH Rules r.14 contents: number of complaints received, disposed, pending > 90 days, workshops/awareness programmes, nature of action taken) generated from counts; employer's annual report inclusion; Board's report disclosure (Companies (Accounts) Rules r.8(5)(x): statement that the company has complied with provisions relating to constitution of IC under POSH Act [LAW]) and number of complaints (as required by the Companies (Accounts) Amendment Rules where applicable [VERIFY current disclosure list]) → feeds P06 Board report draft. Awareness programme records (s.19(c)), orientation for IC members.

### 4I. Policies, training and conduct

**FR-P13-45 — Policy acknowledgements.** Policies from P07 pushed to target groups with read-and-acknowledge tracking (with quiz optional), reminders, completion reports (feeds compliance evidence for code of conduct, whistle-blower/vigil mechanism, insider trading code for listed companies — SEBI PIT designated persons list maintained from P13 positions [LAW SEBI (PIT) Regulations 2015 Sch. B; detail in P06]).

**FR-P13-46 — Training.** Course catalogue (internal, FinLegal Academy deep links — P21, external), mandatory training rules by position (e.g., AML/KYC annual for operations and branch staff; information security for all; POSH for all; DPDP; DSA/DMA training for partner managers), completion import (SCORM/xAPI completion via LMS webhook from trainings.lawdocs.in when the Academy exposes it [VERIFY]), certificates storage, expiry.

**FR-P13-47 — Disciplinary and conduct.** Restricted records (show-cause, inquiry, outcome); fines only per Code on Wages permitted grounds with show-cause and the 7/15-day timelines (Wages (Central) Rules r.16 [VERIFY]); staff accountability examinations for frauds (link to P10/P08 fraud records) [VERIFY RBI fraud MD staff accountability timelines].

**FR-P13-48 — Fit and proper (with P06).** Annual declarations by directors (Companies Act s.184 disclosures, DIR-8 non-disqualification, and RE-specific fit-and-proper declarations and undertakings, e.g., RBI NBFC directors' F&P declaration and deed of covenants [VERIFY current consolidated direction]); senior-management F&P for specified roles; NRC review workflow; CEO/MD prepares the F&P documentation in-tool (R-093); evidence pack export.

### 4J. User and workspace provisioning (R-082)

**FR-P13-49 — Joiner–mover–leaver.** Employee events drive identity: joiner → LDC user (SCIM to Keycloak) with role bundle from position; mover → role re-evaluation, approval for elevated roles; leaver → suspend within 15 minutes of exit-effective time [REC], transfer task ownership, revoke grants; optional `WORKSPACE_PORT` (M365 Graph: create user, assign licence, add to groups/Teams, set manager; Google Admin SDK: same) with dry-run preview; the tenant chooses whether LDC is the source of truth for workspace accounts or merely notifies IT (`hr.workspace.mode` ∈ `OFF`, `NOTIFY_IT`, `PROVISION`).

**FR-P13-50 — Directory sync.** If the tenant's source of truth is Entra ID / Google Directory, LDC imports users and maps them to employees (match on work email/employee ID) — no duplicate people.

### 4K. Tasks and hierarchy

**FR-P13-51 — Hierarchical task assignment.** P04 task engine uses P13 reporting lines: a user may assign tasks to anyone below them in the hierarchy, to peers by delegation rule, or to Vidhi (P17); department heads see all tasks in their department (calendar view — R-094); cross-department assignment requires the other department head's acceptance (configurable).

### 4L. People-risk metrics and ecosystem sharing (R-015)

**FR-P13-52 — KRIs.** Monthly computed aggregates: attrition (voluntary/involuntary; by department and critical role), vacancy duration for regulated roles (CCO, CRO, CISO, PNO, IO, Principal Officer), key-person dependency (single approver concentration from P02 authority matrix), mandatory-leave compliance for sensitive positions, training completion for mandatory courses, overtime cap breaches, POSH cases (count only, threshold alerts), grievance committee cases (count), disciplinary cases (count), background-verification pending, contractor compliance gaps. Delivered to P08 as `risk_metric_value` records (Ecosystem Spec `risk_snapshot_v1` style, pseudonymised — no individual-level data) and, by tenant-approved data-sharing scope, to Finbyx/Udofin dashboards (e.g., collection-agent training completion for Udofin's DSA/recovery agent controls) via `workforce` events (Ecosystem Spec §6.23). Every people-risk metric that leaves P13 (to P08, Finbyx, Udofin or any dashboard outside HR) is an aggregate with small-cell suppression (k ≥ 5; cells below 5 shown as "< 5"), and POSH data leaves only as counts (X-36; NN-13).

---

### 4M. Fast self-service and approvals *(v1.1)*

**FR-P13-53 — One-tap leave.** The employee picks dates on a calendar; the system shows balance before/after, team members already away, holidays and sandwich-rule effects, and policy hints (documents needed for sick leave beyond N days). Submission is one tap; cancellation before start is one tap. Target: leave applied in ≤ 20 seconds on mobile (P23 performance budget).

**FR-P13-54 — Auto-approval rules (Tenant-configurable).** Rules such as "casual leave ≤ 1 day with balance and no team-coverage conflict → auto-approved and the manager notified" or "work-from-home on a declared WFH day → auto-approved". Rules never auto-approve: leave for sensitive positions within the mandatory-leave block (FR-P13-23), leave overlapping a statutory deadline the employee owns (P04 check), loss-of-pay, or anything for the approver's own request (NN-05). Every auto-approval is labelled and audited.

**FR-P13-55 — Approval inbox and delegation.** Managers approve from the Work Inbox (P04) or from e-mail/Teams adaptive cards with signed one-time links; "Review next" for batches; delegation when on leave (never to the requester); escalation after `hr.approval.escalate_after_hours`.

**FR-P13-56 — Attendance regularisation in bulk.** For system outages or offsite events the HR admin regularises a group with one reason; a 24-hour undo window applies (NN-49); originals stay in the register (NN-02).

**FR-P13-57 — Letters on demand.** Employment certificate, salary certificate, address-proof letter, experience letter, relieving letter, Form 16-equivalent [VERIFY Income-tax Act 2025 form] — generated from templates (P07) with QR verification; requests auto-fulfilled when data is complete, else routed to HR. Requests and downloads are logged.

**FR-P13-58 — HR help desk.** Employee queries (payroll, leave, policy) as tickets using the P14 desk engine with an internal HR queue; Vidhi suggests answers citing policy clauses (NN-06); sensitive categories (harassment, health, whistle-blowing) are routed to sealed channels (NN-13) and never to AI drafting.

### 4N. Payroll what-if simulator and design-time tests *(v1.1)*

**FR-P13-59 — What-if simulator.** Run deterministic scenarios on a copy of payroll inputs without posting: annual increment matrix; change of salary structure; moving employees between States (PT/LWF/minimum wage effects); new statutory parameter versions (e.g., a PF ceiling change); bonus and gratuity provisioning impact. Output: per-employee and total cost deltas, net-pay deltas, statutory-base deltas, exceptions — exportable; every number from the payroll engine with lineage (NN-22, NN-37). Scenarios are saved, compared and shareable with the CFO.

**FR-P13-60 — Wage-definition test at design time.** The CTC builder and the structure designer run `wage_code_base` (FR-P13-25) live and warn when excluded components exceed 50 % of total remuneration (Code on Wages s.2(y) proviso) before a structure is saved, showing the add-back and its effect on PF/gratuity/bonus bases [VERIFY scheme-specific bases].

**FR-P13-61 — Pay-run readiness check.** A pre-run checklist computed nightly from cut-off: missing attendance, pending approvals, unverified bank details, new joiners without statutory IDs, parameters `NOT_CONFIRMED` — so the payroll maker starts a run with zero surprises.

### 4O. Contractor self-service portal *(v1.1; G2 IMP-113)*

**FR-P13-62 — Contractor portal.** External identity `ext_contractor` (limited, per contractor organisation) uploads monthly wage registers, attendance, PF ECR and ESI challans, payment proofs, licences and worker lists per establishment; uploads auto-close the principal-employer checkpoints they evidence after a checker review; missing items trigger reminders and, after the threshold, an issue. Contractors see only their own submissions.

### 4P. Apprenticeship workflow *(v1.1; G5 TM-787)*

**FR-P13-63 — Apprentices.** Engagement of apprentices under the Apprentices Act 1961 and rules: designated/optional trades, portal registration [VERIFY current national apprenticeship portal], apprenticeship contract and its registration, stipend computation (rule pack), attendance and leave rules for apprentices, quota tracking against the band applicable to the establishment [VERIFY current band], completion and certificate; apprentices are excluded from employee counts where the law says so (threshold logic, §5.6).

### 4Q. Employee conflict-of-interest and gift declarations *(v1.1)*

**FR-P13-64 — Declarations.** Annual and event-driven declarations by employees (outside interests, relatives in counterparties, outside employment, gifts and hospitality received/offered above thresholds, pre-clearance requests) collected through self-service and stored in the **P26 ethics registers** (conflicts register, gifts and hospitality register, recusal log); HR sees completion status; content of declarations is visible only to the ethics owner and Compliance. Directors' and KMP disclosures remain in P06.

### 4R. Record-retention and penalty-exposure engine *(v1.1; G5 TM-807)*

**FR-P13-65 — Retention.** Retention period per register and record type from rule packs (Code rules, PML Rules where HR holds KYC, Income-tax, DPDP minimisation) with purge proposals at expiry (approval required; legal hold respected).

**FR-P13-66 — Penalty exposure (indicative).** For each open or late labour obligation, the indicative statutory penalty band from the rule pack (first contravention vs repeat, compounding availability) is shown on the labour dashboard and summed by establishment/State — labelled "indicative, not legal advice" (NN-19); feeds the P20 savings model only from actual on-time performance.

### 4S. Establishment and branch register shared with P15 *(v1.1; G2 IMP-093)*

**FR-P13-67 — One register.** `hr.establishments` is the single source of establishments/branches for HR and for P15 entity profiles (`pack.entity_establishments` is a view on it). Adding an establishment with its State and worker count proposes the State packs (S&E, PT, LWF, holiday calendar, minimum wages) and the registrations due — target: "adding a Rajasthan branch adds its pack" in one step with a preview.

### 4T. Global workforce readiness *(v1.1)*

**FR-P13-68 — Foreign-subsidiary employees.** Employees of foreign subsidiaries can be held as people records for governance (directors, officers, KMP, signatories) and for headcount and policy acknowledgement; local payroll and labour content arrive later through P25 jurisdiction packs (or via a local payroll provider connector); records live in the subsidiary's home-region cell (NN-24); group dashboards show aggregates only.

### 4U. Customisation catalogue *(v1.1)*

Registered in §9 and P02: leave types and accrual rules above statutory floors; auto-approval rules; approval chains by grade/value; attendance policies by establishment; letter templates; onboarding/offboarding checklists per department; custom employee fields; probation and confirmation rules; appraisal-cycle hooks to OH-style templates (client-side, optional); department and function names (mapped to codes, Appendix U §U.9.0).


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P13-X01 — Ethics declarations to P26.** Conflict-of-interest and gift declarations made in employee self-service (§4Q) are written to the P26 ethics registers (`lit.ethics_declaration`, Appendix A §A.44); P13 holds only the self-service UI and reminders.

**FR-P13-X02 — People aggregates to P27.** Workforce metrics needed for BRSR (headcount by gender and category, turnover, wages, benefits, training, safety incidents, differently-abled employees) are published to P27 only as aggregates with k ≥ 5 suppression (X-36); POSH as counts only.

**FR-P13-X03 — Reporting lines for compliance accountability *(v1.2)*.** P13 publishes `in.lawdocscomply.hr.ReportingLineChanged.v1` (employee, manager, effective_from, source) and exposes `GET /hr/reporting-line/{user_id}?as_of=` returning the manager chain. P04 uses it to decide who may raise an Explanation Request (FR-P04-241), to route SLA escalations (Appendix A §A.46) and to resolve "superior" in Appendix D §D.19.3. Accountability reports from P04 may be used in HR processes only under the tenant's P13 policy and NN-25; P13 never imports accountability data automatically into appraisal or disciplinary records (NN-47, NN-60).

## 5. Workflows and state machines

### 5.1 Employment (`hr.employments.status`)
`PRE_JOINING → ACTIVE_PROBATION → ACTIVE_CONFIRMED → (ON_NOTICE → SEPARATED) | (SUSPENDED ↔ ACTIVE_*) | (ON_SECONDMENT ↔ ACTIVE_*) | (LONG_LEAVE ↔ ACTIVE_*)`; `SEPARATED → FNF_PENDING → FNF_PAID → ALUMNI`. Guards: `ACTIVE_*` requires appointment letter issued (or task open within 3 months for existing staff), statutory registrations done (UAN/ESIC where applicable); `SEPARATED` triggers the access revocation workflow and the F&F clock `wrk_wages_2wd`.

### 5.2 Leave request
`DRAFT → SUBMITTED → (APPROVED | REJECTED | RETURNED) → (CANCELLATION_REQUESTED → CANCELLED) → AVAILED`. Timer: auto-escalate to next approver after 2 working days (T); approvals by delegate when approver on leave.

### 5.3 Pay run (`hr.pay_runs.status`)
`OPEN → INPUTS_LOCKED → COMPUTED → (RECOMPUTE ↺) → SUBMITTED (maker) → CHECKED (checker ≠ maker) → RELEASE_AUTHORISED (releaser ≠ maker, ≠ checker) → BANK_FILE_ISSUED → DISBURSAL_CONFIRMED (bank response) → CLOSED`. Side: `REJECTED_BY_CHECKER → COMPUTED`. After `RELEASE_AUTHORISED` the run is immutable; corrections only via off-cycle Correction run (NN-02).

```
finalise(run):
  assert distinct(run.maker, run.checker, run.releaser)                 # NN-05
  for p in run.parameters_used:
      if p.status == NOT_CONFIRMED: fail(LDC-HR-040)
      if p.status == SECONDARY_ONLY and not ack(run, p): fail(LDC-HR-041)
  assert hash(recompute(run.inputs, run.param_versions)) == run.register_hash   # NN-22
  emit PayRunReleaseAuthorised
```

### 5.4 POSH case (`lab_posh.cases.status`)
`RECEIVED → (CONCILIATION_REQUESTED → CONCILIATED_CLOSED) | INQUIRY_OPEN → INQUIRY_IN_PROGRESS (clock 90 days) → REPORT_ISSUED (≤ 10 days) → EMPLOYER_ACTION_PENDING (≤ 60 days) → ACTION_TAKEN → CLOSED → (APPEAL_NOTED)`. Interim-relief sub-state. Clocks owned by Presiding Officer; lapses go to a sealed exception visible to the Presiding Officer and the employer's designated officer only (counts to Board).

### 5.5 Statutory register generation
`SCHEDULED → GENERATED (hash) → REVIEWED (HR admin) → SIGNED (authorised signatory; eSign/DSC optional) → PUBLISHED (DMS, locked)`. Regeneration after a correction creates a new version that references the earlier one.

### 5.6 Threshold crossing
Monthly `ThresholdEvaluationJob`: for each establishment and each threshold in Appendix T §T.2, compare headcount (per rule's counting basis: "any day in the preceding 12 months", "on any day of the accounting year", "employees" vs "workers") → on first crossing create obligation instances, tasks and notifications; on falling below, keep obligations until the rule says they cease (some continue, e.g., ESI once covered [VERIFY]).

### 5.7 Committee member term
`ACTIVE → EXPIRING (60 days) → RENEWED | REPLACED → ENDED`; replacement must keep composition rules valid at each instant (validator runs on the proposed future state).

---

## 6. Screens and UX

Menu: **People** (left rail) — Home, Employees, Organisation, Lifecycle, Time & Attendance, Leave, Payroll, Labour Compliance, Committees, POSH (visible only to IC members and HR admin for configuration), Policies & Training, Reports. Self-service: **My Work** › My Profile, My Attendance, My Leave, My Payslips, My Tax, My Documents, My Policies, My Training, Raise a grievance, Report sexual harassment (sealed).

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-HR-01 | People home | People | Headcount by entity/establishment/department, joiners/leavers, threshold alerts ("Bengaluru branch crossed 10 workers — OSH registration due"), labour compliance due list, payroll status card |
| SCR-HR-02 | Employee directory | People › Employees | Saved views, bulk import (XLSX template), bulk actions (assign policy, change manager with effective date, assign training) with preview and undo |
| SCR-HR-03 | Employee profile | (drill) | Tabs: Personal (minimal), Employment, Position & roles (platform roles shown), Pay, Leave, Attendance, Documents, Training, Assets, Committees & regulated roles, History (bitemporal) |
| SCR-HR-04 | Organisation designer | People › Organisation | Entity → establishment → department → function tree, drag-and-drop with preview of impacted users/tasks; compliance-department mapping column; org chart as-of date |
| SCR-HR-05 | Default structure picker | Onboarding / Organisation | Cards per entity family with preview; "adopt and edit" |
| SCR-HR-06 | Positions & regulated roles | People › Organisation › Positions | Regulated-role flags and validation chips (e.g., "CISO reports to Head of IT — violates RBI NBFC 2026 para 81") |
| SCR-HR-07 | Lifecycle board | People › Lifecycle | Kanban: requisitions, offers, pre-joining, probation reviews, exits; F&F clocks |
| SCR-HR-08 | Offer & agreement composer | (drill) | Template + clause library, stamp-duty prompt, eSign routing |
| SCR-HR-09 | Attendance | People › Time | Daily muster, exceptions, regularisations, overtime approvals, cap alerts |
| SCR-HR-10 | Leave console | People › Leave | Requests, team calendar, policy editor (floors shown as locked rows), year-end preview |
| SCR-HR-11 | Payroll cockpit | People › Payroll | Stepper (inputs → compute → variance → submit → check → release → bank file → reconcile); parameter status banner (NOT_CONFIRMED / SECONDARY_ONLY) |
| SCR-HR-12 | Variance review | (drill) | Employee × component diff, filters, explain-line ("i": which rule-pack version and formula) |
| SCR-HR-13 | Statutory outputs | People › Payroll › Statutory | ECR, ESIC, PT, LWF, TDS data files with validation results and acknowledgement upload |
| SCR-HR-14 | Labour compliance home | People › Labour Compliance | Obligation calendar by Code and State; registers; returns; registrations; notices displayed; state rule status matrix |
| SCR-HR-15 | Register viewer | (drill) | Register picker, period, establishment; PDF/XLSX; sign; history |
| SCR-HR-16 | Committees (HR) | People › Committees | GRC, Works, Safety — composition validators, meetings |
| SCR-POSH-01 | IC workspace | People › POSH | Sealed; IC list, member terms, case list (IC only), clocks, annual report |
| SCR-POSH-02 | Case file | (drill, sealed) | Timeline, statements, evidence, hearing schedule, report composer, access log |
| SCR-HR-17 | Policies & training | People › Policies & Training | Acknowledgement campaigns, completion heatmap, Academy links |
| SCR-HR-18 | People-risk KRIs | People › Reports › People risk | KRI tiles with thresholds; "send to risk register" |
| SCR-SS-01..08 | Self-service screens | My Work › … | Mobile-first PWA; one-tap check-in; leave in ≤ 3 taps; payslip download; tax declaration wizard; sealed POSH form reachable in ≤ 2 taps from My Work |
| SCR-HR-19 | Leave quick-apply *(v1.1)* | Me › Leave | Calendar with balance projection, team overlap, one-tap submit |
| SCR-HR-20 | Approval cards *(v1.1)* | Work Inbox / e-mail / Teams | Approve/reject with reason; Review next |
| SCR-HR-21 | Payroll what-if simulator *(v1.1)* | People › Payroll › Simulator | Scenario builder, comparison, export |
| SCR-HR-22 | Contractor portal *(v1.1)* | Contractor (external) | Upload by establishment and month; status of checkpoints |
| SCR-HR-23 | Letters on demand *(v1.1)* | Me › Letters | Request, auto-generate, download with QR |
| SCR-HR-24 | Labour penalty exposure *(v1.1)* | People › Labour compliance | Indicative exposure by establishment/State with disclaimer |
| SCR-HR-25 | Apprentices *(v1.1)* | People › Apprentices | Contracts, stipend, quota tracker |

Accessibility: payslips available as tagged PDF and accessible HTML; screen-reader-friendly leave calendar (list view alternative); captions on tutorial videos; high-contrast theme (NN-21).

---

## 7. Backend design

### 7.1 Modules
`hr` (people, org, lifecycle, time, leave, payroll), `lab` (labour obligations, registers, returns, committees bridge, registrations), `lab_posh` (sealed), using `cfg` (rule packs `rulepack.IN.payroll.*`, `rulepack.IN-<ST>.payroll.*`, `ita25-salary-tds`, `infrabyx-labour-rulepack`), `gov` (persons, committees), `wf`, `dms`, `cmp`, `erm`, `int`, `acc`.

### 7.2 Tables (selected; all with tenant/legal-entity, bitemporal columns, RLS)

| Table | Key columns |
|---|---|
| `hr.establishments` | legal_entity_id, type, state_code, district, address, reg_numbers jsonb, rule_pack_ids[], holiday_calendar_id |
| `hr.departments` / `hr.functions` / `hr.teams` | name, parent_id, head_person_id, compliance_dept_code |
| `hr.positions` | title, grade, department_id, reports_to_position_id, sensitive bool, regulated_role_code, approved_headcount |
| `hr.persons` (view on `gov.persons` + HR attributes) | name, dob, pan_token, uan, esic_ip, digilocker_verified_on, disability_selfdecl (sealed) |
| `hr.employments` | person_id, legal_entity_id, employee_code, type, worker_class, joined_on, confirmed_on, separated_on, status |
| `hr.assignments` | employment_id, position_id, establishment_id, manager_employment_id, from/to, secondment_host_entity |
| `hr.bank_accounts` | employment_id, token, last4, ifsc, verified_at, changed_by, change_held_until |
| `hr.attendance_events` / `hr.attendance_days` | source, ts, method, geo_hash(optional); computed day status, hours, ot_minutes |
| `hr.shifts` / `hr.rosters` | — |
| `hr.leave_policies` / `hr.leave_balances` / `hr.leave_requests` | floor_rule_ref, accrual, carry_cap; balance by type; request status |
| `hr.salary_structures` / `hr.components` / `hr.employee_salaries` | component class, taxable_map, pf_applicable, esi_applicable |
| `hr.pay_runs` / `hr.pay_lines` / `hr.pay_run_params` | period, status, maker/checker/releaser, register_hash; per employee per component amount; param_version_id per line |
| `hr.bank_files` / `hr.disbursal_results` | layout, file_hash, issued_at; status per credit |
| `hr.tax_declarations` / `hr.tax_proofs` | regime, items, proof doc ids |
| `lab.obligations_view` | (view over `cmp.instances` filtered to LAB packs) |
| `lab.registers` / `lab.register_versions` | register_code, establishment_id, period, file ids, hash, signed_by |
| `lab.returns` / `lab.return_runs` | form_code, format_status, file, ack_ref |
| `lab.registrations` | kind, number, valid_to |
| `lab.contractors_deployments` | contractor_vendor_id, establishment_id, headcount, licence_ref, monthly_challan_evidence |
| `lab_posh.ics` / `lab_posh.ic_members` / `lab_posh.cases` / `lab_posh.case_events` / `lab_posh.access_log` | separate schema, separate KMS key |
| `hr.training_records` / `hr.policy_acks` | course_ref, completed_at, cert_doc; policy_version_id, acked_at |
| `hr.fit_proper_cycles` | person_id, year, declarations[], nrc_review_ref, status |
| `hr.people_kri_values` | metric_code, period, value, grain (entity/department), threshold_version |

### 7.3 APIs
`/v1/hr/employees` (CRUD, import), `/v1/hr/employments/{id}:confirm|transfer|separate`, `/v1/hr/org/tree?as_of=`, `/v1/hr/attendance/events` (punch ingest, device API keys), `/v1/hr/leave/requests`, `/v1/hr/pay-runs` (`:lock-inputs`, `:compute`, `:submit`, `:check`, `:authorise-release`, `:issue-bank-file`, `:import-bank-response`), `/v1/hr/statutory/{ecr|esic|pt|lwf|tds}?period=`, `/v1/lab/registers/{code}?establishment=&period=&format=`, `/v1/lab/returns/{form}:prepare`, `/v1/posh/cases` (sealed realm, IC-member tokens only), `/v1/hr/kri?period=` (aggregates), SCIM `/scim/v2/Users` (outbound to Keycloak; inbound from Entra/Google when directory is source).

### 7.4 Domain events (`in.lawdocscomply.hr.*` / `.lab.*`)
`EmployeeHired`, `EmploymentConfirmed`, `EmployeeTransferred`, `RegulatedRoleAssigned`, `RegulatedRoleVacated`, `EmployeeSeparated`, `AccessRevocationRequested`, `LeaveApproved`, `PayRunComputed`, `PayRunReleaseAuthorised`, `BankFileIssued`, `DisbursalReconciled`, `StatutoryFileGenerated`, `RegisterPublished`, `ThresholdCrossed`, `CommitteeCompositionInvalid`, `POSHCaseClockBreached` (sealed: payload = IC id + counts only), `TrainingOverdue`, `PeopleKRIPublished` (Ecosystem `workforce` scope; aggregates).

### 7.5 Jobs and Temporal workflows
`PayRunWorkflow`, `FnFWorkflow` (2-working-day clock), `GratuityPaymentWorkflow` (30-day clock), `ThresholdEvaluationJob` (monthly), `AttendanceDayCloseJob` (nightly), `LeaveAccrualJob` (monthly), `YearEndLeaveJob`, `RegisterGenerationJob` (monthly/annual), `StatutoryCalendarJob`, `WorkspaceJMLWorkflow`, `RuleWatchWorkflow` (VDA cycles 1 Apr / 1 Oct, budgets, EPFO/ESIC circulars, State notifications — creates review tasks for the Payroll Compliance Officer; Appendix T §T.7), `POSHClockWorkflow`, `FitAndProperAnnualJob` (before 31 March / AGM cycle per tenant), `PeopleKRIJob`.

---

## 8. Integrations

`WORKSPACE_PORT` (M365 Graph: users, licences, groups, Teams, calendar out-of-office; Google Admin SDK; manual IT-desk fallback), `ATTENDANCE_DEVICE_PORT` (biometric/door-access vendors; CSV SFTP), `BANK_FILE_PORT` (bank layouts; RazorpayX Payroll/Payouts adapter behind `hr.payout.razorpayx.enabled = OFF`), `ACCOUNTING_PORT` (P11 `acc`, Tally Prime XML import format, Finbyx GL via Ecosystem `finance` events), `ESIGN_PORT` and `ESTAMP_PORT` (P07/P18), `LMS_PORT` (FinLegal Academy, SCORM/xAPI), `BGV_PORT` (background verification vendors — results only), `KYC_PORT` (DigiLocker document pull with consent for joining documents; PAN verification via licensed provider), `ECOSYSTEM_PORT` (`governance`, `workforce` events — Ecosystem Spec §6.23), `SHRAM_PORTAL` (future, flag OFF until official APIs), `EPFO_ECR` (file only).

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `hr.org.default_structure` | T | by entity family | — | `ten_hr_admin` |
| `hr.attendance.methods` | T | [web] | web, pwa_geo, ip_attest, device_import, supervisor | `ten_hr_admin` after monitoring notice published (NN-25) |
| `hr.attendance.geo.enabled` | T | OFF | requires published notice + DPIA screening (P12) | `ten_hr_admin` + DPO |
| `hr.leave.policy.<code>` | T | template | ≥ statutory floor (validator) | `ten_hr_admin` |
| `hr.leave.mandatory_block_days` | T | 10 | 5–15 | CRO |
| `hr.leave.approval_escalation_days` | T | 2 | 1–10 | `ten_hr_admin` |
| `hr.payroll.cutoff_day` | T | 25 | 15–31 | Payroll checker |
| `hr.payroll.bank_detail_hold_days` | T | 5 | 0–10 | CFO |
| `hr.payroll.three_actor_release` | L | ON | — | — |
| `hr.payroll.rule_packs` | G | latest published per State | pinned per run | `plt_content_publisher` (content); tenant adopts version (T) |
| `hr.payout.razorpayx.enabled` | G | OFF | — | super admin after contract |
| `hr.workspace.mode` | T | OFF | OFF / NOTIFY_IT / PROVISION | `ten_admin` |
| `hr.leaver.revoke_minutes` | T | 15 | 1–240 | `ten_admin` |
| `hr.recruitment.candidate_retention_months` | T | 6 | 1–24 | DPO |
| `lab.posh.ic.term_years` | L | 3 (max) | ≤ 3 | — |
| `lab.posh.inquiry_days` | L | 90 | — | — |
| `lab.grc.enabled_threshold_workers` | G | 20 | per Code | content |
| `hr.kri.share_with_ecosystem` | T | OFF | aggregates only | `ten_admin` + DPO |
| `hr.leave.auto_approval_rules` *(v1.1)* | T | none | cannot cover sensitive-position blocks, LOP or own requests | `ten_hr_admin` + CHRO checker |
| `hr.approval.escalate_after_hours` *(v1.1)* | T | 48 | 4–168 | `ten_hr_admin` |
| `hr.approval.channels` *(v1.1)* | T | INBOX, EMAIL | INBOX, EMAIL, TEAMS | `ten_hr_admin` |
| `hr.bulk.undo_window_hours` *(v1.1)* | T | 24 | 1–72 (NN-49) | `ten_hr_admin` |
| `hr.letters.auto_fulfil` *(v1.1)* | T | ON | — | `ten_hr_admin` |
| `hr.contractor_portal.enabled` *(v1.1)* | T | OFF | — | `ten_hr_admin` |
| `hr.penalty_exposure.visible_to` *(v1.1)* | T | CHRO, CCO, CFO | roles | CHRO |
| `hr.ethics.declaration_cycle` *(v1.1)* | T | annual + event | annual/semi-annual + event | CCO |

---

## 10. Security, privacy and audit

- Employee data is personal data of the tenant's employees; LDC acts as the tenant's processor. The P12 notice designer generates the employee/applicant privacy notice; processing activities for HR are pre-seeded in the tenant's ROPA (P12 §4B).
- Payroll data class **Confidential–Pay**: individual pay visible to the employee, payroll roles, the employee's management chain only if tenant policy allows (default: no), and auditors (masked bank). Payroll exports encrypted (password-protected XLSX/ZIP with password via separate channel or SFTP).
- Bank details tokenised; bank file generated in memory and stored encrypted with hash; download requires step-up MFA (P01).
- POSH, disciplinary, health-adjacent fields are sealed classes (NN-13) — separate keys, excluded from search, analytics and Vidhi.
- Monitoring transparency (NN-25): no keystroke logging, screenshots, webcam or continuous location; attendance and work measurement are disclosed by a published monitoring notice with employee acknowledgement before activation.
- Every computation stores input snapshot hash + parameter versions (NN-22); every register version hashed and ledgered (NN-02, NN-09).
- Labour inspector requests: export bundle (registers + returns + notices displayed evidence) with BSA s.63 certificate; time-boxed viewer grant optional (D-12 pattern).

---

## 11. AI touchpoints and guardrails

| Touchpoint | Vidhi does | Guardrail |
|---|---|---|
| Letters and agreements | Drafts offer/appointment/relieving letters and agreement clauses from templates | Uses approved clause library; flags non-compete (s.27); human approves; eSign by humans only |
| Policy drafting | Drafts leave/WFH/code-of-conduct/POSH policy aligned to template and previous version, with tracked changes (P07) | Floors validated by rule engine, not by AI |
| Payslip explanation | Explains a line ("why did PF change in September?") citing parameter version | Read-only; uses the stored computation trace |
| Committee minutes | Drafts GRC/Works/Safety committee minutes from notes (P06) | Not available for POSH case content (sealed) — only the annual report narrative from counts |
| Labour Q&A | Answers from labour notebooks (Codes, Central Rules, State rules) with citations | Says when a State rule is not yet notified (`state_rule_status`) |
| People-risk narrative | Drafts KRI commentary for the CRO | Aggregates only |
| Prohibited | Hiring/firing/promotion/pay recommendations about individuals; sentiment or productivity scoring of individuals from communications | Hard-blocked tools (NN-14; OH "people decisions stay human") |

---

## 12. Acceptance criteria (`tests/acceptance/p13/*.feature`)

```gherkin
Feature: Thresholds
  Scenario: Crossing 10 workers opens OSH and ESI obligations
    Given establishment "Noida Branch" in Uttar Pradesh has 9 workers
    When the 10th worker joins on 3 November 2026
    Then obligation instances for OSH registration and ESI coverage are created with owner HR
    And a notification is sent to the HR admin and the CS

Feature: Payroll three actors
  Scenario: Same person cannot check and release
    Given pay run "Nov-2026" computed by maker "M"
    And checked by "C"
    When "C" attempts to authorise release
    Then the system rejects with LDC-CORE-005

  Scenario: NOT_CONFIRMED parameter blocks finalisation
    Given an employee in Maharashtra and PT slab status NOT_CONFIRMED
    When the checker attempts to check the run
    Then the system blocks with LDC-HR-040 naming parameter "pt.IN-MH.slabs"

  Scenario: Reproducibility
    Given pay run "Oct-2026" was released
    When the auditor triggers recompute
    Then the recomputed register hash equals the stored register hash

Feature: Leave floors
  Scenario: Tenant policy below statutory floor rejected
    When HR saves an annual leave policy granting 1 day per 25 days worked for workers
    Then the system rejects with LDC-HR-021 citing OSH Code s.32

Feature: POSH sealing
  Scenario: HR admin without IC membership cannot read a case
    Given user "H" with role ten_hr_admin and not an IC member
    When "H" opens case "POSH-2026-004"
    Then access is denied and the attempt is logged in the POSH access log

  Scenario: IC composition validator
    When HR saves an IC with 4 members of whom 1 is a woman
    Then the save is blocked with LDC-LAB-011 "At least one-half of IC members must be women (POSH Act s.4(2))"

Feature: Separation
  Scenario: Leaver access revoked and tasks reassigned
    Given employee "E" holds 12 open compliance tasks and is a member of the Risk Management Committee
    When "E" is separated effective 18:00 today
    Then LDC sessions for "E" end by 18:15
    And the re-assignment wizard lists 12 tasks and 1 committee seat for the department head
    And the F&F clock of 2 working days starts

Feature: Regulated-role validation
  Scenario: CISO reporting line warning
    Given an NBFC-ML tenant
    When HR sets the CISO position to report to the Head of IT
    Then a compliance exception is raised citing RBI NBFC Cyber Directions 2026 para 81

Feature: v1.1 people speed and controls
  Scenario: Auto-approval never covers a sensitive-position block
    Given auto-approval rule "CL <= 1 day" is ON
    And employee "Ravi" holds a sensitive treasury position with an open mandatory-leave block
    When Ravi applies for 1 day casual leave inside the block window
    Then the request is routed to the manager and not auto-approved

  Scenario: Wage-definition warning at design time
    Given a salary structure where allowances excluded from wages are 60% of total remuneration
    When the HR admin saves the structure
    Then a warning shows the 10% add-back to wages and its effect on PF and gratuity bases

  Scenario: What-if does not post
    Given a what-if scenario "10% increment"
    When it runs
    Then no pay run, register or ledger entry is created and every figure has lineage

  Scenario: Contractor upload closes principal-employer checkpoint after review
    Given contractor "SecureGuard" uploads its September PF ECR for the Jaipur establishment
    When the checker accepts the upload
    Then the checkpoint "Verify contractor PF remittance — Sep 2026" is complied with act date = ECR date (NN-48)

  Scenario: Adding a branch proposes State packs
    Given a new establishment in Rajasthan with 12 workers
    When the HR admin saves it
    Then State packs for S&E, PT, LWF and minimum wages are proposed with registrations due, for one-click adoption

  Scenario: Every register reproducible from HRMS data (IMP-114)
    Given a month of payroll and attendance data
    When registers are generated
    Then each Appendix T register for the establishment is produced without manual entry
```

NN tests: `NN-01_hr_rls`, `NN-02_pay_run_immutable_after_release`, `NN-05_payroll_three_actors`, `NN-12_no_aadhaar_number_stored`, `NN-13_posh_sealed_store`, `NN-22_payroll_recompute_hash`, `NN-25_monitoring_notice_required`, `NN-26_params_from_signed_pack_only`, `NN-29_policy_change_keeps_history`.

---

## 13. Deliverables and exit gate

Deliverables: `hr`, `lab`, `lab_posh` modules; default structures for 8 entity families; rule-pack adapters pinned to `infrabyx-labour-rulepack` and `ita25-salary-tds`; registers and statutory files for Central sphere + 5 launch States (DL, UP, RJ, MH, KA) with verification status; POSH module; employment-agreement templates and clause library; self-service PWA; workspace provisioning (M365 first); KRI feed; standalone SKU entitlements (P20); documentation and tutorials (P23 sources).

Exit gate: §12 scenarios green; payroll golden fixtures from the shared rule pack identical to OH10/Finbyx GV6 outputs; a pilot tenant's two parallel-run months reconcile to the tenant's existing payroll within ₹1 per employee per component (differences explained); every parameter used in pilot runs is `VERIFIED` or acknowledged `SECONDARY_ONLY`; accessibility audit of self-service.

---

## 14. Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P13-01 | State rules under the four Codes (most pending; old State rules continue) | Notifications in progress | Payroll Compliance Officer (content) | `state_rule_status` per State; obligations show "pending State rules" |
| OI-P13-02 | EPF wage ceiling ₹25,000 from 17 Sep 2026 and split-month method | Gazette text / EPFO guidance | Content | `SECONDARY_ONLY` with acknowledgement |
| OI-P13-03 | Bonus eligibility and calculation ceilings under CoW s.26 | Not notified | Content | `NOT_CONFIRMED` — bonus run blocked until resolved or opinion recorded |
| OI-P13-04 | ESIC contribution rates under CoSS | Notification check | Content | `SECONDARY_ONLY` |
| OI-P13-05 | Income-tax Rules 2026 form numbers (salary TDS statement, annual certificate) and due dates | Recent change | Tax content | `NOT_CONFIRMED` dates; files generated, due dates manual |
| OI-P13-06 | Prescribed wage-slip and unified register formats under Central Rules 2026 | Forms to be mapped | Content | Generic formats with all prescribed fields |
| OI-P13-07 | Remote-employee PT/LWF location rule | Legal opinion | CS / counsel | Tenant policy chooses work-location or establishment basis |
| OI-P13-08 | RBI current instrument for mandatory leave of staff in sensitive positions (banks/NBFCs) | Consolidation | RBI content | Tenant setting with [VERIFY] note |
| OI-P13-09 | Fit-and-proper declaration formats in consolidated RBI directions (NBFC, UCB, ARC) | Consolidation | RBI content | Generic F&P template |
| OI-P13-10 | Shram Suvidha / State portal return formats and any APIs | Portals evolving | CTO | File preparation only |
| OI-P13-11 | Whether Aadhaar last-4 is needed on any statutory form | Form review | Content | Not stored |
| OI-P13-12 | Board-report POSH disclosure list after Companies (Accounts) amendments | Verify current rule text | CS | Disclosure covers r.8(5)(x) + counts |
| OI-P13-13 *(v1.1)* | Apprenticeship portal, quota band and stipend rule numbers under current rules | Not re-verified | Payroll Compliance Officer | Feature flag `hr.apprentices.enabled` OFF until verified |
| OI-P13-14 *(v1.1)* | Income-tax Act 2025 salary certificate form number | Renumbered forms | Content (tax) | Letter template labelled generically |
| OI-P13-15 *(v1.1)* | Penalty bands per Code and compounding schedule | Rules partly notified | Content (labour) | Exposure hidden for bands not VERIFIED |

---

## 15. Sources (accessed 25 October 2026)

1. Equator v3.1 App Z §Z.2 (external pack) (Labour Code status, thresholds, clocks, parameter seed, State packs) and research note RC_LABOUR_PAYROLL (23–24 Oct 2026) — owner's Mac, `Equator Prompt/Equator Build Prompt Pack v3.1/`.
2. Infrabyx Ecosystem Integration Specification v1.1 §12.3 (shared Labour Code rule pack), §6.23 (governance and workforce events).
3. Ministry of Labour and Employment — Labour Codes, Central Rules and FAQs: https://labour.gov.in/labour-codes
4. POSH Act 2013 and Rules 2013: https://wcd.gov.in (Act text); SHe-Box: https://shebox.wcd.gov.in
5. RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions 2026 paras 81–82 (CISO): https://rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=13592
6. RBI (NBFC – Internal Ombudsman) Directions 2026 cl.5, 8 (IO eligibility/tenure): https://www.rbi.org.in/ScriptS/BS_ViewMasDirections.aspx?id=13274
7. Companies (Accounts) Rules 2014 r.8(5)(x): https://www.mca.gov.in
8. SEBI (Prohibition of Insider Trading) Regulations 2015: https://www.sebi.gov.in
9. Income-tax Act 2025 (in force 1 Apr 2026) s.392: https://www.incometax.gov.in

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-25, NN-26 (as before), X-10 (department codes), X-36 (aggregated people metrics); D-11 (no salary money held).

**Added in v1.1:** NN-48.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
