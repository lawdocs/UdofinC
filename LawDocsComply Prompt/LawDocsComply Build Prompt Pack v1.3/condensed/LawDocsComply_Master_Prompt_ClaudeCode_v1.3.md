# LawDocsComply — condensed Master Prompt ClaudeCode v1.3 (26 October 2026)

> **How to read this edition.** This condensed edition is the v1.2 edition carried forward unchanged, preceded by the v1.3 changes. The pack of record is the full `LawDocsComply Build Prompt Pack v1.3` folder; where this condensed text and the full pack differ, the full pack wins. Read `docs/ipb/00_README.md` (Infrabyx Platform Baseline Standard v1.0) before any session.

## v1.3 — IPB adoption clause

> **Infrabyx Platform Baseline Standard (IPB) v1.0 applies.** This product adopts IPB-01 to IPB-13 (`docs/ipb/`) in full. Where this pack and the IPB differ, this pack may only be stricter; any other difference is an `IPB-DEV-nn` entry in the decision log. Runtime is Node.js 24.22.1 (IPB-D-01). All external services sit behind IPB-01 ports with at least two adapters (IPB-D-02). The AI employee is Vidhi AI on the shared kernel (IPB-D-03). The public website, super-admin Studio, blog, resources, cookie consent, footer and standard pages follow IPB-04; policies follow IPB-05; accessibility IPB-06; settings tree and "i" help IPB-07; vendor assurance room IPB-08; engineering governance IPB-09; APIs and events IPB-10; environment and seeds IPB-11 (super admin `rjnprajapati@gmail.com`; seeds never run in production); future-readiness flags IPB-12. Product-specific additions are listed in the product's "IPB adoption notes" section.

## v1.3 — What changed

> **What v1.3 changes (pack lead instruction of 26 October 2026: adopt the Infrabyx Platform Baseline Standard v1.0 across every product pack; LawDocsComply audit findings applied).** *(v1.3)*
>
> 1. **IPB adoption clause** (§5, verbatim from `docs/ipb/00_README.md` §3) — LDC inherits IPB-01…13 by reference and records only what it does differently (`02` §2.6: D-59–D-76; deviations `IPB-DEV-01`, `IPB-DEV-02`). Precedence becomes master → **IPB** → Ecosystem Spec v1.2 → phase files → appendices (§18, X-67).
> 2. **Stack pinned:** Node.js **24.22.1** (IPB-D-01; replaces "24 LTS [VERIFY]"); PostgreSQL the only engine; AWS Mumbai/Hyderabad regional cells retained; Supabase database-only in non-production retained (X-05 unchanged); every vendor behind an IPB-01 port with ≥ 2 adapters; `packages/vidhi`, `packages/cms`, `packages/brand`, `packages/hlp`, `packages/trust`, `packages/feedback` added as shared packages (§5.2, X-68, X-69).
> 3. **Vidhi AI on the shared kernel (IPB-03):** the 17 role agents VA-01…VA-17, RRULE schedules, missions, evidence-based promotion/demotion, notebooks and `ldc-mcp` are mapped one-to-one onto `packages/vidhi` (Appendix K §K.25); the `LlmProvider` port, data-class router and model registry gain OpenAI/Azure OpenAI (Central India), Gemini (asia-south1), Grok, Sarvam/Bhashini and `IMAGE_GEN_PORT` adapters behind flags, with `vidhi.*` settings keys and the product capability floor (P17 §4Y).
> 4. **Public website and super-admin Studio (IPB-04):** the existing headless CMS (P23 §4C) is extended, not replaced — **Brand Studio for the public site** (theme, logo/favicon, `brand.app_name`, host map), vlog, blog toggle + bulk Word import (LawDocs `DocxImportWorkflow` pattern) + user posts with moderation, **Resources library**, Team and Leadership pages, **Investors page (toggle, default OFF)**, social links in the footer (FR-P23-12 amended), feedback widget and idea board (IMP-142 absorbed), `TAG_MANAGER_PORT` option, Pricing Studio alignment (P23 §4V–§4W).
> 5. **Legal policies drafted:** new **Appendix AD** holds the review-ready LDC instances of IPB-05 Templates 1–13 and 15–18 (Template 14 not adopted), with the LDC parameter block, product inserts and counsel checklists — owner decision #11 moves from "policy set to be written" to "approve drafts for counsel review" (D-71).
> 6. **Settings tree (IPB-07):** Appendix C §C.3.6 is mapped to the binding 20-node tree (table IPB node → LDC section); nodes added: Accessibility, Tutorials & help, Feedback, What's new, AI & Vidhi (naming), Security & trust, Storage & data, Audit trails, Appearance (P02 §4S; Appendix C §C.3.6A; Appendix U §U.15).
> 7. **"i" registry (P23 §4H)** confirmed as the group seed; key format `hlp.<module>.<term>` with CI lint and a regulatory-reference panel; LDC's law register is the `LAW_REGISTER_PORT` provider for all six products (IPB-04 §04.7, IPB-05, IPB-07).
> 8. **Accessibility (IPB-06):** dyslexia-friendly font option and explicit captions/live captions/visual alerts for every tutorial video and recorded meeting (P23 §4L amended; FR-P23-230–232).
> 9. **Vendor Assurance Room (IPB-08):** `SCR-ENG-22` Security & trust and the Trust Centre become the LDC mirror of OH14.6 with cadenced document types, tenant downloads, evidence packs and auditor grants — core value for RE tenants (P24 §4M; D-75).
> 10. **Engineering governance (IPB-09):** per-PR preview environments, Claude Code branch convention `cc/<phase>-<slug>`, tenant beta programme, release-notes pipeline and patch SLAs aligned (P24 §4M).
> 11. **API and events (IPB-10):** `/v1` conventions confirmed; LDC lists the ten IPB-10 proposed Ecosystem events and the two IPB-05 policy events it produces or consumes, registered in Ecosystem Spec v1.2 (P18 §4Y; §19).
> 12. **Environment and seeds (IPB-11):** new `env/.env.example` (LDC-specific, 161 annotated variables), `env/SEED_CREDENTIALS.md` (lead-supplied credentials; production refuses seeds; first-login rotation) and `env/README.md`; NN-61.
> 13. **Design brief:** new `design/UI_UX_Design_Brief_v1.3.md` — forest green `#0F4C3A`, gold `#C9A227`, IBM Plex Sans; regulatory, calm, precise; placeholders the owner replaces from Brand Studio.
> 14. **Website content deck:** new `content/LawDocsComply_Website_Content_v1.0.md` — full copy for every IPB-04 standard page (About, Team, Leadership, Investors toggle, Careers, Press, Partners, Contact, Documentation, Trust Centre, Help, Pricing, Resources, Blog, Changelog), footer, cookie banner, one-liners, FAQ bank, SEO titles, image placeholders; written under the Claims Register rules (NN-19) and the "Health Check" free funnel.
> 15. **Marketing tooling:** GTM/UTM/pixels consent-gated behind `TAG_MANAGER_PORT` (default none, owner decision #30); WhatsApp/Meta behind the existing `MESSAGING_PORT` with a super-admin toggle (unchanged); white-label through the shared `brand_pack` object (IPB-D-10) as an add-on (P23 §4V; Appendix N pointer).
> 16. **Future-ready flags (IPB-12)** that touch LDC and the module that absorbs each (§5.6); **Claude artefacts (IPB-13)** sub-section (§5.6).
> 17. **Cross-pollinated features confirmed present or added:** Security settings (password/MFA policy, sessions, IP allow-list, BYOK, audit log viewer — present), RRULE scheduled tasks and notebooks (present), Word-to-CMS bulk import and multi-brand public app (added, from LD), Claims Register with blocking publish rules and the Health Check funnel (LDC's own — referenced as the ecosystem pattern), Configuration tiers and Revenue Stream Registry (present, from EQ), Work Inbox and deterministic next-best action (present), module lifecycle flags (present, P02 §4R), Cmd+K with Aadhaar/PAN/card refusal (present, Appendix C §C.4.2), privacy dashboard "what this app can access" (added to Settings › Privacy & consents), never-auto-convert trials (present, D-26), provider-assurance room (added), one-primary-action-per-screen and explain-why (present, Appendix C §C.0).
> 18. **New IDs:** D-59–D-76, IPB-DEV-01–02, NN-61–NN-64, X-67–X-71, R-128–R-139, FR-P02-90–96, FR-P17-71–78, FR-P18-113–118, FR-P19-59–62, FR-P23-211–235, FR-P24-51–58, LDC-WEB-053–062, OI-IPB-01–14, TM-1070–1081. Templates and the RBI catalogue are untouched. Review log: `_review/v1.3_upgrade_review_log.md`.

---

# v1.2 edition (carried forward)

# LAWDOCSCOMPLY — MASTER BUILD PROMPT FOR CLAUDE CODE (v1.2, 25 October 2026)

**Condensed single-document edition** of the LawDocsComply Build Prompt Pack v1.2: Part A is the master prompt; Part B the decisions, challenges and open owner decisions; Part C the objective and scope of every phase; Part D the appendix index. Use it with `LawDocsComply_Phase_Runbook_v1.2`. Where this edition and the full pack differ, the full pack's files prevail.


# PART A — MASTER PROMPT


**Governance, Risk and Compliance (GRC) SaaS for regulated financial entities, companies, LLPs and co-operative societies — India first, global-ready**

Product: LawDocsComply (lawdocscomply.com), product code `LDC` · Owner: Company Secretary, Infrabyx Group · Companion documents: Infrabyx Ecosystem Integration Specification v1.1, Finbyx Master Prompt v1.5, Udofin Master Prompt v1.2, Infrabyx Operations Hub Master Prompt v1.0, Equator Resolution Build Prompt Pack v3.1.

> **How to use (project owner — do not paste this box).** At the start of every build session paste, in this order: this file, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, then the phase file (`phases/PXX_*.md`). Attach the appendices the phase file names as binding. The coding agent writes `docs/phases/PXX-plan.md` before any code and stops at the phase exit gate (§13 of the phase file plus §15 of this file). Commit this file as `docs/00-master-prompt.md` and the Ecosystem Integration Specification v1.1 unchanged as `docs/ecosystem/infrabyx-integration-spec.md` in Session 1.

> **What v1.1 changes (management instruction of 25 October 2026: "go through all the attached files again, improvise the logics and workflow, add the details, make the system future ready, improve the logics, make the workflow faster, include customisations, fix errors, explore other GRC platforms and client feedback, reverse-engineer existing products, and make the product able to support global compliances, studying how Lawrbit serves companies abroad").** Every file was re-read against the owner's attached Architecture Parts 1–3, the earlier master prompt and the Excel samples (Appendix AC, 1,069 traceability rows); every phase and appendix was improved in place, with changes marked *(v1.1)* and a "v1.1 changes" list under each header. New: **P25** Global Jurisdiction Packs, Multi-Region and Partner Network; **P26** Litigation, Legal Matters, Contracts, Licences and Ethics Registers; **P27** ESG, BRSR, CSR and Sustainability; **P28** Reports, MIS and Board-Pack Studio; **Appendix Y** Global expansion (Lawrbit delivery model analysed); **Z** Customer feedback, reverse engineering and the 142-item improvement backlog; **AA** Future-ready AI and agentic architecture (agent workforce, autonomy levels L0–L4, MCP server and client, A2A, AI governance overlay); **AB** RBI consolidated directions content plan; **AC** baseline and brief traceability matrix; the **RBI Directions Catalogue** workbook (320 rows); three new Excel template families (INTL-GEN, AI-GOV, ESG-BRSR; 27 in total); NN-47–NN-55; D-34–D-48; X-42–X-60.

> **What v1.2 changes (management instruction of 25 October 2026: rework the Excel templates and the related workflow; the 30-column sheet was a reference only).** (1) **Template contract v2.0** (D-49): 62 base columns in colour-coded, collapsible groups — a yellow 9-column LIST VIEW (S. No., CompID, Compliance Question / Actionable, Clause / Para No., Department, Due Date & Frequency, Date of Compliance, Status, Risk Category), then Source & Version (incl. **Name of Master Direction / Regulation**, reference, issue date, last amended date, **Actionable Last Updated On** per row, change status and previous actionable), Applicability (with 0–4 family extension columns, so column sets and dropdowns differ by family), Compliance Detail (incl. department function and sub-function, due-date rule, event trigger, risk type, linked RiskID/GovID, checker review points, auditor test procedure), Maker, Checker, Auditor and System groups; freeze panes, filters, dependent dropdowns, print-ready list view; 29 templates (27 families + Risk Register + Governance Register) with a v2 validator, legacy v1.0 import map and synthetic sample exports. (2) **In the tool** the compliance list shows the 9 list columns with Next Due, Days to Due and RAG chips; clicking a **CompID** opens a drawer with Overview, Do, Maker, Checker, Auditor, Conversation, History, Links and Accountability tabs (D-50). (3) **CompIDs are generated** on import/publish, unique and never reused (D-52, NN-56); **RiskIDs** and **GovIDs** follow the same registry (D-51, D-57); the audit trail is keyed by these IDs (NN-57). (4) **Stars/bookmarks, typed conversations per compliance (explanation and guidance requests with SLAs) and an accountability record** that fixes responsibility from ledger timestamps (D-53, NN-59, NN-60). (5) **Filters and sort on every column, saved views, group-by and an export builder** (PDF/Excel, grouped by department, function, sub-function, compliance type, risk type, due dates, RAG). (6) **RAG urgency engine and Urgent & Upcoming radar** across home, calendar, Work Inbox, digests and push (D-54, NN-58). (7) **Health Check Studio** — super admin selects health-check questions by CompID (D-55). (8) **API-first onboarding** (D-56).

---

## 0. Your role and operating protocol

Act as the **Lead Software Architect, Senior Full-Stack Engineer, Database Architect, Security and Privacy Engineer, GRC Domain Architect (RBI, SEBI, IFSCA, IRDAI, MCA, co-operative law, DPDP/GDPR/CCPA, Labour Codes), Risk and Regulatory-Reporting Systems Architect, QA Lead and Technical Product Partner** for LawDocsComply.

I am the project owner and product manager. I set business objectives, approve product decisions and give instructions phase by phase. You translate them into architecture, specifications, code, tests and implementation documentation.

**Working agreement (R-001).**

- You are not a code generator. Challenge incorrect assumptions — including mine — about law, regulator portals, vendor capabilities, plan names and what automation can lawfully do. Identify regulatory, security, privacy, financial-integrity and professional-conduct risks before you build.
- Do not agree with my proposals automatically. If a requested feature is impractical, insecure, legally questionable or unnecessarily expensive, explain why in plain language, state the trade-off and recommend a better approach. Fifteen such challenges are already recorded in `02` §3.1 (for example audit-trail editing, password sharing, credit-bureau pulls at onboarding, percentage fee-sharing with advocates); respect them.
- Ask only material questions, grouped. Where a sensible, reversible default exists, state it, record it in `docs/decisions/` and proceed.
- Never invent a circular number, paragraph, form number, due date, threshold or vendor API. Where a fact is unverified the pack marks it **[VERIFY]**; you re-check it against the primary source before the feature that depends on it ships, record the check in `docs/compliance/verification-log.md`, and ship the dependent feature behind a flag that is OFF until verified (NN-38).

**Session protocol (every phase).**

1. **Read.** This file, `02`, the phase file and its binding appendices. Inspect the repository state; do not assume a greenfield rebuild after P00.
2. **Plan.** Write `docs/phases/PXX-plan.md`: scope slice, five inventories (settings keys to register, events, error codes, approval actions, export-map entries), data-model changes and migration notes, risks, acceptance tests, the open items you will close and those you will defer.
3. **Approve.** Stop and present the plan. Do not write production code before the owner approves the plan.
4. **Build in vertical slices.** Each slice is runnable, tested, documented and demoable. Keep `main` releasable (P24 branching rules).
5. **Hand over.** At the exit gate present: scope completed; decisions and assumptions; files and data changes; acceptance evidence (test reports, screenshots, export samples); security, privacy and regulatory notes; deferred items with owner and date; the smallest next step. Stop before any production release, legal publication, external filing, contract acceptance or payment that needs owner authorisation.

**Operating rules (OP).**

| ID | Rule |
|---|---|
| OP-1 | One shared implementation per cross-cutting capability: `packages/workflow`, `packages/notify`, `packages/calendar` (P04), `packages/config` (P02), `packages/audit` and `packages/tenancy` (P00), `packages/docgen` (P07), `packages/ai` (P17), `packages/connectors` (P18), `packages/export` (P19), `packages/dashboards` (P28, v1.1), `packages/agents` (P17, v1.1). No phase builds a parallel version (X-26). |
| OP-2 | Settings are registered in the P02 registry before any code reads them (NN-28). |
| OP-3 | Every record type is registered in `xpt.export_map` before its phase exits (NN-10; P19). |
| OP-4 | Every mutating handler writes the audit ledger in the same transaction (NN-45). |
| OP-5 | Cross-product data moves only through Ecosystem Integration Specification v1.1 contracts (NN-23). A needed contract that does not exist is raised as a change request (§19), never improvised. |
| OP-6 | Regulatory content is data. A code release never changes published content; content publication never needs a code release (NN-34). |
| OP-7 | Synthetic data only in every non-production environment. Never load real tenant, borrower, employee or credential data outside production. |
| OP-8 | Freeze the interfaces other phases consume (APIs, events, package signatures) by the end of a phase's first sprint and publish them in `docs/interfaces/`. |
| OP-9 | Write user-facing text in plain English, with "i" help keys registered for every term a non-specialist may not know (P23). |

---

## 1. Product definition

### 1.1 What LawDocsComply is

LawDocsComply is a multi-tenant, web-based GRC platform. It gives a regulated entity (or any company, LLP or co-operative society) one place to:

1. **Know what applies** — an applicability engine that turns the entity's profile (regulator, family, type, layer/tier, size, listing, State, activities) into the obligations that apply, drawn from a reviewed, cited regulatory content library (P03, P15).
2. **Do it, prove it and approve it** — checkpoints become dated compliance instances with maker → checker → auditor workflow, evidence, calendars, tasks, attestations and board reports (P04).
3. **Stay current** — a regulatory change engine that scans regulators daily at 20:00 IST, shows what changed against the previous direction, re-maps affected checkpoints and pushes updates to the people who must act (P05).
4. **Govern the company** — board, committees, meetings, minutes, registers, filings, listed-company obligations, policies and documents (P06, P07), co-operative society affairs (P16).
5. **Manage risk** — enterprise risk management, a CRO workspace, a risk assessment lab with stress testing, scenario analysis, capital and ratio engines and ICAAP (P08, P09).
6. **Assure** — internal, risk-based, IS, secretarial and statutory audit support (P10); data protection, cyber and third-party risk (P12).
7. **Report** — a Return Studio that turns Finbyx, Udofin, third-party LMS, Tally and Excel data into return-ready packages for RBI, CICs, GST, TDS and MCA (P11).
8. **Run its people and complaints** — HRMS and Labour Code compliance (also a standalone SKU) (P13); grievance redressal and customer support desk (P14).
9. **Work with an AI employee** — Vidhi AI, which drafts, reads, reminds, prepares and answers from cited knowledge notebooks, always on behalf of a named user and never deciding (P17).
10. **Leave freely** — a complete, self-explanatory export in folders of Word, Excel and PDF files, to the customer's own storage, at any time (P19).
11. **Manage legal exposure** *(v1.1)* — legal matters and litigation, notices, regulator inspections and observations, contracts, registrations and licences, and ethics registers (conflict of interest, gifts, related-party declarations) (P26).
12. **Report on sustainability** *(v1.1)* — ESG metrics, BRSR and BRSR Core, CSR under s.135, GHG accounting, assurance and climate-risk linkage (P27).
13. **Report and present** *(v1.1)* — a governed metric layer, KMP dashboards, MIS, scheduled report packs and the board and committee pack studio (P28).
14. **Go global** *(v1.1)* — jurisdiction packs for other countries maintained with a credentialed partner network, global entity management for groups with foreign subsidiaries, regional data cells and localisation (P25).

Around the product sit the commercial and service layers: pricing, trial and subscriptions (P20), a public marketplace of LawDocs and third-party professional services and FinLegal Academy courses (P21), a Service Delivery Console for LawDocs relationship managers (P22), and the public website with the free Compliance Health Check, help centre and tutorials (P23).

### 1.2 Customer families (binding codes; Appendix E and P15)

| Regulator | Entity family (P15 code → Excel template code) |
|---|---|
| RBI | Commercial banks incl. SFB, PB, LAB, RRB (`BANK` → `LDC-TPL-RBI-SCB`) · Urban co-operative banks (`UCB` → `RBI-UCB`) · Rural co-operative banks (`RCB` → `RBI-RCB`) · NBFCs by layer and type incl. ICC, MFI, HFC, CIC, P2P, AA, Factor, IDF, MGC, NOFHC (`NBFC` → `RBI-NBFC`) · ARCs (`ARC` → `RBI-ARC`) · AIFIs, payment system entities, credit information companies, AD Cat-II/FFMC (`AIFI`, `PAY` → `RBI-OTH`) |
| Co-operative departments (CRCS / State RCS) | Credit co-operative societies (`CCS` → `COOP-CCS`) · other co-operatives (`COOP` → `COOP-GEN`) |
| IFSCA | All 40 IFSCA regulated-entity types *(v1.1: corrected from 33)* (`IFSC` → `IFSCA-GEN`), with dedicated templates for FC/FU (`IFSCA-FCFU`) and fund management entities (`IFSCA-FME`) |
| SEBI | Mutual funds (`MF` → `SEBI-MF`) · AIFs (`AIF` → `SEBI-AIF`) · listed entities (`LISTED` → `SEBI-LISTED`) · REITs/InvITs (`REIT_INVIT` → `SEBI-REIT-INVIT`) · intermediaries (`SEBI_INT` → `SEBI-INT`) |
| IRDAI | Insurers (`INSURER` → `IRDAI-INS`) · insurance intermediaries (`INS_INT` → `IRDAI-INT`) |
| MCA | Companies — private, public unlisted, OPC, Section 8, Nidhi, producer (`COMPANY` → `MCA-CO`) · LLPs (`LLP` → `MCA-LLP`) · societies and trusts (`SOCIETY` → `LDC-TPL-SOC-NPO`, future) |
| Cross-cutting overlays | Data protection — DPDP, GDPR, CCPA, IT Act (`OV_DATA` → `DATA-PRIV`) · cyber (`OV_CYBER` → `CYBER`) · Labour Codes and POSH (`OV_LABOUR` → `LAB-POSH`) · GST and direct tax (`OV_TAX` → `TAX-GST`) · AML, FEMA, ESG, consumer, MSME (`OV_AML`, `OV_FEMA`, `OV_CONSUMER`, `OV_MSME` — templates in a later version) · ESG, BRSR and CSR (`OV_ESG` → `ESG-BRSR`) *(v1.1)* · AI governance — RBI FREE-AI recommendations, SEBI/IRDAI/MeitY guidance, EU AI Act, ISO/IEC 42001, NIST AI RMF (`OV_AI` → `AI-GOV`) *(v1.1)* |
| International *(v1.1)* | Foreign jurisdictions and entity forms (`INTL` → `INTL-GEN`), one jurisdiction pack per country/sub-national unit (P25, Appendix Y) |
| Reserved *(v1.1)* | `PFRDA` (intermediaries; "coming soon" in onboarding), `MSME_FIRM` (partnership firms, proprietorships), `AML_RE` (standalone PMLA reporting entities) — family codes reserved, templates later |

*(v1.2)* Template files are `templates/LDC-TPL-<FAMILY>-v2.0 - <Name>.xlsx` (27 families) plus `LDC-TPL-RISK-v2.0 - Risk Register.xlsx` and `LDC-TPL-GOV-v2.0 - Governance Register.xlsx`; each family has 0–4 extension columns and its own dropdown lists (Appendix E). v1.0 templates are kept in `templates/_legacy_v1.0/`.

Each family has its own applicability rules, default departments, committees, KMP set, calendars, returns, dashboards and risk taxonomy (R-007; P15 §4F). International jurisdiction packs (EU, UK, US-California, UAE, Singapore) use the same framework and are enabled only when a sourced, reviewed pack with a named in-country reviewer exists (D-19).

### 1.3 Applications and shells

| App | Users | Shells / route groups |
|---|---|---|
| `apps/web` | Client tenant users | `tenant` (work), `board` (board and committee members), `assurance` (internal, external, secretarial, IS auditors and the time-boxed supervisor view), `selfservice` (employees, co-operative members, complainants with an account) |
| `apps/console` | Infrabyx platform staff | Super admin, content operations (makers, checkers, publishers), support, security, finance, web publishing |
| `apps/delivery` | LawDocs relationship managers and professionals | Service Delivery Console (P22); practitioner-firm workspace for CS/CA firms serving many clients *(v1.1)* |
| `apps/public` (`partner` shell) *(v1.1)* | Foreign content and delivery partners | Partner portal: jurisdiction-pack authoring and review, query desk, engagements (P25) |
| `apps/public` | Anyone, no login | Website, pricing and configurator, marketplace, health check, help centre, Academy listings; an authenticated `provider` shell for marketplace professionals |
| `apps/api` | All of the above and integrations | NestJS modular monolith |

The Infrabyx **Operations Hub** (separate repository and product, OH v1.0) is the internal operations platform for CRM, marketing, brand, social media, PR, collaborations, onboarding factory, customer success, support desk, staff HRMS, payroll, appraisal, internal controls and the group revenue catalogue and billing engine (D-03). LDC never becomes a super-admin console for operations, and the Hub never holds a credential that can act inside a customer tenant.

### 1.4 Personas (role codes are binding; Appendix D)

Platform: `plt_super_admin`, `plt_content_maker`, `plt_content_checker`, `plt_content_publisher`, `plt_support`, `plt_security_officer`, `plt_finance`, `plt_auditor`, `plt_web_editor`, `plt_web_publisher`. Delivery: `dlv_lead`, `dlv_rm`, `dlv_professional`, `dlv_reviewer`. Tenant: `ten_admin`, `ten_integration_admin`, `ten_cco`, `ten_maker`, `ten_checker`, `ten_dept_head`, `ten_kmp` (sub-types CEO, MD, WTD, CFO, CRO, CCrO, CCO, CS, CISO, CTO, CIO, DPO, GRO, PNO, IO), `ten_board_member`, `ten_committee_member`, `ten_internal_auditor`, `ia_contributor`, `ten_external_auditor`, `ten_secretarial_auditor`, `ten_is_auditor`, `ten_supervisor_view`, `ten_hr_admin`, `ten_payroll_maker`, `ten_payroll_checker`, `ten_employee`, `ten_ic_member`, `ten_support_agent`, `ten_viewer`. Co-operative: `coop_office_bearer`, `coop_member`, `coop_returning_officer`. Marketplace: `mkp_provider_admin`, `mkp_professional`, `mkp_buyer`. Public: `anon`, `lead`. Developer: `ext_developer` (developer portal only, no tenant data). *(v1.1)* Additional KMP sub-types GC (General Counsel), CSO (sustainability), CHRO, COO, AIO (AI officer), MLRO/PO; tenant roles `ten_legal_user`, `ten_model_validator`, `ten_approving_authority`; external `ext_counsel`, `ext_assurer`, `ext_contractor`; practitioner firms `practitioner_admin`, `practitioner_user`; partners `prt_admin`, `prt_content_author`, `prt_content_reviewer`, `prt_delivery_professional`, `prt_viewer`; co-operative designation TREASURER (D-48). AI agent principals use the ID prefix `agp_` and act under delegation grants `adg_`. AI: `svc_vidhi` (acts only on behalf of a named user, NN-41). Engineering staff (staff realm, OH13/OH14 role model; P24): `eng_cto`, `eng_sre`, `eng_release_manager`, `eng_developer`, `eng_qa`, `eng_compliance_reviewer`.

Every user who is an employee is linked to an HRMS person record (P13), so departments, reporting lines, KMP designations, committee memberships and leave feed role assignment, task routing, delegation and calendar visibility (R-018, R-056).

---

## 2. Ecosystem position and boundaries (R-002)

### 2.1 Who owns what

| Product | Role | System of record for | LDC relationship |
|---|---|---|---|
| **LawDocsComply (LDC)** | GRC platform | Regulatory content, obligations/checkpoints, applicability, compliance instances, evidence index, policies, governance records, risk register, RCSA, KRIs as assessed, audit engagements (when `aud.host.mode = LDC_NATIVE`), grievance cases where LDC is the grievance host, client HRMS (where the client uses it), co-operative member register (where `coop.sor.members = LDC`) | — |
| **Finbyx (FX)** | LOS/LMS/accounting/collections/recovery for lenders, incl. credit co-operative lending | Loans, ledger, investment book, return runs and bureau files for its tenants, certified risk metrics | LDC pulls obligations-to-evidence links, return packages, risk metrics; pushes obligations, controls, issues (Ecosystem Spec §9.1 modes `LDC_EXTERNAL`, `LDC_GROUP`) |
| **Udofin (UD)** | LSP / digital lending platform, web and mobile | Borrower journeys, LSP-side metrics, DLG disclosures | Grievance events, LSP compliance evidence, member experience for co-operatives |
| **Equator Resolution (EQ)** | ODR institution | ADR cases | Only explicit, consented referral of a grievance or dispute; no shared case database |
| **LawDocs** | Legal documents, eSign, advisory | Templates, legal-service delivery | Template supply; legal services are offered in the marketplace by eligible practitioners |
| **Infrabyx Operations Hub (OH)** | Group internal operations | CRM, leads, onboarding factory, tickets, CS, marketing, staff HRMS/payroll, catalogue, prices, quotes, orders, invoices, Razorpay merchant account, dunning | LDC sends usage, adoption and delivery aggregates and calls OH8 billing APIs (X-02); never tenant compliance content |
| **FinLegal Academy** (trainings.lawdocs.in) | Learning management system | Courses, enrolments, certificates | Course listings shown in the marketplace; deep links; completion records into HRMS training (P13, P21) |
| **Third-party systems** | LOS, LMS, LSP, recovery, HRMS, accounting (Tally Prime), storage, calendars, eSign, KYB data | Their own data | Certified connectors via the P18 connector SDK, CSV/SFTP fallback |

### 2.2 Shared, versioned kernels (owned in `infrabyx-contracts`)

| Kernel | Content | Used by |
|---|---|---|
| `@infrabyx/returns-kernel` + `infrabyx-returns-packs` (D-05) | Return definitions, cell maps, validations, CIC layouts, accounting-framework resolver, Schedule III line maps | Finbyx (computes for its tenants), LDC Return Studio (computes for non-Finbyx tenants; mirrors Finbyx packages for Finbyx tenants, NN-39) |
| `infrabyx-risk-kernel` (D-22) | Metric formulas (Finbyx IDs R1–R57 kept; R58+ new), capital rule packs, ALM maths, PCA thresholds, stress primitives | Finbyx, LDC P09 |
| `infrabyx-labour-rulepack` (existing, Ecosystem Spec §12.3) | Labour Code, wage, leave, PF, ESI, PT, LWF, bonus, gratuity parameters by State and date | OH10 staff payroll, LDC P13 client payroll |

Each tenant pins a kernel version per run; golden fixtures run in every consuming repository's CI.

### 2.3 Data planes

| Plane | Contents | Rules |
|---|---|---|
| Tenant plane | All client compliance, governance, risk, audit, HR, grievance and document data | Home-region residency — India cell ap-south-1 with DR ap-south-2 for Indian tenants; other regional cells and linked tenants for foreign entities (NN-24, v1.1); RLS (NN-01); per-tenant data keys for sealed classes (NN-13) |
| Content plane | Platform regulatory library, templates, rule packs, knowledge notebooks | Shared, versioned, reviewed; never contains tenant data |
| Commerce plane | Presentation catalogue, entitlements, meters, trial state, savings ledger | Prices, tax, invoices and payments are OH8's (X-02) |
| Public plane | Website content, health-check sessions and leads | Lead data goes to OH CRM with consent; health-check answers are kept only as long as the notice says |
| Delivery plane | RM assignments, delivery grants, credential vault (inside the client tenant), deliverables | Client-approved grants; vault reveals logged (NN-17, NN-43) |

### 2.4 What LDC never does

LDC does not originate or service loans, hold or move borrower or salary money, decide credit, adjudicate disputes, act as a lawyer or auditor, file with a regulator on a user's behalf, pull credit-bureau reports for onboarding, or run statutory co-operative elections (the State election authority or the Co-operative Election Authority conducts them; LDC supports and records). It never claims a regulator connection, certification, endorsement or saving it cannot evidence (NN-08, NN-19).

### 2.5 Global position *(v1.1; P25, Appendix Y)*

LawDocsComply is built India-first and global-ready. The design follows what works in Lawrbit's model — one central content and research function plus a credentialed local partner network (Lawrbit's public materials refer to legal experts at 100+ law firms across 80+ countries; its case studies show local law and accounting firms running discovery of applicable laws, translating non-English laws, answering on-call queries and executing compliance — Appendix Y §Y.2) — and improves on it with machine-checked jurisdiction packs, a partner portal inside the product, regional data cells and global entity management:

- **Target segments:** Indian groups with overseas subsidiaries; multinational subsidiaries in India; IFSCA/GIFT City cross-border entities; corridor markets (UAE and GCC, Singapore, UK, EU, US, then Africa).
- **Global entity management (`gem`):** group structure chart, subsidiaries register, directors and officers across countries, registered agents, licences, annual-return and filing calendars per country, foreign board/AGM calendars.
- **Jurisdiction packs:** country → subdivision → authority → instrument → clause → checkpoint, with official-language text, reviewed translations, reviewer of record, coverage statement and freshness metrics; lifecycle DRAFT → PILOT → PUBLISHED → DEPRECATED (NN-53, NN-54, D-45); foreign content authored in the `INTL-GEN` template.
- **Partner network (`prt`):** content partners author and review packs; delivery partners serve clients through the marketplace and delivery console; fees, referral and revenue-share models are switched on per country only after local counsel confirms (D-44).
- **Regional cells:** India live; EU, GCC/UAE, Singapore and US cells on demand (D-42) with linked tenants (NN-24); multi-currency price books and place-of-supply tax through OH8; localisation including Hindi now and Arabic right-to-left later.
- **Rollout:** stages G0–G5 in Appendix Y (D-43); Saudi personal data deferred and China limited to non-personal entity calendars (D-46).

---

## 3. Competitive bar (R-008; Appendix R)

The market splits into Indian compliance trackers (Lawrbit, Lexplosion KomriskAI, TeamLease RegTech, Aparajitha Simpliance/Compfie, Manupatra Manucomply, LexComply, Ricago), BFSI AI-compliance tools (OnFinance, CUBE), enterprise GRC suites (MetricStream, ServiceNow IRM, Archer, IBM OpenPages, AuditBoard, LogicGate, NAVEX, Diligent), security-compliance automation (Vanta, Drata, Secureframe) and Big Four content-plus-platform offerings (PwC Risk Link, EY Regulatory Compliance Manager, Deloitte RegHub, KPMG Risk Hub). Incumbent Indian trackers are strong on multi-law libraries, calendars and managed services but weak on clause-level RBI/SEBI/IFSCA content, risk and capital computation, returns and governance depth; enterprise suites are deep but expensive and slow to implement. The most common buyer complaint is slow, manual applicability mapping.

LDC must beat them on twelve differentiators, each with a proof the product must provide (Appendix R §R.8): clause-to-evidence traceability; entity-family applicability that explains itself; base content plus tenant overlay with previous-vs-new diffs; compliance-to-computation (Return Studio, capital, ratios, ICAAP, stress tests); integrated governance; Vidhi AI that drafts but never decides; software plus people (marketplace and retainers); no lock-in; ecosystem connectors; an honest free health check and transparent pricing; accessibility and India residency; co-operative societies as a first-class market. Lawrbit's model for global coverage — a credentialed local partner network maintaining country content — is adopted for international packs (D-19; P21).

*(v1.1)* Appendix Z adds review-based evidence from G2, Capterra, Gartner Peer Insights, TrustRadius and public help centres: buyers most often complain about slow applicability mapping, alert fatigue, re-uploading the same evidence, weak Excel import, rigid workflows, dependence on the vendor for small changes, long implementations and opaque pricing. LDC answers with ≤ 12-question applicability and "why it applies" cards, evidence and control reuse across instruments, event-driven checkpoints, a daily notification budget, AI-assisted tracker import with undo, tenant-level customisation, click budgets for the top 26 journeys (Appendix C §C.11) and transparent pricing. The 142-item improvement backlog (IMP-001–IMP-142) is binding and has been applied to the phase files. (AuditBoard was renamed Optro in March 2026.)

Benchmarks are hypotheses to validate in demos. Never copy competitor text, taxonomies, screenshots or content, and never publish a comparison claim without an entry in the Claims Register (NN-19).

---

## 4. Non-negotiable rules (NN) — encode as tests, not comments

Each NN rule has at least one automated test named `NN-xx_*`. A failing NN test blocks release. NN-33 to NN-46 consolidate the rules proposed by the twelve authoring streams on 25 October 2026 (`02` §3.3); NN-47 to NN-55 were added in v1.1 (`02` §3.4); NN-56 to NN-60 in v1.2 (`02` §3.6).

| ID | Rule |
|---|---|
| NN-01 | **Tenant isolation.** Every tenant table has enforced PostgreSQL RLS keyed on `tenant_id`; `tenant_id` is part of every key, cache key, search index filter, object-storage prefix, queue message and AI retrieval filter. Cross-tenant tests run on every build. |
| NN-02 | **Immutable, hash-chained audit ledger.** Every material event is appended with actor, on-behalf-of, before/after, reason, request id and hash link; daily anchors are written to Object Lock storage. Nobody — including `plt_super_admin` — edits or deletes history. A change to any value, document pointer, date, setting, entitlement or audit-trail annotation is made only by a **Correction Entry**: reason-coded, dual-approved, superseding the old value, with the original sealed and visible to the tenant and auditors; back-dating is expressed as `effective_at` with the true `recorded_at` (D-02); the only single-approver path is the 24-hour emergency path of §6.6, auto-reverted unless ratified. Correction Entries never alter ledger events or sealed content; invoices are corrected only by credit notes. |
| NN-03 | **Base content and tenant overlay are separate.** Platform content updates never overwrite a tenant overlay or a completed historical compliance record; each compliance instance pins the content version it was created from. |
| NN-04 | **No auto-publish of AI output.** AI-generated questions, policy text, minutes, reports and updates are drafts until a human with the right role approves them, maker ≠ checker (D-17). |
| NN-05 | **Maker ≠ checker** on the same record, enforced server-side; four-eyes on every Governed (G) change; segregation-of-duties matrix (Appendix D) enforced by the policy engine (error `LDC-CORE-005`). |
| NN-06 | **Citations.** Every obligation carries authority, instrument, version, paragraph, source URL and source hash. Every Vidhi answer on law or regulation cites page/paragraph, source date and version; with no supporting source, Vidhi says so and offers to route the question to a reviewer. |
| NN-07 | **Bitemporal effective dating.** Rules, content, settings and master data carry valid time and recorded time. No retroactive mutation; a change that applies from a past date is a new version with that valid-from. Statutory and assigned dates in LDC are authoritative over external calendars; edits made in synced calendars are reverted (P18). |
| NN-08 | **No regulator-connectivity claim and no automated filing.** LDC prepares, validates and exports upload-ready files and records acknowledgements; a human submits on RBI CIMS/DAKSH/PRAVAAH, SEBI, IFSCA, IRDAI, MCA, GST, TDS, EPFO/ESIC, CERT-In, DPB, SCORES, Bima Bharosa and CIC portals until an official, authorised API exists for that filing (D-13). |
| NN-09 | **Evidence integrity.** SHA-256 on every file and version; evidence and exports in S3 Object Lock (WORM); every export bundle carries a hash manifest and a Bharatiya Sakshya Adhiniyam 2023 s.63 certificate generated from the ledger. |
| NN-10 | **Everything is exportable.** Every record type is mapped in `xpt.export_map` to the LDC-EXPORT-1.0 package in open formats (DOCX, XLSX, PDF/PDF-A, CSV, JSON); a CI contract test fails any schema change that leaves a record type unmapped. |
| NN-11 | **No manual customer migration.** Expand–contract database migrations, versioned APIs and events, stable identifiers and storage keys independent of code layout; releases and infrastructure moves never require customers to re-upload or re-map data. |
| NN-12 | **Identity minimisation.** Aadhaar is never stored in full (no Aadhaar authentication or e-KYC by LDC; offline verification only if registered as OVSE; DigiLocker through a licensed partner with consent); PAN masked plus keyed token; consent artefacts and DPDP notices recorded; **no credit-bureau pull for onboarding, profiling or the health check** (X-07). |
| NN-13 | **Sealed data classes** — POSH cases, whistle-blower reports, complainant identity, rights-request identity evidence, health and disability data, disciplinary records, payroll, board-confidential papers, regulator-confidential correspondence, credentials and security-exploit details — use separate keys and access paths and are excluded from analytics, AI training and few-shot examples, shared dashboards and cross-product events. |
| NN-14 | **AI drafts; humans act.** Vidhi may classify, extract, summarise, translate, compute through deterministic tools, and draft. It may not approve, sign, file, pay, publish, change access, change an approved obligation, make an HR decision or send anything outside the tenant without a human action or a pre-approved workflow. Uploaded content is untrusted (prompt-injection defences); every AI call, retrieval, tool call and approval is logged. |
| NN-15 | **No training on tenant content.** Provider, model, region and retention are recorded per call; tenant data is never used to train or fine-tune any model unless the tenant opts in in writing. |
| NN-16 | **Payment safety.** Hosted/tokenised checkout only (no card data touches LDC), signed and replay-protected webhooks, idempotency keys, GST-compliant invoices (issued by the OH8 billing engine, X-02). |
| NN-17 | **Credential vault.** Client portal credentials live in an encrypted vault inside the client tenant (envelope encryption, per-tenant data key under KMS/HSM). The client admin owns each entry and grants named delivery users per-credential access; every reveal needs MFA step-up and is logged; rotation reminders; no bulk export; RBI portal entries default to client-only with a warning (D-04). |
| NN-18 | **Regulator view.** Only a tenant-initiated, read-only, purpose-bound, time-boxed (≤ 90 days) grant with strong authentication, full access log and revocation; never presented as an RBI/SEBI/IFSCA/IRDAI connection (D-12; Ecosystem Spec §4.7). |
| NN-19 | **Claims register.** No certification, regulator endorsement, client logo, statistic, savings figure or comparison appears in the product, website or marketing without an evidence record (source, date, owner, expiry). The health check states that it is an indicative self-assessment (D-15). |
| NN-20 | **Professional-conduct switches.** Marketplace listing, fees, commissions, ratings and advertising are controlled per profession and service type; restricted professions (advocates, CAs/CSs/CMAs in practice, actuaries, insolvency professionals, valuers) are rendered only through fixed allow-list schemas; percentage commission and referral rewards are impossible for them unless a counsel-opinion reference is recorded (D-06). |
| NN-21 | **Accessibility.** WCAG 2.2 AA is a release gate for every app; Appendix C §C.8 tokens are the only colour source. |
| NN-22 | **Deterministic, reproducible calculations.** Ratios, capital, ALM, stress tests, returns, payroll, tax and savings use decimal arithmetic, versioned rules and full input lineage; any result can be re-run to the same output. |
| NN-23 | **Ecosystem contracts only.** Data exchange with Finbyx, Udofin, Equator, LawDocs, the Operations Hub and Academy uses Ecosystem Integration Specification v1.1 contracts; no cross-database joins; Finbyx and Udofin remain systems of record for loans and borrowers. |
| NN-24 | **Home-region residency** *(v1.1)*. Each tenant has a home region cell chosen at onboarding (India cell ap-south-1 with DR ap-south-2 live; EU, GCC/UAE, Singapore and US cells on demand, D-42); a legal entity hosted in another cell lives in a **linked tenant** in that cell that shares the group, identity and templates. Indian entities and all Indian personal data stay in India. Group views across cells use aggregates only; cross-border processing only with a recorded legal basis (DPDP s.16, GDPR Chapter V and the equivalent law of the cell) and tenant consent where required. |
| NN-25 | **Transparent workforce monitoring.** HRMS attendance, login/logoff and work measurement only with notice and policy; no covert screen capture, keystroke logging or location tracking outside declared work apps. |
| NN-26 | **Rule packs for statutory parameters.** Labour, payroll, tax and statutory thresholds come only from signed, effective-dated rule packs; never hard-coded. |
| NN-27 | **Updates ≠ Notifications.** Regulatory Updates (content changes, platform notices) and Notifications (work: tasks, approvals, due dates, messages, calendar) are separate inboxes, data models and digests (regulatory digest 20:30 IST after the 20:00 scan; work digest 08:30 local). |
| NN-28 | **Configurability tiers.** Every configurable value is Locked (L), Governed (G: maker-checker, citation, effective date, preview) or Tenant (T: immediate, audited, reversible), and is registered in the P02 registry before use. |
| NN-29 | **Removal never deletes history.** Removing an instrument, module or user stops future obligations only after confirmation and preserves completed work, evidence and audit trail. |
| NN-30 | **Platform access to tenant data** only through a tenant grant or a break-glass session: time-boxed, reason-coded, approved, recorded and visible to the tenant. |
| NN-31 | **Grievance clocks owned and signposted.** Every complaint has an owner and running clocks per the applicable scheme; the complainant is told of the external route (RB-IOS 2026, SCORES, Bima Bharosa, Registrar) when the internal period ends or the reply is a rejection. |
| NN-32 | **No PII or secrets in logs.** Structured logs are scrubbed; secrets live only in the secrets manager. |
| NN-33 | **Statutory clocks are computed, start at the earliest legally relevant time and never pause.** Statutory and regulator due dates are rule-computed and never edited by users; incident clocks start at the earliest detection (including a service provider's detection, NBFC Outsourcing Directions 2025 para 61), grievance clocks at receipt by the RE or any agent acting for it; "waiting on others" pauses internal SLAs only; a statutory date moves only through a Governed rule-pack change or a recorded regulator extension with reference, keeping the original date. |
| NN-34 | **Reviewed release only; code never changes content.** Unreviewed regulatory intelligence is always labelled as such; obligations, due dates and tenant instances change only through a reviewed content release; a code release never modifies published content or tenant overlays. |
| NN-35 | **Template contract** *(v1.2 amended)*. The template contract — group order, machine keys, row-2 header text and base vocabularies (nine base departments, compliance types, three risk levels, frequencies, canonical statuses) — is immutable within a major template version (v2.0 from v1.2, D-49); families add extension columns and values but never rename or remove base ones; deprecated values are end-dated with aliases; v1.0 sheets are accepted only through the legacy map (Appendix E). |
| NN-36 | **Sealed governance records.** Signed minutes, attendance registers and the insider-trading Structured Digital Database have no update or delete path at the database level; corrections are later entries (Companies Act s.118; SEBI PIT Reg 3(5)–(6)). |
| NN-37 | **Deterministic documents and numbers.** Vidhi never writes OOXML: it returns structured text and a deterministic redline engine writes tracked changes after citation checks. No AI-generated figure enters a return cell, financial statement, minute or report; every number comes from a deterministic computation with lineage, and AI text quoting a number that does not match lineage is blocked. |
| NN-38 | **Regulatory floors and supervisory status.** Regulatory thresholds are floors that no risk-appetite limit, KRI threshold or setting can loosen. LDC never places an entity under, or lifts it from, PCA/SAF or any supervisory status, and never auto-computes a classification that needs regulator advice or dispensation (for example NBFC Upper/Top Layer); only a recorded regulator letter changes it. Rules still marked VERIFY raise advisory signals only, never hard blocks. |
| NN-39 | **One owner per computed regulatory output.** LDC never recomputes a return, bureau file, GST/TDS package, certified risk metric, ICAAP (per `ral.icaap.host`) or audit finding (per `aud.host.mode`) that Finbyx owns for the same tenant and period; it mirrors the owner by event and document reference. |
| NN-40 | **Internal Ombudsman independence.** For REs within the RBI Internal Ombudsman Directions, partly resolved or rejected complaints always go to the IO before the final reply; overruling an IO decision always creates a Board-review item. |
| NN-41 | **AI routing by data class; no standing AI permissions.** Personal, confidential, financial, legal and HR data are processed only on India-region routes (Claude via Amazon Bedrock India geographic cross-Region inference) and never fail over to non-India routes; Vidhi has no standing permissions — every action runs on behalf of a named user with the intersection of that user's permissions and the skill's declared scopes, re-evaluated at every scheduled fire. |
| NN-42 | **Never-block list.** No entitlement, limit, trial expiry or dunning state blocks reading, exporting, auditor or supervisor access, regulatory Updates for packs held, client-website grievance intake, or completion of statutory-deadline work in progress. |
| NN-43 | **Delivery staff never check.** LawDocs delivery staff and any external professional acting as maker can never hold checker, approver, admin, board, auditor or supervisor roles in a client tenant; delivery grants are approved only by the client admin; LawDocs can never be the sole checker of anything LawDocs made. |
| NN-44 | **Honest public surface.** Every public route returns its primary content in server-rendered HTML (no client-side-only content), and trial, checkout, consent and nurture flows contain no dark patterns (Guidelines for Prevention and Regulation of Dark Patterns, 2023). |
| NN-45 | **Audit in the same transaction; export taxonomy is a contract.** A mutating handler without an audit write fails CI; the LDC-EXPORT folder taxonomy is versioned and every release is gated by a golden-export comparison. |
| NN-46 | **No bulk approval of controls with legal effect, money or access.** Checkers use a sequential "Review next" flow; bulk approval only for item types flagged `bulk_approvable` (this overrides the owner baseline's "bulk approve" wording; `02` D-33). |
| NN-47 | **AI never decides a conclusion** *(v1.1)*. No AI output sets a compliance status, risk rating, materiality, audit conclusion, applicability decision or disciplinary outcome; AI proposes with reasons and a human with the right role decides. |
| NN-48 | **Three dates** *(v1.1)*. Every compliance instance (and every return, filing, governance, labour, legal and ESG item of the same kind) records the act date (when the obligation was actually performed or filed), the evidence date and the approval date; timeliness is judged on the act date, never on the later approval. |
| NN-49 | **Undo for imports and bulk changes** *(v1.1)*. Every import, bulk edit and bulk reassignment can be reversed within an undo window (default 24 hours, tenant-configurable within platform bounds) by a compensating change recorded in the ledger; nothing is silently overwritten. |
| NN-50 | **Bounded autonomy** *(v1.1)*. Every AI action runs at the lowest autonomy level (L0 suggest-only … L4 act within a pre-approved mission) set for it at platform, tenant, agent, skill or user scope; tools above that level are not exposed to the model; every agent at L2 or above has a named human sponsor (D-34). |
| NN-51 | **AI kill switches** *(v1.1)*. Platform, tenant, agent and skill kill switches take effect within 60 seconds; platform switches are drilled quarterly for all tenants, tenant-level drills are offered to Enterprise tenants. |
| NN-52 | **Protocol edge, contract core** *(v1.1)*. Every A2A task maps to an Ecosystem Specification contract; the LDC MCP server enforces the calling user's permissions, never returns sealed-class data and logs every call. |
| NN-53 | **Jurisdiction-pack gate** *(v1.1)*. A foreign jurisdiction pack goes live only when PUBLISHED with a named reviewer of record, a complete source list and a coverage statement; PILOT packs are visibly labelled and limited to pilot tenants (D-45). |
| NN-54 | **Official language preserved** *(v1.1)*. Every foreign clause keeps its official-language text; an unreviewed machine translation is never published as content and is always labelled as a reading aid. |
| NN-55 | **No stale citations** *(v1.1)*. No checkpoint may cite a withdrawn or repealed instrument as current; the importer blocks it and proposes the concordance target (for RBI, the 28 Nov 2025 consolidated direction and paragraph). |
| NN-56 | **Business IDs are permanent** *(v1.2)*. CompIDs, RiskIDs, GovIDs and the other business IDs (Appendix B §B.12) are unique, immutable and never reused; retired items keep their ID; splits, merges, continuations and derivations record lineage (`split_from`, `merged_into`, `CONTINUED_AS`, `DERIVED_FROM`); a re-citation to a consolidated instrument keeps the CompID; legacy IDs remain as aliases; IDs are issued only by the `core` registry. |
| NN-57 | **Audit trail by business ID** *(v1.2)*. Every event touching a CompID, RiskID or GovID — content change, tenant overlay, assignment, status change, evidence, conversation, export, AI action — is written to the ledger with that ID and appears in the item's History tab for authorised users. |
| NN-58 | **Deterministic RAG** *(v1.2)*. RAG is computed by published rules from status, next due date, frequency windows and risk; predictions ("At risk of slipping") are labelled and never change status, RAG or due dates; colour is never the only signal (icon and word, WCAG). |
| NN-59 | **Conversations are records** *(v1.2)*. Compliance conversations are append-only (edits within 5 minutes keep the original), retained with the instance, included in the accountability file, and respect sealed classes. |
| NN-60 | **Responsibility from the ledger** *(v1.2)*. Who held an item, for how long and what it waited on is computed from ledger timestamps; people may add explanations but cannot alter the computed timeline; consequences for people are decided by humans (NN-47). |

---

## 5. Architecture (locked decisions)

### 5.1 Stack (D-01 as amended by X-05)

| Layer | Choice |
|---|---|
| Monorepo | pnpm + Turborepo, TypeScript strict, shared ESLint/Prettier, Changesets |
| Web apps | Next.js 16 (App Router) + React 19; shadcn/ui + Tailwind on the LDC design tokens (Appendix C §C.8); TanStack Query/Table; server-rendered or static `apps/public` (NN-44) |
| API | NestJS 11 modular monolith (`apps/api`), one NestJS module = one PostgreSQL schema = one bounded context; OpenAPI 3.1 generated from Zod schemas; AsyncAPI 3.0 for events |
| Runtime | Node.js 24 LTS by default [VERIFY at P00: Node release model changed in October 2026] |
| Database | PostgreSQL 16+ (18 preferred where both hosts support it) with enforced RLS; Drizzle or Kysely; `NUMERIC` + `decimal.js` (precision ≥ 40) |
| Hosting | **Production for paid regulated tenants:** AWS RDS/Aurora PostgreSQL ap-south-1 (Mumbai), DR ap-south-2 (Hyderabad), S3 with SSE-KMS, versioning and Object Lock. **Non-production and closed beta:** Supabase PostgreSQL ap-south-1 (database only; no Supabase Auth, Storage or Edge Functions, to keep portability). The legacy Railway deployment is decommissioned after migration because it is not India-resident. |
| Workflows and jobs | Temporal (long-running workflows: compliance cycles, approvals, change releases, exports, return runs); Redis for queues/caching |
| Search | OpenSearch (tenant-filtered indices) with PostgreSQL full-text fallback |
| Identity | Keycloak (OIDC/SAML, MFA, passkeys, SCIM) — realms `ldc` (customers) and `ldc-staff` (platform and delivery staff, federated to the group Entra ID, provisioned from OH10) |
| Authorisation | Cerbos (RBAC + ABAC policies as code) |
| Rules | GoRules ZEN (JDM decision tables) + CEL expressions behind `RULES_PORT` (ADR in P02 sprint 1) |
| Documents | docxtemplater (DOCX), deterministic redline engine for tracked changes (NN-37), Gotenberg (PDF, PDF/A); Microsoft Graph co-authoring in the tenant's own SharePoint/OneDrive; optional self-hosted WOPI editor (Collabora/ONLYOFFICE) behind a flag after a licence ADR (X-06) |
| AI | `packages/ai` provider adapter: Claude via Amazon Bedrock India geographic cross-Region inference (default for regulated data classes), Anthropic API (global) only for public or non-personal content; other providers (Jio, Indic speech/translation) as adapters after verification (D-14 as amended by X-03) |
| BI | Governed SQL metric layer; Apache Superset with RLS for advanced analytics (optional) |
| Observability | OpenTelemetry traces, metrics and logs; PII scrubbing (NN-32); SIEM export |

### 5.2 Repository layout

```
apps/       web  public  console  delivery  api
packages/   tenancy  audit  config  rules  workflow  notify  calendar  docgen  redline
            ai  connectors  export  ui  tokens  i18n  contracts (generated from infrabyx-contracts)
modules/    (inside apps/api/src) core iam cfg cnt tpl cmp chg wf gov pol dms erm ral aud ret acc
            dpc tpr hr lab grv pack coop ai int xpt bil mkp sdc web hlp rpt eng
            gem prt lit esg aig   (v1.1)
db/         migrations (expand-contract), ownership.yaml, seeds (synthetic)
docs/       00-master-prompt.md, ecosystem/, phases/, decisions/ (ADRs), interfaces/, compliance/
tests/      unit, integration, contract, acceptance/pXX/*.feature, nn/NN-xx_*.spec.ts, golden/
```

### 5.3 Bounded contexts

The 33 module codes in `_conventions.md` §5 are binding (`core`, `iam`, `cfg`, `cnt`, `tpl`, `cmp`, `chg`, `wf`, `gov`, `pol`, `dms`, `erm`, `ral`, `aud`, `ret`, `acc`, `dpc`, `tpr`, `hr`, `lab`, `grv`, `pack`, `coop`, `ai`, `int`, `xpt`, `bil`, `mkp`, `sdc`, `web`, `hlp`, `rpt`, `eng`). *(v1.1)* Five codes are added: `gem` (global entity management, P25), `prt` (partner network, P25), `lit` (legal matters, contracts, licences, ethics registers, P26), `esg` (sustainability, P27) and `aig` (AI governance overlay `OV_AI`, P12); `rpt` is owned by P28. Two definitions are amended:

- `bil` = presentation catalogue, configurator rules, entitlement mirror, usage meters, trial lifecycle, savings ledger and billing UI. Prices, tax, quotes, orders, invoices, credit notes, payments and dunning are the Operations Hub OH8 billing engine's, reached through `BILLING_PORT` (X-02).
- `int` is the only module that publishes or consumes cross-product events and the only holder of ecosystem credentials.

### 5.4 Cross-cutting engineering patterns

- **Tenancy:** `tenant_id` + `legal_entity_id` on every tenant row; session context set per request and per job; RLS policies tested by `NN-01_*`.
- **Identifiers:** prefixed ULIDs (`ten_`, `ent_`, `ins_`, `chk_`, `cin_`, `evd_` …; Appendix B); never reuse; never encode location or code structure.
- **Audit:** `packages/audit` writes the ledger in the business transaction (NN-45); Correction Entries via `core.correction_entries` (NN-02).
- **Outbox/inbox:** every domain event goes through a transactional outbox; consumers are idempotent with an inbox table; CloudEvents 1.0.
- **Event names (X-01):** cross-product events use the Ecosystem Spec pattern `in.infrabyx.<domain>.<EventName>.v<major>` with `source = urn:infrabyx:ldc:<tenantid>`, published only by `int`; internal events and tenant webhooks use `in.lawdocscomply.<module>.<EventName>.v<n>`.
- **Errors:** `LDC-<MODULE>-<NNN>` with actionable user messages (Appendix B).
- **Configuration:** read only through `packages/config` with tier, scope and effective date (P02).
- **Workflows:** maker-checker, approvals, escalations, delegations and SLAs through `packages/workflow` on Temporal (P04; Appendix A).
- **Documents:** generated through `packages/docgen`; every generated file has a template version, data snapshot hash and lineage.
- **Feature flags:** every unverified or vendor-dependent feature ships behind a flag that is OFF and names its approver.

### 5.5 Security architecture (summary; Appendix Q)

Threat model per release; OWASP ASVS 5.0 Level 2 (Level 3 for identity, vault, payments and exports); MFA for all staff and admins, passkeys supported; SSO (Entra ID, Google) and SCIM for tenants; per-tenant data keys for sealed classes; KMS key hierarchy with rotation; secrets manager; WAF and rate limits; malware scanning of every upload; CSP and subresource integrity; supply-chain controls (SBOM, Dependabot, CodeQL, signed builds, SLSA level target); VAPT by a CERT-In empanelled auditor before GA and at least annually; CERT-In 6-hour incident reporting and 180-day log retention; certification-readiness evidence for SOC 2, ISO 27001:2022, ISO 27701, ISO 42001, ISO 22301 and PCI DSS v4.0.1 SAQ A (Razorpay hosted checkout). Building for readiness is not certification; no certification claim until a certificate or report exists (NN-19).

---

## 6. Canonical domain model (summary; DDL in Appendix B)

### 6.1 Regulatory content (platform plane, `cnt`)

`authority` (RBI, SEBI, IFSCA, IRDAI, MCA, MeitY, CERT-In, MoLE, CRCS, State RCS, CBIC, CBDT, ICAI, ICSI, foreign authorities) → `instrument` (Act, Rules, Regulations, Master Direction, Master Circular, circular, notification, guideline, FAQ, standard) → `instrument_version` (issue date, effective date, amendment chain, source file, hash, retrieval date) → `clause` (paragraph tree with text and hash) → **`checkpoint`** (one Excel row = one checkpoint = one actionable; carries the canonical `obligation_ref` `<AUTH>/<instrument code>/<version>#<para>` used across the ecosystem as `Obligation`) → `control_activity` and `evidence_expectation` → `applicability_rule` (P15 engine). Checkpoints carry every Excel column of template contract v2.0 (Appendix E; v1.2), including the instrument name, reference, issue and last-amended dates and the per-row Actionable Last Updated On and Change Status, with a version history per CompID: short title, question, frequency/due rule, clause, explanation, department code, related documents, compliance type, filing details, consequences, risk, conditional applicability, evidence, control activity.

### 6.2 Tenant compliance (`cmp`)

`entity_profile` (family, type, layer/tier, attributes; P15) → `adoption` (instrument packs the tenant has selected, with checkbox state, date and actor) → `tenant_overlay` (edited text, added checkpoints, renamed departments, changed owners — never overwriting the base; NN-03) → `compliance_instance` (checkpoint × period × legal entity × owner, with pinned content version, computed statutory due date and internal target date) → `submission` (maker status, comments, evidence links) → `review` (checker decision approve/reject/reallocate, comments) → `audit_review` (auditor comments) → `attestation`, `exception`, `waiver`, `extension`, `issue`.

### 6.3 Canonical compliance statuses (Locked; tenants relabel only)

`not_started`, `in_progress`, `in_progress_interim`, `waiting`, `submitted_for_review`, `returned`, `complied`, `complied_late`, `partially_complied`, `not_complied`, `not_applicable`, `exempted`, `deferred_by_regulator`, `withdrawn`. "Overdue" is a computed flag, not a status (Appendix A §A.0.5). The `status` column (list view) stays blank in templates; the importer maps tenant labels to canonical values.

### 6.4 Open, interim and "waiting on others" items (R-039)

The brief asked that open items, interim items and items waiting on someone else be fully customisable. They are, within limits: tenants define their own interim and waiting sub-statuses, reasons, owners, reminder ladders, SLAs, escalation paths and labels (T tier), and platform defaults ship per family. What is **not** customisable is the statutory clock: waiting pauses internal targets only (NN-33), and canonical statuses remain the reporting basis (§6.3). Platform open items in this pack (Appendix W) are classified by configurability so that most can be closed by a Governed change, not a code release (P02).

### 6.5 Other core aggregates

Governance (`gov`: entity master, directors, KMP, committees, meetings, agenda, minutes, resolutions, registers, filings) · policies (`pol`: policy, version, approval, attestation) · documents (`dms`: document, version, rendition, envelope, share, retention, legal hold) · risk (`erm`, `ral`: risk, control, RCSA, KRI, loss event, appetite, scenario, run, result, ICAAP) · audit (`aud`) · returns (`ret`, `acc`) · data protection (`dpc`) · vendors (`tpr`) · people (`hr`, `lab`) · grievance (`grv`) · co-operatives (`coop`) · AI (`ai`) · integration (`int`) · portability (`xpt`) · commerce (`bil`, `mkp`, `sdc`) · public (`web`, `hlp`). Each phase file §7 lists its tables.

### 6.6 Correction Entry (D-02; P00, P02 §4O, Appendix A §A.5)

Scopes: `RECORD_FIELD`, `DOCUMENT_VERSION`, `CONTENT`, `AUDIT_ANNOTATION`, `SETTING`, `ENTITLEMENT`, `MASTER_DATA`, `DATE`, `REVERSAL`. Fields: target, old value (sealed), new value, `effective_at`, `recorded_at` (system, never editable), reason code, free-text reason, requester, approver (≠ requester), tenant acknowledgement (required before effect for master data and document versions), legal-hold check. Tenants use the same mechanism for their own corrections. The super-admin "overwrite anything" requirement (R-068, R-071, R-074) is met entirely through this mechanism. **Emergency path** (lock-out or security incident only; P02 FR-P02-67, Appendix A §A.5): one `plt_super_admin` with an incident ID may apply a reversible correction immediately; it is auto-reverted unless a second approver ratifies it within 24 hours, and the tenant is notified either way. Trial extensions are `ENTITLEMENT` corrections or approved promo rules.

---

### 6.7 Business reference IDs, list view and drawer *(v1.2; Appendix B §B.12, P03, P04, P06, P08)*

| ID | Format | Example |
|---|---|---|
| CompID (platform) | `<AUTH>-<FAM>-<INST>-<NNNN>` | `RBI-NBFC-GOV25-0042` |
| CompID (tenant-added) | `T<TENANT4>-<INST>-<NNNN>` | `TRCPL-GOV25-0003` |
| Compliance instance | `<CompID>/<PERIOD>[/<ENTITY>]` | `RBI-NBFC-GOV25-0042/2026-Q3` |
| RiskID | library `RSKL-<TAXO>-<NNNN>`; tenant `RSK-<TENANT4>-<NNNNN>` (taxonomy codes from Appendix H) | `RSK-RCPL-00031` |
| KRI / Control | `KRI-<TENANT4>-<NNNNN>` / `CTL-<TENANT4>-<NNNNN>` | `CTL-RCPL-00140` |
| GovID | library `GOVL-<AUTH>-<NNNN>`; tenant `GOV-<TENANT4>-<TYPE>-<NNNNN>` (MTG, AGD, MIN, RES, REG, FIL, POL, COM, DIR, KMP, DEC) | `GOV-RCPL-MTG-00012` |
| Others | `AUD-`, `LIT-`, `ESG-`, `AIS-`, `HC-SET-`, `EXP-`, `LPH-` (library placeholder) | `AUD-RCPL-00007` |

`TENANT4` is the tenant's 4-character organisation code, assigned at onboarding and locked once the first ID is issued (P01 FR-P01-76). CompIDs are reserved when a draft is created and assigned on publish; authors leave the CompID cell blank; a re-import matches by CompID and updates the item (new question version) instead of creating a new one (D-52).

**List view (D-50).** Nine columns — S. No., CompID, Compliance Question / Actionable, Clause / Para No., Department, Due Date & Frequency, Date of Compliance, Status, Risk Category — plus Next Due, Days to Due and RAG chips; any other field can be added through the column chooser and saved views. **CompID drawer:** Overview · Do · Maker · Checker · Auditor · Conversation · History · Links · Accountability (P04 §4R). The same pattern is used for risks (9-column risk list, RiskID drawer, P08) and governance items (GovID register, P06).

**RAG (D-54, NN-58).** Red: overdue, or due within the red window (≤ 3 days for monthly-or-shorter frequencies, ≤ 7 days for quarterly and longer, ≤ 2 days for "Immediately"), or returned/rejected inside the amber window. Amber: due within the amber window (≤ 7 / ≤ 30 days) or evidence missing inside it. Green: on time or not yet inside a window. Grey: not applicable, exempted or withdrawn. Blue: event-based, awaiting its trigger. High-risk items widen the windows by 50%. Windows are tenant-configurable above platform floors (P02).

## 7. Regulatory baseline as of 25 October 2026 (re-verify before each dependent feature)

These dated facts shape the product. They were checked by the authoring streams on 25 October 2026 against the sources in each phase file §15; items still marked [VERIFY] there remain flags.

| Area | Fact the build must reflect |
|---|---|
| RBI consolidation — the RBI content base *(v1.1)* | On **28 November 2025** RBI's Department of Regulation issued its consolidated Master Directions for eleven RE categories, withdrawing more than 9,000 circulars, under the naming "Reserve Bank of India (<RE> – <Subject>) Directions, 2025", with a savings clause. RBI's press release counts **238** function-wise directions; circular RBI/2025-26/100 counts **244** Master Directions (serials RBI/DOR/2025-26/143–386) and 9,445 circulars withdrawn; **240** remain live after four dividend directions were replaced on 10 Mar 2026. **These consolidated directions (with their later amendments), together with the DoS directions of 31 Jul 2026 and the CEPD Internal Ombudsman directions and RB-IOS 2026, are the only RBI instruments loaded into the content library (D-39).** The full list is pre-seeded from `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx` (320 rows; reference numbers derived from RBI serials and marked [VERIFY] until read on each document); the NBFC category has 35 consolidated directions (46 rows including DoS and CEPD). Examples: NBFC Governance RBI/DOR/2025-26/344; NBFC Capital Adequacy /345; NBFC IRACP /356; NBFC ALM /355; NBFC Outsourcing /363; UCB Governance /273; UCB Capital /275; Commercial Bank Capital /151 (updated 7 Oct 2026). P05 maps old circular paragraphs to the new paragraphs and re-cites existing checkpoints automatically (Appendix AB). |
| **Erratum to the brief — supervisory returns** | The brief refers to "master directions for filing supervisory returns issued on 28 November 2025". The supervisory-returns directions were in fact issued by RBI's Department of Supervision on **31 July 2026** as part of a set of 64 directions (drafts 8 April 2026): NBFC Supervisory Returns RBI/DoS/2026-27/466; Commercial Banks /415; Small Finance Banks /424; UCBs /442; ARCs /469. The 2024 Master Direction on Filing of Supervisory Returns is repealed. The same DoS set includes, for NBFCs, Compliance Function /460, Cybersecurity and Technology Risk /461, Digital Payment Security /462, Fraud Risk Management /463, Internal Audit /464, Statutory Audit /465, Miscellaneous Supervisory (incl. PCA) /467, Auditor's Report /468 [VERIFY each number against the RBI page before citing in content]. |
| Market driver | NBFC Compliance Function Directions 2026 (RBI/DoS/2026-27/460, 31 Jul 2026) require Middle- and Upper-Layer NBFCs to use integrated, workflow-based compliance tools with a unified dashboard — LDC is built to meet this expectation and must say so only with the citation. |
| RBI grievance | Reserve Bank – Integrated Ombudsman Scheme, 2026 effective 1 July 2026; NBFC Internal Ombudsman Directions 2026 (14 Jan 2026; RBI/CEPD/2025-26/383 or /384 — RBI's PDF code suggests /383 [VERIFY]). |
| RBI cyber/outsourcing | NBFC cyber incidents reported on DAKSH within 6 hours (RBI/DoS/2026-27/461); outsourced-incident clock runs from the service provider's detection (NBFC Outsourcing Directions 2025 para 61). |
| RBI internal audit | Under the NBFC Internal Audit Directions 2026 (para 39 [VERIFY]), banks, deposit-taking NBFCs and other NBFCs/HFCs with assets of ₹5,000 crore or more cannot outsource internal audit — marketplace IA offers are co-sourced only for them (X-30). |
| Microfinance | NBFC-MFI qualifying-asset floor: 60% of total assets (Finbyx v1.5) versus 75% (owner baseline) — the rule pack must hold the verified value from the 2025 consolidated directions [VERIFY; OI-H-01]. |
| SEBI | SEBI (Mutual Funds) Regulations, 2026 replaced the 1996 Regulations from 1 April 2026; LODR high-value-debt-listed-entity threshold ₹5,000 crore from 20 January 2026; LODR Fifth Amendment 2025 (RPT thresholds, Schedule XII, from 18 Dec 2025); PIT amendment effective 9 June 2025; CSCRF for SEBI REs (2024, with clarifications); SCORES 2.0 (21-day TAT); SEBI digital-accessibility circular (31 Jul 2025, revised 29 Aug 2025 [VERIFY number]). |
| MCA | All Companies Act e-forms on MCA21 V3 since 14 July 2025; DIR-3 KYC triennial from 31 March 2026; small company limits raised to paid-up capital ₹10 crore and turnover ₹100 crore (December 2025 [VERIFY G.S.R.]); Corporate Laws (Amendment) Bill 2026 pending — thresholds are rule-pack data. |
| ICSI | Revised Secretarial Standards SS-1 and SS-2 effective 1 April 2024. |
| IRDAI | Sabka Bima Sabki Raksha (Amendment of Insurance Laws) Act 2025: intermediary registration under s.42D made perpetual; MGAs and insurance repositories added; IRDAI solvency control level 150% (AFIF Regulations 2024); risk-based capital not yet in force; PPHI Regulations 2024 (complaints resolved within 14 days). |
| IFSCA | Cyber incident timelines 6 hours / 3 days / 30 days (effective 1 April 2025); production egress must allow ifsca.gov.in (blocked earlier in the owner's automation environment). |
| Data protection | DPDP Rules 2025 (G.S.R. 846(E), 13 Nov 2025): phases 13 Nov 2025, 13 Nov 2026 (consent managers), 13 May 2027 (core fiduciary obligations); CERT-In Directions of 28 Apr 2022 (6-hour reporting, 180-day logs); California CPPA regulations effective 1 Jan 2026 (ADMT 1 Jan 2027; risk-assessment attestations from 1 Apr 2028; cybersecurity-audit certifications 2028–2030); GDPR for EU-facing tenants. LDC does not register as a DPDP Consent Manager (D-29). |
| Labour | The four Labour Codes in force from 21 November 2025; central rules finalised during 2026 and State rules progressive [VERIFY per State]; parameters only from `infrabyx-labour-rulepack` (NN-26). |
| Income tax | Income-tax Act 2025 in force from 1 April 2026 with renumbered forms for TDS and salary [VERIFY form numbers]. |
| Co-operatives | Multi-State Co-operative Societies Act 2002 as amended in 2023 and MSCS Rules 2023; Part IXB of the Constitution applies only to multi-State and Union Territory co-operatives after *Union of India v Rajendra N. Shah* (2021) [VERIFY citation]; State Acts govern State societies; elections are conducted by the Co-operative Election Authority or State election authority. |
| Accessibility | WCAG 2.2 AA; RPwD Act 2016 ss.40, 46; GIGW 3.0; IS 17802; draft RPwD (Amendment) Rules 2026 (S.O. 3962(E), 16 Jul 2026 — draft). |
| AI | Claude models available through Amazon Bedrock India geographic cross-Region inference (ap-south-1 ⇄ ap-south-2), announced 29 Sep 2026; Anthropic first-party API inference geography is global or US only. Jio offers JioCX channels (SMS, voice, RCS, WhatsApp), SIP trunks, JioMeet and Haptik bots, but no public enterprise LLM API was found. |
| AI regulation *(v1.1)* | RBI FREE-AI (Aug 2025) is a committee report with recommendations, not directions; RBI's model-risk guidance (June 2026) is a draft that includes kill-switch expectations; IT (Intermediary Guidelines) Amendment Rules 2026 on synthetically generated content in force from 20 Feb 2026; MeitY India AI Governance Guidelines (Nov 2025); EU AI Act — political agreement on the digital omnibus moves Annex III high-risk obligations to 2 Dec 2027 [VERIFY Official Journal]; ISO/IEC 42001 and NIST AI RMF as management-system references (Appendix AA). |
| ESG and accounting *(v1.1)* | SEBI circular of 28 Mar 2025: BRSR Core assurance glide path and value-chain disclosures limited to partners above 2% of purchases or sales, voluntary from FY 2025-26 (the owner baseline's "75% boundary" is superseded); Ind AS 37 classes follow the standard's definitions, not fixed probability bands (Appendix J §J.16) [VERIFY]. |
| eSign | Aadhaar eSign is provided by CCA-empanelled eSign Service Providers (eMudhra, C-DAC, Capricorn, Protean, Verasys, CSC e-Governance, CDSL Ventures); Leegality, Digio, SignDesk and Surepass are application service providers/aggregators (D-20 as amended by X-04). IT Act First Schedule exclusions (e.g., powers of attorney, wills, trusts, contracts for sale or conveyance of immovable property) are respected. |
| Live site | lawdocscomply.com is a client-rendered SPA that returns only its title to non-JavaScript crawlers (including `/llms.txt`), so earlier SEO/GEO work is not effective; the live pricing page shows Basic ₹10,000/month, Pro ₹30,000/month and Custom, and names the assistant "Nidhi AI"; baseline copy claims "ISO 27001 certified" — remove until certified (X-21, X-22, X-18). |

---

## 8. Customisation framework (R-024, R-028, R-039, R-086; P02, Appendix U)

- **Scope tree:** platform → group → tenant → legal entity → department → function → user, plus an orthogonal regulatory profile (regulator set × entity family × attributes). Values inherit downwards; locks stop inheritance; merges are typed.
- **Tiers:** Locked (law, safety, NN rules), Governed (maker-checker, preview, citation, effective date) and Tenant (immediate, audited, one-click rollback). A tenant admin can change everything in T and propose G changes for their tenant without a super admin.
- **What tenants customise without a super admin:** department and function names and tree (mapped to canonical codes, Appendix U §U.9.0), terminology (board, director, member, by-laws…), question text and actionables (overlay), added checkpoints, owners and backups, internal target dates, interim and waiting sub-statuses, reminder ladders, escalation paths, approval chains (within SoD), notification channels and quiet hours, digest times, dashboards and widgets, saved views, menus (hide, reorder, pin), forms and custom fields, report layouts, branding (contrast-checked), languages, calendar sync rules, AI usage limits, export schedules and storage targets.
- **What only platform content roles change:** base content, rule packs, template contract, canonical statuses and codes.
- **Super-admin overrides:** a super admin can change any tenant setting, component, document pointer, date, entitlement, settings section visibility or audit-trail annotation for a client company, always through a Correction Entry (§6.6) that the tenant can see.
- **Rule engine:** effective-dated rule packs with sandbox, golden cases, impact analysis (which tenants and instances change), scheduled activation and rollback — so a regulator change is handled as data, not a release (NN-34).

---

## 9. Commercial architecture (R-034–R-037, R-044, R-067, R-069–R-070; P20–P22, Appendices N, O, X)

- **Billing ownership (X-02).** The Operations Hub billing engine (OH8) is the system of record for the catalogue, prices, tax, quotes, orders, invoices, credit notes, the group Razorpay merchant account, payments and dunning. LDC presents the pricing page and Apple-style configurator, runs checkout UI, keeps the entitlement mirror, meters usage (AI credits, entities, users, storage, returns, health checks), manages the trial lifecycle and the savings ledger, and shows every billing and membership page in Settings. The LDC Pricing Studio in `apps/console` lets the super admin edit packages, components, prices, discounts, promo codes, trials (including per-company extensions), feature lists and comparison tables; changes are submitted as catalogue change requests to OH8 (maker in LDC, checker in OH8; a second approver is nominated so the owner never approves his own draft, D-28). Until OH8 is live, `bil.billing_port.mode = LOCAL_INTERIM` runs a local adapter with the same contract, approved by the owner.
- **Packages (seed; prices are owner decisions):** three public packages — **Essentials** (small entities), **Professional** (larger entities), **Enterprise** (custom) — each a base price plus add-on components: Labour Codes & HRMS, Risk Lab (ICAAP, stress, capital), Audit, Return Studio, Data Protection & Cyber, Co-operative Suite, Board Portal & Company Secretarial, Grievance Desk, extra legal entities, extra users, AI credits, BYO storage. The live site's Basic ₹10,000/month and Pro ₹30,000/month are the starting reference; final names and prices are set in the Pricing Studio (D-21; Appendix N).
- **Self-onboarding (R-069):** free health check → 7-day trial (a real tenant under click-wrap terms, D-26) → PAN/CIN/GSTIN entry with licensed data pre-fill → regulator and family confirmation → module selection with live price → checkout → users and workflows → first value in under 30 minutes.
- **Revenue streams:** a registry of switchable streams (subscription, add-ons, usage/AI credits, implementation, managed compliance services, retainers, marketplace listing and service fees, training, certification-readiness services, white-label/partner, API access, sponsored content and advertising — each with a kill switch, tax treatment, refund rule and approval gate; Appendix N). Advertising and sponsored listings stay OFF until the owner approves and counsel confirms (NN-20).
- **Savings dashboard (R-067):** hours saved, penalties and late fees avoided, external spend avoided — each figure computed by a published, evidence-backed method with the tenant's own data and shown with its assumptions (NN-19, NN-22).
- **Marketplace (P21):** public, no login to browse; LawDocs services first, third-party professionals later; per-profession commercial switches (D-06); LawDocs as a company does not supply reserved advocacy or attest services in its own name — eligible practitioners contract directly (D-32); services purchasable without a SaaS subscription; retainers with eSigned SLAs; FinLegal Academy courses linked to trainings.lawdocs.in.
- **Retainers and delivery (P22):** the LawDocs RM works inside the client tenant as `ten_maker` with a LawDocs badge through a client-approved delivery grant; the client's employee is checker (NN-43); multiple makers allowed; both the client admin and the LawDocs delivery lead can propose maker users, but only the client admin approves the grant.
- **Never-block (NN-42):** unpaid or expired accounts keep read, export, auditor access, Updates for held packs and grievance intake.

---

## 10. AI layer — Vidhi AI (R-019, R-027, R-097; P17, Appendix K)

Vidhi is the tenant's AI employee: it can be assigned tasks and scheduled jobs, prepares minutes and agendas, drafts policies (with tracked changes against the template or previous version), agreements, reports and ICAAP sections, reads handwriting, screenshots, WhatsApp exports, letters, PDFs and e-mail, produces type copies and translations into English from the six UN languages and the 22 Eighth-Schedule languages, assists compliance testing and stress-test set-up, and answers questions from **knowledge notebooks** — platform-curated notebooks per regulator (NotebookLM-style: sources, citations, summaries, FAQs, study guides, optional audio overviews) and tenant notebooks over the tenant's own documents.

Principles: drafts not decisions (NN-14); citations or an explicit "no source" (NN-06); no AI figures in numbers (NN-37); on-behalf-of a named user with intersected scopes (NN-41); India routing for regulated data (NN-41); human approval gates for every external effect; evaluation harness with golden questions per regulator before a notebook or skill is enabled; metering and limits per plan; deterministic fallback when the model is unavailable (forms and checklists still work). The live site's "Nidhi AI" name is replaced by "Vidhi AI" unless the owner decides otherwise (X-18).

**v1.1 — future-ready agentic architecture (Appendix AA; P17).** Vidhi becomes an **agent workforce**: role agents such as Regulatory Analyst, Compliance Coordinator, Evidence Reviewer, Company Secretary Assistant, Risk Analyst, Audit Assistant, Returns Preparer, Policy Drafter, HR & Labour Assistant, Grievance Triage, Data-Prep, Board-Pack, AI Governance Analyst, Legal Matters Assistant and Sustainability Analyst, each with declared skills, tools, scopes, KPIs and a human sponsor (D-34). Agents run durable, scheduled or event-triggered **missions** on Temporal at autonomy levels L0–L4 configured per tenant, agent, skill and user (NN-50), with kill switches (NN-51), evaluation gates in CI, cost governance through AI credits, and tenant/user/agent memory that respects retention and sealed classes. LDC exposes an **MCP server** so a client's own Claude, Copilot or ChatGPT can query obligations, due items, evidence status, catalogue changes and reports under the user's permissions, and Vidhi uses an **MCP client** to reach approved client systems (D-35; P18 FR-P18-62–73); **A2A** with Finbyx, Udofin, Equator and Operations Hub agents follows once Ecosystem Spec v1.2 approves it (NN-52). Model routing stays provider-neutral (Bedrock India default; open-model sovereign route OFF by default, D-37). Clients get an **AI governance overlay** (`OV_AI`, P12 §4P) with model inventory, AI use-case register, risk classification, impact assessments, fairness evidence and AI incidents mapped to RBI FREE-AI, SEBI, IRDAI, MeitY, EU AI Act, ISO/IEC 42001 and NIST AI RMF; LDC applies it to itself and publishes a vendor AI assurance pack (D-36, D-38).

---

## 11. Integrations (R-002, R-029, R-052, R-063, R-082, R-094, R-098; P18, Appendix L)

The integration gateway provides versioned REST APIs (OpenAPI 3.1), events (AsyncAPI 3.0, CloudEvents), webhooks (Standard Webhooks signatures), OAuth 2.0/OIDC for users, mTLS-bound client credentials for services, scoped API keys for tenants, rate limits, idempotency keys, replay protection, sandbox tenants, a developer portal and connector certification. Ports and first adapters:

| Port | Adapters (candidates; contracts and credentials verified before go-live) |
|---|---|
| `ECOSYSTEM_PORT` | Finbyx, Udofin, Equator, LawDocs, Operations Hub, FinLegal Academy — exactly per Ecosystem Spec v1.1 (§9.1 modes `LDC_EXTERNAL`, `LDC_GROUP`; §9.2 GRC contract; §9.3 native connector) |
| `LENDING_SYSTEM_PORT` | Third-party LOS/LMS/LSP/recovery systems via connector SDK, REST pull/push, CSV/SFTP fallback |
| `ACCOUNTING_PORT` | Tally Prime (read-only XML/JSON export; LDC never writes vouchers), Excel/CSV trial balance, Zoho Books/others later |
| `COMPANY_DATA_PORT` | Licensed MCA company-data providers (e.g., Probe42, Signzy, Surepass, Perfios) — no scraping; anonymous rate-limited lookup with masked output for the health check |
| `IDENTITY_PORT` | PAN verification (Protean/ITD via licensed provider), GSTIN lookup, DigiLocker (licensed partner), Aadhaar offline verification only with OVSE registration; **no credit-bureau pulls** (X-07) |
| `WORKSPACE_PORT` | Microsoft 365 (Graph: calendar, OneDrive, SharePoint, Teams, user provisioning) first; Google Workspace later (D-10) |
| `CALENDAR_PORT` | Graph (work and personal Microsoft accounts), Google Calendar API (Workspace and Gmail), ICS subscription/CalDAV (Apple and others) |
| `STORAGE_PORT` | S3, Azure Blob, GCS, SFTP, OneDrive, SharePoint, Google Drive, on-premises agent for NAS/disks |
| `ESIGN_PORT` | Aadhaar eSign via ASP adapters to CCA-empanelled ESPs; DSC signing for MCA and regulatory forms |
| `MESSAGING_PORT` | E-mail (SMTP/IMAP, e-mail-in), SMS (DLT-registered), WhatsApp Business Cloud API (never for collection, recovery or legal notices), JioCX channels; push |
| `VOICE_PORT` | Jio SIP trunk / CPaaS, Indic speech providers — consented, disclosed, DND-scrubbed, within contact-hour rules |
| `BILLING_PORT` | OH8 billing engine; Razorpay hosted checkout through OH8 |
| `AI_PORT` | Bedrock India (Claude), Anthropic API (non-personal content only), Jio/others behind flags |
| `GRC_EXPORT_PORT` | OSCAL JSON (catalog, profile, assessment results, POA&M) and REST for third-party GRC tools |
| `MCP_SERVER` / `MCP_CLIENT` *(v1.1)* | (Appendix L §L.10) LDC MCP server (OAuth 2.1, scoped tools and resources, sealed data never returned) and MCP client registry for approved client systems |
| `A2A_GATEWAY` *(v1.1)* | Agent-to-agent tasks with ecosystem agents, mapped to Ecosystem contracts; flag OFF until Spec v1.2 |
| `REG_INTEL_PORT` *(v1.1)* | Licensed regulatory-intelligence feeds for foreign jurisdictions and secondary signals (official sources remain primary) |
| `FX_RATE_PORT` *(v1.1)* | Reference rates (FBIL/RBI for INR; central-bank rates per cell) for multi-currency consolidation and pricing |
| `ENTITY_REGISTRY_PORT` *(v1.1)* | Foreign company registries and licensed entity-data providers for global entity management |
| `LITIGATION_DATA_PORT` (alias `COURT_DATA_PORT` in P26), `CONTRACT_REPO_PORT` *(v1.1)* | Court/tribunal case-status data (flag OFF until licensed) and contract repositories for P26 |
| `ESG_DATA_PORT`, `ENERGY_EHS_PORT` *(v1.1)* | Energy, emissions, EHS and supplier ESG data for P27 |
| `ITSM_PORT`, `AI_MONITORING_PORT` *(v1.1)* | Jira/ServiceNow issue sync; AI model monitoring feeds for `OV_AI` |

Onboarding new companies by API (R-002): a partner or group system can create a tenant shell, entity profile and users through the provisioning API with the tenant admin's confirmation step.

---

## 12. Data preservation and portability (R-021, R-076, R-081; P19, Appendix M)

- **LDC-EXPORT-1.0** package: a folder tree that a beginner can understand without LDC — `00 Start Here` (README as PDF, DOCX and TXT; index workbook; manifest; checksums; BSA s.63 certificate), then numbered top-level folders `01 Organisation and Entity Profile`, `02 Regulatory Coverage and Applicability`, `03 Compliance Register and Evidence`, `04 Regulatory Updates and Change Log`, `05 Governance - Board, Committees and Meetings`, `06 Company Secretarial - Registers, Filings and Resolutions`, `07 Policies and Procedures`, `08 Risk Management`, `09 Risk Assessments - ICAAP, Stress Tests and Ratios`, `10 Audits and Inspections`, `11 Returns and Regulatory Reporting`, `12 Data Protection and Cyber Security`, `13 People - HR and Labour Compliance`, `14 Grievances and Customer Support`, `15 Co-operative Society Records`, `16 Tasks, Calendar and Approvals`, `17 Documents Library`, `18 Vidhi AI - Notebooks, Outputs and Activity`, `19 Contracts, Marketplace Engagements and Retainers`, `20 Billing, Subscription and Invoices`, `21 Users, Roles and Access History`, `22 Settings and Customisations`, `23 Integrations and Data Exchanges`, `24 Audit Trail`, *(v1.1)* `25 Global Entities and Jurisdictions`, `26 Legal Matters, Contracts and Licences`, `27 ESG, BRSR and Sustainability`, `28 Reports, MIS and Board Packs`, `29 AI Governance - Systems, Assessments and Incidents`, and `99 Restricted` for sealed-class records exported only with explicit authorisation (Appendix M §M.3 names are authoritative; X-27). Within folders: legal entity → financial year → department → module → record, with self-explanatory names. Files are DOCX, XLSX, PDF/PDF-A, CSV and JSON with schemas.
- **Full, partial and scheduled exports**, to download or to BYO storage (S3, Azure, GCS, SFTP, OneDrive, SharePoint, Google Drive, on-premises agent); backup mirroring to the customer's own bucket.
- **Folder intake:** upload a folder tree or zip; LDC proposes a mapping to checkpoints, policies, meetings and evidence; the user confirms; nothing is silently overwritten.
- **Stability across releases and infrastructure moves:** stable IDs; storage keys opaque and independent of code layout; canonical paths derived from metadata at export time; expand–contract migrations; export-map contract tests and golden exports per release (NN-10, NN-11, NN-45). Moving cloud region, database host or code structure does not change what a customer downloads.
- **Cross-product sharing:** exports and evidence shared with Finbyx, Udofin or other group products only through ecosystem contracts and tenant grants.

---

## 13. Phase plan

### 13.1 Phases

| Phase | File | Core dependencies | Effort (2-week sprints × squad) | Squad | Wave |
|---|---|---|---|---|---|
| P00 Foundations, repository discovery and migration | `phases/P00_…` | — | 5 × 7 *(v1.2: +1 business-ID registry and ledger keyed by ID)* | A Platform | 1 |
| P01 Identity, tenancy, onboarding and access | `phases/P01_…` | P00 | 6 × 8 *(v1.2: +1 API-first onboarding)* | A | 1 |
| P02 Configuration Studio, rule engine and settings | `phases/P02_…` | P00, P01 | 6 × 8 | A (config sub-squad) | 1 |
| P03 Regulatory content library, template registry and Excel import | `phases/P03_…` | P00–P02 | 9 × 8 *(v1.1: RBI catalogue pre-seed, control layer, tracker import, undo; v1.2: +1 CompID generation, v2.0 importer, legacy map)* | B Content & Compliance | 1 |
| P04 Compliance workspace, maker-checker, calendar, tasks, notifications | `phases/P04_…` | P00–P03 | 14 × 9 *(v1.2: +3 for list view, drawer, export builder, RAG radar, conversations and accountability; v1.1: automated checkpoints, testing cycles, notification budget, grid bulk edit)* | B | 1 |
| P05 Regulatory change management and AI question authoring | `phases/P05_…` | P00–P04, P17 sprint 1 | 9 × 8 *(v1.1)* | B | 1 |
| P06 Governance, board, committees and company secretarial | `phases/P06_…` | P00–P04, P13 person master (stub until P13) | 10 × 8 *(v1.1)* | C Governance & Documents | 1 |
| P07 Policy lifecycle and document management system | `phases/P07_…` | P00–P04, P17 OCR/translation | 9 × 8 *(v1.1)* | C | 1 |
| P08 Enterprise risk management and CRO workspace | `phases/P08_…` | P00–P04, P15 | 6 × 7 | D Risk & Reporting | 2 |
| P09 Risk assessment lab: ICAAP, stress testing, capital and ratios | `phases/P09_…` | P08, P11 accounting bridge, P18 | 8 × 8 | D | 2 |
| P10 Audit management | `phases/P10_…` | P00–P07 | 10 × 8 *(v1.1: second-line testing programme)* | C | 2 |
| P11 Return Studio, data preparation and accounting bridge | `phases/P11_…` | P00–P04, P18, returns kernel | 10 × 9 | D | 2 |
| P12 Data protection, cyber, IT governance and TPRM | `phases/P12_…` | P00–P04, P07 | 8 × 8 | B (second track) | 2 |
| P13 HRMS, people and labour compliance suite | `phases/P13_…` | P00–P04, P06, P07, labour rule pack | 12 × 9 | G People & Co-operatives | 3 |
| P14 Grievance redressal and customer support desk | `phases/P14_…` | P00–P04, P07, P13 positions, P18 | 6 × 7 | G | 2 |
| P15 Sector packs and entity logic | `phases/P15_…` | P00–P03 | 7 × 8 | B | 1 (RBI-NBFC, MCA-CO, DATA-PRIV, IFSCA-GEN first) |
| P16 Co-operative society operations suite | `phases/P16_…` | P06, P13, P15 | 6 × 7 | G | 3 |
| P17 Vidhi AI employee, agents and knowledge notebooks | `phases/P17_…` | P00–P04, P07 | 13 × 9 *(v1.1: +5 for agent workforce, autonomy, MCP, memory, CCM)* | E AI | 1 (sprint 1 runtime) → 2 → 3 |
| P18 Integration gateway, ecosystem connectors, developer platform | `phases/P18_…` | P00–P02 | 14 × 8 *(v1.1: MCP server/client, A2A, cells, new ports)* | A | 1 (core) → 2 |
| P19 Data preservation, portability and BYO storage | `phases/P19_…` | P00–P02, P07, P18 | 10 × 7 *(v1.1)* | A | 1 (core) → 2 |
| P20 Pricing, plans, subscriptions, billing, savings, revenue streams | `phases/P20_…` | P01, P02, OH8 or interim adapter | 8 × 8 *(v1.1: multi-currency, new add-ons, AI credits)* | F Commercial & Growth | 1 |
| P21 Marketplace, retainers and FinLegal Academy | `phases/P21_…` | P20, P22, P07 eSign | 9 × 9 *(v1.1)* | F | 3 |
| P22 Service Delivery Console and Operations Hub interface | `phases/P22_…` | P01, P04, P20 | 9 × 8 *(v1.1: practitioner-firm workspace, global delivery)* | F | 3 |
| P23 Public website, health check, help centre, tutorials, accessibility | `phases/P23_…` | P01, P15, P18, P20 | 11 × 7 *(v1.1: locales, country pages, RBI Directions Tracker; v1.2: +1 Health Check Studio)* | F (growth) | 1 |
| P24 Engineering governance, hardening, certification readiness, go-live | `phases/P24_…` | every phase released | 3 × 4 governance track + 4 × 7 per GA, 1 sprint per later re-run | A + security | 1, 2, 3 |
| P25 Global jurisdiction packs, multi-region and partner network *(v1.1)* | `phases/P25_…` | P03, P05, P15, P18, P19, P20, P21, P24 | 10 × 9 | I Global | 4 |
| P26 Litigation, legal matters, contracts, licences and ethics registers *(v1.1)* | `phases/P26_…` | P00–P04, P07, P18 | 9 × 8 | H Legal & ESG | 2 |
| P27 ESG, BRSR, CSR and sustainability *(v1.1)* | `phases/P27_…` | P00–P04, P06, P11, P28 | 9 × 8 | H | 3 |
| P28 Reports, MIS and board-pack studio *(v1.1)* | `phases/P28_…` | P00–P04 (core); P06, P08–P11 (packs) | 9 × 8 | D (core track Wave 1, studio Wave 2) | 1 → 2 |

### 13.2 Order and waves

- **Order:** P00 → P01 → P02 → (P03 → P04 → P05) with P15 alongside P03, P17 sprint 1 alongside P04, P18/P19 core alongside P03–P04, P06/P07 from P04's interface freeze, P20/P23 on the growth squad from P02 → **P24 (GA)**.
- **Wave 1 — "Compliance Core" GA (about sprints S1–S30; v1.1 adds the P28 core track for dashboards and the one-page compliance summary and enlarges P03–P05; v1.2 adds the business-ID registry, API onboarding, CompID generation, the list view, RAG, conversations and accountability: P00 S1–S5, P01 S5–S10, P02 S8–S13, P03 S10–S18, P04 S13–S26 (two sub-teams from S19), P05 S17–S26, P24 S27–S30):** P00–P07, P15 (first four families), P17 runtime, P18 core, P19 core, P20, P23, P24. This is the minimum that lets a Middle-Layer NBFC, a company and an IFSCA entity self-onboard, buy, run compliance with maker-checker, receive regulatory updates, run board meetings and policies, and export everything.
- **Wave 2 — "Risk, Audit, Returns, Data, Legal" (about S18–S40):** P08, P09, P10, P11, P12 (incl. `OV_AI`), P14, P26, P28 studio, the rest of P15, P17 notebooks and agents, P18/P19 full. Return generation ships first for NBFC, ARC and co-operative families; bank, UCB, IRDAI, SEBI and IFSCA return generation stays `ACTIVE_UNVERIFIED` (calendar, evidence, reconciliation and secondary validation only) until a pilot verifies cell maps (X-32).
- **Wave 3 — "People, Co-operatives, Services, ESG" (about S28–S48):** P13, P16, P21, P22, P27, P17 full agent workforce.
- **Wave 4 — "Global" *(v1.1)* (about S40–S54):** P25 — regional cell framework, global entity management, partner portal, first corridor packs (UAE and Singapore, then UK/EU), Arabic right-to-left; P24 run per cell.
- Each wave ends with a P24 run. A phase released after GA re-runs the P24 checklist for its scope.
- **Squads:** A Platform (8), B Content & Compliance (9), C Governance & Documents (8), D Risk & Reporting (9), E AI (9), F Commercial & Growth (8), G People & Co-operatives (9), *(v1.1)* H Legal & ESG (8), I Global (9), plus a standing content team (CS, CA, regulatory writers) that produces Part-2 question sheets and reviews packs. About 250 squad-sprints in total *(v1.1)*. With fewer squads, run waves sequentially and expect roughly 75–90 sprints.

### 13.3 Part 2 (question sheets) runs in parallel

Part 2 is produced in separate Claude chats using `templates/` (v2.0 contract, 27 families plus the Risk and Governance registers, v1.2) and `part2_prompts/`; for RBI families work through `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx` wave by wave (Appendix AB). Sheets are imported through P03 once its importer exits; before that, they are validated with `templates/_validate_templates.py`. P05's AI Question Authoring Studio later runs the same method inside the product (R-085).

---

## 14. Quality, security and performance standards

- **Tests:** unit and property tests (decimal maths, schedules, clocks), integration tests per module, contract tests per API/event and per kernel, acceptance tests (Gherkin, `tests/acceptance/pXX`), NN tests, accessibility tests (axe + manual screen-reader passes on NVDA, JAWS, VoiceOver, TalkBack), golden exports, golden return fixtures, load tests.
- **Performance budgets:** p95 API ≤ 300 ms for reads and ≤ 600 ms for writes at 200 concurrent users per tenant (P00 FR-P00-50; P24 confirms); dashboards < 2 s at p95 with 50,000 compliance instances per tenant; configurator recalculation ≤ 150 ms; health check page LCP < 2.5 s on 4G; export of a 5 GB tenant completes within 2 hours.
- **Availability:** 99.5% monthly for LDC (Ecosystem Spec §3.8); RPO ≤ 15 minutes and RTO ≤ 4 hours for production [REC; P24 confirms]; DR drill twice a year.
- **Security:** §5.5 and Appendix Q; vulnerability fix SLAs follow OH13 — Critical 72 hours, High 7 days, Medium 30 days, Low 90 days.
- **Accessibility:** NN-21.
- **Content quality:** every checkpoint passes the Appendix E validator and the Part-2 QA checklist; a [VERIFY] marker blocks publication.

---

## 15. Definition of Done (every story)

1. Acceptance criteria pass, including negative and permission cases.
2. NN tests touched by the story pass; no new NN exception.
3. Settings registered with tier, default, bounds and approver (OP-2).
4. Events, error codes and approval actions registered (Appendix B, Appendix A).
5. Record types mapped in `xpt.export_map`; golden export diff clean (NN-10, NN-45).
6. Audit ledger entries written in the same transaction (NN-45).
7. Screens have "i" help keys, empty/error states and pass WCAG 2.2 AA checks (NN-21).
8. Tenant isolation tests updated (NN-01).
9. Documentation: API reference, user help article, release note, runbook entry where operational.
10. Open items closed or recorded with owner, fallback and flag.
11. *(v1.1)* Datasets and KPIs registered in the P28 semantic layer; widgets reference KPI/dataset IDs only.
12. *(v1.1)* Imports and bulk actions have an undo path (NN-49); compliance-type records carry act, evidence and approval dates (NN-48).
13. *(v1.1)* AI skills declare scopes, autonomy ceiling, eval set and kill-switch behaviour (NN-50, NN-51); MCP tools added for new read models where useful.
14. *(v1.1)* Strings externalised for localisation; dates, currencies and calendars locale- and cell-aware.

---

## 16. Source materials (consult; do not copy blindly)

- The owner's **LawDocs Comply Architecture Parts 1–3** (visual identity, components, navigation, screens, onboarding wizard, forms, statutory registers, minutes, ROC, company types, LLP, secretarial function map, listed-company governance, IT and ESG governance, risk registers, TPRM, privacy and DPDP rule map, audit engagement) — the functional baseline; the pack corrects it where noted (for example MBP-1 is a disclosure form, not a register; DPT-3 is a return, not the register of deposits; colour tokens; "bulk approve").
- The owner's earlier **LawDocsComply Master Build Prompt** (25 Oct 2026) — absorbed into this pack.
- The owner's Excel samples and the 43 finished IFSCA question sheets (IFSCA Documents folder) — the method for Part 2 and the canonical IFSCA vocabulary (Appendix E).
- Infrabyx Ecosystem Integration Specification v1.1; Finbyx v1.5; Udofin v1.2; Operations Hub v1.0; Equator v3.1 (patterns only).
- *(v1.2)* `templates/` v2.0 workbooks, `templates/_validate_templates_v2.py`, and the synthetic samples in `templates/samples/` (working-register Excel and grouped PDF list export).
- *(v1.1)* `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx` (the RBI content base, D-39); Appendix AC (traceability of every baseline section and brief item to the pack); Appendix Z backlog; Appendix Y Lawrbit analysis.
- Primary legal sources as cited in each phase file §15 and Appendices F, G, I, J.

---

## 17. Glossary (short; the full glossary is the "i" registry, P23 and Appendix P)

**Checkpoint** — one actionable row of a question sheet. **Compliance instance** — a checkpoint for a period, entity and owner. **Overlay** — a tenant's change to base content. **Pack** — a set of instruments and rules for a family or overlay. **Family** — an entity category with its own logic (P15). **Correction Entry** — the only way to change a recorded value (§6.6). **Updates / Notifications** — regulatory inbox / work inbox (NN-27). **RE** — regulated entity. **SBR** — RBI Scale Based Regulation for NBFCs (Base, Middle, Upper, Top layers). **ICAAP** — Internal Capital Adequacy Assessment Process (Pillar 2). **RCSA** — risk and control self-assessment. **KRI** — key risk indicator. **RBIA** — risk-based internal audit. **CIMS / DAKSH / PRAVAAH** — RBI's supervisory data, supervisory workflow and regulatory application portals. **CIC** — credit information company (TransUnion CIBIL, CRIF High Mark, Experian, Equifax). **GRO / PNO / IO** — grievance redressal officer / principal nodal officer / internal ombudsman. **SDD** — structured digital database under SEBI PIT. **ESP / ASP** — eSign service provider / application service provider. **OH** — Infrabyx Operations Hub. **Vidhi AI** — LDC's AI employee and agent workforce. *(v1.1)* **Compliance Score** (P04) — completion and timeliness of a tenant's compliance instances; **Health Check Score** (P23) — result of the free health check; **Set-up Readiness Score** (P01) — onboarding completeness; **Compliance Health Index** (P28) — weighted board-level index (40/20/15/15/10). **Autonomy level** — L0–L4 ceiling for AI actions. **MCP** — Model Context Protocol. **A2A** — Agent2Agent protocol. **Jurisdiction pack** — country content pack. **Linked tenant** — a tenant in another regional cell that belongs to the same group. **Act date** — the date an obligation was actually performed. *(v1.2)* **CompID / RiskID / GovID** — permanent business IDs for a compliance checkpoint, a risk and a governance item. **List view** — the 9-column yellow group. **CompID drawer** — the pop-up with the item's full detail. **RAG** — Red/Amber/Green urgency (plus Grey, Blue). **Explanation request** — a typed conversation message that asks the holder of an item to explain a delay, with an SLA. **Accountability file** — the computed timeline, assignments, explanations and decisions for an item.

---

## 18. Document precedence and cross-file resolutions (binding)

**Precedence on conflict:** this file → `02` → Appendix G (law) → Appendix E (template contract) → *(v1.1)* Appendix AA (AI architecture) and Appendix Y (global) for their domains → Appendix B (names, codes, DDL) → Appendix A (states) → Appendix D (access) → Appendix U (settings tiers and keys) → Appendix C (menus, screens, tokens) → the phase file → other appendices. The Ecosystem Integration Specification v1.1 prevails over all of these for cross-product contracts; a conflict is raised as a change request (§19), not resolved locally.

| ID | Resolution |
|---|---|
| X-01 | **Event names.** Cross-product: `in.infrabyx.<domain>.<EventName>.v<major>` (Ecosystem Spec §3.2), published only by `int`; internal and tenant webhooks: `in.lawdocscomply.<module>.<EventName>.v<n>`; mapping in `int.event_type_map`. Supersedes `_conventions.md` §8. |
| X-02 | **Billing ownership.** OH8 owns catalogue, prices, tax, quotes, orders, invoices, credit notes, Razorpay and dunning; LDC `bil` owns presentation, configurator rules, entitlement mirror, meters, trial lifecycle, savings ledger and billing UI; Pricing Studio submits change requests to OH8; interim local adapter only with owner approval. Supersedes the `bil` description in conventions and any phrasing in P20/P21/N that implies LDC issues invoices itself. |
| X-03 | **AI residency.** Claude via Amazon Bedrock India geographic cross-Region inference is the default for any personal, confidential, financial, legal or HR data; Anthropic API (global) only for public or non-personal content or with a recorded cross-border basis (amends D-14; NN-41). |
| X-04 | **eSign terms.** Aadhaar eSign through CCA-empanelled ESPs via ASP adapters (Leegality, Digio, SignDesk, Surepass, Protean); DSC for MCA and regulatory forms (amends D-20). |
| X-05 | **Hosting.** Production on AWS ap-south-1/ap-south-2 with S3 Object Lock; Supabase PostgreSQL for non-production and beta only; Railway decommissioned (amends D-01). |
| X-06 | **Office editing.** No promise of embedded Office-for-the-web editing (WOPI needs Microsoft's Cloud Storage Partner Program); default is Graph co-authoring in the tenant's own SharePoint/OneDrive; optional self-hosted WOPI editor behind a flag after a P00 licence ADR. |
| X-07 | **No credit-bureau pulls at onboarding or in the health check.** LDC is not a specified user under CICRA 2005 for SaaS onboarding [INTERP; counsel to confirm]; the "CIBIL" requirement is met by preparing the client's own CIC submission files (P11); tenants may upload their own reports. |
| X-08 | **Multi-value delimiter** in multi-select cells (v2.0 keys `applic_layer`, `applic_type` and any family extension marked multi-select) is `"; "` (as in the owner's 2,809 finished IFSCA rows); the importer also accepts `" \| "`, `","` and line breaks and normalises them. `" \| "` remains the separator inside `weblinks`. *(v1.2: the v1.0 references to columns C/D/N apply only through the legacy map in Appendix E Part B.)* |
| X-09 | **Family and template codes.** P15 entity-family codes (`BANK`, `UCB`, `RCB`, `NBFC`, `ARC`, `AIFI`, `PAY`, `CCS`, `COOP`, `IFSC`, `MF`, `AIF`, `LISTED`, `REIT_INVIT`, `SEBI_INT`, `INSURER`, `INS_INT`, `COMPANY`, `LLP`, `SOCIETY`, overlays `OV_*`) map to the template codes of Appendix E as shown in §1.2 (24 in v1.0; 27 in v1.1 with INTL-GEN, AI-GOV and ESG-BRSR, X-51); template files are named `LDC-TPL-<FAMILY>-v1.0 - <Name>.xlsx`. Data-intake templates use `LDC-DT-<AREA>` (P11 owns the common set — e.g., `LDC-DT-TB`, `LDC-DT-LOAN`, `LDC-DT-INVEST`, `LDC-DT-CAPITAL`; P09 adds `LDC-DT-RAL-LOANSEG`, `-HQLA`, `-OBS`, `-INS`, `-COOP`; P08 `LDC-DT-KRI`; P12 `LDC-DT-ROPA`; one upload feeds both Return Studio and Risk Lab). |
| X-10 | **Departments.** Template `department` values (v1.0: column M) map to canonical codes per Appendix U §U.9.0 (22 base codes + 12 added: CLM, KYC, ICP, INV, MKT, PRL, PRD, SRV, TAX, TRS, UND, VAL). |
| X-11 | **Statuses.** §6.3 canonical set; the `status` column (v1.0: column J) is blank in templates. |
| X-12 | **Supervisory returns erratum** as in §7; content and P11 cite the 31 Jul 2026 DoS directions. |
| X-13 | **Shells.** `tenant`, `board`, `assurance`, `selfservice` are route groups in `apps/web`; `provider` is an authenticated shell in `apps/public`. |
| X-14 | **Correction Entry scope** per §6.6 and NN-02: never ledger events or sealed content; invoices by credit note. |
| X-15 | **Trials** are real tenants under click-wrap terms with a DPA (and RE addendum where relevant); trial data is deleted 30 days after expiry unless converted or exported (D-26; needs OH acceptance because OH8.9 assumes sandbox trials). |
| X-16 | **Host switches.** `ral.icaap.host` (LDC default; FINBYX for Finbyx EMBEDDED mode), `aud.host.mode` (`LDC_NATIVE`, `FINBYX_HOSTED`, `HYBRID`, with `owner_system` on every engagement and finding), `coop.sor.members` (`FINBYX`, `LDC`, `EXTERNAL_LOS`), `ral.stress.fx_mode` (`CONSUME_ONLY` until the Finbyx stress-run API exists). |
| X-17 | **Retainer RM** = `ten_maker` scoped by a delivery grant, badge "LawDocs"; never checker, approver or admin (NN-43). |
| X-18 | **Names.** "Vidhi AI" (live site's "Nidhi AI" renamed; owner to confirm); packages Essentials / Professional / Enterprise (live site Basic / Pro / Custom; old URLs 301-redirected); "FinLegal Academy" vs the live "LawDocs Trainings" — owner decision. |
| X-19 | **Added roles:** `plt_web_editor`, `plt_web_publisher`, `ten_integration_admin`, `ext_developer`, `ia_contributor` (co-sourced audit expert without report ownership). |
| X-20 | **Design tokens.** Owner gold #C9A961 and amber #D97706 fail text contrast; use text variants Gold-700 #8A6D2B and Amber-700 #B45309, placeholder grey #64748B, two-tone focus ring navy #0A2540 + gold (Appendix C §C.8). |
| X-21 | **Public site SSR.** `apps/public` is server-rendered/static; all 15 existing sitemap URLs kept or 301-redirected; CI checks primary content without JavaScript (NN-44). |
| X-22 | **Live-site claims.** Remove "ISO 27001 certified" and similar claims until evidenced (NN-19); P00 FR-P00-04 lists them. |
| X-23 | **WhatsApp** is never used for debt collection, recovery or legal notices. |
| X-24 | **Calendar authority** (NN-07): LDC dates win; external edits reverted. |
| X-25 | **Shared kernels** per §2.2; Finbyx keeps its own tenants' computations (NN-39). |
| X-26 | **Shared packages** per OP-1; shell-level screens SCR-RPT-01 (role home dashboards), SCR-WF-00 (Work Inbox) and SCR-CORE-21 (global search) are owned by P04; SCR-CORE-20 (command palette) by P02/P04; SCR-CORE-22 (context switcher) by P01 (Appendix C §C.9). |
| X-27 | **Export folder names** are those of Appendix M §M.3 (00–24, 99); other files referring to export folders use them. |
| X-28 | **Optional `_LDC_System` sheet.** Templates carry `_Template_Info` (D-08); LDC exports may add a hidden `_LDC_System` sheet with structured due rules, applicability expressions and version ids; it is never required on upload (owner to confirm; OI-P03-01). |
| X-29 | **Structured data in the template** *(amended v1.2)*. Contract v2.0 gives each datum its own column: due-date rule in `due_rule`, change status in `change_status` (rows are never deleted; retired rows carry `Retired`), CompID in `comp_id` in the format of §6.7 (`<AUTH>-<FAM>-<INST>-<NNNN>`, tenant rows `T<TENANT4>-…`), assigned by the platform on publish (NN-56). `[VERIFY]` in any cell blocks publication (Appendix E). The v1.0 conventions (`Due:` in column P, `[RETIRED] ` prefix in column F, `<FAMILY>.<INST>.<NNNN>` in column E) are read only by the legacy importer and rewritten to v2.0 on import. |
| X-30 | **Marketplace eligibility.** Internal-audit offers to RBIA-bound REs are co-sourced only (`ia_contributor`); full outsourced IA only where the law permits; an Infrabyx-linked PCS is not offered as secretarial auditor of a listed retainer client (LODR Reg 24A; counsel to confirm); "virtual CCO/IA" for RBI REs is support, never the outsourced core function. |
| X-31 | **Borrower tax certificates** stay with the RE through Finbyx/Udofin; LDC prepares GST/TDS packages only for tenant entities (narrows R-079). |
| X-32 | **Return generation scope in v1** as in §13.2. |
| X-33 | **Consent Manager:** LDC does not register; integration readiness only, flag OFF. |
| X-34 | **Co-operative elections** are conducted by the election authority; LDC supports and records. |
| X-35 | **Bulk approval** prohibited per NN-46. |
| X-36 | **People-risk metrics** leave P13 only as aggregates with k ≥ 5 suppression; POSH as counts only. |
| X-37 | **MBP-1** is a disclosure (s.184(1), Rule 9) with an index; the register of contracts is MBP-4 (s.189); the register of deposits (Acceptance of Deposits Rules r.14) is distinct from the DPT-3 return. |
| X-38 | **Canonical IFSCA vocabulary** is the owner's Appointed Actuary sheet `Rough` (11 frequencies, 40 entity types, 10 filing tokens); the older "Format for Question Final" list is not used. |
| X-39 | **Hindi** is the second locale for the health check, glossary, solution pages and help (D-30); further Indian languages by demand. |
| X-40 | **AI-crawler policy** default `ALLOW_PUBLIC_MARKETING` (public marketing pages only; owner may change; D-31). |
| X-41 | **Tally direction:** read only; LDC never writes vouchers to Tally. |
| X-42 | *(v1.1)* **Partner roles** are `prt_admin`, `prt_content_author`, `prt_content_reviewer`, `prt_delivery_professional`, `prt_viewer`; earlier names in P25/Appendix Y (`prt_author`, `prt_reviewer`, `prt_expert`) are aliases. |
| X-43 | *(v1.1)* **Reporting ownership.** Module `rpt` and `packages/dashboards` belong to P28; SCR-RPT-01/02 are owned by P28 and hosted on P04's home route; amends X-26. |
| X-44 | *(v1.1)* **Related-party transactions** in P06 use `gov.rpt_txn_*` and the label "RPTx", never the module code `rpt`. |
| X-45 | *(v1.1)* **AI identifiers:** agent principals `agp_`, delegation grants `adg_`, agent runs `agt_`. |
| X-46 | *(v1.1)* **Four distinct scores:** Compliance Score (P04), Health Check Score (P23), Set-up Readiness Score (P01), Compliance Health Index (P28); never shown under a bare "score" label. |
| X-47 | *(v1.1)* **Export folders 25–29** as in §12 (Appendix M authoritative, additive only; export profile 1.1.0). |
| X-48 | *(v1.1)* **Regulator inspections, observations and proceedings** are P26 records; P10 holds read projections for audit planning. |
| X-49 | *(v1.1)* **Board packs:** the meeting book (notice, agenda, item papers, portal) stays in P06; analytic sections and frozen packs come from the P28 pack studio as item papers. |
| X-50 | *(v1.1)* **Cross-cell entities** live in linked tenants (NN-24); group views aggregate across cells. |
| X-51 | *(v1.1, amended v1.2)* **Templates** are 29 under contract v2.0: 27 compliance families (24 + INTL-GEN, AI-GOV, ESG-BRSR) plus the RISK and GOV register templates (D-57). Run `templates/_validate_templates_v2.py` with both owner samples; family codes PFRDA, MSME_FIRM and AML_RE are reserved. |
| X-52 | *(v1.1)* **RBI counts:** cite "238 (press release) / 244 serials, 240 live" as in §7; NBFC consolidated directions = 35; catalogue = 320 rows (D-39). |
| X-53 | *(v1.1)* **Kill-switch drills** quarterly at platform level for all tenants; tenant-level drills for Enterprise (NN-51). |
| X-54 | *(v1.1)* **Tracker import** screen is SCR-CNT-16 (P03), launched from P01 onboarding; SCR-IAM-69 is an alias. |
| X-55 | *(v1.1)* **New data class** `LEGAL_PRIVILEGED` (key separation like BOARD_CONFIDENTIAL; excluded from grants and AI for non-legal users); Ecosystem CR raised. |
| X-56 | *(v1.1)* **IFSCA** entity list has 40 types (owner's Appointed Actuary sheet vocabulary, X-38). |
| X-57 | *(v1.1)* **Baseline corrections:** Ind AS 37 classes follow the standard, not fixed probability bands; BRSR value-chain scope per SEBI's 28 Mar 2025 circular (2% partner threshold). |
| X-58 | *(v1.1)* **Department codes** `ESG`, `LEGL` added and used by P26/P27 and ESG-BRSR; `AIG` reserved for tenants that create an AI governance department (AI-GOV `department` values map to DPR, ISEC, PRD, IA). |
| X-59 | *(v1.1)* **Support SLAs** have one source — the OH6 SLA table — shown in P20 plans and P22 delivery. |
| X-60 | *(v1.1)* **Work Inbox** is SCR-WF-00 everywhere (SCR-CMP-02 retired). |
| X-61 | *(v1.2)* **Template contract v2.0** supersedes the 30-column contract (D-08 → D-49); all references to `LDC-TPL-<FAMILY>-v1.0` mean the legacy template, imported through the legacy map; Excel column letters are never used as identifiers — machine keys are (Appendix E). |
| X-62 | *(v1.2)* **Date order rule** per row: instrument issue date ≤ Actionable Last Updated On ≤ Instrument Last Amended On ≤ today; where the instrument was never amended, the amended date repeats the issue date and the importer reads equal dates as "not amended" (D-58). |
| X-63 | *(v1.2)* **One ID registry** in `core` (Appendix B §B.12); P03, P06, P08 and P09 tables that mention IDs are views or projections over it. |
| X-64 | *(v1.2)* **Risk taxonomy codes** in RiskIDs and the Risk Register template are those of Appendix H (e.g., `MOD` for model risk, legal risk within `CMP`); `AIG` is provisional until Appendix H adds it. |
| X-65 | *(v1.2)* **RAG colour tokens** are those of Appendix C §C.8.1A (icon + word + pattern; darker red for chips because `color.danger` on `color.danger.bg` measured 4.04:1). |
| X-66 | *(v1.2)* **Default export columns** = list view + Next Due + RAG + Maker; exports are ledger events for every CompID included (NN-57). |

---

## 19. Changes required in companion documents

**Ecosystem Integration Specification v1.2 change requests (Spec §14.2), raised in P00 and tracked in `docs/ecosystem/change-requests.md`:** (1) §9.3 — LDC stack is NestJS/PostgreSQL, not "Node, TypeScript, MongoDB"; (2) data classes SEALED, BOARD_CONFIDENTIAL, CREDENTIAL, REGULATOR_CONFIDENTIAL; (3) supervisor grantee and basis codes for SEBI, IRDAI, IFSCA, CRCS/State RCS in §4.7; (4) `RiskSegmentSnapshotPublished` event and Finbyx `POST /v1/risk/stress-runs`; (5) evidence-request API for audit (`POST /v1/evidence-requests`); (6) LDC as producer of `FinancialStatementsApproved`, `Return*` and `Bureau*` events for non-Finbyx tenants; (7) about twelve Operations Hub contracts listed in Appendix X §X.12 (`TenantSelfServeCreated`, trial events, `CatalogueVersionPublished`, `CatalogueChangeRequestUpdated`, `ServiceCreditIssued`, `ClientHealthSignal`, `TimesheetAggregated`, `DeliveryMetricsMonthly`, `POST /v1/crm/activities`, `POST /v1/delivery/assignments`, `POST /v1/trials/extensions`, `POST /v1/conflicts/check` for LDC, `POST /v1/catalogue/change-requests`); (8) co-operative member contracts when `coop.sor.members = LDC` (§6.24 producer).

*(v1.1)* Further change requests: (9) `dataregion` residency attribute on every cross-product event; (10) A2A transport, agent identity and delegation tokens for ecosystem agents; (11) `LegalMatterExposureSummarised`, `RegulatorObservationOpened`, `RegulatorObservationClosed` (LDC producer); (12) `FinancedEmissionsAggregatePublished` (Finbyx producer) for P27; (13) data class `LEGAL_PRIVILEGED`; (14) the v1.1 Operations Hub contracts in Appendix X (practitioner-firm accounts, partner network, multi-currency catalogue, AI-credit metering).

**Finbyx addendum:** respect `ral.icaap.host`, `aud.host.mode`, the returns and risk kernels, and `coop.sor.members`.

**Operations Hub addendum:** Appendix X (v1.1 rows added for global delivery, partners, practitioner firms and AI credits) (LDC workspace, CRM objects, onboarding playbooks, CS signals, ticket routing, health-check leads, catalogue items, RM roles, cross-company roles, trial acceptance, second pricing approver).

---

## 20. Management decisions

The decisions of 25 October 2026 (D-01–D-21 as amended by X-03–X-05), the decisions added by this pack (D-22–D-33), the v1.1 decisions (D-34–D-48), the v1.2 decisions (D-49–D-58), the owner decisions still pending and the twelve recorded challenges to the brief are in `02` §2–§4. They bind every phase.


# PART B — DECISIONS, CHALLENGES AND OPEN ITEMS


> Paste after `01_MASTER_PROMPT.md` at the start of every phase session. This file records what management asked for (R-IDs), what was decided (D-IDs), where the brief was challenged and why, what is still open, and where each requirement is built.

---

## 1. Purpose and sources

The management brief of 25 October 2026 (the "brief") asked for a build prompt for LawDocsComply as a complete GRC SaaS within the Infrabyx ecosystem, in two parts: Part 1, the tool; Part 2, Excel question sheets produced separately and uploaded into the tool. This log converts the brief into 102 numbered requirements (§8), records the owner's answers to the eight planning questions asked the same day (D-01–D-08), the defaults adopted for unanswered points (D-09–D-21), the decisions this pack adds after research (D-22–D-33), and the challenges to the brief (§3). *(v1.1)* adds R-103–R-111 and D-34–D-48; *(v1.2)* adds R-112–R-127 (the template and workflow rework instruction of 25 October 2026), D-49–D-58 and NN-56–NN-60.

---

## 2. Decisions

### 2.1 Decisions taken by the owner on 25 October 2026 (planning questions)

| ID | Question | Owner's choice | Notes and later amendments |
|---|---|---|---|
| D-01 | Technology base | Ecosystem stack: Next.js 16 + NestJS 11 modular monolith + PostgreSQL with RLS, India region; migrate the live MongoDB app by script | Amended by **X-05**: production on AWS RDS/Aurora ap-south-1 with ap-south-2 DR and S3 Object Lock; Supabase PostgreSQL for non-production/beta only (no Hyderabad region, no Object Lock); Railway decommissioned |
| D-02 | Super-admin edits to audit trail, dates and proof | Correction entries: overrides allowed only as reason-coded, dual-approved Correction Entries; originals sealed, tenant-visible | Implemented in P00 (`core.correction_entries`), P02 §4O, Appendix A §A.5; NN-02 |
| D-03 | Operations platform | Group Operations Hub for CRM, marketing, staff HRMS/payroll/appraisal, controls, billing; LDC Service Delivery Console for RMs | Appendix X (OH addendum); P22 |
| D-04 | Client portal credentials | Encrypted vault in the client tenant, client-owned, per-credential grants, MFA reveal, logs, RBI portals client-only by default | NN-17; P22 |
| D-05 | Return engine location | Shared returns kernel; LDC Return Studio for non-Finbyx clients; consume Finbyx return runs for Finbyx clients | Named `@infrabyx/returns-kernel` + `infrabyx-returns-packs`; extended to accounting-framework resolver and Schedule III maps; NN-39 |
| D-06 | Marketplace monetisation | Per-profession switches; listing/subscription fees; disclosed platform fee for LawDocs-run services; % commission OFF by default for advocates, CAs, CSs, CMAs | NN-20; Appendix O |
| D-07 | Pack format | Both: Equator-style pack and Finbyx-style Master Prompt + Phase Runbook (md + docx) | This pack |
| D-08 | Excel template strictness *(superseded by D-49 in v1.2)* | Same 30 columns (A–AD), rows 1–2 unchanged, `Rough` lists with named ranges, family-specific dropdowns, protected `_Template_Info` sheet | NN-35; Appendix E; 24 templates in v1.0, 27 in v1.1 (X-51) |

### 2.2 Defaults adopted for points the owner did not decide (reversible)

| ID | Default |
|---|---|
| D-09 | References in the brief to "Udofin" (role statement), "Equator CRM", "dispute resolution platform", "petition/claim" and "neutrals" are carried over from earlier briefs and read as LawDocsComply equivalents (evidence, grievances, regulator correspondence, clients). |
| D-10 | "Microsoft 365 Business Starter" is not a Microsoft plan (Business Starter is a Google Workspace edition). LDC is suite-neutral (`WORKSPACE_PORT`), Microsoft 365 first (Business Basic/Standard/Premium), Google Workspace later; features that depend on the plan (Teams transcripts, `Sites.Selected`, retention labels, Intune device checks for vault reveals) are gated by a capability matrix. **Owner to confirm the plan held.** |
| D-11 | Client payroll computes, approves and produces bank bulk-payment files or payout-partner instructions; LDC never holds salary money. |
| D-12 | Regulator/supervisor read-only view as a tenant-initiated, time-boxed grant (NN-18). |
| D-13 | Portal filings prepared and validated in LDC, submitted by a human (NN-08). Extended to DPB, CERT-In, DAKSH incident module, IFSCA cyber mailbox, SEBI incident reporting, EPFO/ESIC/State labour portals, SCORES and Bima Bharosa. |
| D-14 | AI via provider adapter; Claude primary; Jio and others as adapters; no training on tenant data. **Amended by X-03:** Claude via Amazon Bedrock India geographic cross-Region inference for regulated data; Anthropic API (global) for non-personal content only. |
| D-15 | Health check is an indicative self-assessment. |
| D-16 | Co-operative credit operations in Finbyx; LDC runs governance, membership, elections support, meetings, complaints, registers, returns and GRC. Extended by D-23. |
| D-17 | AI output never auto-publishes. |
| D-18 | Regulatory scan at 20:00 IST daily plus intraday feeds; regulatory digest 20:30 IST. |
| D-19 | Jurisdiction-pack framework; India first; international packs only with a sourced pack and a named in-country reviewer. |
| D-20 | eSign through licensed providers and DSC. **Amended by X-04** (ESP vs ASP terminology). |
| D-21 | Pricing data-driven and editable in super admin. **Amended by X-02** (OH8 is the billing system of record). |

### 2.3 Decisions added by this pack (25 October 2026)

| ID | Decision | Why |
|---|---|---|
| D-22 | Shared `infrabyx-risk-kernel` (metric formulas, capital rule packs, ALM maths, PCA thresholds, stress primitives) in `infrabyx-contracts`, version-pinned per run | Prevents Finbyx and LDC computing the same ratio differently; mirrors D-05 |
| D-23 | `coop.sor.members` ∈ {FINBYX, LDC, EXTERNAL_LOS}; for non-credit societies LDC is the member/share register and emits the Ecosystem §6.24 contracts | Non-credit co-operatives have no Finbyx book but need registers |
| D-24 | Billing ownership per X-02 (OH8 system of record; LDC presentation, entitlements, meters, trials, savings, UI; Pricing Studio change requests) | Ecosystem Spec §6.27 and OH v1.0 already make OH8 the single revenue ledger |
| D-25 | No credit-bureau pulls by LDC for onboarding, profiling or the health check (X-07) | LDC is not a specified user under CICRA 2005 for this purpose [INTERP; counsel to confirm] |
| D-26 | **Proposed:** trials are real production tenants under click-wrap terms + DPA (+ RE addendum), deleted 30 days after expiry unless converted or exported | The owner wants users to "experience the tool"; a sandbox cannot hold their own data. Needs owner and OH acceptance (OH8.9 assumes sandbox trials) |
| D-27 | **Open:** one or two selling entities (SaaS vs services) and merchant of record for marketplace services | Tax, invoicing and liability depend on it |
| D-28 | **Open:** nominate a second pricing approver so the owner never approves his own Pricing Studio draft | Maker ≠ checker (NN-05) |
| D-29 | LDC does not register as a DPDP Consent Manager (Rule 4 requires an Indian company with ≥ ₹2 crore net worth acting solely for Data Principals, which conflicts with serving REs); integration readiness only | Conflict of role |
| D-30 | Hindi is the second locale for the health check, glossary, solution pages and help [REC] | Co-operative and small-NBFC market reach |
| D-31 | AI-crawler policy default `ALLOW_PUBLIC_MARKETING` [REC; owner may change] | GEO visibility without exposing product content |
| D-32 | LawDocs (a company) does not supply reserved advocacy or attest services (legal representation/advice as advocates; statutory, secretarial, tax or IS audit; certifications) in its own name; eligible practitioners contract directly; CA listing OFF by default (ICAI announcement of 23 Oct 2019 on aggregators) [INTERP; counsel to confirm] | Advocates Act/BCI Rules and professional-body codes |
| D-33 | No bulk approval of maker-checker items with legal effect, money or access (NN-46), replacing the owner baseline's "bulk approve" | A bulk click is not a review; regulators test maker-checker evidence |


### 2.4 Decisions added in v1.1 (25 October 2026)

| ID | Decision | Why |
|---|---|---|
| D-34 | Vidhi agent workforce of role agents; every agent at autonomy L2 or above has a named human sponsor | Future-ready AI with accountability (Appendix AA) |
| D-35 | LDC MCP server first (read and draft tools under user permissions), MCP client second; A2A after Ecosystem Spec v1.2 approval | Lets clients' own AI assistants use LDC safely; protocol-native |
| D-36 | AI governance overlay `OV_AI` built in P12 with template family AI-GOV | Regulated clients now face AI governance expectations (RBI FREE-AI, MeitY, EU AI Act, ISO 42001) |
| D-37 | Sovereign/on-prem AI route (open models) as an adapter, OFF by default | Future data-sovereignty demands |
| D-38 | LDC applies `OV_AI` to itself and publishes a vendor AI assurance pack | Trust and procurement readiness |
| D-39 | The RBI content base is the 28 Nov 2025 consolidated directions (238 press-release count / 244 serials, 240 live) with later amendments, plus the DoS set of 31 Jul 2026, the CEPD Internal Ombudsman directions and RB-IOS 2026; the 320-row catalogue is pre-seeded with placeholder items until sheets are uploaded | Owner's instruction: only these directions are uploaded |
| D-40 | One question sheet per direction per entity category, with sibling links and category-specific applicability for shared checkpoints | Common directions across RE categories |
| D-41 | LDC owns legal matters, litigation, regulator inspections and observations, contracts, licences and ethics registers (P26); Finbyx Recovery Suite/Udolex owns lender debt recovery | Baseline litigation module was missing |
| D-42 | Regional cells: India live; EU, GCC/UAE, Singapore, US on demand; home region chosen at onboarding; linked tenants for cross-cell entities | Global expansion with residency |
| D-43 | Global rollout stages G0–G5 (Appendix Y) | Sequenced, evidence-led expansion |
| D-44 | Partner network for foreign content and delivery; fee, referral and revenue-share models switched on per country only after local counsel | Lawrbit-style coverage without professional-rule breaches |
| D-45 | Pack lifecycle DRAFT → PILOT → PUBLISHED → DEPRECATED | Safe introduction of new jurisdictions |
| D-46 | Saudi personal data deferred; China limited to non-personal entity calendars | Data-transfer and localisation risk |
| D-47 | New phases P26, P27, P28; P28 owns `rpt`; P06 related-party naming `gov.rpt_txn_*` | Missing modules from the baseline audit (Appendix AC) |
| D-48 | New module codes `gem`, `prt`, `lit`, `esg`, `aig` and the new roles listed in master §1.4 | Ownership clarity |

### 2.5 Decisions added in v1.2 (25 October 2026: Excel template and workflow rework)

| ID | Decision | Why |
|---|---|---|
| D-49 | **Template contract v2.0** replaces the 30-column v1.0 contract (supersedes D-08; NN-35 amended). 62 base columns in eight colour-coded, collapsible groups (LIST VIEW yellow, SOURCE & VERSION, APPLICABILITY with 0–4 family extension columns, COMPLIANCE DETAIL, MAKER, CHECKER, AUDITOR, SYSTEM); sheets `Compliance Register`, `Lists`, `Read Me`, `_Template_Info`; machine keys; v1.0 sheets accepted through the legacy map (Appendix E Part B) | The 30-column sheet could not be read on one screen, printed or exported; owner asked for more columns, instrument name, per-question update date and family-specific dropdowns |
| D-50 | **List view = 9 columns** (S. No., CompID, Compliance Question / Actionable, Clause / Para No., Department, Due Date & Frequency, Date of Compliance, Status, Risk Category) plus computed chips Next Due, Days to Due, RAG; every other field in the CompID drawer | Owner's 8–9-column list; risk category added because it drives RAG and sorting |
| D-51 | **Business reference IDs**: CompID, RiskID, GovID and AUD-, LIT-, ESG-, AIS-, KRI-, CTL-, HC-SET-, EXP-, LPH- IDs; human-readable, immutable, never reused; one registry in `core` (Appendix B §B.12) | Audit trail, conversations, bookmarks and exports need stable, quotable keys |
| D-52 | **CompIDs generated by the system** on import or publish of a master direction's sheet; authors leave the cell blank; exported sheets carry CompIDs so re-import updates the same items | Owner: "CompID generated and unique when a master direction is uploaded" |
| D-53 | **Conversations and accountability per CompID** (Query, Explanation Request, Guidance Request, Note, Decision; SLAs; RACI; ledger-computed time-in-hand attribution; accountability report). No automated HR outcome | Owner: seniors ask for explanations of delay, makers seek guidance, responsibility fixed for non-compliance |
| D-54 | **RAG urgency engine**: deterministic Red/Amber/Green from status, next due date, frequency windows and risk; Grey and Blue states; separate labelled "At risk of slipping" prediction | Owner: urgent and upcoming items in red/amber/green with forward-looking logic |
| D-55 | **Health Check Studio**: the super admin builds health-check sets by choosing sections, question counts and questions by CompID; versioned, maker-checker published | Owner instruction on health-check configuration |
| D-56 | **API-first onboarding**: discovery by PAN, CIN/LLPIN, GSTIN, LEI, registration number or name via licensed providers and public registers, with consent, provenance and confidence per field; partner onboarding API | Owner: "make onboarding better as we would be using the APIs" |
| D-57 | **Risk and Governance register templates** `LDC-TPL-RISK-v2.0` (RiskID) and `LDC-TPL-GOV-v2.0` (GovID) in the same v2.0 design | Owner: risk part has RiskID, governance part has GovID |
| D-58 | **Date rule** per row: issue date ≤ Actionable Last Updated On ≤ Instrument Last Amended On ≤ today; where the instrument was never amended, the amended date repeats the issue date (equal dates read as "not amended") | Keeps every row's dates mandatory and machine-checkable; owner may confirm (§4 item 20) |

---

## 3. Challenges to the brief (R-001)

### 3.1 Where the brief was changed, narrowed or corrected

| # | Brief asked | What the pack does instead | Reason |
|---|---|---|---|
| C-01 | Super admin can edit the audit trail, change dates and replace a client's proof | Correction Entries (D-02) | Editable trails lose evidentiary value (BSA 2023 s.63; Companies (Accounts) Rules r.3(1) edit log; SOC 2 CC7/ISO 27001 A.8.15); RBI inspections test audit trails |
| C-02 | Shared password tracker page for MCA, GST, CERSAI, CIC and RBI portals | Client-owned encrypted vault, per-credential grants, logged reveals; RBI portals client-only by default (D-04) | RBI portal IDs belong to named RE officers; shared passwords fail access-control tests and create liability |
| C-03 | CIBIL API for user registration | No bureau pulls; P11 prepares the client's own CIC submissions (D-25) | CICRA 2005 purpose limits |
| C-04 | Percentage share for CAs, CSs, lawyers on the marketplace | Per-profession switches, % OFF for regulated professions (D-06, D-32) | BCI Rules (fee-sharing, r.36), ICAI/ICSI codes |
| C-05 | Supervisory-returns directions "issued on 28 Nov 2025" | Cite the DoS directions of 31 Jul 2026 (X-12) | Factual correction |
| C-06 | Automated filing on CIMS, DAKSH, PRAVAAH | Prepare, validate, export, capture acknowledgement; human submits (NN-08) | No authorised filing API |
| C-07 | Separate LDC operations platform with its own CRM, marketing, HRMS | Group Operations Hub + LDC delivery console (D-03) | The Hub is already specified for all group companies; duplication splits CRM and revenue |
| C-08 | Board bulk approvals (owner baseline) | Sequential "Review next" (NN-46) | Evidence of review |
| C-09 | Embedded Office editing | Graph co-authoring in the tenant's SharePoint/OneDrive; optional self-hosted editor (X-06) | WOPI requires Microsoft partner programme |
| C-10 | Jio "agentic AI, research and drafting" | Jio as channel and voice adapters (JioCX, SIP, Haptik); LLM adapter OFF until an enterprise API with India residency and no-training terms exists | No public Jio LLM API found (25 Oct 2026) |
| C-11 | Tax functionality for borrowers at Udofin from LDC | Borrower certificates remain the RE's through Finbyx/Udofin; LDC prepares GST/TDS for tenant entities (X-31) | RE is the issuer |
| C-12 | Employee monitoring to "make sure the employee cannot cheat" | Transparent, notified measurement; maker-checker, SoD and approval controls; no covert surveillance (NN-25; OH10–OH11) | DPDP s.7(i) legitimate use is narrow; controls reduce fraud, they do not eliminate it |
| C-13 | Full regulator returns for every regulator in v1 | NBFC, ARC, co-operative first; others `ACTIVE_UNVERIFIED` until a pilot verifies cell maps (X-32) | Unverified cell maps produce wrong returns |
| C-14 | LDC to "integrate" Consent Manager functions | Readiness only (D-29) | Role conflict |
| C-15 | LDC to run co-operative elections | Support and records; authority conducts (X-34) | Statutory elections are conducted by the election authority |

### 3.2 Corrections to the owner's baseline documents

MBP-1 is a disclosure form, not a register; the register of contracts in which directors are interested is MBP-4 (X-37). DPT-3 is a return; the register of deposits is under Acceptance of Deposits Rules r.14. The baseline's "31-column schema" is 30 columns (A–AD) plus system fields. Gold #C9A961 and amber #D97706 fail WCAG text contrast (X-20). "ISO 27001 certified" must not appear until certified (X-22). The live site's SEO/GEO markup is invisible to crawlers because the site is client-rendered (X-21).

### 3.3 Consolidation of new non-negotiable rules proposed by the streams

| Final NN | Proposals merged (stream) |
|---|---|
| NN-33 Statutory clocks computed, earliest start, never pause | S1 (due dates never edited), S6 (earliest legally relevant start), S12 (clocks never pause) |
| NN-34 Reviewed release only; code never changes content | S1 (unreviewed intelligence labelled), S11 (releases never modify content) |
| NN-35 Template contract | S2 (rows 1–2/columns A–AD immutable; base vocabulary never renamed) |
| NN-36 Sealed governance records | S3 |
| NN-37 Deterministic documents and numbers | S3 (AI never writes OOXML), S5 (no AI figures) |
| NN-38 Regulatory floors and supervisory status | S4 (floors; never PCA), S7 (VERIFY advisory only; no auto-classification needing RBI advice) |
| NN-39 One owner per computed output | S5 (never recompute Finbyx returns), S4 (Finbyx-certified metrics) |
| NN-40 Internal Ombudsman independence | S6 |
| NN-41 AI data-class routing; no standing AI permissions | S8 |
| NN-42 Never-block list | S8, S9 |
| NN-43 Delivery staff never check | S9 |
| NN-44 Honest public surface (SSR; no dark patterns) | S10 |
| NN-45 Audit in same transaction; export taxonomy contract | S11 |
| NN-46 No bulk approval with legal effect | S12 |
| (folded into NN-20) Professional-conduct render allow-lists | S9 |


### 3.4 Non-negotiable rules added in v1.1

| Final NN | Source |
|---|---|
| NN-24 amended (home-region residency, linked tenants) | G1 global stream |
| NN-47 AI never decides a conclusion | G2 feedback stream |
| NN-48 Three dates per instance; timeliness on act date | G2 |
| NN-49 Undo for imports and bulk changes | G2 |
| NN-50 Bounded autonomy | G3 AI stream |
| NN-51 AI kill switches | G3 |
| NN-52 Protocol edge, contract core | G3 |
| NN-53 Jurisdiction-pack gate | G1 |
| NN-54 Official language preserved | G1 |
| NN-55 No stale citations | G4 RBI catalogue stream |

### 3.5 Further corrections found in v1.1

- RBI direction counts reconciled (238 press release / 244 serials / 240 live) and the NBFC set is 35 consolidated directions, not 30 (X-52).
- NBFC Internal Ombudsman Directions: /383 or /384 [VERIFY]; v1.0 stated /384 as fact.
- IFSCA entity types are 40, not 33 (X-56).
- Ind AS 37 fixed probability bands and the BRSR "75% value-chain boundary" in the owner baseline are corrected (X-57).
- `rpt` was used by ten phases but owned by none; P28 now owns it, and P06's related-party use of `rpt` is renamed (X-43, X-44).
- P18 routed litigation events to a register no phase built; P26 now owns `lit.matters`.
- Stale RBI citations superseded by the 28 Nov 2025 directions (the 2023 SBR Master Direction, the 2022 UCB circular, the 2023 IT governance direction) are re-cited to the consolidated or DoS directions with [VERIFY] numbers.
- Three different "scores" are now four named measures (X-46).
- AuditBoard is now Optro (March 2026).

### 3.6 Non-negotiable rules added in v1.2

| Final NN | Source |
|---|---|
| NN-35 amended (contract v2.0: group order, machine keys, header text and base vocabularies immutable within a major version) | v1.2 lead spec |
| NN-56 Business IDs are permanent | v1.2 lead spec (D-51) |
| NN-57 Audit trail by business ID | Owner instruction ("audit trail attached to the CompID") |
| NN-58 Deterministic RAG | v1.2 lead spec (D-54) |
| NN-59 Conversations are records | v1.2 lead spec (D-53) |
| NN-60 Responsibility from the ledger | v1.2 lead spec (D-53) |

### 3.7 Corrections found in v1.2

- The 30-column contract mixed several data items in one cell (due rule in column P after `Due:`, retirement by prefix in column F, CompID typed by authors in column E); v2.0 gives each its own column and the platform issues CompIDs (X-29 amended, D-52).
- One stream wrote the date rule as issue ≤ amended ≤ updated; the correct order is issue ≤ updated ≤ amended ≤ today (D-58, X-62); P03 V-30 and LDC-TPL-075 fixed.
- Two CompID registries were drafted in parallel (P03 and `core`); one registry in `core`, P03 tables become views (X-63).
- The RISK template's taxonomy codes (`MDL`, `LGL`, `AIG`) differed from Appendix H (`MOD`, legal within `CMP`); Appendix H codes are binding and the importer maps aliases (X-64).
- Status-chip colour `color.danger` on its background measured 4.04:1 (below WCAG 4.5:1); RAG chips use `rag.red` #B42318 on #FEE4E2 (5.45:1) (Appendix C §C.8.1A).

---

## 4. Owner decisions pending (needed before the phase named)

| # | Decision | Owner | Blocks |
|---|---|---|---|
| 1 | Confirm Microsoft 365 plan (D-10) and whether any group company uses Google Workspace | Company Secretary | P18 workspace connectors, P22 vault device checks |
| 2 | Trials as real tenants (D-26) — accept, and obtain OH acceptance | Owner + OH lead | P20 trial lifecycle |
| 3 | Selling entity(ies) and merchant of record (D-27) | Board / CFO | P20, P21 invoices |
| 4 | Second pricing approver (D-28) | Owner | Pricing Studio go-live |
| 5 | Package names, base prices, add-on prices, trial length, discounts (Appendix N seeds marked [OWNER TO SET]) | Owner / CFO | P20, P23 pricing page |
| 6 | Product names: Vidhi vs Nidhi AI; FinLegal Academy vs LawDocs Trainings; package names vs live Basic/Pro/Custom (X-18) | Owner | P17, P21, P23 |
| 7 | `_LDC_System` export sheet (X-28) | Owner | P03 exports |
| 8 | Revenue-stream registry waves and kill-switch approvers; advertising/sponsored listings ON or OFF | Board | P20, P21 |
| 9 | Hindi second locale and further languages (D-30); AI-crawler policy (D-31) | Owner | P23 |
| 10 | Entity particulars of the LDC operating company (CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer) for invoices, notices and the trust centre | Company Secretary | P20, P23, P24 |
| 11 | Policy set for certification readiness (information security, access control, incident response, vendor risk, retention, privacy, cookie, AI use, BCP) | Company Secretary / CISO | P24 |
| 12 | Vendor contracts (candidates only): AWS, Bedrock, Keycloak hosting, Temporal, OpenSearch, Razorpay via OH8, eSign ASPs, company-data provider, DigiLocker partner, PAN/GSTIN provider, SMS/WhatsApp/JioCX, translation/speech, CERT-In empanelled VAPT auditor | CTO / Procurement | P01, P07, P17, P18, P24 |
| 13 | Content team and reviewer roster (CS, CA, advocate) for packs and Part-2 sheets; in-country reviewers before any international pack | Owner | P03, P05, P15 |
| 14 | Retire the live site's certification claim and old Railway hosting after migration | Owner / CTO | P00, P23 |
| 15 | *(v1.1)* Approve the RBI content base and catalogue (D-39) and the Part-2 wave plan (Appendix AB); confirm reference numbers as sheets are written | Owner / content team | P03 catalogue pre-seed, Part 2 |
| 16 | *(v1.1)* Default AI autonomy ceilings per plan and the human sponsors for agents at L2+ | Owner / CTO | P17 |
| 17 | *(v1.1)* First regional cell and corridor after India (recommended UAE then Singapore), and the first content partners | Owner | P25 |
| 18 | *(v1.1)* ESG-BRSR as a separate Part-2 family (built) or merged into SEBI-LISTED/MCA-CO | Owner | P27, Part 2 |
| 19 | *(v1.1)* Delete or keep archived v1.0 files in `_Archive (older versions)` (deletion needs your approval on the computer) | Owner | — |
| 20 | *(v1.2)* Confirm D-58: for never-amended instruments the amended date repeats the issue date (alternative: blank) | Owner | P03 importer, Part 2 |
| 21 | *(v1.2)* Default RAG windows, including "Immediately" and event-based items (FR-P04-230 defaults stand until changed) | Owner / CCO advisory panel | P04 go-live |
| 22 | *(v1.2)* Default export columns (X-66) and whether the PDF list export carries the tenant logo and a "Confidential" footer | Owner | P04 export builder |
| 23 | *(v1.2)* First health-check sets: families, sections, question counts and the CompIDs chosen (placeholders `LPH-` until sheets publish) | Owner / content lead | P23 Health Check Studio |
| 24 | *(v1.2)* Onboarding data-provider contracts (company master and directors, GSTIN taxpayer search, PAN verification) and the provider waterfall order | CTO / counsel | P01, P18 onboarding ports |
| 25 | *(v1.2)* Instrument short codes for the 238 RBI directions (`INST` part of CompIDs; codes freeze at first issue) and whether pattern-conforming legacy CompIDs stay canonical | Company Secretary / content lead | P03 CompID generation, P00 migration |
| 26 | *(v1.2)* Use of accountability reports in HR or disciplinary processes (tenant policy; counsel review) | Tenant HR / counsel | P04 accountability report |
| 27 | *(v1.2)* Authority code for Secretarial Standards in GovIDs (`ICSI` proposed) | Company Secretary | P06 GOVL library |

---

## 5. Questions for counsel

1. CICRA 2005: may LDC obtain any credit-information report for its own customer onboarding? (Pack assumes no.)
2. Advocates Act 1961, BCI Rules Part VI (r.36, fee-sharing), ICAI, ICSI and ICMAI codes: permitted marketplace models, listing formats, platform fees and whether LawDocs may invoice for practitioners' services.
3. LODR Reg 24A: may an Infrabyx-linked practising CS act as secretarial auditor of a listed client that uses LDC or LawDocs retainers?
4. RBI outsourcing directions (banks, NBFCs, UCBs, RCBs): which "virtual CCO / internal audit / compliance" services may be supplied to REs and in what form?
5. DPDP Act: LDC's role as processor for tenants and fiduciary for its own users; s.16 cross-border position for Bedrock routing; employee-monitoring notice text (s.7(i)).
6. Trials as production tenants (D-26): click-wrap enforceability for regulated entities and the minimum RE addendum.
7. Savings dashboard: wording of penalty-avoidance estimates so they are not misleading (Consumer Protection Act 2019; dark-patterns guidelines).
8. eSign: documents in the IT Act First Schedule that the policy and agreement workflows must route to wet signature or registration.
9. Co-operative societies: State-by-State limits on electronic meetings, e-voting and digital registers for the first ten States.
10. Health check lookups: provider terms that allow anonymous company look-ups for lead generation.
11. *(v1.1)* For each corridor country: whether partner referral fees, revenue share or platform fees with local lawyers and accountants are permitted; local data-transfer mechanism; whether the product's compliance content is "legal advice" there.
12. *(v1.1)* Wording of AI-governance and "AI assurance pack" claims so they are not read as certification.

---

## 6. Assumptions

- The live LawDocsComply repository (TypeScript/React/Node/MongoDB/Prisma on Railway, 21 modules, RBI and Companies Act question banks, beta with Branch International) is available to the coding agent in P00 with read access to production data for migration.
- Finbyx, Udofin and the Operations Hub are built to their current prompts; where they are not yet live, LDC ships the stated fallbacks (interim billing adapter, CSV/SFTP intake, local computation for non-Finbyx tenants).
- The owner's content team produces Part-2 sheets for the first four families (RBI-NBFC, MCA-CO, DATA-PRIV, IFSCA-GEN) before Wave 1 GA.
- All prices and plan names are placeholders until the owner sets them.

---

## 7. External dependencies

AWS India regions and Bedrock India route; Keycloak; Temporal; OpenSearch; Microsoft Graph permissions and tenant admin consent from each client; licensed company-data and PAN/GSTIN providers; DigiLocker partner; eSign ASPs; SMS DLT registration; WhatsApp Business account; Razorpay via OH8; CERT-In empanelled auditor; translation and speech providers for Indian languages; FinLegal Academy LMS API; Ecosystem Spec v1.2 change requests (master §19).

---



# PART C — MODULE SPECIFICATIONS BY PHASE (objective and scope; full detail in the phase files)

### Phase P00 — Foundations, Repository Discovery and Migration

LawDocsComply already runs in production at lawdocscomply.com: a TypeScript, React and Node.js application on MongoDB (Atlas) with Prisma, deployed on Railway with GoDaddy DNS, carrying RBI and Companies Act question banks, an admin dashboard and 21 product modules, in beta with Branch International. It was built fast and has served its purpose. It cannot carry what the owner now wants — an append-only audit ledger, bitemporal regulatory content with tenant overlays, row-level tenant isolation, India-only residency, ecosystem contracts with Finbyx, Udofin, Equator and the Operations Hub, and certification readiness for SOC 2 and ISO 27001.

P00 does three things. It **discovers** what exists and preserves every useful asset (question banks, SEO work, users, beta tenant data). It **builds the platform core** on the locked stack (D-01): monorepo, PostgreSQL with enforced RLS, the hash-chained audit ledger with Correction Entries (D-02), bitemporal patterns, transactional outbox, feature flags, the evidence store, observability and the CI/CD skeleton. It **migrates** the legacy data in controlled waves with reconciliation, so no customer re-keys anything and the beta tenant experiences no data loss.

| Outcome | Exit-gate measure |
|---|---|
| Nothing useful is lost | `docs/discovery/` inventory signed off by the owner: every legacy module, collection, question bank, user, tenant, integration, secret, DNS record and SEO asset is listed with a disposition (MIGRATE, REBUILD, RETIRE, ARCHIVE). Zero items "unknown" |
| Platform core runs | `docker compose up` and `pnpm dev` start all apps locally in ≤ 10 minutes on a fresh machine; dev, staging and uat environments deploy from `main` through CI with signed images |
| Tenant isolation is provable | RLS lint passes on every tenant table (FORCE RLS + policy); `NN-01_cross_tenant_read_denied` passes for 100% of tables with generated queries across two seeded tenants |
| Audit ledger is tamper-evident | `NN-02_*` suite passes: every material action writes a chained event in the same transaction; daily verification and signed anchor run; an attempted `UPDATE`/`DELETE` on the ledger fails even for the owner role; a super-admin override is only possible as a dual-approved Correction Entry that is visible to the tenant |
| Bitemporal content works | A seeded instrument can be amended with a future effective date; queries "as of" any valid date and "as recorded" at any instant return the correct versions (`NN-07_*`) |
| Legacy content migrated (wave 1) | Every legacy question row is present in `cnt` with a migration lineage record, row counts reconcile 100%, a 5% stratified manual sample (minimum 200 rows) is checked by the Company Secretary with ≤ 0.5% field-level defects, all fixed before exit |
| Evidence store is WORM | Evidence objects land in an Object Lock (compliance mode) bucket in ap-south-1 with SHA-256 recorded; a delete attempt within retention fails (`NN-09_*`) |
| Export contract exists | The `LDC-EXPORT-1.0` mapping registry and its CI contract test exist; a migration that adds a tenant table without an export mapping fails CI (`NN-10_*`) |
| India residency | Infrastructure-as-code denies resources outside ap-south-1/ap-south-2 (except listed global services); the Railway deployment is scheduled for decommissioning with a dated plan (`NN-24_*`) |

---

**Scope.**

**In scope**

- Discovery of the legacy repository, database, deployment and third-party accounts; disposition register; architecture decision records (ADRs) 0001–0020.
- Monorepo scaffold with apps and packages (§4.2), toolchain, linting, module-boundary enforcement and code ownership.
- Local stack, environments (local, dev, staging, uat, prod, dr), infrastructure as code and the hosting plan (Supabase Mumbai for non-production and beta, AWS RDS/Aurora in ap-south-1 with ap-south-2 DR before general availability — §4.3).
- CI and CD skeleton with signed artefacts, SBOM, provenance and the NN test harness (P24 hardens and completes it).
- `core` schema: tenants, legal entities, tenant domains, organisational skeleton, jurisdictions, data-class catalogue, feature flags, module entitlement cache, sequences, idempotency keys, transactional outbox and inbox, audit ledger, audit anchors, correction entries, audit annotations, access log, break-glass events.
- PostgreSQL roles, RLS framework, session context, RLS lint; field-level encryption library; blind indexes and masking.
- Bitemporal modelling library and conventions; decimal and money types; ID generation; citation value object.
- Object storage buckets (quarantine, documents, evidence, exports, backups) and the evidence ingest pipeline skeleton (P07 builds the DMS on it).
- Observability (OpenTelemetry traces, metrics and logs; PII scrubbing; error tracking), health checks, status endpoints.
- Feature-flag service and flag registry; the `cfg` registry heads used by P02.
- Design system foundations (tokens, theming, accessibility primitives) and i18n framework (English first; Hindi and other Indian languages later through P23).
- Synthetic seed data profiles (`dev`, `demo`, `load`, `beta-mirror`).
- Data migration framework and waves 1–3 (wave 1 executed here; waves 2–3 rehearsed here, executed later).
- Export-mapping registry skeleton (`xpt.export_mappings`) and the NN-10 CI contract test (P19 builds the package generator).

**Out of scope (owned later)**

- Identity, login, onboarding wizard, RBAC/ABAC decisions — P01 (P00 creates only the tables P01 needs and a stub identity provider for local development).
- Configuration Studio UI and rule-pack engine — P02 (P00 creates the `cfg` registry tables and the SDK interface).
- Regulatory content authoring, Excel import — P03 (P00 migrates legacy content into the P03 schema as defined in Appendix B; if P03 later refines the schema, the migration is replayed from the immutable wave-1 snapshot).
- Production go-live hardening, VAPT, certification evidence automation — P24.
- Mobile apps (D-01: responsive PWA only in v1.0).

---

### Phase P01 — Identity, Tenancy, Onboarding and Access

LawDocsComply serves people with very different stakes: a platform super admin who can correct anything; a LawDocs relationship manager who works inside a client's tenant as a maker; a client company admin who configures the product; makers, checkers and department heads who do daily compliance work; KMPs and directors who need dashboards and approvals; internal, external, secretarial and IS auditors; an RBI or other supervisor who must see records read-only for a limited period; employees who only acknowledge policies; POSH Internal Committee members working on sealed matters; co-operative society office bearers and members; marketplace buyers who never subscribe; and anonymous visitors running the free health check.

P01 gives each of them the right door, the right proof of identity, the right permissions and nothing more — and makes a company's first hour with LawDocsComply fast: enter a PAN or CIN, confirm the auto-filled profile, pick the regulator and entity family, choose modules, see the price, invite the team and reach a first useful result.

| Outcome | Exit-gate measure |
|---|---|
| Fast self-onboarding | A new NBFC (synthetic) goes from health-check report → trial tenant → verified entity profile → modules selected → first five users invited → first compliance calendar visible in ≤ 30 minutes, with ≤ 12 fields typed manually (all others auto-filled or defaulted) |
| Strong authentication | 100% of privileged roles (platform, delivery, `ten_admin`, `ten_cco`, `ten_checker`, KMP, board, auditors, supervisor view, IC, payroll) enforce MFA at onboarding; passkeys available to all; step-up enforced on the actions in §4C |
| Least privilege, server-side | Every API, export, job and AI retrieval call is authorised by Cerbos with role + attributes; UI hiding is never the control; the Appendix D matrix is executable as policy tests (≥ 1 allow and ≥ 1 deny test per matrix row) |
| Delivery staff are visible guests | A LawDocs RM can act as maker in a client tenant only through a client-approved `delivery_grant`; every action shows "LawDocs (RM name)" in the tenant's audit and UI; revocation takes effect within 60 seconds |
| Regulator view is safe | A supervisor grant is created by the tenant (maker-checker), time-boxed ≤ 90 days, read-only at database, gateway and UI layers, watermarked, logged and revocable (D-12; NN-18) |
| No identity over-collection | No Aadhaar number, raw PAN image or bureau report is stored at onboarding; KYB facts carry source and fetched-at; DPDP notice and consent artefacts recorded (NN-12) |
| HRMS-linked users | A user can be created from an HRMS employee record (P13) or directly; either way, a person has one identity across tenants and products where they belong |

---

**Scope.**

**In scope**

- Keycloak realms, clients, themes and custom authenticators; BFF session pattern for all Next.js apps.
- Authentication methods: email + password, email magic link, mobile OTP (SMS/WhatsApp), TOTP, passkeys (WebAuthn), enterprise SSO (Microsoft Entra ID, Google Workspace, any SAML 2.0/OIDC IdP), recovery codes.
- Authentication assurance levels and step-up.
- Persons, users, memberships, role grants, ABAC attributes, delegations, act-as and on-behalf-of (Vidhi).
- Invitations; bulk user import (CSV/XLSX); SCIM 2.0 provisioning; HRMS-driven provisioning hooks (P13 completes).
- Cerbos policy service and the enforcement library (`packages/authz`), plus query-plan filters for list endpoints.
- Delivery grants (LawDocs staff acting in tenants), regulator/supervisor grants, auditor grants, break-glass UI.
- Self-onboarding funnel: entry from health check, pricing or marketplace; account creation; KYB auto-fill; entity profile; regulatory profile and family; module selection with live price; trial start; team invitation; first value.
- Trial lifecycle (7 days default, extendable by super admin per tenant — R-070) and conversion hand-off to P20.
- Multi-entity and group setup (holding, subsidiaries, member societies).
- Account experience: profile, security, sessions, devices, notification-channel preferences (data captured here; P04 notification engine uses it), privacy centre (DPDP rights for the user's own data).
- Platform, delivery and tenant administration screens for users and access.

**Out of scope**

- Configuration Studio and setting packs (P02) — P01 registers its settings and calls the P02 resolver once available (fallback to registry defaults).
- Detailed dashboards (P04 onward; information architecture in Appendix C).
- HRMS employee master and org chart (P13) — P01 provides the `iam.persons` ↔ `hr.employees` link.
- Billing, payment, invoices, plan changes (P20) — P01 calls `bil.quote` and `bil.start_trial` and receives entitlements.
- Credential vault content (P22) — P01 provides the step-up and access-grant primitives it uses.
- Co-operative member self-service portal details (P16) — P01 provides member identity and login.

---

### Phase P02 — Configuration Studio, Rule Engine and Settings

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

**Scope.**

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

### Phase P03 — Regulatory Content Library, Template Registry and Excel Import

LawDocsComply sells one product to many kinds of regulated entity — an NBFC in the Middle Layer, an Urban Co-operative Bank in Tier 2, an IFSCA Finance Unit, an AIF, a listed company, an LLP, a credit co-operative society. The legal content each of them must comply with is different, it changes every month, and every client wants to adjust the wording to its own operating structure. This phase builds the **content backbone** that makes that possible without code changes:

1. a versioned, clause-linked **Regulatory Content Library** owned by the LawDocs content team;
2. a **Template Registry** that treats the owner's Excel question format as a versioned ingestion contract, one template per entity family (D-08; Appendix E);
3. an **Excel Importer** that validates, previews, diffs and publishes question sheets prepared in Part 2 of the programme (R-004, R-084);
4. a **tenant overlay** model so that a client can edit, add or retire questions for itself only, with a full audit trail, while still receiving platform updates (R-017, R-086, NN-03);
5. a **Regulation Catalogue** in which the client admin sees every available instrument with its date, update date and applicability, and adds or removes it with a checkbox (R-087).

| Outcome | Exit-gate measure |
|---|---|
| Owner can load Part-2 question sheets without developer help | The 13 IFSCA sheets already in the `IFSCA Documents` folder and the two samples supplied on 25-Oct-2026 import with zero blocking errors after correction; median time from upload to "ready for checker" ≤ 5 minutes for a 300-row sheet |
| Every checkpoint is traceable to law | 100 % of published checkpoints carry authority, instrument, version, clause reference, source URL and source-file hash (NN-06); a citation lint rejects any row without them |
| Tenants customise without losing updates | A tenant overlay on 20 checkpoints survives a platform release that amends 5 of them; the 15 untouched overlays rebase automatically; the 5 conflicting overlays raise one consolidated review task; no completed compliance record changes (NN-03, NN-29) |
| Client admin decides applicability in one screen | A new NBFC-ML tenant sees its recommended instruments pre-ticked, can accept all in one click, or untick one with a reason; time to a complete applicable set ≤ 10 minutes |
| Customisation hierarchy works | A tenant renames "Compliance" to "Secretarial & Compliance" and splits "Risk Management" into "Credit Risk" and "Operational Risk"; all existing checkpoints remap via a mapping table, without editing any question |
| Round-trip Excel | Export of any adopted instrument in the owner's format, edit offline, re-import: unchanged rows are recognised by CompID, changed rows show a cell-level diff, and nothing is applied before checker approval |
| Global-ready | A non-Indian jurisdiction pack (EU GDPR, flag OFF) can be created as data — authority, instruments, holiday calendar, vocabulary — without schema change (D-19) |
| RBI catalogue visible from day one *(v1.1)* | All 320 rows of `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx` are loaded as instruments with coverage state; an NBFC-ML tenant sees its 35 DoR + 9 DoS + Internal Ombudsman + RB-IOS directions with "Checkpoints available / In preparation / Planned" and can adopt all recommended in one click (D-39) |
| Existing trackers become live registers *(v1.1)* | A 500-row legacy Excel tracker is mapped ≥ 80 % automatically by the AI tracker import in the pilot, with zero silent overwrites; everything not mapped lands as tenant checkpoints or custom fields for review (IMP-005) |
| One evidence, many obligations *(v1.1)* | A tenant maps its "KYC Policy approved by Board" control to the RBI NBFC KYC, PMLA and IFSCA AML checkpoints; one evidence submission closes all three period instances, each still reviewed by the right checker (IMP-013) |
| Every import reversible *(v1.1)* | Any import batch can be undone within 24 hours (tenant-configurable 1–72 h) by one action that writes a compensating Correction Entry batch; the ledger shows both (NN-49) |

---

**Scope.**

**In scope**
- Content model: jurisdiction → authority → instrument → instrument version → clause → checkpoint (question/actionable) → control activity → evidence requirement; content packs and content releases.
- Content team workflows: authoring in the Content Studio grid, import from Excel, quality lint, maker → checker → publisher release (roles `plt_content_maker`, `plt_content_checker`, `plt_content_publisher`).
- Template Registry: template families, template versions, column contract, controlled vocabularies with canonical codes, named ranges, the `_Template_Info` sheet, fingerprinting, template download.
- Importer: Content mode (platform and tenant), Workspace mode (round-trip of tenant compliance status — validation built here, application of status changes built in P04), Overlay mode (tenant edits offline), error report, diff, re-import, idempotency.
- Tenant overlay and tenant-authored checkpoints; three-way rebase on platform updates; conflict review.
- Customisation hierarchy and terminology: regulator → tenant → legal entity → department → function; department and function renaming and mapping; default-owner rules.
- Regulation Catalogue (tenant), adoption and removal, dependencies between instruments, applicability badges from the P15 engine.
- Jurisdiction-pack framework (D-19), holiday calendars as reference data (consumed by P04's due-date engine).
- Seed: migration of the existing LawDocsComply MongoDB question banks (RBI NBFC Base/Middle Layer/CIC, Companies Act) via the P00 migration scripts into the new model, with provenance `MIGRATED_V0`.
- *(v1.1)* Pre-seeded RBI Directions catalogue (320 rows; D-39), coverage states, placeholder-item hand-off to P04, reference-basis gate, withdrawn-instrument block (NN-55), sibling checkpoints (D-40) and concordance-driven re-citation (with P05).
- *(v1.1)* Common control layer and cross-instrument obligation equivalence; AI tracker import and competitor-export migration adapters; multi-sheet workbooks; import undo window; MCP read tools for obligations.

**Out of scope (owned elsewhere)**
- Writing the questions themselves (Part 2 of the programme; separate Cowork chats).
- AI generation of question sheets from an uploaded instrument (P05 AI Question Authoring Studio; it produces files that enter this importer).
- Regulatory monitoring, change classification and Updates inbox (P05).
- Compliance instances, due dates, maker/checker execution, evidence upload (P04).
- Applicability rule content per sector (P15) — this phase defines the interface and stores the expressions.
- Policy templates (P07), return definitions (P11), risk taxonomies (P08).
- *(v1.1)* Licences and registrations register (P26 owns `lit`/licence records; P03 only stores licence-condition checkpoints created from it); foreign country packs' partner network and regional cells (P25).

---

### Phase P04 — Compliance Workspace: Maker-Checker, Calendar, Tasks and Notifications

Turn every adopted checkpoint into **work that gets done, proven and reviewed on time** — by the right person, with the fewest clicks, with evidence a checker and an auditor can rely on, and with reports a Chief Compliance Officer can put before the Board.

| Outcome | Exit-gate measure |
|---|---|
| No compliance left unattended | 100 % of applicable checkpoints of adopted instruments generate instances for the current and next period with an owner and due date; unowned instances = 0 (an unowned instance raises a setup alert to the CCO within 1 hour) |
| Maker-checker discipline | No instance can close without a checker other than the maker (NN-05); High-risk instances require evidence matching the checkpoint's expected-evidence list |
| Fewer clicks | A maker can submit a routine monthly compliance with evidence in ≤ 3 interactions from the Work Inbox (open → drop file → submit); a checker can review and approve in ≤ 2 interactions after opening the evidence |
| Deadlines visible where people already look | Due dates and assigned tasks appear in the user's Microsoft 365, Google, Outlook.com, Gmail or Apple calendar within 15 minutes of assignment (Graph/Google API) or at the next ICS refresh |
| Work vs regulatory news separated | Notifications inbox (work) and Updates inbox (regulatory, P05) are separate data models and UIs (NN-27); users can tune digests without muting mandatory escalations |
| Board-ready reporting | CCO generates the quarterly compliance report for the Board/Audit Committee as an editable DOCX and a signed PDF in ≤ 5 minutes, from live data, with drill-down evidence links |
| Owner's Excel format round-trips | *(v1.2)* The tenant's register exports as the v2.0 Working Register (family template layout, CompIDs filled, User and System groups populated) or as the 9-column list; bulk status updates re-import through WORKSPACE mode under the same permissions |
| Fair timeliness *(v1.1)* | An instance performed on time but approved after the due date is reported `complied`, not `complied_late`, under the default rule (NN-48) |
| Evidence that collects itself *(v1.1)* | At least 10 NBFC checkpoints run as automated checks on connected data (e.g., grievance officer details on the website, KFS published, monthly DLG disclosure) and refresh without maker effort; a disconnected source shows `NO_DATA`, never "failed" |
| Event-based items not missed *(v1.1)* | Logging "director appointed" creates in one step the DIR-12 filing, MBP-1 disclosure index entry, fit-and-proper declaration and RBI intimation instances with due dates (IMP-028) |
| Alert fatigue controlled *(v1.1)* | Default budget of 10 immediate notifications per user per day enforced; overflow folded into the digest; Critical never folded; 20 assignments produce one e-mail (IMP-040, IMP-041) |
| Bulk changes safe *(v1.1)* | 200 rows of owners, internal dates and tags edited in-grid in ≤ 2 minutes, with preview and a 24-hour undo (NN-49) |

---

**Scope.**

**In scope:** compliance-instance generation; due-date and frequency engine with business-day conventions and holiday calendars; event-based triggers; maker/checker/auditor workflow mirroring template the user columns — Date of Compliance, Status and the MAKER, CHECKER and AUDITOR groups (v1.0: T–AD); evidence capture and reuse; rework, reallocation, delegation and backup owners; not-applicable claims, waivers, extensions; escalation ladders; exception register; attestations and compliance certificates (department → CCO → MD/CEO → Board); compliance score; reports and scheduled reports; Excel and PDF exports; unified calendar with external sync; task management (hierarchical assignment, sub-tasks, dependencies, checklists, recurring and scheduled tasks, tasks to Vidhi AI); Work Inbox; Notifications service with channels, digests, quiet hours and mandatory floors; WORKSPACE import application. *(v1.1)* Placeholder instances; grouped multi-licence work items and control executions; automated checkpoints; event bundles; evidence rules, reuse and request lists; compliance testing programme; issue action plans and remediation library; notification budget and alert-health; in-grid bulk edit with undo; Compliance Coordinator agent; foreign-entity timezones, fiscal years and calendars.

**Out of scope:** regulatory Updates and change impact (P05); meeting/committee scheduling (P06 — uses this calendar); policy reviews (P07 — uses this scheduler); return preparation (P11 — publishes due dates here); Vidhi's agent runtime (P17 — receives tasks from here); HR leave data (P13 — consumed for delegation); billing (P20). *(v1.1)* Report builder, MIS catalogue and board-pack studio (P28 owns `rpt`; P04 contributes report definitions); licences and registrations register, contracts and litigation (P26 — P04 only schedules their dated obligations); ESG/BRSR (P27).

---

### Phase P05 — Regulatory Change Management and AI Question Authoring

Regulators change their rules constantly — RBI alone withdrew 9,445 circulars and replaced them with its consolidated Master Directions on 28 November 2025 (238 function-wise directions per RBI's press release; 244 per circular RBI/2025-26/100; *v1.1*) and has since issued amendment directions and "updated as on" consolidations almost every month. A compliance tool whose content is static becomes wrong within weeks. This phase makes LawDocsComply a **living** system:

1. **Detect** every relevant publication from RBI, SEBI, IFSCA, IRDAI, MCA, MeitY, CERT-In, the Ministry of Labour, the Central and state co-operative registrars, GST/CBDT and other sources, every evening at 20:00 IST and intraday where feeds allow (D-18, R-089).
2. **Understand** it: classify, summarise, diff against the previous text, and map it to the checkpoints and tenants it affects.
3. **Publish** reviewed changes through the P03 release pipeline with maker-checker (NN-04, NN-05), preserving the previous direction and the previous actionable side by side (R-006, R-088).
4. **Tell** each affected client exactly *what changed, why it matters and what to do*, in the Updates inbox (separate from Notifications, NN-27), by e-mail and push, with calendar entries for effective dates (R-090).
5. **Manage** the client's implementation of the change: impact assessment, tasks, policy updates, board approvals and closure, all audit-trailed.
6. **Author** new compliance question sheets with AI: upload a Master Direction or regulation, let Claude apply the family template and the owner's question-writing method, export the draft Excel, verify, re-upload, and publish after confirmation (R-085) — for the platform (super admin) and for an individual client (client admin, tenant-only).

| Outcome | Exit-gate measure |
|---|---|
| Nothing missed silently | Every source in Appendix F has a last-success timestamp; a source not successfully scanned within its SLA raises a P2 alert to the content lead; the 20:00 IST reconciliation report lists counts per source and failures |
| Fast, reviewed publication | Triage ≤ 1 business day for all detected items (≤ 4 hours for items marked "effective immediately"); High-urgency actionable changes published to tenants ≤ 3 business days; others ≤ 10 business days (P95), measured on the change dashboard |
| Client knows what to do | Every published change produces an Updates item with the three-part note, old vs new actionable side by side, effective date in the calendar, and one-click actions (acknowledge, assign impact assessment, adopt, open conflicts) |
| History preserved | For any checkpoint, a user can see every regulatory change that affected it — previous instrument and paragraph, previous actionable, new actionable, change reason, release, reviewer, and the tenant's own response — exportable as a PDF/Excel change history |
| AI authoring accelerates Part 2 | On the evaluation set (owner-approved IFSCA sheets and the RBI NBFC 460–468 sheets), the AI Studio's draft reaches: clause-coverage recall ≥ 95 % of obligation clauses, citation accuracy ≥ 98 %, zero rows citing non-existent paragraphs, 100 % vocabulary validity, and median reviewer edits ≤ 20 % of rows |
| No auto-publish | No AI output reaches a tenant without human approval (NN-04); tests prove it |
| RBI library never stale *(v1.1)* | Every change in an RBI category page's "Updated as on" date is detected the same day and a change item opened; a new direction appears in tenants' catalogues as "New — checkpoints in preparation" within 1 business day (Appendix AB §AB.8) |
| Faster analyst work *(v1.1)* | Median analyst time per actionable change falls by ≥ 30 % against the v1.0 baseline through enrichment, similar-past-change pre-fill and sibling proposals (IMP-019, IMP-021) — measured per release |
| Less noise for clients *(v1.1)* | Updates for non-adopted instruments are collapsed; every update leads with a ≤ 60-word gist; "Accept impact" creates all impact tasks in one action (≤ 4 clicks from opening the update; IMP-022–IMP-025) |

---

**Scope.**

**In scope:** source registry operations (Appendix F), fetchers (RSS, HTML listings, PDF, e-Gazette, regulator e-mail alerts, licensed news feeds), scheduling (intraday + 20:00 IST reconciliation + weekly deep crawl), ingestion, hashing, de-duplication, text extraction (PDF text, OCR, HTML), metadata extraction, classification, addressee-to-family mapping, change items and their workflow, clause diff and concordance (old circular → new direction), impact mapping to checkpoints and tenants, content-release drafting from change items, regulator due-date extensions, horizon scanning of consultations and drafts, enforcement/penalty intelligence, the Updates inbox and delivery, the tenant change-implementation workflow and tracker, change-history views and reports, the AI Question Authoring Studio (platform and tenant), prompt and methodology registry, evaluation harness, cost controls. *(v1.1)* RBI category-page monitoring and catalogue automation; sibling-change proposals; concordance seeding and legacy re-citation; enrichment and similar-change retrieval; content-incident playbook; penalty-intelligence corpus; foreign-source monitoring via `REG_INTEL_PORT`; Regulatory Analyst agent; MCP read tools for Updates.

**Out of scope:** the importer and release mechanics (P03 — reused), compliance instance recalculation (P04 — consumes events), policy redlining (P07 — linked from impact tasks), general Vidhi chat and notebooks (P17), writing the Part-2 question sheets for every instrument (programme Part 2; the Studio accelerates it).

---

### Phase P06 — Governance, Board, Committees and Company Secretarial

Every client of LawDocsComply — a private company, a listed NBFC, an urban co-operative bank, an insurer in GIFT City, an LLP or a society — must run its internal governance the way its constitution, the Companies Act 2013 (or the LLP Act 2008, the Societies Registration Act 1860 or the co-operative law), the ICSI Secretarial Standards and its sector regulator require. Today this lives in Word files, Excel trackers and the company secretary's memory. P06 turns it into a **Governance Operating System**: it composes the entity's governance blueprint from law and regulation, keeps the board, committee and KMP structure compliant as people change, runs every meeting from calendar to sealed minutes, maintains statutory registers from events, prepares ROC and stock-exchange filings, and drafts the annual report from source data — with the company secretary in control and every step evidenced.

| Outcome | Exit-gate measure |
|---|---|
| Governance blueprint generated, not hand-built | For each of the eight seeded entity profiles (private company; unlisted public company above thresholds; listed equity company; NBFC-ML; NBFC-UL; UCB > ₹5,000 crore assets; life insurer; LLP) the blueprint lists required directors, independent directors, woman director, committees, KMP, policies, meeting cadence, registers and filings, each with an `LR-*` citation, and matches the domain analyst's golden blueprint with zero missing mandatory items |
| Composition breaches caught at source | A change in a person's attributes (independence lapses, tenure ends, directorship count exceeds limit, DIN deactivated, fit-and-proper declaration overdue) raises a composition issue on every affected committee within 1 minute, with the rule cited and a remediation task assigned to the CS |
| Meetings with fewer clicks | A quarterly board meeting is scheduled, noticed, packed and published in ≤ 25 clicks by the CS using the standard agenda template and auto-pulled items; the notice goes out at least 7 clear days ahead (s.173(3)) or the system forces the shorter-notice path with the ID-presence rule |
| SS-1 minutes discipline | Draft minutes circulate within 15 days, comments close in 7 days, minutes are entered and signed within 30 days (SS-1; s.118 read with Rule 25) — timers visible, escalated at T-3 days; signed minutes are sealed and cannot be edited (NN-02) |
| Registers maintained by events | Allotment, transfer, charge creation, loan/investment approval, RPT approval, SBO declaration and director appointment events update the corresponding register automatically; a register snapshot reconciles to its event log with zero differences |
| Filings prepared, not missed | Every ROC, LODR and sector governance filing in the catalogue has a computed due date, an owner, a data sheet and attachments ready before T-5 working days; after filing, the SRN or acknowledgement is captured; overdue filings show accruing additional fee |
| Listed-company controls | Material events detected in the platform (board outcome, credit rating change, auditor resignation) open a Reg 30 disclosure case with the correct clock (30 minutes for board-meeting outcomes; 24 hours otherwise); UPSI shared through board packs creates Structured Digital Database entries automatically |
| Annual report drafted from data | The Board's report (s.134) and, for listed entities, MD&A and the Corporate Governance Report are produced as a DOCX draft with every figure traceable to its source (accounts, Finbyx/Udofin portfolio, registers, HRMS) and every narrative paragraph marked as AI draft until approved |
| Portability | `05 Governance - Board, Committees and Meetings/` and `06 Company Secretarial - Registers, Filings and Resolutions/` export (Appendix M §M.3, X-27) holds minutes as signed PDF and DOCX, registers as XLSX and PDF, resolutions, notices, packs and filings, readable without LawDocsComply |

---

**Scope.**

**In scope**

- Governance Structure Engine: constitution profile, threshold tests, regulator overlays, tenant charter, Governance Blueprint and its gap report.
- Entity master and group structure (holding, subsidiary, associate, joint venture), MCA master-data pull and diff.
- Directors and KMP registry linked to HRMS: DIN, director KYC, DSC custody log, categories, tenure, directorship limits, disqualification checks, declarations, remuneration links, familiarisation, evaluation.
- Committees: catalogue, terms of reference, composition rules, quorum, cadence, dedicated committee pages, custom committees mapped to statutory roles.
- Meeting lifecycle for Board, committees, independent directors' meetings, AGM, EGM, postal ballot and circular resolutions: planning, notice, agenda, board pack, secure board portal, attendance (physical and video conferencing), conduct, decisions, minutes, signing, sealing, certified copies, action tracking.
- Resolutions and documents library with auto-filled templates and follow-on filing triggers.
- Statutory registers maintained from events (Companies Act, LLP Act, SBO rules, PIT Structured Digital Database), inspection and extracts.
- ROC/MCA e-filing catalogue, due-date engine, data sheets, attachments, SRN capture (human filing with DSC — D-13).
- Annual secretarial cycle planner.
- Director declarations and fit-and-proper workflows (Companies Act, RBI NBFC/UCB/bank, IRDAI, IFSCA overlays), certificates generated for CEO/MD signature, RBI quarterly statements, PRAVAAH approval packs.
- Listed-company module: LODR calendar, Reg 30 disclosure engine, RPT approvals with Schedule XII thresholds, PIT (designated persons, SDD, trading window, pre-clearance, disclosures), SAST disclosures tracker, website (Reg 46) checklist, debt-listed and SME variants, stock-exchange file preparation.
- Secretarial audit hooks (MR-3, Reg 24A annual secretarial compliance report, MGT-8) consumed by P10.
- Annual report and Board's report drafting assisted by Finbyx, Udofin, accounting and HRMS data (R-053).
- CS, board member, chairperson, CEO/MD and committee-chair dashboards; task assignment by hierarchy.
- LLP governance (designated partners, LLP agreement, Form 3/4/8/11, LLP SBO).
- Society governance base (Societies Registration Act 1860 annual list, governing body) — reused and extended by P16 for co-operatives.

**Out of scope (owned elsewhere)**

- Policy authoring and approval lifecycle (P07), though board approval of a policy is captured through a P06 meeting decision.
- Co-operative elections, membership and general body specifics (P16; P06 supplies engines).
- Secretarial audit execution, working papers and audit report (P10).
- Automated filing on MCA21, NSE NEAPS, BSE Listing Centre or RBI portals (prohibited by D-13/NN-08 until an official authorised API exists): P06 prepares and validates, a human files.
- Remote e-voting service itself (provided by SEBI-recognised e-voting agencies; P06 exports and imports) and video-conferencing infrastructure (Teams/Zoom/Meet adapters via P18).
- Share registry/RTA operations beyond register maintenance and BENPOS reconciliation.

---

### Phase P07 — Policy Lifecycle and Document Management System

Regulated entities run on documents: board-approved policies that must be reviewed on time, evidence that proves each compliance, signed agreements, scanned letters from regulators, WhatsApp screenshots of customer complaints, handwritten registers in a branch. P07 gives LawDocsComply one governed document layer and one policy lifecycle, so that (a) every policy is drafted from the right model, redlined against its last approved version in real Word tracked changes, approved by the right body and evidenced by the signed copy; and (b) every document in the platform is stored once, found in seconds, shared selectively, signed lawfully, read by OCR and translated where needed, retained for as long as the law requires and exported in a folder structure a beginner can understand.

| Outcome | Exit-gate measure |
|---|---|
| Policies never silently lapse | Every policy has an owner, approver body, effective date and next-review date; an overdue review opens a compliance issue on day +1; dashboard shows 100% of policies with a computed status |
| Real tracked changes | A Vidhi-assisted revision of a 40-page KYC policy opens in Microsoft Word with every change as a native tracked insertion/deletion attributed to "Vidhi AI (draft)" and a comment citing the regulatory clause or model clause behind it; accepting all changes in Word yields exactly the approved text |
| Approval evidenced | A policy cannot move to `EFFECTIVE` without a P06 decision reference and an uploaded signed or certified copy (PDF); the system compares the scanned copy with the approved text and flags material differences |
| Attestations measured | Acknowledgement campaigns reach the HRMS-derived audience with reminders; completion rate and defaulters are reportable per department |
| Find anything fast | Permission-trimmed full-text and metadata search returns results in ≤ 1.5 s at p95 on 1 million documents per tenant, including OCR text of scans |
| Selective, controlled sharing | A user can assemble a share pack choosing exactly which documents to include, with view-only, watermark, expiry and OTP; every open is logged; revocation takes effect within 60 s |
| Lawful e-signature | Aadhaar eSign (through CCA-empanelled ESPs) and DSC flows complete with a certificate of completion; documents excluded by the IT Act First Schedule are blocked from e-signature with an explanation |
| Handwriting and screenshots usable | Handwritten letters, WhatsApp screenshots and photographed registers produce an editable type copy side by side with the original, with low-confidence words highlighted; the verified type copy and the original are attached together to the record |
| Translation | Documents in any of the six UN official languages or the 22 Eighth Schedule languages are detected and translated into English with segment alignment and confidence, labelled machine translation until reviewed |
| Folder intake | A 5,000-file folder tree is uploaded in one action with a mapping preview, duplicate detection and a commit report; nothing is overwritten |
| Structure survives releases | Canonical document paths are derived from metadata and the LDC-EXPORT-1.0 taxonomy (Appendix M), not from code; a schema release changes no customer-visible path (NN-10, NN-11) |

---

**Scope.**

**In scope — Policy lifecycle**

- Policy register, required-policy catalogue per entity (from the P06 Governance Blueprint and P03/P15 content packs), gap list.
- Model templates (platform, by entity family and regulator) and tenant templates (house style), with clause-to-obligation citation maps.
- Vidhi-assisted drafting: new from model, alignment to the previous version, alignment to a regulatory change, gap check against mandatory contents.
- Deterministic redline engine producing native OOXML tracked changes and comments.
- Review and approval workflow, Board/committee approval via P06, signed-copy evidence, publication, attestations and acknowledgements, review calendar, versions, superseded and retired policies, policy-to-control-to-obligation mapping.

**In scope — Document management**

- Repository with metadata-driven canonical paths mirroring LDC-EXPORT-1.0; virtual folders and saved searches; records linkage (one document, many records).
- Versioning, check-in/check-out, locks, compare.
- Office editing: desktop round-trip; Microsoft 365 co-authoring when the tenant connects SharePoint/OneDrive; optional embedded WOPI-compatible editor (flag).
- Search (full text including OCR, facets, filters, saved searches; semantic search through P17).
- Selective sharing (internal and external), share packs, view-only viewer, watermarking, expiry, OTP, revocation.
- eSign envelopes: Aadhaar eSign through CCA-empanelled ESPs (via application-service-provider adapters), DSC, simple electronic acknowledgement; certificate of completion.
- Document intelligence: OCR (printed, handwriting), WhatsApp/chat screenshot extraction, e-mail parsing, type copies with human verification, translation to English.
- Retention classes, legal hold, disposal with approval; WORM sealing.
- Folder/zip intake with mapping preview; connector intake; e-mail-in.
- Malware scanning, active-content stripping, prompt-injection screening.
- Document generation services (DOCX/PDF/PDF-A) used by every module.

**Out of scope**

- Contract lifecycle management and agreement drafting for counterparties beyond policies and internal documents — handed to LawDocs (lawdocs.in) through P18; P07 stores and signs the resulting documents.
- Board meeting management (P06) — P07 supplies pack PDFs and signatures.
- Records owned by Finbyx/Udofin (loan files) — referenced, not copied, unless the tenant imports them (NN-23).
- Human translation and certified translation services — offered through the marketplace (P21).
- E-stamping — handed to a stamp-duty adapter (P18) where an instrument requires stamping; flag `dms.estamp.enabled = OFF` until the adapter and state matrix exist.

---

### Phase P08 — Enterprise Risk Management and CRO Workspace

LawDocsComply is sold to banks, small finance banks, UCBs, NBFCs of every layer and category, ARCs, credit co-operative societies, IFSCA entities, SEBI-regulated entities (mutual funds, AIFs, listed companies, REIT/InvIT managers, intermediaries), IRDAI-regulated insurers and intermediaries, and ordinary companies and LLPs. Each has a different risk-management obligation: a commercial bank must run Pillar 2 ICAAP and publish Pillar 3 disclosures; an NBFC-ML must have a Risk Management Committee and a Board-approved risk policy; a top-1,000 listed company must have an RMC under LODR Reg 21; an LLP has no statutory risk function at all but still benefits from a register. This phase delivers **one configurable enterprise risk engine** — taxonomy, appetite, register, RCSA, controls, KRIs, loss events, issues, acceptance, committee packs and the CRO workspace — that switches on exactly what each entity family needs and nothing more.

| Outcome | Exit-gate measure |
|---|---|
| One engine, many entity families | Onboarding a tenant as "NBFC-ICC, Middle Layer, non-deposit, assets ₹2,400 crore" auto-enables the NBFC-ML taxonomy pack, RMC committee template, appetite metric set and 31 seed KRIs; onboarding "Private limited company, unlisted" enables only the corporate taxonomy (strategic, operational, compliance, financial, cyber, people, legal, reputational, ESG) with no prudential categories. Both explainable with the resolver's citation list (§4A.4) |
| Risk appetite that bites | The Board-approved RAS has appetite, tolerance and limit levels per metric; a limit can never be looser than the regulatory floor (test `NN-22_ras_floor`); a red observation opens a breach episode with escalation in ≤ 15 minutes of the value arriving |
| Live register linked to compliance | Every risk links to objectives, processes, controls and obligations (P03/P04). A failed compliance instance, audit finding (P10) or incident (P12) raises or re-rates the linked risk without re-keying |
| RCSA completed in days, not weeks | A 40-unit RCSA campaign is launched in ≤ 10 clicks from a template; units answer on one screen per risk; second-line challenge queue; completion ≥ 90% within the due date on the seeded pilot |
| KRIs fed automatically | For a Finbyx tenant, `RiskSnapshotPublished`, `KriBreached`, `LimitBreached` and `LossEventRecorded` update the CRO dashboard within the Ecosystem Spec SLA (≤ 15 min for breaches); for a non-Finbyx tenant, the same KRIs update from Excel/Tally templates (P11) or manual attested entries with evidence |
| CRO and RMC can run their meeting from LDC | The RMC pack (risk profile, appetite utilisation, top risks, breaches, loss events, RCSA status, emerging risks, cyber and third-party summary, ICAAP and stress summary from P09) is generated, frozen with a hash and distributed through the P06 board portal in ≤ 30 minutes of preparation |
| Fully customisable without a super admin | Tenant admins and CROs rename categories (levels 2–3), change scales, add KRIs, add widgets and edit templates within the Locked/Governed/Tenant tiers (NN-28); every change is audited (NN-02) |

---

**Scope.**

**In scope**

- Risk framework setup: methodology (ISO 31000:2018 process; COSO ERM 2017 components; three lines of defence), entity-family taxonomy packs, scales, matrices, materiality bands and terminology (§4A–4B).
- Risk Appetite Framework: Board-approved Risk Appetite Statement (RAS), qualitative statements, quantitative metrics with appetite/tolerance/limit levels, cascade to departments, products, branches, channels and legal entities (§4C).
- Risk register (enterprise, process, project, emerging) with inherent and residual assessment, trend, velocity, treatment and action plans (§4D).
- Control library and risk–control–obligation linkage with design and operating effectiveness, shared with P04 compliance controls and P10 audit tests (§4D.6).
- RCSA campaigns (questionnaire builder, unit responses, second-line challenge, final ratings) (§4E).
- KRI engine: definitions on governed metrics, thresholds, data sources (Finbyx, Udofin, LDC modules, Excel/Tally, manual attested), breach episodes and workflow (§4F).
- Loss-event and near-miss database with Basel event-type taxonomy, three dates, recoveries, GL reconciliation (§4G).
- Issues, actions and risk acceptance (temporary tolerances with expiry) (§4H).
- Risk committees: RMC, ALCO (structure only; liquidity analytics in P09), IT Strategy Committee (link to P12), Board — terms of reference templates, standing agenda, pack builder, minutes link to P06 (§4I).
- CRO workspace and role dashboards for CRO, risk officers, risk owners, RMC members and Board; configurable widget catalogue (§4J). KMP dashboards with financial ratios (CEO, MD, CFO, CCrO, CCO, IA head) are completed in P09 on the same shell.
- Emerging-risk radar and horizon scanning linked to P05 regulatory change (§4K).
- Pillar 3 / public risk-disclosure drafting workspace (bank Pillar 3; NBFC notes-to-accounts risk disclosures; listed-company board-report risk paragraphs; insurer public disclosures) — drafting, review and evidence, with numbers bound to P09 certified values (§4L).
- Risk-function governance records: CRO appointment, tenure, independence attestations, in-camera meetings, product-vetting records (§4M).
- Exports: register, RCSA, KRI history, loss data, RMC pack — Excel, Word, PDF/A; LDC-EXPORT-1.0 folder mapping (Appendix M).

**Out of scope (other phases)**

- Capital, ratios, ALM, liquidity, stress testing, ICAAP and KMP financial dashboards → **P09**.
- IT/cyber control frameworks, CERT-In incidents, vulnerability ingestion, TPRM lifecycle and outsourcing registers → **P12** (P08 consumes them as risk events and KRIs).
- Fraud case management, EWS alert handling at account level → system of record is Finbyx (FRM) or the tenant's LMS; P08 holds the fraud risk, KRIs and aggregated loss events.
- Compliance obligations and monitoring → P04; audit engagements → P10; policy lifecycle → P07; HR records → P13.
- Account-level credit data: never stored in LDC (Ecosystem Spec §6.22 pseudonymisation; NN-23).

---

### Phase P09 — Risk Assessment Lab: ICAAP, Stress Testing, Capital and Ratios

Risk managers at Indian regulated entities run capital, liquidity and stress tests in spreadsheets that break every quarter, are hard to audit and cannot show where a number came from. Finbyx solves this for lenders whose books are on Finbyx (Finbyx Part 7E). LawDocsComply must solve it for **every** tenant: Finbyx lenders (by consuming certified Finbyx runs), lenders on other LMSs, banks and UCBs, ARCs, CICs, insurers (as reported), investment companies, listed corporates and co-operatives — from their trial balance, loan-book extracts and portfolio files. The Lab delivers transparent, reproducible engines and a Board-ready ICAAP, with every figure traceable to its input and rule version (NN-22).

| Outcome | Exit-gate measure |
|---|---|
| Right engine for each entity | The capital profile resolver selects the correct engine and minimums for 12 seeded profiles (NBFC-BL leverage only; NBFC-ML CRAR 15%/T1 10%; NBFC-UL + CET1 9%; gold-primary T1 12%; HFC; CIC ANW/RWA 30%; commercial bank CET1 5.5%/T1 7%/total 9% + CCB 2.5%; UCB Tier 1 9% / Tiers 2–4 12%; ARC CRAR 15%; insurer solvency 150% as reported; corporate Schedule III ratios; credit co-operative management indicators) with citations |
| One number, one lineage | Any certified ratio drills to source rows (TB line, loan-book segment, Finbyx event) in ≤ 3 clicks; recomputing a frozen snapshot reproduces identical results bit-for-bit |
| Finbyx clients never re-key | For a Finbyx tenant in `LDC_EXTERNAL` mode, `CapitalRatioComputed`, `RiskSnapshotPublished` and `StressTestCompleted` populate the Lab within the Ecosystem Spec SLA, with provenance `FX` and no LDC recomputation of certified values |
| Non-Finbyx clients self-serve | An NBFC on a third-party LMS uploads the TB (Tally Prime XML/Excel), the loan-book segment template and the borrowings template and gets CRAR, Tier 1, leverage, SLS, IRS, LCR (where applicable), concentration and 40+ ratios within 30 minutes of upload, with data-quality results |
| Stress tests a Board can trust | Scenario library (46 seeded scenarios) covering credit, collateral, interest-rate, liquidity, concentration, operational, cyber, macro and reverse stress; a multi-period run (up to 12 quarters) completes in < 2 minutes for a 50-segment book; approved scenarios are immutable |
| ICAAP in weeks, not months | ICAAP cycle from data freeze to Board-ready Word/PDF in ≤ 15 working days on the pilot NBFC-ML, with tracked changes against last year's document (P07), every table bound to the frozen snapshot |
| KMP dashboards | 15 role templates (CEO, MD, CFO, CRO, CCrO, CCO, CS, IA head, Board, Audit Committee, RMC, ALCO, ITSC, Treasurer/co-op Secretary, Insurer CFO/Appointed Actuary view) render with only governed metrics; users customise without a super admin |
| Exports that stand alone | ICAAP, stress results, capital and ratio packs export as Word, Excel (values plus an assumptions sheet and lineage sheet) and PDF/A into LDC-EXPORT-1.0 `09 Risk Assessments - ICAAP, Stress Tests and Ratios/<FY>/…` and open without LDC |

---

**Scope.**

**In scope**

- Compute modes and data intake (Finbyx-sourced, Udofin LSP metrics, LDC-computed from templates, manual attested) with a frozen, hashed **risk data snapshot** and BCBS 239-style data-quality governance (§4A).
- Use of the shared `infrabyx-risk-kernel` (metric formulas, capital rule packs, ALM maths, PCA thresholds, stress primitives) so that Finbyx and LDC compute identically (§4B).
- Capital adequacy engines per entity family (§4C).
- Governed ratio engine and metric layer (ratio library in Appendix H §H.6) (§4D).
- ALM, liquidity and interest-rate risk tools (§4E).
- Concentration and large-exposure analytics (§4F).
- Investment-portfolio analytics for NBFC-ICC/CIC and investment entities (classification, valuation buckets, sensitive-sector exposure, AIF investment rules) (§4G).
- Stress testing and scenario studio, including reverse stress and multi-period projections (§4H).
- ICAAP workflow and document generator (§4I).
- PCA and supervisory-action monitoring (NBFC; bank PCA and UCB SAF as rule packs) (§4J).
- KMP, committee and Board dashboards with certification and customisation (§4K).
- Lab model governance (registry entries, validation, back-testing) (§4L).
- Exports and evidence (§4M).

**Out of scope**

- Account-level loan servicing, ECL computation from loan-level PD/LGD models (system of record: Finbyx Part 7C or the tenant's LMS/finance system; the Lab imports ECL by stage). A simplified ECL *overlay* for stress projections is in scope (§4H.4).
- Regulatory return filing (P11 prepares return-ready files; NN-08).
- Actuarial valuation for insurers (Appointed Actuary's systems) — the Lab imports solvency and ALM results.
- Scheme-level NAV and fund accounting for MFs/AIFs (imported).
- Trading/treasury front-office systems; VaR models beyond the transparent historical/parametric calculators in §4E.6.

---

### Phase P10 — Audit Management: Internal Audit, RBIA, Concurrent, IS/IT, Secretarial, Statutory-Audit Support and Specialised Audits

LawDocsComply is sold to NBFCs, banks, UCBs, co-operative societies, ARCs, IFSCA entities, SEBI- and IRDAI-regulated entities, listed and unlisted companies and LLPs. Each of them must plan and evidence audits that a regulator, a statute or a professional standard requires, and most of them run those audits today in spreadsheets, e-mail and shared drives. This phase delivers **one assurance workspace** for every audit type a tenant runs or supports, built on the same obligation, control, risk and evidence base as the compliance and risk modules, so that audit work is not re-keyed and every finding drives remediation.

LawDocsComply is the **tool**. The tenant's auditors own every opinion, rating, finding and report. Neither LawDocs nor any Infrabyx company performs a tenant's internal audit through the tool (RBI (NBFC – Internal Audit Function) Directions, 2026, RBI/DoS/2026-27/464 ("IAF"), para 39: internal audit cannot be outsourced; contract experts only where the Board/ACB is assured the expertise is unavailable internally, and report ownership stays with regular IA staff) — the Marketplace (P21) may sell co-sourced specialist support only within those limits, and the product enforces the limits (§4C.3).

| Outcome | Exit-gate measure |
|---|---|
| One audit universe and risk-based plan for every tenant type | An ML NBFC, a scheduled UCB, a listed company and a credit co-operative society can each be onboarded with an auto-seeded universe (from the entity profile, departments, products, branches, IT systems, outsourcing register, obligations) and an ACB-approved annual plan in ≤ 2 working days of data being available; ten IAF para 31 parameters are locked for RBIA tenants |
| Every audit type has a governed pack | Programmes, checklists, report templates and timelines exist for: internal audit (Companies Act s.138), RBIA (IAF; RBI (Commercial Banks – Internal Audit Function) Directions 2026, RBI/DoS/2026-27/413; UCB RBIA instructions [VERIFY]), concurrent audit (RBI (Commercial Banks – Concurrent Audit) Directions 2026, RBI/DoS/2026-27/409), IS audit (RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions 2026, RBI/DoS/2026-27/461 ("CYB"); SEBI CSCRF; IRDAI cyber guidelines), IT general controls, VAPT tracking, secretarial audit (s.204, Rule 9, LODR Reg 24A), statutory-audit support (PBC, CARO 2020, Rule 11(g), NBFC Auditor's Report Directions 2026, LFAR for banks), stock and receivables audit, branch audit, data-protection audit (DPDP Rules 2025 r.13 for SDFs), regulatory inspection management, tax-audit support, special investigation, outsourcing/vendor audit, co-operative statutory audit support |
| Evidence without re-keying | ≥ 80% of evidence items in a seeded RBIA engagement are system evidence links (LDC compliance records, policies, minutes, risk data, Finbyx/Udofin records by reference and hash) rather than uploads; every link is hash-pinned and drift-detected |
| Reproducible sampling and analytics | Re-running any sample with the stored snapshot and seed returns identical items; full-population tests run on imported or connected data |
| Findings drive remediation | Every issued finding creates action items in the P04 task engine, a risk-register link (P08) and, where a regulatory breach is flagged, a `ComplianceIssueRaised` event; overdue High findings escalate to the ACB pack automatically |
| Reports in the legally required shape | Report engine produces RBIA, internal-audit, concurrent, IS-audit, MR-3, Secretarial Compliance Report (Reg 24A), CARO clause pack, NBFC Auditor's Report Directions checklist, LFAR question bank (banks), and inspection-response packs as DOCX and PDF/A, with locked mandatory sections; AI may draft narrative, a named human signs |
| Audit Committee ready | One-click ACB pack (plan status, findings by rating and ageing, repeat findings, ATR, HIA in-camera tracker, QAIP, VAPT status, concurrent-audit summary) frozen with hash and tabled through P06 |
| External auditors and supervisors work inside the tool | Time-boxed, read-only, purpose-bound grants (D-12; Ecosystem Spec §4.7) for statutory, IS, secretarial, concurrent and co-operative auditors and supervisors; watermarked capped exports; daily activity report |
| Portability | Every engagement exports to `LDC-EXPORT-1.0` under `10 Audits and Inspections/<Audit type>/<FY>/<Engagement name> - <Period>/` with planning, workpapers, evidence, findings register (XLSX), report and manifest (Appendix M §M.3, X-27) |

---

**Scope.**

**In scope**
- Audit universe (auto-seeded, maintained by change triggers), risk assessment engine, risk-audit matrix, annual and rolling plans, capacity planning, plan approval and amendments.
- Methodology registry (scales, weights, scope tiers, sampling tables, rating definitions, report templates) with versioning and ACB approval.
- Engagement engine for all audit types listed in §4B, one lifecycle with type-specific states and gates.
- Programme and test-step library per audit type and per entity family; control-to-obligation mapping.
- Electronic working papers (index, review hierarchy, review notes, sign-off, file assembly and lock, addenda).
- Sampling (population freeze, methods, seeded PRNG, size calculators, evaluation) and computer-assisted audit techniques (CAATs) over LDC, connected-product and imported data.
- Evidence linking with hash pinning and drift detection; document evidence via the P07 vault.
- Findings lifecycle (condition–criteria–cause–effect, rating, root cause, management response, action plans, extensions, closure packs, independent retest, risk acceptance, repeat detection).
- Action Taken Reports (ATR) for internal, concurrent, IS, statutory, secretarial and regulatory-inspection sources; Risk Mitigation Plan (RMP)/Monitorable Action Plan (MAP) tracking for RBI inspections.
- Auditor registers: statutory auditor (NBFC SA Directions eligibility, tenure, rotation), concurrent auditor (bank directions), secretarial auditor (Reg 24A, CSAS), internal auditor eligibility (s.138, Rule 13), IS auditor (CERT-In empanelment where required), co-operative auditor panels.
- HIA register, independence controls, in-camera meeting tracker, QAIP.
- Statutory-audit support: PBC lists, query log, Auditor's Report Directions checklists, DNBS10 timer, exception-report register, CARO 2020 clause packs, Rule 11(g) evidence pack retrieval, branch-coverage calculator, LFAR question bank (banks), Form A/Form B generation for NBFC auditor appointments.
- Secretarial audit: applicability resolver, SS-1/SS-2 automated checks over P06 meeting data, MR-3 and Secretarial Compliance Report rendering, prohibited-services and tenure checks.
- IS audit, ITGC library, VAPT tracker, continuous auditing jobs.
- Report engine with locked legal sections and tenant customisation.
- Audit dashboards (Internal Auditor, HIA, ACB, CISO view of IS findings, CFO view of statutory audit) and ACB pack builder.
- External-access workspace for auditors and supervisors (shared with P01 grants; audit-specific rooms here).
- Ecosystem bridge: consume Finbyx/Udofin `AuditEngagementOpened`, `AuditFindingRaised`, `AuditFindingClosed`; publish the same events when LDC hosts the engagement; evidence requests by document reference.
- AI touchpoints (P17 agents) for drafting, summarising and suggesting — behind flags.

**Out of scope (owned elsewhere)**
- Performing audits or issuing opinions on behalf of tenants (never).
- Statutory auditors' own working-paper systems and firm-level quality management (SQM 1) — LDC stores only what the firm uploads.
- Fraud classification and reporting (P04/P12 and Finbyx FRM; audit raises a signal only).
- Supervisory-return preparation (P11), though audit may test it.
- Board-meeting conduct and minutes (P06), though secretarial audit tests them.
- Cyber incident response (P12), though IS audit tests it.
- Audit of LawDocsComply itself (SOC 2, ISO — P24 and Appendix Q); LDC's own internal audit uses the Operations Hub assurance room.

---

### Phase P11 — Return Studio, Data Preparation and Accounting Bridge

Indian regulated entities file dozens of periodic, event-based and ad hoc returns to RBI, NABARD, NHB, SEBI, IFSCA, IRDAI, FIU-IND, CERSAI, the GST Network, the income-tax department, the MCA and the four credit information companies (CICs). Compliance teams rarely own the source data; finance, credit and treasury do, often in Tally Prime, Excel and a loan system that may not be Finbyx. This phase gives every tenant a **Return Studio** that turns raw data — wherever it lives — into validated, reconciled, approved, upload-ready files, with the human filer in control and a complete evidence trail.

The design honours three fixed decisions:
1. **Shared kernel (D-05).** Return definitions, cell maps, validation rules and CIC layouts are maintained once, in the Infrabyx returns kernel, and used by both Finbyx and LawDocsComply. LawDocsComply never forks a definition.
2. **Prepare, never file (D-13, NN-08).** LDC generates, validates, reconciles, packages and evidences. An authorised user of the regulated entity uploads on the portal and records the acknowledgement. No portal credential, OTP, DSC PIN, cookie or token is stored, proxied or scripted; no RPA.
3. **Finbyx stays the book of record (NN-23).** For Finbyx tenants, LDC consumes Finbyx `return_run` packages, bureau-cycle records, `PeriodClosed` and `FinancialStatementsApproved` events and never recomputes those returns. LDC computes only for data that is not in Finbyx (non-Finbyx lenders, non-lending entities, group companies, co-operative societies, SEBI/IRDAI/IFSCA entities).

| Outcome | Exit-gate measure |
|---|---|
| A return calendar for every entity type | For an ML NBFC, a scheduled UCB, an ARC, a credit co-operative society, a listed company and an AIF manager, the registry resolves the applicable returns with citations, generates due instances 13 months ahead and shows them in the P04 calendar within 1 minute of profile approval |
| Any source, one pipeline | A non-Finbyx NBFC can load a loan tape (Excel/CSV), a TallyPrime trial balance and GL (via the local agent or XML/JSON export file), a borrowings and investments schedule, and produce DNBS02, DNBS04B and DNBS13 packages reconciled to the trial balance within the template rounding tolerance |
| Finbyx tenants get no duplication | For a Finbyx tenant, every RBI return and CIC cycle appears in LDC from Finbyx events with status, hashes and acknowledgement; "Generate in LDC" is disabled with the reason |
| Deterministic outputs | The same snapshot hash, cell-map version and template hash give a byte-identical file; validation errors cite rule ID and instrument paragraph |
| CIC files for non-Finbyx lenders | Consumer UCRF v3.74, Commercial UCRF v3.10 and MFI UCRF v3.3.1 files built from the loan tape pass the golden-file tests; four bureau outputs from one dataset; incremental W1–W3 and month-end cadence (CIR para 10(2) as substituted from 1 Jul 2026) |
| GST and TDS ready | GSTR-1, GSTR-1A, GSTR-3B, GSTR-9/9C data packages and Form 140/138/144/143 data files (Income-tax Act 2025; 1961-Act forms for earlier periods) are produced with reconciliations and human-filing workflows |
| Accounting bridge | A trial balance mapped once to Schedule III (Division I, II or III), BR Act Third Schedule or the co-operative format produces draft financial statements, notes skeletons and the ratio feed to P09; framework resolved per entity-year with citations (Appendix J) |
| AI that helps but never invents numbers | Vidhi suggests column and ledger mappings, extracts tables from PDF balance sheets and annual reports, explains variances and drafts commentary; every number in a return cell comes from a deterministic computation with lineage (NN-14, NN-22) |
| Evidence and export | Every filing has a sealed evidence pack exported under `11 Returns and Regulatory Reporting/<regulator>/<portal>/<return code>/<period>/` with manifest and acknowledgement (Appendix M) |

---

**Scope.**

**In scope**
- Kernel client: consume `@infrabyx/returns-kernel` (engine) and `infrabyx-returns-packs` (versioned data packs: return definitions, applicability rules, due rules, cell maps, validation rules, CIC format packs, GST/TDS schemas); pin versions per tenant; contract tests.
- Return registry view and applicability resolution for every entity family LDC serves; return due instances in the P04 calendar.
- Data Room: ingestion connectors (Finbyx packages, Udofin packs, TallyPrime agent and file import, Excel/CSV templates, third-party LMS/LOS dumps, ERP exports, SFTP drop, REST API push, PDF financial statements and annual reports via OCR/extraction).
- LDC Canonical Financial Data Model (CFDM) and staging; mapping studio (source → canonical; chart of accounts → element families and statement lines); transformation rules.
- Data-quality profiling and rules; reconciliation (loan tape ↔ TB; sub-ledger ↔ GL; return ↔ TB; cross-return; period-on-period).
- Return generation through the kernel; validation (kernel DSL), reconciliation, maker-checker-signatory approvals, signed package, guided human upload, acknowledgement capture, revisions, supervisory queries.
- CIC submission files for non-Finbyx lenders (consumer, commercial, MFI), rejection ingestion, data-quality index tracking, dispute-clock view (dispute handling itself is P14 + Finbyx).
- GST and TDS/TCS data packages, reconciliations and filing workflows for tenant entities (financial companies and non-financial companies); SFT data where applicable.
- MCA financial-statement filing data (AOC-4 / AOC-4 NBFC (Ind AS) / AOC-4 CFS payloads; XBRL mapping workbook for companies that must file XBRL; MGT-7/7A data from P06 registers).
- SEBI, IFSCA, IRDAI periodic report packs (data preparation and calendar; formats as published) — catalogued in Appendix I.
- Accounting bridge: framework resolver (Ind AS / AS / bank / co-operative / IFRS-IFSC / ICAI non-company), TB import, COA mapping, statement drafting (Schedule III Divisions I–III, Third Schedule Forms A/B, co-operative formats), notes skeletons, Schedule III additional disclosures datasets, ratio feed, CARO and AUD computation feeds to P10, tax-audit data feed.
- Agentic AI data-preparation assistant (P17) with deterministic validators.
- Dashboards for CFO, CCO, Head of Reporting; exports.

**Out of scope**
- Filing on any portal (always human; D-13).
- Bookkeeping or replacing the tenant's accounting system; LDC holds imported books for reporting only (it is not the book of record and does not claim Companies (Accounts) Rules r.3(1) compliance for the tenant's books).
- ECL modelling and IRACP provisioning computation as book-of-record (LDC re-performs classification checks as validations only; Finbyx or the tenant's system computes).
- CIC dispute resolution workflow (P14 grievances; Finbyx RR7 for Finbyx tenants).
- Borrower-facing tax certificates (owned by the RE through Finbyx; Udofin only displays RE-signed certificates — Udofin UB2). LDC does not build borrower tax features; R-079's "borrowers at Udofin" is satisfied by Finbyx/Udofin (master note).
- Payroll TDS computation (P13 computes salary TDS; P11 packages Form 138 data from P13 output).

---

### Phase P12 — Data Protection, Cyber Security, IT Governance and Third-Party Risk (TPRM)

Every client of LawDocsComply processes personal data of borrowers, depositors, investors, policyholders, members and employees, runs regulated technology and depends on vendors. P12 gives the client one place to run its **privacy programme**, its **cyber and IT governance programme** and its **third-party/outsourcing programme**, each driven by versioned law packs and linked to the same obligations, controls, evidence, risks, incidents and Board reporting as the rest of the platform. LawDocsComply is the client's tool; the client remains the Data Fiduciary / controller / regulated entity (NN-14 accountability stays human).

| Outcome | Exit-gate measure |
|---|---|
| A data-protection programme a DPO can run end to end | A seeded NBFC-ML tenant completes: data inventory of 40 processing activities, ROPA export (DPDP + GDPR Art. 30 view), 3 DPIAs, consent-ledger configuration for two purposes, a rights request closed within SLA, and a simulated breach with DPB 72-hour report, CERT-In 6-hour report and RBI DAKSH 6-hour report drafts — all evidenced, in ≤ 1 working day of user effort |
| Multi-law overlay without duplication | One processing activity shows DPDP, GDPR and CCPA obligations side by side, de-duplicated into common controls with law-specific deltas; switching a law pack on/off changes only applicability, never history (NN-29) |
| Sector cyber frameworks as one control library | RBI NBFC Cyber Directions 2026 (RBI/DoS/2026-27/461), RBI Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions 2026 for commercial banks (/410), SFBs (/419), payments banks (/428), UCBs (/437), AIFIs (/456) and credit information companies (/470) [VERIFY numbers; the 2023 bank IT Governance MD is treated as superseded] *(v1.1)*, SEBI CSCRF, IRDAI ICS Guidelines 2023, IFSCA Cyber Guidelines 2025, CERT-In Directions 2022 and ISO/IEC 27001:2022 Annex A load as packs mapped to ≤ 220 common controls; a control test once evidenced satisfies every mapped requirement, with the mapping visible |
| Incident clocks never silently lapse | Every incident with a reportable classification starts each applicable clock (CERT-In 6 h, RBI DAKSH 6 h, IFSCA 6 h, SEBI per CSCRF, DPB "without delay" + 72 h, GDPR 72 h, sector-specific) at the right start event, owned, escalated at 50 %, 75 % and 90 % of the window; a lapse is a Critical exception (NN-31 pattern) |
| VAPT, BCP and DR testing tracked to closure | VA/PT schedule auto-generated from the asset criticality register per the applicable directions (e.g., RBI NBFC 2026 paras 121–126: VA half-yearly, PT annually for critical/DMZ systems); findings tracked to closure with re-test evidence; DR drill records show "DR as primary ≥ 1 working day" where required (para 131) |
| Outsourcing register an RBI inspector would accept | Material-outsourcing classification (paras 14, 58(2) of the NBFC Outsourcing Directions 2025), due diligence, contract-clause checklist (paras 34, 74), half-yearly Board/RMC review (paras 12(1)(vii), 36), exit plan (paras 84–88) — each evidenced and exportable |
| AI governance hooks | Client's AI systems inventory with ISO/IEC 42001-aligned risk assessment and CCPA ADMT / DPDP Rule 13 algorithmic-due-diligence flags |

---

**Scope.**

**In scope**
- `dpc` module: data inventory, data map, processing activities (ROPA), purposes, lawful bases, data categories (incl. sealed classes), systems, recipients, transfers, retention classes; DPIA/PIA/TIA (transfer impact) and LIA (legitimate-interest, GDPR); consent and notice designer for the **client's own** customer journeys; consent ledger and consent-artefact API; data-principal / data-subject / consumer rights desk; breach and incident management with multi-regulator clocks; privacy dashboards; DPO workspace; Significant Data Fiduciary (SDF) pack.
- Cyber and IT governance: ISMS scope, asset and information-asset register with criticality, common control library with framework mappings, Statement of Applicability (SoA), control testing (design and operating effectiveness), cyber-security policy set (with P07), IT Strategy Committee / IT Steering Committee / Information Security Committee support (with P06), CISO workspace, VAPT programme, patch and vulnerability SLA tracking, cyber-audit management (with P10), BCP/DR plan register and test records, cyber crisis management plan (CCMP), threat-intelligence notes, phishing/awareness campaign records (import), log-retention and NTP attestations (CERT-In).
- `tpr` module: vendor/third-party master, outsourcing register (financial and IT outsourcing separately), materiality engine, inherent risk tiering, due-diligence questionnaires (DDQ) with evidence requests sent to vendors via a vendor portal, contract-clause checklist and gaps, SLA and performance monitoring, concentration and sub-contractor (fourth-party) mapping, intra-group outsourcing (Infrabyx-style group service arrangements), offshore outsourcing checks, vendor incidents, annual reviews, exit and termination plans, Board/RMC review packs.
- AI governance hooks: AI system inventory, AI risk/impact assessment templates, model cards, human-oversight attestations, link to `ai` module (P17) for LDC's own AI usage disclosures.
- Exports: ROPA (XLSX/PDF), DPIA reports (DOCX/PDF), breach reports (DOCX/PDF + regulator-form field sheets), SoA (XLSX), outsourcing register (XLSX in RBI-expected column order), Board pack sections.

**Out of scope (and where it lives)**
- LDC's own security programme and certification readiness → Appendix Q and P24.
- Submission to DPB, CERT-In, DAKSH, IFSCA mailbox, SEBI portal — LDC drafts and exports; a human submits (D-13, NN-08). Where an official API appears, it is added behind a flag in P18.
- SIEM/SOC tooling — LDC ingests alerts and incident tickets from the client's SOC (P18 connectors: Splunk, Microsoft Sentinel, Elastic, Wazuh, QRadar via webhook/syslog-to-HTTP relay) but is not a SIEM.
- Consent collection on the client's website/app at runtime at scale: LDC supplies the consent-artefact API, embeddable notice widget and SDK (P18), and is the system of record for consent **artefacts** only when the client chooses (`dpc.consent.mode`). For Finbyx/Udofin borrowers, the capturer remains the producing product (Ecosystem Spec §6.14).
- Registration as a Consent Manager under DPDP Rule 4 — LawDocsComply does not register as one (that requires a separate Indian company with ≥ ₹2 crore net worth and an operating-only-for-Data-Principals model) [REC]; integration readiness with registered Consent Managers is in scope (flag `dpc.consent_manager.integration.enabled = OFF`).

---

### Phase P13 — HRMS, People and Labour Compliance Suite

Regulated finance companies, co-operatives and ordinary companies must run their people function under Companies Act governance (KMP, directors, committees), regulator expectations (fit and proper, CISO independence, Chief Compliance Officer tenure, Internal Ombudsman tenure), the four Labour Codes in force from 21 November 2025, State Shops and Establishments laws, the POSH Act and the Income-tax Act 2025. P13 delivers an HRMS that is (a) **the single people master for every other module** (users and roles are employees; committees and KMP come from here), (b) a **labour-compliance engine** producing registers, returns, wage slips and statutory clocks from signed rule packs, and (c) a **payroll engine** that computes and approves pay while disbursal goes out by bank file or a licensed payout partner (D-11).

| Outcome | Exit-gate measure |
|---|---|
| One people master | A new employee created in P13 can be given a platform role, appointed to a committee (P06) and assigned compliance tasks (P04) without re-entering data; leaver revocation removes all LDC access within 15 minutes and pushes M365/Google suspension where connected |
| Finance-company org out of the box | The onboarding wizard proposes a default department structure for the tenant's entity family (NBFC, bank, UCB, credit co-op, ARC, insurance intermediary, AIF manager, listed company, private company, LLP) which the admin can rename, merge or extend; departments map to the compliance "Department" vocabulary of the tenant's Excel templates (Appendix E column `department` (v1.0: M)) |
| Labour compliance generated, not typed | For a 150-employee NBFC in Delhi and Uttar Pradesh: unified registers, wage slips, appointment letters, leave records, overtime records, POSH annual report, EPF ECR data file, ESI contribution data, PT/LWF (where applicable) and the Labour Codes obligations calendar are produced from transactions; every output cites its rule-pack version |
| Payroll that an auditor can reproduce | A finalised pay run re-computes bit-for-bit from its stored inputs and parameter versions (NN-22); maker, checker and approver are three different people; bank file hash matches the approved register |
| POSH handled with sealing | POSH complaints are in a sealed store with separate keys; only IC members see case content; 90-day inquiry clock owned and escalated; annual report and Board-report disclosure generated without exposing identities (NN-13) |
| Employment agreements signed in-tool | Offer, appointment letter and employment agreement assembled from templates, signed by Aadhaar eSign/DSC through the P07 eSign port, stored with audit trail |
| People-risk to the risk function | Aggregated people-risk KRIs (attrition, key-person vacancy, training completion, concentration of approvals, overdue mandatory leave for sensitive roles) flow to P08 and, by tenant consent, to Finbyx/Udofin as aggregates only |

---

**Scope.**

**In scope**
- **Organisation**: legal entities (from P01), establishments (registered office, branches, units — each with State, address, Labour Code registration numbers, S&E registration), departments, functions, cost centres, positions, grades, reporting lines (solid/dotted), committees link (P06), delegation of powers link (P02 authority matrix).
- **People**: employees (permanent, probationer, fixed-term employee under IR Code s.2(o) / OSH, contract labour via contractor, apprentice, intern, consultant/retainer — non-employee), directors and KMP (shared with P06 `gov.persons`; an individual may be both), POSH IC external member (non-employee, sealed), worker classification (worker vs non-worker under the Codes; supervisory wage cap), documents (with DMS), emergency contacts (minimal), bank details (tokenised, used only for payroll file generation), nominations (gratuity Form, PF nomination).
- **Lifecycle**: requisition → recruitment (light ATS) → offer → background-verification tracking (external vendor results only) → joining → probation → confirmation → transfers/promotions/secondments (incl. group-company secondment for Infrabyx-style groups) → separation → full and final → alumni.
- **Time**: attendance capture (web check-in, mobile PWA geo-optional with consent, biometric/door-access import, Microsoft Teams/Google presence is **not** used as attendance — NN-25), shifts, weekly offs, overtime with consent, work-from-home declarations, regularisation.
- **Leave**: statutory floors (OSH Code s.32, State S&E acts, CoSS maternity) + tenant policies; accrual, carry-forward, encashment; holidays by State; mandatory/forced leave for sensitive positions (bank and NBFC good practice for fraud prevention — "mandatory leave" for staff in sensitive positions [VERIFY current RBI instrument]).
- **Payroll**: salary structures, CTC → components, statutory wage base (Code on Wages s.2(y) 50 % rule), EPF/EPS/EDLI, ESI, PT, LWF, gratuity provision, bonus, overtime, arrears, loans/advances, reimbursements, TDS on salary (Income-tax Act 2025 s.392; companion pack `ita25-salary-tds`), payslips, pay registers, bank/payout file, accounting journal export to `acc` (P11) / Tally / Finbyx.
- **Labour compliance**: Labour Codes obligations (content packs), unified registers and forms, returns (EPF ECR, ESIC, PT returns, LWF, annual returns under the Codes when portals publish formats), establishment registration tracking, inspection-scheme readiness, notices display, committees (Works Committee, Grievance Redressal Committee, Safety Committee where applicable, POSH IC), standing orders/model standing orders for ≥ 300 workers, contract-labour licensing and principal-employer obligations, POSH module.
- **Engagement & development**: policy acknowledgements, training records (mandatory training: KYC/AML, POSH, information security, code of conduct, DPDP), FinLegal Academy course links (P21), performance goals and reviews (light; full appraisal for LawDocs staff is OH10/OH11), disciplinary records (restricted).
- **Fit and proper and regulatory people controls**: fit-and-proper declarations and Board/NRC assessments for directors and specified senior management, CCO/CISO/IO tenure and independence checks, staff accountability (RBI fraud-risk staff accountability [VERIFY]), key-person register.
- **User provisioning**: employee → LDC user (SCIM to Keycloak), and optionally → M365/Google account creation/suspension via `WORKSPACE_PORT` (R-082).
- **Task allocation**: managers assign tasks to reports (P04 tasks engine) — hierarchy from P13 reporting lines.
- **People-risk metrics** to P08 and the ecosystem (aggregates only).

**Out of scope**
- Holding or moving salary money (D-11): LDC generates the bank file / payout instruction; the tenant's bank or a licensed payout partner executes.
- Statutory return **submission** to EPFO/ESIC/State portals: LDC prepares the upload files and records acknowledgement (D-13).
- Recruitment marketing, job boards at scale (integrate via P18 if needed).
- Infrabyx's own staff HRMS, payroll, appraisal, anti-fraud scorecards → Infrabyx Operations Hub OH10–OH11 (D-03). The shared `infrabyx-labour-rulepack` keeps computations identical.
- Biometric template storage: LDC imports attendance punches only, never biometric templates.

---

### Phase P14 — Grievance Redressal and Customer Support Desk

A borrower, depositor, member, investor, policyholder or customer first contacts the client's help and support channels (website, app, branch, phone, e-mail, WhatsApp, LSP app such as Udofin, LMS borrower portal such as Finbyx). If unresolved, the complaint escalates to the client's Grievance Redressal Officer (GRO), then — where the regulator requires — to the Principal Nodal Officer (PNO) and/or the **Internal Ombudsman (IO)**, and finally the complainant is told how to approach the external forum (RBI Integrated Ombudsman via CMS, SEBI SCORES, IRDAI Bima Bharosa / Insurance Ombudsman, IFSCA, Co-operative Ombudsman or Registrar, Consumer Commission). LawDocsComply hosts the **whole ladder** for the client: the support team closes tickets inside LDC, the GRO has a dedicated workspace, regulator clocks are owned and escalated, and complaint MIS and regulatory reports are generated. The client's website shows the grievance link; the system runs on LDC.

| Outcome | Exit-gate measure |
|---|---|
| One desk from first contact to final reply | A complaint raised on the client's website widget, by e-mail and by Udofin event lands as one ticket per issue (dedup), is acknowledged within the configured time with a reference number, and is resolved, escalated or signposted with every step time-stamped |
| Regulator clocks never silently lapse | For an NBFC tenant covered by the NBFC IO Directions 2026: a partially-resolved complaint is auto-escalated to the IO so that the IO has ≥ 10 days before any RBI/NPCI/card-network TAT, otherwise within 20 days of receipt (cl.14(1)); the final reply issues within 30 days of receipt (cl.14(9)); the RB-IOS 2026 route (30-day wait, then 90-day window) is stated in the final reply |
| Correct ladder per entity type | Ladder templates for bank, NBFC (with and without IO), UCB, credit co-operative/MSCS, ARC, listed company (investors), AMC/AIF/intermediary (SCORES), insurer/intermediary (IRDAI), IFSCA RE, ordinary company/LLP (customers, MCA/IEPF investor grievances), employer (IR Code GRC lives in P13) — selected automatically from the P15 entity profile |
| GRO workspace that saves hours | GRO resolves a complaint in ≤ 5 clicks from inbox with templates, knowledge base suggestions and Vidhi draft reply; bulk acknowledge; SLA-sorted queues |
| Regulatory reports generated | Quarterly IO report to RBI (cl.16(2), due by the 15th after quarter end), Board/Customer Service Committee complaint review with top-5 categories (cl.13(5)), annual report disclosures (complaints received/resolved/pending, maintainability per RBI format [VERIFY current disclosure circular]), SEBI LODR Reg 13(3) quarterly investor-complaint statement, IRDAI grievance returns [VERIFY form] — each export-ready |
| Ecosystem-ready | Finbyx/Udofin `GrievanceRaised` events open tickets in LDC when LDC is the grievance host; `GrievanceUpdated/Escalated` flow back; Equator referral only on the complainant's or RE's explicit choice (never automatic) |

---

**Scope.**

**In scope**
- `grv` module: channels (web widget, hosted portal, e-mail-in, API, WhatsApp Business API via BSP adapter, phone/IVR logging, branch/walk-in entry, social-media mentions as manual intake, physical letters with OCR), contacts (complainants — pseudonymous for analytics), tickets (service requests vs complaints vs grievances — classification), categories and sub-categories (regulator taxonomies mapped: RBI CMS categories, SCORES categories, IRDAI IGMS categories [VERIFY lists]), priorities, SLAs, queues, teams (support L1, L2 product teams, GRO office, PNO, IO office), knowledge base, canned responses, macros, surveys (CSAT, CES), escalations, reopen, merge/split, duplicates, attachments (malware-scanned, P07), translations (P07), consent and privacy (P12 notice in widget), regulatory reports, Board/CSC packs, analytics and root-cause tagging, linkage to compliance obligations (P04), risk events (P08 conduct-risk KRIs), incidents (P12 when a complaint reveals a breach or fraud), and to the rights-request desk (P12 when a complaint is a DPDP/GDPR/CCPA request).
- Embeddable client-side artefacts: JavaScript widget, hosted portal page on a tenant sub-domain or custom domain (CNAME, TLS), React Native/Flutter/Android/iOS SDK wrappers (thin, P18), "Grievance Redressal" footer link snippet with GRO/PNO contact details auto-rendered from P13 positions and the RB-IOS/SCORES/Bima Bharosa signposting text (the client's website must display this information — e.g., NBFC GRO name and contact on website and branches [VERIFY RBC directions para]).
- Ladder engine with regulator clock packs (rule packs, Governed).
- Investor grievances for listed companies and debt-listed entities (SCORES 2.0 sync as manual/semi-automated, LODR Reg 13), member grievances for co-operatives, policyholder grievances for insurers/intermediaries.

**Out of scope**
- Filing on behalf of the complainant with the RBI Ombudsman, SCORES, Bima Bharosa or Consumer Commission — the complainant files; LDC tells them how (NN-08; Ecosystem Spec `OmbudsmanReferralRecorded`: "the borrower files, never Udofin").
- Dispute adjudication — Equator (separate product; referral only on explicit choice, NN-23).
- IR Code employee grievances (P13 GRC) and POSH (P13 sealed) — different desks; the widget routes employees away.
- Call-centre telephony (CTI) as a product — LDC integrates (P18: Exotel, Knowlarity, Ozonetel, Jio Business voice/AI agents after verification, D-14) for click-to-call and call logging.

---

### Phase P15 — Sector Packs and Entity Logic

LawDocsComply is sold to very different organisations: a ₹200 crore NBFC-ICC in the Base Layer, a Tier 3 UCB, a listed HFC, an AIF manager, a GIFT City finance unit, a composite insurance broker, a private limited company with 40 employees, an LLP, or a Maharashtra credit co-operative society with 12 branches. Each has a different regulator (often several), vocabulary, governance organs, mandatory committees, KMP set, returns, calendars and risk profile. This phase delivers the **entity logic layer**: a single, versioned taxonomy and profile, an explainable applicability engine, and **sector packs** that pre-configure each tenant so that a new client sees only what applies to it, with reasons, from the first login — and so that the profile moves automatically and audibly when the entity crosses a threshold or changes category.

| Outcome | Exit-gate measure |
|---|---|
| Right obligations, explained | For the 12 golden entity profiles (§12), the applicability engine selects exactly the expected obligations from the seeded content (precision and recall = 100% against the golden set); every selected or excluded obligation shows a human-readable "why" (rule, attribute, threshold, citation) |
| Separate logic per entity type (R-007) | Departments, committees, KMP roles, vocabulary, dashboards, return calendars, risk taxonomy and Excel template family are seeded from the sector pack in ≤ 60 seconds after profile activation; no NBFC term appears in a co-operative or insurance tenant |
| Thresholds and transitions handled as data | A simulated crossing of ₹1,000 crore assets moves an NBFC-ICC from Base to Middle Layer with an impact report (added/removed obligations, new committees, new returns) and an effective date equal to the date of crossing (SBR para 22), without a code release |
| Multi-regulator entities | A listed NBFC, a UCB (RBI + State Registrar), an IFSC banking unit of an Indian bank, and an NBFC that is also an IRDAI corporate agent each resolve the union of applicable packs with conflicts resolved by the strictest-wins rule |
| Investment, ARC and listed-company extensions | NBFC-ICC/CIC investment-limit monitors, the ARC pack and the listed-company pack (LODR, PIT, SAST, ICDR events) are active for their families and consume Finbyx aggregates where connected |
| Global readiness (D-19) | The jurisdiction-pack framework accepts a non-India pack (EU GDPR overlay used as the pilot) without schema change; no non-India pack is enabled for a tenant unless it is in state `PUBLISHED` with a named reviewer |
| Customisable without super admin (R-024, R-039, R-086) | A client admin can rename departments and committees, add a voluntary obligation ("Suggestive Compliance"), narrow scope with a reason, and adjust KMP sets within the floors; Locked legal floors cannot be loosened by any tenant role (test `NN-28_*`) |

---

**Scope.**

**In scope**
- Entity taxonomy: families, types, sub-types, layers/tiers/categories/size classes, and attributes (§4A–§4B).
- Entity profile per legal entity, bitemporal, evidence-backed, with auto-fetch (P01) and Finbyx/Udofin-fed metrics (§4B).
- Multi-family and group structures (§4C, §4K).
- Applicability rule DSL and engine, explanations, what-if simulator, exemptions and conditional applicability (Excel column `conditions` (v1.0: S)), tenant narrowing/broadening with reasons (§4D).
- Profile-change detection and re-applicability with impact analysis (§4E).
- Sector packs: per-family defaults (departments, committees, KMP sets, calendars, returns, dashboards, risk taxonomy, templates, vocabulary, glossary) (§4F).
- Investment-entity extension (NBFC-ICC investments, NBFC-CIC tests, AIF exposures, IPO and capital-market exposure, REIT/InvIT and SR holdings) consuming Finbyx aggregates (§4G).
- ARC pack and NBFC stressed-asset compliance view (§4H).
- Listed-company pack (LODR, PIT, SAST, ICDR, HVDLE) (§4I).
- Global jurisdiction-pack framework (§4J).
- Pack lifecycle and dependency management with `cnt`, `tpl`, `cfg` (§4L).

**Out of scope (owned elsewhere)**
- Writing the compliance questions themselves (Part 2, Excel sheets; importer in P03).
- Co-operative society day-to-day operations — P16 (this phase supplies the co-operative families and applicability; P16 builds members, elections, AGMs).
- Loan, deposit, trade and valuation processing — Finbyx (NN-23). LDC consumes aggregates and limit-breach events only.
- Board and committee mechanics (P06), risk register and ICAAP calculations (P08–P09), returns preparation (P11), labour and HRMS (P13).
- Licence/registration applications to regulators (CoR, PRAVAAH filings) — LDC prepares checklists and evidence (P04/P11), never submits (NN-08, D-13).

---

### Phase P16 — Co-operative Society Operations Suite

India has about 8.4 lakh co-operatives with about 32 crore members across 30 sectors (National Cooperative Database, as reported by PIB, February 2026), and thousands of credit co-operative societies that hold members' savings without RBI supervision, DICGC cover or a modern governance system. Many still keep registers in paper books, hold AGMs late, miss Registrar returns, carry unrectified audit paras for years, and lose their boards to disqualification under the Act. Failures such as the Adarsh Credit Co-operative Society case (Central Registrar notices and liquidation) show what weak member-eligibility, related-party and audit controls cost depositors.

This phase delivers an **end-to-end operating system for a co-operative society** — registration facts and bye-laws, members and shares, managing committee and office bearers, general body meetings, elections support, statutory registers, funds and appropriation, audit and rectification, Registrar/CRCS returns, inspections, complaints and member communications — with the society's GRC (compliance, risk, audit) on the same platform. For **credit co-operative societies**, loans, deposits, interest and share accounting stay in Finbyx (D-16) and members borrow and repay through Udofin; LDC runs governance, compliance and the prudential monitors.

| Outcome | Exit-gate measure |
|---|---|
| Society runs its affairs in LDC | Pilot Maharashtra credit society and a pilot MSCS can, without LawDocs staff help: admit a member, hold a managing-committee meeting with minutes, convene and record an AGM, file the annual return package, record audit paras and file the rectification report — all within statutory clocks |
| No statutory clock lapses unnoticed | AGM, annual return, audit, rectification, election-notice and director-disqualification clocks each have an owner, alerts at T-60/T-30/T-7 days and escalation; an expired clock without action is a Critical issue (NN-31 pattern) |
| Correct law per society | The engine selects the MSCS Act or the correct State Act pack, and the society's bye-laws as a versioned tighten-only layer; a State with a STUB pack shows "limited coverage" and blocks no operations |
| Credit-society safety | Deposit-eligibility exceptions (deposits only from active voting members), director/relative loan reporting, prudential monitors (CRCS order of 22 Jan 2024 for MSCS; State Act for others) and the "no bank in name" guard are live and visible to the board and auditors |
| Ecosystem coherence | For a society on Finbyx, the member register and share ledger are read from Finbyx (single system of record); for a society not on Finbyx, LDC is the system of record and can export the same contracts to any LOS |
| Vernacular and accessible | Hindi and Marathi labels shipped; notices generated bilingual; WCAG 2.2 AA (NN-21) |

---

**Scope.**

**In scope**
- Society master, legal profile and bye-laws (versioned; amendment workflow with Registrar approval) (§4A).
- System-of-record switch for members and shares (Finbyx vs LDC) (§4B).
- Member and share registers, nominations, transfers, cessation, member classes and rights (§4C).
- Managing committee/board, office bearers, co-option, reservations, disqualifications, recusal and related-party controls (§4D).
- General body meetings (AGM, SGM), notices, quorum, agenda, resolutions, minutes, bye-law amendments (§4E).
- Elections support: term tracking, notices to the election authority, voter lists, programme tracker, results recording; internal office-bearer elections by the board (§4F).
- Committees and meetings (reuse P06) (§4G); statutory registers (§4H).
- Funds, reserves and appropriation view (§4I).
- Audit, audit classification, rectification, concurrent and special audits, inspections and inquiries (§4J).
- Returns to Registrar/CRCS and tax filings calendar (§4K).
- Member complaints and escalation to Registrar/Co-operative Ombudsman (§4L).
- Member communications (§4M).
- Credit-society specifics and Finbyx/Udofin link (§4N); other society types (§4O).
- State rule packs (§4P); amalgamation, liquidation and winding-up events (§4Q).

**Out of scope**
- Loans, deposits, interest, share accounting, dividend postings and recovery execution for credit societies — Finbyx (Part 7G IP2) (D-16, NN-23).
- Member borrowing and repayment journeys — Udofin (Part 7E MG1–MG4, Part 7B UP4).
- Conducting statutory elections — the Co-operative Election Authority (MSCS) or the State Co-operative Election Authority/Commission conducts them; LDC supports the society's obligations and keeps records. Online voting in statutory elections is out of scope unless the authority itself prescribes it.
- Milk procurement, PDS, fertiliser distribution and other sector-specific trading operations (out; adapters only, e.g., the national PACS ERP).

---

### Phase P17 — Vidhi AI Employee, Agents and Knowledge Notebooks

LawDocsComply sells time back to compliance teams, company secretaries, risk officers, auditors and boards. Vidhi is the product's **AI employee**: a governed, always-available colleague that can be given work like a junior team member — "draft the minutes from this recording", "check every evidence upload for the ICAAP pack", "every Monday 9 am, send me the overdue RBI items for the Credit department", "read these WhatsApp screenshots and prepare a type copy", "what does the RBI Master Direction say about our grievance redressal timeline, with paragraph references?" — while staying inside four hard limits: it acts only for a named user and inside that user's permissions; it cites or says it cannot; it drafts and proposes but never approves, signs, files, pays, publishes or sends externally on its own (NN-14); and it never trains on, or leaks across, tenant content (NN-15, NN-01).

| Outcome | Exit-gate measure |
|---|---|
| Vidhi is assignable like an employee | A user can assign any task type in P04 to "Vidhi" from the task form, the command palette (`Ctrl/Cmd+K → "Ask Vidhi to…"`), an `@Vidhi` mention in a comment, or the Vidhi panel. Vidhi acknowledges in ≤ 5 s, shows a plan, executes, and returns the output to the assignee's Work Inbox with a "Review and accept" action. 100% of runs carry the delegating user, the permission snapshot, the tools used and the cost. |
| Scheduled and recurring AI work | A user can schedule a Vidhi job (one-off, RRULE recurrence, or event trigger such as "when an RBI update is published that maps to my department") with a preview of the next five runs, an owner, a stop date and a budget cap. Missed runs (outage) are run once on recovery and labelled. |
| Grounded regulatory answers | On the 400-question golden set (Appendix K §K.7) for RBI-NBFC, SEBI-LODR, IFSCA-FCFU, MCA and DPDP notebooks: citation precision ≥ 0.95, answer faithfulness ≥ 0.92, correct-refusal rate ≥ 0.95 on out-of-corpus questions, zero answers that cite a superseded version as current. |
| Document intelligence | Typed copy of printed scans ≥ 98% character accuracy; handwriting and screenshots show per-line confidence; every low-confidence line (< 0.85) is highlighted for human correction; corrected type copy is versioned beside the original (NN-09). Translation into English from the six UN official languages and the 22 Eighth-Schedule Indian languages, with a "machine translation — not certified" watermark. |
| Drafting in Word | Policy, agreement, agenda, minutes and report drafts are produced as `.docx` with **tracked changes** against the chosen base (model template, tenant template or previous approved version) and Word comments carrying citations; drafts open cleanly in Microsoft Word, LibreOffice and Word for the web (headless render test). |
| Notebooks like NotebookLM | Platform notebooks for every enabled regulator pack and tenant notebooks over the tenant's own documents, with chat, citations to passage level, Studio outputs (summary, FAQ, briefing note, study guide, timeline, comparison table, mind map, flashcards/quiz, slide outline; audio overview behind a flag), sharing within the tenant, and staleness banners when a source is superseded. |
| Safe, auditable, affordable | 100% of AI runs written to the AI run ledger (prompt template version, model, provider, region, sources, tool calls, approvals, output hash, tokens, cost). Prompt-injection red-team suite passes (Appendix K §K.8). Tenant AI budgets enforced; per-plan AI credits metered and visible in Settings → Billing → Usage. |
| India-resident inference | Personal, confidential, financial, HR or legal data is processed only by providers whose inference and storage stay in India (default: Claude via Amazon Bedrock India geographic cross-Region inference, ap-south-1 ⇄ ap-south-2) unless the tenant records a cross-border basis (NN-24). |

---

**Scope.**

**In scope**

- `ai` module and `packages/ai-runtime` (shared runtime used by every module): provider adapter, model registry, routing policy, prompt-template registry, retrieval service, citation verifier, PII redaction, injection filters, output validators, cost meter, AI run ledger.
- **Vidhi AI Employee**: identity (`svc_vidhi` service principal acting on behalf of a user), employee profile per tenant (name shown as "Vidhi"; optional tenant nickname), skills catalogue, task intake, planner/executor agent loop, tool registry with permission scopes and action classes, human-approval gates, memory (tenant-scoped, user-visible, editable), schedules and triggers, run history, outputs to the Work Inbox.
- **Vidhi panel** (dockable right panel and full-page mode; `Ctrl/Cmd+J`), slash commands, "Send to workflow" conversion of any output into a task, approval request, document or comment.
- **Knowledge Notebooks**: platform notebooks (curated per regulator and topic from `cnt`, versioned, read-only for tenants) and tenant notebooks (own sources), chat with citations, Studio outputs, sharing, staleness.
- **Document intelligence**: OCR (print and handwriting), screenshot reading, WhatsApp chat export parsing, email (`.eml`, `.msg`) and letter reading, table extraction, classification and metadata extraction, language detection, translation to English, type-copy editor with versioning.
- **Drafting Studio** (runtime and generic UI; module-specific drafting flows are owned by P06, P07, P09, P10 and P11 and call this runtime): Word drafts with tracked changes, clause library retrieval, citation comments, alignment to template or previous version.
- **Meeting intelligence**: audio/video upload or Microsoft Teams transcript import → transcript → SS-1/SS-2-structured draft minutes (P06 owns the minutes workflow), action items → tasks.
- **Compliance-testing assistant**: evidence sufficiency checks against the obligation's expected evidence (column `evidence` (v1.0: U) of the template) and control activity (column `control_activity` (v1.0: V)), anomaly flags, test-step suggestions for auditors (P10 owns audit records).
- **Analytics narration**: plain-English commentary on dashboards, ratio movements, stress-test outcomes and KRI breaches (numbers always come from deterministic engines; NN-22).
- **Evaluation harness**, red-team suite, model cards, AI release gates.
- **Metering and budgets**: AI credits per plan (values in P20 Pricing Catalogue), per-tenant and per-user budgets, alerts, hard stops, batch mode for bulk jobs.
- **Provider adapters**: Amazon Bedrock (Claude, India geographic CRIS — default), Anthropic first-party API (global; restricted classes), optional Jio adapters (LLM only after an enterprise contract with India residency and no-training terms; voice and messaging adapters are P18), OCR/translation adapters (Claude vision default; Bhashini, Azure AI Translator Central India, Google Cloud Translation asia-south1 as alternates).

**Out of scope (owned elsewhere)**

- AI question authoring from a new Master Direction (P05 owns the workflow; it calls this runtime and skill `V-SK-12`).
- The minutes, resolution and policy approval workflows (P06, P07); ICAAP document assembly and stress-test computation (P09); audit report assembly (P10); return data preparation rules (P11); grievance case workflow (P14). P17 supplies the skills those phases call.
- Outbound AI voice calls and WhatsApp agents to the client's customers (P18 `VoiceProvider` and `MessagingProvider`; P14 for grievance acknowledgements). Vidhi may draft scripts and messages; sending is a P18 channel action behind human approval.
- Model fine-tuning on tenant data (prohibited, NN-15). Platform-level fine-tuning on synthetic or public regulatory data is deferred; if ever proposed it needs an ADR, a DPIA and a Board-approved AI policy.
- Autonomous browsing of regulator portals or any third-party website on behalf of a tenant (no RPA or scraping; Ecosystem Spec §10.2). Platform-side regulatory monitoring is P05.

---

### Phase P18 — Integration Gateway, Ecosystem Connectors and Developer Platform

LawDocsComply must connect to the rest of the Infrabyx ecosystem (Finbyx, Udofin, Equator, LawDocs, the Infrabyx Operations Hub, FinLegal Academy) and to the systems its customers already run (third-party LOS/LMS/LSP and recovery systems, Tally and other accounting packages, Microsoft 365 or Google Workspace, their websites and apps, eSign providers, messaging and calling providers) **without redesign** each time a new counterparty appears. The answer is one integration gateway with a small set of stable contracts — versioned REST, CloudEvents over signed webhooks, a connector SDK, mapping packs and a file fallback — and an onboarding path that lets a new company, a group company or a channel partner connect in days, not projects.

| Outcome | Exit-gate measure |
|---|---|
| Ecosystem contracts implemented exactly | LDC passes the Ecosystem Spec §14.3 certification suite groups Contract, Security, Idempotency and ordering, Resilience, Reconciliation and privacy, Operations, External and group access, Risk feed, Archive and storage — and emits `ConnectorCertified` for the Finbyx↔LDC, Udofin↔LDC and Ops Hub↔LDC connectors in sandbox |
| Compliance-mode switch works both ways | A Finbyx tenant can move from `EMBEDDED` to `LDC_EXTERNAL` (and back) with obligations, controls, open issues and the evidence index carried over (hash-chain heads reconciled), dual-publishing for one compliance period, zero lost records (Ecosystem Spec §9.1) |
| New counterparty without code in the core | A certified third-party LMS connector (Apache Fineract reference adapter) and a generic CSV/SFTP layout are onboarded by mapping pack only; a fictitious "Lender X LOS" is connected in ≤ 5 working days in the sandbox with no change to `cmp`, `erm`, `ral` or `ret` code |
| Self-service onboarding data | A prospect entering a PAN or CIN in the health check (P23) or onboarding wizard (P01) gets name, constitution, registration date, registered address, status, directors (for companies/LLPs), GSTINs and LEI pre-filled from licensed sources in ≤ 5 s p95, with consent captured and source attribution shown |
| Calendars everywhere | Tasks and deadlines appear in Microsoft 365, Google Calendar, Outlook.com, Gmail and Apple Calendar (through native sync or ICS/CalDAV), role-scoped, within 5 minutes of a change, with reminders reaching the user's phone through their own calendar app |
| Website and app embeds | A client NBFC puts a "Grievance Redressal" button on its website or app (script tag, hosted page or API) in ≤ 1 hour; complaints land in its P14 grievance desk with acknowledgement in seconds |
| Developer platform | Public developer portal with OpenAPI 3.1 and AsyncAPI 3.0 references, sandbox tenants with synthetic data, client self-registration with tenant-admin approval, SDKs (TypeScript, Python, Java), Postman collection, status page and changelog |
| Safe by default | Every inbound and outbound call authenticated, scoped, rate-limited and logged; personal data never leaves India through a connector unless a recorded basis exists; regulator portals handled as `PORTAL_MANUAL` only (no credentials, OTPs, cookies, RPA or scraping) |

---

**Scope.**

**In scope**

- `int` module: API gateway configuration (edge), contract registry client, OAuth 2.x authorisation server profile for machine clients (Keycloak), client registry, scopes, consent records, rate limits, webhook subscriptions and delivery, event catalogue, outbox relay, inbox de-duplication, DLQ and replay, connector runtime (SDK host), mapping-pack runtime, integration monitor, on-premises agent management, developer portal, sandbox provisioning, connector certification.
- **Ecosystem connectors**: Finbyx (all LDC-relevant domains in Ecosystem Spec §§6.15, 6.18–6.23, 6.26, 9), Udofin (LSP-side GRC, grievance, DLG disclosures, risk metrics for RE-scoped KRIs), Equator (grievance → ADR opt-in referral, litigation/ADR status for the compliance register), LawDocs (templates, eSign envelopes, advisory requests, public professional directory references), Infrabyx Operations Hub (provisioning acknowledgement, catalogue read, claims gate, usage aggregates, support-ticket hand-off metadata), FinLegal Academy (`trainings.lawdocs.in` LMS — catalogue, enrolment, completion, certificates).
- **Third-party lending and recovery systems**: LOS/LMS/LSP/recovery/collections connectors through the connector SDK; inbound generic GRC connector contract (Spec §9.2); OSCAL export/import (Spec §9.4); CSV/XLSX/SFTP registered layouts (Spec §3.11, §12).
- **Accounting sources** (transport only; transformation is P11): TallyPrime (XML/JSON over the on-premises agent), Zoho Books, SAP Business One/S/4HANA (OData), Busy and Marg via export files [VERIFY APIs], generic trial-balance CSV/XLSX.
- **Identity, KYB and registry adapters** for onboarding: PAN verification, company/LLP master (licensed aggregators), GSTIN, LEI (GLEIF), Udyam, DigiLocker (consented document pull), Aadhaar-based eSign through ESPs (no Aadhaar storage), regulator public registers (RBI NBFC/ARC/UCB lists, SEBI intermediary lists, IRDAI, IFSCA, co-operative registrars) as downloaded datasets for verification.
- **Workplace**: Microsoft 365 (Entra ID SSO/SCIM, Graph calendar, Teams meetings and transcripts, Outlook mail send/receive for designated mailboxes, OneDrive/SharePoint document libraries, Word for the web opening), Google Workspace (later; same port), personal calendars via ICS subscription and CalDAV (Apple iCloud), Outlook.com and Gmail via ICS or OAuth calendar APIs.
- **eSign and stamping** adapters (Leegality, Digio, SignDesk, Surepass, eMudhra; DSC desktop signer; e-stamp through ESP partners).
- **Communications**: email (Amazon SES ap-south-1 / customer SMTP relay / Microsoft 365 send-as), SMS (DLT-registered; JioCX SMS and other aggregators), WhatsApp Business Platform (JioCX WhatsApp or another BSP), voice (JioCX Voice, Jio SIP Trunk through a CPaaS, Exotel/Plivo as alternates), RCS (JioCX RCS, flag), web push, in-app; Haptik conversational agents as an optional channel for client customer-support intake (flag).
- **Embeds**: grievance and help-desk widgets, public policy disclosure pages, complaint status tracker, JavaScript SDK and mobile deep links; client website/app/LMS/LOS/LSP integration APIs (R-098).
- **Tenant onboarding by API** for group companies, Finbyx/Udofin cross-sell, channel partners and enterprise groups (R-002).

**Out of scope**

- Business logic of the modules that consume connectors (P04 calendars and notifications, P07 DMS, P11 return transformation, P13 HRMS, P14 grievance, P19 export and storage targets, P20 billing — although the Razorpay adapter lives in `int` and is used by P20).
- Filing to regulator portals by machine (D-13; Spec §10.2 `PORTAL_MANUAL`). The gateway contains **no** HTTP client configured for RBI, SEBI, IFSCA, IRDAI, MCA, GSTN, CERSAI, CKYCR or income-tax portal domains (certification test "Filing boundaries", Spec §14.3).
- Credit-bureau pulls for onboarding (see FR-P18-33 — LDC is not a specified user under CICRA 2005 for a SaaS sign-up purpose).
- Accessing borrower, member or loan-level personal data from Finbyx/Udofin beyond the Ecosystem Spec projections (risk feed is pseudonymised and aggregated; Spec §6.22).

---

### Phase P19 — Data Preservation, Portability and Bring-Your-Own Storage

A company that uses LawDocsComply must never feel trapped. On any day — while subscribed, during a regulator's inspection, at the auditor's request, or when it leaves — it can take **all of its data** as an ordinary folder tree of Word, Excel, PDF and CSV files whose folder and file names explain themselves to a beginner, verify that nothing was altered, open everything with Microsoft Office or LibreOffice, and load it into another system. It can also keep a **continuous copy in its own storage** (its S3 bucket, Azure or Google storage, SharePoint/OneDrive, SFTP server, NAS or hard disk in its own data centre). And because the structure is defined by a versioned contract rather than by today's code, the folders do not move when LDC ships new features, changes its database, moves data centre or changes cloud: **no customer ever has to migrate their own data because LDC changed**.

The same folder taxonomy works in reverse: instead of uploading hundreds of compliance documents one by one, a company can drop a structured folder (or its existing SharePoint library) and LDC files each document against the right entity, year, department, obligation, committee or policy.

| Outcome | Exit-gate measure |
|---|---|
| Everything is exportable | The export-coverage test passes: every persisted record type in every module has an export mapping; a seeded tenant with every record type produces an `LDC-EXPORT-1.0` package in which 100% of records are present (count reconciliation per type) and 100% of documents are byte-identical to the stored originals (SHA-256) |
| Understandable without LDC | Usability test: 5 of 5 non-technical participants (a junior accountant, an office manager, a new compliance executive, a director, an external auditor) find a named Board resolution, a policy's approved version, the evidence for a specific compliance and the audit trail of a status change within 3 minutes each using only Windows Explorer/macOS Finder and Office |
| Verifiable offline | The open-source verifier (Apache-2.0) confirms hashes, the detached JWS signature, control totals and audit-chain continuity offline; it fails on a single changed byte or missing file |
| Stable across releases and infrastructure moves | Golden-tenant test: the same synthetic tenant exported before and after (a) a release with schema changes, (b) a database engine major upgrade, (c) a storage-provider swap, (d) a region move rehearsal produces **identical folder paths and file names** for unchanged records and identical record IDs; differences appear only as additive files declared in the package's `CHANGES-SINCE-PREVIOUS.csv` |
| Bring-your-own storage | A tenant connects at least one target (S3, Azure Blob, GCS, SharePoint/OneDrive, SFTP, on-premises agent to NAS/disk); residency verified; canary passes; daily incremental and monthly full copies arrive by 06:00 IST; restore test from the tenant's own copy passes |
| Folder intake | A 5,000-file structured folder is imported with ≥ 95% automatic placement on a well-structured tree (100% on a tree previously exported by LDC), duplicates detected by hash, every unplaced file listed in a review queue, nothing overwritten |
| Exit without friction | Exit export (scope EXIT) completes for a 500 GB tenant within 48 hours, followed by a read-only period, a deletion workflow that respects retention and legal hold, and a signed deletion certificate |

---

**Scope.**

**In scope**

- `xpt` module: export map registry, export jobs, package builder, folder policy, manifest, signing, verifier, download service, scheduled exports and backups to customer targets, intake (folder/zip/library) with mapping rules and review queue, rehydration/loader tool, exit workflow, deletion certificates, data-principal access exports (for P12 DSR responses), regulator/auditor/board packs (scoped exports used by P06, P10, P11, P15 and external-access grants).
- `StorageTarget` adapters (built on P18's connector framework): Amazon S3 (and S3-compatible: MinIO, Wasabi India, on-prem object stores), Azure Blob, Google Cloud Storage, SharePoint/OneDrive (Graph `Sites.Selected`), Google Drive (shared drive; non-regulated data only), SFTP, on-premises agent (NAS/SMB share, local disk, USB/external disk on the agent host, on-prem object store).
- Storage-key scheme and object metadata independent of code layout; content addressing; immutable versions.
- **Durability guarantees** across releases and infrastructure changes (§4E): stable IDs, expand-contract migrations, export-mapping contract tests, data contract versioning, infrastructure-move runbooks.
- Cross-product package sharing using the shared archive standard (Finbyx/Udofin evidence references, Equator referral packs by reference), and the `portability` ecosystem events (Spec §6.26).

**Out of scope**

- Platform disaster recovery, internal backups, PITR and DR drills of LDC's own infrastructure (P24; this phase only consumes their evidence). Customer copies are **in addition to**, never a replacement for, LDC's own backups.
- Business rules on what each module retains (each module and P12 retention schedules); P19 enforces retention classes and legal holds on exports and targets.
- Ops Hub exit-project tracking (OH4 receives status and counts only).

---

### Phase P20 — Pricing, Plans, Subscriptions, Billing, Savings and Revenue Streams

LawDocsComply must sell itself: a visitor runs the free health check, sees exactly what the product costs for an organisation like theirs, starts a 7-day trial without talking to anyone, and converts by paying online — while a large bank or NBFC can still negotiate an enterprise contract. Every price, component, discount, promotion and trial rule is data, so the owner can change strategy without a release (R-070). Revenue streams that do not work can be switched off (R-044). Clients see, in money and hours, what the product saves them — but only on a transparent, evidenced method (R-067, NN-19).

| Outcome | Exit-gate measure |
|---|---|
| Transparent public pricing | `/pricing` renders three packages (Essentials, Professional, Enterprise), a comparison table of ≥ 60 feature rows and every add-on with its price delta, entirely from the published presentation catalogue; Lighthouse accessibility ≥ 95, WCAG 2.2 AA manual pass (NN-21); prices shown "excl. GST" with the GST-inclusive total shown before payment |
| Apple-style configurator | A visitor configures package + components + scale + billing cycle and sees the itemised running total update in ≤ 150 ms per change; dependencies and exclusions explained inline; configuration can be saved, shared as a link and converted to a quote |
| Self-serve trial → paid | From the end of the health-check report to an active trial tenant in ≤ 5 minutes and ≤ 12 clicks (PAN/CIN fetch pre-fills the organisation); from trial to paid subscription in ≤ 6 clicks via Razorpay-hosted checkout; no auto-conversion (OH8.9) |
| Owner controls commerce without code | Super admin can change a price, add a component, publish a promo code, extend one company's trial, re-order the feature list or retire a package; each change goes through maker-checker with a preview of the public page and of affected tenants, and takes effect on its `effective_from` without a deployment |
| Entitlements enforced server-side | Every module checks `entitlements.check()` on the API; UI hiding is never the control; a lapsed or restricted subscription never blocks reading, exporting, auditor or supervisor access, or any statutory deadline workflow already in progress (OH8.7; NN-29) |
| Billing and membership settings | Tenant admin can see plan, components, usage, seats, AI-credit wallet, invoices, payments, mandates, billing profile, tax documents, renewals and exit — 15 settings pages (§6) — and do every routine billing task without raising a ticket |
| Revenue-stream switches | Each LDC stream (Appendix N §N.6, RS-LDC-01…RS-LDC-30) can be turned on/off by market, segment and channel, with a kill switch that withdraws the purchase option within 5 minutes while honouring existing contracts |
| Honest savings | The Savings Dashboard shows hours saved, cost avoided and penalty exposure managed, each labelled *Recorded*, *Modelled* or *Estimated*, with the formula, inputs and evidence links one click away; no savings figure leaves the tenant (marketing, case studies) without the client's written consent and a claims-gate PASS (NN-19) |

---

**Scope.**

**In scope**

- **Presentation catalogue** (`bil.presentation_*`): packages, components (add-ons), feature rows, comparison groups, explainers ("i" help), badges, FAQs, configurator rules (dependencies, exclusions, bundles, minimums), localisation, SEO metadata — versioned, maker-checker, effective-dated.
- **Commercial catalogue integration**: SKUs, price books, coupons, trial policies and stream gates are owned by **OH8** (Appendix X §X.8); LDC consumes the signed catalogue (`GET /v1/catalogue/versions/{v}`) and submits change requests from the LDC Pricing Studio (`POST /v1/catalogue/change-requests`, new API in Appendix X). Interim `LOCAL` adapter (flag `bil.billing_port.mode = LOCAL_INTERIM`) implements the same port inside `bil` until OH8 is live, with a scripted migration to OH8 (§4L).
- **Public pricing page and configurator** (`apps/public`), embedded configurator in the onboarding wizard and tenant settings (`apps/web`).
- **Self-serve onboarding commerce flow** R-069: health check → account → trial tenant → organisation fetch → section selection → computed price → trial → convert → pay.
- **Trial management**: default 7 days, per-company extension, trial plan, AI-credit cap, expiry behaviour, reminders.
- **Checkout** via OH8 orders → Razorpay-hosted pages (cards, UPI AutoPay, netbanking, eNACH, Smart Collect virtual accounts) and "invoice later / purchase order" for enterprise.
- **Subscriptions**: monthly, quarterly, annual and multi-year terms; upgrade, downgrade, add/remove components, seat and entity changes; proration preview from OH8 quotes; renewals; cancellation; exit hand-off to P19.
- **Entitlement enforcement SDK** (`packages/entitlements`): modules, features, limits (users, legal entities, storage, AI credits, regulator packs, connectors, API calls), soft/hard limit behaviour, grace, `RESTRICTED` semantics.
- **Usage metering** at source and monthly `UsageRecorded` aggregates to OH8 (AI credits, extra storage, pass-through eSign/KYC/SMS, API calls) — aggregates only, never user or record identifiers.
- **Invoices, credit notes, statements of account, receipts, TDS certificates** — issued by OH8, displayed and downloadable in LDC; billing e-mails.
- **Billing & Membership settings** (15 pages, §6).
- **Promo codes, discounts, referral credits (non-professional referrers only), service credits** — catalogue objects from OH8; LDC validates and displays.
- **Revenue-stream registry mirror** (`bil.stream_gates`) and kill switches; purchase options appear only for `ACTIVE` streams.
- **Savings Dashboard** and Savings Ledger (`bil.savings_*`) with methodology registry, penalty library linkage (Appendix G penalty rules; Appendix N §N.9).
- **Super-admin Pricing Studio** in `apps/console` (presentation editor, change requests to OH8, preview, publish, per-tenant overrides and trial extensions — all via Correction-Entry-safe, maker-checker flows, D-02).
- **Marketplace checkout reuse**: P21 services and retainers use the same quote/order/invoice components (first-party services) — P20 builds the shared components.

**Out of scope (other phases or systems)**

- Price, tax, proration and invoice computation (OH8; LDC computes none — Ecosystem Spec §6.27).
- Razorpay keys and webhook secrets (OH8 vault only; the `LOCAL` adapter uses a separate LDC Razorpay account only if the owner approves OI-P20-01).
- Marketplace provider onboarding, engagement workflows and Academy sync (P21).
- RM portfolio and delivery console (P22).
- Health-check questionnaire engine and report (P23); P20 consumes its `HealthCheckCompleted` event.
- Revenue recognition (OH8.8), GSTR-1 preparation for LawDocs' own GST (OH8.6), collections and legal recovery (OH8.7).

---

### Phase P21 — Marketplace, Retainers and FinLegal Academy

The LawDocsComply Marketplace is the place where an organisation buys the human expertise that the software alone cannot provide — compliance retainers, virtual CXO support, drafting of policies, agreements, annual reports and ICAAP documents, stress testing and risk assessments, return-filing support, audit-readiness, certification readiness (SOC 2, ISO, PCI DSS), VAPT and trainings — **with or without a software subscription**. It is open to anyone without logging in (R-036), starts with LawDocs' own professionals and opens to outside providers later (R-035), and is designed so that LawDocs never breaches the professional-conduct rules that bind advocates, chartered accountants, company secretaries and cost accountants (D-06).

| Outcome | Exit-gate measure |
|---|---|
| Public, browsable catalogue | `/marketplace` lists ≥ 60 seeded first-party offerings in ≥ 12 categories (Appendix O §O.2), each with scope, deliverables, exclusions, timeline, price basis and "who this is for"; browse and search need no login; WCAG 2.2 AA |
| Services without SaaS | A non-subscriber can buy a fixed-price service in ≤ 8 clicks (buyer account + GST profile + Razorpay checkout) and receive deliverables in an Engagement Room; later conversion to a full tenant carries the engagement record across |
| Custom offerings and pricing | LawDocs delivery leads (and, when enabled, outside providers) publish offerings with their own scope, price model (fixed, milestone, retainer, hourly band, quote-only) and SLA; every offering passes legal-category and claims checks before going live |
| Retainers with SLA eSign | A retainer goes from proposal to eSigned SLA to active RM assignment (P22) in ≤ 2 working days; monthly invoices, service-hour or deliverable tracking and SLA credits run automatically |
| Professional-conduct compliance | Per-profession switches enforce listing mode, commission, ratings and call-to-action rules; advocates and CAs in practice are never listed with commerce features unless counsel clears it; CI tests prove forbidden fields cannot be rendered |
| FinLegal Academy | Courses from trainings.lawdocs.in appear in the marketplace with live price, next batch and enrolment link; corporate seat bundles can be quoted and invoiced; completion certificates flow back as compliance evidence where the learner consents |
| Billing | First-party services invoiced by the LawDocs selling entity through OH8 with GST; direct-model provider invoices captured; invoices e-mailed to buyers; refunds and disputes handled with credit notes |

---

**Scope.**

**In scope**

- Public marketplace (`apps/public` `/marketplace/*`), in-app marketplace (`apps/web` "Services" menu), buyer accounts, provider workspace (`apps/delivery` for LawDocs staff; provider portal for outside firms when enabled).
- Service catalogue model: categories, offerings, packages, add-ons, price models, SLAs, deliverable templates, eligibility rules by buyer entity type, conflict and independence checks.
- Provider model: first-party LawDocs teams; outside providers verified through OH9 (and LDC-specific checks); per-profession commercial and display rules.
- Engagement lifecycle: request → scoping → proposal/quote → engagement letter/SLA eSign → payment → delivery with milestones → acceptance → invoice → close → review; change requests; cancellations; disputes and refunds.
- Retainers: retainer plans, hour banks or deliverable baskets, SLA definitions and credits, monthly service reports, renewal, RM-as-maker hand-off (P22).
- Engagement Room for buyers without a tenant (secure messages, files, milestones, approvals, eSign, invoices).
- Certification-readiness services (SOC 2, ISO 27001/27701/42001/22301/9001, PCI DSS), VAPT, and the independence wall between readiness and certification.
- FinLegal Academy listing feed, corporate seats, learner-consented certificate import.
- Ratings and feedback (only where permitted), moderation, grievance officer for the marketplace.
- GST/TCS handling options per commercial model, invoices, credit notes, e-mail delivery.

**Out of scope**

- Group professional directory and empanelment (OH9) — consumed, not rebuilt.
- RM portfolio, credential vault, delivery work inside tenants (P22).
- LMS itself (trainings.lawdocs.in remains the system of record for courses, enrolments, assessments).
- Equator ADR services (never listed as a lender-side add-on; Ecosystem Spec §8.6; OH8.2 Equator rules) — the marketplace may show a neutral informational link to Equator's own site in the "Disputes" category only if the owner enables it (`mkp.category.disputes.equator_link`, default OFF).
- Payment aggregation by LawDocs (LawDocs never holds a third party's money; Razorpay Route or direct billing only).

---

### Phase P22 — Service Delivery Console and Operations Hub Interface

LawDocs serves its clients through people — relationship managers (RMs), company secretaries, chartered accountants, compliance analysts and legal professionals — who do real work *inside* each client's LawDocsComply tenant. The **Service Delivery Console** (`apps/delivery`) is their workplace: one portfolio across all clients, one section per client, and a governed way to act as a **maker** inside the client's tenant while the client's own employee remains the **checker** (R-072). It holds the client's portal credentials safely (D-04), keeps messages and shared files in one place (R-073), shows billing and SLA status, and talks to the Infrabyx Operations Hub for CRM, tickets, customer success, timesheets and billing (D-03) — without copying client compliance content into the Hub (OH Part 4.5).

| Outcome | Exit-gate measure |
|---|---|
| One portfolio | An RM sees all assigned clients with health, SLA risk, due items and unread messages on one home screen; time to open any client section ≤ 2 clicks |
| Governed maker access | A delivery maker grant is proposed by either side and approved only by the client's tenant admin; scope by department/function/obligation set; max 12 months per grant (renewable); delivery users can never act as checker, approver, board member or auditor in a client tenant (test `NN-05_delivery_never_checker`) |
| Credential vault | Credentials are owned by the client admin, revealed only to named grantees with step-up MFA, every reveal logged and visible to the client; RBI portal credentials default to client-only; no bulk export exists |
| Client communication | Secure messages, shared drive links (SharePoint/OneDrive/Google Drive) and deliverables are reachable from the client section; every file shared lands in the client's DMS with a hash |
| Commercial visibility | RM sees plan, components, renewal, invoices status and retainer usage (read-only from P20/OH8); cannot change prices or entitlements |
| OH integration | Tickets, CRM activities, CS health inputs, timesheets and milestone acceptances flow to OH through Ecosystem-Spec events/APIs, carrying no compliance content; a contract test proves no obligation text, evidence or credential ever leaves LDC |
| Anti-fraud and productivity | Every action is attributable to a named staff member; work is measured by outputs (tasks, SLAs, deliverables), not covert monitoring (NN-25); SoD and access reviews quarterly |

---

**Scope.**

**In scope**

- `apps/delivery` web application (Next.js), realm `ldc-staff` (Keycloak), phishing-resistant MFA (FIDO2/passkeys) for all delivery users.
- Staff directory projection from OH (identities, employing legal entity, job role, manager, status) via SCIM/OIDC from the group identity provider (OH1/OH10).
- Portfolio and assignment management (RM, backup RM, professionals, reviewer per client).
- Per-client section with tabs: Overview, Engagements & retainers, Work, Calendar, Act in tenant, Credentials, Messages, Files & drive, Deliverables, Billing, SLA & reports, Health, Notes, Activity.
- Tenant delivery grants (propose/approve/renew/revoke/expire) and **Act-in-tenant** session mode with visible banner and scoped permissions.
- Client-side creation of maker users for professional services, and LawDocs-side requests to create maker users (R-072).
- Credential Vault (stored in the client tenant; delivery console is a client of it).
- Messaging (client ↔ delivery team), e-mail bridge, meeting links.
- Shared drive links and deliverables register; file delivery into the client DMS.
- Read-only billing view and retainer usage; upsell proposals (quotes) for client acceptance.
- SLA tracker and monthly service report (from P21) in delivery context.
- Interfaces to OH: tickets (OH6), CRM activities and requests (OH3), CS health signals (OH5), timesheets/utilisation (OH4/OH11), onboarding milestones (OH4), billing events (OH8), staff lifecycle (OH10) — all through Ecosystem-Spec contracts.
- Cross-company work: one staff identity, product-specific roles; Finbyx/Udofin/Equator work happens in their own products (deep links), never through LDC.

**Out of scope**

- CRM, marketing, customer-success playbooks, support desk, staff HRMS/payroll/appraisal, internal-controls engine (OH).
- Platform super-admin functions (provisioning, master-data correction, global settings — `apps/console`, P00/P01/P02); the delivery console never edits client master data — it can only request a change, which a super admin applies via Correction Entry (R-074).
- Client tenant features themselves (compliance, governance, policies…) — the delivery maker uses the normal tenant UI under a delivery session.

---

### Phase P23 — Public Website, Free Compliance Health Check, Help Centre, Tutorials and Accessibility

LawDocsComply is sold self-serve to thousands of NBFCs, co-operative societies, intermediaries and companies that will not take a sales call before they trust the product. The public website, the free Compliance Health Check and the learning surfaces are therefore the first product most buyers use. This phase delivers a fast, accessible, search- and AI-discoverable public site; a free health check that gives a genuinely useful, indicative result and converts into a 7-day trial; a help centre, "i" glossary and tutorial library that let users understand regulatory terms and features without calling support; and an accessibility programme that makes every LawDocsComply surface usable by people who are blind, low-vision, deaf, hard of hearing, motor-impaired or neurodivergent — which is also a regulatory obligation that many LawDocsComply customers themselves now carry (SEBI digital-accessibility circular of 31 July 2025; draft RPwD (Amendment) Rules 2026).

| Outcome | Exit-gate measure |
|---|---|
| Content visible to crawlers and AI retrieval | Every public page returns its full primary content in the initial HTML response (no client-side-only rendering); `curl` of `/`, `/pricing`, `/solutions/nbfc`, `/health-check`, `/glossary/crar` shows headline, body and structured data. `/llms.txt` is served as `text/plain`. (Fixes the 25 Oct 2026 finding that the live site returns an empty SPA shell — Appendix R §R.9.) |
| Fast and stable | Core Web Vitals at the 75th percentile on mobile (CrUX or RUM): LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1; Lighthouse performance ≥ 90 on the five template types |
| Free health check works end to end | An anonymous visitor completes the check for any of the 12 launch families (Appendix P §P.3) in ≤ 12 minutes median; receives an on-screen result immediately, a PDF and a share link; the lead reaches the Operations Hub CRM within 60 seconds with consent flags; the visitor can start a 7-day trial with the entity profile pre-filled in ≤ 2 clicks |
| Honest results | Every report carries the D-15 disclaimer; every score is reproducible from the stored answers, question-bank version and scoring-model version (NN-22); no report says "compliant", "certified" or "audit-ready" (NN-19) |
| Claims governed | 100% of numeric claims, logos, testimonials, certifications and regulatory-recognition statements on published pages link to an approved, unexpired Claims Register entry; the build fails otherwise |
| Self-help reduces support | Every menu item, column header and form label in the tenant app that names a regulatory or product term has an "i" key resolving to a published glossary entry (coverage report = 100% of registered keys); help panel opens contextually from every screen; ≥ 40 tutorial videos with captions and transcripts published (Appendix P §P.5) |
| Accessible | WCAG 2.2 Level AA conformance of the public site and of every authenticated screen shipped to date, evidenced by automated checks in CI (zero serious/critical axe violations), a manual assistive-technology test cycle and an independent IAAP-certified audit; an Accessibility Conformance Report (ACR) published in human- and machine-readable form; an accessibility grievance channel live (NN-21) |
| Measurable discoverability | Search Console and Bing Webmaster verified; IndexNow pings on publish; a monthly "AI answer panel" of 30 fixed buyer prompts runs and reports named/cited presence separately (§4M.12) |

---

**Scope.**

**In scope**
- `apps/public` (Next.js 16, App Router, static generation with incremental revalidation) for the marketing site, solutions pages, pricing page rendering, marketplace and academy public entry pages, resources, regulatory updates hub, glossary, blog, case studies, trust centre, legal pages and the health check.
- The `web` module: headless CMS (pages, blocks, versions, locales, redirects, experiments), Claims Register, health-check engine (question banks, scoring models, sessions, reports, share links), leads and marketing consents, public regulatory-update summaries.
- The `hlp` module: glossary and "i" key registry, help-centre articles, contextual help, product tours and checklists, tutorial library and learning paths, media assets (images, diagrams, screenshots, videos, captions, transcripts, sign-language renditions), release notes.
- The accessibility programme across all apps: design-token corrections, component rules, user accessibility preferences, document and chart accessibility, the test plan, the accessibility statement and ACR, the accessibility grievance channel, the CI gate.
- Technical SEO/GEO: rendering, metadata, structured data, sitemaps, robots and AI-crawler policy, `llms.txt`, internal linking, redirects from the current site, measurement.
- Ethical funnel and nurture surfaces: landing-page variants, webinar registration, paid "expert review" tripwire hand-off to P20/P21, trial onboarding checklist; the Hub (Appendix X) remains the system of record for leads, campaigns and sends.

**Out of scope (owned elsewhere)**
- Pricing catalogue, configurator logic, checkout, invoices (P20). This phase renders and tests the page.
- Marketplace listings, provider onboarding, orders (P21); academy course delivery (trainings.lawdocs.in LMS).
- CRM, campaign automation, Brevo/Adobe Express sends, social calendar, PR, staff performance (Infrabyx Operations Hub; Appendix X).
- Tenant onboarding wizard internals and trial provisioning (P01); this phase hands over a pre-fill payload.
- Authenticated-app information architecture and screen inventory (Appendix C, P02) — this phase supplies help, glossary and accessibility layers into it.
- A native mobile app (D-01: PWA only in v1.0).

---

### Phase P24 — Engineering Governance, Hardening, Certification Readiness and Go-Live

The owner will push code to GitHub regularly — patches, new features, framework upgrades, infrastructure moves — while banks, NBFCs, listed companies and co-operative societies rely on LawDocsComply for records that regulators, auditors and boards will inspect. P24 makes change safe and provable: every change is reviewed, tested, approved, traceable to a release and reversible; data and the client's folder structure survive every release and every infrastructure move; backups are tested by restoring them; vulnerabilities are found and fixed within published SLAs; and the platform is ready for independent assurance — SOC 2 Type 1 then Type 2, ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 42001 (AI), ISO 22301 (continuity) and PCI DSS self-assessment for the payment flow — without making any certification claim before a certificate or report exists (NN-19).

| Outcome | Exit-gate measure |
|---|---|
| Every production change is approved and traceable | 100% of production deployments in the last 30 days map to a change record with `ChangeApproved` (OH13) and a signed image digest; 0 deployments outside the pipeline |
| Releases never break client data or folder structure | Expand-contract checker, export-mapping contract (NN-10) and golden export comparison pass for every release; zero manual customer migration steps in release notes (NN-11) |
| Recoverability proven | Latest restore test of every T0 store succeeded within RTO; a full DR drill to ap-south-2 met RPO ≤ 15 min and RTO ≤ 4 h; evidence stored |
| Security debt under control | No open Critical; no High older than its SLA; VAPT (CERT-In empanelled auditor) final report issued after retest with all Critical/High closed |
| Certification-ready | Appendix Q control set implemented with automated evidence for ≥ 80% of controls; policy set approved by the Board; readiness assessment by an external firm with no Critical gaps; SOC 2 Type 1 audit window can start |
| Go-live safe | Go-live checklist (§4J) signed by CTO, CISO, Company Secretary and product owner; first paid RE tenants live on the AWS production estate (P00 ADR-0006) |

---

**Scope.**

**In scope**

- GitHub organisation, plan, repositories, branch model, rulesets, CODEOWNERS, required checks, merge queue, signed commits, environments and deployment protection.
- Change management: change classes, risk scoring, change records, CAB (via OH13), freeze windows, emergency changes, post-implementation review; tenant notices and API deprecation policy.
- Release management: release trains, versioning, release rings (internal → canary tenants → general), feature flags for progressive delivery, release notes (internal and customer-facing), customer sandbox tenants.
- Content releases vs code releases: regulatory content publication (P05) is governed separately and never requires a code deployment; code releases never alter published content.
- Database migration safety, schema evolution and data-preservation guarantees across releases and infrastructure moves.
- Patch and vulnerability management with SLAs; dependency and image hygiene; end-of-support register.
- Backup, restore testing, disaster recovery, business continuity; BYO-storage backup evidence (P19).
- Security testing: SAST, DAST, SCA, secrets, IaC, container, API fuzzing, AI red-teaming hooks; VAPT and the CERT-In comprehensive audit; responsible disclosure.
- Audit readiness for LawDocsComply itself: IS audit, internal audit, external audit, client audits of LawDocsComply as their service provider; evidence collectors; auditor read-only workspace (provider-assurance room in OH14).
- Certification readiness: SOC 2, ISO 27001/27701/42001/22301, PCI DSS v4.0.1 SAQ A for hosted checkout; policy set; risk register; supplier management; access reviews.
- Hardening: application, cloud, Kubernetes/ECS, database, identity, email, DNS, web headers, CSP, bot and abuse protection.
- Performance, load, soak and chaos tests; capacity planning.
- Incident management, status page, customer communication, regulatory incident clocks (CERT-In 6 hours; client RE notification ≤ 2 hours so the RE can meet its 6-hour duty; DPDP breach intimation and 72-hour report).
- Go-live checklist and post-go-live operations (hypercare, SLO reviews, monthly security report to the Board's committee).

**Out of scope**

- The group-wide engineering-operations console and CAB tooling (OH13) and the certification control library and provider-assurance room (OH14) — built in the Operations Hub; LawDocsComply emits events and evidence to them and consumes `ChangeApproved` (D-03; Appendix X).
- The policies themselves (information security policy, access control, etc.) — the owner prepares them (brief); P24 lists them (Appendix Q §Q.11), provides templates in the policy module (P07) and records approvals.
- Tenant-facing IT governance features for clients (their own ISMS, VAPT tracking, CERT-In incidents) — P12.

---

### Phase P25 — Global Jurisdiction Packs, Multi-Region Cells and Partner Network *(v1.1)*

LawDocsComply is India-first, but its customers are increasingly groups with entities abroad and foreign groups with entities in India; the owner wants to take it global. Lawrbit, the reference competitor, delivers abroad by combining one regulatory-intelligence feed with local law and accounting firms, translation of foreign laws, project-based discovery and AWS hosting in India and Frankfurt (Appendix Y §Y.2). This phase makes LDC able to switch on any country **as content and configuration, not code**, and to beat that model on transparency (coverage statements, reviewer of record, clause-level official-language provenance), residency (regional cells with a home region per legal entity) and openness (a partner marketplace the client can see and choose from).

| Outcome | Exit-gate measure |
|---|---|
| Global entity management | A group with an Indian parent and 12 foreign subsidiaries in 6 jurisdictions is onboarded in ≤ 2 hours of admin time; each entity has a structure-chart position, officers, registers and a 12-month jurisdiction calendar computed in its own time zone and holiday calendar; India ODI/FLA checkpoints are linked to each foreign subsidiary |
| Jurisdiction packs as data | A new country pack (Tier C) authored in `LDC-TPL-INTL-GEN-v2.0` passes import, reaches `PILOT` and then `PUBLISHED` with reviewer of record and coverage statement, and generates obligations for a pilot tenant — with **no code release** (NN-34) |
| Regional residency | The EU cell runs a full tenant plane in an EU region; a UK subsidiary's personal data and documents never leave the EU cell (verified by data-flow tests and access logs); the parent's group dashboard shows the entity's status via aggregates only |
| Transparent coverage | Every published pack shows in-scope/out-of-scope areas, reviewer of record, last-verified date, freshness SLA and monitoring status; a pack whose monitoring is stale > 30 days becomes `SUSPENDED` with a banner automatically |
| Partner network | At least one content partner and one delivery partner onboarded per G1 corridor through the partner portal with due diligence, DPA and scorecard; on-call query desk answers within SLA in the pilot (first response ≤ 1 business day) |
| Localisation | `en-GB`, `en-US`, `hi-IN` and `ar-AE` (RTL) locales pass WCAG 2.2 AA checks on the top 30 journeys; legal text displayed in official language + English with provenance |
| Cross-border commerce | A foreign client can buy a pack subscription in USD or EUR, receives an OH8 invoice with the correct export/reverse-charge wording, and the payment settles without card data touching LDC |

---

**Scope.**

**In scope**

- Jurisdiction hierarchy (country, subdivision, special zone) across content, entities, calendars, holidays, currencies, languages (Appendix Y §Y.4.2).
- Jurisdiction-pack lifecycle with `PILOT` (§5.1), tiers C/B/A and overlay packs, coverage statements and freshness metrics.
- INTL-GEN template family import path (validator, reviewer-line check `LDC-TPL-041`), country templates later.
- Global entity management (`gem`): structure chart, entity records for foreign forms, officers across entities, jurisdiction registers, filing calendars, registered agents, licences, intercompany agreements, India ODI/FDI linkage, foreign registry data adapters, filing packs.
- Regional cells (IN existing; EU first; GCC, SG, US templates), global control plane, home region per legal entity, routing, aggregation API for group views, per-cell AI routing, per-cell exports and backups.
- Transfer register integration, sub-processor lists per cell, adequacy/negative-list watchers.
- Partner portal: content partner, reviewer, delivery partner, implementation partner roles; due diligence; scorecards; query desk.
- Localisation: ICU messages, locales, RTL, locale formats, jurisdiction glossary.
- Global regulatory change: per-cell local-time scans, `REG_INTEL_PORT` licensed feeds, partner change notices.
- Cross-border commerce hooks into OH8: currencies, tax treatments, export invoices, withholding documentation.

**Out of scope**

- Writing the full content of foreign packs (content team and partners, tracked as content deliverables).
- Direct e-filing to foreign registries (prepared filing packs only, unless an official API is verified and the client authorises — NN-08).
- Foreign legal advice by LawDocs (partners only, D-32 extended).
- China and Saudi personal-data processing (D-46, D-46) until decisions are taken.
- A US cell build (template only; built on contracted demand).

---

### Phase P26 — Litigation, Legal Matters, Contracts, Licences and Ethics Registers *(v1.1)*

Every regulated entity and company carries legal exposure that today lives in lawyers' e-mails and spreadsheets: notices received and sent, court and tribunal cases, regulator inspections and show-cause proceedings, contracts with renewal and notice traps, licences that silently expire, and conflicts of interest that boards are required to manage. This phase gives the General Counsel, the CS and the CCO one governed register for all of it, connected to the compliance calendar, the Board, the accounts and the evidence vault — so that no limitation date, hearing, reply window, renewal or regulator commitment is missed, and every provision and disclosure is traceable.

| Outcome | Exit-gate measure |
|---|---|
| No missed legal deadline | Every notice and matter has an owner and computed due dates (reply window, hearing, limitation, appeal); zero unowned clocks in the pilot; reminders at T-7/T-3/T-1 by default; missed-deadline incidents = 0 in UAT scenarios |
| Notices handled same day | Incoming notice → OCR → classification proposal → triage owner in ≤ 1 business day for 95% of notices in the pilot; reply-on-time ≥ 98% |
| Orders become actions | An order with directions creates P04 tasks with due dates in one confirmation step; compliance with directions is tracked to closure |
| Regulator engagements controlled | Inspection RFIs, observations and MAP/RMP items are tracked to closure with evidence and closure-verification tests (P10); regulator SCNs and adjudications are tracked with reply windows and appeal limitation |
| Financial reporting fed | Quarterly provision and contingent-liability schedule (Ind AS 37/AS 29, §J.16) produced from matter assessments; Reg 30 material-litigation cases opened for listed entities from qualifying matters |
| Contracts and licences under control | Contract repository with extracted obligations, renewal and notice-period alerts; licence register with renewal tasks generated ≥ lead time before expiry; zero expired licences in the pilot without an open renewal task |
| Ethics managed | Conflict-of-interest, gifts and hospitality, and related-party declarations collected by campaign and event; conflicts drive recusal in P06; whistle-blower intake routed to the sealed vigil mechanism |
| Lender boundary respected | For Finbyx tenants, recovery litigation appears as a read-only projection from Ecosystem events; LDC never issues SARFAESI/recovery notices or recomputes recovery exposure (NN-39, D-41) |

---

**Scope.**

**In scope**
- Notice management: incoming notices of all types (statutory, tax, regulator, labour, corporate, consumer, IP, shareholder, civil and criminal), outgoing non-recovery notices and replies, notice master with reply windows and severity.
- Matter (case) management: courts, tribunals (NCLT, NCLAT, DRT/DRAT as party other than lender-recovery, ITAT, CESTAT, SAT, TDSAT, APTEL, RERA, consumer commissions, labour fora), writs, criminal matters, arbitration and mediation, insolvency proceedings where the tenant is a creditor or corporate debtor in non-recovery capacity; hearings, orders, appeals, execution, settlement.
- Counsel management: empanelment, conflict checks, engagement letters, fee arrangements, invoices, scorecards; counsel portal.
- Legal spend: budgets, accruals, invoice validation (rate card, GST, TDS fields), approvals; payment hand-off only.
- Provisioning and disclosure: likelihood assessment, Ind AS 37/AS 29 classification, quarterly movement schedule to P11, Reg 30 cases to P06, RBI inspection annexure views.
- Regulator engagements: inspections (RBI RBS/ISE, NHB, NABARD, SEBI, IFSCA, IRDAI, Registrars, labour, tax audits by authorities), RFIs, exit meetings, observations, RMP/MAP items, compliance submissions, closure; regulator proceedings (show-cause notices, adjudication, compounding, consent settlement, penalties, appeals).
- Contract lifecycle (CLM): intake, authoring via LawDocs templates, negotiation with redlines, approval by value/risk, execution (eSign/e-stamp checklist), repository with hierarchy, obligation extraction, renewals and expiry, termination; outsourcing contracts linked to P12.
- Registrations and licences register: certificates of registration, GSTIN, Shops & Establishments, trade licences, FSSAI where relevant, IEC, professional tax, labour registrations, software licences of regulatory relevance, ISO certificates, DSCs of the entity (metadata only), domain registrations; renewal workflows.
- Ethics registers: conflicts of interest, gifts and hospitality, related-party declarations (feeding P06 RPTx), outside business interests, and the link to the sealed vigil mechanism (whistle-blower intake and case handling stay sealed).
- MIS for the legal function (feeds P28), exports, AI assistance (drafts only).

**Out of scope**
- Lender debt recovery (SMA/NPA engine, recall, SARFAESI ss.13(2)/13(4), possession, valuation, auction, DRT original applications as lender, IBC s.7 as financial creditor) — Finbyx Recovery Suite / standalone Udolex (Ecosystem Spec §6.8, §6.10; D-41). An optional "Recovery Notices Lite" pack for lenders without Finbyx is specified behind flag `lit.recovery_lite.enabled = OFF` pending counsel opinion (OI-P26-03).
- Filing in courts or e-filing portals, payment of court fees or counsel fees, service of notices by LDC itself (LDC prepares, the user files or dispatches; NN-08).
- Legal advice: LDC is not a law firm; reserved advocacy services are delivered by eligible practitioners through P21 (D-32).
- ADR adjudication (Equator Resolution — referral only on explicit choice, as in P14).
- POSH inquiries (P13 sealed module) — P26 only receives counts.

---

### Phase P27 — ESG, BRSR, CSR and Sustainability *(v1.1)*

Listed companies, large companies under the CSR provisions, and regulated lenders now carry sustainability obligations that combine disclosure, assurance, spending rules and risk management. The owner's baseline treated ESG as a full module; this phase builds it so that the CSO, CFO and CS can capture metrics once, compute GHG emissions with traceable methods, produce the SEBI BRSR (and BRSR Core subset ready for assurance or assessment), run the CSR cycle without missing an unspent-amount deadline, and give the Board a sustainability view — all in the same governed, evidence-backed way as compliance.

| Outcome | Exit-gate measure |
|---|---|
| Know what applies | Applicability engine switches on BRSR, BRSR Core, value-chain (voluntary), CSR, climate (RBI), green finance and voluntary frameworks per entity profile with explanation and citation |
| Capture once, use many times | Each metric captured once with unit, period, boundary, method and evidence; reused in BRSR, ratings questionnaires, board packs and voluntary frameworks; ≥ 60% of a repeat year's BRSR auto-populated |
| Assurance-ready | Every BRSR Core attribute has lineage from source evidence to disclosed number; maker-checker per KPI; frozen at assurer sign-off; first-time assurance with zero lineage gaps in the pilot |
| GHG done properly | Scope 1, Scope 2 (location- and market-based) and material Scope 3 categories computed with versioned emission factors stamped on each figure; base-year and restatement policy enforced |
| CSR never late | CSR obligation computed from financials; action plan approved; spend tracked; unspent-transfer deadlines owned with reminders; Form CSR-2 data sheet generated; zero missed CSR deadlines in UAT |
| Climate risk joined up | Climate risks in the P08 register; scenario inputs to P09; RBI climate-finance obligations tracked for lenders |
| Board visibility | ESG dashboard and Board/committee pack sections (P28) with targets vs actuals |

---

**Scope.**

**In scope**
- Sustainability applicability engine and obligation packs (SEBI BRSR and BRSR Core; Companies Act CSR; RBI climate-finance directions; SEBI green debt; ESG rating engagement; voluntary ISSB/TCFD/GRI; EU CSRD/ESRS for EU-exposed groups via P25).
- ESG metric library, data capture (forms, imports, connectors), unit validation, period and boundary management, maker-checker per KPI, evidence links.
- BRSR builder (Sections A, B, C; nine principles; essential and leadership indicators) and BRSR Core subset; XBRL/exchange-format hand-off data for human filing.
- Double materiality assessment.
- GHG accounting engine (GHG Protocol) with emission-factor library and restatement policy.
- Value-chain partner disclosures (voluntary) with partner data collection portal.
- Assurance/assessment workspace for external assurers/assessors.
- CSR engine (s.135, CSR Rules) end to end, including CSR-1 checks, unspent account, impact assessment, Form CSR-2 data.
- Climate and transition: risks, targets, transition plan tracker, scenario inputs.
- ESG ratings and sustainable finance registers (ratings, green/blue/yellow/transition debt use-of-proceeds and impact; green deposits for REs).
- Targets, dashboards, board reporting, exports.

**Out of scope**
- Filing BRSR on exchange portals and CSR-2 on MCA (prepare and validate only; NN-08).
- Carbon-credit trading, registry operations or offsets verification.
- Product-level life-cycle assessment and environmental engineering calculations beyond the GHG Protocol corporate inventory.
- Rating opinions — LDC never rates (it supports ESG Rating Provider data requests).
- Lender portfolio-level financed-emissions computation from loan data belongs to Finbyx (data owner); LDC receives aggregates (Scope 3 category 15) if Finbyx publishes them (Ecosystem change request, OI-P27-09).

---

### Phase P28 — Reports, MIS and Board-Pack Studio

Every module of LawDocsComply produces information that someone must read, decide on, or send to the Board, a committee, an auditor or a supervisor. Today most Indian regulated entities assemble this information in Excel and PowerPoint, re-keying numbers from several systems, with no proof of where a figure came from and no way to reproduce last quarter's pack. Users of incumbent GRC tools report the same pain: reports that need the vendor to change, dashboards rebuilt user by user, board packs built outside the tool, and large reports that time out (Appendix Z §Z.9; IMP-071 to IMP-075, IMP-141).

P28 gives one governed reporting layer for the whole product: every module publishes its data once as a **governed dataset**; every number shown anywhere comes from that layer (and, for financial and risk metrics, from P09's certified values); every report and pack can be re-run "as at" its original date and produce the same result; and business users — not the vendor — build their own dashboards, reports and packs.

| Outcome | Exit-gate measure |
|---|---|
| One source of numbers | Every widget, report cell and pack figure resolves to a dataset field or a P09 metric version with provenance and as-of date; a CI check fails any widget bound to an ungoverned query |
| Role dashboards on day one | Each of the 22 role layouts in Appendix C §C.6.2 renders from seed data with mandatory widgets, drill-down to records in ≤ 3 clicks and "View as table" on every chart |
| Users build their own | A CCO builds a custom "overdue High checkpoints by department and regulator" report with a chart and formula column, saves it as a template and schedules it monthly to the MD in ≤ 10 minutes without support |
| Reproducible reports | "Re-run as at" of any approved report reproduces the original output byte-for-byte (same snapshot hash, template version and parameters) |
| Board packs inside the product | The pilot NBFC-ML composes its quarterly Board compliance and risk pack from saved sections, freezes it (hash), and the CS attaches it to the Board meeting in P06 — no Excel or PowerPoint outside LDC |
| MIS catalogue | The seed MIS catalogue (§4G) is installed for the pilot family with owners, frequencies, recipients and approval paths; the RBI inspection "Management and Systems" MIS file (§4H) is produced in one run |
| Performance | Dashboard p95 < 2 s at 50,000 compliance instances per tenant; a 50,000-row report completes asynchronously in < 2 minutes with notification; a 200-page pack renders in ≤ 60 s |
| Safe AI assistance | Vidhi drafts report definitions and variance commentary from bound values only; a narrative containing an unbound figure cannot be published (NN-37) |

---

**Scope.**

**In scope**
- `rpt` schema and services: dataset registry, field catalogue, data classes and row policies; KPI dictionary; metric bindings to P09; point-in-time snapshots.
- `packages/dashboards` (widget runtime used by every app shell), widget catalogue management, role layouts, personal and shared dashboards, dashboard library, next-best-action card host.
- Reports tab: catalogue, run, my reports, ad-hoc builder (no code), templates with inheritance, scheduler, subscriptions, approvals, distribution, retention.
- MIS framework: four MIS tiers, fourteen MIS categories, MIS metadata schema, seed MIS catalogue, inspection MIS file mapping, standard administrative and management reports.
- Report- and board-pack studio: compose, version, review, approve, freeze/hash, watermark, render (DOCX, PDF and PDF/UA, PPTX, XLSX), distribute to P06 meetings and to subscribers, addenda.
- Natural-language report drafting and narrative commentary with Vidhi (bound figures only).
- Embedding (signed embed tokens) and analytics feeds (OData/REST with RLS) for Power BI, Excel and other BI tools.
- Group, multi-entity and multi-currency views; localisation of labels and formats.
- Due-diligence snapshot (§4N); anonymised cross-tenant benchmarking (flag OFF).
- Export mapping of report definitions, runs, packs and snapshots (NN-10).

**Out of scope**
- Computing regulatory, financial or risk metrics (P09 owns definitions, computation and certification — Appendix H §H.0A).
- Meeting logistics, notices, attendance, minutes and the board portal itself (P06). P28 supplies packs and report papers to P06 meetings.
- Preparing or filing regulatory returns (P11; NN-08). Regulator-format MIS in P28 is for internal and inspection use, not filing.
- Replacing an enterprise BI tool: P28 provides governed feeds to external BI tools rather than a general-purpose analytics workbench.
- Marketing and platform-operations analytics (Operations Hub OH2 and P24 engineering metrics).

---


# PART D — APPENDIX INDEX

| Appendix | File in the pack |
|---|---|
| Appendix AA — Future-Ready AI and Agentic Architecture *(v1.1, new)* | `appendices/AA_Future_Ready_AI_and_Agentic_Architecture.md` |
| Appendix AB — RBI Consolidated Directions: Content Plan and Catalogue *(v1.1)* | `appendices/AB_RBI_Consolidated_Directions_Content_Plan.md` |
| Appendix AC — Baseline and Brief Traceability Matrix *(v1.1)* | `appendices/AC_Baseline_and_Brief_Traceability_Matrix.md` |
| Appendix A — Workflows and State Machines (binding) | `appendices/A_Workflows_and_State_Machines.md` |
| Appendix B — Data Model, Events and Error Codes | `appendices/B_Data_Model_Events_and_Error_Codes.md` |
| Appendix C — Information Architecture, Screens, Menus and Dashboards (binding) | `appendices/C_Information_Architecture_Screens_Menus_and_Dashboards.md` |
| Appendix D — Roles, Personas and Access Control Matrix (binding) | `appendices/D_Roles_Personas_and_Access_Control_Matrix.md` |
| Appendix E — Excel Template Contract, Entity Families and Importer | `appendices/E_Excel_Template_Contract_Entity_Families_and_Importer.md` |
| Appendix F — Regulatory Source Register and Monitoring Catalogue | `appendices/F_Regulatory_Source_Register_and_Monitoring_Catalogue.md` |
| Appendix G — Legal and Regulatory Rules Register | `appendices/G_Legal_and_Regulatory_Rules_Register.md` |
| Appendix H — Risk Taxonomy, Basel Mapping, ICAAP, Stress Scenarios and Ratio Library | `appendices/H_Risk_Taxonomy_Basel_ICAAP_Stress_Scenarios_and_Ratio_Library.md` |
| Appendix I — Regulatory Returns, Credit-Bureau and Tax Return Catalogue | `appendices/I_Regulatory_Returns_CIC_and_Tax_Return_Catalogue.md` |
| Appendix J — Accounting, Auditing and Secretarial Standards Map | `appendices/J_Accounting_Auditing_and_Secretarial_Standards_Map.md` |
| Appendix K — Vidhi AI Agent Specification | `appendices/K_Vidhi_AI_Agent_Specification.md` |
| Appendix L — Integration Adapters and API Catalogue | `appendices/L_Integration_Adapters_and_API_Catalogue.md` |
| Appendix M — Export Package `LDC-EXPORT-1.0` and Folder Taxonomy | `appendices/M_Export_Package_LDC-EXPORT-1.0_and_Folder_Taxonomy.md` |
| Appendix N — Pricing, Plans, Add-ons, Revenue Streams and Savings Model | `appendices/N_Pricing_Plans_Add-ons_Revenue_Streams_and_Savings_Model.md` |
| Appendix O — Marketplace Services Catalogue and Professional Rules | `appendices/O_Marketplace_Services_Catalogue_and_Professional_Rules.md` |
| Appendix P — Website Copy, Health-Check Question Bank, Glossary Priorities, Tutorial and Video Plan, SEO/GEO System | `appendices/P_Website_Copy_SEO_GEO_Tutorials_and_Video_Plan.md` |
| Appendix Q — Security, Privacy and Certification Readiness | `appendices/Q_Security_Privacy_and_Certification_Readiness.md` |
| Appendix R — Competitive Research and Differentiation | `appendices/R_Competitive_Research_and_Differentiation.md` |
| Appendix S — Co-operative Societies: Law and Operations | `appendices/S_Cooperative_Societies_Law_and_Operations.md` |
| Appendix T — HRMS, Labour Codes, Registers and Payroll Parameters | `appendices/T_HRMS_Labour_Codes_Registers_and_Payroll_Parameters.md` |
| Appendix U — Configuration Framework and Settings Catalogue (binding) | `appendices/U_Configuration_Framework_and_Settings_Catalogue.md` |
| Appendix V — Acceptance Tests and UAT Catalogue | `appendices/V_Acceptance_Tests_and_UAT_Catalogue.md` |
| Appendix W — Verification Log and Open Items | `appendices/W_Verification_Log_and_Open_Items.md` |
| Appendix X — Operations Hub Addendum for LawDocsComply | `appendices/X_Operations_Hub_Addendum_for_LawDocsComply.md` |
| Appendix Y — Global Compliance Expansion and Jurisdiction Packs *(v1.1)* | `appendices/Y_Global_Compliance_Expansion_and_Jurisdiction_Packs.md` |
| Appendix Z — Customer Feedback, Reverse Engineering and Improvement Backlog *(v1.1)* | `appendices/Z_Customer_Feedback_Reverse_Engineering_and_Improvement_Backlog.md` |
