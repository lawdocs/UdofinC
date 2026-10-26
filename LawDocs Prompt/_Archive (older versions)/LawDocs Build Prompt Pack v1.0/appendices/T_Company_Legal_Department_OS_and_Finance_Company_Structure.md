# Appendix T — Company Legal Department OS and Finance Company Structure

> **Status:** Binding for the operating model, RACI, intake categories, SLA and DoA defaults and the structure templates (they ship as seed data in `lgo` and the governance/HRMS kernel mounts and are tenant-editable). Legal citations are **Reference**: rows marked V-REG are carried from the LawDocsComply v1.2 rules register; rows marked [VERIFY] must be checked against the primary text before any rule that depends on them leaves advisory status (NN-38).
> **Used by:** P13 (owner), P11, P12, P07, P10, P16, P18, P09 (agents), P02 (departments, positions), P03 (rule packs and templates), Appendix D (roles), Appendix H (agents), Appendix R (settings), Appendix W (open items).
>
> **How to use.** §T.1–§T.5 define how a company runs its legal function on LawDocs: who does what, which requests come in, how fast they are handled, and who approves. §T.6 is the customisable departmental and governance structure for NBFCs and other finance companies, with the Companies Act 2013 and RBI anchors. §T.7 gives lighter templates for startups, private companies, public unlisted and listed companies, LLPs and Section 8 companies. §T.8 is the seed-data format. §T.9 lists what must be verified. The P13 setup wizard (FR-P13-02) loads one §T.6/§T.7 template plus §T.2–§T.5 defaults; every value is editable by the tenant without Super Admin (NN-29), except locked statutory items, which can be removed only with a recorded reason and a checker (FR-P13-47).

---

## T.1 Legal-department operating model

### T.1.1 Positioning and the reserved-services boundary

LawDocs is expressed as **legal operations + AI + on-demand professionals** (D-17), never as a replacement for advocates (CH-14). Only advocates practise law and appear in courts (Advocates Act 1961 ss.29, 33; *Bar Council of India v. A.K. Balaji* (SC 2018) on non-litigious practice [VERIFY citation]; R3 LG-110). LawDocs, the company, does not give legal advice or representation in its own name (NN-41).

| Actor | What it does on LawDocs | What it never does |
|---|---|---|
| **CLO / Head Legal** (`ORG_CLO`; in a small company the CS, CFO or a founder may hold this role) | Owns intake, priorities, DoA for legal actions, panel choice, risk reporting to the board; approves outgoing legal positions; supervises Vidhi agents | — |
| **Legal makers** (`ORG_LEGAL_MAKER`) | Draft, review, negotiate, track matters, run bundles, prepare filings and board items | Approve their own work (NN-18) |
| **Vidhi agents** (Appendix H; `AGT_*`) | Triage proposals, first drafts, digests, minutes drafts, reminders, data extraction | Approve, sign, file, send externally, vote, give advice to individuals without the review lane (NN-13, NN-14, NN-43) |
| **Panel counsel and marketplace advocates** (`ORG_EXT_COUNSEL`, `PRO_ADVOCATE`) | Opinions, court work, appearances, filing, strategy; engaged and paid in their own name | Pay LawDocs a commission, referral or success-linked fee (NN-21; CH-08) |
| **Company Secretary** (`ORG_KMP` CS) | Board and committee work, registers, filings, director declarations (s.205 functions) | — |
| **LawDocs RM / professional** (retainer; `ORG_DELEGATED_MAKER`) | Maker work inside the client tenant under a delivery grant (NN-17); non-reserved services | Act as checker, approver or signatory; give reserved legal services in LawDocs' name |
| **LawDocsComply** (if used) | System of record for compliance, governance and client HRMS (D-10) | — |

### T.1.2 Sizing models

| Model | Typical company | Legal roles | Vidhi agents (default L1) | Panel / marketplace | Approvals |
|---|---|---|---|---|---|
| **A — Founder + Vidhi** | Startup, < 20 staff | Founder or CS as `ORG_CLO`; no makers | `AGT_LEGAL_INTAKE_DESK`, `AGT_CONTRACT_DRAFTER`, `AGT_OBLIGATION_TRACKER`, `AGT_TM_WATCH`, `AGT_COMPLIANCE_CALENDAR` | Marketplace SKUs for opinions, filings, notices | Founder approves; second director for DoA band ≥ ₹10 lakh |
| **B — One CLO** | SME or mid-size, 20–500 staff | CLO; 0–1 maker; CS | Model A + `AGT_REDLINE_NEGOTIATOR`, `AGT_LITIGATION_CLERK`, `AGT_ORDER_DIGEST`, `AGT_BOARD_SECRETARY`, `AGT_MINUTES_DRAFTER`, `AGT_CLO_CHIEF_OF_STAFF` | Panel of 3–8 firms by area; marketplace for overflow | CLO up to band 2; CFO/MD above |
| **C — Legal team** | Mid-size to large | CLO; 2–10 makers by practice (contracts, disputes, corporate, employment, IP, regulatory); CS team | Model B + `AGT_HEARING_PREP`, `AGT_NOTICE_RESPONDER`, `AGT_KMP_BRIEFER`, `AGT_ACTION_ITEM_TRACKER` | Formal panel with annual review and rate cards | Full DoA (§T.5) |
| **D — Group legal** | Group with several entities | Group CLO; entity legal leads; shared services | As C, entity-scoped | Group panel; entity budgets | DoA per entity; group CLO for cross-entity matters |
| **E — Managed retainer** | Company without in-house legal | Client checker (`ORG_CHECKER`/`ORG_APPROVER`); LawDocs RM as delegated maker | As B | Advocates' firm engaged directly by the client for advice (RS-LD-21 OFF until structure memo — [COUNSEL]) | Client approves everything external |

### T.1.3 Legal Department Charter (generated by P13 FR-P13-03)

Sections: 1 Purpose and scope (legal work handled; work referred to advocates); 2 Roles and authority (§T.1.1 table as adopted); 3 Intake rules (channels, categories §T.3, what must come to Legal — e.g., any contract above ₹ X, any notice, any regulator contact, any dispute threat); 4 Service levels (§T.3, §T.4); 5 Delegation of authority (§T.5, with the board resolution reference for board-delegated powers); 6 Panel policy (selection, conflicts, fees — no contingency fees for advocates, rate cards, review); 7 AI use (agents, autonomy ceilings, review lanes, disclosure — NN-14); 8 Confidentiality, privilege and data protection (privileged classes, DPDP processor terms with counsel); 9 Records (LawDocs folders, retention, legal hold); 10 Reporting (weekly CLO brief, quarterly legal risk report to the board/Audit Committee, annual review of the charter).

### T.1.4 Legal-function KPIs (CLO dashboard defaults)

Every KPI shows its formula and source (P13 FR-P13-17). Outcome measures only; no time-on-screen or activity surveillance (NN-33).

| KPI | Formula | Source | Default target [REC] |
|---|---|---|---|
| First-response SLA | Requests with first response ≤ target ÷ requests due in period | `lgo` | ≥ 95% |
| Resolution SLA | Requests resolved or converted ≤ target ÷ requests due | `lgo` | ≥ 90% |
| Self-service rate | SELF_SERVED ÷ all requests in self-service-eligible categories | `lgo` | ≥ 30% |
| Contract cycle time | Median days intake → executed, by category | P07 | Template contracts ≤ 2 days; third-party ≤ 10 days |
| Missed statutory/court dates | Count of MISSED clocks (P11/P12/P13) | `lit`, `ipm`, `gov` | 0 |
| Hearing outcome capture | Outcomes recorded ≤ 24 h ÷ hearings held | P11 | ≥ 98% |
| Order-direction compliance | Directions closed on time ÷ directions due | P11 | 100% |
| Exposure schedule timeliness | Schedule frozen ≤ quarter-end + 10 days | P11 | Every quarter |
| Spend vs budget | Actual ÷ budget by department and matter | P11, P13 | ≤ 100% |
| Panel responsiveness | Counsel updates within 24 h ÷ hearings (internal only) | P11 | ≥ 95% |
| Minutes timeliness | Minutes sealed ≤ 30 days ÷ meetings | `gov` | 100% |
| Requester satisfaction | Mean rating of rated requests | `lgo` | ≥ 4.2 / 5 |

---

## T.2 RACI for legal activities

Legend: **R** responsible (does the work) · **A** accountable (approves, one per row) · **C** consulted · **I** informed · **D** draft only (agent or delegated maker produces a proposal for R). "DoA" = the approver designated by §T.5 for the value band.

| # | Activity | Business requester | Dept head | Legal maker | CLO | CS | CFO | MD/CEO | Board / committee | Counsel / advocate | Vidhi agent | LawDocs RM (retainer) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Raise legal request | R | I | I | I | — | — | — | — | — | D (triage) | — |
| 2 | Triage and assignment | I | I | R | A | — | — | — | — | — | D | D |
| 3 | Standard contract on company template (self-service) | R | A (business) | I | I (audit) | — | — | — | — | — | D | — |
| 4 | Third-party contract review and negotiation | C | C | R | A (within band) | — | C (financial terms) | — | — | C (complex) | D (redlines) | D |
| 5 | Contract signature and stamping | C | I | R (formalities) | C | C (authority) | — | A (authorised signatory per board resolution) | — | — | D (checklist) | D |
| 6 | Obligation tracking after signing | R (performance) | A | C | I | — | I | — | — | — | D (extraction) | D |
| 7 | Notice received — triage and response | I | C | R | A | I | I (if money) | I (if critical) | — | C/R (reply signature) | D (classification) | D |
| 8 | Outgoing legal notice | C | C | R | A | — | — | — | — | R (signs if advocate's notice) | D (draft) | D |
| 9 | New litigation (filing or defence) | C | C | R (management) | A (within DoA) | I | C (budget) | C/A (above band) | I (material) | R (pleadings, appearance) | D (bundles, briefs) | D |
| 10 | Hearings and order compliance | C (directions) | R (directions) | R | A | — | — | — | — | R (appearance) | D (digest, reminders) | D |
| 11 | Settlement or waiver | C | C | R | C | — | C | A (above band) | A (above band per DoA) | C | — | — |
| 12 | Exposure assessment and contingent liabilities | — | C | R | R (assessor) | — | A (reviewer) | I | I (Audit Committee) | C | D (rationale draft only) | — |
| 13 | Counsel engagement and fees | — | — | R | A (within band) | — | C/A (rate cards, above band) | — | — | C | — | D |
| 14 | Legal spend approval | — | C (department budget) | R | A (within band) | — | A (above band) | — | — | — | — | — |
| 15 | Trademark clearance and filing | R (brand brief) | C | R | A | — | — | — | — | R (agent/advocate files) | D (class finder, screen) | D |
| 16 | Journal watch and oppositions | I | C | R | A | — | — | — | — | C/R | D (hits) | D |
| 17 | Board/committee meeting (notice, papers, minutes) | C (papers) | C (papers) | C | C | R/A (process) | C | C | A (decisions) | — | D (agenda, minutes) | D |
| 18 | Resolution follow-on filings (MGT-14, DIR-12, MR-1) | — | — | C | I | R/A | — | I | — | — | D (task) | D |
| 19 | Director/KMP declarations (MBP-1, DIR-8, fit and proper) | — | — | — | I | R | — | I | A (noting) | — | D (campaign) | D |
| 20 | Policy drafting (legal policies) | C | C | R | A | C | — | C | A (board-approved policies) | C | D | D |
| 21 | Employment legal (appointment letters, disciplinary, separation) | C (manager) | R | C | C (contentious) | — | — | A (senior roles) | — | C | D (letters) | — |
| 22 | POSH complaints | — | — | — | — | — | — | I (counts only) | I (annual report counts) | C (if engaged by IC) | — (sealed, unless IC enables L0/L1 drafting) | — |
| 23 | Regulatory proceeding (show-cause, adjudication) | I | C | R | A | C | C | A (material) | I | R (reply/appearance) | D | D |
| 24 | Legal risk report to board | — | I | R | A | C | C | C | I | — | D (`AGT_CLO_CHIEF_OF_STAFF`) | — |

POSH Internal Committee functions are statutory and independent (POSH Act 2013 s.4, s.11); the legal department supports only on request. For NBFCs, compliance obligations themselves sit with the CCO in LawDocsComply; Legal is consulted.

---

## T.3 Intake categories and SLA defaults

Defaults are [REC] seeds for `lgo.intake.request_types` and `lgo.sla.policies`; business hours per the entity calendar. "First response" = an assignee acknowledges with next step; "Target" = resolution or conversion to a longer-running record (whose own clocks then govern). Statutory or court deadlines linked to a request always prevail and never pause (P13 FR-P13-08).

| Code | Category | Examples | Default priority | First response | Target | Default route | Self-service | Converts to | Approval |
|---|---|---|---|---|---|---|---|---|---|
| CNT-STD | New contract — company template | NDA, standard vendor, standard customer, offer letter (HR) | P4 | 4 h | 1 business day | Self-service, then legal maker if outside guardrails | Yes (within `lgo.selfservice.limits`) | P07 agreement | Dept head (business); DoA if above limit |
| CNT-3P | Contract review — third-party paper | Customer MSA, vendor terms, lease | P3 | 1 business day | 5 business days (≤ 30 pages); 10 (> 30) | Contracts maker | No | P07 negotiation | DoA by value and risk tier |
| CNT-AMD | Amendment, renewal or termination | Extension, termination notice, novation | P3 | 1 business day | 5 business days; earlier if notice deadline | Contracts maker | Partial (renewal on same terms) | P07 | DoA |
| NDA-IN | Counterparty NDA | NDA on counterparty paper | P4 | 4 h | 2 business days | Contracts maker | Playbook check by `AGT_REDLINE_NEGOTIATOR` (draft) | P07 | CLO delegate |
| VND-ONB | Vendor onboarding legal check | Outsourcing, data processing, IT vendor | P3 | 1 business day | 5 business days | Contracts maker; LDC for RE outsourcing checklists | Checklist | P07 + LDC (RE) | DoA; CRO/CCO for RE material outsourcing [INTERP] |
| NTC-IN | Notice received | Legal notice, tax notice, regulator letter, consumer notice | P1/P2 by type | 2 h (P1) / 4 h (P2) | Per statutory window (P10/P11 clock) | Disputes maker; tax notices to tax lead (P14) | No | P11 matter / P10 reply | CLO; above band MD |
| NTC-OUT | Send a legal notice | Recovery of dues (non-RE), breach notice, cease and desist | P3 | 1 business day | 3 business days | Disputes maker; advocate signs where it is an advocate's notice | No | P10 notice | CLO |
| DSP | Dispute or threatened claim | Customer threat, vendor claim, employee claim | P2 | 4 h | Triage plan in 2 business days | Disputes maker | No | P11 matter | CLO |
| LIT-UPD | Litigation status request | "What is the status of our case?" | P4 | 4 h | 1 business day | Self-service status page (P11) | Yes | — | — |
| EMP | Employment and HR legal | Disciplinary, termination, contract change, policy query | P3 | 1 business day | 5 business days | Employment maker | Policy answers by `AGT_LEGAL_INTAKE_DESK` with citations | HR document (P13) / P11 | CLO for contentious |
| POL | Policy drafting or review | Privacy policy, anti-bribery, website terms | P3 | 2 business days | 15 business days | Corporate maker | Templates (P06) | P06/P04 policy | Board/committee where required |
| BRD | Board or shareholder matter | Resolution, approval, meeting item | P3 | 1 business day | Before meeting cut-off | CS | Resolution library | Agenda item / resolution | CS; board |
| REG | Regulatory query | Interpretation of a regulation, licence condition | P2 | 4 h | 5 business days | Regulatory maker; LDC for REs | Knowledge answers (non-advice, cited) | LDC compliance query (RE) | CLO/CCO |
| IP | Brand, trademark, IP | Clearance, filing, infringement, licensing | P3 | 1 business day | 5 business days (clearance) | IP maker; marketplace agent | Class finder and screen (P12) | P12 asset / P11 matter | CLO |
| DPR | Data protection | Data breach, rights request, processor terms | P1 (breach) / P3 | 1 h (breach) / 1 business day | Breach per incident runbook (CERT-In 6 h; NN-27); rights requests per DPDP timelines [VERIFY] | DPO / privacy lead | No | Incident (P23) / DPDP request | DPO; CLO |
| LIC | Licence or registration | New licence, renewal, condition breach | P3 | 1 business day | Before lead date | Corporate maker; LDC (RE) | Register update | Licence register (P13/LDC) | CLO |
| CORP | Corporate transaction | Share issue, investment, M&A, funding round | P2 | 4 h | Project plan in 3 business days | Corporate maker + panel | Data room (P07) | Project matter | MD; board |
| ADV | General legal question | "Can we…?" | P4 | 1 business day | 3 business days | Any maker; marketplace consult for specialist areas | Knowledge answers with citations; escalation always available | Marketplace order (P16) | — |
| POA | Authority and signatory | POA, authorised signatory letter, board authority | P3 | 1 business day | 3 business days | CS | Templates (eligibility gate — POAs are not eSign-eligible; NN-07) | P08 wet-ink pack | CS; board resolution |
| EVT | Urgent legal event | Police visit, raid, court summons, injunction served, media crisis | P1 | 30 min | Immediate plan | CLO directly | No | P11 matter | CLO; MD |

Sensitive triggers (always routed to a human; no auto-closure; `AGT_LEGAL_INTAKE_DESK` may only flag): police, FIR, arrest, raid, search, summons, injunction, court, tribunal, regulator, RBI, SEBI, show-cause, data breach, cyber incident, harassment, POSH, whistle-blower, bribery, fraud, death, injury, minors, media.

---

## T.4 Priority matrix

| Priority | Criteria (any one) | First response | Escalation |
|---|---|---|---|
| **P1 — Critical** | Liberty, safety or urgent court/regulator action; statutory deadline ≤ 3 days; data breach; injunction or attachment; exposure ≥ band 4 (§T.5); media or reputational crisis | 30 min (business hours), 2 h (outside) | CLO immediately; MD/CEO if exposure ≥ band 3 |
| **P2 — High** | Statutory or contractual deadline ≤ 10 days; exposure band 3; regulator involvement; new dispute | 4 business hours | CLO at 75% of target |
| **P3 — Normal** | Ordinary contracts, policies, advice with a business date | 1 business day | Team lead at 75%; CLO on breach |
| **P4 — Low** | Templates, status requests, general questions | 1 business day (4 h for self-service follow-ups) | Team lead on breach |

The rules engine computes priority from the request form (value band, deadline, keywords, counterparty type, category default); the triager can raise but not lower a priority set by a sensitive trigger.

---

## T.5 Delegation-of-authority defaults for legal actions

Value bands (₹, per transaction or per matter exposure): band 1 ≤ 10 lakh; band 2 > 10 lakh ≤ 1 crore; band 3 > 1 crore ≤ 10 crore; band 4 > 10 crore. Defaults are [REC] seeds for `lgo.doa.matrix`; board-delegated powers must reference the board resolution (Companies Act s.179(3) matters stay with the board; borrowing, investment and loan limits under s.180 and s.186 follow shareholder/board approvals) [VERIFY band mapping to the tenant's board resolution].

| Action | Band 1 | Band 2 | Band 3 | Band 4 |
|---|---|---|---|---|
| Approve contract (standard risk) | Dept head + legal maker review | CLO | CLO + CFO | MD/CEO (board if s.179/s.180/s.186/s.188 applies) |
| Approve contract (high risk: unlimited liability, exclusivity, IP transfer, data export, RPT) | CLO | CLO + CFO | MD/CEO | Board / committee |
| Approve outgoing notice or reply | Legal maker + CLO | CLO | CLO + MD/CEO | CLO + MD/CEO (board informed) |
| Engage counsel / approve fee estimate | CLO | CLO | CLO + CFO | MD/CEO |
| Approve legal spend invoice | CLO | CLO | CFO | CFO + MD/CEO |
| Settlement or waiver | CLO | CLO + CFO | MD/CEO | Board / committee |
| Commence litigation or arbitration | CLO | CLO | MD/CEO | MD/CEO + board informed |
| Sign on behalf of the company | Authorised signatory per board resolution (all bands) | | | |
| Exposure class and amount (Ind AS 37) | Assessor: CLO; reviewer: CFO (all bands); Audit Committee informed quarterly | | | |

`lgo.spend.approval_threshold_inr` (Appendix R; default ₹50,000) sets the floor below which spend approvals auto-route to the CLO alone.

## T.5A Legal-calendar seed catalogue

Seeds for the P13 legal calendar (FR-P13-13). Each item is generated by its owning module's rules; all periods are rule-pack data with verification status (NN-38). Items marked LDC are shown from LawDocsComply when linked and are not generated by LawDocs.

| Source | Item | Rule (seed) | Owner (default) |
|---|---|---|---|
| P07 | Contract renewal and notice deadline | Expiry − notice period; alerts 90/60/30 days before the notice deadline | Business owner; Legal informed |
| P07 | Contractual obligations (payments, reports, audits, insurance) | As extracted and confirmed | Obligation owner |
| P11 | Hearings; cause-list matches | Licensed source or user/counsel entry | Matter owner |
| P11 | Limitation, appeal, pleading and order-compliance clocks | `rulepack.IN.lit.limitation` | Matter owner |
| P11 | Quarterly exposure schedule | Quarter-end − 10 days (open); quarter-end + 10 days (freeze) | CLO; CFO |
| P12 | Examination reply, hearing, opposition, counter-statement, renewal, restoration | `rulepack.IN.ipm.tm_timelines` | IP owner |
| P10 | Notice reply windows (received notices) | Notice master | Notice owner |
| gov | Board meetings (cadence), notices (7 days), minutes (15/7/30 days), circular resolutions | CA13 s.173, s.118, s.175; SS-1 [VERIFY paras] | CS |
| gov | AGM window; annual filings (AOC-4, MGT-7/7A) | s.96; s.137; s.92 [VERIFY due-date rules] | CS |
| gov | Event filings (MGT-14, DIR-12, MR-1, CHG-1) | s.117; s.170; s.196; s.77 [VERIFY timelines] | CS |
| gov | Director declarations (MBP-1, DIR-8), director KYC | s.184(1), s.164(2); Appointment and Qualification Rules as amended 2025 [VERIFY] | CS |
| gov | KMP vacancy | s.203(4): 6 months | CS; NRC |
| hr | Appointment letters for joiners; wage payment date; full and final | OSH Code s.6(1)(f); Code on Wages s.17 (by the 7th; 2 working days) | HR |
| hr | POSH IC annual report; IC member term expiry | POSH Act s.21; IC constitution | `ORG_POSH_IC_PRESIDING` |
| lgo | Licences and registrations renewal | Expiry − lead days (default 60) | Licence owner; LDC when linked |
| LDC | Regulatory returns, compliance certificates, inspections | LDC rule packs | CCO (in LDC) |

---

## T.6 Finance-company (NBFC) structure template

### T.6.1 Applicability and configuration

The template applies to NBFCs registered with the RBI and, with variants (§T.6.8), to HFCs and other finance companies. Configuration inputs from the setup wizard: layer under the Scale Based Regulation framework (Base, Middle, Upper; Top is empty unless notified) [V-REG], category (e.g., NBFC-ICC, HFC, NBFC-MFI, CIC, NBFC-Factor, IFC, IDF, P2P, AA), deposit-taking or not, customer interface or not, asset size band, listed status (equity/debt), number of branches/outlets. The governance overlay rule pack `gov.rbi_nbfc_2025` (shared kernel content with LDC — NN-47) adds or tightens requirements; it is ADVISORY until verified (P13 FR-P13-48).

Primary anchors (titles as carried in LDC v1.2 Appendix G; [VERIFY exact titles and paragraph numbers against the RBI texts]):

| Ref | Instrument | Used for |
|---|---|---|
| RBI-GOV | Reserve Bank of India (Non-Banking Financial Companies – Governance) Directions, 2025, RBI/DOR/2025-26/344, 28 Nov 2025 — applicability BL Ch III; ML Ch II–IV; UL Ch II–V (V-REG, LDC LR-RBI-027) | Board, committees, CRO, CCO, KMP, fit and proper, compensation, whistle-blower |
| RBI-KYC | NBFC – KYC Directions 2025, RBI/DOR/2025-26/361 (V-REG) | Principal Officer, Designated Director, KYC functions |
| RBI-RBC | NBFC – Responsible Business Conduct Directions 2025, RBI/DOR/2025-26/362 (V-REG) | Grievance Redressal Officer and grievance mechanism |
| RBI-OUT | NBFC – Outsourcing Directions 2025, RBI/DOR/2025-26/363 (V-REG) | Outsourcing oversight duties (vendor legal checks) |
| RBI-WD | NBFC – Wilful Defaulters Directions 2025, RBI/DOR/2025-26/358 (V-REG) | Identification and Review Committees (ML and above) |
| RBI-COMP | RBI directions on the compliance function for NBFCs (LDC records 31 Jul 2026) [VERIFY title and reference] | CCO role, independence, reporting |
| RBI-IT | RBI Master Direction on Information Technology Governance, Risk, Controls and Assurance Practices, 7 Nov 2023 (V-REG) [VERIFY status after the 2025 consolidation and applicability by layer] | IT Strategy Committee, IT Steering Committee, Head of IT, CISO |
| RBI-FRM | RBI directions on fraud risk management for NBFCs (2024; LDC notes a 2025 consolidated reference) [VERIFY] | Board-level fraud monitoring committee, fraud risk function |
| RBI-ALM | RBI liquidity and ALM requirements for NBFCs in the 2025 consolidated set [VERIFY reference] | ALCO |
| RBI-IO | RBI directions on the Internal Ombudsman for NBFCs (LDC records a 2026 instrument) [VERIFY applicability thresholds] | Internal Ombudsman |
| RBI-RBIA | RBI requirements on risk-based internal audit for NBFCs [VERIFY reference and layer applicability] | Head of Internal Audit, RBIA |
| CA13 | Companies Act 2013 and Rules (ss.149, 152, 165, 173–179, 184, 203, 205; Rules cited in §T.6.2) | Company-law baseline |

### T.6.2 Board composition requirements

| Requirement | Source | Applies to | Template default |
|---|---|---|---|
| Minimum directors: 3 (public) / 2 (private); maximum 15 unless special resolution | CA13 s.149(1) | All | Board of 5–7 for ML; 3 for small BL |
| At least one resident director (≥ 182 days in India in the FY) | CA13 s.149(3) | All | Flag on director record |
| Independent directors: one-third for listed public companies; at least two for specified public companies | CA13 s.149(4); Companies (Appointment and Qualification of Directors) Rules 2014 r.4 [VERIFY thresholds] | Listed; specified public | Two IDs for ML and above [REC] |
| Woman director | CA13 s.149(1) second proviso; r.3 [VERIFY thresholds] | Listed; specified public | One |
| At least one director with banking/NBFC experience | RBI-GOV para 8 (V-REG) | As per applicability | Required for ML and above |
| Prior RBI approval for change of more than 30% of directors (excluding IDs) | RBI-GOV paras 10–11 (V-REG) | As per applicability | Blueprint warning on planned appointments |
| Fit-and-proper policy; declarations and Deed of Covenant from directors; quarterly statement on directors to the RBI Regional Office | RBI-GOV paras 12–14 (V-REG) | As per applicability | Declaration campaigns (P13 FR-P13-43) |
| Cap on independent directorships across ML/UL NBFCs | RBI-GOV para 27 (V-REG) | ML/UL | Limit engine warning |
| Directorship limits (20 companies, 10 public) | CA13 s.165 | All | Limit engine |
| Board meetings: ≥ 4 a year, ≤ 120-day gap; 7 days' notice | CA13 s.173(1), (3) | All | Planner |

### T.6.3 Committees

Composition, quorum and cadence rules are kernel rule data; the table shows the template default and the legal basis.

| Committee | Legal basis | Applicability (template) | Composition (template default) | Cadence | Key mandate | LawDocs/LDC hooks |
|---|---|---|---|---|---|---|
| Audit Committee | CA13 s.177; Meetings of Board Rules r.6 [VERIFY]; RBI-GOV para 17 — at least three members, oversight of IS audit (V-REG); LODR Reg 18 if listed | All NBFCs per RBI-GOV; companies per r.6 | ≥ 3 non-executive directors, majority independent, chair independent [REC where law is silent] | ≥ 4 a year (≤ 120-day gap if listed) | Financial reporting, internal audit, IS audit, related-party transactions, vigil mechanism (s.177(9)–(10)) | P11 exposure schedule; P13 legal risk dashboard; LDC audit trackers |
| Nomination and Remuneration Committee | CA13 s.178(1); RBI-GOV para 18 (V-REG); LODR Reg 19 | All NBFCs per RBI-GOV | ≥ 3 non-executive, at least half independent | ≥ 1 a year | Fit and proper, appointments, remuneration, board evaluation | Declarations, KMP records |
| Risk Management Committee | RBI-GOV para 9 (V-REG); LODR Reg 21 (top listed) | ML and above (template); BL optional | Directors + CRO; chair a director | ≥ 2 a year [VERIFY] | Integrated risk, risk appetite | LDC risk modules |
| IT Strategy Committee | RBI-IT [VERIFY applicability] | Per RBI-IT | Chair an independent director with IT expertise [VERIFY]; CIO, CISO, CTO invitees | ≥ quarterly [VERIFY] | IT strategy, IT risk, cyber | LDC IT governance |
| IT Steering Committee (management) | RBI-IT [VERIFY] | Per RBI-IT | Senior management, heads of IT, business, risk | As per policy | Implementation of IT strategy | — |
| Asset-Liability Management Committee (ALCO, management) | RBI-ALM [VERIFY] | All NBFCs above a size threshold [VERIFY] | MD/CEO (chair), CFO, Treasury head, CRO | Monthly [REC] | Liquidity, interest-rate risk, ALM | Finbyx ALM data (if used) |
| CSR Committee | CA13 s.135(1); not required where CSR obligation ≤ ₹50 lakh (s.135(9)) [VERIFY] | When s.135(1) thresholds met | ≥ 3 directors including one ID (where required) | ≥ 2 a year [REC] | CSR policy, spend | Board's report annexure |
| Stakeholders Relationship Committee | CA13 s.178(5) (more than 1,000 security holders); LODR Reg 20 | When thresholds met; listed | Chair non-executive | ≥ 1 a year | Security-holder grievances | Shareholder services |
| Review Committee (wilful defaulters) | RBI-WD (V-REG) | ML and above | MD/CEO + 2 independent/non-executive directors [VERIFY] | As cases arise | Review of wilful-defaulter identification | Finbyx RS (recovery) |
| Fraud monitoring committee | RBI-FRM [VERIFY] | Per RBI-FRM | Board-level, with ID and MD/CEO | As per directions | Fraud oversight | LDC fraud registers |
| Customer service / grievance committee | RBI-RBC [VERIFY whether a committee is mandated] | Customer-facing NBFCs (template optional) | Senior management + GRO | Quarterly [REC] | Grievance trends, conduct | LDC grievance; P15 never used for RE grievances |
| Credit Committee (management) | Board-approved credit policy [REC] | Lending NBFCs | MD/CEO, Credit head, CRO (observer), Business head | As per policy | Sanctions within delegated limits | Finbyx LOS |
| Independent Directors' meeting | CA13 Schedule IV para VII; LODR Reg 25(3) | Where IDs exist | IDs only | ≥ 1 a year | Board evaluation | P13 meeting engine |
| Executive / Borrowing committee | CA13 s.179(3) proviso (delegation) | Optional | Directors as delegated | As needed | Delegated borrowing/investment within limits | DoA references |

### T.6.4 KMP and regulated functionaries

| Role | Basis | Applicability | Reporting line (template) | Key duties seeded (P13 FR-P13-44) | Vacancy / approval |
|---|---|---|---|---|---|
| MD/CEO or Manager; WTD | CA13 s.2(51), s.196, s.203 | Whole-time KMP for listed and specified public companies (Managerial Personnel Rules r.8 [VERIFY]) | Board | Overall management; certifications to RBI/board as required | Fill within 6 months (s.203(4)); MR-1 [VERIFY timeline] |
| Chief Financial Officer | CA13 s.2(51), s.203 | As above | MD/CEO; Audit Committee access | Financial statements authentication (s.134(1)); provisions and contingent liabilities review (P11) | 6 months |
| Company Secretary | CA13 s.2(24), s.203, s.205; r.8A for other companies with paid-up capital ≥ ₹10 crore [VERIFY] | As above | MD/CEO; board | s.205 functions; SS-1/SS-2 compliance; registers; filings | 6 months |
| Chief Risk Officer | RBI-GOV paras 19–24 (V-REG; LDC: required above ₹5,000 crore asset size [VERIFY]) | Per RBI-GOV | MD/CEO and RMC; no business targets | Risk identification, measurement, reporting to RMC | Fixed tenure and board approval for removal per RBI-GOV [VERIFY] |
| Chief Compliance Officer | RBI-GOV para 25 (V-REG); RBI-COMP [VERIFY] | Per RBI-COMP (ML and above in template) | MD/CEO; Audit Committee/board access; no business targets | Compliance function — in LawDocsComply | Per RBI-COMP |
| Head of Internal Audit | RBI-RBIA [VERIFY]; CA13 s.138 (internal auditor) | ML and above (RBIA), others per s.138 | Functionally to Audit Committee; administratively to MD/CEO | RBIA plan, audit reports | Audit Committee approval |
| Chief Information Security Officer | RBI-IT [VERIFY] | Per RBI-IT | Not to the head of IT operations [VERIFY]; to CRO or MD/CEO | Information security, cyber incident response (CERT-In 6 h) | Board/ITSC |
| Head of IT / CIO | RBI-IT [VERIFY] | Per RBI-IT | MD/CEO | IT operations, change management | — |
| Grievance Redressal Officer | RBI-RBC (V-REG) | Customer-facing NBFCs | Senior management; independent of sales | Grievance mechanism, escalation | Display contact details per directions |
| Principal Officer; Designated Director | PML Rules; RBI-KYC (V-REG) [VERIFY rule references] | All NBFCs with customer interface | Principal Officer to senior management; Designated Director a board member or MD | FIU-IND reporting, KYC oversight | Intimation to FIU-IND [VERIFY] |
| Internal Ombudsman | RBI-IO [VERIFY applicability] | Per RBI-IO | Independent; reports to board-level committee [VERIFY] | Review of rejected complaints | Tenure rules per RBI-IO |
| Data Protection Officer / privacy lead | DPDP Act 2023 s.10 (only for a Significant Data Fiduciary) [VERIFY notification]; otherwise a designated privacy contact | SDF only (DPO); all (contact) | Board for DPO | DPDP compliance, rights requests | — |
| Head Legal / CLO | Company choice (no statutory mandate for NBFCs [INTERP]) | Template default for ML and above | MD/CEO; Audit Committee access for legal risk | Legal department OS (P13), litigation exposure (P11) | — |

KMP restrictions for NBFCs (e.g., limits on KMP holding office in other NBFCs) are carried from RBI-GOV para 26 (V-REG) as SoD warnings.

### T.6.5 Departments

| Department | Purpose | Head (position) | Reports to | Line of defence | Key duties (seeded) | Linked committee | Main LawDocs / ecosystem modules |
|---|---|---|---|---|---|---|---|
| Board & Secretarial | Board processes, registers, filings, investor relations (listed/debt-listed) | Company Secretary | MD/CEO; board | GOVERNANCE | Meetings, minutes, registers, MCA filings, declarations | All board committees | P13 `gov`; LDC (if SoR) |
| Executive Management | Strategy and management | MD/CEO | Board | GOVERNANCE | Business plan, delegations | Board | P13 dashboards |
| Business / Sales | Origination, branches, partnerships, co-lending, DSA/DMA and LSP management | Business Head | MD/CEO | FIRST | Sourcing within policy, partner contracts | Credit Committee | P07 (partner agreements); Finbyx/Udofin |
| Credit | Underwriting, credit policy, sanction, monitoring | Head of Credit | MD/CEO (credit risk reporting to CRO) | FIRST (underwriting) | Credit appraisal, sanction within DoA, post-sanction monitoring | Credit Committee; RMC | Finbyx LOS; P07 sanction documentation |
| Operations | Disbursement, servicing, documentation custody, customer service desk | Head of Operations | MD/CEO | FIRST | Documentation, stamping and execution, custody, disbursement checks | — | P08 (eSign/eStamp, evidence), P04 vault; Finbyx LMS |
| Collections & Recovery | Pre-delinquency, field collections, legal recovery (SARFAESI, s.138, arbitration, DRT) | Head of Collections | MD/CEO | FIRST | Fair-practice collections, recovery actions | Review Committee (WD); RMC | Finbyx Recovery Suite (SoR); P11 projections only |
| Treasury | Borrowings, liquidity, investments | Treasurer | CFO | FIRST (front office); back office in F&A | Funding, ALM inputs | ALCO | P07 (borrowing documents), P13 resolutions (s.179/s.180) |
| Finance & Accounts | Accounting, financial reporting, tax, regulatory returns preparation | CFO | MD/CEO; Audit Committee | FIRST (reporting); SUPPORT | Books, Ind AS reporting, provisions, contingent liabilities | Audit Committee | P11 exposure schedule; P14 tax; LDC returns |
| Risk Management | Enterprise, credit, market, liquidity, operational, model risk | CRO | MD/CEO; RMC | SECOND | Risk framework, appetite, monitoring | RMC; ALCO | LDC risk |
| Compliance | Regulatory compliance, KYC/AML oversight, regulatory reporting oversight | CCO | MD/CEO; board/Audit Committee | SECOND | Compliance programme, testing, regulator liaison | Audit Committee; board | LawDocsComply (SoR) |
| Legal | Contracts, disputes, notices, IP, corporate legal, legal opinions (via advocates) | Head Legal / CLO | MD/CEO | SECOND (advisory and legal risk) [INTERP] | Legal intake, contract approvals, litigation management, legal risk reporting | Audit Committee (legal risk) | P13 `lgo`, P07, P10, P11, P12 |
| Information Technology | IT operations, applications, data | Head of IT / CIO | MD/CEO | FIRST | IT service delivery, change management | IT Steering Committee | — |
| Information Security | Security governance, cyber incident response | CISO | CRO or MD/CEO (not IT head) [VERIFY] | SECOND | Security policy, monitoring, incident reporting | IT Strategy Committee | P23 controls (LawDocs' own); LDC |
| Fraud Risk Management | Fraud prevention, detection, reporting | Head of Fraud Risk (or within Risk) | CRO | SECOND | Fraud monitoring and reporting | Fraud monitoring committee | LDC |
| Customer Service & Grievance | Complaints, grievance redressal, Internal Ombudsman liaison | Grievance Redressal Officer | MD/CEO | FIRST (service) / SECOND (oversight by Compliance) | Complaint handling within timelines | Customer service committee (if any) | LDC grievance; Finbyx/Udofin channels |
| Human Resources & Administration | People, payroll, policies, POSH IC support, facilities | Head of HR | MD/CEO | SUPPORT | HR lifecycle, labour compliance, IC support (not membership by default) | NRC (inputs) | P13 `hr` (or LDC HRMS) |
| Internal Audit | Independent assurance, RBIA | Head of Internal Audit | Audit Committee (functional) | THIRD | Audit plan, reports, follow-up | Audit Committee | LDC audit |

Every department has duties attached to positions (P13 FR-P13-45), a department head position, optional sub-functions (renameable; statutory mapping by ID) and its own intake routing in `lgo.routing.table`.

### T.6.6 Three lines of defence and reporting lines

| Line | Departments (template) | Accountability | Independence safeguards (template rules) |
|---|---|---|---|
| Governance | Board, committees, Board & Secretarial, Executive Management | Sets strategy, risk appetite, policies, delegations | Committee composition rules (§T.6.3); independent directors |
| First line | Business/Sales, Credit (underwriting), Operations, Collections & Recovery, Treasury (front office), Finance & Accounts (reporting), IT, Customer Service | Owns and manages risk in daily operations; executes controls | Maker-checker in every critical process (NN-18 analogue in the client's own processes); DoA |
| Second line | Risk Management, Compliance, Legal (advisory and legal risk) [INTERP], Information Security, Fraud Risk | Sets frameworks, monitors and challenges the first line; reports to board committees | No business targets for CRO, CCO, CISO [VERIFY sources per role]; direct access to the Audit Committee/RMC/board; heads not reporting to a first-line head |
| Third line | Internal Audit | Independent assurance to the Audit Committee | Functional reporting to the Audit Committee; no operational responsibilities; access to all records |
| Support | HR & Administration | Enables the organisation | — |

Legal is placed in the second line for its oversight of legal risk and in a service role for first-line requests; tenants may re-classify it (some organisations treat Legal as a support function). The classification drives reports (legal risk dashboard sections) and SoD warnings, not access.

### T.6.7 Segregation-of-duties rules (seed; warnings by default)

| Code | Rule | Basis | Default |
|---|---|---|---|
| SOD-01 | The CRO does not head, or hold targets for, any business or credit-sanctioning department | RBI-GOV paras 19–24 (V-REG) [VERIFY wording] | Warning (AT_RISK) |
| SOD-02 | The CCO has no business targets and does not head a first-line department | RBI-GOV para 25; RBI-COMP [VERIFY] | Warning |
| SOD-03 | The Head of Internal Audit has no operational responsibility and reports functionally to the Audit Committee | RBI-RBIA [VERIFY]; CA13 s.177 | Warning |
| SOD-04 | The CISO does not report to the head of IT operations | RBI-IT [VERIFY] | Warning |
| SOD-05 | Treasury front-office dealing and back-office settlement are held by different persons | [REC] (market practice; ALM controls) | Warning |
| SOD-06 | The same person does not originate (sales), sanction (credit) and disburse (operations) the same loan | [REC]; Finbyx enforces in LOS | Warning |
| SOD-07 | The Grievance Redressal Officer is not a sales or collections head | RBI-RBC [VERIFY] | Warning |
| SOD-08 | Maker and checker differ for any LawDocs approval (contracts, payroll, DoA changes, exports) | NN-18 | Hard block (platform) |
| SOD-09 | POSH IC members do not include the respondent's line manager in a case; the IC Presiding Officer (`ORG_POSH_IC_PRESIDING`) is a senior woman employee | POSH Act 2013 s.4(2) [VERIFY]; [REC] | Hard block per case |
| SOD-10 | Designated Director (PML) is a director or MD; Principal Officer is at senior management level | PML Rules; RBI-KYC [VERIFY] | Warning |
| SOD-11 | An independent director is not KMP or a relative of a promoter/director | CA13 s.149(6) | Warning (blueprint GAP) |
| SOD-12 | The person approving a contract is not conflicted with the counterparty (declared interest or related party) | CA13 s.184, s.188; [REC] | Warning; approver removed from the chain |

Tenants may promote any warning to a hard block (`gov.sod.hard_block_rules`, maker-checker).

### T.6.8 Variants by layer and category

| Variant | Changes to the template |
|---|---|
| NBFC-BL (Base Layer) | Governance Directions Chapter III only (V-REG); Audit Committee and NRC per RBI-GOV applicability [VERIFY]; RMC, CCO, CRO and ITSC optional unless applicable; smaller department set (Risk and Compliance may be one department with SoD warnings explained) |
| NBFC-ML (Middle Layer) | Full template: RMC, NRC, Audit Committee, CCO, Head of Internal Audit (RBIA [VERIFY]), CISO, Review Committee (WD), ALCO; CRO when asset size threshold met (LDC: above ₹5,000 crore [VERIFY]); ID cap warnings (para 27) |
| NBFC-UL (Upper Layer) | ML plus: listing within three years of identification (RBI-GOV para 43, V-REG) — calendar item; enhanced board and committee cadence [VERIFY]; compensation rules (paras 29–37) for KMP and senior management |
| HFC | ML/UL template with housing-finance-specific credit and NHB-related reporting duties [VERIFY current HFC directions]; Governance Directions include HFCs per LR-RBI-027 (V-REG) |
| NBFC-MFI | Adds microfinance-specific duties: household-income assessment and repayment-obligation limits (MFI Directions RBI/DOR/2025-26/371, V-REG), field-staff conduct, grievance at branch level |
| CIC | Group Risk Management Committee and group-level oversight (CIC Directions RBI/DOR/2025-26/367, V-REG) [VERIFY committee names]; lighter customer-facing departments |
| NBFC-ICC (investment/credit) | Template per the business mix: Investments department replaces Credit where the company is mainly an investment company |
| NBFC-P2P / NBFC-AA | Platform-specific departments (platform operations, consent management for AA); partial applicability of governance paras (V-REG) [VERIFY] |
| Deposit-taking NBFC | Adds deposit operations duties and branch authorisation items (BR Directions RBI/DOR/2025-26/342, V-REG); stricter liquidity and grievance obligations [VERIFY] |
| Listed (equity or debt) | Adds LODR overlay (§T.7.4) and Stakeholders Relationship Committee; investor relations under Secretarial |
| Government-owned NBFC | Compensation paras 29–37 not applicable (V-REG) |

### T.6.9 Customisation rules

1. Every department, committee, position, duty and reporting line is editable; names are terminology (TENANT tier) mapped by ID, so renaming never breaks statutory mapping, exports or reports (NN-12).
2. Statutory items (marked LOCKED-STATUTORY in the seed) can be removed only by the CS (or `ORG_ADMIN` for departments) with a checker and a reason; removal creates a blueprint GAP line, not silent deletion.
3. Tenants can merge departments (e.g., Risk + Compliance in a BL NBFC); SoD rules then show warnings with explanations.
4. Tenants can add departments (e.g., Data & Analytics, Co-lending Desk, Digital Lending/LSP Oversight) and committees; custom committees can be mapped to statutory roles (P13 FR-P13-28).
5. Template upgrades (new rule-pack versions) are offered as a diff with accept/reject per line; tenant edits are never overwritten silently.
6. When LDC is SoR (`int.eco.ldc.sor_mode.governance` / `.hrms` = `LDC`; X-11), the template is applied in LDC; LawDocs shows the structure read-only.

---

## T.7 Templates for other company types

### T.7.1 Startup (DPIIT-recognised private company)

| Element | Template |
|---|---|
| Governing body | Board of 2–3 directors (CA13 s.149(1)); founders as directors; investor nominee directors after funding |
| Meetings | Startup private companies: at least one board meeting in each half of the calendar year with a gap of not less than 90 days (s.173(5) and MCA exemption notification for startups [VERIFY current scope]) |
| Committees | None mandatory below thresholds; optional Investment/ESOP committee |
| KMP / officers | Not mandatory below r.8/8A thresholds [VERIFY]; legal lead = founder or CS (part-time/engaged) |
| Departments | Founders' office; Product/Tech; Sales; Finance & Admin; People |
| Legal calendar seeds | First board meeting within 30 days of incorporation; auditor appointment; commencement-of-business declaration (INC-20A) [VERIFY applicability]; AGM; annual filings (AOC-4, MGT-7/7A); DIR-3 KYC per the 2025 amendment [VERIFY]; ESOP grants and vesting; DPIIT recognition validity and tax-exemption applications [VERIFY] |
| Intake emphasis | Founders' agreement, SHA/SSA, ESOP, NDAs, vendor/customer templates, trademark (P12 startup bundles), employment templates, privacy policy |
| Operating model | Model A (§T.1.2) |

### T.7.2 Private company (including small company and OPC)

| Element | Template |
|---|---|
| Governing body | Board ≥ 2 (OPC ≥ 1) (s.149(1)); resident director |
| Meetings | ≥ 4 a year with ≤ 120-day gap; small companies and OPCs one in each half-year with ≥ 90-day gap (s.173(5)); OPC with one director — resolutions entered in the minute book (s.122(4)) [VERIFY] |
| Committees | Audit Committee/NRC only if r.6 thresholds apply (generally not for private companies [VERIFY]); CSR Committee if s.135 thresholds met |
| KMP | Whole-time CS if paid-up capital ≥ ₹10 crore (r.8A) [VERIFY] |
| Departments | Management; Finance & Accounts; Sales/Operations; HR & Admin; Legal & Secretarial (combined) |
| Legal calendar seeds | AGM (s.96; OPC exempt from AGM — s.96(1) [VERIFY]); AOC-4, MGT-7/7A; MBP-1 at first meeting of the FY; DIR-8; DPT-3 [VERIFY applicability]; MSME-1 [VERIFY]; small-company status re-test annually against s.2(85) and the Specification of Definitions Details Rules as amended [VERIFY current thresholds] |
| Operating model | Model A or B |

### T.7.3 Public unlisted company

| Element | Template |
|---|---|
| Governing body | Board ≥ 3; two IDs and a woman director where r.4/r.3 thresholds apply [VERIFY] |
| Committees | Audit Committee and NRC where r.6 thresholds apply; SRC if > 1,000 security holders; CSR if s.135 applies; vigil mechanism where r.7 applies (s.177(9)) [VERIFY] |
| KMP | Whole-time KMP if paid-up capital ≥ ₹10 crore (r.8) [VERIFY] |
| Departments | As private company plus Internal Audit (s.138, r.13 thresholds [VERIFY]) and Secretarial |
| Legal calendar seeds | As private, plus secretarial audit (s.204, r.9 thresholds [VERIFY]), MGT-14 for board resolutions under s.117(3)(g) [VERIFY current scope], interested-director rules at meetings (s.184(2)) |
| Operating model | Model B or C |

### T.7.4 Listed company (equity)

| Element | Template |
|---|---|
| Governing body | LODR Reg 17: composition (at least half non-executive; independent directors one-third or half depending on the chair; woman director/woman ID for specified listed entities) [VERIFY current text] |
| Committees | Audit (Reg 18), NRC (Reg 19), SRC (Reg 20), RMC (Reg 21 for specified top listed entities), CSR (s.135), ID meeting (Reg 25(3)) |
| KMP / officers | MD/CEO, CFO, CS (also Compliance Officer under Reg 6), senior management (Reg 16(1)(d)) |
| Departments | As public company plus Investor Relations and Secretarial (listing compliance) |
| Legal calendar seeds | Reg 30 disclosures (material litigation flags from P11 FR-P11-48 — determination by the authorised KMP), Reg 33 results, Reg 24A secretarial audit, PIT trading window and designated persons, SAST disclosures — the full LODR engine runs in LawDocsComply [REC]; LawDocs-only listed companies get a basic disclosure case (OI-P13-10) |
| Operating model | Model C or D |

### T.7.5 LLP

| Element | Template |
|---|---|
| Governing body | Partners (≥ 2) and designated partners (≥ 2, at least one resident in India) (LLP Act 2008 ss.6–7) |
| Meetings | As per LLP agreement (no statutory board meetings); partners' meetings and resolutions recorded in the governance kernel's LLP mode |
| Registers | Partners and designated partners; contributions; LLP agreement versions |
| Officers | Designated partners (DPIN/DIN, KYC) |
| Departments | Partners' office; Practice/Business units; Finance; HR & Admin; Legal & Compliance |
| Legal calendar seeds | LLP agreement filing (Form 3) within 30 days of incorporation or change; partner changes (Form 4) within 30 days; Form 11 (annual return) within 60 days of FY end; Form 8 (statement of account and solvency) by 30 October; audit if turnover or contribution thresholds are crossed [VERIFY all timelines and thresholds under the LLP Rules 2009 as amended] |
| Operating model | Model A or B |

### T.7.6 Section 8 company

| Element | Template |
|---|---|
| Governing body | Board per s.149 with exemptions available to Section 8 companies under the MCA notification of 5 June 2015 [VERIFY current exemptions] |
| Meetings | Reduced board-meeting frequency where exemptions apply (at least one in each half-year) [VERIFY] |
| Committees | As public/private company thresholds, subject to exemptions; CSR not applicable to receipts as such [INTERP — verify] |
| Officers | Per thresholds; trustees/donor relations in Executive |
| Departments | Programmes; Fundraising & Donor Relations; Finance & Accounts (grant accounting); HR; Legal & Compliance |
| Legal calendar seeds | Licence conditions under s.8; CSR-1 registration for receiving CSR funds [VERIFY]; FCRA registration and returns where foreign contributions are received (Foreign Contribution (Regulation) Act 2010) [VERIFY]; 12A/80G registrations and renewals under the Income-tax Act 2025 [VERIFY new sections] |
| Operating model | Model A or B |

---

## T.8 Seed-data format

Templates ship as versioned YAML in `packages/config/templates/org-structures/` (content, NN-30: reviewer of record, effective date, citations) and are imported by the P13 setup wizard. Tenants can export their adopted structure as `LD-TPL-ORG-v1.0` (XLSX with sheets Departments, Positions, Committees, Members, Duties, DoA, IntakeCategories, SLA) and re-import it with preview, diff and maker-checker.

```yaml
template_id: TPL-ORG-NBFC-ML
version: 1.0.0
effective_from: 2026-11-01
reviewer_of_record: PLT_LEGAL_REVIEWER/<name>
applies_to: { constitution: [PUBLIC_UNLISTED, PRIVATE, LISTED], sector: NBFC, layer: [MIDDLE] }
overlays: [gov.companies_act, gov.rbi_nbfc_2025]          # ADVISORY until verified (NN-38)
departments:
  - code: CREDIT
    name: Credit
    line_of_defence: FIRST
    head_position: HEAD_CREDIT
    reports_to: MD_CEO
    statutory: false
    duties: [CREDIT_APPRAISAL, SANCTION_WITHIN_DOA, POST_SANCTION_MONITORING]
  - code: COMPLIANCE
    name: Compliance
    line_of_defence: SECOND
    head_position: CCO
    reports_to: MD_CEO
    dotted_to: [AUDIT_COMMITTEE]
    statutory: LOCKED-STATUTORY
    citations: [RBI-GOV-25, RBI-COMP]                     # [VERIFY]
committees:
  - code: RMC
    roles: [RISK_MANAGEMENT_COMMITTEE]
    composition_rule: CR-RBI-GOV-09                        # kernel rule id
    cadence_rule: CAD-RMC-2PA                              # [VERIFY]
    statutory: LOCKED-STATUTORY
positions:
  - code: CRO
    kmp: false
    regulated_role: CRO
    sod_rules: [SOD-01]
    vacancy_clock: RBI-GOV-CRO                             # [VERIFY]
intake_categories: TPL-LGO-INTAKE-STD-1.0                  # §T.3
doa: TPL-LGO-DOA-STD-1.0                                   # §T.5
```

Rules: codes are stable IDs; display names are terminology; citations reference rule-pack IDs, never free text; every LOCKED-STATUTORY item carries at least one citation; a template cannot be published while any citation is UNVERIFIED unless the overlay is marked ADVISORY.

---

## T.9 Verification list (Appendix W items)

| # | Item to verify | Where | Affects |
|---|---|---|---|
| T-V01 | Exact titles and paragraph numbers of the RBI NBFC Governance Directions 2025 (RBI/DOR/2025-26/344) items used in §T.6 | RBI website, Master Directions | §T.6.2–§T.6.4, SoD rules |
| T-V02 | Compliance-function, IT governance, ALM/liquidity, fraud-risk, RBIA and Internal Ombudsman instruments and their applicability after the 28 Nov 2025 consolidation | RBI website | §T.6.1 refs RBI-COMP, RBI-IT, RBI-ALM, RBI-FRM, RBI-RBIA, RBI-IO |
| T-V03 | CRO asset-size threshold and tenure/removal rules | RBI-GOV | §T.6.4, §T.6.8 |
| T-V04 | Companies Act rule thresholds: r.3, r.4 (Appointment and Qualification of Directors Rules), r.6 and r.7 (Meetings of Board Rules), r.8/8A (Managerial Personnel Rules), r.9 (secretarial audit), r.13 (internal audit), s.2(85) small-company limits, s.135 CSR thresholds and committee exemption | MCA / India Code | §T.6.2, §T.6.3, §T.7 |
| T-V05 | Startup, OPC, small and Section 8 exemptions from s.173 and other provisions (MCA notifications of 5 June 2015 and 13 June 2017 and later amendments) | MCA notifications | §T.7.1, §T.7.2, §T.7.6 |
| T-V06 | SS-1/SS-2 paragraph numbers for notice, minutes and circular-resolution timelines | ICSI Secretarial Standards (revised, effective 1 Apr 2024 — R3 LG-156) | P13 FR-P13-31, FR-P13-36, FR-P13-37 |
| T-V07 | LODR Reg 17–21, 24A, 25, 30 current text | SEBI | §T.7.4 |
| T-V08 | LLP Act and LLP Rules 2009 timelines and audit thresholds | MCA | §T.7.5 |
| T-V09 | POSH Act s.4(2) composition wording; employer action timeline under s.13 | India Code | SOD-09; P13 FR-P13-59 |
| T-V10 | DPDP Act s.10 DPO trigger (Significant Data Fiduciary notification) | MeitY | §T.6.4 |
| T-V11 | PML Rules references for Principal Officer and Designated Director | DoR / FIU-IND | §T.6.4, SOD-10 |
| T-V12 | Bar Council rules and *A.K. Balaji* citation used in the operating-model boundary | BCI; SCC | §T.1.1 |

Until each item is verified and logged in `docs/compliance/verification-log.md`, the dependent template lines are shipped with the ADVISORY badge and create tasks, not hard blocks (NN-38).
