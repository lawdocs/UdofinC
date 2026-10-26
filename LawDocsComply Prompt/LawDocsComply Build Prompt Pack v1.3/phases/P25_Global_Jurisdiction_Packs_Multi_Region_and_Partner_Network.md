# Phase P25 — Global Jurisdiction Packs, Multi-Region Cells and Partner Network *(v1.1)*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P03** (content model `cnt`, template registry `tpl`, importer — INTL-GEN family and jurisdiction-prefixed `obligation_ref`);
> - **P05** (source monitor, Radar, Updates — per-cell scans and licensed feeds);
> - **P15** (jurisdiction-pack framework §4J, group structures §4K, lifecycle §5.6, entity-form mapping);
> - **P18** (connector framework — `COMPANY_DATA_PORT` country adapters, `REG_INTEL_PORT`, `FX_RATE_PORT`, local `ESIGN_PORT` adapters);
> - **P19** (export packages per cell, infrastructure-move tooling, storage targets);
> - **P20** (entitlements and meters for packs, cells and query bundles; OH8 multi-currency, multi-entity billing);
> - **P21** (marketplace provider shell, engagements, retainers, SLA eSign — reused for foreign partners);
> - **P24** (infrastructure as code, release orchestration, certification evidence — extended per cell).
> - Also reads P06 (governance records of foreign entities), P07 (documents with language metadata), P12 (transfer register, TIA), P13 (person master).
>
> **Sequencing:** Wave 3 (after P21 and P22 exit), or earlier for G0 items already inside P03/P15. Sprint 1 freezes the jurisdiction hierarchy schema, the `home_region` contract, the cell routing API and the partner-portal role model. The EU cell (§4E) is built in sprints 2–5 and goes live only after the G2 entry criteria (Appendix Y §Y.12). Corridor packs (§4C) are content work by the content team and partners in parallel, gated by `PUBLISHED`.
>
> **Binding appendices:** **Y** (global expansion and jurisdiction packs — this phase's specification), E (template contract; INTL-GEN family), F (source register — per-corridor sources), G (rules register — foreign rules carry `LR-<ISO>-nnn`), M (export package per cell), N (pricing hooks), O (marketplace professional rules — extended per country), Q (security, sub-processors per cell), U (settings).
>
> **Requirements covered:** R-110 (global compliance; sub-requirements R-110.1–R-110.8 in Appendix Y §Y.14) and R-111 (Lawrbit delivery model) from the owner's instruction of 25 Oct 2026; extends R-005, R-021, R-034, R-035.
>
> **Estimated effort:** 10 two-week sprints for a squad of 9 (multi-region platform 3, global entity management 3, partner portal and query desk 2, localisation and RTL 1), plus the content team and contracted partners for corridor packs (outside squad capacity).

---

## 1. Objective and business outcome

LawDocsComply is India-first, but its customers are increasingly groups with entities abroad and foreign groups with entities in India; the owner wants to take it global. Lawrbit, the reference competitor, delivers abroad by combining one regulatory-intelligence feed with local law and accounting firms, translation of foreign laws, project-based discovery and AWS hosting in India and Frankfurt (Appendix Y §Y.2). This phase makes LDC able to switch on any country **as content and configuration, not code**, and to beat that model on transparency (coverage statements, reviewer of record, clause-level official-language provenance), residency (regional cells with a home region per legal entity) and openness (a partner marketplace the client can see and choose from).

| Outcome | Exit-gate measure |
|---|---|
| Global entity management | A group with an Indian parent and 12 foreign subsidiaries in 6 jurisdictions is onboarded in ≤ 2 hours of admin time; each entity has a structure-chart position, officers, registers and a 12-month jurisdiction calendar computed in its own time zone and holiday calendar; India ODI/FLA checkpoints are linked to each foreign subsidiary |
| Jurisdiction packs as data | A new country pack (Tier C) authored in `LDC-TPL-INTL-GEN-v2.0` passes import, reaches `PILOT` and then `PUBLISHED` with reviewer of record and coverage statement, and generates obligations for a pilot tenant — with **no code release** (NN-34) |
| Regional residency | The EU cell runs a full tenant plane in an EU region; a UK subsidiary's personal data and documents never leave the EU cell (verified by data-flow tests and access logs); the parent's group dashboard shows the entity's status via aggregates only |
| Transparent coverage | Every published pack shows in-scope/out-of-scope areas, reviewer of record, last-verified date, freshness SLA and monitoring status; a pack whose monitoring is stale > 30 days becomes `SUSPENDED` with a banner automatically |
| Partner network | At least one content partner and one delivery partner onboarded per G1 corridor through the partner portal with due diligence, DPA and scorecard; on-call query desk answers within SLA in the pilot (first response ≤ 1 business day) |
| Localisation | `en-GB`, `en-US`, `hi-IN` and `ar-AE` (RTL) locales pass WCAG 2.2 AA checks on the top 30 journeys; legal text displayed in official language + English with provenance |
| Cross-border commerce | A foreign client can buy a pack subscription in USD or EUR, receives an OH8 invoice with the correct export/reverse-charge wording, and the payment settles without card data touching LDC |

---

## 2. Scope (in / out)

**In scope**

- Jurisdiction hierarchy (country, subdivision, special zone) across content, entities, calendars, holidays, currencies, languages (Appendix Y §Y.4.2).
- Jurisdiction-pack lifecycle with `PILOT` (§5.1), tiers C/B/A and overlay packs, coverage statements and freshness metrics.
- INTL-GEN template family import path (validator, reviewer-line check `LDC-TPL-041`), country templates later.
- Global entity management (`gem`): structure chart, entity records for foreign forms, officers across entities, jurisdiction registers, filing calendars, registered agents, licences, intercompany agreements, India ODI/FDI linkage, foreign registry data adapters, filing packs.
- Regional cells (IN existing; EU first; GCC, SG, US templates), global control plane, home region per legal entity, routing, aggregation API for group views, per-cell AI routing, per-cell exports and backups.
- Transfer register integration, sub-processor lists per cell, adequacy/negative-list watchers.
- Partner portal: content partner, reviewer, delivery partner, implementation partner roles; due diligence; scorecards; query desk.
- Localisation: ICU messages, locales, RTL, locale formats, jurisdiction glossary.
- Global regulatory change: per-cell local-time scans, `REG_INTEL_PORT` licensed feeds, partner change notices.
- Cross-border commerce hooks into OH8: currencies, tax treatments, export invoices, withholding documentation.

**Out of scope**

- Writing the full content of foreign packs (content team and partners, tracked as content deliverables).
- Direct e-filing to foreign registries (prepared filing packs only, unless an official API is verified and the client authorises — NN-08).
- Foreign legal advice by LawDocs (partners only, D-32 extended).
- China and Saudi personal-data processing (D-46, D-46) until decisions are taken.
- A US cell build (template only; built on contracted demand).

---

## 3. Personas and permissions touched

| Role | What changes in P25 |
|---|---|
| `plt_super_admin` | Opens cells (infrastructure change through P24 change control), sets default home-region rules per jurisdiction (G setting), approves partner tiers |
| `plt_content_maker` / `plt_content_checker` / `plt_content_publisher` | Author and publish jurisdiction packs; a pack also needs the partner reviewer's sign-off (two-key publication: platform checker + external reviewer of record) |
| `plt_security_officer` | Approves cell residency assessments, sub-processor lists per cell, transfer-register entries for platform flows |
| `ten_admin` | Adds foreign entities, chooses home regions within allowed options, enables packs, approves delivery grants for foreign partners |
| `ten_cco`, `ten_dept_head`, `ten_kmp` (CS) | Group compliance map, subsidiary governance, policy cascades |
| `ten_maker` / `ten_checker` in foreign entities | Work in their entity's home cell, in their locale and time zone |
| **New** `prt_admin` (partner firm admin) | Manages the partner profile, users, credentials, agreements in the partner portal |
| **New** `prt_content_author` | Authors pack content (INTL-GEN uploads, translations, change notices) |
| **New** `prt_content_reviewer` | Reviewer of record; signs off pack versions; must differ from the author of the same version (NN-05) |
| **New** `prt_delivery_professional` | Answers on-call queries; works inside client tenants only via delivery grant as maker (NN-43) |
| **New** `prt_viewer` *(v1.1, X1)* | Read-only partner staff (partner workspace read; no content edit, no tenant data) |

*(v1.1, X1)* Canonical partner role codes are those of Appendix D §D.16.3 (`prt_admin`, `prt_content_author`, `prt_content_reviewer`, `prt_delivery_professional`, `prt_viewer`); the draft names `prt_author`, `prt_reviewer` and `prt_expert` are retired.
| `mkp_professional`, `mkp_provider_admin` | Existing marketplace roles; foreign partners map to these for engagements |
| `svc_vidhi` | Extracts entity data from foreign documents, explains foreign clauses in the user's locale, drafts queries and resolutions — on behalf of a named user, in-cell routing only (NN-41) |

Partner roles live in the `ldc` realm with partner-organisation scoping; they never see tenant data except through delivery grants.

---

## 4. Functional requirements

### 4A. Jurisdiction hierarchy and content model

**FR-P25-01 Hierarchy.** Implement `pack.jurisdiction` (ISO 3166-1 alpha-2, plus `EU` supranational), `pack.subdivision` (ISO 3166-2), `pack.special_zone` (LDC codes: `AE-DIFC`, `AE-ADGM`, `QA-QFC`, `IN-IFSC`, extensible), and link authorities, instruments, rule packs, holiday calendars and entity forms to the most specific level that creates the law (Appendix Y §Y.4.2).

**FR-P25-02 Jurisdiction-prefixed obligation references.** Non-India checkpoints carry `obligation_ref = <ISO|ISO-SUB|ZONE>/<AUTH>/<INSTR>/<VER>#<clause>`; Indian references keep the v1.0 format and are interpreted as `IN/…` in cross-jurisdiction queries; the Ecosystem `Obligation` contract receives the prefixed form (raise Spec v1.2 change request if the schema constrains the format) *(v1.1)*.

**FR-P25-03 Clause language set.** `cnt.clause` gains `official_languages[]`, `official_text` per language with hash, `english_text`, `translation_provenance` (`OFFICIAL`, `PARTNER`, `MACHINE_REVIEWED`, `MACHINE_UNREVIEWED`), `prevailing_language` and translator/reviewer ids. `MACHINE_UNREVIEWED` blocks publication (NN-54).

**FR-P25-04 Entity-form mapping.** `pack.entity_form_map` maps (jurisdiction, local form) → LDC family/type (e.g., `GB / private company limited by shares` → `COMPANY.PVT`; `AE-DIFC / private company` → `COMPANY.PVT`; `US-DE / LLC` → `COMPANY.LLC_US`), so that generic applicability rules work across countries and country rules specialise them.

**FR-P25-05 Calendars.** The P04 frequency engine accepts per-entity time zone, holiday calendar, working-week pattern and `weekend_rule` from the pack; statutory due dates are computed (NN-33) and shown in entity-local time with the viewer's local time on hover.

**FR-P25-06 Currency.** Every money field carries ISO 4217; penalty amounts in local currency; reporting-currency conversion uses `FX_RATE_PORT` snapshots (rate, source, date, type).

### 4B. INTL-GEN import and country templates

**FR-P25-07 INTL-GEN family.** Register `LDC-TPL-INTL-GEN-v2.0` in the template registry (P03) with its vocabularies (52 jurisdictions, 21 entity forms, 15 departments mapped by Appendix U §U.9.0, 7 compliance types, 15 filing tokens).

**FR-P25-08 Reviewer line rule.** For INTL-GEN and any country template, Column `related_docs` (v1.0: N) must contain `REVIEWER: <firm>, <city>, <YYYY-MM-DD>`; absence blocks publication with `LDC-TPL-041`; the reviewer firm must exist in the partner registry with role `reviewer` and an active agreement; mismatch raises `LDC-TPL-042`.

**FR-P25-09 INDIA-LINK.** `INDIA-LINK: <template code> / <instrument>` in Column `related_docs` (v1.0: N) creates a typed link between a foreign checkpoint and an Indian checkpoint (for example the subsidiary's annual accounts and the parent's APR), used by the group calendar and the India linkage panel (§4F).

**FR-P25-10 Country templates.** A country can be promoted to its own template (`LDC-TPL-<ISO>-<AREA>-v1.0`) through the same build mechanism (`templates/_build/`), keeping rows 1–2 and columns A–AD (NN-35); the importer maps country templates to the same content model.

### 4C. Jurisdiction packs, tiers, coverage statements

**FR-P25-11 Pack tiers.** `pack.jurisdiction_pack.tier` ∈ {C, B, A, OVERLAY}; tier drives freshness SLA (A monthly, B quarterly, C half-yearly + event-driven within 10 business days) and entitlement SKU (P20).

**FR-P25-12 Coverage statement.** Machine-readable JSON + rendered page (fields in Appendix Y §Y.4.5), versioned with the pack; shown in the Regulation Catalogue, the pack detail screen, the public trust page (for published packs) and exports (P19).

**FR-P25-13 Freshness metrics.** Compute per pack: last official-source check, overdue reviews, publication-to-Update latency (median, p90), defects per 1,000 checkpoints, query SLA attainment; feed the coverage statement and the content-ops dashboard.

**FR-P25-14 Auto-suspension.** If monitoring for a pack is stale > `gpk.monitoring.stale_days` (default 30, G) or the reviewer agreement lapses, the pack moves to `SUSPENDED`: tenants see a banner on affected checkpoints; instances continue (no silent stop); new tenants cannot enable it.

**FR-P25-15 Two-key publication.** Publishing a jurisdiction pack version requires the platform publisher and the external reviewer of record (`prt_content_reviewer`) to sign (eSign or step-up approval), with maker ≠ either signer (NN-05).

**FR-P25-16 Corridor starter packs.** Seed G1 Tier C corridor pack skeletons (UAE mainland, DIFC, ADGM, Singapore, UK, US-Delaware, Mauritius, Netherlands) with source registers and checkpoint areas per Appendix Y §Y.4.8 in `DRAFT`; content completed by partners.

**FR-P25-17 Overlay packs.** EU GDPR, UK GDPR, CCPA/CPRA (existing DATA-PRIV content), EU AI Act and DORA overlays attach to Indian entities through scope tests recorded per tenant (for example GDPR Art. 3(2) targeting/monitoring test answers with evidence).

### 4D. Applicability and onboarding of foreign entities

**FR-P25-18 Foreign entity wizard.** Organisation › Entities › Add foreign entity: country → registration number → registry adapter fetch (where licensed) or document upload → Vidhi extraction of name, form, registered office, officers, owners, FYE (draft, human-confirmed; NN-14, NN-37) → parent and ownership → home region (default by jurisdiction, §4E) → proposed packs with coverage statements → owners and delivery partner → calendar generation (Appendix Y §Y.4.9). Target ≤ 20 minutes per entity with registry data available.

**FR-P25-19 Applicability.** The P15 engine evaluates foreign entities with their jurisdiction attributes; strictest-wins logic across Indian overlays and local packs; "why" explanations cite the local clause and the scope test.

**FR-P25-20 Bulk onboarding.** Import a group entity list (`LDC-DT-GEM-ENTITIES`, Excel/CSV with `_Template_Info`) of up to 500 entities with validation, de-duplication against existing entities, proposed home regions and pack suggestions; run as a background job with a results report.

**FR-P25-21 Pack enablement.** Tenant admin enables packs per entity; only `PUBLISHED` packs (or `PILOT` packs for named pilot tenants who accept the pilot notice) can generate obligations (NN-53).

### 4E. Regional cells and home region

**FR-P25-22 Cell model.** `core.cells` (cell_id `IN`, `EU`, `GCC`, `SG`, `US`; regions primary/DR; status; residency attestation; sub-processor list version). Each cell runs the complete tenant plane (apps/api, database with RLS, Object Lock storage, OpenSearch, Temporal workers, AI route, backups) from the same infrastructure-as-code with cell-specific parameters (P24).

**FR-P25-23 Global control plane.** A minimal global service holds tenant directory, legal entity → home cell routing, identity discovery, platform content plane replication, release orchestration and billing references; it stores no tenant personal data or documents. Content plane (regulatory content) replicates read-only to every cell.

**FR-P25-24 Home region per legal entity.** `core.legal_entities.home_cell` is required; default from `gem.default_home_cell_by_jurisdiction` (G: IN→IN; EU/EEA/UK/CH→EU; AE/BH/OM/QA/KW→GCC; SG→SG; others→IN); Indian entities are fixed to IN (L) unless a Governed exception with legal basis is recorded; changes are migrations with evidence packs (P19 FR-P19-30) and tenant approval.

**FR-P25-25 Request routing.** API gateway resolves the target entity's home cell from the request context and routes; cross-cell user sessions are federated; every access to a cell is logged in that cell's audit ledger (NN-02) and, for staff, through grants or break-glass (NN-30).

**FR-P25-26 Aggregation API.** Each cell publishes per-entity aggregates (status counts, due-date lists without personal data, risk scores, KPI values, document titles without content, coverage-tier) to the group home cell every 15 minutes and on change; group dashboards (Appendix Y §Y.6.3) read aggregates only; detail opens in the home cell.

**FR-P25-27 Cross-cell replication by exception.** A tenant may request full replication of selected record types to the group cell; the request requires the DPO/security approval, a transfer-register entry with legal basis (SCCs/IDTA/DIFC/ADGM clauses, consent or other), and is shown in the tenant's data-residency panel (NN-24).

**FR-P25-28 AI routing per cell.** `packages/ai` resolves a per-cell route for each data class (e.g., EU cell → Bedrock in an EU region; GCC cell → in-region or approved route) with no failover outside permitted regions (NN-41) [VERIFY model availability per region at cell launch].

**FR-P25-29 Exports and backups per cell.** LDC-EXPORT packages are built in the home cell; group exports are a set of per-cell packages plus a group index (Appendix M); backups stay in the cell's region pair.

**FR-P25-30 Residency evidence.** Each cell produces a monthly residency attestation (storage locations, key locations, sub-processors, data-flow test results) stored as control evidence (P24) and available to tenants in the trust centre.

### 4F. Global entity management (`gem`)

**FR-P25-31 Entity record.** Fields per Appendix Y §Y.6.1 (local-script and English names, forms, identifiers incl. LEI, registry, registered agent, FYE, currencies, time zone, holiday calendar, languages, home cell, status).

**FR-P25-32 Structure chart.** Ownership graph with direct/indirect percentages, share classes, voting vs economic interest, control flags; as-at slider (bitemporal); filters by jurisdiction, status, overdue items; export to PDF/PNG and Excel; keyboard-navigable alternative table view (NN-21).

**FR-P25-33 Officers across entities.** One person record (P13 person master) across all entities; appointments with role, dates, residency, identity-verification status, signing authority; conflict and over-boarding alerts; local-director requirement checks where a pack defines them.

**FR-P25-34 Registers.** Generate jurisdiction registers (members, directors, secretaries, charges, beneficial owners / PSC / registrable controllers, nominees) from records via pack-defined register templates; entries append-only (NN-36 pattern); printable/exportable in the local format.

**FR-P25-35 Filing calendars and filing packs.** Pack rules generate per-entity calendars; for each filing, a filing pack (pre-filled forms where templates exist, checklist, data from the entity record, signatory list) is prepared for the partner or client; acknowledgement and filing reference captured (NN-08).

**FR-P25-36 Registered agents, licences, intercompany.** Registers for agents (contracts, renewal, fees), licences (conditions, renewals) and intercompany agreements (type, parties, TP documentation status, related-party flags into P06).

**FR-P25-37 India linkage panel.** For each foreign subsidiary of an Indian parent: ODI route and references, APR status per year, FLA status, step-down disclosures, regulator approvals for regulated parents; for Indian subsidiaries of foreign parents: FDI reporting status; checkpoints linked via INDIA-LINK (FR-P25-09) [VERIFY current form names].

**FR-P25-38 Registry adapters.** `COMPANY_DATA_PORT` country adapters (first: UK Companies House public data API; others via licensed aggregators) with licence terms recorded per adapter; read-only; refresh on demand and monthly; change detection raises tasks ("registered office changed at registry but not in LDC").

### 4G. Partner network and portal

**FR-P25-39 Partner registry.** `prt.partners` (firm, jurisdictions, roles, licences/bar numbers, insurance, conflicts policy, sanctions screening result, security questionnaire, agreements, tier, scorecard) with due-diligence workflow and maker-checker approval.

**FR-P25-40 Partner portal.** Provider shell modules: pack workspace (source register, INTL-GEN upload with validator, translation tagging, change notices, review sign-off), query desk, engagements and delivery grants, scorecard, commercial statements (Appendix Y §Y.5.4).

**FR-P25-41 Content contribution workflow.** Partner author uploads → automatic validation → platform content checker review → partner reviewer sign-off → platform publisher → `PILOT`/`PUBLISHED` (two-key, FR-P25-15); every step in the audit ledger.

**FR-P25-42 On-call query desk.** "Ask a local expert" on any foreign checkpoint (entitlement-gated): creates a query with entity context under a delivery grant; routed to the reviewer-of-record firm or a client-chosen partner; SLA clock (first response default 1 business day, answer 3 business days, G within partner agreement bounds); answer stored as a tenant-private expert note; optional proposal to improve the pack with client permission.

**FR-P25-43 Scorecards and tiers.** Quarterly scorecard computation (defect rate, review turnaround, query SLA, client satisfaction, filing timeliness, security incidents) → Gold/Silver/Registered tier; tier changes are approvals by `plt_super_admin` with reason.

**FR-P25-44 Commercial switches per country.** Extend the D-06 switch matrix to (country × profession × service type × model) with defaults OFF and a required counsel-opinion reference to enable (Appendix Y §Y.5.4; NN-20).

### 4H. Localisation

**FR-P25-45 Locales.** Ship `en-GB`, `en-US`, `hi-IN`, `ar-AE` (RTL) in addition to `en-IN`; locale picker per user; tenant default locale per entity.

**FR-P25-46 RTL.** Logical CSS throughout `packages/ui`; mirrored layouts; bidi isolation for mixed scripts; RTL visual-regression tests; Arabic screen-reader passes.

**FR-P25-47 Locale formats.** Dates, numbers (lakh/crore toggle), currencies, names, addresses per locale; jurisdiction glossary terms in the P23 registry.

**FR-P25-48 Bilingual legal display.** Checkpoint and clause views show English + official text toggle with provenance badge; Vidhi explanations labelled as explanations.

### 4I. Global regulatory change monitoring

**FR-P25-49 Per-cell scans.** P05 scheduler supports per-source local-time scans (e.g., 18:00 Gulf Standard Time, 18:00 CET) in addition to the 20:00 IST reconciliation (D-18 extended).

**FR-P25-50 Licensed feeds.** `REG_INTEL_PORT` adapters ingest licensed signals as `LICENSED_SIGNAL` Radar items labelled with provider; display limited by licence; Update created only after reviewer confirmation against the primary source (NN-34).

**FR-P25-51 Partner change notices.** Partners file change notices with the official source link; same triage path; latency measured.

**FR-P25-52 Data-law watchers.** Watch items for DPDP s.16 notifications, EU adequacy decisions, UK adequacy regulations, UAE PDPL Executive Regulations, SDAIA PDPL amendments, PDPC advisories; each raises a transfer-review task in P12.

### 4J. Cross-border commerce (with OH8)

**FR-P25-53 Currencies and price books.** OH8 price books per currency (INR, USD, EUR, GBP, AED, SGD); LDC configurator shows the client's contract currency (X-02).

**FR-P25-54 Tax treatments.** OH8 tax engine supports export with LUT (India), reverse-charge annotations (EU/UK/UAE/Saudi/Singapore B2B), foreign VAT registrations when enabled, withholding documentation (TRC, Form 10F) collection in the client's billing settings (Appendix Y §Y.10) [VERIFY all with tax adviser].

**FR-P25-55 Entitlements.** Pack subscriptions per entity per tier, global entity-management module by entity count, cell residency surcharge, query bundles, partner services — all metered in `bil` and priced by OH8.
### 4K. Group governance across countries

**FR-P25-56 Group compliance map.** SCR-GEM-08 shows, per entity and country, on-time rate, overdue items, 30/60/90-day filings, high-risk open items, pack tier, pack freshness and home cell; built from aggregates only (FR-P25-26); exportable as a board annex.

**FR-P25-57 Subsidiary board calendars.** Each foreign entity's board and shareholder meetings (or written resolutions where the local law allows them instead of an AGM) are generated from its pack; P06 meeting mechanics are reused with jurisdiction rules for notice periods, quorum and minute-signing supplied by the pack (not hard-coded).

**FR-P25-58 Policy cascade.** Group policies published by the parent (P07) can be cascaded to selected entities with a local addendum per jurisdiction (drafted by Vidhi from the pack's local requirements, reviewed by the local partner); attestations are tracked per entity and language.

**FR-P25-59 Group escalation.** Overdue foreign items escalate along a configurable chain (entity owner → regional head → group CCO → group board) using entity-local business calendars for timers; escalation never pauses statutory clocks (NN-33).

**FR-P25-60 Group board pack.** Quarterly group compliance report (status by jurisdiction, exceptions, regulatory changes affecting subsidiaries, licence renewals, director changes) generated in the parent's locale with entity annexes; numbers from aggregates (NN-37).

### 4L. Content operations for jurisdiction packs

**FR-P25-61 Pack production plan.** Content-ops board (Console › Content › Jurisdictions › Plan) lists planned packs by corridor phase (Appendix Y §Y.12), tier, partner, target dates and status; a pack cannot enter `CONTENT_AUTHORED` without a signed content-partner agreement and reviewer of record.

**FR-P25-62 Effort and cost tracking.** For each pack version: checkpoints authored, partner hours, translation cost, review cost and defects found, so that pricing per pack (P20/OH8) reflects real maintenance cost.

**FR-P25-63 Reuse across jurisdictions.** Authors can clone checkpoint structures from a similar jurisdiction (e.g., ADGM from DIFC, or one common-law company cycle to another) as a drafting aid; clones are marked `DERIVED_FROM` and must be re-cited to the local law before review (no inherited citations).

**FR-P25-64 Client-built local content.** A tenant may author its own foreign checkpoints (tenant overlay, P03) for jurisdictions without a published pack; these are labelled "client-authored, not reviewed by LawDocs", never counted in coverage statements, and can be offered to the content team as a pack seed with the tenant's permission.

**FR-P25-65 Pack SKUs.** Each published pack exposes a SKU code (tier × jurisdiction) to OH8; disabling a pack commercially never deletes history (NN-29) and never blocks reading or export (NN-42).



### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P25-X01 — Linked tenants and FX sources.** A legal entity whose home cell differs from its group tenant's is hosted in a **linked tenant** in that cell (same group, identity federation and templates; aggregates only across cells — NN-24 as amended; Appendix D and P01). `FX_RATE_PORT` providers are RBI/FBIL reference rates for INR pairs and the central-bank reference rate of the foreign currency (ECB, CBUAE, MAS) [VERIFY licence terms]; `erm.group.fx_rate_source` in P08 reads from the same snapshots.

---

## 5. Workflows and state machines

### 5.1 Jurisdiction pack version (extends P15 §5.6)

| State | Entry | Exit / transition | Guards | Timers |
|---|---|---|---|---|
| `PROPOSED` | Content team or partner proposes a country/area | → `SOURCE_REGISTER_BUILT` when sources registered | Corridor approved in roadmap | — |
| `SOURCE_REGISTER_BUILT` | All official sources listed (Appendix F format) with monitoring method | → `CONTENT_AUTHORED` | Each source fetchable from production egress | Monitoring starts |
| `CONTENT_AUTHORED` | INTL-GEN/country sheets imported without blocking errors | → `IN_COUNTRY_REVIEW` | No `MACHINE_UNREVIEWED` clauses; every row has `REVIEWER:` line | — |
| `IN_COUNTRY_REVIEW` | Reviewer of record reviewing | → `APPROVED` (reviewer signs) or back to `CONTENT_AUTHORED` (defects) | Reviewer ≠ author (NN-05) | Review SLA by tier |
| `APPROVED` | Platform checker approval + reviewer sign-off | → `PILOT` | Coverage statement complete | — |
| `PILOT` | Enabled for named pilot tenants with pilot notice | → `PUBLISHED` after ≥ 60 days or one filing cycle with no open Critical defect; → `CONTENT_AUTHORED` on Critical defect | Pilot acceptance recorded | Pilot clock |
| `PUBLISHED` | Two-key publication | → `MAINTAINED` (automatic when monitoring active) | — | — |
| `MAINTAINED` | Monitoring active, reviews on schedule | → `SUSPENDED` if monitoring stale > 30 days or reviewer agreement lapses; → new version cycle on change | — | Freshness SLA timers |
| `SUSPENDED` | Banner to tenants; no new enablement | → `MAINTAINED` when cured; → `WITHDRAWN` by decision | — | Escalation to content head at +7 days |
| `WITHDRAWN` | No new instances; history preserved (NN-29) | terminal | Tenant notice ≥ 60 days [REC] | — |

Events: `JurisdictionPackStateChanged`, `JurisdictionPackPublished`, `JurisdictionPackSuspended`, `CoverageStatementPublished`.

### 5.2 Foreign entity onboarding

`DRAFT` (wizard started) → `DATA_FETCHED` (registry adapter or upload processed; Vidhi extraction pending confirmation) → `CONFIRMED` (admin confirms fields) → `HOME_CELL_ASSIGNED` (routing created; transfer-register entries generated) → `PACKS_ENABLED` → `ACTIVE` (calendar generated). Failure paths: registry fetch failed → manual entry; home cell not available (cell not open) → entity placed in IN cell with a recorded basis or kept in `CONFIRMED` until the cell opens (client's choice).

### 5.3 Home-cell migration

`REQUESTED` (tenant admin) → `ASSESSED` (DPO/security: legal basis, sub-processors, keys) → `APPROVED` (tenant + platform) → `SCHEDULED` → `REPLICATING` (copy with checksums; dual-read) → `VERIFYING` (row counts, hashes, audit-chain continuity, golden export diff) → `CUT_OVER` (routing switched; read-only window) → `COMPLETED` (source data purged after retention hold; evidence pack filed) or `ROLLED_BACK`. NN-11: no customer re-upload; record ids unchanged.

### 5.4 On-call query

`OPEN` (client submits) → `ASSIGNED` (partner expert) → `CLARIFICATION_REQUESTED` ↔ `OPEN` → `ANSWERED` → `ACCEPTED` (client) or `REOPENED` → `CLOSED`; optional `PROPOSED_FOR_PACK` (client permits sharing) → content workflow. SLA timers: first response, answer; breach escalates to partner admin and LawDocs partner manager; scorecard updated.

### 5.5 Partner onboarding

`APPLIED` → `SCREENING` (sanctions, licence, insurance, security questionnaire) → `CONTRACTING` (framework, DPA, SLA; eSign) → `ACTIVE` (tier Registered) → `PROBATION` (scorecard below floor) → `SUSPENDED` / `TERMINATED` (content hand-over, access revoked, open queries reassigned).

### 5.6 Licensed signal triage

`RECEIVED` (`LICENSED_SIGNAL`) → `MATCHED` (to pack and instruments) → `PRIMARY_SOURCE_FOUND` → `ASSESSED` (impact on checkpoints) → `UPDATE_PUBLISHED` (via P05 release) or `NO_ACTION` (reason). Never `UPDATE_PUBLISHED` without `PRIMARY_SOURCE_FOUND` (NN-34).

---

## 6. Screens and UX

| Screen ID | Name | Menu path | Roles | Notes |
|---|---|---|---|---|
| SCR-GEM-01 | Group structure chart | Organisation › Group structure | `ten_admin`, `ten_cco`, `ten_kmp`, board | Zoom/pan, as-at slider, colour by jurisdiction or status, keyboard table alternative, export |
| SCR-GEM-02 | Entity list (global) | Organisation › Entities | `ten_admin`, group roles | Filters: country, form, home cell, status, overdue; bulk actions (assign owner, enable pack, export) |
| SCR-GEM-03 | Foreign entity wizard | Organisation › Entities › Add foreign entity | `ten_admin` | Seven steps (§4D), progress saved, registry fetch, Vidhi extraction review side-by-side with source document |
| SCR-GEM-04 | Entity record (foreign) | Organisation › Entities › <entity> | entity roles | Tabs: Overview, Officers, Owners, Registers, Calendar, Licences, Agents, Intercompany, India link, Documents, Residency |
| SCR-GEM-05 | Officers across group | Organisation › People › Officers | `ten_cco`, CS | Person-centric view of appointments, residency, verification, conflicts |
| SCR-GEM-06 | Registers (jurisdiction format) | Entity › Registers | CS, auditors | Local-format register view, print/export, append-only entries |
| SCR-GEM-07 | India linkage panel | Entity › India link | Parent CS/CFO | ODI/APR/FLA/FDI status with linked checkpoints |
| SCR-GEM-08 | Group compliance map | Dashboards › Group compliance | group roles, board | Map + table; aggregates; drill-down routes to home cell |
| SCR-GPK-01 | Jurisdiction pack catalogue (tenant) | Compliance › Regulation catalogue › Jurisdictions | `ten_admin`, `ten_cco` | Country cards with tier, coverage statement, reviewer, freshness, state badge (Pilot/Published/Suspended) |
| SCR-GPK-02 | Coverage statement | Pack › Coverage | all tenant roles; public for published packs | In/out of scope, reviewer, last verified, monitoring, latency metrics |
| SCR-GPK-03 | Jurisdiction packs (platform) | Console › Content › Jurisdictions | `plt_content_*` | Extends SCR-CNT-PK-03 with tiers, partner assignments, two-key publication, PILOT tenant list |
| SCR-GPK-04 | Bilingual clause view | Checkpoint › Source | all | English/official text toggle, provenance badge, prevailing-language note |
| SCR-CELL-01 | Data residency panel (tenant) | Settings › Data residency | `ten_admin`, DPO | Entities by home cell, transfer-register entries, replication exceptions, residency attestations |
| SCR-CELL-02 | Cells console | Console › Platform › Cells | `plt_super_admin`, `plt_security_officer` | Cell status, regions, sub-processor list versions, attestations, migrations |
| SCR-CELL-03 | Home-cell migration | Settings › Data residency › Move entity | `ten_admin` + platform | Request, assessment, schedule, progress, evidence |
| SCR-PRT-01 | Partner portal home | Provider › Home | partner roles | Tasks, queries, pack work, scorecard |
| SCR-PRT-02 | Pack workspace | Provider › Packs | `prt_content_author`, `prt_content_reviewer` | Source register, uploads with validator, translation tags, sign-off |
| SCR-PRT-03 | Query desk | Provider › Queries | `prt_delivery_professional` | SLA timers, context, answer editor, attachments |
| SCR-PRT-04 | Partner registry (platform) | Console › Partners | platform | Due diligence, agreements, tiers, scorecards |
| SCR-QRY-01 | Ask a local expert | Checkpoint › Ask an expert | tenant users with entitlement | Prefilled context, partner choice, SLA shown, price if pay-per-query |

**Fewer clicks.** Foreign entities inherit owners, departments and workflows from a chosen "template entity" (e.g., another UK subsidiary) — one click "copy set-up from"; packs auto-suggested from jurisdiction and form; registers generated automatically from the record; group dashboards default to "what needs attention this week across all countries" *(v1.1)*.

**"i" help keys:** `gem.home_cell`, `gem.registrable_controller`, `gem.confirmation_statement`, `gpk.coverage_statement`, `gpk.reviewer_of_record`, `gpk.translation_provenance`, `gpk.tier`, `cell.aggregation_view`.

---

## 7. Backend design

### 7.1 Modules touched

`gem` (new sub-module of `gov`), `pack` (jurisdiction hierarchy, tiers, coverage), `cnt` (clause language set, prefixed refs), `tpl` (INTL-GEN, reviewer rule), `chg` (per-cell scans, licensed signals), `core` (cells, routing, home cell), `int` (registry adapters, REG_INTEL_PORT, FX_RATE_PORT), `prt` (new: partner registry, portal, queries), `dpc` (transfer register links), `xpt` (per-cell exports), `bil` (meters), `ai` (per-cell routes), `hlp` (glossary), `packages/i18n`, `packages/ui` (RTL).

### 7.2 Tables (key columns)

| Table | Key columns |
|---|---|
| `pack.jurisdictions` | code (ISO), name, type (COUNTRY/SUPRANATIONAL), languages[], currency, default_time_zone, working_week, holiday_calendar_id, default_home_cell |
| `pack.subdivisions` | code (ISO 3166-2), jurisdiction_code, name, time_zone, holiday_calendar_id |
| `pack.special_zones` | code, parent (jurisdiction/subdivision), name, legal_system_note |
| `pack.entity_form_map` | jurisdiction_scope, local_form, ldc_family, ldc_type, notes, valid_from/to |
| `pack.jurisdiction_packs` (extends P15) | pack_id, scope_code, tier, state, version, reviewer_partner_id, content_partner_id, coverage_statement_id, freshness_sla, monitoring_status, last_verified_at |
| `pack.coverage_statements` | id, pack_version_id, json, rendered_doc_id, published_at |
| `pack.pack_metrics` | pack_id, period, latency_p50, latency_p90, defects_per_1000, overdue_reviews, query_sla_pct |
| `cnt.clause_texts` | clause_id, language, text, hash, provenance, translator_id, reviewer_id, prevailing |
| `core.cells` | cell_id, primary_region, dr_region, status, residency_attestation_doc_id, subprocessor_list_version |
| `core.legal_entities` (extended) | + jurisdiction_code, subdivision_code, special_zone_code, local_form, local_reg_no, registry, lei, fye, functional_ccy, reporting_ccy, time_zone, holiday_calendar_id, languages[], home_cell, status |
| `core.entity_routing` (global plane) | tenant_id, legal_entity_id, home_cell, version |
| `core.cell_migrations` | id, entity_id, from_cell, to_cell, state, basis_ref, evidence_pack_id |
| `gem.ownerships` | parent_entity_id, child_entity_id, pct_economic, pct_voting, share_class, valid_from/to (bitemporal) |
| `gem.appointments` | person_id, entity_id, role, start, end, residency, id_verification_status, authority_limits |
| `gem.registers` / `gem.register_entries` | register_type, entity_id, template_ref; entry json, append-only, hash |
| `gem.registered_agents` | entity_id, agent_partner_id, contract_doc_id, renewal_date, fees_ccy, fees_amount |
| `gem.licences` | entity_id, licence_type, authority, number, conditions, renewal_date |
| `gem.intercompany_agreements` | parties[], type, doc_id, tp_documentation_status, rpt_flag |
| `gem.india_links` | foreign_entity_id, parent_entity_id, route (ODI_AUTO/ODI_APPROVAL/FDI), refs, apr_status_by_year, fla_status_by_year |
| `gem.filing_packs` | instance_id, forms_doc_ids[], checklist, signatories[], ack_ref, filed_at |
| `prt.partners` | partner_id, legal_name, jurisdictions[], roles[], licences json, insurance, screening_result, security_questionnaire_doc_id, tier, state |
| `prt.partner_agreements` | partner_id, type (FRAMEWORK/DPA/SLA/CONTENT_LICENCE), doc_id, valid_from/to, counsel_opinion_ref |
| `prt.queries` | query_id, tenant_id, entity_id, checkpoint_id, partner_id, expert_id, state, sla_first_response_at, sla_answer_at, answer_doc_id |
| `prt.scorecards` | partner_id, period, metrics json, tier_result |
| `chg.licensed_signals` | id, provider, external_id, headline, summary (licence-limited), link, matched_pack_id, state |
| `int.fx_rates` | source, ccy_pair, rate_type, date, rate |

### 7.3 APIs (REST, `/v1`)

| Method and path | Purpose |
|---|---|
| `GET /v1/pack/jurisdictions` · `GET /v1/pack/jurisdictions/{code}/packs` | Catalogue of jurisdictions and packs with tiers and states |
| `GET /v1/pack/packs/{id}/coverage` | Coverage statement JSON |
| `POST /v1/pack/packs/{id}/versions/{v}/signoffs` | Reviewer or publisher sign-off (two-key) |
| `POST /v1/gem/entities:foreign` · `GET/PATCH /v1/gem/entities/{id}` | Foreign entity create (wizard backend) and record |
| `POST /v1/gem/entities:bulk-import` | Bulk entity list import (background job) |
| `GET /v1/gem/structure?asAt=` | Ownership graph |
| `GET/POST /v1/gem/entities/{id}/appointments` · `/registers` · `/licences` · `/agents` · `/intercompany` · `/india-links` | Sub-resources |
| `POST /v1/gem/instances/{id}/filing-pack` | Generate filing pack |
| `GET /v1/core/cells` · `POST /v1/core/entities/{id}/cell-migrations` | Cells and migrations |
| `GET /v1/core/aggregates/group/{tenantId}` (internal) | Cross-cell aggregates for group views |
| `GET/POST /v1/prt/partners` · `/agreements` · `/scorecards` | Partner registry (platform) |
| `POST /v1/prt/queries` · `PATCH /v1/prt/queries/{id}` | On-call query lifecycle |
| `POST /v1/prt/packs/{id}/uploads` | Partner content upload (validator response) |
| `POST /v1/chg/licensed-signals` (adapter callback) | Licensed feed ingestion |

### 7.4 Domain events

Internal (`in.lawdocscomply.<module>.<EventName>.v1`): `JurisdictionPackStateChanged`, `JurisdictionPackPublished`, `JurisdictionPackSuspended`, `CoverageStatementPublished`, `ForeignEntityOnboarded`, `EntityHomeCellAssigned`, `CellMigrationCompleted`, `OwnershipChanged`, `AppointmentChanged`, `RegisterEntryAdded`, `FilingPackPrepared`, `PartnerActivated`, `PartnerSuspended`, `QueryOpened`, `QueryAnswered`, `QuerySlaBreached`, `LicensedSignalReceived`, `TransferBasisRecorded`. Cross-product (X-01): ownership and entity changes that group products need (e.g., Finbyx group exposure views) are published as `in.infrabyx.governance.LegalEntityChanged.v1` only through `int` and only if the Ecosystem Spec v1.2 change request is approved.

### 7.5 Jobs and Temporal workflows

`PackFreshnessMonitor` (daily per pack; suspends stale packs), `CoverageStatementBuilder`, `ForeignEntityOnboardingWorkflow`, `RegistryRefreshJob` (monthly + on demand), `CellAggregationPublisher` (15-minute), `CellMigrationWorkflow` (§5.3), `ResidencyAttestationJob` (monthly per cell), `PartnerScorecardJob` (quarterly), `QuerySlaTimer`, `LicensedSignalTriageWorkflow`, `FxRateFetchJob` (daily), `PerCellScanScheduler`.

---

## 8. Integrations (ports and adapters)

| Port | Adapters in P25 | Notes |
|---|---|---|
| `COMPANY_DATA_PORT` | UK Companies House public data API (first); licensed aggregators for other registries (e.g., OpenCorporates-type providers) [VERIFY terms] | Read-only; licence terms per adapter; no scraping |
| `REG_INTEL_PORT` (new) | Candidates: Thomson Reuters Regulatory Intelligence, LexisNexis, Wolters Kluwer, CUBE, Regology, Corlytics, OneTrust DataGuidance | Licence-limited display; signals only |
| `FX_RATE_PORT` (new) | RBI reference rates, ECB reference rates, CBUAE rates, commercial provider | Snapshots stored with every conversion |
| `ESIGN_PORT` (extend) | EU eIDAS QTSP adapter, UAE Pass, Singpass Sign — per corridor after legal-effect verification | Document-type allow-list per jurisdiction |
| `STORAGE_PORT` (extend) | Per-cell storage targets; client BYO storage in the same region family | Residency checks (P19) |
| `AI_PORT` (extend) | Per-cell model routes | NN-41 |
| `BILLING_PORT` | OH8 multi-currency, multi-entity price books and tax engine | X-02 |
| `ECOSYSTEM_PORT` | `LegalEntityChanged` (proposed) | Spec v1.2 CR |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `gem.default_home_cell_by_jurisdiction` | G | IN→IN; EU/EEA/UK/CH→EU; AE/BH/OM/QA/KW→GCC; SG→SG; others→IN | Only cells with status OPEN | `plt_super_admin` (maker-checker) |
| `gem.india_entities_home_cell` | L | IN | — | — |
| `gem.cross_cell_replication.enabled` | T (per tenant, gated) | OFF | Requires transfer-register basis | `ten_admin` + DPO approval |
| `gem.aggregation.interval_minutes` | G | 15 | 5–60 | platform |
| `gpk.monitoring.stale_days` | G | 30 | 7–45 | platform |
| `gpk.pilot.min_days` | G | 60 | 30–180 | platform |
| `gpk.freshness_sla.tier_a_days` / `tier_b_days` / `tier_c_days` | G | 30 / 90 / 180 | 7–365 | platform |
| `gpk.event_update_sla_business_days` | G | 10 | 1–30 | platform |
| `gpk.publication.two_key` | L | ON | — | — |
| `tpl.intl.reviewer_line_required` | L | ON | — | — |
| `prt.query.first_response_hours` | G (per partner agreement) | 8 business hours | 2–24 | platform |
| `prt.query.answer_business_days` | G | 3 | 1–10 | platform |
| `prt.commercial.<country>.<profession>.<model>` | G | OFF | Requires counsel_opinion_ref | `plt_super_admin` |
| `i18n.locales.enabled` | G | en-IN, en-GB, en-US, hi-IN, ar-AE | — | platform |
| `i18n.tenant_default_locale` | T | en-IN | enabled locales | `ten_admin` |
| `i18n.number_grouping` | T (user) | locale default | indian / international | user |
| `chg.scan.local_time_by_cell` | G | IN 20:00 IST; EU 18:00 CET; GCC 18:00 GST | — | platform |
| `fx.rate_source_by_currency` | G | RBI (INR pairs), ECB (EUR), CBUAE (AED) | approved sources | platform |

---

## 10. Security, privacy and audit

- **Cell isolation.** Separate AWS accounts per cell (production), separate KMS key hierarchies, no cross-cell database links; security groups and SCPs prevent cell data stores from being reached from another cell; tested by automated data-flow tests (synthetic PII canaries must never appear outside their home cell's logs, stores or backups).
- **Global control plane minimisation.** Holds no personal data beyond login identifiers needed for routing; reviewed in the threat model (Appendix Q) as a high-value target (routing integrity, release orchestration).
- **Transfer register.** Every inter-cell and cell-to-partner flow has a register entry with legal basis and safeguard document; flows without an entry are blocked by policy (NN-24).
- **Staff access across borders.** Indian staff accessing EU/GCC cells only via break-glass (NN-30) or client-approved delivery grants (NN-43); access logged in the home cell; SCCs/contractual clauses cover such access.
- **Partner security.** Partners pass a security questionnaire, MFA mandatory, device posture checks for experts accessing client data [REC], least-privilege grants, quarterly access recertification; partner data incidents are reportable to LawDocs within 24 hours and flow into the client incident workflows (P12).
- **Sanctions.** Screening of foreign clients and partners at onboarding and periodically; country blocklist enforced at signup and checkout (OH8).
- **Audit.** All pack sign-offs, coverage statement publications, home-cell assignments and migrations, transfer-basis records, partner approvals, query answers and licensed-signal decisions are ledger events (NN-02, NN-45).
- **Sealed classes** (NN-13) remain in the entity's home cell with per-tenant keys; never part of aggregates.
- **Certification scope.** SOC 2 / ISO 27001 scope statements list cells in scope; each new cell enters scope through P24 before paid regulated tenants are onboarded there.

---

## 11. AI touchpoints and guardrails

| Touchpoint | What Vidhi does | Guardrails |
|---|---|---|
| Entity extraction | Reads certificates, registry extracts, annual returns, constitutional documents in any supported language and drafts entity, officer and ownership records | Draft only; side-by-side source view; human confirmation; low-confidence fields flagged (NN-14, NN-37) |
| Clause explanation | Explains a foreign clause in the user's locale | Labelled "explanation", cites official text and translation provenance; never replaces law (NN-54, NN-06) |
| Translation assistance | Pre-translates official text for partner reviewers | Stored as `MACHINE_UNREVIEWED` until a qualified reviewer changes provenance; cannot publish |
| Applicability "why" | Summarises why a pack applies to an entity | Generated from deterministic rule results only |
| Query drafting | Drafts the client's question to the local expert with context | Client edits and sends; answers from humans only |
| Resolution drafting | Drafts board resolutions for foreign entities from pack templates | Local partner review before use; NN-37 for numbers |
| Group briefing | Weekly "what changed across our countries" briefing | Built from published Updates and aggregates; no personal data across cells |

Per-cell AI routes (FR-P25-28); prompts and outputs logged in the home cell; no training on tenant data (NN-15).

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p25/*.feature`)

```gherkin
Feature: Jurisdiction pack publication
  Scenario: INTL-GEN sheet without reviewer line cannot publish
    Given an INTL-GEN workbook for "United Kingdom" where row 7 has no "REVIEWER:" entry in Column `related_docs` (v1.0: N)
    When the content checker attempts to move the pack version to IN_COUNTRY_REVIEW
    Then the importer reports LDC-TPL-041 on row 7
    And the pack version stays in CONTENT_AUTHORED

  Scenario: Two-key publication
    Given a UK Tier C pack version in APPROVED with reviewer partner "Firm X"
    When only the platform publisher signs
    Then the pack does not reach PILOT
    And when the reviewer of record from Firm X also signs, the pack reaches PILOT

  Scenario: Machine translation blocks publication
    Given a Netherlands clause whose English text has provenance MACHINE_UNREVIEWED
    When the publisher attempts publication
    Then publication is blocked with the clause listed

  Scenario: Stale monitoring suspends a pack
    Given the Singapore pack has no successful source scan for 31 days
    When PackFreshnessMonitor runs
    Then the pack state is SUSPENDED
    And tenants using it see a coverage-warning banner on affected checkpoints
    And their existing compliance instances continue

Feature: Global entity management
  Scenario: Foreign entity onboarding with registry data
    Given a tenant with an Indian parent entity
    When the admin adds a UK company by registration number
    Then name, registered office, officers and PSCs are fetched as draft fields
    And after confirmation the entity's calendar is generated in Europe/London time with UK bank holidays
    And the parent's APR and FLA checkpoints are linked to the new entity

  Scenario: Register entries are append-only
    Given a PSC register entry for the UK entity
    When a user attempts to edit the entry in place
    Then the API rejects the change
    And a correction can only be made by a new entry or a Correction Entry

  Scenario: Structure chart as at a past date
    Given the parent sold 40% of a Singapore subsidiary on 1 July 2026
    When the user views the structure chart as at 30 June 2026
    Then the ownership shows 100%
    And as at today it shows 60%

Feature: Regional cells and residency
  Scenario: UK entity data stays in the EU cell
    Given a UK subsidiary with home cell EU
    When its maker uploads evidence containing personal data
    Then the object is stored only in the EU cell's region pair
    And the group dashboard in the IN cell shows only the item's status and due date

  Scenario: Indian entity cannot be moved without basis
    Given an Indian NBFC entity with home cell IN
    When the tenant admin requests a move to the EU cell
    Then the request is refused unless a Governed exception with legal basis is recorded
    And the refusal is logged

  Scenario: Cross-cell replication requires a transfer basis
    Given a tenant requests replication of EU entity documents to the IN group cell
    When no transfer-register entry with a legal basis exists
    Then replication is not started
    And the DPO receives an approval task

Feature: Partner query desk
  Scenario: SLA breach escalates
    Given an on-call query assigned to a UAE partner expert at 10:00 GST on a working day
    When no first response is recorded within 8 business hours
    Then QuerySlaBreached is emitted
    And the partner admin and the LawDocs partner manager are notified
    And the partner's scorecard records the breach

  Scenario: Partner expert cannot check
    Given a partner expert with a delivery grant in a client tenant
    When the expert attempts to approve a compliance instance as checker
    Then the action is denied with LDC-CORE-005 or the NN-43 denial

Feature: Localisation
  Scenario: Arabic RTL layout
    Given a user with locale ar-AE
    When the compliance calendar is opened
    Then the layout direction is right-to-left
    And company names in Latin script render with bidirectional isolation
    And the page passes automated WCAG 2.2 AA checks

Feature: Cross-border commerce
  Scenario: EU client invoice
    Given an EU business client with a validated VAT number buying the Global Entity Management module in EUR
    When OH8 issues the invoice
    Then the invoice carries the reverse-charge note and export-under-LUT wording configured for the selling entity
    And no card data is stored in LDC

Feature: Bulk onboarding and defaults
  Scenario: Bulk import of a group entity list
    Given an LDC-DT-GEM-ENTITIES workbook with 120 rows including 3 duplicates of existing entities
    When the import job runs
    Then 117 entities are created in CONFIRMED state with proposed home cells by jurisdiction
    And the 3 duplicates are reported for merge, not created
    And a results report is available for download

  Scenario: Default home cell follows the jurisdiction rule
    Given gem.default_home_cell_by_jurisdiction maps "DE" to EU and the EU cell is OPEN
    When a German GmbH is added
    Then its proposed home cell is EU
    And if the EU cell were not OPEN the wizard would offer IN with a recorded basis or a deferred activation

Feature: Licensed signals
  Scenario: Licensed signal needs a primary source before an Update
    Given a licensed provider signal about an amendment to the Singapore Companies Act
    When the content checker tries to publish an Update without linking the official source
    Then publication is blocked
    And the signal stays in ASSESSED until PRIMARY_SOURCE_FOUND

Feature: Group governance
  Scenario: Escalation uses entity-local calendars
    Given an overdue filing for an entity in the GCC cell whose working week differs from India's
    When the escalation timer for the regional head runs
    Then business days are counted on the entity's working week and holiday calendar
    And the statutory due date shown is unchanged

  Scenario: Client-authored foreign content is labelled
    Given a tenant authors 12 checkpoints for Kenya where no pack is published
    When a user views one of them
    Then it is labelled "client-authored, not reviewed by LawDocs"
    And the Kenya coverage statement does not count it
```

NN tests touched: `NN-01_cell_isolation_*`, `NN-05_two_key_publication`, `NN-08_no_foreign_autofiling`, `NN-19_coverage_statement_required`, `NN-24_home_cell_residency_*` (renamed per NN-24), `NN-36_register_append_only_foreign`, `NN-41_ai_route_per_cell`, `NN-43_partner_expert_never_checks`; new families `NN-53_*`, `NN-54_*` (renumbered by the lead).

---

## 13. Deliverables and exit gate

**Deliverables:** jurisdiction hierarchy and entity-form mapping; INTL-GEN registration and reviewer-line validation; pack tiers, coverage statements, freshness metrics, auto-suspension, two-key publication, PILOT state; global entity management (structure chart, records, officers, registers, calendars, filing packs, agents, licences, intercompany, India linkage); UK Companies House adapter; EU cell live (infrastructure as code, attestation, sub-processor list, DR test); GCC/SG/US cell templates (not live); aggregation API and group dashboards; home-cell migration workflow; partner registry, portal, query desk, scorecards; `en-GB`, `en-US`, `hi-IN`, `ar-AE` locales with RTL; per-cell scans, `REG_INTEL_PORT` with one licensed provider in sandbox, `FX_RATE_PORT`; OH8 multi-currency and tax-treatment hooks; runbooks (`cell-open.md`, `cell-migration.md`, `partner-offboarding.md`, `pack-suspension.md`); updated Appendix F source registers for G1 corridors; trust-centre pages for cells and published packs.

**Exit gate:**

1. All §12 scenarios and touched NN tests pass in CI and in the EU cell staging environment.
2. Data-flow canary test shows zero PII leakage from the EU cell across 7 consecutive days of synthetic load.
3. One G1 corridor pack (UK Tier C recommended) reaches `PUBLISHED` with reviewer of record and coverage statement; at least one design-partner group runs ≥ 10 foreign entities.
4. P24 checklist re-run for the EU cell (VAPT including cell boundary, DR drill, backup restore, residency attestation, sub-processor DPAs).
5. Counsel opinions recorded for the partner commercial models enabled in the pilot countries (others remain OFF).
6. Tax adviser sign-off recorded for the invoice wording used in the pilot currencies.
7. Export coverage test (NN-10) passes for all new record types (`gem.*`, `prt.queries` tenant-side notes, coverage statements); Appendix M updated with the group-export index and entity sub-folders by jurisdiction.

---

## 14. Open items and verification flags

| OI | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P25-01 | Bedrock (or other approved) model availability in each planned cell region | Regional model availability changes | CTO | `ai.route.<cell>` OFF until verified; AI features disabled in that cell |
| OI-P25-02 | Saudi PDPL Implementing Regulation amendments (consultation to 5 Nov 2026) | Draft localisation and registration duties | DPO / counsel | Saudi entities limited to non-personal Tier C data |
| OI-P25-03 | UAE PDPL Executive Regulations | Unpublished as of Feb 2026 per secondary source | DPO | Contractual safeguards; watcher |
| OI-P25-04 | Companies House API terms for commercial use and rate limits | Licence terms | Product | Manual upload of registry extracts |
| OI-P25-05 | US CTA BOI scope after FinCEN 2025 interim final rule | Rule changes | Content team | Advisory-only checkpoint |
| OI-P25-06 | Partner commercial models per country | Professional rules vary | Counsel | All switches OFF |
| OI-P25-07 | Cross-border tax treatments (EU, UK, UAE, KSA, SG, US) | Adviser confirmation | CFO / tax adviser | Sell in INR/USD to Indian-contracting entities only |
| OI-P25-08 | India ODI/FDI form names and due dates in India link panel | FEMA rules and RBI directions | CS | Labels configurable; advisory dates |
| OI-P25-09 | Licensed regulatory-intelligence provider selection and licence | Commercial | Owner | Official feeds and partner notices only |
| OI-P25-10 | Local e-signature legal effect (eIDAS, UAE Pass, Singpass) per document type | Legal | Counsel | Wet-ink or partner-managed signing |
| OI-P25-11 | Ecosystem Spec v1.2 acceptance of jurisdiction-prefixed `obligation_ref` and `LegalEntityChanged` | Contract change | Integration lead | Keep refs internal; no cross-product entity events |
| OI-P25-12 | Holiday calendars with moon-sighting dates | Dates announced late | Content partners | Provisional dates + confirmation task |

---

## 15. Sources (accessed 25 October 2026)

See Appendix Y §Y.15 (Lawrbit product pages, brochures and client case studies; Diligent Entities; Athennian and the PwC UK collaboration of 22 Jul 2026; TMF Group; TeamLease RegTech AI index; CUBE; OneTrust DataGuidance; Thomson Reuters Regulatory Intelligence; UAE, DIFC, ADGM, Saudi, DPDP data-transfer commentary; GST/VAT summaries). Primary legal instruments named in Appendix Y §Y.4.8 and §Y.8 must be re-verified on official sites by the reviewer of record before any dependent checkpoint is published.

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**Added in v1.1:** NN-24, NN-53, NN-54; D-42–D-46; X-42, X-50.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
