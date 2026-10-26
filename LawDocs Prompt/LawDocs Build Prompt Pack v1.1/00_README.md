# LawDocs — Build Prompt Pack v1.1

**Prepared:** 26 October 2026 (v1.1; v1.0 issued 25 October 2026) · **Owner:** Company Secretary, Infrabyx Group · **Product:** LawDocs (lawdocs.in, product code `LD`) — the Infrabyx group's India-first legal-work platform for individuals, families, startups, professionals and companies: draft, negotiate, stamp, sign, store, track and get expert help, on the web and on iOS and Android · **Companions:** *(v1.1)* **Infrabyx Platform Baseline Standard (IPB) v1.0**, Infrabyx Ecosystem Integration Specification v1.2, Infrabyx Operations Hub v1.1, LawDocsComply v1.3, Equator Resolution v3.2, Finbyx v1.6, Udofin v1.3
**Stack (locked, D-01; IPB v1.0 applies — master §5):** Node.js **24.22.1** · Next.js 16 (`apps/public`, `apps/web`, `apps/delivery`, `apps/console`) · Expo React Native (`apps/mobile`) · NestJS 11 modular monolith · PostgreSQL (only engine) with RLS (reference production AWS Mumbai, DR Hyderabad; portable through IPB-01 ports, Docker/Helm/Terraform per cloud) · Temporal · Redis · OpenSearch · S3 Object Lock · Keycloak · Cerbos · GoRules ZEN + CEL · Vidhi AI on the shared kernel `packages/vidhi` with Claude via Amazon Bedrock India as reference and OpenAI/Azure, Gemini, Grok, Sarvam/Bhashini adapters · MCP server and client · Razorpay through the Operations Hub billing engine

> **What changed in v1.1 (26 October 2026 — IPB adoption).** *(v1.1)*
> 1. IPB v1.0 adopted in full: adoption clause and ports table in master §5 and new §21; precedence master → IPB → Ecosystem Spec v1.2 → `02` → appendices (§18).
> 2. Node.js 24.22.1 pinned (closes the v1.0 runtime [VERIFY]); PostgreSQL the only engine; every vendor behind a port with ≥ 2 adapters; AWS Mumbai becomes the reference, not the only, production (P20 FR-P20-52…55 portability drills).
> 3. AI gateway adapters named (Anthropic, Bedrock India, Azure OpenAI/OpenAI, Gemini, Grok, Sarvam/Bhashini, self-hosted); `IMAGE_GEN` port with mandatory AI label and human review; D-14 kept.
> 4. Vidhi on the shared kernel: skill manifests, RRULE schedules with run-time permission re-check, evidence-based promotion, notebook outputs, MCP rules (P09 §4N; Appendix H §H.15).
> 5. Website: Investors page (toggle OFF, [COUNSEL]), Resources library, blog toggle, guest posts (toggle OFF), footer social links and Delhi/Noida/Jaipur offices, `brand.app_name`, tag-manager option, feedback widget and idea board (P21 §4R–§4S).
> 6. Policies: Payment and Subscription Terms, Blog and UGC Terms, Resources Download Terms, Vendor Assurance Statement, Investors disclaimer (Appendix O §O.17, POL-LD-18…22).
> 7. Vendor Assurance Room mirror under Settings › Security & trust; Trust Centre renders from it (P23 FR-P23-60…62; P21 FR-P21-150).
> 8. Settings tree mapped to the IPB-07 twenty nodes (Appendix C §C.4.17A; P03 §4P) with Security sub-items (password/MFA policy, sessions, IP allow-list, BYOK, audit log).
> 9. "i" registry confirmed `hlp.<module>.<term>` with CI lint and regulatory-reference panel; Cmd+K PII refusal (FR-P03-36A).
> 10. Engineering: `cc/<phase>-<slug>` branches, tenant beta programme, release-notes pipeline (P23).
> 11. APIs and events: IPB-10 conventions; Appendix Y and the ten IPB-10 events now registered in Spec v1.2; `CALENDAR_PORT` (P19).
> 12. New files: `env/.env.example`, `env/SEED_CREDENTIALS.md`, `env/README.md`, `design/UI_UX_Design_Brief_v1.1.md`, `content/LawDocs_Website_Content_v1.1.md`, `condensed/v1.1_Session_Prompt_Addendum.md`, `_review/v1.1_upgrade_review_log.md`.
> 13. Decision log: D-18…D-29 (= IPB-D-01…12), IPB-DEV-01…03, pending decisions 21–25; open items OI-IPB-01…12 (Appendix W §W.4.7).
> 14. Appendix B registers the new error codes (WEB 041–050, 094–095; HLP 021–025; ENG 012, 030–032); Appendix R registers the new keys (§R.9.16A, §R.9.35A, §R.9.39A).
> 15. Nothing verified in v1.0 was removed; superseded lines carry *(v1.1)* and a reason. Pack Markdown total ≈ 770,000 words (was 703,100).

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
| `01_MASTER_PROMPT.md` | LAWDOCS — MASTER BUILD PROMPT (v1.1, 26 October 2026) | 15,400 |
| `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` | LAWDOCS — REQUIREMENTS MAP AND DECISION LOG (v1.1, 26 October 2026) | 6,800 |
| `phases/P00_Foundations_Repository_Discovery_and_Migration.md` | Foundations, Repository Discovery and Migration | 17,100 |
| `phases/P01_Identity_Onboarding_KYC_KYB_and_Consent.md` | Identity, Onboarding, KYC/KYB and Consent | 15,100 |
| `phases/P02_Tenancy_Org_Structure_User_Types_and_Maker_Checker.md` | Tenancy, Organisation Structure, User Types and Maker-Checker | 10,600 |
| `phases/P03_Configuration_Studio_Rule_Engine_and_Settings.md` | Configuration Studio, Rule Engine and Settings *(v1.1: IPB-07 tree, Security sub-items, brand pack, palette PII refusal)* | 17,800 |
| `phases/P04_Legal_Vault_and_Document_Management_System.md` | Legal Vault and Document Management System | 13,700 |
| `phases/P05_Document_Intelligence_OCR_TypeCopy_and_Translation.md` | Document Intelligence: OCR, Handwriting/Screenshot Type Copy, Translation | 9,300 |
| `phases/P06_Template_Library_and_AI_Drafting_Studio.md` | Template Library and AI Drafting Studio | 11,900 |
| `phases/P07_Contract_Lifecycle_Negotiation_Redlines_and_Deal_Rooms.md` | Contract Lifecycle: Negotiation, Redlines, Deal Rooms, Messaging, Approvals | 10,500 |
| `phases/P08_eSign_eStamp_Execution_and_Evidence.md` | eSign, eStamp, Execution and Evidence | 13,500 |
| `phases/P09_Vidhi_AI_Employee_and_Agent_Workforce.md` | Vidhi AI Employee and Agent Workforce *(v1.1: shared kernel §4N, adapters, image gen)* | 17,000 |
| `phases/P10_Pleadings_Notices_and_Court_Drafting_Studio.md` | Pleadings, Notices and Court Drafting Studio | 8,100 |
| `phases/P11_Litigation_and_Matter_Management.md` | Litigation and Matter Management | 15,100 |
| `phases/P12_IP_and_Trademark_Portfolio.md` | IP and Trademark Portfolio | 9,300 |
| `phases/P13_Company_Legal_Department_OS_Governance_and_HRMS.md` | Company Legal Department OS, Governance and HRMS | 14,100 |
| `phases/P14_Business_Services_Start_a_Business_Compliance_and_Tax.md` | Business Services: Start a Business, Compliance Services and Tax | 12,800 |
| `phases/P15_Consumer_Help_Grievances_Challans_and_Vehicles.md` | Consumer Help: Loan/Insurance Grievances, Challans and Vehicles | 10,100 |
| `phases/P16_Marketplace_Professional_Registry_Retainers_and_Academy.md` | Marketplace, Professional Registry, Retainers and FinLegal Academy | 14,900 |
| `phases/P17_Plans_Subscriptions_Billing_Revenue_Streams_and_Savings.md` | Plans, Subscriptions, Billing, GST, Revenue-Stream Switches and Savings Dashboard | 10,800 |
| `phases/P18_Delivery_Console_and_Operations_Hub_Interface.md` | Delivery Console and Operations Hub Interface | 14,600 |
| `phases/P19_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md` | Integration Gateway, Ecosystem Connectors and Developer Platform *(v1.1: IPB-10, connector manifest, CALENDAR_PORT, registered events)* | 16,200 |
| `phases/P20_Data_Preservation_Portability_BYO_Storage_and_Migration_Safety.md` | Data Preservation, Portability, BYO Storage and Migration Safety *(v1.1: cloud portability, drills)* | 11,200 |
| `phases/P21_Public_Website_CMS_SEO_GEO_Help_Centre_and_Accessibility.md` | Public Website, No-Code CMS (Blog/Vlog), SEO/GEO, Help Centre, Tutorials, "i" Glossary and Accessibility *(v1.1: IPB-04 pages, Investors, Resources, guest posts, footer, feedback)* | 22,100 |
| `phases/P22_Mobile_Apps_and_Store_Release.md` | Mobile Apps (iOS/Android) and Store Release | 12,100 |
| `phases/P23_Engineering_Governance_Change_Patch_Hardening_Audit_and_GoLive.md` | Engineering Governance, Change/Patch Management, Hardening, VAPT/IS Audit, Certification Readiness and Go-Live *(v1.1: cc/ branches, beta, release notes, Vendor Assurance mirror)* | 13,300 |
| `appendices/A_Workflows_and_State_Machines.md` | Workflows and State Machines (binding) | 16,900 |
| `appendices/B_Data_Model_Events_and_Error_Codes.md` | Data Model, Events and Error Codes (binding) *(v1.1: new codes registered)* | 19,400 |
| `appendices/C_Information_Architecture_Screens_Menus_Dashboards_and_Click_Budgets.md` | Information Architecture, Screens, Menus, Dashboards and Click Budgets (binding) *(v1.1: §C.4.17A settings-tree mapping, new screens)* | 20,500 |
| `appendices/D_Roles_Personas_and_Access_Control_Matrix.md` | Roles, Personas and Access Control Matrix | 10,200 |
| `appendices/E_Template_Pleading_and_Service_Taxonomy.md` | Template, Pleading and Service Taxonomy | 17,900 |
| `appendices/F_Instrument_Eligibility_Matrix_eSign_Stamp_Registration.md` | Instrument Eligibility Matrix: eSign, Stamp and Registration | 10,800 |
| `appendices/G_Legal_and_Regulatory_Rules_Register.md` | Legal and Regulatory Rules Register | 22,200 |
| `appendices/H_Vidhi_AI_Agent_Specification_and_Prompt_Library.md` | Vidhi AI Agent Specification and Prompt Library *(v1.1: §H.15 kernel mapping)* | 11,300 |
| `appendices/I_Integration_Adapters_and_API_Catalogue.md` | Integration Adapters and API Catalogue | 9,200 |
| `appendices/J_Jio_Business_Services_and_Telecom_Rules.md` | Jio Business Services and Telecom Rules | 5,600 |
| `appendices/K_Export_Package_LD-EXPORT-1.0_and_Folder_Taxonomy.md` | Export Package `LD-EXPORT-1.0` and Folder Taxonomy | 8,000 |
| `appendices/L_Pricing_Plans_Revenue_Stream_Registry_and_Savings_Model.md` | Pricing, Plans, Revenue-Stream Registry and Savings Model | 13,600 |
| `appendices/M_Marketplace_Services_Catalogue_and_Professional_Rules.md` | Marketplace Services Catalogue and Professional Rules | 8,800 |
| `appendices/N_Website_Copy_System_SEO_GEO_Tutorials_and_Video_Plan.md` | Website Copy System, SEO/GEO, Tutorials and Video Plan | 11,200 |
| `appendices/O_Legal_Policies_Review_Ready_Drafts.md` | Legal Policies: Review-Ready Drafts *(v1.1: §O.17 POL-LD-18…22)* | 25,400 |
| `appendices/P_Security_Privacy_and_Certification_Readiness.md` | Security, Privacy and Certification Readiness | 8,700 |
| `appendices/Q_Competitive_Research_and_Improvement_Backlog.md` | Competitive Research and Improvement Backlog | 9,200 |
| `appendices/R_Configuration_Framework_and_Settings_Catalogue.md` | Configuration Framework and Settings Catalogue *(v1.1: §R.9.16A, §R.9.35A, §R.9.39A)* | 24,700 |
| `appendices/S_Consumer_Help_Rules_and_Playbooks.md` | Consumer Help Rules and Playbooks | 9,800 |
| `appendices/T_Company_Legal_Department_OS_and_Finance_Company_Structure.md` | Company Legal Department OS and Finance Company Structure | 9,100 |
| `appendices/U_Accessibility_Specification.md` | Accessibility Specification *(v1.1: IPB-06 alignment note)* | 5,900 |
| `appendices/V_Acceptance_Tests_and_UAT_Catalogue.md` | Acceptance Tests and UAT Catalogue (binding) | 16,700 |
| `appendices/W_Verification_Log_and_Open_Items.md` | Verification Log and Open Items *(v1.1: §W.4.7 OI-IPB-01…12)* | 21,100 |
| `appendices/X_Operations_Hub_and_LawDocsComply_Addenda.md` | Operations Hub and LawDocsComply Addenda *(v1.1 note)* | 7,800 |
| `appendices/Y_Ecosystem_Spec_v1.2_Change_Request_LawDocs.md` | Ecosystem Spec v1.2 Change Request (LawDocs) *(v1.1: §Y.0 — absorbed into Spec v1.2)* | 10,000 |
| `appendices/Z_Brief_Traceability_Matrix.md` | Brief Traceability Matrix | 20,900 |
| `content/LawDocs_Website_Content_v1.0.md` | LawDocs Website Content Deck v1.0 (kept for reference; superseded by v1.1 for the new pages) | 30,100 |
| `content/LawDocs_Website_Content_v1.1.md` *(v1.1)* | LawDocs Website Content Deck v1.1 — Parts 1–7 = v1.0 unchanged; Part 8 adds IPB-04 standard pages, Investors, Resources, blog contributor programme, Trust Centre, footer v1.1, cookie banner v1.1, feedback microcopy, one-liners, FAQs, SEO table, image placeholders | 37,900 |
| `design/UI_UX_Design_Brief_v1.1.md` *(v1.1)* | UI/UX Design Brief — palette (deep navy `#0B2545` + saffron `#E07A1F`), Inter + Source Serif, tokens, dark mode, density, components, imagery placeholders, states, accessibility, sample screens, tenant overrides, do/don't | 3,300 |
| `env/.env.example` *(v1.1)* | Annotated environment template (217 variables; IPB-11 derived, LD-specific) | 2,600 |
| `env/SEED_CREDENTIALS.md` *(v1.1)* | Seed personas, roles, lead-issued passwords, service accounts, rotation log — **never commit to a repository** | 900 |
| `env/README.md` *(v1.1)* | How to use the env files; production refusal; rotation | 400 |
| **Total (pack Markdown, excluding `_research/`, `_review/`, `condensed/`)** | | **≈ 770,400** (v1.0: 703,100) |

Also included: `_research/` (R1–R6 research notes with sources, the page-inventory CSV, authoring conventions and cross-file resolutions — about 82,000 words), `_review/` (review logs F1–F3, G1–G4, lead logs and *(v1.1)* `v1.1_upgrade_review_log.md`), `condensed/` (Finbyx-style Master Prompt and Phase Runbook v1.0, `.md` and `.docx`, plus *(v1.1)* `v1.1_Session_Prompt_Addendum.md` with the updated P00 first-session prompt and the session prompts for P03, P09, P19, P20, P21 and P23 — the lead regenerates the full condensed v1.1 files and the Word copies), the consolidated Word copy `LawDocs_Build_Prompt_Pack_v1.1.docx` (to be regenerated by the lead from the v1.1 Markdown), and the website content deck as Word (`content/LawDocs_Website_Content_v1.0.docx`; v1.1 Word copy to be regenerated).

## 3. How to run the build

1. Create or open the LawDocs repository (the existing lawdocs.in code is inventoried and migrated in P00) and open Claude Code in it.
2. **Session 1 (P00):** commit `01_MASTER_PROMPT.md` as `docs/00-master-prompt.md`, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` as `docs/01-decision-log.md`, `phases/` and `appendices/` under `docs/`, **the IPB pack unchanged as `docs/ipb/` *(v1.1)***, the Ecosystem Integration Specification **v1.2** unchanged as `docs/ecosystem/infrabyx-integration-spec.md`, `_research/00_Authoring_Conventions.md` as `docs/reference/authoring-conventions.md`, and `env/.env.example` + `env/README.md` under `env/` (never `SEED_CREDENTIALS.md`). Then paste the P00 session prompt from `condensed/v1.1_Session_Prompt_Addendum.md` §1 — it begins *"Read docs/ipb/00_README.md in full, then IPB-01, IPB-02, IPB-09 and IPB-11 …"* and ends with the plan and the stop for approval.
3. **Every later session:** use the session prompt for that phase in `condensed/LawDocs_Phase_Runbook_v1.0.md`, replaced for P03, P09, P19, P20, P21 and P23 by the prompts in `condensed/v1.1_Session_Prompt_Addendum.md` *(v1.1)*; every prompt starts with "Read docs/ipb/00_README.md first". Work on `cc/<phase>-<slug>` branches (P23 FR-P23-03A). Approve each plan before code is written. Each phase stops at its exit gate (§13 of the phase file, plus master §15 Definition of Done).
4. **Order and waves (master §13):**
   - **Wave 1 — Vault & Sign GA:** P00 → P01 → P02 → P03 → P04 → P06 → P07 → P08, with P09 runtime, P17, P19 core, P20 core and P21 core; then P23.
   - **Wave 2 — Legal Ops for companies:** P05, P10, P11, P12, P13, P16, P18, P19 full, P20 full, P22, and the P09 workforce L0–L2 slice; then P23.
   - **Wave 3 — Services and Consumer Help:** P14, P15, P09 full workforce, P21 full content, P22 v2; then P23.
5. **Precedence on conflict** *(v1.1)*: master §18 (master → **IPB v1.0** → **Ecosystem Spec v1.2** (prevails for cross-product contracts; Appendix Y is now registered in it) → `02` → Appendix G → F → B → A → D → R → C → phase file → other appendices). A product may tighten an IPB rule, never loosen it; deviations are `IPB-DEV-nn` in `02` §2.4.
6. **Unverified facts:** about 1,900 `[VERIFY]` markers remain by design (*(v1.1)* the Node.js runtime item is closed by IPB-D-01; new v1.1 markers are listed in `_review/v1.1_upgrade_review_log.md` §5) (130 de-duplicated items in Appendix W §W.3). Any feature depending on one ships behind a flag that is OFF or advisory-only until the fact is checked against the primary source (NN-38).

**Indicative effort:** about 186 squad-sprints (two-week sprints, squads of 8). With six squads in parallel, Wave 1 GA in about 12 sprints (≈ 6 months), Wave 2 by about sprint 24, Wave 3 by about sprint 34.

## 4. Website content

*(v1.1)* `content/LawDocs_Website_Content_v1.1.md` is the binding deck: Parts 1–7 are v1.0 unchanged and Part 8 adds the IPB-04 standard pages (About, Team, Leadership, Governance, Investors — toggle, Careers, Press, Partners, Contact with Delhi/Noida/Jaipur offices, Documentation, Trust Centre from the Vendor Assurance Room, Help, Tutorials, Resources library, Blog landing and contributor programme, Changelog, Glossary, Sitemap, Compare and Case-study templates), footer v1.1 with social links, cookie banner v1.1, feedback-widget microcopy, 32 new one-liners, 14 new FAQs, SEO titles and descriptions and the image placeholder list. The design brief `design/UI_UX_Design_Brief_v1.1.md` governs look and feel (deep navy + saffron, Inter + Source Serif; trustworthy legal, warm, minimal).

`content/LawDocs_Website_Content_v1.0` (Markdown and Word) is ready-to-use copy: brand voice and messaging, 80+ one-liners in the owner's style, global blocks (including the "Draft free with Vidhi" and "Hire a professional" blocks on every document page), 15 fully written flagship pages (Home, Rent Agreement, Agreement to Sell, Vehicle Sale, NDA, Employment, Partnership Deed, Startup Desk and Founders' Agreement, Legal Notice, eSign & eStamp, Legal Vault, Case Tracker, Trademark, Marketplace & Retainers, Pricing), a 72-entry FAQ bank, testimonial formats marked as placeholders (genuine testimonials only, no photos), and Consumer Help starter copy. Appendix N and P21 carry the system to rewrite the remaining ≈ 600 pages from the manuals; Appendix E lists every page, its status and whether its source text was copied from third parties or cites repealed law. Appendix O holds review-ready drafts of the privacy notice, terms of use, eSign/eStamp terms, AI use policy, refund and subscription policy, marketplace and professional terms, cookie policy, grievance policy, acceptable use, retention schedule, accessibility statement, security page and Consumer Help terms, and *(v1.1)* §O.17 adds the Payment and Subscription Terms, Blog and UGC Terms, Resources Download Terms, Vendor/Outsourcing Assurance Statement and the Investors disclaimer (POL-LD-18…22) with inserts into the existing policies.

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
| 17 *(v1.1)* | **Investors page publication**: publish for LawDocs at all; gated documents and gating mode; IR contact; disclaimer wording [COUNSEL — Companies Act 2013 s.42, SEBI advertisement code] (`web.investors.enabled` stays OFF until decided) | P21 §4R |
| 18 *(v1.1)* | **Blog contributor (user-post) programme**: open to verified customers and professionals? eligibility roles, account age, daily limit, advocate authorship under BCI Rule 36, moderation staffing (`web.blog.user_posts.enabled` OFF until decided) | P21 §4I |
| 19 *(v1.1)* | **Image generation**: provider for marketing/CMS images and confirmation that human review before publishing any AI-generated image is mandatory (pack default: yes, locked) | P09 §4N, P21 §4I |
| 20 *(v1.1)* | **Tag manager**: none (default) vs server-side GTM vs web GTM; `PLT_DPO` veto | P21 §4L |
| 21 *(v1.1)* | **Alternative adapters to contract first** for Tier-0 ports (second ESP, CPaaS, storage target, `in_zero` LLM) | P00, P19 |

**Counsel questions:** Appendix W §W.5 (52) — the most material are the marketplace structure under BCI Rule 36 after the Madras High Court judgment, CA/CS participation, the Consumer Help entity and fee model, eSign eligibility of agreements to sell, the hosted eSign hand-off for group products, Aadhaar offline verification, DigiLocker retained copies, DPDP roles, and the AI-draft review gate. **Tax memo:** Appendix W §W.6 (17).

**Companion change requests:** Ecosystem Spec v1.2 (Appendix Y — *(v1.1)* now registered), Operations Hub v1.1, LawDocsComply v1.3, Equator v3.2, Finbyx and Udofin notes (master §19, Appendix X) — all delivered in the 26 October 2026 group upgrade; residual asks in Appendix W §W.4.7.

## 6. Requirement coverage

*(v1.1)* IPB coverage: every item of the group upgrade brief §2 (adoption clause, stack pin, precedence, decision log, Vidhi kernel, "i" registry, website and Studio, policies, accessibility, settings tree, vendor assurance, engineering governance, API standard, environment and seeds, design brief, content deck, feedback/tutorials/What's new/search/WhatsApp/marketing/white-label, future-ready flags, Claude artefacts, session prompts, README, cross-pollinated features) is mapped to a LawDocs file in `_review/v1.1_upgrade_review_log.md` §1.

All 92 brief requirements (R-001…R-092) map to phases and appendices (`02` §8). Appendix Z traces 581 atomic asks: owner brief 340 covered, 57 changed by a recorded decision or challenge, 1 partial (a Jio developer-portal reading item); ChatGPT prompt 121 covered, 4 changed; manuals 49 covered, 9 awaiting owner approval of starter lists. Thirty-two challenges to the brief are recorded with lawful alternatives (`02` §3) — among them: no Aadhaar login, no CIBIL or CKYC pulls, no shared plaintext password tracker, no fees from advocates, no eSign for wills and powers of attorney, and no "replace your lawyer" claims.

## 7. Immediate actions independent of the build

- Make lawdocs.in server-rendered (today crawlers see empty pages), fix the non-www sitemap and the robots/sitemap conflict on `/buy/`, and keep or 301-redirect all 186 sitemap URLs (P00, P21).
- Remove unevidenced claims from the live site and manuals (for example "verified", "blockchain", "home delivery", "produced before any Court") and replace the testimonials adapted from other products (content deck §5.5; NN-20, NN-49).
- Start rewriting copied third-party sections and repealed-law references in the manuals (Appendix E, content deck §5).
- Begin vendor diligence for eSign aggregators (ASP structure, second ESP, CCA licence status), eStamp channels, court-data and MCA-data vendors (Appendix W §W.7).
- Request counsel opinions on the marketplace model and the Consumer Help entity before Wave 2 and Wave 3 respectively.
