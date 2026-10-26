# LawDocsComply — Build Prompt Pack v1.2

**Prepared:** 25 October 2026 · **v1.2:** 25 October 2026 (Excel template and workflow rework; supersedes v1.1 and v1.0, which are kept in `_Archive (older versions)`) · **Owner:** Company Secretary, Infrabyx Group · **Product:** LawDocsComply (lawdocscomply.com), the Infrabyx group's governance, risk and compliance (GRC) SaaS for RBI, SEBI, IFSCA and IRDAI regulated entities, companies, LLPs and co-operative societies, with data-protection, cyber, labour, tax, ESG and AI-governance overlays — India first, built to take global compliance later · **Companions:** Infrabyx Ecosystem Integration Specification v1.1, Finbyx v1.5, Udofin v1.2, Infrabyx Operations Hub v1.0, Equator Resolution v3.1
**Stack (locked, D-01/X-05):** Next.js 16 (`apps/web`, `apps/public`, `apps/console`, `apps/delivery`) · NestJS 11 modular monolith · PostgreSQL with RLS in regional cells (India: AWS Mumbai, DR Hyderabad) · Temporal · Redis · OpenSearch · S3 Object Lock · Keycloak · Cerbos · GoRules ZEN + CEL · Claude via Amazon Bedrock India · MCP server and client

---

## 1. What this pack is

A paste-ready, phase-by-phase build prompt for a coding agent (Claude Code or equivalent) to build LawDocsComply end to end — **Part 1** of the owner's two-part plan — plus the tools for **Part 2**: 29 Excel templates under template contract v2.0 (27 question families plus the Risk and Governance registers), the question-writing commands, and the RBI Directions Catalogue that sets the order in which the 28 November 2025 consolidated directions are turned into question sheets.

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
| `01_MASTER_PROMPT.md` | MASTER BUILD PROMPT | 16,700 |
| `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` | REQUIREMENTS MAP AND DECISION LOG | 8,100 |
| `phases/P00_Foundations_Repository_Discovery_and_Migration.md` | Foundations, Repository Discovery and Migration | 16,100 |
| `phases/P01_Identity_Tenancy_Onboarding_and_Access.md` | Identity, Tenancy, Onboarding and Access | 15,500 |
| `phases/P02_Configuration_Studio_Rule_Engine_and_Settings.md` | Configuration Studio, Rule Engine and Settings | 13,500 |
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
| `phases/P17_Vidhi_AI_Employee_Agents_and_Knowledge_Notebooks.md` | Vidhi AI Employee, Agents and Knowledge Notebooks | 16,200 |
| `phases/P18_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md` | Integration Gateway, Ecosystem Connectors and Developer Platform | 17,600 |
| `phases/P19_Data_Preservation_Portability_and_BYO_Storage.md` | Data Preservation, Portability and Bring-Your-Own Storage | 10,600 |
| `phases/P20_Pricing_Plans_Subscriptions_Billing_Savings_and_Revenue_Streams.md` | Pricing, Plans, Subscriptions, Billing, Savings and Revenue Streams | 13,800 |
| `phases/P21_Marketplace_Retainers_and_FinLegal_Academy.md` | Marketplace, Retainers and FinLegal Academy | 9,800 |
| `phases/P22_Service_Delivery_Console_and_Operations_Hub_Interface.md` | Service Delivery Console and Operations Hub Interface | 8,700 |
| `phases/P23_Public_Website_Health_Check_Help_Centre_Tutorials_and_Accessibility.md` | Public Website, Free Compliance Health Check, Help Centre, Tutorials and Accessibility | 20,100 |
| `phases/P24_Engineering_Governance_Hardening_Certification_Readiness_and_GoLive.md` | Engineering Governance, Hardening, Certification Readiness and Go-Live | 9,600 |
| `phases/P25_Global_Jurisdiction_Packs_Multi_Region_and_Partner_Network.md` | Global Jurisdiction Packs, Multi-Region Cells and Partner Network *(new in v1.1)* | 8,300 |
| `phases/P26_Litigation_Legal_Matters_Contracts_Licences_and_Ethics_Registers.md` | Litigation, Legal Matters, Contracts, Licences and Ethics Registers *(new in v1.1)* | 9,800 |
| `phases/P27_ESG_BRSR_CSR_and_Sustainability.md` | ESG, BRSR, CSR and Sustainability *(new in v1.1)* | 8,300 |
| `phases/P28_Reports_MIS_and_Board_Pack_Studio.md` | Reports, MIS and Board-Pack Studio *(new in v1.1)* | 9,400 |
| `appendices/AA_Future_Ready_AI_and_Agentic_Architecture.md` | Future-Ready AI and Agentic Architecture *(new in v1.1)* | 11,500 |
| `appendices/AB_RBI_Consolidated_Directions_Content_Plan.md` | RBI Consolidated Directions: Content Plan and Catalogue *(new in v1.1)* | 8,900 |
| `appendices/AC_Baseline_and_Brief_Traceability_Matrix.md` | Baseline and Brief Traceability Matrix *(new in v1.1)* | 37,800 |
| `appendices/A_Workflows_and_State_Machines.md` | Workflows and State Machines (binding) | 10,500 |
| `appendices/B_Data_Model_Events_and_Error_Codes.md` | Data Model, Events and Error Codes | 34,500 |
| `appendices/C_Information_Architecture_Screens_Menus_and_Dashboards.md` | Information Architecture, Screens, Menus and Dashboards (binding) | 28,900 |
| `appendices/D_Roles_Personas_and_Access_Control_Matrix.md` | Roles, Personas and Access Control Matrix (binding) | 9,300 |
| `appendices/E_Excel_Template_Contract_Entity_Families_and_Importer.md` | Excel Template Contract, Entity Families and Importer | 35,800 |
| `appendices/F_Regulatory_Source_Register_and_Monitoring_Catalogue.md` | Regulatory Source Register and Monitoring Catalogue | 8,400 |
| `appendices/G_Legal_and_Regulatory_Rules_Register.md` | Legal and Regulatory Rules Register | 12,800 |
| `appendices/H_Risk_Taxonomy_Basel_ICAAP_Stress_Scenarios_and_Ratio_Library.md` | Risk Taxonomy, Basel Mapping, ICAAP, Stress Scenarios and Ratio Library | 18,600 |
| `appendices/I_Regulatory_Returns_CIC_and_Tax_Return_Catalogue.md` | Regulatory Returns, Credit-Bureau and Tax Return Catalogue | 8,200 |
| `appendices/J_Accounting_Auditing_and_Secretarial_Standards_Map.md` | Accounting, Auditing and Secretarial Standards Map | 7,100 |
| `appendices/K_Vidhi_AI_Agent_Specification.md` | Vidhi AI Agent Specification | 9,100 |
| `appendices/L_Integration_Adapters_and_API_Catalogue.md` | Integration Adapters and API Catalogue | 8,200 |
| `appendices/M_Export_Package_LDC-EXPORT-1.0_and_Folder_Taxonomy.md` | Export Package `LDC-EXPORT-1.0` and Folder Taxonomy | 7,700 |
| `appendices/N_Pricing_Plans_Add-ons_Revenue_Streams_and_Savings_Model.md` | Pricing, Plans, Add-ons, Revenue Streams and Savings Model | 11,300 |
| `appendices/O_Marketplace_Services_Catalogue_and_Professional_Rules.md` | Marketplace Services Catalogue and Professional Rules | 6,400 |
| `appendices/P_Website_Copy_SEO_GEO_Tutorials_and_Video_Plan.md` | Website Copy, Health-Check Question Bank, Glossary Priorities, Tutorial and Video Plan, SEO/GEO System | 15,300 |
| `appendices/Q_Security_Privacy_and_Certification_Readiness.md` | Security, Privacy and Certification Readiness | 7,700 |
| `appendices/R_Competitive_Research_and_Differentiation.md` | Competitive Research and Differentiation | 6,600 |
| `appendices/S_Cooperative_Societies_Law_and_Operations.md` | Co-operative Societies: Law and Operations | 6,400 |
| `appendices/T_HRMS_Labour_Codes_Registers_and_Payroll_Parameters.md` | HRMS, Labour Codes, Registers and Payroll Parameters | 7,200 |
| `appendices/U_Configuration_Framework_and_Settings_Catalogue.md` | Configuration Framework and Settings Catalogue (binding) | 20,000 |
| `appendices/V_Acceptance_Tests_and_UAT_Catalogue.md` | Acceptance Tests and UAT Catalogue | 11,100 |
| `appendices/W_Verification_Log_and_Open_Items.md` | Verification Log and Open Items | 11,500 |
| `appendices/X_Operations_Hub_Addendum_for_LawDocsComply.md` | Operations Hub Addendum for LawDocsComply | 4,300 |
| `appendices/Y_Global_Compliance_Expansion_and_Jurisdiction_Packs.md` | Global Compliance Expansion and Jurisdiction Packs *(new in v1.1)* | 10,300 |
| `appendices/Z_Customer_Feedback_Reverse_Engineering_and_Improvement_Backlog.md` | Customer Feedback, Reverse Engineering and Improvement Backlog *(new in v1.1)* | 11,000 |
| `part2_prompts/` (32 files) | Part-2 master command, v1.0→v2.0 migration guide, 27 family commands, Risk and Governance library commands, QA checklist | 85,100 |
| `templates/` (29 workbooks) *(v2.0 in v1.2)* | Excel templates `LDC-TPL-<FAMILY>-v2.0` (27 families + RISK + GOV), validator v2, validation report, build scripts, `samples/` (synthetic list exports), `_legacy_v1.0/` (v1.0 workbooks kept for the legacy importer) | — |
| `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx` *(new in v1.1)* | The RBI content base: 320 directions (28 Nov 2025 consolidated set, later amendments, DoS 31 Jul 2026 set, CEPD, RB-IOS 2026) with family, template, wave and status columns | — |
| `condensed/` | Finbyx-style Master Prompt and Phase Runbook (v1.2), .md and .docx | — |
| **Total (Markdown, excluding condensed)** | | **933,700** |

Folders also include `_research/` (dated research notes from all streams), `_review/` (review logs for v1.0, v1.1 and v1.2) and `_Archive (older versions)/` at the top of the LawDocsComply Prompt folder (v1.0 and v1.1). A consolidated Word copy of the whole pack (`LawDocsComply_Build_Prompt_Pack_v1.2.docx`) is included.

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
2. **Session 1 (P00):** commit `01_MASTER_PROMPT.md` as `docs/00-master-prompt.md`, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` as `docs/01-decision-log.md`, `phases/` and `appendices/` under `docs/`, and the Ecosystem Integration Specification v1.1 unchanged as `docs/ecosystem/infrabyx-integration-spec.md`. Then type: *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P00_Foundations_Repository_Discovery_and_Migration.md in full, plus the appendices it names. Write docs/phases/P00-plan.md and stop for my approval."*
3. **Every later session:** use the session prompt for that phase in `condensed/LawDocsComply_Phase_Runbook_v1.2.md`. Approve each plan before code is written. Each phase stops at its exit gate (§13 of the phase file, plus master §15 Definition of Done).
4. **Order and waves (master §13):**
   - **Wave 1 — Compliance Core GA (about S1–S30):** P00 → P01 → P02 → P03 → P04 → P05; in parallel P28 core, P15 (RBI-NBFC, MCA-CO, DATA-PRIV, IFSCA-GEN first), P17 runtime, P18 core, P19 core, P06, P07, P20, P23; then P24.
   - **Wave 2 — Risk, Audit, Returns, Data, Legal:** P08, P09, P10, P11, P12 (incl. AI governance), P14, P26, P28 studio, the rest of P15, P17, P18, P19; then P24.
   - **Wave 3 — People, Co-operatives, Services, ESG:** P13, P16, P21, P22, P27 and the full agent workforce; then P24.
   - **Wave 4 — Global:** P25 (regional cells, global entity management, partner portal, first corridor packs — UAE and Singapore recommended); then P24 per cell.
5. **Precedence on conflict:** master §18 (master → `02` → Appendix G → E → B → A → D → U → C → phase file → other appendices; the Ecosystem Spec prevails for cross-product contracts).
6. **Unverified facts:** about 1,490 `[VERIFY]` markers remain by design. Any feature depending on one ships behind a flag that is OFF (or advisory-only, NN-38) until the fact is checked against the primary source (Appendix W).

**Indicative effort:** about 255 squad-sprints in total (phase table in master §13, excluding P24 re-runs) *(v1.2: +7 for the business-ID registry, API onboarding, CompID generation, the list view, RAG, conversations, accountability and the Health Check Studio)*; with nine squads in parallel, Wave 1 GA in about 30 two-week sprints (roughly 14 months), Waves 2–3 by about sprint 48 and the first global corridor by about sprint 54; with fewer squads expect 75–90 sprints.

**Condensed edition (Finbyx style):** `condensed/LawDocsComply_Master_Prompt_ClaudeCode_v1.2` (master + decisions + objective and scope of every phase + appendix index) and `condensed/LawDocsComply_Phase_Runbook_v1.2` (session prompts, objectives, exit gates, integration notes) — the same content as the pack in two documents.

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

**Counsel questions** are listed in `02` §5 (CICRA, BCI/ICAI/ICSI marketplace rules, LODR Reg 24A, RBI outsourcing of compliance/IA, DPDP roles and cross-border routing, trials as production tenants, savings-claim wording, eSign exclusions, co-operative e-meetings, health-check data terms).

**Ecosystem change requests and companion addenda** (Ecosystem Spec v1.2, Finbyx and Operations Hub) are listed in master §19 and Appendix X.

## 6. Requirement coverage

All 127 requirements (102 from the original brief, R-103–R-111 from the v1.1 instruction and R-112–R-127 from the v1.2 instruction) are mapped to phases and appendices in `02` §8. Requirements the pack narrowed or replaced after challenge are marked there with the decision that governs them.

## 7. Immediate actions independent of the build

- Remove "ISO 27001 certified" and any other unevidenced claim from lawdocscomply.com (X-22).
- Make the public site server-rendered so that search engines and AI crawlers can read it; keep or 301-redirect the 15 existing sitemap URLs (X-21).
- Fix the brand colours that fail contrast before new marketing material is produced (X-20).
- Start Part-2 sheets on the v2.0 templates (convert any sheet already written with `part2_prompts/00A`) for the Wave-1 families from the catalogue: RBI-NBFC (the 35 consolidated directions of 28 Nov 2025 and the 31 Jul 2026 DoS set first), MCA-CO, DATA-PRIV and IFSCA-GEN.
