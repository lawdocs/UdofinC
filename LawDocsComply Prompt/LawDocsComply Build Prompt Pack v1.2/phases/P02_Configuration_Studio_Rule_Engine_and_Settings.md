# Phase P02 — Configuration Studio, Rule Engine and Settings

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, RLS, hash-chained audit ledger, `core.correction_entries`, feature flags, outbox, Temporal), P01 (identity, step-up authentication, role catalogue, delegations, legal-entity and department masters).
>
> **Sequencing:** P02 starts immediately after P01 and runs **in parallel with P03 onwards**. Sprint 1 freezes the settings SDK (`packages/config`), key-naming rules, the scope tree and the tier badge component; every later phase registers its settings in the P02 registry **before** reading them (NN-28, "registry before use"). P02 must be complete before P04 exits and before P20–P22 start, because pricing, marketplace and delivery settings depend on G-tier pipelines.
>
> **Binding appendices:** U (configuration framework and settings catalogue), A (workflow and state-machine conventions), C (menus, widget catalogue, settings menu), D (roles, SoD, delegation), B (DDL conventions, events, error codes). Precedence on conflict: master → 02 → Appendix G (law) → Appendix U (tiers and keys) → this phase → other appendices.
>
> **Requirements covered:** R-023, R-024, R-028, R-039, R-068, R-071, R-074, R-086, R-007 (per-entity logic as configuration), R-013 (maker-checker configuration), R-012 and R-059 (customisable dashboards), R-090 (notification templates, not Updates content).
>
> **Estimated effort:** 6 two-week sprints for a squad of 8 (configuration core 3; rule engine 2; Studio UX, designers and catalogue 3).

> **v1.1 changes (25 October 2026)**
> - Custom Registers builder with 15 templates (FR-P02-77; IMP-060)
> - Approval-chain simulation before publish; preview as role (FR-P02-78, FR-P02-79; IMP-061, IMP-062)
> - Configuration template library and entity-to-entity copy; configuration sandbox (FR-P02-80, FR-P02-81; IMP-063)
> - AI autonomy levels L0–L4 with promotion and demotion; kill-switch panel and drills (FR-P02-82, FR-P02-83; NN-50, NN-51)
> - Undo windows for all bulk/template/import configuration changes (FR-P02-84; NN-49)
> - Automation governance view; settings for P25–P28, host switches, locale and calendars; notification budget; natural-language settings assistant; configuration documentation (FR-P02-85–89)

---

## 1. Objective and business outcome

LawDocsComply is sold to hundreds of organisation types — an NBFC-Middle Layer lender in Delhi, a Tier-2 urban co-operative bank, a Rajasthan credit co-operative society, an IFSCA Finance Unit, a listed company, an LLP, an insurance broker. Each has different laws, structures, names for things and appetite for process. Regulators change rules often. This phase delivers the **Configuration Studio**: one governed place where every user type changes what it is allowed to change **without a super admin or a code release**, while legal floors, security baselines and evidence integrity stay protected.

| Outcome | Exit-gate measure |
|---|---|
| Routine changes without LawDocs staff (R-024, R-039) | A newly onboarded tenant admin can, in ≤ 30 minutes and with no LawDocs action: rename departments and functions; add a function; create two custom fields on compliance instances; change the default checker routing for one department; set an internal reminder cadence; change dashboard defaults for the CCO; brand the workspace (contrast-validated); set quiet hours — all audited and one-click reversible |
| Entity-specific logic as data (R-007) | Applying the setting pack "NBFC-ML — RBI" or "Credit co-operative society — Rajasthan" at onboarding pre-configures departments, committees, workflows, terminology, calendars, dashboards and statutory-clock rule packs in ≤ 15 minutes; switching packs shows a diff and preserves history (NN-29) |
| Legal values governed (NN-05, NN-28) | Every Governed (G) change passes maker ≠ checker, preview, citation and effective date; no Locked (L) value can be changed through any API or UI (tests `NN-28_*`) |
| Regulatory change as data | A changed statutory deadline (e.g., a revised filing due date), a new State Professional Tax slab or a new RBI return frequency can be drafted, previewed against golden cases, impact-analysed, scheduled for a future date and activated without deployment; compliance instances already generated keep their pinned version unless the propagation mode says otherwise (NN-03, NN-07) |
| Open, interim and waiting items configurable (R-039) | Tenants define their own work statuses, "waiting on" parties, reason codes, chase cadences and escalation ladders, mapped to a locked canonical status set so reports, board packs and benchmarks stay comparable; statutory clocks cannot be paused or weakened |
| Super-admin overrides are safe (D-02, R-068, R-071, R-074) | `plt_super_admin` can change any tenant T or G value, enable or hide any component or settings section, and correct tenant master data — only through a dual-approved, reason-coded Correction Entry visible to the tenant in "Changes made by LawDocs" |
| Configuration is portable | A tenant exports its configuration as a signed JSON bundle (and a human-readable XLSX) and imports it into a sandbox or a sister legal entity with a diff; L and out-of-bounds values are rejected |
| Faster administration (R-023, R-028) | Every settings page shows tier badge, current value, source scope, "who can change this", last change and "Request change"; bulk change across departments has an impact preview and a 10-minute undo window |

---

## 2. Scope (in / out)

**In scope**

- `cfg` schema, setting definitions registry, resolver SDK (`packages/config`, TypeScript, used by API, workers and web BFFs), caching and invalidation.
- Scope tree, inheritance, overrides, parent locks, merge strategies, child-direction constraints.
- Three tiers — Locked (L), Governed (G), Tenant (T) — with the decision test, badge, and change pipelines.
- Rule-pack engine (effective-dated, citable, golden cases, sandbox, impact analysis, rollback, review dates, configured fallback) — the engine that later phases use for due-date calculators, applicability predicates, statutory clocks, escalation ladders, labour and payroll parameters, GST/TDS parameters, penalty tables for the savings ledger (P20), ratio thresholds (P09) and grievance clocks (P14).
- Setting packs (entity-family presets) and adoption modes.
- Terminology dictionary; department, function and sub-function catalogue with tenant aliases, merge and split (R-086).
- Custom fields, custom status sets with canonical mapping, reason-code lists, form builder.
- Workflow designer (approval chains, routing rules, delegation, escalation, SLA policies) producing versioned workflow definitions executed by the P04 workflow engine.
- Configurable open, interim and waiting-on-others items (R-039).
- Notification template designer and channel policy (for Notifications only; Updates content belongs to P05, NN-27).
- Dashboard builder, widget catalogue registration, menu (navigation) customisation, saved-view sharing.
- Branding and theme, letterheads, report and PDF templates' non-legal parts, custom domains and email sender domains.
- Super-admin override via Correction Entries; support sessions.
- Configuration export/import, compare and diff, sandbox, Configuration Health dashboard.

**Out of scope (owned elsewhere)**

- Regulatory content (instruments, obligations, question banks) and tenant question overlays — P03 (content pipeline, not settings).
- Regulatory monitoring and the Updates feed — P05 (P02 only links regulatory-watch items to rule packs).
- Pricing catalogue values — P20 (P02 provides the G-elevated pipeline they use).
- Identity, roles and grants — P01 (P02 configures workflow participation, not privileges).
- Execution of workflows and tasks — P04 workflow engine (P02 authors the definitions).

---

## 3. Personas and permissions touched

| Role code | What they do in P02 | Limits |
|---|---|---|
| `plt_super_admin` | Platform defaults and bounds; tenant overrides via Correction Entry; emergency blocks with `plt_security_officer` | Cannot change L values; cannot approve own change; every tenant-scope action is visible to the tenant |
| `plt_content_maker` / `plt_content_checker` / `plt_content_publisher` | Author, check and publish platform rule packs (due-date calculators, applicability predicates, statutory clocks) | Maker ≠ checker ≠ publisher for `permissive` rules |
| `plt_security_officer` | Approves security-baseline G values (session length bounds, MFA policy bounds, IP allow-lists); second approver for overrides and emergency blocks | — |
| `plt_finance` | Second approver for money-affecting G-elevated values (pricing pipelines used by P20) | — |
| `plt_support` | Opens a support session (read-only by default) at tenant request | No write without a tenant grant or break-glass (NN-30) |
| `ten_admin` | All T settings for the tenant; proposes tenant G changes; applies setting packs; locks values for children | Cannot approve own G change |
| `ten_cco` | Default tenant `legal_reviewer` for tenant G changes affecting compliance clocks, routing and statuses | — |
| `ten_dept_head` | T settings delegated to the department (department aliases, function owners, reminder cadence, department dashboards) | Within department scope only |
| `ten_maker`, `ten_checker`, other users | Personal preferences (language, accessibility, digest time, quiet hours narrow-only, dashboard personalisation) | User scope only |
| `dlv_rm` | Proposes T/G changes in a retainer tenant where the tenant has granted `cfg:propose` | Never approves in the tenant (the tenant checker does, D-03) |
| `svc_vidhi` | Drafts change summaries, suggests department mappings and custom-field definitions | Never submits or approves (NN-04, NN-14) |

Permissions (Cerbos resources): `cfg_setting` (`read`, `change_t`, `propose_g`, `approve_g`, `lock`), `rule_pack` (`draft`, `submit`, `approve`, `publish`, `retire`, `adopt`, `adapt`), `cfg_pack` (`apply`, `compare`), `workflow_def` (`draft`, `publish`), `form_def`, `dashboard_layout`, `nav_override`, `branding`, `support_session`, `correction_entry` (`request`, `approve`). Full matrix: Appendix D §D.5.

---

## 4. Functional requirements

### 4A. Settings registry and resolver SDK

**FR-P02-01 — Definitions before values.** Every configurable value used anywhere in LDC has a row in `cfg.setting_definitions` before any code reads it. CI lint (`config-registry-lint`) fails a build that reads an unregistered key or registers a key without owner, tier, default, bounds (where numeric or enumerated), `allowed_scopes`, `merge_strategy`, help key and UI section.

**FR-P02-02 — Definition schema.** Each definition carries:

| Field | Meaning |
|---|---|
| `key` | `<module>.<area>.<key>` snake_case, e.g. `cmp.reminders.default_offsets_days`, `grv.sla.first_response_hours` |
| `tier` | `L`, `G`, `T`; G sub-class `legal`, `elevated` (money, privilege, security), `platform_integration` |
| `value_type` | boolean, integer, decimal (string-encoded), enum, multi-enum, duration (ISO 8601), time-window, cron, money (minor units + currency), percentage, JSON (with JSON Schema 2020-12), rich text (sanitised), colour (with contrast rule), reference (to a catalogue row) |
| `default` | Definition default (used if no scope sets a value) |
| `bounds` | min/max, allowed enum values, regex, JSON Schema; for G-legal values a `floor` and `protective_direction` (`lower` or `higher`) |
| `allowed_scopes` | subset of `platform`, `group`, `tenant`, `legal_entity`, `department`, `function`, `user` |
| `merge_strategy` | `most_specific`, `strictest`, `intersection`, `union`, `longest`, `additive` (Appendix U §U.3) |
| `child_direction` | `any`, `narrow_only`, `raise_only`, `lower_only` |
| `instance_pinned` | true if the resolved value is frozen into a compliance instance, return run, meeting or engagement when that object is created (e.g., due-date rule version) |
| `sensitivity` | `public`, `internal`, `confidential`, `secret_ref` (values stored in the vault, never in `cfg`) |
| `owner_role` | functional owner (e.g., `plt_content_publisher`, `ten_cco`) |
| `citation_required` | true for G-legal; change requests must cite an instrument/para or an LR-ID (Appendix G) |
| `fallback_kind` | `last_approved`, `platform_baseline`, `conservative_value`, `informational_only`, `indicative_label`, `flag_off`, `manual_route`, `block` |
| `ui` | section, label key, help key (`hlp.<key>`) for the "i" button, input widget, display order, advanced flag |
| `requires_restart` | always false for tenant settings (hot reload required) |
| `introduced_in` / `deprecated_in` | release versions; deprecation needs an alias or migration (NN-11) |

**FR-P02-03 — Resolver.** `config.get(key, ctx)` resolves a value for a context `{tenant, legal_entity, department, function, user, entity_family, regulator_set, as_of}` in this order (Appendix U §U.4):

1. L platform value (always wins).
2. Instance pin — when `ctx.instance` is given and the definition is `instance_pinned`, return the pinned value.
3. Active emergency block for the key.
4. Platform G rule-pack value applicable to `entity_family`, `regulator_set`, jurisdiction and `as_of`.
5. Tenant G adaptation within bounds (bounded stricter-only for protective values).
6. T value at the most specific scope with a value: user → function → department → legal entity → tenant → group.
7. Definition default.
8. Declared fallback, if steps 1–7 yield a value that is unapproved, overdue for review or depends on an unverified rule.

Every resolution returns `{value, source_scope, source_version, tier, fallback_applied}` so screens can show "Set by {scope}" and audit can record which version drove a decision.

**FR-P02-04 — Performance and caching.** Resolution p95 ≤ 2 ms from in-process cache, ≤ 15 ms cold; cache key includes tenant ID (NN-01); invalidation by outbox event `SettingChanged` within ≤ 60 s across all pods; a T change is effective within 60 s, a G change at `effective_from`.

**FR-P02-05 — SDK surfaces.** TypeScript generated types per key (codegen from the registry), React hook `useSetting(key)` for web BFFs, `@RequiresSetting` decorator for NestJS handlers, and a test helper `withSettings({...})` for unit tests. No module may read `cfg` tables directly.

### 4B. Scope tree, inheritance and locks

**FR-P02-06 — Scope tree.**

```
platform (LawDocsComply baseline; one)
 └─ group (optional; a corporate group with several tenants, e.g. a holding company and its NBFC and HFC subsidiaries)
     └─ tenant (a client organisation account)
         └─ legal_entity (each company, LLP, society, branch registration under the tenant)
             └─ department (tenant department tree; renameable)
                 └─ function (function / sub-function under a department; renameable)
                     └─ user (personal preferences only)
```

A second, orthogonal dimension — the **regulatory profile** — selects platform G rule packs and setting packs: `regulator_set` (RBI, SEBI, IFSCA, IRDAI, MCA, co-operative registrar of State X, MeitY/DPDP, MoLE/Labour, GST/Income-tax, foreign jurisdictions) × `entity_family` (Appendix E family codes, e.g. `RBI-NBFC`, `RBI-UCB`, `COOP-CCS`, `SEBI-LISTED`, `IFSCA-FCFU`, `MCA-LLP`) × `entity_attributes` (NBFC layer, UCB tier, AUM band, listed or unlisted, employee count, State). This realises the brief's hierarchy "regulator → company → department → function" (R-086): the regulator layer comes from the profile, company from tenant/legal entity, department and function from the tree.

**FR-P02-07 — Inheritance and override.** The resolved T value is the value at the most specific scope that has one; department and function trees inherit from parents. An override is allowed only if the scope is in `allowed_scopes`, the value is within bounds and the parent has not locked it; it records actor, scope, reason (mandatory for G, optional for T) and optional expiry.

**FR-P02-08 — Locked by parent.** An administrator at a parent scope may lock a T value for all children (e.g., a group locks MFA policy for all group tenants; a tenant locks the evidence-retention period for all departments). Children see "Locked by {scope} ({role}, {date})" and a **Request change** button that creates an approval item for the locker.

**FR-P02-09 — Direction constraints.** `child_direction` is enforced against the parent's resolved value: e.g., `cmp.reminders.first_reminder_days_before_due` is `raise_only` relative to the platform minimum (a department can remind earlier, never later than the floor); `notify.quiet_hours` is `narrow_only` for users.

**FR-P02-10 — Scope deletion and re-parenting.** Removing or merging a department or function re-parents its overrides after the admin confirms a diff; no override is silently dropped (pattern PAT-03 bulk preview, Appendix C §C.7).

### 4C. The three tiers (NN-28)

**FR-P02-11 — Tier semantics** (full table in Appendix U §U.2):

| Aspect | L — Locked | G — Governed | T — Tenant |
|---|---|---|---|
| What | NN rules, statutory floors that protect third parties, security baselines, evidence and audit integrity, sealed-data rules, India residency | Legal or regulatory parameters and rule packs (due-date rules, applicability predicates, statutory clocks, thresholds, penalty tables, tax parameters), money and privilege controls, vendor integration settings | Operational settings: labels, department and function names, routing within L constraints, internal SLAs above floors, reminder cadences, custom fields, templates' non-legal text, branding, dashboards, notification preferences |
| Who changes | Nobody in the product; platform release with ADR + passing `NN-*` test + approval of the Company Secretary of the LDC operating entity and the CTO | Platform values: platform content/finance/security owner with maker ≠ checker; tenant values: tenant maker → tenant checker (CCO or delegate) | Tenant admin or delegated user within scope |
| Path | Code + migration + release (P24 change classes) | `core.config_change_requests` (preview, citation, effective date, impact report, step-up) | `cfg.setting_changes` (immediate, audited); tenant may elevate any T key to "approval required" |
| Effective | Next release | `effective_from` (≥ 24 h lead for `legal` class unless `urgent_effective`) | ≤ 60 s |
| Rollback | Release revert | New change request restoring a prior version (preview waived for immediate previous version within 7 days) | One click |
| Badge | 🔒 Locked (grey) | ⚖ Governed (amber) + "approval by …" | ✎ Tenant (green) |

**FR-P02-12 — Decision test** (apply in order; first "yes" wins; full guidance Appendix U §U.2.2):

1. Does the value implement an NN rule, a statutory protection of a third party (borrower, member, employee, complainant, data principal), audit/evidence integrity, a security baseline or a sealed-data rule? → **L** (or an L floor with a bounded T/G margin).
2. Does it move money, set a price, discount, refund, payee or authority limit, or grant privilege? → **G-elevated**.
3. Does it derive from a law, regulation, direction, standard (ICSI SS, ICAI), tax rule or professional rule, or change a deadline, applicability, filing or disclosure? → **G-legal**.
4. Does it depend on an unconfirmed external fact (vendor capability, commencement notification, counsel opinion)? → **G**, flag OFF, configured fallback.
5. Is it operational, reversible and internal to the tenant? → **T**.

Tie-break: choose the higher tier. A value with a legal floor and a tenant margin is **split**: floor L or G; tenant choice above the floor is bounded T.

**FR-P02-13 — LDC worked examples** (seed in Appendix U §U.8):

| Value | Tier | Reason |
|---|---|---|
| Append-only audit ledger; corrections only by Correction Entry | L | NN-02, D-02 |
| Maker ≠ checker on the same compliance instance | L | NN-05 |
| AI output never auto-publishes | L | NN-04 |
| Grievance: RE's final reply window before the complainant may approach the RBI Ombudsman (30 days under RB-IOS 2026) | G-legal with L floor; tenant may set a **shorter** internal target (bounded T) | RB-IOS 2026 (effective 1 Jul 2026) [VERIFY clause]; NN-31 |
| CERT-In incident reporting within 6 hours of noticing | G-legal, L floor; tenant internal target may be shorter | CERT-In Directions of 28 Apr 2022, para (ii) |
| DPDP personal-data breach report to the Board (detailed report within 72 hours) | G-legal, L floor | DPDP Rules 2025, r.7 [VERIFY commencement] |
| Board meeting: minimum 4 per year, gap ≤ 120 days | G-legal (`rulepack.IN.mca.board_meetings`) | Companies Act 2013 s.173(1) |
| Board meeting notice ≥ 7 days | G-legal | s.173(3); SS-1 |
| Draft minutes circulation and finalisation timelines | G-legal (`rulepack.IN.icsi.ss1`) | SS-1 (circulation within 15 days; entry within 30 days) [VERIFY para nos.] |
| AGM within 6 months of FY end (first AGM 9 months) | G-legal | s.96(1) |
| NBFC return due dates and frequencies | G-legal (returns kernel parameters, D-05) | RBI supervisory-returns directions [VERIFY current instrument] |
| Labour Codes: register formats, PT and LWF slabs | G-legal State rule packs | Labour Codes in force 21 Nov 2025; State rules [VERIFY per State] |
| Internal reminder offsets (e.g., T-15, T-7, T-1) | T, `raise_only` against platform minimum T-3 | Operational |
| Department names, function names, aliases | T | R-086 |
| Compliance status labels | T labels over **L canonical statuses** | Comparability of reports (FR-P02-40) |
| Risk-rating scale labels and colours | T; scale size (3×3, 4×4, 5×5) T at tenant scope; mapping to canonical High/Medium/Low L | Board reporting comparability |
| Evidence retention | G-legal floor (e.g., 8 years for books of account, s.128(5); RBI record-retention directions) with `longest` merge; tenant may keep longer (bounded T) | Statutory floors |
| Pricing, discounts, promo codes | Platform G-elevated (`plt_finance` checker) | NN-16, D-21 |
| Session idle timeout | G-elevated, bounds 5–60 min; tenant may shorten | Security baseline |
| Branding colours | T, validated for WCAG 2.2 AA contrast | NN-21 |

### 4D. T-tier change pipeline

**FR-P02-14** A T change is validated (type, bounds, direction, lock, contrast, schema), written to `cfg.setting_changes` with before/after, actor, scope and optional reason, and becomes effective within 60 s. The audit ledger receives `SettingChanged` (keys and IDs only; never `secret_ref` values or personal data).

**FR-P02-15** One-click **Undo** restores the previous value (itself an audited change). A history tab per key shows every change with "Restore this version".

**FR-P02-16** A tenant may mark any T key or section as "approval required" (`cfg.tenant_controls.require_approval_keys`), which routes future changes through the G pipeline with the tenant's chosen checker. This lets conservative clients (banks, listed companies) apply four-eyes even to operational settings.

**FR-P02-17** Bulk T change (e.g., set reminder cadence for 12 departments) uses PAT-03: preview with counts and a sample, commit, per-row result, 10-minute undo window.

### 4E. G-tier change pipeline

**FR-P02-18 — Change request.** A G change creates `core.config_change_requests` with: keys and proposed values, scope, effective date, citation (instrument, para, URL, LR-ID), plain-language summary (≤ 120 words; Vidhi may draft, the maker owns it), reason, impact report, preview result and attachments.

**FR-P02-19 — Approvals.** Maker ≠ checker (L). Approvers by sub-class: G-legal platform → `plt_content_checker` then `plt_content_publisher`; G-legal tenant → tenant `ten_cco` (or a designated tenant legal reviewer); G-elevated platform money → `plt_finance`; security → `plt_security_officer`; privileged grants → two administrators. Step-up authentication (AAL2, ≤ 10 minutes) on approve.

**FR-P02-20 — Preview.** The pipeline runs the proposed and active values side by side over golden cases and, for tenant changes, over a sample of the tenant's live objects in read-only dry-run (e.g., "34 open compliance instances would get a new due date; 3 would move earlier"). Preview is side-effect-free (no outbox, fake adapters).

**FR-P02-21 — Effective dating and lead time.** `effective_from` ≥ now + 24 h for `legal` class unless `urgent_effective` (law takes effect sooner) is recorded with the platform publisher's approval; multiple future versions may queue.

**FR-P02-22 — Propagation modes** (per change): `prospective` (default; only objects created on or after the effective date), `open_items_with_notice` (dry-run list of open compliance instances, tasks to owners, tenant banner, recorded pin override), `emergency_block` (immediate protective block).

**FR-P02-23 — Expiry.** Unapproved requests expire after 14 days (T, 7–30) with notice to the maker; approvals escalate after 2 working days through the escalation ladder.

### 4F. Rule-pack engine

**FR-P02-24 — Rule pack identity.** `rulepack.<jur>.<domain>.<name>@<YYYY.N>`; `jur` ∈ `IN`, `IN-<ST>` (ISO 3166-2:IN), `IFSC`, `INTL`, ISO country codes; tenant packs `rulepack.T-<tenant>.<domain>.<name>`.

**FR-P02-25 — Rule representation.** Decision tables and decision graphs in **GoRules ZEN** JSON Decision Model (open source, MIT-licensed engine with Node bindings; decision tables, expression nodes, switch nodes) for business-readable rules; **CEL** (Common Expression Language) for small predicates embedded in settings, routing conditions and applicability filters (non-Turing-complete, sandboxed, fast). Typed parameters in `cfg.rule_params` validated by JSON Schema. Evaluation is deterministic (NN-22): no network, no clock reads except the supplied `as_of`, decimal arithmetic, pure functions. An ADR in sprint 1 confirms the choice against JSON Logic and OPA Rego; the engine sits behind `RULES_PORT` so it can be swapped.

**FR-P02-26 — Seed rule-pack domains** (detailed by owning phases; registered here):

| Domain | Example packs | Consumers |
|---|---|---|
| Due-date calculators | `IN.calendar.frequency_rules` (monthly by Nth day, quarterly by N days after quarter-end, half-yearly, annual by FY, within N days of event, before event, Indian FY Apr–Mar, IFSCA calendar), working-day adjustment (`IN.calendar.holidays` national + RBI + State + IFSC) | P03, P04, P11 |
| Applicability predicates | `IN.rbi.nbfc.applicability` (layer, type, AUM ≥ thresholds, deposit-taking, customer interface), `IN.rbi.ucb.tiers`, `IN.sebi.lodr.applicability` (top-N by market cap, SME platform), `IN.mca.company_class` (small company, listed, public above thresholds for CSR s.135, independent directors r.4, secretarial audit s.204), `IN.labour.thresholds` (employee counts per Code/State) | P03, P15, P13 |
| Statutory clocks | `IN.mca.board_meetings`, `IN.icsi.ss1`, `IN.icsi.ss2`, `IN.rbi.grievance` (RB-IOS 2026), `IN.certin.incident`, `IN.privacy.dpdp`, `IN.posh.act`, `IN.sebi.lodr.disclosure_clocks` | P04, P06, P12, P14 |
| Escalation ladders | `IN.default.escalation` (platform defaults), tenant packs | P04, P14 |
| Labour, payroll, tax | `IN.payroll.*`, `IN-<ST>.payroll.professional_tax`, `.lwf`, `IN.tax.gst`, `IN.tax.tds` | P13, P20, P11 |
| Penalties and savings | `IN.penalties.mca_additional_fees`, `IN.penalties.gst_late_fee`, `IN.penalties.rbi_monetary` (reference amounts), `IN.savings.time_standards` | P20 savings ledger |
| Ratio thresholds | `IN.rbi.nbfc.prudential` (CRAR 15%, Tier 1 floors by layer, concentration limits), `IN.rbi.ucb.prudential`, `IN.rbi.arc.prudential` | P09 |
| Risk scales | `IN.default.risk_scales` (5×5 likelihood-impact) | P08 |

**FR-P02-27 — Lifecycle.** `draft → review → approved → scheduled → active → superseded → retired`; side exits `rejected`, `withdrawn` (Appendix A §A.8). Activation requires: schema and semantic validators green; every rule cites ≥ 1 LR-ID or instrument para; source document SHA-256 on file (from P03 content library); golden suite with ≥ 1 positive and ≥ 1 negative case per rule; declared fallback; `next_review_due`.

**FR-P02-28 — Effect classes and approvals.** `protective` (blocks, warns, discloses, escalates): maker → checker. `computational` (dates, rates, thresholds): maker → checker → owning function (CCO for compliance clocks; CFO for tax; payroll compliance officer for payroll). `permissive` (enables a route, relaxes a block): maker → checker → publisher; cited rules must be `VERIFIED` and in force. `emergency_block`: publisher + security officer, immediate, post-incident review in 5 working days. Tenants cannot enable a permissive rule the platform has not activated.

**FR-P02-29 — Verification status.** Parameters carry `VERIFIED` (primary source), `SECONDARY_ONLY`, `NOT_CONFIRMED`. Protective rules may activate while `SECONDARY_ONLY`; computational rules may activate while `SECONDARY_ONLY` only with outputs labelled "indicative — under verification"; `NOT_CONFIRMED` blocks finalisation of any filing, payslip or board-pack figure that depends on it; permissive rules need `VERIFIED`.

**FR-P02-30 — Golden cases, preview and sandbox.** Golden cases (`packages/rules/fixtures/<pack>/*.json` and tenant `cfg.golden_cases`) give inputs and expected outputs. Preview diff shows changed due dates, applicability flips, clocks and amounts. Each tenant can open a configuration **sandbox** (synthetic data only, `is_synthetic = true`) to test its own packs and workflow definitions.

**FR-P02-31 — Impact analysis.** On submit and before activation, `RulePackImpactWorkflow` lists adopting tenants (auto-follow vs pinned), open compliance instances, tasks, meetings and return runs whose pinned version is superseded, future due dates that would move, dependent templates, workflows, dashboards and settings, flags whose eligibility changes, and open items closed or opened. IDs and counts only; no personal data.

**FR-P02-32 — "What changed" summary to tenants.** Required on submit: plain-language summary (≤ 120 words; English, optional Hindi), parameter diff table (old → new, unit, citation, verification), tenant action (`none`, `review_adaptation`, `move_pin`, `configure`) and tenant-specific counts. Delivered as a Notification digest to tenant admins and as a "What changed" tab on the pack. Where tenant action ≠ none, a named tenant admin acknowledges; unacknowledged items escalate to `ten_cco` after 5 working days. (Regulatory Updates themselves are P05; this is the configuration consequence of an Update.)

**FR-P02-33 — Rollback.** A new change request with a prior version's content; effects already produced (a filed return, a sent notice, a finalised payslip) are not undone automatically — the rollback report lists them and remediation is a business transaction (supplementary payslip, credit note, corrected filing).

**FR-P02-34 — Review dates and regulatory watch.** Default `next_review_due` 180 days; 90 days for `SECONDARY_ONLY`; 30 days for `volatile` packs (DPDP phases, Labour Code State rules, RBI returns transition, SEBI LODR amendments). Overdue → banner, owner dashboard red, fallback applies to new decisions. P05 regulatory-watch items carry `linked_rule_pack_ids`; when an Update is triaged as "changes a parameter", the linked packs get `next_review_due = today` and an owner task; while a review is open, a linked flag may be switched OFF but not ON.

**FR-P02-35 — Configured fallback.** Every G definition and pack declares `fallback_kind`; fallbacks are shown where used ("Using last approved value — under review"), recorded on the object (`fallback_applied`, kind, reason) and counted on Configuration Health.

**FR-P02-36 — Tenant adoption modes.** `adopt_auto_follow` (default for statutory packs), `adopt_pinned` (stay on a version for ≤ `max_pin_days`, default 90; 0 where the law binds immediately), `adapt_within_bounds` (stricter-only overlays on an allow-list), `tenant_rule` (tenant-authored pack for its own internal processes, labelled "{Tenant} rule — not reviewed by LawDocs"), and **rule challenge** (a tenant that believes a platform rule is wrong submits sources; platform responds within 10 working days). Tenants can never relax a statutory floor.

### 4G. Configurable open, interim and waiting-on-others items (R-039)

**Research conclusion.** Leading GRC platforms (ServiceNow IRM, MetricStream, OneTrust, Archer) let customers configure issue and task states, reason codes and SLA/escalation policies, but keep a fixed internal state model so that reporting, automation and audit remain reliable; statutory deadlines are modelled as separate due dates that workflow states cannot move. LDC follows this: **labels, reasons, owners, cadences and internal SLAs are configurable; the canonical lifecycle and statutory clocks are not.** Making these items customisable is appropriate because client processes differ widely (a retainer client waiting on its statutory auditor; a co-operative waiting on the Registrar; an IFSCA unit waiting on its parent's board) and regulators change expectations; making legal clocks pausable would be inappropriate because a regulator does not stop its clock when a company is waiting on a vendor.

**FR-P02-37 — Item kinds.** The configurable model covers four kinds of "not closed" items across modules:

| Kind | Examples | Configurable (T) | Locked (L) / Governed (G) |
|---|---|---|---|
| Open work item | compliance instance not started; task open; audit finding open; risk action open; grievance open | Status labels, sub-statuses, colours, default owner rules, reminder cadence, internal SLA ≥ floor | Canonical state (`open`); maker ≠ checker; due date from rule pack (G) |
| Interim item | interim compliance (e.g., application filed, approval awaited; partial board approval; interim evidence uploaded; extension sought) | Interim sub-statuses, required interim evidence types, interim review step, next-check date | Canonical state `in_progress_interim`; interim never counts as "complied" in canonical reports |
| Waiting on someone else | waiting on internal department, client (for retainer RM), regulator, statutory/internal auditor, vendor/third party, ecosystem system (Finbyx data feed), board/committee, government portal outage | Waiting-party catalogue, reason codes, expected-by date, chase cadence and channel, auto-chase templates, escalation ladder, whether the **internal SLA** pauses | Canonical state `waiting`; **statutory and regulator clocks never pause** (L); waiting beyond the statutory due date auto-escalates to the owner's department head and CCO |
| Open interpretation / content item | unclear applicability, pending counsel view, pending regulator clarification (FAQ awaited) | Tenant notes, tenant decision with rationale (tenant overlay, P03) | Platform-level open items in Appendix W with fallback (G) |

**FR-P02-38 — Waiting-on record.** Fields: `waiting_party_type` (enum above, extensible by tenant within canonical types), `waiting_party_ref` (user, department, external contact, vendor, regulator code, system connector), `reason_code` (tenant list), `requested_at`, `expected_by`, `chase_policy_id` (cadence, channels, templates, max chases), `internal_sla_paused` (boolean, only allowed if the definition permits), `statutory_clock_ref` (read-only), `last_chased_at`, `response_received_at`, `notes`. External parties receive chase emails from the tenant's sender domain with a secure upload link (P07) where configured.

**FR-P02-39 — Transitions.** Any canonical open state may move to `waiting` with a reason; `waiting → in_progress` on response or manually; auto-reminder per cadence; at `expected_by + grace` escalate per ladder; at statutory due date minus `cmp.escalation.statutory_warning_days` escalate regardless of waiting state. Every transition is audited.

**FR-P02-40 — Canonical status mapping (L).** Tenant labels map one-to-one or many-to-one onto a locked canonical set (Appendix A §A.1): `not_started`, `in_progress`, `in_progress_interim`, `waiting`, `submitted_for_review`, `returned`, `complied`, `complied_late`, `partially_complied`, `not_complied`, `not_applicable` (with reason and approver), `exempted` (with basis), `deferred_by_regulator` (with reference), `withdrawn` (instrument repealed). Board packs, regulator views, benchmarks and the savings ledger use canonical values; screens show tenant labels with the canonical meaning in the "i" tooltip.

**FR-P02-41 — Status-set designer.** Per object type (compliance instance, task, audit finding, risk action, policy review, grievance, return run, marketplace engagement), tenants define status labels, order, colours (contrast-checked), icons, required fields on entry, allowed transitions **within** the canonical graph (they may remove optional transitions, never add a transition the canonical graph forbids), and whether a status needs a checker.

### 4H. Terminology, departments and functions (R-086)

**FR-P02-42 — Canonical department catalogue (platform G).** Seed from the owner's Excel dropdown (column M) and extended for all entity families (Appendix U §U.6): Governance & Administration (incl. Secretarial); Finance, Treasury & Accounts; Legal & Litigation; IT; Information Security; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Credit; Collections & Recovery; Internal Audit; Customer Service & Grievance; Data Protection; Business / Sales & Distribution; Treasury & Investments; Actuarial (insurers); Fund Management / Investment (AMC, AIF, FME); Membership & Society Affairs (co-operatives). Each has a stable `dept_code` used by content (Excel column M), routing and exports.

**FR-P02-43 — Tenant department tree (T).** Tenants create their own tree (departments, sub-departments, functions, sub-functions) with any names, map each node to one or more canonical codes, set an owner (head) linked to an HRMS employee (P13) and a deputy, and set default maker/checker pools. Renaming never breaks references (stable IDs). Merging two departments re-maps open items with a preview; splitting asks for a mapping rule (by function, by content tag, by instrument) and previews the result. Historical records keep the department name as at the time of the event (bitemporal display: "Credit Ops (then: Operations)").

**FR-P02-44 — Content-to-department mapping.** When a content pack is adopted (P03), obligations tagged with canonical `dept_code` are assigned to the tenant node(s) mapped to that code; unmapped codes appear in an "Assign department" queue; Vidhi may suggest mappings with confidence (never auto-applies without the admin's confirmation).

**FR-P02-45 — Terminology dictionary.** Platform default terms per entity family (e.g., co-operatives: "Board" → "Managing Committee", "Director" → "Committee member", "Shareholder" → "Member", "AGM" → "Annual General Body Meeting"; LLP: "Board" → "Designated Partners", "Director" → "Designated Partner"; insurers: "Board" stays; IFSCA branches: "Board" → "Governing body of the parent / Principal Officer" where applicable) plus tenant overrides for any UI term (`cfg.terminology`). Legal terms used in statutory forms and citations are L (e.g., form names, section titles) and cannot be renamed. Terminology applies to UI labels, notifications, exports' human-readable folder names (with the canonical name in the manifest, NN-10).

### 4I. Custom fields, forms and reason codes

**FR-P02-46 — Custom fields.** Tenants add fields to compliance instances, tasks, evidence, risks, controls, audit findings, policies, committees, meetings, grievances, employees, vendors and engagements. Types: text, long text, number, decimal, currency, date, date-time, boolean, single/multi-select (tenant list), user, department, legal entity, URL, file reference, formula (CEL over other fields, read-only). Each field has label (multi-language), help text (feeds the "i" button), required-at-status, visibility and edit permissions by role, PII classification (`none`, `personal`, `sensitive`, `sealed`), searchable flag, export column name. Maximum 100 custom fields per object type per tenant (G-elevated bound). Custom fields are included in exports and APIs automatically (NN-10).

**FR-P02-47 — Form builder.** Drag-and-drop layout of standard and custom fields into sections and tabs; conditional visibility (CEL); field-level validation; preview as role; versioned (published forms pinned to records created under them); accessibility checks at publish (labels, order, error association).

**FR-P02-48 — Reason-code lists.** Tenant-managed lists for: return-for-rework, not applicable, waiting, extension, exception, risk acceptance, policy deviation, grievance closure (within regulator categories), task cancellation. Lists carry codes for analytics; some lists have L minimum entries (e.g., "Not applicable" requires one of: entity type excluded, threshold not met, activity not undertaken, exemption granted, other with text).

### 4J. Workflow designer

**FR-P02-49 — Workflow definitions.** A visual designer produces versioned definitions (`cfg.workflow_defs`, `cfg.workflow_def_versions`) executed by the P04 engine on Temporal. Building blocks: start trigger (object created, status reached, schedule, event), steps (task, approval, review, parallel group, conditional branch, wait-for-event, wait-until, notification, call-AI-draft, webhook-out via P18), assignment rules (named user, role in department, department head, function owner, round-robin pool, least-loaded, from field, from HRMS reporting line), SLAs, escalation ladder, delegation behaviour, end states.

**FR-P02-50 — Locked workflow invariants (L).** Validator refuses publication if: an approval step can be completed by the maker of the same object (NN-05); a High-risk compliance instance has no checker step; an AI step can complete an approval or publish (NN-04, NN-14); a step bypasses evidence requirement for statuses that require evidence; a statutory clock is attached to a pausable timer; a sealed object (POSH, whistle-blower) routes to a role outside its sealed audience (NN-13).

**FR-P02-51 — Approval chains.** Serial, parallel (all/any/quorum N of M), conditional by risk rating, department, legal entity, amount band, instrument, regulator; optional auditor step (`ten_internal_auditor` sample review); board/committee step that links to P06 meeting agenda instead of a person. Retainer mode (D-03): `dlv_rm` may be maker; checker must be a tenant user (`ten_checker` or above) — the validator enforces it when `engagement.retainer = true`.

**FR-P02-52 — Delegation.** Per user, per source, time-bound (≤ 90 days), depth 1; delegate must already hold the permission; delegate cannot approve an item they made; actions recorded "by {delegate} on behalf of {delegator}". Approved leave in HRMS prompts the user to set delegation; never set silently.

**FR-P02-53 — SLA policies and escalation ladders.** Business-hour calendars per legal entity (State holidays), SLA targets per object type and priority (≥ L/G floors), escalation levels L0–L3 with times and recipients (owner → department head → CCO → CEO/Board committee), notification templates per level. Level 3 is mandatory for statutory clocks.

**FR-P02-54 — Versioning and migration.** Publishing a new workflow version never changes in-flight instances unless the admin selects "migrate open instances" — which shows a dry-run mapping of current steps to new steps and records the migration per instance.

**FR-P02-55 — Templates gallery.** Seeded workflow templates per entity family (e.g., "RBI compliance — maker/checker/CCO", "Policy approval — owner → CCO → committee → Board", "Board meeting preparation", "Grievance — L1 support → GRO → IO (where applicable)", "Return filing — preparer → reviewer → authorised signatory → upload evidence", "Retainer delivery — RM maker → client checker"). Tenants clone and adapt.

### 4K. Notification templates and channel policy

**FR-P02-56** Templates for Notifications (work events) per event type, channel (in-app, email, push, SMS via DLT-registered templates, WhatsApp Business templates, Microsoft Teams/Slack connector), language and audience; variables from a whitelisted schema per event (never document text or sealed content); preview with sample data; tenant branding; plain-text alternative; accessibility lint (no information by colour only, descriptive link text).

**FR-P02-57** Channel policy: priority mapping (P1–P4) to channels, digest times, quiet hours (tenant default; user narrow-only), de-duplication window, escalation channels. Regulatory **Updates** are configured in P05 (separate model, NN-27); P02 only exposes the user's Updates digest preferences in the same preference screen with a clear separation.

### 4L. Dashboards, widgets, menus and saved views

**FR-P02-58 — Widget catalogue registration.** Each module registers widgets (`cfg.widget_catalogue`): code, title key, data source API, roles permitted, parameters, default size, drill-down target, export (PNG/CSV/XLSX), accessible table alternative, refresh interval. Catalogue in Appendix C §C.6.1.

**FR-P02-59 — Dashboard builder.** Role default layouts (Appendix C §C.6.2) set at platform, adapted by tenant per role or department, personalised by users (add, remove, resize, reorder, filter) except **mandatory widgets** (bold in Appendix C), which cannot be hidden (e.g., "Overdue statutory items" for CCO and Board). Dashboards can be shared as read-only snapshots to the board pack (P06).

**FR-P02-60 — Menu customisation.** Tenants may hide modules they do not license or use, reorder top-level items, rename labels (terminology dictionary), pin shortcuts, and set a landing page per role. L items cannot be hidden: Work Inbox, Updates, Help, Profile, Settings entry for admins, Audit trail viewer for auditors, "Changes made by LawDocs". Menus are data in `cfg.nav_items` and `cfg.nav_overrides`; entitlements (P20) hide unlicensed modules automatically, with an "Explore" entry showing locked modules (upsell, switchable by tenant).

**FR-P02-61 — Saved views.** Users save filters, columns and sort on any list; share with a role, department or named users; tenant admins publish "official" views (e.g., "Board view — RBI overdue").

### 4M. Branding and theme

**FR-P02-62** Logo (SVG/PNG), primary and accent colours (validated: text contrast ≥ 4.5:1, UI ≥ 3:1), light/dark/high-contrast themes, density (comfortable/compact), font scale default, letterhead (header/footer for exports), PDF cover pages, email sender name and domain (SPF, DKIM, DMARC verification), custom subdomain (`<tenant>.lawdocscomply.com`) and custom domain with managed TLS, favicon, login page message. Defaults from the LDC design tokens (Appendix C §C.8). Branding never changes legal disclaimers or statutory form layouts (L).

### 4N. Setting packs (entity-family presets)

**FR-P02-63** A setting pack bundles T and tenant-G defaults for an entity family: department tree, functions, committees (with P06 templates), workflows, status sets, terminology, dashboards per role, calendar defaults (FY, holiday calendars by State), reminder cadences, notification policies, default reports. Seed packs (Appendix U §U.7): `RBI-NBFC-BL`, `RBI-NBFC-ML`, `RBI-NBFC-UL`, `RBI-NBFC-ICC`, `RBI-HFC`, `RBI-MFI`, `RBI-CIC`, `RBI-ARC`, `RBI-SCB`, `RBI-SFB`, `RBI-UCB-T1…T4`, `COOP-CCS-<State>`, `COOP-MSCS`, `COOP-GEN`, `IFSCA-FCFU`, `IFSCA-FME`, `IFSCA-IBU`, `SEBI-LISTED-MAIN`, `SEBI-LISTED-SME`, `SEBI-MF-AMC`, `SEBI-AIF-MANAGER`, `SEBI-REIT-INVIT-MANAGER`, `SEBI-INTERMEDIARY`, `IRDAI-INSURER`, `IRDAI-BROKER`, `IRDAI-CORP-AGENT`, `MCA-PVT`, `MCA-PUBLIC`, `MCA-SMALL`, `MCA-OPC`, `MCA-SEC8`, `MCA-LLP`, `STANDALONE-HRMS-LABOUR`, `STANDALONE-DATA-PRIVACY`.

**FR-P02-64** Applying a pack shows a diff against current configuration, applies selected sections, records `cfg.pack_adoptions` with version; pack updates are offered as a diff ("Pack v1.3 adds the IT Strategy Committee to NBFC-ML; apply?"); tenant changes made after adoption are preserved.

### 4O. Super-admin overrides via Correction Entries (D-02, R-068, R-071, R-074)

**FR-P02-65 — Scope of override.** `plt_super_admin` may, for any tenant: change any T or tenant-G value; enable, disable or hide any module, component, settings section or feature for that tenant; extend trials; change entitlements (with P20); correct tenant master data (name, CIN, PAN, GSTIN, address, entity family, regulator profile, legal entities); correct a compliance record's dates, status or evidence linkage; replace a document version; annotate the audit trail.

**FR-P02-66 — Mechanism (L).** Every such action is a **Correction Entry** (`core.correction_entries`, P00) with: target object and field(s), old value (sealed copy), new value, `effective_at` (which may be in the past — back-dating), true `recorded_at`, reason code (`client_request`, `data_error`, `migration_fix`, `legal_order`, `security_incident`, `commercial`), free-text reason (≥ 20 characters), evidence attachment (client email or ticket reference), requester and approver (two distinct platform users; approver `plt_super_admin` or `plt_security_officer`), step-up for both. The original record is never mutated; readers see the corrected value with a "Corrected" chip; the tenant sees the entry in **Settings → Account → Changes made by LawDocs** (SCR-CFG-28) and receives a Notification to `ten_admin`; auditors see both values.

**FR-P02-67 — Emergency override.** Where a client is locked out or a security incident requires immediate action, a single super admin may apply an emergency override with `plt_security_officer` approval within 24 hours; un-approved emergency overrides auto-revert after 24 hours where reversible and raise a P1 alert.

**FR-P02-68 — Not overridable.** L values; NN tests; the audit ledger's existence or ordering; sealed content (POSH, whistle-blower) — super admin can restore access for the tenant's own sealed audience but cannot read the content.

### 4P. Export, import, compare, sandbox, health

**FR-P02-69** Configuration export: signed JSON bundle (`ldc-config-1.0`, JWS) and XLSX (one sheet per section, human-readable) of all T and tenant-G values, department tree, status sets, forms, workflows, dashboards, terminology and adopted packs. Included automatically in LDC-EXPORT-1.0 (P19, folder `00 Start Here/Configuration`).

**FR-P02-70** Import into the same tenant (restore), a sandbox or a sister legal entity: dry-run diff; L and out-of-bounds values rejected with reasons; G values become change requests; T values apply after confirmation.

**FR-P02-71** Compare two scopes or two points in time (e.g., "Department A vs B", "today vs 1 April"), with filter by tier and module.

**FR-P02-72** Configuration Health dashboard (SCR-CFG-24): fallbacks in force, overdue reviews, pinned packs near `max_pin_days`, unmapped departments, workflows without a checker for High-risk items (should be zero), unacknowledged "what changed" items, settings changed in last 30 days, contrast or accessibility failures in custom forms.

### 4Q. Faster, safer administration

**FR-P02-73** Settings search across all keys by label, key, help text and value; result shows tier badge, current value and "who can change this".

**FR-P02-74** Every setting row shows: label with "i" help, tier badge, current value, source scope ("Set by Credit department"), last changed by/when, inherited/override indicator, lock indicator, actions (Change, Reset to inherited, History, Request change).

**FR-P02-75** Onboarding checklist for admins (P01 hand-off): apply setting pack → map departments → assign heads → confirm workflows → set reminders → brand → invite users; progress saved; each step deep-links to its settings page.

**FR-P02-76** Keyboard: `g s` opens Settings; `/` focuses settings search; command palette entries "Change reminder cadence", "Rename department", "Add custom field", "Apply setting pack" (Appendix C §C.4).

### 4R. v1.1 additions — custom registers, simulation, templates, autonomy and kill switches *(v1.1)*

**FR-P02-77 — Custom Registers builder (IMP-060).** Tenants build their own registers without code (e.g., insurance policies held, bank accounts and signatories, trademarks, vehicles, branch licences, gifts and hospitality if P26 is not licensed): fields (all custom-field types of FR-P02-46 plus attachments, person, legal entity, location, currency, date with reminder), optional workflow (draft → review → approved → expired) with SoD guard-rails, roles per register, draft/live versions with a build audit log, list and calendar views, reminders on date fields (feeding P04 calendar as internal items), Excel import (as a change batch with undo, NN-49) and export. Publishing a register auto-registers its export mapping (folder `17 Documents Library/Custom Registers/<register name>/` in LDC-EXPORT, NN-10). Limits per plan (Appendix N). Platform templates: 15 common registers seeded (bank accounts & signatories, insurance policies, licences & registrations (until P26), properties & leases, IP, POA register, seal/stamp register, visitor/gift register, key contracts (until P26), branch master, vehicle register, IT assets, data-processing vendors, outsourcing arrangements (until P12), board evaluations).

**FR-P02-78 — Approval-chain simulation (IMP-061).** Before a new workflow version or approval matrix is published, "Simulate" replays the last N days (default 30) of real items through the proposed chain in a read-only sandbox and reports: items that would route differently, approvers who would receive more than X items per day, SoD conflicts, items that would breach SLA, and delegations that would fail. The report is attached to the change (T or G) and must be viewed before "Publish" is enabled.

**FR-P02-79 — Per-role menu preview (IMP-062).** FR-P02-60 gains "Preview as role": the admin sees the left rail, home dashboard and command-palette entries exactly as a chosen role (and optionally a named user) would, before saving.

**FR-P02-80 — Configuration templates across entities and a template library (IMP-063).** `cfg.config_templates` (P00 FR-P00-68): (a) **copy from entity A to entity B** with a section-by-section diff, applied atomically as one change batch (undo 24 h); (b) a **template library** of common set-ups maintained by the platform content team — "NBFC-ML standard", "NBFC-BL lean", "Listed company — main board", "Private company — small", "Credit co-operative — State Act", "Insurance broker", "IFSCA FC/FU", "Group with subsidiaries" — each bundling departments, approval matrix, SLA policies, notification policy, dashboards, menus, reason codes and custom registers; (c) tenants may save their own templates and share them across their group; (d) LawDocs delivery leads may offer a template to a client (maker only; client admin applies — NN-43).

**FR-P02-81 — Sandbox preview tenant.** A tenant admin can open a **configuration sandbox** (clone of configuration and synthetic sample items; no business data), try settings, workflows, templates, rule-pack versions and setting packs, run the simulation of FR-P02-78, and promote the tested bundle to live as one change request (T or G as applicable). Sandboxes inherit the provider-routing guard (no live emails, SMS, eSign or AI calls with personal data).

**FR-P02-82 — AI autonomy levels (NN-50; Appendix AA §AA.3).** Definitions (L): **L0** off; **L1** suggest (read and answer, no drafts saved without a click); **L2** draft (creates drafts, tasks and proposals that a human must approve); **L3** act-with-approval-gate (executes pre-approved internal actions such as creating reminders, assigning tasks within a rule, compiling packs — each with a reversible change batch and notification); **L4** act-autonomously-within-mission (runs scheduled missions end to end inside the tenant, still never approving, signing, filing, paying, publishing or sending externally — NN-14, NN-47). Settings (keys owned by P17: `ai.autonomy.platform_ceiling.<agent>`, `ai.autonomy.tenant_ceiling`, `ai.autonomy.agent.<agent>`, `ai.autonomy.skill.<skill>`, `ai.autonomy.sealed_contexts`) exist at platform (ceiling), tenant, agent, skill, mission and user scope; the Studio is their single editing surface; the **effective level is the minimum** across scopes and the sealed-context rule (L0 for sealed classes). Promotion above L2 is a Governed change with evidence (evaluation pass rate, error log, sponsor approval); demotion is automatic on triggers (evaluation regression, incident, kill switch, sponsor change) and is immediate. Tools above the effective level are not exposed to the model.

**FR-P02-83 — Kill switches in the Studio (NN-51).** Tenant admins and AI Officers (`ten_kmp` AIO) see a kill-switch panel (tenant, agent, skill, mission, connector) with the current state, last drill date and a "Run drill" action; platform switches (provider, model, platform) are in the console. Every switch change is audited; propagation is verified (≤ 60 s) and shown. *(v1.1, X1)* Drills: platform and provider/route switches are drilled quarterly by LawDocsComply for all tenants; tenant-level drills are mandatory at least every 90 days for Enterprise tenants and optional for other plans (`ai.killswitch.drill_frequency_days`); an overdue mandatory drill raises a Work Inbox item to the AI Officer and `ten_admin`.

**FR-P02-84 — Undo windows everywhere (NN-49).** Bulk T changes (FR-P02-17), template and setting-pack applications (FR-P02-64, FR-P02-80), imports of configuration (FR-P02-70) and department merges (5.7) write a change batch (P00 FR-P00-64); the Studio's "Recent changes" list offers Undo until the window closes. The window per batch kind is a G setting (default 24 h).

**FR-P02-85 — Automation governance view (G5 gap).** One screen lists every automation in the tenant — workflow automations, scheduled reports, recurring tasks, Vidhi missions, connector syncs, reminder ladders — with owner, trigger, last run, success rate, next run, autonomy level, kill switch and "pause". Paused automations surface in the Configuration Health dashboard.

**FR-P02-86 — Settings for new modules, regions and jurisdictions.** Register definitions for P25 (jurisdiction packs, partner network, locale), P26 (`lit.*`, `clm.*`), P27 (`esg.*`), P28 (`rpt.*`), host switches (`ral.icaap.host`, `aud.host.mode`, `coop.sor.members`, `ral.stress.fx_mode`) and per-legal-entity locale settings: timezone, fiscal-year start, working week, holiday calendars (country, State, regulator, exchange), currency and number formats, language. A foreign legal entity uses its jurisdiction's defaults from the pack (Appendix Y).

**FR-P02-87 — Notification budget (IMP-040, IMP-041).** Channel policy (FR-P02-57) gains a per-user daily **notification budget** (default 15 interruptive notifications; above that, items roll into the next digest) and per-type batching rules; P1 items (statutory due within 48 h, security, breach clocks) are never budgeted. Users can tighten, not loosen, the tenant budget.

**FR-P02-88 — "Tell me what to change" (IMP-059 extended).** Settings search (FR-P02-73) accepts natural language ("send reminders 5 days earlier for RBI returns"); Vidhi (L2) maps the request to candidate keys, shows the current values and a proposed change as a draft change request; the admin confirms. Nothing changes without the click.

**FR-P02-89 — Configuration documentation.** "Explain my configuration" generates a readable PDF/DOCX of the tenant's configuration (departments, approval matrix, SLAs, autonomy levels, custom registers, overrides by LawDocs) for auditors and inspections, and a diff report between two dates.

---

## 5. Workflows and state machines

Canonical definitions are in Appendix A; this section gives the P02-specific flows.

### 5.1 T-tier change

```
validate(type, bounds, child_direction, parent_lock, contrast/schema)
  ├─ fail → LDC-CFG-001..006 (field-level error, value kept in form)
  └─ pass → if key ∈ tenant.require_approval_keys → go to 5.2 (tenant G path)
            else write cfg.setting_changes (before, after, actor, scope, reason?)
                 emit SettingChanged → cache invalidation (≤ 60 s)
                 toast "Saved · Undo" (10 s) + history entry
```

### 5.2 G-tier change request

States: `draft → submitted → in_review → approved → scheduled → active` | `rejected` | `withdrawn` | `expired`.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| draft | submit | Validators green; citation present if `citation_required`; summary present; preview run ≤ 24 h old; effective date ≥ lead time | submitted | Inbox approval item to eligible checkers |
| submitted | open | Checker eligible (permission, not maker, not delegated from maker) | in_review | — |
| in_review | approve | Step-up AAL2 ≤ 10 min; all approval steps met | approved | Audit; Notification to maker |
| in_review | reject / request changes | Reason ≥ 20 chars | rejected / draft | Notification |
| approved | schedule | `effective_from` > now | scheduled | `ConfigActivationWorkflow` timer |
| approved | activate (immediate) | `effective_from` ≤ now and `urgent_effective` recorded | active | — |
| scheduled | activate | Validators re-run green | active | Previous version superseded; cache bust; propagation per mode |
| any non-terminal | withdraw | Maker | withdrawn | Timers cancelled |
| submitted / in_review | 14 days elapse | — | expired | Maker notified |

### 5.3 Rule-pack version

As 5.2 with the additional steps: golden-suite run (must be green or every mismatch accepted with reason), impact analysis attached, publisher approval for `permissive`, "what changed" summary generated, tenant acknowledgements tracked after activation (Appendix A §A.8).

### 5.4 Setting-pack adoption

`selected → diff_previewed → sections_chosen → applied → (pack_update_available → diff_previewed → applied | declined)`. Applying is a T bulk change (G sections create change requests).

### 5.5 Correction Entry (super-admin override)

`requested → (approved | rejected) → applied → tenant_notified`; emergency path `applied_emergency → (ratified | auto_reverted)` within 24 h. Guards: requester ≠ approver; both step-up; reason code; evidence reference. Effects: target read model shows corrected value; original sealed; ledger event `CorrectionEntryApplied` (Appendix A §A.5).

### 5.6 Waiting-on item

```
any open canonical state --set_waiting(party, reason, expected_by, chase_policy)--> waiting
waiting --response_received | manual_resume--> in_progress
waiting --chase_timer--> waiting (chase_count += 1; send chase template)
waiting --expected_by + grace--> waiting (escalate L1)
any state --statutory_due - warning_days--> (escalate to dept head + CCO; banner "Statutory deadline approaching while waiting on {party}")
```

Internal SLA pauses only if `definition.allow_internal_sla_pause = true` and the reason is in the pausable list; statutory clock never pauses (`NN-33_statutory_clock_never_pauses`).

### 5.7 Department merge / split

`draft_mapping → preview (counts per object type, owners affected, workflows affected) → confirm → applying (job) → applied` with per-object re-assignment records; history keeps old department names; rollback available until any re-assigned item changes state.

### 5.8 Workflow definition version

`draft → validated → published → (superseded)`; validator enforces FR-P02-50 invariants; publishing offers "apply to new objects only" (default) or "migrate open instances" with dry-run mapping.

### 5.9 Resolver with fallback (pseudo-code)

```ts
function resolve(key, ctx): Resolved {
  const def = registry.get(key) ?? throw LDC_CFG_UNREGISTERED_KEY;
  if (def.tier === 'L') return lockedValue(def);
  if (ctx.instance && def.instancePinned) {
    const pin = pins.get(ctx.instance, key); if (pin) return pin;
  }
  const block = emergencyBlocks.active(key, ctx); if (block) return block;
  let v = rulePacks.value(key, ctx.profile, ctx.asOf);        // platform G
  v = tenantAdaptation(key, ctx, v, def.bounds, def.protectiveDirection) ?? v; // tenant G
  const t = mostSpecificTValue(key, ctx, def.allowedScopes);  // user→function→dept→LE→tenant→group
  v = merge(def.mergeStrategy, v, t, def.childDirection);
  v ??= def.default;
  if (isUnapproved(v) || reviewOverdue(v) || dependsOnUnverified(v))
     return applyFallback(def.fallbackKind, key, ctx, v);    // records fallback_applied
  return v;
}
```

### 5.10 Autonomy promotion and demotion *(v1.1)*

`requested (sponsor + evidence: eval pass ≥ threshold, error log, scope) → reviewed (AIO or ten_admin; maker ≠ checker) → approved (effective_from) → active → demoted (trigger: eval regression, incident, kill switch, sponsor change; immediate) | expired (review date)`. Demotion never needs approval; promotion always does (G).

### 5.11 Custom register version *(v1.1)*

`draft → tested (sandbox) → published (vN) → superseded (vN+1)`; records created under vN keep their schema; a migration map converts records when fields change (expand–contract; NN-11).

---

## 6. Screens and UX

All screens live under **Settings** (tenant: `/settings/*`; console: `/console/config/*`). Menu tree in Appendix C §C.3.6. Every screen follows Appendix C patterns: tier badges, "i" help, empty/error/loading states, keyboard access, ≤ 3 clicks from Settings home to any value.

| Screen ID | Name | Path | Roles | Notes |
|---|---|---|---|---|
| SCR-CFG-01 | Settings home | `/settings` | all (sections trimmed by role) | Search bar, sections grid, recent changes, pending approvals count, Configuration Health summary for admins |
| SCR-CFG-02 | Settings section page | `/settings/{section}` | per section | Rows per FR-P02-74; filters by tier and "changed from default" |
| SCR-CFG-03 | Setting detail and history | drawer | — | Value editor, inheritance chain visualiser, history with restore, "who can change", linked help |
| SCR-CFG-04 | Change request composer | `/settings/requests/new` | `ten_admin`, platform roles | Diff, citation picker (Appendix G LR-IDs / P03 instrument para), effective date, propagation mode, summary (Vidhi draft), preview button |
| SCR-CFG-05 | Change request review | Work Inbox decision panel | checkers | Diff, preview result, impact report, citations, approve/reject with step-up |
| SCR-CFG-06 | Rule packs catalogue | `/settings/rules` (tenant), `/console/config/rule-packs` | admins, content roles | Adopted / available / pinned; versions; review due; "what changed" |
| SCR-CFG-07 | Rule-pack editor | console | content roles | Decision-table editor (ZEN JDM), parameter forms, golden cases, run preview |
| SCR-CFG-08 | Golden cases and sandbox runner | console / tenant sandbox | content roles, `ten_admin` | Inputs → expected vs actual diff |
| SCR-CFG-09 | Impact analysis report | linked | approvers | Counts by tenant, object type, date shift histogram |
| SCR-CFG-10 | Setting packs | `/settings/packs` | `ten_admin` | Apply, compare, update diff |
| SCR-CFG-11 | Department & function tree | `/settings/organisation/departments` | `ten_admin`, `ten_dept_head` (own) | Tree editor, canonical mapping, heads/deputies from HRMS, merge/split wizard |
| SCR-CFG-12 | Terminology | `/settings/organisation/terminology` | `ten_admin` | Term, default, tenant term, where used, preview |
| SCR-CFG-13 | Status sets | `/settings/workflow/statuses` | `ten_admin` | Per object type; canonical mapping graph |
| SCR-CFG-14 | Waiting-on parties & chase policies | `/settings/workflow/waiting` | `ten_admin`, `ten_cco` | Party catalogue, reason codes, cadences, templates, pausable flags |
| SCR-CFG-15 | Reason-code lists | `/settings/workflow/reasons` | `ten_admin` | Lists with minimum L entries shown locked |
| SCR-CFG-16 | Custom fields | `/settings/data/custom-fields` | `ten_admin` | Per object type; PII class; usage count |
| SCR-CFG-17 | Form builder | `/settings/data/forms` | `ten_admin` | Drag-drop, conditional logic, preview as role, accessibility lint |
| SCR-CFG-18 | Workflow designer | `/settings/workflow/designer` | `ten_admin`, `ten_cco` | Canvas with keyboard alternative ("Add step after…" menu), validator panel, versions |
| SCR-CFG-19 | SLA policies & escalation ladders | `/settings/workflow/sla` | `ten_admin`, `ten_cco` | Calendars, floors shown, ladder editor |
| SCR-CFG-20 | Delegations | `/settings/me/delegations` and admin view | all users / admins | Create, end, history |
| SCR-CFG-21 | Notification templates & channel policy | `/settings/notifications` | `ten_admin` | Template editor with variables, preview, DLT/WhatsApp template IDs |
| SCR-CFG-22 | Dashboard defaults & builder | `/settings/dashboards` and in-place "Customise" | `ten_admin`, users | Role layouts, mandatory widgets locked |
| SCR-CFG-23 | Menu & landing pages | `/settings/navigation` | `ten_admin` | Hide/reorder/rename, locked items, per-role landing |
| SCR-CFG-24 | Configuration Health | `/settings/health` | `ten_admin`, `ten_cco`, platform | Per FR-P02-72 |
| SCR-CFG-25 | Branding & domains | `/settings/branding` | `ten_admin` | Logo, colours with live contrast checker, sender domain DNS checks |
| SCR-CFG-26 | Export / import / compare | `/settings/transfer` | `ten_admin` | Bundle download, import wizard with dry-run, compare tool |
| SCR-CFG-27 | Personal preferences | `/settings/me` | all | Language, accessibility (font scale, reduced motion, high contrast, screen-reader hints), digest time, quiet hours, Updates digest (separate block) |
| SCR-CFG-28 | Changes made by LawDocs | `/settings/account/lawdocs-changes` | `ten_admin`, `ten_cco`, auditors | Correction Entries list with old/new, reason, approver, date; export |
| SCR-CFG-29 | Tenant override console | `/console/tenants/{id}/config` | `plt_super_admin` | Any tenant setting/section/component; every save opens a Correction Entry |
| SCR-CFG-30 | Correction Entry review | console inbox | `plt_super_admin`, `plt_security_officer` | Diff, reason, evidence, step-up |
| SCR-CFG-31 | Platform settings & bounds | `/console/config/settings` | platform roles | Definitions, defaults, bounds, tier, owners |
| SCR-CFG-32 | Support sessions | `/settings/account/support-access` | `ten_admin` | Grant, scope, duration, revoke, log |

**Fewer-click rules.** Inline editing for T values (click → edit → Enter saves; Esc cancels); "Apply to…" multi-scope picker on any T value; bulk edit via selection; "Copy settings from department X"; contextual "Configure" links from module screens (e.g., a compliance list shows "Reminder cadence: T-15, T-7, T-1 · Change" for admins). Empty states always explain and offer the one next action ("No custom fields yet — Add field").

**v1.1 screens** *(v1.1)*

| Screen ID | Name | Menu path | Roles |
|---|---|---|---|
| SCR-CFG-33 | Custom Registers builder and register list | Settings › Registers | ten_admin |
| SCR-CFG-34 | Workflow / approval-chain simulation report | Settings › Workflows › Simulate | ten_admin, ten_cco |
| SCR-CFG-35 | Preview as role | Settings › Menus | ten_admin |
| SCR-CFG-36 | Configuration templates (library, copy entity → entity, save as template) | Settings › Templates | ten_admin; dlv_lead (offer only) |
| SCR-CFG-37 | Configuration sandbox | Settings › Sandbox | ten_admin |
| SCR-CFG-38 | AI autonomy levels and promotion requests | Settings › AI › Autonomy | ten_admin, ten_kmp (AIO) |
| SCR-CFG-39 | Kill switches and drills | Settings › AI › Kill switches | ten_admin, ten_kmp (AIO) |
| SCR-CFG-40 | Automations (all) | Settings › Automations | ten_admin |
| SCR-CFG-41 | Locale, calendars and fiscal year per legal entity | Settings › Organisation › Locale | ten_admin |
| SCR-CFG-42 | Explain my configuration (document and diff) | Settings › Health | ten_admin, auditors (read) |

---

## 7. Backend design

### 7.1 Modules touched

`cfg` (owner), `core` (change requests, correction entries, feature flags, audit ledger), `wf` (consumes workflow definitions, SLA policies, escalation ladders), `iam` (permissions, delegations data from P01), `hlp` (help keys), `rpt` (widget catalogue, dashboards), `ai` (summary drafts, mapping suggestions).

### 7.2 Tables (PostgreSQL schema `cfg`; tenant RLS unless marked *platform*)

| Table | Key columns |
|---|---|
| `setting_definitions` *platform* | key PK, tier, sub_class, value_type, json_schema, default_value, bounds, allowed_scopes[], merge_strategy, child_direction, protective_direction, instance_pinned, sensitivity, owner_role, citation_required, fallback_kind, ui jsonb, introduced_in, deprecated_in, alias_of |
| `setting_values` | id, tenant_id, scope_kind, scope_id, key, value jsonb, version, locked boolean, lock_scope, valid_from, valid_to, recorded_at, change_id |
| `setting_changes` | id, tenant_id, key, scope, before, after, actor_id, on_behalf_of, reason, via (`ui`, `api`, `pack`, `import`, `correction`), recorded_at |
| `tenant_controls` | tenant_id, require_approval_keys[], max_pin_days, sandbox_enabled |
| `rule_packs` *platform + tenant* | id, code, jurisdiction, domain, name, effect_class, owner_role, volatile, tenant_id null for platform |
| `rule_pack_versions` | id, pack_id, version (`YYYY.N`), status, content jsonb (ZEN JDM), params jsonb, citations jsonb (LR-IDs, instrument_version_id, para), source_sha256[], effective_from, effective_to, applies_to, propagation_mode, next_review_due, verification_status, summary_i18n, created_by, approved_by[] |
| `rule_params` | version_id, code, value, unit, verification_status, citation |
| `golden_cases` | id, pack_id, tenant_id null/!, inputs jsonb, expected jsonb, kind (positive/negative), author |
| `pack_adoptions` | tenant_id, pack_id, mode, pinned_version_id, adapted_params jsonb, adopted_at, acknowledged_changes |
| `rule_challenges` | id, tenant_id, pack_id, sources, status, response, responded_at |
| `setting_packs` *platform* / `setting_pack_versions` | code, entity_family, version, content jsonb (sections) |
| `setting_pack_adoptions` | tenant_id, pack_code, version, sections_applied[], applied_by, applied_at |
| `department_catalogue` *platform* | dept_code, name_i18n, description, entity_families[] |
| `org_nodes` | id, tenant_id, legal_entity_id null, parent_id, kind (`department`, `sub_department`, `function`, `sub_function`), name, canonical_codes[], head_employee_id, deputy_employee_id, maker_pool_id, checker_pool_id, valid_from, valid_to |
| `org_node_history` | node_id, name, parent_id, valid_from, valid_to (bitemporal display) |
| `terminology` | tenant_id null for platform, entity_family, term_key, locale, text, locked |
| `status_sets` / `status_definitions` | tenant_id, object_type, version; status code, label_i18n, canonical_status, colour, icon, requires_checker, required_fields[] |
| `waiting_party_types` / `chase_policies` | tenant_id, code, canonical_type, label; cadence ISO8601, channels[], template_ids[], max_chases, allow_internal_sla_pause |
| `reason_code_lists` / `reason_codes` | tenant_id, list_code, code, label, locked |
| `custom_field_defs` | id, tenant_id, object_type, code, label_i18n, type, options, required_at_status[], visibility_roles[], edit_roles[], pii_class, searchable, export_name, formula_cel |
| `form_defs` / `form_def_versions` | tenant_id, object_type, version, layout jsonb, conditions, status |
| `workflow_defs` / `workflow_def_versions` | tenant_id null for templates, object_type, code, version, graph jsonb, status, validator_report |
| `sla_policies` / `escalation_ladders` / `business_calendars` | tenant_id, object_type, priority, target, floor_ref; levels jsonb; calendar holidays by legal_entity/State |
| `delegations` (owned by `iam`, read here) | — |
| `notification_templates` | tenant_id null for platform, event_type, channel, locale, subject, body, variables_schema, dlt_template_id, wa_template_name, version |
| `channel_policies` | tenant_id, priority, channels, digest_times, quiet_hours |
| `widget_catalogue` *platform* | code, module, title_key, data_api, roles[], params_schema, default_size, mandatory_for_roles[], a11y_table |
| `dashboard_layouts` | tenant_id, scope (`role`, `department`, `user`), scope_ref, widgets jsonb, version |
| `nav_items` *platform* / `nav_overrides` | item code, shell, parent, route, required_permission, entitlement, locked; tenant_id, role, hidden, order, label_override |
| `saved_views` | tenant_id, owner_id, object_type, filters, columns, sort, shared_with, official |
| `branding` | tenant_id, logo_object_key, colours, themes, letterhead, sender_domain, dns_status, custom_domain |
| `fallback_events` | tenant_id, key or pack, object_ref, kind, reason, at |
| `config_bundles` | tenant_id, kind (export/import), object_key, signature, diff_report, status |

### 7.3 APIs (`/v1`; Idempotency-Key on POST; ETag/If-Match on PATCH)

- `GET /v1/settings?section=&scope=` · `GET /v1/settings/{key}/resolve?ctx=` · `PATCH /v1/settings/{key}` (T) · `POST /v1/settings/{key}:undo` · `GET /v1/settings/{key}/history`
- `POST /v1/config-change-requests` · `POST /v1/config-change-requests/{id}:submit|approve|reject|withdraw` · `POST /v1/config-change-requests/{id}:preview`
- `GET /v1/rule-packs` · `POST /v1/rule-packs/{id}/versions` · `POST /v1/rule-pack-versions/{id}:run-golden` · `:impact` · `:submit` · `:approve` · `:publish` · `:retire` · `POST /v1/rule-packs/{id}:adopt|pin|adapt` · `POST /v1/rule-challenges`
- `POST /v1/rules:evaluate` (internal; deterministic evaluation for a pack + inputs; used by modules)
- `GET/POST /v1/setting-packs` · `POST /v1/setting-packs/{code}:preview|apply`
- `GET/POST/PATCH /v1/org-nodes` · `POST /v1/org-nodes:merge|split` (dry-run first)
- `GET/PUT /v1/terminology` · `GET/POST /v1/status-sets` · `GET/POST /v1/custom-fields` · `GET/POST /v1/forms` · `GET/POST /v1/workflow-defs/{id}/versions` · `POST …:validate|publish|migrate`
- `GET/PUT /v1/notification-templates` · `GET/PUT /v1/dashboards/layouts` · `GET/PUT /v1/navigation/overrides` · `GET/PUT /v1/branding` · `POST /v1/branding/domains:verify`
- `POST /v1/config-bundles:export` · `POST /v1/config-bundles:import` (dry-run then commit) · `GET /v1/config:compare?a=&b=`
- Console: `POST /v1/console/tenants/{id}/corrections` · `POST /v1/console/corrections/{id}:approve|reject` · `POST /v1/console/tenants/{id}/support-sessions`

### 7.4 Domain events (CloudEvents; IDs and keys only)

`in.lawdocscomply.cfg.SettingChanged.v1`, `…cfg.ConfigChangeRequested.v1`, `…cfg.ConfigChangeApproved.v1`, `…cfg.ConfigChangeActivated.v1`, `…cfg.RulePackVersionSubmitted.v1`, `…cfg.RulePackVersionActivated.v1`, `…cfg.RulePackRetired.v1`, `…cfg.RulePackReviewDue.v1`, `…cfg.FallbackActivated.v1`, `…cfg.SettingPackApplied.v1`, `…cfg.OrgNodeChanged.v1`, `…cfg.OrgNodesMerged.v1`, `…cfg.WorkflowDefinitionPublished.v1`, `…cfg.StatusSetPublished.v1`, `…cfg.TenantChangeAckOverdue.v1`, `…core.CorrectionEntryRequested.v1`, `…core.CorrectionEntryApplied.v1`, `…core.EmergencyOverrideApplied.v1`, `…cfg.ConfigBundleExported.v1`, `…cfg.ConfigBundleImported.v1`.

### 7.5 Jobs and Temporal workflows

`ConfigActivationWorkflow` (timer to `effective_from`; re-validate; activate; propagate), `RulePackImpactWorkflow`, `GoldenSuiteRunJob`, `ReviewDueScanJob` (daily 06:00 IST), `PinExpiryScanJob`, `TenantAckEscalationJob`, `ChasePolicyWorkflow` (per waiting item), `OrgMergeJob`, `WorkflowMigrationJob`, `CacheInvalidationConsumer`, `DomainVerificationJob`, `EmergencyOverrideRevertWorkflow` (24 h), `ConfigHealthSnapshotJob` (nightly).

**v1.1 tables and APIs** *(v1.1)*: `cfg.custom_registers`, `cfg.custom_register_versions`, `cfg.custom_register_records` (JSONB validated against the version schema), `cfg.config_templates`, `cfg.simulations`, `cfg.autonomy_levels` (scope, scope_id, level, effective_from, approved_by), `cfg.autonomy_requests`, `cfg.automation_registry` (view over module automations), `cfg.locale_profiles`. APIs: `POST /v1/config/registers`, `POST /v1/config/registers/{id}/versions:publish`, `POST /v1/config/simulations`, `POST /v1/config/templates/{id}:apply` (returns change batch id), `POST /v1/config/sandboxes`, `POST /v1/config/sandboxes/{id}:promote`, `GET|POST /v1/ai/autonomy`, `POST /v1/ai/kill-switches/{scope}/{id}`, `POST /v1/config/explain`. Events: `in.lawdocscomply.cfg.CustomRegisterPublished.v1`, `…cfg.AutonomyLevelChanged.v1`, `…ai.KillSwitchChanged.v1`, `…cfg.TemplateApplied.v1`.

---

## 8. Integrations (ports and adapters)

| Port | Use in P02 | Adapters |
|---|---|---|
| `RULES_PORT` | Evaluate rule packs | GoRules ZEN (Node binding) default; CEL (`cel-js` or WASM build of cel-go) for predicates |
| `HRMS_PORT` (internal to P13) | Department heads, reporting lines for assignment rules | LDC HRMS; external HRMS via P18 |
| `CALENDAR_PORT` | Business calendars and holiday lists | Seeded holiday packs; RBI holiday list; State notifications [VERIFY sources per State] |
| `NOTIFY_PORT` | Template rendering and delivery (P04 owns delivery) | Email (SES/Postmark), SMS DLT (MSG91/Gupshup), WhatsApp BSP, MS Teams, push |
| `DNS_CHECK_PORT` | Sender and custom domain verification | Internal resolver checks |
| `AI_PORT` | Drafts change summaries and mapping suggestions | Claude via P17 adapter |

Ecosystem: setting packs and rule packs are LDC-internal; no setting values cross to Finbyx/Udofin except via documented contracts (NN-23). Group tenants may share **policy** settings (MFA, branding kit) through group scope but never data access.

---

## 9. Settings and configuration of the configuration system

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `cfg.change_requests.expiry_days` | T | 14 | 7–30 | `ten_admin` |
| `cfg.change_requests.approval_sla_working_days` | T | 2 | 1–10 | `ten_admin` |
| `cfg.legal.lead_time_hours` | G | 24 | ≥ 0 with `urgent_effective` | `plt_content_publisher` |
| `cfg.packs.max_pin_days` | G | 90 | 0–180 | platform |
| `cfg.review.default_days` | G | 180 | 30–365 | platform |
| `cfg.review.secondary_only_days` | G | 90 | 30–180 | platform |
| `cfg.review.volatile_days` | G | 30 | 7–90 | platform |
| `cfg.t_undo_window_seconds` | T | 600 | 300–1800 | `ten_admin` |
| `cfg.bulk.max_rows` | G | 5000 | 100–20000 | platform |
| `cfg.custom_fields.max_per_object` | G-elevated | 100 | 10–200 | platform |
| `cfg.tenant_ack.escalation_working_days` | T | 5 | 1–15 | `ten_admin` |
| `cfg.sandbox.enabled` | T | true | — | `ten_admin` |
| `cfg.emergency_override.ratify_hours` | L | 24 | — | — |
| `cfg.correction.reason_min_chars` | L | 20 | — | — |
| `wf.waiting.default_chase_cadence` | T | P3D | P1D–P14D | `ten_admin` |
| `wf.waiting.max_chases` | T | 5 | 1–20 | `ten_admin` |
| `wf.waiting.statutory_warning_days` | T (raise_only vs platform 3) | 7 | 3–60 | `ten_cco` |
| `wf.delegation.max_days` | G | 90 | 1–90 | platform |
| `notify.quiet_hours` | T (user narrow_only) | 21:00–08:00 | — | `ten_admin` / user |
| `ui.theme.default` | T | light | light/dark/high-contrast | `ten_admin` / user |

Full catalogue: Appendix U.

**v1.1 settings** *(v1.1)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `cfg.registers.max_per_tenant` | G (plan) | per Appendix N | — | plt_super_admin |
| `cfg.simulation.lookback_days` | T | 30 | 7–180 | ten_admin |
| `cfg.simulation.required_before_publish` | L | true | — | — |
| `cfg.sandbox.enabled` | T | ON | — | ten_admin |
| `ai.autonomy.platform_ceiling.<agent>` | L (per agent; owner P17) | L2 (L3-eligible after gate) | L0–L4 | platform release |
| `ai.autonomy.tenant_ceiling` | G (owner P17) | L1 | L0–platform ceiling | ten_admin + ten_cco (AIO where designated) |
| `ai.autonomy.agent.<agent>` / `ai.autonomy.skill.<skill>` | G raise / T lower (owner P17) | L1 / inherit | ≤ parent | sponsor + ten_admin |
| `ai.autonomy.sealed_contexts` | L | L0 | — | — |
| `ai.autonomy.promotion_min_eval_pass` | G (platform) | 0.95 | 0.90–1.00 | plt_super_admin |
| `ai.killswitch.drill_frequency_days` | T (owner P17) | 90 | 30–365; Enterprise tenants ≤ 90 (mandatory); platform drill quarterly regardless (NN-51) *(X1)* | ten_admin |
| `notify.budget.daily_interruptive` | T | 15 | 5–50 (users may only lower) | ten_admin |
| `cfg.batches.undo_hours.<kind>` | G | 24 | 1–168 | ten_admin + ten_cco |

---

## 10. Security, privacy and audit

- All `cfg` tenant tables under RLS (NN-01); platform tables read-only to tenant roles.
- Secrets never stored in `cfg` (`secret_ref` only, vault-backed; NN-32); events and logs contain keys and IDs, never values of `confidential` or `secret_ref` definitions.
- Every T and G change, every pack adoption, every Correction Entry is written to the hash-chained audit ledger (NN-02) with actor, on-behalf-of, scope, before/after (sealed copy for confidential values), reason and request ID.
- Step-up (AAL2) for G approvals, Correction Entries, branding domain changes and workflow publication.
- Support sessions: tenant-granted, scoped (sections), time-boxed (default 2 h, max 24 h), read-only unless the grant says otherwise, banner visible to tenant users, full log (NN-30).
- Custom fields carry PII class; `sensitive` and `sealed` fields are encrypted at field level and excluded from search indexes and AI context unless the user is in the sealed audience (NN-13).
- Configuration export bundles are signed (JWS) and encrypted at rest; downloads logged.
- Rule evaluation is sandboxed (no I/O); CEL expressions limited by cost budget to prevent denial of service.

---

## 11. AI touchpoints and guardrails

| Touchpoint | What Vidhi does | Guardrail |
|---|---|---|
| Change summary | Drafts the ≤ 120-word "what changed" summary from the diff and cited source | Maker edits and owns; checker approves (NN-04) |
| Department mapping | Suggests canonical `dept_code` mappings for tenant departments and for unmapped obligations, with confidence | Admin confirms each mapping; never auto-applied |
| Custom-field suggestions | Proposes fields from uploaded tenant registers/Excel | Admin creates |
| Workflow lint explanation | Explains validator failures in plain language | Validator decides, not AI |
| Settings Q&A | "How do I change reminder cadence?" answered from help content with deep links | Cites help article; no setting change by AI |

No AI tool in P02 has write permission on `cfg` (`svc_vidhi` lacks `change_t`, `approve_g`).

---

## 12. Acceptance criteria (`tests/acceptance/p02/*.feature`)

```gherkin
Feature: Tiers and pipelines
  Scenario: Locked value cannot be changed
    Given a tenant admin and the L setting "core.audit.append_only"
    When the admin calls PATCH /v1/settings/core.audit.append_only
    Then the response is 403 with code LDC-CFG-010 "Locked setting"
    And no change row is written

  Scenario: T change is effective within 60 seconds and undoable
    Given the T setting "cmp.reminders.default_offsets_days" is "[15,7,1]"
    When the tenant admin sets it to "[30,15,7,1]"
    Then a new compliance instance created 60 seconds later uses offsets [30,15,7,1]
    And the admin can undo within 10 minutes restoring [15,7,1]

  Scenario: Maker cannot approve own G change
    Given ten_admin "A" submits a G change to "grv.sla.final_reply_internal_days"
    When "A" attempts to approve it
    Then the response is 403 with code LDC-CFG-020 "Maker cannot approve"

  Scenario: Tenant cannot relax a statutory floor
    Given the platform floor for grievance final reply is 30 days
    When the tenant proposes 35 days
    Then validation fails with LDC-CFG-004 "Outside protective bound"
    And a bounded value of 21 days is accepted as a stricter internal target

Feature: Rule packs
  Scenario: Future-dated due-date rule with preview
    Given rule pack "rulepack.IN.rbi.nbfc.returns" version 2026.3 is active
    And a draft 2026.4 changes a return's due date from 15 to 21 days after quarter end effective 1 Jan 2027
    When the maker runs preview
    Then the diff lists affected tenants and instance counts for periods ending on or after 31 Dec 2026
    And instances for the quarter ending 30 Sep 2026 keep their pinned due date

  Scenario: Golden case mismatch blocks submission
    Given a rule pack version whose golden case expects due date 2026-11-15
    And the edited table yields 2026-11-14
    When the maker submits
    Then submission is refused with LDC-CFG-080 "Golden suite failing" unless the checker accepts the mismatch with a reason

  Scenario: Overdue review applies fallback
    Given a computational pack with next_review_due yesterday and fallback "last_approved"
    When a compliance instance is generated
    Then it uses the last approved version and shows "Under review" and fallback_applied = true

Feature: Waiting-on items
  Scenario: Statutory clock does not pause while waiting
    Given a compliance instance due on 2026-11-30 set to waiting on "Statutory auditor"
    And internal SLA pause is allowed
    When the date reaches 2026-11-23 (statutory_warning_days = 7)
    Then the department head and CCO are notified "Statutory deadline approaching while waiting"
    And the instance due date remains 2026-11-30

  Scenario: Chase cadence sends templated reminders
    Given waiting party "Finbyx data feed owner" with cadence P2D and max_chases 3
    Then three chase notifications are sent at 2-day intervals and the fourth interval escalates to L1

Feature: Departments and terminology
  Scenario: Rename department keeps history
    Given department "Operations" with 40 open compliance instances
    When it is renamed "Credit Operations"
    Then all 40 instances show "Credit Operations"
    And the audit history of each shows "Operations" for events before the rename

  Scenario: Co-operative terminology pack
    Given a tenant with entity family COOP-CCS
    Then the governance menu shows "Managing Committee" instead of "Board"
    And statutory form names are unchanged

Feature: Workflow designer invariants
  Scenario: Publishing a workflow without a checker for High-risk items fails
    When the admin publishes a workflow where High-risk compliance instances end after the maker step
    Then validation fails with LDC-CFG-041 "High-risk items need a checker"

  Scenario: Retainer RM may be maker but not checker
    Given engagement "retainer" with dlv_rm "R" as maker
    When a workflow assigns "R" to the checker step
    Then publication fails with LDC-CFG-043 "Checker must be a tenant user in retainer mode"

Feature: Super-admin override
  Scenario: Correction Entry visible to tenant
    Given plt_super_admin "S" requests correction of a compliance instance's filing date from 2026-10-10 to 2026-10-08 with reason "data_error"
    And plt_security_officer "Q" approves
    Then the instance shows filing date 2026-10-08 with a "Corrected" chip
    And "Changes made by LawDocs" lists the entry with old and new values, both actors and recorded_at
    And the original value remains in the sealed ledger

  Scenario: Single-person override refused
    When "S" approves their own correction request
    Then the response is 403 LDC-CFG-060

Feature: Export and import
  Scenario: Import rejects out-of-bound values
    Given a configuration bundle containing "cfg.custom_fields.max_per_object = 500"
    When imported into a sandbox
    Then that row is rejected with LDC-CFG-070 and other valid rows are listed for confirmation
```

NN tests: `NN-05_maker_not_checker_cfg`, `NN-28_locked_keys_immutable`, `NN-28_registry_before_use` (CI lint), `NN-33_statutory_clock_never_pauses`, `NN-02_correction_entry_preserves_original`, `NN-03_pack_update_preserves_tenant_adaptation`, `NN-07_pinned_instance_unchanged`, `NN-01_cfg_rls_cross_tenant`, `NN-32_no_secret_values_in_events`, `NN-21_branding_contrast_enforced`.

```gherkin
Feature: Custom register without code (v1.1)
  Scenario: Tenant builds an insurance-policies register
    Given the tenant admin creates a register with fields policy number, insurer, expiry date and premium
    When the register is published
    Then users can add records and receive reminders before expiry
    And the export mapping for the register exists without any code release

Feature: Simulation before publishing an approval chain (v1.1)
  Scenario: Publish is blocked until the simulation is reviewed
    Given a new approval chain for High-risk compliance items
    When the admin tries to publish it without opening the simulation report
    Then Publish is disabled and the admin is asked to run the simulation

Feature: Effective autonomy is the minimum (v1.1)
  Scenario: Skill set to L3 inside a tenant at L2
    Given the tenant autonomy is L2 and the Board Pack skill is set to L3
    When the Board Pack agent runs
    Then it runs at L2 and the L3 tools are not exposed to the model

Feature: Kill switch propagates (v1.1)
  Scenario: Tenant kill switch stops all agents within 60 seconds
    Given three Vidhi missions are running for the tenant
    When the AI Officer turns the tenant kill switch on
    Then all three missions stop within 60 seconds and pending tool calls are refused
```

NN tests added *(v1.1)*: `NN-49_template_apply_undo`, `NN-50_effective_autonomy_min`, `NN-51_tenant_kill_switch_60s`.

---

## 13. Deliverables and exit gate

1. `packages/config` SDK with codegen, React hook, NestJS decorator, test helpers; CI lint `config-registry-lint`.
2. `cfg` schema migrations (expand-contract), seed definitions (Appendix U), seed setting packs (≥ 12 families at exit: NBFC-BL/ML/UL, NBFC-ICC, UCB-T2, COOP-CCS-RJ, IFSCA-FCFU, SEBI-LISTED-MAIN, IRDAI-BROKER, MCA-PVT, MCA-LLP, STANDALONE-HRMS-LABOUR), seed department catalogue, terminology packs, canonical status sets, seed workflow templates (≥ 8).
3. Rule engine (`RULES_PORT` + ZEN + CEL) with ADR, golden-case harness, impact workflow, review-due scanning, fallback.
4. Studio screens SCR-CFG-01 to SCR-CFG-32, accessible (axe-core clean, keyboard paths tested).
5. Correction Entry console path and tenant "Changes made by LawDocs" page.
6. Configuration export/import/compare.
7. Documentation: `docs/config/` (how to add a setting, tier decision test, rule-pack authoring guide, setting-pack authoring guide), runbook for emergency blocks and overrides.

**Exit gate:** all §12 scenarios and NN tests green; zero unregistered keys in CI; p95 resolve ≤ 2 ms warm; a pilot tenant completes the §1 30-minute admin script unaided; Configuration Health shows zero High-risk workflows without a checker; ADR for the rule engine merged; P03–P05 teams have consumed the SDK.

- [ ] *(v1.1)* Custom Registers builder with 15 platform templates; approval-chain simulation; preview-as-role; configuration templates library and entity-to-entity copy; configuration sandbox; autonomy levels and kill-switch panel; automation governance view; locale and calendar profiles; notification budget; natural-language settings assistant (L2); "Explain my configuration".

---

## 14. Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P02-01 | RB-IOS 2026 clause numbers for the RE reply window and the complainant's filing window | Scheme text to be verified at clause level | Content checker | Use 30-day platform floor labelled "per RB-IOS 2026 [VERIFY clause]" |
| OI-P02-02 | SS-1 / SS-2 para numbers for minutes circulation and entry timelines, and any 2024–26 revisions of the Secretarial Standards | ICSI site text not retrieved in research | S3 / content | Use 15/30-day values with `SECONDARY_ONLY` status |
| OI-P02-03 | DPDP Rules 2025 commencement of r.7 breach obligations for the tenant population | Phased commencement | DPO (LDC) | Floor active as protective rule; computational outputs labelled indicative |
| OI-P02-04 | Holiday calendars per State and IFSC (Gujarat) for working-day due-date adjustment | Sources per State to be confirmed annually | Content team | National + RBI holidays only; State flag OFF |
| OI-P02-05 | ZEN engine licence and Node binding maturity at build time; CEL JS implementation choice | Library versions to be confirmed | CTO | ADR; JSON Logic as alternative behind `RULES_PORT` |
| OI-P02-06 | Maximum custom fields per object and performance impact on exports | Load-test needed | Engineering | Bound 100; raise only after load test |
| OI-P02-07 | Whether co-operative terminology varies by State Act (e.g., "Board of Directors" vs "Managing Committee") | State Acts differ | S7 / content | Terminology per `COOP-*-<State>` pack; default "Managing Committee" |
| OI-P02-08 *(v1.1)* | L3-eligibility gate per agent (platform ceiling L2 by default, P17) and promotion evidence threshold | Needs eval data from pilot tenants | AIO / owner | All agents capped at L2; tenant ceiling L1 default |
| OI-P02-09 *(v1.1)* | Plan limits for custom registers and sandboxes | Commercial | Owner | 5 registers on Essentials, 20 Professional, unlimited Enterprise (seed) |

---

## 15. Sources (accessed 25 October 2026)

- Companies Act 2013, ss.96, 128(5), 173 — https://www.mca.gov.in/content/mca/global/en/acts-rules/ebooks/acts.html
- ICSI Secretarial Standards (SS-1 limited revision page) — https://www.icsi.edu/finalss1/ (page content not retrievable; values marked [VERIFY])
- RBI Integrated Ombudsman Scheme 2026, effective 1 July 2026 (news summary; verify against RBI text) — https://www.outlookmoney.com/banking/rbi-integrated-ombudsman-scheme-takes-effect-from-july-1-expands-customer-complaint-redressal ; RE salient-features copies e.g. https://www.bandhan.bank.in/sites/default/files/2026-07/Annexure-Salient_features_of_the_Integrated_Ombudsman_Scheme_2026.pdf
- CERT-In Directions under s.70B(6) IT Act, 28 April 2022 — https://www.cert-in.org.in/
- GoRules ZEN engine (open-source business rules engine, JDM) — https://github.com/gorules/zen-go ; https://www.pypi.org/project/zen-engine
- Common Expression Language — https://opensource.googleblog.com/2024/06/common-expressions-for-portable-policy.html ; https://pkg.go.dev/github.com/google/cel-go/policy
- ServiceNow Regulatory Change Management process flow (benchmark; page could not be read in this session) — https://www.servicenow.com/docs/r/zurich/governance-risk-compliance/reg-change-workflow-swimlane.html
- MetricStream low-code/no-code GRC (benchmark) — https://www.metricstream.com/blog/grc-low-code-no-code.html
- W3C WCAG 2.2 (new criteria 2.4.11, 2.5.7, 2.5.8, 3.3.7, 3.3.8) — https://dequeuniversity.com/resources/wcag-2.2
- Equator v3.1 App V and Equator v3.1 P15 (external pattern reference; not appendices of this pack) *(v1.1)*
- Owner's LawDocs Comply Architecture Part 1 (Layout, Interaction Patterns, Design Tokens)

---

## 16. Master integration notes (pack lead, v1.1 and v1.2, 25 October 2026)

**From v1.0 integration:** NN-33 (waiting pauses internal targets only), NN-46; X-10 (department alias map, Appendix U §U.9.0), X-11 (canonical statuses), X-14 (Correction Entry scope), X-16 (register the host switches as Governed settings).

**Added in v1.1:** NN-49, NN-50, NN-51; X-53, X-58.

**Added in v1.2:** X-65, X-66 (RAG windows `cmp.rag.rules` and export defaults are registered settings; tenants may only widen RAG windows).

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
