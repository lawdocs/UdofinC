# Phase P21 — Marketplace, Retainers and FinLegal Academy

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00, P01** (tenancy, identity — including light-weight **buyer accounts** for organisations without a subscription), **P02** (settings), **P07** (DMS, eSign envelopes, engagement letters), **P04** (tasks, notifications, calendar), **P18** (integration gateway, Academy feed connector), **P20** (shared quote/order/invoice components, `BILLING_PORT`, entitlements, presentation catalogue patterns), **P23** (public site shell, SEO).
> - **External:** Operations Hub **OH8** (first-party service SKUs, quotes, orders, invoices, Razorpay), **OH9** (group professional directory: verification, `ProfessionalEmpanelled`, `ProfessionalSuspended`), **OH3** (leads), **OH6** (complaints about LawDocs services), **OH14** claims gate; LawDocs Trainings LMS (trainings.lawdocs.in).
>
> **Sequencing:** Starts after P20 sprint 2 (shared commerce components frozen). Third-party provider commerce (Model M2/M3, §4C) ships behind flags that stay OFF until counsel clears each profession (D-06; OI-P21-02…05). First-party LawDocs services and the Academy listing ship first.
>
> **Binding appendices:** O (Marketplace Services Catalogue and Professional Rules), N (streams RS-LDC-12…RS-LDC-22), X (OH addendum §X.8–§X.9), G (legal rules LR-BCI-*, LR-ICAI-*, LR-RBI outsourcing), M (export of engagement records).
>
> **Requirements covered:** R-035, R-036, R-037, R-072 (retainer contract basis), R-100, R-020 (service explainers), R-038 (deliverable sharing), R-021 (engagement records in export).
>
> **Estimated effort:** 7 two-week sprints, squad of 9 (marketplace backend 3, frontend 3, Academy/integration 1, QA 1, legal-ops analyst 1). *(v1.1: +2 sprints for v1.1 scope (partner network, new categories, firm accounts) — 9 in total)*


**v1.1 changes (25 October 2026)** *(v1.1)*

- New §4N partner network for foreign jurisdictions and global professionals (D-44; Appendix Y §Y.5): partner types, due diligence, per-country × profession × service commercial switches (all OFF until counsel), jurisdiction conflict checks, scorecards (FR-P21-55–FR-P21-61).
- New §4O service categories: AI governance, ESG/BRSR and assurance, litigation and legal-matter support, global entity services, cross-border tax — with eligibility and independence rules (FR-P21-62–FR-P21-66).
- New §4P practitioner-firm accounts (G5 TM-396) and §4Q gap-driven service suggestions (FR-P21-67–FR-P21-70).
- Partner roles use the lead names (`prt_admin`, `prt_content_reviewer`, `prt_delivery_professional`, `prt_viewer`; Appendix D to reconcile with P25).
- Appendix O extended with categories 16–20, foreign-profession rule rows and partner programme terms; new screens, settings, scenarios and open items.

---

## 1. Objective and business outcome

The LawDocsComply Marketplace is the place where an organisation buys the human expertise that the software alone cannot provide — compliance retainers, virtual CXO support, drafting of policies, agreements, annual reports and ICAAP documents, stress testing and risk assessments, return-filing support, audit-readiness, certification readiness (SOC 2, ISO, PCI DSS), VAPT and trainings — **with or without a software subscription**. It is open to anyone without logging in (R-036), starts with LawDocs' own professionals and opens to outside providers later (R-035), and is designed so that LawDocs never breaches the professional-conduct rules that bind advocates, chartered accountants, company secretaries and cost accountants (D-06).

| Outcome | Exit-gate measure |
|---|---|
| Public, browsable catalogue | `/marketplace` lists ≥ 60 seeded first-party offerings in ≥ 12 categories (Appendix O §O.2), each with scope, deliverables, exclusions, timeline, price basis and "who this is for"; browse and search need no login; WCAG 2.2 AA |
| Services without SaaS | A non-subscriber can buy a fixed-price service in ≤ 8 clicks (buyer account + GST profile + Razorpay checkout) and receive deliverables in an Engagement Room; later conversion to a full tenant carries the engagement record across |
| Custom offerings and pricing | LawDocs delivery leads (and, when enabled, outside providers) publish offerings with their own scope, price model (fixed, milestone, retainer, hourly band, quote-only) and SLA; every offering passes legal-category and claims checks before going live |
| Retainers with SLA eSign | A retainer goes from proposal to eSigned SLA to active RM assignment (P22) in ≤ 2 working days; monthly invoices, service-hour or deliverable tracking and SLA credits run automatically |
| Professional-conduct compliance | Per-profession switches enforce listing mode, commission, ratings and call-to-action rules; advocates and CAs in practice are never listed with commerce features unless counsel clears it; CI tests prove forbidden fields cannot be rendered |
| FinLegal Academy | Courses from trainings.lawdocs.in appear in the marketplace with live price, next batch and enrolment link; corporate seat bundles can be quoted and invoiced; completion certificates flow back as compliance evidence where the learner consents |
| Billing | First-party services invoiced by the LawDocs selling entity through OH8 with GST; direct-model provider invoices captured; invoices e-mailed to buyers; refunds and disputes handled with credit notes |

---

## 2. Scope (in / out)

**In scope**

- Public marketplace (`apps/public` `/marketplace/*`), in-app marketplace (`apps/web` "Services" menu), buyer accounts, provider workspace (`apps/delivery` for LawDocs staff; provider portal for outside firms when enabled).
- Service catalogue model: categories, offerings, packages, add-ons, price models, SLAs, deliverable templates, eligibility rules by buyer entity type, conflict and independence checks.
- Provider model: first-party LawDocs teams; outside providers verified through OH9 (and LDC-specific checks); per-profession commercial and display rules.
- Engagement lifecycle: request → scoping → proposal/quote → engagement letter/SLA eSign → payment → delivery with milestones → acceptance → invoice → close → review; change requests; cancellations; disputes and refunds.
- Retainers: retainer plans, hour banks or deliverable baskets, SLA definitions and credits, monthly service reports, renewal, RM-as-maker hand-off (P22).
- Engagement Room for buyers without a tenant (secure messages, files, milestones, approvals, eSign, invoices).
- Certification-readiness services (SOC 2, ISO 27001/27701/42001/22301/9001, PCI DSS), VAPT, and the independence wall between readiness and certification.
- FinLegal Academy listing feed, corporate seats, learner-consented certificate import.
- Ratings and feedback (only where permitted), moderation, grievance officer for the marketplace.
- GST/TCS handling options per commercial model, invoices, credit notes, e-mail delivery.

**Out of scope**

- Group professional directory and empanelment (OH9) — consumed, not rebuilt.
- RM portfolio, credential vault, delivery work inside tenants (P22).
- LMS itself (trainings.lawdocs.in remains the system of record for courses, enrolments, assessments).
- Equator ADR services (never listed as a lender-side add-on; Ecosystem Spec §8.6; OH8.2 Equator rules) — the marketplace may show a neutral informational link to Equator's own site in the "Disputes" category only if the owner enables it (`mkp.category.disputes.equator_link`, default OFF).
- Payment aggregation by LawDocs (LawDocs never holds a third party's money; Razorpay Route or direct billing only).

---

## 3. Personas and permissions touched

| Role | In P21 | Notes |
|---|---|---|
| `anon` | Browse, search, filter, read offerings and provider pages (as permitted per profession), use "Ask a question" (no personal data required until contact) | No tracking cookies without consent |
| `mkp_buyer` (non-subscriber organisation user) | Create buyer account (organisation + GST profile), request/accept quotes, pay, sign engagement letters, use Engagement Room, rate (where allowed), raise disputes | Light identity: e-mail + OTP; organisation via PAN/CIN/GSTIN fetch (P01) |
| `ten_admin`, `ten_cco`, `ten_kmp`, `ten_dept_head` | Buy services inside the tenant (subject to tenant purchase approvals, P20 FR-P20-32), see engagements in Settings › Billing › Marketplace orders, grant delivery access (P22) | Purchases can be restricted to admins (`mkp.tenant.who_can_buy`) |
| `dlv_lead` | Publish/maintain first-party offerings, approve proposals and discounts within DoA, assign professionals and RMs | Maker-checker with `plt_super_admin` or a second `dlv_lead` for new offerings |
| `dlv_professional`, `dlv_rm` | Scope, propose, deliver, upload deliverables, log effort, request acceptance | Cannot approve own proposal discounts |
| `mkp_provider_admin`, `mkp_professional` | Outside provider: profile, offerings, proposals, delivery, invoices (Model M2) | Only when `mkp.providers.external.enabled = ON` and their profession's mode allows |
| `plt_super_admin` | Category tree, profession rules, commission and listing fees (via OH8 streams), moderation escalations, kill switches | |
| `plt_content_checker` (marketplace compliance reviewer) | Reviews new offerings and provider profiles for professional-conduct and claims compliance | |
| `plt_finance` | Refunds, credit notes (via OH8), settlement monitoring (Route, if enabled), TCS reporting data | |
| Marketplace Grievance Officer (designated `plt_support` with flag) | Buyer complaints about the marketplace (ack 48 h, resolve ≤ 1 month — E-Commerce (Amendment) Rules 2026 r.4(5) adopted) | Complaints about a LawDocs service route to OH6 `client_complaint` |

---

## 4. Functional requirements

### 4A. Catalogue structure

- **FR-P21-01 — Category tree** (seed in Appendix O §O.2; editable by `plt_super_admin`): 1 Compliance retainers & managed compliance · 2 Virtual leadership (vCFO, vCTO, vCISO, vCCO-support, vCS-support, vDPO, vCRO-support) · 3 Regulatory returns & filings (RBI returns preparation support, CIC data preparation, MCA filings, GST/TDS returns, IFSCA/SEBI reporting support) · 4 Policies & regulatory documentation (policy drafting by regulator and entity type, SOPs, board-approved frameworks) · 5 Agreements & legal documentation (commercial agreements, outsourcing/LSP agreements, employment agreements, NDAs — delivered per §4D rules) · 6 Board, secretarial & governance (agenda and minutes preparation, annual report drafting, board evaluation support, secretarial compliance review) · 7 Risk & capital (ICAAP document preparation, stress testing and scenario analysis, RCSA facilitation, KRI design, ALM review) · 8 Audit support (internal audit co-sourcing where permitted, audit readiness, RBIA framework design, IS audit readiness — attest work only by eligible practitioners, §4D) · 9 Data protection & cyber (DPDP readiness, DPIA, ROPA, privacy notices, CERT-In readiness, cyber policy pack, VAPT by CERT-In-empanelled auditors, SOC/SIEM advisory) · 10 Certification readiness (SOC 2 Type 1/2, ISO 27001, ISO 27701, ISO 42001, ISO 22301, ISO 9001, PCI DSS) · 11 Labour, HR & POSH (labour code registers set-up, POSH IC external member, POSH training, payroll compliance review) · 12 Co-operative society services (bye-law drafting, AGM/election support, statutory register set-up, audit-compliance rectification) · 13 Licensing & registrations (NBFC CoR application support, IFSCA registration support, SEBI intermediary registration support, PA/PPI applications — advisory only) · 14 Trainings (FinLegal Academy: compliance, DSA/DMA, CISO, KYC/AML, DPDP, POSH, board & KMP, IFSCA) · 15 Implementation & data migration (LDC set-up, question-bank tailoring, data migration, integration set-up).
- **FR-P21-02 — Offering object.** `offering`: code, title, category, provider (first-party team or provider org), **service class** (§4D), buyer eligibility (entity types, regulators, size bands; e.g., "ICAAP preparation — NBFC ML/UL, UCB Tier 3–4, banks"), description, scope inclusions, **exclusions** (mandatory field), deliverables (each with format: DOCX/XLSX/PDF/board-ready deck; linked deliverable template), inputs required from buyer (checklist), timeline (business days, from inputs-complete), price model (§4B), SLA template (for retainers), revisions included, professional(s) role level (Partner/Senior/Associate — never named ratings), language(s), delivery mode (remote; on-site add-on), related software modules ("Works best with Policy Lifecycle — included in Professional"), tutorial/FAQ, regulatory references (citations, NN-06 style), claims-register refs for any claim, status (`DRAFT → IN_REVIEW → LIVE → PAUSED → RETIRED`), version.
- **FR-P21-03 — Packages within an offering.** Up to 3 tiers (e.g., "Policy pack — Starter 5 policies / Standard 12 / Comprehensive 25") with clear differences; add-ons (e.g., "Board presentation of the policy", "Hindi translation"); configurator-style live total reused from P20 components.
- **FR-P21-04 — Search and filters.** Full-text (OpenSearch; FTS fallback) over titles, descriptions, deliverables; filters: category, buyer entity type, regulator, price model, price range, timeline, language, delivery mode, provider type (LawDocs / verified provider); sort options: relevance, price low–high, timeline, newest — **no sort by rating for professions where ratings are off**; ranking parameters disclosed on the page in descending order of importance (E-Commerce (Amendment) Rules 2026 r.5(3)(f) adopted [VERIFY applicability]); sponsored listings OFF (`mkp.sponsored.enabled`, default OFF; never for advocates, CAs, CSs, CMAs).
- **FR-P21-05 — Offering page.** Title, who it is for, outcome in plain language, scope and exclusions, deliverables with sample (redacted, synthetic) previews, inputs checklist, timeline, price and what is included, GST note ("18% GST extra; legal services by advocates to businesses are taxed under reverse charge" where applicable [VERIFY]), provider panel (first-party: "Delivered by the LawDocs Compliance Services team"; third-party: profession-permitted fields only), FAQs, related software features, "Request a quote" / "Buy now" (fixed price) / "Book a scoping call" (only where profession rules allow), "Save", "Share".

### 4B. Price models

- **FR-P21-06 — Supported models:** `FIXED` (one price, optional tiers); `MILESTONE` (deliverable-linked instalments); `RETAINER_MONTHLY` / `RETAINER_ANNUAL` (with hour bank or deliverable basket); `HOURLY_BAND` (rate card by role level with a not-to-exceed cap — first-party only by default); `QUOTE_ONLY` (scoping first); `PER_UNIT` (e.g., per policy, per return, per training seat, per employee for POSH training); `SUBSCRIPTION_SERVICE` (e.g., monthly compliance health review). Each maps to an OH8 SKU and stream for first-party services (RS-LDC-12…RS-LDC-22).
- **FR-P21-07 — Custom pricing.** Providers set their own prices within category guard-rails (min/max set by `plt_super_admin` to block anomalies, not to fix prices); negotiated quotes per buyer are allowed; discounts on first-party quotes follow OH11 delegation of authority via OH8.
- **FR-P21-08 — Transparency.** Every price shown with basis, GST statement, what is excluded, and cancellation/refund terms (Appendix O §O.6); no anchor prices; quote validity 30 days for sales quotes (OH8.4) unless the provider sets shorter.

### 4C. Commercial models and seller of record

- **FR-P21-09 — Three models** (per offering; Appendix O §O.4):
  - **M1 — First-party (LawDocs is the supplier).** LawDocs selling entity (as recorded in OH8 `selling_entity`; legal entity to be confirmed, OI-P21-06) contracts, invoices through OH8 with GST, collects via Razorpay (OH8 account), delivers through its staff. Default and only model at launch.
  - **M2 — Direct engagement (provider is the supplier; LDC facilitates).** Buyer and provider contract directly (engagement letter between them, eSigned in LDC); provider invoices the buyer in its own name and collects through its own means; LDC records the engagement, hosts the Engagement Room and charges the provider only a **listing/subscription fee** (stream RS-LDC-18) where the profession allows it. No percentage commission (D-06 default). LDC is not a party to the supply and does not collect consideration → no s.52 TCS [INTERP; VERIFY with tax counsel].
  - **M3 — Platform-collected (Razorpay Route).** Buyer pays through LDC checkout; Razorpay (authorised PA) splits to the provider's linked account and LawDocs' platform fee; LawDocs acts as an electronic commerce operator — **s.52 CGST TCS 0.5%** on net taxable supplies, GSTR-8 monthly, provider GSTIN mandatory; E-Commerce Rules duties as marketplace entity; commission allowed only for professions/service types cleared by counsel (D-06). Flag `mkp.model.m3.enabled` = OFF; requires OH8 stream gate `MARKETPLACE_COMMISSION` (new stream code, Appendix X §X.8) and a Route account.
- **FR-P21-10 — Money rule.** LawDocs never receives, holds or remits a provider's fee outside Razorpay Route's PA-regulated settlement (RBI Payment Aggregator Directions [VERIFY current master direction]); no escrow, wallet or pooled balance is built.

### 4D. Professional-conduct rules engine (D-06; Appendix O §O.5; legal rules LR-BCI-*, LR-ICAI-*, LR-ICSI-*, LR-ICMAI-*)

- **FR-P21-11 — Service classes.** Every offering is classified (reviewed by `plt_content_checker`):
  - `RESERVED_ADVOCACY` — legal advice/opinion as an advocate, representation, appearance, drafting of pleadings: may be offered **only by advocates in their own name** under Model M2; LawDocs (a company) cannot supply it [INTERP: Advocates Act 1961 ss.29, 33; *Bar Council of India v A.K. Balaji* (2018) 5 SCC 379 on "practice of law" including non-litigious work — VERIFY with counsel].
  - `RESERVED_ATTEST` — statutory audit, tax audit, secretarial audit (Companies Act s.204; LODR Reg 24A), certifications reserved to practising CAs/CSs/CMAs, IS audit certifications where a regulator requires a qualified auditor: only by eligible practising professionals/firms in their own name (M2), with independence checks (FR-P21-14).
  - `ADVISORY_COMPLIANCE` — compliance management, documentation, policy drafting support, regulatory research, return-preparation support, governance support, training, readiness assessments: may be supplied by LawDocs (M1) or providers (M2/M3).
  - `TECHNICAL` — VAPT, security engineering, implementation, data migration: M1/M2/M3; VAPT for REs flagged "CERT-In empanelled auditor required where the regulator mandates" [VERIFY per regulator].
  - `TRAINING` — Academy and corporate training: M1 (LawDocs Trainings) and M2.
- **FR-P21-12 — Profession modes** (settings `mkp.profession.<code>.*`, Governed, changed only with counsel opinion reference):

| Profession | Default listing mode | Commission | Paid listing | Ratings/reviews | CTA allowed | Notes |
|---|---|---|---|---|---|---|
| Advocate / law firm | `DIRECTORY_RULE36` (Schedule fields only, alphabetical/random order, disclaimer) — inside marketplace only on the "Legal professionals directory" page, never inside commerce listings | OFF (hard) | OFF (hard; OH8 deny list) | OFF (hard) | "Send an enquiry" only if counsel clears; default none | BCI Rules Part VI Ch II r.36; *Sulekha.com v P.N. Vignesh* SLP(C) 25794/2024 pending; BCI directives Mar 2025 |
| Chartered accountant in practice / CA firm | `OFF` (not listed) [ICAI ESB announcement 23 Oct 2019: no listing on application-based aggregators] | OFF | OFF | OFF | none | Clauses (2), (3), (6), (7) Part I First Schedule, CA Act 1949; re-check ICAI 2026 position (OI-P21-03) |
| Company secretary in practice / firm | `OFF` pending ICSI opinion | OFF | OFF | OFF | none | ICSI Guidelines on advertisement/aggregators [VERIFY] |
| Cost accountant in practice | `OFF` pending ICMAI opinion | OFF | OFF | OFF | none | [VERIFY] |
| Actuary | `OFF` pending IAI opinion | OFF | OFF | OFF | none | [VERIFY] |
| Insolvency professional / registered valuer | `OFF` | OFF | OFF | OFF | none | IBBI codes [VERIFY] |
| Non-practising qualified professionals, consulting firms (non-attest), cybersecurity firms, certification consultants, HR/POSH trainers and external members, technology firms | `FULL_MARKETPLACE` | Allowed (M3) when enabled | Allowed | Allowed with moderation | Buy / Quote / Book call | Verification per Appendix O §O.3 |
| LawDocs first-party teams | `FULL_MARKETPLACE` | n/a | n/a | Allowed (aggregate CSAT only, with method) | Buy / Quote / Book call | LawDocs staff who are advocates/CAs act as employees of a company delivering `ADVISORY_COMPLIANCE`, never `RESERVED_*` services in LawDocs' name [INTERP; VERIFY] |

  The render layer uses a fixed response schema per mode; CI fails if a field outside the mode's allow-list (ratings, fees, photos, "top", "premium", "featured", "verified expert", success rates, client names) can be rendered for a restricted profession (test `NN-20_profession_render_allowlist`).
- **FR-P21-13 — RE-buyer guard-rails** (from buyer entity type, P15): for RBI REs, offerings that would amount to outsourcing **core management functions** — policy formulation decisions, internal audit (except permitted co-sourcing of experts), compliance function, KYC compliance, credit sanction, investment-portfolio management — are shown with a mandatory notice and are re-scoped as *support to the RE's own officer*: e.g., "vCCO support" means the RE's designated CCO remains its employee and owner of decisions and reports (RBI outsourcing directions, e.g., Rural Co-operative Banks – Managing Risks in Outsourcing Directions 2025 para 11, RBI/DOR/2025-26/318; NBFC equivalent [VERIFY para]); internal-audit offerings for NBFCs within the internal-audit-function directions are labelled "co-sourcing of specialist expertise only, with report ownership by the RE's internal audit" [VERIFY current NBFC internal audit direction]. The buyer must tick an acknowledgement (unticked by default) before ordering; the acknowledgement is stored with the engagement. For RBIA-bound buyers (banks, deposit-taking NBFCs and NBFCs/HFCs with assets ≥ ₹5,000 crore — NBFC Internal Audit Directions 2026, RBI/DoS/2026-27/464 para 39 [VERIFY]) full outsourced internal-audit offerings are hidden and the co-sourced expert is provisioned only as `ia_contributor` (X-30; Appendix O §O.8).
- **FR-P21-14 — Independence and conflict checks.** Before a proposal is sent: (a) the buyer's declared statutory auditor, secretarial auditor, internal auditor and IS auditor (from P06/P10 registers, or entered at checkout) are compared with the provider; prohibited combinations are blocked (e.g., statutory central auditor of an RE providing non-audit services restricted by RBI's guidelines on appointment of SCAs/SAs (27 Apr 2021) [VERIFY current text]; secretarial auditor of a listed entity providing services prohibited under LODR Reg 24A read with the SEBI circular of 31 Dec 2024 [VERIFY]); (b) **certification wall**: a provider (including LawDocs) that delivered readiness consulting for a standard cannot be the certifying/attesting body for the same scope (ISO/IEC 17021-1 cl. 5.2 impartiality; AICPA independence for SOC 2) — LawDocs lists certification bodies and CPA firms only as referrals with disclosed relationships and **no referral commission** unless counsel and the CB's accreditation rules allow [VERIFY]; (c) group conflicts: Equator neutrals never appear as providers (OH9 `equator_neutral` flag); (d) related-party flag where the provider is a group company (Companies Act s.188 disclosure for the buyer if applicable — informational).
- **FR-P21-15 — No solicitation by LDC on behalf of restricted professions.** No outbound marketing (OH7) promotes individual advocates/CAs/CSs; marketplace campaigns promote LawDocs first-party services and categories only.

### 4E. Provider onboarding (outside providers; flag `mkp.providers.external.enabled` OFF at launch)

- **FR-P21-16 — Verification.** Providers whose profession is regulated are verified through OH9 (`ProfessionalEmpanelled` with credentials); LDC adds marketplace-specific checks (Appendix O §O.3): organisation KYC (PAN, GSTIN, CIN/LLPIN/firm deed), bank account (penny-drop via OH11/OH9 pattern) for M3, PI insurance where required, data-protection undertaking and DPA (provider is an independent fiduciary or processor depending on model — Appendix O §O.7), information-security questionnaire for providers who will access tenant data (P22 grants), CERT-In empanelment evidence for VAPT providers, accreditation evidence for certification bodies listed as referrals, code of conduct acceptance, conflict declarations.
- **FR-P21-17 — States.** `INVITED|APPLIED → PROFILE_SUBMITTED → VERIFIED (OH9 + LDC checks) → AGREEMENT_SIGNED (marketplace terms, DPA) → LIVE → SUSPENDED (on ProfessionalSuspended, complaint upheld, document expiry) → LIVE | REMOVED`; `RETURNED` with reasons and 30-day resubmission window.
- **FR-P21-18 — Offerings review.** Each new or materially changed offering: automated lint (exclusions present, deliverables defined, price basis, prohibited words, profession allow-list) → `plt_content_checker` review (service class, RE guard-rails, claims) → LIVE; spot re-review of 10% LIVE offerings monthly [REC].

### 4F. Engagement lifecycle

- **FR-P21-19 — States** (§5.1 diagram): `REQUESTED → SCOPING → PROPOSED (quote + draft engagement letter) → ACCEPTED → CONTRACTED (engagement letter / SLA eSigned by both sides) → [ADVANCE_PAID] → INPUTS_PENDING → IN_DELIVERY → DELIVERED (per milestone) → ACCEPTED_BY_BUYER | REVISION_REQUESTED → INVOICED → PAID → CLOSED`; side states `ON_HOLD` (reason, review date), `CHANGE_REQUESTED` (scope/price delta with buyer approval), `CANCELLED` (per terms), `DISPUTED` (§4K).
- **FR-P21-20 — Scoping.** Structured intake form per offering (inputs checklist, entity details pre-filled from the tenant or buyer profile, documents upload to the Engagement Room); optional scoping call (Teams/Google Meet link via WORKSPACE_PORT, P18); Vidhi drafts a scope summary from intake for the professional to edit (NN-04).
- **FR-P21-21 — Proposal.** Quote (first-party: OH8 quote; M2: provider quote document generated by LDC from the provider's pricing) + engagement letter generated from template (Appendix O §O.6: parties, scope, exclusions, deliverables, timeline, fees, GST/RCM note, payment terms, confidentiality, data protection, IP in deliverables (buyer owns final deliverables on payment; provider keeps pre-existing know-how), limitation of liability, termination, dispute resolution, professional-conduct statements, RE outsourcing acknowledgement where relevant); proposal validity; buyer can comment and request changes inline.
- **FR-P21-22 — Contracting.** eSign via D-20 ESP adapters (Aadhaar eSign or DSC; click-wrap with OTP allowed for low-value fixed-price first-party services ≤ `mkp.contract.clickwrap_max_value` (G, default ₹50,000 [OWNER TO SET])); signed PDF with audit trail sealed in DMS (NN-09); engagement number issued.
- **FR-P21-23 — Payment terms.** Fixed price: 100% advance (default ≤ ₹50,000) or 50/50; milestones: per milestone on acceptance; retainers: monthly/annual in advance; enterprise: invoice-later with credit terms per contract. First-party payments through OH8 orders; M2 provider-controlled; M3 Route.
- **FR-P21-24 — Delivery.** Milestones with due dates (calendar, P04), tasks for the delivery team, deliverables uploaded as versioned documents (DOCX with tracked changes where the deliverable is a revision of a buyer document — P07), internal review step (`dlv_reviewer`) before release, release to buyer with notification; delivery inside a subscribed tenant can land directly in the tenant's DMS/policy register (P22 grant) — e.g., a drafted policy appears in the Policy Lifecycle as a draft version awaiting the client's approval.
- **FR-P21-25 — Acceptance.** Buyer accepts or requests revision (count against included revisions); deemed acceptance only if the engagement letter says so (default: deemed acceptance after 10 business days with two reminders [OWNER TO SET]); acceptance certificate stored.
- **FR-P21-26 — Close-out.** Final invoice, deliverables index, knowledge-transfer note, feedback request (where ratings allowed), engagement record filed in the buyer's export structure (Appendix M: `Services & Engagements/<FY>/<Engagement no – title>/`).

### 4G. Retainers (R-035, R-072)

- **FR-P21-27 — Retainer plans** (first-party seed in Appendix O §O.2.1): *Compliance Essentials Retainer* (monthly compliance calendar management, maker support for routine returns and filings, monthly status report, x hours advisory); *Regulated Entity Retainer* (RBI/SEBI/IFSCA/IRDAI obligations tracking as maker, return-preparation support, policy reviews, board compliance report drafting, regulatory-change impact notes, quarterly review call); *Secretarial Retainer* (board/committee meeting support, minutes drafting, statutory registers, MCA filings support); *Labour & POSH Retainer*; *Data Protection Retainer*; *Custom retainer*. Each defines: included services catalogue (deliverable basket) and/or hour bank, SLA matrix, named roles (RM, reviewer), meeting cadence, exclusions (e.g., litigation, attest services), price, term, notice period.
- **FR-P21-28 — SLA definitions.** Per service type: acknowledgement time, turnaround (business days), quality checks; per month: report delivery date; escalation matrix; **service credits** for missed SLAs (e.g., 5% of monthly fee per breached SLA category, capped at 20%) issued as OH8 credit notes [OWNER TO SET]. SLA clocks run on the IST business calendar of the buyer's State (holiday calendars from P04).
- **FR-P21-29 — SLA agreement eSign** within the tool (R-035): the retainer's SLA schedule is part of the engagement letter, eSigned by both parties; changes by amendment (eSigned), versioned.
- **FR-P21-30 — Activation.** On contract: P22 creates the RM portfolio entry, proposes the tenant grant (RM as maker in specified departments/functions; client employee as checker — R-072) for the tenant admin to approve; retainer dashboard for the buyer shows hours used / deliverables delivered vs plan, SLA attainment, upcoming items, monthly report archive.
- **FR-P21-31 — Hour bank rules.** Hours logged by delivery staff against tasks (timesheets flow to OH4/OH11 for utilisation; the buyer sees hours by service category, not staff names unless configured); overage requires buyer approval before work continues (hard stop at 100% unless `overage_preapproved_hours` set); unused hours roll over one month by default [OWNER TO SET].
- **FR-P21-32 — Monthly service report** auto-generated (Vidhi draft from engagement data, RM-reviewed): work done, filings supported, items pending with the client, upcoming deadlines, SLA table, risks observed (scoped to the engagement), next month plan; shared in the Engagement Room / tenant DMS.
- **FR-P21-33 — Renewal and exit.** Renewal reminder T-60/T-30; termination per notice; on exit, deliverables index and work-in-progress hand-over pack; revocation of RM tenant grants (P22) on the effective date (automatic, logged).

### 4H. Engagement Room (buyers without a tenant)

- **FR-P21-34 — Features.** Per engagement: secure messages (threaded, mentions, read receipts), file exchange (virus-scanned, versioned, DMS-backed, hash), milestone tracker, approvals (accept deliverable, approve change request), eSign envelopes, invoices and payments, meeting links, activity log; Vidhi Q&A limited to the engagement's documents (NN-13 sealed classes respected).
- **FR-P21-35 — Security.** Buyer users invited by e-mail + OTP; MFA optional (required for amounts above ₹5 lakh [REC]); data in India region; retention per engagement terms (default 8 years for engagement records, deliverables downloadable at any time) [OWNER TO SET]; export as a ZIP in LDC-EXPORT-1.0 sub-structure.
- **FR-P21-36 — Conversion to tenant.** "Add the platform" turns the buyer account into a trial tenant (P20 flow) and moves Engagement Room records into the tenant's DMS and Services register with a reconciliation report; the buyer chooses which documents to carry.

### 4I. FinLegal Academy (R-036)

- **FR-P21-37 — Feed.** `ACADEMY_PORT` adapter pulls the course catalogue from trainings.lawdocs.in (LMS appears to be Graphy-hosted [VERIFY]; via API if available, else a signed JSON/CSV feed published by the Academy team daily): course id, title, category, level, format (live/recorded/blended), duration, language, price, next batch dates, certificate type, trainer (name only if the trainer consents), URL. Display in `/marketplace/trainings` with filters (audience: compliance officers, DSA/DMA, CISO, KYC/AML officers, DPOs, board & KMP, HR/POSH, IFSCA professionals).
- **FR-P21-38 — Enrolment.** Individual enrolment deep-links to the Academy checkout (Academy is the merchant for individual courses unless the owner moves it into OH8 — OI-P21-07); corporate bundles (n seats, custom batches, in-house sessions) are first-party marketplace offerings quoted and invoiced via OH8.
- **FR-P21-39 — Evidence loop.** With learner consent, completion certificates (PDF + certificate id + course + date) are imported into the tenant's HRMS training records (P13) and attached as evidence to relevant obligations (e.g., POSH awareness, KYC/AML training, DSA training under RBI fair-practice/conduct directions [VERIFY]); bulk import via the Academy's export when the tenant bought a corporate bundle.
- **FR-P21-40 — Naming.** The brief calls it "FinLegal Academy"; the live site is branded "LawDocs Trainings" — the display name is a setting (`mkp.academy.display_name`) pending OI-P21-01.

### 4J. Ratings, reviews and moderation

- **FR-P21-41 — Where allowed** (profession mode): 1–5 rating plus optional text after `CLOSED`; only verified buyers of that engagement; one review per engagement; displayed with date and buyer organisation type (not name) unless the buyer consents; provider can reply once; moderation (abusive, confidential information, personal data, claims) by `plt_content_checker`; no incentives for reviews; no review suppression by provider; aggregate scores show count and period. For LawDocs first-party offerings an aggregate CSAT may be shown with method ("average of n post-engagement surveys, last 12 months").
- **FR-P21-42 — Restricted professions**: no ratings stored for display; post-engagement surveys go to the provider privately (and to LawDocs only as aggregate quality metrics for the marketplace).

### 4K. Complaints, disputes, cancellations and refunds

- **FR-P21-43 — Marketplace grievance officer** details displayed on every marketplace page footer and order confirmation (name, designation, contact); acknowledge ≤ 48 h, resolve ≤ 1 month (E-Commerce (Amendment) Rules 2026 r.4(2), 4(5), adopted from launch).
- **FR-P21-44 — Dispute flow.** Buyer raises dispute (category: delay, quality, scope, billing, conduct, confidentiality) → provider response within 5 business days → LawDocs mediation (for M1 the complaint goes to OH6 `client_complaint` as a LawDocs service complaint; for M2/M3 LawDocs facilitates but is not the adjudicator) → outcome (re-work, partial refund via credit note, full refund, no action) → closure; buyer is informed of external remedies (consumer forum where applicable; contract dispute resolution clause). Equator is **not** suggested by default to avoid self-dealing optics; only a neutral list of ADR options if the owner enables `mkp.disputes.show_adr_options` (default OFF).
- **FR-P21-45 — Cancellation and refunds** (Appendix O §O.6): before work starts — full refund less non-refundable scoping fee if stated; after inputs received — pro-rata to milestones delivered; retainers — per notice period, unused prepaid months refunded; refunds via OH8 to the original source with a credit note (OH8.7); M2 refunds are the provider's obligation, tracked by LDC.

### 4L. Invoicing and tax

- **FR-P21-46 — First-party invoices** (M1): OH8 tax invoice (CGST Rules r.46) with SAC per service class (tax review), place of supply, e-invoice IRN where applicable; e-mailed to the buyer's billing contacts with PDF; visible in Engagement Room and Settings › Billing › Marketplace orders.
- **FR-P21-47 — Reverse charge note.** Where a service is legal service by an advocate/firm of advocates to a business entity (M2 only), the provider's invoice states "Tax payable under reverse charge" and LDC shows the buyer a note (Notification 13/2017-Central Tax (Rate) Sl.2 [VERIFY]); LawDocs first-party services are not "legal services by an advocate" and are taxed under forward charge [INTERP; VERIFY].
- **FR-P21-48 — M3 TCS.** When M3 is enabled: TCS 0.5% (CGST Act s.52, rate from 10 Jul 2024) computed by OH8 on net value of taxable supplies through the platform; provider statements monthly; GSTR-8 data export; provider sees TCS credit reference.
- **FR-P21-49 — TDS.** Buyers deduct TDS on professional/technical fees under the Income-tax Act 2025 [VERIFY section and rate; successor of s.194J]; certificate upload as in P20 FR-P20-52.
- **FR-P21-50 — Seller information on invoice and listing** (E-Commerce (Amendment) Rules 2026 r.5(3), 6(5)(j)): provider legal name, registration status, GSTIN/Udyam, address, customer-care contact, shown on listing (where profession mode allows) and on invoice in the same font size as the platform name (M3).

### 4M. Buyer experience: fewer clicks

- **FR-P21-51 — Smart entry points inside the product.** Contextual "Get help with this" links on obligations, returns, policies and risk exercises open a pre-filtered marketplace drawer (e.g., from an overdue ICAAP obligation → "ICAAP document preparation" offerings with the obligation reference attached to the request) — shown only to users with `mkp.buy` and suppressible per tenant (`mkp.tenant.contextual_offers`, T, default on).
- **FR-P21-52 — One-click re-order** of recurring services (e.g., annual policy review pack) with last year's scope pre-filled.
- **FR-P21-53 — Bundles with the subscription.** Configurator step 5 (P20) offers implementation, migration and retainer packages; the order produces one OH8 order with separate lines and stream codes.
- **FR-P21-54 — Saved services and comparisons** (up to 3 offerings side by side: scope, deliverables, timeline, price).

### 4N. Partner network for foreign jurisdictions and global professionals *(v1.1; D-44; Appendix Y §Y.5)*

**FR-P21-55 — Partner types.** The provider registry gains partner types *content partner*, *reviewer of record*, *delivery partner*, *implementation partner*, *referral partner* and *licensed feed provider* (Appendix Y §Y.5.1), each with jurisdictions, professions, languages and services. Content and reviewer partners work in the partner portal (P25); delivery partners appear in the marketplace for their jurisdictions.

**FR-P21-56 — Due diligence.** Onboarding requires: registration and licence/bar standing in each jurisdiction; professional indemnity cover by tier `[OWNER TO SET]`; conflicts policy; sanctions and adverse-media screening of the firm and principals; information-security questionnaire and DPA (with transfer clauses where personal data crosses borders, Appendix Y §Y.8); anti-bribery and professional-rules warranty; references. Verification evidence is stored and re-checked annually (licence expiry alerts).

**FR-P21-57 — Commercial switches per country × profession × service.** `mkp.commercial.<country>.<profession>.<service_class>` with values LISTING_FEE, PLATFORM_FEE_CLIENT, RESALE, CONTENT_LICENCE, REVENUE_SHARE, OFF — every non-OFF value requires a counsel-opinion reference for that country (NN-20 extended; Appendix O §O.14). Default OFF; India rows unchanged.

**FR-P21-58 — Client contracts directly by default.** Delivery partners contract with the client (Model M2); LawDocs resells only where lawful and licensed in that country (D-44). Engagement letters use the partner's jurisdiction and governing-law clauses; the SLA eSign uses an eSign method valid in that jurisdiction (P07 ESIGN_PORT adapters) [VERIFY per country].

**FR-P21-59 — Jurisdiction conflict checks.** Before a delivery partner accepts an engagement, the conflicts check (OH `POST /v1/conflicts/check`) runs with jurisdiction and opposing-party data; a hit blocks acceptance until cleared.

**FR-P21-60 — Scorecards and tiers.** Quarterly scorecard (content defect rate, review turnaround, on-call response time, client satisfaction, filing timeliness, security incidents) drives Gold/Silver/Registered tiers; marketplace ordering uses objective service metrics only — never paid placement for restricted professions (NN-20).

**FR-P21-61 — "Ask a local expert".** From any foreign checkpoint, entitled users (ADD-QRY) send a question to the reviewer-of-record firm or a chosen delivery partner with checkpoint, clause and entity context under a delivery grant; SLA clock from submission; answer stored as a tenant-private expert note; Vidhi drafts the question and summarises the answer but never answers for the firm (NN-14).

### 4O. New service categories with eligibility and independence rules *(v1.1)*

**FR-P21-62 — AI governance services.** AI governance readiness assessment (FREE-AI, MeitY guidelines, EU AI Act, ISO/IEC 42001), AI system inventory build, model validation, bias/fairness testing, AI red-teaming, ISO/IEC 42001 readiness; deliverables land in the client's OV_AI module (folder 29). A provider that built or validated a model may not issue the independent validation of the same model (independence check).

**FR-P21-63 — ESG and BRSR services.** BRSR/BRSR Core preparation, GHG inventory, CSR programme management and impact assessment, and BRSR Core assurance/assessment **only by eligible assurance providers** with an independence check (the preparer cannot assure) [VERIFY SEBI eligibility conditions for BRSR Core assurance providers].

**FR-P21-63A — Litigation and legal-matter support.** Matter-management set-up, notice-reply drafting support, limitation and hearing calendaring, legal-spend analysis (LawDocs first-party, ADVISORY); representation and legal advice only by advocates contracting directly (`RESERVED_ADVOCACY`, M2; D-32), rendered under the Rule 36 schema with no ratings or fees displayed (NN-20).

**FR-P21-64 — Global entity services.** Registered-agent, foreign company-secretarial, annual-return and economic-substance filings, foreign payroll and tax returns — by delivery partners licensed in that country (corporate service provider licences where required [VERIFY per country]).

**FR-P21-65 — Cross-border tax and FEMA.** ODI/FDI reporting support, transfer-pricing documentation support and treaty-relief documentation — eligible professionals only for attest work.

**FR-P21-66 — RE guard-rails extended.** The RE-buyer guard-rails (Appendix O §O.8) apply to new categories (e.g., a "virtual Chief Compliance Officer" for an NBFC remains support only; IA co-sourcing rules per X-30).

### 4P. Practitioner-firm accounts *(v1.1; G5 TM-396; P22 §4L)*

**FR-P21-67 — Firm as customer and provider.** A verified CS/CA/law firm may hold (a) a provider profile (subject to its profession's rules — CA/CS/advocate listings OFF by default) and (b) a practitioner plan (P20 FR-P20-79) giving a firm workspace in `apps/delivery` to serve many client tenants under client-approved delivery grants (NN-43). The two are separate: buying the practitioner plan never lists the firm in the marketplace.

**FR-P21-68 — Client invitation.** The firm invites a client by e-mail; the client either links an existing LDC tenant (client admin approves the grant) or starts a trial with the firm pre-linked; the firm never becomes the client's admin or checker.

### 4Q. Gap-driven suggestions and faster buying *(v1.1)*

**FR-P21-69 — Suggestions from the client's own gaps.** When a tenant has overdue instances, missing policies, an expiring certification, a failed control test or an unpublished BRSR, the marketplace shows a relevant service suggestion inside the workspace (e.g., "Need help with your ICAAP? See ICAAP drafting services"). Suggestions are rule-based from objective gaps, labelled "Suggestion", dismissible, never shown for restricted professions as personalised promotion (NN-20), and switchable off per tenant (`mkp.suggestions.enabled`).

**FR-P21-70 — One-click re-order.** Repeat engagements (e.g., annual BRSR, annual ICAAP, quarterly VAPT) can be re-ordered with last year's scope pre-filled and the same provider pre-selected, subject to independence rules.

---

## 5. Workflows and state machines

### 5.1 Engagement

```
REQUESTED ─(provider triage ≤ 2 BD)→ SCOPING ─→ PROPOSED ─(buyer)→ ACCEPTED ─→ CONTRACTED (both eSigned)
   │                                   │  └→ DECLINED_BY_BUYER (reason)          │
   └→ DECLINED_BY_PROVIDER (reason:     └→ EXPIRED (validity)                     ├→ ADVANCE_PAID (if terms)
       conflict | capacity | out-of-scope | profession rule)                      ↓
                                                         INPUTS_PENDING (checklist; reminders D+3, D+7)
                                                                ↓ inputs complete (timeline clock starts)
                                                         IN_DELIVERY ↔ CHANGE_REQUESTED (delta approved by buyer)
                                                                ↓ milestone released (internal review passed)
                                                         DELIVERED ─→ REVISION_REQUESTED (counts) ─→ IN_DELIVERY
                                                                ↓ accepted | deemed (if contract)
                                                         ACCEPTED_BY_BUYER → INVOICED → PAID → CLOSED → (REVIEWED)
Side: ON_HOLD (reason, review date) from any active state; CANCELLED (terms; refund rule); DISPUTED (§5.3).
Guards: proposal blocked if independence check fails (FR-P21-14) or RE guard-rail acknowledgement missing (FR-P21-13);
        CONTRACTED requires engagement letter version hash on both signatures; delivery staff cannot accept on buyer's behalf.
```

### 5.2 Retainer

```
PROPOSED → CONTRACTED (SLA schedule eSigned) → ONBOARDING (P22 grant proposed → tenant admin approves; kick-off)
  → ACTIVE (monthly cycle: plan → deliver → report → invoice → SLA credit calc)
  → RENEWAL_DUE (T-60) → RENEWED | NOTICE_GIVEN → WIND_DOWN (hand-over pack; grants revoked at end) → ENDED
ACTIVE → SUSPENDED (non-payment per OH8 dunning; statutory work in flight completed or handed over — never abandoned mid-deadline)
```

### 5.3 Dispute

```
RAISED (buyer; category) → PROVIDER_RESPONSE (≤ 5 BD) → RESOLVED_BY_AGREEMENT | ESCALATED
ESCALATED → LAWDOCS_REVIEW (M1: OH6 client_complaint; M2/M3: facilitation, ≤ 10 BD) → OUTCOME (re-work | credit note | refund | no action)
→ CLOSED (buyer informed of external remedies). Grievance-officer clock: ack ≤ 48 h, resolution ≤ 1 month.
```

### 5.4 Provider onboarding — see FR-P21-17. Offering lifecycle: `DRAFT → LINTED → IN_REVIEW → LIVE → PAUSED → RETIRED` (material change creates a new version in review; live version stays until approval).

### 5.5 Academy sync

```
FETCH (daily 03:00 IST + webhook if available) → VALIDATE (schema, price, URL allow-list) → DIFF → PUBLISH (cache)
On failure: keep last good catalogue ≤ 7 days, then hide prices and show "See current details on LawDocs Trainings".
```

---

## 6. Screens and UX

| Screen ID | Name | Path / surface | Roles |
|---|---|---|---|
| SCR-MKP-01 | Marketplace home | `/marketplace` | anon+ — category tiles, "Popular for NBFCs/UCBs/listed companies/co-operatives…" (segment presets, not popularity claims unless evidenced), search bar, "Buy services without a subscription" explainer |
| SCR-MKP-02 | Category page | `/marketplace/{category}` | anon+ — filters, ranking-parameters disclosure link |
| SCR-MKP-03 | Offering page | `/marketplace/s/{slug}` | anon+ |
| SCR-MKP-04 | Compare offerings | `/marketplace/compare` | anon+ |
| SCR-MKP-05 | Provider page (permitted modes only) | `/marketplace/p/{slug}` | anon+ |
| SCR-MKP-06 | Legal professionals directory (Rule 36 mode) | `/marketplace/directory/advocates` | anon+ — disclaimer, random/alphabetical order, Schedule fields only (only if enabled) |
| SCR-MKP-07 | Trainings (Academy) | `/marketplace/trainings` | anon+ |
| SCR-MKP-08 | Request / quote form | modal | anon → buyer |
| SCR-MKP-09 | Buyer sign-up & organisation | `/marketplace/account` | buyer |
| SCR-MKP-10 | Checkout (first-party fixed price) | P20 components | buyer, tenant |
| SCR-MKP-11 | My engagements | `/services` (in-app) and `/marketplace/my` | buyer, tenant |
| SCR-MKP-12 | Engagement Room | `/services/{engagement}` | buyer, provider |
| SCR-MKP-13 | Retainer dashboard | `/services/retainers/{id}` | buyer/tenant |
| SCR-MKP-14 | Monthly service reports archive | tab in SCR-MKP-13 | buyer/tenant |
| SCR-MKP-15 | Disputes & complaints | `/services/{engagement}/dispute` | buyer |
| SCR-MKP-20 | Offering studio (first-party) | `apps/delivery` › Marketplace › Offerings | `dlv_lead` |
| SCR-MKP-21 | Proposal builder | `apps/delivery` › Engagements › Proposal | `dlv_professional`, `dlv_lead` |
| SCR-MKP-22 | Engagement pipeline (kanban by state) | `apps/delivery` › Engagements | delivery roles |
| SCR-MKP-23 | Delivery workbench | `apps/delivery` › Engagement › Work | delivery roles |
| SCR-MKP-24 | Provider portal (external) | `providers.lawdocscomply.com` (flagged) | `mkp_provider_admin` |
| SCR-MKP-30 | Marketplace administration | `apps/console` › Marketplace (categories, profession modes, guard-rails, streams, moderation queue, provider review, grievance queue) | `plt_super_admin`, `plt_content_checker`, grievance officer |
| SCR-MKP-31 | Academy feed monitor | `apps/console` › Marketplace › Academy | `plt_super_admin` |

UX rules: every offering card shows price basis, timeline and "what you get" in three lines; "i" help keys `help.mkp.*`; restricted-profession pages never show buy buttons; buyer sees one unified "Services" menu whether subscribed or not; keyboard shortcuts in the delivery pipeline (`N` new proposal, `A` assign, `→` advance state with confirmation).

**Screens added in v1.1** *(v1.1)*

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-MKP-40 | Jurisdiction browse | Marketplace → By country | Delivery partners and services per jurisdiction; only PUBLISHED packs' countries promoted |
| SCR-MKP-41 | Partner onboarding (foreign) | Provider → Apply → Partner programme | Partner types, due-diligence uploads, DPA |
| SCR-MKP-42 | Partner scorecard | Console → Marketplace → Partners → Scorecard | Tier, metrics, actions |
| SCR-MKP-43 | Country commercial switches | Console → Marketplace → Rules → Countries | Country × profession × service class with counsel references |
| SCR-MKP-44 | Practitioner plan sign-up | Marketplace → For firms | Plan bands, client-link explanation |
| SCR-MKP-45 | Service suggestion card | In-workspace (gap context) | Rule-based, dismissible |

---

## 7. Backend design

### 7.1 Modules: `mkp` (owner), `bil` (shared commerce), `dms` (deliverables, engagement letters), `wf` (tasks, SLAs, notifications), `iam` (buyer accounts, provider orgs), `int` (Academy, OH9 events), `ai` (scoping/report drafts), `sdc` (retainer activation, P22), `xpt` (exports), `core` (audit).

### 7.2 Tables

| Table | Key columns |
|---|---|
| `mkp.categories` | id, parent_id, code, name, description, sort, visible |
| `mkp.providers` | id, type (FIRST_PARTY_TEAM, EXTERNAL_ORG), org_id, oh9_professional_ids[], profession_codes[], listing_mode, status, verification jsonb, agreement_ref, pi_insurance jsonb, suspended_reason |
| `mkp.profession_rules` | profession_code, listing_mode, commission_allowed, paid_listing_allowed, ratings_allowed, cta_allowed[], counsel_opinion_ref, effective_from, version |
| `mkp.offerings` | id, version, provider_id, category_id, service_class, title, slug, eligibility jsonb, scope, exclusions, deliverables jsonb, inputs jsonb, timeline_bd, price_model, price_ref (OH8 SKU or provider price), sla_template_id, languages[], status, claims_refs[], reviewed_by, live_from |
| `mkp.offering_packages` | offering_id, tier_code, inclusions, price |
| `mkp.buyer_orgs` | id, org_id, tenant_id (nullable), gst_profile_ref, declared_auditors jsonb, entity_type, regulator_codes[] |
| `mkp.engagements` | id, number, offering_id/version, buyer_org_id, provider_id, model (M1, M2, M3), state, scope_snapshot, price_snapshot, engagement_letter_doc_id, signatures jsonb, oh8_quote_ref, oh8_order_ref, ack_re_guardrail bool, independence_check jsonb, created_at |
| `mkp.milestones` | engagement_id, seq, title, due_at, state, deliverable_doc_ids[], accepted_by, accepted_at, deemed bool |
| `mkp.change_requests` | engagement_id, delta_scope, delta_price, state, approved_by |
| `mkp.retainers` | id, engagement_id, plan_code, hour_bank, basket jsonb, sla_schedule_id, cycle, renewal_at, state, rm_assignment_ref (sdc) |
| `mkp.sla_schedules` / `mkp.sla_events` | metrics, targets, credits rule; event (metric, due_at, met_at, breached bool, credit_minor) |
| `mkp.time_entries` | retainer_id/engagement_id, staff_ref, hours, category, task_ref, billable — mirrored to OH4/OH11 as aggregates |
| `mkp.service_reports` | retainer_id, period, doc_id, generated_by (AI draft id), approved_by, shared_at |
| `mkp.reviews` | engagement_id, rating, text, status (PENDING, PUBLISHED, REJECTED), moderator, reply |
| `mkp.disputes` | engagement_id, category, state, provider_response, outcome, credit_note_ref, oh6_ref |
| `mkp.academy_courses` | course_id, title, category, audience[], format, duration, language, price_minor, next_batches jsonb, certificate_type, url, fetched_at, feed_hash |
| `mkp.training_certificates` | tenant_id, employee_ref (P13), course_id, certificate_no, issued_at, file_id, consent_ref |
| `mkp.room_messages`, `mkp.room_files` | engagement_id, author, body (encrypted), attachments → dms |

### 7.3 APIs (selected)

`GET /v1/public/marketplace/categories`, `GET /v1/public/marketplace/offerings?q=&filters=`, `GET /v1/public/marketplace/offerings/{slug}`, `GET /v1/public/marketplace/trainings`, `GET /v1/public/marketplace/directory/advocates` (Rule 36 schema, random seed logged, only if enabled); `POST /v1/marketplace/requests`; `POST /v1/marketplace/engagements/{id}/proposals`; `POST /v1/marketplace/engagements/{id}/accept`; `POST /v1/marketplace/engagements/{id}/esign`; `POST /v1/marketplace/engagements/{id}/milestones/{seq}/deliver|accept|revise`; `POST /v1/marketplace/engagements/{id}/change-requests`; `POST /v1/marketplace/engagements/{id}/disputes`; `GET /v1/marketplace/retainers/{id}/dashboard`; `POST /v1/marketplace/reviews`; console: `/v1/console/marketplace/*` (profession rules, moderation, provider review, guard-rails); machine: Academy feed ingest, OH9 events intake.

### 7.4 Domain events

`ServiceRequested`, `ProposalSent`, `EngagementContracted`, `MilestoneDelivered`, `MilestoneAccepted`, `EngagementClosed`, `EngagementCancelled`, `RetainerActivated`, `RetainerSLABreached`, `ServiceCreditIssued` (→ OH8 credit note request), `RetainerEnded` (→ P22 revoke grants), `MarketplaceDisputeRaised` / `Resolved` (→ OH6 for M1), `ProviderSuspended` (from OH9 `ProfessionalSuspended`), `OfferingPublished`, `AcademyCatalogueSynced`, `TrainingCertificateImported`. Consumed: `ProfessionalEmpanelled`, `ProfessionalSuspended` (OH9), `InvoiceIssued`, `SubscriptionPaymentReceived` (OH8), `ImplementationMilestoneReached` (OH4, for implementation services).

### 7.5 Jobs

`EngagementSLAWorkflow` (Temporal: timeline and SLA clocks, reminders, breach events), `RetainerCycleWorkflow` (monthly plan/report/invoice/credit), `InputsReminderJob`, `DeemedAcceptanceJob`, `AcademySyncJob`, `ProviderCredentialWatch` (expiry → suspend listing), `OfferingReReviewSampler` (10% monthly), `RankingDisclosureRenderer`.

---

## 8. Integrations

| Port | Adapter | Use |
|---|---|---|
| `BILLING_PORT` | OH8 | First-party SKUs, quotes, orders, invoices, credit notes; streams RS-LDC-12…22; new stream `MARKETPLACE_COMMISSION` (Appendix X) |
| `DIRECTORY_PORT` | OH9 | Provider credential verification; `ProfessionalEmpanelled`/`Suspended`; Rule 36 fields |
| `ESIGN_PORT` | Leegality / Digio / SignDesk / Surepass (D-20) | Engagement letters, SLAs, amendments |
| `ACADEMY_PORT` | Graphy API or signed feed from trainings.lawdocs.in | Course catalogue, corporate enrolments, completion export |
| `WORKSPACE_PORT` | M365 (Teams meetings, SharePoint links), Google (Meet, Drive) | Scoping calls; deliverable links |
| `PAYMENT_ROUTE` | Razorpay Route (via OH8) | M3 only, flagged |
| `CLAIMS_GATE_PORT` | OH14 | Offering copy, provider claims, CSAT statements |
| `SUPPORT_PORT` | OH6 | Complaints about LawDocs services |
| `CRM_PORT` | OH3 | Quote requests from non-subscribers as leads (with consent) |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `mkp.public.enabled` | G | true | — | `plt_super_admin` |
| `mkp.providers.external.enabled` | G | false | — | Owner + counsel ref |
| `mkp.model.m2.enabled` | G | false | — | Owner + counsel ref |
| `mkp.model.m3.enabled` | G | false | — | Owner + counsel + tax ref |
| `mkp.profession.<code>.listing_mode` | G | per FR-P21-12 | OFF, DIRECTORY_RULE36, DIRECTORY_ICAI, FULL_MARKETPLACE | `plt_super_admin` + `plt_content_checker` + counsel_opinion_ref (mandatory) |
| `mkp.profession.<code>.commission_allowed` | G | false (advocate: L false) | — | as above |
| `mkp.profession.<code>.ratings_allowed` | G | false for regulated professions (advocate: L false) | — | as above |
| `mkp.sponsored.enabled` | G | false | never for regulated professions (L) | Owner |
| `mkp.contract.clickwrap_max_value` | G | ₹50,000 [OWNER TO SET] | ₹0–₹2,00,000 | `plt_super_admin` + legal |
| `mkp.acceptance.deemed_days` | G | 10 BD | 0 (off)–30 | `plt_super_admin` + legal |
| `mkp.retainer.hour_rollover_months` | G | 1 | 0–3 | `dlv_lead` + checker |
| `mkp.retainer.sla_credit_pct` / `cap_pct` | G | 5 / 20 | 0–25 / 0–50 | Owner |
| `mkp.disputes.provider_response_bd` | G | 5 | 2–10 | `plt_super_admin` |
| `mkp.grievance.ack_hours` / `resolve_days` | L | 48 / 30 | — | — |
| `mkp.tenant.who_can_buy` | T | admins + CCO + CFO | any role set | `ten_admin` |
| `mkp.tenant.contextual_offers` | T | true | — | `ten_admin` |
| `mkp.academy.display_name` | G | "LawDocs Trainings — FinLegal Academy" [OWNER TO SET] | — | Owner |
| `mkp.academy.cache_max_age_days` | G | 7 | 1–14 | `plt_super_admin` |
| `mkp.category.disputes.equator_link` | G | false | — | Owner + Equator oversight |
| `mkp.price_guardrail.<category>` | G | min/max per category | — | `plt_super_admin` |

**Settings added in v1.1** *(v1.1)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `mkp.partners.foreign.enabled` | G | false | — | `plt_super_admin` + checker |
| `mkp.commercial.<country>.<profession>.<service_class>` | G | OFF | counsel reference required for non-OFF | `plt_super_admin` + legal checker |
| `mkp.partner.pi_cover_min.<tier>` | G | `[OWNER TO SET]` | — | `plt_super_admin` |
| `mkp.suggestions.enabled` | T | true | — | `ten_admin` |
| `mkp.independence.check.enabled` | L | true | — | — |

---

## 10. Security, privacy and audit

- **Data roles (DPDP)**: for M1 LawDocs is a data fiduciary for buyer contact data and a processor for buyer documents it handles for the buyer; for M2/M3 the provider is an independent fiduciary for professional records and a processor for LDC-hosted Engagement Room content where LDC hosts on its behalf — Appendix O §O.7 sets the DPA templates; buyer notices state this.
- **Sealed classes** (NN-13): POSH-related engagements (external member services) keep complaint content sealed; Engagement Room files may be marked "Board-confidential" with restricted access.
- **Provider access to tenant data** only via P22 grants approved by the tenant admin (NN-30); providers never see other engagements or tenant data beyond grant scope.
- **Audit**: every proposal, signature, delivery, acceptance, dispute action, review moderation, profession-rule change (with counsel opinion reference) in the audit ledger; Correction Entries for fixes (D-02).
- **No marketing misuse**: engagement content never feeds CRM, ad audiences or other group products (OH Part 4.5); only consented contact data becomes an OH3 lead.
- **E-commerce duties** adopted: grievance officer, seller details, ranking disclosure, sponsored labelling, dark-pattern self-audit (Appendix Q evidence).

---

## 11. AI touchpoints and guardrails

- **Scope assistant**: drafts a scope summary and inputs checklist from the buyer's request and uploaded documents; professional edits and owns it (NN-04).
- **Proposal drafter**: drafts the engagement letter from template + scope; clauses from approved clause library only; legal/commercial terms never invented.
- **Monthly service report** and **deliverable QA** (checks citations in a drafted policy against the Regulatory Content Library, flags missing mandatory clauses by regulator template — P07) — drafts only.
- **Service finder** (Vidhi on marketplace): recommends categories/offerings from a described need; never recommends an individual advocate/CA/CS (profession rule); discloses that LawDocs offerings are first-party.
- AI credits consumed by these features are charged to the provider's (LawDocs internal) budget, not the buyer's wallet.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p21/*.feature`)

```gherkin
Feature: Public marketplace
  Scenario: Browse without login
    Given an anonymous visitor
    When they open /marketplace and search "ICAAP"
    Then offerings for ICAAP document preparation are listed with price basis and timeline
    And no login prompt appears until they request a quote

  Scenario: Ranking disclosure
    When a visitor opens any category page
    Then a "How results are ordered" link lists the ranking parameters in descending order of importance

Feature: Professional-conduct rules
  Scenario: Advocate profile cannot show ratings or buy buttons
    Given profession "ADVOCATE" in DIRECTORY_RULE36 mode
    When the directory page renders an advocate
    Then only Rule 36 Schedule fields are present
    And the response schema contains no rating, fee, photo or call-to-action field

  Scenario: CA in practice cannot be listed by default
    Given profession "CA_IN_PRACTICE" with listing_mode OFF
    When a provider admin tries to publish an offering as a CA in practice
    Then publication is refused with LDC-MKP-012 citing the ICAI aggregator restriction

  Scenario: Changing a profession mode needs a counsel opinion reference
    When a super admin sets CS_IN_PRACTICE listing_mode to FULL_MARKETPLACE without counsel_opinion_ref
    Then the change is rejected with LDC-MKP-015

Feature: RE guard-rails and independence
  Scenario: vCCO for an NBFC is support only
    Given a buyer whose entity type is "NBFC - Middle Layer"
    When they open the "Virtual CCO support" offering
    Then a notice states the designated CCO must remain the NBFC's employee and owner of decisions
    And ordering requires the unticked acknowledgement to be ticked

  Scenario: Certification wall
    Given LawDocs delivered "ISO 27001 readiness" to tenant T
    When the same scope "ISO 27001 certification audit" is requested from a provider linked to LawDocs
    Then the proposal is blocked with LDC-MKP-020 (impartiality)

Feature: Services without SaaS
  Scenario: Non-subscriber buys a fixed-price service
    Given a buyer account with a validated GSTIN
    When they buy "Annual policy review pack - Standard" and pay via Razorpay-hosted checkout
    Then an OH8 tax invoice is issued and e-mailed to the billing contact
    And an Engagement Room is created with the inputs checklist
    And no tenant is created

Feature: Retainers
  Scenario: SLA breach issues a service credit
    Given a retainer with a 3 business-day turnaround SLA for return-preparation support
    When a request acknowledged on Monday is delivered on Friday of the same week
    Then RetainerSLABreached is emitted and a credit-note request of 5% of the monthly fee is sent to OH8

  Scenario: Retainer end revokes delivery access
    Given an active retainer with an RM granted maker access in the tenant
    When the retainer ends
    Then the RM's tenant grant is revoked on the effective date and the tenant admin is notified

Feature: Academy
  Scenario: Stale Academy feed
    Given the Academy feed has failed for 8 days
    Then course prices are hidden and each course links to LawDocs Trainings for current details

  Scenario: Certificate import needs consent
    Given an employee completed "POSH awareness" in a corporate bundle without consenting to sharing
    When the tenant imports completions
    Then that employee's certificate is not imported and the count of withheld records is shown
```

NN tests: `NN-05_proposal_discount_maker_checker`, `NN-09_engagement_letter_hash`, `NN-13_posh_engagement_sealed`, `NN-16_marketplace_saq_a`, `NN-19_offering_claims_gate`, `NN-20_profession_render_allowlist`, `NN-20_no_commission_regulated_professions`, `NN-30_provider_access_only_by_grant`.

```gherkin
Feature: v1.1 — partners, new categories, independence

  Scenario: Foreign commercial model needs counsel reference
    When a super admin sets mkp.commercial.AE.ACCOUNTANT.ADVISORY to REVENUE_SHARE without a counsel-opinion reference
    Then the change is rejected

  Scenario: Preparer cannot assure the same BRSR
    Given provider P prepared tenant T's BRSR for FY 2026-27
    When P is offered for BRSR Core assurance for the same report
    Then the independence check blocks the offer

  Scenario: Firm plan does not create a listing
    Given a CA firm buys a practitioner plan
    Then no marketplace listing is created for the firm

  Scenario: Gap suggestion is rule-based and dismissible
    Given tenant T has no approved ICAAP for the current year
    Then an ICAAP service suggestion appears labelled "Suggestion"
    And dismissing it hides it for 90 days
```

---

## 13. Deliverables and exit gate

- Marketplace public and in-app surfaces, buyer accounts, Engagement Room, first-party offering studio, proposal builder, delivery pipeline, retainers with SLA engine, Academy feed, disputes, moderation, profession rules engine with seeded rules, 60+ seeded offerings (Appendix O §O.2), engagement-letter and SLA templates (Appendix O §O.6) approved by counsel.
- **Exit gate:** §12 scenarios and NN tests green; counsel sign-off on engagement letter and marketplace terms; tax sign-off on SAC per service class and RCM statements; owner sign-off on retainer plans and prices; external provider flags remain OFF unless OI-P21-02…05 are closed with opinions recorded.

---

## 14. Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P21-01 | Academy name: "FinLegal Academy" vs "LawDocs Trainings"; LMS platform (Graphy?) and API availability | Brand + technical | Owner | `mkp.academy.display_name`; signed CSV feed |
| OI-P21-02 | Advocate presence in the marketplace (Rule 36 directory only?) pending *Sulekha v P.N. Vignesh* | SC matter pending | Counsel | Directory page OFF; no advocates listed |
| OI-P21-03 | ICAI position on platforms (23 Oct 2019 ESB announcement; any 2025–26 update) | Re-check | Counsel / CA | CA listing OFF |
| OI-P21-04 | ICSI and ICMAI positions on aggregators | Not verified | Counsel | OFF |
| OI-P21-05 | M3 Route marketplace: ECO status, TCS, E-Commerce Rules marketplace duties, PA terms | Tax/legal | Tax counsel | `mkp.model.m3.enabled = OFF` |
| OI-P21-06 | Which group legal entity is the selling entity for LawDocs services (LawDocs vs Infrabyx entity) and its GSTINs | Corporate | Company Secretary | Block M1 go-live until set in OH8 `selling_entity` |
| OI-P21-07 | Individual course checkout: Academy or OH8? | Commercial | Owner | Academy checkout (deep link) |
| OI-P21-08 | Which "legal documentation" services LawDocs (a company) may deliver without being "practice of law" | Advocates Act s.29/33; *A.K. Balaji* | Counsel | Service class `ADVISORY_COMPLIANCE` limited to compliance documentation; agreements drafted as templates/documentation support with advocate review option via M2 |
| OI-P21-09 | RBI NBFC outsourcing and internal-audit directions — exact paras for vCCO/vIA guard-rails | Re-check 2025–26 directions | S7/S5 streams | Generic guard-rail notice |
| OI-P21-10 | Certification-body referral commissions (ISO/IEC 17021-1, accreditation body rules; AICPA for SOC 2) | Impartiality | Counsel | No referral fees; disclosed referrals only |
| OI-P21-11 | E-Commerce (Amendment) Rules 2026 applicability to B2B services marketplace | Consumer definition | Counsel | Adopt duties as policy |
| OI-P21-12 | Deemed acceptance, refund and SLA credit values | Commercial | Owner | Defaults marked [OWNER TO SET] |

**Open items added in v1.1** *(v1.1)*

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P21-21 | Professional rules on fee sharing and referrals per foreign country (UAE, Singapore, UK, EU, US) | Counsel per country | General Counsel | All foreign switches OFF |
| OI-P21-22 | Corporate service provider licensing for resale abroad | Varies by country | Counsel | Model M2 only |
| OI-P21-23 | SEBI eligibility conditions for BRSR Core assurance providers | Verify current circular | Content lead | Assurance listings OFF |

---

## 15. Sources (accessed 25 October 2026)

1. Infrabyx Operations Hub Master Prompt v1.0 — OH8.2 (streams, deny list), OH8.4 (quotes), OH9 (directory, Rule 36), OH6.5 (complaints).
2. Infrabyx Ecosystem Integration Specification v1.1 §6.27, §6.29, §8.6.
3. Bar Council of India Rules, Part VI Chapter II, Rule 36 and Schedule; *Sulekha.com New Media Pvt Ltd v P.N. Vignesh*, SLP (C) 25794/2024 — https://www.verdictum.in/court-updates/supreme-court/sulekhacom-new-media-private-limited-v-pn-vignesh-ors-special-leave-to-appeal-c-nos-257942024-1557830 ; BCI directives March 2025 — https://www.scconline.com/blog/post/2025/03/17/bci-condemns-warns-against-unethical-legal-advertising-advocates-legal-influencers-issues-directives/
4. ICAI Ethical Standards Board announcement (23 Oct 2019) on application-based aggregators — https://taxguru.in/chartered-accountant/cas-cannot-list-with-application-based-service-provider-aggregators-icai.html ; Chartered Accountants Act 1949, First Schedule Part I clauses (2), (3), (6), (7).
5. Advocates Act 1961 ss.29, 33; *Bar Council of India v A.K. Balaji* (2018) 5 SCC 379 [VERIFY].
6. CGST Act 2017 s.52 (TCS 0.5% from 10 Jul 2024) — https://www.taxaj.com/learn/gst-on-e-commerce-operators-tcs-under-section-52-step-by-step-guide/ ; Notification 13/2017-Central Tax (Rate) [VERIFY].
7. Consumer Protection (E-Commerce) (Amendment) Rules 2026 (notified 9 Sep 2026; effective 1 Jan 2027) — https://www.mondaq.com/overview-of-the-consumer-protection-(e-commerce)-(amendment)-rules-2026/1846008
8. RBI (Rural Co-operative Banks – Managing Risks in Outsourcing) Directions 2025, RBI/DOR/2025-26/318 (28 Nov 2025) para 11 — https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12986
9. Razorpay Route documentation — https://razorpay.com/docs/payments/route/
10. ISO/IEC 17021-1:2015 cl. 5.2 (impartiality) [VERIFY edition]; AICPA independence rules for SOC engagements [VERIFY].
11. LawDocs Trainings, https://trainings.lawdocs.in (observed 25 Oct 2026).

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-20 (render allow-lists), NN-43; X-02, X-18 (Academy name), X-30; D-32 (no reserved advocacy/attest services in LawDocs' own name).

**Added in v1.1:** D-44; X-42.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
