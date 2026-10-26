# `v1.1 supplements/` — Infrabyx Operations Hub v1.1 (26 October 2026)

Companions to `Infrabyx_Operations_Hub_Master_Prompt_ClaudeCode_v1.1.md` and `Infrabyx_Operations_Hub_Phase_Runbook_v1.1.md` in the parent folder. Commit this folder to the repository as `docs/supplements/` (except `env/SEED_CREDENTIALS.md`, which is never committed). Earlier versions of the master prompt and runbook are archived in `Earlier versions/` and are not changed.

## What changed in v1.1 (summary; the full list is under the master prompt header)

IPB v1.0 adopted (adoption clause, precedence rule, Node.js 24.22.1, PostgreSQL only, ports, Vidhi kernel, shared packages); product-scope segregation (IPB-D-12) with `product_scope` on every scoped record; HR expansion (OH10.10–OH10.15); deep Microsoft 365 integration (OH12.9); four new modules and phases — OH15 Projects and Work OS (O14), OH16 Knowledge Hub and Vidhi AI (O15), OH17 Marketing, Brand, Media and Meta (O16), OH18 Group website, CMS, Vendor Assurance publishing, feedback and tutorials (O17); Parts 4.13–4.14, 6.2A, 7.7; Appendix B decisions 20–32 with the IPB decision log; Appendix F revision log and adversarial self-review; runbook blocks for the new and expanded phases; this supplements folder.

## Files

| Path | Purpose | Words (approx.) |
|---|---|---|
| `../Infrabyx_Operations_Hub_Master_Prompt_ClaudeCode_v1.1.md` | Master build prompt (Parts 1–10, Appendices A–F, Sources); 18 modules, phases O0–O17 and OP | 89,800 (v1.0: 57,800) |
| `../Infrabyx_Operations_Hub_Phase_Runbook_v1.1.md` | Ready-to-paste session prompts and review gates for every phase, utility prompts, progress tracker | 19,000 (v1.0: 12,400) |
| `env/.env.example` | Annotated environment template, 225 variables (IPB-11 common set plus `OH_*` keys) | — |
| `env/SEED_CREDENTIALS.md` | Lead-issued seed personas (11) with product scopes; service accounts; production-refusal and first-login rules. **Never commit.** | — |
| `env/README.md` | How to use the env and seed files; guard-rails; owner actions | 900 |
| `design/UI_UX_Design_Brief_v1.1.md` | Palette (charcoal `#1F2937`, electric blue `#2563EB`), Inter, spacing, components, iconography, image placeholders, dark mode, accessibility, sample screens, do and don't, tenant override envelope | 3,300 |
| `content/OpsHub_Website_Content_v1.0.md` | Copy for the lean group site: every standard page, footer, cookie texts, 34 one-liners, 44 FAQs, SEO titles and descriptions, placeholder list, open items | 6,200 |
| `phases/Phase_O14_Projects_and_Work_OS.md` | Phase file: card, module OH15, instruction, build notes, API, settings, events, help keys, Gherkin, exit gate, DDL, screens, risks | 6,100 |
| `phases/Phase_O15_Knowledge_Hub_and_Vidhi_AI.md` | Phase file for OH16 | 6,100 |
| `phases/Phase_O16_Marketing_Brand_Media_and_Meta.md` | Phase file for OH17 | 6,300 |
| `phases/Phase_O17_Group_Website_CMS_and_Vendor_Assurance.md` | Phase file for OH18 | 7,200 |

## Run order (v1.1)

O0 → O1 → O2 → O3 → O4 → O5 → O6 → O7 → O8 → O9 (+ v1.1 addendum) → O10 → O11 (+ v1.1 addendum) → O12 → O14 → O15 → O16 → O17 → OP → O13. The first session reads `docs/ipb/00_README.md`, then IPB-01, IPB-02, IPB-09 and IPB-11 in full. `mkt.meta.enabled` and `ai.mcp.server_enabled` stay off until OP.

## Decisions needed from the owner (new in v1.1; Appendix B 20–32)

| # | Decision | Blocks |
|---|---|---|
| 20 | Product-scope assignments at launch; product heads per scope; entity status of LawDocs Trainings and Shikargah Hospitality | O2 seeds, Part 3.3A |
| 21 | Payroll engine mode (in-house or provider) | O9 addendum (OH10.13) |
| 22 | Remote-work operating model inputs | O9 addendum (OH10.10) |
| 23 | Intern programme: stipend bands, certificate wording, EPF/ESI position | O9 addendum (OH10.11) |
| 24 | WhatsApp BSP or Meta Cloud API; Meta verification entity; whether to enable in year one | O16 (OH17.3) |
| 25 | Attendance sources per office; geofence offered or not; shifts | O9 addendum (OH10.12) |
| 26 | Expense policy | O9 addendum (OH10.14) |
| 27 | Tag management adapter and analytics adapter | O16 (OH17.6), O17 CMP |
| 28 | Image-generation provider and synthetic-media rules | O16 (OH17.5) |
| 29 | Group website scope, brand packs for TRN and HSP, blog and Investors toggles, Hindi timing | O17 (OH18.1) |
| 30 | Entity particulars and officers for policies and footer; counsel for IPB-05 review | O17 (OH18.3) |
| 31 | Vendor Assurance cadences, gating, roles, NDA text | O17 (OH18.4) |
| 32 | Microsoft 365 plan held; deep-integration consents | O11 addendum (OH12.9) |

## Coverage against the brief (§2 items 1–23)

Header and what-changed (1) · adoption clause and stack (2) · precedence (3) · new phase content with FR-IDs, screens, settings, events, errors, Gherkin, exit gates (4) · decision log IPB-D-01…12 and `IPB-DEV` register (5) · Vidhi floor with 16 skills, schedules, notebooks, MCP, `vidhi.*` keys (6) · `hlp.oh.<module>.<term>` registry and seed targets (7) · public site, Studio, blog toggle, resources, CMP, footer, Brand and Pricing Studio, Investors toggle, marketing tooling, feedback widget (8) · IPB-05 inserts and footer policy list (9) · accessibility journeys incl. hearing and low literacy (10) · settings-tree mapping (11) · Vendor Assurance Room as system of record (12) · engineering governance (13) · API standard and proposed events (14) · env and seeds (15) · design brief (16) · website content deck (17) · feedback, tutorials, What's new, Cmd+K, WhatsApp toggle, GTM/UTM/pixels, brand pack (18) · `fut.*` flags (19) · Claude artefacts (20) · runbook (21) · this README (22) · cross-pollinated features (23).
