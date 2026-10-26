# Appendix Z — Workforce HRMS, Payroll and Internal Controls (v3.0, 23 October 2026)

> Binding specification for the internal Human Resource Management System (schema `hr`), payroll engine (schema `pay`) and internal-controls engine (schema `ctl`) inside the Operations Platform (`apps/ops`). Built first for Equator Resolution Service Private Limited's own employees, most of whom work remotely across India; group companies (Finbyx, Udofin and others in the Infrabyx Group) are onboarded later as additional employing entities under NN-38. Implemented in Phase P18. All figures in this appendix are **parameters**, not code: each carries a source, an effective date and a verification status, and is loaded as a versioned rule pack (NN-33 tier G).

---

## Z.0 Purpose, sources, precedence

### Z.0.1 Purpose
Management asked for (a) a full employee lifecycle including assignment of work e-mail IDs; (b) leave and salary calculation under Indian labour law for staff working remotely across India; (c) login/logoff time, work measurement and performance assessment, with case managers working from home; (d) decentralised decisions with maker-checker, anti-corruption and anti-embezzlement controls; and (e) a small HR and salary module that can later serve group companies (V3 writer conventions, management brief items 2, 4 and 11). The departmental structure was not supplied; this appendix uses the default, fully configurable model of D3-06 and says so wherever it matters.

It specifies system behaviour, not legal, tax or payroll advice (disclaimer §Z.9.12).

### Z.0.2 Sources
| Tag | Source | Use in this appendix |
|---|---|---|
| [RC] | `research/RC_LABOUR_PAYROLL.md` (law as at 23 Oct 2026) | Labour Codes, State S&E Acts, PT/LWF, Income-tax Act 2025, POSH, monitoring law, retention, anti-fraud controls, chambers sizing. RC's tags are carried forward: **[V]** verified primary, **[V-sec]** reputable secondary, **[K]** settled/carried, **[NC]** not confirmed |
| [RD] | `research/RD_INTEGRATIONS_DEVOPS.md` | Microsoft 365 SKU facts, Microsoft Graph and Google Admin SDK operations, `WORKSPACE_PORT`, JML workflow, accounting audit trail (Companies (Accounts) Rules 2014 r.3), internal-audit applicability |
| [RE] | `research/RE_DIRECTORY_MARKETPLACE_LAW.md` §F5 and DI-E | Employer of record, secondment, DPDP s.7(i) across group entities, Companies Act s.188 shared services, ethical walls |
| [RB] | `research/RB_BUSINESS_MODELS.md` §1 | equatoradr.com operator facts |
| Pack | Master §3, §4, §15; Appendices F, G (LR-LAB, LR-POSH, LR-DPDP, LR-TAX-004), N, O, Q, S, U §U.4; V5 §3.1, §4.1; P01 FR-P01-27; P05 FR-P05-52/55; P09 FR-P09-28/34; P14 FR-P14-21 | Reused patterns, roles, controls and IDs |
| v3 siblings | Appendix AD (group companies, secondment); Appendix AC (`ACCOUNTING_PORT`, connectors); Appendix W / P20 (chambers HR-lite, consumer of the X-58 library and rule packs); P15 (NN-33 settings engine); P16 (Operations Platform shell `apps/ops`) | Dependencies, referenced by function |

### Z.0.3 Precedence
Master §15 order applies. Within the workforce domain: (1) master NN-33, NN-35, NN-36, NN-37, NN-38, NN-40; (2) Appendix G legal-rule status (a payroll parameter's `verification_status` must not be higher than the matching LR row); (3) Appendix F names, types, events and error codes (the codes in §Z.17 are registered in F §F.10.4 v3); (4) this appendix; (5) Phase P18. Where this appendix and Appendix V5 (WRK, a **dispute** vertical about other employers' staff) use the same legal concept, V5 governs the dispute side and this appendix governs Equator's own HR; both call the same pure functions (`wrk_is_worker()`, `wage_code_base()`).

### Z.0.4 Reconciliations made here
| # | Topic | Conflict | Resolution |
|---|---|---|---|
| Z-R1 | Payroll schema name | RC proposes `payroll.rule_params`; conventions use schema `pay` and rule packs in `cfg` | Rule packs live in `cfg` as `rulepack.<jur>.payroll.<name>@<ver>`; `pay.rule_params` is a read model materialised from approved `cfg` versions (X-58) |
| Z-R2 | JML log table | RD names `ops.jml_events`; conventions reserve `ops` for CRM/support | Table is `hr.jml_events`; RD's name is a documentation alias only |
| Z-R3 | Leaver revocation time | Appendix S §1.3 (Equator sessions revoked within 60 s of SCIM `active=false`) vs Appendix Q SC-01 / RD (workspace disable ≤ 4 h) | Both apply to different systems (X-57) |
| Z-R4 | Approval engines | P00 FR-P00-39 `core.config_change_requests` (configuration) vs NN-36 maker-checker for transactions | Two request types, one authority resolver (X-56) |
| Z-R5 | Workspace SKU error | RD `WORKSPACE_SKU_INSUFFICIENT_FOR_ROLE` | Registered as `HR_WORKSPACE_SKU_INSUFFICIENT` with RD name as alias |
| Z-R6 | Interview "scorecard" vs KPI "scorecard" | Same word for two objects | `hr.interview_feedback` (recruitment) and `hr.kpi_scorecards` (performance) |

---

## Z.1 Requirements, decisions and cross-file resolutions

### Z.1.1 Requirements (add to 02 §2)
| ID | Requirement (management brief) | Where specified | Status |
|---|---|---|---|
| R-58 | Internal HRMS with full employee lifecycle — requisition, recruitment, offer, appointment letter, onboarding, assignment of work e-mail and access, probation, movements, secondment, exit and full and final settlement — for Equator and later group companies, remote-first across India | Z.3–Z.5, Z.13; P18 §4A–4D | S+L |
| R-59 | Transparent attendance (login/logoff), work measurement, role scorecards, ROI dashboards and performance appraisal for remote staff, including case managers working from home | Z.6, Z.7, Z.10; P18 §4E–4F, 4I | S+L (NN-35) |
| R-60 | Leave and salary calculation under Indian labour law with versioned State and Central rule packs, statutory outputs and accounting export | Z.2, Z.8, Z.9; P18 §4G–4H | S+L (parameters `[NC]` gated) |
| R-61 | Decentralised decisions within delegated limits, maker-checker, separation of duties, anti-corruption and anti-embezzlement controls, internal-audit sampling on the Appendix AE `eng` audit register | Z.12; P18 §4K; Appendix AE §AE.8 | S (NN-36) |

### Z.1.2 Decisions (add to 02 §3)
| ID | Decision | Reason / source | Effect |
|---|---|---|---|
| D3-30 | **Systems of record.** `hr`, `pay` and `ctl` are the system of record for people, organisation, attendance, leave, compensation, payroll and approvals; Microsoft 365/Google is downstream for identity and mailbox only; Tally/Zoho Books for the general ledger; specialist payroll tools are optional import/export partners (D3-03, NN-40) | NN-40; RD DI-A; RD F1.4 ("M365 must never be the system of record") | Z.5, Z.9.10, `PAYROLL_EXCHANGE_PORT` |
| D3-31 | **Remote-employee jurisdiction default.** Each employee carries `establishment_state` (the office that employs, controls and pays) and `work_location_state` per effective date. Defaults: S&E Act, holiday calendar and "appropriate Government" follow `establishment_state`; minimum wage = higher of the two States; PT and LWF follow `establishment_state` until a written CA/counsel opinion is filed, after which flag `pay.pt.residence_state_mode` may be switched ON | [RC] F6.3 (recommendation; no primary source settles it), open point 9 | Z.2.4, Z.8, Z.9 |
| D3-32 | **Equator Standard leave policy** (earned 18 days, casual 8, sick 12, 10 paid holidays, carry-forward 45, refused leave never lapses) applies to every employee regardless of worker classification, to avoid per-employee divergence; it is validated as ≥ the statutory floor for every class and State, and where a launch-State floor exceeds a template value the template is raised automatically for employees of that `establishment_state` (seed case: Rajasthan S&CE Act s.14 — 1 day per 12 days worked after 240 days, i.e. about 20–22 days, above 18) | [RC] Design implications C.14; F6.2 | Z.8.3 |
| D3-33 | **Output-based measurement only.** Work is measured from platform work items, SLAs, sampled quality reviews and customer feedback. Keystroke logging, webcam capture, covert screen recording, off-hours location tracking, personal-device monitoring and reading personal communications are **Locked OFF**. Individual ROI views are OFF by default (`hr.analytics.individual_roi.enabled`) until a DPIA is approved; team and department views are ON | NN-35; [RC] F12, D.19–24 | Z.6, Z.7 |
| D3-34 | **One transaction-approval engine.** `ctl` provides the authority matrix, maker-checker, separation-of-duties and exception register used by HR, payroll, billing refunds/write-offs, procurement, expenses, vendor and payee changes, privileged-role grants and sensitive exports. The default Delegation of Financial Powers (DoFP) values in Z.12.2 are **proposals subject to Board approval** | NN-36; P05 finance bundles | Z.12; X-56 |

### Z.1.3 Cross-file resolutions (add to master §15)
| # | Topic | Resolution |
|---|---|---|
| X-56 | Maker-checker engines | `core.config_change_requests` (P00 FR-P00-39) remains the engine for **configuration objects** (rule packs, templates, fee schedules, flags). `ctl.approval_requests` is the engine for **business transactions** (pay runs, payments, refunds, write-offs, payee/bank changes, hires, salary revisions, role grants, sensitive exports, allocation overrides). Both resolve approvers and limits through `ctl.resolve_authority()`; P05 `fin.*` bundles become authority-matrix rows with identical limits (refund ≤ ₹25,000 by `fin.operator`; payout release > ₹2,00,000 by `fin.approver`). Neither engine may approve a request whose maker is the checker (DB CHECK). |
| X-57 | Leaver revocation | On `equator.hr.employee.exit_effective.v1`: Equator platform sessions and memberships (Keycloak, `eq-portal-ops`, `/staff/login`) are revoked within **60 s** (Appendix S §1.3); workspace accounts (M365/Google) are disabled with sessions revoked within **≤ 4 h** (`iam.leaver_revoke_hours`, locked floor, tenant may only tighten; Q SC-01); a `termination_for_cause` exit runs both at the moment the decision is recorded, with a second approver. |
| X-58 | Payroll rules library and parameters | A single pure, deterministic library `packages/rules/payroll` computes wage base, statutory contributions, TDS, leave encashment, gratuity and F&F for both `pay` (Equator and group companies) and the Private ADR Chambers HR-lite module (`chm`). Statutory parameters are `cfg` rule packs (tier G) materialised into `pay.rule_params`; run data stays in the owning tenant's schema. RC's `payroll.*` names are superseded by `pay.*`. |

---

## Z.2 Legal and parameter baseline

### Z.2.1 Status of the four Labour Codes (inputs to the rule engine)
All four Codes are in force from 21 Nov 2025 (CoSS S.O. 5319(E), substantially; IR S.O. 5320(E); OSH S.O. 5321(E); CoW S.O. 5322(E)) [V via pack]. Central Rules 2026: Wages G.S.R. 343(E), IR G.S.R. 342(E), CoSS G.S.R. 344(E) (8 May 2026), OSH in force 8 May 2026 (G.S.R. number `[NC]`); EPF/EPS/EDLI Schemes 2026 (corrigenda G.S.R. 703–705(E), 4 Aug 2026); Model Standing Orders 2026 (services) are a template below 300 workers [V-sec]. Equator and private chambers are almost certainly **State-sphere** establishments; old State rules survive where consistent with the Codes (MoLE FAQ Q1) [RC F1].

**Product consequence.** Every State-dependent value is a jurisdiction-scoped parameter with source and `verified_on`; the engine evaluates, per employee and per day, the union of applicable floors (Code + State S&E Act + contract) and applies the most favourable per entitlement (MoLE Additional FAQ Q25) [RC F6.1].

### Z.2.2 Applicability thresholds (evaluated monthly on actual headcount per employing entity and establishment)
| Duty | Threshold | Source | Engine behaviour |
|---|---|---|---|
| Appointment letter to every employee | All employees (existing staff within 3 months) | OSH Code s.6(1)(f) [V]; binding below 10 workers `[NC]` | Always issued (recommended in all cases) |
| Minimum wage, timely payment, deductions cap, equal pay, wage slips, registers | All employees incl. managers (CoW s.2(k)) | CoW ss.3, 5, 15–18, 50 [V] | Always on |
| OSH establishment, registration, s.32 annual leave | 10 or more workers | OSH ss.2(1)(v), 3, 32 [V] | Auto-on at 10; registration task |
| ESI | 10 or more persons; wage threshold ₹21,000/month | CoSS; MoLE FAQ [V] | Auto-on at 10 |
| Gratuity | 10 or more employees | CoSS ss.53–58 [V] | Provision always; statutory payout rules at 10 |
| POSH Internal Committee | 10 or more employees (below → Local Committee) | POSH Act ss.4, 6 [pack LR-POSH] | Uses P09 sealed IC module |
| EPF/EPS/EDLI | 20 or more employees (voluntary below) | CoSS; Schemes 2026 [V]/[V-sec] | Auto-on at 20; voluntary switch below |
| Bonus (CoW Ch. IV) | 20 or more persons on any day in the accounting year | CoW s.41(2) [V] | Auto-on at 20; **ceilings `[NC]`** (§Z.9.5) |
| Grievance Redressal Committee | 20 or more workers | IR Code s.4 [V] | Uses P09 `WRK_IRCODE` desk |
| Crèche (or allowance ≥ ₹500/child/month) | 50 or more employees | CoSS; Central Rules [V]/[V-sec] | Task + allowance component |
| Standing orders | 300 or more workers | IR Code s.28 [V] | Not applicable; MSO used as policy template |
| Vigil mechanism (statutory) | Listed, accepts public deposits, or borrowed > ₹50 crore from banks/PFIs | Companies Act s.177(9)–(10); r.7 [K] | Derived flag `ctl.vigil.statutory_mode`; voluntary channel always on |
| Internal auditor (statutory, private company) | Turnover ≥ ₹200 crore or borrowings > ₹100 crore | Companies (Accounts) Rules r.13 [V-sec] | Configurable fact `group.audit.applicability.*` (Appendix AE §AE.8.2); internal-audit function exists regardless (D3-06) |

### Z.2.3 Statutory clocks owned by HR and payroll (NN-04 pattern; never hard-coded)
| Clock | Period | Start | Owner | Source |
|---|---|---|---|---|
| `pay_monthly_wage_deadline` | Before the 7th day of the following month | Wage-period end | `payroll_checker` | CoW s.17(1) [V] |
| `wrk_wages_2wd` (F&F) | 2 working days | Removal, dismissal, retrenchment, resignation | `hr_manager` | CoW s.17(2) [V]; App. A clock name |
| `osh_leave_encash_2wd` | 2 working days (discharge, dismissal, quitting); 2 months (superannuation, death) | Separation | `hr_manager` | OSH s.32(1)(vi) [V] |
| `coss_gratuity_30d` | 30 days | Gratuity becoming payable | `hr_manager` | CoSS s.56 [V] |
| `osh_appointment_letter_existing_3m` | 3 months | Commencement (existing staff) / joining (new) | `hr_executive` | OSH s.6(1)(f) [V] |
| `cow_fine_show_cause_7d` / `cow_fine_impose_15d` | 7 days to show cause; impose and intimate within 15 days | Notice | `hr_manager` | Wages (Central) Rules r.16 [V-sec] |
| `cow_absence_reply_7d` | 7 days | Intimation of absence deduction | `hr_manager` | r.17 [V-sec] |
| `itax_form130_issue` | By 15 June after the tax year | Tax-year end | `payroll_checker` | Form 130 [V-sec] |
| `itax_form138_quarterly` | Per Income-tax Rules 2026 — `[NC]` | Quarter end | `payroll_checker` | [RC] F8 open point 7 |
| `epf_ecr_monthly` | 15th of following month (e.g., September 2026 ECR due 15 Oct 2026) | Wage month | `payroll_checker` | [V-sec RC F3.1] |
| `service_certificate` | Default 7 days (configurable; MSO template 10 days; Karnataka 7 days) | Exit effective | `hr_executive` | [RC] F5, F6.2 |
| `workspace_leaver_revoke` | ≤ 4 h (Equator sessions ≤ 60 s) | Exit effective | `it_admin` | Q SC-01; S §1.3; X-57 |
| `posh_ic_constitution` | Before 10th employee joins | Headcount crossing | `hr_manager` | POSH Act s.4 |

A clock breach raises a red alert to the HR head and the Company Secretary (`compliance_officer` with designation `company_secretary`) and is an exception in `ctl.exceptions`.

### Z.2.4 Payroll and labour parameter seed (`cfg` rule packs; materialised into `pay.rule_params`)

Each parameter row carries: `param_code`, `jurisdiction` (`IN`, `IN-DL`, `IN-UP`, `IN-RJ`, `IN-MH`, `IN-KA`, …), `sphere` (`central`/`state`), `applies_to` (`worker`, `non_worker`, `fte`, `international_worker`, `apprentice`, `all`), `value` (scalar, slab table or formula ref), `unit`, `effective_from`, `effective_to`, `source_instrument`, `source_url`, `source_type` (`gazette`, `official_guidance`, `secondary`), `verification_status` (`VERIFIED`, `SECONDARY_ONLY`, `NOT_CONFIRMED`), `verified_by`, `verified_on`, `approved_by`, `approved_on`, `review_due` [RC A.1]. Approved versions are immutable; corrections create a new version. Every payslip line stores the `param_version_id` it used.

**Rule-pack map (names binding for `pay` and `chm`; aligned with the Appendix V §V.2.1 rule-pack catalogue).** Central (`rulepack.IN.payroll.<name>`): `wage_definition` (`cow.*` except bonus and minimum wage), `epf` (`coss.epf.*`, `coss.edli.*`), `esi` (`coss.esi.*`), `gratuity` (`coss.gratuity.*`), `bonus` (`cow.bonus.*`), `leave` (`osh.leave.*`, OSH s.32), `maternity` (`coss.maternity.*`, `coss.creche.*`), `income_tax` (`itax.*`), and three packs added by this appendix: `hours` (`osh.daily_hours`, `osh.weekly_hours`, `osh.overtime.*`, `osh.women_night_window`), `min_wage` (`minwage.central.*`) and `thresholds` (`*.establishment_threshold`, `irc.*`, `osh.supervisory_wage_cap`). State (`rulepack.IN-<ST>.payroll.<name>`, `<ST>` = `DL`, `UP`, `RJ`, `MH`, `KA`, …): `professional_tax` (`pt.<state>.*`), `lwf` (`lwf.<state>.*`), `se_hours` and `se_leave` (`se.<state>.*`), and, added here, `min_wage` (`minwage.<state>.*`) and `holidays` (State holiday calendar). Versions follow `@<year>.<n>` (e.g., `rulepack.IN.payroll.epf@2026.2`). Appendix W (chambers) consumes these exact names and defines no payroll pack of its own (X-58).

**Run gate (Locked).** A pay run cannot be finalised if any parameter it uses is `NOT_CONFIRMED` (`PAY_PARAM_NOT_CONFIRMED`, 409); `SECONDARY_ONLY` parameters produce a warning that the named Payroll Compliance Officer (`compliance_officer` with responsibility `payroll_compliance`) must acknowledge per run (`PAY_PARAM_ACK_REQUIRED`) [RC A.3]. A parameter that is `NOT_CONFIRMED` but **legally required** for a run (e.g., a State PT slab for an employee in Maharashtra) must be resolved by the Payroll Compliance Officer either by verifying it against the Gazette or by recording a dated professional opinion; the system never invents a value.

| Rule pack / `param_code` | Seed value | Effective from | Status |
|---|---|---|---|
| `rulepack.IN.payroll.wage_definition@2026.1` · `cow.wage_definition.exclusion_cap_pct` | 50 | 21 Nov 2025 | VERIFIED [RC 1] |
| `cow.in_kind_cap_pct` | 15 | 21 Nov 2025 | VERIFIED |
| `cow.monthly_pay_deadline_day` | before 7th of next month | 21 Nov 2025 | VERIFIED |
| `cow.separation_pay_working_days` | 2 | 21 Nov 2025 | VERIFIED |
| `cow.deduction_cap_pct` | 50 per wage period; excess carried forward (r.13) | 21 Nov 2025 | VERIFIED; carry-forward SECONDARY_ONLY |
| `cow.overtime_multiplier` | 2.0 | 21 Nov 2025 | VERIFIED |
| `cow.min_wage.daily_to_monthly_factor` | × 26; hourly = daily ÷ 8 | 8 May 2026 | SECONDARY_ONLY |
| `cow.bonus.min_pct` / `max_pct` / `min_amount` | 8.33 / 20 / ₹100 | 21 Nov 2025 | VERIFIED |
| `cow.bonus.establishment_threshold` | 20 | 21 Nov 2025 | VERIFIED |
| `cow.bonus.eligibility_wage_ceiling` / `calc_ceiling` | not set | — | **NOT_CONFIRMED** `[VERIFY — open: CoW s.26 ceilings not notified; Payment of Bonus Act values (₹21,000; ₹7,000/minimum wage) not confirmed as saved]` |
| `cow.records.retention_years` | 5 after last entry | 8 May 2026 | SECONDARY_ONLY |
| `osh.establishment_threshold` / `coss.esi.establishment_threshold` / `coss.gratuity.establishment_threshold` / `coss.epf.establishment_threshold` | 10 / 10 / 10 / 20 | 21 Nov 2025 | VERIFIED [RC 2, 3] (drive §Z.2.2 and the chambers compliance wizard, W §W.6.2) |
| `rulepack.IN.payroll.epf@2026.2` · `coss.epf.wage_ceiling` | ₹15,000 to 16 Sep 2026; **₹25,000 from 17 Sep 2026** | 17 Sep 2026 | SECONDARY_ONLY `[VERIFY — open: Gazette text of S.O. 5109(E), 17 Sep 2026]` |
| `coss.epf.ee_rate` / `er_rate` | 12 / 12 (employer: EPS 8.33 on wages up to ceiling + EPF 3.67); 10% classes as notified | 2026 Schemes | SECONDARY_ONLY |
| `coss.edli.rate` / `coss.epf.admin_rate` | 0.50 / 0.50 | 2026 Schemes | SECONDARY_ONLY |
| `coss.epf.split_month_method` | September 2026: ₹15,000 for 1–16 Sep, ₹25,000 for 17–30 Sep, pro rata by calendar day | 1 Sep 2026 | SECONDARY_ONLY `[VERIFY — open: EPFO guidance awaited]` |
| `coss.epf.iw_ceiling_applies` | false (International Workers: 12% of entire wages) | 2026 Schemes | SECONDARY_ONLY (*LG Electronics v UoI* pending) |
| `coss.esi.wage_threshold` | ₹21,000 | 21 Nov 2025 | VERIFIED (MoLE FAQ) |
| `coss.esi.ee_rate` / `er_rate` | 0.75 / 3.25 | — | SECONDARY_ONLY `[VERIFY — open: ESIC rate notification under CoSS]` |
| `coss.gratuity.days_per_year` / `divisor` / `ceiling` | 15 / 26 / ₹20,00,000 | 21 Nov 2025 | VERIFIED (FAQ); ceiling notification `[VERIFY — open: fresh s.53(3) notification]` |
| `coss.gratuity.min_service_years` / `fte_min_service_years` | 5 / 1 | 21 Nov 2025 | VERIFIED |
| `coss.maternity.weeks` / `eligibility_days` / `medical_bonus` | 26 / 80 / ₹3,500 | 21 Nov 2025 | VERIFIED |
| `coss.creche.threshold` / `allowance_min` | 50 / ₹500 per child per month | 8 May 2026 | VERIFIED / SECONDARY_ONLY |
| `osh.daily_hours` / `weekly_hours` | 8 / 48 | 21 Nov 2025 / 8 May 2026 | VERIFIED / SECONDARY_ONLY |
| `osh.overtime.rounding` | 15–30 min → 30 min; > 30 min → 1 h | 8 May 2026 | SECONDARY_ONLY |
| `osh.overtime.quarterly_cap_hours` | not set (State values in §Z.2.5) | — | **NOT_CONFIRMED** (Central) |
| `osh.leave.eligibility_days` / `accrual_ratio` / `carry_forward_cap` | 180 / 1 per 20 days worked / 30 | 21 Nov 2025 | VERIFIED |
| `osh.supervisory_wage_cap` | ₹18,000 | 21 Nov 2025 | VERIFIED |
| `osh.women_night_window` | before 06:00 / after 19:00 | 21 Nov 2025 | VERIFIED |
| `irc.grc_threshold` / `standing_orders_threshold` | 20 / 300 | 21 Nov 2025 | VERIFIED |
| `irc.retrenchment.notice_months` / `comp_days_per_year` / `reskilling_days` | 1 (Ch. IX, 50–299 workers); 3 (Ch. X, 300+) / 15 / 15 | 21 Nov 2025 | VERIFIED |
| `rulepack.IN.payroll.income_tax@2026.1` · `itax.salary_tds_section` | Income-tax Act 2025 s.392 | 1 Apr 2026 | VERIFIED |
| `itax.default_regime.slabs` (TY 2026-27) | 0–4 L 0%; 4–8 L 5%; 8–12 L 10%; 12–16 L 15%; 16–20 L 20%; 20–24 L 25%; > 24 L 30% | 1 Apr 2026 | SECONDARY_ONLY `[VERIFY — open: s.202(1) enacted table]` |
| `itax.standard_deduction.default` / `.old` | ₹75,000 / ₹50,000 | 1 Apr 2026 | SECONDARY_ONLY |
| `itax.rebate.default` | income ≤ ₹12,00,000 → min(tax, ₹60,000), marginal relief above (s.156(2)) | 1 Apr 2026 | VERIFIED |
| `itax.cess_pct` | 4 | 1 Apr 2026 | SECONDARY_ONLY (section number `[NC]`) |
| `itax.employer_nps_deduction_pct` | 14 (s.124) | 1 Apr 2026 | SECONDARY_ONLY |
| `itax.form123_salary_threshold` | ₹1,50,000 (perquisite statement required above) | 1 Apr 2026 | VERIFIED (r.204(2)); issue date `[NC]` |
| `itax.prof_fee_tds` | s.393(1) Table Sl. 6(iii): 10% (FTS 2%), threshold ₹50,000 per tax year | 1 Apr 2026 | VERIFIED via pack LR-TAX-004 |
| `itax.contractor_tds` | s.393 serial, rate and threshold | — | **NOT_CONFIRMED** |
| `itax.deposit_due_dates`, `itax.late_fee` | per Income-tax Rules 2026 | — | **NOT_CONFIRMED** (ClearTax: interest 1%/1.5% per month; ₹200/day — section numbers absent) |
| `minwage.central.*` (from 1 Oct 2026) | Area A daily: clerical/skilled ₹1,024; highly skilled ₹1,111; unskilled ₹840; semi-skilled ₹933 | 1 Oct 2026 | SECONDARY_ONLY (binds central sphere only; order number `[NC]`) |
| `minwage.IN-DL.*` | ₹18,456 / ₹20,371 / ₹22,411 / ₹24,356 (unskilled / semi-skilled / skilled / graduate clerical) — vendor page, cycle unclear | — | **NOT_CONFIRMED** |
| `minwage.IN-UP/RJ/MH/KA.*` | not researched; load from State notifications (VDA cycles 1 Apr / 1 Oct) | — | **NOT_CONFIRMED** |

### Z.2.5 State rule packs — launch States (DL, UP, RJ, MH, KA) [RC F6.2, F7]
All values below are seeded `SECONDARY_ONLY` unless marked; each must be verified against the State Gazette before the first pay run that uses it.

| Item (`se.<state>.*`, `pt.<state>.*`, `lwf.<state>.*`) | Delhi | Uttar Pradesh | Rajasthan | Maharashtra | Karnataka |
|---|---|---|---|---|---|
| Daily / weekly hours | 9 / 48 | 9 / 48 (Amendment Act 2025, eff. 19 Nov 2025) | 10 / 48 (Bill No. 5 of 2026) | 10 / 48 (Ordinance 2025, eff. 1 Oct 2025; Act status `[NC]`) | 9 / 48 |
| Overtime quarterly cap | `NOT_CONFIRMED` | 144 h | 144 h | 144 h per 3 months | `NOT_CONFIRMED` |
| Overtime rate | 2× (CoW s.14) | 2× | 2× (S&CE Act s.8 1.5× superseded by CoW s.14 for covered employees — recommendation) | 2× | 2× |
| Earned/privilege leave | 15 days/yr after 12 months; accumulate 45 | 15 days; accumulate 45 (`NOT_CONFIRMED`) | 1 per 12 days after 240 days; carry 30; refused unlimited | 1 per 20 days (18 after 240 days); accumulate 45 | 18 days/yr; carry 30 |
| Casual / sick leave | CL 12 + SL 12 (`NOT_CONFIRMED` — conflicting sources) | CL 15; SL 5 or 15 (`NOT_CONFIRMED`) | none separate | CL 8 per calendar year, credited quarterly | SL 12 |
| Women night work | restricted (relaxation `[NC]`) | 19:00–06:00 with consent and safeguards | s.22 bar — check exemption notifications | 21:30–07:00 with consent | allowed |
| Festival/national holidays | Delhi Rules 1965 — count `[NC]` | 3 national + State festivals | `[NC]` | 4 national + 4 festival | KA Act 1963 — count `[NC]` |
| Professional tax | none | none | none | Men: nil ≤ ₹7,500; ₹175 (₹7,501–10,000); ₹200 above (₹300 in February); Women: nil ≤ ₹25,000 (conflict: ₹10,000 in older sources), ₹200 above (₹300 Feb) | nil < ₹25,000; ₹200 (₹300 in February) |
| LWF | ₹1 / ₹2 monthly — applicability conflict `[NC]` | no active private-sector LWF | not stated `[NC]` | ₹25 employee / ₹75 employer, half-yearly (June, December) | ₹50 / ₹100 annual (31 Dec); applies at 10 employees |
| Registration | mandatory vs "abeyance" conflict `[NC]` | 20+ employees | within 30 days (0–10 exemption `[NC]`) | 20+ non-managerial; below 20 intimation | electronic, deemed in 7 days; 10+ OSH-registered workers excluded (Act 38/2026) |
| Service certificate | — | — | — | — | within 7 days |

Other States' PT and LWF rows from [RC] F7 (WB, TN, GJ, TS/AP, others) are seeded `SECONDARY_ONLY` with the conflicts noted; States with no PT (DL, UP, RJ, HR, UK, HP and others listed in [RC] F7.1) are seeded with `value = none`. The constitutional ceiling of ₹2,500 per person per year (Art. 276(2)) is a Locked validator on every PT slab.

### Z.2.6 Rule-watch feed
`RuleWatchWorkflow` (owner: Payroll Compliance Officer; reviewer: Company Secretary) creates dated review tasks for VDA cycles (1 April, 1 October), the Union Budget, State budgets (PT), EPFO/ESIC circulars, State S&E amendments, DPDP phase dates (13 Nov 2026; 13 May 2027), bonus-ceiling and floor-wage notifications and Income-tax Rules due dates. New versions: maker `compliance_officer`, checker Company Secretary or `finance_controller`, legal-reviewer sign-off where employees' statutory rights are affected, preview against the last finalised run; old versions are never deleted.

---

## Z.3 Organisation model

### Z.3.1 Objects
| Object | Purpose | Key rules |
|---|---|---|
| **Legal entity** (`hr.legal_entities`) | Employer of record: Equator Resolution Service Private Limited first; group companies later | CIN, PAN, TAN, GSTIN, registered office, EPF establishment code, ESI code, Board-approved DoFP reference; linked to `grp` company record (Appendix AD) when available. Every employee has exactly one `employing_entity_id` at any time (NN-38; [RE] DI-E 24) |
| **Establishment** (`hr.establishments`) | A place of business of a legal entity (Delhi, Noida, Jaipur offices; a "remote hub" is not an establishment) | State, address, S&E registration number and validity, OSH registration (Form III), PT registration per State, LWF registration, holiday-calendar code; drives `establishment_state` |
| **Department** (`hr.departments`) | Functional unit; default list D3-06 | Rename, merge, add, retire; parent department; head (`department_head`); default cost centre; legal entity. Internal Audit has `independent = true` and reports to the Board/Audit function |
| **Cost centre** (`hr.cost_centres`) | Cost collection for budgets, ROI and inter-company recharges | Code, entity, owner, GL mapping (P05 chart of accounts), active dates |
| **Location / work-from-home state** | Where the employee actually works | `work_location_state` and `work_mode` (`office`, `remote`, `hybrid`) per effective date; WFH declaration (§Z.6.4) |
| **Position** (`hr.positions`) | Budgeted seat with job family, grade, band, worker-classification hint | Positions exist before people; a hire fills a position; vacant positions roll into the headcount plan |
| **Reporting line** | Solid-line manager | One solid-line manager per employee per date; cycles blocked (`HR_REPORTING_CYCLE`) |
| **Matrix / cross-functional assignment** (`hr.assignments`) | Dotted-line work for another department, project or group company | Percentage allocation (sum ≤ 100), start/end, dotted-line manager, purpose; cross-company assignments require a secondment (§Z.13) |
| **Headcount plan and budget** (`hr.headcount_plans`) | Annual plan by entity × department × cost centre × quarter | Approved positions, budgeted CTC (₹ minor units), hiring quarter; versioned; approval through `ctl` (DoFP row `HR-HC-PLAN`) |

### Z.3.2 Default department set (D3-06; configurable)
Leadership · Case Services (Registry and Case Management) · Neutral Relations and Panel · Onboarding and Implementation · Customer Success and After-Sales · Support and Grievance · Sales and Business Development · Marketing, Brand and Content · Social Media and PR · Partnerships and Collaborations · Training and Academy Liaison · Finance and Accounts · HR and Administration · Legal and Compliance · Technology and Information Security · Internal Audit (independent). **Management has not yet supplied Equator's departmental structure**; the seed is a default and the first-run wizard asks the HR head to confirm, rename or merge before any position is created.

### Z.3.3 Default job families and grades (seed; T tier)
Seed families: case services, customer and support, growth, corporate, technology, leadership, each with example positions and a worker-classification hint (case, support and technology roles default to `worker` unless duties are mainly managerial or administrative; leadership `non_worker`). Grades G1–G8 with salary bands (min–mid–max, ₹ per month) are tenant data; band edits are maker-checker (DoFP `HR-BAND-EDIT`).

### Z.3.4 Worker classification record (Locked logic; T-tier inputs)
Every employee has `worker_classification` ∈ {`worker`, `non_worker`, `uncertain`} computed by the pure function `wrk_is_worker()` (V5 §4.1; OSH s.2(1)(zzl); IR Code s.2(zr)) from `principal_duties`, `designation_category` and `monthly_wages_minor` against `osh.supervisory_wage_cap` (₹18,000). `uncertain` is treated as `worker`. The record stores the answers, the rule applied and reasons; it is reviewed at joining, on every role change and annually (`HR_WORKER_CLASSIFICATION_REQUIRED` blocks activation until done). The classification drives the leave floor, overtime eligibility and consent, OSH registers and IR routing [RC] F4.1, C.18.

---

## Z.4 Employee lifecycle

### Z.4.1 Lifecycle state machine (`hr.employees.status`)
`candidate_accepted → pre_joining → onboarding → probation → confirmed ⇄ (on_notice | suspended | on_secondment | long_leave) → exit_initiated → exit_effective → settled → archived`

| Transition | Guard | Event |
|---|---|---|
| `candidate_accepted → pre_joining` | Offer accepted (e-signed); position budget reserved | `equator.hr.offer.accepted.v1` |
| `pre_joining → onboarding` | Pre-joining checks complete (§Z.4.5) or approved exception; appointment letter issued and e-signed | `equator.hr.employee.created.v1` |
| `onboarding → probation` | Day-1 checklist: NDA, acceptable-use, staff code (U.4), POSH policy, information-security, confidentiality, privacy notice acknowledged; worker classification done; bank account verified and cooled (§Z.12.5) | `equator.hr.employee.activated.v1` (triggers workspace joiner) |
| `probation → confirmed` | Probation review approved (manager + HR); or deemed confirmation per policy | `equator.hr.employee.confirmed.v1` |
| `probation → probation` | Extension once (default ≤ 3 months; MSO template 6 + 3) with written reasons | `equator.hr.probation.extended.v1` |
| `* → on_secondment` | Signed secondment record (§Z.13) | `equator.hr.secondment.started.v1` |
| `* → suspended` | Disciplinary suspension with written order; subsistence allowance per policy (MSO template 50% for 90 days then 75%) | `equator.hr.employee.suspended.v1` |
| `* → exit_initiated` | Resignation submitted, termination approved (maker-checker), end of fixed term, retirement, death | `equator.hr.exit.initiated.v1` |
| `exit_initiated → exit_effective` | Last working day reached; for cause: decision recorded | `equator.hr.employee.exit_effective.v1` (X-57 revocations) |
| `exit_effective → settled` | F&F paid within `wrk_wages_2wd`; leave encashment paid; gratuity scheduled within 30 days | `equator.pay.fnf.paid.v1` |
| `settled → archived` | Clearance complete, experience/service certificate issued, records moved to retention class | `equator.hr.employee.archived.v1` |

### Z.4.2 Requisition with budget approval
1. A `department_head` (or delegate) raises a requisition against a vacant budgeted position, or for a new position with business case, CTC range, location/work mode and justification.
2. The engine checks the headcount plan: within budget → DoFP `HR-REQ-IN-BUDGET` (department head + `hr_manager`); outside budget or new position → `HR-REQ-OUT-BUDGET` (`ops_director` + `finance_controller`), exceeding plan by > 10% CTC → CEO designation (`HR_REQUISITION_BUDGET_EXCEEDED` until approved).
3. The approved requisition reserves budget and opens recruitment.

### Z.4.3 Recruitment
| Step | Specification |
|---|---|
| Job post | Generated from the position template; mandatory fields (role, location/remote eligibility, CTC range optional, application deadline); equal-opportunity statement; no question on religion, caste, marital status or other characteristic not needed for the role; Careers page on `apps/web` (P13) and optional external boards via manual hand-off (no scraping) |
| Candidate record | Minimal data: name, contact, CV, role-relevant experience, source, consent to process for this vacancy and (separately, optional) for future vacancies; privacy notice shown at application (DPDP s.5 format) |
| Screening | Structured criteria per position; AI may summarise a CV against stated criteria with `requires_human_review = true`; AI never ranks, rejects or scores candidates (NN-01 extended; §Z.18.5) |
| Interviews | Scheduled via `WORKSPACE_PORT.createMeeting` (calendar-backed Teams) or `VIDEO_PORT`; interviewers get a time-bound grant to that candidate only |
| Interview feedback | `hr.interview_feedback` per interviewer against the position's competency rubric (1–5 per competency + evidence text); submitted independently before seeing others' feedback |
| Offer approval | Offer within band → `hr_manager` + `department_head`; above band midpoint by > configured % or outside band → DoFP `HR-OFFER-ABOVE-BAND` (CEO designation + `finance_controller`); joining bonus or relocation → `finance_controller` |
| Decision record | Hire / reject / hold with reasons; candidates notified; retention §Z.18.3 |

### Z.4.4 Offer and appointment letter
- **Offer letter** (template `hr.offer_letter@v`) states position, grade, CTC with component breakdown, work mode, establishment and work-location State, probation, notice period, joining date, conditions (verification, documents).
- **Appointment letter** (template `hr.appointment_letter@v`, OSH format per OSH (Central) Rules — form number `[VERIFY — open: prescribed form number]`) is issued **to every employee** at appointment (OSH s.6(1)(f)); existing employees without one receive it within 3 months (clock `osh_appointment_letter_existing_3m`) [RC] F4.3. Contents include: employer identity, designation, category/skill, wage and components on the CoW s.2(y) basis, wage period and pay date, hours, leave entitlement, social-security coverage (UAN/ESI where applicable), notice, grievance channel, POSH IC details, and the employee privacy notice naming group entities and purposes ([RE] F5.1 item 4).
- Both are e-signed through `ESIGN_PORT`; the signed PDF/A is stored in the employee vault with SHA-256 (NN-10 pattern). Templates require legal-reviewer approval before activation (NN-33 G). An employee without a signed appointment letter is a ghost-employee indicator (§Z.12.6).
- **Engagement types** ([RC] F14.33): `employee`, `fixed_term_employee` (IR Code s.2(o): written contract, parity with permanent workers, pro-rata benefits, gratuity after 1 year), `apprentice`, `professional_engagement` (consultants, retained advocates — fee note, TDS s.393(1) Sl. 6(iii)), `contractor_staff` (via agency; principal-employer wage checks). A misclassification checklist (control, hours, exclusivity, tools, integration — *Dharangadhara Chemical Works v State of Saurashtra* AIR 1957 SC 264 [K]) warns before a `professional_engagement` is created for a role that looks like employment. A practising advocate is never modelled as a full-time salaried employee (BCI Rules Part VI Ch. II r.49 [K]).

### Z.4.5 Pre-joining documents and verification (consent, minimal data)
| Item | Required | Storage rule |
|---|---|---|
| Identity | One government ID; Aadhaar only by offline verification with masked reference (NN-14; App. S §3.3) — never the full number | Masked reference + verification result; image not retained after verification unless the employee chooses it as their ID proof |
| PAN | Yes (TDS s.392) | Encrypted `pan_enc`; `pan_hmac` for duplicate detection |
| UAN / previous ESI IP number | If any | Encrypted; duplicate check |
| Bank account | Own name; penny-drop / name-match verification (App. S §3.11) | `pay.bank_accounts`; cooling-off before first use (§Z.12.5) |
| Address, emergency contact | Yes | Standard tier |
| Education and employment proofs | Per role | Vault, restricted to HR |
| Previous-employer salary (Form 127) | If joining mid-year | `pay.prev_employment` |
| Background verification | Before access (Q SC-21): identity, education, employment, address; criminal-record check only where lawful and with specific consent | BGV vendor report in vault (`bgv_report` retention class); only pass/fail/discrepancy flags visible outside HR |
| Health information | Not collected at pre-joining. Disability accommodation requests are voluntary and stored sealed-style (`hr_health` tier High, HR head only) | — |
| Nomination forms | EPF, gratuity (CoSS s.55 after 1 year), CoW Form VII | Vault |

The candidate portal shows why each item is needed, its legal basis (DPDP s.7(i) employment purpose or consent) and its retention. Optional items are clearly marked and never block joining.

### Z.4.6 Joining and onboarding checklist (`hr.onboarding_tasks`; template per department)
1. Policy acknowledgements recorded as consent-ledger records of kind `undertaking` (FR-P01-27 pattern): staff code ESC-2026.1 (App. U §U.4), POSH policy and IC details, information-security and acceptable-use policy, confidentiality/NDA, employee privacy notice, workforce-measurement notice (NN-35, §Z.6.1), anti-bribery and gifts policy, conflict-of-interest declaration (§Z.12.10). Versions are pinned; re-acknowledgement on material change and annually for the staff code.
2. Equipment and assets assigned (laptop with MDM where SKU allows, security key for phishing-resistant MFA — App. S §2.6, phone, access card) with acknowledgement.
3. Work e-mail and access provisioning (§Z.5).
4. Equator platform roles requested through `ctl` role-grant approval with SoD check (§Z.12.4); case roles additionally require the conflict declaration and `ConflictIndex` refresh (App. S §6.5).
5. Mandatory training assigned (§Z.11.1): staff code, DPDP and information security, POSH awareness; case managers additionally ADR process training.
6. Buddy and 30/60/90-day check-ins scheduled.

### Z.4.7 Probation and confirmation
Default probation 6 months (T tier; MSO services template 6 + 3). Review form at T-30 days: goals met, competencies, conduct; outcomes `confirm`, `extend` (once, ≤ 3 months, reasons), `not_confirmed` (notice per contract; for workers, IR Code requirements apply). If no review is recorded by the end date, the policy setting `tenant.hr.probation.deemed_confirmation` (default true) applies and an exception is logged against the manager.

**Probation reminder ladder (`ProbationReviewWorkflow`; offsets T tier `tenant.hr.probation.reminder_offsets_days`, default 45/30/15/7/0).** T-45: manager notice with the review form pre-filled (goals, check-in notes, scorecard summary with data coverage, attendance, approved-leave days — shown so that leave is never read as under-performance). T-30: review task opens. T-15: reminder to the manager and the `department_head`. T-7: escalation to `hr_manager`; the department head may complete the review if the manager is on leave (§Z.12.2). T-0: confirmation is deemed (letter generated, exception logged) or, where `deemed_confirmation = false`, the status stays `probation` for at most 10 working days with a daily HR task; an `extend` or `not_confirmed` outcome requires written reasons visible to the employee before the end date, and an outcome recorded after the end date can only be `confirm`. Confirmation and extension letters are generated from templates and e-signed; the employee sees the outcome and reasons in `/me`. List view "Probations ending in the next 60 days" (filters: department, overdue, outcome) on SCR-P18-45. KPI: reviews completed by T-0 ≥ 95%; deemed confirmations < 10% of confirmations. *(v3.1)*

### Z.4.8 Transfers, role changes, promotions and secondments
Each movement is an effective-dated `hr.lifecycle_events` row (`transfer_department`, `transfer_location`, `change_work_mode`, `role_change`, `promotion`, `demotion`, `grade_change`, `manager_change`, `entity_transfer`, `secondment_start/end`). Compensation effects go to `pay.employee_compensation` as a new version with approval through `ctl` (DoFP `HR-COMP-REVISION`). A change of `work_location_state` re-evaluates minimum wage (higher-of), holiday calendar options, PT/LWF (per D3-31) and WFH declaration. `role_change` emits `equator.hr.employee.role_changed.v1`, which drives the workspace mover diff and an access re-certification of affected platform roles. `entity_transfer` (moving the employer of record to another group company) is a separation from one entity and a joining at another with continuity-of-service recorded by agreement, never a silent field edit (`HR_ENTITY_TRANSFER_REQUIRES_REJOIN`).

### Z.4.9 Exit
| Step | Specification |
|---|---|
| Initiation | Resignation (employee self-service, with reason taxonomy); termination (manager + HR + DoFP `HR-TERMINATION`; for workers, IR Code checks; protected-status check §Z.12.11); end of fixed term; retirement; death (nominee workflow) |
| Notice | Contractual notice; buy-out or waiver recorded with approval; Rajasthan S&E s.28A/28B one month after 6 months' service where that Act applies [RC] F5; retrenchment rules (IR Code s.70) for workers |
| Clearance (`hr.exit_clearances`) | Parallel tasks: manager hand-over, IT (assets, access), finance (advances, loans, petty cash, corporate card), HR (documents, vault), case services (re-assignment of open matters with party-notice where required), legal hold check |
| Access revocation | X-57: Equator platform ≤ 60 s; workspace ≤ 4 h; for cause immediate. Shared-mailbox conversion and OneDrive transfer to manager at T+1 day; account deletion only after 90 days (30–365) and no legal hold, open grievance, POSH matter or disciplinary case (`HR_WORKSPACE_DELETE_BLOCKED_HOLD`) [RD DI-A 4, 6] |
| Asset return | Checklist with condition; recovery of loss only as a CoW s.18 deduction with prior intimation, within the 50% cap (§Z.9.5) |
| Full and final settlement | Computed by `FnfWorkflow`: salary to last working day, leave encashment (OSH s.32(1)(vi)), notice pay/recovery, bonus pro-rata where applicable, gratuity (separate clock, 30 days), reimbursements, loan recovery within caps, TDS; **paid within 2 working days** of the separation event (CoW s.17(2); clock `wrk_wages_2wd`). No F&F may waive statutory dues (canonical Appendix F code `STATUTORY_WAIVER_FORBIDDEN`; sub-code alias `WRK_STATUTORY_DUES_WAIVER`) |
| Documents | Relieving letter, experience/service certificate (default within 7 days), Form 130 for the tax year, F&F statement, PF transfer guidance |
| Records | Employee file moves to retention class `hr_employee_file` (§Z.18.3); exit interview (optional, anonymous aggregation n ≥ 5) |

---

## Z.5 Work e-mail and access provisioning (workspace connector)

### Z.5.1 SKU position
Management refers to "Microsoft 365 Business Starter". Microsoft has no plan by that name; "Business Starter" is a Google Workspace edition; the likely plan is **Microsoft 365 Business Basic** [RD F1.1]. **D3-04: the Company Secretary confirms the SKU** from the admin centre (Billing → Your products) or `GET /subscribedSkus` (`O365_BUSINESS_ESSENTIALS` is commonly Basic — `[VERIFY — open: tenant SKU]`). The design works on Business Basic and lights up extra controls on Standard or Premium through the capability matrix.

Basic has security defaults (no Conditional Access), Basic Mobility only (no Intune or Defender for Business), retention policies for Teams only, and an India data-residency commitment; Business Premium adds Entra ID P1, Intune P1 and Defender for Business; Google Business Starter has no Vault and no India data region [RD F1.2, F1.3, F2; capability matrix RD DI-A 2, seeded into `core.integration_providers.capabilities`].

**Consequences (Locked).** (1) M365/Google is never the system of record for any HR record (D3-30). (2) Roles that open staff consoles with sealed, Tier-High or financial access require a SKU with Conditional Access and MDM, or a recorded security-lead exception ≤ 90 days (`HR_WORKSPACE_SKU_INSUFFICIENT`, 409) [RD DI-A 3]. Default SKU rules (`tenant.hr.workspace.sku_rules`, T tier with maker-checker): console, finance, HR and payroll roles → Business Premium; everyone else → Business Basic; contractors → no mailbox (guest access only). (3) Case data never enters the workforce suite (hearings on `VIDEO_PORT`, notices on `EMAIL_PORT`/SES) [RD DI-A 7].

### Z.5.2 `WORKSPACE_PORT` (from [RD] DI-A 1; adapters `m365_graph` default, `google_workspace` stub behind `ops.workspace.google.enabled` OFF, `manual_it_desk` fallback)
Operations used by the HRMS: `capabilities()`, `createAccount()`, `setLicences()`, `setGroups()`, `suspend()`, `convertToShared?()`, `transferFiles?()`, `deleteAccount()`, `createMeeting()`, `pullAuditLogs()`. Microsoft Graph mapping (application permissions, app registration `eq-hrms-provisioner`, certificate credential in AWS Secrets Manager, rotation ≤ 90 days):

| Step | Graph call | Permission | Notes |
|---|---|---|---|
| Create user | `POST /users` (`accountEnabled`, `displayName`, `mailNickname`, `userPrincipalName`, `passwordProfile.forceChangePasswordNextSignIn = true`) | `User.Create` | UPN pattern `{first}.{last}@<domain>`; collision → middle initial, then number; Indic names transliterated by a stored table |
| Set usage location | `PATCH /users/{id}` `usageLocation = "IN"` | `User.ReadWrite.All` | Required before licensing `[NC]` — always set |
| Assign licence | `POST /users/{id}/assignLicense` | `LicenseAssignment.ReadWrite.All` | Direct assignment on Basic (group-based licensing P1 dependency `[NC]`); poll `GET /users/{id}/mailboxSettings` until 200 (delay `[NC]`) |
| Groups / DLs | `POST /groups/{id}/members/$ref` | `GroupMember.ReadWrite.All` | Department, location (Delhi/Noida/Jaipur/remote) and role groups from HRMS org units; Teams membership follows the group |
| Temporary credential | — | — | Sent only to the personal e-mail/mobile on file via `EMAIL_PORT`/`MESSAGING_PORT`; never to the manager |
| Disable (leaver) | `PATCH /users/{id}` `accountEnabled = false`; `POST /users/{id}/revokeSignInSessions`; remove groups | `User.ReadWrite.All` | ≤ 4 h (X-57) |
| Shared mailbox | Exchange Online PowerShell runner (not Graph) `[NC]` | — | T+1 day; licence then removed |
| Delete | `DELETE /users/{id}` | `User.ReadWrite.All` | Only via deletion guard |

Throttling: honour `429` + `Retry-After`; map to `ProviderErrorKind = RATE_LIMITED`; bulk backfills use `x-ms-throttle-priority: low` [RD F1.3]. Google adapter (when enabled): Directory API `POST …/admin/directory/v1/users`, `suspended` field for leavers, licences via Enterprise License Manager `[NC]`, service account with domain-wide delegation `[NC]`; residency warning shown because no India region is offered [RD F2].

### Z.5.3 Joiner–mover–leaver workflow (`WorkspaceJmlWorkflow`, Temporal)
- **Joiner** on `equator.hr.employee.activated.v1`: requires BGV pass, NDA and acceptable-use e-signed (Q SC-21) — otherwise `HR_PREJOIN_CHECKS_INCOMPLETE`. Steps: resolve SKU by rule → create → usage location → licence → groups → temporary credential → record `hr.workspace_accounts` (`external_id`, `upn`, `sku`, `provider`) → link to Keycloak workforce identity (App. S §1.3) so `/staff/login` works.
- **Mover** on `equator.hr.employee.role_changed.v1`: diff groups and SKU; downgrade from Premium is blocked while a console role remains.
- **Leaver** on `equator.hr.employee.exit_effective.v1`: X-57 timings; then mailbox conversion, file transfer to manager, licence removal; deletion after the configured delay through the deletion guard.
- **Manual fallback** (`manual_it_desk`): creates an IT ticket with the same checklist and SLA clock; the `it_admin` records completion with evidence; the SLA report treats manual and automatic steps identically.
- Every step writes `audit.append_event` and an `hr.jml_events` row (`employee_id`, `step`, `requested_at`, `completed_at`, `provider_ref`, `sla_met`). Collector `jml_sla_report` (daily) feeds Q §7.3 evidence: joiners without completed checks = 0; leaver revocations within SLA = 100%.

---

## Z.6 Attendance and work time (NN-35)

### Z.6.1 Workforce-measurement notice (Locked content headings; text T tier with legal review)
Before any attendance or work data is captured, the employee receives and acknowledges a notice (English and Hindi; other Eighth-Schedule languages on request) that lists, for **each** data source: what is captured, purpose (security, attendance and statutory registers, operations), lawful basis (DPDP s.7(i) employment purpose, legal obligation for OSH s.33 registers, or consent for optional items), who can see it, retention, how to view one's own data and how to dispute it. Changes to the notice are versioned; adding a new source requires DPO approval and re-notice before the source is switched on (`HR_MONITORING_APPROVAL_REQUIRED`).

### Z.6.2 Capture methods
| Method | Default | Conditions |
|---|---|---|
| Web/mobile clock-in and clock-out in `apps/ops` / `apps/mobile` | ON | One tap; optional note; offline queue on mobile |
| Session log (sign-in/sign-out to Equator platform and workspace) | ON | Used to *suggest* attendance; the employee confirms; never inferred as work quality |
| Shift and roster | ON for rostered teams (support, case services) | Published ≥ 7 days ahead (T tier); swap requests with manager approval |
| Coarse location at check-in only | OFF | City-level; only with notice; never continuous |
| Approved-network check (office egress IP / ZTNA) | OFF | Only with notice; used for "office" attendance mode |
| Geofence for office attendance | OFF (`hr.attendance.geofence.enabled`) | Office premises only, working hours only, notice + DPO approval |
| Biometric attendance | OFF (`hr.attendance.biometric.enabled`) | Templates held only on device/vendor with SPDI-grade consent, never in HRMS [RC D.20] |
| Idle-time / active-window sampling | OFF; team aggregates only if ever enabled | High-risk; opt-in team dashboards, no individual ranking, never outside working hours [RC F12.2] |

**Locked OFF (cannot be enabled by any tenant role; CI test `NN-35_monitoring_prohibited`):** keystroke logging; webcam capture or face-presence detection; covert or continuous screen recording; screenshots of personal devices; off-hours location tracking; reading personal e-mail or private messages; BYOD personal-area access; use of Teams/Meet presence or meeting attendance in performance scoring (Google states the Meet API "isn't intended for performance tracking or user evaluation" [RD F2]). Attempted configuration returns `HR_MONITORING_PROHIBITED` (403).

**Governed exception:** screenshots or screen recording of a **company** device for a specific investigation or regulated-data role only, and only because the workforce-measurement notice (§Z.6.1) discloses this category in advance (so it is never covert monitoring under NN-35; never on personal devices) — approved by `dpo` + `hr_manager` + legal reviewer, per named employee, time-boxed ≤ 30 days, logged, and disclosed to the employee after closure unless disclosure would prejudice the investigation; flag `hr.monitoring.investigation_capture.enabled` OFF until counsel sign-off [RC D.22]. Captures are deleted at case closure + 1 year unless under legal hold.

### Z.6.3 Daily register and hours
`AttendanceDailyCloseJob` (02:00 IST) builds `hr.attendance_days` per employee: status (`present`, `remote_present`, `half_day`, `leave:<type>`, `holiday`, `weekly_off`, `absent`, `on_duty`, `comp_off`), first-in, last-out, worked minutes (sum of confirmed sessions), break minutes, overtime minutes. Registers Form IX (attendance-cum-muster roll) and OSH s.33 registers are generated from it [RC F2.9, F4.7].

| Rule | Default | Tier |
|---|---|---|
| Normal day / week | 8 h / 48 h (OSH s.25; Central Rules); company standard week 40 h | L floor; T company standard |
| Rest interval and spread-over | per State pack (e.g., DL rest after 5 h, spread-over 10.5 h; RJ/MH rest after 6 h, spread-over 12 h) | G |
| Weekly rest | ≥ 1 day; never more than 10 consecutive days without rest | L (Wages Central r.6) |
| Max days per week | 6 (OSH s.26) | L |
| Overtime eligibility | `worker` classification; managerial staff tracked for wellbeing only | L |
| Overtime consent | Prior written consent per instance or standing consent (revocable) before OT is rostered or approved (OSH s.27) | L |
| Overtime rate | ≥ 2× normal rate, daily or weekly basis whichever is more favourable; daily rate = monthly ÷ 26 | L (CoW s.14; OSH s.27) |
| Rounding | 15–30 min = 30 min; > 30 min = 1 h | G |
| Quarterly OT cap | State parameter (144 h in UP, RJ, MH); blocks approval above cap (`HR_OVERTIME_QUARTERLY_CAP`) | G |
| Women night work | Before 06:00 / after 19:00 only with recorded, revocable consent; safety helpline shown; office night work needs the transport/CCTV checklist; for remote night work consent, POSH and helpline duties still apply `[VERIFY — open: counsel confirm remote application]` | L/G |

### Z.6.4 Work-from-home declarations
Each remote or hybrid employee files a WFH declaration (annually and on change): work address State and city (not the full address unless needed for statutory purposes), safe-workspace self-check, connectivity, use of company device, confidentiality of the home workspace (no case discussions audible to others; screen privacy), and acceptance that the virtual workplace is a workplace for POSH purposes [RC F6.3, F9]. The declaration sets `work_location_state`; a change triggers D3-31 re-evaluation. Equator does not inspect homes.

### Z.6.5 Regularisation
Employees request correction of a missed punch or wrong status within `tenant.hr.attendance.regularisation_window_days` (default 7, max 30, T). Manager approves; HR approves bulk regularisations; repeated regularisations above a threshold create a gentle notice, not a penalty. After payroll freeze, corrections flow as arrears in the next run. Any CoW deduction for absence needs prior intimation and a 7-day reply window (r.17) — the engine blocks the deduction until the window passes (`PAY_FINE_EVIDENCE_MISSING`).

### Z.6.6 Employee view, disputes and retention
- **My time** screen shows every captured record about the employee, its source and the retention date. An employee may dispute any record (`hr.data_disputes`); disputes are resolved by the manager within 5 working days, escalate to HR, and the outcome is visible. Disputed data is excluded from appraisal until resolved.
- **Dispute versus reply.** A *dispute* challenges whether a record is correct (it can change the data); a *reply* adds context to a correct figure (it never changes the data). Both are available on every attendance, scorecard and ROI figure the employee can see (§Z.7.4). *(v3.1)*
- **Retention:** raw session telemetry 1 year (DPDP Rule 8(3) floor) then aggregated to daily attendance; daily attendance registers 5 years after last entry (Wages Central r.51); investigation captures as above [RC D.23].
- **No adverse action on telemetry alone:** any disciplinary step relying on attendance or system data requires a human-reviewed explanation opportunity (MSO inquiry norms) [RC D.24].

---

## Z.7 Work measurement, scorecards and ROI dashboards

### Z.7.1 Principle
Work is measured from **work the platform already records**, not from surveillance (NN-35, D3-33). Each measurable action emits a normalised `hr.work_items` row via event subscription: `source_context` (`cases`, `ops.tickets`, `ops.onboarding`, `ops.handoffs` *(v3.1: lead-to-cash hand-off accepted within its SLA, Appendix X §X.4.14 — outcome-based, never time-on-screen)*, `mkt.campaigns`, `mkt.content`, `grm`, `ctl`), `action_code`, `actor_employee_id`, `occurred_at`, `sla_due_at`, `sla_met`, `effort_class` (configured standard minutes), `quality_review_id` (if sampled), `feedback_id` (if any). Payloads carry IDs and codes only — **no case content** and no party PII enter `hr` (NN-16 extended; NN-38).

### Z.7.2 Metric catalogue (seed; T tier, metric definitions maker-checker)
| Role | Metrics (examples) | Excluded (Locked) |
|---|---|---|
| Case manager | Matters handled (active, opened, closed administratively); timeliness of notices (served before due, % on time); scrutiny/deficiency cure time (median days from deficiency notice to cure); hearing logistics readiness (room, bundle, interpreter on time); QA score from sampled maker-checker reviews; party process-satisfaction score (process only, n ≥ 5 per period, X-28 small-number rule) | **Settlement rate, award outcomes, who won, amounts recovered, neutral selection, speed of outcome** — staff must never be incentivised on outcomes (App. U §U.4 items 1–3; NN-28 by analogy). Configuring such a metric returns `HR_METRIC_OUTCOME_FORBIDDEN` (422) |
| Support agent / lead | First-response and resolution SLA attainment; reopen rate; QA score; CSAT (n ≥ 5) | Talk-time ranking without quality context |
| Onboarding, customer success, finance, HR, payroll, engineering | Milestones and close tasks on time; checklist completeness; reconciliation breaks; post-run payroll corrections; planned vs delivered items; change-record compliance | Revenue commission on anything touching case outcomes; lines of code or commit counts |

### Z.7.3 SLA adherence, quality reviews and feedback
- **Quality reviews:** `quality_officer` (cases) or team leads (other queues) review a random sample (default 5% per employee per month, minimum 3 items; T tier) using a rubric; the reviewer cannot be the employee or the employee's maker on that item (maker-checker); the employee sees the review and can respond.
- **Customer feedback:** post-interaction surveys (process questions only); responses shown to the employee only in aggregate at n ≥ 5; free-text visible after PII redaction.
- **Goal completion:** from Z.10 (OKRs).

### Z.7.4 Role scorecards (`hr.kpi_scorecards`)
Each role has a scorecard template: up to 8 KPIs, each with definition, data source, target, weight, floor/ceiling, and an "explain" text. Scores are computed monthly; the scorecard shows the raw numbers, the data coverage (e.g., "3 of 4 weeks; 1 week on approved leave excluded"), and links to underlying work items. Scorecards inform, but never automatically decide, appraisal ratings, increments or discipline.

**Fairness explanation and right of reply (Locked behaviour; windows T tier).** Every KPI tile on the "Work summary" (employee, manager and HR views alike) carries an **Explain** panel listing: the formula and metric-definition version; data coverage; each normalisation applied (approved leave including maternity, holidays, part-time ratio, probation ramp-up, secondment allocation, training time, system outages declared in `eng` incidents, queue mix by `effort_class`); the team median at n ≥ 5 (never a named peer); and open disputes. The employee may add a **reply** (`hr.work_replies`: `period`, `kpi_code`, text ≤ 2,000 characters, optional evidence links) within `tenant.hr.work_summary.reply_window_days` (default 10 working days after the monthly scorecard is published; minimum 5). A reply is shown, unedited and time-stamped, to everyone who can see that figure, is attached automatically to the probation, check-in, calibration and PIP packets for the period, and cannot be edited or hidden by the manager or HR (only redacted for third-party personal data, with the redaction logged). A manager who opens a figure that has a reply sees the reply first. Event `equator.hr.work_reply.added.v1`. KPI: replies acknowledged by the manager within 5 working days ≥ 90%. *(v3.1)*

### Z.7.5 Utilisation vs capacity
Capacity = scheduled hours − approved leave − holidays − training time; utilisation = standard minutes of completed work items ÷ capacity, shown at team level by default. Thresholds: < 60% (under-loaded) and > 110% (over-loaded, wellbeing alert to the manager and HR). Over-load alerts are a duty-of-care signal, not a performance signal.

### Z.7.6 ROI-per-employee dashboards for management (fairness safeguards)
| Element | Specification |
|---|---|
| Cost | Fully loaded monthly cost = CTC + employer statutory contributions + allocated overheads (configurable allocation keys) from `pay` and cost centres |
| Output | Weighted standard output units from work items, plus attributed revenue only where a revenue stream is directly attributable (e.g., sales-closed subscriptions) — never case-outcome-linked revenue |
| Views | Department and team ROI: ON for `ops_director`, `department_head` (own departments), `finance_controller`. **Individual ROI:** OFF by default (`hr.analytics.individual_roi.enabled`); when enabled after a DPIA approved by the DPO and HR head, visible only to the employee, the direct manager and HR |
| Safeguards (Locked) | Normalised for leave (incl. maternity), part-time, probation ramp-up, secondment allocation and role mix; protected characteristics (gender, religion, caste, disability, age, union membership) are never inputs; every number has an "explain" panel with formula and data coverage; no automated adverse action; minimum cohort size n ≥ 5 for comparisons; pay-equity analysis on the CoW s.2(y) second-proviso basis (HRA, conveyance, overtime included) per CoW s.3 [RC F2.8] |
| Contestability | Employee can view and dispute inputs (§Z.6.6); disputes freeze the affected period's individual figures |
| AI | `analytics_narrator` may describe trends in aggregate dashboards with `requires_human_review = true`; it never ranks individuals or recommends personnel actions (NN-01 extended) |

---

## Z.8 Leave engine

### Z.8.1 Two-layer model [RC C.13]
- **Layer 1 — statutory floor** (computed per employee per day): OSH s.32 if the employee is a `worker` in an establishment with ≥ 10 workers; the State S&E Act of `establishment_state` where covered; maternity under CoSS; any more favourable State benefit (MoLE FAQ Q25).
- **Layer 2 — company policy** (tenant-configurable, T tier) may only be **equal to or more generous than** Layer 1 on every dimension (days, accrual, eligibility, carry-forward, encashment). The validator rejects any policy that undercuts the floor for any employee class (`HR_LEAVE_POLICY_BELOW_FLOOR`, 422) and shows the failing class and State.

### Z.8.2 OSH s.32 annual leave (floor for workers) [RC F4.5]
Eligibility 180 days worked in the calendar year; accrual 1 day per 20 days worked (1 per 15 for adolescents); lay-off, maternity leave and annual leave count toward 180 but do not earn leave; holidays within leave excluded; a worker joining after 1 January earns leave after working one-fourth of the remaining days; carry-forward capped at 30 days, refused leave carried forward without limit; encashment on demand at year-end, leave above 30 days encashable; wages in lieu of accrued leave on separation within 2 working days (discharge, dismissal, quitting) or 2 months (superannuation, death); applies to workers and supervisors earning ≤ ₹18,000 (MoLE FAQ Q20); no cap on encashment (Q26).

### Z.8.3 Equator Standard policy (D3-32; default template `leave.equator_standard@2026.1`)
| Leave type | Default | Notes |
|---|---|---|
| Earned / privileged | 18 days/year, accrual 1.5 days/month, from day one, pro-rated | ≥ OSH 1:20 and MH/KA 18 |
| Carry-forward | Up to 45 days; excess above 45 auto-encashed at calendar year-end; OSH workers may request encashment above 30 | meets DL/MH 45 accumulation |
| Refused leave | Never lapses | OSH s.32 |
| Casual | 8 days/calendar year | MH credited quarterly; DL/UP figures `[NC]` |
| Sick | 12 days/year (medical certificate after 2 consecutive days, T tier) | KA SL 12 |
| Holidays | 10 paid holidays: 3 national (26 Jan, 15 Aug, 2 Oct — Locked) + State festival list | MH requires 4 national + 4 festival — State pack overrides upward |
| Maternity | 26 weeks; eligibility 80 days in preceding 12 months; medical bonus ₹3,500; miscarriage/MTP 6 weeks; tubectomy 2 weeks; two nursing breaks until child is 15 months; no dismissal during maternity absence; WFH after maternity leave by mutual agreement | CoSS Ch. VI [RC F3.4]; WFH section number `[NC]` |
| Paternity, adoption, bereavement, marriage, study, sabbatical | Company policy; defaults: paternity 5 working days, bereavement 3 days | No statutory source in [RC]; T tier, management decision `[VERIFY — open: product decision on defaults]` |
| Leave without pay (LWP) | On exhaustion or by request | Feeds payroll as absence (§Z.9.4) |
| Compensatory off | Earned for approved weekly-rest or holiday work (or OT pay for workers, employee's choice where lawful) | Expiry default 60 days (T) |
| On duty / training | Not leave; attendance status | — |

**State uplift (Locked logic).** The validator compares every template value with each launch-State floor in §Z.2.5; where the floor is higher, the employee's entitlement is the floor (most-favourable rule, MoLE Additional FAQ Q25). At seed this raises earned leave for `IN-RJ` establishments (1 day per 12 days worked after 240 days ≈ 20–22 days/year) and would raise casual leave for `IN-DL` (12) and `IN-UP` (15) once those `NOT_CONFIRMED` values are verified. For `IN-MH` the total of 10 paid holidays already exceeds the State's 8, so the uplift changes the **composition** rather than the count: the calendar must contain at least 4 national and 4 festival holidays among the 10 (the validator rejects an `IN-MH` calendar with fewer than 4 national days) *(v3.1)*.

**How a days-worked floor is applied (true-up).** Equator Standard accrues 1.5 days a month from day one; a floor that depends on days actually worked (OSH s.32 1:20; RJ 1:12 after 240 days) can only be known at the end of the calendar year. `LeaveYearEndJob` therefore computes, per employee, `floor = applicable floor(days_worked)` and `credited = Equator accruals for the year`; where `floor > credited` it posts a ledger entry `floor_true_up` for the difference before carry-forward and encashment are calculated; it never debits. On separation the same computation runs on the days worked to the last working day, so leave encashment uses the higher figure. Worked examples (golden tests `HR_leave_true_up_*`): (a) RJ employee, 252 days worked → floor ⌊252 ÷ 12⌋ = 21; credited 18 → true-up 3 days; (b) RJ employee, 230 days worked (below 240) → RJ floor nil; 18 days stand; (c) OSH worker in DL, 252 days worked → floor ⌊252 ÷ 20⌋ = 12; credited 18 → no true-up; (d) joiner on 1 August → accrual 1.5 × 5 = 7.5 days to 31 December. *(v3.1)*

Tenants (and chambers via `chm`) choose the "Statutory minimum" (`leave.statutory_minimum@2026.1`) or "Equator Standard" (`leave.equator_standard@2026.1`) templates and may customise above the floor.

### Z.8.4 Policy engine features
Holiday calendars per State and year (`core.holiday_calendars`; national holidays Locked; festival holidays editable within the State count; remote staff get the `establishment_state` calendar with an optional `work_location_state` festival swap) [RC C.15]; sandwich rule (default not counted); half days; planned-leave notice (default 7 days); maximum consecutive days; documents; negative balance (default 0); calendar leave year; monthly accrual; encashment caps above the floor; approval chain (department head above 10 consecutive days); refusals carry written reasons and are recorded as "applied and refused" for carry-forward.

**Leave planner and team coverage rules (T tier; `tenant.hr.leave.coverage.*`).** Each team (department, roster group or queue) may define: `min_on_duty_pct` (default 60%), `min_headcount_by_role` (e.g., at least one `payroll_maker` and one `payroll_checker` present in pay-run week), `blackout_windows` (e.g., inputs-freeze to `bank_confirmed` for payroll; quarter-end close for finance) with a reason, and `mode` = `warn` (default) or `require_second_approval`. At request time the planner shows the team calendar (types hidden from peers, §Z.8.5), the projected coverage for each requested day, and up to three alternative windows of the same length that keep coverage; the approver sees the same projection. Coverage rules **never block or delay** maternity, sick, bereavement, statutory or court-ordered leave, comp-off expiry or leave needed to avoid lapse; and a refusal on coverage grounds must carry the coverage reason, is recorded as "applied and refused" (OSH s.32 carry-forward), and prompts the approver to offer an alternative date. An optional January **leave plan** (non-binding windows) flags weeks that would breach coverage; from 1 October employees whose balance would exceed the carry-forward cap get a monthly **lapse-risk** nudge. KPIs: coverage breaches per team-month; coverage refusals; balances above cap at 31 December. *(v3.1)*

### Z.8.5 Balances, calendar and payroll feed
`hr.leave_ledger` is append-only (grants, accruals, debits, reversals, encashments, lapses) — balances are derived. Team calendar shows "On leave" without type to peers; managers see type for approval only; sick-leave reasons and medical certificates are visible to HR only. Approved LWP and unauthorised absence (after the r.17 intimation window) feed the payroll input freeze as absence days.

---

## Z.9 Payroll engine

### Z.9.1 Component register and statutory classes (Locked logic)
Every pay component carries a fixed `statutory_class` [RC B.6]:

| Class | Members (default India set) | Effect |
|---|---|---|
| `WAGE_CORE` | Basic, DA, retaining allowance | Always wages (CoW s.2(y)) |
| `EXCLUDED_A_TO_I` (tagged with the s.2(y) letter) | (a) contractual bonus outside terms, (b) house accommodation/amenities value, (c) employer PF/pension contribution, (d) conveyance, (e) special-expense reimbursement, (f) HRA, (g) award/settlement sums, (h) overtime allowance, (i) commission | Counted in the 50% test; excess deemed wages; (d), (f), (g), (h) count as wages for equal-pay and wage-payment purposes |
| `EXCLUDED_J_K` | Gratuity, retrenchment compensation, retirement benefit, ex gratia on termination | Outside the 50% test (MoLE FAQ Q3) |
| `NOT_WAGES` | Performance incentives, ESOPs, variable pay, reimbursements against bills, annual performance incentive, leave encashment | Not wages (MoLE FAQ Q3, Q5; Mar FAQ Q4) |
| `IN_KIND` | Food coupons, ration items, mobile recharge | Counted as wages up to 15% of total wages (Mar FAQ Q18) |

Tenants may add components only by choosing a class; the class is locked once the component is used in a finalised run (`PAY_COMPONENT_CLASS_LOCKED`, 409).

### Z.9.2 Statutory wage calculator (`wage_code_base()`, pure)
`wage_code_base = core + max(0, excluded_a_to_i − cap% × total_remuneration)` where `cap% = cow.wage_definition.exclusion_cap_pct` (50) and total remuneration excludes statutory employer contributions and statutory bonus (MoLE Mar FAQ Q1, Q1b). It runs on every structure save and every pay run and is the base for EPF, ESI, gratuity, bonus, leave encashment and overtime. **Golden test:** total ₹76,000, cap ₹38,000, allowances ₹40,000 → excess ₹2,000 added to basic + DA ₹20,000 → statutory wages ₹22,000 (MoLE Jan FAQ Q7). A CTC template yielding core < 50% raises `wage_definition_warning` (LR-LAB-003) and cannot be finalised unless the add-back is applied (`PAY_WAGE_DEFINITION_BREACH`, 422). Restructuring an existing employee's pay to comply must not reduce wages or benefits to avoid contributions (CoSS s.124) and may need IR Code s.40 notice of change for workers (21 days [K]) — the restructure wizard shows both checks.

### Z.9.3 Salary structures (CTC → components)
- Structure templates per grade/band: CTC input → monthly components (Basic, DA if used, HRA, conveyance, special allowance, employer EPF/ESI/LWF, gratuity provision, NPS employer contribution (≤ 14% deductible, s.124), statutory bonus provision where applicable, flexible-benefit buckets (`NOT_WAGES` reimbursements)).
- The structure preview shows: monthly gross, employer contributions, statutory wage base, employee deductions estimate, net estimate, CTC reconciliation, and the 50% test.
- Minimum-wage check: wage base for the employee's category ≥ `minwage.<state>.<category>.<area>` for the **higher** of establishment and work-location State (D3-31); failure blocks activation of the compensation version (`PAY_MIN_WAGE_BREACH`, 422). Where the State schedule is `NOT_CONFIRMED`, the check is a warning requiring Payroll Compliance Officer acknowledgement.
- Compensation versions (`pay.employee_compensation`) are effective-dated; revisions go through DoFP `HR-COMP-REVISION` and create arrears automatically for back-dated effective dates.

### Z.9.4 Monthly cycle (`PayRunWorkflow`)
| Stage | Owner | Controls |
|---|---|---|
| 1. Calendar | `payroll_maker` | Pay date ≤ statutory deadline (before 7th of next month, CoW s.17(1)); calendar set annually; pay date edit is T tier within the deadline |
| 2. Inputs open | HR, managers, employees | Attendance close, approved leave/LWP, overtime (with consent), new joiners/exits, compensation changes, reimbursements approved in `ctl`, loans/advances, arrears, one-time earnings/deductions with approvals, tax declarations/proofs |
| 3. Inputs freeze | `payroll_maker` | Freeze date (default 25th, T); late items roll to next run as arrears; freeze snapshot hashed |
| 4. Calculation | System | Deterministic library (X-58); each line stores `param_version_id`, `component_id`, `basis`, `formula_ref` |
| 5. Variance review | `payroll_maker` | Variance report vs previous run: headcount, gross, net, employer cost, per-employee change > 10% (T), new bank accounts, new joiners paid in the same run, exits still paid; every flagged line needs a reason (`PAY_RUN_VARIANCE_UNREVIEWED`) |
| 6. Ghost and anomaly gate | System | §Z.12.6 hits; unresolved critical hits block (`PAY_GHOST_HITS_UNRESOLVED`) |
| 7. Maker approval | `payroll_maker` | Submits run for approval; parameter acknowledgements (§Z.2.4) |
| 8. Checker approval | `payroll_checker` (HR side) then `finance_controller` (Finance side) | Maker ≠ checker (DB CHECK; `PAY_MAKER_CHECKER_SAME_USER`); checker not in maker's reporting line for self-related lines; step-up `aal2-pr` ≤ 10 min; DoFP `PAY-RUN-APPROVE` |
| 9. Bank file / payout | `finance_ops` (release) | Bank file generated only from the approved run by the `bank_file` adapter of `PAYOUT_PORT` (the same adapter serves chambers disbursal, Appendix W §W.6.10); SHA-256 recorded; no manual edit of the file; bank-only payment (CoW s.15); release needs a distinct approver from the checker (NN-36); optional `PAYOUT_PORT` route behind `pay.payout.api.enabled` OFF (bank/vendor contract) |
| 10. Bank acknowledgement | `finance_ops` | Bank response file hash and per-line status reconciled; mismatches raise `PAY_BANK_FILE_HASH_MISMATCH`. *v3.1:* a failed or returned line is **never re-sent from the original file**: it becomes a line hold with reason `bank_return` and is re-paid only through an off-cycle run after the account is re-verified (compensation step; same rule as Appendix W §W.6.8 step 9); no acknowledgement 3 working days after the pay date raises a P2 alert to `finance_ops` and the `payroll_checker` (`DisbursalAckWatchJob`, shared with chambers runs); where the re-payment cannot be made before the statutory deadline the CFO/CS decision rule of `PAY_HOLD_PAST_DEADLINE` applies |
| 11. Payslips | System | Wage slip (Form V-style) on or before payment (Wages Central r.52), in English and Hindi; employee self-service download |
| 12. Statutory challans and returns data | `payroll_checker` | EPF ECR, ESI contribution file, PT per State, LWF, TDS deposit data; liability ageing alerts before due dates; challans reconciled to the run |
| 13. Accounting journal | `accounts_maker` → `accounts_checker` | Payroll journal export (§Z.9.10) |
| 14. Lock | System | Run locked; corrections only by reversal/arrears in a later run (`PAY_RUN_LOCKED`) |

Run states: `draft → inputs_open → inputs_frozen → calculated → under_review → maker_submitted → hr_approved → finance_approved → released → bank_confirmed → closed` (any state before `released` → `cancelled` with reason; after `released` only reversal). An approver who rejects at `hr_approved` or `finance_approved` returns the run to `under_review` with a reason; recalculation creates a new calculation version and voids earlier approvals (payload digest, §Z.12.3) *(v3.1)*.

**Run checklist and variance thresholds (`PayRunWorkflow`; thresholds T tier `tenant.pay.variance.*`, loosening needs `internal_auditor` acknowledgement).** The cockpit (SCR-P18-29) shows a dated checklist computed from the configured calendar (F = input-freeze day, default 25th; P = pay day, default last working day; offsets in working days, T tier): F-3 attendance-close reminder to managers listing unapproved regularisations and leave; F-1 cut-off for joiners, exits and compensation changes; F inputs freeze; F+1 calculation; P-3 variance review complete; P-2 HR and Finance approvals complete; P-1 bank file released; P pay date (never later than the statutory deadline). Each item shows owner, due date and status; an overdue item alerts its owner and, from P-2, the `finance_controller`. Variance rules:

| Rule | Default threshold | Default action |
|---|---|---|
| Run headcount vs previous run | any change not explained by joiners/exits in `hr` | Block until reconciled |
| Run gross / net / employer cost vs previous run | ± 5% | Reason required |
| Employee net pay vs own previous month | ± 10% (`tenant.pay.variance_threshold_pct`) | Reason required |
| Employee net pay vs own previous month (excluding first and last months of employment, approved LWP, and arrears or bonus lines already second-checked) | ± 50% | Line auto-hold (below) |
| Negative or zero net pay for an active employee | any | Block line; recovery rescheduled within the 50% cap |
| Arrears or one-time earning | > 1 month's gross | Second checker (`finance_controller`) |
| Overtime in the month | > 25% of monthly wages | Reason required; feeds AN-11 |
| First payment to a new bank account (after cooling) | any | Highlighted; AN-09 |
| Ghost/anomaly hit on the employee | Critical | Line auto-hold |

**Line auto-hold (no silent withholding of wages).** A held line (latest `pay.run_line_holds.hold_status` ∈ `held`, `released`, `paid_offcycle`, `cancelled_ghost`; append-only, §Z.16) is excluded from the bank file while the rest of the run proceeds; the hold carries a reason code and an owner (`internal_auditor` for Critical, `hr_manager` otherwise). Because wages of a genuine employee must still be paid before the statutory deadline (CoW s.17), every hold has a deadline at D-1 of that deadline: by then it must be released (paid in a same-week off-cycle run through `PAY-OFFCYCLE`) or confirmed as not payable (`cancelled_ghost`, only on a resolved GH-01/GH-02/GH-06 finding with a second reviewer). An unresolved hold at D-1 escalates to the `finance_controller` and the Company Secretary, and a hold that would pass the deadline returns `PAY_HOLD_PAST_DEADLINE` (409) until one of them records the decision; the employee sees "Payment under verification — expected by {date}" (never the reason). KPIs: runs closed with zero unexplained variances = 100%; holds resolved before D-1 ≥ 95%; payments after the statutory deadline = 0. *(v3.1)*

### Z.9.5 Statutory components (versioned rule packs)
| Component | Rule summary (parameters in §Z.2.4) |
|---|---|
| EPF / EPS / EDLI | Employee 12% of statutory wages up to ceiling (₹25,000 from 17 Sep 2026; September 2026 split by calendar day pending EPFO guidance); employer 12% split EPS 8.33% (capped at ceiling) + EPF 3.67%; EDLI 0.50%; admin 0.50%; voluntary higher-wage contribution (employer and/or employee) per election; VPF; International Worker rule; EPS membership rule for members previously outside EPS; applicability at 20 employees or voluntary |
| ESI | Employee 0.75% / employer 3.25% where wages ≤ ₹21,000; contribution and benefit periods and mid-period continuity `[K, not re-fetched]` — configurable; applicability at 10 |
| Professional tax | Per State pack, monthly/half-yearly; February ₹300 rule where applicable; ₹2,500 annual Locked cap; State of levy per D3-31 |
| LWF | Per State pack, frequency and due dates; employer share computed |
| TDS on salary (s.392) | §Z.9.7 |
| Gratuity provision | Liability = 15/26 × last drawn monthly statutory wages × completed years of service (part-year above 6 months counted as a year), capped at the ceiling; the monthly provision is the change in that liability (actuarial valuation optional, imported); payout 15 days' wages per completed year (or part > 6 months), 5 years' service (not required on death/disablement/expiry of fixed term; fixed-term after 1 year), ceiling ₹20 lakh, paid within 30 days; new wage definition for exits on or after 21 Nov 2025 |
| Bonus | Applicability at 20; 8.33%–20% of wages or ₹100 minimum, ≥ 30 days' work; **bonus runs are blocked while eligibility/calculation ceilings are `NOT_CONFIRMED`** unless the Payroll Compliance Officer records a dated professional opinion; set-on/set-off per Central Rules rr.21–28 |
| Overtime | 2× on daily/weekly basis whichever more favourable; workers only; consent evidence ID required per OT line |
| Deductions guard | Total deductions per wage period ≤ 50% of wages; excess auto-deferred with an employee-visible schedule (r.13); fines and damage/loss deductions require attached evidence objects (notice, reply-window expiry; fines 7-day show-cause, imposition within 15 days) — `PAY_DEDUCTION_CAP_EXCEEDED`, `PAY_FINE_EVIDENCE_MISSING` |
| Statutory-dues non-waiver | No settlement, F&F or manual adjustment may waive EPF, ESI, gratuity, bonus, maternity benefit or minimum wages (`STATUTORY_WAIVER_FORBIDDEN`, existing Appendix F code) |

### Z.9.6 Arrears, loans, advances and reimbursements
- **Arrears:** past periods re-run with the parameter versions then in force; the difference is paid in the current run and tax re-estimated.
- **Loans and advances**: request → DoFP `PAY-LOAN` approval → schedule (EMI, tenor, interest if any; perquisite valuation of concessional loans per Form 123 rules `[NC]`) → recovery within the 50% deduction cap; outstanding balance recovered at F&F within cap, remainder as a recorded receivable (never withheld from statutory dues).
- **Reimbursements** are raised as `ctl.expense_claims` (§Z.12.8) with receipts and approvals; claims marked `route = payroll` flow into the next run with their tax treatment (taxable/exempt by component class), others go to accounts payable.

### Z.9.7 TDS on salary — Income-tax Act 2025
| Feature | Specification |
|---|---|
| Regime | Default regime (s.202) unless the employee opts for the old regime for withholding; election per employee per tax year, locked after the declaration window closes except once on documented change (`PAY_REGIME_LOCKED`); UI states that the final choice is made at return filing (s.202(4)) |
| Declarations | Form 124 (s.392(5)(b); r.205): HRA, LTC, interest on borrowing, Chapter VIII-A/VIII-B claims — declaration window at start of year and on joining; proof window (default January–February, T); unproved claims reversed in remaining months (`PAY_PROOF_WINDOW_CLOSED`) |
| Previous employer | Form 127 data intake for mid-year joiners |
| Monthly computation | Estimated annual taxable income at the average rate; standard deduction (₹75,000 default / ₹50,000 old); employer NPS; rebate s.156 (₹60,000 up to ₹12 lakh with marginal relief; old ₹12,500 up to ₹5 lakh); cess 4%; surcharge per pack; re-estimated each month — method carried from s.192 `[VERIFY — open: s.392 wording]` |
| Outputs | **Form 130** annual certificate (by 15 June); **Form 123** perquisite statement where salary > ₹1,50,000 (signed by the Form 130 signatory; issue date `[NC]`); **Form 138** quarterly statement data (due dates `[NC]`); deposit challan data |
| Copy | "Computed under the Income-tax Act 2025 and Income-tax Rules 2026 as configured (parameter version …). This is not tax advice." No regime recommendation is shown; a neutral side-by-side computation is available on request |

### Z.9.8 Full and final settlement
`FnfWorkflow` starts on `exit_initiated`, provisional computation at T-5 working days before last day, final at `exit_effective`, payment within 2 working days (`wrk_wages_2wd`). Lines: salary to date, leave encashment (OSH s.32(1)(vi) timing), notice pay or recovery, pro-rata bonus where applicable, reimbursements, arrears, loan recovery within cap, asset loss recovery with prior intimation, TDS, gratuity (separate 30-day clock, shown on the statement). Approval DoFP `PAY-FNF` (HR checker + Finance). The F&F statement is e-signed or acknowledged by the employee; disputes route to HR grievance (`WRK_HR` desk) and never block payment of undisputed amounts.

### Z.9.9 Registers and statutory outputs
Generated electronically from run data: Form I (employee register), Form IV (wages, overtime, advances, fines and deductions), Form IX (attendance-cum-muster roll), Form V wage slip, Form VII nomination (CoW Central Rules rr.45, 51, 52) [RC F2.9]; OSH s.33 registers; EPF ECR; ESI return; PT returns per State (form numbers configurable); LWF returns; Forms 130/123/138 data; Form 124/127 intake. Undisbursed dues are tracked for deposit after 3/6 months and unclaimed amounts held 7 years (rr.45–47). All outputs export in the NN-37 package convention (XLSX registers + PDF summaries + CSV/JSON + manifest).

### Z.9.10 Payroll accounting and specialist-tool exchange
- **Journal export:** after `bank_confirmed`, a balanced payroll journal (salary expense by cost centre, employer contributions, statutory liabilities by type, net pay payable, bank clearing, loan/advance recoveries, inter-company recharges for secondees) is posted to `core.ledger_journals` (P05 FR-P05-52 pattern, chart-of-accounts mapping per legal entity) and exported to Tally (XML/CSV) or Zoho Books (CSV/API) through the P05 FR-P05-55 GL-export mechanism (adapters `tally_file` and `zoho_books` of `ACCOUNTING_PORT`, Appendix AC); locked periods cannot be re-exported without `fin.controller` reopen with reason (`PAY_GL_PERIOD_LOCKED`).
- **`PAYROLL_EXCHANGE_PORT`** (new port, NN-40): `exportInputs()`, `importResults()`, `exportMaster()`, `importMaster()` with adapter `generic_csv` (documented field mapping) so that a specialist payroll provider can run payroll in parallel or replace the engine; imported results are validated against the deterministic library before they can be posted (difference report).

### Z.9.11 Edit log (Companies (Accounts) Rules 2014 r.3(1) proviso — Locked)
Payroll ledgers and master data (`pay.employee_compensation`, `pay.bank_accounts`, `pay.components`, `pay.structure_templates`, run lines) are append-only or temporally versioned with `*_history` tables (`old`, `new`, `changed_by`, `changed_at` IST, `reason`, `change_request_id`); `pgaudit` covers DDL/DML on `pay` and `ctl`; any `ALTER TABLE … DISABLE TRIGGER` or role change on them raises a Critical alert so the trail cannot be disabled [RD F7.3, DI-F 34]. Books remain accessible in India with daily backup in India (r.3(1), r.3(5)); retention 8 years (s.128(5) — `[NC]` in [RD]; pack default). Statutory auditors report under Companies (Audit and Auditors) Rules r.11(g); the internal-audit workspace exposes the trail read-only (§Z.12.14).

### Z.9.12 Disclaimers (Locked text keys)
`pay.disclaimer.computation`: "Payroll and tax figures are computed by configured rules and parameters (shown with source and date). They must be reviewed by a qualified payroll or tax professional before payment or filing. This is not legal or tax advice." Shown on the run review, F&F, tax computation, structure preview and every exported statutory file cover sheet. Each parameter shown carries its `verification_status` badge.

### Z.9.13 Worked examples (golden tests; seed parameter values of §Z.2.4–Z.2.5; recomputed 24 Oct 2026) *(v3.1)*
Each row is a CI golden test `PAY_golden_<id>` in `packages/rules/payroll`; amounts are before rounding unless stated. The EPFO and ESIC rounding rules under the 2026 Schemes are not in [RC] and are a parameter (`coss.epf.rounding`, `coss.esi.rounding`; seed "nearest rupee per component", SECONDARY_ONLY) `[VERIFY — open: EPFO/ESIC rounding rules under the 2026 Schemes]`.

| ID | Inputs | Computation | Result |
|---|---|---|---|
| W01 wage definition | Total ₹76,000; basic + DA ₹20,000; (a)–(i) items ₹40,000 | 50% × 76,000 = 38,000; excess 40,000 − 38,000 = 2,000 | Statutory wages ₹22,000 (MoLE FAQ Q7) |
| W02 EPF full month (Oct 2026) | Statutory wages ₹30,000 | EPF wage = min(30,000, 25,000) = 25,000; employee 12% = 3,000; EPS 8.33% = 2,082.50; employer EPF = 3,000 − EPS; EDLI 0.50% = 125; admin 0.50% = 125 | Employee ₹3,000; EPS ₹2,082.50 (₹2,083 if rounded) and employer EPF ₹917.50 (₹917); employer total incl. EDLI and admin ₹3,250 |
| W03 EPF split month (Sep 2026) | Statutory wages ₹30,000 | Base = 15,000 × 16/30 + 25,000 × 14/30 = 8,000 + 11,666.67 = 19,666.67; employee 12% = 2,360.00; EPS 8.33% = 1,638.23; employer EPF = 2,360.00 − 1,638.23 = 721.77; EDLI and admin 0.50% each = 98.33 | As computed (SECONDARY_ONLY acknowledgement required) |
| W04 ESI | Statutory wages ₹20,000 (≤ ₹21,000) | Employee 0.75%; employer 3.25% | ₹150 and ₹650 |
| W05 overtime | Worker, monthly wages ₹26,000, 3 h approved with consent | Hourly = 26,000 ÷ 26 ÷ 8 = 125; OT rate 2 × 125 = 250 | ₹750 |
| W06 deduction cap | Wages ₹30,000; approved deductions ₹18,000 | Cap 50% = 15,000 | ₹15,000 applied; ₹3,000 deferred to next period (r.13) |
| W07 gratuity | Statutory wages ₹40,000; service 6 years 7 months (part > 6 months counts) | 15 × 40,000 × 7 ÷ 26 | ₹1,61,538.46 (below the ₹20 lakh ceiling) |
| W08 gratuity not payable | Resignation after 4 years 5 months, permanent employee | Below 5 years; not death, disablement or fixed-term expiry | Nil; provision reversed |
| W09 TDS default regime | Annual salary ₹15,00,000; no other income | Taxable = 15,00,000 − 75,000 = 14,25,000; tax = 0 + 20,000 + 40,000 + 15% × 2,25,000 (33,750) = 93,750; rebate nil (> ₹12 lakh); marginal relief nil (93,750 < excess 2,25,000); cess 4% = 3,750 | ₹97,500 a year; ₹8,125 a month if spread evenly |
| W10 rebate | Annual salary ₹12,75,000 | Taxable 12,00,000; tax 60,000; rebate min(60,000, 60,000) | Nil tax; nil TDS |
| W11 marginal relief | Annual salary ₹12,85,000 | Taxable 12,10,000; tax 20,000 + 40,000 + 1,500 = 61,500; capped at income above ₹12 lakh = 10,000; cess 4% = 400 | ₹10,400 a year |
| W12 professional tax | Gross ₹30,000 a month, male, all year | MH: ₹200 × 11 + ₹300 (February); KA: same pattern; DL/UP/RJ: none | MH ₹2,500; KA ₹2,500; DL nil (Art. 276(2) cap respected) |
| W13 absence deduction (LWP) | Monthly wages ₹31,000; 2 LWP days in a 31-day month | Default divisor = calendar days of the wage period (`tenant.pay.lop_divisor`, other divisors G tier and never deducting more than the absence proportion of the wage period) | ₹2,000 |
| W14 F&F due date | Last working day Friday 13 Nov 2026; Saturday and Sunday weekly offs; no holiday on 16–17 Nov in the establishment calendar | 2 working days (CoW s.17(2)) | Due by Tuesday 17 Nov 2026 |

---

## Z.10 Performance appraisal

### Z.10.1 Goals and OKRs
Department objectives (set by `department_head`, approved by `ops_director`) cascade to team and individual goals; each goal has a key result metric (optionally linked to a scorecard KPI), weight, target, evidence links and a due date. Goals are agreed (employee + manager acknowledgement) within 30 days of cycle start or joining. Outcome-linked goals for case staff are blocked by the same rule as §Z.7.2.

### Z.10.2 Feedback, check-ins and cycles
Monthly check-ins (T tier) with shared notes; optional peer feedback (anonymous mode aggregates at n ≥ 3); recognition. AI never infers ratings from feedback text. Cycles: probation review at T-30 (§Z.4.7); mid-year (September: self and manager check-in, goal reset); annual (March–April: self-review → manager review → optional 360 → calibration → release → acknowledgement → appeal window → increment/bonus proposal).

### Z.10.3 Ratings, calibration and 360
- Rating scale configurable (default 5-point: Outstanding, Exceeds, Meets, Partially meets, Does not meet) with behavioural anchors; distribution **guidance** may be shown; forced ranking/forced distribution is OFF (`hr.appraisal.forced_distribution.enabled`, G tier with DPIA).
- **Calibration committee** per department (department head, HR business partner, one peer head); calibration changes require a written reason; the committee sees KPIs, goal evidence, review text and data-coverage notes, and a fairness panel (rating distribution by gender and by work mode — remote vs office — at n ≥ 5, to detect bias; protected data used only in aggregate for this check under a documented purpose).
- **360** optional per cycle; minimum 3 raters; raters chosen jointly; comments shown verbatim only after PII/abuse filter; never sole basis for rating.
- **Calibration views (SCR-P18-34; read-only to the committee until the session opens; locked at release).** (1) *Distribution* — proposed ratings against the published guidance band per department and grade (guidance only; forced distribution stays OFF). (2) *Manager lens* — each manager's mean proposed rating against the department mean, with a "lenient/strict" flag where the gap exceeds 0.5 points on the 5-point scale for teams of n ≥ 5. (3) *Evidence completeness* — per review: goals with evidence, check-ins held, scorecard coverage, open disputes, employee replies (§Z.7.4); a review with completeness below 60% (T) is flagged "insufficient evidence" and cannot move more than one rating step in calibration. (4) *Fairness panel* — distribution by gender, by work mode, by establishment State and by whether the employee took maternity, long sick or disability-related leave in the cycle, each at n ≥ 5 and aggregate only. (5) *Side-by-side* — up to 6 peers in the same role and grade. (6) *Change log* — mover, reason (≥ 30 characters), before/after. Guards: a rating may not be lowered because of approved leave (the engine blocks a reason code that cites absence when the absence is approved leave, `HR_RATING_REASON_PROHIBITED`, 422); a committee member does not rate or move their own direct reports' ratings without a second member's concurrence. KPIs: share of reviews with completeness ≥ 60%; manager-lens gaps after calibration. *(v3.1)*

### Z.10.4 PIP with fairness safeguards
A Performance Improvement Plan (`hr.pips`) can start only after: (a) documented expectations communicated earlier in the cycle; (b) at least one recorded check-in discussing the gap; (c) HR review confirming the data is complete, disputes resolved and adjustments for leave, illness, disability accommodation and workload considered; (d) protected-status check (§Z.12.11). The PIP states specific measurable goals, support and resources, review dates (at least fortnightly), and a minimum duration (default 60 days, T tier ≥ 30). Outcomes: `successful`, `extended` (once), `unsuccessful` → disciplinary/termination workflow under the applicable law and policy (MSO inquiry norms for workers). Missing safeguards block creation (`HR_PIP_SAFEGUARD_MISSING`, 422). The employee may attach a response at every review.

### Z.10.5 Link to increments and bonuses (budget + maker-checker)
The increment cycle opens a merit matrix (rating × position-in-band → % range) within an approved budget (DoFP `HR-INCREMENT-BUDGET`, Board where above threshold). Managers propose; HR checks band and budget; department head approves within limits; `finance_controller` approves the total; CEO designation above budget. Approved changes become compensation versions effective on the cycle date, with letters generated and e-signed. Variable pay/bonus pools follow the same pattern; payouts flow to payroll as `NOT_WAGES` components with approvals.

### Z.10.6 Acknowledgement and appeal
The employee acknowledges the final review (acknowledgement ≠ agreement); appeal within 15 days (T) to a reviewer outside the reporting line (skip-level or HR head); decision with reasons within 21 days; one further appeal to an appeals panel for ratings tied to adverse action. Appeals and outcomes are recorded and reported in aggregate.

---

## Z.11 Learning, certifications, assets and documents vault

### Z.11.1 Learning and certifications
- The internal catalogue reuses the `academy` LMS (P10) in an **internal** tenant space: mandatory modules (staff code ESC-2026.1, DPDP and information security, POSH awareness, anti-bribery and gifts, conflict of interest) with completion deadlines and annual refresh; role curricula (case managers: ADR process, Equator Rules ERR-2026.1, notices and clocks, safeguarding; support: grievance handling).
- **External ADR training for case managers** may be bought from providers including **equatoradr.com**. That site is operated as "Equa Trainings, a brand owned by Infrabyx Consultancy (OPC) Private Limited" [RB §1.1]; purchases by Equator from it are **related-party transactions** to be recorded in the `grp` shared-services register with the Companies Act s.188 approval reference where applicable ([RE] F5.2; CS to confirm), and the training picker lists at least three providers (X-29 principle). Certificates are recorded as issued; the HRMS never describes a course as accredited or as a QAP unless the evidence record in the Claims Register supports it (NN-17; App. N corrections C1–C18).
- `hr.certifications` (issuer, number, expiry, evidence, verification status) with T-60/T-30 reminders; a role may require a current certificate (`HR_CERTIFICATION_REQUIRED`).

### Z.11.2 Assets
`hr.assets` (type, tag, serial, purchase ref, cost centre, MDM enrolment ID, encryption status) and `hr.asset_assignments` (assigned/returned dates, condition, acknowledgement). Laptops for sealed/Tier-High roles must be MDM-enrolled with full-disk encryption (Q SC-15; SKU caveat §Z.5.1). Lost or stolen device → immediate workspace session revoke and MDM wipe where available; security incident ticket.

### Z.11.3 Documents vault (restricted)
Employee files (appointment letter, contracts, BGV, nominations, letters, appraisals, disciplinary records, exit documents) are DMS objects with `confidentiality_tier = high`, field-level encryption for identifiers, per-category access (HR only; manager sees letters addressed to their team member only where the employee consents or policy requires), watermarking on download, no bulk download without `ctl` approval, retention classes per §Z.18.3. **POSH and whistle-blower material is never stored in the vault** (NN-07; P09 FR-P09-34); the vault may carry only an opaque hold flag.

---

## Z.12 Internal controls (`ctl`, NN-36)

### Z.12.1 Control objectives
NN-36 as stated in master §3, plus: decisions decentralised to the lowest competent level within delegated limits; exceptions always logged, approved one level up, time-limited and reported; fraud indicators detected continuously, not only at audit; internal audit with independent, read-only, evidence-grade access.

### Z.12.2 Authority matrix and default DoFP
`ctl.authority_rules` rows: `action_code` × `legal_entity_id` × `scope` (department/cost centre/any) × `amount band` (₹ minor, inclusive lower, exclusive upper) × `approval_chain` (ordered steps; each step = role, designation or named user; `min_approvers`; `distinct_from` constraints) × `conditions` (e.g., `within_budget`, `vendor_age_days ≥ 30`) × `effective_from/to` × `source` (Board resolution reference). Changes to the matrix are configuration (G tier, Board resolution reference mandatory for financial limits; X-56).

**Default values — proposals subject to Board approval (D3-34). Amounts in ₹, exclusive of GST unless stated.**
| Action code | Up to | Approver chain (after maker) |
|---|---|---|
| `EXP-CLAIM` (employee expense claim) | 10,000 | Line manager |
| | 50,000 | Line manager → `department_head` |
| | 2,00,000 | → `finance_controller` |
| | above | → CEO designation |
| `PROC-PO` (purchase order) | 1,00,000 | `department_head` (within budget) |
| | 5,00,000 | → `finance_controller` |
| | 25,00,000 | → CEO designation |
| | above | → Board |
| `VENDOR-ONBOARD` | any | `finance_ops` (KYC) → `finance_controller` |
| `PAY-VENDOR` (payment release) | 2,00,000 | `accounts_checker` |
| | above | → `finance_controller` (`fin.approver`, P05) |
| `REFUND` (billing) | 25,000 | `fin.operator` (P05); above → `fin.approver` |
| `WRITE-OFF` | 25,000 | `finance_controller` |
| | above | → CEO designation; above ₹5,00,000 → Board |
| `PAY-RUN-APPROVE` | any | `payroll_checker` → `finance_controller` |
| `PAY-OFFCYCLE` | 50,000 per employee | `payroll_checker` → `finance_controller`; above → CEO designation |
| `PAY-FNF` | any | `payroll_checker` → `finance_controller` |
| `PAY-LOAN` | 1 month's gross | `hr_manager` → `finance_controller`; above → CEO designation |
| `HR-REQ-IN-BUDGET` | within plan | `department_head` → `hr_manager` |
| `HR-REQ-OUT-BUDGET` | any | `ops_director` → `finance_controller` |
| `HR-OFFER-ABOVE-BAND` | any | `hr_manager` → CEO designation → `finance_controller` |
| `HR-COMP-REVISION` | within band and budget | `department_head` → `hr_manager` |
| | outside band | → CEO designation |
| `HR-TERMINATION` | any | `department_head` → `hr_manager` → CEO designation (legal reviewer for workers) |
| `PAYEE-BANK-CHANGE` | any | Out-of-band confirmation by the payee + checker (§Z.12.5) |
| `ROLE-GRANT-PRIVILEGED` | any | Role owner → `it_admin` (execute) with SoD check; security lead for console roles |
| `EXPORT-SENSITIVE` | any | `dpo` (privacy) + data owner |
| `PETTY-CASH-REPLENISH` | float size | `accounts_checker` |
| `ALLOCATION-OVERRIDE` | any | Per App. N (registrar + committee) — `ctl` only records and enforces maker ≠ checker |
| `REV-STREAM-NEW` (maker `revenue_manager`; Appendix AB §AB.6.5) | N0, families `saas_subscription`, `usage`, `one_time_product`, `professional_service` | `finance_controller` (CFO designation); Board informed at next meeting |
| | N1, or families `case_fee`, `programme`, `membership`, `event` with sponsors | `finance_controller` (CFO designation) + `legal_reviewer` → Board |
| | Any N2 stream, or lowering a rating | `compliance_officer` + `legal_reviewer` + counsel opinion → Board (resolution reference) |
| | Related-party stream (RS-22, RS-55, intercompany cross-charges) | `compliance_officer` (CS designation) + `finance_controller` (CFO designation) → Board under s.188 **[CS to confirm]** |
| `REV-PRICE-CHANGE` | ≤ 5% within bounds (B2B SaaS, usage, services) | `fin.approver` (P05) |
| | > 5% and ≤ 10% within bounds | `finance_controller` (CFO designation); Board informed |
| | > 10%; any consumer-facing case fee or vertical card; any bounds change | `finance_controller` (CFO designation) → Board (B §B.12) |
| `REV-COUPON` (maker `marketing_manager` or `bd_manager`) | 25% | `fin.approver`; above → `finance_controller` (CFO designation) |
| `REV-ENTERPRISE-DISCOUNT` (maker `sales_executive`) | 10% beyond card | `bd_manager`; ≤ 25% → `finance_controller` (CFO designation); above 25% or below floor → Board |
| `REV-KILL-RELEASE` | any | `finance_controller` (CFO designation) + `compliance_officer`; Board where the kill reason was `neutrality_incident`, `legal` or `regulator` |
| `REV-STREAM-RETIRE` | any | `finance_controller` (CFO designation); Board where the stream carried a Board resolution |
| `REV-PRICE-TEST` | policy / individual test | Board (policy) / `finance_controller` (CFO designation, test) |

`REV-*` rows implement Appendix AB §AB.6.5 (thresholds held as `platform.rev.authority.*`, AB §AB.8); the AB labels `cfo` and `company_secretary` are designations on `finance_controller` and `compliance_officer` (§Z.2.3), not separate roles. Kill-switch engage (AB KS-1) needs no approval and is only recorded.

**Decentralisation.** A `department_head` approves within limits without escalation; an approver may delegate (`ctl.delegations`) to a named person for ≤ 30 days (leave cover), never above the delegator's own limit, never to someone in the maker's chain, depth 1 (App. S §6.4 pattern). An approval request is routed to the lowest eligible approver; if no action within the SLA (default 2 working days), it escalates one level and the delay is recorded.

**Delegation of authority during leave (`LeaveDelegationJob`; T tier `tenant.ctl.delegation.on_leave.*`).** (1) When a person who holds any approval authority, or any open approval step, applies for leave of ≥ 2 working days (T), the leave form requires a cover delegate from an eligible list (same or higher level, not in the delegator's own maker chain for open items, no SoD conflict, not on leave on those dates) or the explicit choice "route to my approver". (2) On approval of the leave, a `ctl.delegations` row is created automatically (`reason = leave`, `leave_request_id`, start and end = leave dates, limit = the delegator's limit or a lower one chosen by the delegator; depth 1); leave longer than the 30-day delegation cap (e.g., maternity) is covered by consecutive ≤ 30-day delegations, each confirmed by the delegator's approver, or by an authority-matrix change for the period. (3) The delegation activates at 00:00 IST on the first leave day, moves pending steps to the delegate with an "on behalf of {delegator}" label, and ends automatically when the leave ends or is cancelled; items still open return to the delegator with the delegate's notes. (4) Unplanned absence: when a sick-leave day or an unauthorised absence is recorded for an approver, open steps older than 1 working day route to the delegator's own approver. (5) A delegate can never approve an item they made or an item about themselves; delegated authority never exceeds the delegator's limit, and where it exceeds the delegate's own limit the delegator's approver must approve the delegation before it activates; payroll-checker and finance-release steps can be delegated only to holders of the same role (SoD). (6) Every decision records both identities; the delegator receives a digest on return. KPI: approval items breaching SLA because the approver was on leave = 0. *(v3.1)*

### Z.12.3 Maker-checker engine (`ctl.approval_requests`)
- Generic request: `action_code`, `subject_type`, `subject_id`, `amount_minor`, `currency`, `legal_entity_id`, `payload_digest` (SHA-256 of the exact object to be approved), `maker_user_id`, `created_at`, `expires_at` (default 14 days), `status` (`pending`, `approved`, `rejected`, `expired`, `withdrawn`, `executed`).
- Steps: `ctl.approval_steps` (`step_no`, `approver_user_id`, `decision`, `decided_at`, `acr`, `comment`, `ip_zone`).
- **Rules (Locked):** approver ≠ maker (DB CHECK; `CTL_SELF_APPROVAL_BLOCKED`); approvers within one request are distinct; an approver cannot approve a request about themselves, a declared relative (COI register) or a direct report's self-related compensation where the approver is also the maker's maker; the payload digest is re-verified at execution — any change after approval voids the approval (`CTL_PAYLOAD_CHANGED`); approvals require step-up (`aal2-pr` ≤ 10 min) for money and privileged actions; approval from outside office/ZTNA network zones is denied for `finance_controller` actions (App. S §2.6).
- **API for modules:** `CtlService.request(action, subject, amount, context)` → `requestId`; `CtlService.assertApproved(requestId, payloadDigest)` before execution; events `equator.ctl.approval.requested|approved|rejected|executed.v1`. Every module (pay, billing, procurement, HR, role grants, exports) uses this API; direct execution of a controlled action without an approved request is a Critical detection.

### Z.12.4 Separation-of-duties conflict matrix (checked at role grant and at policy time)
| Rule | Conflicting duties (same user, same legal entity) | Enforcement |
|---|---|---|
| SOD-01 | Create/edit employee master (`hr_executive`) × approve pay run (`payroll_checker`) | Grant blocked |
| SOD-02 | Prepare pay run (`payroll_maker`) × approve the same run (`payroll_checker`) | Grant blocked |
| SOD-03 | Approve pay run × release bank file (`finance_ops`) | Grant blocked |
| SOD-04 | Release payments (`finance_ops`) × bank reconciliation (`accounts_checker`) | Grant blocked |
| SOD-05 | Create/approve vendor (`VENDOR-ONBOARD`) × approve vendor payment | Grant blocked |
| SOD-06 | Approve payee/bank change × release payment to that payee | Per-transaction block |
| SOD-07 | `accounts_maker` × `accounts_checker` on the same journal | Per-transaction block |
| SOD-08 | `it_admin` × approver of own access grants | Per-transaction block |
| SOD-09 | `internal_auditor` × any operational maker/checker role in the audited entity | Grant blocked |
| SOD-10 | Rule-pack maker (`compliance_officer`) × checker of the same version | Per-transaction block |
| SOD-11 | Petty-cash custodian × petty-cash reconciler | Grant blocked |
| SOD-12 | `escrow_officer` ∉ {`case_manager`, `quality_officer`, `finance_controller`} (App. S §6.7, retained) | Grant blocked |
| SOD-13 | `group_hr` cross-entity grant × `payroll_checker` in the target entity | Grant blocked |
| SOD-14 | Requester of a role × approver of that role grant | Per-transaction block |
| SOD-15 | Approver of a payment (e.g., `accounts_checker` on `PAY-VENDOR` ≤ ₹2,00,000) × bank reconciliation of that payment (NN-36: approve and reconcile split) | Per-transaction block; reconciliation routed to another `accounts_checker` or `finance_controller` *(v3.1)* |

At grant time a trigger evaluates `ctl.sod_rules` against the user's active and pending roles across modules (`CTL_SOD_CONFLICT`, 409). A compensating-control exception (small team) needs CEO designation approval, a named compensating control (e.g., monthly independent review by `internal_auditor`), and expiry ≤ 90 days; it appears on the exceptions dashboard until closed.

### Z.12.5 Payee and bank-detail change controls
Applies to employees (`pay.bank_accounts`), vendors and any other payee in `ctl.payees` [RC E.26]:
1. Change only via the payee's own authenticated session with MFA, or HR/finance-initiated with the payee's in-app confirmation.
2. **Penny-drop / name-match** verification against the account-holder name (App. S §3.11 via `KYC_PORT`); mismatch → `CTL_PENNY_DROP_MISMATCH` (422) unless a checker approves with evidence.
3. **Cooling-off:** new account not used for payment for 3 working days (`tenant.ctl.bank_change.cooling_working_days`, T tier within 1–7; floor 1 Locked).
4. **Out-of-band confirmation:** notification to the registered e-mail and phone and to the previous account's last-used channel, with a one-click "This wasn't me" reversal link that freezes the change and opens a security incident.
5. Changes requested within 5 days of a pay run (T) are deferred to the next run unless `finance_controller` approves.
6. Duplicate check: the account number hash (`account_hmac`) must not match any other active employee, vendor or related party (`CTL_DUPLICATE_BANK_ACCOUNT`, 409).
7. A payment to an account inside its cooling window is blocked (`CTL_COOLING_OFF_ACTIVE`, 409).

### Z.12.6 Ghost-employee and duplicate detection (`GhostEmployeeScanJob` weekly + every pay run) [RC E.27]
| Rule | Signal | Severity |
|---|---|---|
| GH-01 | Paid in the period with no attendance, login or work item and no approved leave | Critical |
| GH-02 | Duplicate PAN, Aadhaar reference, UAN, ESI IP number, bank account, phone or e-mail across employees | Critical |
| GH-03 | Bank account shared with a vendor, another employee or a related party | Critical |
| GH-04 | No signed appointment letter (OSH s.6(1)(f)) or no onboarding evidence | High |
| GH-05 | Manager is also the approver for every change to the employee | High |
| GH-06 | Salary paid after the separation date | Critical |
| GH-07 | New hire created and paid in the same run | High |
| GH-08 | One PAN with two active employments within the group without a secondment record (`HR_DUPLICATE_ACTIVE_EMPLOYMENT`) | Critical |
| GH-09 | Employee with no workspace account and no platform login for 30+ days while paid | High |
| GH-10 | Address or phone of an employee matches a vendor's | Medium |

Each hit opens a `ctl.alerts` row and an investigation task assigned to `internal_auditor` (or `hr_manager` for High/Medium); a run cannot be finalised with unresolved Critical hits; dismissal of a hit requires a reason and a second reviewer.

### Z.12.7 Anomaly alerts (`AnomalyDetectionJob`, near-real-time on `ctl` events; rules as data)
| Rule | Detection | Default parameters (T tier) |
|---|---|---|
| AN-01 After-hours approval | Approval of money/privileged action outside 08:00–20:00 IST, on a weekly off or holiday | Window configurable; alert, not block |
| AN-02 Split transactions | ≥ 2 requests by the same maker or to the same payee within 7 days, each within 10% below an approval limit and together above it | 7 days / 10% |
| AN-03 Self-approval attempt | Any attempt blocked by `CTL_SELF_APPROVAL_BLOCKED` | Alert on every attempt; 3 in 30 days → HR and internal audit |
| AN-04 Round-tripping | Payment to a vendor whose bank/address/phone matches an employee or related party; refund to an account different from the source; circular flows employee ↔ vendor within 90 days | — |
| AN-05 Rubber-stamping | Approver approves > 20 items in < 60 s, or median review time < 5 s for money items | 20 / 60 s |
| AN-06 New vendor fast payment | Payment above ₹1,00,000 within 7 days of vendor creation | ₹1,00,000 / 7 days |
| AN-07 Dormant vendor reactivated | Vendor unused 12 months receives payment | 12 months |
| AN-08 Duplicate invoice | Same vendor + invoice number, or same amount + date ± 3 days | — |
| AN-09 Bank change then payment | Payment within 10 days after a bank change (even after cooling) | 10 days |
| AN-10 Expense patterns | Claims just under receipt-required threshold; claims dated on leave days or holidays; duplicate receipts (image hash) | — |
| AN-11 Overtime concentration | Manager approves OT for own team above 20% of team hours in a month | 20% |
| AN-12 Access anomalies | Mass export of HR/payroll data by one actor; sealed-store access outside business hours (Q SC-10) | Q SC-10 thresholds |
| AN-13 Off-cycle compensation change *(v3.1)* | Compensation version effective in a month with no increment cycle, promotion or approved `HR-COMP-REVISION` reference | — |
| AN-14 Bank change near exit *(v3.1)* | Bank-account change within 30 days before or after resignation or exit initiation | 30 days |
| AN-15 Shared device or network for bank changes *(v3.1)* | Bank changes for ≥ 2 different payees from the same device fingerprint or IP within 30 days | 2 / 30 days |
| AN-16 Overtime or claim on a leave day *(v3.1)* | Overtime approved, or an expense dated, on a day the employee was on approved leave or holiday | — |
| AN-17 Vendor GSTIN or PAN status change *(v3.1)* | Payment to a vendor whose GSTIN became cancelled/suspended or whose PAN became inoperative since onboarding (re-verified through `KYC_PORT` monthly) | Monthly |

Alerts go to the owning manager and the exceptions dashboard; Critical alerts also to `internal_auditor` and `compliance_officer`. AI does not decide alerts; rules are deterministic (NN-01).

**Rules library and tuning (`ctl.anomaly_rules`; v3.1).** Each rule is a versioned record: `rule_id`, `version`, `title`, `rationale` (the fraud scheme it targets), `severity`, `parameters` (bounded; bounds are Locked so that no tenant can set a rule that never fires), `mode` ∈ `shadow` (evaluated and logged, no alert), `alert`, `block` (only rules whose block is listed in §Z.12.4–Z.12.6), `scope` (entity, module), `owner`, `review_due`. Workflow: a new rule or a loosened parameter starts in `shadow` for at least 30 days (T, minimum 14) and is promoted to `alert` by maker `compliance_officer` and checker `internal_auditor` after the shadow report (would-be alerts per week and a sample of 10); tightening takes effect at once. Every alert disposition is recorded (`true_positive`, `false_positive`, `benign_explained`, `duplicate`); the weekly **tuning report** shows per rule the volume, precision (true positives ÷ dispositions) and median time to disposition, and flags rules with precision below 10% over 90 days or more than 50 alerts a week for review. Suppressions are per subject (e.g., a known shared office network for AN-15), carry a reason and an expiry ≤ 90 days, and are listed on the exceptions dashboard. Seed rules AN-01…AN-12 ship in `alert` mode and AN-13…AN-17 in `shadow` for the first 30 days after go-live; tenant-added rules may use only the library's deterministic operators (thresholds, windows, joins on hashed identifiers), never a model score (NN-01). *(v3.1)*

### Z.12.8 Expense, procurement, vendor onboarding and petty cash
- **Expense claims** (`ctl.expense_claims`): line items with category, date, amount, GST details, receipt image (required above ₹500, T), purpose, cost centre; per-diem and mileage tables (T); policy checks (category limits, duplicates via image hash, weekend/holiday flags); approval per `EXP-CLAIM`; settlement route payroll or accounts payable; reimbursement within the policy SLA.
- **Procurement:** purchase request → quotations (≥ 3 above ₹5,00,000, T) → PO (`PROC-PO`) → goods/service receipt by a person other than the requester → invoice match (3-way: PO, receipt, invoice; tolerance 2%, T) → payment (`PAY-VENDOR`). Contracts above ₹10,00,000 (T) require legal review. Related-party vendors (group companies, Infrabyx Consultancy (OPC) Pvt Ltd, entities of directors) are flagged and routed through the s.188 check in the `grp` shared-services register.
- **Vendor onboarding with KYC:** legal name, PAN (verified), GSTIN (verified via App. S §3.7), Udyam status where claimed, bank account (penny-drop), beneficial owner for companies where relevant, sanctions/PEP screening for foreign vendors (`SANCTIONS_PORT`), conflict-of-interest check against employee declarations, DPA where the vendor processes personal data (Q §2.7), TDS profile (s.393 categories — contractor TDS parameters `[NC]`). Incomplete KYC blocks POs (`CTL_VENDOR_KYC_INCOMPLETE`, 409).
- **Petty cash:** imprest float per office (default ₹10,000, T), custodian named, single spend cap (default ₹2,000, T), voucher with receipt, monthly count and reconciliation by a different person (SOD-11), replenishment only after reconciliation; remote staff use reimbursements instead of petty cash.

### Z.12.9 Periodic access reviews
Quarterly for all workforce access to `apps/ops`, `hr`, `pay`, `ctl` and finance modules; monthly for privileged roles (`payroll_*`, `finance_*`, `it_admin`, `group_hr`, `internal_auditor`) — reusing `eng.access_reviews` (moved from `ops` by X-65) and `AccessReviewCampaign` (P14 FR-P14-21; Q §7.3). Reviewers are the employee's manager and the role owner; a reviewer cannot review their own access; unactioned items auto-revoke after 10 working days; SoD rules are re-evaluated on every review.

### Z.12.10 Conflict-of-interest declarations and gifts register
- **COI declarations** (`ctl.coi_declarations`) at joining, annually and on change: relationships with parties, representatives, lenders, insurers, employers, law firms (last 3 years — FR-P01-27), vendors, other employers/moonlighting (MSO: harmful moonlighting without permission is misconduct), directorships, shareholdings, relatives employed in the group, and for multi-company staff per group entity [RC F13]. Declarations feed `ConflictIndex` (App. S §6.5), the approval engine (no approval where a declared relationship exists) and vendor onboarding. Undeclared conflict detected → `CTL_COI_UNDECLARED`.
- **Gifts and hospitality register** (`ctl.gifts_register`): staff never accept gifts or hospitality from parties (App. U §U.4 item 5 — Locked); from vendors and partners, anything above ₹1,000 (T) must be declared within 7 days and approved or returned; aggregate per giver per year reported to `compliance_officer`.

### Z.12.11 Whistle-blower / vigil channel and anti-victimisation
- Equator's channel is a P09 `WRK_WHISTLE` desk in the internal tenant (reporter token, no IP/device capture, separate store, never merged with POSH — FR-P09-28/34); anonymous or confidential named reporting.
- **Applicability:** a statutory vigil mechanism (Companies Act s.177(9)–(10); Meetings of Board Rules r.7) is mandatory only for listed companies, companies accepting public deposits, or companies borrowing > ₹50 crore from banks/PFIs; Equator is not currently in scope but runs the channel voluntarily [RC F13]. Flag `ctl.vigil.statutory_mode` (G tier, CS-owned facts) adds direct access to the Audit Committee chair (or Board-nominated director) and the s.177(10) safeguards; group companies that are listed NBFCs follow their own regime (LODR Reg. 22 [K]).
- **Protected status (anti-victimisation):** sealed services (POSH, whistle-blower) may set an opaque `ctl.protected_status` flag on an employee (complainant, witness, reporter) with an expiry (default 24 months, T) **without any reason or detail**. While set, any adverse action (PIP, rating below "Meets", termination, transfer, salary reduction, probation non-confirmation) requires an additional independent reviewer (HR head + a director-level reviewer outside the reporting line) and is reported to the IC presiding officer or vigil officer as a count only. The HRMS shows "Additional review required" — never why.

### Z.12.12 Exception register
`ctl.exceptions`: every override, waiver, compensating-control SoD exception, late approval, policy deviation, missed statutory clock and dismissed alert, with `reason` (≥ 30 characters), `approved_by` (higher authority than the requester), `expires_at`, `compensating_control`, `status`. Exceptions without a reason are rejected (`CTL_EXCEPTION_REASON_REQUIRED`, 422). Monthly exception report to the CEO designation and quarterly to the Board/Audit function.

### Z.12.13 Management dashboards of exceptions
Tiles for open Critical alerts, ghost hits, SoD exceptions by expiry, overdue and after-hours approvals, split-transaction suspects, bank changes in cooling, statutory-clock breaches, access-review completion, COI and gifts declarations, vigil reports (counts only) and audit findings; drill-down respects RBAC.

### Z.12.14 Internal-audit read-only workspace (register owned by Appendix AE)
The audit-evidence register, the auditor read-only workspace and the evidence export packs live in schema `eng` (Appendix AE §AE.8.3, §AE.8.4, §AE.8.7, §AE.11.2; X-66(g)), because `eng` exists from P00 and covers every engagement type. This appendix supplies only what the workforce and controls modules need:
- Roles: `internal_auditor` (Internal Audit department, independent — D3-06) and the existing `auditor` role (App. S) for statutory and external auditors. Access is granted through `eng.auditor_grants` (each grant ≤ 90 days from its start, FR-P01-27; scoped by entity, module and period; read-only; MFA; watermark on every view and export). Write attempts on `hr`, `pay` or `ctl` return `CTL_AUDIT_WORKSPACE_READ_ONLY`.
- Engagements, evidence requests (PBC), findings, management responses and follow-up use `eng.audit_engagements`, `eng.evidence_requests`, `eng.audit_findings` and `eng.management_responses`. The names `ctl.audit_engagements`, `ctl.evidence_requests` and `ctl.audit_findings` exist in v3.0 only as read-only compatibility views over them.
- `ctl` keeps the sampling tool (random, stratified or monetary-unit samples from runs, payments, claims and vendors, with the seed recorded for reproducibility) in `ctl.audit_samples`, with `engagement_id → eng.audit_engagements`.
- Evidence export uses the Appendix AE §AE.8.4 packs (`STATUTORY_BOOKS`, `ASSURANCE_PACK`; Appendix AC §AC.13 taxonomy) [RD DI-F 35]; this module supplies the `pay` and `ctl` ledger audit-trail extracts for them (§Z.9.10, NN-36).
- `ctl` continues to own the authority matrix (§Z.12.2), the maker-checker engine (§Z.12.3), the SoD matrix (§Z.12.4), the exception register (§Z.12.12), conflict-of-interest declarations and the gifts register (§Z.12.10) and the vigil channel (§Z.12.11).

---

## Z.13 Group companies, matrix work and secondment (NN-38; Appendix AD rules)

1. **Employer of record:** one `employing_entity_id` per employee at a time; payroll, EPF and ESI run only in the employing entity ([RE] DI-E 24).
2. **Secondment record** (`hr.secondments`, per Appendix AD): host entity, start/end dates, purpose, percentage of time, day-to-day control, that the lien and the right to terminate stay with the employer, cost-recharge basis and mark-up method, confidentiality to both entities, return on expiry, signed letter (e-signed PDF/A), GST/tax-adviser review flag (*CCE v Northern Operating Systems*, SC, 19 May 2022; CBIC Instruction 05/2023-GST) and the shared-services register reference with the s.188 approval reference where needed ([RE] F5.2–F5.3). Without a signed record, cross-company assignments above 0% cannot start (`HR_SECONDMENT_RECORD_REQUIRED`, 409).
3. **Cross-functional staff for Finbyx/Udofin:** either one employer with documented secondments and recharges, or separate part-time appointments with each entity each paying and contributing on its share — the second option is OFF (`hr.multi_employment.enabled`) pending payroll and PF advice on double-ceiling or under-contribution ([RE] F5.3) `[VERIFY — open: payroll/PF advice]`.
4. **Recharges:** allocations from `hr.assignments` produce monthly inter-company recharge schedules (cost + mark-up) for GST invoicing via the `grp` shared-services register (§Z.9.10). Cross-company dashboards use aggregates only under the GDSA.
5. **Data separation:** RLS by `employing_entity_id`; the host entity sees only the secondee's work-related fields (name, role, work contact, schedule, assignment-related work items) — never compensation, bank, BGV or vault; cross-entity HR views only through `group_hr` grants that are purpose-bound, time-limited (≤ 90 days), maker-checker approved, and logged per access under the Group Data-Sharing Agreement (NN-38). The employee notice names all group entities and purposes ([RE] F5.1).
6. **Ethical walls:** a user with roles in Finbyx or Udofin gets no Equator case-data role for matters involving those companies' clients; the SoD check runs at role grant; annual attestation; case and allocation data are never shared with Finbyx or Udofin (NN-38; [RE] DI-E 26).

---

## Z.14 RBAC and field-level visibility

### Z.14.1 Role × resource matrix (C create · R read · U update · S approve · X execute · — none; [conditions])
| Role | Employee master | Compensation | Bank / tax IDs | Attendance & leave | Pay run / payslips | Appraisal | Recruitment | Vault | `ctl` approvals | Exceptions / alerts | Audit workspace |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `employee` | R, U own (contact, emergency, address) | R own | U own (bank via §Z.12.5); R own masked | C, R own; dispute | R own payslips, Form 130 | C self-review; R own | apply (candidate portal) | R own documents | C requests (own claims) | — | — |
| Manager (contextual: solid-line) | R team [limited fields] | — (R proposals during increment cycle for own team) | — | R team; S approve | — | C, U, R team reviews | R own requisitions' candidates | R letters addressed to team members [policy] | S within limits | R own team's alerts | — |
| `department_head` | R department [limited] | R department aggregates; S per DoFP | — | R; S escalations | R department cost aggregates | S calibration member | C requisitions; S offers per DoFP | — | S within limits | R department | — |
| `hr_executive` | C, R, U [entity] | R | R masked; U via workflow | R, U regularise | R | R | C, R, U | C, R [category] | C requests | R HR alerts | — |
| `hr_manager` | C, R, U, S [entity] | R, U (maker) | R masked; reveal with reason + audit | R, U, S | R | R, S (HR checks) | S | R, U | S per DoFP | R, U HR | — |
| `payroll_maker` | R | R | R masked; reveal for bank file errors with reason | R (frozen inputs) | C, U run; submit | — | — | — | C | R payroll alerts | — |
| `payroll_checker` | R | R | R masked | R | S run (HR side) | — | — | — | S per DoFP | R, resolve ghost hits | — |
| `finance_controller` | R [agg + names in run] | R totals; S per DoFP | — | — | S run (Finance side) | — | — | — | S per DoFP | R | — |
| `finance_ops` | — | — | — | — | X release bank file | — | — | — | X execute approved | R | — |
| `it_admin` | R (name, role, dept, status) | — | — | — | — | — | — | — | X role grants approved | R JML alerts | — |
| `compliance_officer` | R [agg] | — | — | R registers | R statutory outputs; C rule-pack maker | — | — | — | — | R all | — |
| `dpo` | R [DSR / incident grant] | — | — | R (monitoring approvals) | — | — | — | R [grant] | S `EXPORT-SENSITIVE` | R privacy alerts | — |
| `internal_auditor` / `auditor` | R [grant] | R [grant] | R masked | R [grant] | R [grant] | R [grant] | R [grant] | R [grant, watermark] | R | R | C, R, U own engagements |
| `group_hr` | R [cross-entity grant only] | R [grant] | — | R [grant] | — | R [grant] | R [grant] | — | — | R [grant] | — |
| `ops_director` | R [agg] | R aggregates; S per DoFP | — | R aggregates | R cost aggregates | S calibration oversight | S per DoFP | — | S per DoFP | R | — |

### Z.14.2 Field-level rules (Cerbos + RLS; Locked)
- **Manager's team view fields:** name, photo (optional), designation, department, grade (not salary), work mode and `work_location_state`, reporting line, tenure, attendance summary and daily status, leave balances and calendar (type visible for approval only), goals and reviews of direct reports, KPI scorecards of direct reports, assets assigned, training status. **Never:** salary or CTC (except the increment-cycle proposal view for direct reports), bank details, PAN/Aadhaar reference/UAN, BGV report, health or disability information, sick-leave reasons, disciplinary records not addressed to the manager, POSH or whistle-blower status.
- **HR data is visible only to HR roles** within the employing entity; payroll roles see what the run needs; identifiers are masked by default (`PAN ABCDE****F`) and reveal requires a reason, step-up and an `audit.access_log` row (`HR_FIELD_NOT_VISIBLE`, 403, for denied fields).
- **Employees see their own data** completely (NN-35), except third-party confidential content (e.g., interviewer notes about others, investigation material under legal hold) — withholding is recorded with the reason.
- **Sealed:** POSH and whistle-blower content never enters `hr`/`pay`/`ctl` (NN-07); only opaque hold and protected-status flags.
- **Mobile:** employee self-service (attendance, leave, payslips, approvals within limits) is available on mobile; bank changes, salary data of others, pay-run approval and vault downloads are web-only with managed device where the SKU allows.

---

## Z.15 Settings catalogue (NN-33 tiers: L Locked · G Governed · T Tenant)

Keys follow `<scope>.<module>.<key>`; the settings UI shows the tier badge, who may change it and whether approval is needed (P15). G changes use maker ≠ checker, source citation, effective dates, preview against the last finalised run, rollback and legal-reviewer sign-off where third-party (employee) rights are affected.

| Key | Default | Tier | Who changes / bounds |
|---|---|---|---|
| `platform.hr.monitoring.prohibited_set` | keystroke, webcam, covert screen, off-hours location, personal comms, BYOD personal area, meeting-presence scoring | L | — |
| `platform.hr.metrics.outcome_metrics_forbidden` | settlement rate, outcomes, amounts recovered, neutral selection | L | — |
| `platform.pay.wage_definition.logic` | CoW s.2(y) classes and 50% test | L | — |
| `platform.pay.deduction_cap_pct` | 50 | L | — |
| `platform.pay.overtime_min_multiplier` | 2.0 | L | Tenant may set higher (T) |
| `platform.pay.statutory_dues_non_waiver` | on | L | — |
| `platform.pay.run.block_on_not_confirmed_params` | on | L | — |
| `platform.pay.bank_payment_only` | on (no cash) | L | — |
| `platform.hr.national_holidays` | 26 Jan, 15 Aug, 2 Oct | L | — |
| `platform.ctl.maker_ne_checker` | on | L | — |
| `platform.ctl.bank_change.cooling_floor_working_days` | 1 | L | — |
| `iam.leaver_revoke_hours` | 4 | L floor | Tenant may tighten |
| `platform.hr.posh_data_in_hr` | never | L | — |
| `rulepack.IN.payroll.*`, `rulepack.IN-<ST>.payroll.*` (rule-pack map §Z.2.4) | §Z.2.4–Z.2.5 | G | `compliance_officer` maker; CS/`finance_controller` checker; legal reviewer |
| `tenant.hr.establishment_state_rules` (D3-31 mode) | establishment-state | G | CS; counsel/CA opinion reference to change |
| `pay.pt.residence_state_mode` | OFF | G flag | CA opinion on file |
| `pay.epf.voluntary_higher_wage` | per employee election | G | HR + employee consent |
| `pay.bonus.enabled` | auto at 20 employees; blocked while ceilings `NOT_CONFIRMED` | G | Payroll Compliance Officer |
| `tenant.ctl.authority_rules` (DoFP) | Z.12.2 proposals | G | Board resolution reference; CEO designation + `finance_controller` |
| `tenant.ctl.sod_rules` (additions) | SOD-01…15 | G | Additions only; removal of seed rules Locked |
| `ctl.vigil.statutory_mode` | derived from applicability facts | G | CS |
| `group.audit.applicability.*` (owner Appendix AE §AE.8.2, §AE.15; alias `audit.applicability.*`) | r.13, CARO tests | G | CS (maker) + `legal_reviewer` (checker), reviewed each April |
| `hr.monitoring.investigation_capture.enabled` | OFF | G flag | DPO + HR + legal reviewer; per case ≤ 30 days |
| `hr.attendance.geofence.enabled` / `hr.attendance.biometric.enabled` | OFF / OFF | G flag | DPO approval + re-notice |
| `hr.analytics.individual_roi.enabled` | OFF | G flag | DPIA approved by DPO + HR head |
| `hr.appraisal.forced_distribution.enabled` | OFF | G flag | DPIA + HR head |
| `hr.multi_employment.enabled` | OFF | G flag | Payroll/PF advice on file |
| `ops.workspace.google.enabled` (canonical `platform.ops.workspace.google.enabled`; owner Appendix AC §AC.17) | OFF | G flag | Company Secretary + DPO after residency ADR |
| `pay.payout.api.enabled` | OFF | G flag | Bank/vendor contract |
| `tenant.pay.external_payroll.enabled` | OFF | G flag | Entity declares an external payroll system of record; `PAYROLL_EXCHANGE_PORT` imports pay registers read-only (Appendix AC; P21 FR-P21-23) |
| `tenant.hr.workspace.sku_rules` | console/finance/HR/payroll → Premium; others → Basic; contractors → none | T (maker-checker) | `it_admin` + security lead |
| `tenant.hr.workspace.delete_delay_days` | 90 | T | 30–365 |
| `tenant.hr.probation.default_months` / `.max_extension_months` / `.deemed_confirmation` | 6 / 3 / true | T | `hr_manager` |
| `tenant.hr.notice_period_days.<grade>` | 30 (G1–G4), 60 (G5–G8) | T | Not below statute/contract |
| `tenant.hr.attendance.regularisation_window_days` | 7 | T | 1–30 |
| `tenant.hr.attendance.standard_week_hours` | 40 | T | ≤ 48 |
| `tenant.hr.leave.template` | `leave.equator_standard@2026.1` (alternative `leave.statutory_minimum@2026.1`) | T | Validator ≥ floor |
| `tenant.hr.leave.sandwich_rule` | not counted | T | — |
| `tenant.hr.leave.planned_notice_days` | 7 | T | — |
| `tenant.hr.leave.paternity_days` / `.bereavement_days` | 5 / 3 | T | Management decision |
| `tenant.hr.qa.sample_pct` / `.min_items` | 5 / 3 | T | 1–20% |
| `tenant.hr.metrics.min_cohort` | 5 | T | ≥ 5 (floor L) |
| `tenant.hr.appraisal.scale` | 5-point | T | — |
| `tenant.hr.pip.min_days` | 60 | T | ≥ 30 |
| `tenant.hr.appeal.window_days` | 15 | T | ≥ 7 |
| `tenant.hr.protected_status.duration_months` | 24 | T | ≥ 12 |
| `tenant.pay.pay_day` | last working day | T | ≤ statutory deadline |
| `tenant.pay.input_freeze_day` | 25 | T | — |
| `tenant.pay.variance_threshold_pct` | 10 | T | 1–50 |
| `tenant.pay.tax.proof_window` | Jan–Feb | T | — |
| `tenant.ctl.bank_change.cooling_working_days` | 3 | T | 1–7 |
| `tenant.ctl.bank_change.pre_run_freeze_days` | 5 | T | 0–10 |
| `tenant.ctl.approval.expiry_days` / `.escalation_working_days` | 14 / 2 | T | — |
| `tenant.hr.probation.reminder_offsets_days` *(v3.1)* | 45, 30, 15, 7, 0 | T | Last offset 0; first ≥ 30 |
| `tenant.hr.work_summary.reply_window_days` *(v3.1)* | 10 working days | T | ≥ 5 |
| `tenant.hr.leave.coverage.min_on_duty_pct` / `.min_headcount_by_role` / `.blackout_windows` / `.mode` *(v3.1)* | 60% / none / none / `warn` | T | Never applied to maternity, sick, bereavement, statutory or court-ordered leave (L) |
| `tenant.hr.appraisal.min_evidence_completeness_pct` *(v3.1)* | 60 | T | 40–90 |
| `tenant.pay.variance.*` (run, employee, hold and second-checker thresholds, §Z.9.4) *(v3.1)* | §Z.9.4 table | T | Loosening needs `internal_auditor` acknowledgement; hold deadline D-1 of the statutory deadline is L |
| `tenant.pay.lop_divisor` *(v3.1)* | calendar days of the wage period | T (calendar days); G (any other divisor) | Never deducts more than the absence proportion |
| `tenant.ctl.delegation.on_leave.min_days` / `.require_delegate` *(v3.1)* | 2 working days / true | T | Delegation depth 1 and SoD (L) |
| `tenant.ctl.anomaly.shadow_days` *(v3.1)* | 30 | T | ≥ 14 |
| `tenant.ctl.anomaly.*`, `tenant.ctl.expense.*`, `tenant.ctl.petty_cash.*`, `tenant.ctl.procurement.*`, `tenant.ctl.gifts.*`, `tenant.hr.roster.*`, `tenant.hr.workspace.upn_pattern`, `tenant.hr.service_certificate_days` | Values stated in §Z.4–Z.12 | T | Tighten freely; loosening anomaly, expense or petty-cash values needs `internal_auditor` acknowledgement |

---

## Z.16 Data model (DDL sketches; Appendix F conventions; tenant RLS + entity RLS on every table)

```sql
CREATE SCHEMA hr; CREATE SCHEMA pay; CREATE SCHEMA ctl;
-- Entity isolation (NN-38): RESTRICTIVE policy ANDed with tenant_isolation
CREATE FUNCTION rls.enable_entity_rls(p_schema text, p_table text) RETURNS void LANGUAGE plpgsql AS $$
BEGIN PERFORM rls.enable_tenant_rls(p_schema, p_table);
  EXECUTE format('CREATE POLICY entity_scope AS RESTRICTIVE ON %I.%I USING (legal_entity_id = ANY
    (coalesce(nullif(current_setting(''app.entity_ids'', true), '''')::uuid[], ''{}'')) OR core.platform_scope())', p_schema, p_table);
END $$;

CREATE TABLE hr.employees (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL REFERENCES hr.legal_entities(id),
  employee_no text NOT NULL, person_id uuid NOT NULL,                     -- core person (workforce identity link, App. S §1.3)
  engagement_type text NOT NULL CHECK (engagement_type IN ('employee','fixed_term_employee','apprentice','professional_engagement','contractor_staff')),
  status text NOT NULL CHECK (status IN ('candidate_accepted','pre_joining','onboarding','probation','confirmed','on_notice','suspended',
         'on_secondment','long_leave','exit_initiated','exit_effective','settled','archived')),
  establishment_id uuid NOT NULL REFERENCES hr.establishments(id), work_location_state text NOT NULL,
  work_mode text NOT NULL CHECK (work_mode IN ('office','remote','hybrid')),
  worker_classification text NOT NULL CHECK (worker_classification IN ('worker','non_worker','uncertain')),
  department_id uuid NOT NULL, position_id uuid, manager_employee_id uuid REFERENCES hr.employees(id),
  joined_on date, exit_effective_on date, pan_enc bytea, pan_hmac char(64), uan_enc bytea, uan_hmac char(64),
  aadhaar_ref_masked text, retention_class text NOT NULL DEFAULT 'hr_employee_file', retain_until date,
  legal_hold boolean NOT NULL DEFAULT false, std_cols,
  UNIQUE (tenant_id, employee_no), CHECK (manager_employee_id IS DISTINCT FROM id));
CREATE UNIQUE INDEX one_active_employment_per_pan ON hr.employees (tenant_id, pan_hmac)
  WHERE status NOT IN ('exit_effective','settled','archived');              -- GH-08 at DB level within a tenant
-- hr.employees_history: same columns + history_id, op, changed_by, changed_at, reason, change_request_id (r.3(1) edit log)
CREATE TABLE hr.assignments (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL,
  employee_id uuid NOT NULL REFERENCES hr.employees(id), kind text NOT NULL CHECK (kind IN ('primary','matrix','project','secondment')),
  host_entity_id uuid, department_id uuid, dotted_manager_id uuid, allocation_pct numeric(5,2) NOT NULL CHECK (allocation_pct BETWEEN 0 AND 100),
  secondment_id uuid, valid_from date NOT NULL, valid_to date,
  CHECK (kind <> 'secondment' OR secondment_id IS NOT NULL), CHECK (host_entity_id IS NULL OR host_entity_id = legal_entity_id OR secondment_id IS NOT NULL));
CREATE TABLE hr.secondments (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL,
  employee_id uuid NOT NULL, host_entity_id uuid NOT NULL, starts_on date NOT NULL, ends_on date NOT NULL, time_pct numeric(5,2) NOT NULL,
  control_clause text NOT NULL, termination_stays_with_employer boolean NOT NULL CHECK (termination_stays_with_employer),
  recharge_basis jsonb NOT NULL, shared_services_ref uuid, s188_ref text, gst_review_status text NOT NULL DEFAULT 'pending',
  signed_document_id uuid NOT NULL, std_cols, CHECK (ends_on >= starts_on), CHECK (time_pct > 0 AND time_pct <= 100));
CREATE TABLE pay.bank_accounts (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL,
  payee_id uuid NOT NULL REFERENCES ctl.payees(id), account_enc bytea NOT NULL, account_hmac char(64) NOT NULL, ifsc text NOT NULL,
  holder_name_verified text, penny_drop_ref text, name_match_score numeric(5,2), status text NOT NULL CHECK (status IN
  ('pending_verification','cooling','active','frozen','retired')), cooling_until timestamptz, change_request_id uuid NOT NULL);
CREATE TABLE pay.runs (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL,
  period_start date NOT NULL, period_end date NOT NULL, kind text NOT NULL CHECK (kind IN ('regular','offcycle','fnf','bonus','arrears')),
  status text NOT NULL, inputs_snapshot_sha256 char(64), maker_user_id uuid NOT NULL, hr_checker_user_id uuid, finance_checker_user_id uuid,
  release_user_id uuid, bank_file_sha256 char(64), bank_ack_sha256 char(64), approval_request_id uuid,
  CHECK (hr_checker_user_id IS DISTINCT FROM maker_user_id AND finance_checker_user_id IS DISTINCT FROM maker_user_id
     AND finance_checker_user_id IS DISTINCT FROM hr_checker_user_id
     AND release_user_id IS DISTINCT FROM hr_checker_user_id AND release_user_id IS DISTINCT FROM finance_checker_user_id
     AND release_user_id IS DISTINCT FROM maker_user_id),                  -- v3.1: all four actors distinct (NN-36)
  CHECK (period_end >= period_start));
CREATE UNIQUE INDEX one_regular_run_per_period ON pay.runs (legal_entity_id, period_start)
  WHERE kind = 'regular' AND status <> 'cancelled';                          -- v3.1: replaces a UNIQUE that included id
CREATE TABLE ctl.approval_requests (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL,
  action_code text NOT NULL, subject_type text NOT NULL, subject_id uuid NOT NULL, amount_minor bigint, currency char(3),
  payload_sha256 char(64) NOT NULL, maker_user_id uuid NOT NULL, status text NOT NULL CHECK (status IN
  ('pending','approved','rejected','expired','withdrawn','executed')), expires_at timestamptz NOT NULL, created_at timestamptz NOT NULL DEFAULT now());
CREATE TABLE ctl.approval_steps (request_id uuid NOT NULL REFERENCES ctl.approval_requests(id), step_no int NOT NULL,
  approver_user_id uuid NOT NULL, decision text CHECK (decision IN ('approve','reject')), decided_at timestamptz, acr text, network_zone text,
  comment text, PRIMARY KEY (request_id, step_no));
CREATE FUNCTION ctl.no_self_approval() RETURNS trigger LANGUAGE plpgsql AS $$ BEGIN
  IF NEW.approver_user_id = (SELECT maker_user_id FROM ctl.approval_requests WHERE id = NEW.request_id)
     OR EXISTS (SELECT 1 FROM ctl.approval_steps s WHERE s.request_id = NEW.request_id AND s.step_no <> NEW.step_no
                AND s.approver_user_id = NEW.approver_user_id)
  THEN RAISE EXCEPTION 'CTL_SELF_APPROVAL_BLOCKED' USING ERRCODE = '42501'; END IF; RETURN NEW; END $$;
CREATE TRIGGER approval_steps_sod BEFORE INSERT OR UPDATE ON ctl.approval_steps FOR EACH ROW EXECUTE FUNCTION ctl.no_self_approval();
CREATE TABLE ctl.exceptions (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, legal_entity_id uuid NOT NULL,
  kind text NOT NULL, subject_ref uuid, reason text NOT NULL CHECK (length(reason) >= 30), requested_by uuid NOT NULL,
  approved_by uuid NOT NULL CHECK (approved_by <> requested_by), compensating_control text, expires_at timestamptz NOT NULL, status text NOT NULL);
CREATE TABLE ctl.protected_status (employee_id uuid PRIMARY KEY, tenant_id uuid NOT NULL, set_by_service text NOT NULL
  CHECK (set_by_service IN ('posh_sealed','whistle')), expires_at date NOT NULL);       -- no reason column by design
```
Further tables, with key columns, are listed in P18 §7.2; notable constraints not shown above: `hr.attendance_days` CHECK (`overtime_minutes = 0 OR overtime_consent_id IS NOT NULL`); `hr.leave_ledger`, `pay.run_lines` and `hr.jml_events` append-only (`core.deny_mutation()`); `pay.run_lines.param_version_ids uuid[] NOT NULL`; `pay.run_line_holds` (append-only: `run_line_id`, `hold_status` ∈ `held`, `released`, `paid_offcycle`, `cancelled_ghost`, `reason_code`, `owner_role`, `deadline_at`, `decided_by`, `second_reviewer`; the latest row is the line's effective status, none = not held) *(v3.1)*; `hr.work_replies` (append-only; §Z.7.4) and `ctl.anomaly_rules` (versioned; `mode`, `parameters`, `review_due`) with `ctl.alert_dispositions` *(v3.1)*; `pay.rule_params` immutable read model of approved `cfg` versions (columns per §Z.2.4); `hr.work_items` partitioned by `occurred_at`, carrying an opaque `subject_ref` only (NN-16). Database roles: `eq_app` with `app.entity_ids` set per request; `eq_readonly_audit` gains `SELECT` on masked `hr`/`pay`/`ctl` audit views; `pgaudit` on `pay` and `ctl`.

---

## Z.17 APIs, events and error codes

### Z.17.1 API resource map (`/v1/ops/...`; OpenAPI 3.1; Idempotency-Key on every POST that creates money, people or approvals; full list in P18 §7.3)
`/org/*` (entities, establishments, departments, cost-centres, positions, headcount-plans) · `/hr/requisitions`, `/hr/job-posts`, `/hr/candidates`, `/hr/interviews`, `/hr/offers` · `/hr/employees` (+ `/lifecycle-events`, `/assignments`, `/secondments`, `/exits`, `/clearances`) · `/hr/workspace/*` (accounts, jml-events) · `/hr/attendance/*` (sessions, days, regularisations, rosters, wfh-declarations, overtime-consents) · `/hr/leave/*` · `/hr/metrics/*`, `/hr/scorecards` · `/hr/performance/*` (goals, check-ins, cycles, reviews, calibrations, pips, appeals) · `/hr/learning/*`, `/hr/assets` · `/hr/me/*` (self-service, disputes) · `/pay/*` (components, structures, compensation, bank-accounts, tax, runs, payslips, statutory, loans, fnf, journals, registers) · `/ctl/*` (authority-rules, approvals, delegations, sod, payees, bank-changes, vendors, purchase-requests, purchase-orders, expense-claims, petty-cash, alerts, exceptions, coi, gifts, audit).

### Z.17.2 Events (CloudEvents; payloads carry IDs and codes only, never salary, bank or identifier values)
`equator.hr.requisition.approved.v1` · `equator.hr.offer.accepted.v1` · `equator.hr.employee.created.v1` · `equator.hr.employee.activated.v1` · `equator.hr.employee.confirmed.v1` · `equator.hr.employee.role_changed.v1` · `equator.hr.employee.transferred.v1` · `equator.hr.secondment.started.v1` / `.ended.v1` · `equator.hr.exit.initiated.v1` · `equator.hr.employee.exit_effective.v1` · `equator.hr.employee.archived.v1` · `equator.hr.workspace.account_provisioned.v1` / `.account_disabled.v1` · `equator.hr.attendance.day_closed.v1` · `equator.hr.leave.request_decided.v1` · `equator.hr.leave.started.v1` *(v3.1)* · `equator.hr.leave.ended.v1` *(v3.1)* · `equator.hr.leave.cancelled.v1` *(v3.1)* · `equator.hr.review.released.v1` · `equator.hr.pip.started.v1` · `equator.hr.data_dispute.raised.v1` · `equator.pay.rule_param.published.v1` · `equator.pay.run.calculated.v1` / `.approved.v1` / `.released.v1` / `.bank_confirmed.v1` · `equator.pay.payslip.issued.v1` · `equator.pay.fnf.paid.v1` · `equator.pay.statutory_clock.breached.v1` · `equator.ctl.approval.requested.v1` / `.approved.v1` / `.rejected.v1` / `.executed.v1` · `equator.ctl.sod.violation_blocked.v1` · `equator.ctl.bank_change.requested.v1` / `.confirmed.v1` / `.reversed.v1` · `equator.ctl.alert.raised.v1` · `equator.ctl.exception.recorded.v1` · `equator.ctl.access_review.completed.v1` · *(v3.1)* `equator.hr.work_reply.added.v1` · `equator.hr.probation.review_due.v1` · `equator.pay.run_line.held.v1` / `.hold_resolved.v1` · `equator.ctl.delegation.activated.v1` / `.ended.v1` · `equator.ctl.anomaly_rule.promoted.v1`. Internal bus only; never delivered to tenant webhooks.

**Leave-driven cover contract** *(v3.1)*. Every consumer that re-routes work while a person is on leave uses these events and no other `hr` data: Appendix S §6.4 leave-driven cover and delegation, K §5.10 (pre-litigation case-manager queue), N §2.2 (neutral availability and caps), O §7.6 (billing approvals), Q §2.4 (deputy DPO, `tenant.legal_entity.dpo_deputy`), Appendix AG §AG.4.5 (Away prompt), P08 FR-P08-87 and P09 FR-P09-50 (clock and ticket re-assignment), §Z.12.2 `LeaveDelegationJob`, and chambers queues (Appendix W §W.5.8, from the `chm` HR-lite equivalent). `request_decided` (on approval) lets consumers plan cover at least 2 working days ahead; `started`, `ended` and `cancelled` switch it on and off. Payloads carry `employee_id`, `person_id`, `from`, `to`, half-day flags and the `cover_person_id` named on the leave form — **never the leave type, reason or documents** (health and family data stay in `hr`; NN-35). A consumer that misses `ended` restores routing at `to` + 1 working day.

### Z.17.3 Error codes (register in Appendix F §F.10.4 v3; en/hi messages in `packages/i18n/errors.workforce.json`, plain language, no internal detail)

| Code | HTTP | Code | HTTP |
|---|---|---|---|
| `HR_REQUISITION_BUDGET_EXCEEDED` | 422 | `PAY_DEDUCTION_CAP_EXCEEDED` | 422 |
| `HR_REPORTING_CYCLE` | 422 | `PAY_FINE_EVIDENCE_MISSING` | 422 |
| `HR_WORKER_CLASSIFICATION_REQUIRED` | 409 | `PAY_COMPONENT_CLASS_LOCKED` | 409 |
| `HR_APPOINTMENT_LETTER_MISSING` | 409 | `PAY_RUN_LOCKED` | 409 |
| `HR_PREJOIN_CHECKS_INCOMPLETE` | 409 | `PAY_RUN_VARIANCE_UNREVIEWED` | 409 |
| `HR_POLICY_ACK_PENDING` | 409 | `PAY_MAKER_CHECKER_SAME_USER` | 403 |
| `HR_SECONDMENT_RECORD_REQUIRED` | 409 | `PAY_GHOST_HITS_UNRESOLVED` | 409 |
| `HR_DUPLICATE_ACTIVE_EMPLOYMENT` | 409 | `PAY_BANK_FILE_HASH_MISMATCH` | 409 |
| `HR_ENTITY_TRANSFER_REQUIRES_REJOIN` | 409 | `STATUTORY_WAIVER_FORBIDDEN` (existing canonical F code, not new; alias `WRK_STATUTORY_DUES_WAIVER`) | 422 |
| `HR_FIELD_NOT_VISIBLE` | 403 | `PAY_REGIME_LOCKED` | 409 |
| `HR_LEAVE_POLICY_BELOW_FLOOR` | 422 | `PAY_PROOF_WINDOW_CLOSED` | 422 |
| `HR_LEAVE_BALANCE_INSUFFICIENT` | 422 | `PAY_GL_PERIOD_LOCKED` | 409 |
| `HR_OVERTIME_CONSENT_REQUIRED` | 409 | `CTL_AUTHORITY_LIMIT_EXCEEDED` | 403 |
| `HR_OVERTIME_QUARTERLY_CAP` | 422 | `CTL_SELF_APPROVAL_BLOCKED` | 403 |
| `HR_NIGHT_WORK_CONSENT_REQUIRED` | 409 | `CTL_SOD_CONFLICT` | 409 |
| `HR_MONITORING_PROHIBITED` | 403 | `CTL_APPROVER_CONFLICTED` | 403 |
| `HR_MONITORING_APPROVAL_REQUIRED` | 409 | `CTL_PAYLOAD_CHANGED` | 409 |
| `HR_REGULARISATION_WINDOW_CLOSED` | 422 | `CTL_COOLING_OFF_ACTIVE` | 409 |
| `HR_METRIC_OUTCOME_FORBIDDEN` | 422 | `CTL_OOB_CONFIRMATION_PENDING` | 409 |
| `HR_PIP_SAFEGUARD_MISSING` | 422 | `CTL_PENNY_DROP_MISMATCH` | 422 |
| `HR_CERTIFICATION_REQUIRED` | 409 | `CTL_DUPLICATE_BANK_ACCOUNT` | 409 |
| `HR_WORKSPACE_SKU_INSUFFICIENT` (alias `WORKSPACE_SKU_INSUFFICIENT_FOR_ROLE`) | 409 | `CTL_VENDOR_KYC_INCOMPLETE` | 409 |
| `HR_WORKSPACE_DELETE_BLOCKED_HOLD` (alias `WORKSPACE_DELETE_BLOCKED_HOLD`) | 409 | `CTL_COI_UNDECLARED` | 409 |
| `HR_EXIT_CLEARANCE_PENDING` | 409 | `CTL_EXCEPTION_REASON_REQUIRED` | 422 |
| `PAY_PARAM_NOT_CONFIRMED` | 409 | `CTL_APPROVAL_EXPIRED` | 409 |
| `PAY_PARAM_ACK_REQUIRED` | 409 | `CTL_PETTY_CASH_LIMIT` | 422 |
| `PAY_WAGE_DEFINITION_BREACH` | 422 | `CTL_AUDIT_WORKSPACE_READ_ONLY` | 403 |
| `PAY_MIN_WAGE_BREACH` | 422 | `PAY_HOLD_PAST_DEADLINE` *(v3.1)* | 409 |
| `HR_RATING_REASON_PROHIBITED` *(v3.1)* | 422 |  |  |

---

## Z.18 Privacy, retention and audit

### Z.18.1 Lawful basis register (employee data)
| Purpose | Basis | Notes |
|---|---|---|
| Employment administration, payroll, statutory registers and returns, attendance | DPDP s.7(i) (employment) + legal obligation (CoW s.50; OSH s.33; Income-tax Act 2025) | Employer's basis only; a sister company cannot rely on it ([RE] F5.1) |
| Security logs, access control, fraud prevention | s.7(i) (safeguarding the employer from loss or liability) | Not used for productivity scoring |
| Optional items (wellbeing surveys, optional productivity insights, future-vacancy candidate pool, photo) | Consent, separately withdrawable | Withdrawal propagates within 15 min |
| Group processing (shared HRMS run by one entity for others) | Intra-group processing agreement (s.8(2)); notice names entities and purposes | NN-38 |

DPDP core obligations commence 13 May 2027 (build to comply now, NN-15); IT Act s.43A and SPDI Rules continue until then (X-37); biometric data is SPDI sensitive data [K]. The employee privacy notice (s.5 format; English and Hindi) is part of the appointment letter pack and the candidate portal; the workforce-measurement notice is §Z.6.1.

### Z.18.2 Data minimisation and security
Aadhaar never stored in full (NN-14); PAN, UAN, bank numbers encrypted with keyed hashes for duplicate checks; health/disability data High tier, HR head only; BGV reports restricted; identifiers masked on screen; exports of HR/payroll data require `EXPORT-SENSITIVE` approval and carry watermarks; mass-export detection (Q SC-10); HR and payroll screens require managed devices where the SKU allows (App. S §2.6).

### Z.18.3 Retention classes (add to Q §2.8 / `core.retention_classes`; legal hold overrides)
| Class | Default | Driver |
|---|---|---|
| `hr_candidate` | 6 months after decision (12 months with future-vacancy consent) | Policy [recommendation] |
| `hr_employee_file` | 8 years after exit | Covers known floors; EPF/ESI/POSH/income-tax periods `[NC]` ([RC] F11) |
| `payroll_record` | 8 years from end of FY | Companies Act s.128(5) (pack); r.3(1) edit log |
| `attendance_register` | 5 years after last entry | Wages (Central) Rules r.51 |
| `attendance_raw` | 1 year, then aggregated | DPDP Rule 8(3) floor [RC D.23] |
| `bgv_report` | Until confirmation + 1 year, then summary only | Policy [recommendation] |
| `investigation_capture` | Case closure + 1 year | [RC D.22] |
| `appraisal` | 5 years after cycle | Policy |
| `unclaimed_wages` | 7 years | Wages (Central) Rules r.47 |
| `ctl_approval` / `ctl_exception` | 8 years | Books of account support |

### Z.18.4 Audit
Every create/update/approve/execute in `hr`, `pay`, `ctl` writes an NN-22 hash-chained `audit.audit_events` row with before/after digests; every reveal of a masked field and every cross-entity read writes `audit.access_log`; payroll and controls master data keep temporal history (r.3(1) proviso). Evidence collectors added to Q §7.3: `jml_sla_report`, `workspace_sku_role_check`, `ledger_audit_trail_check` (now incl. `pay`, `ctl`), `payroll_run_controls` (per run: maker/checker/releaser distinct, variance reviewed, bank-file hash matched), `ghost_scan_results` (weekly), `sod_matrix_check` (daily: active violations = 0 or excepted), `monitoring_prohibited_check` (daily: prohibited sources disabled), `statutory_clock_report` (monthly).

### Z.18.5 AI guardrails (P11 registry)
Permitted with `requires_human_review = true`: drafting job descriptions and offer/appointment letters from templates; summarising a CV against stated criteria; answering employee policy questions from the approved policy corpus with citations (`hr_policy_assistant`); narrating aggregate dashboards (`analytics_narrator`); extracting fields from receipts and tax proofs (`document_extractor`). **Prohibited (Locked):** ranking or rejecting candidates; generating or suggesting performance ratings, PIPs, terminations or increments; inferring emotions, health, intent or productivity from communications or telemetry; tax-regime recommendations; any use of POSH or whistle-blower content. HR and payroll data never enter few-shot examples or training (FR-P11-17 extended). LLM unavailable → manual forms (NN-02).

---

## Z.19 CI tests required (names; details in P18 §12)
`NN-35_monitoring_prohibited` · `NN-35_employee_self_view_complete` · `NN-35_dispute_freezes_metrics` · `NN-35_outcome_metrics_forbidden` · `NN-36_no_self_approval` · `NN-36_payee_to_reconcile_chain_split` · `NN-36_bank_change_cooling_and_oob` · `NN-36_payroll_edit_log_cannot_be_disabled` · `NN-36_payload_digest_reverified` · `NN-38_entity_rls_hr_pay_ctl` · `NN-38_secondment_required_for_host_work` · `PAY_golden_wage_definition_76000` · `PAY_epf_split_month_sep2026` · `PAY_deduction_cap_carry_forward` · `PAY_run_blocks_not_confirmed_param` · `HR_leave_policy_floor_validator` · `HR_ff_within_two_working_days` · `X-57_leaver_timings` · *(v3.1)* `PAY_golden_W01`…`PAY_golden_W14` (§Z.9.13) · `HR_leave_true_up_rj_252` · `PAY_line_hold_deadline` · `PAY_run_actors_all_distinct` · `NN-36_sod15_approve_reconcile_split` · `HR_coverage_never_blocks_protected_leave` · `CTL_delegation_on_leave_auto` · `CTL_anomaly_shadow_before_alert` · `NN-35_reply_visible_unedited` · `HR_rating_not_lowered_for_approved_leave`.

---

## Z.20 Open items and verification flags
1. **SKU** — Company Secretary to confirm the Microsoft 365 plan (D3-04); Graph licensing details (group-based licensing on Basic, `usageLocation`, mailbox delay, shared-mailbox limits, add-on prices) `[VERIFY — open: RD open point 2]`.
2. **Departmental structure** — management to confirm or replace the D3-06 default before first position creation.
3. **DoFP** — Board to approve the authority matrix values in Z.12.2 (proposals only).
4. **Remote-employee jurisdiction** — written CA/counsel opinion on S&E Act, PT and LWF for permanent remote staff (D3-31) `[VERIFY — open: RC open point 9]`.
5. **Parameters `[NC]`** — every row of §Z.2.4–Z.2.5 marked `NOT_CONFIRMED` or `SECONDARY_ONLY` ([RC] open points 1–12), notably bonus ceilings, OSH Central Rules details, ESIC rates, S.O. 5109(E) text and the September 2026 split month, s.202(1) slabs, Form 123/138 dates, contractor TDS, State minimum wages and PT/LWF conflicts.
6. **Appointment-letter duty below 10 workers** `[NC]` — issued in all cases regardless.
7. **Remote women's night work** — counsel to confirm which OSH Central Rules conditions apply to home working.
8. **Multi-employment option** (§Z.13 item 3) — payroll/PF advice.
9. **Related-party training purchases** from Infrabyx Consultancy (OPC) Pvt Ltd — CS to confirm s.188 treatment and the Infrabyx shareholding chain ([RE] open point 8).
10. **DPDP s.7(i)** — quote enacted text from the Gazette in the employee notice ([RC] open point 13).
11. **Paternity and other non-statutory leave defaults** — management decision.
12. **Retention periods** for income-tax, EPF/ESI and POSH records under the new Rules ([RC] open point 14).
13. **EPF/ESI rounding rules** under the 2026 Schemes (`coss.epf.rounding`, `coss.esi.rounding`; seed nearest rupee per component, SECONDARY_ONLY) and the absence-deduction divisor (`tenant.pay.lop_divisor`) — Payroll Compliance Officer with CA *(v3.1)*.

---

## Z.21 Phase addenda

### For P00
**FR-P00-V3-Z01 — Schemas and entity RLS.** Create schemas `hr`, `pay`, `ctl`; add `rls.enable_entity_rls()` and the `app.entity_ids` session setting; extend CI check `db:rls-catalogue` to require `entity_scope` on every `hr`/`pay`/`ctl` table with `legal_entity_id`. *Acceptance:* a user with entity grant A reads zero rows of entity B in all three schemas.

**FR-P00-V3-Z02 — Ports.** Register `WORKSPACE_PORT` (adapters `m365_graph`, `google_workspace` stub OFF, `manual_it_desk`) and `PAYROLL_EXCHANGE_PORT` (`generic_csv`) in `packages/domain/ports` with fake adapters; add both to the Appendix D §D.0.4 list. *Acceptance:* contract tests pass against fakes; Google adapter refuses calls while `ops.workspace.google.enabled` is OFF.

**FR-P00-V3-Z03 — Config kinds.** Register config kinds `payroll_rule_pack`, `leave_rule_pack`, `hours_rule_pack`, `authority_matrix`, `sod_rules`, `metric_definition` with JSON Schemas, validators (PT ₹2,500 cap; leave floor; outcome-metric ban) and NN-33 tiers. *Acceptance:* a PT slab summing above ₹2,500/year fails validation.

**FR-P00-V3-Z04 — Edit-log guard.** Extend the r.3(1) audit-trail guard (pgaudit + trigger-disable alert) to `pay` and `ctl`. *Acceptance:* `ALTER TABLE pay.run_lines DISABLE TRIGGER ALL` by any role raises a Critical alert and is blocked outside break-glass.

**FR-P00-V3-Z05 — Error and event registry.** Add §Z.17.2 events and §Z.17.3 codes to `packages/domain`. *Acceptance:* CI error-catalogue check passes.

### For P05
**FR-P05-V3-Z06 — Authority matrix integration.** Refunds, write-offs, payout releases, credit notes and fee-schedule approvals call `CtlService.request/assertApproved`; `fin.*` bundle limits are migrated into `ctl.authority_rules` with identical values (X-56). *Acceptance:* a refund of ₹30,000 by a `fin.operator` routes to `fin.approver`; self-approval returns `CTL_SELF_APPROVAL_BLOCKED`.

**FR-P05-V3-Z07 — Payroll journals in the ledger.** `pay.journal_batches` post balanced journals to `core.ledger_journals` with entity chart-of-accounts mapping and flow to the FR-P05-55 Tally/Zoho export. *Acceptance:* journal debits equal credits per currency; re-export of a locked period is blocked.

**FR-P05-V3-Z08 — Unified payee controls.** Neutral payout accounts (FR-P05-V2-17) adopt §Z.12.5 duplicate-account and out-of-band checks in addition to the 24-hour hold. *Acceptance:* a neutral payout account matching an employee's account raises `CTL_DUPLICATE_BANK_ACCOUNT`.

### For P11
**FR-P11-V3-Z09 — HR agents and prohibitions.** Register `hr_policy_assistant` (policy corpus only, citations) and HR uses of `document_extractor` and `analytics_narrator`; add red-team scenarios for candidate ranking, rating suggestions, emotion/productivity inference and tax-regime advice. *Acceptance:* all prohibited prompts are refused in the eval suite; HR data absent from few-shot stores (CI).

**FR-P11-V3-Z10 — Deterministic fallback.** Every HR AI feature has a manual path. *Acceptance:* with `ai.feature.hr_policy_assistant` OFF, policy search still returns the approved documents.

### For P14
**FR-P14-V3-Z11 — Controls and evidence.** Add NN-35/NN-36 controls and the §Z.18.4 collectors to `compliance/controls.yaml`; monthly payroll-controls evidence and weekly ghost-scan evidence. *Acceptance:* Compliance Cockpit shows each collector with owner and last result.

**FR-P14-V3-Z12 — Access reviews and SoD.** `AccessReviewCampaign` covers `apps/ops` roles (quarterly) and payroll/finance/IT/group roles (monthly) with SoD re-evaluation. *Acceptance:* an unactioned privileged item auto-revokes after 10 working days.

**FR-P14-V3-Z13 — HR go-live gate.** First live pay run is blocked until: SKU confirmed; DoFP approved by the Board; appointment-letter and offer templates legal-approved; workforce-measurement notice and employee privacy notice approved by the DPO; every parameter used by the run `VERIFIED` or acknowledged `SECONDARY_ONLY` with no `NOT_CONFIRMED`; a parallel run against a specialist provider or manual computation for at least one month with zero unexplained differences. *Acceptance:* gate checklist rendered with evidence links; missing item blocks `PAY-RUN-APPROVE` for the first live run.
