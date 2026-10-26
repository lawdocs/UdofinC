# Appendix W — Verification Log and Open Items

> Binding for every phase. Compiled by the pack lead on 25 October 2026. Every `[VERIFY]` marker in the pack and every open item below is a build flag: the dependent feature ships OFF (or advisory-only, NN-38) until the item is closed with evidence in `docs/compliance/verification-log.md`.

## W.1 Verification protocol

1. **Primary source first.** Re-check the fact on the regulator's or legislature's own site (Appendix F lists them); record URL, retrieval date, document hash and the exact paragraph.
2. **Classify the result:** `VERIFIED` (primary text read), `SECONDARY_ONLY` (only commentary found — feature stays advisory), `CHANGED` (fact differs — raise a content or rule-pack change), `NOT_CONFIRMED` (cannot be found — keep OFF).
3. **Close by data, not code:** most items are closed by a Governed change (rule pack, setting or content release, P02), never a code release (NN-34). Items needing code are raised as stories.
4. **Recheck triggers:** every closed item records what would reopen it (amendment, new circular, vendor contract change, annual review).
5. **Launch gates:** an item tagged as a launch gate in the phase file blocks the wave's P24 run until closed.

## W.2 `[VERIFY]` census (v1.1, 25 October 2026)

| File | Markers | File | Markers |
|---|---|---|---|
| AA_Future_Ready_AI_and_Agentic_Architecture | 18 | P00_Foundations_Repository_Discovery_and_Migration | 9 |
| AB_RBI_Consolidated_Directions_Content_Plan | 9 | P01_Identity_Tenancy_Onboarding_and_Access | 11 |
| AC_Baseline_and_Brief_Traceability_Matrix | 0 | P02_Configuration_Studio_Rule_Engine_and_Settings | 8 |
| A_Workflows_and_State_Machines | 6 | P03_Regulatory_Content_Library_Template_Registry_and_Excel_Import | 3 |
| B_Data_Model_Events_and_Error_Codes | 2 | P04_Compliance_Workspace_Maker_Checker_Calendar_Tasks_Notifications | 4 |
| C_Information_Architecture_Screens_Menus_and_Dashboards | 1 | P05_Regulatory_Change_Management_and_AI_Question_Authoring | 5 |
| D_Roles_Personas_and_Access_Control_Matrix | 2 | P06_Governance_Board_Committees_and_Company_Secretarial | 49 |
| E_Excel_Template_Contract_Entity_Families_and_Importer | 20 | P07_Policy_Lifecycle_and_Document_Management_System | 9 |
| F_Regulatory_Source_Register_and_Monitoring_Catalogue | 95 | P08_Enterprise_Risk_Management_and_CRO_Workspace | 28 |
| G_Legal_and_Regulatory_Rules_Register | 74 | P09_Risk_Assessment_Lab_ICAAP_Stress_Testing_Capital_and_Ratios | 48 |
| H_Risk_Taxonomy_Basel_ICAAP_Stress_Scenarios_and_Ratio_Library | 139 | P10_Audit_Management_Internal_RBIA_IS_Secretarial_Statutory | 57 |
| I_Regulatory_Returns_CIC_and_Tax_Return_Catalogue | 79 | P11_Return_Studio_Data_Preparation_and_Accounting_Bridge | 59 |
| J_Accounting_Auditing_and_Secretarial_Standards_Map | 73 | P12_Data_Protection_Cyber_Security_IT_Governance_and_TPRM | 46 |
| K_Vidhi_AI_Agent_Specification | 3 | P13_HRMS_People_and_Labour_Compliance_Suite | 30 |
| L_Integration_Adapters_and_API_Catalogue | 21 | P14_Grievance_Redressal_and_Customer_Support_Desk | 57 |
| M_Export_Package_LDC-EXPORT-1.0_and_Folder_Taxonomy | 2 | P15_Sector_Packs_and_Entity_Logic | 38 |
| N_Pricing_Plans_Add-ons_Revenue_Streams_and_Savings_Model | 10 | P16_Cooperative_Society_Operations_Suite | 60 |
| O_Marketplace_Services_Catalogue_and_Professional_Rules | 18 | P17_Vidhi_AI_Employee_Agents_and_Knowledge_Notebooks | 8 |
| P_Website_Copy_SEO_GEO_Tutorials_and_Video_Plan | 32 | P18_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform | 15 |
| Q_Security_Privacy_and_Certification_Readiness | 26 | P19_Data_Preservation_Portability_and_BYO_Storage | 5 |
| R_Competitive_Research_and_Differentiation | 7 | P20_Pricing_Plans_Subscriptions_Billing_Savings_and_Revenue_Streams | 11 |
| S_Cooperative_Societies_Law_and_Operations | 79 | P21_Marketplace_Retainers_and_FinLegal_Academy | 25 |
| T_HRMS_Labour_Codes_Registers_and_Payroll_Parameters | 30 | P22_Service_Delivery_Console_and_Operations_Hub_Interface | 4 |
| U_Configuration_Framework_and_Settings_Catalogue | 15 | P23_Public_Website_Health_Check_Help_Centre_Tutorials_and_Accessibility | 21 |
| V_Acceptance_Tests_and_UAT_Catalogue | 1 | P24_Engineering_Governance_Hardening_Certification_Readiness_and_GoLive | 12 |
| W_Verification_Log_and_Open_Items | 31 | P25_Global_Jurisdiction_Packs_Multi_Region_and_Partner_Network | 5 |
| X_Operations_Hub_Addendum_for_LawDocsComply | 3 | P26_Litigation_Legal_Matters_Contracts_Licences_and_Ethics_Registers | 9 |
| Y_Global_Compliance_Expansion_and_Jurisdiction_Packs | 29 | P27_ESG_BRSR_CSR_and_Sustainability | 24 |
| Z_Customer_Feedback_Reverse_Engineering_and_Improvement_Backlog | 0 | P28_Reports_MIS_and_Board_Pack_Studio | 5 |

Total: 1490 markers. In addition, 318 of the 320 RBI catalogue reference numbers are derived from RBI serials and are verified as each question sheet is written (D-39; importer gate in Appendix E).

## W.3 Owner decisions and counsel questions

See `02` §4 (14 owner decisions) and §5 (10 counsel questions). They are also open items and gate the phases named there.

## W.4 Open items by stream

### Open items — stream S11 (P00, P01, P24, App B, Q)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P00-01 | Legacy Railway / Atlas regions | No account access yet | Owner/CTO | Treat as non-India; disclose; fix cut-over | P00 |
| OI-P00-02 | Supabase PG major version & PITR | Plan-dependent | CTO | PG16 features; daily dumps to ap-south-2 | P00 |
| OI-P00-03 | Temporal Cloud India residency | Vendor | CTO | Self-host | P00 |
| OI-P00-04 | Observability vendor India residency | Vendor | CTO | Self-hosted LGTM | P00 |
| OI-P00-05 | RFC 3161 TSA provider | Contract | CTO/CS | core.audit.anchor.tsa.enabled=OFF | P00 |
| OI-P00-06 | Legacy password hash import | Discovery | Tech lead | Forced reset | P00 |
| OI-P00-07 | Citations of legacy and Sep-2026 RBI banks | Need PDFs | CS | NEEDS_REVIEW | P00 |
| OI-P00-08 | Regulator confidentiality of supervisory correspondence stored with vendor | Legal | Counsel | REGULATOR_CONFIDENTIAL class, opt-in | P00 |
| OI-P00-09 | Node 26 LTS support | Timing | Tech lead | Node 24 | P00 |
| OI-P00-10 | GST invoice numbering/rounding | Tax | CA | Gap-free per-FY per-GSTIN | P00 |
| OI-P01-01 | MCA data provider contract and reuse terms | Vendor/legal | CTO/CS | iam.kyb.mca.enabled=OFF | P01 |
| OI-P01-02 | GSP/ASP for GSTIN search | Vendor | CTO | Manual GSTIN + checksum | P01 |
| OI-P01-03 | PAN verification route | Eligibility | CTO/CA | Format validation | P01 |
| OI-P01-04 | Regulator public registers terms | Terms | Compliance | "Unverified" badge | P01 |
| OI-P01-05 | DLT principal entity | Telecom | CS | Email OTP | P01 |
| OI-P01-06 | Supervisor grantee/basis codes for SEBI/IRDAI/RCS | Ecosystem change | Spec owner | Map to CONTRACT | P01 |
| OI-P01-07 | Director data notice under DPDP | Legal | Counsel | Client instruction + template | P01 |
| OI-P01-08 | Keycloak SCIM | Product | Tech lead | SCIM in iam | P01 |
| OI-P01-09 | DPDP notice rule number; consent manager | Phased | DPO | Flag OFF | P01 |
| OI-P01-10 | GST rate/SAC for SaaS | Tax | CA | "GST as applicable" | P01 |
| OI-P01-11 | Aadhaar OVSE need | UIDAI | CS | DigiLocker/upload | P01 |
| OI-P24-01 | GHEC + security products licensing | Budget | CTO/Board | Compensating workflow | P24 |
| OI-P24-02 | CERT-In 2025 audit guidelines original text | Secondary source | Security | Annual + major-change audit | P24 |
| OI-P24-03 | RBI IT outsourcing paras (2025 consolidation) | Renumbering | Compliance | Contract audit clause | P24 |
| OI-P24-04 | PCI SAQ A eligibility with Razorpay/QSA | Validation | CFO/security | Hosted checkout + script monitoring | P24 |
| OI-P24-05 | ISO 27701:2025 transition | CB rules | CS | After 27001 | P24 |
| OI-P24-06 | DPDP breach rule/commencement | Phased | DPO | Build now | P24 |
| OI-P24-07 | Status/paging vendor residency | Vendor | SRE | Self-host | P24 |
| OI-P24-08 | Annual freeze calendar | Annual | Compliance reviewer | Defaults | P24 |
| OI-P24-09 | Deprecation header RFCs | Standards | Tech lead | Sunset RFC 8594 | P24 |
| OI-P24-10 | MeitY empanelment of regions | Tender | CS | Disclose on request | P24 |
| OI-Q-01..08 | ASVS mapping; framework mapping validation; BSA s.63 form; RBI portal credential terms; AI provider region/retention; SEBI PIT 3(5) scope; DPDP breach form; KMS FIPS statement | See Appendix Q §Q.16 | various | see Q | Q |

### Open items — stream S12 (P02, App A, C, D, U)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P02-01 | RB-IOS 2026 clause numbers (RE reply window, filing window) | Scheme text not verified at clause level | Content checker | 30-day floor labelled [VERIFY clause] | P02 |
| OI-P02-02 | SS-1/SS-2 para numbers and any 2024–26 revisions | ICSI pages not retrievable during research | S3/content | 15/30-day values SECONDARY_ONLY | P02 |
| OI-P02-03 | DPDP r.7 commencement for breach obligations | Phased commencement | LDC DPO | Protective rule active; outputs indicative | P02 |
| OI-P02-04 | State and IFSC holiday calendars | Annual sourcing per State | Content | National + RBI only; State flag OFF | P02 |
| OI-P02-05 | ZEN engine Node binding maturity; CEL JS implementation | Library versions | CTO | JSON Logic behind RULES_PORT | P02 |
| OI-P02-06 | Custom field limit performance | Load test | Engineering | Bound 100 | P02 |
| OI-P02-07 | Co-operative terminology by State Act | State Acts differ | S7 | "Managing Committee" default | P02 |
| OI-C-01 | Permission to display regulator logos | Trademark/emblem use | Legal | Text chips only | Appendix C |
| OI-D-01 | Seat model for board members, auditors, viewers | Commercial decision | P20 / owner | Recommendation in D.13 | Appendix D |
| OI-D-02 | Internal Ombudsman applicability thresholds per RE type (current consolidated RBI directions) | Verify current instrument | S6/S7 | IO workflow behind flag per tenant | Appendix D/A |
| OI-U-01 | Committee applicability in setting packs (by NBFC layer/UCB tier/listed size) | Must be sourced per rule pack | S7 | Packs propose; rule engine decides with citations | Appendix U |

### Open items — stream S1 (P03–P05, App F)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P03-01 | `_LDC_System` hidden sheet in exports | Not in D-08 | Owner / S2 | DB round-trip by CompID | P03 |
| OI-P03-02 | Multi-value separator col D; DV error style | Excel list DV is single-value | S2 / owner | Accept ; and , ; DV "Information" style [VERIFY App E] | P03 |
| OI-P03-03 | Canonical RBI website | website.rbi.org.in redirects | Content lead | Monitor both | P03 |
| OI-P03-04 | IRDAI canonical document site | policyholder.gov.in listings | Content lead | Monitor both | P03 |
| OI-P03-05 | Licensed third-party content | Global packs | Owner | CONTENT_FEED_PORT OFF | P03 |
| OI-P03-06 | Clause index for scanned instruments | OCR quality | Content lead | Manual clause entry | P03 |
| OI-P03-07 | Re-verification cadence | Proposal | Content lead | Setting | P03 |
| OI-P03-08 | Legacy beta tenant texts | Branch beta | Owner | Overlays pinned | P03 |
| OI-P04-01 | Holiday-shift conventions per regulator | Vary | Content lead | NONE default | P04 |
| OI-P04-02 | M365 consent model | Customer IT | Customer IT | Delegated OAuth | P04 |
| OI-P04-03 | WhatsApp BSP / SMS aggregator | Contracts, DLT | Owner | OFF | P04 |
| OI-P04-04 | MD/CEO certificate by entity type | Varies | Content lead | Configurable chain | P04 |
| OI-P04-05 | Compliance score method | Owner preference | Owner | Transparent default | P04 |
| OI-P04-06 | Apple calendar push | No API | — | ICS/CalDAV | P04 |
| OI-P04-07 | Due rules for migrated rows | Authoring backlog | Content team | Frequency defaults flagged | P04 |
| OI-P05-01 | RBI RSS scope | Unknown | Content lead | Listing parsers | P05 |
| OI-P05-02 | IFSCA no RSS; egress | Allowlist | CTO | INTRADAY scrape | P05 |
| OI-P05-03 | IRDAI canonical site | — | Content lead | Monitor both | P05 |
| OI-P05-04 | State co-op registrar sites | 28+ states, languages | Content lead / S7 | WEEKLY_DEEP + OCR/translation | P05 |
| OI-P05-05 | Licensed news feed | Cost | Owner | OFF | P05 |
| OI-P05-06 | Claude India residency / retention | Contract | CTO | Platform runs on public docs only | P05 |
| OI-P05-07 | Penalised entity names display | Reputation | Counsel | Flag | P05 |
| OI-P05-08 | Regulator e-mail alerts | Availability | Content lead | Optional | P05 |
| OI-P05-09 | Radar AI gist | Accuracy | Content lead | OFF until gate | P05 |
| OI-F-01 | All [VERIFY] URLs in Appendix F | Not opened / redirects | P05 sprint 1 | Test-fetch log | App F |

### Open items — stream S2 (App E, templates)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P03-E01 | NBFC layer thresholds / Top Layer status (SBR Directions 2025) | Not re-read from primary text | Content maker (RBI) | Conditions editable in Content Studio | P03/P15 |
| OI-P03-E02 | Titles/numbers of RBI/DoS/2026-27/461–468 | Only /460 confirmed | Content maker (RBI) | [VERIFY] in family command | P03 |
| OI-P03-E03 | UCB tier and BoM thresholds (2025 UCB directions) | Not re-read | Content maker | Values in S | P15 |
| OI-P03-E04 | NABARD vs RBI routing of RCB returns | Varies by return | S5 | Both in P list | P11 |
| OI-P03-E05 | IRDAI 2024–26 regulation titles; composite licence post-2025 Act | Commencement unverified | Content maker (IRDAI) | Value marked [VERIFY] | P15 |
| OI-P03-E06 | SEBI SIF / MF Lite / AIF co-investment status | Recent frameworks | Content maker (SEBI) | [VERIFY] values | P15 |
| OI-P03-E07 | MSCS Act 2023 section numbers | Not re-read | Content maker (Co-op) | s.120 [VERIFY] | P16 |
| OI-P03-E08 | Labour Code State rules; unified portal name | Phased notification | Content maker (Labour) | P token [VERIFY] | P13 |
| OI-P03-E09 | Income-tax Act 2025 form/section numbers; GST due dates post GST 2.0 | New law | Content maker (Tax) | LDC-TPL-018 until set | P11 |
| OI-P03-E10 | California CPPA naming; 2025 CCPA regs dates | Rebranding / phasing | Content maker (Privacy) | Generic P token | P12 |
| OI-P03-E11 | Owner to confirm "Every 2/3/5 Years" frequency additions | Beyond owner's list | Owner | IFSCA-GEN unchanged | P03 |
| OI-P03-E12 | Owner to confirm `_Template_Info` password/visibility | Convenience | Owner | Patch version | P03 |
| OI-P03-E13 | ASVS 5.0 file-handling chapter numbering | Not re-read | S11 | — | P24 |

### Open items — stream S3 (P06–P07)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P06-01 | Para-level citations of revised SS-1/SS-2 (effective 1 Apr 2024) for notice, notes, minutes timelines, circular resolutions | ICSI text to be checked para by para | CS domain analyst | Use values in §9 (aligned with Act); citations shown as "SS-1 [VERIFY]" | P06 |
| OI-P06-02 | Corporate Laws (Amendment) Bill 2026 — enacted status and threshold changes for Companies Act and LLP Act | Bill introduced in Lok Sabha (reported Apr 2026) | Company Secretary | Rule packs carry current thresholds; new pack version on enactment | P06 |
| OI-P06-03 | Director KYC revised form name and event-based update timeline under the 2025 amendment rules | ICAI note does not name form | CS analyst | Filing definition `DIR_KYC_TRIENNIAL` with due 30 Jun 2028 | P06 |
| OI-P06-04 | RBI (Commercial Banks – Governance) Directions 2025 para mapping | Not yet extracted | P15 stream / RBI analyst | Bank governance pack ships behind `pack.rbi_cb_governance.enabled = OFF` | P06 |
| OI-P06-05 | Final status of the June 2026 draft NBFC Governance Amendment Directions (CCO/HIA) and the July 2026 RBI/DoS/2026-27/460–468 directions | Draft proposed effective 1 Jan 2027 | RBI analyst | Seed current 2025 text; draft rules as future-dated version flagged `draft` | P06 |
| OI-P06-06 | MCA general circular currently permitting VC/OAVM general meetings and its validity | Circulars are periodically extended | CS analyst | `gov.gm.vc_allowed` default false after last known expiry date | P06 |
| OI-P06-07 | Restricted items for VC board meetings after omission of Rule 4 (2021) and revised SS-1 wording | Confirm no re-notification | CS analyst | `gov.vc.restricted_items = []` | P06 |
| OI-P06-08 | Reg 30(6) disclosure timelines and Reg 30(11) rumour-verification applicability as on go-live | LODR amended frequently | Listed-company analyst | Clocks as in §4K; flag `gov.lodr.rumour_verification` per entity | P06 |
| OI-P06-09 | PIT pre-clearance validity, continual disclosure trigger and trading-plan rules after 2024–2025 amendments | Amendments | Compliance analyst | Settings bounded by current text | P06 |
| OI-P06-10 | HVDLE threshold and debt-listed governance applicability | 2025 amendment | Listed-company analyst | Chapter V pack OFF unless entity marks HVDLE | P06 |
| OI-P06-11 | MCA additional-fee schedules and CHG-1 extension windows after the 2019/2020 amendments | Fee rules | CS analyst | Fee meter shows "statutory additional fee [VERIFY]" | P06 |
| OI-P06-12 | IRDAI Master Circular on Corporate Governance 2024 — board meeting frequency and specific committee quorum rules | Not captured in secondary source | Insurance analyst | Use Companies Act defaults for insurers until verified | P06 |
| OI-P06-13 | Licensed MCA data provider selection and terms (no scraping) | Vendor contract | CTO | `gov.mca_refresh.enabled = OFF` | P06 |
| OI-P06-14 | E-voting agencies' current file formats | Agency specifications | Integration analyst | Manual CSV template | P06 |
| OI-P06-15 | Whether NBFC s.186(11) exemption interpretation for MBP-2 should default ON for NBFCs in the ordinary course of business | Interpretation | Company Secretary | Default: maintain MBP-2 for non-ordinary-course items; [INTERP] banner | P06 |
| OI-P07-01 | Microsoft CSPP eligibility for WOPI-based Office for the web | Program limited to cloud-storage ISVs | CTO | Graph co-authoring via tenant SharePoint/OneDrive; embedded editor flag OFF | P07 |
| OI-P07-02 | Licence choice for embedded editor (Collabora Online vs ONLYOFFICE) and tracked-changes fidelity | Licence/fidelity | CTO | `dms.embedded_editor.enabled = OFF` | P07 |
| OI-P07-03 | ASP vs ESP contracting (Leegality/Digio/SignDesk/Surepass are application service providers over CCA-empanelled ESPs) and commercial terms | Vendor | CTO/Procurement | Sandbox only | P07 |
| OI-P07-04 | Current IT Act First Schedule list and any amendments | Statute check | Legal analyst | Seed list in §4N; block-by-default | P07 |
| OI-P07-05 | State-wise e-stamping matrix and adapter | Varies by state | Legal analyst | `dms.estamp.enabled = OFF`; manual stamping checklist | P07 |
| OI-P07-06 | Retention floors (Income-tax Act 2025 records, Labour Codes registers, RBI record retention post-2025 consolidation) | Statute check | CCO/legal | Conservative floor (8 years) applied to unverified classes | P07 |
| OI-P07-07 | Per-language OCR/MT quality for low-resource scripts (Ol Chiki, Meetei Mayek, Kashmiri, Sindhi, Dogri, Bodo, Santali) | Evaluation | P17 | Tier C (review mandatory) | P07 |
| OI-P07-08 | Bhashini API terms, residency and retention | Vendor terms | CTO | Not enabled | P07 |
| OI-P07-09 | Mandatory-contents checklists for each required policy (per pack) | Content work in P15 / Part 2 | Content team | Gap check shows "checklist not available" | P07 |
| OI-P07-10 | Website-publication requirements per regulator for policies (Fair Practices Code, grievance policy etc.) after 2025 consolidation | Content check | P15 | Publication flag per policy without legal assertion | P07 |
| OI-P07-11 | BSA 2023 s.63 certificate format for type copies vs originals (Part A/B) | Legal interpretation | Legal analyst | Type copy footer + original attached; certificate from P19 for exports | P07 |

### Open items — stream S4 (P08–P09, App H)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P08-01 | NBFC Governance Directions 2025 paras for RMC (9), CRO (19–24), Board reviews (15) | Taken from Finbyx v1.5 | Platform content (RBI) | [VERIFY] badge | P08 |
| OI-P08-02 | LODR Reg 21 scope and Sch II Part D(C) RMC role text | Frequent amendments | Platform content (SEBI) | pack.sebi_listed.rmc_scope | P08 |
| OI-P08-03 | SEBI MF RMF citation | Not verified | Platform content (SEBI) | Generic pack text | P08 |
| OI-P08-04 | IRDAI corporate governance 2024 RMC/CRO; Ind-RBC | Ind-RBC not final | Platform content (IRDAI) | 150% control level | P08 |
| OI-P08-05 | RBI ORM Guidance Note current reference and paras | Two references | Platform content (RBI) | Cite both [VERIFY] | P08 |
| OI-P08-06 | RBI MRM guidance final | Draft 24 Jun 2026 | Platform content (RBI) | erm.model_risk.rbi_2026_guidance.enabled = OFF | P08 |
| OI-P08-07 | RBI climate directions/disclosure final | Draft | Platform content (RBI) | Climate = voluntary/ICAAP-internal | P08 |
| OI-P08-08 | Bank Pillar 3 template list (Annex III) | Not extracted | Platform content (RBI) | erm.disclosure.bank_pillar3.enabled = OFF | P08 |
| OI-P08-09 | UCB RMC/CRO instruction | Not verified | Platform content (RBI) | Best-practice label | P08 |
| OI-P08-10 | Episode mapping during compliance-mode switch | Ecosystem §9.1 dual-publish | Integration lead | Producer episode_id master | P08 |
| OI-P08-11 | ARC risk-governance paras | Not verified | Platform content (RBI) | [VERIFY] | P08 |
| OI-P09-01 | NBFC CAP Ch V ICAAP paras | Not retrieved | Platform content (RBI) | Cite chapter | P09 |
| OI-P09-02 | Bank leverage minimum, D-SIB, CCyB, Pillar 3, ICAAP format headings, Annex IV sections | Not extracted | Platform content (RBI) | ral.bank.enabled = OFF | P09 |
| OI-P09-03 | Bank 2027 rule changes | Read via Finbyx | Platform content (RBI) | Parallel pack only | P09 |
| OI-P09-04 | SFB/PB/RRB capital minimums | Not verified | Platform content (RBI) | Family disabled | P09 |
| OI-P09-05 | ARC Directions 2025 ref, CRAR paras, SR investment rule | Secondary source | Platform content (RBI) | [VERIFY] | P09 |
| OI-P09-06 | IFSCA FC/FU capital numbers | Not extracted | Platform content (IFSCA) | IMPORTED_RESULT | P09 |
| OI-P09-07 | Insurer Ind-RBC and stress/FCR | Not final | Platform content (IRDAI) | Imported solvency | P09 |
| OI-P09-08 | CIC asset tests and leverage definitions | Not re-fetched | Platform content (RBI) | [VERIFY] | P09 |
| OI-P09-09 | RBI AIF-investment circulars (2023–2025) | Revisions unverified | Platform content (RBI) | [VERIFY] | P09 |
| OI-P09-10 | NBFC CON paras | Read via Finbyx | Platform content (RBI) | [VERIFY] | P09 |
| OI-P09-11 | Bank IRRBB instrument and shocks | Not verified | Platform content (RBI) | Behind flag | P09 |
| OI-P09-12 | Schedule III ratio list and 25% explanation rule | Verify current text | Platform content (MCA) | [VERIFY] | P09 |
| OI-P09-13 | Ecosystem change requests (RiskSegmentSnapshotPublished; Finbyx stress-runs API) | Spec §14.2 change process | Integration lead + owner | ral.stress.fx_mode = CONSUME_ONLY | P09 |
| OI-P09-14 | infrabyx-risk-kernel ownership | New decision | Owner / CTO | Vendored Finbyx RK6 formulas with shared fixtures | P09 |
| OI-P09-15 | Market-data licensing | Vendor terms | Procurement | Tenant-supplied prices | P09 |
| OI-P09-16 | UCB PSL target; UCB liquidity/ALM directions | Not verified | Platform content (RBI) | [VERIFY] | P09 |
| OI-H-01 | MFI qualifying-asset floor: 60% (Finbyx reading of MFI 12–13) vs 75% (owner baseline) | Conflicting internal sources | Platform content (RBI) | R47 uses rule-pack value; [VERIFY] before activation | P09 |
| OI-H-02 | Pillar 3 DIS template codes current list | Not re-verified | Platform content | Generic labels | P08 |

### Open items — stream S5 (P10–P11, App I–J)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P10-01 | NBFC SA Directions 2026 paragraph numbers | Carried from Finbyx; verify PDF | Domain analyst | Rows ACTIVE_UNVERIFIED; warnings only | P10 |
| OI-P10-02 | UCB internal audit / RBIA 2026 direction and threshold | Not fetched | Domain analyst | Legacy 2021 thresholds AU | P10 |
| OI-P10-03 | CYB 2026 para numbers for IS audit/VAPT | Carried | Domain analyst | AU | P10 |
| OI-P10-04 | Companies (Accounts) Rules r.13 internal-audit thresholds | Confirm current text | CS | Resolver "verify" note | P10 |
| OI-P10-05 | ICSI CSAS Revised Edition 2026 effective date/changes | Not published | CS | CSAS 2021 values | P10 |
| OI-P10-06 | LODR Reg 24A prohibited services and ASCR format | Confirm | CS | REC block list | P10 |
| OI-P10-07 | SEBI CSCRF / IRDAI / IFSCA cyber-audit frequencies | Evolving | CISO | Tenant cadence | P10 |
| OI-P10-08 | Bank LFAR format and RBI timeline | Verify | Domain analyst | LFAR pack OFF | P10 |
| OI-P10-09 | DPDP r.13 SDF audit commencement and auditor qualification | Phase 3 date | DPO | Voluntary audit | P10 |
| OI-P10-10 | Co-operative audit classification/rectification per State | 28 States + MSCS | Co-op analyst | AU packs | P10 |
| OI-P10-11 | ITA 2025 Form 26 clause list | New Act | Tax adviser | Pack OFF for TY 2026-27 | P10 |
| OI-P10-12 | TallyPrime edit-log evidence for Rule 11(g) | Vendor feature | Product | Manual checklist | P10 |
| OI-P10-13 | DSC need on regulator-submitted audit reports | Varies | CS | eSign default | P10 |
| OI-P10-14 | Infrabyx-linked PCS group-conflict rule | [REC] interpretation | General Counsel | Rule ON | P10 |
| OI-P11-01 | Owner's "28 Nov 2025" SR reference is an error (DoS SR = 31 Jul 2026) | Brief vs RBI record | Owner/CCO | errata.md | P11 |
| OI-P11-02 | SR numbers for PB, LAB, RRB, rural co-op banks, AIFIs | Not fetched | Reporting analyst | AU | P11 |
| OI-P11-03 | UCB SR rows 8–11, 20, 21 | Fetch truncated | Reporting analyst | AU | P11 |
| OI-P11-04 | CIMS web-form cap; S2S/ADF for NBFC/UCB | Sankalan help | Reporting analyst | File upload; S2S OFF | P11 |
| OI-P11-05 | NHB returns for HFCs | Not in SR | Reporting analyst | HFC pack OFF | P11 |
| OI-P11-06 | IFSCA, IRDAI, SEBI report formats/portals | Many circulars | Sector analysts | Calendar + evidence only | P11 |
| OI-P11-07 | ITA 2025 forms, sections, utility names | New Act | Tax adviser | Rule-pack data [VERIFY] | P11 |
| OI-P11-08 | AOC-4 NBFC (Ind AS) payload format | MCA V3 | CS | Data pack only | P11 |
| OI-P11-09 | MCA XBRL instance tooling | Licence/tool | CTO | Mapping workbook | P11 |
| OI-P11-10 | CIC member specs (encryption, validators) | Member agreements | Bureau ops | Public UCRF golden tests | P11 |
| OI-P11-11 | Co-op Registrar returns per State; MSCS s.120 | 28 States + CRCS | Co-op analyst | Tenant-defined returns | P11 |
| OI-P11-12 | PBC wording in 2025 consolidated Directions | Renumbering | Reporting analyst | 1999 press-release basis | P11 |
| OI-P11-13 | Insurer Ind AS; MF/AIF scheme framework | IRDAI/SEBI | CA | CFO override | P11 |
| OI-P11-14 | NSE/BSE XBRL utility licensing | Exchange terms | CS | Mapping workbook | P11 |
| OI-P11-15 | LDC sending CIR 34(1)(i) borrower alerts | TRAI/consent/contract | Counsel | Lender's system sends | P11 |
| J-OI-01..10 | See Appendix J §J.13 | — | CFO/CS | As listed | App J |

### Open items — stream S6 (P12–P14, App T)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P12-01 | DPDP Rules G.S.R. number; exact Rule 3 notice elements; Rule 7(2) report elements; Rule 14 response period | Secondary sources only in this research | Content checker (privacy) | Seed from Architecture Part 3 map; mark [VERIFY]; clocks Governed | P12 |
| OI-P12-02 | Date on which IT Act s.43A and SPDI Rules cease (DPDP s.44(2)) | Depends on Act commencement notification | Content checker | `effective_to` unset until confirmed | P12 |
| OI-P12-03 | SEBI CSCRF circular number, category thresholds for each RE type, incident reporting timelines to SEBI | Not fully verified | Content checker (SEBI) | Pack `CYB-SEBI-CSCRF` status DRAFT until verified | P12 |
| OI-P12-04 | IRDAI ICS Guidelines 2023 — reporting timelines, audit frequency, log retention specifics | Secondary sources thin | Content checker (IRDAI) | Pack DRAFT | P12 |
| OI-P12-05 | IFSCA cyber circular number and paragraph references | Site blocked from automation shell earlier | Content checker (IFSCA) | Use owner's IFSCA folder copy | P12 |
| OI-P12-06 | Bank/UCB IT governance and IT outsourcing instruments after RBI's Nov 2025 consolidation | Consolidation may have renamed/re-issued | Content checker (RBI banks) | Pack per entity family DRAFT | P12 |
| OI-P12-07 | RBI DAKSH incident template fields | Template not public in research | CISO of pilot client | Structured DOCX + XLSX field sheet | P12 |
| OI-P12-08 | CERT-In current incident reporting form fields and Annex I list text | Re-verify against cert-in.org.in | Content checker | Seed from 2022 Directions | P12 |
| OI-P12-09 | CCPA regulation section numbers (§7021, §7026, risk-assessment content) | Final text numbering post Sep 2025 | Content checker (US) | Pack DRAFT, flag `dpc.law.ccpa.enabled` OFF by default | P12 |
| OI-P12-10 | Restricted countries under DPDP s.16 | None notified as of research date | Content checker | Empty Governed list | P12 |
| OI-P12-11 | KYB/financial-health data vendor for vendor master | Commercial choice | CTO | Manual entry | P12 |
| OI-P12-12 | Whether LDC should offer a DPB-registered Consent Manager via a separate group company | Strategic/legal | Board / CS | Not in v1.0 [REC: do not] | P12 |
| OI-P13-01 | State rules under the four Codes (most pending; old State rules continue) | Notifications in progress | Payroll Compliance Officer (content) | `state_rule_status` per State; obligations show "pending State rules" | P13 |
| OI-P13-02 | EPF wage ceiling ₹25,000 from 17 Sep 2026 and split-month method | Gazette text / EPFO guidance | Content | `SECONDARY_ONLY` with acknowledgement | P13 |
| OI-P13-03 | Bonus eligibility and calculation ceilings under CoW s.26 | Not notified | Content | `NOT_CONFIRMED` — bonus run blocked until resolved or opinion recorded | P13 |
| OI-P13-04 | ESIC contribution rates under CoSS | Notification check | Content | `SECONDARY_ONLY` | P13 |
| OI-P13-05 | Income-tax Rules 2026 form numbers (salary TDS statement, annual certificate) and due dates | Recent change | Tax content | `NOT_CONFIRMED` dates; files generated, due dates manual | P13 |
| OI-P13-06 | Prescribed wage-slip and unified register formats under Central Rules 2026 | Forms to be mapped | Content | Generic formats with all prescribed fields | P13 |
| OI-P13-07 | Remote-employee PT/LWF location rule | Legal opinion | CS / counsel | Tenant policy chooses work-location or establishment basis | P13 |
| OI-P13-08 | RBI current instrument for mandatory leave of staff in sensitive positions (banks/NBFCs) | Consolidation | RBI content | Tenant setting with [VERIFY] note | P13 |
| OI-P13-09 | Fit-and-proper declaration formats in consolidated RBI directions (NBFC, UCB, ARC) | Consolidation | RBI content | Generic F&P template | P13 |
| OI-P13-10 | Shram Suvidha / State portal return formats and any APIs | Portals evolving | CTO | File preparation only | P13 |
| OI-P13-11 | Whether Aadhaar last-4 is needed on any statutory form | Form review | Content | Not stored | P13 |
| OI-P13-12 | Board-report POSH disclosure list after Companies (Accounts) amendments | Verify current rule text | CS | Disclosure covers r.8(5)(x) + counts | P13 |
| OI-P14-01 | RB-IOS 2026 clause numbers, the 90-day reference point, complaint definitions, coverage of co-operative banks | Salient-feature summaries only | Content (RBI CEPD) | Ladder text generic + [VERIFY] | P14 |
| OI-P14-02 | Internal Ombudsman Directions 2026 for banks, CICs, PPI issuers — thresholds and timelines | Only NBFC text verified | Content | Bank ladder DRAFT | P14 |
| OI-P14-03 | NBFC RBC Directions 2025 grievance paragraphs (GRO display, 30-day rule) | Para numbers to map | Content | Cite instrument without para | P14 |
| OI-P14-04 | SCORES 2.0 circular number and Designated Body timelines; LODR Reg 13 timeline | Verify | Content (SEBI) | 21-day clock only | P14 |
| OI-P14-05 | IRDAI 56-day closure rule, Bima Bharosa data exchange format, intermediary timelines | Verify | Content (IRDAI) | Manual Bima Bharosa updates | P14 |
| OI-P14-06 | IFSCA grievance framework instrument | Not researched | Content (IFSCA) | Generic ladder | P14 |
| OI-P14-07 | Co-operative Ombudsman (MSCS s.85A) timelines and procedure rules | Verify | Content (co-op) | Generic co-op ladder | P14 |
| OI-P14-08 | RBI annual-report complaint disclosure format per entity type | Verify current circular | Content | MIS export with all common fields | P14 |
| OI-P14-09 | Whether receipt by an LSP/DSA/recovery agent starts the RE clock | Interpretation | Counsel | Start at earliest receipt (conservative) | P14 |
| OI-P14-10 | WhatsApp policy constraints for regulated communications | Vendor terms | CTO | Channel OFF by default | P14 |

### Open items — stream S7 (P15–P16, App G, S)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P15-01 | UCB Board of Management threshold under UCB Governance Directions 2025 | Not read | Content (CS) | Committee "recommended" | P15 |
| OI-P15-02 | IRDAI CG Regs 2024 committee/KMP lists | Not read in full | Content | INSURER committees STUB | P15 |
| OI-P15-03 | SEBI MF Regulations 2026 regulation numbers | New regime | Content | Instrument-level citations | P15 |
| OI-P15-04 | Small LLP thresholds; small-company G.S.R. number | Gazette not verified | Content | Detector disabled | P15 |
| OI-P15-05 | ARC Directions paragraph numbers | Web text, not PDF | Content | Instrument-level citations | P15 |
| OI-P15-06 | Final paras of Investment in AIF Directions as consolidated | Updated 5 Oct 2026 | Content | July 2025 numbering | P15 |
| OI-P15-07 | LODR timelines as amended 22 Jan 2026 | Consolidated text not fetched | Content | Event register [VERIFY] | P15 |
| OI-P15-08 | REIT/InvIT governance; SM REIT obligations | Not researched to regulation level | Content | Governance STUB | P15 |
| OI-P15-09 | SEBI CSCRF category thresholds | Clarifications | S6 | Declared attribute | P12/P15 |
| OI-P15-10 | Regulator register scraping terms | Terms of use | Legal | Upload-only | P15/P18 |
| OI-P15-11 | PFRDA content | Out of v1.0 | Product | Stub family | Later |
| OI-P15-12 | NBFC Internal Ombudsman Directions 2026 scope | Not supplied | Content | Conditional role | P14/P15 |
| OI-P16-01 | MSCS section numbers (board, reservations, CEA notice, officers, AEC) | 2023 text not re-read | Co-op counsel | Instrument-level citations | P16 |
| OI-P16-02 | CRCS orders (22 Jan 2024; July 2025) text | Secondary | Content | Advisory monitors | P16 |
| OI-P16-03 | Maharashtra values (audit class, XI-1A %, timelines, election classes) | Secondary | MH counsel | Governed [VERIFY] | P16 |
| OI-P16-04 | Nine STUB State packs | Not researched | Counsel at onboarding | Configurable clocks | P16 |
| OI-P16-05 | ITA 2025 successor of s.80P | Numbering | Tax (S5) | Generic label | P11/P16 |
| OI-P16-06 | Virtual general meetings legality | Per Act | Content | Flag OFF | P16 |
| OI-P16-07 | Voter-list formats of CEA/State authorities | Not obtained | Content | Generic XLSX/PDF | P16 |
| OI-P16-08 | National PACS ERP API | Not public | Integrations | Manual upload | P18 |
| OI-P16-09 | Udofin app-store position for non-RE lenders | Udofin open item | Udofin | Web/assisted | Udofin |
| OI-P16-10 | Rajendra N. Shah citation | Verify | Content | Case name only | P16 |
| OI-G-01 | 20 Appendix G rows in VERIFY status and SEC rows with paragraph-level [VERIFY] notes | See G.17 | Content | Advisory-only (rules.unverified_as_advisory) | All |

### Open items — stream S8 (P17–P19, App K–M)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P17-01 | Exact Claude model IDs, quotas and throughput on the Bedrock India geographic profile | Announced 29 Sep 2026; quotas per account | CTO | Use Haiku/Sonnet tiers available; provisioned throughput if needed | P17 |
| OI-P17-02 | Availability of Files API, Agent Skills, citations and batch on Bedrock vs first-party API | Feature parity varies by platform | AI lead | Implement citations via search-result blocks/own verifier; docx via own builder | P17 |
| OI-P17-03 | Jio enterprise LLM API (terms, residency, no-training, SLA) | No public developer API found on jio.com/business (25 Oct 2026) | CTO / Procurement | `ai.provider.jio.enabled = OFF` | P17 |
| OI-P17-04 | Bhashini API access terms for a private SaaS and data-retention position | Not verified | AI lead / DPO | Use Bedrock/Azure India routes | P17 |
| OI-P17-05 | Handwriting OCR quality for Devanagari and other Indic scripts per engine | Needs evaluation | AI lead | Mark low confidence; human type copy | P17 |
| OI-P17-06 | Speech-to-text diarisation quality for Hinglish board meetings | Needs evaluation | AI lead | Typed notes path | P17 |
| OI-P17-07 | Embedding model availability in ap-south-1 on Bedrock | Not verified | AI lead | Self-hosted embedding model in VPC | P17 |
| OI-P17-08 | Whether recording of Board meetings needs every director's consent under tenant policy and SS-1 | Interpretation | Company Secretary | Recording only with recorded consent (default) | P17 |
| OI-P17-09 | AI credit unit price and plan allowances | Commercial | CFO (P20) | Seed in Appendix N | P17 |
| OI-P17-10 | ISO/IEC 42001 certification timing | Strategy | CISO | Build controls now; no claim before certificate (NN-19) | P17 |
| OI-P17-11 | Audio overview TTS voices in Hindi with India residency | Vendor check | AI lead | Flag OFF | P17 |
| OI-P17-12 | Viktor feature parity claims (scheduled prompts, approvals) used only as benchmark | Competitor source | Product | Benchmark only | P17 |
| OI-P18-01 | Ecosystem Spec §9.3 still describes LDC as "Node, TypeScript, MongoDB" | Superseded by D-01 | Owner (contracts change process §14.2) | Raise proposal for Spec v1.2 | P18 |
| OI-P18-02 | Revenue catalogue and Razorpay ownership (Spec §6.27/OH8) vs LDC Pricing Catalogue (D-21, P20) | Cross-document conflict | Owner / P20 | Master note M-S8-02 | P18 |
| OI-P18-03 | Licensed company-data provider selection, data-display and storage rights | Commercial/legal | Procurement / counsel | Manual entry fallback | P18 |
| OI-P18-04 | PAN verification channel eligibility for LDC or its aggregator | Regulatory/vendor | Compliance | Name-only entry; verify later | P18 |
| OI-P18-05 | CICRA position on bureau pulls for onboarding | Counsel confirmation of FR-P18-33 | General Counsel | No pulls (default) | P18 |
| OI-P18-06 | TRAI number-series and DLT rules current text for automated calls to RE customers | Rules changed in 2025–26 | Telecom counsel | `int.voice.ai_agent.enabled = OFF`; tenant's own CPaaS | P18 |
| OI-P18-07 | JioCX API documentation and WhatsApp BSP status | No public developer portal found | Procurement | Alternate CPaaS | P18 |
| OI-P18-08 | WhatsApp INR billing migration deadline 31 Dec 2026 and BSP handling | Meta notice | Procurement | Do not activate WhatsApp until BSP confirms | P18 |
| OI-P18-09 | FinLegal Academy LMS platform and SSO/LTI/xAPI support | Unknown platform | LawDocs Trainings | Catalogue CSV + manual completion upload | P18 |
| OI-P18-10 | Microsoft 365 plan held by Infrabyx and typical client plans (transcripts, `Sites.Selected`, retention labels) | D-10 | Company Secretary / CTO | Capability matrix gates features | P18 |
| OI-P18-11 | JioMeet API availability for meeting creation | Not verified | CTO | Teams/Google Meet only | P18 |
| OI-P18-12 | Native APIs of Busy, Marg and other Indian accounting packages | Not verified | Integrations lead | File-export layouts | P18 |
| OI-P18-13 | Bhashini/ULCA use for SMS/notice translation in regional languages | Terms | AI lead | Human translation | P18 |
| OI-P18-14 | Public disclosure pages — which documents each sector must publish | Sector packs (P15) | Content team | Tenant chooses documents | P18 |
| OI-P19-01 | BSA 2023 s.63 certificate form text and who signs Part B for SaaS-held records | Counsel | General Counsel | Platform statement + tenant-signed Part A; Part B by tenant's expert | P19 |
| OI-P19-02 | Companies (Accounts) Rules r.3(5) current text on India back-up servers and daily back-up | Verify latest amendment | Company Secretary | Treat as India-only for books and returns | P19 |
| OI-P19-03 | Microsoft Graph property/evidence for SharePoint data location India | Vendor | CTO | Signed IT-head attestation | P19 |
| OI-P19-04 | Retention labels and immutability on client M365 plans | Plan-dependent | CTO | No write-once option for SharePoint | P19 |
| OI-P19-05 | Object-lock support on Indian S3-compatible providers | Vendor | CTO | No write-once option | P19 |
| OI-P19-06 | RBI outsourcing directions — exit/termination and data return paragraphs for SaaS GRC providers | Counsel mapping | Compliance | Exit workflow as specified | P19 |
| OI-P19-07 | Statutory retention periods per record class (minutes permanent; registers; KYC; HR records under Labour Codes; tax) | Each module/P12 | Module owners | Longest-known retention applied to write-once | P19 |
| OI-P19-08 | Hindi README translation quality | AI/translation | Content team | English only | P19 |
| OI-P19-09 | Physical media exit handling via agent for > 2 TB | Operational | Delivery lead | Multi-part download / SFTP | P19 |

Appendix-level open items: OI-K-01…05 (Appendix K §K.13), OI-L-01…06 (Appendix L §L.10), OI-M-01…04 (Appendix M §M.17).

### Open items — stream S9 (P20–P22, App N, O, X)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P20-01 | OH8 live at P20 ship? approve LOCAL adapter + LDC Razorpay account | OH build timing | Owner/CTO | `bil.billing_port.mode = OH8` | P20 |
| OI-P20-02 | Production-grade trials (deviation from OH8.9) | OH acceptance | Owner/OH | Sandbox trial | P20 |
| OI-P20-03 | Click-wrap adequacy for RBI REs | RE contract norms | Counsel | eSign MSA path | P20 |
| OI-P20-04 | SAC/GST/IFSC/TDS form numbers (ITA 2025) | Tax review | CA | OH8 computes | P20 |
| OI-P20-05 | E-Commerce Rules 2026 applicability to B2B pricing | Consumer definition | Counsel | Adopt as policy | P20 |
| OI-P20-06 | Seed prices | Owner decision | Owner/CFO | Publish blocked | P20 |
| OI-P20-07 | Time-and-motion baselines | Not measured | Owner/CS | Estimated tiles hidden | P20 |
| OI-P20-08 | Razorpay plan change on domestic-card subscriptions | Vendor constraint | OH8 | Invoice + recreate | P20 |
| OI-P20-09 | e-mandate limits Oct 2026 | Rule change | OH8 | OH8.7 values | P20 |
| OI-P20-10 | Rename "Nidhi AI Assistant" → Vidhi AI on live site | Brand | Marketing | Appendix P copy | P20 |
| OI-P21-01 | Academy name and LMS API | Brand/tech | Owner | Setting + CSV feed | P21 |
| OI-P21-02 | Advocates in marketplace (Sulekha SLP pending) | SC pending | Counsel | Directory OFF | P21 |
| OI-P21-03 | ICAI aggregator position 2026 | Re-check | Counsel/CA | CA OFF | P21 |
| OI-P21-04 | ICSI/ICMAI positions | Not verified | Counsel | OFF | P21 |
| OI-P21-05 | M3 Route: ECO/TCS/PA terms | Tax/legal | Tax counsel | M3 OFF | P21 |
| OI-P21-06 | Selling entity for LawDocs services | Corporate | CS | Block M1 go-live | P21 |
| OI-P21-07 | Individual course checkout owner | Commercial | Owner | Academy checkout | P21 |
| OI-P21-08 | Legal documentation services by a company vs practice of law | Advocates Act; A.K. Balaji | Counsel | ADV class limits | P21 |
| OI-P21-09 | RBI NBFC outsourcing/IA paras for guard-rails | Re-check | S5/S7 | Generic notice | P21 |
| OI-P21-10 | CB referral commissions vs impartiality | ISO 17021-1/AICPA | Counsel | No referral fees | P21 |
| OI-P21-11 | E-Commerce Rules to B2B services marketplace | Consumer definition | Counsel | Adopt duties | P21 |
| OI-P21-12 | Deemed acceptance/refund/SLA credit values | Commercial | Owner | Defaults | P21 |
| OI-P22-01 | RBI/CIC/FIU portal terms on credential sharing | Not verified | Counsel | Client-only + ack | P22 |
| OI-P22-02 | Group IdP/SCIM source | OH/M365 | CTO | Manual provisioning | P22 |
| OI-P22-03 | Managed-device enforcement availability | M365 SKU | CTO | Risk-based step-up | P22 |
| OI-P22-04 | E-mail bridge domain/DMARC | Infra | CTO | In-app only | P22 |
| OI-P22-05 | Employed professionals signing deliverables | Professional rules | Counsel | Company work product | P22 |
| OI-P22-06 | Outsourcing-register auto-entry content | P12 alignment | S6 | Manual prompt | P22 |
| OI-X-01…07 | OH addendum decisions (entities, trials, checker role, LOCAL migration, provider partition, CPE, M365 SKU) | See Appendix X §X.14 | Owner/OH | See X.14 | P20–P22 |

### Open items — stream S10 (P23, App P, R)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P23-01 | Draft RPwD (Amendment) Rules 2026 (S.O. 3962(E)) final notification, ACR format and deadlines | Draft as of 25 Oct 2026 | DPO / CTO | Build ACR now (VPAT + IS 17802 map); track as obligation in `LDC_GROUP` | P23 |
| OI-P23-02 | SEBI digital-accessibility circular 31 Jul 2025 / 29 Aug 2025 exact number, paras and current deadlines | Taken from secondary source | Content team | Pack content marked [VERIFY]; dates not shown publicly until verified | P23 |
| OI-P23-03 | IS 17802 Part 1 clause-to-WCAG 2.2 mapping (IS 17802 tracks WCAG 2.1/EN 301 549) | Standard text purchase/review needed | Accessibility specialist | Treat WCAG 2.2 AA as superset; record IS 17802 clauses as [VERIFY] in ACR | P23 |
| OI-P23-04 | Company-data provider terms for lead-flow lookups and PAN verification in an anonymous flow | Vendor contract | CTO / counsel | `web.hc.lookup.enabled` OFF → manual entry only | P23 |
| OI-P23-05 | CCPA applicability to LDC (thresholds) and GDPR Art. 27 representative need for EU visitors | Depends on volumes and targeting | DPO / counsel | Serve GDPR/CCPA-style notices to self-declared EU/UK/US visitors; no EU targeting campaigns until decided | P23 |
| OI-P23-06 | CCPA (India) Dark Patterns Guidelines 2023 — any 2025–26 amendments/advisories (self-audit) | Re-check source | Counsel | Apply 13-pattern checklist | P23 |
| OI-P23-07 | BCI r.36 website content, ICAI/ICSI rules on member bios and articles | Counsel opinion | General counsel | `web.authors.advocate_bio_mode` Locked to Rule-36 fields | P23 |
| OI-P23-08 | Owner decision on AI training crawlers (`GPTBot`, `Google-Extended`, `CCBot`) | Business choice | Owner | Default ALLOW_PUBLIC_MARKETING | P23 |
| OI-P23-09 | Current lawdocscomply.com page content and pricing (site not readable without JS on 25 Oct 2026) | Fetch returned SPA shell | Owner / growth squad | Export current copy from the existing repo in P00; preserve slugs | P23 |
| OI-P23-10 | Company identity particulars for footer/legal pages (legal entity operating LDC, CIN, GSTIN, registered office, DPO, grievance officer) | Not provided | Company Secretary | Placeholders block publishing of legal pages | P23 |
| OI-P23-11 | ISL interpreter sourcing and cost for priority videos | Vendor | Content lead | Captions + transcripts mandatory; ISL for 12 videos as target | P23 |
| OI-P23-12 | IAAP-certified auditor engagement | Vendor | CTO | Internal audit by in-house specialist; external before ACR v1.0 publication | P23 |
| OI-P23-13 | Whether first-party cookieless analytics can run before consent under DPDP Rules 2025 | Interpretation | DPO | Default: no analytics identifiers before consent | P23 |
| OI-P23-14 | Grievance Officer obligation for LDC under IT Rules 2021 (is LDC an intermediary for user content?) | Interpretation | Counsel | Publish a grievance officer page anyway (also needed under DPDP and consumer law) | P23 |
| OI-P23-15 | Penalty library values used in health-check "why it matters" texts | Each must be cited and current | Regulatory reviewer | Show citation only (no amount) where unverified | P23 |

## W.5 Open items added in v1.1

#### Open items — v1.1 G1 (P25, App Y)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P25-01 | Model availability per planned cell region | Regional availability changes | CTO | ai.route.<cell> OFF | P25 |
| OI-P25-02 | Saudi PDPL Implementing Regulation amendments (consultation 6 Oct–5 Nov 2026) | Draft localisation and registration duties | DPO / counsel | Non-personal Tier C only | P25 |
| OI-P25-03 | UAE PDPL Executive Regulations | Unpublished (secondary source, Feb 2026) | DPO | Contractual safeguards | P25 |
| OI-P25-04 | Companies House API commercial terms | Licence | Product | Manual extract upload | P25 |
| OI-P25-05 | US CTA BOI scope after FinCEN 2025 rule | Rule change | Content | Advisory-only | P25 |
| OI-P25-06 | Partner commercial models per country | Professional rules | Counsel | Switches OFF | P25 |
| OI-P25-07 | Cross-border tax treatments | Adviser confirmation | CFO / tax adviser | Restrict selling currencies | P25 |
| OI-P25-08 | ODI/FDI form names and dates in India link | FEMA/RBI updates | CS | Configurable labels | P25 |
| OI-P25-09 | Licensed intelligence provider choice | Commercial | Owner | Official feeds only | P25 |
| OI-P25-10 | Local e-signature legal effect | Legal | Counsel | Partner-managed signing | P25 |
| OI-P25-11 | Spec v1.2: prefixed obligation_ref, LegalEntityChanged | Contract change | Integration lead | Internal only | P25 |
| OI-P25-12 | Moon-sighting holiday dates | Late announcement | Content partners | Provisional + confirm task | P25 |
| OI-Y-01 | Lawrbit coverage counts inconsistent across its documents | Vendor claims | Product | Do not quote counts in comparisons (NN-19) | App Y |
| OI-Y-02 | Lawrbit partners page unavailable 25 Oct 2026 | Site error | Product | Re-check before sales use | App Y |
| OI-Y-03 | GCC working-week patterns and Saudi weekend | Changes | Content partners | Pack data | App Y |
| OI-Y-04 | India adequacy under GDPR (none expected) and DOJ bulk-data rule country list | Legal changes | DPO | Watchers | App Y |

#### Open items — v1.1 G3 (P17, App AA, K)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-AA-01 | FREE-AI recommendation numbering and final list | Secondary sources differ | Content lead | [VERIFY] blocks publish | P12/P03 |
| OI-AA-02 | RBI Model Risk Management guidance — final issue | Draft Jun 2026 | Content lead | Suggestive Compliance | P12 |
| OI-AA-03 | SEBI AI/ML final circular | Consultation Jun 2025 | Content lead | Suggestive | P12 |
| OI-AA-04 | EU AI Act Digital Omnibus OJ publication | Political agreement 6 May 2026 | Global content | Flag dates | P12/P25 |
| OI-AA-05 | MCP conformance suite and registry listing | Ecosystem maturity | AI platform lead | Internal tests | P18 |
| OI-AA-06 | A2A in Ecosystem Spec v1.2 | Change request | Ecosystem owner | int.a2a.enabled OFF | P18 |
| OI-AA-07 | Open-weight model fitness for sovereign route | Evaluation | AI lead | Route OFF | P17 |
| OI-AA-08 | Keycloak RFC 8693 actor-claim support | Version-dependent | Identity engineer | Custom extension | P01/P17 |
| OI-AA-09 | Vendor admission rules for remote MCP servers (Copilot Studio, Claude, ChatGPT) | Vendor policies | Partnerships | Server OFF by default | P18 |
| OI-AA-10 | New roles ten_model_validator and KMP sub-type AIO | Role catalogue | Lead / Appendix D | Map to CRO / ten_checker | P01/P12 |
| OI-AA-11 | Provenance standard for generated media | Standards choice | AI lead | Visible label | P17 |
| OI-P17-17 | IT Amendment Rules 2026 labelling applicability to LDC | Interpretation | Counsel | Good practice | P17 |

#### Open items — v1.1 F1 (P00–P02, P24, App A, B, D, Q, U)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P00-11 | Foreign cell regions, DR pairs, hosting contracts | Opened on demand (D-42) | CTO / owner | Modules defined, not deployed | P00 |
| OI-P00-12 | Global control plane in IN for foreign tenants' routing metadata | GDPR Art. 44 reading for contact data | Counsel | Directory holds no customer personal data | P00 |
| OI-P01-12 | Which foreign cells first and hosting partners | Demand + legal review (App Y) | Owner / CTO | Only IN sold | P01 |
| OI-P01-13 | Practitioner workspace professional-conduct check | ICSI/ICAI rules | Counsel | `iam.practitioner.enabled` OFF | P01 |
| OI-P01-14 | Tracker-import auto-map threshold calibration | Pilot data | Product | 0.85; all proposals reviewable | P01 |
| OI-P02-08 | L3-eligibility gate per agent and promotion evidence threshold | Eval data needed | AIO / owner | All agents ≤ L2; tenant ceiling L1 | P02 |
| OI-P02-09 | Plan limits for custom registers and sandboxes | Commercial | Owner | 5 / 20 / unlimited (seed) | P02 |
| OI-P24-11 | ISO/IEC 42001 certification body and timing | After ISO 27001 | Owner / CISO | Readiness artefacts only | P24 |
| OI-P24-12 | Cell lag for regulatory-content-driven code fixes in foreign cells | Simultaneous fixes may be needed | CAB | Security override path | P24 |
| OI-Q-v11-01 | ISO/IEC 42001 Annex A control numbering for the SoA | Standard text to be checked | CISO | Map by control area | App Q |
| OI-Q-v11-02 | DPDP s.16 negative list, India adequacy status in EU, UAE PDPL Executive Regulations | Regulatory events | Counsel | Controls in §Q.18.2 apply conservatively | App Q |

#### Open items — v1.1 F2 (P03–P05, App E, F)

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-P03-09 | 318 catalogued RBI references are DERIVED (only NBFC Governance /344 read on the document) | Content checker (RBI) | Release gate V-22 / LDC-TPL-044 |
| OI-P03-10 | Press release counts 238; RBI/2025-26/100 counts 244 (240 live) | Content lead | Catalogue all 244 serials; wording per App AB |
| OI-P03-11 | NBFC / CEPD Integrated Ombudsman direction reference /383 or /384 | Content checker | [VERIFY]; gate V-22 |
| OI-P03-12 | Which competitor export formats to certify first | Product owner | Generic TRACKER mapping |
| OI-P04-08 | Data sources for seed automated tests | Product owner / integrations | Tests ship OFF per tenant |
| OI-P04-09 | Default sampling parameters for compliance testing | CCO advisory panel | Defaults per P04 §4H |
| OI-P04-10 | Whether any regulator expects approval-date timeliness | Content lead | `cmp.timeliness.rule` |
| OI-P05-10 | Stability of RBI category-page ids (`did`) and layout | Content lead | Fingerprint → PARSER_BROKEN |
| OI-P05-11 | Licensed foreign regulatory-intelligence provider | Product owner | `REG_INTEL_PORT` OFF |
| OI-P05-12 | Publication of DPB decisions | Content lead | Add source when published |
| OI-P03-E14 | Owner sign-off that only the 320-row catalogue (28 Nov 2025 set + later) is uploaded; withdrawn circulars history-only | Owner | PLACEHOLDER; nothing published without sign-off |
| OI-P03-E15 | = OI-P03-09 (App E view) | Content maker | LDC-TPL-044 |
| OI-P03-E16 | = OI-P03-11 (App E view) | Content maker | [VERIFY] |
| OI-P03-E17 | Reviewer partners for INTL-GEN priority jurisdictions | Owner / P25 | INTL-GEN rows stay DRAFT |
| OI-P03-E18 | Final status of RBI MRM guidance 2026, SEBI AI/ML guidelines, EU AI Act Digital Omnibus | Content maker (AI-GOV) | Suggestive Compliance + [VERIFY] |
| OI-P03-E19 | Owner confirmation of the `_LDC_System` hidden sheet in register exports | Owner | Kept; patch-removable |
| OI-F-01 (new) | All foreign URLs in App F §F.12A marked [VERIFY] (CBUAE, SCA, DFSA/ADGM rulebook hosts, UAE Data Office, MAS RSS, FCA RSS, SEC paths) | P05 sprint 1 | Test-fetch; source stays inactive until verified |
| OI-F-02 (new) | URL of RBI/2025-26/100 and of the FREE-AI report page (SRC-RBI-53, SRC-AI-01) | Content lead | [VERIFY] |
| OI-F-03 (new) | Count of withdrawn circulars (≈ 9,445) | Content lead | Stated with [VERIFY] in App F §F.2 and P05 §1 |

#### Open items — v1.1 F3 (P06, P07, P10, P26, P27, App J)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P06-16 – OI-P06-22 | Securities clocks, dividend/TDS, IEPF forms, s.94 periods, AOC-4/MGT-7 periods, offline packs device mgmt, foreign subsidiary calendars | See P06 §14 | CS/tax/CTO/global | Advisory / OFF | P06 |
| OI-P07-12 – OI-P07-17 | Forms template feed, add-ins, DPDP consent text, KYC checklist alignment, quiz eval set, foreign model templates | See P07 §14 | Integration/CTO/DPO/content/AI/global | Manual / OFF | P07 |
| OI-P10-15 – OI-P10-21 | CMP 2026 paras, bank/UCB testing rules, CCM validation, edit-log formats, foreign audit calendars, evidence-request API, inspection table migration | See P10 §14 | RBI analyst/HIA/product/integration/tech lead | Tenant defaults / manual | P10 |
| OI-P26-01 – OI-P26-13 | Notice windows, limitation periods, Recovery Lite, e-Courts source, Reg 30 timeline, GST RCM/TDS on legal fees, Bar Council fee rules, retention, regulator compliance timelines, ecosystem events, VA-16, LEGAL_PRIVILEGED class, export folder | See P26 §14 | Legal/CTO/GC/tax/AI/security/P19 | Advisory / OFF | P26 |
| OI-P27-01 – OI-P27-12 | ESG-BRSR template, SEBI 2025 circular, Core attributes, CSR Rules values, RBI climate directions, CEA factors, exchange format, SSAE 3410/ISF, financed emissions event, VA-17, export folder, ISSB roadmap | See P27 §14 | Owner/analysts/AI/P19 | Advisory | P27 |
| J-OI-13 – J-OI-18 | SEBI ESG circular, SSAE 3410/ISF, ISSB roadmap, Omnibus I OJ, CSR Rules, Reg 30 litigation timeline | See Appendix J §J.13 | Analysts | Advisory | App J |

#### Open items — v1.1 F4 (P08, P09, P11, P28, App H, I)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P08-12 | FRM Directions 2026 EWS paragraph | Not re-fetched | Platform content (RBI) | Fraud EWS advisory | P08 |
| OI-P08-13 | Methodology translation tables | Risk SME review | CRO pilot | Manual confirmation | P08 |
| OI-P08-14 | FX reference rate source | Licensing | CFO / P25 | Manual rate | P08 |
| OI-P08-15 | International prudential taxonomy packs | Needs reviewed packs | P25 partners | TAX-INTL-CORP only | P08 |
| OI-P08-16 | CCM test catalogue per family | Connector availability | P04/P12 | Manual tests | P08 |
| OI-P08-17 | EWS threshold calibration | No history | CRO pilots | [REC] defaults | P08 |
| OI-P09-17 | Indian IRRBB standardised shocks for banks | Not verified | Platform content (RBI) | Voluntary scenarios | P09 |
| OI-P09-18 | NGFS parameters licence | Terms | Legal | Generic shock | P09 |
| OI-P09-19 | Sandbox performance on large books | Load test | Engineering | Segment aggregation | P09 |
| OI-P09-20 | Group consolidation rules (NBFC/CIC groups) | Legal definitions | Platform content | Informational view | P09 |
| OI-P09-21 | Foreign-subsidiary prudential packs | P25 dependency | P25 partners | IMPORTED_RESULT | P09 |
| OI-P09-22 | Calibration back-test thresholds | Methodology approval | CRO, validator | Proposals disabled | P09 |
| OI-P11-16 | PB /433, LAB /449, AIFI /458 reference numbers | Derived from serials | Platform content (RBI) | ACTIVE_UNVERIFIED | P11 |
| OI-P11-17 | RRB/RCB/CIC return sources (no DoS SR direction) | Derived from absence | Platform content (RBI) | RBI list rows only | P11 |
| OI-P11-18 | Hindi plain messages | D-30 | Content team | English only | P11 |
| OI-P11-19 | Consolidation assistance scope | Professional review | CA reviewer | Flag OFF | P11 |
| OI-P11-20 | OCR of portal acknowledgements | Formats vary | P17 | Manual entry | P11 |
| OI-P11-21 | Foreign-subsidiary filing packs | P25 dependency | P25 partners | Calendar only | P11 |
| OI-P28-01 | RBI inspection request topic list | Not fetched | Platform content (RBI) | Editable mapping, [VERIFY] | P28 |
| OI-P28-02 | Board compliance report items under RBI/DoS/2026-27/460 | Paras not fetched | Platform content (RBI) | Items labelled [VERIFY] | P28 |
| OI-P28-03 | Benchmarking methodology and consent | Approval and counsel | Product + counsel | Flag OFF | P28 |
| OI-P28-04 | OData feed performance | Load test | Engineering | Feeds OFF | P28 |
| OI-P28-05 | PPTX chart library licence | ADR | CTO | Images with alt text | P28 |
| OI-P28-06 | SCR-RPT-01/02 ownership from P04 to P28 (X-26) | Master update | Pack lead | P04 hosts home | P28 |
| OI-P28-07 | Seed MIS titles from baseline | Owner confirmation | Owner / CS | Editable | P28 |

#### Open items — v1.1 F5 (P12–P16, App G, S, T)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P12-13 | RBI model-risk guidance final; FREE-AI follow-ups | Draft/guidance | Content (RBI) | Advisory frameworks | P12 |
| OI-P12-14 | EU AI Act Annex III numbering and Omnibus dates in OJ | Political agreement only | Content (EU) | EU class advisory | P12 |
| OI-P12-15 | SEBI final AI/ML circular | Consultation | Content (SEBI) | Pack DRAFT | P12 |
| OI-P12-16 | DPDP rule numbers for Schedules; Rule 8(3) log retention | Secondary sources | Content (privacy) | Governed values, advisory | P12 |
| OI-P12-17 | IT Amendment Rules 2026 applicability to non-intermediary REs | Interpretation | Counsel | Optional template | P12 |
| OI-P12-18 | Repeal of 2023 bank IT Governance MD by DoS 2026 cyber directions; LAB/RRB coverage | Not read on document | Content (RBI banks) | Both listed, old SUPERSEDED-PENDING | P12 |
| OI-P12-19 | Adverse-media/sanctions connector | Commercial | CTO | Trigger OFF | P12 |
| OI-P13-13 | Apprenticeship portal, band, stipend | Not re-verified | Payroll Compliance Officer | Flag OFF | P13 |
| OI-P13-14 | Income-tax Act 2025 salary certificate form | Renumbered | Content (tax) | Generic label | P13 |
| OI-P13-15 | Labour penalty bands and compounding | Rules partly notified | Content (labour) | Hide unverified bands | P13 |
| OI-P14-11 | CEPD IO direction numbers /380–/385 | Derived serials | Content (RBI) | Title + date, [VERIFY] | P14 |
| OI-P14-12 | Social-media connector terms | Platform policies | CTO | Connector OFF | P14 |
| OI-P15-13 | Catalogue reference numbers (320 rows) | Derived serials | Content team | Publish gate on CONFIRMED | P15 |
| OI-P15-14 | Equivalence groups across regulators | Content effort | Content checker | UNION_ONLY | P15 |
| OI-P15-15 | AML_RE scope under PMLA notifications | Evolving | Counsel | Family DRAFT | P15 |
| OI-P15-16 | Udyam thresholds; MSMED payment-term interplay | Not re-verified | Content | Advisory | P15 |
| OI-P15-17 | SEZ/GIFT-SEZ obligations for IFSC units | Not researched | Content (IFSCA) | Overlay DRAFT | P15 |
| OI-P16-11 | Members' inspection rights per State | Varies | Co-op analyst | MSCS defaults [VERIFY] | P16 |
| OI-P16-12 | Rectification forms/timelines beyond MH and MSCS | Not researched | Co-op analyst | Generic format | P16 |
| OI-P16-13 | States accepting English filings | Varies | Co-op analyst | Bilingual output | P16 |
| OI-S-05 | MSCS/State sections for inspection, inquiry, surcharge, rectification | Not verified | Co-op analyst | Advisory | App S |
| OI-S-06 | Electronic meetings/e-voting per State | Counsel | Counsel | "Subject to State law" | App S |

#### Open items — v1.1 F6 (P18–P23, App C, L, M, N, O, P, X)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P18-21 | Court/tribunal data licences (e-Courts/NJDG, NCLT, DRT, e-Jagriti) | Terms and lawful API access to verify | CTO / counsel | `int.litigation_data.provider = MANUAL` | P18 |
| OI-P18-22 | MCP registry and assistant-marketplace listing processes | Ecosystems evolving | CTO | Unlisted; direct URL onboarding | P18 |
| OI-P18-23 | A2A as Ecosystem transport (Spec v1.2 CR) | Needs group approval | Owner | `int.a2a.enabled = OFF` | P18 |
| OI-P18-24 | Licensed regulatory-intelligence contracts and display rights | Commercial | Owner / content lead | Official feeds only | P18 |
| OI-P18-25 | Reference-rate sources' terms of use (FBIL, CBUAE, MAS) | Licence check | CTO | Manual rate entry with evidence | P18 |
| OI-P18-26 | Foreign registry data licences (Companies House, ACRA, OpenCorporates) | Licence check | CTO | Manual entry | P18 |
| OI-P18-27 | Partner role naming: lead names `prt_admin`, `prt_content_reviewer`, `prt_delivery_professional`, `prt_viewer` vs P25's `prt_content_author`, `prt_content_reviewer`, `prt_delivery_professional` | Cross-file reconciliation | Lead (Appendix D) | Lead names used here | P18 |
| OI-P19-21 | Inter-cell transfer mechanism and per-law transfer instruments (SCCs, UAE/DIFC, Singapore) | Counsel per cell | DPO / counsel | Cells other than IN disabled | P19 |
| OI-P19-22 | Escrow agent selection and release conditions | Commercial | Owner | Escrow OFF | P19 |
| OI-P19-23 | Migration downtime budget for large entities | Needs load test | CTO | Maintenance window agreed per case | P19 |
| OI-P20-21 | Foreign price books and cell surcharges | Owner pricing decision | Owner / CFO | Market selector shows India only | P20 |
| OI-P20-22 | Cross-border tax positions (export of services/LUT, EU/UK reverse charge, UAE/Saudi/Singapore registration) | Tax adviser | CFO | Foreign checkout OFF; Enterprise by quote | P20 |
| OI-P20-23 | Agent seat pricing and credit rates for missions/CCM | Needs cost data from P17 pilots | Owner / CTO | Agents billed only through credits | P20 |
| OI-P20-24 | Escrow agent and fees | Commercial | Owner | Escrow not sold | P20 |
| OI-P21-21 | Professional rules on fee sharing and referrals per foreign country (UAE, Singapore, UK, EU, US) | Counsel per country | General Counsel | All foreign switches OFF | P21 |
| OI-P21-22 | Corporate service provider licensing for resale abroad | Varies by country | Counsel | Model M2 only | P21 |
| OI-P21-23 | SEBI eligibility conditions for BRSR Core assurance providers | Verify current circular | Content lead | Assurance listings OFF | P21 |
| OI-P22-21 | Firm plan legal terms (data-processing chain client → firm → LDC) | Counsel | Owner | Firm plans OFF | P22 |
| OI-P22-22 | Follow-the-sun staffing and labour-law implications for remote staff abroad | HR/counsel | OH | India-only teams | P22 |
| OI-P23-21 | Arabic copy deck and RTL accessibility testing | Needs GCC cell and translator | Marketing | `web.locale.ar.enabled = OFF` | P23 |
| OI-P23-22 | Foreign registry look-up terms for anonymous lead flow | Provider terms | CTO | Manual entry | P23 |
| OI-P23-23 | Market-specific advertising and comparison-claim rules (UK ASA, EU UCPD, UAE) | Counsel | Marketing | India copy only abroad, no comparisons | P23 |

## W.6 Open items added in v1.2 *(v1.2)*

*(v1.2)* Compiled by the pack lead from the v1.2 editors' registers (T1 templates and Appendix E; T3 P04 list, RAG, conversations and accountability; T4 P03 CompID generation, P05, P23; T5 business-ID registry, P01 onboarding, P06, P08, P09, P18). Where a v1.2 entry amends an earlier code, the v1.2 entry prevails.

#### Cross-file resolutions at v1.2 integration

| Item | Resolution |
|---|---|
| Date order written two ways (P03 V-30 and LDC-TPL-075 vs Appendix E §A.7) | Issue ≤ Actionable Last Updated On ≤ Instrument Last Amended On ≤ today; never-amended instruments repeat the issue date (D-58, X-62); P03 and T4 register fixed |
| Two CompID registries drafted (P03 `IdService`, `core` §B.12) | One registry in `core`; P03 tables are views (X-63); `IdService` may run behind P03's internal API (OI-P03-16) |
| RISK template taxonomy `MDL`/`LGL`/`AIG` vs Appendix H | Appendix H codes bind; `MDL`→`MOD`, `LGL`→`CMP` aliases; `AIG` provisional (X-64; closes OI-E-V12-01 and OI-P08-18 except the AIG decision) |
| Screen IDs SCR-TPL-06–08 collided with §C.9 | Renumbered SCR-TPL-20–22 (P03, Appendix P, C §C.13); closes OI-P04-16 for screens; W-CMP-20–24 and LDC-CMP-200–219 / LDC-WF-200–201 checked free |
| `color.danger` chip contrast 4.04:1 | RAG chips use `rag.red` #B42318 on #FEE4E2 (5.45:1) (X-65); other uses of `color.danger` to be audited (OI-C-01 stays open) |
| Files still naming v1.0 templates, `_validation_report.md` or column letters | Paths updated to v2.0 / `_legacy_v1.0`; column letters in phases and appendices annotated with v2.0 machine keys (v1.0 letter kept in brackets; Appendix E §A.9 map) |
| `fam_short` and default AUTH for cross-authority families | Registered in Appendix E §A.8 table and Appendix B §B.12 (closes OI-E-V12-02) |
| RBI instrument short codes | 319 proposed codes in catalogue v1.2 column AF; RBI-SCB adds a bank-category letter; approval by content lead before first reservation (OI-P00-14) |

#### T1 — Open items (v1.2; Appendix E §A.16; for Appendix W)

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-E-V12-01 | Risk taxonomy `AIG` vs Appendix H (`MOD`, no `AIG`) — T2 X7 | Lead / T5 | `AIG` provisional in RISK Lists; `MDL` alias of `MOD` |
| OI-E-V12-02 | Register `fam_short` and default AUTH for cross-authority families (PRIV, CYBER, LAB, GST, AIGOV, BRSR; MEITY, CERTIN, MOLE, GST, SEBI) in Appendix B | T5 | Appendix E §A.8 table |
| OI-E-V12-03 | Threshold bands in extension lists (NBFC asset size, UCB deposit band, ARC NOF band, MCA thresholds) to be re-read against primary text | Content makers | Exact tests stay in Conditional Applicability with [VERIFY] |
| OI-E-V12-04 | Owner confirmation of the 53-department Function / Sub-function seed (Part-2 §10A map adopted for the nine base departments) | Owner | Tenant overlay relabel/extend |
| OI-E-V12-05 | Excel for the web may open outline groups expanded | P03 QA | Read Me explains outline buttons; print area limits print to list view |
| OI-E-V12-06 | PDF row ceiling (`tpl.export.pdf_max_rows` 5,000) performance test | P04 | Offer Excel above ceiling |
| OI-E-V12-07 | Header text of two extension columns: spec §5 reads "Form of Set-up (Company / Branch / LLP / Trust)" and "Indicator Class (Essential / Leadership / Core)"; templates use "Form of Set-up" and "Indicator Class (Essential / Leadership / Core)" to match the Part-2 commands | Lead | Change by patch rebuild if lead prefers spec text (one constant in `v12_contract.py`) |
| OI-E-V12-08 | Synthetic sample instrument short codes (GOV25, KYC25, SR26, CRM25, FRM26, OUTS25, RBC25, CYB26, CMPF26, IRACP25) are illustrative; the content lead fixes real codes in `cnt.inst_short_codes` (P03 FR-P03-102/113) | Content lead | Samples are labelled SYNTHETIC |

#### T3 — Open items (v1.2)

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P04-11 | Default RAG windows for "Immediately" and event-based items | Management instruction gave monthly/quarterly windows only | CCO advisory panel | Defaults per P04 FR-P04-230; tenant may widen |
| OI-P04-12 | Use of accountability reports in HR/disciplinary processes | Labour-law and employee-consent questions; tenant policy | Tenant HR / legal | Factual, access-restricted report; HR use only under P13 policy (NN-25) [VERIFY with counsel] |
| OI-P04-13 | Hindi and other Indian-language coverage of the NL filter | Model quality for mixed Hindi-English queries | AI lead (P17) | English and Hindi at launch; others behind a flag |
| OI-P04-14 | WhatsApp templates for Red alerts | BSP template approval; DLT for SMS | Product owner (P18) | In-app, e-mail and push only until approved |
| OI-P04-15 | Slip-prediction features and minimum history | Needs pilot data for calibration | Data science | Disabled < 3 months history; threshold 0.6 |
| OI-P04-16 | Screen IDs SCR-CMP-20–29, widget IDs W-CMP-20–24, error codes LDC-CMP-200–219 / LDC-WF-200–201 | May collide with v1.2 IDs chosen by other editors | Pack lead | Renumber at integration if needed |
| OI-C-01 | `color.danger` #C44536 on `color.danger.bg` #FEE2E2 is 4.04:1 (< 4.5:1) | Pre-existing token pair used for status chips | Design lead (App C owner) | RAG/overdue chips switched to `rag.red` #B42318 on #FEE4E2 (5.45:1) in §C.8.1A; other uses to be audited |

#### T4 — Open items (v1.2)

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P03-13 | Subject-abbreviation list for `<SUBJECT><YY>` short codes — **list in Appendix E §A.8; 319 RBI codes proposed in catalogue column AF**; content-lead approval pending | One list across 27 families needed | Content lead / T1 | Generator proposes; content lead approves before freeze (SCR-TPL-22) | P03 |
| OI-P03-14 | `fam_short` for long family codes (e.g. `SEBI-REIT-INVIT`) | Appendix B owns family registry | Pack lead / T5 | `SEBI-RINV` proposed | P03 |
| OI-P03-15 | Amended date for never-amended instruments — **adopted as D-58** (repeat the issue date); owner confirmation only (`02` §4 item 20) | Owner wants the date on every row | Owner | Repeat the issue date (read as "not amended") | P03 |
| OI-P03-16 | Hosting of `IdService` (P03 vs P00) | Also issues RiskID/GovID/HC-/LPH- IDs | Pack lead | In P03 behind internal API; movable without contract change | P03 |
| OI-P05-13 | Which regulator date is "Actionable Last Updated On" when notification, publication and effective dates differ | Owner instruction is per-question update date | Owner / content lead | Amending instrument's date; effective date in `applic_from` | P05 |
| OI-P05-14 | Golden set for `checker_points` / `audit_test` | Owner samples lack these columns | Content lead | Reviewer-rated specificity on 200 rows; optional per family | P05 |
| OI-P05-15 | P08/P09 library readiness for RiskID/GovID suggestions | Libraries built by T5 phases | Pack lead | Suggestions OFF until libraries publish | P05 |
| OI-P23-31 | Final CompIDs for health-check bindings | Only NBFC DoS sheets exist in draft | Content lead | `LPH-` placeholders (Appendix P §P.11) | P23 |
| OI-P23-32 | Separate in-app pulse-check set | Product choice | Product owner | Same set; `IN_APP` channel OFF | P23 |
| OI-P23-33 | A/B testing of a self-assessment vs dark-pattern rules | Counsel review | Counsel | Test wording, order and length only | P23 |
| OI-AP-P-01 | Proposed authority/family codes `LDC`/`GPC` (good-practice library), `MWCD` (POSH), `GST` as TAX-GST fam_short, `RBI-OTH-FEMA19` placement | Appendix B registry | T5 / content lead | Use as proposed until registry confirms; placeholders only, no CompIDs issued | Appendix P |

#### T5 — Open items (v1.2)

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P00-13 | Keep pattern-conforming legacy CompIDs canonical or make them aliases | Owner decision; continuity of clients' audit papers | Owner / Company Secretary | Keep conforming IDs canonical; others aliases |
| OI-P00-14 | Instrument short codes for the 238 RBI Directions of 28 Nov 2025 | Content work; codes freeze at first reservation | Company Secretary / content checker | Proposals held; no reservations until approved |
| OI-P00-15 | s.63 Bharatiya Sakshya Adhiniyam 2023 certificate format for history exports | Legal reading | Counsel | NN-09 certificate template |
| OI-P01-15 | Contracts with company-data providers (MCA master, directors, charges, group data) | No open MCA21 V3 API for third parties confirmed [VERIFY] | CTO / counsel | GLEIF + public registers + manual entry |
| OI-P01-16 | GSP contract (taxpayer search) and PAN verification provider | Licensing | CTO | Manual GSTIN/PAN entry |
| OI-P01-17 | Formats and cadence of RBI/SEBI/IRDAI/IFSCA/CRCS registers | Formats change | Content team | Manual classification with evidence |
| OI-P01-18 | GLEIF Level 2 coverage for Indian groups is limited | Data availability | Product | MCA holding data; manual group set-up |
| OI-P01-19 | EPFO/ESIC establishment lookups through providers | Provider terms, consent | Counsel | `onb.epfo_lookup.enabled = OFF` |
| OI-P18-28 | Stable URLs and formats of each official register file | Publishers change formats | Content ops | Parser versioning, HOLD, manual upload |
| OI-P18-29 | Storage and display rights of MCA-data, PAN and GST providers | Contracts not signed | CTO / counsel | Discovery on GLEIF and public registers only |
| OI-P18-30 | Ecosystem Spec registration of CloudEvents extensions `ldcbizid`, `ldcinstref` | Ecosystem change process | Integration lead | Send anyway (unknown extensions are ignored) |
| OI-P18-31 | GSP access for non-filing onboarding look-ups | GSP licence terms | Counsel | Aggregator taxpayer-search product |
| OI-P08-18 | RISK template taxonomy list (`MDL`, `LGL`, `AIG`) vs Appendix H L1 codes (`MOD`, legal within `CMP`, no AI L1) | Built in parallel | Pack lead / Appendix H owner | Importer maps MDL→MOD, LGL→CMP; AIG only after Appendix H adds it |
| OI-P08-19 | Seed RSKL library content | Content work | CRO adviser / content | Starter kits without library IDs |
| OI-P08-20 | Risk RAG vs appetite RAG on the Board risk view | Owner preference | Owner | Show both, labelled |
| OI-P09-23 | Mapping 62 library scenarios to library RiskIDs | Depends on RSKL library | CRO adviser / content | Map by L1/L2 code |
| OI-P06-23 | Authority code for Secretarial Standards in GOVL IDs (`ICSI` or `MCA`) | Naming decision before first GOVL | Company Secretary | `ICSI` |
| OI-P06-24 | SS-1 minutes-signing window and SS-2 timelines as rule-pack parameters | Paragraph wording to verify | Company Secretary | Amber (not Red) until verified |
| OI-P06-25 | REG GovID volume for large member registers / RTA feeds | Possible millions of IDs | Tech lead | One REG ID per bulk batch for RTA feeds |
