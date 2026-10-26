# Appendix U — Configuration Framework and Settings Catalogue (binding)

> LawDocsComply Build Prompt Pack v1.0 · 25 October 2026 · Owner: S12 (P02). Governs tiers, keys, scopes, merge rules, rule-pack and setting-pack catalogues, the canonical department catalogue and core settings. Module settings registered by each phase are compiled in §U.9. Precedence on tiers and keys: this appendix over phase files (master §precedence).

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

### U.6.1 Department codes (platform G; Excel column M maps by name or code)

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

### U.9.0 Department name → code alias map (binding for the importer, Excel column M)

The Excel family templates (Appendix E) carry 53 department names. Every name resolves to one canonical code from §U.6.1 or to one of the twelve codes added here (X-10). The importer stores the code; the tenant sees its own label (P02 FR-P02-43).

**Codes added to §U.6.1:** `CLM` Claims · `KYC` KYC & AML · `ICP` Internal Committee (POSH; sealed class, NN-13) · `INV` Investor Relations & Services · `MKT` Marketing · `PRL` Payroll · `PRD` Product & Engineering · `SRV` Surveillance · `TAX` Tax · `TRS` Trusteeship & SR Management · `UND` Underwriting · `VAL` Valuation.

| Template name (column M) | Code | Template name (column M) | Code |
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

As P02 §15; plus owner's Excel templates (column M department list: Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management) from `SAMPLE - Finance Company Regulations 2021 - Compliance Questions.xlsx` (Rough sheet, named range `IFSCA_Dept`); Multi-State Co-operative Societies (Amendment) Act 2023 [VERIFY provisions]; Companies Act 2013 ss.96, 128, 173.
