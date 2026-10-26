# Phase P16 — Marketplace, Professional Registry, Retainers and FinLegal Academy

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (identity, KYC/KYB, professional credential verification, consent artefacts), P02 (tenancy, Personal and Company workspaces, maker-checker), P03 (settings registry, rule engine), P04 (Legal Vault — deliverables, engagement records), P07 (negotiation and redlines for engagement letters, SOWs and SLA schedules), P08 (eSign of engagement letters and SLAs; instrument eligibility gate), P09 runtime (Vidhi), P17 (`BILLING_PORT`, price cards, checkout, invoices, credits, stream registry), P18 (Delivery Console, delivery grants, RM-as-maker), P19 core (`int`, OH8/OH9 adapters, Academy feed connector), P20 core (`xpt.export_map`), P21 core (public-site shell, SEO, help keys). External: Operations Hub **OH8** (catalogue, quotes, orders, GST invoices, credit notes, Razorpay incl. Route), **OH9** (group professional directory and credential verification), **OH3** (consented leads), **OH6** (complaints about LawDocs services), **OH14** (claims gate); LawDocsComply (group listings, D-11); FinLegal Academy (trainings.lawdocs.in, Graphy-hosted per R5 §1.3).
> **Sequencing:** Starts after P17 sprint 3 (price-card, quote and checkout components frozen). Ship order: (1) public storefront + first-party LawDocs services (Model M1) + Academy listing; (2) retainers and SLA engine; (3) LawDocs Panel advocates' firm under Model M2 once OI-P16-01 and OI-P16-02 close; (4) third-party professionals behind per-profession switches that stay OFF until counsel opinion + checker approval (NN-21). Freeze point: profession render allow-lists (`RULE36_V1`, `PRO_SERVICE_V1`) and the `mkp.engagements` state machine are frozen at the end of sprint 4 because P15 (Consumer Help) and P14 (Business Services) consume them.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), M (Marketplace Services Catalogue and Professional Rules), L (Pricing, Plans, Revenue-Stream Registry and Savings Model — streams RS-LD-19…RS-LD-33), D (roles), F (instrument eligibility gate), K (`LD-EXPORT-1.0`), R (settings registry), W (open items), X (Operations Hub additions), Y (Ecosystem Spec v1.2 change request).
> **Requirements covered:** R-014, R-016, R-021, R-030, R-037, R-038, R-039, R-040, R-041, R-047, R-064, R-075, R-080, R-081, R-082, R-084 (advocate to contest a court-referred challan, listing only), R-086, R-087, R-088.
> **Decisions applied:** D-02, D-05, D-06, D-10, D-11, D-12, D-15, D-16, D-17 · **Challenges applied:** CH-08, CH-09, CH-14, CH-20, CH-22, CH-25, CH-31 · **Non-negotiables tested:** NN-01, NN-11, NN-13, NN-14, NN-17, NN-18, NN-19, NN-20, NN-21, NN-22, NN-23, NN-24, NN-35, NN-39, NN-41, NN-45, NN-46, NN-49, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, frontend 2 — public + delivery, mobile 0.5 shared with P22, integration 1 — OH8/OH9/Route/Academy, QA 1, legal-ops analyst 0.5)

---

## 1. Objective and business outcome

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

## 2. Scope (in / out)

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

## 3. Personas and permissions touched

(Full matrix in Appendix D.)

| Role code | What they can do in P16 |
|---|---|
| Anonymous visitor | Browse, search, filter, compare, read price cards and FAQs, view Academy courses, use the Vidhi service finder (no personal data until contact), request a callback (consented lead to OH3) |
| `IND_OWNER` (incl. Free account with no plan) | Buy services for self or family, accept offers, eSign engagement letters, pay, upload inputs, approve deliverables, raise change requests, review LawDocs service, raise disputes |
| `IND_DELEGATE`, `IND_GUARDIAN` | Act for the individual within delegated scope (purchase only if delegated with `mkp.buy`) |
| `ORG_OWNER`, `ORG_ADMIN` | Buy services and retainers for the company; set who may buy (`mkp.tenant.who_can_buy`) and purchase approval threshold; approve delivery grants for RMs/professionals (P18) |
| `ORG_CLO` | Request and scope services; approve offers within DoA; act as checker on RM-made work under retainers; monitor SLA dashboards |
| `ORG_APPROVER` | Approve purchases above threshold (step-up MFA); eSign engagement letters/SLA schedules as authorised signatory |
| `ORG_MEMBER`, `ORG_DEPT_HEAD` | Raise a service request through the legal intake desk (P13) that the CLO converts into an order; view own requests |
| `ORG_DELEGATED_MAKER` | RM or engaged professional acting as maker inside the tenant under a delivery grant (P18); cannot approve own work |
| `OPS_DELIVERY_LEAD` | Publish and maintain first-party service products (maker), approve offers and discounts within DoA (OH8), assign professionals and RMs, handle escalations |
| `OPS_PROFESSIONAL` | In-house advocate/CS/CA/tax professional delivering **non-reserved** services as a LawDocs employee (NN-41); scope, draft, deliver, log time |
| `OPS_RM` | Retainer relationship manager; maker under grant; prepares monthly reports; cannot accept deliverables for the client |
| `OPS_QA_REVIEWER` | Internal review before release; monthly 10% quality sample; checker on new service products |
| `OPS_CSM`, `OPS_SUPPORT_AGENT` | Renewals, onboarding calls, buyer support; read engagement metadata only, never deliverable content unless granted |
| `OPS_CONSUMER_CASE_MANAGER` | Consumer Help brand services only (ethical wall, NN-23) |
| `PRO_ADVOCATE`, `PRO_CA`, `PRO_CS`, `PRO_TAX_PRACTITIONER`, `PRO_OTHER` | Practitioner workspace: accept/decline assignments after conflict check, scope, deliver in own name where the service is reserved, log time, view payouts; never see buyer data before acceptance beyond the masked brief |
| `PRO_FIRM_ADMIN`, `PRO_FIRM_MEMBER` | Firm-level onboarding, linked account for Route, allocate work inside the firm |
| `PLT_SUPER_ADMIN` | Category tree, profession rule values (with counsel reference and checker), kill switches, guard-rail bands |
| `PLT_LEGAL_REVIEWER` | Reviewer of record for service products, engagement-letter templates and profession rules; attaches counsel-opinion references |
| `PLT_CONTENT_EDITOR` | Service copy, FAQs, explainers, help keys (claims gate via OH14) |
| `PLT_GRIEVANCE_OFFICER` | Marketplace grievance queue (ack ≤ 48 h, resolve ≤ 1 month) |
| `PLT_AUDITOR_RO` | Read-only audit of profession-rule changes, payouts, disputes |
| `AGT_SERVICE_FINDER`, `AGT_SCOPE_DRAFTER` (Appendix H) | Makers only (NN-43): recommend categories/services, draft scope summaries, proposals and monthly reports for human approval |

---

## 4. Functional requirements

### 4A. Storefront and catalogue (D-11; R-041)

- **FR-P16-01 — One storefront.** `apps/public` serves `/marketplace` (home), `/marketplace/{category}`, `/marketplace/s/{slug}` (service product), `/marketplace/compare`, `/marketplace/trainings`, `/marketplace/startups` (bundle hub), `/marketplace/for/{segment}` (segment presets: individuals, families, freelancers, startups, MSMEs, mid-market, NBFCs and regulated entities, professionals, enterprises), `/marketplace/how-it-works`, `/marketplace/ranking` (ranking parameters), `/marketplace/terms`. Server-rendered/statically generated per catalogue version (NN-31); JSON-LD `Service` + `Offer` with `priceSpecification` per package; no prices rendered only by client JavaScript (R5 fact 17). Browsing needs no login, no subscription and no cookie consent beyond strictly necessary cookies.
- **FR-P16-02 — Category tree** (seed and codes in Appendix M §M.2; editable by `PLT_SUPER_ADMIN` with `PLT_LEGAL_REVIEWER` as checker): 01 Agreements & contract drafting · 02 Consultations, contract review & negotiation support · 03 Legal notices & replies · 04 Policies & documentation · 05 Annual reports, board reports & minutes · 06 Board, secretarial & governance support · 07 Compliance testing & audit readiness · 08 Risk assessment, stress testing & scenario analysis · 09 Retainer advisory & managed legal department · 10 Filings, registrations & returns · 11 Startup bundles · 12 Trademarks & IP · 13 Litigation support · 14 Property & family documentation · 15 Execution services (eStamp facilitation, notary/registration appointments) · 16 Consumer Help (separate brand) · 17 LawDocsComply services (group) · 18 Trainings (FinLegal Academy). A service may appear in up to three categories; one is canonical for URLs and breadcrumbs.
- **FR-P16-03 — Service product object** (`mkp.services`, versioned): code `SVC-<CAT>-<nn>`, title, plain-language outcome, who it is for (segments, entity types, States where the service is available), canonical category, **service class** (§4C), **delivering party type** (LAWDOCS_TEAM, LAWDOCS_PANEL, THIRD_PARTY, LDC, ACADEMY, CONSUMER_HELP_BRAND), seller of record (OH8 `selling_entity` ref), scope inclusions, **exclusions** (mandatory, ≥ 1), deliverables (format: DOCX/XLSX/PDF/PDF-A; linked deliverable template), inputs checklist (each item: label, required/optional, accepted file types, "i" key), timeline in business days from inputs complete, revisions included, SLA template (§4G), price model (§4B), packages, add-ons, required formalities (e.g., stamp, notarisation — P08 gate), language(s), delivery mode (remote; in-person add-on by city), related software features ("Works best with eSign — included in Personal"), FAQs (≥ 3), regulatory references (cited, effective-dated), claims-register references for any claim (OH14), status `DRAFT → LINTED → IN_REVIEW → LIVE → PAUSED → RETIRED`, `live_from`, version. A material change creates a new version in review; the LIVE version stays until approval; every engagement snapshots the version it was bought under.
- **FR-P16-04 — Lint before review.** Automated checks block `IN_REVIEW` when: exclusions empty; deliverables or timeline missing; price card incomplete (§4B); prohibited words present (Appendix M §M.8: "best lawyer", "top advocate", "guaranteed", "100% success", "government-approved", "verified expert", "No. 1", "instant approval"); a reserved service class is assigned to a LawDocs-team delivering party (NN-41, `LD-MKP-010`); a regulated-profession service carries a rating widget (NN-21); a statutory fee is shown without basis and date; Consumer Help service lacks the "no outcome promise" statement (NN-23).
- **FR-P16-05 — Search and filters.** OpenSearch (FTS fallback) over titles, outcomes, deliverables and FAQs in the UI languages of D-07; filters: category, segment, entity type, price band, timeline, language, delivery mode, State, seller (LawDocs / LawDocsComply / Academy / Consumer Help brand), "available without a plan" (always true; shown as a reassurance chip). Sort options: relevance, price low→high, price high→low, fastest timeline, newest. **No sort by rating, popularity or professional** for any service delivered by a regulated profession. Ranking parameters are disclosed at `/marketplace/ranking` in descending order of importance (Consumer Protection (E-Commerce) Rules 2020 r.5 [VERIFY sub-rule]; R3 LG-141). Sponsored listings do not exist (`mkp.sponsored.enabled` locked OFF; NN-35).
- **FR-P16-06 — Service page.** Above the fold: title, outcome, "for", landed price card (§4B), timeline, "what you get" (three lines), primary CTA by model ("Buy now" for fixed price; "Get a quote" for quote-only; "Book a scoping call" only where the delivering party's profession mode allows a CTA). Below: scope and exclusions, deliverables with synthetic sample previews, inputs checklist, how delivery works (who delivers, by role level — never a named advocate), formalities and what LawDocs does not do, related free tools ("Draft it free with Vidhi" — template lane, NN-14), FAQs, grievance officer link, seller-of-record panel (legal name, GSTIN, address, customer-care contact — E-Commerce Rules 2020 r.5 [VERIFY]). "Save", "Share", "Compare".
- **FR-P16-07 — Compare.** Up to 3 service products side by side (scope, exclusions, deliverables, timeline, revisions, landed total, SLA, refund rule); "show differences only" toggle; accessible table semantics (`th scope`, row headers).
- **FR-P16-08 — Click budgets.** Home → category → service page ≤ 2 clicks; any service page → paid order ≤ 4 steps for a signed-in user (Buy → package → review fees → Pay) plus the hosted checkout; with no account ≤ 7 taps on mobile / ≤ 8 clicks on web including OTP sign-up (Appendix C J-28, which governs; R-6); "Hire a professional" block on any public document page (R-087) → pre-filled service page in 1 click with the document type attached.

### 4B. Price models, landed price cards and customised offers

- **FR-P16-09 — Price models** (each maps to an OH8 SKU and an RS-LD stream in Appendix L §L.9): `FIXED` (with up to 3 packages), `PER_UNIT` (per page band, per class, per return, per employee, per seat), `MILESTONE`, `RETAINER_MONTHLY`, `RETAINER_ANNUAL`, `HOUR_BANK_TOPUP`, `HOURLY_BAND_CAPPED` (first-party only; not-to-exceed cap mandatory), `QUOTE_ONLY`, `CONSULT_SLOT` (fixed 15/30/60-minute slots at a flat price — **never per-minute metering**, R6 LD-X01), `SUBSCRIPTION_SERVICE` (e.g., monthly contract-desk service).
- **FR-P16-10 — Landed price card (mandatory lines; R1 IMP-079; NN-22, NN-50).** (1) Service or professional fee — label states who earns it ("LawDocs service fee" or "Professional fee — paid to the delivering advocate's firm"); (2) LawDocs platform fee — separate line, shown only where a regulated professional supplies the work (§4C); (3) Government / statutory fees — estimate with basis and date (e.g., "TM-A e-filing fee ₹4,500 per class for individuals, startups and small enterprises; ₹9,000 others — Trade Marks Rules 2017 First Schedule [VERIFY current schedule]"), stamp duty "at actuals, calculated at checkout from the State and instrument" (P08), marked pass-through; (4) GST per supplier — "18% on LawDocs fees", "Advocate's fee: GST payable by you under reverse charge" where the buyer is a business entity, registered or not (Notification 13/2017-CT(R) Sl. 2), or "Advocate's fee: exempt" where the buyer is not a business entity or is a business entity below the registration threshold (Notification 12/2017-CT(R) [VERIFY entry]) (LG-340, LG-341; W.9 LA-18; R6 T-01, T-02 [TAX MEMO]); (5) **Total payable now** in bold, plus "Total incl. GST" if the plan display is ex-GST; (6) what is not included; (7) cancellation and refund rule (one line + link); (8) SLA. Amounts that will be charged come from an OH8 quote (P17 FR-P17-03); the card's pre-quote total is labelled "Estimated — confirmed at checkout" only when a pass-through (stamp duty, court fee) depends on inputs.
- **FR-P16-11 — Member prices and allowances.** Plans (P17) carry allowances (e.g., Personal: one 15-minute documentation-team session a year; Business: six 30-minute documentation-team sessions a year and member price −10% on LawDocs services; Appendix L §L.2–§L.3). These sessions are guided sessions with the LawDocs documentation team, not legal advice; advocate consultations are never bundled into a plan and are sold only as separate fixed-fee `CONSULT_SLOT` products paid to the advocate (NN-21, CH-08; W.9 LA-16) [COUNSEL]. The card shows the visitor's price for their plan when signed in and "Members pay ₹x" otherwise, without strike-through anchor prices that were never charged (NN-50; P17 FR-P17-14). Allowance consumption is metered (`MKP_CONSULT_ALLOWANCE`) and visible in Settings → Billing → Usage.
- **FR-P16-12 — Customised offers (`ofr_`).** `OPS_DELIVERY_LEAD` or an authorised professional builds an offer from a request: scope snapshot, deliverables, milestones, price lines (each with seller of record and stream), discount (within DoA; above DoA goes to OH8 approval), validity (default 15 days, `mkp.offer.validity_days`), assumptions, exclusions, draft engagement letter (§4F). The buyer can comment inline, request changes, accept, or decline with reason. An accepted offer becomes an OH8 quote → order; the offer version hash is stored on the engagement.
- **FR-P16-13 — Price guard-rails.** Category min/max bands (`mkp.price_guardrail.<category>`) block obvious anomalies (e.g., ₹10 annual report) but never fix third-party prices; for the LawDocs Panel, the professional fee comes from the **panel fee schedule** agreed with the panel firm (a schedule by service, complexity and seniority — not a per-advocate price list displayed to the public) [COUNSEL: confirm that publishing panel SKU prices is not "showing fees of advocates" in the sense criticised in *P.N. Vignesh*; OI-P16-02].
- **FR-P16-14 — Quote requests from anonymous visitors.** "Get a quote" collects name, mobile or e-mail, segment, description and optional files only after a DPDP notice with purpose-wise consent (service contact mandatory; marketing optional and unticked — R4-MKT-09); files go to a quarantined intake bucket, virus-scanned, deleted after 30 days if no account is created (`mkp.intake.retention_days`). The lead goes to OH3 with consented contact data only; never document content (NN-19).
- **FR-P16-15 — Consult slots.** Consult products (`CONSULT_SLOT`) sell a practice-area slot, not a person: buyer picks area, language, mode (chat with response SLA, scheduled audio/video, call-back), and a time window; the assignment engine (§4E) assigns. Masked numbers both ways (R1 IMP-005). A 48-hour follow-up chat is included (R1 IMP-008). Auto-refund if the professional does not join within 10 minutes of the slot start (`mkp.consult.no_show_minutes`) — full refund including platform fee, no form to fill (R1 IMP-009).

### 4C. Service classes, commercial models and per-profession switches (D-05; NN-21, NN-41)

- **FR-P16-16 — Service classes** (assigned by `PLT_LEGAL_REVIEWER`; Appendix M §M.3):
  - `RESERVED_ADVOCACY` — legal advice or opinion, representation, appearance, drafting of pleadings for filing, legal notices on an advocate's letterhead: only by an enrolled advocate or firm of advocates **in their own name** (Advocates Act 1961 ss.29, 33; *Bar Council of India v. A.K. Balaji* — R3 LG-110 [VERIFY citation]). Never supplied by LawDocs (the company) (NN-41).
  - `RESERVED_ATTEST` — certifications and audits reserved to practising CAs/CSs/CMAs (e.g., statutory audit, secretarial audit, certificates required by law): only by an eligible practitioner in own name, engaged directly; LawDocs lists such services only where the profession switch allows (default OFF; R3 LG-114–LG-117).
  - `RESERVED_AGENT` — trademark filings and replies before the Registry by a registered trademark agent or advocate (Trade Marks Act 1999 s.145 [VERIFY]); GST practitioner work under PCT-05 (CGST Rules r.83 — R3 LG-127); ERI-route tax filings verified by the taxpayer (R3 LG-124–LG-125).
  - `DOCUMENTATION` — template-based drafting, documentation support, typing, translation (labelled, NN-48), compilation, formatting, proof-reading against the buyer's instructions: LawDocs team (M1) [COUNSEL: boundary with "practice of law" for bespoke drafting; OI-P16-03].
  - `ADVISORY_COMPLIANCE` — compliance management, compliance testing, risk assessment, stress testing and scenario analysis, policy drafting support, board and secretarial support, minutes drafting, annual-report drafting support, governance reviews, regulatory research: LawDocs team (M1) or third parties.
  - `TECHNICAL` — implementation, migration, integration set-up, data-room set-up: M1.
  - `TRAINING` — Academy and corporate training: Academy merchant or M1 for corporate bundles.
  - `FACILITATION` — eStamp facilitation, notary/registration appointment booking, courier, certified-copy retrieval (OFF until counsel; RS-LD-43): M1, pass-through fees at actuals.
- **FR-P16-17 — Commercial models** (per service product and delivering party; Appendix M §M.4):
  - **M1 — LawDocs supplies.** LawDocs (`[LawDocs Operating Entity]`, OH8 `selling_entity`) contracts, invoices through OH8 at 18% forward charge (SAC per tax memo), collects through its Razorpay account, delivers through employees and contractors. Classes: DOCUMENTATION, ADVISORY_COMPLIANCE, TECHNICAL, TRAINING (corporate), FACILITATION. **Default and only model enabled at launch.**
  - **M2 — Professional supplies; platform-collected via Razorpay Route.** The buyer contracts with the professional (engagement letter between them, eSigned in LawDocs) and with LawDocs (marketplace terms) for the platform service. The buyer pays once on Razorpay hosted checkout; **Route** transfers 100% of the professional fee to the professional's KYC'd linked account (on hold until the release event, FR-P16-61) and LawDocs keeps only its separately invoiced platform fee (NN-22; R6 §R6.1.5). The professional issues their own invoice / bill of supply in their name (stored in the engagement). Classes: RESERVED_ADVOCACY, RESERVED_AGENT, RESERVED_ATTEST (if switched on), ADVISORY_COMPLIANCE by third parties. Flag `mkp.model.m2.enabled` OFF; first enabled only for the **LawDocs Panel** after OI-P16-01 and OI-P16-02 close [COUNSEL; R3 LG-112: collection rails only if counsel confirms no fee-sharing].
  - **M3 — Direct engagement, off-platform payment.** The professional contracts, invoices and collects directly; LawDocs hosts the engagement room and charges the buyer only its platform fee. No money of the professional passes through LawDocs. Flag `mkp.model.m3.enabled` OFF (used for enterprise buyers whose procurement requires direct contracting with the firm).
- **FR-P16-18 — Per-profession switches** (`mkp.profession.<code>.<switch>`; PLATFORM tier; values in Appendix M §M.5). Switches: `listing_mode` (OFF, ASSIGNED_ONLY, DIRECTORY_RULE36, FULL), `commission_pct_allowed`, `listing_fee_allowed`, `paid_ranking_allowed`, `referral_reward_allowed`, `ratings_display_allowed`, `cta_allowed`, `buyer_platform_fee_mode` (FLAT, PERCENT_SEPARATE_LINE, NONE), `model_allowed[]`, `counsel_opinion_ref`, `effective_from`. Lawful defaults:

| Profession | listing_mode | Commission / listing fee / paid ranking / referral reward | Ratings display | Buyer platform fee | Models | Lock |
|---|---|---|---|---|---|---|
| Advocate / law firm (`PRO_ADVOCATE`) | ASSIGNED_ONLY (directory page OFF) | **Hard OFF — not configurable** (BCI Rules Part VI Ch II r.36; fee-sharing bar [VERIFY rule number]; Madras HC 3 Jul 2024; OH8 deny list) | Hard OFF | FLAT ₹49–₹199 per booking (seed ₹99) | M2, M3 | Permanently locked for the four commercial fields; mode change needs counsel ref + checker |
| Chartered accountant in practice (`PRO_CA`) | OFF (ICAI ESB announcement 23 Oct 2019 — R3 LG-115) | OFF (CA Act 1949 First Schedule Part I cl.(2), (3), (6), (7)) | OFF | FLAT | none until opinion | Locked pending counsel opinion + checker |
| Company secretary in practice (`PRO_CS`) | OFF (CS Act 1980 First Schedule analogues [VERIFY]; R3 LG-117) | OFF | OFF | FLAT | none until opinion | Locked pending counsel opinion + checker |
| Cost accountant | OFF | OFF (ICMAI referral-network bar — R6 P-04) | OFF | FLAT | none | Locked |
| Trademark agent (non-advocate) | ASSIGNED_ONLY | OFF recommended [VERIFY agent conduct rules] | OFF | FLAT | M2 | Locked pending counsel |
| Tax return preparer / GST practitioner (non-CA) | ASSIGNED_ONLY | `commission_pct_allowed` OFF by default (≤ 15% permitted only after legal review — RS-LD-26) | Aggregate only, moderated | FLAT | M2 | Counsel ref + checker |
| Notary (facilitation only) | OFF | OFF | OFF | Facilitation fee | M1 facilitation | Locked (Notaries Act 1952) |
| Translators, typists, couriers, process servers, valuers (non-statutory), investigators | FULL | Take rate 10–20% allowed (RS-LD-25) | Allowed (IS 19000 moderation) | NONE | M2 | Checker |
| LawDocs in-house professionals (`OPS_PROFESSIONAL`) | n/a — LawDocs team | n/a | Aggregate CSAT of LawDocs services only | n/a | M1 | — |

  A change to any switch is a maker-checker action (NN-18): maker `PLT_SUPER_ADMIN`, checker `PLT_LEGAL_REVIEWER` (≠ maker), mandatory `counsel_opinion_ref` (document in vault, hash stored) for any regulated profession; effective-dated; audit-ledgered; kill switch per profession (NN-39). The four advocate commercial fields have no write path at all (schema constraint + CI test `NN-21_advocate_commercial_fields_immutable`).
- **FR-P16-19 — Render allow-lists.** Every public or buyer-facing response that includes a professional uses a fixed schema per profession mode: `RULE36_V1` (name, address, telephone, e-mail, enrolment number, enrolment date, State Bar Council, place of practice, professional and academic qualifications, practice areas — BCI Rule 36 proviso and Schedule, R3 LG-111 [VERIFY Schedule wording]; only with the advocate's consent), `PRO_SERVICE_V1` (role level, languages, years band — for assignment confirmations inside an engagement only), `PROVIDER_FULL_V1` (non-regulated providers). Ratings, reviews, testimonials, photos, fees per person, case counts, success rates, "top/premium/featured/verified expert" labels, client names and "book this professional" buttons cannot be rendered for advocates under any mode; CI fails if a forbidden field appears in an advocate response (`NN-21_profession_render_allowlist`).
- **FR-P16-20 — Optional Rule-36 directory page.** `/marketplace/directory/advocates` exists only if `mkp.directory.advocates.enabled` is ON (default OFF; R3 LG-113: OFF at launch pending counsel and the Supreme Court outcome in *Sulekha.com v. P.N. Vignesh*, SLP (C) 25794/2024). When ON: `RULE36_V1` only, seeded random or alphabetical order with the seed logged, filters by State/district/practice area/language, disclaimer "Information furnished by advocates on request; not solicitation or a recommendation", no CTA, no link from commerce listings.
- **FR-P16-21 — No marketing of individual professionals.** OH7/marketing campaigns, the blog and Vidhi never promote a named advocate, CA or CS (R4-MKT-01–03); marketing promotes LawDocs service products and categories only.
- **FR-P16-22 — Professional SaaS is neutral.** A professional may buy a Pro plan (RS-LD-30). Plan status, spend or tenure is never readable by assignment, ordering or search (test `NN-21_plan_status_not_in_ranking_features`).

### 4D. Professional registry and onboarding (P01 verification; OH9)

- **FR-P16-23 — Registry object (`mkp.professionals`, `pro_`).** Person or firm; profession codes; source (LAWDOCS_EMPLOYEE from OH10 provisioning, LAWDOCS_PANEL, THIRD_PARTY); OH9 `professional_id` and credential version; KYC ref (P01 `kyc_`); practice areas, languages, States/districts, courts/forums, service classes eligible, capacity (concurrent engagements, hours/week), availability calendar, professional-indemnity cover, conflict declarations, linked account ref (Route; firm-level allowed), status. Public data is limited to the allow-list of FR-P16-19 and only with consent.
- **FR-P16-24 — Onboarding states.** `INVITED | APPLIED → PROFILE_SUBMITTED → KYC_VERIFIED (P01) → CREDENTIALS_VERIFIED (OH9) → DUE_DILIGENCE → AGREEMENT_SIGNED (panel/provider terms, DPA, code of conduct — eSigned, P08) → ROUTE_LINKED (M2 only) → ACTIVE → SUSPENDED → ACTIVE | REMOVED`; `RETURNED` (reasons; 30-day resubmission); `WITHDRAWN` (professional's request). Maker: `OPS_ONBOARDING`; checker for ACTIVE: `PLT_LEGAL_REVIEWER`.
- **FR-P16-25 — Evidence checklist** (Appendix M §M.7): advocates — enrolment number, State Bar Council, enrolment date, certificate of practice where applicable [VERIFY], no-disciplinary-order declaration; CAs/CSs — membership and certificate of practice, firm registration, peer review where relevant; TM agents — registration [VERIFY register]; GST practitioners — enrolment; all — PAN, GSTIN (if registered), bank account by penny-drop with name match ≥ 85% (via Razorpay Route KYC for linked accounts), PI insurance (panel firms: mandatory, amount `[OWNER TO SET]`), information-security questionnaire if they will access tenant data, data-protection undertaking. Officers verify from official registers only; no scraping (NN-05). LegalKart's weakness (Terms admit no separate verification — R1 §3.5) is the reason this list is mandatory.
- **FR-P16-26 — Credential watch.** OH9 `ProfessionalSuspended` (received via `int`) sets the professional to `SUSPENDED` within 1 hour, blocks new assignments, flags live engagements to `OPS_DELIVERY_LEAD` for re-assignment with buyer consent; expiry alerts at 60/30 days; annual re-verification (R1 IMP-004).
- **FR-P16-27 — LawDocs Panel.** A contracted advocates' firm (or firms) and individual panel advocates engaged under a **panel agreement** with LawDocs that: (a) confirms the advocate supplies legal services in their own name and bears professional responsibility; (b) fixes the panel fee schedule; (c) states that no part of the advocate's fee is shared with LawDocs and LawDocs pays no referral reward; (d) sets SLAs, quality review and confidentiality; (e) sets the Route linked account. [COUNSEL: panel structure — affiliated firm vs contracted panel; OI-P16-01; R6 §R6.8 item 1.]
- **FR-P16-28 — In-house professionals.** LawDocs employees who are advocates, CAs or CSs deliver only non-reserved classes as employees; their names appear on deliverables as "Prepared by LawDocs (reviewer: name, role)" — never with professional seals, enrolment numbers as a credential signal, or "advocate" titles that imply legal practice by the company (BCI r.49 — R3 LG-112; NN-41).
- **FR-P16-29 — Practitioner firms.** `PRO_FIRM_ADMIN` manages members, linked account, capacity and internal allocation; a firm member works only on engagements allocated to them; firm-level conflict declarations apply to all members.

### 4E. Assignment and conflict checks

- **FR-P16-30 — Assignment engine.** For services fulfilled by assigned professionals: eligible pool = ACTIVE professionals with the service class, practice area, language, State/forum, capacity and no conflict; ordering = rotation within the pool weighted only by objective fit (language match, forum match, current load, SLA attainment over 90 days for operational reliability); **never** by payment, plan status, ratings or tenure (R1 IMP-003; OH9 ordering rule). The basis (`ROTATION`, `RULE`, `REASONED_EXCEPTION` with reason) is logged on the engagement.
- **FR-P16-31 — Buyer choice.** The buyer may (a) accept the assignment, (b) request a different professional once without charge before work starts (R1 IMP-003), or (c) for M3 engagements, name a professional they already know. No buyer-facing shortlist ranks advocates. [COUNSEL: confirm assignment with a buyer-side platform fee is not "aiding solicitation" under BCI r.37 — OI-P16-02.]
- **FR-P16-32 — Conflict check.** Before an offer is sent or an assignment accepted: (1) automated check of party names (normalised, salted-hash comparison) and PAN/CIN where provided against the professional's prior and current engagements on LawDocs and their firm's declarations; (2) group check through OH `POST /v1/conflicts/check` for institutional relationships (group lender/insurer clients for Consumer Help, Equator neutral flag — NN-23); (3) the professional confirms "no conflict" with a recorded declaration. A hit blocks progress (`LD-MKP-020`) until cleared by `OPS_DELIVERY_LEAD` with reason or re-assigned. Opposing-party names are visible to the professional only after they accept the masked brief (masked brief = category, forum type, State, value band).
- **FR-P16-33 — Independence checks.** For compliance testing, audit readiness and secretarial support: block where the delivering party is the buyer's statutory, secretarial or internal auditor for the same scope (buyer declares auditors at order; LDC independence rules mirrored for group listings — LDC P21 FR-P21-14).
- **FR-P16-34 — Capacity and SLA fallback.** If no eligible professional accepts within `mkp.assignment.accept_window_hours` (default 4 business hours), the engagement escalates to `OPS_DELIVERY_LEAD`; if no professional is available within 1 business day, the buyer is offered a full refund or a new date — never silent delay.

### 4F. Engagement lifecycle (`eng_`; business ID `LD-ENG-YYYY-nnnnnn`)

- **FR-P16-35 — States** (§5.1): `REQUESTED → SCOPING → OFFERED → ACCEPTED → CONTRACTED → PAID (or ADVANCE_PAID) → INPUTS_PENDING → IN_DELIVERY → DELIVERED (per milestone) → ACCEPTED_BY_BUYER | REVISION_REQUESTED → CLOSED → (REVIEWED)`; side states `ON_HOLD`, `CHANGE_REQUESTED`, `CANCELLED`, `DISPUTED`, `REFUNDED`. Fixed-price products skip SCOPING and OFFERED (buy now → CONTRACTED by click-wrap or eSign per FR-P16-37).
- **FR-P16-36 — Scoping.** Structured intake per service (inputs checklist; facts pre-filled from the workspace profile — entity, State, counterparty, document in vault); optional scoping call (Teams/Google Meet link via `WORKSPACE_PORT`; recorded only with consent); `AGT_SCOPE_DRAFTER` drafts a scope summary that the professional edits and owns (NN-14).
- **FR-P16-37 — Engagement letter / SOW.** Generated from Appendix M §M.9 templates via `@infrabyx/docgen` (P06): parties (buyer; supplier per model; LawDocs as platform where M2/M3), scope by reference to the service version and scope snapshot, exclusions, deliverables and acceptance, inputs and dependencies, timeline from inputs complete, fees with each line's supplier, GST/RCM statement, payment and refund terms, TDS note, change control, confidentiality, data protection (roles per Appendix M §M.12), IP in deliverables (buyer owns final deliverables on payment; supplier keeps pre-existing know-how), professional-conduct statements, limitation of liability, termination, governing law and dispute resolution, electronic execution. Negotiation of non-standard terms uses P07 redlines (versions, NN-37). Execution: eSign through P08 (Aadhaar eSign, DSC or electronic signature) for retainers and any engagement above `mkp.contract.clickwrap_max_value` (default ₹25,000 [OWNER TO SET]); OTP click-wrap with identity, timestamp, IP and document hash (IT Act 2000 s.10A [INTERP]) below it. The signed PDF and evidence pack go to the buyer's vault (NN-09, NN-10).
- **FR-P16-38 — Payment terms.** Fixed price ≤ ₹25,000: 100% at order; above: 50/50 or per milestone; retainers: monthly or annual in advance; enterprise: invoice-later per contract (OH8). Pass-through amounts (stamp duty, court fees, government fees) are collected only when the instrument or filing is ready, as separate lines (NN-08, NN-22).
- **FR-P16-39 — Inputs.** Checklist with per-item upload into a sealed engagement folder in the buyer's vault (Personal or Company workspace); reminders D+3 and D+7; timeline clock starts only when required inputs are complete; WhatsApp/handwritten inputs may be processed by P05 (labelled derived renditions, NN-09).
- **FR-P16-40 — Delivery.** Milestones with due dates on the buyer's legal calendar; tasks for the delivery team (`wf`); deliverables uploaded as versioned documents (DOCX with tracked changes when revising the buyer's document — P07 redline engine); mandatory internal review by `OPS_QA_REVIEWER` for M1 before release (`mkp.qa.review_required`, default ON); release notifies the buyer. Deliverables land **directly in the client vault** — Company: `09 Services and Engagements/<FY>/<Engagement> (LD-ENG-…)/03 Deliverables/` and, when the deliverable is an agreement, a linked copy in the agreement record (P07); Individual: the category folder of the document (e.g., `02 Property/`) with an engagement link. An AI-drafted deliverable for an individual is never released as "reviewed" unless a qualified reviewer approved it (NN-14).
- **FR-P16-41 — Acceptance.** Buyer accepts or requests revision (counted against revisions included); deemed acceptance only if the engagement letter says so (default 7 business days after release with reminders at day 3 and day 6 [OWNER TO SET]); `DeliverableAccepted` releases on-hold Route transfers for that milestone (FR-P16-61).
- **FR-P16-42 — Change requests (`ecr_`; engagement change request — `chg_` is reserved for engineering change records, Appendix B §B.1).** Either side proposes a scope/price/timeline delta; buyer approves (and, for Company workspaces above threshold, `ORG_APPROVER` with step-up MFA); approved delta creates an OH8 quote amendment and an engagement-letter amendment (eSigned if the original was eSigned); work beyond scope cannot be logged against the engagement until approved (`LD-MKP-031`).
- **FR-P16-43 — Close-out.** Final invoice references, deliverables index (auto-generated PDF/XLSX), knowledge-transfer note, feedback request (§4J), engagement record filed in the export structure (§13).
- **FR-P16-44 — Messages and meetings.** Each engagement has a secure thread (`msg`; masked contact details; off-platform contact-sharing nudges — R1 IMP-013, warning only), meeting links, file exchange (virus-scanned, hashed), approvals, activity log visible to the buyer.

### 4G. Retainers (`rtn_`; R-039, R-064, R-080)

- **FR-P16-45 — Retainer packages.** Seeded packages (Appendix L §L.7; Appendix M §M.2 category 09): **Startup Legal Officer**, **SME Legal Desk**, **NBFC Legal & Compliance Retainer**, **Managed Legal Department** (RS-LD-21, OFF until structure memo), plus **Custom retainer**. Each defines: service basket (service codes × monthly quantities), hour bank (hours/month by role level), named roles (RM, reviewer, panel advocate firm for reserved work), meeting cadence, SLA schedule, exclusions (litigation representation unless separately engaged, attest services, filings on portals using client credentials — CH-10, board decisions), term, notice, price lines per supplier, overage rate, rollover rule.
- **FR-P16-46 — Customised scope.** The retainer builder (`apps/delivery`) lets `OPS_DELIVERY_LEAD` add/remove basket items, set hours, SLA targets and price within DoA; the offer shows the client a plain-language "What we will do every month" list plus the formal SLA schedule. Split supply is explicit: LawDocs (M1) supplies coordination, documentation, compliance and RM services; the panel firm (M2) supplies legal advice and opinions under its own engagement letter, both signed in one ceremony (P08 multi-document envelope).
- **FR-P16-47 — SLA schedule (`sla_`) eSigned in-tool.** Metrics per service type: acknowledgement time, turnaround (business days from complete inputs), report date, escalation matrix, service credits for missed SLAs (default 5% of monthly LawDocs fee per breached category, capped at 20% — `[OWNER TO SET]`), measurement method, exclusions (client delays, force majeure). Clocks run on the IST business calendar of the client's State (holiday calendars, `wf`). The SLA schedule is a document version eSigned by both parties (P08); amendments are new versions, eSigned.
- **FR-P16-48 — Activation and RM-as-maker.** On `CONTRACTED`: P18 creates the client section, proposes delivery grants (RM as `ORG_DELEGATED_MAKER` in named departments/functions; client employee as checker — R-064) for `ORG_ADMIN` approval (NN-17); kick-off meeting scheduled; obligations, renewal dates and deliverable calendar seeded. Multiple makers allowed; the client may also create its own maker users for the professional services (R-064). The RM can never be checker or approver (NN-18).
- **FR-P16-49 — Hour bank.** Time entries by delivery staff and panel professionals against tasks (`mkp.time_entries`; declared work sessions only — NN-33); client sees hours by service category and role level (names optional per `mkp.retainer.show_staff_names`, T, default OFF); alerts at 70%, 90%, 100%; **hard stop at 100%** unless the client pre-approved overage hours (`overage_preapproved_hours`) or approves a top-up (`HOUR_BANK_TOPUP`, RS-LD-22); rollover of unused hours one month by default (`mkp.retainer.hour_rollover_months`, 0–3). Utilisation target 70–85% (R6 §R6.7) is an internal metric only.
- **FR-P16-50 — Milestones and statutory work.** Retainer deliverables with statutory due dates (e.g., AGM notice, annual return support) are scheduled backwards from the due date with a "submission-ready ≥ 2 business days before due" SLA where inputs were complete ≥ 7 business days before.
- **FR-P16-51 — Monthly service report.** Auto-drafted by `AGT_SCOPE_DRAFTER` from engagement data (work done, deliverables, hours, SLA table, items pending with the client, upcoming deadlines, risks observed within scope, next-month plan), RM-reviewed, released to the client's vault and dashboard by the 7th business day.
- **FR-P16-52 — Renewal and exit.** Renewal notices at T-60 and T-30 with any price change (≥ 30 days before effect); one-click renew, change scope, or give notice; on exit: deliverables index, work-in-progress hand-over pack, revocation of delivery grants on the effective date (automatic, logged, client notified), final SLA statement; no statutory work abandoned mid-deadline — in-flight items are completed or handed over with acknowledgement.
- **FR-P16-53 — Suspension for non-payment.** Follows OH8 dunning (P17 §4J); a retainer in `SUSPENDED` stops new non-statutory work only; items with a statutory due date ≤ 30 days continue or are handed over with notice.

### 4H. Practitioner workspace (`apps/delivery`)

- **FR-P16-54 — Queue.** Assignments offered (masked brief, SLA, fee, accept/decline with reason — CONFLICT, CAPACITY, OUT_OF_SCOPE, PROFESSION_RULE), active engagements (kanban by state), due today, overdue, revisions requested; keyboard shortcuts (`A` accept, `D` decline, `→` advance with confirmation).
- **FR-P16-55 — Engagement room (practitioner view).** Scope snapshot, inputs, thread, deliverable upload with version compare, internal notes (never visible to the buyer, NN-37), time entries, milestone release request, change-request proposal, conflict declaration, and the client vault folder for this engagement only — access exists only while the engagement is active plus `mkp.practitioner.post_close_access_days` (default 7) and always through an engagement-scoped grant (NN-17).
- **FR-P16-56 — Payouts view.** For M2: Route transfer status per milestone (`ON_HOLD`, `RELEASED`, `SETTLED`, `REVERSED`), TDS deducted under the e-commerce operator provision (Income-tax Act 2025 s.393(1) Table Sl. 8(v), 0.1% — R6 T-07 [VERIFY][TAX MEMO]), GST TCS where applicable (CGST Act s.52 — R6 T-05 [TAX MEMO]), monthly statement download. LawDocs never shows or computes a commission on the professional's fee because there is none.
- **FR-P16-57 — Templates and tools.** Professionals use the LawDocs template and clause library (P06), redline engine (P07), Vidhi drafting with labelling (P09), and evidence/translation tools (P05) inside the engagement; AI credits consumed in delivery are charged to the delivery budget, not the buyer.
- **FR-P16-58 — Professional's own clients.** A professional who buys a Pro plan gets a separate Company workspace for their own practice; nothing from marketplace engagements flows into it except their own payout statements; buying the plan never creates a listing (FR-P16-22).

### 4I. Payments, Route settlement, invoices and tax (NN-22; CH-25)

- **FR-P16-59 — Checkout.** Always through P17 `BILLING_PORT.order()` → OH8 → Razorpay hosted checkout (top-level redirect, SAQ A; no card data). The order carries one line per supplier and stream: LawDocs service fee (M1), professional fee (M2, Route transfer instruction), LawDocs platform fee, pass-through lines, GST per line.
- **FR-P16-60 — Route linked accounts.** Each M2 professional or firm is a Razorpay Route linked account created and KYC'd through OH8 (penny-test validation); LawDocs stores only the linked-account reference and status (R6 B-35). [VERIFY Route transfer fee and MCC approval for a legal-services marketplace; R6 §R6.8 item 4.]
- **FR-P16-61 — Hold and release.** Transfers are created `on_hold` and released on: milestone `DeliverableAccepted` (or deemed acceptance), consult completed + 48-hour follow-up window closed, or dispute outcome; release instructions carry idempotency keys `(eng_id, milestone_seq, attempt)` and are reconciled daily against Razorpay settlement reports (NN-46). Refunds and partial refunds use Route reversals and an OH8 credit note for LawDocs's own fee; maker-checker above ₹25,000 (NN-18).
- **FR-P16-62 — Invoices by supplier.** M1: OH8 tax invoice from the LawDocs selling entity (CGST Rules r.46), e-mailed to the buyer's billing contacts with PDF and filed in the vault (`10 Billing and Invoices/<FY>/` company; `10 Receipts and Invoices/<Year>/` individual). M2: the professional's invoice/bill of supply generated from the engagement data in the professional's name with their GSTIN or registration status, marked "Tax payable under reverse charge by the recipient" where an advocate supplies a business entity (Notification 13/2017-CT(R) Sl. 2 — R6 T-01) and "Exempt" where the recipient is not a business entity or is a business entity below the registration threshold (Notification 12/2017-CT(R) [VERIFY entry] — LG-341; R6 T-02); LawDocs platform fee invoiced by LawDocs at 18%. Pass-through lines carry pure-agent treatment (CGST Rules r.33 [TAX MEMO]).
- **FR-P16-63 — E-commerce operator duties.** When M2 is ON: GST registration as ECO, TCS 0.5% on net taxable supplies made through LawDocs by other suppliers where LawDocs collects consideration (CGST Act s.52; Notification 15/2024-CT), excluding RCM and exempt supplies [TAX MEMO]; GSTR-8 data from OH8; income-tax TDS 0.1% on gross services facilitated (s.393(1) Sl. 8(v) [VERIFY]); seller details on listing and invoice (E-Commerce Rules 2020 r.5 [VERIFY]); grievance officer details on every page.
- **FR-P16-64 — Buyer TDS.** Business buyers may deduct TDS on LawDocs fees and on professional fees (s.393(1) Sl. 6(iii).D(a)/(b) [VERIFY]); certificate upload in P17 Settings → Billing → Tax documents per invoice; the professional uploads/receives their own certificates.

### 4J. Reviews, feedback and quality (NN-49; CH-20; R-088)

- **FR-P16-65 — Reviews of LawDocs services only.** After `CLOSED`, the buyer may rate and review **the LawDocs service** (ordering experience, timeliness, communication, platform) — never a named advocate or regulated professional. One review per engagement; only verified purchasers; consent to display; displayed **without photos by default** (R-088), with date, service name and buyer type (not name unless consented); no incentives conditional on positive reviews; no suppression of negative reviews; moderation per IS 19000:2022 and the E-Commerce Rules 2020 (NN-49); LawDocs may reply once. Aggregate scores show count, period and method. Reviews about an advocate's legal work are stored as **private feedback** for QA and never displayed (R3 LG-111, LG-143).
- **FR-P16-66 — Private professional feedback.** A structured post-engagement survey (on time, clarity, responsiveness) goes to `OPS_QA_REVIEWER` and the professional privately; used for operational reliability (FR-P16-30) and panel review, never published, never sold.
- **FR-P16-67 — Quality sampling.** `OPS_QA_REVIEWER` samples 10% of closed M1 engagements and 5% of M2 engagements monthly (for M2: process quality only — timeliness, scope fit, documentation — not the legal merits, which stay with the advocate, NN-41); findings create corrective actions and, for repeated breaches, panel review.

### 4K. Disputes, cancellations, refunds and grievance

- **FR-P16-68 — Grievance officer.** Name, designation and contact of the marketplace grievance officer on every marketplace page footer, order confirmation and invoice e-mail; acknowledge ≤ 48 hours, resolve ≤ 1 month (E-Commerce Rules 2020 r.4(5) [VERIFY]; the 7-day IT Rules clock governs content grievances — NN-26).
- **FR-P16-69 — Dispute flow** (§5.4): buyer raises (DELAY, QUALITY, SCOPE, BILLING, CONDUCT, CONFIDENTIALITY, NO_SHOW) → supplier response ≤ 5 business days → LawDocs review (M1: OH6 `client_complaint` as a LawDocs service complaint; M2/M3: facilitation, ≤ 10 business days) → outcome (re-work, partial refund, full refund, no action) → closure with external remedies stated (consumer commission where applicable, contract dispute clause). Holds on Route transfers stay until outcome. Equator is not suggested by default (`mkp.disputes.show_adr_options`, OFF) to avoid self-dealing optics.
- **FR-P16-70 — Cancellation and refunds** (Appendix M §M.10): before work starts — full refund (platform fee included); after scoping, before work — refund less a disclosed scoping fee if stated on the card; after inputs — milestones delivered are payable, undelivered refunded; consult no-show — automatic full refund; retainers — notice period, prepaid months beyond notice refunded; refunds to the original method within 7 working days of approval [OWNER TO SET], each with a credit note (NN-22). No wallet balance is ever created by a refund.
- **FR-P16-71 — Escalation.** SLA breach or no response escalates automatically to `OPS_DELIVERY_LEAD` at 1× and to the head of delivery at 2× the SLA; buyers see escalation status (R1 IMP-012).

### 4L. FinLegal Academy (D-16; R-041, R-081)

- **FR-P16-72 — Catalogue feed (`aca`).** `ACADEMY_PORT` pulls the catalogue from trainings.lawdocs.in — Graphy API if available, else a signed JSON/CSV feed published daily by the Academy team [VERIFY Graphy API/feed capability; R5 §1.3]: fields in Appendix M §M.11 (course id, title, category, audience, level, format, duration, language, price, MRP, next batches, certificate type, trainer display name only with consent, URL, updated_at, feed hash). Validate schema, price and URL allow-list; diff; publish to `/marketplace/trainings`. No paid course content (videos, PDFs, assessments) is copied (D-16).
- **FR-P16-73 — Enrolment.** Individual enrolment deep-links to the Academy checkout (Academy is merchant for individual courses unless the owner moves them into OH8 — OI-P16-06); SSO where Graphy supports it [VERIFY]. Corporate seat bundles, custom batches and in-house sessions are first-party offers quoted and invoiced via OH8 (RS-LD-32). Plan allowances (Business: 2 compliance micro-course seats/year; Enterprise: 5 — Appendix L) issue coupon codes through the Academy.
- **FR-P16-74 — Certificates.** With the learner's consent, completion certificates (PDF, certificate id, course, date, verification URL) are imported into the learner's Personal vault or, for corporate bundles, the company's HR training records (P13 `hr`), linkable as evidence to obligations (e.g., POSH awareness). Without consent nothing is imported and the count withheld is shown.
- **FR-P16-75 — Brand and stale feed.** Display name setting `aca.display_name` (default "FinLegal Academy"; R5 found the live site branded "LawDocs Trainings" with wPractical leakage — OI-P16-07). If the feed fails for > 7 days (`aca.cache_max_age_days`), prices and batch dates are hidden and each course links to the Academy for current details. Course reviews copied from the Academy are not displayed (R5: identical reviews on every course — NN-20, NN-49).

### 4M. LawDocsComply services and Equator link (D-11; NN-24)

- **FR-P16-76 — Group listings.** LawDocsComply service products (compliance retainers, policy packs, ICAAP, returns support, certification readiness) appear on the storefront from the OH8 catalogue with seller of record = the LDC selling entity and a "Delivered by LawDocsComply" panel. Ordering creates an OH8 order for the LDC entity; fulfilment happens in LDC. LawDocs hands the order context to LDC only through `int` with the buyer's consent artefact (proposed event `in.infrabyx.ops.ServiceOrderRouted.v1` — Appendix Y §Y.7.9; LDC reports fulfilment status back with `in.infrabyx.ops.ServiceOrderStatusChanged.v1`; NN-24); no LawDocs tenant data moves without consent. LDC shows the same listings in-app (D-11). RE buyers see LDC's guard-rail notices (outsourcing of core management functions) on these pages.
- **FR-P16-77 — Equator.** The "Disputes & ADR" information block may show a neutral link to Equator's own site only if `mkp.category.adr.equator_link` is ON (default OFF; Ecosystem Spec §8.6); no fee, no referral reward, no pre-selection.

### 4N. Consumer Help listings (D-06; NN-23; CH-22, CH-31)

- **FR-P16-78 — Separate brand.** Consumer Help services (loan/lending and insurance grievance drafting and escalation support, credit-report dispute drafting, challan status and contest help, vehicle-sale agreements) are listed in category 16 under `[Consumer Help Brand]` with that brand's entity profile as seller of record (`chp` brand config), its own grievance officer and terms. Delivery runs in P15 under the ethical wall; this phase supplies catalogue, checkout and engagement rails only.
- **FR-P16-79 — Consumer Help rules on the card.** Flat fees only (RS-LD-39 OFF until memo); success fee stream RS-LD-40 locked OFF and never available where an advocate acts (BCI r.20 — R6 C-4; CH-31); mandatory statements: "We do not promise any outcome, waiver or settlement"; "You pay fines, challans and dues only on the official portal" (NN-23); "Before the RBI Ombudsman, an advocate cannot act as your authorised representative" where the RB-IOS 2026 clause applies [VERIFY clause — conventions fact 13]. Challan contest by advocate (R-084) is an M2 `RESERVED_ADVOCACY` product with a flat fee and court fine at actuals paid by the user on the official channel.

### 4O. Buying without a plan, entry points and fewer clicks (R-030, R-040, R-087)

- **FR-P16-80 — No plan needed.** Any signed-in account (Free included) can buy any service; the order never requires a subscription; the post-purchase screen explains, without pressure, what a plan would add (one line, dismissible; no pre-ticked add-on — NN-50). Company buyers without a Company workspace get one created in Free status with the engagement inside it, so records are never orphaned.
- **FR-P16-81 — Contextual entry points.** "Hire a professional" blocks on public document pages (R-087) and in-product "Get help with this" links on: a draft in the Drafting Studio ("Professional review of this draft — ₹499 for ≤ 5 pages"), an incoming legal notice in the vault, a TM objection in the IP portfolio, a hearing in litigation, an overdue obligation in the Company Legal Department OS, an eSign-ineligible instrument (notary/registration appointment). The drawer opens pre-filtered with the context attached (document reference, not content, until the buyer confirms). Suppressible per tenant (`mkp.tenant.contextual_offers`, T, default ON) and never shown for restricted professions as personalised promotion of a person (NN-21).
- **FR-P16-82 — Vidhi service finder.** `AGT_SERVICE_FINDER` recommends categories and service products from a described need, states that LawDocs services are first-party, never recommends a named advocate/CA/CS, and hands off to a human on request (NN-14, NN-43).
- **FR-P16-83 — One-click re-order.** Recurring services (annual policy review, annual report drafting, AGM support, TM renewal) can be re-ordered with last year's scope pre-filled, subject to fresh conflict and independence checks.
- **FR-P16-84 — Startup bundles (R-082).** `/marketplace/startups` shows bundles (Founder Kit, Incorporation + Compliance Year 1, Fundraise Docs, Brand Protection) assembled from service products with a bundle price shown as the sum of lines minus a disclosed bundle discount; each line keeps its own supplier, invoice and refund rule; bundles never include an auto-renewing subscription without a separate, unticked opt-in (R6 LD-X03; NN-50).

---

## 5. Workflows and state machines

State machine: Appendix A §A.51 governs §5.1–§5.5 (engagement, retainer, service product, dispute, Route payout); A.5 governs professional onboarding (Resolution R-A-03: credential status drives onboarding SUSPENDED); P14 service orders are the `bsv` profile of the engagement machine (A.49; R-A-18).

### 5.1 Engagement (`mkp.engagements.state`)

| State | Entry | Allowed transitions | Actor | Guard | Side-effects / events |
|---|---|---|---|---|---|
| REQUESTED | Quote request or "Get a quote" | SCOPING, DECLINED_BY_SUPPLIER | System / `OPS_DELIVERY_LEAD` | Consent artefact present | `ServiceRequested`; triage SLA 1 BD |
| SCOPING | Triage accepted | OFFERED, ON_HOLD | Professional / delivery lead | Conflict check PASS (FR-P16-32) | Scope draft by agent (maker) |
| OFFERED | Offer sent | ACCEPTED, DECLINED_BY_BUYER, EXPIRED | Buyer | Offer validity; independence check PASS | `OfferIssued` |
| ACCEPTED | Buyer accepts | CONTRACTED | Buyer | Price lines confirmed by OH8 quote | OH8 quote → order draft |
| CONTRACTED | Engagement letter executed (eSign or click-wrap) | PAID / ADVANCE_PAID, CANCELLED | Buyer + supplier | Letter version hash on all signatures; formalities gate N/A | `EngagementContracted`; letter + evidence pack to vault |
| PAID | `SubscriptionPaymentReceived` for the order (via P17) | INPUTS_PENDING | System | Server-side payment verification (never redirect) | Route transfers created `on_hold` (M2) |
| INPUTS_PENDING | Payment captured | IN_DELIVERY, ON_HOLD, CANCELLED | Buyer | Required inputs complete | Reminders D+3, D+7; clock not started |
| IN_DELIVERY | Inputs complete | DELIVERED, CHANGE_REQUESTED, ON_HOLD, DISPUTED | Supplier | Time logged only against approved scope | Timeline/SLA clocks run (Temporal) |
| CHANGE_REQUESTED | Delta proposed | IN_DELIVERY | Buyer approves/rejects | Approver per threshold; amendment executed | `mkp.ChangeRequestApproved` / `mkp.ChangeRequestRejected`; OH8 quote amendment |
| DELIVERED | Milestone released after QA | ACCEPTED_BY_BUYER, REVISION_REQUESTED, DISPUTED | Buyer | QA review passed (M1) | `MilestoneDelivered`; deemed-acceptance timer |
| REVISION_REQUESTED | Buyer requests revision | IN_DELIVERY | Supplier | Revisions remaining > 0, else change request | Counter decremented |
| ACCEPTED_BY_BUYER | Accept or deemed | IN_DELIVERY (next milestone), CLOSED | Buyer / system | Deemed only if letter allows | `DeliverableAccepted`; Route release |
| CLOSED | All milestones accepted | REVIEWED | System | Final invoice issued | `EngagementClosed`; export map updated; review request |
| ON_HOLD | Reason + review date | prior state | Supplier / buyer | Reason code | Clocks paused; buyer notified |
| CANCELLED | Per terms | REFUNDED | Buyer / supplier | Refund rule computed | `EngagementCancelled`; credit note / reversal |
| DISPUTED | Dispute raised | prior state, REFUNDED, CLOSED | Grievance flow | §5.4 | Route holds frozen |

Guards across states: delivery staff cannot accept on the buyer's behalf; an agent cannot move any state that is a human decision (NN-13, NN-43); every transition writes the audit ledger in the same transaction (NN-45).

### 5.2 Retainer (`mkp.retainers.state`)

```
OFFERED → CONTRACTED (engagement letter + SLA schedule eSigned; panel letter if split supply)
  → ONBOARDING (P18 grants proposed → ORG_ADMIN approves; kick-off; calendar seeded)
  → ACTIVE (monthly cycle: plan → deliver → hour bank → SLA events → report → invoice → service-credit calc)
  → RENEWAL_DUE (T-60) → RENEWED | NOTICE_GIVEN → WIND_DOWN (hand-over pack; grants revoked at end) → ENDED
ACTIVE → SUSPENDED (OH8 dunning RESTRICTED; statutory items ≤ 30 days continue or are handed over) → ACTIVE
ACTIVE → AMENDMENT_PENDING (scope/SLA change; eSign) → ACTIVE
```

### 5.3 Professional onboarding — see FR-P16-24. Service product lifecycle: `DRAFT → LINTED → IN_REVIEW (OPS_QA_REVIEWER + PLT_LEGAL_REVIEWER for reserved classes) → LIVE → PAUSED → RETIRED`.

### 5.4 Dispute

```
RAISED (category) → SUPPLIER_RESPONSE (≤ 5 BD) → RESOLVED_BY_AGREEMENT | ESCALATED
ESCALATED → LAWDOCS_REVIEW (M1 → OH6 client_complaint; M2/M3 → facilitation ≤ 10 BD)
  → OUTCOME (RE_WORK | PARTIAL_REFUND | FULL_REFUND | NO_ACTION) → CLOSED (external remedies stated)
Grievance clock: acknowledge ≤ 48 h; resolve ≤ 1 month. Route holds stay until OUTCOME.
```

### 5.5 Route payout (M2)

```
ORDER_PAID → TRANSFER_CREATED (on_hold; idempotency key) → RELEASE_REQUESTED (DeliverableAccepted | deemed | consult window closed | dispute outcome)
  → RELEASED → SETTLED (Razorpay settlement report matched) | REVERSED (refund; credit note for LawDocs fee)
Daily reconciliation: unmatched > 24 h → OH8 billing-operations task; never a manual payout from a LawDocs account.
```

### 5.6 Academy sync

```
FETCH (daily 03:00 IST + webhook if supported) → VALIDATE (schema, price, URL allow-list) → DIFF → PUBLISH (cache, sitemap ping)
Failure: keep last good catalogue ≤ 7 days → then hide prices/batches and deep-link only (FR-P16-75).
```

---

## 6. Screens and UX

| ID | App | Screen | Key components | Empty / error states | Mobile | Accessibility |
|---|---|---|---|---|---|---|
| SCR-P16-01 | public | Marketplace home | Search bar, 18 category tiles, segment presets, "Buy without a plan" explainer, Academy strip, how-it-works, grievance link | Search no-results: suggest categories + "Ask Vidhi" | Single column; sticky search | Landmarks; tile headings H2; no carousel autoplay |
| SCR-P16-02 | public | Category page | Filters, sort (no rating sort), ranking-parameters link, service cards (price basis, timeline, "what you get") | Filter returns nothing: reset chip | Filters in bottom sheet | Filter changes announced via live region |
| SCR-P16-03 | public | Service page | Landed price card, packages, scope/exclusions, deliverables, inputs, FAQs, seller panel, CTA | Service PAUSED: "Temporarily unavailable" + alternatives | Price card pinned above CTA | Price card read as a table with total last |
| SCR-P16-04 | public | Compare | ≤ 3 columns, differences toggle | <2 items: prompt | Swipe between columns | `th scope` row headers |
| SCR-P16-05 | public | Trainings | Course cards from feed, filters by audience, "Enrol on FinLegal Academy" | Stale feed: prices hidden notice | Cards stack | External-link announcement |
| SCR-P16-06 | public | Startup bundles | Bundle cards with line-by-line totals | — | — | Bundle lines as list |
| SCR-P16-07 | public | Ranking parameters & how it works | Ordered list of parameters, models M1–M3 explained, fees explained | — | — | Plain-language level B1 |
| SCR-P16-08 | public | Advocates directory (Rule 36) | Only when flag ON | Flag OFF → 404 | — | — |
| SCR-P16-09 | public/web | Quote request | DPDP notice, purpose consents (unticked marketing), description, files | Upload virus-detected → rejected with reason | Camera upload | Error summary at top |
| SCR-P16-10 | web/mobile | Checkout review | Line items by supplier, GST, pass-through, total, terms, refund rule, eSign/click-wrap | Payment failure: reason class + retry/bank transfer | Bottom sheet summary | Total announced before "Pay" |
| SCR-P16-11 | web/mobile | My services | Engagements by state, retainers, actions due | None yet: explainer + popular categories (no popularity claim unless evidenced) | Tabs | — |
| SCR-P16-12 | web/mobile | Engagement room (buyer) | Milestones, inputs checklist, thread, deliverables (accept/revise), change requests, invoices, activity log | Inputs missing banner | Upload from camera/Files; offline read of released deliverables (NN-44) | Status chips have text, not colour only |
| SCR-P16-13 | web | Retainer dashboard | Hour bank gauge, SLA attainment table, upcoming deliverables, monthly reports, renewal | First month: "Kick-off scheduled" | Summary cards | Gauge has numeric text |
| SCR-P16-14 | web/mobile | Dispute & grievance | Category, description, evidence, timeline | — | — | — |
| SCR-P16-15 | web | Company purchase settings | Who can buy, approval threshold, contextual offers toggle | — | — | — |
| SCR-P16-20 | delivery | Service product studio | Editor, lint panel, packages, price card preview, review workflow, version diff | Lint errors block submit | — | — |
| SCR-P16-21 | delivery | Offer / retainer builder | Basket, hour bank, SLA schedule editor, split-supply lines, DoA check, engagement-letter preview | DoA exceeded → OH8 approval | — | — |
| SCR-P16-22 | delivery | Engagement pipeline | Kanban by state, filters, SLA risk flags | — | — | Keyboard shortcuts documented |
| SCR-P16-23 | delivery | Practitioner queue & workspace | Assignments (masked), active work, time entries, release requests, payouts | No assignments | Responsive | — |
| SCR-P16-24 | delivery | Professional onboarding | Evidence checklist, verification results (OH9), agreement eSign, Route linking status | RETURNED reasons | — | — |
| SCR-P16-25 | delivery | QA review & sampling | Release queue, sample list, findings | — | — | — |
| SCR-P16-30 | console | Marketplace administration | Category tree, guard-rail bands, profession switches (maker-checker with counsel ref), kill switches, moderation queue, grievance queue | Switch change without counsel ref → `LD-MKP-015` | — | — |
| SCR-P16-31 | console | Academy feed monitor | Last run, diff, failures, cache age | — | — | — |
| SCR-P16-32 | console | Payout reconciliation | Route transfers vs settlements, breaks | — | — | — |

UX rules: three-line service cards; every jargon term has an "i" key (`hlp.mkp.platform_fee`, `hlp.mkp.reverse_charge`, `hlp.mkp.pure_agent`, `hlp.mkp.route_hold`, `hlp.mkp.hour_bank`, `hlp.mkp.service_credit`, `hlp.mkp.deemed_acceptance`, `hlp.mkp.rule36`, `hlp.mkp.reserved_service`, `hlp.mkp.ranking_parameters`, `hlp.aca.certificate_import`); restricted-profession pages never show buy buttons on a person; one "Services" menu whether or not the user has a plan; languages per D-07 with legal terms glossed.

---

## 7. Backend design

### 7.1 Modules

`mkp` (owner), `aca` (Academy feed and certificates), `bil` (price cards, quotes, checkout via `BILLING_PORT`, P17), `dms` (deliverables, engagement folders), `clm`/`sgn` (engagement letters, SLA eSign — P07/P08), `wf` (tasks, SLA clocks, maker-checker), `msg` (threads), `kyc` (P01), `sdc` (retainer activation, P18), `ai`/`agt` (agents), `int` (OH8/OH9/LDC/Academy), `xpt` (export map), `core` (audit, IDs).

### 7.2 Tables (all tenant-bearing tables carry `tenant_id` + `legal_entity_id` with RLS, NN-01)

| Table | Key columns | Indexes | RLS | Retention class |
|---|---|---|---|---|
| `mkp.categories` | id, parent_id, code, name_i18n, sort, visible | code | public read | Platform config |
| `mkp.services` | `svc_` id, version, code, category_id, service_class, delivering_party_type, seller_entity_ref, scope, exclusions, deliverables jsonb, inputs jsonb, timeline_bd, revisions, price_model, oh8_sku_ref, stream_code, sla_template_id, languages[], states[], status, live_from, reviewed_by, claims_refs[] | (code, version), status | public read LIVE | Platform config, versions kept |
| `mkp.service_packages` | service_id, version, tier_code, inclusions, price_ref | — | public read | Platform config |
| `mkp.offers` | `ofr_` id, tenant_id, engagement_id, version, lines jsonb (supplier, stream, amount_ref), validity, assumptions, letter_doc_id, hash, status | tenant_id, status | tenant | 8 yrs after close [REC] |
| `mkp.engagements` | `eng_` id, business_ref `LD-ENG-…`, tenant_id, legal_entity_id, buyer_user_id, service_id+version, model, supplier_pro_id, state, scope_snapshot, price_snapshot, oh8_quote_ref, oh8_order_ref, letter_doc_id, signature_refs, conflict_check_id, independence jsonb, assignment_basis | tenant_id+state, business_ref unique | tenant; practitioner via engagement grant | 8 yrs after close [REC]; legal hold aware |
| `mkp.milestones` | engagement_id, seq, title, due_at, state, deliverable_doc_ids[], accepted_by, accepted_at, deemed | engagement_id | tenant | as engagement |
| `mkp.change_requests` | `ecr_` id, engagement_id, delta_scope, delta_price_ref, delta_timeline, state, approved_by | engagement_id | tenant | as engagement |
| `mkp.retainers` | `rtn_` id, engagement_id, package_code, basket jsonb, hour_bank jsonb, sla_schedule_id, cycle, term_end, renewal_at, state, sdc_client_section_ref | tenant_id, state | tenant | as engagement |
| `mkp.sla_schedules` / `mkp.sla_events` | `sla_` id, version, metrics jsonb, credit_rule, doc_id; event: metric, due_at, met_at, breached, credit_ref | retainer_id | tenant | as engagement |
| `mkp.time_entries` | retainer_id/engagement_id, staff_ref, role_level, hours (NUMERIC), category, task_ref, created_at | retainer_id, period | tenant + delivery | as engagement |
| `mkp.professionals` | `pro_` id, kind (PERSON, FIRM), source, profession_codes[], oh9_ref, kyc_ref, practice_areas[], languages[], states[], forums[], classes[], capacity jsonb, pi_cover jsonb, route_linked_account_ref, status | status, profession | platform; self-read | Engagement + 8 yrs; DPDP erasure for unused profiles |
| `mkp.profession_rules` | profession_code, switch values, counsel_opinion_ref, maker, checker, effective_from, version | (profession_code, effective_from) | platform | Permanent (audit) |
| `mkp.assignments` | engagement_id, pro_id, offered_at, response, reason, basis, seed | engagement_id | tenant + practitioner | as engagement |
| `mkp.conflict_checks` | id, engagement_id, party_hashes[], result, group_check_ref, declaration_ref, cleared_by | engagement_id | tenant + delivery | as engagement |
| `mkp.reviews` | `rev_` id, engagement_id, target (LAWDOCS_SERVICE only), rating, text, consent_ref, status, moderator, reply | service_id, status | public read PUBLISHED | 3 yrs after display end |
| `mkp.private_feedback` | engagement_id, pro_id, scores jsonb | pro_id | delivery only | 3 yrs |
| `mkp.disputes` | id, engagement_id, category, state, supplier_response, outcome, credit_note_ref, oh6_ref | state | tenant | 8 yrs |
| `mkp.payout_instructions` | engagement_id, milestone_seq, route_transfer_ref, amount_ref, tds_ref, state, idempotency_key, reconciled_at | state, reconciled_at | platform + practitioner own | 8 yrs (tax) |
| `aca.courses` / `aca.feed_runs` / `aca.certificates` | course fields (Appendix M §M.11), feed hash; run status; certificate: user/tenant, course, cert_no, file_id, consent_ref | course_id; run_at | public / tenant | Courses: platform; certificates: per vault |

Money fields are references to OH8 amounts (NUMERIC + decimal.js where displayed; LawDocs never computes tax — P17 FR-P17-03).

### 7.3 APIs (OpenAPI 3.1 from Zod; idempotency on all POSTs)

| Method | Path | Scope | Idempotency |
|---|---|---|---|
| GET | `/v1/public/marketplace/categories`, `/services`, `/services/{slug}`, `/trainings`, `/ranking` | public | — |
| GET | `/v1/public/marketplace/directory/advocates` (only if flag ON; `RULE36_V1`; seed logged) | public | — |
| POST | `/v1/marketplace/requests` | `mkp.request` (anon with consent token) | Idempotency-Key |
| POST | `/v1/marketplace/engagements/{id}/offers` · `/offers/{ofr}/accept` · `/decline` | `mkp.offer.write` / `mkp.buy` | Idempotency-Key |
| POST | `/v1/marketplace/engagements/{id}/contract` (starts P08 ceremony or click-wrap) | `mkp.buy` | Idempotency-Key |
| POST | `/v1/marketplace/engagements/{id}/milestones/{seq}/release` · `/accept` · `/revise` | supplier / buyer | Idempotency-Key |
| POST | `/v1/marketplace/engagements/{id}/change-requests` · `/{ecr}/approve` | both | Idempotency-Key |
| POST | `/v1/marketplace/engagements/{id}/disputes` | buyer | Idempotency-Key |
| GET/POST | `/v1/marketplace/retainers/{id}` · `/time-entries` · `/reports` · `/renew` · `/notice` | tenant / delivery | Idempotency-Key |
| GET/POST | `/v1/practitioner/assignments` · `/{id}/accept` · `/decline` · `/payouts` | `PRO_*` | Idempotency-Key |
| POST | `/v1/console/marketplace/profession-rules` (maker) · `/{id}/approve` (checker) | `PLT_SUPER_ADMIN` / `PLT_LEGAL_REVIEWER` | Idempotency-Key |
| POST | `/v1/marketplace/reviews` · `/v1/console/marketplace/reviews/{id}/moderate` | buyer / moderator | Idempotency-Key |
| POST | `/m/v1/services/*` (mobile BFF projections of the above) | as above | as above |

### 7.4 Domain events (internal and tenant webhooks; CloudEvents 1.0, outbox)

`in.lawdocs.mkp.ServiceRequested.v1`, `OfferIssued.v1`, `OfferAccepted.v1`, `EngagementContracted.v1`, `MilestoneDelivered.v1`, `DeliverableAccepted.v1`, `ChangeRequestApproved.v1`, `ChangeRequestRejected.v1`, `EngagementClosed.v1`, `EngagementCancelled.v1`, `RetainerActivated.v1`, `RetainerHourBankThresholdReached.v1`, `RetainerSLABreached.v1`, `ServiceCreditRequested.v1` (→ P17/OH8 credit note), `RetainerRenewed.v1`, `RetainerEnded.v1` (→ P18 revoke grants), `DisputeRaised.v1`, `DisputeResolved.v1`, `ProfessionalActivated.v1`, `ProfessionalSuspended.v1`, `ProfessionRuleChanged.v1`, `ServicePublished.v1`, `ConflictCheckFailed.v1`, `PayoutReleaseRequested.v1`, `PayoutReconciled.v1`, `ReviewPublished.v1`; `in.lawdocs.aca.CatalogueSynced.v1`, `in.lawdocs.aca.CertificateImported.v1`. Consumed via `int`: `ProfessionalEmpanelled`, `ProfessionalSuspended` (OH9, `in.infrabyx.directory.*`), `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed` (OH8, `in.infrabyx.billing.*`). Proposed cross-product (Appendix Y; inert until merged, never improvised in code before approval): `in.infrabyx.ops.ServiceOrderRouted.v1` (LawDocs → LDC; §Y.7.9), consumption of `in.infrabyx.ops.ServiceOrderStatusChanged.v1` (LDC → LawDocs), `in.infrabyx.billing.MarketplaceTransferInstructed.v1` (LawDocs → OH8: RELEASE / REVERSE / EXTEND_HOLD of the on-hold Route transfers created from the order's `route_transfers[]`, emitted from `PayoutReleaseRequested` and refund or dispute outcomes; §Y.7.7), consumption of `in.infrabyx.billing.MarketplacePayoutSettled.v1` (→ `PayoutReconciled`), and `in.infrabyx.billing.ServiceCreditIssued.v1` from approved `ServiceCreditRequested` (§Y.7.10). Mapping table: Appendix I §I.8.

### 7.5 Jobs and workflows (Temporal unless noted)

`EngagementWorkflow` (timeline and SLA clocks, reminders, deemed acceptance, escalations), `RetainerCycleWorkflow` (monthly plan → report → invoice → service-credit computation), `ConsultSlotWorkflow` (no-show detection, auto-refund, 48-hour follow-up window), `AssignmentWorkflow` (offer → accept window → fallback), `PayoutReleaseWorkflow` (Route release with idempotency; reconciliation), `ProfessionalCredentialWatch` (BullMQ daily; expiry alerts), `ServiceReReviewSampler` (monthly 10%), `AcademySyncJob` (BullMQ daily), `RankingDisclosureRenderer` (on catalogue publish), `IntakeQuarantinePurge` (daily; 30-day purge).

---

## 8. Integrations

| Port | Adapter(s) | Use | Failure behaviour / fallback |
|---|---|---|---|
| `BILLING_PORT` | OH8 (default), LOCAL (interim, P17 §4L), MOCK | SKUs, quotes, orders, invoices, credit notes, Route instructions | OH8 down: browsing continues from last signed catalogue; checkout shows "We'll confirm shortly" and queues quote; no order without OH8 confirmation |
| `DIRECTORY_PORT` | OH9 | Credential verification, suspension events, Rule 36 fields | OH9 down: no new activations; existing ACTIVE professionals continue; suspension events replayed on recovery |
| `ESIGN_PORT` | P08 adapters (Leegality / Digio / Melento / Surepass-type; D-12) | Engagement letters, SLA schedules, panel agreements | ESP down: second ESP route; else OTP click-wrap below threshold; above threshold, wait |
| `PAYOUT_ROUTE` | Razorpay Route via OH8 | Linked accounts, on-hold transfers, releases, reversals | Transfer failure: retry with same idempotency key; break → OH8 task; never manual payout |
| `ACADEMY_PORT` | Graphy API [VERIFY] / signed JSON-CSV feed | Course catalogue, corporate enrolments, completion export | Stale-feed fallback (FR-P16-75) |
| `WORKSPACE_PORT` | M365 (Teams), Google (Meet) | Scoping calls, consult video | Built-in WebRTC call [REC] or phone call-back |
| `CONFLICT_PORT` | OH `POST /v1/conflicts/check` | Group institutional conflicts | Down: hold engagement in SCOPING; never skip |
| `CLAIMS_GATE_PORT` | OH14 | Service copy, CSAT statements, bundle claims | Down: publishing blocked |
| `CRM_PORT` | OH3 via `int` | Consented quote-request leads | Queue; never block the visitor |
| `LDC_PORT` | `int` → LDC (Appendix Y event) | Routing group-listing orders | Queue with consent artefact; buyer sees "Your order is with LawDocsComply" |

---

## 9. Settings and configuration (registered in Appendix R before code reads them — NN-29)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `mkp.public.enabled` | PLATFORM | bool | true | `PLT_SUPER_ADMIN` | Y |
| `mkp.model.m2.enabled` | PLATFORM | bool | false | Owner via `PLT_SUPER_ADMIN` + counsel ref | Y |
| `mkp.model.m3.enabled` | PLATFORM | bool | false | as above | Y |
| `mkp.providers.third_party.enabled` | PLATFORM | bool | false | as above | Y |
| `mkp.profession.<code>.listing_mode` | PLATFORM | enum | per FR-P16-18 | `PLT_SUPER_ADMIN` + `PLT_LEGAL_REVIEWER` + counsel ref | Y |
| `mkp.profession.<code>.commission_pct_allowed` / `.listing_fee_allowed` / `.paid_ranking_allowed` / `.referral_reward_allowed` | PLATFORM | bool | false (advocate: immutable false) | as above | Y |
| `mkp.profession.<code>.ratings_display_allowed` | PLATFORM | bool | false for regulated (advocate: immutable false) | as above | Y |
| `mkp.profession.<code>.buyer_platform_fee_mode` | PLATFORM | enum | FLAT | as above | Y |
| `mkp.platform_fee.flat_inr` | PLATFORM | money | ₹99 (band ₹49–₹199) [OWNER TO SET] | Pricing committee via OH8 | Y |
| `mkp.directory.advocates.enabled` | PLATFORM | bool | false | Owner + counsel ref | Y |
| `mkp.sponsored.enabled` | PLATFORM | bool | false (locked) | — | — |
| `mkp.contract.clickwrap_max_value` | PLATFORM | money | ₹25,000 [OWNER TO SET] | `PLT_SUPER_ADMIN` + legal | Y |
| `mkp.acceptance.deemed_days` | PLATFORM | int (BD) | 7 (0 = off; max 15) | `PLT_SUPER_ADMIN` + legal | Y |
| `mkp.offer.validity_days` | PLATFORM | int | 15 | `OPS_DELIVERY_LEAD` | N |
| `mkp.assignment.accept_window_hours` | PLATFORM | int | 4 (business hours) | `OPS_DELIVERY_LEAD` | N |
| `mkp.consult.no_show_minutes` | PLATFORM | int | 10 | `OPS_DELIVERY_LEAD` | N |
| `mkp.consult.followup_hours` | PLATFORM | int | 48 | `OPS_DELIVERY_LEAD` | N |
| `mkp.qa.review_required` | PLATFORM | bool | true | `OPS_DELIVERY_LEAD` | Y |
| `mkp.retainer.hour_rollover_months` | PLATFORM | int | 1 (0–3) | `OPS_DELIVERY_LEAD` | Y |
| `mkp.retainer.sla_credit_pct` / `.sla_credit_cap_pct` | PLATFORM | decimal | 5 / 20 [OWNER TO SET] | Owner | Y |
| `mkp.retainer.show_staff_names` | TENANT | bool | false | `ORG_ADMIN` | N |
| `mkp.practitioner.post_close_access_days` | PLATFORM | int | 7 | `PLT_SUPER_ADMIN` | Y |
| `mkp.disputes.supplier_response_bd` | PLATFORM | int | 5 | `PLT_SUPER_ADMIN` | N |
| `mkp.disputes.show_adr_options` | PLATFORM | bool | false | Owner | Y |
| `mkp.grievance.ack_hours` / `.resolve_days` | PLATFORM | int | 48 / 30 (floors) | — | — |
| `mkp.intake.retention_days` | PLATFORM | int | 30 | `PLT_DPO` | Y |
| `mkp.price_guardrail.<category>` | PLATFORM | money range | per Appendix M | `PLT_SUPER_ADMIN` | Y |
| `mkp.tenant.who_can_buy` | TENANT | role set | `ORG_OWNER`, `ORG_ADMIN`, `ORG_CLO` | `ORG_ADMIN` | N |
| `mkp.tenant.purchase_approval_threshold` | TENANT | money | off | `ORG_ADMIN` | N |
| `mkp.tenant.contextual_offers` | TENANT / USER | bool | true | `ORG_ADMIN` / user | N |
| `mkp.user.service_suggestions` | USER | bool | true | user | N |
| `mkp.category.adr.equator_link` | PLATFORM | bool | false | Owner + Equator oversight | Y |
| `aca.display_name` | BRAND | string | "FinLegal Academy" [OWNER TO SET] | Owner | Y |
| `aca.feed.mode` | PLATFORM | enum | SIGNED_FEED (API if verified) | `PLT_SUPER_ADMIN` | Y |
| `aca.cache_max_age_days` | PLATFORM | int | 7 (1–14) | `PLT_SUPER_ADMIN` | N |
| `aca.certificate_import.enabled` | TENANT | bool | true (consent per learner) | `ORG_ADMIN` | N |

Kill switches (NN-39): per stream (RS-LD-19…33 via P17 registry), per profession, per model, per category, Academy feed, consult slots.

---

## 10. Security, privacy and audit

- **Threats and controls.** Fee-sharing or ranking introduced by configuration drift → immutable advocate commercial fields, render allow-lists, CI tests. Third-party money custody → Route only, no wallet, daily reconciliation (NN-22). IDOR across engagements → engagement-scoped grants and RLS tests per endpoint (NN-01). Professional seeing buyer data before acceptance → masked brief. Off-platform solicitation → masked contacts, leakage nudges (warning only, no surveillance — NN-33). Fake reviews → verified-purchase only, moderation, no incentives (NN-49). Claims → OH14 claims gate on every service copy (NN-20).
- **Data roles (DPDP).** M1: LawDocs is fiduciary for account and engagement records and processor for buyer documents it handles on the buyer's instructions where the buyer is a business. M2/M3: the professional is an independent fiduciary for professional records; LawDocs hosts the engagement room as processor for that content and is fiduciary for platform data. Notices state this; DPA templates in Appendix M §M.12. Purpose-wise consent artefacts (`cns_`) for quote intake, LDC routing and certificate import (NN-26).
- **Data classes.** Engagement content and deliverables: CONFIDENTIAL (Bedrock India only for AI, NN-15); party names in conflict checks stored as salted hashes; payout and KYC: RESTRICTED; reviews: PUBLIC after moderation.
- **No marketing misuse.** Engagement content never feeds CRM, ad audiences or other group products; only consented contact data becomes an OH3 lead (NN-19, R4-MKT-12); sensitive intents (criminal, matrimonial, debt distress) are excluded from retargeting (R4-MKT-10).
- **Audit ledger events** (NN-02, NN-45): service publish/version, offer, signature, payment confirmation, assignment and basis, conflict result and clearance, delivery, acceptance, change request, refund, dispute action, review moderation, profession-rule change with counsel ref, payout release, grant creation/revocation.
- **Retention.** Engagement records 8 years after closure [REC; VERIFY with tax/limitation counsel]; intake quarantine 30 days; legal hold respected (P04).

---

## 11. AI touchpoints and guardrails

| Agent / feature | Autonomy ceiling | Human confirmation point | Guardrails | Evaluation |
|---|---|---|---|---|
| `AGT_SERVICE_FINDER` (public + in-app) | L1 (suggest) | Buyer chooses; human hand-off on request | Recommends categories/services only; never a named advocate/CA/CS; discloses AI and first-party nature (R4-MKT-07); no legal advice | Weekly sample of 100 sessions: wrong-category rate < 5%, zero person recommendations |
| `AGT_SCOPE_DRAFTER` (scope summaries, offers, engagement-letter fill, monthly reports) | L2 (draft) | Professional/RM approves before any send (NN-13) | Approved clause library only; never invents fees or legal terms; labels "AI draft" internally | Edit-distance and rejection rate tracked; legal-reviewer spot checks |
| Deliverable QA assistant | L1 | Reviewer decides | Checks citations against the rules register; flags unresolved citations as "unverified" (NN-14) | Precision of citation flags ≥ 95% on gold set |
| Intake classifier (quote requests) | L1 | Delivery lead triage | Routes Consumer Help requests behind the ethical wall (NN-23) | Mis-route rate < 2% |

AI credits used by these agents are charged to LawDocs's internal budget, never the buyer (§4H). Agents are makers only (NN-43); kill switch per agent (NN-39).

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p16/*.feature`)

```gherkin
@P16-AT-01
Scenario: Browse and read a landed price card without login
  Given an anonymous visitor on /marketplace
  When they open "Trademark search and filing — 1 class"
  Then the price card shows service fee, government fee estimate with basis and date, GST and "Total payable now"
  And no login or subscription prompt appears

@P16-AT-02 @NN-50
Scenario: Price card lint blocks drip pricing
  Given a service product draft without a government-fee line where the service needs one
  When the maker submits it for review
  Then submission is refused with LD-MKP-004 "Price card incomplete"

@P16-AT-03 @R-040
Scenario: Buy a fixed-price service with a Free account
  Given a user with a Free account and no plan
  When they buy "Professional review of a self-drafted agreement (≤ 5 pages)" and pay on Razorpay hosted checkout
  Then OH8 issues a GST tax invoice and e-mails it to the user
  And an engagement LD-ENG-… is created in INPUTS_PENDING
  And no subscription is created

@P16-AT-04 @NN-21
Scenario: Advocate commercial fields cannot be enabled
  When a super admin attempts to set mkp.profession.ADVOCATE.commission_pct_allowed to true
  Then the request is rejected with LD-MKP-016 "Field not configurable"
  And the audit ledger records the attempt

@P16-AT-05 @NN-21
Scenario: Advocate responses never contain ratings or fees per person
  Given an engagement assigned to a panel advocate
  When the buyer API returns the assignment confirmation
  Then the payload matches PRO_SERVICE_V1 and contains no rating, photo, per-person fee or badge field

@P16-AT-06 @NN-21 @NN-18
Scenario: CA listing switch needs counsel opinion and a different checker
  When PLT_SUPER_ADMIN A proposes mkp.profession.CA.listing_mode = ASSIGNED_ONLY without counsel_opinion_ref
  Then the proposal is rejected with LD-MKP-015
  When A proposes it with a counsel_opinion_ref and A tries to approve it
  Then approval is refused with LD-MKP-017 "Maker cannot be checker"

@P16-AT-07 @NN-41
Scenario: Reserved service cannot be supplied by LawDocs
  When a maker sets delivering party LAWDOCS_TEAM on a RESERVED_ADVOCACY service
  Then lint fails with LD-MKP-010

@P16-AT-08 @NN-22
Scenario: Professional fee goes only through Route on hold
  Given an M2 engagement priced at professional fee ₹1,999 and platform fee ₹99
  When the buyer pays
  Then a Route transfer of ₹1,999 is created on hold to the professional's linked account
  And LawDocs invoices only the ₹99 platform fee plus GST
  And no LawDocs ledger account holds the ₹1,999

@P16-AT-09 @NN-46
Scenario: Duplicate release is idempotent
  Given a milestone accepted and a release instruction sent
  When the release is retried after a timeout
  Then Razorpay receives the same idempotency key and exactly one transfer is released

@P16-AT-10
Scenario: Consult no-show auto-refund
  Given a 30-minute consult slot starting at 11:00 IST
  When no professional joins by 11:10
  Then the buyer receives a full refund including the platform fee without filing a request
  And the slot is offered for rebooking

@P16-AT-11
Scenario: Conflict hit blocks the offer
  Given the counterparty "ABC Finance Ltd" matches an active engagement of the assigned professional
  When the delivery lead tries to send the offer
  Then it is blocked with LD-MKP-020 until cleared with reason or re-assigned

@P16-AT-12 @NN-23
Scenario: Consumer Help request routes behind the ethical wall
  Given a quote request classified as an insurance-claim grievance
  Then it is visible only to OPS_CONSUMER_CASE_MANAGER users of the Consumer Help brand
  And the group conflict check runs against group insurer clients before acceptance

@P16-AT-13 @CH-31
Scenario: Success fee is unavailable where an advocate acts
  When a maker attaches stream RS-LD-40 to a RESERVED_ADVOCACY service
  Then lint fails with LD-MKP-012

@P16-AT-14 @NN-17 @R-064
Scenario: Retainer activation proposes RM-as-maker grants
  Given a Startup Legal Officer retainer is CONTRACTED
  Then a delivery grant is proposed with the RM as ORG_DELEGATED_MAKER in the Legal department
  And the RM gets no access until ORG_ADMIN approves

@P16-AT-15
Scenario: SLA schedule is eSigned before activation
  Given a retainer offer with an SLA schedule
  When the client accepts without signing the SLA schedule
  Then the retainer stays in OFFERED and activation is refused with LD-MKP-033

@P16-AT-16
Scenario: Hour bank hard stop
  Given a retainer with 10 hours and no pre-approved overage
  When time entries reach 10 hours
  Then new time entries are refused with LD-MKP-035 and the client is asked to approve a top-up

@P16-AT-17
Scenario: SLA breach creates a service credit request
  Given a 3 business-day turnaround SLA for contract review
  When delivery happens on business day 5
  Then RetainerSLABreached is emitted and ServiceCreditRequested for 5% of the monthly LawDocs fee is sent to OH8

@P16-AT-18 @NN-49 @R-088
Scenario: Review is about the LawDocs service and shows no photo
  Given a closed M2 engagement delivered by a panel advocate
  When the buyer submits a review
  Then the review target is LAWDOCS_SERVICE and it is displayed without a photo after moderation
  And any text naming the advocate is moved to private feedback

@P16-AT-19 @NN-11
Scenario: Engagement records appear in the export
  Given a closed engagement in a Company workspace for FY 2026-27
  When the tenant runs a full export
  Then "09 Services and Engagements/2026-27/<title> (LD-ENG-…)/" contains the letter, deliverables, correspondence and invoice references

@P16-AT-20 @D-16
Scenario: Stale Academy feed hides prices
  Given the Academy feed has failed for 8 days
  Then course prices and batch dates are hidden and each course deep-links to FinLegal Academy

@P16-AT-21 @NN-24
Scenario: LawDocsComply listing routes only with consent
  Given a buyer orders "ICAAP document preparation" sold by the LDC entity
  When they decline to share their LawDocs profile with LawDocsComply
  Then the order is routed with order reference and contact only and no tenant data is sent

@P16-AT-22 @NN-35
Scenario: No sponsored placement exists
  When any category page renders
  Then no result carries a sponsored flag and the ranking page lists no paid parameter

@P16-AT-23 @NN-13
Scenario: Agent cannot send an offer
  Given AGT_SCOPE_DRAFTER drafted an offer
  When the agent calls the send endpoint
  Then the call is refused and a human approval task is created

@P16-AT-24 @NN-20
Scenario: Prohibited claim words fail lint
  When a service description contains "best lawyers in Delhi"
  Then lint fails with LD-MKP-005 and names the phrase

@P16-AT-25 @NN-01
Scenario: Engagement of another tenant is not reachable
  Given engagement E belongs to tenant A
  When a user of tenant B requests GET /v1/marketplace/engagements/E
  Then the response is 404 and the attempt is audit-ledgered

@P16-AT-26 @NN-19
Scenario: Quote-request lead carries contact data only
  Given an anonymous visitor submits a quote request with two uploaded files and marketing consent
  Then the OH3 lead contains name, contact, segment and consent references
  And it contains no file, file name or description text

@P16-AT-27 @NN-39
Scenario: Profession kill switch stops new assignments
  When PLT_SUPER_ADMIN and PLT_LEGAL_REVIEWER switch off profession TRADEMARK_AGENT
  Then within 5 minutes no new assignment is offered to trademark agents
  And live engagements continue and are flagged to OPS_DELIVERY_LEAD

@P16-AT-28 @NN-14
Scenario: AI-drafted deliverable for an individual stays labelled until reviewed
  Given a deliverable drafted by AGT_SCOPE_DRAFTER for an IND_OWNER buyer
  When it is released without a qualified reviewer's approval
  Then the document carries "AI draft — not reviewed by a professional" and the one-click paid review offer

@P16-AT-29 @NN-45
Scenario: State change and audit entry are atomic
  Given the audit ledger write fails during a milestone acceptance
  Then the acceptance is rolled back and no Route release is requested
```

Error codes introduced: `LD-MKP-001` service not found · `-002` service not LIVE · `-003` category invalid · `-004` price card incomplete · `-005` prohibited claim phrase · `-006` exclusions missing · `-010` reserved class supplied by LawDocs · `-011` profession mode forbids model · `-012` stream not allowed for service class · `-015` counsel opinion reference required · `-016` field not configurable · `-017` maker cannot be checker · `-020` conflict check failed · `-021` independence check failed · `-022` group conflict service unavailable · `-025` offer expired · `-026` DoA exceeded (sent to OH8 approval) · `-030` inputs incomplete · `-031` work outside approved scope · `-033` SLA schedule not executed · `-035` hour bank exhausted · `-040` payout release blocked by dispute · `-041` Route linked account not active · `-045` review target invalid · `-050` grievance clock breached (alert). `LD-ACA-001` feed signature invalid · `-002` feed stale · `-003` certificate import without consent. Each has a user message and help key `hlp.mkp.err_<nnn>`.

NN test files: `tests/nn/NN-21_advocate_commercial_fields_immutable.spec.ts`, `NN-21_profession_render_allowlist.spec.ts`, `NN-21_plan_status_not_in_ranking_features.spec.ts`, `NN-22_no_third_party_funds_in_lawdocs_ledger.spec.ts`, `NN-41_reserved_class_supplier.spec.ts`, `NN-49_review_target_lawdocs_only.spec.ts`, `NN-50_price_card_complete.spec.ts`, `NN-23_consumer_help_wall.spec.ts`.

---

## 13. Exit gate, deliverables and open items

**Checklist**

- [ ] Storefront, service studio, offers, engagements, retainers with SLA engine, practitioner workspace, disputes, reviews, Academy feed and group listings live behind the flags in §9.
- [ ] ≥ 80 LIVE seeded services across 18 categories (Appendix M §M.2) with complete price cards; 4 retainer packages configured (Appendix L §L.7).
- [ ] Engagement-letter, SOW, SLA schedule, panel agreement, marketplace buyer terms and professional terms approved by counsel (Appendix M §M.9).
- [ ] Tax memo signed for SACs, RCM/exempt statements, ECO TCS/TDS treatment and pure-agent lines (OI-P16-04).
- [ ] All §12 scenarios and NN tests green; accessibility audit (axe + manual) passed on SCR-P16-01…14 (NN-28).
- [ ] Settings registered in Appendix R; help keys registered in `hlp`; errors registered with messages.
- [ ] Export-map entries registered (below); Appendix X and Y requests filed.

**Demo script.** (1) Anonymous visitor finds "Rent agreement — professional review", reads the landed card, buys with a new Free account on mobile in ≤ 7 taps including OTP sign-up (J-28); invoice e-mail arrives. (2) In-house professional delivers; QA releases; deliverable appears in the buyer's vault; buyer accepts. (3) Startup buys a Startup Legal Officer retainer; SLA schedule eSigned; RM grant approved by the founder; hour bank and SLA dashboard move during the demo. (4) Console shows advocate commercial fields as non-editable; a CA listing change is rejected without counsel reference. (5) Academy course list renders from the feed; stale-feed fallback demonstrated.

**Export-map entries (`xpt.export_map`, `LD-EXPORT-1.0`)**

| Record type | Company path | Individual path |
|---|---|---|
| `mkp.engagement` | `09 Services and Engagements/<FY>/<Service title> (LD-ENG-…)/{01 Engagement Letter and SOW, 02 Inputs, 03 Deliverables, 04 Correspondence, 05 Invoices and Receipts, 06 Change Requests}` | `10 Receipts and Invoices/<Year>/Services/<Service title> (LD-ENG-…)/`; deliverables also linked from their category folder |
| `mkp.retainer` | `09 Services and Engagements/<FY>/Retainers/<Package> (LD-ENG-…)/{01 Agreement and SLA Schedule, 02 Monthly Reports, 03 Deliverables, 04 Hour Bank and SLA Statements, 05 Invoices}` | n/a |
| `mkp.review` (own) | `99 System Data (CSV and JSON)/marketplace/reviews.csv` | `99 System Data/marketplace/reviews.csv` |
| `mkp.dispute` | `09 Services and Engagements/<FY>/<…>/07 Disputes/` | `10 Receipts and Invoices/<Year>/Services/<…>/Disputes/` |
| `aca.certificate` | `07 People and HR/Training Certificates/<Year>/` | `04 Employment/Training Certificates/` |
| `mkp.professional` (practitioner's own) | `99 System Data/practitioner/` (practitioner export) | — |

**Open items**

| ID | Item | Owner | Fallback / flag |
|---|---|---|---|
| OI-P16-01 | LawDocs Panel structure: affiliated advocates' firm vs contracted panel; invoicing (advocate bill with RCM + LawDocs platform fee) | Owner + [COUNSEL] | `mkp.model.m2.enabled` OFF; M1 non-reserved services only |
| OI-P16-02 | Counsel opinion: assigned-professional model, buyer-side flat platform fee, publishing panel SKU prices, Route collection of advocates' fees vs BCI r.36/r.37 and fee-sharing bar; status of *Sulekha.com v. P.N. Vignesh* | [COUNSEL] | M2 OFF; directory OFF |
| OI-P16-03 | Boundary of DOCUMENTATION class (bespoke drafting by LawDocs staff) vs "practice of law" (*A.K. Balaji*) | [COUNSEL] | Bespoke drafting via panel (M2) with LawDocs documentation support only |
| OI-P16-04 | Tax memo: SAC per class, ECO registration, s.52 TCS exclusion for RCM/exempt, s.393(1) Sl. 8(v) TDS, pure-agent duty lines | [TAX MEMO] | M2 OFF until signed |
| OI-P16-05 | ICAI/ICSI/ICMAI current positions on platforms; CA/CS switches | [COUNSEL] | Locked OFF |
| OI-P16-06 | Individual course checkout: Academy (Graphy) or OH8; Graphy API/SSO capability | Owner + integration lead | Deep link; signed feed |
| OI-P16-07 | Academy brand clean-up ("FinLegal Academy" absent on live site; wPractical leakage — R5 §1.3) | Owner | `aca.display_name` |
| OI-P16-08 | Razorpay Route: MCC approval for legal-services marketplace, transfer fee, on-hold limits | Finance [VERIFY] | M2 OFF |
| OI-P16-09 | E-Commerce Rules 2020 sub-rules and any 2026 amendment applicable to a services marketplace (seller info, ranking disclosure, grievance timelines) | [COUNSEL] [VERIFY] | Adopt duties as policy |
| OI-P16-10 | Trade Marks Act s.145 agent rules and TM-agent conduct for platform listing | [COUNSEL] [VERIFY] | TM filings by advocates on the panel |
| OI-P16-11 | Deemed acceptance, refund timelines, SLA credit values, click-wrap threshold | Owner | Defaults marked [OWNER TO SET] |
| OI-P16-12 | App-store rules for selling professional services in the mobile apps (person-to-person services vs digital goods) — coordinate with P22 | P22 lead [VERIFY] | Services purchasable in app via Razorpay only if confirmed; else web hand-off |

**Conflicts recorded for the master.** R4 §11.6 suggests advocates pay "a flat listing/subscription fee"; this conflicts with D-05/NN-21 and the OH8/OH9 deny lists — this phase follows D-05 (no listing fee for advocates). R3 LG-113 says clients choose advocates and LawDocs does not assign for a fee; conventions fact 11 binds the assigned-professional model — implemented with buyer choice (FR-P16-31) and counsel confirmation (OI-P16-02). Commercial-model letters differ from LDC P21 (LDC M2 = direct, M3 = Route; here M2 = Route, M3 = direct) because Route is LawDocs's primary third-party rail.

