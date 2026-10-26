# LAWDOCSCOMPLY — MASTER BUILD PROMPT (v1.1, 25 October 2026; supersedes v1.0 of the same date)

**Governance, Risk and Compliance (GRC) SaaS for regulated financial entities, companies, LLPs and co-operative societies — India first, global-ready**

Product: LawDocsComply (lawdocscomply.com), product code `LDC` · Owner: Company Secretary, Infrabyx Group · Companion documents: Infrabyx Ecosystem Integration Specification v1.1, Finbyx Master Prompt v1.5, Udofin Master Prompt v1.2, Infrabyx Operations Hub Master Prompt v1.0, Equator Resolution Build Prompt Pack v3.1.

> **How to use (project owner — do not paste this box).** At the start of every build session paste, in this order: this file, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, then the phase file (`phases/PXX_*.md`). Attach the appendices the phase file names as binding. The coding agent writes `docs/phases/PXX-plan.md` before any code and stops at the phase exit gate (§13 of the phase file plus §15 of this file). Commit this file as `docs/00-master-prompt.md` and the Ecosystem Integration Specification v1.1 unchanged as `docs/ecosystem/infrabyx-integration-spec.md` in Session 1.

> **What v1.1 changes (management instruction of 25 October 2026: "go through all the attached files again, improvise the logics and workflow, add the details, make the system future ready, improve the logics, make the workflow faster, include customisations, fix errors, explore other GRC platforms and client feedback, reverse-engineer existing products, and make the product able to support global compliances, studying how Lawrbit serves companies abroad").** Every file was re-read against the owner's attached Architecture Parts 1–3, the earlier master prompt and the Excel samples (Appendix AC, 1,069 traceability rows); every phase and appendix was improved in place, with changes marked *(v1.1)* and a "v1.1 changes" list under each header. New: **P25** Global Jurisdiction Packs, Multi-Region and Partner Network; **P26** Litigation, Legal Matters, Contracts, Licences and Ethics Registers; **P27** ESG, BRSR, CSR and Sustainability; **P28** Reports, MIS and Board-Pack Studio; **Appendix Y** Global expansion (Lawrbit delivery model analysed); **Z** Customer feedback, reverse engineering and the 142-item improvement backlog; **AA** Future-ready AI and agentic architecture (agent workforce, autonomy levels L0–L4, MCP server and client, A2A, AI governance overlay); **AB** RBI consolidated directions content plan; **AC** baseline and brief traceability matrix; the **RBI Directions Catalogue** workbook (320 rows); three new Excel template families (INTL-GEN, AI-GOV, ESG-BRSR; 27 in total); NN-47–NN-55; D-34–D-48; X-42–X-60.

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

Each NN rule has at least one automated test named `NN-xx_*`. A failing NN test blocks release. NN-33 to NN-46 consolidate the rules proposed by the twelve authoring streams on 25 October 2026 (`02` §3.3); NN-47 to NN-55 were added in v1.1 (`02` §3.4).

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
| NN-35 | **Template contract.** Rows 1–2 and columns A–AD of the question template are immutable (changed only by a management-approved major template version). The nine base departments, six compliance types, three risk levels and eleven frequencies exist in every family and are never renamed or removed; families only add values; deprecated values are end-dated with aliases. |
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

`authority` (RBI, SEBI, IFSCA, IRDAI, MCA, MeitY, CERT-In, MoLE, CRCS, State RCS, CBIC, CBDT, ICAI, ICSI, foreign authorities) → `instrument` (Act, Rules, Regulations, Master Direction, Master Circular, circular, notification, guideline, FAQ, standard) → `instrument_version` (issue date, effective date, amendment chain, source file, hash, retrieval date) → `clause` (paragraph tree with text and hash) → **`checkpoint`** (one Excel row = one checkpoint = one actionable; carries the canonical `obligation_ref` `<AUTH>/<instrument code>/<version>#<para>` used across the ecosystem as `Obligation`) → `control_activity` and `evidence_expectation` → `applicability_rule` (P15 engine). Checkpoints carry every Excel column (Appendix E): short title, question, frequency/due rule, clause, explanation, department code, related documents, compliance type, filing details, consequences, risk, conditional applicability, evidence, control activity.

### 6.2 Tenant compliance (`cmp`)

`entity_profile` (family, type, layer/tier, attributes; P15) → `adoption` (instrument packs the tenant has selected, with checkbox state, date and actor) → `tenant_overlay` (edited text, added checkpoints, renamed departments, changed owners — never overwriting the base; NN-03) → `compliance_instance` (checkpoint × period × legal entity × owner, with pinned content version, computed statutory due date and internal target date) → `submission` (maker status, comments, evidence links) → `review` (checker decision approve/reject/reallocate, comments) → `audit_review` (auditor comments) → `attestation`, `exception`, `waiver`, `extension`, `issue`.

### 6.3 Canonical compliance statuses (Locked; tenants relabel only)

`not_started`, `in_progress`, `in_progress_interim`, `waiting`, `submitted_for_review`, `returned`, `complied`, `complied_late`, `partially_complied`, `not_complied`, `not_applicable`, `exempted`, `deferred_by_regulator`, `withdrawn`. "Overdue" is a computed flag, not a status (Appendix A §A.0.5). Excel column J stays blank in templates; the importer maps tenant labels to canonical values.

### 6.4 Open, interim and "waiting on others" items (R-039)

The brief asked that open items, interim items and items waiting on someone else be fully customisable. They are, within limits: tenants define their own interim and waiting sub-statuses, reasons, owners, reminder ladders, SLAs, escalation paths and labels (T tier), and platform defaults ship per family. What is **not** customisable is the statutory clock: waiting pauses internal targets only (NN-33), and canonical statuses remain the reporting basis (§6.3). Platform open items in this pack (Appendix W) are classified by configurability so that most can be closed by a Governed change, not a code release (P02).

### 6.5 Other core aggregates

Governance (`gov`: entity master, directors, KMP, committees, meetings, agenda, minutes, resolutions, registers, filings) · policies (`pol`: policy, version, approval, attestation) · documents (`dms`: document, version, rendition, envelope, share, retention, legal hold) · risk (`erm`, `ral`: risk, control, RCSA, KRI, loss event, appetite, scenario, run, result, ICAAP) · audit (`aud`) · returns (`ret`, `acc`) · data protection (`dpc`) · vendors (`tpr`) · people (`hr`, `lab`) · grievance (`grv`) · co-operatives (`coop`) · AI (`ai`) · integration (`int`) · portability (`xpt`) · commerce (`bil`, `mkp`, `sdc`) · public (`web`, `hlp`). Each phase file §7 lists its tables.

### 6.6 Correction Entry (D-02; P00, P02 §4O, Appendix A §A.5)

Scopes: `RECORD_FIELD`, `DOCUMENT_VERSION`, `CONTENT`, `AUDIT_ANNOTATION`, `SETTING`, `ENTITLEMENT`, `MASTER_DATA`, `DATE`, `REVERSAL`. Fields: target, old value (sealed), new value, `effective_at`, `recorded_at` (system, never editable), reason code, free-text reason, requester, approver (≠ requester), tenant acknowledgement (required before effect for master data and document versions), legal-hold check. Tenants use the same mechanism for their own corrections. The super-admin "overwrite anything" requirement (R-068, R-071, R-074) is met entirely through this mechanism. **Emergency path** (lock-out or security incident only; P02 FR-P02-67, Appendix A §A.5): one `plt_super_admin` with an incident ID may apply a reversible correction immediately; it is auto-reverted unless a second approver ratifies it within 24 hours, and the tenant is notified either way. Trial extensions are `ENTITLEMENT` corrections or approved promo rules.

---

## 7. Regulatory baseline as of 25 October 2026 (re-verify before each dependent feature)

These dated facts shape the product. They were checked by the authoring streams on 25 October 2026 against the sources in each phase file §15; items still marked [VERIFY] there remain flags.

| Area | Fact the build must reflect |
|---|---|
| RBI consolidation — the RBI content base *(v1.1)* | On **28 November 2025** RBI's Department of Regulation issued its consolidated Master Directions for eleven RE categories, withdrawing more than 9,000 circulars, under the naming "Reserve Bank of India (<RE> – <Subject>) Directions, 2025", with a savings clause. RBI's press release counts **238** function-wise directions; circular RBI/2025-26/100 counts **244** Master Directions (serials RBI/DOR/2025-26/143–386) and 9,445 circulars withdrawn; **240** remain live after four dividend directions were replaced on 10 Mar 2026. **These consolidated directions (with their later amendments), together with the DoS directions of 31 Jul 2026 and the CEPD Internal Ombudsman directions and RB-IOS 2026, are the only RBI instruments loaded into the content library (D-39).** The full list is pre-seeded from `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx` (320 rows; reference numbers derived from RBI serials and marked [VERIFY] until read on each document); the NBFC category has 35 consolidated directions (46 rows including DoS and CEPD). Examples: NBFC Governance RBI/DOR/2025-26/344; NBFC Capital Adequacy /345; NBFC IRACP /356; NBFC ALM /355; NBFC Outsourcing /363; UCB Governance /273; UCB Capital /275; Commercial Bank Capital /151 (updated 7 Oct 2026). P05 maps old circular paragraphs to the new paragraphs and re-cites existing checkpoints automatically (Appendix AB). |
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
| P00 Foundations, repository discovery and migration | `phases/P00_…` | — | 4 × 7 | A Platform | 1 |
| P01 Identity, tenancy, onboarding and access | `phases/P01_…` | P00 | 5 × 8 | A | 1 |
| P02 Configuration Studio, rule engine and settings | `phases/P02_…` | P00, P01 | 6 × 8 | A (config sub-squad) | 1 |
| P03 Regulatory content library, template registry and Excel import | `phases/P03_…` | P00–P02 | 8 × 8 *(v1.1: RBI catalogue pre-seed, control layer, tracker import, undo)* | B Content & Compliance | 1 |
| P04 Compliance workspace, maker-checker, calendar, tasks, notifications | `phases/P04_…` | P00–P03 | 11 × 9 *(v1.1: automated checkpoints, testing cycles, notification budget, grid bulk edit)* | B | 1 |
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
| P23 Public website, health check, help centre, tutorials, accessibility | `phases/P23_…` | P01, P15, P18, P20 | 10 × 7 *(v1.1: locales, country pages, RBI Directions Tracker)* | F (growth) | 1 |
| P24 Engineering governance, hardening, certification readiness, go-live | `phases/P24_…` | every phase released | 3 × 4 governance track + 4 × 7 per GA, 1 sprint per later re-run | A + security | 1, 2, 3 |
| P25 Global jurisdiction packs, multi-region and partner network *(v1.1)* | `phases/P25_…` | P03, P05, P15, P18, P19, P20, P21, P24 | 10 × 9 | I Global | 4 |
| P26 Litigation, legal matters, contracts, licences and ethics registers *(v1.1)* | `phases/P26_…` | P00–P04, P07, P18 | 9 × 8 | H Legal & ESG | 2 |
| P27 ESG, BRSR, CSR and sustainability *(v1.1)* | `phases/P27_…` | P00–P04, P06, P11, P28 | 9 × 8 | H | 3 |
| P28 Reports, MIS and board-pack studio *(v1.1)* | `phases/P28_…` | P00–P04 (core); P06, P08–P11 (packs) | 9 × 8 | D (core track Wave 1, studio Wave 2) | 1 → 2 |

### 13.2 Order and waves

- **Order:** P00 → P01 → P02 → (P03 → P04 → P05) with P15 alongside P03, P17 sprint 1 alongside P04, P18/P19 core alongside P03–P04, P06/P07 from P04's interface freeze, P20/P23 on the growth squad from P02 → **P24 (GA)**.
- **Wave 1 — "Compliance Core" GA (about sprints S1–S27; v1.1 adds the P28 core track for dashboards and the one-page compliance summary and enlarges P03–P05: P00 S1–S4, P01 S5–S9, P02 S8–S13, P03 S10–S17, P04 S13–S23, P05 S17–S25, P24 S24–S27):** P00–P07, P15 (first four families), P17 runtime, P18 core, P19 core, P20, P23, P24. This is the minimum that lets a Middle-Layer NBFC, a company and an IFSCA entity self-onboard, buy, run compliance with maker-checker, receive regulatory updates, run board meetings and policies, and export everything.
- **Wave 2 — "Risk, Audit, Returns, Data, Legal" (about S18–S40):** P08, P09, P10, P11, P12 (incl. `OV_AI`), P14, P26, P28 studio, the rest of P15, P17 notebooks and agents, P18/P19 full. Return generation ships first for NBFC, ARC and co-operative families; bank, UCB, IRDAI, SEBI and IFSCA return generation stays `ACTIVE_UNVERIFIED` (calendar, evidence, reconciliation and secondary validation only) until a pilot verifies cell maps (X-32).
- **Wave 3 — "People, Co-operatives, Services, ESG" (about S28–S48):** P13, P16, P21, P22, P27, P17 full agent workforce.
- **Wave 4 — "Global" *(v1.1)* (about S40–S54):** P25 — regional cell framework, global entity management, partner portal, first corridor packs (UAE and Singapore, then UK/EU), Arabic right-to-left; P24 run per cell.
- Each wave ends with a P24 run. A phase released after GA re-runs the P24 checklist for its scope.
- **Squads:** A Platform (8), B Content & Compliance (9), C Governance & Documents (8), D Risk & Reporting (9), E AI (9), F Commercial & Growth (8), G People & Co-operatives (9), *(v1.1)* H Legal & ESG (8), I Global (9), plus a standing content team (CS, CA, regulatory writers) that produces Part-2 question sheets and reviews packs. About 250 squad-sprints in total *(v1.1)*. With fewer squads, run waves sequentially and expect roughly 75–90 sprints.

### 13.3 Part 2 (question sheets) runs in parallel

Part 2 is produced in separate Claude chats using `templates/` (27 families, v1.1) and `part2_prompts/`; for RBI families work through `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx` wave by wave (Appendix AB). Sheets are imported through P03 once its importer exits; before that, they are validated with `templates/_validate_templates.py`. P05's AI Question Authoring Studio later runs the same method inside the product (R-085).

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
- *(v1.1)* `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx` (the RBI content base, D-39); Appendix AC (traceability of every baseline section and brief item to the pack); Appendix Z backlog; Appendix Y Lawrbit analysis.
- Primary legal sources as cited in each phase file §15 and Appendices F, G, I, J.

---

## 17. Glossary (short; the full glossary is the "i" registry, P23 and Appendix P)

**Checkpoint** — one actionable row of a question sheet. **Compliance instance** — a checkpoint for a period, entity and owner. **Overlay** — a tenant's change to base content. **Pack** — a set of instruments and rules for a family or overlay. **Family** — an entity category with its own logic (P15). **Correction Entry** — the only way to change a recorded value (§6.6). **Updates / Notifications** — regulatory inbox / work inbox (NN-27). **RE** — regulated entity. **SBR** — RBI Scale Based Regulation for NBFCs (Base, Middle, Upper, Top layers). **ICAAP** — Internal Capital Adequacy Assessment Process (Pillar 2). **RCSA** — risk and control self-assessment. **KRI** — key risk indicator. **RBIA** — risk-based internal audit. **CIMS / DAKSH / PRAVAAH** — RBI's supervisory data, supervisory workflow and regulatory application portals. **CIC** — credit information company (TransUnion CIBIL, CRIF High Mark, Experian, Equifax). **GRO / PNO / IO** — grievance redressal officer / principal nodal officer / internal ombudsman. **SDD** — structured digital database under SEBI PIT. **ESP / ASP** — eSign service provider / application service provider. **OH** — Infrabyx Operations Hub. **Vidhi AI** — LDC's AI employee and agent workforce. *(v1.1)* **Compliance Score** (P04) — completion and timeliness of a tenant's compliance instances; **Health Check Score** (P23) — result of the free health check; **Set-up Readiness Score** (P01) — onboarding completeness; **Compliance Health Index** (P28) — weighted board-level index (40/20/15/15/10). **Autonomy level** — L0–L4 ceiling for AI actions. **MCP** — Model Context Protocol. **A2A** — Agent2Agent protocol. **Jurisdiction pack** — country content pack. **Linked tenant** — a tenant in another regional cell that belongs to the same group. **Act date** — the date an obligation was actually performed.

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
| X-08 | **Multi-value delimiter** in Excel columns C and D is `"; "` (as in the owner's 2,809 finished IFSCA rows); the importer also accepts `" \| "`, `","` and line breaks and normalises; `" \| "` remains the separator inside column N. Supersedes Appendix E references to `" \| "` for C/D in `_conventions.md`. |
| X-09 | **Family and template codes.** P15 entity-family codes (`BANK`, `UCB`, `RCB`, `NBFC`, `ARC`, `AIFI`, `PAY`, `CCS`, `COOP`, `IFSC`, `MF`, `AIF`, `LISTED`, `REIT_INVIT`, `SEBI_INT`, `INSURER`, `INS_INT`, `COMPANY`, `LLP`, `SOCIETY`, overlays `OV_*`) map to the template codes of Appendix E as shown in §1.2 (24 in v1.0; 27 in v1.1 with INTL-GEN, AI-GOV and ESG-BRSR, X-51); template files are named `LDC-TPL-<FAMILY>-v1.0 - <Name>.xlsx`. Data-intake templates use `LDC-DT-<AREA>` (P11 owns the common set — e.g., `LDC-DT-TB`, `LDC-DT-LOAN`, `LDC-DT-INVEST`, `LDC-DT-CAPITAL`; P09 adds `LDC-DT-RAL-LOANSEG`, `-HQLA`, `-OBS`, `-INS`, `-COOP`; P08 `LDC-DT-KRI`; P12 `LDC-DT-ROPA`; one upload feeds both Return Studio and Risk Lab). |
| X-10 | **Departments.** Excel column M names map to canonical codes per Appendix U §U.9.0 (22 base codes + 12 added: CLM, KYC, ICP, INV, MKT, PRL, PRD, SRV, TAX, TRS, UND, VAL). |
| X-11 | **Statuses.** §6.3 canonical set; Excel column J blank in templates. |
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
| X-29 | **Structured data inside the 30 columns.** Due-date rule in column P after `Due:`; retirement by `[RETIRED] ` prefix in column F (rows never deleted); CompID in column E as `<FAMILY>.<INST>.<NNNN>` (tenant rows `T-<TEN>.<INST>.<NNNN>`); `[VERIFY]` blocks publication (Appendix E). |
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
| X-51 | *(v1.1)* **Template families** are 27 (24 + INTL-GEN, AI-GOV, ESG-BRSR); run the validator with both owner samples; family codes PFRDA, MSME_FIRM and AML_RE are reserved. |
| X-52 | *(v1.1)* **RBI counts:** cite "238 (press release) / 244 serials, 240 live" as in §7; NBFC consolidated directions = 35; catalogue = 320 rows (D-39). |
| X-53 | *(v1.1)* **Kill-switch drills** quarterly at platform level for all tenants; tenant-level drills for Enterprise (NN-51). |
| X-54 | *(v1.1)* **Tracker import** screen is SCR-CNT-16 (P03), launched from P01 onboarding; SCR-IAM-69 is an alias. |
| X-55 | *(v1.1)* **New data class** `LEGAL_PRIVILEGED` (key separation like BOARD_CONFIDENTIAL; excluded from grants and AI for non-legal users); Ecosystem CR raised. |
| X-56 | *(v1.1)* **IFSCA** entity list has 40 types (owner's Appointed Actuary sheet vocabulary, X-38). |
| X-57 | *(v1.1)* **Baseline corrections:** Ind AS 37 classes follow the standard, not fixed probability bands; BRSR value-chain scope per SEBI's 28 Mar 2025 circular (2% partner threshold). |
| X-58 | *(v1.1)* **Department codes** `ESG`, `LEGL` added and used by P26/P27 and ESG-BRSR; `AIG` reserved for tenants that create an AI governance department (AI-GOV column M maps to DPR, ISEC, PRD, IA). |
| X-59 | *(v1.1)* **Support SLAs** have one source — the OH6 SLA table — shown in P20 plans and P22 delivery. |
| X-60 | *(v1.1)* **Work Inbox** is SCR-WF-00 everywhere (SCR-CMP-02 retired). |

---

## 19. Changes required in companion documents

**Ecosystem Integration Specification v1.2 change requests (Spec §14.2), raised in P00 and tracked in `docs/ecosystem/change-requests.md`:** (1) §9.3 — LDC stack is NestJS/PostgreSQL, not "Node, TypeScript, MongoDB"; (2) data classes SEALED, BOARD_CONFIDENTIAL, CREDENTIAL, REGULATOR_CONFIDENTIAL; (3) supervisor grantee and basis codes for SEBI, IRDAI, IFSCA, CRCS/State RCS in §4.7; (4) `RiskSegmentSnapshotPublished` event and Finbyx `POST /v1/risk/stress-runs`; (5) evidence-request API for audit (`POST /v1/evidence-requests`); (6) LDC as producer of `FinancialStatementsApproved`, `Return*` and `Bureau*` events for non-Finbyx tenants; (7) about twelve Operations Hub contracts listed in Appendix X §X.12 (`TenantSelfServeCreated`, trial events, `CatalogueVersionPublished`, `CatalogueChangeRequestUpdated`, `ServiceCreditIssued`, `ClientHealthSignal`, `TimesheetAggregated`, `DeliveryMetricsMonthly`, `POST /v1/crm/activities`, `POST /v1/delivery/assignments`, `POST /v1/trials/extensions`, `POST /v1/conflicts/check` for LDC, `POST /v1/catalogue/change-requests`); (8) co-operative member contracts when `coop.sor.members = LDC` (§6.24 producer).

*(v1.1)* Further change requests: (9) `dataregion` residency attribute on every cross-product event; (10) A2A transport, agent identity and delegation tokens for ecosystem agents; (11) `LegalMatterExposureSummarised`, `RegulatorObservationOpened`, `RegulatorObservationClosed` (LDC producer); (12) `FinancedEmissionsAggregatePublished` (Finbyx producer) for P27; (13) data class `LEGAL_PRIVILEGED`; (14) the v1.1 Operations Hub contracts in Appendix X (practitioner-firm accounts, partner network, multi-currency catalogue, AI-credit metering).

**Finbyx addendum:** respect `ral.icaap.host`, `aud.host.mode`, the returns and risk kernels, and `coop.sor.members`.

**Operations Hub addendum:** Appendix X (v1.1 rows added for global delivery, partners, practitioner firms and AI credits) (LDC workspace, CRM objects, onboarding playbooks, CS signals, ticket routing, health-check leads, catalogue items, RM roles, cross-company roles, trial acceptance, second pricing approver).

---

## 20. Management decisions

The decisions of 25 October 2026 (D-01–D-21 as amended by X-03–X-05), the decisions added by this pack (D-22–D-33), the v1.1 decisions (D-34–D-48), the owner decisions still pending and the twelve recorded challenges to the brief are in `02` §2–§4. They bind every phase.
