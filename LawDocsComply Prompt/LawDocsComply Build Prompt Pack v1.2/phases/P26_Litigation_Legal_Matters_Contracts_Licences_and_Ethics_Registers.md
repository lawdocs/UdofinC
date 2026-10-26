# Phase P26 — Litigation, Legal Matters, Contracts, Licences and Ethics Registers *(v1.1)*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, hash-chained audit ledger, Correction Entries, Object Lock storage, outbox);
> - **P01** (identity, step-up MFA, roles; new restricted external role `ext_counsel`; KMP sub-type GC);
> - **P02** (settings registry, rule packs — notice master, limitation schedule, authority and delegation matrix, licence renewal rules);
> - **P04** (tasks, approvals, calendar, Work Inbox, compliance issues — orders with directions become tasks);
> - **P06** (Board/committee approvals, Reg 30 disclosure cases, penalties register, conflict recusal);
> - **P07** (DMS with privilege tags, redline engine, eSign/e-stamp checklists, OCR and translation);
> - **P12** (TPRM and outsourcing register — contracts link); **P13** (person master for declarants);
> - **P18** (email-in, counsel portal identity, Ecosystem events from the Finbyx Recovery Suite / Udolex).
>
> **Sequencing:** Wave 2. Starts after P07 sprint 3 (DMS privilege tags) and P04 interface freeze. The regulator-engagement register (§4F) is needed by P10 (FR-P10-74 reads it); build §4F in sprint 1–2 and freeze its API first (OP-8).
>
> **Binding appendices:** A (state machines — new §A machines `lit.notice`, `lit.matter`, `lit.reg_engagement`, `lit.contract`, `lit.licence`, `lit.ethics_declaration` added by the lead), B (data model, events, errors), C (screens), D (access matrix — `ext_counsel`, GC), G (legal rules — LR-* for limitation, Reg 30, Ind AS 37 handling), J (§J.16 legal-matter accounting), M (export folder for legal matters — new top-level folder to be assigned by the Appendix M owner), U (settings), AA/K (agents).
>
> **Requirements covered:** R-005 (company and regulated-entity compliance including litigation exposure), R-009 (internal governance — ethics registers), R-013, R-021, R-027 (reads letters, notices, e-mail), R-038 (DMS, type copies, translation), R-052/R-053 (ecosystem data), R-075, R-080 (grievance → litigation hand-off), R-098 (integrations), owner baseline Architecture Part 3 "Legal Notices and Litigation and Debt Recovery Module" and "Litigation & Legal Matter Management"; Appendix Z IMP-121, IMP-122; Appendix AC gaps (G5 §A); decision D-41.
>
> **Estimated effort:** 9 two-week sprints, squad of 8 (matters and notices 3, regulator engagements and licences 2, contracts 2, ethics and reporting 1), plus a legal domain analyst (advocate with corporate-litigation experience) and a CS for licences and ethics registers.
>
> **v1.1 changes (25 October 2026)** — new phase created from G5 gap A, G2 IMP-121/IMP-122 and the owner's baseline litigation module; decision D-41 (LDC owns legal matters, regulator engagements, contracts, licences and ethics registers; Finbyx Recovery Suite/Udolex owns lender debt recovery).

---

## 1. Objective and business outcome

Every regulated entity and company carries legal exposure that today lives in lawyers' e-mails and spreadsheets: notices received and sent, court and tribunal cases, regulator inspections and show-cause proceedings, contracts with renewal and notice traps, licences that silently expire, and conflicts of interest that boards are required to manage. This phase gives the General Counsel, the CS and the CCO one governed register for all of it, connected to the compliance calendar, the Board, the accounts and the evidence vault — so that no limitation date, hearing, reply window, renewal or regulator commitment is missed, and every provision and disclosure is traceable.

| Outcome | Exit-gate measure |
|---|---|
| No missed legal deadline | Every notice and matter has an owner and computed due dates (reply window, hearing, limitation, appeal); zero unowned clocks in the pilot; reminders at T-7/T-3/T-1 by default; missed-deadline incidents = 0 in UAT scenarios |
| Notices handled same day | Incoming notice → OCR → classification proposal → triage owner in ≤ 1 business day for 95% of notices in the pilot; reply-on-time ≥ 98% |
| Orders become actions | An order with directions creates P04 tasks with due dates in one confirmation step; compliance with directions is tracked to closure |
| Regulator engagements controlled | Inspection RFIs, observations and MAP/RMP items are tracked to closure with evidence and closure-verification tests (P10); regulator SCNs and adjudications are tracked with reply windows and appeal limitation |
| Financial reporting fed | Quarterly provision and contingent-liability schedule (Ind AS 37/AS 29, §J.16) produced from matter assessments; Reg 30 material-litigation cases opened for listed entities from qualifying matters |
| Contracts and licences under control | Contract repository with extracted obligations, renewal and notice-period alerts; licence register with renewal tasks generated ≥ lead time before expiry; zero expired licences in the pilot without an open renewal task |
| Ethics managed | Conflict-of-interest, gifts and hospitality, and related-party declarations collected by campaign and event; conflicts drive recusal in P06; whistle-blower intake routed to the sealed vigil mechanism |
| Lender boundary respected | For Finbyx tenants, recovery litigation appears as a read-only projection from Ecosystem events; LDC never issues SARFAESI/recovery notices or recomputes recovery exposure (NN-39, D-41) |

---

## 2. Scope (in / out)

**In scope**
- Notice management: incoming notices of all types (statutory, tax, regulator, labour, corporate, consumer, IP, shareholder, civil and criminal), outgoing non-recovery notices and replies, notice master with reply windows and severity.
- Matter (case) management: courts, tribunals (NCLT, NCLAT, DRT/DRAT as party other than lender-recovery, ITAT, CESTAT, SAT, TDSAT, APTEL, RERA, consumer commissions, labour fora), writs, criminal matters, arbitration and mediation, insolvency proceedings where the tenant is a creditor or corporate debtor in non-recovery capacity; hearings, orders, appeals, execution, settlement.
- Counsel management: empanelment, conflict checks, engagement letters, fee arrangements, invoices, scorecards; counsel portal.
- Legal spend: budgets, accruals, invoice validation (rate card, GST, TDS fields), approvals; payment hand-off only.
- Provisioning and disclosure: likelihood assessment, Ind AS 37/AS 29 classification, quarterly movement schedule to P11, Reg 30 cases to P06, RBI inspection annexure views.
- Regulator engagements: inspections (RBI RBS/ISE, NHB, NABARD, SEBI, IFSCA, IRDAI, Registrars, labour, tax audits by authorities), RFIs, exit meetings, observations, RMP/MAP items, compliance submissions, closure; regulator proceedings (show-cause notices, adjudication, compounding, consent settlement, penalties, appeals).
- Contract lifecycle (CLM): intake, authoring via LawDocs templates, negotiation with redlines, approval by value/risk, execution (eSign/e-stamp checklist), repository with hierarchy, obligation extraction, renewals and expiry, termination; outsourcing contracts linked to P12.
- Registrations and licences register: certificates of registration, GSTIN, Shops & Establishments, trade licences, FSSAI where relevant, IEC, professional tax, labour registrations, software licences of regulatory relevance, ISO certificates, DSCs of the entity (metadata only), domain registrations; renewal workflows.
- Ethics registers: conflicts of interest, gifts and hospitality, related-party declarations (feeding P06 RPTx), outside business interests, and the link to the sealed vigil mechanism (whistle-blower intake and case handling stay sealed).
- MIS for the legal function (feeds P28), exports, AI assistance (drafts only).

**Out of scope**
- Lender debt recovery (SMA/NPA engine, recall, SARFAESI ss.13(2)/13(4), possession, valuation, auction, DRT original applications as lender, IBC s.7 as financial creditor) — Finbyx Recovery Suite / standalone Udolex (Ecosystem Spec §6.8, §6.10; D-41). An optional "Recovery Notices Lite" pack for lenders without Finbyx is specified behind flag `lit.recovery_lite.enabled = OFF` pending counsel opinion (OI-P26-03).
- Filing in courts or e-filing portals, payment of court fees or counsel fees, service of notices by LDC itself (LDC prepares, the user files or dispatches; NN-08).
- Legal advice: LDC is not a law firm; reserved advocacy services are delivered by eligible practitioners through P21 (D-32).
- ADR adjudication (Equator Resolution — referral only on explicit choice, as in P14).
- POSH inquiries (P13 sealed module) — P26 only receives counts.

---

## 3. Personas and permissions touched

| Role | What they do in P26 | Notes |
|---|---|---|
| `ten_kmp` (GC — General Counsel / Head Legal) *(new sub-type, D-48)* | Owns the legal register, approves outgoing notices and settlements within delegation, sets likelihood assessments, approves privilege downgrades | Default owner of all matters |
| `ten_legal_user` *(proposed, crossfile to Appendix D)* | Legal team member: intake, triage, drafting, hearing updates, counsel coordination | Maker for legal records |
| `ten_kmp` (CS) | Licences register owner (default), ethics declarations campaigns for directors/KMP, Reg 30 coordination | |
| `ten_kmp` (CCO) | Regulator engagements owner (default), Reg 30 materiality determination with GC (delegation matrix) | |
| `ten_kmp` (CFO) | Provision review and approval, legal spend approval within delegation, contract approvals by value | |
| `ten_dept_head` | Business owner of contracts and of matters arising in the department; responds to RFIs and observations | |
| `ten_maker` / `ten_checker` | Maker-checker on registers (licences, ethics), contract approvals routing | NN-05 |
| `ten_employee` | Submits ethics declarations, gifts declarations, contract intake requests | Self-service shell |
| `ten_board_member`, `ten_committee_member` | See litigation and regulator summaries in packs; declare conflicts | |
| `ten_internal_auditor` | Reads registers; verifies closure of observations (P10) | Read |
| `ten_external_auditor` | Reads provision schedule and matter list within a scope grant (P10 FR-P10-89) | Privileged documents excluded unless GC grants |
| `ext_counsel` *(new, D-48)* | Empanelled counsel firm users: see only assigned matters; post hearing updates, orders, invoices; secure messaging | No access to any other module |
| `ten_supervisor_view` | Time-boxed read of regulator-engagement records relevant to the inspection | D-12; privileged excluded |
| `dlv_professional` | LawDocs professional acting as maker under a delivery grant for a retainer (drafting, notice replies) | Never checker or approver (NN-43) |
| `svc_vidhi` (VA-16 Legal Matters Assistant, proposed) | Drafts summaries, classifications, replies, digests | On behalf of a named user; L1 default (NN-50) |

Access is matter-scoped (ABAC attribute `matter_id`, `privilege`, `confidentiality_class`): a user sees a matter only if they own it, are a member of its team, are in the legal function with "all matters" permission, or hold a grant. Privileged documents follow P07 FR-P07-67.

---

## 4. Functional requirements

### 4A. Notice management

**FR-P26-01 — Notice intake channels.** Notices arrive by: e-mail-in address per entity (P07 §4T) with attachment OCR; scan upload (single or batch); portal downloads uploaded by users (GST, income-tax, MCA, EPFO, SEBI, RBI, CERT-In); API from client systems (P18); manual entry. Each notice gets a Notice ID, received-on timestamp (the clock start; NN-33 — the earliest receipt by the entity or any agent acting for it, never the date the user logged it), channel, sender, addressee entity and the original file hashed into the vault.

**FR-P26-02 — Classification proposal.** VA-16 proposes: direction (incoming/outgoing), notice type from the notice master, statute and section, issuing authority, reference number, date of notice, response window, hearing date if any, amount demanded, severity, related entity/department/person, related contract or matter, and language (with translation offered, P07 §4P). Each field shows confidence and the source text span; the triage user confirms or corrects (NN-04, NN-47 — AI never sets severity on its own).

**FR-P26-03 — Notice master (rule pack, Governed).** About 70 notice types seeded from the owner's baseline (Table 9-1, 34 types) and extended, each with: statute and section, issuing authority, default reply window (with computation rule: calendar or working days, from date of notice or date of receipt), default severity, default owner role, required approvals, standard reply template, linked compliance checkpoint (if any), and escalation ladder. Examples (all windows **[VERIFY]** before activation): RBI/SEBI/IRDAI/IFSCA show-cause notice — window as stated in the notice (fallback 21 days), Critical; GST DRC-01 — 30 days, High; GST ASMT-10 — 30 days, High; income-tax s.143(2)/s.142(1) equivalents under the Income-tax Act 2025 — as in notice, High; Negotiable Instruments Act s.138 demand received — 15 days, High; IBC s.8 demand notice received — 10 days, Critical; MCA s.206 inquiry — as in notice, High; ROC s.248 strike-off notice — 30 days, Critical; EPFO s.7A summons — hearing date, High; consumer commission notice — as in notice, Medium; trademark cease-and-desist — 15 days, Medium; CERT-In direction — 6 hours/as directed, Critical. Tenants may add types (T) and tighten windows (G); they cannot loosen statutory windows (NN-38).

**FR-P26-04 — Triage.** Same business day: severity and owner set by the triage user (default owner from the notice master), acknowledgement sent where required (template), notice linked to an existing matter or flagged "may convert to matter". Critical notices page the GC and CCO immediately and appear on the CEO dashboard (P28).

**FR-P26-05 — Incoming-notice lifecycle (10 stages).** Inbox → Classification → Triage → Acknowledgement → Investigation (facts, documents, internal inputs as tasks) → Draft reply (template + VA-16 draft, lawyer finalised) → Approval (authority and delegation matrix, §4I) → Dispatch with proof of service (RPAD/speed post receipt, e-mail delivery record, portal acknowledgement uploaded) → Close or convert to matter (≤ 7 days after dispatch) → Audit and disclose (financial-statement and Reg 30 assessments). Stage guards: cannot dispatch without approval; cannot close without proof of service or a recorded decision not to reply (GC approval).

**FR-P26-06 — Outgoing non-recovery notices.** Triggers: manual, or events (contract breach detected from CLM obligations, unpaid vendor dues, IP infringement report, employee absconding — HR case from P13 with HR approval). Data assembly from the source record → statute-correct template → VA-16 draft → **mandatory legal review** (human gate; AI never dispatches, NN-14) → approval by value/type → dispatch (RPAD, speed post, e-mail, portal) → proof and statutory clock (e.g., reply period) → escalation on non-response (convert to matter) → audit. Recovery-related notices for lenders are blocked unless `lit.recovery_lite.enabled` is ON (D-41).

**FR-P26-07 — Tax notices and tax matters.** Tax notices (GST, income tax, customs, professional tax) carry: tax type, notice type, authority and reference, period, amount in dispute (tax, interest, penalty), response due, stage, provision assessment, owner and consultant; they link to P11 returns and reconciliations (GSTR-2B vs books, TDS mismatches) so that the investigation starts from the data. Appeals (first appellate authority, GST Appellate Tribunal, ITAT, High Court) are matters with limitation clocks.

### 4B. Matter (case) management

**FR-P26-08 — Matter record.** Fields: matter ID; cause title ("X vs Y"); matter type (civil suit, writ, criminal complaint/FIR, arbitration, mediation, consumer, labour, tax appeal, company petition, insolvency, regulatory appeal, other); forum and bench; jurisdiction (state, city); case/diary/CNR number; filing date; party role (petitioner, respondent, applicant, complainant, accused, claimant, intervenor); opposing parties and their advocates; claim value and currency; relief sought; related notices, contracts, employees, products, branches; matter team (GC, legal user, business owner, counsel); privilege flag; confidentiality class; stage; next date; status (ACTIVE, STAYED, DISPOSED, APPEAL_FILED, EXECUTION, SETTLED, WITHDRAWN, CLOSED); risk score; provision class; Reg 30 flag; tags.

**FR-P26-09 — Litigation lifecycle (12 stages) with guards.** Onboarding (≤ 2 days of trigger) → Counsel engagement with conflict check and fee letter (≤ 5 days) → Filing / vakalatnama / court fees → Pre-trial (pleadings, discovery, admissions) → Hearings → Interim orders (stay, injunction, interim relief) → Evidence → Arguments → Order/Judgment → Appeal evaluation (limitation clock) → Execution/compliance → Closure and lessons learnt. Guards (rule pack per matter type): e.g., cannot enter Arguments before Evidence closed for civil suits; cannot close while an appeal limitation clock is open unless the GC records "no appeal" with reason; cannot close while order directions remain open. Writs, arbitrations, consumer and tax matters have their own stage sets (configurable, T within the type's Locked skeleton).

**FR-P26-10 — Matter docket (append-only).** A court-style chronological register per matter: docket number, date/time, entry type (filing, hearing, order, adjournment, correspondence, internal note, settlement offer), title, linked document and version, actor, stage, deadline link, privilege tag, ledger reference. No edit or delete; corrections are new entries referencing the corrected one (NN-02 pattern).

**FR-P26-11 — Hearings and cause lists.** Hearing diary per matter (date, bench, item number, purpose, appearance, outcome, next date, adjournment reason); daily digest at `lit.hearings.digest_time` to owners and counsel of hearings in the next N days; calendar entries (P04) for the matter team; counsel or the legal user records the outcome within 24 hours (reminder ladder) — missing outcomes escalate to the GC. Where a lawful, licensed feed of e-Courts case status and cause lists is contracted, it updates next dates automatically (flag `lit.ecourts.enabled = OFF`; no scraping; OI-P26-04).

**FR-P26-12 — Orders and directions.** Uploading an order or judgment triggers VA-16 to propose: outcome (allowed, dismissed, partly allowed, disposed with directions, adjourned), holdings summary, quantum, costs, directions with due dates, whether appealable and the appeal limitation, and the next date. The legal user confirms; confirmed directions create P04 tasks with owners and due dates (one confirmation step); compliance evidence closes each direction. Ecosystem `OrderRecorded` events from Finbyx RS create the same projection for recovery matters.

**FR-P26-13 — Limitation engine.** Limitation and appeal periods are computed from a rule pack (Limitation Act 1963 Schedule and special statutes: e.g., A&C Act s.34 three months plus thirty days, appeal periods for NCLAT, ITAT, GSTAT, SAT, High Court appeals) with exclusion rules (time to obtain certified copy where the law allows) **[VERIFY each period; values Governed, advisory until verified — NN-38]**. Each clock shows start event, period, computed last date, buffer target and owner; reminders at T-30/T-15/T-7/T-3/T-1. Clocks never pause (NN-33); condonation applications are matters in themselves.

**FR-P26-14 — Settlement and ADR.** Settlement offers and counter-offers log (without-prejudice tagged), settlement terms, payment schedule, approvals per delegation matrix, settlement deed (template via P07), compliance tracking of the schedule, referral to mediation (Commercial Courts Act s.12A pre-institution mediation, court-annexed, Lok Adalat) and, only on explicit choice, to Equator Resolution (P14/P18 referral contract).

**FR-P26-15 — Recovery projection (Finbyx tenants).** Ecosystem events `RecoveryCaseOpened`, `RecoveryCaseClosed`, `LitigationCaseOpened`, `LitigationCaseUpdated`, `HearingScheduled`, `OrderRecorded`, `LitigationCaseClosed` (Ecosystem Spec §6.8, §6.10; `in.infrabyx.recovery.*`, `in.infrabyx.litigation.*`) create read-only projection matters tagged `owner_system = FX`. They appear in registers, calendars, MIS and Board summaries; edits happen in Finbyx; LDC adds only internal notes and links (NN-23, NN-39). Recovery provisioning is shown from Finbyx (IRACP/ECL), not computed by Ind AS 37 bands (§J.16).

### 4C. Counsel management and counsel portal

**FR-P26-16 — Empanelment.** Counsel firms and individual advocates are empanelled with: name, bar enrolment number and State Bar Council, practice areas, forums, cities, rate card (per appearance, per hour, fixed fee, success-fee prohibited for advocates — fee arrangements per Bar Council rules are recorded, contingency fees blocked, NN-20), GST registration status (reverse-charge applicability for legal services — recorded, **[VERIFY]**), conflict declarations, documents (engagement terms, NDA). Empanelment review annually with scorecards.

**FR-P26-17 — Conflict check.** Before engagement: the firm declares conflicts against the opposing parties and related parties; LDC checks the tenant's own matter list for the firm acting against the tenant's group entities (where known). Results recorded; GC approval required to proceed despite a flag.

**FR-P26-18 — Engagement and fees.** Engagement letter generated from template with scope, fee, billing cycle, budget, reporting obligations, confidentiality and data-protection clauses (DPDP processor terms where personal data is shared); eSigned (P07). Budgets per matter and per stage; variance alerts at 80% and 100% of budget.

**FR-P26-19 — Counsel portal.** `ext_counsel` users (MFA) see only assigned matters: docket, documents shared with them, hearing diary; they post hearing updates (next date, what transpired, order copy), upload pleadings and opinions (privileged by default), raise and answer queries, and submit invoices. Updates enter a review queue for the legal user (maker-checker light: counsel is maker, legal user accepts). Counsel cannot see other matters, registers or modules.

**FR-P26-20 — Legal spend.** Invoice intake (portal or e-mail-in) with validation against rate card and budget, GST and TDS fields (Income-tax Act 2025 section for professional fees **[VERIFY]**), accrual per period, approval per delegation matrix, and hand-off of the approved invoice to the tenant's accounts payable (P18 accounting/ERP export); LDC never pays. Scorecards: timeliness of updates, outcome record, cost vs budget, responsiveness.

### 4D. Provisioning, disclosure and reporting

**FR-P26-21 — Likelihood and exposure assessment.** Per matter, per quarter (or on a material event): likelihood class PROBABLE / POSSIBLE / REMOTE with rationale and optional percentage estimate (§J.16 — classes follow Ind AS 37 definitions; the owner's fixed bands are guidance only), best estimate of outflow, range, timing, reimbursement expected, assessor and reviewer (GC → CFO). VA-16 may draft the rationale from pleadings and orders; the class and amount are human decisions (NN-47).

**FR-P26-22 — Provision and contingent-liability schedule.** Quarterly schedule (opening, additions, utilisation, reversals, unwinding of discount, closing) and contingent-liability list with nature and estimate, produced for P11 notes and the statutory auditor (scope grant, P10). Frozen at quarter close; changes after freeze create a variance record (NN-22).

**FR-P26-23 — Reg 30 for listed entities.** A matter marked potentially material opens a P06 disclosure case (P06 FR-P06 §4K) with materiality test inputs (policy thresholds, quantum vs Reg 30(4) lower-of test), 24-hour clock where applicable **[VERIFY]**, draft announcement and post-event updates; the determination is recorded by the authorised KMP per delegation (GC + CCO; CEO above threshold).

**FR-P26-24 — Regulatory and Board reporting.** Standard views: legal cases filed by and against the entity; orders passed against the entity or its directors; matters involving KMP; regulator proceedings; provision schedule; top-20 exposures; ageing; forum-wise register. RBI inspection annexure views for REs (format per inspection request) are generated from the register. Board and Audit Committee summaries feed P06 packs; MIS LIT_01–LIT_06 (owner baseline) are published to P28.

**FR-P26-25 — Risk scoring (advisory).** A 1–5 matter risk score from weighted drivers (likelihood class, quantum, reputational sensitivity, regulator involvement, strategic/precedent impact, counterparty profile, forum history) — weights tenant-configurable, model version recorded; the score is advisory and never sets provision class or materiality (NN-47). It feeds P08 legal-risk KRIs (count and value of Critical matters, provision trend).

### 4E. Legal vault, privilege and folders

**FR-P26-26 — Document classes and privilege.** Over 40 legal document classes (plaint, written statement, writ petition, counter-affidavit, rejoinder, application, order, judgment, decree, notice, reply, counsel opinion, settlement deed, vakalatnama, affidavit, evidence, transcript, invoice, engagement letter, internal note…) each with default privilege (PRIVILEGED / CONFIDENTIAL / NON_PRIVILEGED), retention class (e.g., pleadings 10 years after closure; orders and judgments permanent; notices 8 years; counsel opinions permanent and privileged) **[VERIFY retention floors in rule pack]**, and a "producible" flag. Privilege downgrade requires GC approval (P07 FR-P07-67) and is a ledger event. Privileged documents are excluded from auditor and regulator grants and from AI retrieval for non-legal users.

**FR-P26-27 — Standard matter folders.** Each matter has folders `01 Pleadings`, `02 Orders and Judgments`, `03 Notices and Replies`, `04 Evidence`, `05 Correspondence`, `06 Counsel Opinions (Privileged)`, `07 Hearings and Cause Lists`, `08 Costs and Invoices`, `09 Settlement`, `10 Internal Notes (Privileged)`; recovery projections from Finbyx add `11 Loan and Security`, `12 Recovery – SARFAESI`, `13 Valuation and Sale` as read-only links. These map into LDC-EXPORT-1.0 top-level folder `26 Legal Matters, Contracts and Licences/` (Appendix M §M.3, authoritative) *(v1.1, X1)*.

**FR-P26-28 — Type copies and translation.** Notices and orders in regional languages or handwriting get type copies and English translations through P07 §4O–§4P; the original remains the authoritative document; translations are labelled until reviewed.

### 4F. Regulator engagements — inspections, observations and proceedings (D-41)

**FR-P26-29 — Engagement record.** One record per inspection, examination, thematic review, snap check, information call or proceeding: regulator (RBI DoS, NHB, NABARD, SEBI, stock exchanges, IFSCA, IRDAI, MCA/ROC, Registrar of Co-operative Societies, CERT-In, DPB, tax authorities, labour authorities, foreign regulators via P25), type, reference number, reference date for data, period covered, inspection team, on-site window, entity scope, owner (CCO by default), status, confidentiality (REGULATOR_CONFIDENTIAL sealed class).

**FR-P26-30 — Information requests (RFI tracker).** Each request: item text, requested-on, due, owner, data source, response pack (documents and data extracts, hashed), reviewer, submitted-by, channel (e-mail, DAKSH, physical), submission timestamp and reference. Response packs are assembled from LDC records (P04 register snapshots, P07 policies, P06 minutes, P11 returns with lineage, P08/P09 metrics) with one-click inclusion; VA-01/VA-02 propose the pack contents and a readiness score per request (advisory). Submission is by the user through the official channel (NN-08); LDC records reference and hash.

**FR-P26-31 — Exit meeting and observations.** Draft observations (e.g., RBI Inspection Report / Risk Assessment Report observations, SEBI inspection findings, IRDAI, IFSCA, Registrar audit/inspection notes) are imported (upload; VA-01 proposes a split into individual observations with paragraph references) and confirmed by the CCO. Each observation: reference, text, category (governance, credit, KYC/AML, IT/cyber, compliance, customer conduct, financial reporting…), severity as rated by the regulator, regulator's direction, management response, action plan (RMP/MAP items) with owners and due dates, linked checkpoints and policies, evidence, status.

**FR-P26-32 — Compliance submissions and closure.** The compliance (or MAP progress) submission is prepared per the regulator's format and timeline (e.g., RBI compliance within the period stated in the letter **[VERIFY per direction]**), approved by the Board/committee where required (P06 agenda auto-suggest), and submitted by the user (DAKSH or as directed). Before reporting an observation closed, the closure-verification test in P10 (FR-P10-97) must pass. Observations remain open until the regulator's closure is recorded; repeat observations in the next inspection are flagged automatically.

**FR-P26-33 — Regulator proceedings.** Show-cause notices, adjudication proceedings, compounding/consent applications, penalties, directions under the regulator's statute (RBI Act s.45L/45M/58B/58G; BR Act s.35A/47A; SEBI Act s.11/11B/15-I; IRDAI; IFSCA; Companies Act s.454 adjudication), appeals (SAT, appellate authorities, High Court): reply windows from the notice master, hearings, orders, penalties paid (evidence), appeals with limitation, and disclosure obligations (Board's report, Reg 30, RBI annual disclosure of penalties). Each concluded proceeding posts to the P06 penalties, strictures and warnings register (FR-P06-77).

**FR-P26-34 — Live inspection workspace.** During on-site windows: a war-room view with RFIs due today, overdue, submitted; responses awaiting review; documents shared; inspector queries; a tamper-evident submission log (hash-chained); daily status digest to the CEO and CCO. The supervisor's own read access uses the P10 inspection room (FR-P10-86; D-12).

### 4G. Contract lifecycle management (CLM)

**FR-P26-35 — Contract record.** Type (customer, vendor/outsourcing, co-lending, DSA/DMA, LSP, lease, employment template (bulk), NDA, licence, IP, loan from lenders, guarantee, MoU, group intra-company, other), counterparty (vendor or entity master; group company flag for RPT), owner department, stage, value and currency, effective date, expiry date, auto-renewal flag and renewal term, notice period and notice deadline (computed), governing law and jurisdiction, dispute-resolution clause (court, arbitration seat, institution), stamp duty and e-stamp reference (state), signature references, related-party flag (feeds P06 RPTx and the ethics register), outsourcing flag (feeds P12 register and materiality assessment), data-processing flag (DPDP processor/fiduciary terms; P12), parent/child hierarchy (master → amendment → SOW/order).

**FR-P26-36 — CLM stages.** Intake request (form; required fields by type) → authoring (LawDocs template or clause library via P18; or counterparty paper uploaded) → negotiation (versioned redlines using the P07 redline engine; internal comments separate from counterparty-visible comments) → approval routed by value, risk tier and type through the delegation matrix (maker-checker; legal review mandatory above threshold or for non-standard clauses) → execution (eSign envelope or wet signature with e-stamp checklist by state; IT Act First Schedule exclusions blocked from Aadhaar eSign — P07) → repository (signed copy sealed, hash) → obligation and milestone monitoring → renewal/expiry/termination → archive.

**FR-P26-37 — Obligation extraction.** On execution, VA-16 proposes the contract's obligations (payment, reporting, audit rights, SLAs, insurance, confidentiality, data-breach notification, termination triggers, regulatory clauses such as RBI outsourcing access/audit rights) with clause references; the owner confirms each; confirmed obligations become tenant checkpoints in P04 (tenant overlay, NN-03/NN-04) with owners, frequencies and evidence expectations.

**FR-P26-38 — Renewal and notice alerts.** Alerts at `lit.contracts.renewal_alert_days` (default 90/60/30) before expiry and before the notice deadline for auto-renewing contracts ("auto-renew risk"); a renewal decision task (renew, renegotiate, terminate) is created for the owner; decisions are recorded with reasons.

**FR-P26-39 — Regulatory contract checks.** For REs, contract-type checklists verify mandatory clauses (e.g., RBI outsourcing directions — audit and inspection access for the RE and RBI, confidentiality, sub-contracting, BCP, termination; digital-lending LSP agreements; co-lending agreements; DSA codes of conduct) from the content library; gaps are listed before approval; checklists are pack data (P15), not AI judgments.

### 4H. Registrations and licences register

**FR-P26-40 — Licence record.** Licence/registration type, number, issuing authority, legal entity and location/branch, issue date, validity/expiry (or perpetual), renewal lead time, renewal process and portal, fees, conditions attached (each condition can become a checkpoint), responsible owner, documents (certificate, application, acknowledgements), status (ACTIVE, RENEWAL_DUE, RENEWAL_FILED, EXPIRED, SURRENDERED, CANCELLED). Seeded from onboarding (P01 "licences held" step) and the entity profile (P15): e.g., RBI Certificate of Registration (NBFC/ARC/UCB licence), SEBI registration certificates (perpetual with fees), IRDAI registration (perpetual after the 2025 amendment for intermediaries — recorded with periodic fee obligations **[VERIFY]**), IFSCA registration, GSTIN per state, Shops & Establishments per location, trade licence, professional tax registration/enrolment, labour registrations (Codes), FSSAI (where relevant), IEC, ISO certificates, domain names, DSCs of authorised signatories (metadata and expiry only; no keys).

**FR-P26-41 — Renewal workflow.** At lead time a renewal task with checklist is created; filing evidence moves status to RENEWAL_FILED; the new certificate closes it; expiry without renewal raises a Critical compliance issue and a Board-visible exception. Conditions attached to licences (e.g., minimum net owned fund, branch limits, reporting conditions) are linked to checkpoints and monitored.

**FR-P26-42 — Branch and location view.** Licences per location on a map/list (establishment registrations, trade licences, signage permissions where tracked), so that opening a new branch triggers the location's licence set (event catalogue, P04 IMP-028).

### 4I. Ethics registers

**FR-P26-43 — Declarations.** Campaigns (annual and on joining) and event-based declarations for directors, KMP, senior management and employees as configured: conflicts of interest (nature, related party, value, mitigation), outside directorships and business interests, relatives in the organisation or at counterparties, gifts and hospitality given and received (value, counterparty, purpose, date), related-party information (feeds P06 RPTx and Ind AS 24/AS 18 lists). Declarations are signed (eSign or authenticated acknowledgement) and versioned; directors' statutory disclosures (MBP-1) remain in P06 and are cross-referenced.

**FR-P26-44 — Thresholds and approvals.** Gifts and hospitality above `lit.ethics.gift_preclear_value` need pre-clearance; aggregation per counterparty per year; auto-approve below threshold, escalate above (line manager → compliance → GC); declined gifts recorded. Conflicts are reviewed by compliance with a mitigation decision (recusal, reassignment, disclosure only, prohibited); recusal decisions flow to P06 meeting packs (FR-P06-72) and to CLM approvals (a conflicted approver is removed from the chain).

**FR-P26-45 — Vigil mechanism link.** Whistle-blower reports (Companies Act s.177(9)–(10), LODR Reg 22, RBI whistle-blower expectations) are received through a sealed intake (P14/P13 sealed pattern, NN-13); P26 receives only counts and case-category statistics for the Audit Committee unless the Audit Committee chair grants a named investigator access. Investigation hand-offs from P10 special investigations come here as legal matters with restricted access.

**FR-P26-46 — Analytics (advisory).** Matching of declarations against counterparties in contracts, vendor master and agenda items flags potential undeclared conflicts to compliance only; flags are never presented as findings and never decide anything (NN-47).

### 4J. Authority and delegation matrix

**FR-P26-47 — Matrix (Governed).** Default thresholds from the owner's baseline (Table 17-1), tenant-configurable: approve outgoing notice/reply (≤ ₹10 lakh Legal Head; ₹10 lakh–₹1 crore GC; ₹1–10 crore GC; > ₹10 crore GC + CEO); engage counsel/set fee (Legal Head / GC / GC / GC + CFO); approve litigation cost or bill (Legal Head / GC / GC + CFO / CFO + CEO); approve settlement or waiver (— / GC / GC + CFO / Board or committee); Reg 30 materiality (CCO / CCO / CCO + GC / CCO + GC + CEO); contract approval by value and risk tier. The rules engine blocks any action that exceeds the actor's delegation and routes it to the next level; SLA breaches escalate one level. Changes to the matrix are Governed (maker-checker, effective date) and require a Board/committee reference where the delegation is Board-approved.

### 4K. AI assistance (VA-16 Legal Matters Assistant — proposed for Appendix AA/K)

**FR-P26-48 — Skills.** Notice classification and field extraction (FR-P26-02); matter summary and chronology from the docket; order/judgment digest and direction extraction (FR-P26-12); deadline and limitation extraction (proposals only — the engine computes clocks); draft replies and notices from templates with citations; contract obligation extraction (FR-P26-37); RFI pack proposals (FR-P26-30); likelihood rationale drafts (FR-P26-21). Default autonomy L1 (drafts and proposals); L0 for privileged contexts unless the GC enables per matter; never L2 for external effects (dispatch, filing, settlement, payment) — those are not exposed (NN-14, NN-50). Every legal statement cites the source document page or the instrument paragraph (NN-06).

### 4L. Group, global and migration

**FR-P26-49 — Group and foreign entities.** Matters, contracts, licences and regulator engagements carry the legal entity; foreign subsidiaries (P25 `gem`) use jurisdiction packs for notice types, limitation and licences where published, otherwise tenant data labelled "tenant data"; official-language documents retained with labelled translations (NN-54); group dashboards aggregate exposures by entity and currency (P25 FX rates for display only).

**FR-P26-50 — Legacy import.** Excel/CSV import of matter registers, licence registers and contract registers with column mapping, validation, preview and an undo window (NN-49); docket back-fill from uploaded orders (VA-16 proposes dates and entries; user confirms).

### 4M. Dashboards and MIS

**FR-P26-51 — GC dashboard.** Widgets: Critical notices open; replies due in 7 days; hearings this week (with missing outcome flags); limitation clocks < 30 days; orders with open directions; provision movement this quarter; top exposures; counsel spend vs budget; RFIs due; open regulator observations by due date; licences expiring in 90 days; contracts with auto-renew risk; ethics declarations pending. Each widget opens a filtered list with bulk actions (assign, remind, export) and undo for bulk changes (NN-49).

**FR-P26-52 — MIS feeds.** LIT_01 active litigation and forum-wise register (monthly); LIT_02 notice inflow, triage TAT, reply-on-time (weekly); LIT_03 provision and contingent liabilities (quarterly); LIT_04/05 recovery cascade and recovery rate (projected from Finbyx, read-only); LIT_06 Reg 30 disclosure log; REG_01 regulator observations ageing; CLM_01 renewals and auto-renew risk; LIC_01 licence expiries; ETH_01 declarations completion and gifts register summary — all published as report definitions to P28.


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P26-X01 — Inbound records from other modules.** The ethics registers receive P13 self-service declarations (FR-P13-X01); the licence register receives `pack.EntityLicenceAdded` from P15 (FR-P15-X01); Registrar proceedings from P16 open matters of type `REGISTRAR_PROCEEDING` (FR-P16-X01); `lit.matters` consumes the ecosystem litigation events (`LitigationCaseOpened/Updated/Closed`, `HearingScheduled`, `OrderRecorded`; P18 routing) and the notices mailbox (P18 FR-P18-87).

**FR-P26-X02 — Report definitions for P28.** P26 registers report definitions LIT_01–LIT_06 (matters by forum and stage, Critical matters, hearings next 30 days, provision movement, counsel spend, limitation watch), REG_01 (regulator observations and compliance status), CLM_01 (contracts renewing in 90 days), LIC_01 (licences expiring) and ETH_01 (declarations and conflicts) in the P28 catalogue.

---

## 5. Workflows and state machines

### 5.1 Incoming notice (`lit.notice`)

`RECEIVED` → `CLASSIFIED` (user-confirmed) → `TRIAGED` (owner, severity) → `ACKNOWLEDGED` (optional by type) → `UNDER_INVESTIGATION` → `REPLY_DRAFTED` → `PENDING_APPROVAL` → `APPROVED` → `DISPATCHED` (proof uploaded) → `CLOSED` | `CONVERTED_TO_MATTER`. Side transitions: `NO_REPLY_DECIDED` (GC approval with reason) → `CLOSED`. Timers: reply due (from notice master; statutory, never paused — NN-33), internal target (T-3 by default), reminders, escalation to GC at T-1 and on breach (breach creates a Critical issue in P04).

### 5.2 Matter (`lit.matter`)

Stages per FR-P26-09 with guards; status overlay `ACTIVE`/`STAYED`/`DISPOSED`/`APPEAL_FILED`/`EXECUTION`/`SETTLED`/`WITHDRAWN`/`CLOSED`. Closing requires: no open directions, no open limitation clock (or GC "no appeal" record), final provision assessment, lessons-learnt note (optional by setting). Reopen only by a new docket entry with reason (e.g., remand).

### 5.3 Regulator engagement (`lit.reg_engagement`)

`ANNOUNCED` → `DATA_REQUESTED` (RFIs) → `ON_SITE` → `EXIT_MEETING_HELD` → `DRAFT_OBSERVATIONS_RECEIVED` → `RESPONSE_SUBMITTED` → `FINAL_REPORT_RECEIVED` → `COMPLIANCE_IN_PROGRESS` (observations with MAP items) → `COMPLIANCE_SUBMITTED` → `CLOSED_BY_REGULATOR`. Observation sub-machine: `OPEN` → `ACTION_IN_PROGRESS` → `COMPLIED_PENDING_VERIFICATION` → (P10 closure test PASS) `VERIFIED` → `REPORTED_CLOSED` → `CLOSED_BY_REGULATOR`; FAIL returns to `ACTION_IN_PROGRESS`.

### 5.4 Contract (`lit.contract`)

`INTAKE` → `DRAFTING` → `NEGOTIATION` → `PENDING_APPROVAL` → `APPROVED` → `PENDING_SIGNATURE` → `EXECUTED` → `ACTIVE` → (`RENEWAL_DUE` → `RENEWED` | `TERMINATED` | `EXPIRED`) → `ARCHIVED`. Amendments create child contracts; termination requires reason, notice evidence and obligation wind-down tasks (e.g., data return/deletion for processors).

### 5.5 Licence (`lit.licence`)

`ACTIVE` → (lead time) `RENEWAL_DUE` → `RENEWAL_FILED` → `ACTIVE` (new validity) | `EXPIRED` (Critical issue) ; `SURRENDERED`, `CANCELLED` terminal with evidence.

### 5.6 Ethics declaration (`lit.ethics_declaration`)

`REQUESTED` → `SUBMITTED` → `UNDER_REVIEW` → `NO_CONFLICT` | `MITIGATION_DECIDED` (recusal/reassignment/disclosure/prohibited) → `CLOSED`; gifts: `DECLARED` → `AUTO_APPROVED` | `PENDING_PRECLEARANCE` → `APPROVED` | `DECLINED` (returned/donated evidence).

### 5.7 Clock computation (pseudo-code)

```
function computeDue(clockDef, startEvent, entityCalendar):
  start = startEvent.earliestReceipt      // NN-33: earliest receipt by entity or its agent
  if clockDef.excludeCertifiedCopyTime and startEvent.certifiedCopyAppliedOn:
      exclusion = startEvent.certifiedCopyReceivedOn - startEvent.certifiedCopyAppliedOn
  due = addPeriod(start, clockDef.period, clockDef.unit, clockDef.dayType, entityCalendar) + exclusion
  if clockDef.lastDayHolidayRule == NEXT_WORKING_DAY and isHoliday(due, entityCalendar): due = nextWorkingDay(due)
  return { due, ruleVersion: clockDef.version, verified: clockDef.status == VERIFIED }   // unverified → advisory (NN-38)
```

---

## 6. Screens and UX

Menu root in the tenant app: **Legal** (icon: scale), visible to roles with any `lit.*` permission; Ethics declarations also appear under **My Work › Declarations** for every employee. "i" help keys `hlp.lit.*` explain terms such as *limitation*, *vakalatnama*, *contingent liability*, *show-cause notice*, *RMP/MAP*, *auto-renewal*, *privilege*.

| Screen ID | Name | Menu path | Key content and fewer-click design |
|---|---|---|---|
| SCR-LIT-01 | GC Dashboard | Legal › Home | Widgets FR-P26-51; each opens a filtered list; keyboard `g l` |
| SCR-LIT-02 | Notice Inbox | Legal › Notices | Unclassified notices with AI proposals; side-by-side original and proposed fields; `a` accept field, `Enter` confirm all, triage owner picker |
| SCR-LIT-03 | Notice Workspace | Legal › Notices › {notice} | Stepper of 10 stages; reply editor (template + draft); approval panel per delegation; dispatch and proof upload |
| SCR-LIT-04 | Matters Register | Legal › Matters | Grid with forum, stage, next date, exposure, provision class, risk score, owner; saved views; bulk assign |
| SCR-LIT-05 | Matter Workspace | Legal › Matters › {matter} | Tabs: Overview, Docket, Hearings, Orders & directions, Documents (privilege badges), Counsel & costs, Assessment, Settlement, Related |
| SCR-LIT-06 | Hearings Diary | Legal › Hearings | Week/month view across matters; outcome-capture form; missing outcomes highlighted |
| SCR-LIT-07 | Limitation & Deadlines | Legal › Deadlines | All clocks with last date, buffer, owner, verification status badge (advisory if unverified) |
| SCR-LIT-08 | Order Digest Review | Matter › Orders › {order} | AI-proposed outcome and directions; convert directions to tasks in one confirmation |
| SCR-LIT-09 | Counsel Directory | Legal › Counsel | Empanelled firms; rate cards; scorecards; conflict declarations; empanelment review |
| SCR-LIT-10 | Counsel Portal (external) | `apps/web` external shell | Assigned matters only; post hearing update; upload; queries; invoices |
| SCR-LIT-11 | Legal Spend | Legal › Spend | Invoices queue with validation results; budgets vs actuals; accruals; approvals |
| SCR-LIT-12 | Provision Schedule | Legal › Provisions | Quarter view; assessments by matter; movement schedule; freeze; export to P11 |
| SCR-LIT-13 | Regulator Engagements | Legal › Regulators | Engagements list; status; owner; next due |
| SCR-LIT-14 | Inspection War Room | Legal › Regulators › {engagement} › Live | RFIs due today/overdue/submitted; pack builder; submission log; daily digest |
| SCR-LIT-15 | Observations & MAP | Legal › Regulators › {engagement} › Observations | Observation cards with action plans, evidence, verification status (P10) |
| SCR-LIT-16 | Regulator Proceedings | Legal › Regulators › Proceedings | SCNs, adjudication, compounding, penalties, appeals with clocks |
| SCR-LIT-17 | Contracts Repository | Legal › Contracts | Grid with type, counterparty, value, expiry, auto-renew risk, outsourcing/RPT/DPDP flags |
| SCR-LIT-18 | Contract Workspace | Legal › Contracts › {contract} | Stages; versions and redlines; approval route; signature; obligations (confirm grid); renewals |
| SCR-LIT-19 | Contract Intake (self-service) | My Work › Request a contract | Type-specific form; attachments; routing preview |
| SCR-LIT-20 | Licences Register | Legal › Licences | By entity and location; expiry heat strip; renewal tasks; conditions |
| SCR-LIT-21 | Ethics Declarations | Legal › Ethics | Campaigns; completion; conflicts review queue; gifts register |
| SCR-LIT-22 | My Declarations | My Work › Declarations | Pending declarations; gift pre-clearance request; history |
| SCR-LIT-23 | Delegation Matrix | Legal › Settings › Delegations | Matrix editor (Governed); preview who approves what; effective dates |
| SCR-LIT-24 | Legal Reports | Legal › Reports | LIT/REG/CLM/LIC/ETH report definitions (rendered by P28) |

Empty states: "No matters yet — import your existing register (Excel) or add a matter; we will build the docket from your orders." Error states name the rule and the fix ("Approval exceeds your delegation (₹1–10 crore requires GC + CFO). Route to CFO?").

---

## 7. Backend design

### 7.1 Modules touched

`lit` (owner — schema `lit`), `dms`/`pol` (vault, privilege, redline, eSign, templates), `wf` (tasks, approvals, calendar, Work Inbox), `cmp` (issues, checkpoints from contract obligations and licence conditions), `gov` (Reg 30 cases, penalties register, recusal), `aud` (closure-verification tests, inspection room), `acc` (provision schedule feed), `tpr` (outsourcing contracts), `hr` (declarants, HR-triggered notices), `int` (Ecosystem events, e-mail-in, counsel portal identity, LawDocs templates, e-Courts adapter flag OFF), `ai` (VA-16), `rpt` (report definitions, P28), `xpt` (export). Shared packages per master OP-1; this phase builds no parallel workflow, notification, calendar, document or export implementation.

### 7.2 Tables (schema `lit`; all with `tenant_id`, `legal_entity_id`, RLS, bitemporal columns, ledger pointer)

| Table | Key columns |
|---|---|
| `lit.notice_types` (rule pack) | code, statute, section, authority, window_rule jsonb, default_severity, default_owner_role, approvals, template_id, escalation jsonb, status (VERIFIED/UNVERIFIED), version |
| `lit.notices` | id, direction, type_code, sender, addressee_entity_id, reference_no, notice_date, received_at (earliest), channel, amount jsonb, severity, owner_id, matter_id, stage, reply_due_on, dispatched_at, proof_document_id, language, original_document_id |
| `lit.matters` | id, cause_title, matter_type, forum_id, bench, jurisdiction, case_numbers jsonb (CNR, diary, case no.), party_role, opposing_parties jsonb, claim jsonb, relief, stage, status, next_date, team jsonb, privilege_default, confidentiality_class, risk_score, provision_class, reg30_flag, owner_system (LDC/FX), source_ref |
| `lit.docket_entries` (append-only) | matter_id, seq, at, entry_type, title, document_version_id, actor_id, stage, deadline_id, privilege, corrects_entry_id |
| `lit.hearings` | matter_id, date, bench, item_no, purpose, appearance, outcome, next_date, recorded_by, recorded_at |
| `lit.orders` / `lit.order_directions` | order: matter_id, date, type, outcome, quantum jsonb, costs, appealable, appeal_clock_id, document_version_id, confirmed_by; direction: text, owner_id, due_on, task_id, status |
| `lit.clocks` | subject_type, subject_id, rule_code, rule_version, start_at, due_on, buffer_days, owner_id, status, verified |
| `lit.forums` | code, name, type, state, city, holiday_calendar_id |
| `lit.counsel_firms` / `lit.counsel_people` / `lit.engagements` | firm: name, enrolment refs, practice areas, rate_card jsonb, gst jsonb, status; engagement: matter_id, firm_id, letter_document_id, fee_basis, budget jsonb, conflict_check jsonb |
| `lit.invoices` / `lit.accruals` | invoice: engagement_id, number, date, amount, gst, tds_section, validation jsonb, approval_ref, ap_export_ref; accrual: period, amount |
| `lit.assessments` | matter_id, quarter, likelihood_class, pct_estimate, best_estimate, range jsonb, timing, reimbursement, rationale, assessor_id, reviewer_id, frozen_at |
| `lit.provision_schedules` | entity, quarter, rows jsonb, snapshot_hash, frozen_at |
| `lit.settlements` | matter_id, offers jsonb (without-prejudice), terms, schedule jsonb, approval_ref, deed_document_id, status |
| `lit.reg_engagements` / `lit.reg_rfis` / `lit.reg_observations` / `lit.reg_map_items` / `lit.reg_submissions` | engagement: regulator, type, reference, reference_date, window, status; rfi: text, due, owner, pack_hash, submitted_at, channel_ref; observation: ref, text, category, severity, direction, response, status, verified_test_id; map item: action, owner, due, evidence; submission: type, approved_ref, submitted_at, ref, hash |
| `lit.reg_proceedings` | regulator, statute_section, notice_id, stage, hearing dates, order_id, penalty jsonb, appeal_matter_id, disclosure_flags |
| `lit.contracts` / `lit.contract_versions` / `lit.contract_obligations` / `lit.contract_approvals` | contract: type, counterparty_ref, owner_dept, stage, value, dates, auto_renew, notice_deadline, law, dispute_clause, stamp jsonb, flags (rpt, outsourcing, dpdp), parent_id; version: document_version_id, redline_document_id; obligation: clause_ref, text, frequency, owner_id, checkpoint_id, state; approval: level, approver, decision |
| `lit.licences` / `lit.licence_conditions` | licence: type, number, authority, entity, location_id, issued_on, valid_to, lead_days, portal, fee jsonb, status, owner_id, documents; condition: text, checkpoint_id |
| `lit.ethics_campaigns` / `lit.ethics_declarations` / `lit.gifts` / `lit.conflicts` | campaign: population, type, deadline; declaration: person_id, type, payload, signed_ref, status; gift: direction, value, counterparty, purpose, date, decision; conflict: person_id, nature, related_party_ref, mitigation, recusal_scope |
| `lit.delegation_matrix` | action, band_from, band_to, approvers jsonb, effective_from, board_ref |
| `lit.risk_models` | version, weights jsonb, status |

### 7.3 APIs (REST, `/api/v1/lit/...`; tenant and legal-entity scope; `Idempotency-Key` on mutations)

`GET|POST /notices` · `POST /notices/{id}:confirm-classification` · `POST /notices/{id}:triage` · `POST /notices/{id}/reply:draft` (async, VA-16) · `POST /notices/{id}:approve` · `POST /notices/{id}:record-dispatch` · `POST /notices/{id}:convert` · `GET|POST /matters` · `GET /matters/{id}/docket` · `POST /matters/{id}/docket` · `POST /matters/{id}/hearings` · `POST /matters/{id}/orders` · `POST /orders/{id}:confirm` · `POST /orders/{id}/directions:create-tasks` · `GET /clocks?due_before=` · `GET|POST /counsel` · `POST /engagements` · `POST /invoices` · `POST /invoices/{id}:approve` · `POST /matters/{id}/assessments` · `POST /provision-schedules/{quarter}:freeze` · `GET|POST /reg-engagements` · `POST /reg-engagements/{id}/rfis` · `POST /rfis/{id}:record-submission` · `POST /reg-engagements/{id}/observations:import` · `POST /observations/{id}:request-verification` · `GET|POST /reg-proceedings` · `GET|POST /contracts` · `POST /contracts/{id}/versions` · `POST /contracts/{id}:submit-approval` · `POST /contracts/{id}/obligations:extract` (async) · `POST /contract-obligations/{id}:confirm` · `GET|POST /licences` · `POST /licences/{id}:record-renewal` · `GET|POST /ethics/campaigns` · `POST /ethics/declarations` · `POST /gifts` · `POST /gifts/{id}:decide` · `GET|PUT /delegation-matrix` (Governed) · `POST /imports/{register}` (preview, commit, undo).

### 7.4 Domain events

Internal (`in.lawdocscomply.lit.*`): `NoticeReceived`, `NoticeTriaged`, `NoticeDispatched`, `MatterOpened`, `MatterStageChanged`, `HearingRecorded`, `OrderConfirmed`, `DirectionDue`, `ClockBreached`, `ProvisionScheduleFrozen`, `RegEngagementOpened`, `ObservationImported`, `ObservationVerified`, `RegulatorPenaltyRecorded`, `ContractExecuted`, `ContractRenewalDue`, `ContractObligationConfirmed`, `LicenceRenewalDue`, `LicenceExpired`, `EthicsDeclarationSubmitted`, `ConflictMitigationDecided`, `GiftDecided`.
Consumed from the ecosystem (published by Finbyx RS / Udolex; Ecosystem Spec §6.8, §6.10, X-01): `in.infrabyx.recovery.RecoveryCaseOpened.v1`, `…RecoveryCaseClosed.v1`, `in.infrabyx.litigation.LitigationCaseOpened.v1`, `…LitigationCaseUpdated.v1`, `…HearingScheduled.v1`, `…OrderRecorded.v1`, `…LitigationCaseClosed.v1`.
Proposed for publication to the ecosystem (Ecosystem Spec v1.2 change request): `LegalMatterExposureSummarised` (aggregates for group risk) and `RegulatorObservationOpened/Closed` (for Finbyx/Udofin tenants whose operational systems must act) — not published until approved.

### 7.5 Jobs and Temporal workflows

`NoticeLifecycleWorkflow` (timers per clock; escalations), `HearingDigestJob` (daily), `MissingOutcomeChaser` (24 h after hearing), `LimitationWatcher` (hourly recompute on calendar changes), `ProvisionQuarterWorkflow` (assessment tasks at quarter-end −10 days; freeze), `RegEngagementWorkflow` (RFI due timers; daily digest during on-site window), `ObservationClosureWorkflow` (calls P10 verification), `ContractRenewalJob` (daily), `LicenceRenewalJob` (daily), `EthicsCampaignWorkflow`, `EcosystemRecoveryProjector` (consumer, idempotent inbox), `ECourtsSyncJob` (flag OFF).

---

## 8. Integrations (ports and adapters; Appendix L)

| Port | Use | Notes |
|---|---|---|
| `ECOSYSTEM_PORT` | Recovery and litigation events from Finbyx RS/Udolex; Equator referral (explicit choice only) | Read-only projection (NN-23) |
| `MESSAGING_PORT` | E-mail-in for notices and counsel invoices; outbound e-mail dispatch evidence | Dispatch by user action only |
| `ESIGN_PORT` | Contracts, engagement letters, settlement deeds, declarations | ASP adapters to CCA ESPs (X-04); First Schedule exclusions |
| `TEMPLATE_PORT` (LawDocs) | Contract and notice templates, clause library | Versioned; tenant overrides |
| `COURT_DATA_PORT` | Licensed e-Courts/NJDG case status and cause lists | Flag OFF; no scraping (OI-P26-04) |
| `ACCOUNTING_PORT` | Approved counsel invoices to AP; provision schedule to P11 | Export files/API |
| `CALENDAR_PORT` | Hearings, deadlines, renewals in personal calendars | LDC dates authoritative (NN-07) |
| `COMPANY_DATA_PORT` | Counterparty master data (CIN, status) for contracts | Licensed providers only |

---

## 9. Settings and configuration (registered in P02; tiers per NN-28)

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `lit.notice.types` | G | platform rule pack | tenants add types (T); cannot loosen statutory windows | Platform content / GC |
| `lit.notice.internal_target_days_before_due` | T | 3 | 1–10 | GC |
| `lit.notice.reminder_offsets_days` | T | [7, 3, 1] | — | GC |
| `lit.triage.sla_business_days` | T | 1 | 1–3 | GC |
| `lit.approval.matrix` | G | baseline Table 17-1 | Board reference where Board-delegated | GC + CFO |
| `lit.privilege.downgrade_approver` | L | GC | — | — |
| `lit.hearings.digest_time` | T | 07:30 local | — | GC |
| `lit.hearings.lookahead_days` | T | 7 | 1–30 | GC |
| `lit.hearings.outcome_due_hours` | T | 24 | 4–72 | GC |
| `lit.limitation.reminder_offsets_days` | T | [30, 15, 7, 3, 1] | — | GC |
| `lit.limitation.rules` | G | rule pack | — | Platform content |
| `lit.assessment.frequency` | T | quarterly | quarterly/half-yearly | CFO |
| `lit.assessment.pct_guidance_bands` | T | OFF | guidance only; never drives class (§J.16) | CFO |
| `lit.risk.weights` | T | platform default | sum = 1 | GC |
| `lit.reg30.materiality_rule` | G | per Board policy | ≤ Reg 30(4) lower-of test | CS + GC |
| `lit.reg.rfi_reminder_offsets_hours` | T | [24, 4] | — | CCO |
| `lit.reg.closure_requires_verification` | L | true | — | — |
| `lit.contracts.renewal_alert_days` | T | [90, 60, 30] | — | Legal |
| `lit.contracts.legal_review_threshold` | T | ₹10,00,000 or non-standard clause | — | GC |
| `lit.contracts.obligation_extraction` | T | ON | review required | GC |
| `lit.licences.default_lead_days` | T | 60 | 15–180 | CS |
| `lit.ethics.gift_preclear_value` | T | ₹5,000 | ≥ 0 | CCO |
| `lit.ethics.gift_annual_aggregate_limit` | T | ₹25,000 per counterparty | ≥ 0 | CCO |
| `lit.ethics.campaign_month` | T | April | — | CS |
| `lit.ecourts.enabled` | T | OFF | requires licensed adapter | Admin |
| `lit.recovery_lite.enabled` | G | OFF | counsel opinion reference required | Platform + GC |
| `lit.ai.va16.autonomy_ceiling` | T | L1 | L0–L1 | GC (NN-50) |
| `lit.import.undo_hours` | T | 24 | 1–72 | GC (NN-49) |

---

## 10. Security, privacy and audit

- **Privilege and confidentiality**: privileged documents and internal notes use the `BOARD_CONFIDENTIAL`-equivalent key separation in a dedicated `LEGAL_PRIVILEGED` data class (proposed addition to the data-class list; crossfile to Appendix Q); excluded from analytics, AI training, auditor/regulator grants and cross-product events (NN-13).
- **Regulator records**: regulator engagements and proceedings use the sealed `REGULATOR_CONFIDENTIAL` class; observations shared with the Board are summaries unless the Board pack includes the full text by CCO decision.
- **Matter-scoped access**: ABAC by matter team; counsel portal users see only assigned matters; every view/download of a privileged document is logged and visible to the GC.
- **Personal data**: notices and matters often contain personal data of employees, customers or opposing parties — purpose-limited, retention per class, rights requests handled through P12 with legal-hold override (litigation hold suspends deletion; NN-29).
- **Legal hold**: opening a matter can place holds on related documents, mailboxes (via P18 suite connector where available) and records; holds block disposal (P07 §4Q).
- **Ethics data**: declarations are personal; gifts and conflicts visible to compliance and the declarant's line manager only; aggregated in reports.
- **Audit**: every classification confirmation, triage, approval, dispatch, assessment, freeze, privilege change, grant and import is a ledger event (NN-02); docket and submission logs are append-only (NN-36 pattern).

---

## 11. AI touchpoints and guardrails

| Touchpoint | What VA-16 does | Guardrail |
|---|---|---|
| Notice classification | Proposes type, statute, dates, window, severity | User confirms each field; severity never auto-set (NN-47) |
| Reply/notice drafting | Drafts from template and facts with citations | Legal review mandatory; dispatch is a human action (NN-14) |
| Order digest | Outcome, directions, appeal period proposals | Confirmation step; clocks computed by engine, not AI |
| Matter summary/chronology | Summary from docket and documents | Privileged context L0 unless GC enables per matter |
| Contract obligations | Extracts obligations with clause references | Owner confirms each; becomes tenant checkpoint only after approval (NN-04) |
| RFI pack | Proposes records to include and readiness score | CCO reviews; submission by user (NN-08) |
| Likelihood rationale | Drafts reasoning | Class and amounts are human (NN-47); no AI figures in schedules (NN-37) |
| Ethics matching | Flags potential undeclared conflicts | Compliance-only, advisory (NN-47) |

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p26/*.feature`)

```gherkin
Feature: Notice handling
  Scenario: GST DRC-01 is classified, owned and replied on time
    Given a PDF notice arrives by e-mail-in on 3 Nov 2026 at 10:15 for entity "Alpha Finance Ltd"
    When VA-16 proposes type "GST DRC-01" with reply window 30 days
    And the legal user confirms the classification and assigns owner "Tax Manager"
    Then the reply due date is computed from the notice master rule and shown with its rule version
    And reminders are scheduled at 7, 3 and 1 days before the due date

  Scenario: Reply cannot be dispatched without approval
    Given a reply of value ₹2 crore exposure is drafted
    When the legal user tries to record dispatch
    Then the action is blocked with "Approval required: GC + CFO (₹1–10 crore)"

  Scenario: Statutory clock does not pause while awaiting documents
    Given notice N-12 is in UNDER_INVESTIGATION waiting for branch documents
    Then the reply due date remains unchanged (NN-33)

Feature: Orders become actions
  Scenario: Directions create tasks in one step
    Given an order dated 10 Dec 2026 directs "Deposit ₹5,00,000 within 4 weeks" and "File compliance affidavit by 15 Jan 2027"
    When the legal user confirms the AI-proposed directions
    Then two tasks are created with owners and due dates
    And the appeal limitation clock is created from the order date per the rule pack

Feature: Provision schedule
  Scenario: Likelihood class drives treatment, not percentage bands
    Given matter M-4 is assessed POSSIBLE with a 60% guidance estimate
    When the quarter's schedule is produced
    Then M-4 appears in contingent liabilities, not in provisions
    And the schedule is frozen at quarter close with a snapshot hash

Feature: Regulator engagement
  Scenario: Observation closure needs verification
    Given RBI observation O-7 has all MAP items complete
    When the CCO selects "Report closed"
    Then a P10 closure-verification test is requested
    And the observation stays COMPLIED_PENDING_VERIFICATION until the test passes

Feature: Recovery boundary
  Scenario: Finbyx recovery case appears read-only
    Given the tenant is linked to Finbyx in LDC_EXTERNAL mode
    When the event RecoveryCaseOpened arrives for borrower case R-991
    Then a projection matter tagged owner_system FX appears in the register
    And no edit action other than internal notes is available

  Scenario: Recovery notices are blocked without the lite pack
    Given lit.recovery_lite.enabled is OFF
    When a user tries to create an outgoing SARFAESI 13(2) notice
    Then the action is refused with "Recovery notices are issued from the Finbyx Recovery Suite (D-41)"

Feature: Contracts and licences
  Scenario: Auto-renew risk alert
    Given a vendor contract expires on 31 Mar 2027, auto-renews for 1 year, notice period 60 days
    Then the notice deadline is 30 Jan 2027
    And renewal decision tasks are created 90, 60 and 30 days before the notice deadline

  Scenario: Expired licence raises a critical issue
    Given the Shops & Establishments registration for branch "Jaipur-2" expires on 30 Nov 2026 with no renewal filed
    When the date passes
    Then the licence status becomes EXPIRED
    And a Critical compliance issue is opened and shown on the CEO dashboard

Feature: Ethics
  Scenario: Gift above threshold needs pre-clearance
    Given the pre-clearance value is ₹5,000
    When an employee declares a received gift worth ₹12,000 from vendor "V-22"
    Then the gift is PENDING_PRECLEARANCE with the line manager and compliance
    And the vendor's contract approval chain shows the declarant as conflicted

Feature: Counsel portal isolation
  Scenario: Counsel sees only assigned matters
    Given firm "Rao & Co" is assigned to matter M-4 only
    When a Rao & Co user searches for matter M-5
    Then no result is returned and the attempt is logged
```

NN tests: `NN-01_counsel_portal_matter_scope`, `NN-02_docket_append_only`, `NN-05_reply_maker_not_approver`, `NN-08_no_auto_dispatch_or_filing`, `NN-13_privileged_excluded_from_grants_and_ai`, `NN-14_va16_cannot_dispatch`, `NN-22_provision_schedule_reproducible`, `NN-33_notice_clock_never_pauses`, `NN-37_no_ai_figures_in_schedule`, `NN-38_unverified_limitation_advisory`, `NN-39_no_recovery_recompute`, `NN-47_ai_never_sets_severity_or_class`, `NN-49_register_import_undo`, `NN-50_va16_ceiling`.

---

## 13. Deliverables and exit gate

**Deliverables:** `lit` module with migrations; seeded rule packs (notice master ≈ 70 types, limitation and appeal periods, forums list with holiday calendars for the Supreme Court, High Courts and major tribunals, delegation-matrix defaults, licence types and renewal rules, contract-type checklists for RBI outsourcing/LSP/co-lending/DSA); templates (acknowledgement, reply skeletons, engagement letter, settlement deed, NDA, declaration forms); counsel portal; Ecosystem projector; report definitions for P28; export mapping to LDC-EXPORT-1.0; user guides (GC, legal user, counsel portal, licences, ethics).

**Exit gate:**
1. All Gherkin scenarios and NN tests green.
2. Pilot tenant: 50 legacy matters imported with docket back-fill; 20 notices processed end to end with reply-on-time 100%; one order converted to tasks; one quarter's provision schedule frozen and exported to P11.
3. Regulator engagement run on a synthetic RBI inspection: 30 RFIs, 12 observations, MAP items, closure verification through P10.
4. 100 contracts imported with renewal alerts; obligation extraction accepted for 10 contracts; licences register for 5 locations with renewal tasks.
5. Ethics campaign completed for 50 synthetic employees with one conflict driving a P06 recusal.
6. Finbyx projection verified with recorded Ecosystem fixtures; recovery-notice block verified.
7. WCAG 2.2 AA audit of Notice Inbox, Matter Workspace, Counsel Portal and My Declarations (NN-21).
8. All [VERIFY] notice windows and limitation periods for features enabled at go-live verified or advisory-only.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P26-01 | Reply windows for each notice-master type (baseline Table 9-1) | Statute-by-statute check | Legal analyst | Unverified types advisory only (NN-38) |
| OI-P26-02 | Limitation and appeal periods per forum, exclusions for certified copies | Rule pack | Legal analyst | Advisory clocks with "verify" badge |
| OI-P26-03 | "Recovery Notices Lite" for lenders without Finbyx — scope and legality | Counsel opinion | General Counsel | Flag OFF |
| OI-P26-04 | Lawful source for e-Courts/NJDG case status and cause lists | Licensing | CTO | Manual hearing capture |
| OI-P26-05 | Reg 30 timeline and materiality for litigation after latest LODR amendments | SEBI amendments | Listed-company analyst | 24-hour advisory clock |
| OI-P26-06 | GST reverse charge and TDS section on legal fees under the Income-tax Act 2025 | Tax | Tax analyst | Fields captured; validation advisory |
| OI-P26-07 | Bar Council rules on fee arrangements recorded in counsel engagements (contingency prohibition) | Professional rules | General Counsel | Contingency fee type disabled |
| OI-P26-08 | Retention floors for legal document classes | Rule pack | CCO + GC | Conservative 10 years / permanent |
| OI-P26-09 | Regulator compliance-submission timelines per regulator (RBI inspection, SEBI, IRDAI, IFSCA, Registrar) | Varies by letter | CCO | Due date taken from the letter |
| OI-P26-10 | Ecosystem Spec v1.2 change request for `LegalMatterExposureSummarised` and `RegulatorObservationOpened/Closed` | Contract change | Integration lead | Not published |
| OI-P26-11 | VA-16 Legal Matters Assistant addition to Appendix AA/K with eval sets (notice classification, order digest) | Cross-file | AI lead | Drafting skills off until evaluated |
| OI-P26-12 | `LEGAL_PRIVILEGED` data class addition to Appendix Q / Ecosystem data classes | Cross-file | Security lead | Treat as BOARD_CONFIDENTIAL |
| OI-P26-13 | Export folder number for legal matters in Appendix M — **closed (v1.1, X1):** folder `26 Legal Matters, Contracts and Licences` per Appendix M §M.3 | Closed | P19 owner | — |

---

## 15. Sources (accessed 25 October 2026)

1. Owner's baseline: LawDocs Comply Architecture Part 3 — "Legal Notices and Litigation and Debt Recovery Module" (§§ on notice categories, proceedings captured, litigation lifecycle Table 7-1, risk score, authority and delegation matrix Table 17-1, Ind AS 37 Table 23-1, Reg 30, RBI inspection register, settlement/OTS/ADR) and "Litigation & Legal Matter Management" (record and form specifications).
2. Limitation Act, 1963 (Schedule); Code of Civil Procedure, 1908; Bharatiya Nagarik Suraksha Sanhita, 2023 — https://www.indiacode.nic.in
3. Arbitration and Conciliation Act, 1996 ss.9, 17, 21, 34, 37; Commercial Courts Act, 2015 s.12A — https://www.indiacode.nic.in
4. Ind AS 37 Provisions, Contingent Liabilities and Contingent Assets (Companies (Indian Accounting Standards) Rules, 2015); AS 29 (Companies (Accounting Standards) Rules, 2021) — https://www.mca.gov.in
5. SEBI (LODR) Regulations, 2015 — Reg 30 and Schedule III — https://www.sebi.gov.in
6. Companies Act, 2013 ss.177(9)–(10) (vigil mechanism), 184, 188, 454 — https://www.mca.gov.in
7. RBI Act, 1934 ss.45L, 45M, 58B, 58G; Banking Regulation Act, 1949 ss.35A, 47A — https://www.rbi.org.in
8. RBI outsourcing directions in the 28 Nov 2025 consolidated set (NBFC: RBI/DOR/2025-26/363) — contract checklist source (Appendix AB catalogue).
9. Appendix Z (G2: TeamLease litigation module; Lexplosion Komlit; inspection trackers) and Appendix AC (G5 gap A).
10. Infrabyx Ecosystem Integration Specification v1.1 §6.8 (recovery), §6.10 (litigation).


---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**Added in v1.1:** NN-48; D-41; X-48, X-55.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
