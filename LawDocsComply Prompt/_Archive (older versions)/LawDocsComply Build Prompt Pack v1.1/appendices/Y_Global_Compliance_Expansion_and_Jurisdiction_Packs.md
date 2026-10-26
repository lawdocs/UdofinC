# Appendix Y — Global Compliance Expansion and Jurisdiction Packs *(v1.1)*

> **Status:** binding for P25 and for the global hooks in P03, P05, P15, P18, P19, P20, P21 and P24; reference for sales and partner strategy. **Prepared:** 25 October 2026 (stream G1, Build Prompt Pack v1.1). **Owner's instruction (25 Oct 2026):** "I would like to take this product to global level, therefore it should be able to support the global compliances later. For this, explore Lawrbit, how this tool is delivering its services to the companies which are situated abroad."
>
> **How to read.** §Y.2–§Y.3 reverse-engineer how Lawrbit and other cross-border vendors deliver; §Y.4–§Y.11 specify what LawDocsComply (LDC) must build so that global compliance can be switched on country by country without redesign; §Y.12–§Y.13 set the go-to-market order and risks; §Y.14 lists proposals for the master prompt. Facts about vendors come from their public pages and press (self-reported, unaudited); legal facts are marked **[VERIFY]** where only secondary sources were found. All content in this appendix is new in v1.1 *(v1.1)*.

---

## Y.1 Summary *(v1.1)*

1. **Lawrbit does not deliver abroad from software alone.** Its model is *software + a central research team in India + a network of local law and accounting firms*. Partners are engaged per project to discover applicable laws, translate non-English statutes into English, validate content, answer on-call legal queries within an agreed time, and perform compliance work (health checks, execution, assessments). Lawrbit's published case studies are an IT-consulting firm with a 10-country framework built in six months with Tier-1 and Tier-2 local firms; Maersk's Global Service Centre across India, China and the Philippines with local firms in China and the Philippines and translation of Mandarin and Filipino laws; and a hospitality group's Amsterdam hotel with a Tier-1 Dutch firm, Dutch-to-English translation and EU hosting for GDPR. Data is hosted on AWS in India and Frankfurt, with any AWS region offered for localisation. Most clients are Indian companies or foreign companies' Indian captives (Global Capability Centres) — "global" in practice means *Indian-run compliance for multi-country groups*.
2. **LDC can match this and beat it** on four points that Lawrbit's public material does not show: (a) transparent, machine-checkable **coverage statements** per country (what is and is not covered, reviewer of record, last-verified date) instead of headline counts ("70+ countries", "3,500+ / 5,000+ laws" — the counts differ between Lawrbit's own documents); (b) **clause-level citations with official-language text and translation provenance** on every checkpoint; (c) an **open partner marketplace** in which the client sees and chooses the local partner, scope, price and SLA (Lawrbit's partner layer is opaque to the client); (d) **regional data cells** chosen per legal entity, so a group can keep its EU subsidiary's personal data in the EU and its Indian entity's in India while the parent sees one aggregated dashboard.
3. **Build now, switch on later.** Every jurisdiction dimension (country, sub-national unit, special zone, authority, language, currency, time zone, holiday calendar, fiscal year, home region) is part of the data model and code from Wave 1 (P03, P15, P19); content for a country is a *pack* that is enabled only when sourced, reviewed and `PUBLISHED` (D-19; P15 FR-P15-45). Phase **P25** builds the multi-region cells, the global entity-management module, the partner network and the first corridor packs.
4. **Sequence:** (G0) privacy overlays already needed by Indian clients — EU/UK GDPR, CCPA/CPRA; (G1) Indian groups' overseas subsidiaries and IFSCA/GIFT City cross-border entities — **entity-management essentials** (annual cycle, registers, beneficial ownership, tax registrations, India ODI reporting) for the UAE, Singapore, UK, US (Delaware), Mauritius, Netherlands; (G2) **MNC subsidiaries and GCCs in India** — sell India content to foreign-headquartered groups through English-first UX, USD/EUR pricing and an EU data cell (this is where Lawrbit's references sit and is the fastest revenue); (G3) full GCC (UAE, Saudi Arabia, Qatar, Bahrain, Oman, Kuwait) and Singapore regulatory packs for financial-services groups with in-country partners; (G4) Africa corridors (Kenya, Nigeria, South Africa, Mauritius) and South Asia.
5. **Rules and decisions adopted in master v1.1** (§Y.14): new rules on jurisdiction-pack enablement with reviewer of record and coverage statements, home-region residency per legal entity (amending NN-24), official-language provenance; new decisions on regional cells, partner model and corridor order; the requirements are recorded in `02` as R-110 (take the product global) and R-111 (study Lawrbit's delivery abroad) *(v1.1 lead: renumbered)*.

---

## Y.2 How Lawrbit delivers to companies abroad — reverse-engineered *(v1.1)*

### Y.2.1 Company and products

| Item | What the public record shows (25 Oct 2026) | Source |
|---|---|---|
| Entity | Lawrbit Lextech India Private Limited (trading as Lawrbit Global Compliance Network), founded 2018; corporate office Gurgaon (Gurugram), knowledge centre Jaipur, regional office Mumbai, branch Ahmedabad; partner locations listed in Bengaluru, Chennai, Hyderabad, Pune and Tanzania; ~105–120 employees | GCMS 360 brochure; businessofgcc.com profile |
| Enterprise products | Global Compliance Management Solution (GCMS / GCMS 360), Enterprise Compliance Management (India), Legal Matter Management (LMMS: litigation, notices, arbitration, counsel, budgets), Risk & Controls Management (COSO/COBIT mapping) | Product pages; brochures |
| Practice products (for professional firms) | Compliance Service Management (CSMS) — multi-client, multi-country delivery platform for consulting and law firms with scope-of-work configuration, split tasks between firm and client, SOW-based invoicing, client expense approval; Compliance Audit Management (CAMS) for auditors | CSMS brochure; G2 profile |
| Regulatory intelligence (RI) | Claims vary by document: "70+ countries", "1,000+ regulatory bodies", "5,000+ laws" (press 2022), "3,500+ laws" (GCMS 360), "2,000+ central, state and municipal laws and 65,000+ compliance items" (home page), "100,000 obligations" (directory listing), "legal experts at 100+ law firms across 80+ countries" (G2). One RI feed serves all products; updates delivered "through an API integration without manual intervention" | Home page; brochures; press; G2 |
| RI format | Standardised input format of **62 columns across 5 sheets, obligations under 12 headers**; obligation classes one-time (~8%), recurring (~30%), event-based (~12%), ongoing (~50%); risk Extreme/High/Medium/Low from penal provisions and impact; plain-language summaries; bare acts and draft regulations attached; change history and impact assessment | GCMS 360 brochure |
| Content QA | Central legal research → two-step quality check with internal or local legal partners → validation by expert practitioners → near-real-time or periodic updates | GCMS 360 brochure |
| Hosting | AWS; hosted in India and Frankfurt; "any of 60+ AWS data centres" for localisation | GCMS page; GCMS 360 brochure |
| Clients (published) | 300+ entities and 15,000+ users claimed; named or described clients mostly Indian (VGL, Haldia Petrochemicals — replaced a Big Four solution, TTK Prestige, IndiaMART, NBFCs incl. a Middle-Layer NBFC, a credit rating agency) plus Maersk Global Service Centre (Denmark HQ; India, China, Philippines), Cvent India (three SEZ facilities), a Japanese IT provider's Indian unit, a global automotive OEM's Indian unit, a top-10 IT consultancy (10 countries) and a hospitality group (Amsterdam) | lawrbit.com/clients; businessofgcc.com |
| Pricing signal | Custom pricing; a third-party directory quotes US$2,778 for the "Global Compliance" module (unverified) | softwarefinder.com |
| Reviews | Few public reviews (2 on one directory, 4.5/5); pros: timely implementation, post-deployment support, dashboards, real-time updates, customisation; cons: login friction, more categorisation wanted, dashboard refinement, better reminders for half-yearly/annual returns, data download beyond 365 days | softwarefinder.com |
| AI | G2 listing shows generative-AI summarisation and "autonomous task execution" features (claimed) | G2 |

### Y.2.2 The delivery model, step by step (what actually happens for an overseas entity)

From the brochures and the three case studies the process for a client with entities abroad is:

1. **Business discovery** — Lawrbit's project team plus a local law firm (Tier-1 or Tier-2, chosen per country) run questionnaires and workshops per entity and location; output is a *published list of applicable laws* per entity.
2. **Translation** — non-English laws (Dutch, Mandarin, Filipino, and presumably Arabic, Spanish, Portuguese) are translated into English by or with the local firm; the English text becomes the working basis.
3. **Checklist finalisation** — obligations by location, function and act; client agrees applicability and an ownership matrix (Performer → Approver → Group Owner → CXO → Auditor; five "layers of defence").
4. **Configuration** — an AWS instance (India, Frankfurt or a client-chosen region) with responsibility matrix, reminders, escalations and auto-reports.
5. **Training and go-live** — pilot, admin and user training, handover of admin control.
6. **Sustenance** — Lawrbit's central team maintains the RI feed; local partners provide **on-call legal query support within an agreed time**, plus paid services: compliance execution, health checks, business assessments. Long-term partner engagement is sold as continuity and cost predictability.
7. **Timeline** — one public reference: 10 countries in six months.

**Inference [INTERP].** Coverage outside India is *project-built*: a country is "covered" once a client has paid for discovery there and a partner has validated it; the RI feed then reuses that content for later clients. The partner is a subcontractor to Lawrbit; the client contracts with Lawrbit. This keeps the client's procurement simple but hides who reviewed the law, when, and to what standard.

### Y.2.3 What to emulate and what to beat *(v1.1)*

| Lawrbit practice | LDC response | Where built |
|---|---|---|
| Local law firms extend coverage where Lawrbit has no presence | **Emulate**, but make the partner visible: every published pack names its *reviewer of record* and content partner, and the client can see the partner's credentials and SLA (§Y.5) | P25, P21 |
| Translation of non-English laws into English | **Emulate and improve**: keep the official-language text, the English translation and the translation provenance (official / partner / machine-reviewed) side by side at clause level; Vidhi can explain but never replaces the official text (§Y.4.4) | P03, P25, P17 |
| One RI feed for all products, API delivery | **Emulate**: LDC's content plane already serves all tenants; add a licensed-feed adapter for horizon scanning abroad (§Y.11) | P05, P25 |
| 62-column, 5-sheet input format | **Beat** with the owner's single 30-column template per family plus `_Template_Info`, now including `LDC-TPL-INTL-GEN-v1.0` for any foreign jurisdiction (§Y.4.6); simpler to author, machine-validated | Appendix E, `templates/` |
| Headline coverage counts that differ between documents | **Beat** with a live, per-country coverage statement (instruments in scope, out of scope, last verified, reviewer) published on the trust page and inside the product (NN-19) | P25 §4C |
| Hosting in India and Frankfurt, "any AWS region" | **Emulate and structure**: regional cells (India, EU, UAE/GCC, Singapore, US) with a home region per *legal entity*, not per tenant; group views by aggregation (§Y.7) | P25 §4E |
| Five-layer ownership matrix | Already exceeded by LDC's maker → checker → auditor workflow, SoD and Correction Entries (P04, NN-02, NN-05) | P04 |
| CSMS for professional firms serving many clients across countries | **Emulate** through the Service Delivery Console and Marketplace: an Indian CA/CS firm or a foreign partner can serve multiple client tenants with delivery grants (P21, P22) | P21, P22, P25 §4G |
| Long-term partner retainers for continuity | **Emulate** with marketplace retainers and SLA eSign (P21), extended to foreign partners with local-law contract templates | P21, P25 |
| Entity management not prominent | **Beat**: a global entity-management module (structure chart, registers, officers, registered agents, licences, filing calendars per country, ODI linkage) (§Y.6) | P25 §4F |
| Reviews ask for better reminders for half-yearly/annual returns and downloads beyond 365 days | Already met: frequency engine with jurisdiction calendars (P04, P25) and unlimited-period exports (P19) | P04, P19 |

---

## Y.3 Other cross-border models *(v1.1)*

### Y.3.1 Four delivery archetypes

| Archetype | Representative vendors | How they serve entities abroad | Lesson for LDC |
|---|---|---|---|
| **Entity-management platforms** | Diligent Entities; Athennian; CSC Global entity management; Blueprint OneWorld; Commenda | A system of record for legal entities, officers, ownership and registers; compliance calendars driven by jurisdiction rules; statutory forms and some e-filing. Diligent Entities lists statutory forms for 12 jurisdictions (Australia, Canada, France, Gibraltar, Hong Kong, Ireland, Jersey, Malta, Netherlands, South Africa, UK, US-Delaware) and electronic filing in the UK, US, Australia and Ireland; Athennian offers structure charts, workflow templates, AI-assisted data entry and, since 22 July 2026, a collaboration with PwC UK on AI-powered global subsidiary governance | Entity data and the annual company-law cycle are the **entry point** for global groups; e-filing is a premium feature limited to registries with APIs (§Y.6) |
| **Service-led networks with portals** | TMF Group (local experts in 87 jurisdictions, 125+ offices); Vistra; CSC | Directors, company secretaries, registered office, filings, bookkeeping, payroll and tax delivered by own offices or partners, with a client portal | Clients abroad buy *outcomes*; LDC's marketplace and delivery console must let a local partner deliver inside the client's LDC tenant (§Y.5) |
| **Regulatory-intelligence content houses** | Thomson Reuters Regulatory Intelligence; Wolters Kluwer; LexisNexis Regulatory Compliance; OneTrust DataGuidance (privacy laws across a large number of jurisdictions); CUBE (AI-driven "RegPlatform", third generation); Regology; Corlytics; Ascent | Horizon scanning, rule libraries and obligation mapping, often AI-assisted, licensed as data feeds or platforms | LDC should **license**, not build, horizon scanning outside its corridor packs, and map licensed items into its own change workflow without republishing licensed text (§Y.11) |
| **Indian compliance trackers** | TeamLease RegTech (India only: 28 States and 8 UTs, 1,536+ acts, 69,233+ compliances, 3,700+ government websites monitored); Lexplosion Komrisk (claims clients in 30+ countries); Lawrbit | Deep India content; global reach through partners or MNC captives in India | LDC's first global revenue is **MNC subsidiaries and GCCs in India**, served in English with foreign-currency pricing and an EU data cell (§Y.12) |

### Y.3.2 Feature patterns observed across cross-border vendors

1. **Jurisdiction-rule calendars** — due dates generated from entity jurisdiction + incorporation date + financial year + filing rules (Diligent, Athennian).
2. **Structure charts with ownership percentages** and drill-down to entity records (Athennian, Diligent).
3. **Statutory register generation** per jurisdiction (UK PSC register, Singapore Register of Registrable Controllers, beneficial-owner registers in the UAE).
4. **E-filing** only where registries expose APIs (UK Companies House, some US states, Australia, Ireland) — elsewhere, prepared filing packs for partners.
5. **Service catalogues by country** with fixed prices for annual compliance (service-led vendors).
6. **Translation and bilingual records** (Lawrbit case studies; TMF board support with translations).
7. **AI over entity data** — Q&A on governance obligations, extraction of entity data from documents during onboarding and M&A (Athennian).
8. **Data residency choices** — region selection at contract (Lawrbit; most enterprise vendors).

---

## Y.4 Jurisdiction-pack architecture *(v1.1)*

### Y.4.1 Target segments and what each needs

| Segment | Typical customer | What they need first | Packs and modules |
|---|---|---|---|
| S1 Indian groups with overseas subsidiaries | Indian NBFC group with a Dubai or Singapore investment company; Indian manufacturer with UK/US/Netherlands sales subsidiaries; IT services group with 10–40 foreign entities | One group view of every entity's company-law cycle, tax registrations, licences, directors and beneficial ownership; India-side ODI reporting tied to each subsidiary | Global entity management (§Y.6), INTL-GEN corridor packs (company law, tax, payroll registration), India FEMA/ODI overlay |
| S2 MNC subsidiaries and GCCs in India | Foreign-headquartered bank's Indian NBFC; US software company's Indian GCC in an SEZ; Japanese manufacturer's Indian plant | India statutory, labour, data and sector content in English; head-office reporting; group SSO; data held outside India for head-office users only as aggregates | Existing India families + `OV_*` overlays; EU/US data cell for group users' metadata; USD/EUR/JPY pricing |
| S3 IFSCA / GIFT City cross-border entities | IBUs, FCs/FUs, fund management entities, aircraft and ship lessors with foreign parents and foreign customers | IFSCA content (existing) plus home-country parent obligations and foreign-customer data rules | IFSCA families + INTL-GEN parent-jurisdiction rows + GDPR/UK GDPR overlays |
| S4 GCC financial-services groups | UAE/Saudi finance companies, DIFC/ADGM fund managers, Indian banks' GCC branches | Regulator-specific content (CBUAE, DFSA, FSRA, SAMA, CMA), AML, data protection (PDPL, DIFC, ADGM), Arabic UI | Full jurisdiction packs with in-country partners (G3), UAE/GCC data cell, RTL |
| S5 Singapore and ASEAN hubs | Singapore holding companies, MAS-licensed entities | ACRA cycle, MAS notices, PDPA, Arabic not needed; English UI | Singapore pack, Singapore cell (or EU/India with consent) |
| S6 Africa and South Asia corridors | Indian lenders and fintechs in Kenya, Nigeria, Mauritius, Sri Lanka, Bangladesh, Nepal | Entity cycle, central-bank licensing conditions, data protection (Kenya DPA 2019, Nigeria NDPA 2023, Mauritius DPA 2017) | INTL-GEN corridor packs with partners (G4) |

### Y.4.2 Data model *(v1.1)*

The v1.0 content model (master §6.1; P15 §4J) already carries `pack.jurisdiction`. v1.1 makes the jurisdiction hierarchy explicit and binding for every content and calendar record:

```
jurisdiction (ISO 3166-1 alpha-2, e.g. AE)          — country or supranational union (EU)
 └─ subdivision (ISO 3166-2, e.g. US-DE, CA-ON, IN-MH) — state / province / emirate where law is sub-national
     └─ special_zone (LDC code, e.g. AE-DIFC, AE-ADGM, QA-QFC, IN-IFSC) — zone with its own legal system
         └─ authority (regulator, registry, legislature, tax authority, court)
             └─ instrument (Act, regulation, rule, notice, circular, guideline, standard, FAQ)
                 └─ instrument_version (issue date, effective date, official language(s), source file + hash, translation set)
                     └─ clause (official-language text, English text, translation provenance, hashes)
                         └─ checkpoint (one actionable; Excel row; obligation_ref "<ISO>/<AUTH>/<INSTR>/<VER>#<clause>")
                             └─ control_activity, evidence_expectation, applicability_rule
```

**Binding rules.**

- `obligation_ref` for foreign content is prefixed with the jurisdiction code (`GB/CH/CA2006/2026-04#853A`, `AE-DIFC/DIFC/DPL2020/2025-07#27`); Indian refs keep the v1.0 format and are read as `IN/…` *(v1.1)*.
- Every legal entity record carries `jurisdiction`, `subdivision`, `special_zone`, `entity_form` (local form, e.g. *private company limited by shares*, *FZ-LLC*, *GmbH*), `local_registration_no`, `registry`, `incorporation_date`, `financial_year_end`, `functional_currency`, `reporting_currency`, `time_zone`, `working_week` (e.g. Monday–Friday; Saudi Arabia Sunday–Thursday until changes [VERIFY]), `holiday_calendar_id`, `languages[]` and `home_region` (§Y.7).
- Entity forms map to LDC families through `pack.entity_form_map` (country × local form → LDC family/type) so that applicability rules can be written once per concept (for example "every company limited by shares files an annual return") and specialised per jurisdiction.
- Calendars use the entity's time zone and holiday calendar; statutory deadlines that fall on a non-working day move only where the local law says so (rule-pack attribute `weekend_rule`: `NONE`, `NEXT_BUSINESS_DAY`, `PREVIOUS_BUSINESS_DAY`) (NN-33).
- Money values carry ISO 4217 currency; penalties are stored in local currency with an optional reporting-currency conversion snapshot (rate, source, timestamp).

### Y.4.3 Pack types and tiers *(v1.1)*

| Pack tier | Content | Who it suits | Gate |
|---|---|---|---|
| **Tier C — Entity essentials** | Company-law annual cycle (annual return / confirmation statement, accounts filing, AGM or written resolution, registers, beneficial ownership), tax registrations and periodic returns (corporate tax, VAT/GST, withholding), payroll/social security registration, data-protection registration where required, licence renewals | S1, S6: subsidiaries that need a reliable calendar | Partner-reviewed calendar and checkpoints; coverage statement lists excluded areas |
| **Tier B — Corporate core** | Tier C + employment law core, data protection full, AML for designated businesses, consumer law basics, ESG/climate disclosure where mandatory | S1, S2, S5 | Reviewer of record; quarterly freshness review |
| **Tier A — Regulated sector** | Tier B + financial regulator rulebooks for a licence type (bank, finance company, fund manager, insurer, payment institution) | S3, S4 | In-country regulatory specialist reviewer; monthly freshness review; licensed horizon feed connected |
| **Overlay packs** | Cross-border laws that attach to Indian entities: EU GDPR, UK GDPR, CCPA/CPRA, EU AI Act, DORA (for ICT providers to EU financial entities), US OFAC sanctions screening obligations | All segments | Reviewer of record; scope test recorded per tenant (e.g., GDPR Art. 3(2) targeting test) |

### Y.4.4 Language and translation handling *(v1.1)*

1. **Official text is the law.** Each clause stores the official-language text exactly as published (with the source hash) and, where the official language is not English, an English translation with `translation_provenance` ∈ {`OFFICIAL` (published by the government), `PARTNER` (translated by the reviewing firm), `MACHINE_REVIEWED` (machine translation reviewed by a qualified bilingual reviewer), `MACHINE_UNREVIEWED` (allowed only in DRAFT; blocks publication)} *(v1.1)*.
2. **Display.** Checkpoints show the English text by default with a toggle to the official text; exports carry both (P19). Where both are official (e.g., Arabic and English in some UAE federal instruments, or bilingual Hong Kong ordinances), the pack records which version prevails in case of conflict.
3. **UI language is separate from law language.** The product UI may be in Arabic, Hindi or another locale; legal text remains in the official language plus English. Vidhi can explain a clause in the user's locale, labelled as an explanation (NN-06, NN-14).
4. **Right-to-left.** Arabic UI uses logical CSS properties, mirrored navigation and icons with direction, bidirectional isolation for mixed Arabic/Latin strings (company names, citations), Eastern Arabic numerals as a locale option (default Western digits in financial tables) [REC] (§Y.9).

### Y.4.5 Coverage statement, freshness and quality metrics *(v1.1)*

Every published pack carries a machine-readable **coverage statement** (`pack.coverage_statement`, JSON + rendered page):

| Field | Meaning |
|---|---|
| `in_scope` | Instruments and areas covered, with counts of checkpoints per area |
| `out_of_scope` | Areas deliberately excluded (e.g., "municipal licences", "industry-specific environmental permits") |
| `entity_forms` | Local forms covered |
| `reviewer_of_record` | Firm, lead reviewer, qualification, licence/bar number where public, review date |
| `last_verified_at` | Date the pack was last checked against official sources |
| `freshness_sla` | Tier A monthly; Tier B quarterly; Tier C half-yearly, plus event-driven updates within 10 business days of a material change [REC] |
| `monitoring` | Official feeds and licensed feeds connected; last successful scan |
| `languages` | Official languages handled; translation provenance mix |
| `known_gaps` | Open items and [VERIFY] markers, with due dates |

**Quality metrics** shown to the platform content team and summarised to tenants: citation completeness (100% required), clause hash match rate on re-scan, overdue reviews, time from official publication to LDC Update (median and p90), client-reported content defects per 1,000 checkpoints, partner response time to on-call queries.

A pack whose monitoring is stale for more than 30 days moves to `SUSPENDED` with a tenant-visible banner (P15 §5.6).

### Y.4.6 Content production — the INTL-GEN template *(v1.1)*

Foreign content is authored in the owner's 30-column format using `templates/LDC-TPL-INTL-GEN-v1.0 - International Jurisdictions.xlsx` and `part2_prompts/25_INTL-GEN_Command.md`:

- Column C = **Jurisdiction** (52 values: GCC including DIFC/ADGM/QFC, Singapore, Hong Kong, ASEAN, Japan, Korea, China, Australia/New Zealand, South Asia, Mauritius, Kenya, Nigeria, South Africa, Egypt, UK, Ireland, major EU states, EU supranational, US federal and key states, Canada federal/Ontario, Mexico, Brazil, "Other jurisdiction", "All jurisdictions (ALL)").
- Column D = **Entity form** (21 generic forms including "Subsidiary of an Indian parent (ODI)" and "Group parent (consolidated obligations)").
- Column M adds Secretarial, Tax, Privacy Office (DPO), Information Security, KYC & AML and Payroll — all already in the department alias map (Appendix U §U.9.0; X-10).
- Column P filing tokens are generic authority classes (company registry, tax authority corporate/indirect, financial regulator, securities regulator, data protection authority, labour/social security, beneficial-ownership register, FIU, foreign-investment reporting, registered agent, local auditor, India ODI parent reporting, board, not required).
- Column N must carry `REVIEWER: <firm>, <city>, <date>` and, where relevant, `TRANSLATION: <provenance>` and `INDIA-LINK: <template code> / <instrument>`; the importer (P03) treats a missing reviewer line on an INTL-GEN sheet as a blocking error for publication (new error code proposed `LDC-TPL-041`) *(v1.1)*.
- Validation: the template passes all 11 checks of `templates/_validate_templates.py` (report regenerated 25 Oct 2026).

Once a corridor grows beyond Tier C, a dedicated country template (e.g., `LDC-TPL-AE-FIN`, `LDC-TPL-SG-MAS`) is created by the same build mechanism with country-specific Column C/D lists; INTL-GEN remains the generic family.

### Y.4.7 Pack lifecycle *(v1.1)*

The P15 §5.6 lifecycle is canonical. v1.1 inserts a **PILOT** state between `APPROVED` and `PUBLISHED`:

`PROPOSED → SOURCE_REGISTER_BUILT → CONTENT_AUTHORED → IN_COUNTRY_REVIEW → APPROVED → PILOT → PUBLISHED → MAINTAINED → SUSPENDED → WITHDRAWN`

- `PILOT`: enabled only for named pilot tenants who accept a pilot notice; feedback and defects tracked; minimum 60 days or one full filing cycle for Tier C items, whichever is shorter [REC].
- `PUBLISHED`: available to all tenants in the catalogue with coverage statement; enablement gate of P15 FR-P15-45 applies.
- `WITHDRAWN`: the pack stops generating new instances; completed history is preserved (NN-29).

### Y.4.8 Starter content for the G1 corridors (Tier C) *(v1.1)*

The table lists the checkpoint areas each Tier C corridor pack must contain at `PILOT`. Instrument names are given so that content partners can build source registers; every item is **[VERIFY]** against the official source by the reviewer of record before publication.

| Corridor | Company-law cycle | Beneficial ownership / registers | Tax and payroll registrations and returns | Other Tier C items |
|---|---|---|---|---|
| **UAE — mainland** | Federal Decree-Law No. 32 of 2021 on Commercial Companies: general assembly within the period after FYE set by the law, audited accounts, licence renewal with the relevant emirate's economic department, register updates | Cabinet Decision No. 109 of 2023 (real beneficiary procedures): register of beneficial owners and partners/shareholders, filing with the registrar, updates within the prescribed period | Corporate tax (Federal Decree-Law No. 47 of 2022): registration, return within 9 months of FYE; VAT (5%) registration and periodic returns; payroll via Wage Protection System for mainland employers | Trade licence renewal; economic substance regime (repealed for later periods — confirm status); ultimate parent entity notification where applicable |
| **UAE — DIFC** | DIFC Companies Law (Law No. 5 of 2018): annual return/confirmation, accounts filing, registers | DIFC Ultimate Beneficial Ownership Regulations | As mainland for federal taxes; DIFC Employment Law and DEWS (employee workplace savings) contributions | DIFC Data Protection Law 2020 (amended 2025): DPO, registration/notification with the Commissioner, annual assessment where required |
| **UAE — ADGM** | ADGM Companies Regulations 2020: annual return, accounts, registers | ADGM Beneficial Ownership and Control Regulations | Federal taxes; ADGM Employment Regulations | ADGM Data Protection Regulations 2021: registration, DPO where required |
| **Singapore** | Companies Act 1967: AGM (or dispensation), annual return to ACRA (s.197) within the period after FYE, financial statements, registers of members/directors/secretaries | Register of Registrable Controllers (Part 11A) and filing with ACRA; register of nominee directors | IRAS: Estimated Chargeable Income, Form C/C-S; GST registration where threshold met; CPF contributions for employees; IR8A/AIS | PDPA 2012: DPO appointment and business contact information, data-breach notification; licences by sector |
| **United Kingdom** | Companies Act 2006: confirmation statement (s.853A), accounts filing (s.441–442; 9 months after FYE for private companies), registers, AGM where articles require (public companies) | PSC register (Part 21A) and Companies House updates; identity verification under the Economic Crime and Corporate Transparency Act 2023 (phased) | HMRC: corporation tax return (CT600) within 12 months, payment generally 9 months and 1 day after period end; VAT registration if threshold met; PAYE RTI | UK GDPR: ICO data protection fee; Modern Slavery statement where turnover threshold met; gender pay gap for ≥ 250 employees |
| **United States — Delaware (plus federal)** | Delaware General Corporation Law: annual franchise tax report and tax (corporations, by 1 March), registered agent maintenance; LLC annual tax (1 June) | Corporate Transparency Act BOI reporting — scope narrowed by FinCEN interim final rule (2025) to foreign reporting companies [VERIFY] | IRS: Form 1120 (with 5472 for foreign-owned), state income and franchise taxes, payroll (941/940), state registrations where nexus | State privacy laws by consumer footprint; foreign-qualification in states of business |
| **Mauritius** | Companies Act 2001: annual return, financial statements to the Registrar; Global Business Companies under FSC licensing | Beneficial ownership disclosure to the Registrar | MRA: corporate income tax return, VAT where registered | FSC licence conditions and annual fees for GBC licensees; substance requirements for GBCs |
| **Netherlands** | Dutch Civil Code Book 2: annual accounts adoption and filing with the Chamber of Commerce (KVK) within the statutory period | UBO register at KVK | Corporate income tax (Vpb), VAT (BTW) returns, payroll tax (loonheffingen) | GDPR (AP as supervisor); works council thresholds |

India-side items attached to every foreign subsidiary of an Indian parent (written in the Indian families and linked via `INDIA-LINK`): Annual Performance Report under the overseas investment framework, FLA return, disclosure of step-down subsidiaries, approvals for financial-services ODI by regulated entities (for example RBI approval conditions for NBFC overseas investment), consolidation under Ind AS 110 or AS 21, related-party approvals in the parent (P06).

### Y.4.9 Worked journey — onboarding a foreign subsidiary in 20 minutes *(v1.1)*

1. **Group admin opens Organisation › Entities › Add entity** and chooses *Foreign entity*. Enters country (UK) and registration number; the UK registry adapter fetches name, registered office, officers, PSCs, SIC codes and filing history (licensed API); Vidhi proposes the local form (*private company limited by shares*) and FYE from the last accounts.
2. **Ownership** — admin links the parent (Indian holding company, 100%) on the structure chart; the system asks whether the ODI was under the automatic route and records the UIN/approval reference [VERIFY field names].
3. **Home region** — default EU cell for a UK entity (or IN if the client chooses and records the basis); the transfer register entry is created automatically.
4. **Packs** — the applicability engine proposes `GB` Tier C pack (company law, PSC, HMRC registrations, ICO fee) and the UK GDPR overlay; shows the coverage statement and reviewer of record; admin enables.
5. **Owners** — the system proposes owners from the person master (UK finance manager; group CS as checker) and a delivery partner (UK corporate secretarial firm from the marketplace) for filings; client approves the delivery grant (NN-43).
6. **Calendar** — 12 months of instances are generated in Europe/London time with UK bank holidays; group dashboard shows the entity next to Indian entities with consistent statuses.
7. **India link** — APR and FLA checkpoints in the parent's Indian pack are linked to the new entity and pre-filled with entity data each year.

---

## Y.5 Partner network operating model *(v1.1)*

### Y.5.1 Partner roles

| Role | What the partner does | Contract with | Shown to client as |
|---|---|---|---|
| **Content partner** | Builds and maintains a jurisdiction pack: source register, checkpoints in INTL-GEN or country template, translations, change notes | LawDocs (content licence or service agreement) | "Content prepared with <firm>" on the coverage statement |
| **Reviewer of record** | Independent legal review and sign-off of a pack version (may be the content partner's senior lawyer or a separate firm for Tier A) | LawDocs | Named on every pack version |
| **Delivery partner** | Performs compliance work for clients: filings, registered agent, company secretary, payroll, tax returns, health checks, on-call queries | **The client directly** (Model M2 of Appendix O) or LawDocs as reseller where lawful in that country and profession | Marketplace listing with credentials, scope, price, SLA, ratings where allowed (NN-20) |
| **Implementation partner** | Business discovery workshops, applicability mapping, data migration, training for multi-country roll-outs | LawDocs or client | Named on the implementation plan |
| **Referral partner** | Introduces clients | LawDocs (referral agreement) | Not shown; referral rewards subject to professional rules (D-06) |
| **Licensed feed provider** | Horizon scanning / regulatory intelligence data | LawDocs (licence) | "Source: <provider>" on Radar items; never republished in full (§Y.11) |

### Y.5.2 Onboarding and quality

1. **Due diligence:** registration and licence/bar standing in the jurisdiction; professional indemnity insurance with minimum cover by tier [OWNER TO SET]; conflicts policy; sanctions and adverse-media screening of the firm and principals; information-security questionnaire (the firm will see client data) and DPA/sub-processor terms; references.
2. **Agreement set:** framework agreement (services, confidentiality, IP in content — LawDocs owns compiled packs, the firm keeps its pre-existing know-how), DPA with standard contractual clauses where personal data crosses borders (§Y.8), SLA schedule, anti-bribery and sanctions clauses, professional-rules compliance warranty, exit and content hand-over.
3. **Scorecard (quarterly):** content defect rate, review turnaround, on-call response time (target first response within 1 business day, full answer within 3 [REC]), client satisfaction, filing timeliness for delivery work, data-security incidents (zero tolerance).
4. **Conflict checks:** reuse the Hub conflicts API (Appendix X §X.12; `POST /v1/conflicts/check`) extended with jurisdiction and opposing-party checks before a delivery partner accepts an engagement.
5. **Tiering:** Gold / Silver / Registered partners by scorecard; marketplace ranking uses objective service metrics only and never paid placement for restricted professions (NN-20).

### Y.5.3 On-call query desk *(v1.1)*

Clients on Tier A/B packs (or a "query bundle" add-on) can raise a jurisdiction question from any checkpoint ("Ask a local expert"). The query is routed to the reviewer-of-record firm (or a marketplace partner chosen by the client) with the checkpoint, clause and entity context, under the client's delivery grant; SLA clock starts at submission; the answer is stored against the checkpoint as an **expert note** (tenant-private) and may be proposed to the content team as a pack improvement with the client's permission. Vidhi drafts the question and summarises the answer but never answers on behalf of the firm (NN-14).

### Y.5.4 Commercial models per country (subject to counsel) *(v1.1)*

Professional-conduct rules on fee sharing, referral fees and advertising differ by country and profession; many bar associations prohibit sharing legal fees with non-lawyers, while accountancy and corporate-service providers are often freer [INTERP; counsel to confirm per country]. LDC therefore supports, per country × profession × service type (extending D-06):

- **Listing / subscription fee** paid by the partner (default where fee sharing is restricted);
- **Disclosed platform fee** paid by the client on top of the partner's price (client contracts with the partner);
- **Resale** (LawDocs or a local LawDocs entity contracts with the client and subcontracts the partner) — only where lawful and where LawDocs holds any licence the service needs (for example corporate service provider licences in some jurisdictions [VERIFY per country]);
- **Content licence fee** paid by LawDocs to content partners (fixed per pack version + maintenance retainer);
- **Revenue share on pack subscriptions** to content partners where lawful.

All switches default OFF until counsel records an opinion reference per country (NN-20, extended in §Y.14).

---
## Y.6 Global entity management *(v1.1)*

### Y.6.1 Scope

A group-level module (`gem` sub-context within `gov`; P25 §4F) that becomes the system of record for every legal entity in a client group, wherever incorporated, and feeds jurisdiction calendars, governance (P06), risk (P08) and exports (P19).

| Capability | Detail |
|---|---|
| **Group structure chart** | Interactive chart of ownership (direct and indirect percentages, share classes, voting vs economic interest), control relationships, branches and representative offices; as-at date slider (bitemporal, NN-07); export as PDF/PNG and as an Excel ownership table; highlight entities by jurisdiction, risk rating, overdue filings |
| **Entity record** | Legal name (local script and English), former names, local form, registration numbers (company, tax, VAT/GST, LEI, social security), registry, registered office and registered agent, principal place of business, incorporation and FYE dates, functional and reporting currency, share capital, auditors, banks (masked), licences, home region, status (active, dormant, in liquidation, struck off) |
| **Officers and signatories** | Directors, secretaries, legal representatives, authorised signatories, managers, nominee directors (flagged), with appointment/cessation dates, residency, identity verification status (e.g., UK identity verification [VERIFY commencement]), conflicts, other directorships across the group (one person record across entities; P13 person master) |
| **Registers** | Jurisdiction-specific registers generated from the record: members/shareholders, directors, secretaries, charges, beneficial owners / persons with significant control / registrable controllers, nominee registers; register entries are append-only (NN-36 pattern) |
| **Filing calendars** | Generated per entity from the jurisdiction pack: annual return/confirmation statement, accounts filing, AGM/written resolutions, tax returns, VAT/GST returns, payroll filings, beneficial-ownership updates, licence renewals, economic-substance or transfer-pricing documentation where in force [VERIFY per jurisdiction] |
| **Registered agent and service providers** | Agent name, contract, fees, renewal, contact, scope; link to marketplace delivery partner and delivery grant |
| **Licences and permits** | Licence type, issuing authority, conditions, renewal date, fees, linked checkpoints |
| **Intercompany** | Intercompany agreements (services, loans, guarantees, IP), transfer-pricing documentation status, related-party flags feeding P06 RPT approvals of the Indian parent |
| **India linkage (ODI / FDI)** | For overseas subsidiaries of an Indian parent: ODI route, approval references, Annual Performance Report status per year, Foreign Liabilities and Assets (FLA) return status, step-down subsidiary disclosures; for Indian subsidiaries of foreign parents: FDI reporting (FC-GPR, FC-TRS), downstream investment, FLA [VERIFY current form names and due dates under FEMA (Overseas Investment) Rules 2022 and FEMA (Non-debt Instruments) Rules 2019] |
| **Documents** | Constitutional documents, certificates, minute books and resolutions per entity with language and translation metadata (P07) |
| **AI assistance** | Vidhi extracts entity data from certificates, registry extracts and annual returns (any language) into draft records for human confirmation; answers "which entities have filings due next month?" from structured data (NN-14, NN-37) |

### Y.6.2 Data sources and e-filing

- **Registry data:** licensed APIs where available (for example UK Companies House public data API; Singapore ACRA data via licensed providers; OpenCorporates or similar aggregators under licence) through `COMPANY_DATA_PORT` country adapters (P18); manual upload of registry extracts elsewhere [VERIFY each API's terms before use].
- **E-filing:** v1.1 prepares filing packs (forms pre-filled from the entity record, checklists, signing via eSign or local e-signature where valid) for the delivery partner or client to submit; direct e-filing adapters only where an official API exists and the client authorises it (NN-08 applies globally) *(v1.1)*.
- **Local e-signatures:** EU eIDAS qualified/advanced signatures, UAE Pass, Singapore Sign with Singpass and similar are added as `ESIGN_PORT` adapters per corridor only after verification of legal effect for the document type [VERIFY].

### Y.6.3 Group dashboards and governance across countries *(v1.1)*

- **Group compliance map** — world map and table by entity: on-time rate, overdue items, upcoming 30/60/90-day filings, high-risk open items, pack coverage tier, reviewer freshness; drill-down routes to the entity's home cell.
- **Board and audit committee pack (group)** — quarterly report across entities: status by jurisdiction, exceptions, regulatory changes affecting subsidiaries, licence renewals, director changes, litigation flags (from P06/P08 data), generated in the parent's language with entity-local annexes.
- **Subsidiary governance** — board calendar per entity (local AGM/written-resolution rules), director attendance and residency tests (e.g., local-director requirements where a jurisdiction imposes them [VERIFY]), resolution templates per jurisdiction drafted by Vidhi from the pack's templates and reviewed by the local partner.
- **Policies cascade** — group policies (code of conduct, AML, data protection, anti-bribery) published from the parent with local addenda per jurisdiction; attestations tracked per entity (P07).
- **Escalation** — overdue foreign items escalate along the group reporting line (entity owner → regional head → group CCO) with time-zone-aware timers.

---

## Y.7 Multi-region deployment *(v1.1)*

### Y.7.1 Regional cells

| Cell | AWS region (primary / DR) [VERIFY service availability] | Serves | Status |
|---|---|---|---|
| **IN** (primary, existing) | ap-south-1 Mumbai / ap-south-2 Hyderabad | Indian entities; default for all tenants | Wave 1 |
| **EU** | eu-central-1 Frankfurt / eu-west-1 Ireland (or eu-central-2 Zurich for Swiss data) | EU/UK entities; MNC head-office users needing EU residency; GDPR-sensitive data | P25 |
| **GCC** | me-central-1 UAE / me-south-1 Bahrain | UAE (mainland, DIFC, ADGM), Bahrain, Oman, Qatar entities; Saudi entities pending local-region decision (Saudi draft localisation proposal, §Y.8) | P25 (after G3 demand) |
| **SG** | ap-southeast-1 Singapore / ap-southeast-3 Jakarta or ap-southeast-5 Malaysia [VERIFY] | Singapore and ASEAN entities | P25 (on demand) |
| **US** | us-east-1 / us-west-2 | US entities with US-residency requirements | Later, on demand |

**Architecture.** Each cell is a full deployment of the tenant plane (database, object storage with Object Lock, search, Temporal workers, AI routing, backups) with its own KMS keys; cells never share tenant databases. A thin **global control plane** holds only: tenant directory (tenant id, legal entities and their home regions, routing), identity federation metadata (no passwords or personal profile beyond login identifiers needed for routing — the identity provider itself runs per cell with a global discovery service [REC]), platform content plane (regulatory content contains no personal data and is replicated read-only to every cell), billing references (OH8), and release orchestration. *(v1.1)*

### Y.7.2 Home region per legal entity

- Every legal entity has a `home_region` chosen at onboarding (default from jurisdiction: India → IN; EU/EEA/UK → EU; UAE/Bahrain/Oman/Qatar → GCC; Singapore → SG; others → IN unless local law or client policy requires otherwise). Changing it is a Governed migration with evidence pack (P19 FR-P19-30 pattern) and tenant approval.
- A tenant (group) may have entities in several cells. Records are stored in the entity's home cell; group-level records (group policies, group risk appetite) live in the **group home cell** chosen by the client.
- **Cross-cell group views** are built from **aggregates and metadata only** (counts, statuses, due dates, risk scores, KPI values, document titles without content), published by each cell through an internal aggregation API; personal data and document content stay in the home cell. A group user who opens an entity's detail is routed to that cell and accesses it under that cell's rules (audit logged in the home cell). Where a client wants full cross-cell replication, a recorded transfer basis per §Y.8 is required and the transfer register is updated *(v1.1)*.
- **AI routing per cell:** Vidhi uses an in-region model route for each cell (for example Bedrock in the EU for EU cell data) and never routes a cell's regulated data out of its permitted regions (extends NN-41) [VERIFY model availability per region].
- **Exports** are produced in the home cell and delivered to the client's chosen storage target; a group export is a set of per-cell packages plus a group index (P19; Appendix M).

### Y.7.3 What changes in the v1.0 rules

NN-24 ("India residency for tenant data") was written for an India-only product. v1.1 proposes to restate it as **home-region residency**: tenant data of a legal entity is stored and processed in that entity's home cell; Indian entities' home cell is IN (ap-south-1/2) and cannot be changed without a recorded legal basis and the client's written instruction; cross-cell processing only with a recorded basis (§Y.14 proposal NN-24).

---

## Y.8 Data-transfer controls by law *(v1.1)*

### Y.8.1 Legal position (as researched 25 Oct 2026; counsel to confirm before each cell goes live)

| Law | Transfer rule relevant to a multi-region SaaS | Platform control |
|---|---|---|
| **India — DPDP Act 2023 s.16; DPDP Rules 2025** | Transfers outside India are permitted except to countries the Central Government restricts by notification ("negative list"); no country notified as of March 2026 (secondary source); sectoral rules prevail where stricter — e.g., RBI requirement that payment-system data be stored only in India [VERIFY current RBI storage directions]; regulators' outsourcing directions require RE control and supervisory access to data held by service providers | Indian entities' home cell fixed to IN; cross-border copy only for non-personal aggregates unless a recorded basis exists; negative-list watcher in P05 (Updates trigger a transfer review) |
| **EU — GDPR Chapter V** | Transfers to third countries need adequacy (India has no adequacy decision [VERIFY]), appropriate safeguards (Standard Contractual Clauses, Commission Implementing Decision (EU) 2021/914, plus transfer impact assessment) or derogations | EU cell keeps EU entities' personal data in the EU; LawDocs signs SCCs with EU clients for any access from India (support, delivery staff); TIA template in P12 |
| **UK — UK GDPR** | UK adequacy regulations, International Data Transfer Agreement (IDTA) or the UK Addendum to EU SCCs | Same as EU; UK addendum in DPA set |
| **UAE federal — PDPL (Federal Decree-Law No. 45 of 2021)** | In force since January 2022 but Executive Regulations still unpublished as of February 2026; no adequacy list or SCCs issued; transfers rely on contractual safeguards, consent or statutory derogations; commentary indicates full compliance expected by 1 January 2027 [VERIFY] | GCC cell for UAE mainland entities; contractual safeguards in DPA; status watcher for Executive Regulations |
| **UAE — DIFC Data Protection Law No. 5 of 2020 (amended by Law No. 1 of 2025, effective 15 July 2025)** | Adequacy list, DIFC SCCs, BCRs; since July 2025 a documented assessment of the recipient jurisdiction is required even with SCCs | DIFC entities in GCC cell; DIFC SCCs and assessment record in transfer register |
| **UAE — ADGM Data Protection Regulations 2021** | GDPR-like; recognises EU-adequate jurisdictions and DIFC; ADGM SCCs or ADGM addendum to EU SCCs; BCRs | ADGM entities in GCC cell; ADGM addendum |
| **Saudi Arabia — PDPL and Transfer Regulations** | Transfers permitted subject to the PDPL and Transfer Regulations (risk-assessment guidelines 2025); SDAIA draft amendments (consultation 6 Oct–5 Nov 2026) propose that controllers keep personal data stored in the Kingdom and that controllers transferring abroad register with the National Register of Controllers [VERIFY final text] | Saudi entities not onboarded to a non-Saudi cell for personal data until the amendments are settled; Tier C entity-calendar data (non-personal) allowed; decision gate in P25 |
| **Singapore — PDPA s.26 and Transfer Limitation Obligation (PDP Regulations 2021)** | Transfers allowed where the recipient is bound by legally enforceable obligations of comparable protection (contracts, BCRs, certifications) | SG cell optional; contractual clauses in DPA |
| **United States** | No general transfer restriction in most state privacy laws; federal rule on access to Americans' bulk sensitive personal data by countries of concern (DOJ, effective 2025) restricts transfers to listed countries — India is not a listed country [VERIFY] | US entities default to IN or EU cell unless client requires US cell |
| **China — PIPL** | Cross-border transfers need a CAC security assessment, standard contract filing or certification, with thresholds and exemptions | China entities: Tier C non-personal entity calendar only until a China decision is taken [REC] |

### Y.8.2 Platform controls *(v1.1)*

1. **Transfer register** (`dpc.transfer_register`, extends P12): every flow between cells, to sub-processors and to delivery partners, with legal basis, safeguard document, TIA reference, data classes, review date.
2. **Data-class routing:** each record carries a data class (Appendix Q) and the cell enforces which classes may leave it (default: none except platform metadata and aggregates).
3. **Support and delivery access across borders:** staff in India accessing an EU cell entity's data do so via break-glass or delivery grants (NN-30, NN-43) logged in the EU cell; the access is covered by SCCs in the client DPA.
4. **Sub-processors per cell:** the sub-processor list (Appendix Q) is maintained per cell; clients subscribe to change notices for their cells.
5. **Negative-list and adequacy watchers:** P05 monitors MeitY (s.16 notifications), the European Commission (adequacy decisions), UK DSIT, UAE Data Office, SDAIA, PDPC; any change raises an Update and a transfer-review task.

---
## Y.9 Currencies, time, calendars and localisation *(v1.1)*

### Y.9.1 Currency

- All money fields: `NUMERIC` amount + ISO 4217 code (NN-22). Entities have a functional currency; groups have a reporting currency; conversion uses a rate snapshot (source, date, rate type: spot, monthly average, closing) stored with each converted value; rate sources configurable (central bank reference rates such as RBI reference rate, ECB euro foreign exchange reference rates, CBUAE rates) via `FX_RATE_PORT` [REC].
- Penalty exposure and savings dashboards (P20) show local currency first, reporting currency second.
- Pricing and invoices are in the currency of the commercial contract (INR, USD, EUR, GBP, AED, SGD), priced by OH8 (X-02).

### Y.9.2 Time zones, working weeks, holidays, fiscal years

- Each entity has an IANA time zone (e.g., `Asia/Kolkata`, `Asia/Dubai`, `Europe/London`); deadlines are computed and displayed in the entity's zone with the user's zone shown on hover; reminders fire at entity-local business hours.
- Holiday calendars per jurisdiction/subdivision (national and state holidays, bank holidays, Islamic holidays whose dates depend on moon sighting are entered as provisional and confirmed when announced [REC]) are rule-pack data maintained by content partners.
- Working-week patterns per jurisdiction (some GCC countries changed weekends in recent years [VERIFY current patterns]).
- Fiscal years: any financial year end; India's April–March default only for Indian entities; multi-FYE groups get period mapping for consolidated dashboards.

### Y.9.3 Internationalisation and localisation

| Item | Specification |
|---|---|
| Framework | ICU MessageFormat strings in `packages/i18n` with plural and gender rules; no concatenated strings; all user-facing text externalised (lint rule) |
| Locales (planned) | `en-IN` (default), `en-GB`, `en-US`, `hi-IN` (D-30), `ar-AE` (RTL), later `fr-FR`, `de-DE`, `ja-JP`, `id-ID`, `sw-KE` by demand |
| Formats | Locale-aware dates, numbers (Indian lakh/crore grouping for `en-IN` with toggle to international grouping), currencies, names (given/family order), addresses (country-specific address schemas) |
| RTL | Logical CSS (`margin-inline-start` etc.), `dir` on root, mirrored icons with direction, bidirectional isolation for mixed text, charts mirrored where axes imply direction; accessibility tested with Arabic screen readers (NVDA/JAWS Arabic, VoiceOver) |
| Translation workflow | Product strings translated by professional translators with glossary; machine pre-translation allowed for UI strings with human review; legal/regulatory text never translated by the UI pipeline (§Y.4.4) |
| Glossary ("i" help) | Terms per jurisdiction (e.g., "confirmation statement", "registrable controller", "economic substance") added to the P23 glossary registry with jurisdiction scope |
| Vidhi | Answers in the user's chosen locale, citing official-language clauses with English translations (NN-06) |

---

## Y.10 Tax and invoicing for cross-border SaaS and services *(v1.1)*

LawDocs' invoices are issued by OH8 (X-02). This section states the rules the OH8 catalogue and LDC checkout must support when foreign clients buy; all positions are summaries for design and must be confirmed by a tax adviser before launch **[VERIFY all]**.

| Situation | Treatment to support |
|---|---|
| Indian supplier → foreign business client (export of services) | Zero-rated supply under IGST Act s.16 where s.2(6) conditions are met (supplier in India, recipient outside India, place of supply outside India, payment in convertible foreign exchange or INR where RBI permits, not merely establishments of the same person); supply under a Letter of Undertaking (LUT) without payment of IGST, or with IGST and refund; invoice must state "supply meant for export under LUT without payment of IGST"; realisation of export proceeds within FEMA timelines |
| Indian supplier → foreign individual / non-business user | Online information database access and retrieval (OIDAR) rules apply to imports into India; for exports, place of supply and export conditions decide; consumer sales abroad may trigger foreign VAT registration (below) |
| EU business customers | EU VAT reverse charge by the customer (VAT Directive Arts. 44 and 196); invoice states "reverse charge"; capture and validate the customer's VAT number (VIES) |
| EU consumers | Non-Union OSS registration for B2C electronically supplied services; VAT at the consumer's member-state rate |
| UK | B2B reverse charge; B2C digital services require UK VAT registration (no threshold for non-established suppliers) |
| UAE | VAT 5%; B2B reverse charge for VAT-registered recipients; non-resident suppliers of electronic services to non-registered recipients must register [VERIFY] |
| Saudi Arabia | VAT 15%; non-resident digital service suppliers to non-registered customers register; reverse charge for registered businesses [VERIFY] |
| Singapore | GST 9%; Overseas Vendor Registration for B2C remote services where thresholds are exceeded (global turnover above S$1 million and B2C supplies to Singapore above S$100,000 [VERIFY]); B2B handled by the GST-registered recipient under reverse charge |
| United States | Sales tax on SaaS varies by state; economic-nexus thresholds; marketplace and remote-seller rules — handled through a tax-engine adapter in OH8 when US sales start [REC] |
| Withholding tax | Foreign clients may withhold tax on fees for technical services or royalties; collect Tax Residency Certificate and Form 10F, apply DTAA rates, issue documentation to clients for treaty relief [VERIFY per treaty] |
| Local entities later | When volumes justify, LawDocs may set up a UAE free-zone or Singapore entity as a selling entity; OH8 must be multi-entity (selling entity per contract), with intercompany transfer pricing for India-delivered services (decision D-27 extended) |

Payments: international cards and bank transfers through the payment gateway's international acceptance or a second PSP for non-INR settlement (adapter behind `BILLING_PORT`; card data never touches LDC, NN-16).

---

## Y.11 Global regulatory change monitoring *(v1.1)*

1. **Official feeds first** (added to Appendix F per corridor when a pack enters `SOURCE_REGISTER_BUILT`): EUR-Lex (Official Journal), legislation.gov.uk and Companies House notices, FCA and PRA publications, US Federal Register API and eCFR, SEC and state registries, MAS and ACRA, CBUAE rulebook, DFSA and FSRA rulebooks, UAE legislation portal, SDAIA and SAMA, Mauritius FSC, Central Bank of Kenya, CBN Nigeria, etc. Each source records method (RSS/API/HTML diff), language, time zone and freshness SLA. All hosts must be on the production egress allowlist (master §7 note on IFSCA).
2. **Licensed intelligence feeds** through `REG_INTEL_PORT` adapters (candidates: Thomson Reuters Regulatory Intelligence, LexisNexis, Wolters Kluwer, CUBE, Regology, Corlytics, OneTrust DataGuidance for privacy). Licence terms decide display: typically a headline, summary and link may be shown to licensed users; full text is not redistributed. Items enter the P05 Radar as `LICENSED_SIGNAL`, are labelled with the provider, and become LDC Updates only after the pack's reviewer of record confirms the primary source (NN-34).
3. **Partner-reported changes:** content partners file change notices through the partner portal with the official source; same review path.
4. **Scan schedule:** the 20:00 IST daily scan (D-18) is supplemented by per-cell local-time scans (e.g., 18:00 GST for the GCC cell, 18:00 CET for the EU cell) so that Updates reach users in their working day *(v1.1)*.
5. **Metrics:** median and p90 latency from official publication to LDC Update per jurisdiction, shown in the coverage statement.

---

## Y.12 Go-to-market phases and sequencing *(v1.1)*

| Phase | Timing (indicative, after Wave 1 GA) | Scope | Entry criteria | Exit metrics |
|---|---|---|---|---|
| **G0 — Global-ready core** | Already in Waves 1–2 | Jurisdiction dimensions in data model; EU/UK GDPR, CCPA/CPRA overlays; INTL-GEN template; currency/time-zone handling; English-only UI | P03, P15, P19 exits | 3 Indian tenants using GDPR overlay; zero schema change needed for INTL content |
| **G1 — Overseas subsidiaries of Indian groups** | Wave 3 (P25 sprints 1–4) | Global entity management; Tier C packs for UAE (mainland + DIFC + ADGM), Singapore, UK, US-Delaware, Mauritius, Netherlands; India ODI/FEMA overlay; content partners signed in each | 2 design partners (one NBFC group with a GIFT/UAE entity, one corporate group with UK/US subsidiaries) | Calendars for ≥ 30 foreign entities live; partner SLA ≥ 95%; no missed filing attributable to content |
| **G2 — MNC subsidiaries and GCCs in India** | Parallel with G1 | Sell India families to foreign-headquartered groups; EU cell for head-office users and EU entities; USD/EUR pricing; English (UK/US) locales; SSO with head-office IdP | EU cell live (P25 §4E); OH8 multi-currency | ≥ 5 MNC logos; NPS ≥ 40; sales cycle < 120 days |
| **G3 — GCC and Singapore regulated packs** | +2–3 quarters | Tier A packs for UAE finance companies and fund managers (CBUAE, DFSA, FSRA), Singapore MAS-licensed entities; Arabic UI; GCC cell; Saudi decision after SDAIA amendments settle | In-country regulatory reviewers signed; GCC cell residency assessment done | First 3 regulated GCC tenants; Update latency p90 ≤ 5 business days |
| **G4 — Africa and South Asia corridors** | +4 quarters | Tier C/B packs for Kenya, Nigeria, South Africa, Sri Lanka, Bangladesh, Nepal driven by Indian lenders/fintechs' expansion and Finbyx/Udofin customers | Partner availability; client demand ≥ 3 groups per country | — |
| **G5 — Partner-led long tail** | Ongoing | Partners build packs on demand (Lawrbit-style) through the partner portal and INTL-GEN; LawDocs reviews and publishes | Partner programme mature | Countries with PUBLISHED packs; revenue share paid |

**Channel.** Combine direct sales to Indian groups (existing relationships through LawDocs advisory and FinLegal Academy) with partner-led sales abroad: content/delivery partners resell or refer LDC in their markets under D-06 switches; Big Four-style alliances (like Athennian with PwC UK) are a later option once Tier A packs exist.

**Pricing hooks (for Appendix N/OH8):** pack subscriptions per entity per jurisdiction tier (Tier C/B/A), global entity-management module per number of entities, cell surcharge for EU/GCC/SG residency, on-call query bundles, partner delivery services at partner prices plus disclosed platform fee where lawful [OWNER TO SET].

---

## Y.13 Risks and mitigations *(v1.1)*

| Risk | Mitigation |
|---|---|
| Content quality abroad (wrong or stale law) | Reviewer of record, coverage statements, freshness SLAs, `SUSPENDED` state, licensed-feed signals, client-reported defect loop; no pack enabled without `PUBLISHED` (NN-19, D-19) |
| Unauthorised practice of law / professional-rules breach in foreign jurisdictions | LDC provides information and workflow, not legal advice; legal advice only by partners licensed in the jurisdiction contracting directly with the client; counsel opinion per country before commercial switches open (§Y.5.4) |
| Data-transfer non-compliance | Regional cells, home region per entity, transfer register, SCCs/IDTA/DIFC/ADGM clauses, aggregation-only group views (§Y.7–§Y.8) |
| Indian regulator expectations on RE data | Indian entities pinned to IN cell; supervisory access unaffected; outsourcing register entries for any foreign processing (P12) |
| Cost of multiple cells | Open cells only on contracted demand (G-phase entry criteria); infrastructure as code so a cell is reproducible; shared content plane |
| Translation errors | Provenance tags; machine-unreviewed text cannot publish; bilingual reviewers |
| Sanctions and export controls (clients or partners in sanctioned jurisdictions) | Sanctions screening at onboarding and partner onboarding (OFAC, UN, EU, UK, MHA lists); country blocklist in OH8 |
| Tax exposure abroad (VAT/GST registration, permanent establishment) | Tax adviser sign-off per market; OH8 tax engine; local selling entity when thresholds approach |
| Partner concentration or exit | Two partners per Tier A jurisdiction where possible; content IP owned by LawDocs; hand-over clause |
| Competitive response (Lawrbit, TeamLease, global suites) | Differentiate on transparency (coverage statements, reviewer of record), Indian financial-regulation depth, ecosystem (Finbyx/Udofin/Equator), price |

---

## Y.14 Rules, decisions and requirements adopted in master v1.1 *(v1.1)*

**Non-negotiable rules (adopted as numbered in master §4):**

- **NN-53 — Jurisdiction-pack enablement.** A non-India pack (or INTL-GEN sheet) generates obligations only when `PUBLISHED`, with a named reviewer of record, a complete source register and a published coverage statement; INTL-GEN imports without a `REVIEWER:` line in Column N cannot be published.
- **NN-24 — Home-region residency (restates NN-24).** Tenant data of each legal entity is stored and processed in that entity's home cell; Indian entities' home cell is IN; cross-cell processing of personal or confidential data only with a recorded legal basis in the transfer register; group views across cells use aggregates and metadata only.
- **NN-54 — Official-language provenance.** Every non-English clause stores the official text, the English translation and its provenance; `MACHINE_UNREVIEWED` text cannot be published or quoted as law.

**Adopted in master v1.1 (lead integration):** NN-53, NN-24 (amended), NN-54; D-42 regional cells (IN now; EU, GCC, SG, US on contracted demand); D-43 corridor order G0–G5 (§Y.12); D-44 partner model (roles §Y.5.1; client contracts directly with delivery partners by default; resale only where lawful); D-45 PILOT state in the jurisdiction-pack lifecycle; D-46 Saudi Arabia personal-data onboarding deferred until SDAIA amendments settle and China limited to Tier C non-personal calendars; X-51 template families (INTL-GEN is one of the 27); X-42 partner role names; X-50 linked tenants.

**Requirements:** the owner's instruction is recorded in `02` as R-110 (support global compliance later without redesign) and R-111 (study how Lawrbit serves companies abroad). The detailed global needs below are sub-requirements of R-110, numbered R-110.1–R-110.8: (1) support global compliance later without redesign; (2) emulate and beat Lawrbit's delivery abroad (R-111); (3) global entity management for groups with foreign subsidiaries; (4) multi-region data residency; (5) partner network for content and delivery abroad; (6) localisation (languages incl. RTL, currencies, time zones, fiscal years); (7) cross-border tax and invoicing; (8) global regulatory change monitoring (official + licensed feeds).

**Further resolutions applied in the pack:** `obligation_ref` gains a jurisdiction prefix for non-India content; the lifecycle DRAFT→PILOT→PUBLISHED→DEPRECATED (D-45) is canonical; error code `LDC-TPL-041` (INTL-GEN sheet without reviewer line); per-cell local-time scans supplement D-18 (Appendix F §F.12A); `REG_INTEL_PORT` and `FX_RATE_PORT` are in master §11.

---

## Y.15 Sources (accessed 25 October 2026)

**Lawrbit**
- Global Compliance Management Solution — https://www.lawrbit.com/global-compliance-management-solution/
- GCMS 360 brochure (countries, RI format, partner network, hosting, implementation) — https://www.lawrbit.com/wp-content/uploads/2022/03/lawrbit-gcms.pdf
- GCMS brochure (2020) — https://www.lawrbit.com/wp-content/uploads/2020/04/Lawrbit-Global-Compliance-Management-Solution-GCMS.pdf
- Compliance Service Management brochure — https://www.lawrbit.com/wp-content/uploads/2020/03/Lawrbit-CSMS.pdf
- Legal Matter Management brochure — https://www.lawrbit.com/wp-content/uploads/2020/03/Lawrbit-LMMS.pdf
- Clients and case studies — https://lawrbit.com/clients
- Home page — https://www.lawrbit.com/
- Partners page (failed to load on 25 Oct 2026) — https://www.lawrbit.com/partners/
- Press: partnership with ByTheBook Consulting (28 Jul 2022) — https://www.issuewire.com/lawrbit-announces-partnership-with-bythebook-consulting-1739412861451657
- Directory profile (GCC = Global Capability Centres) — https://www.businessofgcc.com/gcc-partners/lawrbit
- G2 listing — https://www.g2.com/products/lawrbit-global-compliance-management-solution/reviews
- Software Finder listing (pricing signal, reviews) — https://softwarefinder.com/legal/lawrbit

**Peers**
- Diligent Entities — https://diligent.com/features/entities/entity-compliance-new
- Athennian entity management — https://athennian.com/solutions/entity-management ; Athennian and PwC UK collaboration (22 Jul 2026) — https://www.athennian.com/news/athennian-and-pwc-uk-collaborate-to-bring-ai--powered-intelligence-to-global-subsidiary-governance
- TMF Group global entity management — https://www.tmf-group.com/en/news-insights/campaigns/global-entity-management
- TeamLease RegTech AI index (coverage counts, India only) — https://teamleaseregtech.com/ai-index/
- CUBE third-generation RegPlatform — https://www.fintechfutures.com/press-releases/cube-launches-new-third-generation-regplatform-to-intelligently-automate-regulatory-compliance
- OneTrust DataGuidance — https://www.onetrust.com/news/onetrust-unveils-the-next-generation-of-dataguidance-regulatory-research/
- Thomson Reuters Regulatory Intelligence — https://thomsonreuters.in/en/products-services/tax-accounting/regulatory-intelligence.html

**Data-transfer law**
- UAE cross-border transfers 2026 (Kayrouz & Associates) — https://www.kayrouzandassociates.com/insights/cross-border-data-transfers-under-uae-law-in-2026
- SDAIA draft amendments to PDPL Implementing Regulation (Clyde & Co, 8 Oct 2026) — https://www.clydeco.com/en/insights/2026/10/sdaia-publishes-draft-amendments-to-the-pdpl
- DPDP s.16 negative-list commentary (Mondaq, 26 Mar 2026) — https://www.mondaq.com/india/data-protection/1764976/from-localisation-debates-to-a-negative-list-making-cross-border-data-transfers-work-under-indias-dpdp-act
- GDPR — Regulation (EU) 2016/679 Chapter V; Commission Implementing Decision (EU) 2021/914 (SCCs) — https://eur-lex.europa.eu [VERIFY current adequacy list]

**Indirect tax (design summaries; adviser to confirm)**
- Singapore GST for overseas vendors — https://www.aseanbriefing.com/news/gst-in-singapore-when-overseas-vendors-must-register-and-collect-tax/
- UAE VAT on non-resident digital services — https://www.vatcalc.com/uae/uae-value-added-tax-on-non-resident-digital-services/
- IGST Act 2017 ss.2(6), 16; CGST Rules r.96A — https://cbic-gst.gov.in [VERIFY]
