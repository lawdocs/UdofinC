# Phase P17 — Plans, Subscriptions, Billing, GST, Revenue-Stream Switches and Savings Dashboard

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P02 (tenancy, Personal/Company workspaces, maker-checker), P03 (settings registry, Configuration Studio, rules), P19 core (`int` gateway, OH8 adapter, signed-artefact verification), P20 core (`xpt.export_map`), P21 core (public-site shell for `/pricing`); P01 for sign-up and GST/PAN profile fetch. External: Operations Hub **OH8** (catalogue, price books, coupons, stream gates, quotes, orders, subscriptions, signed entitlements, GST invoices, credit notes, receipts, Razorpay hosted checkout, Subscriptions, e-mandates, Smart Collect, Route, dunning, revenue accounting — Ecosystem Spec §6.27; OH Master Prompt OH8.1–OH8.10), **OH14** (claims gate), **OH3** (consented leads), **OH6** (billing disputes).
> **Sequencing:** Wave 1. Sprints 1–3 build `BILLING_PORT`, the presentation catalogue, entitlement mirror and checkout (frozen at end of sprint 3 for P16). Sprints 4–5: credits, meters, Settings → Billing & Membership, dunning. Sprints 6–7: revenue-stream registry UI, Pricing Studio, Savings & Value. If OH8 is not live at sprint 3, the interim `LOCAL` adapter (§4L) ships behind an owner decision (OI-P17-01). Every producing module (sgn, ai, lit, ipm, dms, ntf, int, mkp) registers its meters by its own phase exit.
> **Binding appendices:** L (Pricing, Plans, Revenue-Stream Registry and Savings Model), M (marketplace fees, for buyer-fee lines), K (`LD-EXPORT-1.0`), R (settings), W (open items), X (Operations Hub additions — new stream types and meters), Y (Ecosystem Spec v1.2 change request — LawDocs as `UsageRecorded` producer).
> **Requirements covered:** R-017, R-019, R-021, R-027, R-030, R-033, R-034, R-035, R-036, R-040, R-042, R-049, R-054, R-063.
> **Decisions applied:** D-02, D-05, D-08, D-11, D-13 · **Challenges applied:** CH-08, CH-19, CH-21, CH-25 · **Non-negotiables tested:** NN-01, NN-11, NN-18, NN-19, NN-20, NN-21, NN-22, NN-29, NN-35, NN-36, NN-38, NN-39, NN-45, NN-46, NN-50
> **Estimated effort:** 7 two-week sprints, squad of 8 (backend 3, frontend 2, integration 1 — OH8/Razorpay, QA 1, product/finance analyst 1)

---

## 1. Objective and business outcome

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

## 2. Scope (in / out)

**In scope:** `BILLING_PORT` (OH8, LOCAL, MOCK adapters); presentation catalogue (plans, feature rows, add-ons, credit packs, explainers, FAQs); public pricing page and plan configurator; trials; checkout via Razorpay hosted pages (orders, Subscriptions, UPI AutoPay, e-mandates, Smart Collect for B2B); subscription mirror and lifecycle (upgrade, downgrade, proration via OH8 quotes, cycle change, renewal, cancellation); entitlement SDK and enforcement; seats and family members; credits (eSign, eStamp facilitation, Vidhi AI, court-data refresh, storage overage) as prepaid service units; meters at source and `UsageRecorded` aggregates; invoice/receipt/credit-note display, download and vault filing; GST profile and TDS certificate workflow; dunning presentation; coupons and referral credits; revenue-stream registry mirror with LawDocs-side switches; Pricing Studio; Settings → Billing & Membership (Personal and Company); Savings & Value dashboard and value report.

**Out of scope (owner):** price books, tax rates, invoice numbering, e-invoicing IRN, Razorpay accounts and webhooks, revenue recognition, dunning engine, collection — OH8. Marketplace engagements and Route split settlement — P16 (uses this phase's checkout). Enterprise MSAs and negotiated contracts — OH8 sales quotes. Mobile store billing integration — P22 (this phase defines the rule, §4E).

---

## 3. Personas and permissions touched

| Role code | What they can do in P17 |
|---|---|
| Anonymous visitor | Read `/pricing`, use the configurator, save/share a configuration, start sign-up, "Talk to us" (consented lead to OH3) |
| `IND_OWNER` | Choose/upgrade/downgrade Personal, add family members, buy credits, manage payment methods and mandates, download invoices, cancel, view Savings & Value |
| `IND_FAMILY_MEMBER` | Use plan allowances shared by the owner (if allowed); view own usage; cannot change billing |
| `IND_GUARDIAN`, `IND_DELEGATE` | Billing actions only if delegated `bil.manage` |
| `ORG_OWNER`, `ORG_ADMIN` | Full billing: plan, add-ons, seats, credits, billing profile and GSTINs, purchase approvals, cancellation, Savings inputs |
| `ORG_APPROVER` (e.g., CFO) | Approve purchases above threshold (step-up MFA); read all billing |
| `ORG_CLO` | Read billing and usage; request add-ons; view and export Savings & Value |
| `ORG_AUDITOR_RO` | Read invoices and billing history under grant |
| `OPS_CSM`, `OPS_RM` | Read plan, usage and renewal dates for their clients (metadata only); propose quotes via OH8; see Savings only if the tenant allows (`sav.share_with_rm`) |
| `OPS_SUPPORT_AGENT` | Read billing status for tickets; cannot change anything |
| `PLT_SUPER_ADMIN` | Pricing Studio (presentation maker), LawDocs-side stream switches (maker), per-tenant commercial overrides through OH8 (maker), kill switches |
| `PLT_LEGAL_REVIEWER` | Checker for stream switches with legal flags, claims on pricing page, FAQ legal accuracy |
| `PLT_CONTENT_EDITOR` | Feature-row copy, explainers, FAQs, benefits copy (maker) |
| `PLT_AUDITOR_RO` | Read-only commercial audit trail |
| OH8 pricing committee (outside LawDocs) | Approves commercial changes (prices, SKUs, coupons, stream gates) submitted from Pricing Studio |

---

## 4. Functional requirements

### 4A. Commercial architecture and `BILLING_PORT`

- **FR-P17-01 — Ownership split.** OH8 is the source of truth for SKUs, price books, coupons, trial policies, stream gates, quotes, orders, subscriptions, signed entitlements, invoices, credit/debit notes, receipts, mandates and dunning (Ecosystem Spec §6.27; OH8.1–OH8.7). LawDocs `bil` owns: the presentation catalogue, configurator rules, the entitlement mirror as applied, credits as applied (lots and ledger), meters at source, trial lifecycle, LawDocs-side stream switches (narrow only) and the billing UI; `sav` owns the savings ledger.
- **FR-P17-02 — Port.** `packages/billing-port` exposes `getCatalogue(version)`, `quote(req)`, `order(quoteId)`, `getSubscription(tenant)`, `listDocuments(tenant, filters)`, `getDocument(id)`, `submitUsage(statement)`, `disputeUsage(req)`, `getEntitlements(tenant)`, `submitCatalogueChange(req)`, `getChangeStatus(id)`, `validateCoupon(code, ctx)`, `requestCreditNote(req)`, `instructTransfer(req)` (P16 Route). Adapters: `OH8` (default), `LOCAL` (§4L), `MOCK` (tests). The adapter in force is setting `bil.billing_port.mode` (PLATFORM, maker-checker).
- **FR-P17-03 — No price or tax computed by LawDocs.** Display prices come from the signed catalogue in force; any amount to be charged (proration, GST, discounts, totals) comes from an OH8 quote (`POST /v1/billing/quotes`). The pricing page shows "incl. GST" totals computed from the catalogue's **tax hint** and labelled "GST at 18% — confirmed on your invoice" [TAX MEMO: SAC and rate per SKU]. A CI contract test fails if any module other than the `LOCAL` adapter multiplies an amount by a tax rate.
- **FR-P17-04 — Signed artefacts.** LawDocs verifies the JWS of each catalogue version and each `EntitlementChanged` against the pinned Hub key; unsigned or mismatched artefacts are rejected (`LD-BIL-001`) and raise a security task to `PLT_SECURITY_OFFICER`.
- **FR-P17-05 — Offline tolerance.** If OH8 is unreachable: the last valid catalogue keeps rendering; the last valid signed entitlement is honoured for 30 days (§6.27); quotes queue as "pending confirmation"; no tenant loses access because of a Hub outage.

### 4B. Plans and presentation catalogue (Appendix L §L.2–§L.3; prices `[OWNER TO SET]`)

- **FR-P17-06 — Five plans** (R6 §R6.2.2 seeds, ex-GST):

| Plan | Workspace | Annual | Monthly (+20%) | Seats / members | Positioning line |
|---|---|---|---|---|---|
| Free | Personal (and a Free Company workspace for service buyers) | ₹0 | ₹0 | 1 person | "Your legal documents in one safe place." [OWNER: Free-plan storage commitment — W.9 LA-14] |
| Personal | Personal | ₹1,499 | ₹149 | Owner + up to 4 family members (5 in all) | "Draft, sign and keep every agreement your family needs." |
| Pro | Company (sole proprietors, professionals, freelancers, startups) | ₹9,999 per workspace | ₹999 | 3 working seats | "Run your startup's or practice's legal work in one place." |
| Business | Company (companies, LLPs, NBFCs, groups) | ₹59,999 | ₹5,999 | 10 working seats + unlimited free viewer/approver/board seats | "A legal department in a box, with maker-checker and audit trail." |
| Enterprise | Company (banks, NBFCs, groups, platforms) | from ₹3,00,000 or quote | quote | Bands | "Scale, APIs, dedicated options and a managed legal team." |

  Monthly = annual ÷ 12 × 1.2, rounded down to the nearest ₹9 ending (R6 §R6.2.1 principle 5; `bil.pricing.monthly_uplift_pct` = 20, catalogue data). A person can hold a Personal plan and belong to one or more Company workspaces; billing is per workspace.
- **FR-P17-07 — Plan contents are data.** Each plan has a base SKU and components: included (✓), add-on (price delta), not available (—), Enterprise only. Allowances (vault GB, Vidhi credits/month, Aadhaar eSign credits/month, OTP signatures, eStamp facilitations, litigation matters, TM marks, documentation-team session allowance (not advocate consultations — NN-21; W.9 LA-16), Academy seats) are entitlement limits, never code (Appendix L §L.3).
- **FR-P17-08 — Free plan vault.** The Free plan keeps the user's documents within 1 GB for as long as the account is active, subject to the retention schedule and POL-LD-11 (R6 principle 1; perpetual or "free forever" storage is not claimed — NN-20, NN-50, CH-15, W.9 LA-14) [OWNER: confirm the Free-plan commitment]; export is never paywalled (NN-11). Downgrade or lapse to Free never deletes data: over-quota workspaces become upload-restricted, not read-restricted (FR-P17-31).
- **FR-P17-09 — Seat model.** Working seats (makers, checkers, admins) count; viewer, approver-only, board, auditor and counterparty seats are free (LDC N.18 pattern); agents (`AGT_*`) are add-on seats (LD-ADD-AGT), never working seats.
- **FR-P17-10 — Pricing dimensions.** The catalogue supports flat per period, per seat, per family pack, per matter band, per mark band, per unit (credits, GB), minimum commitment, volume tiers and multi-year terms; which dimension applies is catalogue data.

### 4C. Public pricing page (`/pricing`; R-036, R-042; NN-50)

- **FR-P17-11 — Structure.** Hero ("See the full price before you pay"); audience switch (For me and my family · For my startup or practice · For my company); billing toggle Annual (default) / Monthly showing the annual saving in ₹ and %; **three cards** — Personal, Pro, Business — each with: name, one-line positioning, price ex-GST, **"₹x incl. GST"** directly below (e.g., Personal "₹1,499/year + GST = ₹1,768.82/year"), monthly-equivalent line on annual, top 8 inclusions with "i" explainers, CTA ("Start 14-day free trial" / "Choose plan"), "Compare all features" link; a slim **Free** strip above ("Start free — 1 GB vault, export any time" [OWNER: Free-plan commitment]) and an **Enterprise** strip below ("Talk to us — from ₹3,00,000/year"); "Buy services without a plan" strip linking to the marketplace (P16, R-040); **benefits explained** (§FR-P17-13); full comparison table; add-ons and credit packs; FAQs (≥ 25, Appendix L §L.14); trust strip with evidenced claims only (claims gate, NN-20).
- **FR-P17-12 — Comparison table.** ≥ 100 feature rows grouped (Vault & DMS · Drafting & Vidhi AI · Negotiation & CLM · eSign, eStamp & execution · Evidence & preservation · Litigation · Trademarks & IP · Company legal department · Governance & HRMS-lite · Tax & business services · Consumer help · Marketplace benefits · Integrations & API · Security & admin · Data export & portability · Support). Each row: label, "i" explainer (≤ 280 characters + help-centre link, `hlp.bil.f<nnn>` per Appendix L §L.3), value per plan (✓, —, limit text, add-on price), evidence flag for any claim, SEO anchor. Sticky header, collapsible groups, "show differences only", print/PDF. Seed rows in Appendix L §L.3.
- **FR-P17-13 — Benefits explained.** A section per plan answering "What do I get that I don't get on Free?", "What does this replace?" (e.g., "24 Aadhaar eSigns a year — worth ₹360–₹600 at published per-sign prices of ₹15–₹25", benchmark-cited, Appendix L §L.12), "Who should not buy this" (honest disqualifiers), and subscription vs one-time explainer ("Buy one service any time without a plan; a plan makes sense if you expect more than n documents a year") — copy seeds in Appendix L §L.15.
- **FR-P17-14 — Price integrity.** No strike-through price unless it is the lowest price charged for that SKU in the preceding 30 days (price history stored); no countdown timers, "only n left", or pre-ticked add-ons; renewal price, renewal date and cancellation route shown before payment; trial terms ("No card needed. Your trial never converts to paid automatically.") shown on the card (CCPA Dark Patterns Guidelines 2023 — R3 LG-142; OH8.9). Pricing-page copy passes the OH14 claims gate.
- **FR-P17-15 — Configurator.** "Build your plan": workspace type → plan → add-ons (dependencies: `requires`, `excludes`, `min_plan`) → scale (seats, family members, storage, credits) → billing (cycle, payment preference, coupon) → review (every line, allowances, estimated GST, total, renewal terms, refund policy, links to Terms/DPA). Running total updates ≤ 150 ms from the cached catalogue and is labelled "Estimated — confirmed at checkout" until an OH8 quote returns. Never pre-selects a paid add-on; a recommendation shows why ("Recommended because you chose 'Company with litigation'"). Save/share configuration (unguessable token ≥ 128 bits; 30-day expiry; no personal data unless e-mailed).
- **FR-P17-16 — SEO and performance.** Static generation per catalogue version; JSON-LD `Product`/`Offer` with `priceSpecification` (`valueAddedTaxIncluded` false for ex-GST, plus a second `UnitPriceSpecification` incl. GST [REC]); visible FAQ HTML (FAQ rich results discontinued — conventions fact 18 [VERIFY]); LCP ≤ 2.5 s on 4G mid-range Android.

### 4D. Trials and self-serve plan start

- **FR-P17-17 — Trials.** Personal, Pro and Business: 14-day trial (`bil.trial.default_days`, PLATFORM, bounds 0–30), no card required, full plan features with capped meters (Aadhaar eSign 2, Vidhi credits 100, eStamp 0 — duty-bearing services excluded from trials). One trial per person per plan family and per organisation (PAN/CIN/GSTIN uniqueness). Reminders T-3 and T-1 ("Nothing will be charged"). At expiry the workspace returns to Free with all data kept; no auto-conversion (OH8.9).
- **FR-P17-18 — Trial extension.** `OPS_CSM` or `PLT_SUPER_ADMIN` may extend up to 14 days with a reason code; beyond that needs a checker (NN-18); the tenant sees a notice in Billing history.
- **FR-P17-19 — Start paid from anywhere.** Entry points: pricing card, configurator, locked-feature explainer in product ("Not in your plan — see what it does"), marketplace post-purchase line, RM-sent quote (OH8). Sign-up (P01): mobile/e-mail OTP or passkey; Company workspaces add organisation details via PAN/CIN/GSTIN lookup through licensed vendors (P01; NN-05).

### 4E. Checkout and payment (NN-22; CH-19, CH-25)

- **FR-P17-20 — Order.** `BILLING_PORT.order(quoteId)` → OH8 `POST /v1/billing/orders` (Idempotency-Key = quote_id + attempt) → Razorpay-hosted URL → **top-level redirect** (no Razorpay script on LawDocs pages; PCI DSS v4.0.1 SAQ A — R3 LG-148); return page polls the server; a browser redirect is never proof of payment; `SubscriptionPaymentReceived` (signed, via `int`) activates.
- **FR-P17-21 — Methods.** Cards (tokenised by Razorpay; no card data stored — R3 LG-146), UPI and UPI AutoPay, netbanking, Razorpay Subscriptions for monthly/annual plans, eNACH for recurring debits above the e-mandate AFA-free limit (₹15,000 per debit [VERIFY under RBI e-mandate Directions 2026 — R3 LG-147]), Smart Collect virtual account/bank transfer for Business/Enterprise invoices, invoice-later against PO for Enterprise. Pre-debit notice ≥ 24 hours by the issuer plus a LawDocs T-48 h courtesy notice (OH8.7).
- **FR-P17-22 — Billing profile.** Mandatory before the first business order: legal name, GSTIN per billing State (format + status check via licensed GSP/vendor where available), place of supply, billing address, PAN, PO number (optional/required per tenant), billing contacts (1–10), e-invoice recipient e-mail, SEZ/IFSC flag with LUT reference [VERIFY IFSC treatment], TDS applicability declaration. Individuals: name, State (place of supply), e-mail; GSTIN optional. **What reaches OH8 for an individual buyer (X-13):** only the closed `buyer_billing_identity` list — name, email, phone, optional GSTIN and billing address, amounts and tax lines, SKU and quantity — under legal basis `CONTRACT_PERFORMANCE_CUSTOMER` (Appendix Y §Y.6.2); never vault, matter, case, document or consumer-case data. Consumer Help purchases use the same list under the Consumer Help selling entity with generic SKUs that name neither the respondent institution nor the grievance (NN-23). DPO sign-off before the first B2C invoice [OI-Y-03].
- **FR-P17-23 — Purchase approvals (Company).** If `bil.tenant.purchase_approval_threshold` is set, orders above it wait in `PENDING_TENANT_APPROVAL` for `ORG_APPROVER` (step-up MFA); the approver sees quote, GST, renewal and refund terms.
- **FR-P17-24 — Failure handling.** Failure leaves the subscription unchanged; reason class shown with retry; three failures in 24 hours offer bank transfer or "Talk to us"; webhook delay > 15 minutes shows "We are confirming your payment with the bank"; reconciliation resolves within 2 hours or raises an OH8 billing-operations task.
- **FR-P17-25 — Mobile apps.** iOS/Android show plan status, usage, invoices and credits; purchase of plans and AI credits inside the apps follows store policy — default `bil.mobile.purchase_mode = WEB_HANDOFF` (no in-app purchase button where store rules require store billing for digital goods; an informational "Manage on lawdocs.in" link only where permitted) [VERIFY Apple App Review Guidelines §3.1 and Google Play payments policy for India, incl. user-choice/alternative billing; OI-P17-06]. Real-world professional services bought in the marketplace follow P16 (person-to-person services) [VERIFY].

### 4F. Subscription lifecycle and changes

- **FR-P17-26 — States** (mirror OH8.4/OH8.7): `TRIAL`, `TRIAL_ENDED`, `PENDING_ACTIVATION`, `ACTIVE`, `RENEWAL_DUE`, `PAST_DUE`, `GRACE`, `RESTRICTED`, `TERMINATION_NOTICE`, `CANCELLATION_REQUESTED`, `ENDED_TO_FREE`, `EXIT`, `CLOSED`. LawDocs adds only trial states and `ENDED_TO_FREE` (Personal/Pro/Business revert to Free rather than closing the account).
- **FR-P17-27 — Upgrade.** Plan upgrade, add-on, seats, family members or storage: OH8 quote preview (prorated charge on IST calendar-day basis, GST, entitlement diff) → pay → `PlanChanged` + `EntitlementChanged` → applied within 1 minute. Where Razorpay Subscriptions cannot change plan in place (e.g., domestic-card subscriptions allowing only offer updates [VERIFY]), OH8 invoices the prorated difference and re-creates the subscription at the next cycle; the user sees one clear explanation.
- **FR-P17-28 — Downgrade and removal.** Effective at term end by default; the screen lists exactly what will change ("Litigation tracker will track 5 cases; the other 23 stay readable and exportable; alerts for hearings already scheduled continue until each date passes"). Removing a component others depend on is blocked with dependants listed. Seat reduction requires reassigning open maker/checker tasks first (P02 guard).
- **FR-P17-29 — Cycle change.** Monthly → annual immediately with proration credit, or at renewal; annual → monthly at renewal.
- **FR-P17-30 — Renewal and cancellation (NN-50).** Auto-renewal disclosed at purchase and in reminders at T-30 and T-7 (annual) / T-3 (monthly), with any price change notice ≥ 30 days before effect; one-click "Turn off auto-renewal". Cancel lives in Settings → Billing → Cancel or change plan, reachable in ≤ 2 clicks from Billing overview, with no more steps than purchase, no confirm-shaming, no forced call; optional reason; shows end date, refund position (Appendix L §L.13: annual plans — pro-rata refund within the first 30 days of the first term [OWNER TO SET]; Personal — 14-day cooling-off full refund on first purchase [OWNER TO SET]), one-click full export (P20). Withdrawable until effective.
- **FR-P17-31 — Never-block list (floor; not configurable).** No plan limit, lapse, downgrade or dunning stage may block: reading any existing record; downloading or exporting (NN-11); verifying a signed document or evidence pack; sharing a signed document already shared; nominee/guardian emergency access (P04); reminders for deadlines already set (hearings, limitation, TM renewals, obligation due dates); completion of a signing ceremony already started; access by auditors under an active grant; grievance intake under Consumer Help. Test `NN-11_billing_never_blocks`.
- **FR-P17-32 — Pause.** Not offered for Business/Enterprise [REC: pausing a legal-ops tool creates unmanaged obligations; downgrade instead]; Personal may downgrade to Free at any time with data kept.

### 4G. Entitlement enforcement

- **FR-P17-33 — SDK.** `packages/entitlements`: `check(tenant, feature)`, `limit(tenant, key)`, `consume(tenant, meter, qty, idempotencyKey)`, NestJS guard `@RequiresEntitlement('lit.matters')`, React hook `useEntitlement()`. State comes from `bil.entitlements_applied`, updated only by verified `EntitlementChanged` (or `LOCAL`); cache keyed by tenant (NN-01) with event-driven invalidation.
- **FR-P17-34 — Limit behaviour.** 80% soft banner + admin e-mail; at 100%: seats — new invitations blocked; storage — uploads blocked except evidence for an open matter/obligation with a due date ≤ 30 days; AI — Vidhi falls back to deterministic features and offers credits; matters/marks — new tracking blocked, existing continue. No overage charge unless the tenant opted in (`bil.tenant.overage_opt_in`, default OFF) — "no surprise overage" (R6 §R6.2.6).
- **FR-P17-35 — Daily reconciliation.** By 06:00 IST compare applied entitlements with OH8 `GET /v1/entitlements?tenant=`; mismatches raise `ReconciliationBreakRaised` and an OH8 task; the **more generous** state applies until resolved.

### 4H. Credits as prepaid service units (no wallet)

- **FR-P17-36 — Design rule.** LawDocs sells **credits**, never a rupee balance: each credit type is a unit of a specific LawDocs service (Appendix L §L.5). Credits are non-transferable between accounts, cannot be withdrawn as cash, cannot pay third-party professionals, stamp duty, court fees or any amount owed to another person, and are redeemable only for the named LawDocs service. This keeps them outside third-party payment use; any feature that would let a balance pay a third party is prohibited [REC; VERIFY with counsel against the RBI Master Directions on Prepaid Payment Instruments — closed-system PPI scope — before launch; TAX MEMO on whether credit packs are vouchers under CGST Act s.2(118) and their time of supply; OI-P17-03]. R1 records LegalKart's wallet (non-refundable, 30–180-day expiry, inconsistent statements) as the pattern to avoid.
- **FR-P17-37 — Credit types.** `ESIGN_AADHAAR` (1 = one successful Aadhaar eSign by one signatory), `SIGN_ELECTRONIC` (OTP/e-mail signature beyond fair use), `ESTAMP_FACILITATION` (LawDocs's facilitation for one stamp instrument; **duty is never a credit** and is charged at actuals per instrument — NN-08), `VIDHI_AI` (rate card in Appendix L §L.5), `COURT_DATA_REFRESH` (one licensed-provider refresh of one matter), `STORAGE_GB_MONTH` (overage only). Deterministic features (reminders, search, calendar, CNR tracking display) consume 0 credits (R6 §R6.2.4).
- **FR-P17-38 — Lots and ledger.** Every grant is a lot (`bil.credit_lots`: type, quantity, source — PLAN_ALLOWANCE, PACK_PURCHASE, PROMO, REFERRAL, SERVICE_CREDIT, GOODWILL — price ref, granted_at, expires_at). Consumption draws first from the lot expiring soonest, plan allowance before purchased (`bil.credits.consumption_order`). The ledger (`bil.credit_ledger`) is append-only with idempotency keys from the source event (e.g., `sig_` id for an eSign) (NN-45, NN-46).
- **FR-P17-39 — Expiry and refund rules (one rule, stated identically everywhere — R1 IMP-085).** Plan allowances expire at period end (no rollover by default, `bil.credits.allowance_rollover`). Purchased packs are valid **12 months** (`bil.credits.pack_validity_months`, 12–36) with reminders T-30 and T-7 and one free 6-month extension on request; unused purchased credits are refundable pro-rata within 30 days of purchase and on account closure [OWNER TO SET]; promotional and referral credits are labelled separately and expire as stated at grant. A failed or reversed service returns the credit automatically (failed eSign = credit back — "pay only for successful eSigns", R6 B-16).
- **FR-P17-40 — Low balance and caps.** Alerts at 20% and 5%; optional per-user caps (Company, `bil.credits.user_cap.<type>`); **no auto top-up** by default (`bil.credits.auto_topup`, USER/TENANT opt-in only, never pre-ticked).

### 4I. Add-ons and seats

- **FR-P17-41 — Add-ons** (Appendix L §L.4: family extension, extra seat, litigation pack, trademark watch, advanced CLM, advanced DMS, data room, board & secretarial pro, HRMS-lite, SSO + SCIM, API tier, BYO storage/scheduled export, premium support, white-label practice workspace, Vidhi role-agent seat, storage packs). Each add-on: availability by plan, dependencies, price, proration rule, removal effect, "i" explainer.
- **FR-P17-42 — Family members.** Personal owner invites up to 4 members (`IND_FAMILY_MEMBER`); allowances may be shared or allotted per member (`bil.family.allowance_mode`: SHARED default); each member's vault stays private unless shared (P04); a member leaving keeps their own documents in their own Free account.

### 4J. Metering at source

- **FR-P17-43 — Meters** (Appendix L §L.8): `ESIGN_AADHAAR` (sgn), `SIGN_ELECTRONIC` (sgn), `ESTAMP_FACILITATION` (sgn), `VIDHI_CREDITS` (ai), `COURT_DATA_REFRESH` (lit), `TM_WATCH_MARKS` (ipm), `STORAGE_GB_MONTH` (dms), `WHATSAPP_NOTIFY` (ntf), `API_CALLS` and `API_AGREEMENT_GENERATE` (int), `MKP_CONSULT_ALLOWANCE` (mkp), `SEATS_PEAK`, `FAMILY_MEMBERS`. Each producing module calls `consume()` in the same transaction as the business event (NN-45) with an idempotency key.
- **FR-P17-44 — Statements.** Daily provisional and monthly final statements by WD+3; `UsageRecorded` (`usage_aggregate_v1`: tenantid, legal entity, meter, period, quantity, `meter_kind`, statement version, hash) goes to OH8 via `int` — **never** user, document, matter, signer or person identifiers (Ecosystem Spec §6.27; NN-19). LawDocs's registration as a producer is requested in Appendix Y.
- **FR-P17-45 — Transparency and disputes.** Settings → Billing → Usage shows the same aggregates the customer is billed on, with drill-down available only inside the workspace (e.g., eSigns by document for the admin). Dispute within 7 days (`POST /v1/usage-disputes`); invoicing for that meter holds until decided.

### 4K. Invoices, receipts, credit notes and tax documents (R-040)

- **FR-P17-46 — Display and download.** Settings → Billing → Invoices & receipts lists OH8 tax invoices (with IRN/QR where e-invoicing applies to the selling entity — Notification 10/2023-CT [VERIFY AATO]), credit/debit notes (CGST Act s.34), receipts and statements of account; filters by FY/year, type, status, supplier (LawDocs, LawDocsComply, Consumer Help brand, professionals' invoices from P16); PDF download, XLSX statement, bulk ZIP by FY; hash shown.
- **FR-P17-47 — E-mail delivery.** On `InvoiceIssued`, the invoice PDF (or a signed link if > 5 MB) is e-mailed to billing contacts (OH8 sends by default; LawDocs shows in-app; idempotent on invoice number — no duplicates); copy filed automatically in the vault: Company `10 Billing and Invoices/<FY>/Invoices/`; Individual `10 Receipts and Invoices/<Year>/`.
- **FR-P17-48 — GST presentation.** Lines show SAC, taxable value, CGST+SGST or IGST by place of supply (IGST Act s.12(2)); pass-through amounts (stamp duty, government fees) as separate non-taxable pure-agent lines (CGST Rules r.33 [TAX MEMO]); advocates' invoices (P16 M2) shown as the professional's document with the RCM/exempt note (Notification 13/2017-CT(R) Sl. 2; R6 T-01–T-02).
- **FR-P17-49 — TDS certificates.** Business customers upload quarterly TDS certificates against invoices (Income-tax Act 2025 s.393(1); form per OH8 [VERIFY form number]); status tracked; forwarded to OH8 `tds_receivable`. Settings shows LawDocs's published TDS position for its SaaS (technical vs professional characterisation [TAX MEMO]; R6 T-06).
- **FR-P17-50 — Corrections.** Billing disputes open an OH6 ticket `BILLING_DISPUTE`; dunning pauses for that invoice; corrections are always credit/debit notes from OH8, never edits.

### 4L. Interim `LOCAL` adapter (only if OH8 is not live)

- **FR-P17-51 — Scope.** Implements `BILLING_PORT` in schema `bil_local`: SKUs, price books, coupons, quotes, orders, Razorpay (LawDocs-owned account; keys in the platform vault; SAQ A pattern; webhook HMAC verification, de-duplication), subscriptions, GST invoice generation (CGST Rules r.46 fields; e-invoicing via GSP if AATO requires), credit notes, dunning per OH8.7 timings. Flag `bil.billing_port.mode = LOCAL_INTERIM` (owner decision OI-P17-01).
- **FR-P17-52 — Migration to OH8.** Scripted export of SKUs, price-book versions, coupons, customers, subscriptions, invoices (historical, not re-issued), mandates (re-mapped or re-authorised), open balances, credit lots; reconciliation report signed by finance; one-cycle dual run; adapter flips to `OH8`; `bil_local` becomes read-only archive (NN-12).

### 4M. Dunning presentation

- **FR-P17-53 — Tenant view** (OH8.7 timeline: PAST_DUE D0 → retries D+1/D+3/D+7 → GRACE to D+14 → RESTRICTED D+30 after 7 days' notice → TERMINATION_NOTICE D+45): banners to owners/admins and billing contacts; `RESTRICTED` blocks only new seats, add-ons, new matters/marks tracking and credit purchases by card; the never-block list applies; `TERMINATION_NOTICE` prepares the export pack automatically (P20) and reverts the workspace to Free at effect — never deletion.
- **FR-P17-54 — Reinstatement.** Full payment or an OH8 payment plan returns `ACTIVE` within 15 minutes of the event.

### 4N. Coupons, promotions and referral credits

- **FR-P17-55 — Coupons** are OH8 coupons (percentage, fixed, extended trial, free add-on for n months, first-term discount, partner code) with constraints (segments, plans, first purchase only, minimum term, redemptions, validity, stackability default OFF). Validation live in the configurator; discount line and expiry shown. Codes never imply outcomes ("WINYOURCASE" rejected by lint).
- **FR-P17-56 — User referral (RS-LD-35).** Both referrer and referee receive credits (e.g., 2 Aadhaar eSign credits) after the referee's first paid action; credits only, no cash; disclosed in terms (CCPA endorsement rules — R4 §11.6); regulated professionals are excluded from any referral reward (NN-21; RS-LD-29). Affiliate (RS-LD-36) and partner resale (RS-LD-37) run through OH8 partner codes with disclosure and are OFF/ON per the registry.

### 4O. Revenue-stream registry and switches (R-054; NN-18, NN-39)

- **FR-P17-57 — Registry.** `bil.stream_registry` holds RS-LD-01…RS-LD-45 (Appendix L §L.9) with: code, name, segment, OH8 stream type (e.g., `SUBSCRIPTION`, `ONE_TIME_SERVICE`, `MONTHLY_RENTAL`, `PAYG`, `PASS_THROUGH`, `PROFESSIONAL_SERVICES`, `MANAGED_SERVICES`, `TRAINING`, `ADVERTISING_SPONSORSHIP`, plus new types requested in Appendix X: `CREDIT_PACK`, `MARKETPLACE_PLATFORM_FEE`, `RETAINER`, `REFERRAL_CREDIT`, `AFFILIATE`, `PARTNER_RESALE`), payer class, **owner** (named role), **effective_from / effective_to**, **disclosure text** (where shown, exact words), **tax treatment** (SAC, rate, pure-agent lines, RCM/TCS/TDS notes — [TAX MEMO] reference), **refund rule** code, legal-review reference, OH8 gate status (`DRAFT → LEGAL_REVIEW → TAX_REVIEW → OWNER_DECISION → APPROVED → ACTIVE → SUSPENDED | RETIRED` — OH8.3), LawDocs-side switch, kill-switch scope (stream × segment × channel × brand × profession), deny-list flag.
- **FR-P17-58 — Switch semantics.** A purchase option is shown only if its OH8 gate is `ACTIVE` **and** `bil.stream.<code>.enabled` is ON for that brand, segment and channel. LawDocs switches only narrow OH8 gates, never widen them. Switching ON or OFF is maker-checker: maker `PLT_SUPER_ADMIN`, checker `PLT_LEGAL_REVIEWER` for streams flagged legal, owner approval for streams flagged `OWNER_DECISION` (NN-18). Kill switch: one action hides a stream from every surface within 5 minutes (`StreamSwitchChanged` → cache invalidation); existing contracts run on their terms; RMs and CSMs are notified (NN-39).
- **FR-P17-59 — Hard deny list (not configurable).** RS-LD-27 (commission/share of advocates', CAs', CSs', CMAs' fees), RS-LD-28 (listing, featured, ranking, lead or badge fees from regulated professionals), RS-LD-29 (referral rewards to regulated professionals), LD-X01 (per-minute ranked advocate pricing), LD-X02 (sale of user/matter/document data), LD-X03 (pre-ticked bundles and hidden auto-renewing subscriptions), LD-X04 (credit-bureau report marketing), LD-X05 (rupee-denominated stored-value wallet or any balance usable for third-party payments), LD-X06 (lead fees from lenders or insurers for routing consumer complaints), LD-X07 (success fee where an advocate acts) — Appendix L §L.9.1 — stored as `deny = true` with no write path; CI test `NN-21_deny_streams_immutable`.
- **FR-P17-60 — Advertising stays OFF.** RS-LD-34 default OFF; if ever switched ON (owner + counsel), it can render only on public content pages (blog, vlog, learning) labelled "Sponsored", contextual only, never targeted on personal data, never in vault, matters, consumer cases, AI answers, pricing or checkout, and never for advocates, CAs, CSs, lenders or insurers (NN-35; D-13; CH-21).
- **FR-P17-61 — Change in law.** An `ObligationPublished`-type change tag (via LDC rules feed or the `rul` register) touching BCI, ICAI, ICSI, CCPA, GST, ITA25, PA, PPI or DPDP moves affected streams to `SUSPENDED` pending review (OH8.3 re-review); new sales stop; existing contracts continue.

### 4P. Pricing Studio (`apps/console`)

- **FR-P17-62 — Editor tabs.** Plans · Add-ons · Credit packs · Feature rows · Groups · Configurator rules · Bundles · Benefits explained · FAQs · Coupons (draft) · Stream registry · Segment presets · SEO · Preview & publish · History. Preview renders the exact public page for any audience and date (`?as_of=`) side by side with live, with a string and price diff.
- **FR-P17-63 — Two kinds of change.** Presentation changes (copy, order, grouping, explainers, badges, FAQs) are LawDocs-owned: maker → checker → publish with `effective_from` (NN-30 pattern; no code release). Commercial changes (price, SKU, coupon, trial policy, stream gate, tax hint) are drafted here and submitted to OH8 as catalogue change requests; status shown (`SUBMITTED → IN_REVIEW → APPROVED → PUBLISHED | RETURNED`); the matching presentation version publishes automatically with the OH8 catalogue version.
- **FR-P17-64 — Publish guard-rails** (`LD-BIL-030…039`): a plan without a price for the selected market; a row asserting a certification or endorsement without a claims-register reference (NN-20); a "Most popular" badge without a stored basis (orders in last 90 days); a feature row whose entitlement key does not exist; a mandatory dependency purchasable alone; an incl.-GST total missing on any card (NN-50); a strike-through without 30-day price history.
- **FR-P17-65 — Per-tenant commercial overrides (CH-26 pattern).** Trial extension, free add-on for a period (as a coupon), negotiated price (OH8 sales quote), limit change (OH8 order or zero-value entitlement change) — each reason-coded, maker-checker, audit-ledgered, and shown to the tenant in Billing history ("LawDocs extended your trial by 7 days on 26-10-2026: onboarding issue").

### 4Q. Settings → Billing & Membership (R-042 — very detailed)

- **FR-P17-66 — Page set (Personal workspace).** Overview · Plan & benefits · Family members · Credits · Usage · Invoices & receipts · Payment methods & AutoPay · Billing details · Coupons & referral credits · Services & orders (P16) · Renewal & notices · Cancel or change plan · Billing history · Savings & Value · Billing notifications. **(Company workspace)** adds: Add-ons · Seats & users · Legal entities & GSTINs · Purchase approvals · Tax documents (TDS, LUT, GST certificates) · Retainers & SLA credits (P16) · Contracts & order forms. Full field lists in §6.
- **FR-P17-67 — Overview card.** Plan, status chip, term, renewal date with auto-renew toggle, next charge estimate (OH8 quote), payment method, allowances used this period with bars (text values for screen readers), quick actions (Upgrade, Buy credits, Add seats, Download latest invoice, Manage AutoPay), entitlement health ("All features active").
- **FR-P17-68 — Plan & benefits.** Current plan's features grouped as on the pricing page with "You use this" markers from usage (e.g., "You signed 9 documents with Aadhaar eSign this year"); "What changes if I switch to …" comparison for adjacent plans; benefit explainers; downgrade preview (FR-P17-28).
- **FR-P17-69 — Customisation.** Billing contacts per notification type; invoice language (English + one Indian language for the cover e-mail [REC]); PO number rules; consumption order of credits; per-user credit caps; family allowance mode; overage opt-in; purchase approval threshold; RM visibility of savings — all TENANT/USER settings, never needing Super Admin (NN-29).
- **FR-P17-70 — Click budgets.** Download latest invoice ≤ 2 clicks from home (avatar → Billing → latest); buy credits ≤ 3; upgrade ≤ 3 (+ checkout); turn off auto-renewal ≤ 2; cancel ≤ 3 + confirmation.

### 4R. Savings & Value dashboard (R-063; NN-36, NN-20)

- **FR-P17-71 — Honesty principle.** Every tile shows its **evidence class** — **MEASURED** (facts recorded by LawDocs or entered by the user with evidence: counts, durations, amounts paid), **ESTIMATED** (uses default baselines or market benchmarks not measured for this user), **MODELLED** (computed from a published rule and recorded inputs with stated assumptions, e.g., exposure) — plus formula, inputs, period and a "How we calculated this" panel. ESTIMATED tiles have a dotted outline and the word "estimate"; MODELLED tiles carry a "Modelled" chip and their assumptions. Users may hide ESTIMATED tiles (`sav.user.show_estimates`).
- **FR-P17-72 — Metrics** (formulas, baselines, benchmarks and penalty bindings in Appendix L §L.12):
  - **Hours saved (ESTIMATED; MEASURED component)** = Σ_a max(0, B_a − M_a) × N_a ÷ 60, where B_a = baseline minutes for activity *a* (methodology version; user-editable with history), M_a = median measured minutes in LawDocs (workflow timestamps; waiting-on-others time excluded), N_a = completed count (MEASURED).
  - **Money saved vs market (ESTIMATED)** = Σ_i (P_i^bench − P_i^paid) over items used in the period, where P^bench = benchmark price for the equivalent market service (Appendix L §L.12 table: median of published prices with source and date; benchmarks older than 180 days excluded) and P^paid = what the user paid for that item (unit price, credit cost or allocated plan cost: plan price for the period × item's share of included-allowance value). Shows gross market value of usage and net saving; pass-through amounts (stamp duty, government and court fees) are excluded on both sides. Negative results are shown, not hidden.
  - **Spend (MEASURED)** = subscription + add-ons + credits + services paid in the period (from OH8 documents).
  - **People-cost saved (ESTIMATED, Company)** = Hours saved by role band × hourly cost band entered by the tenant (tile hidden until bands are set).
  - **Outside spend avoided (MEASURED if evidenced)** = tenant-entered prior costs of replaced tools or outside drafting, with dates and evidence.
  - **Deadlines met (MEASURED)** = count of obligations, hearings, limitation dates, TM renewals and filings completed before due, by family.
  - **Exposure avoided (MODELLED; labelled "avoided exposure — not money saved")** = Σ_o [completed before due]_o × Penalty(rule_o, d_ref), only for obligations with an evidenced rule, due date and completion record (NN-36); d_ref shown as a range (1 day and 30 days late) unless the user enters a historical late rate; rules unverified for > 180 days are excluded. Non-monetary consequences (e.g., limitation lapse, ex parte risk) show as counts with a description, never a rupee figure.
  - **Measured return (MEASURED)** = Outside spend avoided ÷ Spend; **Estimated return (ESTIMATED, labelled)** = (People-cost saved + Outside spend avoided) ÷ Spend. Neither includes MODELLED exposure or ESTIMATED market-benchmark savings.
- **FR-P17-73 — Placement and outputs.** Settings → Savings & Value (both workspaces); a home widget (hours saved, deadlines met); quarterly "Value report" PDF/DOCX with methodology annex for Company boards/CLOs; RM QBR pack only if `sav.share_with_rm` is ON (TENANT; default ON for retainer clients, OFF otherwise).
- **FR-P17-74 — Use outside the workspace.** Aggregated, anonymised statistics may be used in marketing only across ≥ 20 workspaces, with method disclosure and OH14 claims-gate PASS; a single customer's figures only with written consent (NN-20).

### 4S. Notifications (`ntf`; templates in Appendix L §L.16)

Trial started / T-3 / T-1 / ended; quote ready; payment received; payment failed (with retry); invoice issued; mandate pre-debit courtesy (T-48 h); usage 80% / 100%; credits low / expiring T-30 / T-7; renewal T-30 / T-7 (annual) and T-3 (monthly); price-change notice (≥ 30 days); plan changed; add-on added/removed; restriction notice; termination notice; reverted to Free; override by LawDocs; savings report ready. Payment, renewal, restriction and termination notices are mandatory (cannot be muted); promotional messages only with marketing consent (R4-MKT-09).

---

## 5. Workflows and state machines

### 5.1 Subscription (mirror of OH8 with LawDocs trial states)

| State | Entry | Next | Actor | Guard | Effect |
|---|---|---|---|---|---|
| TRIAL | Trial started | TRIAL_ENDED, PENDING_ACTIVATION | User | One trial per person/org per plan family | Trial entitlement (signed by OH8 or LOCAL) |
| TRIAL_ENDED | Day 14 | PENDING_ACTIVATION, (Free) | System | — | Revert to Free; data kept |
| PENDING_ACTIVATION | Order created | ACTIVE | OH8 | Server-verified payment or PO accepted | `SubscriptionActivated` |
| ACTIVE | Payment / contract start | RENEWAL_DUE, PAST_DUE, CANCELLATION_REQUESTED | — | — | Entitlements applied |
| RENEWAL_DUE | T-30 / T-7 | ACTIVE, CANCELLATION_REQUESTED | User / OH8 | Notices sent | — |
| PAST_DUE → GRACE → RESTRICTED → TERMINATION_NOTICE | OH8.7 timeline | ACTIVE on payment; ENDED_TO_FREE at effect | OH8 | 7 days' notice before RESTRICTED | Never-block list (FR-P17-31) |
| CANCELLATION_REQUESTED | User cancels | ACTIVE (withdraw), ENDED_TO_FREE | User | — | Export reminder; refund per rule |
| ENDED_TO_FREE | Term end after cancel/termination | ACTIVE (re-subscribe) | System | — | Free limits; data kept; read/export always |
| EXIT → CLOSED | Account closure requested by user | — | User + P20 | Export offered; legal hold respected | Deletion per retention with certificate |

### 5.2 Plan change

```
SELECT target → QUOTE (OH8: proration, GST, entitlement diff, valid 7 days) → [PENDING_TENANT_APPROVAL] → ORDER → PAY (or credit applied)
 → PlanChanged + EntitlementChanged (signed) → APPLIED (≤ 1 min) → audit + notification
Downgrade: SCHEDULED (term end) → APPLIED at effect; withdrawable until then.
```

### 5.3 Credit lot

```
GRANTED (allowance | pack | promo | referral | service credit) → ACTIVE → CONSUMED (partial/full; ledger rows)
 → EXPIRED (at expires_at; notice T-30/T-7) | REFUNDED (pro-rata rule; OH8 credit note) | EXTENDED (once, on request)
Reversal of a failed service → RETURNED to the originating lot (idempotent on source event id).
```

### 5.4 Stream switch

```
PROPOSED (maker) → CHECKED (PLT_LEGAL_REVIEWER where legal flag) → [OWNER_APPROVED] → EFFECTIVE (effective_from)
 → StreamSwitchChanged → caches invalidated ≤ 5 min. Kill switch: PROPOSED+CHECKED in one emergency flow with a second approver within 15 min.
```

### 5.5 Savings computation (nightly + on demand)

```
COLLECT (meters, workflow timestamps, OH8 documents, obligations) → APPLY methodology version v → COMPUTE tiles
 → SNAPSHOT (inputs, versions, hash; evidence class per tile) → PUBLISH to dashboard → (quarterly) VALUE_REPORT
Methodology change → new version; past snapshots never recomputed silently (show "computed with v3").
```

---

## 6. Screens and UX

### 6.1 Public and purchase

| ID | App | Screen | Key components | States | Mobile | Accessibility |
|---|---|---|---|---|---|---|
| SCR-P17-01 | public | Pricing page | Audience switch, cycle toggle, three cards with ex-GST and incl.-GST totals, Free/Enterprise strips, benefits explained, services strip | Catalogue unavailable → last good version | Cards stack; sticky CTA | Price read as "₹1,499 per year plus GST, total ₹1,768.82" |
| SCR-P17-02 | public | Comparison table | Grouped rows, "i" explainers, differences toggle, print | — | Horizontal plan switcher (one plan column at a time vs selected) | `th scope`, ✓/— with text alternatives |
| SCR-P17-03 | public | Configurator | Steps, live total, dependency prompts, save/share | Invalid combination → inline reason | Bottom-sheet summary | Live region announces total changes politely |
| SCR-P17-04 | public | Enterprise enquiry | Consented form → OH3 | — | — | — |
| SCR-P17-05 | web/mobile | Checkout review | Lines, GST, total, renewal and cancellation terms, refund rule, Pay (redirect) | Failure reason + retry | Native sheet | Focus moves to total before Pay |
| SCR-P17-06 | web | Payment return | Polling state, confirmation, next steps | Delay > 15 min message | — | — |

### 6.2 Settings → Billing & Membership (`apps/web`; mobile read + limited actions)

| ID | Page | Fields and actions |
|---|---|---|
| SCR-P17-10 | Overview | FR-P17-67 |
| SCR-P17-11 | Plan & benefits | Current plan, features in use, adjacent-plan comparison, upgrade/downgrade with quote preview, scheduled changes |
| SCR-P17-12 | Add-ons (Company) | Each add-on: state (Included / Active / Available / Scheduled removal), price, dependencies, add/remove with quote |
| SCR-P17-13 | Family members (Personal) | Members, invite/remove, allowance mode, per-member usage |
| SCR-P17-14 | Seats & users (Company) | Working vs free seats, last activity, reassign helper, buy seats |
| SCR-P17-15 | Credits | Balance by type and lot (source, expiry), consumption history (workspace-only detail), caps, buy pack, extension request, refund request |
| SCR-P17-16 | Usage | Meters vs allowance, trend, statement versions, dispute (7-day window) |
| SCR-P17-17 | Invoices & receipts | Documents by supplier and FY, filters, PDF/ZIP/XLSX, hash, "Raise billing query" |
| SCR-P17-18 | Payment methods & AutoPay | Tokens (last 4, issuer), mandates (status, max amount, frequency), cancel mandate, update (redirect to Razorpay) |
| SCR-P17-19 | Billing details | Legal name, GSTINs by State, place of supply, addresses, PAN, PO rules, billing contacts, e-invoice e-mail, SEZ/IFSC + LUT, TDS declaration |
| SCR-P17-20 | Tax documents (Company) | TDS certificates by quarter, LUT copies, GST certificates, LawDocs TDS position note |
| SCR-P17-21 | Coupons & referral credits | Applied coupons with expiry, enter code, referral link, referral credits earned |
| SCR-P17-22 | Services & orders | P16 engagements and retainers, SLA credits, professionals' invoices |
| SCR-P17-23 | Purchase approvals (Company) | Threshold, approvers, pending approvals |
| SCR-P17-24 | Renewal & notices | Renewal timeline, auto-renew toggle, price-change notices, contracts and order forms (signed copies) |
| SCR-P17-25 | Cancel or change plan | Options (downgrade, switch cycle, cancel), what changes, refund position, export now |
| SCR-P17-26 | Billing history | Every commercial event incl. LawDocs overrides with reason; Correction Entries with original (NN-02) |
| SCR-P17-27 | Savings & Value | Tiles by evidence class, methodology panels, inputs (baselines, hourly bands, replaced costs, historical late rate), period selector, Value report export |
| SCR-P17-28 | Billing notifications | Recipients per type; mandatory types marked |

### 6.3 Console

| ID | Screen | Purpose |
|---|---|---|
| SCR-P17-40 | Pricing Studio | FR-P17-62–64 |
| SCR-P17-41 | Stream registry | All RS-LD streams, gate status (OH8), LawDocs switch, owner, effective dates, disclosures, kill switch |
| SCR-P17-42 | Tenant commercial view | Plan, entitlements applied vs OH8, overrides (maker-checker), credit lots |
| SCR-P17-43 | Meter health | Statement status per meter, disputes, reconciliation breaks |
| SCR-P17-44 | Savings methodology registry | Activity baselines, benchmark table with source dates, penalty bindings, versions |

UX rules: plain-language labels with "i" keys (`hlp.bil.proration`, `hlp.bil.auto_renewal`, `hlp.bil.credit_lot`, `hlp.bil.pure_agent`, `hlp.bil.reverse_charge`, `hlp.bil.tds_certificate`, `hlp.bil.e_mandate`, `hlp.bil.place_of_supply`, `hlp.sav.evidence_class`, `hlp.sav.avoided_exposure`, `hlp.sav.benchmark`); upsell only as a non-modal "Not in your plan — see what it does" on locked items, never during a signing ceremony or a deadline task; no nagging (one dismissal suppresses for 30 days).

---

## 7. Backend design

### 7.1 Modules

`bil` (owner), `sav` (owner), `int` (OH8 adapter, events), `cfg` (settings), `wf` (approvals, maker-checker), `ntf`, `dms` (invoice filing), `xpt`, producing modules for meters (`sgn`, `ai`, `lit`, `ipm`, `dms`, `ntf`, `int`, `mkp`), `core` (audit).

### 7.2 Tables (tenant tables RLS, NN-01)

| Table | Key columns | Notes |
|---|---|---|
| `bil.catalogue_versions` | version, jws, content_hash, effective_from, fetched_at | Signed copy of OH8 catalogue |
| `bil.presentation_versions` | version, catalogue_version, plans, rows, explainers, faqs, benefits, status, maker, checker | LawDocs-owned |
| `bil.plans` | `pln_` id, code, workspace_type, base_sku, allowances jsonb | Mirror for display |
| `bil.feature_rows` | id, group, label_i18n, explainer_key, values jsonb, claims_ref, anchor | ≥ 100 rows |
| `bil.subscriptions_mirror` | tenant_id, oh8_subscription_ref, plan, state, term, renewal_at, auto_renew | Read model |
| `bil.entitlements_applied` | `etl_` id, tenant_id, version, modules, limits jsonb, jws, applied_at | Only from verified events |
| `bil.credit_lots` | id, tenant_id, user_id (nullable), type, qty (NUMERIC), source, price_ref, granted_at, expires_at, state | Append-only state changes |
| `bil.credit_ledger` | lot_id, delta, reason, source_event_id (unique per type), created_at | Idempotent |
| `bil.meter_events` | tenant_id, meter, qty, source_event_id, occurred_at | Partitioned monthly |
| `bil.usage_statements` | tenant_id, legal_entity_id, meter, period, quantity, version, hash, sent_at, dispute_state | → `UsageRecorded` |
| `bil.billing_profiles` | tenant_id, legal_name, gstins jsonb, pos, pan, contacts, po_rules, sez_ifsc, lut_ref, tds_declared | RESTRICTED class |
| `bil.documents_mirror` | `inv_` id, tenant_id, type, number, supplier, fy, amounts_ref, pdf_doc_id, hash | Filed in vault |
| `bil.payments_mirror` | `pay_` id, tenant_id, razorpay_payment_id, method_class, amount_ref, captured_at | No card data |
| `bil.stream_registry` / `bil.stream_switch_history` | code, fields per FR-P17-57; switch: from, to, maker, checker, effective_from, reason | Permanent audit |
| `bil.trials` | tenant_id, plan, started_at, ends_at, extensions jsonb | — |
| `bil.saved_configs` | token_hash, config jsonb, expires_at | No PII by default |
| `bil.price_history` | sku, price_ref, from, to | For 30-day prior-price rule |
| `sav.methodologies` | version, activities, formulas, published_by | Versioned |
| `sav.baselines` / `sav.benchmarks` / `sav.penalty_bindings` | per Appendix L §L.12 with source, date, last_verified_at | Platform + tenant overrides |
| `sav.tenant_inputs` | tenant_id, hourly_bands, replaced_costs, late_rate_history, evidence_doc_ids | Tenant-entered |
| `sav.snapshots` | tenant_id, period, methodology_version, tiles jsonb (value, class, inputs), hash | Never recomputed silently |

### 7.3 APIs

| Method | Path | Scope | Idempotency |
|---|---|---|---|
| GET | `/v1/public/pricing?audience=&as_of=` · `/v1/public/pricing/compare` | public | — |
| POST | `/v1/public/pricing/configurations` (save/share) | public | Idempotency-Key |
| POST | `/v1/billing/quotes` (→ OH8) · `/v1/billing/orders` (→ OH8) | `bil.manage` | Idempotency-Key |
| GET | `/v1/billing/subscription` · `/entitlements` · `/usage` · `/documents` · `/credits` | `bil.read` | — |
| POST | `/v1/billing/credits/purchase` · `/credits/{lot}/extend` · `/credits/{lot}/refund-request` | `bil.manage` | Idempotency-Key |
| POST | `/v1/billing/usage-disputes` (→ OH8) | `bil.manage` | Idempotency-Key |
| POST | `/v1/billing/cancel` · `/auto-renew` · `/approvals/{id}/approve` | `bil.manage` / `ORG_APPROVER` | Idempotency-Key |
| PUT | `/v1/billing/profile` | `bil.manage` | ETag |
| POST | `/v1/billing/tax-documents` (TDS certificate upload) | `bil.manage` | Idempotency-Key |
| GET/POST | `/v1/savings/dashboard` · `/inputs` · `/value-report` | `sav.read` / `sav.manage` | Idempotency-Key |
| POST | `/v1/console/pricing/presentation-versions` · `/{v}/approve` · `/catalogue-change-requests` | `PLT_*` | Idempotency-Key |
| POST | `/v1/console/streams/{code}/switch` · `/{code}/switch/{id}/approve` | `PLT_SUPER_ADMIN` / `PLT_LEGAL_REVIEWER` | Idempotency-Key |
| Internal | `entitlements.consume(tenant, meter, qty, key)` (SDK, same transaction) | service | source event id |

### 7.4 Domain events

Internal (`in.lawdocs.bil.*.v1`): `TrialStarted`, `TrialEnded`, `QuoteRequested`, `CheckoutStarted`, `SubscriptionActivated`, `PlanChangeScheduled`, `EntitlementApplied`, `LimitThresholdReached`, `CreditsGranted`, `CreditsConsumed`, `CreditsReturned`, `CreditsExpired`, `CreditsLow`, `UsageStatementClosed`, `UsageDisputed`, `InvoiceFiled`, `CancellationRequested`, `AutoRenewToggled`, `BillingProfileChanged`, `StreamSwitchChanged`, `CommercialOverrideApplied`, `PresentationPublished`; `in.lawdocs.sav.SnapshotComputed.v1`, `in.lawdocs.sav.MethodologyPublished.v1`, `in.lawdocs.sav.ValueReportGenerated.v1`. Cross-product via `int` (Ecosystem Spec §6.27 names): consumed `PlanChanged`, `EntitlementChanged`, `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`, `SubscriptionCancelled`; produced `UsageRecorded` (from `UsageStatementClosed`, `usage_aggregate_v1`, counts only), `ModuleAttached`, `ModuleDetached` (from `EntitlementApplied`) — LawDocs registration as producer in Appendix Y §Y.7.7; mapping in Appendix I §I.8.

### 7.5 Jobs

`CatalogueSyncJob` (on `PlanChanged` + daily), `EntitlementReconciliationJob` (06:00 IST), `UsageStatementJob` (daily provisional; monthly final by WD+3), `CreditExpiryJob` (daily; notices), `TrialLifecycleWorkflow` (Temporal), `RenewalNoticeJob`, `PaymentReturnPoller`, `InvoiceFilingJob` (on `InvoiceIssued`), `SavingsSnapshotJob` (nightly), `ValueReportWorkflow` (quarterly), `StreamCacheInvalidator` (on `StreamSwitchChanged`), `LocalToOH8MigrationWorkflow` (one-off, §4L).

---

## 8. Integrations

| Port / adapter | Use | Failure behaviour |
|---|---|---|
| `BILLING_PORT` → OH8 (`/v1/catalogue/versions/{v}`, `/v1/billing/quotes`, `/v1/billing/orders`, `/v1/billing/invoices`, `/v1/usage-disputes`, `/v1/entitlements`) | All commerce | Offline tolerance (FR-P17-05) |
| Razorpay (through OH8 only; LOCAL interim) | Hosted checkout, Subscriptions, UPI AutoPay, e-mandates, Smart Collect, refunds | Webhooks verified by OH8; LawDocs never holds keys except under LOCAL |
| GSTIN status lookup (licensed GSP/vendor via P01) | Billing profile validation | Format check only; user confirms |
| OH14 claims gate | Pricing copy, benefits, savings marketing claims | Publishing blocked |
| OH3 (`int`) | Enterprise enquiries, consented | Queue |
| OH6 | Billing disputes | Ticket queued; dunning pause instruction sent to OH8 |
| P20 `xpt` | Export pack on cancellation/termination | Retry; never blocks cancellation |

---

## 9. Settings and configuration (Appendix R)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `bil.billing_port.mode` | PLATFORM | enum OH8/LOCAL_INTERIM/MOCK | OH8 | Owner via `PLT_SUPER_ADMIN` | Y |
| `bil.pricing.display_mode` | BRAND | enum EX_GST_PLUS_TOTAL / INCL_GST | EX_GST_PLUS_TOTAL (both shown) | `PLT_SUPER_ADMIN` | Y |
| `bil.pricing.monthly_uplift_pct` | PLATFORM | decimal | 20 | Pricing committee (OH8) | Y |
| `bil.trial.default_days` | PLAN | int | 14 (0–30) | `PLT_SUPER_ADMIN` | Y |
| `bil.trial.extension_max_days_without_checker` | PLATFORM | int | 14 | `PLT_SUPER_ADMIN` | Y |
| `bil.refund.annual_prorata_window_days` | PLATFORM | int | 30 [OWNER TO SET] | Owner | Y |
| `bil.refund.personal_cooling_off_days` | PLAN | int | 14 [OWNER TO SET] | Owner | Y |
| `bil.credits.pack_validity_months` | PLATFORM | int | 12 (12–36) | Owner | Y |
| `bil.credits.allowance_rollover` | PLAN | bool | false | Pricing committee | Y |
| `bil.credits.consumption_order` | TENANT | enum | ALLOWANCE_FIRST_THEN_EARLIEST_EXPIRY | `ORG_ADMIN` / `IND_OWNER` | N |
| `bil.credits.auto_topup` | TENANT / USER | bool | false | Owner of workspace | N |
| `bil.credits.user_cap.<type>` | TENANT | int | none | `ORG_ADMIN` | N |
| `bil.family.allowance_mode` | TENANT (Personal) | enum SHARED/ALLOTTED | SHARED | `IND_OWNER` | N |
| `bil.tenant.overage_opt_in` | TENANT | bool | false | `ORG_ADMIN` | N |
| `bil.tenant.purchase_approval_threshold` | TENANT | money | off | `ORG_ADMIN` | N |
| `bil.tenant.po_required` | TENANT | bool | false | `ORG_ADMIN` | N |
| `bil.notifications.recipients.<type>` | TENANT | list | billing contacts | `ORG_ADMIN` | N |
| `bil.mobile.purchase_mode` | PLATFORM | enum WEB_HANDOFF / STORE_BILLING / EXTERNAL_LINK | WEB_HANDOFF [VERIFY] | `PLT_SUPER_ADMIN` | Y |
| `bil.stream.<code>.enabled` | PLATFORM / BRAND / segment | bool | per Appendix L §L.9 | `PLT_SUPER_ADMIN` + `PLT_LEGAL_REVIEWER` (+ owner where flagged) | Y |
| `bil.upsell.dismiss_days` | USER | int | 30 | user | N |
| `bil.exit.read_only_days` | PLATFORM | int | 30 (floor 30) | — | — |
| `sav.enabled` | TENANT | bool | true | `ORG_ADMIN` / `IND_OWNER` | N |
| `sav.user.show_estimates` | USER | bool | true | user | N |
| `sav.share_with_rm` | TENANT | bool | true for retainer clients, else false | `ORG_ADMIN` | N |
| `sav.benchmark.max_age_days` | PLATFORM | int | 180 | `PLT_SUPER_ADMIN` | Y |
| `sav.penalty_rule.max_unverified_days` | PLATFORM | int | 180 | `PLT_LEGAL_REVIEWER` | Y |
| `sav.marketing.min_workspaces` | PLATFORM | int | 20 (floor) | — | — |

---

## 10. Security, privacy and audit

- **PCI DSS v4.0.1 SAQ A scope** (CH-19): hosted/redirect checkout only; script inventory and CSP on pages that launch checkout; no card data stored, processed or logged; annual SAQ A attestation per selling entity is OH8/OH14 evidence — LawDocs copy says "LawDocs never stores card data", never "PCI certified" (R3 LG-148; NN-20).
- **Aggregates only to OH8** (NN-19): usage statements carry no person, document or matter identifiers; schema test with a seeded document id that must be rejected.
- **Maker-checker** (NN-18) on stream switches, overrides, refunds and credit grants above `bil.goodwill_credit_max` (₹2,000 [OWNER TO SET]), adapter mode, methodology publication.
- **Audit ledger** (NN-02, NN-45) for every commercial event; Correction Entries for errors; tenant-visible Billing history.
- **Data classes:** billing profile and payment mirrors RESTRICTED; savings inputs CONFIDENTIAL; Savings snapshots tenant-private; logs exclude PAN in full, GSTIN-linked personal data and mandate details (NN-32).
- **DPDP:** billing processing on contract basis; marketing consent separate; billing contacts' personal data minimised; retention of invoices ≥ 72 months from annual-return due date (CGST Act s.36 [VERIFY]) via OH8; LawDocs vault copies follow the customer's retention.

---

## 11. AI touchpoints and guardrails

| Feature | Autonomy | Human point | Guardrail |
|---|---|---|---|
| Plan advisor (Vidhi, public + in-app) | L1 suggest | User chooses | Explains plans from catalogue data only; discloses AI; never claims savings without the methodology; no pressure language (claims gate) |
| Savings narrative in Value report | L2 draft | Admin/CLO releases report | Narrates computed tiles only; cannot add figures; labels classes |
| Billing support answers | L1 | Escalate to `OPS_SUPPORT_AGENT` | Reads billing metadata of the asking user's workspace only; cannot issue refunds or credits (NN-13) |

No agent can purchase, cancel, change plans, switch streams or grant credits (NN-13, NN-43).

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p17/*.feature`)

```gherkin
@P17-AT-01 @NN-50
Scenario: Pricing card shows total including GST
  Given the Personal plan priced at ₹1,499 per year ex-GST in the catalogue
  When a visitor views /pricing in Annual mode
  Then the card shows "₹1,499/year + GST" and "₹1,768.82/year incl. GST"

@P17-AT-02 @NN-50
Scenario: No strike-through without price history
  When a maker adds a strike-through ₹2,999 for Personal with no 30-day history at ₹2,999
  Then publish fails with LD-BIL-036

@P17-AT-03
Scenario: Upgrade with prorated quote
  Given a Pro workspace on an annual term with 200 days left
  When the admin chooses Business
  Then an OH8 quote shows the prorated charge, GST and entitlement diff before payment
  And after SubscriptionPaymentReceived the Business entitlements apply within 1 minute

@P17-AT-04 @NN-11
Scenario: Lapse never blocks read or export
  Given a Business workspace in RESTRICTED
  When a user opens a signed agreement and requests a full export
  Then both succeed and only new seats and add-ons are blocked

@P17-AT-05 @NN-50
Scenario: Cancellation is as easy as purchase
  Given an IND_OWNER on Personal
  When they cancel from Settings → Billing → Cancel or change plan
  Then cancellation completes in no more steps than the purchase took
  And no confirm-shaming text or forced call is presented

@P17-AT-06
Scenario: Trial never converts automatically
  Given a Pro trial ending today with no order
  Then the workspace reverts to Free with all data kept and no charge is attempted

@P17-AT-07 @NN-22
Scenario: Browser redirect is not proof of payment
  Given a user returns from Razorpay with a success parameter but no verified payment event
  Then the subscription stays PENDING_ACTIVATION and the page shows "We are confirming your payment"

@P17-AT-08
Scenario: Failed eSign returns the credit
  Given a lot with 10 ESIGN_AADHAAR credits
  When a signing attempt fails at the ESP
  Then the consumed credit is returned to the same lot, idempotent on the signing event id

@P17-AT-09
Scenario: Credits cannot pay third parties
  When a user tries to apply VIDHI_AI or ESIGN_AADHAAR credits to a professional fee or to stamp duty
  Then the request is refused with LD-BIL-020

@P17-AT-10 @NN-46
Scenario: Usage statement is idempotent and aggregate only
  Given the monthly ESIGN_AADHAAR statement for tenant T was sent as version 1
  When the job reruns
  Then no duplicate UsageRecorded is sent
  And the payload contains no document, signer or user identifier

@P17-AT-11 @NN-18 @NN-39
Scenario: Stream switch needs a checker and kills within 5 minutes
  Given RS-LD-13 Trademark watch is ON
  When PLT_SUPER_ADMIN proposes OFF and PLT_LEGAL_REVIEWER approves
  Then within 5 minutes no pricing, configurator or in-app surface offers Trademark watch
  And existing subscriptions continue to their term end

@P17-AT-12 @NN-21
Scenario: Deny-listed streams cannot be enabled
  When anyone attempts to enable RS-LD-27
  Then the request is rejected with LD-BIL-041 "Prohibited stream"

@P17-AT-13 @NN-35
Scenario: Advertising off by default and never in private areas
  Given RS-LD-34 is OFF
  Then no ad slot renders on any page
  When an owner switches it ON with counsel reference
  Then ad slots render only on blog, vlog and learning pages labelled "Sponsored"

@P17-AT-14 @NN-36
Scenario: Avoided exposure is labelled and excluded from savings
  Given a company filed an MCA form 3 days before its due date with penalty rule s.403 verified within 180 days
  Then the Exposure avoided tile shows a Modelled range for 1 and 30 days late
  And "Money saved" and both return tiles exclude that amount

@P17-AT-15 @NN-36 @NN-20
Scenario: Stale benchmark excluded
  Given the eSign benchmark was last verified 200 days ago
  Then the Money saved tile omits eSign items and shows "benchmark out of date"

@P17-AT-16
Scenario: Invoice e-mailed and filed
  When OH8 emits InvoiceIssued for a Company workspace in FY 2026-27
  Then billing contacts receive one e-mail with the PDF
  And a copy is filed in "10 Billing and Invoices/2026-27/Invoices/"

@P17-AT-17 @NN-29
Scenario: Tenant changes credit consumption order without Super Admin
  When an ORG_ADMIN sets bil.credits.consumption_order to EARLIEST_EXPIRY_FIRST
  Then the change applies to the next consumption and is audit-ledgered

@P17-AT-18 @NN-38
Scenario: Mobile purchase mode stays web hand-off until verified
  Given bil.mobile.purchase_mode verification is not logged
  Then the iOS app shows no plan purchase button

@P17-AT-19 @NN-19
Scenario: OH8 rejects a statement with a document identifier
  Given a usage statement contaminated with a doc_ id in a test
  Then the int adapter blocks publication with LD-BIL-025 before it leaves LawDocs

@P17-AT-20
Scenario: Purchase approval for companies
  Given a purchase approval threshold of ₹50,000
  When an ORG_ADMIN orders the Business plan
  Then the order waits in PENDING_TENANT_APPROVAL until the ORG_APPROVER approves with step-up MFA

@P17-AT-21 @NN-01
Scenario: Billing documents are tenant-isolated
  Given invoice I belongs to Company workspace A
  When a user of workspace B requests GET /v1/billing/documents/I
  Then the response is 404 and the attempt is audit-ledgered

@P17-AT-22 @NN-45 @NN-46
Scenario: Credit consumption is atomic with the business event
  Given an eSign completes but the transaction fails before commit
  Then no credit is consumed and a retry with the same signing event id consumes exactly one credit
```

Error codes: `LD-BIL-001` signed artefact invalid · `-002` catalogue version unknown · `-005` OH8 unavailable (quote queued) · `-010` disposable e-mail domain · `-011` duplicate trial · `-012` GSTIN invalid · `-015` quote expired · `-016` approval required · `-020` credit type not applicable · `-021` credits expired · `-022` credit cap reached · `-025` usage statement contains prohibited identifier · `-026` dispute window closed · `-030…039` Pricing Studio publish lint (missing price, unevidenced claim, popularity badge without basis, unknown entitlement key, orphan dependency, missing incl.-GST total, strike-through without history) · `-040` stream gate not ACTIVE · `-041` prohibited stream · `-042` checker equals maker · `-050` never-block violation (internal alert). `LD-SAV-001` methodology version missing · `-002` benchmark out of date · `-003` penalty rule unverified · `-004` input evidence missing. Help keys `hlp.bil.err_<nnn>` / `hlp.sav.err_<nnn>`.

NN tests: `NN-11_billing_never_blocks`, `NN-19_usage_aggregates_only`, `NN-21_deny_streams_immutable`, `NN-22_no_price_or_tax_outside_oh8`, `NN-22_redirect_not_payment`, `NN-35_ads_off_and_scoped`, `NN-36_savings_evidence_classes`, `NN-39_stream_kill_switch_latency`, `NN-50_cancel_steps_le_purchase_steps`, `NN-50_price_card_total_incl_gst`.

---

## 13. Exit gate, deliverables and open items

**Checklist**

- [ ] `BILLING_PORT` with OH8 adapter certified against the OH8 sandbox (catalogue, quote, order, entitlements, invoices, usage, disputes); LOCAL adapter only if OI-P17-01 decided.
- [ ] Pricing page, comparison (≥ 100 rows), benefits, FAQs and configurator published from the presentation catalogue; claims gate PASS; accessibility audit passed.
- [ ] Settings → Billing & Membership pages SCR-P17-10…28 live for Personal and Company workspaces.
- [ ] Credits, meters (all producing modules registered), statements and disputes working; no rupee balance anywhere.
- [ ] Stream registry seeded with RS-LD-01…45 and deny list; kill-switch latency test green.
- [ ] Savings & Value with methodology v1, baselines, benchmarks and penalty bindings (Appendix L §L.12) reviewed by `PLT_LEGAL_REVIEWER`.
- [ ] Settings in Appendix R; help keys in `hlp`; errors registered; Appendix X/Y requests filed.

**Demo script.** (1) Visitor compares plans, toggles monthly/annual, sees incl.-GST totals, starts a Personal trial without a card. (2) User converts to annual, pays by UPI on Razorpay hosted page; invoice e-mail arrives and appears in the vault. (3) User buys a 10-pack of eSign credits; one eSign fails and the credit returns. (4) Company admin adds 3 seats with prorated quote; CFO approves above threshold. (5) Admin cancels in 3 steps; workspace reverts to Free at term end with all data readable and exportable. (6) Console: switch off Trademark watch with checker; it disappears from pricing within 5 minutes. (7) Savings & Value shows hours saved (estimate), money saved vs dated benchmarks, deadlines met and Modelled exposure in its own labelled tile.

**Export-map entries**

| Record type | Company path | Individual path |
|---|---|---|
| `bil.invoice`, `bil.credit_note`, `bil.receipt` | `10 Billing and Invoices/<FY>/{Invoices, Credit Notes, Receipts}/` | `10 Receipts and Invoices/<Year>/` |
| `bil.statement`, `bil.usage_statement` | `10 Billing and Invoices/<FY>/Statements and Usage/` | `10 Receipts and Invoices/<Year>/Statements/` |
| `bil.contract` (order forms, MSA, renewal notices) | `10 Billing and Invoices/<FY>/Contracts and Order Forms/` | `10 Receipts and Invoices/<Year>/Plan Terms/` |
| `bil.tds_certificate` | `10 Billing and Invoices/<FY>/TDS Certificates/` | — |
| `bil.credit_ledger`, `bil.billing_history` | `99 System Data (CSV and JSON)/billing/` | `99 System Data/billing/` |
| `sav.snapshot`, `sav.value_report` | `10 Billing and Invoices/<FY>/Value Reports/` + `99 System Data/savings/` | `99 System Data/savings/` |

**Open items**

| ID | Item | Owner | Fallback / flag |
|---|---|---|---|
| OI-P17-01 | OH8 live date vs P17 sprint 3; LOCAL interim adapter decision | Owner + OH lead | LOCAL behind flag |
| OI-P17-02 | Final price points, GST-inclusive display for B2C, refund windows | Owner `[OWNER TO SET]` | R6 seeds |
| OI-P17-03 | PPI/closed-system analysis of credits; voucher time-of-supply and revenue recognition for credit packs and breakage | [COUNSEL] + [TAX MEMO] | Credits limited to LawDocs services; refundable rule |
| OI-P17-04 | SAC per SKU (SaaS, facilitation, platform fee), TDS characterisation guidance for buyers | [TAX MEMO] | Tax hint "18% — confirmed on invoice" |
| OI-P17-05 | e-mandate limits and pre-debit rules under RBI e-mandate Directions 2026; Razorpay plan-change constraints | Finance [VERIFY] | OH8 behaviour |
| OI-P17-06 | Apple/Google store billing rules for India (digital subscriptions, credits) | P22 lead [VERIFY] | `bil.mobile.purchase_mode = WEB_HANDOFF` |
| OI-P17-07 | Time-and-motion study to replace seed activity baselines | Product + ops | Baselines labelled "default estimate" |
| OI-P17-08 | New OH8 stream types and meters (Appendix X) and `UsageRecorded` producer registration (Appendix Y) | OH lead | Map to nearest existing stream type |

**Conflicts recorded.** R6 §R6.2.4 sets pack validity at 12 months with no refund rule; R1 IMP-085 asks for refundable or non-expiring paid balances — this phase sets 12 months with reminders, one free extension and pro-rata refund within 30 days and on closure (owner to confirm). NN-36 classes (MEASURED/ESTIMATED/MODELLED) replace LDC's Recorded/Modelled/Estimated naming.

