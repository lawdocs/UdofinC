# LawDocs — Build Prompt Pack v1.0

**Prepared:** 25 October 2026 · **Owner:** Company Secretary, Infrabyx Group · **Product:** LawDocs (lawdocs.in, product code `LD`) — the Infrabyx group's India-first legal-work platform for individuals, families, startups, professionals and companies: draft, negotiate, stamp, sign, store, track and get expert help, on the web and on iOS and Android · **Companions:** Infrabyx Ecosystem Integration Specification v1.1, Infrabyx Operations Hub v1.0, LawDocsComply v1.2, Equator Resolution v3.1, Finbyx v1.5, Udofin v1.2
**Stack (locked, D-01):** Next.js 16 (`apps/public`, `apps/web`, `apps/delivery`, `apps/console`) · Expo React Native (`apps/mobile`) · NestJS 11 modular monolith · PostgreSQL with RLS (India: AWS Mumbai, DR Hyderabad) · Temporal · Redis · OpenSearch · S3 Object Lock · Keycloak · Cerbos · GoRules ZEN + CEL · Claude via Amazon Bedrock India · MCP server and client · Razorpay through the Operations Hub billing engine

---

## 1. What this pack is

A paste-ready, phase-by-phase build prompt for a coding agent (Claude Code or equivalent) to build LawDocs end to end — backend, web front end, website content and mobile apps — with clear integration boundaries to Finbyx, Udofin, Equator, LawDocsComply, the group Operations Hub and third-party systems.

**What it covers:** DigiLocker-style Legal Vault and DMS with selective sharing and bulk folder intake (P04); OCR, handwriting and WhatsApp-screenshot type copies and translation (P05); template library from the owner's ~330-document manual and free template drafting on every page, with AI-custom drafts behind a professional-review gate (P06); contract negotiation in track changes with deal-room messaging (P07); eStamp and Aadhaar eSign with an instrument-eligibility gate and court-ready evidence (P08); Vidhi AI and a 37-agent AI workforce for individuals, legal teams, KMPs and boards (P09); pleadings and notices (P10); Provakil-class litigation management (P11); trademark tracking (P12); a Company Legal Department OS with governance and HRMS through shared kernels (P13); Start a Business, Startup Desk, compliance services and tax for individuals, companies and LLPs (P14); a separately branded Consumer Help service for loan and insurance grievances, challans and vehicles (P15); the group services marketplace with retainers and FinLegal Academy courses (P16); plans, pricing page, billing, revenue-stream switches and a savings dashboard (P17); a Delivery Console where relationship managers act as makers for retained clients (P18); APIs, partner onboarding and ecosystem connectors (P19); export, BYO storage and change-proof data (P20); the public website, no-code blog and vlog, SEO/GEO, help centre, "i" glossary, tutorials and accessibility (P21); mobile apps (P22); and engineering governance, patch and change management, VAPT, audits and go-live (P23).

**How it was built:** four rounds of owner questions in plan mode (decisions D-01…D-13); six live-web research streams (competitors and LegalKart reverse engineering; consumer-help verticals; Indian legal baseline; Jio, agentic AI and autopilot growth; lawdocs.in and manuals inventory; pricing and data sources); 24 phases and 26 appendices written to the LawDocsComply v1.2 house standard; integration review (30 cross-file resolutions, ID and error collisions fixed, 63 state machines reconciled, 515 screens and 582 phase acceptance scenarios catalogued); an independent legal-accuracy review (36 corrections, Appendix W §W.9); and a second full error review (G1–G4: about 190 further corrections — `_review/G1…G4` logs); and a 581-row traceability audit of the brief, the ChatGPT prompt and the manuals (Appendix Z: 0 missing).

## 2. Files

Word counts are whitespace-separated words, rounded to the nearest 100.

| File | Contents | Words |
|---|---|---|
| `00_README.md` | This guide | — |
| `01_MASTER_PROMPT.md` | LAWDOCS — MASTER BUILD PROMPT (v1.0, 25 October 2026) | 12,200 |
| `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` | LAWDOCS — REQUIREMENTS MAP AND DECISION LOG (v1.0, 25 October 2026) | 5,700 |
| `phases/P00_Foundations_Repository_Discovery_and_Migration.md` | Foundations, Repository Discovery and Migration | 17,100 |
| `phases/P01_Identity_Onboarding_KYC_KYB_and_Consent.md` | Identity, Onboarding, KYC/KYB and Consent | 15,100 |
| `phases/P02_Tenancy_Org_Structure_User_Types_and_Maker_Checker.md` | Tenancy, Organisation Structure, User Types and Maker-Checker | 10,600 |
| `phases/P03_Configuration_Studio_Rule_Engine_and_Settings.md` | Configuration Studio, Rule Engine and Settings | 16,100 |
| `phases/P04_Legal_Vault_and_Document_Management_System.md` | Legal Vault and Document Management System | 13,700 |
| `phases/P05_Document_Intelligence_OCR_TypeCopy_and_Translation.md` | Document Intelligence: OCR, Handwriting/Screenshot Type Copy, Translation | 9,300 |
| `phases/P06_Template_Library_and_AI_Drafting_Studio.md` | Template Library and AI Drafting Studio | 11,900 |
| `phases/P07_Contract_Lifecycle_Negotiation_Redlines_and_Deal_Rooms.md` | Contract Lifecycle: Negotiation, Redlines, Deal Rooms, Messaging, Approvals | 10,500 |
| `phases/P08_eSign_eStamp_Execution_and_Evidence.md` | eSign, eStamp, Execution and Evidence | 13,500 |
| `phases/P09_Vidhi_AI_Employee_and_Agent_Workforce.md` | Vidhi AI Employee and Agent Workforce | 14,100 |
| `phases/P10_Pleadings_Notices_and_Court_Drafting_Studio.md` | Pleadings, Notices and Court Drafting Studio | 8,100 |
| `phases/P11_Litigation_and_Matter_Management.md` | Litigation and Matter Management | 15,100 |
| `phases/P12_IP_and_Trademark_Portfolio.md` | IP and Trademark Portfolio | 9,300 |
| `phases/P13_Company_Legal_Department_OS_Governance_and_HRMS.md` | Company Legal Department OS, Governance and HRMS | 14,100 |
| `phases/P14_Business_Services_Start_a_Business_Compliance_and_Tax.md` | Business Services: Start a Business, Compliance Services and Tax | 12,800 |
| `phases/P15_Consumer_Help_Grievances_Challans_and_Vehicles.md` | Consumer Help: Loan/Insurance Grievances, Challans and Vehicles | 10,100 |
| `phases/P16_Marketplace_Professional_Registry_Retainers_and_Academy.md` | Marketplace, Professional Registry, Retainers and FinLegal Academy | 14,900 |
| `phases/P17_Plans_Subscriptions_Billing_Revenue_Streams_and_Savings.md` | Plans, Subscriptions, Billing, GST, Revenue-Stream Switches and Savings Dashboard | 10,800 |
| `phases/P18_Delivery_Console_and_Operations_Hub_Interface.md` | Delivery Console and Operations Hub Interface | 14,600 |
| `phases/P19_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md` | Integration Gateway, Ecosystem Connectors and Developer Platform | 15,200 |
| `phases/P20_Data_Preservation_Portability_BYO_Storage_and_Migration_Safety.md` | Data Preservation, Portability, BYO Storage and Migration Safety | 10,400 |
| `phases/P21_Public_Website_CMS_SEO_GEO_Help_Centre_and_Accessibility.md` | Public Website, No-Code CMS (Blog/Vlog), SEO/GEO, Help Centre, Tutorials, "i" Glossary and Accessibility | 17,400 |
| `phases/P22_Mobile_Apps_and_Store_Release.md` | Mobile Apps (iOS/Android) and Store Release | 12,100 |
| `phases/P23_Engineering_Governance_Change_Patch_Hardening_Audit_and_GoLive.md` | Engineering Governance, Change/Patch Management, Hardening, VAPT/IS Audit, Certification Readiness and Go-Live | 11,600 |
| `appendices/A_Workflows_and_State_Machines.md` | Workflows and State Machines (binding) | 16,900 |
| `appendices/B_Data_Model_Events_and_Error_Codes.md` | Data Model, Events and Error Codes (binding) | 19,200 |
| `appendices/C_Information_Architecture_Screens_Menus_Dashboards_and_Click_Budgets.md` | Information Architecture, Screens, Menus, Dashboards and Click Budgets (binding) | 19,500 |
| `appendices/D_Roles_Personas_and_Access_Control_Matrix.md` | Roles, Personas and Access Control Matrix | 10,200 |
| `appendices/E_Template_Pleading_and_Service_Taxonomy.md` | Template, Pleading and Service Taxonomy | 17,900 |
| `appendices/F_Instrument_Eligibility_Matrix_eSign_Stamp_Registration.md` | Instrument Eligibility Matrix: eSign, Stamp and Registration | 10,800 |
| `appendices/G_Legal_and_Regulatory_Rules_Register.md` | Legal and Regulatory Rules Register | 22,200 |
| `appendices/H_Vidhi_AI_Agent_Specification_and_Prompt_Library.md` | Vidhi AI Agent Specification and Prompt Library | 10,700 |
| `appendices/I_Integration_Adapters_and_API_Catalogue.md` | Integration Adapters and API Catalogue | 9,200 |
| `appendices/J_Jio_Business_Services_and_Telecom_Rules.md` | Jio Business Services and Telecom Rules | 5,600 |
| `appendices/K_Export_Package_LD-EXPORT-1.0_and_Folder_Taxonomy.md` | Export Package `LD-EXPORT-1.0` and Folder Taxonomy | 8,000 |
| `appendices/L_Pricing_Plans_Revenue_Stream_Registry_and_Savings_Model.md` | Pricing, Plans, Revenue-Stream Registry and Savings Model | 13,600 |
| `appendices/M_Marketplace_Services_Catalogue_and_Professional_Rules.md` | Marketplace Services Catalogue and Professional Rules | 8,800 |
| `appendices/N_Website_Copy_System_SEO_GEO_Tutorials_and_Video_Plan.md` | Website Copy System, SEO/GEO, Tutorials and Video Plan | 11,200 |
| `appendices/O_Legal_Policies_Review_Ready_Drafts.md` | Legal Policies: Review-Ready Drafts | 22,800 |
| `appendices/P_Security_Privacy_and_Certification_Readiness.md` | Security, Privacy and Certification Readiness | 8,700 |
| `appendices/Q_Competitive_Research_and_Improvement_Backlog.md` | Competitive Research and Improvement Backlog | 9,200 |
| `appendices/R_Configuration_Framework_and_Settings_Catalogue.md` | Configuration Framework and Settings Catalogue | 22,900 |
| `appendices/S_Consumer_Help_Rules_and_Playbooks.md` | Consumer Help Rules and Playbooks | 9,800 |
| `appendices/T_Company_Legal_Department_OS_and_Finance_Company_Structure.md` | Company Legal Department OS and Finance Company Structure | 9,100 |
| `appendices/U_Accessibility_Specification.md` | Accessibility Specification | 5,700 |
| `appendices/V_Acceptance_Tests_and_UAT_Catalogue.md` | Acceptance Tests and UAT Catalogue (binding) | 16,700 |
| `appendices/W_Verification_Log_and_Open_Items.md` | Verification Log and Open Items | 20,300 |
| `appendices/X_Operations_Hub_and_LawDocsComply_Addenda.md` | Operations Hub and LawDocsComply Addenda | 7,600 |
| `appendices/Y_Ecosystem_Spec_v1.2_Change_Request_LawDocs.md` | Ecosystem Spec v1.2 Change Request (LawDocs) | 9,800 |
| `appendices/Z_Brief_Traceability_Matrix.md` | Brief Traceability Matrix | 20,900 |
| `content/LawDocs_Website_Content_v1.0.md` | LawDocs Website Content Deck v1.0 | 30,100 |
| **Total (pack Markdown, excluding `_research/`, `_review/`, `condensed/`)** | | **703,100** |

Also included: `_research/` (R1–R6 research notes with sources, the page-inventory CSV, authoring conventions and cross-file resolutions — about 82,000 words), `_review/` (review logs F1–F3, G1–G4 and lead logs), `condensed/` (Finbyx-style Master Prompt and Phase Runbook, `.md` and `.docx`), the consolidated Word copy `LawDocs_Build_Prompt_Pack_v1.0.docx`, and the website content deck as Word (`content/LawDocs_Website_Content_v1.0.docx`).

## 3. How to run the build

1. Create or open the LawDocs repository (the existing lawdocs.in code is inventoried and migrated in P00) and open Claude Code in it.
2. **Session 1 (P00):** commit `01_MASTER_PROMPT.md` as `docs/00-master-prompt.md`, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` as `docs/01-decision-log.md`, `phases/` and `appendices/` under `docs/`, the Ecosystem Integration Specification v1.1 unchanged as `docs/ecosystem/infrabyx-integration-spec.md`, and `_research/00_Authoring_Conventions.md` as `docs/reference/authoring-conventions.md`. Then type: *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P00_Foundations_Repository_Discovery_and_Migration.md in full, plus the appendices it names. Write docs/phases/P00-plan.md and stop for my approval."*
3. **Every later session:** use the session prompt for that phase in `condensed/LawDocs_Phase_Runbook_v1.0.md`. Approve each plan before code is written. Each phase stops at its exit gate (§13 of the phase file, plus master §15 Definition of Done).
4. **Order and waves (master §13):**
   - **Wave 1 — Vault & Sign GA:** P00 → P01 → P02 → P03 → P04 → P06 → P07 → P08, with P09 runtime, P17, P19 core, P20 core and P21 core; then P23.
   - **Wave 2 — Legal Ops for companies:** P05, P10, P11, P12, P13, P16, P18, P19 full, P20 full, P22, and the P09 workforce L0–L2 slice; then P23.
   - **Wave 3 — Services and Consumer Help:** P14, P15, P09 full workforce, P21 full content, P22 v2; then P23.
5. **Precedence on conflict:** master §18 (master → `02` → Appendix G → F → B → A → D → R → C → phase file → other appendices; the Ecosystem Spec prevails for cross-product contracts, changed only through Appendix Y).
6. **Unverified facts:** about 1,900 `[VERIFY]` markers remain by design (130 de-duplicated items in Appendix W §W.3). Any feature depending on one ships behind a flag that is OFF or advisory-only until the fact is checked against the primary source (NN-38).

**Indicative effort:** about 186 squad-sprints (two-week sprints, squads of 8). With six squads in parallel, Wave 1 GA in about 12 sprints (≈ 6 months), Wave 2 by about sprint 24, Wave 3 by about sprint 34.

## 4. Website content

`content/LawDocs_Website_Content_v1.0` (Markdown and Word) is ready-to-use copy: brand voice and messaging, 80+ one-liners in the owner's style, global blocks (including the "Draft free with Vidhi" and "Hire a professional" blocks on every document page), 15 fully written flagship pages (Home, Rent Agreement, Agreement to Sell, Vehicle Sale, NDA, Employment, Partnership Deed, Startup Desk and Founders' Agreement, Legal Notice, eSign & eStamp, Legal Vault, Case Tracker, Trademark, Marketplace & Retainers, Pricing), a 72-entry FAQ bank, testimonial formats marked as placeholders (genuine testimonials only, no photos), and Consumer Help starter copy. Appendix N and P21 carry the system to rewrite the remaining ≈ 600 pages from the manuals; Appendix E lists every page, its status and whether its source text was copied from third parties or cites repealed law. Appendix O holds review-ready drafts of the privacy notice, terms of use, eSign/eStamp terms, AI use policy, refund and subscription policy, marketplace and professional terms, cookie policy, grievance policy, acceptable use, retention schedule, accessibility statement, security page and Consumer Help terms.

## 5. Decisions needed from the owner (`02` §4)

| # | Decision | Blocks |
|---|---|---|
| 1 | Confirm the Microsoft 365 plan actually held ("Business Starter" is a Google Workspace edition name) | P18, P19 |
| 2 | Operating-entity particulars (CIN, GSTIN, registered office, DPO, Grievance and Nodal Officers) | P17, P21 |
| 3 | Consumer Help brand, domain and operating entity | P15, P21, P22 |
| 4 | Plan names, prices, trial, refund window, credit validity (seeds in Appendix L) | P17, P21 |
| 5 | Revenue-stream waves and kill-switch approvers | P17 |
| 6 | eSign/eStamp/KYC vendors and second ESP; later own-ASP decision | P01, P08 |
| 7 | Court-data vendors (two) and trademark data partner | P11, P12 |
| 8 | Approve Appendix E starter lists for six "upcoming" categories and commissioned pleadings | P06, P10 |
| 9 | Blog folder taxonomy and first 20 tutorial videos | P21 |
| 10 | AI-crawler policy; default AI autonomy ceilings and agent sponsors | P21, P09 |
| 11 | Whether one itemised confirmation of a bounded reminder series satisfies NN-13 (with counsel) | P03, P09 |
| 12 | System of record for legal matters when a tenant uses both LawDocs and LawDocsComply | P11, P13, P19 |
| 13 | Public phone number, support hours and SLAs | P18, P21 |
| 14 | App-store purchase mode and GST on store sales | P22 |
| 15 | ERI and GSP routes for tax-filing support | P14 |
| 16 | Marketplace professional panel structure | P16 |

**Counsel questions:** Appendix W §W.5 (52) — the most material are the marketplace structure under BCI Rule 36 after the Madras High Court judgment, CA/CS participation, the Consumer Help entity and fee model, eSign eligibility of agreements to sell, the hosted eSign hand-off for group products, Aadhaar offline verification, DigiLocker retained copies, DPDP roles, and the AI-draft review gate. **Tax memo:** Appendix W §W.6 (17).

**Companion change requests:** Ecosystem Spec v1.2 (Appendix Y), Operations Hub v1.1, LawDocsComply v1.3, Equator v3.2, Finbyx and Udofin notes (master §19, Appendix X).

## 6. Requirement coverage

All 92 brief requirements (R-001…R-092) map to phases and appendices (`02` §8). Appendix Z traces 581 atomic asks: owner brief 340 covered, 57 changed by a recorded decision or challenge, 1 partial (a Jio developer-portal reading item); ChatGPT prompt 121 covered, 4 changed; manuals 49 covered, 9 awaiting owner approval of starter lists. Thirty-two challenges to the brief are recorded with lawful alternatives (`02` §3) — among them: no Aadhaar login, no CIBIL or CKYC pulls, no shared plaintext password tracker, no fees from advocates, no eSign for wills and powers of attorney, and no "replace your lawyer" claims.

## 7. Immediate actions independent of the build

- Make lawdocs.in server-rendered (today crawlers see empty pages), fix the non-www sitemap and the robots/sitemap conflict on `/buy/`, and keep or 301-redirect all 186 sitemap URLs (P00, P21).
- Remove unevidenced claims from the live site and manuals (for example "verified", "blockchain", "home delivery", "produced before any Court") and replace the testimonials adapted from other products (content deck §5.5; NN-20, NN-49).
- Start rewriting copied third-party sections and repealed-law references in the manuals (Appendix E, content deck §5).
- Begin vendor diligence for eSign aggregators (ASP structure, second ESP, CCA licence status), eStamp channels, court-data and MCA-data vendors (Appendix W §W.7).
- Request counsel opinions on the marketplace model and the Consumer Help entity before Wave 2 and Wave 3 respectively.
