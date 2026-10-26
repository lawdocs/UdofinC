# Appendix AB — Revenue Architecture v3 and Revenue Stream Registry (v3.0, 23 October 2026)

> **Binding reference** for P05 (billing engine, entitlements, coupons, invoices, dunning), P10 (Private ADR Chambers add-ons and tenant revenue settings), P13 (pricing pages, "How Equator earns" page, advertising and sponsored slots), P19 (Revenue Stream Registry implementation, kill switches, price governance, viability reviews) and the Operations Platform (`apps/ops`, D3-02) finance and sales workspaces. Read with master NN-16, NN-17, NN-18, NN-21, NN-28, NN-29 and v3 NN-33 to NN-40; decisions D2-14, D2-17, D2-18, D2-19, D3-01, D3-05, D3-08; master X-29; **Appendix O** (revenue architecture v2, plans, entitlements, billing pages, deny-list X-01…X-16 — extended here); **Appendix B** (all figures, refund matrix §B.8, tax table §B.10, FX §B.6 — B prevails on every figure); Appendix U §U.7 (Refund Policy ERP-2026.1, "U-7"); Appendix G (legal rules); Appendix N (neutrality firewall, EQAP, training separation); Appendix AA (Marketplace surfaces and Professional Registry, companion file); Appendix Z (workforce time data used, in aggregate only, for cost-to-serve); Appendix AF (competitive research).
>
> Research: [RB] business models, revenue streams RS-01…RS-35, automations AU-01…AU-26, funnel techniques, equatoradr.com findings; [RA] Jupitice and its marketplace; [RE] legal limits on directories, paid placement, advocate fees, marketplace tax and group data. All research accessed 23 October 2026. Every price is **"Subject to Board approval"** (Appendix B §B.12) and lives in data, never in code.

## AB.0 Purpose, sources, precedence

### AB.0.1 What this appendix does

| # | Purpose | Build consumer |
|---|---|---|
| 1 | Maps every way the Equator ecosystem earns money, who pays, who keeps the money and where the neutrality firewall sits (§AB.1) | Board pack; P19; Ops Platform finance workspace |
| 2 | Specifies the **Revenue Stream Registry** (`rev` schema): one governed record per stream, with status, scope, kill switch, approvals, tax, refunds, cost drivers, KPIs and review cadence (§AB.2) | P19 (implementation); P05 (enforcement at quote, checkout and entitlement time) |
| 3 | Publishes the full **stream catalogue** RS-01…RS-57 with launch default, neutrality rating and approver, and marks streams that are OFF or prohibited (§AB.3) | Seed migration `rev_v3_seed`; CI `revenue-denylist` |
| 4 | Defines the **plans and packages engine** on top of Appendix O: bundles, add-ons, trials, coupons, proration, metering, invoices, dunning, revenue recognition notes and multi-currency (§AB.4) | P05 |
| 5 | Sets **refund, cancellation and renewal codes** for new stream types, as proposals to Appendix B §B.8 and U-7 (§AB.5) | P05; U-7 owner (CFO) |
| 6 | Sets **unit economics and pricing governance**: cost inputs, margin guardrails, price-change workflow, A/B price tests and Board thresholds (§AB.6) | P19; Ops Platform; Board |
| 7 | Gives the **business model canvas, viability scorecard, launch sequencing and stop/go criteria** (§AB.7) | Board; P19 viability reviews |
| 8 | Gives the settings catalogue (L/G/T), DDL, APIs, events, error codes, RBAC, audit, acceptance tests and phase addenda (§AB.8–§AB.15) | P05, P10, P13, P19 |

### AB.0.2 Precedence and what this appendix supersedes

Master §15 precedence applies unchanged: master → Appendix G → **Appendix B on every figure, fee semantic and tax treatment** → Appendix F on names → Appendix A on states → the phase file → other appendices. Within the revenue domain:

| # | Topic | Resolution (binding) |
|---|---|---|
| AB-R1 | System of record for **whether a stream exists, its status, scope and kill switch** | The approved `rev.stream_versions` record (this appendix). Appendix O §1.2 S-01…S-17 stay as descriptive labels; each S-code maps to an RS-code (§AB.3.4). A plan, tariff item, CMS price block or CTA whose stream is not `live` in the caller's scope cannot be quoted, sold or shown (`REV_STREAM_NOT_LIVE`). |
| AB-R2 | Figures | Unchanged: Appendix B cards and `core.plan_prices` hold every amount. The registry holds only **approved price bounds** (minimum and maximum) and links to the schedule versions that implement them. |
| AB-R3 | Deny-list | Appendix O §1.5 X-01…X-16 stay. This appendix adds **deny X-17…X-22** (§AB.3.3). In this appendix "deny X-nn" means a deny-list item and "master X-nn" a master §15 resolution. |
| AB-R4 | Referral rewards to advocates | **Superseded:** Appendix O X-11 ("non-cash credits only"), O S-15 note, Appendix B Card CH ("non-cash credits only (NN-17)") and Appendix B §B.10 partner row ("advocates: credits only"). Under NN-34 advocates, CAs, CSs and CMAs receive **no referral reward of any kind** (master X-62, below). |
| AB-R5 | Paid placement | Appendix O X-03 stays absolute for the Equator institutional neutral directory, allocation, eligibility, Quality Index, grading and conflict checks. Paid placement exists only as stream RS-19 on the Private Practice Marketplace surface (D3-01, NN-34), flag `marketplace.paid_placement` OFF. |
| AB-R6 | Business Assure default | Appendix O §8.6 (`plans.biz_assure.enabled` OFF until the public label is cleared, O-R7) prevails over [RB] RS-12 "ON". RS-12 launches OFF. |
| AB-R7 | Professional Panel Register revenue | [RB] RS-30 "ON (private mode)" is narrowed: OFF until the Board designates the registry owner and a Group Data-Sharing Agreement is signed (D3-05, NN-38, NN-39). |
| AB-R8 | Partner programme | [RB] RS-28 named CA/CS firms as partners. Under NN-34, CAs, CSs and CMAs (and advocates) are excluded from cash or credit referral rewards; partners are limited to non-professional businesses (software vendors, chambers of commerce, industry associations, HR and lending technology firms). |
| AB-R9 | Marketplace take on advocate-neutrals | Pending counsel, the percentage take (Appendix B §B.7.7; O-R2) is **not** applied to fees of a neutral who is an enrolled advocate; a flat platform fee for Equator's own services applies instead ([RE] F1.4(d), C.14–C.15; master X-62). |
| AB-R10 | Jupitice take-rate in Appendix B §B.7.7 rationale | Internal rationale only; never public (NN-17). The figure is unsourced third-party data ([RA] F9). Recorded as a finding in Appendix AF. |
| AB-R11 | Optional paid tools plan for marketplace service providers (Appendix AA §AA.10.1 `mkp.provider_subscriptions`; P19-OI-14) | Registered as **RS-57** (family `saas_subscription`, N1, OFF). The plan buys workspace tools only; it is never readable by ranking, sponsored eligibility, reviews, badges, allocation or the take rate (NN-34). |
| AB-R12 | Marketplace tax flag names | Appendix G names prevail (master §15): `billing.eco_gst_tcs` (LR-TAX-008) and `billing.eco_withholding` (LR-TAX-007). `tax.eco_gst_tcs` and `tax.eco_tds` are aliases only (Appendix AA X-59 (h)). |

### AB.0.3 New identifiers in this appendix

| ID | Statement |
|---|---|
| **R-65** | Equator shall maintain a **Revenue Stream Registry** in which every revenue stream is a versioned, maker-checker-approved record with status (draft → approved → live → paused → retired), scope (jurisdiction, segment, organisation, tenant type, vertical, case scope), a kill switch effective within 5 minutes, legal and ethical dependencies, a neutrality rating, tax treatment, refund code, cost drivers, KPIs and a review cadence; prices are changed only within approved bounds through maker-checker; internal cost and margin data are private; customer-facing explanation pages are generated only from approved records. (Appendix AB; P19, P05, P13) |
| **D3-38** | **Training through equatoradr.com is a related-party stream, ₹0 to Equator by default.** Equator records no revenue from the training site (operated as "Equa Trainings / Equa.Law", a brand of Infrabyx Consultancy (OPC) Private Limited [RB §1.1]) unless the Board approves an arm's-length arrangement under Companies Act 2013 s.188 (with s.184 disclosure and, where thresholds are crossed, shareholder approval; s.177 only where an Audit Committee is mandatory) **[CS to confirm related-party status under s.2(76) — OP-15]**. Stream RS-22 stays OFF until corrections C1–C20 (Appendix AF §AF.4) are evidenced and the operating entity, CIN and GSTIN are displayed on the site. Training never affects empanelment, grade, allocation, EQAP fee or directory position (master X-29). |
| **D3-39** | **Revenue sequencing and stop/go governance.** Streams launch in waves (§AB.7.3); every stream has a viability review (monthly for its first two quarters, then quarterly; annual Board review); Board approval thresholds for new streams and price changes are the authority-matrix defaults in §AB.6.5, held as Governed settings; a stream whose neutrality rating is N2 or above, or which depends on counsel, a vendor contract or an unconfirmed fact, defaults OFF with its approver named. |
| **master X-61** | **Registry precedence.** The approved `rev` record decides whether a stream may be offered in a scope; Appendix B decides its figures; Appendix O decides plan entitlements and billing screens. Deny-list items continue as deny X-17…X-22. Any document that lists a stream as ON while its registry record is not `live` is wrong and is corrected to the registry. |
| **master X-62** | **Professional-rule limits on revenue.** (a) No referral reward of any kind (cash, credit, discount, priority) to advocates, CAs, CSs or CMAs, superseding O X-11, O S-15, B Card CH, B §B.10 and the "credits/co-counsel" wording in master NN-17; (b) no listing, featured, ranking or lead fee charged to them; (c) no commission or share of an advocate's fee, and no percentage of a recovery; (d) the marketplace percentage take is not applied to advocate-neutrals' fees pending counsel — a flat fee for Equator's own services applies; (e) CA, CS and CMA entries follow their institutes' rules (`register.ca`, `register.cs`, `register.cma` OFF) ([RE] F1.2–F1.5; BCI Rules Part VI Ch. II r.36 and the 2008 Schedule, Ch. III r.2; ICAI ESB 23 Oct 2019; ICSI Guidelines 2020; ICMAI Guidelines 2025 **[VERIFY — open: Gazette date]**). |

R-66 (competitive research register) is defined in Appendix AF.

---

## AB.1 Ecosystem revenue map

### AB.1.1 Principles added to Appendix O RA-1…RA-7

| ID | Principle | Enforcement |
|---|---|---|
| RA-8 | **No stream without a record.** Nothing is quoted, invoiced, advertised or bundled unless its registry record is `live` for the buyer's scope. | Quote, checkout and CMS guards call `RevenueRegistry.assertLive(stream, scope)`; CI `REV_ORPHAN_PRICE` fails on any `core.fee_schedules`/`core.plans` row without a `stream_code` |
| RA-9 | **Dependent streams start OFF.** A stream depending on counsel, a Board resolution, a vendor contract, a related-party approval or an unconfirmed fact cannot pass `approved` until the dependency record is attached (conventions "Flags"). | Transition guards `REV_COUNSEL_OPINION_REQUIRED`, `REV_BOARD_RESOLUTION_REQUIRED`, `REV_RELATED_PARTY_APPROVAL_REQUIRED` |
| RA-10 | **Every stream has a kill switch** that stops new sales within 5 minutes and honours existing obligations (run-off). | §AB.2.5; test `REV_KILL_SWITCH_5_MIN` |
| RA-11 | **Revenue is invisible to appointment.** Allocation, eligibility, Quality Index, grading, conflict checks and the institutional directory have no read path to `rev`, `core.subscriptions`, `core.plans`, `core.memberships` or `mkp` billing tables (NN-28, NN-34). | CI `NO_PAID_PLACEMENT` extended to the `rev` schema |
| RA-12 | **Professional rules are product rules.** No stream may pay, reward or charge advocates, CAs, CSs or CMAs in a way listed in master X-62. | Tariff tags `advocate_commission`, `advocate_listing_fee`, `professional_referral_reward` fail the `revenue-denylist` job |
| RA-13 | **Related parties are disclosed and approved.** Any stream that moves money between Equator Resolution Service Private Limited (ERSPL) and a group company or the training site's operator is a `related_party` stream requiring a recorded s.188 approval reference before `approved`. | Guard `REV_RELATED_PARTY_APPROVAL_REQUIRED`; `rev.related_party_arrangements` |
| RA-14 | **Say how we earn.** A public page `/trust/how-we-earn` lists every live stream by who pays, what each never affects, and the deny-list, generated from approved records. | §AB.2.9; test `REV_EXPLANATION_FROM_APPROVED_ONLY` |

### AB.1.2 Map by business area

"Owner" is who books the revenue: **ERSPL** (Equator), **neutral** (pass-through, `revenue_owner = 'neutral'`), **tenant** (a Chambers or institution tenant's own fees), **Institute operator** (the training site's legal entity), **group** (another Infrabyx company). Neutrality ratings N0–N4 are defined in §AB.2.4.

| # | Area | Buyer | Streams (§AB.3) | Owner | Highest neutrality rating | Launch position |
|---|---|---|---|---|---|---|
| 1 | Equator institution — administered cases | Parties; enterprise payers | RS-01, RS-02, RS-15, RS-42…RS-46, RS-56 | ERSPL; neutral fees pass through | N1 | Live at P05 GA (RS-46 OFF) |
| 2 | Enterprise programmes | Lenders, insurers, employers | RS-03, RS-04, RS-05 | ERSPL | N1 (repeat player; disclosed, RA-7) | Live at P09 GA |
| 3 | SaaS — GRM and POSH | Regulated entities, listed companies, employers, HEIs | RS-06, RS-07 | ERSPL | N0 | Live at P09 GA |
| 4 | SaaS — Counsel workspace | Advocates, firms | RS-11 | ERSPL | N0 | Live |
| 5 | SaaS — Private ADR Chambers (subscriptions and rental) | Independent neutrals, chambers, institutions | RS-09, RS-36, RS-37, RS-38, RS-10 | ERSPL; tenant keeps its own fees | N0 | RS-09, RS-36, RS-38 live at P10 GA; RS-10, RS-37 OFF |
| 6 | Marketplace (Private Practice) | Chambers tenants, non-advocate neutrals, ancillary service providers; buyers | RS-18, RS-19, RS-52, RS-57 | ERSPL (take and fees); neutral or tenant (booking fee) | N2 | RS-18 live with the marketplace (Appendix AA); RS-19, RS-52, RS-57 OFF |
| 7 | Registry and panel management (group shared service) | Lenders and enterprises managing their own panels | RS-30, RS-31 | Registry owner designated by the Board (D3-05) | N0 private / N4 for any fee on public search | OFF until D3-05 owner and GDSA |
| 8 | Training via equatoradr.com | Learners (Institute's customers) | RS-22 (Equator side), RS-21 (EQAP — Equator's own) | Institute operator (courses); ERSPL (EQAP only) | N1 | RS-21 live; RS-22 OFF (D3-38) |
| 9 | Implementation and integration services | Enterprises, chambers | RS-27, RS-39, RS-40 | ERSPL | N0 | Live |
| 10 | Premium support and customer success | Tenants | RS-41 | ERSPL | N0 (platform support only) | Live |
| 11 | Consultancy | Enterprises, regulators, institutions | RS-26 | ERSPL | N1 (conflict register) | Live (B2B) |
| 12 | Data and reporting (aggregated, privacy-safe only) | Tenants (own data); public | RS-48, RS-49, RS-35; RS-54 prohibited | ERSPL | N1 (RS-49) / N4 (RS-54) | RS-48, RS-35 live; RS-49 OFF |
| 13 | Events | Professionals, businesses, sponsors | RS-23 | ERSPL | N1 (sponsor screening, deny X-10) | Live |
| 14 | Publications | Practitioners | RS-24 | ERSPL | N0 | Live |
| 15 | Hearing-room rental | Ad hoc tribunals, advocates, chambers, mediators | RS-16, RS-17 | ERSPL; venue partner | N0 / N1 | RS-16 at P04 GA; RS-17 OFF |
| 16 | API usage | Platforms, enterprises | RS-08, RS-47 | ERSPL | N0 | Live |
| 17 | White-label | Enterprises (party portal); chambers and institutions (practice software) | RS-08 (enterprise white-label portal), RS-36 (practice software rental) | ERSPL | N0 | Live |
| 18 | Memberships and forum | Individuals; companies, firms, associations | RS-13, RS-14 | ERSPL | N1 (Forum, disclosed) | Live (post-nominals OFF) |
| 19 | Business plans | MSMEs | RS-12, RS-32 | ERSPL | N1 | RS-32 live; RS-12 OFF (AB-R6) |
| 20 | Partners, group cross-sell | Non-professional partners; group companies | RS-28, RS-55; RS-29 prohibited | ERSPL pays partners; intercompany | N1 | RS-28 live; RS-55 OFF |
| 21 | Advertising | Non-legal B2B vendors | RS-25 | ERSPL | N2 | OFF |
| 22 | Operations Platform resale; careers board | Other ADR centres; employers | RS-33, RS-34 | ERSPL | N0 | OFF |

### AB.1.3 Money flows and the firewall (text diagram)

```
PARTIES / ENTERPRISES ──(case fees, programme fees)──► ERSPL ledger (revenue_owner = equator)
        │                                               │
        └──(neutral fees, routed; T09–T12)────────────► Neutral (revenue_owner = neutral) — never discounted (App. B P2)
SETTLEMENT MONIES ──► bank escrow / trustee (NN-13) — never ERSPL's merchant account
CHAMBERS TENANT ──(subscription, rental, add-ons)──► ERSPL ;  tenant's own clients ──(tenant fees)──► tenant (Route)
MARKETPLACE BUYER ──(booking)──► PA transfer hold (AA §AA.7.1) ──► provider − take (non-advocate); buyer pays flat fee line (advocate-neutral, X-62)
SPONSOR (non-advocate neutral) ──(sponsored listing, RS-19, OFF)──► ERSPL   ┆ FIREWALL ┆  allocation, eligibility,
ADVERTISER (RS-25, OFF) ──► ERSPL                                           ┆ (NN-34)  ┆  Quality Index, grading,
LEARNER ──(course fee)──► Institute operator (separate merchant) — ERSPL ₹0  ┆          ┆  conflicts, institutional
GROUP COMPANY ◄──(intercompany, s.188, GDSA)──► ERSPL                       ┆          ┆  directory: no read path to rev/mkp/billing
```

---

## AB.2 Revenue Stream Registry (`rev` schema)

### AB.2.1 Record model

A stream has one header row (`rev.streams`: code, name, family) and many **versions** (`rev.stream_versions`). Everything that can change — scope, bounds, entitlements, tax, legal dependencies, rating, KPIs — lives on a version. Exactly one version per stream may be `live` in a given scope at a time; a superseded version stays readable for audit and for contracts pinned to it (NN-21). Status transitions are append-only rows in `rev.stream_transitions`.

### AB.2.2 Field catalogue

Tier: **L** locked platform guardrail · **G** governed (maker ≠ checker, source citation, effective dates, preview, rollback, review date) · **T** tenant (only for streams flagged `tenant_configurable`) (NN-33).

| # | Field | Type / values | Meaning | Tier | Maker → checker |
|---|---|---|---|---|---|
| 1 | `code` | `RS-nn` (stable; never reused) | Registry code (§AB.3) | L | platform_admin (seed only) |
| 2 | `slug`, `name_i18n` | text; jsonb | Internal and public names (en, hi; other languages via legal-translator review, NN-23) | G | revenue_manager → marketing_manager (copy) + legal_reviewer |
| 3 | `family` | `case_fee`, `programme`, `saas_subscription`, `rental`, `usage`, `payg_credit`, `one_time_product`, `professional_service`, `membership`, `marketplace_take`, `sponsored_listing`, `advertising`, `event`, `publication`, `partner_payout`, `related_party`, `data_product`, `free_public_good` | Drives defaults for refund code, revenue recognition and tax | L after creation | — |
| 4 | `segment[]`, `buyer_kind[]` | `individual`, `sme`, `organisation`, `enterprise`, `institution`, `neutral`, `chambers`, `advocate`, `partner`, `group_company`, `public` | Who may buy | G | revenue_manager → cfo |
| 5 | `value_statement_i18n` | jsonb | Plain-language value to the payer (source for explanation pages) | G | revenue_manager → legal_reviewer (Claims Register check, NN-17) |
| 6 | `pricing_unit` | `per_case`, `per_stage`, `per_seat_month`, `per_seat_year`, `per_tenant_month` (rental), `per_employee_month`, `per_use`, `per_page`, `per_copy`, `per_instrument`, `per_listing_month`, `per_slot_month`, `per_room_hour`, `per_ticket`, `per_1000_calls`, `pct_of_eligible_booking`, `flat_per_booking`, `one_time_fee`, `annual_licence`, `credit_pack`, `day_rate`, `fixed_project_fee`, `free` | How it is priced | G | revenue_manager → cfo |
| 7 | `cadence` | `transactional`, `monthly`, `annual`, `term`, `on_order`, `on_event`, `project_milestone`, `monthly_statement` | Billing cadence | G | revenue_manager → cfo |
| 8 | `price_bounds` | `{currency, min_minor, max_minor, unit}` per scope | Board-approved band; every schedule version must sit inside it | G | revenue_manager → cfo → Board where §AB.6.5 requires |
| 9 | `schedule_links[]` | FKs to `core.fee_schedules`/`core.plans`/`core.plan_prices` versions | Where the actual figures live (Appendix B) | G | fin.controller |
| 10 | `entitlements[]` | feature keys with limits (Appendix O §4.2 format) | What the buyer gets; limits and overage | G | revenue_manager → cfo |
| 11 | `plan_membership[]` | plan and package codes | Which plans or packages include the stream (§AB.4) | G | revenue_manager → cfo |
| 12 | `revenue_owner` | `equator`, `neutral`, `tenant`, `institute_operator`, `group_company:<id>` | Who books the revenue | L after approval | — |
| 13 | `tax_profile` | `{sac, gst_treatment (T01–T17 per App. B §B.4/§B.10), rcm_possible, eco_tcs_applicable, eco_tds_applicable, payer_tds_section, tax_memo_ref}` | Tax treatment; SAC and treatment codes from Appendix B; anything not in B carries `tax_memo_ref = pending` and blocks `live` for B2C | G | finance_ops → tax adviser sign-off (document) → cfo |
| 14 | `refund_code`, `cancellation_terms`, `renewal_terms` | `RP-*` (App. B §B.8; new codes §AB.5); auto-renew default; notice days | Refund, cancellation and renewal (U-7) | G | revenue_manager → cfo; U-7 owner confirms |
| 15 | `cost_drivers[]` | refs to `rev.cost_inputs` with quantity formula | Cost-to-serve model (§AB.6.1) | G (private) | finance_ops → cfo |
| 16 | `legal_dependencies[]` | `{kind: legal_rule / counsel_opinion / board_resolution / related_party_approval / vendor_contract / regulator_status / unconfirmed_fact, ref, status, review_date}` | Appendix G LR IDs, opinion records, resolution numbers and dates | G | legal_reviewer / company_secretary → compliance_officer |
| 17 | `neutrality_rating` | `N0`…`N4` (§AB.2.4) | Conflict-with-neutrality rating | L for N3/N4; G for N0–N2 | compliance_officer → legal_reviewer |
| 18 | `professional_rule_flags[]` | `advocate_excluded`, `ca_cs_cma_excluded`, `no_referral_reward`, `flat_fee_only_for_advocate_neutrals` | Master X-62 enforcement | L | — |
| 19 | `case_scope_allowed` | `none`, `non_administered`, `administered_parity_safe`, `administered` | Whether the stream may touch an Equator-administered case and on what terms (RA-3) | L for N2+ (`non_administered` max) | compliance_officer |
| 20 | `approver_role`, `approval_refs[]` | role code; refs | Named approver for `approved` and `live` (default per §AB.3) | G | — |
| 21 | `status` | `draft` → `approved` → `live` ↔ `paused` → `retired` (§AB.2.3) | Lifecycle | — | transitions per §AB.2.3 |
| 22 | `kill_switch` | `{engaged bool, scope, reason, engaged_by, engaged_at}` | Emergency stop (§AB.2.5) | — | single authorised user to engage; maker-checker to release |
| 23 | `scopes[]` | jurisdiction (`IN`, `IN-xx` ISO 3166-2, or foreign ISO 3166-1), segment, organisation IDs (allow/deny), tenant type, vertical, channel (`web`, `mobile`, `ops`, `api`) | Where the version may be live (§AB.2.6) | G | revenue_manager → cfo |
| 24 | `tenant_configurable` | bool + bounds | Whether a tenant admin may switch the stream on/off or set its own price inside bounds | L (set at approval) | — |
| 25 | `price_test_policy` | `{allowed bool, max_arms, band_min, band_max, eligible_segments}` | A/B price tests (§AB.2.7) | G | revenue_manager → cfo; Board approves the policy |
| 26 | `kpis[]` | refs to `rev.kpi_definitions` with targets and kill thresholds | Adoption, ARPA, gross margin, churn, CAC payback, and stream-specific KPIs (§AB.2.8) | G | revenue_manager → cfo |
| 27 | `review_cadence` | `monthly` (first two quarters), then `quarterly`; `annual_board` | Viability review (§AB.7.2) | G | — |
| 28 | `public_explanation` | `{summary_i18n, what_you_get_i18n, what_it_never_affects_i18n, faq_i18n, show_on_how_we_earn bool}` | Source for generated customer pages (§AB.2.9) | G | marketing_manager → legal_reviewer |
| 29 | `effective_from`, `effective_to`, `review_date`, `version`, `supersedes_version` | dates; int | Versioning (NN-21) | G | — |
| 30 | `internal_notes` | text (private) | Rationale, benchmarks used ([RB], [RA] references) — never rendered publicly | G (private) | — |

### AB.2.3 Status state machine

```
           propose                approve (checker; gates)           go-live (checker; scope)
 [draft] ───────────► [draft:in_review] ──────────────► [approved] ─────────────────────────► [live]
    ▲  reject (reasons)        │                              │                                 │  ▲
    └──────────────────────────┘                              │ retire (no live scope)          │  │ resume (maker-checker;
                                                              ▼                                 ▼  │  gates re-checked)
                                                          [retired] ◄──── retire (run-off done) [paused]
                                    kill switch engaged ⇒ forced [paused] with killed = true (any scope)
```

| From → To | Actor (maker / checker) | Guards (all must pass) | Effects |
|---|---|---|---|
| `draft` → `draft:in_review` | revenue_manager | Required fields 1–20 present; neutrality rating set; `case_scope_allowed` consistent with rating | Review tasks to checker, legal_reviewer (if N1+), compliance_officer (if N2+), company_secretary (if related party) |
| `in_review` → `draft` (reject) | Any reviewer | Reason text ≥ 20 characters | Returns to maker |
| `in_review` → `approved` | Checker per §AB.3 approver column; maker ≠ checker (NN-36) | Every `legal_dependencies[]` row in `satisfied` state; N2 requires counsel opinion + Board resolution reference; related-party requires s.188 approval reference; `tax_profile.tax_memo_ref` present (B2C streams); price bounds inside Appendix B approved figures; `revenue-denylist` passes on all tags and copy | `equator.rev.stream.approved.v1`; explanation page draft generated |
| `approved` → `live` (per scope) | Maker proposes scope; checker approves | Linked schedule versions `published`; kill switch not engaged in that scope; dependent feature flags ON; for marketplace streams Appendix AA surface live; for N2, annual dark-pattern self-audit current (E-Commerce Amendment Rules 2026 r.4(15) as reported **[VERIFY — open: Gazette text; commencement reported 1 Jan 2027]**) | CMS price blocks and CTAs become renderable; quote and checkout allowed; event `.status_changed.v1` |
| `live` → `paused` | Maker proposes; checker approves (planned pause) | Reason; communication plan for affected customers | New sales stop at `effective_at`; existing obligations continue (run-off) |
| `paused` → `live` | Maker; checker | All `approved` guards re-run against current dependencies; kill switch released | Sales resume |
| `live`/`paused` → `retired` | Maker; checker (cfo); Board if the stream carried a Board resolution | No active subscriptions or open obligations, or a run-off plan with end date and customer notices ≥ 30 days (subscriptions, O AR-8) | Stream code frozen; never reused |
| Any → forced `paused` (kill) | One authorised user: cfo, compliance_officer, ops_director, legal_reviewer, or platform_admin on their instruction | Reason code (`legal`, `regulator`, `neutrality_incident`, `pricing_error`, `security`, `vendor_failure`, `reputational`, `board_direction`) | §AB.2.5 |

Transitions are idempotent, write `rev.stream_transitions` (append-only, hash-chained into the audit log, NN-22) and are mirrored in the un-disableable edit log for billing and pricing tables (NN-36; Companies (Accounts) Rules 2014 r.3(1) proviso).

### AB.2.4 Neutrality rating (conflict-with-neutrality)

| Rating | Meaning | Allowed case scope | Approval gate | Examples |
|---|---|---|---|---|
| **N0** | No credible effect on independence or party equality | Any, subject to RA-3 parity for administered cases | cfo | GRM SaaS, publications, implementation services |
| **N1** | A paid relationship that a counterparty could perceive as influence; acceptable with disclosure and uniform published terms | Any, with `CommercialRelationshipNotice` (RA-7) on the counterparty's case view | cfo + legal_reviewer | Lender programme, Users' Forum, consultancy, events with sponsors |
| **N2** | Commercial visibility or a take linked to neutrals' work; allowed only on a separate surface, never readable by appointment | `non_administered` only | Board resolution + counsel opinion + compliance_officer; annual dark-pattern self-audit | Marketplace take, sponsored listing, advertising |
| **N3** | Prohibited in administered work; allowed elsewhere only with Board + counsel | `non_administered` only; never on surfaces visible in administered cases | Board + counsel; locked by default | (none at launch; reserved) |
| **N4** | Prohibited everywhere (deny-list) | none | Cannot leave `draft` (`REV_STREAM_PROHIBITED`) | Lead fees, advocate referral rewards, paid badges, case-data licensing |

Rules: the rating is set by `compliance_officer`, reviewed by `legal_reviewer`, and can only be **raised** without Board approval; lowering N2+ needs a Board decision-log entry. The finance dashboard shows a **neutrality-exposure tile** — share of revenue from N1 and N2 streams, by vertical, monthly ([RB] A.7).

### AB.2.5 Kill switch

| # | Rule |
|---|---|
| KS-1 | **Who:** one authorised user (cfo, compliance_officer, ops_director, legal_reviewer; platform_admin on recorded instruction) may engage without a checker. Release requires maker-checker and re-runs all `approved` guards. |
| KS-2 | **Scope:** whole stream, or any combination of jurisdiction, segment, organisation, tenant type, vertical and channel. |
| KS-3 | **Effect within 5 minutes (p95 ≤ 60 s):** the config bus publishes `equator.rev.stream.killed.v1`; caches (`EntitlementService`, quote engine, CMS renderer, CPQ, campaign engine) invalidate on receipt and fall back to "deny new sale" if the bus is unavailable for > 60 s for any N2 stream (fail-safe). |
| KS-4 | **What stops:** new quotes, checkouts, plan sign-ups, upgrades into plans containing the stream, coupon redemption, CMS price blocks and CTAs (replaced by a neutral "Not available at present" block, no reason shown publicly), Ops Platform campaigns and sequences referencing the stream (AU-05/AU-07/AU-14 paused), sponsored slots and ads (removed from render). |
| KS-5 | **What continues (run-off):** paid-for entitlements until period end; live hearings; case clocks; delivery of one-time products already paid (or automatic refund if delivery itself is the problem); never-suspend list (Appendix O §7.1 a–j). Renewals of a killed stream do not proceed; customers receive the renewal notice with "This service will not renew" and the refund code. |
| KS-6 | **Notifications:** stream owner, cfo, compliance_officer, Board secretary (for N2 or Board-resolution streams) within 15 minutes; customer notices only through approved templates. |
| KS-7 | **Evidence:** kill and release events are hash-chained; a post-incident review is mandatory within 10 working days for reasons `neutrality_incident`, `legal`, `regulator` and `pricing_error`. |

### AB.2.6 Scope model

Scope dimensions combine with AND; lists within a dimension combine with OR. Defaults: `jurisdiction = IN`, `channel = all`, `vertical = all`, `organisation = all`. Rules:

1. **Jurisdiction:** a stream with state-dependent law (e-stamp, professional tax for RS-10, stamp duty) lists the states in which its rule packs are `published` (e.g., `rulepack.IN-RJ.stamp.duty@2026.1`); other states are excluded automatically (`REV_JURISDICTION_NOT_ENABLED`).
2. **Foreign buyers:** INT streams follow Appendix B §B.6 currencies and NN-19 sanctions screening; streams without an export tax profile cannot be live outside `IN`.
3. **Organisation allow/deny lists:** used for pilots, enterprise-specific bundles and exclusions (e.g., a sponsor excluded for an open Equator-administered matter with the searching party — Appendix AA).
4. **Segment:** consumer segments (`individual`, `sme` without GSTIN) inherit the consumer display and refund rules (Appendix O §6.4; RP-SUB cooling-off).
5. **Case scope:** see field 19; the entitlement evaluator denies a stream in `case_scope = 'administered'` unless `case_scope_allowed ∈ {administered_parity_safe, administered}` (RA-3).
6. **Tenant scope:** for `tenant_configurable` streams, the tenant's own toggle narrows but never widens the platform scope.

### AB.2.7 A/B price tests within approved bounds

Flag `platform.rev.price_tests.enabled` **OFF** until the Board approves a price-testing policy and counsel confirms the position under the Consumer Protection (E-Commerce) Amendment Rules 2026 (search and price manipulation, r.4(11)(c) as reported) and the Dark Patterns Guidelines 2023 **[VERIFY — open]**. When ON:

| # | Rule |
|---|---|
| PT-1 | Allowed only for **B2B self-serve SaaS plans and add-ons** (buyer with GSTIN or organisation account). **Never** for case fees, neutral fees, regulated schedules (SEC), consumer (individual/SME-without-GSTIN) prices, concessions, refunds, or any price shown inside a case, hearing, signing or payment view. |
| PT-2 | Every arm's price lies inside the version's `price_bounds`; at most 2 arms (`platform.rev.price_tests.max_arms`); maximum duration 60 days. |
| PT-3 | Assignment is per **organisation**, persisted at first exposure, never by inferred personal attributes, location below state level, device or browsing history. |
| PT-4 | The price shown is the price charged (quote hash = checkout, Appendix O DP-07). |
| PT-5 | **Honour rule:** when the test ends, any organisation that bought at a higher arm than the adopted price moves to the adopted price from its next billing cycle, and the difference for the test period is credited if the adopted price is lower. |
| PT-6 | Tests on **packaging and presentation** (names, bundle composition, order of cards) use the same rules except PT-5. |
| PT-7 | Each test has a test record (hypothesis, arms, sample size, stop rule), maker-checker approval and a results memo filed to the viability review. |

### AB.2.8 KPI definitions (stored in `rev.kpi_definitions`; computed in `reporting.rev_*` views)

All KPIs are computed from the ledger, usage aggregates and CRM opportunity data; no case-identifying data leaves `core` (NN-16). Definitions extend Appendix O §1.4.

| KPI | Definition / formula | Applies to |
|---|---|---|
| Adoption | Paying accounts using the stream in period ÷ eligible accounts in scope | All paid |
| Attach rate | Cases (or tenants) buying the stream ÷ cases (tenants) eligible | One-time products, add-ons |
| ARPA | Revenue of the stream in period ÷ paying accounts (monthly normalised) | Recurring |
| MRR / ARR | Appendix O §1.4 | Recurring |
| Gross margin % | (Revenue − direct cost-to-serve per §AB.6.1, excluding neutral pass-through and pure-agent items) ÷ revenue | All |
| Contribution margin | Gross margin − allocated sales, onboarding and success time | All |
| Logo churn | Accounts cancelled or expired in period ÷ accounts at period start | Recurring |
| Revenue churn / NRR | Appendix O §1.4 | Recurring |
| CAC | Sales + marketing cost attributed to the stream (CRM-sourced, Ops Platform) ÷ new paying accounts | B2B streams |
| CAC payback (months) | CAC ÷ (monthly ARPA × gross margin %) | B2B streams |
| Take-rate realised | Marketplace take revenue ÷ eligible GMV | RS-18 |
| Complaint rate | Complaints and grievances tagged to the stream ÷ paying accounts (or ÷ 1,000 impressions for RS-19/RS-25) | All, mandatory for N1+ |
| Refund rate | Refunds ÷ revenue | All |
| Neutrality incidents | Count of substantiated complaints or audit findings that the stream affected independence or party equality | N1+ (target 0; any incident triggers review) |
| Time-to-value | Days from contract to first value event | Implementation, onboarding, SaaS |

### AB.2.9 Customer-facing explanation pages

1. Pages are **generated** from `public_explanation`, `pricing_unit`, linked published schedules (prices rendered per Appendix O §6.4), `refund_code` summary (U-7 text) and `what_it_never_affects_i18n`. Hand-written price copy is blocked by the CMS linter.
2. Only versions in `approved` (preview) or `live` (publish) may generate pages; a page whose source version is no longer live is unpublished within 5 minutes (`REV_EXPLANATION_STALE`).
3. **`/trust/how-we-earn`** lists live streams grouped by payer ("What parties pay", "What organisations pay", "What professionals pay", "What we never charge for", "What we never sell"), with the neutrality note for each N1/N2 stream and a link to the deny-list. Sponsored listings and advertising, if ever live, are described there with their labels and caps.
4. Every page shows the approval badge ("Subject to Board approval" until the schedule is Board-approved) and the effective date.
5. Comparative statements about competitors on these pages require Appendix T §0.4 benchmark entries (NN-17); none are generated automatically.

### AB.2.10 Maker-checker and privacy of internal data

- Maker ≠ checker on every version, transition (except kill), price change, coupon above threshold, price test and related-party record (NN-36). Self-approval is blocked (`REV_MAKER_CHECKER_SAME_USER`).
- **Private columns:** `cost_drivers`, `internal_notes`, KPI actuals for margin, CAC and contribution, and `rev.cost_inputs` rates are readable only by `finance_ops`, `accounts_checker`, `cfo`, `internal_auditor`, `compliance_officer` (read) and Board-pack exports. Column-level grants plus RLS; API responses for other roles omit the fields (`REV_COST_DATA_RESTRICTED` on direct request).
- Tenants never see Equator's internal cost or margin data; a tenant sees its own bills, usage and, for its own tenant fees, its own revenue reports.
- Exports of internal cost and margin data are sensitive exports under NN-36 (maker-checker, watermark, logged).

---

## AB.3 Stream catalogue RS-01…RS-57

Codes RS-01…RS-35 keep the numbering of [RB] §C so research traceability is preserved; RS-36…RS-57 are added here (§AB.3.5 lists every change against [RB]). Figures are in Appendix B cards or are "Board" (not yet priced). "Default" is the launch default per scope `IN`. Every row is seeded into `rev.streams`/`rev.stream_versions` by migration `rev_v3_seed` with status `draft`; rows marked ON move to `approved`/`live` only through §AB.2.3.

### AB.3.1 Commercial view

| Code | Stream | Segment / buyer | Value to payer | Pricing unit | Cadence | Plans / packages | Entitlements and limits |
|---|---|---|---|---|---|---|---|
| RS-01 | Case fees: registration, administration; neutral fees as pass-through | Parties; enterprise payers | Administered process with a published card | per_case / per_stage; ad valorem bands per card | transactional | Cards FIN-R, COM-STD, FAM-STD, INS-RET, INS-COM, WRK-STD, INT-USD, INT-MED | Inclusions per App. O §2.1.1; first certified copy ₹0 |
| RS-02 | Settlement administration fee (B2B opt-in) | Business parties only | Drafting, signing, recording a settlement | per_case on signed settlement | transactional | COM-M, INT-M | Only where every party is a business and opted in at filing |
| RS-03 | Lender/NBFC programme | Banks, NBFCs, HFCs, MFIs | Bulk ODR, notices, execution packs | per_stage + volume tier + API | monthly | FIN-L + EAPI + GRM-LENDER | Borrower ₹0; no appointment rights (O `appointment_rights = false`) |
| RS-04 | Insurer programme | Insurers | Settlement days, claims mediation | annual_licence + per_case overage | annual + usage | INS-SUB | Policyholder ₹0; no arbitration against retail policyholders |
| RS-05 | Employer programme | Employers | Workplace ODR | per_case + tier | monthly | GRM-EMPLOYER + WRK-STD (`employer_pays`) | Employee ₹0 in bulk programmes |
| RS-06 | GRM SaaS (lender, listed, employer, university) | Regulated entities, listed companies, employers, HEIs | Grievances answered inside regulator clocks | per_tenant_month tier + per_ticket overage | monthly / annual | GRM-* | Intake never stops at allowance (RA-6) |
| RS-07 | POSH/IC SaaS and IC services (incl. external member via marketplace) | Employers, HEIs | Lawful, sealed IC operation | per_tenant_year band + per service | annual + one-time | POSH-* | Complainant ₹0; open inquiry never blocked (NN-07) |
| RS-08 | Enterprise API, white-label party portal, Clause Registry, BYOK | Platforms, enterprises | Embedded ODR | per_tenant_month + per_1000_calls; annual_licence add-ons | monthly / annual | EAPI-*; add-ons | White-label beside Equator's identity (O §2.7) |
| RS-09 | Private ADR Chambers subscriptions | Independent neutrals, chambers, firms, institutions | Own-brand practice workspace | per_seat_month / per_seat_year; per_case beyond allowance | monthly / annual | CH-LITE, CH-SOLO, CH-PRO, CH-INST | Allowances per O §2.8; run-off 90 days |
| RS-10 | Chambers HR-lite and payroll add-on | Chambers with staff | Staff records, attendance, leave, payroll, payslips | per_employee_month | monthly | Add-on to CH-SOLO and above | Tenant is employer of record; NN-35, NN-36 apply |
| RS-11 | Counsel workspace | Advocates, firms | One place for all Equator matters | per_seat_month / year | monthly / annual | COUNSEL-FREE (₹0), COUNSEL-PRO, FIRM-ENT | No procedural advantage (RA-3); no solicitation features |
| RS-12 | Business Assure | MSMEs | Clause kit + prepaid case credits | annual plan | annual | BIZ-ASSURE-START / GROW / PLUS | Credits redeemable on Equator lines only (O-R6) |
| RS-13 | Neutral membership ladder | Individuals | CPD log, events, library | annual fee | annual | MEM-* | Never read by grading or allocation (RA-4) |
| RS-14 | Users' Forum | Companies, firms, associations | Rules consultation, briefings | annual tier | annual | FORUM-* | Member list published; disclosed in cases |
| RS-15 | Case documents and services (umbrella): transcripts, execution pack, hearing bundle, apostille, registration facilitation, eSign, Explorer human review, process consultation | Requesters (parties, counsel) | Documents and services around a case | per item / page / hour | on_order | ANC.* (O §2.1) | Same price for every party in a case (parity) |
| RS-16 | Virtual hearing-room rental for non-administered matters | Ad hoc tribunals, advocates, chambers, mediators | Secure room with caucus; recording only for arbitration with all-party consent (NN-11) | per_room_hour / day; packs | on_order (PAYG) | Room packs; CH-* add-on | Label "Room hosted on Equator — Equator does not administer this matter" |
| RS-17 | Physical venue partner bookings | Parties needing in-person hearings | Booked rooms at partner venues | commission from venue | transactional | — | Partner status disclosed at booking |
| RS-18 | Marketplace take on private-practice bookings | Chambers tenants; non-advocate neutrals; ancillary service providers (scope `service_providers`) | Payment, escrow, scheduling, documents | pct_of_eligible_booking (Lite/Solo 15%, Pro 12%, Inst 10% — O-R2, Board; service providers `marketplace.take_rate.service_providers` 10%, Board); flat_per_booking for advocate-neutrals, charged to the buyer (X-62) | monthly_statement | CH-* | 0% on administered cases (B §B.7.7); flat and uniform (deny X-19) |
| RS-19 | Sponsored listing — Private Practice Marketplace | Non-advocate private-practice neutrals and chambers | Visibility in a separate labelled slot | per_slot_month per geography and practice area; equal rate card | monthly | Never bundled with plans | ≤ 2 slots per page; label "Sponsored — paid placement. Does not affect Equator appointments." |
| RS-20 | Lead, per-enquiry or pay-to-bid fees | — | — | — | — | — | **Prohibited** |
| RS-21 | EQAP sitting fee | Neutral candidates from any training provider | Competence assessment | per sitting | one-time | — | Identical for every provider (CN-04); no Academy discount |
| RS-22 | Institute related-party arrangements (referral, co-marketing, shared services) | Institute operator | Introductions, shared services | flat per enrolment (never linked to empanelment) or arm's-length cross-charge | monthly / quarterly | — | ≥ 3 providers on any referral card; disclosed (D3-38) |
| RS-23 | Events and conferences | Professionals, businesses, sponsors | Learning, networking | per ticket / exhibitor package / sponsorship | on_event | Member pricing (MEM-*) | Sponsorship register; true capacity only |
| RS-24 | Publications (guides, rules commentary, templates) | Practitioners | Know-how | per title / bundle | one-time | MEM-* library | India ADR Report free; no case data |
| RS-25 | Advertising and sponsored content on public CMS pages | Non-legal B2B vendors | Reach | per_slot_month or per 1,000 impressions | monthly | — | Never on case, directory, neutral, fee, grievance or POSH pages; no ads by advocates, law firms, CAs, CSs, CMAs, neutrals, chambers, ADR institutions, lenders, insurers or other repeat players (Appendix AA §AA.10.8) |
| RS-26 | Dispute-system design and GRM implementation consultancy | Enterprises, regulators, institutions | Scheme design, rules, SOPs | day_rate / fixed_project_fee | project_milestone | — | Never advises a side in a dispute (deny X-01) |
| RS-27 | Implementation and integration services | Enterprises, chambers | Faster go-live: LOS/LMS, HRMS, SSO, connectors | fixed_project_fee / day_rate | project_milestone | RS-40 packages | Statement of work with acceptance criteria |
| RS-28 | Partner and reseller programme (non-professional partners) | Payer is ERSPL; partners are software vendors, chambers of commerce, industry associations | Revenue share | % of first-year subscription | quarterly | — | No advocates, CAs, CSs, CMAs (X-62); disclosed on the referred tenant |
| RS-29 | Referral rewards to advocates, bar bodies, CAs, CSs, CMAs | — | — | — | — | — | **Prohibited** |
| RS-30 | Professional Panel Register — private panel-management mode | Lenders, enterprises managing their own panels | Onboarding, verification status, matter routing, fee tracking for own panel | per_tenant_month + per_seat | monthly / annual | Add-on to GRM-LENDER, EAPI, group-company tenants under GDSA | Tenant-private, `noindex`, no ratings shown (NN-39) |
| RS-31 | Public search of advocates and professionals | Public | Find a professional | free | — | — | Free to professionals and public; any fee **prohibited** |
| RS-32 | Pay-as-you-go wallet and credit packs | Individuals, MSMEs, chambers (usage credits) | Prepay for products and usage | credit_pack | on purchase | Usable across plans | No auto top-up by default; expiry disclosed; Equator lines only (O-R6) |
| RS-33 | Operations Platform resale (Infrabyx Work OS) | Other ADR centres, institutions | Back-office suite | per_seat_month | monthly | — | Tenant isolation (NN-38) |
| RS-34 | Careers and job board | Chambers, institutions (employer pays) | Hiring | per listing | one-time | — | No fee from job seekers |
| RS-35 | Aggregate statistics and India ADR Report | Public | Transparency | free | quarterly / annual | — | k ≥ 10 suppression (master X-28) |
| RS-36 | White-label practice software — monthly tenant rental | Chambers, institutions, bar associations, universities | Branded instance of the practice suite (own domain, rules, panel) rented per tenant | per_tenant_month rental (+ contracted share for managed secretariat, CH-IAAS lineage) | monthly (annual contract) | CH-IAAS; "Practice Suite Rental" packages | Naming guardrail (P10 FR-P10-01); run-off 90 days |
| RS-37 | Page themes for Chambers and neutral public pages | Chambers tenants, independent neutrals | Additional visual themes and layouts | one_time_fee or per_tenant_month | one-time / monthly | Add-on for CH-SOLO and above (Appendix W §W.9) | Never affects ranking or listing; no "premium" wording on public pages (deny X-18); WCAG 2.2 AA (NN-23; Appendix W CHL-L17) |
| RS-38 | Custom domains | CH-SOLO tenants (included in CH-PRO and CH-INST; never CH-LITE — Appendix O FR-P10-V2-O1; Appendix W §W.3.5) | Own domain with TLS | per_tenant_month | monthly | Add-on | DNS verification; Equator identity in footer retained |
| RS-39 | Data migration services | Enterprises, chambers, institutions | Records moved from spreadsheets and other ODR, CRM or HR tools | fixed_project_fee per source | project_milestone | RS-40 packages | Migration rehearsal (NN-40); originals preserved (NN-37) |
| RS-40 | Onboarding packages | New tenants | Self-serve (₹0), Guided, White-glove setup and training | one_time_fee | one-time | Optional with plans | Every package item listed (no basket sneaking, DP-02) |
| RS-41 | Customer-success and premium support tiers | Tenants | Faster platform support, named CSM, QBRs | per_tenant_month or % of ARR | monthly / annual | Standard (included), Priority, Dedicated | Platform support only; never case-administration priority, grievance priority or procedural speed |
| RS-42 | Additional certified copies | Parties | QR-verifiable certified copies | per_copy | on_order | ANC.CERT.COPY | First copy of each outcome ₹0 (deny X-14) |
| RS-43 | Translation (business convenience; certified) | Business parties; individuals beyond 100 pages | Labelled translations (NN-32) | per_page; certified at actuals + 10% | on_order | ANC.TRANSL.* | ₹0 to 100 pages per individual party per case |
| RS-44 | Verified type copies | Parties | Secretariat-verified true type copies | per_page; minimum per order | on_order | ANC.TYPECOPY.VERIFIED | AI type copy ₹0 within fair use |
| RS-45 | e-Stamp facilitation (procurement; franking, e-SBTR, stamp paper) | Parties, tenants | Correct duty procured and attached | per_instrument + duty at actuals | on_order | ANC.ESTAMP, ANC.STAMP.PHYSICAL | State-wise availability |
| RS-46 | Notarisation facilitation | Parties needing notarised documents | Notarisation arranged through a partner notary | per_instrument + notary fee at actuals | on_order | — | Equator never notarises |
| RS-47 | API overage | EAPI tenants; CH-INST | Calls beyond allowance | per_1000_calls | monthly in arrears | EAPI-*, CH-INST | Technical rate limits are separate from billing |
| RS-48 | Tenant own-data analytics and MIS premium | Enterprise, GRM and chambers tenants | Advanced dashboards and scheduled MIS on the tenant's own data | per_tenant_month | monthly | Add-on; included in EAPI-SCALE | Own data only |
| RS-49 | Cross-tenant aggregated benchmark reports | Enterprises, regulators, institutions | Sector benchmarks with k ≥ 10 and no identifiable party, neutral or tenant | per report / annual_licence | annual | — | Never per-party or per-neutral (deny X-09) |
| RS-50 | Listing, featured, ranking or badge fees charged to advocates, CAs, CSs or CMAs | — | — | — | — | — | **Prohibited** |
| RS-51 | Commission or share of advocates' fees, or a percentage of recoveries | — | — | — | — | — | **Prohibited** |
| RS-52 | Buyer processing fee on marketplace bookings | Marketplace buyers | Equator's payment and escrow service | flat_per_booking or disclosed % as a separate line | per booking | — | Never hidden; never on administered cases |
| RS-53 | Paid badges, "verified" labels, sort boosts, "top", "premium", "best", "recommended" labels in any directory | — | — | — | — | — | **Prohibited** |
| RS-54 | Licensing of case-level or pseudonymised case data; per-party or per-neutral statistics | — | — | — | — | — | **Prohibited** |
| RS-55 | Group cross-sell referral fees (Finbyx, Udofin ↔ Equator) | Group companies | Introductions of B2B accounts | flat per converted account at arm's length | quarterly | — | No borrower, case or neutral data used (NN-38) |
| RS-56 | Escrow handling fee | Parties (per card) | Bank escrow with trustee for instalments and deposits | % or flat per card | transactional | Vertical cards | Settlement monies never in ERSPL's merchant account (NN-13) |
| RS-57 | Service-provider tools plan (Private Practice Marketplace) | Ancillary service providers listed on surface (ii) (`mkp.providers.kind = 'service_provider'`); never advocates, CAs, CSs or CMAs (Appendix AA §AA.3.2) | Optional workspace tools: calendar sync, team seats, own-data analytics | per_tenant_month | monthly | Provider plans per Board schedule; never bundled with RS-18, RS-19 or RS-25 | Listing stays free without the plan; never affects ranking, badges, reviews, sponsored eligibility or take (`RANKING_IGNORES_PAID`); cancellation no harder than sign-up |

### AB.3.2 Governance view

Approver = checker for `approved` and `live`. "Tax memo" = the signed tax memo required before go-live (Appendix B §B.10 header); SAC codes not listed in Appendix B §B.10 are **[VERIFY — open: tax memo]** and block `live` for B2C scopes until signed. Refund codes `RP-*` are Appendix B §B.8 or the new codes in §AB.5.

| Code | Default | Rating | Approver | Legal / ethical dependencies | Tax (SAC; TCS/TDS) | Refund / renewal | Cost-to-serve drivers | Kill-switch scope |
|---|---|---|---|---|---|---|---|---|
| RS-01 | ON | N0 | Board (cards); fin.controller (versions) | A&C Act 1996; Mediation Act 2023; App. B P1–P9; NN-18; deny X-07 | 998215, 18% forward (T01–T08); tribunal RCM/exempt (T09/T10); neutral T11/T12; payer TDS s.393(1) Table Sl. 6(iii) | RP-STD-MED, RP-STD-ARB, RP-INS-RET, RP-INS-COM, RP-FIN-L, RP-REG | Notices, video, case-manager time, eSign/eStamp, AI tokens, PG fees | vertical, jurisdiction |
| RS-02 | ON (B2B) | N1 | Board | All-party opt-in at filing; never consumers (deny X-07) | 998215, 18% | RP-STD-MED | Drafting review, eStamp | segment |
| RS-03 | ON | N1 | Board (FIN-L); cfo (contract within card) | RBI KFS instructions (15 Apr 2024); deny X-08; *CORE v ECI-SPIC-SMO-MCML* (SC, 8 Nov 2024); NN-03 | 998215, 18% | RP-FIN-L | Notice volume, postage, hearings, case desk | organisation, vertical |
| RS-04 | ON | N1 | Board | IRDAI instruments; deny X-16; no success fee (NN-18) | 998215, 18% | RP-SUB + RP-INS-* | Batched sessions, interpreters | organisation |
| RS-05 | ON | N1 | Board | Labour Codes (in force 21 Nov 2025 per [RE] F5.3); POSH Act 2013 | 998215, 18% | RP-STD-MED / RP-STD-ARB | Sessions, interpreters | organisation |
| RS-06 | ON | N0 | cfo (within Card GRM) | Regulator clocks (RBI, SEBI LODR/SCORES, UGC 2023) | 998315 or 997331 (tax memo); payer TDS Sl. 6(iii) | RP-SUB | Hosting, messaging, support | segment |
| RS-07 | ON | N0 | cfo | POSH Act 2013 and Rules; NN-07; B §B.7.7 "POSH external-member engagement" 15% (the P09 curated external-member flow — not the Private Practice Marketplace, master X-59(d)) | SaaS per tax memo; member fees per B §B.10 | RP-SUB | External-member time, sealed storage | segment |
| RS-08 | ON | N0 | cfo | Naming guardrails (NN-03, NN-17) | 998315 or 997331; payer TDS Sl. 6(iii) | RP-SUB | Support, SLA credits | organisation |
| RS-09 | ON | N0 | cfo; Board for a new plan | Chambers terms mirror the Code; RA-4 | SaaS per tax memo | RP-SUB (14-day cooling-off for individuals/SMEs) | Storage, video, support | tenant type |
| RS-10 | OFF | N0 | cfo + compliance_officer | Labour Codes as notified by states; professional tax and Shops & Establishments rule packs; TDS on salary; DPDP; payroll UAT pass | SaaS per tax memo | RP-SUB | Payroll engine, rule-pack upkeep, support | jurisdiction (states with published rule packs) |
| RS-11 | ON | N0 | cfo | BCI r.36 (no solicitation features); master X-62 | SaaS per tax memo; payer TDS | RP-SUB | Storage, support | segment |
| RS-12 | OFF (AB-R6) | N1 | Board + counsel (name, O Q-O3) | CPA 2019 s.2(28); deny X-12; closed-system PPI **[VERIFY — open: O Q-O5]** | Plan 18%; credits per tax memo (T16) | RP-SUB | Credits redeemed, reviews | segment |
| RS-13 | ON (post-nominals OFF) | N0 | cfo | Trademark and counsel for post-nominals (O Q-O3) | 18%; SAC per tax memo | RP-SUB (cooling-off) | Events, content | — |
| RS-14 | ON | N1 | cfo | NN-16 disclosure; deny X-05 | 18%; SAC per tax memo | RP-SUB | Events | — |
| RS-15 | ON | N0 | fin.controller | NN-11 (transcripts: arbitration only, all-party consent); NN-32 labels | 998215 / 998599 per line (B §B.10) | O §2.1 product rules; delivery-failure auto-refund | Staff time, OCR, providers | per line |
| RS-16 | OFF until P04 GA | N0 | cfo + ops_director | NN-11; no "court" naming; label that Equator does not administer | SAC per tax memo **[VERIFY]** | RP-ROOM | Video minutes, recording storage, on-call support | channel, segment |
| RS-17 | OFF | N1 | cfo + legal_reviewer | Venue contracts; disclosed partner status | Commission 18% (SAC per tax memo); venue deducts TDS s.393(1) Sl. 1(ii) if applicable | RP-ROOM | Partner management | city |
| RS-18 | ON with marketplace surface (Appendix AA) | N2 | Board (rates) + counsel (advocate-neutral position, [RB] OP-10) | NN-34; E-Commerce Rules 2020 r.4–r.6 and Amendment Rules 2026 **[VERIFY — Gazette]**; IT Rules 2021; BCI Ch. III r.2 | GST on the take at the rate and SAC in the tax memo **[VERIFY — open: O Q-O4]**; GST TCS s.52 0.5% on taxable forward-charge supplies only (not RCM, not exempt) and ITA 2025 s.393(1) Sl. 8(v) 0.1% (₹5 lakh threshold for resident individuals/HUFs with PAN or Aadhaar) where Equator collects consideration (`billing.eco_gst_tcs`, `billing.eco_withholding` OFF pending memo; [RE] F3.4) | RP-MKP | PG fees, trustee, support, fee disputes | jurisdiction, tenant |
| RS-19 | **OFF** (`marketplace.paid_placement`) | N2 | Board + counsel + compliance_officer | NN-34; D3-01; BCI r.36; SLP (C) 25794/2024 pending; E-Commerce Amendment Rules 2026 r.4(12), r.5(3)(f) as reported **[VERIFY]**; Dark Patterns 2023 (disguised advertisement) | 18%; SAC per tax memo **[VERIFY]** | RP-ADS | Ad operations, label audits, monthly self-audit | jurisdiction, practice area |
| RS-20 | **Prohibited** | N4 | — | deny X-17; BCI r.36; NYSBA Op. 1132 reasoning ([RB] [45]) | — | — | — | — |
| RS-21 | ON | N0 | cfo | Appendix N §4.8; CN-04; master X-29 | 18%; SAC per tax memo | RP-ASSESS | Assessors, role-players | — |
| RS-22 | **OFF** (`academy.institute_referral`, `academy.institute_referral_fee`) | N1 | Board (s.188) + company_secretary | Companies Act 2013 ss.2(76), 184, 188 with Rules 2014 r.15(3); s.177 only where mandatory; D3-38; corrections C1–C20 (App. AF) | 18%; SAC per tax memo; TDS per nature | Per agreement | — | — |
| RS-23 | ON | N1 | cfo; compliance_officer for any repeat-player sponsor | deny X-10; CCPA Endorsement Guidelines 2022; true scarcity only (DP-01) | Sponsorship 998397; competition 998596; tickets per tax memo | RP-EVT | Venue, speakers, production | city |
| RS-24 | ON | N0 | cfo | Copyright Act 1957; NN-17; deny X-09 | SAC per tax memo **[VERIFY]** | RP-DIG | Authoring, editing | — |
| RS-25 | **OFF** (`platform.rev.ads.enabled`) | N2 | Board + counsel + compliance_officer | Dark Patterns DP-09 and DP-13 (no third-party ad scripts); CCPA 2022; IT Rules 2021 | 18%; SAC per tax memo **[VERIFY]**; advertiser may deduct TDS | RP-ADS | Ad review, label audits | page tags |
| RS-26 | ON (B2B) | N1 | cfo + legal_reviewer (engagement letter) | Conflict register; disclosure in later cases (RA-7); Advocates Act ss.29, 33 (no legal advice) | SAC per tax memo; payer TDS Sl. 6(iii) | RP-SVC | Senior consultant time (App. Z rates) | organisation |
| RS-27 | ON | N0 | cfo | NN-40 ports and field mapping | SAC per tax memo; payer TDS Sl. 6(iii) | RP-SVC | Engineer and implementation time | organisation |
| RS-28 | ON | N1 | cfo; legal_reviewer confirms partner is not a regulated professional | Master X-62; NN-16 disclosure | Partner's GST (998599); ERSPL deducts TDS s.393(1) Sl. 1(ii) 2% (₹20,000 threshold) | Clawback on refund within 90 days | Partner management | — |
| RS-29 | **Prohibited** | N4 | — | deny X-21; NN-34; master X-62; BCI r.36; ICMAI 2025 referral-network bar ([RE] F1.5) | — | — | — | — |
| RS-30 | **OFF** until D3-05 owner and GDSA | N0 | Board (owner) + DPO + cfo | NN-38, NN-39; DPDP ss.5–8 (substantive duties from 13 May 2027 per [RE] F4.1); BCI r.36; lender outsourcing directions **[VERIFY]**; s.188 for intercompany | SaaS per tax memo | RP-SUB | Verification checks, support | organisation, group company |
| RS-31 | **OFF** (`directory.public_professionals`); any fee prohibited | N4 (fee) | — | NN-39; SLP (C) 25794/2024 | — | — | Moderation | — |
| RS-32 | ON | N0 | cfo | Closed-system PPI **[VERIFY — O Q-O5]**; Ind AS 115 breakage (§AB.4.9) | GST at receipt (T16) per tax memo | Wallet refundable net of dues on termination (RP-SUB) | PG fees | segment |
| RS-33 | OFF | N0 | Board | NN-38, NN-40 | SaaS per tax memo | RP-SUB | Support | — |
| RS-34 | OFF | N0 | cfo | Labour law; DPDP; no fee from job seekers | SAC per tax memo | RP-DIG | Moderation | — |
| RS-35 | ON (free) | N0 | Transparency sub-committee | deny X-09; A&C Act s.42A | — | — | Analytics | — |
| RS-36 | ON | N0 | cfo; Board for a new tier | Naming guardrails; tenant isolation | SaaS per tax memo | RP-SUB (contract) | Hosting, support, secretariat time | tenant type |
| RS-37 | OFF until P10 v3 page builder and accessibility review | N0 | cfo + marketing_manager | NN-34 (themes never readable by allocation); BCI r.36 allow-list for advocate-neutral pages | SaaS per tax memo | RP-DIG | Design upkeep | tenant type |
| RS-38 | ON | N0 | cfo | Naming guardrails | SaaS per tax memo | RP-SUB | Certificates, DNS support | tenant type |
| RS-39 | ON | N0 | cfo | NN-37, NN-40; DPDP processor contract | SAC per tax memo; payer TDS Sl. 6(iii) | RP-SVC | Engineer time, validation | organisation |
| RS-40 | ON | N0 | cfo | Dark Patterns DP-02 | SAC per tax memo | RP-SVC | Onboarding specialist time | segment |
| RS-41 | ON | N0 | cfo | NN-16 (no procedural speed or allocation effect) | SAC per tax memo | RP-SUB | Support and CSM time | segment |
| RS-42 | ON | N0 | fin.controller | A&C Act s.31(5); deny X-14 | 998215, 18% | Non-refundable once issued; Equator errors re-issued free | Registrar time, QES | — |
| RS-43 | ON | N0 | fin.controller | NN-23, NN-32 | 998395, 18% | Delivery-failure refund; Equator errors corrected free | MT tokens, reviewer, translator | language |
| RS-44 | ON | N0 | fin.controller | NN-32 | SAC per tax memo (998215 proposed) | Delivery-failure refund | Secretariat time | — |
| RS-45 | ON in states with published stamp rule packs | N0 | fin.controller | Indian Stamp Act 1899 and state stamp Acts; provider terms | Procurement fee 18% (998599); duty pure agent (T15) | Duty refunded only if the issuer refunds | Provider fee | jurisdiction (state) |
| RS-46 | OFF | N0 | cfo + legal_reviewer | Notaries Act 1952 and Notaries Rules 1956 **[VERIFY — open: whether remote or electronic notarisation is permitted]**; partner contract | Facilitation 18% (SAC per tax memo); notary fee pure agent | Facilitation fee refunded if not arranged | Coordination time | jurisdiction |
| RS-47 | ON | N0 | cfo | — | SaaS per tax memo | Disputes via billing query (O §5.13) | Infrastructure | organisation |
| RS-48 | ON | N0 | cfo | NN-16; DPDP; deny X-09 | SaaS per tax memo | RP-SUB | Analytics compute | organisation |
| RS-49 | OFF | N1 | Board + counsel + Transparency sub-committee | A&C Act s.42A; DPDP purpose limitation; tenant consent in contract | SAC per tax memo | RP-DIG | Analytics, privacy review | segment |
| RS-50 | **Prohibited** | N4 | — | deny X-22; BCI r.36 and the 2008 Schedule; ICAI ESB 23 Oct 2019; ICMAI 2025 | — | — | — | — |
| RS-51 | **Prohibited** | N4 | — | deny X-22; BCI Ch. III r.2, Ch. II r.20; Advocates Act s.45A | — | — | — | — |
| RS-52 | OFF (`marketplace.client_processing_fee`) | N1 | Board + counsel | E-Commerce Amendment Rules 2026 r.5(7) (no bundled fees) as reported **[VERIFY]**; DP-08 drip pricing | 18% Equator supply | RP-MKP | PG fees | jurisdiction |
| RS-53 | **Prohibited** | N4 | — | deny X-03, X-18; *P.N. Vignesh* (Madras HC, 3 Jul 2024) | — | — | — | — |
| RS-54 | **Prohibited** | N4 | — | deny X-09; A&C Act s.42A; DPDP | — | — | — | — |
| RS-55 | OFF | N1 | Board (s.188) + DPO | NN-38; deny X-20; GDSA; s.188 | Intercompany supply between separate taxable persons ([RE] F5.2) | Per agreement | — | group company |
| RS-56 | ON per card | N0 | Board (card) | RBI PA Directions 2025; LR-PAY-001/002; NN-13 | 998599, 18%; bank and trustee charges pure agent | Per card | Trustee and bank fees | vertical |
| RS-57 | **OFF** (`mkp.provider_subscriptions`) | N1 | Board (prices) + cfo + legal_reviewer | NN-34 (plan never readable by ranking, allocation or sponsorship); E-Commerce Rules 2020 r.5(3)(f) and Amendment Rules 2026 r.5(6)–(7) as reported **[VERIFY]**; Dark Patterns 2023 (subscription trap); master X-62 | SaaS per tax memo **[VERIFY]** | RP-SUB (14-day cooling-off for individuals/SMEs) | Hosting, support | jurisdiction, segment |

### AB.3.3 Deny-list additions (extend Appendix O §1.5; CI `revenue-denylist`)

| ID | Not sold | Reason (source) | Instead |
|---|---|---|---|
| deny X-17 | Pay-per-lead, pay-per-enquiry or pay-to-bid charges to advocates, regulated professionals or neutrals | BCI r.36 (direct or indirect solicitation); NYSBA Ethics Op. 1132 reasoning on per-matter "marketing fees" ([RB] §3.2); neutrality | Flat, published SaaS and marketplace fees |
| deny X-18 | Paid or unearned labels such as "top", "premium", "best", "recommended", "featured", "expert" on any person in any directory or marketplace | *P.N. Vignesh v Chairman, BCI* (Madras HC, 3 Jul 2024) ([RE] F1.3); CCPA Misleading Advertisements Guidelines 2022 | "Sponsored" label only on RS-19 slots; badges only from verification records |
| deny X-19 | A take-rate that falls as a neutral's billed fees rise, on any Equator-originated work | Steering incentive ([RB] §3.2 item 7) | Flat take by plan (O-R2) |
| deny X-20 | Marketing use of any data from a case, grievance, POSH or HR record, including group cross-sell | DPDP purpose limitation; NN-16; NN-38 | Separate marketing consent captured outside case journeys |
| deny X-21 | Any referral reward (cash, credit, discount or priority) to advocates, bar bodies, CAs, CSs or CMAs | NN-34; master X-62; BCI r.36; ICMAI Guidelines 2025 ([RE] F1.5) | Equator advertises its own SaaS to professionals on equal terms |
| deny X-22 | Listing, featured, ranking or badge fees charged to advocates, CAs, CSs or CMAs; any commission or share of an advocate's fee or of a recovery | BCI r.36 Schedule; Ch. III r.2; Ch. II r.20; Advocates Act s.45A ([RE] F1.2, F1.4) | Free consent-based registry entry (NN-39); party-side fees only for Equator's own services, priced the same whoever is engaged |

### AB.3.4 Mapping to Appendix O stream codes

| O code | RS code(s) | Note |
|---|---|---|
| S-01 | RS-01 | — |
| S-02 | RS-02 | — |
| S-03 / S-04 / S-05 | RS-03 / RS-04 / RS-05 | — |
| S-06 / S-07 / S-08 | RS-06 / RS-07 / RS-08, RS-47 | API overage split out as RS-47 |
| S-09 | RS-09, RS-36, RS-37, RS-38 | Rental, themes and custom domains split out |
| S-10 / S-11 | RS-11 / RS-12 | RS-12 OFF (AB-R6) |
| S-12 / S-13 | RS-13 / RS-14 | — |
| S-14 | RS-15 (umbrella), RS-42, RS-43, RS-44, RS-45, RS-46 | Children split out so each can be scoped and killed separately |
| S-15 | RS-18, RS-28; RS-29 prohibited | Advocate credits removed (AB-R4) |
| S-16 | RS-22 | ₹0 default (D3-38) |
| S-17 | RS-35 | — |
| (new) | RS-10, RS-16, RS-17, RS-19, RS-21, RS-23–RS-27, RS-30–RS-34, RS-39–RS-41, RS-48, RS-49, RS-52, RS-55, RS-56, RS-57 | RS-21 and RS-56 already existed as card lines; now registered as streams |

### AB.3.5 Changes against the research catalogue ([RB] §C)

| [RB] item | Change here | Reason |
|---|---|---|
| RS-09 "rental of white-label practice software" | Split: RS-09 per-seat subscriptions; RS-36 per-tenant monthly rental | Different pricing unit, contract and kill-switch scope |
| RS-12 Business Assure "ON" | OFF | O §8.6 and O-R7 |
| RS-15 one bundle of products | Umbrella kept; RS-42…RS-46 split out | Separate scope (e.g., state-wise e-stamp) and kill switch |
| RS-18 "ON (Chambers)" | ON only with the Appendix AA marketplace surface; flat fee for advocate-neutrals | NN-34; master X-62 |
| RS-22 training referral fee | Broadened to all Institute related-party arrangements; OFF | D3-38 |
| RS-28 partners incl. CA/CS firms | Non-professional partners only | NN-34; master X-62 |
| RS-29 non-cash credits to advocates "ON" | Prohibited | NN-34; [RE] F1.4 and design implication C.13 |
| RS-30 private panel mode "ON" | OFF until D3-05 owner and GDSA | NN-38, NN-39 |
| — | Added RS-37 page themes, RS-38 custom domains, RS-39 migration, RS-40 onboarding packages, RS-41 support tiers, RS-46 notarisation facilitation, RS-47 API overage, RS-48/RS-49 data products, RS-50/RS-51/RS-53/RS-54 explicit prohibitions, RS-52 buyer processing fee, RS-55 group cross-sell, RS-56 escrow handling, RS-57 service-provider tools plan (v3.0 review; P19-OI-14) | Management brief items 6, 8, 11, 12 and conventions; Appendix AA §AA.10.1 |

---

## AB.4 Plans and packages engine

Appendix O §2 (plans), §4 (entitlements and meters), §5 (billing pages), §6 (compliance), §7 (dunning) stay binding. This section adds what the registry needs.

### AB.4.1 Objects

| Object | Table | Rule |
|---|---|---|
| Plan | `core.plans` (O §8.1) + `stream_code` | A plan belongs to one primary stream; it is sellable only while that stream is `live` in scope |
| Package (bundle) | `rev.packages`, `rev.package_items` | A named set of plans, add-ons and one-time items with a package price; every item has a stand-alone price or is marked "included"; the unbundled alternative is always purchasable (Consumer Protection (E-Commerce) Amendment Rules 2026 r.5(7) as reported — no bundling of unrelated fees, loyalty and membership carve-out **[VERIFY]**) |
| Add-on | `core.plans` with `product_line` and `addon_of[]` | Requires a live base plan; prorated on add (FR-P05-36) |
| Trial | `core.plans.trial_days` (0–30) | `trial_converts_automatically = false` (O DP-12); no payment method at trial start |
| Coupon | `rev.coupons`, `rev.coupon_redemptions` | §AB.4.3 |
| Meter | `core.meters` (O §4.3) | Each meter names its stream; overage lines carry `stream_code` |
| Price-test arm | `rev.price_tests`, `rev.price_test_assignments` | §AB.2.7 |

### AB.4.2 Bundling rules

1. A package may combine streams only if all are `live` in the buyer's scope and none is N2 (sponsored listings, advertising and marketplace take are never bundled with plans).
2. Package discount ≤ the cap in `platform.rev.package.max_discount_pct` (G; default 20%, Board) and never applies to neutral, regulated, pass-through or tenant lines (Appendix B P2).
3. Invoices show each package item as a separate line with its allocated price (needed for GST, refunds and Ind AS 115 allocation, §AB.4.9).
4. Removing an item from a package at renewal is a downgrade (next cycle, no refund of the current cycle; O §2 common terms).
5. A package never contains anything that touches a live administered case unless it is parity-safe (RA-3).

### AB.4.3 Coupons and promotions (dark-pattern compliant)

| # | Rule | Source |
|---|---|---|
| CP-1 | Coupons apply only to lines flagged `promo_eligible` (Appendix B §B.9.4); never to neutral fees, regulated schedules, pass-throughs, statutory ₹0 items or concessions | B §B.9.4; B P2 |
| CP-2 | Validity ≤ 90 days; maximum uses and per-account limit stored; the remaining count shown only if bound to the redemption ledger | B §B.9.4; O DP-01 |
| CP-3 | Maximum commercial discount 50% after stacking (B §B.3.5); coupon applies after concessions and plan discounts | B §B.9.4 |
| CP-4 | No countdown timers unless the end time is fixed server-side and identical for all; never on `/fees`, case, neutral, grievance or POSH pages | O DP-01; [RB] §E.18 |
| CP-5 | Strike-through or "was" prices only with a stored prior price and its date; the prior price must be the lowest price in the previous 30 days where the E-Commerce Amendment Rules 2026 apply **[VERIFY]** | [RB] §3.2 item 3; [RA] F10 |
| CP-6 | Coupons are never sent to served respondents or to any person identified from a case without separate marketing consent | NN-16; B §B.9.4 |
| CP-7 | Coupons cannot target advocates, CAs, CSs or CMAs as a reward for bringing work (deny X-21); a uniform professional-plan offer open to all is allowed | Master X-62 |
| CP-8 | Creation: maker `marketing_manager` or `bd_manager`; checker `fin.approver` (≤ 25% off) or `cfo` (> 25%) | NN-36 |

### AB.4.4 Proration, upgrades and downgrades

Appendix O §5.3 (deterministic preview with `preview_sha256`) applies. Additional rules: (a) upgrading into a plan whose stream is paused or killed is blocked (`REV_STREAM_NOT_LIVE`); (b) a downgrade forced by a kill switch is free and prorated to the day, with a credit note; (c) mid-cycle seat removals take effect next cycle unless the plan contract says otherwise.

### AB.4.5 Usage metering

Appendix O §4.3 meters gain `stream_code`. New meters: `M_ROOM_HOURS` (RS-16), `M_HR_EMPLOYEES` (RS-10, active employees on payroll in month), `M_SPONSORED_IMPRESSIONS` (RS-19, reporting only — not a billing unit at launch, since RS-19 is per slot), `M_AD_IMPRESSIONS` (RS-25), `M_MIGRATION_RECORDS` (RS-39, reporting only), `M_ANALYTICS_REPORTS` (RS-48). Live hearings, case-record uploads, GRM intake and POSH inquiry access are never blocked at 100% (O FR-P05-V2-04).

### AB.4.6 Invoices (itemised, GST)

Appendix O §6.5 and Appendix B §B.4/§B.10 apply. Each line carries `stream_code`, `stream_version`, SAC, treatment code (T01–T17), place of supply, and — for marketplace lines — whether Equator collected the consideration (TCS/TDS flags). Package lines show allocated price. Credit notes reference the original line (CGST Act s.34). Every invoice footer shows the legal entity, GSTIN, grievance officer and refund-policy link (O §6.3).

### AB.4.7 Dunning

Appendix O §7 applies unchanged, including the never-suspend list. Kill-switch run-off is not dunning: it never generates collection messages.

### AB.4.8 Multi-currency

Appendix B §B.6 (FX-1…FX-11) governs. A stream's `price_bounds` are authored per currency; non-INR scopes require an export tax profile (LUT, T05) and NN-19 clearance. INT streams use USD authoring as in B FX-2.

### AB.4.9 Revenue recognition — Ind AS 115 notes (guidance only; the statutory auditor and CFO decide)

| Stream family | Likely performance obligation and timing | Points to confirm |
|---|---|---|
| Case fees (RS-01, RS-02) | Each stage service; recognised as the stage is performed or at a point in time when complete | Whether registration is a separate obligation; refund liabilities under §B.8 as variable consideration |
| Neutral fees (pass-through) | Agent (net) for `neutral_direct`; principal only for `equator_principal` (B §B.7.5) | Principal-versus-agent indicators (control before transfer) |
| Subscriptions, rentals, support (RS-06…RS-11, RS-36, RS-38, RS-41, RS-48, RS-57) | Over time, rateably over the service period | Annual prepay as contract liability |
| Usage and overage (RS-47, meters) | As usage occurs | — |
| One-time products (RS-15, RS-42…RS-46) | At a point in time on delivery | Pass-through duty and fees excluded (pure agent) |
| Professional services (RS-26, RS-27, RS-39, RS-40) | Over time if the customer benefits as performed; otherwise on milestone acceptance | Input or output method |
| Marketplace take (RS-18) and processing fee (RS-52) | Agent: net take when the booking service is provided | Gross bookings are not Equator revenue |
| Wallet and credits (RS-32, RS-12) | Contract liability on receipt; revenue on redemption; breakage recognised only in proportion to the pattern of redemption where expected | Ind AS 115 guidance on customers' unexercised rights; GST at receipt (T16) |
| Bundles (packages) | Allocate the package price to each item by relative stand-alone selling price | Stand-alone price evidence |
| Sponsored listings, advertising (RS-19, RS-25) | Over the display period | Make-goods and pro-rata refunds as variable consideration |
| Memberships, Forum (RS-13, RS-14) | Over the membership year | Event seats as separate obligations if material |
| Events (RS-23) | At the event date | — |
| Sales commissions to partners (RS-28) | Incremental costs of obtaining a contract may be capitalised and amortised | Policy choice for ≤ 12-month contracts |

The ledger (P05 FR-P05-52) stores the recognition schedule per invoice line; the finance export provides a deferred-revenue roll-forward by stream. Nothing here is a tax or accounting opinion.

---

## AB.5 Refund, cancellation and renewal codes for new stream types

Proposed additions to Appendix B §B.8 (B prevails; add in the same PR) and to U-7 (ERP-2026.1) §U.7.2. Existing codes RP-STD-MED, RP-STD-ARB, RP-INS-RET, RP-INS-COM, RP-FIN-L, RP-REG, RP-SUB and RP-ACAD (the Institute's own) are unchanged. All amounts are refunded to the original instrument, with a credit note reversing GST (CGST Act s.34); E-Commerce Rules r.4 cancellation-charge symmetry applies (O §6.3).

| Code | Applies to | Rule (default; Board) |
|---|---|---|
| RP-ROOM | RS-16, RS-17 | Cancellation ≥ 48 h before start: 100%; 24–48 h: 50%; < 24 h: nil. If Equator or the venue cancels, or the room fails for > 15 minutes for a platform reason: 100% plus free rebooking |
| RP-SVC | RS-26, RS-27, RS-39, RS-40 | Milestone fees: refundable before work on the milestone starts; after acceptance non-refundable; Equator-caused failure of a milestone: refund of that milestone's fee; termination for convenience by Equator: pro rata |
| RP-MKP | RS-18, RS-52 | Take and processing fee follow the booking: refunded in full when the booking is refunded under the provider's published stage refund rules; Equator's take is never retained on a booking refunded for provider non-delivery |
| RP-ADS | RS-19, RS-25 | Monthly in advance; pro-rata refund for any period in which the slot is removed by Equator (eligibility loss, label audit failure, kill switch); no refund for sponsor-initiated mid-month cancellation |
| RP-EVT | RS-23 | > 14 days before event: 90%; 7–14 days: 50%; < 7 days: nil, transfer to another person allowed free; Equator cancels: 100% or transfer |
| RP-DIG | RS-24, RS-34, RS-37, RS-49 | Digital goods: refundable only if not delivered or materially defective within 7 days of delivery |
| RP-ASSESS | RS-21 | ≥ 7 days before sitting: 100%; one free reschedule; < 7 days: 50%; medical or Equator cancellation: free reschedule or 100% |

Renewal: auto-renew OFF by default for individuals and SMEs; enterprise per order form; reminders T-30, T-7, T-1; price increases need ≥ 30 days' notice and, for individuals and SMEs on auto-renew, fresh confirmation (O AR-1…AR-8).

---

## AB.6 Unit economics and pricing governance

### AB.6.1 Cost model inputs (`rev.cost_inputs`; private)

Each input has a unit, rate, currency, source, effective dates, owner and review date (G tier). Rates are entered from invoices or contracts, never estimated in code. People time comes from Appendix Z as **aggregate, activity-coded time** (e.g., "case-manager minutes per FIN-L stage"); it is never used to assess an individual employee through this module (NN-35).

| Input code | Unit | Source system | Owner | Review |
|---|---|---|---|---|
| `CI_SMS`, `CI_WHATSAPP`, `CI_EMAIL` | per message by template category | P07 provider invoices | finance_ops | monthly |
| `CI_VOICE_MIN` | per minute (inbound, outbound, AI voice) | Telephony invoices; AI voice vendor | finance_ops | monthly |
| `CI_POSTAGE` | per article (Speed Post, registered) | `POSTAL_PORT` invoices | finance_ops | quarterly |
| `CI_VIDEO_PMIN` | per participant-minute | Video infrastructure cost ÷ metered minutes | it_admin + finance_ops | monthly |
| `CI_RECORDING_GB` | per GB-month | Object storage | it_admin | monthly |
| `CI_STORAGE_GB` | per GB-month | Object storage | it_admin | monthly |
| `CI_AI_TOKENS` | per 1,000 input / output tokens by model | AI Gateway cost meter (Appendix E) | it_admin | monthly |
| `CI_OCR_PAGE`, `CI_MT_PAGE` | per page | OCR and translation providers | finance_ops | quarterly |
| `CI_ESIGN` | per signature by method | eSign provider | finance_ops | quarterly |
| `CI_ESTAMP` | per certificate (excluding duty) | e-stamp provider, by state | finance_ops | quarterly |
| `CI_KYC` | per check (DigiLocker, OVSE, PAN, MCA, GSTIN) | KYC providers | finance_ops | quarterly |
| `CI_PG_MDR` | % or flat by method (UPI, card, net banking, NEFT) | Payment gateway statements | finance_ops | monthly |
| `CI_ROUTE_FEE` | per transfer | Gateway | finance_ops | monthly |
| `CI_TRUSTEE` | per escrow account / transaction | Bank and trustee | finance_ops | quarterly |
| `CI_PEOPLE_<role>` | loaded cost per hour by role (salary, statutory contributions, overheads) | Appendix Z / payroll (aggregate only) | finance_ops + hr_manager | quarterly |
| `CI_PARTNER_PAYOUT` | % of first-year subscription | RS-28 agreements | finance_ops | on change |
| `CI_AD_REVIEW` | minutes per creative and per audit | Marketing operations time (aggregate) | marketing_manager | quarterly |
| `CI_INFRA_FIXED` | monthly fixed platform cost allocated by driver | Cloud bills | it_admin + finance_ops | monthly |

**Cost-to-serve per unit** = Σ (driver quantity per unit × input rate) + allocated people time + allocated fixed cost (driver: active tenants, cases or GB, chosen per stream and recorded on the version). Gross margin and contribution margin follow §AB.2.8.

### AB.6.2 Margin guardrails (G tier; defaults proposed for Board approval)

| Stream family | Gross-margin floor (default) | Action when a proposed price or the trailing-quarter actual is below floor |
|---|---|---|
| SaaS subscriptions and rentals | 65% | Price change below floor needs cfo + Board; actual below floor for 2 quarters → viability review "fix or stop" |
| Usage and overage | 40% | cfo approval |
| Professional services | 30% | cfo approval; check day rates against Appendix Z loaded cost |
| One-time products (excluding pass-through) | 25% | fin.controller approval |
| Marketplace take | 30% after PG, trustee and support costs | Board (rates are Board items anyway) |
| Case fees, neutral fees, regulated schedules, statutory ₹0 items, concessions | **No guardrail applies** | Access-to-justice and NN-18 policy prevail over margin; concessions are never a growth lever (B P8) |

Guardrails never trigger automatic price increases; they trigger reviews.

### AB.6.3 Price-change workflow

1. **Propose** (`revenue_manager` or `fin.controller`): new schedule version in the fee editor (Ruleset Studio, master §6) with rationale, benchmark references (Appendix T §0.4 entries; internal only), cost-to-serve impact, affected customers count, notice plan.
2. **Validate** (system): inside `price_bounds`; schedule harness (FR-P05-07) passes; margin guardrail check; deny-list; consumer display (O §6.4); `REV_PRICE_OUT_OF_BOUNDS` if outside bounds — that requires a bounds change (a new stream version) first.
3. **Preview**: sample quotes and invoices; customer notice drafts; explanation-page diff.
4. **Approve** per the authority matrix (§AB.6.5); maker ≠ checker; Board resolution reference recorded where required.
5. **Publish** with `effective_from` ≥ today + notice period (subscriptions ≥ 30 days; case-fee schedules apply only to cases filed on or after `effective_from` — cases are pinned at filing, NN-21).
6. **Notify** affected subscribers (service template) with the new total incl. GST and how to cancel.
7. **Monitor** for 2 cycles: conversion, churn, complaints; results attached to the next viability review.
8. **Rollback**: the previous version can be re-published by maker-checker; customers who renewed at the new price get the lower price from the next cycle.

### AB.6.4 What may never change through this workflow

Neutral fee bands are changed only under Appendix B §B.7 governance; regulated schedules (SEC) follow the regulator verbatim (NN-18); deny-list items cannot be priced; concessions follow B §B.9.

### AB.6.5 Authority matrix for streams and prices (defaults; G tier; Board to approve the matrix itself)

| Decision | Maker | Checker / approver | Board |
|---|---|---|---|
| New stream with rating N0, family `saas_subscription`, `usage`, `one_time_product`, `professional_service` | revenue_manager | cfo | Informed at next meeting |
| New stream N1, or any new stream in families `case_fee`, `programme`, `membership`, `event` with sponsors | revenue_manager | cfo + legal_reviewer | **Approval required** |
| Any N2 stream (marketplace take, sponsored listing, advertising), or lowering a rating | revenue_manager | compliance_officer + legal_reviewer + counsel opinion | **Approval required** (resolution reference) |
| Any related-party stream (RS-22, RS-55, intercompany cross-charges) | revenue_manager | company_secretary + cfo | **Approval required** under s.188 (shareholder approval where Rules 2014 r.15(3) thresholds are crossed) **[CS to confirm]** |
| Price change within bounds ≤ 5% (B2B SaaS, usage, services) | revenue_manager | fin.approver | — |
| Price change within bounds > 5% and ≤ 10% | revenue_manager | cfo | Informed |
| Price change > 10%, any change to consumer-facing case fees, any change to a vertical card, or a bounds change | revenue_manager / fin.controller | cfo | **Approval required** (B §B.12) |
| Coupon ≤ 25% / > 25% | marketing_manager or bd_manager | fin.approver / cfo | — |
| Enterprise discount beyond card (CPQ, AU-08) | sales_executive | bd_manager ≤ 10%; cfo ≤ 25%; Board > 25% or below floor | As stated |
| Kill switch engage | one authorised user (KS-1) | — | Informed within 24 h for N2 or Board-resolution streams |
| Kill switch release / resume | revenue_manager | cfo + compliance_officer | Approval if the kill reason was `neutrality_incident`, `legal` or `regulator` |
| Retire a stream | revenue_manager | cfo | Approval if it carried a Board resolution |
| Price-test policy / individual test | revenue_manager | Board (policy) / cfo (test) | Policy only |

Thresholds are Governed settings (`platform.rev.authority.*`, §AB.8) with effective dates and version history, enforced as rows of the Appendix Z `ctl.authority_rules` matrix (action codes proposed for Appendix Z: `REV-STREAM-NEW`, `REV-PRICE-CHANGE`, `REV-COUPON`, `REV-ENTERPRISE-DISCOUNT`, `REV-KILL-RELEASE`, `REV-STREAM-RETIRE`, `REV-PRICE-TEST`); exceptions are logged in `ctl.exceptions` with reasons and reported quarterly (NN-36).

---

## AB.7 Business model canvas, viability scorecard, sequencing

### AB.7.1 Business model canvas (Equator ecosystem)

| Block | Content |
|---|---|
| Customer segments | Parties (individual, business); lenders, insurers, employers; regulated entities for GRM; employers and HEIs for POSH; independent neutrals and chambers; institutions (bar associations, chambers of commerce, universities); advocates and firms (Counsel workspace only); platforms (API); group companies (shared services) |
| Value propositions | Defensible, published, neutral administration; regulator-clock grievance handling; own-brand practice software; portable data (NN-37); published prices with GST; no paid influence on appointments |
| Channels | Public website and Dispute Explorer; enterprise sales and partners (non-professional); Ops Platform campaigns (consented); events and publications; marketplace (non-administered work) |
| Customer relationships | Self-serve with honest cancellation; CSM tiers for tenants; statutory grievance desk separate from sales |
| Revenue streams | §AB.3 (57 records; 6 prohibited; 17 OFF at launch) |
| Key resources | Rules and codes (Appendix U); neutral panel and EQAP; platform; Claims Register; registry |
| Key activities | Case administration; allocation; scrutiny; SaaS operation; onboarding and migration; compliance (dark-pattern audits, tax) |
| Key partners | Payment gateway, bank escrow and trustee, eSign and e-stamp providers, telephony, KYC providers, Microsoft 365 / Google Workspace (D3-04), Brevo-class tools behind ports (NN-40), venue partners, training providers (≥ 3; D2-17) |
| Cost structure | §AB.6.1 inputs: messaging and telephony, video, AI tokens, storage, eSign/eStamp, KYC, PG fees, people time, infrastructure, compliance and audit |

### AB.7.2 Viability scorecard (`rev.viability_reviews`)

Gates must all pass; then the weighted score decides.

| Criterion | Type | Weight | Evidence |
|---|---|---|---|
| Neutrality rating ≤ N2 and controls tested (NO_PAID_PLACEMENT, labels, firewall) | Gate | — | CI results; compliance_officer sign-off |
| Legal dependencies satisfied (counsel, Board, related party, tax memo) | Gate | — | `legal_dependencies[]` all `satisfied` |
| No open neutrality incident or regulator query on the stream | Gate | — | Incident register |
| Strategic fit with institutional mission | Score | 15 | Board pack note |
| Demand evidence (pipeline, pilots, adoption vs target) | Score | 20 | CRM, adoption KPI |
| Gross margin vs floor (§AB.6.2) | Score | 20 | `reporting.rev_margin` |
| CAC payback (B2B) ≤ target (default 12 months) | Score | 10 | `reporting.rev_cac` |
| Churn / refund / complaint rates vs targets | Score | 15 | KPIs |
| Operational readiness (support, SOPs, training, vendor fallback NN-40) | Score | 10 | Runbook, ports |
| Reputational risk (press, professional bodies, customer feedback) | Score | 10 | Ops Platform PR log |

**Decision:** Go/continue ≥ 70; fix within one quarter 50–69 (owner and plan recorded); stop (pause then retire) < 50, or any gate failure, or two consecutive quarters below a stream's kill thresholds. Cadence: monthly for the first two quarters after `live`, then quarterly; annual Board review of all streams with the neutrality-exposure tile.

### AB.7.3 Launch sequencing and stop/go criteria

| Wave | When | Streams | Go criteria | Stop criteria |
|---|---|---|---|---|
| 0 — Institutional core | P05 and P09 GA | RS-01, RS-02, RS-03, RS-04, RS-05, RS-06, RS-07, RS-15, RS-21, RS-35, RS-42…RS-45, RS-56 | Board-approved cards; tax memo signed; dark-pattern audit baseline | Any NN-18/NN-29 test failure; regulator objection |
| 1 — SaaS and services | P10 GA and Ops Platform GA | RS-08, RS-09, RS-11, RS-13, RS-14, RS-23, RS-24, RS-26, RS-27, RS-28, RS-32, RS-36, RS-38, RS-39, RS-40, RS-41, RS-47, RS-48; RS-16 at P04 GA | Support runbooks; CSM capacity; partner agreements (non-professional) | Gross margin < floor for 2 quarters; complaint rate > 2% of accounts |
| 2 — Marketplace and practice extensions | Appendix AA marketplace live; HR rule packs published | RS-18; RS-10; RS-37; RS-30 (after D3-05 and GDSA); RS-12 (after name cleared); RS-57 (after Board prices) | Marketplace grievance officer named; E-Commerce Rules controls live; payroll UAT; GDSA signed | Fee-dispute rate > 3% of bookings; any appointment-influence complaint substantiated |
| 3 — Governed, counsel-dependent | After Board + counsel | RS-19, RS-25, RS-52, RS-49, RS-22, RS-55, RS-17, RS-46, RS-33, RS-34 | Counsel opinions; Board resolutions; for RS-19: SLP (C) 25794/2024 position considered, advocates excluded, organic ranking parameters published, annual dark-pattern certificate | Any neutrality incident; sponsored complaint rate > 0.5 per 1,000 impressions; adverse professional-body communication |
| Never | — | RS-20, RS-29, RS-31 (as a fee), RS-50, RS-51, RS-53, RS-54 | — | — |

### AB.7.4 Viability dashboard and stop/go automation with human approval *(v3.1)*

**Dashboard (SCR-P19-AB09, exception-first).** One row per stream and scope, sorted red → amber → grey → green, then by days to next review. Columns: status and rating; RAG; weighted score with the last six periods as a sparkline; each gate (pass/fail); KPIs against target and kill threshold (§AB.2.8, `rev.kpi_targets`); open neutrality incidents and complaint rate; next review due and any decision pending; wave (§AB.7.3). Saved views (by family, rating, wave, owner); filters; XLSX and PDF/A export for the Board pack (NN-37 naming). Private columns follow §AB.2.10.

| RAG | Rule (computed by `packages/rules/rev-viability`, pure, golden vectors) |
|---|---|
| Red | Any gate fails, or score < `stop_score`, or any KPI beyond its kill threshold, or a neutrality incident open |
| Amber | Score between `stop_score` and `go_score`, or a KPI within `platform.rev.viability.amber_band_pct` (default 10%) of its kill threshold, or a review overdue |
| Grey | Insufficient data: fewer than `platform.rev.viability.min_accounts_for_score` (default 10) paying accounts, or fewer than 2 complete periods since `live` — score shown as "not yet meaningful"; gates still evaluated |
| Green | Otherwise |

**Automation (`ViabilityReviewWorkflow`, extended).**
1. **Pack assembly.** On each cadence date (§AB.7.2) the workflow builds the review pack: KPI snapshots, gate results, incident and complaint register extracts, margin versus floor (§AB.6.2), price-change and coupon history, and the previous decision with its actions. Quantitative criteria (gross margin, CAC payback, churn/refund/complaint, demand versus adoption target) are **pre-scored**; strategic fit, operational readiness and reputational risk are left blank for the human reviewer. The reviewer may change any pre-score with a reason (recorded).
2. **Decision proposal.** From the completed scores and gates the workflow drafts one proposal — `continue`, `fix` (owner, actions, due date within one quarter), `pause`, `retire` (with an auto-drafted run-off plan: affected customers, notice dates ≥ 30 days for subscriptions, refunds by RP code) or, for an `approved` stream waiting in a wave, `go_live_scope` once every go criterion of §AB.7.3 for that wave reads green (e.g., grievance officer named, tax memo, dark-pattern certificate). Proposals are stored in `rev.viability_proposals` and **never execute themselves** (L): `pause`, `retire` and `go_live_scope` open the ordinary §AB.2.3 transition with `revenue_manager` as maker and the §AB.6.5 approver as checker (Board where §AB.6.5 requires).
3. **No stop on thin data.** A grey (insufficient-data) stream cannot receive a `pause` or `retire` proposal on score alone; only a failed gate, a kill-threshold breach or a neutrality incident can propose a stop for it (`REV_VIABILITY_DATA_INSUFFICIENT`, 409, if a user tries).
4. **Timeouts and escalation.** A proposal undecided after `platform.rev.viability.decision_sla_days` (G, default 10 working days) escalates to `cfo`; after a further 10 working days it is placed on the next Board agenda through the Board secretary. A `fix` action past due turns the stream amber and re-proposes at the next review; two missed fixes produce a `pause` proposal.
5. **Urgent path.** A gate failure for reason `neutrality_incident`, `legal` or `regulator` immediately alerts the KS-1 roles with a **recommendation** to engage the kill switch; a human engages it (§AB.2.5). The automation never engages a kill switch.
6. **Defer once.** A reviewer may defer a review once by up to 30 days with a reason (never for a red stream with a failed gate).
7. **KPIs of the process.** Reviews completed by due date ≥ 95%; median proposal-to-decision ≤ 10 working days; share of streams red or amber for more than two consecutive reviews (reported to the Board). Acceptance tests in §AB.14.

---

## AB.8 Settings catalogue

Tier per NN-33. "Who" = who may change; "Approval" = second person needed.

| Key | Tier | Default | Who / approval | Notes |
|---|---|---|---|---|
| `platform.rev.registry.enforce` | L | true | — | RA-8 guard on quote, checkout, CMS, CPQ |
| `platform.rev.prohibited_streams` | L | RS-20, RS-29, RS-50, RS-51, RS-53, RS-54 (+ any fee on RS-31) | — | Deny-list mirror |
| `platform.rev.kill_switch.propagation_p95_seconds` | L | 60 (max 300) | — | KS-3 |
| `platform.rev.kill_switch.authorised_roles` | G | cfo, compliance_officer, ops_director, legal_reviewer | cfo → Board | KS-1 |
| `platform.rev.neutrality.n2_requires` | L | counsel opinion + Board resolution + compliance_officer | — | §AB.2.4 |
| `platform.rev.case_scope.n2_max` | L | `non_administered` | — | RA-3, NN-34 |
| `platform.rev.professional_rules.enforce` | L | true | — | Master X-62 tags |
| `group.rev.related_party.approval_required` | L | true | — | RA-13 |
| `platform.rev.authority.price_change_fin_approver_pct` | G | 5 | cfo → Board | §AB.6.5 |
| `platform.rev.authority.price_change_cfo_pct` | G | 10 | cfo → Board | §AB.6.5 |
| `platform.rev.authority.enterprise_discount_bd_pct` / `_cfo_pct` | G | 10 / 25 | cfo → Board | AU-08 |
| `platform.rev.price_change.subscription_notice_days` | G | 30 (min 30) | cfo → legal_reviewer | O AR-8 |
| `platform.rev.price_tests.enabled` | G | **OFF** | Board + counsel | §AB.2.7 |
| `platform.rev.price_tests.max_arms` / `.max_days` | G | 2 / 60 | cfo → Board | PT-2 |
| `platform.rev.price_tests.consumer_allowed` | L | false | — | PT-1 |
| `platform.rev.package.max_discount_pct` | G | 20 | cfo → Board | §AB.4.2 |
| `platform.rev.coupon.max_validity_days` / `.max_discount_pct` | G | 90 / 50 | cfo | B §B.9.4 |
| `platform.rev.margin_floor.<family>_pct` | G | §AB.6.2 | cfo → Board | Private |
| `platform.rev.viability.cadence` | G | monthly × 2 quarters, then quarterly | cfo | D3-39 |
| `platform.rev.viability.go_score` / `.stop_score` | G | 70 / 50 | cfo → Board | §AB.7.2 |
| `platform.rev.viability.amber_band_pct` *(v3.1)* | G | 10 | cfo | §AB.7.4 RAG |
| `platform.rev.viability.min_accounts_for_score` *(v3.1)* | G | 10 | cfo | §AB.7.4 grey state; ≥ 5 |
| `platform.rev.viability.decision_sla_days` *(v3.1)* | G | 10 working days | cfo → Board | §AB.7.4 escalation |
| `platform.rev.viability.auto_execute` *(v3.1)* | L | false | — | Proposals never self-execute |
| `platform.rev.explanation_pages.enabled` | L | true | — | RA-14 |
| `platform.rev.cost_data.roles` | L | finance_ops, accounts_checker, cfo, internal_auditor, compliance_officer (read) | — | §AB.2.10 |
| `platform.rev.ads.enabled` | G | **OFF** | Board + counsel; advertiser policy approved (Appendix AA §AA.10.8) | RS-25; alias `cms.display_ads` (Appendix AA X-59 (h)) |
| `marketplace.paid_placement` | G | **OFF** | Board + counsel | RS-19; NN-34 |
| `marketplace.paid_placement.max_slots_per_page` | G | 2 (locked maximum 2) | compliance_officer | NN-34 |
| `marketplace.paid_placement.advocates` | L | OFF | — | X-62 |
| `marketplace.take_rate.<plan>` | G | O-R2 values | Board | RS-18 |
| `marketplace.take_rate.service_providers` | G | 10% (Board) | Board | RS-18 scope `service_providers`; flat, never falling with volume (deny X-19) |
| `mkp.provider_subscriptions` | G | **OFF** | Board (prices) + cfo | RS-57 (Appendix AA §AA.10.1) |
| `marketplace.advocate_neutral.flat_fee_minor` | G | Board | Board + counsel | X-62(d) |
| `marketplace.client_processing_fee` | G | **OFF** | Board + counsel | RS-52 |
| `academy.institute_referral` / `academy.institute_referral_fee` | G | **OFF** / **OFF** | Board (s.188) | D3-38 |
| `directory.public_professionals` | G | **OFF** | counsel opinion + SLP (C) 25794/2024 decided + Board | RS-31; NN-39 |
| `billing.eco_gst_tcs` / `billing.eco_withholding` | G | **OFF** | cfo after tax memo | RS-18; LR-TAX-008 / LR-TAX-007; aliases `tax.eco_gst_tcs` / `tax.eco_tds` (AB-R12) |
| `tenant.rev.stream.<code>.enabled` | T | per stream | tenant admin (chambers_owner, institution_admin, enterprise_admin) | Only `tenant_configurable` streams; narrows platform scope |
| `tenant.rev.own_fee_schedule.*` | T within G bounds | — | chambers_admin → chambers_accounts | B validators P1–P9 |
| `tenant.rev.coupons.enabled` | T | false | chambers_owner | Tenant's own fees only; CP-1…CP-7 apply |
| `tenant.rev.trial_days` | T (0–30) | 14 | chambers_owner | No auto-convert (L) |
| `tenant.rev.invoice.branding` | T | tenant name and logo | chambers_admin | Equator legal footer retained |

---

## AB.9 Data model (DDL sketch; schema `rev`)

All tables carry `tenant_id` where tenant-scoped, RLS, UUIDv7 keys, `amount_minor BIGINT` + `currency CHAR(3)`; append-only tables revoke UPDATE/DELETE.

```sql
CREATE SCHEMA rev;
CREATE TABLE rev.streams (code text PRIMARY KEY CHECK (code ~ '^RS-[0-9]{2,3}$'), slug text UNIQUE NOT NULL,
  family text NOT NULL, revenue_owner text NOT NULL, created_at timestamptz NOT NULL DEFAULT now());
CREATE TABLE rev.stream_versions (id uuid PRIMARY KEY DEFAULT uuidv7(), stream_code text NOT NULL REFERENCES rev.streams(code),
  version int NOT NULL, status text NOT NULL CHECK (status IN ('draft','in_review','approved','live','paused','retired')),
  name_i18n jsonb NOT NULL, segment text[] NOT NULL, buyer_kind text[] NOT NULL, value_statement_i18n jsonb NOT NULL,
  pricing_unit text NOT NULL, cadence text NOT NULL, entitlements jsonb NOT NULL, plan_membership text[] NOT NULL DEFAULT '{}',
  tax_profile jsonb NOT NULL, refund_code text NOT NULL, cancellation_terms jsonb, renewal_terms jsonb,
  neutrality_rating text NOT NULL CHECK (neutrality_rating IN ('N0','N1','N2','N3','N4')),
  case_scope_allowed text NOT NULL CHECK (case_scope_allowed IN ('none','non_administered','administered_parity_safe','administered')),
  professional_rule_flags text[] NOT NULL DEFAULT '{}', tenant_configurable boolean NOT NULL DEFAULT false,
  price_test_policy jsonb, review_cadence text NOT NULL, public_explanation jsonb NOT NULL,
  approver_role text NOT NULL, effective_from date, effective_to date, review_date date NOT NULL,
  supersedes_version int, maker_id uuid NOT NULL, checker_id uuid,
  UNIQUE (stream_code, version),
  CHECK (checker_id IS NULL OR checker_id <> maker_id),                                   -- NN-36
  CHECK (neutrality_rating <> 'N4' OR status IN ('draft','retired')),                     -- prohibited never approved
  CHECK (neutrality_rating NOT IN ('N2','N3') OR case_scope_allowed IN ('none','non_administered')));
CREATE TABLE rev.stream_scopes (id uuid PRIMARY KEY DEFAULT uuidv7(), version_id uuid NOT NULL REFERENCES rev.stream_versions(id),
  jurisdictions text[] NOT NULL DEFAULT '{IN}', segments text[], tenant_types text[], verticals text[], channels text[],
  org_allow uuid[], org_deny uuid[], live boolean NOT NULL DEFAULT false, live_from timestamptz, live_to timestamptz);
CREATE TABLE rev.price_bounds (id uuid PRIMARY KEY DEFAULT uuidv7(), version_id uuid NOT NULL REFERENCES rev.stream_versions(id),
  currency char(3) NOT NULL, unit text NOT NULL, min_minor bigint NOT NULL, max_minor bigint NOT NULL, board_approval_ref text,
  CHECK (min_minor >= 0 AND max_minor >= min_minor));
CREATE TABLE rev.schedule_links (version_id uuid REFERENCES rev.stream_versions(id), fee_schedule_id uuid, plan_id uuid, plan_price_id uuid);
CREATE TABLE rev.legal_dependencies (id uuid PRIMARY KEY DEFAULT uuidv7(), version_id uuid NOT NULL REFERENCES rev.stream_versions(id),
  kind text NOT NULL CHECK (kind IN ('legal_rule','counsel_opinion','board_resolution','related_party_approval','vendor_contract','regulator_status','unconfirmed_fact','tax_memo')),
  ref text NOT NULL, status text NOT NULL CHECK (status IN ('pending','satisfied','lapsed')), evidence_document_id uuid, review_date date);
CREATE TABLE rev.stream_transitions (id uuid PRIMARY KEY DEFAULT uuidv7(), version_id uuid NOT NULL, from_status text, to_status text NOT NULL,
  scope_id uuid, actor_id uuid NOT NULL, checker_id uuid, reason text, guard_results jsonb NOT NULL, prev_hash char(64), hash char(64) NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now());                                                       -- append-only
CREATE TABLE rev.kill_switch_events (id uuid PRIMARY KEY DEFAULT uuidv7(), stream_code text NOT NULL, scope jsonb NOT NULL,
  action text NOT NULL CHECK (action IN ('engage','release')), reason_code text NOT NULL, reason_text text NOT NULL,
  actor_id uuid NOT NULL, checker_id uuid, propagated_at timestamptz, hash char(64) NOT NULL, created_at timestamptz NOT NULL DEFAULT now(),
  CHECK (action <> 'release' OR (checker_id IS NOT NULL AND checker_id <> actor_id)));         -- append-only
CREATE TABLE rev.price_change_requests (id uuid PRIMARY KEY DEFAULT uuidv7(), stream_code text NOT NULL, from_schedule_id uuid, to_schedule_id uuid NOT NULL,
  change_pct numeric(6,2), rationale text NOT NULL, impact jsonb NOT NULL, required_approver text NOT NULL, board_resolution_ref text,
  maker_id uuid NOT NULL, checker_id uuid, status text NOT NULL CHECK (status IN ('draft','in_review','approved','rejected','published','rolled_back')),
  effective_from date, CHECK (checker_id IS NULL OR checker_id <> maker_id));
CREATE TABLE rev.price_tests (id uuid PRIMARY KEY DEFAULT uuidv7(), stream_code text NOT NULL, hypothesis text NOT NULL, arms jsonb NOT NULL,
  starts_at timestamptz NOT NULL, ends_at timestamptz NOT NULL, adopted_arm text, honour_applied_at timestamptz, maker_id uuid NOT NULL, checker_id uuid NOT NULL,
  CHECK (ends_at <= starts_at + interval '60 days'));
CREATE TABLE rev.price_test_assignments (test_id uuid REFERENCES rev.price_tests(id), organisation_id uuid NOT NULL, arm text NOT NULL,
  assigned_at timestamptz NOT NULL, PRIMARY KEY (test_id, organisation_id));
CREATE TABLE rev.packages (id uuid PRIMARY KEY DEFAULT uuidv7(), code text UNIQUE NOT NULL, name_i18n jsonb NOT NULL, status text NOT NULL, discount_pct numeric(5,2) NOT NULL DEFAULT 0);
CREATE TABLE rev.package_items (package_id uuid REFERENCES rev.packages(id), stream_code text NOT NULL, plan_id uuid, quantity int NOT NULL DEFAULT 1,
  allocated_price_minor bigint NOT NULL, standalone_price_minor bigint NOT NULL, included boolean NOT NULL DEFAULT false);
CREATE TABLE rev.coupons (id uuid PRIMARY KEY DEFAULT uuidv7(), code text UNIQUE NOT NULL, stream_codes text[] NOT NULL, pct_off numeric(5,2), amount_off_minor bigint,
  valid tstzrange NOT NULL, max_uses int NOT NULL, per_account_limit int NOT NULL DEFAULT 1, audience jsonb NOT NULL, maker_id uuid NOT NULL, checker_id uuid NOT NULL,
  CHECK (upper(valid) <= lower(valid) + interval '90 days'), CHECK (checker_id <> maker_id), CHECK (pct_off IS NULL OR pct_off <= 50));
CREATE TABLE rev.coupon_redemptions (id uuid PRIMARY KEY DEFAULT uuidv7(), coupon_id uuid NOT NULL REFERENCES rev.coupons(id), account_id uuid NOT NULL,
  invoice_line_id uuid NOT NULL, redeemed_at timestamptz NOT NULL DEFAULT now());                       -- append-only
CREATE TABLE rev.cost_inputs (code text, effective daterange, unit text NOT NULL, rate_minor bigint NOT NULL, currency char(3) NOT NULL,
  source_document_id uuid, owner_role text NOT NULL, review_date date NOT NULL, PRIMARY KEY (code, effective));   -- private grants
CREATE TABLE rev.cost_drivers (version_id uuid REFERENCES rev.stream_versions(id), input_code text NOT NULL, quantity_formula text NOT NULL);
CREATE TABLE rev.kpi_definitions (code text PRIMARY KEY, formula text NOT NULL, unit text NOT NULL, description_i18n jsonb NOT NULL);
CREATE TABLE rev.kpi_targets (version_id uuid REFERENCES rev.stream_versions(id), kpi_code text REFERENCES rev.kpi_definitions(code),
  target numeric, kill_threshold numeric, PRIMARY KEY (version_id, kpi_code));
CREATE TABLE rev.kpi_snapshots (stream_code text, kpi_code text, period daterange, value numeric, computed_at timestamptz, PRIMARY KEY (stream_code, kpi_code, period));
CREATE TABLE rev.viability_reviews (id uuid PRIMARY KEY DEFAULT uuidv7(), stream_code text NOT NULL, period daterange NOT NULL, gates jsonb NOT NULL,
  scores jsonb NOT NULL, total int NOT NULL, decision text NOT NULL CHECK (decision IN ('go','fix','stop')), actions jsonb, reviewed_by uuid NOT NULL, approved_by uuid NOT NULL,
  CHECK (approved_by <> reviewed_by));
CREATE TABLE rev.viability_proposals (id uuid PRIMARY KEY DEFAULT uuidv7(), review_id uuid NOT NULL REFERENCES rev.viability_reviews(id),   -- v3.1
  stream_code text NOT NULL, scope_id uuid, proposal text NOT NULL CHECK (proposal IN ('continue','fix','pause','retire','go_live_scope')),
  rag text NOT NULL CHECK (rag IN ('red','amber','grey','green')), prescores jsonb NOT NULL, overrides jsonb NOT NULL DEFAULT '[]',
  rationale text NOT NULL, runoff_plan jsonb, due_at timestamptz NOT NULL, escalated_at timestamptz,
  decision text CHECK (decision IN ('accepted','rejected','deferred')), decided_by uuid, transition_id uuid, decided_at timestamptz);
CREATE TABLE rev.related_party_arrangements (id uuid PRIMARY KEY DEFAULT uuidv7(), stream_code text NOT NULL, counterparty_legal_name text NOT NULL,
  counterparty_cin text, nature text NOT NULL, arm_length_basis text NOT NULL, board_resolution_ref text, shareholder_resolution_ref text,
  s184_disclosures jsonb, aoc2_flag boolean NOT NULL DEFAULT true, valid daterange NOT NULL);
CREATE TABLE rev.tenant_stream_settings (tenant_id uuid NOT NULL, stream_code text NOT NULL, enabled boolean NOT NULL, own_price_schedule_id uuid,
  changed_by uuid NOT NULL, changed_at timestamptz NOT NULL, PRIMARY KEY (tenant_id, stream_code));
CREATE TABLE rev.explanation_pages (id uuid PRIMARY KEY DEFAULT uuidv7(), version_id uuid NOT NULL REFERENCES rev.stream_versions(id), locale text NOT NULL,
  route text NOT NULL, content_sha256 char(64) NOT NULL, published_at timestamptz, unpublished_at timestamptz);
-- Grants: allocation, neutrals.*, grading, conflict and directory roles have NO grant on schema rev (RA-11; NO_PAID_PLACEMENT).
-- core.fee_schedules, core.plans, core.plan_prices gain: stream_code text NOT NULL REFERENCES rev.streams(code).
-- Edit log: rev.* and pricing tables are covered by the un-disableable edit log (NN-36).
```

---

## AB.10 APIs (`/v1`, OpenAPI 3.1; Idempotency-Key on every POST/PATCH that changes status, price or money)

| Method and path | Purpose | Role |
|---|---|---|
| `GET /v1/rev/streams?status=&rating=&family=` | List streams (private fields omitted by role) | revenue_manager, cfo, finance_ops, compliance_officer, internal_auditor, marketing_manager (public fields) |
| `POST /v1/rev/streams/{code}/versions` · `PATCH /v1/rev/stream-versions/{id}` | Create / edit draft version | revenue_manager |
| `POST /v1/rev/stream-versions/{id}/submit` · `/approve` · `/reject` | Review workflow | maker / approver per §AB.6.5 |
| `POST /v1/rev/stream-versions/{id}/scopes` · `POST /v1/rev/scopes/{id}/go-live` · `/pause` · `/resume` | Scope lifecycle | maker + checker |
| `POST /v1/rev/streams/{code}/kill` · `POST /v1/rev/kill-events/{id}/release` | Kill switch (step-up MFA) | KS-1 roles / maker-checker |
| `POST /v1/rev/streams/{code}/retire` | Retire with run-off plan | revenue_manager + cfo |
| `GET /v1/rev/check?stream=&scope=` | Runtime `assertLive` (internal; p95 < 15 ms cached) | services |
| `POST /v1/rev/price-change-requests` · `/{id}/approve` · `/{id}/publish` · `/{id}/rollback` | Price governance | per §AB.6.5 |
| `POST /v1/rev/price-tests` · `/{id}/stop` | Price tests (flag-gated) | revenue_manager + cfo |
| `GET/POST /v1/rev/packages` · `GET/POST /v1/rev/coupons` | Packages and coupons | revenue_manager / marketing_manager + checker |
| `GET/PUT /v1/rev/cost-inputs/{code}` | Cost inputs (private) | finance_ops + accounts_checker |
| `GET /v1/rev/kpis?stream=&period=` · `POST /v1/rev/viability-reviews` | KPIs and reviews | cfo, revenue_manager, internal_auditor |
| `GET /v1/rev/viability-dashboard?view=` · `POST /v1/rev/viability-proposals/{id}:accept` · `:reject` · `:defer` *(v3.1)* | RAG dashboard; decide a proposal (accept opens the §AB.2.3 transition for checker approval) | cfo, revenue_manager, compliance_officer, internal_auditor (read) |
| `GET/POST /v1/rev/related-party-arrangements` | Related-party records | company_secretary + cfo |
| `GET/PUT /v1/tenant/rev/streams/{code}` | Tenant toggles for `tenant_configurable` streams | tenant admins |
| `GET /v1/public/how-we-earn?locale=` · `GET /v1/public/streams/{slug}` | Generated explanation content | public |

## AB.11 Events (CloudEvents; IDs and amounts only, never PII)

`equator.rev.stream.created.v1` · `equator.rev.stream_version.submitted.v1` · `.approved.v1` · `.rejected.v1` · `equator.rev.stream.status_changed.v1` (scope, from, to) · `equator.rev.stream.killed.v1` · `equator.rev.stream.kill_released.v1` · `equator.rev.stream.retired.v1` · `equator.rev.price_change.requested.v1` · `.approved.v1` · `.published.v1` · `.rolled_back.v1` · `equator.rev.price_test.started.v1` · `.stopped.v1` · `equator.rev.coupon.created.v1` · `.redeemed.v1` · `equator.rev.package.published.v1` · `equator.rev.kpi.snapshot_computed.v1` · `equator.rev.viability_review.completed.v1` · *(v3.1)* `equator.rev.viability_proposal.created.v1` · `.escalated.v1` · `.decided.v1` · `equator.rev.related_party.recorded.v1` · `equator.rev.tenant_stream.toggled.v1` · `equator.rev.explanation_page.published.v1` · `.unpublished.v1` · `equator.rev.margin_guardrail.breached.v1`.

## AB.12 Error codes (RFC 9457 `code`; register in Appendix F §F.10.4 v3)

| Code | HTTP | Meaning |
|---|---|---|
| `REV_STREAM_NOT_FOUND` | 404 | Unknown stream code |
| `REV_STREAM_NOT_LIVE` | 409 | Stream not live in the caller's scope; sale, quote or render refused |
| `REV_STREAM_PROHIBITED` | 422 | N4 / deny-list stream cannot be approved or priced |
| `REV_KILL_SWITCH_ACTIVE` | 423 | Kill switch engaged for this scope |
| `REV_TRANSITION_INVALID` | 409 | Transition not allowed from current status |
| `REV_MAKER_CHECKER_SAME_USER` | 403 | Checker equals maker (NN-36) |
| `REV_COUNSEL_OPINION_REQUIRED` | 422 | Counsel opinion dependency not satisfied |
| `REV_BOARD_RESOLUTION_REQUIRED` | 422 | Board resolution reference missing |
| `REV_RELATED_PARTY_APPROVAL_REQUIRED` | 422 | s.188 approval reference missing (RA-13) |
| `REV_TAX_MEMO_REQUIRED` | 422 | Tax profile pending for a B2C scope |
| `REV_PRICE_OUT_OF_BOUNDS` | 422 | Schedule or test arm outside approved bounds |
| `REV_PRICE_TEST_NOT_PERMITTED` | 422 | Flag OFF, consumer scope, or prohibited line (PT-1) |
| `REV_SCOPE_NOT_PERMITTED` | 422 | Case scope or segment not allowed for the rating |
| `REV_JURISDICTION_NOT_ENABLED` | 422 | No published rule pack for the state or country |
| `REV_PROFESSIONAL_RULE_BLOCK` | 422 | Master X-62 / deny X-21–X-22 violation |
| `REV_NEUTRALITY_CONFLICT` | 422 | Attempted read path or bundle that breaches RA-11 |
| `REV_TENANT_NOT_CONFIGURABLE` | 403 | Tenant tried to change a non-tenant-configurable stream |
| `REV_COUPON_INVALID` | 422 | Expired, exhausted, wrong audience or ineligible line |
| `REV_COUPON_DARK_PATTERN` | 422 | Coupon breaches CP-1…CP-7 |
| `REV_PACKAGE_ITEM_NOT_LIVE` | 409 | A package item's stream is not live |
| `REV_MARGIN_GUARDRAIL_BREACH` | 422 | Price below floor without the required approver |
| `REV_COST_DATA_RESTRICTED` | 403 | Private cost or margin fields requested without grant |
| `REV_EXPLANATION_STALE` | 409 | Explanation page source version not live |
| `REV_RUNOFF_REQUIRED` | 409 | Retirement attempted with open obligations and no run-off plan |
| `REV_VIABILITY_DATA_INSUFFICIENT` *(v3.1)* | 409 | Stop proposed on score alone for a stream with insufficient data (§AB.7.4 rule 3) |

## AB.13 RBAC and audit

New role (register in Appendix S): `revenue_manager` (Ops Platform; maker for streams, prices, packages). **Designations, not separate roles** (Appendix Z designation model): `cfo` = the CFO designation held by a `finance_controller` user (with the `fin.controller` bundle, P05) plus stream-approval permission; `company_secretary` = the Company Secretary designation held by a `compliance_officer` user (Appendix Z §Z.2.3, §Z.12.2), who records Board and shareholder resolutions, s.184/s.188 references and AOC-2 flags. Cerbos policies test the designation attribute. Existing roles used: `fin.approver`, `fin.controller`, `finance_ops`, `accounts_maker`, `accounts_checker`, `compliance_officer`, `legal_reviewer`, `internal_auditor`, `ops_director`, `marketing_manager`, `bd_manager`, `sales_executive`, `customer_success_manager`, `platform_admin`, tenant roles `chambers_owner`, `chambers_admin`, `chambers_accounts`, `institution_admin`, `enterprise_admin`.

| Action | revenue_manager | cfo | fin.approver | compliance_officer | legal_reviewer | company_secretary | internal_auditor | marketing_manager | Tenant admin |
|---|---|---|---|---|---|---|---|---|---|
| Create/edit draft version | ✓ | — | — | — | — | — | — | copy fields | — |
| Approve version (N0) | — | ✓ | — | — | — | — | — | — | — |
| Approve N1 / N2 | — | ✓ + | — | ✓ (N2) | ✓ | — | — | — | — |
| Set / raise neutrality rating | — | — | — | ✓ | review | — | — | — | — |
| Record Board / s.188 reference | — | — | — | — | — | ✓ | — | — | — |
| Engage kill switch | — | ✓ | — | ✓ | ✓ | — | — | — | — |
| Price change ≤ 5% / ≤ 10% | maker | ✓ (≤ 10%) | ✓ (≤ 5%) | — | — | — | — | — | — |
| View cost and margin | — | ✓ | — | read | — | — | ✓ | — | — |
| Toggle tenant-configurable stream | — | — | — | — | — | — | — | — | ✓ (own tenant) |
| Read all transitions and audit | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | own tenant |

**Audit:** every create, edit, transition, kill, price change, test, coupon and related-party record writes a hash-chained audit entry (NN-22) with before/after values; pricing and billing tables sit under the un-disableable edit log (NN-36; Companies (Accounts) Rules 2014 r.3(1) proviso); quarterly exception report to the Board; `internal_auditor` has read access to everything including private fields; evidence exports follow NN-37 folder conventions.

---

## AB.14 Acceptance tests (Gherkin; `tests/acceptance/rev-v3/`)

```gherkin
Feature: Revenue Stream Registry (Appendix AB)

  Scenario: A price cannot be sold without a live stream (RA-8)
    Given plan "CH-LITE" is linked to stream "RS-09" whose scope IN is "approved" but not "live"
    When a neutral requests a checkout for "CH-LITE"
    Then the response is 409 with code "REV_STREAM_NOT_LIVE"
    And CI job "REV_ORPHAN_PRICE" fails for any plan row without a stream_code

  Scenario: Kill switch stops new sales within 5 minutes and keeps run-off
    Given stream "RS-16" is live and tenant T has 3 prepaid room-hours
    When compliance_officer engages the kill switch for "RS-16" with reason "security"
    Then within 300 seconds quotes, checkouts and CMS price blocks for "RS-16" are refused or hidden
    And tenant T can still use its 3 prepaid room-hours
    And release of the kill switch by the same user is refused with "REV_MAKER_CHECKER_SAME_USER"

  Scenario: Prohibited streams never leave draft
    When revenue_manager submits a version of "RS-29" for review
    Then the response is 422 with code "REV_STREAM_PROHIBITED"

  Scenario: Advocates receive no referral reward (master X-62)
    Given a partner record whose legal_reviewer check marks the partner as an enrolled advocate
    When the partner programme computes payouts for "RS-28"
    Then no payout, credit or discount is created
    And a tariff tagged "professional_referral_reward" fails the revenue-denylist job

  Scenario: N2 streams need counsel and Board before approval
    Given stream "RS-19" has a draft version with neutrality_rating "N2"
    And its counsel_opinion dependency is "pending"
    When cfo approves the version
    Then the response is 422 with code "REV_COUNSEL_OPINION_REQUIRED"

  Scenario: Sponsored listings are invisible to allocation (NN-34)
    Given flag "marketplace.paid_placement" is ON in a test environment and neutral N has a sponsored slot
    When the allocation engine runs 10,000 simulated draws for matters where N is eligible
    Then N's selection frequency is statistically indistinguishable from the control run without sponsorship
    And the schema analyser finds no grant from allocation, grading, conflict or directory roles on schema "rev" or "mkp" billing tables

  Scenario: Advocate-neutral bookings use a flat fee, not a percentage take
    Given chambers tenant C on CH-PRO and a marketplace booking with neutral A flagged "enrolled_advocate"
    When the booking settles
    Then the payout statement shows the flat fee "marketplace.advocate_neutral.flat_fee_minor" and no percentage take

  Scenario: Related-party stream blocked without s.188 reference
    Given stream "RS-22" version with a related_party_approval dependency "pending"
    When cfo approves the version
    Then the response is 422 with code "REV_RELATED_PARTY_APPROVAL_REQUIRED"

  Scenario: Price change above 10% needs Board reference
    Given a price change request of +12% on "RS-09"
    When cfo approves it without board_resolution_ref
    Then the response is 422 with code "REV_BOARD_RESOLUTION_REQUIRED"

  Scenario: Price tests never reach consumers
    Given flag "platform.rev.price_tests.enabled" is ON
    When revenue_manager creates a price test on "RS-01" or for segment "individual"
    Then the response is 422 with code "REV_PRICE_TEST_NOT_PERMITTED"

  Scenario: Coupons cannot touch neutral fees or exceed 90 days
    When marketing_manager creates a coupon on a neutral-fee line or valid for 120 days
    Then the response is 422 with code "REV_COUPON_DARK_PATTERN"

  Scenario: Explanation pages come only from approved records
    Given stream "RS-38" version 2 is live and version 3 is draft
    When the CMS renders "/trust/how-we-earn"
    Then the RS-38 entry shows version 2 content and its approval badge
    And a hand-authored price block for RS-38 fails the CMS linter

  Scenario: Cost data stays private
    When marketing_manager calls GET /v1/rev/streams/RS-09
    Then cost_drivers, internal_notes and margin KPIs are absent
    And a direct request for /v1/rev/cost-inputs returns 403 "REV_COST_DATA_RESTRICTED"

  Scenario: Stop proposal needs human approval (v3.1)
    Given stream "RS-41" scored 44 in two consecutive quarterly reviews with all gates passing
    When ViabilityReviewWorkflow runs
    Then a "pause" proposal with a run-off plan is created in rev.viability_proposals
    And the stream stays "live" until revenue_manager accepts and cfo approves the transition
    And if nobody decides within 10 working days the proposal escalates to cfo

  Scenario: Thin data cannot stop a new stream (v3.1)
    Given stream "RS-57" has 4 paying accounts after one quarter live and no gate failure
    When revenue_manager tries to create a "retire" proposal on score alone
    Then the response is 409 "REV_VIABILITY_DATA_INSUFFICIENT"
    And the dashboard shows the stream as "grey"

  Scenario: Neutrality incident recommends, never engages, the kill switch (v3.1)
    Given a substantiated neutrality incident is linked to "RS-19"
    When the gate is evaluated
    Then KS-1 roles are alerted with a kill-switch recommendation within 15 minutes
    And no kill-switch event exists until a KS-1 user engages it
```

---

## AB.15 Phase addenda

### For P05

**FR-P05-V3-AB01 — Registry guard in billing.** Quote, checkout, plan change, coupon redemption, meter rating and invoice issue call `RevenueRegistry.assertLive(stream, scope)`; `core.fee_schedules`, `core.plans` and `core.plan_prices` gain a mandatory `stream_code`. *Acceptance:* §AB.14 scenarios 1 and 2 pass; p95 overhead < 15 ms.

**FR-P05-V3-AB02 — Kill-switch run-off.** Implement KS-3…KS-5 in the entitlement evaluator, quote engine and renewal job; killed-stream renewals stop with a notice; never-suspend list (O §7.1) unaffected. *Acceptance:* paid entitlements continue to period end; renewal notice shows "This service will not renew" and the refund code.

**FR-P05-V3-AB03 — New refund codes.** Add RP-ROOM, RP-SVC, RP-MKP, RP-ADS, RP-EVT, RP-DIG and RP-ASSESS to the refund engine and Appendix B §B.8 in the same PR; U-7 text updated by its owner. *Acceptance:* golden refund vectors per code; credit notes reverse GST (s.34).

**FR-P05-V3-AB04 — Packages and coupons.** `rev.packages`, `rev.package_items`, `rev.coupons`, `rev.coupon_redemptions` with CP-1…CP-8 and allocated-price invoice lines. *Acceptance:* package invoice lines sum to the package price; a coupon on a neutral line or > 90 days is refused; unbundled purchase remains available.

**FR-P05-V3-AB05 — Marketplace tax lines.** Invoice lines for RS-18 and RS-52 record whether Equator collected the consideration; TCS (s.52) and ITA 2025 s.393(1) Sl. 8(v) TDS computed only when `billing.eco_gst_tcs` / `billing.eco_withholding` are ON; GSTR-8 export. *Acceptance:* with flags OFF no TCS/TDS line appears; with flags ON, RCM and exempt supplies are excluded from TCS (GST FAQ Q14–Q15) and TDS applies to the gross amount subject to the ₹5 lakh resident individual/HUF threshold ([RE] F3.4).

**FR-P05-V3-AB06 — Revenue recognition schedules.** Ledger stores a recognition schedule per invoice line by stream family (§AB.4.9) and exports a deferred-revenue roll-forward. *Acceptance:* annual plans recognise rateably; wallet top-ups sit in contract liability until redemption.

### For P10

**FR-P10-V3-AB01 — Chambers add-on streams.** RS-36 rental, RS-37 page themes (OFF), RS-38 custom domains and RS-10 HR-lite (OFF) as add-ons governed by the registry, with tenant toggles where `tenant_configurable`. *Acceptance:* a Solo tenant can buy RS-38 and not RS-37 while RS-37 is OFF; a Lite tenant cannot buy RS-38; themes never alter listing order.

**FR-P10-V3-AB02 — Plan-dependent take and advocate-neutral flat fee.** `chambers.revenue_share_agreements` read take rates from `marketplace.take_rate.<plan>`; neutrals flagged `enrolled_advocate` receive the flat-fee treatment (master X-62). *Acceptance:* §AB.14 advocate-neutral scenario passes; 0% on administered cases unchanged.

**FR-P10-V3-AB03 — Remove advocate credits.** Delete non-cash referral credits for advocate and bar-association tenants (Appendix B Card CH; O X-11), replaced by "no referral rewards" (deny X-21). *Acceptance:* no credit ledger entry of kind `referral` exists for any tenant flagged advocate or bar body.

**FR-P10-V3-AB04 — Tenant revenue settings.** Settings page section "Revenue and pricing" for chambers owners: own fee schedules (B validators), tenant coupons for own fees (CP rules), trial days (0–30), invoice branding, with tier badges (NN-33). *Acceptance:* a tenant cannot widen a platform scope or enable a non-configurable stream (`REV_TENANT_NOT_CONFIGURABLE`).

### For P13

**FR-P13-V3-AB01 — Generated pricing and "How Equator earns".** `/pricing/*` and `/trust/how-we-earn` render only from approved stream versions and published schedules (§AB.2.9); hand-written prices blocked. *Acceptance:* §AB.14 explanation scenario passes; unpublish within 5 minutes of a kill or pause.

**FR-P13-V3-AB02 — Ad and sponsored slots, OFF.** CMS slot components for RS-25 and the marketplace sponsored slot for RS-19 carry the mandatory labels, page-tag exclusions (case, directory, neutral, fee, grievance, POSH) and no third-party ad scripts (DP-13); both render nothing while their flags are OFF. *Acceptance:* label present, capped at 2 slots, CSP has no ad-network hosts.

**FR-P13-V3-AB03 — Prior-price and countdown components.** Strike-through needs a stored prior price and date; countdowns need a fixed server-side end time and are blocked on tagged pages (CP-4, CP-5). *Acceptance:* seeded violating fixtures fail the CMS linter.

### For P19

**FR-P19-V3-AB01 — `rev` schema and seed.** Create the §AB.9 tables, grants (no grant to allocation, grading, conflict, directory roles), edit-log coverage, and seed RS-01…RS-57 from §AB.3 as `draft`. *Acceptance:* seed loads 57 streams; N4 streams cannot leave `draft`; schema analyser confirms RA-11.

**FR-P19-V3-AB02 — Registry console in the Operations Platform.** Screens SCR-P19-AB01 (stream list with status, rating, scope, kill state), SCR-P19-AB02 (version editor with field tiers), SCR-P19-AB03 (review and approval with dependency checklist), SCR-P19-AB04 (scope go-live and pause), SCR-P19-AB05 (kill switch with step-up MFA), SCR-P19-AB06 (price-change requests), SCR-P19-AB07 (packages and coupons), SCR-P19-AB08 (cost inputs, private), SCR-P19-AB09 (KPIs and viability reviews), SCR-P19-AB10 (related-party arrangements). *Acceptance:* every field shows its tier badge, who may change it and whether approval is needed (NN-33); WCAG 2.2 AA.

**FR-P19-V3-AB03 — State machine and guards.** Implement §AB.2.3 transitions with guards and hash-chained transitions. *Acceptance:* §AB.14 N2, related-party and maker-checker scenarios pass.

**FR-P19-V3-AB04 — Kill switch service.** Config-bus event, cache invalidation in all consumers, fail-safe for N2 streams, notifications (KS-6), post-incident review task (KS-7). *Acceptance:* p95 propagation ≤ 60 s measured in staging; chaos test with the bus down denies new N2 sales after 60 s.

**FR-P19-V3-AB05 — Price governance and tests.** `rev.price_change_requests` workflow with the authority matrix (§AB.6.5) as Governed settings; price tests behind `platform.rev.price_tests.enabled` OFF with PT-1…PT-7 and the honour rule. *Acceptance:* §AB.14 price scenarios pass; the honour job credits higher-arm buyers when a lower arm is adopted.

**FR-P19-V3-AB06 — Unit economics and KPIs.** `rev.cost_inputs`, `rev.cost_drivers`, `reporting.rev_*` views (adoption, ARPA, gross margin, contribution, churn, CAC payback, take-rate, complaint and refund rates, neutrality incidents) and the neutrality-exposure tile. *Acceptance:* views read only ledger, usage aggregates, CRM and aggregate Appendix Z time; no individual employee time is exposed.

**FR-P19-V3-AB07 — Viability reviews.** Scheduler creates reviews per cadence; scorecard with gates; decision `go/fix/stop` with maker-checker; stop decisions open a pause-and-retire plan. *v3.1:* RAG dashboard, pack assembly with pre-scores, proposals in `rev.viability_proposals` that never self-execute, grey state for thin data, escalation timers and the urgent kill-switch recommendation (§AB.7.4). *Acceptance:* a stream below the stop score for two consecutive quarters produces a mandatory pause proposal; the three v3.1 scenarios in §AB.14 pass.

**FR-P19-V3-AB08 — Related-party register.** `rev.related_party_arrangements` linked to RS-22 and RS-55, s.184/s.188 references and AOC-2 flag; export for the Board's report. *Acceptance:* RS-22 cannot be approved without a satisfied reference (§AB.14).

---

## AB.16 Open items and legal verification flags

| # | Item | Owner | Effect until resolved |
|---|---|---|---|
| OI-AB-01 | Gazette text, G.S.R. number and commencement of the Consumer Protection (E-Commerce) Amendment Rules 2026 (sponsored labels, ranking parameters, bundling, self-audit) | Counsel | RS-19, RS-25, RS-52 OFF; controls built to the reported text |
| OI-AB-02 | Whether the marketplace percentage take may apply to advocate-neutrals acting only as arbitrators or mediators ([RB] OP-10) | Counsel | Flat fee for advocate-neutrals (X-62(d)) |
| OI-AB-03 | *Sulekha.com v P.N. Vignesh* (SLP (C) 25794/2024) and *Anil Pandey v BCI* (WP (C) 817/2026) outcomes | Counsel | RS-31 OFF; no advocate placement |
| OI-AB-04 | Related-party status of the training site's operator (Infrabyx Consultancy (OPC) Pvt Ltd) and of Finbyx and Udofin under s.2(76); s.188 thresholds | Company Secretary | RS-22, RS-55 OFF |
| OI-AB-05 | Tax memo: SAC codes for SaaS, rentals, events, publications, advertising, sponsored listings, notarisation facilitation; ECO TCS/TDS on marketplace bookings | Tax adviser | `tax_memo_ref = pending` blocks B2C `live`; TCS/TDS flags OFF |
| OI-AB-06 | Closed-system PPI position for wallets and credits (O Q-O5) | Payments counsel | Redemption limited to Equator's own supplies |
| OI-AB-07 | Whether remote or electronic notarisation is lawful in India for the documents Equator handles | Counsel | RS-46 OFF |
| OI-AB-08 | Board approval of margin floors, authority thresholds, package discount cap, coupon caps and the price-testing policy | Board | Defaults shown as "Subject to Board approval" |
| OI-AB-09 | Ind AS 115 treatment of package allocation, breakage and principal/agent for `equator_principal` lines | Statutory auditor, CFO | Conservative treatment (agent for neutral lines; no breakage until pattern evidence) |
| OI-AB-10 | Mediation Council of India conduct standards for mediation service providers (Mediation Act 2023 s.38(l), s.41) and their effect on paid visibility | Counsel | RS-19 OFF |
