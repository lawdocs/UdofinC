# Phase P05 — Regulatory Change Management and AI Question Authoring

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (Temporal, object storage with Object Lock, outbox, egress proxy), P01, P02 (settings, rule packs, flags), P03 (content model, clause index, importer, release pipeline, overlays, Regulation Catalogue), P04 (Work Inbox, tasks, calendar, notification service, due-date overrides). AI runtime basics from P17 sprint 1 (provider adapter, prompt registry, logging) — P05 may ship with a minimal adapter and adopt P17's when ready.
>
> **Sequencing:** Starts when P03 exits; may overlap P04 sprints 3–8. The source monitor (§4A–4B) ships first so that the content team accumulates history before go-live.
>
> **Binding appendices:** F (source register — every monitored URL, method and SLA), E (template contract and vocabularies used by the AI Studio), K (Vidhi AI agent specification), G (legal rules), B, U, C.
>
> **Requirements covered:** R-006, R-085, R-088, R-089, R-090, R-004, R-005, R-017, R-039, R-102 (generation of data-compliance sheets uses the same studio), R-097 (Vidhi as authoring assistant).
>
> **Requirements added in v1.1:** R-103 (RBI content base and catalogue upkeep; D-39, D-40), R-105–R-107 (foreign jurisdictions via P25), owner's v1.1 instruction (Appendix Z IMP-019–IMP-027), G5 gaps (audience preview, mute, content incidents, penalty intelligence, IRDAI concordance).
>
> **Estimated effort:** 9 two-week sprints for a squad of 8 *(v1.1: +2 for RBI category-page monitoring, catalogue automation, content-incident playbook, penalty corpus, foreign sources and agent evals)* (monitor and ingestion 2; diff, concordance and impact 2; Updates UX and tenant change management 2; AI Question Authoring Studio, agents and evaluation 3).
>
> **v1.1 changes (25 October 2026)**
> - RBI wording reconciled (238 per press release / 244 per RBI/2025-26/100; 9,445 circulars withdrawn; 240 live) and the **consolidated directions made the content base** (D-39).
> - **RBI category-page monitor** for the 22 DoR/DoS pages and the CEPD page — the "Updated as on" date change is the primary change signal; automatic catalogue rows for new directions; supersession flow; **sibling-change proposals** across RE categories (FR-P05-04, FR-P05-46; Appendix AB §AB.8).
> - Concordance seeded from the RBI/2025-26/100 Annex (9,445 circulars) and repeal paragraphs; statuses add MERGED and SPLIT; legacy NBFC re-citation before Wave-1 GA; IRDAI 2024 consolidation concordance (FR-P05-42).
> - Enrichment of every update, similar-past-change retrieval, per-release metrics, tenant filtering to adopted instruments, three-pane old/new/actionable view, summary-first ≤ 60-word gists, one-action "Accept impact", source back-fill after outages, Studio row scoring against the QA checklist (IMP-019–IMP-027).
> - Push-form **audience preview**, "remind until acknowledged", link-a-task, per-user per-domain mute (never CRITICAL), **content-incident playbook** with blast-radius report, **penalty-intelligence corpus** (G5).
> - **Foreign sources** through `REG_INTEL_PORT` with per-jurisdiction schedules in local time; licensed signals never become Updates without the primary source (LDC-CHG-121; NN-53, NN-54).
> - **Regulatory Analyst agent** (D-34) under bounded autonomy with evaluation gates (NN-50); AI Studio supports the 26 families incl. INTL-GEN and AI-GOV; MCP tools for Updates and concordance (NN-52).

---

## 1. Objective and business outcome

Regulators change their rules constantly — RBI alone withdrew 9,445 circulars and replaced them with its consolidated Master Directions on 28 November 2025 (238 function-wise directions per RBI's press release; 244 per circular RBI/2025-26/100; *v1.1*) and has since issued amendment directions and "updated as on" consolidations almost every month. A compliance tool whose content is static becomes wrong within weeks. This phase makes LawDocsComply a **living** system:

1. **Detect** every relevant publication from RBI, SEBI, IFSCA, IRDAI, MCA, MeitY, CERT-In, the Ministry of Labour, the Central and state co-operative registrars, GST/CBDT and other sources, every evening at 20:00 IST and intraday where feeds allow (D-18, R-089).
2. **Understand** it: classify, summarise, diff against the previous text, and map it to the checkpoints and tenants it affects.
3. **Publish** reviewed changes through the P03 release pipeline with maker-checker (NN-04, NN-05), preserving the previous direction and the previous actionable side by side (R-006, R-088).
4. **Tell** each affected client exactly *what changed, why it matters and what to do*, in the Updates inbox (separate from Notifications, NN-27), by e-mail and push, with calendar entries for effective dates (R-090).
5. **Manage** the client's implementation of the change: impact assessment, tasks, policy updates, board approvals and closure, all audit-trailed.
6. **Author** new compliance question sheets with AI: upload a Master Direction or regulation, let Claude apply the family template and the owner's question-writing method, export the draft Excel, verify, re-upload, and publish after confirmation (R-085) — for the platform (super admin) and for an individual client (client admin, tenant-only).

| Outcome | Exit-gate measure |
|---|---|
| Nothing missed silently | Every source in Appendix F has a last-success timestamp; a source not successfully scanned within its SLA raises a P2 alert to the content lead; the 20:00 IST reconciliation report lists counts per source and failures |
| Fast, reviewed publication | Triage ≤ 1 business day for all detected items (≤ 4 hours for items marked "effective immediately"); High-urgency actionable changes published to tenants ≤ 3 business days; others ≤ 10 business days (P95), measured on the change dashboard |
| Client knows what to do | Every published change produces an Updates item with the three-part note, old vs new actionable side by side, effective date in the calendar, and one-click actions (acknowledge, assign impact assessment, adopt, open conflicts) |
| History preserved | For any checkpoint, a user can see every regulatory change that affected it — previous instrument and paragraph, previous actionable, new actionable, change reason, release, reviewer, and the tenant's own response — exportable as a PDF/Excel change history |
| AI authoring accelerates Part 2 | On the evaluation set (owner-approved IFSCA sheets and the RBI NBFC 460–468 sheets), the AI Studio's draft reaches: clause-coverage recall ≥ 95 % of obligation clauses, citation accuracy ≥ 98 %, zero rows citing non-existent paragraphs, 100 % vocabulary validity, and median reviewer edits ≤ 20 % of rows |
| No auto-publish | No AI output reaches a tenant without human approval (NN-04); tests prove it |
| RBI library never stale *(v1.1)* | Every change in an RBI category page's "Updated as on" date is detected the same day and a change item opened; a new direction appears in tenants' catalogues as "New — checkpoints in preparation" within 1 business day (Appendix AB §AB.8) |
| Faster analyst work *(v1.1)* | Median analyst time per actionable change falls by ≥ 30 % against the v1.0 baseline through enrichment, similar-past-change pre-fill and sibling proposals (IMP-019, IMP-021) — measured per release |
| Less noise for clients *(v1.1)* | Updates for non-adopted instruments are collapsed; every update leads with a ≤ 60-word gist; "Accept impact" creates all impact tasks in one action (≤ 4 clicks from opening the update; IMP-022–IMP-025) |

---

## 2. Scope (in / out)

**In scope:** source registry operations (Appendix F), fetchers (RSS, HTML listings, PDF, e-Gazette, regulator e-mail alerts, licensed news feeds), scheduling (intraday + 20:00 IST reconciliation + weekly deep crawl), ingestion, hashing, de-duplication, text extraction (PDF text, OCR, HTML), metadata extraction, classification, addressee-to-family mapping, change items and their workflow, clause diff and concordance (old circular → new direction), impact mapping to checkpoints and tenants, content-release drafting from change items, regulator due-date extensions, horizon scanning of consultations and drafts, enforcement/penalty intelligence, the Updates inbox and delivery, the tenant change-implementation workflow and tracker, change-history views and reports, the AI Question Authoring Studio (platform and tenant), prompt and methodology registry, evaluation harness, cost controls. *(v1.1)* RBI category-page monitoring and catalogue automation; sibling-change proposals; concordance seeding and legacy re-citation; enrichment and similar-change retrieval; content-incident playbook; penalty-intelligence corpus; foreign-source monitoring via `REG_INTEL_PORT`; Regulatory Analyst agent; MCP read tools for Updates.

**Out of scope:** the importer and release mechanics (P03 — reused), compliance instance recalculation (P04 — consumes events), policy redlining (P07 — linked from impact tasks), general Vidhi chat and notebooks (P17), writing the Part-2 question sheets for every instrument (programme Part 2; the Studio accelerates it).

---

## 3. Personas and permissions touched

| Role | Responsibilities |
|---|---|
| `plt_content_maker` (regulatory analyst) | Triage detected items, run analysis, draft releases, run the AI Studio for platform content |
| `plt_content_checker` | Review change analyses, diffs and draft releases; approve |
| `plt_content_publisher` | Publish releases and the tenant-facing change note |
| `plt_super_admin` | Manage sources and schedules (Governed), AI prompt templates (Governed), emergency broadcast notices ("LawDocs notice" category) |
| `ten_admin` | Receives Updates; runs the AI Studio for tenant instruments (tenant-only); approves tenant releases; sets Update preferences for the organisation |
| `ten_cco` | Owns tenant impact assessments; assigns implementation tasks; signs off change implementation; reports to Board |
| `ten_dept_head`, `ten_maker` | Perform implementation tasks; read Updates relevant to their departments |
| `ten_kmp`, `ten_board_member` | Read Updates digests and the quarterly regulatory-change report |
| `dlv_rm`, `dlv_professional` | For retainer clients, prepare impact assessments and tenant question sheets as maker (client approves) |
| `svc_vidhi` | Summaries, diffs, mappings, draft question sheets — always drafts (NN-14) |
| Regulatory Analyst agent *(v1.1, D-34)* | Role agent sponsored by the content lead (platform) or the CCO (tenant): enrichment, summaries, concordance proposals, impact pre-fill, Studio drafts; autonomy L1 (platform analysis may reach L2 for creating draft change items) — never triages to NOT_RELEVANT, approves or publishes (NN-47, NN-50) |
| `prt_content_reviewer` *(v1.1)* | Reviewer of record for foreign packs; reviews change items for its jurisdiction and signs releases (P25; NN-53) |

---

## 4. Functional requirements

### 4A. Source registry and fetchers

**FR-P05-01 Source registry.** `chg.sources` (seeded from Appendix F): `source_id`, authority, name, URL, kind (RSS, HTML_LISTING, HTML_PAGE, PDF_INDEX, EGAZETTE_SEARCH, EMAIL_ALERT, API, NEWS_FEED), parser profile, priority (P1 core regulators, P2 ministries and standard-setters, P3 state departments and low-frequency sources), schedule class, freshness SLA, families affected, language, active flag, robots/terms notes, last_success_at, last_change_at, consecutive_failures. Adding or changing a source is a Governed change (P02).

**FR-P05-02 Fetch methods.**
- **RSS/Atom** (e.g., RBI `https://www.rbi.org.in/Scripts/rss.aspx`; SEBI `https://www.sebi.gov.in/sebirss.xml` covering press releases, circulars and orders): conditional GET (ETag/Last-Modified), item GUID de-duplication.
- **HTML listing pages** (e.g., RBI Notifications `NotificationUser.aspx`, Master Directions `BS_ViewMasterDirections.aspx`, Amendment Directions `Fs_AmendmentDirections.aspx`, Draft Directions RE-wise, Circulars Withdrawn; IFSCA `Home/NewSection`; IRDAI circular listings; MCA notifications; CRCS `circulars`): a parser profile per page (CSS/XPath selectors for date, title, link, reference, type), structural fingerprinting so that a page redesign is detected as `PARSER_BROKEN` rather than "no new items".
- **PDF retrieval**: follow item links to the PDF (e.g., `rbidocs.rbi.org.in/rdocs/notification/PDFs/…`), store the original, compute SHA-256; prefer the English version where a Hindi version is also published and store both.
- **e-Gazette** (egazette.gov.in) searches for Ministry notifications (MCA rules amendments, MeitY DPDP notifications, MoLE code rules) by ministry and date.
- **Regulator e-mail alerts**: subscribe a monitored mailbox where regulators offer e-mail alerts (e.g., IRDAI's e-mail alert registration on policyholder.gov.in; RBI notification subscription where available) and parse alerts as a redundant signal.
- **APIs** where offered (none assumed; [VERIFY] per authority).
- **Licensed news feeds** (P3 signal only, flag `chg.news.enabled` OFF until a licensed feed is contracted): business-news and legal-news feeds to catch announcements before formal publication; news items never create content changes on their own — they create a "watch" item that waits for the official instrument.

**FR-P05-03 Politeness and resilience.** Identified user agent, per-host rate limits (default ≤ 1 request / 3 s), respect for robots directives where applicable to public government pages, exponential backoff, rotating schedule windows, response-size limits, TLS verification, and an **egress allowlist** in production that explicitly includes every Appendix F host (note: `ifsca.gov.in` was observed blocked by an organisation egress allowlist in the owner's automation environment in September 2026 — production must allow it).

**FR-P05-04 RBI Master Directions category pages (Appendix AB §AB.8.1) *(v1.1)*.** Sources `SRC-RBI-30`…`SRC-RBI-52` (Appendix F §F.2A) monitor the RBI Master Directions category pages `BS_ViewMasterDirections.aspx?did=403`–`413` (DoR: commercial banks, SFBs, payments banks, LABs, RRBs, UCBs, RCBs, AIFIs, NBFCs, ARCs, credit information companies), `did=419`–`429` (DoS, same categories) and `did=338` (CEPD). Because RBI updates consolidated directions **in place**, the parser records per row: title, item id, reference, date of issue and the "Updated as on" date; a changed "Updated as on" date is the **primary change signal** and opens a CONSOLIDATION_UPDATE change item linked to the catalogue row and the matching amendment notification (where issued). New rows open NEW_INSTRUMENT items that also **create a catalogue row and instrument automatically** (coverage `PLANNED`, badge "New — checkpoints in preparation", production priority P2 by default, P1 when a compliance date falls within 90 days; Appendix AB §AB.8.3). Disappearing rows raise a "possibly superseded" flag for analyst review — never an automatic repeal; confirmed supersession runs the flow of FR-P05-48.

**FR-P05-05 Foreign and licensed sources (P25; NN-53, NN-54) *(v1.1)*.** Foreign official sources (Appendix F §F.12) are monitored like Indian ones, with the schedule anchored to the **authority's local timezone** (reconciliation at 20:00 local) and results surfacing in the content team's Radar at the next IST working window. Licensed regulatory-intelligence feeds connect through `REG_INTEL_PORT` (flag OFF per provider until contracted): a licensed signal creates a WATCH item that cannot become an Update until the official primary source is linked (LDC-CHG-121). Non-English instruments keep the official text; machine translations are labelled `MACHINE_UNREVIEWED` until a reviewer of record checks them (NN-54).

### 4B. Scheduling (D-18)

**FR-P05-10 Schedule classes.**

| Class | When | Sources |
|---|---|---|
| INTRADAY | Every 30 minutes 09:00–21:00 IST, hourly otherwise | P1 RSS feeds and listing pages (RBI notifications, master/amendment directions, press releases; SEBI RSS; IFSCA NewSection; IRDAI circulars; MCA notifications) |
| EVENING_RECONCILIATION | Daily 20:00 IST (start), with completion target 20:30 IST | Every active source: full listing scan for the last 14 days, diff against stored items, re-check of PDF hashes for items published in the last 7 days (catches silent replacements and corrigenda), freshness check |
| WEEKLY_DEEP | Sundays 03:00 IST | P3 sources (state co-op registrars, state labour departments), archive pages, "updated as on" consolidations, link-rot check of instrument source URLs |
| ON_DEMAND | Content maker action | Any source |

**FR-P05-11 Evening report.** At the end of EVENING_RECONCILIATION the system produces the **Regulatory Radar** for the day: new items per authority, items triaged/untriaged, failures, and stale sources. Internally it goes to the content team. Externally, tenants who opt in (`chg.radar.tenant_digest.enabled`, default ON) receive at ~20:30 IST a **Radar digest** containing only deterministic metadata of new official items relevant to their families — authority, title, reference, date, addressees and official link — labelled **"Detected today — LawDocs review pending"**. An AI one-line gist may be added only when flag `chg.radar.ai_gist.enabled` is ON (default OFF until the evaluation in §4K shows gist accuracy ≥ 97 % for two consecutive months), and is always labelled "automatic summary, not reviewed". Obligations never change through the Radar; they change only through reviewed releases (NN-04, NN-06, NN-34).

**FR-P05-12 Source health and back-fill (IMP-026) *(v1.1)*.** A source-health dashboard (SCR-CHG-04) shows freshness against SLA per source; an SLA breach on a P1 source raises a platform incident (P24 on-call). When a source recovers, a **back-fill scan** covers the whole outage window plus `chg.backfill.margin_days` (default 2) so nothing published during the outage is missed; back-filled items are marked and their detection lag is reported honestly in the monthly KPIs (Appendix F §F.17).

### 4C. Ingestion and classification

**FR-P05-20 Ingestion.** Each detected item becomes a `chg.detected_items` row: source, URL, title, published date (as printed), detected_at, raw object key (Object Lock), SHA-256, content type, language, duplicate_of (same hash or same reference number across sources), version_of (same URL with new hash → possible silent replacement/corrigendum).

**FR-P05-21 Text and metadata extraction.** Native PDF text extraction, OCR fallback for scanned documents (with confidence), HTML-to-text; metadata extraction for reference number (regex libraries per authority, e.g., `RBI/20\d\d-\d\d/\d+`, `DoR\.[A-Z.]+\.REC\.\d+/…`, `SEBI/HO/[A-Z-/]+/P/CIR/\d{4}/\d+`, `IFSCA/…`, `G\.S\.R\. \d+\(E\)`, `S\.O\. \d+\(E\)`), date, addressees ("All Non-Banking Financial Companies", "All Urban Co-operative Banks", "All Stock Brokers", "All IFSC Banking Units"), subject, instruments referenced, instruments superseded/repealed, effective date phrases ("with immediate effect", "from April 1, 2027"), and deadlines (comment-by dates for consultations).

**FR-P05-22 Classification.** `item_class`: NEW_INSTRUMENT, AMENDMENT, CONSOLIDATION_UPDATE ("updated as on"), CORRIGENDUM, REPEAL_WITHDRAWAL, FAQ_CLARIFICATION, CONSULTATION_DRAFT, DUE_DATE_EXTENSION, ENFORCEMENT_PENALTY (e.g., monetary penalties imposed on regulated entities — useful peer intelligence for risk and training), REGISTRATION_CANCELLATION (e.g., NBFC CoR cancellations), PRESS_RELEASE_INFO, PUBLICATION_REPORT, NON_ACTIONABLE (tenders, careers, events). `urgency`: IMMEDIATE (effective on issue or within 7 days), HIGH (≤ 30 days), NORMAL, LOW. `families[]` and `entity_types[]` via an addressee dictionary (e.g., "All NBFCs" → RBI-NBFC all layers; "All Primary (Urban) Co-operative Banks" → RBI-UCB; "Housing Finance Companies" → RBI-NBFC type HFC). Classification is AI-assisted with rules first (reference patterns and addressee dictionary) and a model second; the analyst confirms in triage.

**FR-P05-23 Enrichment (IMP-019) *(v1.1)*.** Before an item reaches triage, an enrichment step attaches context: the source PDF and its prior version (if any), the RBI category-page row and catalogue entry, related FAQs, the press release, linked consultations/drafts (horizon), amending notifications, and similar past change items (FR-P05-45). Every update card shows at least one linked context item or "none found". Enrichment is deterministic retrieval plus AI ranking; nothing in it changes content.

### 4D. Change items and workflow

**FR-P05-30 Change item.** A triaged detected item that matters becomes a `chg.change_items` record linking one or more detected items (e.g., a circular and its press release), with: class, urgency, families, affected instruments (existing) or new instrument, effective date(s), comment deadline (consultations), analyst, checker, status, SLA timers, analysis (§4E), draft release link (§4F), tenant note (§4G).

**FR-P05-31 States.**
```
DETECTED → TRIAGE
TRIAGE → NOT_RELEVANT (reason) | WATCH (news/consultation; revisit date) | INFO_ONLY | ACTIONABLE
INFO_ONLY → NOTE_DRAFTED → NOTE_REVIEWED → PUBLISHED_INFO
ACTIONABLE → ANALYSIS → DRAFT_RELEASE (P03 release in DRAFT) → IN_REVIEW → APPROVED → PUBLISHED → TENANTS_NOTIFIED → CLOSED
CONSULTATION_DRAFT → HORIZON (tracked until final instrument) → links to the final ACTIONABLE item
any → REOPENED (corrigendum or new information) — previous publication preserved
```
Timers: TRIAGE SLA 1 business day (IMMEDIATE: 4 hours, with pager alert to the on-duty analyst); ANALYSIS+DRAFT SLA by urgency (IMMEDIATE 1 business day, HIGH 3, NORMAL 10, LOW 20); IN_REVIEW 1 business day for IMMEDIATE/HIGH. Breaches escalate to the content lead and appear on the change dashboard.

**FR-P05-32 Due-date extensions.** DUE_DATE_EXTENSION items (e.g., an MCA general circular relaxing late fees or extending a filing date, a GST notification extending a return date) produce a structured extension (checkpoints, periods, new due date, conditions) that, after review, creates platform `cmp.due_overrides` (P04 FR-P04-13) and an Updates item; affected open instances recalculate.

**FR-P05-33 Enforcement intelligence.** ENFORCEMENT_PENALTY items (RBI/SEBI/IRDAI/IFSCA penalty orders and press releases) are tagged with the breached provision when stated; analysts link them to checkpoints. Tenants see "Peers penalised for this requirement in the last 24 months" on the checkpoint (names of penalised entities are public in regulator releases; display is factual, sourced and dated), which also feeds risk ratings (P08) and the savings model (P20). [VERIFY presentation with counsel; flag `chg.enforcement.show_entity_names` default ON for regulator-published names.]

**FR-P05-34 Penalty-intelligence corpus (G5 TM-398) *(v1.1)*.** A structured corpus `chg.enforcement_orders` (authority, order date, entity type, provision breached, penalty amount and currency, order type — monetary penalty, compounding, adjudication, cancellation, warning — source link, linked checkpoints) is built from RBI penalty press releases, SEBI adjudication and settlement orders, ROC/RD adjudication orders under the Companies Act (s.454), IRDAI and IFSCA orders, and Data Protection Board decisions once published. Uses: "enforced recently" badges on checkpoints; risk-rating calibration hints (P08); the penalty-exposure report and the savings model's evidence base (P28, Appendix N); the Board report's "peer enforcement" section. Amounts are shown only as published.

**FR-P05-35 Content-incident management (G5 TM-403) *(v1.1)*.** A wrongly published rule (wrong due date, wrong applicability, wrong citation) is a **content incident** with a playbook: (1) declare (any content role or a tenant report via support); (2) **blast-radius report** computed automatically — tenants and legal entities affected, instances created or recalculated, calendar entries pushed, notifications and Updates already sent; (3) contain — one-click **rollback** to the prior release version for future instances (completed instances untouched, NN-03), with a corrective release prepared in parallel; (4) notify — correction notice template to affected tenants through Updates (category LAWDOCS_NOTICE with "Correction" label) and, where dates moved, calendar corrections; (5) post-incident review within 5 business days with root cause and preventive actions, kept as evidence for ISO 27001/SOC 2 change management (P24). Severity S1 (statutory due date wrong for High-risk) requires containment within 4 hours.

### 4E. Analysis: summary, clause diff, concordance and impact

**FR-P05-40 Summary.** Vidhi produces a structured analysis draft: (1) one-paragraph summary; (2) who is affected (families, layers, types, thresholds); (3) what changes (bullets citing new paragraphs); (4) effective dates and transition provisions; (5) what is repealed or superseded; (6) actions an affected entity must take; (7) open questions/ambiguities for the analyst. Every bullet carries a citation to page and paragraph of the source (NN-06); the analyst edits and the checker approves the final text.

**FR-P05-41 Clause diff.** For AMENDMENT, CONSOLIDATION_UPDATE and CORRIGENDUM items, the system builds the new instrument version's clause index (P03 FR-P03-04) and aligns clauses to the previous version by (a) numbering, (b) heading, (c) text similarity, (d) explicit amendment instructions ("in paragraph 12, sub-paragraph (3) shall be substituted by …"). Output per clause: UNCHANGED, MODIFIED (word-level diff), INSERTED, DELETED, RENUMBERED (old → new path), MOVED. Amendment-instruction parsing applies textual amendments to the previous version to produce a **consolidated text** where the regulator has not yet published one, labelled "LDC working consolidation" until the regulator's own consolidation appears.

**FR-P05-42 Concordance for consolidations.** When a new instrument repeals and consolidates earlier instruments (the 28-Nov-2025 pattern), the analyst (with AI proposals) builds a **concordance table**: old instrument + paragraph → new instrument + paragraph, with status SAME_SUBSTANCE, MODIFIED, DROPPED, NEW. The concordance drives an automatic **re-citation** of existing checkpoints: each checkpoint linked to an old paragraph gets a draft new version citing the new paragraph (substance unchanged) or a review flag (modified/dropped). Where RBI published repeal lists with its drafts, they are loaded as evidence. Concordances are published to tenants as a browsable table ("Where did my old circular go?"; P03 SCR-CNT-19). *(v1.1)* Statuses extended to `SAME_SUBSTANCE`, `MODIFIED`, `MERGED`, `SPLIT`, `DROPPED`, `NEW` (Appendix AB §AB.5.1). **Seeding:** the 9,445 withdrawn circulars listed in the Annex to RBI/2025-26/100 are bulk-loaded as historical instruments (`WITHDRAWN_CIRCULAR`, status REPEALED) with RBI's numbers and dates; each consolidated direction's repeal paragraph and any consolidation footnote seed the instrument-level map; paragraph-level mapping is built **only** where LDC has legacy checkpoints or tenant overlays (Appendix AB §AB.5.3), and the legacy NBFC question banks are re-cited before Wave-1 GA (P03 FR-P03-58). The same mechanism handles the **IRDAI 2024 consolidation** of regulations (repeal/concordance mapping for insurers and intermediaries; G5 TM-699) and any future consolidation by SEBI, IFSCA or MCA.

**FR-P05-43 Checkpoint impact.** For each affected clause, the analysis lists impacted checkpoints with proposed action: KEEP, RE-CITE, MODIFY (draft new G/L/U/V/Q text), RETIRE, or NEW (draft rows for new obligations). The analyst opens these drafts in the P03 Content Studio; new rows can be generated with the AI Question Authoring Studio (§4H) scoped to the changed clauses only.

**FR-P05-44 Tenant impact.** At publication, the system computes affected tenants: tenants that adopted the instrument (direct), tenants whose profile matches the instrument's families/entity types but have not adopted it (new applicable instrument), and tenants with overlays on changed checkpoints (conflicts). For each tenant it precomputes counts: checkpoints changed/new/retired, open instances affected, overlays in conflict, policies linked to changed checkpoints (P07), committees linked (P06), returns affected (P11).

**FR-P05-45 Similar-past-change retrieval (IMP-021) *(v1.1)*.** For each new change item, the system retrieves analogous earlier change items (same instrument family and clause topic, same class, embedding similarity) and pre-fills the impacted-checkpoint list, action plan and tenant-note structure "based on" them, with links; the analyst accepts, edits or discards each pre-filled element.

**FR-P05-46 Sibling-change proposals (D-40) *(v1.1)*.** When a change affects a checkpoint with siblings in other RE categories (P03 FR-P03-09A) — typical when RBI updates the same subject for several categories on the same date — the system opens linked draft changes for each sibling instrument with the proposed edits, so one analysis serves all categories; each sibling still has its own diff, review and release (instruments stay separate).

**FR-P05-47 Per-release metrics (IMP-020) *(v1.1)*.** Each release records checkpoints affected, analyst and reviewer minutes, time from detection to publication, tenants reached, and tenant impact tasks closed within 30 days; shown on the change dashboard and used internally; any public statement of these metrics needs a Claims Register entry (NN-19).

**FR-P05-48 Supersession and withdrawal (Appendix AB §AB.8.4) *(v1.1)*.** When a direction is superseded (the March 2026 replacement of four dividend directions is the pattern), the old instrument becomes `SUPERSEDED` with `valid_to`; its checkpoints are re-cited through a concordance to the replacing direction or retired; tenant instances due after `valid_to` are cancelled with an explanation, completed instances remain (NN-29), and the catalogue coverage state becomes `SUPERSEDED`.

### 4F. Publication through the release pipeline

**FR-P05-50** An ACTIONABLE change item publishes only through a P03 content release (maker → checker → publisher). The release carries the change item ID, the approved tenant note, effective dates and impact. Publishing triggers P03 rebase, P04 instance recalculation for future periods, and the Updates fan-out (§4G). INFO_ONLY items publish an Updates note without content changes. Corrections after publication use a corrective release or a Correction Entry (D-02); the earlier note remains visible with a "corrected" marker.

### 4G. Updates inbox and delivery (R-090, NN-27)

**FR-P05-60 Data model.** `chg.updates` (platform-authored, tenant-targeted) and `chg.update_recipients` (tenant/user state: unread, read, acknowledged, actioned, dismissed with reason). Update categories:

| Category | Source | Typical action |
|---|---|---|
| REGULATORY_CHANGE | Published change item | Impact assessment |
| NEW_APPLICABLE_INSTRUMENT | Profile matches a non-adopted instrument | Adopt / decline with reason |
| CONTENT_RELEASE | LawDocs improved content without a regulatory change (e.g., better explanation, split rows) | Review (optional) |
| DUE_DATE_EXTENSION | Extension published | None (auto-applied) / acknowledge |
| CONSULTATION_HORIZON | Draft direction or consultation paper | Optional comment; plan |
| ENFORCEMENT_INSIGHT | Penalty on peers | Self-check task (optional) |
| RADAR_UNREVIEWED | Evening Radar items (opt-in) | Read; wait for review |
| LAWDOCS_NOTICE | Super-admin announcement (product, service, maintenance) | Read |

**FR-P05-61 The three-part note.** Every REGULATORY_CHANGE update shows: **What changed** (plain-language bullets with citations), **Why it matters to you** (computed from the tenant's profile and adoption: "You are an NBFC-ML; paragraphs 14–16 now apply to you from 1-Apr-2027"), **What to do** (prioritised actions with suggested owners and dates: adopt instrument, review 3 conflicting overlays, update the Fair Practices Code policy, table at next Board meeting, train collection staff). Plus: effective date(s), source links (official PDF and LDC working consolidation), the concordance where relevant, and the impact counts.

**FR-P05-62 Old vs new actionable.** A side-by-side table for each affected checkpoint: *Previous instrument & para | Previous actionable (as it applied to you, incl. your overlay) | New instrument & para | New actionable | Change type | What you need to do now*, exportable to Excel/PDF (R-006, R-088). Rows link to the checkpoint lineage (P03 SCR-CNT-15).

**FR-P05-63 Delivery.** In-app Updates inbox (megaphone icon; separate unread count); e-mail per preference (instant for IMMEDIATE/HIGH; daily or weekly digest otherwise); PWA push for IMMEDIATE; Microsoft Teams card (optional); calendar entries (P04 calendar service) for effective dates, transition deadlines and consultation comment deadlines, visible to the CCO and owners of affected departments; targeting by department (an update affecting only the IT and Risk departments goes to those heads plus the CCO; others can still browse). Preferences per user: categories, families, channels, digest times; organisation defaults by `ten_admin`; floor: CCO always receives REGULATORY_CHANGE for adopted instruments.

**FR-P05-64 Acknowledgement.** Tenants acknowledge REGULATORY_CHANGE updates (CCO or delegate); unacknowledged IMMEDIATE/HIGH updates escalate at T+2 and T+5 business days to the CCO and `ten_admin`; acknowledgement and dismissal reasons are audited.

**FR-P05-65 Less noise, more action (IMP-022–IMP-025) *(v1.1)*.** (a) The Updates inbox shows by default only updates for **adopted** instruments and families; "not applicable to you" items sit in a collapsed section with a count (a tenant can expand or subscribe). (b) **Summary first:** each update opens with a gist of at most 60 words (AI draft labelled "unreviewed" until the checker approves; reviewed gists carry the reviewer's initials) and an expandable detail. (c) **Three-pane view** for each changed checkpoint: previous text | new text | actionable diff, with "what to do" and the tenant's due date (IMP-023; complements FR-P05-62). (d) **Accept impact:** one action creates all proposed impact tasks with owners from the department map and due dates from the effective date, after a preview; the CCO can untick tasks before confirming (≤ 4 clicks from opening the update).

**FR-P05-66 Push form for LawDocs notices and targeted pushes (G5 TM-457, TM-285) *(v1.1)*.** A super-admin push (category LAWDOCS_NOTICE or a manual regulatory alert) must set at least one targeting dimension — entity family/type, regulator domain, or named tenants — and shows an **audience preview** ("will reach 142 entities / 1,318 users") before sending; options: recurrence "remind until acknowledged" or "until effective date", and a **"link a task"** toggle that creates a task in each recipient tenant's CCO inbox. Pushes to all tenants need a second approver (§10). **Per-user per-domain mute** lets a user silence a regulator domain or category in Updates for non-mandatory items; CRITICAL updates and the CCO floor for adopted instruments cannot be muted; mutes are audited.

### 4H. AI Question Authoring Studio (R-085)

**FR-P05-70 Purpose.** Convert an uploaded instrument into a draft compliance-question workbook in the correct family template, following the owner's question-writing methodology, so that the owner (platform) or a client admin (tenant) can verify and publish it after confirmation. The Studio is the in-product version of the owner's Part-2 commands, improved.

**FR-P05-71 Inputs.**
- Instrument file(s): PDF, DOCX, HTML, or a URL from the source registry; for tenant use, any document the tenant owns or is subject to (an RBI MD it considers important, an IFSCA circular, a lender covenant, its own policy).
- Family template from the Template Registry (auto-suggested from the instrument's authority and addressees; tenant runs default to the tenant's family).
- **Methodology profile** (versioned; §4I) — the generation rules.
- Optional exemplar: an approved sheet of the same family (e.g., "05 Insurance – IFSCA Appointed Actuary Regulations 2022") used as a style example.
- Options: split bundled sub-clauses (default ON — the owner's rule that a paragraph listing a policy's contents or a committee's responsibilities becomes one row per sub-clause); include suggestive/good-practice rows (default ON, labelled Suggestive Compliance); explanation depth (STANDARD — 2–4 sentences; DETAILED — full paragraph analysis as in the IFSCA Appointed Actuary sheet); scope (whole instrument or selected chapters/clauses, used by §4E for changed clauses only); target departments list (tenant's renamed departments for tenant runs).

**FR-P05-72 Pipeline.**
1. **Extract and index**: P03 clause index (with OCR if needed); the user confirms the structure if confidence is low.
2. **Classify clauses**: OBLIGATION, CONDITIONAL_OBLIGATION, DEFINITION, PROCEDURAL_AUTHORITY (powers of the regulator), EXEMPTION, TRANSITION, NON_ACTIONABLE.
3. **Generate rows** per OBLIGATION/CONDITIONAL_OBLIGATION clause using structured output (JSON schema = the template's content columns: B, C, D, F, G, H, K, L, M, N, O, P, Q, R, S, U, V; columns A, E, I, J, T, W–AD are not generated and are left blank exactly as the owner's commands require). Values for C, D, H, M, O and R must be chosen from the family vocabulary supplied in the prompt; multi-value D allowed. K must quote the paragraph exactly as printed (e.g., "Reg. 4(3)", "Para 12(3)(a)"). G is phrased as a question ("Has the <entity> …?") or an actionable. L explains in plain language. Q states consequences, citing the instrument's penalty provision or the parent Act's penal section when the instrument has none. U names the evidence document; V tells the maker what to do. Exemptions/thresholds go to S.
4. **Self-review pass** (second model call with a reviewer prompt): checks each row's citation against the clause text, flags bundled sub-clauses not split, flags rows with no evidence or control activity, checks coverage (every OBLIGATION clause has ≥ 1 row), and proposes fixes; a deterministic validator then runs the P03 V-rules and L-lint.
5. **Assemble the workbook** from the registered blank template (exact row-1/row-2 headers, `Rough` lists, named ranges, data validation, `_Template_Info` with `generated_by = AI_STUDIO`, prompt/methodology version, model ID, run ID).
6. **Present** in the Studio grid with source-linked citations (click a row → highlighted clause), coverage map, confidence per row, and diff to any existing checkpoints of the same instrument.
7. **Export → verify → re-upload**: the user may edit in the grid or download the workbook, edit in Excel, and re-upload; the importer diffs the edited workbook against the AI draft and records every change (this diff is the evaluation signal, §4K).
8. **Confirm and publish**: platform runs enter a P03 release (checker and publisher approval); tenant runs publish to the tenant only after approval by a second tenant user (`ten_cco`/`ten_admin`), never to other tenants.

**FR-P05-73 Tenant runs (client admin).** Same pipeline in the tenant scope: instrument stored as a tenant instrument; rows become tenant checkpoints; tenant departments used in M; results visible only to the tenant; usage metered (pages processed, rows generated) against the plan's AI quota (P20). A tenant may **suggest the instrument to LawDocs** (explicit consent; only the official instrument file is shared, never the tenant's rows unless the tenant ticks "share my draft"), creating a platform triage item.

**FR-P05-74 Long instruments.** Instruments over the model's practical context are processed chapter by chapter with a shared definitions/context block (prompt caching of template, vocabulary and methodology); very large batches (e.g., the full RBI catalogue — 240 live consolidated DoR directions plus later DoR, 64 DoS and CEPD directions, 320 rows in all; *v1.1*) use the provider's batch interface with per-instrument runs; partial failures resume per chapter. For clone-and-adapt work across RE categories (Appendix AB §AB.7.4), the Studio accepts an approved sibling sheet as the exemplar and the new category's direction as the source, and marks each row CLONED-UNCHANGED, CLONED-ADAPTED or NEW so reviewers focus on differences.

**FR-P05-75 Provider and data handling.** Calls go through the P17 provider adapter (D-14 as amended by master X-03): platform runs on public regulator documents may use either route; any tenant run, or any run that includes tenant documents, uses Claude via Amazon Bedrock India geographic cross-Region inference only and never fails over to a non-India route (NN-41), with zero-retention or minimum-retention settings where contractually available, no training on tenant content (NN-15), tenant documents sent only for tenant runs, platform instruments (public regulator documents) for platform runs. Every run logs model, version, parameters, prompt template version, input hashes, output hash, token counts, cost, duration, user, and the human decisions taken on the output (NN-14).

**FR-P05-76 Row quality scoring (IMP-027) *(v1.1)*.** Before human review, every draft row is scored against the Part-2 QA checklist (`part2_prompts/99_QA_Checklist_for_Question_Sheets.md`) as deterministic checks where possible — citation present and resolving, one actionable, evidence named specifically (not "relevant documents"), control activity present, vocabulary valid, no withdrawn instrument cited (NN-55), Column N conventions (`SUPERSEDES:`, `TEXT: updated as on`, `CATALOGUE: <S.No>`, `Sibling:`; Appendix E §E.4.6), risk calibration — and as model-judged checks for plain-language quality. Rows failing a hard check cannot be approved until fixed; the score is visible per row and per sheet.

**FR-P05-77 Families and autonomy *(v1.1)*.** The Studio covers all 26 families of Appendix E, including `INTL-GEN` (foreign sheets carry the reviewer line in column N, V-23) and `AI-GOV` (AI-governance overlay, D-36). Studio and analysis agents run at autonomy L1 (draft only); no level permits publication (NN-04, NN-50); every methodology, prompt or model change passes the §4K gates before promotion.

### 4I. Methodology profiles and prompt registry

**FR-P05-80 Methodology profile.** A versioned, Governed artefact per family (and a common base) capturing the owner's rules from the NBFC and IFSCA commands, improved:
- one actionable per row; split bundled sub-clauses (policy contents, committee responsibilities, report matters, risk thresholds);
- cover every direction/guideline/compliance mentioned in the text, including obligations stated in Annexes, Schedules, Forms and FAQs that form part of the instrument;
- column-by-column rules (as in FR-P05-72 step 3), with the owner's statement that the maker's evidence must be identified for every row ("every compliance should be having some document to be uploaded as a proof");
- exact citation format per authority (RBI "Para x(y)(z)"; SEBI "Regulation x(y)" / "Para x of Master Circular"; IFSCA "Reg. x(y)"; Companies Act "Section x(y) read with Rule z"; labour codes "Section x of the Code on Wages, 2019 read with Rule y");
- frequency selection rules (event-based where the trigger is an event; ongoing where continuous; one-time for registrations);
- risk rating guidance (High where non-compliance can lead to cancellation of registration, monetary penalty above a threshold, prosecution, or customer harm; Medium for reporting/process lapses; Low for documentation good practice) — tenant-adjustable afterwards;
- plain-language guidance for L and V (reading level, no legalese, explain defined terms);
- consequences guidance for Q (cite penalty provisions; avoid speculative amounts);
- department mapping guidance per family vocabulary;
- forbidden behaviours: inventing paragraph numbers, citing repealed instruments as current, filling user columns, using values outside vocabularies, merging distinct obligations.
The seed profile is the text of `part2_prompts/00_Part2_Master_Command.md` (entry `QUESTION_GEN/question_authoring_v1`) with each family variant seeded from `part2_prompts/01–24`; the QA rules of `99_QA_Checklist_for_Question_Sheets.md` become the deterministic self-review checks. Profiles are stored in `ai.prompt_templates` with family variants, changelog, owner approval, and evaluation results; promotion of a new version requires passing §4K thresholds and maker-checker approval (`plt_super_admin` + content lead).

### 4J. Tenant change-implementation workflow

**FR-P05-90 Impact assessment.** From an Updates item the CCO opens **Assess impact** (or assigns it): applicability confirmation (Applies / Partially / Does not apply — with reason), affected departments, processes, systems, products, policies (auto-listed from P07 links), committees (P06), returns (P11), training needs (P21 academy link), customer communication needs, Board/Committee approval needed (Y/N), implementation plan (tasks with owners and dates — created in P04 Tasks), target completion date (default the effective date), and sign-off. Vidhi pre-fills a draft from the tenant's data.

**FR-P05-91 Implementation tracker.** `chg.tenant_change_impl` with status NOT_STARTED, ASSESSING, PLANNED, IN_PROGRESS, IMPLEMENTED, VERIFIED (CCO or internal audit), NOT_APPLICABLE, OVERDUE; dashboard per CCO with ageing and effective-date proximity; Board report section "Regulatory changes in the period and implementation status" (consumed by P04 FR-P04-92 and the P06 Board pack).

**FR-P05-92 Change history per checkpoint and per instrument.** Views and exports showing every change item affecting the checkpoint/instrument, with the previous direction/actionable, new direction/actionable, release, reviewer, publication date, tenant acknowledgement, impact assessment and implementation status — the "what was the previous direction or actionable and what is the update" record the owner requested (R-006, R-088).

### 4K. Evaluation harness

**FR-P05-100 Golden set.** Owner-approved workbooks (the 13 IFSCA sheets in `IFSCA Documents`, the two 25-Oct-2026 samples, the nine RBI NBFC Master-Direction sheets of 31-Jul-2026 (RBI/DoS/2026-27/460–468)) with their source instruments form the initial golden set; every approved Studio output adds to it (with the human-edited version as the reference).

**FR-P05-101 Metrics.** Clause-coverage recall (obligation clauses covered / total), citation accuracy (row K resolves to the correct clause), hallucinated-citation rate (must be 0), vocabulary validity (100 %), split compliance (bundled sub-clauses split), row-level edit rate (rows changed by reviewers), field-level edit rates (G, L, Q, U, V), mean reviewer time per 100 rows, and cost per 100 rows. For the Radar gist and change summaries: factual-consistency score judged against source by reviewers on a weekly sample.

**FR-P05-102 Gates.** A methodology/prompt/model change is promoted only if it is no worse than the current version on every safety metric (hallucinated citations = 0, vocabulary validity = 100 %) and meets the outcome thresholds in §1; results are recorded in `ai.eval_runs` and shown in the Console.

**FR-P05-103 Agent evaluation and regression (NN-50) *(v1.1)*.** The Regulatory Analyst agent's skills (classification, enrichment ranking, summary, concordance proposal, impact pre-fill, sibling proposal) each have golden sets and thresholds (e.g., concordance pair precision ≥ 0.9 at the confidence shown; summary factual consistency ≥ 97 %); a model or prompt upgrade is promoted only after a regression run against all skill sets and a shadow period of two weeks on live items without user exposure (Appendix AA).

### 4L. MCP tools for Updates (NN-52) *(v1.1)*

**FR-P05-110** *(v1.1, X1: names aligned with Appendix AA §AA.7.4.)* Read tools on the LDC MCP server, under the calling user's permissions and preferences: `list_updates(filters)` (adopted-instrument updates with gist, urgency, effective dates, acknowledgement state), `get_update_impact(update_id)` (three-part note, old-vs-new table, citations), `lookup_concordance(old_ref)` ("where did my old circular go?"), `list_horizon()` (consultations with comment deadlines). Draft tool (L1): `draft_impact_assessment(update_id)`. No tool acknowledges, dismisses or signs off.


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P05-X01 — DPDP Schedule amendments.** When a published Update amends the DPDP Act, the DPDP Rules or their Schedules, P05 triggers P12's data-compliance tree generator (P12 §4R) for every affected tenant and shows the resulting change set as an impact task (NN-34: no automatic change to tenant instances).

**FR-P05-X02 — Supervisory Returns amendments.** For changes to any RBI Supervisory Returns Directions (catalogue rows of the 31 Jul 2026 DoS set), the change item lists the affected `ret.return_definitions` so that P11 can version cell maps and lead-time data requests (P11 FR-P11-81).

**FR-P05-X03 — Public tracker feed.** `cnt.CoverageStateChanged` and `chg.InstrumentCatalogued` are published (metadata only) to the public RBI Directions Tracker in P23; unreviewed items are never shown publicly.

---

## 5. Workflows and state machines

### 5.1 Detected item → change item (see FR-P05-31 for states)

```
fetch(source) ─► new/changed item? ─no─► record heartbeat (last_success_at)
                       │yes
                       ▼
   store raw (Object Lock) + hash ─► dedupe/version_of ─► extract text & metadata ─► classify (rules → model)
                       ▼
   TRIAGE queue (priority by urgency × families × tenant reach)
     ├─ NOT_RELEVANT (reason)                ├─ WATCH (revisit date)
     ├─ INFO_ONLY → note → review → publish  └─ ACTIONABLE → ANALYSIS → DRAFT_RELEASE → review → PUBLISHED → fan-out
```

### 5.2 Publication fan-out (Temporal `ChangePublicationWorkflow`)

1. Activate release (P03) — idempotent.
2. For each affected tenant (batched): rebase overlays (P03), recompute future instances (P04), create Updates items with tenant-specific "why it matters" and impact counts, create calendar entries for effective/transition dates, deliver per preferences.
3. Emit the internal event `in.lawdocscomply.chg.ChangePublished.v1`; the `int` module publishes the Ecosystem event `in.infrabyx.grc.ObligationPublished.v1` (changes) to subscribed products (master X-01).
4. Compensation: a tenant whose fan-out fails is retried with backoff and listed on the change dashboard; no tenant receives a partial update (the Updates item is created only after rebase and recompute succeed for that tenant).

### 5.3 Tenant Updates item

```
DELIVERED → READ → ACKNOWLEDGED → (impact assessment) ASSESSING → PLANNED → IN_PROGRESS → IMPLEMENTED → VERIFIED
DELIVERED/READ → DISMISSED (non-mandatory categories only; reason)
ACKNOWLEDGED → NOT_APPLICABLE (reason; CCO)
Escalation: IMMEDIATE/HIGH not acknowledged at T+2 and T+5 business days; implementation OVERDUE at effective date
```

### 5.4 AI Studio run

```
CREATED → EXTRACTING → INDEXED (user confirms structure if confidence < threshold) → GENERATING (per chapter) → SELF_REVIEW → VALIDATING → DRAFT_READY
DRAFT_READY → (edit in grid | export → offline edit → re-upload) → EDITED → SUBMITTED → IN_REVIEW → APPROVED → (platform) RELEASED | (tenant) PUBLISHED_TENANT
any → FAILED (resumable per chapter) | CANCELLED
```
Guards: SUBMITTED requires zero blocking V-errors; APPROVED requires approver ≠ the user who ran or edited the draft (NN-05); no transition to RELEASED/PUBLISHED_TENANT without APPROVED (NN-04).

### 5.4A RBI category-page row *(v1.1)*

```
ROW_SEEN(first time) → NEW_INSTRUMENT item → catalogue row PLANNED
ROW_UPDATED_AS_ON(changed date) → CONSOLIDATION_UPDATE item → diff v(n)→v(n+1) → sibling proposals → release
ROW_MISSING(previously listed) → POSSIBLY_SUPERSEDED flag → analyst confirms → SUPERSEDED (FR-P05-48) | false alarm (parser) 
```

### 5.4B Content incident *(v1.1)*

```
DECLARED → BLAST_RADIUS_COMPUTED → CONTAINED (rollback for future instances; corrective release drafted) → TENANTS_NOTIFIED → CORRECTED (release published) → REVIEWED (post-incident review filed) → CLOSED
```
Timers: S1 containment ≤ 4 h; S2 ≤ 1 business day; review ≤ 5 business days.

### 5.5 Source health

```
HEALTHY → DEGRADED (1 failure or parser fingerprint drift) → FAILING (≥ 3 consecutive failures or SLA breach → P2 alert) → HEALTHY (success)
HEALTHY → PARSER_BROKEN (structure changed; zero items where history predicts items) → manual fix → HEALTHY
```

---

## 6. Screens and UX

| Screen ID | Name | Menu path | Roles | Key elements |
|---|---|---|---|---|
| SCR-CHG-01 | Change dashboard | Console › Regulatory change › Dashboard | content team | Today's Radar, triage queue size, SLA breaches, source health heatmap, items by authority, publication lead times |
| SCR-CHG-02 | Triage queue | Console › Regulatory change › Triage | `plt_content_maker` | Items with source, class/urgency proposals, addressees, families; actions: Not relevant / Watch / Info / Actionable; merge duplicates |
| SCR-CHG-03 | Change item workspace | Triage › *item* | content team | Source PDF viewer, metadata, AI analysis (editable, cited), clause diff viewer (side-by-side and inline), concordance editor, impacted checkpoints with proposed actions, draft release link, tenant note editor with preview per sample tenant profile |
| SCR-CHG-04 | Sources | Console › Regulatory change › Sources | `plt_super_admin`, content lead | Registry, schedules, parser profiles, test-fetch, health history |
| SCR-CHG-05 | Horizon | Console › Regulatory change › Horizon | content team | Consultations and drafts with comment deadlines, expected finalisation, linked items |
| SCR-CHG-10 | Updates inbox | Megaphone icon; Compliance › Updates | tenant users | Categories tabs, unread counts, filters (authority, family, department, urgency), three-part note, actions |
| SCR-CHG-11 | Update detail | Updates › *item* | tenant users | What changed / why it matters / what to do; old vs new actionable table; concordance; effective dates; Acknowledge; Assess impact; Adopt; Open conflicts; Export |
| SCR-CHG-12 | Impact assessment | Update detail › Assess impact | `ten_cco`, delegates, `dlv_rm` | Form per FR-P05-90 with Vidhi pre-fill; tasks generator; sign-off |
| SCR-CHG-13 | Change implementation tracker | Compliance › Regulatory changes | `ten_cco`, dept heads, IA, Board (read) | Status board, ageing, effective-date countdown, export, Board report section |
| SCR-CHG-14 | Change history | Checkpoint/instrument › Change history | tenant roles | Timeline and table of previous vs new; export PDF/Excel |
| SCR-CHG-15 | Update preferences | Profile › Updates; Settings › Updates (org defaults) | users / `ten_admin` | Categories, families, channels, digest times, department targeting |
| SCR-AIS-01 | AI Question Authoring Studio | Console › Content › AI Studio; Tenant › Compliance › Regulations › Create questions with Vidhi | `plt_content_maker`; `ten_admin`, `ten_cco`, `dlv_rm` | Upload/select instrument; template and methodology selection; options; run progress per chapter; cost estimate before run |
| SCR-AIS-02 | Draft review grid | AI Studio › *run* | same | Rows with confidence, citations linked to source, coverage map, lint, diff vs existing; Export Excel; Re-upload; Submit |
| SCR-AIS-03 | Methodology & prompts | Console › Content › AI Studio › Methodology | `plt_super_admin`, content lead | Profiles per family, versions, changelog, evaluation results, promote/rollback |
| SCR-CHG-06 *(v1.1)* | RBI category monitor | Console › Regulatory change › RBI directions | content team | 23 category pages with last scan, "Updated as on" changes, new rows, missing rows, linked catalogue rows and change items |
| SCR-CHG-07 *(v1.1)* | Content incidents | Console › Regulatory change › Incidents | content lead, super admin | Declare, blast-radius report, rollback, notices, post-incident review |
| SCR-CHG-08 *(v1.1)* | Enforcement corpus | Console › Regulatory change › Enforcement | content team | Orders by authority, provision, amount, linked checkpoints; tenant-facing badges preview |
| SCR-CHG-09 *(v1.1)* | Push composer | Console › Updates › New notice | super admin (+ approver) | Targeting dimensions, audience preview, recurrence, link-a-task, second approval for all-tenant pushes |
| SCR-AIS-04 | Evaluation | Console › Content › AI Studio › Evaluation | content lead | Golden set, metric trends, per-run comparison |

UX rules: Updates items lead with the three-part note in ≤ 120 words before details; urgent items use a banner on the dashboard until acknowledged; the old-vs-new table highlights changed words; "i" help keys `chg.class.<code>`, `chg.category.<code>`; the Studio shows a cost/time estimate before running and a plain-language explanation of what the AI will and will not do ("Vidhi drafts; you approve. Nothing is published until a second person approves.").

---

## 7. Backend design

### 7.1 Modules
`chg` (sources, fetchers, detected items, change items, updates, tenant implementation), `ai` (Studio runs, prompt templates, evaluation), with `cnt`/`tpl` (versions, clauses, releases, importer), `wf` (tasks, calendar, notifications for delivery), `dms` (raw files), `int` (outbound events, Teams cards).

### 7.2 Tables (key columns)

| Table | Key columns |
|---|---|
| `chg.sources` | source_id, authority_id, kind, url, parser_profile JSONB, priority, schedule_class, sla_minutes, families[], active, last_success_at, last_change_at, consecutive_failures, health |
| `chg.fetch_runs` | run_id, source_id, started_at, ended_at, status, items_seen, items_new, http_status, error |
| `chg.detected_items` | item_id, source_id, url, title, published_on, detected_at, raw_object_key, sha256, language, ref_no, addressees[], item_class, urgency, families[], duplicate_of, version_of, triage_state |
| `chg.change_items` | change_id, item_ids[], class, urgency, families[], instrument_ids[], new_instrument_id, effective_dates JSONB, comment_deadline, analyst_id, checker_id, state, sla_due_at, release_id, analysis JSONB, tenant_note JSONB |
| `chg.clause_diffs` | change_id, old_version_id, new_version_id, clause_lineage_id, diff_type, old_path, new_path, diff JSONB |
| `chg.concordance` | change_id, old_instrument_id, old_ref, new_instrument_id, new_ref, status |
| `chg.updates` | update_id, category, change_id, release_id, title, note JSONB (what/why/what-to-do template), urgency, effective_dates, created_by, published_at |
| `chg.update_recipients` | update_id, tenant_id, user_id nullable, why_matters JSONB, impact_counts JSONB, state, acknowledged_by, acknowledged_at, dismissed_reason |
| `chg.tenant_change_impl` | impl_id, tenant_id, update_id, applicability, departments[], plan JSONB, task_ids[], target_date, state, signed_off_by |
| `ai.prompt_templates` | template_id, family_code, kind (QUESTION_GEN, SELF_REVIEW, SUMMARY, DIFF_EXPLAIN, RADAR_GIST), version, body, vocab_binding, state, approved_by, eval_run_id |
| `ai.studio_runs` | run_id, scope (PLATFORM/TENANT), tenant_id, instrument_version_id, template_code, methodology_version, options JSONB, model_id, state, chapters JSONB, tokens_in, tokens_out, cost, output_workbook_key, import_job_id |
| `ai.eval_sets` / `ai.eval_runs` | golden items / metrics JSONB, compared_to, decision |
| `chg.rbi_page_rows` *(v1.1)* | page_did, item_id, title, reference, issue_date, updated_as_on, first_seen_at, last_seen_at, catalogue_sno, state |
| `chg.enforcement_orders` *(v1.1)* | order_id, authority, order_date, entity_type, provision_refs[], amount, currency, order_type, source_url, checkpoint_ids[] |
| `chg.content_incidents` *(v1.1)* | incident_id, severity, release_id, declared_by, blast_radius JSONB, rollback_release_id, corrective_release_id, notice_update_id, review_doc_id, state |
| `chg.enrichment_links` *(v1.1)* | change_id, link_type (PRIOR_VERSION, FAQ, PRESS_RELEASE, CONSULTATION, AMENDING_NOTIFICATION, SIMILAR_CHANGE), target_ref, rank |
| `chg.release_metrics` *(v1.1)* | release_id, checkpoints_affected, analyst_minutes, reviewer_minutes, detect_to_publish_hours, tenants_reached, impact_tasks_closed_30d |
| `chg.update_mutes` *(v1.1)* | user_id, domain, category, created_at |

### 7.3 APIs

Console: `GET/POST /chg/sources` · `POST /chg/sources/{id}/test-fetch` · `GET /chg/items?state=TRIAGE` · `POST /chg/items/{id}/triage` · `GET/PUT /chg/changes/{id}` · `POST /chg/changes/{id}/analyse` · `POST /chg/changes/{id}/concordance` · `POST /chg/changes/{id}/draft-release` · `POST /chg/updates` (info notes, LawDocs notices).
Tenant: `GET /updates?category&state` · `GET /updates/{id}` · `POST /updates/{id}/acknowledge|dismiss` · `POST /updates/{id}/impact` · `GET /changes/implementation` · `GET /checkpoints/{id}/change-history?format=pdf|xlsx` · `PUT /updates/preferences`.
AI Studio: `POST /ai/studio/runs` (instrument ref or upload, template, options; returns cost estimate first with `dry_run=true`) · `GET /ai/studio/runs/{id}` · `GET /ai/studio/runs/{id}/workbook` · `POST /ai/studio/runs/{id}/reupload` · `POST /ai/studio/runs/{id}/submit`. *(v1.1)* Console: `GET /chg/rbi-pages` · `POST /chg/incidents` · `GET /chg/incidents/{id}/blast-radius` · `POST /chg/incidents/{id}/rollback` · `GET/POST /chg/enforcement-orders` · `POST /chg/pushes` (with `preview=true` returning the audience count) · `POST /chg/changes/{id}/siblings`. Tenant: `POST /updates/{id}/accept-impact` (preview + confirm) · `PUT /updates/mutes`.

### 7.4 Domain events
`in.lawdocscomply.chg.ItemDetected.v1`, `…chg.ChangeItemTriaged.v1`, `…chg.ChangePublished.v1`, `…chg.DueDateExtensionPublished.v1`, `…chg.UpdateDelivered.v1`, `…chg.UpdateAcknowledged.v1`, `…chg.ImpactAssessmentSignedOff.v1`, `…chg.ChangeImplemented.v1`, `…chg.SourceHealthChanged.v1`, `…ai.StudioRunCompleted.v1`, `…ai.PromptTemplatePromoted.v1`; *(v1.1)* `…chg.RbiPageRowChanged.v1`, `…chg.InstrumentCatalogued.v1`, `…chg.InstrumentSuperseded.v1`, `…chg.ContentIncidentDeclared.v1`, `…chg.ContentIncidentClosed.v1`, `…chg.EnforcementOrderRecorded.v1`, `…chg.ImpactAccepted.v1`; Ecosystem: `RegulatoryChange` resource events per Integration Spec §9.2 (`ObligationPublished` (changes)).

### 7.5 Jobs / Temporal
`SourcePollWorkflow` (per schedule class), `EveningReconciliationWorkflow` (cron `0 20 * * *` Asia/Kolkata; completion SLA 30 min; report), `WeeklyDeepCrawl`, `IngestItemWorkflow`, `AnalyseChangeWorkflow` (AI summary, diff, impacted checkpoints), `ChangePublicationWorkflow` (§5.2), `UpdateDigestJob` (per user schedule), `AckEscalationJob`, `StudioRunWorkflow` (per chapter, resumable, batch mode), `EvalNightly`; *(v1.1)* `RbiCategoryPageMonitor` (INTRADAY + EVENING), `BackfillScan` (on source recovery), `EnrichmentWorkflow`, `SiblingProposalWorkflow`, `SupersessionWorkflow`, `ContentIncidentWorkflow` (blast radius, rollback, notices), `EnforcementCorpusIngest` (daily), `ForeignSourcePoll` (per authority timezone), `AgentRegressionRun` (on model/prompt change).

---

## 8. Integrations

- **Official sources:** Appendix F (HTTP fetchers via the egress proxy; e-Gazette; regulator e-mail alerts to a monitored mailbox).
- **News (optional):** licensed feed adapter `NEWS_FEED_PORT` (flag OFF).
- **AI provider:** P17 `LLM_PORT` (Claude primary, D-14); `OCR_PORT` for scanned documents.
- **Delivery:** P04 notification service (e-mail, push, Teams, WhatsApp/SMS where enabled), P04 calendar service.
- **Ecosystem:** Finbyx and Udofin subscribe to `ObligationPublished`/`RegulatoryChange`; Finbyx M14 compliance module can display LDC Updates for tenants in LDC_EXTERNAL/LDC_GROUP mode (Integration Spec §9.1).
- **P07 policies:** impact tasks deep-link to the policy redline workspace; P06: "table at next Board meeting" creates a draft agenda item.
- *(v1.1)* **`REG_INTEL_PORT`:** licensed regulatory-intelligence providers for foreign jurisdictions (flag OFF per provider; P25, Appendix Y); signals only.
- *(v1.1)* **P23 public RBI Directions Tracker:** consumes `InstrumentCatalogued` and `CoverageStateChanged` to show titles, dates, last updated and LDC coverage (lead magnet; no tenant data).
- *(v1.1)* **P28:** penalty-exposure and regulatory-change reports read `chg.enforcement_orders` and `chg.tenant_change_impl`.

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `chg.schedule.intraday_minutes` | G | 30 (09:00–21:00 IST), 60 otherwise | 15–240 | super admin |
| `chg.schedule.reconciliation_time` | G | 20:00 Asia/Kolkata | 18:00–23:00 | super admin |
| `chg.reconciliation.lookback_days` | G | 14 | 3–60 | super admin |
| `chg.sla.triage_hours.immediate` | G | 4 | 1–24 | content lead |
| `chg.sla.publish_business_days` | G | IMMEDIATE 1, HIGH 3, NORMAL 10, LOW 20 | — | content lead |
| `chg.radar.tenant_digest.enabled` | T | ON | — | `ten_admin` / user |
| `chg.radar.ai_gist.enabled` | G | OFF | ON only after eval gate | super admin + content lead |
| `chg.news.enabled` | G | OFF | requires licensed feed | super admin |
| `chg.enforcement.show_entity_names` | G | ON | — | super admin (counsel) |
| `chg.updates.ack_required_categories` | T | REGULATORY_CHANGE, NEW_APPLICABLE_INSTRUMENT | must include REGULATORY_CHANGE for adopted instruments (floor) | `ten_admin` |
| `chg.updates.ack_escalation_days` | T | 2, 5 business days | ≤ 10 | `ten_cco` |
| `chg.updates.department_targeting` | T | ON | — | `ten_admin` |
| `chg.updates.digest_time` | T | 20:30 Asia/Kolkata (after the 20:00 reconciliation; NN-27) | 18:00–23:59 or next-morning 07:00–10:00 | user |
| `ai.studio.enabled_tenant` | T | ON (plan-gated) | — | `ten_admin` (plan in P20) |
| `ai.studio.max_pages_per_run` | G | 400 | 50–2,000 | super admin |
| `ai.studio.default_explanation_depth` | T | STANDARD | STANDARD, DETAILED | `ten_admin` |
| `ai.studio.split_subclauses` | T | ON | ON (L for platform runs) | `ten_admin` (tenant runs) |
| `ai.studio.include_suggestive` | T | ON | — | user per run |
| `ai.studio.structure_confirm_threshold` | G | 0.85 OCR/structure confidence | 0.6–0.99 | content lead |
| `ai.eval.promotion_thresholds` | G | per §1 and FR-P05-102 | cannot relax zero-hallucinated-citations (L) | super admin + content lead |
| `chg.backfill.margin_days` *(v1.1)* | G | 2 | 1–14 | content lead |
| `chg.rbi_pages.missing_row_alert` *(v1.1)* | G | ON | — | content lead |
| `chg.updates.collapse_non_adopted` *(v1.1)* | T | ON | — | `ten_admin` / user |
| `chg.updates.gist_max_words` *(v1.1)* | G | 60 | 30–100 | content lead |
| `chg.push.second_approver_scope` *(v1.1)* | G | ALL_TENANTS or > 50 tenants | — | super admin |
| `chg.incident.s1_containment_hours` *(v1.1)* | G | 4 | 1–8 | super admin |
| `chg.foreign.reconciliation_local_time` *(v1.1)* | G | 20:00 authority-local | 18:00–23:00 | content lead (per pack) |
| `ai.autonomy.agent.VA-01` *(v1.1; X1: key aligned with P17 `ai.autonomy.agent.<agent>`; was `ai.agent.regulatory_analyst.autonomy`)* | G (platform) / T (tenant) | L1 | L0–L2 (L2 only for creating draft change items on the platform; NN-50) | content lead / `ten_cco` |

---

## 10. Security, privacy and audit

- Raw source documents are public regulator material, stored immutably with hashes and retrieval metadata, giving a defensible record of "what the regulator published and when we saw it".
- Tenant documents uploaded to the AI Studio are tenant data (RLS, India residency NN-24), sent to the AI provider only for that tenant's run and under the provider terms recorded in P17 (NN-15).
- Prompt-injection defence: instrument text is passed as data with delimiters; the system prompt instructs the model to ignore instructions inside documents; outputs are schema-validated; no tool calls with side effects are available to the Studio model (NN-14).
- Every triage decision, analysis edit, approval, publication, tenant acknowledgement, dismissal, impact assessment and sign-off is in the audit ledger (R-088), as are Studio runs and the human decisions on their outputs.
- Super-admin "LawDocs notice" broadcasts require a second approver for messages to all tenants (prevents accidental or malicious mass messaging).
- Updates e-mails contain no tenant compliance data beyond counts and links; links require login.

---

## 11. AI touchpoints and guardrails

| Touchpoint | Vidhi behaviour | Guardrail |
|---|---|---|
| Classification and addressee mapping | Proposes class, urgency, families | Rules first; analyst confirms |
| Change summary | Structured, cited analysis | Analyst edits, checker approves; uncited claims rejected by validator |
| Clause diff explanation | Explains diffs in plain words | Diff itself deterministic |
| Concordance proposals | Suggests old → new paragraph mapping | Analyst confirms each mapping |
| Impacted checkpoint drafts | Drafts KEEP/RE-CITE/MODIFY/RETIRE/NEW | Through P03 release pipeline |
| "Why it matters to you" | Generated deterministically from profile and adoption data | Template-based; AI not required |
| Impact assessment pre-fill | Drafts assessment from tenant data | CCO edits and signs off |
| Radar gist | One-line gist | Flag OFF until eval gate; labelled unreviewed |
| AI Question Authoring Studio | Generates draft workbook per methodology | Self-review + deterministic validation + human approval; never auto-publishes (NN-04); zero tolerance for invented citations |
| Enrichment and similar-change retrieval *(v1.1)* | Ranks context links and pre-fills impact | Links shown with "based on"; analyst accepts |
| Sibling proposals *(v1.1)* | Drafts edits for sibling instruments | Each sibling reviewed and released separately |
| Gists *(v1.1)* | ≤ 60-word summary | Labelled unreviewed until approved |
| Row quality scoring *(v1.1)* | Model-judged plain-language score | Hard checks deterministic; failing rows cannot be approved |
| Regulatory Analyst agent *(v1.1)* | Orchestrates the above as one mission per change item | Bounded autonomy; regression and shadow gates (FR-P05-103) |

---

## 12. Acceptance criteria (`tests/acceptance/p05/*.feature`)

```gherkin
Feature: Monitoring
  Scenario: Evening reconciliation
    Given all Appendix F sources are active
    When the clock reaches 20:00 Asia/Kolkata
    Then EveningReconciliationWorkflow scans every source within 30 minutes
    And sources not successfully scanned within their SLA raise a P2 alert

  Scenario: Silent replacement detected
    Given an RBI PDF stored with hash H1 on 3-Nov-2026
    When the same URL returns hash H2 during reconciliation
    Then a detected item with version_of = previous item is created for triage

  Scenario: Parser drift
    Given IFSCA NewSection historically yields items weekly
    When the page structure changes and zero items parse for 3 runs
    Then the source state becomes PARSER_BROKEN and the content lead is alerted

Feature: Publication and Updates
  Scenario: Amendment flows to tenants with overlays
    Given tenant T adopted instrument I and has an overlay on checkpoint C of I
    When an amendment to I changes C's clause and the release is published
    Then T receives one REGULATORY_CHANGE update with what/why/what-to-do
    And the update shows previous actionable (T's overlay text) and new actionable side by side
    And a rebase-conflict review task exists for C
    And the effective date appears in the CCO's calendar

  Scenario: Updates are separate from notifications
    Then the update is stored in chg.updates and not in wf.notifications (NN-27)

  Scenario: Unacknowledged high-urgency update escalates
    Given a HIGH update delivered on Monday
    When it is not acknowledged by Wednesday close of business
    Then the CCO and tenant admin are escalated

  Scenario: Due-date extension
    When an MCA extension is published for form X for FY 2025-26
    Then open instances of the linked checkpoints show the new due date and keep the original statutory date on record

Feature: AI Question Authoring Studio
  Scenario: Platform run follows the methodology
    Given the IFSCA (Appointed Actuary) Regulations, 2022 PDF and template LDC-TPL-IFSCA-GEN-v1.0
    When the content maker runs the Studio with split_subclauses ON
    Then the draft workbook has the exact row-1 and row-2 headers
    And columns A, E, I, J, T and W–AD are blank in every row
    And every value in C, D, H, M, O, R is from the IFSCA vocabularies
    And every K value resolves to a clause of the instrument
    And coverage recall against the approved golden sheet is >= 95%

  Scenario: No auto-publish
    When a Studio draft is ready
    Then no tenant can see its rows until a second user approves (NN-04, NN-05)

  Scenario: Tenant-only run
    Given client admin A of tenant T uploads a lender covenant
    When the run is approved by T's CCO
    Then the rows are tenant checkpoints visible only to T (NN-01)

  Scenario: Re-upload diff is recorded
    When the owner downloads the draft, edits 12 rows in Excel and re-uploads
    Then the importer shows 12 CHANGED rows against the AI draft and stores the diff in the evaluation set

Feature: RBI category pages (v1.1)
  Scenario: Updated-as-on change opens a change item
    Given the NBFC DoR category page lists "Concentration Risk Management Directions, 2025" updated as on 1 October 2026
    When the evening scan finds "Updated as on 25 October 2026"
    Then a CONSOLIDATION_UPDATE change item is opened, linked to the catalogue row and the prior version
    And sibling proposals are opened for the same subject in other categories updated on the same date

  Scenario: New direction is catalogued automatically
    When a new row appears on the commercial banks DoR page
    Then an instrument and catalogue row are created in state PLANNED within 1 business day
    And affected tenants see the badge "New — checkpoints in preparation"

Feature: Content incident (v1.1)
  Scenario: Wrong due date rolled back
    Given a published release set a wrong statutory due date for a High-risk checkpoint
    When the content lead declares an S1 incident
    Then the blast-radius report lists affected tenants, instances, calendar entries and notifications
    And rollback restores the prior rule for future instances within 4 hours while completed instances are unchanged

Feature: Updates noise control (v1.1)
  Scenario: Accept impact in one action
    Given an update affecting 3 departments
    When the CCO clicks Accept impact and confirms the preview
    Then impact tasks are created for each department head with due dates from the effective date

  Scenario: Licensed signal needs a primary source
    Given a licensed feed reports a new UAE regulation
    When an analyst tries to publish it as an update without linking the official source
    Then publication is blocked with LDC-CHG-121
```
NN tests: `NN-04_studio_output_requires_approval`, `NN-05_studio_runner_cannot_approve`, `NN-06_change_summary_bullets_cited`, `NN-14_studio_model_has_no_side_effect_tools`, `NN-15_tenant_docs_not_used_for_training_flag_recorded`, `NN-27_updates_model_separate`, `NN-02_change_history_append_only`; *(v1.1)* `NN-34_unreviewed_radar_never_changes_obligations`, `NN-47_agent_cannot_triage_not_relevant`, `NN-50_regulatory_analyst_autonomy_bounded`, `NN-52_mcp_updates_tools_scoped`, `NN-54_foreign_translation_labelled`, `NN-55_studio_rows_citing_withdrawn_blocked`.

---

## 13. Deliverables and exit gate

1. `chg` schema, source registry loaded from Appendix F, fetchers (RSS, HTML listing, PDF, e-Gazette, e-mail alert), schedules incl. 20:00 IST reconciliation, health monitoring and alerts.
2. Ingestion, extraction, metadata and classification; triage UI; change-item workflow with SLAs.
3. Clause diff, amendment-instruction parser, working consolidation, concordance editor and re-citation drafting.
4. Publication fan-out integrated with P03 releases and P04 recalculation; due-date extensions.
5. Updates inbox with categories, three-part notes, old-vs-new tables, delivery channels, preferences, acknowledgement and escalation; calendar entries.
6. Tenant impact assessment, implementation tracker, change history exports, Board report section.
7. AI Question Authoring Studio (platform and tenant), methodology profiles for every Appendix E family, evaluation harness with the golden set, cost estimates and metering hooks (P20).
8. Change dashboard with lead-time metrics; Radar report.
9. §12 scenarios and NN tests green; one-month shadow run before go-live comparing the monitor's detections with a manual check of RBI, SEBI, IFSCA and IRDAI pages (target: zero missed P1 items).
10. *(v1.1)* RBI category-page monitor (23 pages) with catalogue automation, sibling proposals and supersession flow; concordance seeded from the RBI/2025-26/100 Annex; legacy NBFC re-citation completed before Wave-1 GA.
11. *(v1.1)* Enrichment, similar-change retrieval, per-release metrics, collapsed non-adopted updates, gists, Accept impact, push composer with audience preview, mutes.
12. *(v1.1)* Content-incident playbook rehearsed once (tabletop) before GA; enforcement corpus seeded with 24 months of RBI and SEBI orders.
13. *(v1.1)* Regulatory Analyst agent at L1 with golden sets and regression gates; Studio row scoring; INTL-GEN and AI-GOV methodology profiles; MCP Updates tools.

---

## 14. Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P05-01 | RBI RSS feed coverage | `rss.aspx` content scope (notifications vs press releases) to confirm | Content lead | Listing-page parsers for all RBI sections regardless of RSS [VERIFY] |
| OI-P05-02 | IFSCA has no RSS | Listing scrape only | Content lead | INTRADAY polling of NewSection; egress allowlist |
| OI-P05-03 | IRDAI canonical site | irdai.gov.in vs policyholder.gov.in listings | Content lead | Monitor both [VERIFY] |
| OI-P05-04 | State co-op registrar sites | 28+ states, inconsistent sites, many in regional languages | Content lead (with S7 Appendix S) | WEEKLY_DEEP; OCR + translation; priority states first (MH, GJ, KA, UP, RJ, DL, TN, KL, MP, WB) |
| OI-P05-05 | Licensed news feed | Cost, terms | Product owner | `chg.news.enabled` OFF |
| OI-P05-06 | Claude data residency / retention | India-region availability and zero-retention terms | CTO | Provider adapter records terms; public regulator documents only for platform runs until confirmed [VERIFY] |
| OI-P05-07 | Display of penalised entity names | Public information but reputational sensitivity | Counsel | Flag `chg.enforcement.show_entity_names` |
| OI-P05-08 | Regulator e-mail alert subscriptions | Availability per regulator | Content lead | Optional redundancy |
| OI-P05-09 | Radar AI gist | Accuracy threshold | Content lead | OFF until gate passed |
| OI-P05-10 *(v1.1)* | Stability of RBI category-page ids (`did`) and layout | Page ids observed 25 Oct 2026; RBI may redesign | Content lead | Parser fingerprint → PARSER_BROKEN alert; listing-page fallback (SRC-RBI-03) |
| OI-P05-11 *(v1.1)* | Licensed foreign regulatory-intelligence provider | Cost, coverage, terms per country | Product owner | `REG_INTEL_PORT` OFF; official sources only |
| OI-P05-12 *(v1.1)* | Publication of DPB decisions | Board operations under DPDP Rules phased | Content lead | Corpus source added when decisions are published |

---

## 15. Sources (accessed 25 October 2026)

1. RBI — Notifications, Master Directions, Amendment Directions, Draft Directions (RE-wise), Circulars Withdrawn, Press Releases, RSS: https://www.rbi.org.in/ ; https://www.rbi.org.in/Scripts/rss.aspx ; https://www.rbi.org.in/Scripts/BS_ViewMasterDirections.aspx
2. JSA KM Newsflash on RBI Master Directions (29-Nov-2025): https://www.jsalaw.com/wp-content/uploads/2025/11/KM-Newsflash-RBI-Master-Directions.pdf
3. SEBI RSS: https://www.sebi.gov.in/rss.html (feed `https://www.sebi.gov.in/sebirss.xml`)
4. IFSCA New Section: https://ifsca.gov.in/Home/NewSection
5. IRDAI circulars listing (IRDAI-owned site): https://policyholder.gov.in/web/guest/circulars ; e-mail alerts: https://policyholder.gov.in/web/guest/register-for-email-alerts
6. CRCS circulars: https://crcs.gov.in/circulars
7. Ministry of Labour and Employment — Labour Codes effective 21-Nov-2025 (EY alert, Nov 2025): https://www.ey.com/content/dam/ey-unified-site/ey-com/en-in/alerts-hub/2025/11/new-labour-codes-implemented-across-the-country-effective-21-november-2025.pdf
8. ServiceNow, Regulatory Change Management workflow (public documentation index): https://www.servicenow.com/docs/r/zurich/governance-risk-compliance/reg-change-workflow-swimlane.html
9. Compliance Week, "Compliance.ai upgrades RCM solution" (AI obligation extraction; cross-jurisdiction comparison): https://www.complianceweek.com/grc-announcements/complianceai-upgrades-rcm-solution/27272.article
10. Insurance Edge, "CUBE launches RegPlatform Intel" (9-Apr-2025; acquisitions of Thomson Reuters Regulatory Intelligence and Oden): https://insurance-edge.net/2025/04/09/cube-launches-regplatform-enabling-compliance-in-evolving-markets/
11. MetricStream Regulatory Change Management / Kinetix partnership: https://www.metricstream.com/products/regulatory-change-management.htm
12. TeamLease RegTech (12,000 changes/yr; mapping in 24–48 h; circular summariser): https://teamleaseregtech.com/product-services/statutory-regulatory-compliance-management-software/
13. Lawrbit GCMS (2,000+ monitored websites; configurable update mailers): https://www.lawrbit.com/wp-content/uploads/2024/07/solution-overview-gcms-india.pdf
14. Owner's Part-2 commands for NBFC and IFSCA question sheets (25-Oct-2026 brief) — basis of the methodology profile.
15. *(v1.1)* RBI circular RBI/2025-26/100 and press release 2025-2026/1588 (28 Nov 2025): https://website.rbi.org.in/web/rbi/-/notifications/consolidation-of-regulations-withdrawal-of-circulars ; RBI Master Directions category pages (`BS_ViewMasterDirections.aspx?did=403–413, 419–429, 338`), as captured in Appendix AB and the catalogue workbook.
16. *(v1.1)* Appendix Z (IMP-019–IMP-027); Appendix AA (agent workforce, autonomy levels, evaluation); Appendix Y and P25 (foreign sources).

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-33, NN-34; X-01 (event names), X-12; the RBI 28 Nov 2025 concordance (master §7) is a Wave-1 deliverable.

**Added in v1.1:** NN-50, NN-55; D-39; X-52.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
