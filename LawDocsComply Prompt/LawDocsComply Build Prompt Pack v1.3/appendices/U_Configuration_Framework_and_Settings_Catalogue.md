# Appendix U — Configuration Framework and Settings Catalogue (binding)

> LawDocsComply Build Prompt Pack v1.1 · 25 October 2026 (v1.0 of the same date) · Owner: S12 (P02). Governs tiers, keys, scopes, merge rules, rule-pack and setting-pack catalogues, the canonical department catalogue and core settings. Module settings registered by each phase are compiled in §U.9. Precedence on tiers and keys: this appendix over phase files (master §precedence).

> **v1.1 changes (25 October 2026)**
> - §U.12 v1.1 core settings (regions, undo windows, onboarding, custom registers, simulation, sandbox, autonomy, kill switches, notification budget, engineering)
> - Department codes ESG, AIG, LEGL; rule-pack catalogue for P25–P27 and AI governance; configuration template library; who-can-change additions

---

## U.0 Purpose

LawDocsComply serves many regulators, entity families and organisation designs, and the rules change frequently. Configuration therefore carries most of the variability: **what** applies (rule packs), **how** work flows (workflow definitions, status sets, waiting-on policies), **who** does it (department tree, assignment rules), **how it looks** (terminology, menus, dashboards, branding) and **what is sold** (entitlements via P20). This appendix makes that variability safe (NN-28): every value has a tier, an owner, bounds, a merge rule and an audit trail.

---

## U.1 Key naming and definition schema

- Key: `<module>.<area>.<key>` in snake_case; module codes per conventions §5 (`cfg`, `cmp`, `wf`, `notify`, `ui`, `iam`, `dms`, `gov`, `pol`, `erm`, `ral`, `aud`, `ret`, `acc`, `dpc`, `tpr`, `hr`, `lab`, `grv`, `coop`, `ai`, `int`, `xpt`, `bil`, `mkp`, `sdc`, `web`, `hlp`, `rpt`, `eng`, `core`, `chg`, `cnt`, `tpl`, `pack`). `notify` and `ui` are cross-cutting prefixes owned by P02.
- New platform-only keys may prefix the area with `platform`; keys already registered by the owning phase keep their registered names (e.g., `bil.trial.default_days`, P20).
- Feature flags: `<module>.flag.<feature>` (boolean; G unless stated).
- Definition fields: P02 FR-P02-02 (tier, sub-class, type, default, bounds, allowed scopes, merge strategy, child direction, protective direction, instance pinning, sensitivity, owner role, citation required, fallback kind, UI metadata, lifecycle versions).
- Deprecation: a deprecated key must have `alias_of` or a migration; reads of deprecated keys log a warning; removal only after two releases (NN-11).

---

## U.2 Tiers

### U.2.1 Tier table

| Aspect | L — Locked | G — Governed | T — Tenant |
|---|---|---|---|
| Content | NN rules; statutory protections of third parties; audit/evidence integrity; security baselines; sealed-data rules; India residency; canonical state machines and status semantics | Legal/regulatory parameters (due-date rules, applicability predicates, statutory clocks, thresholds, penalty tables, tax parameters, retention floors); money, price and privilege controls; vendor integration settings | Operational values internal to the tenant |
| Sub-classes | — | `legal`, `elevated` (money, privilege, security), `platform_integration` | `bounded` (above a floor), `free` |
| Change path | Release + ADR + NN test + approvals (CTO + LDC Company Secretary) | Change request with maker ≠ checker, preview, citation (legal), effective date, impact | Immediate, audited; tenant may elevate to approval |
| Visible badge | 🔒 Locked | ⚖ Governed — "approval by …" | ✎ Tenant |

### U.2.2 Decision test (first "yes" wins)

| # | Question | Result |
|---|---|---|
| Q1 | Does the value implement an NN rule, protect a third party's statutory right (borrower, member, depositor, policyholder, investor, employee, complainant, data principal), preserve audit/evidence integrity, enforce a security baseline or a sealed-data rule? | **L** (or L floor + bounded margin) |
| Q2 | Does it move money, set a price/discount/refund/payout, change an authority limit or grant a privilege? | **G-elevated** |
| Q3 | Does it come from a statute, regulation, master direction, circular, standard (ICSI SS, ICAI SA/Ind AS), tax rule or professional rule, or affect a deadline, applicability, filing, disclosure or retention? | **G-legal** |
| Q4 | Does it depend on an external fact not yet confirmed (commencement, vendor capability, counsel opinion, regulator approval)? | **G** with flag OFF and fallback; if no runtime effect → documentation note only |
| Q5 | Is it operational, reversible and confined to the tenant's own people and processes? | **T** |

Tie-breaks: if in doubt choose the higher tier; split floor/margin values; values frozen into an instance (due-date rule version, meeting notice rules) are pinned at creation.

### U.2.3 Worked examples (LDC)

| Value | Tier | Basis |
|---|---|---|
| Maker ≠ checker | L | NN-05 |
| Audit ledger append-only; Correction Entries only | L | NN-02, D-02 |
| Canonical compliance status semantics | L | P02 FR-P02-40 |
| Statutory clocks never pause | L | P02 §4G |
| Sealed classes and their audiences | L | NN-13 |
| India data region for tenant data | L | NN-24 |
| AI cannot approve/sign/file/publish | L | NN-14 |
| Board meeting minimum and gap | G-legal | Companies Act s.173(1) |
| Board notice period | G-legal | s.173(3); SS-1 |
| Minutes circulation / entry timelines | G-legal | SS-1 [VERIFY paras] |
| AGM timeline | G-legal | s.96 |
| Grievance final-reply floor (RBI REs) | G-legal + L floor | RB-IOS 2026 [VERIFY clause] |
| CERT-In 6-hour reporting | G-legal + L floor | CERT-In Directions 28-Apr-2022 |
| DPDP breach intimation and report | G-legal + L floor | DPDP Rules 2025 r.7 [VERIFY] |
| Return due dates and frequencies | G-legal (returns kernel) | RBI returns directions [VERIFY current] |
| Evidence retention floor | G-legal, merge `longest` | s.128(5); RBI/SEBI record-keeping |
| State PT slabs, LWF | G-legal State rule packs | State Acts |
| Pricing, discounts, promo codes | G-elevated (platform) | D-21, NN-16 |
| Payroll approval threshold for four-eyes | G-elevated (tenant) | Internal control |
| Session idle timeout | G-elevated, tenant may shorten | Security baseline |
| Department/function names | T | R-086 |
| Reminder offsets | T bounded (`raise_only` vs floor) | Operational |
| Status labels and colours | T over L semantics | Comparability |
| Dashboard layouts (non-mandatory widgets) | T | Operational |
| Branding | T (contrast-validated) | NN-21 |

---

## U.3 Merge strategies and direction constraints

| Strategy | Used for | Rule |
|---|---|---|
| `most_specific` | Labels, templates, branding, assignment defaults | Deepest scope wins |
| `strictest` | Clocks, thresholds, limits, internal SLAs with floors | Most protective per `protective_direction` (`lower` = earlier/smaller wins; `higher` = larger wins) |
| `intersection` | Allowed channels, allowed IP ranges, enabled modules, allowed file types | Only what all layers allow |
| `union` | Block lists, mandatory disclosures, blackout dates, required evidence types, notification recipients for escalations | Everything any layer requires |
| `longest` | Retention, cooling-off, record-keeping | Longest applicable; legal hold overrides deletion |
| `additive` | Tags, custom fields, saved views, widgets | Combined; children hide but cannot delete parent items |

Direction constraints: `narrow_only` (quiet hours, allowed channels), `raise_only` (reminder lead days, retention, sample rates), `lower_only` (attempt caps, upload size limits). Validator compares against the parent's resolved value.

---

## U.4 Resolution order

1. L value. 2. Instance pin (if `instance_pinned` and an instance context exists). 3. Active emergency block. 4. Platform G rule-pack value for the regulatory profile and `as_of`. 5. Tenant G adaptation (within bounds; stricter only for protective values). 6. T value at the most specific scope (user → function → department → legal entity → tenant → group). 7. Definition default. 8. Declared fallback if the value is unapproved, overdue for review or depends on an unverified rule.

Each read returns `{value, source_scope, source_version, tier, fallback_applied}`.

---

## U.5 Rule-pack catalogue (seed)

| Domain | Packs (examples) | Owner → checker | Seed status |
|---|---|---|---|
| Calendar | `IN.calendar.frequency_rules`, `IN.calendar.fy`, `IN.calendar.holidays.national`, `IN.calendar.holidays.rbi`, `IN-<ST>.calendar.holidays`, `IFSC.calendar.holidays` | Content maker → content checker | National and RBI verified annually; State `SECONDARY_ONLY` until sourced |
| RBI applicability | `IN.rbi.nbfc.applicability` (layers BL/ML/UL/TL; types ICC, MFI, HFC, CIC, IDF, MGC, NOFHC, P2P, AA, Factor, SPD-equivalent where applicable), `IN.rbi.bank.applicability` (SCB, SFB, PB, RRB, LAB, foreign bank branches), `IN.rbi.ucb.tiers` (Tier 1–4), `IN.rbi.arc.applicability`, `IN.rbi.aifi.applicability` | Content → checker → publisher (permissive) | Requires S7/P15 verification |
| RBI returns | Returns kernel parameters (D-05) — frequencies, due rules, portal | Content → CFO-domain checker | [VERIFY current directions] |
| RBI prudential | `IN.rbi.nbfc.prudential`, `IN.rbi.ucb.prudential`, `IN.rbi.arc.prudential`, `IN.rbi.bank.basel` | Content → CRO-domain checker | P09 / Appendix H |
| SEBI | `IN.sebi.lodr.applicability`, `IN.sebi.lodr.disclosure_clocks`, `IN.sebi.pit`, `IN.sebi.mf`, `IN.sebi.aif`, `IN.sebi.reit_invit`, `IN.sebi.intermediaries`, `IN.sebi.cscrf` | Content → checker | P15 |
| IFSCA | `IFSC.ifsca.applicability` (≈ 33 entity types), `IFSC.ifsca.fcfu`, `IFSC.ifsca.fme`, `IFSC.ifsca.aml` | Content → checker | P15 |
| IRDAI | `IN.irdai.insurer`, `IN.irdai.intermediary` | Content → checker | P15 |
| MCA / ICSI | `IN.mca.company_class`, `IN.mca.board_meetings`, `IN.mca.agm`, `IN.mca.filings`, `IN.mca.llp`, `IN.icsi.ss1`, `IN.icsi.ss2` | Content → CS-domain checker | P06 |
| Co-operatives | `IN.coop.mscs` (Multi-State Co-operative Societies Act 2002 as amended 2023), `IN-<ST>.coop.<act>` (State Acts, election rules, audit, returns) | Content → checker | P16 / Appendix S |
| Privacy & cyber | `IN.privacy.dpdp`, `IN.privacy.it_spdi`, `IN.certin.incident`, `INTL.privacy.gdpr`, `US-CA.privacy.ccpa`, sector cyber packs (`IN.rbi.it_governance`, `IN.sebi.cscrf`, `IN.irdai.cyber`, `IFSC.ifsca.cyber`) | DPO-domain checker | P12 |
| Labour & payroll | `IN.labour.codes` (Wages, IR, SS, OSH), `IN.payroll.epf`, `.esi`, `.gratuity`, `.bonus`, `.leave`, `.maternity`, `.min_wage`, `.tds_salary`; `IN-<ST>.payroll.professional_tax`, `.lwf`, `.shops_establishments`; `IN.posh.act` | Payroll compliance officer → CS / counsel | P13 / Appendix T |
| Grievance | `IN.rbi.grievance` (RB-IOS 2026, internal ombudsman), `IN.sebi.scores`, `IN.irdai.grievance`, `IFSC.ifsca.grievance`, `IN-<ST>.coop.complaints` | GRO-domain checker | P14 |
| Tax | `IN.tax.gst` (rates, SAC, e-invoice threshold, return due dates), `IN.tax.tds` (Income-tax Act 2025 sections and forms [VERIFY]) | CFO → tax adviser | P11 / P20 |
| Penalties & savings | `IN.penalties.mca`, `IN.penalties.gst`, `IN.penalties.rbi_reference`, `IN.penalties.sebi_reference`, `IN.savings.time_standards` | CFO-domain checker | P20 |
| Risk scales | `IN.default.risk_scales`, `IN.default.kri_bands` | CRO-domain checker | P08 |
| Escalation defaults | `IN.default.escalation` | Content → checker | P04 |

Each pack: `rulepack.<jur>.<domain>.<name>@YYYY.N`; ZEN JDM content; typed params; citations (LR-IDs, instrument version, para); golden cases; fallback; review dates (P02 §4F).

---

## U.6 Canonical department catalogue and terminology defaults

### U.6.1 Department codes (platform G; Excel column `department` (v1.0: M) maps by name or code)

| Code | Canonical name (as in owner's template where present) | Typical families |
|---|---|---|
| `GOV` | Governance & Administration | All |
| `FIN` | Finance, Treasury and Accounts | All |
| `LEG` | Legal & Litigation | All |
| `IT` | IT | All |
| `OPS` | Operations & Management | All |
| `HR` | HR | All |
| `CMP` | Compliance | All |
| `RET` | Returns & Reporting | Regulated entities |
| `RSK` | Risk Management | Regulated entities |
| `SECR` | Secretarial (sub-department of GOV by default) | Companies, listed, NBFC, banks |
| `ISEC` | Information Security | Banks, NBFC-ML+, SEBI REs, insurers, IFSCA |
| `CRD` | Credit | Lenders |
| `COL` | Collections & Recovery | Lenders, ARCs |
| `IA` | Internal Audit | All with IA |
| `CSG` | Customer Service & Grievance | Customer-facing REs |
| `DPR` | Data Protection | All (DPDP) |
| `BUS` | Business / Sales & Distribution | All |
| `TRY` | Treasury & Investments | Banks, NBFC-ICC, insurers, AMCs, AIFs |
| `ACT` | Actuarial | Insurers, IFSCA IIOs |
| `FMI` | Fund Management / Investment | AMCs, AIFs, FMEs, REIT/InvIT managers |
| `MEM` | Membership & Society Affairs | Co-operatives |
| `ADM` | Administration & Facilities | All (optional) |

Families may restrict their Excel dropdown to a subset (Appendix E); tenants map their own tree to these codes (P02 FR-P02-43).

### U.6.2 Terminology defaults per family (examples; P02 FR-P02-45)

| Term key | Default | COOP-* | MCA-LLP | IFSCA branch units | Trusts/Societies (SRA 1860) |
|---|---|---|---|---|---|
| `term.board` | Board of Directors | Managing Committee / Board (per State Act) [VERIFY per State] | Designated Partners | Governing body / Principal Officer of the IFSC unit | Governing Body |
| `term.director` | Director | Committee member | Designated Partner | Principal Officer / Key personnel | Member of Governing Body |
| `term.shareholder` | Shareholder | Member | Partner | Parent entity | Member |
| `term.agm` | Annual General Meeting | Annual General Body Meeting | Meeting of partners (as per LLP agreement) | — | Annual General Meeting |
| `term.company_secretary` | Company Secretary | Secretary / Chief Executive | Designated Partner (compliance) | Compliance Officer | Secretary |
| `term.articles` | Articles of Association | By-laws | LLP Agreement | Constitutional documents of parent | Memorandum & Rules |

Statutory form names, section titles and regulator terms are L and never renamed.

---

## U.7 Setting-pack catalogue (seed; P02 §4N)

| Pack | Presets (summary) |
|---|---|
| `RBI-NBFC-BL` | Departments GOV, FIN, LEG, IT, OPS, HR, CMP, RET, RSK, CRD, COL, CSG, DPR; committees per applicability (Audit Committee where required, NRC/RMC as applicable) [VERIFY by size]; workflows: maker → checker → CCO; RBI + MCA + DPDP + Labour content packs suggested |
| `RBI-NBFC-ML` | BL + ISEC, IA; IT Strategy Committee, RMC, Audit Committee, NRC, IT Steering; CCO and CRO KMP roles; RBIA workflows; ICAAP not mandatory for ML (internal assessment template offered) [VERIFY] |
| `RBI-NBFC-UL` | ML + ICAAP workflows, stress-testing calendar, board-approved risk appetite cycle, independent CRO reporting [VERIFY current SBR text] |
| `RBI-NBFC-ICC` | Investment-focused: TRY department, investment committee, capital-market exposure and AIF investment limit widgets |
| `RBI-HFC`, `RBI-MFI`, `RBI-CIC`, `RBI-ARC` | Family-specific committees, returns calendars and dashboards (P15) |
| `RBI-SCB`, `RBI-SFB` | Banking departments, board committees (ACB, RMC, ITSC, Customer Service Committee, Fraud monitoring), Basel III dashboards, ICAAP annual cycle |
| `RBI-UCB-T1…T4` | Tiered governance (Board of Management where applicable [VERIFY]), UCB prudential widgets, SAF monitoring |
| `COOP-CCS-<State>` | Society terminology, MEM department, general body and managing-committee meetings, election calendar per State election authority, statutory audit by State-panel auditors, registrar returns |
| `COOP-MSCS` | Multi-State Co-operative Societies Act 2002 (amended 2023): Co-operative Election Authority, Central Registrar returns, co-operative information officer, co-operative ombudsman [VERIFY] |
| `COOP-GEN` | Generic society (housing, consumer, dairy, marketing) |
| `IFSCA-FCFU`, `IFSCA-FME`, `IFSCA-IBU` | IFSC calendar, IFSCA reporting, Principal Officer/Compliance Officer roles, parent-entity links |
| `SEBI-LISTED-MAIN`, `SEBI-LISTED-SME` | LODR committees (Audit, NRC, SRC, RMC for top-1000), disclosure clocks, PIT structured digital database, trading-window calendar |
| `SEBI-MF-AMC`, `SEBI-AIF-MANAGER`, `SEBI-REIT-INVIT-MANAGER`, `SEBI-INTERMEDIARY` | Family committees, CSCRF cyber packs, SEBI reporting calendars |
| `IRDAI-INSURER`, `IRDAI-BROKER`, `IRDAI-CORP-AGENT` | Actuarial (insurers), Principal Officer (intermediaries), IRDAI returns |
| `MCA-PVT`, `MCA-PUBLIC`, `MCA-SMALL`, `MCA-OPC`, `MCA-SEC8` | Companies Act calendars, registers, minimal departments |
| `MCA-LLP` | LLP terminology, Form 8/11 calendar, designated partners |
| `STANDALONE-HRMS-LABOUR` | People & Labour only; minimal compliance shell; labour packs by State |
| `STANDALONE-DATA-PRIVACY` | DPDP/GDPR/CCPA/IT Act packs, DPO dashboards |

Committee lists, thresholds and calendars in packs are proposals backed by rule packs; final applicability is determined by the rule engine from the tenant's attributes (P15) and shown with citations.

---

## U.8 Core settings catalogue (platform-owned keys)

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `core.audit.append_only` | L | true | — | — |
| `core.correction.dual_approval` | L | true | — | — |
| `core.correction.reason_min_chars` | L | 20 | — | — |
| `core.emergency_override.ratify_hours` | L | 24 | — | — |
| `core.data_region` | L | ap-south-1 (DR ap-south-2) | — | — |
| `core.timezone.default` | T | Asia/Kolkata | IANA zones | `ten_admin` |
| `core.fy.start_month` | G-legal (tenant) | 4 (April) | 1–12 (foreign entities) | `ten_admin` → `ten_cco` |
| `core.locale.default` | T | en-IN | supported locales | `ten_admin` |
| `core.date_format` | T | dd-MMM-yyyy | listed formats | `ten_admin` / user |
| `core.number_format` | T | Indian grouping | Indian / international | `ten_admin` / user |
| `iam.mfa.required_roles` | G-elevated | admin, KMP, payroll, IA, HR admin, all external | add only | `ten_admin` (narrow not allowed) |
| `iam.mfa.default_all_users` | G-elevated | true | tenant may not disable for privileged | `ten_admin` |
| `iam.session.idle_timeout_minutes` | G-elevated | 30 | 5–60 (lower_only) | `ten_admin` |
| `iam.session.absolute_hours` | G-elevated | 12 | 1–24 | `ten_admin` |
| `iam.ip_allowlist` | G-elevated | none | CIDR list | `ten_admin` + second admin |
| `iam.require_employee_link` | G (tenant) | true when HRMS enabled | — | `ten_admin` |
| `iam.privileged_role_two_person` | T | false | — | `ten_admin` |
| `iam.external_grant.max_days` | G | 90 | 1–90 | platform |
| `iam.leaver.deprovision_time` | T | 23:59 last working day | — | `ten_hr_admin` |
| `wf.tasks.assignment_policy` | T | hierarchy | hierarchy / department / open | `ten_admin` |
| `wf.approval.expiry_days` | T | 14 | 7–30 | `ten_admin` |
| `wf.approval.sla_working_days` | T | 2 | 1–10 | `ten_admin` |
| `wf.bulk_approvable_sources` | G (platform list) + T subset | leave, attendance, low-risk T content | subset only | `ten_admin` |
| `wf.delegation.max_days` | G | 90 | 1–90 | platform |
| `wf.waiting.default_chase_cadence` | T | P3D | P1D–P14D | `ten_admin` |
| `wf.waiting.max_chases` | T | 5 | 1–20 | `ten_admin` |
| `wf.waiting.statutory_warning_days` | T (raise_only vs 3) | 7 | 3–60 | `ten_cco` |
| `wf.escalation.l3_mandatory_for_statutory` | L | true | — | — |
| `wf.inbox.max_snoozes` | T | 3 | 1–5 | user |
| `wf.inbox.away_escalation_hours` | T | 8 (P1: 1) | 1–48 | `ten_admin` |
| `notify.quiet_hours` | T (user narrow_only) | 21:00–08:00 | — | `ten_admin` / user |
| `notify.digest.work_time` | T | 08:30 | — | user |
| `notify.digest.updates_time` | T | 20:30 IST | after scan | user |
| `notify.channels.p1` | T (intersection with platform) | in-app, push, email | + SMS/WhatsApp opt-in | `ten_admin` |
| `notify.dedupe_window_minutes` | G | 15 | 5–60 | platform |
| `ui.theme.default` | T | light | light / dark / high-contrast | `ten_admin` / user |
| `ui.density.default` | T | comfortable | comfortable / compact | user |
| `ui.single_key_shortcuts` | T (user) | false | — | user |
| `ui.explore_unlicensed_modules` | T | true | — | `ten_admin` |
| `ui.celebrations` | T | false | — | user |
| `cmp.reminders.default_offsets_days` | T (raise_only vs [3]) | [15, 7, 1] | 1–90 each | `ten_admin` / dept head |
| `cmp.window.open_lead_days` | T | 30 | 1–120 | `ten_admin` |
| `cmp.maker_attestation_text` | T (bounded: must include completeness + truth statement) | platform text | — | `ten_cco` |
| `cmp.high_risk.requires_stepup_check` | G (tenant) | true | — | `ten_cco` |
| `cmp.auditor_sampling.enabled` | T | false | — | `ten_internal_auditor` + `ten_cco` |
| `cmp.na.requires_cco_for_instruments` | T | high-risk instruments | list | `ten_cco` |
| `cmp.reopen.window_days` | T | 30 | 0–90 | `ten_cco` |
| `dms.upload.max_mb` | G (lower_only) | 100 | 1–500 | platform / `ten_admin` |
| `dms.upload.allowed_types` | G (intersection) | pdf, docx, xlsx, pptx, csv, jpg, png, tiff, msg, eml, zip, txt | — | platform / `ten_admin` |
| `dms.retention.floor_years` | G-legal (longest) | 8 | ≥ statutory | platform |
| `dms.share.external_link_days` | T | 7 | 1–30 | `ten_admin` |
| `dms.watermark.external_downloads` | T | true | — | `ten_admin` |
| `ai.enabled` | T | ON (if plan includes) | ON/OFF | `ten_admin` (aligned with P17) |
| `ai.sealed_classes_enabled` | G (tenant) | false | — | `ten_admin` + `ten_cco` |
| `ai.monthly_credit_cap` | G-elevated (plan) | per plan | — | P20 |
| `ai.user_opt_out_suggestions` | T (user) | false | — | user |
| `xpt.link_expiry_days` | T | 7 | 1–30 | `ten_admin` |
| `xpt.sensitive_scope_requires_checker` | L | true | — | — |
| `xpt.exit_window_days` | G (raise_only vs 30) | 90 | 30–365 | platform |
| `bil.trial.default_days` (canonical key, P20; the earlier name `bil.platform.trial_default_days` is retired, review R1) | G-elevated | 7 | 1–60 | `plt_super_admin` → `plt_finance` |
| `bil.trial.one_per_pan` | G | true | — | platform |
| `cfg.change_requests.expiry_days` | T | 14 | 7–30 | `ten_admin` |
| `cfg.legal.lead_time_hours` | G | 24 | ≥ 0 with urgent flag | platform |
| `cfg.packs.max_pin_days` | G | 90 | 0–180 | platform |
| `cfg.review.default_days` | G | 180 | 30–365 | platform |
| `cfg.review.secondary_only_days` | G | 90 | 30–180 | platform |
| `cfg.review.volatile_days` | G | 30 | 7–90 | platform |
| `cfg.t_undo_window_seconds` | T | 600 | 300–1800 | `ten_admin` |
| `cfg.bulk.max_rows` | G | 5000 | 100–20000 | platform |
| `cfg.custom_fields.max_per_object` | G-elevated | 100 | 10–200 | platform |
| `cfg.tenant_ack.escalation_working_days` | T | 5 | 1–15 | `ten_admin` |
| `cfg.sandbox.enabled` | T | true | — | `ten_admin` |
| `hlp.info_buttons.enabled` | T | true | — | `ten_admin` / user |
| `hlp.tours.auto_start` | T (user) | true for first login | — | user |
| `rpt.board_pack.watermark` | T | director name + date | — | `ten_kmp` (CS) |
| `rpt.dashboard.max_personal` | G | 5 | 1–10 | platform |

---

## U.9 Compiled module settings

*(Compiled by the pack lead from all streams' `_contrib/*_settings.md`.)*

### U.9.0 Department name → code alias map (binding for the importer, Excel column `department` (v1.0: M))

The Excel family templates (Appendix E) carry 53 department names. Every name resolves to one canonical code from §U.6.1 or to one of the twelve codes added here (X-10). The importer stores the code; the tenant sees its own label (P02 FR-P02-43).

**Codes added to §U.6.1:** `CLM` Claims · `KYC` KYC & AML · `ICP` Internal Committee (POSH; sealed class, NN-13) · `INV` Investor Relations & Services · `MKT` Marketing · `PRL` Payroll · `PRD` Product & Engineering · `SRV` Surveillance · `TAX` Tax · `TRS` Trusteeship & SR Management · `UND` Underwriting · `VAL` Valuation.

| Template name (column `department` (v1.0: M)) | Code | Template name (column `department` (v1.0: M)) | Code |
|---|---|---|---|
| Accounts Payable | FIN | Internal Committee (POSH) | ICP |
| Acquisition & Resolution | COL | Investment Team | FMI |
| Actuarial | ACT | Investments | TRY |
| Administration & Facilities | ADM | Investor Grievance | INV |
| Application Development | IT | Investor Relations | INV |
| Asset Management | FMI | Investor Services | INV |
| Audit | IA | KYC & AML | KYC |
| Billing & Receivables | FIN | Legal & Litigation | LEG |
| Business Continuity | RSK | Marketing | MKT |
| Business Operations | OPS | Member Services & Grievance | MEM |
| Claims | CLM | Membership & Elections | MEM |
| Claims Support | CLM | Operations & Management | OPS |
| Client Onboarding & KYC | KYC | Payroll | PRL |
| Collections & Recovery | COL | Policyholder Grievance | CSG |
| Compliance | CMP | Policyholder Servicing & Grievance | CSG |
| Credit | CRD | Privacy Office (DPO) | DPR |
| Credit & Recovery | CRD | Product & Engineering | PRD |
| Customer Service & Grievance | CSG | Returns & Reporting | RET |
| Finance, Treasury and Accounts | FIN | Risk Management | RSK |
| Fund Management & Investments | FMI | Sales & Distribution | BUS |
| Governance & Administration | GOV | Secretarial | SECR |
| HR | HR | Surveillance | SRV |
| IT | IT | Tax | TAX |
| IT Infrastructure | IT | Trusteeship & SR Management | TRS |
| Information Security | ISEC | Underwriting | UND |
| Internal Audit | IA | Valuation | VAL |
| Internal Audit & Inspection | IA | | |

A name that is not in this map is rejected with LDC-TPL error "unknown department" unless the tenant has registered it as a custom department mapped to a code (P02). The nine base names are present in every family template (NN-35).

### U.9.1 Module settings by stream

Settings below are registered in the P02 registry before use (NN-28). Tier: L Locked, G Governed (maker-checker, citation, effective date), T Tenant.

#### Settings — stream S11 (P00, P01, P24, App B, Q)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| core.audit.retention_years | G | 8 | ≥ 8 | plt_super_admin; tenant may increase | P00 |
| core.audit.anchor.time_ist | L | 00:10 | — | — | P00 |
| core.audit.anchor.tsa.enabled | G | false | — | plt_security_officer | P00 |
| core.correction.tenant_ack_mode | G | PRIOR (MASTER_DATA, DOCUMENT_VERSION) / POST | PRIOR\|POST | plt_super_admin with tenant agreement | P00 |
| core.correction.justification_min_chars | L | 50 | — | — | P00 |
| core.correction.escalation_working_days | T | 3 | 1–10 | ten_admin | P00 |
| core.break_glass.max_minutes | G | 240 | 30–480 | plt_security_officer | P00 |
| core.break_glass.two_person | G | true for SEALED/CREDENTIAL/HR/write | — | plt_security_officer | P00 |
| core.tenant.timezone | T | Asia/Kolkata | IANA | ten_admin | P00 |
| core.tenant.fiscal_year_start | T | 04-01 | month start | ten_admin | P00 |
| core.tenant.number_format | T | indian | indian\|international | ten_admin, user | P00 |
| dms.upload.max_mb | G (lower_only) | 100 | 1–500 | platform / ten_admin (aligned with §U core row, review R1) | P00 |
| dms.upload.allow_macro_office | T | false | — | ten_admin | P00 |
| dms.evidence.retention_years | G/T | 8 | ≥ 8 | ten_admin (increase) | P00 |
| migration.max_defect_rate | G | 0.005 | 0–0.02 | plt_super_admin | P00 |
| platform.provider_routing.nonprod | L | sandbox | — | — | P00 |
| iam.mfa.required_roles | G | privileged roles | add only | ten_admin | P01 |
| iam.mfa.maker_aal | T | aal2 | aal1–aal2 | ten_admin | P01 |
| iam.stepup.export_rows_threshold | T | 1000 | 100–100000 | ten_admin | P01 |
| iam.session.idle_minutes.professional | T | 15 | 5–30 | ten_admin | P01 |
| iam.session.absolute_hours.professional | T | 12 | 4–12 | ten_admin | P01 |
| iam.sso.enforce | T | false | — | ten_admin | P01 |
| iam.invitation.ttl_days | T | 14 | 1–30 | ten_admin | P01 |
| iam.delegation.max_days | T | 30 | 1–90 | ten_admin | P01 |
| iam.delivery_grant.tenant_maker_checker | T | false | — | ten_admin | P01 |
| iam.delivery_grant.lawdocs_sole_checker_allowed | L | false | — | — | P01 |
| iam.supervisor_grant.max_days | L | 90 | — | — | P01 |
| iam.supervisor_grant.default_pii_level | T | MASKED | MASKED\|UNMASK_ON_REQUEST | ten_cco | P01 |
| iam.supervisor_grant.anomaly_multiplier | T | 10 | 3–50 | ten_admin / CISO | P01 |
| iam.break_glass.tenant_prior_consent | T | false | — | ten_admin | P01 |
| iam.dormant.suspend_after_days | T | 90 | 30–365 | ten_admin | P01 |
| iam.onboarding.resume_days | G | 30 | 7–90 | plt_super_admin | P01 |
| iam.kyb.sources_order | G | MCA, GSTN, PAN, GLEIF, registers | — | plt_super_admin | P01 |
| iam.kyb.cache_hours | G | 24 | 1–168 | plt_super_admin | P01 |
| iam.kyb.mca.enabled | G | false until contract | — | plt_super_admin | P01 |
| bil.trial.default_days (alias of the P20 key; former P01 name `bil.trial.days` retired, review R1) | G | 7 | 1–60 | plt_super_admin + checker | P01/P20 |
| bil.trial.grace_days | G | 7 | 0–30 | plt_super_admin | P01 |
| bil.trial.card_required | G | false | — | plt_super_admin | P01 |
| bil.trial.one_per_org_months | G | 12 | 0–36 | plt_super_admin | P01 |
| eng.branch.max_age_days | G | 2 | 1–10 | CTO | P24 |
| eng.release.train_day_time | G | Tue 22:00 IST | — | release manager | P24 |
| eng.release.ring1_soak_hours | G | 24 | 4–168 | release manager | P24 |
| eng.notice.regulatory_impact_working_days | G | 5 | ≥ 5 | release manager | P24 |
| eng.api.deprecation_months | G | 6 | ≥ 6 | CTO | P24 |
| eng.vuln.sla.critical_hours | L | 72 | — | — | P24 |
| eng.vuln.sla.high_days | L | 7 | — | — | P24 |
| eng.vuln.sla.medium_days | L | 30 | — | — | P24 |
| eng.vuln.sla.low_days | L | 90 | — | — | P24 |
| eng.vuln.risk_acceptance_max_days | L | 90 | — | — | P24 |
| eng.backup.pitr_days | G | 35 | ≥ 35 | SRE | P24 |
| eng.restore_test.frequency_days | G | 7 | ≤ 7 | SRE | P24 |
| eng.dr.drill_months | G | 6 | ≤ 6 | CTO | P24 |
| eng.logs.retention_days | G | 400 | ≥ 180 | security | P24 |
| eng.incident.client_notice_hours | L | 2 | — | — | P24 |
| eng.bug_bounty.enabled | G (Board) | false | — | Board | P24 |
| eng.vapt.production_window.enabled | G | false | — | security lead + CAB | P24 |
| ten.release.early_access | T | false | — | ten_admin | P24 |
| vault.reveal.seconds | L | 30 | — | — | Q (P22) |
| vault.rbi_portal.client_only_default | G | true | — | plt_security_officer | Q (P22) |

#### Settings — stream S12 (P02, App A, C, D, U)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| core.audit.append_only | L | true | — | — | P00/P02 |
| core.correction.dual_approval | L | true | — | — | P02 |
| core.correction.reason_min_chars | L | 20 | — | — | P02 |
| core.emergency_override.ratify_hours | L | 24 | — | — | P02 |
| core.timezone.default | T | Asia/Kolkata | IANA | ten_admin | P02 |
| core.fy.start_month | G (tenant) | 4 | 1–12 | ten_admin → ten_cco | P02 |
| core.date_format | T | dd-MMM-yyyy | list | ten_admin/user | P02 |
| iam.session.idle_timeout_minutes | G-elevated | 30 | 5–60 lower_only | ten_admin | P01 |
| iam.mfa.required_roles | G-elevated | admin, KMP, payroll, IA, HR, external | add only | ten_admin | P01 |
| iam.require_employee_link | G (tenant) | true if HRMS | — | ten_admin | P01/P13 |
| iam.external_grant.max_days | G | 90 | 1–90 | platform | P01 |
| wf.tasks.assignment_policy | T | hierarchy | hierarchy/department/open | ten_admin | P04 |
| wf.approval.expiry_days | T | 14 | 7–30 | ten_admin | P04 |
| wf.approval.sla_working_days | T | 2 | 1–10 | ten_admin | P04 |
| wf.bulk_approvable_sources | G + T subset | leave, attendance, low-risk T content | subset | ten_admin | P04 |
| wf.delegation.max_days | G | 90 | 1–90 | platform | P02 |
| wf.waiting.default_chase_cadence | T | P3D | P1D–P14D | ten_admin | P02 |
| wf.waiting.max_chases | T | 5 | 1–20 | ten_admin | P02 |
| wf.waiting.statutory_warning_days | T raise_only vs 3 | 7 | 3–60 | ten_cco | P02 |
| wf.escalation.l3_mandatory_for_statutory | L | true | — | — | P02 |
| wf.inbox.max_snoozes | T | 3 | 1–5 | user | P04 |
| wf.inbox.away_escalation_hours | T | 8 (P1: 1) | 1–48 | ten_admin | P04 |
| notify.quiet_hours | T (user narrow_only) | 21:00–08:00 | — | ten_admin/user | P02 |
| notify.digest.work_time | T | 08:30 | — | user | P04 |
| notify.digest.updates_time | T | 20:30 IST | after scan | user | P05 |
| notify.dedupe_window_minutes | G | 15 | 5–60 | platform | P04 |
| ui.theme.default | T | light | light/dark/high-contrast | ten_admin/user | P02 |
| ui.single_key_shortcuts | T | false | — | user | P02 |
| ui.explore_unlicensed_modules | T | true | — | ten_admin | P02/P20 |
| cmp.reminders.default_offsets_days | T raise_only vs [3] | [15,7,1] | 1–90 | ten_admin/dept head | P04 |
| cmp.window.open_lead_days | T | 30 | 1–120 | ten_admin | P04 |
| cmp.high_risk.requires_stepup_check | G (tenant) | true | — | ten_cco | P04 |
| cmp.reopen.window_days | T | 30 | 0–90 | ten_cco | P04 |
| cfg.change_requests.expiry_days | T | 14 | 7–30 | ten_admin | P02 |
| cfg.legal.lead_time_hours | G | 24 | ≥0 (urgent flag) | platform | P02 |
| cfg.packs.max_pin_days | G | 90 | 0–180 | platform | P02 |
| cfg.review.default_days | G | 180 | 30–365 | platform | P02 |
| cfg.review.secondary_only_days | G | 90 | 30–180 | platform | P02 |
| cfg.review.volatile_days | G | 30 | 7–90 | platform | P02 |
| cfg.t_undo_window_seconds | T | 600 | 300–1800 | ten_admin | P02 |
| cfg.bulk.max_rows | G | 5000 | 100–20000 | platform | P02 |
| cfg.custom_fields.max_per_object | G-elevated | 100 | 10–200 | platform | P02 |
| cfg.tenant_ack.escalation_working_days | T | 5 | 1–15 | ten_admin | P02 |
| cfg.sandbox.enabled | T | true | — | ten_admin | P02 |
| rpt.dashboard.max_personal | G | 5 | 1–10 | platform | P02 |
| hlp.info_buttons.enabled | T | true | — | ten_admin/user | P23 |

#### Settings — stream S1 (P03–P05, App F)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| cnt.quality.reverify_months | G | 12 (High 6) | 3–24 | content lead | P03 |
| cnt.review.sla_days | G | 3 business days | 1–10 | content lead | P03 |
| cnt.release.publisher_must_differ | G | true | — | super admin | P03 |
| cnt.overlay.approval_mode | T | SINGLE_APPROVER | SINGLE/TWO_LEVEL | ten_admin | P03 |
| cnt.overlay.conflict_sla_days | T | 15 | 5–60 | ten_admin | P03 |
| cnt.overlay.allowed_fields | T | all permitted | K/authority/obligation_ref locked (L) | ten_admin | P03 |
| cnt.catalogue.removal_second_approver | T | required for Applicable | floor for High-risk | ten_admin | P03 |
| cnt.catalogue.auto_suggest_on_profile_change | T | true | — | ten_admin | P03 |
| cnt.duplicate_similarity_threshold | G | 0.92 | 0.80–0.99 | content lead | P03 |
| tpl.import.max_file_mb | G | 25 | 5–100 | super admin | P03 |
| tpl.import.max_rows | L | 2000 | — (Appendix E contract; LDC-TPL-009) | — (aligned with Appendix E, review R1) | P03 |
| tpl.import.dv_rows | G | 2000 | 345–20000 | super admin | P03 |
| tpl.deprecated_grace_days | G | 180 | 30–365 | super admin | P03 |
| tpl.workspace.max_export_age_days | T | 30 | 1–180 | ten_admin | P03/P04 |
| tpl.import.ai_enrichment | T | ON | ON/OFF | ten_admin / content lead | P03 |
| pack.<code>.enabled | G | IN ON; non-IN OFF | — | super admin + reviewer | P03 |
| cfg.terminology.<term> | T | canonical | ≤60 chars | ten_admin | P03 |
| cmp.schedule.horizon_months | G | 15 | 12–24 | super admin | P04 |
| cmp.window.default_open_days | T | 30 | 7–90 | ten_admin | P04 |
| cmp.internal_buffer_days.by_risk | T | H5 M3 L1 | 0–30 | ten_cco | P04 |
| cmp.immediate.default_hours | G | 24 | 1–72 | content lead | P04 |
| cmp.ongoing.attestation_frequency | T | QUARTERLY | MONTHLY–ANNUAL | ten_cco | P04 |
| cmp.review.high_risk_two_level | T | false | — | ten_cco | P04 |
| cmp.review.bulk_approve_enabled | T | OFF | ON only for content-flagged bulk_approvable checkpoints (L floor, NN-46) | ten_cco | P04 |
| cmp.review.rework_alert_count | T | 2 | 1–5 | ten_cco | P04 |
| cmp.evidence.required_for | T | HIGH, MEDIUM | must include HIGH | ten_cco | P04 |
| cmp.escalation.ladder | T | T-15/-7/-3/-1/T/+3/+7 | cannot remove T, T+3 | ten_cco | P04 |
| cmp.events.<type>.who_can_trigger | T | dept head, CCO, admin | — | ten_admin | P04 |
| cmp.events.<type>.requires_approval | T | false (true for some) | — | ten_admin | P04 |
| cmp.extension.approver_by_risk | T | L/M dept head, H CCO | — | ten_cco | P04 |
| cmp.waiver.board_threshold_risk | T | HIGH | — | ten_cco | P04 |
| cmp.score.weights | T | H3 M2 L1 | 1–10 | ten_cco | P04 |
| cmp.score.status_points | T | §4I | 0–1 | ten_cco | P04 |
| cmp.certificate.chain | T | DEPT→CCO→MD | — | ten_admin | P04 |
| cmp.fy_start_month | T | 4 | 1–12 | ten_admin | P04 |
| cmp.week_start_day | T | MONDAY | — | ten_admin | P04 |
| cal.external.providers_allowed | T | M365, GOOGLE, ICS | subset | ten_admin | P04 |
| cal.external.detail_level | T | own FULL; personal TITLE_ONLY | sealed MINIMAL (L) | ten_admin/user | P04 |
| notify.floors | G | §4N | locked | — | P04 |
| notify.channels.whatsapp.enabled | T | OFF | BSP contract | ten_admin | P04 |
| notify.channels.sms.enabled | T | OFF | DLT | ten_admin | P04 |
| notify.quiet_hours.default | T | 20:00–08:00 | — | user | P04 |
| notify.digest.default | T | daily 08:30 local (NN-27) | — | user | P04 |
| wf.tasks.assignment_rule | T | HIERARCHY | HIERARCHY/DEPARTMENT/OPEN | ten_admin | P04 |
| wf.schedules.max_active_per_user | T | 25 | 1–200 | ten_admin | P04 |
| chg.schedule.intraday_minutes | G | 30 / 60 | 15–240 | super admin | P05 |
| chg.schedule.reconciliation_time | G | 20:00 Asia/Kolkata | 18:00–23:00 | super admin | P05 |
| chg.reconciliation.lookback_days | G | 14 | 3–60 | super admin | P05 |
| chg.sla.triage_hours.immediate | G | 4 | 1–24 | content lead | P05 |
| chg.sla.publish_business_days | G | 1/3/10/20 | — | content lead | P05 |
| chg.radar.tenant_digest.enabled | T | ON | — | ten_admin/user | P05 |
| chg.radar.ai_gist.enabled | G | OFF | eval gate | super admin + content lead | P05 |
| chg.news.enabled | G | OFF | licensed feed | super admin | P05 |
| chg.enforcement.show_entity_names | G | ON | — | super admin (counsel) | P05 |
| chg.updates.ack_required_categories | T | REGULATORY_CHANGE, NEW_APPLICABLE_INSTRUMENT | floor | ten_admin | P05 |
| chg.updates.ack_escalation_days | T | 2,5 | ≤10 | ten_cco | P05 |
| chg.updates.department_targeting | T | ON | — | ten_admin | P05 |
| chg.updates.digest_time | T | 20:30 Asia/Kolkata (NN-27) | 18:00–23:59 or next-morning 07:00–10:00 | user | P05 |
| ai.studio.enabled_tenant | T | ON (plan-gated) | — | ten_admin | P05 |
| ai.studio.max_pages_per_run | G | 400 | 50–2000 | super admin | P05 |
| ai.studio.default_explanation_depth | T | STANDARD | STANDARD/DETAILED | ten_admin | P05 |
| ai.studio.split_subclauses | T | ON | L for platform | ten_admin | P05 |
| ai.studio.include_suggestive | T | ON | — | user | P05 |
| ai.studio.structure_confirm_threshold | G | 0.85 | 0.6–0.99 | content lead | P05 |
| ai.eval.promotion_thresholds | G | §1/FR-P05-102 | zero hallucinated citations (L) | super admin + content lead | P05 |

#### Settings — stream S2 (App E, templates)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| tpl.import.max_rows | L | 2000 | — | — | P03 |
| tpl.import.max_file_mb | G | 25 | 5–50 | plt_super_admin (maker-checker) | P03 |
| tpl.import.official_domains | G | list in App E §E.4.6 | add/remove | plt_content_checker | P03 |
| tpl.import.duplicate_similarity_threshold | G | 0.92 | 0.80–0.99 | plt_content_checker | P03 |
| tpl.import.high_risk_skew_info_pct | G | 70 | 50–95 | plt_content_checker | P03 |
| tpl.import.ai_lint.enabled | G | OFF | ON/OFF | plt_super_admin | P03/P17 |
| tpl.import.require_due_rule_before_publish | L | ON | — | — | P03 |
| tpl.import.verify_marker_blocks_publish | L | ON | — | — | P03 |
| tpl.template.info_sheet_password | G | LDC-TPL | text | plt_super_admin | P03 |
| tpl.template.deprecation_grace_months | G | 12 | 6–24 | plt_super_admin | P03 |
| cmp.content.tenant_publish_requires_checker | T | ON | floor ON for regulated entities | ten_admin | P03 |
| cmp.calendar.holiday_shift | T | next_business_day | previous / next / none | ten_admin | P04 |
| erm.compliance_risk.score_map | T | High 5, Medium 3, Low 1 | 1–5 | `ten_kmp` (CRO) | P08 |
| cnt.retention.source_files_years | G | 10 | 8–20 | plt_super_admin | P03 |

#### Settings — stream S3 (P06–P07)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `gov.notice.board_min_days` | G | 7 | ≥ statutory value | CS + checker | P06 |
| `gov.notice.shorter_notice_requires_id` | L | true | — | — | P06 |
| `gov.notes.min_days_before` | G | 7 | ≥ SS-1 value | CS | P06 |
| `gov.minutes.draft_circulation_days` | G | 15 | ≤ SS-1 value | CS | P06 |
| `gov.minutes.comment_days` | G | 7 | SS-1 value | CS | P06 |
| `gov.minutes.entry_days` | L | 30 | — | — | P06 |
| `gov.minutes.reminder_offsets_days` | T | [3, 0] | 0–10 | CS | P06 |
| `gov.circular.response_days` | G | 7 | 1–15 | CS | P06 |
| `gov.pack.watermark` | T | `name+email+timestamp` | — | CS | P06 |
| `gov.pack.interested_director_access` | G | `VIEW_WITH_BANNER` | `VIEW_WITH_BANNER`/`HIDE` | CS + chair | P06 |
| `gov.portal.download` | T | OFF | ON/OFF | CS | P06 |
| `gov.portal.session_timeout_min` | T | 15 | 5–60 | Admin | P06 |
| `gov.portal.upsi_step_up_mfa` | L | true | — | — | P06 |
| `gov.meeting.transcription` | T | OFF | requires consent capture | CS | P06 |
| `gov.vc.restricted_items` | G | [] | rule pack | Platform content | P06 |
| `gov.gm.vc_allowed` | G | per MCA circular (effective-dated) | — | Platform content | P06 |
| `gov.composition.warning_days` | T | 60 | 15–180 | CS | P06 |
| `gov.filings.reminder_offsets_days` | T | [15, 7, 3, 1] | — | CS | P06 |
| `gov.filings.show_additional_fee_meter` | T | ON | — | CS | P06 |
| `gov.lodr.materiality_thresholds` | G | per board policy | ≤ Reg 30(4) lower-of test | CS + Board resolution reference | P06 |
| `gov.lodr.disclosure_clock_alerts_min` | T | [15, 5] (board outcome) | — | CS | P06 |
| `gov.rpt.alert_pct` | T | [80, 100] | 50–100 | CS | P06 |
| `gov.pit.trading_window_reopen_hours` | G | 48 | ≥ 48 | Compliance officer | P06 |
| `gov.pit.preclearance_validity_trading_days` | G | 7 | ≤ 7 | Compliance officer | P06 |
| `gov.declarations.reminder_interval_days` | T | 3 | 1–7 | CS | P06 |
| `gov.mca_refresh.enabled` | T | OFF | requires adapter contract | Admin | P06 |
| `gov.annual_report.template_id` | T | platform default | tenant template | CS | P06 |
| `pol.review.default_frequency_months` | T | 12 | ≤ instrument-prescribed frequency | CCO | P07 |
| `pol.review.reminder_offsets_days` | T | [60, 30, 7] | — | CCO | P07 |
| `pol.review_sla_days` | T | 5 | 1–30 | CCO | P07 |
| `pol.route.<policy_type>` | T (G for regulatory-mandated end approver) | default route | must include required approver | Admin + CCO | P07 |
| `pol.signed_copy.required` | G | true for Board-approved policies | — | CCO + checker | P07 |
| `pol.scan_match.min_similarity` | T | 0.97 | 0.90–1.00 | CCO | P07 |
| `pol.redline.author_label` | L | "Vidhi AI (draft)" | — | — | P07 |
| `pol.attestation.reminder_days` | T | [3, 7, 14] | — | HR/CCO | P07 |
| `pol.attestation.new_joiner_days` | T | 15 | 1–60 | HR | P07 |
| `dms.checkout.max_hours` | T | 24 | 1–168 | Admin | P07 |
| `dms.autoclassify.auto_apply_threshold` | T | 0.95 (OFF until enabled) | 0.8–1.0 | Admin | P07 |
| `dms.share.external.enabled` | T | ON | — | Admin | P07 |
| `dms.share.default_expiry_days` | T | 14 | 1–365 | Admin | P07 |
| `dms.share.require_otp` | T | ON | cannot be OFF for CONFIDENTIAL | Admin | P07 |
| `dms.share.watermark` | T | ON | — | Admin | P07 |
| `dms.share.board_confidential_requires_cs` | L | true | — | — | P07 |
| `dms.esign.methods_allowed` | T | [AADHAAR_ESIGN, DSC, SIMPLE_ACK] | SIMPLE_ACK only for acknowledgement doc types | Admin | P07 |
| `dms.esign.excluded_types` | L | First Schedule list | — | — | P07 |
| `dms.estamp.enabled` | G | OFF | requires adapter + state matrix | Platform | P07 |
| `dms.embedded_editor.enabled` | G | OFF | requires ADR + fidelity tests | Platform | P07 |
| `dms.intake.max_zip_gb` | T | 10 | 1–50 | Admin | P07 |
| `dms.intake.duplicate_policy` | T | LINK_EXISTING | LINK_EXISTING / KEEP_BOTH | Admin | P07 |
| `dms.translation.target_default` | T | en | — | Admin | P07 |
| `dms.translation.reverse.enabled` | G | OFF | human review mandatory | Platform | P07 |
| `dms.ocr.handwriting.enabled` | T | ON | requires AI provider consent (NN-15) | Admin | P07 |
| `dms.macro_files.allowed_folders` | T | [] | — | Admin + CISO | P07 |
| `dms.retention.<class>.years` | G | floor per rule pack | ≥ floor | CCO + checker | P07 |
| `dms.email_in.enabled` | T | ON | — | Admin | P07 |

#### Settings — stream S4 (P08–P09, App H)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| erm.framework.scale_size | T | 5 | 3–6 | CRO (maker-checker) | P08 |
| erm.framework.impact_aggregation | T | MAX | MAX/WEIGHTED | CRO | P08 |
| erm.framework.severity_bands | T | 1–4/5–9/10–15/16–25 | monotonic | CRO | P08 |
| erm.taxonomy.level1 | L | pack-defined | — | Platform content | P08 |
| erm.taxonomy.level2_3 | T | pack seed | retire not delete | CRO | P08 |
| erm.residual.control_factor_table | T | FR-P08-08 | needs tested control | CRO | P08 |
| erm.residual.override_requires_approval | G | true | true | — | P08 |
| erm.ras.levels | T | appetite/tolerance/limit | limit ≥ regulatory floor | Board via workflow | P08 |
| erm.ras.review_cycle_months | T | 12 | 6–24 | CRO | P08 |
| erm.ras.reminder_days | T | 60,30,7 | — | CRO | P08 |
| erm.ras.concurrence_roles | T | CFO, CCO | KMP list | ten_admin | P08 |
| erm.rcsa.cadence_default | T | ANNUAL | QUARTERLY–BIENNIAL | CRO | P08 |
| erm.rcsa.cadence_high_residual | T | SEMI_ANNUAL | ≤ ANNUAL | CRO | P08 |
| erm.rcsa.self_effective_requires_evidence | G | true | true | — | P08 |
| erm.kri.plan_sla_wd | T | 5 | 1–15 | CRO | P08 |
| erm.kri.cro_review_sla_wd | T | 5 | 1–15 | CRO | P08 |
| erm.kri.cure_rule_default | T | 1 (3 daily) | 1–6 | CRO | P08 |
| erm.kri.acceptance_max_months | G | 6 | ≤ 6 | — | P08 |
| erm.kri.personal_threshold_direction | L | tighter_only | — | — | P08 |
| erm.loss.capture_sla_wd | T | 5 | 1–30 | ORM lead | P08 |
| erm.loss.reporting_threshold_inr | T | 0 | ≥ 0 | ORM lead | P08 |
| erm.loss.three_dates_required | G | true | true | — | P08 |
| erm.acceptance.authority_matrix | T | High→CRO; Critical→RMC | regulatory limits not acceptable | Board | P08 |
| erm.acceptance.max_months | T | 12 | ≤ 12 | Board | P08 |
| erm.pack.freeze_days_before | T | 7 | 2–21 | CS | P08 |
| erm.pack.require_certified_regulatory_metrics | G | true | indicative-with-reason only | — | P08 |
| erm.emerging.digest_frequency | T | QUARTERLY | MONTHLY–ANNUAL | CRO | P08 |
| erm.feed.reconciliation_time | T | 07:00 IST | — | Integration admin | P08 |
| erm.model_risk.rbi_2026_guidance.enabled | G | OFF | ON after final | Platform content | P08 |
| erm.disclosure.bank_pillar3.enabled | G | OFF | ON after template verification | Platform content | P08 |
| erm.dashboard.template_change_requires_approval | G | true | — | — | P08 |
| erm.quick_rcsa.enabled | T | true (CORP/LLP/COOP) | — | ten_admin | P08 |
| pack.sebi_listed.rmc_scope | G | top-1000 + HVDLE [VERIFY] | — | Platform content | P08 |
| ral.compute_mode.<family> | T | LDC_COMPUTED / FX_SOURCED | enum | CFO + CRO | P09 |
| ral.capital.profile | G | resolved | override CCO+CFO with reason | — | P09 |
| ral.capital.board_buffer_bps | T | CRAR 200, T1 100 | ≥ 0 | Board via RAS | P09 |
| ral.capital.red_band_bps | T | 100 | 25–300 | CRO | P09 |
| ral.capital.bl_leverage_alert | T | 6.5 | < 7 | CRO | P09 |
| ral.capital.shadow_frequency | T | WEEKLY (LDC) / DAILY (FX) | D/W/M | CFO | P09 |
| ral.dq.tb_tolerance_inr | T | 100000 | ≥ 0 | Data steward | P09 |
| ral.dq.unclassified_ead_max_pct | G | 0.1 | ≤ 0.1 | — | P09 |
| ral.alm.early_warning_pct | T | 80 | 50–95 | ALCO | P09 |
| ral.alm.lcr_internal_floor_pct | T | 110 | ≥ 100 | ALCO | P09 |
| ral.alm.sls_limits | L | 10/10/20 | — | Rule pack | P09 |
| ral.alm.behavioural_requires_approval | G | true | — | — | P09 |
| ral.concentration.early_warning_pct | T | 90 | 50–99 | CRO | P09 |
| ral.stress.fx_mode | G | CONSUME_ONLY | CONSUME_ONLY/LOCAL_RUN/REMOTE_RUN | Platform | P09 |
| ral.stress.max_horizon_quarters | T | 12 | 1–20 | CRO | P09 |
| ral.stress.approved_immutable | L | true | — | — | P09 |
| ral.icaap.host | T | LDC (non-Finbyx & LDC modes) / FINBYX (EMBEDDED) | LDC/FINBYX | CRO + CFO | P09 |
| ral.icaap.cycle | T | ANNUAL (31 Mar) | — | Board | P09 |
| ral.icaap.oprisk_proxy | T | 15% of 3-yr avg positive gross income | labelled internal | CRO | P09 |
| ral.icaap.timers_days_before_board | T | 45/20/14/7 | — | CS | P09 |
| ral.pca.proximity_bps | T | 150 | 50–300 | CRO | P09 |
| ral.pca.forecast_horizon | T | NEXT_FY_END | — | CRO | P09 |
| ral.bank.enabled | G | OFF until bank pack verified | — | Platform content | P09 |
| ral.bank.oprisk_2027.enabled | G | OFF (parallel from 1 Oct 2026 REC) | — | Platform content | P09 |
| ral.dashboard.personal_threshold_direction | L | tighter_only | — | — | P09 |
| ral.export.watermark | T | ON | — | ten_admin | P09 |

#### Settings — stream S5 (P10–P11, App I–J)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `aud.host.mode` | G | `LDC_NATIVE` (or `HYBRID` when Finbyx linked) | `LDC_NATIVE`, `FINBYX_HOSTED`, `HYBRID` + per-type map | ten_admin + HIA (maker-checker) | P10 |
| `aud.universe.change_task_sla_days` | T | 1 | 1–10 | HIA | P10 |
| `aud.universe.policy_max_interval_days.<unit_type>` | T | low 1095, medium 730, high 365 | must exist per unit type (floor) | HIA (ACB approval via methodology) | P10 |
| `aud.risk.scale` | T | 1–5; H ≥ 4, M 2.5–3.99, L < 2.5 | level + trend + basis mandatory | HIA | P10 |
| `aud.risk.iaf_parameters_locked` | L | true for RBIA tenants | — | — | P10 |
| `aud.plan.matrix_priority_order` | L | IAF para 32 order (RBIA tenants) | tie-breakers T | — | P10 |
| `aud.plan.approval_chain` | G | HIA → MD&CEO (info) → ACB | ACB/Board approval floor | ten_admin + ACB | P10 |
| `aud.engagement.timers.*` | T | as §5.1 | ≥ 1 working day each | HIA | P10 |
| `aud.independence.cooling_months` | T | 12 | 6–36 | HIA | P10 |
| `aud.workpaper.review_levels` | T | 2 (+HIA for high-risk) | ≥ 2 (floor) | HIA | P10 |
| `aud.workpaper.assembly_days` | T | 60 (statutory style), 45 (secretarial) | within standard | HIA | P10 |
| `aud.sampling.default_confidence` | T | 95% | 80–99% | HIA | P10 |
| `aud.finding.rating_scale` | T | Critical/High/Medium/Low | High/Medium pending always to ACB (floor) | HIA | P10 |
| `aud.finding.sla_days.<rating>` | T | 15/30/90/180 | tighter regulatory date wins | HIA | P10 |
| `aud.finding.response_window_wd` | T | 15 | 5–30 | HIA | P10 |
| `aud.finding.max_extensions_before_acb` | T | 1 (High/Critical) | ≥ 0; second always ACB (floor) | HIA | P10 |
| `aud.finding.repeat_lookback_months` | T | 24 | 12–60 | HIA | P10 |
| `aud.risk_acceptance.max_months` | T | 12 | 1–12 | ACB | P10 |
| `aud.atr.ageing_buckets` | T | 0–30, 31–90, 91–180, >180 | — | HIA | P10 |
| `aud.vapt.cadence_months` | L/T | VA 6, PT 12 (L for ML+ NBFC critical systems) | — | CISO | P10 |
| `aud.vapt.sla_days.<sev>` | T | 15/30/90/180 | — | CISO | P10 |
| `aud.is_audit.before_statutory_warning` | T | on | warning only | HIA | P10 |
| `aud.statutory.sa_mode_small_nd` | T | optional-with-checks | SA para 3 | CFO | P10 |
| `aud.statutory.dnbs10_reminders` | T | T−3, T−1, T | due rule L | CFO | P10 |
| `aud.statutory.branch_coverage_min_pct` | T | 15 | ≥ 15 (floor) | CFO | P10 |
| `aud.secretarial.tenure_alert_months` | T | 6 | 1–12 | CS | P10 |
| `aud.secretarial.group_conflict_check` | L | on for listed tenants | — | — | P10 |
| `aud.external.export_row_cap` | T | 50,000 | ≤ 200,000 | CCO | P10 |
| `aud.ai.drafting.enabled` | T | off | requires P17 | ten_admin | P10 |
| `aud.ai.special_investigation.enabled` | T | off | per engagement HIA override | HIA | P10 |
| `aud.acb_pack.lead_wd` | T | 10 | 3–20 | CS | P10 |
| `ret.kernel.version` | G | latest verified | opt-in upgrade with preview | ten_admin + CCO | P11 |
| `ret.host.mode` | G | `LDC_NATIVE`; `FINBYX_MIRROR` for Finbyx families | per return family | CCO | P11 |
| `ret.freeze_lead_days` | T | 3 | 0–15 | Head of reporting | P11 |
| `ret.generate_lead_days` | T | 5 | 1–15 | Head of reporting | P11 |
| `ret.alert_stages` | T | T−7, T−3, T−1, breach | breach alert locked | CCO | P11 |
| `ret.escalation.ceo_after_wd` | T | 2 | 1–5 | CCO | P11 |
| `ret.holiday_calendar` | T | RBI Mumbai + registered-office State | add tenant calendars | ten_admin | P11 |
| `ret.tolerance.rounding_unit` | L | template unit | — | — | P11 |
| `ret.reasonableness.pct.<element>` | T | 25% | 1–200% | Head of reporting | P11 |
| `ret.revision.materiality` | T | any prudential-ratio cell or ≥ ₹1 crore | — | CCO | P11 |
| `ret.approval_matrix.<family>` | G | Appendix I §I.9 defaults | SoD floors | ten_admin + CCO | P11 |
| `ret.webform.record_cap` | L | 2,000 (CIMS) [VERIFY] | — | — | P11 |
| `ret.cic.enabled` | T | off (on when `cic_member[]` set) | — | CCO | P11 |
| `ret.cic.cycles` | L | W1, W2, W3, ME (+ DL by agreement) | from 1 Jul 2026 | — | P11 |
| `ret.cic.transport` | T | `TENANT_HOST` | `TENANT_HOST`, `LDC_AGENT` | CISO | P11 |
| `ret.gst.itc_option` | G (annual lock) | proportionate | proportionate / 50% (banks/FIs/NBFCs) | CFO | P11 |
| `ret.gst.einvoice.enabled` | T | off for financial institutions | on only if not exempt | CFO | P11 |
| `ret.tds.regime_cutover` | L | 1 Apr 2026 (ITA25) | — | — | P11 |
| `ret.mca.xbrl.enabled` | T | off; on when triggers met and not NBFC/bank | — | CS | P11 |
| `acc.framework.override` | G | engine decision | CFO + auditor note | CFO | P11 |
| `acc.rounding.unit` | T | by Schedule III turnover band | — | CFO | P11 |
| `ret.ai.mapping_suggestions` | T | on | — | ten_admin | P11 |
| `ret.ai.prep_runbook.schedule` | T | off | cron | Head of reporting | P11 |
| `ret.share_status_with_ops_hub` | T | off | metadata only if on (Ecosystem Spec) | ten_admin | P11 |
| `ret.tally.agent.allowed` | T | off | loopback enforced | CISO | P11 |

#### Settings — stream S6 (P12–P14, App T)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `dpc.law_packs.enabled` | T (choice) / G (pack content) | derived from entity profile | only published packs | `ten_admin` + DPO (checker) | P12 |
| `dpc.consent.mode` | T | `OFF` | OFF / LEDGER_ONLY / FULL_CAPTURE | DPO | P12 |
| `dpc.consent_manager.integration.enabled` | G | OFF | — | `plt_super_admin` after verification | P12 |
| `dpc.rights.clock.<law>.<type>` | L (floor) + T (internal target ≤ floor) | from rule pack | internal target cannot exceed statutory window | DPO | P12 |
| `dpc.rights.fulfilment_store` | T | `NONE` | NONE / TENANT_VAULT | DPO | P12 |
| `dpc.rights.reopen_window_days` | T | 30 | 0–90 | DPO | P12 |
| `dpc.incident.dpb_initial_target_hours` | T | 24 | 1–72 | DPO | P12 |
| `dpc.incident.escalation_points` | T | [0.5, 0.75, 0.9] | ascending, ≤ 0.95 | CISO | P12 |
| `dpc.incident.severity_matrix` | T | 4×4 default | — | CISO + CRO | P12 |
| `dpc.incident_clocks` | G | per law packs | — | `plt_content_publisher` | P12 |
| `dpc.asset.criticality` | T | CIA max rule | — | CISO | P12 |
| `dpc.vapt.sla_days.{critical,high,medium,low}` | T | 15/30/60/90 | cannot exceed pack floors where a pack sets them | CISO | P12 |
| `dpc.control_test.default_frequency` | T | per control | — | CISO | P12 |
| `dpc.dpia.review_months` | T | 12 | 1–24 (SDF: max 12, Locked) | DPO | P12 |
| `dpc.transfer.restricted_countries` | G | [] | from notifications | `plt_content_publisher` | P12 |
| `tpr.tiering.weights` | T | default model | sum = 100 | CRO | P12 |
| `tpr.review.frequency_months.tier{1..4}` | T | 6/12/12/24 | material financial outsourcing ≤ 12 (para 38) | CRO | P12 |
| `tpr.board_review.frequency_months` | L for NBFC (6) / T otherwise | 6 | — | — | P12 |
| `tpr.vendor_portal.enabled` | T | ON | — | `ten_admin` | P12 |
| `dpc.ai_inventory.enabled` | T | ON | — | `ten_admin` | P12 |
| `hr.org.default_structure` | T | by entity family | — | `ten_hr_admin` | P13 |
| `hr.attendance.methods` | T | [web] | web, pwa_geo, ip_attest, device_import, supervisor | `ten_hr_admin` after monitoring notice published (NN-25) | P13 |
| `hr.attendance.geo.enabled` | T | OFF | requires published notice + DPIA screening (P12) | `ten_hr_admin` + DPO | P13 |
| `hr.leave.policy.<code>` | T | template | ≥ statutory floor (validator) | `ten_hr_admin` | P13 |
| `hr.leave.mandatory_block_days` | T | 10 | 5–15 | CRO | P13 |
| `hr.leave.approval_escalation_days` | T | 2 | 1–10 | `ten_hr_admin` | P13 |
| `hr.payroll.cutoff_day` | T | 25 | 15–31 | Payroll checker | P13 |
| `hr.payroll.bank_detail_hold_days` | T | 5 | 0–10 | CFO | P13 |
| `hr.payroll.three_actor_release` | L | ON | — | — | P13 |
| `hr.payroll.rule_packs` | G | latest published per State | pinned per run | `plt_content_publisher` (content); tenant adopts version (T) | P13 |
| `hr.payout.razorpayx.enabled` | G | OFF | — | super admin after contract | P13 |
| `hr.workspace.mode` | T | OFF | OFF / NOTIFY_IT / PROVISION | `ten_admin` | P13 |
| `hr.leaver.revoke_minutes` | T | 15 | 1–240 | `ten_admin` | P13 |
| `hr.recruitment.candidate_retention_months` | T | 6 | 1–24 | DPO | P13 |
| `lab.posh.ic.term_years` | L | 3 (max) | ≤ 3 | — | P13 |
| `lab.posh.inquiry_days` | L | 90 | — | — | P13 |
| `lab.grc.enabled_threshold_workers` | G | 20 | per Code | content | P13 |
| `hr.kri.share_with_ecosystem` | T | OFF | aggregates only | `ten_admin` + DPO | P13 |
| `grv.ladder` | G | by entity family | Locked steps cannot be removed | `plt_content_publisher`; tenant adopts | P14 |
| `grv.internal_targets.<step>` | T | e.g., GRO 15 days | ≤ regulatory window | CCO | P14 |
| `grv.ack.target_hours` | T | 24 | ≤ regulatory ack window (IRDAI "immediately" → system auto-ack) | CCO | P14 |
| `grv.escalation_points` | T | [0.5, 0.75, 0.9] | — | CCO | P14 |
| `grv.reopen_window_days` | T | 30 | 0–90 | CCO | P14 |
| `grv.io.required` | L (derived) | from entity profile & thresholds | — | — | P14 |
| `grv.channels.enabled` | T | web, email | web, email, whatsapp, phone, branch, api | `ten_admin` | P14 |
| `grv.widget.languages` | T | en, hi | Eighth Schedule + UN languages for translation | `ten_admin` | P14 |
| `grv.dedupe.window_days` | T | 30 | 1–90 | CCO | P14 |
| `grv.survey.enabled` | T | ON | — | CCO | P14 |
| `grv.vidhi.draft_replies` | T | ON | human send always required | CCO | P14 |
| `grv.display_attestation.frequency_months` | T | 3 | 1–12 | CCO | P14 |
| `grv.equator_option.enabled` | T | OFF | explicit consent flow only | `ten_admin` + Legal | P14 |

#### Settings — stream S7 (P15–P16, App G, S)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| pack.profile.attestation_interval_days | T | 90 | 30–90 | ten_cco | P15 |
| pack.profile.stale_after_days | G | 120 | 90–180 | plt_content_checker | P15 |
| pack.change.impact_due_days | T | 15 | 5–30 | ten_cco | P15 |
| pack.change.board_noting_required | T | true (layer/tier) | — | ten_admin | P15 |
| pack.change.approvers | T | CCO + CFO/CS | ≥ 2 distinct | ten_admin | P15 |
| pack.overlay.narrow_locked_second_approver | L | required | — | — | P15 |
| pack.overlay.broaden_allowed | T | true | — | ten_cco | P15 |
| pack.exemption.board_approval_material | T | true | — | ten_admin | P15 |
| pack.exemption.expiry_warning_days | T | 30 | 7–90 | ten_cco | P15 |
| pack.primary_regulator | T | from family | memberships | ten_cco | P15 |
| pack.vocabulary_pack | T | from family | catalogue | ten_admin | P15 |
| pack.updates.auto_accept_non_material | T | false | — | ten_cco | P15 |
| pack.investment.arbitrage_monitor_enabled | G | false | board policy + legal opinion evidence | ten_cco + CFO | P15 |
| pack.arc.clock_warning_days | T | [30,15,7] | tighten only | ten_cco | P15 |
| pack.listed.disclosure_warning_minutes | T | 15 | tighten only | ten_kmp (CS) | P15 |
| pack.jurisdiction.enabled | G | ["IN"] | PUBLISHED packs only | plt_content_publisher + ten_admin | P15 |
| pack.parameter.* | L | per instrument | — | content versioning | P15 |
| rules.unverified_as_advisory | L | true | — | — | P15 (App. G) |
| coop.sor.members | G | FINBYX (CCS on Finbyx) else LDC | FINBYX/LDC/EXTERNAL_LOS | ten_admin + chairperson | P16 |
| coop.act_pack | L | from society master | published packs | content | P16 |
| coop.byelaw.layer_enabled | T | true | — | secretary + chair | P16 |
| coop.agm.escalation_months | T | [4,5] | tighten only | secretary | P16 |
| coop.clock.warning_days | T | [60,30,7] | tighten only | secretary | P16 |
| coop.gbm.virtual_allowed | G | false | citation required | chair + content check | P16 |
| coop.internal_eballot.enabled | T | false | bye-law permits | chair | P16 |
| coop.member_portal.enabled | T | false | — | ten_admin | P16 |
| coop.languages | T | [en, hi] (+mr for MH) | catalogue | ten_admin | P16 |
| coop.notice.channels | T | [email, sms, notice_board] | statutory minimum | secretary | P16 |
| coop.disqualification.alert_days | T | 30 | 7–90 | secretary | P16 |
| coop.deposit_exception.board_agenda_auto | L | true | — | — | P16 |
| coop.guardrails.* | L | on | — | — | P16 |

#### Settings — stream S8 (P17–P19, App K–M)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `ai.enabled` | T | ON (if plan includes) | ON/OFF | `ten_admin` | P17 |
| `ai.skills.enabled` | T | plan set | subset of plan | `ten_admin` | P17 |
| `ai.plan.auto_approve_read_only` | T | true | bool | `ten_admin` | P17 |
| `ai.approval.expiry_days` | T | 7 | 1–30 | `ten_admin` | P17 |
| `ai.approval.step_up_threshold_records` | T | 50 | 1–500 (only lower) | `ten_admin` | P17 |
| `ai.memory.auto_learn` | T | false | bool | `ten_admin` | P17 |
| `ai.log.content_retention_days` | T | 365 | 30–2920 | `ten_admin` | P17 |
| `ai.routing.india_only_all_classes` | T | true for RE families, false otherwise | bool (can only make stricter than platform) | `ten_admin` | P17 |
| `ai.routing.policy` | G | seed table FR-P17-34 | — | `plt_super_admin` + `plt_security_officer` | P17 |
| `ai.routing.cross_border_basis` | G (tenant-scoped) | empty | recorded basis + DPO approval | `ten_admin` + tenant DPO, platform checker | P17 |
| `ai.sealed_allow_list` | G | empty | skill ids | platform + tenant DPO | P17 |
| `ai.run.max_steps` | G | 25 | 5–60 | platform | P17 |
| `ai.run.interactive_timeout_min` | T | 30 | 5–120 | `ten_admin` | P17 |
| `ai.typecopy.low_confidence_threshold` | G | 0.85 | 0.60–0.95 | platform | P17 |
| `ai.meeting.raw_audio_retention_days` | T | 30 | 0–365 | `ten_admin` | P17 |
| `ai.notebook.web_sources.enabled` | T | false | bool | `ten_admin` | P17 |
| `ai.studio.audio_overview.enabled` | G→T | OFF | flag | platform enables, tenant opts in | P17 |
| `ai.marketplace_suggestions.enabled` | T | ON | bool | `ten_admin` | P17 |
| `ai.budget.tenant_monthly_credits` | T | plan allowance | 0–plan + top-ups | `ten_admin` | P17 |
| `ai.budget.overage_cap_credits` | T | 0 | 0–(contract) | `ten_admin` | P17 |
| `ai.schedule.max_active_per_user` | G | 20 | 1–200 | platform | P17 |
| `ai.schedule.pause_after_failures` | T | 3 | 1–10 | `ten_admin` | P17 |
| `ai.provider.jio.enabled` | G | OFF | flag | platform after contract | P17 |
| `ai.supervisor_view.enabled` | T | OFF | flag | `ten_admin` | P17 |
| `ai.disclaimer.regulatory_footer` | G | text in FR-P17-08 | claims register | platform | P17 |
| `bil.ai_credits.retainer_billing` | G/T | tenant | tenant / retainer | P20 | P17 |
| `int.webhooks.max_subscriptions` | G | 25 per tenant | 1–200 | platform | P18 |
| `int.webhooks.default_data_class_max` | G | INTERNAL | ≤ CONFIDENTIAL with CISO approval | platform / tenant CISO | P18 |
| `int.webhooks.retry_hours` | L | 72 | — | locked (Spec §3.4) | P18 |
| `int.idempotency.retention_hours` | L | 24 (168 for billing) | — | locked | P18 |
| `int.rate_limits.profile` | G | per client type | — | platform | P18 |
| `int.clients.secret_rotation_days` | G | 90 | 30–90 | platform | P18 |
| `int.clients.production_requires_admin_approval` | L | true | — | locked | P18 |
| `int.dlq.replay_requires_checker` | L | true | — | locked (NN-05) | P18 |
| `int.calendar.default_mode` | T | ICS (no suite) / NATIVE (suite connected) | enum | `ten_admin` | P18 |
| `int.calendar.write_to_primary` | T | false | bool | `ten_admin` (users may opt in if allowed) | P18 |
| `int.calendar.privacy_mode_default` | T | false | bool | `ten_admin` | P18 |
| `int.calendar.reminder_lead_times` | T | [7d, 1d, 2h] | up to 5 values | user | P18 |
| `int.ics.token_rotation_days` | T | 180 | 30–365 | `ten_admin` | P18 |
| `int.onboarding.lookup_providers` | G | ordered list | approved providers | platform | P18 |
| `int.onboarding.lookup_timeout_ms` | G | 5000 | 2000–10000 | platform | P18 |
| `int.embed.allowed_origins` | T | [] | valid HTTPS origins | `ten_admin` | P18 |
| `int.embed.hosted_domain` | T | `{slug}.care.lawdocscomply.com` | CNAME verified | `ten_admin` | P18 |
| `int.channels.whatsapp.enabled` | T | OFF | flag | `ten_admin` | P18 |
| `int.voice.ai_agent.enabled` | G→T | OFF | flag | platform enables, tenant opts in | P18 |
| `int.rcs.enabled` | G | OFF | flag | platform | P18 |
| `int.agent.auto_update` | T | true | bool | `ten_admin` | P18 |
| `int.compliance_mode.dual_publish_periods` | G | 1 | 1–3 | platform | P18 |
| `int.registry_datasets.refresh_days` | G | 30 | 1–90 | content team | P18 |
| `int.deprecation.public_api_months` | G | 12 | 6–24 | platform | P18 |
| `int.academy.sso_mode` | G | OIDC | OIDC / LTI13 | platform | P18 |
| `xpt.download.link_validity_days` | T | 7 | 1–30 | `ten_admin` | P19 |
| `xpt.download.part_size_gb` | T | 4 | 1–10 | `ten_admin` | P19 |
| `xpt.store.retention_days` | T | 30 | 7–90 | `ten_admin` | P19 |
| `xpt.full_export.requires_second_approver` | L | true | — | locked | P19 |
| `xpt.restricted.requires_dpo` | L | true | — | locked | P19 |
| `xpt.folder.entity_level` | T | auto | auto/always/never | `ten_admin` | P19 |
| `xpt.folder.fy_format` | T | `FY YYYY-YY` | enum | `ten_admin` | P19 |
| `xpt.folder.name_mode` | T | historical | historical/current | `ten_admin` | P19 |
| `xpt.folder.people_naming` | G | ids_only | ids_only / id_and_masked_name (DPO approval) | platform + tenant DPO | P19 |
| `xpt.readme.languages` | T | [en] | en, hi, others as available | `ten_admin` | P19 |
| `xpt.offline_viewer.enabled` | T | true | bool | `ten_admin` | P19 |
| `xpt.jsonl.include` | T | true for FULL/EXIT | bool | `ten_admin` | P19 |
| `xpt.backup.daily_incremental_time` | T | 01:30 IST | 00:00–05:00 | `ten_admin` | P19 |
| `xpt.restore_test.frequency` | T | quarterly | monthly–annually | `ten_admin` | P19 |
| `xpt.target.residency_recheck_days` | L | 7 | — | locked (Spec §12.2) | P19 |
| `xpt.intake.rollback_days` | T | 7 | 1–30 | `ten_admin` | P19 |
| `xpt.intake.max_files_per_job` | G | 50,000 | 1,000–500,000 | platform | P19 |
| `xpt.exit.read_only_days` | T | 90 | 30–180 | contract / `ten_admin` | P19 |
| `xpt.deletion.backup_expiry_disclosure` | L | true | — | locked | P19 |
| `xpt.bsa63.include` | T | true | bool | `ten_admin` | P19 |

#### Settings — stream S9 (P20–P22, App N, O, X)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `bil.billing_port.mode` | G | `OH8` | OH8, LOCAL_INTERIM, MOCK (non-prod) | Owner decision + `plt_super_admin` + checker | P20 |
| `bil.trial.default_days` | G | 7 | 1–60 | `plt_super_admin` + checker | P20 |
| `bil.trial.self_extension_days` | G | 7 | 0–7 | `plt_super_admin` | P20 |
| `bil.trial.lawdocs_extension_max_without_checker` | G | 14 | 0–30 | `plt_super_admin` + checker | P20 |
| `bil.trial.retention_days` | G | 30 | 15–90 | `plt_super_admin` + DPO | P20 |
| `bil.trial.plan_code` | G | `TRIAL_PRO` | catalogue trial policies | Pricing Studio | P20 |
| `bil.trial.ai_credit_cap` | G | 200 | 0–2,000 | Pricing Studio | P20 |
| `bil.trial.reminder_offsets_days` | G | [3, 1] | each 1–14 | Pricing Studio | P20 |
| `bil.exit.read_only_days` | G | 30 | floor 30, max 180 | `plt_super_admin` + checker | P20 |
| `bil.configurator.saved_config_ttl_days` | G | 30 | 7–180 | Pricing Studio | P20 |
| `bil.pricing.show_gst_inclusive_total` | L | true | — | — (always shown before payment) | P20 |
| `bil.pricing.prior_price_window_days` | L | 30 | — | — | P20 |
| `bil.stream.<code>.enabled` | G | per Appendix N §N.6 | narrow-only vs OH8 | `plt_super_admin` (+ checker if high impact) | P20 |
| `bil.tenant.purchase_approval_threshold` | T | off | ₹0–₹1 crore | `ten_admin` | P20 |
| `bil.tenant.purchase_approvers` | T | [] | tenant users with `billing.approve_purchase` | `ten_admin` | P20 |
| `bil.tenant.po_required` | T | false | — | `ten_admin` | P20 |
| `bil.tenant.overage_opt_in` | T | false | — | `ten_admin` | P20 |
| `bil.tenant.billing_contacts` | T | admin | 1–10 | `ten_admin` | P20 |
| `bil.ai.rollover` | G | false | — | Pricing Studio | P20 |
| `bil.ai.user_cap_credits` | T | none | 0–tenant balance | `ten_admin` | P20 |
| `bil.limits.soft_threshold_pct` | G | 80 | 50–95 | `plt_super_admin` | P20 |
| `bil.savings.enabled` | T | true | — | `ten_admin` | P20 |
| `bil.savings.show_estimated` | T | true | — | `ten_admin` | P20 |
| `bil.savings.share_with_rm` | T | on if retainer else off | — | `ten_admin` | P20 |
| `bil.savings.penalty_rule_max_age_days` | G | 180 | 30–365 | `plt_content_checker` | P20 |
| `bil.savings.marketing_min_tenants` | L | 20 | — | — | P20 |
| `bil.badge.most_chosen.window_days` | G | 90 | 30–365 | Pricing Studio | P20 |
| `bil.never_block_list` | L | FR-P20-43 | — | — | P20 |
| `mkp.public.enabled` | G | true | — | `plt_super_admin` | P21 |
| `mkp.providers.external.enabled` | G | false | — | Owner + counsel ref | P21 |
| `mkp.model.m2.enabled` | G | false | — | Owner + counsel ref | P21 |
| `mkp.model.m3.enabled` | G | false | — | Owner + counsel + tax ref | P21 |
| `mkp.profession.<code>.listing_mode` | G | per FR-P21-12 | OFF, DIRECTORY_RULE36, DIRECTORY_ICAI, FULL_MARKETPLACE | `plt_super_admin` + `plt_content_checker` + counsel_opinion_ref (mandatory) | P21 |
| `mkp.profession.<code>.commission_allowed` | G | false (advocate: L false) | — | as above | P21 |
| `mkp.profession.<code>.ratings_allowed` | G | false for regulated professions (advocate: L false) | — | as above | P21 |
| `mkp.sponsored.enabled` | G | false | never for regulated professions (L) | Owner | P21 |
| `mkp.contract.clickwrap_max_value` | G | ₹50,000 [OWNER TO SET] | ₹0–₹2,00,000 | `plt_super_admin` + legal | P21 |
| `mkp.acceptance.deemed_days` | G | 10 BD | 0 (off)–30 | `plt_super_admin` + legal | P21 |
| `mkp.retainer.hour_rollover_months` | G | 1 | 0–3 | `dlv_lead` + checker | P21 |
| `mkp.disputes.provider_response_bd` | G | 5 | 2–10 | `plt_super_admin` | P21 |
| `mkp.tenant.who_can_buy` | T | admins + CCO + CFO | any role set | `ten_admin` | P21 |
| `mkp.tenant.contextual_offers` | T | true | — | `ten_admin` | P21 |
| `mkp.academy.display_name` | G | "LawDocs Trainings — FinLegal Academy" [OWNER TO SET] | — | Owner | P21 |
| `mkp.academy.cache_max_age_days` | G | 7 | 1–14 | `plt_super_admin` | P21 |
| `mkp.category.disputes.equator_link` | G | false | — | Owner + Equator oversight | P21 |
| `mkp.price_guardrail.<category>` | G | min/max per category | — | `plt_super_admin` | P21 |
| `sdc.rm.max_clients` | G | 25 | 5–60 | `dlv_lead` + checker | P22 |
| `sdc.grants.max_months.retainer` | G | 12 | 1–12 | `plt_super_admin` | P22 |
| `sdc.grants.max_months.implementation` | G | 3 | 1–6 | `plt_super_admin` | P22 |
| `sdc.grants.support_session_max_hours` | L | 8 | — | — | P22 |
| `sdc.grants.expiry_notice_days` | G | 14 | 7–30 | `plt_super_admin` | P22 |
| `sdc.grants.alternate_approvers` | T | none | client users with admin/CCO | `ten_admin` | P22 |
| `sdc.grants.include_sealed_classes` | T | false | — | `ten_admin` (step-up, per grant) | P22 |
| `sdc.session.idle_timeout_min` | G | 30 | 10–60 | `plt_security_officer` | P22 |
| `sdc.vault.reveal_seconds` | G | 30 | 10–60 | `plt_security_officer` | P22 |
| `sdc.vault.client_only_types` | G | RBI_CIMS, RBI_DAKSH, RBI_PRAVAAH, CIC_*, FIU_IND | add-only | `plt_security_officer` | P22 |
| `sdc.vault.blocked_types` | L | NET_BANKING, EMAIL, DSC_PIN, OTP_SEED | — | — | P22 |
| `sdc.vault.reveal_notify_mode` | T | IMMEDIATE | IMMEDIATE, DAILY_DIGEST (not for client-only types) | `ten_admin` | P22 |
| `sdc.vault.allowed_hours` | T | none | e.g., 08:00–21:00 | `ten_admin` | P22 |
| `sdc.vault.per_reveal_client_approval` | T | false | per entry | `ten_admin` | P22 |
| `sdc.vault.anomaly_threshold_per_hour` | G | 5 | 2–20 | `plt_security_officer` | P22 |
| `sdc.client_visibility.compliance_metrics` | T | [on_time_pct, overdue_count, high_risk_overdue, due_30d] | subset | `ten_admin` | P22 |
| `sdc.notes.client_visible` | T | false | — | `ten_admin` | P22 |
| `sdc.calendar.sync_detail_level` | G | TITLE_ONLY | NONE, TITLE_ONLY, TITLE_AND_LINK | `plt_security_officer` | P22 |
| `sdc.email.outbound_mode` | G | USER_MAILBOX | USER_MAILBOX, PLATFORM_ON_BEHALF | `plt_super_admin` | P22 |
| `sdc.health.weights` | G | adoption 25, hygiene 25, service 25, commercial 15, relationship 10 | sum 100 | `dlv_lead` + checker | P22 |
| `sdc.access_review.cadence_months` | G | 3 | 1–6 | `plt_security_officer` | P22 |

#### Settings — stream S10 (P23, App P, R)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `web.locale.hi.enabled` | G | true for glossary/health check; false elsewhere until reviewed | — | plt_content_publisher | P23 |
| `web.hc.families_enabled` | G | 12 launch families | subset of P15 families with a published bank | plt_content_publisher | P23 |
| `web.hc.min_questions` | G | 40 | 30–60 | plt_content_checker | P23 |
| `web.hc.bands` | G | 85/70/50 | ascending, 0–100 | plt_content_checker (maker ≠ checker) | P23 |
| `web.hc.critical_cap_count` | G | 3 | 1–10 | plt_content_checker | P23 |
| `web.hc.peer_benchmark.enabled` | G | OFF | requires k ≥ 30 per family | plt_super_admin + plt_content_checker | P23 |
| `web.hc.peer_benchmark.k_min` | L | 30 | — | — | P23 |
| `web.hc.retention_days` | G | 365 | 90–730 | plt_super_admin (DPO consulted) | P23 |
| `web.hc.share_link_expiry_days` | G | 90 | 1–365 | plt_content_publisher | P23 |
| `web.hc.narrative_ai.enabled` | G | ON | — | plt_super_admin | P23 |
| `web.hc.lookup.rate_limit_per_ip_hour` | G | 5 | 1–50 | plt_security_officer | P23 |
| `web.hc.email_gate_position` | G | AFTER_SEGMENT_1 | {AFTER_SEGMENT_1, AT_RESULT_PDF} (never at entry) | plt_content_publisher | P23 |
| `web.reg_updates.public_delay_minutes` | G | 0 | 0–10,080 | plt_content_publisher | P23 |
| `web.claims.default_expiry_days` | G | 365 | 30–730 | plt_content_checker | P23 |
| `web.claims.prohibited_phrases` | L | list in FR-P23-33 | append-only via release | — | P23 |
| `web.authors.advocate_bio_mode` | L | RULE36_FIELDS_ONLY | — | — | P23 |
| `web.robots.ai_training_crawlers` | G | ALLOW_PUBLIC_MARKETING | {ALLOW_PUBLIC_MARKETING, DISALLOW_ALL} | plt_super_admin (owner decision) | P23 |
| `web.robots.ai_search_crawlers` | G | ALLOW | {ALLOW, DISALLOW} | plt_super_admin | P23 |
| `web.experiments.enabled` | G | ON | never on legal/pricing amounts (L guard) | plt_content_publisher | P23 |
| `web.cookies.marketing_pixels.enabled` | G | OFF until consent banner live | — | plt_super_admin | P23 |
| `web.funnel.dark_pattern_audit_required` | L | true | — | — | P23 |
| `hlp.term.inline_default_for_new_users_days` | T (tenant) | 14 | 0–90 | ten_admin | P23 |
| `hlp.tours.enabled` | T | ON | — | ten_admin | P23 |
| `hlp.whats_new.max_per_session` | G | 1 | 0–3 | plt_content_publisher | P23 |
| `hlp.tutorials.diff_threshold` | G | 0.02 | 0.005–0.1 | plt_content_checker | P23 |
| `hlp.learning.per_user_reporting` | T | OFF | requires user notice (NN-25) | ten_admin | P23 |
| `hlp.a11y.grievance_ack_hours` | G | 24 (working) | 4–48 | plt_super_admin | P23 |
| `hlp.a11y.grievance_resolve_days` | G | 15 (working) | 5–30 | plt_super_admin | P23 |
| `hlp.a11y.release_gate` | L | ON | — | — | P23 |
| `user.a11y.*` (text_scale, spacing, font, theme, motion, captions, shortcuts, inline_terms, simplified_layout, read_aloud) | T (user) | system defaults | per FR-P23-129 | each user | P23 |


---

## U.10 Who can change what without a super admin (summary for R-024, R-039)

| User type | Can change on their own | Needs a tenant checker | Needs LawDocs |
|---|---|---|---|
| Any user | Language, accessibility, theme, density, digest times, quiet hours (narrower), personal dashboards, saved views, delegation/away, notification channels within policy, AI suggestion opt-out | — | — |
| Department head | Department aliases (if delegated), function list, reminder cadence (department), assignment pools, department dashboards | Department-level G proposals | — |
| `ten_admin` | All T values: departments, terminology, status labels, custom fields, forms, workflows (subject to invariants), SLA above floors, waiting-on policies, templates' non-legal text, menus, branding, packs application, integrations | Tenant G values (CCO checks), privileged role grants (if two-person enabled) | L values (never); platform G values (raise a request or rule challenge) |
| `ten_cco` | Checks tenant G values; NA and exception approvals; tenant overlays approval | — | — |
| `plt_super_admin` | — (every tenant-scope change is a Correction Entry) | — | Second platform approver |

## U.11 Sources (accessed 25 October 2026)

As P02 §15; plus owner's Excel templates (column `department` (v1.0: M) department list: Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management) from `SAMPLE - Finance Company Regulations 2021 - Compliance Questions.xlsx` (Rough sheet, named range `IFSCA_Dept`); Multi-State Co-operative Societies (Amendment) Act 2023 [VERIFY provisions]; Companies Act 2013 ss.96, 128, 173.

---

## U.12 v1.1 core settings and catalogue additions *(v1.1)*

### U.12.1 Core settings added in v1.1 (P00, P01, P02, P24)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `core.region.default_cell` | L | IN | — | — | P00 |
| `core.region.cells_for_sale` | G (platform) | [IN] | IN, EU, GCC, SG, US | plt_super_admin + second approver | P00, P24 |
| `core.batches.default_undo_hours` | G | 24 | 1–168 | ten_admin + ten_cco | P00, P02 |
| `cfg.batches.undo_hours.<kind>` | G | 24 | 1–168 | ten_admin + ten_cco | P02 |
| `core.sandbox.ttl_days` | G (platform) | 90 | 30–365 | plt_super_admin | P00 |
| `cfg.sandbox.enabled` | T | ON | — | ten_admin | P02 |
| `cfg.registers.max_per_tenant` | G (plan) | per Appendix N | — | plt_super_admin | P02 |
| `cfg.simulation.lookback_days` | T | 30 | 7–180 | ten_admin | P02 |
| `cfg.simulation.required_before_publish` | L | true | — | — | P02 |
| `onb.profile.max_questions` | L | 12 | — | — | P01 |
| `onb.import.enabled` | T | ON | — | ten_admin | P01 |
| `onb.import.undo_window_hours` | G | 24 | 1–168 | ten_admin + ten_cco | P01 |
| `onb.import.auto_map_threshold` | T | 0.85 | 0.70–0.99 | ten_admin | P01 |
| `onb.baseline.enabled` / `onb.first_value_checklist.enabled` | T | ON | — | ten_admin | P01 |
| `pack.pfrda.enabled` | G (platform flag) | OFF | — | plt_content_publisher | P01, P15 |
| `iam.delegation.max_days` | T | 90 | 1–365 | ten_admin | P01 |
| `iam.practitioner.enabled` | G (platform) | OFF | — | plt_super_admin | P01 |
| `ai.autonomy.platform_ceiling.<agent>` | L | L2 (L3-eligible after gate) | L0–L4 | platform release | P17, P02 |
| `ai.autonomy.tenant_ceiling` | G | L1 | L0–platform ceiling | ten_admin + ten_cco (AIO where designated) | P17, P02 |
| `ai.autonomy.agent.<agent>` / `ai.autonomy.skill.<skill>` | G raise / T lower | L1 / inherit | ≤ parent | sponsor + ten_admin | P17, P02 |
| `ai.autonomy.sealed_contexts` | L | L0 | — | — | P17 |
| `ai.autonomy.promotion_min_eval_pass` | G (platform) | 0.95 | 0.90–1.00 | plt_super_admin | P02 |
| `ai.kill_switch.propagation_slo_seconds` | L | 60 | — | — | P00 |
| `ai.killswitch.drill_frequency_days` | T | 90 | 30–365; Enterprise ≤ 90 (mandatory); platform and provider/route switches drilled quarterly by LDC for all tenants (NN-51) *(X1)* | ten_admin | P17, P02 |
| `notify.budget.daily_interruptive` | T | 15 | 5–50 (users may only lower) | ten_admin | P02 |
| `eng.release.cell_lag_days` | G (platform) | 7 | 0–30 | CAB | P24 |
| `eng.ai.eval_regression_max_points` | G (platform) | 2 | 0–5 | eng_ai_lead + plt_security_officer | P24 |
| `eng.ai.canary_days` | G (platform) | 7 | 3–30 | CAB | P24 |
| `eng.ai.client_notice_days_major` | G (platform) | 30 | 0–90 | CAB | P24 |
| `eng.reports.async_threshold_rows` | G (platform) | 10000 | 1000–100000 | eng lead | P24 |
| `eng.ideas.enabled` | G (platform) | ON | — | plt_super_admin | P24 |

Module settings proposed by v1.1 streams G1 (P25), G3 (P17/`OV_AI`) and the stage-2 editors of P03–P28 are compiled by the lead into §U.9.

### U.12.2 Department codes added (extend §U.6.1)

| Code | Canonical name | Typical families |
|---|---|---|
| `ESG` | Sustainability & ESG | Listed (BRSR), large companies (CSR), lenders (climate) |
| `AIG` | AI Governance | All tenants using `OV_AI` |
| `LEGL` | Legal Matters & Litigation (sub-department of LEG when a separate in-house legal team runs P26) | All |

### U.12.3 Rule-pack catalogue additions (extend §U.5)

| Domain | Packs (examples) | Owner → checker | Phase |
|---|---|---|---|
| Legal matters | `IN.lit.notice_windows` (reply windows by notice type), `IN.lit.limitation` (Limitation Act 1963 schedule by forum), `IN.lit.reg30_materiality` | Content → GC-domain checker | P26 |
| ESG & CSR | `IN.csr.s135` (thresholds, 2% computation, unspent-transfer clocks), `IN.esg.brsr` (BRSR / BRSR Core attributes, assurance glide-path), `INTL.ghg.emission_factors` (CEA grid factor, IPCC, DEFRA; versioned) | Content → CS/CSO checker | P27 |
| Jurisdictions | `<ISO-country>.calendar.holidays`, `<ISO-country>.calendar.fy`, `<ISO-country>.<domain>.applicability` per published jurisdiction pack | Partner reviewer of record → platform publisher | P25 |
| AI governance | `IN.ai.governance` (RBI FREE-AI recommendations as advisory, RBI draft MRM as advisory until final, MeitY guidelines), `EU.ai.act` (risk classes, obligations timeline), `INTL.ai.iso42001` | Content → AIO-domain checker | P12 |
| Autonomy | `PLATFORM.ai.autonomy_matrix` (which skills may run at which level by data class) | AI lead → plt_security_officer | P02, P17 |

### U.12.4 Configuration template library (seed; P02 FR-P02-80)

| Template | Bundles |
|---|---|
| NBFC-ML standard | Setting pack `RBI-NBFC-ML` + approval matrix (maker → checker → CCO for High), SLA policies, notification budget 15, dashboards for CCO/CRO/CFO, custom registers (bank accounts & signatories, outsourcing, licences), autonomy L2 |
| NBFC-BL lean | `RBI-NBFC-BL` + single checker, weekly digests, minimal registers |
| Listed company — main board | `SEBI-LISTED-MAIN` + Reg 30 disclosure workflow, PIT SDD, CS dashboards, board-pack templates |
| Private company — small | `MCA-SMALL` + annual calendar, registers, CS-on-retainer delivery grant template |
| Credit co-operative — State Act | `COOP-CCS-<State>` + Hindi labels, general-body calendar, election support |
| Insurance broker | `IRDAI-BROKER` + Principal Officer workflows |
| IFSCA FC/FU | `IFSCA-FCFU` + IFSC calendar, parent-entity links |
| Group with subsidiaries | Group roll-up dashboards, shared policies, entity switcher defaults, configuration inheritance rules |
| Foreign subsidiary (INTL-GEN) | Jurisdiction-pack defaults, locale, holiday calendar, partner delivery grant template (P25) |

### U.12.5 Who can change what — v1.1 additions (extend §U.10)

AI Officer (`ten_kmp` AIO): lower any autonomy level immediately; propose raises (G with `ten_admin`); operate tenant/agent/skill/mission kill switches; schedule drills. Any user: lower the autonomy of agents acting on their behalf, revoke their delegation grants, lower their notification budget. Tenant admin: build custom registers, run simulations, apply configuration templates (undo 24 h), open sandboxes.

Sources (v1.1): Appendix AA (autonomy levels, kill switches); Appendix Y (cells, jurisdiction calendars); Appendix Z (IMP-059–063, IMP-040/041); Companies Act 2013 s.135; SEBI LODR Reg 34(2)(f); Limitation Act 1963.

## U.13 Compiled v1.1 module settings

*(v1.1)* Register before use (NN-28). Where two editors defined the same key, the owning phase's row prevails (`cmp.dashboard.collapse_equivalents` → P04).

#### Settings — v1.1 G1 (P25, App Y)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| gem.default_home_cell_by_jurisdiction | G | IN→IN; EU/EEA/UK/CH→EU; AE/BH/OM/QA/KW→GCC; SG→SG; others→IN | OPEN cells only | plt_super_admin (maker-checker) | P25 |
| gem.india_entities_home_cell | L | IN | — | — | P25 |
| gem.cross_cell_replication.enabled | T (gated) | OFF | requires transfer-register basis | ten_admin + DPO | P25 |
| gem.aggregation.interval_minutes | G | 15 | 5–60 | platform | P25 |
| gpk.monitoring.stale_days | G | 30 | 7–45 | platform | P25 |
| gpk.pilot.min_days | G | 60 | 30–180 | platform | P25 |
| gpk.freshness_sla.tier_a_days | G | 30 | 7–365 | platform | P25 |
| gpk.freshness_sla.tier_b_days | G | 90 | 7–365 | platform | P25 |
| gpk.freshness_sla.tier_c_days | G | 180 | 7–365 | platform | P25 |
| gpk.event_update_sla_business_days | G | 10 | 1–30 | platform | P25 |
| gpk.publication.two_key | L | ON | — | — | P25 |
| tpl.intl.reviewer_line_required | L | ON | — | — | P25 |
| prt.query.first_response_hours | G | 8 business hours | 2–24 | platform (per partner agreement) | P25 |
| prt.query.answer_business_days | G | 3 | 1–10 | platform | P25 |
| prt.commercial.<country>.<profession>.<model> | G | OFF | requires counsel_opinion_ref | plt_super_admin | P25 |
| i18n.locales.enabled | G | en-IN, en-GB, en-US, hi-IN, ar-AE | — | platform | P25 |
| i18n.tenant_default_locale | T | en-IN | enabled locales | ten_admin | P25 |
| i18n.number_grouping | T (user) | locale default | indian / international | user | P25 |
| chg.scan.local_time_by_cell | G | IN 20:00 IST; EU 18:00 CET; GCC 18:00 GST | — | platform | P25 |
| fx.rate_source_by_currency | G | RBI (INR), ECB (EUR), CBUAE (AED) | approved sources | platform | P25 |
| ai.route.<cell> | G | OFF until model availability verified | approved routes only | plt_security_officer | P25 |

#### Settings — v1.1 G3 (P17, App AA, K)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| ai.autonomy.platform_ceiling.<agent> | L | L2 (L3-eligible after gate) | L0–L4 | Platform release | P17 |
| ai.autonomy.tenant_ceiling | G | L1 | L0–platform ceiling | ten_admin + ten_cco | P17 |
| ai.autonomy.agent.<agent> | G | L1 | ≤ tenant ceiling | sponsor + ten_admin | P17 |
| ai.autonomy.skill.<skill> | T lower / G raise | inherit | ≤ agent | sponsor | P17 |
| ai.autonomy.sealed_contexts | L | L0 | — | — | P17 |
| ai.agents.enabled | T | plan set | subset of plan | ten_admin | P17 |
| ai.agents.supervised_days | T | 30 | 7–90 | ten_admin | P17 |
| ai.agents.sponsor_required_from_level | L | L2 | — | — | P17 |
| ai.missions.enabled | T | OFF | ON/OFF | ten_admin | P17 |
| ai.missions.max_duration_days | G | 90 | 1–180 | platform | P17 |
| ai.missions.max_steps | G | 200 | 10–500 | platform | P17 |
| ai.memory.episodic_retention_days | T | 365 | 30–1825 | ten_admin | P17 |
| int.mcp.server.enabled | T | OFF | ON/OFF | ten_admin | P18 |
| int.mcp.allowed_clients | T | empty | list | ten_integration_admin | P18 |
| int.mcp.client_basis | G (tenant) | empty | recorded basis + DPO | ten_admin + DPO | P18 |
| int.mcp.allow_autonomous_external_agents | G | OFF | ON/OFF | ten_admin + ten_cco | P18 |
| int.mcp.rate_limit_per_user_per_min | G | 60 | 10–600 | platform | P18 |
| ai.mcp.client.enabled | T | OFF | ON/OFF | ten_admin | P17 |
| int.a2a.enabled | G | OFF | ON/OFF | platform + ten_admin | P18 |
| ai.routing.sovereign_route | G | OFF | ON/OFF | platform + ten_admin | P17 |
| ccm.enabled | T | OFF | ON/OFF (plan) | ten_admin | P17/P04 |
| ai.killswitch.drill_frequency_days | T | 90 | 30–365 | ten_admin | P17 |
| ai.skill.voice_summary.enabled | G | OFF | ON/OFF | platform + ten_admin | P17 |
| aig.retention_years | G | 10 | 7–20 | platform | P12 |
| aig.enabled | T | OFF (add-on) | ON/OFF (plan) | ten_admin | P12 |

#### Settings — v1.1 F1 (P00–P02, P24, App A, B, D, Q, U)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| core.region.default_cell | L | IN | — | — | P00 |
| core.region.cells_for_sale | G (platform) | [IN] | IN, EU, GCC, SG, US | plt_super_admin + second approver | P00 |
| core.batches.default_undo_hours | G | 24 | 1–168 | ten_admin + ten_cco | P00 |
| core.sandbox.ttl_days | G (platform) | 90 | 30–365 | plt_super_admin | P00 |
| onb.profile.max_questions | L | 12 | — | — | P01 |
| onb.import.enabled | T | ON | — | ten_admin | P01 |
| onb.import.undo_window_hours | G | 24 | 1–168 | ten_admin + ten_cco | P01 |
| onb.import.auto_map_threshold | T | 0.85 | 0.70–0.99 | ten_admin | P01 |
| onb.baseline.enabled | T | ON | — | ten_admin | P01 |
| onb.first_value_checklist.enabled | T | ON | — | ten_admin | P01 |
| pack.pfrda.enabled | G (platform flag) | OFF | — | plt_content_publisher | P01 |
| iam.delegation.max_days | T | 90 | 1–365 | ten_admin | P01 |
| iam.practitioner.enabled | G (platform) | OFF | — | plt_super_admin | P01 |
| cfg.registers.max_per_tenant | G (plan) | per App N | — | plt_super_admin | P02 |
| cfg.simulation.lookback_days | T | 30 | 7–180 | ten_admin | P02 |
| cfg.simulation.required_before_publish | L | true | — | — | P02 |
| cfg.sandbox.enabled | T | ON | — | ten_admin | P02 |
| cfg.batches.undo_hours.<kind> | G | 24 | 1–168 | ten_admin + ten_cco | P02 |
| ai.autonomy.promotion_min_eval_pass | G (platform) | 0.95 | 0.90–1.00 | plt_super_admin | P02 |
| ai.kill_switch.propagation_slo_seconds | L | 60 | — | — | P00 |
| notify.budget.daily_interruptive | T | 15 | 5–50 (users may only lower) | ten_admin | P02 |
| eng.release.cell_lag_days | G (platform) | 7 | 0–30 | CAB | P24 |
| eng.ai.eval_regression_max_points | G (platform) | 2 | 0–5 | eng_ai_lead + plt_security_officer | P24 |
| eng.ai.canary_days | G (platform) | 7 | 3–30 | CAB | P24 |
| eng.ai.client_notice_days_major | G (platform) | 30 | 0–90 | CAB | P24 |
| eng.reports.async_threshold_rows | G (platform) | 10000 | 1000–100000 | eng lead | P24 |
| eng.ideas.enabled | G (platform) | ON | — | plt_super_admin | P24 |

Autonomy and kill-switch keys (`ai.autonomy.*`, `ai.killswitch.drill_frequency_days`) are owned by P17 (G3 settings) and edited in the P02 Studio.

#### Settings — v1.1 F2 (P03–P05, App E, F)

| Key | Tier | Default | Range / values | Who changes | Phase |
|---|---|---|---|---|---|
| `tpl.import.undo_window_hours` | T (G for platform content) | 24 | 1–72 | ten_admin / content lead | P03, App E |
| `tpl.tracker_import.enabled` | T | ON | ON/OFF | ten_admin | P03 |
| `tpl.tracker_import.auto_accept_confidence` | T | 0.95 | 0.85–1.00 | ten_cco | P03 |
| `tpl.tracker_import.approver_must_differ` | T | true | — | ten_admin | P03 |
| `tpl.import.official_domains` (extended) | G + per pack `pack.official_domains` | Indian list + AI list | data | content lead | App E §E.4.6 |
| `cnt.catalogue.placeholder_instances` | T | ON | ON/OFF | ten_admin | P03 |
| `cnt.evidence_reuse.sibling_mode` | T | OFF | OFF / SAME_ENTITY / GROUP | ten_cco | P03 |
| `cnt.equivalence.threshold` | G | 0.88 | 0.80–0.97 | content lead | P03 |
| `cnt.applicability.max_profile_questions` | G | 12 | 8–20 | product owner | P03 (with P01) |
| `cnt.controls.mapping_autonomy` | T | L1 | L0–L1 (NN-50) | ten_cco | P03 |
| `cnt.translation.require_review` | L | true | — (NN-54) | — | P03 |
| `cmp.dashboard.collapse_equivalents` | T | ON (executive views) | ON/OFF per view | ten_admin | P03 + P04 (one key; defined twice — keep one row in U) |
| `cmp.timeliness.rule` | G default; tenant change via maker-checker | ACT_DATE | ACT_DATE, ACT_AND_APPROVAL | ten_cco + approver | P04 |
| `cmp.timeliness.max_evidence_gap_days` | T | 30 | 0–180 | ten_cco | P04 |
| `cmp.requests.external_link_days` | T | 7 | 1–30 | ten_admin | P04 |
| `cmp.evidence.rules_overridable` | T | Medium and Low only | never High (L floor) | ten_cco | P04 |
| `cmp.ladder.adaptive` | T | ON | ON/OFF | ten_cco | P04 |
| `cmp.score.method` | T | INSTANCE_SCORE | INSTANCE_SCORE, HEALTH_INDEX, BOTH | ten_cco | P04 |
| `cmp.bulk.undo_window_hours` | T | 24 | 1–72 | ten_admin | P04 |
| `cmp.testing.remediation_sla_days` | T | H 30, M 60, L 90 | tighten only | ten_cco | P04 |
| `cmp.testing.sampling_defaults` | T | H 95 %/5 %, M 90 %/10 %, L judgemental | — | ten_cco | P04 |
| `cmp.automated_tests.auto_approve_internal` | T | OFF | ON/OFF (internal checkpoints only) | ten_cco | P04 |
| `wf.notify.fatigue.max_immediate_per_day` | T | 10 | — | ten_admin | P04 |
| `wf.notify.batch_window_minutes` | T | 10 | — | ten_admin | P04 |
| `ai.autonomy.agent.VA-02` | T | L1 | L0–L2 (NN-50) | ten_admin | P04 |
| `chg.backfill.margin_days` | G | 2 | 1–14 | content lead | P05, App F §F.14 |
| `chg.rbi_pages.missing_row_alert` | G | ON | — | content lead | P05, App F §F.2A |
| `chg.updates.collapse_non_adopted` | T | ON | — | ten_admin / user | P05 |
| `chg.updates.gist_max_words` | G | 60 | 30–100 | content lead | P05 |
| `chg.push.second_approver_scope` | G | ALL_TENANTS or > 50 tenants | — | super admin | P05 |
| `chg.incident.s1_containment_hours` | G | 4 | — | content lead | P05 |
| `chg.foreign.reconciliation_local_time` | G (per pack) | 20:00 authority-local | 18:00–23:00 | content lead | P05, App F §F.12C |
| `ai.autonomy.agent.VA-01` | G platform / T tenant | L1 | L0–L2 (NN-50) | content lead / ten_admin | P05 |
| `ai.authoring.min_row_score` | G (T for tenant studio) | 0.7 | 0.5–0.95 | content lead | App E §E.11, P05 FR-P05-76 |
| `chg.reg_intel.<provider>.enabled` | G | OFF | ON/OFF per provider | super admin | App F §F.12B |

#### Settings — v1.1 F3 (P06, P07, P10, P26, P27, App J)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| gov.rpt_txn.alert_pct (renamed from gov.rpt.alert_pct) | T | [80, 100] | 50–100 | CS | P06 |
| gov.upload.max_mb | T | 500 | 50–2,000 | Admin | P06 |
| gov.portal.offline_pack.enabled | T | OFF | device enrolment | CS + Admin | P06 |
| gov.portal.offline_pack.ttl_hours | T | 72 | 4–168 | CS | P06 |
| gov.prompts.enabled | T | ON | CS review | CS | P06 |
| gov.prompts.max_per_item | T | 5 | 0–10 | CS | P06 |
| gov.atr.escalate_after_meetings | T | 2 | 1–6 | CS | P06 |
| gov.agenda.autosuggest_sources | T | all | multi-select | CS | P06 |
| gov.annotation.reanchor_min_score | T | 0.8 | 0.6–0.95 | CS | P06 |
| gov.annual_report.assembly_block_on_missing | L | true | — | — | P06 |
| gov.securities.clock_days.* | G | rule pack | ≥ statutory | Platform content | P06 |
| gov.iepf.notice_lead_days | G | 90 | ≥ rule | CS | P06 |
| gov.ai.va04.autonomy_ceiling | T | L1 drafting / L2 internal tasks | L0–L2 | CS | P06 |
| pol.baton.nudge_cooldown_hours | T | 24 | 4–72 | CCO | P07 |
| pol.review.parallel_lanes_enabled | T | ON | Locked sequential where law requires | CCO | P07 |
| pol.drift.enabled | T | ON | — | CCO | P07 |
| pol.drift.parameters | T | all | multi-select | CCO | P07 |
| pol.quiz.pass_mark_pct | T | 70 | 50–100 | HR/CCO | P07 |
| pol.quiz.max_attempts | T | 3 | 1–10 | HR/CCO | P07 |
| pol.bulk.undo_hours | T | 24 | 1–72 | CCO | P07 |
| pol.ai.va05.autonomy_ceiling | T | L1 | L0–L1 | CCO | P07 |
| dms.render.progressive | L | ON | — | — | P07 |
| dms.addins.m365.enabled / dms.addins.google.enabled | T | OFF | admin consent | Admin | P07 |
| aud.pbc.reminder_ladder | T | [3,1,0,-2] | — | HIA | P10 |
| aud.evidence_match.min_score | T | 0.75 | 0.5–0.95 | HIA | P10 |
| aud.share_scope.include_new_evidence | T | ON | — | HIA | P10 |
| aud.workpaper.lock_on_review | L | true | — | — | P10 |
| cmp.testing.cycle_months.{high,medium,low} | T | 12/18/30 | 6–36 | CCO | P10 |
| cmp.testing.sample.* | T | 100%/25/12/5/100% | ≥ 1 | CCO | P10 |
| cmp.testing.tolerable_deviation_pct.* | T | 5/10/15 | 0–20 | CCO | P10 |
| cmp.testing.expand_on_deviation_pct | T | 25 | 0–100 | CCO | P10 |
| cmp.testing.issue_sla_days.* | T | 30/60/90/180 | ≥ 7 | CCO | P10 |
| cmp.testing.critical_escalation_bd | T | 5 | 1–10 | CCO | P10 |
| aud.ai.va07.autonomy_ceiling | T | L1 | L0–L1 | HIA | P10 |
| lit.* (28 keys — notice types, windows, triage SLA, approval matrix, privilege downgrade approver (L), hearings digest/lookahead/outcome, limitation rules and reminders, assessment frequency and guidance bands, risk weights, Reg 30 materiality, RFI reminders, closure verification (L), contract renewal alerts/legal review threshold/obligation extraction, licence lead days, ethics gift thresholds and campaign month, ecourts flag, recovery_lite flag (G, OFF), VA-16 ceiling, import undo) | see P26 §9 | | | GC / CCO / CS / CFO | P26 |
| esg.* (16 keys — rule pack version, boundary, GWP set, restatement threshold, variance threshold, evidence default, value-chain mode/threshold/coverage, Core option, CSR reminders/overhead cap/CSR-1 block (L), ESRS overlay, VA-17 ceiling, import undo) | see P27 §9 | | | CSO / CFO / CS / Platform | P27 |

#### Settings — v1.1 F4 (P08, P09, P11, P28, App H, I)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| erm.methodology.max_active_versions | T | 2 | 1–3 | CRO | P08 |
| erm.ai.autonomy_ceiling | G | L1 | L0–L2 | CRO + ten_admin | P08 |
| erm.ai.suggestions.enabled | T | ON | ON/OFF | CRO | P08 |
| erm.link.kri_to_issue.enabled | G | ON | ON/OFF | Platform | P08 |
| erm.link.kri_to_issue.families | T | regulatory-limit KRIs | subset | CRO, CCO | P08 |
| erm.link.noncompliance_to_risk.enabled | T | ON | ON/OFF | CRO | P08 |
| erm.ccm.consecutive_passes_to_clear | T | 3 | 2–6 | CRO | P08 |
| erm.ews.proximity_pct | T | 10% | 5–25% | CRO | P08 |
| erm.ews.incident_cluster | T | 3 in 30 days | 2–10 / 7–90 days | CRO | P08 |
| erm.ews.complaint_spike_pct | T | 150% | 120–300% | CRO, GRO | P08 |
| erm.group.reporting_currency | T | INR | ISO 4217 | Group CRO | P08 |
| erm.group.fx_rate_source | G | RBI reference / FBIL | P25 provider list | Platform | P08 |
| erm.bulk.undo_window_hours | T | 24 | 1–72 | ten_admin | P08 |
| ral.ai.autonomy_ceiling | G | L2 text / L1 calibration | L0–L2 | CRO + ten_admin | P09 |
| ral.rollforward.version_policy | T | SAME_VERSIONS | SAME/CURRENT | CRO | P09 |
| ral.rollforward.materiality_bps | T | 50 | 10–200 | CRO, CFO | P09 |
| ral.auto_runs.schedule | T | monthly T+5 WD | cron | CRO | P09 |
| ral.dq.min_score_to_certify | T | 90 | 70–100 | CFO | P09 |
| ral.internal_metrics.max_per_tenant | G | 200 | 50–1,000 | Platform | P09 |
| ral.capital_plan.warning_horizon_quarters | T | 4 | 2–8 | CRO | P09 |
| ral.sandbox.enabled | T | ON | ON/OFF | CRO | P09 |
| ret.ai.autonomy_ceiling | G | L2 drafts / L1 mappings | L0–L2 | CFO + ten_admin | P11 |
| ret.mapping.memory.enabled | T | ON | ON/OFF | Head of Reporting | P11 |
| ret.lead_time.data_request_wd | T | 10 | 3–30 | Head of Reporting | P11 |
| ret.prepare_due.schedule | T | 3rd WD after period end | cron | Head of Reporting | P11 |
| ret.variance.threshold_pct | T | 10% | 2–50% | CFO | P11 |
| ret.variance.threshold_abs | T | ₹10 lakh | ≥ 0 | CFO | P11 |
| ret.dq.min_score_to_submit | T | 85 | 60–100 | CFO | P11 |
| ret.validation.locale | T | en-IN | en-IN / hi-IN | ten_admin | P11 |
| ret.consolidation.enabled | T | OFF | ON/OFF | CFO | P11 |
| rpt.async.row_threshold | G | 10,000 | 1,000–100,000 | Platform | P28 |
| rpt.async.seconds_threshold | G | 5 | 2–30 | Platform | P28 |
| rpt.tier.management.approval | T | maker → domain owner | within SoD | ten_admin | P28 |
| rpt.tier.board.approval | T | maker → KMP → CS freeze | add only | ten_admin + CS | P28 |
| rpt.tier.regulator.approval | T | maker → CCO → MD/CEO | add only | ten_admin + CCO | P28 |
| rpt.tier.board.email_attachments | L | OFF | — | — | P28 |
| rpt.approval_sla_wd | T | 2/3/1 | 1–10 | ten_admin | P28 |
| rpt.schedule.lead_time_wd | T | 10 | 1–30 | Report owner | P28 |
| rpt.subscriptions.default_mode | T | DIGEST | DIGEST/IMMEDIATE | User | P28 |
| rpt.dashboards.personal_max | T | 5 | 1–10 | ten_admin | P28 |
| rpt.retention.operational_years | T | 2 | ≥ 1 | ten_admin | P28 |
| rpt.retention.management_years | T | 8 | ≥ 8 | ten_admin | P28 |
| rpt.pack.render_timeout_s | G | 60 | 30–600 | Platform | P28 |
| rpt.narrative.bound_check | L | ON | — | — | P28 |
| rpt.ai.autonomy_ceiling | G | L2 | L0–L2 | ten_admin | P28 |
| rpt.embed.enabled | T | OFF | ON/OFF | ten_admin | P28 |
| rpt.feeds.enabled | T | OFF | ON/OFF | ten_admin + CISO | P28 |
| rpt.benchmarking.enabled | G | OFF | ON/OFF | Platform | P28 |
| rpt.number_format | T | Indian | Indian/International | User | P28 |
| rpt.due_diligence.link_expiry_days | T | 14 | 1–90 | ten_admin | P28 |
| cmp.score.method | T | COMPLIANCE_SCORE | COMPLIANCE_SCORE / HEALTH_INDEX_5C | CCO | P28 (score defined in P04) |

#### Settings — v1.1 F5 (P12–P16, App G, S, T)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| aig.enabled | T | OFF (ON with add-on) | — | ten_admin | P12 |
| aig.frameworks.shown | T | FREE_AI, RBI_MRM_DRAFT, ISO42001, NIST_RMF (+EU_AI_ACT if EU nexus) | published frameworks | AIO | P12 |
| aig.validation_frequency_months.<tier> | T within G floor | High 12, Medium 24, Low 36 | ≤ floor | AIO | P12 |
| aig.kill_switch_test_interval_days | T | 90 | 30–180 | AIO | P12 |
| aig.retention_years | G | 10 | ≥ 8 | plt_content_checker | P12 |
| aig.discovery.sources | T | all five | subset | AIO | P12 |
| aig.va15.autonomy_level | T | L1 | L0–L2 | AIO + checker | P12 |
| dpc.tree.regeneration | T | AUTO_DIFF | AUTO_DIFF / MANUAL | DPO | P12 |
| dpc.raci.matrix | T | §4S seed | one A per row | DPO | P12 |
| tpr.reassessment.triggers | T | all ON | subset | vendor-risk owner | P12 |
| tpr.ddq.ai_extraction.enabled | T | ON | — | vendor-risk owner | P12 |
| tpr.ddq.answer_library.enabled | T | ON | — | CCO | P12 |
| tpr.materiality.weights | G bounds + T | rule pack | within bounds | CRO (checker) | P12 |
| hr.leave.auto_approval_rules | T | none | guard rails (App T §T.16B) | HR admin + CHRO | P13 |
| hr.approval.escalate_after_hours | T | 48 | 4–168 | HR admin | P13 |
| hr.approval.channels | T | INBOX, EMAIL | + TEAMS | HR admin | P13 |
| hr.bulk.undo_window_hours | T | 24 | 1–72 | HR admin | P13 |
| hr.letters.auto_fulfil | T | ON | — | HR admin | P13 |
| hr.contractor_portal.enabled | T | OFF | — | HR admin | P13 |
| hr.penalty_exposure.visible_to | T | CHRO, CCO, CFO | roles | CHRO | P13 |
| hr.ethics.declaration_cycle | T | annual + event | — | CCO | P13 |
| hr.apprentices.enabled | G | OFF | — | plt_content_checker after verification | P13 |
| grv.ai.triage.autonomy_level | T | L1 | L0–L2 (L2 queries only) | CCO + checker | P14 |
| grv.channels.enabled | T | WEB, EMAIL | WEB, EMAIL, WHATSAPP, VOICE, BRANCH, LETTER, SOCIAL, API | ten_admin | P14 |
| grv.taxonomy.tenant | T | family seed | must map to regulator taxonomy | GRO | P14 |
| grv.sla.internal.<category>.<priority> | T | rule-pack seed | ≤ statutory floor | GRO | P14 |
| grv.bulk.undo_window_hours | T | 24 | 1–72 | GRO | P14 |
| grv.human_route.mandatory | L | ON | — | — | P14 |
| pack.questionnaire.max_questions | L | 12 | — | — | P15 |
| pack.dedup.enabled | T | ON | — | ten_cco | P15 |
| pack.dedup.rule | G | MOST_STRINGENT_WINS | MOST_STRINGENT_WINS / UNION_ONLY | plt_content_checker | P15 |
| pack.catalogue.placeholders | T | ON | — | ten_cco | P15 |
| pack.pfrda.enabled | G | OFF | — | plt_super_admin | P15 |
| pack.group.rolldown_mode | T | INHERIT_WITH_OVERRIDE | INHERIT / INHERIT_WITH_OVERRIDE / NONE | group CCO | P15 |
| coop.languages | T | [en, hi] | published templates | secretary | P16 |
| coop.notice.channels | T | SMS, EMAIL, PORTAL, NOTICE_BOARD | + WHATSAPP_SERVICE | secretary | P16 |
| coop.treasurer.approval_limits | T | per bye-laws | ≤ Act limits | committee resolution | P16 |
| coop.inspection.fee_table | G + T | State pack | ≥ 0 | secretary | P16 |
| coop.ai.autonomy_level | T | L1 | L0–L1 | secretary | P16 |

#### Settings — v1.1 F6 (P18–P23, App C, L, M, N, O, P, X)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `int.mcp.server.enabled` | T | false | — | `ten_admin` | P18 |
| `int.mcp.client_allowlist` | T | empty | client metadata URLs | `ten_admin`, `ten_integration_admin` | P18 |
| `int.mcp.client_basis` | T | none | basis code per client | `ten_admin` + DPO note | P18 |
| `int.mcp.rate_limit_user_per_min` | G | 60 | 10–300 | platform | P18 |
| `int.mcp.rate_limit_tenant_per_day` | G | 10,000 | 1,000–200,000 | platform (plan-linked) | P18 |
| `int.mcp.evidence_draft.enabled` | T | false | — | `ten_admin` | P18 |
| `ai.mcp.client.enabled` | T | false | — | `ten_admin` | P18 |
| `int.a2a.enabled` | G | false | requires Spec v1.2 | `plt_super_admin` + checker | P18 |
| `int.a2a.peers_allowlist` | T | ecosystem peers | — | `ten_admin` | P18 |
| `int.health.alert_after_failures` | T | 3 | 1–10 | `ten_integration_admin` | P18 |
| `int.import.undo_window_hours` | T | 24 | 1–168 | `ten_admin` | P18 |
| `int.fx.source.<ccy>` | T | RBI/FBIL (INR), ECB (EUR), CBUAE (AED), MAS (SGD) | registered sources | `ten_admin` | P18 |
| `int.fx.max_staleness_days` | G | 3 | 1–10 | platform | P18 |
| `int.reg_intel.providers` | G | none | licensed adapters | `plt_content_publisher` | P18 |
| `int.litigation_data.provider` | T | MANUAL | MANUAL or licensed adapter | `ten_admin` | P18 |
| `int.itsm.enabled` | T | false | — | `ten_integration_admin` | P18 |
| `xpt.intake.undo_window_hours` | T | 24 | 1–168 | `ten_admin` | P19 |
| `xpt.group_export.enabled` | T | true for multi-cell tenants | — | `ten_admin` | P19 |
| `xpt.cross_cell_target.require_basis` | L | true | — | — | P19 |
| `xpt.migration.max_freeze_hours` | G | 2 | 1–12 | `plt_security_officer` | P19 |
| `xpt.escrow.data.enabled` | T | false | requires P20 add-on | `ten_admin` | P19 |
| `xpt.escrow.data.frequency` | T | monthly | weekly–quarterly | `ten_admin` | P19 |
| `xpt.profile.version` | L | `ldc_tenant_v1` 1.1.0 | — | — | P19 |
| `bil.market.default` | G | IN | IN, AE, SG, GB, EU, US | `plt_finance` + checker | P20 |
| `bil.market.selector.enabled` | G | true | — | `plt_finance` | P20 |
| `bil.ai.budget.tenant_monthly` | T | plan allowance | 0–unlimited | `ten_admin` | P20 |
| `bil.ai.budget.department.<code>` | T | none | — | `ten_admin` | P20 |
| `bil.ai.at_limit_behaviour` | T | `PAUSE_NEW` | PAUSE_NEW, FINISH_RUNNING, OVERAGE | `ten_admin` | P20 |
| `bil.ai.auto_topup.cap` | T | 0 (off) | 0–plan cap | `ten_admin` | P20 |
| `bil.renewal.reminder_days` | G | 60, 30, 7 | ≥ 7 | `plt_finance` | P20 |
| `bil.cancel.retention_offer.enabled` | G | true (once, skippable) | — | `plt_finance` | P20 |
| `bil.seats.free_roles` | G | viewer, board, attester, auditor engagement, supervisor, co-op member, complainant, self-service | — | `plt_finance` + checker | P20 |
| `bil.cost_to_serve.alert_share` | G | per Appendix N §N.13 | — | `plt_finance` | P20 |
| `mkp.partners.foreign.enabled` | G | false | — | `plt_super_admin` + checker | P21 |
| `mkp.commercial.<country>.<profession>.<service_class>` | G | OFF | counsel reference required for non-OFF | `plt_super_admin` + legal checker | P21 |
| `mkp.partner.pi_cover_min.<tier>` | G | `[OWNER TO SET]` | — | `plt_super_admin` | P21 |
| `mkp.suggestions.enabled` | T | true | — | `ten_admin` | P21 |
| `mkp.independence.check.enabled` | L | true | — | — | P21 |
| `sdc.firm.enabled` | G | false until P21 provider verification live | — | `plt_super_admin` | P22 |
| `sdc.firm.max_clients.<plan>` | G | 10 / 50 / quote | — | `plt_finance` | P22 |
| `sdc.ticket.context_bundle.default` | T | ask each time | ask, always, never | `ten_admin` | P22 |
| `sdc.transparency.realtime_breakglass_alert` | T | on | — | `ten_admin` | P22 |
| `sdc.delivery.agent_runs.enabled` | T | false | requires client agent enabled | `ten_admin` | P22 |
| `sdc.followthesun.enabled` | G | false | — | `dlv_lead` | P22 |
| `web.markets.enabled` | G | IN | IN, AE, SG, UK, EU, US | `plt_web_publisher` + checker | P23 |
| `web.locale.ar.enabled` | G | false | requires reviewed copy and GCC cell | `plt_web_publisher` | P23 |
| `web.locale.en_gb.enabled`, `web.locale.en_us.enabled` | G | false | — | `plt_web_publisher` | P23 |
| `web.hc.global.enabled` | G | false until one Global Pack is PUBLISHED | — | `plt_web_publisher` | P23 |
| `hlp.hindi.maker_checker.enabled` | G | true after review | — | `plt_content_publisher` | P23 |
| `hlp.tours.first_visit` | T | on | — | `ten_admin` (per user override) | P23 |

#### Settings — v1.1 V1 explicit rows for P26 and P27

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `lit.notice.types` | G | platform rule pack | tenants add types (T); cannot loosen statutory windows | Platform content / GC | P26 |
| `lit.notice.internal_target_days_before_due` | T | 3 | 1–10 | GC | P26 |
| `lit.notice.reminder_offsets_days` | T | [7, 3, 1] | — | GC | P26 |
| `lit.triage.sla_business_days` | T | 1 | 1–3 | GC | P26 |
| `lit.approval.matrix` | G | baseline Table 17-1 | Board reference where Board-delegated | GC + CFO | P26 |
| `lit.privilege.downgrade_approver` | L | GC | — | — | P26 |
| `lit.hearings.digest_time` | T | 07:30 local | — | GC | P26 |
| `lit.hearings.lookahead_days` | T | 7 | 1–30 | GC | P26 |
| `lit.hearings.outcome_due_hours` | T | 24 | 4–72 | GC | P26 |
| `lit.limitation.reminder_offsets_days` | T | [30, 15, 7, 3, 1] | — | GC | P26 |
| `lit.limitation.rules` | G | rule pack | — | Platform content | P26 |
| `lit.assessment.frequency` | T | quarterly | quarterly/half-yearly | CFO | P26 |
| `lit.assessment.pct_guidance_bands` | T | OFF | guidance only; never drives class (§J.16) | CFO | P26 |
| `lit.risk.weights` | T | platform default | sum = 1 | GC | P26 |
| `lit.reg30.materiality_rule` | G | per Board policy | ≤ Reg 30(4) lower-of test | CS + GC | P26 |
| `lit.reg.rfi_reminder_offsets_hours` | T | [24, 4] | — | CCO | P26 |
| `lit.reg.closure_requires_verification` | L | true | — | — | P26 |
| `lit.contracts.renewal_alert_days` | T | [90, 60, 30] | — | Legal | P26 |
| `lit.contracts.legal_review_threshold` | T | ₹10,00,000 or non-standard clause | — | GC | P26 |
| `lit.contracts.obligation_extraction` | T | ON | review required | GC | P26 |
| `lit.licences.default_lead_days` | T | 60 | 15–180 | CS | P26 |
| `lit.ethics.gift_preclear_value` | T | ₹5,000 | ≥ 0 | CCO | P26 |
| `lit.ethics.gift_annual_aggregate_limit` | T | ₹25,000 per counterparty | ≥ 0 | CCO | P26 |
| `lit.ethics.campaign_month` | T | April | — | CS | P26 |
| `lit.ecourts.enabled` | T | OFF | requires licensed adapter | Admin | P26 |
| `lit.recovery_lite.enabled` | G | OFF | counsel opinion reference required | Platform + GC | P26 |
| `lit.ai.va16.autonomy_ceiling` | T | L1 | L0–L1 | GC (NN-50) | P26 |
| `lit.import.undo_hours` | T | 24 | 1–72 | GC (NN-49) | P26 |
| `esg.rulepack.version` | G | latest verified | — | Platform content | P27 |
| `esg.boundary.default` | T | operational control | operational/financial/equity share | CSO | P27 |
| `esg.gwp_set` | G | per BRSR guidance [VERIFY] | AR5/AR6 | Platform content | P27 |
| `esg.restatement.threshold_pct` | T | 5 | 1–10 | CSO | P27 |
| `esg.variance.explain_threshold_pct` | T | 20 | 5–100 | CSO | P27 |
| `esg.evidence.required_default` | T | ON | — | CSO | P27 |
| `esg.value_chain.mode` | T | voluntary | voluntary / comply-or-explain | CSO | P27 |
| `esg.value_chain.partner_threshold_pct` | G | 2 | ≥ rule | Platform content | P27 |
| `esg.value_chain.coverage_target_pct` | T | 75 | 0–100 | CSO | P27 |
| `esg.core.option` | T | assurance | assurance / assessment | CFO + CSO | P27 |
| `esg.csr.reminder_offsets_days` | T | [30, 15, 7, 3, 1] | — | CS | P27 |
| `esg.csr.admin_overhead_cap_pct` | G | 5 | rule | Platform content | P27 |
| `esg.csr.block_disbursal_without_csr1` | L | true | — | — | P27 |
| `esg.esrs_overlay.enabled` | T | OFF | requires P25 EU pack | CSO | P27 |
| `esg.ai.va17.autonomy_ceiling` | T | L1 | L0–L1 | CSO (NN-50) | P27 |
| `esg.import.undo_hours` | T | 24 | 1–72 | CSO (NN-49) | P27 |

## U.14 Compiled v1.2 module settings *(v1.2)*

*(v1.2)* Compiled by the pack lead from the v1.2 editors' registers (T1 templates and Appendix E; T3 P04 list, RAG, conversations and accountability; T4 P03 CompID generation, P05, P23; T5 business-ID registry, P01 onboarding, P06, P08, P09, P18). Where a v1.2 entry amends an earlier code, the v1.2 entry prevails.

#### T1 — Settings (v1.2; Appendix E Part A; for Appendix U)

Tier: G = global (super admin), T = tenant, L = locked by contract. `tpl.import.max_rows` / `tpl.import.dv_rows` (5,000) are raised by T4 (P03) and not repeated here. RAG windows and export defaults are P04 settings (`cmp.rag.*`, `cmp.export.*`, T3).

| Key | Tier | Default | Bounds | Changed by | Source |
|---|---|---|---|---|---|
| `tpl.template.contract_version` | L | 2.0 | major-version change needs management approval (NN-35) | — | §A.0 |
| `tpl.template.ext_max` | L | 4 | 0–4 extension columns per family | — | §A.4, LDC-TPL-052 |
| `tpl.template.outline_default` | G | COLLAPSED (list view only) | COLLAPSED / EXPANDED | super admin | §A.2 |
| `tpl.template.info_password` | G | `LDC-TPL` | any; convenience control only | super admin | §A.2, OI-P03-E12 |
| `tpl.template.format_rows` | G | 1,000 pre-formatted rows | 500–5,000 | super admin | §A.2 |
| `tpl.import.instrument_uniformity` | G | WARN | WARN / BLOCK | super admin | LDC-TPL-053 |
| `tpl.import.identical_review_text_pct` | G | 20 | 10–50 | super admin | LDC-TPL-062 |
| `tpl.import.event_other_allowed` | G | ON ("Other: <event>" accepted with warning) | ON / OFF | super admin | LDC-TPL-057 |
| `tpl.import.soft_list_unknown` | G | WARN (authority, event trigger, GOV body/timing) | WARN / BLOCK | super admin | LDC-TPL-015 |
| `tpl.import.dependent_list_strict` | G | Function BLOCK, Sub-function WARN | WARN / BLOCK each | super admin | LDC-TPL-054/055 |
| `tpl.export.sheet_per_group_max` | G | 50 | 10–100 | super admin | LDC-TPL-068 |
| `tpl.export.pdf_max_rows` | G | 5,000 | 1,000–20,000 (OI-E-V12-06) | super admin | §A.11.3 |
| `tpl.export.pdf_page` | T | A4 landscape | A4 / Letter landscape | `ten_admin` | §A.11.1 |
| `tpl.export.csv_bom` | G | ON | ON / OFF | super admin | §A.11.1 |
| `tpl.export.risk_type_grouping` | T | PRIMARY (first Risk Type) | PRIMARY / EVERY | `ten_admin`; user per export | §A.11.2 |
| `tpl.export.rag_fills` | L | Red F8696B · Amber FFC000 · Green 63BE7B · Grey BFBFBF · Blue 9BC2E6, black text | fixed (contrast, Appendix C §C.8.1A) | — | §A.2, §A.12 |
| `cfg.tenant_vocab_values` (functions, sub-functions) | T | none | add / relabel only; canonical codes kept | `ten_admin` | §A.6 |

#### T3 — Settings (v1.2; P04 §9; for Appendix U)

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `cmp.list.default_columns` | T | 9 list columns + Next Due, Days to Due, RAG | CompID, Question, Status, Next Due always visible (G floor) | `ten_admin` |
| `cmp.list.default_sort` | T | RAG severity ↓, Days to Due ↑, Risk ↓ | ≤ 4 keys | `ten_admin`; user per view |
| `cmp.list.max_group_levels` | G | 3 | 1–3 | super admin |
| `cmp.rag.rules` | G floor + T | windows per P04 FR-P04-230 (Immediately 2/3 d; ≤ monthly 3/7 d; quarterly+ 7/30 d; event-based 25 %/50 % remaining) | tenant may only widen (L floor) | `ten_cco` |
| `cmp.rag.high_risk_widen_pct` | T | 50 | 50–100 | `ten_cco` |
| `cmp.rag.internal_basis` | T | STATUTORY | STATUTORY / INTERNAL for internal reporting; Red-overdue always statutory (NN-33) | `ten_cco` |
| `cmp.rag.sweep_minutes` | G | 60 | 15–60 | super admin |
| `cmp.predict.enabled` | T | ON (auto-off < 3 months history) | — | `ten_cco` |
| `cmp.predict.threshold` | T | 0.6 | 0.5–0.9 | `ten_cco` |
| `cmp.assign.accept_sla_days` | T | 2 business days | 1–5 | `ten_cco` |
| `cmp.thread.sla_days` | T | Explanation 2, Guidance 2, Query 3 (business days) | 1–10 | `ten_cco` |
| `cmp.thread.escalate_at_pct` | T | 150 | 100–300 | `ten_cco` |
| `wf.message.edit_window_minutes` | L | 5 | fixed (NN-59) | — |
| `cmp.delay_reasons` | T | seeded list (P04 FR-P04-253) | seed codes relabel-only | `ten_cco` |
| `cmp.accountability.individual_view_roles` | T | self, reporting line, CCO, HR | cannot add peers (L floor) | `ten_cco` |
| `cmp.export.default_columns` | T | 9 list columns + Next Due + RAG + Maker | — | `ten_admin` |
| `cmp.export.max_rows` | G | 100,000 | — | super admin |
| `cmp.export.background_threshold_rows` | G | 10,000 | — | super admin |
| `cmp.export.retention_days` | T | 30 | 7–90 | `ten_admin` |
| `cmp.radar.digest_time` | U (T default) | 08:30 local | quiet hours apply except floors | user |
| `cmp.radar.red_nudge_time` | U (T default) | 16:00 local | — | user |
| `cmp.radar.red_push_optin` | U | OFF (push, WhatsApp, SMS) | Red only; DLT templates; X-23 | user within tenant channel policy |
| `ai.nl_filter.languages` | G | en, hi | — | super admin |

#### T4 — Settings (v1.2; for Appendix U)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `tpl.import.max_rows` *(amended)* | L | 5,000 (was 2,000) | — (v2.0 validations rows 3–5000) | — | P03 |
| `tpl.import.dv_rows` *(amended)* | G | 5,000 (was 2,000) | 345–20,000 | super admin | P03 |
| `tpl.import.contract_versions_accepted` | G | `2.0`, `1.0-legacy` | subset; `2.0` mandatory | super admin | P03 |
| `tpl.import.legacy_v10_accept` | G | true (per family) | true/false per family | content lead | P03 |
| `tpl.import.change_status_mismatch` | G | WARN | WARN / BLOCK | content lead | P03 |
| `tpl.import.header_hash_mismatch` | G | WARN when all keys resolve | WARN / BLOCK | super admin | P03 |
| `cnt.compid.reservation_ttl_days` | G | 90 | 14–365 | content lead | P03 |
| `cnt.compid.duplicate_similarity` | G | 0.92 | 0.85–0.98 | content lead | P03 |
| `cnt.compid.seq_warn_at` | L | 9,000 | — | — | P03 |
| `cnt.compid.reuse_allowed` | L | false | — (NN-56) | — | P03 |
| `cnt.version.editorial_is_minor` | L | true | — | — | P03 |
| `ai.studio.schema_version` | L | 2.0 | — | — | P05 |
| `ai.studio.deterministic_instrument_fields` | L | true | — | — | P05 |
| `ai.studio.update_vs_new_similarity` | G | 0.90 | 0.80–0.97 | content lead | P05 |
| `ai.studio.tenant_link_platform_matches` | T | ON | ON/OFF | `ten_admin` | P05 |
| `ai.studio.guidance_columns` | G | ON | ON/OFF per family | content lead | P05 |
| `ai.studio.link_suggestions.min_confidence` | G | 0.70 | 0.50–0.95 | content lead | P05 |
| `web.hc.studio.max_questions` | G | 50 | 10–80 | super admin | P23 |
| `web.hc.studio.max_minutes_warning` | G | 12 | 5–20 | super admin | P23 |
| `web.hc.studio.wording_max_words` | G | 35 | 20–50 | content lead | P23 |
| `web.hc.studio.publish_requires_checker` | L | true | — (NN-05) | — | P23 |
| `web.hc.studio.ab_min_sessions_per_arm` | G | 300 | 100–5,000 | super admin | P23 |
| `web.hc.studio.dropoff_alert_pct` | G | 8 % per question | 3–25 % | super admin | P23 |
| `web.hc.studio.analytics_min_cohort` | L | 30 | — | — | P23 |
| `web.hc.baseline.prefill_on_conversion` | G | ON | ON/OFF | super admin | P23 |
| `web.hc.baseline.states` | L | self-declared states only | — | — | P23 |

#### T5 — Settings (v1.2; P00 §9, P01 §9.1, P06 §9, P08 §9, P18 §9; for Appendix U)

| Key | Tier | Default | Bounds | Changed by | Phase |
|---|---|---|---|---|---|
| `core.bizid.reserve_on` | G (platform) | PREVIEW | PREVIEW, SUBMIT_FOR_CHECK, PUBLISH | plt_super_admin | P00 |
| `core.bizid.platform_seq_width` | L | 4 | — | — | P00 |
| `core.bizid.tenant_seq_width` | L | 5 | — | — | P00 |
| `core.bizid.history.default_window_days` | T | 365 | 30–3650 | ten_admin, user (view) | P00 |
| `core.bizid.history.show_actor_names` | T | true | auditors/admins always see names | ten_admin | P00 |
| `core.bizid.history.export_certificate_default` | T | false | — | ten_admin | P00 |
| `core.tenant_code.editable_until_first_id` | L | true | — | — | P00/P01 |
| `onb.discovery.provider_order.company` (and `.gstin`, `.pan`, `.lei`) | G | [primary, secondary] | registered providers | plt_super_admin (+ plt_security_officer) | P01/P18 |
| `onb.discovery.timeout_ms` | G | 8000 per source / 25000 total | 3000–20000 / 10000–60000 | platform | P01 |
| `onb.cache.public_days` | G | 30 | 1–90 | platform | P01 |
| `onb.reverify.frequency` | G | monthly | weekly–quarterly | platform | P01 |
| `onb.anon.daily_runs_per_ip` | G | 3 | 1–10 | platform | P01 |
| `onb.tenant.monthly_runs` | G | 200 (trial 20) | 0–5000 | super admin per tenant | P01 |
| `onb.bulk.max_rows` | G | 500 | 1–5000 | super admin | P01 |
| `onb.signatory.method` | T | AADHAAR_ESIGN | AADHAAR_ESIGN, DSC, AUTHORITY_LETTER | ten_admin | P01 |
| `onb.directors.auto_import` | T | ON (after confirmation) | ON/OFF | ten_admin | P01 |
| `onb.abandoned.retention_days` | L | 30 | — | — | P01 |
| `onb.epfo_lookup.enabled` | G | OFF | ON/OFF | plt_super_admin after counsel sign-off (OI-P01-19) | P01 |
| `int.lookup.hedge_after_ms` | G | 4000 | 2000–8000 | plt_super_admin | P18 |
| `int.lookup.circuit.failures` / `.window_s` / `.open_s` | G | 5 / 60 / 120 | 3–20 / 30–300 / 30–900 | plt_super_admin | P18 |
| `int.lookup.raw_retention_days` | L | 30 | — | — | P18 |
| `int.registers.hold_diff_pct` | G | 5 | 1–20 | plt_content_checker | P18 |
| `int.registers.stale_after_days` | G | 7 daily / 21 weekly | 2–60 | plt_content_checker | P18 |
| `int.registers.name_match_min` | G | 0.85 | 0.70–0.98 | plt_content_checker | P18 |
| `int.api.notfound_throttle_per_min` | G | 50 | 10–500 | plt_security_officer | P18 |
| `int.events.bizid_extension` | G | true | — | plt_super_admin | P18 |
| `int.mcp.bizid_tools.enabled` | T | true (when MCP server enabled) | — | ten_integration_admin | P18 |
| `erm.list.default_columns` | T | 9 list columns + Trend, Next Review, RAG | any field keys | ten_cro | P08 |
| `erm.rag.review_amber_days` | T | 15 | 7–45 | ten_cro | P08 |
| `erm.rag.action_amber_days` | T | 14 | 7–30 | ten_cro | P08 |
| `erm.rag.red_on_outside_appetite` | T (raise_only) | Critical, High | Critical, High, Medium | ten_cro | P08 |
| `erm.conversation.explanation_sla_working_days` | T | 3 | 1–10 | ten_cro | P08 |
| `erm.export.default_format` | U | XLSX | XLSX, PDF, CSV | user | P08 |
| `erm.import.undo_window_hours` | T | 24 | 1–72 | ten_admin | P08 |
| `gov.register.default_mode` | U | REQUIREMENTS | REQUIREMENTS, RECORDS | user | P06 |
| `gov.list.default_columns` | T | 9 list columns + Next Due, RAG, Responsible Role | any field keys | ten_cs | P06 |
| `gov.rag.red_days` / `gov.rag.red_days_event` | T | 3 / 2 | 1–7 / 1–5 | ten_cs | P06 |
| `gov.rag.amber_days_filings` / `gov.rag.amber_days_annual` | T | 7 / 30 | 3–30 / 14–60 | ten_cs | P06 |
| `gov.rag.board_gap_amber_days` | T | 100 | 60–115 | ten_cs | P06 |
| `gov.rag.notice_alert_days` | T | 2 | 1–7 | ten_cs | P06 |
| `gov.conversation.explanation_sla_working_days` | T | 3 | 1–10 | ten_cs | P06 |
| `gov.import.undo_window_hours` | T | 24 | 1–72 | ten_admin | P06 |

Note for T3/lead: Appendix D §D.19.3 references `cmp.conversation.guidance_route` (default checker → department head → CCO); P04 should register it if not already present. P04 SLA defaults (2 business days) and the P06/P08 defaults above (3 working days) differ by design per domain; the lead may harmonise.

## U.15 Compiled v1.3 settings — IPB adoption *(v1.3; D-59–D-76; X-70)*

*(v1.3)* Compiled by the product-upgrade agent from master §5.6, P02 §4S, P17 §4Y, P18 §4Y, P19 §4Q, P23 §4V–§4W and P24 §4M. Column "IPB" is the IPB-07 tier (USER / ORG / PLATFORM) recorded beside the L/G/T tier (X-70; IPB-DEV-02). Every key below is registered in the P02 registry with its `hlp.cfg.*` help key before any code reads it (OP-2).

### U.15.1 Brand and public site (`brand.*`, `web.*`, `fb.*`, `mkt.*`, `msg.*`)

| Key | Tier | IPB | Type | Default | Bounds / values | Changed by | MC | Phase |
|---|---|---|---|---|---|---|---|---|
| `brand.app_name` | G | PLATFORM (ORG override with white-label entitlement) | string | LawDocsComply | 2–40 chars; claims-lint | plt_super_admin; ten_admin (white-label) | yes | P02, P23 |
| `brand.tokens.*` | G | PLATFORM; ORG within guard-rails | json | IPB-D-11 LDC values | contrast ≥ 4.5:1 text, ≥ 3:1 UI/focus | plt_super_admin; ten_admin | platform yes; tenant no | P02, P23 |
| `brand.hosts` | G | PLATFORM | string[] | lawdocscomply.com, app., console., developers. | verified hosts only | plt_super_admin | yes | P23 |
| `brand.social` | G | PLATFORM | json | {} | https URLs; allow-listed platforms | plt_content_publisher | no | P23 |
| `brand.email_identity` | G | PLATFORM | json | no-reply@lawdocscomply.com | SPF/DKIM/DMARC verified | plt_super_admin | yes | P23 |
| `brand.terminology.vidhi` | G | ORG (white-label plans) | string | Vidhi | 2–24 chars | ten_admin | yes | P02, P17 |
| `web.investors.enabled` | L → G | PLATFORM | bool | false | — | plt_super_admin + plt_legal_reviewer | yes | P23 |
| `web.blog.enabled` | G | PLATFORM | bool | true | — | plt_content_publisher | no | P23 |
| `web.blog.user_posts.enabled` | G | PLATFORM | bool | false | — | plt_super_admin + plt_content_checker | yes | P23 |
| `web.blog.user_posts.moderation_sla_days` | G | PLATFORM | int | 5 | 1–15 | plt_content_checker | no | P23 |
| `web.blog.user_posts.eligible_groups` | G | PLATFORM | enum[] | [] | tenant_authors, verified_practitioners, invited | plt_super_admin | yes | P23 |
| `web.blog.bulk_import.max_files` | G | PLATFORM | int | 200 | 1–500 | plt_super_admin | no | P23 |
| `web.vlog.enabled` | G | PLATFORM | bool | false | captions required on every item | plt_content_publisher | no | P23 |
| `web.resources.gate_default` | G | PLATFORM | enum | none | none, email_gate, login | plt_content_publisher | no | P23 |
| `web.resources.max_file_mb` | G | PLATFORM | int | 100 | 1–250 | plt_security_officer | no | P23 |
| `web.resources.review_cadence_months` | G | PLATFORM | int | 12 | 3–24 | plt_content_checker | no | P23 |
| `web.media.svg_mode` | L | PLATFORM | enum | rasterise | rasterise, sanitise_strict | — (ADR) | — | P23 |
| `web.embeds.allowlist` | L | PLATFORM | string[] | youtube-nocookie, vimeo, static maps | — | plt_security_officer (ADR) | — | P23 |
| `web.team.photo_consent_required` | L | PLATFORM | bool | true | — | — | — | P23 |
| `fb.widget.enabled` | G | PLATFORM (USER view) | bool | true | — | plt_super_admin | no | P23 |
| `fb.ideas.enabled` | G | ORG / PLATFORM | bool | true | — | ten_admin; plt_super_admin | no | P23 |
| `fb.screenshot.enabled` | G | ORG | bool | true | user-initiated; blur offered | ten_admin | no | P23 |
| `mkt.tag_manager.adapter` | G | PLATFORM | enum | none | none, gtm_web, server_side | plt_super_admin + plt_dpo | yes | P23 |
| `mkt.sensitive_routes` | L | PLATFORM | string[] | health-check answers, grievance, legal forms, all authenticated apps | — | — | — | P23 |
| `mkt.utm.capture` | G | PLATFORM | bool | true (cookieless) | — | plt_super_admin | no | P23 |
| `msg.whatsapp.enabled` | G | PLATFORM | bool | false | — | plt_super_admin | yes | P18, P23 |

### U.15.2 Policies (`pol.*`; IPB-05 §05.5 — LDC values)

| Key | Tier | IPB | Type | Default | Changed by | MC | Phase |
|---|---|---|---|---|---|---|---|
| `pol.notice_days` | G | PLATFORM | int | 30 | plt_legal_reviewer | yes | P23 |
| `pol.reconsent.terms_class_keys` | L | PLATFORM | string[] | [terms, payment_terms, ugc_terms] | plt_legal_reviewer | yes | P23 |
| `pol.reconsent.notice_class_keys` | L | PLATFORM | string[] | [privacy, ai_policy] | plt_legal_reviewer | yes | P23 |
| `pol.refusal_mode` | L | PLATFORM | enum | read_only_with_export | — | — | P23 |
| `pol.full_hindi` | G | PLATFORM | bool | false | plt_legal_reviewer (owner #9) | no | P23 |
| `pol.gdpr_annex` / `pol.ccpa_annex` | G | PLATFORM | bool | false | plt_dpo | yes | P23, P25 |
| `pol.dpa_clickwrap` | G | PLATFORM | bool | true | plt_legal_reviewer | yes | P01, P23 |
| `pol.review_cadence_months.<key>` | L | PLATFORM | int | 6 (privacy, cookie, retention, ai) / 12 | plt_legal_reviewer | no | P23 |
| `pol.refund.rule` | G | PLATFORM (per plan) | enum | full_within_window | plt_legal_reviewer | yes | P20, P23 |
| `pol.refund.window_days` | G | PLATFORM (per plan) | int | 7 | plt_legal_reviewer | yes | P20 |
| `pol.refund.timeline_days_min` / `max` | G | PLATFORM | int | 5 / 7 | plt_legal_reviewer | yes | P20 |
| `pol.trial.auto_convert` | L | PLATFORM | bool | false (D-26) | — | — | P20 |
| `pol.billing.renewal_notice_days` | G | PLATFORM | int | 7 | plt_legal_reviewer | yes | P20 |
| `pol.billing.dunning_days` / `grace_days` | G | PLATFORM | int[] / int | [3,7,14] / 14 | OH8 admin | yes | P20 |
| `pol.grievance.ack_hours` / `resolve_days` | G | PLATFORM | int | 48 / 30 | plt_grievance_officer | no | P14, P23 |
| `pol.grievance.intermediary_ack_hours` / `resolve_days` | L | PLATFORM | int | 24 / 15 | — (law) | — | P14 |
| `pol.dpa.exit_assistance_days` | G | PLATFORM (per plan) | int | 90 | plt_legal_reviewer | yes | P19 |
| `pol.dpa.subprocessor_notice_days` | L | PLATFORM | int | 30 | plt_dpo | yes | P24 |
| `pol.vdp.bounty` | G | PLATFORM | enum | none | plt_security_officer | yes | P24 |
| `pol.vdp.disclosure_days` | L | PLATFORM | int | 90 | plt_security_officer | no | P24 |
| `pol.ugc.licence` | G | PLATFORM | enum | non_exclusive_perpetual | plt_legal_reviewer | yes | P23 |
| `pol.resources.default_licence` | G | PLATFORM | enum | personal_internal | plt_legal_reviewer | no | P23 |
| `pol.dispute.odr_mandatory` | G | PLATFORM | bool | false | plt_legal_reviewer [COUNSEL] | yes | P23 |
| `pol.dispute.arbitration` | G | PLATFORM | bool | true (B2B) | plt_legal_reviewer [COUNSEL] | yes | P23 |
| `pol.liability_cap_formula` | G | PLATFORM (per plan) | string | fees_12_months | plt_legal_reviewer | yes | P20 |

### U.15.3 Settings tree, accessibility, help and tutorials (`cfg.*`, `ux.*`, `a11y.*`, `hlp.*`, `tut.*`, `ipb.about.*`)

| Key | Tier | IPB | Type | Default | Changed by | MC | Phase |
|---|---|---|---|---|---|---|---|
| `cfg.registry.require_ipb_tier` | L | PLATFORM | bool | true | — | — | P02 |
| `cfg.registry.require_help_key` | L | PLATFORM | bool | true | — | — | P02 |
| `cfg.nav.ipb_tree_order` | L | PLATFORM | bool | true | — | — | P02 |
| `ux.appearance.density` | T | USER | enum | comfortable | self | no | P02 |
| `ux.appearance.landing` | T | USER | string | role default | self | no | P02 |
| `ux.appearance.date_format` / `number_format` / `first_day` | T | USER | enum | en-IN defaults | self | no | P02 |
| `ux.simple_mode` | T | USER | bool | false | self | no | P02 |
| `a11y.text.font` | T | USER | enum | default | self | no | P23 |
| `a11y.text.size` / `spacing` | T | USER | int | 100 / 0 | self | no | P23 |
| `a11y.contrast_theme` | T | USER | enum | auto | self | no | P23 |
| `a11y.motion.reduced` | T | USER | bool | system | self | no | P23 |
| `a11y.captions.required` | L | PLATFORM | bool | true | — | — | P23 |
| `a11y.alerts.visual` | T | USER | bool | true | self | no | P23 |
| `a11y.tts.enabled` | T | USER | bool | false | self | no | P23 |
| `a11y.gov_facing` | G | ORG | bool | false | ten_admin | no | P23 |
| `hlp.key_format` | L | PLATFORM | string | `hlp.<module>.<term>` | — | — | P23 |
| `hlp.lint.enforce` | L | PLATFORM | bool | true | — | — | P23 |
| `hlp.reference_panel.enabled` | G | PLATFORM | bool | true | plt_content_publisher | no | P23 |
| `hlp.seed_target` | G | PLATFORM | int | 400 (Wave 1), 1,200 (Wave 3) | plt_content_publisher | no | P23 |
| `tut.whats_new.level` | T | ORG | enum | all | ten_admin | no | P23 |
| `tut.tours.autostart` | T | USER | bool | true | self | no | P23 |
| `tut.start_here.tenant_curated` | T | ORG | json | {} | ten_admin | no | P23 |
| `ipb.about.*` | L | USER (read) | — | computed | — | — | P02 |

### U.15.4 AI and Vidhi (`vidhi.*`, `ai.*`)

| Key | Tier | IPB | Type | Default | Changed by | MC | Phase |
|---|---|---|---|---|---|---|---|
| `vidhi.enabled` | G | ORG | bool | true | ten_admin | yes | P17 |
| `vidhi.display_name` | G | ORG (white-label) | string | alias of `brand.terminology.vidhi` | ten_admin | yes | P17 |
| `vidhi.autonomy.ceiling.<skill>` | G | ORG (tighten only; platform ceiling L) | enum | per Appendix K | ten_admin + sponsor | yes | P17 |
| `vidhi.schedules.max_per_tenant` | G | PLATFORM (per plan) | int | 200 | plt_super_admin | no | P17 |
| `vidhi.schedules.permission_recheck` | L | PLATFORM | bool | true | — | — | P17 |
| `vidhi.missions.max_steps` | G | PLATFORM | int | 50 | plt_super_admin | no | P17 |
| `vidhi.notebooks.outputs.enabled` | G | ORG | enum[] | all except quiz off-Academy | ten_admin | no | P17 |
| `vidhi.disclosure.first_use_text_key` | L | PLATFORM | string | consent.ai.first_use | — | — | P17 |
| `vidhi.memory.retention_days` | G | ORG | int | 90 | ten_admin | yes | P17 |
| `ai.provider.<key>.enabled` | L → G after verification | PLATFORM | bool | false (except `bedrock_claude_in`, `anthropic_direct`) | plt_security_officer | yes | P17 |
| `ai.provider.byok.enabled` | G | ORG | bool | false | ten_admin | yes | P17 |
| `ai.routing.residency_floor` | L | PLATFORM (per plan) | enum | IN-ZR on regulated plans | — | — | P17 |
| `ai.image.enabled` | L | PLATFORM | bool | false | — (owner #31) | — | P17 |
| `ai.image.default_adapter` | G | PLATFORM | enum | gemini_imagen | plt_super_admin | yes | P17 |
| `ai.image.review_required` | L | PLATFORM | bool | true | — | — | P17 |
| `ai.image.c2pa.required` | L | PLATFORM | bool | true | — | — | P17 |

### U.15.5 Trust, data, audit, integrations, engineering (`trust.*`, `dat.*`, `aud.*`, `int.*`, `eng.*`)

| Key | Tier | IPB | Type | Default | Changed by | MC | Phase |
|---|---|---|---|---|---|---|---|
| `trust.mirror.staleness_alert_hours` | G | PLATFORM | int | 24 | plt_security_officer | no | P24 |
| `trust.gating.default` | G | PLATFORM | enum | login | plt_security_officer | yes | P24 |
| `trust.auditor_grant.max_days` | L | PLATFORM | int | 90 | — | — | P24 |
| `trust.incidents.contractual_window_hours` | G | PLATFORM (per plan) | int | 2 (regulated) / 24 | plt_security_officer | yes | P24 |
| `trust.questionnaire.sla_working_days` | G | PLATFORM | int | 10 | plt_security_officer | no | P24 |
| `trust.ai.residency_floor` | L | PLATFORM | enum | IN-ZR (regulated plans) | — | — | P17, P24 |
| `dat.retention.floor_lock` | L | PLATFORM | bool | true | — | — | P19 |
| `dat.byo_storage.enabled` | G | ORG (per plan) | bool | plan | ten_admin | yes | P19 |
| `dat.exit.delay_days` | G | ORG | int | 30 | ten_admin | yes | P19 |
| `aud.viewer.export_signed` | L | PLATFORM | bool | true | — | — | P02 |
| `int.mc_threshold` | G | ORG | enum | egress | ten_admin | yes | P18 |
| `int.connector.vapt_max_age_months` | L | PLATFORM | int | 12 | — | — | P18 |
| `int.api.key_prefix` | L | PLATFORM | string | ldck_ | — | — | P18 |
| `int.law_register.snapshot_refresh_hours` | G | PLATFORM | int | 24 | plt_super_admin | no | P18 |
| `eng.cc_branch.plan_required` | L | PLATFORM | bool | true | — | — | P24 |
| `eng.preview.ttl_days` | G | PLATFORM | int | 7 | plt_release_manager | no | P24 |
| `eng.preview.cost_cap_month` | G | PLATFORM | money | [OWNER TO SET] | plt_release_manager | yes | P24 |
| `eng.rings.beta_min_days` | G | PLATFORM | int | 5 | plt_release_manager | no | P24 |
| `eng.release_notes.reg_tag_requires_legal` | L | PLATFORM | bool | true | — | — | P24 |
| `eng.patch_sla_days` | L | PLATFORM | json | {critical: 3, high: 7, medium: 30, low: 90} | — | — | P24 |
| `fut.*` (IPB-12 flags touching LDC; master §5.6) | L | PLATFORM | bool | per IPB-12 §12.5 | plt_release_manager + plt_security_officer (ADR) | yes | P00 |
