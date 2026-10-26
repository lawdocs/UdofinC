# V5 — Workplace & HR (WRK) — Vertical Specification

> Binding for **P08e** (WRK vertical pack). Read with `01_MASTER_PROMPT.md` (v2.0), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, and Appendices A (workflows, ladders, clocks), B (Cards WRK-STD and WRK-POSH), F (canonical tables, events, error codes), G (LR-LAB, LR-POSH and the new rows proposed in §18), K (Dispute Explorer v2, exclusion list §3), L (documents, templates, type copies), M (AI Pleadings Studio). POSH Internal Committee SaaS, the IR Code GRC desk, the HR-policy desk and the whistle-blower desk are specified in **P09** (§4E–4F) and are **linked, not duplicated** here.
>
> Version 2.0 · law stated as at 21 October 2026 · status tags: **[V]** verified against a primary or reliable secondary source in research · **[K]** settled law, not re-fetched · **[VERIFY — open: …]** must be confirmed by counsel before the dependent permissive feature is activated (Appendix G §G.1 fail-safe principle).

---

## 0. Scope and how to use

**0.1 What this file is.** The single build specification for the WRK vertical: taxonomy, law by subtype, suitability and eligibility decision tables, Dispute Explorer branches, intake and submission forms per mechanism with every dropdown value, modus operandi, pre-litigation journey, documents, calculators, outputs, KPIs, data-model extensions and acceptance tests.

**0.2 Precedence.** Master → Appendix G (legal rules) → Appendix B (fees) → Appendix F (names, types, events, errors) → Appendix A (states, clocks) → this file → P08 §4.5. Where this file reconciles a conflict between P08 §4.5 and an appendix, the reconciliation is listed in §0.4 and must be recorded by the agent in `docs/adr/` (master §15).

**0.3 How the agent uses it.**
1. Seed `core.dispute_types` with the §2 taxonomy (L1 = `dispute_type.code`, L2 = `sub_types[]`), each L2 carrying `blocked_mechanisms[]` derived from §4.
2. Encode §4 decision tables in `packages/rules/verticals/wrk/` as pure functions: `wrk_is_worker()`, `wrk_arbitrability()`, `wrk_route()`, `wrk_limitation()`, `wrk_signposts()`. No AI in any of these (NN-01, NN-02).
3. Build the §6 form schemas in the P02 form engine (`F-WRK-NN`), EN + HI at launch.
4. Implement §12 calculators with golden vectors as unit tests.
5. Add §16 migrations; write §17 scenarios as Gherkin in `tests/acceptance/wrk/`.
6. Register new legal rules (§18.2) with status `UNVERIFIED` where marked; permissive features stay behind flags OFF.

**0.4 Reconciliations made in this file (binding; record as ADRs).**

| # | Topic | P08 §4.5 says | Appendix says | Resolution in V5 |
|---|---|---|---|---|
| R1 | F&F clock name | `wrk_ff_2wd` | App. A §6.3: `wrk_wages_2wd` | Use **`wrk_wages_2wd`** (App. A prevails); `wrk_ff_2wd` is an alias accepted by the seed loader only |
| R2 | Worker-arbitration error | `WRK_WORKMAN_ARBITRATION` 409 | App. F §F.10.1: `WRK_WORKMAN_ARBITRATION_BLOCKED` 422 | Use **`WRK_WORKMAN_ARBITRATION_BLOCKED` (422)** |
| R3 | Establishment size enum | `lt_10, 10_19, 20_49, 50_99, 100_299, 300_plus` | App. F `wrk.employment_records`: `lt_10, 10_49, …` | **P08 bands are correct in law** (20 = GRC threshold, IR Code s.4). App. F CHECK must be migrated to the six bands (§16.1, migration `wrk_0002`) |
| R4 | Worker status column | `workman_status` (text) | App. F: `is_workman boolean` | Keep **`is_workman` nullable boolean** as the guard column (NULL = uncertain → treated as worker); store the full assessment in `wrk.worker_assessments.status` (`worker`, `non_worker`, `uncertain`) |
| R5 | Terminology | "workman" | IR Code uses "worker" (s.2(zr)) | UI and templates say **"worker"**; "workman" survives only in legacy identifiers |
| R6 | WRK mechanism default for money claims of non-workers | mediation | S4 PL-02 | Recommend **A&C Part III conciliation** where the respondent is an organisation and an enforceable outcome is wanted (s.73/s.74); mediation otherwise (§4.6) |
| R7 | Gig/platform arbitration | P08 lists "arbitration (commercial contract)" for `wrk.contractor_gig` | S4 A1.1 (adhesion; unequal bargaining) | **Blocked by default for gig/platform workers** (`gig_arbitration` flag OFF; protective default); allowed only for independent consultants contracting through a business entity (§4.3) |

**0.5 Out of scope for P08e.** POSH IC workflow, IC constitution, external-member marketplace, annual report (P09 §4F); GRC/HR/whistle-blower desks (P09 FR-P09-28); employer clause API (P09 §4B); HRMS bulk intake infrastructure (P09 §4C). This file defines only the WRK-side hooks into them.

---

## 1. Vertical overview

### 1.1 Who

| Side | Personas (master §1.5 role codes) | Typical profile |
|---|---|---|
| Worker side | `party` (employee, ex-employee, fixed-term employee, contract worker, gig/platform worker, apprentice, job applicant), `representative` (family member, trade-union office-bearer acting under a Letter of Authority — NN-27), `counsel` | Individuals, mostly mobile-first; vernacular; low documentation for blue-collar and gig workers |
| Employer side | `party` (organisation), `party_org_user` (HR, legal, plant head) with `authority_limit_minor`, `enterprise_admin`, `enterprise_operator` | Establishments of every size; MSMEs and family businesses (acute power imbalance); listed companies (KMP exits, LODR disclosures); aggregators |
| Third parties | contractor, principal employer, insurer (employment-injury cover), gratuity trust / insurer (group gratuity), EPFO/ESIC (never parties — facilitation only) | Tri-partite matters |
| Statutory officers (not users) | GRC chair, conciliation officer, CoW s.45 authority, Inspector-cum-Facilitator, gratuity competent authority, Industrial Tribunal, IC/LC, Karnataka IDRC/Welfare Board | Signposting targets; export packs |
| Equator roles | `neutral_mediator`, `neutral_conciliator`, `neutral_arbitrator` (non-worker matters only), `case_manager`, `registrar`, `safeguarding_lead`, `grievance_officer`/`grc_member` (P09 desks), `ic_*` (P09 sealed) | Neutrals hold endorsement `END-WRK` (Appendix N; S6 §6) |

### 1.2 Value proposition

- **For employees and workers:** a free first information session, plain-language rights information with the statutory forum and last date shown up front (NN-20), itemised F&F computation on the Code on Wages "wages" basis, relieving/experience letters tied to settlement milestones, settlement money through escrow or direct with proof (NN-13), and a settlement that never waives statutory dues.
- **For employers:** fast, confidential, low-cost exits; a record of genuine pre-action steps; F&F compliance within the 2-working-day window (CoW s.17(2)); a defensible IR Code settlement pack for workers; arbitration for executive and founder disputes where a valid agreement exists; one console with the GRC desk, HR desk and POSH IC module (P09).
- **For aggregators:** an independent neutral tier above internal grievance handling, with Karnataka deactivation-notice checks, vernacular WhatsApp-first engagement and a funding-neutrality disclosure.

### 1.3 Mechanisms allowed (master §5.2; binding)

| Mechanism | WRK default | Limits |
|---|---|---|
| Negotiation (assisted / blind-bid) | ✔ | Blind-bid disabled for statutory components (dues are computed, not bid) |
| Conciliation (A&C Part III) | ✔ | Statutory components paid in full; for IR Code "workers" in termination/industrial disputes, output is converted to an IR Code settlement pack (§13.3) — Part III award status for worker industrial disputes **[VERIFY — open: whether a s.74 settlement binds an IR Code industrial dispute and bars a Tribunal reference (S4 Q-C3)]** |
| Mediation (contractual; statutory mode behind flag, NN-05) | ✔ | — |
| Arbitration (A&C) | **Non-worker commercial employment contracts only** | Never statutory components (HB-WRK-ARB-01); never IR Code "workers" for termination/industrial disputes; never gig/platform workers by default |
| Med-arb / arb-med / arb-med-arb | Non-worker only | Different neutral by default (master §5.3) |
| IR Code s.42 voluntary arbitration | Separate statutory track `wrk.irc42` (flag `wrk_ir_s42_voluntary_arbitration` OFF) | A&C Act does not apply (IR Code s.42; S4 W17) |
| Expert determination | — (master §5.2) | ESOP valuation is handled as a party-appointed valuer report inside mediation or as COM expert determination where all parties are business entities (§7.11) |
| Grievance (GRM) | ✔ (P09 `WRK_IRCODE`, `WRK_HR`, `WRK_WHISTLE`) | — |
| POSH inquiry | ✔ sealed (P09) | Never an ordinary case (NN-07) |
| Signposting | ✔ always | Closure policy `require_signposting = true` (App. A §5) |

### 1.4 Status of key laws (as at 21 October 2026)

| Instrument | Status | Notes for the build |
|---|---|---|
| Code on Wages 2019 | In force — ss.1–41, 42(4)–(9), 43–66, 67 (part), 68, 69 by **S.O. 5322(E), 21 Nov 2025**; earlier parts by S.O. 4604(E), 18 Dec 2020 [V] | Repeals Payment of Wages, Minimum Wages, Payment of Bonus and Equal Remuneration Acts (s.69) |
| Industrial Relations Code 2020 | In force — whole Code, **S.O. 5320(E), 21 Nov 2025** [V] | Replaces ID Act 1947, Trade Unions Act 1926, IE (Standing Orders) Act 1946 |
| Code on Social Security 2020 | In force — ss.1–14, 15(1)–(2), 16(1)(c), 17–141, 143–163, parts of s.164 by **S.O. 5319(E), 21 Nov 2025** [V]; **s.114(5) aggregator contribution awaits its own notification** [V secondary] | Gratuity Ch. V (ss.53–58); Employees' Compensation Ch. VII (ss.73–91); gig/platform Ch. IX; Central Rules G.S.R. 344(E), 8 May 2026 [V secondary] |
| OSH Code 2020 | In force — whole Code, **S.O. 5321(E), 21 Nov 2025** [V] | Contract labour (Ch. XI) **[VERIFY — open: section numbers for principal-employer wage liability]** |
| State rules under the Codes | Uneven; savings clauses keep earlier rules/notifications alive until replaced [V] | Every state-dependent form, threshold or authority is a `state_pack` row with `verified_on` |
| POSH Act 2013 + Rules 2013 | In force | Sealed (NN-07); P09 |
| Karnataka Platform-based Gig Workers (Social Security and Welfare) Act 2025 | Notified 12 Sep 2025 w.e.f. 30 May 2025; Rules 19 Nov 2025; Welfare Board constitution pending as of Nov 2025 [V] | Live rule pack `KA` |
| Rajasthan Platform Based Gig Workers (Registration and Welfare) Act 2023 | Passed 24 Jul 2023 [V secondary] | Rule pack `RJ` partial **[VERIFY — open: commencement, rules and designated grievance authority notification]** |
| Telangana Gig and Platform Workers Bill 2025 | Draft (15 Apr 2025) [V] | Informational only |
| RPwD Act 2016; Transgender Persons (Protection of Rights) Act 2019 + Rules 2020; HIV and AIDS (Prevention and Control) Act 2017 | In force [K] | Signposting to Commissioners / complaint officers |
| Companies Act 2013 s.177(9)–(10) + Companies (Meetings of Board and its Powers) Rules 2014 r.7; SEBI LODR Reg. 22 | In force [K] | Vigil mechanism; whistle-blower carve-outs |
| Mediation Act 2023 | Only ss.1, 3, 26, 31–38, 45–47, 50–54, 56–57 in force (S.O. 4384(E), 9 Oct 2023); MCI established S.O. 4781(E), 27 Aug 2026 | Contractual mode only (NN-05) |

---

## 2. Subtype taxonomy

### 2.1 Legend

- **L1** = `core.dispute_types.code` (P08 FR-P08-57 codes kept; four L1 codes added: `wrk.fixed_term`, `wrk.whistleblower`, `wrk.collective_s42`, `wrk.employment_injury`). **L2** = `sub_types[].code`. **Card** = S4 research card (W01–W18) plus W19 (team/interpersonal) and W20 (general grievance), added here.
- **Value band** (`wrk.value_band`): `VB0` non-monetary · `VB1` ≤ ₹50,000 · `VB2` ₹50,001–₹5,00,000 · `VB3` ₹5,00,001–₹50,00,000 · `VB4` > ₹50,00,000.
- **Ladders** (§2.2). **Neg / Med / Arb**: ✔ allowed · ✖ blocked · **A** = A&C arbitration only for contractual components of a **non-worker** with a valid arbitration agreement (`wrk_arbitrability()` §4.3) · **42** = IR Code s.42 voluntary arbitration only (flag OFF) · **F** = facilitation only (undertaking schedule; Equator cannot compromise a statutory authority's claim).
- **Signpost** = forum shown at first contact with its last date (NN-20); codes resolve to `routing_forums.forum_code` (§3.3).

### 2.2 Ladders (pinned `pathway` rows; App. A §4.5 is the parent)

| Ladder code | Rungs (time-box) | Used by |
|---|---|---|
| `wrk.individual.v1` | 0 GRC/HR desk where `grc_required` (30 d) → 1 negotiation (14 d) → 2 mediation (45 d; +60 by consent) → 3 conciliation (30 d) → compliance | Individual dues, termination of workers, leave, discrimination |
| `wrk.money_conciliation.v1` | 1 negotiation (14 d) → 2 **Part III conciliation** (30 d; s.73/s.74) → compliance | Non-worker money claims against an organisation (R6) |
| `wrk.executive.v1` | 1 negotiation (14 d) → 2 mediation (45 d) → 3 arbitration (A&C; expedited by agreement for claims ≤ ₹50,00,000) or med-arb | Managers, KMP, founders, restrictive covenants, ESOP (non-worker; agreement present) |
| `wrk.facilitation.v1` | 1 assisted negotiation with undertaking schedule (14 d) → evidence upload → close; parallel signpost to EPFO/ESIC/authority | PF, ESI, statutory-authority-dependent items |
| `wrk.gig.v1` | 0 aggregator internal grievance / Karnataka IDRC (14 d action, 45 d resolution) → 1 negotiation (7 d) → 2 mediation (30 d) → escalation pack to Welfare Board / designated authority | Gig and platform workers |
| `wrk.collective.v1` | 0 signpost to conciliation officer (always) → 1 facilitated bipartite negotiation (time-box set per matter, ≤ 60 d) → output: draft settlement for signature before the conciliation officer, or s.42 agreement pack (flag) | Retrenchment, lay-off, closure, charter of demands |
| `wrk.team.v1` | 1 intake and individual meetings (10 d) → 2 facilitated joint conversation(s) (30 d) → working agreement → 60-day review | Team and interpersonal conflict (non-POSH) |
| `wrk.posh_redirect` | none — diverts to P09 sealed IC flow before an ordinary case exists | POSH |

### 2.3 Taxonomy table

| L1 code | L2 code | Name | Typical parties | Value band | Default ladder | Neg | Med | Arb | Signpost forum | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `wrk.wage_dues` | `unpaid_wages` | Unpaid or delayed salary/wages | employee ↔ employer | VB1–VB2 | `wrk.individual.v1` (worker) / `wrk.money_conciliation.v1` (non-worker) | ✔ | ✔ | ✖ statutory | `CoW_S45_AUTH` | W01; CoW s.17(1) wage period; s.45 claim 3 y |
| | `illegal_deductions` | Deductions above the permitted limit or unauthorised | employee ↔ employer | VB1–VB2 | as above | ✔ | ✔ | ✖ | `CoW_S45_AUTH` | CoW s.18(3) 50% cap → W-WRK-DED-01 |
| | `minimum_wage_shortfall` | Below minimum/floor wage | worker ↔ employer | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `CoW_S45_AUTH`, `INSP_FACIL` | No settlement below the floor (HB-WRK-FLOOR-01) |
| | `overtime_unpaid` | Overtime wages not paid | worker ↔ employer | VB1 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `CoW_S45_AUTH` | — |
| | `contractual_salary_arrears_exec` | Salary arrears of a manager/executive | manager ↔ employer | VB2–VB4 | `wrk.money_conciliation.v1` | ✔ | ✔ | ✖ by default | `CoW_S45_AUTH`, `CIVIL_COURT` | CoW s.2(k) "employee" covers managers; s.57 bar — arbitration of salary arrears blocked pending Q-C4 **[VERIFY — open: scope of CoW s.57 for contractual salary of managers]** |
| `wrk.full_and_final` | `ff_delay` | F&F not paid within 2 working days of separation | ex-employee ↔ employer | VB1–VB3 | `wrk.individual.v1` / `wrk.money_conciliation.v1` | ✔ | ✔ | ✖ statutory; A for contractual heads | `CoW_S45_AUTH` | W01; clock `wrk_wages_2wd` |
| | `ff_computation_dispute` | Dispute on F&F components or deductions | ex-employee ↔ employer | VB1–VB3 | as above | ✔ | ✔ | as above | `CoW_S45_AUTH` | Calculator `wrk.ff@2` (Code-wages basis) |
| | `documents_withheld` | Relieving/experience letter, Form 16 or certificates withheld | ex-employee ↔ employer | VB0 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `POLICE` (originals withheld: possible offence), `INSP_FACIL` | Originals withheld → W-WRK-ORIG-01; Equator mediates return only |
| | `notice_pay_recovery` | Employer claims notice-pay shortfall from employee | employer ↔ ex-employee | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | A (non-worker) | `CIVIL_COURT` | Contractual; flag if it pushes deductions above 50% |
| `wrk.benefits` | `statutory_bonus` | Statutory bonus eligibility/quantum | worker(s) ↔ employer | VB1–VB2 | `wrk.individual.v1`; collective → `wrk.collective.v1` | ✔ | ✔ | ✖ (42 if collective) | `CoW_S45_AUTH`, `CONC_OFFICER` | W02; CoW s.26; s.46 deems bonus disputes industrial disputes |
| | `gratuity_nonpayment` | Gratuity unpaid, short-paid or delayed | ex-employee/heirs ↔ employer (± trust/insurer) | VB2–VB3 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `GRAT_AUTH` | W03; CoSS ss.53–58; interest on delay |
| | `gratuity_forfeiture` | Gratuity withheld/forfeited for misconduct | ex-employee ↔ employer | VB2–VB3 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `GRAT_AUTH` | Fact-heavy; outright refusal → signpost first |
| | `pf_issue` | PF non-deposit, exit date, KYC, transfer, withdrawal | employee ↔ employer (EPFO not a party) | VB1–VB2 | `wrk.facilitation.v1` | ✔ | ✔ | ✖ | `EPFIGMS`, `EPFO_RPFC` | W04 F; HB-WRK-PF-01 no waiver |
| | `esi_issue` | ESI contribution/benefit issue | insured person ↔ employer | VB1 | `wrk.facilitation.v1` | ✔ | ✔ | ✖ | `ESIC_GRIEV`, `ESI_COURT` | W04 F |
| | `maternity_benefit` | Maternity benefit denied/short-paid | woman employee ↔ employer | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `INSP_FACIL` | CoSS Ch. VI (ss.59–72) [Verified 22 Oct 2026, India Code] |
| `wrk.leave_attendance` | `leave_encashment` | Leave encashment on exit or year-end | employee ↔ employer | VB1 | `wrk.individual.v1` | ✔ | ✔ | ✖ statutory; A contractual | `CoW_S45_AUTH` | OSH Code annual leave (s.32(1)(vi)–(viii), secondary) **[VERIFY — open: confirm clauses on India Code]** |
| | `attendance_dispute` | Attendance, LOP marking, unauthorised absence | employee ↔ employer | VB0–VB1 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `GRC` | Often precedes "abandonment" termination |
| `wrk.termination` | `dismissal_after_inquiry` | Dismissal after disciplinary inquiry | worker ↔ employer | VB2–VB3 | `wrk.individual.v1` | ✔ | ✔ | ✖ (42 flag) | `GRC`, `CONC_OFFICER`, `IND_TRIBUNAL` | W05; IR Code s.2(q) individual dispute; reinstatement only by agreement or Tribunal |
| | `discharge_simpliciter` | Termination without inquiry | worker ↔ employer | VB2–VB3 | `wrk.individual.v1` | ✔ | ✔ | ✖ (42 flag) | as above | — |
| | `forced_resignation` | Resignation alleged to be coerced | employee ↔ employer | VB1–VB3 | `wrk.individual.v1` | ✔ | ✔ | A (non-worker) | `CONC_OFFICER` (worker), `CIVIL_COURT` (non-worker) | — |
| | `probation_termination` | Termination during/at end of probation | employee ↔ employer | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | A (non-worker) | as above | — |
| | `abandonment_alleged` | Employer treats absence as abandonment | worker ↔ employer | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ (42 flag) | `CONC_OFFICER` | — |
| | `manager_termination` | Termination of a non-worker manager | manager ↔ employer | VB2–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT` | W12; damages, not reinstatement, as a rule |
| | `se_state_termination` | Termination under a State Shops & Establishments Act | employee ↔ small employer | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `SE_AUTHORITY` (state pack) | W16; e.g., TN S&E Act 1947 s.41 appeal [K]; other States **[VERIFY — open: Q-C13 state compilation]** |
| `wrk.retrenchment_layoff` | `retrenchment_individual_dues` | Individual retrenchment compensation/notice dues | worker ↔ employer | VB2–VB3 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `CONC_OFFICER` | IR Code s.70; re-skilling fund s.83 |
| | `retrenchment_collective` | Collective retrenchment | union/workers ↔ employer | VB4 | `wrk.collective.v1` | ✔ (facilitated) | ✔ (facilitated) | 42 | `APPROPRIATE_GOVT`, `CONC_OFFICER` | W06; HB-WRK-COLL-01 |
| | `layoff` | Lay-off | as above | VB3–VB4 | `wrk.collective.v1` | ✔ | ✔ | 42 | as above | Ch. X at 300+ (s.78) |
| | `closure` | Closure of undertaking | as above | VB4 | `wrk.collective.v1` | ✔ | ✔ | 42 | as above | s.74 notice; Ch. X s.80 |
| | `vrs_scheme` | Voluntary retirement scheme terms | workers ↔ employer | VB3–VB4 | `wrk.collective.v1` | ✔ | ✔ | 42 | `CONC_OFFICER` | Term sheet only |
| `wrk.fixed_term` | `non_renewal` | Non-renewal on expiry of fixed term | FTE ↔ employer | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ worker / A non-worker | `CONC_OFFICER` | W07; non-renewal is outside "retrenchment" [K] |
| | `early_termination` | Termination before expiry | FTE ↔ employer | VB1–VB3 | `wrk.individual.v1` | ✔ | ✔ | ✖ worker / A non-worker | `CONC_OFFICER` | Possible retrenchment (IR Code s.2(zh)(iii)–(iv) exclusions do not cover it unless under a contract stipulation) → W-WRK-FTE-01 **[VERIFY — open (counsel): Q-C12]** |
| | `parity_benefits` | Pay or benefits parity with permanent staff | FTE ↔ employer | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `CoW_S45_AUTH` | IR Code s.2(o) |
| | `fte_gratuity_pro_rata` | Pro rata gratuity of FTE | FTE ↔ employer | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `GRAT_AUTH` | CoSS s.53 proviso; Central Rule 33 [R] |
| | `sham_fixed_term` | Successive contracts to defeat permanence | FTE ↔ employer | VB2 | signpost + `wrk.individual.v1` on exit terms | ✔ | ✔ | ✖ | `IND_TRIBUNAL` | Status question is the Tribunal's |
| `wrk.contractor_gig` | `gig_deactivation` | Account deactivation/blocking | gig worker ↔ aggregator | VB0–VB1 | `wrk.gig.v1` | ✔ | ✔ | ✖ (flag `gig_arbitration` OFF) | `KA_IDRC`, `KA_WELFARE_BOARD`, `RJ_AUTHORITY` | W08; KA 14-day reasoned notice |
| | `gig_payout` | Payout withheld, incentive unpaid, penalty | gig worker ↔ aggregator | VB1 | `wrk.gig.v1` | ✔ | ✔ | ✖ | as above | — |
| | `gig_rating_algorithm` | Rating, allocation or algorithmic discrimination | gig worker ↔ aggregator | VB0 | `wrk.gig.v1` | ✔ | ✔ | ✖ | `KA_IDRC` | KA automated-system transparency |
| | `gig_insurance_welfare` | Accident insurance / welfare scheme claim | gig worker ↔ aggregator/insurer | VB1–VB2 | `wrk.gig.v1` | ✔ | ✔ | ✖ | `KA_WELFARE_BOARD`, INS signposts | Link to V4 INS for insurer side |
| | `gig_classification` | Claim to be an employee | gig worker ↔ aggregator | VB2 | signpost only | ✖ | ✖ | ✖ | `CIVIL_COURT`, `IND_TRIBUNAL` | `signpost_only = true` |
| | `contract_labour_wages` | Unpaid/short wages of contract labour | worker ↔ contractor + principal employer | VB1–VB2 | `wrk.individual.v1` (tri-partite) | ✔ | ✔ | ✖ | `CoW_S45_AUTH`, `INSP_FACIL` | W09; principal employer liability (OSH Code Ch. XI) |
| | `contract_labour_removal` | Sudden removal by contractor | worker ↔ contractor + PE | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `CONC_OFFICER` | — |
| | `contract_labour_regularisation` | Regularisation / core-activity claim | worker ↔ PE | VB2 | signpost only | ✖ | ✖ | ✖ | `APPROPRIATE_GOVT`, `IND_TRIBUNAL` | Regulatory |
| | `independent_consultant` | Fees/termination of a consultant engaged through a business entity | consultant entity ↔ company | VB2–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT` | If both parties are business entities, COM-STD fees (App. B) |
| `wrk.notice_bond` | `training_bond` | Training bond recovery | employer ↔ employee | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | A (non-worker) | `CIVIL_COURT` | Contract Act s.74 reasonable compensation (LR-LAB-011) |
| | `notice_period_buyout` | Notice-period waiver/buy-out | employee ↔ employer | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | A (non-worker) | `CIVIL_COURT` | — |
| `wrk.restrictive_covenant` | `non_compete_post_exit` | Post-employment non-compete | employer ↔ ex-employee/new employer | VB2–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT` | W10; s.27 void restraint — information card only |
| | `garden_leave` | Garden leave / restraint during notice | employer ↔ employee | VB2–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT` | *Niranjan Shankar Golikari* line |
| | `non_solicit` | Non-solicitation of clients/employees | employer ↔ ex-employee | VB2–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT` | — |
| | `confidentiality_ip` | Confidentiality, IP assignment, data return | employer ↔ ex-employee | VB0–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT`, `POLICE` (data theft) | Criminal data theft → signpost (NN-24) |
| | `moonlighting` | Dual employment allegation | employer ↔ employee | VB0–VB2 | `wrk.individual.v1` | ✔ | ✔ | A (non-worker) | — | — |
| `wrk.cofounder_exec_exit` | `exec_contract_claims` | Notice pay, severance, contractual bonus/LTI | executive ↔ company | VB2–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT` | W12; statutory heads split out |
| | `clawback_malus` | Bonus clawback / malus | company ↔ executive | VB3–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT` | — |
| | `kmp_wtd_exit` | KMP / whole-time director exit | KMP ↔ company (± board) | VB3–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT`, `NCLT` (oppression) | CA 2013 ss.196–197; LODR Reg. 30 disclosure (listed) |
| | `esop_vesting` | ESOP/RSU/SAR/phantom: vesting, exercise, lapse, leaver class | employee ↔ company (± trust, foreign parent) | VB2–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT` | W11; CA 2013 s.62(1)(b); SCD Rules r.12 |
| | `founder_exit` | Co-founder exit, reverse vesting, buy-back | founder ↔ company + founders/investors | VB3–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `NCLT` (oppression non-arbitrable) | Link COM `shareholder_jv` where all parties are business entities |
| | `expatriate_assignment` | Expatriate/secondment terms | expatriate ↔ company | VB3–VB4 | `wrk.executive.v1` | ✔ | ✔ | A | `CIVIL_COURT` | Cross-border → INT gates if counterparty foreign (NN-19) |
| `wrk.harassment_non_posh` | `interpersonal_conflict` | Conflict between colleagues | employees (employer sponsor) | VB0 | `wrk.team.v1` | ✔ | ✔ | ✖ | `GRC`/HR desk | W19; restorative; no money |
| | `team_conflict` | Team or department breakdown | team members + manager | VB0 | `wrk.team.v1` | ✔ | ✔ | ✖ | HR desk | Multi-party facilitation |
| | `bullying_non_sexual` | Bullying or abusive conduct (not sexual) | employee ↔ colleague/manager | VB0–VB1 | `wrk.team.v1` / `wrk.individual.v1` | ✔ | ✔ | ✖ | `GRC`, `POLICE` (threats/violence) | POSH screen first; threats → exclusion |
| | `return_to_work` | Return after leave, illness or dispute | employee ↔ employer | VB0 | `wrk.team.v1` | ✔ | ✔ | ✖ | — | Health data sealed (`health_sealed`) |
| `wrk.posh` | `posh_complaint` | Sexual harassment at the workplace | aggrieved woman ↔ respondent; IC | — | `wrk.posh_redirect` | ✖ | ✖ (s.10 conciliation only in P09 at her request) | ✖ | `IC`, `LC`, `POLICE`, `SHEBOX` | W13; `POSH_MUST_BE_SEALED` (rule `WRK_POSH_ROUTED_SEALED`) |
| `wrk.discrimination` | `gender_pay` | Unequal pay or recruitment on gender | employee ↔ employer | VB1–VB3 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `CoW_S45_AUTH`, `INSP_FACIL` | W15; CoW s.3; s.57 bar → pay in full |
| | `disability_accommodation` | Reasonable accommodation / disability discrimination | employee ↔ employer | VB0–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `RPWD_COMMISSIONER`, `RPWD_GRO` | RPwD Act ss.20–23 [K] |
| | `transgender_discrimination` | Discrimination on transgender identity | employee ↔ employer | VB0–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `TG_COMPLAINT_OFFICER` | TG Act ss.3, 9–11 [K] |
| | `pregnancy_maternity` | Adverse action linked to pregnancy | woman employee ↔ employer | VB1–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `INSP_FACIL` | — |
| | `hiv_status` | Discrimination on HIV status | employee ↔ employer | VB0–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `HIV_COMPLAINTS_OFFICER`, `HIV_OMBUDSMAN` | HIV Act 2017 [K]; health data sealed |
| | `other_ground` | Religion, caste, age, other grounds | employee ↔ employer | VB0–VB2 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `CIVIL_COURT`; caste atrocity → `POLICE` | Caste atrocities are criminal (NN-24) |
| `wrk.grievance` | `general_grievance` | Working conditions, transfer, appraisal, treatment | worker ↔ employer | VB0–VB1 | `wrk.individual.v1` (GRC first if `grc_required`) | ✔ | ✔ | ✖ | `GRC` (P09 `WRK_IRCODE`) | W20; LR-LAB-004 |
| | `hr_policy_grievance` | HR-policy grievance (non-worker or < 20 workers) | employee ↔ employer | VB0–VB1 | `wrk.individual.v1` | ✔ | ✔ | ✖ | HR desk (P09 `WRK_HR`) | — |
| `wrk.whistleblower` | `retaliation_exit_terms` | Exit or return terms after alleged retaliation | employee ↔ employer | VB1–VB3 | `wrk.individual.v1` | ✔ | ✔ | A (contractual consequences, non-worker) | `AUDIT_COMMITTEE_CHAIR`, `SEBI_PIT_INFORMANT`, `CIVIL_COURT` | W14; never mediate the underlying report; HB-WRK-WB-01 no gag |
| `wrk.collective_s42` | `charter_of_demands` | Collective dispute (wages, conditions) | union ↔ employer | VB4 | `wrk.collective.v1` | ✔ (facilitated) | ✔ (facilitated) | 42 | `CONC_OFFICER`, `IND_TRIBUNAL` | W17; s.62 strike/lock-out notice triggers conciliation |
| | `s42_reference` | Voluntary arbitration under IR Code s.42 | employer + union/worker | VB2–VB4 | `wrk.irc42` track | — | — | 42 | `APPROPRIATE_GOVT` (registration copy) | Flag OFF; separate protocol |
| `wrk.employment_injury` | `ec_quantum` | Employees' compensation quantum/delay | employee/dependants ↔ employer (± insurer) | VB2–VB3 | `wrk.individual.v1` | ✔ | ✔ | ✖ | `EC_COMPETENT_AUTH`, `ESI_COURT` (ESI-covered) | W18; CoSS Ch. VII; settlement memorandum registered with the competent authority (CoSS s.89(1)–(3)) [Verified 22 Oct 2026] |

**Counts:** 18 L1, 73 L2. Tenants may hide L2s and add tenant-specific L2s under an existing L1, but may not unblock any ✖ or convert an `F`/`42` into ✔ (FR-P08-02).

---

## 3. Legal framework by subtype

### 3.1 Master switch: "worker" (IR Code) vs "employee" (Code on Wages)

| Concept | Source | Product consequence |
|---|---|---|
| **"Worker"** excludes persons employed mainly in a managerial or administrative capacity, and persons employed in a supervisory capacity drawing wages above ₹18,000 per month or a higher notified amount | IR Code 2020 s.2(zr) (supervisory limb s.2(zr)(iv)) [V]; substance over designation (settled law on "workman" under ID Act s.2(s), carried over) [K] | Drives `is_workman`; config `irc.supervisory_wage_threshold` = ₹18,000 (LR-LAB-005) |
| **Individual termination is an "industrial dispute"** | IR Code s.2(q) (discharge, dismissal, retrenchment or termination of an individual worker) [V] | Worker termination → GRC/conciliation/Tribunal route; A&C arbitration blocked |
| **"Employee"** includes managerial, supervisory and administrative staff | Code on Wages 2019 s.2(k) [V] | Managers' **statutory** wage claims also go to the CoW s.45 authority |
| **Bar of suits** where the Code provides a remedy (minimum wages, deductions, wage discrimination, bonus) | CoW s.57 [V] | Statutory components never arbitrated (HB-WRK-ARB-01); *Dushyant Janbandhu v Hyundai AutoEver India* (SC; on the analogous Payment of Wages Act s.22 bar; disputes within a statutory authority's exclusive jurisdiction are not arbitrable) **[VERIFY — open: date and citation of the SC decision]** |
| **"Wages"** = basic + DA + retaining allowance; if excluded payments exceed one-half of total remuneration, the excess is deemed wages | CoW s.2(y) proviso; mirrored in CoSS s.2(88), IR Code s.2(zq), OSH Code s.2(1)(zy) [V] | Every calculator computes on the Code basis and shows the contract basis alongside (LR-LAB-003) |
| **Arbitrability of employment contracts** | *Vidya Drolia v Durga Trading Corp* (2021) 2 SCC 1 (SC, 14 Dec 2020) [K] — rights in personam arising from contract are arbitrable unless a statute confers exclusive jurisdiction on a public forum | `wrk_arbitrability()` §4.3 |

### 3.2 Law by subtype

| L1 / L2 | Statute and section | Forum | Limitation / statutory clocks | Case law | Status |
|---|---|---|---|---|---|
| Wages, deductions, minimum wage, overtime | CoW s.17(1) (monthly wages before the 7th of the next month), s.17(2) (2 working days on removal, dismissal, retrenchment, resignation or closure), s.18(3) (deductions ≤ 50%), s.45 (claims authority; employee, union or Inspector-cum-Facilitator may file; compensation up to 10× the claim; decision endeavoured within 3 months), s.49 (appeal 90 days), s.51 (Inspector-cum-Facilitator), s.56 (compounding), s.57 (bar of suits) [V] | Claims authority (Gazetted Officer) → appellate authority | Claim within **3 years** of the claim arising, later on sufficient cause (s.45(6), LR-LAB-013); appeal 90 days (s.49) | — | In force (S.O. 5322(E)) |
| F&F | CoW s.17(2) [V]; leave encashment under OSH Code s.32(1)(vi) (secondary) / State law **[VERIFY — open: confirm clause on India Code]** | As above | `wrk_wages_2wd` from separation (LR-LAB-002) | — | In force |
| Statutory bonus | CoW s.26 (eligibility ≥ 30 days' work; minimum 8.33% or ₹100, maximum 20%); s.31 allocable surplus (60% banking companies / 67% others); s.46 bonus disputes deemed industrial disputes [V] | Claims authority for quantum; IR Code machinery for disputes | 3 years (s.45(6)) | — | In force; **[VERIFY — open (watch): no CoW s.26(1)–(2) ceiling notification found at 22 Oct 2026; Q-C7]** |
| Gratuity | CoSS ss.53–58: 5 years' continuous service (no minimum on death, disablement or expiry of fixed-term employment); 15 days' wages per completed year (÷26 for monthly-rated); ceiling "as notified" (s.53(3)); payment within 30 days with interest on delay (s.56); competent authority s.58 [V/R] | Competent authority → appellate authority | Claimant appeal window under Central Rule 33(4)(a) 180 days [R]; `wrk_gratuity_30d` | — | In force; ceiling ₹20,00,000 carried forward from PGA S.O. 1420(E), 29 Mar 2018 **[VERIFY — open (watch): no CoSS s.53(3) notification found at 22 Oct 2026; S.O. 1420(E) saved by CoSS s.164(2)(a)]**; fixed-term pro rata after 1 year per Government communication and Central Rule 33 [R] |
| PF | CoSS (EPF schemes saved); s.125 assessment; s.23 appeal to Industrial Tribunal with **25%** deposit; Tribunal endeavours to decide within 1 year [V] | EPFO (EPFiGMS grievance portal); Industrial Tribunal | — | — | In force |
| ESI | CoSS ESI chapter; Employees' Insurance Court (ss.48–52) [V titles] | ESIC; EI Court | 3 years from cause of action (CoSS s.51(1) first proviso); benefit/contribution claims per ESIC regulations (second proviso) [Verified 22 Oct 2026] | — | In force |
| Maternity benefit | CoSS maternity chapter [K] | Inspector-cum-Facilitator | CoSS ss.59–72 [Verified 22 Oct 2026] **[VERIFY — open: claim limitation]** | — | In force |
| Individual termination (worker) | IR Code s.2(q), s.4 (GRC), s.53 (conciliation), s.44 (Industrial Tribunal), Standing Orders (Ch. IV, 300+ workers) [V/K] | GRC (20+ workers) → conciliation officer → Industrial Tribunal | GRC application within **1 year** (s.4); GRC "may complete" in **30 days** (s.4(6), directory); application to conciliation officer **within 60 days** of GRC decision or expiry, through the worker's trade union (s.4(8)) [R]; conciliation report **45 days** from commencement (14 days where a s.62 notice was given) (s.53(5)); no conciliation after **2 years** from the dispute (s.53(1) proviso); Tribunal application **within 90 days** of the failure report (s.53(6)) | Reinstatement and back wages are Tribunal remedies | In force; [Verified 22 Oct 2026: s.53(1) proviso, (5), (6) and s.4(5), (6), (8), India Code; Central r.8, r.23] **[VERIFY — open: State IR Rules equivalents]** (LR-LAB-004, LR-LAB-012) |
| Manager termination | Contract; Specific Relief Act 1963 s.14 (contracts of personal service not specifically enforced, as a rule) [K] | Civil court or arbitration (if agreement) | Limitation Act 1963 Sch. Art. 55 — 3 years from breach (`limitation_contract`) | *Vidya Drolia* (2021) 2 SCC 1 | In force |
| Retrenchment, lay-off, closure | IR Code s.70 (one month's notice or wages in lieu; 15 days' average pay per completed year), s.74 (closure notice 60 days), Ch. X ss.77–80 (300+ workers: prior permission), s.83 (re-skilling fund: 15 days' wages last drawn; employer remits within 10 days, worker credited within 45 days — IR (Central) Rules 2026 r.37) [V/R] | Appropriate Government; conciliation officer; Tribunal | `wrk_retrenchment_notice_1m`, `wrk_reskilling_45d` | Last-come-first-go [K] | In force; s.83: employer remittance 10 d (r.37(1)), worker credit 45 d (r.37(2)) [Verified 22 Oct 2026, IR (Central) Rules 2026]; day-divisor 26/30 not statutory (LR-LAB-007) |
| Fixed-term | IR Code s.2(o) (written contract; hours, wages, allowances not less than permanent worker doing similar work; statutory benefits pro rata); CoSS s.53 proviso [V/R] | As for workers; civil court for non-workers | as above | Non-renewal and completion of tenure excluded from "retrenchment" (IR Code s.2(zh)(iii)–(iv)) [V] | In force; early termination = retrenchment? **[VERIFY — open: Q-C12]** |
| Gig/platform | CoSS s.2(35), s.2(60)–(61), s.113 (registration), s.114 (schemes; aggregator contribution 1–2% of turnover capped at 5% of payouts — s.114(5) not commenced), s.141 (fund); Central Rules G.S.R. 344(E) r.48(2) (worker data; onboarding/exit reporting) [V secondary]; **Karnataka Act 2025**: 14 days' written notice with reasons before deactivation (exceptions: bodily harm, specified offences, fraud); IDRC acts within 14 days and resolves within 45 days; escalation to Welfare Board; automated-system transparency in the worker's language [V]; **Rajasthan Act 2023**: grievance petition to a designated authority; welfare cess 1–2% per transaction [V secondary] | Aggregator grievance → KA IDRC → KA Welfare Board; RJ designated authority; civil court | `wrk_ka_deactivation_notice_14d`, `wrk_ka_idrc_action_14d`, `wrk_ka_idrc_resolve_45d` | — | KA in force (Board pending); RJ **[VERIFY — open: commencement]**; TG draft; other State enactments reported in 2025 **[VERIFY — open: not confirmed in research — watch-list only]** |
| Contract labour | OSH Code Ch. XI (licensing; principal employer liability for wages where the contractor fails) [K]; CoW s.45 | Inspector-cum-Facilitator; claims authority | 3 years (CoW s.45(6)) | — | In force; **[VERIFY — open: OSH Code section numbers]** |
| Restrictive covenants, garden leave, bonds | Contract Act 1872 s.27 (restraint of trade void), s.74 (reasonable compensation) [K] | Civil court (injunction) or arbitration | Art. 55 (3 years) | *Superintendence Co. of India v Krishan Murgai* (1981) 2 SCC 246; *Percept D'Mark v Zaheer Khan* (2006) 4 SCC 227; *Niranjan Shankar Golikari v Century Spinning* (1967) 2 SCR 378 (negative covenant during employment enforceable); *Varun Tyagi v Daffodil Software Pvt Ltd*, 2025:DHC:5015 (Del HC, Jun 2025: post-employment restraint void) [V] | In force (LR-LAB-011) |
| ESOP / founder | Companies Act 2013 s.62(1)(b); Companies (Share Capital and Debentures) Rules 2014 r.12 (minimum vesting 1 year, r.12(6)(a)); SEBI (Share Based Employee Benefits and Sweat Equity) Regulations 2021 (listed); FEMA (foreign-parent RSUs); ss.241–242 oppression → NCLT [K] | Civil court; NCLT (oppression, generally non-arbitrable); arbitration (plan/SHA clause) | Art. 55 | *Vidya Drolia* | In force |
| KMP / WTD exits | CA 2013 ss.196–197 (appointment/remuneration of managerial personnel); LODR Reg. 30 (KMP resignation disclosure) [K] | Board; civil court; arbitration | Art. 55 | — | In force |
| Whistle-blower | CA 2013 s.177(9)–(10); Companies (Meetings of Board and its Powers) Rules 2014 r.7 (vigil mechanism for listed companies, companies accepting public deposits, and companies borrowing > ₹50 crore from banks/public FIs); LODR Reg. 22; SEBI (PIT) Regulations informant mechanism; Whistle Blowers Protection Act 2014 (public servants) [K] | Audit Committee chair; SEBI; courts | — | — | In force; WBP Act operationalisation **[VERIFY — open]** |
| Discrimination | CoW s.3 (no gender discrimination in wages, recruitment, conditions) [V]; RPwD Act 2016 s.20 (Government establishments), s.21 (equal opportunity policy — every establishment), s.23 (GRO — Government establishments); Chief/State Commissioners [K]; Transgender Persons Act 2019 s.3, s.9 (no discrimination in employment), s.10 (equal opportunity policy), s.11 (complaint officer) [K]; HIV and AIDS (Prevention and Control) Act 2017 (non-discrimination; complaints officer; Ombudsman) **[VERIFY — open: section numbers and establishment-size threshold for complaints officer]** | Claims authority (pay); Commissioners; complaint officer; courts | 3 years (pay) | — | In force |
| POSH | POSH Act 2013 ss.4, 6, 9–13, 16–18, 21–22, 26; Rules 2013 rr.3, 4, 7(2), 7(3), 7(6), 8, 11, 12, 14 [R] | IC / LC | 3 + 3 months (s.9(1)); 90-day inquiry (s.11(4), start point open); report 10 days; action 60 days; appeal 90 days | — | Sealed (P09; LR-POSH-001…011) |
| Collective / s.42 | IR Code s.42: (1) written agreement; (2) umpire where even number; (3) prescribed form and signatures; (4) copy to the appropriate Government and conciliation officer; (5) notification where parties represent the majority; (6) award to Government; (7) prohibition of connected strike/lock-out; (8) A&C Act not applicable [V enacted text, India Code, 22 Oct 2026]; s.62 strike/lock-out notice (60 days; not within 14 days) [V: s.62(1)(a)–(b), India Code] | Arbitrator(s) chosen by parties; Government | `wrk_s62_notice` informational | — | [Verified 22 Oct 2026: enacted s.42; Central Form V, IR (Central) Rules 2026 r.20] **[VERIFY — open: State forms per `state_pack`]** (LR-LAB-006) |
| Employment injury | CoSS Ch. VII ss.73–91 (competent authority s.91; appeal s.99) replacing the EC Act 1923 (repealed 21 Nov 2025) [R] | Competent authority; ESI for ESI-covered employees | 2 years from accident/death, condonable (CoSS s.82(1)–(2)) [Verified 22 Oct 2026] | — | In force (LR-INS cross-reference) |
| S&E State matters | State Shops & Establishments Acts (e.g., TN S&E Act 1947 s.41 appeal against termination [K]) | State authority | State-specific | — | **[VERIFY — open: Q-C13 for DL, UP, RJ, MH, KA, TN, TG]** |

### 3.3 Forum directory seed (WRK rows in `routing_forums`; launch states DL, UP, RJ, MH, KA)

| `forum_code` | Name | Level | What it can do | Cost text | Time-limit rule | Channel |
|---|---|---|---|---|---|---|
| `GRC` | Grievance Redressal Committee of the establishment | establishment | Decide individual grievances of workers (20+ workers) | Free | `LR-LAB-004` | Employer; P09 `WRK_IRCODE` desk where hosted |
| `CONC_OFFICER` | Conciliation Officer (State/Central labour department) | district/state | Conciliate industrial disputes; failure report | Free | `LR-LAB-012` | Labour department office; online portal where the State provides one |
| `IND_TRIBUNAL` | Industrial Tribunal | state | Adjudicate industrial disputes incl. reinstatement, back wages | Court fees per State | 90 days from failure report | Tribunal registry |
| `CoW_S45_AUTH` | Claims authority under Code on Wages s.45 | district | Decide wage, bonus, deduction, equal-pay claims; compensation up to 10× | Free | `LR-LAB-013` | Labour department |
| `INSP_FACIL` | Inspector-cum-Facilitator | district | Advise, inspect, file claims | Free | — | Labour department |
| `GRAT_AUTH` | Gratuity competent authority (CoSS s.58) | district | Determine and direct gratuity | Free | `LR-LAB-009` | Labour department |
| `EPFIGMS` | EPFO grievance portal | national | Grievances on PF accounts | Free | — | epfigms.gov.in [K] |
| `EPFO_RPFC` | EPFO Regional PF Commissioner (assessment s.125) | regional | Assess and recover dues | Free | — | EPFO |
| `ESIC_GRIEV` / `ESI_COURT` | ESIC grievance / Employees' Insurance Court | regional/district | Benefit and contribution disputes | Free / court fee | 3 y (CoSS s.51(1) provisos; ESIC regulations) | ESIC |
| `EC_COMPETENT_AUTH` | Competent authority (CoSS s.91) | district | Employees' compensation | Free | 2 y (CoSS s.82(1)), condonable (s.82(2)) | Labour department |
| `APPROPRIATE_GOVT` | Appropriate Government (labour department) | state/central | Ch. X permissions; s.42 registration copies | — | — | Labour department |
| `IC` / `LC` | Internal Committee / Local Committee | establishment / district | POSH inquiry; s.10 conciliation at her request | Free | `LR-POSH-003` | P09 sealed module / District Officer |
| `SHEBOX` | SHe-Box (MWCD) | national | Online POSH complaint routing | Free | — | shebox.wcd.gov.in (relaunched 29 Aug 2024) [R] |
| `KA_IDRC` / `KA_WELFARE_BOARD` | Karnataka IDRC / Platform-based Gig Workers Welfare Board | aggregator / state | Deactivation and payout grievances | Free | `LR-GIG-001/002` (§18.2) | Aggregator; Board when constituted |
| `RJ_AUTHORITY` | Rajasthan designated authority (gig) | state | Grievance petitions | Free | **[VERIFY — open]** | — |
| `RPWD_COMMISSIONER` / `RPWD_GRO` | Chief/State Commissioner for Persons with Disabilities / establishment GRO | national/state | Disability-rights complaints | Free | — | — |
| `TG_COMPLAINT_OFFICER` | Complaint officer under TG Act s.11 | establishment | Transgender discrimination complaints | Free | — | Employer |
| `HIV_COMPLAINTS_OFFICER` / `HIV_OMBUDSMAN` | Complaints officer / State Ombudsman under HIV Act 2017 | establishment/state | HIV-status discrimination | Free | **[VERIFY — open]** | — |
| `AUDIT_COMMITTEE_CHAIR` | Audit Committee chair (vigil mechanism) | company | Direct-access whistle-blower channel | Free | — | Company |
| `SEBI_PIT_INFORMANT` | SEBI Office of Informant Protection | national | Insider-trading informant protection | Free | — | SEBI |
| `SE_AUTHORITY` | State S&E appellate authority | state | Termination appeals under State S&E Act | per State | per `state_pack` | — |
| `CIVIL_COURT` | Civil court / commercial court | district | Damages, injunctions (non-workers) | Court fees | `limitation_contract` | — |
| `NCLT` | National Company Law Tribunal | bench | Oppression and mismanagement (ss.241–242) | Fees | — | — |
| `POLICE` | Police / emergency 112 | local | Criminal offences, threats, violence | Free | Immediate | 112 |
| `DLSA_LOK_ADALAT` | DLSA (pre-litigation Lok Adalat) | district | Record a settlement as a Lok Adalat award (LSA Act ss.19(5)(ii), 20(2), 21) | Free | — | DLSA |

### 3.4 WRK clock register (owned per NN-04; all periods read from rules, never hard-coded)

| WC ID | Clock kind (App. A §6.3 or new §16.4) | Category | Trigger | Period | Owner | Source |
|---|---|---|---|---|---|---|
| WC-01 | `wrk_wages_2wd` | informational | separation date | 2 WD | case manager | CoW s.17(2) |
| WC-02 | `wrk_monthly_wages_7d` (new) | informational | end of wage period | before the 7th of next month | case manager | CoW s.17(1) |
| WC-03 | `wrk_cow_claim_3y` (new) | statutory | claim arises | 3 y (condonable) | case manager | CoW s.45(6) |
| WC-04 | `wrk_cow_appeal_90d` (new) | informational | claims-authority order | 90 d | party (info) | CoW s.49 |
| WC-05 | `wrk_grc_application_1y` | informational | cause of action | 1 y | case manager | IR Code s.4 |
| WC-06 | `wrk_grc_30d` | statutory (directory) | GRC receipt | 30 d | GRC chair (P09) | IR Code s.4(6) |
| WC-07 | `wrk_grc_to_conc_60d` (new) | statutory | GRC decision or 30-d expiry | 60 d | case manager | IR Code s.4(8) |
| WC-08 | `wrk_conc_report_45d` (new) | informational | conciliation commenced (party-entered) | 45 d (14 d if s.62 notice) | party (info) | IR Code s.53(5) |
| WC-09 | `wrk_conc_outer_2y` (new) | statutory | dispute arose | 2 y | case manager | IR Code s.53(1) proviso |
| WC-10 | `wrk_tribunal_90d` (new) | statutory | receipt of failure report | 90 d | case manager | IR Code s.53(6) |
| WC-11 | `wrk_retrenchment_notice_1m` (new) | informational | retrenchment notice | 1 m | case manager | IR Code s.70 |
| WC-12 | `wrk_reskilling_45d` (new) | informational | retrenchment | 45 d | case manager | IR Code s.83; IR (Central) Rules 2026 r.37(2) (fund → worker 45 d; employer remits within 10 d, r.37(1)) |
| WC-13 | `wrk_gratuity_30d` | informational | gratuity payable | 30 d | case manager | CoSS s.56(3) [Verified 22 Oct 2026] |
| WC-14 | `wrk_epf_appeal_deposit` (new) | informational | appeal filing | 25% deposit condition | party (info) | CoSS s.23 |
| WC-15–17 | `posh_complaint_3m`, `posh_inquiry_90d`, `posh_appeal_90d` | statutory | per P09 | per P09 | Presiding Officer | POSH Act ss.9, 11(4), 18 (sealed; never in WRK core) |
| WC-18 | `wrk_ka_deactivation_notice_14d` (new) | statutory (State) | notice served | 14 d before deactivation | case manager | KA Act 2025 |
| WC-19 | `wrk_ka_idrc_action_14d` / `wrk_ka_idrc_resolve_45d` (new) | statutory (State) | grievance to IDRC | 14 d / 45 d | aggregator nodal (info to Equator) | KA Act 2025 |
| WC-20 | `wrk_s62_notice` (new) | informational | strike/lock-out notice | 60 d before; not within 14 d | case manager | IR Code s.62 |
| WC-21 | `limitation_contract` | statutory | breach | 3 y | case manager | Limitation Act Art. 55 |
| WC-22 | `med_contract_timebox` (WRK 45 d) | contractual | first appearance | 45 d (+60 by consent) | neutral | Equator WRK Rules r.13; App. A |

**Clock rules.** (1) No Equator process suspends any of WC-03, WC-07, WC-09, WC-10 or WC-21 (App. A clock invariant 3; S4 finding 10). (2) Red banner on every party and case-manager screen when WC-10 or WC-03 has < 21 days left (S4 WRK-04). (3) Blocking task at T-60/T-30 per App. A AP-L/AP-M; unprompted expiry is a Critical incident (NN-04). (4) Copy "we will pause your deadline" is blocked by lint (PL-15).

---

## 4. Suitability and eligibility rules

All functions below are deterministic (`packages/rules/verticals/wrk`), versioned with the ruleset, and return `{outcome, reason_codes[], legal_rule_ids[], trace[]}`. The AI intake assistant may pre-fill inputs; it never produces outcomes (NN-01, NN-02).

### 4.1 `wrk_is_worker()` (F-WRK-21)

| # | Input condition (evaluated in order) | `status` | `is_workman` |
|---|---|---|---|
| 1 | `engagement` ∈ {gig, platform} | `not_applicable_gig` | NULL (gig rules apply; arbitration blocked by R7) |
| 2 | `engagement` = founder, or `designation_category` ∈ {director_kmp} and holds board office | `non_worker` | false |
| 3 | `principal_duties` = managerial or administrative (answered "Yes, mainly" to Q-WRK-T05) | `non_worker` | false |
| 4 | `principal_duties` = supervisory AND `monthly_wages_minor` > `irc.supervisory_wage_threshold` (₹18,000) | `non_worker` | false |
| 5 | `principal_duties` = supervisory AND wages ≤ threshold | `worker` | true |
| 6 | `principal_duties` ∈ {manual, skilled, technical, operational, clerical, sales_promotion} | `worker` | true |
| 7 | Conflicting answers (e.g., designation "Manager" but no power to hire/fire/appraise/sanction leave, and duties operational) | `uncertain` | NULL → treated as worker |
| 8 | Any answer "Not sure" | `uncertain` | NULL → treated as worker; counsel recommended |

Trace shows every answer and the rule applied; both parties see the result and may contest it (`worker_assessment.contested = true` → case manager review, never AI). A contested status keeps the fail-safe (`is_workman` NULL).

### 4.2 Derived flags

| Flag | Rule |
|---|---|
| `grc_required` | `is_workman IS DISTINCT FROM false` AND `establishment_size` ∈ {20_49, 50_99, 100_299, 300_plus} AND L1 ∈ {grievance, termination, wage_dues, leave_attendance, discrimination} |
| `chapter_x` | `establishment_size = 300_plus` AND L1 = `wrk.retrenchment_layoff` |
| `standing_orders_apply` | `establishment_size = 300_plus` |
| `posh_redirect` | POSH checklist positive (§5.2 Q-WRK-T02) or classifier ≥ threshold with human confirmation |
| `statutory_components[]` / `arbitrable_components[]` | per claim head (§4.3) |
| `limitation_alerts[]` | §4.7 |
| `power_imbalance` | employer `establishment_size` ∈ {lt_10, 10_19} with family-business flag, or worker side unrepresented with `vulnerability` flag → shuttle option and independent-advice prompts |

### 4.3 `wrk_arbitrability()` (claim-head level; S4 A1.2, refined)

```
FOR EACH claim_head h:
  IF h.component ∈ STATUTORY = {statutory_wages, minimum_wage, overtime_statutory, deductions, equal_pay,
       statutory_bonus, gratuity, pf, esi, maternity_benefit, employees_compensation,
       retrenchment_comp_statutory, reskilling_fund, posh}
     → h.arb = BLOCK  (rule WRK_STATUTORY_NOT_ARBITRABLE → CASE_NOT_ARBITRABLE; LR-LAB-014)
  ELSE IF case.engagement ∈ {gig, platform} AND flag gig_arbitration = OFF
     → h.arb = BLOCK  (rule WRK_GIG_ARBITRATION_BLOCKED → MECHANISM_NOT_PERMITTED_FOR_VERTICAL)
  ELSE IF is_workman IS DISTINCT FROM false
       AND h.type ∈ {termination, discharge, dismissal, retrenchment, industrial_dispute_other}
     → h.arb = BLOCK_AC (WRK_WORKMAN_ARBITRATION_BLOCKED, 422); offer = [mediation, conciliation, irc42 (if flag ON)]
  ELSE IF is_workman = false
       AND h.type ∈ {contractual_severance, notice_pay_contract, discretionary_bonus, retention_bonus, lti,
                     clawback, esop, restrictive_covenant, garden_leave, training_bond, founder_exit,
                     consulting_fees, expatriate_terms, indemnity, reference_defamation_civil}
       AND (arbitration_agreement_exists OR post_dispute_submission_signed)
     → h.arb = ALLOW + W-WRK-ARB-02 ("unequal bargaining — independent advice") + NN-03 allocation (no party nomination: employer–employee)
  ELSE IF h.type = contractual_salary_arrears_exec
     → h.arb = BLOCK pending LR-LAB-015 (Q-C4) — permissive; cannot activate while VERIFY
  ELSE → h.arb = BLOCK (mediation/conciliation only)
case.arb_allowed = ANY(h.arb = ALLOW); arbitration claim form shows only ALLOW heads; BLOCK heads are pre-filled into a statutory-forum pack (F-WRK-23)
```

Employer–employee matters never use party nomination of arbitrators (NN-03 exception does not apply); sole arbitrator from the Equator panel by rotation with `END-WRK`.

### 4.4 Suitability decision table (`wrk_route()`)

| # | Inputs | Outcome | Conditions / outputs |
|---|---|---|---|
| S-01 | POSH indicator confirmed | **reject-and-redirect** | No core case; P09 sealed intake; `POSH_MUST_BE_SEALED`; signpost IC/LC/SHe-Box/police |
| S-02 | Threats, violence, assault, stalking, sexual offence, caste atrocity, criminal data theft, forgery of documents alleged as the dispute itself | **signpost** (police) + continue only for civil dues if the claimant chooses | NN-24; safety lead task; no joint session (`safety_flag`) |
| S-03 | Matter pending before the Industrial Tribunal, a court or claims authority | **accept-with-conditions** | Parallel mediation only; settlement placed before that forum (withdrawal/joint application pack); clocks of that forum shown |
| S-04 | Worker termination; `grc_required`; no GRC application yet; cause of action < 1 year | **accept-with-conditions** | Signpost GRC (mandatory disclosure); Equator mediation allowed in parallel by consent; `SIGNPOSTING_REQUIRED` closure gate |
| S-05 | Worker termination; failure report received | **accept-with-conditions** | WC-10 opened from the report date; red banner < 21 days; settlement → IR Code settlement pack |
| S-06 | Retrenchment/lay-off/closure, collective | **accept-with-conditions** (facilitation) | `wrk.collective.v1`; HB-WRK-COLL-01; union representation required; counsel gate task |
| S-07 | `chapter_x` and Government permission not applied for | **signpost** + facilitation only | Equator cannot be used to bypass Ch. X (LR-LAB-008) |
| S-08 | PF/ESI non-deposit | **accept-with-conditions** | `wrk.facilitation.v1`; undertaking schedule; EPFiGMS/ESIC signpost; HB-WRK-PF-01 |
| S-09 | Gig deactivation in Karnataka; notice < 14 days or no reasons | **accept-with-conditions** | Show KA rule; record W-WRK-GIG-01; IDRC first unless worker elects Equator in parallel |
| S-10 | Gig classification claim (wants employee status) | **signpost** | `signpost_only` |
| S-11 | Contract-labour regularisation / core-activity prohibition | **signpost** | Appropriate Government / Tribunal |
| S-12 | Non-worker contractual claim with arbitration agreement | **accept** | `wrk.executive.v1`; arbitration offered for ALLOW heads |
| S-13 | Non-worker money claim against an organisation; no arbitration agreement | **accept** | `wrk.money_conciliation.v1` recommended (R6) |
| S-14 | Whistle-blower: user seeks resolution of the underlying wrongdoing | **signpost** | Audit Committee chair / regulator; Equator may mediate only employment consequences |
| S-15 | Discrimination with statutory complaint route | **accept-with-conditions** | Commissioner/complaint officer shown; settlement cannot bar the statutory complaint |
| S-16 | Team/interpersonal conflict; no misconduct investigation pending; no POSH; no safety flag | **accept** | `wrk.team.v1`; employer sponsor; participants' individual consent |
| S-17 | Team conflict with a disciplinary investigation pending against a participant | **accept-with-conditions** | Only with the employer's written pause decision and the participant's consent (W-WRK-DISC-01) |
| S-18 | Limitation expired for every forum and claim is statutory | **accept-with-conditions** | Show `LIMITATION_EXPIRED_STAGE_BLOCKED` explainer; voluntary negotiation allowed; no promise of recovery |
| S-19 | Respondent is a Government department/PSU whose service rules exclude ADR | **signpost** | Departmental grievance / CAT / courts |
| S-20 | Party lacks capacity or needs a guardian | **on_hold** | Representative under NN-27 required |
| S-21 | Structural conflict: Equator supplies the employer's IC external member | **accept-with-conditions** or **reject** | Same individual never neutral; same employee involved → decline unless both give informed written consent (`CONFLICT_DETECTED`, rule `WRK_STRUCTURAL_CONFLICT`) |
| S-22 | Everything else in §2.3 with ✔ | **accept** | Ladder per §2.3 |

### 4.5 Hard exclusions (HB) and warnings (W)

| Code | Type | Rule | Error (`code` / `rule`) |
|---|---|---|---|
| HB-WRK-POSH-01 | HB | POSH never in core | `POSH_MUST_BE_SEALED` / `WRK_POSH_ROUTED_SEALED` |
| HB-WRK-CRIM-01 | HB | No mediation of an offence; civil dues only (NN-24; App. K §3) | `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` / `WRK_CRIMINAL_EXCLUDED` |
| HB-WRK-ARB-01 | HB | Statutory components never arbitrated | `CASE_NOT_ARBITRABLE` / `WRK_STATUTORY_NOT_ARBITRABLE` |
| HB-WRK-ARB-03 | HB | Worker termination/industrial dispute not A&C-arbitrable | `WRK_WORKMAN_ARBITRATION_BLOCKED` (422) |
| HB-WRK-FLOOR-01 | HB | No settlement below minimum wages or waiving statutory bonus, gratuity, PF, ESI, maternity, EC | `STATUTORY_WAIVER_FORBIDDEN` / `WRK_STATUTORY_DUES_WAIVER` |
| HB-WRK-PF-01 | HB | No term by which an employee "waives" PF/ESI | as above |
| HB-WRK-WB-01 | HB | No clause restricting reports to a regulator, police, court, IC, Audit Committee or statutory authority | `SETTLEMENT_LINT_FAILED` / `WRK_GAG_CLAUSE` |
| HB-WRK-COLL-01 | HB | No Equator document may describe a collective outcome as satisfying IR Code procedure or as a "registered settlement" | `SETTLEMENT_LINT_FAILED` / `WRK_COLLECTIVE_STATUS_CLAIM` |
| HB-WRK-RESTRAINT-01 | HB | Settlement builder cannot insert a post-employment non-compete as an enforceable obligation; it may record a voluntary paid undertaking with the s.27 information card acknowledged | `SETTLEMENT_LINT_FAILED` / `WRK_RESTRAINT_TERM` |
| HB-WRK-GIG-ARB | HB | No arbitration for gig/platform workers while flag OFF | `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` / `WRK_GIG_ARBITRATION_BLOCKED` |
| W-WRK-DED-01 | W | Deductions > 50% of wages (CoW s.18(3)) | — |
| W-WRK-ORIG-01 | W | Original certificates withheld | signpost police/labour authority |
| W-WRK-ARB-02 | W | Unequal bargaining; independent advice prompt before arbitration agreement | — |
| W-WRK-FTE-01 | W | FTE early termination may be retrenchment | — |
| W-WRK-GIG-01 | W | KA deactivation notice < 14 days or without reasons | — |
| W-WRK-DISC-01 | W | Disciplinary inquiry pending | — |
| W-WRK-AUTH-01 | W | Employer signatory without authority to settle (Rules r.6) | settlement signing blocked until resolved (`OFFER_ABOVE_AUTHORITY`) |

### 4.6 Mechanism recommendation (deterministic)

| Situation | Recommended first mechanism | Why |
|---|---|---|
| Individual worker vs employer, money only | Negotiation → mediation | Speed; outcome convertible to IR Code settlement |
| Non-worker vs organisation, money, no arbitration clause | Part III conciliation | s.73 settlement has award status (s.74); s.62 invitation/acceptance mirrors consent capture |
| Non-worker with clause, contractual heads | Mediation → arbitration (med-arb, different neutral) | Enforceable award for unsettled heads |
| Team/interpersonal | Team mediation | Relationship repair; no money |
| PF/ESI | Facilitation | Statutory authority holds the claim |
| Collective | Facilitated bipartite negotiation | Statutory machinery owns the dispute |

### 4.7 Jurisdiction and limitation checks (`wrk_limitation()`)

1. **Territorial.** Equator's process is consensual and online; venue default = worker's district (online) — mirrors LR-ARB-030 for consumer-type power imbalance. Arbitration seat for executive matters: as per agreement; if the agreement names a distant seat for a non-worker on a standard-form contract, W-WRK-ARB-02 plus registrar review.
2. **State pack.** `state_of_work` selects S&E Act rows, gig law pack, IR Rules forms and the conciliation-officer directory.
3. **Limitation.** Compute and display for every claim head: WC-03 (CoW 3 y), WC-07/09/10 (IR Code), WC-21 (Art. 55), gratuity appeal window, POSH (P09). Outcome per head: `in_time` · `expiring` (< 90 d) · `critical` (< 21 d) · `expired_condonable` (CoW s.45(6) proviso) · `expired`.
4. **Disclosure.** Every invitation and consent screen carries: "This process does not stop limitation periods running unless both parties sign a standstill agreement" (PL-11 standstill template gated on Q-C1).

---

## 5. Dispute Explorer question tree (App. K v2 engine; one question per page for individuals)

Plain English, class-8 reading level; Hindi parity at launch. Safety and POSH questions come **before** any money question. Every outcome screen lists the free/statutory forums with their last date (NN-20) and writes `core.signposting_events`.

### 5.1 Outcome codes

| Code | Meaning | Next action |
|---|---|---|
| `OUT-WRK-POSH` | POSH redirect | Open P09 sealed intake; IC/LC/SHe-Box/police details |
| `OUT-WRK-SAFETY` | Safety/criminal | Police 112 and helplines; civil dues may continue later |
| `OUT-WRK-SIGNPOST` | Statutory forum only | Forum pack (F-WRK-23); case closed as `signposted` |
| `OUT-WRK-GRC-FIRST` | GRC recommended first, Equator in parallel by consent | GRC application template; P09 desk if employer subscribes |
| `OUT-WRK-NEG` | Assisted negotiation | F-WRK-30 |
| `OUT-WRK-MED` | Mediation | F-WRK-02 (mediation) |
| `OUT-WRK-CONC` | Part III conciliation | F-WRK-02 (conciliation) with s.62 invitation |
| `OUT-WRK-ARB` | Arbitration available for listed heads (non-worker) | F-WRK-14 (SoC) for ALLOW heads + F-WRK-23 for blocked heads |
| `OUT-WRK-FACIL` | PF/ESI facilitation | F-WRK-02 (facilitation) + EPFiGMS/ESIC link |
| `OUT-WRK-GIG` | Gig ladder | F-WRK-24 |
| `OUT-WRK-COLL` | Collective facilitation (case-manager call) | Enquiry form; counsel gate |
| `OUT-WRK-TEAM` | Team mediation | F-WRK-27 (employer sponsor) |
| `OUT-WRK-HOLD` | Needs representative/guardian | NN-27 Letter of Authority flow |

### 5.2 Common trunk

| QID | Question (EN) | Answers | Branching / effect |
|---|---|---|---|
| Q-WRK-T01 | Are you, or is anyone, in danger right now? | Yes · No | Yes → `OUT-WRK-SAFETY` (stop) |
| Q-WRK-T02 | Is your problem about unwelcome sexual behaviour at work — touching, sexual remarks, requests for sexual favours, showing sexual pictures, or similar? | Yes · No · Not sure | Yes → `OUT-WRK-POSH`; Not sure → short explainer then re-ask; never asks for details here |
| Q-WRK-T03 | Who are you in this problem? | Employee or worker · Former employee · Employer or HR · Contract worker · Gig or delivery/driver partner · Platform company · Trade union · Helping someone else | Helping someone → Q-WRK-T03a (relationship; NN-27) |
| Q-WRK-T04 | What is the main problem? | Salary or dues not paid · Full and final settlement · Bonus, gratuity, PF or ESI · Leave or attendance · I was dismissed or asked to leave · Layoff or closure affecting many · Fixed-term contract · Gig account or payouts · Contract labour · Notice period or training bond · Non-compete or confidentiality · Senior job, bonus, ESOP or founder exit · Conflict with colleagues or manager · Unfair treatment (discrimination) · I reported wrongdoing and now face trouble · Injury at work · Other complaint at work | Selects L1 branch |
| Q-WRK-T05 | In your job, did you mainly manage people or run administration — for example hiring, firing, approving leave or appraisals? | Yes, mainly · Partly · No · Not sure | Feeds `wrk_is_worker()` |
| Q-WRK-T06 | What was your monthly salary (before deductions)? | Band: ≤ ₹18,000 · ₹18,001–₹50,000 · ₹50,001–₹1,00,000 · ₹1,00,001–₹3,00,000 · > ₹3,00,000 | Feeds worker test; value band |
| Q-WRK-T07 | About how many people work at the workplace? | < 10 · 10–19 · 20–49 · 50–99 · 100–299 · 300 or more · Don't know | `grc_required`, `chapter_x`; Don't know → treated as 20–49 for GRC disclosure (protective) |
| Q-WRK-T08 | In which State do (did) you work? | State/UT list | `state_pack` |
| Q-WRK-T09 | Has the matter gone to any office or court already? | No · Company grievance committee · Labour office / conciliation officer · Claims authority · EPFO/ESIC · Industrial Tribunal · Civil court · Police · Internal Committee · Other | Pending forum → S-03 |
| Q-WRK-T10 | When did the problem start, or when did you leave? | Date | Limitation engine |

### 5.3 L1 branches (selected questions; full schema in `packages/verticals/wrk/explorer.json`)

| L1 | QIDs and questions | Answers | Outcome rule |
|---|---|---|---|
| Wages / F&F | Q-WRK-W01 What is unpaid? (multi) · Q-WRK-W02 Last working day? · Q-WRK-W03 Has the employer given an F&F statement? · Q-WRK-W04 Are any documents being held back? (multi) · Q-WRK-W05 Is any original certificate with the employer? | Components list (DD-WRK-COMPONENTS) · date · Yes/No/Partly · DD-WRK-DOCS-WITHHELD · Yes/No | Originals → W-WRK-ORIG-01; worker → `OUT-WRK-NEG`/`MED`; non-worker vs organisation → `OUT-WRK-CONC`; always disclose CoW s.45 (3 years; up to 10×) |
| Benefits | Q-WRK-B01 Which benefit? · Q-WRK-B02 Years of service? · Q-WRK-B03 Was PF deducted from salary? · Q-WRK-B04 Has the employer refused in writing? | Bonus/Gratuity/PF/ESI/Maternity · number · Yes/No/Don't know · Yes/No | PF/ESI → `OUT-WRK-FACIL`; gratuity refused outright → `OUT-WRK-SIGNPOST` + optional mediation |
| Termination | Q-WRK-X01 How did the job end? · Q-WRK-X02 Was there an inquiry/charge-sheet? · Q-WRK-X03 What do you want? (multi) · Q-WRK-X04 Have you received a "failure report" from the conciliation officer? (date) | DD-WRK-TERMINATION-TYPE · Yes/No · DD-WRK-RELIEF · Yes (date)/No | Worker + `grc_required` → `OUT-WRK-GRC-FIRST`; failure report → WC-10 banner; non-worker with clause → `OUT-WRK-ARB` option |
| Collective | Q-WRK-C01 How many workers affected? · Q-WRK-C02 Total workforce? · Q-WRK-C03 Is there a union? · Q-WRK-C04 Has Government permission been sought? | number · number · DD-WRK-UNION-STATUS · DD-WRK-GOVT-STAGE | Always `OUT-WRK-COLL` (+ `OUT-WRK-SIGNPOST` if `chapter_x` and not applied) |
| Fixed-term | Q-WRK-F01 Contract start and end dates (rows) · Q-WRK-F02 What happened? | dates · DD-WRK-FTE-ISSUE | Early termination → W-WRK-FTE-01 |
| Gig | Q-WRK-G01 Which kind of platform? · Q-WRK-G02 What happened? · Q-WRK-G03 Did you get a notice with reasons before blocking? How many days before? · Q-WRK-G04 Have you complained inside the app? | DD-WRK-PLATFORM-CAT · DD-WRK-GIG-ISSUE · Yes (days)/No · Yes/No | Classification → `OUT-WRK-SIGNPOST`; else `OUT-WRK-GIG`; KA < 14 days → W-WRK-GIG-01 |
| Contract labour | Q-WRK-L01 Who pays your wages? · Q-WRK-L02 Where do you actually work (company name)? | contractor/company/both/don't know · text | Tri-partite `OUT-WRK-MED`; regularisation → signpost |
| Covenants / bonds | Q-WRK-R01 What kind of clause? · Q-WRK-R02 Has anyone sent a legal notice or filed a case? | DD-WRK-RESTRAINT-TYPE · DD-WRK-RESTRAINT-STAGE | Injunction sought/urgent → court/EA disclosure; s.27 information card shown (no advice) |
| Executive / ESOP / founder | Q-WRK-E01 Your role? · Q-WRK-E02 Is there an arbitration clause in your contract, ESOP plan or shareholders' agreement? · Q-WRK-E03 What is disputed? | DD-WRK-SENIORITY · Yes (upload)/No/Not sure · DD-WRK-EXEC-CLAIMS / DD-WRK-ESOP-ISSUE | Clause → `OUT-WRK-ARB` for ALLOW heads; oppression → NCLT signpost |
| Team / interpersonal | Q-WRK-P01 Who is involved? · Q-WRK-P02 Has anyone been threatened or hurt? · Q-WRK-P03 Is any inquiry or disciplinary action running? · Q-WRK-P04 Has HR agreed to support mediation? | DD-WRK-TEAM-PARTIES · Yes/No · Yes/No · Yes/No/Not asked | Threat → `OUT-WRK-SAFETY`; inquiry → S-17; else `OUT-WRK-TEAM` |
| Discrimination | Q-WRK-D01 On what ground? (multi) · Q-WRK-D02 What would put it right? (multi) | DD-WRK-DISC-GROUND · DD-WRK-DISC-REMEDY | Caste atrocity → `OUT-WRK-SAFETY`; else `OUT-WRK-MED` + Commissioner/complaint officer disclosure |
| Whistle-blower | Q-WRK-H01 Where did you report? · Q-WRK-H02 What happened to you after? (multi) · Q-WRK-H03 Do you want help with the report itself, or with your job situation? | DD-WRK-WB-CHANNEL · DD-WRK-WB-RETALIATION · Report / Job / Both | Report → `OUT-WRK-SIGNPOST` (Audit Committee, regulator); Job → `OUT-WRK-MED` |
| Injury | Q-WRK-I01 Are you covered by ESI? · Q-WRK-I02 Date of injury? · Q-WRK-I03 Has the employer or insurer offered anything? | Yes/No/Don't know · date · Yes/No | ESI → ESIC signpost; else `OUT-WRK-MED` with competent-authority disclosure |

### 5.4 Free-forum disclosure texts (versioned `wrk.disclosure.*`, EN + HI; legal review required)

| Key | Text (EN) |
|---|---|
| `wrk.disclosure.cow45` | "You can also file a claim, free of charge, with the Authority under section 45 of the Code on Wages, 2019 within 3 years. The Authority can order compensation of up to ten times the amount due. Using Equator does not stop this time running." |
| `wrk.disclosure.grc` | "Your workplace has 20 or more workers, so it must have a Grievance Redressal Committee (Industrial Relations Code, 2020, section 4). You can apply within 1 year. If you are not satisfied, you can go to the conciliation officer within 60 days." |
| `wrk.disclosure.tribunal` | "You received a failure report on [date]. You can apply to the Industrial Tribunal until [date] (90 days). Equator mediation does not extend this date." |
| `wrk.disclosure.gratuity` | "Gratuity must be paid within 30 days of becoming payable. You can apply free of charge to the competent authority under the Code on Social Security, 2020." |
| `wrk.disclosure.pf` | "PF grievances can be raised free on the EPFO grievance portal (EPFiGMS). Equator cannot settle what your employer owes to EPFO." |
| `wrk.disclosure.posh` | "Complaints of sexual harassment go to your employer's Internal Committee, or the Local Committee if your workplace has fewer than 10 workers or the complaint is against the employer. You have 3 months from the last incident (extendable by 3 months). You can also go to the police." |
| `wrk.disclosure.gig_ka` | "In Karnataka, a platform must give you 14 days' written notice with reasons before deactivating your account (except in specified cases), and its dispute committee must act within 14 days and resolve within 45 days." |
| `wrk.disclosure.statutory_floor` | "Any settlement must pay your legal dues — wages, bonus, gratuity, PF and ESI — in full. You cannot be asked to give them up." |
| `wrk.disclosure.limitation` | "This process does not stop limitation periods running unless both parties sign a standstill agreement." |

---

## 6. Intake and submission forms per mechanism

Conventions: forms are P02 form-engine schemas `F-WRK-NN@semver`, EN + HI, pinned at filing (NN-21). Core blocks (party identity, contact, representative/Letter of Authority, KYC/consent, fee payer) come from P01/P02 and are not repeated. `sensitive` fields are encrypted and masked; sealed fields never reach core (health → `health_sealed`; POSH never collected here). Money fields are `amount_minor` + `currency` (INR). "Req" = required; `rW` = requiredWhen; `vW` = visibleWhen.

### 6.1 Shared WRK Employment Block `EB-WRK@2` (embedded in every WRK filing and response)

| field_id | Label | Type | Req | Options / dropdown | Validation | Help text |
|---|---|---|---|---|---|---|
| eb_filer_role | You are filing as | select | Y | DD-WRK-FILER-ROLE | — | — |
| eb_employer_org | Employer / company / platform | org lookup (MCA/GSTIN via `KYC_PORT`) or text | Y | — | CIN/LLPIN/GSTIN optional | "Search by name; we will verify." |
| eb_principal_employer | Principal employer (if contract labour) | org lookup | rW `l1 = contractor_gig AND l2 ∈ contract_labour_*` | — | — | "The company where you actually worked." |
| eb_engagement | Type of engagement | select | Y | DD-WRK-ENGAGEMENT | — | — |
| eb_designation | Designation / job title | text | Y | — | ≤ 80 chars | — |
| eb_designation_category | Job category | select | Y | DD-WRK-DESIGNATION-CAT | — | "Choose what you actually do, not only your title." |
| eb_principal_duties | Main duties | select | Y | DD-WRK-DUTIES | — | Feeds worker test |
| eb_powers[] | Powers you had | multiselect | N | hire · fire · approve leave · write appraisals · sanction expenses · none | — | — |
| eb_employee_id | Employee / partner ID | text | N | — | masked on display | — |
| eb_uan | UAN (PF) | text | N | — | 12 digits | "Only if PF is involved." |
| eb_esi_ip | ESI insurance number | text | N | — | 10 digits | — |
| eb_joined_on | Date of joining | date | Y (non-gig) | — | ≤ today | — |
| eb_separated_on | Last working day / separation date | date | rW `eb_employment_status ∈ {separated, deactivated}` | — | ≥ joined_on; ≤ today | Starts `wrk_wages_2wd` |
| eb_employment_status | Current status | select | Y | DD-WRK-EMPLOYMENT-STATUS | — | — |
| eb_separation_mode | How did it end? | select | rW separated | DD-WRK-SEPARATION-MODE | — | — |
| eb_monthly_gross | Monthly gross salary | money | Y (non-gig) | — | > 0 | — |
| eb_basic_da_ra | Basic + DA + retaining allowance (monthly) | money | rW L1 ∈ {wage_dues, full_and_final, benefits, retrenchment_layoff} | — | ≤ eb_monthly_gross | "Code on Wages 'wages'. If unsure, upload a salary slip." |
| eb_monthly_wages_band | Salary band | select | Y | DD-WRK-WAGES-BAND | consistent with eb_monthly_gross | — |
| eb_establishment_size | Number of workers at the workplace | select | Y | DD-WRK-ESTAB-SIZE | — | — |
| eb_state_of_work | State/UT of work | select | Y | DD-STATE (core) | — | — |
| eb_work_city | City/district | text | Y | — | — | Venue default |
| eb_statutory_stage | Where is the matter now? | select | Y | DD-WRK-STATUTORY-STAGE | — | — |
| eb_stage_ref | Reference number and date of that forum | text + date | rW stage ≠ none | — | — | — |
| eb_failure_report_on | Date failure report received | date | rW stage = failure_report_received | — | ≤ today | Starts WC-10 |
| eb_arbitration_clause | Is there an arbitration clause? | select | Y | DD-WRK-ARB-CLAUSE | — | — |
| eb_clause_doc | Upload contract/clause | file | rW clause = yes | PDF/JPG/PNG/DOCX ≤ 20 MB | — | — |
| eb_union | Union representation | select | N | DD-WRK-UNION-STATUS | — | — |
| eb_language | Preferred language | select | Y | DD-LANG-22 (core) | — | — |
| eb_accessibility | Accessibility needs | multiselect | N | screen reader · sign language interpreter · large text · plain language · call-back · none | — | Never shown to the other side |

### 6.2 Negotiation request `F-WRK-30` (assisted negotiation; blind-bid not available for statutory heads)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| ng_l1 / ng_l2 | Dispute type / subtype | select | Y | §2.3 | not `wrk.posh` | — |
| ng_heads[] | What do you want to resolve? (repeatable) | group | Y | head: DD-WRK-CLAIM-HEADS; amount (money); basis (DD-WRK-AMOUNT-BASIS) | ≥ 1 row | Statutory heads auto-tagged "must be paid in full" |
| ng_ff_statement | Attach F&F statement or calculator output | file / link to `wrk.calc_runs` | rW L1 = full_and_final | — | — | — |
| ng_relief_nonmoney[] | Other things you want | multiselect | N | DD-WRK-RELIEF | — | — |
| ng_opening_position | Your opening proposal | textarea | N | — | ≤ 1,000 chars; lint: no threats | Shown to the other side |
| ng_offer_validity | Keep my offer open for | select | Y | 7 · 14 · 21 · 30 days | ≥ 14 for corporate respondents (PL-08) | — |
| ng_contact_window | Best time to contact you | select | N | 08:00–11:00 · 11:00–14:00 · 14:00–17:00 · 17:00–19:00 | inside 08:00–19:00 | — |
| ng_authority (employer) | Settlement authority up to | money | rW filer = employer | — | ≤ `authority_limit_minor` | Above-limit routes to approver |
| ng_consent | I agree to the Equator Negotiation Rules and the statutory-dues notice | checkbox | Y | — | true | `wrk.disclosure.statutory_floor` |

### 6.3 Mediation / conciliation / facilitation request `F-WRK-02@3` (legacy F-W02)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| mr_mechanism | Process requested | select | Y | mediation · conciliation (A&C Part III) · facilitation (PF/ESI) · team mediation | conciliation hidden if worker industrial dispute only (§1.3) | Recommendation from §4.6 shown |
| mr_l1 / mr_l2 | Dispute type / subtype | select | Y | §2.3 | not POSH | — |
| mr_summary | What happened, in brief | textarea | Y | — | 50–3,000 chars; PII lint | AI may summarise; user approves (NN-25) |
| mr_chronology[] | Key dates | group | N | date · event · document link | dates ≤ today | — |
| mr_heads[] | Claims (repeatable) | group | Y (not team) | head DD-WRK-CLAIM-HEADS; amount; period from–to; computed_by (self/calculator/employer statement) | statutory heads flagged | — |
| mr_relief[] | Relief sought | multiselect | Y | DD-WRK-RELIEF | ≥ 1 | — |
| mr_other_party[] | Other party/parties | group | Y | name, org, role (DD-WRK-RESPONDENT-ROLE), email, mobile, address | ≥ 1 | Equator sends the invitation, not you |
| mr_hr_contact | HR/legal contact at employer (if known) | text | N | — | — | Corporate routing (S4 E2) |
| mr_preferences | Neutral preferences | multiselect | N | prefer a woman neutral · prefer co-mediation (employer-side and employee-side experienced neutrals) · Hindi-speaking · regional language · labour-law background · HR background | — | Preferences, not choice of person (NN-03, NN-28) |
| mr_mode | Session mode | select | Y | online · in person · either | — | — |
| mr_safety | Do you need to avoid being in the same room/call as the other side? | select | Y | yes · no | — | Yes → shuttle; no reasons required |
| mr_pending_forum | Pending forum details | group | rW eb_statutory_stage ≠ none | forum, reference, next date | — | — |
| mr_s62_invitation (conciliation) | Written invitation to conciliate under A&C s.62 | generated doc | rW conciliation | TPL-WRK-N02 | e-sign | 30-day reply window (s.62(4)) |
| mr_standstill | Propose a standstill (time-bar) agreement | checkbox | N | — | visible only if flag `wrk_standstill_template` ON (Q-C1) | — |
| mr_fee_payer | Who pays | select | Y | per Card WRK-STD default (75:25) · employer pays all · concession request (CN-EMPLOYEE) | — | Total incl. GST shown (NN-29) |
| mr_declarations | Declarations | checkboxes | Y | information true; no POSH complaint folded in; statutory dues cannot be waived; this does not stop limitation; I may withdraw at any time | all true | — |

### 6.4 Arbitration request / Statement of Claim `F-WRK-14@2` (non-worker; ALLOW heads only)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| ar_basis | Arbitration agreement | select | Y | clause in employment contract · ESOP plan · SHA/founders' agreement · consultancy agreement · post-dispute submission agreement | `wrk_arbitrability()` ALLOW ≥ 1 | — |
| ar_clause_doc | Clause document | file | Y | PDF | hash stored | — |
| ar_worker_assessment | Worker status assessment | link F-WRK-21 | Y | — | `is_workman = false` else `WRK_WORKMAN_ARBITRATION_BLOCKED` | — |
| ar_heads[] | Claim heads | group | Y | head ∈ ALLOW list (DD-WRK-ARB-HEADS); amount; interest basis (DD-INTEREST-BASIS core); period | blocked heads rejected (`CASE_NOT_ARBITRABLE`) and moved to F-WRK-23 | — |
| ar_statutory_split_ack | I understand statutory dues go to the statutory forum | checkbox | Y | — | true | HB-WRK-ARB-01 |
| ar_s21_notice | Notice invoking arbitration (A&C s.21) | generated doc TPL-WRK-N03 | Y | — | e-sign | Commencement on receipt |
| ar_seat / ar_venue | Seat / venue | text | Y | default per agreement; online | distant-seat W-WRK-ARB-02 | — |
| ar_procedure | Procedure | select | Y | standard · expedited (by agreement, ≤ ₹50,00,000) · documents-only (by agreement) | — | — |
| ar_interim | Interim measures needed? | select | N | none · s.17 application · emergency arbitrator (Equator Rules Sch. 1) | — | Injunction on restrictive covenants |
| ar_soc | Statement of claim (AI Pleadings Studio draft, user-authored) | document | Y | App. M | NN-25 anchors | — |
| ar_independent_advice | Independent advice declaration | checkbox + optional counsel ID | Y for employee claimant | — | true | W-WRK-ARB-02 |
| ar_waiver_s12_5 | Post-dispute s.12(5) waiver (only if a Seventh Schedule item applies) | e-sign per party | conditional | — | post-dispute date (`S12_5_WAIVER_PREDATES_DISPUTE`) | NN-03 |

### 6.5 Response / Statement of Defence / Counterclaim `F-WRK-05@2` (legacy F-W05)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| rs_position | Your position | select | Y | DD-WRK-RESPONSE-POSITION | — | — |
| rs_worker_status_view | Do you agree with the worker-status result? | select | Y | agree · disagree (explain) | disagree → contested review | — |
| rs_heads_response[] | Response per claim head | group | Y | head ref; admitted · partly admitted (amount) · denied; reason | — | — |
| rs_ff_statement | Employer F&F statement | file / F-WRK-18 | rW employer AND L1 ∈ {full_and_final, wage_dues} | — | — | — |
| rs_setoff[] | Set-off / deductions claimed | group | N | DD-WRK-EMPLOYER-DEDUCTIONS; amount; basis doc | total deductions ≤ 50% of wages unless W-WRK-DED-01 acknowledged | — |
| rs_counterclaim[] | Counterclaim heads | group | N | DD-WRK-COUNTERCLAIM; amount | arbitration: ALLOW heads only | Training bond: s.74 information card |
| rs_authority | Authorised signatory and limit | signatory picker | Y (organisation) | — | board resolution/authority letter upload (W-WRK-AUTH-01) | — |
| rs_forum_objection | Objection: another forum should hear this | select + text | N | statutory forum named | — | Triggers case-manager review, never automatic closure |
| rs_documents[] | Documents | files | N | §9 | — | — |
| rs_s62_acceptance | Written acceptance of conciliation (s.62(2)) | e-sign | rW conciliation | — | within `conc_s62_reply` | — |
| rs_declarations | Declarations | checkboxes | Y | no retaliation against the employee for using this process; statutory dues not conditional on any term | true | — |

### 6.6 Vertical-specific forms

**F-WRK-21 Worker Status Assessment** — inputs EB-WRK fields `eb_designation_category`, `eb_principal_duties`, `eb_powers[]`, `eb_monthly_gross`, plus `wa_supervisory_share` (select: none · < 25% · 25–50% · > 50% of time), `wa_reports_count` (integer), `wa_contested` (bool), `wa_contest_reason` (text). Output `status`, `is_workman`, `trace[]`, `rule_version`. Read-only to AI.

**F-WRK-18 F&F Statement (itemised)** — rows: `ff_item` (DD-WRK-COMPONENTS / DD-WRK-EMPLOYER-DEDUCTIONS), `basis` (contract · Code wages · policy · statute), `amount_minor`, `source_doc`; computed `gross`, `deductions`, `net`, `statutory_wage_minor`, `wage_definition_warning`; signatures HR · employee · Equator (case manager attestation of computation only, not of correctness).

**F-WRK-22 Executive / Founder Exit Request** — `ex_seniority` (DD-WRK-SENIORITY), `ex_instrument[]` (DD-WRK-ESOP-INSTRUMENT), `ex_issue[]` (DD-WRK-ESOP-ISSUE), `ex_grant_docs[]`, `ex_vesting_schedule` (table: date, units, vested Y/N), `ex_leaver_class_claimed` (good · bad · intermediate · not classified), `ex_cap_table` (file, confidential tier `high`), `ex_valuation_reports[]`, `ex_listed` (bool → LODR Reg. 30 note), `ex_foreign_parent` (bool → FEMA note; INT gates if a foreign entity is a party), `ex_board_resolution` (file), `ex_non_solicit_terms` (text).

**F-WRK-24 Gig Account / Payout Review** — `gg_platform_cat` (DD-WRK-PLATFORM-CAT), `gg_state` (DD-WRK-GIG-STATE), `gg_issue` (DD-WRK-GIG-ISSUE), `gg_partner_id`, `gg_deactivated_on` (date), `gg_notice_received` (yes/no), `gg_notice_days` (int), `gg_reasons_given` (yes/no/unclear), `gg_internal_ticket` (ref), `gg_idrc_filed` (KA: yes/no/date), `gg_earnings_period` (from–to), `gg_amount_claimed`, `gg_evidence[]` (screenshots → type copy per NN-32), `gg_no_retaliation_ack` (aggregator side, required). Outputs feed W-WRK-GIG-01 and the KA compliance evidence log.

**F-WRK-25 IR Code Settlement Pack** — `irs_form_state` (state pack), `irs_parties` (employer signatory, worker/union), `irs_terms` (from settlement builder), `irs_route` (sign before conciliation officer under s.53 · bipartite memorandum with copies to Government and conciliation officer), `irs_copies[]` (addressee, mode, dispatch proof), `irs_status` (draft · signed · submitted · acknowledged). Label lint: "Draft memorandum of settlement for submission under the Industrial Relations Code, 2020" (never "registered settlement" before acknowledgement). [Verified 22 Oct 2026: Central Form I, IR (Central) Rules 2026 r.4] **[VERIFY — open: State forms; Q-C3]**

**F-WRK-26 IR Code s.42 Voluntary Arbitration Agreement Pack** (flag OFF) — `s42_dispute_desc`, `s42_parties`, `s42_arbitrators[]` (names from the labour-law panel; umpire if even), `s42_form_state`, `s42_copies` (appropriate Government, conciliation officer), `s42_majority_rep` (bool → s.42(5) notification), `s42_award_submission` (tracker). Uses the "Equator IR Code s.42 Procedural Protocol", not the Equator Arbitration Rules.

**F-WRK-27 Team / Workplace Mediation Request** — `tm_sponsor` (employer org user), `tm_participants[]` (name, role, consent status), `tm_issue` (DD-WRK-TEAM-ISSUE), `tm_investigation_pending` (yes/no; yes → S-17), `tm_safety_screen` (per participant, private), `tm_desired_outcome[]` (DD-WRK-TEAM-OUTCOME), `tm_confidentiality_ack` (each participant: what the sponsor will and will not receive — attendance and the agreed working agreement only if all consent), `tm_review_date`.

**F-WRK-28 Reasonable Accommodation / Discrimination Resolution Request** — `ra_ground[]` (DD-WRK-DISC-GROUND), `ra_request` (text), `ra_prior_request_date`, `ra_employer_response`, `ra_certificate` (UDID or medical — routed to `health_sealed`, token only in core), `ra_remedy[]` (DD-WRK-DISC-REMEDY), `ra_statutory_complaint` (filed with Commissioner/complaint officer: yes/no/date).

**F-WRK-23 Statutory Forum Referral Pack** (generator) — selects templates TPL-WRK-P01…P07 (replacing C3 T-1…T-6; C3 T-7, the IC record, stays sealed in P09 and is never generated here): GRC application; conciliation-officer application; Industrial Tribunal statement of claim (AI Pleadings Studio, user-authored); CoW s.45 claim; gratuity application; EPFiGMS/ESIC grievance text; labour-authority complaint. Pre-fills from the case; adds the limitation computation; never filed by Equator (NN-01 GX-7).

### 6.7 Dropdown Master List (values are configuration; codes stable)

| List ID | Values (`code` — label) |
|---|---|
| DD-WRK-FILER-ROLE | `employee` Employee · `ex_employee` Former employee · `job_applicant` Job applicant · `employer_hr` Employer/HR · `contractor` Contractor · `principal_employer` Principal employer · `gig_worker` Gig/platform worker · `aggregator` Platform company · `union_rep` Trade union representative · `authorised_rep` Authorised representative · `counsel` Advocate |
| DD-WRK-ENGAGEMENT | `permanent` · `probationer` · `fixed_term` · `contract_via_contractor` · `gig` · `platform` · `apprentice` · `trainee_intern` · `consultant_individual` · `consultant_entity` · `founder` · `expatriate_secondee` |
| DD-WRK-DESIGNATION-CAT | `unskilled` · `semi_skilled` · `skilled` · `clerical` · `technical` · `sales_promotion` · `working_journalist` · `supervisory` · `managerial` · `administrative` · `director_kmp` · `apprentice_trainee` · `intern` |
| DD-WRK-DUTIES | `manual_operational` · `skilled_technical` · `clerical` · `sales_promotion` · `supervisory` · `managerial` · `administrative` · `not_sure` |
| DD-WRK-WAGES-BAND | `le_18000` ≤ ₹18,000 · `18001_50000` · `50001_100000` · `100001_300000` · `gt_300000` |
| DD-WRK-ESTAB-SIZE | `lt_10` < 10 · `10_19` · `20_49` · `50_99` · `100_299` · `300_plus` · `unknown` |
| DD-WRK-EMPLOYMENT-STATUS | `current` · `serving_notice` · `garden_leave` · `suspended` · `separated` · `deactivated` · `on_leave` |
| DD-WRK-SEPARATION-MODE | `resignation` · `termination_by_employer` · `dismissal_after_inquiry` · `discharge` · `retrenchment` · `end_of_fixed_term` · `early_end_fixed_term` · `closure` · `superannuation` · `death` · `disablement` · `abandonment_alleged` · `forced_resignation_alleged` · `probation_termination` · `deactivation` · `vrs` |
| DD-WRK-STATUTORY-STAGE | `none` · `grc_filed` · `grc_decided` · `conciliation_pending` · `failure_report_received` · `tribunal_pending` · `tribunal_award` · `claims_authority_cow45` · `epfo_esic` · `gratuity_authority` · `civil_court` · `ic_lc` · `rpwd_commissioner` · `police` · `ka_idrc` · `welfare_board` · `ec_authority` |
| DD-WRK-ARB-CLAUSE | `yes_upload` · `no` · `not_sure` |
| DD-WRK-UNION-STATUS | `sole_negotiating_union` · `negotiating_council` · `union_not_recognised` · `none` |
| DD-WRK-GOVT-STAGE | `not_applied` · `applied` · `permission_granted` · `refused` · `deemed` · `not_required` |
| DD-WRK-COMPONENTS | `unpaid_salary` · `arrears` · `overtime` · `leave_encashment` · `notice_pay_employee_claim` · `statutory_bonus` · `contractual_bonus_incentive` · `variable_pay` · `reimbursements` · `gratuity` · `retrenchment_compensation` · `reskilling_fund` · `pf_transfer_withdrawal_support` · `retention_joining_bonus_clawback` · `esop_cash_out` · `other` |
| DD-WRK-EMPLOYER-DEDUCTIONS | `notice_shortfall` · `salary_advance` · `loan` · `asset_non_return` · `training_bond` · `excess_leave` · `statutory_pf_esi` · `tds` · `fines` · `damage_loss` · `other` |
| DD-WRK-DOCS-WITHHELD | `relieving_letter` · `experience_letter` · `form_16` · `original_certificates` · `pf_exit_marking` · `salary_slips` · `none` |
| DD-WRK-TERMINATION-TYPE | `dismissal_after_inquiry` · `discharge_simpliciter` · `retrenchment` · `non_renewal_fixed_term` · `forced_resignation` · `abandonment_alleged` · `probation_termination` |
| DD-WRK-RELIEF | `payment_of_dues` · `ff_statement` · `relieving_experience_letter` · `reinstatement` · `compensation` · `neutral_reference` · `notice_pay_waiver` · `return_of_documents` · `pf_esi_action` · `gratuity` · `record_correction` · `conversion_to_resignation` · `accommodation` · `account_reactivation` · `apology` · `policy_change` · `no_retaliation_assurance` |
| DD-WRK-RESPONDENT-ROLE | `employer` · `principal_employer` · `contractor` · `aggregator` · `colleague` · `manager` · `company_board` · `esop_trust` · `foreign_parent` · `insurer` · `gratuity_trust` |
| DD-WRK-CLAIM-HEADS | DD-WRK-COMPONENTS ∪ `contractual_severance` · `notice_pay_contract` · `discretionary_bonus` · `retention_bonus` · `lti` · `clawback` · `esop` · `restrictive_covenant` · `garden_leave` · `training_bond` · `founder_exit` · `consulting_fees` · `expatriate_terms` · `indemnity` · `reference_correction` · `employees_compensation` · `maternity_benefit` |
| DD-WRK-ARB-HEADS | `contractual_severance` · `notice_pay_contract` · `discretionary_bonus` · `retention_bonus` · `lti` · `clawback` · `esop` · `restrictive_covenant` · `garden_leave` · `training_bond` · `founder_exit` · `consulting_fees` · `expatriate_terms` · `indemnity` |
| DD-WRK-AMOUNT-BASIS | `salary_slip` · `contract` · `policy` · `calculator` · `employer_statement` · `estimate` |
| DD-WRK-RESPONSE-POSITION | `agree_will_pay` · `agree_in_part` · `dispute` · `object_forum` · `request_information` · `propose_mediation` |
| DD-WRK-COUNTERCLAIM | `notice_shortfall` · `training_bond` · `asset_recovery` · `advance_loan` · `clawback` · `breach_confidentiality` · `breach_non_solicit` · `other` |
| DD-WRK-FTE-ISSUE | `non_renewal` · `early_termination` · `pay_parity` · `gratuity_pro_rata` · `conversion_to_permanent` · `benefits_parity` |
| DD-WRK-PLATFORM-CAT | `ride_sharing` · `food_grocery_delivery` · `logistics` · `e_marketplace` · `professional_services` · `healthcare` · `travel_hospitality` · `content_media` · `other` (CoSS Seventh Schedule) |
| DD-WRK-GIG-STATE | `KA` · `RJ` · `TG` (draft — informational) · `other` |
| DD-WRK-GIG-ISSUE | `deactivation_blocking` · `payout_withheld` · `incentive_not_paid` · `penalty_deduction` · `rating_dispute` · `safety_incident` · `insurance_claim` · `algorithmic_allocation` · `account_kyc` |
| DD-WRK-RESTRAINT-TYPE | `non_compete_post_exit` · `non_compete_notice_garden_leave` · `non_solicit_clients` · `non_solicit_employees` · `confidentiality` · `ip_assignment` · `training_bond` · `moonlighting` |
| DD-WRK-RESTRAINT-STAGE | `none` · `legal_notice_received` · `suit_filed` · `injunction_sought` · `injunction_granted` |
| DD-WRK-SENIORITY | `manager` · `senior_manager` · `director_vp` · `kmp_ceo_cfo_cs` · `whole_time_director` · `expatriate` · `founder` |
| DD-WRK-EXEC-CLAIMS | `notice_pay` · `contractual_severance` · `bonus_lti` · `clawback` · `reference` · `indemnity` · `relocation` · `esop` |
| DD-WRK-ESOP-INSTRUMENT | `esop` · `rsu_foreign_parent` · `sar` · `phantom` · `sweat_equity` · `founder_shares` · `convertible` |
| DD-WRK-ESOP-ISSUE | `leaver_classification` · `accelerated_vesting` · `exercise_window` · `buy_back_price` · `lapse_on_termination` · `tax_withholding` · `clawback` · `founder_reverse_vesting` · `non_compete_linked_vesting` |
| DD-WRK-TEAM-PARTIES | `two_colleagues` · `employee_and_manager` · `team` · `cross_department` · `leadership_team` |
| DD-WRK-TEAM-ISSUE | `communication_breakdown` · `workload_allocation` · `credit_recognition` · `incivility_non_sexual` · `bullying_non_sexual` · `return_to_work` · `restructuring_tension` · `cultural_language` |
| DD-WRK-TEAM-OUTCOME | `working_agreement` · `communication_protocol` · `role_clarity` · `reporting_line_change` · `apology` · `follow_up_review` · `coaching_referral` |
| DD-WRK-DISC-GROUND | `gender` · `disability` · `transgender_identity` · `pregnancy_maternity` · `religion` · `caste` · `age` · `hiv_status` · `marital_status` · `other` |
| DD-WRK-DISC-REMEDY | `pay_correction` · `arrears` · `accommodation` · `role_restoration` · `policy_change` · `training` · `apology` |
| DD-WRK-WB-CHANNEL | `vigil_mechanism` · `audit_committee_chair` · `regulator` · `police` · `media` · `none` |
| DD-WRK-WB-RETALIATION | `termination` · `demotion` · `transfer` · `denial_of_increment` · `harassment` · `exclusion` · `adverse_appraisal` |
| DD-WRK-URGENCY | `none` · `document_withheld` · `imminent_deactivation` · `injunction_threatened` · `limitation_lt_30d` · `tribunal_window_lt_21d` |

---

## 7. Modus operandi per subtype

Common SLAs (App. A §6.3): scrutiny 2 WD; notice served 2 WD; response window 14 d (`response_window`); neutral appointment 3–5 WD after consent; first session ≤ 14 d; mediation 45 d (+60); closure and relieving ≤ 7 d after settlement. Neutrals: `END-WRK` endorsement; structural-conflict check at every appointment (S-21).

### 7.1 F&F / wages (W01) — `wrk.individual.v1` / `wrk.money_conciliation.v1`

| Step | Actor | Action | SLA / clock | Documents | Notices | Decision point |
|---|---|---|---|---|---|---|
| 1 | Employee | Explorer → F-WRK-02/30 + EB-WRK; runs `wrk.ff@2` | `wrk_wages_2wd` from separation (info) | salary slips, letters | `wrk.disclosure.cow45` | POSH/safety screen passed? |
| 2 | Case manager | Scrutiny; worker test; limitation | 2 WD | — | — | accept / signpost |
| 3 | System | Invitation to employer HR/legal (corporate routing) | D0; reminders D3, D7 (call), D21, D28; close D30 | — | TPL-WRK-N01 | respond / no response |
| 4 | Employer | F-WRK-05 + F-WRK-18 | 14 d | F&F statement | — | admit / dispute |
| 5 | Parties | Negotiation on computed heads; statutory heads locked "pay in full" | 14 d | calculator runs | — | agreement? |
| 6 | Neutral | Mediation/conciliation session(s) | 45 d / 30 d | — | T-48 h, T-2 h reminders | settled / not |
| 7 | Neutral + P06 | TPL-WRK-S01 F&F Settlement: payment schedule, relieving/experience letter milestones, carve-outs | 7 d | — | — | lint pass (HB-WRK-FLOOR-01, HB-WRK-WB-01) |
| 8 | Parties | e-sign; e-stamp per State of execution (NN-09) | at signing | — | — | — |
| 9 | Escrow/direct | Tranches: signature → relieving letter → asset return (final release requires both; `ESCROW_MILESTONE_CONDITIONS_UNMET`) | per schedule | proofs | — | breach → enforcement pack |
| 10 | Case manager | Clean exit: relieving + experience + assets + PF/gratuity confirmation (App. A §5) | ≤ 7 d | — | closure report F-WRK-17 | closed |

### 7.2 Worker termination (W05) — `wrk.individual.v1`

| Step | Actor | Action | SLA / clock | Decision point |
|---|---|---|---|---|
| 1 | Worker / union rep | Explorer; F-WRK-21 → `worker`; GRC disclosure if `grc_required` | WC-05, WC-07, WC-09, WC-10 opened as applicable | pending forum? |
| 2 | Case manager | Record statutory stage; red banner if WC-10 < 21 d; offer parallel mediation | 2 WD | worker consents to parallel route |
| 3 | System | Invitation to employer (authority-to-settle request) | D0–D30 | accept / decline |
| 4 | Neutral | Pre-mediation calls; power-imbalance check; shuttle if requested | before session | — |
| 5 | Neutral | Mediation: reinstatement (voluntary), compensation, neutral reference, record correction | 45 d | settled / not |
| 6 | P06 | TPL-WRK-S02 Separation MSA + **F-WRK-25 IR Code settlement pack** (sign before conciliation officer, or memorandum with copies) | 7 d | route chosen |
| 7 | Parties | If Tribunal/conciliation pending: joint application / withdrawal pack | per forum | — |
| 8 | Case manager | Track acknowledgement of copies; compliance | — | closed |

### 7.3 Executive / covenant / ESOP (W10–W12) — `wrk.executive.v1`

| Step | Actor | Action | SLA / clock | Decision point |
|---|---|---|---|---|
| 1 | Claimant | F-WRK-22 / F-WRK-02; clause upload; `wrk_arbitrability()` per head | `limitation_contract` | ALLOW heads? |
| 2 | Registrar | NN-03 allocation (no party nomination); disclosure (Sixth Schedule) | 7 d | challenge window |
| 3 | Neutral (mediator) | Mediation; s.27 information card shown, no advice | 45 d | settled / impasse |
| 4 | Registrar | Impasse → arbitration with a **different neutral** (master §5.3); fresh consent if same neutral (`SAME_NEUTRAL_CONSENT_MISSING`) | `role_switch_consent` 7 d | — |
| 5 | Tribunal | Arbitration (expedited by agreement); s.17/EA for urgent covenant relief | s.23(4) 6 m; s.29A 12 m | award |
| 6 | P06 | Award / consent award; ESOP buy-back instruction; stamp | at signing | execution route (App. R) |

Valuation (W11): parties may jointly appoint a registered valuer whose report is evidence inside mediation/arbitration; where every party is a business entity, COM expert determination applies (V2).

### 7.4 Gig / platform (W08) — `wrk.gig.v1`

| Step | Actor | Action | SLA / clock | Decision point |
|---|---|---|---|---|
| 1 | Worker (WhatsApp-first, vernacular, voice notes) | F-WRK-24; screenshots → type copy (NN-32) | — | classification? → signpost |
| 2 | System | KA rule check: notice ≥ 14 d with reasons; IDRC status | WC-18, WC-19 | W-WRK-GIG-01 |
| 3 | Aggregator (portfolio protocol, PL-16) | Data pull (trip logs, ratings, penalties) via API/CSV | 3 WD | — |
| 4 | Neutral | Negotiation/mediation (30 d) with **funding-neutrality statement** where aggregator pays | 30 d | reactivation / payout / not settled |
| 5 | System | Outcome record; written-reasons log (KA compliance evidence); escalation pack to Welfare Board / RJ authority if unresolved | 7 d | closed |

Equator never acts as the Karnataka IDRC (statutory composition: management and worker representatives); an "IDRC-support" mode is behind flag `wrk_ka_idrc_support` OFF pending Q-C5.

### 7.5 Collective (W06/W17) — `wrk.collective.v1`

| Step | Actor | Action | Decision point |
|---|---|---|---|
| 1 | Employer or union | Enquiry (case-manager call); counsel-gate task | Ch. X applicable? |
| 2 | Case manager | Signpost conciliation officer / appropriate Government (always); WC-11, WC-12, WC-20 | facilitation agreed by both |
| 3 | Co-mediators (employer-side and labour-side experienced neutrals) | Facilitated bipartite negotiation; seniority list, financials | term sheet |
| 4 | P06 | Draft settlement for signature before the conciliation officer; VRS term sheet; or F-WRK-26 (flag) | lint HB-WRK-COLL-01 |

### 7.6 Team mediation (W19) — `wrk.team.v1`

| Step | Actor | Action | SLA | Decision point |
|---|---|---|---|---|
| 1 | HR sponsor | F-WRK-27; confirms no pending investigation or S-17 pause | — | eligible |
| 2 | Neutral | Individual confidential meetings; private safety screen | 10 d | joint session suitable? |
| 3 | Neutral | Joint facilitated conversation(s); no recording (NN-11) | 30 d | working agreement |
| 4 | Participants | Sign working agreement (non-monetary; not a disciplinary record) | — | sponsor receives only what all consent to |
| 5 | Neutral | 60-day review check-in | 60 d | closed / re-convene |

### 7.7 Other subtypes (summary)

| Subtype | Distinctive steps |
|---|---|
| PF/ESI (W04) | Undertaking schedule (deposit by date; ECR/challan upload); EPFiGMS text generated; closure on evidence |
| Gratuity (W03) | `wrk.gratuity@2`; trust/insurer joined as `gratuity_trust`/`insurer`; interest component itemised |
| Fixed-term (W07) | Contract-row capture; comparator evidence; W-WRK-FTE-01 |
| Contract labour (W09) | Tri-partite invitation; principal employer pays and recovers from contractor |
| Whistle-blower (W14) | Optional sealed tier `high`; carve-out clause preserving regulatory reporting auto-inserted; WRK_WHISTLE desk (P09) is the reporting channel |
| Discrimination (W15) | F-WRK-28; accommodation agreement; statutory complaint not barred |
| Injury (W18) | Settlement recorded before the competent authority (pack); health data sealed |

---

## 8. Pre-litigation journey (WRK profile of the `prelit_case` machine; App. A; S4 B5)

| Stage | WRK specifics |
|---|---|
| **Invite** | Sender "Equator Resolution Service Private Limited — Case Administrator", named case manager, case ID, QR and verify-notice page; voluntary; no threat language (lint); 60-word explainer + 60-second vernacular video; "Your other options" lists GRC / conciliation officer / CoW s.45 authority / gratuity authority / EPFiGMS as relevant; limitation disclaimer; DPDP notice (s.17(1)(a) context). Corporate respondents routed to HR/legal head and registered office (MCA master data). Cadence D0 → D3 → D7 (call 08:00–19:00) → D10 final (individual respondents) → D14 close; corporate D21/D28 → D30 close (also s.62(4) for conciliation). ≤ 6 contacts pre-consent; none on public holidays |
| **Consent** | Agreement to Mediate (F-WRK-13) or s.62(2) written acceptance; Aadhaar eSign/DSC; employer signatory authority upload; sub-consents (online mode, no recording, language, fee allocation, optional standstill (flag), optional arbitration agreement for non-workers only — "You do not have to sign this to mediate"); employee-side screen shows `wrk.disclosure.statutory_floor` |
| **Session** | Free 30-minute first information session (PL-07; respondent pays nothing); joint/caucus/shuttle; co-mediation option; WRK 45-day time-box |
| **Settlement** | Drafting checklist: itemised dues; statutory carve-outs; relieving/experience letters; PF/gratuity confirmation; no-gag clause; TDS treatment noted (parties' responsibility); performance schedule; escrow/milestones; default clause; confidentiality with regulatory carve-outs; e-stamp by State of execution |
| **Conversion** | Output ladder for WRK: (1) s.73 settlement with s.74 award status (non-worker money claims; Part III); (2) consent award (A&C s.30; non-worker with arbitration agreement; arbitrator ≠ mediator by default); (3) Lok Adalat recording pack (DLSA joint application, LSA s.20(2)); (4) **IR Code settlement pack** (workers); (5) contractual MSA. Never labelled "registered settlement", "decree" or "s.12A compliant" |
| **Compliance** | Instalments, escrow milestones, relieving/experience letters, PF exit marking, gratuity payment proof; `CLOSED_PERFORMED` / `CLOSED_BREACHED` → enforcement pack (s.36 for awards; suit on MSA; statutory claim revived for unpaid dues) |

KPIs from S4 B5.7 apply with WRK targets (§14).

---

## 9. Document checklists per subtype

Accepted formats (all): PDF, JPG, PNG, HEIC, DOCX, XLSX, CSV, MP3/M4A/OGG (voice notes), WhatsApp export (.txt/.zip); ≤ 25 MB per file; ClamAV scan; originals preserved, type copies labelled (NN-32). Verification codes: **SELF** party declaration · **OCR** extracted and party-validated · **CP** counterparty confirmation · **API** source-system pull (consented) · **CM** case-manager check.

| Code | Document | Subtypes | M/O | Verification |
|---|---|---|---|---|
| WD-01 | Appointment letter / employment contract | all except gig | M (O for blue-collar if none issued — W shown) | OCR + CP |
| WD-02 | Salary slips (last 6–12 months) | wages, F&F, benefits, termination | M | OCR (`document_extractor`) + CP |
| WD-03 | Bank statement showing salary credits | wages, F&F | O | SELF/OCR |
| WD-04 | Attendance / leave records | wages, leave, F&F | O | CP/API (HRMS) |
| WD-05 | Resignation / termination / relieving letter | F&F, termination | M where exists | OCR + CP |
| WD-06 | F&F statement (employer) | F&F | M for employer response | CP |
| WD-07 | Company policies (leave encashment, notice, bonus, gratuity, ESOP) | as relevant | O | CP |
| WD-08 | Form 16 / TDS certificates | F&F, executive | O | OCR |
| WD-09 | PF passbook, UAN, ECR/challan | PF | M (PF) | SELF; employer ECR upload as undertaking evidence |
| WD-10 | ESI IP card / benefit correspondence | ESI | M (ESI) | SELF |
| WD-11 | Show-cause notice, charge-sheet, inquiry report | dismissal | M where exists | OCR |
| WD-12 | GRC application/decision; conciliation correspondence; failure report | worker termination | M where exists | OCR + CM (date drives WC-10) |
| WD-13 | Fixed-term contracts (each) | FTE | M | OCR |
| WD-14 | Partner agreement version; deactivation notice; earnings, ratings, penalties logs | gig | M (agreement/notice if any) | API (aggregator) / screenshots (type copy) |
| WD-15 | Contractor licence/registration; work order; contractor wage slips | contract labour | O | CM |
| WD-16 | Restrictive-covenant clause; bond; training-cost proof | covenants/bonds | M | OCR |
| WD-17 | ESOP plan, grant letters, vesting schedule, board/shareholder resolutions, SHA, cap table, valuation reports | ESOP/founder | M (plan, grant) | CP; tier `high` |
| WD-18 | Disclosure acknowledgement (redacted); adverse-action evidence; vigil policy | whistle-blower | O | SELF; sealed tier option |
| WD-19 | Comparator pay data; accommodation request/response; UDID/medical certificate | discrimination | O (certificate → `health_sealed`) | SELF/CM |
| WD-20 | Injury report, medical records, insurer correspondence | injury | M | `health_sealed` |
| WD-21 | Board resolution / authority letter of employer signatory | all (organisation) | M before settlement signing | CM |
| WD-22 | Letter of Authority / Vakalatnama | represented parties | M | e-sign (NN-27) |
| WD-23 | Seniority list; notices to workers/Government; permission application/order; union recognition | collective | M | CM |

---

## 10. Practical difficulties and product solutions

| # | Difficulty | Product solution |
|---|---|---|
| PD-01 | Employers withhold relieving/experience letters as leverage | Letters are settlement milestones; final escrow tranche blocked until uploaded (`ESCROW_MILESTONE_CONDITIONS_UNMET`) |
| PD-02 | "Wages" basis disputes (CTC structures with low basic) | Calculators show contract basis and Code basis side by side with `wage_definition_warning` (LR-LAB-003); AI guardrail W9 |
| PD-03 | Small employers ignore invitations | Neutral institutional sender, verify-notice page, corporate routing, D7 call, informative (never threatening) mention of the CoW s.45 route; non-commencement notice without reasons |
| PD-04 | Blue-collar and gig workers lack documents | Accept screenshots, voice notes, WhatsApp exports; type copies (NN-32); employer/aggregator data pull under portfolio protocol |
| PD-05 | Tribunal 90-day window keeps running during mediation | WC-10 owned clock; red banner < 21 d; T-30 blocking task; copy lint against "pause" claims |
| PD-06 | Power imbalance (MSME, family business, migrant workers) | Shuttle, independent-advice prompts, support person, free first session, concession CN-EMPLOYEE, neutral may adjourn (WRK Rules r.8) |
| PD-07 | Employer signatory lacks authority | W-WRK-AUTH-01; authority upload before signing; settlement above `authority_limit_minor` routes to approver |
| PD-08 | Perceived employer capture (employer pays) | Funding-neutrality disclosure; NN-03 allocation; panel HR/union background balance published (S9 C-13); no party nomination |
| PD-09 | Structural conflict with POSH external-member services | S-21 rule; same individual never in both roles; disclosure + consent; `CONFLICT_DETECTED` |
| PD-10 | Union insists on representation | `union_rep` as `representative` under Letter of Authority; collective matters require it |
| PD-11 | State-by-State variation (S&E Acts, IR Rules forms, gig laws) | `state_pack` rows with `verified_on`, `next_reverify_due` (+180 d); unverified rows protective-only |
| PD-12 | Restrictive-covenant over-claiming by employers | s.27 information card with citations; no mediator advice (WRK Rules r.7); HB-WRK-RESTRAINT-01 |
| PD-13 | ESOP valuation deadlocks | Joint valuer report; COM expert determination where all parties are entities; confidentiality tier `high` toward investors |
| PD-14 | Retaliation fear (gig, whistle-blower) | Default no-retaliation clause; aggregator acknowledgement on F-WRK-24; sealed tier option for informants |
| PD-15 | Statutory dues "traded" for faster payment | HB-WRK-FLOOR-01 + DB CHECK; settlement lint; employee-side disclosure |

---

## 11. Integrations and APIs

| Provider / system | Purpose | Data | Legal basis / permission | Mode | Fallback |
|---|---|---|---|---|---|
| HRMS/payroll (e.g., Darwinbox, Keka, greytHR, Zoho People, SAP SuccessFactors, Workday) via enterprise connector (P09 §4C) | Separation referrals, F&F components, attendance | employee token, dates, components | Employer tenant contract (DPA); employee notice; DPDP s.7(a)/(i) or consent per purpose **[VERIFY — open: per-vendor API availability]** | API / SFTP CSV | Manual F-WRK-18 upload |
| Aggregator platforms | Trip/order logs, ratings, penalties, deactivation notices | partner token, logs | Portfolio protocol + worker consent | API / CSV | Screenshots + type copy |
| `KYC_PORT` (Surepass/IDfy class) | Employer KYB (MCA, GSTIN, Udyam); PAN of parties | org identifiers | Licensed aggregators (App. S §3; D2-06) | API | Manual KYB |
| EPFO (EPFiGMS, member passbook) | Grievance text; employee uploads own passbook | UAN (masked) | Employee self-service; no Equator credentials on EPFO | Manual export | — |
| ESIC grievance portal | Grievance text | IP number (masked) | Self-service | Manual export | — |
| State labour portals / conciliation officers | Statutory forum packs (F-WRK-23, F-WRK-25) | pack PDF | Party files | Manual export | Speed post via `POSTAL_PORT` (X-02) |
| Karnataka Welfare Board / IDRC | Escalation pack | pack PDF | Worker files | Manual | — |
| SHe-Box, IC/LC | POSH signposting only (P09) | none from WRK core | — | Link | — |
| `ESIGN_PORT`, `ESTAMP_PORT` | Settlements, agreements | documents | IT Act; State Stamp Acts | API | Physical execution |
| `ESCROW_PORT` | F&F tranches | amounts, milestones | RBI PA Directions (NN-13) | API | Direct payment with proof |
| `MESSAGING_PORT` / `VOICE_PORT` | WhatsApp-first vernacular notices, reminders | contact points | NN-12 (Equator-own calls only under `voice.equator_service_number.enabled`; WRK has no 1600 lender-number mode) | API | SMS/email/post |
| LawDocs | Employment ADR clause and exit-document templates | template IDs | Group interop (master §1) | API | Built-in templates |
| BestComply/LawDocsComply | Labour Code compliance calendar signals (F&F 2-WD, gratuity 30 d) to employer tenants | aggregate, no case data | NN-16 firewall: aggregate only | Event export | — |

Events published (App. F naming; P08 FR-P08-66 retained): `equator.wrk.separation.referred.v1` **W**, `equator.wrk.ff.settled.v1` **W**, `equator.wrk.relieving.due.v1` **W**, `equator.wrk.ff_clock.breached.v1`, `equator.wrk.worker_status.assessed.v1`, `equator.wrk.irc_settlement.submitted.v1`, `equator.wrk.gig.deactivation_check.completed.v1`, `equator.wrk.signpost.statutory_pack.generated.v1`. Payloads carry IDs, codes and minor-unit amounts only (no names, POSH, health).

APIs (`/v1`, problem+json): `POST /cases/{caseId}/wrk/worker-assessment` · `POST /cases/{caseId}/wrk/ff-statements` · `POST /cases/{caseId}/wrk/arbitrability` (returns per-head ALLOW/BLOCK) · `POST /wrk/calculators/{name}:run` (public, PII-free telemetry only) · `POST /cases/{caseId}/wrk/statutory-packs` · `POST /cases/{caseId}/wrk/irc-settlement-packs` · `POST /cases/{caseId}/wrk/gig-checks` · `POST /cases/{caseId}/wrk/team-agreements`. Idempotency keys on all POSTs.

---

## 12. Calculators (indicative only; never advice or valuation — NN-01; FR-P08-08)

All outputs carry `indicative: true`, `computation_trace[]`, `legal_rule_ids[]`, and the label "Computed from the figures and policy terms you entered". Money in paise; rounding half-up only at presentation.

| Calculator | Inputs | Formula | Parameters (pinned) | Golden vectors |
|---|---|---|---|---|
| `wrk.ff@2` | unpaid salary, arrears, leave encashment, bonus, reimbursements, gratuity (auto or entered), deductions[]; basic+DA+RA; total remuneration | `code_wage = basic_da_ra + max(0, (total − basic_da_ra) − 0.5 × total)`; `gross = Σearnings`; `net = gross − Σdeductions`; warning if `basic_da_ra < 0.5 × total` | LR-LAB-003 | V-FF-1: unpaid ₹60,000; leave ₹25,000; bonus ₹20,000; reimb. ₹5,000; gratuity ₹40,000 × 6 y → ₹1,38,462; deductions ₹8,000 → gross ₹2,48,462, **net ₹2,40,462**. V-FF-2: total ₹1,25,000, basic+DA ₹40,000 (32%) → Code wage **₹62,500**; gratuity 6 y → **₹2,16,346**; warning true |
| `wrk.gratuity@2` | Code wage, joining/exit dates, exit reason, engagement | `15 × wage × years / 26`; eligibility: ≥ 5 y continuous, none on death/disablement, FTE ≥ 1 y; `years` = completed years with part-year > 6 months counted as a year (`fte_pro_rata_method` = `part_year_over_6m` default; alternative `exact_fraction`) [Verified 22 Oct 2026: CoSS s.53(2) part-year > 6 months; FTE 1 year, IR Code s.2(o)(c)] **[VERIFY — open (counsel): FTE pro rata method]**; `payable = min(computed, ceiling)` | ceiling ₹20,00,000 (LR-LAB-009, VERIFY) | V-GR-1: ₹45,000 × 8 y → **₹2,07,692**. V-GR-2: FTE ₹30,000, 1 y 7 m → `part_year_over_6m` 2 y → **₹34,615**; `exact_fraction` → **₹27,404**. V-GR-3: ₹3,00,000 × 20 y → ₹34,61,538 → capped **₹20,00,000**. V-GR-4: resignation at 4 y 2 m, permanent → **not eligible** |
| `wrk.notice_severance@2` | monthly salary, notice days short, average monthly pay, completed years, last drawn wage | notice in lieu = `salary / 30 × days_short` (contract basis, divisor configurable); retrenchment = `15 × avg_pay / divisor × years`; re-skilling = `15 × last_wage / 26` | divisor default 26, alt 30 (LR-LAB-007) | V-NS-1: ₹60,000, 40 days short → **₹80,000**. V-NS-2: ₹60,000 × 7 y → **₹2,42,308** (/26) or **₹2,10,000** (/30). V-NS-3: re-skilling on ₹60,000 → **₹34,615** |
| `wrk.bonus@1` | wages for computation, months worked, days worked, allocable-surplus % (if known) | eligibility `days ≥ 30` and wage ≤ eligibility ceiling; `bonus = rate × min(wage, computation_ceiling) × months`; rate ∈ [8.33%, 20%]; minimum ₹100 | eligibility and computation ceilings (parameters; none notified under CoW s.26 at 22 Oct 2026) **[VERIFY — open: Q-C7]** | V-BN-1: computation wage ₹7,000 × 12, 8.33% → **₹6,997**; at 20% → **₹16,800**. V-BN-2: days worked 25 → **not eligible** |
| `wrk.limitation@1` | separation date, claim date, failure-report date, planned deactivation date, State calendar | WC clocks §3.4 | holiday calendar per State (P02 FR-P02-25) | V-LM-1: separation Fri 30 Oct 2026 (no holidays) → F&F due **Tue 3 Nov 2026**. V-LM-2: failure report 15 Jan 2027 → Tribunal last date **15 Apr 2027**. V-LM-3: KA deactivation planned 20 Nov 2026 → notice due by **6 Nov 2026**. V-LM-4: CoW claim arising 7 Nov 2026 → **7 Nov 2029** (App. A same-date convention) |

No calculator estimates CoW s.45 compensation, reinstatement value, back wages, damages or ESOP fair value (GX-3).

---

## 13. Outputs, templates, enforcement and registration route

### 13.1 Templates (EN + HI; App. L A4 format; legal review before activation)

| ID | Template | Allowed label | Blocked labels |
|---|---|---|---|
| TPL-WRK-N01 | Invitation to mediation | "Invitation to mediation under the Equator Workplace Mediation Rules" | "Legal notice", threats |
| TPL-WRK-N02 | Invitation to conciliation (A&C s.62) | "Invitation to conciliation under Part III of the Arbitration and Conciliation Act, 1996" | — |
| TPL-WRK-N03 | Notice invoking arbitration (s.21; non-worker) | "Notice of arbitration" | — |
| TPL-WRK-S01 | F&F Settlement Agreement | "Mediated Settlement Agreement (contract)" or "Settlement Agreement under section 73 … status of an arbitral award on agreed terms (section 74)" | "Decree", "MSA under s.19 Mediation Act" (flag OFF) |
| TPL-WRK-S02 | Separation MSA | as above | as above |
| TPL-WRK-S03 | IR Code settlement memorandum (F-WRK-25) | "Draft memorandum of settlement for submission under the Industrial Relations Code, 2020" | "Registered settlement" (until acknowledged) |
| TPL-WRK-S04 | Team working agreement | "Workplace Working Agreement (non-binding except as stated)" | "Disciplinary finding" |
| TPL-WRK-S05 | Accommodation agreement | "Reasonable Accommodation Agreement" | — |
| TPL-WRK-S06 | Gig outcome record | "Account review outcome record" | "IDRC decision" |
| TPL-WRK-A01 | Consent award / award (non-worker) | "Arbitral award on agreed terms (section 30)" / "Arbitral award" | award by the mediator without fresh consent |
| TPL-WRK-P01…P07 | Statutory forum templates (F-WRK-23) | "Prepared by the party with Equator's template" | "Filed by Equator" |
| TPL-WRK-R01 | Non-commencement notice / closure report | "Equator Non-Commencement Notice" / "Equator Mediation Closure Report" (no reasons) | "Failure report", "non-starter report" |
| TPL-WRK-R02 | Record of pre-action steps | "Record of pre-action steps" | "Certificate of compliance" |

Mandatory clauses (settlement lint): statutory dues paid in full; carve-outs from release (statutory dues, PF, gratuity, ESI, POSH complaints, criminal complaints, regulatory reports); no-gag clause; relieving/experience letter undertaking with date; asset return; tax note; default clause; confidentiality subject to law.

### 13.2 Enforcement routes

| Instrument | Route |
|---|---|
| s.73/s.74 settlement | Execution as an arbitral award (A&C s.36; CPC Order XXI); execution where assets are (*Sundaram Finance v Abdul Samad* (2018) 3 SCC 622) — App. R §4 pack |
| Consent award / award (non-worker) | s.36 after the s.34 window (LR-ARB-016) |
| Contractual MSA | Suit on the agreement; unpaid statutory dues revive the statutory claim (carve-out) |
| IR Code settlement | Binding effect per IR Code once completed in the prescribed manner; enforcement through the appropriate Government machinery (IR Code s.57(1), (3); recovery s.59(1)) [Verified 22 Oct 2026, India Code] |
| Lok Adalat award | Deemed decree (LSA Act s.21) via DLSA joint application (Q-C8) |
| s.42 award | Submitted to Government; IR Code enforcement, not A&C s.36 |

### 13.3 Registration

No WRK instrument needs Registration Act registration unless it transfers immovable property (e.g., employer housing) — then NN-08 physical route. Stamp duty by State of execution (NN-09).

---

## 14. Dashboards, KPIs and enterprise hooks

| KPI | Definition | Y1 target |
|---|---|---|
| F&F within 2 WD | separations with F&F paid ≤ `wrk_wages_2wd` / separations referred (employer dashboard) | report |
| Engagement rate | respondents responding in any way / delivered | ≥ 50% (individual v company) |
| Consent rate | consents / delivered | ≥ 35% voluntary; ≥ 70% under employer panel SLA |
| Settlement rate (commenced) | settlements / matters with ≥ 1 substantive session | ≥ 55% (money) |
| Median days to settle | consent → signature | ≤ 30 |
| Compliance rate | fully performed by due date | ≥ 85% |
| Conversion rate | settlements converted to s.73/s.74, consent award, Lok Adalat or IR Code settlement / eligible | ≥ 50% |
| Statutory-waiver attempts blocked | count | report (target trend ↓) |
| Structural-conflict declines | count | report |
| Signposting accuracy | audited | ≥ 98% |
| Procedural-justice gap | absolute difference between employer and employee scores | ≤ 0.4 |
| Panel balance | HR-background vs labour/union-background neutrals on WRK panel | published quarterly |

Widgets: separations pipeline; F&F ageing; WC-10 risk list; GRC compliance (P09); POSH external-member coverage and IC status (P09 — counts only, sealed); gig deactivation-notice compliance (aggregator tenants). No POSH data, no neutral win-rates (NN-07, NN-16).

Enterprise hooks: employer panel SLA (P09 Employer Panel MoU: 12 heads incl. POSH excluded, Code-wage basis, funding neutrality); bulk separations (`/employers/{id}/referrals` → P09 bulk intake); employment ADR clause (F-WRK-19 via P09 clause API: mediation first; excludes POSH; preserves statutory forums; arbitration only for non-workers and only contractual heads).

---

## 15. Competitor notes and Equator differentiation

| Competitor | WRK offering (research) | Equator differentiation |
|---|---|---|
| Presolv360 | Lists employment disputes among dispute types [V R1] | Worker/non-worker master switch; statutory-head split; IR Code settlement conversion |
| Sama | Mediation (insurance & employment) and **arbitration (partnership & employment)** [V R1/S3] | Equator blocks A&C arbitration for workers and statutory heads (HB-WRK-ARB-01/03) — defensible awards |
| CORD | Workplace/employment sector; dispute-system design for organisations [V R1] | Integrated GRC desk + POSH sealed IC SaaS + WRK ODR on one console (P09) |
| Jupitice | General ODR catalogue | WRK-specific calculators on the Code-wage basis; Karnataka gig rule pack |
| POSH consultancies / HR consultancies / law firms | IC training, external members, advisory | Sealed POSH SaaS with statutory clocks and annual-report generator; structural-conflict controls; no advice |
| Statutory forums (complementary) | Free GRC, conciliation, claims authority | Honest signposting with last dates; Equator runs alongside, never instead |

Benchmarks: ACAS early conciliation, EEOC mediation, Fair Work Commission (C3 §2.10); Italy/UK engagement data (S4 B3) set targets.

---

## 16. Data-model extensions (schema `wrk`; tenant RLS + case RLS; App. F §F.8 is the parent)

### 16.1 Migration `wrk_0002` (amends App. F `wrk.employment_records`)

```sql
ALTER TABLE wrk.employment_records DROP CONSTRAINT IF EXISTS employment_records_establishment_size_check;
ALTER TABLE wrk.employment_records ADD CONSTRAINT employment_records_establishment_size_check
  CHECK (establishment_size IN ('lt_10','10_19','20_49','50_99','100_299','300_plus','unknown'));   -- R3: 20 = GRC threshold
ALTER TABLE wrk.employment_records
  DROP CONSTRAINT IF EXISTS employment_records_engagement_check,
  ADD CONSTRAINT employment_records_engagement_check CHECK (engagement IN ('permanent','probationer','fixed_term','contract',
    'gig','platform','apprentice','trainee_intern','consultant_individual','consultant_entity','founder','expatriate_secondee')),
  ADD COLUMN state_of_work char(2) NOT NULL DEFAULT 'XX', ADD COLUMN principal_employer_org_id uuid REFERENCES core.organisations(id),
  ADD COLUMN basic_da_ra_minor bigint, ADD COLUMN total_remuneration_minor bigint,
  ADD COLUMN code_wage_minor bigint GENERATED ALWAYS AS (CASE WHEN total_remuneration_minor > 0 AND basic_da_ra_minor IS NOT NULL
     THEN basic_da_ra_minor + GREATEST(0, (total_remuneration_minor - basic_da_ra_minor) - total_remuneration_minor / 2) END) STORED,
  ADD COLUMN union_status text CHECK (union_status IN ('sole_negotiating_union','negotiating_council','union_not_recognised','none'));
-- is_workman stays nullable: NULL = uncertain → treated as worker (R4).
```

### 16.2 New tables

```sql
CREATE TYPE wrk.worker_status AS ENUM ('worker','non_worker','uncertain','not_applicable_gig');
CREATE TABLE wrk.worker_assessments (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  employment_record_id uuid NOT NULL REFERENCES wrk.employment_records(id), status wrk.worker_status NOT NULL,
  inputs jsonb NOT NULL, trace jsonb NOT NULL, rule_version text NOT NULL, contested boolean NOT NULL DEFAULT false,
  reviewed_by uuid, reviewed_at timestamptz, created_at timestamptz NOT NULL DEFAULT now());
-- trigger: sets employment_records.is_workman = (status='worker') ? true : (status='non_worker') ? false : NULL; contested → NULL until review.

CREATE TABLE wrk.claim_heads (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  head_code text NOT NULL, is_statutory boolean NOT NULL, amount_minor bigint CHECK (amount_minor >= 0), currency char(3) NOT NULL DEFAULT 'INR' CHECK (currency='INR'),
  period daterange, arbitrability text NOT NULL CHECK (arbitrability IN ('allow','block_statutory','block_worker','block_gig','block_pending_rule','block_other')),
  routed_forum_code text, limitation_status text CHECK (limitation_status IN ('in_time','expiring','critical','expired_condonable','expired')));
-- guard: an arbitration proceeding may include only heads with arbitrability = 'allow' (CASE_NOT_ARBITRABLE).

CREATE TABLE wrk.ff_statements (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  version int NOT NULL, prepared_by text NOT NULL CHECK (prepared_by IN ('employer','employee','calculator')), components jsonb NOT NULL,
  gross_minor bigint NOT NULL, deductions_minor bigint NOT NULL, net_minor bigint GENERATED ALWAYS AS (gross_minor - deductions_minor) STORED,
  statutory_wage_minor bigint, wage_definition_warning boolean NOT NULL, calc_run_id uuid, UNIQUE (case_id, version));

CREATE TABLE wrk.settlement_ext (settlement_id uuid PRIMARY KEY, tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  statutory_dues_waived boolean NOT NULL DEFAULT false, statutory_dues_paid_statement boolean NOT NULL,
  gag_clause_present boolean NOT NULL DEFAULT false, post_exit_noncompete_enforceable boolean NOT NULL DEFAULT false,
  relieving_due_on date, experience_letter_due_on date, assets_return_due_on date, pf_exit_confirmed boolean, gratuity_paid_confirmed boolean,
  output_instrument text NOT NULL CHECK (output_instrument IN ('msa_contract','s73_settlement','consent_award','irc_settlement','lok_adalat_pack','team_agreement','accommodation_agreement','gig_outcome_record')),
  CONSTRAINT wrk_no_statutory_waiver CHECK (statutory_dues_waived = false),                 -- LR-LAB-010
  CONSTRAINT wrk_no_gag CHECK (gag_clause_present = false),                                 -- HB-WRK-WB-01
  CONSTRAINT wrk_no_enforceable_restraint CHECK (post_exit_noncompete_enforceable = false),  -- LR-LAB-011
  CONSTRAINT wrk_statutory_statement CHECK (output_instrument IN ('team_agreement','gig_outcome_record') OR statutory_dues_paid_statement));

CREATE TABLE wrk.irc_settlement_packs (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  state_code char(2) NOT NULL, form_ref text NOT NULL, route text NOT NULL CHECK (route IN ('before_conciliation_officer','bipartite_memorandum')),
  document_id uuid NOT NULL, copies jsonb NOT NULL DEFAULT '[]', status text NOT NULL CHECK (status IN ('draft','signed','submitted','acknowledged')),
  acknowledged_ref text, CHECK (status <> 'acknowledged' OR acknowledged_ref IS NOT NULL));

CREATE TABLE wrk.gig_checks (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  state_code char(2) NOT NULL, platform_category text NOT NULL, deactivated_on date, notice_served_on date, reasons_given text CHECK (reasons_given IN ('yes','no','unclear')),
  notice_days int GENERATED ALWAYS AS (deactivated_on - notice_served_on) STORED, ka_notice_compliant boolean, idrc_filed_on date, rule_version text NOT NULL);

CREATE TABLE wrk.team_mediations (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  sponsor_user_id uuid NOT NULL, participant_count int NOT NULL CHECK (participant_count >= 2), investigation_pending boolean NOT NULL,
  employer_pause_document_id uuid, sponsor_disclosure_scope text NOT NULL CHECK (sponsor_disclosure_scope IN ('attendance_only','attendance_and_agreement')),
  review_due_on date, CHECK (NOT investigation_pending OR employer_pause_document_id IS NOT NULL));

CREATE TABLE wrk.state_packs (id uuid PRIMARY KEY DEFAULT uuidv7(), state_code char(2) NOT NULL, kind text NOT NULL
  CHECK (kind IN ('se_act','ir_rules_forms','gig_law','conciliation_directory','holiday_calendar')), payload jsonb NOT NULL,
  legal_rule_ids text[] NOT NULL, verified_on date, next_reverify_due date, status text NOT NULL CHECK (status IN ('active','unverified','superseded')));
-- unverified state_packs may only drive protective outputs (disclosures, warnings), never permissive routes (App. G §G.1).

CREATE TABLE wrk.calc_runs (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid REFERENCES core.cases(id),
  calculator text NOT NULL, version text NOT NULL, inputs jsonb NOT NULL, outputs jsonb NOT NULL, trace jsonb NOT NULL, created_at timestamptz NOT NULL DEFAULT now());
```

### 16.3 Enums and seeds

`wrk.value_band` (`VB0`–`VB4`); ladder codes (§2.2); dropdown lists (§6.7) as `core.option_lists` rows; forum codes (§3.3) in `routing_forums`; sub-codes registered in App. F §F.10.2: `WRK_STATUTORY_NOT_ARBITRABLE` → `CASE_NOT_ARBITRABLE`; `WRK_GIG_ARBITRATION_BLOCKED`, `WRK_CRIMINAL_EXCLUDED` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`; `WRK_GAG_CLAUSE`, `WRK_COLLECTIVE_STATUS_CLAIM`, `WRK_RESTRAINT_TERM` → `SETTLEMENT_LINT_FAILED`.

### 16.4 New clock kinds (extend `core.clock_kind`; add rows to App. A §6.3)

`wrk_monthly_wages_7d`, `wrk_cow_claim_3y` (AP-L, B-CRIT), `wrk_cow_appeal_90d`, `wrk_grc_to_conc_60d` (AP-M, B-CRIT), `wrk_conc_report_45d`, `wrk_conc_outer_2y` (AP-L, B-CRIT), `wrk_tribunal_90d` (AP-M, B-CRIT), `wrk_retrenchment_notice_1m`, `wrk_reskilling_45d`, `wrk_epf_appeal_deposit`, `wrk_ka_deactivation_notice_14d`, `wrk_ka_idrc_action_14d`, `wrk_ka_idrc_resolve_45d`, `wrk_s62_notice`.

### 16.5 Feature flags

`wrk_ir_s42_voluntary_arbitration` OFF · `gig_arbitration` OFF · `wrk_ka_idrc_support` OFF · `wrk_standstill_template` OFF · `wrk_rj_gig_pack` OFF (until commencement verified) · `wrk_exec_salary_arbitration` OFF (Q-C4) · `wrk_lok_adalat_pack` ON (protective; DLSA decides).

---

## 17. Acceptance tests (Gherkin; `tests/acceptance/wrk/`)

```gherkin
Feature: WRK vertical rules

Scenario: NN-07_wrk_posh_never_core_case
  Given a user answers "Yes" to Q-WRK-T02
  When the user tries to create a WRK case
  Then no core case is created
  And the API returns 422 "POSH_MUST_BE_SEALED" with rule "WRK_POSH_ROUTED_SEALED"
  And the user sees IC, Local Committee, SHe-Box and police details

Scenario: NN-24_wrk_threat_signposted_police
  Given Q-WRK-T01 is "Yes"
  Then the outcome is "OUT-WRK-SAFETY" and a signposting event to "POLICE" is recorded
  And no joint session can be scheduled for the matter

Scenario: LR-LAB-005_worker_arbitration_blocked
  Given F-WRK-21 returns status "worker" for a dismissal claim
  When an arbitration proceeding is requested
  Then the API returns 422 "WRK_WORKMAN_ARBITRATION_BLOCKED"
  And mediation and conciliation are offered

Scenario: LR-LAB-005_uncertain_treated_as_worker
  Given the claimant answers "Not sure" to Q-WRK-T05
  Then is_workman is NULL and arbitration is blocked as for a worker

Scenario: HB-WRK-ARB-01_statutory_heads_split
  Given a non-worker manager with an arbitration clause claims contractual severance ₹8,00,000 and gratuity ₹2,07,692
  When wrk_arbitrability() runs
  Then severance is "allow" and gratuity is "block_statutory"
  And the statement of claim lists only severance
  And a gratuity application pack (F-WRK-23) is generated for the competent authority

Scenario: LR-LAB-010_statutory_dues_waiver_rejected
  When a settlement with statutory_dues_waived = true is submitted
  Then the API returns 422 "STATUTORY_WAIVER_FORBIDDEN" with rule "WRK_STATUTORY_DUES_WAIVER"
  And a direct SQL insert fails constraint "wrk_no_statutory_waiver"

Scenario: HB-WRK-WB-01_gag_clause_blocked
  Given a separation MSA contains a clause barring complaints to any regulator
  When the settlement is linted
  Then signing is blocked with "SETTLEMENT_LINT_FAILED" rule "WRK_GAG_CLAUSE"

Scenario: LR-LAB-002_ff_clock_opened
  Given separation on Friday 30 Oct 2026 and no holidays in the State calendar
  Then clock "wrk_wages_2wd" is due on Tuesday 3 Nov 2026 and is shown to both parties

Scenario: WC-10_tribunal_banner
  Given a failure report received on 15 Jan 2027
  Then clock "wrk_tribunal_90d" is due on 15 Apr 2027 with an owner
  And from 26 Mar 2027 (fewer than 21 days left) a red banner shows on party and case-manager screens

Scenario: LR-LAB-004_grc_signpost_required
  Given a worker grievance at an establishment of band "20_49"
  When the case manager tries to close the case
  Then closure is refused with 409 "SIGNPOSTING_REQUIRED" until the GRC signposting event is recorded

Scenario: WRK_establishment_band_19_no_grc
  Given establishment band "10_19"
  Then grc_required is false and the GRC disclosure is not mandatory

Scenario: WRK_structural_conflict
  Given Equator supplies the employer's IC external member "N1"
  When "N1" is proposed as mediator for a money dispute with that employer
  Then the API returns 409 "CONFLICT_DETECTED" with rule "WRK_STRUCTURAL_CONFLICT"

Scenario: WRK_gig_arbitration_blocked_by_default
  Given a gig worker's payout dispute and flag "gig_arbitration" OFF
  When arbitration is requested
  Then the API returns 422 "MECHANISM_NOT_PERMITTED_FOR_VERTICAL" with rule "WRK_GIG_ARBITRATION_BLOCKED"

Scenario: LR-GIG-001_ka_short_notice_warning
  Given state "KA", notice served 10 Nov 2026 and deactivation 20 Nov 2026
  Then the gig check records notice_days 10, ka_notice_compliant false and warning "W-WRK-GIG-01"

Scenario: WRK_s42_flag_off
  Given flag "wrk_ir_s42_voluntary_arbitration" is OFF
  Then F-WRK-26 is not offered and no s.42 proceeding can be created

Scenario: HB-WRK-COLL-01_collective_label_lint
  Given a bipartite settlement draft labelled "Registered settlement under the IR Code"
  Then the template lint fails with "SETTLEMENT_LINT_FAILED" rule "WRK_COLLECTIVE_STATUS_CLAIM"

Scenario: NN-01_calculator_not_valuation
  When the AI assistant is asked "How much will the Tribunal give me?"
  Then it refuses with GX-2/GX-3 refusal text and offers the deterministic calculators and forum information

Scenario: NN-02_explorer_fallback_parity
  Given the LLM is unavailable
  When the Explorer is completed with identical answers
  Then the route, outcome code and clocks equal those produced with AI assistance

Scenario: NN-20_cow45_disclosure_on_wage_claim
  Given a wage claim is accepted
  Then disclosure "wrk.disclosure.cow45" is shown in the party's language and a signposting event is recorded

Scenario: NN-27_union_representative_authority
  Given a union representative without a signed Letter of Authority
  When the representative tries to accept a settlement
  Then the action is refused and the worker's own e-sign is requested

Scenario: WRK_final_escrow_release_conditions
  Given relieving letter uploaded but assets-return evidence missing
  When the final tranche release is requested
  Then the API returns 409 "ESCROW_MILESTONE_CONDITIONS_UNMET"

Scenario: WRK_team_mediation_investigation_pending
  Given a team-mediation request with investigation_pending true and no employer pause document
  Then creation fails the CHECK and the sponsor is asked for the pause decision

Scenario: NN-04_wrk_clock_owner_required
  Given clock "wrk_conc_outer_2y" has no owner
  When closure is attempted
  Then the API returns 409 "CLOCK_UNOWNED"

Scenario: NN-17_no_pause_limitation_copy
  Given a template containing "we will pause your deadline"
  Then CI template lint fails (PL-15)
```

---

## 18. Open items and counsel questions

### 18.1 Counsel questions (S4 Q-C1…Q-C13, carried; owner Head of Legal)

| ID | Question | Blocks |
|---|---|---|
| Q-C1 | Validity of standstill/tolling agreements during private mediation/Part III conciliation (Contract Act s.28; Limitation Act; A&C s.81) | `wrk_standstill_template` |
| Q-C2 | Enacted IR Code s.42 text and Central/State forms; may an institution administer and charge | `wrk_ir_s42_voluntary_arbitration` |
| Q-C3 | Whether an Equator-mediated worker settlement is an IR Code "settlement"; prescribed form; binding-effect section (ID Act s.18 analogue); whether a Part III s.74 settlement binds an industrial dispute | F-WRK-25 copy; §1.3 conciliation note |
| Q-C4 | Scope of CoW s.57 for managers' contractual salary arrears; *Dushyant Janbandhu* citation | `wrk_exec_salary_arbitration` |
| Q-C5 | Equator as external neutral/support for Karnataka IDRC; enforceability of platform-worker arbitration | `wrk_ka_idrc_support`, `gig_arbitration` |
| Q-C6 | CoSS Ch. VII equivalent of EC Act s.28 registration of agreements | W18 output |
| Q-C7 | CoW s.26 bonus ceilings; CoSS s.53(3) gratuity ceiling notification | `wrk.bonus@1`, `wrk.gratuity@2` parameters |
| Q-C8 | DLSAs accepting joint pre-litigation Lok Adalat applications with pre-agreed terms; stamp duty | `wrk_lok_adalat_pack` copy |
| Q-C10 | DPDP s.17(1)(a) for respondent contact before consent | invitation cadence |
| Q-C11 | Non-disparagement/confidentiality vs SEBI PIT informant protection and vigil mechanism | HB-WRK-WB-01 wording |
| Q-C12 | FTE early termination as retrenchment; FTE pro rata gratuity method | W-WRK-FTE-01; `fte_pro_rata_method` |
| Q-C13 | State S&E Acts termination/appeal provisions (DL, UP, RJ, MH, KA, TN, TG) and overlap with IR Code | `wrk.state_packs` |
| Q-C14 (new) | HIV Act 2017 complaints-officer threshold; RPwD s.21 application to private establishments; CoSS maternity and EI Court limitation | §3.2 VERIFY rows |
| Q-C15 (new) | Rajasthan gig Act commencement/designated authority; other 2025 State gig enactments | `wrk_rj_gig_pack` |

### 18.2 New Appendix G rows proposed (status as shown; add in P08e migration)

| Rule ID | Statement (short) | Source | Status | Enforcement |
|---|---|---|---|---|
| LR-LAB-014 | Statutory wage, bonus, gratuity, PF, ESI, maternity and EC components are never arbitrated; claim heads are split | CoW s.57; CoSS; IR Code | IN_FORCE (protective) | `routing` HB |
| LR-LAB-015 | Managers' contractual salary arrears arbitrable | CoW s.57 (scope) | UNVERIFIED (permissive) | flag `wrk_exec_salary_arbitration` OFF |
| LR-LAB-016 | Monthly wages before the 7th of the next month | CoW s.17(1) | IN_FORCE | `clocks` C |
| LR-LAB-017 | Deductions ≤ 50% of wages | CoW s.18(3) | IN_FORCE | W |
| LR-LAB-018 | Statutory bonus 8.33%–20%; ≥ 30 days' work; ceilings as notified | CoW s.26 | IN_FORCE; ceilings UNVERIFIED | calculator CFG |
| LR-LAB-019 | Fixed-term parity and pro rata benefits | IR Code s.2(o); CoSS s.53 | IN_FORCE | W / calculator |
| LR-LAB-020 | EPF appeal requires 25% deposit | CoSS s.23 | IN_FORCE | D |
| LR-GIG-001 | Karnataka: 14 days' written notice with reasons before deactivation | KA Act 2025 | IN_FORCE | `wrk.gig_checks` W |
| LR-GIG-002 | Karnataka IDRC: action 14 days, resolution 45 days; escalation to Welfare Board | KA Act 2025 | IN_FORCE | C / S |
| LR-GIG-003 | Gig/platform workers: no arbitration by default | Equator policy (adhesion; S4 A1.1) | IN_FORCE (Equator policy) | HB |
| LR-DISC-001 | Gender non-discrimination in wages and recruitment | CoW s.3 | IN_FORCE | S |
| LR-DISC-002 | Disability, transgender and HIV-status non-discrimination; complaint forums | RPwD Act ss.20–23; TG Act ss.3, 9–11; HIV Act 2017 | IN_FORCE; sections partly UNVERIFIED | S |
| LR-WB-001 | No settlement term may restrict reporting to a regulator, police, court, IC or Audit Committee | CA 2013 s.177(9)–(10); LODR Reg. 22; Contract Act s.23 | IN_FORCE (protective) | HB |

### 18.3 Build-pack conflicts raised for the editor

1. App. F `wrk.employment_records.establishment_size` lacks the 20-worker band (R3) — fix in App. F and P08 §7.2.
2. App. A §4.5 ladder lists "IR Code s.42 voluntary arbitration via prescribed form" under rung 4 (A&C arbitration); V5 makes s.42 a separate track outside the A&C Rules — App. A should split the row.
3. P08 FR-P08-57 lists arbitration for `wrk.contractor_gig`; V5 blocks it for gig/platform workers (R7).
4. ~~P08 uses `wrk_ff_2wd` and `WRK_WORKMAN_ARBITRATION` (409)~~ — resolved in the v2 review: P08 now uses `wrk_wages_2wd` and `WRK_WORKMAN_ARBITRATION_BLOCKED` (422).
5. App. B Card WRK-STD cites `STATUTORY_DUES_WAIVER_BLOCKED`; canonical code is `STATUTORY_WAIVER_FORBIDDEN` (F.10.2 maps it — no change needed beyond copy).
