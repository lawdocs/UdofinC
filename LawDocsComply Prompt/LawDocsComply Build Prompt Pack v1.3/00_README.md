# LawDocsComply — Build Prompt Pack v1.3

**Prepared:** 25 October 2026 · **v1.3:** 26 October 2026 (adoption of the Infrabyx Platform Baseline Standard v1.0; supersedes v1.2, v1.1 and v1.0, which are kept in `_Archive (older versions)`) · **v1.2:** 25 October 2026 (Excel template and workflow rework) · **Owner:** Company Secretary, Infrabyx Group · **Product:** LawDocsComply (lawdocscomply.com), the Infrabyx group's governance, risk and compliance (GRC) SaaS for RBI, SEBI, IFSCA and IRDAI regulated entities, companies, LLPs and co-operative societies, with data-protection, cyber, labour, tax, ESG and AI-governance overlays — India first, built to take global compliance later · **Companions:** Infrabyx Platform Baseline Standard (IPB) v1.0 *(v1.3; binding — `docs/ipb/`)*, Infrabyx Ecosystem Integration Specification v1.2, LawDocs Build Prompt Pack v1.1, Equator Resolution v3.2, Finbyx v1.6, Udofin v1.3, Infrabyx Operations Hub v1.1 *(v1.2 named Spec v1.1, Finbyx v1.5, Udofin v1.2, OH v1.0, Equator v3.1)*
**Stack (locked, D-01/X-05; IPB-01 and D-59–D-60 in v1.3):** **Node.js 24.22.1** · Next.js 16 (`apps/web`, `apps/public`, `apps/console`, `apps/delivery`) · NestJS 11 modular monolith · PostgreSQL only, with RLS, in regional cells (India: AWS Mumbai, DR Hyderabad; Supabase database-only in non-production) · Temporal · Redis · OpenSearch · S3 Object Lock · Keycloak · Cerbos · GoRules ZEN + CEL · every vendor behind an IPB-01 port with two adapters · `packages/vidhi` kernel (Claude via Amazon Bedrock India as the reference adapter; OpenAI/Azure, Gemini, Grok, Sarvam, self-hosted behind flags) · shared `packages/cms`, `brand`, `hlp`, `trust`, `feedback` · MCP server and client · Docker, Helm and Terraform per cloud

---

## 1. What this pack is

A paste-ready, phase-by-phase build prompt for a coding agent (Claude Code or equivalent) to build LawDocsComply end to end on the Infrabyx Platform Baseline Standard v1.0 *(v1.3)* — **Part 1** of the owner's two-part plan — plus the tools for **Part 2**: 29 Excel templates under template contract v2.0 (27 question families plus the Risk and Governance registers), the question-writing commands, and the RBI Directions Catalogue that sets the order in which the 28 November 2025 consolidated directions are turned into question sheets.

### What v1.3 changes (pack lead instruction of 26 October 2026: adopt the Infrabyx Platform Baseline Standard v1.0 across every product pack) *(v1.3)*

The six Infrabyx products now inherit one baseline — the IPB (`docs/ipb/`, thirteen files, ≈ 132,000 words) — by reference, and each pack records only what it does differently. For LawDocsComply, the audit found the strongest Vidhi, "i" registry, settings-security and Health Check/Claims Register material of the six packs and a few gaps (policies not drafted, no `.env`, Node version floating, Brand Studio and vendor-assurance room partial). v1.3 does the following:

- **IPB adoption clause and precedence** (master §5.0, §18 X-67): master → IPB → Ecosystem Spec v1.2 → `02` → appendices → phase file; LDC may only be stricter; deviations `IPB-DEV-01` (CMS tables stay in schema `web`) and `IPB-DEV-02` (L/G/T tiers kept and mapped to USER/ORG/PLATFORM).
- **Stack pinned** (master §5.1–§5.2): Node.js 24.22.1 (the v1.2 `[VERIFY]` is closed), PostgreSQL only, ports with two adapters named for every vendor, shared packages `vidhi` (the former `agents`, X-68), `cms`, `brand`, `hlp`, `trust`, `feedback`, `consent-ui`, `marketing`; containers, Helm and Terraform per cloud; IPB adoption notes (§5.6) incl. the `fut.*` flags that touch LDC and the Claude artefacts note.
- **Decisions** (`02` §2.6): D-59–D-70 mirror IPB-D-01…12; D-71 policy drafts; D-72 public Brand Studio; D-73 user-post programme; D-74 image generation with mandatory human review; D-75 the Vendor Assurance Room as a core tenant feature; D-76 the twenty-node settings tree. New rules NN-61–NN-64 (seeds never in production; no tag before consent; synthetic images reviewed and labelled; user posts pre-moderated). Resolutions X-67–X-71. Requirements R-128–R-139.
- **Vidhi on the shared kernel** (P17 §4Y, Appendix K §K.25, Appendix AA §AA.24): the 17 agents, skills, missions, RRULE schedules, notebooks and `ldc-mcp` map one-to-one onto kernel objects; adapters for OpenAI, Azure OpenAI (Central India), Gemini (asia-south1), Grok, Sarvam, Bhashini and self-hosted models join the registry OFF until their retention terms are verified; `IMAGE_GEN_PORT` for marketing imagery only; notebook outputs aligned; `vidhi.*` keys.
- **Public website and Studio** (P23 §4V–§4W; FR-P23-12 amended): the existing CMS is extended with a public Brand Studio (`brand_pack`, `brand.app_name`, host map, social links), Team and Leadership pages, an Investors page behind a toggle (OFF) with a locked disclaimer, Careers, Press, Partners, Contact (Delhi, Noida, Jaipur), Documentation and Changelog; blog toggle, bulk Word import (LawDocs pattern) and pre-moderated user posts (OFF); vlog with mandatory captions; a Resources library; policy pages from Appendix AD; the feedback widget and idea board; `TAG_MANAGER_PORT` (none) with consent gating; dyslexia font and captions as release gates. The Health Check Studio and the Claims Register are unchanged and are named by the IPB as the ecosystem pattern.
- **Legal policies drafted** — new **Appendix AD** (13,600 words): LDC instances of IPB-05 Templates 1–13 and 15–18 with the parameter block, inserts, counsel checklists and the Investors disclaimer; Template 14 not adopted. Owner decision #11 is narrowed: the public set is drafted and awaits counsel (#28).
- **Settings tree** (P02 §4S; Appendix C §C.3.6A; Appendix U §U.15): the IPB-07 twenty nodes become the binding `apps/web` Settings order; every key carries its IPB tier and a help key; new nodes Accessibility, Appearance, Storage & data, Audit trails, AI & Vidhi, Feedback, Tutorials & help, Security & trust, What's new, About.
- **Ports, API and Ecosystem events** (P18 §4Y; master §19 items 15–26): every port named against IPB-01 with reference and alternate adapters; connector marketplace manifest; `/v1`, RFC 9457, `ldck_` keys, Standard Webhooks; twelve Ecosystem events LDC produces or consumes, to be registered in Spec v1.2; LDC is the `LAW_REGISTER_PORT` provider for all products.
- **Portability** (P19 §4Q): extension allow-list lint, Object Lock equivalents per cloud, Terraform per cloud, yearly exit drill, Settings › Storage & data with locked retention floors.
- **Vendor Assurance Room, engineering governance, environment** (P24 §4M, §13.2B): the IPB-08 cadenced catalogue mirrored under Settings › Security & trust with evidence packs, auditor grants and a framework checklist filed into the tenant's calendar; `cc/<phase>-<slug>` branches with plan files; per-PR preview environments; tenant beta ring; release-notes pipeline with `reg:*` legal approval; patch SLAs; `env/.env.example` (161 annotated variables), `env/SEED_CREDENTIALS.md` (lead-supplied; never in production) and `env/README.md`.
- **New companion documents:** `design/UI_UX_Design_Brief_v1.3.md` (forest green `#0F4C3A`, gold `#C9A227`, IBM Plex; placeholders the owner replaces from Brand Studio); `content/LawDocsComply_Website_Content_v1.0.md` (15,200 words of page copy, one-liners, FAQ bank, SEO titles, image placeholders and Claims Register entries, written to the Claims Register rules); `condensed/v1.3_Session_Prompt_Addendum.md` (first-session IPB instruction and amended prompts for P00, P02, P17, P18, P19, P23, P24); `_review/v1.3_upgrade_review_log.md` (adversarial self-review).
- **Appendices updated in place:** B §B.14 (events and error codes), C (§C.3.6A, console and public shells, tokens), K §K.25, Q §Q.20 (pointer to IPB-02), U §U.15, W §W.7 (fourteen open items, twelve new `[VERIFY]`), X §X.16, AA §AA.24, AC (TM-1070–TM-1081). Templates, Part-2 prompts and the RBI catalogue are untouched.
- **Owner decisions added:** #28 approve Appendix AD for counsel review and supply entity particulars; #29 Investors page publication; #30 user-post programme and tag management; #31 image-generation provider and mandatory review.

### What v1.2 changes (management instruction of 25 October 2026: rework the Excel templates and the related workflow)

The owner's 30-column sheet was a reference only. It could not be read on one screen, printed or exported cleanly, and several data items shared one cell. v1.2 replaces it and rebuilds the workflow around it:

- **Template contract v2.0 (D-49; Appendix E Part A).** 62 base columns in eight colour-coded, collapsible groups, plus 0–4 extension columns per family, so column sets and dropdowns differ by family. The groups are LIST VIEW (yellow), SOURCE & VERSION, APPLICABILITY, COMPLIANCE DETAIL, MAKER, CHECKER, AUDITOR and SYSTEM. New columns include **Name of Master Direction / Regulation**, **Actionable Last Updated On** (per question), change status and previous actionable, department function and sub-function, risk type, linked RiskID/GovID, maker guidance, checker review points and auditor test procedure. Every template has dependent Department → Function → Sub-function dropdowns, frozen panes, filters on every column, RAG colouring, a print area limited to the list view, a `Read Me` sheet and a protected `_Template_Info` sheet with machine keys. The owner's existing v1.0 sheets still import through the legacy map.
- **List view of 9 columns (D-50; P04 §4R).** The yellow group of the sheet is exactly what the tool shows:
  - the columns are S. No., CompID, Compliance Question / Actionable, Clause / Para No., Department, Due Date & Frequency, Date of Compliance, Status and Risk Category;
  - Next Due, Days to Due and RAG appear as chips;
  - clicking a CompID opens a drawer with the explanation, maker, checker, auditor, evidence, conversation and history.
- **CompIDs, RiskIDs and GovIDs (D-51, D-52, NN-56, NN-57; Appendix B §B.12).**
  - The system generates a unique, permanent CompID such as `RBI-NBFC-GOV25-0042` when a master direction's sheet is uploaded; authors leave the cell blank.
  - Risk items carry RiskIDs (`RSK-…`, library `RSKL-…`) and governance items carry GovIDs (`GOV-…`, library `GOVL-…`).
  - The audit trail, conversations, stars and exports are keyed to these IDs.
- **Work the list (P04 §4R).**
  - Star or bookmark any CompID, and filter and sort on every column, including saved views.
  - Group by up to three levels: department, function, sub-function, compliance type, risk type or due month.
  - Export the current view to Excel or PDF with grouping.
  - A deterministic **red / amber / green** engine and an urgency radar surface what is overdue, due soon and at risk of slipping (D-54, NN-58).
- **Conversations and accountability (D-53, NN-59, NN-60).**
  - Each CompID has typed threads with SLAs: a senior can ask for an explanation of a delay, and a maker can ask for guidance.
  - A RACI per item and a ledger-computed accountability report show who held the item, for how long, and what it waited on. Outcomes for people stay with humans.
- **Health Check Studio (D-55; P23 §4U).** The super admin picks sections, the number of questions and the questions themselves by CompID, then versions and publishes the set with maker-checker approval.
- **API-first onboarding (D-56; P01, P18, Appendix L).** Discovery by PAN, CIN/LLPIN, GSTIN, LEI or name through licensed providers and public registers (MCA, GSTN, RBI, SEBI, IRDAI, IFSCA, GLEIF), with consent, provenance and confidence on every pre-filled field, plus a partner onboarding API for Finbyx, Udofin and the Operations Hub.
- **Risk and Governance register templates (D-57)** in the same design, with Part-2 commands `28` (risk library) and `29` (governance library); `00A` explains how to migrate v1.0 sheets.
- **New rules and decisions:** NN-56–NN-60, D-49–D-58, X-61–X-66 and R-112–R-127 (master §4, §6.7, §18; `02` §2.5, §3.6, §3.7). Synthetic sample exports are in `templates/samples/`.

### What v1.1 changes (management instruction of 25 October 2026)

The owner asked to go through all the attached files again, improve the logic and workflows, add details, make the system future-ready with the latest AI developments, make workflows faster and more customisable, fix errors, study other GRC platforms and their client feedback, reverse-engineer existing products, confirm that only the 28 November 2025 consolidated RBI directions will be uploaded, take the product global and study how Lawrbit serves companies abroad, and archive the older versions. v1.1 does that:

- **Every file improved in place** — logic, workflows, click budgets, customisation and details added and errors fixed; changes are marked *(v1.1)* and each file carries a "v1.1 changes" list under its header.
- **Traceability audit (Appendix AC)** — 1,069 rows map every section of the owner's Architecture Parts 1–3, the earlier master prompt and every ask in the brief to the pack: 938 covered, 77 partial, 12 missing (each listed with its target), 42 changed by a recorded decision.
- **Four new phases** — P25 Global Jurisdiction Packs, Multi-Region and Partner Network; P26 Litigation, Legal Matters, Contracts, Licences and Ethics Registers; P27 ESG, BRSR, CSR and Sustainability; P28 Reports, MIS and Board-Pack Studio.
- **Global (Appendix Y)** — Lawrbit's delivery model (central research in India plus local law and accounting partner firms — its public materials cite experts at 100+ law firms) analysed and improved upon: jurisdiction packs with reviewers of record, a partner portal, global entity management, regional data cells (India live; EU, GCC/UAE, Singapore, US on demand), multi-currency pricing, localisation, and the INTL-GEN template.
- **Client feedback and reverse engineering (Appendix Z)** — reviews and help-centre analysis of Indian and global GRC tools; a binding 142-item improvement backlog (IMP-001–IMP-142) applied to the phases: ≤ 12-question applicability with "why it applies", AI import of existing trackers with undo, one control for many obligations, event-driven checkpoints, three dates per instance, notification budgets, inline bulk editing with undo, click budgets for 26 journeys.
- **Future-ready AI (Appendix AA)** — Vidhi becomes an agent workforce of role agents with autonomy levels L0–L4, human sponsors, missions, memory, evaluation gates and kill switches; an LDC MCP server so clients' own AI assistants can work with LawDocsComply safely, an MCP client, A2A with ecosystem agents; and an AI-governance module and template (AI-GOV) for clients facing RBI FREE-AI, MeitY, SEBI, EU AI Act and ISO 42001 expectations.
- **RBI content base (Appendix AB and `catalogue/`)** — the 28 November 2025 consolidated directions (238 per RBI's press release; 244 serials, 240 live), later amendments, the DoS directions of 31 July 2026, CEPD Internal Ombudsman directions and RB-IOS 2026 — 320 rows pre-seeded in the tool; RBI Part-2 commands rewritten around them.
- **New rules and decisions** — NN-47–NN-55, D-34–D-48, X-42–X-60, R-103–R-111 (master §4, §18; `02` §2.4, §3.4, §3.5).

## 2. Files

Word counts are whitespace-separated words, rounded to the nearest 100.

| File | Contents | Words |
|---|---|---|
| `00_README.md` | This guide | — |
| `01_MASTER_PROMPT.md` *(v1.3)* | MASTER BUILD PROMPT | 20,100 |
| `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` *(v1.3)* | REQUIREMENTS MAP AND DECISION LOG | 10,400 |
| `phases/P00_Foundations_Repository_Discovery_and_Migration.md` | Foundations, Repository Discovery and Migration | 16,100 |
| `phases/P01_Identity_Tenancy_Onboarding_and_Access.md` | Identity, Tenancy, Onboarding and Access | 15,500 |
| `phases/P02_Configuration_Studio_Rule_Engine_and_Settings.md` *(v1.3)* | Configuration Studio, Rule Engine and Settings | 15,000 |
| `phases/P03_Regulatory_Content_Library_Template_Registry_and_Excel_Import.md` | Regulatory Content Library, Template Registry and Excel Import | 20,000 |
| `phases/P04_Compliance_Workspace_Maker_Checker_Calendar_Tasks_Notifications.md` | Compliance Workspace: Maker-Checker, Calendar, Tasks and Notifications | 22,400 |
| `phases/P05_Regulatory_Change_Management_and_AI_Question_Authoring.md` | Regulatory Change Management and AI Question Authoring | 13,200 |
| `phases/P06_Governance_Board_Committees_and_Company_Secretarial.md` | Governance, Board, Committees and Company Secretarial | 21,100 |
| `phases/P07_Policy_Lifecycle_and_Document_Management_System.md` | Policy Lifecycle and Document Management System | 12,900 |
| `phases/P08_Enterprise_Risk_Management_and_CRO_Workspace.md` | Enterprise Risk Management and CRO Workspace | 16,900 |
| `phases/P09_Risk_Assessment_Lab_ICAAP_Stress_Testing_Capital_and_Ratios.md` | Risk Assessment Lab: ICAAP, Stress Testing, Capital and Ratios | 13,800 |
| `phases/P10_Audit_Management_Internal_RBIA_IS_Secretarial_Statutory.md` | Audit Management: Internal Audit, RBIA, Concurrent, IS/IT, Secretarial, Statutory-Audit Support and Specialised Audits | 17,700 |
| `phases/P11_Return_Studio_Data_Preparation_and_Accounting_Bridge.md` | Return Studio, Data Preparation and Accounting Bridge | 15,500 |
| `phases/P12_Data_Protection_Cyber_Security_IT_Governance_and_TPRM.md` | Data Protection, Cyber Security, IT Governance and Third-Party Risk (TPRM) | 15,900 |
| `phases/P13_HRMS_People_and_Labour_Compliance_Suite.md` | HRMS, People and Labour Compliance Suite | 10,700 |
| `phases/P14_Grievance_Redressal_and_Customer_Support_Desk.md` | Grievance Redressal and Customer Support Desk | 9,200 |
| `phases/P15_Sector_Packs_and_Entity_Logic.md` | Sector Packs and Entity Logic | 14,800 |
| `phases/P16_Cooperative_Society_Operations_Suite.md` | Co-operative Society Operations Suite | 8,800 |
| `phases/P17_Vidhi_AI_Employee_Agents_and_Knowledge_Notebooks.md` *(v1.3)* | Vidhi AI Employee, Agents and Knowledge Notebooks | 18,000 |
| `phases/P18_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md` *(v1.3)* | Integration Gateway, Ecosystem Connectors and Developer Platform | 19,300 |
| `phases/P19_Data_Preservation_Portability_and_BYO_Storage.md` *(v1.3)* | Data Preservation, Portability and Bring-Your-Own Storage | 11,400 |
| `phases/P20_Pricing_Plans_Subscriptions_Billing_Savings_and_Revenue_Streams.md` | Pricing, Plans, Subscriptions, Billing, Savings and Revenue Streams | 13,800 |
| `phases/P21_Marketplace_Retainers_and_FinLegal_Academy.md` | Marketplace, Retainers and FinLegal Academy | 9,800 |
| `phases/P22_Service_Delivery_Console_and_Operations_Hub_Interface.md` | Service Delivery Console and Operations Hub Interface | 8,700 |
| `phases/P23_Public_Website_Health_Check_Help_Centre_Tutorials_and_Accessibility.md` *(v1.3)* | Public Website, Free Compliance Health Check, Help Centre, Tutorials and Accessibility | 25,700 |
| `phases/P24_Engineering_Governance_Hardening_Certification_Readiness_and_GoLive.md` *(v1.3)* | Engineering Governance, Hardening, Certification Readiness and Go-Live | 11,700 |
| `phases/P25_Global_Jurisdiction_Packs_Multi_Region_and_Partner_Network.md` | Global Jurisdiction Packs, Multi-Region Cells and Partner Network *(new in v1.1)* | 8,300 |
| `phases/P26_Litigation_Legal_Matters_Contracts_Licences_and_Ethics_Registers.md` | Litigation, Legal Matters, Contracts, Licences and Ethics Registers *(new in v1.1)* | 9,800 |
| `phases/P27_ESG_BRSR_CSR_and_Sustainability.md` | ESG, BRSR, CSR and Sustainability *(new in v1.1)* | 8,300 |
| `phases/P28_Reports_MIS_and_Board_Pack_Studio.md` | Reports, MIS and Board-Pack Studio *(new in v1.1)* | 9,400 |
| `appendices/AA_Future_Ready_AI_and_Agentic_Architecture.md` *(v1.3)* | Future-Ready AI and Agentic Architecture *(new in v1.1)* | 11,800 |
| `appendices/AB_RBI_Consolidated_Directions_Content_Plan.md` | RBI Consolidated Directions: Content Plan and Catalogue *(new in v1.1)* | 8,900 |
| `appendices/AC_Baseline_and_Brief_Traceability_Matrix.md` *(v1.3)* | Baseline and Brief Traceability Matrix *(new in v1.1)* | 38,400 |
| `appendices/AD_Legal_Policies_Review_Ready_Drafts.md` | Legal Policies: Review-Ready Drafts for LawDocsComply (IPB-05 instances) *(new in v1.3)* | 13,600 |
| `appendices/A_Workflows_and_State_Machines.md` | Workflows and State Machines (binding) | 10,500 |
| `appendices/B_Data_Model_Events_and_Error_Codes.md` *(v1.3)* | Data Model, Events and Error Codes | 39,800 |
| `appendices/C_Information_Architecture_Screens_Menus_and_Dashboards.md` *(v1.3)* | Information Architecture, Screens, Menus and Dashboards (binding) | 31,700 |
| `appendices/D_Roles_Personas_and_Access_Control_Matrix.md` | Roles, Personas and Access Control Matrix (binding) | 9,300 |
| `appendices/E_Excel_Template_Contract_Entity_Families_and_Importer.md` | Excel Template Contract, Entity Families and Importer | 35,800 |
| `appendices/F_Regulatory_Source_Register_and_Monitoring_Catalogue.md` | Regulatory Source Register and Monitoring Catalogue | 8,400 |
| `appendices/G_Legal_and_Regulatory_Rules_Register.md` | Legal and Regulatory Rules Register | 12,800 |
| `appendices/H_Risk_Taxonomy_Basel_ICAAP_Stress_Scenarios_and_Ratio_Library.md` | Risk Taxonomy, Basel Mapping, ICAAP, Stress Scenarios and Ratio Library | 18,600 |
| `appendices/I_Regulatory_Returns_CIC_and_Tax_Return_Catalogue.md` | Regulatory Returns, Credit-Bureau and Tax Return Catalogue | 8,200 |
| `appendices/J_Accounting_Auditing_and_Secretarial_Standards_Map.md` | Accounting, Auditing and Secretarial Standards Map | 7,100 |
| `appendices/K_Vidhi_AI_Agent_Specification.md` *(v1.3)* | Vidhi AI Agent Specification | 9,600 |
| `appendices/L_Integration_Adapters_and_API_Catalogue.md` | Integration Adapters and API Catalogue | 8,200 |
| `appendices/M_Export_Package_LDC-EXPORT-1.0_and_Folder_Taxonomy.md` | Export Package `LDC-EXPORT-1.0` and Folder Taxonomy | 7,700 |
| `appendices/N_Pricing_Plans_Add-ons_Revenue_Streams_and_Savings_Model.md` | Pricing, Plans, Add-ons, Revenue Streams and Savings Model | 11,300 |
| `appendices/O_Marketplace_Services_Catalogue_and_Professional_Rules.md` | Marketplace Services Catalogue and Professional Rules | 6,400 |
| `appendices/P_Website_Copy_SEO_GEO_Tutorials_and_Video_Plan.md` | Website Copy, Health-Check Question Bank, Glossary Priorities, Tutorial and Video Plan, SEO/GEO System | 15,300 |
| `appendices/Q_Security_Privacy_and_Certification_Readiness.md` *(v1.3)* | Security, Privacy and Certification Readiness | 8,000 |
| `appendices/R_Competitive_Research_and_Differentiation.md` | Competitive Research and Differentiation | 6,600 |
| `appendices/S_Cooperative_Societies_Law_and_Operations.md` | Co-operative Societies: Law and Operations | 6,400 |
| `appendices/T_HRMS_Labour_Codes_Registers_and_Payroll_Parameters.md` | HRMS, Labour Codes, Registers and Payroll Parameters | 7,200 |
| `appendices/U_Configuration_Framework_and_Settings_Catalogue.md` *(v1.3)* | Configuration Framework and Settings Catalogue (binding) | 24,300 |
| `appendices/V_Acceptance_Tests_and_UAT_Catalogue.md` | Acceptance Tests and UAT Catalogue | 11,100 |
| `appendices/W_Verification_Log_and_Open_Items.md` *(v1.3)* | Verification Log and Open Items | 13,900 |
| `appendices/X_Operations_Hub_Addendum_for_LawDocsComply.md` *(v1.3)* | Operations Hub Addendum for LawDocsComply | 4,600 |
| `appendices/Y_Global_Compliance_Expansion_and_Jurisdiction_Packs.md` | Global Compliance Expansion and Jurisdiction Packs *(new in v1.1)* | 10,300 |
| `appendices/Z_Customer_Feedback_Reverse_Engineering_and_Improvement_Backlog.md` | Customer Feedback, Reverse Engineering and Improvement Backlog *(new in v1.1)* | 11,000 |
| `part2_prompts/` (32 files) | Part-2 master command, v1.0→v2.0 migration guide, 27 family commands, Risk and Governance library commands, QA checklist | 85,100 |
| `templates/` (29 workbooks) *(v2.0 in v1.2)* | Excel templates `LDC-TPL-<FAMILY>-v2.0` (27 families + RISK + GOV), validator v2, validation report, build scripts, `samples/` (synthetic list exports), `_legacy_v1.0/` (v1.0 workbooks kept for the legacy importer) | — |
| `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx` *(new in v1.1)* | The RBI content base: 320 directions (28 Nov 2025 consolidated set, later amendments, DoS 31 Jul 2026 set, CEPD, RB-IOS 2026) with family, template, wave and status columns | — |
| `condensed/` | Finbyx-style Master Prompt and Phase Runbook (v1.2), .md and .docx | — |
| `condensed/v1.3_Session_Prompt_Addendum.md` *(new in v1.3)* | First-session IPB instruction, amended session prompts for P00, P02, P17, P18, P19, P23, P24, progress-tracker rows, hand-over additions | 1,200 |
| `design/UI_UX_Design_Brief_v1.3.md` *(new in v1.3)* | UI/UX design brief: palette (IPB-D-11), typography, spacing, components, iconography, imagery placeholders, dark mode, motion, accessibility, do/don't, sample screens, tenant overrides | 3,200 |
| `content/LawDocsComply_Website_Content_v1.0.md` *(new in v1.3)* | Website content deck: copy for every IPB-04 standard page, Health Check funnel, one-liners, FAQ bank (46), SEO titles, footer and cookie texts, image placeholders, Claims Register entries | 15,200 |
| `env/.env.example`, `env/SEED_CREDENTIALS.md`, `env/README.md` *(new in v1.3)* | IPB-11 environment template (161 annotated variables), seed credentials (lead-supplied; gitignored in the repository; production refuses seeds) and usage guide | 3,100 |
| `_review/v1.3_upgrade_review_log.md` *(new in v1.3)* | Adversarial self-review of the v1.3 upgrade: threat walk, state-machine scenario tables, ID collision check, fixes | 2,400 |
| **Total (Markdown, excluding condensed, `_research/`, `_review/`, `design/`, `content/`, `env/`)** | | **953,800** *(v1.3; v1.2: 933,700)* |

Folders also include `_research/` (dated research notes from all streams), `_review/` (review logs for v1.0, v1.1, v1.2 and the v1.3 upgrade review), *(v1.3)* `design/`, `content/` and `env/` and `_Archive (older versions)/` at the top of the LawDocsComply Prompt folder (v1.0 and v1.1). A consolidated Word copy of the whole pack (`LawDocsComply_Build_Prompt_Pack_v1.3.docx`) is included.

**Excel templates (Part 2 and registers)** — `templates/` *(contract v2.0)*:

- `LDC-TPL-AI-GOV-v2.0 - AI Governance.xlsx`
- `LDC-TPL-COOP-CCS-v2.0 - Credit Co-operative Societies.xlsx`
- `LDC-TPL-COOP-GEN-v2.0 - Other Co-operative Societies.xlsx`
- `LDC-TPL-CYBER-v2.0 - Cyber Security.xlsx`
- `LDC-TPL-DATA-PRIV-v2.0 - Data Protection and Privacy.xlsx`
- `LDC-TPL-ESG-BRSR-v2.0 - ESG BRSR and CSR.xlsx`
- `LDC-TPL-GOV-v2.0 - Governance Register.xlsx`
- `LDC-TPL-IFSCA-FCFU-v2.0 - IFSCA Finance Companies and Units.xlsx`
- `LDC-TPL-IFSCA-FME-v2.0 - IFSCA Fund Management Entities.xlsx`
- `LDC-TPL-IFSCA-GEN-v2.0 - IFSCA Regulated Entities.xlsx`
- `LDC-TPL-INTL-GEN-v2.0 - International Jurisdictions.xlsx`
- `LDC-TPL-IRDAI-INS-v2.0 - Insurers.xlsx`
- `LDC-TPL-IRDAI-INT-v2.0 - Insurance Intermediaries.xlsx`
- `LDC-TPL-LAB-POSH-v2.0 - Labour Codes and POSH.xlsx`
- `LDC-TPL-MCA-CO-v2.0 - Companies.xlsx`
- `LDC-TPL-MCA-LLP-v2.0 - LLPs.xlsx`
- `LDC-TPL-RBI-ARC-v2.0 - Asset Reconstruction Companies.xlsx`
- `LDC-TPL-RBI-NBFC-v2.0 - NBFCs.xlsx`
- `LDC-TPL-RBI-OTH-v2.0 - Other RBI Regulated Entities.xlsx`
- `LDC-TPL-RBI-RCB-v2.0 - Rural Co-operative Banks.xlsx`
- `LDC-TPL-RBI-SCB-v2.0 - Commercial Banks SFBs PBs LABs RRBs.xlsx`
- `LDC-TPL-RBI-UCB-v2.0 - Urban Co-operative Banks.xlsx`
- `LDC-TPL-RISK-v2.0 - Risk Register.xlsx`
- `LDC-TPL-SEBI-AIF-v2.0 - Alternative Investment Funds.xlsx`
- `LDC-TPL-SEBI-INT-v2.0 - SEBI Intermediaries.xlsx`
- `LDC-TPL-SEBI-LISTED-v2.0 - Listed Entities.xlsx`
- `LDC-TPL-SEBI-MF-v2.0 - Mutual Funds.xlsx`
- `LDC-TPL-SEBI-REIT-INVIT-v2.0 - REITs and InvITs.xlsx`
- `LDC-TPL-TAX-GST-v2.0 - GST and Direct Tax.xlsx`

Each workbook has four sheets:

- `Compliance Register`, or `Risk Register` / `Governance Register`: row 1 holds the coloured group bands, row 2 the headers, and data starts at row 3.
- `Lists`: the family vocabularies and named ranges.
- `Read Me`: how to use the sheet, the colour legend, and how to expand the groups.
- `_Template_Info` (protected): the template code, the column contract with machine keys, and the header hash.

Only the yellow list view is open when a template is first opened; click the `+` buttons above the column letters to open the other groups. Leave **CompID** blank, because the platform assigns it on upload. Validate after any change with `python3 templates/_validate_templates_v2.py templates` (latest report `templates/_validation_report_v2.md`: 29/29 PASS). The v1.0 workbooks in `templates/_legacy_v1.0/` remain for the legacy import path. Their regression check needs **both** owner samples: `python3 templates/_legacy_v1.0/_validate_templates.py templates/_legacy_v1.0 "<Finance Company sample>.xlsx" "<Appointed Actuary sample>.xlsx"`.

## 3. How to run the build (Part 1)

1. Create or open the LawDocsComply repository and open Claude Code in it.
2. **Session 1 (P00):** commit `01_MASTER_PROMPT.md` as `docs/00-master-prompt.md`, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` as `docs/01-decision-log.md`, `phases/` and `appendices/` under `docs/`, *(v1.3)* the IPB pack unchanged as `docs/ipb/`, `design/` and `content/` under `docs/`, `env/.env.example` and `env/README.md` at `env/` (never `SEED_CREDENTIALS.md`), and the Ecosystem Integration Specification v1.2 unchanged as `docs/ecosystem/infrabyx-integration-spec.md`. *(v1.3)* Type first: *"Read docs/ipb/00_README.md, then IPB-01, IPB-02, IPB-09 and IPB-11 in full before writing the Phase 0 plan."* Then type: *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P00_Foundations_Repository_Discovery_and_Migration.md in full, plus the appendices it names. Write docs/phases/P00-plan.md and stop for my approval."*
3. **Every later session:** use the session prompt for that phase in `condensed/LawDocsComply_Phase_Runbook_v1.2.md`, preceded by the first line of `condensed/v1.3_Session_Prompt_Addendum.md` §A and, for P00, P02, P17, P18, P19, P23 and P24, the amended prompt in that addendum *(v1.3)*. Approve each plan before code is written. Each phase stops at its exit gate (§13 of the phase file, plus master §15 Definition of Done).
4. **Order and waves (master §13):**
   - **Wave 1 — Compliance Core GA (about S1–S30):** P00 → P01 → P02 → P03 → P04 → P05; in parallel P28 core, P15 (RBI-NBFC, MCA-CO, DATA-PRIV, IFSCA-GEN first), P17 runtime, P18 core, P19 core, P06, P07, P20, P23; then P24.
   - **Wave 2 — Risk, Audit, Returns, Data, Legal:** P08, P09, P10, P11, P12 (incl. AI governance), P14, P26, P28 studio, the rest of P15, P17, P18, P19; then P24.
   - **Wave 3 — People, Co-operatives, Services, ESG:** P13, P16, P21, P22, P27 and the full agent workforce; then P24.
   - **Wave 4 — Global:** P25 (regional cells, global entity management, partner portal, first corridor packs — UAE and Singapore recommended); then P24 per cell.
5. **Precedence on conflict** *(v1.3; X-67)*: master → **IPB v1.0** → **Ecosystem Spec v1.2** → `02` → Appendix G → E → B → A → D → U → C → phase file → other appendices (master §18). LDC may only be stricter than the IPB; any other difference is an `IPB-DEV-nn` entry in `02` §2.6.
6. **Unverified facts:** about 1,490 `[VERIFY]` markers remain by design. Any feature depending on one ships behind a flag that is OFF (or advisory-only, NN-38) until the fact is checked against the primary source (Appendix W).

**Indicative effort:** about 255 squad-sprints in total (phase table in master §13, excluding P24 re-runs) *(v1.2: +7 for the business-ID registry, API onboarding, CompID generation, the list view, RAG, conversations, accountability and the Health Check Studio)*; with nine squads in parallel, Wave 1 GA in about 30 two-week sprints (roughly 14 months), Waves 2–3 by about sprint 48 and the first global corridor by about sprint 54; with fewer squads expect 75–90 sprints.

**Condensed edition (Finbyx style):** `condensed/LawDocsComply_Master_Prompt_ClaudeCode_v1.2` (master + decisions + objective and scope of every phase + appendix index) and `condensed/LawDocsComply_Phase_Runbook_v1.2` (session prompts, objectives, exit gates, integration notes) — the same content as the pack in two documents. *(v1.3)* The condensed files keep their v1.2 names; `condensed/v1.3_Session_Prompt_Addendum.md` carries the v1.3 session prompts and prevails where it differs. **Consolidated edition:** `LawDocsComply_Build_Prompt_Pack_v1.3.docx` (the lead regenerates it from the v1.3 Markdown; the v1.2 file at the pack root is superseded).

## 4. How to produce the question sheets (Part 2)

1. For RBI families, open `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx`, filter the wave and family, and take the next direction (Appendix AB gives the order; NBFC first). Then open a new Claude chat (Cowork). Attach: the family template from `templates/` (v2.0), the regulator's source PDF(s) for one instrument, `part2_prompts/00_Part2_Master_Command.md`, the family command (`part2_prompts/NN_<FAMILY>_Command.md`) and `part2_prompts/99_QA_Checklist_for_Question_Sheets.md`.
2. Ask for **one** sheet first, filling the yellow list view and the other groups as the commands direct, and leaving CompID blank; check it; then proceed instrument by instrument (the owner's established method).
3. Check each finished sheet against the template (or, once P03 is live, upload it to the importer, which shows a preview, row errors and a diff before anything is published).
4. Clear every `[VERIFY]` before upload — the importer blocks publication of rows that still carry one.
5. Once P05 ships, the same method runs inside the product: upload a new master direction, and the AI Question Authoring Studio drafts the sheet with the family template, for review, export, correction, re-upload and approval (R-085). Client admins can do the same for their own tenant only.

## 5. Decisions needed from the owner (`02` §4)

| # | Decision | Blocks |
|---|---|---|
| 1 | Confirm the Microsoft 365 plan actually held ("Business Starter" is a Google Workspace edition, not a Microsoft plan) | P18, P22 |
| 2 | Accept trials as real tenants (D-26) and obtain the Operations Hub's acceptance | P20 |
| 3 | Selling entity or entities and merchant of record (D-27) | P20, P21 |
| 4 | Second pricing approver (D-28) | Pricing Studio |
| 5 | Package names and prices, add-on prices, trial length, discounts (Appendix N seeds) | P20, P23 |
| 6 | Names: Vidhi vs Nidhi AI; FinLegal Academy vs LawDocs Trainings; Essentials/Professional/Enterprise vs Basic/Pro/Custom | P17, P21, P23 |
| 7 | Optional `_LDC_System` sheet in LDC Excel exports (X-28) | P03, P04 |
| 8 | Revenue-stream waves and kill-switch approvers; advertising/sponsored listings ON or OFF | P20, P21 |
| 9 | Hindi second locale (D-30) and AI-crawler policy (D-31) | P23 |
| 10 | LDC operating company particulars (CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer) | P20, P23, P24 |
| 11 | Certification-readiness policy set (information security, access, incident, vendor, retention, privacy, cookie, AI use, BCP) | P24 |
| 12 | Vendor contracts (AWS/Bedrock, eSign ASPs, company-data, PAN/GSTIN, DigiLocker partner, SMS/WhatsApp/JioCX, translation/speech, VAPT auditor) | P01, P07, P17, P18, P24 |
| 13 | Content and reviewer roster (CS, CA, advocate) for packs and Part-2 sheets; in-country reviewers before any international pack | P03, P05, P15 |
| 14 | Remove the live site's "ISO 27001 certified" claim now, and retire Railway hosting after migration | P00, P23 |
| 15 | *(v1.1)* Approve the RBI content base and catalogue (D-39) and the Part-2 wave plan (Appendix AB) | P03, Part 2 |
| 16 | *(v1.1)* Default AI autonomy ceilings per plan and human sponsors for agents at L2+ | P17 |
| 17 | *(v1.1)* First regional cell and corridor after India (UAE then Singapore recommended) and first content partners | P25 |
| 18 | *(v1.1)* Keep ESG-BRSR as a separate Part-2 family (built) or merge it into SEBI-LISTED/MCA-CO | P27 |
| 19 | *(v1.1)* Delete the archived v1.0 and v1.1 files or keep them in `_Archive (older versions)` (deletion needs your approval on the computer) | — |
| 20 | *(v1.2)* Confirm D-58: for never-amended instruments the amended date repeats the issue date | P03, Part 2 |
| 21 | *(v1.2)* Default RAG windows, including "Immediately" and event-based items | P04 |
| 22 | *(v1.2)* Default export columns and PDF branding | P04 |
| 23 | *(v1.2)* First health-check sets (families, sections, counts, CompIDs) | P23 |
| 24 | *(v1.2)* Onboarding data-provider contracts and waterfall order | P01, P18 |
| 25 | *(v1.2)* Instrument short codes for the RBI directions (part of every CompID) and treatment of legacy CompIDs | P03, P00 |
| 26 | *(v1.2)* Use of accountability reports in HR processes (tenant policy, counsel) | P04 |
| 27 | *(v1.2)* Authority code for Secretarial Standards in GovIDs (`ICSI` proposed) | P06 |
| 28 | *(v1.3)* Approve Appendix AD (the drafted public legal policy set) for counsel review and supply the entity particulars that fill it (merges #10 and the public part of #11) | P23, P24, gateway onboarding |
| 29 | *(v1.3)* Investors page: publish or keep `web.investors.enabled = OFF`; gated documents; disclaimer wording [COUNSEL] | P23 |
| 30 | *(v1.3)* User-post programme (author groups, moderation roster, Rule 36 screening) and tag management (none / GTM web / server-side) | P23 |
| 31 | *(v1.3)* Image-generation provider for marketing imagery and confirmation that human review before publication is mandatory | P17, P23 |

**Counsel questions** are listed in `02` §5 (CICRA, BCI/ICAI/ICSI marketplace rules, LODR Reg 24A, RBI outsourcing of compliance/IA, DPDP roles and cross-border routing, trials as production tenants, savings-claim wording, eSign exclusions, co-operative e-meetings, health-check data terms).

**Ecosystem change requests and companion addenda** (Ecosystem Spec v1.2, Finbyx and Operations Hub) are listed in master §19 and Appendix X.

## 6. Requirement coverage

All 139 requirements (102 from the original brief, R-103–R-111 from the v1.1 instruction, R-112–R-127 from the v1.2 instruction and *(v1.3)* R-128–R-139 from the IPB adoption) are mapped to phases and appendices in `02` §8. *(v1.3)* IPB coverage: every item of the pack lead's brief §2 (23 items) is traced in Appendix AC rows TM-1070–TM-1081; deviations are two (`IPB-DEV-01`, `IPB-DEV-02`). Requirements the pack narrowed or replaced after challenge are marked there with the decision that governs them.

## 7. Immediate actions independent of the build

- *(v1.3)* Send Appendix AD to counsel with the entity particulars (owner decision #28); create and monitor the mailboxes it names (support@, privacy@, grievance@, security@, accessibility@, press@).
- *(v1.3)* Decide the Investors page (#29), the user-post programme and tag management (#30) and the image-generation position (#31); all default OFF.
- *(v1.3)* Replace the content deck's placeholders (team, leadership, offices, milestones) in Brand Studio before the public site goes live; photos only with recorded consent.

- Remove "ISO 27001 certified" and any other unevidenced claim from lawdocscomply.com (X-22).
- Make the public site server-rendered so that search engines and AI crawlers can read it; keep or 301-redirect the 15 existing sitemap URLs (X-21).
- Fix the brand colours that fail contrast before new marketing material is produced (X-20).
- Start Part-2 sheets on the v2.0 templates (convert any sheet already written with `part2_prompts/00A`) for the Wave-1 families from the catalogue: RBI-NBFC (the 35 consolidated directions of 28 Nov 2025 and the 31 Jul 2026 DoS set first), MCA-CO, DATA-PRIV and IFSCA-GEN.
