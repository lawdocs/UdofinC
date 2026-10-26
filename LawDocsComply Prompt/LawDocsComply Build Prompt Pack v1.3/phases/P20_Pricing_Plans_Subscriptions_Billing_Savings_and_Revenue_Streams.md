# Phase P20 — Pricing, Plans, Subscriptions, Billing, Savings and Revenue Streams

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, audit ledger, Correction Entries, feature flags, outbox/inbox);
> - **P01** (identity, onboarding wizard, PAN/CIN/GSTIN fetch, trial tenant creation, step-up MFA);
> - **P02** (settings registry and Configuration Studio — every key in §9 is registered there before use, NN-28);
> - **P18** (integration gateway: signed-event inbox, JWS verification of OH catalogue and entitlements, webhook framework);
> - **P23** (public website shell, Free Compliance Health Check that seeds the configurator) — P20 ships the pricing page and configurator components that P23 mounts.
> - **External:** Infrabyx Operations Hub **OH8** (catalogue, quotes, orders, invoices, Razorpay, dunning) and **OH4** (provisioning) per Infrabyx Ecosystem Integration Specification v1.1 §6.27 and §6.29, and Appendix X of this pack.
>
> **Sequencing:** Sprint 1 freezes `BILLING_PORT`, the presentation-catalogue schema and the entitlement SDK (`packages/entitlements`) that every module from P04 onwards calls. P20 may start after P01 exits; its exit gate requires the OH8 adapter to pass contract tests against the OH8 sandbox **or** the interim `LOCAL` adapter to be approved by the owner (D-21; OI-P20-01).
>
> **Binding appendices:** N (Pricing, Plans, Add-ons, Revenue Streams and Savings Model), X (Operations Hub Addendum), U (settings catalogue), B (data model, events, errors), Q (PCI DSS SAQ A scope), P (pricing-page copy and SEO).
>
> **Requirements covered:** R-016 (handoff from health check), R-024, R-034, R-037, R-044, R-067, R-069, R-070, R-071, R-074, R-076 (billing documents download), R-033 (payment security).
>
> **Estimated effort:** 6 two-week sprints, squad of 8 (commerce backend 3, frontend/configurator 3, QA 1, finance-domain analyst 1). *(v1.1: +2 sprints for v1.1 scope (multi-currency presentation, new components, agent credits, transparency fixes) — 8 in total)*


**v1.1 changes (25 October 2026)** *(v1.1)*

- New §4P multi-currency and cross-border commerce: presentation in INR, USD, AED, SGD, EUR and GBP from OH8 price books; place-of-supply tax preview, tax-ID capture and withholding-tax documents (Appendix Y §Y.10); X-02 unchanged — OH8 sets prices, computes tax and issues invoices (FR-P20-70–FR-P20-76).
- New §4Q components for the v1.1 modules — Legal Matters & Contracts (P26), ESG/BRSR & CSR (P27), AI Governance (OV_AI), Global Entity Management and per-jurisdiction Global Packs (P25), Reports & MIS Studio Pro (P28), local-expert query bundles, data residency cells, escrow — plus practitioner-firm plans and free auditor engagement seats (G5 TM-405) (FR-P20-77–FR-P20-82).
- New §4R AI credits for the Vidhi agent workforce: agent seats, mission and control-monitoring meters, MCP calls, department and agent budgets, opt-in top-ups and pay-as-you-go (Appendix AA §AA.14) (FR-P20-83–FR-P20-88).
- New §4S transparency fixes from client feedback: paid seats only for working roles (IMP-104), full-year and renewal price shown (IMP-105), monthly and annual cycles (IMP-106), 60/30/7-day renewal reminders (IMP-107), self-serve cancellation in ≤ 3 clicks (IMP-108), quarterly value report (IMP-109) (FR-P20-89–FR-P20-95).
- New §4T unit-economics telemetry: per-tenant cost-to-serve for channels and AI (G5 TM-400) (FR-P20-96–FR-P20-97).
- Appendix N extended to match (§N.15–§N.21); new screens, settings, meters, acceptance scenarios and open items.

---

## 1. Objective and business outcome

LawDocsComply must sell itself: a visitor runs the free health check, sees exactly what the product costs for an organisation like theirs, starts a 7-day trial without talking to anyone, and converts by paying online — while a large bank or NBFC can still negotiate an enterprise contract. Every price, component, discount, promotion and trial rule is data, so the owner can change strategy without a release (R-070). Revenue streams that do not work can be switched off (R-044). Clients see, in money and hours, what the product saves them — but only on a transparent, evidenced method (R-067, NN-19).

| Outcome | Exit-gate measure |
|---|---|
| Transparent public pricing | `/pricing` renders three packages (Essentials, Professional, Enterprise), a comparison table of ≥ 60 feature rows and every add-on with its price delta, entirely from the published presentation catalogue; Lighthouse accessibility ≥ 95, WCAG 2.2 AA manual pass (NN-21); prices shown "excl. GST" with the GST-inclusive total shown before payment |
| Apple-style configurator | A visitor configures package + components + scale + billing cycle and sees the itemised running total update in ≤ 150 ms per change; dependencies and exclusions explained inline; configuration can be saved, shared as a link and converted to a quote |
| Self-serve trial → paid | From the end of the health-check report to an active trial tenant in ≤ 5 minutes and ≤ 12 clicks (PAN/CIN fetch pre-fills the organisation); from trial to paid subscription in ≤ 6 clicks via Razorpay-hosted checkout; no auto-conversion (OH8.9) |
| Owner controls commerce without code | Super admin can change a price, add a component, publish a promo code, extend one company's trial, re-order the feature list or retire a package; each change goes through maker-checker with a preview of the public page and of affected tenants, and takes effect on its `effective_from` without a deployment |
| Entitlements enforced server-side | Every module checks `entitlements.check()` on the API; UI hiding is never the control; a lapsed or restricted subscription never blocks reading, exporting, auditor or supervisor access, or any statutory deadline workflow already in progress (OH8.7; NN-29) |
| Billing and membership settings | Tenant admin can see plan, components, usage, seats, AI-credit wallet, invoices, payments, mandates, billing profile, tax documents, renewals and exit — 15 settings pages (§6) — and do every routine billing task without raising a ticket |
| Revenue-stream switches | Each LDC stream (Appendix N §N.6, RS-LDC-01…RS-LDC-30) can be turned on/off by market, segment and channel, with a kill switch that withdraws the purchase option within 5 minutes while honouring existing contracts |
| Honest savings | The Savings Dashboard shows hours saved, cost avoided and penalty exposure managed, each labelled *Recorded*, *Modelled* or *Estimated*, with the formula, inputs and evidence links one click away; no savings figure leaves the tenant (marketing, case studies) without the client's written consent and a claims-gate PASS (NN-19) |

---

## 2. Scope (in / out)

**In scope**

- **Presentation catalogue** (`bil.presentation_*`): packages, components (add-ons), feature rows, comparison groups, explainers ("i" help), badges, FAQs, configurator rules (dependencies, exclusions, bundles, minimums), localisation, SEO metadata — versioned, maker-checker, effective-dated.
- **Commercial catalogue integration**: SKUs, price books, coupons, trial policies and stream gates are owned by **OH8** (Appendix X §X.8); LDC consumes the signed catalogue (`GET /v1/catalogue/versions/{v}`) and submits change requests from the LDC Pricing Studio (`POST /v1/catalogue/change-requests`, new API in Appendix X). Interim `LOCAL` adapter (flag `bil.billing_port.mode = LOCAL_INTERIM`) implements the same port inside `bil` until OH8 is live, with a scripted migration to OH8 (§4L).
- **Public pricing page and configurator** (`apps/public`), embedded configurator in the onboarding wizard and tenant settings (`apps/web`).
- **Self-serve onboarding commerce flow** R-069: health check → account → trial tenant → organisation fetch → section selection → computed price → trial → convert → pay.
- **Trial management**: default 7 days, per-company extension, trial plan, AI-credit cap, expiry behaviour, reminders.
- **Checkout** via OH8 orders → Razorpay-hosted pages (cards, UPI AutoPay, netbanking, eNACH, Smart Collect virtual accounts) and "invoice later / purchase order" for enterprise.
- **Subscriptions**: monthly, quarterly, annual and multi-year terms; upgrade, downgrade, add/remove components, seat and entity changes; proration preview from OH8 quotes; renewals; cancellation; exit hand-off to P19.
- **Entitlement enforcement SDK** (`packages/entitlements`): modules, features, limits (users, legal entities, storage, AI credits, regulator packs, connectors, API calls), soft/hard limit behaviour, grace, `RESTRICTED` semantics.
- **Usage metering** at source and monthly `UsageRecorded` aggregates to OH8 (AI credits, extra storage, pass-through eSign/KYC/SMS, API calls) — aggregates only, never user or record identifiers.
- **Invoices, credit notes, statements of account, receipts, TDS certificates** — issued by OH8, displayed and downloadable in LDC; billing e-mails.
- **Billing & Membership settings** (15 pages, §6).
- **Promo codes, discounts, referral credits (non-professional referrers only), service credits** — catalogue objects from OH8; LDC validates and displays.
- **Revenue-stream registry mirror** (`bil.stream_gates`) and kill switches; purchase options appear only for `ACTIVE` streams.
- **Savings Dashboard** and Savings Ledger (`bil.savings_*`) with methodology registry, penalty library linkage (Appendix G penalty rules; Appendix N §N.9).
- **Super-admin Pricing Studio** in `apps/console` (presentation editor, change requests to OH8, preview, publish, per-tenant overrides and trial extensions — all via Correction-Entry-safe, maker-checker flows, D-02).
- **Marketplace checkout reuse**: P21 services and retainers use the same quote/order/invoice components (first-party services) — P20 builds the shared components.

**Out of scope (other phases or systems)**

- Price, tax, proration and invoice computation (OH8; LDC computes none — Ecosystem Spec §6.27).
- Razorpay keys and webhook secrets (OH8 vault only; the `LOCAL` adapter uses a separate LDC Razorpay account only if the owner approves OI-P20-01).
- Marketplace provider onboarding, engagement workflows and Academy sync (P21).
- RM portfolio and delivery console (P22).
- Health-check questionnaire engine and report (P23); P20 consumes its `HealthCheckCompleted` event.
- Revenue recognition (OH8.8), GSTR-1 preparation for LawDocs' own GST (OH8.6), collections and legal recovery (OH8.7).

---

## 3. Personas and permissions touched

| Role code | What they do in P20 | Key permissions |
|---|---|---|
| `anon`, `lead` | Browse pricing, use configurator, save/share configuration, start trial, buy a services-only item (P21) | `pricing.read`, `configurator.save`, `trial.start` |
| `ten_admin` | Choose plan and components, pay, manage billing profile, users and seats, invoices, mandates, renewals, cancellation; view savings | `billing.manage`, `subscription.change`, `savings.read`, `savings.configure` |
| `ten_cco`, `ten_kmp` (CFO) | View plan, invoices, savings; approve purchases above a tenant-set limit (tenant internal approval, §4F.6) | `billing.read`, `billing.approve_purchase` |
| `ten_viewer`, other tenant users | See own entitlements only ("Your plan includes…"), request an add-on from admin | `entitlements.read_self`, `addon.request` |
| `plt_super_admin` | Pricing Studio owner: edit presentation, raise price/promo/trial change requests, per-tenant overrides, extend trials, approve as checker where not maker | `pricing.studio.*`, `tenant.commercial_override` (maker-checker) |
| `plt_finance` | Billing operations from LDC side: reconcile entitlements, view OH8 invoice status, handle usage disputes, process trial/plan support requests | `billing.ops.*` (no price editing) |
| `plt_content_checker` (commercial checker designate) | Second approver for presentation changes (claims, comparison rows) | `pricing.studio.approve` |
| `plt_support` | Read billing state for a ticket; cannot change price or entitlements | `billing.read_any` (logged, purpose-bound) |
| `dlv_rm`, `dlv_lead` | See client plan, components, renewal date, usage (P22 view); propose upsell quotes (sent to client admin for acceptance) | `billing.read_client`, `quote.propose` |
| OH8 (machine) | Publishes catalogue, `PlanChanged`, `EntitlementChanged`, `InvoiceIssued`, payment events | mTLS client, scope `billing.events:write` |

Segregation of duties: the person who drafts a price or promo change cannot approve it (NN-05); a super admin cannot approve a commercial override for a tenant in which they hold any tenant role; `plt_finance` cannot edit the presentation catalogue.

---

## 4. Functional requirements

### 4A. Commercial architecture and `BILLING_PORT`

- **FR-P20-01 — Ownership split.** OH8 is the source of truth for SKUs, price books, coupons, trial policies, stream gates, quotes, orders, subscriptions, signed entitlements, invoices, credit notes, receipts, mandates and dunning (Ecosystem Spec §6.27; OH8.1–OH8.7). LDC (`bil` schema) owns: the **presentation catalogue**; the **configurator rule set** (dependencies, exclusions, bundles — validated against SKU dependencies in the OH8 catalogue); the **entitlement mirror** as applied; **usage meters at source**; the **trial lifecycle** of each tenant; the **Savings Ledger**; and the tenant-facing billing UI.
- **FR-P20-02 — Port.** All commerce calls go through `BILLING_PORT` (`packages/billing-port`) with operations `getCatalogue(version)`, `quote(req)`, `order(quoteId)`, `listInvoices(tenant)`, `getDocument(id)`, `disputeUsage(req)`, `getEntitlements(tenant)`, `submitCatalogueChange(req)`, `getChangeStatus(id)`, `extendTrial(req)`, `validatePromo(code, ctx)`. Adapters: `OH8` (default target), `LOCAL` (interim, §4L), `MOCK` (tests). The adapter in force is a Governed setting; switching adapters requires a migration run with reconciliation sign-off.
- **FR-P20-03 — No price or tax computed by LDC.** Display prices on the pricing page and configurator come from the signed catalogue's price book in force; any amount that will be charged (proration, GST, discounts, totals at checkout) comes from an OH8 quote. The configurator labels its running total "Estimated total — final amount, GST and proration confirmed at checkout" until a quote is obtained. A contract test fails CI if any module other than the `LOCAL` adapter multiplies a price by a tax rate.
- **FR-P20-04 — Signed artefacts.** LDC verifies the JWS of every catalogue version and every `EntitlementChanged` against the pinned Hub key (rotation per Appendix L); unsigned or mismatched artefacts are rejected with `LDC-BIL-001` and raise `ComplianceIssueRaised` to `plt_security_officer`.
- **FR-P20-05 — Offline tolerance.** If OH8 is unreachable, LDC keeps serving the last valid catalogue for display and the last valid signed entitlement for 30 days (Ecosystem Spec §6.27), shows a non-blocking banner to `plt_finance`, queues quotes as "pending confirmation", and never changes a tenant's access because of a Hub outage.

### 4B. Packages and components (presentation catalogue)

- **FR-P20-06 — Three public packages.** Seeded (values in Appendix N §N.2, all prices `[OWNER TO SET]`, starting from the live site's ₹10,000 and ₹30,000 per month):
  - **Essentials** — for small and mid-sized companies, LLPs, small NBFCs (Base Layer), co-operative societies, IFSCA units starting operations. Includes the compliance workspace, one primary regulator pack, governance basics, calendar, tasks, notifications, updates feed, DMS core, standard reports, 1 legal entity, 10 named users, Vidhi AI starter credits.
  - **Professional** (badge "Most chosen", only if the claim is supported by order data; else no badge — NN-19) — for larger and regulated entities (NBFC Middle/Upper Layer, UCBs, listed companies, AIF/MF managers, insurers/intermediaries). Adds maker-checker depth, multi-regulator packs, policy lifecycle with Vidhi drafting, committee & board module, ERM core, audit lite, advanced DMS (OCR, translation), API access, SSO, 3 legal entities, 40 users, higher AI credits.
  - **Enterprise** (custom) — banks, groups, conglomerates, ARCs, large NBFCs: unlimited entities/users bands, dedicated environment option (`DEDICATED` deployment), BYO storage, custom SLAs, data residency attestations, premium support, named CSM, regulator-view grants, custom integrations; "Talk to us" plus a configurable "from" price.
- **FR-P20-07 — Base + add-ons model.** Each package has a **base price** and a list of **components**: (i) *included* (✓), (ii) *add-on* with a price delta (+ ₹/month or per unit), (iii) *not available* (—), (iv) *enterprise only*. Components (Appendix N §N.3, codes `ADD-*`): Labour Codes & POSH Suite; HRMS & Payroll; Enterprise Risk Management; Risk Assessment Lab (ICAAP, stress testing, scenario analysis, capital & ratio engine); Audit Management; Return Studio (RBI returns, CIC files); Tax Data Exports (GST/TDS data); Data Protection & Cyber (DPDP, GDPR, CCPA, CERT-In); Third-Party & Outsourcing Risk; Board Portal & Company Secretarial Pro; Listed Company Pack (LODR, PIT, SAST); Co-operative Society Suite; Grievance Redressal Desk; Advanced DMS (OCR, handwriting, translation); additional regulator packs (each); additional legal entity; user packs (10/25/50); storage packs; BYO storage connector; ecosystem/third-party connectors; API tier; SSO/SCIM; dedicated environment; premium support; Vidhi AI credit packs.
- **FR-P20-08 — Standalone products.** Some components are also sold without the compliance base (R-014): *Labour & HRMS Standalone*, *Grievance Desk Standalone*, *Board Portal Standalone*, *Data Protection Standalone*. A standalone SKU provisions the same tenant with only those modules; adding the compliance base later is an upgrade, not a migration.
- **FR-P20-09 — Pricing dimensions.** The catalogue supports, per SKU: flat per period; per legal entity; per user band; per entity-size band (turnover, AUM, number of branches or members — declared by the client and verifiable from public data where available); per unit (AI credits, storage GB, eSign, return runs); minimum commitment; volume tiers; multi-year terms. Which dimension applies to which SKU is catalogue data, never code (R-070).
- **FR-P20-10 — Feature list and comparison.** Feature rows are grouped (Compliance, Regulatory Change, Governance & Secretarial, Policies & Documents, Risk, Audit, Returns & Data, People & Labour, Data Protection & Cyber, Vidhi AI, Integrations, Security & Admin, Support & Services). Each row: label, "i" explainer (≤ 280 chars + link to Help Centre article), value per package (✓, —, add-on price, limit text), evidence flag for any claim (e.g., "SOC 2 Type 2 report available" may appear only when the claims register has the evidence — NN-19), SEO anchor. Seed of ≥ 120 rows in Appendix N §N.4.
- **FR-P20-11 — Dependencies and exclusions.** Configurator rules: `requires` (e.g., Risk Assessment Lab requires ERM), `includes` (e.g., HRMS includes the employee master used by Labour), `excludes` (e.g., Standalone Board Portal excludes compliance-base-only features), `min_package` (e.g., API tier ≥ Professional), `bundle` (e.g., "Lender Pack" = ERM + Risk Lab + Return Studio at a bundle discount), `entity_type_recommended` (e.g., Return Studio recommended for NBFC/UCB/bank). Rules validated against OH8 SKU dependencies at publish.
- **FR-P20-12 — Recommendations without dark patterns.** The configurator may pre-select components only when (a) they are included in the package at no extra cost, or (b) the visitor accepted a recommendation from the health check with an explicit click; it never pre-ticks a paid add-on (CCPA Dark Patterns Guidelines 2023, "basket sneaking"; E-Commerce (Amendment) Rules 2026 r.4(15) self-audit adopted as policy for B2B too [INTERP]). Each recommendation shows *why* ("Recommended because you selected NBFC – Middle Layer: RBI supervisory returns apply").

### 4C. Public pricing page and configurator

- **FR-P20-13 — Page structure** (`/pricing`, copy in Appendix P): hero ("Simple, transparent pricing — see your price before you talk to anyone"); segment switcher (Company & LLP · NBFC & HFC · Bank & UCB · Co-operative · SEBI-regulated · IFSCA · Insurance) that changes recommended package, regulator pack and default components; billing-cycle toggle (Monthly / Annual with the saving shown as an amount and %); three package cards; "Build your plan" configurator; comparison table (sticky header, collapsible groups, "show differences only" toggle, print/PDF); add-on catalogue; services strip linking to the marketplace (P21) including "Buy services without a subscription"; trial explainer; FAQs (≥ 25, Appendix N §N.10); trust strip (only evidenced claims); "Talk to sales" form (creates OH3 lead via `POST /v1/crm/requests` with consent capture — Appendix X §X.2).
- **FR-P20-14 — Configurator steps** (Apple-style; left column choices, right sticky "Your plan" summary):
  1. *Organisation* — entity type and regulator(s) (pre-filled from the health check or PAN/CIN fetch), number of legal entities, size band.
  2. *Package* — Essentials / Professional / Enterprise; switching shows what is gained or lost.
  3. *Components* — cards grouped by area; each card: name, one-line value, "i", price delta, included/add-on state, dependency notes; toggling a component that `requires` another opens an inline prompt ("Risk Assessment Lab needs Enterprise Risk Management (+ ₹x). Add both?").
  4. *Scale* — users, entities, storage, AI credits (slider with included allowance marked), API tier.
  5. *Services (optional)* — implementation package, data migration, training seats, retainer (links to P21 offerings; first-party only in v1.0).
  6. *Billing* — cycle, term, payment method preference (card/UPI AutoPay, eNACH, invoice/PO); promo code field (validated live; shows the discount line and expiry).
  7. *Review* — every line item, included allowances, estimated GST (from catalogue tax hint, labelled estimate), what happens at trial end, cancellation terms, links to MSA, DPA, RE Addendum (if regulated entity), refund policy; actions: **Start 7-day free trial**, **Buy now**, **Request a quote**, **Save / share configuration**, **Download PDF summary**.
  The summary panel updates on every change (≤ 150 ms, client-side from the cached signed catalogue), shows monthly-equivalent and billed-amount figures, and on mobile collapses to a bottom sheet.
- **FR-P20-15 — Saved configurations.** `bil.saved_configurations` with a short, unguessable token (≥ 128 bits), expiry 30 days (setting), no personal data unless the visitor chooses to e-mail it; a shared link opens the configurator read-only with a "Make a copy" action. A saved configuration converts to an OH8 quote on "Request a quote" (validity 7 days for product quotes, OH8.4).
- **FR-P20-16 — Transparency statements.** Next to every total: "Prices exclude GST at the applicable rate (currently 18% for software services — confirmed on invoice)" [VERIFY rate per SAC in tax review]; trial statement "No card needed for the trial. Your trial never converts to a paid plan automatically."; cancellation statement "Cancel any time from Settings › Billing › Cancel; you keep read and export access for the notice period and 30 days after"; price-change statement "We give at least 30 days' notice of any price change, effective at renewal" (OH8.4).
- **FR-P20-17 — Prior-price display.** When a promotional reduction is shown on the public page, the "prior price" displayed is the lowest price of that SKU in the preceding 30 days (adopting E-Commerce (Amendment) Rules 2026 r.4(13) from 1 Jan 2027 [VERIFY applicability to B2B; adopted as policy]); the presentation catalogue stores price history to compute it; no strike-through "anchor" price that was never charged (OH8.9).
- **FR-P20-18 — Currency and locale.** INR default with lakh/crore grouping; USD/AED/SGD display for international packs (D-19) only when the OH8 price book has an approved price for that market; no automatic FX conversion on the public page.
- **FR-P20-19 — Performance and SEO.** Server-rendered (Next.js RSC) with static generation per catalogue version; JSON-LD `Product`/`Offer` (`priceSpecification` with `valueAddedTaxIncluded = false`) per package (P23 owns the SEO system; Appendix P); `llms.txt` lists the pricing page; no prices hidden behind JavaScript-only rendering (the current live page renders client-side and is invisible to crawlers — fix).

### 4D. Self-serve onboarding and trial (R-069)

- **FR-P20-20 — Entry points.** (a) Health-check report "See your plan and start a free trial" (carries `health_check_id`, entity type, regulator, recommended components — only if the visitor consented to reuse); (b) pricing page "Start free trial"; (c) configurator "Start 7-day free trial" with the configured plan; (d) marketplace "Add the platform" (P21); (e) RM-sent trial invitation (P22, `quote.propose`).
- **FR-P20-21 — Sign-up.** Work e-mail + mobile OTP (DLT-registered template) + name + designation; password-less magic link or passkey; DPDP notice (itemised, Rule 3) and consent for service communications; optional, separate, unticked marketing consent (OH3.3 send gate). Personal e-mail domains are allowed for companies and LLPs but flagged for verification before conversion. Disposable domains are rejected (`LDC-BIL-010`).
- **FR-P20-22 — Organisation fetch.** User enters PAN, CIN, LLPIN or GSTIN (P01 owns the fetch adapters): legal name, constitution, registered address, incorporation date, directors/designated partners, GSTIN list by State, status; for regulated entities the user selects the regulator and registration type and enters the CoR/registration number (verified later in P01/P15). Duplicate detection: an organisation already holding an LDC tenant is told "Your organisation already uses LawDocsComply — ask <masked admin e-mail> to invite you" and may request access; no second trial per organisation (`org_id` uniqueness per product and environment, Ecosystem Spec §6.29).
- **FR-P20-23 — Section selection and computed price.** The wizard shows the regulator packs and components recommended for the entity type (from P15 sector logic), with the package that fits and the computed price from the catalogue (display price); the admin can toggle components exactly as in the configurator; the selection becomes the **trial configuration** and the **default conversion quote**.
- **FR-P20-24 — Trial tenant.** LDC creates the trial tenant itself (product-originated, `origin = SELF_SERVE`) — a production-grade tenant in India region with the full security baseline — and notifies OH with `TenantSelfServeCreated` (new event, Appendix X §X.3) so OH3/OH4 create the account, lead and onboarding case automatically. Before the first upload of any document or personal data, the admin accepts the click-wrap **Terms of Service**, **Data Processing Agreement** and, for regulated entities, the **RE Addendum** (outsourcing/IT-outsourcing clause matrix; Appendix X §X.3 lists the clauses) by an e-sign-equivalent click-wrap with identity, timestamp, IP and document hash recorded (IT Act 2000 s.10A; electronic contract) [INTERP]. This is a deliberate deviation from OH8.9 "sandbox trials with synthetic data only", justified because LDC holds the client's own compliance data, not borrower data; recorded as decision request DR-S9-01 for the master and OH addendum.
- **FR-P20-25 — Trial plan.** Default trial plan = **Professional features** with the client's chosen regulator pack(s), caps: 3 legal entities, 15 users, 2 GB storage, 200 Vidhi AI credits, no API keys, no BYO storage, no regulator-view grants, exports allowed (watermarked "Trial export" on cover sheet only, never on the client's own documents). The trial plan is a catalogue object (`trial_policy`) editable in Pricing Studio.
- **FR-P20-26 — Trial length and extension.** Default **7 days** (`bil.trial.default_days`, G, bounds 1–60). Extension per company from Pricing Studio or the delivery console (P22) with reason code (`SALES_EVALUATION`, `PROCUREMENT_DELAY`, `ONBOARDING_ISSUE`, `PARTNER_REQUEST`, `OTHER`): ≤ 14 additional days by `plt_super_admin` or `dlv_lead` alone; beyond 14 days total extension needs a checker (`plt_super_admin` ≠ maker). Every extension writes an audit event and a tenant-visible notice; the tenant may also request one extension of up to 7 days in-product (auto-approved once, setting `bil.trial.self_extension_days`, T within G bounds 0–7).
- **FR-P20-27 — Reminders.** Day 1 welcome + checklist; T-3 days and T-1 day in-app and e-mail ("Your trial ends on DD-MM-YYYY. Nothing will be charged."); expiry notice. No countdown timers, no "only n hours left" banners (OH8.9).
- **FR-P20-28 — Trial expiry.** On expiry the tenant moves to `TRIAL_EXPIRED`: read-only, export available, no new tasks or uploads, regulatory Updates still shown (so the client is never left without notice of changes it subscribed to see during the trial); after `bil.trial.retention_days` (G, default 30, bounds 15–90) a 7-day deletion notice is sent; then deletion per P19 retention with a deletion certificate. Conversion at any time before deletion restores full access with all trial data.
- **FR-P20-29 — Conversion.** "Choose plan & pay" opens the configurator at step 7 with the trial configuration; the admin may change anything; an OH8 quote is obtained; payment or PO; on `SubscriptionPaymentReceived` (or contract activation for invoice-later) the tenant becomes `ACTIVE` with the signed entitlement; the onboarding case in OH4 continues with kick-off (Appendix X §X.4).

### 4E. Checkout and payment

- **FR-P20-30 — Order.** `BILLING_PORT.order(quoteId)` → OH8 `POST /v1/billing/orders` (Idempotency-Key = `quote_id` + attempt) returns a Razorpay-hosted URL; LDC performs a **top-level redirect** (no Razorpay script on LDC pages; PCI DSS v4.0.1 SAQ A scope — Appendix Q); return URL lands on `/billing/checkout/return?order=` which polls the server for confirmation; **a browser redirect is never proof of payment** (Ecosystem Spec §6.27).
- **FR-P20-31 — Methods.** Cards (tokenised by Razorpay under the RBI card-on-file tokenisation framework), UPI and UPI AutoPay, netbanking, eNACH (recurring > ₹15,000 per debit), Smart Collect virtual account / bank transfer for large invoices, and invoice-later against a PO for Enterprise or where the contract allows. Recurring card/UPI mandates follow the RBI e-mandate framework as implemented by OH8.7 (AFA at registration, ₹15,000 no-AFA limit [VERIFY current limit and exemptions], pre-debit notice ≥ 24 h, plus LDC's T-48 h courtesy notice).
- **FR-P20-32 — Tenant internal approval (optional).** Tenant admin may require that purchases above `bil.tenant.purchase_approval_threshold` (T, default off) are approved by a named tenant approver (e.g., CFO) before the order is placed; the quote is held in `PENDING_TENANT_APPROVAL`; approver sees the quote, GST and terms and approves with step-up MFA.
- **FR-P20-33 — GST details at checkout.** Billing profile is mandatory before the first order: legal name (pre-filled from fetch), GSTIN per billing State (validated format + GSTIN API status where available), place of supply, billing address, PAN, PO number (optional/required per tenant setting), billing contacts (≥ 1, ≤ 10), e-invoice recipient e-mail, SEZ/IFSC unit flag with LUT reference (zero-rated supply, IGST Act s.16 — OH8.6 [VERIFY IFSC treatment]), TDS applicability declaration (customer deducts under Income-tax Act 2025 s.393 [VERIFY]).
- **FR-P20-34 — Failure handling.** Payment failure leaves the trial or subscription unchanged; clear message with the reason class from OH8 and retry; three failed attempts in 24 h offer bank transfer or "Talk to us"; webhook delay > 15 min shows "We are confirming your payment with the bank — you will get an e-mail"; reconciliation job resolves within 2 hours or raises a `plt_finance` task.

### 4F. Subscription lifecycle and changes

- **FR-P20-35 — States.** LDC mirrors OH8 states (OH8.4): `TRIAL`, `TRIAL_EXPIRED`, `PENDING_ACTIVATION`, `ACTIVE`, `RENEWAL_DUE`, `PAST_DUE`, `GRACE`, `RESTRICTED`, `TERMINATION_NOTICE`, `CANCELLATION_REQUESTED`, `EXIT`, `CLOSED`. LDC adds the trial states (product-side) and never invents a commercial state OH8 does not know.
- **FR-P20-36 — Upgrade.** Package upgrade, component add, seat/entity/storage increase: preview via OH8 quote (prorated charge, GST, entitlement diff); effective immediately on payment (or on PO acceptance); `PlanChanged` + `EntitlementChanged` received → modules attached (`ModuleAttached`). Note Razorpay constraint: subscriptions created with domestic cards allow only offer updates, so OH8 handles a plan change on such a subscription by invoicing the prorated difference and re-creating the subscription at the next cycle [VERIFY OH8 implementation; Razorpay docs read 25 Oct 2026].
- **FR-P20-37 — Downgrade and component removal.** Effective at term end by default (OH8.4); the admin sees exactly what will stop: e.g., "Return Studio will become read-only on 31-03-2027; prepared return packages, history and evidence stay viewable and exportable" (NN-29). Removing a component that other components require is blocked with a list of dependants. Downgrading below current usage (e.g., users) requires the admin to deactivate users first or accept automatic deactivation of the least-recently-active non-admin users after a 7-day notice — never deactivation of a user holding an open maker/checker task without reassignment (P04 guard).
- **FR-P20-38 — Billing-cycle and term change.** Monthly ↔ annual at the next renewal by default; immediate switch to annual allowed with proration credit.
- **FR-P20-39 — Renewal.** Reminders at T-90 (with any price change notice, ≥ 30 days before effect), T-30, T-7 (OH5.2); auto-renewal stated clearly at purchase and in each reminder; one-click "Turn off auto-renewal" in settings.
- **FR-P20-40 — Cancellation.** Settings › Billing › Cancel: same number of steps as purchase or fewer (no confirm-shaming, no forced call); reason survey optional; shows end date, refund position (per refund policy — annual plans: pro-rata refund within the first 30 days of the first term only [OWNER TO SET]; otherwise no refund, access to end of term), export reminder with one-click full export (P19); `CANCELLATION_REQUESTED` until effective, withdrawable; at effect `SubscriptionCancelled` → `EXIT` → P19 exit process; read and export continue throughout notice and for 30 days after (`bil.exit.read_only_days`, G, default 30, floor 30).
- **FR-P20-41 — Pause.** Not offered in v1.0 [REC: pausing a compliance tool creates unmanaged obligations; offer downgrade instead].

### 4G. Entitlement enforcement

- **FR-P20-42 — SDK.** `packages/entitlements` exposes `check(tenant, module, feature?)`, `limit(tenant, key)`, `consume(tenant, meter, qty)` and a NestJS guard `@RequiresEntitlement('ret.return_studio')`. Entitlement state is read from the local mirror (`bil.entitlements_applied`) updated only by verified `EntitlementChanged` events (or the `LOCAL` adapter); cached per tenant with event-driven invalidation (tenant id in the cache key, NN-01).
- **FR-P20-43 — Never-block list (floor, not configurable).** No entitlement state, limit or dunning stage may block: (a) reading any existing record; (b) exporting data (P19); (c) access by `ten_external_auditor`, `ten_internal_auditor`, `ten_secretarial_auditor`, `ten_is_auditor`, `ten_supervisor_view` under an active grant; (d) completing a workflow instance already started for a statutory deadline within 30 days (e.g., a return under preparation, a grievance under clock, a board meeting already convened); (e) viewing regulatory Updates for packs the tenant already holds; (f) the grievance intake page published on the client's website (P14) — new grievances continue to be received and acknowledged even in `RESTRICTED`. Test `NN-29_entitlement_never_blocks`.
- **FR-P20-44 — Limits behaviour.** Soft limit (80%): banner and admin e-mail; at 100%: for users — new invitations blocked, existing users unaffected; for storage — uploads continue for evidence linked to an open compliance instance with a due date in ≤ 30 days, other uploads blocked with an upgrade prompt; for AI credits — Vidhi falls back to deterministic features (search, templates) and shows the credit wallet; for legal entities — new entity creation blocked. No overage is charged unless the tenant opted into PAYG overage (`bil.tenant.overage_opt_in`, T, default off).
- **FR-P20-45 — Module attach/detach.** Attach = module schemas already exist; enabling flips entitlement, runs the module's setup wizard and seeds default configuration; detach = module becomes read-only and hidden from navigation (still reachable through Search, history and export); `ModuleAttached` / `ModuleDetached` to OH8 (OH2.4).
- **FR-P20-46 — Daily reconciliation.** By 06:00 IST LDC answers OH8 `GET /v1/entitlements?tenant=` and runs its own comparison; mismatches raise `ReconciliationBreakRaised` and a `plt_finance` task; the tenant is never downgraded automatically because of a mismatch — the more generous of the two states applies until resolved [REC].

### 4H. Usage metering

- **FR-P20-47 — Meters** (Appendix N §N.5): `AI_CREDITS` (Vidhi consumption in credits, not tokens — conversion table versioned), `STORAGE_GB_MONTH`, `ESIGN_PASS_THROUGH` (count by ESP), `KYC_VERIFICATION_PASS_THROUGH` (count by type), `SMS_WHATSAPP_PASS_THROUGH`, `API_CALLS` (above tier allowance), `RETURN_RUNS` (Return Studio packages generated, if PAYG pricing is switched on), `EXTRA_USERS_PEAK`, `EXTRA_ENTITIES`. Measured at source in the producing module; daily provisional and monthly final statements by WD+3; `UsageRecorded` with `usage_aggregate_v1` (tenantid, legal entity, meter, period, quantity, statement_version, statement hash) — **never** user, record, document or person identifiers (Ecosystem Spec §6.27).
- **FR-P20-48 — Transparency.** Settings › Billing › Usage shows the same aggregates the client will be billed on, with drill-down available only inside the tenant (e.g., AI credits by module and by user for the tenant admin — that detail never leaves LDC). Dispute within 7 days via `POST /v1/usage-disputes`.
- **FR-P20-49 — AI credit wallet.** Prepaid credit packs and monthly included credits; expiry of included credits at period end (no rollover by default, `bil.ai.rollover`, G); purchased packs valid 12 months; low-balance alerts at 20% and 5%; a hard cap per user optional (T). Vidhi never consumes credits for safety-critical deterministic functions (deadline computation, applicability) because those are not AI (NN-14).

### 4I. Invoices, credit notes and tax documents

- **FR-P20-50 — Display and download.** Settings › Billing › Invoices lists OH8 invoices, credit/debit notes, receipts and statements of account (filters by FY, status, type); PDF download (GST invoice with IRN and signed QR where e-invoicing applies — OH8.6), XLSX statement export, bulk ZIP by FY; every document's hash shown; a copy is filed automatically in the tenant DMS under `20 Billing, Subscription and Invoices/<FY>/` (P07) so it is included in LDC-EXPORT-1.0 (Appendix M; NN-10).
- **FR-P20-51 — E-mail delivery.** `InvoiceIssued` → e-mail to billing contacts with the PDF attached (or a secure link if > 5 MB), sent by LDC's transactional mail service on behalf of the selling entity with the OH8-provided template, or by OH8 directly (Appendix X §X.8 decides; default OH8 sends, LDC shows in-app) — no duplicate e-mails (idempotency on invoice_no).
- **FR-P20-52 — TDS certificates.** Upload of the customer's TDS certificate per quarter (form under the Income-tax Act 2025 [VERIFY form number; OH8.6 cites Form 131]) against invoices; status tracked; forwarded to OH8 `tds_receivable`.
- **FR-P20-53 — Billing corrections.** Disputes about an invoice open an OH6 ticket of category `BILLING_DISPUTE` with the invoice reference; dunning pauses for that invoice (OH8.7); corrections are always credit/debit notes from OH8 (never edits).

### 4J. Dunning in LDC

- **FR-P20-54 — Tenant view.** `PAST_DUE` banner to `ten_admin` and billing contacts; `GRACE` banner to all admins; `RESTRICTED` (after 7 days' written notice): new users, new modules, new legal entities, new connector activations and AI credit top-ups via card are blocked; everything in the never-block list (FR-P20-43) continues; `TERMINATION_NOTICE` triggers the P19 exit pack preparation automatically and an e-mail to all `ten_admin` and `ten_cco` users.
- **FR-P20-55 — Reinstatement.** Full payment or an approved payment plan (OH8) returns the subscription to `ACTIVE` within 15 minutes of the event.

### 4K. Revenue-stream registry and switches (R-044)

- **FR-P20-56 — Mirror.** `bil.stream_gates` mirrors OH8 stream gates for the LDC selling entity (Appendix N §N.6, RS-LDC-01…RS-LDC-30: subscriptions by package; add-on subscriptions; standalone products; monthly rental of dedicated environments; PAYG meters; AI credit packs; implementation; data migration; regulatory-pack customisation; managed compliance retainers; marketplace first-party services; marketplace listing subscriptions for permitted professions; training seats; certification-readiness services; white-label/partner licences; API access; premium support; sponsored placement (OFF; never for advocates/CAs); event sponsorships (OFF); benchmark reports (OFF pending DPDP and confidentiality review); etc.).
- **FR-P20-57 — Switch semantics.** A purchase option is shown only if its stream is `ACTIVE` **and** the LDC-side switch `bil.stream.<code>.enabled` is on for the market, segment and channel. LDC-side switches can only narrow OH8 gates, never widen them (defence in depth, OH8.3). Kill switch: `plt_super_admin` (with a checker for streams in Appendix N flagged "high impact") turns a stream off; within 5 minutes all purchase surfaces hide it (catalogue cache invalidation event `StreamSwitchChanged`); existing subscriptions continue on their terms; the change is announced to RMs (P22).
- **FR-P20-58 — Experiment hooks.** Price tests only as OH8.10 experiments (approved, segment-bounded, new customers only); LDC renders the variant the quote returns; never different prices for the same buyer in the same session; experiment id logged on the quote.

### 4L. Interim `LOCAL` adapter (only if OH8 is not live when P20 must ship)

- **FR-P20-59 — Scope.** Implements the `BILLING_PORT` contract in `bil_local` schema: SKUs, price books, coupons, quotes, orders, Razorpay (LDC-owned account; keys in LDC vault; SAQ A pattern), subscriptions, GST invoice generation (CGST Rules r.46 fields; e-invoicing via a GSP if AATO requires; credit notes), dunning per OH8.7 timings. Behind flag `bil.billing_port.mode = LOCAL_INTERIM` (G; requires owner decision OI-P20-01).
- **FR-P20-60 — Migration to OH8.** A scripted migration exports SKUs, price-book versions, coupons, customers, subscriptions, invoices (as historical documents, not re-issued), mandates (tokens re-mapped where Razorpay allows; else re-authorisation campaign), open balances; reconciliation report signed by `plt_finance` and the OH finance controller; dual-run for one billing cycle; then the adapter flips to `OH8` and `bil_local` becomes read-only archive.

### 4M. Pricing Studio (super admin, `apps/console`)

- **FR-P20-61 — Editor.** Tabs: Packages · Components · Feature rows · Comparison groups · Configurator rules · Bundles · Promotions · Trial policies · FAQs & explainers · Segment presets · SEO · Preview & publish · History. Rich preview renders the exact public page and configurator for any segment and date (`?as_of=`), side-by-side with the live version, with a diff of every changed string and price.
- **FR-P20-62 — Two kinds of change.** *Presentation changes* (copy, order, grouping, explainers, badges, FAQ, configurator layout) are LDC-owned: maker → checker → publish with `effective_from`. *Commercial changes* (price, new SKU, coupon, trial policy, stream gate, tax hints) are drafted in the same editor but submitted to OH8 as catalogue change requests (`POST /v1/catalogue/change-requests`; Appendix X §X.8) and follow OH8's pricing-committee approval and legality gate; the studio shows status (`SUBMITTED → IN_REVIEW → APPROVED → PUBLISHED` or `RETURNED`) and publishes the matching presentation version automatically when OH8 publishes the catalogue version.
- **FR-P20-63 — Promo codes.** Types: percentage, fixed amount, extended trial, free component for n months, first-term discount, partner code; constraints: segments, packages, components, first purchase only, min term, max redemptions (total and per org), validity window, stackability (default not stackable), channel; code format rules (no codes that look like guaranteed outcomes; claims gate on campaign text). Codes are OH8 coupons; the studio drafts and tracks redemption analytics (aggregate).
- **FR-P20-64 — Per-tenant commercial overrides (R-071).** Super admin can, for a specific tenant: extend trial (FR-P20-26); grant a component free for a period (as a coupon, not an entitlement hack); apply a negotiated price (through an OH8 sales quote — the studio deep-links to OH8 Revenue › Quotes); change components or limits (through an order or a zero-value entitlement change in OH8, so invoices and entitlements stay consistent). Every override is a reason-coded, maker-checker action recorded in the audit ledger; corrections to earlier overrides are Correction Entries (D-02); the tenant sees a notice in Settings › Billing › History ("Your trial was extended by LawDocs on 26-10-2026 by 7 days: procurement delay").
- **FR-P20-65 — Guard-rails.** The studio cannot publish: a package with no price for the selected market; a comparison row asserting a certification or regulator endorsement without a claims-register reference (NN-19); a "Most popular" badge without a computed basis (orders in last 90 days, stored); a feature row for a module whose entitlement key does not exist; a configurator rule that makes a mandatory dependency purchasable alone. Lint errors block publish (`LDC-BIL-030…039`).

### 4N. Savings Dashboard (R-067)

- **FR-P20-66 — Purpose and honesty principle.** The dashboard quantifies value under three labelled evidence levels: **Recorded** (facts the platform has: e.g., late fees actually paid this year vs last year, as entered with receipts; obligations completed before due date; hours logged by users), **Modelled** (exposure avoided computed from the penalty library and the tenant's own historical late rate — formula shown), **Estimated** (time saved from baseline minutes per activity × activity counts; baselines editable by the tenant). Each tile shows its level, formula, inputs, period and a "How we calculated this" panel. Default view shows Recorded and Modelled; Estimated is shown with a dotted outline and the word "estimate".
- **FR-P20-67 — Metrics** (formulas in Appendix N §N.9):
  - *Hours saved* = Σ_activity (baseline_minutes − measured_minutes) × count ÷ 60, where measured minutes come from workflow timestamps (task open → submit; checker queue time excluded) and baseline minutes from the methodology registry (seeded from a time-and-motion study `[OWNER TO SET]`, editable by tenant with history).
  - *People-cost saved* = hours saved × blended hourly cost (tenant-entered by role band; default blank — tile hidden until set).
  - *Penalty exposure managed (Modelled)* = Σ_obligations_with_penalty_rule completed on time × expected penalty if late, where expected penalty = P(late | tenant baseline) × penalty(rule, reference delay d); P(late) from the tenant's own pre-LDC baseline (entered or imported) or, if absent, shown as a range using d = 1 day (minimum) and d = 30 days; penalty rules from Appendix G penalty library (e.g., Companies Act s.403 ₹100/day additional fee; GST late fee ₹50/day with caps; SEBI SOP per-day fines) — each rule carries citation and `last_verified_at`; rules older than 180 days without verification are excluded and flagged.
  - *Late fees actually paid (Recorded)* = Σ late fees/penalties recorded against filings (from P04 evidence fields "late fee paid" and P11 return packages), YoY comparison.
  - *Tool and service cost avoided (Recorded if entered)* = tenant-entered costs of replaced tools/consultants with dates.
  - *Compliance health trend* = on-time completion %, overdue count, high-risk overdue count, average days late (from P04).
  - *Regulatory changes handled* = Updates received, assessed, actioned; median days from Update to impact assessment.
  - *Return on subscription* = (people-cost saved + tool cost avoided + recorded late-fee reduction) ÷ subscription cost for the period — shown only when all inputs are Recorded or tenant-entered; never includes Modelled exposure (prevents inflated ROI).
- **FR-P20-68 — Placement.** Settings › Savings & Value (tenant admin, CFO, CCO), a Savings widget for KMP and Board dashboards (P02/Appendix C), a quarterly "Value report" PDF/DOCX for the board pack (P06) with methodology annex, and the renewal QBR pack shared with the RM (P22) only if the tenant allows (`bil.savings.share_with_rm`, T, default on for retainer clients, off otherwise).
- **FR-P20-69 — Use outside the tenant.** Aggregated, anonymised savings statistics may be used in marketing only (a) across ≥ 20 tenants, (b) with method disclosure, (c) after claims-gate PASS (`GET /v1/claims-gate/check`), and (d) never naming a client without written consent; a single client's figures go into a case study only with the client's written approval and, for an RE, its compliance sign-off (OH5.3).

### 4O. Notifications (P04 notification service; templates in Appendix N §N.11)

Trial started / T-3 / T-1 / expired / deletion notice; quote ready; payment received; payment failed (with retry info); invoice issued; mandate pre-debit courtesy notice; usage 80%/100%; AI credits low; renewal T-90/T-30/T-7; price-change notice; plan changed; component attached/detached; restriction notice; termination notice; trial extended by LawDocs; promo expiring (only if the user opted into marketing); savings report ready. All billing notifications are Notifications (work inbox), never Updates (NN-27); approvals and termination notices are mandatory (cannot be muted).

### 4P. Multi-currency and cross-border commerce *(v1.1; Appendix Y §Y.9–§Y.10; X-02)*

**FR-P20-70 — Price books by currency.** OH8 holds one price book per contract currency (INR, USD, AED, SGD, EUR, GBP; Appendix N §N.15). LDC never converts a price with an FX rate to show a "local" price; it shows the price book that applies to the visitor's selected market. Market is pre-selected from the visitor's country (IP-based hint plus explicit selector), never forced.

**FR-P20-71 — Tax preview.** At checkout LDC collects billing country, billing entity name and address, and tax identifiers (GSTIN for India; EU VAT number; UK VAT; UAE TRN; Singapore GST/UEN; US EIN where relevant), sends them to OH8 for validation (e.g., VIES for EU VAT numbers) and shows OH8's tax treatment preview ("Export of services under LUT — no IGST", "Reverse charge — VAT payable by you", "GST 18% (CGST+SGST or IGST)") before payment. All tax logic is OH8's (X-02); LDC only displays it.

**FR-P20-72 — Withholding-tax documents.** For foreign customers, Settings → Billing → Tax documents lets the customer download LawDocs' Tax Residency Certificate and Form 10F-related information that OH8 publishes, and upload withholding certificates they issue, so OH8 can reconcile short payments [VERIFY per treaty].

**FR-P20-73 — Selling entity.** The invoice header shows the selling entity chosen by OH8 for that contract (Indian entity now; a UAE or Singapore entity later, D-27 extended). The configurator states the seller before payment.

**FR-P20-74 — Payment methods by market.** International cards and bank transfer through the gateway's international acceptance or a second PSP via `BILLING_PORT` (OH8 adapter); UPI and e-mandates for India; invoices payable by wire for Enterprise. Card data never touches LDC (NN-16).

**FR-P20-75 — Cell pricing.** Hosting a legal entity in a non-IN cell (EU, GCC, SG, US — when live) is a component (ADD-CELL) because it carries extra infrastructure and transfer-compliance cost; the configurator explains why and shows it only for entities whose jurisdiction maps to that cell.

**FR-P20-76 — Display rules.** Prices show tax-exclusive with a "plus applicable taxes" note in B2B markets and tax-inclusive where local consumer rules require (e.g., B2C in the EU/UK; LDC is B2B so this is rare); currencies use locale formats (`en-IN` lakh/crore grouping toggle; Appendix Y §Y.9.3).

### 4Q. Components for the v1.1 modules, practitioner plans and auditor seats *(v1.1)*

**FR-P20-77 — New components.** The presentation catalogue adds ADD-LIT (Legal Matters, Contracts, Licences & Ethics Registers — P26), ADD-ESG (ESG, BRSR & CSR — P27), ADD-AIG (AI Governance — OV_AI), ADD-GEM (Global Entity Management — P25), ADD-GLB-<jurisdiction> (Global Pack per jurisdiction per entity, priced by pack tier A/B/C), ADD-QRY (local-expert query bundle), ADD-RPT-PRO (Reports & MIS Studio Pro — P28; basic reports included in every package), ADD-CELL (non-India data residency cell), ADD-ESC-D / ADD-ESC-S (data / source-code escrow, P19 §4N), ADD-AGT (agent seats, §4R) (Appendix N §N.16).

**FR-P20-78 — Dependencies.** ADD-GLB requires ADD-GEM for the foreign entity (or Enterprise); ADD-QRY requires an ADD-GLB pack for that jurisdiction; ADD-ESG suggests ADD-RPT-PRO; ADD-AIG includes LawDocsComply's vendor AI assurance pack import (D-38). The configurator explains each dependency inline.

**FR-P20-79 — Practitioner-firm plans.** A CS/CA/law firm (verified in P21) buys a practitioner plan (`tenant.practice_mode`, ADD-WL extended): firm workspace (P22 §4L) + per-client-entity bands; the firm may pay for clients' tenants or each client pays its own subscription (switch per client link); invoices are OH8's. NN-20 applies to how the firm is presented.

**FR-P20-80 — Auditor engagement seats (G5 TM-405).** Statutory, secretarial, IS and internal-audit firms (and PCS firms issuing certificates) get free, read-only, time-boxed seats scoped to an engagement (P10), counted outside paid seats; access is logged for the tenant; seats expire with the engagement.

**FR-P20-81 — Bundles.** New bundle seeds: *Group Pack* (GEM + 3 Global Packs + ADD-CELL where needed), *Governance+ Pack* (Board Portal + Legal Matters + Reports Pro), *Sustainability Pack* (ESG + Reports Pro), *Responsible AI Pack* (AI Governance + Data Protection advanced).

**FR-P20-82 — Standalone SKUs.** ADD-LIT-S (Legal & Contracts) and ADD-ESG-S (ESG & BRSR) are sellable standalone, like the Labour and Board Portal SKUs.

### 4R. AI credits and the agent workforce *(v1.1; Appendix AA §AA.4, §AA.14)*

**FR-P20-83 — One credit currency.** All AI usage (chat, drafting, OCR/translation, agent missions, control-monitoring runs, `ask_regulation` via MCP) consumes Vidhi credits from the tenant wallet at rates in the versioned `ai.credit_rates` table (Appendix N §N.17). Deterministic READ tools via MCP consume no credits.

**FR-P20-84 — Agent seats.** "Hiring" a role agent (Appendix AA §AA.4.2) is an agent seat (ADD-AGT) with a monthly fee that includes a credit allowance for that agent; the seat page shows the agent's sponsor, autonomy level, expected tasks and last month's accepted outputs, so the buyer sees value per agent.

**FR-P20-85 — Budgets.** Budgets per tenant, department, agent and mission (`bil.ai.budget.*`); alerts at 50/80/100%; at 100% the tenant chooses (pre-set) between pause, finish running missions only, or overage at the published rate. Statutory-deadline work in progress is never stopped by a credit limit — it degrades to deterministic flows (NN-42; master §10 deterministic fallback).

**FR-P20-86 — Top-ups.** One-click credit packs; optional auto top-up with a monthly cap; pay-as-you-go overage only if the admin opted in (no surprise charges).

**FR-P20-87 — Transparency.** Settings → Billing → AI usage shows credits by agent, skill, department and user, with cost per accepted output; exportable to folder 20.

**FR-P20-88 — Rate changes.** A change to credit rates is a commercial change (OH8 approval), announced 30 days ahead, never retroactive to bought packs.

### 4S. Transparency fixes from client feedback *(v1.1; Appendix Z §Z.9.11)*

**FR-P20-89 — Seat model (IMP-104).** Paid seats = users who perform work: admins, makers, checkers, department heads, KMP workspace users, payroll and HR admins. Free (fair-use): viewers, board and committee members, attesting employees, auditor engagement seats (FR-P20-80), supervisor-view grants, co-operative members, complainants and self-service employees. The seat counter on SCR-BIL-11 shows both counts.

**FR-P20-90 — Full-year and renewal price (IMP-105).** The configurator and checkout show monthly, annual and first-year totals and the **renewal price** (list price after any promotion ends), plus the price of each add-on on its own line.

**FR-P20-91 — Billing cycles (IMP-106).** Monthly and annual cycles both purchasable for Essentials and Professional; the annual discount is stated in percentage and rupees.

**FR-P20-92 — Renewal reminders (IMP-107).** Reminders at 60, 30 and 7 days before renewal (e-mail + in-app to admin and finance contact) with one-click "change plan", "change seats" and "download usage report".

**FR-P20-93 — Cancellation (IMP-108).** Self-serve cancellation in ≤ 3 clicks from Settings → Billing (reason picker optional, retention offer at most once and skippable); the confirmation shows the read-only window, export reminder and the date access ends (NN-42, NN-44).

**FR-P20-94 — Quarterly value report (IMP-109).** A quarterly e-mail/PDF to the admin: instances completed on time, overdue avoided, Updates processed, hours saved (method cited, NN-19), AI outputs accepted; generated from the Savings Dashboard data.

**FR-P20-95 — Support SLA by plan (IMP-110 link).** Settings → Billing → Plan shows the support SLA of the current plan and what changes on upgrade (P22 §4M).

### 4T. Unit-economics telemetry *(v1.1; G5 TM-400)*

**FR-P20-96 — Cost-to-serve meters.** Internal meters (not billed) for SMS/WhatsApp/voice pass-through, AI tokens by model and route, OCR pages, storage and egress per tenant, emitted as `CostToServeRecorded` aggregates to OH8/OH finance dashboards.

**FR-P20-97 — Margin alerts.** When a tenant's monthly cost-to-serve exceeds the guard-rail share of its revenue (Appendix N §N.13), OH finance receives an alert with the drivers; LDC never changes a customer's service automatically because of margin.


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P20-X01 — Quarterly value report.** The quarterly value report to clients (IMP-109) is a P28 scheduled report; P20 supplies the savings and usage datasets only.

**FR-P20-X02 — Entitlements for new portals and modules.** Add-on `AI Governance` (included in Enterprise), contractor portal (P13) and member portal (P16) are catalogue entitlements; prices remain OH8 data (X-02).

**FR-P20-X03 — Support SLA single source.** Support response and resolution SLAs shown on pricing and plan pages are read from the Operations Hub OH6 SLA table (the same source P22 uses); no SLA value is duplicated in LDC configuration.

---

## 5. Workflows and state machines

### 5.1 Self-serve: health check → trial → paid

```
HEALTH_CHECK_COMPLETED (P23, consented reuse)
  → SIGNUP (work e-mail + mobile OTP, DPDP notice)                       [≤ 2 min]
  → ORG_FETCH (PAN/CIN/LLPIN/GSTIN → P01 adapters; duplicate check)     [≤ 1 min]
  → SECTION_SELECTION (recommended packs/components; display price)
  → CLICKWRAP (ToS + DPA [+ RE Addendum]; hash, time, IP, identity)
  → TRIAL_ACTIVE (tenant created; TenantSelfServeCreated → OH)
      ├─ T-3, T-1 reminders
      ├─ EXTENDED (self once ≤ 7 d | LawDocs ≤ 14 d | > 14 d with checker)
      └─ CONVERT → QUOTE (OH8) → [PENDING_TENANT_APPROVAL] → ORDER → PAYMENT (Razorpay hosted)
            → SubscriptionPaymentReceived → ACTIVE (EntitlementChanged applied)
  → TRIAL_EXPIRED (read-only + export) → DELETION_NOTICE (T+retention−7) → DELETED (certificate)
      └─ CONVERT allowed until DELETED
Guards: one trial per org_id per product; no paid add-on pre-ticked; RE tenants must accept RE Addendum before first personal-data upload.
```

### 5.2 Subscription (mirror of OH8.4 with LDC trial states)

```
TRIAL → TRIAL_EXPIRED → (CONVERT) → PENDING_ACTIVATION → ACTIVE
ACTIVE → RENEWAL_DUE (T-90) → ACTIVE (renewed) | CANCELLATION_REQUESTED
ACTIVE → PAST_DUE → GRACE → RESTRICTED → TERMINATION_NOTICE → EXIT → CLOSED
ACTIVE → CANCELLATION_REQUESTED → (term end) → EXIT → CLOSED   (withdrawable until effective)
any dunning state → ACTIVE (full payment or approved plan)
EXIT: P19 exit pack, read + export for ≥ 30 days; CLOSED only after exit sign-off (OH4.6).
```

### 5.3 Plan change (upgrade / downgrade / component)

```
REQUESTED (tenant admin | RM proposal accepted by tenant admin)
  → QUOTED (OH8 quote: price, proration, GST, entitlement diff; valid 7 days)
  → [TENANT_APPROVAL if threshold]
  → ORDERED → PAID | INVOICE_LATER_ACCEPTED
  → APPLIED (PlanChanged + EntitlementChanged verified; ModuleAttached/Detached emitted)
Downgrade/removal: SCHEDULED (effective term end) → APPLIED; cancellable until effective.
Failure: payment fails → nothing changes; quote may be re-ordered while valid.
```

### 5.4 Pricing Studio change

```
DRAFT (maker) → LINTED (FR-P20-65 rules; claims-gate check for copy)
  → PREVIEWED (public page + configurator at as_of date; impacted tenants list)
  → [Presentation] CHECKER_APPROVED → SCHEDULED (effective_from) → LIVE
  → [Commercial] SUBMITTED_TO_OH8 → IN_REVIEW (OH8 legality + pricing committee) → APPROVED → CATALOGUE_PUBLISHED
        → presentation version auto-bound → LIVE
  RETURNED (reasons) → DRAFT;  WITHDRAWN by maker before approval
Rollback: publish previous version as a new version (never edit history).
```

### 5.5 Trial extension

```
REQUESTED (tenant self | dlv_lead | plt_super_admin) → reason code
  → AUTO_APPROVED (tenant once ≤ 7 d) | APPROVED (LawDocs ≤ 14 d cumulative) | CHECKER_APPROVED (> 14 d cumulative)
  → APPLIED (trial_end_at updated as a new trial_period row; tenant notice; audit event TrialExtended)
```

### 5.6 Savings computation (nightly job + on demand)

```
COLLECT (P04 completions, P11 returns, timestamps, late-fee fields, tenant inputs)
  → CLASSIFY per methodology (Recorded | Modelled | Estimated)
  → VALIDATE (penalty rule last_verified_at ≤ 180 d; baselines present; inputs dated)
  → COMPUTE (deterministic, decimal; methodology_version, penalty_rule_versions stored — NN-22)
  → PUBLISH snapshot (bil.savings_snapshots, hash) → dashboard + report
Excluded items listed with reasons ("GST late-fee rule awaiting re-verification").
```

---

## 6. Screens and UX

### 6.1 Public (`apps/public`)

| Screen ID | Name | Path | Notes |
|---|---|---|---|
| SCR-BIL-01 | Pricing page | `/pricing` | Segment switcher, cycle toggle, 3 package cards, comparison, add-ons, services strip, FAQs, trust strip; server-rendered |
| SCR-BIL-02 | Configurator | `/pricing/build` (also embedded) | 7 steps, sticky summary/bottom sheet, dependency prompts, promo field, save/share/PDF |
| SCR-BIL-03 | Saved configuration | `/pricing/c/{token}` | Read-only view, "Make a copy", "Request a quote", "Start trial with this plan" |
| SCR-BIL-04 | Compare packages (full) | `/pricing/compare` | Printable; "show differences only"; anchor per row |
| SCR-BIL-05 | Add-on detail | `/pricing/add-ons/{slug}` | What it does, who needs it (by entity type), regulations it supports, price, dependencies, screenshots, tutorial link |
| SCR-BIL-06 | Start trial | `/start` | Sign-up, OTP, consent |
| SCR-BIL-07 | Organisation fetch | `/start/organisation` | PAN/CIN/LLPIN/GSTIN entry; fetched data preview with "This is correct / Edit" |
| SCR-BIL-08 | Choose sections | `/start/sections` | Regulator packs + components with prices; recommended reasons |
| SCR-BIL-09 | Terms acceptance | `/start/terms` | ToS, DPA, RE Addendum (if regulated), summaries in plain language, full text, download; checkbox per document (unticked) |
| SCR-BIL-10 | Checkout return | `/billing/checkout/return` | Pending/confirmed/failed states; never trusts redirect |

### 6.2 Tenant app — Settings › Billing & Membership (`apps/web`; `ten_admin`, read for `ten_cco`/CFO)

| Screen ID | Page | Key content and actions |
|---|---|---|
| SCR-BIL-11 | Overview | Package, status chip, term, renewal date, auto-renew toggle, next invoice estimate, payment method, quick actions (Upgrade, Add component, Add users, Buy AI credits, Download latest invoice), entitlement health |
| SCR-BIL-12 | Plan & components | All components with state (Included / Active add-on / Available / Scheduled removal), price, dependencies; Add/Remove with quote preview; standalone products owned |
| SCR-BIL-13 | Usage & limits | Users, entities, storage, AI credits, API calls, pass-through counts vs allowance; trend; statement versions; Dispute (7-day window) |
| SCR-BIL-14 | Users & seats | Seat count, active/inactive users, last activity, deactivate/reassign helper, seat purchase |
| SCR-BIL-15 | Legal entities | Entities covered, add entity (quote), group structure link (P01) |
| SCR-BIL-16 | Vidhi AI credits | Wallet balance, included vs purchased, expiry, consumption by module/user (tenant-only detail), caps per user, buy pack |
| SCR-BIL-17 | Invoices & documents | Invoices, credit/debit notes, receipts, statements; filters; PDF/ZIP/XLSX; hash; "Raise billing query" |
| SCR-BIL-18 | Payments & mandates | Payment history, saved methods (Razorpay tokens: last 4, issuer), mandates (status, max amount, frequency), cancel mandate, update method (redirect to Razorpay) |
| SCR-BIL-19 | Billing profile | Legal name, GSTINs by State, place of supply, addresses, PAN, PO settings, billing contacts, e-invoice e-mail, SEZ/IFSC & LUT, TDS declaration |
| SCR-BIL-20 | Tax documents | TDS certificates upload/status by quarter; LUT copies; GST registration certificates |
| SCR-BIL-21 | Promotions & credits | Applied coupons with expiry, service credits (SLA), referral credits, enter promo code |
| SCR-BIL-22 | Renewals & notices | Renewal timeline, price-change notices, contract documents (MSA, DPA, RE Addendum, order forms), signed copies |
| SCR-BIL-23 | Purchase approvals | Tenant approval threshold, approvers, pending approvals (FR-P20-32) |
| SCR-BIL-24 | Marketplace orders & retainers | P21 engagements and retainers bought by the tenant, SLA status, invoices from LawDocs and (direct-model) provider invoices stored |
| SCR-BIL-25 | Cancel & exit | Cancel subscription, turn off auto-renew, exit pack status (P19), download all data, data retention after exit |
| SCR-BIL-26 | Billing history (audit) | Every commercial event: quotes, orders, overrides by LawDocs (with reason), trial extensions, plan changes; Correction Entries shown with original |
| SCR-BIL-27 | Savings & Value | Tiles by evidence level, methodology panels, inputs (baselines, hourly cost bands, replaced-tool costs, pre-LDC late-fee history), period selector, export Value Report |
| SCR-BIL-28 | Notification preferences (billing) | Recipients per notification type; mandatory types marked |

In-product upsell surfaces (non-intrusive): a locked module in navigation shows "Not in your plan — see what it does" (opens SCR-BIL-05 inside the app with "Ask your admin" for non-admins → `addon.request` notification to admins); never modal interruptions during a compliance task.

### 6.3 Platform console (`apps/console`, `plt_super_admin`, `plt_finance`)

| Screen ID | Name | Notes |
|---|---|---|
| SCR-BIL-40 | Pricing Studio home | Live version, drafts, scheduled versions, pending OH8 requests, lint status |
| SCR-BIL-41 | Package & component editor | Fields, SKU binding, included/add-on matrix, limits, explainers, media |
| SCR-BIL-42 | Feature rows & comparison editor | Drag-and-drop ordering, groups, per-package values, claims-register link |
| SCR-BIL-43 | Configurator rules editor | Requires/includes/excludes/min-package/bundles with a rule tester ("simulate a configuration") |
| SCR-BIL-44 | Promotions | Draft coupons → OH8; redemption analytics (aggregate) |
| SCR-BIL-45 | Trial policies | Trial plan, caps, default days, retention, reminder schedule |
| SCR-BIL-46 | Preview & publish | Side-by-side live vs draft, segment and date picker, diff, impacted tenants (for limit changes), approve/publish |
| SCR-BIL-47 | Tenant commercial panel | For one tenant: subscription, entitlements (published vs applied), trial periods, overrides history, extend trial, propose order, open OH8 record |
| SCR-BIL-48 | Stream switches | RS-LDC list with OH8 gate status, LDC switch by market/segment/channel, kill switch, change log |
| SCR-BIL-49 | Reconciliation | Entitlement breaks, usage statements, disputes, webhook/event lag |
| SCR-BIL-50 | Savings methodology registry | Baselines, activity catalogue, penalty-rule bindings, versions, verification dates |

UX rules: every price shown with its basis ("per month, billed annually, excl. GST"); keyboard navigation through configurator steps (`←/→`), `Enter` toggles a component card, `?` opens shortcuts; "i" help keys `help.billing.*` (Appendix C); empty states ("No invoices yet — your first invoice will appear after your trial converts").

**Screens added in v1.1** *(v1.1)*

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-BIL-60 | Market and currency selector | Public pricing page header; checkout | Market hint, explicit selector, seller entity shown |
| SCR-BIL-61 | Tax details and preview | Checkout → Billing details | Tax IDs, validation result, OH8 tax treatment preview |
| SCR-BIL-62 | AI usage and budgets | Settings → Billing → AI usage | Credits by agent/skill/department, budgets, top-ups |
| SCR-BIL-63 | Agent seats | Settings → Billing → Agent seats | Hired agents, sponsors, allowance, value per agent |
| SCR-BIL-64 | Cancel subscription | Settings → Billing → Plan → Cancel | ≤ 3 clicks, read-only window, export reminder |
| SCR-BIL-65 | Auditor engagement seats | Settings → Users → Auditor seats | Free seats, engagement, expiry, access log |
| SCR-BIL-66 | Withholding tax documents | Settings → Billing → Tax documents | TRC download, WHT certificate upload |

---

## 7. Backend design

### 7.1 Modules touched
`bil` (owner), `cfg` (settings), `core` (audit, Correction Entries, tenant lifecycle), `iam` (signup, step-up), `int` (event inbox/outbox, JWS), `dms` (billing document filing), `rpt` (savings widgets), `web` (public pages), `wf` (notifications, tenant approvals), `xpt` (exit), `ai` (credit consumption hooks).

### 7.2 Tables (key columns; all tenant tables RLS, NN-01)

| Table | Key columns |
|---|---|
| `bil.presentation_versions` | id, version, status (DRAFT, IN_REVIEW, SCHEDULED, LIVE, SUPERSEDED), catalogue_version_ref (OH8), effective_from, content_hash, maker, checker, published_at |
| `bil.packages` | id, presentation_version_id, code (ESSENTIALS, PROFESSIONAL, ENTERPRISE), sku_ref, display_name, tagline, badge_code, badge_basis_ref, sort, segment_overrides jsonb |
| `bil.components` | id, presentation_version_id, code (`ADD-*`), sku_ref, module_keys[], area, name, value_line, explainer_key, availability per package jsonb, standalone bool |
| `bil.feature_rows` | id, presentation_version_id, group_code, label, explainer_key, values per package jsonb, claim_ref, anchor, sort |
| `bil.configurator_rules` | id, presentation_version_id, type (REQUIRES, INCLUDES, EXCLUDES, MIN_PACKAGE, BUNDLE, RECOMMENDED_FOR), subject, object, params jsonb, message_key |
| `bil.price_history` | sku_ref, market, price_book_version, price_minor, currency, valid_from, valid_to (for prior-price rule) |
| `bil.saved_configurations` | token_hash, payload jsonb (no PII), segment, created_at, expires_at, converted_quote_ref |
| `bil.catalogue_cache` | catalogue_version, jws, verified_at, content jsonb |
| `bil.trial_periods` | tenant_id, period_no, start_at, end_at, reason_code, granted_by, approved_by, origin (DEFAULT, SELF, LAWDOCS) |
| `bil.subscriptions_mirror` | tenant_id, oh_subscription_id, state, package_code, term, renewal_at, auto_renew, last_event_at |
| `bil.entitlements_applied` | tenant_id, entitlement_id, version, jws, modules[], limits jsonb, valid_from, valid_to, applied_at |
| `bil.usage_meters` | tenant_id, legal_entity_id, meter, period, quantity, statement_version, statement_hash, state (PROVISIONAL, FINAL, DISPUTED) |
| `bil.ai_credit_ledger` | tenant_id, entry_type (GRANT, PURCHASE, CONSUME, EXPIRE, ADJUST), credits, module, user_id (tenant-internal only), ref, at — append-only |
| `bil.billing_profiles` | tenant_id, legal_name, gstins jsonb, pos_state, addresses, pan_token, po_required, contacts jsonb, sez_ifsc jsonb, tds_declared |
| `bil.documents_index` | tenant_id, oh_doc_id, type, number, date, amount_minor, gst_minor, irn, hash, dms_file_id |
| `bil.tenant_purchase_approvals` | tenant_id, quote_ref, requested_by, approver_id, state, decided_at |
| `bil.stream_gates` | stream_code, oh_state, ldc_switch jsonb (market × segment × channel), high_impact bool, updated_by, updated_at |
| `bil.commercial_overrides` | tenant_id, type, params, reason_code, maker, checker, oh_ref, effective_from, superseded_by |
| `bil.savings_methodologies` | id, version, activity_code, baseline_minutes, source, editable_by_tenant, valid_from |
| `bil.savings_inputs` | tenant_id, input_type (HOURLY_COST_BAND, BASELINE_OVERRIDE, PRE_LDC_LATE_FEES, REPLACED_TOOL_COST, PRE_LDC_LATE_RATE), value, evidence_file_id, entered_by, valid_from |
| `bil.savings_snapshots` | tenant_id, period, metrics jsonb, methodology_version, penalty_rule_versions jsonb, excluded jsonb, hash, computed_at |
| `bil_local.*` | Only with `LOCAL` adapter: skus, price_books, coupons, quotes, orders, subscriptions, invoices, credit_notes, receipts, mandates, dunning_cases (schema mirrors OH8.1) |

### 7.3 APIs (tenant and public; versioned `/v1`)

| Method & path | Purpose |
|---|---|
| `GET /v1/public/pricing?segment=&as_of=` | Presentation + display prices (cached; no auth) |
| `POST /v1/public/configurations` / `GET /v1/public/configurations/{token}` | Save/load configuration |
| `POST /v1/public/configurations/{token}/quote` | Convert to OH8 quote (requires e-mail verification) |
| `POST /v1/signup`, `POST /v1/signup/verify`, `POST /v1/signup/organisation`, `POST /v1/signup/sections`, `POST /v1/signup/accept-terms` | Self-serve flow (P01 owns identity parts) |
| `GET /v1/billing/overview` | Tenant billing overview |
| `POST /v1/billing/quotes` | Proxy to OH8 via BILLING_PORT (tenant scope enforced) |
| `POST /v1/billing/orders` | Proxy to OH8; returns hosted URL |
| `GET /v1/billing/orders/{id}/status` | Server-side confirmation poll |
| `GET /v1/billing/invoices`, `GET /v1/billing/documents/{id}` | Documents (stream from OH8, cache in DMS) |
| `POST /v1/billing/usage-disputes` | Proxy |
| `GET /v1/billing/usage` | Meters and statements |
| `GET/PUT /v1/billing/profile` | Billing profile |
| `POST /v1/billing/tds-certificates` | Upload |
| `POST /v1/billing/trial/extend-self` | One-time self extension |
| `POST /v1/billing/cancel`, `POST /v1/billing/cancel/withdraw`, `PUT /v1/billing/auto-renew` | Lifecycle |
| `POST /v1/billing/addon-requests` | Non-admin requests |
| `GET /v1/entitlements/self` | Current user's view |
| `GET /v1/savings?period=`, `PUT /v1/savings/inputs`, `POST /v1/savings/report` | Savings |
| Console: `/v1/console/pricing/*`, `/v1/console/tenants/{id}/commercial/*`, `/v1/console/streams/*`, `/v1/console/reconciliation/*` | Studio, overrides, switches, reconciliation |
| Machine (from OH8, mTLS + signed CloudEvents): inbox for `PlanChanged`, `EntitlementChanged`, `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`, `SubscriptionCancelled`, `CatalogueVersionPublished`, `CatalogueChangeRequestUpdated`, `StreamGateChanged` | Event intake |

### 7.4 Domain events (LDC-produced; `in.lawdocscomply.bil.*.v1` unless an Ecosystem name exists)

`TenantSelfServeCreated` (→ OH; new, Appendix X), `TrialStarted`, `TrialExtended`, `TrialExpired`, `TrialConverted`, `ConfigurationSaved` (no PII), `QuoteRequested`, `TenantPurchaseApprovalDecided`, `ModuleAttached` / `ModuleDetached` (Ecosystem names → OH8), `UsageRecorded` (Ecosystem name → OH8), `EntitlementApplied`, `ReconciliationBreakRaised` (Ecosystem name), `StreamSwitchChanged`, `PresentationVersionPublished`, `CommercialOverrideApplied`, `SavingsSnapshotPublished`, `AddonRequested`, `CancellationRequested`, `CancellationWithdrawn`.

### 7.5 Jobs / Temporal workflows

`TrialLifecycleWorkflow` (per tenant: reminders, expiry, deletion notice, deletion hand-off to P19); `CheckoutConfirmationWorkflow` (poll order status, timeouts, `plt_finance` task); `EntitlementReconciliationJob` (05:30–06:00 IST daily); `UsageStatementJob` (daily provisional, monthly final WD+3); `CatalogueSyncJob` (on event + daily); `PriceHistoryJob` (prior-price maintenance); `SavingsSnapshotJob` (nightly 02:00 IST + on demand); `RenewalReminderWorkflow`; `StreamCacheInvalidation` (≤ 5 min SLA); `LocalToOH8MigrationWorkflow` (only if LOCAL used).

---

## 8. Integrations (ports and adapters)

| Port | Adapter(s) | Notes |
|---|---|---|
| `BILLING_PORT` | `OH8` (default), `LOCAL` (interim), `MOCK` | Ecosystem Spec §6.27; Appendix X §X.8 new APIs `POST /v1/catalogue/change-requests`, `GET /v1/catalogue/change-requests/{id}`, `POST /v1/trials/extensions` (sync), `TenantSelfServeCreated` |
| `CRM_PORT` | OH3 `POST /v1/crm/requests` | "Talk to sales", enterprise quote requests, lost-trial reasons (with consent) |
| `PROVISIONING_PORT` | OH4 | `TenantSelfServeCreated` (LDC → OH); `TenantProvisioned` (OH → LDC) for sales-led tenants; `PUT /v1/provisioning-requests/{id}` |
| `CLAIMS_GATE_PORT` | OH14 `GET /v1/claims-gate/check` | Pricing copy, badges, savings marketing |
| `ORG_LOOKUP_PORT` | P01 adapters (MCA/PAN/GSTIN providers) | Organisation fetch |
| `PAYMENT` | Razorpay (via OH8; via LDC only in LOCAL) | Hosted checkout/Payment Links/Subscriptions/eNACH/Smart Collect; webhooks verified in OH8 |
| `NOTIFY_PORT` | P04 notification service; e-mail (SES/M365), SMS/WhatsApp via DLT templates | Billing notifications |
| `DMS_PORT` | P07 | Filing invoices and contracts |

---

## 9. Settings and configuration (registered in P02; Appendix U)

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `bil.billing_port.mode` | G | `OH8` | OH8, LOCAL_INTERIM, MOCK (non-prod) | Owner decision + `plt_super_admin` + checker |
| `bil.trial.default_days` | G | 7 | 1–60 | `plt_super_admin` + checker |
| `bil.trial.self_extension_days` | G | 7 | 0–7 | `plt_super_admin` |
| `bil.trial.lawdocs_extension_max_without_checker` | G | 14 | 0–30 | `plt_super_admin` + checker |
| `bil.trial.retention_days` | G | 30 | 15–90 | `plt_super_admin` + DPO |
| `bil.trial.plan_code` | G | `TRIAL_PRO` | catalogue trial policies | Pricing Studio |
| `bil.trial.ai_credit_cap` | G | 200 | 0–2,000 | Pricing Studio |
| `bil.trial.reminder_offsets_days` | G | [3, 1] | each 1–14 | Pricing Studio |
| `bil.exit.read_only_days` | G | 30 | floor 30, max 180 | `plt_super_admin` + checker |
| `bil.configurator.saved_config_ttl_days` | G | 30 | 7–180 | Pricing Studio |
| `bil.pricing.show_gst_inclusive_total` | L | true | — | — (always shown before payment) |
| `bil.pricing.prior_price_window_days` | L | 30 | — | — |
| `bil.stream.<code>.enabled` | G | per Appendix N §N.6 | narrow-only vs OH8 | `plt_super_admin` (+ checker if high impact) |
| `bil.tenant.purchase_approval_threshold` | T | off | ₹0–₹1 crore | `ten_admin` |
| `bil.tenant.purchase_approvers` | T | [] | tenant users with `billing.approve_purchase` | `ten_admin` |
| `bil.tenant.po_required` | T | false | — | `ten_admin` |
| `bil.tenant.overage_opt_in` | T | false | — | `ten_admin` |
| `bil.tenant.billing_contacts` | T | admin | 1–10 | `ten_admin` |
| `bil.ai.rollover` | G | false | — | Pricing Studio |
| `bil.ai.user_cap_credits` | T | none | 0–tenant balance | `ten_admin` |
| `bil.limits.soft_threshold_pct` | G | 80 | 50–95 | `plt_super_admin` |
| `bil.savings.enabled` | T | true | — | `ten_admin` |
| `bil.savings.show_estimated` | T | true | — | `ten_admin` |
| `bil.savings.share_with_rm` | T | on if retainer else off | — | `ten_admin` |
| `bil.savings.penalty_rule_max_age_days` | G | 180 | 30–365 | `plt_content_checker` |
| `bil.savings.marketing_min_tenants` | L | 20 | — | — |
| `bil.badge.most_chosen.window_days` | G | 90 | 30–365 | Pricing Studio |
| `bil.never_block_list` | L | FR-P20-43 | — | — |

**Settings added in v1.1** *(v1.1)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `bil.market.default` | G | IN | IN, AE, SG, GB, EU, US | `plt_finance` + checker |
| `bil.market.selector.enabled` | G | true | — | `plt_finance` |
| `bil.ai.budget.tenant_monthly` | T | plan allowance | 0–unlimited | `ten_admin` |
| `bil.ai.budget.department.<code>` | T | none | — | `ten_admin` |
| `bil.ai.at_limit_behaviour` | T | `PAUSE_NEW` | PAUSE_NEW, FINISH_RUNNING, OVERAGE | `ten_admin` |
| `bil.ai.auto_topup.cap` | T | 0 (off) | 0–plan cap | `ten_admin` |
| `bil.renewal.reminder_days` | G | 60, 30, 7 | ≥ 7 | `plt_finance` |
| `bil.cancel.retention_offer.enabled` | G | true (once, skippable) | — | `plt_finance` |
| `bil.seats.free_roles` | G | viewer, board, attester, auditor engagement, supervisor, co-op member, complainant, self-service | — | `plt_finance` + checker |
| `bil.cost_to_serve.alert_share` | G | per Appendix N §N.13 | — | `plt_finance` |

---

## 10. Security, privacy and audit

- **PCI DSS SAQ A** scope: LDC pages launch checkout only by top-level redirect to Razorpay-hosted pages; no Razorpay JS on LDC origins (CSP `script-src` allow-list excludes payment scripts); script inventory and integrity monitoring on `/pricing/*`, `/start/*`, `/settings/billing/*` (PCI DSS v4.0.1 req. 6.4.3 and 11.6.1 apply to SAQ A merchants per the revised SAQ A of 31 Jan 2025 [VERIFY]); no card data stored, processed or logged (Appendix Q).
- **No secrets in LDC** for OH8 mode; LOCAL mode keeps Razorpay keys in the LDC vault with 90-day rotation and dual-secret webhook verification (raw body HMAC-SHA256, constant-time compare, event-id de-duplication).
- **DPDP**: sign-up notice; marketing consent separate and unticked; saved configurations hold no PII unless e-mailed; savings inputs are tenant data (NN-24 India residency); usage aggregates to OH8 carry no personal identifiers (contract test rejects `user_id`, `email`, `pan`, `aadhaar` patterns).
- **Audit ledger** (NN-02): every price/presentation publish, override, trial extension, stream switch, plan change, cancellation and savings-input change; Correction Entries for any fix (D-02); tenant-visible commercial history (SCR-BIL-26).
- **Maker-checker** (NN-05) for every Governed change; super admin cannot approve own drafts; step-up MFA for publish, overrides, kill switch.
- **Dark-pattern controls** (OH8.9; CCPA Dark Patterns Guidelines 2023; E-Commerce (Amendment) Rules 2026 r.4(15) annual self-audit adopted as policy): CI lint for countdown timers, pre-ticked paid boxes, confirm-shaming copy, hidden costs; the annual self-audit report stored as evidence in Appendix Q control library.
- **Abuse controls**: rate limits on configuration save and quote endpoints; CAPTCHA-free bot mitigation (privacy-preserving challenge only on anomaly; WCAG-compliant alternative — NN-21); trial abuse detection (same PAN/CIN/GSTIN, same device fingerprint hashed, disposable e-mail).
- **Confidentiality**: LDC usage and savings data never reach OH sales teams beyond aggregates allowed in Appendix X §X.5; LDC's knowledge of a client's compliance weaknesses is never used to sell other group products (OH Part 4.5).

---

## 11. AI touchpoints and guardrails

- **Plan advisor** (Vidhi, public and in-app): answers "Which plan do I need?" from the presentation catalogue and the entity type; cites feature rows; never invents prices — any price it states is rendered by the configurator component, not generated text; hands off to the configurator with a pre-filled configuration the user must confirm (NN-14).
- **Savings narrative**: drafts the Value Report commentary from the snapshot; every number in the text is bound to a metric id; human review before the report is shared outside the tenant (NN-04).
- **Pricing Studio assistant**: suggests explainer copy and FAQ answers; claims-gate check before submit; never auto-publishes.
- AI credit consumption itself is metered (FR-P20-49); AI features degrade gracefully when credits are exhausted.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p20/*.feature`)

```gherkin
Feature: Transparent pricing and configurator
  Scenario: Running total updates with dependencies
    Given the live presentation version has Risk Assessment Lab requiring Enterprise Risk Management
    When a visitor on Professional toggles "Risk Assessment Lab"
    Then an inline prompt offers to add "Enterprise Risk Management" with its price delta
    And the summary shows both lines and an updated estimated total within 150 ms
    And no paid component is selected without the visitor's click

  Scenario: Prior price rule
    Given SKU ADD-RET had prices 8000, 7000 and 7500 in the last 30 days
    When a promotion shows ADD-RET at 6000
    Then the struck-through prior price shown is 7000

  Scenario: GST-inclusive total before payment
    Given a configuration with an annual total of 3,60,000 excl. GST
    When the visitor reaches Review and requests a quote
    Then the OH8 quote's GST and grand total are displayed before the "Pay" button is enabled

Feature: Self-serve trial
  Scenario: Health check to trial in under 12 clicks
    Given a completed health check for a "NBFC - Base Layer" with consent to reuse
    When the visitor starts a trial, verifies OTP, enters a valid CIN and accepts the terms
    Then a trial tenant is created with the RBI NBFC pack and the recommended components
    And TenantSelfServeCreated is emitted once
    And the click count recorded by the test harness is at most 12

  Scenario: One trial per organisation
    Given an organisation with an existing LDC tenant
    When another user tries to start a trial with the same CIN
    Then the trial is refused with LDC-BIL-011 and an access-request option is shown

  Scenario: Trial never converts automatically
    Given a trial ending today with no order placed
    When the trial end time passes
    Then the tenant becomes TRIAL_EXPIRED, read-only with export available
    And no payment, mandate or invoice is created

  Scenario: Trial extension beyond 14 days needs a checker
    Given a tenant whose trial was already extended by 14 days by LawDocs
    When a super admin requests a further 7-day extension
    Then the extension stays pending until a different super admin approves it
    And the tenant sees the extension notice only after approval

Feature: Entitlements and dunning
  Scenario: Restricted subscription keeps statutory work running
    Given a tenant in RESTRICTED with a return package in preparation due in 10 days
    When a maker submits the return package for checking
    Then the submission succeeds
    And exports and auditor access remain available
    And inviting a new user is refused with LDC-BIL-020

  Scenario: Entitlement mismatch never downgrades
    Given OH8 reports an entitlement without ADD-AUD while LDC has it applied
    When the daily reconciliation runs
    Then ReconciliationBreakRaised is emitted and a plt_finance task is opened
    And the tenant keeps Audit Management until the break is resolved

  Scenario: Browser redirect is not proof of payment
    Given a checkout returning with status=success in the URL but no SubscriptionPaymentReceived
    Then the order stays pending and the tenant is told payment is being confirmed

Feature: Pricing Studio
  Scenario: Certification claim without evidence cannot publish
    Given a draft feature row "ISO 27001 certified platform" with no claims-register reference
    When the maker submits for review
    Then lint error LDC-BIL-033 blocks submission

  Scenario: Price change goes to OH8
    Given a maker edits the Essentials monthly price
    When the change is submitted
    Then a catalogue change request is created in OH8 and the studio shows IN_REVIEW
    And the public page keeps the old price until OH8 publishes the catalogue version

  Scenario: Kill switch hides a stream in five minutes
    Given RS-LDC-07 "AI credit packs" is ACTIVE
    When a super admin turns its LDC switch off with a checker
    Then the "Buy AI credits" action disappears from all surfaces within 5 minutes
    And existing credit balances remain usable

Feature: Savings dashboard
  Scenario: ROI excludes modelled exposure
    Given hours saved of 120, hourly cost band 1,500 and modelled penalty exposure of 2,00,000
    When the Return on subscription tile is computed
    Then it uses 1,80,000 and excludes the 2,00,000 modelled exposure
    And the modelled exposure tile is labelled "Modelled"

  Scenario: Stale penalty rule is excluded
    Given the GST late-fee rule was last verified 200 days ago
    When the savings snapshot runs
    Then GST late-fee exposure is excluded and listed with the reason
```

NN tests: `NN-01_billing_rls`, `NN-02_override_audit`, `NN-05_pricing_maker_checker`, `NN-16_saq_a_no_payment_script`, `NN-19_claims_gate_pricing`, `NN-21_pricing_wcag`, `NN-22_savings_reproducible`, `NN-27_billing_notifications_not_updates`, `NN-29_entitlement_never_blocks`, `NN-32_no_pii_in_usage_aggregate`.

```gherkin
Feature: v1.1 — cross-border commerce, agent credits and transparency

  Scenario: Foreign customer sees the right currency and tax treatment
    Given a visitor from the UAE selects Professional with the AI Governance add-on
    When they enter a valid UAE TRN at checkout
    Then prices show from the AED price book and the OH8 preview states the applicable VAT treatment
    And no price was produced by FX conversion in LDC

  Scenario: Statutory work survives an exhausted AI budget
    Given tenant T's AI budget is exhausted and at-limit behaviour is PAUSE_NEW
    When a maker opens a checkpoint due today
    Then submission, evidence upload and approval work without AI and the AI panel explains the limit

  Scenario: Board members do not consume paid seats
    Given 12 board members and 3 auditors are added to tenant T
    Then the paid seat count does not change

  Scenario: Renewal price is visible before payment
    Given a 20% first-year promotion applies
    When the buyer reaches checkout
    Then the first-year total and the renewal price are both shown

  Scenario: Cancellation in three clicks
    When the admin opens Settings → Billing → Plan and cancels
    Then cancellation completes in at most three clicks and the read-only end date and export reminder are shown

  Scenario: Auditor engagement seats expire with the engagement
    Given an IS audit engagement ends on 31 March
    Then the auditor seat is disabled on 1 April and the access log remains visible to the tenant
```

---

## 13. Deliverables and exit gate

- Presentation catalogue schema, Pricing Studio, public pricing page, configurator (public + embedded), self-serve trial flow, Billing & Membership settings (SCR-BIL-11…28), entitlement SDK adopted by all modules built so far, usage meters, Savings Dashboard and Value Report, stream switches, `BILLING_PORT` with OH8 adapter contract-tested (or LOCAL adapter approved, OI-P20-01).
- Seed data: Appendix N catalogue, feature rows, FAQs, savings methodology registry (baselines marked `[OWNER TO SET]` until the time-and-motion study is done).
- Evidence: SAQ A scope note, dark-pattern self-audit v1, claims-gate PASS for all public copy, accessibility report, load test (pricing page p95 TTFB ≤ 300 ms at 200 rps), reconciliation dry run with OH8 sandbox.
- **Exit gate:** all §12 scenarios and NN tests green; owner sign-off on seeded prices (Appendix N `[OWNER TO SET]` resolved) and refund policy; legal sign-off on ToS, DPA, RE Addendum and click-wrap design (OI-P20-03); tax sign-off on SAC per SKU (OH8 tax review).

---

## 14. Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P20-01 | Is OH8 live when P20 ships? Approve `LOCAL` adapter with an LDC Razorpay account? | OH v1.0 build sequence unknown | Owner / CTO | `bil.billing_port.mode = OH8`; P20 exit blocked until decided |
| OI-P20-02 | Production-grade trial tenants with client data (deviation from OH8.9 sandbox-only trials) | Needs OH addendum acceptance (Appendix X §X.3) | Owner / OH product head | If rejected: trial on sandbox with synthetic sample data; conversion migrates nothing |
| OI-P20-03 | Click-wrap ToS/DPA/RE Addendum adequacy for RBI REs (IT outsourcing directions require board-approved policy and contract terms) | RE may insist on signed MSA | Legal counsel | Offer eSign MSA path (D-20) for REs before conversion |
| OI-P20-04 | GST rate/SAC per SKU, IFSC/SEZ zero-rating, TDS form numbers under Income-tax Act 2025 | Tax review | CA / tax counsel | Display "GST as applicable"; OH8 computes |
| OI-P20-05 | E-Commerce (Amendment) Rules 2026 applicability to B2B SaaS pricing pages | Consumer definition | Counsel | Policy adoption anyway (prior price, dark-pattern audit) |
| OI-P20-06 | Seed prices for packages/components | Owner decision | Owner / CFO | `[OWNER TO SET]`; publish blocked |
| OI-P20-07 | Time-and-motion baselines for hours-saved | Not yet measured | Owner / CS | Estimated tiles hidden until baselines set |
| OI-P20-08 | Razorpay plan-change on domestic-card subscriptions (only offer updatable) | Vendor constraint | OH8 team | Invoice prorated difference + recreate subscription at cycle |
| OI-P20-09 | e-mandate no-AFA limit and exemptions as of Oct 2026 | Rule changes | OH8 team | Use OH8.7 values |
| OI-P20-10 | Rename "Nidhi AI Assistant" on live pricing page to "Vidhi AI" | Brand consistency | Owner / marketing | Copy updated in Appendix P |

**Open items added in v1.1** *(v1.1)*

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P20-21 | Foreign price books and cell surcharges | Owner pricing decision | Owner / CFO | Market selector shows India only |
| OI-P20-22 | Cross-border tax positions (export of services/LUT, EU/UK reverse charge, UAE/Saudi/Singapore registration) | Tax adviser | CFO | Foreign checkout OFF; Enterprise by quote |
| OI-P20-23 | Agent seat pricing and credit rates for missions/CCM | Needs cost data from P17 pilots | Owner / CTO | Agents billed only through credits |
| OI-P20-24 | Escrow agent and fees | Commercial | Owner | Escrow not sold |

---

## 15. Sources (accessed 25 October 2026)

1. Infrabyx Ecosystem Integration Specification v1.1, §6.27 (billing) and §6.29 (ops) — owner's corpus.
2. Infrabyx Operations Hub Master Prompt v1.0, OH4, OH5, OH8 (OH8.1–OH8.11), OH9, OH14.6 — owner's corpus.
3. LawDocsComply live pricing page, https://www.lawdocscomply.com/pricing (observed 25 Oct 2026).
4. Razorpay, "Update a Subscription", https://razorpay.com/docs/payments/subscriptions/update ; Razorpay Route, https://razorpay.com/docs/payments/route/
5. Department of Consumer Affairs, Consumer Protection (E-Commerce) (Amendment) Rules 2026 (notified 9 Sep 2026, effective 1 Jan 2027) — summary https://www.mondaq.com/overview-of-the-consumer-protection-(e-commerce)-(amendment)-rules-2026/1846008 [VERIFY gazette].
6. CCPA, Guidelines for Prevention and Regulation of Dark Patterns, 2023 (30 Nov 2023).
7. CGST Act 2017 ss.31, 34, 36, 50, 52; CGST Rules r.46, r.48(4); IGST Act ss.12, 13, 16; Notification 10/2023-Central Tax (e-invoicing ₹5 crore).
8. PCI SSC, PCI DSS v4.0.1 and SAQ A (revised 31 Jan 2025) [VERIFY].
9. Companies Act 2013 s.403; Companies (Registration Offices and Fees) Rules 2014; SEBI Master Circular SEBI/HO/CFD/PoD2/CIR/P/0155 (11 Nov 2024) — penalty library seeds (Appendix N §N.9).
10. Vanta pricing observations, https://soc2auditors.org/insights/vanta-pricing/ (benchmark only).

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-42, NN-44; X-02 (OH8 is the billing system of record; `bil` scope per master §5.3), X-15, X-18; open owner decisions D-26, D-27, D-28.

**Added in v1.1:** D-42; X-59.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
