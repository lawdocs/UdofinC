# Phase P19 — Equator Marketplace, Infrabyx Professional Registry and Revenue Stream Registry

> Paste after `01_MASTER_PROMPT.md` (v3.0). **Binding references:** Appendix **AA** (Marketplace and Professional Registry — every section), Appendix **AB** (Revenue Architecture v3 and Stream Registry — §AB.2, §AB.3, §AB.6, §AB.8–§AB.15), Appendix N §2.5, §6, §7, §8; Appendix O §1.5, §2.8, §6; Appendix R §4; Appendix S §3, §4.5, §6; Appendix U §U.1, §U.6; Appendix V (configuration framework, tiers L/G/T, `cfg.setting_definitions`); Appendix W (Chambers page builder); Appendix X (Operations Platform: marketplace operations workspace, grievance desk); Appendix Z (`ctl` authority matrix and maker-checker engine).
>
> **Dependencies (must be complete):** **P03** (neutral directory, allocation, conflict graph, blind conflict check), **P05** (fee engine, payments, split settlement, payouts, invoicing, GST), **P10** (Private ADR Chambers tenants, Route linked accounts, overflow), **P15** (configuration framework and settings UI, Appendix V), **P16** (Operations Platform `apps/ops`, Appendix X). Consumed directly: P01 (identity, KYC), P06 (execution and registration support), P09 (enterprise consoles, bulk intake), P13 (CMS, public pages). Estimated effort: 8 sprints (2-week) for a squad of 10 in three sub-squads: Marketplace (4), Registry (3), Revenue and Paid Visibility (3).

---

## 1. Objective and business outcome

Build the Equator Marketplace as a revenue line without weakening the institution's neutrality, give the Infrabyx group one consent-based professional registry, and put every revenue stream under a governed, switchable registry.

| Line | Built here | Business outcome (measurable at the exit gate) |
|---|---|---|
| Private Practice Marketplace (surface (ii)) | Public search and profiles; provider onboarding and verification; enquiry → conflict check → engagement → fee disclosure → booking → payment → delivery → review → complaint; payouts with maker-checker; GST TCS and income-tax withholding as an e-commerce operator; enterprise procurement of ancillary services | A party finds a verified non-advocate mediator, books with both sides' confirmation, pays the GST-inclusive total and the matter opens in the mediator's Chambers tenant; the provider is paid T+3 after the milestone, with TCS/TDS shown on the statement |
| Surface isolation | Three surfaces with no join path; `NO_PAID_PLACEMENT` extended; `MKP_SURFACE_ISOLATION`; `GROUP_SHARE_SCOPE` | CI proves the allocation engine, grading, Quality Index, conflict engine and institutional directory cannot read any marketplace, sponsorship or revenue table |
| Infrabyx Professional Registry (`dir`) and Professional Panel Register (surface (iii)) | Group shared service with consent per purpose, provenance, two-person verification, freshness, propagation of correction/withdrawal/erasure, consumer API for Equator, Finbyx, Udofin and LawDocs; tenant-private panels with RFQs, engagements and SLAs | A lender tenant builds a panel of recovery advocates from professionals who consented to that use; an advocate's erasure reaches every consumer within 72 hours with acknowledgements on record |
| Post-resolution services | Post-Resolution Professional Chooser (legal aid first; own professional; optional Equator Post-Resolution Advocate Panel OFF; in person); item-level document authorisation | Every execution or registration hand-off records the party's choice and consent; Equator never recommends or is paid by a professional |
| Paid visibility (OFF) | Sponsored listings and display advertising built, tested and switched off; dark-pattern self-audit; disclosure in s.12 statements | When the Board and counsel approve, sponsorship can be turned on in one governed change with labels, caps, rotation and audits already proven |
| Revenue Stream Registry | Appendix AB `rev` schema, state machine, kill switches, price governance, KPIs, explanation pages (FR-P19-V3-AB01…AB08) | Every quote, checkout, CMS price block and EOP quote line checks `assertLive`; a kill switch stops new sales of a stream within 60 s (p95) |

---

## 2. Scope (in / out)

**In scope**
- `mkp` module in `apps/api`; `services/registry` (the `dir` service) deployed to the registry owner's account; `REGISTRY_PORT` adapters for Equator (and reference adapters for Finbyx, Udofin, LawDocs consumers); `rev` schema and services (Appendix AB).
- Public marketplace pages in `apps/web` (SSR): `/marketplace`, category and profile pages, `/marketplace/how-ranking-works`, `/marketplace/transparency`, `/marketplace/review-policy`, `/marketplace/content-policy`, `/marketplace/fee-disputes`, `/marketplace/terms`, `/marketplace/provider-terms`, `/marketplace/advertise`, `/trust/dark-patterns`, `/trust/how-we-earn` (AB §AB.2.9).
- Provider portal (web and mobile) and buyer flows (web and mobile).
- Marketplace operations, moderation, verification, enforcement, sponsorship and ad review workspaces inside the Operations Platform (`apps/ops`, Appendix X marketplace operations).
- Registry admin console (owner entity) and professional self-service `/registry/me`.
- Tenant Professional Panel Register module in enterprise and Chambers consoles.
- Post-Resolution Professional Chooser in the case app (P06 hand-off).
- Revenue Stream Registry console (SCR-P19-AB01…AB10 per Appendix AB §AB.15) and runtime enforcement.
- Phase addenda from Appendix AA §AA.24 for P03, P05, P06, P09, P13 are delivered in this phase where they touch P19 components, and in the owning phase's next release train otherwise (listed in §13).

**Out of scope (do not build here)**
- Switching ON any OFF flag: `marketplace.paid_placement`, `platform.rev.ads.enabled`, `directory.public_professionals`, `postres.advocate_panel`, `marketplace.advocate_neutrals.listing`, institute flags, `billing.eco_gst_tcs`, `billing.eco_withholding`, `mkp.provider_subscriptions`, `marketplace.client_processing_fee`. Each needs its named approver (Appendix AA §AA.15); P19 delivers them built, tested and OFF.
- Bulk import of Bar Council rolls or institute directories, or any automated roll look-up (`KYC_PORT.lookupBarRoll.{state}` stays OFF per State).
- Public advocate search (NN-39) and any professional ratings.
- Equator-administered appointment flows (P03) other than the addenda listed.
- Finbyx, Udofin and LawDocs product work beyond the reference `REGISTRY_PORT` consumer adapter and contract tests (their teams integrate).
- The GDSA text, s.188 approvals and the Board designation of the registry owner (business tasks; the product must enforce them as gates).

---

## 3. Personas and permissions touched

| Role code | What it can do in P19 | Key restrictions |
|---|---|---|
| `party` (buyer) | Search; enquire; accept proposals; confirm and pay; confirm milestones; review completed engagements; complain; use the post-resolution chooser | Cannot see sponsorship in any case context; reviews only for completed engagements |
| `party_org_user` / `enterprise_admin` | Procure ancillary services; vendor panels; RFQs; SLAs; reports; lender panel register via `panel_register_*` | `MKP_ENTERPRISE_NEUTRAL_PROCUREMENT_BLOCKED` for neutrals (NN-03) |
| `mkp_provider_owner` | Apply; manage profile (Appendix W builder for Chambers); offerings; availability; proposals; payee and tax data; statements; reply to reviews; order sponsored listings (when ON and eligible); appeal | Payee changes subject to cooling-off; cannot remove reviews |
| `mkp_provider_staff` | Messages, calendar, proposals | No payee, tax or sponsorship actions |
| `chambers_admin` | Link Chambers tenant to marketplace provider; matters from bookings arrive in the tenant | NN guardrails of the tenant (Appendix N §8.3) |
| `marketplace_manager` | Category activation (maker), rate cards (maker), ranking-policy versions (maker), enforcement E1–E3, transparency report publication | Cannot approve own changes |
| `marketplace_moderator` | Profile, review and content moderation; complaint triage support | Recuses on own conflicts |
| `provider_verifier` | Credential and professional-status verification (two-person) | Second verifier ≠ first |
| `ad_reviewer` | Sponsored creatives and display ads (maker) | — |
| `compliance_officer` | Checker on ranking, sponsorship, ads, transparency, dark-pattern audit; related-party flags | — |
| `legal_reviewer` | Category law checks; flag evidence; policy documents | — |
| `grievance_officer` | Marketplace grievance desk (Appendix X), clocks, NCH convergence | — |
| `finance_ops`, `accounts_maker`, `accounts_checker`, `finance_controller`, `cfo` | Tax memo flags; payout batches (maker/checker/second approver); reconciliation; rate cards and take rates | SoD (NN-36) |
| `revenue_manager` | Stream registry maker (Appendix AB) | Maker ≠ checker |
| `registry_steward`, `registry_verifier` | Registry owner operations: verification, freshness, DSRs, consumer onboarding | Owner entity staff only; no access to tenant notes |
| `panel_register_admin`, `panel_register_user` | Tenant-private panels, invitations, RFQs, engagements, SLAs, private notes | Own tenant only (`DIR_TENANT_SCOPE`) |
| Professional (advocate, CA, CS, CMA, valuer, process agent) | Self-register; consents per purpose; corrections; withdrawal; erasure; see distribution log; accept panel invitations; respond to RFQs | Never pays; never rated publicly |
| `group_admin` | Consumer registrations and purposes under GDSA | Purpose grants need Owner DPO checker |
| `internal_auditor` | Read-only on all P19 evidence | Time-boxed grant |
| `machine` | Consumer API clients (`Equator-Purpose` header) | Purpose-bound; no bulk endpoints |

New roles are registered in Appendix S §6 (v3) and Appendix V `cfg` role catalogue in the first P19 migration.

---

## 4. Functional requirements

### 4A. Surface isolation and firewall

**FR-P19-01 — Three surfaces, no join path.** Implement surfaces (i), (ii) and (iii) exactly as Appendix AA §AA.2.1. Create database roles per service; revoke every grant on `mkp`, `rev` and `dir` (other than the F2 conflict-signal consumer) from the allocation, grading, Quality Index, conflict, institutional-directory and AI Gateway roles (AA.2.2 rule 1). *Acceptance:* schema analyser lists zero cross-surface grants outside `config/mkp_flow_allowlist.yaml`; `MKP_SURFACE_ISOLATION` passes on main and fails on a seeded forbidden view.

**FR-P19-02 — `NO_PAID_PLACEMENT` extended.** Extend the existing CI test to cover `mkp.sponsorship_*`, `mkp.ad_*`, `mkp.provider_subscriptions` and all `rev` tables (AA.10.6; AB RA-11). Add runtime assertion: the allocation service refuses to start if its role has any grant on those schemas. *Acceptance:* toggling sponsorship, plan, related-party and stream attributes in the golden-vector allocation suite changes nothing (`RANKING_IGNORES_PAID`, allocation variant).

**FR-P19-03 — Allowed flows only.** Implement flows F1–F5 (AA.2.2 rule 4) and nothing else: identity link by the person; conflict-signal edges from `dir.panel_memberships` and closed `mkp.engagements` (payload `person_ref`, `organisation_id`, dates only); sponsorship boolean to the disclosure module; blind conflict check. *Acceptance:* contract tests reject any extra field in F2/F3/F4 payloads; the conflict engine cannot query `dir` directly.

**FR-P19-04 — Case-context suppression.** Sponsored slots, ads and marketplace promotions never render for a viewer with an open Equator-administered matter, nor on any page tagged `case`, `hearing`, `notice`, `grievance`, `posh`, `fees_case`, nor in notices and e-mails (AA.10.3 rule 2; Appendix O X-15). Cerbos `DENY` on `mkp:sponsorship` and `mkp:ad` for case roles (AA.16). *Acceptance:* `NO_SPONSOR_IN_CASE_CONTEXT` passes across web and mobile render tests.

### 4B. Provider categories, onboarding and verification

**FR-P19-05 — Category register as rule packs.** Seed `mkp.provider_categories` and rule packs `rulepack.IN.mkp.category.<code>@2026.1` for every row of AA.3.1, with eligibility, evidence, verification method, re-verification cycle, law check, reviews flag, sponsor-eligible flag and take flag. A category becomes active only after `legal_reviewer` signs its law check (maker `marketplace_manager`). `SVC-EST` and `SVC-VEN` ship OFF; excluded categories (AA.3.1) cannot be created (`MKP_CATEGORY_DISABLED`). *Acceptance:* a category without a signed law check cannot accept applications; rule-pack versions pinned on each provider category link.

**FR-P19-06 — Professional-status rules.** Enforce AA.3.2: advocates and CA/CS/CMA members as professionals never list on surface (ii) (`MKP_PROFESSIONAL_NOT_ALLOWED`); institute-member neutrals only while their institute flag is ON with a uniform entry; advocate-neutrals only while `marketplace.advocate_neutrals.listing` is ON, with Schedule fields, no photo or video, no reviews, "Fees on request", no sponsorship, no take. *Acceptance:* Gherkin "Advocate cannot list as a service provider", "Advocate-neutral listing hidden while flag OFF".

**FR-P19-07 — Application and KYC/KYB.** Implement AA.4.1 steps 1–2: category choice; identity level per category (Appendix S §3.1); declarations (professions, related-party, conflicts, disciplinary, convictions wording **[VERIFY — open: counsel]**); DPDP notice; per-field display consents; PAN, GSTIN, MCA21 KYB, Aadhaar only via OVSE/DigiLocker (NN-14); penny-drop; sanctions screen for foreign providers. Reference `EQ/MKP/{YYYY}/{NNNNN}`. *Acceptance:* acknowledgement ≤ 2 working days tracked as an SLA with owner; drafts archived at 90 days.

**FR-P19-08 — Two-person credential and status verification.** `mkp.provider_credentials` with source, method, evidence hash in Object Lock storage, `verifier_1 ≠ verifier_2` (DB CHECK and Cerbos). Professional-status look-ups are manual and evidenced (AA.4.3); CI `NO_ROLL_SCRAPING` blocks scheduled jobs and HTTP clients targeting hosts in `dir.blocked_source_hosts`. *Acceptance:* same-user second verification returns 403; a scheduled job calling a roll-portal host fails CI.

**FR-P19-09 — Agreements, payout and tax setup.** E-sign `MPT-2026.1`, `MPC-2026.1` (and ECC-2026.1 for neutrals); payee account with penny-drop, out-of-band confirmation and cooling-off (AA.7.6); tax profile (GST status, GSTIN, PAN-Aadhaar link status for TDS threshold, TDS certificate e-mail); Chambers Route linked account link. *Acceptance:* `listed` impossible until all guards pass (AA.4.2); payee in cooling-off blocks payouts (`MKP_PAYEE_COOLING_OFF`).

**FR-P19-10 — Profile build, moderation, quality and offboarding.** Profile via Appendix W page builder (Chambers) or the provider profile form, constrained to the AA.5.4 allow-list; moderation with copy lint (`MKP_LABEL_FORBIDDEN`: "top", "best", "premium", "recommended", "featured", "expert", "specialist", "No. 1", outcome claims, "court"); quality signals (AA.4.5) with outcome metrics forbidden (`MKP_OUTCOME_METRIC_FORBIDDEN` CI); re-verification T-30/T-7 and annual; freshness label at 12 months and hide at 18; offboarding with run-off, reviews retained, export and erasure 30 days after run-off (AA.4.6). *Acceptance:* Gherkin "Stale profile hidden at 18 months", "Forbidden label blocked".

### 4C. Search, ranking and profiles

**FR-P19-11 — Public, server-rendered search.** `/marketplace` SSR with filters exactly as AA.5.1; first results page works without JavaScript; facet counts suppressed below 3; compare up to 3; no ad pixels. OpenSearch index `mkp-listings-{env}` built from `mkp.listings` published versions only. *Acceptance:* Lighthouse SEO ≥ 95, accessibility ≥ 95; WCAG 2.2 AA; build check fails on a client-only shell (master §4.1).

**FR-P19-12 — Governed ranking policy.** `packages/rules/mkp-ranking` implements `MKP-RANK-2026.1` (AA.5.3): hard filter match → availability tier → language tier → freshness tier → session-seeded random rotation. Policy object `mkp.ranking_policies` is G-tier (maker `marketplace_manager`, checker `compliance_officer`, legal sign-off), versioned, effective-dated, published with a 30-day notice and changelog; the published page hash is stored and compared on deploy (`RANKING_PARAMS_PUBLISHED`). Unknown `sort` → `MKP_SORT_NOT_ALLOWED` (400). *Acceptance:* golden vectors GV-MKP-01…05 reproduce orders for fixed seeds; toggling sponsorship, plan, rating, booking count, related-party or Equator panel status produces identical organic order (`RANKING_IGNORES_PAID`).

**FR-P19-13 — "Why am I seeing this?"** Every organic and sponsored card has an explanation popover listing tiers met (organic) or the sponsorship statement (AA.10.3 rule 3). *Acceptance:* DOM test on 100 random searches.

**FR-P19-14 — Profiles and seller details.** Profile pages per AA.5.4 including the seller details panel (legal name, registration status, address, customer care, website and e-mail, GSTIN/Udyam), related-to-Equator label (AA.3.3), paid-visibility disclosure when sponsoring, complaint link and the fixed institutional statement. Never-displayed list enforced by `R36_PROFILE_ALLOW_LIST` (professionals) and the marketplace allow-list lint (others). *Acceptance:* E-Commerce r.5(3)(a)/r.6(5)(j) checklist test passes for each category; `aggregateRating` never emitted.

**FR-P19-15 — Marketplace assistant (optional).** If enabled (`mkp.assistant.enabled`, T, default OFF), the assistant explains filters, categories, fee models and processes; it never ranks, recommends or names a provider, never uses sponsorship, plan or fees paid, and logs prompts and answers (AA.5.2; [RA] EQM-09). *Acceptance:* eval set `mkp-assistant-neutrality` (200 prompts) shows zero named-provider recommendations.

### 4D. Booking journey

**FR-P19-16 — Enquiry and messaging.** Enquiry form and inbox per AA.6.2; PII redaction preview; off-platform-payment lint (warning, never a block on direct contact); provider response clock 2 working days; expiry at 7 days with one notice. *Acceptance:* Gherkin "Enquiry expires with a single notice".

**FR-P19-17 — Conflict check before proposal.** Neutral and expert categories require a conflict check: tenant conflict graph plus `POST /v1/conflicts/blind-check` (P03 FR-P03-32); `hard` blocks (`MKP_CONFLICT_HARD`); `disclosable` requires a written disclosure to all parties (A&C s.12(1), Sixth Schedule format for arbitrators); panel-counsel edges (`counsel_panel_of`) are hard conflicts for bookings involving that organisation; group relationships trigger `CommercialRelationshipNotice` (NN-16). Service categories record a declaration. *Acceptance:* Gherkin "Lender's panel advocate blocked as mediator in lender's dispute".

**FR-P19-18 — Neutral booking guardrails.** Implement AA.6.4: arbitrator bookings need every party (`MKP_ONE_PARTY_ARBITRATION_BLOCKED`); repeat-player initiator vs individual counterparty blocks arbitration (`MKP_REPEAT_PLAYER_ARBITRATION_BLOCKED`) and requires informed acceptance for mediation with links to the administered route and free statutory forums (NN-20); FAM safety-flagged, POSH and criminal matters not bookable; "move to private" step for disputes with an open Equator case. *Acceptance:* one Gherkin scenario per rule.

**FR-P19-19 — Engagement proposal and fee disclosure.** `mkp.engagements` proposals with scope, fee disclosure per component (provider fee, Equator fee lines if any, GST or RCM note, pass-throughs, total), ADR-native milestones, refund and cancellation terms, disclosures (conflict, paid visibility, related-to-Equator, group relationships), pinned terms versions; validity 7 days; variations through the same path. Fee figures come from the provider's published offerings and the P05 fee engine. *Acceptance:* confirmation without an accepted disclosure returns `MKP_FEE_DISCLOSURE_REQUIRED` (409); the disclosure hash equals the checkout hash (Appendix O DP-07).

**FR-P19-20 — Explicit confirmation and joint booking.** Unticked confirmation checkbox and "Confirm and pay" showing the total including GST (E-Commerce r.4(9); NN-29); no pre-selected add-ons; for neutral services every party confirms; first payment held at the PA (`on_hold` transfer) for `platform.mkp.hold_days` (14) and auto-refunded if not all confirm. *Acceptance:* Gherkin "Hold refunded when counterparty declines"; no pre-ticked control in any marketplace checkout (`ECOM_no_preticked`).

**FR-P19-21 — Matter creation in the provider's tenant.** On confirmation create the matter in the provider's Chambers tenant with `source = 'private_marketplace'` (X-59), engagement `confirmed`, calendar holds; hand off to the Chambers workspace (P10). *Acceptance:* the matter is invisible to Equator registry roles; Equator-administered case lists never show it.

**FR-P19-22 — Service delivery for service categories.** Task workspaces per AA.6.8: secure links to selected documents only (Appendix L §2.6), interpreter channel for booked sessions, process-agent delivery tasks with proof-of-delivery, report uploads; every disclosure from an Equator case writes `core.disclosures`. NN-11: stenography in mediation is blocked; arbitration transcription only with all consents. *Acceptance:* revoking a link ends access in the same transaction; mediation transcription booking returns 422.

**FR-P19-23 — Milestones, deemed release and fee disputes.** Milestone confirmation by buyer within 5 working days, notice at day 3, deemed release with notice; milestone dispute holds funds and opens the fee-dispute procedure `MKP-FDP-2026.1` (7-day direct window → independent fee reviewer not on the provider's panel, Equator staff recused) (AA.6.9). *Acceptance:* Gherkin "Disputed milestone stays on hold until the fee reviewer decides".

### 4E. Payments, tax and payouts

**FR-P19-24 — Collection model and tax-memo gate.** Implement `platform.mkp.collection_model` (`provider_merchant_of_record` default; `equator_collects_as_eco`) and the gate `tax_memo.mkp_eco_recorded`: while false, paid bookings are blocked (`MKP_TAX_MEMO_MISSING`, 409) and only free enquiries work (AA.2.4 rule 5). *Acceptance:* the toggle requires CFO maker and `legal_reviewer` checker with the tax memo document attached.

**FR-P19-25 — Take and advocate-neutral flat fee.** Apply `marketplace.take_rate.<plan>` and `marketplace.take_rate.service_providers` to non-advocate bookings at source; for advocate providers apply no take and no deduction, and add `marketplace.advocate_neutral.flat_fee_minor` as a buyer-side line (RS-18 `flat_per_booking`; master X-62(d)); 0% on administered cases. Take is invoiced monthly to the provider with GST. *Acceptance:* tariff lint `ADVOCATE_TARIFF_LINT` green; statements show the plan rate; RS-52 lines absent while `marketplace.client_processing_fee` is OFF.

**FR-P19-26 — GST TCS engine.** AA.7.3: supply characterisation, exclusions for exempt and RCM supplies (advocate and arbitral-tribunal services to business entities, Notification 13/2017-CT(Rate) entries 2–3), rate `platform.tax.gst_tcs_rate` (0.5%, Notification 15/2024-CT), monthly base per supplier GSTIN, GSTR-8 data file, supplier statements; behind `billing.eco_gst_tcs` (OFF). *Acceptance:* golden vectors TCS-01…TCS-08 (registered mediator B2C; registered mediator B2B; unregistered provider; arbitral tribunal to business (RCM, no TCS); exempt supply; returns in month; inter-State IGST; composition supplier per memo).

**FR-P19-27 — Income-tax withholding engine.** AA.7.4: 0.1% of gross at earlier of credit or payment, ₹5,00,000 threshold for resident individual/HUF with PAN or Aadhaar, no threshold otherwise, interaction mode from the tax memo; quarterly return data and certificates; behind `billing.eco_withholding` (OFF). *Acceptance:* vectors TDS-01…TDS-05 including threshold crossing mid-year.

**FR-P19-28 — Payout batches with SoD.** Nightly batch preparation; `accounts_checker` approval with step-up MFA; second approver (`finance_controller`) above the `ctl` authority-matrix limit; release via PAYOUT_PORT; reconciliation by a user other than the approver; new-provider holds for the first 3 engagements; payout SLA T+3 (AA.7.5). *Acceptance:* `MKP_PAYOUT_SOD_VIOLATION` when the approver tries to reconcile; un-disableable edit log on payout, payee and tax tables (NN-36).

**FR-P19-29 — Refunds, credit notes and RP-MKP.** Refund code RP-MKP (Appendix AB §AB.5): take and processing fees follow the booking and are never retained on refunds for provider non-delivery; stage refunds per offering; cancellation symmetry; refunds to original instrument; credit notes reverse GST (CGST s.34); TCS/TDS reversal per memo. *Acceptance:* Gherkin "Provider cancels late — buyer refunded in full and offered rebooking".

### 4F. Reviews, complaints, enforcement, takedown, transparency, fraud

**FR-P19-30 — Process-only reviews.** AA.8.1: eligible reviewers only; invitation 48 h after completion; 30-day window; question sets per category with no outcome items (`MKP_REVIEW_OUTCOME_ITEM` schema lint); no incentives; display at n ≥ 10; moderation ≤ 72 h with published policy; right of reply; licence limited to listing period + 30 days; never for advocates, institute members or surface (iii) professionals (`MKP_REVIEW_PROFESSIONAL_FORBIDDEN`). *Acceptance:* Gherkin "Public review score appears only at ten", "No review for advocate provider".

**FR-P19-31 — Marketplace grievance desk.** Complaint intake channels; named Marketplace Grievance Officer on every page and invoice; clocks 48 h acknowledgement and one-month redress (E-Commerce r.4(5)), 7-day intermediary grievances and 3-hour specified-content takedown (IT Rules amendment 2026 [P]); complaint copy to complainant; NCH convergence adapter behind `mkp.nch_integration.enabled` (G, OFF until the specification is confirmed) **[VERIFY — open]**; severity S1–S3 with S1 interim suspension. Integrates with the Appendix X grievance desk (`rulepack.IN.grievance.ecommerce@2026.1`, and `@2026.2` from commencement of the 2026 Amendment; Appendix X §X.8.3). *Acceptance:* clock breach raises an owned incident; Gherkin "S1 complaint suspends new enquiries within 5 minutes".

**FR-P19-32 — Enforcement ladder and appeals.** E1–E5 and interim measures with reasons mandatory (`MKP_REASONS_REQUIRED`), 15-day reply window, Marketplace Review Panel (two members independent of sales and ad operations, one from Legal and Compliance), Marketplace Appeals Panel with an external member, decisions ≤ 30 days (AA.8.3). *Acceptance:* a sales or ad-ops user cannot be added to either panel (composition validator).

**FR-P19-33 — Takedown and content policy.** Takedown queue with per-category clocks (`MCP-2026.1`; AA.8.4), reasons to the provider, counter-notice, logs. *Acceptance:* 3-hour clock category list is a G setting with citation **[VERIFY — open: G.S.R. 120(E) categories]**.

**FR-P19-34 — Quarterly transparency report.** Versioned query pack, dataset hash, n < 10 suppression, Claims Register entries, contents per AA.8.5 including sponsored and ad revenue shares, `compliance_officer` approval, publication by `marketplace_manager`. *Acceptance:* the report regenerates byte-identically from the stored query pack version and dataset hash.

**FR-P19-35 — Fraud controls.** `mkp.fraud_signals` with detectors per AA.8.6 (fake identity, false credentials, review farming, collusive bookings, bank-detail fraud, off-platform demands, sponsored-slot abuse, insider manipulation); actions through the enforcement ladder; quarterly internal-audit sample export. *Acceptance:* seeded review-farming pattern is flagged and held before publication.

### 4G. Enterprise procurement

**FR-P19-36 — Neutral procurement block.** Enterprises cannot create vendor panels, RFQs or bulk requests in neutral categories (`MKP_ENTERPRISE_NEUTRAL_PROCUREMENT_BLOCKED`, 403; AA.9.1). *Acceptance:* Gherkin "Lender cannot empanel mediators".

**FR-P19-37 — Ancillary procurement engine.** Bulk intake (CSV/XLSX/API, validation report, per-row errors, idempotency), enterprise vendor panels with acceptance of panel terms, RFQs with comparison grid (totals incl. GST) and award reasons, SLA policies with owned clocks and defined credits, enterprise reporting and exports (AA.9.2). Shared pure logic in `packages/procurement`, also used by the registry RFQ module (FR-P19-53). *Acceptance:* a 2,000-row translation request validates in ≤ 2 minutes; SLA breach credits computed deterministically.

**FR-P19-38 — Finbyx and Udofin use cases.** Seed and demo the four flows of AA.9.3 end to end in sandbox (lender recovery-advocate panel via Finbyx consumer; award execution by a Udofin partner lender; translation vendor panel; valuer engagement). *Acceptance:* `GROUP_SHARE_SCOPE` green; no case or allocation data leaves Equator.

### 4H. Paid placement and display advertising (built, OFF)

**FR-P19-39 — Sponsor eligibility.** Implement `sponsor_eligible()` (AA.10.2) as a pure function in `packages/rules/mkp-sponsor`, with each failing condition returned in the problem detail (`MKP_SPONSOR_INELIGIBLE`, 422). *Acceptance:* table-driven tests for every condition, including advocate, law firm, chambers with an advocate-neutral, institute member, related party, open S1/S2, enforcement ≥ E3, MCI rule pack prohibition.

**FR-P19-40 — Sponsored inventory, rate card, ordering.** `mkp.sponsorship_products` per category × geography; equal published rate card (Board-approved schedule only, `SCHEDULE_NOT_APPROVED`); orders with eligibility → creative from verified profile only → `ad_reviewer` maker → `compliance_officer` checker → activation on the 1st; e-mandate or prepaid; per-sponsor cap; pro-rata refund rules (AA.10.3 rules 4–6). All endpoints return `MKP_PAID_PLACEMENT_OFF` (409) while the flag is OFF, and `REV_STREAM_NOT_LIVE` while RS-19 is not live. *Acceptance:* order flow passes end to end in a test environment with the flag forced ON; production config proves OFF.

**FR-P19-41 — Sponsored rendering and rotation.** Separate block above organic results; label "Sponsored — paid placement. Does not affect Equator appointments." in the provider-name font size, adjacent to the name; dismissible per session; never interleaved; cap `marketplace.paid_placement.max_slots_per_page` (2) and 20% of results; weighted round-robin rotation with session seed; daily aggregated impressions only; monthly rotation fairness report with credits when outside ±5% (AA.10.3 rules 2, 3, 5). *Acceptance:* `SPONSORED_LABEL_PRESENT`, `SPONSORED_NOT_INTERLEAVED`, `SPONSORED_SLOT_CAP` visual-regression and DOM tests pass on web and mobile.

**FR-P19-42 — Ranking and sponsorship disclosure page.** `/marketplace/how-ranking-works` renders the live ranking policy and the sponsored-listing rules from `MRS-2026.1`, with the first-paragraph statement in AA.10.4 and links to the rate card and transparency report. *Acceptance:* page version equals the deployed policy version (`RANKING_PARAMS_PUBLISHED`).

**FR-P19-43 — Dark-pattern self-audit.** Annual self-audit workflow (AA.10.5): automated DP-01…DP-13 test results, manual walkthrough with second signer from Internal Audit, findings and remediation tickets, signed report, certificate displayed on `/trust/dark-patterns` and the marketplace footer; overdue audit blocks re-enabling sponsorship (`MKP_DARK_PATTERN_AUDIT_OVERDUE`); monthly sponsored-listing operations audit (RB AU-25) feeds it. *Acceptance:* the AB `approved → live` guard for N2 streams reads the current certificate.

**FR-P19-44 — Display advertising on content pages.** Advertiser KYB, policy categories (allowed and prohibited per AA.10.8), campaigns, creatives with copy lint, first-party serving from `mkp.ad_creatives`, slot component allowed only on `content`-tagged CMS pages, label "Advertisement", ≤ 2 per page, no third-party scripts or pixels, server-side aggregate impression counts; behind `platform.rev.ads.enabled` (OFF). *Acceptance:* `MKP_AD_PLACEMENT_FORBIDDEN` on forbidden tags; `MKP_AD_CATEGORY_PROHIBITED` for a lender, law firm or neutral advertiser; bundle scan finds no third-party ad script.

### 4I. Post-resolution services

**FR-P19-45 — Post-Resolution Professional Chooser.** SCR-P19-30 replaces SCR-P06-65 (X-60): options in order — free legal aid (individuals; DLSA/SLSA for the district; LSA Act 1987 s.12 summary), own professional (invite; verification via Appendix S §4.5), Equator Post-Resolution Advocate Panel (only if `postres.advocate_panel` ON), act in person; fixed banner; `mkp.postres_choices` append-only with options shown and order seed. *Acceptance:* Gherkin "Party chooses the professional"; no ranking, rating or fee field exists in the chooser.

**FR-P19-46 — Authorised document transfer.** Item-level authorisation via representative scope `view_documents` + `court_steps_support` (Appendix S §4.3) or secure link (Appendix L §2.6); each item writes `core.disclosures` (`ENFORCEMENT`, `REGISTRATION`, `PARTY_COUNSEL`); one-step revocation; registration and execution trackers record `acting_professional_ref` and label professional-entered milestones (AA.11.3, AA.11.5). *Acceptance:* revocation ends access in the same transaction; disclosure log export lists each item.

**FR-P19-47 — Equator Post-Resolution Advocate Panel (OFF).** Equator tenant panel register `EQ-POSTRES` on the registry; membership by consent to `postres_panel` and acceptance of `PRP-2026.1` (free listing; no fee-share, commission, referral fee or reward; no ratings; Schedule fields only); seeded-random within State, district, court type, language and area filters (languages and courts as filter-only metadata); per-case hiding of advocates who acted as neutral, for any party, or as Equator staff; annual reconfirmation; removal on disciplinary order; shown only in-case to authenticated parties after an outcome exists (AA.11.4). *Acceptance:* flag OFF in production; with the flag forced ON in test, no public route, SEO page or sitemap entry exists.

### 4J. Infrabyx Professional Registry (`dir`)

**FR-P19-48 — Registry service and owner gate.** Deploy `services/registry` to the owner entity's AWS account (ap-south-1; DR ap-south-2) with its own Aurora cluster `grp-registry`, KMS keys and RLS by `consumer_entity_id` and `tenant_ref` (AA.2.3). Go-live blocked while `group.dir.owner_entity_id` is unset or lacks a Board resolution reference. Equator consumes only through `REGISTRY_PORT`. *Acceptance:* Equator `apps/api` has no database credentials for `grp-registry`; the owner gate blocks consumer onboarding.

**FR-P19-49 — Consumers and GDSA gate.** `dir.consumers` and `dir.gdsa_agreements` with allowed purposes per consumer; OAuth2 client credentials per consumer; consumer onboarding maker `group_admin`, checker Owner DPO; no GDSA → `DIR_GDSA_MISSING` (403); s.188 reference recorded where consideration is payable (shared-services register). *Acceptance:* a consumer without a live GDSA receives 403 on every endpoint.

**FR-P19-50 — Professional self-registration and type allow-lists.** `/registry/me` self-registration and invitation claiming; types and allow-lists per AA.12.2–AA.12.3; filter-only metadata never rendered; display order alphabetical or seeded-random (`DIR_SORT_NOT_ALLOWED`); tenant uploads create invitations, never records (`DIR_BULK_IMPORT_FORBIDDEN`). *Acceptance:* `R36_PROFILE_ALLOW_LIST` passes on every API response and view; a CSV of enrolment numbers yields invitations only.

**FR-P19-51 — Consent per purpose.** Purposes per AA.12.4 with notice versions, recipients named, affirmative action, one-toggle withdrawal; consent artefacts exportable; API returns only records whose consent covers the caller's purpose and recipient (`DIR_PURPOSE_NOT_GRANTED`). *Acceptance:* Gherkin "Finbyx cannot see a record consented only for Equator".

**FR-P19-52 — Provenance, two-person verification and freshness.** Field provenance and evidence hashes (AA.12.5); two-person verification (`DIR_VERIFIER_SAME_PERSON`); CoP 5-year cycle plus annual Equator check; reconfirmation label at 12 months and hide at 18 (`DIR_RECORD_STALE`); lapse or Council suspension published as an update within 1 hour of recording. *Acceptance:* freshness job tests with clock control; update event within SLA.

**FR-P19-53 — Professional Panel Register.** Tenant-private `dir.panel_registers`, invitations, memberships with panel-terms versions (lint blocks fee-share, referral or success terms), RFQs and responses (shared procurement logic), engagements with opaque matter references, SLA policies, private tenant notes that never leave the tenant (`DIR_TENANT_SCOPE`); pricing per tenant/seat/module only (`DIR_PER_ENGAGEMENT_PRICING_FORBIDDEN`); professionals never pay; no rating fields outside tenant notes; cross-tenant analytics aggregate only (k ≥ 10) (AA.12.6). *Acceptance:* Gherkin "Tenant notes are invisible to another tenant and to the registry owner".

**FR-P19-54 — Propagation and reconciliation.** Outbox events `equator.dir.record.updated|withdrawn|erased.v1` to every consumer in `dir.distribution_log`; ACK endpoint; reminders at 24 h; `DIR_PROPAGATION_OVERDUE` incident to both DPOs at 72 h; nightly reconciliation of consumer projection hashes; drift tasks; `retained_for_legal_obligation` flags with basis (AA.12.7). *Acceptance:* Gherkin "Registry erasure propagates within the SLA"; reconciliation detects a seeded drift.

**FR-P19-55 — Consumer API and access logging.** Endpoints in AA.18 (registry block); `Equator-Purpose` header mandatory; filter-required search (type + State), ≤ 50 per page, no bulk export; rate limits per consumer; every response logged in `dir.access_logs` (partitioned monthly); no unauthenticated access while `directory.public_professionals` is OFF (`DIR_PUBLIC_SEARCH_OFF`, 404). *Acceptance:* contract tests for each consumer adapter; attempt to page beyond limits is throttled.

**FR-P19-56 — Data-principal rights and distribution log.** Access, correction, erasure and grievance through `/registry/me` with effort equal to sign-up; `GET /v1/registry/me/distribution` shows who received the data and when; DSR clocks per Appendix Q. *Acceptance:* DSR test suite (access, correction, erasure, withdrawal) passes across Owner and two consumers.

### 4K. Revenue Stream Registry (Appendix AB implementation)

**FR-P19-57 — `rev` schema, seed and grants.** Implements **FR-P19-V3-AB01**: Appendix AB §AB.9 tables, grants (none to allocation, grading, conflict or directory roles), edit-log coverage, seed RS-01…RS-57 as `draft` (`rev_v3_seed`). *Acceptance:* 57 streams loaded; N4 streams cannot leave `draft` (`REV_STREAM_PROHIBITED`).

**FR-P19-58 — Registry console.** Implements **FR-P19-V3-AB02**: SCR-P19-AB01…AB10 in the Operations Platform with NN-33 tier badges, who may change each field and whether approval is needed. *Acceptance:* WCAG 2.2 AA; private columns hidden by role (`REV_COST_DATA_RESTRICTED`).

**FR-P19-59 — State machine, maker-checker and neutrality rating.** Implements **FR-P19-V3-AB03** (AB §AB.2.3–§AB.2.4): transitions with guards (dependencies satisfied; N2 requires counsel opinion, Board resolution and current dark-pattern certificate; related-party requires s.188 reference; tax memo for B2C), hash-chained `rev.stream_transitions`, self-approval blocked (`REV_MAKER_CHECKER_SAME_USER`). *Acceptance:* AB §AB.14 N2, related-party and maker-checker scenarios pass.

**FR-P19-60 — Kill switch service.** Implements **FR-P19-V3-AB04** (AB §AB.2.5): config-bus event `equator.rev.stream.killed.v1`; cache invalidation in EntitlementService, quote engine, CMS renderer, CPQ, EOP campaign engine, marketplace sponsored-slot renderer and ad server; fail-safe deny for N2 streams if the bus is unavailable > 60 s; notifications within 15 minutes; post-incident review task. *Acceptance:* p95 propagation ≤ 60 s in staging; chaos test with the bus down denies new RS-19/RS-25/RS-18 sales after 60 s; run-off obligations continue.

**FR-P19-61 — Runtime enforcement everywhere money is offered.** `GET /v1/rev/check` (`assertLive`, p95 < 15 ms cached) called by P05 quote and checkout, P13 CMS price blocks and CTAs, EOP quotes (Appendix X §X.4.3), marketplace booking (RS-18, RS-52), sponsorship orders (RS-19), ad campaigns (RS-25), panel-management subscriptions (RS-30), service-provider tools plans (RS-57), hearing-room rentals (RS-16); failure returns `REV_STREAM_NOT_LIVE`. Every invoice line carries `stream_code` (FK `rev.streams(code)`). *Acceptance:* contract test per consumer; a killed stream disappears from new quotes within 5 minutes.

**FR-P19-62 — Price governance and tests.** Implements **FR-P19-V3-AB05**: price-change requests with the authority matrix (AB §AB.6.5) as G settings in `ctl`; A/B tests behind `platform.rev.price_tests.enabled` (OFF) with PT-1…PT-7 and the honour rule; never on case fees, neutral fees, consumer prices or marketplace provider fees. *Acceptance:* AB §AB.14 price scenarios pass.

**FR-P19-63 — Unit economics, KPIs and neutrality-exposure tile.** Implements **FR-P19-V3-AB06**: `rev.cost_inputs`, `rev.cost_drivers`, `reporting.rev_*` views including take-rate realised, complaint rate per 1,000 sponsored impressions and neutrality incidents; finance dashboard tile showing N1 and N2 revenue share. *Acceptance:* views read only ledger, usage aggregates, CRM and aggregate Appendix Z time.

**FR-P19-64 — Viability reviews, related-party register and explanation pages.** Implements **FR-P19-V3-AB07** and **FR-P19-V3-AB08**; generates `/trust/how-we-earn` and stream explanation pages only from approved or live versions (AB §AB.2.9), unpublishing within 5 minutes when a version stops being live (`REV_EXPLANATION_STALE`). *Acceptance:* a stream below the stop score for two consecutive quarters produces a mandatory pause proposal; RS-22 cannot be approved without a satisfied related-party reference.

### 4L. Governance documents, settings and exports

**FR-P19-65 — Marketplace and registry policy documents.** Register AA-1…AA-11 (AA.13) in the policy registry (`core.procedure_rules`) with owners, approvers, versioning, 30-day change notices and re-consent prompts; public pages render from the registry only. *Acceptance:* a CMS edit of policy text is blocked by the linter.

**FR-P19-66 — Settings registration.** Register every key in AA.15 and AB §AB.8 in `cfg.setting_definitions` (Appendix V D3-11) with tier, scopes, type, bounds, default, fallback, owner role and audit class; aliases per X-59 (h) and Appendix V X-44 alias registry. *Acceptance:* CI fails on any unregistered key read by P19 code.

**FR-P19-67 — Exports (NN-37).** Provider export (scope `MARKETPLACE_PROVIDER`), professional export (`USER_SELF` via `dir`), tenant panel export (within `ENTERPRISE_TENANT`) and regulatory packs (`STATUTORY_BOOKS`, `ASSURANCE_PACK`) per AA.21, built by the P21 export service with the D3-41 / Appendix AC §AC.13 taxonomy and naming (`00_README.pdf`/`.html`, `00_Contents.xlsx`, numbered folders, `99_Manifest/` with manifest CSV + JSON and SHA-256), DOCX/XLSX/PDF (PDF/A for final records), root ≤ 40 and paths below root ≤ 140 characters (AC §AC.13.7). *Acceptance:* export of a seeded provider with 50 engagements validates against the manifest schema; free at exit; delivered within 7 days.

**FR-P19-68 — Audit and evidence.** Hash-chained audit on all `mkp`, `dir` and `rev` writes; un-disableable edit log on payout, payee, tax, rate-card and price tables; evidence catalogue entries for transparency reports, dark-pattern audits, sponsorship monthly audits, propagation SLA reports and kill-switch drills (Appendix AE). *Acceptance:* internal-audit sample export produced for one quarter.

**FR-P19-69 — Service-provider tools plan (RS-57, built OFF).** Optional monthly plan for `mkp.providers.kind = 'service_provider'` (calendar sync, team seats, own-data analytics) sold through the P05 plan engine with `stream_code = 'RS-57'`, behind `mkp.provider_subscriptions` (OFF) and `assertLive('RS-57')`; cancellation takes no more steps than sign-up; never offered to advocates, CAs, CSs or CMAs; plan status has no read path to ranking, sponsor eligibility, reviews, badges or take (Appendix AB AB-R11). *Acceptance:* with the flag OFF the plan page and checkout return `REV_STREAM_NOT_LIVE`; with the flag forced ON in test, `RANKING_IGNORES_PAID` stays green when plan status is toggled.

---

## 5. Workflows and state machines

### 5.1 Provider lifecycle (`mkp.providers.status`; Appendix AA §AA.4.2)

| From | Event | Guard | To | Effects |
|---|---|---|---|---|
| `draft` | submit | required fields; declarations; consents | `submitted` | reference issued; SLA 2 WD |
| `submitted` | start KYC | — | `kyc_pending` | KYC tasks |
| `kyc_pending` | KYC complete | PAN/KYB/penny-drop pass; sanctions clear | `verifying` | verification tasks (two-person) |
| `kyc_pending`/`verifying` | request info | reason | `info_requested` | 14-day clock; reminder day 7 |
| `info_requested` | no reply 14 days | — | `paused` | notice |
| `verifying` | all credentials verified | `verifier_1 ≠ verifier_2`; status check evidenced | `agreement_pending` | e-sign envelopes |
| `agreement_pending` | all signed | MPT, MPC (+ ECC) | `payout_setup` | payee + tax tasks |
| `payout_setup` | payee approved, tax complete | cooling-off may continue (payout hold only) | `profile_draft` | builder unlocked |
| `profile_draft` | submit profile | allow-list lint | `profile_review` | moderation SLA 3 WD |
| `profile_review` | approve | lint clean; seller details complete; Chambers workspace active (neutrals) | `listed` | index; `equator.mkp.listing.published.v1` |
| `listed` | interim S1 / E4 | reasons | `suspended` | enquiries stop; open engagements reviewed |
| `suspended` | decision lifted | — | `listed` | — |
| `suspended` | E5 | reasons; appeal window | `delisted` | run-off |
| `listed` | provider withdraws | — | `withdrawn` | run-off; export offered |
| `withdrawn`/`delisted` | run-off and appeal window end | — | `closed` | erasure scheduled +30 days |
| any pre-listing | reject / archive | reasons / 90-day draft | `rejected` / `archived` | re-apply after 6 months |

### 5.2 Engagement (`mkp.engagements.status`; AA.6.7) — Temporal `MarketplaceEngagementWorkflow`

```
enquiry_open ─(provider proposes after conflict check)→ proposal_sent
proposal_sent ─(neutral service)→ counterparty_invited ─(all parties accept ≤ 10 d)→ counterparty_accepted
proposal_sent | counterparty_accepted ─(explicit confirmation + payment hold)→ confirmed ─→ in_delivery
in_delivery ─→ milestone_due ─(buyer confirms ≤ 5 WD or deemed release)→ milestone_released ─…→ completed
milestone_due ─(dispute)→ milestone_disputed ─(fee reviewer decision)→ milestone_released | refunded
completed ─→ review_window (30 d) ─→ closed
exits: enquiry_expired (7 d) | proposal_declined | proposal_expired (7 d) | cancelled_by_buyer | cancelled_by_provider | refunded
```

Signals: `ProviderProposed`, `PartyAccepted`, `PartyDeclined`, `Confirmed`, `MilestoneConfirmed`, `MilestoneDisputed`, `FeeReviewerDecided`, `Cancelled`. Timers per §9. Every transition audited; payment holds released or refunded by activity with idempotency keys.

### 5.3 Payout batch (`mkp.payout_batches`)

`prepared (system) → pending_approval → approved (accounts_checker; second approver if > limit) → released (PAYOUT_PORT) → reconciled (accounts_maker ≠ approver)`; exits `rejected` (reasons; lines return to pool) and `partially_failed` (failed transfers re-queued after payee check). SoD enforced by Cerbos and DB CHECKs (AA.17).

### 5.4 Sponsorship order (`mkp.sponsorship_orders.status`)

`requested → (eligibility_failed | creative_review) → approved (ad_reviewer maker, compliance_officer checker) → active (1st of month; RS-19 live; flag ON) → ended | refunded | cancelled`. Kill switch or flag OFF forces `active → ended` with pro-rata refund (unless ended for S1 misconduct). Monthly `SponsorshipAuditJob` produces the operations audit and rotation-fairness report.

### 5.5 Registry record (`dir.professional_records.status`) and propagation

```
pending ─(two-person verification)→ active ─(12 m no reconfirm)→ active [stale label] ─(18 m)→ active [hidden]
active ─(CoP lapse)→ lapsed ─(re-verified)→ active
active ─(Council suspension recorded)→ suspended_by_council ─(lifted)→ active
any ─(withdraw all consents)→ withdrawn ─(erasure request)→ erased
```

Temporal `RegistryPropagationWorkflow` per event: fan-out to consumers in `dir.distribution_log` → await ACK signal per consumer → reminder at 24 h → incident at 72 h → close when all ACKed; nightly `RegistryReconciliationJob`.

### 5.6 Revenue stream

Appendix AB §AB.2.3 (draft → in review → approved → live ↔ paused → retired; forced pause by kill switch). Temporal `StreamKillWorkflow` and `ViabilityReviewWorkflow` (AB §AB.7.2).

### 5.7 Complaint and enforcement

`received → acknowledged (≤ 48 h) → triaged (S1/S2/S3) → [interim_suspension] → investigating → provider_response (15 d) → decided (≤ 30 d; reasons) → [appealed → appeal_decided (≤ 30 d)] → closed`; redress clock one month from receipt; complaint copy sent at acknowledgement.

---

## 6. Screens and UX (web + mobile)

| ID | Route / location | Users | Purpose | Mobile |
|---|---|---|---|---|
| SCR-P19-01 | `/marketplace` | Public | Search with filters, organic results, separate sponsored block (when ON), compare tray | Yes (filters in bottom sheet) |
| SCR-P19-02 | `/marketplace/{category}/{slug}` | Public | Profile: badges with popovers, offerings and fees incl. GST, availability, reviews (n ≥ 10), seller details, disclosures, complaint link | Yes |
| SCR-P19-03 | `/marketplace/how-ranking-works` | Public | Ranking parameters in descending order; sponsored rules; changelog | Yes |
| SCR-P19-04 | `/marketplace/transparency` | Public | Quarterly reports | Yes |
| SCR-P19-05 | `/marketplace/compare` | Public | Up to 3 profiles side by side (no sponsored marker beyond the label) | Yes |
| SCR-P19-06 | `/app/marketplace/enquiries/{id}` | Buyer, provider | Enquiry thread; conflict-check status; proposal card | Yes |
| SCR-P19-07 | `/app/marketplace/engagements/{id}/proposal` | Buyer, counterparty | Fee disclosure, terms, disclosures, unticked confirmation, "Confirm and pay" | Yes |
| SCR-P19-08 | `/app/marketplace/engagements/{id}` | Parties, provider | Milestones, deliveries, documents shared, dispute button, review invitation | Yes |
| SCR-P19-09 | `/app/marketplace/complaints/new` | Anyone | Complaint form with categories and copy-of-complaint receipt | Yes |
| SCR-P19-10 | `/provider/apply` | Applicant | Category choice, declarations, KYC/KYB, consents, status tracker (Appendix N §2.4 pattern) | Yes |
| SCR-P19-11 | `/provider/profile` | Provider | Profile form or Appendix W builder; allow-list hints; preview; freshness banner | Partial (edit text and availability) |
| SCR-P19-12 | `/provider/offerings` | Provider | Service offerings, fee models, refund rules | Yes |
| SCR-P19-13 | `/provider/calendar` | Provider, staff | Availability and holds | Yes |
| SCR-P19-14 | `/provider/payouts` | Provider owner | Payee (cooling-off state), tax profile, statements with take, GST, TCS, TDS | Yes |
| SCR-P19-15 | `/provider/reviews` | Provider | Reviews, replies, re-moderation request | Yes |
| SCR-P19-16 | `/provider/sponsorship` | Eligible provider | Eligibility check result, rate card, order, invoices (hidden while flag OFF) | Yes |
| SCR-P19-17 | `/provider/enforcement` | Provider | Notices, reply, appeal | Yes |
| SCR-P19-18 | `/provider/export` | Provider | Export package request and download | Yes |
| SCR-P19-20 | Ops: Marketplace operations queue | `marketplace_moderator`, `marketplace_manager` | Applications, moderation, complaints flags, ranking publication status (Appendix X marketplace workspace) | No |
| SCR-P19-21 | Ops: Verification workbench | `provider_verifier` | Two-person evidence capture and confirmation | No |
| SCR-P19-22 | Ops: Category and rule-pack admin | `marketplace_manager`, `legal_reviewer` | Category law checks, activation | No |
| SCR-P19-23 | Ops: Ranking policy editor | `marketplace_manager`, `compliance_officer` | Versions, preview with golden vectors, publish with notice | No |
| SCR-P19-24 | Ops: Enforcement and panels | Panel members | Cases, reasons editor, decisions, appeals | No |
| SCR-P19-25 | Ops: Sponsorship and ads | `ad_reviewer`, `compliance_officer` | Orders, creatives, rotation fairness, monthly audit, ad campaigns, advertiser policy list | No |
| SCR-P19-26 | Ops: Payout batches | `finance_ops`, `accounts_checker`, `finance_controller` | Batch review, approvals, reconciliation | No |
| SCR-P19-27 | Ops: Tax engine | `finance_ops`, CFO | TCS ledger, GSTR-8 data, withholding ledger, certificates | No |
| SCR-P19-28 | Ops: Transparency and dark-pattern audit | `compliance_officer`, `internal_auditor` | Report generation, audit workflow, certificate | No |
| SCR-P19-29 | Ops: Marketplace grievance desk | `grievance_officer` | Clocks, NCH status, takedowns (Appendix X desk) | No |
| SCR-P19-30 | Case app: Post-Resolution Professional Chooser | Party | Legal aid first; own professional; Equator panel (if ON); in person; banner; consent | Yes |
| SCR-P19-31 | Case app: Share with my professional | Party | Item-level authorisation; active shares; revoke | Yes |
| SCR-P19-32 | Enterprise console: Procurement | `enterprise_admin` | Vendor panels, bulk requests, RFQs, SLAs, reports | Partial (approvals) |
| SCR-P19-33 | Enterprise/Chambers console: Professional Panel Register | `panel_register_*` | Registers, invitations, memberships, RFQs, engagements, SLA reports, private notes | Partial |
| SCR-P19-34 | `/registry/me` | Professional | Record, fields with provenance, consents per purpose, distribution log, invitations, DSRs | Yes |
| SCR-P19-35 | Registry admin console | `registry_steward`, `registry_verifier` | Verification queue, freshness, consumers, GDSA gates, propagation dashboard, reconciliation | No |
| SCR-P19-36 | `/trust/dark-patterns` | Public | Latest certificate and summary | Yes |
| SCR-P19-37 | `/marketplace/advertise` | Public | Rate card and rules for sponsored listings (hidden while OFF); advertising policy | Yes |
| SCR-P19-AB01…AB10 | Ops: Revenue Stream Registry console | AB roles | Per Appendix AB §AB.15 FR-P19-V3-AB02 | No |

**UX rules.** One primary action per screen; totals including GST before payment (NN-29); no countdowns, scarcity badges or nagging; every sponsored card labelled; cancellation of a sponsorship or provider plan takes no more steps than ordering; English and Hindi at launch, other languages by configuration (NN-23); WCAG 2.2 AA; mobile uses bottom sheets for filters and sticky "Confirm and pay" only after the disclosure is scrolled into view (no forced scrolling — the checkbox is the consent).

**Copy deck (selected, en).**
- Search header: "Book a private mediator, arbitrator or ADR service. These are private engagements: Equator does not appoint the provider or administer the matter."
- Sponsored block label: "Sponsored — paid placement. Does not affect Equator appointments."
- Profile institutional statement: "Bookings on the Equator Marketplace are private engagements. Equator does not administer them, appoint the provider or guarantee any result."
- Fee disclosure heading: "What you will pay — total {amount} including GST."
- Chooser banner: "You choose who helps you. Equator does not recommend, refer or pay any advocate and receives nothing from them. Free legal aid may be available to you."
- Registry consent (Finbyx): "Make my professional profile available to lender clients of Finbyx for engaging me in execution, registration and recovery matters. You can turn this off at any time."

---

## 7. Backend design

### 7.1 Modules touched

New: `mkp` (Nest module in `apps/api`), `registry` (standalone `services/registry` exposing the `dir` API), `rev` (Nest module per Appendix AB), `procurement` (pure package `packages/procurement`), rules packages `packages/rules/mkp-ranking`, `packages/rules/mkp-sponsor`, `packages/rules/mkp-tax`. Extended: `neutrals` (conflict edges, disclosure item), `billing` and `payments` (take, TCS, TDS, holds, payouts), `chambers` (matter creation from bookings), `execution` (chooser, acting professional), `cms` (ads slot, trust pages), `enterprise` (procurement, panel register UI), `consent` (registry purposes mirror for Equator consumer), `integrations` (`REGISTRY_PORT`, NCH connector), `audit`, `reporting`.

### 7.2 Tables

Canonical DDL: Appendix AA §AA.17 (`mkp.*`, `dir.*`) and Appendix AB §AB.9 (`rev.*`). Additive changes elsewhere:

| Table | Change |
|---|---|
| `core.cases` | `source` enum + `private_marketplace`, `panel_direct_request` (alias `marketplace` retained, X-59) |
| `core.conflict_edges` | edge types + `counsel_panel_of`, `privately_engaged_by`; columns `source_system` (`dir`/`mkp`), `source_ref` |
| `core.neutral_disclosures` | item kind + `paid_visibility_24m` (non-deletable when pre-filled) |
| `core.party_representatives` | scope key `court_steps_support` (Appendix S §4.3 catalogue) |
| `core.disclosures` | purposes reused: `ENFORCEMENT`, `REGISTRATION`, `PARTY_COUNSEL`, `TRANSLATOR`, `INTERPRETER` |
| `core.registration_tasks`, `core.execution_proceedings` | + `acting_professional_ref`, `acting_professional_source` |
| `core.advocate_listings` | Converted to read-only view over `dir` projection (X-60) |
| `core.invoice_lines` (P05 canonical) | + `stream_code` REFERENCES `rev.streams(code)`, NOT NULL for new lines (Appendix AB §AB.4.6) |
| `cfg.setting_definitions` | Rows for AA.15 and AB §AB.8 keys |

RLS: `mkp` tables by `tenant_id` where tenant-scoped (procurement, vendor panels) and by `provider_id` ownership; public projections served from `mkp.listings` published versions only; `dir` by `consumer_entity_id` + `tenant_ref`; `dir.tenant_notes` additionally by `register_id` membership.

### 7.3 APIs

Appendix AA §AA.18 (marketplace and registry) and Appendix AB §AB.10 (revenue registry) are canonical. Additional internal endpoints:

| Method and path | Purpose | Caller |
|---|---|---|
| POST `/v1/internal/mkp/engagements/{id}/matter` | Create matter in provider's Chambers tenant | `MarketplaceEngagementWorkflow` |
| POST `/v1/internal/conflicts/edges:upsert` | Conflict edge from F2/F3 | registry consumer adapter; mkp |
| GET `/v1/internal/neutrals/{id}/paid-visibility` | Boolean + period for disclosure (F4) | `neutrals` disclosure module only |
| POST `/v1/internal/mkp/tax/gstr8-export?period=` · POST `/v1/internal/mkp/tax/tds-export?quarter=` | Regulatory data | finance jobs |
| POST `/v1/internal/registry/consumers/{id}/ack-batch` | Batched ACKs | consumer adapters |

All public and partner endpoints: cursor pagination, allow-listed filters, Idempotency-Key on creating POSTs, RFC 9457 errors with AA §AA.20 and AB §AB.12 codes, rate limits per tenant, per API key and per consumer.

### 7.4 Events

Appendix AA §AA.19 (`equator.mkp.*`, `equator.dir.*`) and Appendix AB §AB.11 (`equator.rev.*`). Consumers: `neutrals` consumes `equator.dir.panel_membership.created|ended.v1` and `equator.mkp.engagement.completed.v1` (edges only); `reporting` consumes aggregates; EOP consumes `equator.mkp.provider.status_changed.v1`, `equator.mkp.complaint.received.v1`, `equator.rev.stream.*` for read models. No event payload carries PII, case facts or tenant notes.

### 7.5 Temporal workflows and jobs

| Workflow / job | Trigger | Notes |
|---|---|---|
| `ProviderOnboardingWorkflow` | Application submitted | KYC → two-person verification → agreements → payout setup → profile review; SLAs and reminders |
| `CredentialReverificationWorkflow` (mkp) | T-30 before expiry; annual | Tasks; hide on expiry |
| `MarketplaceEngagementWorkflow` | Enquiry created | §5.2; payment holds; matter creation; review invitation |
| `FeeDisputeWorkflow` | Milestone disputed | 7-day direct window → reviewer assignment (conflict-checked) → decision → release/refund |
| `PayoutBatchJob` | Nightly | Prepare batch; approval tasks; release; reconciliation task |
| `TcsMonthlyJob`, `TdsQuarterlyJob` | Monthly / quarterly | Ledgers, exports, certificates (flags gate) |
| `ReviewInvitationJob`, `ReviewAggregationJob` | 48 h after completion; nightly | n ≥ 10 rule |
| `ComplaintClockWorkflow` | Complaint received | 48 h / 1 month / 7 days / 3 h clocks; incidents on breach |
| `TakedownWorkflow` | Takedown received | Category clocks |
| `SponsoredRotationService` | Per request | Session-seeded round-robin; stateless with daily aggregates |
| `SponsorshipAuditJob` | Monthly | Label, cap, interleave and rotation checks; report to `compliance_officer` |
| `DarkPatternSelfAuditWorkflow` | Annual (and on demand) | Automated results + manual walkthrough + signatures + certificate |
| `TransparencyReportJob` | Quarterly | Query pack, dataset hash, approvals |
| `FreshnessJob` (mkp and dir) | Daily | Labels at 12 months; hide at 18 |
| `RegistryPropagationWorkflow` | `dir.record.*` events | Fan-out, ACK, reminder, incident |
| `RegistryReconciliationJob` | Nightly | Projection hash comparison per consumer |
| `DsrWorkflow` (registry) | DSR request | Appendix Q clocks across Owner and consumers |
| `ProcurementBulkIntakeWorkflow` | Upload | Validation report; per-row errors |
| `RfqWorkflow` (mkp and dir) | RFQ issued | Response window; comparison; award |
| `StreamKillWorkflow`, `ViabilityReviewWorkflow`, `PriceChangeWorkflow` | AB events and schedules | Appendix AB |

---

## 8. Integrations (ports and adapters)

| Port | Use in P19 | Fallback (NN-40) |
|---|---|---|
| `PAYMENTS_PORT` (Razorpay Route primary) | Booking payments, transfer holds, split settlement to provider linked accounts | Manual-capture window pattern (P03 FR-P03-31) and second PA adapter; bookings pause, never auto-switch money rails without finance approval |
| `PAYOUT_PORT` | Provider payouts | Second payout provider; manual bank file with maker-checker |
| `TAX_INVOICE_PORT` | GST invoices for take, sponsorship, ads; GSTR-8 data | CSV/JSON export for the tax filer |
| `KYC_PORT` | PAN, GSTIN, MCA21, penny-drop, DigiLocker/OVSE; `lookupBarRoll.{state}` stays OFF | Manual two-person verification with evidence |
| `ESIGN_PORT` | MPT, MPC, ECC, PRP, panel terms, GDSA signatures | Alternate eSign provider |
| `REGISTRY_PORT` (new) | Equator as a registry consumer: search within purpose, get record, ACK events, invitations | Read from local projection (≤ 24 h) for display; new engagements blocked if the registry is unavailable > 1 h |
| `CONNECTOR_PORT` — NCH | National Consumer Helpline convergence (`mkp.nch_integration.enabled` OFF) | Manual NCH reference entry |
| `CRM_PORT` / EOP | Provider and advertiser accounts as EOP records; marketplace operations workspace | — |
| `VIDEO_PORT` | Interpreter channel and hearing rooms for bookings (via Chambers tenant) | Per P04 |
| `MESSAGING_PORT`, `EMAIL_PORT` | Notices: enquiry, proposal, confirmations, reviews, complaints, propagation alerts; DLT templates `MKP_*`, `DIR_*` | Channel fallback per P07 |
| `ANALYTICS_PORT` | Aggregate, first-party only on marketplace pages; no ad pixels | — |
| OpenSearch | `mkp-listings-{env}` index; `dir` search inside the registry cluster only | Postgres full-text fallback with the same ranking package |

**Consumer adapters for Finbyx, Udofin and LawDocs.** P19 ships a reference TypeScript client (`packages/registry-client`) with OAuth2 client credentials, `Equator-Purpose` header, ACK handling, projection cache with TTL ≤ 24 h, and a contract-test suite that each consumer must pass before its `dir.consumers.status` becomes `active`. Field mapping, system-of-record declaration (registry is the system of record for professional records; each consumer for its engagements) and a migration rehearsal follow NN-40 and Appendix AC.

---

## 9. Configuration surface

All keys are registered in `cfg.setting_definitions` (Appendix V) and shown in the settings UI with tier badge, who may change them and whether approval is needed (NN-33). The full catalogue is Appendix AA §AA.15 and Appendix AB §AB.8; the keys P19 code reads most are:

| Key | Tier | Default | Approver / bounds |
|---|---|---|---|
| `marketplace.paid_placement` | G | OFF | Board resolution + counsel sign-off + D2-14 amendment entry (D3-01) |
| `marketplace.paid_placement.advocates` | L | OFF | Not switchable |
| `marketplace.paid_placement.max_slots_per_page` | G | 2 | ≤ 2; ≤ 20% of results (L) |
| `marketplace.advocate_neutrals.listing` | G | OFF | Counsel opinion OI-03 |
| `marketplace.institute_neutral.ca` / `.cs` / `.cma` | G | OFF | Institute opinion |
| `marketplace.related_party_sponsorship` | G | OFF | Board + counsel |
| `marketplace.take_rate.<plan>` / `.service_providers` | G | 15/15/12/10% / 10% | Board |
| `marketplace.advocate_neutral.flat_fee_minor` | G | Board | Board + counsel |
| `marketplace.client_processing_fee` | G | OFF | Board + counsel |
| `platform.mkp.collection_model` | G | `provider_merchant_of_record` | CFO + `legal_reviewer` |
| `tax_memo.mkp_eco_recorded` | G | false | CFO with memo document |
| `billing.eco_gst_tcs` / `billing.eco_withholding` | G | OFF | Tax memo (LR-TAX-008 / LR-TAX-007) |
| `platform.tax.gst_tcs_rate` / `.eco_tds_rate` / `.eco_tds_individual_threshold_minor` | G | 0.5% / 0.1% / ₹5,00,000 | Citation required |
| `platform.mkp.hold_days` | G | 14 | 7–21 |
| `platform.mkp.payee_cooling_off_hours` | G | 72 | ≥ 48 |
| `platform.mkp.payout_sla_days` | T | 3 | 2–7 |
| `platform.mkp.new_provider_payout_hold_count` | T | 3 | 1–5 |
| `platform.mkp.ranking_policy_version` | G | `MKP-RANK-2026.1` | 30-day notice |
| `platform.mkp.freshness.label_months` / `.hide_months` | G | 12 / 18 | ≤ 12 / ≤ 18 |
| `platform.mkp.enquiry_response_wd` / `.proposal_validity_days` | T | 2 / 7 | 1–5 / 3–14 |
| `platform.mkp.review.min_n_public` | L | 10 | master X-28 |
| `platform.mkp.category.<code>.enabled` | G | AA.3.1 | Law check signed |
| `mkp.assistant.enabled` | T | OFF | Tenant/platform admin; eval gate passed |
| `mkp.nch_integration.enabled` | G | OFF | Counsel confirms NCH specification |
| `mkp.provider_subscriptions` | G | OFF | Board prices; stream RS-57 live (Appendix AB AB-R11) |
| `platform.rev.ads.enabled` | G | OFF | Board + counsel on advertiser policy |
| `directory.public_professionals` | G | OFF | Counsel opinion and SLP (C) 25794/2024 decided |
| `register.ca` / `register.cs` / `register.cma` | G | OFF | Institute position confirmed |
| `postres.advocate_panel` | G | OFF | Counsel opinion on PRP-2026.1 |
| `group.dir.owner_entity_id` | G | unset | Board resolution |
| `group.dir.propagation_sla_hours` | G | 72 | ≤ 72 |
| `group.dir.consumer.<entity>.purposes[]` | G | none | GDSA schedule; Owner DPO checker |
| `tenant.dir.panel.terms_version` / `.display_order` | T | template / alphabetical | Lint blocks fee-share terms |
| `tenant.mkp.vendor_panel.distribution` | T | `round_robin` | — |
| `platform.rev.price_tests.enabled` | G | OFF | Board policy + counsel (AB §AB.2.7) |

Configured fallbacks (NN-33): if a G value is unapproved or expired, the system uses the last approved version; if none exists, the dependent feature stays OFF (never a permissive default).

---

## 10. Security, privacy and audit

1. **Isolation.** Separate DB roles per surface; `grp-registry` in a separate AWS account and cluster with its own KMS keys; Equator has no direct DB access to it (AA.2.3). CI tests `NO_PAID_PLACEMENT`, `MKP_SURFACE_ISOLATION`, `GROUP_SHARE_SCOPE`, `R36_PROFILE_ALLOW_LIST`, `NO_ROLL_SCRAPING`, `ADVOCATE_TARIFF_LINT` are release blockers.
2. **Identity and step-up.** Staff via `eq-portal-ops` with phishing-resistant MFA (X-24); providers and professionals with passkey/TOTP; step-up (`aal2-pr`) for payee changes, payout approvals, sponsorship approvals, enforcement decisions, flag changes, consumer purpose grants and kill-switch use.
3. **Separation of duties (NN-36).** Payee creator ≠ approver; payout batch approver ≠ releaser ≠ reconciler; ranking, rate-card, category and flag changes maker ≠ checker; two-person verification for credentials and registry records; enforcement panel composition validator.
4. **Privacy (NN-15, NN-30, NN-39).** DPDP notices at provider application and registry registration; consent per purpose with recipients named; no reliance on DPDP s.3(c)(ii); minimisation (allow-lists); field-level encryption for enquiry payloads, messages, tenant notes and bank references; masked display (PAN, phone); retention per Appendix Q; DSR workflows across Owner and consumers; erasure propagation ≤ 72 h; distribution log visible to the professional.
5. **Neutrality firewall (NN-16, NN-34).** No marketing use of marketplace enquiries without separate marketing consent; no ad pixels or audiences on marketplace pages; case data never in `mkp` or `dir`; sponsorship invisible to case roles; F4 boolean only to disclosures.
6. **Payments (NN-13, NN-31).** Hosted checkout only; no card data; holds at the PA; settlement sums never on the marketplace.
7. **Content and intermediary duties.** Content policy, takedown clocks, grievance officer, complaint copies, logs retained for the periods the IT Rules require **[VERIFY — open: log retention period under the 2026 amendment]**.
8. **Audit.** Hash-chained audit events for every write; un-disableable edit log on payouts, payees, tax lines, rate cards and prices; evidence catalogue (Appendix AE) for transparency reports, dark-pattern audits, sponsorship audits, propagation SLA reports, kill-switch drills and verification samples.
9. **Abuse and fraud.** Rate limits on search, enquiries and registry API; CAPTCHA on public complaint and takedown forms; fraud detectors (FR-P19-35); WAF rules for scraping patterns on `/marketplace` and blocking bulk enumeration of profiles; `robots.txt` allows search crawlers and blocks AI-training crawlers on profiles (master X-42).
10. **Security testing.** Threat model update for the marketplace and registry; DAST on public pages and APIs; authorisation test matrix generated from Cerbos policies (every role × resource × action in AA.16); penetration test scope includes the registry consumer API and payout flows (Appendix AE VAPT cycle).

---

## 11. AI touchpoints and guardrails

| Touchpoint | Allowed | Never (NN-01, NN-25) | Controls |
|---|---|---|---|
| Profile copy assistant (provider) | Suggest plain-language bio edits within the allow-list; translate with "Translation — for convenience" label (NN-32) | Invent credentials, outcome claims, "top/best" labels | Output passes `MKP_LABEL_FORBIDDEN` lint; provider approves every change |
| Document extraction for verification | Extract certificate numbers and dates for the verifier | Decide verification | Two-person human verification always |
| Moderation triage | Classify reviews and content for PII, abuse, misconduct allegations | Remove or publish on its own | Moderator decides; reason codes logged |
| Complaint triage | Suggest category and severity | Decide severity S1 or sanctions | Grievance officer and panels decide |
| Marketplace assistant (OFF) | Explain filters, categories, fee models, processes | Rank, recommend or name providers; use sponsorship, plan or fees paid; legal advice | Eval gate `mkp-assistant-neutrality`; logs; kill switch per feature (AI Gateway) |
| Registry | Extract fields from a professional's own uploaded certificate | Scrape or enrich from third-party sites | Source recorded as `self_entered` until verified |
| Revenue analytics narrative | Summarise KPI movements for the viability review | Propose prices automatically | Human review; private data stays in role scope |

No AI principal may approve, publish, sponsor, rank, moderate, enforce, verify, pay or change settings (Cerbos `DENY` for `machine` with `ai_agent` subject). LLM calls run via the AI Gateway in-country (Bedrock India), with no case content in marketplace prompts.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p19/`)

```gherkin
Feature: P19 Marketplace, Professional Registry and Revenue Stream Registry

  Scenario: Allocation cannot read marketplace or revenue tables
    Given the allocation service database role
    When the schema analyser lists its grants
    Then it has no grant on any table in schemas mkp, rev or dir
    And the allocation service refuses to start if such a grant is added

  Scenario: Organic order ignores paid and commercial attributes
    Given golden vector GV-MKP-03 with seed "s-42" and 30 mediators in Rajasthan
    When sponsorship, Chambers plan, related-party status and review counts are toggled for 10 of them
    Then the organic order is identical in every run

  Scenario: Sponsored listings stay off until approved
    Given marketplace.paid_placement is OFF
    When an eligible mediator orders a sponsored listing
    Then the response is 409 with code "MKP_PAID_PLACEMENT_OFF"
    And GET /v1/public/marketplace/sponsored returns an empty block

  Scenario: Sponsored block is labelled, separate, capped and rotated
    Given marketplace.paid_placement is ON in the test environment and RS-19 is live
    And 5 eligible sponsors exist for "Mediation" in "Rajasthan"
    When 10,000 searches for mediation in Rajasthan are simulated
    Then each page shows at most 2 sponsored cards above organic results and none inside them
    And every card shows "Sponsored — paid placement. Does not affect Equator appointments."
    And each sponsor's impression share is within 5% of equal

  Scenario: No sponsorship in case context
    Given a party has an open Equator-administered matter
    When that party opens /marketplace
    Then no sponsored block is rendered

  Scenario: Advocates are never sponsored or reviewed
    Given provider P is an enrolled advocate listed as an advocate-neutral in the test environment
    When P orders a sponsored listing
    Then the response is 422 with code "MKP_SPONSOR_INELIGIBLE"
    And completing an engagement with P creates no review invitation

  Scenario: Advocate cannot list as a service provider
    When an applicant who declares "advocate" applies in category "SVC-EXP"
    Then the response is 422 with code "MKP_PROFESSIONAL_NOT_ALLOWED"

  Scenario: One-party arbitration booking blocked
    Given a lender organisation flagged repeat player initiates an arbitrator booking against an individual borrower
    Then the response is 422 with code "MKP_REPEAT_PLAYER_ARBITRATION_BLOCKED"

  Scenario: Lender's panel advocate blocked as mediator in the lender's dispute
    Given advocate-mediator M is a member of lender L's recovery panel in the registry
    When a buyer requests M for a mediation in which L is a party
    Then the conflict check returns "hard" with reason "counsel_panel_of"
    And the proposal cannot be sent

  Scenario: Fee disclosure and explicit confirmation
    Given a proposal with a provider fee of ₹10,000 and GST of ₹1,800
    When the buyer opens the proposal
    Then the total "₹11,800.00 including GST" is shown before payment
    And the confirmation checkbox is unticked
    And confirming without accepting the disclosure returns 409 "MKP_FEE_DISCLOSURE_REQUIRED"

  Scenario: Hold refunded when the counterparty declines
    Given the claimant paid for a mediator booking and the payment is on hold
    When the respondent declines within 10 days
    Then the hold is refunded in full to the original instrument
    And no matter is created

  Scenario: Paid bookings blocked without the tax memo
    Given tax_memo.mkp_eco_recorded is false
    When a buyer tries to confirm a paid booking
    Then the response is 409 with code "MKP_TAX_MEMO_MISSING"

  Scenario: No TCS on reverse-charge arbitral tribunal fees
    Given billing.eco_gst_tcs is ON and Equator is recorded as an e-commerce operator
    And a company books a sole arbitrator whose fee is taxed under reverse charge
    When the milestone is released
    Then no TCS line is created for that fee
    And the GST TCS ledger excludes it

  Scenario: Payout separation of duties
    Given accounts_checker A approved payout batch B
    When A tries to reconcile batch B
    Then the response is 403 with code "MKP_PAYOUT_SOD_VIOLATION"

  Scenario: New bank account waits out the cooling-off
    Given a provider changed bank details 10 hours ago
    When a payout batch includes that provider
    Then the line is held with code "MKP_PAYEE_COOLING_OFF" until 72 hours have passed and out-of-band confirmation is recorded

  Scenario: Public review score appears only at ten
    Given a translator has 9 published reviews
    Then no aggregate score is shown on the profile
    When the 10th review is published
    Then the aggregate and per-item bars are shown with the date range

  Scenario: S1 complaint suspends new enquiries
    When a complaint alleging a false credential is triaged as S1
    Then the provider stops receiving new enquiries within 5 minutes
    And open engagements are listed for review
    And the complainant has received a copy of the complaint as recorded

  Scenario: Lender cannot empanel mediators
    When an enterprise_admin creates a vendor panel in category "NEU-MED"
    Then the response is 403 with code "MKP_ENTERPRISE_NEUTRAL_PROCUREMENT_BLOCKED"

  Scenario: Party chooses the professional
    Given an individual award holder opens the post-resolution chooser
    Then "Free legal aid" is the first option
    And no option shows a rating, fee or "recommended" label
    When the party chooses "I have my own advocate" and invites advocate X
    Then mkp.postres_choices records the choice, the options shown and the order seed
    And X sees only the items the party authorises

  Scenario: Registry does not accept bulk roll imports
    When a tenant uploads 500 enrolment numbers to create registry records
    Then no registry record is created
    And 500 invitations are queued for the professionals to accept
    And a direct bulk create returns 422 "DIR_BULK_IMPORT_FORBIDDEN"

  Scenario: Purpose-bound consumer access
    Given advocate A consented to "equator_engagement" but not to "group_share_finbyx"
    When the Finbyx consumer searches the registry with Equator-Purpose "group_share_finbyx"
    Then A is not returned
    And a direct GET of A's record returns 403 "DIR_PURPOSE_NOT_GRANTED"

  Scenario: Registry erasure propagates within the SLA
    Given A's record version 7 was distributed to Equator and Udofin consumers
    When A requests erasure
    Then equator.dir.record.erased.v1 is delivered to both consumers
    And when Udofin has not acknowledged within 72 hours an incident "DIR_PROPAGATION_OVERDUE" is raised to both DPOs
    And A's distribution log shows both deliveries and the acknowledgement status

  Scenario: Tenant notes stay in the tenant
    Given lender L wrote a private note on advocate A in its panel register
    When lender M or the registry owner queries A
    Then the note is not returned to either
    And a direct request returns 403 "DIR_TENANT_SCOPE"

  Scenario: Kill switch stops new sales within a minute
    Given RS-18 is live
    When the CFO engages the kill switch for RS-18 in scope IN
    Then new marketplace booking confirmations return "REV_STREAM_NOT_LIVE" within 60 seconds at p95
    And engagements already confirmed continue to completion

  Scenario: Dark-pattern self-audit gates sponsorship
    Given the last dark-pattern self-audit certificate is older than 12 months
    When a revenue_manager proposes RS-19 go-live
    Then the transition is refused and "MKP_DARK_PATTERN_AUDIT_OVERDUE" is shown
```

Plus all Appendix AA §AA.22 and Appendix AB §AB.14 scenarios.

---

## 13. Deliverables and exit gate

**Deliverables (checklist)**
- [ ] Migrations for `mkp`, `rev` (AB §AB.9) and the `grp-registry` cluster `dir` schema; additive changes in §7.2; RLS policies; grants proving isolation.
- [ ] Rule packages `mkp-ranking`, `mkp-sponsor`, `mkp-tax`; `packages/procurement`; `packages/registry-client`.
- [ ] Public marketplace pages (SSR) and trust pages; provider portal; buyer flows; mobile screens marked in §6.
- [ ] Operations Platform workspaces SCR-P19-20…29 and SCR-P19-AB01…AB10.
- [ ] Registry service with admin console and `/registry/me`; consumer onboarding with GDSA gate; reference adapters and contract tests for Finbyx, Udofin and LawDocs.
- [ ] Tenant Professional Panel Register module; enterprise procurement module.
- [ ] Post-Resolution Professional Chooser and authorised sharing (P06 integration).
- [ ] Tax engines (TCS, withholding) behind flags; payout batches with SoD; RP-MKP refunds.
- [ ] Sponsored listings and display ads built, tested and OFF; dark-pattern self-audit workflow; monthly sponsorship audit job.
- [ ] Revenue Stream Registry (FR-P19-57…64) with kill-switch drill evidence.
- [ ] Policy documents AA-1…AA-11 registered as drafts with owners and approvers.
- [ ] Settings registered in `cfg` with tiers, fallbacks and approvers; flags OFF with approvers named.
- [ ] Seed and demo data: 40 providers across all ON categories (incl. 3 Chambers, 6 translators, 4 interpreters incl. ISL, 3 process agents, 3 valuers), 120 engagements across states, 60 reviews, 6 complaints (S1–S3), 2 enforcement decisions with an appeal, 1 lender panel register with 25 advocates and 2 RFQs, 1 Finbyx consumer and 1 Udofin consumer in sandbox, 57 streams in the registry; `P19-demo.md` click-path: search → profile → enquiry → conflict check → proposal → joint confirmation → payment hold → matter in Chambers tenant → milestone → payout batch → review → complaint → enforcement → export; registry: self-registration → consent → two-person verification → lender invitation → RFQ → erasure → propagation report.
- [ ] Phase addenda delivered: FR-P03-V3-AA01…AA04, FR-P05-V3-AA01…AA04, FR-P06-V3-AA01…AA03, FR-P09-V3-AA01…AA03, FR-P13-V3-AA01…AA03 (Appendix AA §AA.24) and FR-P19-V3-AB01…AB08 (Appendix AB §AB.15).

**Exit gate**
1. All §12, Appendix AA §AA.22 and Appendix AB §AB.14 scenarios green on web and mobile.
2. Release-blocking CI tests green: `NO_PAID_PLACEMENT` (extended), `MKP_SURFACE_ISOLATION`, `GROUP_SHARE_SCOPE`, `R36_PROFILE_ALLOW_LIST`, `NO_ROLL_SCRAPING`, `ADVOCATE_TARIFF_LINT`, `RANKING_PARAMS_PUBLISHED`, `RANKING_IGNORES_PAID`, `SPONSORED_LABEL_PRESENT`, `SPONSORED_NOT_INTERLEAVED`, `SPONSORED_SLOT_CAP`, `NO_SPONSOR_IN_CASE_CONTEXT`, `MKP_REVIEW_OUTCOME_ITEM`, `MKP_OUTCOME_METRIC_FORBIDDEN`, `revenue-denylist` (registry-aware).
3. Simulation: 1,000 FIN bulk allocations and 200 COM rules-weighted allocations run with sponsorship forced ON in a test environment show zero difference from the OFF baseline.
4. Kill-switch drill: p95 ≤ 60 s for RS-18, RS-19 and RS-25 in staging; fail-safe deny proven with the config bus down.
5. Registry propagation drill: 500 updates and 50 erasures across two consumers, 100% acknowledged within 72 hours or incidents raised; reconciliation reports zero unexplained drift.
6. Tax vectors TCS-01…08 and TDS-01…05 pass; tax memo status recorded (or paid bookings remain blocked by `MKP_TAX_MEMO_MISSING`).
7. Marketplace Grievance Officer named in `tenant.legal_entity`; E-Commerce Rules controls checklist (seller details, ranking disclosure, grievance clocks, no pre-ticked boxes, complaint copy, NCH placeholder) signed by `compliance_officer`.
8. Dark-pattern baseline self-audit completed and certificate rendered (even with sponsorship OFF).
9. Flags OFF in production with approvers named: `marketplace.paid_placement`, `platform.rev.ads.enabled`, `directory.public_professionals`, `postres.advocate_panel`, `marketplace.advocate_neutrals.listing`, institute flags, `register.*`, `mkp.provider_subscriptions`, `marketplace.client_processing_fee`, `mkp.nch_integration.enabled`, `platform.rev.price_tests.enabled`; `billing.eco_gst_tcs` and `billing.eco_withholding` per tax memo.
10. Registry cannot accept consumers until `group.dir.owner_entity_id` has a Board resolution reference and at least one GDSA is live; the gate is proven in staging.
11. Exports for a provider, a professional and a tenant panel validate against the D3-07 manifest schema and open in Microsoft Office.
12. Security: threat model updated, DAST clean of high findings, authorisation matrix tests generated from Cerbos policies pass.

---

## 14. Open items and legal verification flags

| # | Item | Effect until closed | Owner |
|---|---|---|---|
| P19-OI-01 | *Sulekha.com v P.N. Vignesh*, SLP (C) 25794/2024, and *Anil Pandey v BCI*, WP (C) 817/2026 (AA-OI-01) | `directory.public_professionals` OFF; tenant-private registers only | Counsel |
| P19-OI-02 | Verbatim BCI r.36 proviso and Schedule; Ch. III r.2 official text (AA-OI-02) | Allow-lists per research; languages and courts filter-only | Counsel |
| P19-OI-03 | Advocate-neutral marketplace profiles under r.36 (pack OI-03; AA-OI-03) | `marketplace.advocate_neutrals.listing` OFF | Counsel |
| P19-OI-04 | Consumer Protection (E-Commerce) Amendment Rules 2026 — Gazette text, sub-rules, commencement (1 Jan 2027 per one source) (AA-OI-04) | Full compliance from go-live | Counsel |
| P19-OI-05 | Tax memo: e-commerce operator status for GST TCS and ITA 2025 s.393(1) Sl. 8(v) under the split-settlement model; SAC and rate on the take; interaction with payer TDS (AA-OI-05; LR-TAX-007/008) | Paid bookings blocked | Tax adviser; CFO |
| P19-OI-06 | RBI PA Directions 2025 and transfer holds (AA-OI-06) | Holds at PA/escrow bank only | Payments counsel |
| P19-OI-07 | ICSI aggregator position; ICMAI 2025 Gazette date; ICAI fee-sharing clauses (AA-OI-07) | Institute flags OFF | Counsel |
| P19-OI-08 | Mediation Council of India conduct standards (AA-OI-08) | `rulepack.IN.mkp.mci_conduct` empty; watch | Legal |
| P19-OI-09 | Registry owner entity designation; GDSA approvals under s.188; shareholding chain (AA-OI-09) | Registry consumers blocked | Company Secretary; Board |
| P19-OI-10 | NCH integration specification under the 2026 amendment | `mkp.nch_integration.enabled` OFF; manual reference entry | Counsel; Ops |
| P19-OI-11 | IT Rules amendment G.S.R. 120(E): specified-content categories for the 3-hour takedown and log retention | Conservative: 3-hour clock for all unlawful-content categories | Counsel |
| P19-OI-12 | Per-State e-stamp vendor authorisation evidence; ISL certifying bodies; valuer registration scope; document-writer licensing (AA-OI-11) | `SVC-EST` OFF; evidence-gated categories | Legal; Ops |
| P19-OI-13 | Board approvals: take rates, sponsored-listing rate card, advocate-neutral flat fee, provider plan prices, display-ad rates (AA-OI-12) | "Subject to Board approval"; no binding quotes | Board |
| P19-OI-14 | **Closed (v3.0 review):** the optional service-provider tools plan is registered in Appendix AB as stream RS-57 (N1, OFF; AB-R11) | Built behind `mkp.provider_subscriptions` (OFF) and the RS-57 registry guard; listing stays free; prices await the Board (P19-OI-13) | Appendix AB owner |
| P19-OI-15 | Declaration wording on criminal convictions and disciplinary history for providers | Neutral wording; counsel review before go-live | Counsel |

## v3 Addendum (23 October 2026)

The requirements below come from the v3.0 appendices and are part of this phase's scope and exit gate.

### From Appendix AF — Competitive Research v3: Jupitice, Institutions and Training

**FR-P19-V3-AF01 — Marketplace benchmark acceptance set.** The Appendix AA marketplace passes checks derived from §AF.1.7: public no-login search; published ranking page; sponsored label and cap when ON; fee breakup before booking; bank-escrow milestone release; independent fee-dispute route; export package; named grievance officer; mobile parity. *Acceptance:* each check is an automated test or a recorded UAT step before marketplace go-live.

**FR-P19-V3-AF02 — Quarterly Marketplace Transparency Report.** Generate REC-13 metrics with k ≥ 10 suppression and publish after compliance_officer sign-off. *Acceptance:* report renders from data only; no individual neutral is identifiable in any cell below the threshold.

