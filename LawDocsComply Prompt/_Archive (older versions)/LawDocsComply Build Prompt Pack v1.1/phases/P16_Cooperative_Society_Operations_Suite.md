# Phase P16 — Co-operative Society Operations Suite

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P15** (families `CCS` and `COOP`, entity profile, applicability engine, vocabulary pack `COOP`, State rule-pack framework);
> - **P04** (compliance instances, calendar, tasks, maker-checker);
> - **P06** (meetings, minutes, resolutions, statutory-register engine — reused with co-operative templates);
> - **P07** (bye-laws and policy versioning, DMS, eSign);
> - **P13** (staff HRMS for society employees), **P14** (complaints and grievance desk), **P18** (Finbyx/Udofin connectors), **P11** (Registrar/CRCS return preparation).
>
> **Sequencing:** starts after P15 sprint 2 (taxonomy frozen). MSCS and Maharashtra packs ship complete; other States ship as STUB packs completed with counsel at each client's onboarding (P15 FR-P15-49).
>
> **Binding appendices:** S (co-operative law and operations — the legal source for every rule here), G (rules register `LR-COOP-*`), E (template family `LDC-TPL-COOP-CCS` and `LDC-TPL-COOP-GEN`), I (Registrar/CRCS returns), M (export folder taxonomy — co-operative profile).
>
> **Requirements covered:** R-062, R-093, R-096, R-009, R-056 (co-operative variant), R-080 (member grievance), R-081, R-007, R-086.
>
> **Estimated effort:** 6 two-week sprints for a squad of 7 (registers and members 2; general body, elections and governance 2; audit, returns and credit-society monitors 2; UX/vernacular 1) plus a co-operative law analyst.

>
> **v1.1 changes (25 October 2026)**
> - New **§4R member self-service and multilingual communications**: member portal (LDC self-service shell for non-credit societies; Udofin for credit-society members, D-16), OTP-acknowledged notices, regional-language templates (Hindi first, D-30; Marathi, Gujarati, Kannada, Tamil, Telugu, Bengali, Malayalam, Punjabi, Odia on demand), WhatsApp for service notices only (X-23) (FR-P16-48–FR-P16-51).
> - New **§4S office-bearer workbench** — President, Secretary/CEO and **Treasurer** dashboards (Treasurer added as an office-bearer designation and `ten_kmp`-equivalent for funds approvals, G5), approvals from mobile, agenda-to-minutes in one flow (FR-P16-52–FR-P16-54).
> - New **§4T faster audit rectification** (audit memo OCR → para-wise action tracker → auto-compiled rectification report per State form) and **§4U Registrar inspection/inquiry tracker and members' register-inspection protocol** (G5 TM-111) (FR-P16-55–FR-P16-59).
> - New **§4V AI assistance with bounded autonomy** (bye-law clause extraction, regional-language drafting, AGM pack assembly; NN-47, NN-50) and **§4W customisation catalogue** (FR-P16-60–FR-P16-62).
> - Elections remain conducted by the Co-operative Election Authority / State Election Authority; LDC supports and records (X-34). Act/evidence/approval dates (NN-48) applied to Registrar returns.
---

## 1. Objective and business outcome

India has about 8.4 lakh co-operatives with about 32 crore members across 30 sectors (National Cooperative Database, as reported by PIB, February 2026), and thousands of credit co-operative societies that hold members' savings without RBI supervision, DICGC cover or a modern governance system. Many still keep registers in paper books, hold AGMs late, miss Registrar returns, carry unrectified audit paras for years, and lose their boards to disqualification under the Act. Failures such as the Adarsh Credit Co-operative Society case (Central Registrar notices and liquidation) show what weak member-eligibility, related-party and audit controls cost depositors.

This phase delivers an **end-to-end operating system for a co-operative society** — registration facts and bye-laws, members and shares, managing committee and office bearers, general body meetings, elections support, statutory registers, funds and appropriation, audit and rectification, Registrar/CRCS returns, inspections, complaints and member communications — with the society's GRC (compliance, risk, audit) on the same platform. For **credit co-operative societies**, loans, deposits, interest and share accounting stay in Finbyx (D-16) and members borrow and repay through Udofin; LDC runs governance, compliance and the prudential monitors.

| Outcome | Exit-gate measure |
|---|---|
| Society runs its affairs in LDC | Pilot Maharashtra credit society and a pilot MSCS can, without LawDocs staff help: admit a member, hold a managing-committee meeting with minutes, convene and record an AGM, file the annual return package, record audit paras and file the rectification report — all within statutory clocks |
| No statutory clock lapses unnoticed | AGM, annual return, audit, rectification, election-notice and director-disqualification clocks each have an owner, alerts at T-60/T-30/T-7 days and escalation; an expired clock without action is a Critical issue (NN-31 pattern) |
| Correct law per society | The engine selects the MSCS Act or the correct State Act pack, and the society's bye-laws as a versioned tighten-only layer; a State with a STUB pack shows "limited coverage" and blocks no operations |
| Credit-society safety | Deposit-eligibility exceptions (deposits only from active voting members), director/relative loan reporting, prudential monitors (CRCS order of 22 Jan 2024 for MSCS; State Act for others) and the "no bank in name" guard are live and visible to the board and auditors |
| Ecosystem coherence | For a society on Finbyx, the member register and share ledger are read from Finbyx (single system of record); for a society not on Finbyx, LDC is the system of record and can export the same contracts to any LOS |
| Vernacular and accessible | Hindi and Marathi labels shipped; notices generated bilingual; WCAG 2.2 AA (NN-21) |

---

## 2. Scope (in / out)

**In scope**
- Society master, legal profile and bye-laws (versioned; amendment workflow with Registrar approval) (§4A).
- System-of-record switch for members and shares (Finbyx vs LDC) (§4B).
- Member and share registers, nominations, transfers, cessation, member classes and rights (§4C).
- Managing committee/board, office bearers, co-option, reservations, disqualifications, recusal and related-party controls (§4D).
- General body meetings (AGM, SGM), notices, quorum, agenda, resolutions, minutes, bye-law amendments (§4E).
- Elections support: term tracking, notices to the election authority, voter lists, programme tracker, results recording; internal office-bearer elections by the board (§4F).
- Committees and meetings (reuse P06) (§4G); statutory registers (§4H).
- Funds, reserves and appropriation view (§4I).
- Audit, audit classification, rectification, concurrent and special audits, inspections and inquiries (§4J).
- Returns to Registrar/CRCS and tax filings calendar (§4K).
- Member complaints and escalation to Registrar/Co-operative Ombudsman (§4L).
- Member communications (§4M).
- Credit-society specifics and Finbyx/Udofin link (§4N); other society types (§4O).
- State rule packs (§4P); amalgamation, liquidation and winding-up events (§4Q).

**Out of scope**
- Loans, deposits, interest, share accounting, dividend postings and recovery execution for credit societies — Finbyx (Part 7G IP2) (D-16, NN-23).
- Member borrowing and repayment journeys — Udofin (Part 7E MG1–MG4, Part 7B UP4).
- Conducting statutory elections — the Co-operative Election Authority (MSCS) or the State Co-operative Election Authority/Commission conducts them; LDC supports the society's obligations and keeps records. Online voting in statutory elections is out of scope unless the authority itself prescribes it.
- Milk procurement, PDS, fertiliser distribution and other sector-specific trading operations (out; adapters only, e.g., the national PACS ERP).

---

## 3. Personas and permissions touched

| Role | P16 use |
|---|---|
| `ten_admin` | Society admin: configures society master, bye-laws, users, packs |
| `coop_office_bearer` (sub-type: CHAIRPERSON, VICE_CHAIRPERSON, SECRETARY, TREASURER, DIRECTOR, CO_OPTED_EXPERT, FUNCTIONAL_DIRECTOR) | Approves admissions (as committee), signs minutes, convenes meetings, owns statutory filings |
| `ten_kmp` (CEO/Manager, COMPLIANCE_OFFICER, INFORMATION_OFFICER) | Day-to-day maker for registers, notices and returns |
| `ten_maker`, `ten_checker` | Clerks and accountants (maker) and manager/secretary (checker) |
| `coop_member` | Member portal (optional): own share and membership details, notices, AGM papers, complaint filing, nomination update request; voting list check |
| `coop_returning_officer` | Read-only voter list, nomination and result recording screens during an election programme (time-boxed grant) |
| `ten_external_auditor` (panel auditor), `ten_internal_auditor`, concurrent auditor | Read-only registers, minutes, ledgers projection; audit para recording |
| `ten_supervisor_view` (Registrar / Central Registrar inspector) | D-12 time-boxed read-only grant |
| `dlv_rm`, `dlv_professional` | LawDocs retainer team as maker under tenant grant (R-072) |
| `svc_vidhi` | Drafts notices, minutes, rectification replies, returns narratives; extracts data from scanned registers (NN-04, NN-14) |

---

## 4. Functional requirements

### 4A. Society master, legal profile and bye-laws

**FR-P16-01 Society master.** Name (validated by guard-rail GR-COOP-01: no "bank", "banker" or "banking" in the name or materials of a non-bank co-operative — BR Act s.7 as applicable to co-operative societies under s.56, effective 29 Sep 2020 per the Banking Regulation (Amendment) Act 2020 [VERIFY effective date]), registration number and date, governing Act (`MSCS_2002` or State Act code), State(s) of operation (MSCS: at least two States), area of operation (districts, talukas, villages; employer for salary-earner societies), society type (P15 `CCS`/`COOP` types), class/sub-class under the State classification (e.g., Maharashtra Rule 10 classification) [VERIFY], registered office, branches, financing bank (DCCB/StCB or other), federation memberships, PAN, GSTIN, TAN, bank accounts (masked), statutory auditor, number of members by class, deposits (credit societies), staff count.

**FR-P16-02 Constitutional context.** The pack records that Part IXB of the Constitution (Arts. 243ZH–243ZT, inserted by the 97th Amendment, 2011) applies to multi-State co-operative societies and those in Union Territories only, following *Union of India v. Rajendra N. Shah* (Supreme Court, 20 July 2021), which held Part IXB inoperative for State co-operatives for want of ratification [LAW; verify citation in Appendix S]; State societies are governed by their State Act, which in most States already mirrors Part IXB features (5-year term, election authority, reservation). Rules referencing Part IXB therefore attach only to `CCS_MSCS`/`MSCS_OTHER`/UT societies unless the State Act contains the equivalent.

**FR-P16-03 Bye-laws as a versioned rule layer.** Bye-laws are uploaded (DOCX/PDF), structured by Vidhi into clauses (member classes, admission fee, share face value and holding cap, loan and deposit rules for credit societies, board size, quorum, notice periods, office-bearer terms, appropriation, dividend, disputes), confirmed by the secretary (maker) and chairperson (checker). Structured values become a **L3 rule layer** that can only tighten the Act/Rules (L0) and Registrar orders (L1); a bye-law value that loosens a higher layer is rejected with `LDC-COOP-001 RULE_LOOSENING_BLOCKED` and shown with the governing provision (Finbyx IP1.3 pattern).

**FR-P16-04 Bye-law amendment workflow.** `DRAFTED → COMMITTEE_APPROVED → GENERAL_BODY_NOTICE (≥ 15 days for MSCS where a special majority is required [VERIFY], per State pack otherwise) → GENERAL_BODY_PASSED (two-thirds of members present and voting, MSCS s.11 [VERIFY]) → SUBMITTED_TO_REGISTRAR (within the prescribed period) → REGISTERED | RETURNED_FOR_CORRECTION | REFUSED → EFFECTIVE`. Only `REGISTERED` amendments change the L3 layer; the previous version remains in history (NN-07). Model bye-laws published by the CRCS or State Registrar are seeded as templates.

### 4B. System-of-record switch for members and shares

**FR-P16-05** Setting `coop.sor.members` ∈ {`FINBYX`, `LDC`, `EXTERNAL_LOS`} per society, Governed (requires CCO/secretary + chairperson approval and a migration plan):
- **FINBYX** (default for credit societies on Finbyx): Finbyx IP2.3–IP2.4 is the system of record for the member register and share ledger; LDC holds a **governance projection** (member id, class, status, voting eligibility, State/area, nominee present flag, share count band) refreshed from `MemberAdmitted`/`ShareCapitalPosted` events and a nightly `member_register_v1` file (Integration Spec §6.24, §3.11). LDC never edits these records; edits deep-link to Finbyx.
- **LDC** (default for non-credit societies and for credit societies without Finbyx): LDC is the system of record; it emits the same contracts (`MemberAdmitted`, `ShareCapitalPosted`, membership API) so that any certified LOS (or Udofin via Finbyx) can consume them later without redesign (R-002).
- **EXTERNAL_LOS**: a third-party core system pushes the register through the generic file contract; LDC holds the projection as for FINBYX.
- A switch never loses data: the outgoing system exports the full register with hash-chain heads, the incoming imports and reconciles counts and share totals before the effective date; dual-running for one month [REC] (NN-10, NN-11).

### 4C. Member and share registers

**FR-P16-06 Member classes and rights** (State/MSCS pack; bye-law may tighten): `ORDINARY_VOTING`, `NOMINAL`, `ASSOCIATE` (meaning per State: in Maharashtra a joint holder not first-named), `NON_VOTING_SHAREHOLDER` (MSCS s.26 proviso), `INSTITUTIONAL`. Rights matrix (vote, deposit, borrow, surety, attend general body, dividend) as in Appendix S §S.4 (deposit right only for active voting members — MSCS s.67 Explanation; MCS Act s.144-5A; BUDS Act 2019 First Schedule).

**FR-P16-07 Admission.** Application (paper upload, branch entry, member portal, or Udofin via the membership-application API when SoR = LDC) → scrutiny (area of operation, eligibility under bye-laws, KYC — Aadhaar never stored in full, NN-12) → committee decision with resolution reference → communication with reasons for refusal. **Timers:** MSCS — decision within 4 months and communication within 15 days, else deemed refused (s.25(4) as amended 2023) [VERIFY]; State per pack (e.g., Maharashtra s.22 — refusal communicated with reasons within the prescribed period; appeal to Registrar) [VERIFY]. Deemed refusal raises a Critical compliance issue.

**FR-P16-08 Registers maintained.** Member register (Maharashtra Form I; list of members Form J; MSCS Rules 2023 register of members [VERIFY form names]), share register, nomination register, transfer register, cessation register (resignation, expulsion with bar period — 3 years under the 2023 MSCS amendment [VERIFY], death with nominee claim workflow), defaulter list (voting disqualification where bye-laws/Act provide), associate/nominal member list. Every register is generated from the event log and reproducible as at any date (NN-07, NN-22).

**FR-P16-09 Share rules (SoR = LDC).** Allotment, instalment, transfer (approval; minimum holding period per bye-laws), refund/redemption at face value, forfeiture, lien; holding cap (≤ one-fifth of share capital or bye-law/Act limit); no finance to buy shares; no redemption while the member or a surety is in default (credit societies). For SoR = FINBYX these are Finbyx functions; LDC shows the register projection and governance checks only.

**FR-P16-10 Member 360 (governance).** Membership status and class, voting eligibility for the next general body/election (with reason if ineligible — e.g., default, non-attendance rules, minimum transactions under some State Acts [VERIFY: "active member" definitions such as Maharashtra s.26–27]), nominations, complaints, notices served, attendance history.

### 4D. Managing committee/board, office bearers and disqualification

**FR-P16-11 Composition rules (pack).** MSCS: board of not more than 21 directors, with reservation of one seat for SC/ST and two for women (MSCS s.41 as amended 2023) and up to two co-opted experts (without voting rights for office-bearer elections) [VERIFY sections]; term of five years (s.45 / Art. 243ZJ); office bearers (chairperson, vice-chairperson and others per bye-laws) elected by the board. State Acts per pack (e.g., Maharashtra s.73AAA board size and reservations [VERIFY]). Functional directors (CEO) as per Act.

**FR-P16-12 Office-bearer register.** Name, designation, category (elected/co-opted/nominated/functional), date of election/appointment, term end, KYC (DIN not applicable; internal ID), declarations (disqualification, related parties, other society memberships), attendance, training (some State Acts require training of directors [VERIFY]), committee memberships.

**FR-P16-13 Disqualification watch.** Rules per Act (e.g., MSCS s.43: default in repayment, convicted, interest in contracts, failure of the board to hold AGM/file returns/conduct elections leading to disqualification for five years [VERIFY sub-clauses]; Maharashtra s.73CA). The engine computes each director's exposure to a disqualification trigger (days to AGM deadline, days to annual return deadline, election notice deadline, own loan default status from Finbyx projection) and shows a **countdown dashboard**; at T-30 days the chairperson and secretary receive a High notification; at breach a Critical issue opens with the consequence text (R-093).

**FR-P16-14 Related-party and recusal controls.** Director/relative register; loans to directors and relatives (credit societies) tracked from Finbyx with aggregate limit per bye-laws (Finbyx IP2.6 step 4) and reporting to the AGM (MSCS s.39(3) — annual report to include loans to directors and relatives [VERIFY]); recusal recorded in minutes for any agenda item where the director is interested; non-unanimous decisions register (MSCS 2023 amendment requires disclosure in the annual report [VERIFY]).

**FR-P16-15 Board supersession and administrator.** If the Registrar supersedes the board or appoints an administrator/committee (e.g., MSCS s.123; Maharashtra s.78/78A [VERIFY]), the tenant enters `ADMINISTRATOR_MODE`: the administrator user receives the board's approval rights; the event is recorded with order reference; election-to-new-board clock starts.

### 4E. General body meetings (AGM/SGM)

**FR-P16-16 AGM clock.** MSCS: within six months of the close of the financial year (s.39) — escalation at month 4 and 5; State per pack (e.g., Maharashtra s.75: on or before 30 September) [VERIFY]. If the board fails, the Registrar may convene (MSCS s.39 proviso / State equivalent), recorded as an event.

**FR-P16-17 Notice and agenda pack.** Notice period (MSCS 14 clear days for AGM, 7 for SGM [VERIFY]; State per pack), mode (post, email, SMS/WhatsApp with DLT templates, notice board, newspaper where required), bilingual. Agenda pack builder: annual report (board report incl. non-unanimous decisions and director/relative loans), audited accounts, audit report and rectification report, appropriation proposal (§4I), budget, appointment of auditor from the Registrar's panel, bye-law amendments, write-offs (where General Body approval is required, e.g., Maharashtra Rule 49), election of delegates, any member resolutions. Vidhi drafts; secretary approves.

**FR-P16-18 Quorum and conduct.** Quorum per Act/bye-laws (e.g., one-fifth of members or a fixed number, whichever is less [VERIFY per Act]); adjourned-meeting rules; attendance capture (register, QR check-in, or roll call); voting by show of hands/ballot per bye-laws; proxy prohibited unless the Act allows [VERIFY]; minutes drafted from the agenda and recorded decisions, approved and signed by the chairperson within the prescribed period (e.g., 30 days); minutes book generated (reuse P06 minutes engine with co-operative template).

**FR-P16-19 Hybrid/virtual meetings.** Permitted only where the Act, Rules, bye-laws or a Registrar circular allows (setting `coop.gbm.virtual_allowed`, Governed, default OFF with citation required).

### 4F. Elections support

**FR-P16-20 Term tracker and notices.** For each board, term end date (5 years), and the statutory notice to the election authority: MSCS — inform the Co-operative Election Authority at least six months before the expiry of the board's term (s.45J(8) as inserted 2023) [VERIFY]; Maharashtra — State Co-operative Election Authority (MCS Act s.73CB) under the Maharashtra Co-operative Societies (Election to Committee) Rules 2014 with society classification A/B/C/D for election procedure [VERIFY]; other States per pack.

**FR-P16-21 Election programme tracker.** Stages modelled as a programme set by the authority: `PROVISIONAL_VOTER_LIST → OBJECTIONS → FINAL_VOTER_LIST → NOTIFICATION → NOMINATIONS → SCRUTINY → WITHDRAWAL → SYMBOL_ALLOTMENT (if any) → POLL → COUNTING → RESULT_DECLARED → BOARD_CONSTITUTED → OFFICE_BEARER_ELECTION`. The society's tasks (prepare and certify the voter list from the member register as at the cut-off date, deposit election expenses, provide premises/records, publish notices) are compliance instances with owners; dates come from the authority's programme, entered by the secretary with the notification uploaded. The voter list is generated from the register with eligibility reasons and is exportable in the authority's prescribed format (XLSX/PDF) [VERIFY format per authority].

**FR-P16-22 Returning officer access.** Time-boxed, read-only grant (D-12 pattern) for the returning officer to view the certified voter list and record results; results recorded become the new board composition after the secretary confirms with the authority's declaration.

**FR-P16-23 Internal elections.** Elections of office bearers by the board (chairperson, vice-chairperson) and of committee members can be run as minuted board items with ballot recording; electronic secret ballot (flag `coop.internal_eballot.enabled`, OFF) only where bye-laws allow.

**FR-P16-24 Election disputes.** Petitions under the Act (e.g., MSCS s.84 disputes; State election-petition provisions) tracked as litigation matters (P06 litigation register) with hearing dates.

### 4G. Committees and meetings

**FR-P16-25** Reuse P06 meeting lifecycle for board/managing-committee meetings (frequency per Act/bye-laws, e.g., at least once in three months [VERIFY]), sub-committees (loans, recovery, audit and ethics, staff, purchase), with co-operative templates (notice, agenda, minutes, resolution register). Quorum and interested-director rules apply. Minutes and resolutions are signed by the chairperson (eSign or wet-ink upload).

### 4H. Statutory registers and records

**FR-P16-26 Register engine.** Generates and maintains, per pack: register of members; share register; nomination register; register of directors/committee members; minutes books (general body, board, sub-committees); register of loans to directors and relatives (credit societies, from Finbyx); register of investments; register of assets/dead stock; register of borrowings; cash book and ledgers (projection from accounts — not an accounting system); complaints register; register of audit paras and rectification; register of inspections; register of notices received from Registrar; RTI/information requests register (MSCS 2023: Information Officer [VERIFY section]). Each register prints in the statutory format (where prescribed) and in a standard XLSX/PDF for export (Appendix M co-operative folder profile).

**FR-P16-27 Records retention and inspection by members.** Members' right to inspect certain records (Act/bye-laws) handled as a request workflow with fee, timeline and redaction of other members' personal data (DPDP: legitimate use under statute; NN-12).

### 4I. Funds, reserves and appropriation view

**FR-P16-28** LDC shows (from Finbyx or the society's accounts/Tally import, P11 accounting bridge) the profit and the statutory appropriation proposal with validations: MSCS — at least 25% of net profit to reserve fund, 1% to the Co-operative Education Fund, at least 10% to a reserve for unforeseen losses, and the Co-operative Rehabilitation, Reconstruction and Development Fund contribution of the lesser of ₹1 crore and 1% of net profit where profitable in each of the preceding three years (ss.63, 63A as amended 2023); dividend within the prescribed cap; State per pack (e.g., Maharashtra s.66 reserve ≥ 25%, s.67 dividend cap, s.68 education fund, Rule 52 dividend equalisation) [VERIFY rates in Appendix S]. Proposal approved by the board, then the general body; posting is in Finbyx/accounts. Board and AGM agenda items are created automatically.

### 4J. Audit, audit class, rectification, inspections

**FR-P16-29 Auditor appointment.** From the Registrar's/Central Registrar's panel (MSCS s.70; special panel where turnover or deposits exceed ₹500 crore [VERIFY]); appointed by the general body; consent and intimation to the Registrar within the prescribed period (e.g., Maharashtra s.81 — within one month of the AGM [VERIFY]); rotation limit (e.g., three consecutive years in Maharashtra [VERIFY]).

**FR-P16-30 Audit completion clocks.** MSCS — audit report within six months [VERIFY s.70(3A)]; Maharashtra — within four months of the year end (s.81) [VERIFY]; concurrent audit where turnover/deposits > ₹500 crore (MSCS s.70A) [VERIFY].

**FR-P16-31 Audit paras and audit class.** Audit observations are imported (structured from the report by Vidhi; confirmed by the secretary) into the audit-para register with category, amount, responsibility, due date; the audit class (A–D, e.g., Maharashtra Rule 69 with Form N-2 marks [VERIFY bands]) is recorded per year and drives class-dependent rules (election procedure class, write-off fund eligibility, dashboards).

**FR-P16-32 Rectification report.** Maharashtra — rectification report in Form O within three months of the audit report (s.82) [VERIFY]; MSCS and other States per pack. Each para has an owner, rectification action, evidence and status; overdue paras escalate to the board; the rectification report is generated in the prescribed format and filed by an authorised person (NN-08).

**FR-P16-33 Special audit, inspection and inquiry.** Registrar-ordered special audit, inspection (e.g., MSCS s.108), inquiry (e.g., Maharashtra s.83) and surcharge proceedings (e.g., Maharashtra s.88) [VERIFY] tracked as matters with document requests, response drafts (Vidhi) and timelines; regulator user access via D-12 grant.

### 4K. Returns and filings

**FR-P16-34 Registrar/CRCS returns.** MSCS — annual return within six months of the close of the financial year to the Central Registrar through the CRCS portal (s.120 as amended 2023), including audited accounts, appropriation, bye-law amendments, board election details, and other prescribed items [VERIFY list]; CRCS quarterly prudential return for credit MSCS (CRCS order of 22 Jan 2024) [VERIFY]; State returns per pack (e.g., Maharashtra s.79(1A) annual statements within six months; returns on the State co-operative department portal [VERIFY portal]). Return Studio (P11) prepares; humans file (NN-08, D-13).

**FR-P16-35 Tax and other filings calendar.** Income-tax return and the co-operative deduction under the Income-tax Act 2025 (successor of s.80P of the 1961 Act) [VERIFY section], TDS statements, GST (where registered), professional tax, labour registers (P13), FIU-IND (only if the society is a reporting entity — generally not [VERIFY]), CERSAI (if creating security interests [VERIFY applicability to societies]).

### 4L. Member complaints and grievances

**FR-P16-36** Complaint intake (member portal, branch, email, WhatsApp, letter scan) into the P14 desk with co-operative routing: society grievance officer → (MSCS) Co-operative Ombudsman under s.85A (notified 5 Mar 2024; complaints on deposits, equitable benefits or individual rights; decision timelines per the Act and Rules [VERIFY 3-month decision and appeal to Central Registrar]) / (State) Registrar or the State's grievance mechanism → Consumer Commission where applicable. The RBI Ombudsman route is never shown to members of non-bank societies (they are outside RB-IOS 2026; Integration Spec §6.24). Disputes touching the constitution, management or business of the society are signposted to the statutory forum (MSCS s.84 arbitration; Maharashtra s.91 Co-operative Court) and private arbitration is blocked (GR-COOP-05; Finbyx GR-7G-05).

### 4M. Member communications

**FR-P16-37** Notice templates (AGM, SGM, election-related, dividend, share call, defaulter notices, rectification, general circulars) in English, Hindi, Marathi (v1.0) and other scheduled languages via translation (P07) with human approval; channels: email, SMS and WhatsApp (DLT-registered templates, TRAI TCCCPR), letters (print-to-post), notice-board PDF; delivery logs as evidence; quiet hours and opt-outs for non-statutory messages; statutory notices are not suppressible by opt-out.

### 4N. Credit-society specifics, Finbyx and Udofin

**FR-P16-38 Prudential monitors (read from Finbyx RK6/IP2.7 or imported).** For `CCS_MSCS`: CRCS order L-11012/01/2023-Reg (22 Jan 2024) [REG; VERIFY order text] — size class (Micro ≤ ₹10 crore deposits; Small ≤ ₹100 crore; Medium ≤ ₹500 crore; Large > ₹500 crore), CRAR 9% (Micro/Small) and 12% (Medium/Large) on the glide path to 2028-29, cash ≥ 2% of deposits, liquid investments rising to 18% of deposits, leverage (deposits + borrowings ≤ 10 × (paid-up capital + reserves − accumulated losses)), single 15% / group 25% exposure of Tier I + II capital, unsecured loans ≤ 15% of loans, housing loans only by Medium (≤ ₹1 crore) and Large (≤ ₹1.2 crore) societies, quarterly return; branch-expansion eligibility (CRCS order, July 2025: GNPA < 7%, NNPA < 3%, profit in each of three years, CRAR met, State Registrar certificate on no deposits from non-voting members) [VERIFY]. For `CCS_STATE` in Maharashtra: Chapter XI-1A of the MCS Act (ss.144-5A to 144-30A: no non-member deposits; SLR ≥ 25% of deposits; administrative-expense cap; Regulatory Board regulations; Stabilisation and Liquidity Support Fund) [VERIFY %]. Other States per pack. These are **legal limits under the society's own Act, not RBI ratios**, and are labelled so (P15 vocabulary).

**FR-P16-39 Deposit-eligibility exception register.** Every Finbyx `GR-7G-01` exception (deposit from a non-voting/nominal/associate member or non-member) is mirrored in LDC as a Critical compliance issue with board alert, root cause, refund/remediation plan and evidence; the count is a standing agenda item for every board meeting until zero.

**FR-P16-40 Director and relative loans.** Aggregate and per-director loans (projection from Finbyx, pseudonymised for non-board users) vs bye-law cap; inclusion in the annual report and AGM agenda (FR-P16-14).

**FR-P16-41 Recovery and dispute matters.** Statutory recovery tracks (Maharashtra s.101 recovery certificate for notified classes, s.91 Co-operative Court, s.98 execution; MSCS s.84 arbitration and s.94-type recovery [VERIFY]) are recorded in LDC's litigation register as matters with hearing dates and outcomes (Finbyx R1 owns case operations; LDC receives `RecoveryCaseOpened`/`LitigationCaseUpdated` for governance reporting).

**FR-P16-42 Udofin member experience.** Members discover, apply for membership and loans, and repay through Udofin (web and assisted channels; mobile per Udofin's app-store position [VERIFY]) under the member-only track; Udofin never lists, solicits or collects deposits (Integration Spec §6.24 hard blocks). When SoR = LDC, LDC exposes `POST /v1/societies/{id}/membership-applications` and `GET /v1/societies/{id}/members/{ref}` exactly as specified there; the statutory admission timer starts on receipt.

**FR-P16-43 Guard-rails shown as compliance controls.** No "bank" in name (GR-COOP-01); deposits only from voting members (GR-COOP-02); no co-lending, loan sale/purchase or DLG with NBFCs (TDCR paras 7, 12(4), 97; CF para 19) (GR-COOP-03); no loans on the security of own shares and no non-member surety (MSCS s.66(1)) (GR-COOP-04); no private arbitration of statutory-forum disputes (GR-COOP-05); RBI Ombudsman not offered (GR-COOP-06). Guard-rails are Locked (NN-28).

**FR-P16-44 DICGC disclosure.** Member-facing documents generated by LDC for a credit society carry the statement that deposits are not insured by DICGC [REC; Finbyx IP2.5].

### 4O. Other society types

| Type | Specific features (seed; extensible) |
|---|---|
| `HOUSING` | Member/flat register with share certificate linkage, nomination, transfer of flats and premium/transfer fee per bye-laws and State rules (e.g., Maharashtra model bye-laws for housing societies and s.154B provisions for housing societies [VERIFY]), maintenance and sinking/repair fund tracking (from accounts), NOC register, parking allotment register, conveyance/deemed-conveyance matter tracker, redevelopment decision workflow (special general body, consent records, Registrar directives [VERIFY]), complaints |
| `PACS` | Adapter to the national common ERP for computerised PACS (79,630 sanctioned; 61,025 onboarded per PIB, Feb 2026) — read-only compliance projection; multipurpose activities register (CSC, PDS, fertiliser, Jan Aushadhi) as obligations only; DCCB/StCB linkage |
| `DAIRY`, `FISHERIES`, `MARKETING`, `CONSUMER`, `PRODUCER_COOP` | Governance, registers, AGM, audit and returns core; sector licences (FSSAI, APMC/market licences, fisheries registrations) as obligations via overlays |
| `LABOUR_CONTRACT` | Labour overlay (P13) prominence; contract registers; work-order register |
| `FEDERAL` | Member-society register (institutional members), delegates, representation rules |
| `MSCS_OTHER` | MSCS Act and Rules 2023 core (registration in ≥ 2 States, CEA elections, CRCS returns, Co-operative Ombudsman) |

### 4P. State rule packs

**FR-P16-45 Pack variables.** Each State pack fills the same variable set (Appendix S §S.7 matrix): governing Act and Rules; Registrar hierarchy; classification of societies; member classes and "active member" rules; admission timeline and appeal; board size, reservations, co-option, term; disqualification grounds; election authority and election rules; AGM deadline, notice, quorum; appropriation and dividend caps; audit appointment, timeline, rotation, classification, rectification form and timeline; annual return contents and deadline; dispute forum and recovery route; credit-society prudential chapter (if any); special provisions for housing societies; State portals; languages.

**FR-P16-46 Completeness.** Shipped complete: `MSCS` (Act 2002 as amended 2023, Rules 2023, CRCS orders, model bye-laws) and `MH` (Maharashtra Co-operative Societies Act 1960 and Rules 1961, election rules 2014, Chapter XI-1A). STUB with variables pre-listed: Gujarat (Gujarat Co-operative Societies Act 1961), Rajasthan (Rajasthan Co-operative Societies Act 2001, Rules 2003), Uttar Pradesh (UP Co-operative Societies Act 1965, Rules 1968), Delhi (Delhi Co-operative Societies Act 2003, Rules 2007), Karnataka (Karnataka Co-operative Societies Act 1959; Karnataka Souharda Sahakari Act 1997), Madhya Pradesh (MP Co-operative Societies Act 1960), Telangana (Telangana/Andhra Pradesh Mutually Aided Co-operative Societies Act 1995 and the Co-operative Societies Act 1964 [VERIFY current status]), Bihar (Bihar Self-Supporting Co-operative Societies Act 1996 and Bihar Co-operative Societies Act 1935), Kerala (Kerala Co-operative Societies Act 1969), Tamil Nadu (TN Co-operative Societies Act 1983) [VERIFY each]. A society in a STUB State can use every operational feature; legal clocks show as "configure from your Act" tasks until counsel completes the pack.

### 4Q. Amalgamation, division, liquidation

**FR-P16-47** Events modelled as governance matters: amalgamation/transfer of assets and liabilities/division (general body special resolution, creditor notice, Registrar approval), conversion (e.g., credit society to UCB requires RBI licence — out of scope beyond checklist), liquidation (Registrar order, liquidator appointment, claims register, LDC records frozen to read-only for the liquidator with export, NN-10). Deregistration closes the tenant only after export confirmation.

---


### 4R. Member self-service and multilingual communications *(v1.1)*

**FR-P16-48 — Member portal.** For societies where LDC is the member SoR (`coop.sor.members = LDC`) members use the `selfservice` shell (X-13): profile and nominee updates (maker-checker by the society), share certificate download, notices and AGM papers, attendance confirmation, register-inspection requests (§4U), complaints (P14). For credit societies on Finbyx, the member experience is Udofin (D-16) and LDC shows only governance items (AGM, elections support, notices) via deep link.

**FR-P16-49 — Notices that reach members.** AGM/SGM notices, election programme notices (as issued by the authority), bye-law amendment notices and dividend/interest-on-share notices go out by SMS (DLT templates), e-mail, WhatsApp service template (never for recovery or legal demand notices, X-23), notice-board PDF and member portal; delivery and OTP acknowledgements become evidence for the statutory notice checkpoint with act date = dispatch date (NN-48).

**FR-P16-50 — Regional languages.** Templates for notices, minutes extracts, member letters and the member portal UI in Hindi first (D-30), then Marathi, Gujarati, Kannada, Tamil, Telugu, Bengali, Malayalam, Punjabi and Odia as tenants request; statutory text is never machine-translated without human review; bilingual (regional + English) output by default for Registrar filings where the State accepts English [VERIFY per State].

**FR-P16-51 — Low-bandwidth and assisted mode.** Branch staff can record member acknowledgements on a tablet/PWA offline and sync later; large-print and audio (text-to-speech) versions of notices for members with low vision (NN-21).

### 4S. Office-bearer workbench *(v1.1)*

**FR-P16-52 — Role dashboards.** President (board agenda, pending approvals, disqualification watch, audit class trend), Secretary/CEO (statutory calendar, registers, returns, member complaints), **Treasurer** (reserve-fund and statutory-fund appropriation status, dividend/interest-on-share limits, investment-of-funds compliance under the Act and bye-laws, cash-handling and bank reconciliation evidence — the books themselves stay in Finbyx or the society's accounting system, D-16). Treasurer is an office-bearer designation (`coop_office_bearer` with designation TREASURER) with approval rights configured by bye-laws.

**FR-P16-53 — Mobile approvals.** Office bearers approve admissions, transfers, refunds and agenda items from mobile with step-up authentication; approvals follow bye-law authority limits (configured once) and never let the requester approve (NN-05).

**FR-P16-54 — Agenda-to-minutes in one flow.** Pending items (admissions, audit paras, returns, Registrar letters, loan-policy changes for credit societies) auto-populate the managing-committee agenda; minutes are drafted by Vidhi from the agenda and notes in the chosen language, reviewed and signed (P06 mechanics; NN-36), and resolution entries update the relevant registers automatically.

### 4T. Faster audit rectification *(v1.1)*

**FR-P16-55 — Audit memo intake.** Upload the statutory audit memo/report (PDF/scan); OCR with type copy (P07) splits it into paragraphs with para numbers, amounts and audit class; the secretary confirms the split in one screen.

**FR-P16-56 — Para-wise tracker.** Each para gets an owner, action, evidence and due date (State timelines for the rectification report [VERIFY per State, e.g., Maharashtra Form O]); status roll-up per audit class; repeated paras across years are linked.

**FR-P16-57 — Auto-compiled rectification report.** The rectification report in the State's prescribed format (or MSCS format) is generated from the tracker, with board approval link and dispatch evidence; the AGM pack includes the audit report and rectification status as the Act requires.

### 4U. Registrar inspection/inquiry tracker and register-inspection protocol *(v1.1; G5 TM-111)*

**FR-P16-58 — Registrar inspections and inquiries.** Track inspections, inquiries and surcharge proceedings initiated by the Registrar or CRCS (with State-pack section references [VERIFY]): letters received (OCR), observations as action items, replies with approvals, hearing dates on the calendar, outcomes; links to P26 legal matters where proceedings become contentious.

**FR-P16-59 — Members' right to inspect.** Members' requests to inspect or obtain copies of the bye-laws, registers (own entries), audit report, balance sheet and minutes of general body meetings, as permitted by the Act and bye-laws: request intake, eligibility check, fee computation (State pack), inspection slot or certified copy generation, statutory response time clock (NN-33), log of what was shown; sealed and other members' personal data are redacted automatically.

### 4V. AI assistance with bounded autonomy *(v1.1)*

**FR-P16-60 — What Vidhi does here.** Extracts bye-law clauses into the rule layer (FR-P16-03) for human confirmation; drafts notices, minutes and member letters in regional languages; assembles the AGM pack; summarises Registrar letters into action items; answers office bearers' questions from the State Act notebook with citations (NN-06). Autonomy default L1 (draft/propose) — no member admission, disqualification finding, election matter or Registrar reply is decided or sent by AI (NN-47, NN-50).

### 4W. Customisation catalogue *(v1.1)*

**FR-P16-61 — Tenant options.** Member classes and fees within the Act, committee names, office-bearer designations and authority limits, notice channels and languages, agenda templates, register column extras, member-portal features, reminder ladders for returns and rectification.

**FR-P16-62 — Federation view.** District/State federations and multi-unit societies may view aggregates of affiliated societies that grant access (group view, aggregates only, NN-24 not applicable cross-border but the same aggregation principle).


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P16-X01 — Registrar proceedings as legal matters.** Registrar inquiries, surcharge proceedings, arbitration references and appeals under the State Act or MSCS Act are opened as P26 legal matters (type `REGISTRAR_PROCEEDING`) with the society's office bearers as owners; P16 shows them in the society dashboard.

## 5. Workflows and state machines

### 5.1 Membership admission (SoR = LDC)

`APPLIED → SCRUTINY → COMMITTEE_QUEUE → APPROVED | REJECTED | DEEMED_REFUSED → ACTIVE ⇄ DEFAULTER → RESIGNED | EXPELLED | DECEASED → LIABILITY_TAIL → CLOSED`.
Guards: `APPROVED` only with resolution reference; `REJECTED` requires written reasons; `DEEMED_REFUSED` automatically at the statutory deadline with Critical issue; expulsion requires general body/board procedure per Act and records the bar date. Timers: statutory decision and communication windows; ex-member liability tail (e.g., two years per bye-laws [VERIFY]). Events: `MemberAdmitted`, `MemberStatusChanged`.

### 5.2 AGM

`PLANNED (auto at FY end) → PAPERS_IN_PREPARATION → BOARD_APPROVED_NOTICE → NOTICE_SERVED (≥ notice days) → HELD | ADJOURNED → MINUTES_DRAFTED → MINUTES_SIGNED → FILINGS_DONE`; side state `DEFAULTED` (deadline passed) → Critical issue + director-disqualification countdown + "Registrar may convene" note.

### 5.3 Election support

`TERM_TRACKED → AUTHORITY_INFORMED (≥ 6 months before term end for MSCS) → PROGRAMME_RECEIVED → VOTER_LIST_PREPARED → VOTER_LIST_CERTIFIED → [authority-led stages tracked] → RESULT_RECORDED → BOARD_CONSTITUTED → OFFICE_BEARERS_ELECTED`; `DELAYED` if the authority has not issued a programme by term end (records correspondence; interim arrangements per Act).

### 5.4 Audit and rectification

`AUDITOR_APPOINTED → AUDIT_IN_PROGRESS → REPORT_RECEIVED → PARAS_STRUCTURED → RECTIFICATION_IN_PROGRESS → RECTIFICATION_REPORT_FILED → REGISTRAR_REVIEW → CLOSED | REOPENED`. Timers per pack; overdue para escalation at 30/60/90 days.

### 5.5 Bye-law amendment
See FR-P16-04.

### 5.6 Disqualification watch (pseudo-code)

```
daily for each director d in board:
  for trigger in pack.disqualification_triggers:     // e.g. AGM_NOT_HELD, RETURN_NOT_FILED, ELECTION_NOT_CONDUCTED, LOAN_DEFAULT
     exposure = trigger.evaluate(society, d, today)   // uses clocks and Finbyx projection
     if exposure.days_to_breach <= 30: notify(chair, secretary, HIGH, trigger.consequence_text)
     if exposure.breached: open_issue(CRITICAL, d, trigger, citation)
```

---

## 6. Screens and UX

| Screen ID | Name | Menu path |
|---|---|---|
| SCR-COOP-01 | Society home (dashboard) | Home — tiles: next AGM, annual-return countdown, audit paras open, deposit-eligibility exceptions (credit), board term end, director disqualification watch, complaints open |
| SCR-COOP-02 | Society master and legal profile | Settings › Society |
| SCR-COOP-03 | Bye-laws | Governance › Bye-laws (versions, structured clauses, amendment workflow) |
| SCR-COOP-04 | Members register | Members › Register (filters class/status/area/defaulter; Admit member wizard; Form I/J exports) |
| SCR-COOP-05 | Member 360 | Members › Register › Member |
| SCR-COOP-06 | Shares register | Members › Shares (SoR LDC: transactions; SoR Finbyx: read-only projection with deep link) |
| SCR-COOP-07 | Board and office bearers | Governance › Board (composition vs rules, terms, declarations, disqualification watch) |
| SCR-COOP-08 | General body meetings | Governance › General Body (AGM/SGM planner, notice and agenda builder, attendance, minutes) |
| SCR-COOP-09 | Elections | Governance › Elections (term tracker, authority notices, programme tracker, voter list) |
| SCR-COOP-10 | Statutory registers | Records › Registers (print/export each) |
| SCR-COOP-11 | Appropriation | Finance › Appropriation (proposal with validations, approvals) |
| SCR-COOP-12 | Audit and rectification | Audit › Statutory audit (auditor, paras, class history, Form O/rectification) |
| SCR-COOP-13 | Registrar returns | Returns › Registrar / CRCS |
| SCR-COOP-14 | Inspections and inquiries | Compliance › Registrar matters |
| SCR-COOP-15 | Credit-society monitors | Risk › Prudential (CRCS/State limits), Deposit-eligibility exceptions, Director loans |
| SCR-COOP-16 | Member portal | Member › My membership, Notices, AGM papers, Complaints |
| SCR-COOP-17 | Returning-officer view | Elections › Officer (time-boxed) |
| SCR-COOP-18 | Member portal *(v1.1)* | Self-service › Society |
| SCR-COOP-19 | Office-bearer workbench (President / Secretary / Treasurer) *(v1.1)* | Home (role-based) |
| SCR-COOP-20 | Audit para tracker and rectification report *(v1.1)* | Audit › Rectification |
| SCR-COOP-21 | Registrar inspections and inquiries *(v1.1)* | Compliance › Registrar |
| SCR-COOP-22 | Register inspection requests *(v1.1)* | Members › Inspection requests |

UX: vernacular toggle (EN/HI/MR) on every screen; large-text mode; voice-readable notices; one-click "prepare AGM pack" (Vidhi drafts everything for review); bulk notice dispatch with preview and delivery log; offline-friendly register import from Excel/scans with Vidhi OCR and human verification (P07); empty-state copy explains the legal reason for each register.

---

## 7. Backend design

### 7.1 Modules
`coop` (owner), `pack`, `gov`, `dms`, `cmp`, `wf`, `grv`, `ret`, `int`, `ai`, `rpt`.

### 7.2 Tables (key columns)

| Table | Key columns |
|---|---|
| `coop.society` | tenant_id, legal_entity_id, act_code, state_codes[], reg_no, reg_date, type, class, area_json, sor_members, financing_bank, status |
| `coop.byelaw_version` | society_id, version, doc_id, structured_json, state (DRAFT…EFFECTIVE), registrar_ref, effective_from |
| `coop.member` (SoR LDC) / `coop.member_projection` (SoR FINBYX/EXTERNAL) | member_ref, class, status, admitted_at, area_check, nominee_ids, voting_eligible, eligibility_reason, source_event_id |
| `coop.share_txn` (SoR LDC) | member_ref, txn_type, shares, amount, approval_ref, posted_at |
| `coop.application` | applicant_ref, channel, received_at, decision_due_at, communication_due_at, state, resolution_ref, reasons |
| `coop.office_bearer` | person_id, designation, category, elected_on, term_end, declarations_doc_ids, status |
| `coop.disqualification_watch` | person_id, trigger_code, days_to_breach, breached_at, issue_id |
| `coop.general_body_meeting` | type, fy, due_by, notice_served_at, held_at, quorum_met, minutes_doc_id, state |
| `coop.election_cycle` | board_term_end, authority_code, informed_at, programme_json, voter_list_doc_id, result_doc_id, state |
| `coop.register_def` / `coop.register_snapshot` | register_code, format_ref; snapshot as_of, doc_id, hash |
| `coop.appropriation` | fy, net_profit, allocations_json, validations_json, board_approval_ref, gb_approval_ref |
| `coop.audit_cycle` / `coop.audit_para` | fy, auditor_id, appointed_ref, report_doc_id, audit_class; para no, category, amount, owner, action, evidence_doc_ids, status, due_at |
| `coop.registrar_matter` | type (INSPECTION, INQUIRY, SPECIAL_AUDIT, SURCHARGE, SUPERSESSION), order_ref, due_dates, state |
| `coop.prudential_snapshot` | as_of, source, metrics_json, breaches_json |

### 7.3 APIs
- `GET/PATCH /v1/coop/society`; `GET/POST /v1/coop/byelaws`, `POST /v1/coop/byelaws/{v}/submit|register`
- `GET/POST /v1/coop/members`, `POST /v1/coop/members/{ref}/status`; `GET /v1/coop/registers/{code}?asOf=`
- Integration Spec membership APIs (`/v1/societies/{id}/membership-applications`, `/v1/societies/{id}/members/{ref}`) when SoR = LDC
- `GET/POST /v1/coop/general-body-meetings`, `/v1/coop/elections`, `/v1/coop/audit-cycles`, `/v1/coop/audit-paras`, `/v1/coop/appropriations`, `/v1/coop/registrar-matters`
- `GET /v1/coop/prudential`

### 7.4 Domain events (`in.lawdocscomply.coop.*.v1`)
`SocietyActivated`, `ByelawAmendmentRegistered`, `MemberAdmitted` (SoR LDC; Integration Spec name), `MemberStatusChanged`, `ShareCapitalPosted` (SoR LDC), `MembershipDeemedRefused`, `GeneralBodyMeetingHeld`, `GeneralBodyMeetingDefaulted`, `ElectionAuthorityInformed`, `BoardConstituted`, `DirectorDisqualificationRisk`, `AuditReportReceived`, `RectificationReportFiled`, `RegistrarReturnFiled`, `DepositEligibilityExceptionMirrored`. Consumed: Finbyx `MemberAdmitted`, `ShareCapitalPosted`, `LimitBreached`, `RecoveryCaseOpened`, `LitigationCaseUpdated`; Udofin membership applications (via API).

### 7.5 Jobs
`CoopClockWatcher` (daily 06:00 IST: AGM, return, audit, rectification, election notice, admission timers); `DisqualificationWatch` (daily); `MemberProjectionSync` (event-driven + nightly file reconciliation with count/total checks); `PrudentialSnapshotImport` (monthly / on Finbyx event); `RegisterSnapshot` (on demand and at FY end, hashed).

---

## 8. Integrations
`ECOSYSTEM_PORT` (Finbyx IP2, Udofin MG/UP4 via Integration Spec §6.24); `REGISTRAR_PORTAL_PORT` (export packages for CRCS/State portals; no credentials stored — D-04 vault optional for the society's own use); `MESSAGING_PORT` (DLT SMS, WhatsApp Business, email, print-to-post); `PACS_ERP_PORT` (national PACS software, read-only, [VERIFY] API availability); `ACCOUNTING_PORT` (Tally/Excel for societies without Finbyx, P11); `ESIGN_PORT` (D-20).

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `coop.sor.members` | G | FINBYX for CCS on Finbyx; else LDC | FINBYX/LDC/EXTERNAL_LOS | ten_admin + chairperson (migration plan) |
| `coop.act_pack` | L | from society master | published packs | content team |
| `coop.byelaw.layer_enabled` | T | true | — | secretary + chair |
| `coop.agm.escalation_months` | T | [4,5] after FY end (MSCS) | tighten only | secretary |
| `coop.clock.warning_days` | T | [60,30,7] | tighten only | secretary |
| `coop.gbm.virtual_allowed` | G | false | needs citation | chair + content check |
| `coop.internal_eballot.enabled` | T | false | bye-law permits | chair |
| `coop.member_portal.enabled` | T | false | — | ten_admin |
| `coop.languages` | T | [en, hi] (+ mr for MH) | catalogue | ten_admin |
| `coop.notice.channels` | T | [email, sms, notice_board] | statutory minimum enforced | secretary |
| `coop.disqualification.alert_days` | T | 30 | 7–90 | secretary |
| `coop.deposit_exception.board_agenda_auto` | L | true | — | — |
| `coop.guardrails.*` | L | on | — | — |
| `coop.languages` *(v1.1)* | T | [en, hi] | Eighth-Schedule languages with published templates | secretary |
| `coop.notice.channels` *(v1.1)* | T | SMS, EMAIL, PORTAL, NOTICE_BOARD | + WHATSAPP_SERVICE | secretary |
| `coop.treasurer.approval_limits` *(v1.1)* | T | per bye-laws | ≤ Act limits | managing committee resolution |
| `coop.inspection.fee_table` *(v1.1)* | G (State pack) + T | State pack | ≥ 0 | secretary |
| `coop.ai.autonomy_level` *(v1.1)* | T | L1 | L0–L1 (NN-50) | secretary |

---

## 10. Security, privacy and audit
- Member personal data is minimised: Aadhaar never stored (NN-12); phone/email encrypted; voter lists exported only for the authority and watermarked.
- Member portal users see only their own records (RLS + ABAC, NN-01); inspection-of-records requests redact other members' data.
- Registers and minutes are hash-chained and immutable; corrections via Correction Entry (NN-02, D-02).
- Returning officer and Registrar access are time-boxed grants with logs visible to the society (NN-18, NN-30).
- Complaints marked sensitive (fraud allegations, harassment) follow sealed classes (NN-13).

---

## 11. AI touchpoints and guardrails
- **Register digitisation:** Vidhi OCRs scanned paper registers (Marathi/Hindi/English handwriting and print) into draft rows with confidence; clerk verifies row by row; nothing posts without verification (NN-04, NN-14).
- **Bye-law structuring:** Vidhi maps clauses to the variable set and flags conflicts with the Act; secretary decides.
- **AGM pack drafting:** notice, agenda, annual report narrative, appropriation note and rectification replies drafted with citations; chairperson approves.
- **Member Q&A notebook:** a society-scoped notebook (Act, Rules, bye-laws, circulars) answers members' and staff questions with citations (NN-06), never personal advice on disputes.
- Vidhi never admits or expels a member, certifies a voter list, files a return or signs minutes.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p16/*.feature`)

```gherkin
Feature: Co-operative operations

  Scenario: Deemed refusal of membership (MSCS)
    Given an MSCS credit society with SoR = LDC
    And an application received on 2026-06-01 with no committee decision
    When the clock watcher runs on 2026-10-02
    Then the application state is DEEMED_REFUSED
    And a Critical compliance issue cites the MSCS Act admission provision

  Scenario: Bye-law cannot loosen the Act
    Given the MSCS pack allows deposits only from voting members
    When the secretary structures a bye-law clause permitting deposits from nominal members
    Then the clause is rejected with LDC-COOP-001 and the governing provision is shown

  Scenario: AGM default triggers disqualification watch
    Given an MSCS society whose FY ended on 2026-03-31 and no AGM recorded
    When the date is 2026-09-01
    Then each director shows a disqualification risk countdown of 29 days
    And the chairperson receives a High notification

  Scenario: Election authority notice
    Given an MSCS board whose term ends on 2027-04-15
    When the date reaches 2026-10-15 without an "authority informed" record
    Then a Critical issue is raised for the CEA notice obligation

  Scenario: Finbyx is system of record
    Given a credit society with SoR = FINBYX
    When a clerk tries to edit a member's class in LDC
    Then the edit is refused with LDC-COOP-007 and a deep link to Finbyx is shown
    And the projection updates after Finbyx emits MemberStatusChanged or the nightly file reconciles

  Scenario: Deposit-eligibility exception mirrored
    Given Finbyx raises a GR-7G-01 exception for an FD held by a NOMINAL member
    When LDC receives the event
    Then a Critical issue appears on the board dashboard and the next board meeting agenda

  Scenario: Appropriation validation (MSCS)
    Given net profit of 2 crore and profit in each of the preceding three years
    When the board proposes 20% to the reserve fund
    Then validation fails with "reserve fund at least 25%"
    And a CRRD Fund line of 2 lakh is required

  Scenario: Rectification clock (Maharashtra)
    Given an audit report received on 2026-07-15 for a Maharashtra society
    Then the rectification report due date is 2026-10-15
    And on 2026-10-16 the item is overdue and escalated to the board

  Scenario: RBI Ombudsman not offered
    Given a member complaint in a credit society
    When the complaint is escalated
    Then the escalation options include the Co-operative Ombudsman (MSCS) or the Registrar
    And do not include the RBI Ombudsman

  Scenario: No "bank" in name
    Given a society master with the name "Shree Sahakari Bank Credit Society"
    When activation is attempted
    Then activation fails with GR-COOP-01

  Scenario: STUB State pack
    Given a Rajasthan credit society on a STUB pack
    When the admin opens the AGM planner
    Then the AGM deadline field asks "configure from your Act" with a task to counsel
    And all operational features remain available

Feature: v1.1 society speed features
  Scenario: Notice delivery becomes evidence with act date
    Given an AGM notice dispatched by SMS and e-mail on 01 Aug 2026
    Then the statutory notice checkpoint records act date 01 Aug 2026 and the delivery report as evidence

  Scenario: Audit memo becomes a para tracker
    Given an uploaded audit memo with 23 paras
    When the secretary confirms the OCR split
    Then 23 action items are created with owners and the rectification report draft lists all 23

  Scenario: Member inspection request redacts other members' data
    Given member "M-1042" requests copies of the member register
    Then only M-1042's own entry and non-personal summary fields are produced and the request clock is shown

  Scenario: AI cannot decide disqualification
    Given Vidhi summarises a Registrar letter alleging default by a director
    Then a disqualification-watch item is proposed for the secretary and no status is changed automatically
```

NN tests: `NN-02_coop_register_immutable`, `NN-07_register_as_at_replay`, `NN-12_no_aadhaar_in_member_record`, `NN-23_finbyx_sor_no_edit`, `NN-28_coop_guardrails_locked`, `NN-31_coop_clock_owned`.

---

## 13. Deliverables and exit gate
1. `coop` schema with RLS, registers engine, clocks, workflows and events above.
2. MSCS and Maharashtra packs complete (variables, templates, notices, forms) and STUB packs for nine States.
3. Member projection sync with Finbyx and membership APIs per Integration Spec §6.24 (contract tests).
4. Screens SCR-COOP-01–17 with EN/HI/MR; member portal behind flag.
5. Export profile for co-operatives in LDC-EXPORT-1.0 (top-level folder `15 Co-operative Society Records/` with sub-folders `Bye-laws`, `Members register and share capital`, `Managing Committee`, `General Body Meetings`, `Elections`, `Statutory audit by co-operative auditor`, `Returns to Registrar`, `Complaints and disputes`; registers, compliance and other records sit in the standard top-level folders 03–24 — Appendix M §M.3 names are authoritative, X-27) (P19, Appendix M).
6. Docs: `docs/coop/state-pack-<code>.md`, `docs/coop/sor-switch.md`.

**Exit gate:** §12 scenarios and NN tests green; pilot MSCS and pilot Maharashtra credit society run one full annual cycle in staging (AGM, return, audit, rectification) with synthetic data; counsel sign-off on MSCS and MH packs.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P16-01 | MSCS section numbers for board composition, reservations, CEA notice (s.45J(8)), Information Officer, compliance officer, Audit and Ethics Committee, non-unanimous decisions disclosure | 2023 amendment text not re-read this session | Content (co-op counsel) | Rules carry instrument-level citations | P16 |
| OI-P16-02 | CRCS order of 22 Jan 2024 and July 2025 branch order texts | Secondary sources | Content | Monitors labelled `[VERIFY]` | P16 |
| OI-P16-03 | Maharashtra audit-class bands, Form O timeline, Chapter XI-1A percentages, election rules 2014 classification | Secondary sources | Content (MH counsel) | Pack ships with [VERIFY] markers; values Governed | P16 |
| OI-P16-04 | State Acts other than MSCS/MH | Not researched to section level | Content per onboarding | STUB packs | P16 |
| OI-P16-05 | Income-tax Act 2025 successor of s.80P | 2025 Act numbering | S5 / tax | Show "co-operative deduction" without section | P11/P16 |
| OI-P16-06 | Virtual/hybrid general body meetings legality per Act | Varies by State | Content | `coop.gbm.virtual_allowed` OFF | P16 |
| OI-P16-07 | Voter-list formats prescribed by CEA and State authorities | Not obtained | Content | Generic XLSX/PDF | P16 |
| OI-P16-08 | National PACS ERP API availability | Not public | Integrations | Manual upload | P18 |
| OI-P16-09 | Udofin app-store position for non-RE lenders | Udofin open item | Udofin team | Web/assisted only | Udofin |
| OI-P16-10 | Rajendra N. Shah citation details and State-Act mirror provisions | Verify judgment cite | Content | Rule text with case name only | P16 |
| OI-P16-11 *(v1.1)* | Members' inspection rights, fees and response times per State Act | Varies by State | Co-op law analyst | State stub uses MSCS defaults with [VERIFY] | P16 |
| OI-P16-12 *(v1.1)* | Rectification report forms and timelines per State (beyond Maharashtra and MSCS) | Not researched | Co-op law analyst | Generic format | P16 |
| OI-P16-13 *(v1.1)* | States accepting English-language filings | Varies | Co-op law analyst | Bilingual output | P16 |

---

## 15. Sources (accessed 25 October 2026 unless stated)
1. Multi-State Co-operative Societies Act, 2002 as amended by the MSCS (Amendment) Act, 2023; MSCS Rules, 2023 (Ministry of Cooperation; CRCS). https://crcs.gov.in ; https://egazette.gov.in/WriteReadData/2023/247816.pdf
2. CRCS order L-11012/01/2023-Reg (22 Jan 2024) on prudential norms for credit MSCS; CRCS branch-expansion order (July 2025) — as summarised in Finbyx v1.5 IP2.7 [VERIFY].
3. PIB, Ministry of Cooperation document (Feb 2026): National Cooperation Policy 2025 (24 Jul 2025), National Cooperative Database (~8.4 lakh co-operatives, ~32 crore members), PACS computerisation, Co-operative Ombudsman notified 5 Mar 2024 (s.85A), CEA elections in > 222 MSCS. https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc202624779801.pdf
4. Indian Cooperative: post-2023 amendment statistics (elections, Ombudsman orders, 113 MSCS in liquidation). https://www.indiancooperative.com/from-states/post-mscs-amend-act-2023-197-elections-held-113-co-ops-liquidated/amp
5. Maharashtra Co-operative Societies Act, 1960 and Rules, 1961. https://www.indiacode.nic.in/bitstream/123456789/15836/3/maharashtra.pdf
6. Banking Regulation Act, 1949 s.7 and s.56 (as amended 2020).
7. Constitution of India Part IXB (97th Amendment, 2011); *Union of India v. Rajendra N. Shah*, Supreme Court, 20 Jul 2021 [VERIFY citation].
8. Banning of Unregulated Deposit Schemes Act, 2019, First Schedule.
9. Infrabyx Ecosystem Integration Specification v1.1 §6.24 (members and group lending) — owner's corpus.
10. Finbyx Master Prompt v1.5 Part 7G IP1–IP2 (institution profiles, credit co-operative societies) — owner's corpus.
11. Adarsh Credit Co-operative Society: Central Registrar notices — https://www.indiancooperative.com/featured/massive-fraud-central-registrar-serves-notice-on-adarsh-credit-co-op/amp

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-38; X-16 (`coop.sor.members`, D-23), X-34 (elections conducted by the authority).

**Added in v1.1:** NN-48.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
