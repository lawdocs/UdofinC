# LAWDOCS — MASTER BUILD PROMPT (v1.1, 26 October 2026)

**India-first legal-work platform for individuals, startups, professionals and companies: draft, negotiate, stamp, sign, store, track and get expert help — web, iOS and Android**

Product: LawDocs (lawdocs.in), product code `LD` · Mobile apps: "LawDocs" (App Store, Google Play) · Owner: Company Secretary, Infrabyx Group (project owner and product manager) · Operating entity: `[LawDocs Operating Entity]` (D-08) · Companion documents *(v1.1)*: **Infrabyx Platform Baseline Standard (IPB) v1.0** (`docs/ipb/`), Infrabyx Ecosystem Integration Specification v1.2, Infrabyx Operations Hub Master Prompt v1.1, LawDocsComply Build Prompt Pack v1.3, Equator Resolution Build Prompt Pack v3.2, Finbyx Master Prompt v1.6, Udofin Master Prompt v1.3. (v1.0 named Ecosystem Spec v1.1, OH v1.0, LDC v1.2, EQ v3.1, FBX v1.5, UDF v1.2 — superseded by the 26 October 2026 group upgrade.)

> **How to use (project owner — do not paste this box).** At the start of every build session paste, in this order: this file, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, then the phase file (`phases/PXX_*.md`). Attach the appendices the phase file names as binding. The coding agent writes `docs/phases/PXX-plan.md` before any code and stops at the phase exit gate (§13 of the phase file plus §15 of this file). In Session 1 commit this file as `docs/00-master-prompt.md`, `02` as `docs/01-decision-log.md`, `phases/` and `appendices/` under `docs/`, the Ecosystem Integration Specification v1.2 unchanged as `docs/ecosystem/infrabyx-integration-spec.md`, **the IPB pack unchanged as `docs/ipb/` *(v1.1)*** (read `docs/ipb/00_README.md` in every session before the phase file), and `_research/00_Authoring_Conventions.md` as `docs/reference/authoring-conventions.md` (phase and appendix files cite it as "conventions §n"; where it differs from this master, this master and §18 resolutions win — e.g., its §14 export layout is superseded by Appendix K, X-07). The condensed two-document edition (`condensed/`) carries the same content for owners who prefer one master and one runbook.

> **Note on the brief.** The owner's role paragraph says "for the development of Udofin". That is a copy-paste slip: this pack builds **LawDocs**. Udofin, Finbyx, Equator and LawDocsComply appear only as ecosystem neighbours.

---


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

> **Infrabyx Platform Baseline Standard (IPB) v1.0 applies.** This product adopts IPB-01 to IPB-13 (`docs/ipb/`) in full. Where this pack and the IPB differ, this pack may only be stricter; any other difference is an `IPB-DEV-nn` entry in the decision log. Runtime is Node.js 24.22.1 (IPB-D-01). All external services sit behind IPB-01 ports with at least two adapters (IPB-D-02). The AI employee is Vidhi AI on the shared kernel (IPB-D-03). The public website, super-admin Studio, blog, resources, cookie consent, footer and standard pages follow IPB-04; policies follow IPB-05; accessibility IPB-06; settings tree and "i" help IPB-07; vendor assurance room IPB-08; engineering governance IPB-09; APIs and events IPB-10; environment and seeds IPB-11 (super admin `rjnprajapati@gmail.com`; seeds never run in production); future-readiness flags IPB-12. Product-specific additions are listed in the product's "IPB adoption notes" section.

*(v1.1)* The clause above is pasted verbatim from IPB `00_README.md` §3 and is binding. LawDocs' adoption notes are §21 of this file. In the repository, commit the IPB pack as `docs/ipb/` and the Ecosystem Specification v1.2 as `docs/ecosystem/`; Claude Code reads `docs/ipb/00_README.md` in every session before a phase file. The reference choices in §5.1 (Razorpay, Bedrock India, Keycloak, Leegality-type eSign aggregators, JioCX) remain the **reference adapters**; each port named in §21.1 has at least one alternative adapter kept green in CI.

### 5.1 Stack (D-01)

| Layer | Choice |
|---|---|
| Monorepo | pnpm + Turborepo, TypeScript strict, shared ESLint/Prettier, Changesets |
| Web apps | Next.js 16 (App Router) + React 19; shadcn/ui + Tailwind on LawDocs design tokens (Appendix C); TanStack Query/Table; i18next; `apps/public` server-rendered/static, multi-brand (NN-31) |
| Mobile | Expo (React Native) with EAS builds and controlled OTA updates; one codebase, brand flavours (LawDocs, Consumer Help brand); mobile BFF `/m/v1` (P22) |
| API | NestJS 11 modular monolith (`apps/api`), one NestJS module = one PostgreSQL schema = one bounded context; OpenAPI 3.1 generated from Zod; AsyncAPI 3.0 for events |
| Runtime | **Node.js 24.22.1** pinned in `.nvmrc`, `package.json` `engines`, Dockerfiles and CI (IPB-D-01; IPB-01 §01.4.1) *(v1.1 — supersedes "Node.js 24 LTS [VERIFY at P00]": the IPB fixed the exact version; Node 26 only through a dated ADR, not before Q2 2027, flag `fut.node26-runtime`)* |
| Database | PostgreSQL 16+ (18 preferred) with enforced RLS; Drizzle or Kysely; `NUMERIC` + `decimal.js` for money; pgvector for tenant-scoped embeddings. *(v1.1)* PostgreSQL is the **only** database engine (IPB-D-02); no second engine for any module; portability rules IPB-01 §01.4.6 (no vendor-specific extensions outside an allow-list; logical-replication move drill in P20 FR-P20-52) |
| Hosting | Production: AWS ap-south-1 (Mumbai), DR ap-south-2 (Hyderabad); RDS/Aurora PostgreSQL; S3 with SSE-KMS, versioning and **Object Lock** for originals, signed files and evidence. Non-production may use Supabase PostgreSQL (database only; IPB-01 §01.4.11). *(v1.1)* AWS ap-south-1 is the **reference** production deployment, not a lock-in: every cloud capability sits behind an IPB-01 port (`STORAGE`, `KMS`, `SECRETS`, `QUEUE`, `DNS_CDN`, `OBSERVABILITY`…), containers are built once (`infrabyx-app` Helm chart), Terraform modules exist per cloud (`infra/terraform/{aws,azure,gcp}`) with one output contract, Object Lock equivalents are mapped per cloud (IPB-01 §01.4.7), and P20 §4H adds the portability drills (FR-P20-52…55). The legacy Vite/Express/MongoDB/Railway deployment is migrated and decommissioned in P00 with a 301 map (R5 found client-side rendering that crawlers see as empty, non-www sitemap URLs that fail, and robots blocking `/buy/` pages the sitemap lists). |
| Workflows and jobs | Temporal (signing ceremonies, negotiations, hearings and deadline clocks, exports/imports, agent missions, service orders); Redis (cache, rate limits, short jobs) |
| Search | OpenSearch (tenant-filtered indices, Indic analysers) with PostgreSQL full-text fallback |
| Identity | Keycloak (OIDC/SAML, OTP, passkeys/WebAuthn, MFA, SCIM): realm `ld` (customers, counterparties, professionals, partners) and realm `ld-staff` (federated to the group Entra ID; provisioned from OH10) |
| Authorisation | Cerbos (RBAC + ABAC policies as code; Appendix D) |
| Rules | GoRules ZEN decision tables + CEL behind `RULES_PORT` (P03) |
| Documents | docxtemplater (DOCX), `@infrabyx/redline` (OOXML track changes, NN-37), Gotenberg/LibreOffice (PDF, PDF/A-2b/3b); optional co-authoring in the customer's own Microsoft 365 or Google Workspace; optional ONLYOFFICE/Collabora WOPI behind a licence ADR |
| Document intelligence | `packages/dix`: deterministic OCR (Tesseract/PaddleOCR with Indic models) for print; Claude vision for handwriting and screenshots; translation adapters behind `TRANSLATE_PORT` (P05) |
| AI | `packages/ai` provider-neutral gateway: Claude via Amazon Bedrock India for confidential data classes; Anthropic API only for public or non-personal content; model registry and version pinning; MCP server and client (P09, D-14). *(v1.1)* Adapters named per IPB-03 §03.4.3: `bedrock_claude_in` (reference, `IN-ZR`), `anthropic_direct` (GLOBAL, PUBLIC/INTERNAL only), `azure_openai_in` (Central India) / `openai_direct`, `vertex_gemini_in` (asia-south1), `xai_grok` (GLOBAL, PUBLIC only), `sarvam` and `bhashini` (Indic text and speech), `self_hosted_vllm` (sovereign open-weight); data-class routing bands `open` / `in_zero` / `self` (IPB-D-06); `IMAGE_GEN` port (marketing and CMS images only, labelled AI-generated, human review before publish — `02` §4 row 23); `SPEECH`, `EMBEDDING`, `RERANK` ports. Vidhi kernel `packages/vidhi` (IPB-D-03) hosts skills, missions, scheduled tasks and notebooks; `packages/agents` (P09) becomes the LawDocs skill and agent catalogue on that kernel |
| Payments | Razorpay hosted checkout, Subscriptions, e-mandate, Route split settlement, Smart Collect — through OH8 via `BILLING_PORT` (NN-22) |
| Communications | `packages/notify`: email (SES / Brevo transactional), SMS, voice, WhatsApp and RCS via JioCX and other DLT-registered CPaaS adapters (Appendix J), in-app, push |
| Observability | OpenTelemetry traces, metrics and logs; PII scrubbing (NN-32); SIEM export |
| Shared IPB packages *(v1.1)* | `packages/vidhi` (AI kernel, IPB-03), `packages/cms` (headless CMS, IPB-04), `packages/brand` (Brand Studio, `brand_pack`, IPB-D-10), `packages/hlp` ("i" glossary registry, IPB-07), `packages/trust` (Vendor Assurance Room mirror, IPB-08), `packages/feedback` (feedback widget, IPB-04 §04.3.11), `packages/marketing` (`mkt.*`, consent-gated tags and pixels), `packages/consent-ui` (cookie CMP). Existing LawDocs modules `web`, `hlp`, `ai`, `agt`, `eng` **consume** these packages (OP-1); they do not fork them |
| Containers and infrastructure *(v1.1)* | Multi-stage Dockerfiles (distroless Node 24.22.1 base), shared Helm chart `infrabyx-app`, Terraform modules per cloud with identical names and outputs (IPB-01 §01.4.8–01.4.9); per-PR preview environments (IPB-09 §09.3.C; P23 FR-P23-07) |
| Calendar *(v1.1)* | `CALENDAR_PORT`: internal calendar module with ICS feeds (reference, authoritative for hearings and deadlines) + adapters Microsoft Graph Calendar, Google Calendar, CalDAV (IPB-01 catalogue; P19 FR-P19-85) |

### 5.2 Repository layout

```
apps/       public  web  delivery  console  mobile  api
packages/   tenancy audit config rules workflow notify docgen redline dix ai agents
            connectors export ui tokens i18n a11y contracts (generated from infrabyx-contracts)
            vidhi cms brand hlp trust feedback marketing consent-ui   # (v1.1) IPB shared packages
modules/    (inside apps/api/src) core iam kyc org cfg rul wf ntf msg dms dix tpl drf clm sgn
            ai agt pld lit ipm gov hr lgo bsv tax chp mkp aca bil sav sdc cvl int xpt web hlp
            rpt mob eng
db/         migrations (expand-contract), ownership.yaml, seeds (synthetic)
content/    templates, clauses, eligibility rows, legal rules, glossary (as data, versioned)
docs/       00-master-prompt.md, 01-decision-log.md, ipb/ (IPB v1.0, read first — v1.1), ecosystem/, phases/, decisions/ (ADRs),
            interfaces/, compliance/ (verification-log.md, ropa, dpia), runbooks/
tests/      unit, integration, contract, acceptance/pxx/*.feature, nn/NN-xx_*.spec.ts,
            journeys/J-xx, golden/ (archives, redlines, documents), a11y/
env/        .env.example, SEED_CREDENTIALS.md (gitignored), README.md    # (v1.1) IPB-11
infra/      terraform/{aws,azure,gcp}, helm/, policy/                   # (v1.1) IPB-01, IPB-09
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
- **Shared kernel *(v1.1)*:** Vidhi runs on `packages/vidhi` (IPB-03). Each of the 37 agents is a bundle of **skills** declared by `skill.manifest.json` (key `ld.<skill>`, inputs/outputs, tool allow-list, `data_class_max`, `autonomy_ceiling`, `locked_actions`, `prompt_key`, `eval_set_ref`, `owner_role`, `surfaces`); tasks `tsk_`, missions `msn_`, scheduled tasks `sch_` with RFC 5545 `RRULE` + `DTSTART` + time zone + `EXDATE` and **run-time permission re-check** (skip with `IPB-VID-020` after revocation; pause after `vidhi.sched.max_skips`); autonomy promotion L2→L3 needs ≥ 50 approved L2 runs in 90 days at ≥ 95 % approval and zero guardrail incidents — LawDocs keeps its stricter FR-P09-40 thresholds (200 actions) as an `IPB-DEV`-free tightening; automatic demotion on any locked-action attempt. The IPB-03-71 locked list (payments, filings, eSign initiation, deletions, external sharing, price changes, regulator messages…) plus LawDocs' additions (sending to counterparties, court or registry upload, public publication) can never be automated at any level. Mapping of P09/Appendix H vocabulary to the kernel: Appendix H §H.15.
- **Providers *(v1.1)*:** adapters in §5.1; routing by data class (`PUBLIC`/`INTERNAL` → `open` band may use GLOBAL adapters; `PERSONAL`/`CONFIDENTIAL`/`SENSITIVE` → `in_zero` band, India-resident zero-retention only; tenant floor `ai.routing.india_only_all_classes`); BYOK per tenant on eligible plans (`ai.byok.*`); kill switches `ai.kill.*`. D-14 stands: Claude remains the reference model family; other providers are adapters behind evaluation gates.
- **Images *(v1.1)*:** `IMAGE_GEN` is available only to `apps/public` and `apps/console` (CMS media, marketing creatives, blog hero images), never for evidence, documents or identity artefacts; every generated image is labelled as AI-generated with a C2PA-style sidecar before storage (IT Rules synthetically generated information labelling [VERIFY current rule text]), and publication needs human review (`cms.media.ai_images.require_review = true`, locked) — owner decision `02` §4 row 23.
- **Knowledge notebooks *(v1.1)*:** P09 §4B platform and tenant notebooks adopt the IPB-03 notebook model (`nbk_` sources with hash, `fetched_at`, `data_class`, `acl`; outputs Q&A, FAQ, briefing, timeline, Mermaid mind map, flashcards, slide outline → PPTX, audio overview with transcript, each a `res_` artefact with provenance). Cross-tenant sharing of a notebook is a locked action.

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
| `CALENDAR_PORT` *(v1.1)* | Hearings, deadlines, reminders, agent schedules in the user's calendar | Internal calendar + ICS feed (authoritative) → Microsoft Graph Calendar → Google Calendar → CalDAV (IPB-01 catalogue; P19 FR-P19-85) |
| `IMAGE_GEN_PORT` *(v1.1)* | Marketing and CMS images (labelled, human-reviewed) | Bedrock image models ap-south-1 [VERIFY availability] → Vertex Imagen asia-south1 → OpenAI image API (PUBLIC prompts only) |
| `TAG_MANAGER_PORT` *(v1.1)* | Consent-gated tag container on `apps/public` only | `none` (default) → `gtm_server` (self-hosted server-side container) → `gtm_web` (owner decision IPB open item 5) |
| `TRUST_PORT`, `SUPPORT_PORT`, `BACKLOG_PORT`, `HR_PORT` *(v1.1)* | Vendor documents mirror; feedback → tickets and backlog; careers applications | OH14.6 / OH6 / OH product backlog / OH10 HTTP clients → internal fallbacks (read-only mirror, lightweight ticket table, GitHub Issues, applications table) |
| `CONSENT_PORT`, `AV_PORT`, `MEDIA_PORT`, `EGRESS_PORT`, `PLAGIARISM_PORT`, `LAW_REGISTER_PORT` *(v1.1)* | Consent ledger; upload scanning; image/video processing; SSRF-guarded outbound fetch; content-import duplicate check; stale-citation lookups | Internal `consent` module → registered Consent Manager API (from 13 Nov 2026); ClamAV → cloud scanner; sharp/ffmpeg → Cloudinary (PUBLIC only); internal egress proxy; internal shingling → Copyscape; LDC rules register → local snapshot |

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
| Companion packs | *(v1.1)* IPB v1.0 (`docs/ipb/`, binding baseline), Ecosystem Spec v1.2 (canonical for cross-product contracts; absorbed Appendix Y), Operations Hub v1.1, LawDocsComply v1.3, Equator v3.2, Finbyx v1.6, Udofin v1.3 (v1.0 cited Spec v1.1, OH v1.0, LDC v1.2, EQ v3.1) |
| Live sites | lawdocs.in (186 sitemap URLs; redirect map in P00/P21), trainings.lawdocs.in (Graphy, 16 courses) |

---

## 17. Glossary (short; the full "i" registry is P21 and Appendix N)

**ASP** — Application Service Provider that integrates eSign under contract with an ESP. **ESP** — eSign Service Provider licensed by CCA. **OVSE** — offline verification-seeking entity under Aadhaar regulations. **eStamp** — electronic stamp certificate issued through authorised channels. **CNR** — unique case number in eCourts. **Type copy** — a typed transcription of a handwritten or image document, filed with the original. **s.63 certificate** — the certificate for electronic records under the Bharatiya Sakshya Adhiniyam 2023. **Maker / Checker** — the person who prepares and the person who approves; never the same for controlled actions. **Delivery grant** — a client-approved, time-bound permission for LawDocs staff or a professional to work in the client's workspace. **Retainer** — a continuing engagement with agreed scope, hours and SLA. **SoR** — system of record.

---

## 18. Document precedence and cross-file resolutions (binding)

**Precedence on conflict** *(v1.1)*: this master → **IPB v1.0 (`docs/ipb/`)** → **Ecosystem Integration Specification v1.2** (prevails for cross-product contracts) → `02` decision log → Appendix G (legal rules) → Appendix F (instrument eligibility) → Appendix B (data model, events, errors) → Appendix A (state machines) → Appendix D (roles and access) → Appendix R (settings) → Appendix C (IA and screens) → the phase file → other appendices → research notes. The Ecosystem Integration Specification prevails for cross-product contracts; a needed change is raised through a change request in the Appendix Y format (Appendix Y's own content is now registered in Spec v1.2 *(v1.1)*), never improvised. A product may tighten an IPB rule, never loosen it; any other difference is recorded in `02` §2.4 as `IPB-DEV-nn` with reason and owner *(v1.1)*. Where a phase file and an appendix disagree on a detail the phase owns (its tables, its defaults), the owning phase wins unless an NN rule says otherwise (X-11).

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
| *(v1.1)* All companions | The 26 October 2026 group upgrade delivered these requests: Ecosystem Spec v1.2 registered Appendix Y and the ten IPB-10 proposed events; OH v1.1, LDC v1.3, EQ v3.2, FBX v1.6, UDF v1.3 adopted the IPB. Remaining LawDocs-originated asks are tracked in Appendix W §W.4.7 (`OI-IPB-*`). | IPB `00_README.md` §5; Appendix X, Y |

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
| D-18 *(v1.1)* | = IPB-D-01: Node.js 24.22.1 pinned; 26.12.1 only through a dated ADR after dependency verification (not before Q2 2027). |
| D-19 *(v1.1)* | = IPB-D-02: ports + reference stack; PostgreSQL the only database engine; every cloud/vendor capability behind a port with ≥ 2 adapters; container-ready; reference production AWS Mumbai with DR Hyderabad; Supabase database-only in non-production. |
| D-20 *(v1.1)* | = IPB-D-03: one AI employee brand, Vidhi AI, on the shared kernel with product skills and autonomy ceilings; display-name override only on white-label plans (not offered on LawDocs core plans in v1). |
| D-21 *(v1.1)* | = IPB-D-04: seed credentials in `env/SEED_CREDENTIALS.md` (24+ character generated passwords); super admin rjnprajapati@gmail.com; production refuses seeds; first production login forces password change and MFA. |
| D-22 *(v1.1)* | = IPB-D-05: NestJS modular monolith; module = schema = bounded context (already LawDocs' §5.3 rule). |
| D-23 *(v1.1)* | = IPB-D-06: multi-provider AI with data-class routing; confidential and regulated classes only to India-resident zero-retention endpoints. D-14 (Claude reference) unchanged. |
| D-24 *(v1.1)* | = IPB-D-07: payment-gateway neutral; Razorpay reference; hosted checkout only; OH8 billing engine of record (already NN-22). |
| D-25 *(v1.1)* | = IPB-D-08: every product ships a public website with super-admin CMS, Brand Studio, Pricing Studio, blog, vlog, resources, cookie CMP, standard footer and pages (P21 extended). |
| D-26 *(v1.1)* | = IPB-D-09: Vendor Assurance Room with cadenced uploads; OH14.6 system of record; LawDocs mirror under Settings › Security & trust. |
| D-27 *(v1.1)* | = IPB-D-10: shared `brand_pack` object for white-label and multi-brand (LawDocs uses it for the `[Consumer Help Brand]` site and any future resale). |
| D-28 *(v1.1)* | = IPB-D-11: distinct visual identity per product within WCAG 2.2 AA contrast guard-rails — LawDocs: deep navy `#0B2545` + saffron `#E07A1F`, Inter + Source Serif (`design/UI_UX_Design_Brief_v1.1.md`). |
| D-29 *(v1.1)* | = IPB-D-12: Operations Hub staff segregated by product scope in addition to legal entity (LawDocs sends `product_scope = LD` on every OH call). |

---

## 21. IPB adoption notes (LawDocs) *(v1.1)*

### 21.1 Ports LawDocs uses (IPB-01 catalogue; reference adapter → alternatives kept green in CI)

| Port | Reference adapter | Alternative(s) | Where in this pack |
|---|---|---|---|
| IDENTITY, AUTHZ | Keycloak 26 (realms `ld`, `ld-staff`); Cerbos | Zitadel; OPA (policy mirror) | P01, P02, Appendix D |
| STORAGE, KMS, SECRETS | S3 + Object Lock; AWS KMS; Secrets Manager | MinIO / Azure Blob immutability / GCS retention; Vault PKCS#11; Vault KV | P00, P04, P20, P23 |
| QUEUE, WORKFLOW, CACHE | Redis/BullMQ; Temporal; Redis | NATS JetStream; Temporal Cloud or self-hosted; Valkey | P00, P03 |
| SEARCH, VECTOR, EMBEDDING, RERANK | OpenSearch; pgvector; Bedrock Titan/Cohere embed (IN); self-hosted bge-reranker | PostgreSQL FTS; Qdrant; Voyage/OpenAI (PUBLIC only); none | P04, P09, P21 |
| EMAIL, SMS, WHATSAPP, PUSH, VOICE, NOTIFY | SES; JioCX (DLT); Meta Cloud API via BSP; Expo/FCM/APNs; Exotel; `packages/notify` | Brevo; Kaleyra/Gupshup; Gupshup WABA; direct FCM/APNs; Kaleyra Voice; OH notification service | P00, P19, Appendix J |
| ESIGN, ESTAMP, KYC, COMPANY_DATA, DIGILOCKER, OVSE | Aggregator ASP (D-12); contracted ACC/aggregator; licensed KYC vendor; licensed MCA-data vendor; DigiLocker requester; OVSE | Second ESP route; manual attach + UIN check; alternative licensed vendor; GSP | P01, P08, P14, Appendix I |
| LLM, IMAGE_GEN, SPEECH, TRANSLATE, OCR | Bedrock Claude India; Bedrock image models [VERIFY]; Bhashini + Transcribe/Polly; Bhashini [VERIFY]; Tesseract/PaddleOCR | §5.1 AI row; Vertex Imagen; Sarvam/Azure Speech; Google/Azure translate; Claude vision | P05, P09 |
| DOCGEN, PDF | docxtemplater + `@infrabyx/docgen`; Gotenberg/LibreOffice | Carbone; pdf-lib + PAdES via KMS | P06, P08 |
| PAYMENTS, BILLING | Razorpay hosted checkout via OH8 `BILLING_PORT` | PayU; Cashfree (OH8 switch, never product-local) | P17 |
| CALENDAR, WORKSPACE | Internal calendar + ICS; Microsoft Graph | Google Calendar/CalDAV; Google Workspace | P11, P13, P18, P19 |
| ANALYTICS, TAG_MANAGER, FEATURE_FLAG, OBSERVABILITY, ERROR_TRACKING, DNS_CDN | Self-hosted Matomo/PostHog (IN); `none`; OpenFeature + file/Unleash; OTel → Grafana stack; Sentry self-hosted; Route 53 + CloudFront | Plausible; `gtm_server`; Flagsmith; Datadog (GLOBAL, INTERNAL only); GlitchTip; Cloudflare | P21, P23 |
| RULES, CONSENT, AV, MEDIA, EGRESS, PLAGIARISM, LAW_REGISTER | GoRules ZEN + CEL; internal `consent`; ClamAV; sharp/ffmpeg; internal egress proxy; internal shingling; LDC register | CEL-only; registered Consent Manager (13 Nov 2026); GuardDuty malware; Cloudinary (PUBLIC); NAT egress rules; Copyscape; local snapshot | P03, P04, P21 |
| TRUST, SUPPORT, BACKLOG, HR, CRM, ODR, ACCOUNTING, COURT_DATA, TRADEMARK_DATA | OH14.6; OH6; OH backlog; OH10; OH3; Equator; Tally Prime; two licensed aggregators; licensed TM partner [VERIFY] | Internal mirror; internal tickets/Zendesk; GitHub Issues; applications table; Brevo; other ODR institutions; Zoho Books/CSV; manual CNR refresh; WIPO GBD | P11, P12, P16, P18, P19, P21, P23 |

LawDocs product ports not in the IPB catalogue (registered per IPB-01 §01.4.4.0 with ADRs): `COURT_DATA_PORT`, `TRADEMARK_DATA_PORT`, `OVSE_PORT`, `DIGILOCKER_PORT`, `GSTIN_PORT`, `ODR_PORT`, `ACCOUNTING_PORT`, `HRMS_SOURCE_PORT`, `CUSTOMER_CRM_PORT`, `DSC_PORT`, `RCS_PORT` (Appendix I §I.2). LawDocs publishes `packages/connectors/esign/lawdocs` as the group's reference ESIGN adapter **only as a hosted hand-off** (NN-06, X-05, D-12A): other products receive status and evidence, never a sublet eSign capability. **IPB-DEV-01** records this nuance (`02` §2.4).

### 21.2 Settings tree, "i" registry, feedback, What's new, search

The 20-node IPB-07 tree is mapped to LawDocs screens in Appendix C §C.4.17A; new nodes are built by P03 (Appearance, Accessibility, Feedback, Tutorials & help, What's new, About), P20 (Storage & data), P00/P23 (Audit trails), P23/P21 (Security & trust), P09 (AI & Vidhi). Help keys stay `hlp.<module>.<term>` (X-10) with CI lint `hlp-lint` and the regulatory-reference panel (P21 FR-P21-120A). Feedback widget on every public page and authenticated surface (P21 §4S). Cmd+K refuses Aadhaar, PAN, card and account numbers (FR-P03-36A).

### 21.3 Website, Studio, policies, vendor assurance, engineering

IPB-04 pages added or confirmed in P21 §4R (Investors toggle, Team, Leadership, Governance, Resources library, Changelog, Compare, Case studies, Sitemap); Studio is the existing Content Studio renamed **Website Studio** for IPB-04 scope with **Document Studio** for templates (IPB-04 §04.7 LD note). Policies: Appendix O §O.17 adds POL-LD-18…22. Vendor Assurance Room mirror: P23 §4I FR-P23-60…62 and P21 FR-P21-150. Engineering: `cc/<phase>-<slug>` branches, beta programme, release-notes pipeline (P23 FR-P23-03A, FR-P23-24A, FR-P23-59).

### 21.4 Future-ready flags (IPB-12) that touch LawDocs

| Flag | Default | Owner | Module that absorbs it |
|---|---|---|---|
| `fut.passkeys-default` | OFF → ON by Q2 2027 | `PLT_SECURITY_OFFICER` | `iam` (P01) |
| `fut.webauthn-conditional-ui` | ON | `PLT_SECURITY_OFFICER` | `iam` |
| `fut.pqc-hybrid-sign` | OFF | `PLT_SECURITY_OFFICER` | `sgn` evidence packs (P08) — hybrid ML-DSA signatures when a CA issues them |
| `fut.cbom-export` | OFF | `PLT_SECURITY_OFFICER` | `eng` (P23) |
| `fut.digilocker-vc`, `fut.vc-verify` | OFF | LD lead | `kyc` (P01) |
| `fut.dpdp-consent-manager-api` | OFF → ON after 13 Nov 2026 | `PLT_DPO` | `kyc` consent ledger (P01), `CONSENT_PORT` |
| `fut.dpdp-consent-ledger` | ON | `PLT_DPO` | `kyc` |
| `fut.ai-provenance-label` | ON (locked) | `PLT_LEGAL_REVIEWER` | `ai`, `web` media (P09, P21) |
| `fut.ai-inventory`, `fut.sbom-aibom-publish`, `fut.guardrails-v2` | ON | `PLT_SECURITY_OFFICER` / `PLT_RELEASE_MANAGER` | `ai`, `eng` |
| `fut.mcp-server` | OFF per tenant | Platform architect | `ai` MCP server (P09 FR-P09-48) |
| `fut.a2a-agent-card` | OFF | Platform architect | `int`/`agt` (Appendix H §H.12A) |
| `fut.webmcp-page-tools` | OFF | `PLT_RELEASE_MANAGER` | `apps/public` free tools (P21) |
| `fut.edge-local-inference`, `fut.sovereign-model-primary`, `fut.confidential-inference` | OFF | AI lead / `PLT_SECURITY_OFFICER` | `packages/ai` adapters |
| `fut.node26-runtime`, `fut.nest12-esm`, `fut.pg19`, `fut.temporal-nexus` | OFF | `PLT_RELEASE_MANAGER` / architect | `eng` runtime ADRs (P23) |
| `fut.http3-edge`, `fut.webhooks-standard-envelope`, `fut.api-errors-rfc9457` | ON | `PLT_RELEASE_MANAGER` / architect | `int` (P19) |
| `fut.api-signatures-rfc9421` | OFF | architect | `int` partner API |
| `fut.ecourts-api` | OFF | LD lead | `lit` `COURT_DATA_PORT` (P11) — switch from aggregators when an official API is published |
| `fut.stamp-national-regime` | OFF | LD lead | `sgn` `rules.estamp.*` (P08) — on enactment of a national stamp bill [VERIFY] |
| `fut.outsourcing-evidence-pack` | ON | `PLT_SECURITY_OFFICER` | `trust` mirror (P23 §4I) |

### 21.5 Claude artefacts (IPB-13)

Optional, never binding: phase plans may be drafted as Claude Docs for owner review before being committed as Markdown; Appendix A state machines and Appendix C menu trees may be rendered as Mermaid in `docs/`; the Vidhi notebook "slide outline" output uses the same PPTX export path as IPB-13; dashboards for the P23 Engineering console may be prototyped as interactive artefacts, then rebuilt in `apps/console`. Anything in-product follows IPB-13 §13.3 (no third-party scripts, no tenant data in artefacts hosted outside the platform).

*End of master prompt.*
