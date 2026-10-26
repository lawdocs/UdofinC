# Phase P18 — Workforce HRMS, Payroll and Internal Controls
> Paste after `01_MASTER_PROMPT.md` (v3.0). **Dependencies (must be complete):** P00 (platform core, audit chain, Ruleset Studio maker-checker, ports, RLS), P01 (identity, workforce SSO with phishing-resistant MFA, `/staff/login`, consent ledger, staff onboarding FR-P01-27), P15 (NN-33 three-tier configuration and settings engine, `cfg` rule packs), P16 (Operations Platform shell `apps/ops`, `eq-portal-ops` client, navigation, notifications). **Consumes:** the Appendix AE `eng` audit register and auditor workspace (created in P00, FR-P00-V3-AE07), P05 ledger and GL export, P09 `WRK_WHISTLE` and POSH sealed desks, P10 `academy` LMS, P14 access-review campaign. **Binding specification:** Appendix Z (this phase implements it; where this file is silent, Appendix Z governs). Estimated effort: 10 sprints (2-week) for a squad of 9 in three sub-squads — People (HR lifecycle, attendance, leave, performance) 4; Payroll 3; Controls 2.

---

## 1. Objective and business outcome

Give Equator Resolution Service Private Limited — and, later, each Infrabyx group company as a separate employing entity — a built-in HRMS, payroll and internal-controls system inside the Operations Platform, designed for staff who mostly work remotely across India, including case managers working from home. It must be lawful under the four Labour Codes, State Shops and Establishments Acts and the Income-tax Act 2025; transparent to employees (NN-35); and resistant to fraud, embezzlement and corruption through delegated authority, maker-checker and separation of duties (NN-36).

| Outcome | Measured at the exit gate |
|---|---|
| Hire to productive in one flow | A requisition approved within budget becomes an e-signed offer and OSH-format appointment letter, pre-joining checks, onboarding checklist, Microsoft 365 account with licence and groups, and Equator platform roles — with no manual step except approvals; joiner checks incomplete = 0 |
| Leaver risk closed in hours | Exit effective → Equator sessions revoked ≤ 60 s, workspace disabled ≤ 4 h, assets and clearance tracked, F&F paid within 2 working days (CoW s.17(2)) in the UAT scenario |
| Lawful, explainable payroll | A month's run for 40 synthetic employees across DL, UP, RJ, MH and KA computes EPF (incl. the September 2026 ₹25,000 split), ESI, PT, LWF and TDS under s.392, produces wage slips, registers, ECR/ESI files, Form 130/138 data and a balanced journal to Tally/Zoho — every line traceable to a dated, sourced parameter version; a run with a `NOT_CONFIRMED` parameter cannot be finalised |
| Transparent measurement | Attendance and work metrics come only from clock-in/out, session logs and platform work items; prohibited monitoring cannot be configured; every employee can see and dispute their own data |
| Fair appraisal | Goals cascade from departments; mid-year and annual cycles with calibration, optional 360, PIP safeguards, increments within budget through maker-checker, acknowledgement and appeal |
| Controls that bite | Self-approval, SoD-conflicting role grants, payments to accounts in cooling-off and runs with unresolved ghost-employee hits are all blocked; anomalies (split transactions, after-hours approvals, round-tripping) raise alerts; the internal auditor works from a read-only workspace with exportable evidence |

---

## 2. Scope (in / out)

**In scope**
- Org model: legal entities, establishments, departments (D3-06 default), cost centres, locations and work-from-home States, positions, grades and bands, reporting lines, matrix and cross-functional assignments, secondments (Appendix AD rules), headcount plan and budget.
- Lifecycle: requisition → recruitment (job posts, candidates, interviews, feedback, offer approval) → offer and appointment letter (OSH s.6(1)(f)) → pre-joining documents and verification → onboarding and policy acknowledgements → assets → work e-mail and access provisioning through `WORKSPACE_PORT` (Microsoft Graph; Google stub; manual fallback) → probation and confirmation → transfers, promotions, role changes, secondments → exit, clearance, access revocation, asset return, F&F, letters, record retention.
- Attendance and work time (NN-35), work measurement and scorecards, utilisation, ROI dashboards with fairness safeguards.
- Leave engine (statutory floor + company policy; State rule packs; holidays; balances; LWP to payroll).
- Payroll engine (structures, wage definition, monthly cycle, statutory components, TDS, arrears, loans, reimbursements, F&F, registers, statutory outputs, accounting journals, specialist-tool exchange, edit log).
- Performance appraisal (OKRs, check-ins, cycles, calibration, 360, PIP, increments, acknowledgement, appeal).
- Learning and certifications (internal LMS space; external ADR training incl. equatoradr.com as a related-party provider), assets, documents vault.
- Internal controls `ctl`: authority matrix/DoFP, maker-checker engine for all modules, SoD matrix, payee/bank-change controls, ghost/duplicate detection, anomaly alerts, expenses, procurement, vendor onboarding with KYC, petty cash, access reviews, COI, gifts register, vigil channel configuration, protected status, exception register, dashboards, internal-audit sampling (`ctl.audit_samples`) and workforce drill-downs inside the Appendix AE auditor workspace (the engagement, evidence and findings register and the evidence export packs are Appendix AE `eng`, X-66(g)).
- Web screens in `apps/ops`; employee self-service on web and mobile (`apps/mobile`).

**Out of scope (do not build here)**
- Private ADR Chambers HR-lite (`chm`) screens and tenant flows — owned by Phase P20 (Appendix W); it **reuses** `packages/rules/payroll` and the leave validator (X-58).
- The `grp` group-company registry, Group Data-Sharing Agreements and shared-services register (Appendix AD / P21); P18 integrates through `grp_company_id`, `shared_services_ref` and `s188_ref` fields and works with Equator as the only entity until P21 lands.
- POSH inquiry and whistle-blower case handling (P09 sealed desks); P18 only configures the internal desk and consumes the opaque protected-status flag.
- Running payroll for third-party tenants as a service; bank host-to-host integration (flag `pay.payout.api.enabled` OFF); actuarial valuation (imported as a file).
- Any statutory filing on a government portal (the system produces files and data; humans file).
- Biometric devices, geofencing and investigation screen capture (built behind OFF flags only where §9 says so).

---

## 3. Personas and permissions touched

| Role code | What it can do in P18 | Key restrictions |
|---|---|---|
| `employee` | Self-service: profile, bank change (with controls), attendance, leave, payslips, tax declarations/proofs, goals, self-review, feedback, claims, COI and gifts declarations, view and dispute own data | Sees only own data; cannot see others' salary or identifiers |
| Line manager (contextual, solid line) | Approve team leave, regularisation, overtime (with consent), claims within limits; reviews; requisitions via department head | Limited team fields (Appendix Z §Z.14.2); never salary except increment proposals for direct reports |
| `department_head` | Requisitions, offers within band, department goals, calibration, approvals per DoFP, department dashboards | Cannot approve own or own-chain requests |
| `hr_executive` | Employee master maker, recruitment admin, onboarding, documents, regularisation bulk | SOD-01 with `payroll_checker` |
| `hr_manager` | HR approvals, letters, probation, exits, PIP HR checks, masked-field reveal with reason | Cannot approve own requests |
| `payroll_maker` | Prepare runs, inputs, variance review, submit | Cannot approve own run (SOD-02) |
| `payroll_checker` | HR-side run approval, ghost-hit resolution, statutory outputs | Cannot release bank file (SOD-03) |
| `finance_controller` | Finance-side run approval, DoFP approvals, GL locks | Network zone office/ZTNA only (App. S §2.6) |
| `finance_ops` | Release bank files, vendor KYC, payee records | Cannot reconcile own releases (SOD-04) |
| `accounts_maker` / `accounts_checker` | Payroll journals, reconciliations | Maker ≠ checker per journal |
| `it_admin` | Execute approved role grants; workspace JML; manual fallback tickets | Cannot approve own access (SOD-08) |
| `compliance_officer` | Rule-pack maker; Payroll Compliance Officer responsibility; statutory clocks; vigil desk configuration | Cannot check own rule-pack version (SOD-10) |
| `dpo` | Monitoring approvals, privacy notices, sensitive-export approvals, DPIAs | — |
| `internal_auditor` | Read-only audit workspace, sampling, findings, evidence export; ghost-hit investigation | No operational role in audited entity (SOD-09) |
| `ops_director` | Department plans, out-of-budget requisitions, aggregate dashboards, calibration oversight | — |
| `group_hr`, `group_admin` | Cross-entity views under purpose-bound grants; entity setup | NN-38; SOD-13 |
| `legal_reviewer` | Sign-off on letter templates, G-tier rule packs affecting employee rights | — |
| `quality_officer` | Sampled QA reviews of case-services work items | Not the employee's maker on that item |
| `auditor` (statutory/external) | Same workspace as `internal_auditor`, time-boxed | ≤ 90 days, scoped |
| Candidate (unauthenticated → candidate portal) | Apply, upload, consent, interview scheduling, offer acceptance | Sees only own application |

---

## 4. Functional requirements

### 4A. Organisation model

**FR-P18-01 — Legal entities and establishments.** CRUD for `hr.legal_entities` (CIN, PAN, TAN, GSTIN, EPF/ESI codes, DoFP resolution reference, optional `grp_company_id`) and `hr.establishments` (State, S&E/OSH/PT/LWF registrations with validity, holiday-calendar code). Entity creation is `group_admin` maker + Company Secretary checker (`compliance_officer` with designation `company_secretary`), CEO designation informed — the same rule as Appendix AD §AD.3 and §AD.15.1, which own entity records once P21 lands *(v3.1)*. Every `hr`/`pay`/`ctl` table carries `legal_entity_id` with entity RLS (FR-P00-V3-Z01). *Acceptance:* a user granted entity A reads zero entity-B rows across the three schemas.

**FR-P18-02 — Departments and cost centres (D3-06).** Seed the 16 default departments with a first-run wizard that requires the HR head to confirm, rename, merge or add before positions can be created; Internal Audit is flagged `independent` and reports outside operations. Cost centres map to the P05 chart of accounts per entity. Rename/merge preserves history; retired departments keep historical assignments.

**FR-P18-03 — Positions, grades and bands.** Positions are budgeted seats (family, grade, band, worker-classification hint, location eligibility, budgeted CTC). Grades G1–G8 and bands (min–mid–max) are tenant data with maker-checker (`HR-BAND-EDIT`). Hires fill positions; vacant positions feed the headcount plan.

**FR-P18-04 — Reporting lines and matrix assignments.** One solid-line manager per employee per date (cycles blocked, `HR_REPORTING_CYCLE`); matrix, project and cross-functional assignments with allocation % (sum ≤ 100) and dotted-line managers; cross-company assignments require a secondment (FR-P18-61). Org chart view (solid and dotted lines) with effective-date slider.

**FR-P18-05 — Headcount plan and budget.** Annual plan by entity × department × cost centre × quarter (positions, budgeted CTC); versioned; approval via `ctl` (`HR-HC-PLAN`); live consumption (filled, offered, open, budget remaining) shown to department heads and finance.

### 4B. Recruitment, offer, pre-joining and onboarding

**FR-P18-06 — Requisitions with budget approval.** Department head raises a requisition against a vacant position or proposes a new one; the engine checks the plan and routes `HR-REQ-IN-BUDGET` or `HR-REQ-OUT-BUDGET` (Appendix Z §Z.4.2, §Z.12.2); > 10% over plan escalates to the CEO designation. Approved requisitions reserve budget.

**FR-P18-07 — Job posts and candidate portal.** Job posts from position templates; publish to the Careers page (`apps/web`, P13) and export text for external boards (manual hand-off; no scraping). Candidate portal on `apps/web`: application with minimal data, CV upload (ClamAV), consent for this vacancy and separate optional consent for future vacancies, DPDP s.5-format notice, status tracking. No questions on religion, caste, marital status or other characteristics not needed for the role (form-schema lint `HR_FORM_PROHIBITED_FIELD` in CI).

**FR-P18-08 — Screening, interviews and feedback.** Structured criteria per position; interview scheduling via `WORKSPACE_PORT.createMeeting` (calendar-backed Teams) or `VIDEO_PORT`; interviewers get time-bound grants to that candidate only; `hr.interview_feedback` is submitted independently against the competency rubric before others' feedback becomes visible. AI may summarise a CV against stated criteria for a human (`requires_human_review = true`); AI never ranks, scores or rejects (Appendix Z §Z.18.5).

**FR-P18-09 — Offer approval and letters.** Offer builder shows the CTC breakdown, CoW s.2(y) wage-base check and minimum-wage check; approval per band rule (`HR-OFFER-ABOVE-BAND`); offer letter and **appointment letter** (OSH s.6(1)(f); prescribed format from OSH (Central) Rules — form number `[VERIFY — open]`) generated from legal-approved templates, e-signed through `ESIGN_PORT`, stored as PDF/A with SHA-256. Existing employees without a letter are listed with the 3-month clock `osh_appointment_letter_existing_3m`.

**FR-P18-10 — Engagement types and misclassification check.** `employee`, `fixed_term_employee`, `apprentice`, `professional_engagement`, `contractor_staff` (Appendix Z §Z.4.4). Creating a `professional_engagement` runs the control/integration checklist and warns when the role looks like employment; practising advocates are never modelled as salaried employees.

**FR-P18-11 — Pre-joining documents and verification.** Checklist per Appendix Z §Z.4.5: ID (Aadhaar only by offline verification with masked reference — NN-14), PAN (encrypted + keyed hash), UAN/ESI IP number, bank account with penny-drop (`KYC_PORT`), education/employment proofs, Form 127, nominations, background verification before access (Q SC-21; criminal-record check only where lawful and specifically consented). The portal explains purpose, basis and retention for each item; optional items never block. Health information is not collected.

**FR-P18-12 — Onboarding checklist and policy acknowledgements.** Department templates generate `hr.onboarding_tasks`: acknowledgements as consent-ledger `undertaking` records (staff code ESC-2026.1 — App. U §U.4; POSH policy and IC details; information security and acceptable use; confidentiality/NDA; employee privacy notice; workforce-measurement notice; anti-bribery and gifts; COI declaration), asset assignment, provisioning, platform role requests (via `ctl` with SoD check and, for case roles, `ConflictIndex` refresh), mandatory training, buddy and 30/60/90 check-ins. Activation (`equator.hr.employee.activated.v1`) is blocked until acknowledgements, worker classification and bank cooling are complete (`HR_POLICY_ACK_PENDING`, `HR_WORKER_CLASSIFICATION_REQUIRED`).

### 4C. Work e-mail and access provisioning

**FR-P18-13 — Workspace connector.** Implement `WORKSPACE_PORT` adapters: `m365_graph` (default; app registration `eq-hrms-provisioner` with `User.Create`, `User.ReadWrite.All`, `LicenseAssignment.ReadWrite.All`, `GroupMember.ReadWrite.All`; certificate credential in Secrets Manager, rotation ≤ 90 days), `google_workspace` (stub, `ops.workspace.google.enabled` OFF; residency warning), `manual_it_desk` (IT ticket with the same checklist and SLA). Capability matrix per SKU hides unsupported actions. Throttling per Graph guidance (`429`/`Retry-After`, low priority for backfills).

**FR-P18-14 — SKU rules and console-role guard.** `tenant.hr.workspace.sku_rules` (default: console/finance/HR/payroll roles → Business Premium; others → Business Basic; contractors → no mailbox). A privileged console role cannot be granted to a user whose SKU lacks Conditional Access and MDM unless a security-lead exception ≤ 90 days exists (`HR_WORKSPACE_SKU_INSUFFICIENT`). The SKU itself is confirmed by the Company Secretary (D3-04); until confirmed, the capability matrix assumes Business Basic.

**FR-P18-15 — JML automation.** `WorkspaceJmlWorkflow` per Appendix Z §Z.5.3: joiner (create user with UPN pattern and transliteration, `usageLocation = IN`, licence, groups for department/location/role, temporary credential to the personal channel only, Keycloak workforce link), mover (group/SKU diff), leaver (X-57 timings; shared-mailbox conversion via PowerShell runner and file transfer at T+1; licence removal; deletion after 90 days through the deletion guard). Every step writes `hr.jml_events` and audit events; `jml_sla_report` collector runs daily.

### 4D. Probation, movements and exit

**FR-P18-16 — Probation and confirmation.** Review task at T-30; outcomes confirm / extend once (≤ 3 months, reasons) / not confirmed; deemed confirmation per setting with an exception logged against the manager; confirmation letter generated. Reminder ladder T-45/30/15/7/0 with pre-filled review packet, escalation to department head and HR, completion by the department head when the manager is on leave, reasons for extension or non-confirmation visible to the employee before the end date, and the "Probations ending in 60 days" tracker (SCR-P18-45) per Appendix Z §Z.4.7. *(v3.1)*

**FR-P18-17 — Lifecycle events.** Effective-dated transfers, promotions, role and grade changes, manager changes, work-mode and work-location-State changes; compensation effects via `HR-COMP-REVISION`; `work_location_state` changes re-evaluate minimum wage, holidays, PT/LWF (D3-31) and require an updated WFH declaration; `role_changed` drives the workspace mover and a targeted access re-certification. Changing the employer of record requires exit and rejoining (`HR_ENTITY_TRANSFER_REQUIRES_REJOIN`).

**FR-P18-18 — Exit initiation and notice.** Resignation via self-service (reason taxonomy, proposed last day); termination via `HR-TERMINATION` chain with worker-classification checks (IR Code for workers) and protected-status check (Appendix Z §Z.12.11); end of fixed term, retirement, death (nominee workflow). Notice computation from contract and State rules; buy-out/waiver with approval.

**FR-P18-19 — Clearance, access revocation and assets.** Parallel clearance tasks (manager hand-over, IT, finance, HR, case re-assignment, legal-hold check); `exit_effective` emits the event that drives X-57 revocations; assets returned with condition; any loss recovery only as a CoW s.18 deduction with prior intimation within the 50% cap.

**FR-P18-20 — Full and final settlement and exit documents.** `FnfWorkflow` (provisional at T-5 working days, final at exit) computes salary, leave encashment (OSH s.32(1)(vi)), notice pay/recovery, pro-rata bonus, reimbursements, arrears, loan recovery within cap, TDS; gratuity on its 30-day clock; payment within 2 working days (`wrk_wages_2wd`); statutory dues never waived (`STATUTORY_WAIVER_FORBIDDEN`, existing Appendix F code). Relieving letter and experience/service certificate (default 7 days), F&F statement acknowledgement, Form 130, record retention class assignment; optional anonymous exit survey (aggregate n ≥ 5).

### 4E. Attendance and work time (NN-35)

**FR-P18-21 — Workforce-measurement notice.** Versioned notice listing every data source with purpose, basis, viewers, retention, self-view and dispute route (Appendix Z §Z.6.1), in English and Hindi; acknowledgement required before capture; adding a source requires DPO approval and re-notice (`HR_MONITORING_APPROVAL_REQUIRED`).

**FR-P18-22 — Clock-in/out, session logs, shifts and rosters.** Web and mobile clock-in/out (offline queue), session-log suggestions confirmed by the employee, shifts and rosters published ≥ 7 days ahead with swap requests; optional office-network check and coarse city at check-in behind notice; geofence and biometric OFF flags. **Prohibited set Locked** (keystroke logging, webcam/face presence, covert or continuous screen recording, personal-device screenshots, off-hours location, personal communications, BYOD personal area, meeting-presence scoring): any attempt returns `HR_MONITORING_PROHIBITED` (403).

**FR-P18-23 — Daily register, hours and overtime.** `AttendanceDailyCloseJob` builds `hr.attendance_days` and Form IX/OSH s.33 registers; rules per Appendix Z §Z.6.3: 8 h/48 h floors, weekly rest (never > 10 consecutive days without rest), ≤ 6 days/week, overtime only for workers with recorded consent (OSH s.27; `HR_OVERTIME_CONSENT_REQUIRED`), 2× rate, rounding, State quarterly cap (`HR_OVERTIME_QUARTERLY_CAP`), women's night-work consent (`HR_NIGHT_WORK_CONSENT_REQUIRED`).

**FR-P18-24 — WFH declarations and regularisation.** Annual/on-change WFH declaration (State, city, safe-workspace self-check, home confidentiality, virtual workplace for POSH); regularisation within the window with manager approval; corrections after freeze become arrears; absence deductions wait for the r.17 intimation and 7-day reply window.

**FR-P18-25 — My time, disputes and retention.** Employees see every captured record with source and retention date and can dispute it; disputes resolve within 5 working days and freeze affected metrics; raw sessions retained 1 year then aggregated; registers 5 years after last entry; no adverse action on telemetry alone.

### 4F. Work measurement, scorecards and ROI

**FR-P18-26 — Work-item ingestion.** Subscribe to events from `cases`, `ops` tickets and onboarding, `mkt` campaigns/content, `grm` and `ctl`; write `hr.work_items` with opaque `subject_ref`, SLA due/met, standard minutes and QA link — no case content or party PII (NN-16). Event-to-action mapping is configuration (`metric_definition` kind).

**FR-P18-27 — Metric definitions and role scorecards.** Seed the Appendix Z §Z.7.2 catalogue; maker-checker on definitions; scorecards (≤ 8 KPIs, target, weight, explain text, data coverage). **Outcome metrics for case staff are rejected** (`HR_METRIC_OUTCOME_FORBIDDEN`): settlement rate, award outcomes, amounts recovered, neutral selection, speed of outcome. Every KPI tile has an Explain panel (formula version, coverage, normalisations, team median at n ≥ 5) and a **Reply** action for the employee (`hr.work_replies`, window 10 working days; shown unedited wherever the figure is shown and attached to probation, calibration and PIP packets) — Appendix Z §Z.7.4. *(v3.1)*

**FR-P18-28 — Quality reviews and feedback.** Random sampling (default 5%, min 3 items/month) assigned to `quality_officer` (cases) or team leads; rubric; reviewer ≠ employee and ≠ the employee's maker on the item; employee can respond. Customer process-satisfaction surveys shown to the employee at n ≥ 5.

**FR-P18-29 — Utilisation and ROI dashboards.** Utilisation vs capacity at team level with wellbeing alerts (> 110%); department and team ROI (fully loaded cost vs weighted output and directly attributable revenue — never case-outcome-linked); individual ROI behind `hr.analytics.individual_roi.enabled` OFF (DPIA); safeguards per Appendix Z §Z.7.6 (normalisation, no protected characteristics, explain panels, n ≥ 5 cohorts, no automated adverse action, pay-equity analysis on the CoW s.2(y) second-proviso basis).

### 4G. Leave

**FR-P18-30 — Leave rule packs and floor validator.** Load OSH s.32 and State packs (DL, UP, RJ, MH, KA; statuses per Appendix Z §Z.2.5); compute the per-employee statutory floor daily; company policies must be ≥ floor for every class and State (`HR_LEAVE_POLICY_BELOW_FLOOR` names the failing class/State).

**FR-P18-31 — Equator Standard and policy features.** Seed templates `leave.equator_standard@2026.1` (D3-32) and `leave.statutory_minimum@2026.1` (same IDs used by chambers, Appendix W §W.6.6), with the State uplift of Appendix Z §Z.8.3 (e.g., Rajasthan earned leave above 18 days); leave types per Appendix Z §Z.8.3 (maternity 26 weeks, 80-day eligibility, ₹3,500 medical bonus, nursing breaks; paternity/bereavement as policy defaults pending management decision); accrual, carry-forward 45 with auto-encashment above, refused-leave carry-forward, sandwich rule, half days, notice, documents, approval chain, written refusal reasons.

**FR-P18-32 — Requests, approvals, balances and calendars.** Request with balance preview; approvals with delegation (leave cover ≤ 30 days); append-only `hr.leave_ledger`; team calendar showing "On leave" without type to peers; State holiday calendars with Locked national holidays and festival swap for remote staff. **Leave planner** (SCR-P18-46): projected team coverage per requested day against `tenant.hr.leave.coverage.*`, up to three alternative windows, blackout windows with reasons, `warn` or `require_second_approval` mode; coverage never blocks maternity, sick, bereavement, statutory or court-ordered leave; coverage refusals carry the reason and are recorded "applied and refused"; annual non-binding leave plan; lapse-risk nudges from 1 October; year-end and separation `floor_true_up` for days-worked floors (Appendix Z §Z.8.3–Z.8.4). An approver applying for ≥ 2 working days' leave must name a cover delegate or choose "route to my approver" (Appendix Z §Z.12.2). *(v3.1)*

**FR-P18-33 — LWP and encashment to payroll.** Approved LWP and post-intimation unauthorised absence feed the input freeze; encashments (year-end, separation) become payroll lines with the OSH timing clocks.

### 4H. Payroll

**FR-P18-34 — Rule-pack loader and run gate.** `cfg` payroll rule packs (Appendix Z §Z.2.4–Z.2.5) materialise into `pay.rule_params`; parameters immutable once approved; intra-period changes pro-rated by calendar day (EPF September 2026 split) with per-parameter override; finalisation blocked on `NOT_CONFIRMED` (`PAY_PARAM_NOT_CONFIRMED`); `SECONDARY_ONLY` acknowledged per run by the Payroll Compliance Officer (`PAY_PARAM_ACK_REQUIRED`); `RuleWatchWorkflow` tasks.

**FR-P18-35 — Components and wage calculator.** Component register with Locked statutory classes and s.2(y) letters; `wage_code_base()` in `packages/rules/payroll` with the MoLE ₹76,000 → ₹22,000 golden test and the Appendix Z §Z.9.13 golden set W01–W14 (EPF full and split month incl. employer EPS/EPF split, ESI, overtime, deduction cap, gratuity, TDS default regime, rebate and marginal relief, PT, LWP, F&F date) *(v3.1)*; structure save and run both enforce the 50% test (`PAY_WAGE_DEFINITION_BREACH`); class locked after use.

**FR-P18-36 — Salary structures and compensation versions.** CTC → components templates per grade; preview (gross, employer contributions, wage base, deductions, net, CTC reconciliation); minimum-wage check on the higher of establishment and work-location State (`PAY_MIN_WAGE_BREACH`; warning-with-acknowledgement where the State schedule is `NOT_CONFIRMED`); effective-dated `pay.employee_compensation` with history; back-dated revisions generate arrears; restructure wizard shows CoSS s.124 and IR Code s.40 checks.

**FR-P18-37 — Pay calendar and input freeze.** Annual calendar with pay date ≤ statutory deadline (before the 7th; CoW s.17(1)); inputs (attendance, leave, OT with consent IDs, joiners/exits, compensation, approved claims, loans, arrears, one-time items, tax data) frozen on the freeze date with a hashed snapshot; late items roll as arrears.

**FR-P18-38 — Calculation, variance review and approvals.** Deterministic calculation with `param_version_ids` and `formula_ref` per line; variance report (headcount, gross, net, employer cost, per-employee > 10%, new bank accounts, same-run hires, exits still paid) with mandatory reasons (`PAY_RUN_VARIANCE_UNREVIEWED`); ghost/anomaly gate; maker submit → HR checker → Finance checker with step-up; DB CHECK that maker, HR checker, Finance checker and releaser are all distinct. **Run checklist and holds (Appendix Z §Z.9.4):** dated checklist from freeze day and pay day with owners and overdue alerts; the variance-rule table with actions (reason, second checker, block, line auto-hold); held lines (`pay.run_line_holds`) excluded from the bank file while the run proceeds, each resolved by D-1 of the statutory deadline by release through an off-cycle run or `cancelled_ghost` with a second reviewer (`PAY_HOLD_PAST_DEADLINE` otherwise); the employee sees "Payment under verification — expected by {date}"; a checker rejection returns the run to `under_review` and voids earlier approvals. *(v3.1)*

**FR-P18-39 — Bank file, payout and payslips.** Bank-specific bulk file generated only from the approved run; SHA-256 stored; release by `finance_ops` (≠ checkers); bank acknowledgement import reconciled line by line (`PAY_BANK_FILE_HASH_MISMATCH` on mismatch); payments to accounts in cooling-off blocked; Form V-style payslips (English/Hindi) on or before payment; optional `PAYOUT_PORT` route OFF. *v3.1:* failed or returned lines are never re-sent from the original file — each becomes a `bank_return` line hold, re-paid only through an off-cycle run after account re-verification; `DisbursalAckWatchJob` alerts when no acknowledgement arrives 3 working days after the pay date (Appendix Z §Z.9.4 stage 10). *Acceptance:* re-uploading the original file after a return is refused; the off-cycle run carries only the returned lines *(v3.1)*.

**FR-P18-40 — Statutory contributions and returns data.** EPF/EPS/EDLI (ceiling, rates, VPF, voluntary higher wages, IW, EPS membership rule), ESI (threshold and rates), PT per State (February rule; ₹2,500 annual cap), LWF per State, gratuity provision, bonus (blocked while ceilings `NOT_CONFIRMED` unless a dated professional opinion is recorded), overtime, deductions guard (50% cap with carry-forward schedule; fines and damage deductions need evidence objects). Outputs: EPF ECR, ESI file, PT and LWF returns data, challan data, liability ageing alerts before due dates, challan-to-run reconciliation.

**FR-P18-41 — TDS on salary (Income-tax Act 2025 s.392).** Regime election per employee per tax year (default regime; lock after window); Form 124 declarations and proofs windows; Form 127 intake; monthly re-estimation with standard deduction, employer NPS (s.124), s.156 rebate with marginal relief, cess and surcharge from the pack; outputs Form 130 (by 15 June), Form 123 where salary > ₹1,50,000, Form 138 quarterly data (due dates `[NC]`). No regime recommendation; neutral side-by-side computation on request; disclaimer on every tax screen.

**FR-P18-42 — Arrears, loans, advances and reimbursements.** Arrears via re-run with historical parameter versions; loans/advances with `PAY-LOAN` approval, schedules and recovery within the cap, receivable for any residual; reimbursements flow from `ctl.expense_claims` with `route = payroll` and tax treatment by component class.

**FR-P18-43 — Registers, outputs and portability.** Form I, IV, IX, V, VII and OSH s.33 registers; unclaimed-dues tracking (3/6-month deposit, 7-year hold); all exports in the NN-37 package convention (XLSX + PDF + CSV/JSON + manifest with checksums).

**FR-P18-44 — Payroll accounting, exchange and edit log.** Balanced payroll journals by cost centre into `core.ledger_journals` and the P05 Tally/Zoho export (locked periods blocked, `PAY_GL_PERIOD_LOCKED`); recharge tags for secondees; `PAYROLL_EXCHANGE_PORT` (`generic_csv`) for specialist tools with a difference report before posting; `*_history` edit logs and pgaudit on `pay`/`ctl` with Critical alert on any trigger disable (r.3(1) proviso). Every computation screen and file cover shows `pay.disclaimer.computation`.

### 4I. Performance appraisal

**FR-P18-45 — Goals and OKRs.** Department objectives (approved by `ops_director`) cascade to team and individual goals with weights, targets, evidence links and due dates; agreement within 30 days of cycle start or joining; outcome-linked goals for case staff blocked.

**FR-P18-46 — Check-ins, feedback and cycles.** Monthly check-ins; optional peer feedback (anonymous aggregates n ≥ 3); recognition; probation, mid-year and annual cycles per Appendix Z §Z.10.2; self-review → manager review → optional 360 (≥ 3 raters) → calibration → release → acknowledgement → appeal.

**FR-P18-47 — Calibration and PIP safeguards.** Calibration committee per department with written reasons for every change and a fairness panel (distribution by gender and by work mode at n ≥ 5); forced distribution OFF; PIP creation blocked unless prior expectations, a recorded check-in on the gap, HR completeness review (disputes resolved, leave/illness/accommodation/workload considered) and protected-status check exist (`HR_PIP_SAFEGUARD_MISSING`); PIP minimum 60 days, fortnightly reviews, employee responses. Calibration screen views per Appendix Z §Z.10.3: distribution against guidance, manager lens with leniency flag (n ≥ 5), evidence completeness (reviews below 60% move at most one step), fairness panel including employees who took maternity, long sick or disability-related leave, side-by-side comparison, change log; a reason citing approved leave cannot lower a rating (`HR_RATING_REASON_PROHIBITED`). *(v3.1)*

**FR-P18-48 — Increments, bonuses, acknowledgement and appeal.** Merit matrix within an approved budget (`HR-INCREMENT-BUDGET`); manager proposals → HR band/budget check → department head → `finance_controller` total → CEO designation above budget; approved changes become compensation versions with e-signed letters; acknowledgement (≠ agreement); appeal within 15 days to a reviewer outside the line; decision with reasons within 21 days; second-level appeal for ratings tied to adverse action.

### 4J. Learning, assets and documents vault

**FR-P18-49 — Learning and certifications.** Internal catalogue in the `academy` LMS internal space: mandatory modules with deadlines and annual refresh; role curricula; external ADR training providers listed (≥ 3, X-29 principle) including equatoradr.com, operated by Infrabyx Consultancy (OPC) Pvt Ltd — purchases are flagged related-party and linked to the `grp` shared-services register/s.188 reference; certifications register with expiry reminders and role prerequisites (`HR_CERTIFICATION_REQUIRED`); no accreditation claim without a Claims Register record (NN-17).

**FR-P18-50 — Assets and documents vault.** Asset register and assignments (MDM enrolment and encryption status; loss → session revoke, wipe, incident); documents vault with High tier, per-category access, watermarked downloads, no bulk download without `EXPORT-SENSITIVE` approval; POSH and whistle-blower material never stored (opaque hold flag only).

### 4K. Internal controls (`ctl`, NN-36)

**FR-P18-51 — Authority matrix and DoFP.** `ctl.authority_rules` with action × entity × scope × amount band × chain × conditions; seed the Appendix Z §Z.12.2 values marked "Proposed — subject to Board approval"; the first live use of any financial row requires a Board resolution reference (G tier); `ctl.resolve_authority()` returns the chain for any request; delegations ≤ 30 days, depth 1, never above the delegator's limit; escalation after 2 working days of inaction. Leave-linked delegation (`LeaveDelegationJob`, Appendix Z §Z.12.2): auto-created from the approved leave request, active 00:00 IST on the first leave day, ends with the leave, "on behalf of" label, unplanned-absence routing to the delegator's approver after 1 working day, same-role-only delegation for payroll-checker and finance-release steps. *(v3.1)*

**FR-P18-52 — Maker-checker engine for all modules.** `CtlService.request()` / `assertApproved()` with payload digest re-verification at execution (`CTL_PAYLOAD_CHANGED`); approver ≠ maker and distinct approvers (DB trigger; `CTL_SELF_APPROVAL_BLOCKED`); no approval where the approver has a declared conflict (`CTL_APPROVER_CONFLICTED`); step-up for money and privileged actions; network-zone rule for finance approvals; expiry (14 days). Integrations in this phase: HR (requisition, offer, compensation, termination, loans), payroll (runs, off-cycle, F&F), billing (refunds, write-offs, payout releases — FR-P05-V3-Z06), procurement, expenses, payee/bank changes, privileged role grants, sensitive exports, allocation overrides (record-only for App. N decisions).

**FR-P18-53 — Separation-of-duties matrix.** Seed SOD-01…SOD-15 (SOD-15: approver of a payment cannot reconcile it — *v3.1*); evaluated at role grant (DB trigger across modules, including pending grants) and at transaction time; `CTL_SOD_CONFLICT` on conflict; compensating-control exceptions need CEO designation approval, a named compensating control and expiry ≤ 90 days; tenants may add rules but not remove seeded ones.

**FR-P18-54 — Payee and bank-detail change controls.** Unified `ctl.payees` for employees, vendors and petty cash; changes only via the payee's MFA session or with in-app confirmation; penny-drop/name-match (`CTL_PENNY_DROP_MISMATCH`); cooling-off default 3 working days (1–7; floor Locked); out-of-band notifications to registered e-mail/phone and the previous account's channel with a "This wasn't me" freeze link; pre-run freeze 5 days unless `finance_controller` approves; duplicate-account check across all payees (`CTL_DUPLICATE_BANK_ACCOUNT`); payments in cooling blocked (`CTL_COOLING_OFF_ACTIVE`).

**FR-P18-55 — Ghost-employee and duplicate detection.** `GhostEmployeeScanJob` weekly and in every run implementing GH-01…GH-10; DB unique index on active PAN hash per tenant; Critical hits block finalisation (`PAY_GHOST_HITS_UNRESOLVED`); dismissals need a reason and a second reviewer; investigations assigned to `internal_auditor` or `hr_manager`.

**FR-P18-56 — Anomaly alerts.** `AnomalyDetectionJob` implementing AN-01…AN-17 as data-driven rules (thresholds T tier; loosening needs `internal_auditor` acknowledgement); alerts to owners and the exceptions dashboard; Critical to `internal_auditor` and `compliance_officer`; deterministic only. **Rules library (SCR-P18-47, Appendix Z §Z.12.7):** versioned rules with `shadow` / `alert` / `block` modes; new or loosened rules run ≥ 30 days in shadow and are promoted by `compliance_officer` with `internal_auditor` as checker; dispositions on every alert; weekly tuning report (volume, precision, time to disposition; flags precision < 10% over 90 days or > 50 alerts a week); per-subject suppressions with reason and expiry ≤ 90 days. *(v3.1)*

**FR-P18-57 — Expenses, procurement, vendors and petty cash.** Expense claims with receipts (above ₹500), image-hash duplicate check, policy checks and `EXP-CLAIM` approval, settlement via payroll or AP; procurement PR → quotations (≥ 3 above ₹5,00,000) → PO (`PROC-PO`) → receipt by a different person → 3-way match (2% tolerance) → `PAY-VENDOR`; legal review above ₹10,00,000; vendor onboarding with PAN/GSTIN/Udyam/bank verification, sanctions screening for foreign vendors, COI check, DPA where personal data is processed, TDS profile, related-party flag (`CTL_VENDOR_KYC_INCOMPLETE` blocks POs); petty cash imprest with custodian, caps, vouchers and independent monthly reconciliation.

**FR-P18-58 — Access reviews, COI and gifts.** `AccessReviewCampaign` scope extended to `apps/ops` (quarterly) and privileged payroll/finance/IT/group roles (monthly) with SoD re-evaluation and auto-revoke after 10 working days; COI declarations at joining, annually and on change (per group entity for multi-company staff) feeding `ConflictIndex` and the approval engine (`CTL_COI_UNDECLARED`); gifts register (no gifts from parties — Locked; vendor/partner gifts above ₹1,000 declared within 7 days).

**FR-P18-59 — Vigil channel and protected status.** Configure the internal `WRK_WHISTLE` desk (P09) for Equator staff with anonymous and confidential named reporting; `ctl.vigil.statutory_mode` derived from CS-owned applicability facts (listed / public deposits / borrowings > ₹50 crore — Companies Act s.177(9)–(10), r.7) adding Audit Committee chair access when ON; consume the opaque `ctl.protected_status` flag from sealed services: adverse actions against a protected employee require an additional independent reviewer and are reported as counts only, with no reason shown in HR.

**FR-P18-60 — Exception register, dashboards and internal-audit workspace.** `ctl.exceptions` (reason ≥ 30 characters, higher-authority approval, expiry, compensating control); monthly report to the CEO designation and quarterly to the Board/Audit function; exception dashboards per Appendix Z §Z.12.13; internal-audit workspace screens over the Appendix AE `eng` register (plans, engagements, evidence requests, findings with management responses and follow-up in `eng.audit_plans`, `eng.audit_engagements`, `eng.evidence_requests`, `eng.audit_findings`, `eng.management_responses`; access via `eng.auditor_grants`; X-66(g)), with reproducible sampling in `ctl.audit_samples` and evidence export through the Appendix AE §AE.8.4 packs (`STATUTORY_BOOKS`, `ASSURANCE_PACK`; Appendix AC §AC.13 taxonomy) incl. audit-trail reports, read-only and watermarked (`CTL_AUDIT_WORKSPACE_READ_ONLY`).

### 4L. Group companies and secondment

**FR-P18-61 — Secondments.** `hr.secondments` with host entity, dates, time %, control clause, lien and termination with employer (CHECK), recharge basis, shared-services and s.188 references, GST-review status and signed letter (Appendix AD); cross-company assignments > 0% blocked without it (`HR_SECONDMENT_RECORD_REQUIRED`); payroll, EPF and ESI only in the employing entity; host sees work-related fields only; recharge schedules feed `grp` invoicing; one active employment per PAN within the group without a secondment (`HR_DUPLICATE_ACTIVE_EMPLOYMENT`); multi-employment option OFF pending PF advice.

**FR-P18-62 — Cross-entity access and ethical walls.** `group_hr` grants purpose-bound, ≤ 90 days, maker-checker, logged per access under the GDSA (NN-38); users with Finbyx/Udofin roles cannot hold Equator case roles for matters involving those companies' clients (role-grant check + annual attestation); group dashboards aggregate only.

### 4M. Self-service, privacy and audit

**FR-P18-63 — Employee self-service hub.** `/me` on web and mobile: profile, documents, payslips, tax, leave, attendance, goals and reviews, claims, assets, training, declarations, "My data" (every HR, attendance and metric record with source, viewers and retention) with dispute and DSR links; bank changes web-only with step-up.

**FR-P18-64 — Privacy notices and lawful-basis register.** Employee privacy notice (s.5 format, English/Hindi) bundled with the appointment letter and candidate portal, naming group entities and purposes; lawful-basis register per Appendix Z §Z.18.1; consent for optional items with withdrawal propagation ≤ 15 min; retention classes per §Z.18.3 registered in `core.retention_classes`; legal hold overrides; DSR workflow (P14) covers HR data with HR-specific exemptions recorded.

**FR-P18-65 — Field-level RBAC and audit.** Cerbos policies and RLS implementing Appendix Z §Z.14 (managers' limited fields; HR-only identifiers; masked by default with reason + step-up reveal logged in `audit.access_log`; `HR_FIELD_NOT_VISIBLE`); every action in `hr`/`pay`/`ctl` writes NN-22 audit events; evidence collectors per Appendix Z §Z.18.4.

---

## 5. Workflows and state machines

### 5.1 Employee lifecycle
`candidate_accepted → pre_joining → onboarding → probation → confirmed ⇄ (on_notice | suspended | on_secondment | long_leave) → exit_initiated → exit_effective → settled → archived` — guards and events per Appendix Z §Z.4.1. Temporal: `EmployeeLifecycleWorkflow` (one per employee; signals for each transition; timers for probation review T-30, appointment-letter clock, service-certificate clock).

### 5.2 Requisition → offer
| State | Trigger | Next | Notes |
|---|---|---|---|
| `draft` | Department head submits | `pending_approval` | Budget check result attached |
| `pending_approval` | `ctl` approval | `approved` / `rejected` | Chain from `HR-REQ-IN-BUDGET` or `HR-REQ-OUT-BUDGET` |
| `approved` | Job post published | `sourcing` | Budget reserved |
| `sourcing` | Candidate selected | `offer_drafted` | Feedback complete from all panel members |
| `offer_drafted` | Offer approval | `offer_approved` | `HR-OFFER-ABOVE-BAND` if applicable |
| `offer_approved` | Offer sent via `ESIGN_PORT` | `offer_sent` | Expiry default 7 days |
| `offer_sent` | Candidate e-signs | `filled` (→ employee `candidate_accepted`) | Declined/expired → `sourcing` |
| any | Withdrawn | `closed` | Budget released |

### 5.3 Pay run
`draft → inputs_open → inputs_frozen → calculated → under_review → maker_submitted → hr_approved → finance_approved → released → bank_confirmed → closed`; before `released` any state may go to `cancelled` (reason); after `released` only reversal/arrears. Guards: `inputs_frozen` needs attendance close and approvals cut-off; `maker_submitted` needs zero unreviewed variances, zero unresolved Critical ghost hits, zero `NOT_CONFIRMED` parameters and SECONDARY_ONLY acknowledgement; `hr_approved` and `finance_approved` need distinct checkers with step-up; `released` needs a releaser distinct from maker and checkers and a bank file whose hash matches; `bank_confirmed` needs the bank acknowledgement reconciled. Clock `pay_monthly_wage_deadline` alerts at D-5, D-3, D-1 (configurable) before the 7th. Rejection at `hr_approved` or `finance_approved` → `under_review` (approvals voided). Line holds run in parallel: `held → released → paid_offcycle` or `held → cancelled_ghost` (second reviewer), deadline D-1 of the statutory deadline; a run may reach `closed` with lines in `paid_offcycle` but not with any line still `held` *(v3.1)*.

### 5.4 Approval request (`ctl`)
`pending → (approved | rejected | expired | withdrawn)`; `approved → executed` only via `assertApproved()` with a matching payload digest; escalation timer per step (2 working days); expiry 14 days. Each step records approver, decision, `acr`, network zone and comment. When the step's approver is on approved leave the step is reassigned to the active leave delegate (or, without one, to the approver's own approver) before the escalation timer starts, so leave never consumes the SLA; the step records both the delegator and the acting delegate *(v3.1)*.

### 5.5 Bank-detail change
`requested → verifying (penny-drop) → (mismatch_review | cooling) → active`; any state → `frozen` on "This wasn't me" → `security_review`; pre-run freeze holds `cooling → active` until the run closes unless `finance_controller` approves. Notifications at `requested` (registered e-mail, phone, previous account's channel) and at `active`.

### 5.6 Exit and F&F
`exit_initiated → clearance_in_progress → exit_effective → fnf_provisional → fnf_approved → fnf_paid → documents_issued → archived`. Clocks: `wrk_wages_2wd` from the separation event; `osh_leave_encash_2wd`; `coss_gratuity_30d`; `service_certificate` (7 days); X-57 revocation timers. Undisputed F&F amounts are never held back for a dispute or for incomplete clearance; recoveries follow CoW s.18.

### 5.7 Leave request
`draft → submitted → (approved | rejected_with_reason | withdrawn) → taken → (cancelled_after_approval → reversed)`. Rejections are recorded as "applied and refused" for OSH s.32 carry-forward; approval delegation for cover. At `submitted` the coverage check runs: in `warn` mode the approver sees the projection; in `require_second_approval` mode a breach adds the department head as a second approver; protected leave types skip the check; a `rejected_with_reason` on coverage grounds must offer an alternative window *(v3.1)*.

### 5.8 PIP
`proposed → hr_safeguard_check → (blocked | active) → review_n … → (successful | extended_once | unsuccessful)`; `unsuccessful` hands off to the disciplinary or termination workflow; protected-status adds `independent_review` before `active` and before any adverse outcome.

### 5.9 Workspace JML
Joiner: `queued → user_created → licensed → mailbox_ready → groups_set → credential_sent → linked` (manual fallback mirrors steps as checklist items). Leaver: `queued → disabled_and_revoked (≤ 4 h) → groups_removed → mailbox_converted (T+1) → files_transferred → licence_removed → delete_pending (90 days) → deleted | held`.

---

## 6. Screens and UX (web + mobile)

All screens live in `apps/ops` (desktop-first, keyboard-complete, WCAG 2.2 AA, English and Hindi), with loading, empty, error (problem `code` + `traceId`) and success states. Tier badges (L/G/T) on every settings field (P15). Sensitive screens show a watermark with user and time.

**Routes** *(v3.1)*: Operations Platform routes are host-relative on `ops.equatorresolution.in` (Appendix AG D3-47(a)). Read each `/ops/x` route below as `/x` (for example `/hr/employees`, `/pay/runs/:id`, `/controls/authority`, `/me/pay`); the `/ops/...` forms are kept here for traceability and 301 to the canonical path (FR-P16-V31-AG01). Exceptions: SCR-P18-43 is `/audit/workforce` (a tab of SCR-P16-41, AG §AG.0.5 #3), and SCR-P18-36 is the `ctl` source view of the Work Inbox (AG §AG.0.5 #5).

| ID | Route | Roles | Purpose | Key elements |
|---|---|---|---|---|
| SCR-P18-01 | `/ops/org/entities` | `group_admin`, `hr_manager` | Entities and establishments | Registrations with expiry chips, holiday calendar, DoFP reference |
| SCR-P18-02 | `/ops/org/structure` | HR, department heads | Departments, cost centres, org chart | D3-06 first-run wizard banner "Default structure — confirm before use", solid/dotted lines, effective-date slider |
| SCR-P18-03 | `/ops/org/positions` | HR, finance | Positions, grades, bands | Budgeted CTC, status, worker-classification hint |
| SCR-P18-04 | `/ops/org/headcount` | HR, finance, department heads | Headcount plan and budget | Plan vs filled/offered/open, approval status |
| SCR-P18-05 | `/ops/hr/requisitions` | Department heads, HR | Requisitions | Budget check panel, approval chain preview |
| SCR-P18-06 | `/ops/hr/recruitment` | HR, interviewers (grant) | Pipeline board | Stages, candidate cards (minimal data), feedback completeness |
| SCR-P18-07 | `/careers/*` (apps/web) | Candidates | Careers page and candidate portal | Job post, application, consent toggles, status |
| SCR-P18-08 | `/ops/hr/offers/:id` | HR, approvers | Offer builder | CTC breakdown, wage-base and minimum-wage checks, approval chain, letter preview |
| SCR-P18-09 | `/ops/hr/prejoin/:id` | HR, candidate | Pre-joining checklist | Item purpose/basis/retention, verification status, BGV flags only |
| SCR-P18-10 | `/ops/hr/onboarding/:id` | HR, manager, IT, employee | Onboarding checklist | Acknowledgements, assets, provisioning status, role requests with SoD results |
| SCR-P18-11 | `/ops/hr/employees` | HR | Employee directory | Filters by entity, department, State, work mode, status; masked identifiers |
| SCR-P18-12 | `/ops/hr/employees/:id` | HR (full), manager (limited) | Employee 360 | Tabs: profile, job, assignments, compensation (HR), documents, attendance, leave, performance, assets, history |
| SCR-P18-13 | `/ops/hr/movements` | HR, managers | Lifecycle events | Effective-dated change forms with impact preview (pay, holidays, PT, workspace groups) |
| SCR-P18-14 | `/ops/hr/secondments` | HR, `group_hr` | Secondments | Required clauses checklist, recharge basis, s.188/shared-services refs, GST review flag |
| SCR-P18-15 | `/ops/hr/exits/:id` | HR, manager, IT, finance | Exit and clearance | Clocks (2 working days, 4 h, 30 days), clearance tasks, F&F preview |
| SCR-P18-16 | `/ops/it/provisioning` | `it_admin` | Workspace JML console | Queue, step status, SLA, manual fallback tickets, SKU guard results |
| SCR-P18-17 | `/ops/time/today` | Employees, managers | Clock-in/out and team status | One-tap clock, session suggestions to confirm, team presence (status only) |
| SCR-P18-18 | `/ops/time/rosters` | Team leads | Shifts and rosters | Publish ahead, swaps, OT consent indicators, night-work consent indicators |
| SCR-P18-19 | `/ops/time/regularisations` | Managers, HR | Regularisation queue | Window countdown, bulk approve (HR) |
| SCR-P18-20 | `/ops/time/overtime` | Managers, HR | Overtime | Consent evidence, quarterly cap meter by State |
| SCR-P18-21 | `/ops/me/data` | Employee | My data and disputes | Every record with source, viewers, retention; dispute button |
| SCR-P18-22 | `/ops/work/scorecards` | Employee (own), manager (team), HR | Scorecards | KPIs with explain panel and data coverage; QA reviews; feedback aggregates |
| SCR-P18-23 | `/ops/work/capacity` | Managers, department heads | Utilisation vs capacity | Team heatmap, wellbeing alerts |
| SCR-P18-24 | `/ops/analytics/roi` | `ops_director`, department heads, finance | ROI dashboards | Department/team views; individual tab hidden while flag OFF; explain panels; cohort-size guard |
| SCR-P18-25 | `/ops/leave` | Employees, managers | Leave requests and balances | Balance preview, calendar, approval inbox |
| SCR-P18-26 | `/ops/settings/leave-policies` | HR (T), compliance (G packs) | Leave policies and packs | Floor validator results by class/State, template chooser |
| SCR-P18-27 | `/ops/settings/payroll-params` | `compliance_officer`, CS | Rule packs and parameters | Status badges (VERIFIED / SECONDARY_ONLY / NOT_CONFIRMED), source links, effective dates, diff and preview against last run |
| SCR-P18-28 | `/ops/pay/structures` | HR, payroll | Components and structures | Statutory class, 50% test, minimum-wage check |
| SCR-P18-29 | `/ops/pay/runs/:id` | Payroll, finance | Pay-run cockpit | Stage stepper, inputs freeze, variance review, ghost/anomaly gate, approvals, bank file hash, acknowledgement reconciliation, disclaimer |
| SCR-P18-30 | `/ops/pay/statutory` | `payroll_checker`, compliance | Statutory outputs | ECR/ESI/PT/LWF files, challans, due-date clocks, Form 130/123/138 data |
| SCR-P18-31 | `/ops/me/pay` | Employee | Payslips and tax | Payslips (EN/HI), regime election, Form 124 declarations/proofs, Form 130 download |
| SCR-P18-32 | `/ops/pay/fnf/:id` | HR, payroll, finance | F&F | Line-by-line computation with parameters, clocks, approvals, statement |
| SCR-P18-33 | `/ops/performance` | Employees, managers, HR | Goals, check-ins, reviews | Cascade tree, cycle tasks, acknowledgement, appeal |
| SCR-P18-34 | `/ops/performance/calibration/:cycle` | Calibration committee | Calibration | Distribution, fairness panel (n ≥ 5), change reasons |
| SCR-P18-35 | `/ops/performance/increments/:cycle` | Managers, HR, finance | Increment cycle | Merit matrix, budget burn, approval chain |
| SCR-P18-36 | `/ops/controls/approvals` | All approvers | Approval inbox | Payload summary + digest, authority source, SoD/COI checks, step-up. *v3.1:* `ctl` source view of the Work Inbox; delegated items show "On behalf of {delegator} until {date}"; without an item ID the route 302s to `/inbox?source=ctl` |
| SCR-P18-37 | `/ops/controls/authority` | CS, finance (G) | Authority matrix and DoFP | "Proposed — subject to Board approval" banner until resolution reference entered; simulation tool |
| SCR-P18-38 | `/ops/controls/sod` | Security lead, compliance | SoD matrix and violations | Rules, blocked attempts, exceptions with expiry |
| SCR-P18-39 | `/ops/controls/payees` | Finance, HR | Payees and bank changes | Cooling timers, penny-drop results, duplicate warnings, freeze events |
| SCR-P18-40 | `/ops/controls/spend` | Employees, approvers, finance | Expenses, procurement, vendors, petty cash | Claim builder with receipt capture, PR/PO/receipt/invoice match, vendor KYC checklist, petty-cash book |
| SCR-P18-41 | `/ops/controls/exceptions` | Management, compliance | Exceptions and alerts dashboard | Tiles per Appendix Z §Z.12.13; drill-down by RBAC |
| SCR-P18-42 | `/ops/controls/declarations` | Employees, compliance | COI and gifts | Annual declaration wizard, per-entity sections, gifts register |
| SCR-P18-43 | `/audit/workforce` *(v3.1; was `/ops/audit`)* | `internal_auditor`, `auditor` | Internal-audit sampling and workforce/controls drill-down (the auditor read-only workspace itself is Appendix AE §AE.8.3) | Sampling (seed shown) from `ctl.audit_samples`; links to AE engagements, evidence requests, findings and §AE.8.4 export packs |
| SCR-P18-44 | `/ops/learning` | Employees, HR | Learning and certifications | Mandatory modules, external providers (≥ 3; related-party label), certificate register |
| SCR-P18-45 | `/ops/hr/probations` | HR, managers, department heads | Probation tracker *(v3.1)* | Ending in 60 days, overdue reviews, reminder stage, outcome and letters, bulk reminder |
| SCR-P18-46 | `/ops/leave/planner` | Employees, managers | Leave planner and coverage *(v3.1)* | Team coverage heatmap, blackout windows, alternative-window suggestions, annual plan, lapse-risk list |
| SCR-P18-47 | `/ops/controls/anomaly-rules` | `compliance_officer`, `internal_auditor` | Anomaly rules library *(v3.1)* | Rule versions and modes, shadow reports, tuning metrics, suppressions with expiry, promotion approvals |

**Pay-run cockpit additions (SCR-P18-29, v3.1):** checklist rail (item, owner, due, status), variance table grouped by rule with bulk "apply reason to selected lines" (reason text required per rule, never blank), held-lines tab with deadline countdown and "release to off-cycle" / "confirm not payable" actions, and keyboard shortcuts `J`/`K` (next/previous flagged line), `R` (add reason), `H` (hold/release, with confirmation). *(v3.1)*

**Mobile (`apps/mobile`, employee space):** SCR-P18-M01 clock-in/out with offline queue; M02 leave request and balances (with a coverage projection for the employee's own team shown as counts only, never others' leave types) *(v3.1)*; M03 approvals inbox (leave, regularisation, claims within limits — money approvals above ₹50,000 and pay runs are web-only); M04 payslips; M05 claims with receipt camera capture (image hash computed on device); M06 My data and disputes; M07 goals and check-ins. Mobile never shows other employees' salary, bank or identifiers; screenshot protection on payslip and claim screens (P12 pattern).

**Copy rules.** Measurement notice headline: "What we record about your work, and why." Payroll disclaimer per Appendix Z §Z.9.12. No screen uses "productivity score"; scorecards are labelled "Work summary". Locked settings show "Fixed by law or platform policy" with the source.

---

## 7. Backend design

### 7.1 Modules
New NestJS bounded contexts in `apps/api`: `hr` (org, lifecycle, recruitment, attendance, leave, performance, learning, assets, vault index, work items), `pay` (rule-param read model, components, structures, compensation, runs, statutory, tax, F&F, journals, registers) and `ctl` (authority, approvals, SoD, payees, spend, vendors, alerts, exceptions, declarations, audit workspace). Pure libraries: `packages/rules/payroll` (wage base, statutory contributions, TDS, gratuity, leave encashment, F&F — X-58), `packages/rules/leave` (floor computation and validator), `packages/rules/ctl` (authority resolution, SoD evaluation, anomaly rules). UI in `apps/ops`. No cross-module DB access: `pay` reads `hr` through published services; `ctl` is called through `CtlService`.

### 7.2 Tables (new; key columns; DDL sketches in Appendix Z §Z.16; all with `tenant_id`, `legal_entity_id`, tenant + entity RLS, `std_cols`, retention columns where personal data)
- **Org:** `hr.legal_entities` (cin, pan_enc, tan, gstin, epf_code, esi_code, grp_company_id, dofp_resolution_ref); `hr.establishments` (state_code, se/osh/pt/lwf registrations, holiday_calendar_code); `hr.departments` (parent_id, head_employee_id, cost_centre_id, independent); `hr.cost_centres` (code, gl_mapping); `hr.positions` (grade, band, budgeted_ctc_minor, status); `hr.grades`, `hr.bands`; `hr.headcount_plans` (version, lines jsonb, approval_request_id).
- **People:** `hr.employees` (+ `_history`) (employee_no, person_id, engagement_type, status, establishment_id, work_location_state, work_mode, worker_classification, department_id, position_id, manager_employee_id, pan_enc/pan_hmac, uan_enc/uan_hmac, aadhaar_ref_masked); `hr.worker_classifications` (answers jsonb, rule_applied, reviewed_at); `hr.assignments` (kind, allocation_pct, dotted_manager_id, host_entity_id, secondment_id); `hr.secondments`; `hr.lifecycle_events` (kind, effective_on, payload jsonb, approval_request_id).
- **Recruitment and onboarding:** `hr.requisitions`, `hr.job_posts`, `hr.candidates` (consent_ids, retention_class `hr_candidate`), `hr.applications`, `hr.interviews`, `hr.interview_feedback` (competency scores jsonb, submitted_at), `hr.offers`, `hr.appointment_letters` (document_id, sha256, esign_ref, issued_on), `hr.prejoin_checks` (item, status, evidence_document_id, basis), `hr.onboarding_tasks`, `hr.probation_reviews`.
- **Exit:** `hr.exits` (type, initiated_on, last_working_day, reason_code, approval_request_id), `hr.exit_clearances` (area, owner, status).
- **Workspace:** `hr.workspace_accounts` (provider, external_id, upn, sku, status), `hr.jml_events` (step, requested_at, completed_at, provider_ref, sla_met; append-only).
- **Time:** `hr.attendance_sessions` (partitioned), `hr.attendance_days`, `hr.shifts`, `hr.rosters`, `hr.wfh_declarations`, `hr.regularisation_requests`, `hr.overtime_consents`, `hr.night_work_consents`, `hr.monitoring_approvals`, `hr.measurement_notices` (version, sources jsonb), `hr.data_disputes`.
- **Work and performance:** `hr.work_items` (partitioned), `hr.metric_definitions`, `hr.kpi_scorecards`, `hr.qa_reviews`, `hr.goals`, `hr.checkins`, `hr.feedback`, `hr.review_cycles`, `hr.reviews`, `hr.calibrations`, `hr.pips`, `hr.appeals`.
- **Leave:** `hr.leave_types`, `hr.leave_policies` (template, version, rules jsonb, floor_validation jsonb), `hr.leave_requests`, `hr.leave_ledger` (append-only).
- **Learning and assets:** `hr.learning_assignments` (academy course ref, due_on, completed_on), `hr.certifications`, `hr.assets`, `hr.asset_assignments`, `hr.vault_index` (document_id, category, access_policy).
- **Payroll:** `pay.rule_params`, `pay.components`, `pay.structure_templates`, `pay.employee_compensation` (+ `_history`), `pay.bank_accounts`, `pay.regime_elections`, `pay.tax_declarations`, `pay.tax_proofs`, `pay.prev_employment`, `pay.runs`, `pay.run_inputs` (snapshot_sha256), `pay.run_lines` (append-only), `pay.payslips`, `pay.variance_items`, `pay.bank_files` (sha256, ack_sha256, status), `pay.statutory_challans`, `pay.statutory_returns`, `pay.loans`, `pay.loan_schedules`, `pay.arrears`, `pay.fnf_settlements`, `pay.gratuity_provisions`, `pay.bonus_runs`, `pay.journal_batches`, `pay.registers`, `pay.param_acknowledgements` (run_id, param_version_id, acknowledged_by), `pay.run_line_holds` (append-only; run_line_id, hold_status, reason_code, owner_role, deadline_at, decided_by, second_reviewer) *(v3.1)*.
- **v3.1 additions (HR and controls):** `hr.work_replies` (employee_id, period, kpi_code, text, evidence_refs; append-only), `hr.leave_coverage_rules` (team_ref, min_on_duty_pct, min_headcount_by_role jsonb, blackout_windows jsonb, mode), `ctl.anomaly_rules` (rule_id, version, mode, parameters jsonb, owner, review_due, change_request_id), `ctl.alert_dispositions` (alert_id, disposition, decided_by, decided_at), `ctl.alert_suppressions` (rule_id, subject_ref, reason, expires_at ≤ 90 days); `ctl.delegations` gains `reason` (`manual`, `leave`, `unplanned_absence`) and `leave_request_id`; `hr.probation_reviews` gains `reminder_stage`. *(v3.1)*
- **Controls:** `ctl.authority_rules`, `ctl.delegations`, `ctl.approval_requests`, `ctl.approval_steps`, `ctl.sod_rules`, `ctl.sod_violations`, `ctl.payees`, `ctl.bank_change_requests`, `ctl.vendors`, `ctl.vendor_kyc`, `ctl.purchase_requests`, `ctl.purchase_orders`, `ctl.goods_receipts`, `ctl.expense_claims`, `ctl.expense_lines` (receipt_document_id, image_sha256), `ctl.petty_cash_floats`, `ctl.petty_cash_entries`, `ctl.anomaly_rules`, `ctl.alerts`, `ctl.exceptions`, `ctl.coi_declarations`, `ctl.gifts_register`, `ctl.protected_status`, `ctl.audit_samples` (seed, population_query_hash, `engagement_id → eng.audit_engagements`). Audit engagements, evidence requests, findings and management responses are the Appendix AE `eng` tables (§AE.11.2, created in P00); `ctl.audit_engagements`, `ctl.evidence_requests` and `ctl.audit_findings` are v3.0 read-only compatibility views only (X-66(g)).
- **Reused:** `core.consent_records` (undertakings; Appendix F name), `core.holiday_calendars`, `core.retention_classes`, `core.ledger_journals`, `core.role_grants`, `eng.access_reviews` (moved from `ops` by X-65), `audit.audit_events`, `audit.access_log`.

### 7.3 APIs (`/v1/ops`; OpenAPI 3.1; problem+json; cursor pagination; Idempotency-Key on every POST that creates money, people, approvals or provisioning)
| Method and path | Purpose | Roles | Notes |
|---|---|---|---|
| `GET/POST/PATCH /org/entities`, `/org/establishments` | Entity and establishment admin | `group_admin`, `hr_manager` | Creation via `ctl` approval |
| `GET/POST/PATCH /org/departments`, `/org/cost-centres`, `/org/positions` | Structure | HR | — |
| `POST /org/headcount-plans` · `POST /org/headcount-plans/{id}/submit` | Plan and approval | Department heads, HR | `HR-HC-PLAN` |
| `POST /hr/requisitions` · `POST /hr/requisitions/{id}/submit` | Requisition | Department heads | Budget check in response |
| `POST /hr/job-posts` · `POST /hr/job-posts/{id}/publish` | Posts | HR | — |
| `POST /public/careers/{post}/applications` | Candidate application | Public (rate-limited, CAPTCHA) | Consent IDs required |
| `POST /hr/interviews` · `POST /hr/interviews/{id}/feedback` | Interviews | HR, interviewers (grant) | Feedback hidden until own submitted |
| `POST /hr/offers` · `POST /hr/offers/{id}/send` | Offer | HR | `ESIGN_PORT` envelope |
| `GET/PATCH /hr/employees/{id}` | Employee record | HR; manager (filtered) | Field-level policy |
| `POST /hr/employees/{id}/classification` | Worker classification | HR | Pure function trace returned |
| `POST /hr/employees/{id}/lifecycle-events` | Movements | HR, managers | Impact preview `?dryRun=true` |
| `POST /hr/secondments` | Secondment | HR, `group_hr` | Signed document required |
| `POST /hr/exits` · `POST /hr/exits/{id}/effective` | Exit | HR, employee (resignation) | Emits `exit_effective` |
| `GET /hr/workspace/accounts` · `POST /hr/workspace/jml/{id}/retry` · `POST /hr/workspace/jml/{id}/manual-complete` | Provisioning | `it_admin` | Evidence upload for manual |
| `POST /hr/attendance/clock` · `GET /hr/attendance/days` | Attendance | Employees; managers (team) | Offline batch supported |
| `POST /hr/attendance/regularisations` · `POST /hr/attendance/overtime-consents` · `POST /hr/attendance/wfh-declarations` | Time requests | Employees | — |
| `POST /hr/me/disputes` · `GET /hr/me/data` | Own data | Employee | — |
| `GET /hr/scorecards/{employeeId}` · `POST /hr/qa-reviews` | Measurement | Employee/manager; QA | Outcome-metric guard |
| `GET /hr/analytics/roi` | ROI | `ops_director`, department heads, finance | `level=individual` 403 while flag OFF |
| `POST /hr/leave/requests` · `POST /hr/leave/requests/{id}/decision` · `GET /hr/leave/balances` | Leave | Employees, managers | Reason required on reject |
| `POST /hr/leave/policies` · `POST /hr/leave/policies/{id}/validate` | Policies | HR | Floor report |
| `POST /hr/performance/goals` · `/checkins` · `/reviews` · `/calibrations` · `/pips` · `/appeals` | Performance | As §3 | PIP safeguard check |
| `GET/POST /pay/rule-params` (via `cfg` change requests) | Parameters | `compliance_officer`, CS | G-tier flow |
| `POST /pay/components` · `POST /pay/structures` · `POST /pay/structures/{id}/preview` | Structures | HR, payroll | 50% test, minimum wage |
| `POST /pay/compensation` | Compensation version | HR | `HR-COMP-REVISION` |
| `POST /pay/runs` · `POST /pay/runs/{id}/freeze` · `/calculate` · `/variances/{vid}/reason` · `/submit` · `/approve` · `/release` · `/bank-ack` | Pay run | Payroll, finance | Distinct-actor CHECKs; step-up |
| `GET /pay/runs/{id}/payslips` · `GET /pay/me/payslips` | Payslips | Payroll; employee | — |
| `POST /pay/me/regime` · `POST /pay/me/declarations` · `POST /pay/me/proofs` | Tax | Employee | Windows enforced |
| `GET /pay/statutory/{kind}` | ECR, ESI, PT, LWF, Form 130/123/138 data | `payroll_checker` | NN-37 package |
| `POST /pay/loans` · `POST /pay/fnf/{exitId}/compute` · `/approve` | Loans, F&F | HR, payroll | — |
| `POST /pay/journals/{runId}` · `POST /pay/exchange/export` · `POST /pay/exchange/import` | Accounting and exchange | Accounts, payroll | Difference report on import |
| `POST /ctl/approvals` · `POST /ctl/approvals/{id}/decision` · `GET /ctl/approvals/inbox` | Approvals | Modules; approvers | Digest re-verified on execution |
| `GET/POST /ctl/authority-rules` · `POST /ctl/authority-rules/simulate` | Authority | CS, finance | Board ref for financial rows |
| `POST /ctl/delegations` | Delegation | Approvers | ≤ 30 days |
| `GET /ctl/sod/check?userId&role` | SoD pre-check | `it_admin`, HR | Used by role-grant UI |
| `POST /ctl/payees/{id}/bank-changes` · `POST /ctl/bank-changes/{id}/freeze` | Bank changes | Payee, HR/finance; public freeze link (signed token) | Cooling, OOB |
| `POST /ctl/expense-claims` · `/purchase-requests` · `/purchase-orders` · `/goods-receipts` · `/vendors` · `/petty-cash/entries` | Spend | As §3 | KYC gate |
| `GET /ctl/alerts` · `POST /ctl/alerts/{id}/resolve` · `POST /ctl/exceptions` | Alerts, exceptions | Owners, compliance | Second reviewer on dismissal |
| `GET/POST /ctl/anomaly-rules` · `POST /ctl/anomaly-rules/{id}/promote` · `GET /ctl/anomaly-rules/tuning-report` · `POST /ctl/alert-suppressions` *(v3.1)* | Rules library | `compliance_officer` (maker), `internal_auditor` (checker) | Shadow ≥ 30 days before `alert` |
| `POST /pay/runs/{id}/lines/{lineId}/hold` · `/release` · `/confirm-not-payable` *(v3.1)* | Line holds | `payroll_maker` (hold); owner (release); `internal_auditor` + second reviewer (not payable) | Deadline guard `PAY_HOLD_PAST_DEADLINE` |
| `POST /hr/me/work-replies` · `GET /hr/leave/coverage?team&from&to` · `GET /hr/probations?endingWithinDays=60` *(v3.1)* | Reply, coverage projection, probation tracker | Employee; employees and managers; HR and managers | Reply immutable after save |
| `POST /ctl/declarations/coi` · `POST /ctl/gifts` | Declarations | Employees | — |
| `GET/POST /ctl/audit/samples` (owned here) · `/ctl/audit/engagements`, `/evidence-requests`, `/findings` as facades over `/v1/eng/audit-engagements`, `/v1/eng/audit-findings` (Appendix AE §AE.12.1) · exports via `POST /v1/exports` (`STATUTORY_BOOKS`, `ASSURANCE_PACK`) | Audit workspace | `internal_auditor`, `auditor` | Read-only on operational data |

### 7.4 Domain events
As listed in Appendix Z §Z.17.2 (contexts `hr`, `pay`, `ctl`); published through the transactional outbox; internal bus only (never tenant webhooks); payloads carry IDs and codes only — never salary, bank or identifier values. Consumers: `WorkspaceJmlWorkflow` (`hr.employee.activated|role_changed|exit_effective`), identity (Keycloak revocation within 60 s), `pay` (lifecycle and leave events), `ctl` (all money and role events for anomaly rules), `reporting` (aggregates only). *v3.1:* the leave-driven cover consumers listed in Appendix Z §Z.17.2 (S §6.4, K §5.10, N §2.2, O §7.6, Q §2.4, AG §AG.4.5, P08, P09, W) read only `equator.hr.leave.request_decided|started|ended|cancelled.v1`, whose payloads never carry the leave type or reason.

### 7.5 Temporal workflows and jobs
`EmployeeLifecycleWorkflow` · `RequisitionWorkflow` · `OfferWorkflow` (expiry timer) · `PreJoiningWorkflow` (BGV vendor callbacks) · `OnboardingWorkflow` · `WorkspaceJmlWorkflow` (per-step retries; manual fallback signal) · `ProbationReviewWorkflow` · `ExitWorkflow` (X-57 timers) · `FnfWorkflow` (2-working-day clock) · `AttendanceDailyCloseJob` (02:00 IST) · `LeaveAccrualJob` (monthly) · `LeaveYearEndJob` (carry-forward, encashment) · `PayRunWorkflow` (stage signals, deadline timers) · `TdsReEstimationJob` (monthly) · `StatutoryDueDateWorkflow` (ECR, ESI, PT, LWF, TDS clocks) · `RuleWatchWorkflow` · `AppraisalCycleWorkflow` · `PipWorkflow` · `IncrementCycleWorkflow` · `BankChangeWorkflow` (cooling timer, OOB) · `ApprovalEscalationJob` · `LeaveDelegationJob` (daily 00:00 IST + on leave events; v3.1) · `PayLineHoldDeadlineJob` (hourly; v3.1) · `AnomalyTuningReportJob` (weekly; v3.1) · `GhostEmployeeScanJob` (weekly + per run) · `AnomalyDetectionJob` (streaming on outbox) · `AccessReviewCampaign` (extended scope) · `CertificationExpiryJob` · `WorkspaceDeletionGuardJob` · `RetentionJob` (HR classes) · `EvidenceCollectors` (`jml_sla_report`, `payroll_run_controls`, `ghost_scan_results`, `sod_matrix_check`, `monitoring_prohibited_check`, `statutory_clock_report`).

---

## 8. Integrations (ports and adapters)

| Need | Port / adapter | Default provider | Failure behaviour |
|---|---|---|---|
| Work e-mail, licences, groups, meetings | `WORKSPACE_PORT` (new) — `m365_graph`, `google_workspace` (OFF), `manual_it_desk` | Microsoft 365 (SKU to be confirmed; designed for Business Basic) | No automatic failover (identity is stateful); step retried with backoff; after 3 failures a manual IT ticket is opened with the SLA clock still running |
| Appointment letters, offers, F&F statements, secondment letters | `ESIGN_PORT` | Leegality (P06) | Envelope pending; no auto-acceptance; re-create manually on provider outage |
| Penny-drop and PAN/GSTIN/Udyam verification | `KYC_PORT` | Licensed aggregator (App. S §3.5–3.11) | Manual verification with evidence upload; payee stays `pending_verification` |
| Background verification | `KYC_PORT` (`bgv` capability) | BGV vendor under DPA | Manual report upload; access remains blocked until pass |
| Notifications and out-of-band confirmations | `EMAIL_PORT`, `MESSAGING_PORT`, `PUSH_PORT` | SES, MSG91/Gupshup, Expo | Fallback channel; bank change stays in cooling until at least one OOB channel delivers |
| Payroll payout | `PAYOUT_PORT` — `bank_file` adapter (default; shared with chambers, Appendix W §W.6.10) and provider API adapter behind `pay.payout.api.enabled` OFF | Bank bulk file uploaded by `finance_ops` | API failure falls back to a regenerated bank file with a new hash |
| Accounting | P05 GL export through `ACCOUNTING_PORT` (Appendix AC; `tally_file`, `zoho_books`) | Per entity | Export batch fails as a whole; no partial posting |
| Specialist payroll tool | `PAYROLL_EXCHANGE_PORT` (new) — `generic_csv` | None by default | Import rejected with row-level difference report |
| Sanctions screening for foreign vendors | `SANCTIONS_PORT` | Existing provider | PO blocked until screened |
| LMS | `academy` internal space (P10) | Built-in | External provider certificates uploaded manually |
| Whistle-blower and POSH | P09 sealed desks (internal service) | Built-in | Protected-status flag only crosses the boundary |
| Interview and internal meetings | `WORKSPACE_PORT.createMeeting` or `VIDEO_PORT` | Teams (calendar-backed) / LiveKit | Fall back to `VIDEO_PORT`; hearings never on Teams |

---

## 9. Configuration surface

The full catalogue with tiers is Appendix Z §Z.15. Items this phase must make editable (with the P15 tier badge and approval rules):

| Item | Tier | Default | Guardrail |
|---|---|---|---|
| Monitoring prohibited set; outcome-metric ban; national holidays; wage-definition logic; 50% deduction cap; 2× OT floor; statutory-dues non-waiver; run block on `NOT_CONFIRMED`; bank-only payment; maker ≠ checker; cooling floor 1 day; leaver floor 4 h | L | Fixed | Not editable by any tenant role; CI tests |
| Payroll, leave and hours rule packs (Central and State) | G | Appendix Z §Z.2.4–Z.2.5 | Source, effective dates, maker ≠ checker, legal sign-off, preview against last run, rollback |
| DoFP / authority matrix | G | Proposals (Appendix Z §Z.12.2) | Board resolution reference for financial rows |
| Remote-employee jurisdiction mode; PT residence mode | G | Establishment State; OFF | CA/counsel opinion reference |
| Flags: investigation capture, geofence, biometric, individual ROI, forced distribution, multi-employment, Google adapter, payout API | G (flags) | OFF | Named approver per flag (Appendix Z §Z.15) |
| SoD additions | G | SOD-01…15 seeded | Seeded rules cannot be removed |
| Probation reminder offsets; work-summary reply window; leave coverage rules; evidence-completeness threshold; pay-run variance and hold thresholds; LWP divisor; leave-delegation minimum days; anomaly shadow days *(v3.1)* | T (LWP divisor other than calendar days: G) | Appendix Z §Z.15 v3.1 rows | Protected leave never subject to coverage; hold deadline D-1 Locked; loosening variance or anomaly values needs `internal_auditor` acknowledgement |
| SKU rules, deletion delay, UPN pattern | T (maker-checker) | Per Appendix Z §Z.5 | Console-role SKU guard Locked |
| Probation, notice, service-certificate days, regularisation window, roster publish, standard week | T | 6 months, 30/60 days, 7, 7, 7, 40 h | Never below statute |
| Leave template and company policy | T | Equator Standard | Floor validator |
| QA sampling, metric definitions, scorecard templates, cohort minimum | T | 5% / 3; catalogue; n ≥ 5 | Outcome ban; cohort floor 5 |
| Appraisal scale, PIP minimum, appeal window, protected-status duration | T | 5-point; 60 days; 15 days; 24 months | PIP ≥ 30 days; appeal ≥ 7 days |
| Pay day, freeze day, variance threshold, proof window | T | Last working day; 25th; 10%; Jan–Feb | Pay day ≤ statutory deadline |
| Cooling days, pre-run freeze, approval expiry/escalation, anomaly thresholds, expense/petty-cash/procurement/gifts thresholds | T | 3; 5; 14/2; Appendix Z §Z.12 | Loosening anomaly/expense/petty-cash values needs `internal_auditor` acknowledgement |

---

## 10. Security, privacy and audit

- **Identity:** all `apps/ops` users sign in through `eq-portal-ops` with workforce SSO and phishing-resistant MFA (X-24; App. S §2.6); step-up `aal2-pr` ≤ 10 min for approvals, reveals, bank changes, pay-run actions and exports; finance approvals only from office/ZTNA network zones; console roles require a SKU with Conditional Access and MDM or a time-boxed exception (FR-P18-14). Candidates use a separate low-assurance portal with no access to `apps/ops`.
- **Isolation:** tenant RLS + entity RLS on every `hr`/`pay`/`ctl` table (NN-38); Cerbos field-level policies (Appendix Z §Z.14); `pay` and `ctl` reachable only through their services; `eq_growth` and marketing services have no `USAGE` on these schemas (NN-16).
- **Encryption and minimisation:** PAN, UAN, bank account numbers and Aadhaar references encrypted (`*_enc`) with keyed hashes for duplicate checks; Aadhaar never stored in full (NN-14); BGV reports and health/accommodation data High tier, HR head only; identifiers masked by default; reveals logged with reason.
- **Sealed boundaries:** no POSH or whistle-blower content in HR, payroll, controls, analytics, AI or exports (NN-07); only the opaque protected-status flag and legal-hold flags cross.
- **Monitoring law:** NN-35 prohibited set Locked; governed investigation capture OFF; notice-before-capture; self-view and dispute; retention limits (Appendix Z §Z.6.6); no adverse action on telemetry alone; Meet/Teams presence never scored. Lawful bases per Appendix Z §Z.18.1 (DPDP s.7(i) is the employer's basis only; group processing under an intra-group agreement).
- **Books and edit log:** append-only ledgers and run lines; temporal history on master data; pgaudit on `pay`/`ctl`; Critical alert and block on trigger disable outside break-glass (Companies (Accounts) Rules r.3(1) proviso); books accessible in India, daily backup in India (r.3(5)); 8-year retention.
- **Exports:** HR/payroll exports require `EXPORT-SENSITIVE` approval (DPO + data owner), carry watermarks and NN-37 manifests, and expire from the exports bucket in 7 days (Q SC-14).
- **Detections (Q SC-10 additions):** mass export or reveal of HR/payroll identifiers by one actor; SoD violation attempts; payroll table mutation attempts; approval from unusual network/device; bank change followed by payment; access to `pay` outside business hours by non-payroll roles.
- **Retention:** classes per Appendix Z §Z.18.3 registered in `core.retention_classes`; `RetentionJob` with 2-week dry run; legal hold (open grievance, POSH matter, disciplinary case, litigation) overrides deletion and blocks workspace deletion.
- **Audit:** NN-22 hash-chained events for every create/update/approve/execute; `audit.access_log` for every read of High-tier fields and every cross-entity read; evidence collectors feed the Compliance Cockpit (FR-P14-V3-Z11).

---

## 11. AI touchpoints and guardrails

| Agent / feature | Permitted use | Guardrails |
|---|---|---|
| `drafting_assistant` (HR templates) | Draft job descriptions, offer and appointment letters, policy FAQs from approved templates | `requires_human_review = true`; legal-approved template is the source; no new terms invented |
| `document_extractor` | Extract fields from receipts, tax proofs, education certificates | Human confirms every extracted field; confidence shown; originals preserved (NN-32) |
| CV summary (within `document_extractor`) | Summarise a CV against the position's stated criteria for the recruiter | No ranking, scoring, rejection or protected-characteristic inference; recruiter decides |
| `hr_policy_assistant` (new) | Answer employees' policy questions from the approved policy corpus with citations | No legal, tax or regime advice; "ask HR" escalation; no access to individual records |
| `analytics_narrator` | Describe trends in aggregate dashboards | Aggregates only (n ≥ 5); never ranks individuals or recommends personnel actions |
| **Prohibited (Locked; red-team scenarios in P11)** | — | Candidate ranking or rejection; rating, PIP, termination or increment suggestions; emotion, health, intent or productivity inference from communications or telemetry; tax-regime recommendation; any use of POSH or whistle-blower content; HR/payroll data in few-shot or training sets |

Every AI call goes through the AI Gateway (FR-P11-01) with PII redaction, kill switch `ai.feature.<agent>` and deterministic fallback (manual forms and search) when disabled (NN-02). Payroll, leave, authority and anomaly computations are deterministic rules code with no model involvement (NN-01).

---

## 12. Acceptance criteria (Gherkin)

```gherkin
Feature: P18 workforce HRMS, payroll and internal controls

Scenario: NN-35_monitoring_prohibited
  Given a tenant admin with every HR configuration permission
  When they try to enable keystroke logging, webcam capture or off-hours location tracking
  Then the API returns 403 HR_MONITORING_PROHIBITED
  And no configuration change request is created
  And an audit event records the attempt

Scenario: NN-35_notice_before_capture
  Given an employee who has not acknowledged measurement notice version 3
  When they open the clock-in screen
  Then they must read and acknowledge the notice first
  And no session is recorded before acknowledgement

Scenario: NN-35_employee_sees_and_disputes_own_data
  Given an employee with 22 attendance days and 140 work items this month
  When they open My data
  Then every record shows its source, who can see it and its retention date
  When they dispute the attendance status of 14 October
  Then the manager receives a dispute task due in 5 working days
  And that day is excluded from the employee's scorecard until resolved

Scenario: NN-35_outcome_metrics_forbidden
  Given a metric definition "settlement rate per case manager"
  When an HR manager submits it for approval
  Then the API returns 422 HR_METRIC_OUTCOME_FORBIDDEN

Scenario: Joiner provisioning on Business Basic
  Given an offer accepted, BGV passed, NDA and acceptable-use signed for "Ananya Rao" in Case Services, remote, Jaipur
  When the employee is activated
  Then a Microsoft 365 user "ananya.rao@<domain>" is created with usageLocation IN and the Business Basic licence
  And the user is added to the Case Services and Remote groups
  And the temporary credential is sent only to the personal e-mail on file
  And hr.jml_events shows every step with sla_met = true

Scenario: Console role blocked on insufficient SKU
  Given an employee on Business Basic
  When it_admin grants the finance_controller console role
  Then the API returns 409 HR_WORKSPACE_SKU_INSUFFICIENT
  Unless a security-lead exception with expiry ≤ 90 days exists

Scenario: X-57_leaver_timings
  Given an employee whose exit becomes effective at 18:00 IST
  Then Equator platform sessions are revoked by 18:01
  And the workspace account is disabled with sessions revoked by 22:00
  And the mailbox is converted to shared and files transferred to the manager on the next day
  And the account is not deleted while a disciplinary case references the employee

Scenario: Appointment letter required
  Given an employee activated without a signed appointment letter
  Then the ghost-employee scan raises GH-04 High
  And the osh_appointment_letter_existing_3m clock is owned by an hr_executive

Scenario: Worker overtime needs consent and is paid at twice the rate
  Given a worker-classified support agent with monthly wages of ₹26,000
  When a team lead approves 3 hours of overtime without a consent record
  Then the API returns 409 HR_OVERTIME_CONSENT_REQUIRED
  When consent is recorded and the overtime approved
  Then the pay run includes overtime at 2 × (₹26,000 ÷ 26 ÷ 8) = ₹250 per hour, ₹750 for the 3 hours

Scenario: Leave policy below floor rejected
  Given a draft company policy with 12 earned leave days per year for Maharashtra employees
  When HR validates it
  Then the API returns 422 HR_LEAVE_POLICY_BELOW_FLOOR naming class "worker" and State "IN-MH"

Scenario: PAY_golden_wage_definition_76000
  Given a structure with total remuneration ₹76,000, basic plus DA ₹20,000 and excluded allowances ₹40,000
  When the structure is previewed
  Then statutory wages are ₹22,000
  And the add-back of ₹2,000 is shown with the CoW s.2(y) proviso reference

Scenario: PAY_epf_split_month_sep2026
  Given an employee with statutory wages of ₹30,000 for September 2026
  When the September run is calculated with the pro-rata split method
  Then the EPF wage base is ₹15,000 × 16/30 + ₹25,000 × 14/30 = ₹19,666.67 before rounding
  And the employee EPF contribution is 12% of that base, ₹2,360.00 before rounding
  And the parameter version shows status SECONDARY_ONLY with source S.O. 5109(E)
  And the run cannot be submitted until the Payroll Compliance Officer acknowledges it

Scenario: PAY_run_blocks_not_confirmed_param
  Given a bonus run whose eligibility ceiling parameter is NOT_CONFIRMED
  When the payroll maker submits it
  Then the API returns 409 PAY_PARAM_NOT_CONFIRMED

Scenario: PAY_deduction_cap_carry_forward
  Given monthly wages of ₹30,000 and approved deductions of ₹18,000 in October
  When the run is calculated
  Then deductions of ₹15,000 are applied in October
  And ₹3,000 is scheduled for November with an employee-visible schedule

Scenario: NN-36_pay_run_distinct_actors
  Given a run prepared by payroll_maker "P1"
  When "P1" tries to approve it as payroll_checker
  Then the API returns 403 PAY_MAKER_CHECKER_SAME_USER
  When "C1" approves for HR and "F1" approves for Finance
  And "C1" tries to release the bank file
  Then the release is blocked by SOD-03

Scenario: Bank file hash verified
  Given an approved run with bank file hash H
  When a bank acknowledgement for a file with a different hash is imported
  Then the API returns 409 PAY_BANK_FILE_HASH_MISMATCH and no line is marked paid

Scenario: NN-36_bank_change_cooling_and_oob
  Given an employee changes their bank account on 2 November
  Then penny-drop name-match passes
  And notifications go to the registered e-mail, phone and the previous account's channel
  And the new account cannot receive payment until 3 working days have passed
  When the employee clicks "This wasn't me"
  Then the change is frozen and a security incident is opened

Scenario: Duplicate bank account across payees
  Given vendor "V9" has bank account hash X
  When an employee submits a bank change to an account with hash X
  Then the API returns 409 CTL_DUPLICATE_BANK_ACCOUNT
  And alert AN-04 round-tripping is raised

Scenario: Ghost employee blocks finalisation
  Given an employee paid in October with no attendance, login, work item or approved leave
  When the run reaches the integrity gate
  Then GH-01 Critical is raised
  And submission returns 409 PAY_GHOST_HITS_UNRESOLVED until an internal_auditor resolves it with a reason and a second reviewer

Scenario: F&F within two working days
  Given an employee resigns with last working day Friday 13 November 2026
  And the establishment has Saturday and Sunday weekly offs and no holiday on 16 or 17 November
  When the exit becomes effective
  Then the F&F with leave encashment is computed and approved
  And payment is due by Tuesday 17 November 2026 (wrk_wages_2wd, establishment calendar)
  And gratuity, if payable, carries its own 30-day clock

Scenario: NN-36_no_self_approval
  Given an expense claim of ₹8,000 raised by department head "D1"
  When "D1" tries to approve it
  Then the API returns 403 CTL_SELF_APPROVAL_BLOCKED
  And alert AN-03 is recorded

Scenario: Split transaction detected
  Given a department head with a PO limit of ₹1,00,000
  When three POs of ₹95,000, ₹92,000 and ₹97,000 to the same vendor are raised within 7 days
  Then alert AN-02 split transaction is raised to finance and internal audit

Scenario: SoD conflict at role grant
  Given a user holding hr_executive in Equator Resolution Service Private Limited
  When it_admin grants payroll_checker in the same entity
  Then the API returns 409 CTL_SOD_CONFLICT citing SOD-01

Scenario: Payload changed after approval
  Given an approved vendor payment of ₹1,50,000
  When the payee bank account is altered before execution
  Then execution returns 409 CTL_PAYLOAD_CHANGED and a new approval is required

Scenario: PIP safeguards
  Given a manager proposes a PIP with no recorded check-in on the performance gap
  Then the API returns 422 HR_PIP_SAFEGUARD_MISSING
  Given the employee has an active protected status
  Then any PIP requires an additional independent reviewer and HR sees only "Additional review required"

Scenario: NN-38_secondment_required_for_host_work
  Given an Equator employee assigned 30% to Udofin without a secondment record
  When the assignment is saved
  Then the API returns 409 HR_SECONDMENT_RECORD_REQUIRED
  And payroll for the employee runs only in the employing entity after a secondment is signed

Scenario: Ethical wall for group staff
  Given a user with a role in Finbyx
  When they are proposed for the case_manager role on a matter where a Finbyx client is a party
  Then the grant is denied with 409 GRP_ETHICAL_WALL_CONFLICT (Appendix AD EW-01)

Scenario: Payroll edit log cannot be disabled
  Given a database session as eq_migrator outside break-glass
  When it runs ALTER TABLE pay.run_lines DISABLE TRIGGER ALL
  Then the statement is blocked and a Critical alert is raised

Scenario: Internal auditor is read-only
  Given an internal_auditor with a 60-day grant on payroll for FY 2026-27
  When they try to edit a pay-run variance reason
  Then the API returns 403 CTL_AUDIT_WORKSPACE_READ_ONLY
  And they can export the audit-trail report as an NN-37 package with a manifest

Scenario: Individual ROI hidden while flag OFF
  Given hr.analytics.individual_roi.enabled is OFF
  When ops_director requests GET /v1/ops/hr/analytics/roi?level=individual
  Then the API returns 403 and team-level views remain available with explain panels

# --- v3.1 additions (24 October 2026) ---

Scenario: PAY_golden_W02 EPF full month after the ceiling change
  Given an employee with statutory wages of ₹30,000 for October 2026
  When the October run is calculated
  Then the EPF wage is ₹25,000 and the employee contribution is ₹3,000
  And EPS is ₹2,082.50 and employer EPF is ₹917.50 before rounding
  And EDLI and admin charges are ₹125 each

Scenario: PAY_golden_W03 employer side of the September 2026 split
  Given the September 2026 base of ₹19,666.67 from PAY_epf_split_month_sep2026
  Then EPS is ₹1,638.23 and employer EPF is ₹721.77 before rounding

Scenario: PAY_golden_W09_W11 TDS default regime, rebate and marginal relief
  Given annual salaries of ₹15,00,000, ₹12,75,000 and ₹12,85,000 with no other income in TY 2026-27
  When annual tax is estimated under the default regime
  Then the tax including cess is ₹97,500, nil and ₹10,400 respectively
  And the ₹12,85,000 computation shows marginal relief of ₹51,500

Scenario: PAY_golden_W07 gratuity
  Given statutory wages of ₹40,000 and service of 6 years 7 months
  When F&F is computed
  Then gratuity is ₹1,61,538.46 on its own 30-day clock

Scenario: HR_leave_true_up_rj_252
  Given an Equator Standard employee of a Rajasthan establishment who worked 252 days in 2026
  When LeaveYearEndJob runs on 31 December 2026
  Then a floor_true_up of 3 days is posted (floor 21, credited 18) before carry-forward and encashment

Scenario: PAY_line_hold_deadline
  Given a run whose line for employee "E7" is auto-held for a Critical ghost-employee hit
  Then the bank file excludes E7 and the rest of the run is released
  And E7 sees "Payment under verification — expected by" a date before the statutory deadline
  When the hold is still unresolved at D-1 of the deadline
  Then the finance_controller and the Company Secretary are alerted
  And closing the run returns 409 PAY_HOLD_PAST_DEADLINE until the line is paid off-cycle or confirmed not payable with a second reviewer

Scenario: Leave coverage never blocks protected leave
  Given team "Support L1" with min_on_duty_pct 60% in require_second_approval mode and coverage already at 60% on 9 December
  When an agent applies for casual leave on 9 December
  Then the department head is added as a second approver and three alternative windows are shown
  When another agent applies for sick leave on 9 December
  Then no coverage check runs and the request goes to the line manager only

Scenario: Delegation on leave
  Given department head "D2" with 4 pending approvals applies for 5 working days' leave and names "D3" as cover
  When the leave is approved and its first day begins
  Then the pending steps move to "D3" labelled "on behalf of D2" without starting the escalation timer
  And "D3" cannot approve an item that "D3" made
  And on D2's return open items revert to "D2" with D3's notes

Scenario: Anomaly rule must shadow before alerting
  Given compliance_officer creates rule AN-18 "reimbursement after resignation"
  Then it runs in shadow mode for 30 days and raises no alerts
  When compliance_officer tries to promote it after 10 days
  Then the promotion is refused
  And after 30 days promotion needs internal_auditor approval with the shadow report attached

Scenario: Right of reply is shown unedited
  Given an employee replies to October's "first-response SLA" figure within 10 working days
  When the manager, HR or the calibration committee opens that figure
  Then the reply is shown first, unedited and time-stamped
  And the manager cannot edit or hide it

Scenario: Rating not lowered for approved leave
  Given an employee on maternity leave for 4 months of the cycle
  When a calibration change lowers the rating with reason code "absence"
  Then the API returns 422 HR_RATING_REASON_PROHIBITED

Scenario: NN-36_sod15_approve_reconcile_split
  Given accounts_checker "A1" approved a vendor payment of ₹1,80,000
  When the bank reconciliation item for that payment is assigned
  Then it cannot be assigned to "A1" and routes to another accounts_checker

Scenario: Probation reminder ladder
  Given an employee whose probation ends on 30 April 2027 and no review submitted
  Then the manager is reminded on 16 March, 31 March and 15 April, HR on 23 April
  And on 30 April deemed confirmation applies with an exception logged against the manager
```

---

## 13. Deliverables and exit gate

- [ ] Schemas `hr`, `pay`, `ctl` with tenant + entity RLS; `db:rls-catalogue` extended; migrations forward-only with history tables and append-only triggers.
- [ ] Org model with D3-06 first-run wizard; positions, bands, headcount plan with approvals.
- [ ] Recruitment to onboarding end-to-end, OSH-format appointment letter e-signed, pre-joining checks, policy acknowledgements, worker classification.
- [ ] `WORKSPACE_PORT` with `m365_graph` working against a Microsoft 365 test tenant on Business Basic; Google stub OFF; manual fallback; JML SLA report green (joiners without checks = 0; leaver revocations within SLA = 100%).
- [ ] Movements, secondments, exit, clearance, F&F within 2 working days, exit documents.
- [ ] Attendance (web + mobile), rosters, overtime with consent, WFH declarations, regularisation, My data and disputes; NN-35 prohibited set tests green.
- [ ] Work items from `cases`, `ops`, `mkt`, `grm`, `ctl`; scorecards; QA sampling; utilisation; ROI dashboards (team level) with safeguards.
- [ ] Leave engine with OSH s.32 and five State packs, Equator Standard and statutory-minimum templates, floor validator, balances, calendars.
- [ ] Payroll: rule packs with statuses and run gate; component classes; wage calculator golden test; structures; full monthly cycle for 40 synthetic employees across DL/UP/RJ/MH/KA; EPF September 2026 split; ESI; PT; LWF; TDS s.392 with regime election and Form 124/127; payslips (EN/HI); registers; ECR/ESI/PT/LWF files; Form 130/123/138 data; journals to Tally and Zoho Books; `PAYROLL_EXCHANGE_PORT` import with difference report.
- [ ] Performance: goals cascade, check-ins, mid-year and annual cycles, calibration with fairness panel, 360, PIP safeguards, increment cycle within budget, acknowledgement and appeal.
- [ ] Learning space, certifications, assets, documents vault.
- [ ] Controls: authority matrix with Board-approval banner, maker-checker engine adopted by HR, payroll, billing (FR-P05-V3-Z06), procurement and expenses; SoD matrix; payee/bank controls; ghost and anomaly jobs; vendor KYC; petty cash; access-review extension; COI and gifts; vigil desk configuration and protected status; exception register; dashboards; internal-audit sampling and drill-downs on the Appendix AE `eng` register, with evidence export through the AE §AE.8.4 packs.
- [ ] NN-35, NN-36, NN-37 (HR exports), NN-38, NN-22 tests green; all 43 Gherkin scenarios above passing (30 v3.0 + 13 v3.1); Appendix Z §Z.19 CI tests present.
- [ ] ADRs: entity RLS pattern; `WORKSPACE_PORT` and SKU capability matrix; payroll rules library shared with `chm` (X-58); approval engines (X-56); bank-file hashing and acknowledgement reconciliation; protected-status boundary with sealed services.
- [ ] Seed data: Equator entity with Delhi, Noida and Jaipur establishments; 40 synthetic employees (workers and non-workers, remote across five States, one fixed-term, one secondee to a synthetic Udofin entity, one leaver); vendors including one related party; demo script `docs/phases/P18-demo.md`.
- [ ] **Go-live gate (FR-P14-V3-Z13):** SKU confirmed by the Company Secretary; DoFP approved by the Board; letter templates legal-approved; measurement and privacy notices DPO-approved; parameters used by the first live run `VERIFIED` or acknowledged; one-month parallel run with zero unexplained differences.

---

## 14. Open items and legal verification flags

1. **Microsoft 365 SKU** — "Business Starter" is not a Microsoft plan; the Company Secretary confirms the actual SKU (likely Business Basic) (D3-04) **[VERIFY — open: tenant SKU via admin centre or `subscribedSkus`]**; Graph details not confirmed: group-based licensing on Basic, `usageLocation` requirement, mailbox delay, shared-mailbox limits, Exchange RBAC for `Mail.Send` **[VERIFY — open: RD open point 2]**.
2. **Department structure** — management has not supplied it; the D3-06 default ships with a confirmation wizard **[VERIFY — open: management decision]**.
3. **DoFP values** — proposals only; Board resolution required before first financial use **[VERIFY — open: Board approval]**.
4. **Remote employees' State law, PT and LWF** — no authoritative source; default establishment State (D3-31) **[VERIFY — open: CA/counsel opinion]**.
5. **Statutory parameters not confirmed** — CoW s.26 bonus ceilings; OSH (Central) Rules G.S.R. number, appointment-letter form number, quarterly OT cap; ESIC rates under CoSS; S.O. 5109(E) Gazette text and EPFO guidance on the September 2026 split; gratuity ceiling notification under CoSS s.53(3); s.202(1) slab text; Form 123 issue date; Form 138 and TDS deposit due dates; contractor TDS under s.393; State minimum wages (DL, UP, RJ, MH, KA); State leave, holiday-count, registration and LWF conflicts; PT conflicts (Maharashtra women's threshold, TN, GJ) **[VERIFY — open: RC open points 1–12]**.
6. **Appointment-letter duty below 10 workers** — issued in all cases **[VERIFY — open: RC open point 1]**.
7. **Women's night work from home** — which OSH Central Rules conditions apply **[VERIFY — open: counsel]**.
8. **Separate part-time appointments across group companies** — OFF pending payroll/PF advice **[VERIFY — open: RE F5.3]**.
9. **Secondment GST and s.188** — tax-adviser review of recharge structure (*Northern Operating Systems*; CBIC Instruction 05/2023-GST); Infrabyx shareholding chain and related-party status (s.2(76)(iv)) **[VERIFY — open: CS / tax adviser]**.
10. **Related-party training** — purchases from Infrabyx Consultancy (OPC) Pvt Ltd (equatoradr.com) **[VERIFY — open: CS to confirm s.188 treatment]**.
11. **DPDP s.7(i) wording** — quote enacted Gazette text in the employee notice **[VERIFY — open: RC open point 13]**.
12. **Non-statutory leave defaults** (paternity 5 working days, bereavement 3 days) **[VERIFY — open: management decision]**.
13. **Record-retention periods** for income-tax, EPF/ESI and POSH records under the new Rules; current defaults 8 years for payroll and employee files **[VERIFY — open: RC open point 14]**.
14. **Vigil mechanism applicability** — Equator not currently in scope of Companies Act s.177(9); CS maintains the applicability facts annually.
15. **EPF/ESI rounding and the LWP divisor** — rounding rules under the 2026 Schemes (seed: nearest rupee per component, SECONDARY_ONLY) and any absence-deduction divisor other than calendar days **[VERIFY — open: Payroll Compliance Officer with CA]** *(v3.1)*.

## v3 Addendum (23 October 2026)

The requirements below come from the v3.0 appendices and are part of this phase's scope and exit gate.

### From Appendix AD — Group Companies and Cross-Functional Operations

**FR-P18-V3-AD01 — Group columns for secondments and cross-entity employment guard.** Additive `hr.secondments` columns (AD-R3); `hr.legal_entities.id` foreign key to `grp.legal_entities` (AD-R1); `GRP_DUPLICATE_EMPLOYMENT` extends Appendix Z's one-active-employment-per-PAN index across entity tenants; Appendix Z allocations feed `IntercompanyChargeRunWorkflow`; payroll runs only in the employing entity. *Acceptance:* AD-T08, AD-T09, AD-T10.

