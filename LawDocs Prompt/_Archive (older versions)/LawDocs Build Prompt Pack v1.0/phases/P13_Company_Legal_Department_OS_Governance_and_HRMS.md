# Phase P13 — Company Legal Department OS, Governance and HRMS

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (identity, KYB, director/KMP identity attributes), P02 (organisations, legal entities, departments, positions, user types, maker-checker, delegations), P03 (Configuration Studio, settings registry, `RULES_PORT`), P04 (Legal Vault, retention, legal hold), P06 (templates: resolutions, notices, minutes skeletons, appointment letters, policies), P07 (CLM approvals, obligations, renewal dates), P08 (eSign/DSC for minutes, registers, declarations, appointment letters), P09 (Vidhi runtime and agents), P11 (matters, clocks, spend, counsel panel; frozen `lit` read API), P12 (IP calendar), P16 (marketplace professionals and retainers), P17 (plans and entitlements), P18 (Delivery Console; RM as maker), P19 (LawDocsComply connectors, workplace and company-data adapters), P20 (export), P22 (mobile). Shared kernels (used, never forked — NN-47): `@infrabyx/governance-kernel`, `@infrabyx/hrms-kernel`, `infrabyx-labour-rulepack`, `@infrabyx/docgen`, `@infrabyx/redline`. External: LawDocsComply (when the tenant uses it), licensed MCA-data vendors, Microsoft 365 / Google Workspace, e-voting agencies (file hand-off).
> **Sequencing:** Wave 2, after P11 sprint 2. Track A (`lgo`, sprints 1–3): intake desk, SLAs, CLO dashboard, legal calendar, DoA matrix. Track B (`gov` mount, sprints 2–6): mode resolver, company-type configuration, board and committees, meetings, minutes, resolutions, registers, directors and KMP, duties. Track C (`hr` mount, sprints 5–8): people, positions, departments, leave, payroll via the labour rule pack, documents, acknowledgements, POSH. Sprints 9–10: finance-company templates (Appendix T), agents, LDC SoR sync certification, mobile, hardening. Freeze the kernel versions at sprint 2 and record them in `docs/kernels.lock`.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), D (roles), H (agent roster), K (export), R (settings), T (legal-department operating model and finance-company structure — companion to this phase), W (open items), X (Operations Hub addendum — boundary for staff HR), Y (Ecosystem Spec change requests).
> **Requirements covered:** R-002, R-018, R-019, R-021, R-026, R-027, R-028, R-030, R-047, R-053, R-055, R-059, R-060, R-064, R-067, R-068.
> **Decisions applied:** D-02, D-10, D-15, D-17 · **Challenges applied:** CH-14, CH-24, CH-26, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-09, NN-11, NN-13, NN-14, NN-17, NN-18, NN-19, NN-24, NN-26, NN-28, NN-29, NN-30, NN-32, NN-33, NN-38, NN-12, NN-40, NN-43, NN-45, NN-47
> **Estimated effort:** 10 two-week sprints, squad of 8 (backend 4, frontend 2, QA 1, integration 1) plus a part-time Company Secretary (secretarial domain), an HR/labour analyst and a counsel reviewer for the operating model.

---

## 1. Objective and business outcome

The owner wants companies to run their legal work "with one CLO" (brief l.68) and to manage people, KMPs, directors, duties and departmental structures, including finance-company structures aligned with the Companies Act 2013 and RBI directions (brief l.67). This phase delivers the **Company Legal Department OS**:

1. **Legal team in a box** — positioned per D-17 and CH-14 as **legal operations + AI + on-demand professionals**. LawDocs gives the company the operating system of a legal department (intake, triage, SLAs, calendar, records, drafting, spend, dashboards). Advice and representation come from advocates engaged in their own name (Advocates Act 1961 ss.29, 33; R3 LG-110). A company with one CLO, or a CS or compliance head acting as legal lead, can run its legal function on LawDocs; it still needs advocates for court work and opinions, and the product says so.
2. **Governance kernel mount** — board, committees, meetings, minutes, resolutions, registers, directors and KMP, duties — mounted locally for LawDocs-only companies and served from LawDocsComply (system of record) when the company also uses LDC (D-10, NN-47).
3. **HRMS kernel mount for client companies** — people, positions, KMP designations, departments, duties, leave, payroll through the shared labour rule pack, onboarding and exit documents, policy acknowledgements, POSH Internal Committee records — again local or LDC-served.
4. **Departmental structure templates**, including the customisable finance-company (NBFC) structure in Appendix T.

| Outcome | KPI / exit-gate measure |
|---|---|
| Every legal request has an owner and a clock | 100% of intake requests triaged within the category SLA in pilot; first-response SLA met ≥ 95% |
| Self-service where safe | ≥ 30% of standard requests (e.g., NDA on the company template) closed by guided self-service with no lawyer time, within guardrails |
| One legal calendar | Contracts, cases, trademarks, licences, board and HR statutory dates in one calendar; 0 missed statutory dates in UAT |
| Board work faster | Notice + agenda + pack issued in ≤ 6 steps; minutes draft circulated within 3 working days of the meeting in pilot; 0 edits to sealed minutes (SS-1 bar on altering entered minutes [VERIFY para]; tampering is an offence under s.118(12)) |
| No double entry with LDC | When LDC is SoR, 0 governance or HR rows written locally; governance and HR work happens in LDC; LawDocs reads governance facts on demand; switch reconciliation 100% |
| Structure in minutes | A new NBFC tenant adopts the Appendix T template (departments, committees, KMP, three lines of defence) in ≤ 15 minutes and customises it without Super Admin (NN-29) |
| Proportionate HR | Attendance and work measurement disclosed and outcome-based; 0 surveillance features (NN-33) |

## 2. Scope (in / out)

**In scope**
- Operating-model setup wizard (company type, size, sector → Appendix T template).
- Legal intake desk for all departments; categories, dynamic forms, triage, routing, SLAs, self-service, conversions, satisfaction.
- CLO dashboard, legal calendar, legal risk dashboard for KMPs and the board.
- Licences and registrations register (light; LDC owns it when present).
- Legal spend view across matters, retainers and marketplace orders; counsel panel (from P11).
- Delegation-of-authority (DoA) matrix for legal actions.
- Governance kernel mount: company-type configuration, board and committees, meetings (notice, agenda, papers, attendance incl. video, quorum, minutes per SS-1/SS-2, resolutions incl. circular resolutions, action items), statutory registers, directors/KMP profiles (DIN, KYC status, interests under s.184, disclosures), duties and task assignment.
- Finance-company (NBFC) governance overlay through the shared kernel rule pack, aligned with the RBI consolidated Directions of 28 November 2025 (verified titles only).
- HRMS kernel mount: people, employments, positions, KMP designation, department allocation, duties, leave, attendance (proportionate), payroll via `infrabyx-labour-rulepack`, onboarding and exit documents, policy acknowledgements, POSH IC records (sealed).
- LDC system-of-record synchronisation through contracts.
- Board/KMP AI agent hooks (from P09).
- Retainer delivery with the LawDocs RM as delegated maker (R-064).

**Out of scope (owner)**
- Infrabyx's own staff HRMS, payroll, appraisal and staff CRM — Operations Hub (D-02; Appendix X).
- Compliance management, regulatory returns, RBI/SEBI checkpoint libraries, inspections — LawDocsComply (D-10). LawDocs shows LDC tasks in the legal calendar when linked.
- ROC/MCA e-filing, e-voting execution, filing of labour returns — done by the company or its professional on the official portals (NN-05, NN-13). LawDocs prepares data sheets and records filings.
- Listed-company disclosure engine (LODR Reg 30 workflows, PIT, SAST) in depth — LDC; LawDocs-only listed companies get a basic disclosure case and are advised to use LDC [REC].
- Litigation, IP, CLM detail — P11, P12, P07.
- Payment of salaries — the company's bank; LawDocs exports bank files and never holds funds (NN-22).

## 3. Personas and permissions touched

| Role code | What they can do in P13 |
|---|---|
| `ORG_OWNER`, `ORG_ADMIN` | Run the setup wizard; choose governance/HR mode; manage departments, positions, users; approve critical configuration with a checker |
| `ORG_CLO` | Owns the intake desk, categories, SLAs, routing, DoA for legal actions; CLO dashboard; legal calendar; spend |
| `ORG_LEGAL_MAKER` | Works requests; drafts; converts requests into contracts, notices, matters, TM tasks, board items |
| `ORG_CHECKER`, `ORG_APPROVER` | Check and approve per DoA (maker ≠ checker, NN-18) |
| `ORG_DEPT_HEAD` | Raises and tracks department requests; assigns duties within the department; approves leave; sees department dashboards |
| `ORG_MEMBER` | Raises legal requests; uses self-service; acknowledges policies; HR self-service |
| `ORG_KMP` (CS) | Governance owner: meetings, minutes, resolutions, registers, director declarations; (CFO) spend and exposure; (MD/CEO) approvals, dashboards |
| `ORG_DIRECTOR` | Board portal: papers, annotations (private), questions, circular resolution votes, declarations, minutes comments, eSign |
| `ORG_BOARD_OBSERVER` | Read papers granted for specific meetings; no vote |
| `ORG_AUDITOR_RO` | Time-boxed read of registers, minutes and reports (secretarial/internal auditor) |
| `ORG_EXT_COUNSEL` | Assigned requests or matters only |
| `ORG_DELEGATED_MAKER` / `OPS_RM` / `OPS_PROFESSIONAL` | Under a delivery grant (NN-17): maker for requests, drafts, agendas, minutes skeletons, register entries, HR documents; never checker, approver or signatory |
| `ORG_HR_ADMIN` | HR administration and HR maker work in `local_kernel` mode: people, positions, duties, leave rules, attendance methods, onboarding/exit documents, policy acknowledgements; never sees sealed POSH content |
| `ORG_PAYROLL_MAKER` | Prepares pay-run inputs, locks inputs, computes with the pinned labour pack |
| `ORG_PAYROLL_CHECKER` | Reviews and approves pay runs and bank files; must differ from the maker (NN-18; `hr.payroll.checker_required` LOCKED) |
| `ORG_POSH_IC_PRESIDING` | Presiding Officer of an Internal Committee (POSH Act 2013 s.4(2)(a)): sealed POSH cases of that IC, clocks, reports, annual report; enables scoped AI assistance |
| `ORG_POSH_IC_MEMBER` | Member of that IC: sealed cases of that IC only |
| `AGT_BOARD_SECRETARY`, `AGT_RESOLUTION_DRAFTER`, `AGT_MINUTES_DRAFTER`, `AGT_ACTION_ITEM_TRACKER`, `AGT_BOARD_PACK_SUMMARISER`, `AGT_COMPLIANCE_CALENDAR`, `AGT_LEGAL_INTAKE_DESK`, `AGT_CLO_CHIEF_OF_STAFF`, `AGT_KMP_BRIEFER` (Appendix H #13–18, #27–29) | Makers only (NN-43): propose triage, drafts, agendas, minutes, task lists, reminders and briefs; never vote, sign, approve, seal, file or send externally |

## 4. Functional requirements

### 4A. Operating model and setup

**FR-P13-01 — Positioning in product.** The Company workspace "Legal Department" home carries a persistent, plain statement (content key `hlp.lgo.operating_model`): "LawDocs runs your legal operations — requests, contracts, cases, trademarks, board work and records — with Vidhi AI. Legal advice and court work are given by advocates you engage. You can hire one through LawDocs." Marketing copy must not say "replace your lawyers" or "no lawyer needed" (NN-20; CH-14).

**FR-P13-02 — Setup wizard (≤ 15 minutes).** Steps: (1) company profile from KYB (P01) — constitution, listing status, sector, size bands (paid-up capital, turnover, borrowings, employees — inputs to kernel thresholds); (2) regulated status (NBFC with layer and category; HFC; other RE; none); (3) choose operating template from Appendix T (startup, private company, OPC, public unlisted, listed, LLP, Section 8, NBFC-BL/ML/UL, HFC, other finance company); (4) preview: departments, positions, committees, KMP and functionaries, intake categories with SLAs, DoA defaults, legal calendar seeds; (5) edit inline or accept; (6) choose governance and HR mode (FR-P13-22); (7) invite CLO, CS, department heads. Adoption is one transaction with audit; re-running the wizard creates a diff, never overwrites tenant edits silently.

**FR-P13-03 — Operating model artefacts.** The tenant gets a generated, editable **Legal Department Charter** (DOCX via `docgen`): scope, roles (CLO, legal makers, approvers, panel counsel, Vidhi agents with autonomy ceilings, LawDocs RM if retained), intake rules, SLAs, DoA, escalation, confidentiality and privilege rules, reporting to the board — from the Appendix T model. Board approval of the charter can be routed as an agenda item.

### 4B. Legal intake desk

**FR-P13-04 — Channels.** (a) "Request legal help" button on every Company workspace page and in the mobile app (≤ 3 clicks to submit); (b) intake e-mail address per entity (`int` mailbox), with sender matched to a user; (c) Microsoft Teams / Google Chat message extension through `WORKSPACE_PORT` [VERIFY app-store requirements] (R-053, R-055); (d) API for the tenant's own systems (P19). Every request (`lrq_`, new prefix; business ID `LD-LRQ-YYYY-NNNNNN`) records channel, requester, department, entity, timestamps and attachments (originals hashed, NN-09).

**FR-P13-05 — Categories and dynamic forms.** Categories come from Appendix T §T.3 (e.g., new contract — standard template; contract review — third-party paper; NDA; vendor onboarding legal check; notice received; dispute or threatened claim; employment/HR legal query; policy drafting or review; board or shareholder matter; regulatory query; IP/brand clearance; data protection query; licence or registration; litigation update request; general legal question). Each category has: form (questionnaire from `tpl`, conditional fields), required attachments, default priority rule, SLA policy, routing rule, self-service path (if any), conversion target, approval requirements and "i" help. Tenants add, rename, retire and reorder categories (TENANT tier, NN-29).

**FR-P13-06 — Triage.** On submission, `AGT_LEGAL_INTAKE_DESK` proposes category (if the requester chose "Not sure"), priority (P1–P4 per Appendix T §T.4 matrix: value, deadline, regulator involvement, reputational risk, litigation risk), related records (counterparty agreements, matters), and the routing target. Rules decide; the agent only proposes. P1 requests and any request mentioning a statutory deadline, a regulator, police, court summons or data breach are routed to a human triager immediately, never auto-closed. Triage by a human takes ≤ 2 clicks (accept proposal / change and accept).

**FR-P13-07 — Routing.** Deterministic rules (GoRules decision table, `lgo.routing.table`): by category, department, entity, value band, counterparty type, language and workload caps → individual, team queue, panel counsel (P11), marketplace SKU (P16), LawDocs delivery team under a retainer (P18) or LDC (compliance questions when linked). Round-robin and skills-based options; out-of-office respected from the HR kernel leave calendar.

**FR-P13-08 — SLA engine.** SLA policies per category and priority: first response, resolution target, business calendar (entity holidays from HR kernel), pause conditions (only "waiting on requester" or "waiting on counterparty" with a reason; **statutory and court clocks never pause** — they are P11 clocks linked to the request), breach escalation ladder (assignee → team lead → CLO), SLA status chip (on track, at risk at 75%, breached). Defaults in Appendix T §T.3.

**FR-P13-09 — Self-service with guardrails.** For low-risk categories the requester can complete the task alone: generate an NDA or standard contract from the approved template with only permitted variables (P06 template automation — not AI advice), within value and counterparty limits (`lgo.selfservice.limits`); answers from the approved knowledge base and policies with citations; checklist-driven vendor onboarding. Anything outside the guardrails (edited clause, value above limit, high-risk counterparty) converts to a legal review request automatically. Self-service outputs are logged as requests with outcome SELF_SERVED.

**FR-P13-10 — Conversion.** One click converts a request into: contract intake (P07), outgoing notice or reply (P10), matter (P11), trademark clearance or filing (P12), board/committee agenda item (gov), HR case or document (hr), compliance query (LDC via `int` when linked), marketplace order (P16). The request stays as the parent with SLA history; status mirrors the child until closure.

**FR-P13-11 — Requester experience.** Requesters see "My requests" with plain status, who is working on it, what is needed from them, expected date; they can add information, upload, chat with the assignee and rate the outcome (1–5 with optional comment; internal only). Notifications per FR-P11-59/60 channel rules.

**FR-P13-12 — Waiting items and handovers.** Open, interim and waiting-for-others items (`itm_`) are tenant-configurable (R-047): e.g., "Waiting for business approval", "Waiting for counterparty draft", "Waiting for stamp paper", "Waiting for board". Each has an owner and ageing; handovers on leave or exit are proposed from the HR kernel (FR-P13-56). Items are created, chased, escalated and resolved only in the P03 items engine (`wf.items`, Appendix A §A.15); P13 configures item types for legal requests and reads them through the `lgo.waiting_items` view (X-09) — it never writes a separate waiting-item record.

### 4C. CLO dashboard, legal calendar and legal risk dashboard

**FR-P13-13 — Legal calendar (one view).** Sources (read through APIs, never copied): contract renewals, notice deadlines and obligations (P07); hearings, limitation and order clocks (P11); trademark and IP deadlines (P12); licences and registrations (FR-P13-18 or LDC); board and committee meetings, minutes clocks, filings tasks (gov); HR statutory dates — appointment letters, wage payment dates, POSH annual report, F&F timers (hr); LDC compliance tasks when linked. Filters by source, entity, department, owner, risk; ICS/Graph/Google sync with privacy-safe titles (`lgo.calendar.include_titles` default OFF). Statutory items show their rule and verification badge (NN-38).

**FR-P13-14 — CLO dashboard.** Widgets: intake queue by SLA state; requests by department and category; P1 items; overdue clocks (all sources); hearings this week; contracts awaiting legal review or signature; renewals in 90 days; TM deadlines and watch hits; board actions overdue; minutes clocks; spend vs budget; exposure movement (from P11); team workload (counts and SLA outcomes only — no time tracking, NN-33); Vidhi agent activity and approvals awaiting. Each widget opens a filtered list with bulk actions and undo.

**FR-P13-15 — Legal risk dashboard (KMP and board).** Aggregated, frozen-on-publish view (IMP-104): material matters and exposure (P11 frozen schedule), top contract risks (auto-renew traps, unlimited liability positions flagged in P07), IP risks (lapses, oppositions), governance gaps (blueprint), HR legal risks (POSH counts only, labour disputes), regulatory proceedings, upcoming critical dates. Directors see it in the board portal for meetings where it is tabled.

**FR-P13-16 — Weekly legal brief and KMP briefs.** `AGT_CLO_CHIEF_OF_STAFF` (Appendix H #28) drafts a weekly brief for the CLO — new requests, closures, SLA breaches, new matters, adverse orders, deadlines in the next 14 days, spend vs budget, decisions needed — with every figure taken from `rpt` (no model-generated numbers). `AGT_KMP_BRIEFER` (#29) drafts role-tailored briefs for the MD/CEO, CFO and CS. The CLO or KMP reviews and sends; a recurring template-based send to internal users runs automatically only if the tenant enables it within the agent's ceiling; a digest to directors always needs CLO approval (`LD-LGO-009`; NN-13).

**FR-P13-17 — Metrics with formulas.** Every metric shows its formula and source (e.g., "First-response SLA met = requests with first response ≤ target ÷ requests due in period"). Savings estimates link to `sav` with evidence class (MEASURED/ESTIMATED/MODELLED, NN-36).

### 4D. Licences and registrations register (light)

**FR-P13-18 — Register.** For LawDocs-only tenants: licence/registration type (e.g., GSTIN per State, Shops and Establishments per location, trade licence, professional tax, FSSAI, IEC, labour registrations, sector licences such as RBI Certificate of Registration recorded as metadata, ISO certificates, DSCs of signatories — metadata and expiry only, never keys), number, authority, entity, location, issue and expiry, renewal lead days (default 60), conditions, owner, documents, status (ACTIVE, RENEWAL_DUE, RENEWAL_FILED, EXPIRED, SURRENDERED, CANCELLED). Renewal tasks at lead time; expiry without renewal creates a calendar exception.

**FR-P13-19 — LDC boundary.** If the tenant uses LDC, the LDC licence register is authoritative (compliance domain, D-10); LawDocs shows it read-only in the legal calendar through `int` and offers "Open in LawDocsComply".

### 4E. Legal spend and counsel panel (department view)

**FR-P13-20 — Spend roll-up.** Legal spend across: matter spend (P11), advisory retainers and marketplace orders (P16 order mirrors), contract-review fees, eSign/eStamp and filing costs (from `bil` usage, excluding statutory duties shown separately). Budgets per department and FY, with approvals per DoA. Reports by department, category, vendor, entity.

**FR-P13-21 — Panel.** The counsel panel is P11's `counsel_panel`; P13 adds empanelment reviews (annual), panel policy (categories of work routed to the panel vs marketplace vs in-house), and rate-card approvals by the CFO (checker).

### 4F. Governance kernel mount: modes

**FR-P13-22 — Mode resolver.** The effective mode is read from the P19 keys `int.eco.ldc.sor_mode.governance` and `int.eco.ldc.sor_mode.hrms` (values `LOCAL` = the `local_kernel` mount below, `LDC` = `ldc_sor`); X-11 retired the former `gov.mode` / `hr.mode` keys, and P13 registers no mode key of its own. The keys change only through the P19 kernel system-of-record switch (FR-P19-28; Appendix A §A.48), never by direct edit:

| Mode | When | Behaviour |
|---|---|---|
| `local_kernel` | Company does not use LawDocsComply | LawDocs mounts `@infrabyx/governance-kernel` and `@infrabyx/hrms-kernel` with their schemas (`gov`, `hr`, `hr_posh`) in the LawDocs database; LawDocs is system of record for these records and runs every P13 governance and HR screen |
| `ldc_sor` | Company also uses LDC | LDC is system of record (D-10, NN-47) and governance and HR work is done in LDC screens (single sign-on; no double entry). LawDocs keeps: (a) read-through facts for legal workflows — resolutions, KMP and authorised signatories for the formalities gate and DoA (`governance.resolution:read`, `governance.kmp:read`, no caching beyond the request — FR-P19-29) and the minimal people projection for task assignment (name, work e-mail, department, position, status — FR-P19-33); (b) deep links from the P13 menus into LDC; (c) proposals to LDC — agenda items suggested by LawDocs modules and documents as `DocumentShared` (Spec §6.13) — where Appendix Y §Y.7.6 allows. No `gov`/`hr` rows are written locally |

The switch is offered when the ecosystem organisation registry (Ecosystem Spec §4.1) shows the same `org_id` subscribed to LDC; it is proposed by `ORG_ADMIN` and approved by `ORG_OWNER` and the LDC admin (P19). Governance and workforce events stay tenant-internal (Ecosystem Spec §6.23 routing rule 1): never to the Operations Hub or another group company (NN-19).

**FR-P13-23 — Kernel hooks for the switch.** P19 owns the switch states (PROPOSED → APPROVED → EXPORTING → IMPORTING → DUAL_RUNNING → CUTOVER → RECONCILED → CLOSED; ROLLBACK on any failure with LawDocs still SoR and nothing deleted). P13 supplies the kernel-side hooks: export of every `gov`/`hr` record with hash-chain heads (sealed minutes byte-identical, register event stores with sequence heads, POSH cases only to LDC's sealed store with the IC Presiding Officer's approval); read-only mode with deep links during DUAL_RUNNING (one board-meeting cycle or 30 days); local tables kept as read-only archives after cutover (NN-12: no destructive change in the same release). The reverse switch uses the same hooks.

**FR-P13-24 — Unavailability.** In `ldc_sor` mode, if LDC is unreachable, LawDocs shows "LawDocsComply unavailable" where a governance fact is needed, keeps legal drafting (agenda notes, resolution drafts) in the matter or request, and blocks actions that depend on the fact (e.g., the NN-40 formalities gate "board approval recorded") until LDC responds (`LD-GOV-013`).

### 4G. Company-type configuration and governance blueprint

**FR-P13-25 — Company types.** Constitution profiles supported by the kernel rule packs: private company, small company (s.2(85)), one person company (s.2(62)), public unlisted, listed (equity / debt-only / SME), Section 8 company, start-up private company (DPIIT-recognised — relaxations recorded as rule data [VERIFY]), LLP (LLP Act 2008), and NBFC overlays by layer (BL, ML, UL) and category (e.g., NBFC-ICC, HFC, MFI, CIC) — Appendix T §T.6–T.7.

**FR-P13-26 — Blueprint.** The kernel composes requirements from layers (constitution → Companies Act/LLP Act → securities overlay if listed → sector overlay such as `gov.rbi_nbfc_2025` → tenant charter) and outputs required organs, director categories and counts, committees with composition, quorum and cadence, KMP and functionaries, meeting cadence, registers, recurring and event filings, declarations — each line with citation, status (MET, GAP, AT_RISK, NOT_APPLICABLE, WAIVED with evidence) and "Why is this required?" (LDC P06 FR-P06-01 to FR-P06-05 pattern, shared kernel). Gaps create tasks for the CS. Thresholds are rule data with effective dates, never constants (NN-29, NN-30). Examples of Companies Act anchors (V-REG from LDC, R3 LG-155–LG-160): minimum directors s.149(1) (3 public, 2 private, 1 OPC); resident director s.149(3); independent directors s.149(4) with Rule 4 of the Companies (Appointment and Qualification of Directors) Rules 2014 [VERIFY thresholds]; Audit Committee s.177 and NRC s.178(1) (classes per Rule 6 of the Companies (Meetings of Board and its Powers) Rules 2014 [VERIFY]); Stakeholders Relationship Committee s.178(5); CSR Committee s.135; whole-time KMP s.203 with Rules 8/8A of the Companies (Appointment and Remuneration of Managerial Personnel) Rules 2014 [VERIFY].

### 4H. Board and committees

**FR-P13-27 — Board record.** Directors with category (executive, non-executive, independent, nominee with nominating institution, woman, resident), date of appointment, term, retirement by rotation (s.152(6)), ID term limits (s.149(10)–(11)), chair, committee memberships; composition validated against the blueprint on every change.

**FR-P13-28 — Committees.** Kernel catalogue with ToR template, composition rule, quorum, cadence and mandatory agenda items: Audit Committee, NRC, Stakeholders Relationship Committee, CSR Committee, Risk Management Committee, IT Strategy Committee, ALCO, Credit Committee, Review Committee (wilful defaulters), fraud risk monitoring committee, customer service / grievance committee, Independent Directors' meeting, executive/borrowing committee, POSH IC (link only — sealed in hr) and custom committees. NBFC-specific requirements and citations sit in Appendix T §T.6.3. Tenants rename committees and map one committee to several statutory roles (e.g., "Audit and Risk Committee"); the validator applies the union of rules and the strictest cadence. Invitees never count for quorum.

**FR-P13-29 — Committee page.** Composition, ToR (versioned, P04), calendar, meetings, decisions and recommendations with status, actions, attendance statistics, minutes, documents, blueprint status. Members see only their committees.

### 4I. Meetings, minutes and resolutions

**FR-P13-30 — Planner and cadence.** Annual planner with statutory cadence checks: Board — first meeting within 30 days of incorporation; at least four meetings a year with not more than 120 days between two consecutive meetings (s.173(1)); OPC, small, dormant and start-up private companies — at least one meeting in each half of the calendar year with a gap of not less than 90 days (s.173(5); the start-up private-company extension under MCA notification of 13 Jun 2017 applies only where the company is not in default of filings under s.92 or s.137 — the planner checks that flag [VERIFY current scope]); committee cadences from the blueprint; AGM window (s.96: within six months of FY end, not more than 15 months between AGMs; first AGM within nine months of the first FY end). The planner warns before a plan breaches a gap rule. Director availability poll; chosen dates create calendar holds (Graph/Google) and a pre-meeting task chain.

**FR-P13-31 — Notice.** Board: at least seven days' written notice to every director at the registered address, by hand, post, courier or electronic means, with proof of delivery captured (s.173(3); SS-1 [VERIFY para]). Shorter notice for urgent business is allowed only with the s.173(3) proviso path: at least one independent director present, or decisions circulated and ratified by at least one independent director — the system forces the path, records the ground of urgency and blocks finalising minutes until ratification is recorded (where the company has independent directors). Notice content: date, day, time, venue, video-conferencing facility and link, agenda, notes or the date they will follow (`LD-GOV-003` if notice period is short without the urgency path). General meetings: 21 clear days (s.101(1)), shorter notice with members' consent per s.101(1) proviso (thresholds per meeting type [VERIFY]), explanatory statement (s.102), proxies (s.105).

**FR-P13-32 — Agenda and papers.** Agenda items: title, type (noting, approval, discussion, recommendation), presenter, draft resolution (template library), notes on agenda, attachments, classification (NORMAL, CONFIDENTIAL, UPSI, INTEREST_SENSITIVE), interested directors (from s.184 disclosures and the related-party map), required majority, follow-on actions. **Auto-suggested items** from LawDocs modules: litigation and disputes section (P11 FR-P11-65), IP portfolio section (P12), contracts requiring board approval (P07, e.g., s.180/s.186/s.188 matters where applicable [INTERP — rule pack]), KMP appointments or changes (hr), policies due for review (P04/P06), legal risk dashboard (FR-P13-15), action-taken report, committee minutes for noting, and — when linked — LDC compliance items. Standard templates for first meeting of FY (MBP-1 disclosures, DIR-8 noting, s.149(7) ID declarations), quarterly and annual-accounts meetings.

**FR-P13-33 — Board pack and portal.** One click compiles notice, agenda, notes and previous minutes into a bookmarked, paginated, per-recipient watermarked PDF and a portal book. Interested directors get the item with a recusal banner (or the item hidden — `gov.pack.interested_director_access`). Portal: upcoming meetings, books, private annotations (never shared unless the director chooses), questions to presenters, circular resolution votes, declarations, minutes comments, signature requests; downloads OFF by default; step-up MFA for UPSI items; session timeout 15 minutes; mobile offline pack flagged OFF until P22 encrypted cache passes review (NN-44).

**FR-P13-34 — Attendance including video conferencing.** Modes: physical, video conferencing or other audio-visual means (s.173(2); Companies (Meetings of Board and its Powers) Rules 2014 r.3), leave of absence. The r.3 procedure is a CS checklist with evidence: roll call at start and after breaks; each director confirms identity and location, that no unauthorised person is present, and that they can see and hear others; recording kept in safe custody; the notice venue is the deemed place of meeting [VERIFY r.3 sub-rules]. Teams/Meet links via `WORKSPACE_PORT`; participant logs may suggest attendance, the CS confirms. Attendance register generated per SS-1 and sealed with the minutes.

**FR-P13-35 — Quorum monitor and conduct console.** Live quorum (s.174(1): one-third of total strength or two directors, whichever is higher; VC participants counted); interested directors excluded per s.184(2) for public companies (private-company exemption per MCA notification of 5 June 2015 [VERIFY]). Loss of quorum offers adjournment per s.174(4). Conduct console records per item: decision (passed unanimously / by majority with counts / deferred / withdrawn / noted), dissent and abstention names, interested directors leaving and returning, invitees, action items with owner and due date. Transcription OFF unless all participants consent at join (`gov.meeting.transcription`).

**FR-P13-36 — Minutes (s.118; SS-1/SS-2).** `AGT_MINUTES_DRAFTER` drafts from agenda, decisions log, attendance and the CS's notes (and transcript only if consented) using the SS-1 structure; every sentence is a draft until the CS accepts it; the agent never invents attendance, votes or decisions (R4 LV-12 guardrail). **Clocks:** draft to members within 15 days of the meeting; comments within 7 days of receipt; entry in the minute book within 30 days of the meeting (s.118(1) read with Companies (Management and Administration) Rules 2014 r.25 and SS-1 [VERIFY paras]); escalation at T-3 and T-0 to CS and chair. Signing by the chairperson of the meeting or of the next meeting via eSign/DSC (P08), pages consecutively numbered; signed PDF/A hashed and **SEALED**. **No alteration after signing** (SS-1: entered minutes are not altered except with the Board's express approval at a subsequent meeting [VERIFY para]; tampering with minutes is an offence under s.118(12); s.118(7)–(8) make duly kept minutes evidence of the proceedings): no edit function for any role including Super Admin; errors are handled by a note in the next meeting's minutes and a Correction Entry annotation cross-referencing it (NN-02, NN-09). General meeting minutes per SS-2 within 30 days. Certified true copies generated on request with a serial number register.

**FR-P13-37 — Resolutions, circular resolutions and follow-on actions.** Resolution register (`res_`): body, meeting, type (BOARD, CIRCULAR, COMMITTEE, ORDINARY, SPECIAL, UNANIMOUS), text, effective date, filings and actions triggered. **Circular resolutions** (s.175): draft with necessary papers circulated to all directors entitled to vote; passed when approved by a majority of them; interested directors excluded; if not less than one-third of the total number of directors then in office require the matter to be decided at a meeting, the circulation stops and an agenda item is created; result noted at the next meeting and recorded in its minutes. Matters that must be decided at a meeting (s.179(3) and others in the rule pack [VERIFY list]) are blocked from circulation (`LD-GOV-005`). Response window `gov.circular.response_days` (default 7 [VERIFY SS-1]). **Follow-on**: each resolution template declares follow-ons — e.g., MGT-14 filing task within 30 days for resolutions under s.117(3) [VERIFY list], DIR-12 on director changes, MR-1 within 60 days for MD/WTD/manager appointments [VERIFY], bank mandate updates, register entries — created as tasks with due dates; filing is done by the CS or engaged professional on MCA21 (NN-13), who records SRN and date. Decisions with action elements create tasks immediately; an action-taken report is generated for the next meeting.

### 4J. Statutory registers

**FR-P13-38 — Register engine (kernel).** Registers are projections over an append-only event store (never free-edited tables; NN-02): register of members (s.88; MGT-1), debenture holders (MGT-2), directors and KMP and their shareholding (s.170), loans, guarantees, security and acquisitions (s.186(9); MBP-2), contracts or arrangements with related parties and in which directors are interested (s.189; MBP-4), charges (s.85; CHG-7), significant beneficial owners (s.90; Companies (Significant Beneficial Owners) Rules 2018 [VERIFY form]), share certificates issued/renewed/duplicated (SH-2), employee stock options (SH-6) [VERIFY], transfers and transmissions; LLP: partners and designated partners, contributions. Each register declares legal basis, form, columns, source events, inspection rules and retention. Entries are created by events from meetings and resolutions (e.g., an allotment resolution proposes MGT-1 entries) and confirmed by the CS (maker-checker for master-data changes, CH-26).

**FR-P13-39 — Inspection and extracts.** Inspection and copy requests (members, directors, creditors as permitted — s.94 with Management and Administration Rules r.14 [VERIFY]; s.119 minutes of general meetings) are logged with requester type, fee if any, approval and the extract produced (PDF with serial number). Registers are kept electronically per the Rules [VERIFY r.27–28 on electronic maintenance] with hash-chained history.

### 4K. Directors and KMP profiles

**FR-P13-40 — Person master.** Directors, KMP, senior management and non-director committee members are `prs_` persons projected into governance roles; non-employees (independent and nominee directors) have no employment record. Identity minimisation (NN-04, NN-32): DIN stored; PAN masked + token; Aadhaar never stored; date of birth only where a statutory form needs it, encrypted at field level; passport only for foreign directors.

**FR-P13-41 — Director record.** DIN and status; director KYC status and next due date (the Companies (Appointment and Qualification of Directors) Amendment Rules 2025 move director KYC to once every three years — LDC V-REG, effective 31 Mar 2026 [VERIFY form name and dates]); DSC metadata (class, issuer, serial, expiry, custody log — no private keys); category; appointment and term; directorships held and limits (s.165: 20 companies including 10 public); disqualification watch (s.164(1)–(2)) and vacation (s.167); declarations (MBP-1 under s.184(1) at the first board meeting of each FY and on change; DIR-8 under s.164(2); s.149(7) independence declaration; NBFC fit-and-proper declaration and Deed of Covenant — Appendix T §T.6.2); interests feeding agenda recusal; committee memberships; familiarisation and evaluation records.

**FR-P13-42 — KMP record and vacancy clocks.** MD/CEO/manager, WTD, CFO, CS (s.2(51), s.203) and sector functionaries (CRO, CCO, Head of Internal Audit, CISO, Grievance Redressal Officer, Principal Officer and Designated Director under PML Rules, Internal Ombudsman where applicable — Appendix T §T.6.4). Each has appointment chain (board resolution, shareholder approval where needed, regulator approval or intimation), filings (DIR-12; MR-1 [VERIFY]), and vacancy clock (s.203(4): fill a whole-time KMP vacancy within six months). KMP designations are made in the HR kernel position record and projected here; a change emits `KmpChanged` internally (Ecosystem Spec §6.23 shape; never PAN or date of birth); in `ldc_sor` mode the KMP record lives in LDC and LawDocs reads it on demand (FR-P19-29).

**FR-P13-43 — Declaration campaigns.** Campaigns issue pre-filled declaration forms (MBP-1, DIR-8, s.149(7), fit-and-proper, code-of-conduct affirmation, related-party information) with deadlines; directors complete and eSign in the portal; the CS reviews changes against last year (highlighted); results feed the blueprint and agenda (first meeting of the FY).

### 4L. Duties and task assignment

**FR-P13-44 — Duty catalogue (content, NN-30).** Duties are versioned content with citation and owner role: directors' duties (s.166), independent directors' duties (Schedule IV [VERIFY]), CS functions (s.205), CFO duties (financial statements authentication s.134(1)), board's report responsibility statement (s.134(5)), KMP and functionary duties for NBFCs (Appendix T §T.6.4), legal department duties (Appendix T §T.2 RACI), HR statutory duties (appointment letters, wage payment, IC). Tenants add their own duties (TENANT tier).

**FR-P13-45 — Assignment.** Duties attach to **positions**, not persons (so they move with role changes): position → duties → recurring tasks (frequency, due rule, evidence required, reviewer). Hierarchical assignment uses HR reporting lines: a user may assign to anyone below them, to peers by delegation rule, or to an agent (as maker); the CS and committee chairs may assign within their body regardless of hierarchy. Assignment, acknowledgement, completion evidence and review are logged. Duties without a holder (vacant position) raise a gap on the CLO/CS dashboard.

**FR-P13-46 — Delegation of authority (DoA).** A matrix of actions × value bands × approvers (legal actions from Appendix T §T.5 — e.g., approve contract by value and risk tier, engage counsel, approve settlement or waiver, approve legal spend, sign on behalf of the company — plus board-delegated powers under s.179 resolutions). The rules engine blocks any action above the actor's delegation and routes it to the next level (`LD-LGO-007`). Matrix changes are maker-checker, effective-dated, and reference the board resolution where the delegation is board-approved.

### 4M. Finance-company structure and RBI alignment

**FR-P13-47 — NBFC template.** NBFC tenants adopt the Appendix T §T.6 template: board composition requirements, committees, KMP and regulated functionaries, departments (Credit, Risk, Compliance, Legal, Finance & Accounts, Treasury, Operations, Collections & Recovery, IT, Information Security, HR, Internal Audit, Customer Service/Grievance, Secretarial, Business), reporting lines, three lines of defence and segregation-of-duties rules. Everything is editable; statutory items are flagged and cannot be deleted silently — deleting a statutory committee or functionary requires the CS and a checker and creates a blueprint GAP with the reason.

**FR-P13-48 — RBI overlay through the shared kernel.** The governance overlay for NBFCs comes from the kernel rule pack `gov.rbi_nbfc_2025`, the same content LDC uses (NN-47). Its anchor is the **Reserve Bank of India (Non-Banking Financial Companies – Governance) Directions, 2025, RBI/DOR/2025-26/344, 28 November 2025** (title as carried in LDC v1.2 G LR-RBI-027 and R3 LG-161 [VERIFY exact title wording]), with paragraph references for: director with banking/NBFC experience (para 8), Risk Management Committee (para 9), prior approval for change of more than 30% of directors (paras 10–11), fit-and-proper declarations and Deed of Covenant (paras 12–13), quarterly statement on directors (para 14), Audit Committee (para 17), NRC (para 18), CRO (paras 19–24), CCO (para 25), KMP restrictions (para 26), cap on independent directorships (para 27), compensation (paras 29–37), whistle-blower mechanism (para 38) — V-REG from LDC, to be re-verified against the RBI text before the overlay flag leaves advisory (NN-38; OI-P13-03). Other directions in the 28 Nov 2025 consolidated set (e.g., KYC RBI/DOR/2025-26/361, Responsible Business Conduct RBI/DOR/2025-26/362, Outsourcing RBI/DOR/2025-26/363, Wilful Defaulters RBI/DOR/2025-26/358 — V-REG) only seed committees, functionaries and departmental duties here; compliance obligations live in LDC.

**FR-P13-49 — Recommendation for regulated entities.** For NBFCs and other REs, LawDocs shows a one-time, dismissible recommendation that compliance management, returns and inspections run in LawDocsComply, with LDC as governance SoR [REC]. LawDocs-only NBFCs can still run governance locally with the overlay pack; the product does not claim RBI compliance (NN-20).

**FR-P13-50 — Three lines of defence and segregation of duties.** Each department carries `line_of_defence` (FIRST, SECOND, THIRD, SUPPORT, GOVERNANCE) and reporting line (to MD/CEO, to a board committee, dual). SoD rules (content) flag conflicting assignments — e.g., the same person as head of a business department and CRO; CCO with business targets; Head of Internal Audit reporting to a business head; CISO reporting to the head of IT [VERIFY each rule source in Appendix T]; maker and checker on the same process. Conflicts appear as blueprint AT_RISK lines with the rule citation; they do not block HR changes (warnings, not hard blocks) unless the tenant elects hard blocking for specific rules.

### 4N. HRMS kernel mount for client companies

**FR-P13-51 — Scope and modes.** `int.eco.ldc.sor_mode.hrms` = `LOCAL` (`local_kernel`) or `LDC` (`ldc_sor`) (FR-P13-22). In `local_kernel` mode the mount gives client companies their HRMS: persons, employments, establishments, departments, positions, grades, reporting lines, KMP designations, duties, leave, attendance, payroll, documents, acknowledgements and POSH. Infrabyx's own staff HR is the Operations Hub (D-02) — never this module. In `ldc_sor` mode LDC P13 is authoritative and LawDocs uses only the minimal people projection (FR-P19-33).

**FR-P13-52 — Establishments, departments and positions.** Establishments (registered office, branches, etc.) with State (drives the labour rule pack's State rules) and headcount; departments (department → function → team, renameable; mapping by ID); positions with approved headcount, grade, reporting position, location, sensitive-position flag, regulated-role flag (CCO, CRO, CISO, PNO, GRO, Principal Officer, Designated Director, DPO, Internal Ombudsman) and KMP flag. Org chart auto-generated with an "as of" date; accessible list view.

**FR-P13-53 — People and lifecycle.** Person vs employment (one person may have several employments over time); worker classification per the Labour Codes (employee/worker, fixed-term, contract labour via contractor) from the rule pack (R3 LG-162); lifecycle: requisition → offer → appointment → joining → probation → confirmation → movements → separation. Joiner–mover–leaver drives access in LawDocs (SCIM to Keycloak; role bundle from position; leaver access off the same day — Ecosystem Spec §6.23 `EmployeeOffboarded` semantics).

**FR-P13-54 — Documents from templates.** Offer letter, **appointment letter** (mandatory under the OSH Code s.6(1)(f) — R3 LG-164), employment agreement (clause library: duties, confidentiality, DPDP employee notice, IP assignment, non-solicit within lawful limits [COUNSEL]), NDA, policy acknowledgements, confirmation, transfer, promotion, warning/show-cause (restricted), relieving and experience letters, full-and-final statement. Generated via `docgen`, eSigned via P08 (all are eSign-eligible employment documents [INTERP — Appendix F]); stored in `07 People and HR/`.

**FR-P13-55 — Leave.** Two layers: statutory floors from the labour rule pack (e.g., OSH Code s.32 annual leave with wages — 1 day for every 20 days of work after 180 days in a calendar year, carry-forward cap 30 — R3 LG-164; State Shops and Establishments rules where higher) and the company's policy on top (casual, sick, maternity 26 weeks under the SS Code — R3 LG-165, paternity, bereavement, WFH days). Apply/approve in ≤ 2 taps; auto-approval rules (tenant-configured); team calendar respecting privacy (sensitive leave types hidden).

**FR-P13-56 — Attendance and work measurement (proportionate, disclosed).** Capture: web/mobile check-in and check-out, optional geo-tag only at check-in/out moments with notice and consent, Wi-Fi/IP ranges, or declared WFH. **Not built:** keystroke or mouse logging, covert screenshots, webcam capture, browsing monitoring, continuous location, AI productivity scores used for discipline or pay (NN-33; CH-24; CH-32; Ecosystem Spec §6.23 rule 4). Productivity views use outcomes: tasks closed, SLA met, deliverables approved. Login/logout times are kept for attendance only and are visible to the employee.

**FR-P13-57 — Payroll via `infrabyx-labour-rulepack`.** Components with statutory class; statutory wage base per Code on Wages s.2(y) (if excluded components exceed 50% of total remuneration, the excess is added back — R3 LG-163); EPF, ESI, gratuity, bonus, PT and LWF by State from the pack; monthly pay run with maker-checker (`PAYROLL_MAKER` ≠ `PAYROLL_CHECKER`, NN-18), lock and payslips; wage payment timing checks (Code on Wages s.17: monthly wages before the seventh day of the following month; full and final within two working days of separation — R3 LG-163); TDS on salary under the Income-tax Act 2025 [VERIFY sections; TAX MEMO]; corrections as Correction Entries (NN-02); bank payment file export (the company pays; LawDocs never holds funds). The pack is consumed, never forked (NN-47); a new pack version applies by effective date without a code release (NN-30).

**FR-P13-58 — Policy acknowledgements and training.** Policies (P04/P06) pushed to groups with read-and-acknowledge tracking, reminders and completion reports; mandatory trainings by position may link to FinLegal Academy courses (deep links, D-16).

**FR-P13-59 — POSH Internal Committee (sealed).** For workplaces with 10 or more employees: IC constitution per office/administrative unit (POSH Act 2013 s.4: Presiding Officer — a senior woman employee, at least two employee members, one external member; at least half women [VERIFY composition text]); IC member terms; complaint intake through a sealed channel (no line-manager visibility); clocks: complaint within three months of the incident (s.9, extendable for reasons), inquiry completion within 90 days (s.11(4)), report within 10 days of completion (s.13), employer action within 60 days of the report (s.13(4)) [VERIFY], annual report (s.21) and Board's report disclosure (Companies (Accounts) Rules 2014 r.8(5)(x) [VERIFY]). Sealed store: separate schema `hr_posh` with its own KMS key; access only for `ORG_POSH_IC_PRESIDING` and `ORG_POSH_IC_MEMBER` holders of that IC and the employer action officer for outcome actions; excluded from search, AI retrieval (except a sealed, IC-only drafting assistant at L0/L1 if the IC enables it), exports to other roles, analytics and every cross-product event; only counts leave the seal (NN-19, NN-26).

**FR-P13-60 — HR legal matters.** Labour disputes, employee suits and POSH appeals create P11 matters with the minimum necessary data; sealed POSH content never flows into P11 (the matter references the IC case ID only).

### 4O. Board and KMP AI agents (P09 hooks)

**FR-P13-61 — Agents.**

| Agent (Appendix H #; R4 roster) | Work | Default / ceiling | Human gate |
|---|---|---|---|
| `AGT_BOARD_SECRETARY` (#13; LV-11) | Annual planner, notices, agendas, auto-suggested items, pack index, quorum/cadence checks (deterministic), SS-1/SS-2 checklists, declaration campaigns, register-entry proposals | L1 / L2 | CS approves notices, agendas and packs; issuing is a human action |
| `AGT_RESOLUTION_DRAFTER` (#16) | Resolutions and explanatory statements from the library and meeting outcomes; CTC drafts | L1 / L1 | CS approves; signatory signs CTC |
| `AGT_MINUTES_DRAFTER` (#15; LV-12) | Minutes drafts and action-taken reports | L1 / L1 | CS accepts each sentence; chair signs; never invents attendance or votes |
| `AGT_ACTION_ITEM_TRACKER` (#17) | Turns decisions into task proposals; chases internal owners; status table for the next meeting | L1 / L3 (internal reminders) | Chair/CS approves the task list |
| `AGT_COMPLIANCE_CALENDAR` (#18; LV-13) | Legal calendar items from rules (filings, KMP vacancies, minutes clocks, HR statutory dates); chasers to internal owners; defers to LDC when linked | L1 / L3 (internal reminders only) | Filing always human; no "complied" marking by AI |
| `AGT_LEGAL_INTAKE_DESK` (#27) | Intake classification, document collection, routing proposals, self-service answers from approved knowledge with citations | L1 / L2 | Legal team accepts routing; human triage for P1 and sensitive categories |
| `AGT_CLO_CHIEF_OF_STAFF` (#28) | Weekly CLO brief (figures only from `rpt`) | L1 / L1 | CLO reviews and sends |
| `AGT_BOARD_PACK_SUMMARISER` (#14) in the board portal | Per-item summaries in the director's language; up to five questions a director may wish to ask, citing source records | L1 / L1 (read-only; nothing enters memory) | Director decides; private to the director |
| `AGT_KMP_BRIEFER` (#29) | Role briefs (CEO, CFO, CS); "my duties this week"; draft certificates and confirmations for review | L1 / L1 | KMP reviews and signs |

Agents never vote, sign, approve, seal, file, or send outside the tenant (NN-13, NN-43). Autonomy ceilings are tenant settings within plan limits (maker-checker). Privileged, UPSI and POSH contexts are excluded unless the owner role enables a scoped run.

### 4P. Retainer delivery and makers

**FR-P13-62 — RM as delegated maker (R-064).** For retainer clients, the LawDocs RM (`OPS_RM`) works inside the client tenant as `ORG_DELEGATED_MAKER` under a client-approved, scoped, time-bound delivery grant (NN-17): drafts, agenda items, minutes skeletons, register entry proposals, HR documents; the client's employee is checker/approver. Multiple makers are allowed; the client can create makers for professional services, and the Delivery Console can propose a maker for the client's approval (P18). Every action is in the client's access-transparency log.

**FR-P13-63 — Managed legal department retainers.** A "Managed Legal Department" retainer (R6 RS-LD-21) stays OFF until the structure memo confirms that advice is supplied by an advocates' firm engaged directly by the client and LawDocs bills only SaaS and coordination [COUNSEL; OI-P13-06].

### 4Q. Group and multi-entity

**FR-P13-64 — Group view.** A tenant with several legal entities sees a group legal calendar, intake by entity, governance blueprint status per entity, common directors and interlocks, and HR headcount by entity; entity-level roles restrict access. Cross-entity request routing (e.g., a shared legal team serving subsidiaries) follows the routing table with entity scopes.

### 4R. Customisation and click budgets

**FR-P13-65 — Customisation hooks (no Super Admin; NN-29).** Intake categories, forms, SLAs (within platform floors), routing tables, self-service limits, waiting-item types, DoA matrix, department and committee names and structure, duty catalogue additions, board-pack templates, minute templates, notice templates, register views, leave policies, auto-approval rules, payroll components (within statutory rules), document templates, dashboard widgets, digest content and cadence, agent autonomy (within plan ceiling).

**FR-P13-66 — Click budgets.**

| Journey | Budget |
|---|---|
| Raise a legal request from any page | ≤ 3 clicks |
| Triage a request (accept proposal) | ≤ 2 clicks |
| Self-serve an NDA on the company template | ≤ 6 steps, no lawyer touch |
| Schedule a board meeting and issue notice with agenda | ≤ 6 steps |
| Circulate draft minutes after the meeting | ≤ 3 clicks from the conduct console |
| Approve a circular resolution (director, mobile) | ≤ 3 taps with step-up |
| Assign a duty to a position | ≤ 3 clicks |
| Approve leave (manager, mobile) | 1 tap from the notification |
| Adopt the NBFC structure template | ≤ 15 minutes in the wizard |

## 5. Workflows and state machines

### 5.1 Legal request (`lgo.request`)

State machine: Appendix A §A.46 governs (Resolution R-A-13 — one front door). When `lgo` is enabled, a Company tenant has **one** intake front door: contract requests are legal requests, and CONVERTED creates the P07 `clm.intake_request` directly in its TRIAGED state with the `lrq_` link (no second triage); when `lgo` is not enabled (plans without the Legal Department OS) the P07 CLM intake stands alone. Teams, email-in and mobile channels post to whichever front door is active. WAITING uses the single items engine: the waiting item is a `wf.items` row (P03, A.15); `lgo.waiting_items` is only a read view over `wf.items` + `wf.item_waits` (X-09; R-A-07).

| State | Entry | Next | Actor | Guard | Side effects / events |
|---|---|---|---|---|---|
| SUBMITTED | Any channel | TRIAGED, SELF_SERVED | Requester / `AGT_LEGAL_INTAKE_DESK` proposes | Required fields | SLA timers start; `in.lawdocs.lgo.RequestSubmitted.v1` |
| TRIAGED | Category, priority, owner confirmed | IN_PROGRESS, CONVERTED, REJECTED | Triager | P1/sensitive → human only | `RequestTriaged` |
| IN_PROGRESS | Work started (first response) | WAITING, PENDING_APPROVAL, RESOLVED, CONVERTED | Assignee | — | First-response SLA met/breached |
| WAITING | Waiting on requester/counterparty/internal | IN_PROGRESS | Assignee | Reason + waiting item (`itm_`) | SLA pause only for permitted reasons |
| PENDING_APPROVAL | Output needs approval per DoA | IN_PROGRESS, RESOLVED | Approver ≠ maker | DoA band | — |
| CONVERTED | Child record created (contract, notice, matter, TM, board item, HR, LDC, marketplace) | RESOLVED (mirrors child) | Assignee | Child exists | `RequestConverted` |
| SELF_SERVED | Guided path completed within guardrails | CLOSED | Requester | Guardrail check passed | — |
| RESOLVED | Outcome recorded | CLOSED, IN_PROGRESS (reopen ≤ 14 days) | Assignee | Outcome text | Satisfaction prompt |
| REJECTED | Out of scope / duplicate | CLOSED | Triager | Reason | — |
| CLOSED | Auto after 7 days or on rating | — | System | — | Metrics |

### 5.2 Meeting (`gov.meeting`, kernel)

State machine: Appendix A §A.47 governs until the kernel's own definition is pinned in `docs/kernels.lock` (NN-47).

DRAFT → SCHEDULED (date fixed; cadence check) → NOTICE_ISSUED (proof of delivery; shorter-notice path if used) → PAPERS_CIRCULATED → IN_SESSION (attendance, quorum monitor) → CONCLUDED → MINUTES_DRAFTED (≤ 15 days) → MINUTES_CIRCULATED → COMMENTS_CLOSED (7 days) → MINUTES_SIGNED → SEALED (≤ 30 days; s.118). Side states: ADJOURNED (quorum lost, s.174(4)), CANCELLED (reason). Ratification pending blocks SEALED when the shorter-notice path was used.

### 5.3 Circular resolution (kernel)

State machine: Appendix A §A.47 governs (Resolution R-A-17: the general resolution lifecycle is compiled there from FR-P13-37; the kernel definition prevails once pinned).

DRAFT → BLOCKED (s.179(3) or other meeting-only matter) | CIRCULATED → [votes] → PASSED (majority of directors entitled to vote) | FAILED | REFERRED_TO_MEETING (≥ one-third require a meeting) → NOTED_AT_NEXT_MEETING.

### 5.4 Kernel system-of-record switch

State machine: Appendix A §A.48 governs.

State machine owned by P19 §5.6 (PROPOSED → APPROVED → EXPORTING → IMPORTING → DUAL_RUNNING → CUTOVER → RECONCILED → CLOSED | ROLLBACK). P13 kernel hooks per FR-P13-23: EXPORTING emits per-record hashes and hash-chain heads; DUAL_RUNNING sets `gov`/`hr` screens read-only with deep links; RECONCILED requires counts, hash heads and byte equality for sealed minutes; CLOSED archives local tables read-only.

### 5.5 KMP vacancy

POSITION_FILLED → VACANCY_OPENED (cessation recorded; s.203(4) six-month clock; regulator intimation tasks for regulated functionaries) → CANDIDATE_PROPOSED → APPROVALS (board, shareholders where needed, regulator where needed) → APPOINTED (filings tasks: DIR-12/MR-1) → POSITION_FILLED. Clock breach → blueprint GAP and CS/CLO alert.

### 5.6 POSH complaint (sealed, kernel)

RECEIVED → (optional) CONCILIATION_REQUESTED by the aggrieved woman (s.10; no monetary settlement) → INQUIRY (≤ 90 days) → REPORT_ISSUED (≤ 10 days of completion) → EMPLOYER_ACTION (≤ 60 days) → CLOSED; APPEAL_NOTED (P11 matter reference only). Only counts and ageing leave the seal.

### 5.7 Pay run (kernel)

INPUTS_OPEN (`ORG_PAYROLL_MAKER`) → INPUTS_LOCKED → COMPUTED (pack version recorded) → REVIEWED (`ORG_PAYROLL_CHECKER` ≠ maker) → APPROVED → PAYSLIPS_PUBLISHED → BANK_FILE_EXPORTED → PAID_CONFIRMED; corrections create an off-cycle run referencing the original.

## 6. Screens and UX

Menus (Company workspace): **Legal Department** (Home, Requests, Calendar, Spend, Panel, Licences, Settings), **Board & Governance** (Planner, Meetings, Resolutions, Registers, Directors & KMP, Committees, Blueprint), **People** (Directory, Org chart, Leave, Attendance, Payroll, Documents, Policies, POSH (sealed entry)). Board portal for directors. "i" keys: `hlp.lgo.sla`, `hlp.lgo.self_service`, `hlp.lgo.doa`, `hlp.gov.quorum`, `hlp.gov.circular_resolution`, `hlp.gov.shorter_notice`, `hlp.gov.minutes_clock`, `hlp.gov.mbp1`, `hlp.gov.din`, `hlp.gov.kmp`, `hlp.gov.blueprint`, `hlp.gov.three_lines`, `hlp.hr.wage_base`, `hlp.hr.appointment_letter`, `hlp.hr.posh_ic`, `hlp.hr.full_and_final`.

| ID | App | Purpose | Key components | Empty / error | Mobile | Accessibility |
|---|---|---|---|---|---|---|
| SCR-P13-01 Setup Wizard | web | Operating model adoption | 7 steps; template preview; diff on re-run | — | Not on phone | Stepper landmarks |
| SCR-P13-02 Legal Department Home (CLO) | web, mobile | CLO dashboard | Widgets FR-P13-14 | "Invite your team and set categories" | Tile list | Tiles as headings |
| SCR-P13-03 Request Legal Help | web, mobile, Teams/Chat | Intake | Category picker with search, dynamic form, attachments, self-service offer | — | ≤ 3 taps | Form errors summarised |
| SCR-P13-04 Requests Queue | web | Triage and work | Queue with SLA chips, proposals, bulk assign | — | List | SLA state as text |
| SCR-P13-05 Request Workspace | web | One request | Thread, files, waiting items, conversions, approval | — | Read and reply | — |
| SCR-P13-06 My Requests | web, mobile | Requester view | Status, needed from you, chat, rating | — | Primary | Plain language |
| SCR-P13-07 Legal Calendar | web, mobile | All legal dates | Month/agenda; source filters; verification badges | — | Agenda default | Agenda accessible default |
| SCR-P13-08 Legal Risk Dashboard | web, board portal | KMP/board view | Frozen sections with as-of dates | — | Read-only | Tables with captions |
| SCR-P13-09 DoA Matrix | web | Delegations | Matrix editor, preview "who approves what", effective dates | — | — | Grid keyboard |
| SCR-P13-10 Licences Register | web | Light register / LDC projection | Expiry strip, renewal tasks | LDC mode → "Open in LawDocsComply" | List | — |
| SCR-P13-11 Governance Blueprint | web | Requirements vs structure | Lines with status, citations, "why" drawer, gap tasks | — | Read-only | — |
| SCR-P13-12 Board & Committees | web | Composition | Members, categories, terms, validator results | — | Read-only | — |
| SCR-P13-13 Meeting Planner | web | Annual calendar | Cadence warnings, availability poll | — | — | — |
| SCR-P13-14 Meeting Workspace | web | Notice, agenda, pack, attendance, console | Tabs per stage; quorum monitor | Short notice → urgency path | Tablet for console | Live quorum announced |
| SCR-P13-15 Board Portal | web (PWA), mobile | Directors | Books, annotations, questions, votes, declarations, signatures | — | Primary for directors | Screen-reader-friendly book outline |
| SCR-P13-16 Minutes Editor | web | Draft → seal | SS-1 skeleton, AI draft with accept per sentence, comments, clocks, sign and seal | Sealed → read-only + CTC | — | Diff view accessible |
| SCR-P13-17 Resolutions Register | web | Resolutions and follow-ons | Filters, follow-on task status, SRN capture | — | List | — |
| SCR-P13-18 Statutory Registers | web | Register projections | Register picker, entries, inspection log, extracts | — | Read-only | Tables |
| SCR-P13-19 Directors & KMP | web | Profiles | DIN, KYC due, DSC expiry, declarations, limits, vacancies | — | Read-only | — |
| SCR-P13-20 Duties | web | Duty catalogue and assignments | Position → duties → tasks; gaps | — | My duties (mobile) | — |
| SCR-P13-21 Org Structure | web | Departments, positions, org chart, lines of defence | Template diff, SoD warnings | — | Org chart list view | List view is accessible default |
| SCR-P13-22 People Directory & Profile | web, mobile | HR records | Employment, documents, leave, payslips (self) | — | Self-service | — |
| SCR-P13-23 Leave & Attendance | web, mobile | Apply/approve; check-in | One-tap leave, team calendar, disclosed capture | Consent missing → notice | Primary | Calendar with list alternative |
| SCR-P13-24 Payroll | web | Pay runs | Inputs, readiness check, compute, review, approve, bank file | Pack version mismatch → block | — | — |
| SCR-P13-25 POSH (sealed) | web | IC only | Cases, clocks, documents, annual report | Non-IC → "Restricted area" | — | Accessible complaint form for any employee |
| SCR-P13-26 Policy Acknowledgements | web, mobile | Read and acknowledge | Policy viewer, acknowledge, quiz optional | — | Primary | Readable PDF/HTML |

## 7. Backend design

### 7.1 Modules

`lgo` (owner; schema `lgo`): intake, categories, routing, SLA, waiting-item type configuration and the read view over `wf.items` (X-09), calendar aggregation, licences (light), spend roll-up, DoA, duties catalogue binding, dashboards. `gov` (kernel mount; schema `gov` provided by `@infrabyx/governance-kernel` migrations): entities' governance profile, blueprint, board, committees, meetings, agenda, packs, attendance, minutes, resolutions, register event store, directors/KMP roles, declarations. `hr` (kernel mount; schemas `hr` and `hr_posh` from `@infrabyx/hrms-kernel`): persons/employments, establishments, departments, positions, leave, attendance, payroll (with `infrabyx-labour-rulepack`), documents, acknowledgements, POSH. LawDocs adds behaviour only through kernel extension points (hooks, extension tables `gov_ext_*`, `hr_ext_*`), never by patching kernel code (NN-47); kernel versions pinned in `docs/kernels.lock`.

### 7.2 Tables

**Schema `lgo`** (all rows: `tenant_id`, `legal_entity_id`, RLS, ledger pointer):

| Table | Key columns | Indexes | Retention |
|---|---|---|---|
| `requests` | id `lrq_`, ref, channel, requester_id, department_id, category_code, priority, state, owner_id, sla_policy_id, due_first_response, due_resolution, converted_ref, outcome, rating | (tenant, state, due_resolution), (tenant, category_code) | 8 years after closure [REC] |
| `request_events` (append-only) | request_id, seq, type, actor, payload | (request_id, seq) | as requests |
| `categories` | code, name, form_tpl_id, attachments, priority_rule, sla_policy_id, routing_rule_id, selfservice jsonb, conversion_target, approvals, active | (tenant, active) | while active + 3 years |
| `sla_policies` / `sla_timers` | targets per priority, calendar_id, pause_reasons; timer: request_id, kind, started_at, paused_ms, breached_at | (tenant, breached_at) | as requests |
| `routing_rules` | decision table ref (`rul`), version | — | versions kept |
| `waiting_items` (read **view** over `wf.items` + `wf.item_waits`, X-09; no separate table, no separate `itm_` allocation) | id `itm_`, subject_ref, type_code, waiting_on, since, owner_id, state | (tenant, state, since) | as subject |
| `licences` | type, number, authority, entity, location, issued_on, valid_to, lead_days, conditions jsonb, owner_id, status | (tenant, valid_to) | expiry + 8 years |
| `doa_matrix` | action, band_from, band_to, approvers jsonb, effective_from, board_ref, version | (tenant, action, effective_from) | permanent (versions) |
| `budgets` | department_id, fy, category, amount | (tenant, fy) | 8 FY |
| `calendar_items` (materialised view) | source, source_ref, due_on, rule_ref, verified, owner_id, entity | (tenant, due_on) | rebuilt |
| `duty_assignments` | duty_code, position_id, frequency, due_rule, evidence_required, reviewer_position_id | (tenant, position_id) | while active + 8 years |
| `digests` | period, audience, content_ref, approved_by, sent_at | (tenant, period) | 3 years |

**Schemas `gov`, `hr`, `hr_posh`** — provided by the kernels (key tables listed for orientation; definitions belong to the kernels): `gov.entity_profiles`, `gov.blueprint_lines`, `gov.bodies`, `gov.body_members`, `gov.meetings`, `gov.agenda_items`, `gov.packs`, `gov.attendance`, `gov.decisions`, `gov.minutes` (sealed hash, sealed_at), `gov.resolutions` (`res_`), `gov.register_events` (append-only) with register projections, `gov.officer_roles`, `gov.declarations`; `hr.persons`, `hr.employments`, `hr.establishments`, `hr.departments` (`dep_`, shared with `org`), `hr.positions` (`pos_`), `hr.leave_*`, `hr.attendance_events`, `hr.pay_runs`, `hr.payslips`, `hr.documents`, `hr.acknowledgements`; `hr_posh.ics`, `hr_posh.cases`, `hr_posh.case_events` (separate KMS key). In `ldc_sor` mode these schemas are not populated; read-through facts come from LDC.

### 7.3 APIs (REST under `/v1/<module>/` per FR-P19-03 and Appendix I §I.5; scopes `<module>.<resource>:<action>`; `Idempotency-Key` on every mutation)

| Method | Path | Scope | Notes |
|---|---|---|---|
| POST | `/v1/lgo/intake-requests` | `lgo.intake:create` | Any authenticated tenant user |
| GET/PATCH | `/v1/lgo/intake-requests/{id}` | `lgo.intake:read` / `lgo.intake:work` | Row access by requester, assignee, team |
| POST | `/v1/lgo/intake-requests/{id}:triage` · `:convert` · `:resolve` | `lgo.intake:work` | Convert calls the target module API |
| GET/PUT | `/v1/lgo/request-types`, `/v1/lgo/routing`, `/v1/lgo/sla-policies` | `lgo.config:write` | Maker-checker on publish |
| GET | `/v1/lgo/calendar?from=&to=` | `lgo.calendar:read` | Aggregated; source-scoped permissions |
| GET | `/v1/lgo/spend?period=` | `lgo.spend:read` | Roll-up across matters, retainers, orders |
| GET/PUT | `/v1/lgo/doa` | `lgo.doa:read` / `lgo.doa:write` | Effective-dated versions |
| GET/POST | `/v1/lgo/licences` | `lgo.licence:read` / `lgo.licence:write` | `ldc_sor` → read-only proxy |
| GET | `/v1/lgo/dashboards/{code}` | role-based | — |
| GET/POST | `/v1/gov/meetings`, `/v1/gov/resolutions`, `/v1/gov/registers/{code}`, `/v1/gov/officers`, `/v1/gov/declarations`, `/v1/gov/blueprint` | `gov.meeting:*`, `gov.resolution:*`, `gov.register:*`, `gov.officer:*`, `gov.declaration:*`, `gov.blueprint:read` | Kernel API surface; `local_kernel` mode only |
| GET | `/v1/hr/people?fields=minimal` | `hr.employee:read.minimal` | Served from LDC in `ldc_sor` mode (FR-P19-33) |
| GET/POST | `/v1/hr/...` (employments, positions, leave, attendance, pay-runs, documents, acknowledgements) | `hr.<resource>:*` | Kernel API surface; `local_kernel` mode only |
| GET/POST | `/v1/hr/posh/...` | `hr.posh:*` | IC role + sealed-session step-up |
| GET | `/m/v1/legal-home`, `/m/v1/board-portal`, `/m/v1/me/hr` | mobile BFF | Minimal payloads |

### 7.4 Domain events (internal)

`in.lawdocs.lgo.RequestSubmitted.v1`, `RequestTriaged.v1`, `RequestConverted.v1`, `RequestResolved.v1`, `SlaAtRisk.v1`, `SlaBreached.v1`, `SelfServiceCompleted.v1`, `LicenceRenewalDue.v1`, `LicenceExpired.v1`, `DoaChanged.v1`, `DigestApproved.v1`, `DutyGapDetected.v1`; `in.lawdocs.gov.MeetingScheduled.v1`, `NoticeIssued.v1`, `PackPublished.v1`, `MeetingConcluded.v1`, `MinutesCirculated.v1`, `MinutesSealed.v1`, `ResolutionPassed.v1`, `CircularResolutionReferred.v1`, `RegisterEntryRecorded.v1`, `KmpChanged.v1`, `KmpVacancyOpened.v1`, `DeclarationSubmitted.v1`, `BlueprintGapOpened.v1`, `SorModeChanged.v1`; `in.lawdocs.hr.EmployeeOnboarded.v1`, `EmployeeOffboarded.v1`, `PositionChanged.v1`, `LeaveApproved.v1`, `PayRunApproved.v1`, `PolicyAcknowledged.v1`, `PoshCaseCountChanged.v1` (counts only).

**Cross-product (via `int`; NN-24):** in `ldc_sor` mode LawDocs reads governance facts on demand (`governance.resolution:read`, `governance.kmp:read`; FR-P19-29) and the minimal people projection (`hr.employee:read.minimal`; FR-P19-33); Appendix Y §Y.7.6 proposes letting §6.23 governance events (`BoardMeetingScheduled`, `ResolutionPassed`, `KmpChanged`, `TaskAssigned`) reach the same organisation's legal SoR under an `LDC_SOR` link. In `local_kernel` mode LawDocs emits only internal events. Tenant-internal routing applies: never to the Operations Hub, Equator or another tenant (§6.23 rule 1; NN-19). Payloads never carry PAN, Aadhaar, date of birth, bank account, salary, leave reason or health data (§6.23 rule 3).

### 7.5 Jobs and workflows

`SlaTimerWorkflow` (per request), `RoutingWorker`, `IntakeMailParser`, `CalendarAggregationJob` (every 15 minutes + on events), `LicenceRenewalJob` (daily), `DigestWorkflow` (weekly/monthly), `BlueprintEvaluator` (on change + nightly), `MeetingWorkflow` (notice → minutes clocks), `CircularResolutionWorkflow`, `DeclarationCampaignWorkflow`, `KmpVacancyWatcher`, `DutyTaskGenerator` (daily), `SorSwitchKernelHooks` (export, read-only, archive — invoked by the P19 switch), `PayRunWorkflow`, `LeaveAccrualJob` (monthly), `PoshClockWorkflow` (sealed worker with its own key access), `LdcReconciliationJob` (daily, `ldc_sor` mode).

## 8. Integrations

| Port / adapter | Use | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `GOVERNANCE_SOR_PORT` → `LocalKernel` / `LdcAdapter` | `local_kernel`: kernel reads/writes; `ldc_sor`: read-through governance facts (FR-P19-29) and Appendix Y §Y.7.6 proposals | — | LDC unreachable → dependent actions blocked (FR-P13-24) | Legal drafting continues in the request or matter |
| `HRMS_SOR_PORT` → `LocalKernel` / `LdcAdapter` | `local_kernel`: kernel reads/writes; `ldc_sor`: minimal people projection only (FR-P19-33) | — | As above | — |
| `COMPANY_DATA_PORT` | Director list, DIN status, charges, filing status refresh | Licensed MCA-data vendors (Probe42, Signzy, Surepass, Perfios-Karza — R6 D-15 [VERIFY]) | Show last fetched with date | User entry with evidence |
| `WORKSPACE_PORT` | Teams/Meet links, participant logs, calendars, Teams/Chat intake app, SCIM directory | Microsoft Graph, Google Workspace | Retry; ICS fallback | Manual link |
| `ESIGN_PORT` (P08) | Minutes, declarations, appointment letters, registers extracts | Aggregator ESPs; DSC | Queue | Wet-ink upload with formalities gate (NN-40) |
| E-voting hand-off (file) | General meetings | NSDL, CDSL, KFin Technologies, MUFG Intime [VERIFY formats] | — | Upload results file |
| `ACCOUNTING_PORT` / bank file | Payroll bank file, legal spend export | Bank formats (NEFT bulk), ERP | Download | — |
| `NOTIFY` | Notices proof of delivery (e-mail), reminders, approvals | SES/Brevo; DLT SMS; push | Channel fallback | — |
| `BILLING_PORT` (OH8) | Entitlements (Business/Enterprise), agent seats | — | — | — |

## 9. Settings and configuration (register in Appendix R)

Keys marked **(R)** are already in Appendix R §R.9; the others are new for registration by this phase.

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `lgo.template.adopted` | ENT | ref | — | `ORG_ADMIN` | Y |
| `lgo.intake.enabled` (R) | TEN | bool | true (Business+) | `ORG_ADMIN` | N |
| `lgo.intake.channels` (R) | TEN | menum web/email/teams/gchat | web, email | `ORG_ADMIN` | N |
| `lgo.intake.request_types` (R) | TEN→DEP | list | Appendix T §T.3 seed | `ORG_CLO` | N (publish is maker-checker via `lgo.config`) |
| `lgo.triage.sla_hours` (R) | TEN→DEP | int 1–120 | 24 (overridden per category by `lgo.sla.policies`) | `ORG_CLO` | N |
| `lgo.sla.policies` | TEN | json (P1 floors locked) | Appendix T §T.3 | `ORG_CLO` | Y |
| `lgo.sla.business_calendar` | ENT | ref | entity holidays | `ORG_ADMIN` | N |
| `lgo.assignment.policy` (R) | TEN→DEP | enum manual/round_robin/least_loaded | round_robin | `ORG_CLO` | N |
| `lgo.routing.table` | TEN | ref (decision table) | seed by template | `ORG_CLO` | Y |
| `lgo.selfservice.enabled` | TEN | bool | true for NDA and standard templates | `ORG_CLO` | Y |
| `lgo.selfservice.limits` | TEN | json (value, counterparty risk, template list) | ₹10,00,000; LOW risk; NDA, standard vendor | `ORG_CLO` | Y |
| `lgo.calendar.include_obligations` (R) | TEN | bool | true | `ORG_CLO` | N |
| `lgo.calendar.include_titles` | DEP | bool | false | `ORG_DEPT_HEAD` | N |
| `lgo.clo_dashboard.mandatory_widgets` (R) | BRD | list, LOCKED | legal deadlines, overdue items | — | — |
| `lgo.spend.tracking` (R) | TEN | bool | true | `ORG_CLO` | N |
| `lgo.spend.approval_threshold_inr` (R) | ENT | money | ₹50,000 | `ORG_OWNER` | Y |
| `lgo.counsel_panel.enabled` (R) | TEN | bool | false (P11 `lit.counsel_panel.enabled` follows it) | `ORG_CLO` | N |
| `lgo.doa.matrix` | ENT | json | Appendix T §T.5 | `ORG_CLO` + `ORG_KMP` (CFO) | Y |
| `lgo.licences.default_lead_days` | ENT | int | 60 | `ORG_CLO` | N |
| `lgo.digest.weekly.enabled` | TEN | bool | true (CLO) | `ORG_CLO` | N |
| `lgo.digest.board_monthly.enabled` | TEN | bool | false | `ORG_CLO` + `ORG_KMP` (CS) | Y |
| (mode) — no P13 key; read `int.eco.ldc.sor_mode.governance` (P19, X-11) | TENANT | enum `LOCAL`/`LDC` | `LOCAL`; set only by the P19 switch | ORG_ADMIN (maker), ORG_OWNER (checker) via P19 workflow | Y |
| `gov.board.min_meetings_per_year` (R) | PLT | int | 4 (s.173(1)) | `PLT_LEGAL_REVIEWER` | Y |
| `gov.board.max_gap_days` (R) | PLT | int | 120 (s.173(1)) | `PLT_LEGAL_REVIEWER` | Y |
| `gov.board.notice_min_days` (R) | PLT | int | 7 (s.173(3)); a tenant charter may raise it per entity via `gov.board.notice_days_charter` | `PLT_LEGAL_REVIEWER` | Y |
| `gov.board.notice_days_charter` | ENT ↑ | int (≥ platform minimum) | 7 | `ORG_KMP` (CS) | Y |
| `gov.minutes.circulation_days` (R) | PLT | int | 15 (SS-1) [VERIFY para] | `PLT_LEGAL_REVIEWER` | Y |
| `gov.minutes.comment_days` | PLT | int | 7 (SS-1) [VERIFY para] | `PLT_LEGAL_REVIEWER` | Y |
| `gov.minutes.entry_days` (R) | PLT | int | 30 (SS-1; s.118) [VERIFY para] | `PLT_LEGAL_REVIEWER` | Y |
| `gov.agm.deadline_months` (R) | PLT | int | 6 after FY end (s.96(1)) | `PLT_LEGAL_REVIEWER` | Y |
| `gov.circular.response_days` | ENT | int | 7 [VERIFY SS-1] | `ORG_KMP` (CS) | Y |
| `gov.resolution.numbering` (R) | ENT | ref pattern | `{ENTITY}/BR/{FY}/{SEQ:3}` | `ORG_ADMIN` | N |
| `gov.registers.enabled` (R) | ENT | menum | members, directors and KMP, charges | `ORG_ADMIN` | N |
| `gov.board_portal.director_access` (R) | ENT | enum app/email_pack | app | `ORG_ADMIN` | N |
| `gov.pack.interested_director_access` | ENT | enum VIEW_WITH_BANNER/HIDE | VIEW_WITH_BANNER | `ORG_KMP` (CS) | N |
| `gov.portal.download` | ENT | bool | false | `ORG_KMP` (CS) | N |
| `gov.flag.offline_pack` | ENT | bool | false | `ORG_KMP` (CS) + `ORG_ADMIN` | Y |
| `gov.meeting.transcription` | ENT | bool | false (consent required at join) | `ORG_KMP` (CS) | Y |
| `gov.rulepack.overlays` | ENT | menum | by template (e.g., `gov.rbi_nbfc_2025`) | `ORG_KMP` (CS) | Y |
| `gov.rulepack.overlay_status` | PLT | enum ADVISORY/ACTIVE | ADVISORY until verified (NN-38) | `PLT_LEGAL_REVIEWER` | Y |
| `gov.sod.hard_block_rules` | ENT | list | empty (warnings only) | `ORG_ADMIN` + `ORG_KMP` | Y |
| (mode) — no P13 key; read `int.eco.ldc.sor_mode.hrms` (P19, X-11) | TENANT | enum `LOCAL`/`LDC` | `LOCAL`; set only by the P19 switch | ORG_ADMIN (maker), ORG_OWNER (checker) via P19 workflow | Y |
| `hr.labour_rulepack.version` (R) | PLT | ref (pinned) | latest signed `infrabyx-labour-rulepack` | `PLT_LEGAL_REVIEWER` | Y (NN-30) |
| `hr.monitoring.keylogging` (R) | PLT | bool, LOCKED | false (NN-33) | — | — |
| `hr.monitoring.screenshots_webcam` (R) | PLT | bool, LOCKED | false (NN-33) | — | — |
| `hr.attendance.sessions_for_attendance_only` (R) | PLT | bool, LOCKED | true (CH-32) | — | — |
| `hr.attendance.methods` | ENT | menum | web check-in, WFH declaration | `ORG_HR_ADMIN` | N |
| `hr.attendance.geo_at_checkin` | ENT | bool | false (notice + consent required) | `ORG_ADMIN` | Y |
| `hr.employees.max` (R) | PLN | int | add-on per employee | `PLT_SUPER_ADMIN` | Y |
| `hr.payroll.enabled` (R) | PLN→ENT | bool | false (add-on) | `ORG_ADMIN` | Y |
| `hr.payroll.checker_required` | ENT | bool, LOCKED | true (NN-18) | — | — |
| `hr.leave.auto_approval_rules` | ENT | json | none | `ORG_HR_ADMIN` | N |
| `hr.policy_ack.reminder_days` (R) | ENT | int 1–30 | 7 | `ORG_ADMIN` | N |
| `hr.duties.assignment_notice` (R) | ENT | bool | true | `ORG_ADMIN` | N |
| `hr.posh.enabled` | ENT | bool | true when headcount ≥ 10 | `ORG_ADMIN` | N |
| `hr.posh.ai_assist.enabled` | ENT | bool | false | `ORG_POSH_IC_PRESIDING` | Y |
| `hr.export.restricted_archive` (R) | PLT | bool, LOCKED | true (P20 FR-P20-08) | — | — |
| `agt.autonomy.agent.<code>` (R family) for `AGT_LEGAL_INTAKE_DESK`, `AGT_BOARD_SECRETARY`, `AGT_MINUTES_DRAFTER`, `AGT_RESOLUTION_DRAFTER`, `AGT_ACTION_ITEM_TRACKER`, `AGT_COMPLIANCE_CALENDAR`, `AGT_CLO_CHIEF_OF_STAFF`, `AGT_KMP_BRIEFER`, `AGT_BOARD_PACK_SUMMARISER` | TEN | enum within Appendix H ceilings (FR-P13-61) | L1 | `ORG_CLO` (legal agents) / `ORG_KMP` CS (governance agents) | Y |

## 10. Security, privacy and audit

- **Data classes:** requests CONFIDENTIAL (privileged when legal advice is sought from counsel); board packs, minutes and director annotations BOARD_CONFIDENTIAL (separate key context; director annotations private to the director); UPSI items step-up MFA and access log; HR records `HR` class (salary, bank, leave reasons, health never in events or logs — NN-32); POSH sealed (`hr_posh`, own KMS key, IC-only).
- **Threats and controls:** cross-tenant leakage (RLS, IDOR tests per endpoint, NN-01); RM over-reach (delivery grants, transparency log, NN-17); tampering with minutes and registers (sealed hashes, append-only event store, no edit for any role, NN-02, NN-09); unauthorised master-data changes by staff (maker-checker with client approval and notification, CH-26, NN-18); surveillance creep (no capture of prohibited monitoring data — schema tests, NN-33); director data over-collection (minimisation; PAN masked; no Aadhaar — NN-04).
- **DPDP:** the company is fiduciary for employee and director data; LawDocs is processor; employee processing notice from the template; legitimate-use basis for employment purposes where applicable [VERIFY DPDP s.7 clause for employment] and consent where not; rights requests routed to the tenant; retention per HR kernel schedules with legal hold override.
- **Audit:** every request transition, triage decision, conversion, SLA pause, DoA change, meeting step, notice proof, attendance confirmation, quorum event, minutes acceptance per sentence, sealing, register entry, declaration, KMP change, payroll run approval, POSH access (inside the seal, visible to the Presiding Officer) is a ledger event in the same transaction (NN-45).

## 11. AI touchpoints and guardrails

| Touchpoint | Agent | Autonomy | Human confirmation | Evaluation |
|---|---|---|---|---|
| Intake triage and routing proposal | `AGT_LEGAL_INTAKE_DESK` | L2 | Human for P1/sensitive; requester can override category | Category accuracy ≥ 90%; zero auto-closures of P1 |
| Self-service answers | `AGT_LEGAL_INTAKE_DESK` | L1 (answers from approved knowledge with citations) | Escalation button always present | Citation validity 100%; refusal tests for advice |
| Agenda and pack assembly | `AGT_BOARD_SECRETARY` | L2 | CS approves and issues | Missing-paper detection recall ≥ 95% |
| Minutes draft | `AGT_MINUTES_DRAFTER` | L1 | CS accepts each sentence; chair signs | 0 invented attendance/votes on 100 synthetic meetings |
| Calendar and chasers | `AGT_COMPLIANCE_CALENDAR` | L3 (internal reminders) | Filing always human | Due-date accuracy vs rule engine 100% |
| Director questions | Vidhi (portal) | L0 | Private to director | Source-citation check |
| HR letters and policy answers | Vidhi | L1 | HR maker approves letters | — |

Agents cannot issue notices, seal minutes, record votes, approve, sign or file (NN-13, NN-43); legal statements cite sources or show "unverified" (NN-14); kill switch per agent (NN-39); no training on customer data (NN-15).

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p13/*.feature`)

```gherkin
Feature: Legal intake desk

  @P13-AT-01
  Scenario: Business user raises a request in three clicks
    Given a user in Sales on any Company workspace page
    When the user clicks "Request legal help", picks "Contract review — third-party paper" and submits with an attachment
    Then request LD-LRQ-2026-000101 is created with SLA timers from the category policy

  @P13-AT-02
  Scenario: Sensitive request is never auto-triaged
    Given a request text mentions "court summons received"
    When AGT_LEGAL_INTAKE_DESK proposes category and priority
    Then the request is routed to a human triager with priority P1
    And no automatic resolution is possible

  @P13-AT-03
  Scenario: Self-service NDA within guardrails, escalation outside
    Given self-service limits allow the company NDA template for LOW-risk counterparties
    When a user generates an NDA without editing locked clauses
    Then the request closes as SELF_SERVED with the NDA in the vault
    When another user edits the confidentiality clause
    Then the request converts to a legal review request

  @P13-AT-04
  Scenario: SLA pauses only for permitted reasons and never for statutory clocks
    Given request R-7 is linked to a P11 reply clock due 30 Nov 2026
    When the assignee sets WAITING "waiting on requester"
    Then the request SLA pauses but the P11 clock keeps running

  @P13-AT-05 @NN-18
  Scenario: Approval within DoA, maker cannot approve
    Given the DoA requires CLO approval for contracts between Rs 10 lakh and Rs 1 crore
    When the maker who drafted a Rs 40 lakh contract tries to approve it
    Then approval is refused with LD-LGO-007 and routed to the CLO

Feature: Governance modes

  @P13-AT-06 @NN-47
  Scenario: LDC is system of record when linked
    Given entity "Alpha Finance Ltd" has int.eco.ldc.sor_mode.governance = LDC
    When the CS opens Board & Governance › Meetings in LawDocs
    Then LawDocs deep-links to the LDC meeting planner with single sign-on
    And no row is written to the local gov schema

  @P13-AT-07
  Scenario: LDC unavailable blocks finalising actions
    Given int.eco.ldc.sor_mode.governance is LDC and LDC is unreachable
    When the legal maker marks a share-purchase agreement executed and the formalities gate needs the board approval
    Then the action is refused with LD-GOV-013 and the agreement stays in its current state

  @P13-AT-08 @NN-12
  Scenario: Switch to LDC reconciles sealed minutes before cutover
    Given 24 sealed minutes exist locally
    When the P19 switch reaches IMPORTING and DUAL_RUNNING
    Then LDC holds 24 sealed minutes with byte-identical hashes before CUTOVER and gov screens in LawDocs are read-only with deep links

Feature: Meetings and minutes

  @P13-AT-09
  Scenario: Board meeting cadence warning
    Given the last board meeting was on 1 Jul 2026
    When the CS plans the next one on 5 Nov 2026
    Then the planner warns that the gap exceeds 120 days (s.173(1))

  @P13-AT-10
  Scenario: Shorter notice requires the urgency path
    When the CS issues notice 3 days before the meeting
    Then the system requires the urgency ground and the independent-director presence or ratification path
    And minutes cannot be sealed until ratification is recorded where required

  @P13-AT-11
  Scenario: VC attendance checklist
    Given two directors attend by video conference
    Then the CS must complete the roll-call checklist for each before the quorum monitor counts them

  @P13-AT-12 @NN-02 @NN-09
  Scenario: Sealed minutes cannot be altered by anyone
    Given minutes of the board meeting of 5 Oct 2026 are SEALED
    When a Super Admin calls PATCH on the minutes
    Then the request is refused and audited
    And a correction is possible only as an annotation referencing the next meeting's minutes

  @P13-AT-13 @NN-43
  Scenario: Minutes writer cannot invent attendance or votes
    Given the attendance register shows 5 directors present
    When AGT_MINUTES_DRAFTER drafts minutes
    Then the draft lists exactly those 5 directors and the votes recorded in the conduct console
    And every sentence is marked draft until the CS accepts it

  @P13-AT-14
  Scenario: Circular resolution referred to a meeting
    Given a board of 6 directors and a circular resolution circulated
    When 2 directors require that it be decided at a meeting
    Then the circulation stops and an agenda item is created for the next meeting

  @P13-AT-15
  Scenario: Meeting-only matter blocked from circulation
    When the CS circulates a resolution to approve financial statements
    Then the action is refused with LD-GOV-005 citing s.179(3)

  @P13-AT-16
  Scenario: Follow-on filing task from a special resolution
    When a special resolution is passed on 10 Nov 2026
    Then an MGT-14 filing task is due on 10 Dec 2026 with the rule citation and verification badge
    And the task can be closed only with an SRN entered by a user

Feature: Directors, KMP and duties

  @P13-AT-17
  Scenario: KMP vacancy clock
    When the CFO's cessation is recorded on 1 Dec 2026
    Then a vacancy clock due on 1 Jun 2027 is created under s.203(4) and the blueprint shows AT_RISK

  @P13-AT-18
  Scenario: Duties follow the position
    Given duty "Authenticate financial statements" is attached to position "CFO"
    When a new CFO is appointed to the position
    Then the duty's recurring tasks move to the new holder without reassignment

Feature: Finance company structure

  @P13-AT-19
  Scenario: Adopt NBFC-ML template and customise
    Given a new tenant selects "NBFC — Middle Layer"
    When the admin adopts the Appendix T template and renames "Collections & Recovery" to "Recoveries"
    Then departments, committees and functionaries are created with lines of defence
    And the statutory mapping of the renamed department is preserved by ID

  @P13-AT-20 @NN-38
  Scenario: RBI overlay is advisory until verified
    Given gov.rulepack.overlay_status is ADVISORY
    Then blueprint lines from gov.rbi_nbfc_2025 show "Advisory — verify" and create tasks but no hard blocks

  @P13-AT-21
  Scenario: Segregation-of-duties warning
    When the same person is assigned Head of Credit and Chief Risk Officer
    Then an AT_RISK blueprint line cites the SoD rule and notifies the CS and CLO

Feature: HRMS

  @P13-AT-22 @NN-33
  Scenario: No surveillance data can be captured
    Then the hr schema and APIs contain no fields or endpoints for keystrokes, mouse activity, screenshots, webcam images, browsing history or continuous location

  @P13-AT-23
  Scenario: Wage base 50 percent rule
    Given total remuneration Rs 1,00,000 with excluded allowances Rs 60,000
    When payroll computes the statutory wage base with the current labour pack
    Then Rs 10,000 is added back and the wage base is Rs 50,000

  @P13-AT-24 @NN-19
  Scenario: POSH content stays sealed
    Given an IC case exists
    When a non-IC HR admin searches, exports or asks Vidhi about it
    Then no case content is returned and only counts appear in reports
    And no event leaves the tenant with case content

Feature: Export

  @P13-AT-25 @NN-11
  Scenario: Governance and HR export folders
    When the company exports everything
    Then "05 Board and Governance/FY 2026-27/Board Meetings/2026-10-05 - Board Meeting 3 of FY 2026-27/" contains notice, agenda, papers, attendance and sealed minutes PDF
    And "07 People and HR/Employees [R]/" contains EMP-number folders with appointment letters and no POSH case files
    And POSH case files are produced only as the separately encrypted "POSH Internal Committee [R]" archive requested by the ORG_POSH_IC_PRESIDING of that IC
```

NN test files: `NN-01_lgo_gov_hr_scope.spec.ts`, `NN-02_minutes_and_registers_immutable.spec.ts`, `NN-09_sealed_minutes_hash.spec.ts`, `NN-13_agents_cannot_issue_or_seal.spec.ts`, `NN-17_rm_delegated_maker_grant.spec.ts`, `NN-18_payroll_and_doa_maker_checker.spec.ts`, `NN-19_governance_events_tenant_internal.spec.ts`, `NN-24_ldc_sor_contract_only.spec.ts`, `NN-33_no_surveillance_schema.spec.ts`, `NN-38_overlay_advisory.spec.ts`, `NN-40_formalities_gate_minutes.spec.ts`, `NN-45_audit_same_tx.spec.ts`, `NN-47_kernel_not_forked.spec.ts` (CI checks kernel package integrity against `docs/kernels.lock`).

## 13. Exit gate, deliverables and open items

**Deliverables:** `lgo` module; kernel mounts for `gov`, `hr`, `hr_posh` with pinned versions; LDC SoR adapters (certified against LDC sandbox); setup wizard and Appendix T templates as seed data (YAML/JSON, §T.8); intake categories, SLA policies, routing seeds; DoA seeds; Legal Department Charter template; board-pack and minutes templates (from kernel library, tenant-copyable); duty catalogue; dashboards; report definitions (LGO-01 intake and SLA, LGO-02 workload outcomes, LGO-03 spend by department, GOV-01 meetings and minutes clocks, GOV-02 blueprint gaps, GOV-03 resolutions and follow-ons, HR-01 headcount by department/establishment, HR-02 leave, HR-03 payroll register summary, HR-04 POSH counts); user guides (CLO, CS, director portal, HR admin, employee) and tutorial scripts ("Raise a legal request", "Run a board meeting end to end", "Set up your NBFC structure").

**Exit checklist:**
1. All `@P13-AT-*` scenarios and NN tests green.
2. Pilot A (LawDocs-only private company, 80 employees): 100 requests through the desk; one board meeting from planning to sealed minutes; one AGM notice pack; one month of payroll on the labour pack; one POSH IC set up with an annual-report draft.
3. Pilot B (NBFC-ML on LDC): mode `ldc_sor` with zero local governance/HR rows; formalities-gate checks served from LDC governance facts; deep links verified for every P13 menu; one switch rehearsal (`local_kernel` → `ldc_sor`) on a sandbox tenant with a clean reconciliation report.
4. Template adoption tested for startup, private company, listed company, LLP, NBFC-BL/ML/UL and HFC.
5. Every statutory rule used in pilots VERIFIED or advisory-badged and logged (NN-38).
6. WCAG 2.2 AA / IS 17802 audit of SCR-P13-03, -06, -07, -15, -16, -23, -25 (complaint form) (NN-28).
7. Settings registered (Appendix R); help keys `hlp.lgo.*`, `hlp.gov.*`, `hlp.hr.*` registered.
8. **Export-map entries registered (NN-11):** `lgo.request`, `lgo.request_event`, `lgo.category`, `lgo.licence`, `lgo.doa_version`, `lgo.duty_assignment`, `lgo.digest`; `gov.meeting`, `gov.agenda_item`, `gov.pack`, `gov.attendance`, `gov.minutes`, `gov.resolution`, `gov.register_entry`, `gov.officer_role`, `gov.declaration`, `gov.blueprint_snapshot`; `hr.person`, `hr.employment`, `hr.position`, `hr.department`, `hr.leave_record`, `hr.attendance_record`, `hr.pay_run`, `hr.payslip`, `hr.document`, `hr.acknowledgement`, `hr_posh.case` (IC-only export). Paths (Appendix K §K.3.1 governs — X-07): `05 Board and Governance/{<Entity>/}<FY>/{Board Meetings, Committee Meetings/<Committee>, General Meetings, Resolutions by Circulation, Filings}/<YYYY-MM-DD> - …/`, `05 Board and Governance/Registers/` (statutory registers, incl. directors and KMP, in prescribed layouts + PDF extracts); `06 Policies and Registers/` (DoA matrix versions, Legal Department Charter) and `06 Policies and Registers/Licences and Permits/`; `07 People and HR/Employees [R]/EMP-<number>/…` (ids only in names), `Departments and Positions.xlsx`, `Duties and Delegations.xlsx`, `Policy Acknowledgements.xlsx`, `Payroll [R]/<FY>/`; `07 People and HR/POSH Internal Committee [R]/` never in an owner, admin or auditor export — produced only on request of `ORG_POSH_IC_PRESIDING` as a separately encrypted archive (Appendix K `hr_posh_case` row); `09 Services and Engagements/Legal Requests (internal)/<FY>/<YYYY-MM-DD> - <Request title> (LD-LRQ-…)/`. In `ldc_sor` mode governance and HR folders are produced by LDC's export (`LDC-EXPORT-1.0`) and referenced from the LawDocs README.
9. Demo script: setup wizard (NBFC-ML) → request from Sales → triage → convert to contract → board item auto-suggested → meeting with VC attendance → minutes drafted, accepted, signed and sealed → MGT-14 task → KMP change with vacancy clock → payroll run with checker → POSH IC annual-report count.

**Error codes:** `LD-LGO-001`–`LD-LGO-010` — 001 Category inactive · 002 Required form fields missing · 003 Self-service guardrail exceeded (converted to review) · 004 SLA pause reason not permitted · 005 Conversion target unavailable · 006 Routing rule conflict · 007 Action exceeds your delegation · 008 Licence register is managed in LawDocsComply · 009 Digest to directors needs CLO approval · 010 Duty has no position holder. `LD-GOV-001`–`LD-GOV-014` — 001 Blueprint rule unverified — advisory · 002 Composition rule failed · 003 Notice period shorter than required without urgency path · 004 Quorum not present · 005 Matter cannot be passed by circulation · 006 Interested director cannot vote on this item · 007 Minutes clock breached · 008 Minutes sealed — no edits · 009 Ratification pending · 010 Register entries are event-based — use the source action · 011 Declaration campaign closed · 012 Filing task needs SRN · 013 System of record unavailable — draft only · 014 Mode change blocked while migration runs. `LD-HR-001`–`LD-HR-010` — 001 Labour pack version mismatch · 002 Pay run needs a different checker · 003 Wage payment date beyond statutory limit · 004 Leave below statutory floor · 005 Geo capture needs notice and consent · 006 Prohibited monitoring field · 007 POSH area restricted · 008 Appointment letter missing before joining · 009 Position vacant for regulated role · 010 HR record managed in LawDocsComply. Each with user text and `hlp.<module>.err.<nnn>`.

**Open items (Appendix W):**

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-P13-01 | Appendix Y §Y.7.6 (governance facts and proposals to the same organisation's SoR) and §Y.7.7 (`SystemOfRecordSwitched`) — tracked by P19; SoR keys reconciled by X-11 (`int.eco.ldc.sor_mode.governance` / `.hrms` only; Appendix R to drop `gov.mode`/`hr.mode`); per-legal-entity scoping of the mode (P13 originally ENTITY tier vs P19 TENANT tier) to be confirmed by the Appendix R owner | Integration lead + Appendix R owner | `local_kernel` mode only |
| OI-P13-02 | Kernel extension points needed by `lgo` (duty binding, intake conversions) — request to kernel owners, no fork | Architecture lead | Extension tables only |
| OI-P13-03 | Verify RBI NBFC Governance Directions 2025 title and paragraphs; IT governance, ALM and fraud-risk committee sources after 2025 consolidation | Regulatory analyst | Overlay ADVISORY |
| OI-P13-04 | Verify Companies Act thresholds and rule numbers used in the blueprint seeds (Rules 3, 4, 6, 8, 8A; SS-1/SS-2 paras; MGT-14 list; MR-1 timeline; electronic registers rules) | CS reviewer | Advisory badges |
| OI-P13-05 | Teams/Google Chat intake app publication requirements | Integration lead | Web/e-mail intake |
| OI-P13-06 | Managed Legal Department retainer structure (advocates' firm, invoicing) | [COUNSEL] + [TAX MEMO] | RS-LD-21 OFF |
| OI-P13-07 | DPDP basis for employee processing (s.7 legitimate uses) and employee notice text | DPO + [COUNSEL] | Consent-based notice |
| OI-P13-08 | HR, payroll and POSH role codes `ORG_HR_ADMIN`, `ORG_PAYROLL_MAKER`, `ORG_PAYROLL_CHECKER`, `ORG_POSH_IC_PRESIDING`, `ORG_POSH_IC_MEMBER` registered in Appendix D with their Cerbos policies (in progress at integration review) | Appendix D owner | Assign via `ORG_ADMIN` custom roles carrying the same permissions |
| OI-P13-09 | New ID prefix `lrq_` and business ID `LD-LRQ-…` for conventions §5 | Pack lead | Use as proposed |
| OI-P13-10 | LawDocs-only listed companies: scope of basic disclosure case vs LDC | [OWNER] | Recommend LDC |
