# Appendix W — Verification Log and Open Items

> Binding for every phase. Compiled by the pack lead on 25 October 2026. Every `[VERIFY]` marker in the pack and every open item below is a build flag: the dependent feature ships OFF (or advisory-only, NN-38) until the item is closed with evidence in `docs/compliance/verification-log.md`.

## W.1 Verification protocol

1. **Primary source first.** Re-check the fact on the regulator's or legislature's own site (Appendix F lists them); record URL, retrieval date, document hash and the exact paragraph.
2. **Classify the result:** `VERIFIED` (primary text read), `SECONDARY_ONLY` (only commentary found — feature stays advisory), `CHANGED` (fact differs — raise a content or rule-pack change), `NOT_CONFIRMED` (cannot be found — keep OFF).
3. **Close by data, not code:** most items are closed by a Governed change (rule pack, setting or content release, P02), never a code release (NN-34). Items needing code are raised as stories.
4. **Recheck triggers:** every closed item records what would reopen it (amendment, new circular, vendor contract change, annual review).
5. **Launch gates:** an item tagged as a launch gate in the phase file blocks the wave's P24 run until closed.

## W.2 `[VERIFY]` census (25 October 2026)

| File | Markers | File | Markers |
|---|---|---|---|
| A_Workflows_and_State_Machines | 4 | P01_Identity_Tenancy_Onboarding_and_Access | 11 |
| B_Data_Model_Events_and_Error_Codes | 2 | P02_Configuration_Studio_Rule_Engine_and_Settings | 8 |
| C_Information_Architecture_Screens_Menus_and_Dashboards | 1 | P03_Regulatory_Content_Library_Template_Registry_and_Excel_Import | 3 |
| D_Roles_Personas_and_Access_Control_Matrix | 2 | P04_Compliance_Workspace_Maker_Checker_Calendar_Tasks_Notifications | 4 |
| E_Excel_Template_Contract_Entity_Families_and_Importer | 22 | P05_Regulatory_Change_Management_and_AI_Question_Authoring | 6 |
| F_Regulatory_Source_Register_and_Monitoring_Catalogue | 64 | P06_Governance_Board_Committees_and_Company_Secretarial | 41 |
| G_Legal_and_Regulatory_Rules_Register | 62 | P07_Policy_Lifecycle_and_Document_Management_System | 8 |
| H_Risk_Taxonomy_Basel_ICAAP_Stress_Scenarios_and_Ratio_Library | 136 | P08_Enterprise_Risk_Management_and_CRO_Workspace | 27 |
| I_Regulatory_Returns_CIC_and_Tax_Return_Catalogue | 60 | P09_Risk_Assessment_Lab_ICAAP_Stress_Testing_Capital_and_Ratios | 46 |
| J_Accounting_Auditing_and_Secretarial_Standards_Map | 55 | P10_Audit_Management_Internal_RBIA_IS_Secretarial_Statutory | 55 |
| K_Vidhi_AI_Agent_Specification | 2 | P11_Return_Studio_Data_Preparation_and_Accounting_Bridge | 53 |
| L_Integration_Adapters_and_API_Catalogue | 19 | P12_Data_Protection_Cyber_Security_IT_Governance_and_TPRM | 33 |
| M_Export_Package_LDC-EXPORT-1.0_and_Folder_Taxonomy | 2 | P13_HRMS_People_and_Labour_Compliance_Suite | 26 |
| N_Pricing_Plans_Add-ons_Revenue_Streams_and_Savings_Model | 9 | P14_Grievance_Redressal_and_Customer_Support_Desk | 40 |
| O_Marketplace_Services_Catalogue_and_Professional_Rules | 16 | P15_Sector_Packs_and_Entity_Logic | 29 |
| P_Website_Copy_SEO_GEO_Tutorials_and_Video_Plan | 31 | P16_Cooperative_Society_Operations_Suite | 56 |
| Q_Security_Privacy_and_Certification_Readiness | 20 | P17_Vidhi_AI_Employee_Agents_and_Knowledge_Notebooks | 7 |
| R_Competitive_Research_and_Differentiation | 7 | P18_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform | 11 |
| S_Cooperative_Societies_Law_and_Operations | 50 | P19_Data_Preservation_Portability_and_BYO_Storage | 5 |
| T_HRMS_Labour_Codes_Registers_and_Payroll_Parameters | 27 | P20_Pricing_Plans_Subscriptions_Billing_Savings_and_Revenue_Streams | 10 |
| U_Configuration_Framework_and_Settings_Catalogue | 15 | P21_Marketplace_Retainers_and_FinLegal_Academy | 21 |
| V_Acceptance_Tests_and_UAT_Catalogue | 1 | P22_Service_Delivery_Console_and_Operations_Hub_Interface | 4 |
| X_Operations_Hub_Addendum_for_LawDocsComply | 3 | P23_Public_Website_Health_Check_Help_Centre_Tutorials_and_Accessibility | 20 |
| P00_Foundations_Repository_Discovery_and_Migration | 9 | P24_Engineering_Governance_Hardening_Certification_Readiness_and_GoLive | 12 |

Total: 1155 markers. The densest files (Appendices H, I, F, G, J, S and phases P16, P10, P11, P09) carry regulatory parameters, return codes and State co-operative rules; they are verified by the content team in the first sprint of the phase that uses them.

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
