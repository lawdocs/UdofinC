# Phase P27 — ESG, BRSR, CSR and Sustainability *(v1.1)*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00–P02** (tenancy, audit ledger, Correction Entries, settings registry and rule packs — emission factors, thresholds and glide paths are rule-pack data);
> - **P03/P04** (sustainability obligations as content packs and compliance instances; maker-checker per KPI);
> - **P06** (CSR Committee, Board approvals, Board's report CSR annexure, BRSR section of the annual report, Reg 34 submission);
> - **P07** (DMS evidence classes for ESG — FR-P07-68; redline engine for policies such as ESG, CSR, climate policies);
> - **P08/P09** (climate and environmental risk in the taxonomy; climate scenarios into the stress engine);
> - **P11** (accounting bridge — net profit under s.198 for CSR, CSR expense postings, green-finance allocations);
> - **P12** (vendor master and TPRM — value-chain partners); **P13** (HR aggregates with k ≥ 5 suppression, X-36);
> - **P18** (utility/EHS/ERP connectors, assurer access); **P25** (global frameworks and foreign entities); **P28** (reports and board packs).
>
> **Sequencing:** Wave 2 (after P06 and P11 interface freezes). The CSR engine (§4H) can ship earlier as a P06-adjacent increment for unlisted companies because it needs only financials and governance.
>
> **Binding appendices:** A (new machines `esg.disclosure_cycle`, `esg.metric_value`, `esg.csr_project`, `esg.assurance` — added by the lead), B, C, D (CSO role, `ext_assurer`), G (legal rules — LR-SEBI BRSR, LR-MCA CSR), H (climate risk), J (§J.15 sustainability standards, §J.18 CSR accounting), M (export folder for sustainability — number to be assigned by the Appendix M owner), U (settings), AA/K (agents).
>
> **Requirements covered:** R-005 (listed-company and company compliance), R-009 (governance), R-010/R-011 (climate and environmental risk, scenarios), R-013, R-021, R-053 (annual report from data), R-059 (dashboards), R-066 (listed companies — BRSR), owner baseline Architecture Part 2 "Environment & Social Governance" (applicability, CSR engine, ESG metric library, double materiality, GHG accounting, data → disclosure → assurance lifecycle, climate risk, ratings, forms/registers/returns, KPIs, roadmap); G5 gap B; decision D-47.
>
> **Estimated effort:** 9 two-week sprints, squad of 8 (metric library and data capture 3, BRSR/BRSR Core and assurance 2, GHG engine 2, CSR and sustainable finance 1), plus a sustainability domain analyst (BRSR/GHG) and a CS for CSR.
>
> **v1.1 changes (25 October 2026)** — new phase porting the owner's ESG chapter, updated for the SEBI ESG changes of 28 March 2025 (BRSR Core assurance **or** assessment; value-chain disclosures voluntary from FY 2025-26 with partners ≥ 2% of purchases/sales; green-credits indicator), the RBI Climate Finance and Management of Climate Change Risks Directions, 2025 in the consolidated set, ICAI SSAE 3000, and EU Omnibus I for EU-exposed groups.

---

## 1. Objective and business outcome

Listed companies, large companies under the CSR provisions, and regulated lenders now carry sustainability obligations that combine disclosure, assurance, spending rules and risk management. The owner's baseline treated ESG as a full module; this phase builds it so that the CSO, CFO and CS can capture metrics once, compute GHG emissions with traceable methods, produce the SEBI BRSR (and BRSR Core subset ready for assurance or assessment), run the CSR cycle without missing an unspent-amount deadline, and give the Board a sustainability view — all in the same governed, evidence-backed way as compliance.

| Outcome | Exit-gate measure |
|---|---|
| Know what applies | Applicability engine switches on BRSR, BRSR Core, value-chain (voluntary), CSR, climate (RBI), green finance and voluntary frameworks per entity profile with explanation and citation |
| Capture once, use many times | Each metric captured once with unit, period, boundary, method and evidence; reused in BRSR, ratings questionnaires, board packs and voluntary frameworks; ≥ 60% of a repeat year's BRSR auto-populated |
| Assurance-ready | Every BRSR Core attribute has lineage from source evidence to disclosed number; maker-checker per KPI; frozen at assurer sign-off; first-time assurance with zero lineage gaps in the pilot |
| GHG done properly | Scope 1, Scope 2 (location- and market-based) and material Scope 3 categories computed with versioned emission factors stamped on each figure; base-year and restatement policy enforced |
| CSR never late | CSR obligation computed from financials; action plan approved; spend tracked; unspent-transfer deadlines owned with reminders; Form CSR-2 data sheet generated; zero missed CSR deadlines in UAT |
| Climate risk joined up | Climate risks in the P08 register; scenario inputs to P09; RBI climate-finance obligations tracked for lenders |
| Board visibility | ESG dashboard and Board/committee pack sections (P28) with targets vs actuals |

---

## 2. Scope (in / out)

**In scope**
- Sustainability applicability engine and obligation packs (SEBI BRSR and BRSR Core; Companies Act CSR; RBI climate-finance directions; SEBI green debt; ESG rating engagement; voluntary ISSB/TCFD/GRI; EU CSRD/ESRS for EU-exposed groups via P25).
- ESG metric library, data capture (forms, imports, connectors), unit validation, period and boundary management, maker-checker per KPI, evidence links.
- BRSR builder (Sections A, B, C; nine principles; essential and leadership indicators) and BRSR Core subset; XBRL/exchange-format hand-off data for human filing.
- Double materiality assessment.
- GHG accounting engine (GHG Protocol) with emission-factor library and restatement policy.
- Value-chain partner disclosures (voluntary) with partner data collection portal.
- Assurance/assessment workspace for external assurers/assessors.
- CSR engine (s.135, CSR Rules) end to end, including CSR-1 checks, unspent account, impact assessment, Form CSR-2 data.
- Climate and transition: risks, targets, transition plan tracker, scenario inputs.
- ESG ratings and sustainable finance registers (ratings, green/blue/yellow/transition debt use-of-proceeds and impact; green deposits for REs).
- Targets, dashboards, board reporting, exports.

**Out of scope**
- Filing BRSR on exchange portals and CSR-2 on MCA (prepare and validate only; NN-08).
- Carbon-credit trading, registry operations or offsets verification.
- Product-level life-cycle assessment and environmental engineering calculations beyond the GHG Protocol corporate inventory.
- Rating opinions — LDC never rates (it supports ESG Rating Provider data requests).
- Lender portfolio-level financed-emissions computation from loan data belongs to Finbyx (data owner); LDC receives aggregates (Scope 3 category 15) if Finbyx publishes them (Ecosystem change request, OI-P27-09).

---

## 3. Personas and permissions touched

| Role | What they do | Notes |
|---|---|---|
| `ten_kmp` (CSO — Chief Sustainability Officer / Head ESG) *(new sub-type, D-48)* | Accountable for materiality, metric library, BRSR, climate, ratings | Default owner |
| `ten_kmp` (CFO) | Financial-linked metrics, CSR spend, green-finance allocations, assurance engagement | Approves financial ESG KPIs |
| `ten_kmp` (CS) | CSR Committee, policy, Board approvals, CSR-2 filing data, BRSR in annual report | |
| `ten_dept_head` / site and function owners | Enter metrics (energy, water, waste, HR, safety, community) as makers | Per-KPI ownership |
| `ten_checker` | Review metric values and evidence per KPI | NN-05 |
| `ten_internal_auditor` | Assurance-readiness reviews | Read + review notes |
| `ext_assurer` *(new, D-48)* | External assurer or assessor of BRSR Core / sustainability information; time-boxed scope seat | Like auditor rooms (P10); D-12 pattern |
| Value-chain partner (external, OTP) | Submits requested ESG data through a partner form | No account beyond the request |
| `ten_board_member`, CSR Committee members | Approve materiality, CSR policy and plan, review dashboards | |
| `svc_vidhi` (VA-17 Sustainability Analyst, proposed) | Data-gap detection, narrative drafts, factor suggestions, ratings questionnaire pre-fill | L1 default (NN-50) |

---

## 4. Functional requirements

### 4A. Applicability and obligations

**FR-P27-01 — Applicability engine.** From the entity profile (P15: listing status, market-capitalisation rank as at 31 March, net worth, turnover, net profit, RE family, labelled-debt issuer flag, EU exposure, voluntary framework choices) the engine evaluates the sustainability rule pack and explains each result:

| Obligation | Default rule (rule pack; [VERIFY] values) | Citation |
|---|---|---|
| BRSR | Top 1,000 listed entities by market capitalisation (as at 31 March each year) include BRSR in the annual report | LODR Reg 34(2)(f); SEBI BRSR circulars |
| BRSR Core (nine attributes) — reasonable assurance or assessment | Glide path by market-cap rank (e.g., top 150 → 250 → 500 → 1,000 over successive years) with the 28 Mar 2025 option of assurance **or** assessment by an assessor under ISF standards [VERIFY current years] | SEBI BRSR Core circulars as amended 28 Mar 2025 |
| Value-chain ESG disclosures | **Voluntary** from FY 2025-26 for applicable entities; value-chain partners = upstream/downstream partners individually ≥ 2% of purchases or sales; voluntary assessment/assurance from FY 2026-27 | SEBI 28 Mar 2025 changes [VERIFY] |
| Green credits leadership indicator (Principle 6) | Disclose green credits generated/procured by the entity and its top-10 value-chain partners from FY 2024-25 | SEBI 28 Mar 2025 changes [VERIFY] |
| CSR | Net worth ≥ ₹500 crore or turnover ≥ ₹1,000 crore or net profit ≥ ₹5 crore in the immediately preceding financial year | Companies Act s.135(1); CSR Rules |
| CSR Committee | Required unless CSR obligation ≤ ₹50 lakh (functions then discharged by the Board) [VERIFY s.135(9)] | s.135(9) |
| Climate finance (RBI) | Commercial banks, SFBs, NBFCs, deposit-taking NBFCs, HFCs per the directions' applicability — green deposits framework, Board-approved policies, financing framework, third-party verification, impact assessment, disclosures | RBI (… – Climate Finance and Management of Climate Change Risks) Directions, 2025 (NBFC: RBI/DOR/2025-26/364 [VERIFY]) |
| Climate-related financial risk disclosures (RBI) | Draft disclosure framework (28 Feb 2024) — advisory only until finalised | NN-38 |
| Green/blue/yellow/transition debt | Issuers under SEBI NCS Regulations: use of proceeds, third-party reviewer, allocation and impact reporting | SEBI NCS framework [VERIFY master circular] |
| ESG ratings | Entities rated by SEBI-registered ESG Rating Providers — data requests, rating rationale responses | SEBI CRA Regulations (ERP chapter) |
| Voluntary frameworks | ISSB IFRS S1/S2, TCFD, GRI, CDP — mapping only | §J.15 |
| EU CSRD/ESRS | Only for groups in scope after Omnibus I (EU entity > 1,000 employees and > €450 million turnover; non-EU parent with EU turnover > €450 million and an EU subsidiary/branch > €200 million) | P25 overlay; §J.15 |

**FR-P27-02 — Glide-path tracking.** For BRSR Core and value-chain items, the engine records the entity's market-cap rank history and shows the year in which each requirement first applies; a rank change creates an Update (P05) and a planning task (lead time configurable). Unverified glide-path values are advisory (NN-38).

**FR-P27-03 — Obligation packs.** Each obligation is a content pack in P03 with checkpoints (Part-2 family `ESG-BRSR` to be added — OI-P27-01; until then checkpoints live in `SEBI-LISTED` and `MCA-CO` sheets) so that disclosure deadlines, Board approvals and filings appear in the compliance register and calendar.

### 4B. ESG metric library and data capture

**FR-P27-04 — Metric library.** Platform library of metrics (KPIs) by pillar, each with: ID, name, definition, unit and allowed units with conversion, aggregation rule (sum, weighted average, max), period type, boundary rule, required evidence, BRSR mapping (section/principle/indicator/question), BRSR Core attribute flag, framework mappings (ISSB, GRI, ESRS datapoints where relevant), source options (manual form, import, connector, other module), owner role default, validation rules (range, year-on-year variance threshold), and sensitivity (personal-data aggregates).

Pillars and examples:
- **Environment:** Scope 1, 2, 3 emissions (tCO2e) and intensities (per ₹ crore revenue, per unit of output, PPP-adjusted where required); energy consumption by source (renewable/non-renewable, GJ); energy intensity; water withdrawal, consumption and discharge by source and quality; water intensity; waste generated by category, recovered, disposed (MT); air emissions (NOx, SOx, PM where applicable); EPR obligations; biodiversity-sensitive areas; green credits.
- **Social:** employees and workers by gender, age band, category and permanence; differently-abled; wages paid to females as % of total; median remuneration by gender; return to work and retention after parental leave; benefits coverage (PF, gratuity, ESI, insurance); health and safety (LTIFR, fatalities, high-consequence injuries); training hours; complaints (sexual harassment counts — aggregate only, NN-13; discrimination; wages); grievance mechanisms; human-rights training; CSR beneficiaries; customer complaints by category (from P14); data-privacy complaints and breaches (from P12); product recalls.
- **Governance:** board composition and diversity (from P06), ethics and anti-corruption (P26 ethics registers — counts), conflicts of interest disclosures, related-party transactions summary (P06 RPTx), fines and penalties (P06 penalties register), public policy positions, cybersecurity incidents (P12), supplier code coverage.
- **Climate:** physical and transition risk exposures, targets, transition-plan milestones, financed emissions aggregates (lenders, if available from Finbyx), green-finance allocations.

**FR-P27-05 — Data capture paths (fewest clicks).** (a) **Forms** per reporting unit (site, branch, function) generated from the metric library with only the metrics assigned to that unit; save-as-you-go; offline-tolerant PWA; (b) **imports** — Excel template `LDC-DT-ESG-METRICS` (one row per unit × metric × period) and utility/EHS exports with mapping memory; (c) **connectors** — utilities (where APIs exist), EHS systems, ERP/GL, HRMS (P13 aggregates), meter data (P18); (d) **cross-module reuse** — governance, complaints, privacy and HR metrics are pulled from the owning modules, never re-keyed. Each value records source, method, evidence link(s), maker and timestamp.

**FR-P27-06 — Validation and variance.** Unit checks and conversions; range checks; completeness per unit and period; year-on-year variance above threshold requires an explanation; outliers flagged by VA-17 (advisory). A value cannot be approved without evidence when the metric requires evidence.

**FR-P27-07 — Maker-checker per KPI.** Each metric value is entered by a maker and approved by a checker (NN-05); approvals roll up: unit → function → entity; the CSO signs off the entity set; CFO co-signs financial-linked metrics (e.g., CSR spend, green-finance allocations, revenue denominators). Rejected values return with comments.

**FR-P27-08 — Periods and boundaries.** Reporting period (FY), boundary (standalone vs consolidated; operational control by default, financial control or equity share selectable per framework), inclusion/exclusion of subsidiaries and joint ventures with reasons, and base year per metric; changes to boundary trigger the restatement policy (§4F).

### 4C. BRSR and BRSR Core builder

**FR-P27-09 — BRSR structure.** The builder renders Section A (general disclosures), Section B (management and process disclosures) and Section C (principle-wise performance — nine NGRBC principles with essential and leadership indicators) in SEBI's format, populated from approved metric values and module data (P06, P12, P13, P14, P26), with narrative fields drafted by VA-17 (labelled drafts, NN-04) and confirmed by owners. Every number is a bound value (NN-37).

**FR-P27-10 — BRSR Core subset.** The nine BRSR Core attributes (GHG footprint; water footprint; energy footprint; embracing circularity — waste; enhancing employee well-being and safety; enabling gender diversity in business; enabling inclusive development; fairness in engaging with customers and suppliers; open-ness of business) **[VERIFY attribute list and parameters]** are flagged in the library; the Core view shows each parameter with value, intensity, lineage completeness and assurance/assessment status.

**FR-P27-11 — Disclosure checklist and freeze.** Each BRSR question is Filled / Not applicable with reason / Missing; publication is blocked while any mandatory question is Missing (same pattern as P06 FR-P06-81). On CSO + CFO approval the disclosure is frozen (snapshot hash); post-freeze changes create a restatement record. Outputs: PDF and DOCX section for the annual report (P06 FR-P06-78), exchange XBRL/Excel hand-off data **[VERIFY current exchange filing format]**, and a data workbook with lineage.

### 4D. Assurance and assessment workspace

**FR-P27-12 — Engagement set-up.** Engagement type (reasonable assurance, limited assurance, BRSR Core assessment under ISF standards), provider (assurer firm or assessor; independence declarations; non-audit-service conflict check where the statutory auditor is also engaged — tenant policy), scope (attributes, entities, period), standard (ICAI SSAE 3000; SSAE 3410 for GHG [VERIFY]; ISF assessment standards), timeline back-scheduled from the AGM (P06 critical path FR-P06-80).

**FR-P27-13 — Assurer seat.** `ext_assurer` receives a time-boxed scope grant (pattern of P10 FR-P10-89): metric values with lineage, evidence, methods and factor versions, sampling support (P10 sampling engine), query log and request list with auto-chasing; assurer findings and adjustments are recorded; the opinion/report is uploaded and linked; assured values are frozen.

**FR-P27-14 — Assurance readiness.** Before the engagement, an internal readiness review (internal audit or ESG team) runs checks: lineage completeness per attribute, evidence present, maker-checker complete, methods and factors stamped, reconciliations to source (e.g., electricity bills vs meter totals; HR headcount vs payroll), restatements explained; readiness score per attribute (advisory) and gap tasks.

### 4E. Double materiality

**FR-P27-15 — Process.** Topic universe (seeded from BRSR principles, ISSB/SASB industry topics, ESRS topical standards — tenant-editable) → financial-materiality scoring (likelihood × magnitude of effect on cash flows, cost of capital, access to finance) → impact-materiality scoring (scale, scope, irremediability, likelihood for actual/potential impacts on people and environment) → stakeholder input (surveys through P23 forms; investor, employee, customer, community, regulator, supplier groups; response summaries) → materiality matrix with configurable thresholds → Board (or committee) approval recorded in P06 → annual refresh and on material change. Outputs drive: which metrics are mandatory for the entity, Scope 3 categories in scope, value-chain boundary, assurance scope suggestions and narrative sections.

### 4F. GHG accounting engine

**FR-P27-16 — Inventory structure.** Organisational boundary (operational control default), operational boundary, base year, reporting year; emission sources register by facility (stationary combustion, mobile combustion, process, fugitive — refrigerants; purchased electricity, steam, heat; Scope 3 categories 1–15 as material).

**FR-P27-17 — Calculation.** Activity data × emission factor × GWP (IPCC AR version selectable; default per BRSR guidance [VERIFY]) with unit conversions; Scope 2 location-based (CEA grid emission factor for India, by year and grid [VERIFY latest CEA CO2 baseline database version]) and market-based (contractual instruments: RECs, green tariffs, PPAs with evidence); Scope 3 by method (spend-based, average-data, supplier-specific) with data-quality score per category. Every figure stores the factor ID and version, GWP set, method and data-quality tier (NN-22).

**FR-P27-18 — Emission-factor library.** Versioned library (platform-maintained, G): CEA grid factors, IPCC defaults, DEFRA/DESNZ conversion factors (for overseas operations and some Scope 3 categories), fuel properties, refrigerant GWPs; tenant-specific factors (supplier-specific or measured) as T with evidence. Factor updates never change frozen figures; a recalculation creates a new version and a restatement assessment.

**FR-P27-19 — Base-year recalculation and restatement policy.** Configurable significance threshold (default 5% of base-year emissions) for structural changes (acquisitions, divestments, outsourcing/insourcing), methodology changes and discovered errors; the engine proposes recalculation; the CSO approves; restatements are disclosed with reason.

**FR-P27-20 — Intensities and targets.** Intensity metrics (per revenue, per output, per employee, per square metre as configured); targets (absolute and intensity, base year, target year, pathway, SBTi status as tenant data); progress tracking and forecast against pathway.

### 4G. Value chain

**FR-P27-21 — Partner identification.** From P12 vendor master and P11 sales/purchase data, the system proposes the value-chain partners above the 2% threshold (or tenant-defined coverage target), computes coverage %, and records the selection with reasons.

**FR-P27-22 — Partner data collection.** Requests to partners via OTP-secured forms (data for the BRSR value-chain format; green credits; GHG supplier-specific data), reminders, partner self-declarations and evidence uploads, validation and maker-checker on receipt; partner data never flows to other tenants. Because value-chain disclosure is voluntary from FY 2025-26 (SEBI 28 Mar 2025), the module defaults to "voluntary — report if coverage ≥ tenant target" with comply-or-explain text option.

### 4H. CSR engine (Companies Act s.135; CSR Rules)

**FR-P27-23 — Applicability and obligation.** Applicability test from the preceding year's net worth, turnover and net profit (P11) — auto-flag with explanation; CSR obligation = 2% of the average net profit of the three immediately preceding financial years computed under s.198 (excluding items as the CSR Rules require, §J.18); set-off of excess spend from earlier years (up to three succeeding years, Board resolution); obligation register per FY.

**FR-P27-24 — Committee and policy.** CSR Committee constitution and composition check (P06; at least three directors with one independent director where required, or two for private companies/ where no ID required [VERIFY s.135(1) proviso]); CSR policy (P07) with Board approval; annual action plan (Rule 5(2)) — projects/programmes, Schedule VII area, implementation modalities, implementing agencies, fund utilisation schedule, monitoring mechanism, impact assessment need — recommended by the committee and approved by the Board.

**FR-P27-25 — Implementing agencies.** Agency master with CSR-1 registration number, legal form (s.8 company, registered trust/society, government entity), track record and documents; disbursal is blocked if the agency lacks a valid CSR-1 number (Rule 4(2)) [VERIFY]; agreements via P26 CLM; utilisation certificates collected.

**FR-P27-26 — Spend tracking and unspent amounts.** Project budgets, disbursements (from P11 GL tags), administrative overheads within the 5% cap (Rule 7(1)) [VERIFY]; at FY end: unspent amount for **ongoing projects** to be transferred to the Unspent CSR Account within 30 days of the end of the FY and spent within three FYs, else transferred to a Schedule VII fund within 30 days of completion of the third FY; unspent amount for **other than ongoing projects** to be transferred to a Schedule VII fund within six months of the end of the FY (s.135(5), (6)) **[VERIFY]**. Each transfer is a compliance instance with a statutory clock (NN-33) and reminders; transfers require evidence (bank statement).

**FR-P27-27 — Impact assessment.** Required for companies with average CSR obligation ≥ ₹10 crore in the three immediately preceding FYs for projects with outlays ≥ ₹1 crore completed at least one year before the assessment (Rule 8(3)) **[VERIFY]**; assessor engagement, report upload, Board placement, annual report annexure; expense cap for impact assessment (higher of 2% of CSR spend or ₹50 lakh) tracked [VERIFY].

**FR-P27-28 — Reporting and filing data.** Board's report CSR annexure (CSR Rules Annexure II) generated from the engine (P06 annual report section); Form CSR-2 data sheet (annual) prepared for human filing on MCA (NN-08); website disclosures of committee, policy and projects approved by the Board (s.135(4)) tracked as a checkpoint; capital assets created recorded per Rule 7(4).

### 4I. Climate and transition

**FR-P27-29 — Climate risk register link.** Physical (acute, chronic) and transition (policy, legal, technology, market, reputation) risks recorded in P08 with climate-specific attributes (time horizon, geography, sector exposure, channel — credit, market, operational, liquidity); lenders map sector and geographic exposures from Finbyx aggregates.

**FR-P27-30 — Scenarios.** Climate scenarios (NGFS-style orderly, disorderly, hot-house; or RBI/tenant-defined) are defined here as parameter sets and passed to the P09 stress engine (sector PD shocks, collateral value haircuts by geography, carbon-price effects); results return as P09 runs (NN-22).

**FR-P27-31 — RBI climate-finance obligations (REs).** For applicable REs: green-deposit framework records (eligible activities, allocation, third-party verification, impact assessment), Board-approved policies and financing framework, disclosures; tracked as checkpoints from the 2025 consolidated direction (catalogue lookup) with evidence. The 2024 draft disclosure framework is shown as advisory (NN-38) until finalised.

**FR-P27-32 — Transition plan.** Targets, levers (energy efficiency, renewable procurement, fleet, supplier engagement, product changes), milestones, capex/opex plans, responsible owners and progress; Board review cadence.

### 4J. ESG ratings and sustainable finance

**FR-P27-33 — Ratings register.** ERP name, product, rating, date, rationale, data requests received, responses (pre-filled by VA-17 from approved metrics; owner confirms), disagreements raised and outcomes.

**FR-P27-34 — Labelled debt and green finance.** Use-of-proceeds register for green/blue/yellow/transition debt (eligible categories, allocations, unallocated balance), third-party reviewer reports, impact metrics and annual reporting obligations; for REs, green-deposit allocation register (FR-P27-31).

### 4K. Global and voluntary frameworks

**FR-P27-35 — Framework mapping.** Each metric maps to ISSB (IFRS S1/S2), GRI, TCFD, CDP and ESRS datapoints where relevant; a framework view renders the disclosure index (e.g., GRI content index, ISSB index) from the same approved values; foreign entities in `gem` (P25) can be included in consolidated sustainability data with their local frameworks noted; EU-in-scope groups get an ESRS overlay switch (OFF by default; §J.15).

### 4L. Dashboards and board reporting

**FR-P27-36 — ESG dashboard.** Widgets: data completeness by unit and pillar; approvals pending; BRSR checklist status; Core lineage completeness; GHG trend by scope with targets; energy and water intensities; CSR obligation vs spend vs unspent clocks; assurance status; ratings; climate risk heat map; value-chain coverage. Configurable per role (P02/P28).

**FR-P27-37 — Board and committee packs.** Sections for the Board, CSR Committee and Risk/ESG Committee: performance vs targets, material topics, CSR plan and spend, assurance results, climate risk and scenario results — generated by P28 report templates with bound figures (NN-37).

### 4M. AI assistance (VA-17 Sustainability Analyst — proposed for Appendix AA/K)

**FR-P27-38 — Skills.** Data-gap and outlier detection (advisory); evidence-to-metric matching (proposes which uploaded bill supports which value); emission-factor suggestions with citations to the library (never invents a factor); narrative drafts for BRSR Section B and leadership indicators; ratings questionnaire pre-fill; materiality topic summaries from stakeholder responses. Default L1; it never approves a value, selects a factor without user confirmation, sets materiality or computes figures outside the engine (NN-37, NN-47, NN-50).


### 4N. Forms, registers and returns (port of baseline Tables 11-1 and 11-2, updated)

**FR-P27-39 — Forms.** All forms are generated from the metric library and rule pack (P02 form builder), validate against the framework and record evidence:

| Form | Captures | Validation (v1.1) | Feeds |
|---|---|---|---|
| ESG metric entry | Unit, metric, period, value, unit of measure, method, source, evidence | Unit conversion; range; variance explanation; evidence where required | Metric console, BRSR, frameworks |
| Materiality assessment | Topics, financial and impact scores, stakeholder inputs, thresholds | Scores in defined scales; Board approval reference before use | Disclosure scope, metric requirements |
| Value-chain partner | Partner, upstream/downstream, share of purchases/sales, requested ESG fields, green credits | **Partner threshold 2% and tenant coverage target** — the baseline's "75% boundary" rule is superseded by the SEBI changes of 28 Mar 2025 *(v1.1 correction)* | Value-chain disclosure (voluntary) |
| CSR project | Project, Schedule VII item, type (ongoing/other), agency (CSR-1), budget, phasing, impact-assessment need | Disbursal blocked without valid CSR-1; overhead cap; ongoing-project duration ≤ 3 years beyond the FY of commencement [VERIFY] | CSR engine, CSR-2 data |
| Assurance/assessment request | Scope, attributes, provider, type, standard | Independence declaration; scope ⊇ mandatory Core attributes | Assurance workspace |
| Green-finance use of proceeds | Instrument, eligible category, project, allocation, reviewer | Allocation ≤ proceeds; eligible category list from rule pack | Impact reporting |
| Climate scenario request | Scenario family, horizon, parameters | Parameter bounds | P09 stress engine |

**FR-P27-40 — Registers and returns.** BRSR / BRSR Core disclosure register (per FY with freeze hash); assurance register (attributes, provider, opinion, date); value-chain register; CSR register (projects, spend, unspent, transfers, capital assets) and Form CSR-2 data; ESG-rating register; green-finance register; GHG/climate inventory (scopes, factors, targets, scenario inputs); restatement register. Each is a projection over approved records — no direct edit.

### 4O. Controls (assurance-readiness control set; port of baseline Tables 8-2 and 14-3)

| Control | Risk mitigated | Type | Evidence emitted |
|---|---|---|---|
| Board-approved double materiality | Wrong or incomplete reporting scope | Preventive | Materiality record with approval reference |
| Source-to-disclosure lineage per figure | Unverifiable ESG figure | Detective | Lineage graph + evidence documents |
| Method and factor stamp per figure | Inconsistent or unsupported emissions | Detective | Methodology record (factor id, version, GWP) |
| Maker-checker per KPI | Wrong or unauthorised values | Preventive | Approval log |
| Reconciliation to source | Disclosed value does not tie to source | Detective | Reconciliation record (e.g., bills vs meters; HR vs payroll) |
| Immutable evidence after freeze/assurance (WORM) | Tampering, greenwashing | Preventive | Object Lock + ledger |
| Restatement log | Silent changes to published figures | Detective | Restatement record with approval |
| CSR-1 check before disbursal | CSR spend to ineligible agency | Preventive | Agency verification log |
| 2% computation and unspent-transfer engine | CSR shortfall or late transfer | Detective | Computation + transfer log with clocks |
| Maker-checker on disclosure and filing data | Wrong or unauthorised BRSR/CSR-2 | Preventive | Approval log |
| Value-chain threshold and coverage check | Incomplete value-chain disclosure | Preventive | Partner selection record |
| Green-finance allocation tracking | Misallocation of labelled-debt proceeds | Detective | Allocation register |
| Claims register for ESG statements in marketing/annual report | Greenwashing claims without evidence | Preventive | NN-19 claims entries |

Each control is registered in the P08/P10 control library so that internal audit and the assurer can test it; control results publish `ControlTestResultPublished` like any other control.

### 4P. ESG–risk linkage (port of baseline Table 5-2)

| ESG area | Risk in P08 taxonomy | Linkage |
|---|---|---|
| Climate — physical and transition | Credit, market, operational, strategic, reputational | Climate risks register; scenarios to P09 |
| Environment (resources, pollution, waste) | Operational, legal/compliance, reputational | Breaches (consent conditions, EPR) open risks and issues |
| Social (workforce, safety, community, POSH counts) | People, conduct, reputational | P13 aggregates feed KRIs |
| Governance | Compliance, conduct, governance | P06/P26 data |
| Disclosure and greenwashing | Compliance, reputational | Assurance controls; claims register |

### 4Q. Persona dashboards and RACI (port of baseline Tables 14-1 and 14-2)

| Persona | Default dashboard content |
|---|---|
| CSO | Targets vs actual, disclosure and assurance status, materiality, data completeness, ratings |
| CFO | CSR spend vs obligation and unspent clocks, assurance cost, green-finance allocation, financial denominators |
| Company Secretary | BRSR in annual report status, CSR-2 data readiness, Board CSR annexure, CSR Committee meetings |
| CRO | Climate/ESG risks, scenario impacts, KRIs |
| Internal Audit | Assurance readiness, lineage and evidence completeness, control effectiveness |
| Board / RMC / CSR Committee | ESG posture, Core attributes, targets, ratings, climate, CSR plan and spend |

| Activity | CSO | CFO | CS | Internal Audit | Board |
|---|---|---|---|---|---|
| Materiality assessment | A/R | C | C | C | A (approves) |
| Capture and validate ESG metrics | A/R | C | I | C | I |
| Build BRSR / BRSR Core | A/R | C | C | C | I |
| Obtain assurance or assessment | A | R | I | C | I |
| Run CSR cycle and prepare CSR-2 data | C | R | A/R | I | I |
| Climate risk and scenarios | A/R | C | I | C | I |
| ESG rating engagement | A/R | C | I | I | I |
| Board and disclosure reporting | A | C | R | C | A |

The RACI is tenant-configurable (P02); defaults seed role assignments and approval routes.

### 4R. KPIs and success metrics (port of baseline Table 16-1)

| KPI | Definition | Default target |
|---|---|---|
| BRSR / Core published on time | Disclosure included in the annual report by the due date | 100% |
| Assurance/assessment obtained (Core) | Completed for in-scope entities | 100% |
| Metric completeness | Captured vs required by attribute | ≥ 98% |
| Data-quality exceptions at freeze | Anomalous or missing values at disclosure | Declining trend |
| GHG lineage complete | Scope 1/2/3 figures with method, factor and evidence | 100% |
| CSR spend vs obligation | Spend ÷ obligation | ≥ 100% |
| Unspent CSR transfers on time | Transfers within statutory windows | 100% |
| Climate targets on track | Targets on pathway | Improving |
| Repeat-year auto-population | Share of BRSR values pre-filled from systems | ≥ 60% |
| Disclosure cycle time | Days from FY end to frozen BRSR | −40% vs baseline year |

### 4S. Migration and first-year set-up

**FR-P27-41 — Import last year's BRSR.** Upload the prior-year BRSR (PDF or exchange workbook); VA-17 proposes values for the comparative year with page references; the CSO confirms; confirmed values become prior-year comparatives (labelled "imported, not re-verified") so that year-on-year variance checks and intensity trends work from day one.

**FR-P27-42 — Guided set-up.** A seven-step wizard: entity and boundary → reporting units (import from P15 locations/branches) → applicability confirmation → metric assignment (auto from BRSR mapping) → factor library selection → CSR configuration (if applicable) → calendar (AGM-anchored). Target: a listed company ready to collect data in under two hours.


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P27-X01 — Rules, ports and filings.** CSR rules LR-MCA-034/035 and BRSR rule LR-SEBI-032 (Appendix G §G.16A.2) drive applicability; ESG data arrives through `ESG_DATA_PORT` and `ENERGY_EHS_PORT` (Appendix L §L.13) as draft metric values; emission factors are signed, effective-dated rule packs (NN-26 pattern); BRSR XBRL output is generated through P11's XBRL tooling and filed by a human (NN-08). Part-2 checkpoints come from the ESG-BRSR family (`templates/LDC-TPL-ESG-BRSR-v1.0`; Appendix E §E.15.27).

---

## 5. Workflows and state machines

### 5.1 Metric value (`esg.metric_value`)

`DRAFT` (maker) → `SUBMITTED` → `APPROVED` (checker) | `RETURNED` → … ; `APPROVED` values roll up; `FROZEN` at disclosure freeze or assurer sign-off; changes after freeze → `RESTATED` (new version with reason; restatement record).

### 5.2 Disclosure cycle (`esg.disclosure_cycle`)

`PLANNED` (scope, materiality refresh, assignments; critical path from AGM) → `COLLECTING` → `REVIEWING` (CSO checks, readiness review) → `ASSURANCE` (if applicable) → `APPROVED` (CSO + CFO; Board noting) → `FROZEN` → `PUBLISHED` (annual report, exchange hand-off) → `CLOSED`.

### 5.3 CSR project (`esg.csr_project`)

`PROPOSED` → `COMMITTEE_RECOMMENDED` → `BOARD_APPROVED` (in action plan) → `ONGOING` / `ACTIVE` → `COMPLETED` → `IMPACT_ASSESSED` (if required) → `CLOSED`; FY-end branch: unspent ongoing amount → `UNSPENT_TRANSFER_DUE` (30-day clock) → `TRANSFERRED`; three-year spend window → `FUND_TRANSFER_DUE` → `TRANSFERRED`.

### 5.4 Assurance engagement (`esg.assurance`)

`PLANNED` → `READINESS_REVIEW` → `FIELDWORK` (scope grant active) → `ADJUSTMENTS_AGREED` → `REPORT_ISSUED` → `CLOSED` (grant expired); unresolved adjustments block `APPROVED` in the disclosure cycle.

### 5.5 Applicability change on market-cap rank *(annual)*

`RANK_UPDATED` (31 March rank published by exchanges, imported or entered) → `APPLICABILITY_RECOMPUTED` → if a new obligation applies: `UPDATE_ISSUED` (P05 Update to CSO/CS with first-applicable year) → `PLANNING_TASKS_CREATED` (assignments, assurance procurement lead time) → `ACKNOWLEDGED`. If an obligation stops applying, completed history is preserved and future instances stop only after confirmation (NN-29).

### 5.6 Value-chain request

`DRAFT` → `SENT` (OTP link) → `REMINDED` (ladder) → `RESPONDED` → `UNDER_REVIEW` → `ACCEPTED` | `CLARIFICATION_REQUESTED` → … ; `EXPIRED` after the window, with "data not received" recorded for the coverage statement.

---

## 6. Screens and UX

Menu root: **Sustainability** (icon: leaf). "i" help keys `hlp.esg.*` explain BRSR, BRSR Core, Scope 1/2/3, location- vs market-based, double materiality, CSR-1, unspent CSR account, ongoing project.

| Screen ID | Name | Menu path | Key content and fewer-click design |
|---|---|---|---|
| SCR-ESG-01 | ESG Dashboard | Sustainability › Home | Widgets FR-P27-36 |
| SCR-ESG-02 | Applicability | Sustainability › Applicability | Obligations with "why it applies" and first-applicable year; rank history |
| SCR-ESG-03 | Metric Console | Sustainability › Metrics | Unit × metric × period grid; completeness heat map; bulk assign; approve queue |
| SCR-ESG-04 | Data Entry (unit form) | My Work › ESG data | Only assigned metrics; unit conversion; evidence drop zone; save-as-you-go |
| SCR-ESG-05 | Materiality Workspace | Sustainability › Materiality | Topic universe; scoring; survey results; matrix; Board approval link |
| SCR-ESG-06 | GHG Inventory | Sustainability › GHG | Sources by facility; scope totals; factor stamps; restatement assessments; targets |
| SCR-ESG-07 | Emission-Factor Library | Sustainability › Settings › Factors | Versions, sources, tenant factors with evidence |
| SCR-ESG-08 | BRSR Builder | Sustainability › BRSR | Sections A/B/C with checklist state; narrative drafts; Core view; freeze |
| SCR-ESG-09 | Assurance Workspace | Sustainability › Assurance | Engagement, scope grant, request list, findings, report |
| SCR-ESG-10 | Value-Chain Partners | Sustainability › Value chain | Threshold computation, coverage, requests, responses |
| SCR-ESG-11 | Partner Form (external) | external shell | OTP; requested fields only; evidence upload |
| SCR-ESG-12 | CSR Engine | Sustainability › CSR | Obligation computation; action plan; projects; agencies; unspent clocks; CSR-2 data |
| SCR-ESG-13 | Climate & Transition | Sustainability › Climate | Risk links (P08), scenarios (to P09), targets, transition plan |
| SCR-ESG-14 | Ratings & Green Finance | Sustainability › Ratings & finance | Ratings register; use-of-proceeds; green deposits |
| SCR-ESG-15 | Framework Index | Sustainability › Frameworks | ISSB/GRI/TCFD/ESRS index views from the same data |

Empty state: "Start with the metrics BRSR needs — we have pre-assigned them to your sites and functions. Import last year's BRSR workbook to pre-fill (2 clicks)."

---

## 7. Backend design

### 7.1 Modules touched

`esg` (owner — schema `esg`), `cnt`/`cmp` (obligation packs, checkpoints), `gov` (CSR committee, approvals, annual report), `acc` (financials, CSR postings, denominators), `hr` (aggregates), `erm`/`ral` (climate risks and scenarios), `tpr` (vendors), `lit` (agency agreements, ethics counts), `dms` (evidence), `aud` (sampling, readiness reviews), `int` (connectors, partner forms, assurer grants), `ai` (VA-17), `rpt` (P28 reports), `xpt`. Shared packages per OP-1.

### 7.2 Tables (schema `esg`; tenant, legal entity, RLS, bitemporal, ledger pointer)

| Table | Key columns |
|---|---|
| `esg.metrics` (library) | id, pillar, name, definition, unit, allowed_units, aggregation, period_type, boundary_rule, evidence_required, brsr_map jsonb, core_attribute, framework_map jsonb, validation jsonb, sensitivity, version |
| `esg.reporting_units` | id, type (site, branch, function, subsidiary), parent_id, location, boundary_included, owner_ids |
| `esg.assignments` | unit_id, metric_id, period, maker_id, checker_id |
| `esg.metric_values` | unit_id, metric_id, period, value, unit, normalised_value, method, source, evidence_ids[], maker_id, checker_id, state, frozen_at, version, restates_id |
| `esg.materiality_topics` / `esg.materiality_scores` / `esg.stakeholder_inputs` | topic, framework refs; scores (financial, impact components), threshold result; inputs: group, method, summary |
| `esg.ghg_sources` / `esg.ghg_activity` / `esg.ghg_results` | facility, scope, category, method; activity: quantity, unit, period, evidence; result: tco2e, factor_id, factor_version, gwp_set, data_quality |
| `esg.emission_factors` | id, source (CEA, IPCC, DEFRA, tenant), version, activity_type, unit, value, valid_from, valid_to, evidence |
| `esg.restatements` | metric/scope, reason, base_year_change, before, after, approved_by |
| `esg.targets` | metric, base_year, base_value, target_year, target_value, type, pathway jsonb |
| `esg.disclosures` / `esg.disclosure_items` | framework (BRSR, CORE, ISSB…), fy, state, snapshot_hash; item: question_ref, state (FILLED, NA, MISSING), value_refs, narrative_doc_id |
| `esg.assurance_engagements` / `esg.assurance_findings` | type, provider, standard, scope jsonb, grant_id, report_doc_id; finding: item, adjustment, status |
| `esg.value_chain_partners` / `esg.partner_requests` | partner_ref, share_pct, selected, coverage; request: fields, status, responses, evidence |
| `esg.csr_obligations` / `esg.csr_projects` / `esg.csr_agencies` / `esg.csr_transfers` | FY computation (inputs, amount, set-off); project: area, type (ongoing/other), budget, spend, agency_id, impact_required; agency: csr1_no, form, documents, verified; transfer: type, due_on, amount, done_on, evidence |
| `esg.climate_scenarios` | name, family, parameters jsonb, p09_run_ids |
| `esg.transition_actions` | lever, milestone, owner, capex, status |
| `esg.ratings` / `esg.green_finance` | ERP, rating, date, rationale; instrument, eligible category, allocation, unallocated, impact metrics, reviewer report |

### 7.3 APIs (`/api/v1/esg/...`)

`GET /applicability` · `GET|POST /metrics` · `GET|POST /units` · `POST /assignments:bulk` · `GET|POST /values` · `POST /values/{id}:approve` · `POST /imports/metrics` (preview, commit, undo) · `GET|POST /materiality/topics` · `POST /materiality:approve` · `GET|POST /ghg/sources` · `POST /ghg/activity` · `POST /ghg:calculate` · `GET /ghg/results?fy=` · `GET|POST /factors` · `POST /restatements` · `GET|POST /targets` · `GET /disclosures/{framework}/{fy}` · `POST /disclosures/{id}:freeze` · `GET|POST /assurance` · `POST /assurance/{id}/grant` · `GET|POST /value-chain/partners` · `POST /value-chain/requests` · `GET|POST /csr/obligations` · `GET|POST /csr/projects` · `GET|POST /csr/agencies` · `POST /csr/transfers/{id}:record` · `GET /csr/{fy}/csr2-data` · `GET|POST /climate/scenarios` · `POST /climate/scenarios/{id}:send-to-p09` · `GET|POST /ratings` · `GET|POST /green-finance`.

### 7.4 Domain events

Internal `in.lawdocscomply.esg.*`: `MetricValueSubmitted`, `MetricValueApproved`, `DisclosureFrozen`, `RestatementApproved`, `GhgInventoryCalculated`, `MaterialityApproved`, `AssuranceReportIssued`, `CsrObligationComputed`, `CsrTransferDue`, `CsrTransferRecorded`, `ClimateScenarioSubmitted`, `PartnerResponseReceived`. Ecosystem (proposed, change request): `FinancedEmissionsAggregatePublished` from Finbyx (consumed) — OI-P27-09.

### 7.5 Jobs and Temporal workflows

`DisclosureCycleWorkflow` (critical path from AGM; reminders), `UnitCollectionCampaign` (per period), `GhgRecalcJob` (on activity or factor change → draft version), `CsrYearEndWorkflow` (computes unspent; creates transfer instances with statutory clocks), `ValueChainRequestWorkflow`, `AssuranceGrantExpiryJob`, `RankWatcher` (annual market-cap rank update → applicability change).

---

## 8. Integrations

| Port | Use |
|---|---|
| `ACCOUNTING_PORT` | Net profit (s.198 inputs), turnover, net worth, CSR GL tags, revenue denominators |
| `ENERGY_EHS_PORT` *(new; Appendix L addition)* | Utility bills/APIs, meter data, EHS incident data |
| `WORKSPACE_PORT` / `STORAGE_PORT` | Evidence intake from SharePoint/Drive |
| `ECOSYSTEM_PORT` | Finbyx sector/geography exposure aggregates; financed-emissions aggregates (if published) |
| `EXCHANGE_FILES_PORT` | BRSR exchange-format/XBRL hand-off (prepare only) |
| `MCA_DATA_PORT` | CSR-1 registration verification via licensed data where available (else document check) |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `esg.rulepack.version` | G | latest verified | — | Platform content |
| `esg.boundary.default` | T | operational control | operational/financial/equity share | CSO |
| `esg.gwp_set` | G | per BRSR guidance [VERIFY] | AR5/AR6 | Platform content |
| `esg.restatement.threshold_pct` | T | 5 | 1–10 | CSO |
| `esg.variance.explain_threshold_pct` | T | 20 | 5–100 | CSO |
| `esg.evidence.required_default` | T | ON | — | CSO |
| `esg.value_chain.mode` | T | voluntary | voluntary / comply-or-explain | CSO |
| `esg.value_chain.partner_threshold_pct` | G | 2 | ≥ rule | Platform content |
| `esg.value_chain.coverage_target_pct` | T | 75 | 0–100 | CSO |
| `esg.core.option` | T | assurance | assurance / assessment | CFO + CSO |
| `esg.csr.reminder_offsets_days` | T | [30, 15, 7, 3, 1] | — | CS |
| `esg.csr.admin_overhead_cap_pct` | G | 5 | rule | Platform content |
| `esg.csr.block_disbursal_without_csr1` | L | true | — | — |
| `esg.esrs_overlay.enabled` | T | OFF | requires P25 EU pack | CSO |
| `esg.ai.va17.autonomy_ceiling` | T | L1 | L0–L1 | CSO (NN-50) |
| `esg.import.undo_hours` | T | 24 | 1–72 | CSO (NN-49) |

---

## 10. Security, privacy and audit

Personal data enters only as aggregates (HR, safety, complaints) with k ≥ 5 suppression for small cells (X-36); POSH as counts only (NN-13). Partner data is tenant-confidential and never shared across tenants. Assurer access is time-boxed and logged (D-12 pattern). Frozen disclosures and assured values are immutable; restatements are new versions (NN-02, NN-22). Emission factors and methods are versioned; every figure is reproducible.

---

## 11. AI touchpoints and guardrails

| Touchpoint | What VA-17 does | Guardrail |
|---|---|---|
| Data gaps and outliers | Flags missing or unusual values | Advisory; never changes values (NN-47) |
| Evidence matching | Proposes evidence ↔ value links | User confirms |
| Factor suggestion | Suggests a library factor with citation | Never invents factors; user selects |
| Narratives | Drafts BRSR narrative fields | Draft until owner confirms (NN-04); no AI figures (NN-37) |
| Ratings questionnaires | Pre-fills from approved values | Owner confirms each answer |
| Materiality summaries | Summarises stakeholder input | Scores and approval are human |

---

## 12. Acceptance criteria (`tests/acceptance/p27/*.feature`)

```gherkin
Feature: Applicability
  Scenario: Listed company within top 1,000 gets BRSR
    Given entity "Beta Industries Ltd" ranks 640 by market capitalisation on 31 Mar 2026
    When the applicability engine runs
    Then BRSR applies for FY 2025-26 with citation LODR Reg 34(2)(f)
    And value-chain disclosure shows "voluntary" with the 2% partner threshold

Feature: Metric governance
  Scenario: Value needs evidence and a checker
    Given metric "Electricity purchased (GJ)" requires evidence
    When maker "Site-Pune" submits 12,400 GJ without evidence
    Then submission is refused with "Evidence required"
    And after attaching bills the value goes to the checker, who cannot be the maker

Feature: GHG engine
  Scenario: Scope 2 stamps factor version
    Given 3,444,000 kWh grid electricity in FY 2025-26 for site Pune
    When the inventory is calculated with CEA factor version "CEA-2025"
    Then the Scope 2 location-based result stores factor id, version and GWP set
    And a later factor update creates a draft recalculation, not a change to frozen results

Feature: CSR clocks
  Scenario: Unspent ongoing-project amount transfer
    Given FY 2026-27 ends on 31 Mar 2027 with ₹42 lakh unspent on ongoing project P-3
    Then a transfer instance to the Unspent CSR Account is due on 30 Apr 2027
    And reminders fire at 30, 15, 7, 3 and 1 days before the due date

  Scenario: Disbursal blocked without CSR-1
    Given implementing agency "Asha Trust" has no CSR-1 number recorded
    When the CFO approves a disbursal
    Then the disbursal is blocked with "Valid CSR-1 registration required"

Feature: Disclosure freeze
  Scenario: BRSR cannot be published with missing items
    Given BRSR question "P6-E1 energy consumption" is MISSING
    When the CSO clicks Publish
    Then publication is refused
    And after approval and freeze, a later value change creates a restatement record
```

```gherkin
Feature: Restatement policy
  Scenario: Acquisition above threshold triggers base-year recalculation proposal
    Given base-year Scope 1+2 emissions are 50,000 tCO2e and the restatement threshold is 5%
    When an acquired subsidiary adds 3,100 tCO2e of base-year emissions
    Then a base-year recalculation is proposed to the CSO with reason "structural change"
    And no frozen figure changes until the CSO approves and a restatement record is created

Feature: Value chain under 2025 rules
  Scenario: Partner selection uses the 2% threshold
    Given purchases from vendor V-7 are 2.4% of total purchases and from V-9 are 1.1%
    When the CSO proposes value-chain partners
    Then V-7 is proposed and V-9 is not
    And the coverage percentage of selected partners is computed and shown
```

NN tests: `NN-05_esg_maker_not_checker`, `NN-13_posh_counts_only_in_esg`, `NN-22_ghg_reproducible`, `NN-33_csr_transfer_clock`, `NN-37_no_ai_figures_in_brsr`, `NN-38_unverified_glidepath_advisory`, `NN-47_va17_never_approves`, `NN-49_metric_import_undo`, `NN-50_va17_ceiling`.

---

## 13. Deliverables and exit gate

**Deliverables:** `esg` module; metric library (≥ 250 metrics mapped to BRSR, Core, ISSB/GRI where relevant); emission-factor library v1 (CEA, IPCC, DEFRA subsets) with sources; BRSR and Core templates; CSR engine with rule pack; materiality toolkit; assurance workspace; partner portal; report definitions for P28; export mapping; user guides (CSO, site data owners, CS for CSR, assurers).

**Exit gate:**
1. Gherkin and NN tests green.
2. Pilot listed company: FY data for 10 units captured, approved and frozen; BRSR generated with zero Missing items; Core lineage 100% for the nine attributes; a simulated assurance engagement completes with one adjustment.
3. GHG inventory for the pilot reproduced exactly from stored activity data and factors.
4. CSR cycle for a synthetic unlisted company: obligation computed from P11 data; action plan approved via P06; unspent transfer instance created with the right clock; CSR-2 data sheet generated.
5. Climate scenario passed to P09 and results returned.
6. WCAG 2.2 AA audit of data entry, partner form and BRSR builder (NN-21).
7. All [VERIFY] rule-pack values for enabled features verified or advisory.

**Indicative sprint plan.** S1 metric library, units, assignments, applicability engine; S2 data capture (forms, imports, connectors), validation, maker-checker; S3 GHG engine and factor library, restatement; S4 BRSR builder, Core view, checklist and freeze; S5 assurance workspace, readiness review, partner portal; S6 CSR engine end to end; S7 materiality, climate scenarios to P09, ratings and green finance; S8 dashboards, P28 report definitions, framework index, exports; S9 hardening, accessibility, pilot UAT.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P27-01 | Part-2 template family `ESG-BRSR` (or extension of SEBI-LISTED and MCA-CO) | Owner/template decision | Owner + content lead | Checkpoints in SEBI-LISTED / MCA-CO sheets |
| OI-P27-02 | SEBI 28 Mar 2025 circular number; BRSR Core glide-path years and value-chain timelines | Verification | Listed-company analyst | Advisory clocks (NN-38) |
| OI-P27-03 | BRSR Core attribute list and parameters as currently notified | Verification | ESG analyst | Platform list marked [VERIFY] |
| OI-P27-04 | CSR Rules values (unspent timelines, overhead cap, impact assessment thresholds, CSR committee composition) | Rule text | CS analyst | Rule pack [VERIFY]; advisory |
| OI-P27-05 | RBI Climate Finance and Management of Climate Change Risks Directions, 2025 — numbers per RE category and paragraph mapping | Catalogue verification | RBI analyst | Checkpoints from catalogue rows marked [VERIFY] |
| OI-P27-06 | CEA CO2 baseline database latest version and grid factors | Data | ESG analyst | Prior published version with label |
| OI-P27-07 | Exchange filing format for BRSR (XBRL/Excel) | Exchange specs | Integration analyst | PDF/DOCX + data workbook |
| OI-P27-08 | SSAE 3410 status and ISF assessment standards | ICAI/ISF | ESG analyst | SSAE 3000 checklist |
| OI-P27-09 | Ecosystem event for financed-emissions aggregates from Finbyx | Ecosystem Spec v1.2 change request | Integration lead | Tenant upload |
| OI-P27-10 | VA-17 Sustainability Analyst addition to Appendix AA/K with eval sets | Cross-file | AI lead | Skills off until evaluated |
| OI-P27-11 | Export folder number for Sustainability in Appendix M — **closed (v1.1, X1):** folder `27 ESG, BRSR and Sustainability` per Appendix M §M.3 | Closed | P19 owner | — |
| OI-P27-12 | Indian roadmap for ISSB-aligned standards | Policy | ESG analyst | Voluntary mapping |

---

## 15. Sources (accessed 25 October 2026)

1. Owner's baseline: LawDocs Comply Architecture Part 2 — "Environment & Social Governance" (Table 2-1 obligations, Table 3-1 applicability matrix, CSR lifecycle Table 4-1, CSR controls, ESG metric library, materiality, GHG methodology, data → disclosure → assurance lifecycle, climate risk and transition, ESG ratings and sustainable finance, forms/registers/returns, KPIs, roadmap).
2. SEBI (LODR) Regulations, 2015 Reg 34(2)(f); SEBI BRSR and BRSR Core circulars — https://www.sebi.gov.in
3. SEBI ESG disclosure changes of 28 March 2025 — summary: https://www.corporateprofessionals.com/regulatoryupdate/sebi-amends-esg-disclosure-norms-green-credits-value-chain-reporting-assurance-updates-circular-march-28-2025/ ; https://ksandk.com/newsletter/sebis-esg-green-credits-ease-doing-business/
4. Companies Act, 2013 s.135, s.198; Schedule VII; Companies (Corporate Social Responsibility Policy) Rules, 2014 as amended — https://www.mca.gov.in
5. RBI Climate Finance and Management of Climate Change Risks Directions, 2025 (consolidated set) — summary: https://uniqus.com/wp-content/uploads/2026/01/Building-Credibility-in-Green-Finance-Interpreting-RBIs-New-Directions-on-Climate-Finance.pdf ; RBI draft Disclosure Framework on Climate-related Financial Risks, 28 Feb 2024 — https://www.rbi.org.in
6. ICAI SSAE 3000 — summary: https://studycafe.in/icai-issues-standard-on-sustainability-assurance-engagements-ssae-3000-191471.html
7. GHG Protocol Corporate Accounting and Reporting Standard; Scope 2 Guidance; Corporate Value Chain (Scope 3) Standard — https://ghgprotocol.org
8. Central Electricity Authority, CO2 Baseline Database for the Indian Power Sector — https://cea.nic.in
9. IFRS S1/S2 (ISSB) — https://www.ifrs.org ; EU Omnibus I (CSRD scope) — https://www.mofo.com/resources/insights/251222-eu-sustainability-omnibus-i-detailed-omnibus
10. Appendix AC (G5 gap B) and Appendix J §J.15, §J.18.


---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**Added in v1.1:** NN-48; X-57, X-58.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
