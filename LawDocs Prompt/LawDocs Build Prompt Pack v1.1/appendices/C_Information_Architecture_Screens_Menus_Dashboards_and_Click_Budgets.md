# Appendix C — Information Architecture, Screens, Menus, Dashboards and Click Budgets (binding)

> LawDocs Build Prompt Pack v1.0 · 25 October 2026 · Compiled by X2 from every phase file §6 (Screens and UX), P02 §4L, P03 §4C–4D, P21 §4B/§4N, P22 §4A/§6 and Appendix U. Consumed by every phase.
>
> **Precedence.** This appendix governs the app map, shells, global navigation, menu trees, command palette, quick actions, home dashboards and widget catalogue, click budgets, design tokens, component list, state patterns, responsive and multilingual layout rules, and customisation surfaces. Each phase file governs the content and behaviour of its own screens (`SCR-Pxx-nn`). Appendix U governs accessibility success criteria and screen-reader patterns; where a token or component rule here and Appendix U differ, the stricter rule applies. Where this appendix reconciles two phases that disagree, the reconciliation is listed in §C.16 and the phase author applies it at integration.
>
> **Menus are data.** Every menu item, widget and quick action is a row in `cfg.nav_items` / `cfg.widget_catalogue` / `cfg.quick_actions.set` (P03 FR-P03-33–35) and maps to exactly one screen ID owned by a phase. UI trimming is a convenience: Cerbos enforces every action on the server (P02 FR-P02-56).

---

## C.0 Design principles (R-017, R-019, R-025, R-028, R-030, R-032, R-047)

1. **Role-first home.** Every user lands on a home built for the active context and role (§C.7). Next actions sit on top; statutory and legal deadlines are visible without a click. No user starts from a blank module list.
2. **Minimum clicks, measured.** The 40 journeys in §C.8 are release gates with budgets counted by an explicit rule (§C.8.1). Routine actions (open an item, approve, upload, ask Vidhi, sign, find a document) are reachable in ≤ 3 interactions from home, the Inbox, a notification or the command palette.
3. **Seven or fewer.** The primary navigation of any shell shows at most **7 top-level items**. Further entitled modules sit in one "More" list; unlicensed modules appear once in "Discover" with a plain explanation, never as disabled clutter (FR-P02-56).
4. **One inbox.** All actionable work — tasks, approvals, signature requests, waiting items, mentions, deal-room replies, deadlines — lives in the Inbox, backed by the single `wf.items` engine (X-09). Modules do not keep private to-do lists.
5. **Ask, search or act from anywhere.** Universal search and the command palette (`Ctrl/Cmd+K`), Ask Vidhi (`Ctrl/Cmd+J`, top bar, mobile floating button) and the "+" quick-action menu are present on every authenticated screen.
6. **Explain everything.** Every jargon label, status, column heading and error has an "i" button bound to a help key (`hlp.<module>.<term>`; general jargon `hlp.gen.<term>`, X-10). Definitions are ≤ 40 words at reading grade ≤ 8 (FR-P21-120).
7. **Calm, minimal UI.** White (or dark) surfaces, one primary action per view, generous spacing on a 4-pt grid, no decorative motion, no carousels that auto-advance, no upsell during a signing ceremony or a deadline task (P17 UX rules).
8. **Automation before forms.** Pre-fill from KYB sources with provenance (P01), from documents (P05 extraction), from previous records and from templates; users confirm rather than type (WCAG 3.3.7 redundant entry).
9. **Context is always visible.** The context bar shows workspace → legal entity (and grant, if acting under one). Every outbound action names the context in its confirmation: "Send as **Alpha Pvt Ltd**?" (FR-P02-08).
10. **Accessible and Indian-first by default.** WCAG 2.2 AA and IS 17802 (NN-28); INR with Indian digit grouping (₹ 12,34,567.00); dates `dd-MMM-yyyy`; financial year `FY 2026-27` (April–March); tax year labels per X-12; IST shown explicitly; ten launch UI languages (D-07).
11. **Same patterns everywhere.** Lists, record pages, drawers, approvals, imports, exports and signing use one component library (§C.10) so that learning one module teaches all.
12. **Honest surfaces.** No unevidenced claims (NN-20), no dark patterns (NN-50), AI output always labelled (NN-14), data freshness always shown for vendor-sourced court and IP data (P11, P12).

---

## C.1 App map

### C.1.1 Applications and hosts

| App | Host(s) | Brand variants | Realm / auth | Users | Purpose |
|---|---|---|---|---|---|
| `apps/public` | `www.lawdocs.in` (canonical), Consumer Help brand host `[Consumer Help Brand domain]` (`web.brand.host_map`) | LawDocs; `[Consumer Help Brand]` | Anonymous; preference cookie; inline OTP sign-in sheet (SCR-P01-04) | Visitors, buyers before sign-in | Website (≈ 600 pages, P21 FR-P21-11), marketplace storefront (P16), pricing (P17), blog/vlog, help centre, glossary, free tools, public drafter widget (P06), "Verify a document" (SCR-P08-12) |
| `apps/web` — **Personal workspace** | `my.lawdocs.in` | LawDocs; Consumer Help brand theme on the brand origin (FR-P15-01) | `ld` | `IND_OWNER`, `IND_FAMILY_MEMBER`, `IND_DELEGATE`, `IND_GUARDIAN`, `IND_NOMINEE` | Legal Vault, drafting, signing, my matters (cases, notices, brands), tax, services, consumer issues |
| `apps/web` — **Company workspace** | `my.lawdocs.in` (same app; context switcher) | LawDocs; tenant theme overrides on LD tokens (FR-P03-31) | `ld` (+ tenant SSO/SCIM, SCR-P01-22) | All `ORG_*` roles; outsiders under grants | Legal desk (`lgo`), contracts (`clm`), vault/DMS, matters (`lit`), IP (`ipm`), board & governance (`gov` mount or LDC projection), people (`hr` mount), services, settings |
| Board portal (route group of `apps/web`, PWA) | `my.lawdocs.in/board` | Tenant theme | `ld` | `ORG_DIRECTOR`, `ORG_KMP`, `ORG_BOARD_OBSERVER` | Board books, votes, declarations, signatures (SCR-P13-15) |
| Guest surfaces (route group of `apps/web`) | `my.lawdocs.in/g/*`, `sign.lawdocs.in` (signing ceremonies only; `frame-ancestors 'none'`, FR-P19-38) | Inviting tenant's brand line + LawDocs | Magic link + OTP | `CP_GUEST`, `ORG_EXT_COUNSEL` (counsel portal), share recipients | Single-task pages: review, comment, sign, upload, record outcome (SCR-P01-15, SCR-P04-10, SCR-P07-19, SCR-P08-04, SCR-P11-11) |
| `apps/delivery` | `work.lawdocs.in` | LawDocs; Consumer Help brand context for case managers (FR-P18-53) | `ld-staff` (staff; federated to group Entra ID) and `ld` (third-party professionals' practitioner workspace) | `OPS_*`; `PRO_*` | Delivery Console: portfolio, client sections, delegated-maker work under grants, deliverables, SLA, practitioner workspace, Consumer Help case queue |
| `apps/console` | `admin.lawdocs.in` (not on the public CDN; SSO + device posture) | — | `ld-staff` | `PLT_*`; `OPS_CONTENT_PUBLISHER` (Content Studio only, X-22) | Platform administration, content and rule studios, providers, pricing studio, engineering governance (`/eng`) |
| Developer portal (route group of `apps/public`) | `developers.lawdocs.in`, `sandbox.lawdocs.in` | — | Public + API client auth | Integrators | Guides, API reference, sandbox, SDKs, changelog (SCR-P19-19–22) |
| Partner portal (authenticated route group of `apps/web`) | `my.lawdocs.in/partner` | — | `ld` | Ecosystem partner admins | Onboarding batches (SCR-P19-11) |
| `apps/mobile` | iOS and Android "LawDocs"; Consumer Help flavour in v2 (P22 FR-P22-01) | `BRAND` flavours | `ld` via BFF `/m/v1` | All customer-realm users | Approvals, signing, vault, scan, Vidhi, matters, marketplace (parity matrix P22 §6.1) |
| Microsoft Teams / Google Chat apps | Tenant's own suite (`WORKSPACE_PORT`) | — | Tenant SSO | `ORG_MEMBER`, `ORG_DEPT_HEAD`, approvers | Request legal help, approval cards (SCR-P07-02, SCR-P13-03) |
| External, linked only | `trainings.lawdocs.in` (FinLegal Academy on Graphy, D-16), `status.lawdocs.in`, Operations Hub, LDC, Finbyx, Udofin, Equator | — | Their own | — | Deep links only; never embedded data (NN-19, NN-24) |

### C.1.2 How the apps connect (journey view)

```
lawdocs.in (public) ──"Start free" / drafter / Buy──▶ auth.lawdocs.in (OTP, passkey, SSO) ──▶ my.lawdocs.in
   │                                                                                 ├─ Personal workspace ◀── context switcher ──▶ Company workspace(s)
   │                                                                                 ├─ /board (directors)        └─ grants shown with expiry
   │                                                                                 └─ /g/* guest pages ◀── invitations (one + reminders, NN-34)
   ├─ /marketplace (no login, D-11) ──checkout (OH8, Razorpay hosted)──▶ engagement room in my.lawdocs.in
   └─ Consumer Help brand host ──▶ brand-themed my.lawdocs.in origin (separate cell, X-17; ethical wall NN-23)
sign.lawdocs.in ◀── hosted signing hand-off from LawDocs and sister products (X-05; status/evidence only flows back)
work.lawdocs.in (delivery) ──delivery grant (client-approved, NN-17)──▶ acts inside client tenant with banner
admin.lawdocs.in (console) ──Correction Entries / master-data changes (maker-checker + client approval, CH-26)──▶ tenant "Changes made by LawDocs"
```

### C.1.3 Consumer Help brand variant (D-06, NN-23, X-17, X-26)

| Aspect | Rule |
|---|---|
| Public site | Separate brand host rendered by `apps/public` with the brand's tokens, legal pages, fee sheet, grievance officer (SCR-P15-01). lawdocs.in carries only one explainer page `/consumer-help` with a link (FR-P21-11). |
| Signed-in experience | `apps/web` and `apps/mobile` with the brand theme on the brand's own origin; data in the separate Consumer Help cell (X-17). The context switcher shows the brand workspace only when the person linked sign-in (FR-P02-08, FR-P01-69). |
| Navigation | Own rail (§C.4.13); never shows Contracts, Board, People, Integrations or any lender-facing module (P22-AT-23). |
| Staff | `OPS_CONSUMER_CASE_MANAGER` signs in to `apps/delivery` in the brand context with a separate menu (FR-P18-53); no other tenant, client or brand data reachable. |
| Design tokens | Brand token set `packages/tokens/brands/consumer_help.json`; same contrast validator; never mimics a lender's, insurer's or government brand. |
| Copy | Reading level ≤ Class 8 target [REC]; "We never collect fines or dues"; no outcome promises (NN-23). |

---

## C.2 Shell anatomy

### C.2.1 `apps/web` (Personal and Company)

| Region | Content and rules |
|---|---|
| **Top bar** (56 px; 64 px at text scale ≥ 150%) | Logo (tenant or brand) · **context switcher** (workspace → legal entity; grant chip "via LawDocs retainer · until 31-Mar-2027") · **search / command palette** field (`Ctrl/Cmd+K`) · **"+" quick actions** (≤ 6, `cfg.quick_actions.max_per_user`) · **Ask Vidhi** (`Ctrl/Cmd+J`) · **Inbox** bell with count (LOCKED) · **Help** "?" (LOCKED; consistent location, WCAG 3.2.6) · profile menu (Personal settings, Billing for individuals, Privacy and my data, accessibility, language, sign out). |
| **Left rail** (240 px; collapses to 72 px icons + tooltips that are also accessible names; state remembered) | Primary group ≤ 7 items for the active role (§C.4); "Pinned" group ≤ 8 user pins (`cfg.nav.max_pinned_items`) shown above the primary group and collapsible; "More" (other entitled modules); "Discover" (once, unlicensed modules, dismissible). Icons always with text labels. |
| **Context band** (4 px under the top bar) | Workspace colour band (`org.context.colour_band`, contrast-checked) + text label; turns into a full **delivery banner** when acting under a grant: "You are working in Beta Finance Ltd as delegated maker (LawDocs). Client checker: R. Iyer. Grant ends 31-Mar-2027." (SCR-P18-17; P18-AT-30). |
| **Page header** | Title + "i" · breadcrumb (views over canonical IDs, NN-12) · one primary action · secondary actions in "⋯" · status chip for record pages. |
| **Main area** | Forms max 720 px reading width; lists full width; record pages two-column ≥ 1,280 px (content + details pane). |
| **Right panel** (400 px, dockable, optional) | Vidhi panel with record context chip (SCR-P09-05), activity/timeline, related items, help panel (SCR-P21-35). One panel open at a time. |
| **System banners** (stacked, max 2 visible, rest in a "2 more notices" disclosure) | Sandbox (amber), support/break-glass session active (NN-17), changes made by LawDocs not yet seen (SCR-P00-08), kill switch engaged for a used feature, vendor degraded with "as of", plan lapse (read and export still allowed, P17-AT-04), maintenance (SCR-P23-19). |
| **Footer** (32 px) | Version, status page, accessibility statement, privacy, grievance officer. |

### C.2.2 `apps/delivery`

Top bar adds **Product switcher** (SCR-P18-29, deep links to OH, LDC, Finbyx, Udofin, Equator per role) and a **"Acting as"** chip. The palette searches clients, tasks and deliverables in scope only (P18 UX rules). Client sections open as a sub-shell with their own tab row (Overview, Contacts, Plan, Engagements, Tasks, Deliverables, Messages, Meetings, Shared drive, Billing, SLA, Access log, Notes, Act in tenant, Credentials). "Act in tenant" launches the client's `apps/web` context with the delivery banner; it never embeds client screens inside `apps/delivery`.

### C.2.3 `apps/console`

Restricted shell: IP and device-posture gated; every page shows the environment badge; every tenant-affecting save opens a Correction Entry or a master-data change request (SCR-P03-28, SCR-P18-35). `OPS_CONTENT_PUBLISHER` sees a Content-Studio-only rail (Cerbos `web.content_studio`, FR-P21 §4I).

### C.2.4 `apps/mobile`

Workspace switcher (SCR-P22-03) then a per-workspace tab bar of 5 (§C.4.18). A floating **Ask Vidhi** button on Home and in the document viewer (FR-P22-04); a **Scan** action in the Create tab and the Home quick actions. Protected screens (credential metadata, evidence of others, signing consent, approvals) set the secure flag (NN-44).

### C.2.5 `apps/public`

Header: logo, top navigation of exactly seven disclosure menus (FR-P21-13), utility bar (Search, language, accessibility preferences, Log in, "Start free"). Mobile: one menu button opening a full-height dialog; sticky bottom bar "Draft free" / "Hire a pro" that never covers focused content (FR-P21-15). Footer per FR-P21-16.

---

## C.3 Global navigation rules

| # | Rule | Source |
|---|---|---|
| N-1 | Primary rail ≤ 7 items per role; anything else goes to "More". Tenants may reorder, rename (terminology) and hide items (`cfg.nav.order`, `cfg.nav.hidden_modules`), never exceed 7 in the primary group. | FR-P03-34, R-030 |
| N-2 | **LOCKED** (cannot be hidden by any tier): Home; Inbox (top bar); Documents/Vault; Help (top bar); Profile and Settings; Privacy and my data; "Changes made by LawDocs" for `ORG_OWNER`/`ORG_ADMIN`; Audit trail for `ORG_AUDITOR_RO`. | FR-P03-34 |
| N-3 | Users pin up to 8 leaves ("Pinned" group) and reorder by drag or by the keyboard "Move up/down" menu; pins are per user per context. | FR-P03-34 |
| N-4 | A person with one workspace never sees the context switcher; a person with more than seven contexts gets search in the switcher; recent first. | FR-P02-08, FR-P02-10 |
| N-5 | Unlicensed modules: one "Discover" entry with a plain description and "See what it does"; one dismissal suppresses it for 30 days; never shown during signing, approvals or a deadline task. | FR-P02-56, P17 UX |
| N-6 | Deep links carry context (`?ctx=ten_…&ent=ent_…`); opening a link for another context prompts "Switch to Alpha Pvt Ltd to open this?" rather than failing. | FR-P02-08 |
| N-7 | "Preview as user type" shows rail, home and palette exactly as that user type sees them before an admin saves menu changes. | FR-P03-34 |
| N-8 | Every menu label carries a help key; statutory labels ("Stamp duty", "Power of attorney", "Affidavit") are LOCKED labels with tenant-editable help text only. | FR-P02-56, FR-P03-38 |
| N-9 | Registers paginate with counts; no infinite scroll without a keyboard path. | P11 global UX rules, Appendix U §U.5.4 |
| N-10 | Landing page per user type is configurable (`cfg.nav.landing_page`); default Home. | Appendix R |

---

## C.4 Menu trees per user type

Legend: leaf → screen ID (owning phase). **(L)** LOCKED. **[E]** shown only if entitled (P17). **[M]** LDC projection when `int.eco.ldc.sor_mode.*` is LDC (X-11, NN-47). Top-bar items (Search, "+", Ask Vidhi, Inbox, Help, Profile) are common to every tree and not repeated. Labels are defaults; tenants may rename them (FR-P03-38/39).

### C.4.1 Individual — `IND_OWNER` (Personal workspace; 6 primary items)

```
Home (L) ....................................... SCR-P02-18 (widgets §C.7.2)
Vault (L)
  ├ Life-event folders (Property, Family, Work, Money, Vehicle, Disputes, Tax) .. SCR-P04-01, SCR-P04-03
  ├ Search ....................................... SCR-P04-08
  ├ Expiring soon and reminders .................. SCR-P04-13
  ├ Vault health ................................. SCR-P04-17
  ├ Add from DigiLocker ........................... SCR-P04-20
  ├ Shared by me / sharing activity .............. SCR-P04-11
  ├ Family and nominees ........................... SCR-P04-14 (who can see: SCR-P02-16)
  └ Recycle bin .................................. SCR-P04-18
Create
  ├ Draft something (catalogue, search) .......... SCR-P06-02 → SCR-P06-03
  ├ Continue drafts .............................. SCR-P06-05
  ├ Pleadings and notices ......................... SCR-P10-02, SCR-P10-08
  └ Type copy and translate (from a document) .... SCR-P05-01
Sign
  ├ Waiting for me / waiting for others .......... SCR-P08-07
  ├ Formalities (stamp, notary, registration) .... SCR-P08-09, SCR-P08-10
  └ Evidence packs ............................... SCR-P08-11
My matters
  ├ My cases ..................................... SCR-P11-15, SCR-P11-16
  ├ Notices sent and received .................... SCR-P10-09
  ├ My brands and creations ...................... SCR-P12-14
  ├ Tax ........................................... SCR-P14-09, SCR-P14-13
  └ Consumer issues (opens brand origin if linked) SCR-P15-04
Services
  ├ Browse (same catalogue as /marketplace) ...... SCR-P16-01–03
  ├ My services and orders ....................... SCR-P16-11, SCR-P16-12, SCR-P14-04
  └ AI workforce [E] ............................. SCR-P09-12
Profile menu: Personal settings (SCR-P03-29) · Billing & Membership (SCR-P17-10–28) · Privacy and my data (L) (SCR-P01-18, SCR-P20-01) · Security (SCR-P01-05) · Verify your identity (SCR-P01-06) · Connected apps (SCR-P19-10) · Close my account (SCR-P20-12)
```

**Scoped individual roles.** `IND_FAMILY_MEMBER` and `IND_DELEGATE`: rail = Home · Shared · Tasks (FR-P02-12/13); delegate actions are labelled "by Rohan for Ananya". `IND_GUARDIAN`: adds "Wards" (SCR-P01-16) to the profile menu and a ward switcher in the context switcher. `IND_NOMINEE`: no rail before release; a single status page (SCR-P04-15, SCR-P01-17).

### C.4.2 Company admin — `ORG_OWNER` / `ORG_ADMIN` (7 primary items)

```
Home (L) ....................................... SCR-P02-18
Legal desk ..................................... SCR-P13-02 (Requests SCR-P13-04, Calendar SCR-P13-07, Spend SCR-P11-12, Panel SCR-P11-10, Licences SCR-P13-10 [M])
Contracts ...................................... SCR-P07-14 (Intake queue SCR-P07-03, Repository, Renewals SCR-P07-17, Bulk SCR-P07-18, Import SCR-P07-15)
Vault (L) ...................................... SCR-P04-02 (DMS home), SCR-P04-03, SCR-P04-08, SCR-P04-16
Matters ........................................ SCR-P11-01 (Register SCR-P11-02, Hearings SCR-P11-06, Deadlines SCR-P11-09, Reports SCR-P11-18)
People ......................................... SCR-P02-04 (Org structure SCR-P02-02, Roles SCR-P02-07, Outsider access SCR-P02-14, Access reviews SCR-P02-15; HR: Directory SCR-P13-22, Leave SCR-P13-23, Payroll SCR-P13-24 [M])
Settings (L) ................................... SCR-P03-01 (tree §C.4.17)
More: IP & Trademarks (SCR-P12-01) · Board & Governance (SCR-P13-13–19 [M]) · Services (SCR-P16-11) · Startup Desk [E] (SCR-P14-07) · Tax (SCR-P14-11, SCR-P14-12) · AI workforce (SCR-P09-12) · Integrations (SCR-P19-01) · Reports
Admin-only LOCKED leaf: Settings › Audit & history › Changes made by LawDocs (SCR-P00-08, SCR-P03-27)
```

### C.4.3 Chief legal officer — `ORG_CLO` (7)

```
Home (L) — Legal Department Home ............... SCR-P13-02 (legal risk dashboard widgets §C.7.3)
Legal desk ..................................... SCR-P13-04, SCR-P13-05, SCR-P13-07, SCR-P13-09, SCR-P13-10
Contracts ...................................... SCR-P07-03, SCR-P07-14, SCR-P07-16 (CLO dashboard), SCR-P07-17
Matters ........................................ SCR-P11-01, SCR-P11-02, SCR-P11-07, SCR-P11-13, SCR-P11-12
IP ............................................. SCR-P12-01, SCR-P12-02, SCR-P12-10
Notices ........................................ SCR-P10-09 (and SCR-P10-08 to compose)
Reports ........................................ SCR-P11-18, SCR-P12-13, SCR-P13-08, SCR-P06-17 (tenant view), SCR-P17-27
More: Vault · Board & Governance · Templates and playbooks (SCR-P06-18) · AI workforce · Notebooks (SCR-P09-19)
```

### C.4.4 Maker — `ORG_LEGAL_MAKER` and `ORG_DELEGATED_MAKER` (5)

```
Home (L) — My queue ............................ SCR-P02-18 (widgets: My queue, Returned to me, Due dates)
Queue .......................................... SCR-P03-18 (My items), SCR-P13-04 (assigned requests), SCR-P07-03
Contracts ...................................... SCR-P07-04, SCR-P07-05, SCR-P07-06, SCR-P07-12, SCR-P07-13
Drafting ....................................... SCR-P06-02, SCR-P06-05, SCR-P10-02, SCR-P05-01
Vault (L) ...................................... SCR-P04-03, SCR-P04-07 (bulk intake where permitted)
More (by grant scope): Matters · IP · Notices
```

`ORG_DELEGATED_MAKER` sees only the scopes in the delivery or engagement grant; the delivery banner is permanent (NN-17); "Approve", "Sign", "Export everything" and "Settings" never appear (FR-P02-17; P18-AT-02).

### C.4.5 Checker / approver — `ORG_CHECKER` and `ORG_APPROVER` (4)

```
Home (L) — Approvals first ..................... SCR-P02-18 (mandatory widget: Approvals awaiting me)
Approvals ...................................... SCR-P02-12 ("Review next"), SCR-P07-10, SCR-P09-14, SCR-P20-04, SCR-P18-31
Sign ........................................... SCR-P08-07, SCR-P08-04, SCR-P08-06 (DSC)
Contracts ...................................... SCR-P07-14 (read), SCR-P07-04
```

### C.4.6 Department user — `ORG_DEPT_HEAD` and `ORG_MEMBER` (4)

```
Home (L) ....................................... "Request legal help" tile, My requests, Contracts of my department
Requests ....................................... SCR-P13-03 (raise), SCR-P13-06 (my requests), SCR-P07-01 (contract request)
Contracts ...................................... SCR-P07-14 (department view only)
Vault (L) ...................................... department folders and shared items only
Department heads add: Team workload (counts only, NN-33) on Home; Access review items (SCR-P02-15); Policy acknowledgements (SCR-P13-26) for all members
```

"Request legal help" is also a button on every Company workspace page and in Teams/Google Chat (FR-P13 intake; ≤ 3 clicks to submit).

### C.4.7 Director / KMP — `ORG_DIRECTOR`, `ORG_KMP`, `ORG_BOARD_OBSERVER` (4; board portal)

```
Home (L) ....................................... Items awaiting my approval or signature; board items; legal risk summary
Approvals ...................................... SCR-P02-12, SCR-P22-20 (mobile)
Board .......................................... SCR-P13-15 (board portal: books, votes, declarations, signatures), SCR-P13-14 (meeting), SCR-P13-17
Reports ........................................ SCR-P13-08 (frozen legal risk dashboard), SCR-P11-18 (board section)
KMP (CS) adds: Meeting planner SCR-P13-13, Minutes editor SCR-P13-16, Registers SCR-P13-18, Directors & KMP SCR-P13-19, Governance blueprint SCR-P13-11 [M]
Board observers: read-only Board; no vote or sign controls rendered.
```

### C.4.8 Auditor — `ORG_AUDITOR_RO` (3)

```
Home (L) — Audit scope ......................... scope, period, items requested
Assigned ....................................... read-only records in scope (watermarked downloads)
Audit trail (L) ................................ SCR-P00-09, SCR-P03-27, SCR-P17-26, SCR-P18-34 (access transparency)
```

### C.4.9 External counsel — `ORG_EXT_COUNSEL` (guest shell, 1)

```
Assigned matters ............................... SCR-P11-11 (counsel portal: matters, 4-field outcome form, uploads, tasks, invoices, messages)
```

No search beyond assigned matters (P11-AT-13). Outcome form reachable in ≤ 2 taps from the e-mail or WhatsApp utility template (J-21).

### C.4.10 Counterparty — `CP_GUEST` (single-task page)

One page per invitation: what you are asked to do, who invited you, notice, OTP; then review/comment/sign (SCR-P01-15, SCR-P07-19, SCR-P08-04, SCR-P04-10). Optional "Create an account to keep a copy". One invitation plus reminders the guest can stop (NN-34).

### C.4.11 LawDocs relationship manager and delivery — `OPS_RM`, `OPS_DELIVERY_LEAD`, `OPS_PROFESSIONAL`, `OPS_QA_REVIEWER` (`apps/delivery`, 7)

```
Home — Portfolio ............................... SCR-P18-01 (client cards by next breach)
Inbox (federated, per-tenant partitions) ....... SCR-P18-02
Clients ........................................ SCR-P18-03 → client section SCR-P18-04–18
Grants ......................................... SCR-P18-19 (propose), SCR-P18-20 (board), SCR-P18-21 (reviews)
Engagements .................................... SCR-P16-22 (pipeline), SCR-P16-21 (offer/retainer builder), SCR-P16-20 (service studio, product roles)
Team ........................................... SCR-P18-22 (delivery lead), SCR-P18-25 (portfolio reports)
Me ............................................. SCR-P18-23 (time), SCR-P18-24 (my outcome metrics; no ranks, NN-33)
OPS_PROFESSIONAL replaces Grants with "Work queue" (SCR-P14-14, SCR-P06-10, SCR-P09-08 QRG reviews). OPS_QA_REVIEWER: Home · QA queue (SCR-P16-25) · Me.
```

### C.4.12 Professional — `PRO_ADVOCATE`, `PRO_CA`, `PRO_CS`, `PRO_TAX_PRACTITIONER`, `PRO_OTHER`, `PRO_FIRM_ADMIN`, `PRO_FIRM_MEMBER` (`apps/delivery` practitioner workspace, 6)

```
Home ........................................... SCR-P18-27 (engagements, calendar, payouts)
Engagements .................................... SCR-P16-23 (assignments, active work, time, release requests)
Reviews ........................................ SCR-P06-10 (draft review), SCR-P10-11 (advocate pleading review), SCR-P09-08 (QRG)
Calendar ....................................... hearings and deliverable dates of engaged matters
Messages ....................................... engagement threads
Profile & firm ................................. SCR-P18-28 (Rule 36 fields only for advocates, NN-21), SCR-P16-24 (onboarding), SCR-P01-13; firm members (PRO_FIRM_ADMIN)
Client work happens only inside client tenants via engagement grants (FR-P02-16); payouts view is read-only (Route, OH8).
```

### C.4.13 Consumer Help — consumer and `OPS_CONSUMER_CASE_MANAGER`

```
Consumer (brand origin; 5)                         Case manager (apps/delivery, brand context; 5)
Home ............ SCR-P15-01 tiles / case status   Queue ........ SCR-P15-14, SCR-P18-26 (deadline risk, conflict status)
My cases ........ SCR-P15-04 (+ triage SCR-P15-02/03) Cases ....... SCR-P15-04 (case-manager view), SCR-P15-07 letter studio
Evidence ........ SCR-P15-05, SCR-P15-06 harassment log  Calendar .... deadlines, Lok Adalat dates
Vehicles & challans SCR-P15-11, SCR-P15-12, SCR-P15-13   Messages .... case threads
Consents & authorities SCR-P15-08                       Me .......... time, own outcome metrics
Specialised desks open from a case: credit-report dispute SCR-P15-09; insurance claim desk SCR-P15-10.
```

### C.4.14 Platform — `PLT_SUPER_ADMIN` and platform roles (`apps/console`, 7)

```
Home ........................................... SCR-P00-01 (platform health)
Tenants ........................................ SCR-P00-02, SCR-P17-42 (commercial view), SCR-P03-28 (override → Correction Entry)
Platform ....................................... Flags & kill switches SCR-P00-03/SCR-P03-24 · Migration SCR-P00-06 · Events SCR-P00-07 · Providers SCR-P08-14, SCR-P01-20, SCR-P19-15 · Models SCR-P09-22 · Integrations monitor SCR-P19-16
Audit & corrections ............................ SCR-P00-04, SCR-P00-05, SCR-P18-35 (master-data queue), SCR-P18-36 (break-glass)
Content & rules ................................ Template Studio SCR-P06-11–16 · Rule-set editor SCR-P03-21 · Review queue SCR-P03-22 · Eligibility registry SCR-P08-15 · Consumer Help rules SCR-P15-15 · Service studio SCR-P14-15 · Tax packs SCR-P14-16 · Notices & consent SCR-P01-19
Commercial ..................................... Pricing Studio SCR-P17-40 · Streams SCR-P17-41 · Marketplace admin SCR-P16-30 · Payouts SCR-P16-32 · Savings methodology SCR-P17-44
Engineering (/eng) ............................. SCR-P23-01–18
Role trimming: PLT_SECURITY_OFFICER (Audit, Platform › kill switches, /eng security); PLT_SRE (Platform, /eng ops); PLT_CONTENT_EDITOR and PLT_LEGAL_REVIEWER (Content & rules only); PLT_DPO (privacy queues, SCR-P00-11, SCR-P15-16); PLT_GRIEVANCE_OFFICER (grievance queues); PLT_AUDITOR_RO (read-only Audit and /eng evidence).
```

### C.4.15 Content publisher — `OPS_CONTENT_PUBLISHER` (`apps/console` Content Studio, 7; X-22)

```
Content ........................................ SCR-P21-23 (list), SCR-P21-24 (block editor)
Import from Word ............................... SCR-P21-25
Review ......................................... SCR-P21-26 (maker ≠ checker, P21-AT-08)
Media & videos ................................. SCR-P21-33
Tutorials & tours .............................. SCR-P21-30, SCR-P21-31
Campaign pages ................................. SCR-P21-32
SEO & redirects ................................ SCR-P21-28, SCR-P21-27
PLT_CONTENT_EDITOR adds Glossary studio SCR-P21-29; accessibility issues board SCR-P21-34 is shared with PLT roles.
```

### C.4.16 Public site (`apps/public`; 7 top-level, FR-P21-13)

```
Documents ▾  Court & Notices ▾  Business ▾  Product ▾  Marketplace ▾  Pricing  Resources ▾      [Search] [Language] [Accessibility] [Log in] [Start free]
Documents: 18 category hubs → sub-hubs → document pages (SCR-P21-03/04/05) · Court & Notices: pleadings, notices, litigation tracker (SCR-P21-06)
Business: start a business, compliance, regulated entities, advisory, startups (SCR-P14-01/02, SCR-P21-13) · Product: Vidhi, eSign/eStamp, vault, contracts, trackers, legal department
Marketplace: SCR-P16-01–08, SCR-P21-11 · Pricing: SCR-P17-01–04, SCR-P21-12 · Resources: blog, videos, help, glossary, tools, tutorials (SCR-P21-14/15/16/09/22)
```

### C.4.17 Settings tree (Company workspace; Personal settings in brackets)

```
Settings home ........................ SCR-P03-01 (search first, natural-language assistant FR-P03-30; recent changes; pending approvals)
├ Organisation ....................... structure SCR-P02-02, departments SCR-P02-03, company profile SCR-P01-10, signatories SCR-P01-12
├ People and access .................. SCR-P02-04–08, SCR-P02-11 (maker-checker), SCR-P02-09/10 (DoA), SCR-P02-13 (delegation), SCR-P02-14, SCR-P02-15
├ LawDocs team ....................... SCR-P18-30 (grants, standing authorisation), SCR-P18-32 (credential vault, OFF by default), SCR-P18-33
├ Appearance and navigation .......... SCR-P03-06 (theme), SCR-P03-07 (home and quick actions), SCR-P03-08 (menus), SCR-P03-09 (terminology)
├ Data model ......................... SCR-P03-10 custom fields, SCR-P03-11 statuses, SCR-P03-12 numbering, SCR-P03-13 forms, SCR-P03-16 item types, SCR-P03-17 chase policies
├ Documents and templates ............ SCR-P04-19 (DMS), SCR-P03-15 (letterheads), SCR-P06-18 (templates/playbooks), SCR-P08-16 (signing)
├ Communications ..................... SCR-P03-14 (templates; DLT IDs), SCR-P11-21 (alert preferences)
├ Rules and automations .............. SCR-P03-20 (rules adopted), SCR-P03-30 (automations and agents), SCR-P09-20 (Vidhi), SCR-P03-24 (flags/kill switches, tenant scope)
├ Integrations ....................... SCR-P19-01–09, SCR-P19-13, SCR-P19-14
├ Data and storage ................... SCR-P20-01, SCR-P20-05, SCR-P20-10, SCR-P20-11
├ Billing & Membership ............... SCR-P17-10–28; purchase settings SCR-P16-15
├ Security and privacy ............... SCR-P01-22 (SSO/SCIM), SCR-P18-34 (access transparency), SCR-P01-18
├ Audit & history (L) ................ SCR-P00-08 (changes made by LawDocs), SCR-P00-09 (integrity), SCR-P03-27
└ Tools .............................. SCR-P03-25 (templates, import, compare, sandbox), SCR-P03-26 (configuration health), SCR-P03-31 (explain my configuration)
[Personal settings SCR-P03-29: Language · Accessibility · Appearance · Home · Quick actions · Notifications and quiet hours · Delegation · My data — each ≤ 2 taps from home]
```

### C.4.17A IPB-07 twenty-node Settings tree — mapping to the v1.0 tree *(v1.1; P03 FR-P03-106…109)*

The tree above is **kept as the inventory of screens**; from v1.1 the Settings home renders the binding IPB-07 §07.4.2 order and names. Each node lists the v1.0 section it absorbs and the screens it reaches. "New" = shell built by P03 in v1.1; content owned by the phase named.

| # | IPB node (binding name) | Tier | v1.0 section absorbed | Screens | Notes |
|---|---|---|---|---|---|
| 1 | Profile | USER | [Personal settings] (name, signature block) | SCR-P03-29, SCR-P01-10 (own profile) | LD adds Bar Council enrolment no. and signature block (IPB-07 LD row) |
| 2 | Security | USER (ORG policy view) | Security and privacy (part) | SCR-P01-18 (password, MFA, passkeys, sessions), SCR-P01-22 (SSO/SCIM, read-only here) | ORG policy sub-items: password and MFA policy, sessions, IP allow-list, BYOK, audit-log link — FR-P03-108 (new screen SCR-P03-33) |
| 3 | Privacy & consents | USER | Security and privacy (part); [My data] | SCR-P01-18 (consents), SCR-P18-34 (access transparency), SCR-P20-10 (my data requests) | Adds "What this app can access" (device permissions, connected identities) — UDF pattern |
| 4 | Accessibility | USER | [Accessibility] | SCR-P03-29 (Appendix U §U.4 set) | New node; FR-P03-107(a) |
| 5 | Appearance | USER | Appearance and navigation (user part); [Appearance · Home · Quick actions] | SCR-P03-06, SCR-P03-07 | Adds density, formats, first day of week, default landing, simple mode — FR-P03-107(b) |
| 6 | Notifications | USER (ORG routing) | Communications (user part); [Notifications and quiet hours] | SCR-P11-21, SCR-P03-14 (routing, ORG) | Mandatory classes shown locked |
| 7 | Customisation | ORG | Appearance and navigation (tenant part); Data model; Documents and templates | SCR-P03-06…09, SCR-P03-10…13, SCR-P03-15…17, SCR-P06-18 | Branding = `brand_pack` tenant layer (FR-P03-31A); terminology; navigation; dashboards; custom fields; numbering; forms; templates and letterheads |
| 8 | Organisation & people | ORG | Organisation; People and access; LawDocs team | SCR-P02-02…15, SCR-P01-10, SCR-P01-12, SCR-P18-30, SCR-P18-32, SCR-P18-33 | Security policy editor (FR-P03-108) lives here as "Security policy" |
| 9 | Billing | ORG | Billing & Membership (payment part) | SCR-P17-10…14 | Split per IPB-07 LD note |
| 10 | Invoices | ORG | Billing & Membership (invoices part) | SCR-P17-15…19 | OH8 mirror |
| 11 | Plans & subscription | ORG | Billing & Membership (plan part); purchase settings | SCR-P17-20…28, SCR-P16-15 | Cancellation as easy as purchase |
| 12 | Storage & data | ORG | Data and storage | SCR-P20-01, SCR-P20-05, SCR-P20-10, SCR-P20-11 | P20 FR-P20-55 |
| 13 | Audit trails | ORG (PLATFORM ledger) | Audit & history (L) | SCR-P00-08, SCR-P00-09, SCR-P03-27 | Hash-chain verification status; signed export |
| 14 | Integrations | ORG | Integrations | SCR-P19-01…09, SCR-P19-13, SCR-P19-14 | Adds connector marketplace, calendar/workspace, webhook designer (P19 FR-P19-76A, FR-P19-85) |
| 15 | AI & Vidhi | ORG (PLATFORM ceilings) | Rules and automations (Vidhi part) | SCR-P09-20, SCR-P09-11…19 | Providers and BYOK, autonomy per skill, locked list (read-only), agents, schedules, notebooks, connections, memory, digest (P09 §4N) |
| 16 | Feedback | USER (ORG view) | — | SCR-P21-40 | New node; `packages/feedback` (P21 §4S) |
| 17 | Tutorials & help | USER (ORG curation) | — (help panel SCR-P21-35) | SCR-P21-35, SCR-P21-16 | New node; learning paths, tours re-launch, shortcuts, glossary, "Start here" (ORG) |
| 18 | Security & trust | ORG (read) / PLATFORM (publish) | — | SCR-P23-20 (new) | Vendor documents, sub-processors, certifications, status, DPA, incident notices, evidence packs, auditor grants, questionnaire responder (P23 FR-P23-61) |
| 19 | What's new | USER | — (SCR-P23-19 existed as tenant notices) | SCR-P23-19 | Release cards from FR-P23-59; suppression level (ORG) |
| 20 | About | USER | — | SCR-P03-34 (new) | Product and `brand.app_name`, version, licences, provider entity, Vidhi kernel version, terms, support, Grievance Officer, residency |
| LD+ | Rules and automations · Tools | ORG | Rules and automations (rules, flags part); Tools | SCR-P03-20, SCR-P03-24, SCR-P03-25, SCR-P03-26, SCR-P03-31 | LawDocs additions placed after node 20 in the ORG group |

Platform-only nodes in `apps/console` (after node 20, never in `apps/web`): Tenants & plans, Brand Studio (platform layer), Pricing Studio, Website Studio (CMS, P21), Compliance Documents (Vendor Assurance Room publish — `PLT_SECURITY_OFFICER`), Feature flags & releases, Engineering (P23), AI registry. The Personal workspace shows nodes 1–6, 12 (my data), 13 (my history), 16, 17, 19, 20 and a reduced 7 (home, quick actions) — each ≤ 2 taps from home.

### C.4.18 Mobile tab bars (P22 FR-P22-03 governs; reconciliation R-3 in §C.16)

P22 FR-P22-03 defines the default tab sets (Personal, Company, Consumer Help flavour; none for guests); this table restates them and adds nothing that P22 does not define. Role differences are expressed only through (a) the tenant default for the two middle slots of the Company set (`mob.bottom_bar.items`, re-scoped by R-3) and (b) the user's own order (`mob.nav.tab_order`, USER). Home, Inbox (Company) and the last tab (Me / More) are fixed positions.

| Workspace | Tabs (P22 default) | Who may change what | Floating / quick actions |
|---|---|---|---|
| Personal | Home · Vault · Create · Activity · Me | User reorders (`mob.nav.tab_order`) | Ask Vidhi (floating), Scan, Upload |
| Company (every role) | Home · Inbox · Contracts · Matters · More | Tenant may set the middle slots from the role's mobile-available rail items (e.g., Sign and Board for checkers, approvers and directors) through `mob.bottom_bar.items`; user reorders within the set | Ask Vidhi, Request legal help (where `lgo` is enabled), Scan |
| Consumer Help flavour (v2) | Home · My cases · Evidence · Vehicles · Me | User reorders | Ask, Capture evidence |
| Guest (`CP_GUEST`) | No tab bar; single task | — | Help |

"More" lists the rest of the role's web rail items available on mobile per the parity matrix (P22 §6.1); items marked `W` open a hand-off card ("Continue on the web — we saved your place").

---
## C.5 Universal search, command palette, quick actions, Ask Vidhi and "i"

### C.5.1 Universal search (`/` or the top-bar field)

| Aspect | Rule |
|---|---|
| Indexed objects | Documents (title, metadata, permitted OCR/type-copy text), folders (views), agreements, negotiations, obligations, signing requests, matters, cases (CNR, party, court), hearings, orders, notices, pleadings, trademarks and IP assets, requests, items, meetings, resolutions, people (in scope), engagements, orders, invoices, settings (by label and key), help articles and glossary terms. |
| Trimming | Permission-trimmed in the index per tenant alias and per grant; sealed classes (POSH, privileged matter notes, credential secrets) are never indexed (NN-01, FR-P18-33). Search never crosses contexts: a result in another workspace shows only "1 result in Alpha Pvt Ltd — switch to view" when the user holds that context. |
| Languages | Indic analysers (OpenSearch) with transliteration ("kirayanama" finds "किरायानामा" and "rent agreement"); synonym sets from the glossary; spelling suggestions; PostgreSQL FTS fallback (P04). |
| Performance | ≤ 800 ms p95 for an individual's vault (10,000 documents) and ≤ 1.5 s p95 for 1 million documents per tenant (P04 §1). |
| Results UI | Typed groups (Documents, Contracts, Matters, People, Settings, Help) with counts; facets in a bottom sheet on mobile; "Save view" ≤ 3 clicks; zero results → spelling, other language, glossary, "Ask Vidhi" (SCR-P04-08). |

### C.5.2 Command palette (`Ctrl/Cmd+K`)

The palette combines records, actions and settings (FR-P03-36, FR-P02-57). Seed commands (role-filtered; each maps to a quick-action or screen):

| Group | Commands |
|---|---|
| Create | New document from template… · New NDA · New legal notice · Upload documents · Upload a folder · Scan (mobile) · Add a court case · Add a trademark · Raise a legal request · Start a consumer complaint (brand) |
| Act | Send for signature… · Approve next · Review next change · Request professional review · Book a professional · Export this as a folder · Share… |
| Go to | Home (`g h`) · Inbox (`g i`) · Vault (`g v`) · Settings (`g s`) · any record by business reference (`LD-AGR-2026-000123`, CNR, TM application number) |
| Switch | Switch to <context> · Switch legal entity · Personal workspace |
| Settings | Any setting by label or key (opens the setting drawer SCR-P03-03) · "Change text size" · "Turn on dark mode" |
| Help | Explain <term> (glossary) · Start tour · Contact support · Keyboard shortcuts (`?`) |

Rules: the palette never bypasses a confirmation, step-up or maker-checker step (NN-13, NN-18) — an action command opens the same review screen as the button; commands show their shortcut; recent commands first; agents cannot invoke the palette.

### C.5.3 Quick actions ("+" menu; mobile floating action)

Up to 6 per user (`cfg.quick_actions.max_per_user`), chosen from the module catalogue (FR-P03-35). Defaults per user type:

| User type | Default quick actions |
|---|---|
| `IND_OWNER` | Draft something · Scan · Upload · Send for signature · Ask Vidhi · Add a court case |
| `ORG_LEGAL_MAKER` / delegated maker | New agreement from template · Upload documents · Send for signature · Add a court case · Ask Vidhi · Upload a folder |
| `ORG_CLO` | Raise a legal request (on behalf) · New agreement · Add a court case · Add a trademark · Ask Vidhi · Book a professional |
| `ORG_MEMBER` / `ORG_DEPT_HEAD` | Raise a legal request · Upload documents · Ask Vidhi |
| `ORG_ADMIN` | Invite · Upload a folder · Ask Vidhi · Book a professional |
| `ORG_CHECKER` / `ORG_DIRECTOR` | Approve next · Ask Vidhi |
| Consumer Help user | Start a consumer complaint · Capture evidence · Check challans on official portal · Ask |

Each action deep-links with context (current folder, current matter).

### C.5.4 Ask Vidhi everywhere (P09; Appendix H roster, X-27)

| Surface | Entry | Behaviour |
|---|---|---|
| Public pages | Drafter widget and "Describe your situation" box (SCR-P06-01, SCR-P21-02) | General information only; template automation is free; AI-custom lane labelled (NN-14, CH-30) |
| `apps/web` | Top-bar button, `Ctrl/Cmd+J`, right panel (SCR-P09-05) with record context chip | Tools act on the open record; outputs are cards with sources, confidence and cost (SCR-P09-06); external actions go to the user for confirmation (NN-13) |
| Individual home | Ask box widget (SCR-P09-01) | Answer ≤ 2 taps from home (J-08); emergency hand-off card bypasses payment (P09-AT-13) |
| Mobile | Floating button on Home and document viewer; push-to-talk voice (SCR-P22-23) | AI disclosure first; transcript confirmed before sending |
| Signing ceremony, approval dialogs | "Explain this" only (help mode, `hlp.vidhi_help_mode.enabled`) | Explains terms and the document; never recommends signing; no upsell |
| `apps/delivery` | Panel scoped to the active client grant | Retrieval limited to the grant scope; RM-started output still needs the client's checker (P18-AT-28) |
| Errors | "Ask Vidhi about this error" link beside the "i" | Uses the error's help key; never exposes stack traces |

### C.5.5 Contextual "i" buttons

Per FR-P21-121: an "i" button beside the label (accessible name "About {term}"), click/Enter/Space opens a non-modal popover, Escape closes without moving focus, persistent while hovered or focused (WCAG 1.4.13), target ≥ 24×24 CSS px web and 44×44 pt / 48×48 dp mobile; content = plain definition, "Listen", "Learn more", "Watch". `hlp.inline.explanations` (USER) renders definitions under labels. CI fails on untagged jargon (P21-AT-20). Tenant terminology shows "LawDocs term: Checker" beneath the tenant label (FR-P21-123).

### C.5.6 Keyboard shortcuts

`Ctrl/Cmd+K` palette · `Ctrl/Cmd+J` Ask Vidhi · `/` search · `g h` / `g i` / `g v` / `g s` go to Home / Inbox / Vault / Settings · `n` / `p` next / previous change in the redline and diff views (U.5.1) · `?` shortcut sheet. Single-key shortcuts work only when the user enables them (`cfg.ui.shortcuts_enabled`); all are remappable or can be turned off (WCAG 2.1.4).

---

## C.6 Inbox and notifications

| Element | Rule |
|---|---|
| Inbox kinds | Approvals (maker-checker, DoA, agent actions, exports, grants, reveals) · Signature requests · My items and waiting items (`wf.items`, X-09) · Deal-room replies · Mentions · Deadlines (limitation, hearings, registration windows, renewal notice dates) · Deliverables to accept · Requests assigned · System notices (Correction Entries) |
| Ordering | Legal clocks and statutory deadlines first (earliest last date), then SLA-at-risk, then approvals by age, then the rest; ties by the record's business reference. Deterministic; never AI-ranked. |
| Actions | Open; approve/return from the item with diff (step-up where required); "Review next"; snooze (not for legal clocks); reassign within permissions. No bulk approval of legal-effect, money or access actions (NN-18; P02 rules). |
| Notifications | Every notification names the workspace (FR-P02-09); push taps open the exact item in the right context; quiet hours per context; digests daily or weekly; email has a plain-text alternative (U.7.3); counterparties get one invitation plus stoppable reminders (NN-34). |
| Empty | "Nothing needs you right now." with one next action ("Upload a document" or "Draft something"). |

---

## C.7 Home dashboards

### C.7.1 Widget catalogue (`cfg.widget_catalogue`; FR-P03-33; keys registered by owning modules)

Each widget declares: data API, Cerbos permission, sizes (S 1×1, M 2×1, L 2×2), drill-down screen, accessible table alternative, refresh interval, empty state and whether it may be mandatory.

| Widget key | Title (default) | Owner | Content | Drill-down |
|---|---|---|---|---|
| `w.wf.my_items` | My open items | P03 | Count by ageing bucket + top 5 with clocks as text | SCR-P03-18 |
| `w.wf.waiting_on_others` | Waiting on others | P03 | Who holds what, since when, next chase | SCR-P03-18 |
| `w.wf.due_this_week` | Due this week | P03 | Dated items incl. legal clocks | SCR-P03-19 |
| `w.wf.approvals` | Approvals awaiting me | P02 | Count, oldest, "Review next" | SCR-P02-12 |
| `w.sgn.awaiting_my_signature` | Awaiting my signature | P08 | Requests with due dates | SCR-P08-04 |
| `w.sgn.in_progress` | Out for signature | P08 | Requests by participant state | SCR-P08-07 |
| `w.drf.start` | Draft something | P06 | Search + 6 suggested templates by life stage | SCR-P06-02 |
| `w.drf.continue` | Continue drafts | P06 | Last 5 drafts with lane chip | SCR-P06-05 |
| `w.dms.life_folders` | My vault | P04 | Life-event folder tiles with counts | SCR-P04-01 |
| `w.dms.expiring` | Expiring soon | P04 | Documents with expiry/renewal ≤ 90 days | SCR-P04-13 |
| `w.dms.recent` | Recent documents | P04 | Last 8 opened or added | SCR-P04-04 |
| `w.dms.health` | Vault health | P04 | Issues by severity (text + icon) | SCR-P04-17 |
| `w.clm.renewals` | Renewals | P07 | Renewal notice deadlines in 30/60/90 days | SCR-P07-17 |
| `w.clm.pipeline` | Agreements by stage | P07 | Canonical stages with counts | SCR-P07-14 |
| `w.clm.high_risk` | High-risk clauses pending | P07 | Playbook deviations awaiting decision | SCR-P07-09 |
| `w.clm.obligations` | Obligations due | P07 | Verified obligations by owner | SCR-P07-13 |
| `w.lit.next_hearings` | Next hearings | P11 | Date, court, item, freshness chip | SCR-P11-06 |
| `w.lit.legal_deadlines` | Legal deadlines | P11 | Clocks ≤ 30 days with VERIFIED/ADVISORY badge | SCR-P11-09 |
| `w.lit.outcomes_awaited` | Outcomes awaited | P11 | Hearings without recorded outcome | SCR-P11-01 |
| `w.lit.exposure` | Exposure movement | P11 | Quarter view by class (human-set) | SCR-P11-13 |
| `w.ipm.deadlines` | Trademark deadlines | P12 | Replies, oppositions, renewals | SCR-P12-01 |
| `w.ipm.watch_hits` | Watch hits to decide | P12 | Hits with days left | SCR-P12-10 |
| `w.lgo.intake_queue` | Legal requests | P13 | New/unassigned with SLA chips | SCR-P13-04 |
| `w.lgo.my_requests` | My requests | P13 | Status, "needed from you" | SCR-P13-06 |
| `w.lgo.team_workload` | Team workload | P13 | Assigned counts per person — counts only, no activity data (NN-33) | SCR-P13-04 |
| `w.lgo.legal_spend` | Legal spend | P11/P13 | Approved vs budget, invoices to approve | SCR-P11-12 |
| `w.gov.board_items` | Board items | P13 | Next meeting, papers due, resolutions to sign | SCR-P13-15 |
| `w.gov.my_declarations` | My director compliance | P13 | DIN KYC, DSC expiry, declarations due | SCR-P13-19 |
| `w.ai.ask` | Ask Vidhi | P09 | Ask box + language chip | SCR-P09-01 |
| `w.ai.suggestions` | Vidhi suggestions | P09 | Deterministic triggers (expiring, missing stamp) proposing a task; never auto-acts | SCR-P09-06 |
| `w.agt.workforce` | My AI workforce | P09 | Agents, status, budget burn, **Pause** | SCR-P09-12 |
| `w.sav.year` | Savings this year | P17 | Tiles by evidence class with formula link (NN-36) | SCR-P17-27 |
| `w.bil.plan_usage` | Plan and usage | P17 | Meters vs allowance, renewal date | SCR-P17-10 |
| `w.mkp.my_services` | My services | P16 | Engagements and actions due | SCR-P16-11 |
| `w.mkp.retainer` | Retainer | P16 | Hour bank, SLA attainment | SCR-P16-13 |
| `w.bsv.orders` | Orders | P14 | Milestones, "waiting on" chip | SCR-P14-04 |
| `w.tax.year` | Tax year | P14 | Checklist and status for the current tax year | SCR-P14-09 |
| `w.chp.case_status` | My consumer cases | P15 | Status, waiting on, next deadline | SCR-P15-04 |
| `w.org.setup_checklist` | Finish setting up | P01/P02 | Steps until done, then auto-hides | SCR-P01-11 |
| `w.org.people` | People and roles | P02 | Invites pending, SoD warnings | SCR-P02-04 |
| `w.core.changes_by_lawdocs` | Changes made by LawDocs | P00 | Unacknowledged Correction Entries | SCR-P00-08 |
| `w.int.health` | Integrations | P19 | Degraded connectors with "as of" | SCR-P19-14 |
| `w.sdc.portfolio` | My clients | P18 | Next breach, open tasks, unread, grant expiry | SCR-P18-01 |
| `w.sdc.grants_expiring` | Grants expiring | P18 | Grants ending ≤ 14 days | SCR-P18-20 |
| `w.pro.deliverables` | Deliverables due | P16/P18 | Due, in review, released | SCR-P16-23 |
| `w.pro.payouts` | Payouts | P16 | Route status (read-only) | SCR-P18-27 |
| `w.hlp.learn` | Learn LawDocs | P21 | Next tour, 2 short tutorials | SCR-P21-35 |

### C.7.2 Default layouts and KPIs per persona (**bold** = mandatory: may be moved, not removed)

| Persona | Row 1 | Row 2 | Row 3 | Headline KPIs (text values; formula on "i") |
|---|---|---|---|---|
| `IND_OWNER` | `w.drf.start`, **`w.sgn.awaiting_my_signature`** | `w.dms.life_folders`, `w.dms.expiring` | `w.ai.ask`, `w.drf.continue`, `w.lit.next_hearings` (when cases exist) | Documents in vault · expiring ≤ 90 days · waiting for you |
| `IND_FAMILY_MEMBER` / `IND_DELEGATE` | Shared folders, tasks from owner | `w.dms.recent` | — | Tasks open |
| `ORG_OWNER` / `ORG_ADMIN` | `w.org.setup_checklist` (until done), **`w.core.changes_by_lawdocs`** | `w.wf.approvals`, `w.org.people` | `w.bil.plan_usage`, `w.int.health`, `w.sav.year` | Seats used · approvals pending · integrations degraded |
| `ORG_CLO` | **`w.lit.legal_deadlines`**, `w.lgo.intake_queue` | `w.clm.renewals`, `w.clm.high_risk`, `w.lit.next_hearings` | `w.lgo.team_workload`, `w.lgo.legal_spend`, `w.ipm.deadlines` | Requests within SLA % · agreements expiring ≤ 90 days · hearings this week · open clocks ≤ 30 days · spend vs budget |
| `ORG_LEGAL_MAKER` / `ORG_DELEGATED_MAKER` | **`w.wf.my_items`**, returned to me | `w.wf.due_this_week`, `w.clm.pipeline` (mine) | `w.ai.suggestions` | Items open · returned · due this week |
| `ORG_CHECKER` / `ORG_APPROVER` | **`w.wf.approvals`**, **`w.sgn.awaiting_my_signature`** | `w.clm.pipeline` (awaiting approval) | — | Approvals waiting · oldest age |
| `ORG_DEPT_HEAD` / `ORG_MEMBER` | Request legal help tile, `w.lgo.my_requests` | Contracts of my department | `w.lgo.team_workload` (heads only) | Requests open · needed from me |
| `ORG_DIRECTOR` / `ORG_KMP` | **`w.wf.approvals`**, **`w.sgn.awaiting_my_signature`** | `w.gov.board_items`, `w.gov.my_declarations` | Legal risk summary (frozen, SCR-P13-08) | Papers due · resolutions to sign · declarations due |
| `ORG_AUDITOR_RO` | Audit scope and period | Requests to auditee | — | Items in scope |
| `PRO_*` | `w.pro.deliverables`, engagements | Calendar | `w.pro.payouts` | Deliverables due ≤ 7 days |
| `OPS_RM` | **`w.sdc.portfolio`** | `w.sdc.grants_expiring`, federated `w.wf.my_items` | SLA breaches | Clients at risk · grants expiring · items due |
| `OPS_CONSUMER_CASE_MANAGER` | Case queue by deadline risk | Letters awaiting user approval | Conflict checks pending | Cases ≤ 7 days to a forum deadline |
| Consumer Help user | **`w.chp.case_status`** | Start a complaint tiles | Evidence reminders | Next deadline · waiting on |
| `PLT_SUPER_ADMIN` | Platform health (SCR-P00-01) | Kill switches ON, DLQ, outbox lag | Verification gates open | — |
| `OPS_CONTENT_PUBLISHER` | Review due, scheduled | Stale pages, broken links | CWV and accessibility issues | Pages awaiting review |

### C.7.3 Personalisation and next step

- Users add, remove (non-mandatory), resize and reorder widgets by drag or the "Move" menu; layouts are per user per context (`cfg.home.layout`). The tenant sets defaults per user type or department; brand and platform set the base.
- **Next step banner** (one line above Row 1): the first `wf.items` entry by the §C.6 ordering ("Pay stamp duty for the Noida rent agreement — due today"); deterministic, never an advertisement or upsell.
- Empty home (first run): checklist with ≤ 5 steps and a first-run tour (FR-P21-129); the checklist disappears when done.
- Charts on dashboards always have a data-table toggle and a text summary (Appendix U §U.4 rule 10); KPIs show the formula and source on "i" (FR-P13-17).

---

## C.8 Click budgets

### C.8.1 Counting rule (binding)

1. A **click** is one pointer click, tap or keyboard activation (Enter/Space) that navigates, opens, selects from a list, toggles or commits. A keyboard shortcut counts as one click.
2. Not counted, but stated beside the budget: **+ inputs** (typing, questionnaire answers, choosing a file in the OS picker), **+ OTP**, **+ step-up** (biometric/passkey/MFA, which also serves as the confirmation for legal-effect approvals), **+ hosted** (ESP, Razorpay, IdP consent pages operated by third parties). Scrolling is not counted.
3. "From home" starts on the role home of the correct context, signed in. "From notification" counts the notification tap as click 1. "From the record" starts on the record page.
4. Budgets are maxima at p50 measured in production analytics (`journey.start` / `journey.complete`, aggregated, no PII) and as automated journey tests (`tests/journeys/J-xx.spec.ts` on web, Maestro flows on mobile) that count activations. A regression > 20% at p50 against the last release, or any automated journey above its budget, blocks promotion beyond `ring1` (P23). Budgets are tested with the default navigation; tenant customisation that breaks a budget is shown as a warning in "Preview as user type".

### C.8.2 Top 40 journeys (release gates)

| J | Journey | Start | Path (click by click) | Budget | Source |
|---|---|---|---|---|---|
| J-01 | Draft a rent agreement and send it for Aadhaar eSign with an attached e-stamp | Home (individual) | Draft something (1) → "Rent agreement" (2) → answers → Finish (3) → Send for signing (4) → Attach e-stamp, confirm (5) → add landlord → Send (6) | **≤ 6** + inputs (buy e-stamp instead: ≤ 8 + hosted payment) | P06, P08 |
| J-02 | Check a case's next date | Home | Next hearings widget shows date (0) — or My cases (1) → case card (2) | **≤ 2** | P11 |
| J-03 | Upload a folder of documents | Home | Vault (1) → Upload folder (2) → choose folder → Start import (3) | **≤ 3** + picker | P04, P20 |
| J-04 | Approve as checker | Notification | Notification (1) → Approve on the diff (2) | **≤ 2** + step-up | P02, P07, P22 |
| J-05 | Counterparty signs from the invitation | Invitation e-mail/SMS | Link (1) → OTP → Review and consent (2) → Sign with Aadhaar eSign (3) → hosted ESP → Done (4) | **≤ 4** + OTP + hosted | P08 |
| J-06 | Scan a paper document into the vault (mobile) | Home | Scan (1) → capture pages (2) → Save (3) | **≤ 3** | P04, P22 |
| J-07 | Find a document by title | Home | Search (1) → result (2) | **≤ 2** + query | P04 |
| J-08 | Ask Vidhi and get a cited answer | Home | Ask box (1) → Ask (2) | **≤ 2** + question | P09 |
| J-09 | Start a new document | Home | Draft something (1) → template from suggestions or search (2) → first question shown | **≤ 2** (≤ 3 when browsing the catalogue) | P02, P06 |
| J-10 | Share one document view-only, page range, expiring | Document | Share (1) → pick version/pages (2) → view-only (3) → expiry (4) → recipient (5) → Send (6) | **≤ 6** + inputs | P04 |
| J-11 | Set a reminder from a document | Document | Reminders (1) → offset (2) → Save (3) | **≤ 3** | P04 |
| J-12 | Add a nominee | Home | Vault (1) → Family and nominees (2) → Add nominee (3) → scope (4) → Confirm (5) | **≤ 5** + inputs | P04 |
| J-13 | Business user raises a legal request | Any company page | Request legal help (1) → category (2) → Submit (3) | **≤ 3** + inputs | P13 |
| J-14 | CLO assigns an intake request | Home (CLO) | Request (1) → Accept proposal / choose assignee (2) | **≤ 2** | P02, P13 |
| J-15 | CLO sees agreements expiring in 90 days | Home (CLO) | Renewals widget (1) → 90 days filter (2) | **≤ 2** | P02, P07 |
| J-16 | Maker submits a draft for approval | Draft | Submit for approval (1) → Confirm route (2) | **≤ 2** | P02 |
| J-17 | Guest sees the shared version | Invitation | Link (1) → OTP → View (2) | **≤ 3** (link, OTP, view) | P07 |
| J-18 | Maker decides the first change in a received version | Received version | Open compare (1) → Accept/Reject (2) | **≤ 2** | P07 |
| J-19 | Send an agreed company NDA for DSC signing | Agreed version | Send for signing (1) → method DSC (2) → order (3) → fields auto-placed, confirm (4) → Send (5) | **≤ 6** | P07, P08 |
| J-20 | Add a court case by CNR | Home | Add a court case (1) → CNR or scan → Find (2) → Confirm (3) | **≤ 3** mobile, ≤ 4 web | P11 |
| J-21 | External counsel records a hearing outcome | Utility message link | Link (1) → OTP → 4-field form → Submit (2) | **≤ 2** after opening + OTP | P11 |
| J-22 | Confirm an uploaded order into tasks | Order upload | Review digest (1) → Confirm directions (2) → Create tasks (3) | **≤ 3** | P11 |
| J-23 | Add a trademark by application number | Home | Add a trademark (1) → number → Find (2) → Confirm (3) | **≤ 3** | P12 |
| J-24 | Decide a Journal watch hit | Watch queue | Hit (1) → Decide (2) | **≤ 2** | P12 |
| J-25 | Request a type copy of a handwritten page or WhatsApp screenshot | Document | Make type copy (1) → Confirm language (2) | **≤ 2** | P05 |
| J-26 | Translate a document to English | Document | Translate (1) → English (2) | **≤ 2** | P05 |
| J-27 | Prepare a template legal notice up to the dispatch summary | Notice page | Prepare (1) → answers → Review (2) → sender mode (3) → dispatch channel (4) → recipients (5) → Dispatch summary (6) | **≤ 6** + inputs; dispatch itself needs explicit confirmation (NN-13) | P10 |
| J-28 | Buy a fixed-price service | Service page (signed in) | Buy (1) → package (2) → review fees (3) → Pay (4) → hosted checkout | **≤ 4** + hosted; no account: ≤ 7 taps mobile / ≤ 8 clicks web incl. OTP sign-up | P16 |
| J-29 | Upgrade the plan | Home | Avatar/Settings (1) → Billing (2) → Upgrade with prorated quote (3) | **≤ 3** + checkout | P17 |
| J-30 | Cancel a subscription | Billing overview | Cancel or change plan (1) → Cancel (2) → Confirm (3) | **≤ 3**, never more steps than purchase (NN-50) | P17 |
| J-31 | Download the latest invoice | Home | Avatar → Billing (1) → Latest invoice (2) | **≤ 2** | P17 |
| J-32 | Export everything | Home | Settings (1) → My data (2) → Export everything (3) | **≤ 3** + approval where required | P20 |
| J-33 | Hire an AI agent | Agent catalogue | Choose (1) → sponsor (2) → scope (3) → autonomy (4) → budget (5) → Confirm (6) | **≤ 6** | P09 |
| J-34 | Pause any agent | Any page | Workforce widget or palette (1) → Pause (2) | **≤ 2**, effect ≤ 60 s | P09 |
| J-35 | RM opens a client section | Home (RM) | Client card (1) → section tab (2) | **≤ 2** | P18 |
| J-36 | RM proposes a delivery grant | Client section | Propose grant (1) → scope template (2) → Submit to client (3) | **≤ 3** + inputs | P18 |
| J-37 | Client approves a grant, reveal or deliverable | Notification | Notification (1) → Approve (2) | **≤ 2** + step-up | P18 |
| J-38 | RM reveals a client-granted credential | Client › Credentials | Entry (1) → Request/Reveal with reason (2) → Copy (3) | **≤ 3** + step-up (+ client approval where configured) | P18 |
| J-39 | Consumer reaches a triage result | Consumer Help home | Issue tile (1) → up to 5 one-tap answers (2–6) → result | **≤ 6** | P15 |
| J-40 | Publisher turns a Word file into a scheduled post | Content Studio | Upload DOCX (1) → draft ready (2); Submit (3–5); checker Approve → Schedule (2) | **≤ 2 / ≤ 3 / ≤ 2** by stage | P21 |

### C.8.3 Supplementary budgets (also gated, owned by their phases)

Returning sign-in ≤ 2 taps + code, or 1 with a passkey (P01) · Home → "Verify your identity" ≤ 2 (P01) · Withdraw a marketing consent ≤ 3, or 1 from the message footer (P01) · Invite a colleague ≤ 3 (P01, P02) · Change a DoA value ≤ 4 (P02) · Change text size, theme, language, home widgets ≤ 2 (P03) · "Changes made by LawDocs" ≤ 3 (P00) · Super admin starts a Correction Entry ≤ 4 (P00) · Restore from recycle bin ≤ 3 (P04) · Import a WhatsApp export ≤ 4 (P05) · Attach original + type copy + translation to an annexure ≤ 3 (P05) · "I have filed" → case created ≤ 2 (P10) · Buy a professional review from a draft ≤ 3 (P06, P09) · Approve an agent action from the notification ≤ 2 (P09) · Record a registration receipt ≤ 3 (P08) · Board notice + agenda + pack ≤ 6 steps (P13) · Apply for leave ≤ 2 (P13) · Order status ≤ 2 from home; upload a missing document ≤ 3 from the notification (P14) · Harassment log quick-add ≤ 2 (P15) · Connect Microsoft 365 ≤ 5 from Settings (P19) · Create a webhook ≤ 4 (P19) · Link Udofin for deposits ≤ 3 (P19) · Activate an invited company ≤ 4 from the e-mail (P19) · Export one record ≤ 2 (P20) · Log time ≤ 2 (P18) · Schedule a client meeting ≤ 3 (P18) · Open Vidhi from anywhere on mobile ≤ 1 (P22).

---
## C.9 Design tokens and minimalist UI principles (`packages/tokens`; FR-P00-59, FR-P03-31/32, Appendix U §U.4)

### C.9.1 Minimalist UI principles

1. One primary button per view (filled); secondary actions outlined or in "⋯"; destructive actions never primary-coloured and always confirmed with the object named.
2. Content before chrome: no hero images inside the product; illustrations only in empty states (simple line art, `aria-hidden`).
3. Status by **icon + word + colour** (and pattern in charts), never colour alone (WCAG 1.4.1).
4. White space over borders: separate groups with spacing (`space.6`/`space.8`) before adding lines; cards only for genuinely separate objects.
5. Plain-language labels; legal terms keep their names with an "i"; sentence case everywhere; no all-caps (and never for Indic scripts, which have no case).
6. Motion only to explain change (expand, move, reorder); ≤ 200 ms; none when `prefers-reduced-motion` or `cfg.ui.reduced_motion` is set.
7. Numbers in tabular figures; money right-aligned in tables with currency symbol and Indian grouping; dates never relative alone ("in 3 days · 28-Oct-2026").

### C.9.2 Colour — light theme (contrast computed with the WCAG 2.x relative-luminance formula against the stated background)

| Token | Hex | Use | Contrast | Rule |
|---|---|---|---|---|
| `color.bg` | #F8FAFC | App background | — | — |
| `color.surface` | #FFFFFF | Cards, dialogs, tables | — | — |
| `color.text` | #0F172A | Body text | 17.85:1 on surface | — |
| `color.text.secondary` | #475569 | Secondary text, metadata | 7.58:1 on surface; 7.24:1 on bg | — |
| `color.text.placeholder` | #64748B | Placeholders, hints | 4.76:1 on surface; 4.55:1 on bg | Lightest colour allowed for informative text |
| `color.border.input` | #64748B | Input and control borders | 4.76:1 | Meets 3:1 for UI components (SC 1.4.11) |
| `color.border.divider` | #E2E8F0 | Decorative dividers | 1.2:1 | Never the only boundary of a control |
| `color.disabled` | #94A3B8 | Disabled controls only | 2.56:1 | Disabled state exempt; never for active information |
| `color.primary` | #1E3A8A | Primary buttons, links in UI chrome, selected nav | 10.36:1 on surface; white text on it 10.36:1 | — |
| `color.primary.hover` | #172E6E | Hover/pressed | 12.71:1 | — |
| `color.primary.wash` | #EEF2FB | Selected rows, hover backgrounds | primary text on wash 9.24:1 | Background only |
| `color.link` | #1D4ED8 | Inline links in body text | 6.70:1 | Underlined in body text |
| `color.success` / `.bg` | #166534 / #DCFCE7 | Executed, approved, verified | 7.13:1 on surface; 6.49:1 on bg chip | Icon `circle-check` + word |
| `color.warning` / `.bg` | #92400E / #FEF3C7 | Due soon, advisory, stale data | 7.09:1; 6.37:1 on chip | Icon `triangle-alert` + word; #D97706 (3.19:1) only for non-text fills ≥ 3:1 |
| `color.danger` / `.bg` | #B42318 / #FEE4E2 | Overdue, blocked, failed | 6.57:1; 5.45:1 on chip; white on danger 6.57:1 | Icon `octagon-alert` + word |
| `color.info` / `.bg` | #1D4ED8 / #DBEAFE | Waiting, informational | 6.70:1; 5.49:1 on chip | Icon `info` or `hourglass` + word |
| `color.ai` / `.bg` | #6D28D9 / #F3E8FF | AI label border and text ("AI draft — not reviewed by a professional") | 7.10:1; 6.02:1 on chip | Always with the word "AI"; never used for status (NN-14) |
| `color.focus` | #1D4ED8 ring 2 px + 2 px #FFFFFF offset | Focus indicator | 6.70:1 against surface | Visible in all themes (SC 2.4.11/2.4.13 guidance) |

Consumer Help brand primary (brand token set): `color.primary` #0F766E (5.47:1 on white; white on it 5.47:1), hover #115E59 (7.58:1); `color.primary.wash` #E6F4F1 (primary text on it 4.84:1).

### C.9.3 Colour — dark theme

| Token | Hex | Contrast |
|---|---|---|
| `color.bg` | #0B1220 | — |
| `color.surface` | #121A2B | — |
| `color.surface.raised` | #1A2438 | — |
| `color.text` | #E5E9F0 | 14.27:1 on surface; 12.74:1 on raised |
| `color.text.secondary` | #A9B4C6 | 8.30:1 on surface; 7.41:1 on raised |
| `color.border.input` | #7C8BA5 | 5.04:1 on surface (≥ 3:1) |
| `color.border.divider` | #2A3650 | decorative only |
| `color.primary` | #8AB4FF | 8.32:1 on surface; text on primary button #0B1220 8.96:1 |
| `color.success` / chip bg | #4ADE80 / #0F2E1D | 9.97:1 on surface; 8.43:1 on chip |
| `color.warning` / chip bg | #FBBF24 / #3A2A06 | 10.41:1; 8.31:1 |
| `color.danger` / chip bg | #F87171 / #3B1414 | 6.28:1; 5.86:1 |
| `color.info` / chip bg | #93C5FD / #13254A | 9.64:1; 8.37:1 |
| `color.ai` / chip bg | #C4B5FD / #2A1B4A | 9.41:1; 8.40:1 |
| Consumer Help primary | #5EEAD4 | 11.75:1 on surface; #0B1220 text on it 12.66:1 |

**High-contrast themes** (LOCKED available to every user, FR-P03-31): light = #000000 on #FFFFFF (21:1), links #0000EE (9.4:1), focus 3 px #000000 + 2 px offset; dark = #FFFFFF on #000000 (21:1), focus #FFFF00 (19.56:1). Windows forced-colours mode honoured with system colours (U.7.1). CI validates every brand and tenant theme in all four themes; a failing tenant theme cannot be saved (P03-AT-07).

### C.9.4 Typography

| Token | Size / line height (px) | Use |
|---|---|---|
| `type.display` | 36/44 | Public site hero only |
| `type.h1` | 28/36 | Page title (one per page) |
| `type.h2` | 22/30 | Section |
| `type.h3` | 18/26 | Sub-section, card title |
| `type.body` | 16/24 | Default body and controls (minimum body size web 16 px, mobile 16 pt — U.4) |
| `type.body.sm` | 14/20 | Metadata, table secondary lines — never for instructions, errors or legal text |
| `type.legal` | 17/28 serif | Long-form legal documents in viewers and previews |
| `type.mono` | 14/20 | Business references, hashes (grouped in fours), CNR, application numbers |

Families (self-hosted subsets, loaded per active locale, `font-display: swap`; FR-P21-55): **Noto Sans** (Latin) and Noto Sans Devanagari, Bengali, Gurmukhi, Gujarati, Tamil, Telugu, Kannada, Malayalam for UI; **Noto Serif** + matching Noto Serif scripts for legal text; **Noto Sans Mono** for IDs; a dyslexia-friendly option from the token set (`cfg.ui.dyslexia_font`). Weights 400/500/600/700; emphasis by weight, not italics (most Indic scripts have no true italics). Text scale 100–200% (`cfg.ui.text_scale_percent`) with reflow to 400% zoom at 320 CSS px without horizontal scrolling (FR-P03-32).

### C.9.5 Spacing, shape, elevation, motion, density, breakpoints

```json
{
  "space": {"0":0,"1":4,"2":8,"3":12,"4":16,"5":20,"6":24,"8":32,"10":40,"12":48,"16":64},
  "radius": {"sm":4,"md":6,"lg":10,"xl":14,"pill":9999},
  "elevation": {"0":"none","1":"0 1px 2px rgba(15,23,42,.08)","2":"0 4px 12px rgba(15,23,42,.10)","3":"0 12px 32px rgba(15,23,42,.14)"},
  "motion": {"fast":"120ms","base":"200ms","slow":"320ms","easing":"cubic-bezier(.2,0,0,1)","reduced":"0ms; no parallax; no auto-play"},
  "density": {"comfortable":{"row":48,"control":40},"compact":{"row":36,"control":32},"spacious":{"row":56,"control":48}},
  "target": {"web_min":24,"web_default":40,"mobile_min_pt":44,"android_min_dp":48},
  "breakpoints": {"xs":360,"sm":640,"md":768,"lg":1024,"xl":1280,"2xl":1536},
  "layout": {"form_max":720,"content_max":1200,"rail":240,"rail_collapsed":72,"right_panel":400,"topbar":56}
}
```

Density changes row and control height only; touch targets never fall below `target.*`; compact density is not offered on mobile.

---

## C.10 Component library (`packages/ui` on shadcn/ui + Radix; React Native equivalents in `apps/mobile`)

| Family | Components | Accessibility pattern (Appendix U) |
|---|---|---|
| Shell | AppShell, TopBar, ContextSwitcher (combobox), Rail (with Pinned, More, Discover), BottomTabBar, ContextBand, DeliveryBanner, SystemBanner stack, Footer | Landmarks; skip link; switcher announces new context |
| Find and act | SearchBox, ResultsList, FacetPanel/Sheet, CommandPalette, QuickActionMenu, SavedViewMenu | Combobox/listbox; results count in live region |
| Help | HelpPopover ("i"), HelpPanel, TourStep, GlossaryTerm (`<dfn>`), ListenButton (TTS), VideoFacade with captions | Non-modal popover (FR-P21-121); dialog per tour step |
| Vidhi | AskBox, VidhiPanel, OutputCard (sources, confidence, cost, Accept/Edit/Reject), CitationChip (Verified/Unverified), AILabel, VoiceInput (push-to-talk), AgentCard with Pause, DigestCard | `log` region; streamed answer announced once complete (U.5.7) |
| Forms | Field (label + hint + error), OTPInput (single field, `one-time-code`), DateInput (typed + optional picker), MoneyInput (INR), PAN/GSTIN/CIN/IFSC/PIN inputs (normalising), Select, Combobox, Checkbox, RadioGroup, Switch (with text state), Stepper, ErrorSummary, ConsentBlock (unticked, equal choices — P01-AT-19) | U.4.3–4.4 |
| Data | DataTable (TanStack; sortable headers, row selection, bulk bar, virtualisation with `aria-rowcount`), CardList (narrow), Tree (org, folders), Kanban with list alternative, Timeline (ordered list), Calendar (agenda default + grid), KPI tile, Chart with table toggle | U.5.3, U.5.4 |
| Documents | DocumentViewer (text layer, zoom buttons), RenditionSwitcher (Original · Type copy · Translation, with labels and confidence), RedlineViewer, CompareView (side-by-side / inline / Before-After), ChangeList (n/p), AnnexureBuilder (buttons for reorder), SignatureFieldPlacer (page + position form alternative), Scanner (mobile), FolderUpload ("Choose folder" + drop), WatermarkPreview, RedactionTool (text-pattern mode) | U.5.1, U.5.5, U.5.9 |
| Workflow | ApprovalCard, DiffView ("Field: old → new"), StepUpDialog, ConfirmDialog (object named; typed confirmation for master data and bulk delete), StatusChip, FreshnessChip ("Data from {vendor} · as of 10:42"), ClockCountdown (text "6 days left — last date 31-Oct-2026"), EligibilityBadge (eSign valid · Wet-ink needed · Registration required), FormalitiesChecklist, WaitingOnChip | U.5.8 |
| Communication | Thread/Chat log, Composer with AudienceBanner ("Internal — not visible to {counterparty}"), MessageCorrection (no delete; NN-02), NotificationItem, DigestEmail templates | U.5.7; NN-37 |
| Commerce | PriceCard / FeeBreakdown (duty, government fee, professional fee, LawDocs fee, GST, total last; read as a table), PlanCard, ComparisonTable, CheckoutSummary (focus to total before Pay), PlanLockCard ("Not in your plan — see what it does") | P17 UX; NN-22, NN-50 |
| Security | MaskedSecret with reveal countdown and copy, GrantBadge (scope, expiry), KillSwitchToggle (dual control), AccessLogTable, ProtectedScreen wrapper (mobile secure flag) | NN-16, NN-44 |
| Feedback | Toast (status/alert; undo 10 s default, `cfg.toast_undo_seconds`), EmptyState, ErrorState, Skeleton, ProgressBar/JobCard, LiveRegion | §C.11 |

Every component ships with: tokens only (no raw hex), light/dark/high-contrast stories, an axe test, keyboard map, RTL-safe logical properties (for future Arabic/Urdu UI), and a React Native counterpart or an explicit "web only" note in `parity.json` (P22).

---

## C.11 Empty, error and loading states

### C.11.1 Empty states

Pattern: one sentence of what belongs here, one primary next action, optional two suggestions; line illustration `aria-hidden`; never a sales pitch. Examples from phases: "Your vault is empty — scan your first document" (SCR-P04-01), "No matters yet — import your register or add a case by CNR" (SCR-P11-01), "No one is holding you up" (SCR-P03-18), "Nothing needs you right now" (Inbox), "LawDocs has not corrected any of your records. If we ever do, it will appear here with the reason and who approved it." (SCR-P00-08), "No agents yet — start with Vidhi · Contract Drafter" (SCR-P09-12).

### C.11.2 Error states

| Type | Presentation | Copy pattern |
|---|---|---|
| Field validation | Inline under the field + error summary at top on submit; focus moves to the summary | "Enter a 10-character PAN, for example ABCDE1234F." |
| Business rule block | Card above the primary action with reason, fix and "i" | "This document cannot be signed electronically. Wills are excluded by the IT Act First Schedule. Get a wet-ink signing pack instead." + `LD-SGN-014` + `hlp.sgn.esign_eligibility` |
| Permission | Neutral message; unknown or cross-tenant IDs return the same 404 (NN-01, P00-AT-02) | "You do not have access to this item. Ask your admin, or switch workspace." |
| Plan limit | PlanLockCard; never modal; dismissible 30 days | "Not in your plan — see what it does." |
| Flag OFF pending [VERIFY] (NN-38) | Feature card in advisory or disabled state | "Coming soon — under legal review." (SCR-P05-11) |
| Kill switch engaged | Banner on affected screens; alternatives listed | "Aadhaar eSign is paused. You can sign with DSC or request a wet-ink pack." |
| Vendor degraded / stale | Banner with "as of" and the fallback | "Court data from {vendor} is delayed (as of 09:10). Check the court record before relying on it." |
| System failure | ErrorState with retry, what was saved, error code and trace ID; never "Oops" | "We could not save your changes. Nothing was sent. Try again. Code LD-DMS-031 · Trace 7f3a…" |
| Offline (mobile) | Offline badge; cached-only notice; queued actions list | "You are offline. Showing saved copies. 2 uploads will send when you reconnect." |

Every `LD-<MODULE>-<NNN>` error carries a help key and the "i" link (FR-P21-127).

### C.11.3 Loading states

- < 300 ms: no indicator. 300 ms–2 s: skeletons matching the final layout (no layout shift; CLS ≤ 0.1). > 2 s: progress bar with stage text. Long jobs (Temporal: imports, exports, OCR, bundles, agent missions): a JobCard with stages, ETA, "We'll notify you" and safe navigation away; completion arrives in the Inbox and as push.
- Live regions announce start and completion politely; no per-token or per-percent announcements (U.5.7).
- Optimistic UI only for reversible, internal actions (star, pin, reorder); never for send, sign, pay, share, file, approve or delete (NN-13).

---

## C.12 Responsive and mobile rules

| Width | Layout |
|---|---|
| ≥ 1,280 px | Full shell: rail 240 px, main, optional right panel 400 px; record pages two columns |
| 1,024–1,279 px | Rail collapses to 72 px; right panel becomes an overlay; tables keep columns with optional detail rows |
| 768–1,023 px (tablet) | Rail as drawer; record pages single column with section menu; editors that need precision (bundle builder, data sheet, kiosk) supported here (P11, P12, P08) |
| < 768 px | Phone layout: bottom navigation (role's first four items + More, FR-P02-58); tables become card lists that keep header–value pairs (U.5.4); drawers open full screen; filters in bottom sheets; sticky primary action at the bottom that never obscures focus |
| 320–360 px | Minimum supported; no horizontal page scroll; only data tables inside their own region may scroll horizontally (FR-P21 SCR-P21-08) |

Mobile app rules: one-hand reach for approve, sign and scan; biometric unlock device-local (NN-44); protected screens set the secure flag; push deep-links into the right workspace; offline encrypted cache partitioned by `(tenant_id, legal_entity_id, workspace)` (FR-P22-03); `W` items hand off to web with state saved; cold start < 2.5 s mid-range Android (P22 §1); voice input on all free-text fields; captions on by default.

---

## C.13 Multilingual layout rules (D-07; NN-48)

1. **Launch UI languages:** English, Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Kannada, Malayalam, Punjabi. Document input (OCR/translation) supports all 22 Eighth-Schedule languages and the six UN languages; their rendering in viewers uses the matching Noto family.
2. **Line height:** Latin body 1.5; Devanagari, Bengali, Gurmukhi and Gujarati body ≥ 1.6; Tamil, Telugu, Kannada and Malayalam body ≥ 1.7 to keep matras and stacked conjuncts clear of adjacent lines [REC; verify with native-reader usability tests in P21]. Headings never below 1.3 in any script. Controls grow in height rather than clip glyphs.
3. **Text expansion:** design labels for +40% length; buttons wrap to two lines rather than truncate; never truncate legal terms; tooltips are not used to reveal truncated labels.
4. **No case or tracking tricks:** no uppercase transforms, no letter-spacing on Indic scripts, no italic emphasis (use weight).
5. **Fonts per locale:** load only the active locale's subset; fall back to Noto Sans for mixed-script content (English legal terms inside Hindi UI); set `lang` on every segment that changes language so screen readers switch voices (SCR-P05-08, SCR-P06-07).
6. **Numbers and dates:** Western Arabic numerals with Indian grouping for money, IDs, dates and counts in every locale (legal and banking documents use them); month names localised; IST shown.
7. **Legal terms:** statutory labels are LOCKED; translations of legal terms come from the reviewed glossary; machine translations are labelled until a human reviewer for that language approves (NN-48, FR-P21-126); unapproved locales fall back to English with a notice.
8. **Bilingual documents:** side-by-side columns with a governing-language selector (SCR-P06-07); on phones, a language toggle per clause rather than two narrow columns.
9. **Input:** transliteration and native keyboards accepted in search and forms; names stored as entered with an optional Latin transliteration for matching (name-match rules P01).
10. **Right-to-left:** components use logical CSS properties so Urdu/Arabic document views and any future RTL UI mirror correctly; not a launch UI language.

---

## C.14 Customisation surfaces

| Surface | Individual (USER) | Company user (USER) | Department / tenant admin (DEPARTMENT/TENANT) | Brand / platform | Locked parts |
|---|---|---|---|---|---|
| Rail and menus (`cfg.nav.*`) | Pin ≤ 8, reorder pins | Pin ≤ 8, reorder pins, reorder primary items | Hide modules, reorder, rename, landing page per user type, preview as user type | Base trees, max pins | LOCKED items (N-2); ≤ 7 primary |
| Home (`cfg.home.layout`) | Add, remove, resize, reorder widgets | Same | Default layout per user type or department; mandatory widgets | Base layouts | Mandatory widgets cannot be removed |
| Quick actions (`cfg.quick_actions.set`) | Choose ≤ 6 | Choose ≤ 6 | Defaults per user type | Catalogue, max 6 | — |
| Mobile tabs (`mob.nav.tab_order`) | Reorder within workspace set | Reorder | Default middle slots | Tab sets per workspace (P22) | Home first |
| Appearance (`cfg.theme.*`, `cfg.ui.*`) | Mode, text size, density, reduced motion, underline links, dyslexia font | Same | Tenant theme (contrast-validated), logo, colour band, default mode, density default | Brand tokens | High contrast always available; accessibility preferences follow the person and cannot be overridden by tenants (FR-P03-32) |
| Terminology and labels (`cfg.terminology.overrides`) | — | — | Rename non-statutory labels and fields per locale | Platform translations | Statutory labels; canonical names in APIs and exports |
| Language (`cfg.ui.language`) | Any launch language | Same | Default per entity/branch | Enabled set | — |
| Saved views | Save, share with self | Save, share with user type/department | Publish official views | — | — |
| Notifications | Channels, quiet hours, digest time | Same per context | Mandatory types, communication templates (DLT IDs) | Channel adapters | Security and legal-clock notices cannot be muted |
| Shortcuts (`cfg.ui.shortcuts_enabled`) | On/off, remap | On/off, remap | — | Defaults | — |
| Inline help (`hlp.inline.explanations`) | On/off | On/off | Tenant help notes (`hlp.tenant_notes.enabled`) | Glossary | Legal definitions |

Every change is a setting registered in Appendix R before code reads it (NN-29), effective within 60 seconds for OPEN keys and undoable (P03-AT-03); no customisation needs Super Admin or a code release.

---
## C.15 Consolidated screen inventory (every `SCR-Pxx-nn`, compiled 25 October 2026)

Compiled from each phase §6 by script; 515 screens (re-run at registry review G4, 25 Oct 2026: SCR-P08-17 added); no screen ID is referenced anywhere in the pack without an inventory row except the three IDs proposed in §C.16 R-8 (SCR-P03-33…35, pending registration in P03), and no duplicate IDs exist. Gaps in numbering are intentional where a phase grouped its screens (P16 uses 01–15 public/web, 20–25 delivery, 30–32 console; P17 uses 01–06 public/purchase, 10–28 settings, 40–44 console). The phase §6 row is the content specification; this table is the registry used for routing, `cfg.nav_items`, `data-tour-id` binding and tutorial capture.

**Persona codes.** IND `IND_OWNER` · FAM `IND_FAMILY_MEMBER` · DLG `IND_DELEGATE` · GDN `IND_GUARDIAN` · NOM `IND_NOMINEE` · ADM `ORG_OWNER`/`ORG_ADMIN` · CLO `ORG_CLO` · MKR `ORG_LEGAL_MAKER`/`ORG_DELEGATED_MAKER` · CHK `ORG_CHECKER`/`ORG_APPROVER` · DEP `ORG_DEPT_HEAD`/`ORG_MEMBER` · DIR `ORG_DIRECTOR`/`ORG_KMP`/`ORG_BOARD_OBSERVER` · AUD `ORG_AUDITOR_RO` · EXT `ORG_EXT_COUNSEL` · ICM POSH Internal Committee members (custom role, sealed scope) · CP `CP_GUEST` · PRO `PRO_*` · RM `OPS_RM`/`OPS_DELIVERY_LEAD` · OPS other `OPS_*` (onboarding, professional, QA, support) · CCM `OPS_CONSUMER_CASE_MANAGER` · CHU Consumer Help user · CPUB `OPS_CONTENT_PUBLISHER` · CED `PLT_CONTENT_EDITOR` · LRV `PLT_LEGAL_REVIEWER` · PLT `PLT_SUPER_ADMIN` · SEC `PLT_SECURITY_OFFICER` · SRE `PLT_SRE` · REL `PLT_RELEASE_MANAGER` · DPO `PLT_DPO` · PAUD `PLT_AUDITOR_RO` · PTN ecosystem partner admin · DEV API integrator · ANON visitor · ALL any signed-in user of the app.

### C.15.1 P00 — Foundations, Repository Discovery and Migration (11)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P00-01 | console › Home | PLT, SRE | Platform health |
| SCR-P00-02 | console › Tenants | PLT | Tenant list and detail (provisioning only in P00) |
| SCR-P00-03 | console › Platform › Flags & kill switches | PLT, SEC | Manage flags |
| SCR-P00-04 | console › Audit › Platform chain | PAUD, SEC | Explore and verify |
| SCR-P00-05 | console › Audit › Corrections | PLT, SEC | Create and approve Correction Entries |
| SCR-P00-06 | console › Platform › Migration | PLT, SRE | Migration console |
| SCR-P00-07 | console › Platform › Events | PLT, SRE | Outbox and integration health |
| SCR-P00-08 | my.lawdocs.in › Settings › Audit & history › Changes made by LawDocs | ADM, AUD | Tenant view of platform corrections |
| SCR-P00-09 | my.lawdocs.in › Settings › Audit & history › Integrity | ADM, AUD, IND | Tenant chain verification |
| SCR-P00-10 | console › Website › Redirects | PLT, CPUB | Redirect map |
| SCR-P00-11 | console › Platform › Disposition register | PLT, DPO | Asset dispositions |

### C.15.2 P01 — Identity, Onboarding, KYC/KYB and Consent (22)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P01-01 | auth.lawdocs.in | ALL | Sign-in / sign-up |
| SCR-P01-02 | auth | ALL | OTP entry |
| SCR-P01-03 | web/mobile | ALL | Passkey prompt after first sign-in |
| SCR-P01-04 | www side panel | ANON | Anonymous draft save sheet |
| SCR-P01-05 | web | ALL | Security settings |
| SCR-P01-06 | web | IND, ADM | Verification centre ("Verify your identity") |
| SCR-P01-07 | web | IND | DigiLocker consent and result |
| SCR-P01-08 | web | IND | Aadhaar offline verification |
| SCR-P01-09 | web | ADM | Company discovery |
| SCR-P01-10 | web | ADM | Company profile card |
| SCR-P01-11 | web | ADM | Company set-up wizard (steps 4–7) |
| SCR-P01-12 | web | ADM, DIR | Signatory authority |
| SCR-P01-13 | delivery (practitioner) | PRO | Professional application |
| SCR-P01-14 | console / delivery | OPS, PLT | KYB and credential review queue |
| SCR-P01-15 | guest | CP | Guest landing |
| SCR-P01-16 | web | GDN | Wards (guardian) |
| SCR-P01-17 | web | IND, NOM | Nominees |
| SCR-P01-18 | web | ALL | Privacy centre |
| SCR-P01-19 | console | PLT, DPO | Notice versions and consent purposes |
| SCR-P01-20 | console | PLT | Identity providers and KYC/KYB vendors |
| SCR-P01-21 | console / OH4 | OPS, PTN | Partner onboarding requests |
| SCR-P01-22 | web | ADM | SSO and SCIM settings |

### C.15.3 P02 — Tenancy, Organisation Structure, User Types and Maker-Checker (18)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P02-01 | all | ALL | Context switcher |
| SCR-P02-02 | web | ADM | Organisation structure |
| SCR-P02-03 | web | ADM, DEP | Department detail |
| SCR-P02-04 | web | ADM | People |
| SCR-P02-05 | web | ADM | Person access detail |
| SCR-P02-06 | web | ADM | Invite / grant wizard |
| SCR-P02-07 | web | ADM | Roles catalogue |
| SCR-P02-08 | web | ADM | Custom role builder |
| SCR-P02-09 | web | ADM, CLO | DoA tables |
| SCR-P02-10 | web | ADM, CLO, MKR | "Who approves?" simulator + gap check |
| SCR-P02-11 | web | ADM | Maker-checker settings |
| SCR-P02-12 | web/mobile | CHK, DIR | Approvals inbox |
| SCR-P02-13 | web | ALL | Delegation and away |
| SCR-P02-14 | web | ADM | Outsider access (grants) |
| SCR-P02-15 | web | ADM, DEP | Access reviews |
| SCR-P02-16 | web (Personal) | IND | Who can see my vault |
| SCR-P02-17 | delivery / web | RM, ADM | Master-data change request |
| SCR-P02-18 | web | ALL | Home (role-based) |

### C.15.4 P03 — Configuration Studio, Rule Engine and Settings (32)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P03-01 | web, delivery | ADM, RM | Settings home |
| SCR-P03-02 | web, delivery | ADM | Section page |
| SCR-P03-03 | web, delivery | ADM | Setting drawer |
| SCR-P03-04 | web | ADM | Change request composer |
| SCR-P03-05 | web, mobile | CHK, ADM | Change approval card (Inbox) |
| SCR-P03-06 | web | ADM | Appearance |
| SCR-P03-07 | web, mobile | ALL | Home and quick actions |
| SCR-P03-08 | web | ADM | Menus |
| SCR-P03-09 | web | ADM | Terminology and labels |
| SCR-P03-10 | web | ADM | Custom fields |
| SCR-P03-11 | web | ADM | Status sets |
| SCR-P03-12 | web | ADM | Numbering schemes |
| SCR-P03-13 | web | ADM | Form designer |
| SCR-P03-14 | web | ADM | Communication templates |
| SCR-P03-15 | web | ADM | Documents and letterheads |
| SCR-P03-16 | web | ADM, CLO | Item types |
| SCR-P03-17 | web | ADM, CLO | Chase policies and ladders |
| SCR-P03-18 | web, mobile | ALL | My items / Waiting on others |
| SCR-P03-19 | web, mobile | ALL | Item detail |
| SCR-P03-20 | web | ADM, CLO | Rules adopted |
| SCR-P03-21 | console | CED | Rule-set editor |
| SCR-P03-22 | console | LRV | Review queue (reviewer of record) |
| SCR-P03-23 | console | CED, LRV | Content and rule release calendar |
| SCR-P03-24 | console, web | PLT, ADM | Flags and kill switches |
| SCR-P03-25 | web | ADM | Templates, import, compare, sandbox |
| SCR-P03-26 | web, console | ADM, PLT | Configuration Health |
| SCR-P03-27 | web | ADM, AUD | Changes made by LawDocs |
| SCR-P03-28 | console | PLT | Tenant override console |
| SCR-P03-29 | web, mobile | ALL | Personal settings |
| SCR-P03-30 | web | ADM, IND | Automations and agents |
| SCR-P03-31 | web | ADM | Explain my configuration |
| SCR-P03-32 | delivery | RM | RM proposal view |
| SCR-P03-33 *(v1.1)* | web | ADM | Security policy (password, MFA, sessions, IP allow-list, BYOK, audit-log link) |
| SCR-P03-34 *(v1.1)* | web/mobile | ALL | About (product, display name, version, licences, provider entity, kernel version, residency) |

### C.15.5 P04 — Legal Vault and DMS (20)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P04-01 | web, mobile | IND, FAM, DLG | Vault home |
| SCR-P04-02 | web | ADM, CLO, MKR, DEP | Company DMS home |
| SCR-P04-03 | web, mobile | ALL | Folder view / list |
| SCR-P04-04 | web, mobile | ALL | Document page |
| SCR-P04-05 | web, mobile | ALL | Upload and classify sheet |
| SCR-P04-06 | mobile | ALL | Scanner |
| SCR-P04-07 | web | ADM, MKR | Bulk intake mapping preview |
| SCR-P04-08 | web, mobile | ALL | Search |
| SCR-P04-09 | web, mobile | IND, MKR | Share pack builder |
| SCR-P04-10 | web, mobile | CP | Recipient viewer (external) |
| SCR-P04-11 | web, mobile | IND, ADM | Sharing activity |
| SCR-P04-12 | web | MKR, CLO | Redaction tool |
| SCR-P04-13 | web, mobile | IND, ADM | Reminders and Expiring soon |
| SCR-P04-14 | web, mobile | IND | Family and nominees |
| SCR-P04-15 | web, mobile | NOM | Nominee claim (claimant) |
| SCR-P04-16 | web | ADM, CLO | Retention, holds and disposal |
| SCR-P04-17 | web, mobile | IND, ADM | Vault health |
| SCR-P04-18 | web, mobile | IND, ADM | Recycle bin |
| SCR-P04-19 | web | ADM | DMS settings (tenant) |
| SCR-P04-20 | web, mobile | IND | Add from DigiLocker |

### C.15.6 P05 — Document Intelligence: OCR, Type Copy, Translation (12)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P05-01 | web, mobile | IND, MKR | Document intelligence panel (on P04 document page) |
| SCR-P05-02 | web, mobile | IND, MKR | Type copy request |
| SCR-P05-03 | web | IND, MKR, PRO | Side-by-side correction editor |
| SCR-P05-04 | mobile | IND | Line-by-line confirm |
| SCR-P05-05 | web, mobile | IND, MKR | Verification and attestation |
| SCR-P05-06 | web | IND, MKR | WhatsApp import |
| SCR-P05-07 | web | IND, MKR, PRO | Chat type copy view |
| SCR-P05-08 | web, mobile | IND, MKR | Translation view |
| SCR-P05-09 | web, mobile | IND, MKR | Certified translation order |
| SCR-P05-10 | web | MKR | Extraction review |
| SCR-P05-11 | web | IND, MKR | s.63 certificate (Part A) |
| SCR-P05-12 | console | PLT, SRE | Evaluation and engines |

### C.15.7 P06 — Template Library and AI Drafting Studio (19)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P06-01 | public | ANON | Drafting widget on every document page |
| SCR-P06-02 | public/web | ANON, IND, MKR | Template catalogue |
| SCR-P06-03 | web/mobile | ANON, IND, MKR | Interview + live preview |
| SCR-P06-04 | web/mobile | IND | Lane chooser and escalation warning |
| SCR-P06-05 | web | IND, MKR | Draft workspace |
| SCR-P06-06 | web/mobile | IND, MKR | Vidhi panel |
| SCR-P06-07 | web | IND, MKR | Bilingual side-by-side |
| SCR-P06-08 | web/mobile | IND, MKR | Export dialog |
| SCR-P06-09 | web/mobile | IND | Request professional review |
| SCR-P06-10 | delivery | PRO, OPS | Review workbench |
| SCR-P06-11 | console | CED | Template Studio — template editor |
| SCR-P06-12 | console | CED | Questionnaire builder |
| SCR-P06-13 | console/web | CED, CLO | Clause library |
| SCR-P06-14 | console | CED | Variants and languages |
| SCR-P06-15 | console/web | LRV, CLO | Review and publish (checker) |
| SCR-P06-16 | console | CED, LRV | Content legal-review backlog board |
| SCR-P06-17 | console/web | CED, CLO | Template analytics |
| SCR-P06-18 | web | CLO, ADM | Tenant templates and playbooks |
| SCR-P06-19 | console/web | CED | Template test harness |

### C.15.8 P07 — Contract Lifecycle, Negotiation, Redlines, Deal Rooms (19)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P07-01 | web/mobile | DEP | Intake form |
| SCR-P07-02 | Teams | DEP | Teams app card |
| SCR-P07-03 | web | CLO, MKR | Intake queue |
| SCR-P07-04 | web/mobile | MKR, CLO, DEP | Agreement overview |
| SCR-P07-05 | web/mobile | MKR, CP | Deal room |
| SCR-P07-06 | web | MKR | Compare view |
| SCR-P07-07 | web | MKR | Share dialog + leakage check |
| SCR-P07-08 | web/mobile | MKR, CP | Clause editor |
| SCR-P07-09 | web | MKR, CLO | Playbook review results |
| SCR-P07-10 | web/mobile/Teams/email | CHK, DIR | Approval card |
| SCR-P07-11 | web | ADM, CLO | DoA matrix editor |
| SCR-P07-12 | web/mobile | MKR, CP | Agreed version and lock |
| SCR-P07-13 | web/mobile | MKR, CLO | Obligations and key dates |
| SCR-P07-14 | web | CLO, MKR, AUD | Repository |
| SCR-P07-15 | web | MKR | Legacy import verification queue |
| SCR-P07-16 | web | CLO | CLO dashboard |
| SCR-P07-17 | web | CLO, MKR | Renewal decision |
| SCR-P07-18 | web | MKR | Bulk contracting |
| SCR-P07-19 | public (guest) | CP | Guest landing |

### C.15.9 P08 — eSign, eStamp, Execution and Evidence (17)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P08-01 | web, mobile | IND, MKR | Prepare for signing |
| SCR-P08-02 | web, mobile | IND, MKR | Stamp panel |
| SCR-P08-03 | web, mobile | IND, MKR | Attach existing e-stamp |
| SCR-P08-04 | web, mobile | CP, IND, DIR | Signer page |
| SCR-P08-05 | web, mobile | CP, IND | Consent and method |
| SCR-P08-06 | desktop web | DIR, CHK | DSC signing |
| SCR-P08-07 | web, mobile | IND, MKR | Request tracker |
| SCR-P08-08 | web | MKR | Bulk batch |
| SCR-P08-09 | web, mobile | IND, MKR | Formalities |
| SCR-P08-10 | web, mobile | IND, MKR | Wet-ink / notary / registration pack |
| SCR-P08-11 | web, mobile | IND, MKR, AUD | Evidence pack |
| SCR-P08-12 | public web | ANON | Verify a document |
| SCR-P08-13 | web (assisted) | OPS, CP | Kiosk mode |
| SCR-P08-14 | console | PLT | Providers |
| SCR-P08-15 | console | CED, LRV | Eligibility, duty and State registry content |
| SCR-P08-16 | web | ADM | Signing settings (tenant) |
| SCR-P08-17 | web, mobile, kiosk | IND, CP, OPS | Signing assistance (helper, witness, accessible reading view; FR-P08-57) |

### C.15.10 P09 — Vidhi AI Employee and Agent Workforce (25)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P09-01 | web, mobile, public | IND, ANON | Ask Vidhi (individual) |
| SCR-P09-02 | web, mobile | IND | Problem card |
| SCR-P09-03 | web, mobile | IND | Options |
| SCR-P09-04 | web, mobile | IND | Emergency hand-off |
| SCR-P09-05 | web | ADM, CLO, MKR, PRO | Vidhi panel (company/pro) |
| SCR-P09-06 | web, mobile | ALL | Output card |
| SCR-P09-07 | web | ALL | Citation viewer |
| SCR-P09-08 | delivery, web | PRO | QRG reviewer workspace |
| SCR-P09-09 | web, mobile | IND | QRG purchase and status |
| SCR-P09-10 | web | ADM, IND | Agent catalogue |
| SCR-P09-11 | web | ADM, IND | Hire agent wizard |
| SCR-P09-12 | web, mobile | ADM, IND | My AI workforce |
| SCR-P09-13 | web | ADM | Agent detail and activity log |
| SCR-P09-14 | web, mobile | MKR, CHK, IND | Approvals for agent actions |
| SCR-P09-15 | web, mobile, email | ALL | Daily digest |
| SCR-P09-16 | web | ADM | Agent Review (monthly) and Autonomy Readiness |
| SCR-P09-17 | web | ADM, CLO | Missions |
| SCR-P09-18 | web | ADM | Schedules and triggers |
| SCR-P09-19 | web | CLO, MKR | Notebooks |
| SCR-P09-20 | web | ADM | Settings → Vidhi |
| SCR-P09-21 | web | ALL | What Vidhi remembers |
| SCR-P09-22 | console | PLT | Model registry and routes |
| SCR-P09-23 | console | PLT | Evaluation and red-team |
| SCR-P09-24 | console | PLT, SEC | Kill switches and AI incidents |
| SCR-P09-25 | web | ADM, IND | Usage and credits |

### C.15.11 P10 — Pleadings, Notices and Court Drafting Studio (12)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P10-01 | public | ANON | Pleading/notice page widget |
| SCR-P10-02 | web/mobile | IND, MKR | Pleading interview |
| SCR-P10-03 | web | IND, MKR | Draft and section review |
| SCR-P10-04 | web | IND, MKR | Validation report |
| SCR-P10-05 | web | IND, MKR | Annexure builder |
| SCR-P10-06 | web | IND, MKR | Render preview |
| SCR-P10-07 | web/mobile | IND, MKR | Filing pack |
| SCR-P10-08 | web/mobile | IND, MKR | Notice composer and dispatch |
| SCR-P10-09 | web/mobile | IND, MKR | Notice tracker |
| SCR-P10-10 | web/mobile | IND | Affidavit route |
| SCR-P10-11 | delivery | PRO | Advocate review workbench |
| SCR-P10-12 | console | CED, LRV | Render profile and limitation-row manager |

### C.15.12 P11 — Litigation and Matter Management (22)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P11-01 | web, mobile | CLO, MKR | Litigation Home |
| SCR-P11-02 | web | CLO, MKR, AUD | Matters Register |
| SCR-P11-03 | web, mobile | CLO, MKR, IND | Add Case wizard |
| SCR-P11-04 | web | CLO, MKR, EXT | Matter Workspace |
| SCR-P11-05 | web, mobile | CLO, MKR | Docket & Timeline |
| SCR-P11-06 | web, mobile | CLO, MKR, EXT | Hearings Calendar |
| SCR-P11-07 | web, mobile | CLO, MKR | Cause List Today |
| SCR-P11-08 | web | CLO, MKR | Order Review |
| SCR-P11-09 | web, mobile | CLO, MKR | Deadlines |
| SCR-P11-10 | web | CLO | Counsel Panel |
| SCR-P11-11 | web (guest); apps/delivery for marketplace professionals | EXT, PRO | Counsel Portal |
| SCR-P11-12 | web | CLO, CHK | Legal Spend |
| SCR-P11-13 | web | CLO, DIR | Exposure |
| SCR-P11-14 | web | MKR, EXT | Bundle Builder |
| SCR-P11-15 | web, mobile (Personal) | IND | My Cases |
| SCR-P11-16 | web, mobile | IND | Case Explainer |
| SCR-P11-17 | web | CLO, ADM | Bulk Import |
| SCR-P11-18 | web | CLO, DIR | Reports & Board Section |
| SCR-P11-19 | web, mobile | CLO, MKR | ADR Referral |
| SCR-P11-20 | web (admin) | ADM | Data Sources |
| SCR-P11-21 | web, mobile | ALL | Alert Preferences |
| SCR-P11-22 | web | CLO | Party Watch Review |

### C.15.13 P12 — IP and Trademark Portfolio (14)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P12-01 | web | CLO, MKR | IP Home — Portfolio control |
| SCR-P12-02 | web | CLO, MKR | Portfolio Register — All assets |
| SCR-P12-03 | web | CLO, MKR | Trademark Workspace — One mark |
| SCR-P12-04 | web, mobile | CLO, MKR, IND | Add mark / import — Add by application number or import |
| SCR-P12-05 | web, mobile | CLO, MKR, IND | Assisted refresh — Upload status evidence |
| SCR-P12-06 | web, mobile | IND, MKR | Class finder — Business description → classes |
| SCR-P12-07 | web | CLO, MKR | Knock-out screen — Screening results |
| SCR-P12-08 | web | MKR, PRO | Data sheet — TM-A preparation |
| SCR-P12-09 | web | CLO, PRO | Examination & hearing — Objections |
| SCR-P12-10 | web, mobile | CLO, MKR | Watch Queue — Journal hits |
| SCR-P12-11 | web | OPS, ADM | Journal Ingestion (ops/admin) — Upload or partner status |
| SCR-P12-12 | web | CLO, MKR | Other IP registers — Copyright, design, patent, domain |
| SCR-P12-13 | web | CLO, DIR | IP Reports — IPM-01–06, board section |
| SCR-P12-14 | web, mobile (Personal) | IND | My Brands — Individual view |

### C.15.14 P13 — Company Legal Department OS, Governance and HRMS (26)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P13-01 | web | ADM, CLO | Setup Wizard — Operating model adoption |
| SCR-P13-02 | web, mobile | CLO | Legal Department Home (CLO) — CLO dashboard |
| SCR-P13-03 | web, mobile, Teams/Chat | DEP | Request Legal Help — Intake |
| SCR-P13-04 | web | CLO, MKR | Requests Queue — Triage and work |
| SCR-P13-05 | web | MKR, CLO | Request Workspace — One request |
| SCR-P13-06 | web, mobile | DEP | My Requests — Requester view |
| SCR-P13-07 | web, mobile | CLO, MKR, DIR | Legal Calendar — All legal dates |
| SCR-P13-08 | web, board portal | DIR, CLO | Legal Risk Dashboard — KMP/board view |
| SCR-P13-09 | web | ADM, CLO | DoA Matrix — Delegations |
| SCR-P13-10 | web | CLO, ADM | Licences Register — Light register / LDC projection |
| SCR-P13-11 | web | DIR, CLO | Governance Blueprint — Requirements vs structure |
| SCR-P13-12 | web | DIR | Board & Committees — Composition |
| SCR-P13-13 | web | DIR | Meeting Planner — Annual calendar |
| SCR-P13-14 | web | DIR | Meeting Workspace — Notice, agenda, pack, attendance, console |
| SCR-P13-15 | web (PWA), mobile | DIR | Board Portal — Directors |
| SCR-P13-16 | web | DIR | Minutes Editor — Draft → seal |
| SCR-P13-17 | web | DIR, AUD | Resolutions Register — Resolutions and follow-ons |
| SCR-P13-18 | web | DIR, AUD | Statutory Registers — Register projections |
| SCR-P13-19 | web | DIR, ADM | Directors & KMP — Profiles |
| SCR-P13-20 | web | ADM, DEP | Duties — Duty catalogue and assignments |
| SCR-P13-21 | web | ADM | Org Structure — Departments, positions, org chart, lines of defence |
| SCR-P13-22 | web, mobile | ADM, DEP | People Directory & Profile — HR records |
| SCR-P13-23 | web, mobile | DEP, ADM | Leave & Attendance — Apply/approve; check-in |
| SCR-P13-24 | web | ADM | Payroll — Pay runs |
| SCR-P13-25 | web | ICM | POSH (sealed) — IC only |
| SCR-P13-26 | web, mobile | DEP | Policy Acknowledgements — Read and acknowledge |

### C.15.15 P14 — Business Services, Start a Business, Compliance and Tax (16)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P14-01 | public | ANON | Service page order widget |
| SCR-P14-02 | public/web | ANON, IND | Entity chooser |
| SCR-P14-03 | web | IND, ADM | Checkout and fee review |
| SCR-P14-04 | web | IND, ADM | Order tracker |
| SCR-P14-05 | web | IND, ADM | Document checklist |
| SCR-P14-06 | web | IND, ADM | Filing preview and approval |
| SCR-P14-07 | web | ADM | Startup Desk dashboard |
| SCR-P14-08 | web | ADM | Data room readiness |
| SCR-P14-09 | web | IND | Personal tax home |
| SCR-P14-10 | web | IND | ERI consent guide |
| SCR-P14-11 | web | ADM | Entity tax calendar |
| SCR-P14-12 | web | ADM, MKR | GST workspace |
| SCR-P14-13 | web | IND, ADM | Tax notice desk |
| SCR-P14-14 | delivery | PRO, OPS | Practitioner work queue |
| SCR-P14-15 | console | CED, LRV | Service definition studio |
| SCR-P14-16 | console | CED, LRV | Tax rule-pack studio |

### C.15.16 P15 — Consumer Help (16)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P15-01 | public (brand host) | ANON | Consumer Help home |
| SCR-P15-02 | web/mobile | CHU | Triage |
| SCR-P15-03 | web/mobile | CHU | Triage result |
| SCR-P15-04 | web/mobile | CHU, CCM | Case workspace |
| SCR-P15-05 | mobile | CHU | Evidence capture |
| SCR-P15-06 | web/mobile | CHU | Harassment log |
| SCR-P15-07 | web | CCM, CHU | Letter studio (P10 embed) |
| SCR-P15-08 | web | CHU | Authority and consent centre |
| SCR-P15-09 | web | CHU | Credit-report dispute |
| SCR-P15-10 | web | CHU | Insurance claim desk |
| SCR-P15-11 | mobile/web | CHU, IND | My vehicles |
| SCR-P15-12 | mobile/web | CHU, IND | Challan desk |
| SCR-P15-13 | web | CHU, IND, CP | Vehicle sale room |
| SCR-P15-14 | delivery (Consumer Help scope) | CCM | Case-manager queue |
| SCR-P15-15 | console | CED, LRV | Rules and calendars |
| SCR-P15-16 | console | PLT, DPO | Wall and conflict monitor |

### C.15.17 P16 — Marketplace, Professional Registry, Retainers and Academy (24)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P16-01 | public | ANON | Marketplace home |
| SCR-P16-02 | public | ANON | Category page |
| SCR-P16-03 | public | ANON | Service page |
| SCR-P16-04 | public | ANON | Compare |
| SCR-P16-05 | public | ANON | Trainings |
| SCR-P16-06 | public | ANON | Startup bundles |
| SCR-P16-07 | public | ANON | Ranking parameters & how it works |
| SCR-P16-08 | public | ANON | Advocates directory (Rule 36) |
| SCR-P16-09 | public/web | ANON, IND, ADM | Quote request |
| SCR-P16-10 | web/mobile | IND, ADM | Checkout review |
| SCR-P16-11 | web/mobile | IND, ADM | My services |
| SCR-P16-12 | web/mobile | IND, ADM | Engagement room (buyer) |
| SCR-P16-13 | web | ADM, CLO | Retainer dashboard |
| SCR-P16-14 | web/mobile | IND, ADM | Dispute & grievance |
| SCR-P16-15 | web | ADM | Company purchase settings |
| SCR-P16-20 | delivery | RM, OPS | Service product studio |
| SCR-P16-21 | delivery | RM | Offer / retainer builder |
| SCR-P16-22 | delivery | RM | Engagement pipeline |
| SCR-P16-23 | delivery | PRO, OPS | Practitioner queue & workspace |
| SCR-P16-24 | delivery | PRO, OPS | Professional onboarding |
| SCR-P16-25 | delivery | OPS | QA review & sampling |
| SCR-P16-30 | console | PLT | Marketplace administration |
| SCR-P16-31 | console | PLT | Academy feed monitor |
| SCR-P16-32 | console | PLT | Payout reconciliation |

### C.15.18 P17 — Plans, Subscriptions, Billing, Revenue Streams and Savings (30)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P17-01 | public | ANON | Pricing page |
| SCR-P17-02 | public | ANON | Comparison table |
| SCR-P17-03 | public | ANON | Configurator |
| SCR-P17-04 | public | ANON | Enterprise enquiry |
| SCR-P17-05 | web/mobile | IND, ADM | Checkout review |
| SCR-P17-06 | web | IND, ADM | Payment return |
| SCR-P17-10 | web | IND, ADM | Settings › Billing & Membership › Overview |
| SCR-P17-11 | web | IND, ADM | Settings › Billing & Membership › Plan & benefits |
| SCR-P17-12 | web | ADM | Settings › Billing & Membership › Add-ons (Company) |
| SCR-P17-13 | web | IND | Settings › Billing & Membership › Family members (Personal) |
| SCR-P17-14 | web | ADM | Settings › Billing & Membership › Seats & users (Company) |
| SCR-P17-15 | web | IND, ADM | Settings › Billing & Membership › Credits |
| SCR-P17-16 | web | IND, ADM | Settings › Billing & Membership › Usage |
| SCR-P17-17 | web | IND, ADM | Settings › Billing & Membership › Invoices & receipts |
| SCR-P17-18 | web | IND, ADM | Settings › Billing & Membership › Payment methods & AutoPay |
| SCR-P17-19 | web | IND, ADM | Settings › Billing & Membership › Billing details |
| SCR-P17-20 | web | ADM | Settings › Billing & Membership › Tax documents (Company) |
| SCR-P17-21 | web | IND, ADM | Settings › Billing & Membership › Coupons & referral credits |
| SCR-P17-22 | web | IND, ADM | Settings › Billing & Membership › Services & orders |
| SCR-P17-23 | web | ADM | Settings › Billing & Membership › Purchase approvals (Company) |
| SCR-P17-24 | web | IND, ADM | Settings › Billing & Membership › Renewal & notices |
| SCR-P17-25 | web | IND, ADM | Settings › Billing & Membership › Cancel or change plan |
| SCR-P17-26 | web | IND, ADM, AUD | Settings › Billing & Membership › Billing history |
| SCR-P17-27 | web | IND, ADM, CLO | Settings › Billing & Membership › Savings & Value |
| SCR-P17-28 | web | IND, ADM | Settings › Billing & Membership › Billing notifications |
| SCR-P17-40 | console | PLT | Pricing Studio |
| SCR-P17-41 | console | PLT | Stream registry |
| SCR-P17-42 | console | PLT | Tenant commercial view |
| SCR-P17-43 | console | PLT | Meter health |
| SCR-P17-44 | console | PLT | Savings methodology registry |

### C.15.19 P18 — Delivery Console and Operations Hub Interface (36)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P18-01 | delivery | RM | Portfolio home |
| SCR-P18-02 | delivery | RM, PRO | Work inbox (federated) |
| SCR-P18-03 | delivery | RM | Client list |
| SCR-P18-04 | delivery | RM | Client › Overview |
| SCR-P18-05 | delivery | RM | Client › Contacts |
| SCR-P18-06 | delivery | RM | Client › Plan & entitlements |
| SCR-P18-07 | delivery | RM | Client › Engagements & retainers |
| SCR-P18-08 | delivery | RM | Client › Tasks |
| SCR-P18-09 | delivery | RM | Client › Deliverables |
| SCR-P18-10 | delivery | RM | Client › Messages |
| SCR-P18-11 | delivery | RM | Client › Meetings |
| SCR-P18-12 | delivery | RM | Client › Shared drive |
| SCR-P18-13 | delivery | RM | Client › Billing & invoices |
| SCR-P18-14 | delivery | RM | Client › SLA & reports |
| SCR-P18-15 | delivery | RM | Client › Access log |
| SCR-P18-16 | delivery | RM | Client › Notes |
| SCR-P18-17 | delivery | RM | Client › Act in tenant |
| SCR-P18-18 | delivery | RM | Client › Credentials |
| SCR-P18-19 | delivery | RM | Propose grant / delegated maker |
| SCR-P18-20 | delivery | RM | Grants board |
| SCR-P18-21 | delivery | RM | Access reviews |
| SCR-P18-22 | delivery | RM | Team & assignments |
| SCR-P18-23 | delivery | RM, PRO | Me › Time |
| SCR-P18-24 | delivery | RM, PRO | Me › My metrics |
| SCR-P18-25 | delivery | RM | Portfolio reports |
| SCR-P18-26 | delivery | CCM | Consumer case queue (CHP brand) |
| SCR-P18-27 | delivery | PRO | Practitioner home |
| SCR-P18-28 | delivery | PRO | Practitioner profile (Rule 36 fields) |
| SCR-P18-29 | delivery | RM, OPS | Product switcher |
| SCR-P18-30 | web | ADM | Settings › LawDocs team |
| SCR-P18-31 | web/mobile | ADM, CHK | Approve request (grant, reveal, change, deliverable) |
| SCR-P18-32 | web | ADM | Settings › Credential vault |
| SCR-P18-33 | web | ADM | Master-data change tracker |
| SCR-P18-34 | web | ADM, AUD | Settings › Security › Access transparency |
| SCR-P18-35 | console | PLT | Master-data change queue |
| SCR-P18-36 | console | PLT, SEC | Break-glass approvals |

### C.15.20 P19 — Integration Gateway, Ecosystem Connectors and Developer Platform (22)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P19-01 | web (Company) | ADM | Integrations home |
| SCR-P19-02 | web | ADM | Connector setup wizard |
| SCR-P19-03 | web | ADM | Connector detail and health |
| SCR-P19-04 | web | ADM | Infrabyx ecosystem connections |
| SCR-P19-05 | web | ADM | Kernel system-of-record switch (LDC) |
| SCR-P19-06 | web | ADM, DEV | API clients and keys |
| SCR-P19-07 | web | ADM, DEV | Webhooks |
| SCR-P19-08 | web | ADM | Delivery log and DLQ |
| SCR-P19-09 | web | ADM, AUD | Sharing ledger (company) |
| SCR-P19-10 | web + mobile (Personal) | IND | Connected apps and sharing |
| SCR-P19-11 | partner portal (web) | PTN | Onboarding batches |
| SCR-P19-12 | web (public route) | ADM | Invitation acceptance |
| SCR-P19-13 | web | ADM | Automation (Zapier, Make, Power Automate) |
| SCR-P19-14 | web | ADM | Integration health dashboard |
| SCR-P19-15 | console | PLT | Platform connector catalogue and kill switches |
| SCR-P19-16 | console | PLT, SRE | Platform integration monitor |
| SCR-P19-17 | console | PLT | Certification workbench |
| SCR-P19-18 | console | PLT | Contract registry status |
| SCR-P19-19 | developers | DEV | Portal home and quick start |
| SCR-P19-20 | developers | DEV | API reference and try-it (sandbox) |
| SCR-P19-21 | developers | DEV | Sandbox and test data |
| SCR-P19-22 | developers | DEV | SDKs, events and changelog |

### C.15.21 P20 — Data Preservation, Portability, BYO Storage and Migration Safety (15)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P20-01 | web, mobile | IND, ADM | My data and exports `/settings/data` |
| SCR-P20-02 | web | ADM | Export wizard |
| SCR-P20-03 | web, mobile | IND, ADM | Export progress and download |
| SCR-P20-04 | web | ADM, CHK | Approval card (export) |
| SCR-P20-05 | web | ADM | Storage targets `/settings/data/storage` |
| SCR-P20-06 | web | ADM | Target detail and health |
| SCR-P20-07 | web | IND, ADM, MKR | Import wizard `/import` |
| SCR-P20-08 | web | IND, ADM, MKR | Import review grid |
| SCR-P20-09 | web, mobile | IND, ADM | Import report and undo |
| SCR-P20-10 | web | ADM | Folder policy `/settings/data/folders` |
| SCR-P20-11 | web | ADM | Exit plan and closure |
| SCR-P20-12 | web, mobile | IND | Close my account (individual) |
| SCR-P20-13 | console | PLT | Export map registry |
| SCR-P20-14 | console | PLT, SRE | Platform portability health |
| SCR-P20-15 | web | ALL | "Download as folder" action |

### C.15.22 P21 — Public Website, CMS, SEO/GEO, Help Centre and Accessibility (35)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P21-01 | public | ANON | Home |
| SCR-P21-02 | public | ANON | Section landing (Documents, Pleadings, Compliance, Start a Business, Regulated entities) |
| SCR-P21-03 | public | ANON | Category hub |
| SCR-P21-04 | public | ANON | Sub-category hub |
| SCR-P21-05 | public | ANON | Document page |
| SCR-P21-06 | public | ANON | Pleading page |
| SCR-P21-07 | public | ANON | Service page |
| SCR-P21-08 | public | ANON | Comparison page |
| SCR-P21-09 | public | ANON | Glossary index and term |
| SCR-P21-10 | public | ANON | State variant page |
| SCR-P21-11 | public | ANON | Marketplace storefront (landing, category, service, retainers, academy) |
| SCR-P21-12 | public | ANON | Pricing |
| SCR-P21-13 | public | ANON | Startups hub |
| SCR-P21-14 | public | ANON | Blog index, category, post |
| SCR-P21-15 | public | ANON | Vlog index and video page |
| SCR-P21-16 | public | ANON, ALL | Help centre home and article |
| SCR-P21-17 | public | ANON | Legal policy page |
| SCR-P21-18 | public | ANON | About, Team, Partnership, Careers, Contact, Press, Trust |
| SCR-P21-19 | public | ANON | Campaign landing page |
| SCR-P21-20 | public | ANON | Accessibility statement and feedback form |
| SCR-P21-21 | public | ANON | Search results |
| SCR-P21-22 | public | ANON | Free tools hub and tool page |
| SCR-P21-23 | console | CPUB, CED, LRV | Content Studio — content list |
| SCR-P21-24 | console | CPUB, CED | Page/post block editor |
| SCR-P21-25 | console | CPUB | DOCX import wizard |
| SCR-P21-26 | console | CPUB, LRV | Review queue |
| SCR-P21-27 | console | CPUB, PLT | Redirect manager |
| SCR-P21-28 | console | CPUB, PLT | SEO and GEO dashboard |
| SCR-P21-29 | console | CED, LRV | Glossary studio |
| SCR-P21-30 | console | CPUB, CED | Tutorial studio and clip exporter |
| SCR-P21-31 | console | CPUB, CED | Tour builder |
| SCR-P21-32 | console | CPUB | Landing-page builder |
| SCR-P21-33 | console | CPUB | Media and video library |
| SCR-P21-34 | console | PLT, CPUB | Accessibility issues board |
| SCR-P21-35 | web/delivery/console/mobile | ALL | In-app help panel and "i" popover |
| SCR-P21-36 *(v1.1)* | console | CPUB, PLT | Guest-post moderation queue |
| SCR-P21-37 *(v1.1)* | public | ANON | Investors page (toggle) |
| SCR-P21-38 *(v1.1)* | public | ANON | Resources library and resource detail |
| SCR-P21-39 *(v1.1)* | console | CPUB | Resources Studio |
| SCR-P21-40 *(v1.1)* | public/web/delivery/console/mobile | ALL | Feedback widget and My feedback |
| SCR-P21-41 *(v1.1)* | public | ANON | Team, Leadership, Governance, Changelog, Compare, Case studies, HTML sitemap |
| SCR-P21-42 *(v1.1)* | console | PLT, CPUB | Website Studio › Footer & Contact and Brand pack |

### C.15.23 P22 — Mobile Apps and Store Release (33)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P22-01 | mobile | ALL | Welcome and sign-in |
| SCR-P22-02 | mobile | ALL | Biometric set-up and app lock |
| SCR-P22-03 | mobile | ALL | Workspace switcher |
| SCR-P22-04 | mobile | IND | Home (personal) |
| SCR-P22-05 | mobile | ADM, CLO, MKR, CHK, DIR | Home (company) / Inbox |
| SCR-P22-06 | mobile | ALL | Vault folders and search |
| SCR-P22-07 | mobile | ALL | Document detail and viewer |
| SCR-P22-08 | mobile | ALL | Scanner |
| SCR-P22-09 | mobile | ALL | Aadhaar masking prompt |
| SCR-P22-10 | mobile | ALL | Share-extension destination picker |
| SCR-P22-11 | mobile | IND, MKR | WhatsApp import review |
| SCR-P22-12 | mobile | ALL | Upload queue |
| SCR-P22-13 | mobile | IND, MKR | Questionnaire (template lane) |
| SCR-P22-14 | mobile | IND, MKR | Draft preview and Vidhi adapt |
| SCR-P22-15 | mobile | MKR, CP, IND | Deal room |
| SCR-P22-16 | mobile | MKR, CHK, CP | Change review |
| SCR-P22-17 | mobile | IND, MKR | Eligibility and stamp step |
| SCR-P22-18 | mobile | IND, MKR, CP, DIR | Pre-sign summary and consent |
| SCR-P22-19 | mobile | IND, MKR | Signing status and evidence |
| SCR-P22-20 | mobile | CHK, DIR | Approval detail |
| SCR-P22-21 | mobile | CLO, MKR, IND | Matters and hearing calendar |
| SCR-P22-22 | mobile | CLO, IND | Trademark portfolio |
| SCR-P22-23 | mobile | ALL | Vidhi chat and voice |
| SCR-P22-24 | mobile | IND, ADM | Marketplace and checkout |
| SCR-P22-25 | mobile | IND, ADM | Plan and entitlements (store-policy aware) |
| SCR-P22-26 | mobile | ALL | Notifications centre and settings |
| SCR-P22-27 | mobile | ALL | Devices and security |
| SCR-P22-28 | mobile | ALL | Accessibility preferences |
| SCR-P22-29 | mobile | ALL | Help panel and tours |
| SCR-P22-30 | mobile | IND, ADM | Export and account deletion |
| SCR-P22-31 | mobile | ALL | Restricted mode banner/screen |
| SCR-P22-32 | mobile | ALL | Update required |
| SCR-P22-33 | mobile | CHU | Consumer Help home and case timeline (v2 flavour) |

### C.15.24 P23 — Engineering Governance, Change/Patch, Hardening, Audit and Go-Live (19)

| Screen | App | Persona | Purpose |
|---|---|---|---|
| SCR-P23-01 | console `/eng` | PLT, SRE, SEC, REL | Engineering home |
| SCR-P23-02 | console `/eng` | PLT, SRE, REL | Change record |
| SCR-P23-03 | console `/eng` | PLT, REL | Change calendar |
| SCR-P23-04 | console `/eng` | REL, SRE | Release console |
| SCR-P23-05 | console `/eng` | REL | Deploy gate status |
| SCR-P23-06 | console `/eng` | SEC | Vulnerability register |
| SCR-P23-07 | console `/eng` | SEC | SBOM and end-of-support |
| SCR-P23-08 | console `/eng` | SRE, SEC | Backup and restore assurance |
| SCR-P23-09 | console `/eng` | SRE | DR drills |
| SCR-P23-10 | console `/eng` | SEC | VAPT engagements |
| SCR-P23-11 | console `/eng` | SEC, DPO | Incident console |
| SCR-P23-12 | console `/eng` | SEC, PAUD | Control evidence |
| SCR-P23-13 | console `/eng` | SEC, PLT | Evidence packs |
| SCR-P23-14 | console `/eng` | SEC | Access reviews |
| SCR-P23-15 | console `/eng` | PLT, CED | Claims register |
| SCR-P23-16 | console `/eng` | PLT | Go-live checklist |
| SCR-P23-17 | console `/eng` | PLT, SRE | Hypercare dashboard |
| SCR-P23-18 | console `/eng` | PLT | AI change and model registry |
| SCR-P23-19 | web | ADM, ALL | Tenant "What's new" and maintenance notices (`apps/web`) |
| SCR-P23-20 *(v1.1)* | web | ADM, AUD, CLO | Settings › Security & trust › Vendor documents (list, download, subscribe, request, evidence packs, auditor grants, questionnaire responder) |
| SCR-P23-21 *(v1.1)* | web | ADM | Settings › Engineering › Beta (opt-in, flags received, feedback per flag) |
| SCR-P23-22 *(v1.1)* | console `/eng` | PLT | Release-notes editor and notice-period gate |

---

## C.16 Reconciliations and gaps found at compilation (apply at integration)

| # | Finding | Resolution (binding unless the owner decides otherwise) | Owner |
|---|---|---|---|
| R-1 | P02 FR-P02-55 puts "Help" in the Personal rail and "Drafts" as a rail label; P22 calls the same area "Create"; P03 FR-P03-34 makes Help LOCKED. | Help lives in the top bar for every shell (consistent location, WCAG 3.2.6); the Personal rail label is **Create** on web and mobile; tenants may rename. | P02, P22 |
| R-2 | P03 FR-P03-34 lets users "pin up to 8 items to the top of the rail"; this appendix caps the primary group at 7. | Pins form a separate, collapsible "Pinned" group (≤ 8, `cfg.nav.max_pinned_items`); the primary group stays ≤ 7. | P03 |
| R-3 | Appendix R `mob.bottom_bar.items` (4 items: Home, Documents, Sign, Inbox) conflicts with P22 FR-P22-03 (5-tab sets per workspace, `mob.nav.tab_order`) and P02 FR-P02-58 ("first four items"). | P22 governs native apps (owning phase wins, X-11 pattern). `mob.bottom_bar.items` is re-scoped as the tenant default for the middle slots of the Company tab set; FR-P02-58 applies to mobile web only. **Done:** Appendix R §R.9.38 row corrected (exactly 2 middle slots; P22 FR-P22-03 governs). | Appendix R, P22 |
| R-4 | P02 role rails omit an Inbox; P03 lists Inbox as LOCKED. | Inbox is a LOCKED top-bar control on every shell; makers and checkers also get "Queue"/"Approvals" in their rail. | P02, P03 |
| R-5 | "Start a new document": P02 ≤ 2 taps, P06 ≤ 3 taps to the first question, P22 ≤ 3 taps. | J-09: ≤ 2 from the home widget; ≤ 3 when browsing the catalogue or from the mobile Create tab. | P02, P06, P22 |
| R-6 | P16 states three different purchase budgets (≤ 7 taps from the service page for a non-subscriber; ≤ 6 mobile / ≤ 8 web with no account; ≤ 4 further steps signed in). | J-28 harmonises: signed in ≤ 4 + hosted checkout; no account ≤ 7 mobile / ≤ 8 web including OTP sign-up. | P16 |
| R-7 | Budgets of "≤ 2 from notification" for approvals versus Appendix U §U.5.8 (confirmation before approval, SC 3.3.4). | Approvals with legal effect, money or access require step-up (Appendix D §D.11), which is the confirmation; other approvals are reviewed on a visible diff (SC 3.3.4 "checked") and the approve control names the object. | P02, Appendix U |
| R-8 | No screen IDs exist for the unified Inbox, the command palette and the universal search results page (the Inbox is composed of SCR-P02-12, SCR-P03-18 and SCR-P08-07; SCR-P04-08 is vault search). | Register in P03: **SCR-P03-33 Inbox (unified)**, **SCR-P03-34 Command palette**, **SCR-P03-35 Search results (all objects)**; tours and tutorials bind to these IDs. | P03 |
| R-9 | Widget keys were not namespaced in any phase. | `w.<module>.<name>` (§C.7.1) registered in `cfg.widget_catalogue`; owning phases seed their widgets. | P03 + owners |
| R-10 | Duplicate or overlapping settings keys found in Appendix R at compilation: several AI-crawler keys under `web.crawl.ai_*` and two caption-default keys under `hlp.video.*`. | Keep one key per concept at integration (P21 decides), alias the others for one release (NN-12 expand → contract). **Done:** Appendix R now carries `web.crawl.ai_search_bots_allowed`, `web.crawl.ai_training_bots_allowed` and `hlp.video.captions_default_on` only; the registry-review G4 duplicate-key check found no duplicate key. | Appendix R, P21 |
| R-11 | P13 screens for HR, payroll and POSH name roles (HR admin, payroll maker/checker, IC members) that are not role codes in conventions §6. | Model as custom roles over `ORG_ADMIN`/`ORG_MEMBER` capability families (Appendix D §D.4) with the POSH IC as a sealed-scope custom role; Appendix D to confirm. | Appendix D, P13 |
| R-12 | P02 §4L names "Legal desk" while P13 names the module "Legal Department". | Rail label "Legal desk" (short); page title "Legal Department"; one help key `hlp.lgo.legal_desk`. | P02, P13 |

---

*End of Appendix C.*
