# Appendix O — Revenue Architecture, Plans and Benefits, Billing and Settings (binding specification)

> **Binding reference** for P05 (billing engine, subscriptions, mandates, invoices, settings pages), P10 (Private ADR Chambers plans, memberships, Institute referral), P13 (pricing pages and plan copy), P03 (no paid placement), P07 (renewal and dunning templates) and P09 (enterprise contracts). Read with the master prompt (NN-03, NN-13, NN-16, NN-17, NN-18, NN-25, NN-28, NN-29, NN-31), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` (R-20, R-30, R-37; D2-17, D2-18, D2-19), **Appendix B** (rate cards — B prevails on every figure that also appears in B, master §15), Appendix C (screen catalogue), Appendix F (DDL names), Appendix G (legal rules), Appendix K §4.4 (Explorer human review CTA), Appendix L (type copies, translations), Appendix M (AI Pleadings Studio), Appendix N (grades, allocation, Chambers), Appendix Q §4 (PCI DSS SAQ A) and Appendix S §7 (settings shell). Version 2.0, 21 October 2026.
>
> **Every price in this appendix is a default "Subject to Board approval"** (M-01; Appendix B §B.12). Prices are data in the Ruleset Studio fee editor and `core.plan_prices`, never constants in code. Figures are **exclusive of GST** unless a cell says "incl. GST" (Appendix B §B.0 convention); §6.4 governs how they are displayed to consumers. New lines introduced here are added to Appendix B as new cards (`NEU`, `CH-LITE`, `COUNSEL`, `BIZ`, `MEM`, `FORUM`) and new `ANC.*` lines in the P05 seed migration; Appendix B must be updated in the same PR (§10, FR-P05-V2-01).

## 0. Scope, precedence and reconciliations made here

| # | Topic | Resolution in this appendix |
|---|---|---|
| O-R1 | Figures overlapping Appendix B | Appendix B figures are reproduced unchanged (Cards ANC, FIN-L, INS-SUB, GRM, WRK-POSH, EAPI, CH, ACAD). Only **new** lines are priced here. |
| O-R2 | Marketplace take for Chambers bookings | Appendix B §B.7.7 has a flat 15%. This appendix makes it plan-dependent (Lite/Solo 15%, Pro 12%, Institution 10%) — Board item; B.7.7 to be amended. |
| O-R3 | Settings routes | P05 SCR-P05-11 `/(enterprise)/billing` and SCR-P05-12 `/(app)/subscriptions` are superseded by the `/settings/billing/*` pages in §5 (Appendix S §7 shell). Old routes 301-redirect. Screen IDs SCR-P05-19 → SCR-P05-34 are allocated here (Appendix C §A rule 1). |
| O-R4 | Consultation call price | Appendix C SCR-P13-14 says "₹1,000"; Appendix B ANC.CONSULT (₹999 / ₹1,999, credited on filing) prevails. Appendix K's free 10-minute process call-back (`talk_to_human`) stays free. |
| O-R5 | "Premium AI drafting ₹999/seat/month" (Card CH add-on) | Allowed only as a **neutral/secretariat** tool inside a Chambers tenant (orders, minutes, award skeletons). It never applies to party-side drafting: party drafting is the AI Pleadings Studio, free and identical for both sides (NN-25, §2.1.9). |
| O-R6 | Enterprise wallet (P05 FR-P05-39) vs RBI PPI rules | A wallet or credit balance may be redeemed only against **Equator's own supplies** (`revenue_owner = 'equator'` lines and `equator_principal` resupply). Redemption against `neutral_direct` fee notes or tenant fees is blocked (`WALLET_LINE_NOT_REDEEMABLE`), so the balance stays a closed-system prepaid instrument (§6.7). P05 FR-P05-39 is narrowed accordingly. |
| O-R7 | Plan name "Business Assure" | Kept as the management name (code `BIZ-ASSURE`). The C1 digest flagged "Equator Assurance" as a brand risk, and "assure/assurance" can suggest insurance or a guaranteed outcome. The public label is configuration (`plans.biz_assure.public_label`, default "Business Assure"), released only after a Claims Register entry and counsel's naming check (§11 Q-O3). |
| O-R8 | Membership Member grade entry rule | S9 proposed "Academy certificate" as the Member entry rule. Replaced by "a certificate from **any** recognised training provider (Appendix N list) + Equator assessment", so membership never steers learners to the Institute (D2-17). |

---

## 1. Revenue architecture

### 1.1 Principles (binding)

| ID | Principle | Enforcement |
|---|---|---|
| RA-1 | **Sell process, tools and administration — never outcomes, visibility or advice.** | Product gate `NO_LEGAL_ADVICE_product_gate`; §1.5 prohibited list as a CI deny-list on plan codes and feature flags |
| RA-2 | **Access to the forum never depends on a subscription.** Everything a party, counsel or panel neutral needs to take part in an Equator-administered case is available at ₹0 plan cost (case fees still apply per the vertical card). | `NN-16_no_paid_procedural_advantage` |
| RA-3 | **Equality of arms.** No paid feature operates on the content of a live Equator-administered proceeding unless the other side can get the same feature on the same terms (A&C Act 1996 s.18 equal treatment; NN-25). | Entitlement evaluator denies plan-gated features in `case_scope = 'administered'` unless flagged `parity_safe = true` |
| RA-4 | **Neutral selection, grading and directory order never read billing data** (NN-03, NN-16, NN-28). | `NO_PAID_PLACEMENT` CI test: no join path from `neutrals.directory_view`, allocation queries or grading jobs to `core.subscriptions`, `core.memberships`, `core.plans` |
| RA-5 | **Honest pricing** (NN-29): totals with GST for consumers, no drip pricing, cancellation no harder than sign-up, auto-renew OFF by default for individuals and SMEs. | §6 lint and tests |
| RA-6 | **Statutory duties are in every tier.** Regulator clocks, signposting, grievance intake and POSH inquiry access are never premium features and never blocked by dunning (FR-P05-37). | Entitlement matrix §4.2 marks these `always_on` |
| RA-7 | **Paid relationships are disclosed** to counterparties (NN-16): enterprise contracts, Business Assure, Users' Forum, partner status. | Disclosure banner component `CommercialRelationshipNotice` on notices and the counterparty's case view |

### 1.2 Revenue streams

Type key: **R** recurring subscription · **U** usage-recurring (contracted, billed on usage) · **T** transactional (per case or stage) · **O** one-time product · **M** membership.

| # | Stream | Type | Payer | Card / plan codes | Billing event | Notes |
|---|---|---|---|---|---|---|
| S-01 | Case fees: registration, administration, neutral fees | T | Parties (or enterprise) | FIN-R, COM-STD, FAM-STD, INS-RET, INS-COM, WRK-STD, INT-USD, INT-MED (App. B §B.11) | Filing; acceptance; appointment; session/deposit | Neutral components pass through (`revenue_owner = 'neutral'`) |
| S-02 | Settlement administration fee (B2B opt-in) | T | Business parties | COM-M, INT-M | Signed settlement | Only where all parties are businesses and opted in at filing |
| S-03 | Lender/NBFC programme | U | Lender | FIN-L + EAPI plan + volume tier | Monthly usage invoice | Borrower ₹0 |
| S-04 | Insurer programme | R + U | Insurer | INS-SUB, batched days | Annual fee + per-case overage | Policyholder ₹0 |
| S-05 | Employer programme | R + U | Employer | GRM-EMPLOYER + WRK-STD (employer-pays) + volume tier | Monthly | Employee pays nothing in employer-panel bulk |
| S-06 | GRM SaaS (4 variants) | R | Regulated entity, listed company, employer, HEI | GRM-* | Monthly/annual | Complainants ₹0 |
| S-07 | POSH / IC SaaS and services | R + O | Employer, HEI | POSH-*, IC services | Annual; per service | Complainant never charged |
| S-08 | Enterprise API, white-label, Clause Registry, BYOK | R | Enterprise | EAPI-*, add-ons | Monthly/annual | — |
| S-09 | Private ADR Chambers | R + T | Neutrals, firms, institutions | CH-LITE, CH-SOLO, CH-PRO, CH-INST, CH-IAAS | Monthly/annual + per case beyond allowance | Marketplace take per §0 O-R2 |
| S-10 | Counsel workspace | R | Advocates, firms | COUNSEL-PRO, FIRM-ENT | Monthly/annual | COUNSEL-FREE is ₹0 |
| S-11 | Business Assure (MSME/business annual plan) | R | MSMEs, businesses | BIZ-ASSURE-START/GROW/PLUS | Annual | Includes clause kit and case credits |
| S-12 | Neutral membership ladder | M | Individuals | MEM-ASSOC, MEM-MEMBER, MEM-FELLOW | Annual | Separate from empanelment |
| S-13 | Users' Forum | M | Companies, firms, associations | FORUM-CORP, FORUM-FIRM, FORUM-ASSOC | Annual | Member list published |
| S-14 | One-time products (documents and services) | O | Requester | ANC.* (§2.1) | On order | Includes certified copies, type copies, translations, transcripts, execution pack, e-stamp procurement, Explorer human review |
| S-15 | Marketplace and referral fees | T | Neutral (deducted), Chambers tenant | §B.7.7; Card CH referral 10% × 12 months | Monthly statement | No referral reward of any kind to advocates, bar bodies, CAs, CSs or CMAs (BCI Rules Part VI Ch. II Section IV r.36; NN-34; master X-62 — v3.0 supersedes "non-cash credits only") |
| S-16 | Academy (Equator ADR Institute — separate entity) | — for Equator | Learners, institutions | Card ACAD (Institute's revenue) | Institute's own billing | Equator earns nothing by default from referrals (§2.10) |
| S-17 | Research and statistics | Free | Public | India ADR Report, statistics feed | — | No case-level data sales (§1.5 X-09) |

### 1.3 Customer segments and the stream each buys

| Segment | Size/identifier | Entry product | Recurring product | One-time products | Must see first |
|---|---|---|---|---|---|
| Individual party (borrower, policyholder, spouse/heir, employee) | No GSTIN; consumer display | Dispute Explorer (free) | None (no subscription is ever offered in a case journey) | Explorer human review, certified copies, type copies, translations, execution pack | Free or statutory forum card (NN-20) |
| Business party (MSME, company) | GSTIN/Udyam | Explorer or clause kit | Business Assure | As above + transcript, bundle | Free MSME ODR/MSEFC route for delayed payments (Card COM-STD C10 note) |
| Lender / NBFC / HFC / MFI | RBI-regulated | GRM-LENDER or sandbox | FIN-L programme + EAPI + GRM | Execution packs per FIN-L L6 | Contract checklist §2.4.1 |
| Insurer | IRDAI-regulated | Settlement-day pilot | INS-SUB | Batched settlement days | No arbitration against retail policyholders (DB CHECK `no_arbitration_on_retail`) |
| Employer | Any; POSH duty at ≥ 10 employees (POSH Act 2013 s.4) | POSH checker | POSH SaaS, GRM-EMPLOYER, employer programme | IC training, external member | — |
| Listed company | SEBI LODR | GRM-LISTED | GRM-LISTED | — | SCORES clocks always on |
| University / college | UGC 2023 regulations | GRM-UNIV | GRM-UNIV; Institute membership (Institute's product) | — | — |
| Independent neutral | Individual | NEU-PANEL (free) | CH-LITE → CH-SOLO; membership | — | "Panel workspace is always free" |
| Law firm / advocate | Bar enrolment | COUNSEL-FREE | COUNSEL-PRO / FIRM-ENT | — | "Free access to every case you appear in" |
| Chamber of commerce, bar association, university centre | Institution | CH-INST trial | CH-INST / CH-IAAS | Secretariat add-on | Naming guardrail (P10 FR-P10-01) |
| Developer / platform (marketplace, ONDC seller app, HRMS) | Enterprise | EAPI-SANDBOX | EAPI | — | — |
| International business | Foreign party | INT pages | — (case-based) | Apostille facilitation, certified translation | Currency selector; NN-19 gates |

### 1.4 Unit-economics drivers (definitions for the finance dashboard)

All metrics are computed in `reporting.finance_*` views from the ledger (P05 FR-P05-52) and usage events; no case-identifying data leaves `core` (NN-16). Figures below are **definitions and formulas**, not forecasts.

| Driver | Formula / definition | Stream(s) | Lever |
|---|---|---|---|
| Institutional revenue per case | Σ institutional lines (`revenue_owner = 'equator'`) net of concessions, promos and credit notes ÷ cases closed in period | S-01, S-03, S-05 | Fee card, concession mix, stage reached |
| Neutral pass-through ratio | Σ neutral lines ÷ Σ all case lines | S-01 | Not a margin lever: neutral fees are never discounted (App. B P2) |
| Cost to serve per case | Notices (SMS/WhatsApp/voice/post at provider cost) + eSign/eStamp provider cost not recovered + video minutes + LLM tokens (AI Gateway cost meter) + OCR/translation pages + storage + case-manager minutes × loaded rate + gateway fee | All | Automation rate, channel mix (digital before physical) |
| Gateway cost | Σ PG fees (MDR, platform fee, Route transfer fee) by method; UPI share | All | UPI-first checkout on mobile (P05 SCR-P05-02) |
| Contribution margin per case | Institutional revenue per case − cost to serve per case | S-01, S-03 | — |
| MRR / ARR | Σ active subscription price normalised to monthly (annual ÷ 12) by plan family | S-06 … S-13 | Plan mix, annual share |
| Net revenue retention (NRR) | (Opening MRR + expansion − contraction − churn) ÷ opening MRR, cohort of 12 months | S-06 … S-11 | Seats, tier upgrades, overage |
| Logo churn | Subscriptions moving to `cancelled`/`expired` ÷ active at period start | Recurring | Honest retention only (§5.12) |
| Allowance utilisation | Used ÷ included per meter (§4.3) | Recurring | Right-sizing at renewal (never upsell inside case views) |
| Committed-use attainment | Actual annual run-rate ÷ committed volume (enterprise) | S-03, S-05, S-08 | True-up (§2.4.3) |
| Recurring revenue share | Recurring + usage-recurring revenue ÷ total revenue, by vertical | All | Board pack tile vs Portfolio Model targets (FIN 55%, WRK 70%, INS 41%, COM 30%, FAM 35% — corpus C-29) |
| Concession cost | Σ concessions absorbed by Equator ÷ institutional revenue | S-01 | Policy only; never a growth lever (App. B P8) |
| Payback on enterprise acquisition | Sales and onboarding cost ÷ monthly contribution of the contract | S-03 … S-08 | — |
| Chargeback reserve ratio | Reserve ÷ monthly card volume (default 0.5%, FR-P05-57) | All | — |

### 1.5 What Equator must not sell (D2-18) — deny-list

IDs X-01…X-16 in this appendix are deny-list items, not the master §15 resolutions; references to the latter are written "master X-nn".

The CI job `revenue-denylist` fails if a plan, tariff item, feature flag, CMS price block or CTA matches any row (matching on codes, tags and copy linter phrases).

| ID | Not sold | Reason (source) | What Equator offers instead |
|---|---|---|---|
| X-01 | One-sided legal advice, merit opinions, "case strength" or outcome prediction, valuation of a claim | Advocates Act 1961 ss.29, 33; *Bar Council of India v A.K. Balaji* (2018) 5 SCC 379 (practice of law includes non-litigious work); NN-01 GX-1–GX-3 | Process information; free Explorer; Explorer human review (process only); "Find an advocate" signposting to bar-association lists (no commission) |
| X-02 | Legal notice / demand letter drafted by Equator for one party | Same; institution would be partisan | Free self-help letter library `/help/letters` (S9 FR-S9-06) and institutional "Invitation to mediate" notice (neutral wording, included in registration) |
| X-03 | Paid visibility for neutrals: featured, sponsored or "spotlight" listings, sort boosts, paid "verified" badges | NN-16, NN-28; Dark Patterns Guidelines 2023 Annexure 1 "Disguised Advertisement"; CCPA Misleading Advertisements Guidelines 2022; BCI r.36 for advocate-neutrals | Directory order seeded-random within filters (App. C §F.7); badges only from verification records |
| X-04 | Empanelment or panel-listing fees | Looks like selling appointments (App. B Card ACAD: empanelment listing ₹0) | EQAP sitting fee, identical for every candidate whatever their training provider (Appendix N §4.8, CN-04); no listing fee |
| X-05 | Priority case assignment, "premium access to the arbitrator database", panel preference, veto, or any appointment influence for subscribers (Marketing Playbook "Premium Institutional Subscription") | NN-03; *CORE v ECI-SPIC-SMO-MCML* (SC, 8 Nov 2024); A&C Act s.12 and Fifth Schedule | Users' Forum (§2.9) — nothing touching a pending case |
| X-06 | Paid AI drafting or analysis available to one side inside a live administered case | A&C Act s.18; NN-25 | AI Pleadings Studio free, identical for both sides (§2.1.9) |
| X-07 | Percentage-of-claim or success fees in retail insurance, FIN retail, FAM, individual WRK, POSH | App. B §B.1 P3; Equator Insurance Rules r.27; X-07 master §15; BCI Part VI Ch. II Section II r.20 (no contingency for advocates) | Flat published fees; free statutory routes first (S3 PI-INS-01) |
| X-08 | Fees added to a borrower's loan dues by Equator documents | RBI KFS instructions (15 Apr 2024); App. B §B.13 item 11 | Lender-pays programme |
| X-09 | Licensing of case-level or pseudonymised case data; per-party or per-neutral statistics | A&C Act s.42A; DPDP Act 2023 purpose limitation; NN-16 | Free aggregate statistics and India ADR Report (k ≥ 10 cell suppression) |
| X-10 | Sponsorship by a repeat-player enterprise of neutral CPD, empanelment or assessment programmes | Apparent bias (S9 E-9) | Disclosed sponsorship of student competitions only, on the public sponsorship register |
| X-11 | Referral rewards of any kind (cash, commission, credits, discounts, gifts or priority) to advocates, bar bodies, CAs, CSs or CMAs or their firms | BCI Rules Part VI Ch. II Section IV r.36 and Ch. III r.2; ICAI, ICSI and ICMAI guidelines ([RE] F1.2–F1.5); NN-34 | None. *v3.0 (23 Oct 2026): the v2.1 "non-cash credits only" exception is withdrawn (master X-54, X-62; D3-27); professionals may be relationship partners without reward* |
| X-12 | Outcome guarantees ("resolved in 30 days or your money back") without a precise, Claims-Register-backed definition | CPA 2019 s.2(28); CCPA Misleading Advertisements Guidelines 2022 | None at launch (S9 E-12 rejected until defined) |
| X-13 | Mandate or "auto-pay convenience" fees | RBI E-mandate Framework 2026 (no charge to customer for the facility) | — |
| X-14 | Fees for signposting, Explorer, interpretation for individuals in enabled languages, POSH complainants, DPDP requests, case-status verification, first certified copy | App. B §B.1 P5 | ₹0 lines |
| X-15 | Upsell, upgrade or cross-sell prompts inside case, hearing, signing, payment-of-case-fee or sealed views | NN-29 (Nagging); neutrality | Upgrade prompts only in Settings and pricing pages (§6.2 DP-10) |
| X-16 | Insurance claim "preparation" services for policyholders by Equator | Insurance Act 1938 s.2(10B) and s.42D (intermediary registration) — unsettled (02 §5 Q10; S3 C5) | Free Ombudsman route first; neutral mediation at flat fee |

---

## 2. Plan and product catalogue

Each entry states: **for** (who it suits) · **includes / excludes** · **price and billing** (all "Subject to Board approval"; ex-GST unless stated) · **renewal, cancellation, refund, tax** · **user benefit** · **how it differs** from the nearest alternative. Refund codes refer to Appendix B §B.8; tax codes to §B.4/§B.10.

Common terms (apply unless an entry says otherwise):

| Term | Rule |
|---|---|
| GST | 18% forward (T01–T04 by place of supply); export under LUT for foreign recipients (T05). SAC 998215 for ADR services and one-time case products; SaaS plans 998315 or 997331 per the tax memo (App. B §B.10). |
| Annual price | 10 × monthly (shown as "₹X billed yearly — you save ₹Y", where Y = 2 × monthly; never a countdown offer). |
| Auto-renew default | **OFF** for individuals and SMEs (counsel, Lite/Solo, memberships, Business Assure); **contract-governed** for enterprise, GRM, POSH, EAPI, CH-PRO/INST (auto-renew allowed only with an active mandate or a signed order form). |
| Renewal reminders | T-30, T-7 and T-1 days (service templates, P07); the bank's own ≥ 24 h pre-debit notice applies to every mandate debit (RBI E-mandate Framework 2026). |
| Trials | No payment method needed at trial start; **trials never convert automatically** (`trial_converts_automatically = false`). |
| Refund (subscriptions) | RP-SUB: monthly fees non-refundable; annual plans non-refundable except Equator convenience termination or Equator material breach (pro rata); a **14-day cooling-off full refund** applies to first-time annual purchases by individuals and SMEs (no GSTIN or Udyam micro/small) if no included entitlement has been used — Equator default for consumer trust **[Board]**. |
| Downgrade | Effective next cycle; no refund of the current cycle. |
| Data | Workspace export always available; 90 days after cancellation for subscription workspaces; case records follow the retention schedule regardless of billing (master §11). |

### 2.1 Parties — pay per case and one-time products

#### 2.1.1 Pay-per-case (all six verticals)

| Field | Content |
|---|---|
| For | Any party filing or responding in an Equator-administered case |
| Includes | Registration (digital notices with 3 attempts, institutional invitation notice, case portal, Draft Assist / AI Pleadings Studio within fair use, hearing room, case-status tracker, first certified copy of the outcome to each party, interpretation in enabled Indian languages for individuals); administration per stage; neutral fees per the card |
| Excludes | Pass-throughs at actuals (stamp duty, registration fees, postage, bank/trustee charges — T15), optional one-time products (§2.1.2–§2.1.8) |
| Price and billing | Vertical cards FIN-R, COM-STD, FAM-STD, INS-RET, INS-COM, WRK-STD, INT-USD, INT-MED (App. B §B.11). Billed by stage: registration at filing; administration at acceptance; neutral fees on appointment or per session/deposit; payer rule per card |
| Refund | RP-STD-MED, RP-STD-ARB, RP-INS-RET, RP-INS-COM by mechanism (App. B §B.8); refund to original instrument |
| Tax | Equator lines 18% forward; tribunal fees RCM/exempt (T09/T10); neutral fees per neutral's GST status (T11/T12) |
| Benefit | You see the whole cost before you start; you pay only for the stage you reach; concessions for hardship, seniors, persons with disabilities, legal-aid referrals |
| Differs from | Business Assure (prepaid credits for repeat business filers) and enterprise programmes (counterparty pays ₹0) |

#### 2.1.2 Explorer human review (`ANC.EXPLORER.REVIEW`, new)

| Field | Content |
|---|---|
| For | A person who has completed the free Dispute Explorer and wants a case manager to check the report for process accuracy (Appendix K §4.4 CTA `request_human_review`) |
| Includes | A case manager reviews the answers and report for missing facts, wrong forum, missed dates and documents; written note within 2 working days; one follow-up message; process information only |
| Excludes | Any view on merits, strength, likely outcome or value (NN-01 GX-1–GX-3); drafting of letters; representation |
| Price | **₹499 per report** (₹588.82 incl. GST); credited against registration if a case is filed within 30 days; **₹0** where any of CN-HARD, CN-SENIOR, CN-PWD, CN-LEGALAID, CN-DV, CN-INS-SMALL, CN-GOVT-SCHEME applies (`concession.explorer_review_free`) |
| Refund | 100% if the note is not delivered within 2 working days (auto-refund job); otherwise non-refundable once delivered |
| Benefit | A person checks that you have the right forum, dates and documents before you spend more |
| Differs from | Free 10-minute call-back (spoken, general) and ANC.CONSULT (live 30/60-minute process consultation) |

#### 2.1.3 Process consultation (`ANC.CONSULT`, App. B)

₹999 (30 min) / ₹1,999 (60 min), credited against registration if filed within 30 days; process information only; script forbids merits (GX-1); if legal advice is wanted, the screen shows "Find an advocate" (bar-association lists, no commission). Refund 100% if Equator cancels or the slot is missed by Equator; user cancellation ≥ 24 h before → 100%; < 24 h → 50% (symmetry: if Equator cancels late, the user gets 100% + free rebooking — E-Commerce Rules 2020 r.4 cancellation-charge symmetry).

#### 2.1.4 Certified copies (`ANC.CERT.COPY`, App. B)

First certified copy of each outcome document to each party **₹0** (A&C Act s.31(5) delivery of a signed copy; App. B P5); additional certified copies **₹500 per copy** (digital, QR-verifiable; physical dispatch + postage at actuals). Non-refundable once issued.

#### 2.1.5 Type copies (`ANC.TYPECOPY`, new — Appendix L §6)

| Variant | Content | Price |
|---|---|---|
| AI type copy (self-service) | Typed transcription of handwritten pages or screenshots inside the AI Pleadings Studio / DMS; user corrects; labelled "Type copy" with confidence and uncertain passages; original preserved (NN-32) | ₹0 within fair use (§4.4) |
| Verified type copy | Secretariat-verified line-by-line against the original; certificate "True type copy prepared by Equator secretariat from the original uploaded on {date}, hash {sha256}"; for annexures and court filings | **₹40 per page (≤ 300 words)**, **₹60 per page (> 300 words)**, minimum ₹200 per order; delivery 3 working days (express 1 working day + 50%) |

Same price for every party in the case (parity). Refund: 100% if not delivered on time; corrections of Equator errors free.

#### 2.1.6 Translations (`ANC.TRANSL.*`, new — Appendix L §7)

| Variant | Content | Price |
|---|---|---|
| Convenience translation — individuals | Machine translation with glossary + automated QA, labelled "Translation — for convenience" (NN-32), into/from English and the 11 enabled Indian languages (Hindi + 10, NN-23) | ₹0 up to 100 pages per party per case; then ₹150/page |
| Convenience translation — business parties | Same, with human review | ₹300/page (Indian languages); ₹400/page (UN official languages other than English: Arabic, Chinese, French, Russian, Spanish) |
| Certified translation | Sworn/qualified translator; notarisation if required for court or foreign enforcement | At actuals + 10% (App. B ANC.INTERP) |

#### 2.1.7 Hearing transcripts (`ANC.TRANSCRIPT`, new)

Arbitration only, and only with the recorded consent of all parties and the tribunal (NN-11; never mediation or conciliation). AI transcript with human proof-reading **₹1,500 per hearing-hour** (billed in 15-minute units); live stenography at actuals + 10%. Payer: requesting party, or `equal_split` where PO1 so directs. Delivered with a hash and a BSA 2023 s.63(4) certificate part generated from the evidence ledger (NN-10).

#### 2.1.8 Outcome and enforcement products (App. B Card ANC unless "new")

| Code | Product | Price |
|---|---|---|
| ANC.EXEC.PACK | Execution pack (A&C s.36 + CPC Order XXI annexures; Appendix R §4) | ₹2,500 (claim ≤ ₹50 lakh) / ₹5,000 (above); FIN-L per card |
| ANC.ESTAMP | e-Stamp procurement | ₹49 per certificate + duty at actuals |
| ANC.STAMP.PHYSICAL | Franking / e-SBTR / stamp-paper facilitation | ₹500 per instrument + duty at actuals |
| ANC.ESIGN | e-Sign | Provider charge at actuals + ₹20 per signature |
| ANC.REGN.FACIL | Registration-route facilitation (NN-08) | ₹5,000 per instrument + statutory fees at actuals |
| ANC.BUNDLE (new) | Paginated, hyperlinked hearing bundle prepared by the secretariat | ₹1,000 per 250 pages (CN-HARD waivers apply) |
| ANC.APOSTILLE (new) | Apostille/legalisation facilitation for awards to be enforced abroad (INT) | ₹2,500 + government and courier charges at actuals |

#### 2.1.9 AI Pleadings Studio — included, fair use (Appendix M)

| Field | Content |
|---|---|
| For | Every party (and its representative) in an administered case, on identical terms (NN-25) |
| Includes | Statement of claim, response/statement of defence, counterclaim, rejoinder, list of dates, synopsis, index, affidavit text (sworn before an oath commissioner/notary), AI type copies and convenience translations of the party's own material, within the fair-use meters in §4.4 |
| Excludes | Suggested defences, provisions or precedents (S9 C-21 / FR-S9-05); any edit by Equator staff; filing without the user's approval |
| Price | **₹0** — no paid tier and **no paid overage** for parties. If a fair-use cap is reached, the case manager may raise it for **all parties in that case equally** (`PLEADINGS_FAIR_USE_RAISED` audit event) |
| Benefit | Turn your own documents into a clear, properly formatted filing; every sentence points to its source |
| Differs from | Counsel-Pro (practice management, not drafting advantage) and Chambers premium AI (neutral-side tool) |

### 2.2 Counsel

| Plan | COUNSEL-FREE | COUNSEL-PRO | FIRM-ENT |
|---|---|---|---|
| For | Every advocate or authorised representative appearing in an Equator case | Advocates managing several Equator matters across clients | Law firms with ≥ 10 seats needing SSO and matter-level permissions |
| Includes | Authorities/vakalatnama (App. S §4), filing and response for clients, documents, hearings, messages, client invoices from the case, Pleadings Studio on the same terms as the client | Everything in Free + cross-client matter dashboard, team seats and matter assignment, calendar sync (Google/Outlook, case number only in titles), bulk download of own case files, client-update share links, firm-branded client reports, saved firm clause precedents in the clause builder | Everything in Pro + firm SSO, matter-level permissions, DMS export, firm admin console (App. S §4.6), named support |
| Excludes | — | **Anything that changes how a proceeding runs**: no faster scheduling, no priority, no extra drafting power inside an administered case, no neutral information beyond what parties see | Same exclusion |
| Price and billing | ₹0 | **₹999 per seat per month** or **₹9,990 per seat per year** | Quote (floor ₹799/seat/month on annual terms) |
| Renewal / cancel / refund | — | Auto-renew OFF by default; cancel in ≤ 3 steps; RP-SUB with 14-day cooling-off on first annual purchase | Per order form |
| Tax | — | 18% (SaaS SAC per tax memo); TDS by firm per s.393(1) Table Sl. 6(iii) where applicable | Same |
| Benefit | Appear for any client without paying Equator anything | One place for all your Equator matters and your team | Firm-wide control and single sign-on |
| Differs from | — | Practice convenience only; the other side's counsel on Free has identical procedural tools (RA-3) | Adds identity and governance controls |

Disclosure: if a firm is also a referral partner, the relationship is disclosed to counterparties (NN-16). No referral reward of any kind is given to advocates, CAs, CSs or CMAs (X-11 as amended in v3.0; master X-62).

### 2.3 Businesses and MSMEs — Business Assure (annual plan)

| Field | BIZ-ASSURE-START | BIZ-ASSURE-GROW | BIZ-ASSURE-PLUS |
|---|---|---|---|
| For | Micro and small enterprises (Udyam) and start-ups | Growing businesses with regular B2B contracts | Mid-size businesses with many contracts and occasional disputes |
| Clause kit | Model Equator clauses (negotiation → mediation → arbitration ladders by contract type), plain-language clause notes, 10 registered contract instruments/year in the Clause Registry (QR seal, P09 SCR-P09-05) | 50 instruments/year + bulk clause export | 250 instruments/year + API clause insertion (EAPI-SANDBOX → STARTER credentials, no platform fee) |
| Case credits (prepaid entitlement) | ₹6,000 credit value | ₹18,000 credit value | ₹40,000 credit value |
| Explorer human reviews | 2 | 5 | 12 |
| Process consultations (60 min) | 1 | 2 | 4 |
| Seats (business users) | 2 | 5 | 15 |
| Dashboards | Disputes and contracts overview | + clause coverage by counterparty | + MIS export |
| Price | **₹9,999 per year** | **₹24,999 per year** | **₹49,999 per year** |
| Billing | Annual in advance; no monthly option | Same | Same |

Rules:

1. **Credits** are redeemable only against Equator's own institutional lines (registration, administration, ANC lines with `revenue_owner = 'equator'`) in cases where the plan holder is a party, for the plan holder's own share or — by express choice — for a counterparty's share (`paid_on_behalf_of`). Never against neutral fees, pass-throughs, regulated tables (SEC) or tenant fees (O-R6). Credits are applied after concessions and before promos in the App. B §B.9.4 stack; neutral components are untouched (App. B P2).
2. **Credit validity:** plan term + 90 days; unused credits lapse (shown on the purchase page, in the T-60/T-30 reminders and on the Wallet page §5.8). Credits are not cash, carry no interest, are not transferable and are not refundable except under RP-SUB convenience/breach termination (pro rata to unused value).
3. **No procedural benefit.** Business Assure gives no priority, no neutral choice, no faster scrutiny and no information the counterparty does not get. Counterparties see the `CommercialRelationshipNotice`: "{Business} holds an Equator Business Assure plan. This gives it no say in who decides your matter and no priority."
4. **Excludes:** bespoke drafting, legal advice, contract review opinions (X-01), representation.
5. **Renewal:** auto-renew OFF by default; reminders T-60 (with credit balance), T-30, T-7, T-1.
6. **Refund:** 14-day cooling-off full refund on first purchase if no entitlement used; else RP-SUB.
7. **Tax:** the plan invoice is a tax invoice for the full plan price at issue. Case invoices for credit-covered lines show the line, the credit applied and "Covered by Business Assure credit — invoice {no}"; the tax treatment of credit redemption (entitlement already taxed vs advance adjusted under CGST Rules r.50/r.51) follows the tax memo **[VERIFY — open: tax memo, same question as App. B T16]**.
8. **Benefit copy:** "Put fair dispute clauses in your contracts and pre-pay for resolving the disputes that still happen."
9. **Differs from** pay-per-case (the plan bundles the clause kit, Clause Registry instruments, seats and dashboards with prepaid credits — START: ₹6,000 credit + 2 Explorer reviews + 1 consultation + clause kit for ₹9,999; the credits alone are not cheaper than paying per case, and no saving is claimed without a Claims Register entry) and from enterprise programmes (no volume commitment, no API platform fee, no counterparty-pays-nothing structure).

### 2.4 Enterprise ODR contracts (lenders, insurers, employers)

#### 2.4.1 Contract structure

| Component | Lender (FIN) | Insurer (INS) | Employer (WRK) |
|---|---|---|---|
| Platform | EAPI-STARTER/GROWTH/SCALE (Card EAPI) or GRM-LENDER | INS-SUB-ENTRY/STD/ENT/GROUP | GRM-EMPLOYER-S/M/L |
| Per-case pricing | Card FIN-L stage table (L1–L7) | INS-SUB overage per case; batched settlement days | Card WRK-STD with payer rule `employer_pays` (100%) in employer-panel bulk |
| Programme discount | Any EAPI plan −25% on institutional components | Included in subscription | EAPI plan −25% if subscribed |
| Volume tiers (annual committed cases; institutional components only) | T1 5,000+ −10% · T2 25,000+ −20% · T3 1,00,000+ −30% + dedicated case desk | Plan band by grievance volume | Same T1–T3 |
| Counterparty pays | ₹0 (borrower) | ₹0 (policyholder) | ₹0 in employer-panel bulk; 75:25 split only for individually filed matters (WRK-STD) |
| Neutral fees | Never discounted; identical settled or not (App. B P2, P3) | Same | Same |
| Independence | No choice or veto of neutrals; Independence Evidence Pack free (NN-03) | Same; no arbitration against retail policyholders | Same; arbitration only for non-workman contracts |
| Billing | Monthly usage invoice on the 1st (IST) per billing GSTIN with masked annexure (FR-P05-38) | Annual fee in advance + quarterly overage invoice | Monthly |
| Payment | NEFT/RTGS to virtual account, eNACH mandate, or prepaid wallet (Equator lines only, O-R6) | Same | Same |
| Term | 12 or 36 months; renewal by order form; non-renewal notice 60 days | Same | Same |
| Exit | Data export; open cases continue under pinned rules; dunning never stops clocks or grievance intake | Same | Same |

Contract clause heads are structured fields on `core.enterprise_contracts` (§8.1; S9 §1.6 checklist; FR-S9-09): scope and mechanisms, loan/policy products, claim ceiling, price table version, committed volume, tier, true-up dates, SLA and credits, contact-conduct terms (NN-12), DPA and data roles (NN-14, NN-15), disclosure flag, authority-to-settle evidence (board resolution or authority letter before L2 conciliation — S9 C-33), RBI outsourcing interface clauses where the lender treats ODR as outsourcing **[VERIFY — open: current RBI outsourcing Directions for the lender's RE category]**.

#### 2.4.2 Committed use

| Option | Mechanics | Default |
|---|---|---|
| Volume commitment | Annual committed case count sets the tier from day 1 | ON |
| Spend commitment | Annual ₹ commitment drawn down by rated usage; unused commitment at year end is **not** charged unless the shortfall fee is ON | Available on request |
| Minimum-commitment shortfall fee | (Committed − actual) × tier rate × shortfall % | **OFF** (App. B Card EAPI) |
| Prepaid wallet | Optional; Equator lines only (O-R6); low-balance alerts at 20% and 10% of 30-day consumption | Optional |

#### 2.4.3 True-up (quarterly, prospective)

1. At each quarter end (31 Mar, 30 Jun, 30 Sep, 31 Dec), `TrueUpJob` computes `run_rate = actual_cases_contract_ytd × 12 / months_elapsed`.
2. **Up-tier:** if `run_rate ≥` the next tier threshold, the higher tier applies **from the first day of the next quarter** automatically (customer benefit; notice by email).
3. **Down-tier:** if `run_rate < 0.9 × current_tier_threshold` for **two consecutive quarters**, the lower tier applies from the first day of the next quarter, after **30 days' written notice** with the computation attached.
4. No retroactive re-rating unless the contract has `retro_true_up = true` (default false); if true, a credit or debit note is issued at the anniversary for the difference (CGST s.34).
5. Every run writes `core.true_up_runs` with inputs, outputs and hash; the Enterprise contract page (§5.15) shows the forecast tier.

### 2.5 GRM SaaS (four variants; Card GRM)

| Variant | Plans (monthly; annual prepay = 10 × monthly) | Included tickets/month → overage | Always on in every tier | For |
|---|---|---|---|---|
| Lender → borrower | GRM-LENDER-S ₹25,000 · M ₹50,000 · L ₹1,00,000 | 500 → ₹40 · 2,500 → ₹30 · 10,000 → ₹20 | RB-IOS 2026 30-day RE window, Internal Ombudsman routing where applicable, GRO details in replies | Banks, NBFCs, HFCs, LSPs |
| Listed company → shareholder/investor | GRM-LISTED-S ₹15,000 · M ₹35,000 | 100 → ₹50 · 1,000 → ₹40 | SEBI LODR/SCORES-mapped clocks, RTA hand-off | Listed companies |
| Employer → employee | GRM-EMPLOYER-S ₹10,000 (≤ 250) · M ₹25,000 (251–2,000) · L ₹15/employee, min ₹40,000 (> 2,000) | 200 → ₹40 · 1,000 → ₹30 · 3,000 → ₹20 | IR Code 2020 GRC workflow | Employers |
| University → student | GRM-UNIV-S ₹10,000 · M ₹20,000 · L ₹30,000 | 300 → ₹30 · 1,000 → ₹25 · 3,000 → ₹20 | UGC 2023 SGRC and Ombudsperson clocks | HEIs |

Complainants pay ₹0. Escalation to ODR is billed on the vertical card. Overage is billed monthly in arrears; **intake never stops at the allowance** (soft limit — RA-6). Refund RP-SUB. Benefit: "Answer every grievance inside the regulator's clock, with an independent escalation route." Differs from enterprise ODR (GRM handles the regulated entity's own grievance duty; ODR is independent resolution).

### 2.6 POSH / IC SaaS (Card WRK-POSH)

POSH-SME ₹15,000/yr (≤ 50 employees) · POSH-GROWTH ₹36,000/yr (51–500) · POSH-ENT ₹90,000/yr (501–5,000) · POSH-LARGE ₹30/employee/yr, min ₹1,50,000 (> 5,000); e-learning ₹40/employee/yr; external IC member ₹60,000/yr retainer + ₹15,000 per inquiry (marketplace 15%); IC training ₹35,000, awareness ₹15,000, annual-report support ₹20,000, compliance audit ₹50,000. Annual in advance; RP-SUB. **Complainants are never charged and an open inquiry inside its 90-day clock is never blocked by billing** (NN-07; FR-P05-37). Employee-count meter is self-declared with annual attestation; over-count triggers a prospective re-band at renewal, never mid-inquiry. Benefit: "Run your Internal Committee lawfully, on time and in a sealed workspace." Differs from GRM-EMPLOYER (general grievances, not sealed).

### 2.7 API and white-label (Card EAPI)

EAPI-SANDBOX ₹0 · EAPI-STARTER ₹25,000/month (2,50,000 calls; ₹50 per 1,000 beyond) · EAPI-GROWTH ₹60,000 (10,00,000; ₹40) — includes clause API and **white-label party portal** · EAPI-SCALE ₹1,00,000 (50,00,000; ₹30) — mTLS, SFTP, 99.9% SLA credits. Add-ons: Clause Registry ₹1,50,000 / ₹3,00,000 / ₹5,00,000 per year; BYOK ₹2,00,000/yr; dedicated SFTP ₹10,000/month. White-label rule: the portal may carry the enterprise's brand **beside** Equator's institutional identity; the institution, rules and neutral appointment are always Equator's and the page says so (NN-03, NN-17). Institutions that want their own centre buy Chambers (CH-INST/CH-IAAS), not EAPI white-label.

### 2.8 Private ADR Chambers (L2; P10) and neutral plans

| Plan | NEU-PANEL | CH-LITE (new) | CH-SOLO | CH-PRO | CH-INST | CH-IAAS |
|---|---|---|---|---|---|---|
| For | Every empanelled neutral | Neutral with occasional private matters | Independent neutral running a practice | Groups, small firms, ADR chambers | Chambers of commerce, bar associations, university centres, large firms | Bodies wanting a managed centre |
| Price | ₹0 | **₹699/month or ₹6,990/year**, 1 seat | ₹1,499/seat/month or ₹14,990/seat/year; 1–2 seats | ₹2,999/seat/month or ₹29,990/seat/year; min 3 | ₹4,999/seat/month or ₹49,990/seat/year; min 10 | ₹3,00,000–₹8,00,000/yr + revenue share |
| Private matters included | — (administered cases only) | 2 new/month | 5 new/month | 25 new/month | 100 new/month | Contracted |
| Beyond allowance | — | ₹999 per matter or upgrade | ₹999 | ₹899 | ₹799 | Contracted |
| Key entitlements | Full workspace for Equator-administered cases: calendar, hearings, drafting with AI drafts under human review, DSC/eSign, earnings, tax profile, CPD record, profile | Own-brand workspace on `{slug}.chambers.equatorresolution.in`, Equator Rules template, fee-note generation with GST, client intake link, 50 GB storage | + standard templates, 2 seats | + custom domain, own rules and fee schedules, own panel with allocation engine, overflow listings | + SSO, API keys, own committees, public panel directory, MIS, bulk intake (P10 FR-P10-06) | + managed secretariat, hearing support, co-branded rules |
| Excludes | Any effect on allocation, ranking or visibility | Custom domain, team seats, own panel | Own panel | — | — | — |
| Marketplace take (bookings via Equator marketplace) | n/a (0% on administered cases, App. B §B.7.7) | 15% | 15% | 12% | 10% | Contracted |
| Trial | — | 14 days | 14 days | 14 days | 14 days | Pilot by contract |
| Auto-renew default | — | OFF | OFF | ON (order form) | ON (order form) | Contract |

Rules: add-ons per Card CH (secretariat, video beyond 1,000 participant-minutes/seat/month ₹1.50, premium AI drafting ₹999/seat/month for neutral-side drafting only (O-R5), messaging at actuals + 10%, storage ₹500/100 GB/month). Run-off guarantee: parties' matters continue 90 days after suspension or cancellation (P10 FR-P10-04). Code of Conduct: no side payments on Equator-administered cases; Chambers terms mirror it (S9 FR-S9-30). Chambers subscription status never affects a neutral's Equator panel grade or allocation (RA-4). Benefit copy: "Run your own ADR practice on Equator's case, hearing, payment and e-sign tools." Differs: Lite is the low-cost practice tier below Solo; Panel is free and covers only Equator-administered work.

### 2.9 Neutral memberships and Users' Forum

#### 2.9.1 Membership ladder (issuer: Equator Resolution Service Private Limited; separate from empanelment)

| Grade | Entry rule | Annual fee | Benefits | Never a benefit |
|---|---|---|---|---|
| Student Associate | Enrolled law/ADR student | ₹0 | Newsletter, webinars, competition notices | — |
| Associate (AEqR) | Completion of any recognised ADR course (Appendix N list, not limited to the Institute) | ₹2,500 | CPD log, member events, resource library (rules commentary, practice notes, templates for private practice), member pricing at events | Panel eligibility, grade, allocation, directory position |
| Member (MEqR) | Certificate from any recognised provider + Equator assessment (O-R8) | ₹5,000 | Above + mentoring circle, co-mediation **observation** slots (observer role, consent of parties), verified membership page | Same |
| Fellow (FEqR) | Member + ≥ 25 completed matters at any institution + peer review | ₹10,000 | Above + Fellows' forum, rules-consultation responses, speaking roster for public events | Same |

No joining fee. Auto-renew OFF; renewal by active choice. Grace 30 days after expiry, then designation use ceases (Settings shows "You may not use AEqR/MEqR/FEqR after {date}"). Refund: 14-day cooling-off on first purchase; else non-refundable. GST 18%. Post-nominals need trademark clearance and counsel review (S9 §10 Q8) — flag `membership.postnominals.enabled` OFF until cleared. **Empanelment and grading (Appendix N) never read membership data** (RA-4).

#### 2.9.2 Users' Forum (replaces the Playbook "Premium Institutional Subscription")

| Tier | FORUM-CORP (company) | FORUM-FIRM (law firm) | FORUM-ASSOC (MSME, association, NGO) |
|---|---|---|---|
| Price | ₹1,50,000/yr | ₹75,000/yr | ₹25,000/yr |
| Benefits | Annual rules-consultation seat, 5 event seats, quarterly briefing on **published** aggregate statistics, clause-drafting clinic | Rules-consultation seat, 3 event seats, quarterly briefing | 1 seat, quarterly briefing |
| Never | Anything touching a pending case; panel access; appointment influence; non-public data | Same | Same |

The member list is published on `/trust/how-we-stay-neutral`; membership is a disclosed relationship in any case where a member is a party (NN-16). Annual in advance; auto-renew per order form; RP-SUB.

### 2.10 Academy referrals (Equator ADR Institute is a separate entity)

| Rule | Detail |
|---|---|
| Separation | Institute courses are sold and invoiced by the Institute (Card ACAD). Equator pages show "Equator ADR Institute is a separate organisation related to Equator" wherever a referral appears (flag `academy.institute_referral`, gated on assumption A-03). |
| Choice | Every training referral card lists **at least three** recognised providers, the Institute being one (D2-17); order is alphabetical or seeded-random per session, never Institute-first (Appendix N §9.6). |
| No effect | Training purchases never affect empanelment, grade, allocation or directory (NN-28). |
| Money | Default: **no referral fee** to Equator (`academy.institute_referral_fee` OFF). If the Board enables one, it is a related-party transaction: arm's-length terms, Board approval under Companies Act 2013 s.188 read with Companies (Meetings of Board and its Powers) Rules 2014 r.15 (shareholder approval where its thresholds apply), prior Audit Committee approval under s.177(4)(iv) only if ERSPL is required to constitute an Audit Committee (a private company ordinarily is not), and the interested director's s.184 disclosure, disclosed on the referral card and in the related-party register **[VERIFY — open: whether the Institute is a "related party" under s.2(76) once its operating entity is confirmed]**. |
| Data | No learner data flows from the Institute to Equator's case systems; referral attribution is aggregate (NN-16). |

---

## 3. Benefit explanations and plan-comparison page content

### 3.1 Page architecture (P13; S9 §2.2)

| Route | Audience | Structure | Price display |
|---|---|---|---|
| `/fees` (SCR-P13-06) | Parties and counsel | "What kind of dispute is it?" (6 tiles) → calculator pre-filtered (SCR-P05-01) → **"Free options first"** card (NN-20) → card tables with "Included / Not included" → one-time products → concessions link → refunds summary → schedule version + approval badge | **Total incl. GST first**, breakup beneath (§6.4) |
| `/pricing/organisations` (SCR-P13-20, new) | Lenders, insurers, employers, listed companies, universities, developers | Segment selector → 3–4 plan cards → comparison table → calculators (NBFC cost comparison, POSH plan finder) → "Talk to us" form routed by volume band | "₹X / month + GST" |
| `/pricing/professionals` (SCR-P13-21, new) | Neutrals, counsel, members, Forum | Three columns: Neutral (Panel · Lite · Solo · Pro · Institution) · Counsel (Free · Pro · Firm) · Membership (Associate · Member · Fellow) + Users' Forum; "What is always free" box | Individuals without GSTIN: total incl. GST first; toggle "I have a GSTIN" shows ex-GST |
| `/pricing/business-assure` (SCR-P13-22, new) | MSMEs and businesses | Three cards + credit explainer + worked example | "+ GST"; incl.-GST total beneath |

Plan card anatomy (top → bottom): tier name + "Best for …" · price (rules in §6.4) · 3–5 numbered entitlements · overage line · one primary CTA (verb + object) · end-of-trial / renewal line ("We won't charge you unless you choose a plan"). Comparison table: sticky header on desktop; stacked cards with a segmented control on mobile (no horizontal scroll); collapsible groups (Case handling · Clocks and compliance · Reporting · Integrations · Security · Support); values in words, never colour or ticks alone (WCAG 2.2 SC 1.4.1); "Show differences only" toggle; statutory rows appear in every tier; one highlighted plan labelled "Recommended for {segment}" (never "Most popular" unless a Claims Register entry proves it).

### 3.2 Copy deck (en; Hindi via legal-translator review, NN-23)

| Plan | Headline | One-liner | Benefits (3–5) | FAQ |
|---|---|---|---|---|
| Pay per case | Our fees, in full, before you start. | You pay for the stage you reach — nothing hidden. | 1) Total with GST shown before you pay · 2) Pay by UPI, card or netbanking · 3) Ask for a fee waiver if you can't afford it · 4) Refunds follow a published table | *Do I pay if the other side never replies?* You get back the fees the refund table shows for that stage. · *Is there a cheaper public option?* Sometimes, yes. We show it first. |
| Explorer human review | Have a person check your options report. | A case manager checks your forum, dates and documents. | 1) Written note in 2 working days · 2) Checks dates you must not miss · 3) Free if you qualify for a concession · 4) Credited if you file within 30 days | *Will you tell me if I'll win?* No. Nobody at Equator gives that view; an advocate can advise you. · *What if the note is late?* We refund you automatically. |
| AI Pleadings Studio | Turn your documents into a clear filing. | Free for both sides, on the same terms. | 1) Every sentence linked to your document · 2) Gaps shown, never filled · 3) Court-format A4 output · 4) You approve every section | *Can the other side buy a better version?* No. There is one version and it is free for everyone. · *Will Equator staff write it for me?* No. You are the author. |
| Certified copies, type copies, translations, transcripts | Documents ready for court and for record. | Originals stay untouched; copies are clearly labelled. | 1) First certified copy free · 2) Verified type copies from ₹40 a page · 3) Translations labelled "for convenience" or "certified" · 4) Arbitration transcripts only with everyone's consent | *Is an AI translation enough for court?* Usually not. Order a certified translation. |
| Counsel Free | Free for every case you appear in. | Your access to a matter never depends on a plan. | 1) File and respond for clients · 2) Hearings, documents and messages · 3) Same drafting tools as your client | *Do I need Counsel Pro to appear?* No. |
| Counsel Pro | All your Equator matters in one place. | Practice tools for advocates — never a procedural advantage. | 1) Cross-client dashboard · 2) Team seats and assignment · 3) Calendar sync · 4) Client update links · 5) Firm precedents in the clause builder | *Does Pro get my hearings scheduled sooner?* No. Scheduling is the same for everyone. · *Can I cancel any time?* Yes, in three steps. |
| Business Assure | Fair clauses in your contracts. Credits for the disputes that still happen. | An annual plan for businesses that sign many contracts. | 1) Model dispute clauses with QR-sealed registration · 2) Pre-paid case credits for Equator fees · 3) Explorer reviews and process consultations included · 4) One dashboard for contracts and disputes | *Do credits pay the mediator?* No. Neutral fees are paid separately and are never discounted. · *Does the other side know I have this plan?* Yes. We tell them, and that it gives you no priority. · *Do unused credits roll over?* For 90 days after your plan ends. |
| Enterprise ODR (lender/insurer/employer) | Fair to your customers. Defensible to your regulator. | Volume pricing for independent dispute resolution — your customers pay nothing. | 1) Stage pricing by claim band · 2) Volume tiers with quarterly true-up · 3) Independence Evidence Pack on every case · 4) Monthly invoice per GSTIN | *Can we choose the arbitrator?* No. Equator appoints independently. That is what makes outcomes defensible. · *What if our volume falls?* Your tier changes only after two quarters and 30 days' notice. |
| GRM SaaS | Answer every grievance inside the regulator's clock. | Grievance desks for lenders, listed companies, employers and universities. | 1) Regulator-mapped clocks in every plan · 2) Escalation to independent ODR in one click · 3) Regulator MIS exports · 4) Intake never stops when you exceed your allowance | *What happens above the ticket allowance?* Tickets keep coming in; overage is billed monthly. |
| POSH SaaS | Run your Internal Committee lawfully and on time. | Sealed inquiry workspace with the 90-day clock. | 1) IC constitution and sealed records · 2) 90-day inquiry clock · 3) Annual-report generator · 4) External members on request | *Does the complainant pay?* Never. |
| API and white-label | Add Equator to your product. | APIs, webhooks and clause insertion, with a sandbox to start. | 1) Free sandbox · 2) Case and clause APIs · 3) Branded party portal (Growth and above) · 4) SLA credits (Scale) | *Can we brand the institution as ours?* No. Your brand sits beside Equator's; the institution and its appointments stay Equator's. |
| Panel (neutrals) | Everything you need for Equator cases — free. | The institution never charges its neutrals to do its work. | 1) Hearings, drafting and e-sign · 2) Earnings and tax documents · 3) CPD record | *Will a paid plan get me more cases?* No. Allocation never reads plans or payments. |
| Chambers Lite | Start a private practice for ₹699 a month. | Two private matters a month in your own workspace. | 1) Own-brand workspace · 2) Fee notes with GST · 3) Client intake link · 4) 14-day trial, no card | *What happens after the trial?* Nothing, unless you choose a plan. |
| Chambers Solo / Pro / Institution | Practise ADR, independently. | Case, hearing, payment and e-sign tools for your own centre. | 1) Your rules and fee schedule (Pro+) · 2) Your panel and allocation (Pro+) · 3) SSO, committees, public directory (Institution) · 4) Parties' cases continue even if your plan lapses | *Can we call our centre a "court"?* No. Names suggesting a court, tribunal or government body are not allowed. |
| Membership | Learn, connect and keep your CPD on record. | A professional community — separate from the panel. | 1) CPD log · 2) Events and resources · 3) Mentoring and observation (Member+) · 4) Fellows' forum (Fellow) | *Does membership help me get on the panel or get cases?* No. Empanelment and allocation are merit-based and never read membership. |
| Users' Forum | Help shape Equator's rules. | A published forum for organisations that use ADR. | 1) Rules-consultation seat · 2) Event seats · 3) Quarterly statistics briefing | *Do members get any case advantage?* None, and the member list is public. |

Prohibited in all plan copy (copy linter `pricing-copy`): "guaranteed", "win", "best/top" without Claims Register evidence, "priority" except "faster administrative handling" where literally true and never on party-facing plans, "limited time", "only N left" unless bound to a ledger count, "free" for any line that is not ₹0, "court", "decree" (Equator), "MCI-registered", "s.27 enforceable" while NN-05 flag is OFF.

---

## 4. Entitlements and metering model

### 4.1 Model

`plan` → many `plan_entitlements` (feature flag keys with value: boolean, limit, or tier) → `subscription` snapshot (`entitlement_snapshot` jsonb pinned at activation and at each change, NN-21) → runtime evaluator `EntitlementService.check(tenant, subject, feature_key, case_scope)` returning `allow | deny(reason) | allow_with_overage(price)`. Evaluator rules: (1) `always_on` keys return allow regardless of billing state; (2) in `case_scope = 'administered'`, keys without `parity_safe = true` return deny (RA-3); (3) `suspended_soft` returns deny for keys tagged `new_work` and allow for `existing_work`; (4) result cached 60 s; deny reasons map to problem codes (§8.5).

### 4.2 Entitlement matrix (feature-flag keys)

`A` = always on (never billed, never blocked) · `✓` included · number = limit per period · `—` not included.

| Key | Party (per case) | Counsel Free | Counsel Pro | Biz Assure S/G/P | Panel | CH-LITE | CH-SOLO | CH-PRO | CH-INST | GRM S/M/L | EAPI St/Gr/Sc |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `clocks.statutory` | A | A | A | A | A | A | A | A | A | A | A |
| `signposting.directory` | A | A | A | A | A | A | A | A | A | A | A |
| `case.records.read` / `case.records.export` | A | A | A | A | A | A | A | A | A | A | A |
| `pleadings.studio` (fair use §4.4) | A | A | A | A | — | — | — | — | — | — | — |
| `counsel.multi_matter_dashboard` | — | — | ✓ | — | — | — | — | — | — | — | — |
| `counsel.calendar_sync` | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| `clause.registry.instruments` | — | — | — | 10/50/250 per yr | — | — | — | ✓ | ✓ | — | add-on |
| `credits.case` | — | — | — | ₹6,000/₹18,000/₹40,000 | — | — | — | — | — | — | — |
| `explorer.human_review` | paid/concession | — | — | 2/5/12 per yr | — | — | — | — | — | — | — |
| `chambers.private_matters` | — | — | — | — | — | 2/mo | 5/mo | 25/mo | 100/mo | — | — |
| `chambers.custom_domain` | — | — | — | — | — | — | — | ✓ | ✓ | — | — |
| `chambers.own_rules` / `own_fee_schedule` | — | — | — | — | — | — | — | ✓ | ✓ | — | — |
| `chambers.own_panel_allocation` | — | — | — | — | — | — | — | ✓ | ✓ | — | — |
| `chambers.sso` / `api_keys` / `committees` | — | — | — | — | — | — | — | — | ✓ | — | — |
| `grm.tickets` | — | — | — | — | — | — | — | — | — | 500/2,500/10,000 (lender) | — |
| `grm.intake` | — | — | — | — | — | — | — | — | — | A | — |
| `api.calls` | — | — | — | — | — | — | — | — | ✓ | — | 2.5 lakh/10 lakh/50 lakh |
| `api.white_label_portal` | — | — | — | — | — | — | — | — | — | — | —/✓/✓ |
| `seats` | — | 1 | per seat | 2/5/15 | 1 | 1 | 1–2 | ≥ 3 | ≥ 10 | per plan | per plan |
| `storage.gb` | case | case | 50 | 25/50/100 | case | 50 | 100/seat | 100/seat | 100/seat | 200 | 500 |

POSH keys (`posh.ic_workspaces`, `posh.locations`, `posh.employees_covered`, `posh.inquiry.open_access` = A) follow Card WRK-POSH; INS-SUB keys (`ins.matters_included`, `ins.batched_days`) follow Card INS-SUB; membership keys (`membership.cpd_log`, `membership.observation_slots`, `membership.fellows_forum`) follow §2.9.

### 4.3 Usage meters

| Meter code | Unit | Reset | Plans | Alerts (in-app + email to billing contacts) | At limit |
|---|---|---|---|---|---|
| `M_PRIVATE_MATTERS` | new private matter opened | calendar month (IST) | CH-* | 80%, 100% | Soft: per-matter overage at plan rate with confirmation dialog; or upgrade |
| `M_GRM_TICKETS` | ticket created | calendar month | GRM-* | 80%, 100%, 150% | **Never blocks intake**; overage billed in arrears |
| `M_API_CALLS` | billable API call (excl. webhooks, health) | calendar month | EAPI-* | 80%, 100% | Overage per 1,000; hard rate limits are technical, not billing |
| `M_CASES_PROGRAMME` | case reaching each stage (FIN-L L1–L7, WRK, INS) | contract year | Enterprise | committed-use forecast monthly | Rated per stage; tier per §2.4.3 |
| `M_INS_MATTERS` | matter accepted | subscription year | INS-SUB | 80%, 100% | Per-case overage |
| `M_SEATS` | active seat | point-in-time | All seat plans | at plan minimum | Adding seats prorates (FR-P05-36) |
| `M_VIDEO_MIN` | participant-minute | month | CH-* | 80%, 100% | ₹1.50/participant-minute; **never cuts a live hearing** |
| `M_STORAGE_GB` | GB-month | month | CH-*, Counsel Pro, Biz | 80%, 100% | Uploads continue for case records (A); ₹500/100 GB/month |
| `M_CLAUSE_INSTRUMENTS` | registered instrument | plan year | Biz, Registry add-on | 80%, 100% | Upgrade or ₹30/instrument **[Board]** |
| `M_CREDITS` | ₹ of credit value consumed | plan term + 90 days | Biz | 50%, 80%, T-60/T-30 to lapse | Pay-per-case after exhaustion |
| `M_EXPLORER_REVIEWS` | review used | plan year | Biz | at 0 remaining | Paid per review |
| `M_POSH_EMPLOYEES` | declared employees | annual attestation | POSH-* | at band edge | Re-band at renewal |
| `M_STUDIO_PAGES` | source pages ingested; AI type-copy pages; translation pages; draft runs | per party per case | All parties | 80% to user and case manager | Case manager may raise for all parties equally (§2.1.9) |

Meter events are append-only rows in `core.usage_events` (idempotent on `event_id`), aggregated hourly into `core.usage_aggregates`; the Usage page (§5.7) reads aggregates with a "last updated" time.

### 4.4 Fair-use policy — AI Pleadings Studio (identical for every party in a case)

| Resource | Fair-use cap per party per case | Basis |
|---|---|---|
| Source pages ingested (OCR/extraction) | 1,000 | Appendix M ingestion |
| AI type-copy pages | 300 | Appendix L §6 |
| Convenience translation pages (individuals) | 100 | §2.1.6 |
| Draft generation runs per document type | 30 section-runs | AI Gateway cost meter |
| Documents | SoC/response/counterclaim/rejoinder/list of dates/synopsis/index/affidavit — 1 active draft each + versions | NN-25 |

Caps are configuration (`studio.fair_use.*`), shown on the Studio header as "You have used X of Y". Raising a cap is a case-level action by the case manager (reason required) that applies to every party; no party can buy more.

### 4.5 Overage rating

Overage = `max(0, usage − included) × overage_rate`, rated at period close by `UsageRatingJob`, invoiced with the next cycle (subscriptions) or the monthly usage invoice (enterprise). Mid-cycle upgrades re-baseline included quantities pro rata (`included × remaining_days / cycle_days`). Overage lines are separate invoice lines with meter code and period; disputes go through the Refund/billing-query flow (§5.13).

---

## 5. Billing and settings pages (screen specifications)

### 5.0 Shell, visibility and common rules

Billing lives in the `/settings` shell (Appendix S §7; left rail on web, list screen on mobile). Section label: **"Billing"** for buyers of plans (enterprise, chambers, counsel-pro, Business Assure, members, Forum) and **"Payments and receipts"** for individual parties, who buy per case, never plans. Neutrals see **"Payouts and tax"**.

| Page | Screen ID | Route | Party | Neutral | Counsel / Member / Biz / Chambers | Enterprise / GRM / POSH admin | Mobile |
|---|---|---|---|---|---|---|---|
| Billing overview | SCR-P05-19 | `/settings/billing` | — (see SCR-P05-34) | — | ✓ | ✓ | ✓ |
| Plan and membership | SCR-P05-20 | `/settings/billing/plan` | — | Panel/Lite upgrade path | ✓ | read-only contract summary | ✓ |
| Change plan | SCR-P05-21 | `/settings/billing/plan/change` | — | ✓ (Lite/Solo) | ✓ | "Request change" only | ✓ |
| Payment methods | SCR-P05-22 | `/settings/billing/payment-methods` | ✓ (in SCR-P05-34) | — | ✓ | ✓ | ✓ |
| Invoices and credit notes | SCR-P05-23 | `/settings/billing/invoices` | ✓ (in SCR-P05-34) | panel-fee invoices | ✓ | ✓ | ✓ (download) |
| Tax details | SCR-P05-24 | `/settings/billing/tax` | optional GSTIN | via SCR-P05-32 | ✓ | ✓ multi-GSTIN | ✓ |
| Usage and meters | SCR-P05-25 | `/settings/billing/usage` | — | — | ✓ | ✓ | ✓ (read) |
| Wallet and credits | SCR-P05-26 | `/settings/billing/wallet` | — | — | Biz | ✓ | ✓ (read) |
| Mandates and auto-pay | SCR-P05-27 | `/settings/billing/mandates` | case instalment mandates shown read-only | — | ✓ | ✓ | ✓ |
| Billing contacts | SCR-P05-28 | `/settings/billing/contacts` | — | — | ✓ | ✓ | web |
| Membership details and renewal | SCR-P05-29 | `/settings/membership` | — | ✓ if member | ✓ | Forum | ✓ |
| Cancel plan | SCR-P05-30 | `/settings/billing/cancel` | — | ✓ | ✓ | non-renewal notice | ✓ |
| Refunds and billing queries | SCR-P05-31 | `/settings/billing/refunds` | ✓ | — | ✓ | ✓ | ✓ |
| Payouts and tax (neutral) | SCR-P05-32 | `/settings/payouts` | — | ✓ | Chambers tenant payouts | — | ✓ |
| Enterprise contract | SCR-P05-33 | `/settings/billing/contract` | — | — | — | ✓ | read-only |
| Payments and receipts (party) | SCR-P05-34 | `/settings/payments` | ✓ | — | — | — | ✓ |
| Concessions (party) | SCR-P05-05 (existing) | `/cases/[caseId]/billing/concession` | ✓ | — | non-profit/education discount request | — | ✓ |

Common rules for every page:

1. **Permissions** (policy engine, master §4.1): `billing.view` (read all billing pages of the tenant), `billing.manage` (change plan, payment methods, contacts, tax), `billing.cancel` (cancel/non-renew), `billing.refund.request`; individuals hold all four for their own account. Step-up (aal2 within 5 minutes) for: change plan, cancel, add/remove payment method, mandate cancel, payout account change, GSTIN change, wallet withdrawal. Enterprise changes above ₹2,00,000 annual value need maker–checker inside the tenant if it has ≥ 2 billing admins.
2. **Money display:** Indian grouping, ₹ symbol with ISO code on foreign currencies (P05 §6); amounts read in words to screen readers; never colour alone.
3. **States:** empty, loading (Skeleton), error (problem `code` + `traceId`), success, read-only (insufficient permission: "Ask your billing admin — {names}"), `past_due` banner (§7), `suspended_soft` banner.
4. **No upsell** inside case, hearing, signing or sealed views (X-15); upgrade prompts live only here and on pricing pages, max one prompt per user per 7 days (DP-10).
5. **Audit** (NN-22): every write emits an `equator.billing.*.v1` event (§8.4) and a hash-chained audit event.
6. **Languages:** en + hi at launch; legal billing text (refund policy, mandate notice) from versioned templates with legal review.

### 5.1 Billing overview — SCR-P05-19

Purpose: one glance at what you pay, what's next and anything needing action.

| Block | Content | Source |
|---|---|---|
| Action needed (top; only if any) | Failed payment, expiring card token (≤ 30 days), mandate needing AFA, GSTIN mismatch on invoice, credits lapsing ≤ 30 days, TDS certificate missing for a quarter | billing alerts |
| Current plan(s) | Card per product line: plan name, price (§6.4 display), billing interval, status chip (`trialing`, `active`, `past_due`, `suspended_soft`, `cancelling — ends {date}`), renewal date, auto-renew state (text "Auto-renew is off — your plan ends on 31 Oct 2027"), seats used/included | `core.subscriptions` |
| Next charge | Date, amount incl. GST, instrument (masked: "UPI AutoPay — rahul@okaxis, max ₹20,000"), "Your bank will notify you at least 24 hours before" | `core.subscriptions`, `core.mandates` |
| Usage snapshot | Top 3 meters with bars and numbers ("18 of 25 private matters this month") | `core.usage_aggregates` |
| Wallet / credits | Balance and lapse date (Biz, enterprise) | `core.credit_ledger`, `core.wallet_ledger` |
| Recent invoices | Last 3 with status and download | `core.invoices` |
| Quick links | Change plan · Payment methods · Invoices · Tax details · Cancel plan (same weight as Change plan — DP-05) | — |

Actions: none mutate on this page. Mobile: same blocks stacked; "Action needed" pinned.

### 5.2 Plan and membership — SCR-P05-20

| Field | Type | Notes |
|---|---|---|
| `plan_name`, `plan_code`, `version` | text | Pinned price version and its approval badge ("Subject to Board approval" until `board_approval_ref`) |
| `price_display` | money | §6.4 |
| `billing_interval` | enum `monthly` \| `annual` | — |
| `term_start`, `term_end`, `renewal_date` | date | — |
| `auto_renew` | toggle | Default per §2 common terms; switching ON requires an active mandate or saved instrument and shows: "We will charge ₹{total incl. GST} on {date}. Your bank will notify you at least 24 hours before. You can switch this off any time before then." Switching OFF is one click + confirmation, no retention screen |
| `entitlements` | list | Each key from §4.2 in words with numbers |
| `trial_end` | date | "Your trial ends on {date}. We won't charge you unless you choose a plan." |
| `pause` | action | Chambers only: up to 3 months per year **[Board]**; paused = no new matters, existing matters continue (P10 FR-P10-04) |

Actions: Change plan (→ SCR-P05-21) · Turn auto-renew on/off · Pause (Chambers) · Cancel plan (→ SCR-P05-30). Enterprise: read-only summary + "Request a change" (creates a ticket to the account manager; no self-serve change of contracted plans).

### 5.3 Change plan with proration preview — SCR-P05-21

Steps: (1) choose plan / seats / interval → (2) **preview** → (3) confirm (step-up) → confirmation page (reference number, email, audit).

Preview panel (computed by `GET /v1/subscriptions/{id}/change-preview`, deterministic engine; never AI):

| Row | Formula / content |
|---|---|
| Today's charge (upgrade, seat add, interval monthly → annual) | `price_delta × remaining_days / cycle_days` in IST calendar days inclusive of the change day (FR-P05-36), rounded per App. B §B.3.4; GST shown separately and total (e.g., App. B WE-12: 2 seats × ₹2,999 × 20/30 = ₹3,999 + GST ₹719.82 = ₹4,718.82) |
| Downgrade | "Takes effect on {next renewal}. No charge today. No refund for the current period." |
| Next renewal amount | New price × quantity, incl. GST |
| Entitlements gained / lost | Diff of §4.2 keys with dates ("You will lose 2 seats on 1 Dec 2026 — choose which members lose access") |
| Usage conflict | If current usage exceeds the new plan's limits (e.g., 30 private matters this month on downgrade to Solo): existing matters continue; new matters billed per-matter until the cycle ends |
| Mandate check | If the new per-debit amount > mandate `max_amount` → "Your mandate allows up to ₹{max}. You'll be asked to approve a new mandate." If > ₹15,000 → "Your bank will ask you to approve this payment (additional authentication)" (RBI E-mandate Framework 2026) |
| Annual switch | Shows saving as computed (`2 × monthly`), no urgency copy |

Field list:

| field_id | Label | Type | Required | Options / validation |
|---|---|---|---|---|
| `target_plan_code` | Plan | radio cards | Y | Plans of the same product line visible to the subject's segment |
| `seats` | Number of seats | stepper | Y for seat plans | ≥ plan minimum; ≤ 500 self-serve |
| `interval` | Billing | segmented | Y | Monthly · Yearly (equal visual weight — DP-06) |
| `seat_removals` | Who loses access | multiselect | Y if seats decrease | Members list; admin seat cannot be removed |
| `po_number` | PO number (optional) | text | N | ≤ 40 chars; printed on invoice |
| `confirm` | "I agree to pay ₹{today} today and ₹{renewal} on {date}" | checkbox (unticked) | Y | Explicit affirmative action (E-Commerce Rules 2020 r.4(9)) |

Errors: `PLAN_NOT_AVAILABLE`, `SEAT_MINIMUM`, `MANDATE_LIMIT_EXCEEDED` (offers new mandate), `PRORATION_PREVIEW_STALE` (> 10 minutes old → re-preview), `STEP_UP_REQUIRED`. Event: `equator.billing.subscription.changed.v1`.

### 5.4 Payment methods — SCR-P05-22 (NN-31)

All instruments are created in the provider's hosted/standard checkout (Razorpay Standard Checkout / hosted mandate pages); Equator stores only provider tokens and display metadata (PCI DSS v4.0.1 SAQ A; Appendix Q §4). No card number, CVV or UPI PIN field exists in any Equator UI or API.

| Column | Content |
|---|---|
| Type | Card (tokenised under RBI CoFT, effective 1 Oct 2022) · UPI ID (for one-time collect/intent) · UPI AutoPay mandate · eNACH mandate · Netbanking (one-time) · Bank transfer to virtual account (enterprise) |
| Display | Card network + last 4 + expiry month/year; UPI handle masked (`ra***@okaxis`); bank name + last 4 of account for eNACH |
| Default for | Subscriptions · Case payments · Wallet top-up |
| Status | active · expiring (≤ 30 days) · expired · revoked by customer · failed verification |
| Actions | Set default · Remove (step-up; blocked with `INSTRUMENT_IN_USE_BY_MANDATE` if a live mandate depends on it — link to Mandates) · Add new (opens provider checkout in a modal/redirect) |

Field rules: `provider_token_ref` (opaque), `display_last4` (4 digits), `network`, `expiry_mm_yy`, `instrument_kind`; CI test `NN-31_no_pan_fields` greps DTOs, DB schema and logs for PAN/CVV patterns. International cards: via Razorpay International (INT only), same token-only rule.

### 5.5 Invoices and credit notes — SCR-P05-23

List (filters: period, type, status, GSTIN, product line; search by number):

| Column | Content |
|---|---|
| Document | Tax invoice · Bill of supply (exempt lines, e.g., arbitral tribunal T10) · Receipt voucher (advance, CGST Rules r.50) · Refund voucher (r.51) · Credit note / Debit note (CGST s.34; r.53) · Fee note in a neutral's name (where `neutral_direct`) · Payment receipt |
| Number | Gapless series per FY per GSTIN (`core.document_series`) |
| Date, period | Issue date; service period for subscriptions/usage |
| Supplier GSTIN / Recipient GSTIN | Equator legal entity GSTIN; buyer GSTIN or "Unregistered" |
| Place of supply | State name + code (IGST Act s.12(2)) |
| Taxable value, CGST, SGST, IGST, total | Per §B.4 treatment; RCM lines flagged "Tax payable on reverse charge: Yes" |
| IRN / e-invoice | IRN, ack number and signed QR where `einvoice_applicable` (AATO > ₹5 crore, Notification 10/2023-CT; 30-day IRP window for AATO ≥ ₹10 crore); status `irn_pending` blocks B2B PDF release (P05 §8) |
| Status | issued · paid · partially paid · overdue · cancelled (IRN within 24 h) · credited |
| Actions | Download PDF (A4, bilingual header option) · Download XML/JSON (e-invoice) · Email to billing contacts · Raise a query (→ SCR-P05-31) · View usage annexure (enterprise; masked identifiers only) |

Rules: invoices show the legal entity particulars from `tenant.legal_entity` (master X-15); B2C invoices carry recipient name, address and state where CGST Rules r.46 requires; GSTIN correction after issue → credit note + re-issue (never edit), blocked after the s.34(2) cut-off (`CREDIT_NOTE_PERIOD_CLOSED`). Bulk download (zip, ≤ 12 months) for enterprise.

### 5.6 Tax details — SCR-P05-24

| field_id | Label | Type | Required | Options / validation | Help text |
|---|---|---|---|---|---|
| `buyer_kind` | Who is paying? | radio | Y | Individual · Business or organisation | "This decides what your invoice shows." |
| `gstin` | GSTIN | text | N (Y for B2B invoices) | 15 chars `^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$` + checksum; verified via `KYC_PORT` GSTIN lookup; status must be Active | "Add it to claim input tax credit." |
| `legal_name` | Legal name | text | Y if GSTIN | Auto-filled from GSTIN lookup; read-only after verification | — |
| `trade_name` | Trade name | text | N | — | — |
| `pan` | PAN | text | Y for business; N for individuals | `^[A-Z]{5}[0-9]{4}[A-Z]$`; must match GSTIN chars 3–12 when both given | Masked display `ABCDE****F` |
| `billing_address` | Billing address | address block | Y | PIN lookup; state auto-derived | — |
| `place_of_supply_state` | State for GST | select | Y | 38 state/UT codes (GST state code list incl. 97 Other Territory) | Derived from address; editable only with reason |
| `additional_gstins[]` | Other GSTINs (enterprise) | repeater | N | Each with address, state, cost centre tag, default product lines | "Invoices are raised per GSTIN." |
| `po_required` | We need a PO number on invoices | toggle | N | — | — |
| `sez_unit` | SEZ unit/developer | toggle + LoA upload | N | If ON: LUT on file required for zero-rating (T07) | — |
| `foreign_recipient` | Billing entity outside India | toggle | N | Country, tax ID (free text), currency; zero-rated export under LUT (T05) if conditions met | — |
| `lut_reference` | (Equator) LUT ARN and FY | read-only | — | Shown for export invoices: "Supply meant for export under LUT without payment of IGST" | — |
| `tds_deductor` | We deduct TDS on payments to Equator | toggle | N | If ON: `tan` (`^[A-Z]{4}[0-9]{5}[A-Z]$`), section code (default s.393(1) Table Sl. 6(iii)), rate | "Upload certificates each quarter so we can match them." |
| `tds_certificates[]` | TDS certificates | upload repeater | N | PDF ≤ 5 MB; quarter, FY, amount, section; matched to Form 26AS/AIS import (FR-P05-54) — status `matched` / `mismatch` / `pending` | Certificate form: Form 16A (1961 Act) or the corresponding form under the Income-tax Rules 2026 **[VERIFY — open: form number]** |
| `govt_entity` | Government department / notified entity (GST-TDS) | toggle | N | If ON: GST-TDS 2% under CGST s.51 tracked (T17) | — |
| `e_invoice_contact_email` | Email for e-invoice copies | email | N | — | — |

Changes to GSTIN or state apply to **future** invoices only; the page shows "Past invoices stay as issued. Ask for a correction if one is wrong." Events: `equator.billing.tax_profile.updated.v1`.

### 5.7 Usage and meters — SCR-P05-25

| Element | Content |
|---|---|
| Meter cards | One per §4.3 meter applicable to the plan: used / included, % bar with text, period, reset date, overage rate, projected end-of-period usage (linear; labelled "estimate") |
| Alerts settings | Per meter: thresholds (default 80/100; editable 50–100 in steps of 10), recipients (billing contacts), channels (email, in-app; SMS only service template) |
| Breakdown | Table by day/week/month; for enterprise by stage, product, branch/cost centre; masked case references only |
| Export | CSV (enterprise annexure format FR-P05-38) |
| Commitment strip (enterprise) | Committed vs actual run-rate vs tier thresholds; next true-up date; forecast tier (§2.4.3) |
| Fair-use (parties) | Not shown here — shown in the Studio header (§4.4) |
| Freshness | "Updated {hh:mm} IST" (hourly aggregate) |

### 5.8 Wallet and prepaid credits — SCR-P05-26

Two ledgers, shown separately: **Wallet** (enterprise prepaid money, FR-P05-39) and **Credits** (Business Assure entitlement value).

| Element | Wallet | Credits |
|---|---|---|
| Balance | ₹ balance by currency; "held for pending invoices" amount | ₹ credit value remaining; lapse date (term end + 90 days) |
| Ledger | Append-only rows: top-up, receipt voucher no., consumption (invoice ref), refund, adjustment | Grant, redemption (case no. masked, line code), lapse, reversal |
| Top-up | Amount (₹10,000–₹1,00,00,000), method (VA/NEFT details, mandate, PG); receipt voucher issued (T16) | Not available (credits come only with a plan) |
| Auto top-up | Toggle; threshold and amount; requires mandate; pre-debit notice applies | — |
| Redeemable on | "Equator fees only — not neutral fees, stamp duty, government or bank charges" (O-R6) | Same |
| Withdraw / refund | On termination net of dues (FR-P05-39), step-up, to original instrument or verified account in the customer's name | Not refundable except RP-SUB termination cases |
| Alerts | Low balance 20% and 10% of trailing 30-day consumption | 50%, 80% used; T-60 and T-30 before lapse |

Error: `WALLET_LINE_NOT_REDEEMABLE` when a redemption targets a non-Equator line.

### 5.9 Mandates and auto-pay — SCR-P05-27 (RBI E-mandate Framework 2026)

| Column / element | Content |
|---|---|
| Mandate list | Merchant name as shown to the bank ("Equator Resolution Service Pvt Ltd"), descriptor (plan name), type (UPI AutoPay · card e-mandate · eNACH), maximum amount per debit, frequency (monthly · yearly · as presented), start and end (validity), created date, status (`active`, `paused`, `cancelled_by_customer`, `cancelled_by_merchant`, `expired`, `failed_registration`), linked subscriptions |
| AFA notice | "Payments above ₹15,000 need your approval each time (additional authentication)." Shown on every mandate with max > ₹15,000 |
| Pre-debit notice | "Your bank will notify you at least 24 hours before each debit with the amount, date and reason. You can stop that single debit from your bank or UPI app." |
| No fee | "Setting up or using a mandate is free." (`EMANDATE_no_fee` test) |
| Create | Opens provider mandate flow (AFA at registration by the customer's bank/PSP); Equator never collects UPI PIN or card data. UPI AutoPay `max_amount` default = plan annual price + 20% headroom, capped by `mandate_limits.upi_autopay_max_debit` (₹99,999 general categories; S9 §3.4) — above that, eNACH is offered |
| Modify max amount | Through provider flow (AFA) |
| Cancel mandate | Button on each row → confirmation ("Cancelling stops all future auto-debits for {linked plans}. Your plan stays active until {end}; you can pay manually.") → Equator calls PSP cancel-mandate API and records `cancelled_by_customer`; also shows "You can also cancel from your UPI app or bank" |
| Debit history | Per mandate: pre-debit notice sent (time, channel), debit attempt, result, retry (retries only within the mandate, never by card-on-file outside it) |

Events: `equator.payments.mandate.registered.v1`, `.cancelled.v1`, `.debit_notified.v1`, `.debit_failed.v1`.

### 5.10 Billing contacts — SCR-P05-28

| field_id | Label | Type | Required | Validation |
|---|---|---|---|---|
| `contacts[]` | Billing contact | repeater (max 5; enterprise max 5 per GSTIN) | ≥ 1 | — |
| `contacts[].name` | Name | text | Y | ≤ 80 chars |
| `contacts[].email` | Email | email | Y | Verified by link before activation |
| `contacts[].mobile` | Mobile | phone | N | E.164; OTP-verified; SMS only for service templates (TCCCPR 2018) |
| `contacts[].roles` | Receives | multiselect | Y | Invoices · Payment failures · Renewal reminders · Usage alerts · TDS reminders · Contract notices |
| `contacts[].gstin_scope` | For GSTIN | select | N | Enterprise only |
| `escalation_contact` | Escalation contact | contact | N (enterprise Y) | — |

Billing emails are service communications; promotional upgrade messages require separate marketing consent (DPDP Act 2023; NN-16).

### 5.11 Membership details and renewal — SCR-P05-29

| Element | Content |
|---|---|
| Card | Grade (Associate/Member/Fellow) or Forum tier; membership number; valid from/to; status (`active`, `grace`, `lapsed`); post-nominal permission (only when flag ON) |
| Benefits used | Entitlement meters stated as numbers (events booked, observation slots used, CPD hours logged) — S9 C-27 |
| Grade progress | Requirements checklist for the next grade (e.g., Fellow: matters ≥ 25 — self-declared with evidence; peer review status). Text: "Grades are about learning and contribution. They do not affect panel membership or case allocation." |
| Renewal | Auto-renew OFF by default; "Renew for 12 months — ₹{total incl. GST}" button from T-60; reminders T-60/T-30/T-7/T-1; grace 30 days |
| Certificate | Download membership certificate (QR-verifiable) |
| Leave | "End membership" → SCR-P05-30 flow (2 steps) |

### 5.12 Cancellation flow — SCR-P05-30 (no more steps than sign-up; ≤ 3)

| Step | Screen content | Rules |
|---|---|---|
| 1 | Entry point: "Cancel plan" link on Billing overview and Plan pages, same size and weight as "Change plan" | Never hidden behind support, chat, email or phone (DP-05 Subscription Trap) |
| 2 | One page: **What happens** — end date (end of paid term; or immediately for trials), "Your open cases stay open" (Chambers: run-off 90 days, P10 FR-P10-04), data export window (90 days), credits/allowances that lapse (with amounts), refund (if any) computed by policy (cooling-off/RP-SUB) · **Optional reason** (single choice: Too expensive · Not using it enough · Missing feature · Switching provider · Practice closing · Other + free text; skippable) · **At most one retention option**, shown only if genuinely cheaper or better fitting (e.g., "Switch to Lite at ₹699 a month"), styled as a secondary option · Primary button "Cancel my plan" | No guilt or fear wording (DP-03 Confirm Shaming — linter phrases: "lose your cases", "are you sure you want to give up", "risk"); no countdown; no second retention screen |
| 3 | Confirmation page: reference number, end date, export link, mandate cancelled notice ("We have cancelled your bank mandate for this plan") — Equator calls the PSP cancel-mandate API in the same transaction; email + in-app receipt | `NO_SUBSCRIPTION_TRAP` test: steps to cancel ≤ steps to subscribe for the same plan (measured by the e2e harness) |

Undo: "Keep my plan" available until the end date (one click, no fee). Enterprise contracts: "Send non-renewal notice" (≥ 60 days before term end) with PDF acknowledgement; cancellation for convenience mid-term follows the order form.

### 5.13 Refund requests and billing queries — SCR-P05-31

| field_id | Label | Type | Required | Options / validation |
|---|---|---|---|---|
| `subject` | What is this about? | radio | Y | Case fee refund · Subscription refund (cooling-off / termination) · Duplicate or wrong payment · Invoice correction (GSTIN, name, address) · Usage or overage dispute · Other |
| `reference` | Invoice / payment / case | select | Y | User's own documents only (RLS) |
| `computed_amount` | Amount due back under the policy | read-only money | — | From the deterministic refund engine (App. B §B.8; FR-P05-32): stage reached, policy code, line-by-line; pass-throughs "refunded only if the provider refunds" |
| `requested_amount` | Amount you are asking for | money | N | If different from computed → reason required; routes to `fin.approver` |
| `reason` | Tell us more | textarea | conditional | ≤ 1,000 chars |
| `attachments[]` | Supporting documents | upload | N | PDF/JPG/PNG ≤ 10 MB each |
| `refund_to` | Refund goes to | read-only | — | Original instrument (RBI PA Directions 15 Sep 2025); bank transfer only where the original rail was a bank transfer, to a penny-drop-verified account in the payer's name |

Status timeline: `submitted` → `under_review` → `approved` / `partially_approved` / `rejected (reason)` → `initiated` (within 3 working days of approval, FR-P05-33) → `completed` (UTR/ARN shown) with the credit note number (CGST s.34). Expected credit times shown per rail ("UPI: usually within 1–2 working days after we initiate; cards: 5–7 working days" — [K], provider-dependent). Acknowledgement within 48 hours and resolution within one month for consumer queries (E-Commerce Rules 2020 r.4(5); LR-CONS-006).

### 5.14 Payouts and tax (neutral side) — SCR-P05-32 (extends SCR-P05-06/07)

| Tab | Fields and content |
|---|---|
| Payout account | Account holder name (must match PAN name — fuzzy ≥ 0.85 or manual review), account number (masked after save), IFSC (`^[A-Z]{4}0[A-Z0-9]{6}$`), account type; penny-drop/penniless verification (App. S §3.11); change requires step-up and triggers a 24-hour payout hold if a payout follows (FR-P05-56); Route linked-account status (24-hour cooling period) |
| Tax profile | PAN, GSTIN (optional; T11/T12), state, composition flag, residency (resident / non-resident), for non-residents: TRC, Form 41, no-PE/no-fixed-base declaration, DTAA article (App. B §B.10), validity dates with expiry reminders |
| Earnings | By case (case number + mechanism; no party names in list view): fee, hold status, release milestone (App. B §B.7.6), released date, panel administration fee deducted (§B.7.7 — 0% on administered cases), net |
| TDS | By deductor (party/corporate or Equator where principal): section (s.393(1) Table Sl. 6(iii); s.393(2) Sl. 17 for non-residents), amount, quarter, certificate status (received / awaited / mismatch with AIS) and "Ask deductor for certificate" (sends a service message via case manager; never direct party contact outside the case channel) |
| Statements | Monthly statement PDF (gross, panel-fee invoice from Equator with GST, TDS, net), annual earnings summary (FY), downloadable CSV for the neutral's accountant |
| Panel-fee invoices | Equator's monthly tax invoices to the neutral for marketplace/referral take (B.7.7) |
| Fee notes | Fee notes generated in the neutral's name under standing authorisation (`neutral_direct`) — or neutral self-upload where the tax memo requires **[VERIFY — open: P05 §14 item 3]** |

Rule text on the page: "Your earnings never depend on whether a case settles or who wins. Plans and memberships do not affect allocation." (App. B P2; RA-4.)

### 5.15 Enterprise contract — SCR-P05-33

| Block | Content |
|---|---|
| Contract summary | Contract number, legal entity, term, products (EAPI/GRM/INS-SUB/FIN-L/WRK), price table versions (pinned), payment terms (net days), renewal/non-renewal date, account manager |
| Commitment vs usage | Committed volume or spend; actual YTD; run-rate; current tier; forecast tier after next true-up; chart with thresholds (accessible table alternative) |
| True-up history | Each run: date, inputs, result, notice sent, effective date, hash (`core.true_up_runs`) |
| SLA | SLA targets (acknowledgement, scrutiny, notice dispatch, scheduling), monthly attainment, SLA credits earned (EAPI-SCALE) and applied credit notes |
| Independence and disclosure | Fixed text: "Neutrals are appointed independently by Equator. Your contract gives you no choice or veto (NN-03). Your customers are told about this commercial relationship (NN-16)." Link to Independence Evidence Pack samples |
| Authority to settle | Uploaded board resolution / authority letters, signatories, limits, expiry (S9 C-33) — required before L2 conciliation offers |
| Documents | Order form, MSA, DPA, SLA schedule, amendment history (read-only, hashes) |
| Actions | Request change (ticket) · Download contract pack · Send non-renewal notice |

### 5.16 Payments and receipts (individual party) — SCR-P05-34

| Block | Content |
|---|---|
| Across my cases | Per case: paid, due (with due date), refundable, deposits held on account (arbitration), concessions applied (own only, never the counterparty's) — "What this costs so far / what's next" (S9 §5.3) |
| Receipts and invoices | Tax invoice / bill of supply / receipt per payment; download; language switch |
| Saved payment methods | Tokenised card / UPI for future case payments; remove |
| Instalment mandates (settlements) | Read-only list of mandates on the **payee's** rail for settlement instalments (NN-13) with "Manage in your bank/UPI app" — Equator is not the merchant |
| Refunds | Link to SCR-P05-31 |
| Concession | Link to SCR-P05-05 per case |
| Data | "Download my case records" — always available, even if a fee is unpaid (FR-P05-37) |

No plan, upgrade or membership content appears for parties on this page (X-15).

---

## 6. Compliance controls for pricing, billing and subscriptions

### 6.1 Instruments applied (treated as applicable by default; counsel to confirm characterisation — §11)

| Instrument | Key duties used here | Register ID (Appendix G) |
|---|---|---|
| Consumer Protection Act 2019 ss.2(28) (misleading advertisement), 2(47) (unfair trade practice), 18 and 21 (CCPA powers, penalties) | No misleading price or plan claims | existing NN-17 tests; propose LR-CONS-007 |
| Guidelines for Prevention and Regulation of Dark Patterns, 2023 (CCPA, notified 30 Nov 2023, under CPA s.18; Annexure 1 lists 13 patterns); CCPA advisory of 5 Jun 2025 (self-audit within 3 months; self-declaration encouraged) [V-2] | §6.2 lint | propose LR-CONS-008 |
| Consumer Protection (E-Commerce) Rules 2020 (23 Jul 2020) — r.4(4) grievance officer; r.4(5) 48 h acknowledgement, one-month redress; r.4(9) explicit consent, no pre-ticked boxes; r.4 cancellation-charge symmetry and refund within a reasonable period; r.7 (inventory e-commerce entity) total price with breakup of compulsory and voluntary charges, refund/cancellation terms **[VERIFY — open: sub-rule numbers for symmetry, refund and price-breakup duties]** | §6.3 | LR-CONS-006 (existing); propose LR-CONS-009, LR-CONS-010 |
| RBI Digital Payments – E-mandate Framework, 2026 (RBI/DPSS/2026-27/396, CO.DPSS.POLC.No.S56/02.14.003/2026-27, 21 Apr 2026) | AFA at registration/modification/withdrawal; AFA-free ≤ ₹15,000 per debit (₹1 lakh only for insurance premia, MF, credit-card bills); pre-debit notice ≥ 24 h; per-debit or full opt-out; no charge for the facility | LR-PAY-003 (extend scope to subscriptions) |
| RBI card-on-file tokenisation (merchants may not store card data from 1 Oct 2022) [K] | Tokens only (NN-31) | propose LR-PAY-005 |
| RBI (Regulation of Payment Aggregators) Directions 2025 (15 Sep 2025) | Refund to original instrument; settlement sums off Equator's merchant | LR-PAY-001 |
| RBI Master Directions on Prepaid Payment Instruments (27 Aug 2021, as amended) — closed-system PPIs (issued by an entity for its own goods/services, no cash withdrawal) need no RBI authorisation **[VERIFY — open: current consolidated PPI Directions reference]** | Wallets and credits redeemable only for Equator's own supplies (O-R6) | propose LR-PAY-006 |
| CGST Act 2017 ss.13, 31, 34; CGST Rules 2017 rr.46, 48(4), 49, 50, 51, 53; Notification 10/2023-CT (e-invoice > ₹5 crore AATO); GSTN advisory 5 Nov 2024 (30-day IRP window, AATO ≥ ₹10 crore); IGST Act ss.12, 13, 16; CGST Rules r.96A (LUT) | §6.5 | LR-TAX-001…009; propose LR-TAX-011 |
| DPDP Act 2023 + Rules 2025 | Marketing consent separate from billing service messages | NN-15 |
| TRAI TCCCPR 2018 (as amended) | Billing SMS = service templates; upsell SMS = promotional with consent | NN-12 |
| Advocates Act 1961 ss.29, 33; BCI Rules Part VI Ch. II rr.20, 36 | X-01, X-07, X-11 | existing |
| Companies Act 2013 ss.177, 188 | Institute referral arrangements (§2.10) | propose LR-CORP-001 |

### 6.2 The 13 dark patterns → lint and tests (Dark Patterns Guidelines 2023, Annexure 1)

| ID | Pattern | Where it could arise at Equator | Control | Test / lint |
|---|---|---|---|---|
| DP-01 | False Urgency | Promo banners, plan pages, Explorer report | No timers or scarcity on `/fees`, `/pricing/*`, checkout, settings; promo "remaining" count must bind to `promo_redemptions` ledger; deadlines shown are only statutory clocks with sources | `DARK_PATTERN_lint_false_urgency` (CMS + component deny-list) |
| DP-02 | Basket Sneaking | Checkout adds e-sign, express type copy, donation | Cart = user-selected lines + mandatory pass-throughs already disclosed on the quote; no pre-added optional lines | `DARK_PATTERN_basket_snapshot` (quote hash vs cart) |
| DP-03 | Confirm Shaming | Cancel, decline add-on, decline review | Copy linter phrase list (en/hi): "lose your case", "risk", "are you sure you want to give up", "I don't care about…" | `DARK_PATTERN_lint_confirm_shaming` |
| DP-04 | Forced Action | Requiring sign-up or marketing consent to see fees; requiring a subscription to respond to a case | Prices public without login; marketing consent never bundled; RA-2 | `DARK_PATTERN_prices_public`, `NN-16_no_paid_procedural_advantage` |
| DP-05 | Subscription Trap | Cancel only by email/phone; hidden cancel | §5.12 ≤ 3 steps, self-serve; mandate cancelled automatically | `NO_SUBSCRIPTION_TRAP` |
| DP-06 | Interface Interference | Grey "Monthly", tiny "No thanks", hidden "Choose free plan" | Equal visual weight tokens for binary choices; contrast ≥ 4.5:1 on secondary options | `DARK_PATTERN_equal_weight` (visual regression + axe) |
| DP-07 | Bait and Switch | Advertised price unavailable at checkout | Checkout price must equal quote hash or show a re-quote with reason | `DARK_PATTERN_quote_hash_equals_checkout` |
| DP-08 | Drip Pricing | GST, e-sign, platform fee revealed late | B2C total incl. GST and pass-throughs on first display (§6.4) | `ECOM_total_price_breakup` |
| DP-09 | Disguised Advertisement | Paid partner content as guidance; "featured" neutrals | "Sponsored"/"Partner" label on any paid CMS placement; no paid neutral placement (X-03) | `DARK_PATTERN_label_sponsored`, `NO_PAID_PLACEMENT` |
| DP-10 | Nagging | Repeated upgrade modals | Max one upgrade prompt per user per 7 days; none in case/hearing/sealed views | `DARK_PATTERN_nag_rate_limit` |
| DP-11 | Trick Question | "Uncheck to not receive offers" | Positive opt-in wording; double negatives rejected by linter | `DARK_PATTERN_lint_trick_question` |
| DP-12 | SaaS Billing | Silent trial-to-paid; unused seats billed silently; positive-option renewals | `trial_converts_automatically = false`; auto-renew OFF default for individuals/SMEs; seat changes shown before charge | `DARK_PATTERN_no_silent_conversion` |
| DP-13 | Rogue Malwares | Malicious scripts/ads injected into pages | No third-party ad scripts; CSP allow-list; SRI on scripts; dependency and malware scanning (master §11) | `DARK_PATTERN_csp_no_ad_scripts` |

**Quarterly self-audit:** `DarkPatternAuditJob` runs all DP tests plus a sampled manual review of 20 live flows; the `compliance_officer` signs the report (`core.dark_pattern_audits`); the first report also records the Board's decision on filing a self-declaration (§11 Q-O2).

### 6.3 E-Commerce Rules 2020 → controls

| Duty | Control |
|---|---|
| Display legal name, address, customer care, grievance officer (r.4(4)) | Footer and `/contact` from `tenant.legal_entity` (master X-15); grievance officer on every invoice and receipt |
| Acknowledge in 48 h, redress in one month (r.4(5)) | Billing queries (§5.13) carry clocks `ecom_ack_48h` and `ecom_redress_1m` with owner (NN-04 pattern) |
| Explicit consent; no pre-ticked boxes (r.4(9)) | All checkout and plan-change consents unticked; test `ECOM_no_preticked` |
| No cancellation charges unless the entity bears similar charges when it cancels | Late-cancellation lines (ANC.ADJOURN, consult < 24 h) are mirrored: if Equator or the neutral cancels late, the user gets a full refund **and** free rebooking; test `ECOM_r4_cancellation_symmetry` |
| Refunds within a reasonable period, to the original instrument | §5.13 SLA; FR-P05-33 |
| Total price with breakup of all compulsory and voluntary charges; refund and cancellation terms before purchase (r.7) | §6.4; "Refund policy" summary on every checkout (SCR-P05-02) |

### 6.4 Consumer price display (GST-inclusive)

| Buyer context (deterministic) | Lead price | Beneath | Example |
|---|---|---|---|
| No GSTIN on the buyer profile **or** party-facing case checkout for an individual | **Total payable incl. GST and pass-throughs** | "₹X + ₹Y GST" and each pass-through at actuals | "₹588.82 total (₹499 + ₹89.82 GST)" |
| GSTIN on profile **or** `/pricing/organisations` | "₹X / month + GST" | Total incl. GST on hover-free expandable line and on the preview | "₹25,000 / month + GST (₹29,500 total)" |
| Foreign buyer (INT) | Amount in invoice currency with INR equivalent and FX snapshot date (App. B §B.6) | "Zero-rated export under LUT" or GST as applicable | "USD 1,500.00 (≈ ₹1,32,375.00 at FBIL 21 Oct 2026)" (illustrative rate 88.25; live value from the FX snapshot) |
| RCM lines to a business (arbitral tribunal) | Fee without GST | "Tax payable on reverse charge: Yes (18% self-assessed by you: ₹{rcm})" | — |

Rules: GST is computed by the tax engine for the buyer's place of supply (state required at checkout for B2C — IGST s.12(2)(b)); paise shown (no rounding up to hide tax); a Board option `billing.b2c_tax_inclusive_authoring` (default OFF) would allow round GST-inclusive B2C prices authored in the fee editor with back-computed taxable value — it changes Appendix B's ex-GST convention and therefore needs Board approval and a B amendment.

### 6.5 GST invoicing rules (implemented in P05 §4E; summarised)

1. Tax invoice particulars per CGST Rules r.46 (incl. recipient name, address and state for unregistered recipients where the rule requires), gapless series per FY per GSTIN; bill of supply for exempt supplies (r.49); receipt voucher for advances, wallet top-ups and annual plans paid before the period begins where the tax memo treats them as advances (r.50); refund voucher (r.51); credit/debit notes (s.34; r.53) with the s.34(2) cut-off.
2. Continuous supply of services (subscriptions): invoice on or before the due date of payment (CGST s.31(5)(a)); annual plans invoiced at start.
3. e-Invoice IRN and QR for B2B/export/SEZ documents when AATO > ₹5 crore; 30-day IRP window when AATO ≥ ₹10 crore; IRN cancellation ≤ 24 h, else credit note. B2C dynamic QR applies only above AATO ₹500 crore (Notification 14/2020-CT) — flag `gst.b2c_dynamic_qr` OFF.
4. Place of supply per IGST Act s.12(2) (B2B by recipient location; B2C by address on record, else supplier location); export under LUT with r.96A realisation tracking (LR-TAX-009).
5. Pure-agent pass-throughs excluded from taxable value (CGST Rules r.33; T15).
6. GSTIN validation before B2B invoice; mismatched or cancelled GSTIN → invoice as B2C with notice to the buyer.

### 6.6 Auto-renewal and recurring debits

India has no single auto-renewal statute; Equator's rule set combines the RBI E-mandate Framework 2026, Dark Patterns DP-05/DP-12 and E-Commerce r.4(9):

| Rule | Implementation |
|---|---|
| AR-1 Auto-renew OFF by default for individuals and SMEs; enterprise per signed order form | `core.plans.auto_renew_default` |
| AR-2 Turning auto-renew ON is an explicit action showing amount, date and how to stop | §5.2 |
| AR-3 Reminders T-30, T-7, T-1 (service templates) with "Turn off auto-renew" deep link | P07 journey `billing.renewal_reminder` |
| AR-4 Pre-debit notice ≥ 24 h by the PSP/bank (merchant name, amount, date, mandate reference, reason) | Descriptor = plan name (`EMANDATE_descriptor_present`) |
| AR-5 Debits above ₹15,000 need AFA each time; UI warns before the user commits | §5.3, §5.9 |
| AR-6 No fee for mandates | `EMANDATE_no_fee` |
| AR-7 Cancelling the plan cancels the mandate | §5.12 |
| AR-8 Price increase at renewal: ≥ 30 days' notice with the new total; renewal does not proceed at the new price for auto-renew customers unless they confirm (individuals/SMEs) | `RENEWAL_PRICE_CHANGE_CONSENT` |

### 6.7 Refund timelines and prepaid balances

| Item | Timeline / rule |
|---|---|
| Decision on a refund request | ≤ 7 working days (Equator SLA); consumer queries acknowledged ≤ 48 h, redressed ≤ 1 month (E-Commerce r.4(5)) |
| Initiation after approval | ≤ 3 working days (FR-P05-33) |
| Auto-refunds (Explorer review late, duplicate payment, Equator cancellation) | Initiated within 1 working day without a request |
| Instrument | Original instrument (RBI PA Directions 2025) |
| Credit note | Issued with the refund for taxed supplies (s.34) |
| Wallets and credits | Redeemable only for Equator's own supplies (closed-system PPI position; O-R6); wallet refundable net of dues on termination; credits per §2.3 |

### 6.8 Proposed Legal Rules Register entries (add to Appendix G, `status = 'UNVERIFIED'` until legal reviewer sign-off)

| ID | Rule | Source |
|---|---|---|
| LR-CONS-007 | No misleading price, saving or plan claims; every price claim needs a Claims Register entry | CPA 2019 ss.2(28), 21; CCPA Misleading Advertisements Guidelines 2022 |
| LR-CONS-008 | The 13 dark patterns are prohibited; quarterly self-audit | Dark Patterns Guidelines 2023 (30 Nov 2023), Annexure 1; CCPA advisory 5 Jun 2025 |
| LR-CONS-009 | Explicit affirmative consent for purchases; no pre-ticked boxes; cancellation-charge symmetry | E-Commerce Rules 2020 r.4 |
| LR-CONS-010 | Total price with breakup of compulsory charges before purchase | E-Commerce Rules 2020 r.7 **[VERIFY — sub-rule]** |
| LR-PAY-005 | Card data never stored; tokens only | RBI CoFT framework (effective 1 Oct 2022); PCI DSS v4.0.1 |
| LR-PAY-006 | Wallets/credits redeemable only for Equator's own supplies | RBI PPI Master Directions (27 Aug 2021, as amended) **[VERIFY]** |
| LR-TAX-011 | Subscription invoicing for continuous supply of services | CGST Act s.31(5) |
| LR-CORP-001 | Related-party referral arrangements need Audit Committee/Board approval and disclosure | Companies Act 2013 ss.177(4)(iv), 188; Rules 2014 r.15 |

---

## 7. Dunning, failed payments, grace and suspension

### 7.1 Never-suspend list (hard rule; overrides every ladder below)

Billing state (any subscription, any unpaid invoice) **never** blocks: (a) joining or continuing a scheduled or live hearing or session; (b) reading or downloading case records, outcomes, awards, settlements, orders, certified first copies and the evidence bundle needed to protect legal rights (e.g., to file a s.34 challenge or an execution petition); (c) any running statutory or regulatory clock, its alerts or its owner's tasks (NN-04); (d) receiving notices and responding to a case, including filing a response within a deadline; (e) GRM ticket intake and replies within regulator clocks; (f) an IC's access to an open POSH inquiry within its 90-day clock (NN-07); (g) signing an outcome already agreed; (h) paying into escrow or making settlement instalments (NN-13 rails); (i) DPDP data-principal requests and data export; (j) signposting. Test suite `NN-04_dunning_never_stops_clocks` + `BILLING_never_blocks_*` (one test per item a–j).

### 7.2 Subscription ladder (P05 §5.6, with copy)

| Day | State | Action | Banner / message (en) |
|---|---|---|---|
| D0 | `past_due` | Renewal debit fails; notice 1 (in-app + email) | "We couldn't take your payment of ₹3,537.64 for Solo (2 seats) (due 1 Nov). Your cases are not affected. Update your payment method." |
| D+1, D+3, D+5 | `past_due` | Auto-retry within the mandate only (never by card-on-file outside it) | — |
| D+7 | `past_due` | Notice 2 to billing contacts + owner (email, in-app, SMS service template) | "Payment still due. On 16 Nov, new private matters will pause. Existing cases, hearings and deadlines continue." |
| D+15 | `suspended_soft` | Features tagged `new_work` off (new private matters, new bulk batches, new API case creation, new seats); `existing_work` continues | "New private matters are paused until payment. Your existing cases continue." |
| D+45 | `cancelled` | Plan ends; data export offered 90 days; Chambers run-off 90 days for parties (P10 FR-P10-04) | "Your plan has ended. Download your data by 16 Mar 2027." |

Grace for annual plans paid by invoice (enterprise): due date + 30 days before D0 of the ladder. Reinstatement at any point before D+45 on payment, with no reinstatement fee.

### 7.3 Enterprise usage invoices

Net-30 default; reminders at due date, +7, +15; at +30 `account_on_hold`: new bulk batches and new API case creation paused **after 7 days' written notice**; existing cases, notices already scheduled, hearings, GRM intake, clocks continue; interest on late payment only if the contract states it. Wallet auto-top-up failures follow the same notice pattern.

### 7.4 Party case fees

Unpaid party case fees follow the case's billing rules, not dunning: stage progression requires payment **except** where waiting would stop a statutory clock (then the case proceeds and the debt is pursued separately, FR-P05-57); arbitration deposits follow the A&C Act s.38 deposit workflow (substitute payment; suspension or termination of proceedings is a tribunal decision under s.38(2), not a billing automation). No collection messages threaten case outcomes; no unpaid fee ever blocks access to records or bars a person from future matters (contrast Sama's "barred from future matters" term — not adopted).

### 7.5 Failed one-time payments

Intent expires after 30 minutes (configurable); the quote stays valid for its validity period; retry with another method; no penalty; three failures in an hour → 30-minute cool-off (FR-P05-56) with a "Pay by bank transfer instead" option.

---

## 8. Data model, APIs, events and errors

All tables: `tenant_id` + RLS; money as `amount_minor BIGINT` + `currency CHAR(3)`; UUIDv7; append-only where stated (UPDATE/DELETE revoked). Names align with Appendix F; this section **extends** `core.plans` and `core.subscriptions` (F §F.4.8) — the P05 v2 migration applies these changes.

### 8.1 DDL (binding deltas and new tables)

```sql
-- Extend core.plans (F §F.4.8; P05 FR-P05-35)
ALTER TABLE core.plans
  DROP CONSTRAINT IF EXISTS plans_product_line_check,
  ADD CONSTRAINT plans_product_line_check CHECK (product_line IN (
    'chambers','grm_lender','grm_listed','grm_employer','grm_university','posh','enterprise_api',
    'academy_membership','neutral','counsel','business_assure','membership','users_forum','insurer_programme')),
  ADD COLUMN segment text NOT NULL DEFAULT 'organisation' CHECK (segment IN ('individual','sme','organisation','enterprise','institution')),
  ADD COLUMN auto_renew_default boolean NOT NULL DEFAULT false,
  ADD COLUMN trial_days int NOT NULL DEFAULT 0 CHECK (trial_days BETWEEN 0 AND 30),
  ADD COLUMN trial_converts_automatically boolean NOT NULL DEFAULT false CHECK (trial_converts_automatically = false),  -- DP-12
  ADD COLUMN annual_multiplier numeric(4,2) NOT NULL DEFAULT 10.00,
  ADD COLUMN cooling_off_days int NOT NULL DEFAULT 0,
  ADD COLUMN public_label_i18n jsonb NOT NULL,
  ADD COLUMN status text NOT NULL DEFAULT 'draft' CHECK (status IN ('draft','in_review','approved','published','superseded')),
  ADD COLUMN board_approval_ref text;

CREATE TABLE core.plan_prices (
  id uuid PRIMARY KEY DEFAULT uuidv7(), plan_id uuid NOT NULL REFERENCES core.plans(id),
  version int NOT NULL, interval text NOT NULL CHECK (interval IN ('monthly','annual')),
  unit text NOT NULL CHECK (unit IN ('flat','per_seat','per_employee','per_student')),
  amount_minor bigint NOT NULL CHECK (amount_minor >= 0), currency char(3) NOT NULL,
  minimum_minor bigint, min_quantity int, max_quantity int,
  effective_from date NOT NULL, effective_to date,
  UNIQUE (plan_id, version, interval));

CREATE TABLE core.plan_entitlements (
  id uuid PRIMARY KEY DEFAULT uuidv7(), plan_id uuid NOT NULL REFERENCES core.plans(id), plan_version int NOT NULL,
  feature_key text NOT NULL,                       -- §4.2
  value_kind text NOT NULL CHECK (value_kind IN ('bool','limit','money','tier')),
  value jsonb NOT NULL, period text CHECK (period IN ('month','year','term','case','none')),
  overage_rate_minor bigint, hard_limit boolean NOT NULL DEFAULT false,
  always_on boolean NOT NULL DEFAULT false, parity_safe boolean NOT NULL DEFAULT false,
  UNIQUE (plan_id, plan_version, feature_key),
  CHECK (NOT (always_on AND hard_limit)));

ALTER TABLE core.subscriptions
  ADD COLUMN subject_kind text NOT NULL CHECK (subject_kind IN ('tenant','person','organisation')),
  ADD COLUMN subject_id uuid NOT NULL,
  ADD COLUMN plan_version int NOT NULL,
  ADD COLUMN quantity int NOT NULL DEFAULT 1,
  ADD COLUMN interval text NOT NULL,
  ADD COLUMN auto_renew boolean NOT NULL,
  ADD COLUMN cancel_at timestamptz, cancelled_at timestamptz, cancellation_reason text,
  ADD COLUMN trial_ends_at timestamptz, paused_until date,
  ADD COLUMN mandate_id uuid REFERENCES core.mandates(id),
  ADD COLUMN entitlement_snapshot jsonb NOT NULL,      -- pinned (NN-21)
  ADD COLUMN contract_id uuid,                          -- enterprise
  ADD CONSTRAINT subscriptions_status_check CHECK (status IN ('trialing','active','past_due','suspended_soft','cancelled','expired','paused'));

CREATE TABLE core.subscription_changes (       -- append-only
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, subscription_id uuid NOT NULL REFERENCES core.subscriptions(id),
  change_kind text NOT NULL CHECK (change_kind IN ('create','upgrade','downgrade','seat_add','seat_remove','interval_change','auto_renew_on','auto_renew_off','pause','resume','cancel_scheduled','cancel_undone','cancelled','renewed','price_change_notice')),
  preview jsonb NOT NULL, preview_sha256 char(64) NOT NULL, proration_minor bigint NOT NULL DEFAULT 0,
  effective_at timestamptz NOT NULL, actor_user_id uuid NOT NULL, step_up_at timestamptz, created_at timestamptz NOT NULL DEFAULT now());

CREATE TABLE core.meters (code text PRIMARY KEY, unit text NOT NULL, reset text NOT NULL, aggregation text NOT NULL CHECK (aggregation IN ('sum','max','last','unique_count')), description_i18n jsonb NOT NULL);
CREATE TABLE core.usage_aggregates (
  tenant_id uuid NOT NULL, subscription_id uuid, contract_id uuid, meter_code text NOT NULL REFERENCES core.meters(code),
  period tstzrange NOT NULL, quantity bigint NOT NULL, computed_at timestamptz NOT NULL,
  PRIMARY KEY (tenant_id, meter_code, period, subscription_id));
CREATE TABLE core.meter_alerts (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, subscription_id uuid NOT NULL, meter_code text NOT NULL,
  threshold_pct int NOT NULL CHECK (threshold_pct BETWEEN 50 AND 150), channels text[] NOT NULL, last_fired_period tstzrange);

CREATE TABLE core.credit_grants (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, subscription_id uuid NOT NULL REFERENCES core.subscriptions(id),
  amount_minor bigint NOT NULL CHECK (amount_minor > 0), currency char(3) NOT NULL, expires_at timestamptz NOT NULL, source_invoice_id uuid NOT NULL);
CREATE TABLE core.credit_ledger (           -- append-only
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, grant_id uuid NOT NULL REFERENCES core.credit_grants(id),
  entry_kind text NOT NULL CHECK (entry_kind IN ('grant','redeem','reverse','lapse')),
  amount_minor bigint NOT NULL, invoice_line_id uuid, case_id uuid, created_at timestamptz NOT NULL DEFAULT now(),
  CHECK (entry_kind <> 'redeem' OR invoice_line_id IS NOT NULL));
-- Trigger: a 'redeem' row is rejected unless the target invoice line has revenue_owner = 'equator'
-- and basis <> 'REGULATED_TABLE' (O-R6 → WALLET_LINE_NOT_REDEEMABLE). Same trigger on core.wallet_ledger consumption.

CREATE TABLE core.billing_profiles (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, subject_kind text NOT NULL, subject_id uuid NOT NULL,
  buyer_kind text NOT NULL CHECK (buyer_kind IN ('individual','organisation')), pan_enc bytea, tan text, legal_name text, trade_name text,
  billing_address jsonb NOT NULL, state_code char(2) NOT NULL, po_required boolean NOT NULL DEFAULT false,
  tds_deductor boolean NOT NULL DEFAULT false, tds_section_code text, govt_entity boolean NOT NULL DEFAULT false,
  foreign_recipient boolean NOT NULL DEFAULT false, country char(2), UNIQUE (subject_kind, subject_id));
CREATE TABLE core.billing_gstins (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, billing_profile_id uuid NOT NULL REFERENCES core.billing_profiles(id),
  gstin char(15) NOT NULL CHECK (gstin ~ '^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$'), legal_name text NOT NULL, address jsonb NOT NULL,
  state_code char(2) NOT NULL, status text NOT NULL, verified_at timestamptz, sez boolean NOT NULL DEFAULT false, cost_centre text,
  is_default boolean NOT NULL DEFAULT false, UNIQUE (billing_profile_id, gstin));
CREATE TABLE core.billing_contacts (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, billing_profile_id uuid NOT NULL REFERENCES core.billing_profiles(id),
  name text NOT NULL, email text NOT NULL, mobile text, roles text[] NOT NULL, gstin_id uuid, verified_at timestamptz);
CREATE TABLE core.tax_documents (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, billing_profile_id uuid,
  kind text NOT NULL CHECK (kind IN ('tds_certificate','lut','sez_loa','trc','form_41','no_pe_declaration','gst_tds_certificate')),
  fy text NOT NULL, quarter int CHECK (quarter BETWEEN 1 AND 4), amount_minor bigint, section_code text, document_id uuid NOT NULL,
  match_status text NOT NULL DEFAULT 'pending' CHECK (match_status IN ('pending','matched','mismatch','not_applicable')));

CREATE TABLE core.enterprise_contracts (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, contract_no text NOT NULL UNIQUE,
  organisation_id uuid NOT NULL, term daterange NOT NULL, products text[] NOT NULL, price_versions jsonb NOT NULL,
  commitment_kind text NOT NULL CHECK (commitment_kind IN ('none','volume','spend')), committed_volume int, committed_spend_minor bigint,
  tier_code text, shortfall_fee_enabled boolean NOT NULL DEFAULT false, retro_true_up boolean NOT NULL DEFAULT false,
  sla jsonb NOT NULL, disclosure_flag boolean NOT NULL DEFAULT true CHECK (disclosure_flag = true),     -- NN-16
  appointment_rights boolean NOT NULL DEFAULT false CHECK (appointment_rights = false),                  -- NN-03
  authority_to_settle jsonb, non_renewal_notice_days int NOT NULL DEFAULT 60, status text NOT NULL);
CREATE TABLE core.true_up_runs (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, contract_id uuid NOT NULL REFERENCES core.enterprise_contracts(id),
  quarter_end date NOT NULL, inputs jsonb NOT NULL, run_rate int NOT NULL, from_tier text, to_tier text, effective_from date,
  notice_sent_at timestamptz, sha256 char(64) NOT NULL, UNIQUE (contract_id, quarter_end));

CREATE TABLE core.memberships (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, person_id uuid, organisation_id uuid,
  programme text NOT NULL CHECK (programme IN ('neutral_ladder','users_forum')),
  grade text NOT NULL CHECK (grade IN ('student_associate','associate','member','fellow','forum_corp','forum_firm','forum_assoc')),
  membership_no text NOT NULL UNIQUE, valid daterange NOT NULL, status text NOT NULL CHECK (status IN ('active','grace','lapsed','ended')),
  subscription_id uuid REFERENCES core.subscriptions(id), CHECK ((person_id IS NULL) <> (organisation_id IS NULL)));
-- NO_PAID_PLACEMENT: neutrals.*, allocation and grading schemas have no SELECT grant on core.memberships, core.subscriptions, core.plans.

CREATE TABLE core.cancellation_requests (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, subscription_id uuid NOT NULL,
  steps_taken int NOT NULL CHECK (steps_taken <= 3), reason_code text, reason_text text, retention_offer_code text, retention_accepted boolean,
  mandate_cancel_ref text, effective_at timestamptz NOT NULL, reference_no text NOT NULL UNIQUE, created_at timestamptz NOT NULL DEFAULT now());
CREATE TABLE core.billing_queries (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, requester_user_id uuid NOT NULL,
  subject text NOT NULL, reference_kind text NOT NULL, reference_id uuid NOT NULL, computed_minor bigint, requested_minor bigint,
  status text NOT NULL, ack_due_at timestamptz NOT NULL, redress_due_at timestamptz NOT NULL, refund_id uuid, credit_note_id uuid);
CREATE TABLE core.dark_pattern_audits (id uuid PRIMARY KEY DEFAULT uuidv7(), period daterange NOT NULL, results jsonb NOT NULL,
  manual_sample jsonb NOT NULL, signed_by uuid NOT NULL, signed_at timestamptz NOT NULL, self_declaration_filed boolean);
```

`core.mandates` (P05) gains: `descriptor text NOT NULL`, `max_amount_minor`, `frequency`, `valid daterange`, `afa_required_above_minor bigint NOT NULL DEFAULT 1500000`, `customer_cancelled_at`, `merchant_cancelled_at`.

### 8.2 Enumerations (seed)

`plan_code`: NEU-PANEL, CH-LITE, CH-SOLO, CH-PRO, CH-INST, CH-IAAS, COUNSEL-FREE, COUNSEL-PRO, FIRM-ENT, BIZ-ASSURE-START, BIZ-ASSURE-GROW, BIZ-ASSURE-PLUS, MEM-STUDENT, MEM-ASSOC, MEM-MEMBER, MEM-FELLOW, FORUM-CORP, FORUM-FIRM, FORUM-ASSOC, GRM-* (11), POSH-* (4), EAPI-* (4), INS-SUB-* (4). New ANC codes: ANC.EXPLORER.REVIEW, ANC.TYPECOPY.AI (₹0), ANC.TYPECOPY.VERIFIED, ANC.TRANSL.CONV.IND, ANC.TRANSL.CONV.BIZ, ANC.TRANSL.CONV.UN, ANC.TRANSL.CERT, ANC.TRANSCRIPT.AI, ANC.TRANSCRIPT.STENO, ANC.BUNDLE, ANC.APOSTILLE. `cancellation reason_code`: too_expensive, low_usage, missing_feature, switching_provider, practice_closing, other.

### 8.3 APIs (`/v1`, OpenAPI 3.1; Idempotency-Key on all POST/PATCH that create money or change plans)

| Method & path | Purpose | Role |
|---|---|---|
| `GET /v1/public/plans?segment=&product_line=` | Published plans with display prices (§6.4 mode by query `buyer=individual|organisation`) | Public |
| `GET /v1/billing/overview` | SCR-P05-19 data | `billing.view` |
| `GET /v1/subscriptions/{id}` · `GET /v1/subscriptions/{id}/entitlements` | Plan and entitlements | `billing.view` |
| `GET /v1/subscriptions/{id}/change-preview?plan=&seats=&interval=` | Proration preview (hash returned) | `billing.manage` |
| `PATCH /v1/subscriptions/{id}` | Apply change with `preview_sha256` | `billing.manage` + step-up |
| `POST /v1/subscriptions/{id}/auto-renew` | `{enabled}` | `billing.manage` |
| `POST /v1/subscriptions/{id}/cancel` · `POST /v1/subscriptions/{id}/cancel/undo` | Cancel / undo | `billing.cancel` + step-up |
| `POST /v1/subscriptions/{id}/pause` | Chambers pause | `billing.manage` |
| `GET /v1/entitlements/check?feature=&case_id=` | Runtime check (internal + UI) | authenticated |
| `GET /v1/usage?meter=&from=&to=` · `GET /v1/usage/export` | Meters | `billing.view` |
| `PUT /v1/usage/alerts/{meter}` | Alert thresholds | `billing.manage` |
| `GET/POST/DELETE /v1/payment-methods` | List; create provider checkout session; remove | `billing.manage` + step-up for DELETE |
| `GET /v1/mandates` · `POST /v1/mandates` · `POST /v1/mandates/{id}/cancel` | Mandates | `billing.manage` + step-up |
| `GET /v1/invoices?type=&status=&gstin=` · `GET /v1/invoices/{id}/pdf` · `/xml` | Documents | `billing.view` |
| `GET/PUT /v1/billing-profile` · `POST /v1/billing-profile/gstins` · `POST /v1/billing-profile/tax-documents` | Tax details | `billing.manage` (+ step-up for GSTIN change) |
| `GET/PUT /v1/billing-contacts` | Contacts | `billing.manage` |
| `GET /v1/credits` · `GET /v1/wallets/{id}` · `POST /v1/wallets/{id}/topups` · `POST /v1/wallets/{id}/withdrawals` | Balances | `billing.view` / `billing.manage` |
| `POST /v1/billing-queries` · `GET /v1/billing-queries/{id}` | Refunds and queries | `billing.refund.request` |
| `GET /v1/memberships/me` · `POST /v1/memberships/{id}/renew` | Membership | member |
| `GET /v1/enterprise/contracts/{id}` · `GET /v1/enterprise/contracts/{id}/true-ups` · `POST /v1/enterprise/contracts/{id}/non-renewal` | Contract view | `enterprise_admin` |
| `GET /v1/neutrals/me/payouts` · `PUT /v1/neutrals/me/payout-account` | Neutral payouts | neutral (+ step-up) |

### 8.4 Domain events (CloudEvents; payloads carry IDs and amounts, never PII)

`equator.billing.plan.published.v1` · `equator.billing.subscription.created.v1` · `.changed.v1` (existing) · `.auto_renew_changed.v1` · `.trial_ending.v1` (T-3) · `.renewal_reminder_due.v1` (T-30/T-7/T-1) · `.past_due.v1` (existing) · `.suspended_soft.v1` · `.cancel_scheduled.v1` · `.cancelled.v1` · `.renewed.v1` · `equator.billing.entitlement.denied.v1` · `equator.billing.meter.threshold_crossed.v1` · `equator.billing.credit.granted.v1` · `.redeemed.v1` · `.lapsing.v1` · `.lapsed.v1` · `equator.billing.tax_profile.updated.v1` · `equator.billing.tds_certificate.matched.v1` · `equator.billing.query.opened.v1` · `.resolved.v1` · `equator.billing.true_up.computed.v1` · `equator.billing.membership.renewed.v1` · `.lapsed.v1` · `equator.payments.mandate.registered.v1` · `.cancelled.v1` · `.debit_notified.v1` · `.debit_failed.v1` · `equator.compliance.dark_pattern_audit.signed.v1`.

### 8.5 Error codes (RFC 9457 `code`; add to Appendix F catalogue)

`PLAN_NOT_AVAILABLE` · `PLAN_NOT_PUBLISHED` · `SEAT_MINIMUM` · `PRORATION_PREVIEW_STALE` · `PREVIEW_HASH_MISMATCH` · `MANDATE_LIMIT_EXCEEDED` · `MANDATE_REQUIRED_FOR_AUTO_RENEW` · `INSTRUMENT_IN_USE_BY_MANDATE` · `ENTITLEMENT_DENIED` · `ENTITLEMENT_NOT_PARITY_SAFE` · `METER_LIMIT_REACHED` · `WALLET_LINE_NOT_REDEEMABLE` · `CREDIT_EXPIRED` · `GSTIN_INVALID` · `GSTIN_INACTIVE` · `PAN_GSTIN_MISMATCH` · `TDS_CERT_DUPLICATE` · `CANCEL_ALREADY_SCHEDULED` · `RENEWAL_PRICE_CHANGE_CONSENT` · `PROHIBITED_PRODUCT` (deny-list X-01…X-16) · `PAID_PLACEMENT_FORBIDDEN` · `BILLING_STATE_CANNOT_BLOCK` (thrown in tests if any guard tries to block a never-suspend action) · `STEP_UP_REQUIRED` (existing).

### 8.6 Configuration keys and feature flags

`plans.ch_lite.enabled` (ON) · `plans.counsel_pro.enabled` (ON) · `plans.biz_assure.enabled` (OFF until public label cleared, O-R7) · `plans.biz_assure.public_label` · `membership.ladder.enabled` (ON) · `membership.postnominals.enabled` (OFF) · `forum.enabled` (ON) · `academy.institute_referral` (OFF until A-03) · `academy.institute_referral_fee` (OFF) · `billing.cooling_off_days` (14) · `billing.b2c_tax_inclusive_authoring` (OFF) · `billing.upgrade_prompt_min_days` (7) · `billing.cancel_max_steps` (3) · `billing.renewal_reminder_days` ([30,7,1]) · `mandate_limits.afa_free_limit` (₹15,000) · `mandate_limits.upi_autopay_max_debit` (₹99,999) · `mandate.headroom_pct` (20) · `studio.fair_use.*` (§4.4) · `trueup.downtier_quarters` (2) · `trueup.downtier_threshold_pct` (90) · `trueup.notice_days` (30) · `chambers.pause_max_months_per_year` (3) · `gst.b2c_dynamic_qr` (OFF).

---

## 9. Acceptance tests (Gherkin; `tests/acceptance/billing-v2/`)

```gherkin
Feature: Plans, billing and settings (Appendix O)

  Scenario: NN-29 consumer sees the total including GST first
    Given an individual without a GSTIN opens the Explorer human review checkout
    Then the largest price shown is "₹588.82"
    And beneath it "₹499 + ₹89.82 GST" is shown
    And no other charge is added at the payment step

  Scenario: Business buyer sees ex-GST plan prices
    Given a buyer with a verified GSTIN views /pricing/organisations
    Then GRM-LENDER-S is shown as "₹25,000 / month + GST"

  Scenario: DP-12 trial never converts silently
    Given a neutral starts a 14-day CH-LITE trial without a payment method
    When the trial end date passes
    Then the subscription status is "expired"
    And no payment intent or mandate debit was created

  Scenario: DP-05 cancellation takes no more steps than sign-up
    Given a counsel subscribed to COUNSEL-PRO in 3 steps
    When the counsel cancels from Settings → Billing
    Then cancellation completes in at most 3 steps
    And the linked UPI AutoPay mandate is cancelled through the PSP API in the same transaction
    And a confirmation with a reference number is shown and emailed

  Scenario: Retention offer is honest and single
    When a CH-SOLO admin reaches the cancel page
    Then at most one retention option is shown
    And the copy linter finds no confirm-shaming phrase

  Scenario: Proration preview equals the charge
    Given a CH-PRO tenant with 3 seats at ₹2,999 monthly on day 11 of a 30-day cycle
    When the admin previews adding 2 seats
    Then today's charge is ₹3,999 plus GST ₹719.82
    And applying the change with the preview hash charges exactly ₹4,718.82

  Scenario: AFA warning above ₹15,000
    Given a COUNSEL-PRO annual renewal for 5 seats of ₹58,941 including GST on a UPI AutoPay mandate
    Then the plan page warns "Your bank will ask you to approve this payment"
    And the mandate page shows that debits above ₹15,000 need approval each time

  Scenario: EMANDATE_no_fee
    When any mandate is created
    Then no invoice line with a mandate or auto-pay fee exists

  Scenario: NN-31 no card data in Equator systems
    When the API schema, database schema and application logs are scanned
    Then no field or value matches a PAN or CVV pattern
    And payment methods store only provider token references and last four digits

  Scenario: Dunning never blocks a live hearing
    Given a CH-SOLO tenant in "suspended_soft"
    And a hearing in one of its matters is scheduled now
    Then the neutral and the parties can join the hearing
    And they can download the case record and any award

  Scenario: GRM intake continues above allowance and in arrears
    Given a GRM-LENDER-S desk with 520 tickets this month and an overdue invoice
    When a borrower submits a new grievance
    Then the ticket is created and its RB-IOS clock starts
    And a ₹40 overage is rated for the new ticket (21 tickets above the 500 allowance = ₹840 for the period so far)

  Scenario: POSH inquiry never blocked by billing
    Given a POSH-SME employer is "past_due"
    And an inquiry is on day 40 of its 90-day clock
    Then IC members can open the sealed inquiry workspace

  Scenario: Business Assure credits never pay a neutral
    Given a BIZ-ASSURE-GROW holder with ₹18,000 credit files a COM mediation
    When credits are applied to the quote
    Then credits reduce only Equator registration and administration lines
    And the mediator's session fee is unchanged and payable in full
    And a redemption against the neutral line fails with WALLET_LINE_NOT_REDEEMABLE

  Scenario: Counterparty told about Business Assure
    Given the claimant holds a Business Assure plan
    When the respondent opens the case
    Then the respondent sees "This gives it no say in who decides your matter and no priority"

  Scenario: NO_PAID_PLACEMENT
    When the CI schema analyser inspects the directory, allocation and grading queries
    Then no query reads core.subscriptions, core.memberships or core.plans
    And two neutrals identical except for CH-PRO and membership status have equal allocation probability over 10,000 simulated draws (±2%)

  Scenario: Counsel-Pro gives no procedural advantage
    Given claimant counsel on COUNSEL-PRO and respondent counsel on COUNSEL-FREE in the same administered case
    Then the set of case actions and Pleadings Studio limits available to both is identical

  Scenario: Pleadings Studio fair-use raised for everyone
    Given a party reaches 1,000 ingested pages
    When the case manager raises the cap to 1,500 with a reason
    Then the cap is 1,500 for every party in that case
    And no paid overage option is shown to any party

  Scenario: Explorer human review auto-refund
    Given a paid review not delivered within 2 working days
    Then a full refund to the original instrument is initiated within 1 working day
    And a credit note is issued

  Scenario: Explorer human review never gives a merits view
    When a case manager's review note contains "strong case" or "likely to win"
    Then the qa_auditor blocks the note with GX-1 and it is not delivered

  Scenario: Quarterly true-up is prospective
    Given a lender contract committed at 25,000 cases (T2) with run-rate 21,000 in Q1 and 21,500 in Q2
    When the Q2 true-up runs
    Then tier T1 applies from 1 Oct after a notice dated at least 30 days earlier
    And no past invoice is re-rated

  Scenario: Up-tier is automatic
    Given run-rate reaches 1,00,000 at a quarter end
    Then tier T3 applies from the next quarter without notice period

  Scenario: E-Commerce cancellation symmetry
    Given Equator cancels a paid process consultation 2 hours before the slot
    Then the user receives a full refund and a free rebooking link

  Scenario: Membership never affects grade or allocation
    Given a Grade C neutral holding MEM-MEMBER
    When the membership is upgraded to Fellow or lapses
    Then the neutral's panel grade record and allocation weights are unchanged
    And a Fellow application without 25 completed matters and peer review is rejected

  Scenario: Invoice GST by place of supply
    Given Equator's GSTIN is in Delhi and an individual in Jaipur buys a verified type copy of 10 pages
    Then the invoice shows IGST 18% on ₹400 = ₹72.00 with place of supply "08-Rajasthan"

  Scenario: GSTIN change applies only to future invoices
    When an enterprise changes its default GSTIN
    Then existing invoices are unchanged
    And a correction request creates a credit note and a re-issued invoice before the s.34(2) cut-off

  Scenario: Renewal price increase needs consent for individuals
    Given a Lite subscriber with auto-renew ON and a published price increase
    When renewal is due without the subscriber's confirmation
    Then the renewal does not debit the new price and RENEWAL_PRICE_CHANGE_CONSENT is raised

  Scenario: Prohibited product cannot be published
    When a fee editor tries to publish a tariff item tagged "featured_listing" or "legal_notice_drafting"
    Then publication fails with PROHIBITED_PRODUCT

  Scenario: Upgrade prompts never appear in case views
    When a CH-LITE neutral at 100% of private matters opens a hearing room
    Then no upgrade prompt is rendered
```


---

## 10. Phase addendum (paste into P05)

**FR-P05-V2-01 — New cards and lines.** Seed `core.fee_schedules`/`core.plans` with NEU, CH-LITE, COUNSEL, BIZ, MEM, FORUM and the new ANC lines (§2, §8.2), all "Subject to Board approval"; update Appendix B §B.11 and §B.7.7 (O-R2) in the same PR. *Acceptance:* the schedule harness (FR-P05-07) passes for every new item; no new line has `revenue_owner = 'neutral'` with `discountable = true`; the public plans API returns each plan with its approval badge.

**FR-P05-V2-02 — Plan model extensions.** Apply §8.1 deltas to `core.plans` and `core.subscriptions`; add `plan_prices`, `plan_entitlements`, `subscription_changes`. *Acceptance:* a plan with `trial_converts_automatically = true` cannot be inserted; every subscription row carries a pinned `entitlement_snapshot`; changing a plan price creates a new version and never alters active subscriptions until renewal (NN-21).

**FR-P05-V2-03 — Entitlement service.** Implement `EntitlementService.check` with `always_on`, `parity_safe` and `new_work/existing_work` semantics (§4.1). *Acceptance:* `always_on` keys return allow in every billing state; a non-parity-safe key returns `ENTITLEMENT_NOT_PARITY_SAFE` inside an administered case; p95 < 20 ms with cache.

**FR-P05-V2-04 — Meters and alerts.** Meters in §4.3 with hourly aggregates and configurable alerts. *Acceptance:* alerts fire once per threshold per period; GRM intake, video in a live hearing and case-record uploads are never blocked at 100%.

**FR-P05-V2-05 — Settings pages.** Build SCR-P05-19 → SCR-P05-34 (§5) on web and mobile (mobile: all except SCR-P05-28 and full SCR-P05-33); 301 from `/(app)/subscriptions` and `/(enterprise)/billing`. *Acceptance:* each page implements the mandatory states; axe zero serious violations; works at 200% font scale; en + hi.

**FR-P05-V2-06 — Change-plan preview.** Deterministic preview with hash; apply only with matching hash (§5.3). *Acceptance:* WE-12 golden vector reproduced; preview older than 10 minutes → `PRORATION_PREVIEW_STALE`; AFA and mandate-limit warnings rendered when thresholds are crossed.

**FR-P05-V2-07 — Cancellation ≤ 3 steps.** Per §5.12 with automatic PSP mandate cancellation and undo until end date. *Acceptance:* `NO_SUBSCRIPTION_TRAP` measures steps-to-cancel ≤ steps-to-subscribe for every self-serve plan; at most one retention option; confirm-shaming lint passes.

**FR-P05-V2-08 — Mandates page and e-mandate rules.** Per §5.9 and §6.6. *Acceptance:* `EMANDATE_no_fee` and `EMANDATE_descriptor_present` pass; UPI AutoPay max = min(annual price × 1.2, configured cap); retries only within the mandate.

**FR-P05-V2-09 — Tax details and TDS certificates.** Per §5.6 with GSTIN verification, multi-GSTIN, TDS certificate matching against the 26AS/AIS import. *Acceptance:* invalid or inactive GSTIN rejected with `GSTIN_INVALID`/`GSTIN_INACTIVE`; PAN–GSTIN mismatch blocked; GSTIN changes affect future invoices only.

**FR-P05-V2-10 — Consumer price display.** §6.4 modes on quotes, checkouts, plan cards and invoices. *Acceptance:* `ECOM_total_price_breakup` passes on every B2C surface; no rounding hides GST; RCM lines labelled.

**FR-P05-V2-11 — Credits and wallet redemption guard.** `core.credit_grants`/`credit_ledger` and the redemption trigger (O-R6) for credits and wallets; narrow FR-P05-39 accordingly. *Acceptance:* redemption against a `neutral_direct`, tenant, pass-through or regulated line fails with `WALLET_LINE_NOT_REDEEMABLE`; lapse job writes `lapse` entries at `expires_at` after T-60/T-30 reminders.

**FR-P05-V2-12 — Enterprise contract object and true-up.** `core.enterprise_contracts`, `TrueUpJob` (§2.4.3), SCR-P05-33. *Acceptance:* the two true-up scenarios in §9 pass; `appointment_rights` and `disclosure_flag` CHECKs cannot be overridden; no retro re-rating unless `retro_true_up = true`.

**FR-P05-V2-13 — Refunds and billing queries.** SCR-P05-31 with E-Commerce clocks (48 h / 1 month) and auto-refunds (§6.7). *Acceptance:* computed amount equals the refund engine output; consumer queries carry owned clocks; auto-refund for a late Explorer review is initiated within 1 working day.

**FR-P05-V2-14 — Never-suspend guarantees.** Implement §7.1 items a–j as guards and tests `BILLING_never_blocks_*`. *Acceptance:* every test passes with the tenant in `past_due`, `suspended_soft` and `cancelled` (run-off) states.

**FR-P05-V2-15 — Dark-pattern controls.** DP-01…DP-13 checks (§6.2) in CI and `DarkPatternAuditJob` quarterly with `compliance_officer` sign-off. *Acceptance:* each DP test fails on a seeded violating fixture and passes on the shipped UI; the first audit report is generated in UAT.

**FR-P05-V2-16 — Prohibited-product deny-list.** `revenue-denylist` CI job and `PROHIBITED_PRODUCT` publish-time validator (§1.5). *Acceptance:* seeded items tagged with any X-01…X-16 tag cannot be published.

**FR-P05-V2-17 — Neutral payouts and tax page.** SCR-P05-32 (§5.14). *Acceptance:* payout account change requires step-up and triggers the 24-hour hold rule; TDS by deductor reconciles to AIS import; statement totals equal ledger totals.

**FR-P05-V2-18 — Unit-economics views.** `reporting.finance_*` views for §1.4 drivers and the recurring-share tile. *Acceptance:* views read only ledger and usage aggregates (no case PII); Board pack export includes recurring share by vertical.

## 10A. Phase addendum (paste into P10)

IDs carry the `O` suffix so they do not collide with Appendix N's FR-P10-V2-01…14.

**FR-P10-V2-O1 — CH-LITE plan.** Add CH-LITE (₹699/month; ₹6,990/year; 1 seat; 2 private matters/month; sub-domain only; 14-day trial without card; auto-renew OFF) to FR-P10-03 and the sign-up flow (SCR-P10-01). *Acceptance:* a Lite tenant cannot enable custom domain, own panel or extra seats; upgrade to Solo prorates per FR-P05-36.

**FR-P10-V2-O2 — Plan-dependent marketplace take.** Lite/Solo 15%, Pro 12%, Institution 10% (O-R2) in `chambers.revenue_share_agreements` defaults and §B.7.7. *Acceptance:* payout statements show the plan-specific rate; 0% on Equator-administered cases is unchanged.

**FR-P10-V2-O3 — Premium AI drafting scope.** The CH add-on applies only to neutral and secretariat drafting (O-R5). *Acceptance:* party-role users in a Chambers case cannot access the add-on; party drafting uses the Pleadings Studio with fair-use parity.

**FR-P10-V2-O4 — Pause.** Chambers pause up to 3 months per year: no new matters; existing matters continue. *Acceptance:* clocks, hearings and notices continue in paused tenants; a fourth month is refused.

**FR-P10-V2-O5 — Membership ladder and Users' Forum.** Implement §2.9 (`core.memberships`, SCR-P05-29), entry rules, no auto-renew default, post-nominals behind flag. *Acceptance:* Member entry accepts certificates from any recognised provider (not only the Institute); `NO_PAID_PLACEMENT` passes; Forum member list renders on `/trust/how-we-stay-neutral`.

**FR-P10-V2-O6 — Institute referral card.** §2.10 (implemented within Appendix N FR-P10-V2-09): ≥ 3 providers, alphabetical or seeded-random order, related-entity disclosure, referral fee flag OFF. *Acceptance:* card hidden while `academy.institute_referral` is OFF; when ON, disclosure text present and order alphabetical or randomised per session, never Institute-first.

**FR-P10-V2-O7 — Chambers billing in settings.** Chambers admins use SCR-P05-19 → SCR-P05-31 in tenant scope with tenant branding; run-off banner during suspension. *Acceptance:* parties in a suspended tenant see the run-off notice, not a billing error.

## 10B. Phase addendum (paste into P13)

**FR-P13-V2-O1 — Pricing routes.** `/fees`, `/pricing/organisations` (SCR-P13-20), `/pricing/professionals` (SCR-P13-21), `/pricing/business-assure` (SCR-P13-22) per §3.1 with plan-card anatomy and comparison-table rules. *Acceptance:* no horizontal scroll at 360 px; values never conveyed by colour alone; prices visible without login; all figures from the published-plans API with approval badge.

**FR-P13-V2-O2 — Plan copy deck.** §3.2 copy in en (hi after legal-translator review); `pricing-copy` linter with the prohibited phrase list. *Acceptance:* every plan page has headline, one-liner, benefits and FAQ from CMS; linter blocks seeded violations.

**FR-P13-V2-O3 — Consultation price alignment.** SCR-P13-14 shows ANC.CONSULT prices (O-R4). *Acceptance:* no "₹1,000" consultation copy remains.

## 10C. Phase addendum (paste each item into its own phase only: P03, P07, P09)

**FR-P03-V2-O1 — NO_PAID_PLACEMENT.** Directory, allocation and grading code paths have no grant on billing, plan or membership tables; simulation test per §9. *Acceptance:* CI schema analyser and the 10,000-draw simulation pass.

**FR-P07-V2-O1 — Billing journeys.** Service templates (DLT-registered) for renewal reminders T-30/T-7/T-1, trial ending, dunning D0/D+7/D+15/D+45, credit lapse T-60/T-30, meter alerts; promotional upgrade messages only with marketing consent. *Acceptance:* templates tagged `service_billing`; no billing message mentions case outcomes.

**FR-P09-V2-O1 — Enterprise contract fields.** Enterprise onboarding captures §2.4.1 clause heads into `core.enterprise_contracts`, including authority-to-settle evidence before L2 conciliation offers. *Acceptance:* an L2 offer by a lender without authority evidence is blocked; contract view shows NN-03/NN-16 disclosure text.

---

## 11. Open items and counsel questions

| # | Item | Owner | Effect until resolved |
|---|---|---|---|
| Q-O1 | E-Commerce Rules 2020 characterisation of Equator's own-service sales and Chambers marketplace bookings; exact sub-rule numbers for cancellation-charge symmetry, refunds and price breakup | Counsel | Comply with all r.4 and r.7 duties by default |
| Q-O2 | Whether the Dark Patterns Guidelines apply to B2B SaaS checkouts; whether to file a self-declaration after the first quarterly audit | Counsel + Board | Apply to all journeys |
| Q-O3 | Naming check for "Business Assure" (insurance/guarantee connotation; Claims Register) and post-nominals AEqR/MEqR/FEqR (trademark; confusion with MCI accreditation) | Counsel, CS | `plans.biz_assure.enabled` and `membership.postnominals.enabled` OFF |
| Q-O4 | Tax memo: Business Assure credit redemption and enterprise wallets (advance vs deposit; T16); SAC for SaaS plans; e-commerce-operator TDS/TCS on marketplace bookings (LR-TAX-007/008) | Tax adviser | Conservative treatment (GST at receipt) |
| Q-O5 | RBI PPI position for wallets and credits (closed system) and the current consolidated PPI Directions reference | Payments counsel | Redemption limited to Equator's own supplies (O-R6) |
| Q-O6 | Explorer human review by non-advocate case managers (Appendix K Q-K1) and the process-only script | Counsel | Process-only script; GX-1 blocks |
| Q-O7 | Counsel-Pro and Users' Forum: any justifiable-doubt risk under A&C Act s.12 and Fifth Schedule; adequate disclosure | Counsel | Disclosure on; no case-touching benefits |
| Q-O8 | Institute referral: related-party status (Companies Act s.2(76)) once the Institute's operating entity is confirmed; approvals under ss.177/188 | CS, Audit Committee | Referral fee OFF |
| Q-O9 | 14-day cooling-off refund for individual/SME first-time annual purchases (Equator policy, not a statutory duty) | Board | Default ON |
| Q-O10 | Board approval of all new figures in this appendix (CH-LITE, COUNSEL, BIZ, MEM, FORUM, ANC lines, marketplace take by plan) | Board | "Subject to Board approval" badge; no binding quotes from unapproved schedules (`SCHEDULE_NOT_APPROVED`) |
| Q-O11 | TDS certificate form number under the Income-tax Rules 2026 (successor to Form 16A) | Tax adviser | Field label generic ("TDS certificate") |
| Q-O12 | Optional GST-inclusive authoring of B2C prices (`billing.b2c_tax_inclusive_authoring`) | Board | OFF; ex-GST authoring with inclusive display |
