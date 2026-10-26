# Equator Resolution — Insurance Dispute Resolution Framework

**Version 1.0 · July 2026 · Law stated as at July 2026**
An Infrabyx Group venture · www.equatorresolution.com

---

## Read this first

Insurance is the only Equator vertical in which the State has already built a **free, competent,
policyholder-friendly forum**. The Insurance Ombudsman has 17 centres, costs nothing, needs no lawyer, and its
award binds the insurer up to ₹30 lakh while leaving the complainant free to go elsewhere.

Equator does not compete with it. This whole framework rests on one finding: in 2023-24 the Ombudsman centres
disposed of 49,705 complaints and treated **12,855 — roughly one in four — as non-entertainable**. Those
complaints failed on *process*: no written representation to the insurer, the one-year window missed, the
monetary limit exceeded, or the matter already pending elsewhere.

**Most rejected insurance complaints fail on process, not on merits.** Fixing that, and settling the disputes
the statutory forum structurally cannot reach, is the business.

> **New — the exhaustive reference.** `11 Practice Guides` now holds the **Insurance Products & Disputes
> Compendium** (25 pp): every line written in India — life/ULIP/annuity, health, government & micro schemes
> (PM-JAY, PMFBY, PMJJBY/PMSBY), motor, property & fire, marine/hull/transit, aviation, engineering, liability
> (CGL/PI/D&O), cyber, financial lines (credit/surety/fidelity/BBB), Employees' Compensation, crop & rural,
> title & specialty, and reinsurance — mapped against all 35 dispute types, the deciding document, the forum,
> and whether it is mediable. It is accompanied by the **Authorities & Citations Digest** (verified Supreme
> Court / NCDRC / IRDAI authorities + the IRDAI turnaround-and-interest regime) and the **Business Interruption
> & Emerging-Risk Supplement** (pandemic, cyber, parametric, climate). The Forms Pack now runs to **F-I26** with
> six line-specific claim schedules.

---

## The three rules that govern everything here

| # | Rule | Where it is enforced |
|---|------|----------------------|
| **R1** | **No arbitration on a retail policy.** IRDAI circular dated 27 October 2023 — retail general-insurance policies shall not contain an arbitration clause. Commercial policies may, by mutual agreement, have a *separate* arbitration agreement. | Form F-I02 (mandatory classification) · Form F-I13 (reviewed) · API 409 · **PostgreSQL CHECK constraint** · AI guardrail IN-G-02 |
| **R2** | **No settlement may waive a non-waivable statutory right**, or discharge future claims. | Form F-I16 · API 422 · **PostgreSQL CHECK constraint** |
| **R3** | **No case closes without a delivered signposting event and an owner on every clock.** | Form F-I13 · Form F-I19 · API 409 · **PostgreSQL trigger** |

These are not policies. They are constraints. There is no override header.

---

## What is in each folder

| Folder | Contents |
|--------|----------|
| **01 Master Blueprint** | `Equator_Insurance_Dispute_Resolution_Master_Blueprint.docx` — 111 pages, Parts A–I. The opportunity, the legal framework, the forum map, the process design, the data model, operations and economics, risk and ethics, annexures, model clauses, and the full text of all 20 forms. |
| **02 Developer Handoff** | The build spec: dropdowns, taxonomy, route matrix, Ombudsman eligibility engine, clock engine, form-field schema, workflow states, SLAs, API surface, integrations, PII map, AI guardrails and KPIs. 15 sheets. |
| **03 Workflow Diagrams** | 14 diagrams (PNG + SVG): lifecycle · **retail/commercial triage** · Ombudsman escalation · repudiation analysis · mis-selling · commercial arbitration · timeline · AI explorer · plus 6 UML sequence diagrams. |
| **04 Archive — Forms Pack** | **F-I01 to F-I26** as standalone Word documents (F-I21–F-I26 are line-specific claim schedules: life/ULIP, marine & transit, liability CGL/PI/D&O, crop & rural, government health scheme, cyber & BI). Also reproduced in full in Part I of the Blueprint. |
| **05 Board Deck** | 13-slide board and investor briefing. |
| **06 Calculators** | Ombudsman Eligibility & Clock Calculator · Health Claim Deduction Analyser · Motor Claim Settlement Estimator · Underinsurance, Average & BI Calculator. All with live formulas, recalculation-verified. |
| **07 Operations** | Neutral Toolkit & SOP Runbooks (6 runbooks, 6 scripts, 6 quick-reference grids) · Compliance & Security Workbook (controls IN-C-01 to IN-C-12, health-data handling, retention, incident response, audit programme). |
| **08 Outreach** | Policyholder leaflet (English + हिंदी) · website and channel copy · Policyholder Letters Library (12 letters, bilingual). |
| **09 Interactive Prototype** | Bilingual Dispute Explorer — working route matrix, Ombudsman eligibility engine, clock calculator, guardrailed AI assistant, draft generator. Open in any browser. |
| **10 Rules & Tariff** | Equator Insurance Dispute Resolution Rules (28 rules + the signposting schedule) · Schedule of Fees (retail, commercial, subscription, batched settlement days, waivers, refunds). |
| **11 Practice Guides** | **Products & Disputes Compendium** (the exhaustive reference — every line, every dispute, the master matrices, worked numericals, decision trees, verified authorities) · **Authorities & Citations Digest** (verified SC/NCDRC/IRDAI authorities + IRDAI turnaround/interest regime) · **BI & Emerging-Risk Supplement** (pandemic, cyber, parametric, climate) · Line Playbooks (health, motor, life, commercial, mis-selling) · Forum Map & Interfaces Guide · Clause Bank & Model Agreements. |
| **12 Financial & Market** | Competitive & Market Note · Financial Model (unit economics, 36-month build-up, scenarios). |
| **13 Institutional Readiness** | Go-live checklist (20 items) · empanelment rubric · insurer BD playbook · panel MoU heads of terms · regulatory note. |
| **14 Build Handoff** | Technical Architecture & Data Spec · AI Implementation & Evaluation Spec · `schema_in.sql` (23 tables, 9 enums, 3 triggers, 3 views) · `openapi_in.yaml` (24 paths, 23 schemas) · UI Wireframe Kit (9 clickable screens) · AI Eval Harness & UAT Pack (28 guardrail cases, 12 routing cases, 12 clock cases, 40 UAT scripts). |
| **15 Risk Register** | 20 risks scored severity × likelihood, with controls, owners and a risk-to-control map. |
| **16 Training & Certification** | ECIN — Equator Certified Insurance Neutral. 12 modules, 84 hours, assessment weighting, panel obligations. |

---

## Where to start, by role

- **Board / investor** → 05 Board Deck, then 12 Financial & Market.
- **Legal** → 01 Master Blueprint Parts B and C, then 10 Rules & Tariff and 11 Practice Guides.
- **Product / engineering** → 14 Build Handoff (`schema_in.sql` first — the constraints are the spec), then 02 Developer Handoff.
- **Operations** → 07 Operations, then 04 Forms Pack.
- **Business development** → 13 Institutional Readiness (the insurer BD section), then 05 Board Deck.
- **A policyholder** → 08 Outreach, or open the prototype in 09.
- **Anyone who needs the law on a specific line or dispute** → the **Products & Disputes Compendium** in 11, then the **Authorities & Citations Digest**.

## Verified authorities (July 2026)

The Compendium and Digest are grounded in genuine, web-verified authority. Pinpoint citations are marked `[verify]`
for counsel to confirm against the reporter; the case names are real. Key authorities relied on: *Mithoolal Nayak
v. LIC* (materiality / s.45); *Reliance Life Insurance v. Rekhaben Nareshbhai Rathod* (insurer's burden;
contra proferentem); *United India Insurance v. Orient Treasures* (contra proferentem); *Amalendu Sahoo v.
Oriental Insurance* and *National Insurance v. Nitin Khandelwal* (condition breach / nexus / non-standard
settlement); *National Insurance v. Boghara Polyfab* (discharge voucher under duress); *Emaar MGF v. Aftab Singh*
and *National Seeds Corp. v. M. Madhusudhan Reddy* (consumer remedy not ousted by arbitration); IRDAI (PPHI)
Regulations 2024 and the 2024 Master Circulars (cashless 1 hr / discharge 3 hr; claim 30 days; interest 2% above
bank rate).

---

## The numbers this framework is built on

| Indicator | Figure | Source |
|---|---|---|
| Complaints to the 17 Ombudsman centres, 2023-24 | 52,575 received; 49,705 disposed | Council for Insurance Ombudsmen, Annual Report 2023-24 |
| Of those disposed, non-entertainable | **12,855 — about one in four** | Same |
| Outcomes | 15,528 recommendations; 9,287 awards for complainants; 8,638 for insurers | Same *[verify — composition]* |
| Year-on-year | Disposal up over 43%; non-entertainable down about 50% | Same |
| Bima Bharosa grievances, 2023-24 | 2,15,569 (1,20,726 life) | IRDAI Annual Report 2023-24 *[verify — latest edition]* |

## What changed in the eighteen months to July 2026

- **Sabka Bima Sabki Raksha (Amendment of Insurance Laws) Act, 2025** — passed 16–17 December 2025, assent
  20 December 2025. Up to 100% FDI in Indian insurers. *[verify — provisions brought into force]*
- **Bima Sugam** — notified March 2024; Phase 1 live December 2025. *[verify — current scope]*
- **Draft IRDAI (Internal Insurance Ombudsman) Guidelines, 2025** — issued 23 July 2025, consultation closed
  17 August 2025. Would add a mandatory internal escalation before the statutory Ombudsman.
  *[verify — finalisation and commencement]*

---

## `[verify]` marks

Where a figure or legal position is genuinely open — a Bill passed but not commenced, draft guidelines not
finalised, or an annually published statistic that may have been superseded — it is marked **[verify]**. These
are not gaps; they are the points at which a reader must check the primary source. Every one is listed in the
platform-level *[verify] Register* with an owner and a check date.

---

## Standing instruction

If a proposed commercial arrangement, product or marketing message would require R1, R2 or R3 to be relaxed,
it is refused at officer level and reported to the Board.

*Equator Resolution is a private dispute-resolution institution. It is not the Insurance Ombudsman, IRDAI, a
consumer commission or a court. It does not give legal advice, does not represent any party, and does not
estimate what a claim is worth.*
