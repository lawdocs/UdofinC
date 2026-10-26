# Equator Resolution — Build Prompt Pack v3.2

**Prepared:** 19 October 2026 · **Revised:** 20 October 2026 (v1.1) · **v2.0:** 22 October 2026 (dispute-type specifications, ten new binding appendices, full v2 review) · **v2.1:** 22 October 2026 (all 469 open items researched and dispositioned; Appendix U policy baselines) · **v3.0:** 23 October 2026 (configuration framework, Operations Platform, marketing, workforce and payroll, marketplace and registry, revenue registry, workspace suites and portability, group companies, engineering governance; eleven new appendices and seven new phases) · **v3.1:** 24 October 2026 (review-and-improve pass on every file: errors fixed, workflows, options and menus improved; changes marked *(v3.1)*) · **v3.2:** 26 October 2026 (Infrabyx Platform Baseline Standard v1.0 adopted; Vidhi AI phase P22; full website content deck; design brief; environment and seed files; changes marked *(v3.2)*) · **Owner:** Company Secretary, Infrabyx Group · **Entity:** Equator Resolution Service Private Limited · **Product:** Equator Resolution (equatorresolution.in), an ODR institution with web and mobile platforms, plus the Equator Operations Platform for staff
**Stack (locked; IPB v1.0 applies — master §4.0):** Node.js 24.22.1 · Next.js web (`apps/web`) and Operations Platform (`apps/ops`) · NestJS (TypeScript) modular monolith · PostgreSQL only (Aurora PostgreSQL as reference adapter) with RLS · Temporal · Redis · OpenSearch · S3 Object Lock · React Native (Expo) mobile · Keycloak (`eq-portal-ops` for staff, phishing-resistant MFA) · Vidhi AI on `packages/vidhi` · 51 provider ports · AWS Mumbai (DR Hyderabad) as reference production, Terraform per cloud *(v3.2)*
**Companions (v3.2):** IPB v1.0 (`docs/ipb/`) · Ecosystem Integration Specification v1.2 · LawDocs Build Prompt Pack v1.1 · LawDocsComply Build Prompt Pack v1.3 · Finbyx Master Prompt v1.6 · Udofin Master Prompt v1.3 · Infrabyx Operations Hub Master Prompt v1.1

---

## 1. What this pack is

This is a paste-ready, phase-by-phase build prompt for a coding agent (Claude Code, Antigravity or equivalent) to build Equator Resolution end to end. It brings together the Equator corpus (551 documents) and research current to 26 October 2026 (v1: R1–R5, C1–C5 and the verification of 514 flags; v2: research streams S1–S9; v3: research streams RA–RE; v3.2: the IPB research notes, including the Jupitice and comparable-site structure review).

**What v3.2 changes (26 October 2026)** *(v3.2)*

The Infrabyx Platform Baseline Standard (IPB) v1.0 of 25–26 October 2026 is adopted in full. Every change is marked *(v3.2)*; nothing verified earlier is removed. Read `docs/ipb/00_README.md` before any phase.

- **IPB adoption clause** in master §4.0; precedence master → IPB → Ecosystem Spec → phase files → appendices (master §15); Equator's adoption notes and `fut.*` flags in master §4.6; deviations `IPB-DEV-01` (Payload retained as CMS editor runtime) and `IPB-DEV-02` (219-variable environment template).
- **Node.js 24.22.1** pinned everywhere (D3-48); **PostgreSQL only** with Aurora as the reference adapter; Terraform modules per cloud with one output contract; AWS Mumbai stays the reference production (D3-49).
- **51 provider ports**: the 35 Equator tokens aliased to IPB-01 names plus sixteen IPB ports incl. `TAG_MANAGER_PORT`, `EMBEDDING`, `TRUST`, `CONSENT`, `EGRESS`, `AV`, `HR`, `NOTIFY` (X-67).
- **Phase P22 — Vidhi AI Employee and Knowledge Notebooks (new).** The P11 agents become Vidhi skills on the shared kernel with autonomy ceilings (L2 maximum; L3 only for scheduling proposals and staff reminders) and the Equator locked list EQ-LK-01…12; five platform notebooks and private research notebooks; RRULE scheduled tasks with run-time permission re-checks, aligned with the Operations Platform autopilot (X-69); MCP server with read tools and confirmation-gated writes; four mandatory indicators on every surface. **NN-01 is unchanged.** P11 and Appendix E point to P22.
- **Website content deck** `content/Equator_Website_Content_v1.0.md` (≈ 18,700 words): full copy for Home, the four process pages and the hybrid page, six vertical landing pages, Neutrals (grading, Independence Evidence Pack), Marketplace, For organisations, Chambers, Training, About, Governance, Advisory Council, Team, Leadership, Investors (toggle; [COUNSEL]), Careers, Documentation hub, Press and media kit, Partners, Trust, Help, Pricing copy layer, Resources library, Blog with the user-post programme, Vlog, Contact (Delhi, Noida, Jaipur), Changelog, Accessibility statement; footer with social links and "Part of the Infrabyx Group"; cookie banner; 44 one-liners; 55 FAQs; SEO register; image placeholders; policy page list. Appendix P §3.1 (P-55–P-72) and Appendix AG §AG.2.1 updated.
- **Blog and resources**: toggle, bulk DOCX import with lint, user-authored posts (neutrals, academics; moderation; Claims Register; no case details), vlog with captions, Resources library with typed artefacts (P13 v3.2 addendum).
- **Brand Studio** `brand.app_name` (T with a G guard), social links, Investors toggle; **Pricing Studio** copy layer over Appendices O and AB; `TAG_MANAGER_PORT` with the Appendix Y ML-10 pixel rule kept (D3-54, D3-57).
- **Per-field "i" registry** `hlp.<module>.<term>` with CI lint and a regulatory-reference panel; ≥ 400 seeded terms (D3-60; X-70).
- **Vendor Assurance Room tenant mirror** under Settings › Security & trust › Vendor documents with SEBI CSCRF and IRDAI presets, evidence pack and auditor grants (P14 v3.2 addendum; D3-56).
- **Feedback widget and idea board**; **video tutorial pipeline** with staleness checks; What's new from release notes (D3-62, D3-63).
- **Engineering**: per-PR preview environments, `cc/<phase>-<slug>` branches, tenant beta programme, release-notes pipeline (Appendix AE; D3-64).
- **Settings tree** mapped to the twenty IPB-07 nodes (Appendix AG §AG.3.1; P15 v3.2 addendum; D3-58).
- **Policies**: ten IPB-05 inserts as new Appendix U registry kinds U-16–U-25 (D3-66).
- **`design/UI_UX_Design_Brief_v3.2.md`**: teal `#0E6E6E`, coral `#F26B5B`, Manrope; neutral, balanced, institutionally calm; tenant overrides within contrast guard-rails.
- **`env/`**: `.env.example` (221 annotated variables), `SEED_CREDENTIALS.md` (nine personas with the lead's exact credentials; production refuses seeds; first-login rotation), `README.md`.
- **Governance records**: `02` D3-48–D3-66, R-73–R-80, counsel questions 24–27, §7B phase mapping, §8C log; master X-67–X-70; Appendix F events #186–#189, §F.9.1 proposed Ecosystem events, §F.10.4 v3.2 codes; Appendix J §J.10 launch gates LG-V3-13–16 and open items V32-OI-01–18; `_review/v3.2_upgrade_review_log.md`.
- **Owner decisions added** (§4 items 22–25): Investors page publication and gating, Vidhi naming for Equator, the blog user-post programme, and the one-alternative-adapter rule for Tier-0 ports.

**What v3.1 changes (24 October 2026)**

Management's instruction of 24 October 2026: "Continue. Improvise the logics, workflows, options, menu, etc. so that I can build a better software, wherever possible. Review and fix the errors/mistakes." (R-11, R-29, R-71, R-72). v3.1 adds one appendix, no business module, and reviews and improves every file in place; each substantive change is marked *(v3.1)*.

- **Appendix AG — Information Architecture, Navigation, Menus and Workflow Patterns (new).** Shells and the complete menu tree of every portal, each leaf mapped to a screen ID and owning phase; one settings menu aligned to Appendix V; a unified **Work Inbox** that collects every approval, task, mention and deadline across the case plane and the business database without a cross-database join; global search and a `Ctrl/Cmd+K` command palette; role dashboards, a widget catalogue and deterministic "next best action" rules; a workflow pattern library (bulk jobs with preview and undo, drafts, confirmations, deep links); tenant menu and terminology overrides by tier; tours and in-app help; navigation accessibility, performance budgets and usability KPIs. Menus are data in a navigation registry (`cfg.nav_items`; D3-45–D3-47), and AG resolves eleven route and screen-ID collisions (§AG.0.5). Its addenda join P00, P01, P12, P13, P15 and P16 as `## v3.1 Addendum (24 October 2026)`.
- **Improvement themes applied across the pack.** (1) Missing workflow states with timers and escalation — withdrawn, on hold, reopened, partially settled, paused, superseded, merged — and idempotent retries with compensation steps (no partial activation). (2) Approvals: one inbox, review SLAs, escalation, delegation when the approver is on leave (never to the maker), and four distinct actors on pay runs. (3) Fewer clicks: document-first intake with pre-fill, KYB pre-fill, saved views, deadline-aware queues, bulk actions with impact preview and undo windows, keyboard shortcuts and palette entries. (4) Safety: previews, typed confirmations for irreversible steps, conflict re-checks, slot holds, grievance clock-start and level-2 rules, contact hours in force now with the 09:00–18:00 microfinance window. (5) Options: new settings registered with tier, default, bounds and approver. (6) Measurement: KPIs and acceptance tests for each improvement.
- **Counts.** Eight reviewers made **340 fixes** and **213 improvements** (`02` §8B, per reviewer); AG adds 11 cross-file resolutions. Governance files add master operating rules OP-1–OP-9, a v3 Definition of Done V-1–V-9, the P14 deferral rule and a hand-off checklist, and the P15–P21 squad plan (§3.1); `02` R-71, R-72 and D3-45–D3-47; Appendix F events #168–#185 and a v3.1 event register, actionable errors and every code defined in v3.1 (48 v3-context and 9 v2-context codes, plus 6 earlier gaps); Appendix G §G.7 v3 legal bases, flag-driving watch triggers, LR-SUCC-021 and the retirement of duplicate LR-MSME-016; Appendix J launch gates LG-V3-01–12 and the residual register V31-OI-01–24 (§J.9.3); Appendix U aligned with v3.

**What v3.0 adds (23 October 2026)**

Management's brief of 23 October 2026 asked for configurable open items and complete settings; deeper customisation and a small HR module for Private ADR Chambers and independent neutrals; a separate Operations Platform; workforce lifecycle, payroll and internal controls; Microsoft 365 with portable records; switchable revenue streams; marketing automation; empanelled advocates and a group-wide professional directory; change, patch and audit management; a departmental structure; multi-company operations; and an Equator Marketplace benchmarked against Jupitice.

- **Appendix V — Configuration Framework, Rule Engine and Settings Catalogue.** Three tiers for every configurable value (Locked, Governed, Tenant; NN-33); a Governed rule engine with effective dating, sandbox, impact analysis, rollback and a regulatory-watch feed; all 469 open items classified by configurability (L 65, G 346, T 7, N 51); a settings catalogue for every persona.
- **Appendix W — Private ADR Chambers Workspace v3 and Practice HR.** Practice pages and verified domains as a separate surface, extensive chambers and neutral settings, staff and case-manager queues, and a practice HR-lite module with salary records, pay runs and bank-file disbursal (Equator never holds salary money).
- **Appendix X — Equator Operations Platform: CRM, Onboarding, Customer Success, Support and Grievance.** A separate staff app (`apps/ops`), not the super-admin console; default departments and workspaces; the CRM of record (open to Brevo, HubSpot and Zoho); tickets and grievances; a no-code automation engine with a locked human-approval list.
- **Appendix Y — Marketing, Brand, Social Media, PR and Growth Automation.** The campaign and social calendar kept in Equator while Brevo, Adobe Express and social tools send or publish; partnerships, PR, attribution and outcome-based contribution metrics; "autopilot" with human approval of claims, prices and mass sends.
- **Appendix Z — Workforce HRMS, Payroll and Internal Controls.** Full employee lifecycle including work e-mail provisioning; transparent attendance and output-based work measurement (no covert monitoring, NN-35); leave and payroll under Indian labour law on versioned rule packs; authority matrix, maker-checker, separation of duties and anti-fraud controls (NN-36).
- **Appendix AA — Equator Marketplace and Infrabyx Professional Registry.** Three isolated surfaces; a Private Practice Marketplace with labelled, capped sponsored listings (OFF); a consent-based professional registry run as a group shared service; a post-resolution professional chooser for execution, registration and recovery.
- **Appendix AB — Revenue Architecture v3 and Revenue Stream Registry.** 57 switchable streams (RS-01–RS-57) — one-time, subscription, monthly rental, pay-as-you-go, advertising — each with a kill switch, neutrality rating, tax treatment, refund code and Board gate.
- **Appendix AC — Workspace Suites, Open Integrations and Data Portability.** A suite-neutral `WORKSPACE_PORT` (Microsoft 365 first, Google Workspace later), an open-integrations catalogue with systems of record and field mappings, and the export package `EQ-EXPORT-1.0` (folders of Word, Excel and PDF with a manifest; NN-37).
- **Appendix AD — Group Companies and Cross-Functional Operations.** Legal entities, shared services as processing, cross-company grants under a Group Data-Sharing Agreement, secondment and recharges; case and allocation data never shared with Finbyx or Udofin (NN-38).
- **Appendix AE — Engineering Change, Release, Backup and Audit Management.** GitHub branching and protection, change classes and CAB, patch SLAs, backups and restore tests, VAPT, IS audit, internal and external audit, auditor workspace.
- **Appendix AF — Competitive Research v3 (reference).** Jupitice and its ADR Marketplace, institutions' operating and revenue models, the equatoradr.com training site (corrections C1–C20), and dated corrections to Appendices T, H and B.
- **Phases P15–P21.** P15 Configuration Studio and Tenant Settings · P16 Operations Platform (CRM, support, onboarding, customer success) · P17 Marketing, Brand and Growth Automation · P18 Workforce HRMS, Payroll and Internal Controls · P19 Marketplace, Professional Registry and Revenue Stream Registry · P20 Chambers Workspace v3 and Practice HR · P21 Group Operations, Integrations and Portability.
- **Governance records.** Master NN-33–NN-40, cross-file resolutions X-43–X-66, §4.5 data planes and §18 v3 reading order; `02` requirements R-44–R-70, decisions D3-01–D3-44 (D2-14 retained for the institutional directory), eight new counsel questions and the v3 review log; Appendix F §F.10.4 v3 error-code register; Appendix S §6.9 v3 roles; Appendix J §J.9 configurability; corrections to Appendices B, D, G, H, O, Q, T and phases P00, P01, P05, P10, P13.
- **Departmental structure.** Management's message said it would explain the departmental structure but did not. v3.0 therefore ships a **default, fully configurable** department model (D3-06; master §18 item 5) that management can rename, merge or replace without code.

**What v2.1 added (22 October 2026):** Appendix J rebuilt — every one of the 469 open items has a disposition, evidence, residual uncertainty, approver, production gate and recheck trigger (129 closed, 90 provisional, 250 awaiting counsel, vendors, decisions or a regulatory event; 19 launch gates); 355 in-place corrections; Appendix U policy baselines from the old Equa site; Code of Conduct ECC-2026.1 additions; R-41–R-43, D2-28–D2-29; role `neutral_facilitator`.

**What v2.0 added to v1.1:** one specification per dispute type (`verticals/V1–V6`, with separate intake forms for negotiation, mediation and arbitration); Dispute Explorer v2 and the dispute-type plug-in framework (K); DMS, Supreme Court A4 formats, type copies and translation (L); AI Pleadings Studio (M); neutral governance, grades, QAP, Code of Conduct and Private ADR Chambers (N); revenue, plans, billing and settings (O); website copy deck and SEO/GEO (P); privacy, security and certification readiness (Q); case status, publication, execution and registration (R); identity, separate logins and RBAC (S); benchmarks (T); NN-24–NN-32 and X-19–X-42.

**What v1.1 covered (unchanged unless superseded):** six verticals plus SEBI SMART ODR as an optional connector (flag OFF); every mechanism including med-arb and arb-med-arb; Private ADR Chambers, Enterprise API and bulk intake, GRM SaaS, POSH/IC SaaS and the Academy; the fee engine (INR default; USD/EUR/GBP/SGD/AED for international matters; approval-gated rate cards); voice and omnichannel communications, eSign/eStamp, payments and escrow; website remediation.

## 2. Files

Word counts were recomputed by script (`wc -w` on the pack folder) on 26 October 2026 after the v3.2 commit, with the v2, v3, v3.1 and v3.2 addenda included in the phase files and the new P22, content, design, env and review files added (whitespace-separated words; rounded to the nearest 100; tables count). *(v3.2)* The v3.1 count was 1,225,100; the lead re-runs the count at release if any file changes after integration.

| File | Purpose | Words |
|---|---|---|
| `00_README.md` | This guide | 8,400 |
| `01_MASTER_PROMPT.md` | Constitution: product, **NN-01–NN-40**, architecture (incl. §4.0 IPB adoption clause, §4.5 v3 data planes, §4.6 IPB adoption notes and `fut.*` flags), domain model, customisability, fees, integrations, AI (Vidhi), phase plan P00–P22, precedence and cross-file resolutions **X-01–X-70**, management decisions, v2, v3 and v3.2 reading order | 21,200 |
| `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` | Requirements R-01–R-80, decisions D2-01–D2-29, D3-01–D3-66 and IPB-DEV-01–02, assumptions, counsel questions 1–27, dependencies, phase mapping (incl. §7B v3.2), v2, v3.0, v3.1 and v3.2 logs | 15,500 |
| `phases/P00–P14` (15 files) | Build phases; each ends with a **v2 addendum** and a **v3 addendum** (P00, P01, P12 and P13 also a **v3.1 addendum** from Appendix AG; P00, P11, P13 and P14 a **v3.2 addendum** from the IPB), which are part of that phase's scope and exit gate | 222,700 in total |
| `phases/P15_Configuration_Studio_and_Tenant_Settings.md` | Configuration Studio, settings registry and SDK, rule-pack engine (Appendix V); v3.2 addendum: twenty-node settings tree, v3.2 keys | 12,200 |
| `phases/P16_Operations_Platform_CRM_Support_Onboarding.md` | Operations Platform: CRM, support, onboarding, customer success (Appendix X) | 12,600 |
| `phases/P17_Marketing_Brand_and_Growth_Automation.md` | Marketing, brand and growth automation (Appendix Y) | 12,200 |
| `phases/P18_Workforce_HRMS_Payroll_and_Controls.md` | Workforce HRMS, payroll and internal controls (Appendix Z) | 13,800 |
| `phases/P19_Marketplace_Professional_Registry_and_Revenue.md` | Marketplace, professional registry, revenue stream registry (Appendices AA, AB, AF) | 12,700 |
| `phases/P20_Chambers_Workspace_v3_and_Practice_HR.md` | Chambers workspace v3 and practice HR (Appendix W) | 11,100 |
| `phases/P21_Group_Operations_Integrations_and_Portability.md` | Group operations, integrations and portability (Appendices AC, AD) | 13,200 |
| `phases/P22_Vidhi_AI_Employee_and_Knowledge_Notebooks.md` *(v3.2)* | Vidhi AI on the shared kernel: agent → skill mapping with ceilings, EQ-LK locked list, notebooks, RRULE schedules, MCP, surfaces, `vidhi.*` settings (IPB-03) | 8,100 |
| `verticals/V1–V6` (6 files) | FIN, COM, FAM, INS, WRK and INT dispute-type specifications | 159,200 in total |
| `appendices/A–J` | v1 binding specifications: workflows (A), fees (B), screens (C), integrations (D; v3.2 port note), AI and voice (E; §E.0 Vidhi pointer), data model, events and errors (F; §F.9.1 proposed Ecosystem events; v3 and v3.2 registers §F.10.4), legal rules register (G), competitors, GTM and website corrections (H), tests (I), verification log and open items (J; §J.9 configurability; §J.10 v3.2 items) | 221,800 in total (J ≈ 74,100) |
| `appendices/K–U` | v2 and v2.1 binding specifications (Dispute Explorer v2, DMS, Pleadings Studio, neutral governance, revenue and settings, copy deck (P; v3.2 companion-deck note and P-55–P-72), privacy and security (Q; IPB-02 pointer), case status, identity and RBAC — S §6.9 v3 roles — benchmarks, institutional rules (U; §U.14 IPB-05 inserts)) | 246,900 in total |
| `appendices/V_Configuration_Framework_Rule_Engine_and_Settings_Catalogue.md` | Configuration framework (v3.0; §V.4.11 v3.2 key register) | 26,400 |
| `appendices/W_Private_ADR_Chambers_Workspace_v3_and_Practice_HR.md` | Chambers workspace v3 and practice HR (v3.0) | 23,800 |
| `appendices/X_Equator_Operations_Platform_CRM_Support_Customer_Success.md` | Operations Platform (v3.0) | 24,300 |
| `appendices/Y_Marketing_Brand_Social_PR_and_Growth_Automation.md` | Marketing, brand, social, PR and growth automation (v3.0; §Y.0.6 tag management under IPB-04) | 21,500 |
| `appendices/Z_Workforce_HRMS_Payroll_and_Internal_Controls.md` | Workforce HRMS, payroll and internal controls (v3.0) | 23,800 |
| `appendices/AA_Marketplace_and_Professional_Registry.md` | Equator Marketplace and Infrabyx Professional Registry (v3.0) | 21,800 |
| `appendices/AB_Revenue_Architecture_v3_and_Stream_Registry.md` | Revenue architecture and stream registry (v3.0) | 20,100 |
| `appendices/AC_Workspace_Suites_Open_Integrations_and_Data_Portability.md` | Workspace suites, integrations and portability (v3.0) | 19,200 |
| `appendices/AD_Group_Companies_and_Cross_Functional_Operations.md` | Group companies and cross-functional operations (v3.0) | 11,800 |
| `appendices/AE_Engineering_Change_Release_Backup_and_Audit_Management.md` | Engineering change, release, backup and audit (v3.0; v3.2 `cc/*` branches, preview environments, beta programme, release notes) | 23,000 |
| `appendices/AF_Competitive_Research_v3_Jupitice_Institutions_Training.md` | Competitive research v3 (reference, v3.0; §AF.11 website structure review note) | 14,500 |
| `appendices/AG_Information_Architecture_Navigation_Menus_and_Workflow_Patterns.md` | Information architecture, navigation, menus and workflow patterns (v3.1; v3.2 mega-menu rows, twenty-node settings mapping, Ask Vidhi) | 30,800 |
| `content/Equator_Website_Content_v1.0.md` *(v3.2)* | Website content deck: full copy for every standard page, footer, cookie banner, one-liners, FAQ bank, SEO register, image placeholders, policy list | 18,700 |
| `design/UI_UX_Design_Brief_v3.2.md` *(v3.2)* | UI/UX design brief: palette, type, spacing, components, iconography, imagery, dark mode, states, motion, accessibility, do/don't, sample screens, tenant overrides | 3,000 |
| `env/.env.example` · `env/SEED_CREDENTIALS.md` · `env/README.md` *(v3.2)* | Environment template (221 variables), seed personas and credentials (gitignored in the repository), usage guide | 3,700 in total |
| `_review/v3.2_upgrade_review_log.md` *(v3.2)* | Adversarial self-review, state-machine scenarios, ID collision check, fixes | 2,100 |
| **Total** | 71 files (+ `_research/` 5 files, ≈ 50,700) | **≈ 1,330,000** |

Earlier versions stay in their own folders for reference (v1, v2, v2.1, v3.0, v3.1 in `_Archive (older versions)/`); v3.2 supersedes them. A consolidated Word copy (`Equator_Build_Prompt_Pack_v3.2.docx`) is produced separately by the lead for review and sign-off; the v3.1 copy in this folder is superseded *(v3.2)*. Appendix V exceeds the usual appendix length because it holds the full 469-row configurability register.

## 3. How to run the build

1. Create an empty repository and open the coding agent in it.
2. **At the start of every phase session,** *(v3.2)* read `docs/ipb/00_README.md` (and, in the first P00 session, IPB-01, IPB-02, IPB-09 and IPB-11 in full; IPB-03 before P11 or P22; IPB-04, -05, -07 before P13; IPB-08 before P14), then paste `01_MASTER_PROMPT.md`, then `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, then the phase file (including its v2, v3, v3.1 and v3.2 addenda). Attach the appendices and vertical files that the phase cites. Read master §18 before any v3 work, and apply the v3 operating rules (master §0, OP-1–OP-9) and Definition of Done (§12, V-1–V-9) to every v3 story *(v3.1)*.
3. **Phase order (v3.2):** **P00 → P01 → P15 → P02 → … → P14**, then P16–P21 as below, with **P22 after P16** (beside P17–P19; before P21's export gate).
   - **P22** (Vidhi AI Employee and Knowledge Notebooks) needs P11, P15, the P16 `apps/ops` shell and the P13 CMS; soft dependencies with fallbacks: P07 (WhatsApp surface OFF), P09 (enterprise MCP clients), P21 (calendar connectors). *(v3.2)*
   - **P15** starts directly after P01 and runs alongside P02 onwards: every later phase registers its settings in the P15 registry as it builds them (registry before use, D3-11), using the SDK from P15 sprint 1. P15 must be complete before P16–P21 start.
   - P08 runs as six sub-iterations, P08a FIN → P08f INT, each starting with the matching `verticals/V<n>` file.
   - P13 may run in parallel with P08–P11 using a second squad. Mobile work starts in P01 and closes in P12.
   - **P16** (Operations Platform) needs P00, P01, P15 and P05 read models; it ships stated fallbacks where P09, P13, P07, P11, P18 or P21 are not yet done.
   - **P17** (marketing) needs P13, P15 and P16.
   - **P18** (HRMS, payroll, controls) needs P00, P01, P15 and P16; it consumes P05, P09, P10 and P14.
   - **P19** (marketplace, registry, revenue registry) needs P03, P05, P10, P15 and P16.
   - **P20** (chambers v3, practice HR) needs P10, P15, P18 and P19.
   - **P21** (group operations, integrations, portability) runs last: it needs P00–P14 and P15–P18.
   - Each v3 phase has its own exit gate; a v3 phase released after the first go-live re-runs the P14 hardening and go-live checklist for its scope.
4. **Before coding,** the agent writes `docs/phases/PXX-plan.md`, including the five inventories of master §0 step 2 (settings, events, error codes, approval actions, export mapping). It stops at the phase exit gate (§13 of each phase file plus the addenda's acceptance tests) and hands over only when the master §10 hand-off checklist is met *(v3.1)*.
5. **Precedence on conflict** follows master §15 (master and 02 → Appendix G for law → B for fees → F for names and codes → A for states → phase file → other appendices; v3: Appendix V on tiers and keys, the AB registry on whether a stream may be offered, and each v3 appendix on the schema it owns; v3.1: Appendix AG on menus, navigation, the Work Inbox and workflow patterns). The X-resolutions record the conflicts already resolved.
6. **Unverified rules and dependencies:** any feature that depends on a legal rule still marked `UNVERIFIED` or **[VERIFY — open]**, a vendor contract, a Board approval or an unconfirmed fact ships behind a flag that is OFF and names its approver.

**Indicative effort:** 30–36 two-week sprints for P00–P14 with two squads (platform + verticals) plus a growth/website squad. The v3 phase files estimate P15 6 sprints (squad of 8), P16 8 (9), P17 6 (7), P18 10 (9), P19 8 (10), P20 6 (9) and P21 6 (8); several run in parallel once P15 and P16 are done.

### 3.1 v3 squad and sprint plan (P15–P21) *(v3.1)*

Sprint numbers count two-week sprints from the start of P00 (S1). The plan assumes the main track runs P00 S1–S4, P01 S5–S9, P02 S10–S15, P03 and P05 in parallel S16–S20, P10 S21–S25 and P13 S21–S26 (growth squad), with P14 finishing by S36; move the v3 rows by the same amount if the main track slips. Hard gates are the phase files' dependency headers.

| Phase | Squad (size; sub-squads) | Sprints | Starts when (hard gates) | Freeze by end of its sprint 1 (master OP-8) | Exit evidence beyond §13 of the phase |
|---|---|---|---|---|---|
| P15 Configuration Studio | **C** Configuration (8; core 4, Studio UX and catalogue 4) | S10–S15 | P01 exit | Registry SDK (`packages/config`), key-naming rules, scope tree, tier badge component — consumed by P02 onwards | Every main-track key read so far is registered; P16–P21 entry conditions of P15 §13 met |
| (bridge) | **C** as the settings guild | S16–S20 | P15 exit | — | Reviews every main-track settings pull request; builds setting packs and Studio entries for P03, P05, P07; drafts the P16 interface ADR |
| P16 Operations Platform | **O** Operations (9 = squad C + 1 integrations engineer) | S21–S28 | P15 exit **and** P05 read models (P05 exit) | `apps/ops` shell, navigation, notifications, staff directory projection, `ops.crm_*` read views, automation-engine API — consumed by P17, P18, P19 | P14 re-run for the Operations Platform scope; deferred P14 v3 items for X closed |
| P17 Marketing | **O** (7 of 9) | S29–S34 | P13 and P16 exits | `mkt` calendar and audience APIs; `MARKETING_PORT` contract | Brevo activation gate LG-V3-10 evidenced or `mkt.brevo.enabled` stays OFF; marketing export package passes AC §AC.13.13 |
| P18 Workforce, payroll, controls | **W** Workforce (9; People 4, Payroll 3, Controls 2) | S29–S38 | P16 exit | `packages/rules/payroll` and `packages/rules/leave` function signatures; `ctl.approval_requests` API and action codes; `equator.hr.employee.*` events — consumed by P20, P21 | LG-V3-05, -06, -07 and -12 closed before the first live pay run and attendance capture; payroll engine package versioned for P20 |
| P19 Marketplace, registry, revenue | **M** Marketplace (10; Marketplace 4, Registry 3, Revenue and paid visibility 3) | S29–S36 | P03, P05, P10, P15 and P16 exits | `mkp` projection schema and eligibility attributes; `rev` registry API and kill-switch events; `REGISTRY_PORT` contract — consumed by P20, P21 | `NO_PAID_PLACEMENT` and `MKP_SURFACE_ISOLATION` green; LG-V3-02, -03, -04, -09 recorded (features stay OFF until closed) |
| (gap) | **M** | S37–S38 | P19 exit | — | P14 re-run for the P19 scope; P20 discovery and interface ADR (no P20 code before P18 exits) |
| P20 Chambers v3 and practice HR | **M** (8) + payroll domain analyst from **W** (= 9) | S39–S44 | P10, P15, P18 and P19 exits | Practice-page routes and lint profile; chambers settings keys; HR-lite pay-run contract on the P18 engine | Chambers pay run reconciles to the bank file; NN-38 tests show no chambers employee row in `hr`/`pay` |
| P21 Group, integrations, portability | **I** Integrations (8 from **O** after P17; Integrations and Portability 5, Group 3) | S39–S44 | P00–P14, P15, P16, P17 and P18 exits | `xpt` scopes and folder map; `STORAGE_PORT`, `ACCOUNTING_PORT` contracts; `grp` grant API | Export-coverage test (master §12 V-4) green for every scope; group go-live gate (P14 v3 addenda) passed for the first group company |

**Reading the plan.** The critical path is P01 → P02 → P05 → P16 → P18 → P20/P21, about 44 sprints from S1; P19 runs beside P18. Peak load is S29–S36 (squads O, W and M, about 26 people, beside the main-track squads finishing P11–P14); with only two v3 squads, run P19 after P18 and expect about 8 more sprints. Squad O spends S35–S38 on P16–P17 go-live work and the P21 interface ADR before re-forming as squad I.

**Every sprint of a v3 phase** *(v3.1)*: review the settings-registry diff; run the NN suite and the master §12 V-1–V-9 checks; demo one approval round trip and one tenant T-setting change; reconcile the open-items list with the phase's markers; every second sprint, validate a seeded export of each scope touched (Appendix AC §AC.13.13).

**P14 and the v3 phases.** The first P14 run completes only the P14 v3 items whose module exists; the rest go to `docs/phases/P14-deferred.md` and close at the exit of the phase that builds them (master §10).

## 4. Decisions and approvals needed before go-live

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | **Rate cards and fee schedules.** Rate cards are customisable and approval-gated (M-01). The Board approves the default fee schedules (Appendix B) and the plans and one-time products (Appendix O). | Board / CFO | P05, P13 fees and plans pages |
| 2 | **Entity particulars** for Equator Resolution Service Private Limited (M-02): CIN, registered office, GSTIN, DPO, Grievance Officer, Nodal Officer. | Company Secretary | P13, P14, invoices, privacy notices |
| 3 | **Rulebooks:** Equator Rules (arbitration, mediation, conciliation, negotiation), vertical rules, Code of Conduct for neutrals, Institutional Committee charter (majority external) and complaints procedure. | Board / Legal | P03, P04, P08, App. N |
| 4 | **Neutral grading policy** (A/B/C), QAP design and fees, assessor panel, and the published allocation formula (D2-12, D2-13). | Head of Institution | P03, P10 |
| 5 | **Equator ADR Institute (D2-17, D3-38):** confirm its operating entity (the site shows Infrabyx Consultancy (OPC) Pvt Ltd) and correct its public claims (C1–C20, Appendix AF §AF.4.3). The referral card and stream RS-22 stay OFF until then; any referral arrangement is a related-party transaction (s.188; s.177 only where an Audit Committee is required; s.184 disclosure) **[CS to confirm]**. | Company Secretary / Institute | P10, P13, P19 |
| 6 | **UIDAI and DigiLocker:** OVSE registration for Aadhaar offline verification; DigiLocker requester partnership. No bureau pulls at onboarding (D2-06). | CTO / Compliance | P01 |
| 7 | **Counsel opinions** in 02 §5 items 1–15 (s.42A publication consent, AI self-help drafting, s.442 panel mediations, MSMED 2026, Insurance Act intermediary question, "Court" in Chambers names, recovery-agency status). | General Counsel / external counsel | Flags in P06, P08, P10, P13 |
| 8 | **Telecom and calling (M-05):** DLT Principal Entity registration, CPaaS contracts, CLI opinion for Equator's own service numbers; Jio carrier and Haptik RFP (D2-23). | CTO / telecom counsel | P07 |
| 9 | **Pre-suit mediation (M-06):** voluntary pre-suit mediation is live now; mandatory s.12A PIMS stays with the Legal Services Authority until the four gates close. | General Counsel | P08 COM |
| 10 | **Vendor contracts** (candidates, not commitments): ElevenLabs Enterprise (India residency), Sarvam, Exotel/Plivo, Gupshup, MSG91, Leegality, Digio, SignDesk, Surepass, Razorpay, Castler, LiveKit, AWS Bedrock India, OCR and translation providers; v3: Brevo, Adobe Express, social platform access, payroll and accounting tools (Tally/Zoho Books). | CTO / Procurement | P01, P05–P07, P11, P16, P17, P21 |
| 11 | **Policy set** for certification readiness: information security, access control, incident response, vendor risk, retention, privacy notices, cookie policy. | Company Secretary / CISO | P14, App. Q |
| 12 | **Live website corrections:** apply Appendix H §5 and the Appendix P replacement copy now, independent of the build. | Marketing + Legal | Immediate |
| 13 | **Open items:** work through Appendix J §J.5.3, starting with the 19 launch gates (§J.5.2) and the 12 v3 launch gates LG-V3-01–12 (§J.9.1) and the v3.1 residuals V31-OI-01–24 (§J.9.3); every v1–v2 item is also classified by configurability in Appendix V §V.3, and v3 open items join the same register (Appendix J §J.9 rules 5–6). | Legal counsel / tax adviser / CTO | Feature flags |
| 14 | **Confirm the Microsoft 365 SKU (D3-04).** Management named "Business Starter", which is not a Microsoft plan; the design works on Business Basic. Confirm the plan held and decide Business Premium (or add-ons) for console, Tier-High, sealed and finance users (D3-40). | Company Secretary | P18 work e-mail provisioning, P21 workspace connection |
| 15 | **Board approval of revenue streams and paid placement.** The stream registry waves, prices and Board thresholds (D3-39; Appendix AB) and the sponsored-listing stream RS-19 with its equal rate card (D3-37) — `marketplace.paid_placement` stays OFF until the Board approves and counsel signs off (NN-34). | Board / CFO / counsel | P19, P13 pricing and marketplace pages |
| 16 | **Counsel on the professional directory (NN-39):** BCI r.36 and its Schedule, *Sulekha.com v P.N. Vignesh* (SLP (C) 25794/2024), ICAI/ICSI/ICMAI aggregator and referral bars, the Post-Resolution Advocate Panel terms; the E-Commerce (Amendment) Rules 2026 text. `directory.public_professionals` and `postres.advocate_panel` stay OFF. | General Counsel / external counsel | P19 public search and panel, P06 chooser |
| 17 | **Group Data-Sharing Agreement and registry owner.** The Board designates the registry owner entity (D3-05); GDSAs, intra-group processing agreements and service agreements are signed with s.188 status recorded; the shareholding chain and related-party status (s.2(76)) are confirmed. | Board / Company Secretary | P19 registry go-live, P21 group go-live |
| 18 | **Payroll parameters sign-off.** Every `NOT_CONFIRMED` or `SECONDARY_ONLY` parameter in Appendix Z §Z.2.4–§Z.2.5, and the remote-employee PT/LWF opinion (D3-31). | Payroll Compliance Officer with CA / counsel | First live pay run (P18), chambers pay runs (P20) |
| 19 | **Employee monitoring notice (NN-35).** Issue the notice for attendance, login/logoff and work measurement (quoting the enacted DPDP s.7(i) text); approve the DPIA before individual ROI views are enabled (D3-33). | DPO / HR head | P18 attendance capture |
| 20 | **GitHub Enterprise Cloud (D3-09).** Licence GHEC (with Secret Protection and Code Security) for environment protection on private repositories, or record the `ReleaseApprovalWorkflow` compensating control. | CTO / Board | P00 production deployments |
| 21 | **Delegation of Financial Powers (D3-34)** and the **department model (D3-06):** the Board approves the authority-matrix values; management confirms or replaces the default departments. | Board / management | P16 workspaces, P18 go-live |
| 22 *(v3.2)* | **Investors page publication (D3-55; V32-OI-01).** Whether to publish `/investors` (toggle `platform.web.investors.enabled`, OFF), which documents are login-gated with an NDA flag, and counsel's wording of the locked disclaimer under Companies Act 2013 s.42 and the Prospectus and Allotment Rules r.14 (`02` counsel question 24). | Board / Company Secretary / counsel | P13 FR-P13-V32-02; LG-V3-14 |
| 23 *(v3.2)* | **Vidhi naming confirmed for Equator (D3-50; V32-OI-02).** The AI employee is "Vidhi" in the institution tenant; display-name override only on white-label plans. | Owner | P22; P11 |
| 24 *(v3.2)* | **Blog user-post programme (D3-55; V32-OI-03; LG-V3-16).** Approve the programme for empanelled neutrals, partner-university academics and invited practitioners; name the editorial board; counsel on question 27. | Owner / General Counsel | P13 FR-P13-V32-03 |
| 25 *(v3.2)* | **Alternative adapters for Tier-0 ports (D3-49; IPB README §7 item 8).** Contract one alternative adapter per Tier-0 port (identity, storage, payments, email, LLM, video, eSign) so that it runs live in CI; decide the tag-management option (V32-OI-09) and the image-generation provider (V32-OI-05). | CTO / Procurement / Owner | P00 FR-P00-V32-04; P13 FR-P13-V32-10 |

## 5. Requirement coverage map

The full map with status is in `02` §2 (R-01–R-71).

**Briefs of 19–22 October 2026 (v1–v2.1)**

| Area | Where addressed |
|---|---|
| Six dispute types, subtypes, separate law, rules, process, forms per mechanism, dropdowns, integrations and APIs | V1–V6; Master §1.2, §5.2; P08 (P08a–f); App. K §4 |
| Add further dispute types later | App. K §6 plug-in framework |
| Arbitration, mediation, med-arb, negotiation, conciliation; pre-litigation mediation | Master §1.3, §5.3; P04; App. A; App. K §5; V1–V6 §8 |
| Dispute Explorer, ADR suitability, criminal exclusion | App. K §1–§3; NN-24 |
| AI drafting of claims, defences and affidavits; pluggable AI | App. M; NN-25; P11 |
| Separate logins, onboarding APIs, representatives, dashboards, RBAC | App. S; P01; NN-14, NN-27 |
| DMS, A4 Supreme Court format, type copies, translation | App. L; NN-32 |
| Case status, publication with consent, execution and registration | App. R; NN-26 |
| Neutral onboarding, directory, grades, QAP, Code of Conduct, complaints, ratings, allocation; Private ADR Chambers SaaS | App. N; P03, P10; NN-28 |
| Training providers, Equator ADR Institute, IMI QAP | App. N §9–§10; App. T §3; App. AF §AF.4; D2-17, D3-38 |
| Competitors, international institutions, Reliance Jio AI | App. T; App. H; App. AF |
| Revenue streams, subscriptions, billing and membership settings | App. O; App. AB; NN-29 |
| Privacy laws; PCI DSS, SOC 2, ISO readiness | App. Q; NN-30, NN-31 |
| Copywriting, SEO/GEO/AI search; clean minimal UI | App. P; App. C |
| Fees in INR with foreign currency; approval-gated rate cards | Master §7; App. B; P05; V6 |
| GRM SaaS, POSH/IC SaaS, Enterprise API, Academy | P09, P10 |
| SEBI optional; Equator places its own calls; pre-suit mediation | Master §1.2, NN-12, §16 |
| Policies from the old Equa site; research on every open item | App. U; App. J §J.5–§J.9 |

**Brief of 23 October 2026 (v3.0)**

| # | Brief item | Where addressed |
|---|---|---|
| 1 | Open, interim and externally dependent items configurable through settings; routine changes without a super admin; legally sensitive values governed | NN-33; App. V §V.1–§V.3 (469 items classified); P15; D3-10–D3-14; App. J §J.9 |
| 2 | Complete settings for every user type; extra customisation and website pages for Private ADR Chambers and independent neutrals; staff and case-manager management; small HR module with salary records and disbursal | App. V §V.4; App. W §W.3–§W.8 (pages, settings, staff), §W.6 (practice HR); P20; D3-15–D3-19 |
| 3 | Separate Operations Platform for operations, service delivery, after-sales, onboarding, customer success, marketing, brand, social, PR, collaborations, CRM, grievances and tickets; open to Brevo and other tools with integration and migration | D3-02; App. X (P16); App. Y (P17); App. AC §AC.11–§AC.14; NN-40; X-50–X-55 |
| 4 | Performance appraisal and full employee lifecycle (incl. e-mail IDs); decentralised decisions, maker-checker, anti-corruption, anti-embezzlement; leave and salary under Indian labour law; remote work; login/logoff, work measurement; case managers at home | App. Z; P18; NN-35, NN-36; D3-30–D3-34; X-56–X-58 |
| 5 | Microsoft 365 (SKU to confirm) with Teams and SharePoint, Google Workspace later; documents open in MS Office; downloads as self-explanatory folders of Word, Excel and PDF | App. AC; P21; D3-04, D3-40, D3-41 (`EQ-EXPORT-1.0`); NN-37; master §18 item 6 |
| 6 | Switchable, customisable revenue streams (one-time, subscription, monthly rental, pay-as-you-go, advertising); paid preference placement for private-practice neutrals | App. AB (RS-01–RS-57, kill switches); App. AA §AA.10; P19; NN-34; D3-01, D3-37, D3-39; X-61, X-62 |
| 7 | "Autopilot" business automation; full marketing architecture with calendar inside Equator | App. X §X.12 (engine, human-approval list); App. Y §Y.7; P16, P17; D3-23, D3-25–D3-29 |
| 8 | Empanelled advocates and an all-India directory of advocates and professionals shared across the group (execution, registration, NPA recovery suits) | App. AA §AA.11–§AA.12; NN-39; D3-05, D3-36; X-60; App. AD |
| 9 | Change and patch management on GitHub branches; backups, VAPT, IS audit, internal and external audit | App. AE; D3-09, D3-43, D3-44; X-65, X-66; P00 FR-P00-08 note; Q SC-11 |
| 10 | Departmental structure (to be explained by management — not received) | D3-06 default, fully configurable model; master §18 item 5; FR-P18-02; App. X §X.3 |
| 11 | Multi-company: staff cross-functional for Finbyx and Udofin; dashboards, content and data shareable under controls | App. AD; P21; NN-38; D3-42; X-64; App. D §D.7 note |
| 12 | Jupitice and its ADR Marketplace researched; an Equator Marketplace as a revenue stream | App. AF; App. AA; P19; D3-35; corrections to T, H and B |
| 13 | ChatGPT "Expanded Prompt" (configurability classes, settings and permission matrix, Operations Platform, CRM, marketing, workforce, maker-checker, portable records and manifest, revenue and marketplace economics, opt-in directory, competitive research, autopilot with human approval, multi-company, change and audit, staged delivery) | Followed where consistent with D3-01–D3-09: V, X, Y, Z, AA–AF; App. S §6.9; master §10 staged order |

**Instruction of 24 October 2026 (v3.1)**

| # | Instruction | Where addressed |
|---|---|---|
| 14 | "Improvise the logics, workflows, options, menu, etc. so that I can build a better software, wherever possible. Review and fix the errors/mistakes." (R-11, R-29, R-71, R-72) | App. AG (navigation, menus, Work Inbox, search, palette, dashboards, workflow patterns); every file's *(v3.1)* changes; master §0 OP-1–OP-9, §10, §12 V-1–V-9; §3 of this guide; `02` §8B |

**Brief of 26 October 2026 (v3.2 — IPB adoption)** *(v3.2)*

| # | Brief item (PRODUCT_UPGRADE_BRIEF §2 and the Equator deltas) | Where addressed |
|---|---|---|
| 15 | IPB adoption clause, Node 24.22.1, PostgreSQL only, ports, shared packages, Docker/Helm/Terraform per cloud, precedence | Master §4.0, §4.1, §4.2, §4.4, §4.6, §15; P00 v3.2 addendum; D3-48, D3-49; X-67 |
| 16 | Vidhi AI on the shared kernel; agent mapping; notebooks; schedules; MCP; `vidhi.*` settings; NN-01 preserved | P22; P11 header and v3.2 addendum; App. E §E.0; master §9; App. V §V.4.11; D3-50, D3-61; X-69 |
| 17 | "i" help registry with CI lint and regulatory-reference panel; ≥ 400 terms | P13 FR-P13-V32-13; App. AG §AG.8.5; X-70; D3-60 |
| 18 | Public website and Studio: standard pages, blog toggle/bulk/user posts, vlog, Resources library, CMP, footer, Brand Studio `app_name`, Pricing Studio, Investors toggle, marketing tooling, feedback widget | `content/Equator_Website_Content_v1.0.md`; P13 FR-P13-V32-01…11; App. P §3.1; App. AG §AG.2.1; App. Y §Y.0.6; D3-54, D3-55, D3-57, D3-62 |
| 19 | Policies (IPB-05 inserts and footer list) | App. U §U.14 (U-16–U-25); content deck §34; D3-66 |
| 20 | Accessibility (hearing-centric journeys, low literacy) | Design brief §11; P04/P12 (unchanged); master §4.6 IPB-06 row |
| 21 | Settings tree (twenty nodes) | App. AG §AG.3.1 mapping; P15 FR-P15-V32-01; D3-58 |
| 22 | Vendor Assurance Room mirror | P14 FR-P14-V32-01…03; App. Q §0; D3-56 |
| 23 | Engineering governance (previews, `cc/*`, beta, release notes, patch SLAs) | App. AE §AE.2.3, §AE.3.1; P00 FR-P00-V32-08; P14 FR-P14-V32-06; D3-64 |
| 24 | API standard and proposed Ecosystem events | App. F §F.9.1 (five proposed events for the Ecosystem agent) |
| 25 | Environment and seeds | `env/`; P00 FR-P00-V32-06, -07; D3-51 |
| 26 | UI/UX design brief | `design/UI_UX_Design_Brief_v3.2.md`; D3-58 |
| 27 | Feedback, tutorials, What's new, Cmd+K PII refusal, WhatsApp super-admin toggle, consent-gated pixels, `brand_pack` | P13 FR-P13-V32-10, -11, -14; App. AG §AG.5.4; `env/.env.example` `MSG_WHATSAPP_ENABLED_SUPERADMIN`; D3-57, D3-62, D3-63 |
| 28 | Future-ready flags | Master §4.6 table; App. V §V.4.11; D3-65 |
| 29 | Claude artefacts | Master §4.6 IPB-13 row |
| 30 | Decision log, README, open items, review | `02` §3A D3-48–D3-66, §7B, §8C; this guide; App. J §J.10; `_review/v3.2_upgrade_review_log.md` |

## 6. Key judgments embedded (read before approving)

**v3.0 judgments**

- **Paid placement has hard limits (NN-34).** Sponsored listings exist only on the Private Practice Marketplace, only for non-advocate private-practice neutrals and chambers, in a separate block labelled "Sponsored — paid placement. Does not affect Equator appointments.", at most 2 per page and 20% of results, at one equal rate card, with published ranking rules. They never touch the institutional directory, allocation, eligibility, Quality Index, grading or conflict checks. The flag is OFF until the Board approves and counsel signs off. Advocates, CAs, CSs and CMAs are never sold placement, ratings or featured labels and receive no referral reward of any kind (X-62).
- **The advocate directory is consent-based and OFF in public (NN-39).** Listings are opt-in with per-field display consent, verified and removable; nothing is scraped or bulk-imported from Bar Council rolls or institute directories; advocate fields follow the BCI r.36 Schedule; public advocate search stays OFF pending counsel and the Supreme Court appeal (SLP (C) 25794/2024). The party always chooses the professional.
- **No covert monitoring (NN-35).** Attendance and work measurement are disclosed, purpose-limited and outcome-based; keystroke logging, webcam capture, screenshots of personal devices and undisclosed device monitoring are locked OFF; employees see and can dispute their own data.
- **Maker-checker everywhere money or authority moves (NN-36).** No single person can create a payee, change bank details, approve and execute a payment and reconcile it; bank changes have a cooling-off period and out-of-band confirmation; the authority matrix is a Board proposal; ledger, billing and payroll keep an un-disableable edit log.
- **Portability is free at exit (NN-37).** Every organisation, user and group company can export everything as folders of DOCX/XLSX/PDF (PDF/A for final records) with a README and a checksummed manifest, within OneDrive and Windows path limits.
- **Group boundaries (NN-38).** Group membership grants no data access; cross-company access needs a purpose-bound, time-limited grant under a Group Data-Sharing Agreement; case and allocation data are never shared with Finbyx or Udofin, which receive a lender's case events only as that lender's processor (X-64).
- **Microsoft 365 Business Basic caveat (D3-04).** "Business Starter" is not a Microsoft plan; the design works on Business Basic, where Office desktop apps are not included (web and mobile only), so exports are tested in Office for the web. Keycloak, not the Microsoft plan, controls access to every Equator console, and Microsoft 365 is never a system of record. Equator-administered hearings never run on Teams.
- **Configuration never weakens the law (NN-33).** Statutory floors and NN rules are locked; legal parameters are governed with citations, maker-checker and a configured fallback; tenants change routine settings themselves.
- **Training stays separate (D3-38).** Equator books ₹0 from the training site unless the Board approves an arm's-length related-party arrangement; training never affects empanelment, grade, allocation or the EQAP fee.

**Judgments carried from v1–v2.1**

- **No legal advice.** AI never advises, predicts or values a party's case (NN-01). The Dispute Explorer reports suitability, pathways, cost, time, limitation flags and free-forum options.
- **AI Pleadings Studio is self-help** on identical terms to both sides, grounded only in the party's documents and a verified corpus (NN-25, D2-07).
- **Criminal matters are excluded** (NN-24); where the law allows, only the civil dimension is settled.
- **Publication of awards and settlements** needs every party's consent after the outcome; arbitral publication stays OFF until counsel rules on s.42A (NN-26, X-35).
- **Aadhaar** only through offline verification; no bureau pulls at onboarding (D2-06).
- **Pre-suit mediation (M-06)** is voluntary; Equator never claims to satisfy Commercial Courts Act s.12A until the four gates close.
- **Lender arbitration** is built to survive challenge after *CORE* (2024) and *Bhadra* (2026).
- **Mediation Act 2023** statutory mode stays behind a flag; the Singapore Convention is signed, not ratified, so consent-award conversion is offered.
- **IBC and in-rem matters** are never decided by Equator (D2-02).
- **Neutral grades** follow management's definition with a competence gate; allocation rules are published; the institutional directory has no paid listings and no outcome statistics (NN-28).
- **Honest pricing:** GST-inclusive prices, all 13 dark patterns linted, cancellation as easy as sign-up (NN-18, NN-29).
- **Certification readiness, not certification** (NN-17, NN-31).
- **Settlement money never passes through Equator's merchant account** (NN-13).
- **POSH, health and family-safety data are sealed** (NN-07).

## 7. Completion checklist

**Complete in this pack (specified and cross-checked)**

- [x] Six vertical specifications V1–V6; Appendices K–U; v2 addenda in every phase file
- [x] Appendices V–AF and phases P15–P21 (v3.0), each reviewed independently (RVA–RVE, about 190 fixes) and integrated (I1 new files; I2 existing files)
- [x] Master NN-33–NN-40, X-43–X-66, §4.5 data planes, §10 phases P15–P21, §18 v3 reading order
- [x] `02` R-44–R-70, D3-01–D3-44, D2-14 amendment, counsel questions 16–23, v3 phase mapping and review log
- [x] Appendix F §F.10.4 v3 error-code register (extracted by script from the defining appendices) and v3 event contexts; Appendix S §6.9 v3 roles and permissions; Appendix J §J.9 configurability summary
- [x] Corrections applied: e-commerce TDS threshold (G LR-TAX-007, B §B.10, P05); advocate referral credits removed (O, B, P01, P10, P13, S; X-54/X-62); P13 mini-CRM superseded (X-51); `growth.*` → `mkt.*` flag aliases (X-55); Q SC-11 patch-SLA ceilings (X-66); P00 GitHub plan note (D3-09) and port count; D ports, `bank_file` adapter, `CrmPortV3` and X-64 note; Appendix AF corrections to T, H and B that rest on dated sources or binding v3 rules
- [x] v3 addenda appended to P00–P14 from the appendices' phase-addenda sections (by the lead, by script)
- [x] v3.1 review-and-improve pass on every file (24 October 2026; R-71, R-72; logs `LOG_<id>.md` in the build archive) and integration of every log's cross-file requests (logs `INTEG_<id>.md`); Appendix AG added; Appendix F registers every v3.1 code and event (script check)
- [x] *(v3.2)* IPB v1.0 adopted: master §4.0, §4.6; P22; v3.2 addenda to P00, P11, P13, P14, P15; content deck, design brief, env and seed files; D3-48–D3-66, R-73–R-80, X-67–X-70; Appendix F events #186–#189 and v3.2 codes; Appendix J §J.10; `_review/v3.2_upgrade_review_log.md`. Follow-ups for the lead: regenerate the consolidated `.docx`; re-run the screen and role extraction so Appendix C §B.1 and Appendix S §6.9 pick up SCR-P13-65…74, SCR-P14-20…22, SCR-P22-01…10, `content_editor` and `AGT_VIDHI`

**Depends on vendors or registrations** (flags OFF until contracted or registered)

- [ ] UIDAI OVSE; DigiLocker partner; MCA/KYB aggregator
- [ ] DLT/telecom: CPaaS, Jio carrier, CLI declarations; ElevenLabs India residency; Jio Haptik RFP
- [ ] eSign/eStamp providers by state; payment gateway (Standard Checkout, Route) and bank escrow
- [ ] LLM in India (Bedrock India) for case content; OCR and translation providers meeting the residency rules
- [ ] Independent assessors: PCI DSS ASV scans and SAQ A attestation; SOC 2 auditor; ISO 27001/27701 certification body
- [ ] v3: Microsoft 365 SKU confirmed; Brevo account and DPA; social platform API access; GitHub Enterprise Cloud; payroll and accounting tool exchange formats
- [ ] *(v3.2)* One alternative adapter live in CI per Tier-0 port; Gupshup BSP contract before the Vidhi WhatsApp surface; OH14.6 live before the Vendor Assurance Room mirror; eCourts API terms (`fut.ecourts-api`); SEBI SMART ODR 2.0 final circular (`fut.sebi-odr-v2`)

**Needs qualified counsel, Board or management sign-off before launch**

- [ ] Counsel questions in `02` §5 (items 1–23) and Appendix J
- [ ] Every Legal Rules Register row marked `UNVERIFIED` (including the v3 rows in Appendix G §G.7) and every open item in Appendix J §J.5.3 (19 launch gates in §J.5.2) and §J.9 (12 v3 launch gates in §J.9.1)
- [ ] Board and counsel approval of the policy set in Appendix U before publication
- [ ] Rulebooks, Code of Conduct, Committee charter, grading policy, fee schedules and plans (§4 items 1–4)
- [ ] Institute entity, corrections C1–C20 and related-party approvals (§4 item 5)
- [ ] Policy documents for certification readiness (§4 item 11)
- [ ] v3: revenue streams and sponsored listings (§4 item 15); directory counsel (item 16); registry owner and GDSA (item 17); payroll parameters (item 18); employee monitoring notice (item 19); authority matrix and departments (item 21)
- [ ] v3.1 residual decisions V31-OI-01–24 (Appendix J §J.9.3; items 04, 05 and 14 gate their scope)
- [ ] *(v3.2)* v3.2 open items V32-OI-01–18 and launch gates LG-V3-13–16 (Appendix J §J.10); owner decisions §4 items 22–25; counsel questions 24–27 (`02` §5); the ten IPB-05 policy instances U-16–U-25 approved by counsel before publication

## 8. Not in this pack

- Legal opinions (the pack lists the questions).
- Signed vendor contracts and the Group Data-Sharing Agreements.
- The policy documents management will prepare, including the employee monitoring notice.
- Final rulebook text and the Delegation of Financial Powers approved by the Board.
- Management's own departmental structure (a configurable default is used, D3-06).
- Translated copy beyond the English and Hindi samples given (the translation workflow is specified).
