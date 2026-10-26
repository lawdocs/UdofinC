# Appendix AA — Equator Marketplace and Infrabyx Professional Registry (v3.0, 23 October 2026)

## AA.0 Purpose, sources, precedence

### AA.0.1 What this appendix specifies

This appendix specifies, to implementation level:

1. the **Equator Marketplace** (schema `mkp`): three separate surfaces with no join path between them —
   - (i) the **Equator Neutral Directory** (institutional; never paid; Appendix N §2.5 unchanged except as stated in AA.2);
   - (ii) the **Private Practice Marketplace** (chambers and independent non-advocate neutrals booked directly by parties, plus ancillary ADR service providers);
   - (iii) the **Professional Panel Register** (advocates, chartered accountants, company secretaries, cost accountants; consent-based; tenant-private by default; public search OFF);
2. the marketplace journeys (search → profile → enquiry → conflict check → engagement → fee disclosure → booking → payment → delivery → review → complaint → suspension/appeal), enterprise procurement, provider onboarding, payments and tax as an e-commerce operator, and marketplace governance;
3. **paid placement and display advertising** under NN-34 (all OFF by default, each with a named approver);
4. **post-resolution services**: execution of awards and settlements and registration support in which the party chooses the advocate or professional, and the optional Equator Post-Resolution Advocate Panel;
5. the **Infrabyx Professional Registry** (schema `dir`), the group shared service of decision D3-05, with consent per purpose, provenance, two-person verification, freshness rules, propagation of correction, withdrawal and erasure, and an API for Finbyx, Udofin and LawDocs under the Group Data-Sharing Agreement (GDSA);
6. revenue hooks into the stream registry owned by **Appendix AB** (`AB_Revenue_Architecture_v3_and_Stream_Registry.md`), the settings catalogue (tiers L/G/T, NN-33), RBAC, DDL sketches, APIs, events, error codes, audit, exports and acceptance tests;
7. phase addenda for P03, P05, P06, P09 and P13. Phase **P19** (`phases/P19_Marketplace_Professional_Registry_and_Revenue.md`) implements this appendix and the AB stream registry.

### AA.0.2 Sources

Research: **[RA]** `research/RA_JUPITICE.md` (Jupitice ADR Marketplace benchmark and design implications EQM-01…EQM-23); **[RE]** `research/RE_DIRECTORY_MARKETPLACE_LAW.md` (advocates and BCI Rules; CA/CS/CMA institute rules; Mediation Act 2023; E-Commerce Rules 2020 and the 2026 Amendment; CCPA guidelines; IT Rules; GST TCS/TDS; DPDP; GDSA; design implications A1–F29); **[RB]** `research/RB_BUSINESS_MODELS.md` (revenue stream catalogue RS-01…RS-35; deny-list proposals X-17…X-20; sponsored-listing design §B; automation AU-25). Pack v2.1: master NN-03, NN-13, NN-16, NN-17, NN-28, NN-29; 02 D2-11, D2-13, D2-14, D2-24; Appendix N §2.5, §6, §7, §8; Appendix O §1, §2.8, §6; Appendix R §4; Appendix S §4.5, §6; Appendix U §U.6; Appendix B §B.7.7; Appendix G LR-TAX-007, LR-TAX-008, LR-CONS-008. v3.0 binding decisions: NN-33 to NN-40 and D3-01 to D3-09 (`V3_WRITER_CONVENTIONS.md`).

Primary sources are cited as the research files cite them. Where research marks a point **[K]** (not confirmed), this appendix keeps the value configurable and marks it `**[VERIFY — open: …]**`.

### AA.0.3 Precedence and identifiers allocated here

Master §15 precedence applies. NN-34 (paid visibility), NN-38 (group boundaries) and NN-39 (professional directory) prevail over every statement in this appendix. Appendix AB is canonical for the revenue stream registry data model and stream codes; this appendix only declares which streams the marketplace and registry raise and the guardrails on them.

| Kind | IDs | Subject |
|---|---|---|
| Requirements | **R-62** | Equator Marketplace: three isolated surfaces; Private Practice Marketplace journeys, provider onboarding, payments as e-commerce operator, reviews, complaints, enterprise procurement, governance |
| | **R-63** | Infrabyx Professional Registry (`dir`) and Professional Panel Register; post-resolution services with party choice |
| | **R-64** | Paid placement (sponsored listings) and display advertising under NN-34; marketplace revenue hooks into the AB stream registry |
| Decisions | **D3-35** | Operating model of the Private Practice Marketplace (AA.2.4) |
| | **D3-36** | Registry topology and the Post-Resolution Advocate Panel (AA.12.1, AA.11.4) |
| | **D3-37** | Sponsored-listing and display-advertising commercial rules (AA.10.3) |
| Resolutions | **X-59** | Marketplace terminology, schema and flag names reconciled (AA.0.4) |
| | **X-60** | Advocate directory and advocate referral rewards superseded (AA.0.4) |

### AA.0.4 Cross-file resolutions (to be added to master §15)

| # | Topic | Resolution |
|---|---|---|
| **X-59** | "Marketplace" names, schemas and flags | (a) P03 §4.6 FR-P03-31 "Find a Neutral: direct hire" is an **institutional** flow on surface (i): a party requests a named Equator panel neutral for an **Equator-administered** mediation; 0% panel administration fee (Appendix B §B.7.7 row 1); renamed **"Request this panel neutral"**; `MarketplaceBookingWorkflow` renamed `PanelDirectRequestWorkflow`; case `source` value `panel_direct_request` with `marketplace` kept as a legacy alias for existing rows. (b) The words "Equator Marketplace" and "Private Practice Marketplace" refer only to surface (ii); a matter created from a surface (ii) booking has `source = 'private_marketplace'` and lives in the provider's Chambers tenant. (c) Appendix B §B.7.7 row "Marketplace booking (non-administered) 15%" is applied through the plan-dependent take (Appendix O O-R2; master X-31) on surface (ii) only, and only to non-advocate providers. (d) P09 FR-P09-36 "external-member marketplace" stays an Equator-curated, rotation- and conflict-checked proposal flow; it is not surface (ii) and carries no sponsorship. (e) Canonical schemas are `mkp` (marketplace) and `dir` (registry). Research names `marketplace.sponsorships`, `mkt.sponsorships` and `directory.professional_records` map to `mkp.sponsorship_orders` and `dir.professional_records`; research events `directory.record.*.v1` map to `equator.dir.record.*.v1`. (f) Canonical flag for sponsored placement is `marketplace.paid_placement` (NN-34); `mkt.sponsored_placement` and `marketplace.sponsored_placement` [RA, RB] are aliases and must not be created as separate flags. (g) `chambers.marketplace_listings` (P10 FR-P10-09) remains the anonymised overflow/referral channel between Chambers tenants and Equator; it is not a public surface. (h) Marketplace tax flags keep the Appendix G names `billing.eco_gst_tcs` (LR-TAX-008) and `billing.eco_withholding` (LR-TAX-007) (master §15 precedence: Appendix G before other appendices); Appendix AB §AB.8 uses the same names; `tax.eco_gst_tcs` and `tax.eco_tds` (Appendix B §B.10, Appendix W §W.4.9, Appendix V J-159) are registered aliases only and must not be created as separate flags. Marketplace commercial keys follow Appendix AB §AB.8: `marketplace.paid_placement.max_slots_per_page`, `marketplace.take_rate.<plan>`, `marketplace.take_rate.service_providers`, `marketplace.advocate_neutral.flat_fee_minor`, `marketplace.client_processing_fee`, `mkp.provider_subscriptions` (stream RS-57). The display-advertising flag is `platform.rev.ads.enabled` (Appendix AB, stream RS-25); `cms.display_ads` (earlier drafts) is an alias. Invoice and payout lines carry the column `stream_code` (FK `rev.streams(code)`, Appendix AB §AB.9). |
| **X-60** | Advocate directory and referral rewards | (a) Appendix R §4.8 public route `/advocates`, table `core.advocate_listings` and flag `advocate_directory.enabled` are **superseded** by the Professional Registry (AA.12) and the in-case Post-Resolution Professional Chooser (AA.11). Public advocate search exists only behind `directory.public_professionals` = OFF (NN-39). `core.advocate_listings` becomes a read-only view over `dir` for migration. (b) Appendix O deny-list X-11 ("non-cash credits only") and [RB] RS-29 ("non-cash referral credits — advocates") are **superseded by NN-34** and master X-62 (Appendix AB): no referral rewards of any kind (cash, credits, discounts, priority) to advocates, CAs, CSs or CMAs [RE C.13; J-107]. RS-29 is registered in AB as **Prohibited**. Master NN-17's last sentence ("credits/co-counsel") is read accordingly. |

### AA.0.5 Status labels used

**ON** live at the phase exit gate. **OFF** built and tested, switched off, with the named approver. **[VERIFY — open: …]** a fact research could not confirm; the value is a governed (G) parameter with a configured fallback.

---

## AA.1 Legal frame and the control each source drives

| # | Source | What it requires (as researched) | Control in this appendix | Status |
|---|---|---|---|---|
| 1 | Advocates Act 1961 ss.29, 30, 33, 45, 45A; BCI Rules Part VI Ch. II r.36 and the 2008 Schedule (BCI Resolution 50/2008); r.37; Ch. II r.20; Ch. III r.2 [RE F1.1–F1.2] | Advocates may not solicit or advertise directly or indirectly; website information limited to the five Schedule items (name; address, telephone, e-mail; enrolment number, date, State Bar Council and Bar Association; qualifications; areas of practice); no fee-sharing or remuneration-sharing with non-advocates; no contingency fees; no use of the advocate's name to aid unauthorised practice | Advocates only on surface (iii); field allow-list = Schedule (CI `R36_PROFILE_ALLOW_LIST`); never paid placement, ratings, fees, featured labels, referral rewards, per-lead fees; tariff lint blocks `advocate_commission`, `advocate_listing_fee`, `advocate_lead_fee`; public search OFF | r.36 Schedule verbatim text **[VERIFY — open: Gazette text of Resolution 50/2008; Ch. III r.2 official text]** |
| 2 | *P.N. Vignesh v Chairman and Members, BCI* (Madras HC, 3 Jul 2024); BCI cease-and-desist notices July 2024; *Sulekha.com v P.N. Vignesh*, SLP (C) 25794/2024 (notice 13 Nov 2024, no stay reported); *Anil Pandey v BCI*, WP (C) 817/2026 [RE F1.3] | Platforms aggregating lawyer profiles for engagement were held to be soliciting; no IT Act s.79 safe harbour for such listings; Supreme Court question pending | `directory.public_professionals` OFF until counsel's written opinion **and** the SLP is decided; tenant-private panel register is the default form | Pending (watch item AA-OI-01) |
| 3 | ICAI Ethical Standards Board announcement (23 Oct 2019) and Website Advisory (14 Oct 2020); ICSI Advertisement Guidelines 2020; ICMAI Advertisement Guidelines 2025 [RE F1.5] | CAs may not list on app-based aggregators; CMAs may not list services on aggregator sites or join referral networks; CS websites are advertisements | Separate flags `register.ca`, `register.cs`, `register.cma` (all OFF); when ON: uniform, alphabetical, verification-only entries in tenant registers only | ICMAI Gazette date and ICSI aggregator position **[VERIFY — open]** |
| 4 | Mediation Act 2023 ss.38(e), (f), (i), (j), (l) and 41(a), (d); MCI established 27 Aug 2026 [RE F2.1] | MCI to lay down standards of conduct for mediators and mediation service providers; MSPs accredit mediators and maintain panels | Watch item: MCI conduct standards could restrict advertising or paid visibility; sponsored placement auto-suspends for mediators if a published standard prohibits it (G-tier rule pack `rulepack.IN.mkp.mci_conduct`) | Regulations not yet made |
| 5 | A&C Act 1996 ss.11, 12(1), 12(3), 12(5), 18 and Fifth to Seventh Schedules; *CORE v ECI-SPIC-SMO-MCML* (SC, 8 Nov 2024) [RE F2.2] | Equal treatment applies at appointment; unilateral appointment invalid; curated panels do not cure it; justifiable doubts arise from commercial relationships | Paid status never readable by allocation (`NO_PAID_PLACEMENT`); sponsor's s.12(1) disclosure includes "I pay Equator for marketplace visibility"; repeat-player arbitration bookings blocked on surface (ii); enterprise neutral procurement blocked | In force |
| 6 | Consumer Protection (E-Commerce) Rules 2020 rr.4, 5, 6, 7 [RE F3.1; Appendix O §6.3] | Grievance officer (acknowledge 48 h, redress one month); no pre-ticked consent; seller details before purchase; ranking parameters explained; price breakup | Marketplace grievance officer and clocks; seller panel on every profile and checkout; `/marketplace/how-ranking-works`; explicit booking confirmation | In force |
| 7 | Consumer Protection (E-Commerce) (Amendment) Rules 2026 (notified 9 Sep 2026; commencement 1 Jan 2027 per one source) [RE F3.1; RA F10] | Ranking parameters in descending order of significance (r.5(3)(f)); no search manipulation (r.4(11)(c)); sponsored listings clearly and prominently identified (r.4(12)); annual dark-pattern self-audit with displayed certificate (r.4(15)); complaint copy to complainant; NCH convergence; seller website, e-mail, GSTIN; no self-preferencing of related sellers (r.5(6)); no bundled fees (r.5(7)) | AA.5, AA.8, AA.10 controls; "Related to Equator" label; ranking code versioned and governed | Commencement date and sub-rule numbers **[VERIFY — open: Gazette text]** |
| 8 | CCPA Misleading Advertisements Guidelines 2022; Dark Patterns Guidelines 2023 [RE F3.2] | Truthful, substantiated claims; material connections disclosed; no disguised advertisement, false urgency, nagging, drip pricing | Claims Register on every marketplace number (NN-17); copy lint; sponsored label; no countdowns or "most booked" nudges | In force |
| 9 | IT Act 2000 s.79; IT Rules 2021 r.3; IT Rules amendment G.S.R. 120(E), 10 Feb 2026 (7-day grievance disposal; 3-hour takedown for specified content) [RE F3.3] | Intermediary due diligence for user-generated content (bios, reviews); grievance and takedown timelines | Takedown queue with 3-hour and 7-day clocks; published content policy | In force [P] |
| 10 | CGST Act ss.2(45), 24(x), 52; Notification 15/2024-CT (TCS 0.5% from 10 Jul 2024); GST FAQs Q14–Q15 (no TCS on exempt or RCM supplies); Notification 13/2017-CT(Rate) entries 2–3 (RCM for advocates and arbitral tribunals to business entities) [RE F3.4] | E-commerce operator collecting consideration must register and collect TCS on taxable forward-charge supplies; GSTR-8 monthly | Marketplace tax engine (AA.7.3); gate `tax_memo.mkp_eco_recorded` | Applicability to split-settlement model **[VERIFY — open: tax memo, LR-TAX-008]** |
| 11 | Income-tax Act 2025 s.393(1) Table Sl. 8(v) (successor of s.194-O), effective 1 Apr 2026 [RE F3.4] | 0.1% TDS on gross amount facilitated by an e-commerce operator; ₹5 lakh threshold for resident individuals/HUFs furnishing PAN or Aadhaar | Withholding engine (AA.7.4) | Interaction with payer TDS **[VERIFY — open: LR-TAX-007]** |
| 12 | DPDP Act 2023 ss.3(c)(ii), 5, 6, 7(a), 8(1)–(3), 8(7), 11–13; DPDP Rules 2025; substantive duties from 13 May 2027 [RE F4] | No reliance on the "publicly available" exemption; consent after notice; accuracy where data is disclosed to another fiduciary; erasure on withdrawal incl. by processors | Registry consent per purpose; freshness clocks; propagation ≤ 72 h; no bulk import | Build to DPDP now (NN-15) |
| 13 | Companies Act 2013 ss.2(76), 184, 188; G.S.R. 464(E) [RE F5.2] | Group-company shared services and data-sharing with consideration are related-party transactions unless ordinary course and arm's length | GDSA and registry service agreement logged in the shared-services register with s.188 reference | Shareholding chain **[VERIFY — open: CS]** |
| 14 | Legal Services Authorities Act 1987 s.12 (Appendix R §4.8) | Free legal aid for eligible persons | DLSA/SLSA option shown first in every post-resolution chooser for individuals | In force |
| 15 | RBI Payment Aggregator Directions (15 Sep 2025); NN-13 | Settlement sums never through Equator's merchant account | Marketplace collects only provider fees and Equator's own fees; settlement sums stay on the escrow rail (P05) | In force |

---

## AA.2 Architecture: three surfaces, one registry, no join path

### AA.2.1 Surfaces

| Property | (i) Equator Neutral Directory | (ii) Private Practice Marketplace | (iii) Professional Panel Register |
|---|---|---|---|
| Route | `/neutrals`, `/neutrals/{slug}` (Appendix N §2.5) | `/marketplace`, `/marketplace/{category}/{slug}`, `/marketplace/how-ranking-works` | Inside the tenant app only: `/app/panels/*`; nothing public while `directory.public_professionals` = OFF |
| Who is listed | Equator-empanelled neutrals | (a) Private ADR Chambers tenants; (b) independent **non-advocate** neutrals (retired judges who are not practising advocates, CA/CS/CMA neutrals only where their institute flag permits, other professionals); (c) ancillary ADR service providers (AA.3) | Advocates, CAs, CSs, CMAs (and, as tenant-private vendor entries, valuers and process agents a tenant empanels) |
| Who books or engages | Equator appoints under the published allocation policy; parties may request a panel neutral for administered mediation (X-59 (a)) | The party (or both parties jointly) books directly; the matter is **not** administered by Equator | The tenant (lender, enterprise, Chambers) engages its own professionals for its own matters |
| Data owner (DPDP) | Equator | Provider is a seller; Equator is the marketplace e-commerce entity and fiduciary for marketplace accounts; the Chambers tenant is fiduciary for its case data (Appendix N §8.5 cl. 1) | Registry owner (D3-05) for master records; each consuming tenant for its own panel and engagement data |
| Paid placement | **Never** (D2-14 retained; NN-28) | Only sponsored slots under NN-34, flag `marketplace.paid_placement` OFF | **Never** |
| Ratings / reviews | Process ratings under Appendix N §7 (n ≥ 10) | Process-only reviews for non-advocate neutrals and service providers (AA.8.1) | **Never** (tenant-private performance notes only, never shared) |
| Ranking | Seeded-random or alphabetical (N §2.5) | Published parameters in descending order of significance (AA.5.3) | Alphabetical or seeded-random |
| Indexing | Indexable | Indexable (profiles server-rendered) | `noindex`; no SEO pages |
| Schema | `core` (neutrals) | `mkp` | `dir` (group registry service) |

### AA.2.2 Isolation rules (L — Locked)

1. **No join path.** The database roles used by the allocation service, grading jobs, Quality Index job, conflict engine and the institutional directory projection have **no grant** on any `mkp` table and **no access to `dir` at all** (the registry runs in a separate cluster with no Equator database credentials, AA.2.3); the only registry-derived input is the F2 conflict-signal edge written to `core.conflict_edges` from `equator.dir.panel_membership.*` events (rule 4). The `mkp` service role has no grant on `core.allocation_runs`, `core.appointments`, `core.neutral_grades`, `core.quality_index_snapshots`, `core.neutral_scorecards`, `core.neutral_reviews` or `core.cases`. CI test `MKP_SURFACE_ISOLATION` parses migrations and service code and fails on any cross-surface SQL, view, foreign key or service call not in the allow-list (rule 4).
2. **`NO_PAID_PLACEMENT` extended.** The existing test (Appendix N §2.5; Appendix O RA-4) additionally fails on any read path from `mkp.sponsorship_*`, `mkp.ad_*`, `mkp.provider_subscriptions` or any `rev` table to `directory.neutral_public_view`, the allocation service, eligibility, grading, Quality Index or conflict checks (NN-34).
3. **No sponsorship visibility to case roles.** Sponsorship status is never exposed to `case_manager`, `registrar`, `deputy_registrar`, Panel Bench, APPT or CHAL members, or the AI Gateway prompt context; Cerbos `DENY` on resource `mkp:sponsorship` for those roles.
4. **Allowed cross-surface flows (exhaustive allow-list `config/mkp_flow_allowlist.yaml`):**
   | Flow | From → To | Payload | Purpose and basis |
   |---|---|---|---|
   | F1 Identity | `core.persons` ↔ `mkp.providers.person_id`, `dir.professional_records.person_ref` | Opaque person reference only | One login per person (Appendix S §1); the person links accounts themselves |
   | F2 Conflict signal | `dir.panel_memberships` → `core.conflict_edges` (edge type `counsel_panel_of`) | `person_ref`, `organisation_id`, `since`, `until` | Seventh Schedule-style screening [RA EQM-15]; registry consent purpose `conflict_screening` (AA.12.4) and GDSA clause; **no performance data, notes or engagement details** |
   | F3 Conflict signal | `mkp.engagements` (closed) → `core.conflict_edges` (edge type `privately_engaged_by`) | `person_ref`, `organisation_id`, `engaged_on` | Same; marketplace terms disclose it |
   | F4 Sponsorship disclosure | `mkp.sponsorship_orders` (active or within 24 months) → `core.neutral_disclosures` prompt | Boolean `has_paid_visibility_24m` and period | s.12(1) disclosure text (AA.10.7); never visible to allocation |
   | F5 Blind conflict check | Provider tenant → `POST /v1/conflicts/blind-check` (P03 FR-P03-32) | Salted hashes | Existing pattern |
5. **Group boundary (NN-38).** No `mkp` or `dir` table contains case data from Equator-administered matters. Case and allocation data are never sent to Finbyx, Udofin or LawDocs. Lender-side panel performance data never enters Equator's neutral systems (CI test `GROUP_SHARE_SCOPE`).

### AA.2.3 Deployment topology

| Component | Deployed as | Database | Owner entity |
|---|---|---|---|
| `mkp` module | NestJS module in `apps/api` (Equator) | Equator Aurora cluster, schema `mkp`, tenant RLS | Equator Resolution Service Private Limited |
| `dir` service | NestJS module packaged as a standalone service `services/registry` (same monorepo conventions) deployed in the registry owner's AWS account (ap-south-1; DR ap-south-2) | Dedicated Aurora cluster `grp-registry`, schema `dir`, RLS by `consumer_entity_id` and `tenant_ref` | Entity designated by the Board (D3-05; D3-36) |
| `REGISTRY_PORT` | Adapter in each consumer (Equator, Finbyx, Udofin, LawDocs) | Local projection tables only for fields that consumer is entitled to (cache TTL ≤ 24 h, invalidated by events) | Each consumer |

Equator has **no privileged direct access** to the `grp-registry` database even if Equator is designated owner; Equator's product uses the registry through `REGISTRY_PORT` like any other consumer, with its own consumer registration and purposes. Registry administration (verification, DSR handling) is done in the registry admin console by `registry_steward` and `registry_verifier` roles of the owner entity.

### AA.2.4 Decision D3-35 — operating model of the Private Practice Marketplace

1. Equator operates surface (ii) as a **marketplace e-commerce entity** under the E-Commerce Rules 2020 for every category, without relying on the *D.K. Gandhi* carve-out [RE F3.1 default].
2. A neutral or chambers listing on surface (ii) must hold an active Chambers workspace (any plan from CH-LITE; Appendix O §2.8). A booking creates the matter **in the provider's Chambers tenant**, which is the administering institution (or the neutral acts ad hoc) and fiduciary for case data; Equator is processor (Appendix N §8.5 cl. 1).
3. Ancillary service providers hold a **provider workspace** (`mkp.providers.kind = 'service_provider'`) without case administration; they receive only the documents a party authorises (AA.6.8).
4. Equator's percentage take applies only to bookings of **non-advocate** providers (NN-34; RE C.15). Where the provider is an advocate (for example an advocate-neutral, if ever listed under AA.3.2 rule 4), Equator charges no take, no listing fee and no placement fee, and nothing is deducted from the advocate's fee; Equator's own services on that booking carry the flat fee `marketplace.advocate_neutral.flat_fee_minor` (RS-18 `flat_per_booking`; master X-62(d)), charged to the buyer as a separate line and identical whatever provider is chosen (RE F1.4(d)).
5. Payment collection model (`platform.mkp.collection_model`, G): `provider_merchant_of_record` (default; the Chambers tenant's own Razorpay Route linked account is merchant of record and Equator's fee is split at source, Appendix N §8.3) or `equator_collects_as_eco`. In either mode, marketplace paid bookings stay disabled until the tax memo records the e-commerce operator position for GST TCS and income-tax TDS (`tax_memo.mkp_eco_recorded = true`; LR-TAX-007, LR-TAX-008). The tax engine supports both outcomes (AA.7).
6. Settlement sums between parties never pass through the marketplace (NN-13).

---

## AA.3 Provider categories, eligibility and law checks (surface (ii))

### AA.3.1 Category register (`mkp.provider_categories`, G — Governed)

Each category is a governed rule-pack object `rulepack.IN.mkp.category.<code>@<version>` holding eligibility, required evidence, verification method, re-verification cycle, the law check and display limits. A category goes live only when its law check is signed off by `legal_reviewer` (maker `marketplace_manager`, checker `legal_reviewer`). Categories marked OFF ship disabled.

| Code | Category | Eligibility floor (Equator; tenants may add, never lower) | Required evidence and verification | Law check (what the reviewer confirms) | Reviews | Sponsor-eligible (NN-34) | Take applies | Default |
|---|---|---|---|---|---|---|---|---|
| `NEU-MED` | Independent mediator (non-advocate) | 40 hours of mediation training from any recognised provider (Appendix N §9.2); Code acceptance (ECC-2026.1 or equivalent, N §8.3); no open S1/S2 complaint; no income test [RA EQM-05] | Training certificate (verify endpoint or issuer e-mail); KYC; declaration of profession | Not an advocate on any State roll (declaration + roll check by staff, AA.4.3); MCI registration shown only when `mci_regs_in_force` ON | Yes | Yes | Yes | ON |
| `NEU-ARB` | Independent arbitrator (non-advocate) | Verifiable professional basis (Appendix N §2.3 `experience_basis`), ≥ 10 years for sole arbitrator in commercial matters (G; tenant may raise); Seventh Schedule self-check | Basis evidence; two references | Not an advocate; A&C s.12(1) disclosure template accepted | Yes | Yes | Yes | ON |
| `NEU-CON` | Conciliator | As `NEU-MED` | As `NEU-MED` | A&C Part III | Yes | Yes | Yes | ON |
| `NEU-EXD` | Expert determiner / technical expert neutral | Professional qualification in the field (engineer, valuer, accountant) | Membership / registration certificate | Institute rules of the expert's profession (for CA/CS/CMA see AA.3.2 rule 3) | Yes | Yes (non-institute members only) | Yes | ON |
| `NEU-JUD` | Retired judge (not practising) | Retirement order; not enrolled as practising advocate since retirement | Retirement order; staff roll check | Honorific "Justice (Retd.)" only for retired SC/HC judges, verified (Appendix N §2.3); "Senior" lint (master X-26) | Yes | Yes | Yes | ON |
| `CHM` | Private ADR Chambers (institution or group) | Active Chambers tenant; adopted code; ≥ 1 verified neutral per enabled mechanism (Appendix N §8.4) | KYB (PAN, GSTIN, CIN/LLPIN/registration); authorised signatory | Name/label validator (no "court"; Emblems and Names Act 1950 check, N §8.1); if a law firm or any listed neutral is an advocate → AA.3.2 rule 4 | Yes (chambers-level, process only) | Only if no advocate is listed under it and it is not a law firm | Yes, except on advocate neutrals' bookings | ON |
| `SVC-TRN` | Translator | Language pair proficiency evidence; for certified translation, the certifying basis (Appendix L §7) | Certificate / sample test | Derived-text labelling NN-32; confidentiality undertaking | Yes | **No** | Yes | ON |
| `SVC-INT` | Interpreter, incl. Indian Sign Language | Proficiency evidence; for ISL, recognised ISL certification **[VERIFY — open: certifying bodies list]** | Certificate | Confidentiality; neutrality undertaking in hearings | Yes | No | Yes | ON |
| `SVC-STN` | Stenographer / transcriptionist | Speed and accuracy test or certificate | Test result | NN-11: mediation never recorded or transcribed by default; arbitration only with consents | Yes | No | Yes | ON |
| `SVC-PRC` | Process agent (delivery of notices and proof of delivery) | Registered business; delivery SOP | KYB; SOP upload | May deliver arbitral and contractual notices only (A&C s.3); may **not** hold out as serving court process or as court staff; **recovery or collection agents, DSAs and lender-side staff are excluded** (NN-12; Appendix S §4.7) | Yes | No | Yes | ON |
| `SVC-EST` | e-stamp facilitation vendor | Authorised collection centre or authorised agent of the State's e-stamping system **[VERIFY — open: per-State authorisation evidence; SHCIL ACC status]** | Authorisation letter per State | State stamp law (NN-09); Equator's own e-stamp rail (ESTAMP_PORT) remains the default in Equator flows | Yes | No | Yes | OFF until per-State evidence model is signed off |
| `SVC-VAL` | Valuer | Registered valuer for the asset class where the law requires registration **[VERIFY — open: Companies Act 2013 s.247 and the Registered Valuers Rules 2017 scope; SARFAESI valuer requirements]** | Registration certificate | Valuation is not legal advice and not a neutral's decision; AI never estimates value (NN-01 GX-3) | Yes | No | Yes | ON |
| `SVC-EXP` | Expert witness (forensic, handwriting, medical, technical) | Qualification in the field | Certificate / registration | Expert opinion under BSA 2023 (as applicable) is party-commissioned; never presented as Equator's view | Yes | No | Yes | ON |
| `SVC-VEN` | Venue / hearing-room provider | Premises with accessibility statement; safety | KYB; photos; accessibility checklist | Shops and establishments registration **[VERIFY — open: per State]**; venue never implies Equator administers (RS-17 copy rule) | Yes | No | Commission per RS-17 | OFF (RS-17 OFF) |
| `SVC-TRG` | Trainer / training provider | Organisation identity, published hours and assessment (Appendix N §9.6) | KYB; course outline | Training neutrality (master X-29): no advantage in empanelment; picker shows ≥ 3 providers; Equator ADR Institute shown only with "Related to Equator" label and `academy.institute_referral` ON | Yes | No | Yes | ON |
| `SVC-VHR` | Virtual hearing-room hosting (Equator's own RS-16 product, not a third-party seller) | — | — | Branded "Room hosted on Equator"; never implies administration | — | — | n/a (Equator's own supply) | ON after P04 GA |

**Excluded categories (L):** recovery or collection agents; DSAs and loan service providers; "case-winning" consultants; anyone offering legal advice who is not an advocate (Advocates Act s.33; Appendix O X-01); paid-review or testimonial services; any category whose listing would be an unregistered intermediary in a regulated activity (insurance claim "preparation", Appendix O X-16).

### AA.3.2 Advocates, CAs, CSs and CMAs on surface (ii) (L)

1. **Advocates as advocates** are never listed on surface (ii). They appear only on surface (iii) (AA.12) and, when enabled, the in-case Post-Resolution Professional Chooser (AA.11).
2. **CA, CS and CMA members as professionals** are never listed on surface (ii) (ICAI 2019 aggregator bar; ICMAI 2025 aggregator bar; ICSI treated equivalently [RE F1.5]).
3. **CA, CS or CMA members acting only as neutrals** (`NEU-MED`, `NEU-ARB`, `NEU-EXD`) may list only while the institute flag for that profession (`marketplace.institute_neutral.ca|cs|cma`, G, OFF) is ON after an institute opinion is on file; while ON they get a uniform entry: no fee display, no reviews, no sponsorship.
4. **Advocate-neutrals** (an enrolled advocate acting as mediator or arbitrator) may list only if `marketplace.advocate_neutrals.listing` (G, OFF; approver: counsel opinion on OI-03 recorded in the legal-flag register) is ON. While ON: Schedule fields plus neutral roles only; no photo or video; no reviews; no fee display other than "Fees on request"; no sponsored slot (`marketplace.paid_placement.advocates` is **L OFF** in v3.0); no take on their bookings (AA.2.4 rule 4).
5. The provider's professional status is captured at application (`declared_professions[]`) and checked by staff against official sources (AA.4.3). A false declaration is an S1 marketplace complaint ground (AA.8.3).

### AA.3.3 Related-to-Equator providers (E-Commerce r.5(6) as amended)

Any provider that is a group company, controlled by a director, shareholder or employee of Equator or of an Infrabyx group company, or the Equator ADR Institute, carries `related_to_equator = true` (set at onboarding by `compliance_officer` from the related-party register; CS confirms). Effects (L): label "Related to Equator" on cards and profile; no ranking advantage (ranking code ignores the attribute except to apply the label); no use of platform data to favour it; it may not buy sponsored slots unless `marketplace.related_party_sponsorship` (G, OFF; approvers Board and counsel) is ON; transactions with it are logged for the s.188/AOC-2 process (Appendix O §2.10).

---

## AA.4 Provider onboarding, verification, quality and offboarding

### AA.4.1 Journey and service levels

| # | Step | `mkp.providers.status` | Actor | What happens | Equator SLA |
|---|---|---|---|---|---|
| 1 | Apply | `draft → submitted` | Applicant | Choose category(ies); identity sign-in (Appendix S §3, level per category: K2 individual, KYB for organisations); declarations (professions held, related-party, conflicts, no disciplinary order, no criminal conviction for offences involving fraud **[VERIFY — open: wording, counsel]**); DPDP notice; per-field display consents | Acknowledge ≤ 2 working days with `EQ/MKP/{YYYY}/{NNNNN}` |
| 2 | KYC / KYB | `kyc_pending ⇄ info_requested` | Applicant; `provider_verifier` | PAN (and GSTIN where registered), Aadhaar only via OVSE/DigiLocker (NN-14), MCA21 KYB for companies/LLPs, bank account penny-drop (Appendix S §3.11), sanctions screen for foreign providers | ≤ 5 working days |
| 3 | Credential verification | `verifying` | Two `provider_verifier`s (different users) | Category evidence (AA.3.1); professional-status check (AA.4.3); references for neutrals; result per credential with source, method, verified date, valid-until | ≤ 10 working days from complete documents |
| 4 | Agreement | `agreement_pending` | Applicant | E-sign the Marketplace Provider Terms `MPT-2026.1` and the Provider Code of Conduct `MPC-2026.1` (AA.13); for neutrals also ECC-2026.1 or adopted code | — |
| 5 | Payout and tax setup | `payout_setup` | Applicant; `finance_ops` | Payee account (penny-drop name match); GST registration status (registered / unregistered / composition); PAN-Aadhaar link status for the TDS threshold (AA.7.4); TDS certificate e-mail; for Chambers, the Razorpay Route linked account (Appendix N §8.4) | ≤ 3 working days; bank detail change rules AA.7.6 |
| 6 | Profile build | `profile_draft` | Applicant | Profile through the Chambers page builder (**Appendix W**) or the provider profile form; allow-list per category (AA.5.4); service offerings with fee model; availability; languages; service area | — |
| 7 | Review and go-live | `profile_review → listed` | `marketplace_moderator` | Copy lint (claims, "top/best/expert", outcome claims, "court"), image checks, fee-model completeness, seller-detail completeness (E-Commerce r.5(3)(a), r.6(5)(j)) | ≤ 3 working days |
| 8 | Quality monitoring | `listed` | System; `marketplace_moderator` | AA.4.5 signals | Continuous |
| 9 | Re-verification | `listed` (badge states) | System; verifiers | Credential expiry T-30/T-7; annual re-verification; profile reconfirmation every 12 months (stale label) and hide at 18 months | — |
| 10 | Suspension / offboarding | `suspended`, `delisted`, `withdrawn`, `closed` | Provider; `marketplace_manager`; Marketplace Review Panel | AA.8.4 due process; run-off of open engagements; export (AA.21) | — |

Additional states: `rejected` (reasons; re-apply after 6 months), `paused` (information request unanswered 14 days), `archived` (draft older than 90 days). Every transition writes audit and emits `equator.mkp.provider.status_changed.v1`.

### AA.4.2 State machine (`mkp.providers.status`)

```
draft → submitted → kyc_pending ⇄ info_requested → verifying ⇄ info_requested
      → agreement_pending → payout_setup → profile_draft → profile_review → listed
listed → suspended → (listed | delisted)        listed → withdrawn (by provider) → closed
any pre-listing state → rejected | paused | archived
delisted → closed (after run-off and appeal window)
```

Guards: `listed` requires every category credential `verified` and unexpired, agreements signed, payee verified, tax profile complete, profile passed moderation, and (neutrals/chambers) an active Chambers workspace. Loss of any guard moves the affected category listing to `hidden` with reason (other categories stay listed).

### AA.4.3 Professional-status check (anti-circumvention)

To enforce AA.3.2, staff check whether an applicant for a neutral category is an enrolled advocate or an institute member. Method (L): manual, staff-assisted look-up against the official portal for the State or institute the applicant names **and** a declaration; screenshot, URL and timestamp captured as evidence with SHA-256 hash; two-person review. **No scripted querying or scraping of Bar Council rolls or institute directories** (NN-39; CI lint `NO_ROLL_SCRAPING` blocks scheduled jobs and HTTP clients targeting configured roll-portal hosts) [RE F4.2, D.19].

### AA.4.4 Onboarding for organisations

KYB per Appendix S §3.6; authorised signatory with authority letter or Board resolution; for chambers, the Chambers tenant must already exist (P10 onboarding §8.4) and the chambers admin links it. Multiple users per provider: `mkp_provider_owner` (one or more), `mkp_provider_staff` (bookings, messages, calendar; no payout or bank changes).

### AA.4.5 Quality monitoring signals (process-only)

| Signal | Threshold (T-tier, within L bounds) | Action |
|---|---|---|
| Response time to enquiries | Median > 2 working days over 30 days | Nudge to provider; badge "Usually responds within {n} days" recomputed |
| Acceptance-then-cancellation by provider | ≥ 2 in 90 days | Moderator review; cancellation symmetry refund to buyer (Appendix O §6.3) |
| Complaint rate | ≥ 3 complaints in 12 months, or any S1 | Review; S1 interim suspension (AA.8.3) |
| Review "pressured to settle" (neutrals) | Any "Yes" | Quality review ticket (Appendix N §7.5 pattern) |
| Credential expiry | Expired | Category hidden automatically |
| Fee-model drift | Invoice exceeds disclosed fee model without buyer approval | Booking hold; refund of the excess |
| Disintermediation attempt (soliciting off-platform payment before booking) | Detected by message lint or report | Warning; repeat → S2 |

Outcome metrics (settlement rates, award outcomes, who won) are never computed for or used against providers (L; lint `MKP_OUTCOME_METRIC_FORBIDDEN`).

### AA.4.6 Offboarding

Provider withdrawal or delisting: new enquiries stop immediately; open engagements continue under run-off (90 days, Appendix N §8.3) or are transferred with the buyer's consent; payouts for delivered milestones continue; reviews remain displayed with "Provider no longer listed" (no deletion by the provider); the provider receives a full export (AA.21); personal data is erased 30 days after run-off ends unless retention is required (tax records 8 years per Appendix Q retention schedule **[VERIFY — open: final retention schedule]**).

### AA.4.7 Onboarding progress score, next best action and staff queue *(v3.1)*

1. **Progress score (0–100).** `onboarding_progress()` (pure function in `packages/rules/mkp-onboarding`, golden vectors) sums the weights of completed steps, with partial credit inside a step in proportion to items done (for example 2 of 3 credentials verified = two-thirds of the credential weight). Default weights (`platform.mkp.onboarding.weights`, T within the L rule that the weights total 100):

   | Step (AA.4.1) | Weight | Counts as done when |
   |---|---|---|
   | 1 Apply (declarations, consents) | 10 | `submitted` |
   | 2 KYC / KYB | 15 | KYC tasks passed |
   | 3 Credential verification | 25 | every required credential `verified` (two-person) |
   | 4 Agreements | 10 | MPT, MPC (and ECC) signed |
   | 5 Payout and tax setup | 15 | payee verified, tax profile complete (cooling-off may still run) |
   | 6 Profile build | 15 | every category-mandatory field present and lint-clean |
   | 7 Review | 10 | moderation passed |

   The score, the blocking items and an **estimated listing date** (sum of the remaining Equator SLAs in AA.4.1, in working days from today) are shown on the applicant tracker (SCR-P19-10) and on the staff queue. The score is an onboarding aid only: it is never read by ranking, sponsor eligibility, reviews or badges (L; covered by `RANKING_IGNORES_PAID`).
2. **Next best action.** The tracker shows one primary action for the applicant ("Upload your mediation-training certificate", "Sign the Provider Terms", "Confirm your bank account"), deep-linked to the field. Information the applicant already gave in their own Equator identity profile (name, verified mobile and e-mail, KYC level; Appendix S §3) or, for chambers, in the Chambers tenant's KYB is **pre-filled through the applicant's own session** and shown for confirmation; it is never read by `mkp` service roles from `core` neutral tables (AA.2.2 rule 1).
3. **Reminders without nagging.** For steps waiting on the applicant: reminders on working days 3, 7 and 12 after the step opened, then none (at most 3 per step; one-click "pause reminders"); day 14 moves the application to `paused` as today (AA.4.1). No countdown or scarcity wording (Dark Patterns 2023).
4. **Staff queue (deadline-aware).** SCR-P19-19 orders work items by SLA due time, then by score (highest first, so nearly complete applications finish first); filters by step, category, verifier and age; bulk actions for moderators (assign, request the same missing document from several applicants with one template, approve lint-clean profiles one by one with a mandatory per-item confirmation — no bulk approval of credentials, which stay two-person); an item at 80% of its SLA turns amber and at 100% escalates to `marketplace_manager`.
5. **KPIs.** Median submitted → `listed` ≤ 15 working days; first-submission completeness (all documents at step 1) ≥ 60%; drop-off rate per step (reported monthly, by category); SLA attainment per step ≥ 95%. Events: `equator.mkp.provider.onboarding_progressed.v1` (provider ID, score band, step; no PII).

---

## AA.5 Search, ranking and profiles (surface (ii))

### AA.5.1 Public, no-login search [RA EQM-03]

`/marketplace` is server-rendered and works without login or JavaScript for the first results page. Filters (all optional; facet counts shown only where ≥ 3 results to avoid singling out):

| Filter | Values | Source |
|---|---|---|
| Category | AA.3.1 codes (public names) | `mkp.listings.category_code` |
| Dispute type | Appendix K taxonomy (vertical → L1 category) | Provider's declared areas |
| Method | negotiation facilitation, mediation, conciliation, arbitration, expert determination; for services: translation, interpretation, transcription, notice delivery, valuation, expert report, venue, training | Service offerings |
| Language | 28-language set (master X-33) with proficiency ≥ professional | Verified or declared (badge shows which) |
| Jurisdiction | State, district, seat city; "serves all India online" | Service area |
| Availability | "Can start within 7 / 14 / 30 days"; specific date | Availability engine |
| Fee model | fixed fee, per session, per hour, per page/word, per day, sliding scale (with published bands) | Service offerings |
| Mode | online, in-person, hybrid | Service offerings |
| Verified qualifications | training hours ≥ 40; accreditation bodies (Appendix N §11.4 enum); registration types | `mkp.provider_credentials` (verified only) |
| Accessibility | ISL, screen-reader-friendly documents, wheelchair-accessible venue | Verified checklist |
| Experience | years since verified start date (bands) | Verified start date only |

Compare up to 3 profiles side by side. Search requests carry no personal data; analytics are aggregated (no ad pixels on marketplace pages, NN-16).

**Query relevance *(v3.1)*.** A free-text box ("What do you need help with?") is translated into the filters above, never into a hidden score:
1. The query is matched against a governed synonym and phrase dictionary `mkp.search_synonyms` (G; maker `marketplace_manager`, checker `compliance_officer`; versioned) that maps plain-language and Indic or romanised phrases (English, Hindi and the enabled languages, NN-23) to category codes, Appendix K dispute types, methods and languages — for example "loan settlement" → FIN dispute types + mediation/negotiation facilitation; "translation into Marathi" → `SVC-TRN` + language `mr`. Typo tolerance (edit distance ≤ 2) and transliteration use the same dictionary.
2. Matched terms appear as **removable filter chips** with the text "We searched for: Mediation · Property disputes · Hindi"; the user can remove or change any chip. A query that maps to nothing shows the filter panel, not a guess.
3. The dictionary may never map to a provider name, a provider attribute outside AA.5.1, sponsorship, plan, rating or "best" wording (lint `MKP_SYNONYM_FORBIDDEN_TARGET`); a query containing a provider's name returns that provider's profile link only if the provider is `listed` (exact-name lookup), without changing the order of other results.
4. **Zero-result recovery:** when no provider matches, the page suggests relaxing one filter at a time with the count it would return (shown only where ≥ 3) and links to Equator's administered route and free forums (NN-20); it never suggests a named provider.
5. **Saved searches** (signed-in users, opt-in): the user may save a filter set and opt in to a weekly e-mail when a newly `listed` provider matches (`EMAIL_PORT`; a service message the user asked for, so it carries only the matching listings in organic order — no sponsored slot or promotion (AA.10.3 rule 2); one-click stop; maximum 5 saved searches). Recently viewed profiles are kept on the device only.
6. **KPIs:** zero-result rate ≤ 5% of searches; search → enquiry conversion; median time from first search to first enquiry; chip-removal rate (dictionary quality signal reviewed monthly). Acceptance tests in P19 §12. *(v3.1)*

### AA.5.2 What search never does (L)

- No sort by price low-to-high that hides fee components; price sort uses the **total including GST** of a standard reference engagement per offering.
- No sort or boost by rating, number of bookings, "popularity", revenue, plan tier, sponsorship, related-party status, Equator panel status or Equator grade.
- No "most booked", "trending", countdowns, scarcity badges or "x people are viewing" (Dark Patterns 2023: false urgency, interface interference).
- No AI-generated ranking or recommendation of a named provider (NN-01; [RA EQM-09]). The marketplace assistant explains filters and processes only.
- Search results for a query never show providers that do not match the hard filters (E-Commerce r.4(11)(c) as amended: no manipulation relative to the query).

### AA.5.3 Organic ranking parameters (published; G)

Ranking policy `mkp.ranking_policies` is a governed object (maker `marketplace_manager`, checker `compliance_officer`, legal sign-off), versioned, effective-dated, published at `/marketplace/how-ranking-works` **in descending order of significance** with plain-language explanations (E-Commerce r.5(3)(f) as amended). Default policy `MKP-RANK-2026.1`:

| Order | Parameter | How it works | Weight |
|---|---|---|---|
| 1 | Match to your filters | Only providers meeting every filter you chose are shown | Hard filter |
| 2 | Availability in your window | Providers who can start in the window you chose appear before those who cannot | Tier |
| 3 | Language match | Providers sharing every language you chose appear before partial matches | Tier |
| 4 | Profile completeness and freshness | Profiles with every **category-mandatory** field present (a yes/no test; optional sections such as video, page themes or paid tools never count) and confirmed in the last 12 months appear before others; profiles not confirmed for 18 months are hidden *(v3.1: completeness defined)* | Tier |
| 5 | Random rotation | Within each tier, order is random and changes every session (seeded per session) so no one is always first | Final |

Nothing else affects order. Each result has "Why am I seeing this?" listing the tiers it met. Sponsored slots are **outside** organic results (AA.10). The ranking code lives in `packages/rules/mkp-ranking` and is covered by golden vectors; a change of parameter or order is a governed change with a 30-day public notice and a changelog on the page.

**Sort options the visitor may choose *(v3.1)*.** The default is "Published order" (the table above). The visitor may switch to one of the sorts below; each is defined in `MKP-RANK-2026.1`, published on `/marketplace/how-ranking-works`, applies only **after** the hard filter (order 1), and breaks ties by the session seed. The list is the enum `platform.mkp.search.sort_options` (G; adding an option is a ranking-policy change with the 30-day notice); any other `sort` value returns `MKP_SORT_NOT_ALLOWED` (400).

| Sort | Definition | Never uses |
|---|---|---|
| `published_order` (default) | Tiers 2–5 above | — |
| `earliest_start` | Earliest date the provider can start a first session in the chosen mode, from the availability engine; providers with no availability in 90 days last | Rating, bookings, plan, sponsorship |
| `price_total_asc` | Total including GST of the offering's standard reference engagement (AA.5.2), lowest first; offerings without a reference price last, with "Price on proposal" | Discounts not available to everyone |
| `name_az` | Legal or trade name, locale-aware collation | — |
| `nearest_venue` | Distance from the visitor's chosen district to the provider's declared in-person venue; shown only when mode = in-person | Visitor's device location unless the visitor types or allows it for this search |

The chosen sort is named in every "Why am I seeing this?" popover and in the URL (shareable), and the default is restored on the next visit. Sponsored slots stay in their separate block whatever the sort (AA.10.3 rule 3). `RANKING_IGNORES_PAID` runs its golden vectors under every sort option. *(v3.1)*

### AA.5.4 Profile allow-list per category (L list; per-field display consent T)

| Field | Neutral categories | Chambers | Service providers | Rule |
|---|---|---|---|---|
| Name, honorific (verified) | ✔ | Legal name + trade name | ✔ | Honorific only if verified |
| Photo, short/long bio | ✔ | Logo, description | ✔ | Copy lint; per-field consent; advocate-neutrals: no photo/video |
| Captioned video (≤ 90 s) | ✔ | ✔ | ✔ | Controls, captions and transcript mandatory [RB E.19] |
| Roles / services offered | ✔ | ✔ | ✔ | — |
| Verified badges | ✔ | ✔ | ✔ | Popover: credential, verification method, verified date, valid until; never the document [RA EQM-04] |
| Languages, service area, modes | ✔ | ✔ | ✔ | — |
| Fee model and published fees | ✔ | ✔ | ✔ | Total incl. GST for consumers (NN-29); advocate-neutrals "Fees on request" only |
| Availability indicator | ✔ | ✔ | ✔ | "Usually can start within {n} days" |
| Response-time indicator | ✔ | ✔ | ✔ | Computed (AA.4.5) |
| Process reviews | ✔ (n ≥ 10) | ✔ (n ≥ 10) | ✔ (n ≥ 10) | AA.8.1; not for advocates or institute members |
| Seller details panel | ✔ | ✔ | ✔ | Legal name, registration status, address, customer-care contact, website and e-mail where available, GSTIN/Udyam (E-Commerce r.5(3)(a), r.6(5)(j) as amended) |
| Related-to-Equator label | if applicable | if applicable | if applicable | AA.3.3 |
| Paid-visibility disclosure | if sponsoring | if sponsoring | — | "This provider pays Equator for sponsored listings. Sponsorship does not change their organic order, reviews or badges." |
| Complaint link | ✔ | ✔ | ✔ | `/marketplace/complaints` |
| Institutional statement | ✔ | ✔ | ✔ | Fixed: "Bookings on the Equator Marketplace are private engagements. Equator does not administer them, appoint the provider or guarantee any result." |

**Never displayed (L):** settlement, success or win rates; outcome distributions; amounts recovered; awards upheld; client names or logos without written consent and Claims Register entry; "top", "best", "premium", "recommended", "featured", "expert", "specialist", "No. 1" labels (copy lint `MKP_LABEL_FORBIDDEN`; RB X-18); Equator grade or Quality Index; any statement implying Equator endorses the provider.

### AA.5.5 Freshness

| Age since provider last confirmed profile | Effect |
|---|---|
| ≤ 12 months | Normal |
| 12–18 months | Label "Details last confirmed {date}"; reminder at 11, 12 and 15 months |
| > 18 months | Hidden from search until reconfirmed (record kept) |
| Credential expired | That badge removed; dependent category hidden |

---

## AA.6 Booking journey (surface (ii))

### AA.6.1 End-to-end flow

```
Search → Profile → Enquiry → Provider conflict check → Engagement proposal (scope + fee disclosure)
 → [Counterparty joins, for neutral services] → Explicit booking confirmation → Payment
 → Service delivery on Equator tools → Milestone confirmation → Payout
 → Review invitation → (Complaint / fee dispute) → Close
```

### AA.6.2 Enquiry

- Buyer signs in (Appendix S, level K1 for enquiry; K2 before payment). Enquiry form: service, dispute type, languages, preferred mode and window, counterparties' names (for neutral services; used only for the conflict check), short description (≤ 1,000 characters; PII redaction preview; "do not include amounts or confidential facts").
- Messages run in the platform inbox (`mkp.enquiry_messages`); contact details may be exchanged after confirmation. Message lint flags off-platform payment requests (AA.4.5) but never blocks a buyer from contacting a provider directly outside Equator (no lock-in).
- Provider response clock: 2 working days (T-tier); auto-expiry at 7 days with a polite notice to the buyer suggesting other providers (no nagging; one notice).

### AA.6.3 Conflict check

- **Neutral and expert categories:** the provider runs a conflict check before proposing an engagement. Inputs: counterparties and their representatives as entered by the buyer. Method: provider's tenant conflict graph (P10) plus the Equator blind check `POST /v1/conflicts/blind-check` (salted hashes; returns `clear | disclosable | hard`; P03 FR-P03-32). A `hard` result blocks the proposal (`MKP_CONFLICT_HARD`). A `disclosable` result requires a written disclosure to every party before booking (A&C s.12(1) and Sixth Schedule format for arbitrators; Code disclosure for mediators).
- **Group relationships (NN-16 extended):** if any party is a client of an Infrabyx group company (Finbyx, Udofin) or of Equator under an enterprise contract, the counterparty sees the relationship notice (`CommercialRelationshipNotice`; Appendix O RA-7) before booking.
- **Panel-counsel edges (AA.2.2 F2):** a provider who is on a lender's professional panel is blocked as neutral in any booking involving that lender (`MKP_CONFLICT_HARD`, reason `counsel_panel_of`).
- **Service categories:** a lighter declaration ("I have no relationship with the other side") is recorded.
- **Re-check before payment *(v3.1)*.** A conflict result is valid only for the party set it was run on and for `platform.mkp.conflict_check.validity_days` (G, default 14, bounds 7–30). It is re-run automatically, before any payment can be taken, when (a) a counterparty joins and names representatives, an organisation or group entities not in the original enquiry, (b) the buyer edits the counterparties, or (c) the result is older than the validity period. If the re-check returns `hard`, the engagement moves to `conflict_blocked`, any held payment is refunded in full automatically (P05 refund activity, idempotent), and the buyer is offered the search again with the same filters; if it returns `disclosable` where it was `clear`, a disclosure step is inserted and every party must acknowledge it before the "Confirm and pay" button is enabled. The provider sees only the result and the reason code, never the counterparties' hashes.

### AA.6.4 Booking guardrails for neutral services (L)

1. **Arbitration needs both sides.** An arbitrator booking requires every party to join and confirm the appointment of that arbitrator after the dispute has arisen (`joint_booking = true`). One-party arbitration booking is impossible (`MKP_ONE_PARTY_ARBITRATION_BLOCKED`).
2. **Repeat-player disputes.** Where the initiating party is an organisation flagged repeat player (lender, insurer, employer, platform) and any counterparty is an individual consumer, borrower, employee or policyholder, surface (ii) arbitration bookings are blocked (`MKP_REPEAT_PLAYER_ARBITRATION_BLOCKED`) and mediation bookings require the individual's informed acceptance after seeing the organisation's relationship with the provider (if any) and a link to Equator's administered route and free statutory forums (NN-20). This mirrors NN-03 and *CORE* [RE F2.2].
3. **Sealed and safety matters.** FAM matters with a safety flag, POSH matters and criminal matters are not bookable on surface (ii) (NN-07, NN-24); the enquiry form routes them to the safe route.
4. **Pending Equator case.** If the buyer and counterparty already have an Equator-administered case on the same dispute, booking a private neutral for it requires an explicit "move to private" step with both parties' consent; sponsored slots are never shown in that context.

### AA.6.5 Engagement proposal and fee disclosure

The provider sends a proposal (`mkp.engagements` in `proposed`) with:

| Item | Content | Rule |
|---|---|---|
| Scope | Service, sessions/pages/days, deliverables, timeline, mode, venue | — |
| Fee disclosure | Each component: provider fee (model, rate, estimate), Equator platform fee (if any), GST per component (or RCM note for arbitral tribunal or advocate services to a business entity), pass-throughs at actuals, total payable | Appendix O §6.4 display; no drip pricing (NN-29); fee shown is binding up to the estimate unless the buyer approves a variation |
| Payment milestones | e.g., registration, per session, on delivery of report | ADR-native milestones, not hourly work diaries [RA EQM-12] |
| Cancellation and refund | Stage-based refunds; cancellation symmetry (Appendix O §6.3) | Shown before payment (E-Commerce r.7) |
| Disclosures | Conflict disclosure; paid-visibility disclosure if the provider sponsors (AA.10.7); related-to-Equator; group relationships | — |
| Terms | Provider's engagement terms (template in AA.13) and the provider's adopted rules for neutral services | Versioned, pinned to the engagement |

Proposal validity 7 days (T). Variations follow the same proposal → confirmation path.

### AA.6.6 Booking confirmation and payment

- Explicit confirmation: an unticked checkbox "I have read the fee disclosure and terms" and a "Confirm and pay" button showing the total including GST (E-Commerce r.4(9); NN-29). No pre-selected add-ons.
- For neutral services, every party confirms; the first payer's payment is held at the payment aggregator (transfer `on_hold`) until all parties confirm or the hold period (`platform.mkp.hold_days`, 14 days, **G** within 7–21 — v3.1 fix: AA.15 is the tier of record) lapses, then refunded automatically (P03 FR-P03-31 hold pattern).
- On confirmation: a matter is created in the provider's Chambers tenant (`source = 'private_marketplace'`), the engagement moves to `confirmed`, calendar holds are created, and the Chambers case workspace takes over.

**Ready-to-pay gate *(v3.1)*.** "Confirm and pay" is enabled only when `GET /v1/mkp/engagements/{id}/readiness` returns every item green; the screen shows the same checklist so the buyer knows what is missing and who must act:

| # | Check | Fails with | Who fixes it |
|---|---|---|---|
| R1 | Conflict check `clear`, or `disclosable` with every party's acknowledgement, valid for the current party set and age (AA.6.3) | `MKP_CONFLICT_CHECK_REQUIRED` / `MKP_CONFLICT_CHECK_STALE` (409) | System re-runs; provider discloses; parties acknowledge |
| R2 | Booking guardrails AA.6.4 pass (joint booking, repeat-player, sealed matters, pending Equator case) | Existing AA.6.4 codes | — |
| R3 | Proposal valid (not expired) and fee disclosure accepted; disclosure hash = checkout hash | `MKP_FEE_DISCLOSURE_REQUIRED` | Buyer |
| R4 | First session slot held: a tentative hold on the provider's calendar for the proposed slot, taken when the buyer opens checkout, kept for `platform.mkp.slot_hold_minutes` (T, default 30, bounds 15–120), enforced by an exclusion constraint so two buyers cannot hold the same slot | `MKP_SLOT_UNAVAILABLE` (409) with the next three free slots | Buyer picks another slot |
| R5 | Identity level K2 for the payer (Appendix S §3) | `KYC_REQUIRED` (Appendix F) | Buyer |
| R6 | Paid bookings allowed: `tax_memo.mkp_eco_recorded = true` and RS-18 live in scope (`assertLive`) | `MKP_TAX_MEMO_MISSING` / `REV_STREAM_NOT_LIVE` | Equator (no buyer action; enquiry stays open) |
| R7 | Provider still `listed` with the category visible and no interim suspension | `MKP_PROVIDER_NOT_LISTED` | — (buyer offered other providers; nothing charged) |

The checkout call carries an `Idempotency-Key`; a repeated click never creates a second payment. **Compensation:** if the payment is captured but matter creation in the Chambers tenant fails, the activity retries three times with back-off; if it still fails, the hold is refunded automatically, the slot released, the buyer told in plain words, and an incident opened for `marketplace_manager` (no money is ever kept for a booking that did not open). *(v3.1)*

### AA.6.7 Engagement state machine (`mkp.engagements.status`)

```
enquiry_open → proposal_sent → (counterparty_invited → counterparty_accepted)? → confirmed → in_delivery
in_delivery → milestone_due ⇄ milestone_disputed → milestone_released → … → completed → review_window → closed
exits: enquiry_expired | proposal_declined | proposal_expired | cancelled_by_buyer | cancelled_by_provider
       | refunded | fee_dispute → (resolved → in_delivery | closed)
v3.1:  proposal_sent | counterparty_accepted → conflict_recheck → (back to the same state | conflict_blocked → refunded)
       confirmed | in_delivery ⇄ on_hold (reason: provider_unavailable | party_request | court_or_authority_order | fee_dispute;
                                          clocks paused; max platform.mkp.on_hold_max_days, then cancel with refund or substitution)
       confirmed | in_delivery → partially_completed → closed   (milestones released so far kept; rest refunded per RP-MKP)
```

Timers: provider response 2 WD; proposal 7 days; counterparty 10 days; milestone confirmation by buyer 5 working days (silence = deemed release with prior notice at day 3); review window 30 days after `completed`.

**On hold, substitution and partial completion *(v3.1)*.** `on_hold` pauses the milestone and response clocks with a mandatory reason visible to every party; it lasts at most `platform.mkp.on_hold_max_days` (T, default 30, bounds 7–60), after which the buyer chooses cancellation with refund of unreleased milestones or substitution. **Substitution:** where the provider is a Chambers tenant (or an individual on leave) the chambers may propose another listed neutral of the same chambers; the proposal re-runs the conflict check (AA.6.3) and needs every party's fresh acceptance (and, for arbitrators, fresh appointment confirmation, AA.6.4 rule 1); fees cannot rise without a variation the buyer accepts. A provider's out-of-office set in the calendar (SCR-P19-13) pauses new enquiries automatically and shows "Not taking new bookings until {date}" instead of hiding the profile. `partially_completed` closes an engagement where the parties stop early by agreement: released milestones stay paid, unreleased ones are refunded under RP-MKP, and the review invitation still issues. *(v3.1)*

### AA.6.8 Service delivery on Equator tools

| Category | Delivered in | Data shared with provider |
|---|---|---|
| Neutral / chambers | Provider's Chambers tenant: hearings (LiveKit), documents, outcomes, eSign/eStamp | Matter data under the Chambers tenant's role (fiduciary) |
| Translator / transcriptionist | Task workspace: secure link to the selected documents (Appendix L §2.6) with watermark and expiry | Only documents the party selects; disclosure logged in `core.disclosures` (purpose `TRANSLATOR`/`INTERPRETER`) where the documents belong to an Equator case |
| Interpreter | Hearing room interpreter channel | Session access for the booked session only |
| Process agent | Delivery task: recipient name, address, document envelope hash; proof-of-delivery upload | Minimum necessary; returns POD to the buyer |
| Valuer / expert | Task workspace with selected documents; report upload | As selected |
| Venue | Booking calendar, attendee count, accessibility needs | No case content |

### AA.6.9 Disputes about fees

A fee dispute between buyer and provider goes to a published fee-dispute procedure (`MKP-FDP-2026.1`): first, a 7-day direct resolution window in the platform; then a decision by an independent fee reviewer who is not on the provider's Chambers panel, with Equator staff recused from the merits [RA EQM-13]. The reviewer's decision binds the release of held funds only; either side keeps all legal remedies. Equator is never the final decider of a provider's fees.

---

## AA.7 Payments, tax and payouts

### AA.7.1 Money flows (NN-13, NN-31)

| Flow | Rail | Merchant of record (default) | Notes |
|---|---|---|---|
| Provider fee (neutral, chambers) | PAYMENTS_PORT split settlement (Razorpay Route linked account of the Chambers tenant) | Chambers tenant | Equator's take split at source (AA.7.2) |
| Provider fee (service provider) | Split settlement to the provider's linked account | Provider | Same |
| Buyer processing fee (RS-52, `marketplace.client_processing_fee` OFF) and advocate-neutral flat fee (AA.2.4 rule 4) | Equator merchant account | Equator | Separate line, never hidden; identical whatever provider is chosen (RE C.14) |
| Sponsored listing and provider subscription fees | Equator merchant account; e-mandate for monthly plans (Appendix O §5.9) | Equator | Equator's own supply, GST forward-charged |
| Settlement sums between parties | Escrow rail (P05 §4H) | — | Never on the marketplace |

Holds use the payment aggregator's transfer-hold feature so funds remain with the aggregator or escrow bank and never sit in an Equator account **[VERIFY — open: RBI PA Directions 2025 treatment of marketplace transfer holds; PA confirmation]**.

### AA.7.2 Equator's take on non-advocate bookings

- Rate by the provider's Chambers plan (`marketplace.take_rate.<plan>`): CH-LITE/CH-SOLO 15%, CH-PRO 12%, CH-INST 10%, CH-IAAS contracted (Appendix O O-R2; master X-31; **Subject to Board approval**). Service providers: `marketplace.take_rate.service_providers` (default 10% **[Board]**), registered as a scope of RS-18 in AB.
- Flat and uniform per plan; never falls as a provider's billed fees rise (RB X-19); never applied to Equator-administered cases (0%, B §B.7.7) or to advocate providers (AA.2.4).
- Equator's take is Equator's own taxable supply to the provider, invoiced monthly with GST at the applicable rate and SAC **[VERIFY — open: rate and SAC, tax adviser; Appendix O Q-O4]**.

### AA.7.3 GST TCS engine (CGST s.52; G)

Runs only when the tax memo concludes Equator is an e-commerce operator collecting consideration for the relevant collection model (`billing.eco_gst_tcs` flag, LR-TAX-008).

| Step | Rule |
|---|---|
| Determine supply character per line | Provider GST status (registered/unregistered/composition), supply type, recipient type (business entity or not), place of supply |
| Exclusions | No TCS on exempt supplies (GST FAQ Q14) or supplies taxed under reverse charge (FAQ Q15): legal services by an advocate or firm of advocates to a business entity and services of an arbitral tribunal to a business entity are RCM (Notification 13/2017-CT(Rate) entries 2–3) |
| Rate | `platform.tax.gst_tcs_rate` = 0.5% (0.25% CGST + 0.25% SGST/UTGST, or 0.5% IGST) from 10 Jul 2024 (Notification 15/2024-CT); G-tier with source citation |
| Base | Net value of taxable supplies (supplies less returns) per supplier per month |
| Output | TCS ledger per supplier GSTIN; monthly GSTR-8 data file (via TAX_INVOICE_PORT or export); supplier statements show TCS collected |
| Registration | Compulsory registration as ECO (s.24(x)) is a go-live checklist item |

### AA.7.4 Income-tax withholding engine (Income-tax Act 2025 s.393(1) Table Sl. 8(v); G)

Runs when `billing.eco_withholding` is ON (LR-TAX-007). Rate `platform.tax.eco_tds_rate` = 0.1% of gross amount, at the earlier of credit or payment; threshold `platform.tax.eco_tds_individual_threshold_minor` = ₹5,00,000 per tax year (Income-tax Act 2025) for resident individual/HUF participants who furnished PAN or Aadhaar; no threshold for others. Interaction with the payer's own professional-fee TDS is handled per the tax memo (`tax_memo.eco_tds_interaction` enum: `eco_only`, `payer_only_with_declaration`, `both`) **[VERIFY — open: LR-TAX-007]**. Quarterly return data and certificates (generic label "TDS certificate", Appendix O Q-O11).

### AA.7.5 Payouts with maker-checker (NN-36)

```
Milestone released → payout line created (provider fee − take − TCS − TDS − refunds) 
 → nightly payout batch prepared by system (maker identity = system run, owner finance_ops)
 → accounts_checker approves batch (step-up MFA; limits per authority matrix ctl)
 → batches above the authority limit need a second approver (finance_controller)
 → transfer release via PAYOUT_PORT → reconciliation by a third user (accounts_maker ≠ approver)
```

- Separation of duties (L): no user may create a payee, change bank details, approve and release a payout, and reconcile it (NN-36). Cerbos rule `MKP_PAYOUT_SOD`; violation `MKP_PAYOUT_SOD_VIOLATION` (403).
- Payout SLA T+3 working days after release (T-tier within T+2 to T+7) [RA EQM-14].
- Provider statement: gross, take, GST on take, TCS, TDS, refunds, net; downloadable XLSX and PDF.

### AA.7.6 Payee and bank-detail changes (NN-36)

A new payee or a bank-detail change: penny-drop name match → out-of-band confirmation to the provider's registered e-mail and mobile → **cooling-off of 72 hours** (G; ≥ 48) during which payouts to the new account are held (`MKP_PAYEE_COOLING_OFF`, 409) → `finance_ops` checker approves. Changes are logged in the un-disableable edit log.

### AA.7.7 Refunds and cancellations

Refund code RP-MKP (Appendix AB §AB.5): Equator's take and any processing fee follow the booking and are never retained on a booking refunded for provider non-delivery. Stage-based refunds per service (published on the offering); cancellation symmetry (if the provider cancels late, full refund and free rebooking with another provider); refunds to the original instrument; credit note reverses GST on refunded taxable value (CGST s.34); TCS/TDS reversed per the tax memo.

---

## AA.8 Reviews, complaints, enforcement, takedown, transparency and fraud

### AA.8.1 Process-only reviews (non-advocate neutrals and service providers only)

- **Eligibility (L):** only a buyer or counterparty of a `completed` engagement; one review per person per engagement; invitation sent 48 hours after completion; 30-day window; both sides invited equally [RA EQM-10]. Never for advocates, CA/CS/CMA members, or any surface (iii) professional (`MKP_REVIEW_PROFESSIONAL_FORBIDDEN`).
- **Questions (L list, wording G):** neutral services — explained the process clearly; listened; treated both sides equally; kept to time; respectful; "Did you feel pressured to settle?". Service providers — delivered on time; quality matched what was agreed; communication; fees matched the disclosure; accessibility. Free text ≤ 1,000 characters with PII redaction preview. **No item on outcome, result, amount or who won** (schema lint `MKP_REVIEW_OUTCOME_ITEM`, 422).
- **No incentives:** no discount, credit or entry to a draw for reviewing; providers may not ask for reviews outside the platform invitation.
- **Display:** aggregate shown only at n ≥ 10 published reviews (master X-28); per-item bars; date range; "Reviews come only from people who completed a booking." No `aggregateRating` schema markup.
- **Moderation** (queue `marketplace_moderator`, ≤ 72 hours): Appendix N §7.3 checks (PII, abuse, misconduct allegations → complaint intake on the reviewer's consent, coordinated or retaliatory rating, repeat-player weighting cap 20%). Published moderation policy `/marketplace/review-policy` with categorised removal statistics in the transparency report. Neither providers nor sponsors can remove reviews. Equator takes only a licence to display reviews for the listing period plus 30 days [RA EQM-18]. Practice reference IS 19000:2022 **[VERIFY — open: standard text]**.
- **Right of reply:** provider reply ≤ 1,000 characters shown with the review; one re-moderation request per review.

### AA.8.2 Complaints about a provider (E-Commerce Rules r.4; IT Rules 2021)

| Element | Rule |
|---|---|
| Channels | `/marketplace/complaints` form, in-booking "Report a problem", e-mail to the published grievance address, phone-assisted |
| Grievance Officer | Named Marketplace Grievance Officer (`grievance_officer`, Operations Platform, Appendix X) with name, designation and contact on every marketplace page and invoice (E-Commerce r.4(4)) |
| Clocks | Acknowledge ≤ 48 hours; redress ≤ one month (r.4(5)); intermediary grievances on content ≤ 7 days and specified-content takedown ≤ 3 hours (IT Rules amendment 2026 [P]); clocks owned (NN-04 pattern) |
| Complaint copy | Complainant receives a copy of the complaint as recorded (r.4(5) as amended 2026) |
| NCH | National Consumer Helpline convergence through the integration the 2026 amendment requires **[VERIFY — open: NCH integration specification and commencement]** |
| Categories | service not delivered; quality; fees beyond disclosure; conduct; conflict not disclosed; confidentiality; impersonation or false credential; harassment; off-platform payment demand; content (bio, review) |
| Severity | S1 (false credential, undisclosed hard conflict, harassment, fraud, confidentiality breach) → immediate interim suspension of new enquiries and review of open engagements; S2 (repeated non-delivery, fee overcharge) → pause new bookings; S3 → none |

### AA.8.3 Enforcement ladder and due process [RA EQM-06]

| Level | Action | Due process |
|---|---|---|
| E1 | Guidance note | Recorded; no listing effect |
| E2 | Formal warning | Recorded; visible to moderators at re-verification |
| E3 | Category hidden (e.g., translation only) | Notice with reasons; 15-day reply window |
| E4 | Suspension of the whole listing (1–6 months) | Notice with reasons; 15-day reply; decision by Marketplace Review Panel (two members independent of sales and ad operations; one from Legal and Compliance) |
| E5 | Delisting | As E4; re-application after ≥ 2 years |
| Interim | Immediate suspension for S1 pending decision | Decision ≤ 30 days; reasons |

Appeal to the Marketplace Appeals Panel (members not involved in the first decision; at least one external member) within 15 days; decision ≤ 30 days. Grounds, notices and decisions are recorded in `mkp.enforcement_actions` with reasons (mandatory, `MKP_REASONS_REQUIRED`). Categorised statistics are published quarterly.

### AA.8.4 Takedown and content policy

Published Marketplace Content Policy (`MCP-2026.1`) listing prohibited content (false credentials, outcome guarantees, "top/best" claims, client names without consent, discriminatory content, solicitation for advocates, links to off-platform payment). Takedown queue with clocks (3 hours for specified content categories under the IT Rules amendment; 36 hours otherwise **[VERIFY — open: category list per G.S.R. 120(E)]**), reasons sent to the provider, counter-notice route, and logs for the transparency report.

### AA.8.5 Quarterly Marketplace Transparency Report [RA EQM-22]

Published at `/marketplace/transparency` (Claims Register entries, NN-17; cells n < 10 suppressed, master X-28): listings by category and State; applications, verification rejections by reason; enforcement actions by level and category; appeals and outcomes; reviews published and removed by reason; complaints by category with median time to acknowledge and redress; takedowns by category and time; fee disputes and outcomes; median payout time; **sponsored revenue as a share of marketplace revenue and number of sponsors**; display-ad revenue share; ranking-policy version in force; dark-pattern self-audit status. Generated from a versioned query pack with dataset hash; approved by `compliance_officer` and published by `marketplace_manager`.

### AA.8.6 Fraud controls

| Risk | Control |
|---|---|
| Fake provider / identity theft | KYC/KYB; penny-drop name match; liveness for individuals (Appendix S §3.12); two-person credential verification |
| False credentials | Source verification (verify endpoint, issuer e-mail, official portal look-up with evidence hash); annual re-verification; S1 complaint ground |
| Fake reviews | Only completed engagements; device and payment-instrument link analysis; burst detection; repeat-player weight cap |
| Collusive bookings to farm reviews or launder money | Same buyer–provider pair limits; refund-pattern alerts; payouts held for first 3 engagements of a new provider (T, within 1–5) |
| Bank-detail fraud | AA.7.6 cooling-off and out-of-band confirmation |
| Off-platform payment demands | Message lint; buyer education banner; complaint category |
| Sponsored-slot abuse (fake competitor sponsorship, keyword squatting) | Sponsor KYC; slot targeting limited to category and geography (no competitor names) |
| Insider abuse (staff altering order or reviews) | Ranking computed in code from governed policy; no manual pinning; staff actions audited; quarterly internal-audit sample (Appendix X internal audit) |

Signals go to `mkp.fraud_signals`; actions follow AA.8.3.

---

## AA.9 Enterprise procurement

### AA.9.1 What enterprises may and may not procure (L)

| Procurement | Allowed? | Where |
|---|---|---|
| Ancillary services (translation, interpretation, transcription, notice delivery, valuation, expert reports, venues, training) for the enterprise's own needs | Yes | Surface (ii) procurement (AA.9.2) |
| The enterprise's **own** professionals (advocates, CAs, CSs, CMAs, valuers, process agents) for its own matters — e.g., a lender's panel advocates for NPA recovery suits, SARFAESI steps, DRT applications, execution petitions on Equator awards | Yes | Surface (iii) Professional Panel Register (AA.12.6) |
| Neutrals for disputes with the enterprise's own customers, borrowers, employees or policyholders | **No** (`MKP_ENTERPRISE_NEUTRAL_PROCUREMENT_BLOCKED`, 403) | Only Equator's administered allocation (NN-03) or a Chambers institution's own rules where the enterprise has no role in appointment |
| A panel of neutrals curated by the enterprise | **No** | *CORE* (curated panels do not cure unilateral appointment) [RE F2.2] |

### AA.9.2 Procurement engine for ancillary services (`mkp.procurement_*`)

1. **Bulk intake.** CSV/XLSX/API upload of service requests (e.g., 2,000 translations of notices into 6 languages; 500 notice deliveries in 3 districts) with validation report and per-row errors (P09 bulk pattern).
2. **Enterprise vendor panel.** The enterprise creates a vendor panel from listed providers (`mkp.enterprise_vendor_panels`), each provider accepting the panel terms. Allocation of work within the panel is the enterprise's choice; Equator offers round-robin and capacity-based distribution tools.
3. **RFQ.** RFQ with scope, volume, SLA, languages, geography and deadline to selected panel members or to all eligible providers in a category; providers respond with priced quotes; comparison grid shows total including GST; award recorded with reasons.
4. **SLAs.** Per panel: turnaround, quality acceptance criteria, rework rules, credits for breach (defined, not outcome-based); SLA clocks with owners.
5. **Reporting.** Enterprise dashboard: volumes, turnaround, SLA attainment, spend by vendor and category, quality rejections; exports (NN-37). Reports never include case outcomes.

### AA.9.3 Finbyx and Udofin use cases

| Use case | Surface | Flow |
|---|---|---|
| Lender client of Finbyx (LOS/LMS) builds a panel of recovery advocates across 12 States for NPA suits | (iii) via registry API in the Finbyx tenant | Finbyx consumes `dir` records consented to purpose `group_share_finbyx`; the lender invites professionals; each accepts the lender's panel terms; RFQ and SLAs in the lender's panel register; matters referenced opaquely |
| Udofin digital lending platform's lender partners need execution of Equator awards | (iii) in Equator enterprise tenant or Udofin tenant | Award-holder lender selects its own panel advocate; Equator execution pack shared under authority (AA.11.3) |
| Lender needs notices translated into regional languages | (ii) procurement | Vendor panel of translators; derived-text labels NN-32 |
| Lender needs valuers for SARFAESI | (iii) tenant-private vendor entries (valuers) or (ii) `SVC-VAL` | Lender's choice; Equator never values (NN-01) |

Lender-side panel performance notes, RFQ prices and SLA scores stay in the lender's tenant; they never enter Equator's neutral systems or any other tenant (NN-16, NN-38; CI `GROUP_SHARE_SCOPE`).

---

## AA.10 Paid placement and display advertising (NN-34; R-64)

### AA.10.1 Gates (all OFF by default)

| Flag | Tier | Default | Approver(s) before ON | Effect |
|---|---|---|---|---|
| `marketplace.paid_placement` | G | OFF | Board resolution (number and date recorded) **and** counsel sign-off in the legal-flag register; D2-14 amendment entry (D3-01) | Enables sponsored slots on surface (ii) for eligible sponsors |
| `marketplace.paid_placement.advocates` | **L** | OFF | Not switchable in v3.0 (would need an NN-34 change by the Board) | — |
| `marketplace.related_party_sponsorship` | G | OFF | Board and counsel | AA.3.3 |
| `platform.rev.ads.enabled` | G | OFF | Board; counsel on the advertiser policy; `compliance_officer` | Enables display advertising on content pages (AA.10.8) |
| `mkp.provider_subscriptions` | G | OFF | Board (prices); CFO | Optional paid tools plan for service providers, stream RS-57 (AA.14) |

Kill switch: each flag and its revenue stream (AB) stops new impressions and new orders within 5 minutes, hides price blocks and CTAs, and keeps run-off obligations (pro-rata refunds) [RB A.6].

### AA.10.2 Sponsor eligibility (`sponsor_eligible()`, L logic, G parameters)

A provider may buy a sponsored slot only if all are true: category is `NEU-*` or `CHM` (AA.3.1); provider is not an advocate, not a law firm, and (for chambers) lists no advocate-neutral; not an institute member listed under AA.3.2 rule 3; `listed` with every credential verified; ≥ 40 hours mediation training for mediator categories and Code acceptance [RB B.10]; no open S1/S2 complaint and no enforcement level ≥ E3 in 12 months; not related to Equator unless AA.10.1 flag ON; not restricted by an MCI conduct standard (`rulepack.IN.mkp.mci_conduct`). Failure returns `MKP_SPONSOR_INELIGIBLE` (422) with the failing condition.

### AA.10.3 Decision D3-37 — commercial rules for sponsored listings

1. **Product name** in all copy: "Sponsored listing". Never "preference", "priority", "premium", "featured", "top" or "recommended" [RB B.11; X-18].
2. **Inventory:** sponsored slots exist only on surface (ii) search results and category pages. Maximum `marketplace.paid_placement.max_slots_per_page` = 2 (G; L ceiling 2) and never more than 20% of results shown (L) [RA EQM-08]. No slots on profiles, the institutional directory, allocation screens, enterprise consoles, live-case or hearing screens, notices or e-mails to any respondent, AI assistant answers, or any page where the viewer has an open Equator-administered matter (L).
3. **Placement:** a visually distinct block above organic results, never interleaved, with the label in the same font size as the provider name, adjacent to it: **"Sponsored — paid placement. Does not affect Equator appointments."** (NN-34). Each sponsored card has "Why am I seeing this?" ("This provider paid for a sponsored listing in {category}, {geography}. Sponsored listings rotate among sponsors. Organic results below are not affected.") and is dismissible for the session. A sponsor also appears in organic results in its normal organic position; sponsorship never changes that position.
4. **Rate card (equal for all):** flat price per slot-month per (category × State or "All India online") published at `/marketplace/advertise` with GST; no auctions, bids, discounts by relationship, or volume tiers at launch (G; prices **Subject to Board approval**). Monthly spend cap per sponsor `platform.mkp.sponsored.max_slot_months_per_sponsor` = 2 per category-geography (G).
5. **Rotation:** sponsors in a category-geography rotate per page view with equal impression share (weighted round-robin with session seed); rotation fairness report monthly (each sponsor's impression share within ±5% of equal; else credit).
6. **Ordering and billing:** order → `sponsor_eligible()` → creative check (name, photo, one-line description from the verified profile only; no new claims) → `ad_reviewer` approves → `compliance_officer` checker → activation on the 1st of the month; e-mandate or prepaid; pro-rata refund on removal for ineligibility not caused by misconduct; no refund on delisting for S1 misconduct (stated in terms).
7. **Targeting:** category and geography only. No targeting by query text naming another provider, by viewer identity, by past searches, by case data, or by any counterparty (L).

### AA.10.4 Published ranking parameters and sponsored disclosure

`/marketplace/how-ranking-works` (AA.5.3) states, in its first paragraph: "Sponsored listings are paid placements shown in a separate block labelled 'Sponsored'. They do not change the order of the results below, any reviews or badges, or anything about appointments in matters Equator administers." It lists the sponsored rules (slot cap, rotation, rate card link) and links to the transparency report. This meets E-Commerce r.4(12) and r.5(3)(f) as amended **[VERIFY — open: sub-rule numbers per Gazette]**.

### AA.10.5 Annual dark-pattern self-audit (E-Commerce r.4(15) as amended; LR-CONS-008)

- Cadence *(v3.1 fix)*: the **certified** self-audit is annual (r.4(15) as reported [RE F3.1]); a quarterly internal self-audit is permanent Equator policy (Appendix G LR-CONS-008, cadence settled in v3.1): automated DP-01…DP-13 results plus a sampled manual walkthrough, signed by `compliance_officer`, feeding the annual certificate.
- Scope: every marketplace, checkout, sponsored, advertising, subscription and cancellation flow against the 13 patterns (Appendix O §6.2, DP-01…DP-13).
- Method: automated lint and test results (DP tests), a manual walkthrough on web and mobile by `compliance_officer` with a second reviewer from Internal Audit, screenshots, findings, remediation tickets.
- Output: a signed self-audit report and a **compliance certificate displayed prominently** on `/marketplace` footer and `/trust/dark-patterns` with the date; monthly sponsored-listing operations audit (RB AU-25) feeding it. **Ownership of AU-25:** sponsored-listing operations (order intake, creative review, label, cap, interleave and rotation checks, refunds and the monthly self-audit) are owned by this appendix in schema `mkp` (Appendix X §X.12.5 points here; Appendix Y does not own them). They stay OFF under `marketplace.paid_placement`; while the flag is OFF, `SponsorshipAuditJob` (P19 §7.5) runs in baseline mode and certifies that no sponsored slot rendered. Each monthly audit is signed by `compliance_officer`.
- Failure: any critical finding blocks re-enabling `marketplace.paid_placement` after the annual date until fixed (`MKP_DARK_PATTERN_AUDIT_OVERDUE`).

### AA.10.6 Firewall tests (CI and runtime)

| Test | Fails when |
|---|---|
| `NO_PAID_PLACEMENT` (extended) | Any read path from `mkp.sponsorship_*`, `mkp.ad_*`, `mkp.provider_subscriptions`, `rev.*` to the institutional directory, allocation, eligibility, grading, Quality Index or conflict checks |
| `MKP_SURFACE_ISOLATION` | Any cross-surface join, view, FK or call not in the AA.2.2 allow-list |
| `SPONSORED_LABEL_PRESENT` | A rendered sponsored card lacks the exact label text, size and adjacency (visual regression + DOM assertion) |
| `SPONSORED_NOT_INTERLEAVED` | A sponsored card appears inside the organic list |
| `SPONSORED_SLOT_CAP` | More than the configured slots, or > 20% of results |
| `RANKING_PARAMS_PUBLISHED` | Deployed ranking-policy version differs from the published page version |
| `RANKING_IGNORES_PAID` | Golden-vector run shows any difference in organic order when sponsorship, plan or related-party attributes are toggled |
| `NO_SPONSOR_IN_CASE_CONTEXT` | A sponsored slot renders for a viewer with an open administered matter, or on any page tagged `case`, `hearing`, `notice`, `grievance`, `posh`, `fees_case` |
| `R36_PROFILE_ALLOW_LIST` | An advocate or institute-member record renders a field outside its allow-list |
| `ADVOCATE_TARIFF_LINT` | A tariff, plan or stream is tagged `advocate_commission`, `advocate_listing_fee`, `advocate_lead_fee` or `professional_referral_reward` |
| `NO_ROLL_SCRAPING` | A scheduled job or HTTP client targets a configured roll-portal host |
| `GROUP_SHARE_SCOPE` | Case, allocation or neutral data flows to a Finbyx, Udofin or LawDocs consumer, or lender panel performance data flows into `core` |

### AA.10.7 Disclosure in s.12 statements and conflict notices

When a neutral who held a sponsored listing in the preceding 24 months is proposed or appointed in **any** matter (Equator-administered or private), the disclosure template (Appendix N §5 Code; A&C s.12(1), Sixth Schedule format) pre-fills: "I pay (or paid between {from} and {to}) Equator Resolution Service Private Limited for sponsored listings on the Equator Marketplace. This is a commercial relationship with the institution; it does not give me any priority in appointments." The neutral cannot delete the pre-filled item. In Equator-administered matters the item is disclosed to parties; allocation still never reads it (flow F4 carries only the boolean to the disclosure module). Group relationships of the parties (Finbyx/Udofin clients) are disclosed under NN-16.

### AA.10.8 Display advertising on content pages (RS-25; OFF)

| Rule | Detail |
|---|---|
| Where | Only CMS content pages tagged `content` (blog, guides, glossary, regulatory updates) on `apps/web` (P13) |
| Never (L) | Marketplace search and profiles, institutional directory, neutral profiles, fee or pricing pages, case, hearing, notice, grievance, POSH, complaint, Dispute Explorer, signup and checkout flows, e-mails and notices, mobile case screens |
| Allowed advertisers (policy list `mkp.ad_policy_categories`, G) | Non-legal B2B vendors: HR technology, accounting and compliance software, document scanning, e-stamp/e-sign technology vendors, training technology, office and hearing equipment, accessibility services |
| Prohibited advertisers (L) | Advocates, law firms, legal-service aggregators, neutrals, chambers, ADR institutions; lenders, NBFCs, insurers, collection or recovery agencies and any repeat-player enterprise; CA/CS/CMA members and firms (institute rules); political, gambling, crypto, betting, tobacco, alcohol; anyone in an open dispute on Equator |
| Format | Static image or text slot, labelled "Advertisement", maximum 2 per page, no auto-play, no pop-ups, no tracking pixels from advertisers (ads served first-party from `mkp.ad_creatives`; impressions counted server-side, aggregate only) |
| Claims | Advertiser claims substantiated; no claims about Equator's endorsement; CCPA 2022 Guidelines; copy lint |
| Approval | `ad_reviewer` (maker) → `compliance_officer` (checker); categories outside the list need `legal_reviewer` |
| Disclosure | Ad revenue reported in the transparency report; advertiser register published annually |

---

## AA.11 Post-resolution services: execution and registration with party choice

### AA.11.1 Principles (L)

1. Equator prepares execution packs and registration checklists, tells the party which forums the law points to, books registration appointments and tracks progress (Appendix R §4.1; D2-11). It does **not** file, appear, advise on remedy choice, or represent anyone (Advocates Act ss.29, 33).
2. **The party always chooses** the advocate or professional, or chooses to act in person; Equator never recommends, ranks or refers a named professional and receives nothing from any professional (NN-39; RE C.14).
3. **Free options first:** for individuals, the chooser shows the District/State Legal Services Authority legal-aid route first (LSA Act 1987 s.12 eligibility summary and contact), then court-annexed help desks where configured.
4. **No guarantee** of outcome, timeline or enforceability beyond what the law states (Appendix O X-12).
5. Documents move only with the party's authorisation, item by item, logged.

### AA.11.2 Post-Resolution Professional Chooser (SCR-P19-30, replaces Appendix R §4.8 per X-60)

*Screen ID (v3.1):* the canonical ID is **SCR-P19-30** (P19 §6, FR-P19-45; Appendix AG §AG.0.5 #10 and AG.2.2). "SCR-P06-65 v3" is a retired alias kept only for traceability; the case-app route renders SCR-P19-30.

| Option (in this order) | What the party sees | Record |
|---|---|---|
| Free legal aid (individuals) | DLSA/SLSA for the district of execution or registration; eligibility summary; contact | `postres_choice = 'legal_aid'` |
| I have my own advocate / professional | Invite by name, e-mail or mobile and (optional) enrolment number; the invitee verifies through Appendix S §4.5 | `postres_choice = 'own_professional'` |
| Equator Post-Resolution Advocate Panel (only if `postres.advocate_panel` ON) | Seeded-random list within filters (State, district, court type, language, area of practice); Schedule fields only; disclosure banner | `postres_choice = 'equator_panel'` with `record_ref` |
| Act in person | Self-help checklist; forum resolver (Appendix R §4.3) | `postres_choice = 'in_person'` |

Banner (fixed copy): "You choose who helps you. Equator does not recommend, refer or pay any advocate and receives nothing from them. Free legal aid may be available to you." The choice, the time, the options shown (IDs and order seed) and the party's consent are stored in `mkp.postres_choices` (append-only).

### AA.11.3 Authorising document transfer

After choosing, the party authorises the professional by adding them as representative with scope `view_documents` + `court_steps_support` (Appendix S §4.3) or sends a secure link (Appendix L §2.6) to **selected** items of the execution or registration pack (award or settlement certified copy, BSA s.63(4) certificate, asset schedule if any, compliance history). Each transfer writes `core.disclosures` (purpose `ENFORCEMENT`, `REGISTRATION` or `PARTY_COUNSEL`). The party can revoke at any time; revocation ends access in the same transaction.

### AA.11.4 Decision D3-36 (part) — Equator Post-Resolution Advocate Panel

- An **optional** panel of verified advocates for parties who ask for help with execution, registration conveyancing, s.34/s.36/s.47 steps or Family Court/NCLT steps (Appendix R §4.8 purposes). Flag `postres.advocate_panel` (G, OFF; approver: counsel's written opinion on the panel terms and on r.36 risk, plus `legal_reviewer`).
- Implemented as an Equator tenant panel register `EQ-POSTRES` on the registry (AA.12.6), membership by the advocate's consent to purpose `postres_panel` and acceptance of the Post-Resolution Panel Terms `PRP-2026.1`: **listing free**; **no fee-share, commission, referral fee or reward**; fees agreed directly between party and advocate; no ratings or reviews; Schedule fields only; seeded-random order; advocates who acted as neutral, for any party, or as Equator staff in the case are hidden for that case; annual reconfirmation; removal on disciplinary order.
- Shown only inside the party's own case, to authenticated parties, after an outcome exists. No public page, no SEO.

### AA.11.5 Registration and execution hand-offs

The registration workflow (Appendix R §4.6) and execution tracking (R §4.5) record which professional acts (`acting_professional_ref`) for reminders and milestone entry; Equator sends reminders to the party (and to the professional if the party authorised it). Milestones entered by a professional are labelled with the source.

---

## AA.12 Infrabyx Professional Registry (`dir`; D3-05 group shared service)

### AA.12.1 Decision D3-36 — topology and roles

| Role (DPDP) | Who | For what |
|---|---|---|
| Directory Owner — Data Fiduciary | The entity the Board designates (`group.dir.owner_entity_id`, G; Board resolution reference required before go-live) | Collection, verification, master record, publication within consented purposes |
| Consumer — independent Data Fiduciary | Equator, Finbyx, Udofin, LawDocs, and each of their tenants that engages professionals | Its own engagement use of records it receives |
| Processor | Hosting/IT operator; the Owner when it hosts a consumer's tenant-private panel data | Under s.8(2) contracts |

The GDSA (D3-05) between the Owner and each consumer is a provisioning gate (`DIR_GDSA_MISSING`, 403). Minimum contents [RE D.21]: purpose schedule (execution, registration and recovery engagement; conflict screening; no marketing; no credit scoring or profiling of professionals); role matrix; data minimisation (allow-listed fields + verification status only); onward-transfer ban; correction and erasure propagation SLA ≤ 72 hours; breach cooperation; audit rights; termination and deletion; arm's-length consideration with the Companies Act s.188 approval reference where consideration is payable (shared-services register; **[VERIFY — open: related-party status, CS]**).

### AA.12.2 Who can be in the registry

Professional types (`dir.professional_types`, G): `advocate`, `ca`, `cs`, `cma`, `registered_valuer`, `process_agent`, `document_writer` **[VERIFY — open: State licensing of deed/document writers]**. Each type has its own field allow-list, verification sources and re-verification cycle. A record is created only by the professional (self-registration or claiming an invitation from a tenant) — **never by bulk import** of Bar Council rolls or institute directories (`DIR_BULK_IMPORT_FORBIDDEN`; NN-39). Tenant-uploaded vendor lists create **invitations**, not records; a record exists only when the professional accepts and consents.

### AA.12.3 Field allow-lists (L)

| Type | Displayable fields (each needs per-field display consent) | Filter-only metadata (never displayed; pending counsel) | Never stored in the display record |
|---|---|---|---|
| `advocate` | Name; address, telephone, e-mail; enrolment number, enrolment date, State Bar Council of original and current enrolment; Bar Association; professional and academic qualifications; areas of practice (BCI r.36 Schedule) + Equator verification badge text (Appendix S §4.5(d)) | Languages; courts of practice; districts (J2-090) | Ratings, reviews, testimonials, fees or ranges, client names or logos, win or recovery statistics, photo, video, "featured/top/recommended/expert" labels, "hire now" CTA |
| `ca`, `cs`, `cma` | Name; membership number; firm name; city; "Chartered Accountant" / "Company Secretary" / "Cost Accountant"; verification status | Languages; districts | As above; plus no service write-ups for CMAs; no contact details for CMAs on third-party platforms per ICMAI 2025 **[VERIFY — open]** |
| `registered_valuer` | Name; registration number and asset class; city; verification status | Districts | Fees; ratings |
| `process_agent`, `document_writer` | Business name; registration; service districts; contact | — | Ratings outside tenant |

CI `R36_PROFILE_ALLOW_LIST` enforces the table for every API response and rendered view. Display order: alphabetical or seeded-random only (`DIR_SORT_NOT_ALLOWED`).

### AA.12.4 Consent per purpose

| Purpose code | Meaning | Default | Recipients named in notice |
|---|---|---|---|
| `registry_record` | Hold and verify my record | Required to exist | Owner |
| `tenant_invitations` | Tenants may find my record to invite me to their panel (authenticated tenant users only; no public search) | OFF until the professional opts in | Consumers listed by name |
| `group_share_finbyx` | Make my profile available to lender clients of Finbyx for engaging me in execution, registration and recovery matters | OFF (separate toggle) | Finbyx and its lender tenants |
| `group_share_udofin` | Same, for Udofin | OFF | Udofin and its partner tenants |
| `group_share_lawdocs` | Same, for LawDocs document and eSign services | OFF | LawDocs |
| `equator_engagement` | Equator enterprise tenants may engage me | OFF | Equator and its tenants |
| `postres_panel` | List me on the Equator Post-Resolution Advocate Panel (AA.11.4) | OFF | Equator |
| `conflict_screening` | Use my panel memberships to prevent conflicts when I am considered as a neutral | ON when the professional is also a neutral; explained | Equator conflict engine |
| `public_display` | Public search (only when `directory.public_professionals` ON) | OFF | Public |

Consent is free, specific, informed and by affirmative action (DPDP s.6); withdrawal is as easy as granting (one toggle) and propagates (AA.12.7). Consent artefacts (notice version, purpose, recipients, timestamp, channel) are stored in `dir.consents` and exportable. s.7(a) covers using an advocate's details in a case where she appears; it does not cover directory reuse [RE F4.3].

### AA.12.5 Provenance, verification and freshness

- **Provenance** per field: `source` ∈ `self_entered` | `staff_verified_official_portal` | `council_api_permitted` (only where the Council's written permission is on file; `KYC_PORT.lookupBarRoll.{state}` OFF per State) | `institute_certificate` | `tenant_supplied_pending_confirmation`; `source_url`, `source_captured_at`, `evidence_hash` (SHA-256 of the screenshot or document in Object Lock storage).
- **Verification (two-person):** `registry_verifier` A captures evidence; `registry_verifier` B (different user, `DIR_VERIFIER_SAME_PERSON` 403) confirms; result `verified` | `mismatch` | `unverifiable`. Advocates: enrolment and Certificate of Practice (5-year cycle; BCI CoP Rules 2015 r.9.1) plus Equator annual check; CA/CS/CMA: membership and certificate of practice where applicable; valuers: registration.
- **Freshness:** `last_confirmed_by_professional_at`; at 12 months the record shows "details last confirmed {date}" to consumers; at 18 months it is hidden from tenant search until reconfirmed (s.8(3) accuracy); verification `reverify_due` triggers tasks at T-30; a lapsed CoP or a suspension by a Council sets `status = lapsed | suspended_by_council` and emits an update event within 1 hour of staff recording it.

### AA.12.6 Professional Panel Register (surface (iii), tenant-private)

| Object | Purpose | Visibility |
|---|---|---|
| `dir.panel_registers` | A tenant's named panel (e.g., "Recovery advocates — Rajasthan") | Tenant users with `panel_register_admin`/`panel_register_user` |
| `dir.panel_invitations` | Invite by e-mail/mobile or from records consented to `tenant_invitations` | Tenant |
| `dir.panel_memberships` | Accepted membership with the tenant's panel terms version | Tenant; conflict signal F2 only |
| `dir.rfqs`, `dir.rfq_responses` | Tenant asks panel members for quotes for a batch of matters (matters referenced opaquely) | Tenant and invited members only |
| `dir.engagements` | Tenant's engagement of a professional for a matter (opaque `matter_ref`) | Tenant and that professional |
| `dir.sla_policies` | Turnaround and reporting expectations | Tenant and members |
| `dir.tenant_notes` | Private vendor-management notes | Tenant only; **never** shared across tenants or consumers, never exported to the registry master, never used for ranking anywhere |

Rules (L): the tenant pays for panel management (RS-30) by tenant, seat or module — **never per engagement, per referral or by success** (`DIR_PER_ENGAGEMENT_PRICING_FORBIDDEN`); professionals never pay; no rating fields exist outside `dir.tenant_notes`; tenant analytics are limited to the tenant's own panel; cross-tenant analytics are aggregate counts by State and type only (k ≥ 10).

### AA.12.7 Correction, withdrawal and erasure propagation

```
Professional edits / withdraws consent / requests erasure
 → dir.professional_records updated; outbox emits equator.dir.record.updated|withdrawn|erased.v1
 → each consumer that received the record (dir.distribution_log) must apply and ACK within 72 h (G ≤ 72)
 → no ACK at 24 h: reminder; at 72 h: DIR_PROPAGATION_OVERDUE incident to the consumer's DPO and the Owner's DPO
 → nightly ReconciliationRun compares consumer projection hashes; drift → task
```

Erasure removes display fields everywhere; tenants keep only what law requires for engagements already made (contract and tax records), flagged `retained_for_legal_obligation` with the basis. A professional can see **who received their data and when** (`GET /v1/registry/me/distribution`).

### AA.12.8 Registry API for consumers

OAuth2 client credentials per consumer entity; every call carries `Equator-Purpose: <purpose_code>` and returns only records whose consent covers that purpose and recipient (`DIR_PURPOSE_NOT_GRANTED`, 403). Endpoints in AA.18. Rate limits per consumer; every response logged in `dir.access_logs` (consumer, tenant_ref, purpose, record IDs). No bulk export endpoint; search requires a filter set (type + State at minimum) and returns ≤ 50 results per page. The API never returns records to unauthenticated users while `directory.public_professionals` is OFF.

### AA.12.9 Data-principal rights

Access (s.11), correction and erasure (s.12) and grievance (s.13) through `/registry/me` with the same effort as sign-up; DSR clocks per Appendix Q; responses cover the Owner and, through propagation, consumers.

---

## AA.13 Marketplace governance documents (policy registry, Appendix U §U.1 workflow)

| # | Document (version key) | Public URL | Owner (maker) | Approver (checker) | Key contents |
|---|---|---|---|---|---|
| AA-1 | Marketplace User Terms `MUT-2026.1` | `/marketplace/terms` | Company Secretary | General Counsel | Equator as marketplace; bookings are private engagements; no administration, appointment or guarantee; fees and refunds; complaint route; governing law (Appendix U §U.6 cl. 12 pattern) |
| AA-2 | Marketplace Provider Terms `MPT-2026.1` | `/marketplace/provider-terms` | Company Secretary | General Counsel; Board for fees | Seller duties (accuracy, E-Commerce r.6), take and fees, tax data, payouts, holds, reviews licence (listing + 30 days), enforcement ladder, run-off, export, data roles, no off-platform diversion of booked work, liability cap |
| AA-3 | Provider Code of Conduct `MPC-2026.1` | `/marketplace/code` | Head of Marketplace | Rules Sub-Committee | Honesty of credentials; conflicts; confidentiality; no outcome promises; no side payments; respectful conduct; accessibility |
| AA-4 | Ranking and Sponsored Listings Policy `MRS-2026.1` | `/marketplace/how-ranking-works` | Head of Marketplace | Compliance officer; counsel | AA.5.3, AA.10.3–AA.10.4 |
| AA-5 | Review Policy `MRV-2026.1` | `/marketplace/review-policy` | Head of Marketplace | Compliance officer | AA.8.1 |
| AA-6 | Content and Takedown Policy `MCP-2026.1` | `/marketplace/content-policy` | Grievance Officer | General Counsel | AA.8.4 |
| AA-7 | Fee Dispute Procedure `MKP-FDP-2026.1` | `/marketplace/fee-disputes` | Head of Marketplace | General Counsel | AA.6.9 |
| AA-8 | Advertising Policy `MAP-2026.1` | `/advertise/policy` | Marketing Manager | Compliance officer; counsel | AA.10.8 |
| AA-9 | Registry Notice and Terms `RPN-2026.1` | `/registry/notice` | Owner's DPO | Owner's General Counsel | AA.12.4 purposes and recipients |
| AA-10 | Post-Resolution Panel Terms `PRP-2026.1` | In-app only | Company Secretary | Counsel | AA.11.4 |
| AA-11 | Group Data-Sharing Agreement `GDSA-2026.1` | Not public | Company Secretary (Owner) | Boards of each party | AA.12.1 |

Material changes to AA-1, AA-2, AA-9 give 30 days' notice and, where fresh consent is needed, a re-consent prompt (Appendix U §U.1).

---

## AA.14 Revenue hooks (Appendix AB stream registry)

Appendix AB owns the stream registry model (`rev.streams`, `rev.stream_versions`, `rev.stream_transitions`), stream codes RS-01…RS-57, neutrality ratings N0–N4, the state machine (draft → in review → approved → live ↔ paused → retired; forced pause by kill switch) and kill switches (D3-08; AB §AB.2). This appendix raises the following streams; each is switchable and its launch state is the AB catalogue default (AB §AB.3).

| Stream (AB code per RB) | What | Payer | Pricing unit | Guardrail (L) | Initial state |
|---|---|---|---|---|---|
| RS-18 Marketplace take (N2) | % of non-advocate provider fees on surface (ii) bookings; flat per booking for advocate-neutrals (charged to buyer) | Provider (deducted) / buyer (flat) | `pct_of_eligible_booking` by plan; `flat_per_booking` | Flat per plan; never on administered cases; deny X-19; X-62 | Live with surface (ii) once tax memo recorded |
| RS-18 scope: service providers | % on ancillary bookings (`marketplace.take_rate.service_providers`) | Service provider | `pct_of_eligible_booking` | Same | Draft until Board rate |
| RS-52 Buyer processing fee (N1) | Equator payment and escrow service | Buyer | Flat or disclosed % as separate line | Never hidden; never on administered cases | **OFF** |
| RS-09 Chambers SaaS | Workspace required for neutral/chambers listings | Chambers | Plan | Never affects Equator allocation (RA-4) | ON |
| RS-19 Sponsored listing | AA.10 | Eligible non-advocate neutrals and chambers | Slot-month | NN-34; `marketplace.paid_placement` | **OFF** |
| RS-25 Display advertising | AA.10.8 | Allowed advertisers | Slot-month or CPM | Policy list; page tags | **OFF** |
| RS-37 / RS-38 Page themes and custom domains | Chambers profile extras built in Appendix W | Chambers tenants | Add-on | Never affects ranking or listing (deny X-18) | Per AB |
| RS-57 Service-provider tools plan (N1) | Optional tools (calendar sync, team seats, own-data analytics) | Service providers (`mkp.providers.kind = 'service_provider'`) | `per_tenant_month` | Listing stays free without the plan; the plan never affects ranking, badges, reviews, sponsored eligibility or take (`RANKING_IGNORES_PAID`); never sold to advocates, CAs, CSs or CMAs | **OFF** (`mkp.provider_subscriptions`) until Board prices |
| RS-30 Panel management (N0) | AA.12.6 | Tenants (lenders, enterprises) | Tenant + seat | Never per engagement/referral; professionals never pay | **OFF** until D3-05 owner designated and GDSA signed (AB-R7) |
| RS-31 Public professional search | — | — | Free; no fees from listed professionals | NN-39 | **OFF** |
| RS-16 Virtual hearing-room rental | Equator's own room product | Ad hoc tribunals, chambers, advocates | Room-hour | "Room hosted on Equator" | ON after P04 GA |
| RS-17 Venue partner commission | `SVC-VEN` bookings | Venue | Commission | Disclosed partner status | **OFF** |
| RS-15, RS-42–RS-45 One-time products | Transcripts, certified copies, translations, type copies and e-stamp facilitation sold by Equator itself (not by marketplace providers) | Requester | Per item / page / instrument | Labels NN-32; parity within a case | Per AB |
| RS-20 Lead / per-enquiry fees | — | — | — | X-17 | **Prohibited** |
| RS-29, RS-50, RS-51, RS-53 | Referral rewards to professionals; listing/featured/badge fees for professionals; share of advocates' fees or recoveries; paid badges and sort boosts | — | — | X-60; master X-62; deny X-17…X-22 | **Prohibited** (N4) |

Every marketplace invoice line carries `stream_code`; the AB neutrality-exposure tile reports RS-19 and RS-25 revenue as a share of total.

---

## AA.15 Settings catalogue (NN-33 tiers)

Keys follow `<scope>.<module>.<key>`. **L** never tenant-editable; **G** maker ≠ checker, citation, effective dates, preview, rollback, review date, configured fallback; **T** tenant admin with audit and rollback.

| Key | Tier | Default | Bounds / fallback | Who changes (checker) |
|---|---|---|---|---|
| `marketplace.paid_placement` | G | OFF | Board + counsel evidence required | `marketplace_manager` (`compliance_officer`; Board ref) |
| `marketplace.paid_placement.advocates` | L | OFF | — | — |
| `marketplace.advocate_neutrals.listing` | G | OFF | Counsel opinion OI-03 | `legal_reviewer` (`compliance_officer`) |
| `marketplace.institute_neutral.ca` / `.cs` / `.cma` | G | OFF | Institute opinion on file | `legal_reviewer` |
| `marketplace.related_party_sponsorship` | G | OFF | Board + counsel | Board ref |
| `directory.public_professionals` | G | OFF | Counsel opinion **and** SLP (C) 25794/2024 decided | `legal_reviewer` (Board ref) |
| `register.ca` / `register.cs` / `register.cma` | G | OFF | Institute position confirmed | `legal_reviewer` |
| `postres.advocate_panel` | G | OFF | Counsel opinion on PRP-2026.1 | `legal_reviewer` |
| `platform.rev.ads.enabled` | G | OFF | Board; advertiser policy approved | `compliance_officer` |
| `mkp.provider_subscriptions` | G | OFF | Board-approved prices; stream RS-57 `live` (AB) | CFO |
| `platform.mkp.collection_model` | G | `provider_merchant_of_record` | Tax memo | CFO (`legal_reviewer`) |
| `tax_memo.mkp_eco_recorded` | G | false | Blocks paid bookings while false | CFO |
| `billing.eco_gst_tcs` (LR-TAX-008) | G | OFF | Tax memo | CFO |
| `platform.tax.gst_tcs_rate` | G | 0.5% | Notification citation | CFO (tax adviser) |
| `billing.eco_withholding` (LR-TAX-007) | G | OFF | Tax memo | CFO |
| `platform.tax.eco_tds_rate` / `.eco_tds_individual_threshold_minor` | G | 0.1% / ₹5,00,000 | ITA 2025 s.393(1) Sl. 8(v) | CFO |
| `marketplace.paid_placement.max_slots_per_page` (AB key) | G | 2 | 0–2 (L ceiling); 20% of results (L) | `marketplace_manager` (`compliance_officer`) |
| `platform.mkp.sponsored.max_slot_months_per_sponsor` | G | 2 per category-geography | 1–3 | same |
| `platform.mkp.sponsored.rate_card_id` | G | Board-approved card | No unapproved card (`SCHEDULE_NOT_APPROVED`) | CFO |
| `platform.mkp.ranking_policy_version` | G | `MKP-RANK-2026.1` | 30-day notice on change | `marketplace_manager` (`compliance_officer`, legal) |
| `marketplace.take_rate.<plan>` (AB key) | G | 15/15/12/10% | Board; flat only | CFO |
| `marketplace.take_rate.service_providers` | G | 10% [Board] | Flat | CFO |
| `marketplace.advocate_neutral.flat_fee_minor` (AB key) | G | Board | Board + counsel; buyer-side line only | CFO |
| `marketplace.client_processing_fee` (AB key) | G | OFF | Board + counsel | CFO |
| `platform.mkp.hold_days` | G | 14 | 7–21 | `finance_controller` |
| `platform.mkp.payout_sla_days` | T | 3 | 2–7 | `finance_ops` |
| `platform.mkp.payee_cooling_off_hours` | G | 72 | ≥ 48 | `finance_controller` |
| `platform.mkp.new_provider_payout_hold_count` | T | 3 | 1–5 | `finance_ops` |
| `platform.mkp.review.min_n_public` | L | 10 | ≥ 10 (master X-28) | — |
| `platform.mkp.freshness.label_months` / `.hide_months` | G | 12 / 18 | ≤ 12 / ≤ 18 | `marketplace_manager` |
| `platform.mkp.enquiry_response_wd` / `.proposal_validity_days` | T | 2 / 7 | 1–5 / 3–14 | `marketplace_manager` |
| `platform.mkp.search.sort_options` *(v3.1)* | G | `published_order`, `earliest_start`, `price_total_asc`, `name_az`, `nearest_venue` | Never rating, bookings, plan, sponsorship or related-party (L); 30-day notice | `marketplace_manager` (`compliance_officer`) |
| `mkp.search_synonyms` dictionary version *(v3.1)* | G | `MKP-SYN-2026.1` | Targets limited to AA.5.1 filters (L) | `marketplace_manager` (`compliance_officer`) |
| `platform.mkp.conflict_check.validity_days` *(v3.1)* | G | 14 | 7–30 | `marketplace_manager` (`legal_reviewer`) |
| `platform.mkp.slot_hold_minutes` *(v3.1)* | T | 30 | 15–120 | `marketplace_manager` |
| `platform.mkp.on_hold_max_days` *(v3.1)* | T | 30 | 7–60 | `marketplace_manager` |
| `platform.mkp.onboarding.weights` *(v3.1)* | T | AA.4.7 | Total = 100 (L); never read by ranking (L) | `marketplace_manager` |
| `platform.mkp.onboarding.reminder_days` *(v3.1)* | T | 3, 7, 12 | ≤ 3 reminders per step (L) | `marketplace_manager` |
| `platform.mkp.category.<code>.enabled` | G | AA.3.1 | Law check signed | `marketplace_manager` (`legal_reviewer`) |
| `platform.mkp.show_institutional_panel_badge` | G | OFF | — | `compliance_officer` |
| `group.dir.owner_entity_id` | G | unset (registry cannot go live) | Board resolution | `group_admin` (Board ref) |
| `group.dir.propagation_sla_hours` | G | 72 | ≤ 72 | Owner DPO |
| `group.dir.freshness.label_months` / `.hide_months` | G | 12 / 18 | ≤ 12 / ≤ 18 | Owner DPO |
| `group.dir.reverify_months.<type>` | G | 12 | ≤ 12 | `registry_steward` |
| `group.dir.consumer.<entity>.purposes[]` | G | none | GDSA schedule | `group_admin` (Owner DPO) |
| `tenant.dir.panel.terms_version` | T | template | Must not add fee-share/referral terms (lint) | `panel_register_admin` |
| `tenant.dir.panel.display_order` | T | alphabetical | alphabetical / seeded-random | `panel_register_admin` |
| `tenant.dir.rfq.default_response_days` | T | 5 | 1–30 | `panel_register_admin` |
| `tenant.mkp.vendor_panel.distribution` | T | round_robin | round_robin / capacity / manual | `enterprise_admin` |
| `tenant.mkp.sla.<metric>` | T | per panel | — | `enterprise_admin` |
| `tenant.mkp.profile.sections_enabled[]` | T | all | Within allow-list | `mkp_provider_owner` |
| `rulepack.IN.mkp.mci_conduct@<v>` | G | empty | Auto-suspends sponsorship for mediators if prohibited | `legal_reviewer` |

The settings UI shows the tier badge, who may change it and whether approval is needed (NN-33).

---

## AA.16 RBAC (additions to Appendix S §6; Cerbos)

New roles: `marketplace_manager`, `marketplace_moderator`, `provider_verifier`, `ad_reviewer` (Operations Platform, `eq-portal-ops`); `mkp_provider_owner`, `mkp_provider_staff` (providers); `registry_steward`, `registry_verifier` (registry owner); `panel_register_admin`, `panel_register_user` (tenant). Existing: `grievance_officer`, `compliance_officer`, `legal_reviewer`, `finance_ops`, `accounts_maker`, `accounts_checker`, `finance_controller`, `enterprise_admin`, `party`, `dpo`, `internal_auditor`.

| Resource → / Role ↓ | Provider record | Listing / profile | Engagement | Payout | Review | Complaint / enforcement | Sponsorship / ads | Ranking policy | Registry record | Tenant panel |
|---|---|---|---|---|---|---|---|---|---|---|
| `party` (buyer) | — | R | C, R, S confirm [own] | — | C [completed, own] | C [own] | R (labelled) | R published | — | — |
| `mkp_provider_owner` | R, U [own] | C, U [own, moderated] | R, U propose [own] | R statements [own]; U payee (cooling-off) | R; reply | R [own]; appeal | C order [eligible] | R | — | — |
| `mkp_provider_staff` | R [own] | U draft [own] | R, U propose [own] | — | R | R [own] | — | R | — | — |
| `marketplace_moderator` | R | S approve/reject [¬own conflicts] | R metadata | — | S moderate | C, U triage | — | R | — | — |
| `provider_verifier` | U verify [two-person] | — | — | — | — | — | — | — | — | — |
| `marketplace_manager` | R, U status | U hide | R | — | R | S E1–E3 | C (maker) rate card, products | C (maker) | — | — |
| `ad_reviewer` | — | — | — | — | — | — | S creative (maker) | — | — | — |
| `compliance_officer` | R | R | R | — | R | S checker; audit | S checker | S checker | — | — |
| `grievance_officer` | R | R | R [complaint] | — | R | C, U, S respond | — | — | — | — |
| `finance_ops` / `accounts_maker` | R tax | — | R | C batch (maker); reconcile [≠ approver] | — | — | R billing | — | — | — |
| `accounts_checker` / `finance_controller` | — | — | — | S approve batch [aal2-pr, limit] | — | — | — | — | — | — |
| `registry_steward` | — | — | — | — | — | — | — | — | R, U status; DSR | — |
| `registry_verifier` | — | — | — | — | — | — | — | — | U verify [two-person] | — |
| `panel_register_admin` | — | — | — | — | — | — | — | — | R [purpose-granted] | C, R, U [tenant] |
| `panel_register_user` | — | — | — | — | — | — | — | — | R [purpose-granted] | R; C RFQ [tenant] |
| `enterprise_admin` | — | R | C procurement [org] | — | — | C [org] | — | R | — | via panel roles |
| `internal_auditor` | R | R | R | R | R | R | R | R | R [grant] | R [grant] |

Hard `DENY` rules: case roles (`case_manager`, `registrar`, Panel Bench, APPT, CHAL, AI principals) on `mkp:sponsorship` and `mkp:ad`; any principal on `dir:tenant_notes` outside its tenant; any principal approving a payout batch it prepared or releasing a payout to a payee it created or changed (NN-36); `enterprise_*` on neutral procurement (AA.9.1); AI principals on ranking, review moderation decisions and enforcement decisions (NN-01).

---

## AA.17 Data model (DDL sketches; Appendix F conventions; UUIDv7; money in minor units; RLS)

```sql
-- mkp (Equator cluster; tenant RLS; audit on every write)
mkp.provider_categories(code PK, rulepack_ref, public_name_i18n jsonb, reviews_allowed bool, sponsor_eligible bool,
  take_applies bool, enabled bool, law_check_signed_by uuid, law_check_signed_at timestamptz, version int)
mkp.providers(id, kind CHECK (kind IN ('neutral','chambers','service_provider')), person_id NULL, organisation_id NULL,
  chambers_tenant_id NULL, ref text UNIQUE, status text CHECK (status IN ('draft','submitted','kyc_pending','info_requested',
  'verifying','agreement_pending','payout_setup','profile_draft','profile_review','listed','suspended','delisted','withdrawn',
  'closed','rejected','paused','archived')), declared_professions text[], is_advocate bool NOT NULL DEFAULT false,
  institute_member text NULL, related_to_equator bool NOT NULL DEFAULT false, gst_status text, gstin text NULL, pan_masked text,
  last_confirmed_at timestamptz, created_at, updated_at,
  CHECK (num_nonnulls(person_id, organisation_id) = 1))
mkp.provider_category_links(provider_id, category_code, status CHECK (status IN ('pending','listed','hidden','removed')), reason, PRIMARY KEY (provider_id, category_code))
mkp.provider_credentials(id, provider_id, category_code, credential_type, number_masked, issuer, valid_until date,
  source text, source_url, evidence_hash char(64), verifier_1 uuid, verifier_2 uuid, verified_at, result,
  CHECK (verifier_1 IS NULL OR verifier_1 <> verifier_2))
mkp.provider_agreements(id, provider_id, doc_key text, version text, esign_request_id, accepted_at)
mkp.payee_accounts(id, provider_id, account_ref_enc bytea, ifsc, name_match_score numeric(4,3), oob_confirmed_at,
  cooling_off_until timestamptz, created_by uuid, approved_by uuid, CHECK (created_by <> approved_by))
mkp.listings(id, provider_id, slug UNIQUE, profile jsonb, field_consents jsonb, published_version int, status, moderated_by, moderated_at)
mkp.service_offerings(id, provider_id, category_code, method, fee_model CHECK (fee_model IN ('fixed','per_session','per_hour',
  'per_page','per_word','per_day','sliding')), price_minor bigint, currency char(3), gst_treatment, refund_policy jsonb, modes text[], languages text[])
mkp.availability_windows(id, provider_id, from_ts, to_ts, capacity int)
mkp.ranking_policies(id, version UNIQUE, params jsonb, published_page_hash char(64), effective_from, approved_by, legal_signoff_by)
mkp.enquiries(id, buyer_user_id, provider_id, category_code, payload_enc bytea, status, created_at, expires_at)
mkp.enquiry_messages(id, enquiry_id, sender, body_enc bytea, lint_flags text[], created_at)
mkp.conflict_checks(id, enquiry_id, method text[], result CHECK (result IN ('clear','disclosable','hard')), disclosure_doc_id NULL, at)
mkp.engagements(id, enquiry_id, provider_id, chambers_case_id NULL, joint_booking bool, status, scope jsonb, fee_disclosure jsonb,
  terms_versions jsonb, confirmed_at, completed_at)
mkp.engagement_parties(engagement_id, party_user_id, role, confirmed_at, PRIMARY KEY (engagement_id, party_user_id))
-- v3.1: engagements.status adds 'conflict_recheck','conflict_blocked','on_hold','partially_completed'; columns on_hold_reason, on_hold_until
mkp.slot_holds(id, provider_id, engagement_id, slot tstzrange, expires_at, released_at,
  EXCLUDE USING gist (provider_id WITH =, slot WITH &&) WHERE (released_at IS NULL))      -- v3.1 R4
mkp.readiness_checks(engagement_id, check_code, status CHECK (status IN ('pass','fail')), reason_code, checked_at)   -- v3.1; latest row per check
mkp.search_synonyms(id, dictionary_version, locale, phrase, target_kind CHECK (target_kind IN ('category','dispute_type','method','language')),
  target_code, approved_by, checker)                                                       -- v3.1 G object
mkp.saved_searches(id, user_id, filters jsonb, alert_weekly bool, created_at)              -- v3.1; max 5 per user
mkp.onboarding_progress(provider_id PK, score int CHECK (score BETWEEN 0 AND 100), next_action_code, blocking jsonb, eta_date, computed_at)  -- v3.1
mkp.milestones(id, engagement_id, label, amount_minor, status CHECK (status IN ('due','disputed','released','refunded')), due_at, released_at)
mkp.tax_lines(id, engagement_id, milestone_id, kind CHECK (kind IN ('gst_on_take','gst_tcs','eco_tds')), base_minor, rate numeric(6,4), amount_minor, period char(7))
mkp.payout_batches(id, prepared_by_run, approved_by uuid, second_approver uuid NULL, released_at, reconciled_by uuid,
  CHECK (reconciled_by IS NULL OR reconciled_by <> approved_by))
mkp.payout_lines(id, batch_id, provider_id, gross_minor, take_minor, tcs_minor, tds_minor, refund_minor, net_minor, stream_code)
mkp.reviews(id, engagement_id, reviewer_user_id, item_scores jsonb, pressured text, body_enc bytea, status, published_at,
  UNIQUE (engagement_id, reviewer_user_id))
mkp.review_moderation(id, review_id, decision, reason_code, moderator, at) · mkp.review_replies(id, review_id, body, at)
mkp.complaints(id, ref, complainant_kind, provider_id, engagement_id NULL, categories text[], severity, status,
  ack_due_at, redress_due_at, copy_sent_at, nch_ref NULL)
mkp.enforcement_actions(id, provider_id, level CHECK (level IN ('E1','E2','E3','E4','E5','interim')), reasons text NOT NULL,
  decided_by uuid[], effective_from, effective_to, appeal_id NULL)
mkp.appeals(id, enforcement_action_id, filed_at, panel uuid[], decision, decided_at)
mkp.takedown_requests(id, target_kind, target_id, category, received_at, due_at, action, reasons)
mkp.sponsorship_products(id, category_code, geography, price_minor, rate_card_id, active)
mkp.sponsorship_orders(id, provider_id, product_id, month date, status CHECK (status IN ('requested','eligibility_failed',
  'creative_review','approved','active','ended','refunded','cancelled')), approved_by, checker, mandate_id, UNIQUE (provider_id, product_id, month))
mkp.sponsored_impressions_daily(product_id, order_id, day date, impressions int, PRIMARY KEY (order_id, day))  -- aggregate only
mkp.ad_policy_categories(code PK, allowed bool, notes) · mkp.ad_advertisers(id, organisation_id, category_code, kyb_status)
mkp.ad_campaigns(id, advertiser_id, slot, month, status, approved_by, checker) · mkp.ad_creatives(id, campaign_id, asset_ref, copy, lint_result)
mkp.dark_pattern_audits(id, year, report_doc_id, certificate_doc_id, signed_by uuid[], findings jsonb, status)
mkp.procurement_requests(id, tenant_id, category_code, rows_ref, rfq jsonb, status) · mkp.procurement_responses(id, request_id, provider_id, quote_minor, terms)
mkp.enterprise_vendor_panels(id, tenant_id, name, distribution, sla_policy jsonb) · mkp.vendor_panel_members(panel_id, provider_id, accepted_at)
mkp.postres_choices(id, case_id, case_party_id, choice CHECK (choice IN ('legal_aid','own_professional','equator_panel','in_person')),
  options_shown jsonb, order_seed text, record_ref NULL, consented_at)   -- append-only
mkp.fraud_signals(id, subject_kind, subject_id, signal, score, at, status)
mkp.transparency_reports(id, quarter, query_pack_version, dataset_hash, approved_by, published_at)

-- dir (grp-registry cluster; RLS by consumer_entity_id and tenant_ref; append-only history tables)
dir.professional_types(code PK, display_allow_list text[], filter_only text[], reverify_months int, sources text[])
dir.professional_records(id, person_ref uuid, professional_type, status CHECK (status IN ('pending','active','lapsed',
  'suspended_by_council','withdrawn','erased')), last_confirmed_by_professional_at, reverify_due date, erasure_requested_at NULL, version int)
dir.record_fields(record_id, field_key, value_enc bytea, display_consent bool, source, source_url, source_captured_at,
  evidence_hash char(64), PRIMARY KEY (record_id, field_key))
dir.verification_tasks(id, record_id, field_keys text[], verifier_1, verifier_2, result, at, CHECK (verifier_1 <> verifier_2))
dir.consents(id, record_id, purpose_code, recipients text[], notice_version, granted_at, withdrawn_at NULL, channel)
dir.consumers(id, legal_entity_id, name, gdsa_id, allowed_purposes text[], oauth_client_id, status)
dir.gdsa_agreements(id, version, parties uuid[], s188_ref text NULL, effective_from, effective_to, doc_id)
dir.distribution_log(id, record_id, consumer_id, tenant_ref NULL, purpose_code, record_version, sent_at)
dir.propagation_acks(event_id, consumer_id, acked_at, PRIMARY KEY (event_id, consumer_id))
dir.reconciliation_runs(id, consumer_id, run_at, drift_count, details_ref)
dir.panel_registers(id, consumer_id, tenant_ref, name, terms_version, display_order)
dir.panel_invitations(id, register_id, invitee_contact_hash, record_id NULL, status, sent_at)
dir.panel_memberships(id, register_id, record_id, accepted_terms_version, status, since, until)
dir.rfqs(id, register_id, matter_refs_opaque text[], scope jsonb, due_at) · dir.rfq_responses(id, rfq_id, record_id, quote_minor, terms, at)
dir.engagements(id, register_id, record_id, matter_ref_opaque, started_at, ended_at)
dir.sla_policies(id, register_id, metrics jsonb)
dir.tenant_notes(id, register_id, record_id, body_enc bytea, author, at)   -- never leaves tenant_ref
dir.access_logs(id, consumer_id, tenant_ref, purpose_code, record_ids uuid[], at) -- partitioned by month
dir.dsr_requests(id, record_id, kind, received_at, due_at, status)
dir.blocked_source_hosts(host PK, reason)   -- read by NO_ROLL_SCRAPING lint
```

No table in `mkp` or `dir` has a rating, rank-boost or sponsorship column for advocates or institute members (by design; schema lint).

---

## AA.18 APIs (`/v1`; OpenAPI 3.1; Idempotency-Key on creating POSTs; RFC 9457 errors)

| Method and path | Purpose | Caller |
|---|---|---|
| GET `/public/marketplace/search` · GET `/public/marketplace/providers/{slug}` · GET `/public/marketplace/ranking-policy` · GET `/public/marketplace/transparency/{quarter}` | Search (filters only from AA.5.1; unknown `sort` → `MKP_SORT_NOT_ALLOWED`), profile, policy, report | public |
| GET `/public/marketplace/sponsored?category=&geo=` | Sponsored block (empty while flag OFF; never with `case_context`) | public |
| POST `/mkp/providers` · PATCH `/mkp/providers/{id}` · POST `/mkp/providers/{id}:submit` | Application | applicant |
| POST `/mkp/providers/{id}/credentials/{cid}:verify` | Two-person verification step | `provider_verifier` |
| POST `/mkp/providers/{id}/agreements` · POST `/mkp/providers/{id}/payees` · POST `/mkp/payees/{pid}:approve` | Terms; payee with cooling-off | provider; `finance_ops` checker |
| PUT `/mkp/listings/{id}` · POST `/mkp/listings/{id}:moderate` | Profile; moderation | provider; moderator |
| POST `/mkp/enquiries` · POST `/mkp/enquiries/{id}/messages` · POST `/mkp/enquiries/{id}/conflict-checks` | Enquiry; messages; conflict check | buyer; provider |
| POST `/mkp/engagements` · POST `/mkp/engagements/{id}:invite-counterparty` · POST `/mkp/engagements/{id}:confirm` | Proposal; joint booking; explicit confirmation | provider; parties |
| GET `/mkp/engagements/{id}/readiness` · POST `/mkp/engagements/{id}/slot-holds` · POST `/mkp/engagements/{id}:hold` · `:resume` · `:substitute` · `:close-partial` *(v3.1)* | Ready-to-pay checklist (R1–R7); slot hold; on hold; substitution; partial completion | parties; provider; chambers admin |
| GET `/public/marketplace/search?q=&…&sort=` · POST `/mkp/saved-searches` · GET `/mkp/providers/me/onboarding` *(v3.1)* | Query-to-filter relevance with chips; saved searches; onboarding progress and next action | public; buyer; applicant |
| POST `/mkp/milestones/{id}:release` · POST `/mkp/milestones/{id}:dispute` · POST `/mkp/fee-disputes` | Milestones; fee disputes | buyer; provider |
| POST `/mkp/payout-batches/{id}:approve` · POST `/mkp/payout-batches/{id}:reconcile` | Payouts (SoD) | `accounts_checker`; `accounts_maker` |
| GET `/mkp/providers/me/statements?period=` | Statements incl. TCS/TDS | provider |
| POST `/mkp/reviews/{token}` · POST `/mkp/reviews/{id}:moderate` · POST `/mkp/reviews/{id}/replies` | Reviews | participant; moderator; provider |
| POST `/public/marketplace/complaints` · POST `/mkp/complaints/{id}:triage` · POST `/mkp/enforcement-actions` · POST `/mkp/enforcement-actions/{id}/appeals` | Complaints and due process | public; `grievance_officer`; panel; provider |
| POST `/mkp/takedowns` | Takedown | public / authority |
| POST `/mkp/sponsorship-orders` · POST `/mkp/sponsorship-orders/{id}:approve` | Sponsored listing orders (`MKP_PAID_PLACEMENT_OFF` while flag OFF) | provider; `ad_reviewer`, `compliance_officer` |
| POST `/mkp/ad-campaigns` · POST `/mkp/ad-campaigns/{id}:approve` | Display ads (`platform.rev.ads.enabled`) | advertiser; reviewers |
| POST `/mkp/dark-pattern-audits` · POST `/mkp/dark-pattern-audits/{id}:certify` | Annual self-audit | `compliance_officer` + second signer |
| POST `/mkp/procurement-requests` · POST `/mkp/procurement-requests/{id}/responses` · POST `/mkp/vendor-panels` | Enterprise procurement | `enterprise_admin`; provider |
| POST `/cases/{caseId}/postres-choices` · GET `/cases/{caseId}/postres-options` | Post-resolution chooser | party |
| **Registry** (served by `services/registry`; consumer OAuth; `Equator-Purpose` header) | | |
| POST `/registry/me` · PATCH `/registry/me/fields` · PUT `/registry/me/consents/{purpose}` · GET `/registry/me/distribution` · POST `/registry/me/dsr` | Professional self-service | professional |
| POST `/registry/records/{id}/verification-tasks` · POST `/registry/verification-tasks/{id}:confirm` | Two-person verification | `registry_verifier` |
| GET `/registry/search?type=&state=&…` | Consumer search within purpose (≤ 50/page; no bulk) | consumer |
| GET `/registry/records/{id}` | Record within purpose | consumer |
| POST `/registry/events/{eventId}:ack` | Propagation ACK | consumer |
| POST `/registry/panels` · POST `/registry/panels/{id}/invitations` · POST `/registry/panels/{id}/rfqs` · POST `/registry/rfqs/{id}/responses` · POST `/registry/panels/{id}/engagements` | Tenant-private panel register | tenant roles; professional |

---

## AA.19 Events (CloudEvents `equator.<context>.<entity>.<verb>.v1`; IDs and codes only, never PII)

**mkp:** `provider.status_changed` · `credential.verified` · `credential.expired` · `listing.published` · `listing.hidden` · `enquiry.created` · `enquiry.expired` · `conflict_check.completed` · `engagement.proposed` · `engagement.confirmed` · `engagement.completed` · `milestone.released` · `milestone.disputed` · `fee_dispute.decided` · `payout_batch.approved` · `payout.released` · `payee.changed` · `review.published` · `review.removed` · `complaint.received` · `complaint.redressed` · `enforcement.decided` · `appeal.decided` · `takedown.completed` · `sponsorship.activated` · `sponsorship.ended` · `ad_campaign.approved` · `ranking_policy.published` · `dark_pattern_audit.certified` · `transparency_report.published` · `postres_choice.recorded` · `procurement.awarded` · *(v3.1)* `provider.onboarding_progressed` · `conflict_check.rechecked` · `engagement.conflict_blocked` · `engagement.on_hold` · `engagement.resumed` · `engagement.substituted` · `engagement.partially_completed` · `slot_hold.expired`.

**dir:** `record.created` · `record.updated` · `record.verified` · `record.stale` · `record.withdrawn` · `record.erased` · `consent.granted` · `consent.withdrawn` · `panel_membership.created` · `panel_membership.ended` · `propagation.acknowledged` · `propagation.overdue` · `reconciliation.drift_detected` · `access.logged` (aggregate hourly).

Example: `equator.dir.record.erased.v1` `{record_id, version, erased_fields[], due_by}`. `equator.dir.panel_membership.created.v1` is the only event the Equator conflict engine consumes from `dir` (flow F2).

---

## AA.20 Error codes (register in Appendix F §F.10.4 (v3))

| Code | HTTP | Meaning |
|---|---|---|
| `MKP_PAID_PLACEMENT_OFF` | 409 | Sponsored listings are not enabled |
| `MKP_SPONSOR_INELIGIBLE` | 422 | Provider fails `sponsor_eligible()` (detail lists condition) |
| `MKP_SPONSOR_SLOT_CAP` | 409 | No sponsored inventory left for that category-geography-month or sponsor cap reached |
| `MKP_SORT_NOT_ALLOWED` | 400 | Sort parameter not in the published policy |
| `MKP_SURFACE_FORBIDDEN` | 403 | Cross-surface access attempted |
| `MKP_CATEGORY_DISABLED` | 409 | Category law check not signed or category OFF |
| `MKP_PROFESSIONAL_NOT_ALLOWED` | 422 | Advocate or institute member cannot list in this category (AA.3.2) |
| `MKP_LABEL_FORBIDDEN` | 422 | Profile or creative contains a forbidden label or claim |
| `MKP_PROVIDER_NOT_LISTED` | 409 | Provider not in `listed` |
| `MKP_CONFLICT_HARD` | 409 | Hard conflict found |
| `MKP_CONFLICT_CHECK_REQUIRED` *(v3.1)* | 409 | No valid conflict check (or unacknowledged disclosure) for the current party set |
| `MKP_CONFLICT_CHECK_STALE` *(v3.1)* | 409 | Conflict check older than the validity period; re-check running |
| `MKP_SLOT_UNAVAILABLE` *(v3.1)* | 409 | Proposed slot is held or booked; next free slots returned |
| `MKP_SYNONYM_FORBIDDEN_TARGET` *(v3.1)* | 422 | Search dictionary entry maps to a provider or a forbidden attribute |
| `MKP_ONE_PARTY_ARBITRATION_BLOCKED` | 422 | Arbitrator booking needs every party |
| `MKP_REPEAT_PLAYER_ARBITRATION_BLOCKED` | 422 | Repeat-player vs individual arbitration on surface (ii) |
| `MKP_ENTERPRISE_NEUTRAL_PROCUREMENT_BLOCKED` | 403 | Enterprises cannot procure neutrals for their own disputes |
| `MKP_FEE_DISCLOSURE_REQUIRED` | 409 | Confirmation attempted without accepted fee disclosure |
| `MKP_BOOKING_CONFIRMATION_REQUIRED` | 422 | Explicit confirmation missing |
| `MKP_TAX_MEMO_MISSING` | 409 | Paid bookings blocked until tax memo recorded |
| `MKP_PAYOUT_SOD_VIOLATION` | 403 | Separation of duties breached |
| `MKP_PAYEE_COOLING_OFF` | 409 | Payee in cooling-off |
| `MKP_REVIEW_NOT_ELIGIBLE` | 403 | Reviewer not a participant of a completed engagement |
| `MKP_REVIEW_OUTCOME_ITEM` | 422 | Review form contains an outcome item |
| `MKP_REVIEW_PROFESSIONAL_FORBIDDEN` | 422 | Reviews not allowed for this provider type |
| `MKP_REASONS_REQUIRED` | 422 | Enforcement decision without reasons |
| `MKP_AD_CATEGORY_PROHIBITED` | 422 | Advertiser category not allowed |
| `MKP_AD_PLACEMENT_FORBIDDEN` | 422 | Ad slot on a prohibited page tag |
| `MKP_ADVOCATE_TARIFF_FORBIDDEN` | 422 | Tariff tag for advocate commission, listing, lead or referral |
| `MKP_DARK_PATTERN_AUDIT_OVERDUE` | 409 | Annual self-audit not certified |
| `MKP_OUTCOME_METRIC_FORBIDDEN` | 500 (CI) | Outcome metric computed for a provider |
| `DIR_CONSENT_REQUIRED` | 403 | No consent for this use |
| `DIR_PURPOSE_NOT_GRANTED` | 403 | Purpose not granted to consumer or recipient |
| `DIR_GDSA_MISSING` | 403 | Consumer has no active GDSA |
| `DIR_FIELD_NOT_ALLOWED` | 422 | Field outside the type allow-list |
| `DIR_SORT_NOT_ALLOWED` | 400 | Sort other than alphabetical/seeded-random |
| `DIR_BULK_IMPORT_FORBIDDEN` | 422 | Bulk creation of records attempted |
| `DIR_SOURCE_BLOCKED` | 422 | Source host is a blocked roll portal |
| `DIR_VERIFIER_SAME_PERSON` | 403 | Second verifier same as first |
| `DIR_RECORD_STALE` | 409 | Record hidden for freshness |
| `DIR_PUBLIC_SEARCH_OFF` | 404 | Public professional search disabled |
| `DIR_TENANT_SCOPE` | 403 | Tenant-private data outside its tenant |
| `DIR_PER_ENGAGEMENT_PRICING_FORBIDDEN` | 422 | Panel pricing by engagement, referral or success |
| `DIR_REFERRAL_REWARD_FORBIDDEN` | 422 | Reward to a professional for referral |
| `DIR_PROPAGATION_OVERDUE` | 500 (alert) | Consumer has not applied an update within the SLA |

---

## AA.21 Audit and exports (NN-22, NN-37)

- **Audit:** every state change in `mkp` and `dir` writes a hash-chained audit event (actor, tenant/consumer, before/after digest). Un-disableable edit log on payouts, payees, tax lines and rate cards (NN-36). Registry `access_logs` retained 3 years **[VERIFY — open: retention schedule, Appendix Q]**.
All packages below use the D3-41 / Appendix AC §AC.13 taxonomy, naming and manifest (root ≤ 40 characters, paths below root ≤ 140, AC §AC.13.7); this appendix defines no folder scheme of its own.
- **Provider export** (scope `MARKETPLACE_PROVIDER`, Appendix AC §AC.13.3; individual neutrals may also use `NEUTRAL_PRACTICE` and chambers `CHAMBERS_TENANT`; any time, free; on exit within 7 days): `00_README.pdf` and `00_README.html`; `00_Contents.xlsx`; `01_Organisation_Profile/` (profile DOCX + PDF; credential verification records, not third-party evidence images); `04_Billing_and_Subscriptions/` (invoices and statements PDF + XLSX, TCS/TDS records); `05_Operations/` (engagements register XLSX with proposals and terms as PDF; complaints and decisions as PDF); `08_Reports/` (reviews with replies as XLSX); `99_Manifest/` (`manifest.csv`, `manifest.json` with SHA-256 checksums, `schemas/`); structured data in each folder's `_Data/` subfolder (CSV + JSON).
- **Professional export** (registry; scope `USER_SELF` served by the `dir` service): `01_Organisation_Profile/` (registry record with field provenance and freshness dates), `08_Reports/` (distribution log — "who received my data" — and verification history), `09_Settings_and_Configuration/` (consents history per field and purpose), `99_Manifest/`.
- **Tenant panel export** (part of `ENTERPRISE_TENANT`, folder `05_Operations/Panels/`): registers, memberships, RFQs, engagements, SLA reports, tenant notes (tenant's own data).
- **Regulatory packs:** GSTR-8 data and TDS return data in `STATUTORY_BOOKS` (`04_Billing_and_Subscriptions/`); transparency report dataset, dark-pattern self-audit and sponsored-listing monthly audit in `ASSURANCE_PACK` (`data/08_Reports/`, Appendix AE §AE.8.4).

---

## AA.22 Acceptance tests (selection; full set in P19 §12)

```gherkin
Feature: Equator Marketplace and Professional Registry

Scenario: NO_PAID_PLACEMENT extended to marketplace sponsorship
  Given neutral N holds an active sponsored listing on the Private Practice Marketplace
  When the allocation engine runs for an Equator-administered case where N is eligible
  Then the run inputs contain no attribute derived from any mkp or rev table
  And the organic directory order for /neutrals is identical with and without N's sponsorship

Scenario: Sponsored block is labelled, separate and capped
  Given marketplace.paid_placement is ON and 5 eligible sponsors exist for "Mediation, Rajasthan"
  When a visitor searches mediation in Rajasthan
  Then at most 2 sponsored cards render above the organic list, none inside it
  And each shows "Sponsored — paid placement. Does not affect Equator appointments." adjacent to the name

Scenario: Advocates are never sold placement or reviews
  Given provider P is an enrolled advocate
  When P orders a sponsored listing
  Then the response is 422 with code "MKP_SPONSOR_INELIGIBLE"
  And no review invitation is ever created for P's engagements

Scenario: Repeat-player arbitration booking blocked
  Given a lender initiates an arbitrator booking on surface (ii) against an individual borrower
  Then the response is 422 with code "MKP_REPEAT_PLAYER_ARBITRATION_BLOCKED"

Scenario: One-party arbitration booking blocked
  Given company A requests an arbitrator on surface (ii) in a dispute with company B
  When A tries to confirm the booking before B has joined and confirmed the appointment
  Then the response is 422 with code "MKP_ONE_PARTY_ARBITRATION_BLOCKED"

Scenario: Conflict re-check before payment (v3.1)
  Given a mediator's conflict check was "clear" for buyer X and counterparty Y
  When Y joins and names lender L, on whose recovery panel the mediator sits, as its group company
  Then the readiness check R1 fails and the re-check returns "hard" with reason "counsel_panel_of"
  And any held payment is refunded in full and the engagement is "conflict_blocked"

Scenario: Slot hold prevents double booking (v3.1)
  Given buyer P holds the 10:00 slot of mediator M for 30 minutes
  When buyer Q opens checkout for the same slot
  Then Q receives 409 "MKP_SLOT_UNAVAILABLE" with the next three free slots

Scenario: Sort options never use paid attributes (v3.1)
  Given 30 mediators in Rajasthan, 5 of them sponsors and 8 on paid plans
  When the search is run with each sort in platform.mkp.search.sort_options
  Then toggling sponsorship, plan and review counts changes no organic order
  And sort "rating" returns 400 "MKP_SORT_NOT_ALLOWED"

Scenario: Registry erasure propagates within the SLA
  Given advocate A's record was distributed to Finbyx and Udofin consumers
  When A requests erasure
  Then equator.dir.record.erased.v1 is emitted to both consumers
  And if a consumer has not acknowledged within 72 hours "DIR_PROPAGATION_OVERDUE" is raised to both DPOs

Scenario: No bulk import of roll data
  When a tenant uploads a CSV of 500 enrolment numbers to create registry records
  Then no record is created, invitations are generated instead
  And the response for direct record creation is 422 with code "DIR_BULK_IMPORT_FORBIDDEN"

Scenario: Party chooses the professional
  Given an award holder opens the post-resolution chooser
  Then "Free legal aid" appears first for an individual party
  And the choice, options shown and order seed are recorded in mkp.postres_choices

# NN-39 owner-file scenarios (v3.1; Appendix I I.(i-a) holds the catalogue copies)
Scenario: NN-39_registry_order_never_ranked
  When a consumer requests registry results with sort "rating"
  Then the response is 400 with code "DIR_SORT_NOT_ALLOWED"
  And results with the default sort are in alphabetical or seeded-random order with the seed recorded

Scenario: NN-39_purpose_bound_consumer_access
  Given consumer entity E holds a GDSA whose purpose schedule omits "postres_engagement"
  When E calls the registry API with header "Equator-Purpose: postres_engagement"
  Then the response is 403 with code "DIR_PURPOSE_NOT_GRANTED"
  And no professional record is returned
```

---

## AA.23 Open items and legal verification flags

| # | Item | Default until closed | Owner |
|---|---|---|---|
| AA-OI-01 | *Sulekha v P.N. Vignesh* SLP (C) 25794/2024 and *Anil Pandey v BCI* WP (C) 817/2026 outcomes | `directory.public_professionals` OFF; tenant-private registers only | Counsel |
| AA-OI-02 | Verbatim BCI r.36 proviso and Schedule (Resolution 50/2008); Ch. III r.2; any separate brokerage rule | Allow-list per RE; languages/courts filter-only | Counsel |
| AA-OI-03 | Whether r.36 reaches advocate-neutral marketplace profiles (pack OI-03) | `marketplace.advocate_neutrals.listing` OFF | Counsel |
| AA-OI-04 | E-Commerce Amendment Rules 2026: Gazette text, G.S.R. number, sub-rule numbers, commencement (1 Jan 2027 per one source); characterisation of ADR services after *D.K. Gandhi* | Comply in full from P19 go-live | Counsel |
| AA-OI-05 | Tax memo: ECO status under the split-settlement model (GST s.52 TCS; ITA 2025 s.393(1) Sl. 8(v)); SAC and rate on take; interaction with payer TDS | Paid bookings blocked (`MKP_TAX_MEMO_MISSING`) | Tax adviser; CFO |
| AA-OI-06 | RBI PA Directions 2025 and marketplace transfer holds | Holds only at the PA/escrow bank | Payments counsel |
| AA-OI-07 | ICSI aggregator position; ICMAI 2025 guidelines Gazette date; ICAI fee-sharing clauses | Institute flags OFF | Counsel |
| AA-OI-08 | Mediation Council of India conduct standards for mediators and MSPs (Mediation Act s.38(f), (l)) | Rule pack empty; watch | Legal |
| AA-OI-09 | Registry Owner entity designation; GDSA s.188 approvals; Infrabyx shareholding chain | Registry cannot go live without `group.dir.owner_entity_id` | Company Secretary; Board |
| AA-OI-10 | Bar Council of Delhi representation on roll-portal data (*Aditya Chauhan*, due about Nov 2026) | Manual verification evidence only | Legal |
| AA-OI-11 | Per-State e-stamp vendor authorisation evidence; ISL certification bodies; valuer registration scope; document-writer licensing | Affected categories OFF or evidence-gated | Legal; Ops |
| AA-OI-12 | Board approval: rate card for sponsored listings, take rates, provider subscription prices, display-ad rates | "Subject to Board approval"; no binding quotes | Board |

---

## AA.24 Phase addenda

### For P03

**FR-P03-V3-AA01 — Rename institutional direct hire.** Rename FR-P03-31 "Find a Neutral: direct hire" to "Request this panel neutral", `MarketplaceBookingWorkflow` to `PanelDirectRequestWorkflow`, and case `source` `marketplace` to `panel_direct_request` (legacy alias kept) per X-59. *Acceptance:* no UI string on surface (i) uses "Marketplace"; migration maps existing rows; 0% panel administration fee unchanged.

**FR-P03-V3-AA02 — Extend `NO_PAID_PLACEMENT` and add `MKP_SURFACE_ISOLATION`.** Revoke all grants on `mkp` and `rev` from the allocation, grading, QI, conflict and directory roles; add the AA.10.6 tests to CI. *Acceptance:* both tests fail on a seeded forbidden join and pass on main.

**FR-P03-V3-AA03 — Conflict edges from panels and private engagements.** Consume `equator.dir.panel_membership.created|ended.v1` and closed `mkp` engagements into `core.conflict_edges` (`counsel_panel_of`, `privately_engaged_by`) with only the AA.2.2 F2/F3 payload. *Acceptance:* a neutral on lender L's recovery panel is a hard conflict in any matter involving L; no other `dir` field is readable by the conflict engine.

**FR-P03-V3-AA04 — Paid-visibility item in disclosures.** Pre-fill the s.12(1)/Code disclosure with the AA.10.7 statement when flow F4 reports `has_paid_visibility_24m = true`; the neutral cannot delete it. *Acceptance:* the item appears in the IEP for administered appointments; allocation logs show no read of F4.

### For P05

**FR-P05-V3-AA01 — Marketplace tax engine.** Implement AA.7.3 (GST TCS, GSTR-8 data, RCM/exempt exclusions) and AA.7.4 (ITA 2025 s.393(1) Sl. 8(v) withholding with threshold) behind `billing.eco_gst_tcs` and `billing.eco_withholding`, with rates as G settings. *Acceptance:* golden vectors for registered/unregistered mediators, RCM arbitral tribunal to a business, individual below ₹5 lakh threshold.

**FR-P05-V3-AA02 — Marketplace payouts with SoD.** Payout batches, second approver above authority limit, reconciliation by a third user, payee cooling-off (AA.7.5–AA.7.6). *Acceptance:* `MKP_PAYOUT_SOD_VIOLATION` and `MKP_PAYEE_COOLING_OFF` scenarios pass; edit log cannot be disabled.

**FR-P05-V3-AA03 — Transfer holds and milestone release.** Holds at the PA, ADR-native milestones, deemed release with notice, fee-dispute hold (AA.6.6–AA.6.9). *Acceptance:* no marketplace funds ever settle to an Equator account other than Equator's own fee lines.

**FR-P05-V3-AA04 — Stream codes on lines.** Every marketplace, sponsorship, advertising and panel-management invoice line carries `stream_code` (AB). *Acceptance:* finance dashboard neutrality-exposure tile shows RS-19 and RS-25 shares.

### For P06

**FR-P06-V3-AA01 — Post-Resolution Professional Chooser.** Replace SCR-P06-65 with SCR-P19-30 (AA.11.2, built in P19 FR-P19-45; P06 provides the case-outcome entry point) (legal aid first; own professional; Equator panel behind `postres.advocate_panel`; in person), record `mkp.postres_choices`. *Acceptance:* Gherkin "Party chooses the professional" passes; no ranking, rating or fee field exists in the chooser.

**FR-P06-V3-AA02 — Authorised document transfer.** Item-level authorisation to the chosen professional via scope `court_steps_support` or secure link; `core.disclosures` entries; revocation in one step (AA.11.3). *Acceptance:* revocation ends access in the same transaction.

**FR-P06-V3-AA03 — Retire `/advocates`.** Remove the public route and `advocate_directory.enabled` flag; `core.advocate_listings` becomes a read-only migration view (X-60). *Acceptance:* `/advocates` returns 410 with a link to the help page; no public advocate listing is reachable while `directory.public_professionals` is OFF.

### For P09

**FR-P09-V3-AA01 — Enterprise procurement and the neutral block.** Vendor panels, bulk service requests, RFQs, SLAs and reporting for ancillary services (AA.9.2); `MKP_ENTERPRISE_NEUTRAL_PROCUREMENT_BLOCKED` for neutrals. *Acceptance:* a lender can tender 2,000 notice translations; a lender attempt to empanel mediators returns 403.

**FR-P09-V3-AA02 — Lender Professional Panel Register.** Lender console module for panel registers, invitations, RFQs, engagements and SLAs on the registry (AA.12.6), Finbyx and Udofin connectors through `REGISTRY_PORT` under the GDSA. *Acceptance:* tenant notes never leave the tenant (`DIR_TENANT_SCOPE`); pricing is per tenant/seat only.

**FR-P09-V3-AA03 — External-member flow unchanged.** FR-P09-36 remains Equator-curated (X-59 (d)); POSH external members are never on surface (ii) or sponsor-eligible. *Acceptance:* no POSH category exists in `mkp.provider_categories`.

### For P13

**FR-P13-V3-AA01 — Marketplace public pages.** SSR `/marketplace`, category and profile pages, `/marketplace/how-ranking-works`, `/marketplace/transparency`, `/marketplace/review-policy`, `/marketplace/terms`, `/marketplace/provider-terms`, `/marketplace/advertise` with the operator footer and grievance officer. *Acceptance:* Lighthouse SEO ≥ 95; pages render without JavaScript; Claims Register binds every number.

**FR-P13-V3-AA02 — Display-ad slots in CMS.** Ad slot component allowed only on pages tagged `content`; blocked tags per AA.10.8; first-party serving; "Advertisement" label. *Acceptance:* `MKP_AD_PLACEMENT_FORBIDDEN` when a slot is placed on a forbidden tag; no third-party ad scripts in the bundle.

**FR-P13-V3-AA03 — Dark-pattern certificate display.** Footer badge and `/trust/dark-patterns` page rendering the latest certified self-audit (AA.10.5). *Acceptance:* the page shows date and signer roles; missing certificate after the annual date blocks re-enabling sponsorship.
