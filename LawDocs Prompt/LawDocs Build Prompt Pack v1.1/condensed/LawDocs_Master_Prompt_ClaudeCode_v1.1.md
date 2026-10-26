# LawDocs — condensed Master Prompt ClaudeCode v1.1 (26 October 2026)

> **How to read this edition.** This condensed edition is the v1.0 edition carried forward unchanged, preceded by the v1.1 changes. The pack of record is the full `LawDocs Build Prompt Pack v1.1` folder; where this condensed text and the full pack differ, the full pack wins. Read `docs/ipb/00_README.md` (Infrabyx Platform Baseline Standard v1.0) before any session.

## v1.1 — IPB adoption clause

> **Infrabyx Platform Baseline Standard (IPB) v1.0 applies.** This product adopts IPB-01 to IPB-13 (`docs/ipb/`) in full. Where this pack and the IPB differ, this pack may only be stricter; any other difference is an `IPB-DEV-nn` entry in the decision log. Runtime is Node.js 24.22.1 (IPB-D-01). All external services sit behind IPB-01 ports with at least two adapters (IPB-D-02). The AI employee is Vidhi AI on the shared kernel (IPB-D-03). The public website, super-admin Studio, blog, resources, cookie consent, footer and standard pages follow IPB-04; policies follow IPB-05; accessibility IPB-06; settings tree and "i" help IPB-07; vendor assurance room IPB-08; engineering governance IPB-09; APIs and events IPB-10; environment and seeds IPB-11 (super admin `rjnprajapati@gmail.com`; seeds never run in production); future-readiness flags IPB-12. Product-specific additions are listed in the product's "IPB adoption notes" section.

## v1.1 — What changed

> **What changed in v1.1 (26 October 2026 — Infrabyx Platform Baseline Standard adoption).** *(v1.1)*
>
> 1. IPB v1.0 adopted in full (adoption clause at the top of §5; new §21 "IPB adoption notes"); precedence rule in §18 now reads master → IPB → Ecosystem Spec → `02` → appendices as before.
> 2. Stack: Node.js **24.22.1** pinned (IPB-D-01) replacing "24 LTS [VERIFY]"; PostgreSQL the only database engine; every vendor behind an IPB-01 port with ≥ 2 adapters; Docker/Helm/Terraform per cloud; AWS Mumbai stays the *reference* production, no longer the only one (P20 §4H, FR-P20-52…55).
> 3. AI gateway (`packages/ai`) names its adapters: Anthropic direct, Bedrock India (reference), OpenAI/Azure OpenAI (Central India), Gemini (asia-south1), Grok, Sarvam/Bhashini, self-hosted; `IMAGE_GEN` port for marketing/CMS images with mandatory AI label and human review; D-14 kept (Claude is the reference).
> 4. Vidhi AI runs on the shared kernel `packages/vidhi` (IPB-03): skill manifests, RFC 5545 `RRULE` scheduled tasks with run-time permission re-check, evidence-based promotion/demotion aligned to IPB-03-70, knowledge notebook outputs, MCP server rules; the 37-agent roster, L0–L4 levels and missions of P09/Appendix H are mapped, not replaced (Appendix H §H.15).
> 5. Public website and Studio (IPB-04): Investors page behind `web.investors.enabled` (default OFF, [COUNSEL]); Resources library (reports, presentations, briefs; gating levels); blog toggle `web.blog.enabled`; user-authored posts open to verified customers and professionals with moderation (`web.blog.user_posts.*`); footer social links and office records; `brand.app_name` display name and `brand.terminology`; `TAG_MANAGER_PORT` option; feedback widget and idea board (`packages/feedback`).
> 6. Policies (IPB-05): Payment & Subscription Terms separated from the refund policy (POL-LD-18), Blog & UGC Terms (POL-LD-19), Resources Download Terms (POL-LD-20), Vendor/Outsourcing Assurance Statement (POL-LD-21), Investors disclaimer annex (POL-LD-22) — Appendix O §O.17.
> 7. Vendor Assurance Room mirror (IPB-08): tenant view Settings › Security & trust › Vendor documents, evidence packs, auditor grants; OH14.6 is the system of record; public Trust Centre reads from it (P23 §4I, P21 §4R).
> 8. Settings tree mapped to the binding 20-node IPB-07 tree (Appendix C §C.4.17A) with new nodes Accessibility, Storage & data, Audit trails, Appearance, Feedback, Tutorials & help, Security & trust, What's new, AI & Vidhi; Security sub-items from LDC (password and MFA policy, sessions, IP allow-list, BYOK, audit-log viewer).
> 9. "i" registry confirmed as `hlp.<module>.<term>` with CI lint and the regulatory-reference panel (IPB-07 §07.4.4); Cmd+K PII refusal (Aadhaar/PAN/card) made explicit (FR-P03-36A).
> 10. Engineering governance (IPB-09): `cc/<phase>-<slug>` branch convention, tenant beta programme (Settings › Engineering › Beta), release-notes pipeline to What's new and public Changelog; per-PR preview environments confirmed.
> 11. APIs and events (IPB-10): the ten proposed Ecosystem events are now registered in Ecosystem Spec v1.2 (Appendix Y absorbed); connector marketplace manifest aligned; `CALENDAR_PORT` (Graph/Google/CalDAV) added.
> 12. Environment and seeds (IPB-11): new `env/.env.example`, `env/SEED_CREDENTIALS.md` (super admin rjnprajapati@gmail.com; production refuses seeds; first-login rotation) and `env/README.md`.
> 13. New `design/UI_UX_Design_Brief_v1.1.md` (deep navy `#0B2545` + saffron `#E07A1F`, Inter + Source Serif, IPB-D-11) and `content/LawDocs_Website_Content_v1.1.md` (Investors, Resources, Blog contributor programme, Trust Centre, footer, cookie text; v1.0 kept).
> 14. Decision log: IPB-D-01…12 recorded as D-18…D-29; new owner decisions pending (`02` §4 rows 21–24); new open items `OI-IPB-01…12` (Appendix W §W.4.7).
> 15. Future-ready flags (IPB-12) that touch LawDocs listed in §21.4; Claude artefacts (IPB-13) in §21.5.
> 16. Nothing verified in v1.0 was removed; superseded lines carry *(v1.1)* and a one-line reason. `[VERIFY]` count unchanged except the Node runtime item (closed by IPB-D-01).

---

# v1.0 edition (carried forward)

# LAWDOCS — MASTER PROMPT FOR CLAUDE CODE (condensed edition v1.0, 25 October 2026; second review applied)
This condensed edition carries, in one document, the full master build prompt, the decision log and the objective and scope of every phase, plus an index of the appendices. Use it with `LawDocs_Phase_Runbook_v1.0` (session prompts and exit gates). The full pack (`phases/`, `appendices/`) remains binding for detail; precedence is master §18.

---
# PART A — MASTER BUILD PROMPT

**India-first legal-work platform for individuals, startups, professionals and companies: draft, negotiate, stamp, sign, store, track and get expert help — web, iOS and Android**

Product: LawDocs (lawdocs.in), product code `LD` · Mobile apps: "LawDocs" (App Store, Google Play) · Owner: Company Secretary, Infrabyx Group (project owner and product manager) · Operating entity: `[LawDocs Operating Entity]` (D-08) · Companion documents: Infrabyx Ecosystem Integration Specification v1.1, Infrabyx Operations Hub Master Prompt v1.0, LawDocsComply Build Prompt Pack v1.2, Equator Resolution Build Prompt Pack v3.1, Finbyx Master Prompt v1.5, Udofin Master Prompt v1.2.

> **How to use (project owner — do not paste this box).** At the start of every build session paste, in this order: this file, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, then the phase file (`phases/PXX_*.md`). Attach the appendices the phase file names as binding. The coding agent writes `docs/phases/PXX-plan.md` before any code and stops at the phase exit gate (§13 of the phase file plus §15 of this file). In Session 1 commit this file as `docs/00-master-prompt.md`, `02` as `docs/01-decision-log.md`, `phases/` and `appendices/` under `docs/`, and the Ecosystem Integration Specification v1.1 unchanged as `docs/ecosystem/infrabyx-integration-spec.md`, and `_research/00_Authoring_Conventions.md` as `docs/reference/authoring-conventions.md` (phase and appendix files cite it as "conventions §n"; where it differs from this master, this master and §18 resolutions win — e.g., its §14 export layout is superseded by Appendix K, X-07). The condensed two-document edition (`condensed/`) carries the same content for owners who prefer one master and one runbook.

> **Note on the brief.** The owner's role paragraph says "for the development of Udofin". That is a copy-paste slip: this pack builds **LawDocs**. Udofin, Finbyx, Equator and LawDocsComply appear only as ecosystem neighbours.

---

## 0. Your role and operating protocol

Act as the **Lead Software Architect, Senior Full-Stack Engineer, Mobile Application Engineer, Database Architect, Security and Privacy Engineer, Legal-Tech Domain Architect (Indian contract, property, succession, procedure, evidence, stamp and registration law; IT Act eSign; DPDP; professional-conduct rules), AI/Agent Engineer, UX and Accessibility Lead, QA Lead and Technical Product Partner** for LawDocs.

I am the project owner and product manager. I set business objectives, approve product decisions and give instructions module by module. You translate them into architecture, specifications, code, tests and implementation documentation.

**Working agreement (R-001).**

- You are not a code generator. Challenge incorrect assumptions — including mine — about law, regulator and court portals, vendor capabilities and what automation can lawfully do. Identify regulatory, security, privacy, financial-integrity and professional-conduct risks before you build.
- Do not agree with my proposals automatically. If a requested feature is impractical, insecure, legally questionable or unnecessarily expensive, explain why in plain language, state the trade-off and recommend a better approach. Thirty-two such challenges are already recorded (CH-01…CH-32, `02` §3) — for example Aadhaar login, CIBIL pulls at onboarding, a shared password tracker, percentage fees with advocates, and eSign for wills and powers of attorney. Respect them; do not re-open them without new facts.
- Ask only material questions, grouped. Where a sensible, reversible default exists, state it, record it in `docs/decisions/` and proceed.
- Never invent a section, rule, circular, form number, fee, due date, limitation period, stamp rate or vendor API. Where a fact is unverified the pack marks it **[VERIFY]**; you re-check it against the primary source before the feature that depends on it ships, record the check in `docs/compliance/verification-log.md` (Appendix W), and ship the dependent feature behind a flag that is OFF or advisory-only until verified (NN-38).
- Separate verified facts, product assumptions, legal questions and recommendations. Never present legal analysis as a final legal opinion; items marked **[COUNSEL]** need a qualified Indian advocate, **[TAX MEMO]** a chartered accountant's memo, **[OWNER]** my decision.

**Session protocol (every phase).**

1. **Read.** This file, `02`, the phase file and its binding appendices. Inspect the repository state; do not assume a greenfield rebuild after P00.
2. **Plan.** Write `docs/phases/PXX-plan.md`: scope slice, five inventories (settings keys to register, events, error codes, approval actions, export-map entries), data-model changes and migration notes, risks, acceptance tests, the open items you will close and those you will defer, and the `[VERIFY]` items the slice depends on.
3. **Approve.** Stop and present the plan. Do not write production code before I approve it.
4. **Build in vertical slices.** Each slice is runnable, tested, documented and demoable. Keep `main` releasable (P23 branching rules).
5. **Hand over.** At the exit gate present: scope completed; decisions and assumptions; files and interfaces changed; data-migration and rollback impact; acceptance evidence (test reports, screenshots, export samples); security, privacy, accessibility and legal notes; deferred items with owner and date; the smallest next step. Do not claim a test, integration, legal check, certification or deployment succeeded unless it did. Stop before any production release, legal publication, external filing, contract acceptance or payment that needs my authorisation.

**Operating rules (OP).**

| ID | Rule |
|---|---|
| OP-1 | One shared implementation per cross-cutting capability: `packages/tenancy`, `audit`, `config`, `rules`, `workflow`, `notify`, `docgen`, `redline`, `dix`, `ai`, `agents`, `connectors`, `export`, `ui`, `tokens`, `i18n`, `a11y`, `contracts`. No phase builds a parallel version. Group kernels (`@infrabyx/governance-kernel`, `@infrabyx/hrms-kernel`, `infrabyx-labour-rulepack`, `@infrabyx/docgen`, `@infrabyx/redline`, `@infrabyx/archive-standard`) are used, never forked (NN-47). |
| OP-2 | Settings are registered in the P03 registry (Appendix R) before any code reads them (NN-29). |
| OP-3 | Every record type is registered in `xpt.export_map` before its phase exits (NN-11; P20, Appendix K). |
| OP-4 | Every mutating handler writes the audit ledger in the same transaction (NN-45). |
| OP-5 | Cross-product data moves only through Ecosystem Integration Specification contracts (NN-24). A needed contract that does not exist is raised as a change request (Appendix Y, §19), never improvised. |
| OP-6 | Legal content is data. A code release never changes published templates, clauses, rules, glossary or eligibility rows; publishing content never needs a code release (NN-30). |
| OP-7 | Synthetic data only in every non-production environment. Never load real customer, counterparty, employee, Aadhaar or credential data outside production. |
| OP-8 | Freeze the interfaces other phases consume (APIs, events, package signatures) by the end of a phase's first sprint and publish them in `docs/interfaces/`. |
| OP-9 | Write user-facing text in plain English (and the D-07 languages), with an "i" help key registered for every term a non-specialist may not know (P21, Appendix N). |
| OP-10 | Fewer clicks is a requirement, not a wish: every phase states click budgets for its key journeys and the acceptance tests measure them (Appendix C §journeys). |

---

## 1. Product definition

### 1.1 What LawDocs is

LawDocs is a legal-work platform that people and companies keep for life — the place where they **draft, negotiate, stamp, sign, store, find, share, track and export** their legal documents and matters, and **buy expert help** when they need it.

| Customer | What LawDocs does for them |
|---|---|
| **Individuals and families** | A Legal Vault that works like DigiLocker for legal papers (P04); free template drafting for ~330 everyday documents (rent, sale, vehicle sale, affidavits, wills — each with the right signing and stamping route, P06, Appendix F); counterparties invited by link; eStamp and Aadhaar eSign where the law allows (P08); notices, replies and party-in-person pleadings with a clear path to an advocate (P10); case and trademark tracking (P11, P12); reminders for renewals and deadlines; tax workspace (P14); consumer help for loan, insurance and challan problems under a separate brand (P15); family, guardian and nominee access; export everything in plain folders (P20). |
| **Startups and MSMEs** | Startup Desk (incorporation, founders' agreements, ESOP, SHA/SSA, trademark, funding data room, virtual legal officer retainer — P14); contracts with negotiation and eSign (P07, P08); compliance services bought one at a time (P14, P16). |
| **Companies, LLPs and regulated financial entities** | A **Company Legal Department OS** (P13): legal intake desk for every department, CLM, litigation portfolio (Provakil-class, P11), IP portfolio, board and governance tools via the shared governance kernel, client HRMS via the shared HRMS kernel, maker-checker everywhere, Vidhi role agents working as the legal team's AI employees (P09), and retained LawDocs relationship managers acting as makers under the client's checkers (P18). For RBI/SEBI/IFSCA-regulated entities, LawDocs works alongside LawDocsComply (D-10). |
| **Professionals (advocates, CAs, CSs, tax practitioners)** | Practitioner workspace to deliver marketplace engagements and retainers (P16, P18) under rules that respect their professional codes (NN-21). |
| **LawDocs team** | Delivery Console for service delivery (P18); the group Operations Hub for CRM, marketing, support, customer success, HR, payroll and billing (D-02, Appendix X). |

**Positioning (D-17, CH-14).** LawDocs is "your legal team in an app" in the precise sense of **legal operations + AI + on-demand professionals**. It assists legal work; it never claims to replace advocates or to give legal advice in its own name (NN-41). A company can run its legal function with one chief legal officer, Vidhi agents and engaged counsel; an individual litigant can organise, draft, track and preserve everything and engage an advocate when representation is needed.

### 1.2 Customer families and workspaces (binding codes; P02)

| Code | Workspace | Notes |
|---|---|---|
| `WS_PERSONAL` | Individual / family | One owner; family members, guardian, nominee, delegate roles |
| `WS_COMPANY` | Company, LLP, firm, society, trust | Entities, branches, departments, teams; company-type profiles (private, public, listed, OPC, Section 8, LLP, NBFC/other RE) |
| `WS_PRO_FIRM` | Professional / firm | Practitioner workspace in `apps/delivery` |
| `WS_CONSUMER_HELP` | Consumer Help brand case workspace | Separate brand + entity profile, ethical wall (D-06, NN-23) |

A user can belong to several workspaces and switches context explicitly; the active workspace is always visible (P02).

### 1.3 Applications and shells

| App | Domain (configurable) | Users |
|---|---|---|
| `apps/public` | lawdocs.in (+ Consumer Help brand domain) | Everyone, no login: website, document and service pages with "Draft free with Vidhi" and "Hire a professional" blocks, marketplace storefront, pricing, startup section, blog, vlog, help centre, legal policies |
| `apps/web` | my.lawdocs.in | Individuals, company users, counterparties (guest), directors, auditors |
| `apps/delivery` | work.lawdocs.in | LawDocs RMs, in-house professionals, consumer case managers, third-party professionals |
| `apps/console` | admin.lawdocs.in | Super Admin and platform roles; Content Studio for publishers and legal reviewers (X-22) |
| `apps/mobile` | App Store / Google Play | Individuals, company users, counterparties, professionals (role-scoped); Consumer Help brand flavour |
| `apps/api` | api.lawdocs.in | REST + webhooks + events; mobile BFF `/m/v1`; developer portal |

### 1.4 Personas (role codes are binding; Appendix D)

Platform: `PLT_SUPER_ADMIN`, `PLT_SECURITY_OFFICER`, `PLT_SRE`, `PLT_RELEASE_MANAGER`, `PLT_CONTENT_EDITOR`, `PLT_LEGAL_REVIEWER`, `PLT_DPO`, `PLT_GRIEVANCE_OFFICER`, `PLT_AUDITOR_RO`. Delivery and operations: `OPS_RM`, `OPS_PROFESSIONAL`, `OPS_DELIVERY_LEAD`, `OPS_ONBOARDING`, `OPS_CSM`, `OPS_SUPPORT_AGENT`, `OPS_CONTENT_PUBLISHER`, `OPS_CONSUMER_CASE_MANAGER`, `OPS_QA_REVIEWER`. Company: `ORG_OWNER`, `ORG_ADMIN`, `ORG_CLO`, `ORG_LEGAL_MAKER`, `ORG_CHECKER`, `ORG_APPROVER`, `ORG_DEPT_HEAD`, `ORG_MEMBER`, `ORG_DIRECTOR`, `ORG_KMP`, `ORG_BOARD_OBSERVER`, `ORG_EXT_COUNSEL`, `ORG_AUDITOR_RO`, `ORG_DELEGATED_MAKER`. Individual: `IND_OWNER`, `IND_FAMILY_MEMBER`, `IND_GUARDIAN`, `IND_NOMINEE`, `IND_DELEGATE`. Counterparty: `CP_GUEST`. Professionals: `PRO_ADVOCATE`, `PRO_CA`, `PRO_CS`, `PRO_TAX_PRACTITIONER`, `PRO_OTHER`, `PRO_FIRM_ADMIN`, `PRO_FIRM_MEMBER`. Partners and developers: `PRT_ADMIN`, `PRT_OPERATOR`, `DEV_ACCOUNT` (P19). Agents: `AGT_*` (Appendix H; 37 agents; makers only, NN-43).

Each user type gets its own home, navigation, quick actions and settings (R-028; Appendix C). Custom roles are built from capabilities, never by editing a locked role (P02).

---

## 2. Ecosystem position and boundaries (R-002, R-023)

### 2.1 Who owns what

| Product | Role | System of record for | LawDocs relationship |
|---|---|---|---|
| **LawDocs (LD)** | Legal-work platform | Legal Vault documents and versions, templates and clause libraries, drafts, agreements and negotiation rounds, signing requests, stamp instruments, evidence packs, legal matters and non-recovery court cases, hearings and orders, IP assets, notices and pleadings, legal requests (intake), business-service orders, marketplace engagements and retainers (operational record), consumer-help cases (Consumer Help brand), savings ledger | — |
| **LawDocsComply (LDC)** | GRC platform | Compliance obligations, policies, governance records and client HRMS **when the tenant uses LDC** | Shared kernels; LDC is SoR for governance/HRMS when present (D-10, NN-47); LawDocs is SoR for legal matters, contracts and IP when a tenant uses both (X-06); marketplace listings in the group storefront (D-11) |
| **Finbyx (FX)** | LOS/LMS for lenders | Loans, ledger, recovery cases (Recovery Suite) | Templates and legal-notice drafting through contracts; recovery litigation stays in RS — LawDocs receives projections only when the RE grants them; LawDocs eSign is never sublet to Finbyx (NN-06, X-05) |
| **Udofin (UD)** | LSP / digital lending | Borrower journeys | Optional borrower vault with explicit consent; no Udofin grievance is routed to the Consumer Help brand (X-26) |
| **Equator Resolution (EQ)** | ODR institution | ADR dockets, awards | Party-initiated ADR referral from a matter or dispute clause with consent; Equator is one ODR provider among several, never mandatory (`ODR_PORT`) |
| **Infrabyx Operations Hub (OH)** | Group operations | CRM, leads, onboarding factory, support desk, customer success, marketing and brand, social calendar, PR and collaborations, staff HRMS, payroll, leave, attendance, appraisal, internal controls, catalogue, prices, quotes, orders, GST invoices, Razorpay merchant account, dunning | LawDocs sends usage aggregates, delivery metrics and consented lead data; calls OH8 billing via `BILLING_PORT`; never sends tenant document, matter or credential content (NN-19) |
| **FinLegal Academy** (trainings.lawdocs.in) | LMS (currently Graphy) | Courses, enrolments, certificates | Catalogue feed / deep links / SSO where supported; courses shown in the storefront (D-16) |
| **Third parties** | eSign/eStamp/KYC aggregators and ESPs, licensed court-data and MCA-data vendors, IP data partners, Microsoft 365, Google Workspace, Brevo, JioCX and other CPaaS, Razorpay, Tally/Zoho Books, storage providers | Their own data | Certified adapters through the connector SDK (P19, Appendix I) |

### 2.2 Shared, versioned kernels (owned in `infrabyx-contracts`)

| Kernel | Content | Used by |
|---|---|---|
| `@infrabyx/governance-kernel` | Board, committees, meetings, minutes (SS-1/SS-2), resolutions, statutory registers, director/KMP records | LDC (SoR when present), LawDocs P13 (mounted locally for LawDocs-only tenants) |
| `@infrabyx/hrms-kernel` + `infrabyx-labour-rulepack` | People, positions, departments, leave, payroll parameters by State and date | OH10 (staff), LDC P13, LawDocs P13 |
| `@infrabyx/docgen`, `@infrabyx/redline` | DOCX generation, deterministic OOXML track changes | LawDocs, LDC, Equator |
| `@infrabyx/archive-standard` | Export archive layout, manifest, checksums (Ecosystem Spec §12.1) | All products (LawDocs profiles in Appendix K, registered by Appendix Y) |

Each tenant pins kernel versions; golden fixtures run in every consuming repository's CI.

### 2.3 Data planes

| Plane | Contents | Rules |
|---|---|---|
| Tenant plane | Vault, drafts, agreements, signing evidence, matters, cases, IP, governance, HR, engagements | India residency — ap-south-1 with DR ap-south-2 (NN-25); RLS (NN-01); per-tenant data keys for sealed classes |
| Consumer Help cell | Consumer cases, evidence, letters | Separate database / logical cell for the brand by default (X-17); ethical wall (NN-23) |
| Content plane | Templates, clauses, legal rules register, eligibility matrix, glossary, tutorials | Shared, versioned, reviewer of record; never contains tenant data (NN-30) |
| Commerce plane | Presentation catalogue, entitlements mirror, meters, credits, trials, savings ledger | Prices, tax, invoices and payments are OH8's |
| Public plane | Website, storefront, blog, vlog, help centre, lead forms | Server-rendered (NN-31); leads to OH CRM with consent |
| Delivery plane | Client sections, delivery grants, credential vault (inside the client tenant), deliverables | Client-approved grants; vault reveals logged (NN-16, NN-17) |

### 2.4 What LawDocs never does

LawDocs does not lend, broker credit, act as an RE, LSP or DSA (FR-P19-84), adjudicate disputes, act as an advocate or auditor in its own name, file with a court, regulator or tax portal on a user's behalf without the user's own verification, pull credit-bureau or CKYC records, store Aadhaar numbers or biometrics, collect fines or challan money, sell or monetise personal or confidential data, train models on customer data, or claim a certification, endorsement, saving or outcome it cannot evidence (NN-05, NN-15, NN-20, NN-22, NN-23, NN-41).

## 3. Competitive bar (R-016, R-075, R-086; Appendix Q)

LegalKart is the main competitor; Vakilsearch, IndiaFilings, OnlineLegalIndia, LegalWiz, Provakil, SpotDraft, Leegality, Digio, Melento (formerly SignDesk), Rocket Lawyer and LegalZoom set the other benchmarks (R1, Appendix Q). LawDocs must beat them on the gap no one fills: **one app that holds the vault, the signing, the case and trademark deadlines and access to professionals**, with transparent pricing and lawful professional engagement.

| Benchmark | Their pattern | LawDocs bar |
|---|---|---|
| LegalKart | Prepaid per-minute wallet (chat from ₹22/min, talk from ₹31/min), lawyer listings, commission on services, court-data API, challan service | No ranked lawyer directory (Madras HC 2024, NN-21); fixed-price services fulfilled by assigned professionals; credits with disclosed, fair validity; no unverifiable "verified lawyer" claims (NN-20); server-rendered pages with complete, answered FAQs |
| Vakilsearch / IndiaFilings | "From ₹X" pricing with government fees hidden | Professional fee + government fee + LawDocs fee + GST = total before payment (NN-22, NN-50) |
| Provakil | Enterprise case, IP and contract management | Same depth for companies (P11–P13) plus an individual litigant mode, Vidhi order summaries and plain-language status |
| Leegality / Digio / Melento | Multi-ESP eSign, BharatStamp, stamp-duty calculators | Provider-neutral adapters with failover (D-12), instrument eligibility gate (NN-07), stamp-before-sign (NN-08), evidence pack + s.63 certificate (NN-10) |
| Rocket Lawyer / LegalZoom | Memberships with unlimited documents and attorney access | Membership plans with included credits and review allowances; no auto-renewing bundled traps (NN-50) |

The 105-item improvement backlog (IMP-001…IMP-105, Appendix Q; IMP-106 onwards reserved for new findings) is binding: each item names its phase.

---

## 4. Non-negotiable rules (NN) — encode as tests, not comments

Each rule has at least one test in `tests/nn/NN-xx_*.spec.ts` and at least one Gherkin scenario (Appendix V coverage matrix). A pull request that weakens an NN test fails CI.

| ID | Rule |
|---|---|
| NN-01 | Tenant isolation: `tenant_id` + `legal_entity_id` on every tenant row; enforced PostgreSQL RLS; deny by default; IDOR/BOLA tests per endpoint. |
| NN-02 | Audit ledger is append-only and hash-chained; no user, including Super Admin, edits history; corrections use Correction Entries that reference the original. |
| NN-03 | Authentication ≠ identity verification ≠ signing. Aadhaar is never a login method. Login = mobile/email OTP, passkey, password + MFA, or enterprise SSO (R3 LG-021–025; CH-01). |
| NN-04 | Never store a full Aadhaar number, biometric, OTP, e-KYC XML or Aadhaar authentication payload. Auto-mask Aadhaar numbers in every upload/OCR output (first 8 digits) before storage of derived text; keep last 4 digits only where needed (Aadhaar Act s.29(4); R3 LG-026–031). |
| NN-05 | No CKYC search/download, no credit-bureau pull, no direct PAN-database call without a lawful upstream warranty, and no scraping, CAPTCHA solving or credential-driven automation of any court, registry, regulator, government or bureau portal (R3 LG-046–060; CH-03–06). |
| NN-06 | eSign only through a licensed ESP, via a contracted aggregator acting as ASP or LawDocs' own ASP arrangement (`asp_mode` per vendor), never sublet: LawDocs' eSign capability is never offered to Finbyx, Udofin, Equator, LDC or any customer application as a provider — other products hand off to a LawDocs-hosted signing page within a LawDocs customer relationship and receive status and evidence only (X-05, X-15). Signer consent screen, eSign transaction evidence and logs retained per CCA requirements; routing blocks any ESP whose CCA licence has lapsed or expired without recorded renewal evidence (X-16). |
| NN-07 | The **instrument eligibility gate** (Appendix F) runs before any signing request: instruments excluded by the IT Act First Schedule (wills and other testamentary dispositions; trusts; powers of attorney other than those empowering an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity; negotiable instruments other than cheques and demand promissory notes/bills of exchange in favour of such entities — as amended by S.O. 4720(E) [VERIFY Gazette text and date]; Appendix F governs) cannot be routed to eSign; they get a wet-ink/notary/registration pack instead. |
| NN-08 | **Stamp before sign.** eStamp only through authorised channels (SHCIL as CRA, ACCs, State-authorised e-stamp/e-SBTR/franking routes) per State; stamp duty passed through at actuals; LawDocs' facilitation fee disclosed separately; certificate UIN verified and linked to the document hash. |
| NN-09 | Original uploads and signed files are immutable (S3 Object Lock, SHA-256 at ingest). OCR text, type copies, translations and summaries are derived renditions (`drv_`) — labelled, editable, versioned, with confidence scores and page/region anchors. Never silently replace an original. |
| NN-10 | Evidence: every signed/executed document gets an evidence pack (hashes, signer events, IP/device, timestamps, provider certificate, audit extract) and a one-click **BSA 2023 s.63(4) certificate** draft (Part A for the party, Part B for the expert, as the Schedule requires) for court use. |
| NN-11 | Portability: every record type is registered in `xpt.export_map` before its phase exits; any tenant or individual can export everything, any time, without staff help, in `LD-EXPORT-1.0` (Appendix K) — human-readable folders, DOCX/XLSX/PDF(-A)/CSV/JSON + manifest + hashes + README. |
| NN-12 | Migration safety: expand → migrate → contract; no destructive change in the release that introduces its replacement; backfills idempotent and verified; folder paths and categories are **views over stable canonical IDs**, so code, schema, storage vendor or region changes never require manual re-filing of customer data. |
| NN-13 | No AI agent or automation performs an irreversible external action — send, file, submit, sign, pay, share outside the tenant, call, accept, withdraw, delete — without a per-action human confirmation by an authorised user (and the required second approval where maker-checker applies). |
| NN-14 | AI outputs are labelled, sourced and dated; no fabricated case law, sections or citations — every legal citation is resolved against the rules register or a retrieved source or is shown as "unverified". AI-customised legal documents for individuals are marked **"AI draft — not reviewed by a professional"** until a qualified reviewer approves, with one-click paid review; AI use is disclosed (Anthropic Usage Policy high-risk legal use requirements [VERIFY current text/effective date — R4]). Assembly of a vetted template from the user's answers is template automation, not AI advice. |
| NN-15 | Customer data is never used to train models; confidential classes go only to Bedrock India (or another approved in-region endpoint with zero data retention); prompts and tool outputs pass the PII/secret scrubber; retrieval is tenant- and permission-scoped. |
| NN-16 | Client credentials (portal logins) live only in the client-owned credential vault (`cvl`): envelope-encrypted with client-scoped keys, masked by default, delegation-first (named users/practitioner roles preferred), just-in-time reveal with reason + client approval (configurable), time-boxed, every view/copy/change logged and visible to the client; OTPs, DSC PINs and recovery codes are never stored; the feature is OFF until the client admin enables it (D-03; CH-07). |
| NN-17 | Delivery staff and professionals access a tenant only through client-approved, scoped, time-bound **delivery grants**; the client sees an access-transparency log; break-glass needs dual approval and is reported to the client within 24 hours. |
| NN-18 | Maker-checker with segregation of duties (maker ≠ checker, enforced) for: payments/refunds/credits, access grants, data exports of a tenant, role elevation, critical configuration, master-data changes of a client, template/rule publication, price and revenue-stream switches, bulk deletes, agent autonomy changes. |
| NN-19 | Only aggregates and commercial records go to the Operations Hub; no tenant document, matter, case, credential or personal-content data (Ecosystem Spec principle 12). CRM receives only consented lead/contact data. |
| NN-20 | No unevidenced claims anywhere (site, app, invoices, AI): certifications, "verified lawyers", "real-time" court data, success rates, savings, rankings, "government-approved". |
| NN-21 | Marketplace professional rules (Appendix M): no commission, fee-share, referral reward, lead fee, listing fee or paid ranking for advocates; practising CA/CS listings and any percentage model follow ICAI/ICSI rules; each such switch is locked OFF until a counsel opinion is attached and a checker approves; neutral ordering; advocates' profiles show BCI Rule 36 permitted fields only; no ratings or testimonials about advocates (Madras HC 2024; R1, R3 LG-110–117). |
| NN-22 | Money: hosted/tokenised checkout only (no PAN/CVV storage; PCI DSS SAQ A scope); marketplace payouts only via Razorpay Route split settlement under the RBI Payment Aggregator Directions; LawDocs never pools third-party money; statutory/government fees and stamp duty shown separately from professional fees and LawDocs fees; total incl. GST shown before payment; GST tax invoices issued by OH8. |
| NN-23 | Consumer Help (`chp`) runs under its own configurable brand and legal-entity profile with an ethical wall: no access to any LDC/Finbyx/Udofin/Equator tenant data; conflict check against the group's lender/insurer clients before acceptance; no promise of waiver, settlement or outcome; never collects fines, challans or dues — users pay on official portals; representation only where the forum's rules allow (e.g., no advocate as authorised representative before the RBI Ombudsman where the 2026 Scheme bars it — R2). |
| NN-24 | Cross-product data moves only through Ecosystem Spec contracts with a `consentref` or `legalbasis`; LawDocs is registered as owner code `LD` (Appendix Y); no shared database, no direct table reads. |
| NN-25 | Residency: tenant plane in India (ap-south-1, DR ap-south-2); any processing abroad only after a recorded transfer assessment and customer-sector check. |
| NN-26 | DPDP: notice + consent artefacts per purpose, consent withdrawal, retention schedules with automatic erasure subject to legal hold, breach workflow (Data Protection Board + affected users), children's data only with verifiable guardian consent, grievance officer SLAs per IT Rules 2021 as amended [VERIFY current SLA — R3 reports 7 days from 20 Feb 2026]. GDPR/CCPA controls switch on by jurisdiction flag. |
| NN-27 | CERT-In: 6-hour incident reporting; 180-day log retention in India; NTP-synced clocks. |
| NN-28 | Accessibility: WCAG 2.2 AA and IS 17802 (Parts 1–2) for every web and mobile surface; no accessibility overlays; automated (axe) + manual (NVDA/JAWS/VoiceOver/TalkBack, keyboard, 400% zoom) gates per release. |
| NN-29 | Settings are registered (Appendix R) before code reads them; tiered and effective-dated; tenant-level customisation never needs Super Admin or a code release. |
| NN-30 | Legal content is data: templates, clauses, rules, glossary terms, eligibility rows and jurisdiction variants are versioned, sourced, effective-dated, jurisdiction-scoped and carry a reviewer of record; publishing content never needs a code release and a code release never changes published content. |
| NN-31 | Public site is server-rendered/static; private content is never indexable (noindex, auth, signed URLs); AI-crawler policy is a setting. |
| NN-32 | Logs, traces, analytics and support tickets never contain Aadhaar, secrets, document content, OTPs or full PAN; PII scrubbing in OpenTelemetry pipelines. |
| NN-33 | Workforce measurement is proportionate and disclosed: outcome and SLA metrics, declared work sessions; no keylogging, covert screenshots, webcam capture or browsing surveillance (applies to client HRMS defaults and to any LawDocs staff tooling). |
| NN-34 | Telecom: DLT-registered headers/templates, consent, calling windows, DND, AI-voice disclosure and human hand-off, pre-declared numbers for automated calls (TCCCPR as amended 2026 — R4); counterparties receive at most one LawDocs-originated invitation plus reminders they did not opt out of, and no automated calls until they opt in. |
| NN-35 | Advertising stream is OFF by default; if ON, only on public content pages (blog, vlog, learning), labelled "Sponsored", contextual only, never targeted on personal data, never in vault/matters/consumer cases/AI answers, never for advocates (D-13). |
| NN-36 | Savings and value dashboards show the formula, inputs, assumptions and evidence class (MEASURED / ESTIMATED / MODELLED) for every figure; "penalty avoided" appears only with an evidenced obligation, due date and completion before due, labelled as avoided exposure, not money saved. |
| NN-37 | Redlining is deterministic: every negotiation round is a version; counterparties see only versions shared with them; internal comments are never visible externally; accepted/rejected changes are logged per change. |
| NN-38 | Any feature depending on a `[VERIFY]` fact ships behind a flag that is OFF (or advisory-only) until the fact is verified and logged in `docs/compliance/verification-log.md`. |
| NN-39 | Kill switches exist for every AI agent, revenue stream, vendor adapter, consumer vertical and outbound channel, operable by authorised roles with audit. |
| NN-40 | Formalities gate: a document cannot be marked "Executed/Complete" until its required formalities (stamp, witnesses, notarisation, registration, board approval, counterparty signatures) are recorded or explicitly waived by an authorised user with reason. |
| NN-41 | Professional judgement stays with the professional. LawDocs (the company) does not provide reserved legal services (advice/representation by advocates, attest functions by CAs) in its own name; those are delivered by eligible practitioners under direct engagement terms; LawDocs provides technology, administration and non-reserved services (D-05, LDC D-32). |
| NN-42 | DigiLocker-pulled documents follow the requester terms: store the URI and verification result; retain a copy only for a recorded user purpose permitted by the terms [VERIFY with NeGD]; user uploads are stored normally with hashes (R3 LG-036–038). |
| NN-43 | Agents are makers only — never checkers, approvers or signers; every agent has a human sponsor, an autonomy ceiling (L0–L4) set by the tenant within plan limits, a mission scope, tool allowlist, budget and kill switch. |
| NN-44 | Mobile: no sensitive data in device logs or screenshots of protected screens; encrypted offline vault cache with device-bound keys; biometric unlock device-local only; root/jailbreak and tamper detection; certificate pinning. |
| NN-45 | Every mutating handler writes the audit ledger in the same database transaction. |
| NN-46 | Every external side effect (payment, eSign, eStamp, message, export to BYO storage, agent tool call) carries an idempotency key and is reconciled. |
| NN-47 | Shared group kernels are used, never forked; when a tenant also uses LawDocsComply, LDC is system of record for governance, compliance and client HRMS and LawDocs reads/writes through the contracts (D-10). |
| NN-48 | Machine translations of legal text are labelled, versioned and reviewed before operative use; translations filed in court route to a certified-translation service (R3 LG-093/094). |
| NN-49 | Reviews and testimonials are genuine, consented, from verified purchases, never about advocates, displayed without photos by default, and moderated per IS 19000:2022 and the Consumer Protection (E-Commerce) Rules 2020. |
| NN-50 | No dark patterns (CCPA Guidelines for Prevention and Regulation of Dark Patterns 2023): no drip pricing, subscription traps, forced continuity, confirm-shaming or false urgency; renewal and cancellation terms shown before payment; cancellation as easy as sign-up. |


---

## 5. Architecture (locked decisions)

### 5.1 Stack (D-01)

| Layer | Choice |
|---|---|
| Monorepo | pnpm + Turborepo, TypeScript strict, shared ESLint/Prettier, Changesets |
| Web apps | Next.js 16 (App Router) + React 19; shadcn/ui + Tailwind on LawDocs design tokens (Appendix C); TanStack Query/Table; i18next; `apps/public` server-rendered/static, multi-brand (NN-31) |
| Mobile | Expo (React Native) with EAS builds and controlled OTA updates; one codebase, brand flavours (LawDocs, Consumer Help brand); mobile BFF `/m/v1` (P22) |
| API | NestJS 11 modular monolith (`apps/api`), one NestJS module = one PostgreSQL schema = one bounded context; OpenAPI 3.1 generated from Zod; AsyncAPI 3.0 for events |
| Runtime | Node.js 24 LTS [VERIFY at P00] |
| Database | PostgreSQL 16+ (18 preferred) with enforced RLS; Drizzle or Kysely; `NUMERIC` + `decimal.js` for money; pgvector for tenant-scoped embeddings |
| Hosting | Production: AWS ap-south-1 (Mumbai), DR ap-south-2 (Hyderabad); RDS/Aurora PostgreSQL; S3 with SSE-KMS, versioning and **Object Lock** for originals, signed files and evidence. Non-production may use Supabase PostgreSQL (database only). The legacy Vite/Express/MongoDB/Railway deployment is migrated and decommissioned in P00 with a 301 map (R5 found client-side rendering that crawlers see as empty, non-www sitemap URLs that fail, and robots blocking `/buy/` pages the sitemap lists). |
| Workflows and jobs | Temporal (signing ceremonies, negotiations, hearings and deadline clocks, exports/imports, agent missions, service orders); Redis (cache, rate limits, short jobs) |
| Search | OpenSearch (tenant-filtered indices, Indic analysers) with PostgreSQL full-text fallback |
| Identity | Keycloak (OIDC/SAML, OTP, passkeys/WebAuthn, MFA, SCIM): realm `ld` (customers, counterparties, professionals, partners) and realm `ld-staff` (federated to the group Entra ID; provisioned from OH10) |
| Authorisation | Cerbos (RBAC + ABAC policies as code; Appendix D) |
| Rules | GoRules ZEN decision tables + CEL behind `RULES_PORT` (P03) |
| Documents | docxtemplater (DOCX), `@infrabyx/redline` (OOXML track changes, NN-37), Gotenberg/LibreOffice (PDF, PDF/A-2b/3b); optional co-authoring in the customer's own Microsoft 365 or Google Workspace; optional ONLYOFFICE/Collabora WOPI behind a licence ADR |
| Document intelligence | `packages/dix`: deterministic OCR (Tesseract/PaddleOCR with Indic models) for print; Claude vision for handwriting and screenshots; translation adapters behind `TRANSLATE_PORT` (P05) |
| AI | `packages/ai` provider-neutral gateway: Claude via Amazon Bedrock India for confidential data classes; Anthropic API only for public or non-personal content; model registry and version pinning; MCP server and client (P09, D-14) |
| Payments | Razorpay hosted checkout, Subscriptions, e-mandate, Route split settlement, Smart Collect — through OH8 via `BILLING_PORT` (NN-22) |
| Communications | `packages/notify`: email (SES / Brevo transactional), SMS, voice, WhatsApp and RCS via JioCX and other DLT-registered CPaaS adapters (Appendix J), in-app, push |
| Observability | OpenTelemetry traces, metrics and logs; PII scrubbing (NN-32); SIEM export |

### 5.2 Repository layout

```
apps/       public  web  delivery  console  mobile  api
packages/   tenancy audit config rules workflow notify docgen redline dix ai agents
            connectors export ui tokens i18n a11y contracts (generated from infrabyx-contracts)
modules/    (inside apps/api/src) core iam kyc org cfg rul wf ntf msg dms dix tpl drf clm sgn
            ai agt pld lit ipm gov hr lgo bsv tax chp mkp aca bil sav sdc cvl int xpt web hlp
            rpt mob eng
db/         migrations (expand-contract), ownership.yaml, seeds (synthetic)
content/    templates, clauses, eligibility rows, legal rules, glossary (as data, versioned)
docs/       00-master-prompt.md, 01-decision-log.md, ecosystem/, phases/, decisions/ (ADRs),
            interfaces/, compliance/ (verification-log.md, ropa, dpia), runbooks/
tests/      unit, integration, contract, acceptance/pxx/*.feature, nn/NN-xx_*.spec.ts,
            journeys/J-xx, golden/ (archives, redlines, documents), a11y/
```

### 5.3 Bounded contexts (binding module codes)

`core` tenancy, audit ledger, correction entries, IDs · `iam` accounts, sessions, MFA, passkeys, realms · `kyc` identity and business verification, consent artefacts, DigiLocker, Aadhaar offline verification (OVSE), licensed lookups · `org` organisations, entities, branches, departments, teams, positions, delegations · `cfg` settings registry, Configuration Studio, flags, kill switches · `rul` rule engine, legal rules register runtime, jurisdiction packs · `wf` tasks, maker-checker, approvals, SLAs, open/interim/waiting items (`wf.items`) · `ntf` notifications · `msg` secure messaging and comments · `dms` Legal Vault and DMS · `dix` document intelligence · `tpl` templates and clauses · `drf` drafting studio · `clm` contract lifecycle · `sgn` eSign, DSC, eStamp, execution, evidence · `ai` Vidhi runtime · `agt` agent workforce · `pld` pleadings and notices · `lit` matters, cases, hearings, orders · `ipm` IP portfolio · `gov` governance kernel mount · `hr` HRMS kernel mount · `lgo` Company Legal Department OS · `bsv` business services and Startup Desk · `tax` tax workspace · `chp` Consumer Help · `mkp` marketplace, registry, engagements, retainers · `aca` FinLegal Academy link · `bil` presentation catalogue, entitlements, meters, credits, billing UI (engine is OH8) · `sav` savings and value ledger · `sdc` Delivery Console · `cvl` credential vault · `int` integration gateway (only module that publishes/consumes cross-product events and holds ecosystem credentials) · `xpt` export, import, BYO storage · `web` public site CMS · `hlp` help centre, glossary, tutorials · `rpt` dashboards and reports · `mob` mobile BFF · `eng` engineering governance.

### 5.4 Cross-cutting engineering patterns

- **Tenancy:** `tenant_id` + `legal_entity_id` on every tenant row; session context set per request and per job; RLS tested by `NN-01_*`.
- **Identifiers:** prefixed ULIDs (Appendix B §B.1 registry, conventions + X-01); human-readable business references `LD-AGR-2026-000123`, `LD-MAT-…`, `LD-CAS-…`, `LD-TMK-…`, `LD-ENG-…`, `LD-GRV-…`, `LD-NTC-…`, `LD-ORD-…`, `LD-LRQ-…`. Never reused; never encode location (NN-12).
- **Audit:** `packages/audit` writes the hash-chained ledger in the business transaction (NN-02, NN-45); corrections only by Correction Entry.
- **Outbox/inbox:** transactional outbox; idempotent consumers with an inbox table; CloudEvents 1.0.
- **Event names:** cross-product events follow the Ecosystem Spec pattern `in.infrabyx.<domain>.<EventName>.v<major>` with `source = urn:infrabyx:lawdocs:<tenantid>`, published only by `int` and only once registered (Appendix Y); internal events and tenant webhooks use `in.lawdocs.<module>.<EventName>.v<n>` (Appendix B §B.4).
- **Errors:** `LD-<MODULE>-<NNN>` with actionable user messages and help keys (Appendix B §B.5).
- **Configuration:** read only through `packages/config` with tier, scope and effective date (P03).
- **Workflows:** maker-checker, approvals, escalations, delegations, SLAs and open/interim/waiting items through `packages/workflow` on Temporal (P02, P03; Appendix A).
- **Documents:** generated through `packages/docgen`; every generated file records template version, data snapshot hash and lineage; originals immutable (NN-09).
- **Feature flags:** every unverified or vendor-dependent feature ships behind a flag that is OFF and names its approver (NN-38); kill switches per agent, vendor, stream, vertical and channel (NN-39); canonical events `cfg.KillSwitchEngaged` / `cfg.KillSwitchReleased`.

### 5.5 Security architecture (summary; Appendix P)

Threat model per release; OWASP ASVS 5.0 Level 2 (Level 3 for identity, credential vault, signing, payments and exports); MFA for all staff and admins, passkeys for everyone; SSO (Entra ID, Google) and SCIM for company tenants; envelope encryption with per-tenant data keys for sealed classes; KMS hierarchy with rotation; secrets manager; WAF and rate limits; malware scanning of every upload; CSP and subresource integrity; supply-chain controls (SBOM, Dependabot, CodeQL, signed builds, SLSA target); VAPT by a CERT-In-empanelled auditor before each wave's GA and at least annually; CERT-In 6-hour reporting and 180-day India log retention (NN-27); DigiLocker requester obligations (24-hour breach reporting to NeGD, annual audit [VERIFY]); certification-readiness evidence for SOC 2 Type I/II, ISO 27001:2022, ISO 27701, ISO 42001, ISO 22301 and PCI DSS v4.0.1 SAQ A. Building for readiness is not certification; no claim until a certificate or report exists (NN-20).

---

## 6. Canonical domain model (summary; DDL and registry in Appendix B)

### 6.1 Core legal objects

| Object | Prefix / ref | Owner module | Key relationships |
|---|---|---|---|
| Person / party | `prs_` | `kyc` | users, counterparties, directors, witnesses, advocates |
| Document, version, derived rendition | `doc_`, `ver_`, `drv_` | `dms`, `dix` | original immutable (Object Lock); OCR text, type copy, translation, summary are `drv_` (NN-09) |
| Folder, smart folder, share | `fld_`, `svw_`, `shr_` | `dms` | folders are views over canonical IDs (NN-12) |
| Template, clause, draft | `tpl_`, `cls_`, `drf_` | `tpl`, `drf` | template version + reviewer of record (NN-30) |
| Agreement, negotiation round, obligation | `agr_` / `LD-AGR-…`, `neg_`, `obl_` | `clm` | deal room, redlines (NN-37), key dates |
| Signing request, signature event, stamp instrument, evidence pack | `sgr_`, `sig_`, `stp_`, `evp_` | `sgn` | eligibility gate (NN-07), stamp-before-sign (NN-08), s.63 certificate (NN-10) |
| Matter, court case, hearing, order, notice, pleading | `mat_`, `cas_`, `hrg_`, `odr_`, `ntc_`, `pld_` | `lit`, `pld` | court-data refresh with staleness (NN-05) |
| IP asset | `tmk_` | `ipm` | application lifecycle, deadlines, watch |
| Legal request, meeting, resolution | `lrq_`, `mtg_`, `res_` | `lgo`, `gov` | intake desk; governance kernel |
| Service, offer, engagement, retainer, SLA, professional | `svc_`, `ofr_`, `eng_`, `rtn_`, `sla_`, `pro_` | `mkp`, `bsv` | Route split settlement (NN-22) |
| Consumer case, challan record, vehicle record | `grv_`, `chl_`, `veh_` | `chp` | Consumer Help cell, ethical wall (NN-23) |
| Delivery grant, credential entry | `grt_`, `cvl_` | `sdc`, `cvl` | client-approved (NN-16, NN-17) |
| Agent, mission, run | `agt_`, `msn_`, `run_` | `agt`, `ai` | makers only (NN-43) |
| Export job, import job, storage target | `exp_`, `imp_`, `stg_` | `xpt` | `LD-EXPORT-1.0` (Appendix K) |

### 6.2 Canonical statuses (summary; Appendix A governs — tenants relabel only)

Documents (A.18): `PROCESSING → ACTIVE → ARCHIVED → DELETED (recycle bin) → PURGED`, with `QUARANTINED` and `REJECTED`; flags `is_executed`, `on_legal_hold`, `health_status`, `superseded`; execution status is A.33. Agreements (A.30): `DRAFT → IN_NEGOTIATION → IN_APPROVAL → APPROVED → LOCKED_FOR_SIGNATURE → IN_SIGNATURE → SIGNED_PENDING_FORMALITIES → EXECUTED`, then `AMENDED` / `RENEWED` / `TERMINATED` / `EXPIRED`, or `CANCELLED` before signature. Signing requests (A.31): `DRAFT → (PENDING_APPROVAL) → READY → SENT → IN_PROGRESS → COMPLETED`, with `HELD_FOR_REVIEW`, `CHANGES_REQUESTED`, `DECLINED`, `EXPIRED`, `VOIDED` and `CANCELLED`. Items (`wf.items`, A.15): `OPEN`, `IN_PROGRESS`, `WAITING` (with waiting-on party type: counterparty, court, registry, regulator, vendor, client, internal), `INTERIM`, `ON_HOLD`, `RESOLVED`, `WAIVED`, `CANCELLED`, `SUPERSEDED`. All 63 machines are in Appendix A; where this summary and Appendix A differ, Appendix A wins.

### 6.3 Open, interim and "waiting on others" items (R-047)

Every module raises work through one items engine (`wf.items`, P03 §4J): item types, statuses, owners, SLA clocks, auto-chasers and external waits are **tenant-configurable** (61 seeded item types, Appendix R), effective-dated and versioned, so changes in law or practice never need a code release or Super Admin. Locked canonical statuses keep reports and exports stable; tenants rename, add sub-statuses, change SLAs and chaser cadence.

### 6.4 Correction Entries

No record of legal significance is edited in place once finalised (signed documents, evidence, audit, invoices mirror, court orders captured). Corrections are Correction Entries that reference the original, carry reason and approver, and appear in history and exports (NN-02).

---

## 7. Regulatory baseline as of 25 October 2026 (re-verify before each dependent feature; Appendix G)

| Area | Position the build follows | Rule refs |
|---|---|---|
| eSign | IT Act 2000 s.3A, s.5, Second Schedule; CCA eSign API v3.x via licensed ESPs; ASP may not sublet; consent and logs retained; First Schedule exclusions as amended 26 Sep 2022 (entry for contracts for sale or conveyance of immovable property omitted [VERIFY Gazette text and date — S.O. 4720(E)]; wills, trusts, POAs other than those in favour of RBI/NHB/SEBI/IRDAI/PFRDA-regulated entities, and negotiable instruments other than cheques and DPNs/bills in favour of such entities remain excluded) | LG-001–LG-014; X-02; Appendix F |
| Aadhaar | No authentication by LawDocs (Aadhaar Act s.4(4); s.57 private-entity use omitted by the Aadhaar and Other Laws (Amendment) Act 2019 after *Puttaswamy* (2018)); Aadhaar App / QR offline verification as OVSE [VERIFY registration route]; never store the number; mask under s.29(4) | LG-021–LG-034; NN-03, NN-04 |
| DigiLocker | Requester terms (June 2025): purpose-limited storage, 24-hour breach report to NeGD, annual audit | LG-036–LG-041; NN-42 |
| Closed data | CKYC only for PMLA REs; credit bureaus only for specified users (CICRA s.17(4), s.22); no open MCA, eCourts or IP India APIs for LawDocs | LG-046–LG-060; NN-05 |
| Data protection | DPDP Act 2023 + Rules 2025 (consent-manager provisions 13 Nov 2026; core obligations 13 May 2027 [VERIFY]) — built to full DPDP from day one; IT Rules 2021 as amended 20 Feb 2026 (grievance 7 days, AI-content labelling [VERIFY]); CERT-In Directions 2022; GDPR/CCPA on triggers | LG-061–LG-086; NN-26, NN-27 |
| Evidence | Bharatiya Sakshya Adhiniyam 2023 ss.61–63; s.63(4) certificate with hash value | LG-090–LG-096A; NN-10 |
| Stamp and registration | Indian Stamp Act 1899 and State Acts; e-stamping via SHCIL (CRA)/ACCs/State systems; Registration Act 1908 s.17; notarisation for affidavits | LG-096–LG-107; NN-08, NN-40 |
| Professional conduct | Advocates Act 1961; BCI Rules Part VI Ch II (Rules 20, 36, 37 and fee-sharing bar); Madras HC 3 Jul 2024 on listing platforms (SC pending, no stay found); ICAI 23 Oct 2019 aggregator restrictions; ICSI analogues | LG-110–LG-119; NN-21, NN-41 |
| Payments and tax | RBI Payment Aggregator Directions (15 Sep 2025) → Route split; GST 18% on LawDocs services, RCM on advocates' services to business entities (Notification 13/2017-CT(R)); e-commerce TCS/TDS [TAX MEMO]; Income-tax Act 2025 from 1 Apr 2026 [VERIFY section mapping]; ERI and GSP routes for filings | LG-123–LG-130, LG-145–LG-148; NN-22 |
| Consumer forums | RB-IOS 2026 (from 1 Jul 2026: RE first, 30-day wait, no advocate as authorised representative); Insurance Ombudsman Rules 2017 as amended (₹50 lakh cap, 1 year); Consumer Protection Act 2019 and E-Commerce Rules 2020; CCPA Dark Patterns Guidelines 2023; recovery-agent conduct rules from 1 Jan 2027 [VERIFY] | LG-140–LG-150, LG-170–LG-172; NN-23, NN-50 |
| Telecom | TCCCPR 2018 as amended (Third Amendment 18 Sep 2026: pre-declared numbers for automated/AI-voice calls [VERIFY]); DLT | NN-34; Appendix J |
| AI | Anthropic Usage Policy: legal document preparation for individuals is a high-risk use — qualified human review before delivery and AI disclosure [VERIFY effective date]; IT Rules synthetic-media labelling | NN-14; CH-30 |
| Accessibility | RPwD Act 2016 ss.40–46, RPwD Rules 2017 r.15 (GIGW / IS 17802); WCAG 2.2 AA | LG-133–LG-137; NN-28; Appendix U |
| Labour | Four Labour Codes (from 21 Nov 2025 [VERIFY]); POSH Act 2013 | LG-162–LG-167; P13, OH10; labour rulepack |

---

## 8. Customisation framework (R-027, R-030, R-047; P03, Appendix R)

- **Tiers:** PLATFORM → BRAND → PLAN → TENANT → ENTITY → DEPARTMENT → USER, each setting with type, default, allowed tiers, who may change it, maker-checker flag and effective dating. About 1,200 keys are catalogued in Appendix R.
- **What a company admin can change without us:** labels and menus, home widgets, quick actions, numbering schemes, custom fields and statuses, item types and SLAs, approval matrices and DoA, maker-checker coverage (within locked minimums), notification channels and quiet hours, letterheads and branding, template playbooks and clause positions, retention schedules (within legal floors), export folder profile, language and region, AI autonomy ceilings within plan limits, integrations.
- **What an individual can change:** language, reading mode (easy-read, large text, high contrast, dyslexia-friendly font), reminders, family and nominee access, folder views, AI assistance level, privacy and sharing defaults, notification channels.
- **What only the platform changes:** locked statuses, NN controls, legal floors, eligibility rows (through Content Studio with reviewer of record), revenue-stream switches (maker-checker), vendor routing.
- **Configuration as data:** configuration templates can be exported/imported between tenants (onboarding accelerators for NBFCs, startups, law firms); every change is versioned, diffable and reversible.

---

## 9. Commercial architecture (R-035–R-042, R-054, R-063; P16, P17, Appendices L, M)

- **Plans (seed prices, ex-GST, [OWNER TO SET]):** Free (₹0); **Personal** ₹1,499/yr or ₹149/month; **Pro** ₹9,999/yr or ₹999/month per workspace (professionals, freelancers, startups); **Business** ₹59,999/yr or ₹5,999/month (companies, LLPs, NBFCs); **Enterprise / Custom** from ₹3,00,000/yr. The public pricing page shows Personal, Pro and Business with a full feature matrix, "benefits explained", totals incl. GST and renewal/cancellation terms before payment (NN-50), with links to Free and Enterprise.
- **Add-ons and credits:** eSign credits (₹19–₹29 retail; plan allowances), eStamp facilitation (₹49 + duty at actuals), AI credits, court-data refresh credits, family extension, seats, litigation pack, TM watch, advanced CLM, advanced DMS, virtual data room, board and secretarial pro, HRMS-lite, SSO/SCIM, API tier, BYO storage (Appendix L §add-ons).
- **One-time products and retainers:** documents reviewed or drafted by professionals, notices, filings, registrations, startup bundles; retainers — Startup Legal Officer, SME Legal Desk, NBFC Legal & Compliance Retainer, Managed Legal Department (LDaaS) — with customised scope, hour banks and eSigned SLAs.
- **Marketplace:** one group storefront (D-11); services purchasable without any SaaS plan (R-040); per-profession switches with lawful defaults (D-05, NN-21): no fee of any kind from advocates; a disclosed buyer-side platform fee; regulated-professional percentage models locked pending counsel; Route split settlement.
- **Revenue-stream registry:** 45 streams (RS-LD-01…45) with owner, segment, model, default ON/OFF, disclosure text, tax treatment, refund rules and kill switch; switches change through maker-checker (NN-18, NN-39). Advertising is OFF by default and public-pages-only if ever ON (D-13, NN-35).
- **Billing engine:** prices, tax, quotes, orders, GST invoices (emailed), credit notes, payments, e-mandates and dunning are OH8's; LawDocs presents, meters and enforces entitlements (`bil`).
- **Savings & Value dashboard** (Settings → Savings): hours saved, money saved against dated market benchmarks, avoided exposure for evidenced deadlines met — every figure with formula, inputs and evidence class (NN-36).

---

## 10. AI layer — Vidhi AI (R-007, R-010, R-015, R-018; P09, Appendix H)

- **Gateway:** provider-neutral; Claude via Bedrock India for confidential classes, Anthropic API only for public content; model registry with tiers and version pinning (R4 reports Bedrock India profiles Opus 5 / Sonnet 5 / Haiku 4.5 [VERIFY at build]; keep model names configurable); prompt caching; batch for bulk jobs; per-tenant metering into AI credits.
- **Vidhi for individuals:** "Find an answer to my problem" — triage, plain-language explanation in the user's language, options and next steps, the right document/notice/complaint draft, and the "Hire a professional" path. Not legal advice; disclosed; reviewed where NN-14 requires.
- **Vidhi as the AI employee for companies:** 37 role agents (Appendix H) for the legal team, CLO, KMP (CS, CFO, CEO) and board — contract drafter, redline negotiator, obligation tracker, litigation clerk, hearing prep, order summariser, TM watch, notice responder, evidence/type-copy clerk, translator, research associate, board-pack summariser, minutes drafter, resolution drafter, action-item tracker, onboarding and billing assistants, consumer-help assistant and more — each with a human sponsor, autonomy ceiling L0–L4, missions, schedules, budgets, approvals and a kill switch; makers only (NN-43); "what my AI employee did today" digest.
- **Guardrails:** retrieval scoped by tenant and permission; prompt-injection defences for uploaded files and email; tool allowlists; PII/secret scrubbing (NN-15); citations resolved or flagged (NN-14); no irreversible action without per-action confirmation — an itemised, bounded send-plan counts as confirmation (NN-13, X-04); evaluation sets per language and task; red-teaming; incident handling.
- **Interoperability:** LawDocs MCP server so customers' own assistants can use LawDocs tools within their permissions; MCP client for approved external tools; agent-to-agent with ecosystem agents through Appendix Y proposals.
- **Voice:** Indic speech-to-text and text-to-speech adapters; AI-voice disclosure and human hand-off (NN-34).

---

## 11. Integrations (R-002, R-003, R-005, R-029, R-053, R-055, R-062; P19, Appendix I)

| Port | Purpose | Route (primary → fallback) |
|---|---|---|
| `ESIGN_PORT`, `DSC_PORT` | Aadhaar eSign, DSC, electronic signatures | Aggregator ASP (Leegality / Digio / Melento / Surepass-type) → second ESP; own ASP later (D-12, NN-06) |
| `ESTAMP_PORT` | eStamp procurement and verification | Contracted ACC / aggregator per State → manual attach with UIN verification (NN-08) |
| `KYC_PORT`, `OVSE_PORT`, `DIGILOCKER_PORT` | Identity and documents | DigiLocker requester; Aadhaar offline verification; licensed PAN route with lawful upstream (CH-04) |
| `COMPANY_DATA_PORT`, `GSTIN_PORT` | KYB pre-fill | Licensed MCA-data vendors (Probe42 / Signzy / Surepass / Perfios-Karza); GSP for GSTIN |
| `COURT_DATA_PORT` | Case status, cause lists, orders | Two licensed aggregators + user-entered CNR + manual refresh; staleness labels; never "real time" (NN-05, NN-20) |
| `TRADEMARK_DATA_PORT` | TM status and journal | User-entered numbers + assisted refresh + WIPO Global Brand Database + licensed partner [VERIFY]; no scraping |
| `BILLING_PORT` | Prices, invoices, payments | OH8 (Razorpay) |
| `COMMS_PORT`, `VOICE_PORT` | SMS, WhatsApp, RCS, email, voice | JioCX and other DLT-registered CPaaS; SES/Brevo email (Appendix J) |
| `WORKSPACE_PORT` | Microsoft 365 (Graph: OneDrive, SharePoint, Teams, Outlook) now; Google Workspace (Drive, Meet, Gmail) later | OAuth with narrow scopes; customer-owned files stay in the customer's suite |
| `CRM_PORT` | OH CRM; Brevo migration and two-way sync | OH first; Brevo adapter |
| `STORAGE_PORT` | BYO storage targets | S3-compatible, Azure Blob, GCS, SharePoint/OneDrive, Google Drive, SFTP/on-prem agent (P20) |
| `ODR_PORT` | ADR referral | Equator and other institutions (party choice) |
| `ACCOUNTING_PORT` | Legal-spend and invoice exports | Tally Prime, Zoho Books, CSV |
| `TRANSLATE_PORT`, `SPEECH_PORT` | Translation and speech | Indic providers [VERIFY], cloud fallbacks |

**Partner onboarding API** (R-003): Finbyx, Udofin, LDC, OH and approved third parties create or link company tenants in bulk with consent and KYB pre-fill (P19). **Developer platform:** versioned REST, signed webhooks, sandbox tenants, SDKs, rate tiers, health dashboard.

---

## 12. Data preservation and portability (R-021–R-024, R-053, R-068; P20, Appendix K)

- **Export any time, without staff:** `LD-EXPORT-1.0` archives (company, individual, professional and consumer-help profiles) with a `00 Start Here/` folder, README, index workbook, manifest, checksums and beginner-friendly folders by year, department, counterparty, matter or category; formats DOCX, XLSX, PDF/PDF-A, CSV, JSON plus originals and signature evidence (Appendix K governs the layout, X-07).
- **Bring your own storage:** scheduled or continuous mirrors to the customer's bucket, server, SharePoint/OneDrive, Google Drive or data centre, with clear ownership, sync direction, overwrite, conflict, encryption and revoke semantics.
- **Bulk intake:** import folder trees, ZIPs and drives with preview, AI classification, correction before commit, duplicate handling and an import report with checksums (R-024).
- **Change-proof structure:** folders are views over canonical IDs; expand-migrate-contract migrations; export-map regression tests and golden archives in CI; region/vendor move runbooks — code pushes, patches, server or data-centre changes never require manual re-filing of customer data (NN-12, R-022).
- **Ecosystem sharing:** purpose-bound, consented, ledgered sharing with Finbyx, Udofin, Equator and LDC through registered contracts (NN-24, CH-16).


---

## 13. Phase plan

### 13.1 Phases (file names are binding)
| Phase | File | Title | Sprints | Depends on | Wave |
|---|---|---|---|---|---|
| P00 | `P00_Foundations_Repository_Discovery_and_Migration.md` | Foundations, Repository Discovery and Migration | 6 | — | 1 |
| P01 | `P01_Identity_Onboarding_KYC_KYB_and_Consent.md` | Identity, Onboarding, KYC/KYB and Consent | 8 | P00 | 1 |
| P02 | `P02_Tenancy_Org_Structure_User_Types_and_Maker_Checker.md` | Tenancy, Organisation Structure, User Types and Maker-Checker | 6 | P00, P01 | 1 |
| P03 | `P03_Configuration_Studio_Rule_Engine_and_Settings.md` | Configuration Studio, Rule Engine and Settings | 6 | P02 | 1 |
| P04 | `P04_Legal_Vault_and_Document_Management_System.md` | Legal Vault and Document Management System | 9 | P02, P03 | 1 |
| P05 | `P05_Document_Intelligence_OCR_TypeCopy_and_Translation.md` | Document Intelligence: OCR, Handwriting/Screenshot Type Copy, Translation | 7 | P04, P09 runtime | 2 |
| P06 | `P06_Template_Library_and_AI_Drafting_Studio.md` | Template Library and AI Drafting Studio | 8 | P03, P04, P09 runtime | 1 |
| P07 | `P07_Contract_Lifecycle_Negotiation_Redlines_and_Deal_Rooms.md` | Contract Lifecycle: Negotiation, Redlines, Deal Rooms, Messaging, Approvals | 8 | P04, P06 | 1 |
| P08 | `P08_eSign_eStamp_Execution_and_Evidence.md` | eSign, eStamp, Execution and Evidence | 8 | P01, P04, P07 | 1 |
| P09 | `P09_Vidhi_AI_Employee_and_Agent_Workforce.md` | Vidhi AI Employee and Agent Workforce | 10 (runtime 4 in Wave 1) | P02, P03, P04 | 1–3 |
| P10 | `P10_Pleadings_Notices_and_Court_Drafting_Studio.md` | Pleadings, Notices and Court Drafting Studio | 6 | P05, P06 | 2 |
| P11 | `P11_Litigation_and_Matter_Management.md` | Litigation and Matter Management | 9 | P04, P10, P19 core | 2 |
| P12 | `P12_IP_and_Trademark_Portfolio.md` | IP and Trademark Portfolio | 6 | P04, P11 | 2 |
| P13 | `P13_Company_Legal_Department_OS_Governance_and_HRMS.md` | Company Legal Department OS, Governance and HRMS | 10 | P02, P04, P07, P11 | 2 |
| P14 | `P14_Business_Services_Start_a_Business_Compliance_and_Tax.md` | Business Services: Start a Business, Compliance Services and Tax | 8 | P16, P17 | 3 |
| P15 | `P15_Consumer_Help_Grievances_Challans_and_Vehicles.md` | Consumer Help: Loan/Insurance Grievances, Challans and Vehicles | 9 | P04, P05, P10, P16 | 3 |
| P16 | `P16_Marketplace_Professional_Registry_Retainers_and_Academy.md` | Marketplace, Professional Registry, Retainers and FinLegal Academy | 8 | P07, P08, P17 | 2 |
| P17 | `P17_Plans_Subscriptions_Billing_Revenue_Streams_and_Savings.md` | Plans, Subscriptions, Billing, GST, Revenue-Stream Switches and Savings Dashboard | 7 | P02, P03 | 1 |
| P18 | `P18_Delivery_Console_and_Operations_Hub_Interface.md` | Delivery Console and Operations Hub Interface | 7 | P02, P04, P16, P17 | 2 |
| P19 | `P19_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md` | Integration Gateway, Ecosystem Connectors and Developer Platform | 9 (core 3 in Wave 1) | P00, P02 | 1–2 |
| P20 | `P20_Data_Preservation_Portability_BYO_Storage_and_Migration_Safety.md` | Data Preservation, Portability, BYO Storage and Migration Safety | 6 (core 2 in Wave 1) | P04 | 1–2 |
| P21 | `P21_Public_Website_CMS_SEO_GEO_Help_Centre_and_Accessibility.md` | Public Website, No-Code CMS (Blog/Vlog), SEO/GEO, Help Centre, Tutorials, "i" Glossary and Accessibility | 10 | P00 (SSR shell and redirect targets, needed by the P00 cut-over); P06 (Draft-free blocks) | 1–3 |
| P22 | `P22_Mobile_Apps_and_Store_Release.md` | Mobile Apps (iOS/Android) and Store Release | 9 | P01, P04, P08, P19 | 2 |
| P23 | `P23_Engineering_Governance_Change_Patch_Hardening_Audit_and_GoLive.md` | Engineering Governance, Change/Patch Management, Hardening, VAPT/IS Audit, Certification Readiness and Go-Live | 6 (re-run per wave) | all | each wave |

**Waves.** Wave 1 "Vault & Sign GA" (individuals, startups, SMEs): P00 → P01 → P02 → P03 → P04 → P06 → P07 → P08, with P09 runtime, P17, P19 core, P20 core, P21 core (site + top 50 pages + marketplace storefront shell); then P23. Wave 2 "Legal Ops for companies": P05, P10, P11, P12, P13, P16, P18, P19 full, P20 full, P22, P09 workforce L0–L2 (company panel, MCP server); then P23. Wave 3 "Services and Consumer": P14, P15, P09 full agent workforce, P21 full content, P22 v2; then P23.

**Total indicative effort:** about 186 squad-sprints (two-week sprints, squads of 8), excluding P23 re-runs. With six squads in parallel, Wave 1 GA in about 12 sprints (≈ 6 months), Wave 2 by about sprint 24 and Wave 3 by about sprint 34; with three squads expect 60–65 sprints. Treat these as planning ranges, not commitments.

### 13.2 Waves and release gates

| Wave | Goal | Phases | Gate |
|---|---|---|---|
| 1 — Vault & Sign GA | Individuals, startups and SMEs can draft, negotiate, stamp, sign, store, share and export; storefront and pricing live | P00 → P01 → P02 → P03 → P04 → P06 → P07 → P08; with P09 runtime, P17, P19 core, P20 core, P21 core (site, top 50 pages, storefront shell, policies) | P23 go-live checklist; VAPT; accessibility audit; counsel sign-off on Appendix F rows used, Appendix O policies and the "Draft free" flow (NN-14) |
| 2 — Legal Ops for companies | Company Legal Department OS, litigation, IP, pleadings, document intelligence, marketplace and delivery console, mobile apps | P05, P10, P11, P12, P13, P16, P18, P19 full, P20 full, P22, P09 workforce L0–L2 | P23 re-run; court-data vendor certification; marketplace counsel opinion (NN-21) |
| 3 — Services and Consumer Help | Business services, Startup Desk, tax workspace, Consumer Help brand, full agent workforce, full content migration | P14, P15, P09 full, P21 full content (≈ 626 pages), P22 v2 | P23 re-run; Consumer Help entity, terms and fee model approved [COUNSEL]; ERI/GSP route confirmed |

### 13.3 Content runs in parallel

Template rewriting (Appendix E, ≈ 327 canonical documents, 70 pleading pages, 48 services) and website copy (content deck + Appendix N) run alongside engineering, through Content Studio, with a reviewer of record per item; copied third-party text and outdated law (CrPC/IPC/Evidence Act → BNSS/BNS/BSA; Consumer Protection Act 1986 → 2019; Udyog Aadhaar → Udyam; Income-tax Act 1961 → 2025 [VERIFY]; Labour Codes) are rewritten before publication (D-04, X-24).

---

## 14. Quality, security and performance standards

| Area | Standard |
|---|---|
| Tests | Unit ≥ 80% on domain modules; contract tests for every port and ecosystem contract; Gherkin acceptance per phase; NN tests (§4); journey tests J-01…J-40 with click budgets (Appendix C); golden files for redlines, DOCX/PDF output, archives |
| Performance | Public pages: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at p75 on mid-range Android over 4G; app API p95 ≤ 300 ms (reads) / 800 ms (writes); search p95 ≤ 1 s; vault upload resumable; signing ceremony page ≤ 2 s |
| Availability | 99.9% monthly for apps/web, apps/api and signing; RPO ≤ 15 min, RTO ≤ 4 h (Appendix P; P23) |
| Accessibility | WCAG 2.2 AA + IS 17802; automated and manual gates per release (NN-28; Appendix U) |
| Security | ASVS L2/L3; no critical/high open findings at release; dependency SLAs (critical 72 h, high 7 days); secrets scanning; SBOM per build |
| Privacy | DPIA per high-risk feature (vault, KYC, AI, consumer help, credential vault); RoPA maintained; data minimisation reviews per phase |
| Localisation | D-07 languages; Indic script rendering checked; legal translations labelled (NN-48) |
| Documentation | ADRs; interface docs; runbooks; help-centre articles and "i" keys for every new term; release notes in plain English |

---

## 15. Definition of Done (every story)

1. Acceptance criteria met and demoed; Gherkin passes in CI.
2. RLS, authorisation and IDOR tests pass for every new endpoint (NN-01).
3. Audit events written in-transaction (NN-45); correction paths defined for finalised records (NN-02).
4. Settings registered in Appendix R / registry (NN-29); flags and kill switches named with approvers (NN-38, NN-39).
5. Export-map entry registered and covered by the golden-archive test (NN-11).
6. Migration is expand-migrate-contract with rollback notes (NN-12).
7. Accessibility checks pass (keyboard, screen reader, contrast, zoom) (NN-28).
8. Help keys and "i" text registered for new jargon; help article drafted (OP-9).
9. Privacy: data classes tagged; logs scrubbed (NN-32); DPIA delta noted.
10. Legal facts used are verified or the feature is flagged OFF (NN-38); verification log updated.
11. Click budget for the journey measured and within target (OP-10).
12. Mobile behaviour defined (responsive web and, where in scope, app parity).
13. Documentation, release note and runbook updated; no hidden blocker; out-of-scope findings logged as backlog or owner decisions.

---

## 16. Source materials (consult; do not copy blindly)

| Source | Use |
|---|---|
| Owner's brief (25 Oct 2026) | Requirements R-001…R-092; traced in Appendix Z (581 rows) |
| Owner's manuals: Documents, Pleadings and Court Drafts, Compliance, Start a Business | Template, pleading and service taxonomy (Appendix E); website content (content deck, Appendix N, P21). Contain copied third-party text and outdated law — rewrite before use |
| Earlier ChatGPT master prompt | Hard boundaries and scope catalogue (traced, Appendix Z TC rows) |
| Research notes R1–R6 (`_research/`) | Competitors, consumer verticals, legal baseline, Jio/AI/growth, site inventory, pricing and data sources |
| Companion packs | Ecosystem Spec v1.1 (canonical for cross-product contracts), Operations Hub v1.0, LawDocsComply v1.2, Equator v3.1 |
| Live sites | lawdocs.in (186 sitemap URLs; redirect map in P00/P21), trainings.lawdocs.in (Graphy, 16 courses) |

---

## 17. Glossary (short; the full "i" registry is P21 and Appendix N)

**ASP** — Application Service Provider that integrates eSign under contract with an ESP. **ESP** — eSign Service Provider licensed by CCA. **OVSE** — offline verification-seeking entity under Aadhaar regulations. **eStamp** — electronic stamp certificate issued through authorised channels. **CNR** — unique case number in eCourts. **Type copy** — a typed transcription of a handwritten or image document, filed with the original. **s.63 certificate** — the certificate for electronic records under the Bharatiya Sakshya Adhiniyam 2023. **Maker / Checker** — the person who prepares and the person who approves; never the same for controlled actions. **Delivery grant** — a client-approved, time-bound permission for LawDocs staff or a professional to work in the client's workspace. **Retainer** — a continuing engagement with agreed scope, hours and SLA. **SoR** — system of record.

---

## 18. Document precedence and cross-file resolutions (binding)

**Precedence on conflict:** this master → `02` decision log → Appendix G (legal rules) → Appendix F (instrument eligibility) → Appendix B (data model, events, errors) → Appendix A (state machines) → Appendix D (roles and access) → Appendix R (settings) → Appendix C (IA and screens) → the phase file → other appendices → research notes. The Ecosystem Integration Specification prevails for cross-product contracts; a needed change is raised through Appendix Y, never improvised. Where a phase file and an appendix disagree on a detail the phase owns (its tables, its defaults), the owning phase wins unless an NN rule says otherwise (X-11).

### 18.1 Cross-file resolutions made at integration
| ID | Conflict | Resolution |
|---|---|---|
| X-01 | ID prefixes introduced by phase authors not in conventions §5 | Accepted and registered in Appendix B: `aev_ cor_ anc_ mig_ bkf_ brd_ ope_ mbr_ ivt_ dev_ ntv_ onb_ pcr_ gdn_ brn_ tem_ apr_ dlg_` (P00–P02), `shr_ hld_ svw_ nom_ sgb_` (P04/P08), `nbk_ qrv_` (P09), `dlv_ tme_ dls_` (P18), `tfl_` (P14), `clk_ cnl_ lsi_ exa_ lrq_` (P11/P13); business refs `LD-ORD-`, `LD-LRQ-`. |
| X-02 | R5 CSV eSign flags vs R3 LG-003 | IT Act First Schedule entry for "contract for sale or conveyance of immovable property" was omitted on 26 Sep 2022 [VERIFY/COUNSEL] → agreements for sale are eSign-eligible (conveyance/sale deeds still need registration). Affidavits, vakalatnamas, pleadings, adoption deeds are not plain "Valid" (oath/notary/forum rules). **Appendix F §9 governs; R5 CSV eSign column is superseded.** |
| X-03 | R4 §11.6 flat listing fee for advocates | Rejected. No fee of any kind from advocates (D-05, NN-21). |
| X-04 | NN-13 per-action confirmation vs bounded reminder/nudge plans | One confirmation of an **itemised, bounded send-plan** (every message, recipient, channel and date listed) satisfies NN-13; any change re-requires confirmation; setting `agt.send_plan.mode` default `itemised_confirmation`; [OWNER]/[COUNSEL] OI. |
| X-05 | OH v1.0, LDC FR-P18-22/-40 and EQ AC treat "LawDocs eSign" as a provider other products call | Breaches NN-06. Replaced by **hosted hand-off**: signing always happens on a LawDocs-hosted page within a LawDocs customer relationship; other products receive status/evidence only. Companion change requests to OH, LDC v1.3, EQ v3.2 (master §19). [COUNSEL] confirm. |
| X-06 | LDC v1.2 P26/D-41 builds its own legal-matter and contract register vs D-10 | When a tenant uses both, LawDocs is SoR for legal matters, contracts, IP; LDC P26 registers become projections (`lit.sor.mode`). Companion change request to LDC; [OWNER] confirms. |
| X-07 | Conventions §14 export layout vs Ecosystem Spec §12.1 | Appendix K governs (follows Appendix Y §Y.11.2: `00 Start Here/` folder, spec root naming with `owner_readable` naming mode; personal data in folder names only when the owner enables readable naming). Conventions §14 superseded. |
| X-08 | Archive profiles | Appendix Y registers `ld_company_v1`, `ld_individual_v1`, `ld_professional_v1`, `ld_consumer_help_v1`. |
| X-09 | `lgo.waiting_items` (P13) vs `wf.items` (P03) | `wf.items` is the single engine; P13 uses a read view. |
| X-10 | Help-key namespace overlaps `hlp.*` settings | Help keys and settings are separate registries; general jargon uses `hlp.gen.<term>` (replace any `hlp.hlp.`). |
| X-11 | Appendix R defaults vs owning phases | Owning phase wins: `kyc.digilocker.retain_copy` default OFF; `org.master_data.change_policy` has no `owner_only` option (NN-18); `gov.mode`/`hr.mode` replaced by `int.eco.ldc.sor_mode.governance` / `.hrms`; OVSE flag split into `kyc.ovse.qr.enabled` and `kyc.ovse.avc.enabled`. |
| X-12 | Appendix K gaps | Add `06 Policies and Registers/Contract Templates and Playbooks/`; add company tax folder; individual tax folders labelled "Tax Year <YYYY-YY>" (Income-tax Act 2025 terminology [VERIFY]) with legacy "AY" alias for pre-2026 years. |
| X-13 | Consumer invoicing on OH8 vs Spec data class INTERNAL | Only billing fields (name, email, phone, optional GSTIN/address, amounts, SKU) go to OH8 under legal basis `CONTRACT_PERFORMANCE_CUSTOMER`; no case content; DPO sign-off [OI]. |
| X-14 | Aadhaar in uploads | Store only the masked rendition plus a pre-mask SHA-256; no unmasked option for any role; [COUNSEL]. |
| X-15 | NN-06 wording vs D-12 aggregator-first | NN-06 reads: "eSign only through a licensed ESP, via a contracted aggregator acting as ASP or LawDocs' own ASP arrangement (`asp_mode` per vendor), never sublet". |
| X-16 | ESP licence status | Routing blocks any ESP whose CCA licence is lapsed (Capricorn lapsed 15 May 2026) or expires (Protean 26 Oct 2026) unless renewal evidence is recorded [VERIFY]. |
| X-17 | Consumer Help storage | P15's separate database (logical cell) for the Consumer Help brand is the default; cost is an [OWNER] decision. |
| X-18 | Government fees | Default: customer pays the official portal directly; LawDocs collects only its own and the professional's fee; optional pure-agent collection OFF pending [TAX MEMO]. |
| X-19 | Assigned-professional model vs client choice (R3 LG-113) | Buyer may request a different professional (once by default, configurable); counsel confirms the model. |
| X-20 | Ops creating maker users for a client | Client-approved standing authorisation, OFF by default. |
| X-21 | Marketplace model letters | LawDocs: M1 LawDocs-delivered, M2 Route-collected third-party, M3 direct engagement (differs from LDC lettering — note in Appendix M). |
| X-22 | Content Studio location | `apps/console` "Content Studio" area, restricted to `OPS_CONTENT_PUBLISHER`, `PLT_CONTENT_EDITOR`, `PLT_LEGAL_REVIEWER`; Super Admin not required. |
| X-23 | Pleading page count | 70 consolidated pleading pages (P10/Appendix E) supersede R5's ≈68. |
| X-24 | Copied content list | Add "StartupSeven" mention (Compliance manual l.1060) to the rewrite list. |
| X-25 | Phase lengths over target | Accepted; precision preferred over brevity. |
| X-26 | `chp` Consumer Help case manager and ethical wall | `int.chp.ecosystem_clients.allowlist` empty by default; no Udofin grievance is routed to the Consumer Help brand. |
| X-27 | Agent names across phases | Appendix H roster (37 agents) is canonical; phases use those codes. |
| X-28 | Error code ranges | `LD-WF-001–099` P02 (maker-checker/DoA), `LD-WF-100–149` P03 (items engine). Other module ranges as declared in each phase. |
| X-29 | Court/TM data ports | Appendix I `COURT_DATA_PORT` and `TRADEMARK_DATA_PORT` include the operations P11/P12 use; no WIPO scraping actor (NN-05). |
| X-30 | Appendix O gherkin tags `@APPO-AT-nn` and POL-LD-01…17 policy register | Accepted; P21 renders policies from the POL register. |

---

## 19. Changes required in companion documents

| Companion | Change | Ref |
|---|---|---|
| Ecosystem Integration Spec → v1.2 | Register LawDocs (`LD`) per Appendix Y: product row, entities #46–#54, event domains `legal`, `esign`, `ip`, `engagement`, ADR party-initiated referrals, governance routing amendment, archive profiles `ld_company_v1`, `ld_individual_v1`, `ld_professional_v1`, `ld_consumer_help_v1`, scopes, legal basis `CONTRACT_PERFORMANCE_CUSTOMER`, data class `CONSUMER_HELP`, principles 14–15, certification group "Legal-tech boundaries"; plus proposed events `ServiceOrderStatusChanged`, `ServiceOrderRouted`, `MarketplaceTransferInstructed`, LawDocs as `UsageRecorded` producer, OH delivery-metric events, cross-product customer sign-in by token exchange | Appendix Y; X-05, X-08, X-13; Appendix B §B.4 |
| Operations Hub v1.0 → v1.1 | LawDocs legal-entity scope; CRM pipelines; autopilot marketing engine; content ops; Brevo sync; consumer-help billing fields only; six OH8 stream types; LawDocs as caller of CRM, ticket and asset-library APIs; remove "LawDocs eSign as provider" (hosted hand-off) | Appendix X Part 1; X-05, X-13 |
| LawDocsComply v1.2 → v1.3 | Shared governance/HRMS kernels and SoR switch; P26 legal-matter/contract registers become projections when the tenant uses LawDocs; storefront listings via D-11; remove LDC FR-P18-22/-40 "LawDocs eSign as provider" | Appendix X Part 2; X-05, X-06 |
| Equator v3.1 → v3.2 | ADR referral from LawDocs matters with consent; LawDocs-hosted signing hand-off (AC appendix) | Appendix X Part 3; X-05 |
| Finbyx v1.5 / Udofin v1.2 | Template supply and legal-notice drafting contracts; no LawDocs eSign sublet; Udofin borrower vault opt-in; no grievance routing to the Consumer Help brand | Appendix X Part 3; X-26 |

---

## 20. Management decisions (25 October 2026)

| ID | Decision |
|---|---|
| D-01 | Ecosystem stack (master §5.1); migrate off Vite/Express/MongoDB/Railway in P00 with redirects. |
| D-02 | Shared group **Operations Hub** (CRM, onboarding factory, support desk, customer success, marketing and brand, social calendar, PR/collaborations, staff HRMS, payroll, leave, appraisal, internal controls, billing OH8) + a **LawDocs Delivery Console** (`apps/delivery`) for client service delivery. LawDocs never re-builds OH functions; Appendix X lists what OH must add. |
| D-03 | Client portal credentials only in the encrypted, client-owned credential vault (NN-16). |
| D-04 | Website copy: content system + page inventory + ~15 flagship pages rewritten now (content deck); P21 rewrites the remaining ~600 pages from the manuals; all copied third-party text is replaced; outdated law references are corrected (R5). |
| D-05 | Marketplace with **per-profession commercial switches**. Lawful defaults (amended after research, R3/R6): advocates — no listing fee, no commission, no paid ranking; buyer pays a separate disclosed LawDocs platform fee; CA/CS — practising-member listing and any % model OFF pending ICAI/ICSI-compliant structure; LawDocs-employed professionals deliver non-reserved services at LawDocs prices; any percentage/subscription switch for regulated professionals is locked until counsel opinion + checker approval (NN-21). |
| D-06 | **Consumer Help** is a separate configurable brand + entity profile on the same platform with an ethical wall (NN-23). Placeholder brand: `[Consumer Help Brand]`. |
| D-07 | Languages: UI and Vidhi in English, Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Kannada, Malayalam, Punjabi at launch; document OCR/translation input supports all 22 Eighth-Schedule languages + the six UN official languages (Arabic, Chinese, English, French, Russian, Spanish), labelled machine translation (NN-48). |
| D-08 | Operating entity is a placeholder `[LawDocs Operating Entity]` (CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer configured in Super Admin). |
| D-09 | 24 phases P00–P23 (master §13). |
| D-10 | LawDocs is system of record for legal work (CLM, eSign/eStamp, vault/DMS, litigation, IP, pleadings, notices, legal advisory engagements, consumer help, startup desk, business-service orders). LawDocsComply is system of record for compliance, governance and client HRMS. Common code in shared kernels; a LawDocs-only company mounts Governance and HRMS locally; when the company also uses LDC, LDC is SoR with SSO and no double entry. |
| D-11 | One group **services storefront** at lawdocs.in/marketplace for LawDocs and LawDocsComply services plus FinLegal Academy courses; catalogue, prices, quotes, orders, GST invoices and Razorpay run on OH8; LDC shows the same listings in-app. Browsing needs no login and no subscription. |
| D-12 | eSign/eStamp/KYC through provider-neutral adapters, **aggregator first** (Leegality / Digio / Melento (formerly SignDesk) / Surepass-type), with a second ESP route as required by the eSign API spec [VERIFY v3.3 two-ESP rule — R3]; P00/P08 verify each vendor's ASP/ESP structure; LawDocs may become its own ASP with a direct ESP later without code change. |
| D-13 | Advertising: switch default OFF; public content pages only (NN-35). |
| D-14 | AI provider: Claude (owner supplies API/Bedrock credentials); provider-neutral gateway; Jio and Indic providers as adapters after verification. |
| D-15 | Brand of the AI employee: **Vidhi** (Vidhi AI). |
| D-16 | Academy brand: **FinLegal Academy** at trainings.lawdocs.in (currently on Graphy — R5); integrate by catalogue feed/deep links/SSO where Graphy supports it; never copy paid course content. |
| D-17 | Positioning: "your legal team in an app" is expressed as **legal operations + AI + on-demand professionals** — never as a replacement for advocates (CH-14). |

*End of master prompt.*


---

# PART B — REQUIREMENTS MAP AND DECISION LOG

Companion to `01_MASTER_PROMPT.md`. Paste after the master prompt in every session. Precedence: master §18.

---

## 1. Purpose and sources

This file records (a) every decision the owner has taken, (b) every place the pack challenged the brief and what it builds instead, (c) decisions still pending, (d) questions for counsel and tax advisers, (e) assumptions and external dependencies, and (f) the coverage map from every brief requirement (R-001…R-092) to phases and appendices. The atomic traceability (581 rows: 398 owner-brief rows TM-…, 125 ChatGPT-prompt rows TC-…, 58 manual rows MW-…) is Appendix Z.

Sources: the owner's brief of 25 October 2026; the four Word manuals (Documents; Pleadings and Court Drafts; Compliance; Start a Business); the earlier ChatGPT master prompt; the owner's answers in plan mode on 25 October 2026 (four rounds of questions, D-01…D-13); research streams R1–R6 (`_research/`); and the companion packs (Ecosystem Spec v1.1, Operations Hub v1.0, LawDocsComply v1.2, Equator v3.1).

---

## 2. Decisions

### 2.1 Owner decisions taken on 25 October 2026 (plan mode and pack lead)

| ID | Decision |
|---|---|
| D-01 | Ecosystem stack (master §5.1); migrate off Vite/Express/MongoDB/Railway in P00 with redirects. |
| D-02 | Shared group **Operations Hub** (CRM, onboarding factory, support desk, customer success, marketing and brand, social calendar, PR/collaborations, staff HRMS, payroll, leave, appraisal, internal controls, billing OH8) + a **LawDocs Delivery Console** (`apps/delivery`) for client service delivery. LawDocs never re-builds OH functions; Appendix X lists what OH must add. |
| D-03 | Client portal credentials only in the encrypted, client-owned credential vault (NN-16). |
| D-04 | Website copy: content system + page inventory + ~15 flagship pages rewritten now (content deck); P21 rewrites the remaining ~600 pages from the manuals; all copied third-party text is replaced; outdated law references are corrected (R5). |
| D-05 | Marketplace with **per-profession commercial switches**. Lawful defaults (amended after research, R3/R6): advocates — no listing fee, no commission, no paid ranking; buyer pays a separate disclosed LawDocs platform fee; CA/CS — practising-member listing and any % model OFF pending ICAI/ICSI-compliant structure; LawDocs-employed professionals deliver non-reserved services at LawDocs prices; any percentage/subscription switch for regulated professionals is locked until counsel opinion + checker approval (NN-21). |
| D-06 | **Consumer Help** is a separate configurable brand + entity profile on the same platform with an ethical wall (NN-23). Placeholder brand: `[Consumer Help Brand]`. |
| D-07 | Languages: UI and Vidhi in English, Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Kannada, Malayalam, Punjabi at launch; document OCR/translation input supports all 22 Eighth-Schedule languages + the six UN official languages (Arabic, Chinese, English, French, Russian, Spanish), labelled machine translation (NN-48). |
| D-08 | Operating entity is a placeholder `[LawDocs Operating Entity]` (CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer configured in Super Admin). |
| D-09 | 24 phases P00–P23 (master §13). |
| D-10 | LawDocs is system of record for legal work (CLM, eSign/eStamp, vault/DMS, litigation, IP, pleadings, notices, legal advisory engagements, consumer help, startup desk, business-service orders). LawDocsComply is system of record for compliance, governance and client HRMS. Common code in shared kernels; a LawDocs-only company mounts Governance and HRMS locally; when the company also uses LDC, LDC is SoR with SSO and no double entry. |
| D-11 | One group **services storefront** at lawdocs.in/marketplace for LawDocs and LawDocsComply services plus FinLegal Academy courses; catalogue, prices, quotes, orders, GST invoices and Razorpay run on OH8; LDC shows the same listings in-app. Browsing needs no login and no subscription. |
| D-12 | eSign/eStamp/KYC through provider-neutral adapters, **aggregator first** (Leegality / Digio / Melento (formerly SignDesk) / Surepass-type), with a second ESP route as required by the eSign API spec [VERIFY v3.3 two-ESP rule — R3]; P00/P08 verify each vendor's ASP/ESP structure; LawDocs may become its own ASP with a direct ESP later without code change. |
| D-13 | Advertising: switch default OFF; public content pages only (NN-35). |
| D-14 | AI provider: Claude (owner supplies API/Bedrock credentials); provider-neutral gateway; Jio and Indic providers as adapters after verification. |
| D-15 | Brand of the AI employee: **Vidhi** (Vidhi AI). |
| D-16 | Academy brand: **FinLegal Academy** at trainings.lawdocs.in (currently on Graphy — R5); integrate by catalogue feed/deep links/SSO where Graphy supports it; never copy paid course content. |
| D-17 | Positioning: "your legal team in an app" is expressed as **legal operations + AI + on-demand professionals** — never as a replacement for advocates (CH-14). |

### 2.2 How each decision changed the pack

| Decision | Effect |
|---|---|
| D-01 | P00 migrates the live Vite/Express/MongoDB/Railway site; every phase uses the locked stack (master §5.1). |
| D-02 | No CRM, HR, payroll, appraisal, marketing or billing engine is built in LawDocs; P18 builds the Delivery Console; Appendix X lists what the Operations Hub adds. |
| D-03 | P18 §credential vault and NN-16; feature OFF by default; delegation-first. |
| D-04 | Content deck (15 flagship pages) now; P21 and Appendix N migrate ≈ 626 pages; Appendix E flags copied/outdated content. |
| D-05 | P16, Appendix M: lawful defaults; locked switches; Route split; buyer-side platform fee. |
| D-06 | P15 + Appendix S; separate brand domain, entity profile, cell and ethical wall. |
| D-07 | P05, P09, P21, P22 language plans; NN-48. |
| D-08 | Every policy, invoice and footer uses `[LawDocs Operating Entity]` placeholders configured in Super Admin. |
| D-09 | 24 phases. |
| D-10 | P13 mounts shared kernels; `int.eco.ldc.sor_mode.*`; X-06 for legal matters. |
| D-11 | P16 storefront serves LawDocs and LDC listings; OH8 catalogue. |
| D-12 | P08 adapters; `asp_mode` per vendor; second-ESP route; licence-expiry monitoring. |
| D-13 | P17 stream registry; NN-35. |
| D-14–D-17 | P09 gateway; Vidhi brand; Academy integration; positioning copy in the content deck. |

### 2.3 Amendments after research (pack lead; owner may reverse)

| ID | Amendment | Why |
|---|---|---|
| D-05A | Advocates pay no fee of any kind (listing, subscription, commission, lead or ranking); buyer-side platform fee only | BCI Rules 36/37/20; Madras HC 3 Jul 2024 (R1, R3 LG-110–LG-113); R4's flat listing-fee idea rejected (X-03) |
| D-05B | Practising CA/CS listings and any percentage model locked OFF until an ICAI/ICSI-compliant structure and counsel opinion exist | ICAI 23 Oct 2019 aggregator restrictions (R3 LG-114–LG-117) |
| D-12A | eSign capability is never offered to other group products as a provider; hosted hand-off instead | CCA ASP no-sublet rule (R3); X-05 |
| D-12B | ESPs with lapsed or expiring CCA licences are blocked without renewal evidence | R3 found Capricorn lapsed (15 May 2026) and Protean expiring (26 Oct 2026) [VERIFY]; X-16 |
| D-07A | Six UN official languages are for reading/translation input only; court filings use certified translations | CH-11; NN-48 |
| D-11A | Consumer billing data sent to OH8 is limited to billing fields under legal basis `CONTRACT_PERFORMANCE_CUSTOMER` | Ecosystem Spec principle 12; X-13 |

---

## 3. Challenges to the brief (R-001)

Each row states the owner's wish, why it cannot be built as asked, and what the pack builds instead. Rule references are to Appendix G.

| CH | Brief's wish | Conflict | What the pack builds instead |
|---|---|---|---|
| CH-01 | Individuals "login through Aadhaar" | Aadhaar Act s.4(4): authentication only where Parliamentary law or a prescribed purpose allows; s.57 private-entity use omitted (2019 Amendment Act, after *Puttaswamy* 2018); Aadhaar must be voluntary with alternatives (LG-021–LG-025) | Login by mobile/email OTP, passkey, password + MFA or SSO (NN-03); Aadhaar used only for offline verification as an OVSE [VERIFY] and for ESP eSign (P01, P08) |
| CH-02 | Aadhaar APIs "automatically fetch the details" | LawDocs is not an AUA/KUA; an OVSE may not store the number (s.8A(4)); s.29(4) masking | Aadhaar App credential/QR verification; store only needed signed attributes + last 4 digits; auto-masking in uploads (NN-04, X-14) |
| CH-03 | CKYC-based APIs | CKYCR is for PMLA reporting entities (LG-046) | DigiLocker and Entity Locker with consent; no reuse of a sister RE's CKYC result |
| CH-04 | PAN APIs | Direct PAN verification is limited to enumerated entities (LG-047) | DigiLocker PAN + name match; licensed vendor only with a lawful-upstream warranty |
| CH-05 | CIBIL APIs at registration | CICRA s.17(4) and s.22 (offence); specified users only (LG-056–LG-060) | No bureau pull; users upload their own reports; credit-report dispute drafting in Consumer Help |
| CH-06 | Company-registration APIs | No open MCA API; scraping breaches terms | Licensed MCA-data vendors (Probe42/Signzy/Surepass/Perfios-Karza) or user-initiated lookup; Entity Locker (P01, P19) |
| CH-07 | Password tracker where client and LawDocs staff view and change portal passwords (CERSAI, MCA, CIBIL, Experian, GST, RBI CIMS, Daksh, Pravaah…) | Credentials and DSCs are issued to named officers; sharing defeats attribution required by RBI cyber/outsourcing directions, SOC 2 and ISO 27001; IT Act s.66C/s.72A exposure; acting inside a regulator portal as a client officer is impersonation | Delegation first (practitioner roles, separate named users where portals allow); otherwise a client-owned, envelope-encrypted vault with masked entries, just-in-time reveal with reason + client approval, time-boxing, tamper-evident logs, no OTP/DSC PIN storage; OFF by default (D-03, NN-16, P18) |
| CH-08 | Advocates on subscription or percentage basis; ratings and testimonials | BCI Rules 36, 37, 20 and the fee-sharing bar; Madras HC 2024 (SC pending, no stay) | Fixed-price services fulfilled by assigned professionals; Rule-36-only directory OFF until counsel opinion; buyer-side platform fee; no ratings/testimonials about advocates (D-05A, NN-21) |
| CH-09 | CAs and CSs on subscription or percentage basis | CA Act Schedule I; ICAI 2019 aggregator restrictions; CS Act analogues | LawDocs-employed professionals deliver non-attest services; attest work by independent practitioners engaged directly; switches locked (D-05B) |
| CH-10 | LawDocs team files returns using client passwords | Returns must be verified by the taxpayer; credential sharing defeats verification (LG-125/126) | ERI route with client consent and taxpayer EVC/DSC; GST practitioner roles; TDS by deductor or ERI (P14) |
| CH-11 | Identify and read "UN-approved languages" and all main Indian languages; attach AI translations to petitions | The UN has six official languages; courts need court-language filings and certified translations | D-07 phased languages; UN languages for reading only; labelled machine translation; certified-translation hand-off (NN-48, P05) |
| CH-12 | eSign for all personal, business and property contracts | IT Act First Schedule still excludes wills, trusts, ordinary POAs and most negotiable instruments; sale deeds and long leases need registration; affidavits need oath | Instrument eligibility gate with wet-ink, notary and registration packs (NN-07, NN-40, Appendix F) |
| CH-13 | "Buy stamp papers online" through an eStamp API | Only the CRA, ACCs and licensed vendors issue; coverage differs by State | Agent procurement via a contracted ACC/aggregator; duty passed through at actuals; State coverage registry; stamp-before-sign; UIN checks (NN-08) |
| CH-14 | "The tool shall be sufficient instead of a legal team" | Only advocates practise law and appear in court; a company cannot (LG-110) | Legal-operations platform run by a CLO with Vidhi agents and engaged advocates; party-in-person tools for individuals (D-17, NN-41) |
| CH-15 | Vault "like DigiLocker", kept forever | LawDocs is not a DigiLocker service provider; requester terms bar storage beyond purpose (LG-036–LG-041) | "Legal Vault": DigiLocker URI + verification; copy retained only for a recorded permitted purpose; user uploads stored with hashes (NN-42) |
| CH-16 | Data freely shareable across ecosystem apps | DPDP purpose limitation and consent; DigiLocker terms; eSign no-sublet; CICRA | Purpose-bound, consented, ledgered sharing through registered contracts (NN-24, Appendix Y) |
| CH-17 | Jio automated and AI calling | TCCCPR/DLT, consent, pre-declared numbers (2026 amendment), AI-voice labelling | DLT-registered telemarketer route, consent, calling windows, disclosure and human hand-off (NN-34, Appendix J) |
| CH-18 | "In consonance with GDPR, CCPA" | Apply only when their territorial triggers are met | DPDP-first design with GDPR-grade controls; jurisdiction flags switch on supplements (Appendix O, P) |
| CH-19 | PCI-DSS "certification" | Hosted-checkout merchants self-assess (SAQ A) | Hosted/tokenised Razorpay checkout; SAQ A attestation; copy says "LawDocs never stores card data" (NN-22) |
| CH-20 | Testimonials on every page | BCI Rule 36 for advocates; fake-review rules (IS 19000, E-Commerce Rules) | Genuine, consented, verified-purchase testimonials about LawDocs' own services only, without photos (NN-49) |
| CH-21 | Advertisements as a revenue stream | Advocate advertising barred; targeted ads raise DPDP issues; confidential areas | Switch OFF by default; contextual, labelled ads on public content pages only (NN-35) |
| CH-22 | Check, pay and contest challans; FREED-like loan and insurance grievance resolution | Collecting money for others is payment aggregation; no lawful third-party e-challan API; ombudsman representation rules; no outcome guarantees | Deep links to official portals for lookup and payment; contest via Virtual Courts/Lok Adalat or an engaged advocate; drafting and tracking while the user files; no money handled (NN-23, P15) |
| CH-23 | Sell vehicles through LawDocs | RC transfer happens on Vahan | Sale agreement + delivery note + pre-sale checks + Vahan checklist (P15) |
| CH-24 | "Employees cannot cheat"; login/logoff tracking | DPDP proportionality; productivity is not presence | Maker-checker, segregation, immutable logs, outcome and SLA metrics; sessions recorded for attendance only (NN-33; OH) |
| CH-25 | Marketplace and duty payments through LawDocs; saved cards | RBI PA Directions, card-on-file tokenisation, e-mandate rules | Route split settlement; tokens; e-mandates with pre-debit notices (NN-22) |
| CH-26 | Super Admin changes crucial client details | DPDP accuracy; evidence integrity; processor role | Master-data change requests with maker-checker, client approval, reason codes and client notification (P18) |
| CH-27 | Trademark and Provakil-like case tracking via APIs | No open eCourts/IP India APIs for LawDocs; scraping breaches terms | Licensed partners, user-entered numbers, assisted/manual refresh, staleness labels (P11, P12, NN-05) |
| CH-28 | AI reads WhatsApp screenshots and handwriting and attaches them to petitions | Screenshots are secondary evidence; s.63(4) certificate with hash needed | Native chat exports preferred; originals immutable and hashed at upload; labelled, correctable type copies; s.63 Part A/Part B workflow (NN-09, NN-10, P05) |
| CH-29 | "Microsoft 365 Business Starter" | "Business Starter" is a Google Workspace edition name; Microsoft's plans are Business Basic, Standard and Premium | Suite-neutral `WORKSPACE_PORT`; owner to confirm the actual plan [OWNER] |
| CH-30 | Free AI drafting of agreements on every page for individuals | Anthropic Usage Policy treats legal document preparation for individuals as high-risk: qualified human review before delivery and AI disclosure [VERIFY] | Free **template automation** from vetted templates; AI-customised drafts labelled "AI draft — not reviewed" with one-click paid professional review (NN-14, P06) |
| CH-31 | Success fees in grievance and claim help | Advocates cannot take contingent fees (BCI Rule 20) | Flat fees by default; success fee only in the non-advocate Consumer Help entity, capped, OFF by default [COUNSEL] |
| CH-32 | Login and logoff time as the measure of productivity | Presence is a poor and intrusive proxy | Attendance from declared sessions; productivity from outcomes and SLAs; no covert monitoring (NN-33) |

---

## 4. Owner decisions pending (needed before the phase named)

| # | Decision | Blocks |
|---|---|---|
| 1 | Confirm the Microsoft 365 plan actually held (CH-29) and the timing of any Google Workspace move | P18, P19 |
| 2 | Operating entity particulars: name, CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer (D-08) | P17, P21, Appendix O |
| 3 | Consumer Help brand name, domain and operating entity; separate cell cost (X-17) | P15, P21, P22 |
| 4 | Plan names and prices, monthly premium, trial length, refund window, credit validity, downgrade storage policy (Appendix L seeds) | P17, P21 |
| 5 | Revenue-stream waves; kill-switch approvers; second pricing approver | P17 |
| 6 | eSign/eStamp/KYC vendors (primary and second ESP) and the long-term own-ASP decision (D-12) | P01, P08 |
| 7 | Court-data vendors (two) and TM data partner | P11, P12 |
| 8 | Approve Appendix E starter lists for categories D5, D6, D7, D14, D15, D18 and the commissioned pleadings (Appendix E §4.3) | P06, P10 |
| 9 | Blog folder taxonomy from the owner's Word files; first 20 tutorial videos | P21 |
| 10 | AI-crawler policy for the public site (allow, allow-list, block) | P21 |
| 11 | Default AI autonomy ceilings per plan and human sponsors for agents at L2+ | P09 |
| 12 | Whether one itemised confirmation of a bounded reminder/nudge series satisfies NN-13 (X-04) [COUNSEL] | P03, P09 |
| 13 | SoR when a tenant uses both LawDocs and LDC for legal matters and contracts (X-06) | P11, P13, P19 |
| 14 | ~~Environment names~~ — resolved at review: `dev`, `test`, `staging`, `pre-prod`, `prod` (P23 governs) | — |
| 15 | Public phone number and support hours; support SLAs by plan | P18, P21 |
| 16 | In-app purchase mode on iOS/Android and GST on store sales [TAX MEMO] | P22 |
| 17 | ERI registration route for income-tax filing support; GSP partner | P14 |
| 18 | Professional panel structure for the marketplace (employed, empanelled, direct engagement) | P16 |
| 19 | Remove unevidenced claims from the live site and manuals now (blockchain, home delivery, "produced before any Court", "verified") | P00, P21 |
| 20 | One credential vault per client when the client also uses LDC (OI-X-05); grievance ownership across group products (OI-X-07) | P18 |

---

## 5. Questions for counsel and tax advisers

The full list is in Appendix W §W.5 (52 counsel questions, CQ-01…CQ-52) and §W.6 (17 tax-memo points). The most material:

1. Marketplace structure under BCI Rule 36 after the Madras HC 2024 judgment: assigned-professional model, buyer-side platform fee, Rule-36 directory content (NN-21).
2. ICAI/ICSI-compliant structures for CA/CS participation (D-05B).
3. Consumer Help entity: authority letters, representation before RB-IOS 2026 and the Insurance Ombudsman, success-fee legality and caps (CH-31).
4. First Schedule eligibility of agreements for sale after 26 Sep 2022; electronic attestation and witnesses (Appendix F).
5. Hosted eSign hand-off for other group products under the CCA ASP rules (X-05).
6. Aadhaar offline verification as an OVSE and masked-only storage (CH-01, CH-02, X-14).
7. DigiLocker retained copies (NeGD position) (NN-42).
8. DPDP roles: LawDocs as fiduciary or processor for company workspaces; group data sharing (CH-16).
9. Review gate wording for AI drafts and who may review (NN-14, CH-30).
10. Migration of users from the legacy contracting entity: fresh consent or notice (CQ-01).
11. [TAX MEMO] GST on credits and platform fees; RCM on advocates' services; e-commerce TCS/TDS; pure-agent treatment of stamp duty and government fees; Income-tax Act 2025 section mapping.

---

## 6. Assumptions

| # | Assumption | If wrong |
|---|---|---|
| A-1 | The owner supplies Claude credentials (Bedrock India and Anthropic API) | Gateway runs with another approved provider; AI features flagged |
| A-2 | At least one aggregator with ASP status and two ESP routes can be contracted before Wave 1 GA | eSign ships with DSC and wet-ink packs only |
| A-3 | The Operations Hub (OH8 billing, CRM, OH10) is available for Wave 1; otherwise a minimal billing adapter runs behind `BILLING_PORT` and migrates later | P17 builds a temporary adapter (flagged) |
| A-4 | The Consumer Help entity is incorporated before Wave 3 | P15 stays OFF |
| A-5 | Live-site users and orders can be migrated under notice (CQ-01) | Re-consent flow in P00 |
| A-6 | Graphy supports catalogue export and deep links for FinLegal Academy | Manual catalogue sync |

---

## 7. External dependencies

Vendor contracts (Appendix W §W.7, 32 items): AWS (and Bedrock), Anthropic, eSign aggregator(s) and second ESP, eStamp ACC/aggregator, DigiLocker requester onboarding, Aadhaar offline-verification route, MCA-data vendor(s), GSP, licensed court-data aggregators (two), TM data partner, JioCX and other CPaaS (DLT), WhatsApp BSP, Razorpay (via OH8), Microsoft Graph and Google Workspace app registrations, Brevo, translation and speech providers, VAPT auditor (CERT-In empanelled), SOC 2/ISO auditors, app-store developer accounts.

---

## 8. Requirements coverage map

Status counts from Appendix Z (after the traceability-review edits): owner brief 340 covered, 57 changed by decision, 1 partial (TM-296 Jio developer-page reading, OI-R4-01), 0 missing; ChatGPT prompt 121 covered, 4 changed by decision; manuals 49 covered, 9 partial (owner approvals in §4 item 8).

| R | Requirement | Phases | Appendices | Rows by status (Appendix Z) |
|---|---|---|---|---|
| R-001 | working agreement (challenge, don't auto-agree) | P00, P23 | — | COVERED 13; PARTIAL 1 |
| R-002 | ecosystem integration boundaries (Finbyx, Udofin, Equator, LDC, third parties) | P00, P10, P11, P13, P18, P19 | Y | COVERED 12 |
| R-003 | APIs/gateways for data transfer and easy onboarding of new companies | P00, P01, P19 | — | COVERED 5 |
| R-004 | use owner's Word files + deep research; Word/.md/phase files | P00, P21, P23 | — | COVERED 7; PARTIAL 2 |
| R-005 | individuals and companies; easy onboarding via Aadhaar/PAN/CKYC/DigiLocker/MCA/CIBIL APIs | P01, P02, P04, P05, P15, P22 | — | COVERED 8; CHANGED-BY-DECISION 5 |
| R-006 | business agreements + Aadhaar eSign | P06, P07, P08, P19 | — | COVERED 7 |
| R-007 | AI employee drafting (Vidhi) | P06, P08, P09 | — | COVERED 3 |
| R-008 | multi-language | P00, P06, P09, P21, P22 | — | COVERED 2 |
| R-009 | individual "Aadhaar login" and AI agreements | P01, P06 | — | CHANGED-BY-DECISION 1; COVERED 2 |
| R-010 | Vidhi answers user problems | P09 | — | COVERED 2 |
| R-011 | DigiLocker-like always-kept app: prepare, enter, eSign, amend, preserve; DMS | P04, P06, P07, P08, P11, P17, P20 | — | CHANGED-BY-DECISION 1; COVERED 7 |
| R-012 | litigation tracking for companies | P11, P12 | — | COVERED 4; CHANGED-BY-DECISION 1 |
| R-013 | trademark application tracking | P12 | — | CHANGED-BY-DECISION 1; COVERED 2 |
| R-014 | marketplace of advocates, tax assistants, CA, CS | P01, P06, P14, P16 | — | COVERED 5 |
| R-015 | Claude API for Vidhi | P09, P23 | — | COVERED 3 |
| R-016 | explore LegalKart and similar; parity | P09, P16 | — | COVERED 2 |
| R-017 | web app mobile-friendly; iOS/Android apps | P00, P02, P19, P21, P22 | — | COVERED 4; CHANGED-BY-DECISION 1 |
| R-018 | agentic AI for users, KMPs, boards; agents as employees | P03, P05, P07, P09, P11, P13, P23 | — | COVERED 9 |
| R-019 | "i" buttons/glossary | P00, P03, P09, P21 | — | COVERED 4 |
| R-020 | tutorials (text, images, diagrams, screenshots, videos) reusable on social | P21 | — | COVERED 6 |
| R-021 | data preservation/export/migration in standard folders and formats; BYO storage (servers, buckets, OneDrive, drives, data centre) | P04, P20, P22 | — | COVERED 16 |
| R-022 | structure preserved across code/infra changes; no manual migration | P00, P04, P18, P20, P23 | — | COVERED 11 |
| R-023 | data shareable across ecosystem apps both ways | P04, P19, P20 | — | CHANGED-BY-DECISION 2; COVERED 1 |
| R-024 | bulk intake via folder structure | P04, P11, P12, P20 | — | COVERED 3 |
| R-025 | accessibility for hearing/visually impaired, all types | P01, P21, P22, P23 | — | COVERED 4 |
| R-026 | faster cross-team/department workflows; better logic | P02, P03, P11, P12, P13, P16, P18, P21 | — | COVERED 4 |
| R-027 | extensive customisation in settings | P03 | — | COVERED 1 |
| R-028 | user types: super admin, operations hub, company admin, maker/checker etc., individuals — distinct features per type | P02, P03, P18 | — | COVERED 8 |
| R-029 | Jio AI services (agentic AI, agent calling, automated calling, marketing, research, drafting) | P03, P06, P09 | — | COVERED 3; CHANGED-BY-DECISION 5 |
| R-030 | detailed customisable content/features/UI; fewer clicks; automation | P03, P09, P11, P13, P17, P22 | — | COVERED 3 |
| R-031 | GDPR/CCPA/DPDP/IT Act/privacy compliance | P00, P01, P18, P19, P20, P21, P23 | — | CHANGED-BY-DECISION 2; COVERED 6 |
| R-032 | SEO/GEO/AI-search content; clean minimalist UI | P00, P21 | — | COVERED 7 |
| R-033 | certification readiness (PCI DSS, SOC 2 Type 1/2, ISO) | P17, P23 | — | CHANGED-BY-DECISION 1; COVERED 7 |
| R-034 | payment-gateway security; Razorpay | P16, P17, P19 | — | COVERED 3 |
| R-035 | billing/subscription in settings; plan up/downgrade | P17 | — | COVERED 3 |
| R-036 | subscription/business model and revenue streams per company type; 3-plan pricing page with feature list | P01, P17, P21 | — | COVERED 9 |
| R-037 | LawDocs services (returns, one-time, retainer) on marketplace; third-party professionals on subscription/% | P09, P14, P16, P17 | — | COVERED 9; CHANGED-BY-DECISION 3 |
| R-038 | service types (agreements, policies, annual reports, stress testing, compliance testing, risk assessment, retainer advisory, minutes) | P13, P16 | — | COVERED 10 |
| R-039 | custom solutions/pricing; customised retainers with eSigned SLAs | P16 | — | COVERED 4 |
| R-040 | services purchasable without SaaS subscription; billing, invoices, GST, emailed invoices, Razorpay | P16, P17, P18 | — | COVERED 8 |
| R-041 | FinLegal Academy courses on marketplace; marketplace open without login; categorised | P16, P21 | — | COVERED 5 |
| R-042 | recurring revenue architecture; explain plan benefits; detailed billing/membership settings | P17 | — | COVERED 4 |
| R-043 | advanced DMS (share, eSign, search, filter, selective sharing) | P04, P07, P08, P20 | — | COVERED 6 |
| R-044 | AI type copy of handwritten docs/WhatsApp screenshots attached to petitions; editable | P05, P10, P22 | — | COVERED 5 |
| R-045 | translation to English; UN + Indian languages | P05, P21 | — | COVERED 4 |
| R-046 | revise and fix errors | P00, P03, P14, P21 | Z | COVERED 2 |
| R-047 | customisable open/interim/waiting items; dynamic rule/content engine; settings for every user; no super admin for small changes | P03, P11, P13, P14, P19, P23 | — | COVERED 9 |
| R-048 | operations dashboard separate from super admin (delivery, after-sales, marketing, CS, social, PR, collaborations) | P18, P21 | — | COVERED 8; CHANGED-BY-DECISION 3 |
| R-049 | explore revenue/business model again | P16 | — | COVERED 2 |
| R-050 | own CRM integrated (ops, marketing, after-sales, CS, onboarding, grievances, tickets); open to Brevo migration/integration | P01, P03, P16, P18, P19, P21 | — | COVERED 8 |
| R-051 | performance appraisal; employee lifecycle; email IDs; decentralised decisions; anti-fraud maker-checker | P02, P18 | — | CHANGED-BY-DECISION 4; COVERED 5 |
| R-052 | leave, salary, payroll per Indian labour law; WFH; pan-India hiring; login/logoff; work measurement | P13, P18 | — | CHANGED-BY-DECISION 3; COVERED 7 |
| R-053 | M365 now (Teams, SharePoint), Google Workspace later; smooth migration for ops and clients; Office-openable files; self-explanatory folders | P03, P04, P18, P19, P20 | — | CHANGED-BY-DECISION 1; COVERED 8 |
| R-054 | switchable revenue streams (one-time, subscription, rental, PAYG, ads…) | P16, P17, P21 | — | COVERED 10; CHANGED-BY-DECISION 1 |
| R-055 | clients on M365 or Google Workspace; workflows for both | P04, P07, P18 | — | COVERED 1 |
| R-056 | business on autopilot (VSL-funnel style); marketing architecture (Brevo, Adobe Express, social calendar, employee reporting) | P21 | — | COVERED 5; CHANGED-BY-DECISION 3 |
| R-057 | patch/change management, GitHub branches, backups, VAPT, IS/internal/external audit | P00, P02, P23 | — | COVERED 9 |
| R-058 | cross-functional group roles; shared ops data across group companies | P02, P18, P19 | — | COVERED 5; CHANGED-BY-DECISION 2 |
| R-059 | client-company HRMS: KMPs, directors, duties, departments; finance-company departmental structure; Companies Act 2013 governance aligned with RBI MDs; task assignment | P02, P03, P11, P13 | — | COVERED 10; CHANGED-BY-DECISION 1 |
| R-060 | tool sufficient instead of legal team; one CLO | P06, P07, P09, P10, P13 | — | CHANGED-BY-DECISION 2; COVERED 1 |
| R-061 | individuals: DigiLocker-like; litigant self-help end to end | P04, P10, P11, P16 | — | CHANGED-BY-DECISION 1; COVERED 2 |
| R-062 | Jio services for customers and ops (research, automated calling, customer service) | P09, P10, P19 | — | COVERED 4; CHANGED-BY-DECISION 1; PARTIAL 1 |
| R-063 | savings page (money, hours, penalties) with quantification | P07, P14, P15, P17 | — | COVERED 6 |
| R-064 | RM as maker for retainer clients; client checker; multiple makers; both sides can create makers | P02, P13, P16, P18, P19 | — | COVERED 7; CHANGED-BY-DECISION 2 |
| R-065 | ops-hub client section: password tracker, billing/invoices feeding client billing, data sharing, messaging, common drive links | P18 | — | COVERED 9; CHANGED-BY-DECISION 3 |
| R-066 | super admin changes crucial client details; transparent fast workflow | P02, P18 | — | CHANGED-BY-DECISION 1; COVERED 2 |
| R-067 | audit trail | P00, P05, P08, P20 | — | COVERED 3 |
| R-068 | user download of documents and data | P04, P20, P22 | — | COVERED 2 |
| R-069 | taxation for individuals, companies, LLPs | P14 | — | COVERED 4 |
| R-070 | study lawdocs.in public pages; reuse; write missing copy | P00, P10, P21 | — | COVERED 6 |
| R-071 | frontend + backend + frontend content | P00 | — | COVERED 3 |
| R-072 | privacy policy, terms, other policies integrated | P03, P21 | — | COVERED 6 |
| R-073 | blog section from owner's categorised Word files | P21 | — | COVERED 2 |
| R-074 | vlog section with YouTube videos | P21 | — | COVERED 2 |
| R-075 | add services similar products offer | P16 | — | COVERED 1 |
| R-076 | Provakil-like multi-case management | P11 | — | COVERED 1 |
| R-077 | parties message while signing; track-changes review; eSign; records/audit | P07, P08 | — | COVERED 7 |
| R-078 | eStamp API: buy online or attach stamp paper, then eSign | P08 | — | CHANGED-BY-DECISION 2; COVERED 2 |
| R-079 | court pleadings drafting | P10 | — | COVERED 2 |
| R-080 | legal advisory retainer + one-time business model | P14, P16 | — | COVERED 3 |
| R-081 | FinLegal Academy integration | P16 | — | COVERED 3 |
| R-082 | startup section (registration, advisory, legal officer, TM, funding docs) | P12, P14, P21 | — | COVERED 6 |
| R-083 | loan/lending/insurance grievance help (FREED/ClaimBuddy/Insurance Samadhan); separate entities; status tracking | P00, P11, P14, P15, P18, P22 | — | COVERED 13; CHANGED-BY-DECISION 1 |
| R-084 | challans check/pay/contest; hire advocate (ChallanPay-type) | P15 | — | CHANGED-BY-DECISION 2; COVERED 3 |
| R-085 | vehicle sale agreements; vehicle loans/challans | P15 | — | COVERED 4; CHANGED-BY-DECISION 1 |
| R-086 | reverse-engineer LegalKart, OnlineLegal, Vakilsearch | P09, P14, P16, P21 | — | COVERED 4 |
| R-087 | per-page "Draft with AI free" + "Hire a professional" blocks | P06, P21 | — | COVERED 2; CHANGED-BY-DECISION 1 |
| R-088 | testimonials without photos | P21 | — | COVERED 2 |
| R-089 | team uploads blogs without developers | P21 | — | COVERED 1 |
| R-090 | improve Word-file content; one-liners; FAQs for search | P14, P21 | — | COVERED 4; CHANGED-BY-DECISION 1 |
| R-091 | consider the ChatGPT prompt | P00, P23 | Z | COVERED 1; CHANGED-BY-DECISION 1 |
| R-092 | ask questions in plan mode (done 25 Oct 2026) | P00, P23 | — | COVERED 1; CHANGED-BY-DECISION 1; PARTIAL 1 |

---

## 9. Review log (v1.0)

| Date | Step | Result |
|---|---|---|
| 25 Oct 2026 | Plan mode: four rounds of owner questions | D-01…D-13 |
| 25 Oct 2026 | Research streams R1–R6 (live web, first-party first) | ~71k words; LG register, IMP backlog, page inventory, pricing and data sources |
| 25 Oct 2026 | Authoring: 24 phases, 26 appendices, content deck | ~600k words |
| 25 Oct 2026 | Integration review: cross-file resolutions X-01…X-30; ID/error collisions fixed (Appendix B §B.7); state machines reconciled (Appendix A, 21 notes); 515 screens catalogued; 582 phase scenarios; NN coverage complete | `_review/` logs |
| 25 Oct 2026 | Traceability: 581 rows; 3 FRs added (FR-P15-70, FR-P19-84, FR-P23-58) | Appendix Z |
| 25 Oct 2026 | Second error review (owner instruction "review, look for the errors and fix them"): G1 legal (P01, P04, P05, P08, P10–P12; 37 fixes), G2 legal/commercial (P13–P18; 29), G3 architecture/logic (P00, P02, P03, P06, P07, P09, P19–P23; 91), G4 registries (A, B, C, D, K, R, V, W, Z; 24); lead fixes to master, 02, README, G, K, L, R, W, X and content (trade-mark reply period restored to "one month" per r.33(4); `WORKSPACE_PORT` unified; master §6.2 aligned to Appendix A; P09 L0–L2 slice added to Wave 2; conventions file committed to `docs/reference/`) | `_review/G1…G4_log.md`, `_review/LEAD_second_review_log.md` |


---

# PART C — PHASE OBJECTIVES AND SCOPE

## Phase P00 — Foundations, Repository Discovery and Migration

**File:** `phases/P00_Foundations_Repository_Discovery_and_Migration.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** none (first phase). Read-only access to the legacy lawdocs.in repository, a point-in-time restore of the MongoDB Atlas database, the Railway project (viewer), the DNS zone, the PayU merchant dashboard (read-only), the Anthropic console (usage and key list), Google Search Console and the live site. Companion documents committed unchanged under `docs/ecosystem/` with SHA-256 checks: Infrabyx Ecosystem Integration Specification v1.1, Operations Hub Master Prompt v1.0, LawDocsComply Pack v1.2 (reference only), Equator v3.1 (reference only).
> **Sequencing:** Sprint 1 discovery and repository scaffold run in parallel; sprints 2–4 build the platform core; sprint 4 starts P01 (identity) and P21 core (SSR site shell) in parallel; sprints 5–6 run migration rehearsals and the SEO cut-over. **Freeze points:** (1) the disposition register is signed off by the owner before any legacy asset is retired; (2) the `core` schema, ID prefixes, audit-event structure and export-map contract freeze at the end of sprint 4 (later phases extend, never change); (3) the 301 map freezes 10 days before DNS cut-over (T−10 d, §5.5; `web.redirects.freeze_days_before_cutover`). The legacy site stays live and read-write until cut-over (§5.5). **Customer cut-over dependency:** T0 (§5.5) needs P01's OTP sign-in, P04's vault list view and P17's order/billing mirror view running in pre-prod; if they are not ready by sprint 6, P00 exits with R1–R3 passed and every other gate item met, and the final customer migration run, DNS cut-over, decommissioning (FR-P00-83) and @P00-AT-15/16 move to a dated P00 tail that must close before the Wave 1 P23 go-live gate.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles and access — coarse platform roles only in P00), K (export package `LD-EXPORT-1.0`; export-map registry created here), P (security, privacy and certification readiness), R (settings registry; heads created here), W (verification log and open items), Y (Ecosystem Spec v1.2 change request: owner code `LD`).
> **Requirements covered:** R-001, R-002, R-003, R-021 (storage foundations), R-022, R-031 (foundations), R-032 (rendering and host hygiene), R-033 (foundations), R-057 (CI/CD skeleton; detail in P23), R-067, R-068 (foundations), R-070, R-071.
> **Decisions applied:** D-01, D-02, D-08, D-09, D-10, D-14 (AI gateway stub only), D-16 · **Challenges applied:** CH-15, CH-16, CH-19 (claims hygiene of the legacy site), CH-20 · **Non-negotiables tested:** NN-01, NN-02, NN-04, NN-09, NN-11, NN-12, NN-15, NN-19, NN-20, NN-24, NN-25, NN-27, NN-29, NN-31, NN-32, NN-38, NN-39, NN-45, NN-46, NN-47
> **Estimated effort:** 6 two-week sprints, squad of 8 (tech lead, 2 backend engineers, 1 frontend engineer, 1 platform/DevOps engineer, 1 data-migration engineer, 1 QA/security engineer, 1 web/SEO engineer) plus the owner as product owner and a part-time content reviewer for blog migration.

### Objective and business outcome

lawdocs.in runs today as a client-side React single-page application built with Vite, an Express backend that includes a chatbot route calling the Anthropic API, MongoDB Atlas as the database, Railway as the host and an earlier PayU payment integration [VERIFY all five facts at discovery; they come from the owner, not from code inspection]. Research shows the public site is invisible to non-JavaScript crawlers (every URL returns the same title and an empty body), its sitemap lists 186 non-www URLs while only the www host serves deep pages, and `robots.txt` blocks `/buy/` while the sitemap lists 20 `/buy/*` URLs (R5 §1.1–§1.2). The stack cannot carry what the owner now wants: tenant isolation, an append-only audit ledger, India residency, immutable signed originals, portability in `LD-EXPORT-1.0`, ecosystem contracts and certification readiness.

P00 does four things:

1. **Discover and keep what works.** Inventory every route, collection, user, order, blog post, integration, secret, DNS record and SEO asset; give each a disposition; carry forward everything useful (content, users, order history, search equity).
2. **Build the platform core** on the locked stack (D-01): pnpm/Turborepo monorepo, NestJS 11 modular monolith, Next.js 16 apps, PostgreSQL with enforced RLS, the hash-chained audit ledger with Correction Entries, prefixed-ULID IDs and business reference IDs, transactional outbox, settings and flag heads, the evidence store with Object Lock, observability, the CI/CD skeleton, the NN test harness and synthetic data.
3. **Migrate** users, content and orders from MongoDB to PostgreSQL through rehearsed, reconciled, idempotent runs, so no customer re-keys anything and no order or invoice record is lost.
4. **Cut over without losing search traffic**: SSR shell from P21 core, one canonical host (`https://www.lawdocs.in`), a complete 301 map for all 186 sitemap URLs and the legacy indexed URLs, a corrected `robots.txt` and sitemap, then decommission Railway, MongoDB Atlas and PayU in a controlled order.

| Outcome | Exit-gate measure |
|---|---|
| Nothing useful is lost | `docs/discovery/10-disposition-register.md` signed by the owner; every asset has a disposition (MIGRATE, REBUILD, RETIRE, ARCHIVE); zero rows "unknown" |
| Platform core runs | `docker compose up && pnpm dev` starts all apps on a fresh machine in ≤ 10 minutes; `dev`, `test`, `staging` and `pre-prod` deploy from `main` through CI with signed images (environment names per P23 FR-P23-07) |
| Isolation is provable | `NN-01_cross_tenant_denied` passes for 100% of tenant tables across two seeded tenants for SELECT, UPDATE and DELETE; RLS lint passes |
| History is tamper-evident | `NN-02_*` suite passes: every mutating handler writes a chained ledger event in the same transaction (`NN-45_*`); `UPDATE`/`DELETE` on the ledger fails for every role including the owner role |
| Migration is exact | Final rehearsal reconciles 100% on counts and order-amount sums by month and status; field-level defect rate ≤ 0.5% on a 5% stratified sample (minimum 200 rows per entity); all defects resolved or carried as flagged rows with owner sign-off |
| Search equity preserved | 100% of the 186 sitemap URLs and every legacy URL with impressions in the last 16 months return a single-hop 301 (or a deliberate 410) to an SSR page returning 200 with a unique title, H1 and body to a no-JavaScript fetch; zero redirect chains; Search Console shows no rise in 404s above baseline + 5% in the 28 days after cut-over |
| India residency | IaC denies regions other than ap-south-1/ap-south-2 except listed global services; no tenant data outside India after cut-over (`NN-25_*`); Railway, MongoDB Atlas and the legacy chatbot key are decommissioned on the dated plan |
| Portability contract exists | `xpt.export_map` registry and its CI contract test exist; a migration that adds a tenant table without an export-map entry fails CI (`NN-11_*`) |

**What "done" looks like for users.** A returning customer signs in to the new my.lawdocs.in with their mobile or email (P01), finds their past orders and invoices under Billing, and finds the documents they bought in their Legal Vault. A visitor arriving from an old Google result for `lawdocs.in/smartdrafts/...` lands on the right new document page in one hop. Nobody sees a "page not found".

---

### Scope (in / out)

**In scope**

- Discovery of the legacy repository, database, hosting, DNS, payments, AI usage, analytics and third-party accounts; security triage of the live system; disposition register.
- Monorepo scaffold (all six apps of master §1.3 plus `apps/worker`), toolchain, module skeletons for every bounded context in master §5.3, boundary enforcement and code ownership.
- Environments (`local`, `dev`, `test`, `staging`, `pre-prod`, `prod`, `dr`, plus the `mig` migration zone inside the prod account; names per P23 FR-P23-07, which governs), hosting topology, domains and infrastructure as code.
- CI/CD skeleton with branch model, signed artefacts, SBOM and the NN suite as a required check (P23 hardens and completes it).
- `packages/tenancy`, `packages/audit`, `packages/ids` (prefixed ULID + business reference IDs), `packages/money`, `packages/crypto`, `packages/db`, `packages/config` (registry heads), `packages/contracts` (generated from `infrabyx-contracts`), `packages/observability`, `packages/testing`.
- `core` schema: tenants, legal entities, brands and operating-entity profiles (D-06, D-08), tenant domains, data-class catalogue, sequences, idempotency keys, outbox and inbox, audit ledger, anchors, correction entries, access log, break-glass events, migration lineage.
- Object storage (quarantine, documents, originals with Object Lock, exports, backups) and the ingest pipeline skeleton (P04 builds the Legal Vault on it).
- Observability, error model, SLO budgets; design-token, i18n and accessibility foundations.
- NN test harness (`tests/nn/`), synthetic seed profiles.
- Data migration framework and the full MongoDB → PostgreSQL migration (users, orders, payments, blog content, leads, chatbot logs disposition, any uploaded files).
- SEO-safe cut-over with the 301 map, host canonicalisation, robots and sitemap correction (with P21 core supplying the SSR pages).
- Decommissioning of Railway, MongoDB Atlas, the legacy Anthropic key and the PayU integration.
- ADR set and the `docs/` structure.

**Out of scope (owned later)**

| Item | Owner phase |
|---|---|
| Login, onboarding, KYC/KYB, consent capture UI | P01 (P00 creates the `iam`/`kyc` schemas' parent tables only where `core` needs them, and a stub IdP for local development) |
| Organisation structure, user types, maker-checker engine | P02 |
| Settings Studio UI, rule engine | P03 (P00 creates the heads of `cfg.setting_definitions`, `cfg.setting_values`, `cfg.flags` and `cfg.kill_switches`; P03 owns them) |
| Legal Vault and DMS features | P04 (P00 creates buckets and ingest skeleton) |
| Public website pages, CMS, content rewrite | P21 (P00 owns the redirect map, host rules, robots/sitemap generator contract and the cut-over runbook; P21 core supplies the SSR shell and the top pages that receive redirects) |
| Billing engine, invoices, refunds | Operations Hub OH8 via `BILLING_PORT`; LawDocs mirror in P17 |
| Full CI/CD hardening, CAB, VAPT, go-live | P23 |
| Mobile apps | P22 (P00 scaffolds `apps/mobile` with Expo and the design tokens only) |
| Ecosystem connectors | P19 (P00 imports the contracts package and stubs the `ECOSYSTEM_PORT`) |

---

## Phase P01 — Identity, Onboarding, KYC/KYB and Consent

**File:** `phases/P01_Identity_Onboarding_KYC_KYB_and_Consent.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (core schema, tenancy, ledger, settings heads, flags, ingest, provider routing). External: Keycloak; a DLT-registered SMS route (JioCX or another CPaaS) and optional WhatsApp authentication templates; Google and Microsoft OIDC apps; DigiLocker Requester onboarding with NeGD; UIDAI Aadhaar secure-QR verification (Phase 1, no registration) and OVSE registration under Reg 13A (Phase 2); one licensed KYB vendor (MCA data), one GSP (GSTIN search), GLEIF (LEI); Operations Hub OH3 (consented leads), OH4 (provisioning), OH9 (professional directory).
> **Sequencing:** Starts in P00 sprint 4. Sprints 1–3: identity architecture, login methods, sessions, consent ledger, individual fast path. Sprints 4–6: verification ladder, DigiLocker, Aadhaar offline (QR), KYB, signatory authority, company wizard. Sprints 7–8: professionals, guests, guardians, nominees, partner onboarding API, accessibility pass. P02 starts in parallel from sprint 2 (it needs persons, users and memberships, which freeze at the end of sprint 2). Wave-2 migration activation (P00 users) runs at the P01 exit.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles, grant types, assurance requirements), K (export folders for profile, KYC and consent records), P (security and privacy controls; DPDP programme), R (settings), W (verification log and open items), Y (ecosystem change request: LawDocs as onboarding target and `TenantProvisioned` consumer).
> **Requirements covered:** R-002, R-003, R-005, R-009, R-017 (identity for web and mobile), R-023 (consented sharing foundations), R-025 (accessible authentication), R-028, R-030, R-031, R-061 (individual identity), R-064 (maker accounts), R-072 (notices and policies in-product).
> **Decisions applied:** D-01, D-02, D-06, D-08, D-10, D-12 (KYC via provider-neutral adapters) · **Challenges applied:** CH-01, CH-02, CH-03, CH-04, CH-05, CH-06, CH-08, CH-09, CH-15, CH-16, CH-17, CH-18, CH-30 · **Non-negotiables tested:** NN-03, NN-04, NN-05, NN-06, NN-11, NN-13, NN-19, NN-20, NN-21, NN-23, NN-24, NN-26, NN-28, NN-32, NN-34, NN-38, NN-42, NN-44, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (tech lead, 2 backend engineers, 2 frontend engineers (web + responsive/mobile flows), 1 identity and security engineer, 1 integrations engineer for KYC/KYB vendors, 1 QA and accessibility engineer).

### Objective and business outcome

The owner asked for "Aadhaar login", automatic fetching of details from Aadhaar, PAN, CKYC, MCA and CIBIL APIs, and very fast onboarding for individuals and companies. Research shows that LawDocs is not, and does not plan to become, an Aadhaar requesting entity (Aadhaar Act s.4(4); s.57 omitted by the 2019 Amendment Act; the good-governance route under LG-027 is a long path, never a dependency; R3 LG-021–025), cannot search or download CKYC (PML Rules r.9; R3 LG-046), is unlikely to qualify for direct PAN verification (R3 LG-047), cannot pull credit-bureau data (CICRA ss.17(4), 22; R3 LG-057–058) and has no open MCA API (R3 LG-050). P01 delivers the lawful version of the same experience, and makes it faster than the owner's design:

- **Sign-in in one step** with mobile OTP, email OTP, passkey, password + MFA, Google or Microsoft sign-in, or enterprise SSO. No Aadhaar login (NN-03, CH-01).
- **Verification only when needed**, on a four-level ladder (L0 → L3), using DigiLocker issued documents, Aadhaar secure-QR / e-Aadhaar verification and later Aadhaar Verifiable Credentials as a registered OVSE, licensed KYB vendors, GSPs, GLEIF and Entity Locker — never storing an Aadhaar number (NN-04).
- **Companies discovered from one identifier** (CIN, LLPIN, GSTIN, PAN of the entity, LEI or Udyam) with provenance per field, then the authorised signatory verified with authority evidence.
- **Professionals onboarded with real credential checks**, advocates showing only BCI Rule 36 fields (NN-21).
- **Counterparties sign without an account**, guardians manage wards, nominees get time-locked access after verified events.
- **Consent per DPDP purpose** with versioned notices, one-tap withdrawal and a privacy centre.
- **Partners and sister products** start onboarding on the customer's behalf — group products through the Operations Hub (`TenantProvisioned`), third-party partners through the P19 partner API — but every workspace starts as an invitation; nothing activates until the customer confirms, and the requester gets no access.

| Outcome | Measure (exit gate; p75 in moderated usability tests with 10 participants per journey, then production analytics) |
|---|---|
| Individual: first draft fast | Landing on a document page → first draft preview ≤ **2 minutes** for documents with ≤ 10 required questions; account creation adds ≤ 3 taps + one OTP |
| Company: set-up fast | Sign-up → company workspace with discovered profile, departments and approval model → first agreement started ≤ **10 minutes** |
| No Aadhaar login exists | `NN-03_no_aadhaar_login`: no route, IdP, Keycloak authenticator or UI string offers Aadhaar as a login method |
| No Aadhaar number stored | `NN-04_*` suite: zero Aadhaar-number columns; QR payloads discarded after verification; logs clean |
| Discovery quality | Companies with a CIN: ≥ 85% of profile fields pre-filled with provenance; discovery p50 ≤ 20 s, p95 ≤ 40 s |
| Consent integrity | 100% of optional processing has a consent artefact referencing a notice version; withdrawal propagates internally ≤ 1 hour and to the Operations Hub ≤ 1 hour (Ecosystem Spec §6.14 [REC]) |
| Accessible authentication | WCAG 2.2 AA incl. SC 3.3.8; no image CAPTCHA; every verification path has a non-visual, non-liveness alternative (R3 LG-136 [VERIFY]) |

---

### Scope (in / out)

**In scope:** Keycloak realms, clients and themes; BFF session handling; all login methods; MFA, passkeys, recovery; sessions and devices; step-up; the identity verification ladder and its providers; KYB for companies, LLPs, partnership firms, proprietorships, trusts, societies and HUFs; authorised-signatory verification and authority evidence; professional onboarding and credential verification; counterparty guest identity; minors, wards and guardians; nominees and legacy access; consent artefacts, notice versions, withdrawal and the privacy centre; the activation flow for partner invitations (API surface in P19 §4K) and Operations Hub provisioning consumption; the individual fast path and the company set-up wizard; Consumer Help brand identity separation; migration activation of P00 users.

**Out of scope**

| Item | Owner phase |
|---|---|
| Organisation structure, user types, roles builder, maker-checker engine, delivery grants | P02 |
| Settings Studio UI | P03 |
| eSign signer authentication (performed by the ESP), signing ceremony, signer consent screen | P08 (P01 supplies the signer's account/guest identity and verification level) |
| Drafting questionnaire engine and Vidhi drafting | P06 / P09 (P01 supplies the anonymous-draft session and save-to-account step) |
| Marketplace professional registry, listing switches, payouts | P16 (P01 captures and verifies credentials) |
| Billing, plan purchase | P17 / OH8 |
| Credential vault for portal passwords | P18 (`cvl`, NN-16) |
| DigiLocker document pull into the vault beyond identity verification | P04 |

---

## Phase P02 — Tenancy, Organisation Structure, User Types and Maker-Checker

**File:** `phases/P02_Tenancy_Org_Structure_User_Types_and_Maker_Checker.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenants, legal entities, ledger, settings heads, flags), P01 (persons, users, memberships, invitations, verification levels, signatory authorities). External: Cerbos; Operations Hub OH10 (staff SCIM and `group_grant` memberships), OH4 (onboarding milestones); `@infrabyx/governance-kernel` for director/KMP designations when mounted (P13) or LawDocsComply when it is system of record (D-10).
> **Sequencing:** Starts in P01 sprint 2 (persons/users/memberships frozen). Sprints 1–2: org model, workspace types, context switcher, role grants, Cerbos policy framework. Sprints 3–4: maker-checker engine, DoA tables, SoD engine, delegation and out-of-office. Sprints 5–6: custom roles, group and cross-functional grants, delivery-grant interface, access reviews, role-based homes and navigation. P03 (Configuration Studio) consumes the maker-checker and DoA schemas from sprint 4; P18 builds the Delivery Console UI on the grant model frozen at the end of sprint 5.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles, permission matrix, maker-checker action catalogue, SoD pairs, Cerbos conventions, grant types), P (access-control and privileged-access controls), R (settings), K (export folders for organisation and access records), W (open items), X (Operations Hub additions: group-grant feed and access-review event).
> **Requirements covered:** R-026, R-027, R-028, R-030, R-047 (configurable approvals; item types in P03), R-048 (separation of operations from super admin), R-051 (maker-checker, anti-fraud), R-058, R-059 (organisation structure foundations), R-060 (one-CLO operating model), R-064, R-065 (client section access model), R-066, R-067.
> **Decisions applied:** D-02, D-03, D-06, D-10, D-17 · **Challenges applied:** CH-14, CH-16, CH-24, CH-26, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-11, NN-13, NN-17, NN-18, NN-19, NN-23, NN-28, NN-29, NN-33, NN-43, NN-45, NN-47
> **Estimated effort:** 6 two-week sprints, squad of 8 (tech lead, 3 backend engineers, 2 frontend engineers, 1 security/authorisation engineer, 1 QA engineer).

### Objective and business outcome

The owner wants many user types — super admin, an operations team serving clients, company admins, makers and checkers, departmental users, individuals — each with its own features, fewer clicks and an anti-fraud design where "employees cannot cheat". P02 gives LawDocs one authorisation model that serves every workspace type, without special-case code:

- **Structure:** tenant → legal entities → branches → departments → teams → positions, renameable and effective-dated, for a one-person startup and for a listed group with forty subsidiaries.
- **Workspaces:** Personal, Company, Professional firm and the Consumer Help brand, with a context switcher that always shows *where* and *as whom* the user is acting.
- **Roles:** the binding role codes (master §1.4; Appendix D), scoped grants, a custom-role builder and positions, so that a company can model "Head – Legal (Delhi)" without asking LawDocs.
- **Approvals:** a configurable maker-checker engine per action type and a delegation-of-authority (DoA) matrix by value, document type and department, with segregation of duties enforced at person level.
- **Controlled outsiders:** LawDocs relationship managers as delegated makers, engaged professionals, external counsel, auditors, counterparties, family members, delegates and nominees — each through a scoped, time-bound grant the customer controls; Infrabyx cross-functional staff through purpose-bound group grants that are never inherited (Ecosystem Spec §4.6).
- **Integrity without surveillance:** maker ≠ checker, approvals bound to the exact version approved, quarterly access reviews and immutable logs — not keystroke or screen monitoring (NN-33; CH-24, CH-32).

| Outcome | Exit-gate measure |
|---|---|
| One model, every workspace | All persona journeys in §4L pass with the same policy engine; no `if (tenant.kind === …)` authorisation branches in handlers (Semgrep rule) |
| Maker ≠ checker everywhere | `NN-18_*` suite: for every action in the Appendix D catalogue with mode REQUIRED/LOCKED, the maker (and the maker's delegator, linked staff identity or agent sponsor) cannot approve |
| Approvals bind to content | Changing a payload after approval invalidates the approval (`LD-WF-012`) in 100% of catalogue actions |
| Outsiders are scoped | `NN-17_*`: delivery and engagement grants require client approval, expire, revoke within 60 s; break-glass needs two approvers and a client report ≤ 24 h |
| Group roles never inherited | `NN-17_group_grant_not_inherited`: membership in a parent tenant or another Infrabyx company never yields access to a child tenant without an explicit grant |
| Fewer clicks | Role-based home screens meet the click budgets of §4L in moderated tests |
| Customisation without LawDocs | A company owner creates a custom role, a new department and a DoA rule, and enables maker-checker on external sharing, without any LawDocs staff action (NN-29) |

---

### Scope (in / out)

**In scope:** organisation model (`org`); workspace types and the context switcher; role grants, scopes and positions; custom roles; the Cerbos policy framework, derived roles and query plans; the maker-checker engine (`wf.approvals`) and action catalogue wiring; DoA decision tables (schema, defaults, evaluator call through `RULES_PORT`, simulator); SoD engine; delegation and out-of-office; individual sharing roles (family, delegate) and their scopes; professional-firm roles; group tenants and cross-entity grants; Infrabyx `group_grant` enforcement; grant types for delivery, engagement, onboarding, external counsel, auditor, nominee and break-glass (model, lifecycle, enforcement); access reviews; master-data change of a client by LawDocs staff (CH-26); role-based home dashboards and navigation.

**Out of scope**

| Item | Owner phase |
|---|---|
| Configuration Studio UI, rule-pack authoring, open/interim/waiting item types | P03 (P02 provides the approval and DoA schemas it edits) |
| Delivery Console screens, client sections, RM workbench, access-transparency log UI | P18 (P02 provides the grant model, enforcement and APIs) |
| Board, committees, KMP registers, client HRMS | P13 (governance and HRMS kernels; LDC when SoR) |
| Agent workforce, autonomy ceilings, sponsors | P09 (P02 enforces "agents are makers only") |
| Seat counting and plan limits | P17 (P02 exposes counts by role class) |

---

## Phase P03 — Configuration Studio, Rule Engine and Settings

**File:** `phases/P03_Configuration_Studio_Rule_Engine_and_Settings.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, `packages/config` skeleton, hash-chained audit ledger, `core.correction_entries`, transactional outbox, Temporal, Cerbos, OpenTelemetry), P01 (identity, step-up authentication, consent artefacts), P02 (tenants, legal entities, departments, positions, user types, delegations and the maker-checker engine in `wf`). External: none at runtime (GoRules ZEN and CEL are embedded libraries).
> **Sequencing:** Sprint 1 freezes four contracts that every later phase consumes: the settings SDK (`packages/config`: registry, resolver, codegen, CI lint), the tier tree and control classes, `RULES_PORT` (`packages/rules`) and the open/interim/waiting **items API** (`packages/workflow` → `wf.items`). P04, P06, P07, P08, P17 and P19 start consuming in sprint 2. Studio screens follow in sprints 2–5; rule authoring and golden-case tooling in sprints 3–5; configuration templates, sandbox and export/import in sprint 6. No phase may read a setting, evaluate a legal rule or create a waiting item through any other path after sprint 1 (NN-29).
> **Binding appendices:** A (workflows and state machines — A.13–A.17), B (data model, events and error codes), R (configuration framework and settings catalogue — binding for every key, tier and default), D (roles and access matrix), F (instrument eligibility gate — rows run in this engine), H (agent roster — autonomy keys), K (export package — configuration and items folders), W (open items), Y (Ecosystem Spec v1.2 change request). Precedence on conflict: master §18 (master → `02` → G → F → B → A → D → R → C → this phase), except that this phase wins on the defaults of the keys it owns (X-11).
> **Requirements covered:** R-027, R-030, R-047, R-026, R-028, R-019, R-025 (accessible theming), R-008 (labels per language), R-064 (RM proposes configuration), R-066 (super-admin changes through a transparent workflow), R-067, R-054 (revenue-stream switches use the registry; values in P17), R-053/R-055 (suite-neutral templates).
> **Decisions applied:** D-01, D-02, D-06, D-07, D-10, D-12, D-13, D-15 · **Challenges applied:** CH-12, CH-21, CH-24, CH-26, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-07, NN-13, NN-18, NN-28, NN-29, NN-30, NN-34, NN-38, NN-39, NN-40, NN-43, NN-45
> **Estimated effort:** 6 two-week sprints, squad of 8 (configuration core 2 backend; rule engine 2 backend; items engine 1 backend; Studio UX 2 frontend; QA/accessibility 1).

### Objective and business outcome

LawDocs serves an individual signing a rent agreement, a five-person startup, a 2,000-employee NBFC with a legal department, a practising advocate and a consumer-help case manager. Each wants different words, screens, reminders, approvals and defaults. Indian law also changes often: a State revises stamp duty, the IT Act First Schedule is amended, the RBI replaces its Ombudsman Scheme. The owner's brief asks for "very complete settings", a "dynamic rule and content engine, not static", customisable "open, interim and waiting-for-someone-else items", and "super admin not needed for small changes" (R-047).

P03 delivers one governed configuration system:

- a **settings registry** where every configurable value is declared once, with a tier, a control class, bounds, an owner and an "i" help key;
- a **Configuration Studio** with three faces — Super Admin console, tenant administration (company admin, department head, professional firm admin) and personal settings (every user) — so that each user type changes what it may change, immediately and with audit;
- a **rule engine** (GoRules ZEN decision tables + CEL predicates behind `RULES_PORT`) that runs legal rules, jurisdiction variants, instrument-eligibility rows, reminders and SLA policies as versioned, sourced, effective-dated data with a reviewer of record (NN-30);
- an **open / interim / waiting items engine** used by every module, with configurable item types, statuses, owners, SLA clocks and chasers, and locked legal clocks that never pause;
- **feature flags and kill switches** for every agent, revenue stream, vendor adapter, consumer vertical and outbound channel (NN-39).

| Outcome | Exit-gate measure |
|---|---|
| Small changes without LawDocs staff (R-047) | A new company admin, unaided, in ≤ 20 minutes: renames two departments, adds three custom fields to agreements, relabels two agreement statuses, sets a numbering scheme, uploads a letterhead, changes the reminder cadence for renewals, pins three menu items and two quick actions, and sets quiet hours — all audited and undoable; zero LawDocs actions |
| Individuals customise in ≤ 2 taps | From home: theme, text size, language, home widgets and reminder timing each reachable in ≤ 2 taps on mobile and ≤ 2 clicks on web |
| Legal values governed | 100% of GOVERNED changes pass maker ≠ checker, preview, citation and effective date; 0 LOCKED values changeable through any UI or API (`NN-29_*`, `NN-18_*` tests) |
| Law changes as data | A changed State stamp-duty row, a new First Schedule entry or a revised Ombudsman timeline is drafted, golden-tested, reviewed by `PLT_LEGAL_REVIEWER`, scheduled and activated with no deployment; documents already in flight keep their pinned rule version |
| Waiting items work everywhere | The items API is frozen in sprint 1 and proven by a reference adopter and contract tests at P03 exit; each adopting phase (P04, P07, P08 in Wave 1; P11, P15, P16, P18 later) must pass `items-adoption` at its own exit gate; the "Waiting on others" widget shows every item with party, age, next chase and the legal clock that keeps running |
| Safe switches | Every kill switch registered in Appendix R propagates in ≤ 60 seconds and is drilled at least quarterly |

---

### Scope (in / out)

**In scope**

- `cfg` module: setting definitions, values, change requests, scheduled activations, change batches and undo, tier tree, control classes, merge strategies, Studio APIs, configuration templates, sandbox, export/import, Configuration Health.
- UI/UX customisation: themes over LD design tokens with contrast validation, density, font scale, home widgets, menu pinning and reordering, quick actions, landing pages, terminology and field labels, custom fields, custom status sets, reason codes, numbering schemes, form layouts, notification templates (rendered by `ntf`), document branding and letterheads (rendered by `packages/docgen`).
- `rul` module: `RULES_PORT`, ZEN and CEL runtimes, rule-set registry, jurisdiction packs, golden cases, preview and impact analysis, lifecycle with reviewer of record, verification status, fallback; the shared **content-version framework** used by `tpl`, `hlp` and `dms` retention schedules.
- `wf.items`: item types, canonical states, waiting parties, clocks, chase policies, escalation ladders, item widgets and APIs.
- Feature flags and kill switches (`cfg.flags`, `cfg.kill_switches`) — the **single platform registry** (R-A-09): P00 creates the heads, P09 and P19 read and engage switches through it and emit/consume only `in.lawdocs.cfg.KillSwitchEngaged.v1` / `in.lawdocs.cfg.KillSwitchReleased.v1`.
- Tasks (`wf.tasks`, `tsk_`; R-A-08): the one task table used by P11, P13, P18 and Appendix I.
- Super-admin configuration overrides through Correction Entries with client approval (CH-26).

**Out of scope (owner phase)**

- Maker-checker engine, approval chains, delegations, department and position masters — P02 (P03 configures them; P02 executes them).
- Template, clause and questionnaire **content** — P06; glossary and help content — P21; P03 supplies the versioning framework they use.
- Instrument-eligibility **rows** (content of Appendix F) — P08 owns the content; P03 runs it.
- Plan prices and revenue-stream values — P17 (uses the GOVERNED-elevated pipeline from P03).
- Notification delivery, DLT registration and channel adapters — `ntf` in P00/P19; P03 owns templates and channel policy only.
- Export of configuration in `LD-EXPORT-1.0` — P20 builds the package; P03 registers the export-map entries (§13).

---

## Phase P04 — Legal Vault and Document Management System

**File:** `phases/P04_Legal_Vault_and_Document_Management_System.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (repository, S3 SSE-KMS with versioning and Object Lock, audit ledger, outbox, OpenSearch, pgvector, Temporal, `packages/dix` skeleton), P01 (accounts, OTP/passkey sessions, step-up MFA, `CP_GUEST` magic-link identities, DigiLocker requester integration in `kyc`, consent artefacts `cns_`), P02 (tenants, legal entities, departments, user types, maker-checker, delivery grants), P03 (settings registry, rule engine `RULES_PORT`, metadata-schema and retention content packs). External: DigiLocker Requester API (NeGD), malware engines, Microsoft Graph and Google Drive APIs (optional), JioCX WhatsApp BSP (optional, flagged).
> **Sequencing:** Wave 1. Sprints 1–3 build the storage core (§4A–§4E, §4M, §4N) because P06, P07 and P08 write into it; sprints 4–6 build search, sharing, intake and reminders (§4F–§4K); sprints 7–9 build family vault, nominee access, Office co-editing, mobile offline and health checks (§4L, §4O–§4R). P04 ships the **`packages/dix` baseline** (malware scan, true-type sniffing, deterministic print OCR for search, Aadhaar detection and masking) so that NN-04 holds from the first upload; P05 (Wave 2) adds handwriting, type copies, translation and extraction on the same pipeline. P20 core (Wave 1) owns the import engine and `LD-EXPORT-1.0` packaging; P04 owns the vault-side mapping UX. **Freeze point:** the canonical document model (§4A) and the folder-view rule pack format freeze at end of sprint 3; later changes follow expand → migrate → contract (NN-12).
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (personas and permission matrix), F (instrument eligibility — read by health checks), K (`LD-EXPORT-1.0` folder taxonomy — vault folder views mirror it), R (settings registry), W (open items), Y (Ecosystem Spec v1.2 change request — LD as producer of `documents` events).
> **Requirements covered:** R-011, R-021, R-022, R-023, R-024, R-043, R-053, R-055, R-061, R-067, R-068; contributes to R-005 (DigiLocker pull), R-017 (mobile), R-025 (accessibility), R-027, R-030, R-044 (inputs for type copy).
> **Decisions applied:** D-01, D-07, D-10, D-12 (DigiLocker via `kyc`) · **Challenges applied:** CH-02, CH-15, CH-16, CH-28, CH-29 · **Non-negotiables tested:** NN-01, NN-02, NN-04, NN-09, NN-11, NN-12, NN-13, NN-15, NN-17, NN-18, NN-24, NN-25, NN-26, NN-28, NN-29, NN-30, NN-32, NN-38, NN-40 (health-check input), NN-42, NN-44, NN-45, NN-46
> **Estimated effort:** 9 two-week sprints, squad of 8 (backend 3, web 2, mobile 1, search/data 1, QA/accessibility 1), plus a part-time content analyst for metadata schemas and retention packs.

### Objective and business outcome

LawDocs must be the app a person or a company **keeps** — the place where every agreement, ID, policy, notice, order and receipt lives, can be found in seconds, is shared exactly as far as the owner chooses, and survives code releases, vendor changes and the owner's own exit. P04 builds the **Legal Vault** (individuals and families) and the **Document Management System** (companies) as one `dms` bounded context with two experiences.

The vault is not a "DigiLocker" under the IT (Preservation and Retention of Information by Intermediaries Providing Digital Locker Facilities) Rules 2016 — LawDocs is not a licensed Digital Locker Service Provider. Product copy says **"Legal Vault"**, never "DigiLocker"; DigiLocker is a source the vault pulls from with consent (R3 LG-036–038; CH-15) **[LAW]**.

| Outcome | Exit-gate measure |
|---|---|
| Keep everything, lose nothing | Every original is stored once with SHA-256 at ingest and S3 Object Lock; zero originals overwritten in the release test suite (NN-09) |
| Find anything fast | Permission-trimmed search ≤ 1.5 s p95 on 1 million documents per tenant, ≤ 800 ms p95 on 10,000 documents per individual, including OCR text and Indic queries |
| Share exactly what you mean | A share pack containing one version, pages 3–7, redacted, view-only, watermarked, expiring in 72 hours, created in ≤ 6 clicks; revocation effective ≤ 60 s; every open logged and visible to the owner |
| Structure survives change | Folder views are computed from canonical IDs and metadata; a release that renames, reorders or adds folder views changes zero stored objects (NN-12) |
| Bulk intake | A 5,000-file folder tree or ZIP maps, previews and commits in one job with duplicate detection and no overwrite; re-import of an `LD-EXPORT-1.0` package maps 100% from its manifest |
| Nothing expires unnoticed | Every document with an expiry or renewal date produces reminders at the configured offsets; dashboard of "expiring in 30/60/90 days" |
| Family and legacy | An individual can add family members, guardians for dependants and a nominee with time-locked legacy access; the nominee release flow completes with identity verification and a cancellable waiting period |
| Lawful by construction | No full Aadhaar number is ever written to storage or to derived text (NN-04); DigiLocker documents are stored as URI + verification result unless a permitted retained copy is recorded (NN-42) |
| Portable | Every record type in this phase is registered in `xpt.export_map` and exports in `LD-EXPORT-1.0` without staff help (NN-11) |

"Done" for an individual: from the home screen they photograph a rent agreement, it is auto-classified as "Rent agreement", the expiry date is extracted as a suggestion, they confirm it, a renewal reminder is set, and they share pages 1–4 with their landlord's advocate for 7 days, view-only — in under two minutes.

---

### Scope (in / out)

**In scope**

- Canonical document model: documents, versions, derived-rendition links, document links to records, relationships, folders as views, smart folders and saved views.
- Personal Legal Vault (individual tenant type) and Company DMS (company tenant type) on one engine with different defaults.
- Metadata schemas per document type (content packs), tags, custom fields.
- Versions, check-in/check-out, compare, restore.
- Search (full text, metadata, semantic, Indic), filters, facets, saved views.
- Selective sharing: internal and external share packs (document, version, page range, redacted copy), expiry, watermark, download/print control, view-only, OTP, revocation, access log; shares to counterparties, advocates, family, nominee and ecosystem apps (through `int`).
- Ingestion channels: web upload, drag-and-drop, phone camera scanner, device scanner (TWAIN-free: via OS share sheet/PDF), email-in, WhatsApp forward (flagged), DigiLocker pull, connector pull (OneDrive/SharePoint/Google Drive), bulk folder/ZIP intake (with the P20 importer).
- `packages/dix` baseline: malware scan, content disarm for renditions, true-type sniffing, print OCR for search, Aadhaar detection and masking at ingest.
- Retention schedules, legal hold, recycle bin, disposal with approval and disposal certificate.
- Reminders on expiry/renewal facts (IDs, leases, insurance, warranties, licences, PUC, registrations).
- Family vault, dependants, guardians, nominee/legacy access.
- Document health checks (rule-driven).
- Office-openable files; optional co-editing in the customer's own Microsoft 365 or Google Workspace.
- Mobile vault including encrypted offline cache.
- Pricing hooks: storage quotas, overage meter, add-on entitlements.

**Out of scope (owner phase)**

| Item | Owner |
|---|---|
| Handwriting/screenshot type copies, translation, field extraction beyond expiry-date suggestions, PII redaction suggestions | P05 |
| Template assembly, AI drafting | P06 |
| Negotiation rounds, redlines, deal rooms for negotiation, obligations register | P07 |
| eSign, eStamp, execution formalities, evidence packs, BSA s.63 certificate service | P08 |
| Vidhi Q&A over documents ("ask your vault"), agents | P09 (P04 exposes permission-scoped retrieval) |
| Court bundles, annexure builder, court render profiles | P10 |
| Matter and case records | P11 |
| Export packaging, BYO storage sync, import engine | P20 (P04 registers record types and supplies mapping UX) |
| Mobile store release and device-trust plumbing | P22 (P04 specifies vault behaviour) |
| Credential vault (portal passwords) | `cvl` (P18) — never stored in the DMS |

---

## Phase P05 — Document Intelligence: OCR, Handwriting/Screenshot Type Copy, Translation

**File:** `phases/P05_Document_Intelligence_OCR_TypeCopy_and_Translation.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (canonical document model, `drv_` renditions, ingest workflow, `packages/dix` baseline with print OCR and Aadhaar mask-before-commit, viewer, redaction tool, confidentiality classes), P09 runtime (`packages/ai` gateway: Claude vision and text via Amazon Bedrock India, guardrails, prompt registry, evaluation harness, credit metering), P08 (`sgn` evidence ledger and `Bsa63CertificateService`), P03 (rule engine, settings registry), P16 (marketplace fulfilment for certified translation and expert Part B services — stubbed until P16 ships). External: OCR engines (self-hosted), `TRANSLATE_PORT` adapters (Bhashini [VERIFY], Google/Azure India-region fallbacks), Bedrock India.
> **Sequencing:** Wave 2. Sprints 1–2: engine router, print OCR upgrade, handwriting and screenshot reading, Aadhaar detection on derived text; sprints 3–4: type copy generator, side-by-side editor, verification and labels, WhatsApp export parser; sprint 5: language identification and machine translation with glossary locks; sprint 6: extraction, classification and PII redaction suggestions; sprint 7: evaluation sets, quality tiers, petition/claim attachment contracts with P10/P15, hardening. P10 consumes the type-copy and translation rendition contract from sprint 4 (freeze point: `drv_` kinds, labels and anchor format at end of sprint 3).
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (personas), F (eligibility families — classification feeds the gate), H (agent roster — `AGT_EVIDENCE_CLERK` #8, `AGT_TRANSLATOR` #9, `AGT_DMS_LIBRARIAN` #20), K (`LD-EXPORT-1.0`), R (settings), W (open items).
> **Requirements covered:** R-044, R-045, R-046 (correct AI errors), R-008, R-043; contributes to R-007, R-012, R-061, R-079 (pleadings annexures), R-083 (grievance evidence), R-025.
> **Decisions applied:** D-07, D-14, D-15 · **Challenges applied:** CH-11, CH-28 · **Non-negotiables tested:** NN-04, NN-09, NN-10, NN-13, NN-14, NN-15, NN-25, NN-28, NN-32, NN-38, NN-43, NN-46, NN-48
> **Estimated effort:** 7 two-week sprints, squad of 8 (ML/AI engineers 2, backend 2, web 1, linguist-QA 1, evaluation/data 1, QA/accessibility 1), plus a part-time panel of language reviewers for the evaluation sets.

### Objective and business outcome

Litigants and companies in India rely on documents that machines read badly: handwritten agreements and letters, photographed registers, WhatsApp chats, screenshots of UPI payments and bank messages, regional-language notices. The brief asks that AI "reads WhatsApp screenshots and handwritten documents, attaches them to the petition/claim with the typed copy; users can correct AI errors", plus translation into English (R-044, R-045, R-046).

P05 delivers that safely. The original stays the evidence (NN-09); everything the machine produces is a **derived rendition** — labelled, versioned, anchored to the page and line it came from, with confidence shown, corrected by a human and signed off before it is used in a filing. WhatsApp evidence is ingested from the **native chat export** wherever possible, hashed at upload and supported by a BSA 2023 s.63(4) certificate workflow (CH-28; R3 LG-091). Machine translations are labelled as such; filings route to certified translation (NN-48; CH-11).

| Outcome | Exit-gate measure |
|---|---|
| Handwriting usable | On the evaluation set, printed English/Hindi OCR character error rate (CER) ≤ 2%; handwritten English CER ≤ 8%, handwritten Hindi ≤ 12% before human correction **[targets to be confirmed by baseline run]**; every line carries a confidence band and a page/line anchor |
| Human in control | 100% of type copies attached to a filing are in `USER_CORRECTED` or `VERIFIED` status, or carry an explicit "not verified" acknowledgement shown in the bundle index |
| WhatsApp done right | A native export ZIP of 10,000 messages parses in ≤ 60 s with zero dropped lines on the 12 locale fixtures; ambiguous date formats are asked, never guessed |
| Languages | Language identification on 28 languages (22 Eighth-Schedule + 6 UN official languages) with per-language quality tiers published; translation to English available for all, marked machine translation |
| Aadhaar never leaks into derived text | Zero unmasked Aadhaar numbers in OCR text, type copies, translations, extractions, search index, logs (NN-04) on the red-team set |
| Extraction saves time | Parties, dates, amounts and key clauses proposed for ≥ 85% of agreements in the evaluation set with precision ≥ 0.95 on confirmed fields; obligations proposed to P07 |
| Court-ready | One action attaches original + type copy + translation as paired annexures to a P10 petition or P15 claim, with index rows, page references and the s.63 Part A draft |

---

### Scope (in / out)

**In scope**

- Engine router for OCR, vision reading and translation by content type × language/script × data class.
- Print OCR (deterministic engines) upgrade from the P04 baseline: layout, tables, reading order, multi-column, stamps/seals detection.
- Handwriting, screenshot and photographed-document reading with Claude vision (Bedrock India).
- Native WhatsApp chat-export ingestion (Android/iOS variants), chat screenshots, SMS/UPI/bank-app screenshots, email files.
- Type copy generation in court-acceptable formats with page/line anchors; side-by-side correction editor; confidence highlighting; verification and reviewer sign-off; fixed labels.
- Attachment contract for petitions (P10) and consumer claims/grievances (P15).
- BSA s.63 certificate workflow for uploaded electronic records (using the P08 service).
- Language identification for 28 languages and code-mixed romanised Indic; machine translation to English and between supported languages; legal glossary and term locks; back-translation checks.
- Certified-translation hand-off (marketplace, P16).
- Aadhaar detection and masking on all derived outputs (defence in depth over P04).
- Classification, metadata and clause/obligation extraction; PII redaction suggestions.
- Evaluation sets and quality tiers per language; regression gates per model/engine version.
- Credit metering hooks.

**Out of scope (owner)**

| Item | Owner |
|---|---|
| Storage, versions, sharing, viewer, manual redaction tool | P04 |
| Court render profiles, annexure builder, bundle pagination, e-filing exports | P10 (P05 supplies renditions and anchors) |
| Vidhi Q&A over documents, summaries, legal research | P09 |
| Obligations register and renewals | P07 (`clm`) — P05 proposes |
| Signed-document evidence packs and the certificate generator itself | P08 |
| Certified translators' and experts' engagement, payment and payout | P16 |
| Voice-note transcription for Vidhi intake | P09 (shares the language catalogue) |

---

## Phase P06 — Template Library and AI Drafting Studio

**File:** `phases/P06_Template_Library_and_AI_Drafting_Studio.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P03 (settings registry, `RULES_PORT` with GoRules ZEN/CEL, jurisdiction packs, State stamp/registration rule packs as data); P04 (Legal Vault: `doc_`/`ver_`, Object Lock, folder views, sharing); P09 runtime (Vidhi model gateway `packages/ai`, retrieval, citation resolver, guardrails, credit metering); P02 (maker-checker engine, roles, delivery grants); P01 (accounts, anonymous-to-registered conversion, consent artefacts). Consumers: P07 (CLM uses templates, clause library and playbooks), P08 (signing reads stamp/registration/eligibility metadata), P10 (Pleadings Studio reuses the template engine), P16 (review SKUs), P17 (credits, export quotas, prices), P21 (public document pages embed the drafting widget).
> **Sequencing:** Sprint 1–2: template schema, docgen, interview engine, 20 launch templates. Sprint 3–4: clause library, variants, language versions, export, Template Studio with maker-checker. Sprint 5–6: AI-custom lane, Vidhi tools, review gate, review SKU hand-off. Sprint 7–8: tenant templates/playbooks, analytics, content backlog, Wave 1 content load (Appendix E wave 1). **Freeze point:** the template schema (§4B) and clause object (§4D) freeze at the end of sprint 2 because P07, P08 and P10 bind to them.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles and permissions), E (template, pleading and service taxonomy — the content load list), F (instrument eligibility gate), H (agent roster), K (`LD-EXPORT-1.0`), M (marketplace professional rules — for the review SKU), R (settings registry), W (open items).
> **Requirements covered:** R-004, R-006, R-007, R-008, R-009, R-010 (drafting part), R-019, R-027, R-030, R-038 (agreements, policies), R-045, R-046, R-047, R-070, R-071, R-087, R-090 (content quality), R-091.
> **Decisions applied:** D-04, D-07, D-10, D-14, D-15, D-17 · **Challenges applied:** CH-11, CH-12, CH-14, CH-30 · **Non-negotiables tested:** NN-01, NN-02, NN-07, NN-08, NN-09, NN-11, NN-13, NN-14, NN-15, NN-18, NN-20, NN-28, NN-29, NN-30, NN-38, NN-45, NN-48, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, frontend 2, docgen/redline 1, AI 1, QA 1) plus 1 legal content analyst and the `PLT_LEGAL_REVIEWER` panel for content.

### Objective and business outcome

LawDocs wins or loses on its first draft. A person who lands on the "Residential Rent Agreement" page must leave with a fair, correct, State-aware draft in minutes, free; a company legal team must turn its own paper into a governed, reusable template without a developer. P06 builds the template library from the owner's Documents manual (~330 unique documents, 18 categories, 134 sub-categories — R5 §8.1; Appendix E resolves three further duplicates, leaving 327 canonical templates), the clause library, the guided interview with live preview, and the AI Drafting Studio with Vidhi.

The phase carries one legal line that the owner's brief blurs and that we hold firmly (CH-30, NN-14, R4 §6.4):

| Lane | What it is | Price | Gate |
|---|---|---|---|
| **Template automation** | A lawyer-authored, versioned template filled deterministically from the user's answers. No model writes document text. | Free on every public document page | None beyond the template's own reviewer of record |
| **AI-custom drafting** | Vidhi writes or rewrites clauses that are not in the vetted template | AI credits | Labelled **"AI draft — not reviewed by a professional"**; for individuals, no clean export, eStamp or eSign until a qualified reviewer approves (one-click paid review) |

The owner asked for "draft with AI free on every page". We implement it as free template automation plus paid, gated AI customisation. The reasons are the Anthropic Usage Policy treatment of preparing legal documents for individuals as high-risk (qualified human review before delivery, AI disclosure — R4 D-R4-09 [VERIFY effective date 12 Nov 2026]), the Advocates Act 1961 ss.29/33 boundary (R3 LG-110, LG-119), and NN-14.

**Outcomes and exit-gate measures**

| Outcome | Measure at exit |
|---|---|
| Library live | Appendix E wave-1 documents published with reviewer of record, effective date and law-as-of date; 0 published templates with an open outdated-law backlog item |
| Fast first draft | Median time from page load to downloadable draft ≤ 6 minutes for wave-1 templates; ≤ 3 taps from a document page to the first question |
| Neutral by design | 100% of platform templates pass the neutrality checklist (§4C) |
| Deterministic assembly | Same answers + same template version → byte-identical DOCX body (excluding metadata timestamps) in CI |
| AI clearly separated | 100% of AI-touched drafts carry the AI label and lane flag; 0 AI-custom drafts for individuals reach eSign or clean export without a review record (NN-14 test) |
| Review upsell | "Hire a professional to review" available from every draft in ≤ 2 taps; price shown before start (NN-50) |
| Content without code | A new template, clause, State variant or language version is published by content staff through maker-checker with no code release (NN-30) |
| Multilingual | Interview UI in the 10 launch languages (D-07); vetted language versions for the top 30 wave-1 templates in Hindi; bilingual side-by-side export |

---

### Scope (in / out)

**In scope**
- Template library and taxonomy (18 categories → 134 sub-categories → documents) as data; canonical document IDs from Appendix E; duplicates resolved to one canonical template.
- Template schema: questionnaire, variables, computed fields, conditional clauses, State/jurisdiction variants, language versions, stamp and registration metadata, eligibility link, execution formalities, reviewer of record, version, effective dates, sources, neutrality record.
- Clause library with fallback ladders, risk notes, plain-language explanations and "i" keys.
- Guided interview with live preview (web and mobile), save and resume, anonymous start.
- Two drafting lanes (template automation; AI-custom) with labels, credits, review gate and the "Hire a professional to review" hand-off to P16.
- Vidhi drafting assistant tools: explain clause, change tone, add clause, translate draft, plain-language summary, consistency check.
- Multilingual drafts, vetted language versions, machine translation labelling (NN-48), bilingual side-by-side.
- Export to DOCX and PDF (PDF/A-2b option), save to Vault, hand-off to P07 negotiation and P08 signing.
- Template Studio for `PLT_CONTENT_EDITOR` (maker) and `PLT_LEGAL_REVIEWER` (checker/reviewer of record) with test harness and publication without code release.
- Tenant private templates and clause playbooks (companies), with tenant maker-checker.
- Template analytics (aggregate, privacy-safe).
- Content legal-review backlog: outdated law, copied third-party text, stubs (R5 §3–§5) and periodic law-change sweeps.

**Out of scope (owner phase)**
- Negotiation, redlines between parties, deal rooms, approvals, obligations: **P07** (P06 provides the clause playbook positions P07 uses).
- eSign, eStamp purchase, duty calculation, signing ceremonies, evidence packs: **P08** (P06 supplies template metadata only).
- Instrument eligibility rules themselves: **Appendix F** (owned by P08); P06 links each template to a row.
- Court pleadings, notices, court formats, limitation: **P10** (reuses the P06 engine).
- OCR, type copies, translation of uploaded documents: **P05** (P06 translates drafts it generates through the same `TRANSLATE_PORT`).
- Public page copy, SEO, page templates and CMS: **P21** (P06 provides the embeddable widget and the content-status feed).
- Review SKU catalogue, professional assignment, payouts: **P16**; prices, credits, plans: **P17** (engine in OH8).
- Vidhi runtime, agent workforce and autonomy model: **P09**.

---

## Phase P07 — Contract Lifecycle: Negotiation, Redlines, Deal Rooms, Messaging, Approvals

**File:** `phases/P07_Contract_Lifecycle_Negotiation_Redlines_and_Deal_Rooms.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (Vault/DMS: `doc_`/`ver_`, Object Lock, sharing, bulk intake); P06 (templates, clause library, position ladders, tenant playbooks, drafts); P02 (org structure, positions, DoA attributes, maker-checker engine, delivery grants); P03 (settings, `RULES_PORT` decision tables); P01 (accounts, `CP_GUEST` magic-link + OTP, step-up MFA); P09 runtime (Vidhi gateway, credit metering); P05 (OCR of scanned counterparty paper — Wave 2; until then PDF intake is text-layer only). Hand-off: P08 (eSign, eStamp, formalities, evidence). Later consumers: P11 (disputes from contracts), P13 (CLO dashboard, governance approvals, legal intake desk), P20 (export).
> **Sequencing:** Sprint 1–2: agreement record, deal room, guest access, messaging, version sharing. Sprint 3–4: `packages/redline` compare/accept/reject, rounds, silent-edit detection. Sprint 5: approvals/DoA, version lock, P08 hand-off. Sprint 6: obligations, key dates, renewals, amendments. Sprint 7: intake (form, email, Teams), repository views, legacy import, CLO dashboard. Sprint 8: company-to-company rooms, Office/Google co-editing, AI playbook redlines, hardening. **Freeze point:** the version/visibility model and change-record schema (§4F) freeze at the end of sprint 3 — P08 signs locked hashes from it.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles), E (taxonomy for agreement types), F (instrument eligibility gate, owned by P08), H (agent roster), K (`LD-EXPORT-1.0`), R (settings), W (open items), Y (Ecosystem Spec change requests).
> **Requirements covered:** R-006, R-007, R-011, R-018 (CLO/KMP agents, contract part), R-026, R-027, R-030, R-043, R-047, R-053, R-055, R-060, R-064, R-067, R-077, R-086 (SpotDraft/Ironclad/Leegality parity), R-091.
> **Decisions applied:** D-02, D-10, D-12, D-17 · **Challenges applied:** CH-12, CH-14, CH-29 · **Non-negotiables tested:** NN-01, NN-02, NN-07, NN-08, NN-09, NN-11, NN-13, NN-14, NN-17, NN-18, NN-24, NN-28, NN-34, NN-37, NN-40, NN-43, NN-45, NN-46
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, frontend 2, redline/OOXML 1, integrations 1, QA 1).

### Objective and business outcome

Two parties — two people, two companies, or one of each — must agree a text, know exactly what changed in every round, keep their internal discussion private, get the right internal approvals, and send the one agreed version to signature. After signing, the company must never miss a renewal, a notice window or a payment obligation. P07 delivers this as LawDocs' contract lifecycle (Ironclad's Create → Review → Approve → Sign → Store → Fulfil → Analyse, adapted — R1 §8), with deal rooms where parties message while negotiating (R-077) and a **deterministic** redline engine (NN-37).

The brief says "the tool sufficient instead of a legal team". We build the legal-operations layer a single CLO can run — intake, playbooks, approvals, obligations — with Vidhi as a maker and professionals on demand (CH-14, D-17). We do not claim it replaces advocates.

| Outcome | Exit-gate measure |
|---|---|
| Faster cycle | Median intake → locked version for NDAs ≤ 1 working day in pilot tenants; TAT measured per type |
| Every change accountable | 100% of changes between any two shared versions are listed with author, round and decision; accept/reject logged per change (NN-37) |
| No silent edits | 100% of untracked differences in a counterparty-returned DOCX are detected and shown (test corpus of 200 files) |
| Internal stays internal | 0 internal comments, internal versions or internal metadata in any file or view available to a counterparty (automated test on every share) |
| Right approvals | No version reaches signing without the approvals the DoA matrix requires for that version hash |
| Nothing lapses | Every executed agreement has verified key dates; renewal and notice-window reminders fire at configured offsets |
| Low friction for counterparties | A guest can review, comment, upload a redline and confirm the agreed version without creating an account, ≤ 3 taps from the invitation |

---

### Scope (in / out)

**In scope:** contract intake (web form, mobile, email-in, Microsoft Teams app); agreement record and matter linkage; authoring from P06 templates, tenant templates or third-party paper; deal rooms with internal and counterparty participants (`CP_GUEST`); secure messaging, threads and clause-anchored comments with internal vs shared channels; negotiation rounds; deterministic compare of any two versions; accept/reject per change; silent-edit detection; playbook-based AI redline suggestions (maker-only); approval workflows (DoA matrix, maker-checker, delegation); version lock and hand-off to P08; post-signature repository; obligation and key-date extraction with human verification; renewals, terminations, amendments, novations; repository views and legacy import; CLM dashboards for the CLO; company-to-company contracting where both parties are on LawDocs; optional co-editing in the customer's own Microsoft 365 or Google Workspace; bulk contracting from a spreadsheet.

**Out of scope (owner phase):** eSign, eStamp, signing order, evidence packs, wet-ink execution recording — **P08**. Template and clause authoring, playbook authoring UI — **P06**. Litigation and dispute management arising from a contract — **P11** (and Equator via `int`). Board/committee approvals as governance records — **P13** (`gov` kernel; LDC is SoR where the tenant uses LDC — NN-47). OCR of scans — **P05**. Legal spend and counsel panel — **P13**. CRM (deal pipeline of the customer's sales team) — not LawDocs; CRM connectors are P19.

---

## Phase P08 — eSign, eStamp, Execution and Evidence

**File:** `phases/P08_eSign_eStamp_Execution_and_Evidence.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (identities, OTP/passkey sessions and step-up, `CP_GUEST`, KYC artefacts for signer identity binding), P02 (delegation of authority, authorised signatories, maker-checker), P03 (rule engine for the eligibility gate, duty rules and formalities; settings registry), P04 (frozen PDFs, executed versions under compliance-mode Object Lock, relationships, health checks), P06 (template answers → duty inputs, execution blocks), P07 (final agreed version, negotiation threads), P17 (credits, meters, duty pass-through presentation through OH8). External: eSign aggregator(s) and ESPs, eStamp vendor(s), DSC local signing agent, RFC 3161 timestamp authority, Razorpay via OH8.
> **Sequencing:** Wave 1. Sprint 1: provider registry, ports, licence monitor, eligibility gate (Appendix F runtime); sprints 2–3: signing ceremonies, Aadhaar eSign through the primary aggregator, consent, evidence capture; sprint 4: DSC agent, electronic acceptance, assisted and mobile signing, messaging; sprint 5: eStamp (attach existing e-stamp with UIN verification, then purchase), duty calculator (advisory), stamp-before-sign lock; sprint 6: formalities gate, wet-ink/notary/registration packs; sprint 7: evidence pack, certificate of completion, s.63 certificate service, validation, LTV, public verification; sprint 8: bulk signing, second ESP route, amendments/void flows, hardening and ASP audit readiness. **Freeze points:** port contracts (`ESIGN_PORT`, `ESTAMP_PORT`, `DSC_PORT`) end of sprint 1; Appendix F row schema end of sprint 1 (content can change any time after, NN-30).
> **Binding appendices:** F (instrument eligibility matrix and eStamp State coverage registry — runtime data; §9 supersedes the R5 eSign flags, X-02), A (state machines A.31–A.34), B (data model, events, errors), D (personas), U (accessibility), K (`LD-EXPORT-1.0`), R (settings), W (open items), Y (Ecosystem Spec change request — LD as producer).
> **Requirements covered:** R-006, R-009 (signing part; Aadhaar is never login), R-011 (enter, eSign, amend, preserve), R-039 (SLAs eSigned), R-077, R-078, R-067; contributes to R-017, R-025, R-035, R-054.
> **Decisions applied:** D-12, D-10, D-17 · **Challenges applied:** CH-01, CH-12, CH-13, CH-16, CH-28 · **Non-negotiables tested:** NN-03, NN-04, NN-06, NN-07, NN-08, NN-09, NN-10, NN-13, NN-18, NN-22, NN-24, NN-28, NN-34, NN-37, NN-38, NN-39, NN-40, NN-43, NN-45, NN-46, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, web 1, mobile 1, PKI/security engineer 1, integrations 1, QA/accessibility 1), plus a part-time legal analyst for Appendix F rows and State registry verification.

### Objective and business outcome

The brief's core promise is "two parties … enter into personal, business or property contracts by making Aadhaar-based eSign", with eStamp "buy … online or attach stamp papers, then eSign" (R-006, R-078). P08 delivers execution that a court will respect: the right instrument goes to the right method, stamp duty is paid **before** signing, formalities are tracked to completion, and every execution leaves an evidence pack with a BSA 2023 s.63 certificate draft (NN-10).

Two corrections to the brief are built in. (1) **Not every instrument can be eSigned**: the IT Act 2000 First Schedule (as amended by S.O. 4720(E) [VERIFY: Gazette text; S.O. dated 26 Sep 2022, published 4 Oct 2022 — Appendix W §W.9 LA-01]) excludes negotiable instruments other than cheques (with a regulated-entity carve-out), powers of attorney (with a regulated-entity carve-out), trusts, and wills/testamentary dispositions; registrable property instruments still need the sub-registrar (R3 LG-003, LG-104) **[LAW]** — CH-12, NN-07. (2) **LawDocs does not sell stamp paper**: certificates are issued only through the CRA (SHCIL) and authorised collection centres or State routes; LawDocs procures as the user's agent through a contracted vendor, passes duty through at actuals and discloses its own fee (R3 LG-098–100) — CH-13, NN-08.

| Outcome | Exit-gate measure |
|---|---|
| Lawful routing | 100% of signing requests pass the eligibility gate; 0 excluded instruments reach an ESP in the test corpus (all 35 R5 "not valid" templates plus wills/POAs/trusts/NIs uploaded as free documents) |
| Stamp before sign | 0 signing requests started for a chargeable instrument without a verified stamp record or a cited exemption |
| Fast signing | Median time from "Send" to all-signed ≤ 24 h for two-party Aadhaar eSign; signer completes in ≤ 4 taps + OTP on mobile |
| Resilient | ESP failover within one attempt; ≥ 99% successful completion for started Aadhaar eSign sessions excluding signer abandonment; routing never sent to an ESP whose licence date has passed without renewal evidence |
| Provable | Every completed execution has an evidence pack (hashes, consent versions, signer events, provider evidence, validation report, certificate of completion) and a s.63 Part A draft available in one click |
| Formalities complete | No document reaches `EXECUTED` while a required formality is open, unless waived by an authorised user with reason (NN-40) |
| Transparent money | Every checkout shows stamp duty (at actuals), LawDocs facilitation fee, ESP/eSign credits and GST separately, with the total before payment (NN-22, NN-50) |

---

### Scope (in / out)

**In scope:** provider-neutral ports and adapters (`ESIGN_PORT`, `ESTAMP_PORT`, `DSC_PORT`, `TSA_PORT`); provider registry, health and licence monitoring; the instrument eligibility gate (Appendix F runtime); signing requests and ceremonies; Aadhaar eSign (OTP; biometric at assisted counters; face only if verified), account-based eSign (API 3.x), DSC signing for company signatories, electronic acceptance where lawful; in-person/assisted and mobile signing; messaging with counterparties during signing; bulk signing; stamp-before-sign with eStamp purchase via authorised channels, attachment of existing e-stamp certificates with UIN verification, physical stamp paper/franking/e-SBTR for the wet-ink route; stamp duty calculator per State × instrument (advisory until verified); formalities gate (witness, notary, registration, board approval, counterparties) with appointment tracking; wet-ink/notary/registration packs; evidence packs, certificate of completion, `Bsa63CertificateService`; signature validation, LTV, timestamping, public hash verification; amendments, re-execution, cancellation, void, decline and expiry; pricing hooks; ecosystem boundary rules.

**Out of scope (owner):** drafting and negotiation (P06, P07); storage, sharing and health-check UI (P04); type copies and translations (P05); marketplace notary/registration-assistance professionals (P16, consumed here as services); billing engine and GST invoices (OH8 via P17); mobile store release (P22); court e-filing signatures for pleadings (P10 uses this phase's DSC/eSign services under forum rules).

---

## Phase P09 — Vidhi AI Employee and Agent Workforce

**File:** `phases/P09_Vidhi_AI_Employee_and_Agent_Workforce.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, audit ledger, outbox, Temporal, S3 Object Lock, OpenTelemetry), P02 (tenancy, org structure, roles, maker-checker, delegations), P03 (settings registry, rule engine `rul`, jurisdiction packs — the deterministic engines Vidhi must call), P04 (Legal Vault/DMS — documents, versions, folders, permissions). Consumes read models of P05–P08 and P10–P16 as they ship and degrades to stated fallbacks when they do not exist. External: Amazon Bedrock (ap-south-1 ⇄ ap-south-2 `in.` geographic profile), Anthropic API (public content only), Keycloak (agent clients, token exchange), Cerbos, OpenSearch + pgvector, speech/translation adapters (`INDIC_SPEECH_PORT`, `TRANSLATE_PORT`), CPaaS adapters (Appendix J).
>
> **Sequencing:** **Wave 1 — runtime (4 sprints):** `packages/ai` gateway, routing, model registry, prompt registry, PII scrubber, citation resolver, retrieval over platform notebooks and the tenant vault, AI run ledger, credits meter, Qualified Review Gate (QRG) service and the individual Vidhi chat (general-information mode). Freeze point at end of sprint 2: the `AiGateway` TypeScript interface and the `vidhi_answer_v1` / `vidhi_draft_v1` schemas, so P05, P06 and P07 can call the runtime. **Wave 2 (3 sprints):** company Vidhi panel, embedded actions, agent workforce at L0–L2, approvals, kill switches, activity log and daily digest, MCP server (read + propose). **Wave 3 (3 sprints):** L3 envelopes for eligible agents, missions, schedules at scale, MCP client, A2A (behind the Appendix Y change request), voice intake agent, full multilingual evaluation suites.
>
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), H (Vidhi AI Agent Specification and Prompt Library), J (Jio Business Services and Telecom Rules), D (roles and permissions), F (instrument eligibility), K (`LD-EXPORT-1.0`), M (marketplace professional rules), R (settings registry), W (open items), Y (Ecosystem Spec v1.2 change requests).
>
> **Requirements covered:** R-007, R-008, R-010, R-015, R-018, R-019 (Vidhi "i" explanations), R-026, R-027, R-029, R-030, R-044 (runtime for type copy), R-045 (runtime for translation), R-047, R-060, R-061 (self-help triage), R-062, R-063 (AI hours-saved inputs), R-087 (runtime for "Draft with AI free" + "Hire a professional"), R-091.
>
> **Decisions applied:** D-01, D-05, D-07, D-10, D-14, D-15, D-17 · **Challenges applied:** CH-11, CH-14, CH-17, CH-30 · **Non-negotiables tested:** NN-01, NN-02, NN-04, NN-05, NN-11, NN-13, NN-14, NN-15, NN-18, NN-20, NN-21, NN-25, NN-28, NN-29, NN-32, NN-34, NN-38, NN-39, NN-43, NN-45, NN-46, NN-48
>
> **Estimated effort:** 10 two-week sprints (runtime 4 in Wave 1; 3 in Wave 2; 3 in Wave 3), squad of 8 (AI platform engineers 3, agent and tool engineers 2, retrieval/notebooks 1, evaluation and safety 1, full-stack UI 1; plus a part-time `PLT_LEGAL_REVIEWER` for golden sets and disclaimers).

### Objective and business outcome

Vidhi is LawDocs' AI employee (D-15). For an individual it is the first place to go with a legal problem: it listens in the user's language, explains the position in plain words, lays out the options, prepares the letter, notice, complaint or agreement, and — where the law or Anthropic's Usage Policy requires it — routes the work to a qualified professional before it is used. For a company it is a workforce of role agents that work beside the CLO, company secretary, CFO, CEO and the board: they read contracts, track hearings and trademarks, draft board papers and minutes, chase signatures, and report what they did every evening. Vidhi never replaces an advocate (D-17, CH-14); it makes a one-person legal function workable and makes self-help safe.

Four hard limits apply to every surface built in this phase:

1. **Acts for a named human, inside that human's permissions** (NN-01, NN-43). Agents have no standing rights.
2. **Cites or says it cannot** (NN-14). Every legal citation resolves against the rules register or a retrieved source or is shown as "unverified".
3. **Drafts and proposes; never decides or acts externally on its own** (NN-13, NN-43). Sign, pay, file, send, share outside the tenant, call, accept, withdraw and delete need a human's per-action confirmation.
4. **India-resident, no training, scrubbed** (NN-15, NN-25). Personal and client data goes only to the Bedrock India route.

| Outcome | Exit-gate measure |
|---|---|
| Individuals get an answer, not a menu | From the home screen, a user reaches a triaged, cited plain-language answer in ≤ 2 taps and ≤ 60 s p95 in any of the 10 launch languages (D-07); 100% of answers carry a dated source list or an "unverified" label; ≥ 90% of golden-set problems are routed to the correct track (DIY / notice / complaint / consult / court). |
| Safe self-help drafting | 100% of AI-custom drafts for individuals carry "AI draft — not reviewed by a professional" and cannot be sent for eSign or downloaded as "final" until the Qualified Review Gate records a review (NN-14; Anthropic Usage Policy legal High-risk Area, R4 D-R4-09). QRG standard turnaround ≤ 4 working hours p80. |
| Company workforce is governable | A tenant admin can hire an agent, name a sponsor, set its autonomy (L0–L2; L3 for eligible agents), budget and schedule in ≤ 6 clicks; pause it in ≤ 2 clicks with effect ≤ 60 s; every agent action appears in the activity log and the daily "What my AI employee did today" digest. |
| Grounded and accurate | On the Appendix H golden sets: citation validity 100% (no fabricated section, case or circular), number/date fidelity 100% in translations and summaries, correct-refusal rate ≥ 0.95 on out-of-corpus questions, triage accuracy ≥ 0.90; zero cross-tenant retrieval in canary tests. |
| Affordable | AI provider cost ≤ 40% of the credit price at the blended model mix (R6); 100% of runs metered to tenant/user/agent/mission with credits visible in Settings → Billing → Usage. |
| Interoperable | Customers' own assistants (Copilot, Claude, ChatGPT) can read their LawDocs matters, documents and calendars through the LawDocs MCP server as the signed-in user, with no prohibited tool exposed. |

---

### Scope (in / out)

**In scope**

- `ai` module and `packages/ai`: provider-neutral model gateway, routing policy (`R4-AI-01`), model registry and version pinning, prompt-template registry, prompt caching, batch, cost metering and AI credits, PII/secret scrubber, untrusted-content isolation, output validators, citation resolver, AI run ledger, evaluation harness, red-team suite, online monitoring, AI incident workflow.
- Retrieval: hybrid (OpenSearch BM25 with Indic analysers + pgvector) over tenant documents and **legal knowledge notebooks** — Statutes Register, Template and Clause Library, Glossary (`hlp` "i" terms), Firm/Company Playbooks, Court and Forum Guides, Tenant notebooks.
- **Qualified Review Gate (QRG)** service: review queue, reviewer eligibility, attestation, diff, AI-use stamp, SLA, one-click paid review (fee and engagement via P16/P17).
- **Vidhi chat for individuals** (Personal workspace, public widget on `apps/public`, mobile): triage → explain → options → draft/notice/complaint → hire a professional.
- **Vidhi for companies and professionals**: dockable panel, `@Vidhi`, command palette, embedded record actions, Work Inbox output cards.
- `agt` module and `packages/agents`: agent catalogue (Appendix H roster), tenant hiring, sponsors, autonomy L0–L4 with LawDocs ceilings, envelopes (playbooks), missions, schedules and triggers, memory policies, budgets, approvals, kill switches, activity log, daily digest, monthly agent review.
- Agent identity and delegation (Keycloak token exchange, Cerbos principal + actor checks).
- **MCP server** (`ld-mcp`) for customers' assistants and **MCP client** for tenant-registered servers.
- **A2A** agent cards for ecosystem hand-offs (Equator, LawDocsComply, Finbyx/Udofin) — transport only, mapped to Ecosystem contracts, flag OFF until Appendix Y approval.
- **Voice**: speech-to-text, text-to-speech and the inbound multilingual intake voice agent through adapters; synthetic-audio labelling.

**Out of scope (owned elsewhere)**

| Item | Owner |
|---|---|
| OCR/handwriting/screenshot pipeline, type-copy editor, translation workflow and certified-translation routing | P05 (`dix`) — calls this runtime |
| Template library, questionnaires, the Drafting Studio UI and the template lane's deterministic assembly | P06 (`tpl`, `drf`) — calls QRG and runtime |
| Redline engine and negotiation rooms | P07 (`clm`, `packages/redline`) |
| eSign/eStamp ceremonies and the instrument eligibility gate | P08 (`sgn`; Appendix F) |
| Pleadings, notices and court-drafting flows | P10 (`pld`) |
| Court and TM data feeds (licensed aggregators, user-entered numbers) | P11 (`lit`), P12 (`ipm`) |
| Board, committee, minutes and resolution workflows; Legal Department OS | P13 (`gov`, `lgo`) |
| Consumer Help case workflow, forum signposting rules, ethical wall | P15 (`chp`) |
| Professional registry, engagement terms, reviewer payouts | P16 (`mkp`) |
| AI-credit prices, packs, agent-seat SKUs, invoices | P17 (`bil`; engine OH8) |
| Delivery Console use of Vidhi by RMs | P18 (`sdc`) |
| `int` gateway, OAuth for third-party apps, developer portal, CPaaS adapters, outbound send rails | P19 (`int`, `packages/notify`, `packages/connectors`) |
| Public "Draft free with Vidhi" page blocks and CMS | P21 (`web`) |
| Model fine-tuning on customer data | Prohibited (NN-15). Platform fine-tuning on synthetic/public data needs an ADR, DPIA and owner approval [OWNER]. |
| Computer use or any automation of court, IP India, MCA, GST, bureau or government portals | Prohibited (NN-05). Computer use only in sandboxed internal QA. |

---

## Phase P10 — Pleadings, Notices and Court Drafting Studio

**File:** `phases/P10_Pleadings_Notices_and_Court_Drafting_Studio.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P06 (template engine, questionnaire engine, clause library, lanes, review gate, export, Template Studio — reused, not rebuilt); P05 (originals, OCR, handwriting/WhatsApp type copies, translations as derived renditions `drv_`); P04 (Vault, Object Lock, hashes); P08 (eSign where permitted, BSA s.63(4) certificate drafts, evidence packs); P09 runtime (Vidhi, citation resolver); P16 (advocate review and "hire an advocate" SKUs); P03 (rule packs: limitation, court fees, forum profiles). Consumer: P11 (a filed pleading becomes a court case record).
> **Sequencing:** Sprint 1–2: forum render profiles, document anatomy, annexure builder, index/pagination, PDF/A e-filing pack. Sprint 3: pleading interview + library load (Appendix E §4 wave 1). Sprint 4: legal notices and replies with dispatch and proof of delivery. Sprint 5: limitation and jurisdiction prompts, party-in-person mode, advocate review gate. Sprint 6: affidavit/verification routes, vakalatnama, P11 hand-off, hardening. **Freeze point:** render-profile token schema at the end of sprint 1 (P11 and P15 reuse it).
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles), E (§4 pleadings taxonomy; §7 outdated-law backlog), F (eligibility gate — affidavits and verifications are never eSign-only), H (agents), K (`LD-EXPORT-1.0`), M (marketplace rules for advocate SKUs), R (settings), W (open items).
> **Requirements covered:** R-012 (pre-filing part), R-044, R-045, R-061, R-079, R-084 (notice and court-drafting part), R-087, R-090, R-091.
> **Decisions applied:** D-05, D-06, D-07, D-17 · **Challenges applied:** CH-11, CH-14, CH-28, CH-30 · **Non-negotiables tested:** NN-05, NN-07, NN-09, NN-10, NN-11, NN-13, NN-14, NN-20, NN-28, NN-34, NN-38, NN-41, NN-48
> **Estimated effort:** 6 two-week sprints, squad of 8 (backend 2, frontend 2, docgen/PDF 1, AI 1, QA 1, legal content analyst 1) plus advocate reviewers from the `PLT_LEGAL_REVIEWER` panel.

### Objective and business outcome

Individuals facing a dispute and companies running litigation need court-ready documents: a properly formatted plaint or petition, a list of dates, a verified affidavit, a vakalatnama, annexures marked P-1, P-2 with typed copies of handwritten notes and WhatsApp screenshots and their translations, and a legal notice sent with proof of delivery. P10 delivers a Pleadings, Notices and Court Drafting Studio on the P06 engine, loaded from the owner's Pleadings manual (13 areas, 89 drafts → 70 consolidated pages — X-23 supersedes R5 §8.2's ≈68; FR-P10-01; Appendix E §4), **updated to the new criminal laws** (BNS, BNSS, BSA in force 1 July 2024), CPC 1908, Commercial Courts Act 2015 and Consumer Protection Act 2019.

Two lines we hold (and say plainly to the owner):
1. **LawDocs prepares documents; it does not file, argue or advise.** Filing, appearance and advice are for the party in person or an enrolled advocate (Advocates Act 1961 ss.29, 33 — R3 LG-110; NN-41). No auto-filing on any court portal and no portal automation (NN-05, NN-13). The manual's line "file directly before any High Court and Supreme Court" is withdrawn.
2. **AI-assisted court documents for individuals pass a qualified-review gate** before final download (NN-14, R4 §6.4 "pleadings self-help" row), and every AI-assisted document carries a disclosure line.

| Outcome | Exit-gate measure |
|---|---|
| Correct format | Exports validate against the selected forum render profile (page size, margins, font, spacing, numbering); unverified profiles never labelled "court-ready" |
| Correct law | 0 published pleading templates citing CrPC/IPC/Evidence Act/CPA 1986 as current law; old→new mapping shown where users search old sections |
| Annexures right | Every annexure referenced in the text exists in the index and vice versa; typed copies and translations sit next to their originals with labels; BSA s.63(4) certificate draft generated for each electronic-record annexure |
| Filing pack | PDF/A-2b, OCR text layer, bookmarks from index, continuous pagination, size split per profile — validated by veraPDF in CI |
| Notices with proof | Legal notices dispatched only after human confirmation, with dispatch evidence (India Post tracking, email delivery) attached to the notice record |
| Safe self-help | Party-in-person mode shows forum-specific disclaimers, legal-aid route and "hire an advocate" path at every final step |

---

### Scope (in / out)

**In scope:** pleadings library (13 areas, consolidated, variants as toggles — Appendix E §4); court-format render profiles and document anatomy (cover, index, synopsis and list of dates, memo of parties, body, prayer, verification, affidavit, vakalatnama, annexures, certificates); forum and jurisdiction prompts; limitation prompts (advisory); legal notices and replies (s.138 NI Act, s.80 CPC, money recovery, consumer, RERA, tenancy/eviction, employment dues, IP infringement, defamation, others from Appendix E) with dispatch and proof of delivery; party-in-person mode; annexure builder linking originals, type copies and translations from P05; e-filing preparation packs; advocate review gate and disclosure stamp; affidavit swearing route and verification signing route; hand-off to P11.

**Out of scope (owner phase):** case tracking, hearings, orders, cause lists — **P11**; filing on any portal — **never automated** (user or advocate files); OCR/type copy/translation engines — **P05**; consumer grievances before ombudsmen and regulators (RBI-IOS, Insurance Ombudsman) — **P15** (reuses P10 notices and formats); arbitration statements and Equator proceedings — **Equator** (EQ App. M) via `int`; criminal FIRs and police complaints drafting for others by LawDocs staff — not offered as a staff service (templates for self-use only, with review gate).

---

## Phase P11 — Litigation and Matter Management

**File:** `phases/P11_Litigation_and_Matter_Management.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P02 (organisations, departments, maker-checker, delegations), P03 (settings registry, `RULES_PORT`, limitation and forum rule packs), P04 (Legal Vault: folders, versions, legal hold, bulk folder intake), P05 (OCR, type copies and translation of orders and notices), P09 runtime (Vidhi agents `AGT_LITIGATION_CLERK`, `AGT_ORDER_DIGEST`, `AGT_HEARING_PREP`, `AGT_EVIDENCE_CLERK`, `AGT_NOTICE_RESPONDER`), P10 (notice register `ntc_`, pleadings `pld_`, annexure and bundle builder), P16 (marketplace engagements of advocates), P17 (plan limits, meters, add-on `LD-ADD-LIT`), P19 core (`int` gateway, connector framework, ecosystem inbox/outbox), P20 core (export map), P22 (push). External: two licensed court-data aggregators (contracts pending), Equator Resolution (ADR referral contract — Appendix Y), Finbyx/Udofin Recovery Suite (litigation events, Ecosystem Spec §6.10), LawDocsComply (when the tenant uses it).
> **Sequencing:** Wave 2. Sprint 1–2: matter/case model, forum registry, manual CNR, vault folders; freeze the `lit` read API (`GET /v1/lit/matters`, `/v1/lit/cases`, `/v1/lit/clocks`) at the end of sprint 2 for P12 (oppositions as matters) and P13 (CLO dashboard, board MIS). Sprint 3–5: court-data adapters, hearings, cause lists, orders, deadline engine. Sprint 6–7: counsel, spend, exposure, bundles, bulk import, individual view. Sprint 8–9: Equator referral, ecosystem projections, reports, mobile, hardening. The second court-data vendor can follow in Wave 2's last sprint (R6 §R6.6.6 v1.1).
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles and access matrix), H (agent roster), K (`LD-EXPORT-1.0` folder taxonomy), M (marketplace professional rules), R (settings registry), T (legal-department operating model and intake SLAs), W (verification log and open items), Y (Ecosystem Spec v1.2 change request).
> **Requirements covered:** R-002, R-012, R-017, R-019, R-021, R-023, R-026, R-027, R-030, R-047, R-060, R-061, R-062 (alerts), R-067, R-068, R-076, R-083 (status tracking for consumer cases that reach a forum), R-086.
> **Decisions applied:** D-02, D-05, D-07, D-10, D-14, D-15, D-17 · **Challenges applied:** CH-08, CH-14, CH-16, CH-27, CH-28, CH-31 · **Non-negotiables tested:** NN-01, NN-02, NN-05, NN-09, NN-10, NN-11, NN-13, NN-14, NN-17, NN-19, NN-20, NN-21, NN-24, NN-28, NN-29, NN-30, NN-34, NN-38, NN-39, NN-43, NN-45, NN-46
> **Estimated effort:** 9 two-week sprints, squad of 8 (backend 3, frontend 2, mobile 1, QA 1, integration 1) plus a part-time legal domain analyst (advocate with corporate and recovery litigation experience) and a chartered accountant for the exposure schedule.

### Objective and business outcome

Indian companies run litigation from spreadsheets, counsel e-mails and the eCourts app one case at a time. Individuals do not understand what "Stage: Appearance — next date 14.01.2027" means or what they must do next. This phase builds a Provakil-class matter and case management system (R1 §5; IMP-060 to IMP-069) for both audiences:

- **Companies:** one register of every dispute and pre-dispute (notices, suits, writs, arbitrations, consumer complaints, tribunal and regulatory proceedings), with hearings, cause lists, orders turned into tasks, limitation and order-compliance clocks, counsel and spend control, exposure estimates for the financial statements, document bundles and board/audit-committee MIS.
- **Individuals ("My cases"):** add a case by CNR or case number, see the status in plain language in their language, get reminders, keep every paper in the Legal Vault, and hire a professional when they need one.

LawDocs is a technology and legal-operations platform. It does not appear in court, give legal advice or file anything on anyone's behalf (NN-41, CH-14). Court data comes only from licensed sources or the user (NN-05, CH-27).

| Outcome | KPI and exit-gate measure |
|---|---|
| No missed date | 100% of active cases have an owner and a next date or an explicit "date awaited" status; missed-hearing-outcome rate < 2% after 48 hours in pilot; 0 missed limitation clocks in UAT |
| Data is honest | Every court-sourced field shows source, fetched-at time and a staleness label; 0 screens use "real-time", "live", "official" or "certified" for vendor data (NN-20) |
| Orders become actions | An uploaded order produces a confirmed digest and tasks in ≤ 3 clicks; 95% of directions have an owner within 1 business day |
| Company control | Board MIS and quarterly exposure schedule produced in ≤ 10 minutes for a 300-matter tenant; counsel invoice validated against budget before approval |
| Onboarding speed | 500-row Excel import with CNR de-duplication, preview and undo in < 5 minutes |
| Individual clarity | "What this status means / what happens next" shown for 100% of seeded status codes in the 10 launch languages (D-07) |
| Boundaries kept | Recovery cases from the Recovery Suite appear only as read-only projections; 0 LawDocs writes to recovery records (Ecosystem Spec §6.10) |

**Done for users.** A CLO opens Litigation Home, sees today's cause-list matches, overdue outcomes and clocks under 30 days, and clears them from one screen. An individual opens the app, taps "My cases", and reads "Your case is listed on 14 January 2027 before Court No. 4. The court will hear arguments on your application. Bring: copy of the agreement, payment receipts."

### Scope (in / out)

**In scope** (detailed in §4A–§4R)
- Matters: litigation, pre-litigation (notices, demands, opinions), arbitration and mediation, regulatory and quasi-judicial proceedings, criminal complaints where the tenant or individual is a party.
- Court cases across the Supreme Court, High Courts, district, commercial and family courts, NCLT/NCLAT, DRT/DRAT, consumer commissions, RERA authorities and appellate tribunals, other tribunals, Lok Adalats and arbitral tribunals; CNR and case-number capture; `COURT_DATA_PORT` with two licensed aggregators, manual refresh and staleness labels.
- Hearings calendar, cause-list matching, next-date tracking; orders and judgments with Vidhi digests and directions as tasks; limitation, appeal, pleading and order-compliance clocks.
- Counsel panel, external-counsel portal, fees, legal spend; exposure and contingent-liability schedule; bundles, folders and evidence; team tasks and waiting items.
- Individual "My cases" with plain-language explainer, legal-aid signposting and professional hand-off; alerts; bulk import; reports and board/audit-committee MIS.
- ADR referral through the P19 route panel (Equator as one provider) and read-only Recovery Suite projections (Ecosystem Spec §6.10, entity #24).

**Out of scope (owner phase)**
- Drafting pleadings, notices, replies, vakalatnamas and annexure indices — P10 (`pld`). P11 links to them and opens the drafting studio in context.
- Dispatch and proof of service of notices — P10 (with `ntf`).
- Hiring, paying and reviewing marketplace professionals — P16. P11 consumes engagements.
- Recovery litigation (SARFAESI, DRT original applications as lender, s.138 as lender, IBC as financial creditor, recovery-linked arbitration) — Finbyx/Udofin Recovery Suite (system of record). LawDocs shows projections only.
- ADR adjudication, neutral appointment and awards — Equator Resolution.
- Regulator inspections, RFIs, observations and MAP items — LawDocsComply (compliance system of record, D-10). LawDocs records regulatory **proceedings** (show-cause, adjudication, appeal) as matters.
- E-filing, court-fee payment, appearance — done by the advocate or party-in-person outside LawDocs (NN-05, NN-13, NN-41).
- Consumer-help grievance desks (pre-forum complaints to banks, insurers, ombudsmen) — P15; a grievance that becomes a consumer-commission case creates a P11 case.
- Board-pack assembly and listed-company disclosure workflow — P13 (P11 supplies MIS and flags).

## Phase P12 — IP and Trademark Portfolio

**File:** `phases/P12_IP_and_Trademark_Portfolio.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (Legal Vault, bulk intake, legal hold), P05 (OCR and extraction of examination reports, Journal pages and registry e-mails), P06 (templates: assignment, licence, co-existence, user affidavit), P07 (CLM for IP licences and assignments; obligations), P08 (stamp-before-sign and eSign for IP deeds), P09 runtime (`AGT_TM_WATCH`), P11 (oppositions, rectifications, infringement and appeals as matters; deadline engine; frozen `lit` read API), P14 (Startup Desk bundles), P16 (marketplace filing and opinion SKUs delivered by trade marks agents and advocates), P17 (plan limits, add-on `LD-ADD-TMW`, AI credits), P19 (`TRADEMARK_DATA_PORT` adapters, IP mailbox), P20 (export map). External: WIPO Global Brand Database (terms [VERIFY]), a licensed trademark data and Journal-watch partner (not yet selected [VERIFY]).
> **Sequencing:** Wave 2, after P11 sprint 2 (deadline engine and matter API frozen). Sprint 1–2: asset model, trademark register, status taxonomy, deadline rules, manual and assisted refresh. Sprint 3–4: clearance assistance, filing-support service hand-off, examination and hearing workflow, renewals. Sprint 5: Journal watch (partner or manual upload), copyright/design/patent/domain registers. Sprint 6: licences and assignments, reports, mobile, hardening.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), D (roles), H (agent roster), K (export taxonomy), M (marketplace professional rules), R (settings), T (intake categories and SLAs for IP requests), W (verification log and open items).
> **Requirements covered:** R-013, R-017, R-019, R-021, R-027, R-030, R-037, R-061, R-075, R-082, R-086.
> **Decisions applied:** D-05, D-10, D-11, D-14, D-15, D-17 · **Challenges applied:** CH-08, CH-09, CH-14, CH-27 · **Non-negotiables tested:** NN-01, NN-02, NN-05, NN-08, NN-09, NN-11, NN-13, NN-14, NN-20, NN-21, NN-22, NN-29, NN-30, NN-38, NN-39, NN-43, NN-46
> **Estimated effort:** 6 two-week sprints, squad of 8 (backend 3, frontend 2, data/ML 1 for similarity, QA 1, integration 1) plus a part-time IP domain analyst (advocate or registered trade marks agent).

### Objective and business outcome

Startups and SMEs file trademarks through aggregators and then lose track: the examination report goes to the agent's address for service, the one-month reply window (Trade Marks Rules 2017 r.33(4)) passes, the application is abandoned, or the ten-year renewal is missed. IP India offers status lookups behind an OTP, a weekly Journal and e-filing, but no portfolio view, alerts or similarity watch (R1 §7.1). Nobody combines **portfolio tracking + deadline engine + Journal watch + reply drafting + professional filing** for an SME at a low price (R1 key finding 8).

This phase builds that portfolio for companies and individuals (sole proprietors, founders, creators), centred on trademarks with lighter registers for copyrights, designs, patents and domain names, and links IP disputes to P11 and IP agreements to P06/P07.

| Outcome | KPI and exit-gate measure |
|---|---|
| No lost application or registration | Every asset has a normalised status, last-refreshed time and a computed next deadline; 0 missed deadlines in UAT; renewal tasks created ≥ 12 months before expiry |
| Honest status | Every status shows its source (user, agent, assisted refresh, licensed partner, WIPO route) and staleness; no "live", "official" or "real-time" wording (NN-20) |
| Faster filing | From "I want to protect my brand" to a filing-ready TM-A data sheet handed to an agent in ≤ 15 minutes and ≤ 8 screens |
| Watch that matters | Journal hits reviewed with ≥ 30 days left in the 4-month opposition window for 95% of hits in pilot |
| Clean boundaries | LawDocs never files with IP India, never handles the eRegister OTP and never automates the IP India portal (NN-05, NN-13) |

### Scope (in / out)

**In scope**
- IP asset model (`tmk_`, business ID `LD-TMK-YYYY-NNNNNN`) for trademarks, copyrights, designs, patents and domain names; optional confidential-information register.
- Trademark register: marks, Nice classes, applicants, application numbers, filing dates, priority and use claims, status lifecycle, Journal details, registration and renewals.
- Deadline rule pack for trademarks (and lighter rules for other assets) with verification flags.
- Status refresh through `TRADEMARK_DATA_PORT`: user-entered numbers, assisted refresh, WIPO Global Brand Database route (if licensed), licensed partner.
- Search and clearance assistance (Vidhi): Nice class finder, knock-out screening, absolute/relative-ground explainers.
- Filing-support service through the marketplace: TM-A data sheet, documents, hand-off to an authorised agent or advocate, recording of the filing.
- Examination report, reply and show-cause hearing workflow.
- TM Journal watch (partner or manual upload) with similarity scoring and review queue.
- Oppositions, rectification, cancellation, infringement and passing-off as P11 matters.
- Licences, assignments and recordals (link P06/P07/P08).
- Renewal reminders, use-evidence locker, portfolio valuation notes, startup bundles, dashboards and reports.

**Out of scope (owner phase)**
- Filing, replying or attending hearings before the Registry — done by the authorised agent or advocate from their own account (NN-13, NN-41). LawDocs prepares and records.
- Legal opinions on registrability or infringement — marketplace professionals (P16).
- Litigation management — P11.
- Contract drafting and negotiation — P06/P07.
- Statutory valuation reports — registered valuers via P16.
- Geographical indications, plant varieties, semiconductor layouts — not in v1 (tenant may record as "Other IP" with manual dates).
- Foreign national filings other than recording the status and dates of Madrid designations and foreign registrations entered by the user.

## Phase P13 — Company Legal Department OS, Governance and HRMS

**File:** `phases/P13_Company_Legal_Department_OS_Governance_and_HRMS.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (identity, KYB, director/KMP identity attributes), P02 (organisations, legal entities, departments, positions, user types, maker-checker, delegations), P03 (Configuration Studio, settings registry, `RULES_PORT`), P04 (Legal Vault, retention, legal hold), P06 (templates: resolutions, notices, minutes skeletons, appointment letters, policies), P07 (CLM approvals, obligations, renewal dates), P08 (eSign/DSC for minutes, registers, declarations, appointment letters), P09 (Vidhi runtime and agents), P11 (matters, clocks, spend, counsel panel; frozen `lit` read API), P12 (IP calendar), P16 (marketplace professionals and retainers), P17 (plans and entitlements), P18 (Delivery Console; RM as maker), P19 (LawDocsComply connectors, workplace and company-data adapters), P20 (export), P22 (mobile). Shared kernels (used, never forked — NN-47): `@infrabyx/governance-kernel`, `@infrabyx/hrms-kernel`, `infrabyx-labour-rulepack`, `@infrabyx/docgen`, `@infrabyx/redline`. External: LawDocsComply (when the tenant uses it), licensed MCA-data vendors, Microsoft 365 / Google Workspace, e-voting agencies (file hand-off).
> **Sequencing:** Wave 2, after P11 sprint 2. Track A (`lgo`, sprints 1–3): intake desk, SLAs, CLO dashboard, legal calendar, DoA matrix. Track B (`gov` mount, sprints 2–6): mode resolver, company-type configuration, board and committees, meetings, minutes, resolutions, registers, directors and KMP, duties. Track C (`hr` mount, sprints 5–8): people, positions, departments, leave, payroll via the labour rule pack, documents, acknowledgements, POSH. Sprints 9–10: finance-company templates (Appendix T), agents, LDC SoR sync certification, mobile, hardening. Freeze the kernel versions at sprint 2 and record them in `docs/kernels.lock`.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), D (roles), H (agent roster), K (export), R (settings), T (legal-department operating model and finance-company structure — companion to this phase), W (open items), X (Operations Hub addendum — boundary for staff HR), Y (Ecosystem Spec change requests).
> **Requirements covered:** R-002, R-018, R-019, R-021, R-026, R-027, R-028, R-030, R-047, R-053, R-055, R-059, R-060, R-064, R-067, R-068.
> **Decisions applied:** D-02, D-10, D-15, D-17 · **Challenges applied:** CH-14, CH-24, CH-26, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-09, NN-11, NN-13, NN-14, NN-17, NN-18, NN-19, NN-24, NN-26, NN-28, NN-29, NN-30, NN-32, NN-33, NN-38, NN-12, NN-40, NN-43, NN-45, NN-47
> **Estimated effort:** 10 two-week sprints, squad of 8 (backend 4, frontend 2, QA 1, integration 1) plus a part-time Company Secretary (secretarial domain), an HR/labour analyst and a counsel reviewer for the operating model.

### Objective and business outcome

The owner wants companies to run their legal work "with one CLO" (brief l.68) and to manage people, KMPs, directors, duties and departmental structures, including finance-company structures aligned with the Companies Act 2013 and RBI directions (brief l.67). This phase delivers the **Company Legal Department OS**:

1. **Legal team in a box** — positioned per D-17 and CH-14 as **legal operations + AI + on-demand professionals**. LawDocs gives the company the operating system of a legal department (intake, triage, SLAs, calendar, records, drafting, spend, dashboards). Advice and representation come from advocates engaged in their own name (Advocates Act 1961 ss.29, 33; R3 LG-110). A company with one CLO, or a CS or compliance head acting as legal lead, can run its legal function on LawDocs; it still needs advocates for court work and opinions, and the product says so.
2. **Governance kernel mount** — board, committees, meetings, minutes, resolutions, registers, directors and KMP, duties — mounted locally for LawDocs-only companies and served from LawDocsComply (system of record) when the company also uses LDC (D-10, NN-47).
3. **HRMS kernel mount for client companies** — people, positions, KMP designations, departments, duties, leave, payroll through the shared labour rule pack, onboarding and exit documents, policy acknowledgements, POSH Internal Committee records — again local or LDC-served.
4. **Departmental structure templates**, including the customisable finance-company (NBFC) structure in Appendix T.

| Outcome | KPI / exit-gate measure |
|---|---|
| Every legal request has an owner and a clock | 100% of intake requests triaged within the category SLA in pilot; first-response SLA met ≥ 95% |
| Self-service where safe | ≥ 30% of standard requests (e.g., NDA on the company template) closed by guided self-service with no lawyer time, within guardrails |
| One legal calendar | Contracts, cases, trademarks, licences, board and HR statutory dates in one calendar; 0 missed statutory dates in UAT |
| Board work faster | Notice + agenda + pack issued in ≤ 6 steps; minutes draft circulated within 3 working days of the meeting in pilot; 0 edits to sealed minutes (SS-1 bar on altering entered minutes [VERIFY para]; tampering is an offence under s.118(12)) |
| No double entry with LDC | When LDC is SoR, 0 governance or HR rows written locally; governance and HR work happens in LDC; LawDocs reads governance facts on demand; switch reconciliation 100% |
| Structure in minutes | A new NBFC tenant adopts the Appendix T template (departments, committees, KMP, three lines of defence) in ≤ 15 minutes and customises it without Super Admin (NN-29) |
| Proportionate HR | Attendance and work measurement disclosed and outcome-based; 0 surveillance features (NN-33) |

### Scope (in / out)

**In scope**
- Operating-model setup wizard (company type, size, sector → Appendix T template).
- Legal intake desk for all departments; categories, dynamic forms, triage, routing, SLAs, self-service, conversions, satisfaction.
- CLO dashboard, legal calendar, legal risk dashboard for KMPs and the board.
- Licences and registrations register (light; LDC owns it when present).
- Legal spend view across matters, retainers and marketplace orders; counsel panel (from P11).
- Delegation-of-authority (DoA) matrix for legal actions.
- Governance kernel mount: company-type configuration, board and committees, meetings (notice, agenda, papers, attendance incl. video, quorum, minutes per SS-1/SS-2, resolutions incl. circular resolutions, action items), statutory registers, directors/KMP profiles (DIN, KYC status, interests under s.184, disclosures), duties and task assignment.
- Finance-company (NBFC) governance overlay through the shared kernel rule pack, aligned with the RBI consolidated Directions of 28 November 2025 (verified titles only).
- HRMS kernel mount: people, employments, positions, KMP designation, department allocation, duties, leave, attendance (proportionate), payroll via `infrabyx-labour-rulepack`, onboarding and exit documents, policy acknowledgements, POSH IC records (sealed).
- LDC system-of-record synchronisation through contracts.
- Board/KMP AI agent hooks (from P09).
- Retainer delivery with the LawDocs RM as delegated maker (R-064).

**Out of scope (owner)**
- Infrabyx's own staff HRMS, payroll, appraisal and staff CRM — Operations Hub (D-02; Appendix X).
- Compliance management, regulatory returns, RBI/SEBI checkpoint libraries, inspections — LawDocsComply (D-10). LawDocs shows LDC tasks in the legal calendar when linked.
- ROC/MCA e-filing, e-voting execution, filing of labour returns — done by the company or its professional on the official portals (NN-05, NN-13). LawDocs prepares data sheets and records filings.
- Listed-company disclosure engine (LODR Reg 30 workflows, PIT, SAST) in depth — LDC; LawDocs-only listed companies get a basic disclosure case and are advised to use LDC [REC].
- Litigation, IP, CLM detail — P11, P12, P07.
- Payment of salaries — the company's bank; LawDocs exports bank files and never holds funds (NN-22).

## Phase P14 — Business Services: Start a Business, Compliance Services and Tax

**File:** `phases/P14_Business_Services_Start_a_Business_Compliance_and_Tax.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P16 (marketplace catalogue, offering object, engagement lifecycle, professional registry, Rule 36 directory, buyer platform fee), P17 (`BILLING_PORT`, OH8 SKUs and streams, entitlements, GST invoice mirror, refunds), P04 (vault folders, document checklists, retention, legal hold), P06 (templates and questionnaires: founders' agreement, SHA, SSA, term sheet, ESOP plan, partnership deed, trust deed, MoA/AoA), P07 (deal rooms, obligations `obl_`), P08 (eSign, DSC, eStamp, instrument eligibility gate), P10 (notice replies), P11 (tax litigation matters), P13 (governance kernel mount, compliance calendar for LawDocs-only tenants, HRMS/payroll kernel), P18 (Delivery Console, delivery grants, RM-as-maker), P19 (`int`: LDC contracts, GSP/ERI/KYB adapters), P03 (settings, rule engine, effective-dated tax-year rule packs). External: Operations Hub OH8 (catalogue, prices, invoices, Razorpay) and OH9 (professional directory); MCA V3, IP India, FoSCoS, DGFT, Udyam, State portals (user- or practitioner-operated only); a licensed GSP; LawDocs' own ERI registration (Type 2) [VERIFY]; KYB vendor (R6 D-15).
> **Sequencing:** Wave 3. Sprint 1 freezes the service-definition schema (§4A) and fee-line model (§4F) so that P21 content can bind service pages to `svc_` codes. Catalogue seeding (§4B–§4C) and Startup Desk (§4J) run in parallel with the tax workspace (§4K–§4N). ERI and GSP adapters ship behind flags (NN-38) until registrations and contracts are verified. Attest services (statutory, tax and secretarial audit) ship in BYO-professional mode only (§4G).
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), D (roles and access matrix), F (instrument eligibility gate), H (agent roster), K (`LD-EXPORT-1.0`), M (marketplace and professional rules), R (settings registry), W (verification log and open items), X (Operations Hub additions), Y (Ecosystem Spec v1.2 change request).
> **Requirements covered:** R-014, R-036, R-037, R-038, R-039, R-040, R-047, R-063, R-064, R-069, R-075, R-080, R-082, R-086, R-087, R-090.
> **Decisions applied:** D-02, D-05, D-10, D-11, D-12, D-17 · **Challenges applied:** CH-06, CH-07, CH-08, CH-09, CH-10, CH-12, CH-13, CH-16, CH-19, CH-25 · **Non-negotiables tested:** NN-01, NN-05, NN-07, NN-08, NN-11, NN-13, NN-14, NN-16, NN-17, NN-18, NN-20, NN-21, NN-22, NN-29, NN-30, NN-38, NN-40, NN-41, NN-45, NN-46, NN-47, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, frontend 2, tax/rules analyst 1, QA 1, CS/CA content reviewer 1).

### Objective and business outcome

LawDocs sells the owner's **Start a Business** catalogue (26 services) and **Compliance** catalogue (22 services) as **productised services**. A founder, SME or individual can see what a service needs, what it costs line by line, who may lawfully perform it, how long LawDocs takes and how long the government takes, and can then buy it with or without a subscription (R-040, D-11). Every document collected and every certificate received lands in the Legal Vault and drives renewal reminders, so the customer has a reason to keep LawDocs (R-011). The **Startup Desk** packages incorporation, founder documents, funding readiness and a "virtual legal officer" retainer (R-082). The **Tax workspace** gives individuals, companies and LLPs one place for returns, TDS, GST, professional tax, advance-tax calendars and tax notices (R-069), without anyone sharing a portal password (CH-10).

**Why it matters.** Commodity filings have settled at ₹1,499–₹2,999 + GST + government fees (R6 B-06–B-15). LawDocs wins on (i) a free guided start and free AI-drafted first documents, (ii) the vault and renewal engine, (iii) honest fee breakdowns (IMP-075) and (iv) live order tracking (IMP-080).

| Outcome | Exit-gate measure |
|---|---|
| Productised catalogue | 48 services seeded as `svc_` definitions, each with questionnaire, document checklist, fee lines, lawful-performer rule, SLA, deliverables and renewal rule; every definition has a reviewer of record (NN-30) |
| Buy without subscription | A non-subscriber orders a fixed-price service in ≤ 7 taps from the service page (buyer account, eligibility answers, fee review, checkout) |
| Fee honesty | 100% of orders show government fee, stamp duty, third-party costs, professional fee, LawDocs fee and GST per supplier as separate lines before payment; zero drip-pricing defects in the NN-50 test suite |
| Lawful delivery | 0 orders assigned to a performer who lacks the credential the service's rule requires (CI test `NN-41_performer_credential_gate`) |
| Tracking | Every order shows the current milestone, "Waiting on" owner and next date; customer status updates by in-app, email and opted-in WhatsApp within 15 minutes of a milestone change |
| Renewals | Every certificate with an expiry or periodic duty creates an obligation with T-60/T-30/T-7 reminders |
| Tax without passwords | ITR filing via the ERI route reaches "Awaiting taxpayer e-verification" without LawDocs ever receiving an OTP, DSC PIN or e-filing password |
| KPIs (post-launch) | Order-to-inputs-complete median ≤ 3 days; LawDocs SLA attainment ≥ 95%; rework rate ≤ 3%; refund-dispute rate ≤ 1%; renewal capture ≥ 40% |

### Scope (in / out)

**In scope**
- `bsv` module: service definitions (catalogue data), service orders, intake, eligibility questionnaires, document checklists, fee lines, practitioner assignment, milestone tracker, deliverables, renewals and the Startup Desk.
- `tax` module: tax profiles (individual, HUF [VERIFY scope], company, LLP, firm), tax-year rule packs, ITR via ERI, GST returns via GSP and GST practitioners, TDS returns, professional tax, advance-tax calendar, tax-notice intake and response, tax computation drafts, tax document checklists.
- Binding of the 48 service pages (`/start-a-business/*`, `/compliance/*`; R5 §8.3–§8.4) to `svc_` codes for the order widget, the "Draft with AI free" block and the "Hire a professional" block (R-087). Page copy is P21.
- Correction of outdated law in service definitions (R5 §5): Udyam not Udyog Aadhaar; GSTR-1/1A/3B/2B and IMS, not GSTR-2/3; GST audit re-scoped to GSTR-9/9C; Income-tax Act 2025 and "tax year"; Labour Codes for PF/ESI/payroll; hallmarking dates; Nidhi 2022 amendment; OPC 2021 liberalisation.

**Out of scope (owner phase)**
- Marketplace mechanics, professional onboarding, Rule 36 directory, buyer platform fee and Route payouts — P16. P14 consumes them.
- Plans, GST invoices, credit notes and revenue-stream switches — P17 and OH8.
- Compliance calendars, obligation registers and regulatory returns for regulated entities — **LawDocsComply is system of record** when the tenant uses LDC (D-10, NN-47); otherwise the P13 governance kernel mount. P14 only sells and fulfils services against those obligations.
- Client payroll engine — P13 HRMS kernel via `infrabyx-labour-rulepack`. P14 sells the "payroll maintenance" service that runs on it.
- LawDocs' own staff payroll, CRM and billing engine — Operations Hub (D-02).
- Trademark portfolio tracking after filing — P12 (P14 hands the application number to `ipm`).
- Tax litigation after an appeal is filed — P11. Notice drafting studio — P10.
- Consumer grievances — P15.

## Phase P15 — Consumer Help: Loan/Insurance Grievances, Challans and Vehicles

**File:** `phases/P15_Consumer_Help_Grievances_Challans_and_Vehicles.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (vault, evidence folders, Object Lock, legal hold), P05 (OCR, screenshot and handwriting type copies, translation, call-recording transcripts), P10 (letters, complaints and notices drafting studio), P16 (Rule 36 advocate directory, fixed-fee engagements, buyer platform fee, Route payouts), P06 (vehicle sale agreement, delivery note, authority letters), P07 (deal rooms, messaging), P08 (eSign, eStamp, eligibility gate, evidence pack, BSA s.63 certificate), P17 (separate selling entity, Razorpay merchant, stream switches RS-LD-39/40), P18 (Delivery Console in the Consumer Help entity scope), P19 (`int`; conflict-check client), P01 (DigiLocker pulls of RC/DL [VERIFY issuer availability]), P03 (rule engine, effective-dated rule data). External: Operations Hub conflict service (extension of OH1.6; Appendix X), OH8 (Consumer Help selling entity), official portals by deep link only (cms.rbi.org.in, sachet.rbi.org.in, Bima Bharosa, cioins.co.in, e-Jagriti, NCH 1915, echallan.parivahan.gov.in, vcourts.gov.in, vahan.parivahan.gov.in, State traffic Lok Adalat pages).
> **Sequencing:** Wave 3. Sprint 1 builds the brand/entity profile, ethical wall and conflict check; nothing else ships until the wall tests pass. Vertical A (loans) and the challan/vehicle verticals run in parallel from sprint 2; Vertical B (insurance) from sprint 4. Success-fee code ships dark (RS-LD-40 OFF). Rules data (Appendix S) is loaded and verified per row before the related screen leaves advisory mode (NN-38).
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), S (Consumer Help Rules and Playbooks), D (roles), F (instrument eligibility gate), K (`LD-EXPORT-1.0`), M (marketplace professional rules), R (settings), W (verification log), X (Operations Hub additions), Y (Ecosystem Spec v1.2 change request).
> **Requirements covered:** R-002, R-011, R-044, R-047, R-061, R-063, R-083, R-084, R-085, R-086, R-087, R-088.
> **Decisions applied:** D-05, D-06, D-11, D-12, D-13 · **Challenges applied:** CH-05, CH-08, CH-12, CH-13, CH-16, CH-20, CH-22, CH-23, CH-25, CH-28, CH-30, CH-31 · **Non-negotiables tested:** NN-01, NN-04, NN-05, NN-07, NN-08, NN-09, NN-10, NN-13, NN-14, NN-16, NN-17, NN-19, NN-20, NN-21, NN-22, NN-23, NN-24, NN-26, NN-34, NN-35, NN-38, NN-39, NN-40, NN-45, NN-46, NN-49, NN-50
> **Estimated effort:** 9 two-week sprints, squad of 8 (backend 3, frontend 2, rules/legal-ops analyst 1, QA 1, security engineer 0.5, content 0.5).

### Objective and business outcome

Indian consumers who face recovery-agent harassment, unfair loan charges, a wrong credit report, a rejected insurance claim, a traffic challan or a used-vehicle sale usually do not know which forum to approach, by when, or with what evidence. Competitors either "take everything over" for a success fee (FREED, Insurance Samadhan) or collect fines through their own accounts (Park+) (R2 §1(a), §2(a), §3(a)). `[Consumer Help Brand]` is the **documented, user-controlled** alternative: it tells the user the right forum and deadline, captures evidence that will stand up, drafts the letters, tracks every clock, and adds a human case manager or an advocate only where the forum allows it (R2 §0).

The brand runs on the LawDocs platform but under its **own brand and legal-entity profile** with an ethical wall from the group's lender-facing products (D-06, NN-23). Finbyx, Udofin and LawDocsComply serve lenders. Consumer Help sometimes acts against lenders. The two must never share data, staff or incentives.

| Outcome | Exit-gate measure |
|---|---|
| Separate brand and entity | Brand, domain, legal entity, GSTIN, Razorpay merchant, privacy notice, grievance officer and staff group configured independently; wall tests (§12) pass |
| Right forum, right time | Triage returns a forum, eligibility result and computed deadline for 100% of seeded scenarios in Appendix S, each tied to a verified rule row or shown as advisory |
| Evidence that survives | Every evidence item hashed at capture, time-stamped, with a typed copy for screenshots and a BSA 2023 s.63 certificate draft on export (NN-10) |
| User control | User signs and files wherever the forum expects the complainant; every authority letter is scoped, time-bound and revocable in-app |
| No money handling | LawDocs never receives fines, dues, settlement amounts or vehicle prices (NN-22, NN-23); CI test proves no payment intent can name a government or lender beneficiary |
| No outcome promises | Banned-phrase lint blocks "waiver", "guaranteed", "stop EMIs", "100% success" across site, app, templates and AI output (NN-20) |
| KPIs (post-launch) | First draft letter ≤ 24 h from intake; 0 missed statutory windows on managed cases; median days per stage by forum published internally; refund-dispute rate ≤ 1%; NPS by vertical |

### Scope (in / out)

**In scope**
- `chp` module: brand and entity profile, ethical wall, conflict checks, issue-first intake, case workspace (`grv_`, `LD-GRV-…`), evidence locker, escalation ladders, deadline engine, authority letters and consents, case-manager workflow, advocate path, fee models, outcome reporting.
- Verticals: **A** loans and lending (recovery harassment, unfair charges, KFS/APR issues, digital-loan-app complaints, settlement and closure, NOC and document release); **A2** credit-report disputes (CIC); **B** insurance (claim rejection, delay, short settlement, mis-selling); **C** traffic challans (lookup by deep link, pay on official portal, Lok Adalat, Virtual Court, advocate to contest, reminders); **D** vehicles (pre-sale checks, sale agreement and delivery note, RC transfer checklist, hypothecation removal, foreclosure letters, deal room, eSign, vehicle documents in vault).
- Consumer commission complaints through e-Jagriti and the National Consumer Helpline as escalation steps for A and B.

**Out of scope (owner phase)**
- Drafting engine, templates and court formats — P10/P06 (P15 supplies the templates' data and triggers).
- Advocate directory and engagement mechanics — P16.
- Litigation after a court case is filed — P11 (P15 opens the matter and hands over).
- Debt-settlement programmes, savings corpus, "loan waiver" products, lender lead generation, insurance selling or comparison — **excluded by design** (R2 §1(d), §2(e) B1; RBI cautions of 11 Dec 2023 and 4 May 2026).
- Bulk or fleet challan APIs — excluded until a lawful source is verified (R2 §3(b)); fleet subscription is OI-P15-04.
- Escrow of vehicle sale price — excluded unless a licensed bank or escrow partner is engaged (R2 §4(e) D3; OI-P15-05).

## Phase P16 — Marketplace, Professional Registry, Retainers and FinLegal Academy

**File:** `phases/P16_Marketplace_Professional_Registry_Retainers_and_Academy.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (identity, KYC/KYB, professional credential verification, consent artefacts), P02 (tenancy, Personal and Company workspaces, maker-checker), P03 (settings registry, rule engine), P04 (Legal Vault — deliverables, engagement records), P07 (negotiation and redlines for engagement letters, SOWs and SLA schedules), P08 (eSign of engagement letters and SLAs; instrument eligibility gate), P09 runtime (Vidhi), P17 (`BILLING_PORT`, price cards, checkout, invoices, credits, stream registry), P18 (Delivery Console, delivery grants, RM-as-maker), P19 core (`int`, OH8/OH9 adapters, Academy feed connector), P20 core (`xpt.export_map`), P21 core (public-site shell, SEO, help keys). External: Operations Hub **OH8** (catalogue, quotes, orders, GST invoices, credit notes, Razorpay incl. Route), **OH9** (group professional directory and credential verification), **OH3** (consented leads), **OH6** (complaints about LawDocs services), **OH14** (claims gate); LawDocsComply (group listings, D-11); FinLegal Academy (trainings.lawdocs.in, Graphy-hosted per R5 §1.3).
> **Sequencing:** Starts after P17 sprint 3 (price-card, quote and checkout components frozen). Ship order: (1) public storefront + first-party LawDocs services (Model M1) + Academy listing; (2) retainers and SLA engine; (3) LawDocs Panel advocates' firm under Model M2 once OI-P16-01 and OI-P16-02 close; (4) third-party professionals behind per-profession switches that stay OFF until counsel opinion + checker approval (NN-21). Freeze point: profession render allow-lists (`RULE36_V1`, `PRO_SERVICE_V1`) and the `mkp.engagements` state machine are frozen at the end of sprint 4 because P15 (Consumer Help) and P14 (Business Services) consume them.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), M (Marketplace Services Catalogue and Professional Rules), L (Pricing, Plans, Revenue-Stream Registry and Savings Model — streams RS-LD-19…RS-LD-33), D (roles), F (instrument eligibility gate), K (`LD-EXPORT-1.0`), R (settings registry), W (open items), X (Operations Hub additions), Y (Ecosystem Spec v1.2 change request).
> **Requirements covered:** R-014, R-016, R-021, R-030, R-037, R-038, R-039, R-040, R-041, R-047, R-064, R-075, R-080, R-081, R-082, R-084 (advocate to contest a court-referred challan, listing only), R-086, R-087, R-088.
> **Decisions applied:** D-02, D-05, D-06, D-10, D-11, D-12, D-15, D-16, D-17 · **Challenges applied:** CH-08, CH-09, CH-14, CH-20, CH-22, CH-25, CH-31 · **Non-negotiables tested:** NN-01, NN-11, NN-13, NN-14, NN-17, NN-18, NN-19, NN-20, NN-21, NN-22, NN-23, NN-24, NN-35, NN-39, NN-41, NN-45, NN-46, NN-49, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, frontend 2 — public + delivery, mobile 0.5 shared with P22, integration 1 — OH8/OH9/Route/Academy, QA 1, legal-ops analyst 0.5)

### Objective and business outcome

LawDocs sells human expertise that software cannot replace — drafting, review, notices, policies, annual reports, minutes and board support, compliance testing, risk assessment, stress testing and scenario analysis, retainer advisory, filings and returns, startup bundles, trademark work, litigation support — **with or without a SaaS plan** (R-040). The marketplace is the single group storefront at `lawdocs.in/marketplace` (D-11) for LawDocs services, LawDocsComply services and FinLegal Academy courses. It is public and browsable without login (R-041).

It must beat LegalKart on the points where LegalKart is weak (R1 §1, §3.4–3.5): no per-minute ranked advocates, no non-refundable short-expiry wallet, real verification instead of "does not separately verify", landed prices instead of "starting at", SLA-backed delivery instead of "lawyer stopped responding". It must also stay lawful where every lawyer directory is exposed: BCI Rule 36, the Madras High Court judgment of 3 July 2024 and the ICAI aggregator bar (R3 LG-111–LG-117).

**Design in one line.** Fixed-scope, landed-price **service products** sold by LawDocs, fulfilled by professionals that LawDocs assigns (LawDocs team first, a contracted advocates' panel next, third parties later), with a separate, disclosed **buyer-side platform fee** where a regulated professional supplies the work, Razorpay Route for any money that belongs to a professional, and no listing fee, commission, ranking or rating for advocates (D-05, NN-21, NN-22).

| Outcome | Exit-gate measure |
|---|---|
| Public storefront | `/marketplace` serves ≥ 80 seeded LIVE service products in the 18 categories of Appendix M §M.2, server-rendered, indexable, WCAG 2.2 AA; browse, search, filter and read price cards with no login and no cookie wall |
| Services without a plan | A visitor with no account buys a fixed-price service in ≤ 7 taps on mobile / ≤ 8 clicks on web from the service page, including OTP sign-up (Appendix C J-28) (OTP sign-up → GST profile only if business → Razorpay hosted checkout); GST tax invoice e-mailed by OH8 within 15 minutes of capture |
| Landed price | 100% of LIVE price cards show professional/service fee, LawDocs platform fee (where applicable), government/statutory fee estimate with basis, GST, **total payable now**, exclusions, refund rule and SLA (NN-22, NN-50); lint blocks any card without them |
| Professional-conduct compliance | CI proves restricted fields (ratings, fees per advocate, photos, badges, "top", "book this lawyer") cannot render for advocates; per-profession switches for commission, listing, ratings and percentage fees are locked OFF without a counsel-opinion reference and a checker (NN-21) |
| Retainers | A retainer moves from proposal to eSigned SLA schedule to active RM-as-maker grant in ≤ 2 working days; hour bank, SLA attainment and monthly report visible to the client in real time |
| Delivery quality | ≥ 90% of milestones delivered within SLA in the pilot cohort; auto-refund on professional no-show within 2 hours (R1 IMP-009) |
| Money safety | 0 rupees of professional fees held in a LawDocs account; every professional payout is a Route transfer with an idempotency key reconciled daily (NN-22, NN-46) |
| Academy | Course catalogue from trainings.lawdocs.in synced daily; stale-feed fallback works; no paid course content copied (D-16) |
| Portability | Every engagement, retainer, deliverable, SLA report and invoice reference appears in `LD-EXPORT-1.0` under `09 Services and Engagements/` (company) or the individual mapping in §13 (NN-11) |

---

### Scope (in / out)

**In scope**

- Public storefront in `apps/public` (`/marketplace/*`), in-app "Services" menu in `apps/web` (Personal and Company workspaces), service drawer in `apps/mobile`, delivery and practitioner workspace in `apps/delivery`, administration in `apps/console`.
- Catalogue: categories, service products (`svc_`), packages, add-ons, price models, landed price cards, inputs checklists, deliverables, SLAs, exclusions, eligibility rules, seller of record (LawDocs or LawDocsComply entity), Academy courses.
- Customised offers and quotes (`ofr_`) for bespoke scope, retainers and enterprise work.
- Professional registry (`pro_`): LawDocs in-house professionals, the LawDocs Panel (contracted advocates' firm and individual panel advocates), third-party professionals and firms; onboarding through P01 verification and OH9 credentials; per-profession commercial switches.
- Assignment engine and conflict checks.
- Engagement lifecycle (`eng_`): request → scoping → offer → engagement letter/SOW eSign (P08) → payment → inputs → delivery by milestone → deliverables into the client's vault → acceptance → close; change requests (`ecr_`); cancellations; disputes.
- Retainers (`rtn_`): customised scope, service basket, hour bank, SLA schedule (`sla_`) eSigned in-tool, milestones, monthly reports, renewals, RM-as-maker activation via P18 delivery grants (R-064).
- Practitioner workspace for professionals in `apps/delivery` (queue, engagement room, time entries, deliverable upload, payouts view).
- Reviews of LawDocs services only (NN-49), private professional feedback, quality sampling.
- Grievance officer, disputes, refunds (via OH8 credit notes and Route reversals).
- Route split settlement instructions through OH8 (NN-22); invoice and tax presentation per model.
- FinLegal Academy listing via catalogue feed and deep link; corporate seat bundles; consented certificate import (D-16).
- LawDocsComply services listed on the same storefront (D-11) and Consumer Help services under the separate `[Consumer Help Brand]` (D-06, NN-23).

**Out of scope (owner phase)**

- Price books, tax computation, invoices, Razorpay accounts and Route configuration — OH8 via `BILLING_PORT` (P17).
- Group professional directory credential master — OH9 (consumed, never rebuilt).
- Delivery inside client tenants, delivery grants, credential vault, RM portfolio — P18 (`sdc`, `cvl`).
- Consumer Help case workflows (grievances, challans, vehicles) — P15; this phase lists them and supplies the commerce rails.
- Business-service order workflows (incorporation, registrations, tax returns via ERI/GSP) — P14; this phase lists them and supplies engagement records.
- LMS, course delivery, assessments — FinLegal Academy (Graphy) remains system of record.
- Mediation and arbitration — Equator (a referral link only, OFF by default, §4M).
- Ranked advocate directory — not built; an optional Rule-36-only directory page exists behind a flag that is OFF (NN-21; R3 LG-113).

---

## Phase P17 — Plans, Subscriptions, Billing, GST, Revenue-Stream Switches and Savings Dashboard

**File:** `phases/P17_Plans_Subscriptions_Billing_Revenue_Streams_and_Savings.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P02 (tenancy, Personal/Company workspaces, maker-checker), P03 (settings registry, Configuration Studio, rules), P19 core (`int` gateway, OH8 adapter, signed-artefact verification), P20 core (`xpt.export_map`), P21 core (public-site shell for `/pricing`); P01 for sign-up and GST/PAN profile fetch. External: Operations Hub **OH8** (catalogue, price books, coupons, stream gates, quotes, orders, subscriptions, signed entitlements, GST invoices, credit notes, receipts, Razorpay hosted checkout, Subscriptions, e-mandates, Smart Collect, Route, dunning, revenue accounting — Ecosystem Spec §6.27; OH Master Prompt OH8.1–OH8.10), **OH14** (claims gate), **OH3** (consented leads), **OH6** (billing disputes).
> **Sequencing:** Wave 1. Sprints 1–3 build `BILLING_PORT`, the presentation catalogue, entitlement mirror and checkout (frozen at end of sprint 3 for P16). Sprints 4–5: credits, meters, Settings → Billing & Membership, dunning. Sprints 6–7: revenue-stream registry UI, Pricing Studio, Savings & Value. If OH8 is not live at sprint 3, the interim `LOCAL` adapter (§4L) ships behind an owner decision (OI-P17-01). Every producing module (sgn, ai, lit, ipm, dms, ntf, int, mkp) registers its meters by its own phase exit.
> **Binding appendices:** L (Pricing, Plans, Revenue-Stream Registry and Savings Model), M (marketplace fees, for buyer-fee lines), K (`LD-EXPORT-1.0`), R (settings), W (open items), X (Operations Hub additions — new stream types and meters), Y (Ecosystem Spec v1.2 change request — LawDocs as `UsageRecorded` producer).
> **Requirements covered:** R-017, R-019, R-021, R-027, R-030, R-033, R-034, R-035, R-036, R-040, R-042, R-049, R-054, R-063.
> **Decisions applied:** D-02, D-05, D-08, D-11, D-13 · **Challenges applied:** CH-08, CH-19, CH-21, CH-25 · **Non-negotiables tested:** NN-01, NN-11, NN-18, NN-19, NN-20, NN-21, NN-22, NN-29, NN-35, NN-36, NN-38, NN-39, NN-45, NN-46, NN-50
> **Estimated effort:** 7 two-week sprints, squad of 8 (backend 3, frontend 2, integration 1 — OH8/Razorpay, QA 1, product/finance analyst 1)

### Objective and business outcome

Give every LawDocs user a plan they understand at a glance, a price they can trust before they pay, and a billing area they can run themselves — upgrade, downgrade, buy credits, download GST invoices, cancel — with no phone call and no dark pattern (R-035, R-036, R-042; NN-50). Give the owner switchable revenue streams with legality gates and kill switches (R-054; NN-18, NN-39). Show every customer, in Settings, an honest Savings & Value account of hours saved, money saved against published market prices and exposure avoided by meeting deadlines — each figure with its formula and evidence class (R-063; NN-36).

LawDocs does not build a billing engine (D-02). OH8 owns money, tax and documents; LawDocs (`bil`, `sav`) owns presentation, entitlement enforcement, metering at source, credits as applied, the billing UI and the savings ledger.

| Outcome | Exit-gate measure |
|---|---|
| Clear pricing page | `/pricing` shows Personal, Pro and Business cards (+ Free and Enterprise links), monthly/annual toggle with saving in ₹ and %, ex-GST price **and total incl. GST** on every card, ≥ 100-row comparison table, "benefits explained", ≥ 25 FAQs; server-rendered; WCAG 2.2 AA |
| Self-serve | Free → paid in ≤ 4 clicks from the pricing page for a signed-in user; upgrade with prorated quote preview in ≤ 3 clicks from Settings; cancellation in no more steps than purchase |
| Never-block floor | 0 cases where non-payment, plan limits or downgrade block reading, exporting, verifying a signed document, nominee access or a deadline reminder already set (test `NN-11_billing_never_blocks`) |
| Money and tax correctness | 0 prices or taxes computed outside OH8 (CI contract test); 100% of invoices e-mailed within 15 minutes of issue and filed in the vault |
| Credits, not wallets | No stored-value balance in rupees exists; all prepaid purchases are service-unit credits redeemable only for LawDocs's own services |
| Revenue-stream control | 45 streams in the registry with owner, effective date, disclosure, tax, refund rule and gate status; a kill switch hides a stream from all surfaces within 5 minutes |
| Honest value | 100% of Savings tiles show formula, inputs, period and evidence class; Modelled exposure never counted in "money saved" or ROI |

---

### Scope (in / out)

**In scope:** `BILLING_PORT` (OH8, LOCAL, MOCK adapters); presentation catalogue (plans, feature rows, add-ons, credit packs, explainers, FAQs); public pricing page and plan configurator; trials; checkout via Razorpay hosted pages (orders, Subscriptions, UPI AutoPay, e-mandates, Smart Collect for B2B); subscription mirror and lifecycle (upgrade, downgrade, proration via OH8 quotes, cycle change, renewal, cancellation); entitlement SDK and enforcement; seats and family members; credits (eSign, eStamp facilitation, Vidhi AI, court-data refresh, storage overage) as prepaid service units; meters at source and `UsageRecorded` aggregates; invoice/receipt/credit-note display, download and vault filing; GST profile and TDS certificate workflow; dunning presentation; coupons and referral credits; revenue-stream registry mirror with LawDocs-side switches; Pricing Studio; Settings → Billing & Membership (Personal and Company); Savings & Value dashboard and value report.

**Out of scope (owner):** price books, tax rates, invoice numbering, e-invoicing IRN, Razorpay accounts and webhooks, revenue recognition, dunning engine, collection — OH8. Marketplace engagements and Route split settlement — P16 (uses this phase's checkout). Enterprise MSAs and negotiated contracts — OH8 sales quotes. Mobile store billing integration — P22 (this phase defines the rule, §4E).

---

## Phase P18 — Delivery Console and Operations Hub Interface

**File:** `phases/P18_Delivery_Console_and_Operations_Hub_Interface.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (Keycloak realms `ld` and `ld-staff`, passkeys, step-up MFA), P02 (tenancy, legal entities, departments, user types, maker-checker engine, grant primitive), P03 (settings registry, rule engine), P04 (Legal Vault/DMS, sharing, folder intake), P09 runtime (Vidhi briefs and drafting, agent sponsorship), P13 (departments, positions and Company Legal Department OS roles), P16 (engagements `eng_`, retainers `rtn_`, SLAs `sla_`, professional registry `pro_`, assignment engine), P17 (billing presentation, entitlements mirror, `BILLING_PORT`), P19 (`int` gateway, `WORKSPACE_PORT`, OH contracts, webhook signing), P20 (`xpt.export_map`, `LD-EXPORT-1.0`). P15 supplies the consumer-case model used by the queue in §4I. **External:** Infrabyx Operations Hub (OH1 group identity and grants, OH1.6 conflict service, OH3 CRM, OH4 onboarding factory, OH5 customer success, OH6 support desk, OH8 billing, OH9 directory, OH10 staff HRMS, OH11 internal controls, OH12 workplace); Microsoft Graph (now); Google Workspace APIs (later, flag OFF).
> **Sequencing:** Start when P02 and P04 have exited and the P16 engagement/retainer schema is frozen (freeze point F-P16-ENG). Sprints 1–3: staff realm, portfolio, client section, delivery grants, act-in-tenant sessions, credential vault. Sprints 4–5: master-data change requests, deliverables, messages/meetings/drives, SLA tracker, practitioner workspace. Sprints 6–7: OH interfaces (contract-tested against the OH sandbox), timesheets and metrics, consumer case queue (built in Wave 2 behind `chp.brand.enabled = false` — the P15 key; switched on with P15 in Wave 3). **P18 must exit before any retainer or LDaaS engagement goes live** (P16 gate).
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), X (Operations Hub and LawDocsComply Addenda), D (roles, personas and access matrix), R (settings catalogue), K (`LD-EXPORT-1.0`), M (marketplace professional rules), Y (Ecosystem Spec v1.2 change request), W (verification log and open items), Q (competitive research and improvement backlog: IMP-003, IMP-010, IMP-012, IMP-087).
> **Requirements covered:** R-014, R-026, R-027, R-028, R-030, R-037, R-039, R-047, R-048, R-050, R-051, R-052, R-053, R-055, R-058, R-062, R-064, R-065, R-066, R-067, R-068, R-080, R-083 (queue only).
> **Decisions applied:** D-02, D-03, D-05, D-06, D-10, D-11, D-17 · **Challenges applied:** CH-07, CH-08, CH-09, CH-10, CH-16, CH-24, CH-26, CH-29, CH-31, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-11, NN-13, NN-16, NN-17, NN-18, NN-19, NN-21, NN-23, NN-24, NN-25, NN-28, NN-29, NN-32, NN-33, NN-39, NN-41, NN-43, NN-45, NN-46
> **Estimated effort:** 7 two-week sprints, squad of 8 (backend 3, frontend 2, integration engineer 1, security engineer 1, QA 1)

### Objective and business outcome

LawDocs sells legal services as well as software: one-time drafting and filings, retainers (Startup Legal Officer, SME Legal Desk, NBFC Legal & Compliance Retainer — Appendix L §L.7), Managed Legal Department (LDaaS) and marketplace engagements (P16). People deliver that work — relationship managers (RMs), in-house professionals, consumer case managers and third-party professionals. **The Delivery Console** (`apps/delivery`, work.lawdocs.in) is their workplace. It gives each staff member one portfolio, a **dedicated section per client company**, a governed way to act as **maker** inside the client's own tenant while the client's employee remains the **checker** (R-064), a client-owned **credential vault** (NN-16), a transparent **master-data change workflow** (CH-26, R-066), and clean interfaces to the Infrabyx Operations Hub (OH) for CRM, onboarding, tickets, customer success, billing, staff identity and timesheets (D-02) — without copying any tenant document, matter, credential or personal content into OH (NN-19).

The console is **not** the Operations Hub (no CRM, marketing, HRMS, payroll or billing engine here) and **not** the Super Admin console (`apps/console`). It is the client-service surface that sits between them (R-048).

| Outcome | Exit-gate measure |
|---|---|
| One portfolio | An RM sees every assigned client with next breach, SLA risk, open tasks, unread messages and grant expiry on one home screen; any client section opens in ≤ 2 clicks from home |
| Governed maker access | Every LawDocs maker in a client tenant holds a client-approved, scoped, time-bound delivery grant; no delivery user can ever be a checker, approver, signatory, director or auditor in a client tenant (`NN-17_delivery_never_checker`) |
| Fast client approval | A client admin approves a proposed grant in ≤ 2 taps from the notification on web or mobile; median proposal-to-active time ≤ 4 working hours (measured) |
| Credential vault | OFF by default; when ON, delegation is offered first, secrets are revealed just-in-time with reason, every view/copy/change is logged and visible to the client; OTPs, DSC PINs and recovery codes cannot be stored |
| Master-data integrity | No crucial client detail (legal name, PAN, CIN/LLPIN, GSTIN, registered office, owner contacts, authorised signatories) changes without client approval, a second Super Admin checker and notification to all owners (`NN-18_masterdata_maker_checker`) |
| Commercial clarity | The client section's Billing tab shows exactly what the client sees on its own Billing page (same component, same OH8 data); RMs cannot change prices, credits or entitlements |
| Clean OH interface | Tickets, CRM activities, onboarding milestones, CSAT/NPS, health signals and timesheets flow through Ecosystem-Spec contracts; a contract test proves no document text, matter data, credential, message body or end-customer personal data leaves LawDocs (`NN-19_no_content_to_oh`) |
| Proportionate productivity | Work is measured by outcomes (tasks, SLAs, deliverables accepted first time, CSAT); sessions are recorded only for attendance; no covert monitoring (NN-33, CH-24, CH-32) |
| Ethical wall | Consumer case managers work in a separate brand queue; no person holds both a Consumer Help role and a delivery grant in a lender/insurer tenant (`NN-23_people_wall`) |

---

### Scope (in / out)

**In scope**

1. `apps/delivery` (Next.js 16) on realm `ld-staff` for LawDocs staff and realm `ld` for third-party professionals (practitioner workspace), phishing-resistant MFA (passkeys/FIDO2) for every delivery user.
2. Staff projection from the group identity provider (OH1/OH10 → Entra ID → SCIM 2.0 → Keycloak `ld-staff`).
3. Portfolio, assignments (RM, backup RM, professionals, reviewer), reassignment and leaver handling.
4. Per-client section: Overview, Contacts, Plan & entitlements, Engagements & retainers, Tasks, Deliverables, Messages, Meetings, Shared drive, Billing & invoices, SLA & reports, Access log, Notes.
5. Delivery grants (propose / approve / standing authorisation / renew / suspend / revoke / expire), multiple delegated makers, departmental role assignment, client checker binding, act-in-tenant sessions.
6. Credential vault (`cvl`) UI and service (client side in `apps/web`, delivery side in `apps/delivery`).
7. Master-data change requests with client approval and Super Admin maker-checker (`apps/console` screens built here).
8. Deliverables register and release gate; messages (`msg`), meetings (Teams now, Google Meet later), shared drive links (SharePoint/OneDrive now, Google Drive later) via `WORKSPACE_PORT`.
9. SLA tracker and monthly service reports.
10. Consumer case manager queue for the `[Consumer Help Brand]` (UI, assignment, walls; case logic is P15).
11. Practitioner workspace for third-party professionals and firms (PRO_* roles).
12. Time entries, utilisation aggregates to OH11, monthly outcome metrics to OH10/OH11, anti-fraud controls in delivery.
13. OH interfaces: CRM (OH3), onboarding (OH4), customer success, CSAT/NPS (OH5), tickets (OH6), billing (OH8), directory (OH9), staff identity (OH10/OH12), cross-company roles (OH1, Ecosystem Spec §4.6), conflict service (OH1.6).
14. Client-side surfaces in `apps/web` and `apps/mobile`: Settings › LawDocs team, approvals, vault, access log, master-data change tracker.

**Out of scope (owner phase)**

| Item | Owner |
|---|---|
| CRM, marketing, social calendar, PR, onboarding factory engine, CS playbooks, support desk engine, staff HRMS, payroll, leave, appraisal, internal-controls engine, billing engine and GST invoices | Operations Hub (Appendix X lists what OH must add) |
| Platform provisioning, global settings, feature flags, break-glass framework | P00, P02, P03, P23 (`apps/console`) |
| Engagement/retainer catalogue, offers, SLAs definition, professional verification and assignment engine | P16 |
| Plans, entitlements, presentation catalogue, Razorpay checkout UI | P17 |
| Consumer case workflows, forum rules, authority letters | P15 |
| Client-tenant legal features (CLM, litigation, IP, governance) — the delegated maker uses the normal tenant UI | P04–P13 |
| Mobile app shell and store release | P22 |

---

## Phase P19 — Integration Gateway, Ecosystem Connectors and Developer Platform

**File:** `phases/P19_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, transactional outbox, audit ledger, KMS, Temporal, OpenTelemetry), P02 (tenancy, roles, maker-checker, delivery grants), P03 (settings registry, flags). Built on P19 later: P01 (KYB/identity adapters), P04 (vault deposits), P07/P08 (eSign/eStamp adapters, hosted signing hand-off), P09 (MCP server edge), P11/P12 (court-data and trademark adapters), P13 (LDC system-of-record switch), P17 (OH8 billing connector), P18 (Delivery Console UI over the OH connector), P20 (storage targets, `LD-EXPORT-1.0`). External: Infrabyx Ecosystem Integration Specification v1.1 (committed unchanged as `docs/ecosystem/infrabyx-integration-spec.md`, SHA-256 checked in CI), the `infrabyx-contracts` registry, the Ecosystem PKI, `@infrabyx/connector-sdk`, and the Appendix Y change request (Ecosystem Spec v1.2) for every LawDocs-specific contract.
>
> **Sequencing:** **Core (Wave 1, sprints 1–3):** gateway, OAuth 2.1 profile, scopes, error model, idempotency, correlation, rate limits, outbox relay, tenant webhooks, DLQ, connector runtime, Operations Hub connector, eSign/eStamp/KYB adapter scaffolding for P01/P08, minimum developer portal. **Full (Wave 2, sprints 4–9):** LDC, Finbyx, Udofin and Equator connectors (behind `int.eco.v12_contracts.enabled` until Appendix Y is merged), partner onboarding API, court-data, trademark, workplace, accounting, HRMS and CRM adapters, Zapier/Make and iPaaS, SDKs, sandbox personas, health dashboard, certification workbench. **Freeze:** scope catalogue and tenant webhook catalogue (Appendix I §I.6–§I.7) freeze at the end of sprint 3; later changes follow FR-P19-06.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), I (Integration Adapters and API Catalogue), Y (Ecosystem Spec v1.2 Change Request — LawDocs), K (`LD-EXPORT-1.0`), R (settings), D (roles), F (instrument eligibility, via P08), M (professional rules), W (verification log). The Ecosystem Spec prevails for any cross-product contract (NN-24).
> **Requirements covered:** R-002, R-003, R-005 (KYB pre-fill transport), R-006 and R-078 (eSign/eStamp adapters), R-012 and R-076 (court data), R-013 (trademark data), R-021 and R-022 (connector framework, stable IDs), R-023, R-024 (bulk intake by API), R-029 and R-062 (Jio channels as adapters), R-034 (payments via OH8), R-041 and R-081 (Academy feed), R-050 (CRM openness via OH3/Brevo), R-053 and R-055 (Microsoft 365, Google Workspace), R-058, R-067 (sharing ledger).
> **Decisions applied:** D-01, D-02, D-10, D-11, D-12, D-14, D-16 · **Challenges applied:** CH-02, CH-03, CH-04, CH-05, CH-06, CH-13, CH-16, CH-17, CH-27 · **Non-negotiables tested:** NN-01, NN-05, NN-06, NN-07, NN-11, NN-13, NN-18, NN-19, NN-23, NN-24, NN-25, NN-32, NN-34, NN-38, NN-39, NN-46, NN-47
> **Estimated effort:** 9 two-week sprints (core 3 in Wave 1), squad of 8 (gateway and platform 3, ecosystem connectors 2, third-party adapters 2, developer experience 1)

### Objective and business outcome

LawDocs must exchange data with four sister products, the group Operations Hub and many third-party systems without each new counterparty becoming a project, and must make "onboarding of new companies easy" (R-002, R-003). P19 delivers one gateway with a small set of stable contracts — versioned REST, CloudEvents over signed webhooks, a connector SDK with mapping packs, a file fallback — and the module `int`, the **only** LawDocs module that publishes or consumes cross-product events (master §5.3). Modules write internal events to the outbox; `int` decides, through registered contracts, what may leave LawDocs, to whom, on which consent or legal basis, and records each movement in a **sharing ledger** the customer can read (CH-16).

Three boundaries shape the design; the brief's wording is challenged where it would breach them:

1. **eSign is not shared.** "Data shareable across ecosystem apps both ways" (R-023) does not extend to LawDocs' ASP capability: an ASP may integrate eSign "only for applications owned or operated by them", and consent and logs stay with the ASP (CCA eSign FAQ; R3 LG-007) [LAW]. Finbyx, Udofin, Equator, LDC and the Operations Hub never use LawDocs' ESP route. A sister product's user signs through LawDocs only as a **LawDocs customer**, in a LawDocs tenant, on a LawDocs-hosted ceremony under LawDocs' consent screen — or the sister product uses its own ESP (NN-06). P19 offers a **hosted signing hand-off**, not an eSign API.
2. **Cross-product data needs a contract and a reason.** No shared database, no direct table reads; every message is a registered event, API or layout with `consentref` or `legalbasis` (NN-24; Spec principles 1, 5). LawDocs has no owner code in Spec v1.1; Appendix Y raises the change request and v1.2-dependent flows stay behind a flag until it is merged (NN-38).
3. **Walls stay up.** Consumer Help (`chp`) exchanges nothing with Finbyx, Udofin, Equator or LDC tenants (NN-23); the Hub receives only commercial records and aggregates (NN-19; Spec principle 12); the Equator neutrality wall covers LawDocs staff identities (Spec §4.6).

| Outcome | Exit-gate measure |
|---|---|
| Ecosystem contracts implemented exactly | Spec §14.3 groups Contract, Security, Idempotency and ordering, Resilience, Reconciliation and privacy, Operations, Aggregates only, Isolation, Archive and storage, plus Appendix Y §Y.13 "Legal-tech boundaries", pass; `ConnectorCertified` emitted for OH, LDC, Finbyx, Udofin and Equator connectors in sandbox |
| One way in | 100% of machine traffic passes the gateway; no module controller reachable outside it |
| Easy company onboarding | A 500-row partner batch gets KYB pre-fill for ≥ 90% of valid CINs/GSTINs at ≤ 5 s p95 per row; invitations go out the same day; activation ≤ 4 taps from the email |
| Time to first API call | ≤ 15 minutes from developer sign-up to an authenticated sandbox call (usability test, 5 developers) |
| Reliable events | Outbox lag p95 ≤ 30 s; webhook delivery p95 ≤ 5 min; zero loss in a 4-hour counterpart-outage drill; DLQ replay only under maker-checker |
| Every share visible | Each cross-product movement of tenant or personal data appears in the sharing ledger within 60 s with counterparty, purpose, basis, record ids and hash |
| No portal automation | No HTTP client in the gateway or connector runtime targets eCourts, IP India, MCA21, GSTN portal UI, CKYCR, bureaus, Parivahan or income-tax portal domains; CI egress test passes (NN-05) |

### Scope (in / out)

**In scope**
- `int`: edge gateway, contract registry client (`contracts.lock`), OAuth 2.1 authorisation-server profile on Keycloak (realms `ld`, `ld-staff`), client registry, restricted API keys, scopes, client-tenant consents, rate limits and quotas, correlation, idempotency store, outbox relay, inbox, tenant webhooks, ecosystem push/pull, DLQ and replay, event-type map, sharing ledger, connector runtime, mapping packs, file fallback, partner onboarding API, health dashboard, developer portal, sandbox, SDKs, automation connectors, certification workbench.
- **Ecosystem connectors:** Operations Hub (provisioning, catalogue, quotes, orders, invoices, entitlements, usage, CRM requests, tickets, directory, claims gate, SCIM staff identity, engineering evidence); LDC (kernel system-of-record switch, legal-matter and contract-obligation projections, policy documents, template packs); Finbyx (template and drafting packs, recovery-litigation projection, hosted signing hand-off for RE tenants that are LawDocs customers); Udofin (opt-in deposit of a borrower's own documents into their Personal vault); Equator (ADR referral, evidence pack, status, award into vault).
- **Third-party adapters** (Appendix I §I.2): eSign, eStamp, KYB/identity, court data, trademark data, Microsoft Graph, Google Workspace, email/SMS/RCS/WhatsApp/voice (JioCX and alternates), TallyPrime, Zoho Books, customer HRMS and CRM, storage (framework; feature in P20), FinLegal Academy feed.
- Tenant webhooks, Zapier/Make-style triggers and actions, Power Automate connector, OpenAPI/AsyncAPI exports.

**Out of scope (owner phase)**
- Ceremony, eligibility and evidence logic (P08); KYC/KYB journeys (P01); vault and folder import UX (P04); litigation and IP modules (P11, P12); governance/HRMS mounts (P13); marketplace (P16); billing UI (P17); Delivery Console screens (P18); exports and BYO storage (P20); website forms (P21).
- MCP server and MCP client registry — **P09** (FR-P19-83).
- Razorpay: LawDocs holds no Razorpay keys; payments run on OH8 (Spec §6.27). P19 builds only `BILLING_PORT` to OH8.
- Machine filing to, or scraping of, any court, registry, regulator, government or bureau portal (NN-05; Spec §10.2 `PORTAL_MANUAL`); bureau pulls, CKYC, direct PAN-database calls (CH-03–CH-05).
- Cross-product A2A agent traffic (OI-P19-09).

## Phase P20 — Data Preservation, Portability, BYO Storage and Migration Safety

**File:** `phases/P20_Data_Preservation_Portability_BYO_Storage_and_Migration_Safety.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (prefixed ULIDs, audit ledger with daily anchors, S3 SSE-KMS + versioning + Object Lock, expand-migrate-contract framework, Temporal), P02 (approvals, delegations), P03 (settings registry, `wf.items`, configuration bundle), P04 (Legal Vault/DMS: documents, versions, SHA-256 at ingest, folders as views, retention classes, legal hold), P19 core (connector framework, `int`, secrets vault for connector credentials), P05 (document classification — Wave 2 import assist), P08 (evidence packs and BSA s.63 certificate generator). Every module that persists records registers its record types in `xpt.export_map` before its own exit gate (NN-11) — enforced by the CI contract test built here.
> **Sequencing:** **Core (Wave 1, 2 sprints):** extend the P00 export-map registry head and its CI contract test (FR-P00-87; `NN-11_export_map_complete` and `ci/export-contract` are the same gate) in sprint 1, before P04 exits; `LD-EXPORT-1.0` builder for on-demand full and partial exports with download, folder/ZIP import with rule-based placement, golden archives. **Full (Wave 2, 4 sprints):** BYO storage targets and continuous mirror, scheduled exports, AI-assisted import classification, verifier and loader tools, exit/offboarding, region and vendor move runbooks, ecosystem archive sharing.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), K (export package `LD-EXPORT-1.0` and folder taxonomy — binding for every folder, file name, format and manifest field), R (settings `xpt.*`), D (roles), F (eligibility — for evidence-pack contents), Y (Ecosystem Spec v1.2 change request: folder-profile registration and `portability` producer). **The Infrabyx Ecosystem Integration Specification v1.1 §12.1 (archive standard 1.0) and §12.2 (customer-controlled storage connector contract) prevail on conflict** (NN-24); `LD-EXPORT-1.0` is LawDocs' set of folder profiles within that standard.
> **Requirements covered:** R-021, R-022, R-024, R-068, R-011 (preserve), R-043 (selective export/sharing), R-053, R-055, R-023 (archive sharing across ecosystem apps), R-031 (DPDP portability and erasure), R-061, R-067 (audit trail export).
> **Decisions applied:** D-01, D-02, D-06, D-10, D-11 · **Challenges applied:** CH-15, CH-16, CH-29 · **Non-negotiables tested:** NN-01, NN-02, NN-04, NN-09, NN-10, NN-11, NN-12, NN-13, NN-17, NN-18, NN-19, NN-24, NN-25, NN-26, NN-32, NN-42, NN-45, NN-46
> **Estimated effort:** 6 two-week sprints (core 2 in Wave 1; full 4 in Wave 2), squad of 8 (portability core 3 backend, connectors 2, import 1, frontend 1, QA/verification 1).

### Objective and business outcome

A LawDocs user must never feel trapped and must never lose a document. On any day — while subscribed, after cancelling, during a court case, when an auditor asks, or when a company switches tools — any individual or company can take **everything** as an ordinary folder tree of Word, Excel, PDF/A, CSV and original files, with self-explanatory folder and file names that a person can follow in Windows Explorer or macOS Finder without LawDocs. A company can keep a **continuous copy in its own storage** (its S3 bucket, Azure or Google storage, SharePoint/OneDrive, Google Drive, SFTP server, NAS or data centre). The same taxonomy works in reverse: a user drops an existing folder of 3,000 agreements and LawDocs files them, instead of the user uploading one by one (R-024).

Because folder paths are **views over permanent canonical IDs** and the export layout is a versioned contract rather than today's code, the owner can push patches, add features, change the database engine, swap storage vendor or move data centre without any customer re-filing or migrating data (R-021, R-022, NN-12).

| Outcome | Exit-gate measure |
|---|---|
| Everything exportable (NN-11) | Export-coverage test: every persisted record type maps to `xpt.export_map`; a seeded tenant with every record type exports with 100% count reconciliation per type and 100% of originals byte-identical (SHA-256) |
| Understandable without LawDocs | Usability test: 5 of 5 non-technical participants (a homeowner, an office manager, a junior lawyer, a startup founder, an external auditor) each find a named signed agreement with its stamp certificate and signing evidence, a court order, and the audit trail of a status change within 3 minutes using only Explorer/Finder and Office |
| Verifiable offline | Open-source verifier (Apache-2.0) confirms checksums, the detached JWS, control totals and audit-chain continuity; fails on one changed byte or one missing file |
| Stable across change (R-022) | Golden-archive test: the same synthetic tenants exported before and after (a) a release with schema changes, (b) a PostgreSQL major upgrade, (c) a storage-vendor swap, (d) a region-move rehearsal give identical paths, file names and IDs for unchanged records; differences only as additions declared in `CHANGES-SINCE-PREVIOUS.csv` |
| BYO storage (R-021) | A tenant connects S3, Azure Blob, SharePoint and SFTP targets; residency and canary pass; continuous mirror lag p95 ≤ 15 min; nightly reconciliation zero drift; restore test from the tenant's own copy passes |
| Bulk intake (R-024) | A 5,000-file folder imports with ≥ 90% automatic placement on a tidy tree (100% for a tree previously exported by LawDocs), duplicates linked by hash, every unplaced file in a correction queue before commit, nothing overwritten, full undo for 7 days |
| Exit without friction | Exit export of a 200 GB company completes in ≤ 24 h; read-only period; deletion certificate; never blocked by billing state |

---

### Scope (in / out)

**In scope**

- `xpt` module: export map registry, export jobs and scopes, package builder, folder profiles, manifest, checksums and signing, verifier and loader, download service, scheduled exports, continuous mirror, BYO storage targets (`stg_`), import jobs (`imp_`), exit/offboarding workflow, deletion certificates, DPDP access and portability exports.
- `StorageTarget` adapters built on P19's connector framework, implementing Ecosystem Spec §12.2.
- Schema-evolution and infrastructure-move safety mechanisms that protect customer data and folder structure (CI gates, golden archives, archive versioning, move runbooks). Platform backups, PITR and DR of LawDocs' own estate are P23.

**Out of scope (owner phase)**

- Business retention rules per record type (owning modules + P04 retention engine); P20 enforces retention classes and legal holds on exports, targets and deletion.
- Co-authoring in Microsoft 365 or Google Workspace (P19 suite connectors); P20 uses the same connector credentials only for storage push.
- Ops Hub exit-project tracking (OH4 receives status and counts only, NN-19).
- Platform backup/restore and DR drills (P23).

---

## Phase P21 — Public Website, No-Code CMS (Blog/Vlog), SEO/GEO, Help Centre, Tutorials, "i" Glossary and Accessibility

**File:** `phases/P21_Public_Website_CMS_SEO_GEO_Help_Centre_and_Accessibility.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, `apps/public` scaffold, CDN, legacy-site inventory and the seed 301 map, host decision `https://www.lawdocs.in`); P01 (consent ledger and notice versions, OTP sign-up, account creation from the drafter); P02 (roles, maker-checker engine, screen and menu registry that carries `help_key` and `data-tour-id`); P03 (settings registry, rules register `rul` used for citations, stamp-duty and jurisdiction facts); P06 (published templates and questionnaires behind the "Draft free with Vidhi" block); P08 (instrument eligibility gate, Appendix F, for the eSign badge; State stamp registry); P09 runtime (Vidhi help mode and the content-drafting agent); P16 (marketplace catalogue, service tiers and professional rules rendered on public pages); P17 (plans, prices, credit packs, trial rules rendered on the pricing page); P19 core (`int` gateway for Operations Hub CRM, support desk, claims gate and asset library calls). External: Operations Hub OH3 (CRM), OH7 (marketing, social calendar, asset library), OH14 (claims gate); YouTube; Google Search Console and Bing Webmaster Tools; IndexNow; a plagiarism-check provider; `TRANSLATE_PORT` providers.
> **Sequencing:** Wave 1 delivers §4A–§4H core (site shell, rendering, multi-brand theming, 301 map, legal policies from Appendix O, pricing page, marketplace storefront shell, the top 50 content pages from Appendix N §N.9 wave 1, the CMS with DOCX import and blog, 150 glossary terms, the help panel framework and the accessibility statement). Wave 2 adds vlog, tutorials pipeline, guided tours, landing-page builder, Hindi plus four further D-07 languages and 350 glossary terms. Wave 3 completes the ≈626 manual-derived pages, the remaining D-07 languages, 500+ glossary terms, ISL tutorial renditions and the Consumer Help brand site. **First slice for the P00 cut-over:** the SSR shell, host rules and the redirect-target pages P00 needs (P00 §5.5, T−28 d) depend only on P00 and do not wait for P06; the "Draft free with Vidhi" blocks attach when P06 publishes templates, and until P16 exits (Wave 2) the storefront shell renders the P17 presentation catalogue (OH8 feed). Freeze points: the URL scheme (§4B) and the block schema (§4I) freeze at the end of sprint 2; after that, changes go through expand → migrate → contract (NN-12) with redirects.
> **Binding appendices:** N (website copy system, SEO/GEO, tutorials and video plan), O (legal policies), U (accessibility specification), M (marketplace professional rules), F (instrument eligibility), R (settings registry), D (roles), K (`LD-EXPORT-1.0`), H (agent roster), X (Operations Hub addendum: CRM, funnels, social calendar, asset library), Y (Ecosystem Spec v1.2 change request), W (open items).
> **Requirements covered:** R-004, R-008, R-016, R-019, R-020, R-025, R-030, R-032, R-036 (pricing page rendering), R-041 (open marketplace and academy entry), R-056 (funnel surfaces; OH is system of record), R-070, R-071, R-072, R-073, R-074, R-075 (public pages for added services), R-082 (startup section), R-086 (competitor-informed IA), R-087, R-088, R-089, R-090, R-091.
> **Decisions applied:** D-01, D-02, D-04, D-05, D-06, D-07, D-08, D-11, D-13, D-15, D-16, D-17 · **Challenges applied:** CH-08, CH-11, CH-12, CH-14, CH-20, CH-21, CH-30 · **Non-negotiables tested:** NN-02, NN-07, NN-11, NN-14, NN-18, NN-19, NN-20, NN-21, NN-22, NN-26, NN-28, NN-29, NN-30, NN-31, NN-32, NN-35, NN-38, NN-45, NN-48, NN-49, NN-50
> **Estimated effort:** 10 two-week sprints, squad of 8 (2 front-end, 1 back-end, 1 content engineer, 1 SEO/technical-content lead, 1 accessibility specialist (IAAP CPACC or WAS), 1 product designer, 1 QA), plus a standing content team of 4 (two legal writers, one technical writer, one video producer) and a reviewer of record (`PLT_LEGAL_REVIEWER`) for legal pages. Wave split: Wave 1 = 4 sprints, Wave 2 = 3, Wave 3 = 3.

### Objective and business outcome

The live lawdocs.in is a client-side single-page application. A crawler or AI engine sees only a `<head>`: one title and one meta description on every URL, no H1, no body and no links (R5 §1.1). The sitemap lists non-www URLs that fail, `robots.txt` blocks `/buy/` while the sitemap lists 20 `/buy/*` URLs, and the positioning is compliance-first rather than documents, eSign and Vidhi. The manuals hold about 626 usable pages of content after de-duplication, but 21 sections contain copied competitor or Wikipedia text, the testimonials look adapted from proposal software, and much of the law is out of date (CrPC/IPC/Evidence Act, CPA 1986, Udyog Aadhaar, Income-tax Act 1961, pre-Code labour statutes) (R5 §3–§5).

This phase replaces that site with a server-rendered, multi-brand public website and a no-code content system, and builds the help layer that every authenticated app uses.

**Who benefits**

| Audience | Outcome |
|---|---|
| Individuals and small businesses | Find the right document, pleading or service in plain language; draft free from a vetted template; see whether eSign is legally valid for that instrument; see the full price before paying; hire a professional at a fixed price. |
| Companies and legal teams | Clear module, pricing and marketplace pages; tutorials and tours that shorten onboarding; contextual "i" explanations of legal and product jargon. |
| Search engines and AI answer engines | Unique, indexable, citable pages with answer-first summaries, visible FAQs, valid structured data, named reviewers and dated citations. |
| Users with disabilities | WCAG 2.2 AA and IS 17802 conformant pages, captions, transcripts, Indian Sign Language (ISL) renditions of core tutorials, easy-read summaries, a working feedback channel (Appendix U). |
| LawDocs operations (`OPS_CONTENT_PUBLISHER`) | Publish a blog post from a categorised Word file in under 10 minutes, with maker-checker and legal review, without a developer (R-089). |

**KPIs (measured from go-live of each wave)**

| KPI | Target |
|---|---|
| Indexable routes returning server HTML with a unique title, meta description, one H1 and ≥ 150 words of main content | 100% (CI-enforced) |
| Legacy URLs (186 sitemap URLs plus known indexed URLs) resolving 200 or a single-hop 301/410 | 100% |
| URLs passing Core Web Vitals at p75 on mobile (field data, Search Console) | ≥ 90% within 90 days of each wave |
| Published legal pages with a reviewer of record and a last-reviewed date | 100%; pages without one are `noindex` automatically |
| Pages failing the plagiarism gate at publication | 0 |
| Pages citing superseded law without a "(formerly …)" mapping | 0 (outdated-law linter) |
| DOCX → published blog post median time (publisher + checker) | ≤ 10 minutes of hands-on time |
| Lead captured → visible in Operations Hub CRM | ≤ 60 seconds p95 |
| Glossary coverage | 150 terms (Wave 1), 350 (Wave 2), ≥ 500 (Wave 3), each with plain definitions in all enabled D-07 languages |
| UI strings tagged as jargon without a registered "i" key | 0 (lint) |
| Automated axe-core serious or critical violations on any public template | 0; manual audit per Appendix U §U.8 each release |
| Free draft → paid action (eSign, eStamp, clean download or professional review) | ≥ 15% [target to calibrate — R4 §11.10] |

**Done for users** means: a visitor lands on `/documents/property-transactions/rent/rent-agreement-residential`, reads a 50-word answer, sees that eSign is valid, drafts the agreement in five to eight questions, sees the State stamp duty with its source and verification date, and either pays to eStamp and eSign or hires a professional, in ≤ 3 clicks from the page and with every fee shown separately before payment.

### Scope (in / out)

**In scope**

1. `apps/public` (Next.js 16 App Router, SSR/SSG with incremental revalidation), multi-brand: **LawDocs** (`www.lawdocs.in`) and **`[Consumer Help Brand]`** (own host, own legal entity profile, D-06/NN-23).
2. Information architecture: the four manual sections (`/documents`, `/pleadings`, `/compliance`, `/start-a-business`), the fifth section `/regulated-entities` carried over from the live sitemap, `/advisory` practice areas, product pages (Vidhi, eSign and eStamp, Legal Vault, contracts and negotiation, litigation tracker, trademark tracker, company legal department), marketplace storefront, pricing, startup section, FinLegal Academy entry, Consumer Help entry, blog, vlog, help centre, glossary, free tools, legal policies (Appendix O), About, Partnership, Careers, Contact, Trust.
3. Page templates with the embedded **"Draft free with Vidhi"** and **"Hire a professional"** blocks (R-087), eSign eligibility badge, key-facts box, State variations, visible FAQs, testimonials without photos (NN-49), E-E-A-T footer.
4. Technical SEO: canonical host, sitemaps, robots and AI-crawler policy (NN-31), structured data, hreflang, Core Web Vitals budgets, IndexNow, the 301 migration map (seeded in P00, owned here from P21 onwards), optional `llms.txt`.
5. GEO for AI answers: definitions first, entity consistency, original data assets, citations, AI-answer monitoring.
6. No-code CMS (`web` module, Content Studio in `apps/console`): pages, blog posts from DOCX, categories, tags, authors, scheduling, SEO fields, maker-checker, legal-review flag, preview, rollback; vlog with YouTube privacy-enhanced embeds; landing-page builder for campaigns; lead capture to Operations Hub CRM with consent.
7. Help centre (`hlp` module): public help articles, in-app help panel for all apps, the "i" glossary registry, guided tours, the tutorial pipeline (text, annotated screenshots, diagrams, interactive artefacts, short captioned videos with ISL option) that also produces social-ready clips (R-020).
8. Accessibility statement, conformance report and feedback channel for the public site; the accessibility specification itself is Appendix U (binding on every phase).

**Out of scope (owner phase)**

| Item | Owner |
|---|---|
| Template content, questionnaires, assembly engine, AI Drafting Studio | P06 (this phase embeds them) |
| Vidhi runtime, guardrails, agent roster | P09, Appendix H |
| Instrument eligibility rules and State stamp registry data | P08, Appendix F |
| Plan, price, credit and trial data; checkout; GST invoices | P17 and OH8 (this phase renders) |
| Marketplace catalogue, engagements, professional registry, academy feed | P16 (this phase renders the storefront) |
| CRM, nurture sequences, Brevo, social calendar and posting, PR | Operations Hub (Appendix X); this phase hands off leads and assets through `int` |
| Consumer Help case flows (grievances, challans, vehicles) | P15 (this phase builds the brand site and its content pages) |
| Mobile app store listing copy and in-app help rendering on native | P22 (reuses `hlp` content and APIs) |
| Legal policy texts | Appendix O (this phase publishes and versions them) |
| Legacy platform decommissioning and data migration | P00 |
| Advertising stream (OFF by default) | P17 revenue-stream switch; placement rules here (NN-35) |

## Phase P22 — Mobile Apps (iOS/Android) and Store Release

**File:** `phases/P22_Mobile_Apps_and_Store_Release.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (OIDC realms, OTP, passkeys, consent ledger, Aadhaar offline verification flows), P02 (workspaces, roles, maker-checker), P04 (vault APIs, Object Lock, hashes), P05 (OCR, type copy, translation renditions), P06/P07 (questionnaires, Drafting Studio, redlines, deal rooms, messaging), P08 (eligibility gate, eStamp, ESP adapters, evidence packs), P09 (Vidhi runtime), P11/P12 (case and trademark status), P15 (Consumer Help cases — v2), P16/P17 (catalogue, checkout, entitlements), P19 (gateway, webhooks), P20 (export jobs), P21 (`hlp` content, glossary, tours, tutorials). External: Apple App Store Connect, Google Play Console, Expo Application Services (EAS Build, Submit, Update), APNs/FCM, Play Integrity API, App Attest, Razorpay React Native SDK, the eSign aggregator chosen in P08.
> **Sequencing:** Wave 2 ships v1 of the LawDocs app (individuals and companies: vault, scan, share import, drafting, negotiation, eSign/eStamp, approvals, case/TM status, Vidhi chat, marketplace purchase, notifications). Wave 3 ships v2: the `[Consumer Help Brand]` flavour, Vidhi voice in all D-07 languages, practitioner-lite space for `PRO_*`, offline Vidhi help. The BFF contract (`/m/v1`) freezes at the end of sprint 2; device-trust and offline-cache designs pass a security review (P23) before any store submission.
> **Binding appendices:** U (accessibility), F (instrument eligibility), K (`LD-EXPORT-1.0`), M (marketplace rules), N (store listing copy, video plan), R (settings), D (roles), H (Vidhi agents), W (open items), Y (ecosystem change request).
> **Requirements covered:** R-008, R-010, R-011, R-012, R-013, R-017, R-019, R-025, R-030, R-034, R-043, R-044, R-045, R-061, R-064 (approvals), R-068, R-077, R-078, R-083, R-084 (status and deep links; v2).
> **Decisions applied:** D-01, D-06, D-07, D-11, D-12, D-14, D-15 · **Challenges applied:** CH-01, CH-02, CH-11, CH-12, CH-13, CH-15, CH-28, CH-30 · **Non-negotiables tested:** NN-01, NN-03, NN-04, NN-06, NN-07, NN-08, NN-09, NN-11, NN-13, NN-14, NN-18, NN-20, NN-22, NN-23, NN-26, NN-28, NN-32, NN-34, NN-37, NN-44, NN-46, NN-48, NN-50
> **Estimated effort:** 9 two-week sprints (v1 6, v2 3), squad of 8 (3 React Native engineers, 1 native-module engineer (iOS/Android), 1 back-end engineer for `mob` and the BFF, 1 mobile security engineer (shared with P23), 1 product designer with accessibility specialism, 1 QA/device-lab engineer).

### Objective and business outcome

The owner wants users to keep LawDocs "the way people use DigiLocker": always on the phone, used to prepare, negotiate, sign, amend and preserve agreements (R-011, R-017). LegalKart's app is a consultation wallet; LawDocs' app is the Legal Vault plus signing and drafting in the pocket (R1 §3.7). The phone is also where most evidence is born: photographs of stamp papers, handwritten receipts, WhatsApp chats and screenshots (CH-28).

**Outcomes and KPIs**

| KPI | Target |
|---|---|
| First document from install to signed (template lane, Aadhaar eSign, eligible instrument) | ≤ 5 minutes median; ≤ 3 taps from home to start |
| Open a pinned offline document | ≤ 1 s from unlock, no network |
| Signing-invite link → signer reviewing the document (guest, no app) | ≤ 2 taps and one OTP |
| Crash-free sessions (production) | ≥ 99.7% |
| ANR rate (Android) | < 0.47% (below Play "bad behaviour" threshold [VERIFY current threshold]) |
| Cold start to interactive | < 2.5 s mid-range Android; < 4.0 s low-end |
| Download size | ≤ 35 MB Android per-device APK; ≤ 50 MB iOS thinned |
| Parity matrix coverage (every web capability has a mobile status) | 100%, CI-enforced |
| Accessibility: five critical journeys pass manual VoiceOver and TalkBack scripts | 100% per release |
| PII found in crash or analytics payloads in the monthly sample audit | 0 |

**Done** means an individual can scan a stamp paper, draft a rent agreement in Hindi, negotiate one clause in chat, eStamp and eSign, and find the signed copy offline a year later; a company checker can approve a contract from a push notification with biometric step-up; a counterparty can sign from a WhatsApp or RCS link without installing anything.

### Scope (in / out)

**In scope**

1. `apps/mobile` (Expo React Native, New Architecture, Hermes, Expo Router, TypeScript strict), one codebase, two brand flavours: **LawDocs** and **`[Consumer Help Brand]`** (v2).
2. Mobile BFF `/m/v1` in the `mob` module; device registry, push tokens, deep-link tokens, app-version policy, OTA release records.
3. Features per the parity matrix (§6.1): vault with encrypted offline cache; camera scan with edge detection and OCR; share-sheet import including WhatsApp chat exports; drafting (template lane and Vidhi lane); negotiation chat and change review; eSign and eStamp flows; maker-checker approvals; case, hearing and trademark status with alerts; Vidhi chat and voice in D-07 languages; marketplace browse and purchase; notifications; help panel, "i" popovers, tours; accessibility preferences; account and data export requests.
4. Device trust, biometric unlock, integrity attestation, certificate pinning, screen protection (NN-44).
5. Store compliance: purchase-method classification for Apple and Google, listings and ASO, App Privacy labels, privacy manifest, Google Play Data safety form, account deletion, review notes and demo accounts.
6. Release trains with EAS, OTA update policy, crash and analytics with PII scrubbing.

**Out of scope (owner)**

| Item | Owner / channel |
|---|---|
| Content Studio, console administration, rule and template authoring | Web (`apps/console`), P03/P06/P21 |
| Delivery Console for `OPS_*` roles | Responsive web (`apps/delivery`) in v1; native "ops approvals" only if Appendix X requests it |
| Bulk folder import (R-024) and BYO storage set-up | Web (P04, P20); mobile can trigger and download exports |
| DSC (USB token) signing | Web/desktop (P08); mobile shows DSC tasks as "Sign on computer" |
| Client credential vault reveal (`cvl`) | Web only in v1 (NN-16 controls); mobile shows that a request exists |
| Redline authoring of whole documents | Web; mobile reviews changes, accepts/rejects per change and comments |
| FinLegal Academy course consumption | `trainings.lawdocs.in` (D-16); not sold or played in the app |
| Consumer Help case management (`OPS_CONSUMER_CASE_MANAGER`) | Web (P15) |

## Phase P23 — Engineering Governance, Change/Patch Management, Hardening, VAPT/IS Audit, Certification Readiness and Go-Live

**File:** `phases/P23_Engineering_Governance_Change_Patch_Hardening_Audit_and_GoLive.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, CI/CD skeleton, AWS accounts, Terraform, audit ledger, Object Lock buckets, OpenTelemetry), P01 (staff realm `ld-staff`, MFA, break-glass), P03 (settings registry, feature flags, kill switches), P20 (export-map contract test, golden archives, move runbooks) and **every functional phase whose scope is being released**. External: GitHub organisation, Operations Hub **OH13** (engineering console and CAB record, `ChangeApproved`) and **OH14** (control library and provider-assurance room), CERT-In-empanelled auditor, certification bodies.
> **Sequencing:** The governance track (§4A–§4F) starts in sprint 1 of P00 in reduced form and is complete before P04 exits, so that every Wave 1 module is built under the final controls. The hardening, evidence and go-live track (§4G–§4M) runs before each wave's general availability. **P23 re-runs once per wave** (Wave 1 "Vault & Sign GA", Wave 2 "Legal Ops for companies", Wave 3 "Services and Consumer") for the scope released in that wave (§13.3).
> **Binding appendices:** P (security, privacy and certification readiness — control set, claims language, log retention), R (settings `eng.*`), D (staff roles and segregation of duties), K (export package — golden archives), W (open items and the `[VERIFY]` census — `ci/verify-census`), X (Operations Hub addendum: OH13/OH14 interfaces), Y (ecosystem events), Z (brief traceability matrix — `ci/trace-check`). Ecosystem Spec §6.29 (`ReleasePublished`, `ChangeApproved`, `ControlEvidenceCollected`), §6.26 (`BackupCompleted`, `RestoreTested`) and §14 (versioning and certification) prevail on conflict.
> **Requirements covered:** R-057, R-033, R-034, R-031, R-021, R-022, R-067, R-017 (mobile release governance), R-001 (challenge on certification claims).
> **Decisions applied:** D-01, D-02, D-12, D-14 · **Challenges applied:** CH-19, CH-24 (no surveillance of engineers), CH-32 · **Non-negotiables tested:** NN-02, NN-12, NN-18, NN-20, NN-25, NN-27, NN-28, NN-30, NN-32, NN-33, NN-38, NN-39, NN-45, NN-46
> **Estimated effort:** 6 two-week sprints for the first run (governance 2 with a platform squad of 4 in parallel with P02–P04; hardening and go-live 4 with a squad of 8: SRE ×2, security engineer ×2, QA lead, backend ×2, compliance analyst); each later wave re-run 2 sprints.

### Objective and business outcome

The owner will push code to GitHub often — patches, features, framework upgrades, infrastructure moves — while individuals rely on LawDocs to keep their property papers and signed agreements for decades, and companies rely on it for evidence they will produce in court. P23 makes change safe and provable:

- every change is reviewed, tested, approved by someone other than its author, traceable to a release and reversible;
- customer data and folder structures survive every release and every infrastructure move (with P20);
- backups are proven by restoring them; disaster recovery is drilled;
- vulnerabilities are fixed within published deadlines;
- the platform is ready for an annual CERT-In-empanelled audit, IS and internal audits, client audits and certification (SOC 2 Type 1 then Type 2, ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 42001, ISO 22301, PCI DSS SAQ A for hosted checkout) — **without claiming any certification before the certificate or report exists** (NN-20, R-033);
- each wave goes live through a signed checklist and a hypercare period.

| Outcome | Exit-gate measure |
|---|---|
| Every production change approved and traceable | 100% of production deployments in the trailing 30 days map to a change record with a matching `ChangeApproved` (OH13) and a signed image digest; zero deployments outside the pipeline |
| Releases never disturb customer data | `ci/migrations`, `ci/export-contract` and the golden-archive diff (P20) pass for every release; zero customer migration steps in release notes (NN-12) |
| Recoverability proven | Latest restore test of every T0 store passed within RTO; one full DR failover to ap-south-2 met RPO ≤ 15 min and RTO ≤ 4 h; evidence filed |
| Security debt under control | No open Critical; no High past SLA; CERT-In-empanelled audit report issued after retest with Critical/High closed |
| Certification-ready | ≥ 80% of mapped controls with automated evidence; policy set approved by the Board of `[LawDocs Operating Entity]`; external readiness assessment with no Critical gaps; trust page makes no unevidenced claim |
| Safe go-live | Wave checklist signed by CTO, `PLT_SECURITY_OFFICER`, `PLT_DPO`, Company Secretary (owner) and product owner; hypercare exit criteria met |

---

### Scope (in / out)

**In scope**

- GitHub organisation, repositories, branch model, rulesets, CODEOWNERS, signed commits and tags, PR template, merge queue, required checks.
- Environments: dev, test, staging, pre-prod, prod (+ DR region, backup and log-archive accounts); test-data policy; secrets; infrastructure as code.
- Change management (CAB-lite with OH13), change classes, risk scoring, maker-checker deployment approvals, change calendar and freeze windows, customer notice periods, release notes.
- Database migration governance and data preservation across releases and infrastructure moves (with P20).
- Release management: trains, rings, feature-flag rollouts (P03 registry), mobile store releases (with P22), content releases vs code releases.
- Patch and vulnerability management: intake, severity, SLAs, dependency hygiene and SBOM, OS and container patching, end-of-support register, exceptions.
- Backups (PITR, cross-region, immutable), restore drills, DR (RTO/RPO), business continuity.
- Security testing: SAST, SCA, secrets, IaC, container, DAST, API fuzzing, mobile testing, AI red-team suite; VAPT by a CERT-In-empanelled auditor; ASP/eSign and DigiLocker audits; responsible disclosure.
- Audit readiness: IS audit, internal audit, statutory/external audit support, client audits, evidence rooms, access reviews.
- SOC 2 / ISO evidence automation and certification programme; PCI DSS SAQ A scope control.
- Hardening, performance and resilience testing; incident management and regulatory clocks.
- Go-live checklist per wave and hypercare.

**Out of scope (owner)**

- Group-wide engineering console, CAB tooling and control library: Operations Hub OH13/OH14 (D-02). LawDocs emits events and evidence to them and consumes `ChangeApproved`; where OH13/OH14 are not yet live, the local `eng` records act as the system of record and back-fill OH when it arrives (Appendix X).
- Writing the policies themselves (information security, access control, acceptable use, etc.) — the owner prepares them (brief); P23 lists them, hosts them in LawDocs' own Company workspace (dog-fooding P04/P13) and records Board approvals.
- Tenant-facing security features for client companies (their own incident registers) — P13.

---


---

# PART D — APPENDIX INDEX

| Appendix | Title | Words |
|---|---|---|
| `appendices/A_Workflows_and_State_Machines.md` | Appendix A — Workflows and State Machines (binding) | 16,900 |
| `appendices/B_Data_Model_Events_and_Error_Codes.md` | Appendix B — Data Model, Events and Error Codes (binding) | 19,200 |
| `appendices/C_Information_Architecture_Screens_Menus_Dashboards_and_Click_Budgets.md` | Appendix C — Information Architecture, Screens, Menus, Dashboards and Click Budgets (binding) | 19,500 |
| `appendices/D_Roles_Personas_and_Access_Control_Matrix.md` | Appendix D — Roles, Personas and Access Control Matrix | 10,200 |
| `appendices/E_Template_Pleading_and_Service_Taxonomy.md` | Appendix E — Template, Pleading and Service Taxonomy | 17,900 |
| `appendices/F_Instrument_Eligibility_Matrix_eSign_Stamp_Registration.md` | Appendix F — Instrument Eligibility Matrix: eSign, Stamp and Registration | 10,800 |
| `appendices/G_Legal_and_Regulatory_Rules_Register.md` | Appendix G — Legal and Regulatory Rules Register | 22,200 |
| `appendices/H_Vidhi_AI_Agent_Specification_and_Prompt_Library.md` | Appendix H — Vidhi AI Agent Specification and Prompt Library | 10,700 |
| `appendices/I_Integration_Adapters_and_API_Catalogue.md` | Appendix I — Integration Adapters and API Catalogue | 9,200 |
| `appendices/J_Jio_Business_Services_and_Telecom_Rules.md` | Appendix J — Jio Business Services and Telecom Rules | 5,600 |
| `appendices/K_Export_Package_LD-EXPORT-1.0_and_Folder_Taxonomy.md` | Appendix K — Export Package `LD-EXPORT-1.0` and Folder Taxonomy | 8,000 |
| `appendices/L_Pricing_Plans_Revenue_Stream_Registry_and_Savings_Model.md` | Appendix L — Pricing, Plans, Revenue-Stream Registry and Savings Model | 13,600 |
| `appendices/M_Marketplace_Services_Catalogue_and_Professional_Rules.md` | Appendix M — Marketplace Services Catalogue and Professional Rules | 8,800 |
| `appendices/N_Website_Copy_System_SEO_GEO_Tutorials_and_Video_Plan.md` | Appendix N — Website Copy System, SEO/GEO, Tutorials and Video Plan | 11,200 |
| `appendices/O_Legal_Policies_Review_Ready_Drafts.md` | Appendix O — Legal Policies: Review-Ready Drafts | 22,800 |
| `appendices/P_Security_Privacy_and_Certification_Readiness.md` | Appendix P — Security, Privacy and Certification Readiness | 8,700 |
| `appendices/Q_Competitive_Research_and_Improvement_Backlog.md` | Appendix Q — Competitive Research and Improvement Backlog | 9,200 |
| `appendices/R_Configuration_Framework_and_Settings_Catalogue.md` | Appendix R — Configuration Framework and Settings Catalogue | 22,900 |
| `appendices/S_Consumer_Help_Rules_and_Playbooks.md` | Appendix S — Consumer Help Rules and Playbooks | 9,800 |
| `appendices/T_Company_Legal_Department_OS_and_Finance_Company_Structure.md` | Appendix T — Company Legal Department OS and Finance Company Structure | 9,100 |
| `appendices/U_Accessibility_Specification.md` | Appendix U — Accessibility Specification | 5,700 |
| `appendices/V_Acceptance_Tests_and_UAT_Catalogue.md` | Appendix V — Acceptance Tests and UAT Catalogue (binding) | 16,700 |
| `appendices/W_Verification_Log_and_Open_Items.md` | Appendix W — Verification Log and Open Items | 20,300 |
| `appendices/X_Operations_Hub_and_LawDocsComply_Addenda.md` | Appendix X — Operations Hub and LawDocsComply Addenda | 7,600 |
| `appendices/Y_Ecosystem_Spec_v1.2_Change_Request_LawDocs.md` | Appendix Y — Ecosystem Spec v1.2 Change Request (LawDocs) | 9,800 |
| `appendices/Z_Brief_Traceability_Matrix.md` | Appendix Z — Brief Traceability Matrix | 20,900 |
