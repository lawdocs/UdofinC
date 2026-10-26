# Equator Resolution — Build Prompt Pack v3.0

**Prepared:** 19 October 2026 · **Revised:** 20 October 2026 (v1.1) · **v2.0:** 22 October 2026 (dispute-type specifications, ten new binding appendices, full v2 review) · **v2.1:** 22 October 2026 (all 469 open items researched and dispositioned; Appendix U policy baselines) · **v3.0:** 23 October 2026 (configuration framework, Operations Platform, marketing, workforce and payroll, marketplace and registry, revenue registry, workspace suites and portability, group companies, engineering governance; eleven new appendices and seven new phases) · **Owner:** Company Secretary, Infrabyx Group · **Entity:** Equator Resolution Service Private Limited · **Product:** Equator Resolution (equatorresolution.in), an ODR institution with web and mobile platforms, plus the Equator Operations Platform for staff
**Stack (locked):** Next.js web (`apps/web`) and Operations Platform (`apps/ops`) · NestJS (TypeScript) modular monolith · PostgreSQL (Aurora) with RLS · Temporal · Redis · OpenSearch · S3 Object Lock · React Native (Expo) mobile · Keycloak (`eq-portal-ops` for staff, phishing-resistant MFA) · AWS Mumbai (DR Hyderabad)

---

## 1. What this pack is

This is a paste-ready, phase-by-phase build prompt for a coding agent (Claude Code, Antigravity or equivalent) to build Equator Resolution end to end. It brings together the Equator corpus (551 documents) and research current to 23 October 2026 (v1: R1–R5, C1–C5 and the verification of 514 flags; v2: research streams S1–S9; v3: research streams RA–RE).

**What v3.0 adds (23 October 2026)**

Management's brief of 23 October 2026 asked for configurable open items and complete settings; deeper customisation and a small HR module for Private ADR Chambers and independent neutrals; a separate Operations Platform; workforce lifecycle, payroll and internal controls; Microsoft 365 with portable records; switchable revenue streams; marketing automation; empanelled advocates and a group-wide professional directory; change, patch and audit management; a departmental structure; multi-company operations; and an Equator Marketplace benchmarked against Jupitice.

- **Appendix V — Configuration Framework, Rule Engine and Settings Catalogue.** Three tiers for every configurable value (Locked, Governed, Tenant; NN-33); a Governed rule engine with effective dating, sandbox, impact analysis, rollback and a regulatory-watch feed; all 469 open items classified by configurability (L 65, G 346, T 7, N 51); a settings catalogue for every persona.
- **Appendix W — Private ADR Chambers Workspace v3 and Practice HR.** Practice pages and verified domains as a separate surface, extensive chambers and neutral settings, staff and case-manager queues, and a practice HR-lite module with salary records, pay runs and bank-file disbursal (Equator never holds salary money).
- **Appendix X — Equator Operations Platform: CRM, Onboarding, Customer Success, Support and Grievance.** A separate staff app (`apps/ops`), not the super-admin console; default departments and workspaces; the CRM of record (open to Brevo, HubSpot and Zoho); tickets and grievances; a no-code automation engine with a locked human-approval list.
- **Appendix Y — Marketing, Brand, Social Media, PR and Growth Automation.** The campaign and social calendar kept in Equator while Brevo, Adobe Express and social tools send or publish; partnerships, PR, attribution and outcome-based contribution metrics; "autopilot" with human approval of claims, prices and mass sends.
- **Appendix Z — Workforce HRMS, Payroll and Internal Controls.** Full employee lifecycle including work e-mail provisioning; transparent attendance and output-based work measurement (no covert monitoring, NN-35); leave and payroll under Indian labour law on versioned rule packs; authority matrix, maker-checker, separation of duties and anti-fraud controls (NN-36).
- **Appendix AA — Equator Marketplace and Infrabyx Professional Registry.** Three isolated surfaces; a Private Practice Marketplace with labelled, capped sponsored listings (OFF); a consent-based professional registry run as a group shared service; a post-resolution professional chooser for execution, registration and recovery.
- **Appendix AB — Revenue Architecture v3 and Revenue Stream Registry.** 57 switchable streams (RS-01–RS-57) — one-time, subscription, monthly rental, pay-as-you-go, advertising — each with a kill switch, neutrality rating, tax treatment, refund code and Board gate.
- **Appendix AC — Workspace Suites, Open Integrations and Data Portability.** A suite-neutral `WORKSPACE_PORT` (Microsoft 365 first, Google Workspace later), an open-integrations catalogue with systems of record and field mappings, and the export package `EQ-EXPORT-1.0` (folders of Word, Excel and PDF with a manifest; NN-37).
- **Appendix AD — Group Companies and Cross-Functional Operations.** Legal entities, shared services as processing, cross-company grants under a Group Data-Sharing Agreement, secondment and recharges; case and allocation data never shared with Finbyx or Udofin (NN-38).
- **Appendix AE — Engineering Change, Release, Backup and Audit Management.** GitHub branching and protection, change classes and CAB, patch SLAs, backups and restore tests, VAPT, IS audit, internal and external audit, auditor workspace.
- **Appendix AF — Competitive Research v3 (reference).** Jupitice and its ADR Marketplace, institutions' operating and revenue models, the equatoradr.com training site (corrections C1–C20), and dated corrections to Appendices T, H and B.
- **Phases P15–P21.** P15 Configuration Studio and Tenant Settings · P16 Operations Platform (CRM, support, onboarding, customer success) · P17 Marketing, Brand and Growth Automation · P18 Workforce HRMS, Payroll and Internal Controls · P19 Marketplace, Professional Registry and Revenue Stream Registry · P20 Chambers Workspace v3 and Practice HR · P21 Group Operations, Integrations and Portability.
- **Governance records.** Master NN-33–NN-40, cross-file resolutions X-43–X-66, §4.5 data planes and §18 v3 reading order; `02` requirements R-44–R-70, decisions D3-01–D3-44 (D2-14 retained for the institutional directory), eight new counsel questions and the v3 review log; Appendix F §F.10.4 v3 error-code register; Appendix S §6.9 v3 roles; Appendix J §J.9 configurability; corrections to Appendices B, D, G, H, O, Q, T and phases P00, P01, P05, P10, P13.
- **Departmental structure.** Management's message said it would explain the departmental structure but did not. v3.0 therefore ships a **default, fully configurable** department model (D3-06; master §18 item 5) that management can rename, merge or replace without code.

**What v2.1 added (22 October 2026):** Appendix J rebuilt — every one of the 469 open items has a disposition, evidence, residual uncertainty, approver, production gate and recheck trigger (129 closed, 90 provisional, 250 awaiting counsel, vendors, decisions or a regulatory event; 19 launch gates); 355 in-place corrections; Appendix U policy baselines from the old Equa site; Code of Conduct ECC-2026.1 additions; R-41–R-43, D2-28–D2-29; role `neutral_facilitator`.

**What v2.0 added to v1.1:** one specification per dispute type (`verticals/V1–V6`, with separate intake forms for negotiation, mediation and arbitration); Dispute Explorer v2 and the dispute-type plug-in framework (K); DMS, Supreme Court A4 formats, type copies and translation (L); AI Pleadings Studio (M); neutral governance, grades, QAP, Code of Conduct and Private ADR Chambers (N); revenue, plans, billing and settings (O); website copy deck and SEO/GEO (P); privacy, security and certification readiness (Q); case status, publication, execution and registration (R); identity, separate logins and RBAC (S); benchmarks (T); NN-24–NN-32 and X-19–X-42.

**What v1.1 covered (unchanged unless superseded):** six verticals plus SEBI SMART ODR as an optional connector (flag OFF); every mechanism including med-arb and arb-med-arb; Private ADR Chambers, Enterprise API and bulk intake, GRM SaaS, POSH/IC SaaS and the Academy; the fee engine (INR default; USD/EUR/GBP/SGD/AED for international matters; approval-gated rate cards); voice and omnichannel communications, eSign/eStamp, payments and escrow; website remediation.

## 2. Files

Word counts were computed on 23 October 2026 after integration and before the v3 addenda are appended to P00–P14 (whitespace-separated words, as `wc -w`; rounded to the nearest 100; tables count).

| File | Purpose | Words |
|---|---|---|
| `00_README.md` | This guide | 5,100 |
| `01_MASTER_PROMPT.md` | Constitution: product, **NN-01–NN-40**, architecture (incl. §4.5 v3 data planes), domain model, customisability, fees, integrations, AI, phase plan P00–P21, precedence and cross-file resolutions **X-01–X-66**, management decisions, v2 and v3 reading order | 15,800 |
| `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` | Requirements R-01–R-70, decisions D2-01–D2-29 and D3-01–D3-44, assumptions, counsel questions, dependencies, phase mapping, v2 and v3 review logs | 11,400 |
| `phases/P00–P14` (15 files) | Build phases; each ends with a **v2 addendum** and a **v3 addendum**, which are part of that phase's scope and exit gate | 192,700 in total |
| `phases/P15_Configuration_Studio_and_Tenant_Settings.md` | Configuration Studio, settings registry and SDK, rule-pack engine (Appendix V) | 9,800 |
| `phases/P16_Operations_Platform_CRM_Support_Onboarding.md` | Operations Platform: CRM, support, onboarding, customer success (Appendix X) | 10,900 |
| `phases/P17_Marketing_Brand_and_Growth_Automation.md` | Marketing, brand and growth automation (Appendix Y) | 11,300 |
| `phases/P18_Workforce_HRMS_Payroll_and_Controls.md` | Workforce HRMS, payroll and internal controls (Appendix Z) | 11,800 |
| `phases/P19_Marketplace_Professional_Registry_and_Revenue.md` | Marketplace, professional registry, revenue stream registry (Appendices AA, AB, AF) | 11,600 |
| `phases/P20_Chambers_Workspace_v3_and_Practice_HR.md` | Chambers workspace v3 and practice HR (Appendix W) | 9,300 |
| `phases/P21_Group_Operations_Integrations_and_Portability.md` | Group operations, integrations and portability (Appendices AC, AD) | 11,000 |
| `verticals/V1–V6` (6 files) | FIN, COM, FAM, INS, WRK and INT dispute-type specifications | 157,200 in total |
| `appendices/A–J` | v1 binding specifications: workflows (A), fees (B), screens (C), integrations (D), AI and voice (E), data model, events and errors (F; v3 register §F.10.4), legal rules register (G), competitors, GTM and website corrections (H), tests (I), verification log and open items (J; §J.9 configurability) | 202,200 in total (J ≈ 70,700) |
| `appendices/K–U` | v2 and v2.1 binding specifications (Dispute Explorer v2, DMS, Pleadings Studio, neutral governance, revenue and settings, copy deck, privacy and security, case status, identity and RBAC — S §6.9 v3 roles — benchmarks, institutional rules) | 230,100 in total |
| `appendices/V_Configuration_Framework_Rule_Engine_and_Settings_Catalogue.md` | Configuration framework (v3.0) | 22,000 |
| `appendices/W_Private_ADR_Chambers_Workspace_v3_and_Practice_HR.md` | Chambers workspace v3 and practice HR (v3.0) | 21,000 |
| `appendices/X_Equator_Operations_Platform_CRM_Support_Customer_Success.md` | Operations Platform (v3.0) | 20,200 |
| `appendices/Y_Marketing_Brand_Social_PR_and_Growth_Automation.md` | Marketing, brand, social, PR and growth automation (v3.0) | 19,700 |
| `appendices/Z_Workforce_HRMS_Payroll_and_Internal_Controls.md` | Workforce HRMS, payroll and internal controls (v3.0) | 20,400 |
| `appendices/AA_Marketplace_and_Professional_Registry.md` | Equator Marketplace and Infrabyx Professional Registry (v3.0) | 19,300 |
| `appendices/AB_Revenue_Architecture_v3_and_Stream_Registry.md` | Revenue architecture and stream registry (v3.0) | 19,100 |
| `appendices/AC_Workspace_Suites_Open_Integrations_and_Data_Portability.md` | Workspace suites, integrations and portability (v3.0) | 18,100 |
| `appendices/AD_Group_Companies_and_Cross_Functional_Operations.md` | Group companies and cross-functional operations (v3.0) | 10,700 |
| `appendices/AE_Engineering_Change_Release_Backup_and_Audit_Management.md` | Engineering change, release, backup and audit (v3.0) | 21,200 |
| `appendices/AF_Competitive_Research_v3_Jupitice_Institutions_Training.md` | Competitive research v3 (reference, v3.0) | 14,000 |
| **Total** | 63 files | **1,095,800** |

Earlier versions stay in their own folders for reference (v1, v2, v2.1); v3.0 supersedes them. A consolidated Word copy is produced separately for review and sign-off. Appendix V exceeds the usual appendix length because it holds the full 469-row configurability register.

## 3. How to run the build

1. Create an empty repository and open the coding agent in it.
2. **At the start of every phase session,** paste `01_MASTER_PROMPT.md`, then `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, then the phase file (including its v2 and v3 addenda). Attach the appendices and vertical files that the phase cites. Read master §18 before any v3 work.
3. **Phase order (v3.0):** **P00 → P01 → P15 → P02 → … → P14**, then P16–P21 as below.
   - **P15** starts directly after P01 and runs alongside P02 onwards: every later phase registers its settings in the P15 registry as it builds them (registry before use, D3-11), using the SDK from P15 sprint 1. P15 must be complete before P16–P21 start.
   - P08 runs as six sub-iterations, P08a FIN → P08f INT, each starting with the matching `verticals/V<n>` file.
   - P13 may run in parallel with P08–P11 using a second squad. Mobile work starts in P01 and closes in P12.
   - **P16** (Operations Platform) needs P00, P01, P15 and P05 read models; it ships stated fallbacks where P09, P13, P07, P11, P18 or P21 are not yet done.
   - **P17** (marketing) needs P13, P15 and P16.
   - **P18** (HRMS, payroll, controls) needs P00, P01, P15 and P16; it consumes P05, P09, P10 and P14.
   - **P19** (marketplace, registry, revenue registry) needs P03, P05, P10, P15 and P16.
   - **P20** (chambers v3, practice HR) needs P10, P15, P18 and P19.
   - **P21** (group operations, integrations, portability) runs last: it needs P00–P14 and P15–P18.
   - Each v3 phase has its own exit gate; a v3 phase released after the first go-live re-runs the P14 hardening and go-live checklist for its scope.
4. **Before coding,** the agent writes `docs/phases/PXX-plan.md`. It stops at the phase exit gate (§13 of each phase file plus the addenda's acceptance tests).
5. **Precedence on conflict** follows master §15 (master and 02 → Appendix G for law → B for fees → F for names and codes → A for states → phase file → other appendices; v3: Appendix V on tiers and keys, the AB registry on whether a stream may be offered, and each v3 appendix on the schema it owns). The X-resolutions record the conflicts already resolved.
6. **Unverified rules and dependencies:** any feature that depends on a legal rule still marked `UNVERIFIED` or **[VERIFY — open]**, a vendor contract, a Board approval or an unconfirmed fact ships behind a flag that is OFF and names its approver.

**Indicative effort:** 30–36 two-week sprints for P00–P14 with two squads (platform + verticals) plus a growth/website squad. The v3 phase files estimate P15 6 sprints (squad of 8), P16 8 (9), P17 6 (7), P18 10 (9), P19 8 (10), P20 6 (9) and P21 6 (8); several run in parallel once P15 and P16 are done.

## 4. Decisions and approvals needed before go-live

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | **Rate cards and fee schedules.** Rate cards are customisable and approval-gated (M-01). The Board approves the default fee schedules (Appendix B) and the plans and one-time products (Appendix O). | Board / CFO | P05, P13 fees and plans pages |
| 2 | **Entity particulars** for Equator Resolution Service Private Limited (M-02): CIN, registered office, GSTIN, DPO, Grievance Officer, Nodal Officer. | Company Secretary | P13, P14, invoices, privacy notices |
| 3 | **Rulebooks:** Equator Rules (arbitration, mediation, conciliation, negotiation), vertical rules, Code of Conduct for neutrals, Institutional Committee charter (majority external) and complaints procedure. | Board / Legal | P03, P04, P08, App. N |
| 4 | **Neutral grading policy** (A/B/C), QAP design and fees, assessor panel, and the published allocation formula (D2-12, D2-13). | Head of Institution | P03, P10 |
| 5 | **Equator ADR Institute (D2-17, D3-38):** confirm its operating entity (the site shows Infrabyx Consultancy (OPC) Pvt Ltd) and correct its public claims (C1–C20, Appendix AF §AF.4.3). The referral card and stream RS-22 stay OFF until then; any referral arrangement is a related-party transaction (s.188; s.177 only where an Audit Committee is required; s.184 disclosure) **[CS to confirm]**. | Company Secretary / Institute | P10, P13, P19 |
| 6 | **UIDAI and DigiLocker:** OVSE registration for Aadhaar offline verification; DigiLocker requester partnership. No bureau pulls at onboarding (D2-06). | CTO / Compliance | P01 |
| 7 | **Counsel opinions** in 02 §5 items 1–15 (s.42A publication consent, AI self-help drafting, s.442 panel mediations, MSMED 2026, Insurance Act intermediary question, "Court" in Chambers names, recovery-agency status). | General Counsel / external counsel | Flags in P06, P08, P10, P13 |
| 8 | **Telecom and calling (M-05):** DLT Principal Entity registration, CPaaS contracts, CLI opinion for Equator's own service numbers; Jio carrier and Haptik RFP (D2-23). | CTO / telecom counsel | P07 |
| 9 | **Pre-suit mediation (M-06):** voluntary pre-suit mediation is live now; mandatory s.12A PIMS stays with the Legal Services Authority until the four gates close. | General Counsel | P08 COM |
| 10 | **Vendor contracts** (candidates, not commitments): ElevenLabs Enterprise (India residency), Sarvam, Exotel/Plivo, Gupshup, MSG91, Leegality, Digio, SignDesk, Surepass, Razorpay, Castler, LiveKit, AWS Bedrock India, OCR and translation providers; v3: Brevo, Adobe Express, social platform access, payroll and accounting tools (Tally/Zoho Books). | CTO / Procurement | P01, P05–P07, P11, P16, P17, P21 |
| 11 | **Policy set** for certification readiness: information security, access control, incident response, vendor risk, retention, privacy notices, cookie policy. | Company Secretary / CISO | P14, App. Q |
| 12 | **Live website corrections:** apply Appendix H §5 and the Appendix P replacement copy now, independent of the build. | Marketing + Legal | Immediate |
| 13 | **Open items:** work through Appendix J §J.5.3, starting with the 19 launch gates (§J.5.2); every item is also classified by configurability in Appendix V §V.3 (Appendix J §J.9). | Legal counsel / tax adviser / CTO | Feature flags |
| 14 | **Confirm the Microsoft 365 SKU (D3-04).** Management named "Business Starter", which is not a Microsoft plan; the design works on Business Basic. Confirm the plan held and decide Business Premium (or add-ons) for console, Tier-High, sealed and finance users (D3-40). | Company Secretary | P18 work e-mail provisioning, P21 workspace connection |
| 15 | **Board approval of revenue streams and paid placement.** The stream registry waves, prices and Board thresholds (D3-39; Appendix AB) and the sponsored-listing stream RS-19 with its equal rate card (D3-37) — `marketplace.paid_placement` stays OFF until the Board approves and counsel signs off (NN-34). | Board / CFO / counsel | P19, P13 pricing and marketplace pages |
| 16 | **Counsel on the professional directory (NN-39):** BCI r.36 and its Schedule, *Sulekha.com v P.N. Vignesh* (SLP (C) 25794/2024), ICAI/ICSI/ICMAI aggregator and referral bars, the Post-Resolution Advocate Panel terms; the E-Commerce (Amendment) Rules 2026 text. `directory.public_professionals` and `postres.advocate_panel` stay OFF. | General Counsel / external counsel | P19 public search and panel, P06 chooser |
| 17 | **Group Data-Sharing Agreement and registry owner.** The Board designates the registry owner entity (D3-05); GDSAs, intra-group processing agreements and service agreements are signed with s.188 status recorded; the shareholding chain and related-party status (s.2(76)) are confirmed. | Board / Company Secretary | P19 registry go-live, P21 group go-live |
| 18 | **Payroll parameters sign-off.** Every `NOT_CONFIRMED` or `SECONDARY_ONLY` parameter in Appendix Z §Z.2.4–§Z.2.5, and the remote-employee PT/LWF opinion (D3-31). | Payroll Compliance Officer with CA / counsel | First live pay run (P18), chambers pay runs (P20) |
| 19 | **Employee monitoring notice (NN-35).** Issue the notice for attendance, login/logoff and work measurement (quoting the enacted DPDP s.7(i) text); approve the DPIA before individual ROI views are enabled (D3-33). | DPO / HR head | P18 attendance capture |
| 20 | **GitHub Enterprise Cloud (D3-09).** Licence GHEC (with Secret Protection and Code Security) for environment protection on private repositories, or record the `ReleaseApprovalWorkflow` compensating control. | CTO / Board | P00 production deployments |
| 21 | **Delegation of Financial Powers (D3-34)** and the **department model (D3-06):** the Board approves the authority-matrix values; management confirms or replaces the default departments. | Board / management | P16 workspaces, P18 go-live |

## 5. Requirement coverage map

The full map with status is in `02` §2 (R-01–R-70).

**Briefs of 19–22 October 2026 (v1–v2.1)**

| Area | Where addressed |
|---|---|
| Six dispute types, subtypes, separate law, rules, process, forms per mechanism, dropdowns, integrations and APIs | V1–V6; Master §1.2, §5.2; P08 (P08a–f); App. K §4 |
| Add further dispute types later | App. K §6 plug-in framework |
| Arbitration, mediation, med-arb, negotiation, conciliation; pre-litigation mediation | Master §1.3, §5.3; P04; App. A; App. K §5; V1–V6 §8 |
| Dispute Explorer, ADR suitability, criminal exclusion | App. K §1–§3; NN-24 |
| AI drafting of claims, defences and affidavits; pluggable AI | App. M; NN-25; P11 |
| Separate logins, onboarding APIs, representatives, dashboards, RBAC | App. S; P01; NN-14, NN-27 |
| DMS, A4 Supreme Court format, type copies, translation | App. L; NN-32 |
| Case status, publication with consent, execution and registration | App. R; NN-26 |
| Neutral onboarding, directory, grades, QAP, Code of Conduct, complaints, ratings, allocation; Private ADR Chambers SaaS | App. N; P03, P10; NN-28 |
| Training providers, Equator ADR Institute, IMI QAP | App. N §9–§10; App. T §3; App. AF §AF.4; D2-17, D3-38 |
| Competitors, international institutions, Reliance Jio AI | App. T; App. H; App. AF |
| Revenue streams, subscriptions, billing and membership settings | App. O; App. AB; NN-29 |
| Privacy laws; PCI DSS, SOC 2, ISO readiness | App. Q; NN-30, NN-31 |
| Copywriting, SEO/GEO/AI search; clean minimal UI | App. P; App. C |
| Fees in INR with foreign currency; approval-gated rate cards | Master §7; App. B; P05; V6 |
| GRM SaaS, POSH/IC SaaS, Enterprise API, Academy | P09, P10 |
| SEBI optional; Equator places its own calls; pre-suit mediation | Master §1.2, NN-12, §16 |
| Policies from the old Equa site; research on every open item | App. U; App. J §J.5–§J.9 |

**Brief of 23 October 2026 (v3.0)**

| # | Brief item | Where addressed |
|---|---|---|
| 1 | Open, interim and externally dependent items configurable through settings; routine changes without a super admin; legally sensitive values governed | NN-33; App. V §V.1–§V.3 (469 items classified); P15; D3-10–D3-14; App. J §J.9 |
| 2 | Complete settings for every user type; extra customisation and website pages for Private ADR Chambers and independent neutrals; staff and case-manager management; small HR module with salary records and disbursal | App. V §V.4; App. W §W.3–§W.8 (pages, settings, staff), §W.6 (practice HR); P20; D3-15–D3-19 |
| 3 | Separate Operations Platform for operations, service delivery, after-sales, onboarding, customer success, marketing, brand, social, PR, collaborations, CRM, grievances and tickets; open to Brevo and other tools with integration and migration | D3-02; App. X (P16); App. Y (P17); App. AC §AC.11–§AC.14; NN-40; X-50–X-55 |
| 4 | Performance appraisal and full employee lifecycle (incl. e-mail IDs); decentralised decisions, maker-checker, anti-corruption, anti-embezzlement; leave and salary under Indian labour law; remote work; login/logoff, work measurement; case managers at home | App. Z; P18; NN-35, NN-36; D3-30–D3-34; X-56–X-58 |
| 5 | Microsoft 365 (SKU to confirm) with Teams and SharePoint, Google Workspace later; documents open in MS Office; downloads as self-explanatory folders of Word, Excel and PDF | App. AC; P21; D3-04, D3-40, D3-41 (`EQ-EXPORT-1.0`); NN-37; master §18 item 6 |
| 6 | Switchable, customisable revenue streams (one-time, subscription, monthly rental, pay-as-you-go, advertising); paid preference placement for private-practice neutrals | App. AB (RS-01–RS-57, kill switches); App. AA §AA.10; P19; NN-34; D3-01, D3-37, D3-39; X-61, X-62 |
| 7 | "Autopilot" business automation; full marketing architecture with calendar inside Equator | App. X §X.12 (engine, human-approval list); App. Y §Y.7; P16, P17; D3-23, D3-25–D3-29 |
| 8 | Empanelled advocates and an all-India directory of advocates and professionals shared across the group (execution, registration, NPA recovery suits) | App. AA §AA.11–§AA.12; NN-39; D3-05, D3-36; X-60; App. AD |
| 9 | Change and patch management on GitHub branches; backups, VAPT, IS audit, internal and external audit | App. AE; D3-09, D3-43, D3-44; X-65, X-66; P00 FR-P00-08 note; Q SC-11 |
| 10 | Departmental structure (to be explained by management — not received) | D3-06 default, fully configurable model; master §18 item 5; FR-P18-02; App. X §X.3 |
| 11 | Multi-company: staff cross-functional for Finbyx and Udofin; dashboards, content and data shareable under controls | App. AD; P21; NN-38; D3-42; X-64; App. D §D.7 note |
| 12 | Jupitice and its ADR Marketplace researched; an Equator Marketplace as a revenue stream | App. AF; App. AA; P19; D3-35; corrections to T, H and B |
| 13 | ChatGPT "Expanded Prompt" (configurability classes, settings and permission matrix, Operations Platform, CRM, marketing, workforce, maker-checker, portable records and manifest, revenue and marketplace economics, opt-in directory, competitive research, autopilot with human approval, multi-company, change and audit, staged delivery) | Followed where consistent with D3-01–D3-09: V, X, Y, Z, AA–AF; App. S §6.9; master §10 staged order |

## 6. Key judgments embedded (read before approving)

**v3.0 judgments**

- **Paid placement has hard limits (NN-34).** Sponsored listings exist only on the Private Practice Marketplace, only for non-advocate private-practice neutrals and chambers, in a separate block labelled "Sponsored — paid placement. Does not affect Equator appointments.", at most 2 per page and 20% of results, at one equal rate card, with published ranking rules. They never touch the institutional directory, allocation, eligibility, Quality Index, grading or conflict checks. The flag is OFF until the Board approves and counsel signs off. Advocates, CAs, CSs and CMAs are never sold placement, ratings or featured labels and receive no referral reward of any kind (X-62).
- **The advocate directory is consent-based and OFF in public (NN-39).** Listings are opt-in with per-field display consent, verified and removable; nothing is scraped or bulk-imported from Bar Council rolls or institute directories; advocate fields follow the BCI r.36 Schedule; public advocate search stays OFF pending counsel and the Supreme Court appeal (SLP (C) 25794/2024). The party always chooses the professional.
- **No covert monitoring (NN-35).** Attendance and work measurement are disclosed, purpose-limited and outcome-based; keystroke logging, webcam capture, screenshots of personal devices and undisclosed device monitoring are locked OFF; employees see and can dispute their own data.
- **Maker-checker everywhere money or authority moves (NN-36).** No single person can create a payee, change bank details, approve and execute a payment and reconcile it; bank changes have a cooling-off period and out-of-band confirmation; the authority matrix is a Board proposal; ledger, billing and payroll keep an un-disableable edit log.
- **Portability is free at exit (NN-37).** Every organisation, user and group company can export everything as folders of DOCX/XLSX/PDF (PDF/A for final records) with a README and a checksummed manifest, within OneDrive and Windows path limits.
- **Group boundaries (NN-38).** Group membership grants no data access; cross-company access needs a purpose-bound, time-limited grant under a Group Data-Sharing Agreement; case and allocation data are never shared with Finbyx or Udofin, which receive a lender's case events only as that lender's processor (X-64).
- **Microsoft 365 Business Basic caveat (D3-04).** "Business Starter" is not a Microsoft plan; the design works on Business Basic, where Office desktop apps are not included (web and mobile only), so exports are tested in Office for the web. Keycloak, not the Microsoft plan, controls access to every Equator console, and Microsoft 365 is never a system of record. Equator-administered hearings never run on Teams.
- **Configuration never weakens the law (NN-33).** Statutory floors and NN rules are locked; legal parameters are governed with citations, maker-checker and a configured fallback; tenants change routine settings themselves.
- **Training stays separate (D3-38).** Equator books ₹0 from the training site unless the Board approves an arm's-length related-party arrangement; training never affects empanelment, grade, allocation or the EQAP fee.

**Judgments carried from v1–v2.1**

- **No legal advice.** AI never advises, predicts or values a party's case (NN-01). The Dispute Explorer reports suitability, pathways, cost, time, limitation flags and free-forum options.
- **AI Pleadings Studio is self-help** on identical terms to both sides, grounded only in the party's documents and a verified corpus (NN-25, D2-07).
- **Criminal matters are excluded** (NN-24); where the law allows, only the civil dimension is settled.
- **Publication of awards and settlements** needs every party's consent after the outcome; arbitral publication stays OFF until counsel rules on s.42A (NN-26, X-35).
- **Aadhaar** only through offline verification; no bureau pulls at onboarding (D2-06).
- **Pre-suit mediation (M-06)** is voluntary; Equator never claims to satisfy Commercial Courts Act s.12A until the four gates close.
- **Lender arbitration** is built to survive challenge after *CORE* (2024) and *Bhadra* (2026).
- **Mediation Act 2023** statutory mode stays behind a flag; the Singapore Convention is signed, not ratified, so consent-award conversion is offered.
- **IBC and in-rem matters** are never decided by Equator (D2-02).
- **Neutral grades** follow management's definition with a competence gate; allocation rules are published; the institutional directory has no paid listings and no outcome statistics (NN-28).
- **Honest pricing:** GST-inclusive prices, all 13 dark patterns linted, cancellation as easy as sign-up (NN-18, NN-29).
- **Certification readiness, not certification** (NN-17, NN-31).
- **Settlement money never passes through Equator's merchant account** (NN-13).
- **POSH, health and family-safety data are sealed** (NN-07).

## 7. Completion checklist

**Complete in this pack (specified and cross-checked)**

- [x] Six vertical specifications V1–V6; Appendices K–U; v2 addenda in every phase file
- [x] Appendices V–AF and phases P15–P21 (v3.0), each reviewed independently (RVA–RVE, about 190 fixes) and integrated (I1 new files; I2 existing files)
- [x] Master NN-33–NN-40, X-43–X-66, §4.5 data planes, §10 phases P15–P21, §18 v3 reading order
- [x] `02` R-44–R-70, D3-01–D3-44, D2-14 amendment, counsel questions 16–23, v3 phase mapping and review log
- [x] Appendix F §F.10.4 v3 error-code register (extracted by script from the defining appendices) and v3 event contexts; Appendix S §6.9 v3 roles and permissions; Appendix J §J.9 configurability summary
- [x] Corrections applied: e-commerce TDS threshold (G LR-TAX-007, B §B.10, P05); advocate referral credits removed (O, B, P01, P10, P13, S; X-54/X-62); P13 mini-CRM superseded (X-51); `growth.*` → `mkt.*` flag aliases (X-55); Q SC-11 patch-SLA ceilings (X-66); P00 GitHub plan note (D3-09) and port count; D ports, `bank_file` adapter, `CrmPortV3` and X-64 note; Appendix AF corrections to T, H and B that rest on dated sources or binding v3 rules
- [ ] v3 addenda appended to P00–P14 from the appendices' phase-addenda sections (by the lead, by script)

**Depends on vendors or registrations** (flags OFF until contracted or registered)

- [ ] UIDAI OVSE; DigiLocker partner; MCA/KYB aggregator
- [ ] DLT/telecom: CPaaS, Jio carrier, CLI declarations; ElevenLabs India residency; Jio Haptik RFP
- [ ] eSign/eStamp providers by state; payment gateway (Standard Checkout, Route) and bank escrow
- [ ] LLM in India (Bedrock India) for case content; OCR and translation providers meeting the residency rules
- [ ] Independent assessors: PCI DSS ASV scans and SAQ A attestation; SOC 2 auditor; ISO 27001/27701 certification body
- [ ] v3: Microsoft 365 SKU confirmed; Brevo account and DPA; social platform API access; GitHub Enterprise Cloud; payroll and accounting tool exchange formats

**Needs qualified counsel, Board or management sign-off before launch**

- [ ] Counsel questions in `02` §5 (items 1–23) and Appendix J
- [ ] Every Legal Rules Register row marked `UNVERIFIED` and every open item in Appendix J §J.5.3 (19 launch gates in §J.5.2)
- [ ] Board and counsel approval of the policy set in Appendix U before publication
- [ ] Rulebooks, Code of Conduct, Committee charter, grading policy, fee schedules and plans (§4 items 1–4)
- [ ] Institute entity, corrections C1–C20 and related-party approvals (§4 item 5)
- [ ] Policy documents for certification readiness (§4 item 11)
- [ ] v3: revenue streams and sponsored listings (§4 item 15); directory counsel (item 16); registry owner and GDSA (item 17); payroll parameters (item 18); employee monitoring notice (item 19); authority matrix and departments (item 21)

## 8. Not in this pack

- Legal opinions (the pack lists the questions).
- Signed vendor contracts and the Group Data-Sharing Agreements.
- The policy documents management will prepare, including the employee monitoring notice.
- Final rulebook text and the Delegation of Financial Powers approved by the Board.
- Management's own departmental structure (a configurable default is used, D3-06).
- Translated copy beyond the English and Hindi samples given (the translation workflow is specified).
