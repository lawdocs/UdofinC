# Phase P03 — Configuration Studio, Rule Engine and Settings

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, `packages/config` skeleton, hash-chained audit ledger, `core.correction_entries`, transactional outbox, Temporal, Cerbos, OpenTelemetry), P01 (identity, step-up authentication, consent artefacts), P02 (tenants, legal entities, departments, positions, user types, delegations and the maker-checker engine in `wf`). External: none at runtime (GoRules ZEN and CEL are embedded libraries).
> **Sequencing:** Sprint 1 freezes four contracts that every later phase consumes: the settings SDK (`packages/config`: registry, resolver, codegen, CI lint), the tier tree and control classes, `RULES_PORT` (`packages/rules`) and the open/interim/waiting **items API** (`packages/workflow` → `wf.items`). P04, P06, P07, P08, P17 and P19 start consuming in sprint 2. Studio screens follow in sprints 2–5; rule authoring and golden-case tooling in sprints 3–5; configuration templates, sandbox and export/import in sprint 6. No phase may read a setting, evaluate a legal rule or create a waiting item through any other path after sprint 1 (NN-29).
> **Binding IPB files *(v1.1)*:** IPB-07 §07.4.2 (binding 20-node Settings tree — mapped in Appendix C §C.4.17A), IPB-04 §04.3.2 (Brand Studio tenant layer, `brand_pack`), IPB-02 (password/MFA policy, sessions, IP allow-list, BYOK), IPB-09 §09.3.F (OpenFeature flags). New §4P adds the tree alignment and the Security sub-items; §4E gains FR-P03-31A and FR-P03-36A.
> **Binding appendices:** A (workflows and state machines — A.13–A.17), B (data model, events and error codes), R (configuration framework and settings catalogue — binding for every key, tier and default), D (roles and access matrix), F (instrument eligibility gate — rows run in this engine), H (agent roster — autonomy keys), K (export package — configuration and items folders), W (open items), Y (Ecosystem Spec v1.2 change request). Precedence on conflict: master §18 (master → `02` → G → F → B → A → D → R → C → this phase), except that this phase wins on the defaults of the keys it owns (X-11).
> **Requirements covered:** R-027, R-030, R-047, R-026, R-028, R-019, R-025 (accessible theming), R-008 (labels per language), R-064 (RM proposes configuration), R-066 (super-admin changes through a transparent workflow), R-067, R-054 (revenue-stream switches use the registry; values in P17), R-053/R-055 (suite-neutral templates).
> **Decisions applied:** D-01, D-02, D-06, D-07, D-10, D-12, D-13, D-15 · **Challenges applied:** CH-12, CH-21, CH-24, CH-26, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-07, NN-13, NN-18, NN-28, NN-29, NN-30, NN-34, NN-38, NN-39, NN-40, NN-43, NN-45
> **Estimated effort:** 6 two-week sprints, squad of 8 (configuration core 2 backend; rule engine 2 backend; items engine 1 backend; Studio UX 2 frontend; QA/accessibility 1).

---

## 1. Objective and business outcome

LawDocs serves an individual signing a rent agreement, a five-person startup, a 2,000-employee NBFC with a legal department, a practising advocate and a consumer-help case manager. Each wants different words, screens, reminders, approvals and defaults. Indian law also changes often: a State revises stamp duty, the IT Act First Schedule is amended, the RBI replaces its Ombudsman Scheme. The owner's brief asks for "very complete settings", a "dynamic rule and content engine, not static", customisable "open, interim and waiting-for-someone-else items", and "super admin not needed for small changes" (R-047).

P03 delivers one governed configuration system:

- a **settings registry** where every configurable value is declared once, with a tier, a control class, bounds, an owner and an "i" help key;
- a **Configuration Studio** with three faces — Super Admin console, tenant administration (company admin, department head, professional firm admin) and personal settings (every user) — so that each user type changes what it may change, immediately and with audit;
- a **rule engine** (GoRules ZEN decision tables + CEL predicates behind `RULES_PORT`) that runs legal rules, jurisdiction variants, instrument-eligibility rows, reminders and SLA policies as versioned, sourced, effective-dated data with a reviewer of record (NN-30);
- an **open / interim / waiting items engine** used by every module, with configurable item types, statuses, owners, SLA clocks and chasers, and locked legal clocks that never pause;
- **feature flags and kill switches** for every agent, revenue stream, vendor adapter, consumer vertical and outbound channel (NN-39).

| Outcome | Exit-gate measure |
|---|---|
| Small changes without LawDocs staff (R-047) | A new company admin, unaided, in ≤ 20 minutes: renames two departments, adds three custom fields to agreements, relabels two agreement statuses, sets a numbering scheme, uploads a letterhead, changes the reminder cadence for renewals, pins three menu items and two quick actions, and sets quiet hours — all audited and undoable; zero LawDocs actions |
| Individuals customise in ≤ 2 taps | From home: theme, text size, language, home widgets and reminder timing each reachable in ≤ 2 taps on mobile and ≤ 2 clicks on web |
| Legal values governed | 100% of GOVERNED changes pass maker ≠ checker, preview, citation and effective date; 0 LOCKED values changeable through any UI or API (`NN-29_*`, `NN-18_*` tests) |
| Law changes as data | A changed State stamp-duty row, a new First Schedule entry or a revised Ombudsman timeline is drafted, golden-tested, reviewed by `PLT_LEGAL_REVIEWER`, scheduled and activated with no deployment; documents already in flight keep their pinned rule version |
| Waiting items work everywhere | The items API is frozen in sprint 1 and proven by a reference adopter and contract tests at P03 exit; each adopting phase (P04, P07, P08 in Wave 1; P11, P15, P16, P18 later) must pass `items-adoption` at its own exit gate; the "Waiting on others" widget shows every item with party, age, next chase and the legal clock that keeps running |
| Safe switches | Every kill switch registered in Appendix R propagates in ≤ 60 seconds and is drilled at least quarterly |

---

## 2. Scope (in / out)

**In scope**

- `cfg` module: setting definitions, values, change requests, scheduled activations, change batches and undo, tier tree, control classes, merge strategies, Studio APIs, configuration templates, sandbox, export/import, Configuration Health.
- UI/UX customisation: themes over LD design tokens with contrast validation, density, font scale, home widgets, menu pinning and reordering, quick actions, landing pages, terminology and field labels, custom fields, custom status sets, reason codes, numbering schemes, form layouts, notification templates (rendered by `ntf`), document branding and letterheads (rendered by `packages/docgen`).
- `rul` module: `RULES_PORT`, ZEN and CEL runtimes, rule-set registry, jurisdiction packs, golden cases, preview and impact analysis, lifecycle with reviewer of record, verification status, fallback; the shared **content-version framework** used by `tpl`, `hlp` and `dms` retention schedules.
- `wf.items`: item types, canonical states, waiting parties, clocks, chase policies, escalation ladders, item widgets and APIs.
- Feature flags and kill switches (`cfg.flags`, `cfg.kill_switches`) — the **single platform registry** (R-A-09): P00 creates the heads, P09 and P19 read and engage switches through it and emit/consume only `in.lawdocs.cfg.KillSwitchEngaged.v1` / `in.lawdocs.cfg.KillSwitchReleased.v1`.
- Tasks (`wf.tasks`, `tsk_`; R-A-08): the one task table used by P11, P13, P18 and Appendix I.
- Super-admin configuration overrides through Correction Entries with client approval (CH-26).

**Out of scope (owner phase)**

- Maker-checker engine, approval chains, delegations, department and position masters — P02 (P03 configures them; P02 executes them).
- Template, clause and questionnaire **content** — P06; glossary and help content — P21; P03 supplies the versioning framework they use.
- Instrument-eligibility **rows** (content of Appendix F) — P08 owns the content; P03 runs it.
- Plan prices and revenue-stream values — P17 (uses the GOVERNED-elevated pipeline from P03).
- Notification delivery, DLT registration and channel adapters — `ntf` in P00/P19; P03 owns templates and channel policy only.
- Export of configuration in `LD-EXPORT-1.0` — P20 builds the package; P03 registers the export-map entries (§13).

---

## 3. Personas and permissions touched

Full matrix: Appendix D. Cerbos resources: `cfg_setting` (`read`, `change_open`, `propose_governed`, `approve_governed`, `lock`), `cfg_template` (`apply`, `publish`), `rule_set` (`draft`, `submit`, `review`, `publish`, `retire`, `adopt`), `item_type` (`define`, `publish`), `item` (`create`, `assign`, `wait`, `chase`, `resolve`, `waive`), `flag` (`toggle`), `kill_switch` (`engage`, `release`), `correction_entry` (`request`, `approve`).

| Role code | What they do in P03 | Limits |
|---|---|---|
| `PLT_SUPER_ADMIN` | Platform and brand defaults, bounds and plan limits (with P17); tenant overrides only through a Correction Entry | Cannot change LOCKED values; cannot approve own change; every tenant-scope action visible to the tenant |
| `PLT_CONTENT_EDITOR` | Drafts rule sets, jurisdiction packs, eligibility rows, glossary-linked rules | Maker only |
| `PLT_LEGAL_REVIEWER` | Reviewer of record for every legal rule or content version (NN-30); approves publication | Cannot review own draft |
| `PLT_SECURITY_OFFICER` | Approves security-baseline GOVERNED values; co-approves emergency blocks and platform kill switches | — |
| `PLT_RELEASE_MANAGER` | Owns flag rollout plans and ring assignments (with P23) | Flags only; no legal rules |
| `PLT_DPO` | Approves keys of class `privacy` (retention floors, consent defaults, transfer flags) | — |
| `ORG_OWNER`, `ORG_ADMIN` | All OPEN tenant settings; proposes tenant GOVERNED changes; applies templates; defines item types and chase policies; engages tenant kill switches | Cannot approve own GOVERNED change |
| `ORG_CLO` | Default tenant checker for GOVERNED legal-workflow keys (approval matrices, formalities waivers policy, retention above floors) | — |
| `ORG_DEPT_HEAD` | Department-scope OPEN settings (labels, reminders, dashboards, default owners, chase cadence) when delegated | Own department only |
| `ORG_LEGAL_MAKER`, `ORG_CHECKER`, `ORG_APPROVER`, `ORG_MEMBER`, `ORG_DIRECTOR`, `ORG_KMP` | Personal settings; create and manage items on records they can edit | User scope only |
| `ORG_DELEGATED_MAKER` / `OPS_RM` | Proposes OPEN or GOVERNED tenant changes where the delivery grant includes `cfg:propose` (R-064) | Never approves in the client tenant; client checker decides |
| `IND_OWNER` | All personal-workspace settings (the individual is their own admin) | LOCKED and plan bounds apply |
| `IND_FAMILY_MEMBER`, `IND_DELEGATE` | Own preferences; items on shared records within scope | — |
| `PRO_FIRM_ADMIN` | Practice workspace settings (letterhead, numbering, templates' non-legal text, item types) | — |
| `PRO_ADVOCATE`, `PRO_CA`, `PRO_CS`, `PRO_TAX_PRACTITIONER` | Personal settings; items on engagements | — |
| `OPS_CONSUMER_CASE_MANAGER` | Item and chase settings inside the Consumer Help brand | Brand scope; ethical wall (NN-23) |
| `AGT_*` | Propose settings changes and create items as maker only | Never approves, never engages chasers to external parties without confirmation (NN-13, NN-43) |

---

## 4. Functional requirements

### 4A. Settings registry and resolver SDK

**FR-P03-01 — Registry before use (NN-29).** Every configurable value has a row in `cfg.setting_definitions` before any code reads it. The CI check `config-registry-lint` fails a build that (a) reads an unregistered key, (b) registers a key without tier, control class, type, default, bounds (for numeric and enumerated types), allowed scopes, merge strategy, owner role, help key and Studio section, or (c) registers a key absent from Appendix R. Appendix R is generated from the registry seed (`packages/config/seed/*.yaml`) and the two must not drift (`appendix-r-sync` check).

**FR-P03-02 — Definition schema.** Each definition carries: `key` (`<module>.<area>.<key>`, module codes per master §5.3 only); `tier` (owning tier `PLATFORM`, `BRAND`, `PLAN`, `TENANT`, `ENTITY`, `DEPARTMENT`, `USER`) and `allowed_scopes` below it (e.g., `TENANT→USER`); `control_class` (`LOCKED`, `GOVERNED` with sub-class `legal`/`elevated`/`privacy`/`integration`, `OPEN`); `value_type` (boolean, integer, decimal string, enum, multi-enum, ISO 8601 duration, time window, RRULE, money in paise, percentage, colour with contrast rule, catalogue or rule-set reference, JSON with JSON Schema 2020-12, sanitised rich text); `default`; `bounds` (with `floor` and `protective_direction` for protective values); `merge_strategy` and `child_direction` (Appendix R §R.3); `maker_checker` (`Y` forces the GOVERNED pipeline at any scope — NN-18); `effective_dating` (`immediate`, `scheduled_allowed`, `scheduled_required`); `instance_pinned`; `sensitivity` (`public`, `internal`, `confidential`, `secret_ref` — only a vault reference is stored); `owner_role`; `citation_required` (instrument + provision or `LG-xxx`); `depends_on_verify` (verification-log ID, NN-38); `fallback_kind` (`last_approved`, `platform_default`, `conservative`, `advisory_only`, `flag_off`, `manual_route`, `block`); `ui` (section, label key, `hlp.<module>.<term>` help key, widget, user types); `introduced_in`/`deprecated_in`/`alias_of` (a deprecated key needs an alias or migration — NN-12).

**FR-P03-03 — Resolver.** `config.get(key, ctx)` resolves for `ctx = {brand, plan, tenant, entity, department, user, user_type, jurisdiction, as_of, instance?}` in this order (Appendix R §R.4):

1. LOCKED definition value — always wins.
2. Active kill switch or emergency block for the key (forces the safe value).
3. Instance pin, when `ctx.instance` is given and the key is `instance_pinned`.
4. The most specific valid value among USER → DEPARTMENT → ENTITY → TENANT, combined by the key's merge strategy.
5. PLAN value (plan defaults and limits from entitlements mirrored by `bil`).
6. BRAND value (LawDocs, `[Consumer Help Brand]`, white-label brand).
7. PLATFORM value, then the definition default.
8. Declared fallback, if the value found is unapproved, past review date, or depends on an unverified fact.

**Bounds cascade downward:** the effective bounds at any scope are the intersection of PLATFORM, BRAND and PLAN bounds and any parent lock; a lower-tier value outside them is rejected at write time (`LD-CFG-004`) and ignored at read time. Every resolution returns `{value, source_tier, source_scope_id, source_version, control_class, fallback_applied}` so screens can show "Set by Legal department" and audit can record which version drove a decision.

**FR-P03-04 — Performance.** p95 ≤ 2 ms from the in-process cache, ≤ 15 ms cold; cache keys include `tenant_id` (NN-01); invalidation through the outbox event `in.lawdocs.cfg.SettingChanged.v1` reaches every pod in ≤ 60 s; an OPEN change is effective in ≤ 60 s, a GOVERNED change at `effective_from`.

**FR-P03-05 — SDK surfaces.** Generated TypeScript types per key; `useSetting(key)` React hook (web and Expo); `@RequiresSetting()` and `@FeatureFlag()` NestJS decorators; `withSettings({...})` test helper; mobile BFF (`/m/v1/settings/bootstrap`) returns the resolved user-visible subset in one call with an ETag. No module reads `cfg` tables directly; direct SQL on `cfg.*` from another schema fails the `schema-boundary` lint.

**FR-P03-06 — Tenancy.** All tenant-scoped `cfg`, `rul` and `wf` rows carry `tenant_id` and, where relevant, `legal_entity_id`, under enforced RLS (NN-01). Platform rows (`tenant_id IS NULL`) are readable by tenant roles only through the resolver.

**FR-P03-07 — Personal workspaces.** An individual's Personal workspace is a tenant of kind `personal`; `IND_OWNER` acts as its administrator and the ENTITY and DEPARTMENT tiers are hidden. A user who belongs to a Company workspace and a Personal workspace has separate USER-tier values per workspace, except accessibility and language preferences, which follow the person across workspaces unless overridden (`cfg.user.follow_person_preferences`, default ON).

**FR-P03-08 — Brand tier (D-06).** BRAND scopes carry theme tokens, legal-entity profile, footer and policy links, sender domains, enabled verticals, help-centre space and AI persona label. The `[Consumer Help Brand]` brand has its own values and an ethical wall: a Consumer Help tenant never inherits a LawDocs tenant's configuration and vice versa (NN-23).

### 4B. Tiers and control classes

**FR-P03-09 — Two dimensions.** *Tier* says **where** a value is set (PLATFORM … USER). *Control class* says **how** it may change:

| Aspect | LOCKED | GOVERNED | OPEN |
|---|---|---|---|
| What | NN rules, statutory protections of third parties, audit/evidence integrity, security baselines, India residency, canonical state machines | Legal parameters and rule sets, retention floors, money, price and privilege controls, vendor and outbound-channel settings, anything in the NN-18 list | Operational choices internal to the tenant or user: labels, layouts, reminders above floors, custom fields, branding, preferences |
| Who changes | Nobody in the product; platform release with ADR, passing NN test, CTO + Company Secretary (owner) approval (P23 `REGULATED` change) | Platform: maker ≠ checker among platform roles (legal rules need `PLT_LEGAL_REVIEWER`); tenant: tenant maker → tenant checker | Any user permitted at that scope |
| Path | Code + migration + release | Change request: preview, citation, effective date, impact report, step-up on approval | Immediate, audited, one-click undo |
| Effective | Next release | `effective_from` | ≤ 60 s |
| Badge in Studio | "Locked" (grey, padlock icon, text label) | "Needs approval" (amber, with approver role) | "Editable" (green) |

Badges use icon **and** text; colour is never the only cue (NN-28).

**FR-P03-10 — Decision test.** Apply Appendix R §R.2.3 (first "yes" wins: third-party protection or NN → LOCKED; money, privilege, data-sharing or NN-18 → GOVERNED-elevated; legal source or deadline → GOVERNED-legal; unconfirmed fact → GOVERNED with flag OFF; otherwise OPEN). Tie-break: the stricter class; split floor and margin.

**FR-P03-11 — LawDocs worked examples** (seed; full list Appendix R):

| Value | Tier / class | Basis |
|---|---|---|
| Audit ledger append-only | PLATFORM / LOCKED | NN-02 |
| Excluded instruments cannot be routed to eSign | PLATFORM / LOCKED (rows GOVERNED-legal) | IT Act 2000 First Schedule as amended by S.O. 4720(E), 26 Sep 2022 [VERIFY Gazette text and date] (R3 LG-003); NN-07 |
| Stamp before sign | PLATFORM / LOCKED | NN-08 |
| Second ESP route live within 30 days of the first | PLATFORM / GOVERNED-legal | CCA eSign API v3.3 (R3 LG-008) [VERIFY current API version] |
| eSign evidence retention ≥ 7 years after the later of signing and account closure | PLATFORM / GOVERNED-legal, `longest`, LOCKED floor | R3 LG-008, LG-092 |
| Grievance acknowledgement 24 h, resolution 7 days | PLATFORM / GOVERNED-legal, LOCKED floor; tenant may set shorter internal target | IT Rules 2021 r.3(2) as amended 2026 (R3 LG-077) [VERIFY post-2026 text] |
| DPDP rights-request response ≤ 90 days; internal target 30 days | PLATFORM / GOVERNED-privacy, floor LOCKED | DPDP Rules 2025 r.14(3) (R3 LG-068) |
| Agreement status labels | TENANT→DEPARTMENT / OPEN over LOCKED canonical states | Comparability (§4J) |
| Renewal reminder offsets | TENANT→USER / OPEN, `raise_only` against platform minimum | Operational |
| Approval matrix for agreements above ₹ value | TENANT→ENTITY / GOVERNED-elevated, `maker_checker = Y` | NN-18 |
| Buyer platform fee per booking | PLATFORM / GOVERNED-elevated | D-05, NN-21 |
| Theme accent colour | BRAND→USER / OPEN, contrast-validated | NN-28 |
| Advertising stream | PLATFORM / GOVERNED-elevated, default OFF | D-13, NN-35 |

**FR-P03-12 — Plan tier.** PLAN values come from entitlements (`bil.entitlements`, mirror of OH8 `EntitlementChanged`). They set **limits** (custom fields per object, workflows, item types, sandboxes, storage, AI credits) and **feature availability**. A plan downgrade never deletes configuration: settings above the new limit become read-only with a banner ("Your plan allows 25 custom fields; 31 exist. Existing fields keep their data; you cannot add more."). Data entered in those fields remains exportable (NN-11).

**FR-P03-13 — Locks by parent.** An administrator at a parent scope may lock an OPEN value for all children (e.g., an `ORG_OWNER` locks the letterhead for all entities). Children see "Locked by {scope} ({role}, {date})" with a **Request change** action that creates a `wf.items` item of type `CFG_CHANGE_REQUEST` for the locker.

**FR-P03-14 — Direction constraints.** `child_direction` is checked against the parent's resolved value: e.g., `ntf.quiet_hours.window` is `narrow_only` for users (a user may extend quiet hours but not shorten the tenant's); `clm.renewal.reminder_offsets_days` is `raise_only` (a department may remind earlier, never later than the floor).

### 4C. Change pipelines and maker-checker for critical settings

**FR-P03-15 — OPEN change.** Validated (type, bounds, direction, lock, contrast, schema), written to `cfg.setting_changes` with before/after, actor, on-behalf-of, scope and optional reason in the same transaction as the audit-ledger entry (NN-45); effective in ≤ 60 s. Toast "Saved · Undo" for 10 s; history tab per key with "Restore this version".

**FR-P03-16 — Tenant elevation.** A tenant may mark any OPEN key or Studio section "approval required" (`cfg.tenant.require_approval_keys`). Conservative clients (banks, listed companies) thereby apply four-eyes even to operational settings.

**FR-P03-17 — GOVERNED change request.** `cfg.change_requests` with: keys and proposed values, scope, `effective_from`, propagation mode, citation (instrument + provision, URL, `LG-xxx`), plain-language summary (≤ 120 words; Vidhi may draft, the maker owns it), reason, preview result, impact report and attachments. The maker-checker engine of P02 executes approvals; P03 defines the approver rule per sub-class:

| Sub-class | Platform approver | Tenant approver |
|---|---|---|
| `legal` | `PLT_LEGAL_REVIEWER` (reviewer of record) | `ORG_CLO` or designated tenant legal checker |
| `elevated` (money, price, fees, payouts, revenue streams) | `PLT_SUPER_ADMIN` + finance approver in OH8 workflow (P17) | `ORG_OWNER` or `ORG_APPROVER` |
| `elevated` (privilege, access grants, data export of a tenant) | `PLT_SECURITY_OFFICER` | Second `ORG_ADMIN` or `ORG_OWNER` |
| `privacy` | `PLT_DPO` | Tenant DPO role holder if designated, else `ORG_OWNER` |
| `integration` | `PLT_SECURITY_OFFICER` | `ORG_ADMIN` other than the maker |

Maker ≠ checker is enforced (NN-18); a delegate cannot approve an item the delegator made; step-up authentication (≤ 10 minutes old) on approve.

**FR-P03-18 — NN-18 critical-settings list.** These keys carry `maker_checker = Y` regardless of tier, and the CI check `nn18-keys` fails if any is registered with `N`: approval matrices and authority limits; payment, refund and credit settings; access-grant and delivery-grant policies; data-export approval policy; role elevation and break-glass settings; tenant master-data change policy; template, rule and content publication settings; prices, plan limits and revenue-stream switches; bulk-delete policies; agent autonomy ceilings; kill-switch release (engage is single-person, release needs two — §4K); outbound-channel enablement (SMS, WhatsApp, voice); BYO storage targets for regulated data classes.

**FR-P03-19 — Preview and impact.** Before submission the pipeline evaluates proposed and active values side by side over golden cases and over a read-only sample of the tenant's live objects ("14 open agreements would get a new renewal reminder date; 2 would move earlier"). Preview is side-effect-free (no outbox, fake adapters).

**FR-P03-20 — Lead time and expiry.** `effective_from ≥ now + 24 h` for `legal` changes unless `urgent_effective` (the law itself takes effect sooner) is recorded with reviewer approval; multiple future versions may queue. Unapproved requests expire after `cfg.change_requests.expiry_days` (default 14) with notice to the maker; pending approvals escalate after 2 working days.

**FR-P03-21 — Undo and change batches.** Bulk OPEN changes, template applications and imports are one change batch with an undo window (`cfg.batches.undo_window_hours`, default 24). Undo applies compensating changes and is itself audited. After the window, use a new change.

**FR-P03-22 — Every change is explainable.** The history panel shows who, when, scope, before → after, reason, approver, effective date, the request or batch ID and, for platform changes, the "what changed" summary. Tenants see platform-originated changes affecting them in **Settings › Audit & history › Changes made by LawDocs** (SCR-P00-08 / SCR-P03-27; Appendix C).

### 4D. Configuration Studio for every user type (R-047)

**FR-P03-23 — Three faces, one engine.** The same registry and resolver back three surfaces; each shows only keys whose `ui.user_types` include the viewer and whose control class and scope the viewer may change. LOCKED keys are shown read-only with the reason ("Required by law: IT Act First Schedule — wills cannot be eSigned. Learn why" → `hlp.sgn.excluded_instruments`).

| Surface | App and path | Who | Sections |
|---|---|---|---|
| Platform console | `apps/console` `/config/*` | `PLT_*` | Definitions and bounds, brands, plan limits (with P17), rule sets and jurisdiction packs, content release calendar, flags and kill switches, tenant overrides (Correction Entries), Configuration Health across tenants |
| Workspace administration | `apps/web` `/settings/*` (Company), `apps/delivery` `/practice/settings/*` (professional firms), `apps/delivery` `/ch/settings/*` (Consumer Help case desk, brand scope) | `ORG_OWNER`, `ORG_ADMIN`, `ORG_CLO`, `ORG_DEPT_HEAD` (own department), `PRO_FIRM_ADMIN`, `OPS_DELIVERY_LEAD` (Consumer Help) | Organisation, appearance, menus and home, data (fields, statuses, numbering, forms), documents and branding, communications, workflow and items, rules adopted, automations and agents, security and access, integrations, data and exports, plan and billing (P17), account and changes by LawDocs |
| Personal settings | `apps/web` `/me/settings`, `apps/mobile` Profile tab, `apps/delivery` `/me` | Every user | Profile, language, accessibility, appearance, home and quick actions, notifications and quiet hours, reminders for my items, delegation and away, connected accounts, privacy and consents, my data (export, P20) |

**FR-P03-24 — Settings home.** Search box first ("What do you want to change?"), sections grid, recently changed, pending approvals count, Configuration Health summary for admins. Every setting row shows label with "i", class badge, current value, "Set by {scope}", last changed by/when, inherited/override indicator, lock indicator and actions (Change, Reset to inherited, History, Request change).

**FR-P03-25 — Click budgets.**

| Task | Budget |
|---|---|
| Any personal preference (theme, text size, language, quiet hours) | ≤ 2 taps/clicks from home (avatar → setting) |
| Any tenant OPEN value | ≤ 3 clicks from Settings home, or 1 search + 1 click |
| Change a status label from a list screen | 1 click on the column header menu "Rename status…" (admins only) |
| Pin a menu item or quick action | 1 click (pin icon on hover/long-press) |
| Propose a GOVERNED change | ≤ 4 clicks to submit including preview |
| Undo the last change | 1 click from toast or Recent changes |

**FR-P03-26 — Contextual "Configure" links.** Module screens show admins the setting that drives what they see ("Renewal reminders: 60, 30, 7 days before · Change"), opening the setting drawer in place. Users without rights see the value and "Ask admin" (creates a `CFG_CHANGE_REQUEST` item).

**FR-P03-27 — Department heads.** When `ORG_ADMIN` delegates a section to departments (`cfg.delegation.department_sections`), `ORG_DEPT_HEAD` changes those keys for their department only: labels, default owners, reminder cadence, chase cadence, dashboards, quick actions for members, intake form defaults.

**FR-P03-28 — RM and delegated makers (R-064, CH-26).** An `OPS_RM` or `ORG_DELEGATED_MAKER` with `cfg:propose` in the delivery grant (P18) sees the tenant Studio read-only plus **Propose change**. The proposal is a change request whose checker must be a tenant user; the client sees "Proposed by {RM name}, LawDocs" in the approval card. The RM never approves in the client tenant.

**FR-P03-29 — Individuals and families.** `IND_OWNER` manages workspace settings (family-member labels, shared-folder defaults, reminder timing, nominee release policy within P01/P04 locks) from the same Personal settings surface; the Studio uses plain words ("Who in my family can see this folder?") and hides tiers. Guardians (`IND_GUARDIAN`) manage settings for a ward's records within their scope.

**FR-P03-30 — Natural-language settings assistant.** The search box accepts plain requests ("remind me a week earlier before rent agreements expire"; "show Hindi labels to the Jaipur office"). Vidhi (autonomy L2, Appendix H) maps the request to candidate keys, shows current and proposed values, and opens a pre-filled change form. Nothing changes until the user clicks Save (OPEN) or Submit (GOVERNED). Vidhi never writes `cfg` directly.

### 4E. UI/UX customisation

**FR-P03-31 — Themes within accessible tokens.** Themes are sets of overrides on the LD design tokens (`packages/tokens`): primary, accent, surface, radius scale, logo, favicon, illustration style. The validator enforces WCAG 2.2 AA (text ≥ 4.5:1, large text and UI components ≥ 3:1, focus indicator per SC 2.4.11 and 2.4.13 guidance) against both light and dark surfaces; a failing combination cannot be saved and the editor suggests the nearest passing shade. Built-in modes: light, dark, high-contrast (always available to every user, cannot be disabled by any tier — LOCKED), and system. No accessibility overlay widgets (NN-28).

**FR-P03-32 — Density and text.** Density `comfortable` (default), `compact`, `spacious`; text scale 100–200% in 10% steps with reflow to 400% zoom (no horizontal scrolling at 320 CSS px); reduced motion; underline links; dyslexia-friendly font option (from the token set); captions on by default for video (P21); screen-reader verbosity hints. Accessibility preferences are USER tier, follow the person (FR-P03-07) and cannot be overridden by tenant settings.

**FR-P03-31A — Tenant branding as a `brand_pack` layer *(v1.1; IPB-04 §04.3.2, IPB-D-10)*.** The FR-P03-31 theme is stored as the tenant layer of a `brand_pack` (`brd_`, `packages/brand`): logo set (sanitised SVG — scripts, external references and event handlers stripped; PNG fallbacks; favicon), colour tokens validated by the contrast guard (`brand.contrast.min_text` 4.5, `min_ui` 3.0 — platform may only raise), self-hosted fonts only, `brand.app_name` (display name shown in header, titles, e-mails and push for tenants on a white-label plan; LawDocs core plans show "LawDocs"), `brand.terminology` (label overrides per locale; legal definitions and "i" entries never change — FR-P21-123), sender identities (DMARC required). Tenant admins edit within guard-rails in Settings › Customisation › Branding without any super-admin involvement; platform-tier packs (lawdocs.in, `[Consumer Help Brand]`) are maker-checker with `PLT_LEGAL_REVIEWER` on legal-entity fields (P21 FR-P21-05A). Export: the pack is part of `99 System Data/branding.json`.

**FR-P03-33 — Home widgets.** Home is a grid of widgets from the widget catalogue (`cfg.widget_catalogue`; each module registers widgets with data API, permissions, sizes, drill-down, accessible table alternative, refresh interval). Seed widgets: My open items; Waiting on others; Due this week; Awaiting my signature; Expiring documents; Renewals; Next hearings; Trademark deadlines; Recent documents; Vidhi suggestions; Savings this year (P17); Consumer case status (Consumer Help); Team workload (department heads); Legal spend (CLO). Role default layouts set at PLATFORM/BRAND, adapted by tenant per user type or department, personalised by users. **Mandatory widgets** (e.g., "Awaiting my signature" for signers, "Legal deadlines" for `ORG_CLO`) cannot be removed but can be moved.

**FR-P03-34 — Menus.** Menus are data (`cfg.nav_items`, `cfg.nav_overrides`). Tenants hide unlicensed or unused modules, reorder top-level items, rename labels (terminology), set a landing page per user type; users **pin** up to 8 items to the top of the rail (mobile tab bar per P22 FR-P22-03, which governs), reorder pinned items by drag or by keyboard ("Move up/down" menu). Items that cannot be hidden (LOCKED): Home, Inbox/My items, Documents (Vault), Help, Profile and Settings, Privacy and my data, "Changes made by LawDocs" for admins, Audit trail for `ORG_AUDITOR_RO`. "Preview as user type" shows the rail, home and command palette exactly as a chosen user type sees them before saving.

**FR-P03-35 — Quick actions.** A configurable quick-action bar (web header "+" menu, mobile floating action) of up to 6 actions per user, from a catalogue registered by modules: New agreement from template; Upload documents; Upload a folder (P20 intake); Send for signature; Ask Vidhi; Add a court case; Add a trademark; Raise a legal request (to `lgo` intake); Start a consumer complaint (Consumer Help brand); Book a professional. Tenant admins set defaults per user type; users add, remove and reorder. Each action deep-links with context (current folder, current matter).

**FR-P03-36 — Command palette and shortcuts.** `Ctrl/Cmd+K` palette searches records, actions and settings; shortcuts `g h` home, `g s` settings, `/` search; every shortcut can be turned off or remapped per user (WCAG 2.1.4).

**FR-P03-37 — Saved views.** Users save filters, columns and sort on any list and share them with a user type, department or named users; tenant admins publish "official" views.

**FR-P03-36A — Palette PII refusal and result model *(v1.1; IPB-07 §07.4.6)*.** The `Ctrl/Cmd+K` palette (FR-P03-36) classifies every query before search: strings that match Aadhaar (12 digits with Verhoeff check), PAN (`[A-Z]{5}[0-9]{4}[A-Z]`), card PAN (13–19 digits passing Luhn), bank account + IFSC pairs, CVV-like or OTP-like sequences and passport numbers are **refused** — the palette shows "We don't search by identity or payment numbers. Open the record from its list instead." (`hlp.gen.palette_pii_refusal`), logs only the pattern class (never the value), and never sends the string to the search index, analytics or Vidhi. Results follow the IPB-07 model: `record`, `action`, `setting`, `help`, `glossary` (plain definition inline), `vidhi` (ask), each with scope badge and keyboard reach; actions respect Cerbos and maker-checker (an action that needs approval opens the approval screen, never executes). Tenants cannot disable the refusal (`cfg.palette.pii_refusal` LOCKED true).

**FR-P03-38 — Language and terminology per locale.** UI language per user from the D-07 launch set; tenant terminology overrides are stored per locale; a missing tenant translation falls back to the platform translation, never to a blank label. Legal terms with statutory meaning (e.g., "Stamp duty", "Power of attorney", "Affidavit") are LOCKED labels with tenant-editable help text only.

### 4F. Data customisation: labels, fields, statuses, numbering, forms

**FR-P03-39 — Field labels.** Tenants relabel any non-statutory field per locale (e.g., "Counterparty" → "Vendor/Customer"); the canonical field name remains in APIs and exports, and the "i" tooltip shows "Also called: Counterparty".

**FR-P03-40 — Custom fields.** On agreements, documents, folders, matters, cases, hearings, trademarks, engagements, consumer cases, parties, items and requests. Types: text, long text, number, decimal, money, date, date-time, boolean, single/multi-select (tenant list), user, department, entity, party, URL, document reference, formula (CEL, read-only). Each field: label (multi-locale), help text (feeds "i"), required-at-status, visibility and edit rights by role, PII class (`none`, `personal`, `sensitive`), searchable flag, export column name. Plan limit on count (Appendix R `cfg.custom_fields.max_per_object`). Custom fields appear in APIs and exports automatically (NN-11); `sensitive` fields are field-level encrypted and excluded from search and AI context unless the user may read them.

**FR-P03-41 — Custom status sets.** Per object type, tenants define labels, order, colours (contrast-checked, with icon), required fields on entry, allowed transitions **within** the canonical graph (they may remove optional transitions, never add one the canonical graph forbids), and whether entry needs a checker. Every tenant status maps to one canonical state (LOCKED); reports, evidence packs, exports and ecosystem events use canonical states with tenant labels as display fields. Example for agreements — canonical states per Appendix A §A.30 (which governs): `DRAFT`, `IN_NEGOTIATION`, `IN_APPROVAL`, `APPROVED`, `LOCKED_FOR_SIGNATURE`, `IN_SIGNATURE`, `SIGNED_PENDING_FORMALITIES`, `EXECUTED`, `RENEWED`, `TERMINATED`, `EXPIRED`, `CANCELLED`; a tenant may show "With legal", "With vendor", "Board approval" as sub-statuses of `DRAFT`, `IN_NEGOTIATION` and `IN_APPROVAL`. `EXECUTED` is reachable only through the formalities gate (NN-40, §4J FR-P03-79).

**FR-P03-42 — Reason codes.** Tenant-managed lists for: return for rework, rejection, cancellation, waiver of formality, termination, item closure, wait reasons, extension reasons. Some lists carry LOCKED minimum entries (e.g., formality waiver requires one of: "not legally required for this instrument", "completed outside LawDocs — evidence attached", "counsel advised", "other with text ≥ 20 characters").

**FR-P03-43 — Numbering schemes.** The permanent business reference (`LD-AGR-2026-000123`, `LD-MAT-…`, `LD-CAS-…`) is generated by `core` and never changes (LOCKED). Tenants may add a **display reference** per object type and entity using a pattern of tokens: `{ENTITY_CODE}`, `{DEPT_CODE}`, `{FY}` (e.g., `2026-27`), `{CY}`, `{MM}`, `{SEQ:n}` (zero-padded, sequence per scope), `{TYPE_CODE}`, literal text and separators `/ - _`. Example `ABC/LEG/{FY}/{SEQ:4}` → `ABC/LEG/2026-27/0045`. Rules: uniqueness per scope enforced; sequences gap-tolerant (cancelled numbers are not reused); reset per FY or CY optional; changing a pattern applies to new records only; display references are searchable and exported alongside the permanent ID. Errors: `LD-CFG-030` duplicate, `LD-CFG-031` invalid token.

**FR-P03-44 — Form layouts.** Drag-and-drop arrangement of standard and custom fields into sections and tabs for intake and edit forms (agreement request, legal request, matter intake, consumer complaint intake); conditional visibility (CEL); preview as user type; versioned (records keep the form version they were created under); accessibility lint at publish (label association, order, error messages, no colour-only cues).

**FR-P03-45 — Tags and folder views.** Tenants and individuals define tag sets; vault folder names visible to users are **views** over canonical IDs and categories (P04, NN-12), so a renamed folder never moves a document and never breaks an export path.

### 4G. Communications and document branding

**FR-P03-46 — Notification templates.** Per event type, channel (in-app, email, push, SMS, WhatsApp, RCS, Microsoft Teams/Google Chat connector), locale and audience; variables from a whitelisted schema per event (never document content, OTPs or Aadhaar — NN-32); preview with sample data; plain-text alternative; accessibility lint (descriptive link text, no meaning by colour). SMS and WhatsApp templates must carry the DLT template ID and the approved header or the registered WhatsApp template name before activation (NN-34; `ntf.dlt.require_template_id` LOCKED); edits to an SMS/WhatsApp body create a new template version pending registration, and the old version keeps sending until the new one is registered.

**FR-P03-47 — Channel policy.** Priority (P1–P4) to channel mapping, digest times, quiet hours (tenant default; user `narrow_only`), daily interruptive budget per user (default 15; P1 items such as "signature expiring today" and security alerts are never budgeted), de-duplication window. Counterparty rules are LOCKED (NN-34): one LawDocs-originated invitation plus reminders the counterparty has not opted out of; no automated calls until opt-in; every message carries an opt-out.

**FR-P03-48 — Email sender identity.** Tenant sender name and, on Business plans and above, a verified sender domain (SPF, DKIM, DMARC checks via `DNS_CHECK_PORT`); until verified, mail goes from the brand's domain "on behalf of {Tenant}".

**FR-P03-49 — Document branding and letterheads.** Letterhead (header, footer, logo, watermark text, page numbering style, font from the token set), cover pages for reports and evidence packs, signature-page styling, and footer text per entity. Applied by `packages/docgen` to DOCX and PDF renditions. LOCKED: the legal body of a template, statutory notices, stamp-paper layouts, evidence-certificate wording (BSA 2023 s.63 — NN-10), AI labels (NN-14) and the "e-acceptance" vs "eSign" distinction (R3 LG-001) cannot be hidden or restyled into illegibility (minimum font size and contrast enforced).

**FR-P03-50 — Suite-neutral templates.** Email and document templates render identically whether the tenant uses Microsoft 365 or Google Workspace (R-053, R-055); "Open in Word" and "Open in Google Docs" links are settings of the connected suite (P19), not template variants.

### 4H. Rule engine (`rul`)

**FR-P03-51 — Port and engines.** All rule evaluation goes through `RULES_PORT` (`packages/rules`). Default adapters: **GoRules ZEN** (JSON Decision Model: decision tables, expression nodes, switch nodes; Node binding) for business-readable rules, and **CEL** (Common Expression Language; non-Turing-complete, sandboxed, cost-bounded) for small predicates inside settings, routing conditions, form visibility and item triggers. A sprint-1 ADR confirms library versions and licences [VERIFY at P03 start: ZEN Node binding maturity and licence; CEL JavaScript implementation] and records JSON Logic as the fallback adapter. No module embeds legal logic in code where a rule set exists (lint `no-hardcoded-legal-rules` flags literals tagged `@legal` outside `packages/rules`).

**FR-P03-52 — Determinism.** Evaluation is a pure function of `(rule_set_version, inputs, as_of)`: no network, no clock reads except the supplied `as_of`, decimal arithmetic, no randomness. Every evaluation that drives a user-visible decision is recorded (`rul.evaluations`: rule-set ID and version, input hash, output, `as_of`, caller, object reference) so that "why was this blocked?" is answerable later and reproducible from the export.

**FR-P03-53 — Rule-set identity.** `rulepack.<jur>.<domain>.<name>@<YYYY.N>`; `jur` ∈ `IN`, `IN-<ST>` (ISO 3166-2:IN), `INTL`, ISO country code; tenant-authored sets `rulepack.T-<tenant>.<domain>.<name>` (internal policies only; labelled "{Tenant} rule — not reviewed by LawDocs").

**FR-P03-54 — Seed rule-set catalogue.** Registered here, content owned by the named phase (full list Appendix R §R.6). Key sets: the legal-rules register runtime (one row per R3 `LG-xxx` used by code); instrument eligibility `IN.sgn.eligibility` (instrument × signer type × State → `ESIGN_OK`, `DSC_OK`, `WET_INK_ONLY`, `REGISTRATION_REQUIRED`, `NOTARY_REQUIRED`, `STAMP_REQUIRED`; P08, Appendix F); formalities `IN.sgn.formalities`; State stamp-duty tables and eStamp channels `IN-<ST>.stamp.*` (data only, [VERIFY] per State; P08); limitation advisory `IN.lit.limitation_advisory` (Limitation Act 1963 Schedule; output "Advisory — confirm with counsel", R3 LG-092; P11); consumer-forum timelines `IN.chp.rbios_2026` and Insurance Ombudsman (P15, [VERIFY] clauses); privacy, intermediary and CERT-In clocks (P01, P23); default reminders and SLA calendars (P03); marketplace profession rules (P16); telecom `IN.ntf.tcccpr` (P19, [VERIFY]).

**FR-P03-55 — Lifecycle and reviewer of record (NN-30).** States `DRAFT → IN_REVIEW → APPROVED → SCHEDULED → ACTIVE → SUPERSEDED → RETIRED`; side exits `REJECTED`, `WITHDRAWN`. Activation requires: schema and semantic validators green; each row cites an instrument and provision or an `LG-xxx`; source document SHA-256 on file; golden suite with ≥ 1 positive and ≥ 1 negative case per row; declared fallback; `next_review_due`; and a **reviewer of record** — a named `PLT_LEGAL_REVIEWER` (advocate, CS or CA as the domain requires; enrolment or membership number held in the professional registry) who is not the maker. The reviewer's name, qualification and review date are stored on the version and shown in the rule's "Source and review" panel. Publishing a rule set never requires a code release, and a code release never changes a published rule (`NN-30_release_does_not_touch_rules`).

**FR-P03-56 — Effect classes.** `protective` (blocks, warns, discloses, escalates): maker → reviewer. `computational` (dates, amounts, thresholds): maker → reviewer → owning function (P08 for stamp duty; P15 for consumer clocks). `permissive` (enables a route or relaxes a block, e.g., a new State allowing eStamp for an article): maker → reviewer → `PLT_SUPER_ADMIN` publisher; cited facts must be `VERIFIED`. `emergency_block` (e.g., an ESP licence lapses — R3 LG-005): `PLT_LEGAL_REVIEWER` + `PLT_SECURITY_OFFICER`, immediate, post-incident review within 5 working days.

**FR-P03-57 — Verification status (NN-38).** Every row and parameter carries `VERIFIED` (primary source checked and logged in `docs/compliance/verification-log.md`), `SECONDARY_ONLY` or `NOT_CONFIRMED`. Protective rows may run while `SECONDARY_ONLY`; computational rows may run while `SECONDARY_ONLY` only with outputs labelled "Indicative — under verification"; permissive rows need `VERIFIED`; a `NOT_CONFIRMED` row cannot drive a payment, a filing, an execution status or a user-facing legal statement — the declared fallback applies (usually `advisory_only` or `block`).

**FR-P03-58 — Golden cases, preview, sandbox.** Golden cases live in `packages/rules/fixtures/<set>/*.json` (platform) and `rul.golden_cases` (tenant). The preview diff shows changed outcomes per golden case and, for platform sets, counts of affected in-flight objects across tenants (IDs and counts only). Tenants test their own rule sets and workflows in the configuration sandbox (§4M).

**FR-P03-59 — Instance pinning and propagation.** Objects record the rule-set version that decided them (a signing request pins the eligibility and formalities versions at creation; a stamp computation pins the duty table version). Propagation modes per version: `prospective` (default), `open_items_with_notice` (dry-run list of affected open objects; owners get an item; tenant banner), `emergency_block` (immediate protective block on new actions; existing completed actions untouched).

**FR-P03-60 — Review dates.** Default `next_review_due` 180 days; 90 days for `SECONDARY_ONLY`; 30 days for volatile sets (DPDP commencement, TCCCPR, RB-IOS 2026, State stamp-duty tables in a budget month). Overdue → owner item, console banner, and the declared fallback applies to new decisions.

**FR-P03-61 — Tenant adoption.** Platform legal sets are `auto_follow` (default) or `pinned` for ≤ `rul.adoption.max_pin_days` (default 30; 0 for protective sets). Tenants may layer **stricter-only** adaptations on an allow-list (e.g., require notarisation of all leases even where not mandatory) and author `T-` sets for internal policy (approval thresholds, house rules). Tenants can never relax a protective platform row. A tenant that believes a platform rule is wrong files a **rule challenge** with sources; LawDocs responds within 10 working days.

**FR-P03-62 — "What changed" notices.** On activation of a platform set affecting tenants: plain-language summary (≤ 120 words, English plus the tenant's primary language as a labelled machine translation — NN-48), parameter diff table, citation, effective date, tenant action (`none`, `review`, `configure`) and tenant-specific counts. Delivered as a digest to admins and as a "What changed" tab; where action ≠ none, an admin acknowledges.

### 4I. Content-version framework (templates, clauses, glossary, help)

**FR-P03-63 — One framework, many content kinds.** `rul.content_kinds` registers versioned legal content types: template (`tpl_`), clause (`cls_`), questionnaire, eligibility row, jurisdiction variant, glossary term (`trm_`), help article, tutorial (`tut_`), notification template with legal text, retention schedule. Each version carries: jurisdiction scope, effective dates, sources, change summary, maker, reviewer of record, verification status, locale, and a content hash. Owner phases (P06, P21, P04) build their editors on this framework.

**FR-P03-64 — Content release calendar.** A console calendar lists scheduled content and rule activations by date and jurisdiction; it is independent of the code release calendar (P23). Content may publish during a code freeze; code may not alter published content.

**FR-P03-65 — Pinning in documents.** A draft or executed document records the template, clause and questionnaire versions used. Updating a template never changes an existing draft; the drafter sees "A newer version of this clause is available — compare" with a redline (P06).

**FR-P03-66 — AI-labelled content.** Content drafted with Vidhi carries `ai_assisted = true` until a reviewer of record approves; individual-facing AI-customised documents keep the label "AI draft — not reviewed by a professional" until a qualified reviewer approves (NN-14).

### 4J. Open, interim and waiting items engine (`wf.items`)

**Design conclusion.** Legal work stalls mostly while someone else acts: a counterparty reviewing a redline, a Sub-Registrar giving an appointment, a court issuing a certified copy, an insurer replying to a complaint, an ESP recovering from an outage, a client sending documents to its RM. Tools that model these as free-text notes lose them. LawDocs makes them **first-class items** with a type, an owner, a waiting party, clocks and chasers. Labels, types, owners, cadences and internal SLAs are configurable (R-047). Legal clocks are not: a court, a limitation period or a regulator does not stop counting because a party is slow. This mirrors how mature work-management and GRC tools keep a fixed internal state model behind configurable labels so that reports, automation and audit stay reliable.

**FR-P03-67 — Item model.** `wf.items` (`itm_`): `item_type_code`, `parent_ref` (any record: agreement, document, signing request, matter, case, hearing, trademark, engagement, consumer case, request, import job), `title`, `canonical_state`, `tenant_status_code`, `owner_user_id` / `owner_team_id`, `watchers[]`, `priority` (P1–P4), `opened_at`, `due_at`, `clocks[]`, `waiting` (sub-record), `interim` (sub-record), `chase_policy_id`, `escalation_ladder_id`, `visibility` (`internal`, `shared_with_parties`), `external_label` (shown to counterparties if shared), `source` (`user`, `rule`, `agent`, `integration`, `import`), `created_by`, `resolved_at`, `resolution_code`, `evidence_refs[]`. Items inherit the parent record's permissions; they never widen access.

**FR-P03-68 — Canonical states (LOCKED).**

| Canonical state | Meaning | Counts as done? |
|---|---|---|
| `OPEN` | Created, not started | No |
| `IN_PROGRESS` | Owner working | No |
| `INTERIM` | Partly done; an interim outcome recorded (e.g., application filed, acknowledgement received, first draft sent) | No — interim never counts as complete in reports or the formalities gate |
| `WAITING` | Blocked on another party (§FR-P03-70) | No |
| `ON_HOLD` | Paused by an authorised user with a reason (internal decision) | No |
| `RESOLVED` | Outcome achieved, evidence attached where the type requires it | Yes |
| `WAIVED` | Not required, by an authorised user with a reason code (formalities waivers need `ORG_CLO`/`ORG_APPROVER` or the individual owner; NN-40) | Yes (labelled "Waived") |
| `CANCELLED` | No longer relevant (parent cancelled, duplicate) | n/a |
| `SUPERSEDED` | Replaced by another item | n/a |

Tenants add their own statuses mapped to these states (§4F); transitions follow the canonical graph in Appendix R §R.8.

**FR-P03-69 — Item types.** `wf.item_types` (platform seed + tenant-defined; catalogue in Appendix R §R.11): code, name (multi-locale), parent record types allowed, default owner rule (record owner, role in department, assignee of parent, named user, round-robin pool, the RM under a delivery grant), default priority, required evidence to resolve, allowed waiting-party types, default chase policy, internal SLA, escalation ladder, whether waiting pauses the internal SLA, whether the type participates in the formalities gate, auto-create triggers (CEL on parent events, e.g., `agreement.status == 'SIGNED_PENDING_FORMALITIES' && rules.formalities.registration_required`), auto-resolve triggers (e.g., signing request completed). Tenants and individuals define types within plan limits; platform types carry LOCKED parts (e.g., `AGR_STAMP_PENDING` cannot drop its "certificate UIN verified" resolve condition — NN-08).

**FR-P03-70 — Waiting record.** Fields: `party_type` (enum below, extensible by tenant only as sub-types), `party_ref` (user, department, party `prs_`, organisation, professional `pro_`, court `cas_`/forum code, registry office code, regulator code, vendor adapter code, connector ID), `reason_code`, `requested_at`, `expected_by`, `external_reference` (e.g., complaint number, diary number, application number, token number), `chase_policy_id`, `internal_sla_paused`, `legal_clock_refs[]` (read-only), `last_chased_at`, `chase_count`, `response_received_at`, `notes`.

| `party_type` | Examples | How chasing works |
|---|---|---|
| `INTERNAL_USER`, `INTERNAL_DEPARTMENT` | Approver, finance team, board secretariat | In-app/email/push; escalation ladder |
| `CLIENT` | Retainer client owing documents to its RM (P18) | Client portal item + email; client sees it in "Waiting on you" |
| `COUNTERPARTY` | Other party reviewing a draft, signing, paying stamp share | Email/SMS/WhatsApp within NN-34; confirm-mode rules (FR-P03-73) |
| `SIGNATORY`, `WITNESS`, `NOTARY` | Pending signature, witness attestation, notary appointment | As counterparty for external persons; signing reminders via P08 |
| `PROFESSIONAL` | Engaged advocate, CA, CS delivering a deliverable (P16) | Engagement thread + SLA from the engagement (eSigned SLA, R-039) |
| `COURT` | Order awaited, certified copy, next date, defect cure listing | **Never contacted automatically**; internal "Check status" task with deep link; court-data refresh via licensed aggregator where configured (P11), staleness shown (NN-05) |
| `REGISTRY` | Sub-Registrar, ROC/MCA, Trade Marks Registry, GST/tax office | **Never contacted automatically**; status-check task + deep link; user-entered application number (NN-05; CH-27) |
| `REGULATOR` | RBI Ombudsman (CMS), Insurance Ombudsman, IRDAI Bima Bharosa, consumer commission | **Never contacted automatically**; countdown and status-check tasks (P15) |
| `GOVERNMENT_PORTAL` | Parivahan/Vahan, e-challan, DigiLocker outage | Status-check task; deep link; no automation of the portal |
| `VENDOR` | ESP, eStamp vendor, KYC vendor, court-data aggregator | Adapter health and status API polling where the adapter supports it; vendor support ticket template |
| `ECOSYSTEM_SYSTEM` | Awaiting LDC, Equator, Finbyx or Udofin via `int` | Event correlation; auto-resume on the matching event |
| `PAYMENT` | Awaiting payment confirmation from OH8/Razorpay | Auto-resume on `SubscriptionPaymentReceived`/order paid; never treat a browser redirect as proof |
| `OTHER` | Free text with reason | Manual |

**FR-P03-71 — Clocks.** Each item can carry several clocks; each clock has `kind`, `starts_at`, `due_at`, `source` and `pausable`:

| Kind | Examples | Pausable? |
|---|---|---|
| `LEGAL` | Limitation date (advisory), statutory or regulator deadline, court date, TM opposition window, RB-IOS filing window, DPDP 90-day response | **Never** (LOCKED) |
| `CONTRACTUAL` | Notice period, renewal option window, lock-in, payment due under the agreement | Never by the system; a user may record an agreed extension with evidence, which creates a new clock version |
| `EARLIEST_ACTION` | Waiting period before the next step is allowed (e.g., 30 days after complaining to the RE before approaching the RBI Ombudsman under RB-IOS 2026 [VERIFY clause]) | Never; when it ends, the item suggests the next action |
| `INTERNAL_SLA` | Tenant's own target (first response, review turnaround) | Only if the item type allows and the wait reason is on the pausable list |

A legal clock approaching its due date (`wf.items.legal_warning_days`, default 7, `raise_only` against platform floor 3) escalates to L2 regardless of waiting or hold state, with the banner "Legal deadline approaching while waiting on {party}" (`NN-29_legal_clock_never_pauses`).

**FR-P03-72 — Chase policies.** `wf.chase_policies`: cadence (ISO 8601 duration or RRULE), first chase offset, `max_chases`, channels per party type, templates per locale, business-hours calendar, quiet hours, stop conditions (response received, parent state change, opt-out), and escalation after the last chase.

**FR-P03-73 — External chasers and human confirmation (NN-13, NN-34).** Messages to anyone outside the tenant are external side effects. Modes:

- `CONFIRM_EACH` (default): at each due time the owner gets a ready-to-send chaser in "My items" — one tap sends it.
- `PRE_APPROVED_SERIES` (GOVERNED, `maker_checker = Y`): allowed only for **transactional** templates tied to an action the recipient has already been invited to (sign, review a shared draft, upload a requested document); the authorising user approves the whole bounded series (recipients, template versions, dates, `max_chases ≤ 5`) on one confirmation screen listing every send; any change to recipients, template or count re-opens confirmation. [INTERP: a single informed confirmation of a fully enumerated, bounded series is the per-action confirmation NN-13 requires; owner to confirm — OI-P03-05.]
- Never: automated calls before opt-in, chasers to courts, registries, regulators or government portals, chasers by agents without a human confirmation.

Every chase is idempotent (key = item ID + chase sequence; NN-46), logged on the item and in the counterparty's message history, and respects opt-outs.

**FR-P03-74 — Escalation ladders.** Levels L1–L3 with time offsets and recipients: L1 owner; L2 department head or matter lead (Company), delegate or family member (Personal, if set), `OPS_DELIVERY_LEAD` (Delivery and Consumer Help); L3 `ORG_CLO` or `ORG_OWNER`. L3 is mandatory for items with a `LEGAL` clock.

**FR-P03-75 — Interim outcomes.** Interim records capture what was achieved (e.g., "Application filed — diary no. entered", "Stamp duty paid — awaiting certificate", "Draft sent to counterparty"), with evidence and the next check date. An interim outcome can set a new waiting record in one action ("Filed; now waiting on Registry").

**FR-P03-76 — Bulk and quick actions.** From lists: set waiting (party, reason, expected by), reassign, change priority, snooze internal SLA (if allowed), resolve with evidence; keyboard and screen-reader accessible; bulk actions over 50 items preview first and are one undoable batch.

**FR-P03-77 — Views and widgets.** "My items", "Waiting on others" (grouped by party type, ageing buckets 0–7, 8–30, 31–90, > 90 days), "Waiting on me" (for clients and counterparties, shared items only), "Legal deadlines", "Stalled" (no activity in N days), calendar view of `due_at` and clocks, team workload. Each widget has an accessible table alternative.

**FR-P03-78 — Shared items.** Items with `visibility = shared_with_parties` appear to the relevant counterparty, client or professional with `external_label` only ("Awaiting your signature", "Please upload the property tax receipt"); internal notes, reasons, owner names (if configured) and other items are never shown externally (NN-37 spirit).

**FR-P03-79 — Formalities gate (NN-40).** For an agreement or instrument, P08 creates one item per required formality from `IN.sgn.formalities` (stamp, witnesses, notarisation, registration, board approval, counterparty signatures). The parent cannot enter canonical `EXECUTED` until each formality item is `RESOLVED` (with evidence) or `WAIVED` (authorised user, reason code from the LOCKED list). The gate check calls `RULES_PORT` and records the evaluation.

**FR-P03-80 — Agents and items.** `AGT_*` agents may create items, propose waiting records and draft chasers (maker only); they cannot resolve items that require evidence review, waive formalities, or send external chasers (NN-13, NN-43). Agent-created items show the agent and its human sponsor.

**FR-P03-81 — Module adoption.** Every module that has "not closed" work uses `wf.items` through `packages/workflow`; a module-local "pending" table without an item mirror fails the `items-adoption` architecture test. Module tables that already name waiting items (e.g., P13 `lgo.waiting_items`) are implemented as read projections over `wf.items` filtered by parent type, so chasers, clocks, escalations and exports stay in one engine. Minimum adopters by Wave 1 exit: `clm`, `sgn`, `dms` (import review), `drf` (AI draft review); by Wave 2 exit: `dix` (type-copy review), `mkp` (engagement deliverables), `sdc` (client approvals). Each adopter is checked at its own phase exit, not at P03's.

**FR-P03-82 — Ecosystem.** Items waiting on another Infrabyx product resume on matching events received through `int` (NN-24); item contents never leave LawDocs; only status counts may reach the Operations Hub aggregates (NN-19).

### 4K. Feature flags and kill switches

**FR-P03-83 — Flags as registered settings.** Feature flags are boolean or variant keys `<module>.flag.<feature>` in the same registry, with: owner, purpose (`release`, `experiment`, `ops`, `permission`, `verify_gate`), targeting (brand, plan, tenant segment, release ring, user type, percentage with sticky hashing on `tenant_id`), default, expiry date for `release` flags (stale-flag check after 90 days), and linked `[VERIFY]` entry for `verify_gate` flags (NN-38: OFF or advisory-only until verified). An OpenFeature-compatible evaluation API is exposed to apps; any external flag service is an adapter behind the registry [REC; ADR at sprint 1].

**FR-P03-84 — Kill switches (NN-39).** Registered for every AI agent (`agt.kill.<agent>`), Vidhi as a whole (`ai.kill.vidhi`), each revenue stream (`bil.kill.<stream>`), each vendor adapter (`int.kill.<adapter>`: ESPs, eStamp vendors, KYC vendors, court-data aggregators, TM data partners, AI providers, storage connectors), each consumer vertical (`chp.kill.<vertical>`: loan grievance, insurance grievance, credit-report dispute, challans, vehicles), each outbound channel (`ntf.kill.<channel>`: email, SMS, WhatsApp, RCS, voice, push) and advertising (the advertising stream's `bil.kill.<stream>` switch; D-13, NN-35). Scopes: PLATFORM (console), BRAND, TENANT (for tenant-usable agents, channels and connectors). Every switch, wherever it is engaged (console, P09 agent workforce, P19 connector console), is a row in `cfg.kill_switches` (registry scopes `AI_AGENT`, `REVENUE_STREAM`, `VENDOR_ADAPTER`, `CONSUMER_VERTICAL`, `OUTBOUND_CHANNEL`, `CONNECTOR`, `CREDENTIAL_REVEAL`, `BRAND`; Appendix A §A.17) and every change emits only `in.lawdocs.cfg.KillSwitchEngaged.v1` or `in.lawdocs.cfg.KillSwitchReleased.v1` with `scope` and `target`; module-specific aliases (`core.KillSwitchChanged`, `agt.KillSwitchActivated/Released`, `int.KillSwitchToggled`) are retired (R-A-09). Module settings that tune behaviour on engagement (e.g., P09 agent pause behaviour) stay with their module but never create a second registry.

**FR-P03-85 — Engage and release.** Engaging a kill switch is single-person (any authorised role) with reason, effective ≤ 60 s, and verified by a propagation probe shown on screen. Releasing needs a second authorised person (NN-18) and a recorded check that the cause is resolved. In-flight work fails safe: agent missions stop and pending tool calls are refused; queued outbound messages are held, not dropped; signing ceremonies in progress are paused with a user-facing notice and resumable through another adapter only if the user confirms (D-12).

**FR-P03-86 — Drills.** Platform switches are drilled quarterly on a test tenant (`cfg.kill_switch.drill_frequency_days`, default 90); drill evidence goes to P23 control evidence. Overdue drills raise an item to the switch owner.

**FR-P03-87 — Flag rollout.** Release flags support rings (P23): `ring0` internal tenants, `ring1` opt-in early access, `ring2` general. A flag cannot be removed from code while any ring still depends on it; removal is a change with the flag-cleanup check.

**FR-P03-88 — Transparency.** Tenants see the state of kill switches and flags that affect them (e.g., "eStamp in Maharashtra is temporarily unavailable — use physical stamp paper or try later") with an "i" explanation; internal flag names are not shown.

### 4L. Effective-dated changes

**FR-P03-89 — Scheduling.** GOVERNED and selected OPEN keys (`effective_dating = scheduled_allowed`) accept `effective_from` (and optional `effective_to`). `ConfigActivationWorkflow` (Temporal) re-validates at activation; failure keeps the old value and raises an item to the maker.

**FR-P03-90 — Bitemporal history.** Values store `valid_from`/`valid_to` (business time) and `recorded_at` (system time); "as of" reads return what was in force on a date and what the system believed at a time. Exports carry both (P20).

**FR-P03-91 — Future view.** Settings screens show "Changes scheduled" with countdowns; Compare (FR-P03-96) can compare today with any future date.

**FR-P03-92 — Backdating.** Not allowed for settings. Corrections of past effects are business transactions (e.g., a corrected reminder, a re-issued notice) or Correction Entries (FR-P03-98), never retroactive setting edits.

### 4M. Configuration templates, export/import, sandbox, compare

**FR-P03-93 — Configuration bundle.** `ld-config-1.0`: signed JSON (JWS, tenant export-signing key) plus a human-readable XLSX (one sheet per Studio section) containing OPEN and tenant-GOVERNED values, terminology, custom fields, status sets, reason codes, numbering patterns, forms, item types, chase policies, escalation ladders, quick-action and menu defaults, dashboards, notification templates (tenant versions), letterheads (as assets), adopted rule-set versions and tenant `T-` rule sets. Never included: secrets, credentials, personal data, user-level preferences (unless the user exports their own). Included automatically in `LD-EXPORT-1.0` (P20; Appendix K `99 System Data (CSV and JSON)/Settings and Customisations/`).

**FR-P03-94 — Templates of configuration.** `cfg.config_templates`: (a) platform library seeded by LawDocs (e.g., "Startup — lean", "SME — two-person approval", "NBFC legal department", "Law firm practice", "Individual — family vault", "Consumer Help desk"); (b) tenant-saved templates shared within a group of tenants under a `tenant_link`; (c) an RM or `OPS_ONBOARDING` may **offer** a template to a client (maker only; the client admin applies it). Applying a template shows a section-by-section diff, applies as one change batch (undo 24 h), turns GOVERNED sections into change requests, and records `cfg.template_applications`.

**FR-P03-95 — Import between tenants.** Importing a bundle into another tenant (sister entity, new workspace, sandbox): dry-run diff; LOCKED and out-of-bound values rejected with reasons (`LD-CFG-070`); references re-mapped by code (departments, users by email only when the admin confirms each match); GOVERNED values become change requests.

**FR-P03-96 — Compare.** Two scopes or two dates ("Legal vs Finance department", "today vs 1 April 2027"), filterable by class, module and "changed from default".

**FR-P03-97 — Sandbox.** A tenant admin opens a configuration sandbox (clone of configuration with synthetic sample records; no personal data; outbound adapters replaced by fakes), tries settings, templates, item types, forms and tenant rule sets, then promotes the tested bundle as one change batch or change request. Sandboxes are plan-limited.

### 4N. Super-admin overrides and support access (CH-26, R-066)

**FR-P03-98 — Correction Entries.** `PLT_SUPER_ADMIN` may change a tenant's OPEN or GOVERNED value, enable or hide a module or section for the tenant, or correct configuration-linked master data only through a **Correction Entry** (`core.correction_entries`): target, old value (sealed copy), new value, reason code (P00 FR-P00-37 list: `DATA_ENTRY_ERROR`, `CLIENT_REQUEST`, `LEGAL_ORDER`, `MIGRATION_FIX`, `CONTENT_ERRATUM`, `SECURITY_INCIDENT`, `DUPLICATE`, `OTHER`), justification (≥ 50 characters, `core.correction.justification_min_chars`), evidence (ticket or client email reference), requester and a second platform approver (`PLT_SUPER_ADMIN` or `PLT_SECURITY_OFFICER`), both with step-up. For **crucial client details** (legal name, CIN/LLPIN, PAN, GSTIN, registered address, authorised signatories, approval matrix), the entry also requires **client approval** by `ORG_OWNER` or `ORG_ADMIN` (CH-26) unless a legal order or security incident is recorded (then the client is notified within 24 hours). The original value is never mutated (NN-02); the tenant sees each entry in SCR-P03-27 and gets a notification.

**FR-P03-99 — Emergency override.** For lock-outs or incidents, `PLT_SUPER_ADMIN` with `PLT_SECURITY_OFFICER` may apply an emergency override (`APPLIED_EMERGENCY`, Appendix A §A.1); the tenant is notified within 24 hours and the tenant owner ratifies; un-ratified overrides auto-revert after 24 hours where reversible and raise a P1 alert.

**FR-P03-100 — Not overridable.** LOCKED values, NN tests, ledger existence and order, and any value whose change would widen access to a tenant's documents (that needs the tenant's own grant — NN-17).

**FR-P03-101 — Support sessions.** Tenant-granted `SUPPORT_SESSION` grants (P02 FR-P02-51): section-scoped, time-boxed (≤ `iam.support_session.max_minutes`, default 60), read-only; banner visible to tenant users; full log in the access-transparency view (P18).

### 4O. Configuration Health and documentation

**FR-P03-102 — Health dashboard.** Fallbacks in force; rule sets past review; pinned sets near expiry; flags past expiry; kill switches engaged; drills overdue; items stalled beyond ladders; workflows or approval matrices where maker could equal checker (must be zero); custom forms with accessibility failures; templates applied with pending GOVERNED sections; unregistered keys (platform view; must be zero).

**FR-P03-103 — "Explain my configuration".** Generates a DOCX and PDF/A description of the tenant's configuration (approval matrices, item types and SLAs, numbering, adopted rule sets with versions, kill-switch states, changes made by LawDocs) for auditors, plus a diff report between two dates.

**FR-P03-104 — Help keys.** Every Studio section and every key has an "i" help key registered in `hlp` before release (`help-key-lint`). Seed keys this phase: `hlp.cfg.locked`, `hlp.cfg.needs_approval`, `hlp.cfg.editable`, `hlp.cfg.inherited`, `hlp.cfg.effective_date`, `hlp.cfg.maker_checker`, `hlp.cfg.numbering_scheme`, `hlp.cfg.custom_field`, `hlp.cfg.canonical_status`, `hlp.cfg.config_template`, `hlp.cfg.sandbox`, `hlp.rul.rule_set`, `hlp.rul.reviewer_of_record`, `hlp.rul.verification_status`, `hlp.rul.indicative`, `hlp.wf.open_item`, `hlp.wf.interim`, `hlp.wf.waiting`, `hlp.wf.legal_clock`, `hlp.wf.internal_sla`, `hlp.wf.earliest_action`, `hlp.wf.chaser`, `hlp.wf.escalation`, `hlp.wf.formalities_gate`, `hlp.cfg.kill_switch`, `hlp.cfg.feature_flag`.

**FR-P03-105 — Studio documentation for developers.** `docs/config/`: how to add a setting (tier test, Appendix R row, help key, codegen), how to add a rule set (fixtures, citations, reviewer), how to add an item type, how to add a kill switch; runbooks for emergency blocks and overrides.

---

### 4P. IPB-07 Settings-tree alignment and Security sub-items *(v1.1)*

**FR-P03-106 — Twenty-node tree.** The Settings home (SCR-P03-01) is organised in the binding IPB-07 §07.4.2 order and names — 1 Profile · 2 Security · 3 Privacy & consents · 4 Accessibility · 5 Appearance · 6 Notifications · 7 Customisation · 8 Organisation & people · 9 Billing · 10 Invoices · 11 Plans & subscription · 12 Storage & data · 13 Audit trails · 14 Integrations · 15 AI & Vidhi · 16 Feedback · 17 Tutorials & help · 18 Security & trust · 19 What's new · 20 About — with LawDocs' additions placed at the end of each tier group (LawDocs team, Documents and templates, Rules and automations, Tools). The v1.0 tree in Appendix C §C.4.17 is **mapped, not deleted**: §C.4.17A gives node → v1.0 section → screens; "Billing & Membership" is split into nodes 9–11 (IPB-07 LD note); "Data and storage" becomes node 12; "Audit & history" node 13; "Security and privacy" splits into nodes 2, 3 and 18. The tree is data (`cfg.settings_tree`, platform seed; tenants may hide empty nodes but never reorder the first six USER nodes). Each node carries a help key `hlp.cfg.node_<n>`.

**FR-P03-107 — New USER nodes built here.** (a) **Accessibility** (node 4): the Appendix U §U.4 preference set rendered verbatim (theme, text size 100–200 %, line spacing, reduced motion, dyslexia-friendly font, inline "i" explanations, captions default on, visual alerts for sounds, keyboard-shortcut remap) — stored in `a11y.*` (USER) and applied across `apps/web`, `apps/delivery`, `apps/console`, `apps/mobile` and `apps/public` when signed in. (b) **Appearance** (node 5): theme shortcut, density (FR-P03-32), language, date and number formats, first day of week, default landing page, **simple mode** (`ux.simple_mode`: one primary action per screen, fewer widgets — UDF pattern). (c) **Feedback** (node 16): submit feedback/bug/idea/accessibility problem through `packages/feedback` (P21 FR-P21-151), my submissions and status, tenant-wide list for `ORG_ADMIN`, roadmap votes if `fb.idea_board.enabled`. (d) **Tutorials & help** (node 17): learning paths and progress, re-launch tours (P21 §4O), tutorials library, keyboard shortcuts, glossary, contact support, tenant-curated "Start here" (ORG). (e) **What's new** (node 19): release cards from the P23 release-notes pipeline (FR-P23-59), changelog link, per-release articles, suppression level (ORG: `tut.whats_new.suppress = none | minor | all_but_regulatory`). (f) **About** (node 20): product and `brand.app_name`, version and build (`rel_`), open-source notices, provider legal entity (D-08), Vidhi kernel version, terms and privacy links, support contact, Grievance Officer, data residency — read-only (`ipb.about.*`).

**FR-P03-108 — Security node sub-items (node 2; ORG policy from LDC pattern).** The USER view (password, MFA — TOTP, passkeys/WebAuthn L3 —, active sessions with revoke, trusted devices, recovery codes and contact, login history) sits above a read-only view of the tenant policy; `ORG_ADMIN` edits the policy in Organisation & people › Security policy with maker-checker (NN-18 critical keys): **password policy** (`sec.org.password.min_length` ≥ 12 floor, breached-password check locked on, rotation only on compromise — NIST SP 800-63B-4 [VERIFY current revision]), **MFA policy** (`sec.org.mfa.required_roles`, default all `ORG_*` admin roles; passkeys-first), **session policy** (`sec.org.session.idle_minutes` 15–480, `sec.org.session.max_concurrent`), **IP allow-list** (`sec.org.ip_allowlist` CIDR list for `apps/web` sign-in, with a break-glass path for the `ORG_OWNER` recovery contact and a 24-hour notice before enforcement), **BYOK** (`sec.org.byok.kms_key_ref` for sealed classes on Enterprise plans — key in the tenant's own KMS, LawDocs holds a grant; loss of grant makes sealed data unreadable, stated on screen), **audit-log viewer** (link to node 13 with the tenant's security events filter), **SSO/SCIM** (P01 SCR-P01-22). Every change emits `in.lawdocs.cfg.SecurityPolicyChanged.v1` and a notice to all tenant admins.

**FR-P03-109 — ORG nodes owned elsewhere, surfaced here.** Storage & data (node 12 — P20: usage by class, BYO storage, export, retention schedules with locked regulatory floors, legal holds, deletion requests); Audit trails (node 13 — P00/P23 ledger viewer with hash-chain verification, filters, signed export, scheduled actions awaiting delay window, settings-change history, access reviews); Integrations (node 14 — P19: API keys, webhooks, connected apps, WhatsApp/Meta, calendar/workspace, connector marketplace); AI & Vidhi (node 15 — P09: providers and BYOK, autonomy ceilings per skill, locked list read-only, agents, schedules, notebooks, connections, what Vidhi remembers, digest); Security & trust (node 18 — P23 FR-P23-60…62: vendor documents, sub-processors, certifications, status, DPA, incident notices, evidence packs, auditor grants, questionnaire responder). The registry marks each node's owning phase; P03 ships the shell, navigation, search and empty states so later phases plug in.

**FR-P03-110 — Flags on OpenFeature.** The FR-P03-87 flag registry exposes the OpenFeature API (`FEATURE_FLAG_PORT`; reference adapter in-house file/DB registry, alternatives Unleash and Flagsmith — OI-P03-07 stays open) with module lifecycle states `AVAILABLE → ENABLED → DEPRECATED → DISABLED → DETACHED` (FBX pattern) and the settings "floor vs commercial" class: a key marked `floor` (regulatory or security floor) can never be loosened by a plan or tenant; a key marked `commercial` is plan-gated. Rings (P23 FR-P23-22) and tenant beta opt-in (P23 FR-P23-24A) are flag segments.

## 5. Workflows and state machines

### 5.1 OPEN change

```
validate(type, bounds ∩ plan ∩ brand ∩ platform, child_direction, parent_lock, contrast/schema)
  ├─ fail → field-level message, value kept in form, in validator order:
  │        LD-CFG-001 type/schema · LD-CFG-004 bounds (platform ∩ brand ∩ plan) or floor ·
  │        LD-CFG-005 plan limit · LD-CFG-002 child direction · LD-CFG-006 parent lock ·
  │        LD-CFG-003 contrast below 4.5:1
  └─ pass → key ∈ tenant.require_approval_keys or maker_checker = Y ? → 5.2
            else write cfg.setting_changes + audit ledger (same txn, NN-45)
                 emit in.lawdocs.cfg.SettingChanged.v1 → cache invalidation ≤ 60 s
                 toast "Saved · Undo"
```

### 5.2 GOVERNED change request (`cfg.change_requests.state`)

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| `DRAFT` | submit | Validators green; citation if required; summary; preview ≤ 24 h old; lead time met | `SUBMITTED` | Approval item to eligible checkers (P02 engine) |
| `SUBMITTED` | open | Checker eligible, ≠ maker, not delegated from maker | `IN_REVIEW` | — |
| `IN_REVIEW` | approve | Step-up ≤ 10 min; all approval steps met | `APPROVED` | Audit; notify maker |
| `IN_REVIEW` | reject / return | Reason ≥ 20 chars | `REJECTED` / `DRAFT` | Notify |
| `APPROVED` | schedule | `effective_from` > now | `SCHEDULED` | `ConfigActivationWorkflow` timer |
| `APPROVED`/`SCHEDULED` | activate | Re-validation green | `ACTIVE` | Previous version `SUPERSEDED`; cache bust; propagation per mode; `ConfigChangeActivated` |
| any non-terminal | withdraw | Maker | `WITHDRAWN` | Timers cancelled |
| `SUBMITTED`/`IN_REVIEW` | expiry | `expiry_days` elapsed | `EXPIRED` | Notify maker |

### 5.3 Rule-set version (`rul.rule_set_versions.state`)

`DRAFT → IN_REVIEW (golden suite green or mismatches accepted with reason; citations complete; reviewer assigned ≠ maker) → APPROVED (reviewer of record signs; owning function for computational; publisher for permissive) → SCHEDULED → ACTIVE → SUPERSEDED → RETIRED`; `REJECTED`, `WITHDRAWN`; `ACTIVE → EMERGENCY_BLOCKED` (protective block overlay) → `ACTIVE` after review. Events: `RuleSetVersionSubmitted`, `RuleSetVersionActivated`, `RuleSetReviewDue`, `RuleSetRetired`.

### 5.4 Item lifecycle (`wf.items.canonical_state`) and tasks

State machine: Appendix A §A.15 governs (Resolutions R-A-07, R-A-08). Tasks (`wf.tasks`, `tsk_`): `OPEN → IN_PROGRESS → DONE | CANCELLED`; a task that waits on someone opens a linked `itm_` in `WAITING` instead of adding a waiting state; assignment emits `wf.TaskAssigned`.

| From | Event | Actor | Guard | To | Side effects |
|---|---|---|---|---|---|
| — | create | user, rule, agent, integration, import | Item type allowed for parent; owner resolvable | `OPEN` | Clocks started; `ItemOpened` |
| `OPEN` | start | owner | — | `IN_PROGRESS` | — |
| `OPEN`/`IN_PROGRESS`/`INTERIM` | set_waiting | owner, authorised user, agent (proposal → owner confirms) | Party type allowed; `expected_by` set | `WAITING` | Chase policy scheduled; internal SLA paused if allowed; `ItemWaitingStarted` |
| `WAITING` | response / manual_resume / matching event | system, owner | — | `IN_PROGRESS` | Chases stopped; `ItemWaitingEnded` |
| `WAITING` | chase_due | system | Mode `CONFIRM_EACH` → owner item; `PRE_APPROVED_SERIES` → send; stop conditions false | `WAITING` | `chase_count += 1`; `ItemChased` |
| `WAITING` | expected_by + grace | system | — | `WAITING` | Escalate L1 → L2 |
| any open | legal_due − warning_days | system | Any `LEGAL` clock | (unchanged) | Escalate L2/L3; banner |
| `IN_PROGRESS` | record_interim | owner | Interim evidence if required | `INTERIM` | `ItemInterimRecorded` |
| any open | hold | authorised user | Reason code | `ON_HOLD` | Internal SLA paused; legal clocks continue |
| any open | resolve | owner (or checker if type requires) | Required evidence attached; maker ≠ checker where configured | `RESOLVED` | Parent re-evaluates gates; `ItemResolved` |
| any open | waive | `ORG_CLO`/`ORG_APPROVER`/`IND_OWNER` | Reason from LOCKED list; not an agent | `WAIVED` | Formalities gate re-check; `ItemWaived` |
| any open | cancel / supersede | owner, system | Parent cancelled or replacement linked | `CANCELLED`/`SUPERSEDED` | — |

### 5.5 Kill switch

State machine: Appendix A §A.17 governs (Resolution R-A-09: one registry, one event pair).

`RELEASED → ENGAGED (one authorised person, reason; propagation probe ≤ 60 s; KillSwitchEngaged) → RELEASE_REQUESTED (cause resolved, evidence) → RELEASED (second person ≠ requester; KillSwitchReleased)`; `ENGAGED` cannot be released by the engager alone.

### 5.6 Configuration template application / import

`SELECTED → DIFF_PREVIEWED → SECTIONS_CHOSEN → APPLYING (job) → APPLIED (batch id; undo window open) → UNDONE | FINALISED (window closed)`; GOVERNED sections branch to 5.2.

### 5.7 Correction Entry (configuration)

State machine: Appendix A §A.1 governs (Resolution R-A-01); `TENANT_NOTIFIED` is a side effect of `APPLIED`, not a state.

`DRAFT → SUBMITTED → APPROVED (platform checker) → CLIENT_APPROVAL_PENDING (crucial details only) → APPLIED` (tenant notification is a side effect of `APPLIED`); `REJECTED` at either approval; `WITHDRAWN`; emergency path `APPLIED_EMERGENCY → RATIFIED | AUTO_REVERTED` within 24 h. State names are those of A.1 (`target_kind = CONFIGURATION`).

---

## 6. Screens and UX

All screens follow the LD design system: class badges with text, "i" help on every label, empty states with one next action, keyboard paths, focus order, live-region announcements for saves and errors, accessible tables for every chart. Mobile: personal settings fully available in `apps/mobile`; tenant administration on mobile is limited to approvals, kill switches, items and quick edits of OPEN labels (full Studio is web).

| Screen ID | App | Name / path | Purpose, states and accessibility notes |
|---|---|---|---|
| SCR-P03-01 | web, delivery | Settings home `/settings` | Search, sections grid, recent changes, pending approvals, health summary · "Nothing changed yet" · Search first in tab order |
| SCR-P03-02 | web, delivery | Section page `/settings/{section}` | Setting rows (FR-P03-24), filters by class and "changed" · Locked rows read-only with reason · Rows are list items with headings |
| SCR-P03-03 | web, delivery | Setting drawer | Editor, inheritance chain ("Platform → Business plan → ABC Ltd → Legal dept"), history, who can change · Out-of-bounds message with allowed range · Drawer traps focus; Esc closes |
| SCR-P03-04 | web | Change request composer | Diff, citation picker (`LG-xxx`, instrument + provision), effective date, propagation, summary (Vidhi draft), preview · Missing citation blocks submit |
| SCR-P03-05 | web, mobile | Change approval card (Inbox) | Diff, preview result, impact, citation, approve/reject with step-up · Maker sees "Waiting for checker" · Mobile approval supported |
| SCR-P03-06 | web | Appearance `/settings/appearance` | Theme editor with live contrast checker, density, logo, preview in light/dark/high-contrast · Failing contrast suggests nearest passing shade · Contrast results read as text |
| SCR-P03-07 | web, mobile | Home and quick actions | Widget catalogue, drag/keyboard reorder, mandatory widgets marked · "Add your first widget" · Reorder via "Move" menu |
| SCR-P03-08 | web | Menus `/settings/navigation` | Hide, reorder, rename, landing page per user type, preview as user type · Locked items shown with padlock + text |
| SCR-P03-09 | web | Terminology and labels | Term, default, tenant term per locale, where used · Missing translation falls back |
| SCR-P03-10 | web | Custom fields | Per object type; PII class; usage count; plan limit meter · Limit reached banner |
| SCR-P03-11 | web | Status sets | Per object type; canonical mapping graph; transitions · Forbidden transition explained · Graph has table alternative |
| SCR-P03-12 | web | Numbering schemes | Pattern builder with tokens, preview of next 3 numbers · Duplicate/invalid token errors |
| SCR-P03-13 | web | Form designer | Drag-drop with "Add field after…" keyboard menu; conditions; preview as user type; accessibility lint · Lint failures block publish |
| SCR-P03-14 | web | Communication templates | Event, channel, locale; variables; DLT/WhatsApp IDs; preview · SMS without DLT ID cannot activate |
| SCR-P03-15 | web | Documents and letterheads | Letterhead editor per entity; cover pages; preview DOCX/PDF · Minimum font/contrast enforced |
| SCR-P03-16 | web | Item types | Catalogue; owner rules; evidence; SLA; waiting parties; formalities flag · Platform-locked parts marked |
| SCR-P03-17 | web | Chase policies and ladders | Cadence, channels, templates, confirm mode, max chases, ladders · `PRE_APPROVED_SERIES` shows governance note |
| SCR-P03-18 | web, mobile | My items / Waiting on others | Lists, ageing buckets, bulk actions, clocks with countdown text · "No one is holding you up" · Countdown as text, not colour only |
| SCR-P03-19 | web, mobile | Item detail | Timeline, waiting record, interim outcomes, clocks, chase log, evidence · Legal clock banner |
| SCR-P03-20 | web | Rules adopted `/settings/rules` | Platform sets in use, versions, "what changed", stricter adaptations, tenant `T-` sets, rule challenge |
| SCR-P03-21 | console | Rule-set editor | ZEN decision-table editor, CEL predicate editor, citations, fixtures, run preview · Golden failures listed |
| SCR-P03-22 | console | Review queue (reviewer of record) | Diff, sources, golden results, impact; approve with qualification captured |
| SCR-P03-23 | console | Content and rule release calendar | Scheduled activations by date and jurisdiction |
| SCR-P03-24 | console, web | Flags and kill switches | State, scope, owner, last drill, engage/release, propagation probe · Release disabled for engager · Confirm dialogs labelled |
| SCR-P03-25 | web | Templates, import, compare, sandbox `/settings/transfer` | Library, apply with diff, bundle export/import, compare, sandbox · Rejected rows with reasons |
| SCR-P03-26 | web, console | Configuration Health | FR-P03-102 panels · All green state |
| SCR-P03-27 | web | Changes made by LawDocs | Correction Entries and platform changes affecting the tenant; export · "No changes by LawDocs" |
| SCR-P03-28 | console | Tenant override console | Any tenant key; every save opens a Correction Entry |
| SCR-P03-29 | web, mobile | Personal settings `/me/settings` | Language, accessibility, appearance, home, quick actions, notifications, quiet hours, delegation, my data · ≤ 2 taps from home |
| SCR-P03-30 | web | Automations and agents | Every automation (rules, chasers, agent missions, scheduled exports) with owner, last run, autonomy, kill switch, pause |
| SCR-P03-31 | web | Explain my configuration | Generate DOCX/PDF; diff between dates |
| SCR-P03-32 | delivery | RM proposal view | Read-only tenant Studio with "Propose change" · Proposal pending badge |
| SCR-P03-33 *(v1.1)* | web | Security policy (FR-P03-108) | Password, MFA, sessions, IP allow-list (notice banner), BYOK (key-loss warning), audit-log link · maker-checker |
| SCR-P03-34 *(v1.1)* | web/mobile | About (FR-P03-107(f)) | Product and display name, version, licences, provider entity, Vidhi kernel version, terms, support, Grievance Officer, residency · read-only, copyable |

---

## 7. Backend design

### 7.1 Modules

`cfg` (owner: registry, values, changes, templates, flags, kill switches, UI customisation), `rul` (owner: rule sets, evaluations, content-version framework), `wf` (owner of `wf.items`; uses P02 approvals), `core` (audit ledger, correction entries, IDs), `ntf` (renders templates), `hlp` (help keys), `rpt` (widgets), `ai` (drafts summaries and mappings), `bil` (plan entitlements read).

### 7.2 Tables (tenant tables under RLS with `tenant_id`, `legal_entity_id` where relevant; retention class in brackets)

| Table | Key columns | Indexes / notes |
|---|---|---|
| `cfg.setting_definitions` *platform* | key PK, tier, allowed_scopes[], control_class, sub_class, value_type, json_schema, default_value, bounds, merge_strategy, child_direction, protective_direction, maker_checker, effective_dating, instance_pinned, sensitivity, owner_role, citation_required, depends_on_verify, fallback_kind, ui jsonb, introduced_in, deprecated_in, alias_of | [permanent] |
| `cfg.setting_values` | id, tenant_id null, scope_tier, scope_id, key, value jsonb, version, locked, valid_from, valid_to, recorded_at, change_id | unique (scope_tier, scope_id, key, valid_from); [permanent] |
| `cfg.setting_changes` | id, tenant_id, key, scope, before, after, actor_id, on_behalf_of, reason, via (`ui`,`api`,`template`,`import`,`correction`,`agent_proposal`), batch_id, recorded_at | [7 years] |
| `cfg.change_requests` | id, tenant_id null, items jsonb, state, sub_class, citation jsonb, summary_i18n, effective_from, propagation_mode, preview_ref, impact_ref, maker_id, approvals jsonb | [7 years] |
| `cfg.change_batches` | id, tenant_id, kind, undo_until, state | — |
| `cfg.tenant_controls` | tenant_id, require_approval_keys[], department_sections[], sandbox_enabled | — |
| `cfg.brands` *platform* | brand_code, legal_entity_profile_id, tokens jsonb, domains, verticals[] | — |
| `cfg.widget_catalogue` *platform* / `cfg.dashboard_layouts` | widget code, module, data_api, roles, sizes, mandatory_for[], a11y_table; layout scope (`user_type`,`department`,`user`), widgets jsonb | — |
| `cfg.nav_items` *platform* / `cfg.nav_overrides` | code, app, parent, route, permission, entitlement, locked; tenant_id, user_type, user_id, hidden, order, pinned, label_override | — |
| `cfg.quick_actions` | tenant_id, scope, user_id null, actions jsonb | — |
| `cfg.terminology` | tenant_id null, brand_code null, term_key, locale, text, locked | — |
| `cfg.custom_field_defs` | id, tenant_id, object_type, code, label_i18n, type, options, required_at_status[], visibility_roles[], edit_roles[], pii_class, searchable, export_name, formula_cel | — |
| `cfg.status_sets` / `cfg.status_defs` | tenant_id, object_type, version; code, label_i18n, canonical_state, colour, icon, requires_checker, required_fields[] | — |
| `cfg.reason_code_lists` / `cfg.reason_codes` | list_code, code, label_i18n, locked | — |
| `cfg.numbering_schemes` / `cfg.number_sequences` | tenant_id, legal_entity_id, object_type, pattern, reset_rule, active_from; sequence scope key, next_value | Row lock on increment; [permanent] |
| `cfg.form_defs` / `cfg.form_versions` | tenant_id, object_type, version, layout jsonb, conditions, state | — |
| `cfg.letterheads` | tenant_id, legal_entity_id, asset refs, styles, version | — |
| `cfg.flags` / `cfg.flag_targets` | key, purpose, owner, expiry, verify_ref; targeting rules | — |
| `cfg.kill_switches` / `cfg.kill_switch_events` | code, scope, state, engaged_by, reason, released_by, probe_result, last_drill_at | [7 years] |
| `cfg.config_templates` / `cfg.template_applications` | code, owner scope, content jsonb, version; tenant_id, template_code, batch_id | — |
| `cfg.config_bundles` | tenant_id, kind (`export`,`import`), object_key, signature, diff_report, state | [3 years] |
| `cfg.fallback_events` | tenant_id, key or rule_set, object_ref, kind, reason, at | [3 years] |
| `rul.rule_sets` / `rul.rule_set_versions` | code, jurisdiction, domain, effect_class, owner_role, volatile; version, state, content jsonb (JDM), cel jsonb, citations jsonb, source_sha256[], verification_status, effective_from, effective_to, propagation_mode, next_review_due, maker_id, reviewer_of_record jsonb (user, qualification, registration no., reviewed_at), summary_i18n | [permanent] |
| `rul.golden_cases` | rule_set_id, tenant_id null, inputs, expected, kind | — |
| `rul.evaluations` | id, tenant_id, rule_set_version_id, input_hash, output jsonb, as_of, caller, object_ref, at | Partitioned monthly; [as parent record, min 7 years for signing decisions] |
| `rul.adoptions` / `rul.adaptations` / `rul.challenges` | tenant_id, rule_set_id, mode, pinned_version, adapted_params; challenge sources, state, response | — |
| `rul.content_kinds` / `rul.content_versions` | kind code, editor module; content_id, version, jurisdiction, effective dates, sources, reviewer_of_record, hash, ai_assisted | [permanent] |
| `wf.item_types` | tenant_id null, code, names_i18n, parent_types[], owner_rule, priority, evidence_rule, waiting_party_types[], chase_policy_id, sla_policy_id, ladder_id, pause_internal_sla, formalities, triggers jsonb, locked_parts jsonb | — |
| `wf.items` | id (`itm_`), tenant_id, legal_entity_id, item_type_code, parent_type, parent_id, canonical_state, tenant_status_code, owner_user_id, owner_team_id, priority, due_at, visibility, external_label, source, created_by, resolved_at, resolution_code | idx (tenant_id, owner_user_id, canonical_state), (tenant_id, parent_type, parent_id), (tenant_id, due_at); [as parent] |
| `wf.item_waits` | item_id, party_type, party_ref, reason_code, requested_at, expected_by, external_reference, internal_sla_paused, response_received_at | — |
| `wf.item_clocks` | item_id, kind, source, starts_at, due_at, pausable, paused_intervals jsonb, version | idx (tenant_id, kind, due_at) |
| `wf.item_interims` | item_id, outcome, evidence_refs, next_check_at | — |
| `wf.chase_policies` / `wf.chase_log` | cadence, first_offset, max_chases, channels jsonb, templates, confirm_mode, series_approval_id; item_id, seq, channel, recipient_ref, template_version, idempotency_key, sent_at, result | [as parent] |
| `wf.escalation_ladders` / `wf.sla_policies` / `wf.business_calendars` | levels jsonb; targets per type and priority; holidays by State | — |
| `wf.tasks` (R-A-08) | id (`tsk_`), tenant_id, legal_entity_id, parent_type, parent_id, title_i18n, state (`OPEN`,`IN_PROGRESS`,`DONE`,`CANCELLED`), assignee_user_id, assignee_team_id, assigned_by, due_at, priority, checklist jsonb, depends_on[] (`tsk_`), evidence_rule, evidence_refs[], linked_item_id (`itm_`, when waiting), source (`user`,`rule`,`agent_proposal`,`integration`,`import`), completed_at | idx (tenant_id, assignee_user_id, state), (tenant_id, parent_type, parent_id), (tenant_id, due_at); [as parent] |

### 7.3 APIs (`/v1`; `Idempotency-Key` on POST; `If-Match` on PATCH; mobile BFF mirrors under `/m/v1`)

| Method and path | Scope | Notes |
|---|---|---|
| `GET /v1/settings?section=&scope=` · `GET /v1/settings/{key}/resolve` | read | Returns value + source + class |
| `PATCH /v1/settings/{key}` · `POST /v1/settings/{key}:undo` · `GET /v1/settings/{key}/history` | `change_open` | OPEN only; GOVERNED returns `LD-CFG-012` with a link to create a request |
| `POST /v1/config-change-requests` · `POST …/{id}:submit|approve|reject|withdraw|preview` | `propose_governed` / `approve_governed` | Step-up on approve |
| `GET/PUT /v1/appearance` · `/v1/navigation` · `/v1/home-layout` · `/v1/quick-actions` · `/v1/terminology` | per section | — |
| `GET/POST /v1/custom-fields` · `/v1/status-sets` · `/v1/reason-codes` · `/v1/numbering-schemes` · `/v1/forms` · `/v1/letterheads` · `/v1/notification-templates` | admin | Versioned publish endpoints `…:publish` |
| `POST /v1/rules:evaluate` | internal service | Deterministic; records evaluation when `record=true` |
| `GET /v1/rule-sets` · `POST /v1/rule-sets/{id}/versions` · `POST /v1/rule-set-versions/{id}:run-golden|impact|submit|review|publish|retire|emergency-block` | platform roles | Reviewer of record captured on `:review` |
| `POST /v1/rule-sets/{id}:adopt|pin|adapt` · `POST /v1/rule-challenges` | tenant admin | — |
| `GET/POST /v1/item-types` · `GET/POST /v1/chase-policies` · `GET/POST /v1/escalation-ladders` | admin | — |
| `GET /v1/wf/tasks?assignee=me&state=` · `POST /v1/wf/tasks` · `POST /v1/wf/tasks/{id}:assign|start|complete|cancel` | `wf.task:read` / `wf.task:write` | Agents may create tasks as proposals only (NN-43); `:complete` checks the evidence rule (`LD-WF-131`) and open dependencies (`LD-WF-130`) |
| `POST /v1/items` · `GET /v1/items?owner=&state=&party_type=` · `POST /v1/items/{id}:start|wait|resume|interim|hold|resolve|waive|cancel|reassign` · `POST /v1/items/{id}/chases/{seq}:send` · `POST /v1/items:bulk` | per item | `:send` is the human confirmation for `CONFIRM_EACH` |
| `GET /v1/flags:evaluate` · `POST /v1/kill-switches/{code}:engage|request-release|release` | per switch | Release requires second person |
| `POST /v1/config-bundles:export|import` · `GET /v1/config:compare` · `POST /v1/config-templates/{code}:apply` · `POST /v1/config-sandboxes` · `POST /v1/config-sandboxes/{id}:promote` | admin | Dry-run first on import/apply |
| Console: `POST /v1/console/tenants/{id}/corrections` · `POST /v1/console/corrections/{id}:approve|reject` · `POST /v1/console/tenants/{id}/support-sessions` | platform | Client approval step for crucial details |

### 7.4 Domain events (CloudEvents; IDs and keys only — never values of `confidential` or `secret_ref` keys)

`in.lawdocs.cfg.SettingChanged.v1`, `in.lawdocs.cfg.ConfigChangeRequested.v1`, `in.lawdocs.cfg.ConfigChangeApproved.v1`, `in.lawdocs.cfg.ConfigChangeActivated.v1`, `in.lawdocs.cfg.ConfigTemplateApplied.v1`, `in.lawdocs.cfg.ConfigBundleExported.v1`, `in.lawdocs.cfg.ConfigBundleImported.v1`, `in.lawdocs.cfg.FallbackActivated.v1`, `in.lawdocs.cfg.FlagChanged.v1`, `in.lawdocs.cfg.KillSwitchEngaged.v1`, `in.lawdocs.cfg.KillSwitchReleased.v1`, `in.lawdocs.rul.RuleSetVersionSubmitted.v1`, `in.lawdocs.rul.RuleSetVersionActivated.v1`, `in.lawdocs.rul.RuleSetReviewDue.v1`, `in.lawdocs.rul.RuleSetRetired.v1`, `in.lawdocs.rul.RuleSetEmergencyBlocked.v1`, `in.lawdocs.rul.ContentVersionPublished.v1`, `in.lawdocs.wf.ItemOpened.v1`, `in.lawdocs.wf.ItemWaitingStarted.v1`, `in.lawdocs.wf.ItemWaitingEnded.v1`, `in.lawdocs.wf.ItemChased.v1`, `in.lawdocs.wf.ItemEscalated.v1`, `in.lawdocs.wf.ItemInterimRecorded.v1`, `in.lawdocs.wf.ItemResolved.v1`, `in.lawdocs.wf.ItemWaived.v1`, `in.lawdocs.wf.LegalClockWarning.v1`, `in.lawdocs.wf.TaskCreated.v1`, `in.lawdocs.wf.TaskAssigned.v1` (R-A-08; consumed by `ntf`, `sdc`, `mob`), `in.lawdocs.wf.TaskCompleted.v1`, `in.lawdocs.core.CorrectionApplied.v1` (P00-owned event, emitted for configuration corrections with `target_kind = CONFIGURATION`; Appendix B §B.4). Tenant webhooks may subscribe to `wf.Item*`, `wf.Task*` and `cfg.KillSwitch*` (tenant scope). `cfg.KillSwitchEngaged` / `cfg.KillSwitchReleased` are the only kill-switch events in the platform; P00, P09 and P19 emit them through this registry (R-A-09). No P03 event crosses to another product; ecosystem waits are resumed by events `int` consumes.

### 7.5 Jobs and Temporal workflows

`ConfigActivationWorkflow`, `CacheInvalidationConsumer`, `RuleSetImpactWorkflow`, `GoldenSuiteRunJob`, `RuleReviewDueScanJob` (daily 06:00 IST), `PinExpiryScanJob`, `ItemClockWorkflow` (per item with clocks; timers for warnings and SLA), `ChasePolicyWorkflow` (per waiting item; respects quiet hours and calendars), `EscalationJob`, `StaleFlagScanJob` (weekly), `KillSwitchProbeJob` (on change + hourly), `KillSwitchDrillReminderJob`, `TemplateApplyJob`, `ConfigBundleExportJob`, `SandboxProvisionJob`, `EmergencyOverrideRevertWorkflow` (24 h), `ConfigHealthSnapshotJob` (nightly), `DomainVerificationJob`.

---

## 8. Integrations

| Port | Use in P03 | Adapters | Failure behaviour |
|---|---|---|---|
| `RULES_PORT` | Evaluate rule sets and predicates | GoRules ZEN (default), CEL, JSON Logic (fallback) | Engine error → declared fallback (`block` for protective eligibility); alert |
| `NOTIFY_PORT` (`ntf`) | Render and send templates and chasers | Email (SES/Brevo transactional), SMS/WhatsApp/RCS via JioCX and other DLT-registered CPaaS, push, Teams/Google Chat connectors | Channel kill switch holds messages; retry with idempotency; fallback channel only if the policy lists it |
| `DNS_CHECK_PORT` | Sender and custom domain verification | Internal resolver | Unverified → send "on behalf of" |
| `AI_PORT` (`packages/ai`) | Change summaries, NL settings mapping, item suggestions | Claude via Bedrock India (D-14) | AI unavailable → manual forms; nothing blocks |
| `ENTITLEMENT_PORT` (`bil` mirror of OH8) | Plan limits | OH8 `EntitlementChanged` | Keep last valid signed entitlement for 30 days if OH unreachable (Ecosystem Spec §6.27) |
| `COURT_DATA_PORT`, `TRADEMARK_DATA_PORT` (P11, P12) | Status refresh for items waiting on courts/registry | Licensed aggregators | Staleness label; manual check task |

No settings cross to other products; group tenants may share configuration **templates** through `tenant_link`, never data access (NN-24).

---

## 9. Settings and configuration

Representative keys owned by P03 (full catalogue with tier, type, default, changed-by and maker-checker: Appendix R §R.9 `cfg`, `rul`, `wf`, `ntf`).

| Key | Tier (scopes) | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `cfg.registry.require_registration` | PLATFORM | LOCKED | boolean | true | — | — |
| `cfg.batches.undo_window_hours` | TENANT | OPEN | integer 1–168 | 24 | `ORG_ADMIN` | N |
| `cfg.tenant.require_approval_keys` | TENANT | GOVERNED-elevated | multi-enum | [] | `ORG_OWNER` | Y |
| `cfg.custom_fields.max_per_object` | PLAN | GOVERNED-elevated | integer | Free 5 · Personal 10 · Pro 25 · Business 75 · Enterprise 150 | `PLT_SUPER_ADMIN` | Y |
| `cfg.theme.high_contrast_available` | PLATFORM | LOCKED | boolean | true | — | — |
| `cfg.ui.text_scale_percent` | USER | OPEN | integer 100–200 | 100 | user | N |
| `rul.reviewer_of_record.required` | PLATFORM | LOCKED | boolean | true | — | — |
| `wf.items.legal_clock_pausable` | PLATFORM | LOCKED | boolean | false | — | — |
| `wf.items.legal_warning_days` | TENANT→DEPARTMENT | OPEN (`raise_only`, floor 3) | integer 3–60 | 7 | `ORG_CLO` | N |
| `wf.items.external_chase_mode` | TENANT | GOVERNED-elevated | enum CONFIRM_EACH/PRE_APPROVED_SERIES | CONFIRM_EACH | `ORG_ADMIN` → `ORG_CLO` | Y |
| `wf.items.auto_contact_courts_registries_regulators` | PLATFORM | LOCKED | boolean | false | — | — |
| `ntf.dlt.require_template_id` | PLATFORM | LOCKED | boolean | true | — | — |
| `cfg.kill_switch.release_second_person` | PLATFORM | LOCKED | boolean | true | — | — |
| `core.correction.client_approval_crucial_details` | PLATFORM | LOCKED | boolean | true | — | — |
| `cfg.settings_tree` *(v1.1)* | PLATFORM | GOVERNED | json | IPB-07 20-node seed + LD additions | `PLT_SUPER_ADMIN` | Y |
| `cfg.palette.pii_refusal` *(v1.1)* | PLATFORM | LOCKED | boolean | true | — | — |
| `ux.simple_mode` *(v1.1)* | USER | OPEN | boolean | false | user | N |
| `ux.appearance.density` *(v1.1)* | USER | OPEN | enum comfortable/compact/spacious | comfortable | user | N |
| `a11y.*` (Appendix U §U.4 set) *(v1.1)* | USER | OPEN | per key | per Appendix U | user | N |
| `sec.org.password.min_length` *(v1.1)* | TENANT | GOVERNED-elevated (`raise_only`, floor 12) | integer 12–64 | 12 | `ORG_ADMIN` | Y |
| `sec.org.mfa.required_roles` *(v1.1)* | TENANT | GOVERNED-elevated | multi-enum | all `ORG_*` admin roles | `ORG_ADMIN` | Y |
| `sec.org.session.idle_minutes` *(v1.1)* | TENANT | GOVERNED | integer 15–480 | 60 | `ORG_ADMIN` | Y |
| `sec.org.session.max_concurrent` *(v1.1)* | TENANT | GOVERNED | integer 1–10 | 5 | `ORG_ADMIN` | Y |
| `sec.org.ip_allowlist` *(v1.1)* | TENANT | GOVERNED-elevated | CIDR[] | [] | `ORG_OWNER` | Y (24 h notice) |
| `sec.org.byok.kms_key_ref` *(v1.1)* | TENANT (Enterprise) | GOVERNED-elevated | secret-ref | null | `ORG_OWNER` | Y |
| `tut.whats_new.suppress` *(v1.1)* | TENANT | OPEN | enum none/minor/all_but_regulatory | none | `ORG_ADMIN` | N |
| `brand.app_name` / `brand.terminology` (tenant layer) *(v1.1)* | TENANT (white-label plan) | GOVERNED | string / map | "LawDocs" / {} | `ORG_OWNER` | Y |

Customisation hooks introduced: every key with class OPEN above; tenant item types, chase policies and ladders; templates of configuration; numbering patterns; letterheads; themes.

---

## 10. Security, privacy and audit

| Threat | Control |
|---|---|
| Tenant changes a LOCKED or out-of-bound value through the API | Server-side validation on every write; LOCKED keys have no write path; `NN-29_locked_keys_immutable` |
| Single administrator weakens controls (removes checker, raises limits) | NN-18 keys force maker-checker; workflow validator rejects approval steps that the maker can complete; Health shows zero such configurations |
| Super Admin silently edits client configuration | Correction Entries only; client approval for crucial details; tenant-visible log (CH-26) |
| Secret leakage through settings | `secret_ref` keys store vault references only; events and logs carry keys, never values (NN-32) |
| Rule tampering | Rule versions hashed; activation requires reviewer of record; evaluations recorded with version; console actions audited |
| CEL denial of service | Cost budget per evaluation; timeouts; no I/O |
| Chaser spam or harassment of counterparties | NN-34 caps, opt-out honoured, confirm-each default, DLT templates only, no automated calls before opt-in |
| Cross-tenant cache bleed | Cache keys include `tenant_id`; RLS on all tenant tables; `NN-01_cfg_rls_cross_tenant` |
| Sensitive custom fields exposed | Field-level encryption; excluded from search and AI context unless permitted |

Audit: every OPEN and GOVERNED change, template application, import, rule activation, evaluation that blocks or permits a legal action, item transition, chase, waiver, flag change and kill-switch event is written to the hash-chained ledger in the same transaction (NN-02, NN-45). Retention: change records 7 years; rule versions and content versions permanent; evaluations as long as the record they decided (≥ 7 years for signing decisions — R3 LG-008). DPDP: configuration contains no personal data except user preferences (USER tier, deleted with the account) and custom-field values (owned by the record's module and retention class).

---

## 11. AI touchpoints and guardrails

| Touchpoint | What Vidhi does | Autonomy ceiling | Human confirmation point |
|---|---|---|---|
| Natural-language settings | Maps a request to keys; drafts the change | L2 | User clicks Save/Submit |
| Change summaries | Drafts the ≤ 120-word "what changed" text | L2 | Maker edits and owns; checker approves |
| Item suggestions | Proposes items, waiting parties and expected-by dates from a document or email ("The lessor must register within 4 months" → `AGR_REGISTRATION_PENDING` with a legal clock — citation required) | L2 | Owner confirms each item; legal clock must cite a rule set or show "unverified" (NN-14) |
| Chaser drafts | Drafts polite chasers in the recipient's language (labelled machine translation where translated) | L2 | Owner sends (`CONFIRM_EACH`) |
| Rule drafting assist | Converts a cited provision into a draft decision table with golden cases | L2 | `PLT_CONTENT_EDITOR` edits; `PLT_LEGAL_REVIEWER` reviews; Vidhi is never a reviewer |
| Template mapping | Suggests department/status/field mappings during template application | L2 | Admin confirms |

`AGT_*` principals have no `change_open`, `approve_governed`, `release` or `:send` permissions (NN-43). Evaluation: a golden set of 200 natural-language settings requests with expected key mappings (≥ 95% top-3 accuracy before GA); zero tolerance for any AI path that writes `cfg` or sends a chaser.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p03/*.feature`)

```gherkin
@P03-AT-01 @NN-29
Scenario: Unregistered key fails the build
  Given a pull request that reads "clm.renewal.new_unregistered_key"
  When CI runs config-registry-lint
  Then the build fails with "Unregistered setting key"

@P03-AT-02 @NN-29
Scenario: Locked value cannot be changed
  Given ORG_ADMIN of tenant "ABC Ltd"
  When she calls PATCH /v1/settings/wf.items.legal_clock_pausable with true
  Then the response is 403 with code LD-CFG-010 "This setting is locked"
  And no change row or ledger entry is written

@P03-AT-03
Scenario: Open change is effective within 60 seconds and undoable
  Given "clm.renewal.reminder_offsets_days" resolves to [60,30,7] for ABC Ltd
  When ORG_ADMIN sets it to [90,60,30,7]
  Then a renewal item created 60 seconds later uses [90,60,30,7]
  And ORG_ADMIN can undo within the undo window restoring [60,30,7]

@P03-AT-04 @NN-18
Scenario: Maker cannot approve own governed change
  Given ORG_ADMIN "A" submits a change to the agreement approval matrix
  When "A" attempts to approve it
  Then the response is 403 with code LD-CFG-020 "You cannot approve your own change"

@P03-AT-05 @NN-18
Scenario: Critical keys are always maker-checker
  Given the registry seed declares "bil.streams.ads.enabled" with maker_checker N
  When CI runs nn18-keys
  Then the build fails naming "bil.streams.ads.enabled"

@P03-AT-06
Scenario: Plan bounds cascade
  Given ABC Ltd is on the Pro plan with cfg.custom_fields.max_per_object = 25
  And agreements already have 25 custom fields
  When ORG_ADMIN adds a 26th field
  Then the request fails with LD-CFG-005 "Plan limit reached" and offers plan options without pre-selecting an upgrade

@P03-AT-07 @NN-28
Scenario: Theme cannot break contrast
  When ORG_ADMIN sets the primary colour to #9AD0F5 on a white surface
  Then saving is blocked with LD-CFG-003 "Text contrast 1.65:1 is below 4.5:1"
  And the editor suggests a passing shade

@P03-AT-08
Scenario: Individual changes text size in two taps on mobile
  Given IND_OWNER on the my.lawdocs.in home screen on a 360 px mobile browser (repeated in the Android app at P22)
  When she taps the avatar and then "Text size"
  Then the text-size control is focused and changes apply immediately to all screens

@P03-AT-09 @NN-30
Scenario: Rule set needs a reviewer of record who is not the maker
  Given PLT_CONTENT_EDITOR "M" drafts "rulepack.IN-MH.stamp.duty_table@2027.1"
  When "M" assigns herself as reviewer
  Then the action fails with LD-RUL-011 "Reviewer must differ from maker"
  And activation remains blocked until a PLT_LEGAL_REVIEWER approves with qualification recorded

@P03-AT-10 @NN-30
Scenario: Code release does not change published rules
  Given rule set versions are hashed before the release rehearsal
  When the release migrations run
  Then every rul.rule_set_versions hash is unchanged

@P03-AT-11 @NN-07
Scenario: Excluded instrument is blocked by the eligibility rule
  Given the active eligibility set marks "Will" as WET_INK_ONLY citing LG-003
  When a user requests eSign on a will
  Then the request is refused with LD-SGN-014 and the evaluation is recorded with the rule version
  And the user is offered a wet-ink execution pack

@P03-AT-12 @NN-38
Scenario: Unverified computational row stays indicative
  Given a State stamp-duty row with verification_status SECONDARY_ONLY
  When a user computes duty
  Then the amount is labelled "Indicative — under verification"
  And payment of duty through LawDocs is not offered for that row

@P03-AT-13 @NN-29
Scenario: Legal clock never pauses while waiting
  Given item "AGR_REGISTRATION_PENDING" with a LEGAL clock due 2027-02-28
  And the item is WAITING on REGISTRY with internal SLA paused
  When the date reaches 2027-02-21 with legal_warning_days 7
  Then L2 and L3 recipients are notified "Legal deadline approaching while waiting on Sub-Registrar"
  And the LEGAL clock due date remains 2027-02-28

@P03-AT-14 @NN-05
Scenario: No automatic contact with courts or registries
  When an admin tries to add an email channel to a chase policy for party type COURT
  Then the save fails with LD-WF-112 "LawDocs never contacts courts, registries or regulators automatically"

@P03-AT-15 @NN-13 @NN-34
Scenario: External chaser needs a human send by default
  Given an item WAITING on COUNTERPARTY with cadence P3D
  When the first chase falls due
  Then the owner receives a ready-to-send chaser
  And no message is sent until the owner taps Send

@P03-AT-16 @NN-34
Scenario: Pre-approved series stays bounded
  Given external_chase_mode PRE_APPROVED_SERIES approved by ORG_CLO for signing reminders
  When a user configures 7 chases
  Then validation fails with LD-WF-114 "At most 5 reminders"
  And a counterparty who opts out receives no further reminders

@P03-AT-17 @NN-40
Scenario: Agreement cannot be marked executed with an open formality
  Given an agreement with items stamp RESOLVED, registration WAITING
  When the user marks the agreement Executed
  Then the action fails with LD-WF-120 "1 formality pending: Registration"
  And ORG_CLO may waive it only with a reason from the locked list

@P03-AT-18 @NN-43
Scenario: Agent cannot waive or send
  Given agent AGT_SIGNING_COORDINATOR proposes a chaser and a waiver
  Then the chaser appears as a draft for the owner
  And the waiver request is refused with LD-WF-121

@P03-AT-19 @NN-39
Scenario: Kill switch propagates and needs two people to release
  Given ESP adapter "esp_primary" is live
  When PLT_SECURITY_OFFICER engages int.kill.esp_primary
  Then new signing requests route away from it within 60 seconds
  And the same officer cannot release it

@P03-AT-20 @NN-02
Scenario: Super Admin change to a crucial detail needs client approval
  Given PLT_SUPER_ADMIN "S" requests a correction of ABC Ltd's GSTIN with evidence
  And PLT_SECURITY_OFFICER "Q" approves
  Then the correction waits for ORG_OWNER approval
  And after approval "Changes made by LawDocs" shows old and new values, both platform actors and the client approver
  And the original value remains in the ledger

@P03-AT-21
Scenario: Configuration template applies with diff and undo
  Given the template "SME — two-person approval"
  When ORG_ADMIN applies it
  Then a diff lists every section and GOVERNED sections become change requests
  And the OPEN sections can be undone within 24 hours as one batch

@P03-AT-22
Scenario: Import rejects out-of-bound values
  Given a bundle with "wf.items.max_chases_external = 9"
  When imported into a sister tenant
  Then that row is rejected with LD-CFG-070 and the other rows are listed for confirmation

@P03-AT-23 @NN-01
Scenario: Settings never leak across tenants
  Given tenants A and B with different letterheads
  When a user of A requests B's letterhead by ID
  Then the response is 404 and the attempt is logged

@P03-AT-24
Scenario: RM proposes, client approves
  Given OPS_RM with a delivery grant including cfg:propose for tenant ABC Ltd
  When the RM proposes a new item type
  Then the change request's checker must be an ABC Ltd user
  And the RM cannot approve it

@P03-AT-25
Scenario: Display numbering never replaces the permanent reference
  Given pattern "ABC/LEG/{FY}/{SEQ:4}"
  When an agreement is created on 2026-11-02
  Then its display reference is "ABC/LEG/2026-27/0001" and its permanent reference is "LD-AGR-2026-…"
  And exports carry both

# ---- v1.1 additions (IPB-07 tree, security, palette) ----

@P03-AT-26 @IPB-07
Scenario: Settings tree follows the binding order and maps v1.0 screens
  Given a Company workspace admin opens Settings
  Then the first six nodes are Profile, Security, Privacy & consents, Accessibility, Appearance, Notifications in that order
  And "Billing", "Invoices" and "Plans & subscription" are separate nodes each reaching the v1.0 P17 screens

@P03-AT-27 @IPB-07-28
Scenario: Palette refuses identity and payment numbers
  Given a user types a 12-digit number passing the Verhoeff check into the command palette
  Then no search request is sent and the refusal message is shown
  And the audit log records pattern class "aadhaar_like" and no digits

@P03-AT-28 @NN-18
Scenario: IP allow-list change needs a checker and a notice period
  Given ORG_ADMIN proposes an IP allow-list of one office CIDR
  When ORG_OWNER approves
  Then enforcement starts 24 hours later, every tenant admin is notified, and the recovery contact's break-glass path remains documented on the sign-in error

@P03-AT-29 @IPB-04
Scenario: Tenant brand colour below contrast guard is rejected
  Given a white-label tenant sets primary text colour with 3.9:1 contrast on the surface token
  When they save
  Then the save fails with LD-CFG-003 and a suggested nearest compliant colour

@P03-AT-30 @IPB-09
Scenario: Floor-class key cannot be loosened by plan or tenant
  Given "sec.org.password.min_length" is a floor key with minimum 12
  When a plan seed sets 8 or a tenant sets 10
  Then both writes are rejected with LD-CFG-004
```

NN tests added: `NN-29_registry_before_use`, `NN-29_locked_keys_immutable`, `NN-29_legal_clock_never_pauses`, `NN-18_critical_keys_maker_checker`, `NN-30_reviewer_of_record`, `NN-30_release_does_not_touch_rules`, `NN-38_unverified_rows_indicative`, `NN-39_kill_switch_60s`, `NN-13_external_chaser_confirmation`, `NN-34_counterparty_reminder_caps`, `NN-40_formalities_gate`, `NN-43_agent_no_waive_no_send`, `NN-01_cfg_rls_cross_tenant`, `NN-02_correction_preserves_original`, `NN-45_cfg_audit_same_txn`.

---

## 13. Exit gate, deliverables and open items

**Deliverables**

1. `packages/config` (registry, resolver, codegen, hooks, decorators, test helpers) with CI checks `config-registry-lint`, `appendix-r-sync`, `nn18-keys`, `help-key-lint`, `schema-boundary`.
2. `packages/rules` with `RULES_PORT`, ZEN and CEL adapters, ADR, fixtures harness, evaluation recorder; seed rule sets registered (content per owning phase).
3. `packages/workflow` items API, `wf.items` schema, seed item types (Appendix R §R.11), chase and escalation workflows, widgets.
4. Studio screens SCR-P03-01 to SCR-P03-32 (axe clean; keyboard and screen-reader paths tested; mobile personal settings).
5. Flags and kill-switch registry with probes and drill reminders; all NN-39 switches registered.
6. Configuration bundle export/import, templates library (6 seeds), sandbox, compare, "Explain my configuration".
7. `docs/config/` developer guides and runbooks.

**Exit gate**

- [ ] All §12 scenarios and listed NN tests green; zero unregistered keys; Appendix R in sync with the seed.
- [ ] p95 resolve ≤ 2 ms warm; invalidation ≤ 60 s measured across pods.
- [ ] Pilot company admin completes the §1 20-minute script unaided; pilot individual completes the 2-tap tasks on mobile web (app parity re-tested in P22).
- [ ] Items API frozen and published in `docs/interfaces/`; `items-adoption` architecture test wired into CI so that each adopting phase (FR-P03-81) fails its own exit gate without items; a reference adopter (test module) passes it.
- [ ] Every NN-39 kill switch drilled once on the test tenant.
- [ ] **Export-map entries registered** (`xpt.export_map`): `cfg.setting_values` (tenant scopes) → `99 System Data (CSV and JSON)/Settings and Customisations/settings.csv|.xlsx|.json`; `cfg.custom_field_defs`, `cfg.status_sets`, `cfg.numbering_schemes`, `cfg.form_versions`, `cfg.letterheads` → same folder (`customisations.xlsx` + JSON); `cfg.setting_changes` and `cfg.change_requests` → `99 System Data (CSV and JSON)/Settings and Customisations/Change history/`; `rul.evaluations` → alongside the parent record (`… /04 Evidence and Certificates/Rule decisions.xlsx`) and `99 System Data (CSV and JSON)/Rule Decisions/`; `rul.adoptions` → `Settings and Customisations/Rules in use.xlsx`; `wf.items` with waits, clocks, interims and chase log → human file `Open and Waiting Items.xlsx` at the parent record folder and full set under `99 System Data (CSV and JSON)/Open and Waiting Items/`; `cfg.config_bundles` → `Settings and Customisations/Configuration bundle (ld-config-1.0).json` (Appendix K §K.3.5, §K.11).
- [ ] **Settings registered** in Appendix R §R.9 (`cfg`, `rul`, `wf`, `ntf` areas) and **help keys** of FR-P03-104 registered in `hlp`.
- [ ] Error codes registered (ranges `LD-CFG-001`–`099`, `LD-RUL-001`–`049`, `LD-WF-100`–`149`; `LD-WF-001`–`099` belong to P02; X-28) — enumerated below and mirrored in Appendix B §B.5.3; codes not listed are reserved:

| Code | Meaning (user message key `hlp.<module>.err_<nnn>`) |
|---|---|
| `LD-CFG-001` | Value type or schema invalid |
| `LD-CFG-002` | Child-direction rule violated (narrow / raise / lower only) |
| `LD-CFG-003` | Text contrast below 4.5:1 |
| `LD-CFG-004` | Value outside platform, brand or plan bounds, or below a floor |
| `LD-CFG-005` | Plan limit reached (upgrade options shown, none pre-selected; NN-50) |
| `LD-CFG-006` | Value locked at a parent tier |
| `LD-CFG-010` | Setting is locked |
| `LD-CFG-012` | Governed key — create a change request |
| `LD-CFG-013` | Citation required for this key |
| `LD-CFG-014` | Impact preview older than 24 hours — refresh before submitting |
| `LD-CFG-015` | Effective date earlier than the key's lead time |
| `LD-CFG-020` | You cannot approve your own change |
| `LD-CFG-021` | Checker not eligible (delegated from the maker or same SoD group) |
| `LD-CFG-022` | Change request expired |
| `LD-CFG-030` | Numbering token duplicate |
| `LD-CFG-031` | Numbering token invalid |
| `LD-CFG-040` | Custom form fails the accessibility check |
| `LD-CFG-050` | Kill switch cannot be released by the person who engaged it |
| `LD-CFG-051` | Kill-switch drill overdue (warning) |
| `LD-CFG-060` | Sandbox promotion conflicts with live changes |
| `LD-CFG-070` | Imported row rejected (locked or out of bounds) |
| `LD-CFG-071` | Configuration bundle signature invalid |
| `LD-CFG-080` | Support session needs tenant approval |
| `LD-CFG-081` | Emergency override expired — automatically reverted |
| `LD-RUL-001` | Rule set not found or not active for this jurisdiction and date |
| `LD-RUL-002` | Rule content (JDM/CEL) invalid |
| `LD-RUL-003` | Golden suite failed — mismatches not accepted |
| `LD-RUL-004` | Citations incomplete — cannot submit |
| `LD-RUL-005` | Source hash does not match the cited source |
| `LD-RUL-006` | Rule unverified — result is advisory only (NN-38) |
| `LD-RUL-007` | Pinned version expired — re-adopt or move to current |
| `LD-RUL-008` | Adaptation outside the permitted parameters |
| `LD-RUL-009` | Evaluation input incomplete |
| `LD-RUL-010` | Emergency block in force — action blocked |
| `LD-RUL-011` | Reviewer must differ from maker |
| `LD-RUL-012` | Reviewer of record lacks the required qualification |
| `LD-RUL-013` | Cannot retire a rule set still adopted without a replacement |
| `LD-RUL-014` | A challenge to this rule set is already open |
| `LD-RUL-015` | A code release cannot change published legal content (NN-30) |
| `LD-WF-100` | Item type not allowed for this parent |
| `LD-WF-101` | Item owner cannot be resolved |
| `LD-WF-102` | Waiting party type not allowed for this item type |
| `LD-WF-103` | Expected-by date required for a waiting item |
| `LD-WF-110` | Chaser deferred — quiet hours or business calendar |
| `LD-WF-111` | Chaser stopped — stop condition met |
| `LD-WF-112` | LawDocs never contacts courts, registries or regulators automatically |
| `LD-WF-113` | Counterparty reminder cap reached (NN-34) |
| `LD-WF-114` | Pre-approved series exceeds the maximum reminders (5) |
| `LD-WF-120` | Formality pending — cannot mark executed |
| `LD-WF-121` | Agents cannot waive an item |
| `LD-WF-122` | Evidence required to resolve this item |
| `LD-WF-123` | A checker must resolve this item type |
| `LD-WF-130` | Task has open dependencies |
| `LD-WF-131` | Task evidence missing |

**Demo script (10 minutes).** Company admin renames statuses, adds custom fields, sets a numbering scheme and letterhead; individual changes theme and text size on mobile; content editor drafts a State stamp-duty row, reviewer of record approves it with a future date, preview shows impact; an agreement hits the formalities gate with registration waiting on the Sub-Registrar while the legal clock keeps counting; owner sends a one-tap chaser to the counterparty; security officer engages and a second person releases an ESP kill switch.

**Open items**

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-P03-01 | ZEN Node binding maturity and licence; CEL JavaScript implementation choice | CTO (ADR sprint 1) | JSON Logic adapter behind `RULES_PORT` |
| OI-P03-02 | State-wise stamp-duty tables and registration thresholds — primary sources per State | P08 content team + `PLT_LEGAL_REVIEWER` | Rows `SECONDARY_ONLY` → indicative; manual stamp route |
| OI-P03-03 | RB-IOS 2026 clause numbers for the RE wait and filing windows | P15 content | Advisory clocks labelled [VERIFY] |
| OI-P03-04 | Plan limits for custom fields, item types, sandboxes, templates | [OWNER] with P17 | Seeds in Appendix R |
| OI-P03-05 | Confirm that a single confirmation of an enumerated, bounded reminder series satisfies NN-13 for transactional signing/review reminders | [OWNER] + [COUNSEL] | `CONFIRM_EACH` only until confirmed |
| OI-P03-06 | TCCCPR 2026 calling windows and AI-voice disclosure parameters for `IN.ntf.tcccpr` | P19 | Voice channel flag OFF |
| OI-P03-07 | Whether an external flag service (e.g., Unleash) is adopted or the in-house registry suffices | CTO | In-house registry |
| OI-P03-08 *(v1.1)* | NIST SP 800-63B revision and breached-password service for `sec.org.password.*` [VERIFY] | `PLT_SECURITY_OFFICER` | Length ≥ 12, local breach list |
| OI-P03-09 *(v1.1)* | Which plans carry BYOK (`sec.org.byok.kms_key_ref`) and the key-loss liability wording [COUNSEL] | [OWNER] | Enterprise only; feature flag OFF |
