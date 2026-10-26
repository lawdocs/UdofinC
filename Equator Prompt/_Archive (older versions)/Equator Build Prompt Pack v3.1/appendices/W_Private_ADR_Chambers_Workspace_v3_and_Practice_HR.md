# Appendix W — Private ADR Chambers Workspace v3 and Practice HR (v3.0, 23 October 2026)

> Paste-ready specification. Owner: Product (Chambers). Implemented in **Phase P20** (`phases/P20_Chambers_Workspace_v3_and_Practice_HR.md`) with addenda to P03, P05, P10, P12 and P13 (§W.18). This appendix is the **detailed chambers settings catalogue** that Appendix V (configuration framework) cross-references.

## W.0 Purpose, sources, precedence

### W.0.1 Purpose

Management's brief of 23 October 2026 (item 2) asks for "extra customisation for Private ADR Chambers / independent neutrals (their pages on the Equator website), plus staff/case-manager management and a small HR module with salary records and disbursal". This appendix specifies:

1. **Public practice pages** on the Equator website and on tenant domains, built with a page builder inside accessibility, naming, professional-conduct and truth-in-marketing guardrails (§W.3).
2. **Practice configuration**: rules, fees, templates, intake forms, notifications, numbering, letterheads, e-sign, the chambers' own GST invoicing, payment collection, status labels and client-portal branding (§W.4).
3. **Staff management**: role templates, case-level access, delegation, queues, tasks, calendars, SLAs and workload, with a hard confidentiality wall between HR/accounts roles and case content (§W.5).
4. **Practice HR (HR-lite)** for chambers staff, including salary records, monthly payroll on the Appendix Z rule packs, payslips and disbursal under maker-checker, with compensating controls for sole practitioners (§W.6).
5. **Practice dashboards and reports** (§W.7), the **practice settings catalogue** (§W.8), **plans and pricing hooks** to the Appendix AB revenue-stream registry (§W.9), the `chm` data model, APIs, events, errors, RBAC, audit, exports and tenant offboarding (§W.10–§W.15), acceptance tests (§W.16), open items (§W.17) and phase addenda (§W.18).

### W.0.2 Sources

Pack: Appendix N §1.8, §8, §11.6 [N]; Appendix O §1.5, §2.8, §4.2, §8.6 [O]; Phase P10 FR-P10-01–12 and v2 addenda [P10]; Appendix S §2.8, §6.2–§6.3 [S]; Appendix U §U.4, §U.8, §U.11 [U]; Appendix P §1.4, P-34, §8.1 [P]. Research: [RA] Jupitice ADR Marketplace (F3, F8, EQM-01–23); [RB] business models (§A–§C, RS-09/10/18/19); [RC] labour and payroll (F1–F14, implications A–G); [RD] export package `EQ-EXPORT-1.0` (DI-C); [RE] directory and marketplace law (F1–F3, implications A–F). Primary legal sources are cited as the research files cite them. Where research marks a fact "not confirmed", it is a parameter with an open marker **[VERIFY — open: …]**.

### W.0.3 Precedence

Master §15 and the 02 decision log prevail; within this appendix's scope, this appendix prevails over P10 §4A and the Appendix N §8 / Appendix O §2.8 text where they differ (each difference is listed in §W.0.5). Where this appendix and Appendix Z (HRMS and payroll) define the same statutory parameter, **Appendix Z's rule pack is the single source** and this appendix only consumes it (X-49). Where this appendix and Phase P19 / the marketplace appendix define the same marketplace rule, **P19 is the single source** for ranking and sponsorship; this appendix only supplies eligibility attributes (X-48).

### W.0.4 Decisions, requirements and cross-file resolutions recorded here

| ID | Kind | Statement |
|---|---|---|
| R-48 | Requirement | Extensive customisation for Private ADR Chambers and independent neutrals, including public practice pages on the Equator website and tenant domains (brief item 2) → §W.3, §W.4, §W.8 |
| R-49 | Requirement | Staff and case-manager management for chambers with queues, SLAs and confidentiality separation → §W.5 |
| R-50 | Requirement | Small HR module with salary records, payroll and disbursal for chambers staff (RC F14) → §W.6 |
| D3-15 | Decision | **Practice pages are a separate surface** at `/chambers/{slug}` (and its person pages `/chambers/{slug}/people/{person}`, §W.3.1), the tenant sub-domain and a verified custom domain. They are never linked from, ranked with or rendered inside `/neutrals` or any allocation, eligibility or live-case screen; an empanelled neutral's institutional profile does not link to their practice page. Equator hosts them as an intermediary (IT Rules 2021 r.3) [RE F3.3] |
| D3-16 | Decision | **Tenant-governed approvals.** G settings affecting third parties' rights inside a chambers (rules, award/order/settlement templates, fee schedules, status labels, procedural notices) are approved by a tenant-designated holder of `chm.config.approve.legal` after platform validators pass. Equator validates against L guardrails but **does not review, approve or endorse** tenant legal content (Appendix N §8.5 cl.1); platform rule packs (payroll, GST, label deny-list, lint) stay Equator-governed |
| D3-17 | Decision | **Practice HR is the chambers' own employer tool.** The chambers is employer and fiduciary; Equator is processor; calculations are tools, not advice; Equator **never holds or routes salary money** (bank file uploaded by the chambers, or a payout API on a chambers-owned account) |
| D3-18 | Decision | **Single-person separation of duties.** Where only one natural person can act, NN-36 maker-checker is met by compensating controls (§W.6.10): passkey step-up per approval after a minimum gap, cooling and out-of-band confirmation for bank changes, anomaly holds, an optional free external checker, and `SINGLE_PERSON_SOD` exception reporting |
| D3-19 | Decision | **Confidentiality wall.** `chambers_hr` and `chambers_accounts` never read case content; case roles never read HR or salary records. Cerbos `DENY`, separate RLS on `chm` HR tables, field-level encryption of salary data |
| X-47 | Resolution | **Schemas, events, roles.** v2 `chambers.*` tables stay canonical for workspace and subscription state; v3 tables are in **`chm`** and reference `chambers.workspaces.id`; v2 events `equator.chambers.*.v1` unchanged, v3 events use context **`chm`**; seat `case_manager` → role `chambers_case_manager`; `chambers_admin` unchanged plus new `chambers_owner` (§W.2) |
| X-48 | Resolution | **Routes and surfaces.** `/chambers` still 301s to `/private-adr-chambers` (FR-P10-V2-01); `/chambers/login`, `/start`, `/admin/*` keep their meaning as **reserved slugs** (§W.3.2). Canonical host = verified custom domain, else `equatorresolution.in/chambers/{slug}`; the sub-domain serves portal routes and 301s page routes. Marketplace listing is a **consented projection** into P19 `mkp`; sponsorship lives only in `mkp` and is never readable by `chm`, the institutional directory or allocation |
| X-49 | Resolution | **Practice HR persistence and engine.** Chambers HR and payroll data persist in `chm` under tenant RLS; calculation uses the **P18 payroll engine** — the pure library `packages/rules/payroll` and leave validator `packages/rules/leave` (Appendix Z X-58) — with **Appendix Z rule packs** under the exact names of the Appendix Z §Z.2.4 rule-pack map (`rulepack.<jurisdiction>.<domain>.<name>@<version>`, from `cfg`). No chambers employee row is written to the group `hr` or `pay` schemas (NN-38). Disbursal uses Appendix Z's naming: `PAYOUT_PORT` with the shared `bank_file` adapter (§W.6.10); engine-raised errors keep their Appendix Z canonical codes, to which the `CHM_` codes of §W.13 map |

### W.0.5 Changes to earlier text

| Earlier text | Change |
|---|---|
| P10 §3 `case_manager (chambers seat)` | Replaced by `chambers_case_manager`; new roles `chambers_owner`, `chambers_staff`, `chambers_hr`, `chambers_accounts` (§W.2) |
| P10 FR-P10-05 public pages "about, rules, fee schedule, panel directory, contact, grievance officer" | Superseded by the page builder (§W.3); the listed pages become default blocks and page kinds |
| P10 FR-P10-12 health dashboard | Superseded by practice dashboards (§W.7) |
| Appendix O §4.2 `seats` | New seat types `staff`, `hr`, `accounts` and a checker-only seat (§W.9) |
| Appendix S §6.2 `chambers_admin` row | Extended by the chambers RBAC matrix (§W.14); hard denials of D3-19 added |
| Appendix N §8.3 "Branding" row | Extended by themes, fonts and accessibility rules (§W.3.4) |

---

## W.1 Principles and Locked guardrails

The chambers is the administering institution (or the neutral acts ad hoc); Equator is the technology provider [N §8.1]. Customisation is wide, but the following are **Locked (L)** in every chambers tenant and cannot be changed by any tenant role, plan or flag:

| ID | Locked guardrail | Source | Enforcement |
|---|---|---|---|
| CHL-L01 | No "court", "judge", "decree", "tribunal" (except "arbitral tribunal" in procedural documents), "bench", "Lok Adalat", government/statutory/regulator names, State Emblem or Schedule names in any tenant name, slug, page, template, sender name, status label or domain; counsel override per tenant only through `chambers.court_label_override` | N §1.8; P10 FR-P10-01; U §U.8; NN-17 | Label validator; LINT-001, LINT-002; CHM-LINT-01 |
| CHL-L02 | Non-removable legal footer on every page and portal view: tenant legal entity, CIN/registration, "This centre is not a court and does not exercise judicial power", "Private practice page hosted on Equator Resolution. Matters here are not administered by Equator unless referred to Equator with every party's consent.", grievance contact, "Report this page" | P10 FR-P10-01; RE F3.3 | Renderer; snapshot test |
| CHL-L03 | No outcome claims (settlement rates, win rates, recovery rates, "awards never set aside", guaranteed timelines) and no unevidenced numbers | NN-17; NN-28; U §U.8; LINT-005, LINT-010, LINT-011, LINT-012 | Copy lint (blocking) |
| CHL-L04 | No claim or implication that matters are Equator-administered, Equator-approved or Equator-certified; no use of Equator's panel grade as a marketing label unless `chambers.pages.show_equator_panel_status` is ON (§W.3.8) | N §8.5 cl.2; RE F3.1 (E-Commerce r.5(6) 2026) | CHM-LINT-02 |
| CHL-L05 | Professional-conduct regimes for page subjects (BCI r.36 Schedule for advocates; ICAI/ICSI/ICMAI limits) restrict blocks and fields (§W.3.7) | RE F1.2, F1.5 | Block allow-lists per regime |
| CHL-L06 | Paid placement never appears on a practice page and never affects the institutional directory, allocation, eligibility, Quality Index, grading or conflict checks | NN-34; NN-28 | CI `NO_PAID_PLACEMENT` (extended) |
| CHL-L07 | Rules validator: no reduced statutory clock, no prohibited mechanism × vertical, no removal of Sixth Schedule disclosure, arbitration objection window ≥ 15 days, no unilateral appointment, mediation recording OFF by default, no success fees where prohibited, no statutory-enforceability claims while NN-05 is OFF | P10 FR-P10-07; NN-03, NN-04, NN-11, NN-18 | `RULESET_GUARDRAIL_VIOLATION` |
| CHL-L08 | Template locked blocks (footer, BSA s.63(4) certificate hook, e-stamp block, NN-08 excluded-instrument routing, signature blocks) cannot be removed | NN-08, NN-09, NN-10 | `CHM_TEMPLATE_LOCKED_BLOCK_REMOVED` |
| CHL-L09 | Settlement money never through any merchant account; chambers is merchant of record for its own fees only | NN-13; P10 FR-P10-08 | P05 split engine |
| CHL-L10 | Equator never holds or routes salary or consultant-fee money | D3-17; NN-13 | `CHM_PAYOUT_ACCOUNT_NOT_TENANT_OWNED` |
| CHL-L11 | Prohibited monitoring — the platform set `platform.hr.monitoring.prohibited_set` (Appendix Z §Z.6.2, §Z.15): keystroke logging; webcam capture or face-presence detection; covert or continuous screen recording; screenshots of personal devices; off-hours location tracking; reading personal email or private messages; BYOD personal-area access; use of meeting presence in performance scoring. The Appendix Z governed investigation-capture exception is not offered to chambers tenants | NN-35; RC F12.2, D22 | Settings absent; `CHM_MONITORING_PROHIBITED` (maps to `HR_MONITORING_PROHIBITED`) |
| CHL-L12 | Payroll statutory logic: s.2(y) wage classification, 50% deduction cap per wage period, overtime ≥ 2×, pay deadline before the 7th of the following month, F&F within 2 working days, national holidays, statutory-dues non-waiver | RC F2, design §G item 36 | Engine (Appendix Z) |
| CHL-L13 | Maker-checker (or D3-18 compensating controls) on every money movement, pay run, payee or bank-detail change, salary revision, privileged-role grant, sensitive export and legal-content publication | NN-36 | `CHM_MAKER_CHECKER_SAME_USER` |
| CHL-L14 | Confidentiality wall between HR/accounts and case content | D3-19; NN-11 | Cerbos `DENY` |
| CHL-L15 | Party access, statutory clocks and records never withheld for the tenant's non-payment (run-off 90 days) | P10 FR-P10-04; N §8.5 cl.6 | Run-off workflow |
| CHL-L16 | Free full export at any time and at exit (`EQ-EXPORT-1.0`) | NN-37; RD DI-C | Export service |
| CHL-L17 | WCAG 2.2 AA on every published page and theme | NN-23 | Theme validator; axe CI |
| CHL-L18 | Students and learners cannot hold any chambers role | P10 FR-P10-11 | `STUDENT_ROLE_FORBIDDEN_IN_TENANT` |

---

## W.2 Personas, role templates and access model

### W.2.1 Role templates

All roles are tenant-scoped grants in `core.role_grants` (P01) for principals signed in through `eq-portal-chambers` / `eq-portal-chambers-{slug}` (Appendix S §2.8). MFA (passkey or TOTP) is mandatory for every chambers role; step-up to phishing-resistant authentication (passkey) is required for the actions marked "step-up" in §W.14.

| Role code | Who | Default capabilities | Cannot |
|---|---|---|---|
| `chambers_owner` | Proprietor, managing partner or the body's authorised signatory; exactly one primary owner, up to 2 deputy owners | Everything `chambers_admin` can do; subscription and plan; ownership transfer; approve G settings if holding `chm.config.approve.legal`; approve pay runs and disbursal; view salary records; tenant offboarding | Disable L guardrails; read caucus notes of another neutral; act as checker on own maker action (D3-18 applies only when no second person exists) |
| `chambers_admin` | Practice manager or administrator | Practice pages, branding, domain, T settings, staff invitations (non-privileged roles), work queues, SLAs, templates (maker), rules and fees (maker) | Grant `chambers_owner`, `chambers_hr` or `chambers_accounts` without owner approval; read salary; read case content unless also granted a case role on that case |
| `chambers_case_manager` | Registry or case manager | Administer assigned matters on shared engines: intake, scrutiny, notices, scheduling, bundles, service, clocks; tasks and queues | Read caucus notes; sign orders or awards; read HR or salary |
| `chambers_staff` | Assistant, tribunal secretary, clerk, receptionist | Scoped by sub-template: `assistant` (calendar, enquiries, scheduling, document intake), `tribunal_secretary` (organisational support to a named tribunal on named cases: hearing logistics, transcripts, bundles, chronology drafts — never deliberation or reasons), `front_desk` (enquiries, contact) | Read caucus notes; draft reasons of an award; access HR or salary; publish pages unless granted `chm.pages.publish` |
| `chambers_hr` | HR or office manager | Staff records, onboarding/offboarding checklists, leave, attendance, policy acknowledgements, salary structures and pay-run preparation (maker) | Read any case content (D3-19); approve a pay run they prepared; disburse |
| `chambers_accounts` | Accounts executive or the chambers' CA | Invoices, receipts, receivables, GST data, consultant fee notes and TDS, pay-run checking (checker), disbursal file generation after approval, accounting exports. Sub-template `external_checker` (checker-only, no create rights) for an outside CA | Read case content beyond the billing view (matter number, payer, amounts); create a payee and approve its payment; change bank details |
| `neutral_mediator` / `neutral_conciliator` / `neutral_arbitrator` / `neutral_expert` / `neutral_facilitator` (tenant scope) | The chambers' neutrals | Per Appendix S §6.2 within the tenant | As Appendix S; never read HR records of staff other than their own ESS |
| `employee` (self-service, tenant scope) | Every staff record with a login | Own profile, own attendance and leave, own payslips and tax declarations, own goals and reviews, policy acknowledgements, own data export | Anything else |

Rules: (1) a person may hold several roles, subject to the SoD engine (§W.5.6); (2) **case-level access** is a separate grant `chm.case_access` (`assigned` default, `all_tenant_matters` opt-in and logged, `none`); a tribunal secretary needs a per-case instruction artefact from the presiding arbitrator and a party disclosure notice before access starts **[VERIFY — open: no Indian statutory rule on tribunal secretaries was found; counsel to confirm the default]**; (3) seats per §W.9 — ESS-only logins do not consume a paid seat (`tenant.chm.seats.ess_free`, G-bounded by Appendix AB); (4) staff without logins exist only as HR records (§W.6.3).

### W.2.2 Access dimensions (ABAC)

| Attribute | Values | Used by |
|---|---|---|
| `chm.role` | role codes above | Cerbos role policies |
| `chm.case_access` | `assigned`, `all_tenant_matters`, `none` | Case resources |
| `chm.hr_scope` | `none`, `self`, `records`, `records_and_salary` | HR resources |
| `chm.money_scope` | `none`, `view`, `maker`, `checker`, `releaser` | Billing, pay runs, disbursal |
| `chm.page_scope` | `none`, `edit`, `publish` | Practice pages |
| `chm.config_scope` | `none`, `t_edit`, `g_maker`, `g_approve_legal` | Settings |
| `chm.delegation_id` | uuid or null | Time-bound delegated authority (§W.5.3) |
| `chm.conflicts[]` | case ids | Hard deny on conflicted cases (Appendix S hard denial) |

---

## W.3 Public practice pages and page builder

### W.3.1 What a practice page is

A practice page is the public face of a chambers tenant or an individual neutral's private practice. It explains who the practice is, how it runs ADR processes, its rules and fees, and how to contact it. It is **not** part of Equator's institutional directory (D3-15) and it never shows Equator appointment data. Equator's role is limited to hosting (intermediary) and to the technology the practice uses.

Page kinds (`chm.page_kind`):

| Kind | Route (Equator host) | Purpose | Max per tenant |
|---|---|---|---|
| `practice_home` | `/chambers/{slug}` | Home page of the chambers (or the individual practice for a sole practitioner) | 1 |
| `person` | `/chambers/{slug}/people/{person}` | One neutral or staff member who has consented | Plan seats × 1 (neutrals only by default; staff pages optional) |
| `rules` | `/chambers/{slug}/rules` and `/rules/{version}` | Published rules of procedure, code of conduct, versions and change log | 1 (+ versions) |
| `fees` | `/chambers/{slug}/fees` | Fee schedule rendered from the fee engine | 1 |
| `faq` | `/chambers/{slug}/faq` | Answer-first FAQs | 1 |
| `contact` | `/chambers/{slug}/contact` | Contact and enquiry form | 1 |
| `publications` | `/chambers/{slug}/publications` | Articles and papers | 1 |
| `legal` | `/chambers/{slug}/privacy`, `/terms`, `/grievance` | The chambers' own privacy notice (it is the data fiduciary), terms and grievance policy | 3 |
| `custom` | `/chambers/{slug}/{page}` | Other pages built from allowed blocks | Plan-dependent (§W.9) |

### W.3.2 Hosts, canonical URLs, slugs

| Host | Serves | Canonical? |
|---|---|---|
| `equatorresolution.in/chambers/{slug}/…` | All page kinds | Yes, unless a custom domain is verified |
| `{slug}.chambers.equatorresolution.in` | Portal routes (`/login`, `/track`, `/verify/{number}`, `/app/*`); page routes 301 to canonical | No |
| Custom domain (for example `www.example-adr.in`) | All page kinds and portal routes | Yes, once verified (§W.3.5) |

Slug rules: 3–40 characters, `^[a-z0-9]+(-[a-z0-9]+)*$`, passes the label validator (CHL-L01), unique across tenants, changeable at most twice a year with 301s kept for 12 months. **Reserved slugs** (cannot be registered; `CHM_SLUG_RESERVED`): `login`, `start`, `admin`, `app`, `api`, `help`, `pricing`, `directory`, `search`, `people`, `rules`, `fees`, `track`, `verify`, `terms`, `privacy`, `grievance`, `marketplace`, `neutrals`, `equator`, `equator-resolution`, `institute`, `academy`, `campus`, `official`, `government`, `support`, `status`, `docs`, plus every word on the label deny-list. **Workspace segments** *(v3.1; Appendix AG §AG.0.5 #6, D3-47(d))* are also reserved because the chambers workspace shell uses them under `/chambers/`: `work`, `workload`, `hr`, `me`, `controls`, `dashboards`, `inbox`, `settings`, `exports`, `offboarding`, `approvals`, `reports`. A practice slug equal to one of these (none expected before launch) is migrated to a new slug with a 301 kept for 12 months. The workspace shell root is `/chambers/work` (home SCR-P20-29, dashboard `practice_home`); `/app/chambers/*` 301s there and `core.login_portals.dashboard_route` for `chambers` points to it (AG §AG.0.5 #7). Released slugs are quarantined for 12 months (§W.15.5) to prevent impersonation.

Person slugs: `{given}-{family}` transliterated to ASCII, de-duplicated with a numeric suffix; never a Bar enrolment number or other identifier.

### W.3.3 Block catalogue

Every page is an ordered list of blocks. Each block has a schema (`packages/forms`-style Zod schema), a renderer (web SSR and an AMP-free static variant for crawlers), a lint profile and a per-regime availability (§W.3.7). Free text in any block passes the copy lint (§W.3.9) on save and on publish.

| Block | Fields (key ones) | Data source | Constraints |
|---|---|---|---|
| `hero` | Display name (validated label), one-liner (≤ 25 words), image (consented), primary action (one of `enquire`, `request_session`, `view_rules`) | Tenant | One `h1` (LINT-043); one primary action; no countdowns or carousels (Appendix P UX-01) |
| `bio` | Rich text (≤ 600 words), qualifications list, former offices (credential phrase allow-list: "retired judge of", "former judicial office") | Tenant + verification records | "Verified on {date}" only with a verification record, else "Self-declared" |
| `practice_areas` | Dispute types (Appendix K taxonomy), mechanisms offered, sectors | Taxonomy | Taxonomy only; master §5.2 matrix enforced |
| `process_explainer` | Mechanism (negotiation, mediation, conciliation, arbitration, med-arb, expert determination), steps, typical documents | Equator explainer library (editable copy) | LINT-006, LINT-008, LINT-009; edited text keeps its library source ID |
| `fee_schedule` | Rendered from the tenant's published fee schedule (`FeeToken`s), GST-inclusive toggle for individuals | Fee engine (P05) | LINT-020; NN-29 GST-inclusive totals; not in restricted regimes (§W.3.7) |
| `rules_adopted` | Rules title, version, effective date, base ("Based on the Equator Resolution Rules template" when forked), code of conduct adopted, download (DOCX/PDF) | Rulebook (§W.4.1) | Fixed sentence when forked: "These rules are based on a template provided by Equator Resolution. Matters under them are administered by {Chambers}, not by Equator." |
| `availability` | Coarse availability (week view: available / limited / unavailable; earliest slot), session modes (online / in person / hybrid), cities | Calendar (§W.5.5) | No case details or counts; hidden if sync is stale > 24 hours |
| `enquiry_form` | Name, email/phone, dispute type, other party's name (for conflict check), short description (≤ 1,000 characters), preferred mechanism, language, consent checkboxes (unticked) | Tenant inbox (§W.5.4) | Chambers' DPDP notice inline; CAPTCHA; rate limit; not in restricted regimes |
| `faq` | Question, answer-first answer (first sentence ≤ 25 words), sources | Tenant | LINT-021-style answer-first rule; `FAQPage` markup only when visible text matches (LINT-046) |
| `publications` | Title, venue, date, link or uploaded PDF, co-authors | Tenant | Copyright attestation; malware scan; lint |
| `languages` | Languages of service, interpreter availability, ISL | Tenant | ISO 639 codes; at least one |
| `jurisdictions` | Seats and venues offered, States served, international work (yes/no), governing-law familiarity (free text, linted) | Tenant | No enforceability claims beyond NN-19 facts (LINT-008) |
| `team` | Cards for consented people: name, role, languages, link to person page | Person records with `display_consent` | Per-field consent (NN-39 pattern); alphabetical or seeded-random order |
| `contact` | Address, phone, email, office hours, map (static image, no third-party map script by default), grievance officer name and contact | Tenant | Grievance officer mandatory |
| `model_clause` | Clause type (arbitration, mediation, med-arb, negotiation first, multi-tier, expert determination, submission agreement), blanks, plain-language note, "when not to use", download DOCX/PDF | Generated from the tenant's rules and Appendix U §U.11 patterns | No unilateral appointment; MC-1F lender limits; consumer caution locked; names the chambers, never Equator, as administering body |
| `rich_text` | Headings (h2–h4), paragraphs, lists, links | Tenant | No scripts, iframes or pixels; links `nofollow ugc` |
| `image` | Image, alt text (mandatory), caption | Tenant | ≤ 2 MB; EXIF stripped; consent for identifiable people |
| `video` | Upload or YouTube/Vimeo link, captions file mandatory | Tenant | Captions required (WCAG 1.2.2); click-to-load embeds |
| `notice` | Short banner text (for example closure days) | Tenant | ≤ 40 words; no urgency language (LINT-033) |
| `case_status_lookup` | Case number + verification code | P02 tracker | Rate-limited; canonical public status only |
| `marketplace_link` | "Book through the Equator Marketplace" | P19 | Shown only when the practice has opted into the marketplace projection (§W.3.10) |

Blocks **not** offered (deny-listed): testimonials, ratings, reviews, "clients we have served" logos, win/settlement statistics, comparison with courts, "featured"/"top"/"best"/"premium"/"recommended" labels, chat widgets that open by themselves, pop-ups on entry, third-party analytics or ad pixels (Appendix O X-03, X-18 [RB §A item 5]; RE F1.4(e), F1.5; Appendix P UX-10).

Process-feedback block (`process_feedback`, aggregate of the chambers' own post-matter process feedback: punctuality, clarity, courtesy, accessibility, timeliness — never outcome) is **flag-gated** `tenant.chm.pages.process_feedback_block` (G; default OFF; requires n ≥ 10 responses per item and a tenant claims record with definition and as-of date) and is never available in restricted regimes [RA EQM-10].

### W.3.4 Themes, brand, fonts and accessibility

| Item | Rule |
|---|---|
| Themes | Platform themes (`classic`, `modern`, `minimal`, `institutional`) on every plan; additional themes via Appendix AB RS-37 "Page themes" (§W.9; never labelled "premium" on public pages); themes change layout, never blocks |
| Brand tokens | `brand.primary`, `brand.secondary`, `surface`, `surface.alt`, `text`, `text.muted`, `accent`, `focus`, light and optional dark sets |
| Contrast | Text ≥ 4.5:1, large text ≥ 3:1 (WCAG 2.2 SC 1.4.3); UI components and focus ≥ 3:1 (SC 1.4.11); failures → `CHM_THEME_CONTRAST_FAIL` listing the pairs |
| Built-in (not editable) | Visible focus (SC 2.4.7), focus not obscured (SC 2.4.11), targets ≥ 24 × 24 CSS px (SC 2.5.8), `prefers-reduced-motion`, no autoplay, RTL for Urdu |
| Fonts and logo | Platform-hosted allow-list with Indic coverage for enabled locales, ≤ 2 families, body ≥ 16 px (`CHM_FONT_NOT_ALLOWED`); logo SVG/PNG ≤ 500 KB, SVG sanitised, alt text required |
| Preview | Light/dark, mobile/desktop, each locale; axe report stored with every version |

### W.3.5 Sub-domain, custom domain and TLS

Extends P10 FR-P10-05.

1. **Sub-domain** `{slug}.chambers.equatorresolution.in`: provisioned at sign-up (wildcard certificate), every plan.
2. **Custom domain** (entitlement `chambers.custom_domain`: CH-PRO, CH-INST, or the add-on on CH-SOLO; never CH-LITE [O §2.8; FR-P10-V2-O1]): the system issues a TXT ownership token `_equator-verify.{host}` and a CNAME target; apex domains use ALIAS/ANAME or an apex-to-`www` redirect.
3. **Checks before issuance:** TXT present; CNAME resolves; CAA (if any) permits Amazon's CA (`amazon.com`, `amazontrust.com`, `awstrust.com`, `amazonaws.com`), else `CHM_DOMAIN_CAA_BLOCKS_ISSUANCE` with the line to add; label validator passes; host not attached elsewhere (`CHM_DOMAIN_IN_USE`).
4. **Certificate:** ACM DNS-validated, on the CloudFront multi-tenant distribution (P10); TLS 1.2+; HSTS `max-age=31536000` on the verified host as soon as the certificate is active (L, Appendix V §V.4.1 `domains.custom`). `includeSubDomains` is added only after tenant confirmation (T), because it affects the tenant's other hosts. Preload is never automatic. Renewal alerts at T-30/T-14/T-7. *(v3.1: reconciles the earlier "HSTS after confirmation" wording with V's locked HSTS)*
5. **Health:** daily re-check; DNS lost > 72 hours → `degraded`, canonical reverts to `/chambers/{slug}`, admin notified. Sender domains are verified separately (SES, P10). Release: §W.15.5.

### W.3.6 SEO, structured data and multilingual pages

| Item | Rule |
|---|---|
| Titles, meta, canonical | SEO title ≤ 60 characters, meta 70–155, unique (LINT-040–042); self-canonical on the canonical host (LINT-044); `noindex` default in `bci_r36` (§W.3.7) and on previews |
| Sitemaps | One per indexable practice, referenced from the Equator sitemap index |
| Structured data | `Organization` (practice), `Person` (person pages: `jobTitle`, `worksFor`, `knowsLanguage`, `knowsAbout`, `hasCredential` for verified credentials only), `Service` per mechanism, `BreadcrumbList`, `FAQPage` for visible FAQs, `WebPage` with `inLanguage`; JSON-LD parity with visible text (LINT-046) |
| Prohibited schema | `Review`, `AggregateRating`, `LegalService` (flag OFF), prices in restricted regimes (CHM-LINT-07) |
| Locales and hreflang | English and Hindi on every plan; other NN-23 languages by configuration; reciprocal hreflang with `x-default` (LINT-048); locale parity of fee tokens, rule IDs and claims (LINT-025) |
| Translation | Machine drafts (`TRANSLATION_PORT`) labelled "Draft translation — review required"; no locale publishes until reviewed; `legal` and `rules` translations need the D3-16 legal approver |
| Crawlers and speed | AI-training crawlers blocked on person pages by default (master X-42; T); SSR/SSG (master §4.1); LCP ≤ 2.5 s at p75 on 4G |

### W.3.7 Professional-conduct regimes

Each page subject (the practice and each person) carries a `regime` derived from verification records and self-declaration (a person enrolled as an advocate with any State Bar Council is `bci_r36` even when acting only as a neutral, pending counsel; OI-03):

| Regime | Applies to | Source |
|---|---|---|
| `general` | Neutrals who are not advocates, CAs, CSs or CMAs (for example retired judges not enrolled, other professionals, mediators by training) | RE F2.1 (no statute restricts advertising by non-advocate neutrals; general consumer-protection law applies) |
| `bci_r36` | Advocate-neutrals; chambers whose `is_advocate_entity = true` (law firm, bar association) | BCI Rules Part VI Ch. II Section IV r.36 and the 2008 Schedule [RE F1.2]; *P.N. Vignesh* (Mad HC 2024); SLP (C) 25794/2024 pending |
| `icai` | Chartered accountants | ICAI ESB 23 Oct 2019; Website Advisory 14 Oct 2020 [RE F1.5] |
| `icsi` | Company secretaries | ICSI Guidelines for Advertisement 2020 (ICAI-equivalent restrictions applied by default) [RE F1.5] |
| `icmai` | Cost accountants | ICMAI Guidelines for Advertisement 2025 (effective date not confirmed) [RE F1.5] |

Block availability by regime (✓ available; R restricted as noted; — not available):

| Block | `general` | `bci_r36` | `icai` / `icsi` / `icmai` |
|---|---|---|---|
| `hero` | ✓ | R: name, address/contact line, "Advocate, {State Bar Council}" only; no tagline; no primary action | R: name and designation only; no tagline |
| `bio` | ✓ | R: Schedule fields only — name; address, telephone, email; enrolment number, date, State Bar Council of original and current enrolment, Bar Association; professional and academic qualifications; areas of practice | R: write-up of services the member may lawfully render; no superiority claims, awards or "why choose us" |
| `practice_areas` | ✓ | ✓ (as "areas of practice") | ✓ |
| `process_explainer` | ✓ | ✓ (institutional process text only, not about the person) | ✓ |
| `fee_schedule` | ✓ | — | — |
| `rules_adopted` | ✓ | ✓ | ✓ |
| `availability` | ✓ | — | — |
| `enquiry_form` | ✓ | — | — |
| `faq` | ✓ | R: process FAQs about the centre only | ✓ |
| `publications` | ✓ | — (pending counsel) | R: titles only |
| `languages`, `jurisdictions` | ✓ | — (filter metadata only, hidden) | ✓ |
| `team` | ✓ | R: Schedule fields only | R: name and designation |
| `contact` | ✓ | ✓ (Schedule contact fields) | ✓ |
| `model_clause` | ✓ | ✓ (centre's clause) | ✓ |
| Photos and video | ✓ (consented) | — (OFF pending OI-03) | — |
| `marketplace_link` | ✓ | — | — |
| Indexing | `index` | `noindex` default (G: `tenant.chm.pages.r36_indexing`, counsel opinion required) | `index` |
| Sponsored eligibility (§W.3.10) | Possible | Never | Never |

Fee transparency for restricted regimes: fees are disclosed to a party inside the matter (intake quote, P05 binding quote) and in the downloadable rules document; this is disclosure to a party, not advertising **[VERIFY — open: counsel to confirm for advocate-neutral centres (OI-03)]**.

A chambers tenant with mixed people (for example a general chambers with one advocate member) renders each person card and person page under that person's regime; the practice home uses the tenant regime (`bci_r36` if `is_advocate_entity`, else `general`).

### W.3.8 Equator panel status on practice pages

An empanelled neutral may want to say they are on Equator's panel. Because this can imply that Equator endorses the private practice and engages E-Commerce Rules r.5(6) (no presenting a seller as associated with the marketplace without consent; no self-preferencing) [RE F3.1], the panel-status line is **flag-gated** `chambers.pages.show_equator_panel_status` (L platform flag, default **OFF**). No tenant or platform role can switch it in the product: it changes only by a platform release with an ADR and Head of Legal approval (X-43), on the recommendation of Equator legal counsel and the Institutional Committee Transparency sub-committee. When ON, only the fixed sentence "Also empanelled with Equator Resolution for Equator-administered matters. Appointments to those matters follow Equator's published allocation policy." may appear, generated from the verification record, without grade, and never in `bci_r36`, `icai`, `icsi` or `icmai` regimes.

### W.3.9 Copy lint for practice pages

Profile `chambers_practice` of the Appendix P linter applies LINT-001–LINT-050 (LINT-015 not applicable; LINT-021/022 only to process explainers) plus:

| ID | Rule | Pattern / check | Severity |
|---|---|---|---|
| CHM-LINT-01 | Court framing in tenant names and labels | Label validator deny-list (CHL-L01) on page titles, headings, nav labels, alt text, slugs | B† |
| CHM-LINT-02 | Equator endorsement | "Equator[- ]?(approved\|certified\|accredited\|recommended\|verified (mediator\|arbitrator\|chambers))", "administered by Equator", "Equator panel (grade\|member)" outside the §W.3.8 sentence | B† |
| CHM-LINT-03 | Outcome statistics | `\d+\s?%` within 8 words of (settle\|success\|won\|recover\|upheld\|resolved), "never (set aside\|challenged)", "(cases\|matters) (won\|resolved) " with a number | B† |
| CHM-LINT-04 | Guarantees of enforceability | "enforceable (anywhere\|worldwide\|in all countries)", "binding (like\|as) a (decree\|judgment)", "court-ready" (master X-34) | B† |
| CHM-LINT-05 | Regime field allow-list | Any field or block outside §W.3.7 for the subject's regime | B† |
| CHM-LINT-06 | Solicitation phrasing in restricted regimes | "hire", "book now", "call now", "best", "expert", "specialist", "free consultation" on `bci_r36` / `icai` / `icsi` / `icmai` subjects | B† |
| CHM-LINT-07 | Prohibited schema | `Review`, `AggregateRating`, `LegalService` (flag OFF), `Offer`/`price` in restricted regimes | B† |
| CHM-LINT-08 | Disguised advertisement | "Sponsored", "featured", "promoted", "partner" labels authored by the tenant (only P19 renders sponsorship labels, never on the practice page) | B |
| CHM-LINT-09 | Confidential information | Case numbers, party names or settlement amounts of real matters (pattern match on the tenant's own case-number prefix and party names of its matters) | B† |
| CHM-LINT-10 | Contact-hour and recovery tone | LINT-013 phrases; any implication that the chambers collects debts | B |
| CHM-LINT-11 | Staff code statements | "our lawyers", "legal advice" (except "not legal advice") on chambers pages (U §U.4 item 1; LINT-014) | B |
| CHM-LINT-12 | Unverified credentials | A credential phrase not backed by a verification record unless marked "Self-declared" | B |

B = blocks publish; † = no override. Other B rules can be overridden only by the D3-16 legal approver with a written, audited reason. Lint runs on save (inline), on publish (blocking) and nightly on the live crawl; a published page that newly fails and stays unresolved for 7 days moves to `suspended_lint` and the last passing version is restored.

### W.3.10 Marketplace projection and sponsored-placement eligibility (NN-34)

1. A practice can opt into the **Equator Marketplace** (P19 `mkp` surface) as a consented projection: the owner selects which person cards and fields are projected; each person's own display consent is required.
2. `chm` computes and publishes `sponsored_eligible` (boolean) with reason codes to P19; P19 owns ranking, sponsorship, rate cards and labels (X-48). `chm` never reads sponsorship status.
3. `sponsored_eligible = true` only if **all** hold: flag `marketplace.paid_placement` is ON (Board + counsel; default OFF); the subject's regime is `general`; the tenant is not `is_advocate_entity`; the subject has accepted the Equator Code or an equivalent adopted code (FR-P10-V2-04); no open complaint or discipline under Appendix N §7.8 or the tenant's own code; identity and credentials verified; for mediators, the training floor configured in P19 (research proposes 40 hours [RB §B item 10]); no unresolved CHM-LINT finding on the practice pages.
4. Reason codes (`CHM_SPONSORED_INELIGIBLE` detail): `FLAG_OFF`, `REGIME_RESTRICTED`, `ADVOCATE_ENTITY`, `CODE_NOT_ADOPTED`, `OPEN_DISCIPLINE`, `UNVERIFIED`, `TRAINING_FLOOR`, `LINT_OPEN`.
5. Practice pages never display "Sponsored", "Featured" or any paid marker; sponsorship appears only in P19's separately labelled slot ("Sponsored — paid placement. Does not affect Equator appointments.").
6. Group-affiliated practices (any chambers related to an Infrabyx group company or the Equator ADR Institute) carry the P19 "related to Equator" label and receive no ranking advantage [RE design F29].

### W.3.11 Editing, preview, publish and versioning

State machine `chm.page_versions.status`:

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | create | `chm.page_scope ≥ edit` | `draft` | Autosave every 10 s; editor presence lock |
| `draft` | submit | Lint has no blocking finding; theme validator passes; every enabled locale either reviewed or excluded | `in_review` | Reviewer notified; immutable snapshot hash |
| `in_review` | approve | Approver ≠ last editor when the tenant has ≥ 2 users with `publish`; sole practitioner: step-up confirmation (D3-18); `legal`/`rules` pages need `chm.config.approve.legal` | `approved` | — |
| `in_review` | reject | Reason required | `draft` | — |
| `approved` | publish (now or scheduled) | Domain healthy or Equator host; nightly lint not failing | `published` | Previous published version → `superseded`; CDN invalidation ≤ 60 s; sitemap update; `equator.chm.page.published.v1` |
| `published` | unpublish | Reason | `unpublished` | 410 for 30 days, then 404; sitemap removal |
| `published` | nightly_lint_fail (unresolved 7 days) | — | `suspended_lint` | Last passing version restored; tenant alerted |
| `superseded` | rollback | `publish` scope | `approved` → `published` | New version row referencing the restored snapshot |

Every version stores: block JSON, rendered HTML per locale, assets with SHA-256, lint report, axe report, approver, timestamps. Diff view between any two versions (blocks and rendered text). Versions are retained for the life of the tenant and exported at exit.

**Editor usability** *(v3.1)*

| Capability | Specification |
|---|---|
| Starter layouts | At first use, the editor offers starter layouts per page kind and regime: "Solo mediator home", "Arbitration chambers home", "Institution home", "Advocate-led centre (BCI r.36)" and "Fees and rules". Each is built only from blocks allowed for the subject's regime (§W.3.7) and pre-filled from data already held: display name, practice areas from the taxonomy, languages, the published rules version and fee schedule tokens, the grievance officer and contact. Every pre-filled field is marked "From your profile" until edited |
| Block library and saved sections | An insert panel (`/` or "+") lists only the blocks allowed for the regime, grouped Identity · Process · Fees and rules · Contact · Media. Owners and admins may save a configured block group as a **section** (`chm.page_sections`) for reuse across pages. A section re-runs lint wherever it is used, and editing a section offers "update everywhere" as a new draft of each page using it, never a silent change |
| Autosave and recovery | Autosave every 10 s to the server draft; the browser also keeps a local copy (IndexedDB) for offline recovery. After a crash or lost connection, "Restore unsaved changes from {time}" compares the local copy with the server draft before applying it |
| Concurrent editing | One editor holds the presence lock; the lock lapses after 2 minutes idle. Others see the page read-only with "Being edited by {name}" and may request takeover. The holder has 60 s to save and release, after which the lock passes. A save against a stale version returns `CHM_PAGE_EDIT_LOCKED` with a three-way diff |
| Undo and redo | 50 steps per editing session (`Ctrl/⌘ Z`, `Ctrl/⌘ Shift Z`); deleting a block is undoable until the session ends |
| Version compare | Side by side, rendered or block JSON, for draft vs published, any two versions, or one version across two locales. Changed blocks are highlighted, and lint findings are shown inline for both versions |
| Preview by device and context | Widths of 360, 768 and 1280 CSS px; light and dark; every enabled locale; "as the public sees it" (no editor chrome); and a regime simulation ("show this person page as `bci_r36`") so a general chambers can check an advocate member's card. The preview URL is signed, valid for 24 h and `noindex` |
| Live checks panel | Lint, contrast and axe results update on each autosave. Each finding links to its block, and a "Fix" action applies a suggested correction where one is defined (for example, adding missing alt text) |
| Scheduling | Publish at a date and time with an IANA time zone (default Asia/Kolkata). Scheduled versions show in a page calendar. A scheduled publish re-runs lint and domain health at the time of publishing and stays `approved` with an alert if a check fails |
| Keyboard shortcuts | `Ctrl/⌘ S` save; `/` insert block (screen-scoped to the editor canvas, Appendix AG §AG.5.5); `Alt ↑/↓` move block; `Ctrl/⌘ D` duplicate block; `Ctrl/⌘ Alt P` preview (*v3.1:* was `Ctrl/⌘ Shift P`, which some browsers reserve for a private window; AG §AG.5.5 rule 2); `?` lists the shortcuts. Every action is also reachable without the keyboard shortcut, and the editor is fully keyboard-operable (WCAG 2.1.1) |
| KPIs | Median time from first open to first published lint-clean page ≤ 30 minutes for CH-SOLO; share of publish attempts blocked by lint (target falling month on month); share of autosave recoveries used successfully |

---

## W.4 Practice configuration

All practice configuration objects are versioned and pinned to each matter at filing (NN-21). Each object has a tier (L/G/T, NN-33), a maker and, for G objects, an approval by the tenant's `chm.config.approve.legal` holder after the platform validators pass (D3-16). The full key list is in §W.8.

### W.4.1 Rules of procedure and codes

| Option | Behaviour |
|---|---|
| Adopt Equator Rules template | ERR-2026.1 (Appendix U §U.2) adopted with the chambers as administering body; Parts H–I (Equator's role, Institutional Committee, Registrar) replaced by "the Centre", "the Centre's appointing authority", "the Centre's case manager"; base version recorded |
| Fork and edit | Clause editor; each clause `locked`, `bounded` (within validator bounds) or `free`; diff against base |
| Upload own rules | DOCX converted to structured clauses (AI may segment; a human confirms every clause, NN-01); original preserved (NN-32) |
| Codes | Conduct: ECC-2026.1 or an equivalent passing the 15-Part validator (FR-P10-V2-04). Staff: ESC-2026.1 (Appendix U §U.4) or an equivalent with items 1–9, acknowledged by every staff member (§W.6.12) |

Validator (L, from P10 FR-P10-07 and CHL-L07) returns rule IDs and sources; G approval cannot proceed while any finding is open. Published rules appear on the `rules` page with version, effective date and change log; matters pin the version in force at filing.

### W.4.2 Fee schedules (NN-18, NN-29)

| Element | Configurable | Bounds |
|---|---|---|
| Registration, administration and neutral fees | Flat, banded, ad valorem with cap, hourly, per session/day, per stage | No outcome-contingent fees where prohibited (Appendix O X-07); no contingency fee or fee-sharing for advocates (BCI r.20; Ch. III r.2 [RE F1.2]) |
| Deposits, cancellation, refunds | Per stage and party; tenant policy text | Not less favourable than the platform floor (Appendix U §U.7); shown before payment (NN-29) |
| Currencies | INR; USD, EUR, GBP, SGD, AED for INT | FX snapshot (NN-13) |
| Regulated schedules | e.g. SEBI SMART ODR | Applied exactly; not editable (NN-18) |
| Concessions | Waiver classes (legal aid, hardship) | Equal criteria for every party |

Fee schedules are G (they affect parties' rights). The calculator, quotes and GST-inclusive display come from P05; tenant fee pages render `FeeToken`s only (LINT-020).

### W.4.3 Document templates

Template families: procedural orders, notices, appointment and disclosure letters (Sixth Schedule format for arbitrators), terms of reference, interim orders, awards (final, partial, additional, consent/settlement award under A&C s.30), corrections and interpretations (s.33), mediation settlement agreements, conciliation settlement agreements (ss.73–74), non-participation records, certificates of service, fee notes and invoices, letters to parties.

Rules for templates:

1. **Locked blocks** (CHL-L08): legal footer; e-stamp block where stamping applies (NN-09); excluded-instrument routing notice (NN-08); BSA 2023 s.63(4) certificate hook on export bundles (NN-10); signature blocks bound to `ESIGN_PORT`; QR verification block; page numbering "Page x of y".
2. **Award template checks** (validator, L): in writing and signed by the members of the tribunal (A&C s.31(1)); where signatures are omitted, the reason (s.31(2)); reasons unless the parties agreed otherwise or the award is on agreed terms (s.31(3)); date and place of arbitration (s.31(4)); costs under s.31A; interest under s.31(7) where awarded; delivery of a signed copy to each party (s.31(5)) is a workflow step, not template text.
3. **Settlement templates**: no "decree", "final and binding" within 10 words of mediation (LINT-004), no s.27 enforceability text while NN-05 is OFF (LINT-006); consent-award conversion offered where mechanisms allow (NN-19).
4. **Merge fields** only from the case data dictionary (Appendix F); unknown fields fail compilation; previews with synthetic data.
5. **Languages**: a template in any language requires human legal review before activation (NN-23) by the tenant's legal approver.
6. **Formats**: authored in the template engine, output DOCX (editable working copy) and PDF/A-2b (record copy) per D3-07.

Templates for orders, awards and settlements are G; letters, fee notes and non-legal notices are T.

### W.4.4 Intake forms

Built on the P02 form engine (`packages/forms`). Tenants may add fields, sections, conditional logic and document checklists to the platform intake for each mechanism × vertical. **Locked fields** that cannot be removed or reworded: DPDP notice and purpose-specific consents (NN-15), signposting cards where required (NN-20), conflict-disclosure inputs (other party names), vertical exclusions (NN-06, NN-24), representative authority (NN-27), accessibility and language preferences (NN-23). Tenant intake forms are T unless they add an eligibility rule that changes a party's access (then G).

### W.4.5 Notification templates

Channels: email (tenant sender domain or Equator fallback with tenant display name), SMS (DLT-registered headers and templates under the tenant's own entity when sending in its own name; P10 FR-P10-12), WhatsApp (approved templates), in-app, push. Locked: grievance-officer details and contact-hour limits in recovery-related messages (NN-12); no threat or recovery tone (LINT-013); unsubscribe for marketing; no marketing to respondents without separate consent (NN-16). Statutory and procedural notices are G; reminders and courtesy messages are T.

### W.4.6 Case numbering

Pattern tokens: `{PFX}` (tenant prefix, 2–6 capital letters, P10), `{VERT}`, `{MECH}` (NEG, MED, CON, ARB, MDA, EXD), `{CITY}` (IATA-style 3-letter code from a platform list), `{YYYY}`, `{FY}` (for example 2026-27), `{SEQ:n}` (zero-padded, n = 4–7), literal separators `/` and `-`. Default `{PFX}/{VERT}/{YYYY}/{SEQ:5}`. Rules: must contain `{PFX}` and `{SEQ}`; ≤ 40 characters rendered; unique per tenant; sequence resets per `{YYYY}` or `{FY}` when that token is present; **a format is immutable once a number has been issued under it** — a new format applies only to new matters (`CHM_NUMBERING_IMMUTABLE`); numbers never re-used; QR verification page on the canonical host. Tier T.

### W.4.7 Letterheads

Header (logo, name, address, registration numbers), footer (locked legal footer + tenant text), watermark options (`DRAFT`, `CONFIDENTIAL`, `SIMULATED` locked for sandbox), paper size A4 default (Letter optional), margins within print-safe bounds. One letterhead per legal entity and optionally per office. Tier T.

### W.4.8 E-sign and e-stamp settings

Default signature type per document class — Aadhaar eSign via ESP, DSC for neutrals' awards, click-wrap only for non-legal acknowledgements (G for awards and settlements, T otherwise); signing order, reminder cadence (1–7 days) and link expiry (3–30 days) (T); witness/attestation by document class (L, NN-08); e-stamp procurement through P06 or by the chambers with upload (G; the State duty matrix is platform-owned, NN-09); neutral DSC via USB token flow, never stored by Equator (L). Keys in §W.8.5.

### W.4.9 Invoicing as the chambers' own supply

The chambers is the supplier and merchant of record for its fees (P10 FR-P10-08); Equator's platform fee is Equator's own supply to the chambers.

| Field / rule | Detail | Tier |
|---|---|---|
| Legal entity | Name, PAN, CIN/LLPIN/registration, registered address, State code | G (KYB-verified; change needs re-verification) |
| GST registration | `registered` (GSTIN, validated checksum and PAN match), `unregistered` (bill of supply / fee note without GST; threshold parameter seeded at the CGST Act s.22 limit for services **[VERIFY — tax memo: ₹20 lakh / ₹10 lakh special-category States]**), `composition` (not available for most services; blocked unless the tax memo enables it **[VERIFY — tax memo]**) | G |
| Multiple GSTINs | One per State registration; place of supply decides which GSTIN invoices (P05 FR-P05-28) | G |
| SAC codes | Per service line from a platform list **[VERIFY — tax memo for arbitral, mediation and administration services]** | G |
| Reverse charge | Arbitral tribunal services and advocate legal services to a business entity flagged RCM (Notification 13/2017-CT(Rate) entries 2 and 3) — invoice shows "Tax payable on reverse charge: Yes" [RE F3.4] | L (rule), T (party classification evidence) |
| Invoice series | Tenant-defined prefix per GSTIN and financial year; consecutive serial, ≤ 16 characters including prefix, characters A–Z, 0–9, `-` and `/` only, unique per financial year (CGST Rules 2017 r.46(b)) — `CHM_INVOICE_SERIES_INVALID` | T within L rule |
| e-invoicing | IRN through `TAX_INVOICE_PORT` when the chambers' aggregate turnover crosses the notified threshold (parameter **[VERIFY — tax memo: current threshold]**); the tenant declares turnover band annually | G |
| TDS on receipts | Business payers may deduct TDS on the chambers' professional fees under ITA 2025 s.393(1) Table Sl. 6(iii); receipts accept net-of-TDS payment and track Form 131 certificates (P05 FR-P05-23) | T |
| Credit notes | Against original invoice; reasons; GST adjustment | T (maker-checker money rule applies) |
| Equator's platform fee | Equator invoices the chambers monthly (or deducts at source through Route with a monthly invoice) | L |
| E-commerce operator taxes | GST TCS (CGST s.52, 0.5%) and ITA 2025 s.393(1) Sl. 8(v) TDS (0.1%) where Equator collects consideration through the marketplace — governed by `billing.eco_withholding` / `billing.eco_gst_tcs` (LR-TAX-007/008; Appendix AA X-59 (h); default OFF until the tax memo; `tax.eco_*` are aliases, Appendix V X-44) [RE F3.4] | L (platform) |

### W.4.10 Payment collection settings

| Setting | Options | Tier |
|---|---|---|
| Linked account | Razorpay Route linked account in the chambers' name (KYC by the payment aggregator, penny-drop name match ≥ 0.85, 24-hour cooling on new linked accounts — P05 FR-P05-20) | G |
| Methods offered | UPI, cards, net banking, NEFT/RTGS virtual account; international cards for INT | T |
| Who pays which fee | Per mechanism default split (equal / claimant / as agreed) | G (affects parties) |
| Payment links | Expiry 1–30 days; reminders | T |
| Deposit requests | Per stage; escalation if unpaid | T |
| Refund approval | Maker-checker; refund policy per §W.4.2 | T (L for maker-checker) |
| Settlement money | Never through the chambers' linked account; bank escrow or direct party-to-party with proof (NN-13) | L |

### W.4.11 Case-status labels and client portal branding

**Status labels.** The canonical case state machine (master §5.1) is fixed. A tenant may set display labels per state and locale (for example `in_hearing` → "Sessions in progress"). Validator: label deny-list (CHL-L01); maximum 40 characters; may not imply a different legal effect (a label for `award_issued` cannot contain "decree", "judgment" or "order of court"); each label has a tooltip with the canonical meaning in plain words. Tier G (party-facing meaning).

**Client portal branding.** Party and counsel views of the tenant's matters use the tenant's logo, theme tokens (validated as §W.3.4), welcome text, help contacts and support hours. Locked: processor disclosure ("Technology provided by Equator Resolution Service Private Limited"), grievance officer, statutory notices, signposting cards, accessibility controls, the run-off notice when applicable, and the absence of any upsell in case views (Appendix O X-15). Tier T.

---

## W.5 Staff management and work

### W.5.1 Invitations and provisioning

1. **Invite** by email or mobile (OTP) with a role template, case-access mode and optional delegation. Privileged roles (`chambers_owner`, `chambers_hr`, `chambers_accounts`, `chm.config.approve.legal`) need owner approval with step-up (NN-36 privileged-role grant).
2. The invitee accepts the chambers' terms of access, the staff code (ESC-equivalent), the confidentiality undertaking and the monitoring notice (NN-35) before the first session.
3. If the invitee also has an HR record, the account links to it (one person, one record); otherwise HR may create the record later.
4. Seats are checked against the plan (`CHM_SEAT_LIMIT`).
5. Provisioning and revocation are logged in `chm.access_events`; the HR offboarding checklist (§W.6.4) revokes all grants, sessions, API keys and delegations at the exit timestamp.

### W.5.2 Case-level access

Access to a matter requires `chm.case_access` and, for `assigned`, an assignment row (`chm.case_assignments`: case, user, function — `case_manager`, `assistant`, `tribunal_secretary`, `observer_staff`; start, end). Assignment is blocked for users with a declared conflict on that case (`CHM_STAFF_CONFLICT_DECLARED`; Appendix S hard denial "no workforce principal accesses a case in its `conflicts[]`"). Caucus notes remain sealed to their author neutral for everyone (NN-11). Sealed tiers (POSH, health, family safety) follow NN-07 and are visible only to roles the sealed service allows.

### W.5.3 Delegation

A user may delegate named capabilities to another user for a period (≤ 90 days, renewable), with a reason. Delegation cannot exceed the delegator's own scope, cannot create a maker-checker conflict (the delegate cannot check what the delegator made), cannot delegate `chm.config.approve.legal`, owner capabilities or salary access, and is shown on every action taken under it ("on behalf of {delegator}"). Expiry is automatic; early revocation is immediate.

### W.5.4 Work queues, tasks and enquiries

| Queue | Items | Default routing | SLA default (T) |
|---|---|---|---|
| `enquiries` | Practice-page and marketplace enquiries | Round-robin among `front_desk`/`assistant`; owner sees all | First response 1 working day |
| `intake_scrutiny` | New filings needing scrutiny | Case managers by mechanism | 2 working days |
| `service` | Notices to serve, re-service | Assigned case manager | 1 working day |
| `scheduling` | Hearing/session scheduling requests | Assistant or case manager | 2 working days |
| `documents` | Uploaded documents to index or bundle | Assistant | 2 working days |
| `signatures` | Envelopes pending | Case manager | Reminder cadence per §W.4.8 |
| `payments` | Unpaid deposits, failed payments, refunds | Accounts | 3 working days |
| `hr` | Leave requests, regularisations, onboarding tasks | HR / reporting manager | 2 working days |
| `approvals` | One unified inbox for every approval the user may decide: G settings and legal content (via `core.config_change_requests`), page publication, pay runs, off-cycle and F&F runs, bank-change exceptions, salary revisions, privileged grants, consultant payments, refunds and sensitive exports *(v3.1)* | Checker pool; items whose maker is the viewer are never shown as actionable | 1 working day; ordered by hard deadline first (pay date, F&F clock, `effective_from`), then age *(v3.1)* |

Tasks: title, linked object (case, enquiry, staff record, invoice), assignee, due date, priority, checklist, comments, attachments (stored in the object's store, never duplicating case documents into HR or vice versa). **Statutory clocks are not tasks**: they come from the clocks engine (NN-04) and appear in queues as read-only clock items with their owner.

Enquiry handling: `received → acknowledged → conflict_check → qualified | declined → converted_to_matter | closed`. The conflict check compares names against the tenant's own matters and contacts and, with the chambers' consent, the P03 blind-check index (§W.18). Declines use neutral templates. Enquiry data is the chambers' and never reaches Equator marketing (NN-16).

*(v3.1)* Additional enquiry states and checks:
- `awaiting_enquirer`: the chambers has asked the enquirer for information. The first-response SLA is met and the conversion clock pauses with reason `awaiting_enquirer`. After 14 days with no reply, the enquiry auto-closes, with a courtesy message.
- `withdrawn`: the enquirer withdraws through a link in the acknowledgement.
- **Duplicate check on receipt.** The same email or phone, with the same other-party name, within 30 days is flagged "possible duplicate", and the front desk may merge. A merge keeps both submissions and their consents.
- **Marketplace substitution within the chambers** *(Appendix AA §AA.6.7)*. For a marketplace engagement that is `on_hold` (provider on leave or unavailable), the owner or admin may propose another listed neutral of the same chambers. The proposal re-runs the conflict check (AA §AA.6.3) for the new neutral, needs every party's fresh acceptance (and, for an arbitrator, fresh appointment confirmation), and cannot raise fees without a variation the buyer accepts; until all accept, the original engagement stays `on_hold`. The chambers never substitutes a neutral in an Equator institutional appointment (NN-03).
- **Conversion pre-fill.** Conversion pre-fills P02 intake with the enquirer's details, dispute type, other party and language. Nothing is carried over from the free-text description except by a user's explicit copy.

### W.5.5 Calendars

Per neutral and staff member: working hours, leave (from HR-lite), hearings (from P04), holidays (State calendars from Appendix Z), buffer rules. Two-way sync with Microsoft 365 calendars through `WORKSPACE_PORT` (NN-40); the Google adapter stays OFF with the platform flag `platform.ops.workspace.google.enabled` (no India data region; Appendix AC D3-40). Sync exports **busy/free only** exported to the external calendar by default (no party names; T setting may add the case number). Practice-page availability (§W.3.3) reads only free/busy. `chambers_hr` and `chambers_accounts` see other people's calendars as busy/free only — hearing titles, case numbers and parties are withheld (D3-19).

**Out of office and the marketplace** *(v3.1; Appendix AA §AA.6.7)*. An out-of-office period set for a neutral or the practice on this calendar pauses new marketplace enquiries and bookings for the listed person automatically; the marketplace profile stays visible with "Not taking new bookings until {date}" (SCR-P19-13). Existing engagements are not affected; where one would breach a milestone during the absence, the `enquiries` queue gets a task to propose a substitution (§W.5.4).

### W.5.6 SLAs, workload and separation-of-duties engine

1. SLA policies per queue (T): target, working-day calendar, warning at 75%, breach event `equator.chm.sla.breached.v1`, escalation to admin.
2. Workload view: open items per person, due this week, overdue, hours scheduled in hearings, leave; capacity per person (T). Individual workload is visible to the person, their reporting manager, the admin and the owner; team aggregates to all managers (NN-35 outcome-based measurement; no activity telemetry).
3. **SoD engine** (L rules, evaluated at role grant, delegation, maker-checker submission and nightly): payee or employee creator ≠ payment approver; salary revision maker ≠ checker; bank-detail change approver ≠ the employee concerned ≠ the HR maker; pay-run maker ≠ checker ≠ (where possible) releaser; reconciler ≠ releaser; a person cannot approve their own record or that of a declared relative [RC design E item 25]. Conflicts block with `CHM_ROLE_SOD_CONFLICT`; in a single-person tenant D3-18 applies and an exception row is written.

### W.5.7 Staff conduct and conflicts

Every staff member signs the adopted staff code on joining and annually; declares conflicts (relationships with parties, representatives or neutrals); and records gifts or hospitality offered (default policy: refuse; register required). Declarations feed `chm.case_assignments` blocks and the tenant's conflict search.

### W.5.8 Assignment, workload balancing and leave-aware reassignment *(v3.1)*

These rules apply to staff work items only. Neutrals are never assigned by this engine: appointment in chambers matters follows the chambers' rules (§W.4.1), and Equator allocation never reads `chm` (NN-03, NN-28; `NO_CHM_READ_IN_ALLOCATION`).

1. **Strategies.** `tenant.chm.work.assignment_strategy` (T; per queue) is one of `balanced` (default), `round_robin` or `manual`.
2. **Eligibility.** A candidate is eligible only if all of these hold:
   - they hold the queue's function;
   - they speak the item's language where one is set;
   - they have no declared conflict on the case (`CHM_STAFF_CONFLICT_DECLARED`);
   - they are not on approved leave or a holiday on the due date;
   - their load is below `tenant.chm.work.overload_threshold_pct` of capacity.
3. **`balanced` scoring.** For each eligible candidate, load = Σ(open items × queue weight) ÷ weekly capacity hours (`tenant.chm.work.capacity_hours_week`). Queue weights are T and default to 1 (`intake_scrutiny` 2). The candidate with the lowest load wins; ties go round-robin. If no one is eligible, the item goes to the queue's lead with the reason "No eligible assignee: {reason}".
4. **Deadline-aware ordering.** Every queue sorts by:
   1. statutory clock expiry (read-only clock items, NN-04);
   2. SLA due time;
   3. priority;
   4. age.

   "Due today" and "Breached" tabs are pinned. A personal view never hides a clock item owned by the viewer.
5. **Leave-aware reassignment.** When leave of at least `tenant.chm.work.leave_reassign_min_days` working days (default 2; 1–10) is approved, the engine proposes reassignment of the person's items due during the leave. Each item goes to the person's delegate under §W.5.3, or else is re-scored under `balanced`. The owner or admin approves the proposal as one bulk action, item by item or all at once. Unapproved items stay with the person and show "Assignee on leave". Return from leave never pulls items back automatically.
6. **Rebalancing.** If a person stays above the overload threshold for 2 working days, the admin receives a rebalancing suggestion listing the items to move and to whom, ordered by due date. Accepting it reassigns those items, with "Reassigned by {admin}" on each.
7. **SLA pause with reason.** A queue SLA timer (never a statutory clock) may pause for a reason from `tenant.chm.work.sla_pause_reasons` (T; default `awaiting_party`, `awaiting_payment`, `awaiting_neutral`, `awaiting_enquirer`). Each pause is capped at 10 working days, after which the timer resumes and the item is flagged. Pause time is reported separately on the Staff workload dashboard.
8. **Bulk actions.** Reassign, change priority, snooze (≤ 3 working days with reason) and close duplicates. Each bulk action shows a preview of the items affected and writes one audit event per item.
9. **NN-35.** Workload is measured on items, due dates and SLA attainment only. No activity telemetry, keystrokes or screen time is ever an input. Individual workload stays visible only to the roles in §W.5.6 (2).
10. **KPIs** (Staff workload dashboard): SLA attainment per queue; share of items reassigned during leave before their due date; median load spread (maximum ÷ median load per queue); paused-time share.

---

## W.6 Practice HR (HR-lite)

### W.6.1 Scope, position and disclaimer

Practice HR is an add-on (Appendix AB stream RS-10 "Chambers HR-lite and payroll add-on", **OFF until payroll UAT passes** [RB §C]) for chambers that employ or engage staff. It covers staff records, onboarding and offboarding, access provisioning, attendance and leave, salary structures and records, monthly payroll, payslips, disbursal, consultant fees with TDS, goals and reviews, policy acknowledgements and exports. It reuses the P18 payroll engine and the Appendix Z rule packs (X-49).

The chambers is the employer and data fiduciary; Equator is processor (D3-17). Fixed disclaimer, shown on the payroll home, every pay-run approval screen, the compliance wizard and every statutory output file cover sheet (not on employees' payslips):

> "Practice HR calculates statutory amounts from rule packs that Equator maintains from published sources, with the source and verification status of each value shown. It is a tool, not legal, tax or payroll advice. You remain responsible for your obligations as an employer. Where a value is marked 'secondary source' or 'not confirmed', check it with your chartered accountant or adviser before you rely on it."

Payslips carry instead: "Computed under the rule packs as configured: {pack list with versions}." [RC design B item 12].

### W.6.2 Size-aware compliance wizard

At activation and monthly on actual headcount, the wizard records headcount by class and switches duties on or off by threshold [RC F14, design F item 32]. Thresholds are the Appendix Z §Z.2.4 parameters under the same codes (`osh.establishment_threshold`, `coss.esi.establishment_threshold`, `coss.gratuity.establishment_threshold`, `coss.epf.establishment_threshold`, `cow.bonus.establishment_threshold`, `irc.grc_threshold`, `coss.esi.wage_threshold`, `coss.epf.wage_ceiling`); the seeds below are from research.

| Duty | Seed threshold | Status in research | Effect when crossed |
|---|---|---|---|
| Code on Wages: minimum wage, timely payment (s.17), deductions (s.18), equal pay (s.3), registers and wage slips (s.50) | All employees, any size | VERIFIED [RC F2, F14] | Always on |
| Appointment letter (OSH Code s.6(1)(f)) | Recommended for every hire; whether it binds below 10 workers is not confirmed | NC [RC F14] | Template issued for every hire by default |
| ESI | 10 or more persons; coverage wage ≤ ₹21,000/month; 0.75% employee, 3.25% employer | Threshold VERIFIED; rates SECONDARY [RC F3.2] | ESI lines computed; registration reminder |
| Gratuity | 10 or more employees; 5 years (fixed-term 1 year); 15 days' wages per year; divisor 26; ceiling ₹20 lakh | VERIFIED (official FAQ) [RC F3.3] | Provision and F&F computation |
| POSH Internal Committee | 10 or more employees; below 10 → Local Committee details displayed and a policy kept | [RC F9] | IC set-up task (P09 POSH SaaS link) or LC notice |
| OSH establishment, registration, s.32 annual leave | 10 or more workers | VERIFIED [RC F4.2, F4.5] | Leave floor layer switched on for `worker` class |
| EPF / EPS / EDLI | 20 or more employees (voluntary below); 12% + 12% (EPS 8.33% on wages up to ceiling, EPF 3.67%), EDLI 0.50%, admin 0.50%; wage ceiling ₹15,000 to 16 Sep 2026 and ₹25,000 from 17 Sep 2026 (S.O. 5109(E)) | Threshold VERIFIED; rates and ceiling SECONDARY [RC F3.1] | EPF lines; ECR file |
| Bonus (CoW Chapter IV) | 20 or more persons; 8.33%–20%; eligibility and calculation ceilings not notified | Ceilings NOT_CONFIRMED [RC F2.7] | Bonus computation disabled until ceilings are set (warning shown) |
| IR Code Grievance Redressal Committee | 20 or more workers | VERIFIED [RC F5] | Committee task |
| Shops and Establishments registration | Per State: UP 20+; Maharashtra 20+ (intimation below); Delhi conflicting; Rajasthan possibly exempt 0–10; Karnataka excluded for 10+ OSH-registered | SECONDARY / NC [RC F6.2] | State task with source links |
| Professional tax | By `pt_state`, which defaults to `establishment_state` (`tenant.chm.payroll.pt_state_rule`; Appendix Z D3-31) until a CA opinion supports the residence State; none in Delhi, Uttar Pradesh, Rajasthan; slabs elsewhere | SECONDARY / conflicts [RC F7.1, F6.3] | PT lines by `pt_state` |
| Labour Welfare Fund | By State | SECONDARY [RC F7.2] | LWF lines |

Whether advocates' chambers are "commercial establishments" in each State is **[VERIFY — open: RC F14, State S&E Acts]**; the wizard asks the chambers to confirm its registration status and stores evidence.

### W.6.3 Staff records and engagement types

`chm.staff_records` (one per person per engagement):

| Group | Fields |
|---|---|
| Identity | Legal name, preferred name, date of birth (restricted), gender (optional, for equal-pay analytics and maternity rules), photo (optional), PAN (validated, masked display), Aadhaar **reference only** (masked; never full number, NN-14), UAN, ESI IP number |
| Contact | Personal email, mobile, address, emergency contacts (name, relation, phone; at least one) |
| Engagement | `engagement_type` ∈ `employee`, `fixed_term_employee`, `apprentice`, `professional_engagement`, `contractor_staff` [RC F14, design F item 33]; designation; reporting manager; start date; probation end; confirmation date; fixed-term end; notice period; exit date and reason |
| Classification | `worker_class` ∈ `worker`, `non_worker`, `uncertain` (treated as worker) with reasons; reviewed annually and on role change [RC design C item 18] |
| Location | `establishment_state` and `work_location_state` per effective date; work mode (`office`, `remote`, `hybrid`) [RC F6.3] |
| Pay | Pay group, salary structure assignment, bank account (verified, §W.6.10), tax regime election per tax year |
| Documents | Appointment letter, offer, ID proofs (masked), qualification certificates, NDA, policy acknowledgements, exit documents — stored in the HR document store (separate S3 prefix and KMS key from case documents) |
| Access | Linked user account (optional), roles granted, devices issued |

Rules: advocates engaged by chambers (junior advocates on retainer) are modelled as `professional_engagement`, not `employee`, because BCI Rules Part VI Ch. II r.49 restricts a practising advocate from full-time salaried employment **[RC F14 tag K; VERIFY — open: counsel]**. A misclassification checklist (control of how work is done, fixed hours, exclusivity, employer tools, integration) runs before a `professional_engagement` is created for a non-advocate and returns `CHM_ENGAGEMENT_MISCLASSIFICATION_WARNING` (acknowledgement with reason required) when answers indicate employment [RC F14, citing *Dharangadhara Chemical Works v State of Saurashtra* AIR 1957 SC 264]. `contractor_staff` records hold the agency and principal-employer wage-payment check.

### W.6.4 Onboarding and offboarding checklists

Default onboarding checklist (tenant may add items; L = locked): offer accepted (e-sign); appointment letter in the OSH format (L — may be marked "not applicable" only with a reason); identity and PAN verified with masked Aadhaar reference (L); bank account verified by penny-drop (L); UAN/ESI registration where applicable (conditional L); policy acknowledgements — staff code, confidentiality, POSH policy, monitoring notice, IT use, leave policy (L); conflict declaration (L); nominations (CoW Form VII; gratuity after 1 year); seat, role and case-access provisioning (owner approval for privileged roles); equipment; probation goals.

Default offboarding checklist: resignation/termination recorded with date and reason; notice period and handover; **access revocation at the exit timestamp** (sessions, grants, delegations, API keys, calendar sync) — L; reassignment of open tasks and case assignments — L (performed by the owner or admin; `chambers_hr` sees only the count of open items, never the matters, D3-19); device and document return; F&F computed and paid **within 2 working days** of removal, dismissal, retrenchment or resignation (CoW s.17(2)) with leave encashment (OSH s.32(1)(vi)) — L clock; gratuity within 30 days where applicable (CoSS s.56) — L clock; service/experience certificate within the tenant-configured period (default 7 days, covering Karnataka's 7-day rule and the Model Standing Orders' 10 days [RC F5, F6.2]); exit interview (optional).

### W.6.5 Attendance (NN-35)

Default ON: check-in/out in the Equator app or derived from Equator login/logoff; coarse city-level location at check-in only (OFF by default); regularisation with manager approval; self-view and dispute of own records [RC design D items 20–24]. Biometrics OFF by default (templates never enter Equator). Prohibited monitoring is not offered (CHL-L11). An auto-generated monitoring notice (sources, purposes, retention, access; English and Hindi) is acknowledged at onboarding and on change. Telemetry 1 year then daily aggregates; registers 5 years after the last entry (Wages (Central) Rules 2026 r.51) [RC F11]. No adverse action on attendance data without a human-reviewed explanation opportunity.

Hours and overtime: default 8 hours/day, 48 hours/week for `worker` class; time above flags overtime requiring the worker's prior consent and pay at 2× (OSH s.27; CoW s.14); State quarterly overtime caps as parameters (144 hours where amended); never more than 10 consecutive days without a rest day [RC F2.6, F4.4, design C item 16]. Women's night work (before 06:00 or after 19:00) needs recorded, revocable consent and shows safety helpline details [RC F4.6].

### W.6.6 Leave

Two-layer model [RC design C item 13]:

1. **Statutory floor** computed per person from OSH s.32 (worker in a 10+ establishment: 180 days' eligibility, 1 day per 20 worked, carry-forward 30, encashment rules), the State S&E Act of the `establishment_state` where covered, and any more favourable State benefit.
2. **Practice policy** chosen from the Appendix Z templates — `leave.statutory_minimum@2026.1` or `leave.equator_standard@2026.1` (earned leave 18 days/year accruing 1.5/month from day one, carry-forward 45 with encashment of the excess, casual 8, sick 12, 10 paid holidays) [RC design C item 14] — or custom. The Appendix Z State uplift applies (§Z.8.3: for example a Rajasthan establishment's earned leave rises to the S&CE Act s.14 floor of 1 day per 12 days worked after 240 days). The validator rejects any policy that is less generous than the floor for any class on any dimension (`CHM_LEAVE_POLICY_BELOW_FLOOR`).

**Shared validator rules** *(v3.1)*: chambers leave ledgers use the same `packages/rules/leave` checks as Appendix Z §Z.8.3 — the `IN-MH` holiday-composition check (at least 4 national and 4 festival holidays among the 10 paid holidays; calendars with fewer national days are rejected) and the year-end `floor_true_up` entry (never a debit; also run on separation) — and the golden tests `HR_leave_true_up_*` run on chambers fixtures.

Leave types: earned/privilege, casual, sick, maternity (26 weeks; eligibility 80 days in the preceding 12 months; medical bonus ₹3,500 where not ESI-covered) [RC F3.4], paternity and others (tenant policy), compensatory off, leave without pay, work-from-home (recognised as a work mode, not leave). Holiday calendars per State and year from Appendix Z: the three national holidays are locked; festival holidays editable within the State count [RC design C item 15]. Leave applications, approvals and refusals are in writing (refusals with reasons; refused leave carries forward).

### W.6.7 Salary structures and records

1. **Components** come from the Appendix Z component register with a fixed `statutory_class` (`WAGE_CORE`, `EXCLUDED_A_TO_I` tagged by s.2(y) letter, `EXCLUDED_J_K`, `NOT_WAGES`, `IN_KIND`); a tenant may add components only by choosing a class, and the class is locked once used in a finalised run [RC design B item 6].
2. **Statutory wage calculator** on every structure save: wages = core + max(0, excluded(a–i) − 50% × total remuneration); in-kind counted up to 15%; golden test from the MoLE worked example (total ₹76,000 → statutory wages ₹22,000) [RC F2.1, design B item 7]. A CTC template that yields core below 50% without the add-back cannot be finalised.
3. **Structures** (CTC templates) and **assignments** are effective-dated; revisions are maker-checker (HR maker, owner checker; D3-18 in single-person tenants); arrears computed automatically.
4. **Restricted access**: salary amounts, bank details, tax declarations and payslips are Tier-High fields with field-level encryption; readable only by the employee (own), `chambers_owner`, and `chambers_hr` with `hr_scope = records_and_salary`; `chambers_accounts` sees amounts in pay-run totals and the disbursal file only. Every read of an individual's salary is logged in `audit.access_log` and visible to that employee on request.
5. **Equal-pay analytics** (optional, aggregate, shown only when each group has ≥ 3 people) on the CoW s.2(y) second-proviso basis [RC F2.8].

### W.6.8 Monthly payroll

Pipeline (Temporal `ChambersPayRunWorkflow`):

| Step | What happens | Gate |
|---|---|---|
| 1. Open period | Pay group, period, pay date (any date up to the statutory deadline — before the 7th of the following month for monthly wage periods, CoW s.17(1)) | L deadline; T pay date |
| 2. Freeze inputs | Attendance and loss-of-pay days, leave, overtime (with consent evidence), variable pay, reimbursements (with receipts), advances and loan instalments, fines and damage deductions (with show-cause and reply-window evidence), new joiners and leavers | Inputs locked after freeze; changes need reopen with reason |
| 3. Calculate | P18 engine (`packages/rules/payroll`, X-58) with Appendix Z rule packs: statutory wages, EPF/EPS/EDLI, ESI, PT by `pt_state`, LWF, TDS on salary under ITA 2025 s.392 with regime election, Form 124 claims and previous-employer Form 127 data, monthly re-estimation, rebate under s.156 with marginal relief [RC F8]; intra-period parameter changes pro-rated by calendar day (for example the September 2026 EPF ceiling split, method pending EPFO guidance) [RC design A item 2] | **Blocked** if any parameter used is `NOT_CONFIRMED` (`CHM_PAYRUN_PARAM_UNCONFIRMED`); `SECONDARY_ONLY` parameters require the owner's per-run acknowledgement [RC design A item 3] |
| 4. Guards | Total deductions ≤ 50% of wages per period with excess deferred and shown to the employee (CoW s.18(3); Central Rules r.13) (`CHM_PAYRUN_DEDUCTION_CAP`); no waiver of statutory dues (`CHM_STATUTORY_DUES_WAIVER` → `STATUTORY_WAIVER_FORBIDDEN`) | L |
| 5. Checks | Variance report vs previous run (headcount, gross, net, any person > 10% change — T threshold); ghost-employee checks: paid with no attendance; duplicate PAN/UAN/ESI/bank/phone/email; bank account shared with another payee; no appointment letter; paid after exit date; joined and paid in the same run [RC design E item 27] | Critical hits must be resolved (`CHM_PAYRUN_GHOST_HIT_UNRESOLVED`) |
| 6. Submit (maker) | `chambers_hr` (or owner in a sole practice) submits with comments | — |
| 7. Approve (checker) | `chambers_owner` or `chambers_accounts` checker; WYSIWYS summary (headcount, gross, deductions, net, employer contributions, variance, hits resolved); step-up passkey | Maker ≠ checker (`CHM_MAKER_CHECKER_SAME_USER`) or D3-18 single-person controls |
| 8. Disburse | Bank file or payout API (§W.6.10) generated only from the approved run by a releaser other than the maker (and other than the checker where a third person holds a money role, §W.5.6) | File hash recorded |
| 9. Reconcile | Bank acknowledgement / UTRs matched per payee; failures to an exception queue. A failed or returned line is never edited or re-sent from the original file. It is re-paid only through an off-cycle run after the payee's account is re-verified (penny-drop; cooling if the account changed), and the original line stays `failed` with its reason. Lines with no acknowledgement 3 working days after the pay date raise an alert to the owner *(v3.1)* | Reconciler ≠ releaser where ≥ 2 users |
| 10. Release payslips | Payslips become visible to employees on or before payment (Wages (Central) Rules r.52) | — |
| 11. Statutory outputs | Registers (Form I, IV, IX as per Central Rules r.51 or the State form loaded in the rule pack), EPF ECR, ESI return data, PT returns per State, LWF, TDS Form 138 quarterly data, Form 130 annually and Form 123 where salary > ₹1,50,000 [RC F8, design B item 11] | Output files carry the disclaimer cover sheet |
| 12. Lock | Period locked; corrections only by an off-cycle run (maker-checker) | Un-disableable edit log (NN-36; Companies (Accounts) Rules 2014 r.3(1) proviso) |

F&F runs are off-cycle runs with the 2-working-day clock (`wrk_wages_2wd`) shown as a red banner from the exit date; breaches alert the owner [RC design B item 10].

**Golden tests** *(v3.1)*: the Appendix Z §Z.9.13 worked examples (EPF full and split month, ESI, deduction cap, gratuity, TDS, rebate and marginal relief, LWP) run as CI tests against `ChambersPayRunWorkflow` with chambers fixtures (`CHM_payroll_golden_*`); a chambers result that differs from the Z result fails the build (X-49, X-58).

### W.6.9 Payslips

PDF/A-2b per person per run from the approved run and letterhead; fields per the wage-slip form in the rule pack (Wages (Central) Rules 2026 r.52 Form V, or the State form **[VERIFY — open: State forms]**): establishment, employee, period, days worked and paid, earnings and deductions by component, net pay, employer contributions, leave balances, tax summary, masked bank, pay date, rule-pack versions; bilingual where the pack requires. Available in ESS (web, mobile with app lock); email only as a PDF protected by a password the employee sets (never PAN or date of birth).

### W.6.10 Disbursal, bank details and maker-checker

**Disbursal port** `PAYOUT_PORT` (Appendix D §D.4.2; NN-40; renamed from the draft `DISBURSAL_PORT` under the X-49 naming rule so that `pay` and `chm` share one port and one bank-file generator):

| Adapter | How it works | Notes |
|---|---|---|
| `bank_file` (default) | Generates the bulk-payment file for the chambers' bank in a tenant-selected template (generic NEFT/RTGS CSV, plus bank-specific templates maintained as data); SHA-256 of the file recorded; the chambers uploads it to its own net banking; the bank's acknowledgement or UTR file is uploaded back for reconciliation | No manual edit of the generated file; a regenerated file gets a new hash and voids the old one; hash mismatch on acknowledgement → `CHM_DISBURSAL_FILE_HASH_MISMATCH` [RC design E item 28]. Bank template specifications **[VERIFY — open: per-bank formats to be confirmed during UAT]** |
| `payout_api` (optional, flag `tenant.chm.payroll.payout_api` G, default OFF) | Calls a `PAYOUT_PORT` provider adapter on an account **owned by the chambers** (credentials stored per tenant in Secrets Manager; Equator never a party to the funds) | `CHM_PAYOUT_ACCOUNT_NOT_TENANT_OWNED` if the account's KYC name ≠ the chambers' legal entity. Provider operating model and RBI Payment Aggregator Directions characterisation **[VERIFY — open: vendor contract and counsel]** |

**Bank-detail changes** [RC design E item 26]: only from the employee's own authenticated session (MFA) or HR-initiated with the employee's in-app confirmation; penny-drop name match; **cooling period of 3 working days** (T within L bounds 1–7) before the new account is used; notifications to the employee's registered email and phone and to the previous channel, with a reversal link that freezes the change; changes within 5 days of a pay date defer to the next run unless the owner approves with reason (`CHM_BANK_CHANGE_COOLING`). Name mismatch blocks (`CHM_BANK_NAME_MISMATCH`).

**Authority matrix (NN-36)** — defaults (T within L rules):

| Action | Maker | Checker | Releaser | Notes |
|---|---|---|---|---|
| Create staff record / payee | `chambers_hr` | `chambers_owner` | — | Creator cannot approve its first payment |
| Salary revision | `chambers_hr` | `chambers_owner` | — | — |
| Bank-detail change | Employee or `chambers_hr` | Employee confirmation + cooling period; `chambers_owner` for in-window exceptions | — | — |
| Pay run | `chambers_hr` | `chambers_owner` or `chambers_accounts` | `chambers_accounts` (file generation) | Releaser ≠ maker; releaser ≠ checker where a third person holds a money role (otherwise the owner checks); reconciler ≠ releaser where ≥ 2 users |
| Off-cycle / F&F | `chambers_hr` | `chambers_owner` | `chambers_accounts` | — |
| Consultant fee payment | `chambers_accounts` | `chambers_owner` | `chambers_accounts` other than the maker; else `chambers_owner` | Releaser ≠ maker; the user who created the payee cannot approve its first payment *(v3.1 fix: NN-36)* |
| Sensitive export (payroll, HR files) | Requester | `chambers_owner` | — | Step-up |
| Amount limits | Per role, configurable (for example owner approval above a run total set by the tenant) | — | — | Exceptions logged with reasons and reported monthly |

**Single-person tenants (D3-18).** When exactly one active natural person holds any money or HR capability: (a) that person may check their own submission only in a separate session with passkey step-up at least 10 minutes after submission, seeing the WYSIWYS summary; (b) bank-change cooling and out-of-band confirmation apply with no in-window override; (c) a 24-hour automatic hold applies to any run that adds a payee, uses a bank account changed in the period or breaches the variance threshold; (d) the owner may invite the chambers' CA as a free `external_checker`, after which normal maker-checker applies; (e) each self-check writes a `SINGLE_PERSON_SOD` row in `chm.control_exceptions`, summarised monthly to the owner and exportable to auditors. Moving from two-person back to single-person mode requires a 7-day cooling period.

### W.6.11 Consultant and professional fees

For `professional_engagement` records (junior advocates on retainer, consultants, freelance case-support professionals): fee notes or invoices received (GST if the professional is registered; RCM flag where an advocate supplies legal services to a business entity **[VERIFY — tax memo: chambers' status as business entity]** [RE F3.4]); TDS under ITA 2025 s.393(1) Table Sl. 6(iii) at 10% (2% for fees for technical services) once payments to the payee in the tax year exceed ₹50,000 [RC F14; P05 FR-P05-23]; lower-deduction certificates; Form 140 quarterly statement data and Form 131 certificates; payment through `PAYOUT_PORT` (`bank_file` default) under maker-checker. TDS deposit due dates under the Income-tax Rules 2026 are parameters **[VERIFY — open: RC open point 7]**; contractor-payment TDS (old s.194C successor under s.393) is not seeded **[VERIFY — open: serial, rate and threshold]**.

### W.6.12 Goals, reviews and policy acknowledgements

**Goals and reviews.** Goals per cycle (quarterly or annual, T) measured on outcomes — tasks on time, SLA adherence, quality reviews, client process feedback — never activity telemetry (NN-35). Case-outcome measures — settlement rate, award outcomes, who won, amounts recovered, neutral selection, speed of outcome — cannot be configured as goals or review measures for any chambers staff (`platform.hr.metrics.outcome_metrics_forbidden`, Appendix Z §Z.7.2; CHL-L03). Reviews: self and manager assessment, 3- or 5-point scale (no forced distribution by default), employee acknowledgement and right of response. AI may summarise the person's own goal notes on request but never proposes a rating. Review data never feeds allocation, neutral selection or any Equator system.

**Policy acknowledgements.** Versioned policies (staff code, confidentiality, POSH policy with IC/LC details, monitoring notice, IT use, data protection, leave, gifts and conflicts, reimbursements) e-acknowledged with timestamp and version, re-acknowledged on each new version; overdue items go to the HR queue.

### W.6.13 Exports to accounting and payroll tools

`ACCOUNTING_PORT` (Appendix AC; NN-40): payroll, invoice and receipt journals as CSV/XLSX with documented field mappings; named-package adapters (`tally_file`, `zoho_books`) behind flags **[VERIFY — open: vendor import formats]**. Payroll-tool exchange uses `PAYROLL_EXCHANGE_PORT` (`generic_csv`, Appendix Z §Z.9.10). Payroll exports (employee master, pay register, statutory registers, YTD tax) as XLSX + CSV + JSON (D3-07). Imports of employee masters and opening YTD balances from CSV with a dry-run report (migration rehearsal, NN-40).

### W.6.14 Micro-practice mode (1–5 people) *(v3.1)*

Most chambers employ one to five people: a clerk, an assistant, perhaps a junior on retainer. Micro-practice mode makes Practice HR usable for them without weakening any Locked control (CHL-L10 to CHL-L14 and D3-18 apply unchanged).

| Aspect | Micro-practice behaviour |
|---|---|
| Activation | `tenant.chm.hr.micro_mode` (T): `auto` (default; ON while active staff records ≤ 5), `on` or `off`. When `auto` crosses 5 records, the tenant gets a 30-day notice and a "switch to full mode" checklist. Data and history are identical in both modes; only the screens differ |
| Three-step setup | (1) Establishment State and address (pre-filled from KYB); (2) staff list: add people or import CSV, with engagement type, start date, monthly gross and bank account; (3) pay date and leave template ("statutory minimum" or "Equator standard"). The compliance wizard runs in the background and shows only the duties that apply. Duties not triggered appear as one line each, for example "ESI — not applicable below 10 employees (VERIFIED)", with the threshold that would trigger them |
| Monthly run | **"Repeat last month"** creates the run pre-filled with last month's inputs. Attendance defaults to the full period unless leave, LOP or exit is recorded. Changes from last month are highlighted, and the variance check and ghost checks still run. The run is one screen with three actions: review → submit → approve. The D3-18 timing rules apply automatically where one person holds every role, and the approve button shows the time remaining before it unlocks |
| Disbursal | Bank file by default, generated in one click after approval. A banner gives the steps to upload it in net banking, and the acknowledgement upload is offered the same day |
| Reminders | One compliance calendar shows the pay date (D-5, D-2), statutory payment and return dates for the duties that apply, policy re-acknowledgements and probation ends. Reminders go to the owner and HR only |
| Hidden by default | Performance reviews, equal-pay analytics, multiple pay groups, custom components beyond the template, and consultant TDS unless a `professional_engagement` exists. Each can be shown with one click from "More HR tools" |
| Checker prompt | While only one person holds money capabilities, the run screen offers a one-click invitation to the chambers' CA as the free `external_checker` (§W.9), which ends single-person mode for future runs |
| Guardrails kept | Fixed disclaimer; `NOT_CONFIRMED` block; per-run `SECONDARY_ONLY` acknowledgement; 50% deduction cap; pay-date deadline; F&F 2-working-day clock; bank-change cooling; un-disableable edit log; prohibited monitoring absent |
| KPIs | Median time to complete a monthly run for ≤ 5 staff ≤ 10 minutes (excluding the D3-18 gap); share of micro tenants with an external checker; share of runs approved on or before the pay date |

---

## W.7 Practice dashboards and reports

Dashboards render from tenant-scoped reporting views (no cross-tenant data, no Equator benchmarking across tenants — Appendix N §8.5 cl.7). Each metric has a definition, owner role and visibility.

| Dashboard | Metrics (definitions) | Visible to |
|---|---|---|
| Caseload | Open matters by mechanism, vertical and stage; new matters this month vs plan allowance; matters per neutral; clock risk (count of statutory clocks at T-30 or worse) | Owner, admin, case managers (assigned scope) |
| Stages | Median days in each stage; matters exceeding the tenant's internal stage targets (internal only, never published as a claim) | Owner, admin |
| Revenue | Invoiced, collected, by fee type, by neutral, by month and FY; GST collected; platform fees paid to Equator | Owner, accounts |
| Receivables | Ageing buckets (0–30, 31–60, 61–90, > 90 days) by payer type; deposits outstanding by matter | Owner, accounts |
| Utilisation | Hearing/session hours per neutral vs declared capacity; room usage | Owner, admin, each neutral (own) |
| Staff workload | Open tasks, overdue, SLA attainment per queue and person; leave calendar | Owner, admin, managers; each person (own) |
| Client process satisfaction | Process items only (punctuality, clarity, courtesy, accessibility, timeliness); response rate; shown when n ≥ 5 per item (internal) | Owner, admin, neutral (own) |
| Marketplace and enquiries | Enquiries received (practice page, marketplace), acknowledged within SLA, conflict-cleared, converted to matters, conversion rate, median time to first response; source breakdown | Owner, admin, front desk |
| HR | Headcount by class and State, joiners/leavers, leave liability, overtime hours, pending acknowledgements, compliance duties triggered | Owner, HR |
| Payroll | Run status, gross-to-net summary, employer cost, statutory dues and due dates, exceptions | Owner, HR, accounts |
| Controls | Maker-checker exceptions, `SINGLE_PERSON_SOD` rows, bank-change events, ghost-check hits | Owner, external checker |

**Workspace home** *(v3.1)*. `/chambers/work` (SCR-P20-29) renders the dashboard code `workspace_home`: a role-filtered composition of tiles from the dashboards above (clock risk and caseload; my tasks and SLA; enquiries; approvals waiting; revenue and receivables for owner and accounts; payroll and controls for owner, HR and the external checker). It is the landing route for chambers sign-in (Appendix AG §AG.0.5 #7). `workspace_home` is a dashboard code and is distinct from the page kind `practice_home` (§W.3.1).

Reports (scheduled or on demand; XLSX + PDF): monthly practice report, matter register, fee register, GST sales register, receivables, TDS receivable (certificates outstanding), staff register, leave register, pay register, statutory registers, control exceptions. Report scheduling is T; recipients must be tenant users.

---

## W.8 Practice settings catalogue

This is the chambers settings catalogue referenced by Appendix V. Tier per NN-33: **L** locked platform guardrail (shown read-only with its reason); **G** governed (maker + tenant legal approver `chm.config.approve.legal` after validators pass, D3-16; or Equator-governed where the "Who" column names an Equator role); **T** tenant (immediate, audited, roll-back). "Owner" = `chambers_owner`; "Admin" = `chambers_admin`; "HR" = `chambers_hr`; "Accts" = `chambers_accounts`; "Legal" = holder of `chm.config.approve.legal`. Every change writes `equator.chm.config.changed.v1` with before/after digests, in addition to the platform event `equator.cfg.setting.changed.v1` that busts the resolver cache (Appendix V §V.6.3). The settings UI shows the tier badge, who may change and whether approval is needed (NN-33).

### W.8.1 Practice identity and pages

| Key | Tier | Who may change | Default | Bounds / notes |
|---|---|---|---|---|
| `platform.chm.label.denylist` | L | Platform release only (ADR + Head of Legal; X-43) | P10 FR-P10-01 list | Tenants cannot edit; alias of `platform.naming.restricted_words` (J-106) |
| `chambers.court_label_override` | G | Equator counsel per tenant | OFF | Opinion attached (Appendix N §11.6) |
| `tenant.chm.identity.display_name` | G | Admin → Owner | Legal name | Label validator; change re-checks pages |
| `tenant.chm.identity.slug` | T | Owner | From display name | §W.3.2 rules; ≤ 2 changes/year |
| `tenant.chm.identity.public_label` | T | Admin | "Private ADR Chambers" | Label validator |
| `tenant.chm.identity.regime` | L (derived) | System from verification | `general` / `bci_r36` | Derived; counsel override per OI-03 only |
| `tenant.chm.pages.enabled` | T | Owner | ON | OFF unpublishes all pages (410) |
| `tenant.chm.pages.kinds_enabled` | T | Admin | `practice_home`, `rules`, `fees`, `contact`, `legal` | Entitlement for `custom` count |
| `tenant.chm.pages.default_locale` | T | Admin | `en-IN` | Any enabled locale |
| `tenant.chm.pages.locales` | T | Admin | `en-IN`, `hi-IN` | NN-23 list; each needs review before publish |
| `tenant.chm.pages.theme` | T | Admin | `classic` | Additional themes need entitlement `chm.pages.extra_themes` (RS-37) |
| `tenant.chm.pages.brand_tokens` | T | Admin | Theme defaults | Contrast validator (L) |
| `tenant.chm.pages.fonts` | T | Admin | Theme default | Allow-list (L); ≤ 2 families |
| `tenant.chm.pages.dark_mode` | T | Admin | OFF | Both palettes validated |
| `tenant.chm.pages.publish_approval` | T | Owner | Two-person when ≥ 2 publishers | Sole: step-up (L) |
| `tenant.chm.pages.legal_page_approval` | L | — | Legal approver required | D3-16 |
| `tenant.chm.pages.indexing` | T | Admin | `index` (`general`) | `bci_r36` uses next key |
| `tenant.chm.pages.r36_indexing` | G | Equator counsel per tenant | `noindex` | Counsel opinion; OI-03 |
| `tenant.chm.pages.ai_crawlers` | T | Admin | Block on person pages | Master X-42 |
| `tenant.chm.pages.process_feedback_block` | G | Legal | OFF | n ≥ 10 per item (L); claims record |
| `chambers.pages.show_equator_panel_status` | L (platform flag) | Platform release only, on counsel + Transparency sub-committee recommendation (X-43) | OFF | §W.3.8 |
| `tenant.chm.pages.enquiry_form` | T | Admin | ON (`general`) | Not available in restricted regimes (L) |
| `tenant.chm.pages.enquiry_fields_optional` | T | Admin | Description, language | Conflict-check field locked ON |
| `tenant.chm.pages.availability_block` | T | Admin | OFF | Needs calendar sync healthy |
| `tenant.chm.pages.map_provider` | T | Admin | Static image | Third-party map script needs cookie consent |
| `tenant.chm.pages.video_embeds` | T | Admin | Click-to-load | Captions required (L) |
| `tenant.chm.pages.lint_override_reasons` | L | — | Legal approver for non-† rules | † rules no override |
| `tenant.chm.pages.nightly_lint_grace_days` | L | — | 7 | — |
| `tenant.chm.marketplace.opt_in` | T | Owner | OFF | Per-person consent (L) |
| `tenant.chm.marketplace.projected_fields` | T | Owner | Name, practice areas, languages, cities | Regime allow-list (L) |
| `marketplace.paid_placement` | G (platform flag; not tenant-editable) | Board + counsel (P19) | OFF | NN-34; Appendix AA §AA.15 (`marketplace.paid_placement.advocates` is the L flag, always OFF) |

### W.8.2 Domains and SEO

| Key | Tier | Who may change | Default | Bounds / notes |
|---|---|---|---|---|
| `tenant.chm.domain.custom_host` | T | Owner | — | Entitlement `chambers.custom_domain`; TXT + CNAME + CAA checks (L) |
| `tenant.chm.domain.hsts` | L (host) / T (`includeSubDomains`) | Owner (sub-domain option only) | Host HSTS ON once the certificate is active; `includeSubDomains` OFF until confirmed | `max-age` 31536000; preload never automatic (§W.3.5) |
| `tenant.chm.domain.redirect_apex` | T | Admin | ON (apex → www) | — |
| `tenant.chm.domain.degraded_after_hours` | L | — | 72 | — |
| `tenant.chm.seo.title_template` | T | Admin | `{Page} — {Practice}` | ≤ 60 characters (L) |
| `tenant.chm.seo.meta_descriptions` | T | Admin | Generated | 70–155 characters (L) |
| `tenant.chm.seo.sitemap` | T | Admin | ON | OFF if `noindex` |
| `tenant.chm.seo.schema_types` | L | — | §W.3.6 set | Prohibited types blocked |
| `tenant.chm.seo.hreflang` | L | — | Auto | Reciprocal required |

### W.8.3 Rules, codes and fees

| Key | Tier | Who may change | Default | Bounds / notes |
|---|---|---|---|---|
| `platform.chm.rules.validator` | L | Platform release only (ADR + Head of Legal; X-43) | FR-P10-07 checks | — |
| `tenant.chm.rules.base` | G | Admin → Legal | Equator Rules template | Fork / upload |
| `tenant.chm.rules.version_published` | G | Admin → Legal | — | Pinned per matter (NN-21) |
| `tenant.chm.rules.code_of_conduct` | G | Admin → Legal | ECC-2026.1 | 15-Part validator (L) |
| `tenant.chm.rules.staff_code` | G | Owner → Legal | ESC-2026.1 | Items 1–9 present (L) |
| `tenant.chm.rules.arbitration_objection_window_days` | G | Admin → Legal | 15 | ≥ 15 (L) |
| `tenant.chm.rules.mediation_recording_default` | L | — | OFF | NN-11 |
| `tenant.chm.rules.tribunal_secretary_policy` | G | Admin → Legal | Disclosure + party consent | **[VERIFY — open]** |
| `tenant.chm.fees.schedule_version` | G | Accts/Admin → Legal | Template | NN-18 validator (L) |
| `tenant.chm.fees.currencies` | T | Accts | INR | INT: USD, EUR, GBP, SGD, AED |
| `tenant.chm.fees.consumer_gst_inclusive_display` | L | — | ON for individuals | NN-29 |
| `tenant.chm.fees.refund_policy` | G | Accts → Legal | Platform floor | Not below floor (L) |
| `tenant.chm.fees.concession_classes` | G | Owner → Legal | None | Equal criteria for all parties |
| `tenant.chm.fees.cost_split_default` | G | Admin → Legal | Equal | Mechanism-specific |
| `tenant.chm.fees.outcome_contingent` | L | — | Blocked where prohibited | Appendix O X-07; BCI r.20 |

### W.8.4 Templates, intake, notifications, numbering, letterheads

| Key | Tier | Who may change | Default | Bounds / notes |
|---|---|---|---|---|
| `tenant.chm.templates.awards_orders` | G | Admin → Legal | Platform set | Locked blocks (L); s.31 checks (L) |
| `tenant.chm.templates.settlements` | G | Admin → Legal | Platform set | LINT-004/006 (L) |
| `tenant.chm.templates.letters` | T | Admin | Platform set | Lint |
| `tenant.chm.templates.languages` | G | Admin → Legal | en, hi | Human legal review per language (L) |
| `tenant.chm.intake.forms` | T | Admin | Platform intake | Locked fields (L) |
| `tenant.chm.intake.eligibility_rules` | G | Admin → Legal | None | Cannot narrow statutory access |
| `tenant.chm.notify.procedural_templates` | G | Admin → Legal | Platform set | DLT/WhatsApp approval where applicable |
| `tenant.chm.notify.reminder_templates` | T | Admin | Platform set | LINT-013 (L) |
| `tenant.chm.notify.sender_email_domain` | T | Admin | Equator fallback | SES verification (L) |
| `tenant.chm.notify.sms_sender_mode` | G | Owner | Equator principal entity | Own DLT entity requires registration evidence |
| `tenant.chm.notify.recovery_contact_hours` | L | — | 08:00–19:00 local | NN-12 |
| `tenant.chm.numbering.format` | T | Admin | `{PFX}/{VERT}/{YYYY}/{SEQ:5}` | Immutable once used (L) |
| `tenant.chm.numbering.prefix` | T | Admin | From signup | 2–6 capitals; label validator |
| `tenant.chm.letterhead.*` | T | Admin | Generated | Locked footer (L) |
| `tenant.chm.status_labels.map` | G | Admin → Legal | Canonical labels | Deny-list; ≤ 40 characters |
| `tenant.chm.portal.branding` | T | Admin | Practice theme | Locked disclosures (L) |
| `tenant.chm.portal.help_contacts` | T | Admin | Practice contact | Grievance officer mandatory (L) |

### W.8.5 E-sign, invoicing and payments

| Key | Tier | Who may change | Default | Bounds / notes |
|---|---|---|---|---|
| `tenant.chm.esign.default_type.awards` | G | Admin → Legal | DSC (neutral) | Aadhaar eSign alternative |
| `tenant.chm.esign.default_type.settlements` | G | Admin → Legal | Aadhaar eSign | NN-08 routing (L) |
| `tenant.chm.esign.signing_order` | T | Admin | Parallel | — |
| `tenant.chm.esign.reminder_days` | T | Admin | 2 | 1–7 |
| `tenant.chm.esign.link_expiry_days` | T | Admin | 14 | 3–30 |
| `tenant.chm.estamp.mode` | G | Owner | Platform procurement | State duty matrix platform-owned (L) |
| `tenant.chm.invoice.legal_entity` | G | Owner | KYB record | Re-verification on change |
| `tenant.chm.invoice.gst_status` | G | Owner → Accts | From KYB | `registered` / `unregistered` (composition blocked pending tax memo) |
| `tenant.chm.invoice.gstins` | G | Owner → Accts | From KYB | Checksum + PAN match (L) |
| `tenant.chm.invoice.sac_map` | G | Accts → Owner | Platform list | **[VERIFY — tax memo]** |
| `tenant.chm.invoice.series` | T | Accts | `{PFX}/{FY2}/` + serial | r.46(b): ≤ 16 characters, unique per FY (L) |
| `tenant.chm.invoice.einvoice_enabled` | G | Accts → Owner | Per turnover declaration | Threshold parameter **[VERIFY]** |
| `tenant.chm.invoice.rcm_rules` | L | — | Notification 13/2017 entries 2–3 | Party evidence T |
| `tenant.chm.payments.linked_account` | G | Owner | — | KYC, penny-drop ≥ 0.85, 24 h cooling (L) |
| `tenant.chm.payments.methods` | T | Accts | UPI, cards, net banking | — |
| `tenant.chm.payments.link_expiry_days` | T | Accts | 7 | 1–30 |
| `tenant.chm.payments.refund_maker_checker` | L | — | ON | NN-36 |
| `tenant.chm.payments.settlement_money_routing` | L | — | Escrow or direct only | NN-13 |

### W.8.6 Staff, work and calendars

| Key | Tier | Who may change | Default | Bounds / notes |
|---|---|---|---|---|
| `tenant.chm.staff.role_templates` | T | Owner | §W.2.1 set | Custom templates ⊆ platform capabilities; cannot include hard-denied combinations (L) |
| `tenant.chm.staff.privileged_grant_approval` | L | — | Owner + step-up | NN-36 |
| `tenant.chm.staff.case_access_default` | T | Owner | `assigned` | `all_tenant_matters` logged |
| `tenant.chm.staff.tribunal_secretary_instruction_required` | G | Legal | ON | **[VERIFY — open]** |
| `tenant.chm.staff.delegation_max_days` | T | Owner | 90 | 1–90 |
| `tenant.chm.seats.ess_free` | G | Equator (Appendix AB registry) | true | ESS-only logins consume no paid seat |
| `tenant.chm.staff.mfa` | L | — | Mandatory | Passkey or TOTP |
| `tenant.chm.staff.session_idle_minutes` | T | Owner | 15 | 5–30 (Appendix S portal policy bound) |
| `tenant.chm.work.queues` | T | Admin | §W.5.4 set | — |
| `tenant.chm.work.sla.*` | T | Admin | §W.5.4 defaults | Warning at 75% (T) |
| `tenant.chm.work.capacity_hours_week` | T | Admin | 40 per person | — |
| `tenant.chm.work.individual_metrics_visibility` | L | — | Person + manager + admin + owner | NN-35 |
| `tenant.chm.work.assignment_strategy` *(v3.1)* | T | Admin | `balanced` (per queue) | `balanced`, `round_robin`, `manual`; never assigns neutrals (L) (§W.5.8) |
| `tenant.chm.work.queue_weights` *(v3.1)* | T | Admin | 1 (`intake_scrutiny` 2) | 0.5–5 per queue |
| `tenant.chm.work.overload_threshold_pct` *(v3.1)* | T | Admin | 120 | 100–200 |
| `tenant.chm.work.leave_reassign_min_days` *(v3.1)* | T | Admin | 2 working days | 1–10 |
| `tenant.chm.work.sla_pause_reasons` *(v3.1)* | T | Admin | `awaiting_party`, `awaiting_payment`, `awaiting_neutral`, `awaiting_enquirer` | ≤ 10 working days per pause (L); statutory clocks never pause (L, NN-04) |
| `tenant.chm.calendar.sync` | T | Each user | OFF | `WORKSPACE_PORT` |
| `tenant.chm.calendar.export_detail` | T | Owner | Busy/free only | Case number optional |
| `tenant.chm.enquiry.first_response_sla_days` | T | Admin | 1 working day | — |
| `tenant.chm.enquiry.retention_days` | T | Owner | 365 for unconverted | 30–730; DPDP purpose limitation |
| `tenant.chm.enquiry.awaiting_enquirer_close_days` *(v3.1)* | T | Admin | 14 | 7–30 (§W.5.4) |
| `tenant.chm.enquiry.duplicate_window_days` *(v3.1)* | T | Admin | 30 | 7–90 |

### W.8.7 Practice HR, payroll and disbursal

| Key | Tier | Who may change | Default | Bounds / notes |
|---|---|---|---|---|
| `tenant.chm.hr.enabled` | T | Owner | OFF | Entitlement (§W.9); stream ON in Appendix AB |
| `tenant.chm.hr.micro_mode` *(v3.1)* | T | Owner | `auto` (ON while ≤ 5 active staff records) | `auto`, `on`, `off`; Locked controls unchanged in every mode (§W.6.14) |
| `tenant.chm.ai.hr_summary` *(v3.1: key registered for P20 §11)* | T | Owner | OFF | Summarises an employee's own goal notes on request; never ratings, never attendance data (NN-01, NN-35) |
| `tenant.chm.hr.establishment_state` | G | Owner → HR | From KYB address | Drives S&E, PT, holidays |
| `tenant.chm.hr.offices` | T | HR | Registered office | Each with State |
| `tenant.chm.hr.headcount_basis` | L | — | Actual monthly headcount by class | Wizard re-run monthly |
| `tenant.chm.hr.engagement_types` | L | — | Five types (§W.6.3) | — |
| `tenant.chm.hr.misclassification_check` | L | — | ON | Acknowledgement with reason |
| `tenant.chm.hr.onboarding_checklist` | T | HR | §W.6.4 | Locked items (L) |
| `tenant.chm.hr.service_certificate_days` | T | HR | 7 | ≤ 10 (State rules may require fewer) |
| `tenant.chm.hr.probation_months` | T | HR | 6 | 0–12 |
| `tenant.chm.hr.notice_period_days` | T | HR | 30 | Contract; State floors (L) |
| `tenant.chm.attendance.capture` | T | HR | App check-in + login/logoff | — |
| `tenant.chm.attendance.checkin_location` | T | HR | OFF | City-level, at check-in only |
| `tenant.chm.attendance.biometric` | G | Owner | OFF | Templates never in Equator (L) |
| `tenant.chm.attendance.prohibited_monitoring` | L | — | Not available | CHL-L11 |
| `tenant.chm.attendance.telemetry_retention_days` | L | — | 365 then aggregate | RC D23 |
| `tenant.chm.time.daily_hours` / `weekly_hours` | T | HR | 8 / 48 | ≤ State and Code limits (L) |
| `tenant.chm.time.overtime_consent_required` | L | — | ON (workers) | OSH s.27 |
| `tenant.chm.time.overtime_multiplier` | L | — | 2.0 | Floor (L); may be higher (T) |
| `tenant.chm.leave.policy_template` | T | HR | `leave.statutory_minimum@2026.1` | `leave.equator_standard@2026.1` or custom; floor validator and State uplift (L) |
| `tenant.chm.leave.types` | T | HR | Template set | Maternity locked (L) |
| `tenant.chm.leave.holiday_calendar` | T | HR | State calendar | National holidays locked (L) |
| `tenant.chm.leave.approval_chain` | T | HR | Reporting manager | — |
| `tenant.chm.payroll.pay_groups` | T | HR | Monthly | — |
| `tenant.chm.payroll.pay_date` | T | Owner | Last working day | Before 7th of next month (L) |
| `tenant.chm.payroll.rule_packs` | L (mandatory adoption) | — (tenant cannot opt out, pin or adapt below the floor). Pack content is platform G, changed by the Appendix Z Payroll Compliance Officer → Company Secretary or `finance_controller` (Appendix V §V.2.1) | Latest approved versions | Tenant sees source, status and the "what changed" summary (Appendix V §V.2.7) |
| `tenant.chm.payroll.secondary_param_ack` | L | — | Owner per run | RC A3 |
| `tenant.chm.payroll.unconfirmed_param_block` | L | — | Block | RC A3 |
| `tenant.chm.payroll.epf_voluntary_below_threshold` | G | Owner → HR | OFF | Voluntary coverage evidence |
| `tenant.chm.payroll.epf_higher_wage_basis` | G | Owner → HR | OFF | Scheme rules (Appendix Z) |
| `tenant.chm.payroll.pt_state_rule` | G | Owner | `establishment_state` | Remote-staff residence State OFF pending CA opinion (RC G35) |
| `tenant.chm.payroll.components` | T | HR → Owner | Template | Class locked once used (L) |
| `tenant.chm.payroll.ctc_templates` | G | HR → Owner | Template | 50% wage rule (L) |
| `tenant.chm.payroll.variance_threshold_pct` | T | Owner | 10 | 5–25 |
| `tenant.chm.payroll.ghost_checks` | L | — | ON | Critical hits block |
| `tenant.chm.payroll.deduction_cap` | L | — | 50% of wages per period | CoW s.18(3) |
| `tenant.chm.payroll.payslip_language` | T | HR | English + Hindi | Rule pack may require State language (L) |
| `tenant.chm.payroll.payslip_email` | T | Each employee | OFF | Password set by employee |
| `tenant.chm.disbursal.adapter` | T | Owner | `bank_file` (`PAYOUT_PORT`) | `payout_api` needs next key |
| `tenant.chm.payroll.payout_api` | G | Owner | OFF | Tenant-owned account (L); **[VERIFY]** |
| `tenant.chm.disbursal.bank_template` | T | Accts | Generic NEFT/RTGS CSV | Data templates |
| `tenant.chm.bank_change.cooling_working_days` | T | Owner | 3 | 1–7 (L bounds) |
| `tenant.chm.bank_change.prepay_freeze_days` | T | Owner | 5 | 3–10 |
| `tenant.chm.control.two_person_mode` | T | Owner | Auto (ON when ≥ 2 eligible users) | Switch back to single needs 7-day cooling (L) |
| `tenant.chm.control.single_person_min_gap_minutes` | L | — | 10 | D3-18 |
| `tenant.chm.control.single_person_anomaly_hold_hours` | L | — | 24 | D3-18 |
| `tenant.chm.control.authority_limits` | T | Owner | None (owner approves all) | Exceptions reported (L) |
| `tenant.chm.consultant.tds_rules` | L (tenant cannot alter) | — (parameters are platform G in `rulepack.IN.tax.gst_it`, CFO + tax adviser) | s.393(1) Sl. 6(iii) 10%/2%, ₹50,000 | Parameters versioned |
| `tenant.chm.performance.cycle` | T | HR | Annual | Quarterly optional |
| `tenant.chm.performance.rating_scale` | T | HR | 5-point | 3 or 5; no forced distribution default |
| `tenant.chm.performance.ai_rating` | L | — | Not available | NN-01 pattern |
| `tenant.chm.policies.catalogue` | T | HR | §W.6.12 set | Monitoring notice mandatory (L) |
| `tenant.chm.posh.mode` | L (derived) | System | IC if ≥ 10 employees else LC notice | POSH Act ss.4, 6 |

### W.8.8 Reports, exports and offboarding

| Key | Tier | Who may change | Default | Bounds / notes |
|---|---|---|---|---|
| `tenant.chm.reports.schedules` | T | Owner/Admin | Monthly practice report | Tenant recipients only |
| `tenant.chm.reports.min_n_feedback` | L | — | 5 internal / 10 public | — |
| `tenant.chm.export.formats` | L | — | DOCX/XLSX/PDF(A)/CSV/JSON | NN-37 floor |
| `tenant.chm.export.sensitive_approval` | L | — | Owner + step-up | NN-36 |
| `tenant.chm.export.push_to_workspace` | T | Owner | OFF | SharePoint/OneDrive via `STORAGE_PORT` (Appendix AC §AC.11.8; destinations `tenant.xpt.push_destinations`); Google Drive only once `platform.ops.workspace.google.enabled` is ON |
| `tenant.chm.offboarding.runoff_days` | L | — | 90 | ≥ 60 platform bound (P10 §9) |
| `tenant.chm.offboarding.redirect_url` | T | Owner | None | 90 days; label validator on target text |
| `tenant.chm.offboarding.slug_quarantine_months` | L | — | 12 | — |
| `tenant.chm.offboarding.erasure_days_after_runoff` | L | — | 30 | Legal hold overrides |

---

## W.9 Plans, pricing hooks and entitlements

Plan prices and allowances remain those of Appendix O §2.8 (all "Subject to Board approval"). Chambers streams are rows in the **Appendix AB revenue-stream registry** under its `RS-xx` codes (Appendix AB owns the codes, status, price, GST/SAC, kill switch and approvals; status vocabulary `draft`, `in_review`, `approved`, `live`, `paused`, `retired`). This appendix sets **no new price figure**: every v3 price is a registry parameter that stays unpriced until the Board approves.

| Registry stream (Appendix AB code) | What it unlocks | Pricing unit (from research) | Eligible plans | Default status | Dependencies |
|---|---|---|---|---|---|
| RS-09 Private ADR Chambers subscriptions (CH-LITE…CH-INST; CH-IAAS under RS-36 rental) | Practice workspace per Appendix O | Per seat / month or year; per matter above allowance | All CH plans | ON (existing) | Appendix O §2.8 |
| RS-10 Chambers HR-lite and payroll add-on | Practice HR (§W.6) | Per employee record / month **[Board: price]** | CH-SOLO, CH-PRO, CH-INST, CH-IAAS | **OFF until payroll UAT passes** and payroll rule packs for the tenant's State are approved | Appendix Z; P18 |
| RS-38 Custom domains | Custom domain on CH-SOLO (included in CH-PRO/CH-INST) | Per tenant / month (price per Appendix O §2.8) | CH-SOLO (never CH-LITE — O §2.8; FR-P10-V2-O1) | ON (existing; Appendix AB) | §W.3.5 |
| RS-37 Page themes for Chambers and neutral public pages | Additional themes and extra `custom` pages (never labelled "premium" on public pages) | One-time or per tenant / month **[Board: price]** | CH-SOLO and above; included in CH-INST | OFF until the page builder and accessibility review pass (Appendix AB) | §W.3.4 |
| RS-09 (additional seats) | `chambers_staff`, `chambers_hr`, `chambers_accounts` seats beyond included | Per seat / month **[Board: price]** | CH-SOLO and above | `draft` price version under RS-09 | §W.2.1 |
| RS-19 Sponsored listing — Private Practice Marketplace | Sponsored slot on the Equator Marketplace for eligible practices | Per month per geography/practice area, equal rate card | Eligible `general`-regime practices only | **OFF** (`marketplace.paid_placement`) | NN-34; P19 |
| RS-18 Marketplace take on private-practice bookings | Marketplace take on bookings | 15/15/12/10% by plan (Appendix O O-R2, Board pending); flat per-booking fee for advocate-neutrals (master X-62) | CH plans | ON with the Appendix AA marketplace surface once the tax memo is recorded (AB §AB.3.2) | P19 |

Entitlement keys (add to Appendix O §4.2; values per plan are registry-owned):

| Key | CH-LITE | CH-SOLO | CH-PRO | CH-INST | CH-IAAS |
|---|---|---|---|---|---|
| `chm.pages.basic` (practice home, rules, fees, contact, legal, person pages for seats) | ✓ | ✓ | ✓ | ✓ | ✓ |
| `chm.pages.custom_count` | 0 | 2 | 10 | 25 | Contract |
| `chm.pages.extra_themes` (RS-37 Page themes) | — | add-on | add-on | ✓ | ✓ |
| `chambers.custom_domain` | — | add-on | ✓ | ✓ | ✓ |
| `chm.pages.locales_beyond_en_hi` | — | ✓ | ✓ | ✓ | ✓ |
| `chm.staff.seats_included` (staff + hr + accounts) | 0 | 1 | 3 | 10 | Contract |
| `chm.staff.external_checker_seat` (free, checker-only) | ✓ | ✓ | ✓ | ✓ | ✓ |
| `chm.hr.enabled` | — | add-on | add-on | add-on | Contract |
| `chm.hr.payout_api` | — | add-on (with HR) | add-on (with HR) | add-on (with HR) | Contract |
| `chm.reports.scheduled` | — | ✓ | ✓ | ✓ | ✓ |
| `chm.marketplace.opt_in` | ✓ | ✓ | ✓ | ✓ | ✓ |

The figures in the `custom_count` and `seats_included` rows are **proposals for the registry** (product decision, Board to approve), not facts. The external-checker seat is free on every plan because it exists to satisfy NN-36 (D3-18) and must not be priced as a barrier to a control. Upgrade prompts for these add-ons appear only in Settings and pricing pages, never in case, hearing or payroll-approval views (Appendix O X-15; LINT-034). A kill switch on any stream stops new charges within 5 minutes and keeps existing obligations (run-off) [RB §A item 6]; switching RS-10 off never deletes HR records — the module becomes read-only with full export.

---

## W.10 Data model (`chm` schema)

All tables: `tenant_id uuid NOT NULL` (the chambers tenant), RLS policy `tenant_id = current_setting('app.tenant_id')::uuid`, audit trigger writing hash-chained `audit.audit_events` (NN-22), UUIDv7 keys, `created_at`/`updated_at timestamptz`. HR tables (`staff_*`, `salary_*`, `pay_*`, `payslips`, `bank_accounts`, `consultant_*`, `reviews`, `goals`) have an **additional RLS policy** requiring `app.hr_scope` ≥ the row's sensitivity and are not granted to the DB role used by case services (D3-19). Salary amounts and bank account numbers are encrypted with a per-tenant data key (envelope encryption, KMS) and decrypted only in the HR service.

### W.10.1 Table inventory

| Group | Table | Key columns |
|---|---|---|
| Pages | `chm.sites` | `id`, `tenant_id`, `workspace_id → chambers.workspaces`, `slug` UNIQUE, `regime`, `default_locale`, `theme_code`, `brand_tokens jsonb`, `fonts text[]`, `status` (`active`, `suspended_lint`, `offboarded`) |
| | `chm.pages` | `id`, `site_id`, `kind`, `path` UNIQUE per site, `subject_person_id` (person pages), `published_version_id` |
| | `chm.page_versions` | `id`, `page_id`, `version_no`, `status` (§W.3.11), `blocks jsonb`, `snapshot_sha256`, `lint_report jsonb`, `axe_report jsonb`, `edited_by`, `approved_by`, `published_at`, `scheduled_for` |
| | `chm.page_renditions` | `page_version_id`, `locale`, `html_sha256`, `s3_key`, `reviewed_by`, `reviewed_at`, `machine_translated bool` |
| | `chm.page_assets` | `id`, `site_id`, `s3_key`, `sha256`, `media_type`, `alt_text`, `consent_attested_by`, `exif_stripped bool` |
| | `chm.people` | `id`, `site_id`, `user_id` (nullable), `staff_record_id` (nullable), `display_name`, `slug`, `regime`, `display_consent jsonb` (per field), `consented_at`, `withdrawn_at` |
| | `chm.domains` | `id`, `site_id`, `host` UNIQUE, `kind` (`subdomain`, `custom`), `txt_token`, `cname_target`, `caa_ok`, `acm_arn`, `status` (`pending`, `verified`, `active`, `degraded`, `released`), `hsts`, `verified_at`, `released_at` |
| | `chm.slug_quarantine` | `slug`, `released_at`, `quarantine_until` |
| | `chm.lint_overrides` | `id`, `page_version_id`, `rule_id`, `reason`, `approved_by` |
| | `chm.page_sections` *(v3.1)* | `id`, `site_id`, `name`, `blocks jsonb`, `regime_scope`, `version`, `created_by`, `used_in_page_ids uuid[]` |
| | `chm.page_edit_locks` *(v3.1)* | `page_id` PK, `holder_id`, `acquired_at`, `last_seen_at`, `takeover_requested_by`, `takeover_requested_at` |
| | `chm.marketplace_projection` | `site_id`, `person_id`, `projected_fields text[]`, `opted_in_at`, `sponsored_eligible bool`, `ineligible_reasons text[]`, `evaluated_at` |
| | `chm.enquiries` | `id`, `site_id`, `source` (`practice_page`, `marketplace`), `name_enc`, `contact_enc`, `dispute_type`, `other_party_names_enc`, `description_enc`, `consents jsonb`, `status`, `assigned_to`, `converted_case_id`, `retention_until` |
| Config | `chm.settings` (view) | Read-only view over `cfg.setting_values` for `tenant.chm.*` keys: `key`, `tier`, `value`, `version`, `effective_from`, `changed_by`, `approved_by`, `reason`. Values are stored only in `cfg` (one configuration plane, D3-10) *(v3.1 fix)* |
| | `chm.config_approvals` | Side table of `core.config_change_requests` (the only configuration approval engine, D3-10, X-56): `config_change_request_id` PK/FK, `object_type`, `object_id`, `object_version`, `validator_report jsonb`, `single_person bool`. Maker, approver and decision are read from the change request *(v3.1 fix)* |
| | `chm.templates` | `id`, `family`, `language`, `version`, `tier`, `body_ref`, `locked_blocks text[]`, `status`, `approved_by` |
| | `chm.numbering_formats` | `id`, `pattern`, `first_issued_at` (non-null ⇒ immutable), `reset_basis` |
| | `chm.status_label_maps` | `id`, `version`, `locale`, `map jsonb`, `approved_by` |
| | `chm.invoice_profiles` | `id`, `gstin`, `state_code`, `gst_status`, `series_prefix`, `fy`, `next_serial`, `einvoice_enabled`, `sac_map jsonb` |
| Staff and work | `chm.case_assignments` | `id`, `case_id`, `user_id`, `function`, `starts_at`, `ends_at`, `instruction_doc_id` (tribunal secretary) |
| | `chm.delegations` | `id`, `from_user`, `to_user`, `capabilities text[]`, `reason`, `starts_at`, `ends_at`, `revoked_at` |
| | `chm.queues` / `chm.tasks` | `queue.code`, `sla_policy jsonb`, `assignment_strategy`, `weight`; `task.object_type`, `object_id`, `assignee`, `due_at`, `priority`, `status`, `sla_breached_at`, `sla_paused_reason`, `sla_paused_at`, `paused_total_minutes`, `reassigned_from`, `reassign_reason` *(v3.1 columns)* |
| | `chm.staff_declarations` | `id`, `user_id`, `kind` (`conflict`, `gift`, `relative`), `subject`, `case_id`, `declared_at` |
| | `chm.access_events` | `id`, `user_id`, `event` (`invited`, `granted`, `revoked`, `session_killed`), `role`, `by`, `at` |
| HR | `chm.staff_records` | §W.6.3 fields; `engagement_type`, `worker_class`, `establishment_state`, `work_location_state`, `start_date`, `exit_date`, `status` |
| | `chm.staff_documents` | `id`, `staff_record_id`, `doc_type`, `s3_key` (HR prefix, HR KMS key), `sha256`, `expires_on` |
| | `chm.checklists` / `chm.checklist_items` | `kind` (`onboarding`, `offboarding`), `item_code`, `locked`, `status`, `evidence_ref` |
| | `chm.attendance_days` | `staff_record_id`, `date`, `status`, `first_in`, `last_out`, `source`, `regularisation_id` |
| | `chm.leave_policies` / `chm.leave_balances` / `chm.leave_requests` | `policy.template`, `floor_check jsonb`; `balance.type`, `accrued`, `used`, `carried`; `request.status`, `approver`, `reason` |
| | `chm.compliance_profile` | `tenant_id`, `month`, `headcount jsonb`, `duties_on text[]`, `evidence jsonb` |
| | `chm.salary_structures` / `chm.salary_assignments` | `components jsonb` (component code + statutory class + formula); `staff_record_id`, `structure_id`, `amounts_enc`, `effective_from`, `approved_by` |
| | `chm.bank_accounts` | `staff_record_id` or `payee_id`, `account_enc`, `ifsc`, `holder_name`, `name_match_score`, `status` (`pending_cooling`, `active`, `frozen`, `retired`), `cooling_until`, `requested_via` |
| | `chm.pay_runs` | `id`, `pay_group`, `period`, `pay_date`, `status`, `rule_pack_versions jsonb`, `totals_enc`, `variance_report jsonb`, `ghost_hits jsonb`, `maker_id`, `checker_id`, `releaser_id`, `single_person bool`, `hold_until` |
| | `chm.pay_lines` | `pay_run_id`, `staff_record_id`, `component`, `amount_enc`, `param_version_id` |
| | `chm.payslips` | `id`, `pay_run_id`, `staff_record_id`, `pdf_s3_key`, `sha256`, `released_at` |
| | `chm.disbursal_batches` | `id`, `pay_run_id` or `consultant_batch_id`, `adapter`, `file_sha256`, `status`, `ack_sha256`, `reconciled_at` |
| | `chm.consultant_engagements` / `chm.consultant_payments` | `staff_record_id`, `pan`, `tds_category`, `ytd_paid`, `ldc_ref`; `invoice_ref`, `gross`, `tds`, `net`, `status` |
| | `chm.goals` / `chm.reviews` | `cycle`, `measure`, `status`; `self_text`, `manager_text`, `rating`, `employee_ack_at`, `employee_response` |
| | `chm.policies` / `chm.policy_acks` | `code`, `version`, `doc_id`; `user_id`, `policy_version`, `acked_at` |
| | `chm.control_exceptions` | `id`, `kind` (`SINGLE_PERSON_SOD`, `IN_WINDOW_BANK_CHANGE`, `AUTHORITY_LIMIT`, `LINT_OVERRIDE`), `object_ref`, `reason`, `by`, `at`, `reported_in` |
| Offboarding | `chm.offboarding_runs` | `id`, `state` (§W.15.4), `requested_by`, `export_run_id → xpt.export_runs`, `runoff_until`, `domain_released_at`, `erased_at`, `legal_hold bool` |

### W.10.2 Key constraints

Binding DDL for `chm.page_versions`, `chm.numbering_formats`, `chm.invoice_profiles`, `chm.bank_accounts` and `chm.pay_runs` is in Phase P20 §7.2. Constraints that the DDL must encode: approver ≠ editor unless `approval_single_person`; numbering pattern contains `{PFX}` and `{SEQ:n}` and is immutable after first issue (trigger); invoice series prefix + serial ≤ 16 characters from `A–Z 0–9 / -` and unique per GSTIN and FY (CGST Rules 2017 r.46(b)); one owner per bank account and activation only after `cooling_until` with employee confirmation (trigger, no volatile functions in CHECK); regular monthly pay date before the 7th of the following month (CoW s.17(1)); no approval while any `NOT_CONFIRMED` parameter is used; checker ≠ maker unless `single_person`, with a trigger asserting the D3-18 conditions.

---

## W.11 APIs

REST `/v1`, OpenAPI 3.1, RFC 9457 errors, Idempotency-Key on every POST that creates money, pay runs, payees, exports or publications. Resource groups: public page and enquiry endpoints (`/v1/public/chambers/{slug}…`); sites, pages, versions, lint, themes and domains; marketplace projection and eligibility (read by the P19 service identity); settings with approve and rollback; rules, templates, numbering, status labels and invoice profiles; staff invitations, case assignments, delegations, queues, tasks and enquiries; HR staff records, compliance wizard, attendance, leave, salary, bank accounts (with a public reversal-token endpoint); pay-run workflow (`freeze`, `calculate`, `submit`, `approve`, `disbursal`, `acknowledgement`, `release-payslips`, `lock`) and statutory outputs; ESS payslips; consultant payments; goals, reviews and policy acknowledgements; dashboards and reports; exports and offboarding. The endpoint table with auth scopes is binding in Phase P20 §7.3.

---

## W.12 Events (CloudEvents `equator.chm.<entity>.<verb>.v1`; payloads carry IDs, versions and counts — never salary amounts, bank details, enquiry text or case content)

| Event | Emitted when | Key payload |
|---|---|---|
| `equator.chm.page.published.v1` / `.unpublished.v1` / `.suspended.v1` | Page workflow | `site_id`, `page_id`, `version_no`, `locales[]` |
| `equator.chm.domain.verified.v1` / `.degraded.v1` / `.released.v1` | Domain lifecycle | `site_id`, `host` |
| `equator.chm.enquiry.received.v1` / `.converted.v1` | Enquiry lifecycle | `enquiry_id`, `source`, `case_id` |
| `equator.chm.marketplace.eligibility_changed.v1` | Eligibility recomputed | `site_id`, `person_id`, `eligible`, `reasons[]` |
| `equator.chm.config.changed.v1` / `.approved.v1` / `.rolled_back.v1` | Settings | `key`, `tier`, `version`, `before_digest`, `after_digest` |
| `equator.chm.rules.published.v1` / `equator.chm.template.published.v1` | Legal content | `object_id`, `version`, `approver_role` |
| `equator.chm.staff.invited.v1` / `.access_granted.v1` / `.access_revoked.v1` | Provisioning | `user_id`, `role`, `by_role` |
| `equator.chm.delegation.created.v1` / `.ended.v1` | Delegation | `delegation_id`, `capabilities[]` |
| `equator.chm.sla.breached.v1` | Queue SLA breach | `queue`, `item_id` |
| `equator.chm.task.reassigned.v1` *(v3.1)* | Balancing, leave reassignment or bulk reassign (§W.5.8) | `task_id`, `queue`, `reason` (`balanced`, `leave`, `rebalance`, `manual`), `by_role` |
| `equator.chm.sla.paused.v1` / `.resumed.v1` *(v3.1)* | Queue SLA pause with reason | `item_id`, `reason` |
| `equator.chm.hr.staff_created.v1` / `.staff_exited.v1` | Staff record | `staff_record_id`, `engagement_type` |
| `equator.chm.hr.compliance_duties_changed.v1` | Wizard | `duties_on[]`, `duties_off[]` |
| `equator.chm.leave.decided.v1` | Leave | `request_id`, `decision` |
| `equator.chm.bank_change.requested.v1` / `.activated.v1` / `.frozen.v1` | Bank details | `account_id`, `cooling_until` |
| `equator.chm.payrun.calculated.v1` / `.approved.v1` / `.held.v1` / `.disbursal_generated.v1` / `.reconciled.v1` / `.locked.v1` | Pay run | `pay_run_id`, `headcount`, `rule_pack_versions`, `single_person` |
| `equator.chm.payslip.released.v1` | Payslips | `pay_run_id`, `count` |
| `equator.chm.consultant.payment_approved.v1` | Consultant fees | `payment_id`, `tds_applied` (bool) |
| `equator.chm.control.exception_recorded.v1` | Control exceptions | `kind`, `object_ref` |
| `equator.chm.export.ready.v1` | Export | `export_run_id`, `scope`, `manifest_sha256` |
| `equator.chm.tenant.offboarding_started.v1` / `.offboarded.v1` / `.erased.v1` | Offboarding | `offboarding_id`, `state` |

Consumers: P19 (eligibility, projection), P13 (sitemaps, CDN), P07 (notifications), audit, reporting. **No consumer in `neutrals`, allocation or the institutional directory may subscribe** to `equator.chm.*` (CI test `NO_CHM_READ_IN_ALLOCATION`).

---

## W.13 Error codes (new canonical codes; register in Appendix F §F.10.4)

Codes marked "maps to" are chambers-surface sub-codes of an Appendix Z or Appendix F canonical code raised by the shared payroll library, leave validator or controls (X-49, X-58); the HTTP status is the canonical code's status and the canonical code is returned in `canonical_code`.

| Code | HTTP | Meaning |
|---|---|---|
| `CHM_SLUG_RESERVED` | 409 | Slug is reserved or quarantined |
| `CHM_SLUG_TAKEN` | 409 | Slug used by another tenant |
| `CHM_LABEL_PROHIBITED` | 422 | Label validator failed (maps to `LABEL_PROHIBITED_TERM`) |
| `CHM_COPY_LINT_BLOCKED` | 422 | Blocking lint finding(s); `violations[]` lists rule IDs |
| `CHM_BLOCK_NOT_ALLOWED_FOR_REGIME` | 422 | Block or field outside the subject's regime allow-list |
| `CHM_THEME_CONTRAST_FAIL` | 422 | Palette fails WCAG 2.2 contrast |
| `CHM_FONT_NOT_ALLOWED` | 422 | Font not on the allow-list or too many families |
| `CHM_SCHEMA_PROHIBITED_TYPE` | 422 | Prohibited structured-data type |
| `CHM_LOCALE_NOT_REVIEWED` | 409 | Locale rendition not reviewed |
| `CHM_PUBLISH_APPROVAL_REQUIRED` | 409 | Approval missing or approver = editor |
| `CHM_PAGE_EDIT_LOCKED` *(v3.1)* | 409 | Another editor holds the page lock, or the save is against a stale version (three-way diff returned) |
| `CHM_DOMAIN_UNVERIFIED` | 409 | TXT/CNAME not found |
| `CHM_DOMAIN_IN_USE` | 409 | Host attached to another tenant |
| `CHM_DOMAIN_CAA_BLOCKS_ISSUANCE` | 422 | CAA records block the CA |
| `CHM_ENTITLEMENT_REQUIRED` | 403 | Plan or add-on does not include the feature |
| `CHM_SPONSORED_INELIGIBLE` | 422 | Not eligible for sponsored placement; reasons in `detail` |
| `CHM_EQUATOR_ENDORSEMENT_CLAIM` | 422 | Copy implies Equator endorsement or administration |
| `CHM_TEMPLATE_LOCKED_BLOCK_REMOVED` | 422 | Locked template block missing |
| `CHM_AWARD_TEMPLATE_INCOMPLETE` | 422 | s.31 required element missing |
| `CHM_FEE_PROHIBITED_STRUCTURE` | 422 | Fee structure prohibited (maps to NN-18 validator) |
| `CHM_NUMBERING_FORMAT_INVALID` | 422 | Pattern lacks `{PFX}`/`{SEQ}` or too long |
| `CHM_NUMBERING_IMMUTABLE` | 409 | Format already used |
| `CHM_INVOICE_SERIES_INVALID` | 422 | Series breaches CGST Rules r.46(b) |
| `CHM_GSTIN_INVALID` | 422 | GSTIN format, checksum or PAN mismatch |
| `CHM_STATUS_LABEL_PROHIBITED` | 422 | Status label prohibited or changes legal meaning |
| `CHM_LEGAL_APPROVER_REQUIRED` | 409 | G change needs `chm.config.approve.legal` |
| `CHM_ROLE_SOD_CONFLICT` | 409 | Role or delegation creates a separation-of-duties conflict |
| `CHM_CONFIDENTIALITY_WALL` | 403 | HR/accounts role requested case content, or case role requested HR data |
| `CHM_SALARY_ACCESS_DENIED` | 403 | No salary scope |
| `CHM_DELEGATION_SCOPE_EXCEEDED` | 403 | Delegation beyond delegator's scope |
| `CHM_SEAT_LIMIT` | 403 | No seat available |
| `CHM_STAFF_CONFLICT_DECLARED` | 403 | Assignment blocked by declared conflict |
| `CHM_SLA_PAUSE_NOT_ALLOWED` *(v3.1)* | 422 | Pause reason not configured, pause cap reached, or the item is a statutory clock |
| `CHM_ENGAGEMENT_MISCLASSIFICATION_WARNING` | 409 | Engagement looks like employment; acknowledgement required |
| `CHM_LEAVE_POLICY_BELOW_FLOOR` | 422 | Leave policy less generous than statutory floor (maps to `HR_LEAVE_POLICY_BELOW_FLOOR`) |
| `CHM_MONITORING_PROHIBITED` | 403 | Prohibited monitoring requested (maps to `HR_MONITORING_PROHIBITED`) |
| `CHM_PAYRUN_PARAM_UNCONFIRMED` | 409 | A rule-pack parameter used is `NOT_CONFIRMED` (maps to `PAY_PARAM_NOT_CONFIRMED`) |
| `CHM_PAYRUN_DEDUCTION_CAP` | 422 | Deductions exceed 50% of wages (maps to `PAY_DEDUCTION_CAP_EXCEEDED`) |
| `CHM_PAYRUN_GHOST_HIT_UNRESOLVED` | 409 | Critical integrity hit unresolved (maps to `PAY_GHOST_HITS_UNRESOLVED`) |
| `CHM_PAYRUN_DEADLINE` | 422 | Pay date after statutory deadline |
| `CHM_STATUTORY_DUES_WAIVER` | 422 | Attempt to waive statutory dues (maps to canonical `STATUTORY_WAIVER_FORBIDDEN`; F alias `WRK_STATUTORY_DUES_WAIVER`) |
| `CHM_MAKER_CHECKER_SAME_USER` | 403 | Checker equals maker outside D3-18 (maps to `CTL_SELF_APPROVAL_BLOCKED`) |
| `CHM_SINGLE_PERSON_GAP` | 409 | D3-18 minimum gap or hold not elapsed |
| `CHM_STEP_UP_REQUIRED` | 401 | Phishing-resistant step-up needed |
| `CHM_BANK_CHANGE_COOLING` | 409 | Account in cooling period or pre-pay freeze (maps to `CTL_COOLING_OFF_ACTIVE`) |
| `CHM_BANK_NAME_MISMATCH` | 422 | Penny-drop name match below threshold (maps to `CTL_PENNY_DROP_MISMATCH`) |
| `CHM_DISBURSAL_FILE_HASH_MISMATCH` | 409 | Acknowledgement does not match generated file (maps to `PAY_BANK_FILE_HASH_MISMATCH`) |
| `CHM_PAYOUT_ACCOUNT_NOT_TENANT_OWNED` | 422 | Payout account not owned by the chambers |
| `CHM_EXPORT_SCOPE_DENIED` | 403 | Export scope not permitted |
| `CHM_OFFBOARDING_OPEN_MATTERS` | 409 | Step blocked while matters are open (run-off continues) |

---

## W.14 RBAC matrix (chambers tenant)

Actions: **C** create · **R** read · **U** update · **S** approve/sign · **X** execute (publish, release, disburse, export) · **—** none. Brackets are conditions. Resources: Pages = practice pages and domains; Config-G / Config-T = settings by tier; Case content = case record, documents, hearings, orders, awards, settlements, notes; Billing = invoices, receipts, receivables (billing view shows matter number, payer and amounts only); Staff = invitations, roles, assignments, delegations; HR = staff records, attendance, leave, documents, goals, reviews, policies; Salary = structures, assignments, pay lines, payslips, bank accounts; Pay run = pay-run workflow; Exports = `CHAMBERS_TENANT` (alias `CHAMBERS_PRACTICE`), `EMPLOYEE_FILE`, `PAYROLL_FY` (Appendix AC §AC.13.3).

| Role | Pages | Config-G | Config-T | Case content | Billing | Staff | HR | Salary | Pay run | Exports |
|---|---|---|---|---|---|---|---|---|---|---|
| `chambers_owner` | C, R, U, S, X | C, U (maker); S [legal approver grant] | C, R, U | R [case role or `all_tenant_matters`; not caucus] | R, S refunds | C, R, U, S privileged grants [step-up] | R, U, S | R, S [step-up] | S checker; X hold release [step-up] | S, X [step-up] |
| `chambers_admin` | C, R, U, X [publish grant] | C, U (maker) | C, R, U | R [case role; not caucus] | R | C, R, U [non-privileged] | R [directory fields only] | — | — | X `CHAMBERS_TENANT` (no HR/payroll parts) [owner S] |
| `chambers_case_manager` | — | — | R | R, U [assigned] | R [assigned matters] | — | — | — | — | — |
| `chambers_staff` | R; U [`page_scope` grant] | — | — | R, U [assigned; function-limited; tribunal secretary: instructed cases; never caucus or deliberation] | — | — | — | — | — | — |
| `chambers_hr` | — | C, U HR keys (maker) | R, U HR keys | **— (DENY)** | — | R [directory]; U onboarding/offboarding checklist items | C, R, U | C, R, U [`records_and_salary`]; S never own record | C, U, submit (maker) | C request `EMPLOYEE_FILE` (owner S) |
| `chambers_accounts` | — | C, U invoicing keys (maker) | R, U billing keys | **— (DENY)** | C, R, U | — | R [payee identity only] | R [run totals, disbursal file] | S checker [≠ maker]; X disbursal file [≠ maker; ≠ checker where a third money-role holder exists]; X reconcile [≠ releaser where ≥ 2 users] | C request `PAYROLL_FY` (owner S) |
| `chambers_accounts` (`external_checker`) | — | — | — | **— (DENY)** | R | — | — | R [run totals] | S checker only | — |
| `neutral_*` (tenant) | R; U own person page [consent] | — | R | Per Appendix S §6.2 [appointed] | R own fee notes | — | R own ESS | R own | — | X own `EMPLOYEE_FILE` (if staff record exists) |
| `employee` (self) | — | — | — | — | — | — | R, U own; C leave, regularisation, acknowledgements | R own payslips; C own bank change | — | X own `EMPLOYEE_FILE` |
| Equator `support_agent` | R [ticketed grant ≤ 24 h] | — | R [ticketed] | — | R status | — | — | — | — | — |
| Equator `platform_admin` | — by default; JIT elevation [aal3, approved] | — | — | — | — | — | — | — | — | — |
| `auditor` (tenant-invited) | R | R | R | R [grant ≤ 90 days, scoped, watermark] | R | R | R [grant] | R [grant] | R | — |

**Hard denials (Cerbos `DENY`, override every allow):** `chambers_hr` and `chambers_accounts` on any case-content resource (`CHM_CONFIDENTIALITY_WALL`, D3-19); any role on caucus notes except the author neutral (NN-11); any case role on HR or Salary resources unless the same person also holds an HR scope — and then only through the HR service, never via case APIs; no principal approves their own salary, bank change or pay line; no principal is checker on a run they made (outside D3-18); Equator staff never read Salary or HR resources (processor access is limited to encrypted storage operations and break-glass with tenant notification); `machine` principals (including P19) read only `chm.marketplace_projection`.

---

## W.15 Audit, retention, exports and tenant offboarding

### W.15.1 Audit

Every material action writes a hash-chained `audit.audit_events` row (NN-22) with actor, role, delegation (if any), tenant, object, action, before/after digests and `single_person` flag. The payroll, billing and ledger tables keep an **un-disableable edit log** (NN-36; Companies (Accounts) Rules 2014 r.3(1) proviso). Reads of individual salary, bank and payslip records are written to `audit.access_log` and visible to the data principal on request. Page publications store snapshot hashes; domain events store DNS evidence.

### W.15.2 Retention (defaults; the chambers as employer/fiduciary may extend)

| Record | Default retention | Basis |
|---|---|---|
| Wage registers, attendance-cum-muster roll, wage slips | 5 years after the last entry | Wages (Central) Rules 2026 r.51 [RC F2.9] |
| Payroll, statutory returns, TDS records | 8 years from end of FY (recommended default covering known floors) | RC F11 recommendation; Companies Act s.128(5) books of account 8 years [RC tag K] |
| Raw attendance/session telemetry | 1 year, then daily aggregates | DPDP Rules r.6/r.8(3) floor [RC F11, D23] |
| Unconverted enquiries | 365 days (T, 30–730) | DPDP purpose limitation |
| Page versions | Life of tenant + export | NN-37 |
| Matter records | Per tenant records policy and Appendix Q | — |
| HR files after exit | 8 years (T) | Contract and limitation; employer decision |

Income-tax, EPF, ESI and POSH record periods under the new Rules are **[VERIFY — open: RC open point 14]**.

### W.15.3 Exports (NN-37, D3-07, `EQ-EXPORT-1.0`)

Scopes use the canonical Appendix AC §AC.13.3 names: `CHAMBERS_TENANT` (whole practice; `CHAMBERS_PRACTICE` is accepted as a v3.0 alias), `EMPLOYEE_FILE` (one person, for HR), `EMPLOYEE_SELF` (a staff member's own file), `PAYROLL_FY` (one financial year), plus `PARTY_IN_CASE` (party view) or `CASE_FULL` (the chambers' own administered matters, `chambers_owner`) per matter (`CASE` is an alias). Sensitive scopes (`EMPLOYEE_FILE` for others, `PAYROLL_FY`, any scope including HR data) need owner approval with step-up and run through the `ctl` action `EXPORT-SENSITIVE` (AC §AC.13.3; NN-36; D3-18 in single-person tenants). Export is free at any time and at exit.

Layout and taxonomy are those of D3-41 and Appendix AC §AC.13.2–§AC.13.9; this appendix adds no folder scheme of its own. `CHAMBERS_TENANT` and `PAYROLL_FY` default to the archival bag. Names are ASCII `NN_Title_Case_English`; the root is ≤ 40 characters and every path below the root ≤ 140 characters (AC §AC.13.7); files follow `<YYYY-MM-DD>_<DocType>_<ShortRef>_v<NN>.<ext>`. Where chambers records sit in the AC taxonomy:

```
Equator_Export_<OrgSlug>_<YYYY-MM-DD>/        bag root (≤ 40 characters, AC §AC.13.7)
  bagit.txt, bag-info.txt, manifest-sha512.txt, manifest-sha256.txt, tagmanifest-sha512.txt
  00_README.pdf                    what this is, folder guide, how to verify, records the chambers must keep as employer; English + Hindi
  99_Manifest/                     manifest.csv, manifest.json, checksums-sha256.txt, export_certificate.pdf (Equator DSC), schemas/, Tools/
  data/
    00_README.html
    00_Contents.xlsx               one row per file with SHA-256
    01_Organisation_Profile/       practice profile, legal-entity details, brands, signatories
    02_People_and_Roles/           users, roles, delegations, staff list, access reviews
    03_Cases/<CaseNo>_<ShortTitle>/  per matter, AC §AC.13.5; signed originals stay in their record folder as …_signed.pdf with …_rendition.pdf; audit extract and s.63(4) certificate in 10_Audit_Trail/
    04_Billing_and_Subscriptions/  invoices PDF/A, Invoice_Register.xlsx, credit notes, receipts, TDS certificates received, Ledger_Audit_Trail.csv
    05_Operations/
      Rules_and_Codes/             each published version DOCX + PDF/A, change logs
      Fee_Schedules/
      Website/                     page versions: HTML per locale, blocks JSON, assets, lint and axe reports
      Controls_Log/                maker-checker log, control exceptions, access events
    07_HR_and_Payroll/             RESTRICTED; present only where Practice HR was used (AC §AC.13.4 rule 3)
      Employment_File/<StaffSlug>/ EMPLOYEE_FILE layout (employment, leave and attendance, appraisals)
      Payslips/<FY>/               PDF/A
      Disbursal_Files/<FY>/        bank files + acknowledgements (hashes in the manifest)
      Payroll_Register_<FY>.xlsx, Statutory_Dues.xlsx, Attendance_and_Leave.xlsx, Payroll_Audit_Trail.csv
    08_Reports/                    practice dashboards as XLSX + PDF/A
    09_Settings_and_Configuration/ Settings.xlsx (tiers, versions, approvals), Rule_Packs.xlsx, Templates/ (DOCX sources + rendered PDF samples)
```

Structured data for each folder sits in its `_Data/` subfolder (CSV + JSON, AC §AC.13.4 rule 4). The README lists the records the chambers must keep as employer after exit (§W.15.2). Sealed-store data is excluded except via break-glass (Appendix Q).

### W.15.4 Tenant offboarding state machine

| State | Event | Guard | Next | Side effects |
|---|---|---|---|---|
| `active` | owner requests offboarding (step-up) | — | `offboarding_requested` | Banner to all users; new matters blocked; pages stay live; `equator.chm.tenant.offboarding_started.v1` |
| `offboarding_requested` | full export built and valid (bag valid, hashes match) | — | `export_ready` | Owner downloads; optional push to SharePoint/Drive with sample re-hash |
| `export_ready` | owner confirms download (or 14 days elapse) | — | `runoff` | P10 run-off for open matters (90 days, CHL-L15); parties notified with transfer/export options (FR-P10-04); HR-lite read-only; staff ESS export links sent to each staff member |
| `runoff` | day 90 or all matters closed/transferred | — | `domain_release` | Pages unpublished (tombstone, §W.15.5) |
| `domain_release` | release steps done | — | `closed` | Logins disabled; final export link (7-day validity) re-issued on request until erasure |
| `closed` | 30 days elapse, no legal hold | — | `erased` | Erasure per DPA; erasure certificate; `equator.chm.tenant.erased.v1` |
| any before `erased` | legal hold placed | — | same state, `legal_hold = true` | Erasure suspended; hold reason recorded |
| `offboarding_requested` / `export_ready` | owner cancels | subscription current | `active` | — |

Parties' access to their own matter records is never cut by offboarding before run-off ends (CHL-L15; NN-37).

### W.15.5 Domain and slug release

1. Remove the custom host from the CloudFront distribution; delete the ACM certificate; invalidate the TXT token; mark `chm.domains.status = released`; show the owner the DNS records to remove.
2. Equator-hosted `/chambers/{slug}` serves a tombstone page for 90 days: "This practice page is no longer hosted on Equator." with an optional tenant-provided redirect link (`tenant.chm.offboarding.redirect_url`, label-validated text, `rel="nofollow"`), then 410.
3. The sub-domain stops resolving portal routes after run-off; `/verify/{number}` QR pages for issued documents keep working read-only for the life of the documents' verification promise (the verification record is retained in Equator's verification index without case content) **[VERIFY — open: retention period for verification stubs after tenant erasure — product + DPO]**.
4. The slug enters `chm.slug_quarantine` for 12 months.

---

## W.16 Acceptance tests

The acceptance scenarios for this appendix are maintained once, in Phase P20 §12 (`tests/acceptance/p20/`), and cover every Locked guardrail CHL-L01–CHL-L18, the regime rules of §W.3.7, the settings bounds of §W.8 and the controls of §W.6.10. The CI checks `NO_PAID_PLACEMENT` (extended), `NO_CHM_READ_IN_ALLOCATION`, `CHM_CONFIDENTIALITY_WALL_MATRIX` (every HR/accounts role × every case resource returns 403) and `CHM_LINT_PROFILE` are part of the P20 exit gate.

---

## W.17 Open items and legal verification flags

| ID | Item | Default until closed | Approver | Disposition (App. J §J.6) |
|---|---|---|---|---|
| W-OI-01 | Whether BCI r.36 reaches chambers- or institution-run practice pages of advocate-neutrals (OI-03); outcome of SLP (C) 25794/2024 and WP (C) 817/2026 | `bci_r36` restricted mode; `noindex`; no fees, enquiry form, photos or sponsored eligibility | Counsel | Counsel sign-off |
| W-OI-02 | Fee disclosure for advocate-neutral centres (inside matters and rules documents only) | As §W.3.7 | Counsel | Counsel sign-off |
| W-OI-03 | Display of Equator panel status on practice pages (§W.3.8) | Flag OFF | Counsel + Transparency sub-committee | Product decision |
| W-OI-04 | Tribunal secretary disclosure and consent default | Instruction artefact + party disclosure required | Counsel | Counsel sign-off |
| W-OI-05 | GST: registration threshold for services, composition eligibility, SAC codes for arbitral/mediation/administration services, e-invoicing threshold, RCM where a junior advocate supplies a chambers | Parameters with `SECONDARY_ONLY` status; composition blocked | Tax adviser (tax memo) | Counsel sign-off |
| W-OI-06 | Payout API operating model (tenant-owned account, provider partner/OAuth model) and RBI Payment Aggregator Directions characterisation | `payout_api` OFF; bank file only | Counsel + vendor | Vendor confirmation |
| W-OI-07 | Bank bulk-payment file templates per bank | Generic NEFT/RTGS CSV only | Product (UAT with ≥ 3 banks) | Vendor confirmation |
| W-OI-08 | State wage-slip and register forms where the State is the appropriate Government | Central forms (Wages (Central) Rules 2026 r.51–r.52) with State override slot | Payroll compliance officer (Appendix Z) | Provisional |
| W-OI-09 | Whether advocates' chambers are "commercial establishments" under each launch State's S&E Act; Delhi registration status; Rajasthan 0–10 exemption | Wizard asks the tenant to confirm and upload evidence | Counsel | Counsel sign-off |
| W-OI-10 | BCI r.49 restriction on salaried employment of advocates (modelling junior advocates as `professional_engagement`) | `professional_engagement` default for advocates | Counsel | Counsel sign-off |
| W-OI-11 | PT and LWF for remote staff by residence State | `establishment_state` rule | CA opinion | Counsel sign-off |
| W-OI-12 | EPF September 2026 split-month method; bonus ceilings under CoW s.26; gratuity ceiling notification | Calendar-day pro-rating; bonus disabled; ₹20 lakh per official FAQ | Appendix Z owner | Watch / provisional |
| W-OI-13 | TDS deposit due dates (Income-tax Rules 2026); s.393 contractor-payment serial/rate/threshold | Parameters unset → contractor TDS disabled | Tax adviser | Provisional |
| W-OI-14 | Record retention periods for TDS, EPF, ESI and POSH records under the new Rules | 8-year default | Counsel + DPO | Provisional |
| W-OI-15 | Retention of QR verification stubs after tenant erasure | Retain number, issue date, issuer and hash only | Product + DPO | Product decision |
| W-OI-16 | Prices of v3 chambers add-ons and the included counts in §W.9 | Registry `draft`; features unavailable to buy | Board | Product decision |
| W-OI-17 | E-Commerce (Amendment) Rules 2026 sub-rule numbers and commencement (1 Jan 2027 per one source) for "related to Equator" labels and ranking disclosure on the marketplace projection | Comply in full from launch | Counsel | Counsel sign-off |
| W-OI-18 | Referral rewards to advocate tenants (FR-P10-10). **Closed in v3.0 by NN-17, X-54, X-60 and X-62:** no referral reward of any kind (cash, credit, discount or priority) to advocates, CAs, CSs or CMAs or their firms | No referral reward of any kind in any chambers flow (locked; `referral.exclude_advocates`, J-107) | — (decided) | Closed *(v3.1: stale open item corrected)* |

---

## W.18 Phase addenda

> Paste each block into the named phase file under a "v3 Addendum (23 October 2026) — From Appendix W" heading. Bare § references point to this appendix.

### For P03

**FR-P03-V3-W01 — Institutional profile isolation from practice pages.** `/neutrals/{slug}` (SCR-P03-02) and every allocation, eligibility and live-case screen render no link, badge, canonical, sitemap entry or structured-data reference to `/chambers/*`, a tenant sub-domain or a tenant custom domain (D3-15). *Acceptance:* crawl test over all seeded empanelled neutrals who own practice pages finds zero such references; `NO_PAID_PLACEMENT` and `NO_CHM_READ_IN_ALLOCATION` pass.

**FR-P03-V3-W02 — No `chm` reads in allocation.** The `neutrals` module and the allocation service have no DB grant on schema `chm`, no import of the `chm` client and no subscription to `equator.chm.*` events. *Acceptance:* the CI dependency and grant scans fail the build on any such path.

**FR-P03-V3-W03 — Blind conflict index includes chambers parties with consent.** With the chambers' consent under its DPA, party and enquiry names from `chm` matters and enquiries are added to the P03 blind-check index as salted hashes (no names, no case data), so a neutral's private-practice relationships surface as conflicts in Equator-administered appointments and vice versa (P10 FR-P10-06). *Acceptance:* a party who is a chambers client of neutral N produces a blind-check hit when N is proposed in an Equator matter; the hit reveals only "possible relationship — disclosure required".

### For P05

**FR-P05-V3-W01 — Chambers invoice profiles.** Invoicing in the chambers' name uses `chm.invoice_profiles` (GSTIN per State, FY series ≤ 16 characters under CGST Rules r.46(b), RCM flag rules, e-invoice enablement by turnover declaration) and `TAX_INVOICE_PORT` for IRN. *Acceptance:* `CHM_INVOICE_SERIES_INVALID` and `CHM_GSTIN_INVALID` scenarios pass; an RCM invoice prints "Tax payable on reverse charge: Yes".

**FR-P05-V3-W02 — `PAYOUT_PORT` for chambers disbursal.** Add the `bank_file` adapter to `PAYOUT_PORT` (default; hash-recorded files, acknowledgement reconciliation; shared with Equator payroll, Appendix Z §Z.9.4) and allow provider adapters on a tenant-owned account only (`payout_api`, flag OFF) for chambers payroll and consultant payments. Equator never holds these funds (D3-17). *Acceptance:* regenerated files void earlier hashes; acknowledgement mismatch raises `CHM_DISBURSAL_FILE_HASH_MISMATCH`; a payout account not in the chambers' name is refused.

**FR-P05-V3-W03 — Consultant fees with TDS for chambers payers.** Where the chambers is the payer, TDS under ITA 2025 s.393(1) Table Sl. 6(iii) is computed per payee per tax year (10% / 2%, ₹50,000 threshold) with Form 131/140 data. *Acceptance:* the first payment that takes a payee's tax-year total above ₹50,000 deducts TDS on the amount the rule pack specifies; certificates generate quarterly.

**FR-P05-V3-W04 — Chambers add-on entitlements.** Entitlement keys of §W.9 are read from the Appendix AB registry; add-ons are purchasable only when the registry stream is `live`. *Acceptance:* with RS-10 in `draft`, the HR add-on is not offered and `tenant.chm.hr.enabled` cannot be set.

### For P10

**FR-P10-V3-W01 — Role templates replace the v2 chambers seat model.** Migrate `case_manager (chambers seat)` to `chambers_case_manager`; add `chambers_owner`, `chambers_staff` (sub-templates `assistant`, `tribunal_secretary`, `front_desk`), `chambers_hr`, `chambers_accounts` (incl. `external_checker`) with the §W.14 matrix and hard denials (X-47). *Acceptance:* existing tenants migrate with no loss of access; the first admin of each tenant becomes `chambers_owner`.

**FR-P10-V3-W02 — Onboarding wizard v3.** FR-P10-12 gains steps "Practice page", "Staff and roles" and (if the add-on is enabled) "Practice HR compliance wizard", each with "Do this later". *Acceptance:* a CH-SOLO tenant can publish a lint-clean practice page during onboarding in one session.

**FR-P10-V3-W03 — Branding and domain v3.** FR-P10-05 is extended by §W.3.4–§W.3.5 (themes, fonts, WCAG 2.2 validator, CAA check, degraded state, release). *Acceptance:* Appendix W contrast and CAA scenarios pass.

**FR-P10-V3-W04 — Run-off covers Practice HR.** During run-off and suspension, HR-lite is read-only, payslips and ESS exports remain available to staff, and no pay run can be created after `closed`. *Acceptance:* a suspended tenant's employees can download payslips and their `EMPLOYEE_FILE` export.

**FR-P10-V3-W05 — Practice dashboards replace the health dashboard.** SCR-S-D10 renders the §W.7 dashboards by role. *Acceptance:* `chambers_hr` sees the HR and payroll dashboards and no caseload or revenue tiles.

### For P12

**FR-P12-V3-W01 — Chambers staff self-service on mobile.** Attendance check-in/out (location OFF by default), leave requests, payslip download (app lock and screen protection as for Tier-High, FR-P12-07), policy acknowledgements, own goals. *Acceptance:* payslips cannot be screenshotted on Android (`FLAG_SECURE`) and are blurred in the iOS app switcher.

**FR-P12-V3-W02 — Work queues and tasks on mobile.** Chambers case managers and staff see their queues, tasks and enquiries with offline drafts. *Acceptance:* a task updated offline syncs with conflict resolution "server wins, local kept as comment".

**FR-P12-V3-W03 — Owner approvals on mobile.** Pay-run, bank-change exception and privileged-grant approvals show the WYSIWYS summary and require passkey step-up in the system browser; D3-18 timing rules apply. *Acceptance:* approval within 10 minutes of submission in a single-person tenant is refused with `CHM_SINGLE_PERSON_GAP`.

### For P13

**FR-P13-V3-W01 — Practice page renderer.** SSR/SSG routes `/chambers/{slug}` and sub-paths with reserved slugs, canonical-host logic, tombstones and 410s (X-48); `/chambers` bare keeps the 301 to `/private-adr-chambers`. *Acceptance:* the SSR build check passes for all seeded practices; reserved slugs return `CHM_SLUG_RESERVED` at registration.

**FR-P13-V3-W02 — `chambers_practice` lint profile.** Add CHM-LINT-01–CHM-LINT-12 to `packages/content-lint` and run them on save, publish and nightly crawl. *Acceptance:* the §W.16 lint scenarios pass; nightly regressions move pages to `suspended_lint` after 7 days.

**FR-P13-V3-W03 — Structured data and sitemaps for practices.** Per-practice sitemaps, hreflang, `Organization`/`Person`/`Service`/`BreadcrumbList`/`FAQPage` JSON-LD with parity; prohibited types blocked (CHM-LINT-07). *Acceptance:* Rich Results and schema validators show no errors; no `Review` or `AggregateRating` anywhere under `/chambers/`.

**FR-P13-V3-W04 — "Report this page" and intermediary grievance.** Every practice page footer links to a report form routed to Equator's grievance officer with IT Rules 2021 timelines (7-day disposal; 3-hour takedown for specified content) [RE F3.3]. *Acceptance:* a report creates a P09 desk ticket with the page version snapshot attached.

**FR-P13-V3-W05 — `/private-adr-chambers` copy v3.** Add a "Your practice page" feature section (page builder, your domain, multilingual pages, practice HR as an add-on "subject to availability") under the Appendix P rules, with no outcome or ranking claims and a statement that practice pages are separate from Equator's neutral directory. *Acceptance:* LINT-001–LINT-050 pass; the page states "Your practice page does not affect appointments to Equator-administered matters."
