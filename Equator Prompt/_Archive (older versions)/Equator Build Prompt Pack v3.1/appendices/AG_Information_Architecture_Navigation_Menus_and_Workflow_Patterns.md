# Appendix AG — Information Architecture, Navigation, Menus and Workflow Patterns (v3.1, 24 October 2026)

## AG.0 Purpose, sources, precedence

### AG.0.1 What this appendix owns

This appendix makes the whole product navigable as **one system**. It specifies:

- the application shells and the navigation model shared by every portal (AG.1);
- the complete menu tree of each portal, with every leaf mapped to a screen ID and an owning phase (AG.2);
- the settings menu, aligned to the Appendix V catalogues (AG.3);
- the unified Work Inbox and notification centre (AG.4);
- global search and the command palette (AG.5);
- role dashboards, the widget catalogue and the "next best action" rules (AG.6);
- a library of reusable workflow patterns (AG.7);
- what tenants may customise in menus and terminology, plus onboarding tours and in-app help (AG.8);
- accessibility, performance, privacy-safe analytics and usability KPIs for navigation (AG.9);
- the data model, APIs, events, error codes and acceptance tests (AG.10);
- addenda for P00, P01, P12, P13, P15 and P16 (AG.11).

It adds no business module. Every object it puts in a menu is owned elsewhere; AG owns only **where it appears, who sees it, how one gets to it and how it behaves as a pattern**.

### AG.0.2 Sources

Appendix C (screen inventory, navigation maps §C, dashboards §D, design system §E, UX principles §F); Appendix S (portal registry §2.0, dashboards §5, RBAC §6, settings shell §7); Appendix V (settings catalogue §V.4, settings UX §V.5, `cfg` schema §V.6); Appendices W (chambers), X (Operations Platform), Y (marketing), Z (HRMS, payroll, controls), AA (marketplace and registry), AB (revenue registry), AC (exports and connectors), AD (group), AE (engineering and assurance), L (saved views `core.saved_views`), O (billing settings SCR-P05-19…34), P (website copy, route index §3.1), R (Case Desk SCR-P02-93…95); phases P00–P21 §6 screen tables. External standards: WCAG 2.2 (W3C Recommendation, 5 October 2023); WAI-ARIA Authoring Practices (menu button, disclosure navigation, combobox and dialog patterns); Apple Human Interface Guidelines and Material Design 3 guidance on tab bars (3–5 destinations). No legal fact is introduced here; where a navigation rule depends on law it cites the owner file.

### AG.0.3 Precedence

1. The master prompt (NN rules, §15 X-resolutions) and the owner appendix of an object prevail on that object's rules, fields and permissions.
2. **This appendix prevails** on shell anatomy, menu placement and order, labels of menu items (subject to Appendix P terminology and copy lint), context switching, deep-link and back-navigation behaviour, the inbox, search, the command palette, dashboard composition, navigation analytics and the workflow pattern library.
3. AG **supersedes** Appendix C §C.1 (web global frame), §C.2 (side navigation) and §C.3 (mobile tabs), and amends P13 FR-P13-03 (top navigation) through FR-P13-V31-AG01. Appendix C §D and Appendix S §5 remain the widget defaults; AG.6 extends them.
4. Menus never grant access. A route is protected by its owner's policy whether or not a menu item points to it (AG.1.4 rule R-8).

### AG.0.4 Decisions and requirements recorded here (add to `02`)

| ID | Statement | Why |
|---|---|---|
| **D3-45** | **Navigation registry.** Every menu, tab bar, palette command, quick action and settings rail entry is a data row in `cfg.nav_items`, resolved server-side for each request context as *published* ∧ *permission held* ∧ *feature flag ON* ∧ *plan or stream entitlement granted* ∧ *tenant kind matches* ∧ *not hidden by an allowed override*. One shell framework (`packages/shell`) renders all web apps; one native shell renders mobile. Tenants customise menus only through tiered overrides (AG.8). | Ends drift between C §C.2, phase screen tables and code; makes flags and entitlements visible in the UI without code changes; makes NN-33 apply to menus. |
| **D3-46** | **Unified Work Inbox, federated by data plane.** One inbox per user collects tasks, approvals (every maker-checker request from `core.config_change_requests`, `ctl.approval_requests`, chambers, group, engineering and marketing queues), mentions, messages, deadlines and system updates. Each data plane keeps its own inbox store (`core.inbox_items` in the case plane; `ops.ws_inbox_items` in the business database); the shell's backend-for-frontend (BFF) merges them **without a cross-database join** (D3-20). The inbox never decides: every action calls the owning engine's API, which re-runs its own checks (step-up, SoD, authority, validators). | One place to act; no approval lost in a module the approver never opens; preserves plane isolation and NN-36. |
| **D3-47** | **Route, screen-ID and top-navigation canonicalisation.** (a) Operations Platform routes are host-relative on `ops.equatorresolution.in`; the `/ops` prefix used in P17 and P18 screen tables is dropped (old paths 301); (b) the route collisions listed in AG.0.5 are resolved as stated there; (c) the P13 phase §6 IDs SCR-P13-01…19 prevail over Appendix C §B.1/§B.14 allocations; (d) chambers workspace segments are added to the reserved-slug list; (e) the public site uses the v3.1 mega-menu of AG.2.1. | The review found real collisions that would break routing and cross-references. |
| **R-71** | Navigation, menus, inbox, search, palette and dashboards are specified per portal and role, rendered from the navigation registry, and measured by the usability KPIs of AG.9.4 (management instruction of 24 October 2026: "improvise … menu"). | — |
| **R-72** | Every workflow screen is built from the AG.7 pattern library, with the pattern's states, timeouts, undo, confirmation and audit rules; deviations need an ADR. | — |

### AG.0.5 Errors and inconsistencies found in review (resolved here; owner-file changes listed in the log)

| # | Found | Resolution (binding from v3.1) |
|---|---|---|
| 1 | **P13 screen-ID collision.** Appendix C §B.1 allocates SCR-P13-01…32 with one meaning (e.g., SCR-P13-08 "Calculators hub"); P13 §6 uses SCR-P13-01…19 with another (SCR-P13-08 = neutral directory); master X-51 cites SCR-P13-18 in the P13 §6 sense. | P13 §6 IDs prevail (D3-47(c)). Appendix C IDs that have no P13 §6 counterpart are renumbered SCR-P13-40…58 (map in AG.2.1, last table). SCR-P13-60…69 stay reserved for the Decisions Library (Appendix R §3.9). |
| 2 | **Operations Platform route prefixes differ** (P16 host-relative `/crm/...`; P17 `/ops/mkt/...`; P18 `/ops/hr/...`; P21 `ops /group`). | Canonical host-relative routes (D3-47(a)): `/mkt/...`, `/hr/...`, `/time/...`, `/pay/...`, `/controls/...`, `/org/...`, `/me/...`, `/group/...`. |
| 3 | **`/audit` collision** in `apps/ops`: SCR-P16-41 and SCR-P18-43. | `/audit` = SCR-P16-41 (Internal Audit workspace home); SCR-P18-43 becomes `/audit/workforce` (tab). |
| 4 | **`/exports` collision** in `apps/ops`: SCR-P16-40 (department exports) and SCR-P21-09 (all exports). | `/exports` = SCR-P21-09; SCR-P16-40 becomes the saved view "Department exports" with scope `OPS_DEPARTMENT` pre-filtered. |
| 5 | **Three approval inboxes for the same approver** (SCR-P15-05 settings, SCR-P16-03 operations, SCR-P18-36 controls) plus SCR-P20-11 (chambers), SCR-P21-22 (group grants), SCR-AE-02 (CAB) and SCR-P17-09 (marketing reviews). | All become **source tabs of the Work Inbox** (AG-SCR-01, D3-46). The listed screens remain as deep-link targets (the detail and decision views) and as filtered inbox views; their routes 302 to `/inbox?source=…` when opened without an item ID. |
| 6 | **Chambers workspace routes collide with practice slugs.** P20 uses `/chambers/work`, `/chambers/workload`, `/chambers/hr`, `/chambers/me`, `/chambers/controls`, `/chambers/dashboards/…`; Appendix W §W.3.2 reserves only `login`, `start`, `admin` and others, not these. A practice registering slug `work` would shadow the workspace. | Add `work`, `workload`, `hr`, `me`, `controls`, `dashboards`, `inbox`, `settings`, `exports`, `offboarding`, `approvals`, `reports` to the reserved list (D3-47(d)); registration returns `CHM_SLUG_RESERVED`. Existing practice slugs equal to these (none expected before launch) are migrated with a 301. |
| 7 | **Chambers route roots differ:** Appendix C §B.11 and Appendix S §2.0 land chambers users on `/app/chambers` (SCR-S-D10, SCR-P10-03); P20 uses `/chambers/...` and SCR-P20-29 replaces SCR-S-D10. | Canonical chambers shell root `/chambers/work` (home = SCR-P20-29 dashboard `workspace_home`; *v3.1 integration:* the earlier name `practice_home` is Appendix W's public home-page kind, §W.3.1, so the dashboard code is `workspace_home`; work queues SCR-P20-18 move to `/chambers/work/queues`); `/app/chambers/*` 301s. `core.login_portals.dashboard_route` for `chambers` is updated. |
| 8 | **Top navigation differs:** Appendix C §C.1 (Resolve · Solutions · Neutrals · Academy · Rules & Fees · Resources · About) vs P13 FR-P13-03 and Appendix P §3.0 (Resolve · Disputes · For Organisations · Neutrals · Fees · Rules · Learn · About). | Superseded by the v3.1 mega-menu (AG.2.1), which keeps every FR-P13-03 destination and adds Marketplace, Chambers and Help. |
| 9 | **Mobile party tabs differ:** Appendix C §C.3 (Home · Cases · Messages · Payments · Profile) vs P07 SCR-P07-17 ("app tab Inbox with badge"). | AG.2.13: Home · Cases · Inbox · Pay · More. Messages move into Inbox (Messages filter) and the case hub. |
| 10 | Superseded screens still listed in Appendix C: SCR-P05-11/-12 (replaced by `/settings/billing/*`, SCR-P05-19…34, Appendix O O-R3); SCR-P13-18 (X-51); SCR-P10-03 and SCR-P10-12 health dashboard (Appendix W §W.0.5); SCR-P06-65 `/advocates` (X-60, now the Post-Resolution Professional Chooser SCR-P19-30). | Menus in AG.2 point only to the successors. *v3.1 integration:* SCR-P19-30 is agreed with Appendix AA §AA.11.2 ("SCR-P06-65 v3" is a retired alias). |
| 11 | Appendix AE registers non-conforming IDs `SCR-AE-01…12`. | Kept as aliases; canonical IDs SCR-P21-AE01…AE12 (owning phase P21), consistent with the `SCR-P19-AB01…AB10` precedent. |
| 12 *(v3.1)* | **Pricing pages had two IDs:** this appendix allocated SCR-P13-44 to `/pricing/organisations` and `/pricing/professionals`, while P13 §6 (which prevails, D3-47(c)) defines SCR-P13-20 (`/pricing/organisations`), SCR-P13-21 (`/pricing/professionals`) and SCR-P13-22 (`/pricing/business-assure`). | Menus use SCR-P13-20…22; SCR-P13-44 is withdrawn and stays unallocated. Where Appendix C §H item 6 maps a v1 ID differently from the AG.2.1 renumbering map (for example C-04 "section of P13-01" against SCR-P13-40), the AG.2.1 map prevails for menus and new references. |
| 13 *(v3.1)* | **Approval keys differed:** Appendix X §X.3.5 bound `A` approve, `R` reject, `D` delegate, against AG.5.4–AG.5.5 (`A` reassign, `R` reply; no one-key approve); P09 FR-P09-50 binds `e` escalate against AG's `E` mark done. | Screen-scoped key maps (AG.5.5 rule 5): inside an open decision panel `A`/`R`/`D` open the approve, reject or delegate confirmation; on a screen that declares its own map (GRO desk, scrutiny queue, page editor) the screen's single keys apply and the inbox keys do not. Global chords never change. |

---

## AG.1 Navigation model

### AG.1.1 Shell catalogue

A **shell** is a top-level application frame with its own host or route root, sign-in client, layout, menu and session rules. Every screen belongs to exactly one shell (`cfg.nav_items.shell`). A person with memberships in several shells moves between them through the context switcher (AG.1.3); sessions are per Keycloak client, so crossing shells may ask for step-up.

| Shell code | Audience | Host / route root | Keycloak client (App. S §2.0) | Min ACR | Layout | Lands on (home) | Mobile space (P12) |
|---|---|---|---|---|---|---|---|
| `public` | Visitors, prospects, respondents before sign-in | `equatorresolution.in/` (SSR/SSG), `/hi/…` | none (sign-in links only) | — | Mega-menu header, footer, no side nav | SCR-P13-01 | none (mobile web) |
| `party` | Parties, organisation users acting as parties | `/app` | `eq-portal-parties` | aal1 (aal2 for signing, payment above threshold, sealed) | Top bar + side nav | SCR-S-D01 | `party` |
| `representative` | Counsel, representatives, law firms | `/app/counsel` | `eq-portal-counsel` | aal2 | Top bar + side nav + client switcher | SCR-S-D02 | `party` (representative mode) |
| `neutral` | Mediators, conciliators, facilitators, arbitrators, experts | `/app/neutral?space=mediation\|arbitration` | `eq-portal-neutral` | aal2 (aal2-pr to sign) | Top bar + side nav + space toggle | SCR-S-D03 / SCR-S-D04 | `neutral` |
| `chambers` | Chambers owners, admins, case managers, staff, HR, accounts, tenant neutrals | `/chambers/work` (or verified custom domain / sub-domain) | `eq-portal-chambers` / `-{slug}` | aal2 | Top bar + side nav, tenant-branded | SCR-P20-29 (`practice_home`) | `neutral` (tenant variant) + `chambers` tabs (AG.2.13) |
| `enterprise` | Lenders, insurers, employers, listed companies, universities; GRM desk; POSH IC (sealed sub-shell) | `/app/enterprise`, `/app/grm`, `/app/posh` | `eq-portal-enterprise` | aal2 (IC: aal2, 10 min idle) | Top bar + side nav; POSH sub-shell has SealedBanner and no global search | SCR-S-D08 / SCR-S-D09 / SCR-P09-17 list | `enterprise` |
| `console` | Equator case services: case managers, registrar, panel, quality, escrow, safeguarding, committee (via its own portal) | `console.equatorresolution.in` (`/staff/login`) | `eq-portal-staff` | aal2-pr | Top bar + side nav + queue rail | SCR-S-D05 / SCR-S-D06 | `neutral` (staff tab, case managers only) |
| `ops` | Equator and group-company workforce (all departments, HR, payroll, controls, engineering, group) | `ops.equatorresolution.in` | `eq-portal-ops` | aal2-pr | Top bar + department rail + side nav | SCR-P16-01 | `employee` (ESS), `ops-approvals` (AG.2.13) |
| `selfservice` | Every employee (ESS) — Equator and group companies; chambers staff ESS lives in `chambers` | `ops.equatorresolution.in/me` | `eq-portal-ops` | aal2-pr | Reduced side nav (Me area) | AG-SCR-20 (`/me`) | `employee` |
| `admin` | Platform super-admin: `platform_admin`, `dpo`, `legal_reviewer` (platform scope), `support_agent`, SRE | `admin.equatorresolution.in` | `eq-portal-admin` | aal2-pr; aal3 for elevation | Top bar + side nav + elevation banner | SCR-S-D12 | none (web only) |
| `assurance` | External and internal auditors (engagement-scoped) | `assurance.equatorresolution.in` | `eq-portal-assurance` | aal2-pr (passkey) | Top bar + side nav; watermark on every page | SCR-P21-AE09 (`SCR-AE-09`) | none |
| `partners` | Partners | `/partners` | `eq-portal-partners` | aal2 | Top bar + side nav | SCR-S-D11 | none |
| `committee` | Committee members and chairs | `/committee` | `eq-portal-committee` | aal2-pr | Minimal side nav | SCR-S-D07 | content-free push only |
| `academy` / `campus` | Learners, trainers, students, university admins | `/academy`, `/campus` | P10 clients | aal1/aal2 | Top bar + side nav | SCR-P10-10 / SCR-P10-19 | none |

The `selfservice` shell is the `ops` shell rendered with the `me` menu only, so that an employee who holds no department role sees nothing else. It is a separate shell code so that its menu, tour and dashboard can be configured separately.

### AG.1.2 Shell anatomy (web)

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ Skip link · [Logo/tenant] [Context chip ▾] [Search / ⌘K ……………] [Inbox ●12] [Help ?] [Me ▾] │  ← global header (56 px)
├──────────────┬───────────────────────────────────────────────────────────────────────────┤
│ Side nav     │ Breadcrumbs (depth ≥ 3)                                                    │
│ (240 px;     │ Page header: H1 · status chip · primary action · secondary menu (…)         │
│ collapsible  │ ────────────────────────────────────────────────────────────────────────── │
│ to 64 px)    │ Content (max 1200 px reading; tables may use full width)                    │
│ Group label  │                                                                            │
│  • Item  (3) │ Right drawer (optional): details, AI assist (labelled), help, activity     │
│  • Item      │                                                                            │
│ ─ Pinned ─   │                                                                            │
│ ─ Settings ─ │                                                                            │
└──────────────┴───────────────────────────────────────────────────────────────────────────┘
```

| Zone | Rules |
|---|---|
| Skip link | First focusable element: "Skip to main content"; a second skip link "Skip to navigation" appears on shells with side nav. |
| Logo / tenant | Links to the shell home. On tenant-branded shells, the Equator legal-entity line remains in the footer of every page (App. P §3.0). |
| Context chip | Shows `{role label} · {organisation or company} · {legal entity if > 1}`; opens the context switcher (AG.1.3). Always visible; never truncated below the role label. |
| Search | Opens global search and the command palette (AG.5). Absent in the POSH sub-shell, the committee portal and the `public` shell (which has site search only). |
| Inbox | Bell-and-tray icon with an unread-actionable count (tasks + approvals + mentions due; not FYI updates). Opens the inbox drawer; "Open inbox" goes to AG-SCR-01. Counts in sealed sub-shells are content-free. |
| Help | Same position on every screen (WCAG 3.2.6 Consistent Help): contextual help panel (AG.8.5), "Contact support" (SCR-P16-42), keyboard shortcuts (AG-SCR-11), "What's new". |
| Me menu | Profile, settings (`/settings/me`), out-of-office and delegation (AG-SCR-06), language, accessibility, sign out, sign out everywhere. |
| QuickExit | On FAM, WRK-POSH, safety-flagged and sealed screens: top-right button and `Esc` twice (Appendix C §F.5); z-index 1200; never hidden by any customisation (L). |
| Side nav | Ordered groups from the resolved menu (AG.1.4). Maximum depth two in the side nav (group → item); third-level navigation is in-page tabs. Badges show counts from the item's `badge_source`. A "Pinned" group lists up to 8 user pins. "Settings" is always the last group. Collapsed state is remembered per user per shell. |
| Breadcrumbs | Shown at depth ≥ 3. Built from the route's registered parents, not from browser history. The last crumb is the current page (`aria-current="page"`), not a link. Case pages show the case number crumb in mono type. |
| Page header | One H1; at most one primary action; other actions in a "More actions" menu; destructive actions never primary. |
| Footer (authenticated) | Legal-entity line, Grievance Officer link, privacy notice, accessibility statement, status page, version (`/v1/meta/version` tag). |

**Mobile web (< 768 px).** The side nav becomes a full-height drawer opened by a "Menu" button (labelled, not icon-only); the header keeps logo, context chip (role label only), search icon, inbox icon. Breadcrumbs collapse to a "Back to {parent}" link.

### AG.1.3 Context model and switcher (SCR-P01-38 extended as AG-SCR-05)

**Context dimensions.**

| Dimension | Meaning | Carried in | Who has more than one |
|---|---|---|---|
| Shell | Which application frame | Host / route root | Anyone with memberships in several portals |
| Organisation (tenant) | The tenant whose data is in view | `Equator-Context.tenant` (X-01) | Counsel acting for clients of several enterprises; neutrals on Equator and in chambers; group staff |
| Legal entity / company | Employing or contracting entity in `grp` (ops) or a tenant's legal entity (enterprise with several entities) | `Equator-Context.entity` (additive claim, D3-45) | Group staff working for Equator, Finbyx and Udofin (NN-38) |
| Acting role | The role whose permissions apply | `Equator-Context.role` | Most professionals and staff |
| Chambers | A chambers tenant (a special organisation) | `Equator-Context.tenant` with `tenant_kind = chambers` | Neutrals who are members of several chambers |
| Case | The case in focus | `Equator-Context.case` | Everyone with several cases |
| Client (representative) | The party the representative is acting for | Derived from the authority on the case | Counsel |

**Switcher behaviour.**

1. **Open:** click the context chip, or `Ctrl/Cmd+Shift+O`, or palette command "Switch context". The panel lists memberships grouped by shell, then organisation, then entity, then role, with a search box when there are more than 8 rows. Each row shows the tenant logo, role label, entity short name and a badge with that context's actionable inbox count (counts only, computed by the target plane).
2. **Only valid contexts are listed:** active memberships with an unexpired grant; cross-company grants show a countdown ("Finbyx — read access until 14 Nov"). Contexts blocked by an ethical wall (Appendix AD §AD.10) are listed greyed with the reason "Not available: conflict wall" and cannot be selected.
3. **Workforce and consumer identities never mix** (Appendix S §1.3): a workforce session never lists party, counsel or neutral memberships, and vice versa. The switcher says "Signed in as staff. To act as a party, sign in through the parties portal."
4. **Switching within a shell** re-issues the context (gateway-signed `Equator-Context`), clears in-memory query caches and palette recents for the old context, closes drawers and modals, and lands on the target context's home, unless a deep link asked for a page that exists there. Unsaved form data prompts: "Save as draft", "Discard", "Stay". Drafts are context-bound and never carried into another context.
5. **Switching across shells** opens the target shell's home in the same tab via SSO; if the target client's minimum ACR is higher, the step-up dialog appears first. The previous shell's session stays alive until its own idle timeout.
6. **Default context at sign-in:** the last-used context if still valid; else the portal default from the post-login gate (Appendix S §1.5); else the switcher is shown before any data loads.
7. **Every irreversible confirmation** (AG.7.16) repeats the context line ("You are approving as Accounts checker for Equator Resolution Service Private Limited").
8. **Case context** is set when a case page opens and cleared when the user leaves case routes. Actions taken from the inbox or palette on a case item set the case context for the duration of that action only.
9. **Representative client switcher** (representative shell): a second chip "Acting for: {client}" filters matters; "All clients" is the default; acting on a case always uses the authority recorded on that case (NN-27) regardless of the chip.
10. **Audit:** each switch writes `equator.identity.context.switched.v1` (from and to context IDs, reason `user|deeplink|grant_expiry`), never page content.

### AG.1.4 Menu rendering (navigation resolver)

The resolver (`packages/shell/nav-resolver`, server-side in the BFF of each app) computes the menu for a request context. Pseudo-code:

```ts
resolveMenu(ctx: RequestContext, shell: ShellCode): ResolvedMenu {
  const items = registry.publishedItems(shell, ctx.appRelease)          // cfg.nav_items at the pinned menu version
  const overrides = overridesFor(ctx.tenant, ctx.unit, ctx.user)        // cfg.nav_overrides, tiers T (tenant/unit) and user prefs
  const perms = cerbos.checkPermissions(ctx.principal, items.flatMap(i => i.permissions))  // one batched call
  const flags = flagService.evaluate(items.flatMap(i => i.flags), ctx)  // OpenFeature + DB legal flags
  const ents = entitlementService.check(items.flatMap(i => i.entitlements), ctx.tenant) // App. O §4, App. AB
  return prune(items
    .filter(i => i.tenantKinds.includes(ctx.tenantKind) || i.tenantKinds.length === 0)
    .filter(i => allOf(i.permissionsAll, perms) && anyOf(i.permissionsAny, perms))
    .filter(i => allOf(i.flags, flags))
    .filter(i => allOf(i.entitlements, ents))
    .filter(i => contextConditions(i.conditions, ctx))                  // e.g., vertical, sealed role, case open
    .map(i => applyOverride(i, overrides))                              // rename, reorder, hide (never for lock_tier = 'L')
  )                                                                     // drop empty groups; enforce depth ≤ 2
}
```

**Rules.**

| # | Rule |
|---|---|
| R-1 | An item is **visible** only if published, the acting role holds every permission in `permissions_all` and at least one in `permissions_any` (when set), every flag in `flags` is ON for the context, every entitlement in `entitlements` is granted, the tenant kind matches and context conditions hold. |
| R-2 | **Flag OFF → hidden, never teased.** Features waiting for counsel, Board or vendor (e.g., `marketplace.paid_placement`, `directory.public_professionals`, `postres.advocate_panel`) are invisible to everyone except, in Settings → Feature status (SCR-P00-06), the roles that may propose turning them on. |
| R-3 | **Entitlement missing → hidden from the menu.** Tenant admins see the feature in Settings → Plan and billing (SCR-P05-20) as "Available on {plan}" with a neutral description. No upgrade prompt appears inside a case workflow, a statutory workflow or to a party (NN-29; Appendix AB RA-6: statutory duties are in every tier). |
| R-4 | **Permission missing → hidden.** If a user reaches the route directly, the page returns `403 FORBIDDEN` with "You don't have access to this page" and, when the permission is requestable (`cfg.nav_items.requestable = true`), a "Request access" button that creates an access request in the tenant admin's inbox. Sealed and flag-OFF routes return `404 NOT_FOUND` so their existence is not revealed. |
| R-5 | **Locked items** (`lock_tier = 'L'`) cannot be hidden, renamed outside the glossary, or moved out of their group: Help, Grievance / complaints, Privacy centre, Accessibility statement, Legal notices, Sign out, QuickExit, the "Sponsored" label on marketplace slots, the Grievance Officer link in footers, the free-forum signpost entry on party homes, and the Work Inbox (AG.8.2). |
| R-6 | **Badges** come from the inbox count service by `badge_source` (e.g., `inbox.approvals.waiting_for_me`, `cases.actions_due`). Counts are capped at "99+", announced to screen readers as "{label}, {n} items need action". A badge never shows a sealed count outside the sealed sub-shell. |
| R-7 | **Caching:** the resolved menu is cached per (user, context, menu version, flag-set hash, entitlement hash) for 5 minutes and invalidated on `equator.cfg.setting.changed.v1`, `equator.cfg.nav_menu.published.v1`, `equator.identity.membership.granted.v1` / `.revoked.v1`, `equator.rev.stream.killed.v1` and context switch. Payload ≤ 8 KB gzip. |
| R-8 | **Menus are not security.** Every route and API re-checks policy. CI test `NAV_ROUTE_GUARDED` fails if a registered route has no server-side policy check. |
| R-9 | **Empty groups are pruned**; a group with one visible child renders the child at top level. |
| R-10 | **Depth:** side nav ≤ 2 levels; in-page tabs ≤ 8; a tab set larger than 8 uses a "More" tab menu. |
| R-11 | **Order:** platform default order (`sort_key`) → tenant override (T) → user pins (pins appear in "Pinned", they do not reorder the platform menu). |
| R-12 | **Disabled-with-reason** is used only for actions inside a page whose preconditions are unmet (e.g., "Submit — 2 required documents missing"), never for menu items. |

### AG.1.5 Deep links

| Aspect | Rule |
|---|---|
| Format | `https://{host}/{route}?ctx={contextToken}&src={channel}` where `ctx` is an opaque, signed context hint (tenant + role + case IDs; no names) and `src` ∈ `email`, `sms`, `whatsapp`, `push`, `inbox`, `ics`, `export`, `share`. Links in SMS use the short-link service with the same target. |
| Landing on the action | A deep link opens the action screen (respond, pay, sign, join, upload, approve), not the dashboard (Appendix S §5 rule 2), after the minimum step-up for that action. |
| Context resolution | If the user holds the hinted context, the shell switches to it automatically and shows a dismissible banner "Switched to {context} to open this link" with "Switch back". If the user holds a different valid context for the same object (e.g., a new role), that one is used. If none, `403` page with "This link is for another account" and a sign-out-and-switch button; nothing about the object is shown. |
| Expired or used links | Notice-possession links (`/r/{code}`, P01 FR-P01-13) and approval links obey their owner's expiry; expired links show `410` with `CFG_DEEPLINK_EXPIRED` and the safe next step ("Sign in to see your case"). |
| Sealed matters | Deep links for POSH and sealed items carry no case number or category in the URL or link text; they open the sealed entry with step-up. |
| Mobile | Universal links / App Links for `equatorresolution.in/app/*`, `/r/*`, `/sign/*`, `/pay/*`, `/hearing/*`, `/inbox/*` open the app when installed (P12 FR-P12-14); otherwise mobile web. |
| Calendar (ICS) links | Event titles carry the case number only (Appendix S §7); the link opens the hearing lobby. |
| Shareable internal links | "Copy link" on any record produces a permission-neutral link: the recipient sees the record only if they have access. Copying never embeds tokens. |
| Analytics | `src` is recorded in the privacy-safe navigation event (AG.9.3); URLs with personal data are never logged (route templates only). |

### AG.1.6 Back-navigation rules

| Situation | Behaviour |
|---|---|
| Browser back between pages | Always works; lists restore their filters, sort, scroll position and selected row from the URL state (`?view=…&sort=…&cursor=…`). |
| Inside a wizard (AG.7.1) | Each step is a URL (`/file/{draftId}/step/{n}`); browser back moves to the previous step with data kept; the in-page "Back" link does the same. Leaving the wizard keeps the draft (save-and-resume). |
| Modal or drawer open | Browser back closes the modal or drawer first (history entry pushed on open); `Esc` does the same. |
| After a successful submit (POST) | Post/Redirect/Get: the confirmation page replaces the form in history, so back does not resubmit. A second submit with the same Idempotency-Key returns the original result. |
| After an irreversible action (sign, pay, approve, serve, publish) | Back from the receipt goes to the object's page in its new state, never to the editable form; the form route shows "This was already submitted on {date}" with a link to the receipt. |
| QuickExit | Replaces the current history entry with a neutral external page and clears session storage (Appendix C §F.5); back cannot return. |
| Deep link from outside | A "Back" link in the page header goes to the logical parent (breadcrumb parent), not to the external site. |
| Context switch | History before the switch is kept, but pages from the old context reload with a "This page belongs to {old context} — switch back?" interstitial instead of showing stale data. |
| Mobile hardware back (Android) / swipe back (iOS) | Same as browser back; on a tab root it goes to the Home tab; on Home it backgrounds the app. Pay and sign screens ask "Leave without finishing?" if a provider session is in progress. |
| Session timeout | After re-authentication the user returns to the same route with draft data restored (autosave ≤ 10 s). |

### AG.1.7 Route conventions (D3-47)

1. Route segments are lower-case English nouns; IDs are UUIDv7 or human references (case number, invoice number) where already public to the viewer; locale prefix only on the public site (`/hi/...`).
2. One canonical route per screen; aliases 301. The registry column `cfg.nav_items.route_template` must equal the screen table route of the owning phase.
3. `apps/ops` areas: `/` home · `/inbox` · `/leadership` · `/tasks` · `/crm` · `/onboarding` · `/success` · `/support` · `/grievances` · `/kb` · `/service` · `/finance` · `/training` · `/marketplace-ops` · `/automations` · `/connectors` · `/integrations` · `/mkt` · `/org` · `/hr` · `/time` · `/work` · `/leave` · `/pay` · `/performance` · `/learning` · `/controls` · `/group` · `/engineering` · `/revenue` · `/audit` · `/reports` · `/exports` · `/imports` · `/settings` · `/me`.
4. `apps/web` authenticated roots: `/app` (party), `/app/counsel`, `/app/neutral`, `/app/enterprise`, `/app/grm`, `/app/posh`, `/chambers/*` (workspace segments reserved per AG.0.5 #6), `/partners`, `/committee`, `/academy`, `/campus`, `/settings`, `/inbox`, `/exports`, `/imports`.
5. Old routes are kept as 301 redirects for 12 months and listed in `cfg.route_redirects` (AG.10.1); the link checker in CI fails on any internal link to a redirected route.

---

## AG.2 Complete menu trees per portal

**How to read the trees.** *Group* is the top level (side-nav group or mega-menu column); *Item* is the second level (the menu entry); *Key actions* are the primary in-page actions reached from the item (also registered as palette commands, AG.5.4); *Screen* is the screen ID (the owning phase's screen table governs fields); *Phase* owns the screen; *Gate* is the rendering condition beyond shell membership (role or permission bundle; flag; entitlement). "**New v3.1**" marks a screen proposed here (`AG-SCR-nn`; register in AG.2.14). Items marked 🔒 are locked (AG.8.2). Every tree is seeded as `cfg.nav_items` rows by the owning phase (FR-P00-V31-AG02).

### AG.2.1 Public website mega-menu (shell `public`; D3-47(e); amends FR-P13-03)

**Header layout.** Logo · ten menu buttons (below) · utility bar: **Understand your options** (primary → `/dispute-explorer`) · Respond to a notice · Track · Language · **Log in ▾** (Parties · Representatives and advocates · Mediators · Arbitrators · Organisations · Private ADR Chambers · Partners; staff and committee portals are never linked publicly — Appendix P §3.0).

**Responsive priority.** ≥ 1280 px: all ten buttons. 1024–1279 px: Resolve, Disputes, Neutrals, Marketplace, For organisations, Chambers, then **More ▾** (Training, Resources, About, Help). < 1024 px: "Menu" button opens a full-screen drawer with the ten groups as accordions, the utility actions pinned at the top and the Log in list at the bottom. Mega-menu panels open on click or Enter/Space (not on hover alone), close on `Esc`, follow the WAI-ARIA *disclosure navigation* pattern (not `role="menu"`), and contain plain links only.

| Group (menu button) | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| **Resolve** | Understand your options (Dispute Explorer) | Start; answer questions instead; get the Readiness and Pathway Report | SCR-P02-01 → SCR-P02-03 (SCR-P11-14 when AI intake is ON) | P02 / P11 | AI variant: P11 intake feature ON (tenant `ai.features.*`, App. V §V.4.1); deterministic route always offered (NN-02) |
| Resolve | File a case | Sign in or sign up, then the filing wizard | SCR-P02-04 | P02 | — |
| Resolve | Respond to a notice | Enter notice code; "This is me / not me" | P-20 `/respond` → SCR-P01-09 | P13 / P01 | — |
| Resolve | Track a case | Reference + OTP | SCR-P02-17 | P02 | — |
| Resolve | Verify a document or outcome | Upload or paste hash; enter verification code | SCR-P02-22 · SCR-P06-12 | P02 / P06 | — |
| Resolve | How it works | Ladder explainer; "Equator is not a court" | SCR-P13-40 | P13 | — |
| Resolve | Ways to resolve (negotiation, conciliation, mediation, arbitration, med-arb, pre-litigation mediation, expert determination) | Mechanism page | SCR-P13-41 (template; P-21–P-27) | P13 | Med-arb, expert determination per master §5.2 matrix |
| Resolve | Fees, calculator, fees by vertical, enterprise fees, refunds and waivers | Indicative quote with GST | SCR-P13-06 · SCR-P05-01 | P13 / P05 | — |
| Resolve | Book a consultation call | Slot; pay ANC.CONSULT ₹999 (30 min) or ₹1,999 (60 min) + GST, credited against registration if a case is filed within 30 days (Appendix B; Appendix O O-R4); the free 10-minute call-back stays free *(v3.1)* | SCR-P13-14 | P13 | — |
| Resolve | Get a copy of a settlement or award | Reference + OTP retrieval (`/settlements-and-awards`) | SCR-P02-17 (retrieval mode) | P02 | — |
| **Disputes** (by type) | Loans, cards and payments · Business and commercial · Family, marriage and family property · Insurance · Workplace and employment · International commercial | Vertical hub with free-forum signposts first (NN-20) | SCR-P13-02 | P13 | Vertical enabled for the institution tenant |
| Disputes | Popular situations (subtypes P-10–P-19, e.g., loan settlement, health claim rejected, unpaid MSME invoices, POSH) | Subtype page with Explorer CTA | SCR-P13-42 (template) | P13 | Page published (legal review stamp) |
| Disputes | Calculators and checkers (limitation, MSMED interest, s.12A, OTS, gratuity, POSH checker, grievance SLA check) | Run tool; download result | SCR-P13-12 · SCR-P08-21 | P13 / P08 | Per tool flag |
| **Neutrals** | Find a neutral (Equator panel) | Search, filters, profile (seeded-random order) | SCR-P13-08 (renders SCR-P03-01/-02) | P13 / P03 | — |
| Neutrals | Become a neutral | Eligibility, apply | SCR-P13-43 → SCR-P03-03 | P13 / P03 | — |
| Neutrals | Panels · Code of conduct | Panel list; read versioned rules | SCR-P13-08 (`/neutrals/panels`) · SCR-P13-07 | P13 | — |
| Neutrals | How appointments stay neutral | Neutrality explainer | SCR-P13-09 (`/trust/how-we-stay-neutral`) | P13 | — |
| **Marketplace** | Private Practice Marketplace (search) | Search, filter, compare (≤ 3); sort selector limited to the published sorts (`platform.mkp.search.sort_options`); save a search with opt-in weekly alert (signed in) *(v3.1)* | SCR-P19-01 · SCR-P19-05 | P19 | ≥ 1 `platform.mkp.category.<code>.enabled` ON; else the whole group is hidden |
| Marketplace | How ranking works | Ranking parameters, changelog | SCR-P19-03 | P19 | as above |
| Marketplace | Transparency reports · Dark-pattern audit | Download | SCR-P19-04 · SCR-P19-36 | P19 | as above |
| Marketplace | List your practice or service | Apply; then "My onboarding" tracker with progress score, next action and estimated listing date (FR-P19-72) *(v3.1)* | SCR-P19-10 | P19 | as above |
| Marketplace | Advertise | Rate card and rules | SCR-P19-37 | P19 | `marketplace.paid_placement` ON (G, OFF) |
| Marketplace | Report a listing 🔒 | Complaint form | SCR-P19-09 | P19 | as group |
| Marketplace | Panel note 🔒 | Fixed text in the panel: "The Marketplace is separate from Equator's institutional panel. Nothing here affects Equator appointments." | — | P19 | L (NN-34) |
| **For organisations** | Lenders and NBFCs · Insurers · Employers · Listed companies · Universities · Marketplaces and fintech · Government and legal services | Segment page; request a demo (volume band, `/request-demo`) | SCR-P13-04 | P13 | — |
| For organisations | Grievance Redressal SaaS · POSH Internal Committee SaaS | Variant page with regulator clocks | SCR-P13-05 | P13 | — |
| For organisations | Model clause generator · Clause library | Build clause; DOCX/PDF; verify a clause seal | SCR-P13-13 · SCR-P09-05 | P13 / P09 | — |
| For organisations | Pricing for organisations · Business Assure (MSMEs) | Plans, GST shown | SCR-P13-20 (`/pricing/organisations`) · SCR-P13-22 (`/pricing/business-assure`) *(v3.1: was SCR-P13-44)* | P13 | — |
| For organisations | Developers and integrations | API reference, sandbox keys | SCR-P09-01 | P09 | — |
| **Chambers** | Private ADR Chambers (product) | Features, practice pages, HR add-on "subject to availability" | SCR-P13-45 (`/private-adr-chambers`) | P13 | — |
| Chambers | Pricing for professionals | Plans | SCR-P13-21 (`/pricing/professionals`) *(v3.1: was SCR-P13-44)* | P13 | — |
| Chambers | Start a 14-day trial | Sign-up | SCR-P10-01 (`/chambers/start`) | P10 | — |
| Chambers | Find a practice | Opens Marketplace search filtered to chambers | SCR-P19-01 | P19 | Marketplace gate |
| **Training** | Training overview | Programmes, dates | SCR-P13-46 (`/training`) | P13 | — |
| Training | Programme catalogue | Course cards; enrol | SCR-P10-07 · SCR-P10-08 | P10 | — |
| Training | Equator ADR Institute (opens equatoradr.com) | External link, labelled as leaving the site | — | Y §Y.7.7 | — |
| Training | Verify a certificate | Enter register number or scan QR (`/verify/certificate/{id}`) | SCR-P10-14 | P10 | — |
| **Resources** | Guides and articles (`/learn`) · Glossary · Letters library | Read; "last legally reviewed" stamp | SCR-P13-47 | P13 | — |
| Resources | Published awards and settlements (Decisions Library) | Search published outcomes (consented only, NN-26) | SCR-P13-60 → SCR-P13-63 | P13 (App. R §3.9) | — |
| Resources | Rules, procedure and codes (incl. appointment policy, AI governance) | Version picker, diff, PDF with hash | SCR-P13-07 | P13 | — |
| Resources | Outcomes and statistics | Process KPIs only, never win rates | SCR-P13-09 (`/trust/outcomes`) | P13 | Claims Register entries active (NN-17) |
| Resources | Free tools | as Disputes → Calculators | SCR-P13-12 | P13 | — |
| Resources | Press | Releases, media contact | SCR-P13-10 (`/press`) | P13 | — |
| **About** | About Equator · Governance · Advisory council · Secretariat | Read | SCR-P13-10 | P13 | — |
| About | Trust and security · Sub-processors · DPA | Read; download | SCR-P13-09 | P13 | — |
| About | Service status · Report a vulnerability | Status; VDP form | SCR-P14-10 · SCR-P14-11 | P14 | — |
| About | Careers | Jobs; apply | SCR-P18-07 (`/careers`) | P18 | — |
| About | Partner programme | Apply | SCR-P13-15 | P13 | `portal.partners.enabled` |
| About | Contact | Form; office NAP; Grievance Officer and DPO | SCR-P13-11 | P13 | — |
| **Help** | Help centre 🔒 | Search articles | SCR-P16-43 (`/help`) | P16 | — |
| Help | Contact support | Form with deflection; track by signed link | SCR-P16-43 (`/help/contact`) | P16 | — |
| Help | Complaints about Equator 🔒 | Policy and complaint route (`/rules/complaints-about-equator`) | SCR-P13-07 | P13 | — |
| Help | Grievance Officer 🔒 · Accessibility statement 🔒 · Terms · Privacy · Cookies · Disclaimer | Read; raise grievance | SCR-P13-48 | P13 | — |
| Help | Cookie settings 🔒 | Reopen banner | SCR-P13-49 | P13 | — |

**Footer** keeps the Appendix P §3.0 link groups; the Grievance Officer, DPO, accessibility and legal links are locked (L).

**Renumbering map for Appendix C (D3-47(c)).**

| Appendix C ID (old meaning) | v3.1 ID | Note |
|---|---|---|
| SCR-P13-01, -02, -03, -06, -14 | unchanged | Same meaning in P13 §6 |
| SCR-P13-04 How it works | SCR-P13-40 | — |
| — (mechanism pages, App. P P-21–P-27) | SCR-P13-41 | New allocation |
| — (subtype pages P-10–P-19) | SCR-P13-42 | New allocation |
| — (Become a neutral P-36) | SCR-P13-43 | New allocation |
| — (Pricing P-39) | SCR-P13-20 · -21 · -22 (P13 §6) | *v3.1:* SCR-P13-44 withdrawn (AG.0.5 #12) |
| — (Private ADR Chambers P-34) | SCR-P13-45 | New allocation |
| — (Training P-37) | SCR-P13-46 | New allocation |
| SCR-P13-05 Rules | SCR-P13-07 | P13 §6 meaning |
| SCR-P13-07 Clause generator | SCR-P13-13 | P13 §6 meaning |
| SCR-P13-08 Calculators hub · -09 POSH checker · -10 Grievance SLA check | SCR-P13-12 (tool variants) | — |
| SCR-P13-11 Trust centre · -19 Published outcomes and statistics | SCR-P13-09 | — |
| SCR-P13-12 About | SCR-P13-10 | — |
| SCR-P13-13 Resources and blog | SCR-P13-47 | — |
| SCR-P13-15 Enterprise demo request | SCR-P13-04 (demo form) | — |
| SCR-P13-16 Legal pages | SCR-P13-48 | — |
| SCR-P13-17 Cookie banner | SCR-P13-49 | — |
| SCR-P13-18 International pages | SCR-P13-02 (INT hub) | Merged |
| SCR-P13-21 CMS editor · -22 Claims Register | SCR-P13-16 · SCR-P13-17 | — |
| SCR-P13-23 SEO metadata · -24 Programmatic pages | SCR-P13-51 · SCR-P13-52 | — |
| SCR-P13-25 CRM leads · -26 Referral admin | superseded (X-51; SCR-P17-23) | — |
| SCR-P13-27 → -32 Partner portal screens | SCR-P13-53 → SCR-P13-58 (tabs of SCR-P13-15) | — |

### AG.2.2 Party portal (shell `party`, `/app`)

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Home | Next action; join session; pay; add a representative | SCR-S-D01 | P01 | — |
| (top) | My cases | Filter by status; open Case Desk | SCR-P02-16 list · SCR-P02-93 desk | P02 | — |
| (top) | Start or respond | File a case · Continue a draft · Respond to a notice | SCR-P02-04 · SCR-P02-29 · SCR-P02-07 | P02 | — |
| (top) | Inbox 🔒 | Tasks, messages, updates, deadlines | AG-SCR-01 | P00 | — |
| Case work | Calendar | Sessions, hearings and deadlines across my cases; add to calendar | AG-SCR-23 **New v3.1** | P04 | — |
| Case work | Documents | Requested documents across cases; upload; served on me | AG-SCR-22 **New v3.1** | P02 | — |
| Case work | Signatures | Waiting for my signature; signed | AG-SCR-24 **New v3.1** | P06 | — |
| Case work | Payments | Due, paid, refunds, instalments, receipts | AG-SCR-21 **New v3.1** | P05 | — |
| After the outcome | Next steps (execution, registration) | Choose a professional; share documents with my professional | SCR-P21-28 · SCR-P19-30 · SCR-P19-31 | P21 / P19 | Chooser panel option "Equator panel": `postres.advocate_panel` |
| After the outcome | Compliance with agreed terms | Mark paid; dispute an instalment | SCR-P06-15 · SCR-P06-64 | P06 | Case has compliance tracker |
| Services | Marketplace engagements | Enquiries; proposals; engagement | SCR-P19-06 → SCR-P19-08 | P19 | Marketplace gate; user has an enquiry |
| Account | My representatives | Grant, narrow, revoke | `/settings/representatives` (SCR-P01-25) | P01 | — |
| Account | My data exports | Request export; download | SCR-P21-08 · SCR-P21-09 | P21 | — |
| Account | Help 🔒 | Raise a ticket; my tickets; grievance link | SCR-P16-42 | P16 | — |
| Account | Settings | AG.3 personal settings | SCR-P15-22 | P15 | — |

**Case Desk tabs** (inside a case, ≤ 8 tabs; R-10):

| Tab | Contents | Screens | Phase |
|---|---|---|---|
| Overview | Action inbox for this case, status, clocks, who decides next, free-forum reminder | SCR-P02-93 · SCR-P02-16 | P02 |
| Documents | Folder tree, requests, share dialog, activity | SCR-P02-13 · SCR-P02-61 · SCR-P02-62 | P02 |
| Messages | Case thread, communications timeline | SCR-P07-04 · SCR-P12-14 | P07 |
| Proceedings | Ladder, negotiation, blind bid, filings, consents, applications, adjournment, appeal | SCR-P04-01 · -02 · -03 · -08 · -11 · -18 · -21 | P04 |
| Hearings | Sessions, lobby, room, e-bundle | SCR-P02-85 · SCR-P04-13 · -14 · -15 | P04 |
| Orders and outcome | Orders; heads of terms; settlement editor; signing; e-stamp; execution | SCR-P02-86 · SCR-P02-87 · SCR-P06-02 · -03 · -07 · -09 · -10 · -13 · -14 | P06 |
| Money | Payments and deposits; checkout; escrow; instalments; concession | SCR-P02-88 · SCR-P05-02 → -05 · -09 · -10 | P05 |
| More ▾ | People and representatives (SCR-P02-81) · Papers, applications, notices registers (SCR-P02-82 → -84) · Linked matters (SCR-P02-90) · Appointment participation (SCR-P03-11 · -12 · -14 · -15 · -16) · AI use on this case (SCR-P11-12) · Validate extracted facts (SCR-P11-09) · Case notifications (SCR-P02-91) · Case history statement (SCR-P02-92) · Working copies (SCR-P21-13) · Feedback or complaint about a neutral (SCR-P03-21 · -23) · Withdraw (SCR-P02-19) · Vertical panels (SCR-P08-01 → -15 by vertical) | as listed | P02–P21 |

### AG.2.3 Representative portal (shell `representative`, `/app/counsel`)

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Home | File for client; request authority; join hearing; message case manager | SCR-S-D02 | P01 | — |
| (top) | Matters | Client switcher; filter by due date; open Case Desk with scope badge | SCR-P10-30 · SCR-P02-93 | P10 / P02 | — |
| (top) | Inbox 🔒 | Filings due, offers awaiting client, authority requests | AG-SCR-01 | P00 | — |
| Work | File for a client | Choose authority; client OTP confirmation | SCR-P02-05 | P02 | Authority scope `file` |
| Work | Filings due (7 / 14 / 30 days) | Saved view of Matters | SCR-P10-30 (view `filings_due`) | P10 | — |
| Work | Calendar | Hearings across matters; ICS feed | AG-SCR-23 **New v3.1** | P04 | — |
| Work | Signatures | Instruments awaiting my signature within authority | AG-SCR-24 **New v3.1** | P06 | Authority scope `sign_*` |
| Clients | Authorities | Accept, renounce, expiries | SCR-P01-25 | P01 | — |
| Clients | Enrolment verification | Status; re-verification date | SCR-P01-24 | P01 | — |
| Firm | Firm administration | Members, roles, sub-delegation, firm matters | AG-SCR-25 **New v3.1** | P01 | `firm_admin` |
| Profile | Professional registry record | Fields, consents, distribution log | SCR-P19-34 | P19 | `group.dir.owner_entity_id` set (registry live) |
| Account | Help 🔒 · Settings | — | SCR-P16-42 · SCR-P15-22 | P16 / P15 | — |

The representative shell never shows marketplace sponsorship, ratings, referral rewards or ranking for advocates (NN-34, NN-39); those items do not exist in its registry.

### AG.2.4 Neutral portal (shell `neutral`, mediation and arbitration spaces)

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Today | Join next session; accept or decline offer; mark availability | SCR-S-D03 / SCR-S-D04 (SCR-P03-17) | P01 / P03 | Space |
| (top) | Inbox 🔒 | Offers, drafting due, disclosure renewals, messages | AG-SCR-01 | P00 | — |
| Cases | My cases | Open neutral Case Desk | SCR-P02-94 | P02 | — |
| Cases | Appointment offers | Disclose and accept / decline (countdown) | SCR-P03-13 | P03 | — |
| Cases | Calendar | Sessions, hearings, deadlines; fair-slot finder | AG-SCR-23 · SCR-P04-12 | P04 | — |
| Cases | Drafting | Orders, outcomes and awards in drafting with age | AG-SCR-26 **New v3.1** → SCR-P04-17 · SCR-P06-01 · SCR-P06-05 · SCR-P11-10 | P06 | Award items: `neutral_arbitrator` |
| Cases | Caucus notes | Open sealed notes (author only) | SCR-P04-05 | P04 | Mediation space; author |
| Cases | Mediation and arbitration consoles | Workspace; PO1 builder; hybrid switch; expert determination | SCR-P04-04 · -06 · -07 · -19 · -20 | P04 | Role per mechanism |
| Practice | Availability | Weekly grid; exceptions; capacity cap | SCR-P03-18 | P03 | — |
| Practice | Earnings and payouts | Statements; TDS; payout status | SCR-P03-24 · SCR-P05-06 | P03 / P05 | — |
| Practice | Tax and bank profile | PAN, GST, bank (cooling-off) | SCR-P05-07 | P05 | — |
| Practice | CPD and training | Hours; evidence; courses | SCR-P03-20 · SCR-P10-15 | P03 / P10 | — |
| Practice | Scorecard (process only) | KPIs; feedback aggregates | SCR-P03-19 | P03 | — |
| Profile | Public profile (Equator panel) | Per-field consent; preview | SCR-P03-25 | P03 | — |
| Profile | Marketplace listing (private practice) | Profile, offerings, calendar (out of office pauses new bookings), payouts, reviews; "My onboarding" (SCR-P19-10) until listed *(v3.1)* | SCR-P19-11 → SCR-P19-15 | P19 | Marketplace gate; non-advocate neutral, or `marketplace.advocate_neutrals.listing` ON |
| Profile | Sponsorship | Eligibility, order, invoices | SCR-P19-16 | P19 | `marketplace.paid_placement` ON and `sponsor_eligible()` |
| Profile | My chambers | Switch into a chambers context | AG-SCR-05 | P01 | Holds a chambers membership |
| Account | Help 🔒 · Settings | — | SCR-P16-42 · SCR-P15-22 | P16 / P15 | — |

The Equator panel profile and the marketplace listing are separate groups with separate labels so that a neutral cannot confuse paid visibility with panel status (NN-34).

### AG.2.5 Chambers workspace (shell `chambers`, `/chambers/*`)

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Home | Dashboard `workspace_home` at `/chambers/work`: caseload, clock risk, my tasks, enquiries, approvals; revenue for owner and accounts *(v3.1: renamed from `practice_home`, AG.0.5 #7)* | SCR-P20-29 | P20 | — |
| (top) | Inbox 🔒 | Tasks, G approvals, pay-run approvals, privileged grants | AG-SCR-01 (source `chm`) | P00 / P20 | — |
| Work | Work queues and tasks | Next task; bulk assign; leave-aware reassignment proposals (`/chambers/work/queues`) | SCR-P20-18 | P20 | `chambers_case_manager`, `chambers_staff`, admin |
| Work | Enquiries | Conflict check; convert to matter | SCR-P20-09 | P20 | front desk, admin |
| Work | Matters | Scrutiny, notices, clocks, bundles (tenant-scoped console screens) | SCR-P02-08 · -11 · -12 · -14 · SCR-P02-95 | P02 | `chm.case_access` |
| Work | Calendar | Sessions, rooms, staff leave overlay | AG-SCR-23 | P04 | — |
| Work | Workload | Per team and person (permitted viewers) | SCR-P20-19 | P20 | owner, admin, managers |
| Practice setup | Rules of procedure | Adopt, fork, upload; publish (G) | SCR-P20-12 | P20 | admin; legal approver |
| Practice setup | Fee schedules | Slabs; quote preview (G) | SCR-P05-17 (tenant scope) | P05 | admin; legal approver |
| Practice setup | Templates | Families; locked blocks; language versions | SCR-P20-13 | P20 | admin |
| Practice setup | Numbering, status labels, letterheads | Pattern builder; label map | SCR-P20-14 | P20 | admin |
| Website | Site · Pages · Theme · Domains · People | Edit, review, publish; DNS wizard | SCR-P20-02 → SCR-P20-08 | P20 | admin; owner for domains |
| Website | Marketplace listing | Opt in; offerings; propose a substitution for an `on_hold` engagement (same chambers, fresh conflict check and acceptance; FR-P20-57) *(v3.1)* | SCR-P19-11 · SCR-P19-12 | P19 | `tenant.chm.marketplace.opt_in`; Marketplace gate |
| People and HR | Staff and roles · Delegations | Invite; privileged-grant approval; delegate | SCR-P20-16 · SCR-P20-17 | P20 | owner, admin |
| People and HR | HR home · Staff records · Leave and attendance | Compliance wizard; records; approvals | SCR-P20-20 → SCR-P20-22 | P20 | `chambers_hr`, owner |
| People and HR | Payroll · Disbursal · Consultants | Run, approve, disburse, reconcile; TDS | SCR-P20-23 → SCR-P20-25 | P20 | HR (maker), accounts (checker), owner |
| People and HR | Performance and policies | Goals, reviews, acknowledgements | SCR-P20-26 | P20 | — |
| Money | Invoicing profiles | GSTIN/FY series, SAC map, e-invoice | SCR-P20-15 | P20 | `chambers_accounts`, owner |
| Money | Revenue and receivables | Dashboards `revenue`, `receivables` | SCR-P20-29 | P20 | owner, accounts |
| Money | Equator subscription | Plan, invoices, usage | SCR-P05-19 → SCR-P05-28 | P05 | owner |
| Oversight | Controls | Exceptions, single-person log, bank changes | SCR-P20-28 | P20 | owner, external checker |
| Oversight | Reports | Scheduled XLSX + PDF reports (§W.7) | SCR-P20-29 (reports tab) | P20 | per report |
| Oversight | Export and offboarding | Export scopes; offboarding wizard | SCR-P20-30 | P20 | owner |
| Me | My work and pay (ESS) | Check-in, leave, payslips, declarations | SCR-P20-27 | P20 | `employee` |
| Account | Help 🔒 · Settings | Settings catalogue (§W.8) | SCR-P16-42 · SCR-P20-10 | P16 / P20 | per tier |

Tenant neutrals see the neutral menu (AG.2.4) in tenant branding plus "Work → Calendar" and "Me".

### AG.2.6 Enterprise console, GRM desk and POSH IC workspace (shell `enterprise`)

**Enterprise console (`/app/enterprise`).**

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Dashboard | New bulk batch; file a case; approve offer within authority; download MIS | SCR-S-D08 → vertical desk SCR-P09-07 (FIN) · -08 (INS) · -09 (WRK) · -10 (listed) | P01 / P09 | Vertical of tenant |
| (top) | Inbox 🔒 | Offer approvals, bulk batch validation, SLA breaches | AG-SCR-01 | P00 | — |
| Cases | All cases | Saved views; bulk reminder (AG.7.3) | SCR-P02-16 list (enterprise view) | P02 | — |
| Cases | File one case | Clause selector; GRO block (FIN) | SCR-P02-06 | P02 | `enterprise_operator` |
| Cases | Bulk intake | Upload; validate; commit or abort | SCR-P09-06 | P09 | `enterprise_operator` |
| Cases | Settlement compliance | Instalment grid; default escalation | SCR-P06-15 · SCR-P06-64 | P06 | — |
| Cases | Campaigns | Voice and WhatsApp within NN-12 window | SCR-P07-09 | P07 | Entitlement `campaigns`; contact policy approved |
| Portfolio | Clause library and coverage | Adopt version; coverage % | SCR-P09-04 | P09 | `enterprise_admin` |
| Portfolio | Vertical dashboards and MIS | Widget packs; board export | SCR-P08-20 | P08 | — |
| Services | Procurement (ancillary services) | Vendor panels, RFQs, SLAs | SCR-P19-32 | P19 | Marketplace gate; entitlement `procurement` |
| Services | Professional panel register | Registers, invitations, engagements | SCR-P19-33 | P19 | `panel_register_*` |
| Integrations | API keys · Webhooks | Create key (shown once); replay deliveries | SCR-P09-02 · SCR-P09-03 | P09 | `enterprise_admin` |
| Integrations | Connectors and mappings | Enable wizard; mapping set; system of record | SCR-P21-05 → SCR-P21-07 | P21 | `enterprise_admin` |
| Admin | SLA policies and agreements | Locked statutory rows | SCR-P09-11 | P09 | `enterprise_admin`, `dpo` |
| Admin | People and SSO | Members; SSO test | SCR-P01-44 · SCR-P01-30 | P01 | `enterprise_admin` |
| Admin | Billing | Plan, invoices, contract, usage | SCR-P05-19 → SCR-P05-33 | P05 | billing admin |
| Admin | Help 🔒 · Settings | — | SCR-P16-42 · SCR-P15-01 | P16 / P15 | — |

No item in this shell lists neutrals with select, rank or veto controls (Appendix C §B.8; NN-03); the registry has no such item and CI test `NAV_NO_NEUTRAL_SELECTION_ENTERPRISE` asserts it.

**GRM desk (`/app/grm`).**

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Desk inbox | Next ticket; filter by regulator clock (T-7, T-3, breached) | SCR-S-D09 · SCR-P09-12 | P01 / P09 | `grievance_officer`, `internal_ombudsman` |
| (top) | Ticket | Respond from template; route to IO; offer ODR | SCR-P09-13 | P09 | — |
| Desk | Escalations | Offered / accepted escalations; IO referrals | SCR-P09-12 (view `escalations`) | P09 | — |
| Desk | Reports and committees | Regulator MIS exports; GRC/SGRC registry | SCR-P09-15 | P09 | GRO, admins |
| Setup | Complainant portal | White-label portal preview; categories | SCR-P09-14 | P09 | `enterprise_admin` |
| Setup | GRO public profile | Contact card | SCR-P01-31 | P01 | GRO |
| Account | Help 🔒 · Settings | — | SCR-P16-42 · SCR-P15-01 | P16 / P15 | — |

**POSH IC workspace (`/app/posh`, sealed sub-shell).** No global search, no palette search over records (palette offers navigation commands only), no analytics events, no badges with categories, step-up on entry, 10-minute idle (NN-07; Appendix C §A.4).

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Complaints | Open complaint; 90-day clock; inquiry; report | SCR-P09-17 | P09 | IC roles |
| (top) | Constitution | Validator (≥ one-half women; external member) | SCR-P09-16 | P09 | `ic_presiding_officer`, `enterprise_admin` |
| (top) | External members and reports | Engage; s.21 / s.22 reports | SCR-P09-18 | P09 | presiding officer |
| (top) | My IC onboarding | Undertaking; conflicts | SCR-P01-32 | P01 | IC roles |
| (top) | QuickExit 🔒 | — | — | P00 | always |

### AG.2.7 Case-services and registry console (shell `console`)

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Queue | Next in queue; assign clock owner; compose notice; schedule session | SCR-S-D05 (SCR-P10-31) | P01 / P10 | `case_manager` |
| (top) | Inbox 🔒 | Clock alerts, service failures, handoffs, approvals | AG-SCR-01 | P00 | — |
| Case management | Scrutiny | Accept, deficient, signpost, reject | SCR-P02-08 | P02 | `case_manager`, `registrar` |
| Case management | Clocks cockpit | Assign owner; resolve blocking tasks | SCR-P02-11 | P02 | — |
| Case management | Notices and service | Compose; deemed-service decision; speed-post batch | SCR-P02-12 · SCR-P07-05 · SCR-P07-14 | P02 / P07 | — |
| Case management | Hearings logistics | Schedule; attendance; interpreters; INT scheduler | SCR-P04-12 · SCR-P04-16 · SCR-P08-19 | P04 / P08 | — |
| Case management | Bundles and evidence | Build bundle; s.63(4) certificate | SCR-P02-14 · SCR-P02-15 | P02 | — |
| Case management | Linked matters | Consolidation wizard (maker-checker) | SCR-P02-18 | P02 | — |
| Case management | Signing and closure | Envelope tracker; closure checklist | SCR-P06-08 · SCR-P06-17 | P06 | — |
| Case management | Registry notes | Generate and sign | SCR-P02-89 | P02 | — |
| Case management | Handoffs | Live transfers; callbacks | SCR-P07-13 | P07 | `case_manager`, `support_agent`, `safeguarding_lead` |
| Registrar | Registrar desk | Run allocation; build agenda; certified copy; approve break-glass | SCR-S-D06 | P01 | `registrar`, deputy |
| Registrar | Appointments | Allocation run (counts only) | SCR-P03-10 | P03 | `registrar` |
| Registrar | Challenges · Challenge windows | Timeliness; decision drafting; s.34 / s.28 windows | SCR-P04-09 · SCR-P06-16 | P04 / P06 | `registrar`, committee |
| Registrar | Certified copies · Sealed-award vault | Issue; release control | SCR-P06-11 · SCR-P06-19 | P06 | `registrar` |
| Registrar | Compliance cockpit | Unowned clocks; closure guards | SCR-P14-01 | P14 | `registrar`, `quality_officer` |
| Panel | Applications and verification | Verify per credential | SCR-P03-05 | P03 | `panel_manager` |
| Panel | Assessments · Committee room | Rubric; agenda, recusal, vote | SCR-P03-06 · SCR-P03-07 | P03 | assessor, committee |
| Panel | Panel health · Allocation policies | Shortages; dry run on last 500 cases | SCR-P03-08 · SCR-P03-09 | P03 | `panel_manager`, `institution_admin` |
| Quality | Award scrutiny · Publication review | Return to tribunal; redaction checklist | SCR-P06-06 · SCR-P06-18 | P06 | `quality_officer` |
| Quality | Voice QA · Quality dashboard | Score calls; panel quality | SCR-P07-11 · SCR-P03-19 (admin view) | P07 / P03 | `quality_officer` |
| Escrow | Escrow console | Dual-control release; reconciliation | SCR-P05-08 | P05 | `escrow_officer` |
| Safeguarding | Screenings | Screen before joint sessions | SCR-P04-22 | P04 | `safeguarding_lead` |
| Reports | Vertical MIS | Per-vertical outcomes | SCR-P08-16 | P08 | `registrar`, `institution_admin` |
| Account | Help 🔒 · Settings | — | SCR-P16-42 · SCR-P15-22 | P16 / P15 | — |

**Institution administration** (tenant scope, rendered in the `admin` shell for `institution_admin`): Dashboard (SCR-P10-32) · People and memberships (SCR-P01-44) · Verification queue (SCR-P01-45) · Privacy desk (SCR-P01-46) · Panels and allocation (SCR-P03-09) · Rules and legal (SCR-P15-10 → SCR-P15-12) · Communications (SCR-P07-01 → -03, -07, -08, -12, -19) · Finance (SCR-P05-13 → -16, -18) · AI controls (SCR-P11-05, -16) · Lok Adalat sittings (SCR-P09-20, LSA tenants) · Settings (SCR-P15-01).

### AG.2.8 Operations Platform (shell `ops`, `ops.equatorresolution.in`)

The **department rail** (left, icons with labels) lists only the departments in which the user holds a role; the side nav shows that department's items. A user with one department sees no rail. Group-company staff see a **company switcher** in the context chip (AG.1.3).

| Group (department) | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Home — my work | Next task; tickets; approvals | SCR-P16-01 | P16 | all ops |
| (top) | Inbox 🔒 | All sources (AG.4) | AG-SCR-01 | P00 | all ops |
| (top) | Tasks | Queues; cross-department requests; load view | SCR-P16-04 | P16 | all ops |
| (top) | Hand-offs *(v3.1)* | Accept or reject (reason) lead-to-cash hand-offs; checklist; breach chips (`/handoffs`) | SCR-P16-44 | P16 | all hand-off owners |
| Leadership | Leadership cockpit | Approve; open escalation; publish group dashboard; export board pack | SCR-P16-02 | P16 | `ops_director`, heads |
| Leadership | ROI dashboards (department/team) | Explain panel; cohort guard | SCR-P18-24 | P18 | `ops_director`, heads, finance |
| Leadership | Weekly management review pack *(v3.1)* | Drill down; edit action log; approve to distribute (`/reports/weekly`) | SCR-P16-45 | P16 | leadership, heads; approval `ops_director` |
| Sales and BD | Leads · Lead detail | Bulk assign; convert | SCR-P16-05 · SCR-P16-06 | P16 | sales |
| Sales and BD | Accounts · Contacts | 360° view; preferences (read) | SCR-P16-07 → SCR-P16-09 | P16 | sales, CS, support |
| Sales and BD | Pipeline · Opportunities · Quotes | Move stage (gates); quote; request approval | SCR-P16-10 → SCR-P16-12 | P16 | sales |
| Sales and BD | Segments · Duplicates · Imports | Build segment; merge; import with dry run | SCR-P16-13 → SCR-P16-15 | P16 | sales, `crm.merge`, `ops_manager` |
| Sales and BD | Partners (CRM) | Partner records; attribution | SCR-P16-17 | P16 | partnerships |
| Onboarding | Projects board · Project · Sign-off | New project; book training; migration dry run; request sign-off | SCR-P16-18 → SCR-P16-20 | P16 | onboarding, CSM |
| Customer success | Success home · Account health · QBRs | Start playbook; schedule QBR; renewal | SCR-P16-21 → SCR-P16-23 | P16 | CSM |
| Support | Support queue · Ticket | Next ticket; macro; escalate; convert to grievance | SCR-P16-24 · SCR-P16-25 | P16 | support |
| Grievances | Grievance desk · Grievance | Acknowledge; final reply; appeal | SCR-P16-27 · SCR-P16-28 | P16 | `grievance_officer`; `escalation_reviewer` |
| Knowledge | Knowledge base | Write; legal review; publish to CMS | SCR-P16-29 | P16 | all (write by bundle) |
| Case services | Service delivery (metadata) | Open in case console (link-out); service request | SCR-P16-30 | P16 | `case_services_lead` |
| Finance ops | Receivables and dunning | Collections task; route refund to P05 | SCR-P16-31 | P16 | `finance_ops` |
| Finance ops | Marketplace payouts · Tax engine | Batch review; TCS ledger | SCR-P19-26 · SCR-P19-27 | P19 | `finance_ops`, `accounts_checker` |
| Training ops | Training operations | Schedule session; record attendance | SCR-P16-32 | P16 | training bundle |
| Marketplace ops | Marketplace operations queue | Review listing; suspend (maker) | SCR-P16-33 · SCR-P19-20 | P16 / P19 | `marketplace_*` |
| Marketplace ops | Onboarding pipeline *(v3.1)* | Deadline-aware queue (SLA due, then progress score); bulk assign; request information; stuck-step chips | SCR-P19-19 | P19 | `provider_verifier`, `marketplace_moderator`, `marketplace_manager` |
| Marketplace ops | Verification · Categories · Ranking policy · Enforcement · Sponsorship and ads · Transparency audit · Marketplace grievances | Two-person verification; publish ranking policy; panel decisions | SCR-P19-21 → SCR-P19-25 · SCR-P19-28 · SCR-P19-29 | P19 | as P19 §6 (sponsorship: `marketplace.paid_placement`) |
| Marketplace ops | Registry administration | Verification, freshness, GDSA gates | SCR-P19-35 | P19 | `registry_steward`, `registry_verifier` |
| Marketing | Marketing home · OKRs · Segments · Messaging houses | — | SCR-P17-01 → SCR-P17-04 | P17 | marketing roles |
| Marketing | Campaigns · Calendar · Content · Reviews · Publications | Brief; schedule; review; record evidence; on the calendar (SCR-P17-07) conflict badges CC-01–CC-10 with one-click resolutions and multi-select bulk reschedule, hold, release and reassign (PAT-03 preview) *(v3.1)* | SCR-P17-05 → SCR-P17-10 | P17 | marketing roles |
| Marketing | Social accounts · Engagement inbox | Triage; route; safety escalation | SCR-P17-11 · SCR-P17-12 | P17 | social, PR |
| Marketing | Brand assets · Boilerplates | Rights badges; co-branding approvals | SCR-P17-13 → SCR-P17-15 | P17 | designer, marketing |
| Marketing | Audiences · Sends · Consent health · Deliverability | Compose; test; request send approval | SCR-P17-16 → SCR-P17-19 | P17 | marketing, DPO, IT admin |
| Marketing | Lead magnets · Sequences · Events · Referrals | Build; version; kill switch | SCR-P17-20 → SCR-P17-23 | P17 | marketing, partnerships |
| Marketing | PR · Crisis room | Release; embargo; crisis statements | SCR-P17-24 · SCR-P17-25 | P17 | PR, crisis team |
| Marketing | Partnerships (MoUs) · SEO · Analytics | MoU checklist; briefs; attribution | SCR-P17-27 → SCR-P17-29 | P17 | partnerships, SEO, leadership |
| Automations | Automations · Builder | Pause; simulate; publish (approval) | SCR-P16-34 · SCR-P16-35 | P16 | authors, publishers |
| HR and admin | Entities · Structure · Positions · Headcount | First-run D3-06 wizard; effective-dated changes | SCR-P18-01 → SCR-P18-04 | P18 | `group_admin`, HR, heads |
| HR and admin | Requisitions · Recruitment · Offers · Pre-joining · Onboarding | Approve requisition; offer builder | SCR-P18-05 · SCR-P18-06 · SCR-P18-08 → SCR-P18-10 | P18 | HR, heads, interviewers |
| HR and admin | Employees · Employee 360 · Movements · Secondments · Exits | Change forms with impact preview | SCR-P18-11 → SCR-P18-15 | P18 | HR, managers (limited), `group_hr` |
| HR and admin | Probations *(v3.1)* | Reviews ending in 60 days; overdue; outcome (`/hr/probations`) | SCR-P18-45 | P18 | HR, managers, heads |
| HR and admin | Time: rosters · regularisations · overtime | Publish roster; bulk approve | SCR-P18-18 → SCR-P18-20 | P18 | team leads, managers, HR |
| HR and admin | Scorecards · Capacity · Performance · Calibration · Increments | Cycle tasks; calibration (n ≥ 5) | SCR-P18-22 · -23 · -33 → -35 | P18 | managers, HR, committee |
| HR and admin | Leave · Leave planner · Learning | Approvals; team coverage against the minimum on duty (`/leave/planner`, *v3.1*); mandatory modules | SCR-P18-25 · SCR-P18-46 · SCR-P18-44 | P18 | managers, HR |
| Payroll | Structures · Pay runs · Statutory outputs · F&F | Run cockpit; approve (checker); bank file | SCR-P18-28 → SCR-P18-30 · SCR-P18-32 | P18 | `payroll_maker`, `payroll_checker`, finance |
| Controls | Authority matrix · SoD · Payees and bank changes · Spend · Exceptions · Declarations | Simulate authority; cooling timers | SCR-P18-37 → SCR-P18-42 | P18 | CS, finance, security lead, compliance |
| Controls | Anomaly rules *(v3.1)* | Shadow mode; promote a rule (maker-checker) (`/controls/anomaly-rules`) | SCR-P18-47 | P18 | `internal_auditor`, `finance_controller` |
| Technology | Workspace provisioning (JML) | Queue; manual fallback | SCR-P18-16 | P18 | `it_admin` |
| Technology | Workspace connections · Capabilities · Integrations health · Connectors · Migrations | Test connection; rehearsal | SCR-P21-01 → SCR-P21-04 · SCR-P16-36 · SCR-P16-37 | P21 / P16 | `it_admin`, DPO, `ops_manager` |
| Technology | Engineering governance (overview · CAB · change records · releases · vulnerabilities · backup and DR · VAPT · production access · keys · capacity) | Approve change (checker); freeze window; approve the daily standard train (two-person, SCR-P21-AE02); open the restore-assurance report (SCR-P21-AE06) *(v3.1)* | SCR-P21-AE01 → AE08 · AE10 → AE12 | P21 | engineering roles per App. AE §AE.1.1 |
| Legal and compliance | Regulatory watch · Rule packs | Triage; adopt; propose | SCR-P15-12 · SCR-P15-10 · SCR-P15-11 | P15 | `legal_ops`, `legal_reviewer`, `compliance_officer` |
| Legal and compliance | Review queue (KB, articles, complaints, contracts) | Saved view of Work Inbox source `legal_review` | AG-SCR-01 (view) | P00 | `legal_reviewer` |
| Revenue | Revenue Stream Registry | Stream versions; kill switch (maker) | SCR-P19-AB01 → AB10 | P19 | `revenue_manager`, `finance_controller` |
| Revenue | Viability dashboard and proposals *(v3.1)* | RAG by stream; open a proposal (decided in the Work Inbox, source `rev`); defer once | SCR-P19-AB09 | P19 | `revenue_manager`, CFO; Board via the CFO |
| Group | Group overview · Grants · Approvals · Walls · Agreements · Charges · Secondments · Shared artefacts · Consolidated pack | Request grant; approve; recharge run | SCR-P21-20 → SCR-P21-27 · SCR-P21-29 | P21 | `group_admin`, CS, DPO, compliance, accounts |
| Group | Assignment requests *(v3.1)* | Request, accept or decline cross-company work; SLA chip (`/group/assignment-requests`) | SCR-P21-30 | P21 | host `department_head`, employing HR, line manager |
| Internal audit | Audit workspace · Workforce drill-down · Audit plan and findings | Sample; request evidence; export (watermarked) | SCR-P16-41 · SCR-P18-43 (`/audit/workforce`) · SCR-P21-AE08 | P16 / P18 / P21 | `internal_auditor` |
| (bottom) | Reports · Exports · Imports | Schedule; request export with pre-flight estimate and presets (SCR-P21-08); progress and resumable download; verify a package (`/exports/verify`, SCR-P21-31); "Department exports" saved view; import with mapping preview *(v3.1)* | SCR-P16-38 · SCR-P21-09 · SCR-P21-11 | P16 / P21 | by role |
| (bottom) | Help 🔒 · Settings | Operations settings (P15 shell) | AG-SCR-12 · SCR-P16-39 | P16 | by tier |

### AG.2.9 HR and self-service (shell `selfservice`, `ops…/me`; chambers staff use SCR-P20-27)

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Me — home | Clock in; request leave; latest payslip; tasks | AG-SCR-20 **New v3.1** (ID for FR-P18-63 hub) | P18 | `employee` |
| (top) | Inbox 🔒 | My approvals (if approver), acknowledgements, reminders | AG-SCR-01 | P00 | — |
| Time | Today (clock in/out) · Rosters (own) | One-tap clock; confirm session suggestions | SCR-P18-17 | P18 | — |
| Time | Regularisation requests | Raise within window | SCR-P18-19 (own view) | P18 | — |
| Leave | Leave and balances | Request; cancel; calendar | SCR-P18-25 | P18 | — |
| Pay | Payslips and tax | Download (EN/HI); regime election; declarations and proofs; Form 130 | SCR-P18-31 | P18 | — |
| Pay | Claims and expenses | New claim with receipt capture | SCR-P18-40 (own) | P18 | — |
| Growth | Goals, check-ins and reviews · Learning | Acknowledge; appeal; enrol | SCR-P18-33 · SCR-P18-44 | P18 | — |
| Growth | My work summary · My contribution | Explain panel; dispute | SCR-P18-22 (own) · SCR-P17-26 | P18 / P17 | contribution: marketing roles |
| Me | My data and disputes 🔒 | See every record, source and viewer; dispute (NN-35) | SCR-P18-21 | P18 | — |
| Me | Declarations (COI, gifts) | Annual wizard | SCR-P18-42 (own) | P18 | — |
| Me | My cross-company grants | Request; countdown | SCR-P21-21 | P21 | — |
| Me | My exports | Own-data export | SCR-P21-08 · SCR-P21-09 | P21 | — |
| Account | Help 🔒 · Settings (personal) | — | AG-SCR-12 · SCR-P15-22 | P16 / P15 | — |

### AG.2.10 Platform super-admin console (shell `admin`, `admin.equatorresolution.in`)

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Overview | Request elevation; provision tenant; flip release flag (maker); open incident | SCR-S-D12 · SCR-P00-01 | P01 / P00 | `platform_admin` |
| (top) | Inbox 🔒 | Flag proposals, change requests, break-glass reviews, support-session requests | AG-SCR-01 | P00 | — |
| Tenancy | Tenants · Tenant editor · Domains · Branding | Mechanism matrix; contrast check | SCR-P00-02 → SCR-P00-05 | P00 | `platform_admin` |
| Configuration | Feature flags (legal and release) | Propose change → change request | SCR-P00-06 | P00 | `platform_admin`, `legal_reviewer`, `registrar` |
| Configuration | Settings registry | Definitions, tiers, owners, usage | SCR-P15-23 | P15 | product owner, CTO, auditors |
| Configuration | Navigation registry | Menu versions; preview as role; publish | AG-SCR-07 (platform mode) | P15 | `platform_admin` (maker), product owner (checker) |
| Rules and legal | Studio home · Objects · Draft · Review · Preview runner | Maker-checker | SCR-P00-07 → SCR-P00-11 (re-skinned in SCR-P15-10/-11, X-43) | P00 / P15 | per role |
| Rules and legal | Legal Rules Register | Status chips; next review | SCR-P00-12 · SCR-P00-13 | P00 | `legal_reviewer`, `registrar`, `dpo`, `auditor` |
| Audit | Audit explorer · Chain verification · Evidence ledger | Verify chain | SCR-P00-14 → SCR-P00-16 | P00 | `platform_admin`, `dpo`, `auditor` |
| Platform operations | Events · Webhook inbox · Provider routing · Jobs · Environment | DLQ replay; circuit state | SCR-P00-17 → SCR-P00-21 | P00 | `platform_admin`, `support_agent` |
| Platform operations | SLOs · Incidents | Burn rate; regulatory clocks | SCR-P14-02 · SCR-P14-03 | P14 | SRE, incident commander |
| Platform operations | Connectors (government/ecosystem) · DLT registry | Last sync; expiry alerts | SCR-P09-19 · SCR-P07-16 | P09 / P07 | `platform_admin` |
| Access | Elevation (JIT) | Time-boxed privileges | SCR-P01-37 | P01 | `platform_admin` |
| Access | Support sessions | Sessions granted by tenants (≤ 72 h; D3-14) | SCR-P15-09 (platform view) | P15 | `platform_admin` |
| Privacy | Privacy desk (DPO dashboard) · DSR · RoPA/DPIA | Assign DSR; start breach workflow | SCR-S-D13 · SCR-P14-04 · SCR-P14-05 | P01 / P14 | `dpo` |
| AI governance | Console · Prompts · Models · Evals · Kill switches · Incidents · Red team · Corpora · Monitoring | Gate status; signed eval reports | SCR-P11-01 → SCR-P11-08 · SCR-P11-15 | P11 | `quality_officer`, `platform_admin`, `auditor` |
| Website and content | CMS · Claims Register · SEO metadata · Programmatic pages | Legal-review workflow | SCR-P13-16 · SCR-P13-17 · SCR-P13-51 · SCR-P13-52 | P13 | CMS bundles, claims owner |
| Go-live | Launch readiness · Migration · UAT · Security findings | Sign-offs; waivers | SCR-P14-06 → SCR-P14-09 | P14 | leads, migration engineer, UAT lead |
| (bottom) | Help 🔒 · Settings | — | AG-SCR-12 · SCR-P15-01 | P16 / P15 | — |

Every admin page shows the elevation banner with countdown when elevated, and the tenant banner "Support session for {tenant} until {time}" when acting inside a support session.

### AG.2.11 Auditor workspace (shell `assurance`)

| Group | Item | Key actions | Screen | Phase | Gate |
|---|---|---|---|---|---|
| (top) | Engagement home | Grant scope, expiry countdown, PBC status | SCR-P21-AE09 · SCR-S-D14 | P21 / P01 | `auditor` (engagement grant) |
| Evidence | Control library · Evidence catalogue | Filter by control; view artefact hash | SCR-P21-AE09 (tabs `controls`, `evidence`) | P21 | — |
| Evidence | Change records and approvals · Releases | Read | SCR-P21-AE03 · AE04 (read) | P21 | — |
| Evidence | Patch and VAPT trackers · Backup and restore results | Read | SCR-P21-AE05 · AE06 · AE07 (read) | P21 | — |
| Evidence | Access reviews · Policies | Read | SCR-P21-AE09 (tabs) | P21 | — |
| Records | Ledger audit-trail reports · Chain verifier | Run `audit.verify_chain()`; download offline verifier | SCR-P21-AE09 (tab `ledgers`) · SCR-P00-15 (read) | P21 / P00 | — |
| Records | Samples | Select sample → redacted rendition | SCR-P21-AE09 (tab `samples`) | P21 | DPO approval for unredacted (≤ 7 days) |
| Requests | PBC list · Comments | Request evidence; comment | SCR-P21-AE09 (tab `requests`) | P21 | — |
| Requests | Findings tracker | Management responses (read) | SCR-P21-AE08 (read) | P21 | — |
| Requests | Evidence export packs | Request pack (watermarked) | SCR-P21-AE09 (§AE.8.4) | P21 | — |
| (bottom) | Help 🔒 | — | AG-SCR-12 | P16 | — |

No item reaches case content, sealed stores, caucus notes or raw personal data (Appendix AE §AE.8.3(3)); every page carries the watermark.

### AG.2.12 Partner and committee portals (brief)

- **Partners (`/partners`):** Dashboard (SCR-S-D11 · SCR-P13-53) · Referral links and codes (SCR-P13-54) · Co-branded pages (SCR-P13-55) · Clause adoptions (SCR-P13-56) · Statements (SCR-P13-57; reward items absent for professional-class partners, X-54/X-62) · Resources (SCR-P13-58) · Help 🔒 · Settings.
- **Committee (`/committee`):** Home (SCR-S-D07) · Papers and votes (SCR-P03-07) · Challenges assigned (SCR-P04-09, committee view) · Help 🔒. No search over papers outside the meeting scope.

### AG.2.13 Mobile tab bars per persona (P12 governs implementation)

**Rule.** A tab bar has **at most five slots**. When a persona has more than five top destinations, slot 5 is **More**, which opens a sheet (AG-SCR-14) listing the remaining items of that persona's menu in registry order, plus Settings, Help 🔒, the space switcher and Sign out. Tabs show icon **and** text label; badges follow R-6. The user may reorder slots 1–4 from the More sheet ("Edit tabs"); Home/Today stays in slot 1 (L) and Inbox, where present, cannot be removed (L).

| Persona (space) | Slot 1 | Slot 2 | Slot 3 | Slot 4 | Slot 5 | More sheet (default order) |
|---|---|---|---|---|---|---|
| Party (`party`) | Home (SCR-P12-04) | Cases (SCR-P12-05) | Inbox (AG-SCR-01; replaces SCR-P07-17 tab) | Pay (SCR-P12-13 list = AG-SCR-21) | More | Calendar · Documents · Signatures · Next steps · My representatives · Exports · Privacy (SCR-P12-21) · Settings · Help |
| Representative (`party`, representative mode) | Home | Matters | Inbox | Calendar | More | File for a client · Authorities · Signatures · Firm · Settings · Help |
| Neutral (`neutral`) | Today (SCR-P12-15) | Cases | Calendar | Inbox | More | Offers (SCR-P12-16) · Availability (SCR-P12-17) · Earnings · CPD · Drafting (read and sign only) · My chambers · Settings · Help |
| Case manager (staff tab in `neutral` space) | Queue | Clocks | Inbox | Calendar | More | Handoffs · Notices (read) · Settings · Help |
| GRO / internal ombudsman (`enterprise`) | Queue (SCR-P12-18) | Escalations | Inbox | Insights (SCR-P12-20) | More | Reports (read) · Settings · Help |
| Enterprise admin / operator (`enterprise`) | Home | Approvals (Inbox filter `approvals`) | Cases | Insights | More | Bulk batches (status only) · Compliance · Settings · Help |
| Chambers case manager / staff (`chambers`) | Work (FR-P12-V3-W02) | Calendar | Inbox | Me (FR-P12-V3-W01) | More | Enquiries · Settings · Help |
| Chambers owner (`chambers`) | Home | Approvals (FR-P12-V3-W03) | Work | Me | More | Reports (read) · Controls (read) · Settings · Help |
| Employee ESS (`employee`) | Today (SCR-P18-M01) | Leave (SCR-P18-M02) | Pay (SCR-P18-M04) | Inbox (incl. SCR-P18-M03 approvals) | More | Claims (SCR-P18-M05) · Goals (SCR-P18-M07) · My data (SCR-P18-M06) · Settings · Help |
| Ops reviewer / social executive (`ops-approvals`) | Approvals (SCR-P17-31 approvals) | Triage (SCR-P17-31 inbox) | Evidence (SCR-P17-31 evidence) | Inbox | More | Settings · Help |

**Operations Platform on mobile** *(v3.1)*: the only native EOP space is `ops-approvals` above (the three SCR-P17-31 flows plus Work Inbox approvals under the AG.4.3 rules and the web-only money threshold of FR-P12-V31-AG02); every other EOP screen stays responsive web, consistent with Appendix X §X.2.1.

IC roles receive content-free notifications only; the sealed workspace stays web-only (Appendix C §C.3). A user with several spaces switches with the avatar (top-left); the switcher behaves as AG.1.3.

### AG.2.14 Register of new screens proposed by this appendix

| ID | Screen | Route(s) | Shells | Owning phase | Purpose |
|---|---|---|---|---|---|
| AG-SCR-01 | Work Inbox | `/inbox` (each app) | all authenticated | P00 | Unified tasks, approvals, mentions, messages, deadlines, updates (AG.4); supersedes the SCR-P07-17 list UI (data source kept) |
| AG-SCR-02 | Inbox item panel | `/inbox/{itemId}` (drawer) | all | P00 | Generic item detail with the owning engine's decision component embedded (AG.4.3) |
| AG-SCR-03 | Command palette | overlay (`Ctrl/Cmd+K`) | all authenticated except POSH record search | P00 | Commands, navigation, recent items (AG.5.4) |
| AG-SCR-04 | Search results | `/search?q=` | all authenticated except POSH | P00 | Permission-trimmed results by object type (AG.5) |
| AG-SCR-05 | Context switcher | overlay; extends SCR-P01-38 | all | P01 | Organisation, entity, role, chambers and client switching (AG.1.3) |
| AG-SCR-06 | Away and delegation | `/settings/me/away` | all professional and workforce shells | P01 | Out-of-office, inbox delegation, approval delegation within S §6.4 limits (AG.4.5) |
| AG-SCR-07 | Navigation and terminology editor | `/settings/navigation`; admin platform mode | tenant admin; platform | P15 | Menu overrides, terminology, preview-as-role, tours (AG.8) |
| AG-SCR-08 | Dashboard editor and widget gallery | `/settings/dashboards` and in-place "Customise" | all with dashboards | P15 | Layout, widget picker within the role's catalogue (AG.6.3) |
| AG-SCR-09 | Saved views manager | `/settings/me/views` | all | P15 | Own and shared views, defaults, sharing scope (AG.5.6) |
| AG-SCR-10 | Getting started (checklists and tours) | `/getting-started` | all | P15 | Persona and tenant onboarding checklists (AG.8.4) |
| AG-SCR-11 | Keyboard shortcuts | overlay (`?`) and `/settings/me/shortcuts` | all authenticated | P00 | Shortcut reference and remapping (AG.5.5) |
| AG-SCR-12 | Help panel | right drawer (`F1` / Help) | all | P16 | Contextual KB articles, contact support, what's new (AG.8.5) |
| AG-SCR-13 | Public mega-menu and mobile drawer | header component | `public` | P13 | AG.2.1 |
| AG-SCR-14 | Mobile More sheet and tab editor | native sheet | mobile spaces | P12 | AG.2.13 |
| AG-SCR-15 | Navigation and usability analytics | `ops…/reports/navigation` | `ops` (product, CS leads) | P16 | AG.9.3–AG.9.4 dashboards |
| AG-SCR-16 | What's new | Help panel tab; `/whats-new` | all | P00 | Customer release notes (App. AE §AE.4.8) by shell and role |
| AG-SCR-17 | Request access | `/access/request?route=` (from 403) | all authenticated | P01 | Access request to the tenant admin's inbox |
| AG-SCR-18 | System pages v3.1 | 403 / 404 / 410 / 429 / 500 / maintenance | all | P00 | Extends SCR-P00-23 with next-step guidance and trace ID |
| AG-SCR-19 | Bulk job monitor | `/jobs` (each app) | staff, enterprise, ops | P00 | Bulk actions with preview, progress, undo window (AG.7.3) |
| AG-SCR-20 | Employee self-service home | `ops…/me` | `selfservice` | P18 | ID for the FR-P18-63 hub |
| AG-SCR-21 | Payments (all my cases) | `/app/payments` | `party` | P05 | Due, paid, refunds, instalments across cases |
| AG-SCR-22 | Documents (all my cases) | `/app/documents` | `party` | P02 | Requested, served on me, my filings across cases (L `core.saved_views` defaults) |
| AG-SCR-23 | Calendar (my sessions and deadlines) | `/app/calendar`, `/app/counsel/calendar`, `/app/neutral/calendar`, `/console/calendar`, `/chambers/work/calendar` | party, representative, neutral, console, chambers | P04 | Cross-case agenda with time-zone handling (AG.7.7) |
| AG-SCR-24 | Signatures (all) | `/app/signatures` and representative equivalent | party, representative | P06 | Waiting for me, waiting for others, signed |
| AG-SCR-25 | Firm administration | `/app/counsel/firm` | `representative` | P01 | Firm members, roles, sub-delegation (S §4.6) |
| AG-SCR-26 | Drafting queue | `/app/neutral/drafting` | `neutral` | P06 | Orders and awards in drafting with age and s.29A context |
| AG-SCR-27 | Undo and activity tray | header drawer "Recent actions" | all authenticated | P00 | Last 20 own actions with undo where the window is open (AG.7.16) |

---

## AG.3 Settings menu structure

### AG.3.1 One settings shell, scoped sections

Every app has one settings shell (Appendix V §V.5: `/settings`, `/admin/settings`, `ops…/settings`, `/chambers/admin/settings`). The rail has up to three levels: **section** (scope) → **module** → in-page **group**. A section appears only if the user can read at least one setting in it (`cfg:read` on any key of the section, R-1). Personal is always first; Approvals, History and Health are always last. A search box sits at the top of the rail (SCR-P15-02); typing a canonical key jumps straight to it.

| Section | Modules in the rail (order) | Catalogue (owner) | Tiers met | Who sees the section | Screens |
|---|---|---|---|---|---|
| **Personal** | Profile · Sign-in and security · Sessions and devices · Notifications (channels, categories, quiet hours, digests) · Away and delegation · Language and accessibility · Privacy and consents · Connected accounts · Representatives (party) or Clients and authorities (representative) · Professional (neutral: availability and caps, fees, bank and tax, disclosures; representative: firm, snippets) · Directory listing · My views and dashboards · Shortcuts · My exports | V §V.4.2–§V.4.4; S §7 | T (user); G for neutral fees, bank and tax; L rows shown read-only (legal notices, NN-12 floor, advocate field set) | Everyone | SCR-P15-22 (SCR-P01-39 → -42), AG-SCR-06, AG-SCR-09, AG-SCR-11, SCR-P05-07 |
| **Organisation** | Profile and legal entity · Branding · Domains · Languages and time · Structure · Access (users, roles, privileged grants, permission sets, delegated admins, temporary access, access reviews, support sessions) · Cases (dispute types, intake forms, document requirements, templates, clocks, status labels, queues, SLAs and escalation) · Notifications · Billing and plan · Integrations · Custom fields · Reports and dashboards · Data (import, export, retention, legal hold, deletion) · Security · Privacy · AI · Public profile · Marketplace · **Navigation and terminology** · **Getting started** · Setting packs · Transfer (export/import settings) · Sandbox | V §V.4.1; O §5 (billing); AC §AC.17 | T, T≥G, G (TC or TLR), L read-only | Tenant admin, delegated admins (their modules only), DPO, billing admin, integration admin | SCR-P15-06 → -21, SCR-P05-19 → -33, AG-SCR-07, AG-SCR-10; *v3.1:* SCR-P15-27 (setting packs wizard, `/settings/onboarding`), SCR-P15-26 (bulk change, `/settings/bulk`), SCR-P15-25 (compare, `/settings/compare`) |
| **Rules and legal** | Rule-pack catalogue · Pack detail · Regulatory watch · Open items *(v3.1)* | V §V.2 | G (legal roles); read-only for admins | Legal roles; admins (read) | SCR-P15-10 → -12, SCR-P15-28 |
| **Chambers** | Practice identity and pages · Domains and SEO · Rules, codes and fees · Templates, intake, notifications, numbering, letterheads · E-sign, invoicing and payments · Staff, work and calendars · Practice HR, payroll and disbursal · Reports, exports and offboarding · Meetings (Teams bridge) · File mirror | W §W.8.1–§W.8.8; P21 §9 | T; G with `chm.config.approve.legal`; money G (NN-36) | Chambers owner, admin, HR, accounts (their modules) | SCR-P20-10, SCR-P20-11 (approvals → inbox), SCR-P21-12, SCR-P21-14 |
| **Enterprise** | Variant settings (lender, insurer, employer, university, POSH) · GRM clocks and routing · Complainant portal · Contact policy · Campaign limits | V §V.4.6 | T above floors; G by TLR; L statutory rows read-only | Enterprise admin, GRO (GRM modules), POSH presiding officer (sealed module) | SCR-P15-03 (module pages), SCR-P09-11, SCR-P07-07 |
| **Operations** | Departments and teams · CRM and pipeline · Support and grievance · Customer success · Onboarding · Knowledge base · Automations · Connectors and workspace · Marketing and social · Reports · Guest access | X §X.13; Y §Y.12; AC §AC.17 | T; G for scoring, discount bands, stage gates, grievance clocks, claims | `ops_director`, `ops_manager`, `department_head` (own unit), `support_lead`, `marketing_manager`, `it_admin` | SCR-P16-39, SCR-P16-16, SCR-P16-26, SCR-P17-30, SCR-P21-01 → -03 |
| **HR and payroll** | Organisation and entities · Leave policies and packs · Holidays and calendars · Attendance and measurement notice · Performance cycles · Payroll parameters (rule packs) · Pay structures · Statutory outputs · Workspace (UPN, SKU rules) | Z §Z.15 | T≥G; G for parameters; L monitoring prohibitions (NN-35) shown read-only | `hr_manager`, `payroll_checker`, `compliance_officer`, `it_admin` | SCR-P18-26, SCR-P18-27, SCR-P18-28 |
| **Controls** | Authority matrix and DoFP · Separation of duties · Bank-change cooling-off · Expense and procurement limits | Z §Z.12, V §V.4.7 | G (NN-36); cooling-off T above L floor | `finance_controller`, CS, security lead; `internal_auditor` read | SCR-P18-37, SCR-P18-38 |
| **Group** | Group register · Group templates and locks · Cross-company grant templates · Shared dashboards · Registry consumer settings | V §V.4.8; AD §AD.16 | G (with Company Secretary / DPO); T at group scope for templates | `group_admin`, `group_hr`, DPO | SCR-P15-24, SCR-P21-20 |
| **Platform** (admin shell only) | Registry browser · Navigation registry · Platform flags · Platform G values | V §V.6 | G (platform checker); L release only | Product owner, CTO, `platform_admin`, HL | SCR-P15-23, SCR-P00-06, AG-SCR-07 |
| (always last) | **Approvals** · **History** · **Health** | V §V.5 | — | Anyone with items / history / admin | Inbox view `source=cfg` (AG-SCR-01), SCR-P15-04, SCR-P15-14 |

### AG.3.2 Row anatomy, tier badges and where approvals appear

1. **Tier badge** on every row, with icon and text (colour is never the only cue): `🔒 Locked` (L), `⚖ Governed` (G), `✎ Tenant` (T); bounded rows show `✎ Tenant (within limits)` with the bound in the popover. The "Who can change this" popover lists roles, approvers, bounds, citations and effective scope (V §V.5).
2. **Inheritance chip:** "Inherited from {scope}", "Overridden here", or "🔒 Locked by {scope}" (V §V.1.3).
3. **Save button text follows the tier:** T → **Save** (applies immediately; toast "Saved · Undo" for 10 seconds, then history restore); G → **Submit for approval** (shows the approver role and the SLA, e.g., "Tenant legal reviewer · usually within 2 working days"); L → no button, reason text "Fixed by law or platform policy" with the source (P18 copy rule).
4. **Pending state:** a G change shows a yellow "Pending approval" chip with requester, approver role and age; the previous value stays in force until approval (or the configured fallback, V §V.2.10). Opening the chip opens the request in the Work Inbox item panel.
5. **Where approvals appear:** (a) the approver's **Work Inbox** (source `cfg`, `chm` or `ctl` per engine); (b) the settings section's **Approvals** rail item (filtered inbox); (c) the requester's "My requests" tab; (d) the Configuration Health page counts. There is no separate approval queue anywhere else (D3-46).
6. **Preview before save** for branding, templates, clocks, rule packs and notifications (V §V.5); the preview must be fresh (`CFG_PREVIEW_STALE` otherwise).
7. **Bulk edits** of settings are allowed only through setting packs, import or the Bulk change screen SCR-P15-26 (change sets with an impact preview and the V §V.5.2 undo window, `CFG_UNDO_WINDOW_EXPIRED` after it), never by multi-select on a module page *(v3.1)*.

---

## AG.4 Unified Work Inbox and notification centre (AG-SCR-01, AG-SCR-02; D3-46)

### AG.4.1 Item kinds

| Kind | Meaning | Examples | Actionable | Counts in header badge |
|---|---|---|---|---|
| `task` | Work assigned to me or my queue | Upload requested document; scrutiny of a filing; onboarding step; regularise attendance | Yes | Yes |
| `approval` | A maker-checker request where I am an eligible checker | Settings change; payroll run; payee bank change; refund; write-off; discount; privileged grant; sensitive export; rule-pack publication; allocation override; change record; cross-company grant; sponsored creative | Yes | Yes |
| `mention` | Someone @mentioned me in an internal note, task, ticket, KB comment or review | "@Priya please check the GST line" | Yes (reply / done) | Yes |
| `message` | A new message in a thread I belong to | Case thread; ticket reply; enquiry | Yes (reply) | Yes |
| `deadline` | A dated obligation I own, shown before it becomes a task | Clock T-7; challenge-window end; renewal T-30; certification expiry | Yes (open) | Only at amber/red |
| `alert` | An exception needing attention | SLA breach; reconciliation break; automation auto-paused; ghost-employee hit | Yes | Yes |
| `request` | Someone asks me for something outside a workflow | Access request (AG-SCR-17); auditor evidence request (PBC); data-room request | Yes | Yes |
| `update` | Information only (the old notification centre, SCR-P07-17) | Order issued; payment received; hearing rescheduled | No (mark read) | No |

### AG.4.2 Sources (adapters registered in `cfg.inbox_sources`)

| Source code | Owning engine | Store (plane) | Kinds | Decision component (embedded in AG-SCR-02) |
|---|---|---|---|---|
| `cfg` | `core.config_change_requests`, `cfg.change_sets` (X-56) | `core.inbox_items` | approval, alert | Change-request review (SCR-P00-10 / SCR-P15-05 component) |
| `ctl` | `ctl.approval_requests` (payroll, payments, payees, refunds, write-offs, spend, privileged grants, sensitive exports) | store of the cluster that holds `ctl` (P15 ADR) | approval, alert | Approval payload summary with digest, authority source, SoD/COI result (SCR-P18-36 component) |
| `case` | Cases, clocks, notices, hearings, outcomes, documents | `core.inbox_items` | task, deadline, message, update | Case Desk action components (SCR-P02-93/-94/-95) |
| `chm` | Chambers G approvals, pay runs, privileged grants, enquiries | store of the `chm` cluster | approval, task | SCR-P20-11, SCR-P20-23 components |
| `grp` | Cross-company grants, GDSA, recharge checks; *v3.1:* assignment requests (SCR-P21-30) | store of the `grp` cluster | approval, request | SCR-P21-22 component |
| `eng` | Change records (CAB, production approval), JIT access, risk acceptances; *v3.1:* daily standard-train approval (two-person), missed restore tests | `core.inbox_items` | approval, alert | SCR-P21-AE03 / AE10 components; SCR-P21-AE02 train summary |
| `rev` *(v3.1)* | Stream transitions, price-change requests, viability proposals (`rev.viability_proposals`, Appendix AB §AB.7.4) | store of the `rev` cluster (P15 ADR) | approval, alert | SCR-P19-AB03 / AB09 components |
| `ops` | Tasks, tickets, grievances, onboarding, CS playbooks, automations, CRM approvals (quotes, imports, retention offers) | `ops.ws_inbox_items` | task, approval, alert, mention, message | SCR-P16-03 component; ticket composer |
| `mkt` | Content reviews, send approvals, crisis tasks, evidence due | `ops.ws_inbox_items` | approval, task | SCR-P17-09, SCR-P17-17 components |
| `hr` | Leave, regularisation, claims, onboarding checklists, acknowledgements, performance cycle tasks; *v3.1:* probation reviews (SCR-P18-45) | store of the `hr` cluster | task, approval | SCR-P18-25, SCR-P18-19 components |
| `mkp` | Provider verification (two-person), moderation, payout batches; *v3.1:* onboarding-pipeline work items (SCR-P19-19) | store of the `mkp` cluster | approval, task | SCR-P19-21, SCR-P19-26 components |
| `xpt` | Export approvals and ready downloads | `core.inbox_items` | approval, update | SCR-P21-09 component |
| `comms` | Notifications (P07) | `core.inbox_items` | update, message | Notification card |
| `identity` | Access requests, delegation notices, break-glass reviews | `core.inbox_items` | request, approval | AG-SCR-17; break-glass review component |

**Federation (D3-46).** Each source writes inbox items through `InboxPort.upsert()` into the store of its own cluster (the cluster mapping is in the P15 ADR on schema placement, master §4.5). The BFF of each app reads the stores the user's shell is entitled to, in parallel, with the user's token, and merges them by the ordering key (AG.4.4); there is no database join across clusters. Items in another shell are not shown; the inbox header says "Also waiting for you: Console 3 · Operations 5" with links (counts only, fetched from each shell's count endpoint for the same person).

**Item content rule.** An inbox item stores IDs, codes, a title template key with non-sensitive parameters, due date, priority, SLA state and allowed action codes — never document text, party names beyond what the viewer may already see, amounts on sealed matters, or anything from a sealed store. POSH items read "You have an update in the IC workspace" (NN-07).

### AG.4.3 Acting on an item

1. Opening an item opens AG-SCR-02 (drawer on desktop, full screen on mobile) with the owner's **decision component** loaded from `GET /v1/inbox/items/{id}/view` (view model supplied by the owning module) and the item's history.
2. Every action calls the **owning engine's API** with `If-Match: {sourceVersion}`; the engine re-runs authority, SoD, step-up and validators. A stale item returns `CFG_INBOX_ACTION_STALE` (409) and the panel reloads with "This changed since you opened it".
3. Approve and reject require a reason when the engine requires one, and step-up where the engine requires it (G approvals aal2; money aal2-pr). The confirmation repeats the context line (AG.1.3 rule 7).
4. **Bulk actions:** mark read, snooze, reassign (to a queue member holding the permission), and mark done for tasks. **Bulk approve is not allowed** for G-legal changes (V §V.5), money movements, payroll, payee or bank changes, privileged grants and sensitive exports (NN-36). Bulk approve is allowed only for sources flagged `bulk_approvable` in `cfg.inbox_sources` (default: leave requests, attendance regularisations, T-tier content reviews), with each item still checked individually and failures listed. *v3.1:* these are single-approver operational approvals, not maker–checker controls; Appendix C §F item 12 (no bulk for any maker–checker approval or decision with legal effect) is read with this list, and a source may be flagged `bulk_approvable` only if none of its items is a maker–checker control over money, legal effect or access.
5. Done items move to **Done** (kept 90 days in the inbox; the source keeps its own record permanently).

### AG.4.4 Ordering, priority and SLA colouring

**Priority** is computed by the source and normalised:

| Priority | Rule |
|---|---|
| P1 | Statutory or regulator deadline due ≤ 24 h or breached; security alert; money release awaiting dual control where the payee deadline is today |
| P2 | SLA amber or red; approval blocking other people's work; due ≤ 3 working days |
| P3 | Normal actionable work |
| P4 | Updates (FYI) |

**Default order (deadline-aware):** `(legal_blocking DESC, sla_state_rank DESC, due_at ASC NULLS LAST, priority ASC, created_at ASC)`, where `legal_blocking` is true for owned statutory clocks (NN-04) and regulator clocks (GRM, grievance). Users may sort by "Newest" or "Source" but the default returns on each visit.

**SLA colouring** uses the server-computed state only (`green`, `amber`, `red`, `breached`) and the clock tokens of Appendix C §E.1, always with text: "Due in 3 h", "Due 12 Nov (2 days)", "Overdue by 1 day". The UI never computes clock state (Appendix C §G.3).

### AG.4.5 Snooze, delegation and away

| Feature | Rule |
|---|---|
| Snooze | Until a time, "tomorrow 09:00", "next working day" or until an event ("until the other side replies"). P1 items cannot be snoozed; P2 items cannot be snoozed past `due_at − 24 h`. Statutory-clock items cannot be snoozed past T-24 h (L). Maximum 3 snoozes per item (`user.inbox.max_snoozes`, T, 1–5); beyond that `CFG_INBOX_SNOOZE_LIMIT`. Snoozed items reappear at the top with "Snoozed earlier". |
| Away (AG-SCR-06) | Start and end date-time, optional message ("Away until 18 Nov", no reason field), and per-source handling: **delegate**, **return to queue** or **hold**. Shown to requesters on items assigned to the user and on @mention pickers. Approved leave in `hr` prompts the employee to set Away; it is never switched on silently. |
| Delegation of approvals | Delegate must already hold the permission and an authority limit ≥ the item amount; delegation obeys Appendix S §6.4 (≤ 90 days, depth 1) and `core.delegations`; the delegate can never approve an item they made (NN-36); delegated actions are recorded "by {delegate} on behalf of {delegator}". Invalid choice → `CFG_INBOX_DELEGATION_NOT_ALLOWED`. |
| Delegation of tasks | Reassign to a named colleague or queue; cross-department reassignment records the reason (Appendix X §X.3.4). |
| Delegated-item visibility *(v3.1)* | In the delegate's inbox each delegated item carries the chip "On behalf of {delegator} until {date}" and a filter "On behalf of others"; the source object shows "Covered by {delegate} until {date}" (Appendix C §F item 15); on return the delegator sees a summary of what was decided for them. Leave-linked delegations (Appendix Z §Z.12.2 `LeaveDelegationJob`) appear the same way. |
| Request SLA chips *(v3.1)* | Cross-company grant and assignment requests (`grp`) show the remaining decision time against `group.grants.approval_sla_working_days` / `group.assignments.decision_sla_working_days` ("Decide by 14 Nov · 2 working days"); revenue viability proposals show `platform.rev.viability.decision_sla_days`. |
| No delegate set | Items of an away user follow the source's escalation ladder (AG.7.13): after `tenant.inbox.away_escalation_hours` (T, default 8 working hours; P1 items 1 hour) they move to the role queue and the department head is told. |
| Unassigned approvals | An approval with no eligible checker within the authority matrix escalates to the next authority level and raises an `alert` to the control owner (NN-36 exception log). |

### AG.4.6 Notification centre, digests and quiet hours

1. **Updates tab** replaces the SCR-P07-17 list UI; the P07 data model, channels and evidence stay. Every update links to its object and to "Why am I getting this?" (rule, category, preference link).
2. **Channels per kind** (user-tunable within S §7 categories; legal notices cannot be switched off):

| Kind / priority | In-app | Push | Email | SMS / WhatsApp |
|---|---|---|---|---|
| P1 | Immediate | Immediate | Immediate | Immediate for parties where the category is case-critical; staff only if on the on-call roster |
| P2 | Immediate | Immediate | Daily digest (or immediate if the user opts in) | No (parties: per case-critical category) |
| P3 | Immediate | Optional | Daily digest | No |
| P4 updates | Immediate | No | Weekly digest (optional) | No |

3. **Digest rules.** Daily digest at the user's chosen time (default 08:30 in the user's zone); weekly digest Monday 08:30; a digest lists counts per source and the top 10 items by the AG.4.4 order; no digest when there is nothing actionable; digests never include sealed content, document text or amounts on sealed matters; party digests are plain-language and in the notice language.
4. **Quiet hours.** User quiet hours are narrow-only against the tenant setting (`notify.quiet_hours`, default 21:00–08:00) and never wider than the locked NN-12 contact window for borrower-facing contact (08:00–19:00 local; FIN floor 19:00–08:00 quiet). During quiet hours push, SMS and WhatsApp are held and released at the end of quiet hours in priority order; in-app items still arrive. Exceptions: account-security alerts to the account holder; on-call staff alerts. Legal-notice service follows P07 and NN-12, not these preferences.
5. **De-duplication.** One event produces at most one inbox item per user; a later event about the same object updates the item (e.g., "3 new messages") rather than adding items. Channel sends are de-duplicated by `(user, object, kind, 15-minute window)`.

---

## AG.5 Global search and command palette (AG-SCR-03, AG-SCR-04)

### AG.5.1 Indexed objects per shell and role

Each shell searches only its own plane's indexes (master §4.4: OpenSearch per-tenant aliases; sealed data never indexed; Appendix X §X.2.1 company-scoped `ops-{company}-*` aliases).

| Shell | Object types indexed | Who finds them | Searchable fields | Never indexed |
|---|---|---|---|---|
| `party` | Own cases; documents filed in or served in own cases; messages; invoices and receipts; help articles | The party (case membership) | Case number, title, other side's organisation name, document title, exhibit label, invoice number | Other side's private uploads, caucus notes, screening and vulnerability data, sealed tiers |
| `representative` | Matters under active authority; their documents and messages; clients | Representative within authority scope | As party + client name | Matters after authority ends (results show "Authority ended on {date}") |
| `neutral` | Assigned cases; orders and outcomes drafted by me; appointment offers | Neutral | Case number, parties' labels, order number | Caucus notes of others; unconstituted cases |
| `console` | Cases of the tenant; parties; notices; hearings; bundles; tickets with verified case links (support roles) | Staff per role and team | Case number, party name, mobile (exact match only, masked in results), notice number, hearing date | POSH, health, family-safety, caucus notes; IC data |
| `chambers` | Matters (by `chm.case_access`), enquiries, staff (HR roles only), invoices, pages | Per role | As console; staff name for HR | Salary and bank fields; case content for HR and accounts roles (D3-19) |
| `enterprise` | Own portfolio cases, batches, tickets (GRM), clauses | Enterprise roles | Loan/policy/claim reference, case number, batch ID, ticket number | POSH records (sealed sub-shell has no search) |
| `ops` | Leads, accounts, contacts, opportunities, quotes, tickets, grievances, projects, KB, campaigns, content items, assets, employees (directory projection), tasks, change records | Per role, company and grant | Names, numbers, emails (exact), ticket and grievance numbers | Ticket bodies flagged `case_linked` except for support roles; salary, appraisal, leave reasons; any `hr`/`pay` field not in the staff directory projection |
| `admin` | Tenants, flags, rule packs, settings keys, audit events (by ID), incidents, AI artefacts | Platform roles | Codes, keys, IDs | Case content |
| `assurance` | Engagement evidence, controls, findings | Auditor within engagement | Control ID, artefact name, finding ID | Everything outside the engagement scope |

### AG.5.2 Permission trimming and sealed exclusion

1. **Document-level security at query time:** every indexed document carries ACL tokens (`tenant`, `entity`, `company`, `case_member:{caseId}`, `role:{code}`, `team:{id}`); the query adds a filter for the caller's tokens resolved from `Equator-Context`.
2. **Post-filter:** the top 50 hits are re-checked with Cerbos `checkResources` before rendering; any denial drops the hit and is logged as `search.acl_drift` (alerting if > 0.1 % of queries).
3. **Counts never leak:** result counts are computed after trimming and shown as "About 40 results" only above 100; tabs show counts per type after trimming.
4. **Sealed exclusion (L):** POSH, INS health, FAM safety, caucus notes and IC data are never indexed; the POSH sub-shell has no search box; global search in other shells returns nothing for them and gives no hint that they exist. CI test `SEARCH_NO_SEALED` seeds sealed records and asserts zero hits for every role.
5. **Exact-match identifiers:** mobile numbers, emails, PAN and Aadhaar-like strings are matched only by exact normalised value (never prefix), for staff roles that may search them; results show masked values (master §4.4 PII rule). Aadhaar numbers are never indexed.
6. **Query logging:** query text is not stored; only length, result-count bucket, clicked rank and object type (AG.9.3).

### AG.5.3 Query behaviour

- A case number pattern (`EQ/{VERT}/{CITY}/{YYYY}/{NNNNN}` or a tenant prefix) jumps straight to the case when exactly one accessible match exists.
- Type prefixes: `case:`, `doc:`, `inv:`, `tkt:`, `lead:`, `acct:`, `emp:` (HR roles), `set:` (settings keys), `cmd:` (commands only), `@` (people the user may mention).
- Typo tolerance (edit distance 1 for terms ≥ 5 characters); language analysers for the enabled locales; Hindi and other Indic-script queries match native-script fields; transliteration is not applied to legal names.
- Results grouped by type, each with a primary action (open, pay, reply, approve opens the item panel).
- Empty results suggest: "Search in Help", "Check the spelling", and, for staff, "You may not have access to some records".

### AG.5.4 Command palette (`Ctrl/Cmd+K`)

The palette lists **commands** (registered as `cfg.nav_items` with `kind = 'command'`), **navigation targets** (every visible menu item), **recent items** (last 20 objects opened in this context) and **search results** (after 2 characters, from AG.5.1). Commands obey the same resolver rules as menus (R-1 to R-5). In the POSH sub-shell the palette offers navigation only.

| Command | Shells | Shortcut | Action |
|---|---|---|---|
| Go to Home | all | `G` then `H` | Shell home |
| Go to Inbox | all | `G` then `I` | AG-SCR-01 |
| Go to Cases / Matters / Queue | party, representative, neutral, console, chambers, enterprise | `G` then `C` | Case list or queue |
| Go to Calendar | party, representative, neutral, console, chambers | `G` then `K` | AG-SCR-23 |
| Go to Settings | all | `G` then `S` | Settings home |
| New … (context: case, ticket, lead, task, claim, leave request) | per shell | `N` | Create form for the current list's object |
| File a case | party, enterprise | — | SCR-P02-04 / SCR-P02-06 |
| Respond to a notice | party | — | SCR-P02-07 |
| Pay a fee | party | — | AG-SCR-21 (due first) |
| Join next session | party, representative, neutral | `J` then `S` | Hearing lobby of the next session within 15 min |
| Next in queue | console, ops, chambers, GRM | `Shift+N` | Opens the next item by AG.4.4 order |
| Assign clock owner | console | — | SCR-P02-11 action |
| Compose notice | console | — | SCR-P02-12 |
| Approve or reject selected item | inbox | — (opens the decision panel; never one-key approve) | AG-SCR-02 |
| Snooze / Mark done / Reassign | inbox | `S` / `E` / `A` | Item actions |
| Reply | inbox, tickets, threads | `R` | Composer |
| Switch context | all | `Ctrl/Cmd+Shift+O` | AG-SCR-05 |
| Request an export | all | — | SCR-P21-08 |
| Clock in / Clock out | selfservice, chambers ESS | — | SCR-P18-17 / SCR-P20-27 |
| Request leave | selfservice, chambers ESS | — | SCR-P18-25 / SCR-P20-22 |
| Find a setting | all | `G` then `,` | Settings search |
| Toggle side navigation | all | `[` | Collapse or expand |
| Keyboard shortcuts | all | `?` | AG-SCR-11 |
| Help for this page | all | `Ctrl/Cmd+/` | AG-SCR-12 |
| Find setting… · Change setting… · Compare with… · Apply pack… · Bulk change… · Restore previous value… (T only) · Open configuration health *(v3.1)* | all with settings access | `G` then `,` (find); others none | Settings search; row editor; SCR-P15-25; SCR-P15-27; SCR-P15-26; history restore; SCR-P15-14 (Appendix V §V.5) |
| Open approvals · Approvals: overdue *(v3.1)* | all | `G` then `I` (then filter) | Work Inbox filtered to `approval` kind, or to approvals past SLA, in AG.4.4 order |
| Marketplace: saved searches · My onboarding *(v3.1)* | public (signed in), neutral, chambers | — | AA §AA.5 saved searches; SCR-P19-10 |
| Exports: estimate · Exports: progress · Verify a package *(v3.1)* | all | — | SCR-P21-08 estimate; SCR-P21-09 progress; SCR-P21-31 |
| Engineering: standard train approval · Restore assurance report *(v3.1)* | ops (engineering roles) | — | SCR-P21-AE02 (train); SCR-P21-AE06 |
| Revenue: viability proposals *(v3.1)* | ops (`revenue_manager`, CFO) | — | Work Inbox source `rev`; SCR-P19-AB09 |
| Queue views: vertical case-manager views (FR-P08-87) · GRO inbox views (FR-P09-50) *(v3.1)* | console, enterprise (GRM) | — | Opens the system saved view by name (AG.5.6) |
| QuickExit | sealed, FAM, safety | `Esc` twice | Appendix C §F.5 |

### AG.5.5 Keyboard shortcut rules

1. Single-character shortcuts (`G`, `N`, `S`, `E`, `A`, `R`, `J`, `[`, `?`) work only when focus is not in a text input, and every one can be turned off or remapped in AG-SCR-11 (WCAG 2.2 SC 2.1.4 Character Key Shortcuts). The setting `user.ui.single_key_shortcuts` defaults ON for workforce shells and OFF for party and representative shells.
2. Reserved browser and assistive-technology combinations are never bound (`Ctrl/Cmd+L`, `Ctrl/Cmd+T`, `Ctrl/Cmd+W`, `Alt+F4`, screen-reader modifier keys); a remap to a reserved or duplicate binding fails with `CFG_SHORTCUT_RESERVED` or `CFG_SHORTCUT_CONFLICT`.
3. No shortcut performs an irreversible action; approve, sign, pay, serve and publish always open a confirmation (AG.7.16).
4. List navigation: `J`/`K` next and previous row, `X` select, `Enter` open, `Shift+X` select range; tables announce the selected row.
5. **Screen-scoped key maps** *(v3.1)*. A screen may declare its own single-key map (registered as `cfg.nav_items` rows with `kind = 'command'` and the screen ID), shown in AG-SCR-11 and remappable like any other key. Inside that screen its map replaces the inbox single keys of AG.5.4; global chords (`G` then …, `Ctrl/Cmd+K`, `Ctrl/Cmd+Shift+O`, `Shift+N`, `?`, `[`) can never be redefined. Registered maps: **open approval decision panel** (AG-SCR-02, SCR-P16-03, SCR-P18-36, SCR-P15-05) `A` approve, `R` reject, `D` delegate — each opens the confirmation with reason and step-up, never completing the decision (rule 3); **scrutiny queue** SCR-P02-08 `A` accept, `D` deficiency, `S` signpost, `R` reject (each opens the decision panel with that outcome pre-selected; legally effective, so never bulk, Appendix C §F item 12), `J`/`K`; **GRO desk** SCR-P09-12 (FR-P09-50) `a` assign to me, `d` request AI draft, `e` escalate, `j`/`k`; **chambers page editor** SCR-P20-04 (W §W.3.11) `/` insert block. Elsewhere `/` focuses the screen's search or filter box when it has one (settings shell: settings search, Appendix V §V.5).
6. *(v3.1)* The reserved list of rule 2 also includes `Ctrl/Cmd+N`, `Ctrl/Cmd+Shift+N` and `Ctrl/Cmd+Shift+P` (new and private windows), so the page-editor preview uses `Ctrl/Cmd+Alt+P` (W §W.3.11).

### AG.5.6 Recent items, pins and saved views

| Feature | Rule |
|---|---|
| Recent items | Last 20 objects opened per user per context, stored in the plane of the object (`core.recent_items`, `ops.ws_recent_items`); shown in the palette and on home; cleared on context switch for that context only; never include sealed objects; retention 30 days. |
| Pins | Up to 8 pinned menu items or saved views per user per shell (`cfg.user_nav_prefs`); shown in the side-nav "Pinned" group. |
| Saved views | One contract across planes (`core.saved_views` from Appendix L; `ops.ws_saved_views` from Appendix X; additive columns in AG.10.1): name, object type, filters (allow-listed fields only; sealed fields rejected with `CFG_VIEW_FILTER_FORBIDDEN`), columns, sort, grouping, sharing scope (`me`, `team`, `department`, `tenant`, `company`), `is_default`, `pinned`. Shared views re-apply the viewer's permissions at render time. Sharing beyond the owner's own scope fails with `CFG_VIEW_SHARE_SCOPE`. System views (e.g., "Filings due in 7 days", "Breaching in ≤ 60 min", "Waiting for my signature") are seeded from `cfg.view_definitions` and cannot be deleted, only hidden. *v3.1:* the seeds include the per-vertical case-manager views of P08 FR-P08-87 (e.g., FIN "NOC/bureau overdue", COM "s.29A month 10+", FAM "registration 4-month clock < 30 days"), the GRO views of P09 FR-P09-50 ("IO routing due in ≤ 3 days", "Final reply due today", "Awaiting complainant > 5 days", "RB-IOS reference not yet captured", "Duplicates to confirm") and the open-items views of Appendix J §J.9.2 ("My items", "Awaiting counsel", "Chase overdue", "Blocking next release"); each appears under its queue in the side nav "Views" group and as a palette target. |
| View URL | A saved view has a stable URL (`?view={id}`); opening it without access shows the owner's name and "This view is not shared with you". |

---

## AG.6 Dashboards, widget catalogue and "next best action"

### AG.6.1 Widget catalogue (`cfg.widget_catalogue`)

Every widget is registered once with a data source, the roles that may add it, its privacy rule and refresh. Dashboards are server-composed (`GET /v1/me/dashboard/{code}`, Appendix S §8.2; `ops` equivalent in the business plane); each widget shows "Data as of {time}" and drills down only to records the viewer may open. **Privacy rules applied to every widget:** no sealed data outside the sealed workspace (NN-07); no neutral outcome statistics, win rates or rankings (NN-16, NN-28); aggregates about people need n ≥ 5 internally and n ≥ 10 when public (X-28); individual-employee metrics only to the person, their manager line and HR within NN-35.

| Widget code | Shows | May be added by | Source | Refresh |
|---|---|---|---|---|
| `W-INBOX` | Inbox summary by kind and P1/P2 count | all | AG.4 count service | live |
| `W-NBA` | Next-best-action panel (AG.6.4) | all | `cfg.nba_rules` evaluator | on load + events |
| `W-NEXT` | Next action card with due date, days left and "who decides" | party, representative | Case Desk read model | live |
| `W-MYCASES` | Cases with status chip, ClockPill, "what happens next" | party, representative, neutral | cases read model | 1 min |
| `W-SIGNPOST` | Free or statutory forum reminder with last date (NN-20) | party | routing results | daily |
| `W-SESSIONS` | Upcoming sessions with join (15 min before) | party, representative, neutral, chambers | hearings | live |
| `W-MONEY` | Paid, due, refundable, instalments | party | billing | 5 min |
| `W-DOCREQ` | Documents requested from me | party, representative | documents | live |
| `W-REPS` / `W-AUTH` | My representatives / authorities expiring ≤ 14 days | party / representative | representatives | daily |
| `W-FILINGS-DUE` | Filings due 7 / 14 / 30 days | representative | cases | hourly |
| `W-OFFERS` | Appointment offers with countdown / offers awaiting client decision | neutral / representative | neutrals, proceedings | live |
| `W-CLOCKS-MINE` | Owned statutory clocks amber/red (s.29A for arbitrators) | neutral, case manager, registrar | clocks service | live |
| `W-DRAFTING` | Orders and awards in drafting with age | neutral | outcomes | hourly |
| `W-CPD` / `W-EARNINGS` | CPD hours vs requirement / payouts pending | neutral | neutrals, payouts | daily |
| `W-QUEUE` | Queue by stage with SLA timers | case manager, chambers case manager | cases | live |
| `W-SERVICE-FAIL` | Service failures and deemed-service decisions due | case manager | notices | 5 min |
| `W-UNOWNED-CLOCKS` | Unowned statutory clocks (must be 0) | registrar, case services lead | clocks | live |
| `W-APPOINTMENTS` / `W-CHALLENGES` | Allocation runs pending (counts only) / challenges with timeliness | registrar | neutrals, proceedings | 5 min |
| `W-PRACTICE` | Caseload, stage medians, clock risk (§W.7) | chambers owner, admin | `chm` reporting views | hourly |
| `W-PRACTICE-MONEY` | Revenue, receivables ageing, GST collected | chambers owner, accounts | `chm` | hourly |
| `W-ENQUIRIES` | Enquiries acknowledged within SLA, conversion | chambers owner, admin, front desk | `chm` | hourly |
| `W-PAYRUN` | Pay-run stage, variance, ghost hits, statutory due dates | chambers owner, HR, accounts; `payroll_*` | `chm` / `pay` | live |
| `W-CONTROLS` | Maker-checker exceptions, bank-change events, single-person log | chambers owner, external checker, compliance, `internal_auditor` | `chm` / `ctl` | live |
| `W-ENT-PORTFOLIO` | Volumes FY, settled pre-arbitration %, notice funnel, instalment compliance | enterprise | cases aggregates | hourly |
| `W-SLA-HEAT` | SLA heatmap by stage or queue | enterprise, support lead, ops director, department head | per source | 15 min |
| `W-NEUTRALITY` | Fixed banner "Neutrals are appointed independently by Equator" | enterprise (mandatory, L) | static | — |
| `W-GRM-CLOCKS` | Tickets by regulator clock state (T-7, T-3, breached) and ageing | grievance officer, internal ombudsman | `grm` / `ops` grievance | live |
| `W-OPS-SCORE` | Company scorecard (ARR, NRR, GRR, CSAT, ticket SLA %, grievance breaches) | ops director, department head (own unit) | `ops` reporting | hourly |
| `W-APPROVALS-ME` | Approvals awaiting me, by source and age | any approver | AG.4 | live |
| `W-REV-STREAMS` | Revenue by stream with neutrality-exposure tile | ops director, finance, revenue manager | `rev` (App. AB) | daily |
| `W-ONB` | Projects by RAG; go-live sign-offs due; migration failures | onboarding, CSM | `ops` | 15 min |
| `W-CS-HEALTH` | Health distribution and movers; renewals 120/90/60/30 | CSM, ops director | `ops` | daily |
| `W-SUPPORT` | My queue by SLA; breaching ≤ 60 min; unassigned; backlog age; reopen rate; CSAT | support agent, support lead | `ops` | live |
| `W-AGENT-LOAD` | Open items and SLA attainment per agent (work items only, NN-35) | support lead, department head | `ops` | 5 min |
| `W-MKT` | OKR progress; items due for review; held items; evidence overdue; sends awaiting approval | marketing manager, content roles | `mkt` | 15 min |
| `W-CRISIS` | Active crisis banner with clocks | marketing manager, PR, ops director | `mkt` | live |
| `W-HR` | Headcount by entity/State, joiners and leavers, pending acknowledgements, leave liability | HR manager, group HR | `hr` | daily |
| `W-HR-CLOCKS` | HR statutory clocks (F&F, exit, registrations expiring) | HR manager | `hr` | live |
| `W-TEAM` | Team queues, capacity vs utilisation, leave calendar | department head, managers | `ops`, `hr` projection | hourly |
| `W-ESS` | Clock-in state, leave balance, latest payslip, my tasks, goals due | employee | `hr`, `pay` (own) | live |
| `W-AUDIT` | Engagement grant countdown, PBC status, samples, findings | auditor, internal auditor | `eng` | live |
| `W-GROUP` | Entities, grants expiring ≤ 14 days, wall attestations overdue, related-party approvals pending, consolidated pack (k-suppressed) | group admin | `grp` | daily |

### AG.6.2 Default layouts per role (row 1 → row 3; **bold** = mandatory, cannot be hidden)

| Role | Dashboard (screen) | Row 1 | Row 2 | Row 3 |
|---|---|---|---|---|
| Party | SCR-S-D01 | **`W-NEXT`**, `W-NBA` | **`W-MYCASES`**, `W-SESSIONS` | **`W-SIGNPOST`** (when applicable), `W-MONEY`, `W-DOCREQ`, `W-REPS` |
| Representative | SCR-S-D02 | `W-NBA`, `W-INBOX` | **`W-MYCASES`** (matters by client), `W-FILINGS-DUE` | `W-SESSIONS`, `W-OFFERS`, `W-AUTH` |
| Neutral (mediator / arbitrator) | SCR-S-D03 / -D04 | **`W-SESSIONS`** (mediation) or **`W-CLOCKS-MINE`** (arbitration, s.29A), `W-NBA` | `W-OFFERS`, `W-DRAFTING` | `W-CPD`, `W-EARNINGS` |
| Chambers owner | SCR-P20-29 `workspace_home` *(v3.1)* | `W-NBA`, `W-APPROVALS-ME` | `W-PRACTICE`, `W-PRACTICE-MONEY` | `W-ENQUIRIES`, `W-PAYRUN`, `W-CONTROLS` |
| Case manager | SCR-S-D05 | **`W-QUEUE`**, `W-NBA` | **`W-CLOCKS-MINE`**, `W-SERVICE-FAIL` | `W-SESSIONS` (logistics), `W-INBOX` |
| Registrar | SCR-S-D06 | **`W-UNOWNED-CLOCKS`**, `W-NBA` | `W-APPOINTMENTS`, `W-CHALLENGES` | `W-APPROVALS-ME` (break-glass, certified copies) |
| Enterprise admin | SCR-S-D08 | **`W-NEUTRALITY`**, `W-NBA` | `W-ENT-PORTFOLIO`, `W-SLA-HEAT` | `W-APPROVALS-ME` (offers within authority), `W-INBOX` |
| Grievance officer | SCR-S-D09 / SCR-P16-27 | **`W-GRM-CLOCKS`**, `W-NBA` | `W-INBOX` (acknowledgements due ≤ 12 h) | `W-SLA-HEAT` (categories) |
| Ops director | SCR-P16-02 | **`W-OPS-SCORE`**, **`W-APPROVALS-ME`** | `W-REV-STREAMS`, `W-SLA-HEAT` | `W-CS-HEALTH` (at risk), `W-CRISIS`, `W-NBA` |
| Onboarding specialist | SCR-P16-18 | **`W-ONB`**, `W-NBA` | `W-INBOX` | `W-SESSIONS` (training this week) |
| Customer success manager | SCR-P16-21 | **`W-CS-HEALTH`**, `W-NBA` | `W-ONB` (hypercare), `W-INBOX` | `W-APPROVALS-ME` (retention offers) |
| Support lead | SCR-P16-24 (lead layout) | **`W-SUPPORT`**, `W-NBA` | `W-AGENT-LOAD`, `W-SLA-HEAT` | `W-APPROVALS-ME` |
| Marketing manager | SCR-P17-01 | **`W-MKT`**, `W-CRISIS` (when active) | `W-APPROVALS-ME` (sends, sequences), `W-NBA` | `W-INBOX` |
| HR manager | AG-SCR-20 (HR layout) / SCR-P18-11 | **`W-HR-CLOCKS`**, `W-NBA` | `W-HR`, `W-APPROVALS-ME` | `W-TEAM` |
| Payroll checker | SCR-P18-29 (cockpit summary) | **`W-PAYRUN`**, **`W-APPROVALS-ME`** | `W-CONTROLS` | `W-NBA` |
| Department head | SCR-P16-01 (head layout) | `W-TEAM`, `W-APPROVALS-ME` | `W-SLA-HEAT` (own unit), `W-OPS-SCORE` (own unit) | `W-NBA` |
| Employee | AG-SCR-20 | **`W-ESS`**, `W-NBA` | `W-INBOX` | — |
| Auditor | SCR-P21-AE09 · SCR-S-D14 | **`W-AUDIT`** | `W-INBOX` (PBC) | — |
| Group admin | SCR-P21-20 | **`W-GROUP`**, `W-APPROVALS-ME` | `W-NBA` | — |

### AG.6.3 Personalisation rules (AG-SCR-08)

1. Users may hide non-mandatory widgets, reorder, resize (S, M, L) and add widgets from their role's catalogue; maximum 12 widgets per dashboard; layouts saved in `core.dashboard_layouts` (Appendix S) or `ops.ws_dashboard_layouts` (Appendix X) by plane.
2. Tenant admins (T) may set the default layout per role and add tenant-mandatory widgets; they cannot remove platform-mandatory widgets (L) or add a widget a role may not see (`CFG_WIDGET_NOT_PERMITTED`). Hiding a mandatory widget fails with `CFG_WIDGET_MANDATORY`.
3. "Reset to default" restores the current tenant default; layout changes are versioned with 30-day history.
4. Widget data requests run in parallel with a 1.5 s budget each; a slow widget renders a skeleton then an inline "Couldn't load — retry" state without blocking others. Mobile dashboards make ≤ 4 API calls on open (FR-P12-V2-05).
5. Shared dashboards across group companies follow Appendix AD §AD.7 (aggregates; grant needed for drill-down).

### AG.6.4 Next-best-action rules (`cfg.nba_rules`; deterministic, never AI-decided)

**Engine rules.** Rules are data (trigger predicate over read models or an event; suggestion text key; one-click action = a palette command with parameters; guard; priority; cooldown). The panel shows at most **3** suggestions ordered by priority then due date. Each can be done, snoozed (24 h) or dismissed with a reason (cooldown 7 days per object). **Locked guards (L):** no suggestion gives legal advice on merits, predicts an outcome or values a claim (NN-01); no suggestion selects, ranks or recommends a neutral (NN-03); no suggestion upsells inside a case, statutory or grievance flow (NN-29); no suggestion uses sealed data. Rule changes are T-tier for tenant rules (with a preview against last 30 days showing how many users would see them) and platform-maintained for the seed below. The AI copilot panel (SCR-P11-13) is separate, labelled, and may only propose; NBA is the deterministic layer.

| Rule ID | Role | Trigger | Suggestion | One-click action |
|---|---|---|---|---|
| NBA-PTY-01 | Party | Response due ≤ 7 days and draft not submitted | "Your response is due on {date} ({n} days)." | Continue response (SCR-P02-07) |
| NBA-PTY-02 | Party | Fee invoice due ≤ 3 days | "Pay {amount} including GST by {date} to keep your filing on track." | Pay (SCR-P12-13 / SCR-P05-02) |
| NBA-PTY-03 | Party | Session within 24 h and device check not done | "Check your camera and microphone before {time}." | Run pre-check (SCR-P12-10) |
| NBA-PTY-04 | Party | Settlement or award awaiting my signature | "A document is waiting for your signature." | Open signing room (SCR-P06-07) |
| NBA-REP-01 | Representative | Authority expires ≤ 14 days on an active matter | "Your authority for {case} ends on {date}." | Request renewal (SCR-P01-25) |
| NBA-REP-02 | Representative | Offer above my authority limit awaiting client | "Your client must approve this offer." | Send to client for approval |
| NBA-NEU-01 | Neutral | Appointment offer expires ≤ 24 h | "Respond to the appointment offer by {time}." | Open disclosure and decide (SCR-P03-13) |
| NBA-NEU-02 | Arbitrator | s.29A mark ≤ 60 days and no extension record | "{case} reaches the 12-month mark on {date}." | Open s.29A cockpit (SCR-P02-94) |
| NBA-NEU-03 | Neutral | Disclosure renewal due ≤ 14 days | "Renew your disclosure statement." | Open disclosure form |
| NBA-CHM-01 | Chambers owner | Pay run in `submitted` ≥ 24 h | "The {month} pay run is waiting for your approval." | Open pay run (SCR-P20-23) |
| NBA-CHM-02 | Chambers owner | Enquiry unacknowledged past SLA | "{n} enquiries have not been acknowledged." | Open enquiries (SCR-P20-09) |
| NBA-CM-01 | Case manager | Statutory clock owned by me turns red | "{case}: {clock} is due on {date}." | Open clocks cockpit filtered (SCR-P02-11) |
| NBA-CM-02 | Case manager | Notice undelivered on all channels ≥ 48 h | "Service failed for {case}. Consider another channel or speed post." | Open notice composer (SCR-P02-12) |
| NBA-CM-03 | Case manager | Session ≤ 2 working days without registry note | "Generate the registry note for {session}." | Generate note (SCR-P02-89) |
| NBA-REG-01 | Registrar | Unowned statutory clock exists | "{n} clocks have no owner. Closure is blocked." | Assign owners (SCR-P02-11) |
| NBA-REG-02 | Registrar | Challenge filed and timeliness check pending | "Decide timeliness for challenge {ref}." | Open challenge file (SCR-P04-09) |
| NBA-ENT-01 | Enterprise admin | Bulk batch validated and not committed ≥ 24 h | "Batch {id} is validated. Commit or abort." | Open batch (SCR-P09-06) |
| NBA-ENT-02 | Enterprise admin | Instalment overdue ≥ 7 days on a compliance tracker | "{n} instalments are overdue." | Open compliance (SCR-P06-64) |
| NBA-GRO-01 | Grievance officer | Ticket at T-3 of regulator clock | "{n} tickets reach the regulator deadline in 3 days." | Open next ticket (SCR-P09-12) |
| NBA-GRO-02 | Grievance officer (Equator) | Acknowledgement due ≤ 12 h | "Acknowledge {n} grievances today." | Bulk acknowledge with template (SCR-P16-27) |
| NBA-OPS-01 | Ops director | Approval awaiting me ≥ 2 working days | "{n} approvals have waited more than 2 days." | Open inbox, approvals filter |
| NBA-OPS-02 | Ops director | Grievance breach count > 0 this month | "Grievance breaches this month: {n}." | Open grievance desk breached view |
| NBA-ONB-01 | Onboarding | Project RAG turns red | "{project} is at risk: {reason}." | Open project (SCR-P16-19) |
| NBA-ONB-02 | Onboarding | Go-live date ≤ 5 days and sign-off pack incomplete | "Complete the sign-off pack for {project}." | Open sign-off (SCR-P16-20) |
| NBA-CSM-01 | CSM | Renewal ≤ 90 days and no renewal opportunity | "Create the renewal for {account} ({date})." | Create renewal opportunity |
| NBA-CSM-02 | CSM | Health score drops ≥ 15 points in 30 days | "{account} health fell from {a} to {b}." | Start at-risk playbook |
| NBA-SUP-01 | Support lead | ≥ 5 tickets breaching ≤ 60 min in one queue | "{queue}: {n} tickets breach within an hour." | Reassign in bulk (AG.7.3) |
| NBA-SUP-02 | Support lead | Unassigned tickets older than first-response target | "{n} tickets are unassigned past target." | Run auto-assignment |
| NBA-MKT-01 | Marketing manager | Scheduled item uses a claim expiring ≤ 7 days | "{n} scheduled items use a claim that expires on {date}." | Open held items |
| NBA-MKT-02 | Marketing manager | Publication evidence overdue | "Record publication evidence for {n} items." | Open publications (SCR-P17-10) |
| NBA-HR-01 | HR manager | Exit with F&F clock ≤ 2 working days | "F&F for {employee} is due on {date}." | Open F&F (SCR-P18-32) |
| NBA-HR-02 | HR manager | Registration or licence expiring ≤ 30 days | "{registration} expires on {date}." | Open entities (SCR-P18-01) |
| NBA-PAY-01 | Payroll checker | Pay run submitted and variance > threshold | "Review {n} variances before approving." | Open variance review (SCR-P18-29) |
| NBA-PAY-02 | Payroll checker | Statutory payment due ≤ 3 days | "{challan} is due on {date}." | Open statutory outputs (SCR-P18-30) |
| NBA-DH-01 | Department head | Team member's queue ≥ 150 % of capacity for 3 days | "{team} is over capacity." | Open capacity view (SCR-P18-23) |
| NBA-DH-02 | Department head | Requisition approved but unfilled ≥ 45 days | "Requisition {id} is still open." | Open requisition |
| NBA-EMP-01 | Employee | Not clocked in by shift start + 30 min (shift workers) | "You have not clocked in today." | Clock in (SCR-P18-17) |
| NBA-EMP-02 | Employee | Mandatory acknowledgement or declaration due | "Please acknowledge {policy} by {date}." | Open acknowledgement |
| NBA-AUD-01 | Auditor | Grant ends ≤ 7 days with open PBC items | "Your access ends on {date}; {n} requests are open." | Open requests |
| NBA-GRP-01 | Group admin | Cross-company grant expires ≤ 14 days | "{n} grants expire soon." | Open grants (SCR-P21-21) |
| NBA-GRP-02 | Group admin | Wall attestation overdue | "{n} people have not completed the annual wall attestation." | Send reminder (SCR-P21-23) |

---

## AG.7 Workflow pattern library (`packages/patterns`; R-72)

Each pattern is a UI component set plus a backend contract. Phases cite the pattern ID in their screen tables; deviations need an ADR. Common to all: problem+json errors with `code` and `traceId`; Idempotency-Key on creating POSTs; audit event per state change; mandatory empty, loading, error, success, read-only and sealed states (Appendix C §A.3).

| ID | Pattern | UI | States | Backend contract | Rules |
|---|---|---|---|---|---|
| PAT-01 | **Wizard with save-and-resume** | Stepper (≤ 7 steps; each a URL), "Check your answers" page, autosave indicator | `draft → in_progress → review → submitted`; `expired` | `POST /drafts` → `PATCH /drafts/{id}` (autosave ≤ 10 s, `If-Match`) → `POST /drafts/{id}:submit` | Drafts kept 90 days (T 30–180) with reminder at day 7 and 3 days before expiry; resume from any device; pinned schema version shown in footer (NN-21); data pre-filled from earlier answers (WCAG 3.3.7); validation per step, ErrorSummary on submit |
| PAT-02 | **Maker-checker approval** | Request form with diff and reason → inbox item → decision panel with diff, validation, preview, impact, citations | `draft → submitted → approved | rejected | withdrawn | expired` | Owner engine (`core.config_change_requests` or `ctl.approval_requests`, X-56); decision `POST …:approve` with step-up | Maker ≠ checker (`MAKER_CHECKER_SAME_USER`); approval SLA per source (default 2 working days) then escalation (PAT-13); request expires after 14 days (T) and the maker is told; WYSIWYS summary with digest; reason mandatory on reject |
| PAT-03 | **Bulk action with preview and undo window** | Select rows → "Preview changes" (counts, sample of 10, exclusions with reasons) → confirm → job monitor (AG-SCR-19) | `previewed → queued → running → completed | partially_failed | undone` | `POST /bulk-jobs` (dry run first, returns `previewId`), `POST /bulk-jobs/{id}:commit`, `POST /bulk-jobs/{id}:undo` | Reversible bulk actions (assign, tag, status within T, reminder scheduling) have an undo window of 10 minutes (T 5–30); sent messages, served notices and money actions are not bulk-undoable and require PAT-16 confirmation; per-row result file (CSV); limit 5,000 rows per job (T up to 20,000 for staff) |
| PAT-04 | **SLA queue with deadline-aware ordering** | Queue list with SLA chips, "Next" button, filters, saved views, load indicator | item: `new → assigned → in_progress → waiting (paused with reason) → done` | Order key of AG.4.4; `POST /queues/{id}:next` assigns atomically (`SELECT … FOR UPDATE SKIP LOCKED`) | SLA pauses only with a reason from a fixed list (awaiting customer, awaiting third party, legal hold) and never for statutory clocks (L); "Next" skips items the user may not take (conflict, wall, language); round-robin and skill routing per queue (T) |
| PAT-05 | **Kanban pipeline** | Columns by stage, card counts and value, drag with keyboard alternative ("Move to…" menu), stage-gate modal | stage list per pipeline | `POST /items/{id}:move {toStage}` validates gates | Gate failures show what is missing; drag never the only way (WCAG 2.5.7); WIP limits per column (T) warn, never block; moving back records reason |
| PAT-06 | **Timeline and case history** | Ordered list with filters (who, kind, date), expandable entries, "jump to date" | — | Read model from audit/outbox events; `GET /…/timeline?cursor=` | Each entry shows actor role (not personal names to parties where policy hides them), time in IST and viewer zone, evidence links; public timeline uses public-safe events only (Appendix C §G) |
| PAT-07 | **Calendar and scheduling with time zones** | Month/week/agenda views; slot finder showing each participant's local time; holiday overlays | slot: `proposed → held (TTL) → confirmed → rescheduled | cancelled` | `POST /slots:find`, `POST /holds` (TTL 15 min), `POST /bookings` | Store UTC, display viewer zone plus participant zones ("10:30 IST / 09:00 GST"); working-day logic from forum calendars; contact windows enforced for borrower-facing reminders (NN-12); ICS titles carry case number only; daylight-saving changes re-validated nightly for INT matters |
| PAT-08 | **Document review, annotate and approve** | Viewer with page thumbnails, comments anchored to text or page area, version compare, approve/request changes | `draft → in_review → changes_requested → approved → locked` | Annotations as separate records (never alter the original, NN-32); approval writes a hash of the reviewed version | Approval applies to a specific version hash; a new version resets approvals; watermark on sensitive documents; comments visible per audience (internal / party) chosen explicitly |
| PAT-09 | **E-sign ceremony** | Pre-sign summary (what, who, hash prefix, IT Act s.3A statement), signer order, provider hand-off, return page | envelope: `prepared → sent → partially_signed → completed | declined | expired | voided` | `ESIGN_PORT`; webhook inbox; evidence ledger entry | Excluded instruments blocked (NN-08); step-up before sign; reminders at 48 h and 24 h before expiry; void requires reason and notifies all signers; signed PDF verifiable (SCR-P06-12) |
| PAT-10 | **Payment and checkout** | Quote breakdown with GST, payer, UPI intent first, hosted checkout, status polling, receipt | `quoted → initiated → pending → captured | failed | expired → refunded` | `PAYMENTS_PORT` hosted pages only (NN-31); idempotent order create; webhook reconciliation | Price shown before any personal data beyond what is needed (S §5 rule 3); retry never double-charges; "Paid" shown only after capture confirmation; failure states give the reason and a next step |
| PAT-11 | **Import with mapping preview** | Template download → upload → column mapping (auto-suggested, editable) → dry-run report per row → approval (for G imports) → commit → reconciliation | `uploaded → mapped → validated → approved → committing → committed | rolled_back` | `POST /imports`, `PUT /imports/{id}/mapping`, `POST …:dry-run`, `POST …:commit`, `POST …:rollback` | Dry run mandatory; duplicates and consent conflicts listed; people, case and money imports are G (TC); rollback available until dependent records exist; reconciliation counts must match before close (SCR-P21-11) |
| PAT-12 | **Export package request** | Scope picker filtered by role → layout and destination → redaction profile → preview of folders and counts → approval if sensitive → progress → certificate | `requested → approved → building → ready → downloaded | expired` | `xpt` (App. AC §AC.13; `EQ-EXPORT-1.0`) | Sensitive scopes need a checker (NN-36); links expire (T, default 7 days); free at exit (NN-37); manifest with checksums |
| PAT-13 | **Escalation ladder** | Escalation chip on items ("Level 2 — Head of Support since 14:10"), ladder view per policy | `L0 → L1 → L2 → L3` | Temporal timer per item and policy (`cfg` SLA policies) | Levels and times are T above statutory floors; level 3 mandatory for statutory clocks (L, V §V.4.1); each escalation notifies the next owner and the previous owner; de-escalation on action |
| PAT-14 | **Exception handling** | Exception list with severity, owner, age, linked object; resolve with reason; accept risk with expiry | `open → acknowledged → resolved | risk_accepted (expiry) → reopened` | `ctl.exceptions` or source equivalent | Every override of a control is an exception with reason (NN-36); risk acceptance needs an approver above the owner and expires (≤ 12 months); expired acceptances reopen automatically |
| PAT-15 | **Empty, error and loading states** | EmptyState (one sentence + one button), Skeleton (no spinners > 1 s without text), InlineAlert with `code` + `traceId`, offline banner | — | Problem+json catalogue (App. F) and microcopy `emp`, `err` (App. P §4.3, §4.6) | Never blank; preserve entered data on error; retry with backoff for idempotent reads; "stale" state when data older than refresh interval |
| PAT-16 | **Undo and confirmation for irreversible actions** | Reversible: toast "Done · Undo" (10 s) and the AG-SCR-27 tray; irreversible: confirmation **screen** (not a checkbox in a modal) stating what will happen, to whom, and that it cannot be undone, with context line and step-up | — | Reversible actions are soft (pending commit for the undo window, then outbox); irreversible actions commit immediately after confirmation | Irreversible list (L): serve a notice, sign, pay, release escrow, approve payroll or payment, publish an outcome, submit a filing, send a mass message, delete data after cooling-off, revoke a representative's authority. Typing the object's reference is required for destructive deletes and mass sends; confirmations announce via `aria-live` |

---

## AG.8 Menu and terminology customisation, tours and help

### AG.8.1 What tenants may change (AG-SCR-07)

| Element | Rename | Hide | Reorder | Add | Tier and who |
|---|---|---|---|---|---|
| Side-nav items and groups (unlocked) | Yes, per locale, glossary-linted | Yes (for all roles or per role) | Yes, within the group | — | T; tenant admin (unit admin for own unit's ops workspace) |
| Custom link items | Yes | Yes | Yes | Up to 10 per shell: internal route or an allow-listed HTTPS domain (`tenant.nav.custom_link_domains`); opens in the same tab for internal, new tab with "opens {domain}" label for external | T; tenant admin. A link to another domain fails with `CFG_NAV_CUSTOM_LINK_DOMAIN` |
| Dashboard defaults per role | — | Non-mandatory widgets | Yes | From the role catalogue | T (AG.6.3) |
| Status labels (case) | Yes, 1:1 to canonical states | No | No | No | T with glossary lint (V §V.4.1 `case.status_labels`); pinned once used in a served notice |
| Terminology (`cfg.terminology`: e.g., "Matter" for "Case", "Desk" for "Queue", "Client" for "Party" in chambers) | Yes | — | — | — | T for operational nouns; G (TLR) for any term that appears in legal templates or notices |
| Mobile tabs | No (slots fixed per persona) | No | Users only (slots 2–4) | No | User preference |
| Tours and checklists | Text and order | Optional steps | Yes | Tenant-specific steps (≤ 10) | T |
| Locked items | No | No | No | — | L |

**Preview as role.** AG-SCR-07 renders the resolved menu for any role and context the admin may see, with a diff against the platform default; publishing an override set is a change set with history and one-click rollback (V §V.5). Overrides never change permissions: hiding an item does not revoke access to its route.

### AG.8.2 Locked (L) items and labels

Help; Contact support; Grievance Officer and grievance or complaint routes (including "Complaints about Equator" and marketplace "Report a listing"); Privacy centre and consents; Accessibility statement; Legal notices (terms, privacy notice, cookies, disclaimer); Work Inbox; Sign out and "Sign out everywhere"; QuickExit; the fixed "Sponsored — paid placement. Does not affect Equator appointments." label and the Marketplace separation note (NN-34); the "Equator is not a court" identity line where Appendix P requires it; the free-forum signpost widget on party homes (NN-20); the enterprise neutrality banner; My data and disputes for employees (NN-35); footer legal-entity line and CIN. Their labels may be translated only through approved catalogues and may not be renamed by tenants (`CFG_NAV_ITEM_LOCKED`).

**Glossary lint (L).** Labels and terminology overrides are linted with Appendix P LINT rules: no "court", "judge", "decree", "judgment" for Equator; no "guaranteed", "win", "best neutral"; no regulator names implying endorsement; violations fail with `CFG_NAV_LABEL_PROHIBITED`.

### AG.8.3 Localisation of menu labels

1. Labels are keys (`nav.{shell}.{item}`) in i18n catalogues; English and Hindi ship at launch; other enabled locales follow NN-23. A missing translation falls back to English with `lang="en"` on the element so screen readers switch voice.
2. Tenant label overrides are stored per locale; an override in one locale does not overwrite others; the editor shows all enabled locales side by side and warns when a locale is missing.
3. Labels that are legal terms (e.g., "Award", "Settlement agreement", "Statement of claim") use glossary-approved translations only (legal-translator review, Appendix C §H.4).
4. Urdu renders RTL with mirrored side nav and chevrons; icons with direction meaning (back, next) mirror; numerals follow the locale setting.
5. Label length budget: side-nav ≤ 24 characters (en) with wrapping allowed to two lines; tabs ≤ 16 characters; truncation only with a tooltip and full text available to assistive technology.

### AG.8.4 Onboarding checklists and tours (AG-SCR-10)

| Persona | Checklist (first-run; progress shown on home until done or dismissed) | Tour (≤ 5 steps, skippable, replay from Help) |
|---|---|---|
| Party | Verify mobile · choose notice language · add a representative (optional) · set notification channels | Home → case card → Inbox → Pay → Help |
| Representative | Verify enrolment · accept pending authorities · set calendar feed · set digest | Matters → client switcher → Filings due → Inbox |
| Neutral | Complete profile consents · set availability · tax and bank profile · disclosure template | Today → offers → calendar → drafting |
| Chambers owner | Brand and site · domain · rules and fees · staff invitations · invoicing profile · payroll compliance wizard (if HR add-on) | Home → website → staff → settings approvals |
| Enterprise admin | SSO · users and units · clause adoption · bulk template · SLA policies · API key | Dashboard → bulk intake → inbox → settings |
| Grievance officer | GRO profile · complainant portal · templates · regulator MIS contacts | Desk inbox → ticket → reports |
| Ops staff (any department) | Confirm profile and skills · set working hours · Away settings · pin top queues | Department rail → queue → inbox → palette (`Ctrl/Cmd+K`) |
| Employee | Read the workforce-measurement notice (NN-35) · bank and tax declarations · emergency contact · first clock-in | Me → Time → Leave → Pay → My data |
| Auditor | Confirm engagement scope · read watermark notice · first PBC review | Engagement home → evidence → requests |
| Group admin | Entities register · group templates and locks · GDSA register · grant templates | Group overview → grants → walls |

Rules: tours never block a task, never cover the primary action, respect `prefers-reduced-motion` (no animated spotlight), are keyboard-operable with focus moved to each step and returned on close, and are recorded only as `tour.step_viewed`/`tour.completed` events (AG.9.3). Checklist items complete automatically from domain events (e.g., the SSO test-sign-in result recorded by SCR-P01-30).

### AG.8.5 In-app help (AG-SCR-12)

Every `cfg.nav_items` row and every screen has a `help_article_key`; the Help panel opens the article for the current route (KB space `public_help` for customer shells, `internal` for workforce), followed by "Contact support", "Keyboard shortcuts", "What's new" (AG-SCR-16) and "Report a problem" (pre-fills route template, app version and `traceId`, never page content). CI warns when a published route has no article (`NAV_HELP_MISSING`); P16 KB review dates apply.

---

## AG.9 Accessibility, performance, analytics and usability KPIs

### AG.9.1 Accessibility for navigation (WCAG 2.2 AA floor, NN-23)

1. **Landmarks:** `header`, `nav` (labelled "Main", "Section", "Breadcrumb"), `main`, `aside`, `footer`; one H1 per page.
2. **Keyboard order:** skip links → header (logo, context chip, search, inbox, help, me) → side nav → main → drawer. Side nav is a list of links (not `role="menu"`); disclosure groups use `aria-expanded`. Mega-menus follow the disclosure navigation pattern; `Esc` closes and returns focus to the trigger.
3. **Focus:** visible 2 px teal ring with 2 px offset (Appendix C §E.1), never removed; sticky headers never obscure the focused element (SC 2.4.11); focus moves to the H1 after route change and the new page title is announced via a polite live region.
4. **Targets:** ≥ 24 × 24 CSS px (SC 2.5.8); 44 × 44 on touch.
5. **Drag alternatives** for tab editing, dashboard layout and kanban (SC 2.5.7).
6. **Consistent help** in the same place on every page (SC 3.2.6); consistent navigation order across pages of a shell (SC 3.2.3).
7. **Reduced motion:** with `prefers-reduced-motion`, no slide or fade on drawers, tours or menus (instant state change).
8. **Badges and SLA chips** carry text; colour is never the only cue (SC 1.4.1); contrast per Appendix C tokens.
9. **Zoom and reflow:** 200% text and 320 CSS px width without horizontal scrolling for menus and inbox (SC 1.4.10); side nav collapses to the drawer.
10. **Screen-reader scripts** extended to: switch context, find and act on an inbox approval, use the palette, edit mobile tabs.

### AG.9.2 Performance budgets for shells

| Shell | Shell JS (gzip, excluding page) | Menu resolve (server p95) | Inbox count (p95) | Palette open to first results (p95) | First load LCP (4G) |
|---|---|---|---|---|---|
| `public` | ≤ 70 KB (mega-menu ≤ 12 KB, works without JS as plain links) | static | — | — (site search ≤ 500 ms) | < 2.5 s |
| `party`, `representative` | ≤ 120 KB | ≤ 80 ms | ≤ 150 ms | ≤ 300 ms | < 2.5 s (3G < 5 s) |
| `neutral`, `chambers`, `enterprise`, `console` | ≤ 150 KB | ≤ 80 ms | ≤ 150 ms | ≤ 300 ms | < 2.5 s |
| `ops`, `selfservice`, `admin`, `assurance` | ≤ 180 KB | ≤ 100 ms | ≤ 200 ms (federated) | ≤ 350 ms | < 3.0 s |
| Mobile native | Tab switch ≤ 100 ms; cold start to interactive home ≤ 3 s on a 2 GB-RAM Android device | cached menu (24 h) refreshed in background | ≤ 150 ms | ≤ 300 ms | — |

A budget breach fails the `perf-budget` CI check (Lighthouse CI for web, Maestro timing for mobile).

### AG.9.3 Navigation analytics (privacy-safe)

Events (first-party, through `ANALYTICS_PORT`; disclosed in the privacy notice; product analytics for signed-in users can be switched off in Privacy settings; public site only after cookie consent, SCR-P13-49):

| Event | Properties (exhaustive) |
|---|---|
| `nav.item_clicked` | shell, item_code, position, source (`sidenav`, `tab`, `megamenu`, `palette`, `pinned`, `dashboard`, `nba`), role_class, device_class |
| `nav.search_performed` | shell, query_length, result_bucket (`0`, `1–5`, `6–20`, `>20`), object_types[], clicked_rank, time_to_click_ms |
| `nav.palette_command` | shell, command_code, invoked_by (`keyboard`, `click`) |
| `nav.context_switched` | from_shell, to_shell, reason |
| `nav.deeplink_opened` | route_template, src, outcome (`landed`, `switched`, `denied`, `expired`) |
| `nav.dead_end` | route_template, code (`403`, `404`, `410`), referrer_kind |
| `inbox.item_actioned` | source, kind, action, age_bucket, via (`panel`, `bulk`, `mobile`) |
| `task.completed` | task_code (AG.9.4), clicks, screens, duration_ms, success |
| `tour.step_viewed` / `tour.completed` | tour_code, step |

**Never collected:** user, tenant or case IDs in analytics (a rotating daily pseudonymous session ID only); query text; page content; URLs with IDs (route templates only); anything from sealed shells (POSH sub-shell, caucus notes, IC) or screens marked sealed (Appendix C §A.4). Reports apply k ≥ 10 suppression. Raw events kept 13 months, aggregates indefinitely.

### AG.9.4 Usability KPIs and the top-20 task budget

**Programme KPIs:** task completion ≥ 90% unassisted in moderated tests (8 participants per persona per release train, including at least 2 screen-reader users and 2 Hindi-first users); SUS ≥ 75 for party and representative, ≥ 70 for workforce shells; search-to-click success ≥ 70%; dead-end rate (`nav.dead_end` per 1,000 page views) ≤ 2; inbox approval median time-to-decision ≤ 1 working day; palette adoption ≥ 30% of weekly active workforce users by month 3.

**Clicks-to-complete** counts clicks or taps from the stated start point to the final confirmation, excluding typing and step-up; measured by the `ux.click_budget` Playwright lint (Appendix S §5) and `task.completed` events.

| # | Task | Persona | Start point | Target clicks | Target screens |
|---|---|---|---|---|---|
| 1 | Respond to a notice | Respondent | SMS deep link | ≤ 6 | ≤ 5 |
| 2 | Pay a fee | Party | Inbox or dashboard | ≤ 4 | ≤ 3 |
| 3 | Sign a settlement | Party | Push notification | ≤ 4 | ≤ 3 |
| 4 | Join a session | Party / neutral | Dashboard | ≤ 2 | ≤ 2 |
| 5 | Upload a requested document | Party | Inbox | ≤ 4 | ≤ 2 |
| 6 | File a case (after Explorer report) | Party | Report CTA | ≤ 12 | ≤ 7 |
| 7 | Accept an appointment offer with disclosure | Neutral | Inbox | ≤ 6 | ≤ 3 |
| 8 | Issue a procedural order from a template | Arbitrator | Case Desk | ≤ 8 | ≤ 4 |
| 9 | Assign an owner to an unowned clock | Registrar | Dashboard | ≤ 3 | ≤ 2 |
| 10 | Take the next scrutiny item and accept it | Case manager | Queue | ≤ 5 | ≤ 2 |
| 11 | Approve a settings change (G) | Checker | Inbox badge | ≤ 4 | ≤ 2 |
| 12 | Approve a pay run | Payroll checker | Inbox | ≤ 5 | ≤ 3 |
| 13 | Commit a validated bulk batch | Enterprise operator | Dashboard | ≤ 4 | ≤ 3 |
| 14 | Respond to a grievance ticket from a template | Grievance officer | Desk inbox | ≤ 5 | ≤ 2 |
| 15 | Convert a lead to an opportunity | Sales executive | Lead list | ≤ 4 | ≤ 2 |
| 16 | Resolve a support ticket with a macro | Support agent | Next ticket | ≤ 4 | ≤ 1 |
| 17 | Request leave | Employee | Me home (mobile) | ≤ 4 | ≤ 2 |
| 18 | Clock in | Employee | App open | ≤ 1 | ≤ 1 |
| 19 | Switch to another company and open its queue | Group staff | Any page | ≤ 3 | ≤ 1 |
| 20 | Request a full data export | Tenant admin | Settings | ≤ 6 | ≤ 4 |

A task that misses its target by more than 50% in two consecutive releases opens a UX defect with priority P2.

---

## AG.10 Data model, APIs, events, errors and acceptance tests

### AG.10.1 Tables (DDL sketches; Appendix F conventions; UUIDv7; tenant RLS unless stated)

```sql
-- Navigation registry (platform rows; tenants never write) — D3-45
CREATE TABLE cfg.nav_menus (
  menu_code text PRIMARY KEY,                 -- e.g. 'party.sidenav', 'ops.rail', 'public.megamenu', 'mobile.party.tabs'
  shell text NOT NULL, surface text NOT NULL CHECK (surface IN ('sidenav','rail','megamenu','tabs','more_sheet','palette','quick_actions','settings_rail','footer')),
  version int NOT NULL, status text NOT NULL CHECK (status IN ('draft','published','retired')),
  min_app_release text, published_by uuid, approved_by uuid, published_at timestamptz,
  CHECK (approved_by IS NULL OR approved_by <> published_by));
CREATE TABLE cfg.nav_items (
  item_code text NOT NULL, menu_code text NOT NULL REFERENCES cfg.nav_menus, menu_version int NOT NULL,
  parent_code text, kind text NOT NULL CHECK (kind IN ('group','link','command','external','divider')),
  sort_key int NOT NULL, label_key text NOT NULL, icon text, route_template text, screen_id text, owning_phase text,
  permissions_all text[] NOT NULL DEFAULT '{}', permissions_any text[] NOT NULL DEFAULT '{}',
  flags text[] NOT NULL DEFAULT '{}', entitlements text[] NOT NULL DEFAULT '{}', tenant_kinds text[] NOT NULL DEFAULT '{}',
  conditions jsonb NOT NULL DEFAULT '{}',     -- e.g. {"space":"arbitration"}, {"vertical_in":["FAM"]}
  badge_source text, shortcut text, help_article_key text, requestable boolean NOT NULL DEFAULT false,
  lock_tier text NOT NULL DEFAULT 'T' CHECK (lock_tier IN ('L','T')), sealed boolean NOT NULL DEFAULT false,
  mobile_tab_eligible boolean NOT NULL DEFAULT false, analytics_code text NOT NULL,
  PRIMARY KEY (menu_code, menu_version, item_code),
  CHECK (kind <> 'link' OR route_template IS NOT NULL), CHECK (kind <> 'external' OR route_template ~ '^https://'));
CREATE TABLE cfg.nav_overrides (               -- tenant/unit customisation (T) and user prefs live separately
  id uuid PRIMARY KEY DEFAULT uuidv7(), scope_id uuid NOT NULL REFERENCES cfg.scopes, menu_code text NOT NULL,
  item_code text NOT NULL, action text NOT NULL CHECK (action IN ('rename','hide','reorder','add_link')),
  role_codes text[] NOT NULL DEFAULT '{}',    -- empty = all roles
  label_i18n jsonb, sort_key int, link_url text, change_set_id uuid REFERENCES cfg.change_sets,
  status text NOT NULL CHECK (status IN ('active','reverted')), created_by uuid NOT NULL, created_at timestamptz NOT NULL DEFAULT now());
CREATE TABLE cfg.terminology (
  scope_id uuid NOT NULL REFERENCES cfg.scopes, term_key text NOT NULL, locale text NOT NULL, value text NOT NULL,
  tier text NOT NULL CHECK (tier IN ('T','G')), change_id uuid, PRIMARY KEY (scope_id, term_key, locale));
CREATE TABLE cfg.user_nav_prefs (
  user_id uuid NOT NULL, shell text NOT NULL, context_hash text NOT NULL,
  pins jsonb NOT NULL DEFAULT '[]' CHECK (jsonb_array_length(pins) <= 8),
  sidenav_collapsed boolean NOT NULL DEFAULT false, mobile_tab_order text[], last_context jsonb,
  PRIMARY KEY (user_id, shell, context_hash));
CREATE TABLE cfg.shortcut_bindings (command_code text PRIMARY KEY, default_keys text NOT NULL, single_key boolean NOT NULL,
  shells text[] NOT NULL, reserved boolean NOT NULL DEFAULT false);
CREATE TABLE cfg.user_shortcuts (user_id uuid NOT NULL, command_code text NOT NULL REFERENCES cfg.shortcut_bindings,
  keys text, disabled boolean NOT NULL DEFAULT false, PRIMARY KEY (user_id, command_code));
-- Dashboards and next best action
CREATE TABLE cfg.widget_catalogue (widget_code text PRIMARY KEY, title_key text NOT NULL, data_endpoint text NOT NULL,
  plane text NOT NULL CHECK (plane IN ('core','business')), roles text[] NOT NULL, min_cohort int NOT NULL DEFAULT 5,
  sealed_allowed boolean NOT NULL DEFAULT false CHECK (sealed_allowed = false), refresh_seconds int NOT NULL, sizes text[] NOT NULL);
CREATE TABLE cfg.dashboard_defaults (scope_id uuid NOT NULL REFERENCES cfg.scopes, dashboard_code text NOT NULL, role_code text NOT NULL,
  layout jsonb NOT NULL, mandatory_widgets text[] NOT NULL, version int NOT NULL, PRIMARY KEY (scope_id, dashboard_code, role_code));
CREATE TABLE cfg.nba_rules (rule_code text NOT NULL, scope_id uuid NOT NULL REFERENCES cfg.scopes, version int NOT NULL,
  role_codes text[] NOT NULL, trigger jsonb NOT NULL,           -- {"event":"…"} or {"query":"<read-model predicate DSL>"}
  suggestion_key text NOT NULL, action_command text NOT NULL, action_params jsonb NOT NULL DEFAULT '{}',
  guards text[] NOT NULL DEFAULT '{NO_MERITS,NO_NEUTRAL_SELECTION,NO_UPSELL_IN_STATUTORY,NO_SEALED}',
  priority int NOT NULL, cooldown_hours int NOT NULL DEFAULT 168, status text NOT NULL, PRIMARY KEY (rule_code, scope_id, version));
-- Views, sources, tours, redirects
CREATE TABLE cfg.view_definitions (view_code text PRIMARY KEY, object_type text NOT NULL, plane text NOT NULL,
  filters jsonb NOT NULL, columns text[] NOT NULL, sort jsonb NOT NULL, roles text[] NOT NULL, deletable boolean NOT NULL DEFAULT false);
CREATE TABLE cfg.inbox_sources (source_code text PRIMARY KEY, owner_module text NOT NULL, plane text NOT NULL,
  kinds text[] NOT NULL, bulk_approvable boolean NOT NULL DEFAULT false, decision_component text NOT NULL,
  default_sla_hours int, escalation_policy text);
CREATE TABLE cfg.tours (tour_code text NOT NULL, scope_id uuid NOT NULL REFERENCES cfg.scopes, shell text NOT NULL, role_codes text[] NOT NULL,
  steps jsonb NOT NULL CHECK (jsonb_array_length(steps) <= 5), checklist jsonb NOT NULL DEFAULT '[]', version int NOT NULL,
  PRIMARY KEY (tour_code, scope_id, version));
CREATE TABLE cfg.tour_progress (user_id uuid NOT NULL, tour_code text NOT NULL, state text NOT NULL CHECK (state IN ('not_started','in_progress','completed','dismissed')),
  checklist_done text[] NOT NULL DEFAULT '{}', updated_at timestamptz NOT NULL DEFAULT now(), PRIMARY KEY (user_id, tour_code));
CREATE TABLE cfg.route_redirects (from_route text PRIMARY KEY, to_route text NOT NULL, reason text NOT NULL, expires_on date NOT NULL);
```

**Per-plane tables (not `cfg`, because they hold user work, D3-46):**

| Table | Plane | Key columns | Notes |
|---|---|---|---|
| `core.inbox_items` | case plane (and any cluster the P15 ADR co-locates) | id, tenant_id, entity_id, user_id or queue_id, source_code, kind, object_type, object_id, source_version, title_key, title_params jsonb (non-sensitive), priority, legal_blocking, sla_state, due_at, status (`open`,`snoozed`,`done`,`dismissed`,`expired`,`delegated`), snoozed_until, snooze_count, delegated_to, actions text[], sealed boolean, created_at, updated_at | Unique `(source_code, object_id, user_id, kind)`; RLS by tenant and user; sealed items carry generic title only; partition by month; done items purged after 90 days |
| `ops.ws_inbox_items` | business database | as above + company_id | RLS `ops_company_isolation` |
| `core.recent_items` · `ops.ws_recent_items` | per plane | user_id, context_hash, object_type, object_id, opened_at | ≤ 20 per context; 30-day TTL; sealed objects rejected by trigger |
| `core.saved_views` (additive) | case plane | `pinned boolean`, `is_default boolean`, `shared_scope text`, `view_code text NULL REFERENCES cfg.view_definitions` | Appendix L table |
| `ops.ws_saved_views` (additive) | business | same additive columns | Appendix X table |
| `core.dashboard_layouts` / `ops.ws_dashboard_layouts` (additive) | per plane | `history jsonb` (30-day versions) | Mandatory widgets enforced server-side |

### AG.10.2 APIs (`/v1`; problem+json; Idempotency-Key on creating POSTs)

| Method and path | Purpose | Auth |
|---|---|---|
| GET `/v1/me/navigation?shell=` | Resolved menu (ETag; ≤ 8 KB gzip) | session |
| GET `/v1/me/navigation/badges?shell=` | Badge counts by `badge_source` | session |
| PUT `/v1/me/navigation/prefs` | Pins, collapsed state, mobile tab order | session |
| GET `/v1/admin/navigation/menus` · POST `…/menus/{code}/versions` · POST `…/versions/{v}:publish` | Platform registry (maker-checker) | `nav:registry:write` / `nav:registry:publish` |
| GET `/v1/tenant/navigation/preview?role=&context=` | Preview as role | `nav:override:write` |
| POST `/v1/tenant/navigation/overrides` (change set) · POST `…/{id}:revert` | Tenant overrides (T) | `nav:override:write` |
| PUT `/v1/tenant/terminology/{termKey}` | Terminology (T or G by key) | `nav:override:write`; G via change request |
| GET `/v1/inbox?view=&source=&kind=&cursor=` | Federated inbox (BFF merges planes) | session |
| GET `/v1/inbox/counts` | Actionable counts per shell (for "Also waiting for you") | session |
| GET `/v1/inbox/items/{id}/view` | Owner-supplied decision view model | session + owner policy |
| POST `/v1/inbox/items/{id}:snooze` · `:done` · `:dismiss` · `:reassign` | Item actions (decisions go to the owner API) | session |
| POST `/v1/inbox/bulk` | Bulk read/snooze/reassign/done; bulk approve only for `bulk_approvable` sources | session |
| PUT `/v1/me/away` · DELETE `/v1/me/away` | Away and per-source delegation | session aal2 |
| GET `/v1/search?q=&types=&cursor=` | Permission-trimmed search in the caller's shell | session |
| GET `/v1/me/palette?q=` | Commands, navigation targets, recents | session |
| GET/PUT `/v1/me/shortcuts` | Shortcut remaps | session |
| GET `/v1/me/views?object=` · POST `/v1/me/views` · PATCH `/v1/me/views/{id}` | Saved views (per plane) | session |
| GET `/v1/me/dashboard/{code}` · GET/PUT `/v1/me/dashboard-layouts/{code}` | Existing (Appendix S §8.2); now include `W-NBA` | session |
| GET `/v1/me/nba?dashboard=` · POST `/v1/me/nba/{ruleCode}/{objectId}:dismiss` | Next-best-action suggestions | session |
| PUT `/v1/tenant/dashboards/{code}/defaults/{role}` | Tenant default layout (T) | `dashboard:default:write` |
| POST `/v1/tenant/nba-rules` · POST `…/{code}:preview` · `:publish` | Tenant NBA rules with 30-day preview | `nba:rule:write` |
| GET `/v1/me/tours` · POST `/v1/me/tours/{code}/progress` | Tours and checklists | session |
| POST `/v1/access-requests` | From a 403 page (AG-SCR-17) | session |
| POST `/v1/bulk-jobs` · `:commit` · `:undo` · GET `/v1/bulk-jobs/{id}` | PAT-03 | per object policy |

New Cerbos permissions: `nav:registry:write`, `nav:registry:publish` (platform; publisher ≠ author), `nav:override:write` (tenant admin; unit admin within unit), `dashboard:default:write`, `nba:rule:write`, `inbox:bulk_approve` (only for `bulk_approvable` sources), `analytics:navigation:read` (AG-SCR-15).

### AG.10.3 Events (CloudEvents; IDs and codes only)

`equator.cfg.nav_menu.published.v1` (menu_code, version) · `equator.cfg.nav_override.changed.v1` (scope_id, menu_code, item_code, action) · `equator.cfg.terminology.changed.v1` (scope_id, term_key, locale) · `equator.cfg.dashboard_default.changed.v1` · `equator.cfg.nba_rule.published.v1` · `equator.cfg.tour.completed.v1` (user_id, tour_code) · `equator.identity.context.switched.v1` (existing P01 event; payload gains `from_shell`, `to_shell`, `reason`) · `equator.identity.access_request.created.v1` / `.decided.v1` · `equator.notifications.inbox_item.created.v1` / `.updated.v1` / `.actioned.v1` (item_id, source_code, kind, action) · `equator.notifications.away.set.v1` / `.cleared.v1` · `equator.cfg.bulk_job.committed.v1` / `.undone.v1`.

### AG.10.4 Error codes (new `CFG_` codes; register in Appendix F §F.10.4; no collision with the 30 existing `CFG_` codes)

| Code | HTTP | Message (en) |
|---|---|---|
| `CFG_NAV_ITEM_LOCKED` | 403 | This menu item is fixed by platform policy and cannot be changed. |
| `CFG_NAV_ROUTE_UNKNOWN` | 422 | This link points to a page that does not exist. |
| `CFG_NAV_DEPTH_EXCEEDED` | 422 | Menus can have at most two levels. |
| `CFG_NAV_LABEL_PROHIBITED` | 422 | This label uses words that are not allowed (for example "court"). |
| `CFG_NAV_CUSTOM_LINK_DOMAIN` | 422 | Links can only go to approved web addresses. |
| `CFG_NAV_TOO_MANY_ITEMS` | 422 | You have reached the limit for this menu ({max}). |
| `CFG_WIDGET_NOT_PERMITTED` | 403 | This widget is not available for this role. |
| `CFG_WIDGET_MANDATORY` | 409 | This widget is required and cannot be hidden. |
| `CFG_DASHBOARD_LIMIT` | 422 | A dashboard can have at most 12 widgets. |
| `CFG_VIEW_SHARE_SCOPE` | 403 | You cannot share this view more widely than your own access. |
| `CFG_VIEW_FILTER_FORBIDDEN` | 422 | This view uses a field that cannot be filtered. |
| `CFG_SHORTCUT_CONFLICT` | 409 | This shortcut is already used by "{command}". |
| `CFG_SHORTCUT_RESERVED` | 422 | This key combination is reserved by the browser or assistive technology. |
| `CFG_INBOX_ACTION_STALE` | 409 | This item changed since you opened it. Please review it again. |
| `CFG_INBOX_DELEGATION_NOT_ALLOWED` | 403 | This person cannot act on these items for you. |
| `CFG_INBOX_SNOOZE_LIMIT` | 422 | This item cannot be snoozed again. |
| `CFG_INBOX_BULK_NOT_ALLOWED` | 422 | These items must be decided one at a time. |
| `CFG_CONTEXT_SWITCH_DENIED` | 403 | You cannot switch to this organisation or role. |
| `CFG_DEEPLINK_EXPIRED` | 410 | This link has expired. Sign in to continue. |
| `CFG_DEEPLINK_CONTEXT_MISMATCH` | 409 | This link is for another account or role. |
| `CFG_NBA_GUARD_VIOLATION` | 422 | This suggestion rule breaks a platform guard ({guard}). |
| `CFG_BULK_UNDO_WINDOW_CLOSED` | 409 | The undo window for this action has closed. |

*v3.1:* `CFG_BULK_UNDO_WINDOW_CLOSED` is the generic PAT-03 bulk-job code (`tenant.bulk.undo_window_minutes`). Settings change sets use Appendix V's `CFG_UNDO_WINDOW_EXPIRED` (`tenant.cfg.bulk.undo_minutes`); the two are distinct codes, not aliases (V §V.6.4).

### AG.10.5 Settings and flags registered by this appendix

| Key | Tier | Default | Bounds / rule | Who |
|---|---|---|---|---|
| `platform.nav.menu_version.<shell>` | G (platform) | latest published | Publisher ≠ author | product owner |
| `tenant.nav.overrides` | T | none | Locked items untouchable; ≤ 10 custom links per shell | tenant admin |
| `tenant.nav.custom_link_domains` | T | none | HTTPS only; no URL shorteners | tenant admin |
| `tenant.nav.terminology` | T / G | platform glossary | G when used in legal templates (TLR) | tenant admin |
| `tenant.inbox.away_escalation_hours` | T | 8 working hours (P1: 1 h) | 1–24 | tenant admin |
| `tenant.inbox.approval_request_expiry_days` | T | 14 | 3–30 | tenant admin |
| `tenant.bulk.undo_window_minutes` | T | 10 | 5–30 | tenant admin |
| `tenant.bulk.max_rows` | T | 5,000 | ≤ 20,000 (staff) | tenant admin |
| `tenant.drafts.retention_days` | T | 90 | 30–180 | tenant admin |
| `tenant.dashboards.defaults.<code>.<role>` | T | AG.6.2 | Platform-mandatory widgets kept (L) | tenant admin |
| `tenant.nba.rules` | T | AG.6.4 seed | Guards L | tenant admin |
| `user.inbox.max_snoozes` | T (user) | 3 | 1–5 | user |
| `user.inbox.digest_time` | T (user) | 08:30 local | — | user |
| `user.ui.single_key_shortcuts` | T (user) | ON workforce / OFF party and representative | — | user |
| `platform.analytics.navigation.enabled` | G | ON for workforce shells; ON for customer shells only with the privacy-notice version that discloses it | Sealed shells never | DPO |

### AG.10.6 Acceptance tests (Gherkin; `tests/acceptance/appendix-AG.feature`)

```gherkin
Feature: Navigation registry and resolver (D3-45)
  Scenario: Item hidden when flag is OFF and route returns 404
    Given flag "marketplace.paid_placement" is OFF
    When a neutral eligible for sponsorship loads the neutral menu
    Then the item "Sponsorship" is absent
    And GET "/provider/sponsorship" returns 404 with code "NOT_FOUND"

  Scenario: Entitlement missing hides the item without upsell in a case
    Given the tenant plan lacks entitlement "campaigns"
    When an enterprise operator opens a case
    Then no "Campaigns" item or upgrade prompt is shown
    And the tenant admin sees "Available on Business" only in Settings → Plan and billing

  Scenario: Locked item cannot be hidden
    When a tenant admin submits an override hiding "Help"
    Then the response is 403 with code "CFG_NAV_ITEM_LOCKED"

  Scenario: Menu is not security
    Given a user without permission "crm.merge"
    When the user requests "/crm/duplicates" directly
    Then the response is 403 with code "FORBIDDEN"
    And CI test "NAV_ROUTE_GUARDED" lists no unguarded registered route

Feature: Unified Work Inbox (D3-46)
  Scenario: Approvals from two planes appear in one ordered list
    Given a payroll run approval in "ctl" due today and a settings change in "cfg" due in 3 days
    When the payroll checker opens the inbox
    Then both items appear under "Approvals" with the payroll run first
    And no SQL statement joins tables across clusters

  Scenario: Maker cannot approve via delegation
    Given Asha created payee change P and Ravi delegated approvals to Asha
    When Asha opens P from Ravi's delegated items and approves
    Then the response is 409 with code "MAKER_CHECKER_SAME_USER"

  Scenario: Bulk approve refused for money items
    When a checker selects 3 refund approvals and chooses "Approve all"
    Then the response is 422 with code "CFG_INBOX_BULK_NOT_ALLOWED"

  Scenario: Statutory item cannot be snoozed past T-24h
    Given an owned statutory clock item due in 30 hours
    When the owner snoozes it until tomorrow 18:00 (beyond T-24h)
    Then the snooze is capped at T-24h and the user is told why

  Scenario: POSH items are content-free outside the sealed workspace
    Given an IC member has a new POSH complaint task
    Then the inbox title is "You have an update in the IC workspace"
    And the item has no case number, category or name

Feature: Search and palette
  Scenario: Sealed data is never found
    Given sealed POSH and health records containing the word "Sharma"
    When any role searches "Sharma"
    Then no sealed record is returned and the counts exclude them

  Scenario: Single-key shortcuts can be turned off
    Given the user turns off single-key shortcuts
    When the user presses "G" then "I" outside a text field
    Then nothing happens and "Ctrl/Cmd+K" still opens the palette

Feature: Context switching and deep links
  Scenario: Deep link switches company with an undo banner
    Given Neha holds roles in Equator and Finbyx and is in the Equator context
    When she opens a deep link for a Finbyx task
    Then the context switches to Finbyx and a banner offers "Switch back"
    And event "equator.identity.context.switched.v1" has reason "deeplink"

  Scenario: Ethical wall blocks a context
    Given a wall blocks Raj from Equator matter metadata for client C
    Then the switcher lists that context greyed with "Not available: conflict wall"

Feature: Dashboards and next best action
  Scenario: NBA never suggests a neutral
    When a tenant admin publishes an NBA rule whose action is "select neutral"
    Then the response is 422 with code "CFG_NBA_GUARD_VIOLATION"

  Scenario: Mandatory widget stays
    When a party hides "W-SIGNPOST" on a case where signposting applies
    Then the response is 409 with code "CFG_WIDGET_MANDATORY"

Feature: Routes (D3-47)
  Scenario: Reserved chambers segments
    When a practice registers slug "work"
    Then the response is 409 with code "CHM_SLUG_RESERVED"

  Scenario: Old ops routes redirect
    When a user opens "ops.equatorresolution.in/ops/hr/employees"
    Then the response is 301 to "/hr/employees"
```

---

## AG.11 Phase addenda

### For P00

**FR-P00-V31-AG01 — Shell framework.** Build `packages/shell` (web) with the AG.1.2 anatomy, skip links, context chip, header search entry, inbox tray, help entry, me menu, QuickExit slot and breadcrumbs generated from registered route parents; every app (`apps/web` shells, `apps/ops`, admin, assurance) uses it. *Acceptance:* axe shows no violations on each shell's home; route change moves focus to the H1 and announces the title.

**FR-P00-V31-AG02 — Navigation registry and resolver.** Create `cfg.nav_menus`, `cfg.nav_items`, `cfg.route_redirects`, the resolver of AG.1.4 (rules R-1–R-12) in each BFF, `GET /v1/me/navigation`, cache invalidation on the listed events, and seed rows for every tree in AG.2 (each owning phase adds its rows in the same PR as its screens). CI checks `NAV_ROUTE_GUARDED`, `NAV_HELP_MISSING` (warning), `NAV_NO_NEUTRAL_SELECTION_ENTERPRISE` and a registry-to-screen-table consistency check (route template equals the phase §6 route). *Acceptance:* the AG.10.6 resolver scenarios pass; menu payload ≤ 8 KB gzip.

**FR-P00-V31-AG03 — Work Inbox service.** `InboxPort`, `core.inbox_items`, `cfg.inbox_sources`, BFF federation across plane stores without cross-cluster joins, AG-SCR-01/-02, ordering (AG.4.4), snooze and bulk rules (AG.4.3, AG.4.5), digests and quiet hours (AG.4.6) using P07 channels; SCR-P07-17 becomes the Updates tab. *Acceptance:* the inbox scenarios of AG.10.6 pass; a P1 item reaches push within 60 s.

**FR-P00-V31-AG04 — Search and command palette.** Document-level ACL tokens on every index, Cerbos post-filter, `SEARCH_NO_SEALED`, case-number jump, type prefixes, AG-SCR-03/-04, AG-SCR-11 with remapping and the single-key switch (WCAG 2.1.4), recent items tables. *Acceptance:* search and palette scenarios pass; palette p95 ≤ 300 ms (customer shells).

**FR-P00-V31-AG05 — Pattern library.** Ship `packages/patterns` PAT-01 to PAT-16 with Storybook stories, accessibility tests and backend contract helpers (`BulkJobService`, `DraftService`, `UndoWindow`), plus AG-SCR-18, AG-SCR-19 and AG-SCR-27. *Acceptance:* each pattern has stories for every state and passes axe; bulk undo works within the window and fails after it with `CFG_BULK_UNDO_WINDOW_CLOSED`.

**FR-P00-V31-AG06 — Navigation analytics.** Emit the AG.9.3 events through `ANALYTICS_PORT` with the exhaustive property lists, pseudonymous daily session IDs, k ≥ 10 reporting and no events from sealed shells. *Acceptance:* a contract test rejects any event carrying an ID-shaped value or query text; POSH sub-shell emits zero events.

### For P01

**FR-P01-V31-AG01 — Context switcher v3.1.** Extend SCR-P01-38 as AG-SCR-05: dimensions of AG.1.3 (organisation, entity, role, chambers, client), wall-blocked contexts greyed, workforce/consumer separation, unsaved-draft prompt, cross-shell switching with step-up, `Equator-Context.entity` claim, and the extended `equator.identity.context.switched.v1` payload. *Acceptance:* the context scenarios of AG.10.6 pass.

**FR-P01-V31-AG02 — Away and delegation.** AG-SCR-06 with per-source handling (delegate, return to queue, hold), checks against `core.delegations` limits (≤ 90 days, depth 1), authority-limit check for approval delegation, prompt when approved leave starts, and `equator.notifications.away.set.v1`. *Acceptance:* a delegate without the permission or with a lower authority limit is refused with `CFG_INBOX_DELEGATION_NOT_ALLOWED`.

**FR-P01-V31-AG03 — Deep links and access requests.** Signed context hints in links, auto-switch with "Switch back", mismatch and expiry handling (`CFG_DEEPLINK_CONTEXT_MISMATCH`, `CFG_DEEPLINK_EXPIRED`), and AG-SCR-17 access requests routed to the tenant admin's inbox. *Acceptance:* a link for another account shows nothing about the object.

**FR-P01-V31-AG04 — Firm administration and landing routes.** AG-SCR-25 for representative firms; update `core.login_portals.dashboard_route` for `chambers` to `/chambers/work` (AG.0.5 #7). *Acceptance:* chambers sign-in lands on SCR-P20-29; `/app/chambers` 301s.

### For P12

**FR-P12-V31-AG01 — Persona tab bars and More sheet.** Implement the AG.2.13 tab bars from `cfg.nav_items` (`mobile.*.tabs` menus), the More sheet and tab editor (AG-SCR-14), locked Home/Today and Inbox slots, and badges from the count service; the Inbox tab replaces the P07 "Inbox" and C §C.3 "Messages" tabs. *Acceptance:* each persona shows ≤ 5 slots; reordering persists across devices.

**FR-P12-V31-AG02 — Mobile inbox and approvals.** Native Work Inbox with the AG.4 ordering, snooze rules and decision panel; money approvals above the web-only threshold (₹50,000 per P18, and pay runs) show "Approve on the web" with a deep link. *Acceptance:* a P1 item appears within 60 s of the source event; screenshots blocked on sealed and payslip screens.

**FR-P12-V31-AG03 — Universal links and back behaviour.** Universal/App Links for the AG.1.5 route list, Android back and iOS swipe rules of AG.1.6, and "Leave without finishing?" on pay and sign. *Acceptance:* Maestro journeys for tasks 1–5 and 17–18 of AG.9.4 meet their click targets.

### For P13

**FR-P13-V31-AG01 — v3.1 mega-menu (amends FR-P13-03).** Build AG-SCR-13 with the ten groups of AG.2.1, responsive priority, disclosure-navigation semantics, no-JS fallback, Marketplace group gated by enabled categories with the locked separation note, and the Log in menu of Appendix P §3.0. All FR-P13-03 destinations remain reachable. *Acceptance:* every FR-P13-03 route is linked from the menu or footer; Lighthouse accessibility 100 on the header; the menu works with JavaScript disabled.

**FR-P13-V31-AG02 — Screen-ID reconciliation.** Adopt the renumbering map of AG.2.1 (SCR-P13-40 → -58), register it in Appendix C §B.1 and §B.14 in the same PR, and fix references in Appendices C, P and S. *Acceptance:* a script finds no SCR-P13 ID with two meanings across the pack.

### For P15

**FR-P15-V31-AG01 — Settings rail by section.** Restructure the settings shell into the AG.3.1 sections with section visibility by `cfg:read`, tier-specific save buttons and pending chips (AG.3.2), and route the Approvals rail item to the Work Inbox filtered by source. *Acceptance:* a G change shows "Submit for approval" naming the approver role; the approval appears only in the inbox.

**FR-P15-V31-AG02 — Navigation and terminology editor.** AG-SCR-07 with preview-as-role, overrides as change sets with rollback, terminology per locale with glossary lint, custom links with the domain allow-list, and the platform registry mode (maker-checker publish). *Acceptance:* hiding a locked item fails with `CFG_NAV_ITEM_LOCKED`; a "Court" label fails with `CFG_NAV_LABEL_PROHIBITED`.

**FR-P15-V31-AG03 — Dashboards, views, tours.** AG-SCR-08 (widget gallery from `cfg.widget_catalogue`, tenant defaults per role, mandatory enforcement), AG-SCR-09 (saved views with sharing scope and pins; system views from `cfg.view_definitions`), AG-SCR-10 (checklists and tours from `cfg.tours`), and tenant NBA rules with 30-day preview and guards. *Acceptance:* the dashboard and NBA scenarios of AG.10.6 pass.

**FR-P15-V31-AG04 — ADR on inbox store placement.** Record, in the schema-placement ADR required by master §4.5, which inbox store each source writes to (`core.inbox_items` or `ops.ws_inbox_items`) according to its cluster. *Acceptance:* `cfg.inbox_sources.plane` matches the ADR for every source.

### For P16

**FR-P16-V31-AG01 — Department rail and route normalisation.** Render the AG.2.8 department rail and menus from the registry; apply D3-47(a) (drop `/ops` prefixes from P17/P18 routes with 301s), resolve `/audit` and `/exports` per AG.0.5 #3–#4, and make SCR-P16-03 and SCR-P18-36 views of the Work Inbox. *Acceptance:* no two screens share a route in `apps/ops`; old routes redirect.

**FR-P16-V31-AG02 — Help panel and what's new.** AG-SCR-12 driven by `help_article_key`, KB spaces `public_help` and `internal`, "Report a problem" with route template and trace ID only; AG-SCR-16 from customer release notes (Appendix AE §AE.4.8). *Acceptance:* every ops route has a help article or a CI warning.

**FR-P16-V31-AG03 — Navigation and usability analytics dashboard.** AG-SCR-15 reporting the AG.9.4 KPIs (task completion, clicks-to-complete for the top 20 tasks, dead-end rate, search success, palette adoption, inbox time-to-decision) with k ≥ 10 suppression. *Acceptance:* the dashboard shows each KPI with target and trend; no row identifies a user.

**FR-P16-V31-AG04 — Operations NBA and queue patterns.** Apply PAT-03, PAT-04 and PAT-13 to support, grievance, onboarding and CS queues, and seed NBA-OPS, NBA-ONB, NBA-CSM, NBA-SUP and NBA-GRO rules. *Acceptance:* "Next ticket" respects AG.4.4 ordering and skips wall-blocked items with `OPS_ETHICAL_WALL` logged.
