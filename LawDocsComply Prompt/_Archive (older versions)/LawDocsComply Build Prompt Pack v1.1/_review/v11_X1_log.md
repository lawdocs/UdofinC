# v1.1 X1 — cross-file resolution and re-audit log

Scope: F1–F6 cross-file requests and G4 integration notes applied to phases/appendices; ESG-BRSR template family built; Appendix AC re-audited; pack-wide consistency scan. All edits marked *(v1.1)* / *(v1.1, X1)*. Lead-owned files (01_MASTER_PROMPT, 02_*, 00_README, phase §16, §B.9, §C.9, §U.9, App V, App W) not edited.

## Changes by file

| File | Change |
|---|---|
| `appendices/D_Roles_Personas_and_Access_Control_Matrix.md` | D: prt_content_author row; / `prt_delivery_professional` / Local professional deliverin; D: ext_contractor; / TREASURER (co-operatives; treasury heads) /; Each Vidhi role agent (VA-01…VA-15, P17/Appendix AA); / SoD-24 / Applicability challenger deciding their own chall; D: rpt permission set; / `coop_office_bearer` / President, vice-president, secretar |
| `phases/P25_Global_Jurisdiction_Packs_Multi_Region_and_Partner_Network.md` | partner role names canonicalised; / **New** `prt_delivery_professional` / Answers on-call quer; added §4X cross-file hooks (1 FRs) |
| `phases/P18_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md` | partner role names canonicalised |
| `_contrib/v11/G1_master_notes.md` | partner role names canonicalised |
| `_contrib/v11/G1_screens.md` | partner role names canonicalised |
| `_contrib/v11/F6_open_items.md` | partner role names canonicalised |
| `phases/P04_Compliance_Workspace_Maker_Checker_Calendar_Tasks_Notifications.md` | `GET /rpt/compliance/score` (served by P28's `rpt` module fr; added §4X cross-file hooks (6 FRs); MCP tool names aligned to AA §AA.7.4; / `wf.agent.coordinator.autonomy` *(v1.1)* / T / L1 / L0–L2  |
| `appendices/C_Information_Architecture_Screens_Menus_and_Dashboards.md` | Home (role dashboard) ......................................;   ├ Compliance register (all obligations; list / timeline / ;   ├ Compliance health score ................................; §C.6.1 widget catalogue: 41 rows added for widgets used in layouts/P28 FR-P28-09 but undefined |
| `appendices/B_Data_Model_Events_and_Error_Codes.md` | use the prefix `gov.rpt_txn_*` (or `gov.related_party_*`) an; **Score names (v1.1; G5 E-06).** Three different scores must; **Compliance Health Index** (`rpt.compliance_health_index`,  |
| `phases/P28_Reports_MIS_and_Board_Pack_Studio.md` | **FR-P28-05 — Three distinct scores (G5 error E-06).** The d; added §4X cross-file hooks (1 FRs) |
| `phases/P01_Identity_Tenancy_Onboarding_and_Access.md` | / SCR-IAM-69 / Tracker import — upload, mapping review queue; added §4X cross-file hooks (3 FRs) |
| `phases/P26_Litigation_Legal_Matters_Contracts_Licences_and_Ethics_Registers.md` | These map into the LDC-EXPORT-1.0 top-level folder for legal; / OI-P26-13 / Export folder number for legal matters in Appe; added §4X cross-file hooks (2 FRs) |
| `phases/P27_ESG_BRSR_CSR_and_Sustainability.md` | / OI-P27-11 / Export folder number for Sustainability in App; added §4X cross-file hooks (1 FRs) |
| `phases/P17_Vidhi_AI_Employee_Agents_and_Knowledge_Notebooks.md` | tenants on Enterprise plans run a quarterly kill-switch dril; / `ai.killswitch.drill_frequency_days` / T / 90 / 30–365 / `; VA-14 Control Monitor, VA-15 AI Governance Officer Assistant; P18 hosts an MCP server (specification revision 2025-11-25;; **v1.1 deliverables** *(v1.1)*: agent workforce (VA-01–VA-15; V-SK-30 Voice note and call summary (consented recordings on; Each enabled agent per tenant is a Keycloak client (`agt_<te |
| `appendices/AA_Future_Ready_AI_and_Agentic_Architecture.md` | Quarterly drill per tenant on Enterprise plans (evidence for; / `ai.killswitch.drill_frequency_days` / T / 90 / 30–365 / `; / **VA-15 AI Governance Officer Assistant** *(v1.1)* / Maint; / `get_kri`, `get_ratio` / READ / Numbers from engines only ; **V-SK-30 Voice note and call summary** (consented recording; Keycloak client per tenant agent (`agt_<tenant>_<VA-nn>`); / — / PROHIBITED / Not exposed (approve, attest, mark compli |
| `appendices/U_Configuration_Framework_and_Settings_Catalogue.md` | / `ai.killswitch.drill_frequency_days` / T / 90 / 30–365; En |
| `phases/P02_Configuration_Studio_Rule_Engine_and_Settings.md` | / `ai.killswitch.drill_frequency_days` / T (owner P17) / 90 ; Every switch change is audited; propagation is verified (≤ 6 |
| `appendices/K_Vidhi_AI_Agent_Specification.md` | **V-SK-30 Voice note and call summary.** Purpose:; ## K.16 Agent cards (workforce VA-01–VA-15) *(v1.1)*; / VA-15 AI Governance Officer Assistant / 28 / READ, DRAFT, ; / `get_kri`, `get_ratio` / `T-erm-get_kri_history`, `T-rpt-g; > **v1.1 changes (25 October 2026):** new §K.15 skills V-SK-; / `attach_evidence_draft` / `T-dms-attach_to_record` / INTER |
| `appendices/Q_Security_Privacy_and_Certification_Readiness.md` | / REGULATOR_CONFIDENTIAL / Inspection reports, risk-assessme |
| `phases/P00_Foundations_Repository_Discovery_and_Migration.md` | `CREDENTIAL` (vault secrets, D-04) and `REGULATOR_CONFIDENTI; `beta-mirror` (a synthetic re-creation; Names, PANs and CINs in seeds use reserved invalid patterns |
| `appendices/A_Workflows_and_State_Machines.md` | A: added A.36–A.45 state machines; Timer: a test stuck in `RUNNING` beyond `ccm.run.timeout_min; (SLA by risk: High 30 days, Medium 60, Low 90 — tenant may s |
| `appendices/L_Integration_Adapters_and_API_Catalogue.md` | L: new adapters and port-name map; / `GET/POST /v1/esg/data-requests` ; `/metrics` ; `/ghg/inve |
| `appendices/M_Export_Package_LDC-EXPORT-1.0_and_Folder_Taxonomy.md` | M: 03 sub-folders; M: 15 sub-folders;     Regulatory Inspections/; / `inspection` / aud / `10 …/Regulatory Inspections/{date} -; / `control`, `control_test` / dpc / `12 …/` / `ISMS controls;     [Tenant DMS folders as configured]/  (originals and vers |
| `phases/P05_Regulatory_Change_Management_and_AI_Question_Authoring.md` | added §4X cross-file hooks (3 FRs); MCP tool names aligned to AA §AA.7.4; / `ai.agent.regulatory_analyst.autonomy` *(v1.1)* / G (platf |
| `phases/P06_Governance_Board_Committees_and_Company_Secretarial.md` | added §4X cross-file hooks (2 FRs) |
| `phases/P08_Enterprise_Risk_Management_and_CRO_Workspace.md` | added §4X cross-file hooks (1 FRs) |
| `phases/P09_Risk_Assessment_Lab_ICAAP_Stress_Testing_Capital_and_Ratios.md` | added §4X cross-file hooks (1 FRs) |
| `phases/P10_Audit_Management_Internal_RBIA_IS_Secretarial_Statutory.md` | added §4X cross-file hooks (2 FRs) |
| `phases/P11_Return_Studio_Data_Preparation_and_Accounting_Bridge.md` | added §4X cross-file hooks (3 FRs) |
| `phases/P12_Data_Protection_Cyber_Security_IT_Governance_and_TPRM.md` | added §4X cross-file hooks (3 FRs) |
| `phases/P13_HRMS_People_and_Labour_Compliance_Suite.md` | added §4X cross-file hooks (2 FRs) |
| `phases/P15_Sector_Packs_and_Entity_Logic.md` | added §4X cross-file hooks (1 FRs) |
| `phases/P16_Cooperative_Society_Operations_Suite.md` | added §4X cross-file hooks (1 FRs) |
| `phases/P20_Pricing_Plans_Subscriptions_Billing_Savings_and_Revenue_Streams.md` | added §4X cross-file hooks (3 FRs) |
| `phases/P22_Service_Delivery_Console_and_Operations_Hub_Interface.md` | added §4X cross-file hooks (1 FRs) |
| `phases/P23_Public_Website_Health_Check_Help_Centre_Tutorials_and_Accessibility.md` | added §4X cross-file hooks (1 FRs); The health check is LawDocsComply's lead magnet and the star |
| `/home/claude/ldc_v11/appendices/AC_Baseline_and_Brief_Traceability_Matrix.md` | AC re-audit: v1.1 status column, §AC.0 summary and open list |
| `appendices/AC_Baseline_and_Brief_Traceability_Matrix.md` | ## AC.2 Summary |
| `phases/P03_Regulatory_Content_Library_Template_Registry_and_Excel_Import.md` | MCP tool names aligned to AA §AA.7.4 |
| `appendices/E_Excel_Template_Contract_Entity_Families_and_Importer.md` | MCP tool names aligned to AA §AA.7.4 |
| `_contrib/v11/F2_settings.md` | autonomy keys aligned |
| `templates/LDC-TPL-ESG-BRSR-v1.0 - ESG BRSR and CSR.xlsx` | New family (built by `templates/_build/v11_X1_build_esg.py`); validator 27/27 PASS; `_validation_report.md` regenerated |
| `part2_prompts/27_ESG-BRSR_Command.md` | New Part 2 command for ESG-BRSR |
| phases P01, P04–P06, P08–P13, P15, P16, P20, P22, P23, P25–P28 | New `### 4X. Cross-file hooks` sections (FR-Pnn-X01…) |
| `appendices/C_*` | §C.6.1: 41 widget rows added (W-AI-05…08, W-AIG-01…04, W-ESG-01…05, W-FRM-01…04, W-GEM-01…04, W-LIT-01…06, W-PRT-01…03, W-RSK-07, W-RAL-10, W-RET-05/06, W-RPT-01…06, W-GRP-01); every widget code used in the pack is now catalogued (123) |
| `appendices/AC_*` | Re-audited: COVERED 938, PARTIAL 77, MISSING 12, CHANGED 42; new §AC.0 summary; 89 open rows grouped |

## Resolutions applied

- Partner roles canonical: `prt_admin`, `prt_content_reviewer`, `prt_delivery_professional`, `prt_viewer`, `prt_content_author`.
- Roles added: practitioner_admin/user, ten_legal_user, ext_contractor, ten_model_validator; KMP GC/CSO/CHRO/COO/AIO/MLRO-PO; coop TREASURER.
- `rpt` owned by P28; `gov.rpt_txn_*`; agent principals `agp_`; Work Inbox SCR-WF-00; SCR-CNT-16 (alias SCR-IAM-69); four score names incl. Compliance Health Index (App B §B.1.1).
- Export folders 25–29 per App M; P10 inspection = projections of P26; LEGAL_PRIVILEGED in App Q/P00.
- VA-15/16/17, skills V-SK-31–34, MCP `list_reports`/`run_report` and P03–P05 tools in K, AA, P17; snake_case MCP names and `ai.autonomy.agent.VA-nn` keys aligned.
- State machines A.36–A.45 (App A); adapters/port-name map (App L); reserved family codes PFRDA, MSME_FIRM, AML_RE (App E).
- Kill-switch drill: quarterly at platform level; tenant drills Enterprise-only — consistent across P17, P02, U §U.12, AA.

## Left for the lead

1. §C.9 compiled rows: SCR-CMP-02 and SCR-RPT-01/02 owner still P04 → should be P28.
2. §B.9 / §C.9 / §U.9 need compilation of v11 contrib (F1–F6, G1, G3, incl. F2_settings keys).
3. Master prompt: NN-47–55, D-34–48, linked-tenant wording, X-26 screen ownership (SCR-RPT-01/02 → P28, SCR-WF-00, SCR-CORE-21), folder 99 "Restricted", folders 25–29 names, effort updates (P17 13, P18 14, P19 10, P20 8, P21 9, P22 9, P23 10, P28 9).
4. P25 §16 still cites G1 proposal IDs.
5. Department code AIG not used by the AI-GOV family — confirm or drop.
6. 89 AC rows still PARTIAL/MISSING (see §AC.0).
7. Unverified: BSA privilege section references [VERIFY]; sanctions-screening vendor choice.

## Consistency scan

No broken file references, unbalanced code fences or malformed tables found; "238" appears only in source citations; all widget codes defined; ESG-BRSR validates.
