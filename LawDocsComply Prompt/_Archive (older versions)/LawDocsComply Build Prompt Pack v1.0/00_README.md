# LawDocsComply — Build Prompt Pack v1.0

**Prepared:** 25 October 2026 · **Owner:** Company Secretary, Infrabyx Group · **Product:** LawDocsComply (lawdocscomply.com), the Infrabyx group's governance, risk and compliance (GRC) SaaS for RBI, SEBI, IFSCA and IRDAI regulated entities, companies, LLPs and co-operative societies, with data-protection, cyber, labour and tax overlays · **Companions:** Infrabyx Ecosystem Integration Specification v1.1, Finbyx v1.5, Udofin v1.2, Infrabyx Operations Hub v1.0, Equator Resolution v3.1
**Stack (locked, D-01/X-05):** Next.js 16 (`apps/web`, `apps/public`, `apps/console`, `apps/delivery`) · NestJS 11 modular monolith · PostgreSQL with RLS on AWS Mumbai (DR Hyderabad) · Temporal · Redis · OpenSearch · S3 Object Lock · Keycloak · Cerbos · GoRules ZEN + CEL · Claude via Amazon Bedrock India

---

## 1. What this pack is

A paste-ready, phase-by-phase build prompt for a coding agent (Claude Code or equivalent) to build LawDocsComply end to end — **Part 1** of the owner's two-part plan. It also ships the tools for **Part 2**: 24 Excel question templates (one per entity family, in the owner's 30-column format) and the improved commands for producing question sheets in separate Claude chats.

It brings together the owner's brief of 25 October 2026 (102 numbered requirements), the owner's LawDocs Comply Architecture Parts 1–3, the earlier LawDocsComply master prompt, the Excel samples and the 43 finished IFSCA question sheets, the companion ecosystem prompts, and research current to 25 October 2026 by twelve research streams, followed by six review passes.

**What the brief changed after challenge** (`02` §3): super-admin audit edits became Correction Entries; the shared password page became a client-owned vault; no credit-bureau pulls at onboarding; no percentage fee-sharing with regulated professionals by default; RBI filing is prepared and validated, never auto-submitted; operations use the group Operations Hub plus an LDC delivery console; the "28 Nov 2025 supervisory returns" reference is corrected to the RBI DoS directions of 31 Jul 2026; Jio is integrated as channels and voice, not as an LLM, until an enterprise API exists.

## 2. Files

Word counts are whitespace-separated words (as `wc -w`), rounded to the nearest 100, computed on 25 October 2026.

| File | Contents | Words |
|---|---|---|
| `00_README.md` | This guide | — |
| `01_MASTER_PROMPT.md` | MASTER BUILD PROMPT (v1.0, 25 October 2026) | 12,200 |
| `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` | REQUIREMENTS MAP AND DECISION LOG (v1.0, 25 October 2026) | 5,200 |
| `phases/P00_Foundations_Repository_Discovery_and_Migration.md` | Foundations, Repository Discovery and Migration | 12,200 |
| `phases/P01_Identity_Tenancy_Onboarding_and_Access.md` | Identity, Tenancy, Onboarding and Access | 9,500 |
| `phases/P02_Configuration_Studio_Rule_Engine_and_Settings.md` | Configuration Studio, Rule Engine and Settings | 11,500 |
| `phases/P03_Regulatory_Content_Library_Template_Registry_and_Excel_Import.md` | Regulatory Content Library, Template Registry and Excel Import | 10,300 |
| `phases/P04_Compliance_Workspace_Maker_Checker_Calendar_Tasks_Notifications.md` | Compliance Workspace: Maker-Checker, Calendar, Tasks and Notifications | 8,500 |
| `phases/P05_Regulatory_Change_Management_and_AI_Question_Authoring.md` | Regulatory Change Management and AI Question Authoring | 7,900 |
| `phases/P06_Governance_Board_Committees_and_Company_Secretarial.md` | Governance, Board, Committees and Company Secretarial | 14,800 |
| `phases/P07_Policy_Lifecycle_and_Document_Management_System.md` | Policy Lifecycle and Document Management System | 10,500 |
| `phases/P08_Enterprise_Risk_Management_and_CRO_Workspace.md` | Enterprise Risk Management and CRO Workspace | 11,400 |
| `phases/P09_Risk_Assessment_Lab_ICAAP_Stress_Testing_Capital_and_Ratios.md` | Risk Assessment Lab: ICAAP, Stress Testing, Capital and Ratios | 11,100 |
| `phases/P10_Audit_Management_Internal_RBIA_IS_Secretarial_Statutory.md` | Audit Management: Internal Audit, RBIA, Concurrent, IS/IT, Secretarial, Statutory-Audit Support and Specialised Audits | 14,900 |
| `phases/P11_Return_Studio_Data_Preparation_and_Accounting_Bridge.md` | Return Studio, Data Preparation and Accounting Bridge | 13,100 |
| `phases/P12_Data_Protection_Cyber_Security_IT_Governance_and_TPRM.md` | Data Protection, Cyber Security, IT Governance and Third-Party Risk (TPRM) | 10,300 |
| `phases/P13_HRMS_People_and_Labour_Compliance_Suite.md` | HRMS, People and Labour Compliance Suite | 8,900 |
| `phases/P14_Grievance_Redressal_and_Customer_Support_Desk.md` | Grievance Redressal and Customer Support Desk | 7,700 |
| `phases/P15_Sector_Packs_and_Entity_Logic.md` | Sector Packs and Entity Logic | 11,600 |
| `phases/P16_Cooperative_Society_Operations_Suite.md` | Co-operative Society Operations Suite | 7,400 |
| `phases/P17_Vidhi_AI_Employee_Agents_and_Knowledge_Notebooks.md` | Vidhi AI Employee, Agents and Knowledge Notebooks | 12,600 |
| `phases/P18_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md` | Integration Gateway, Ecosystem Connectors and Developer Platform | 10,900 |
| `phases/P19_Data_Preservation_Portability_and_BYO_Storage.md` | Data Preservation, Portability and Bring-Your-Own Storage | 9,000 |
| `phases/P20_Pricing_Plans_Subscriptions_Billing_Savings_and_Revenue_Streams.md` | Pricing, Plans, Subscriptions, Billing, Savings and Revenue Streams | 11,600 |
| `phases/P21_Marketplace_Retainers_and_FinLegal_Academy.md` | Marketplace, Retainers and FinLegal Academy | 8,400 |
| `phases/P22_Service_Delivery_Console_and_Operations_Hub_Interface.md` | Service Delivery Console and Operations Hub Interface | 7,200 |
| `phases/P23_Public_Website_Health_Check_Help_Centre_Tutorials_and_Accessibility.md` | Public Website, Free Compliance Health Check, Help Centre, Tutorials and Accessibility | 15,900 |
| `phases/P24_Engineering_Governance_Hardening_Certification_Readiness_and_GoLive.md` | Engineering Governance, Hardening, Certification Readiness and Go-Live | 7,900 |
| `appendices/A_Workflows_and_State_Machines.md` | Workflows and State Machines (binding) | 6,300 |
| `appendices/B_Data_Model_Events_and_Error_Codes.md` | Data Model, Events and Error Codes | 22,900 |
| `appendices/C_Information_Architecture_Screens_Menus_and_Dashboards.md` | Information Architecture, Screens, Menus and Dashboards (binding) | 18,900 |
| `appendices/D_Roles_Personas_and_Access_Control_Matrix.md` | Roles, Personas and Access Control Matrix (binding) | 5,700 |
| `appendices/E_Excel_Template_Contract_Entity_Families_and_Importer.md` | Excel Template Contract, Entity Families and Importer | 15,500 |
| `appendices/F_Regulatory_Source_Register_and_Monitoring_Catalogue.md` | Regulatory Source Register and Monitoring Catalogue | 5,300 |
| `appendices/G_Legal_and_Regulatory_Rules_Register.md` | Legal and Regulatory Rules Register | 11,300 |
| `appendices/H_Risk_Taxonomy_Basel_ICAAP_Stress_Scenarios_and_Ratio_Library.md` | Risk Taxonomy, Basel Mapping, ICAAP, Stress Scenarios and Ratio Library | 17,000 |
| `appendices/I_Regulatory_Returns_CIC_and_Tax_Return_Catalogue.md` | Regulatory Returns, Credit-Bureau and Tax Return Catalogue | 7,400 |
| `appendices/J_Accounting_Auditing_and_Secretarial_Standards_Map.md` | Accounting, Auditing and Secretarial Standards Map | 5,800 |
| `appendices/K_Vidhi_AI_Agent_Specification.md` | Vidhi AI Agent Specification | 6,200 |
| `appendices/L_Integration_Adapters_and_API_Catalogue.md` | Integration Adapters and API Catalogue | 6,200 |
| `appendices/M_Export_Package_LDC-EXPORT-1.0_and_Folder_Taxonomy.md` | Export Package `LDC-EXPORT-1.0` and Folder Taxonomy | 5,800 |
| `appendices/N_Pricing_Plans_Add-ons_Revenue_Streams_and_Savings_Model.md` | Pricing, Plans, Add-ons, Revenue Streams and Savings Model | 9,300 |
| `appendices/O_Marketplace_Services_Catalogue_and_Professional_Rules.md` | Marketplace Services Catalogue and Professional Rules | 5,200 |
| `appendices/P_Website_Copy_SEO_GEO_Tutorials_and_Video_Plan.md` | Website Copy, Health-Check Question Bank, Glossary Priorities, Tutorial and Video Plan, SEO/GEO System | 11,700 |
| `appendices/Q_Security_Privacy_and_Certification_Readiness.md` | Security, Privacy and Certification Readiness | 6,500 |
| `appendices/R_Competitive_Research_and_Differentiation.md` | Competitive Research and Differentiation | 5,800 |
| `appendices/S_Cooperative_Societies_Law_and_Operations.md` | Co-operative Societies: Law and Operations | 5,600 |
| `appendices/T_HRMS_Labour_Codes_Registers_and_Payroll_Parameters.md` | HRMS, Labour Codes, Registers and Payroll Parameters | 6,400 |
| `appendices/U_Configuration_Framework_and_Settings_Catalogue.md` | Configuration Framework and Settings Catalogue (binding) | 13,600 |
| `appendices/V_Acceptance_Tests_and_UAT_Catalogue.md` | Acceptance Tests and UAT Catalogue | 7,700 |
| `appendices/W_Verification_Log_and_Open_Items.md` | Verification Log and Open Items | 8,200 |
| `appendices/X_Operations_Hub_Addendum_for_LawDocsComply.md` | Operations Hub Addendum for LawDocsComply | 3,700 |
| `part2_prompts/` (26 files) | Part-2 master command, 24 family commands, QA checklist | 21,000 |
| `templates/` (24 workbooks) | Excel question templates `LDC-TPL-<FAMILY>-v1.0`, validator, validation report, build scripts | — |
| `condensed/LawDocsComply_Master_Prompt_ClaudeCode_v1.0.md` | LAWDOCSCOMPLY — MASTER BUILD PROMPT FOR CLAUDE CODE (v1.0, 25 October 2026) | 36,600 |
| `condensed/LawDocsComply_Phase_Runbook_v1.0.md` | LAWDOCSCOMPLY — PHASE RUNBOOK FOR CLAUDE CODE (v1.0, 25 October 2026) | 26,100 |
| **Total (Markdown)** | | **584,400** |


Folders also include `_research/` (dated research notes from the twelve streams and the superseded authoring conventions) and `_review/` (six review logs). A consolidated Word copy of the whole pack (`LawDocsComply_Build_Prompt_Pack_v1.0.docx`) and Word copies of the condensed Master Prompt and Phase Runbook are included for review and sign-off.

**Excel templates (Part 2)** — `templates/`:

- `LDC-TPL-COOP-CCS-v1.0 - Credit Co-operative Societies.xlsx`
- `LDC-TPL-COOP-GEN-v1.0 - Other Co-operative Societies.xlsx`
- `LDC-TPL-CYBER-v1.0 - Cyber Security.xlsx`
- `LDC-TPL-DATA-PRIV-v1.0 - Data Protection and Privacy.xlsx`
- `LDC-TPL-IFSCA-FCFU-v1.0 - IFSCA Finance Companies and Units.xlsx`
- `LDC-TPL-IFSCA-FME-v1.0 - IFSCA Fund Management Entities.xlsx`
- `LDC-TPL-IFSCA-GEN-v1.0 - IFSCA Regulated Entities.xlsx`
- `LDC-TPL-IRDAI-INS-v1.0 - Insurers.xlsx`
- `LDC-TPL-IRDAI-INT-v1.0 - Insurance Intermediaries.xlsx`
- `LDC-TPL-LAB-POSH-v1.0 - Labour Codes and POSH.xlsx`
- `LDC-TPL-MCA-CO-v1.0 - Companies.xlsx`
- `LDC-TPL-MCA-LLP-v1.0 - LLPs.xlsx`
- `LDC-TPL-RBI-ARC-v1.0 - Asset Reconstruction Companies.xlsx`
- `LDC-TPL-RBI-NBFC-v1.0 - NBFCs.xlsx`
- `LDC-TPL-RBI-OTH-v1.0 - Other RBI Regulated Entities.xlsx`
- `LDC-TPL-RBI-RCB-v1.0 - Rural Co-operative Banks.xlsx`
- `LDC-TPL-RBI-SCB-v1.0 - Commercial Banks SFBs PBs LABs RRBs.xlsx`
- `LDC-TPL-RBI-UCB-v1.0 - Urban Co-operative Banks.xlsx`
- `LDC-TPL-SEBI-AIF-v1.0 - Alternative Investment Funds.xlsx`
- `LDC-TPL-SEBI-INT-v1.0 - SEBI Intermediaries.xlsx`
- `LDC-TPL-SEBI-LISTED-v1.0 - Listed Entities.xlsx`
- `LDC-TPL-SEBI-MF-v1.0 - Mutual Funds.xlsx`
- `LDC-TPL-SEBI-REIT-INVIT-v1.0 - REITs and InvITs.xlsx`
- `LDC-TPL-TAX-GST-v1.0 - GST and Direct Tax.xlsx`

Each keeps the owner's row 1 and row 2 exactly, rebuilds the `Rough` sheet with family-specific lists and named ranges, places dropdowns on columns C, D, H, M, O, R (and a reference list on P) for rows 3–2000, and adds a protected `_Template_Info` sheet with the template code, version, regulator, column contract, header hash and a worked example row. After any change run `python3 templates/_validate_templates.py templates "<path to the owner's sample workbook>.xlsx" > templates/_validation_report.md` (the sample is used to confirm rows 1–2 are unchanged); the latest report shows 24/24 PASS.

## 3. How to run the build (Part 1)

1. Create or open the LawDocsComply repository and open Claude Code in it.
2. **Session 1 (P00):** commit `01_MASTER_PROMPT.md` as `docs/00-master-prompt.md`, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` as `docs/01-decision-log.md`, `phases/` and `appendices/` under `docs/`, and the Ecosystem Integration Specification v1.1 unchanged as `docs/ecosystem/infrabyx-integration-spec.md`. Then type: *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P00_Foundations_Repository_Discovery_and_Migration.md in full, plus the appendices it names. Write docs/phases/P00-plan.md and stop for my approval."*
3. **Every later session:** use the session prompt for that phase in `condensed/LawDocsComply_Phase_Runbook_v1.0.md`. Approve each plan before code is written. Each phase stops at its exit gate (§13 of the phase file, plus master §15 Definition of Done).
4. **Order and waves (master §13):**
   - **Wave 1 — Compliance Core GA:** P00 → P01 → P02 → P03 → P04 → P05; in parallel P15 (RBI-NBFC, MCA-CO, DATA-PRIV, IFSCA-GEN first), P17 runtime, P18 core, P19 core, P06, P07, P20, P23; then P24.
   - **Wave 2 — Risk, Audit, Returns, Data:** P08, P09, P10, P11, P12, P14, the rest of P15, P17, P18, P19; then P24.
   - **Wave 3 — People, Co-operatives, Services:** P13, P16, P21, P22; then P24.
5. **Precedence on conflict:** master §18 (master → `02` → Appendix G → E → B → A → D → U → C → phase file → other appendices; the Ecosystem Spec prevails for cross-product contracts).
6. **Unverified facts:** 1,150-odd `[VERIFY]` markers remain by design. Any feature depending on one ships behind a flag that is OFF (or advisory-only, NN-38) until the fact is checked against the primary source (Appendix W).

**Indicative effort:** about 190 squad-sprints in total; with seven squads running in parallel, Wave 1 GA in about 25 two-week sprints (roughly 12 months) and all three waves in about 46 sprints; with fewer squads expect 60–70 sprints.

**Condensed edition (Finbyx style):** `condensed/LawDocsComply_Master_Prompt_ClaudeCode_v1.0` (master + decisions + objective and scope of every phase + appendix index) and `condensed/LawDocsComply_Phase_Runbook_v1.0` (session prompts, objectives, exit gates, integration notes) — the same content as the pack in two documents.

## 4. How to produce the question sheets (Part 2)

1. Open a new Claude chat (Cowork). Attach: the family template from `templates/`, the regulator's source PDF(s) for one instrument, `part2_prompts/00_Part2_Master_Command.md`, the family command (`part2_prompts/NN_<FAMILY>_Command.md`) and `part2_prompts/99_QA_Checklist_for_Question_Sheets.md`.
2. Ask for **one** sheet first; check it; then proceed instrument by instrument (the owner's established method).
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

**Counsel questions** are listed in `02` §5 (CICRA, BCI/ICAI/ICSI marketplace rules, LODR Reg 24A, RBI outsourcing of compliance/IA, DPDP roles and cross-border routing, trials as production tenants, savings-claim wording, eSign exclusions, co-operative e-meetings, health-check data terms).

**Ecosystem change requests and companion addenda** (Ecosystem Spec v1.2, Finbyx and Operations Hub) are listed in master §19 and Appendix X.

## 6. Requirement coverage

All 102 requirements of the brief are mapped to phases and appendices in `02` §8. Requirements the pack narrowed or replaced after challenge are marked there with the decision that governs them.

## 7. Immediate actions independent of the build

- Remove "ISO 27001 certified" and any other unevidenced claim from lawdocscomply.com (X-22).
- Make the public site server-rendered so that search engines and AI crawlers can read it; keep or 301-redirect the 15 existing sitemap URLs (X-21).
- Fix the brand colours that fail contrast before new marketing material is produced (X-20).
- Start Part-2 sheets for the Wave-1 families: RBI-NBFC (the 2025 consolidated directions and the 31 Jul 2026 DoS set first), MCA-CO, DATA-PRIV and IFSCA-GEN.
