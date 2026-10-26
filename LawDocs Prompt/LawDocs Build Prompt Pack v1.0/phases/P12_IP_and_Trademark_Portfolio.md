# Phase P12 — IP and Trademark Portfolio

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (Legal Vault, bulk intake, legal hold), P05 (OCR and extraction of examination reports, Journal pages and registry e-mails), P06 (templates: assignment, licence, co-existence, user affidavit), P07 (CLM for IP licences and assignments; obligations), P08 (stamp-before-sign and eSign for IP deeds), P09 runtime (`AGT_TM_WATCH`), P11 (oppositions, rectifications, infringement and appeals as matters; deadline engine; frozen `lit` read API), P14 (Startup Desk bundles), P16 (marketplace filing and opinion SKUs delivered by trade marks agents and advocates), P17 (plan limits, add-on `LD-ADD-TMW`, AI credits), P19 (`TRADEMARK_DATA_PORT` adapters, IP mailbox), P20 (export map). External: WIPO Global Brand Database (terms [VERIFY]), a licensed trademark data and Journal-watch partner (not yet selected [VERIFY]).
> **Sequencing:** Wave 2, after P11 sprint 2 (deadline engine and matter API frozen). Sprint 1–2: asset model, trademark register, status taxonomy, deadline rules, manual and assisted refresh. Sprint 3–4: clearance assistance, filing-support service hand-off, examination and hearing workflow, renewals. Sprint 5: Journal watch (partner or manual upload), copyright/design/patent/domain registers. Sprint 6: licences and assignments, reports, mobile, hardening.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), D (roles), H (agent roster), K (export taxonomy), M (marketplace professional rules), R (settings), T (intake categories and SLAs for IP requests), W (verification log and open items).
> **Requirements covered:** R-013, R-017, R-019, R-021, R-027, R-030, R-037, R-061, R-075, R-082, R-086.
> **Decisions applied:** D-05, D-10, D-11, D-14, D-15, D-17 · **Challenges applied:** CH-08, CH-09, CH-14, CH-27 · **Non-negotiables tested:** NN-01, NN-02, NN-05, NN-08, NN-09, NN-11, NN-13, NN-14, NN-20, NN-21, NN-22, NN-29, NN-30, NN-38, NN-39, NN-43, NN-46
> **Estimated effort:** 6 two-week sprints, squad of 8 (backend 3, frontend 2, data/ML 1 for similarity, QA 1, integration 1) plus a part-time IP domain analyst (advocate or registered trade marks agent).

---

## 1. Objective and business outcome

Startups and SMEs file trademarks through aggregators and then lose track: the examination report goes to the agent's address for service, the one-month reply window (Trade Marks Rules 2017 r.33(4)) passes, the application is abandoned, or the ten-year renewal is missed. IP India offers status lookups behind an OTP, a weekly Journal and e-filing, but no portfolio view, alerts or similarity watch (R1 §7.1). Nobody combines **portfolio tracking + deadline engine + Journal watch + reply drafting + professional filing** for an SME at a low price (R1 key finding 8).

This phase builds that portfolio for companies and individuals (sole proprietors, founders, creators), centred on trademarks with lighter registers for copyrights, designs, patents and domain names, and links IP disputes to P11 and IP agreements to P06/P07.

| Outcome | KPI and exit-gate measure |
|---|---|
| No lost application or registration | Every asset has a normalised status, last-refreshed time and a computed next deadline; 0 missed deadlines in UAT; renewal tasks created ≥ 12 months before expiry |
| Honest status | Every status shows its source (user, agent, assisted refresh, licensed partner, WIPO route) and staleness; no "live", "official" or "real-time" wording (NN-20) |
| Faster filing | From "I want to protect my brand" to a filing-ready TM-A data sheet handed to an agent in ≤ 15 minutes and ≤ 8 screens |
| Watch that matters | Journal hits reviewed with ≥ 30 days left in the 4-month opposition window for 95% of hits in pilot |
| Clean boundaries | LawDocs never files with IP India, never handles the eRegister OTP and never automates the IP India portal (NN-05, NN-13) |

## 2. Scope (in / out)

**In scope**
- IP asset model (`tmk_`, business ID `LD-TMK-YYYY-NNNNNN`) for trademarks, copyrights, designs, patents and domain names; optional confidential-information register.
- Trademark register: marks, Nice classes, applicants, application numbers, filing dates, priority and use claims, status lifecycle, Journal details, registration and renewals.
- Deadline rule pack for trademarks (and lighter rules for other assets) with verification flags.
- Status refresh through `TRADEMARK_DATA_PORT`: user-entered numbers, assisted refresh, WIPO Global Brand Database route (if licensed), licensed partner.
- Search and clearance assistance (Vidhi): Nice class finder, knock-out screening, absolute/relative-ground explainers.
- Filing-support service through the marketplace: TM-A data sheet, documents, hand-off to an authorised agent or advocate, recording of the filing.
- Examination report, reply and show-cause hearing workflow.
- TM Journal watch (partner or manual upload) with similarity scoring and review queue.
- Oppositions, rectification, cancellation, infringement and passing-off as P11 matters.
- Licences, assignments and recordals (link P06/P07/P08).
- Renewal reminders, use-evidence locker, portfolio valuation notes, startup bundles, dashboards and reports.

**Out of scope (owner phase)**
- Filing, replying or attending hearings before the Registry — done by the authorised agent or advocate from their own account (NN-13, NN-41). LawDocs prepares and records.
- Legal opinions on registrability or infringement — marketplace professionals (P16).
- Litigation management — P11.
- Contract drafting and negotiation — P06/P07.
- Statutory valuation reports — registered valuers via P16.
- Geographical indications, plant varieties, semiconductor layouts — not in v1 (tenant may record as "Other IP" with manual dates).
- Foreign national filings other than recording the status and dates of Madrid designations and foreign registrations entered by the user.

## 3. Personas and permissions touched

| Role code | What they can do in P12 |
|---|---|
| `ORG_CLO` | Owns the IP portfolio; approves filings, oppositions, licences and assignments within delegation; configures watch scope and settings `ipm.*` |
| `ORG_LEGAL_MAKER` | Creates assets, records statuses, uploads documents, prepares data sheets, triages watch hits, creates renewal tasks |
| `ORG_CHECKER` | Checks data sheets before hand-off, bulk imports, assignment recordals |
| `ORG_MEMBER` (e.g., marketing, product) | Requests brand clearance through the P13 intake desk; sees assets for their products |
| `ORG_KMP` | Reads portfolio summary; CFO sees spend and valuation notes |
| `ORG_EXT_COUNSEL` | Guest on assigned assets/matters: posts status updates, uploads Registry documents, records filings |
| `IND_OWNER` | Tracks own marks and creative works; buys filing services; receives reminders |
| `PRO_ADVOCATE`, `PRO_OTHER` (sub-type `TRADE_MARKS_AGENT`, `PATENT_AGENT` — proposed for Appendix D) | Through a marketplace engagement: review data sheets, file from their own IP India account, record filing details, draft replies, attend hearings |
| `OPS_PROFESSIONAL`, `ORG_DELEGATED_MAKER` | Prepare data sheets and status updates under a delivery grant (NN-17); never approve |
| `AGT_TM_WATCH` (R4 LV-10) | Maker only (NN-43): proposes status extractions, class suggestions, screening results, watch hits, reply outlines, reminders |
| `PLT_LEGAL_REVIEWER`, `PLT_CONTENT_EDITOR` | Maintain status taxonomy, deadline rules, fee table, class-term lists and explainers (NN-30) |

## 4. Functional requirements

### 4A. IP asset model

**FR-P12-01 — Common asset fields.** Asset ID and business ID; asset type (TRADEMARK, COPYRIGHT, DESIGN, PATENT, DOMAIN_NAME, CONFIDENTIAL_INFO, OTHER_IP); title (mark text, work title, design article, invention title, domain); owner (legal entity `ent_` or person `prs_`; joint owners with shares); jurisdiction (IN default; foreign office code for recorded foreign assets); business owner and product lines; status (normalised) and raw status text; key dates; agent/attorney of record (text, plus marketplace engagement link if any); linked documents, matters (`mat_`), agreements (`agr_`), tasks; confidentiality; tags; source and last-refreshed time; valuation notes (FR-P12-36).

**FR-P12-02 — Trademark fields.** Mark type (word, device/logo, composite, shape, sound, colour combination, three-dimensional, series, collective, certification) [VERIFY list under Trade Marks Rules 2017]; mark text; transliteration and translation for non-English or non-Roman words [VERIFY requirement]; representation image (original immutable, NN-09); Vienna codes (as assigned by the Registry, recorded only); Nice classes (one or more — multi-class application under Trade Marks Act 1999 s.18(2) [VERIFY]); goods/services specification per class; application number; filing date; priority claim (convention country, number, date — s.154 [VERIFY]); use claim ("proposed to be used" or "used since <date>" with supporting user affidavit); applicant category for fees (individual, sole proprietor, startup, small enterprise, others); address for service; Journal number and date of advertisement; acceptance mode (accepted and advertised / advertised before acceptance); registration certificate date and number; validity ("valid until", computed per FR-P12-08); renewal history; Madrid designations (if any, recorded).

**FR-P12-03 — Nice classes.** 45 classes (1–34 goods, 35–45 services) under the Nice Classification; the edition in force at IP India is a content setting `ipm.nice.edition` [VERIFY current edition]. Class headings and the class-term list are content (NN-30) with explanations in launch languages (`hlp.ipm.nice_class`).

**FR-P12-04 — Applicants and owners.** Applicant may differ from the eventual owner (e.g., founder files before incorporation). An **ownership gap** warning shows when the applicant is an individual but the brand is used by the tenant company, with a suggested assignment (FR-P12-33). Same for domains registered in an employee's personal account.

### 4B. Trademark status lifecycle

**FR-P12-05 — Normalised statuses.** IP India status labels (R1 §7.2, per the Intepat guide; confirm against the Registry [VERIFY]) map to LawDocs states with user labels and next actions (content table, versioned):

| LawDocs state | IP India label(s) (as published) | User label | Next action | Clock (FR-P12-07) |
|---|---|---|---|---|
| NEW_APPLICATION | New Application | Filed | Check particulars; keep receipt | — |
| VIENNA_CODIFICATION | Send to Vienna Codification | Logo being classified | None | — |
| FORMALITIES_FAIL | Formalities Chk Fail | Paperwork defect | Cure the defect | TM-FORMALITY-CURE |
| FORMALITIES_PASS | Formalities Chk Pass | Paperwork OK | None | — |
| MARKED_FOR_EXAM | Marked for Exam | Waiting for examiner | Collect evidence of use | — |
| EXAM_REPORT_ISSUED | Exam Report Issued; Objected | Examiner objected | Draft and file reply (agent) | TM-EXAM-REPLY |
| REPLY_FILED | (as published) | Reply filed | Await decision or hearing | — |
| SHOW_CAUSE_HEARING | Ready for Show Cause Hearing | Hearing fixed | Prepare; agent attends | TM-HEARING |
| ADVERTISED | Accepted and Advertised; Advertised bef Acc | Published in Journal | Monitor oppositions | TM-OPPOSITION-WINDOW |
| OPPOSED | Opposed | Someone opposed | File counter-statement (P11 matter) | TM-COUNTER-STATEMENT |
| REGISTERED | Registered | Registered ® | Download certificate; diarise renewal; keep use evidence | TM-RENEWAL-WINDOW, TM-NON-USE-WATCH |
| RENEWAL_DUE | (derived) | Renewal due | File renewal (agent) | TM-RENEWAL-WINDOW |
| REMOVED | Removed | Lapsed | Renew with surcharge or restore | TM-RENEWAL-SURCHARGE, TM-RESTORATION |
| REFUSED | Refused | Refused | Consider appeal or re-filing | TM-APPEAL-HC |
| ABANDONED | Abandoned | Abandoned | Advice on review or re-filing | As advised |
| WITHDRAWN | Withdrawn | Withdrawn | — | — |
| RECTIFICATION_FILED | Rectification Filed | Registration challenged | P11 matter | As per forum |
| CANCELLED | Cancelled | Cancelled | — | — |

Unknown labels show raw text, map to `UNMAPPED`, and open a mapping task for `PLT_CONTENT_EDITOR`.

**FR-P12-06 — Status history.** Every status change is a timeline entry with source, date as published, date recorded, evidence document (status page PDF, Registry e-mail, examination report) and actor. History is append-only; corrections reference the corrected entry (NN-02).

### 4C. Deadline rules

**FR-P12-07 — Rule pack (`rul` content; P11 engine).** Clocks reuse the P11 deadline engine (FR-P11-29 to FR-P11-33): start event, period, day type, caps, verification status, reminder ladder, never pause. Seeds — every row **[VERIFY against the Trade Marks Act 1999 and Trade Marks Rules 2017 (as amended), Copyright Act 1957, Designs Act 2000, Patents Act 1970 and Patents Rules 2003 (as amended)]**; until verified, the clock is advisory (NN-38; OI-P12-01):

| Code | Clock | Seed period | Source to verify |
|---|---|---|---|
| TM-FORMALITY-CURE | Cure formalities defect | 1 month from communication | Trade Marks Rules 2017 (rule on formalities) |
| TM-EXAM-REPLY | Reply to examination report | **One month** from the date of receipt (compute as a calendar month, not 30 days); non-reply may lead to abandonment | Rules 2017 r.33(4) (ipindia.gov.in text checked 25 Oct 2026: "within one month from the date of receipt of the examination report"); hearing under r.33(6) with r.115; Act s.132 (abandonment) |
| TM-HEARING | Show-cause hearing | Hearing date; adjournment request before the date per rules | Rules 2017 (hearing and adjournment rules) |
| TM-OPPOSITION-WINDOW | Third-party opposition window after advertisement | 4 months from the date of publication of the Journal; not extendable | Act s.21(1) read with Rules 2017 r.42(1) (Form TM-O; text checked 25 Oct 2026 — the Act's "3 months + 1 month" is applied by the Rules as a flat four months) (R1 §7.1; R3 LG-170) |
| TM-OPPOSE-OTHERS | Our opposition to a third-party mark | 4 months from that Journal's date | Act s.21(1); Rules 2017 r.42(1) |
| TM-COUNTER-STATEMENT | Counter-statement after opposition | 2 months from receipt of the copy of the notice of opposition (Form TM-O); failure treated as abandonment | Act s.21(2), (3); Rules 2017 r.44(1) [VERIFY extension position] |
| TM-EVIDENCE-OPPONENT / -APPLICANT / -REPLY | Evidence stages in opposition | 2 months from service of counter-statement / 2 months from receipt of opponent's affidavits / 1 month from receipt of applicant's affidavits; opponent's or applicant's inaction = deemed abandonment | Rules 2017 rr.45–47 (text checked 25 Oct 2026) |
| TM-RENEWAL-WINDOW | Renewal filing window | Not more than 1 year before expiry (Form TM-R) | Act s.25(2); Rules 2017 r.57(1) |
| TM-EXPIRY | Registration validity | 10 years from the date of registration (which is the filing date) | Act s.23(1), s.25(1) |
| TM-RENEWAL-SURCHARGE | Renewal after expiry with surcharge | 6 months after expiry (Form TM-R) | Act s.25(3) proviso; Rules 2017 r.59 |
| TM-RESTORATION | Restoration after removal | Up to 1 year from expiry (Form TM-R) | Act s.25(4); Rules 2017 r.60 |
| TM-APPEAL-HC | Appeal against Registrar's order | 3 months from the order | Act s.91 as amended by the Tribunals Reforms Act 2021 [VERIFY] |
| TM-NON-USE-WATCH | Vulnerability to removal for non-use (advisory) | 5 years from the date the mark is entered on the register + 3 months | Act s.47(1)(b) [VERIFY] |
| CR-REG-OBJECTION | Objection window after copyright application diary number | 30 days [VERIFY] | Copyright Rules 2013 |
| CR-TERM | Copyright term (literary, dramatic, musical, artistic) | Author's life + 60 years (other works per Act) | Copyright Act 1957 ss.22–29 |
| DS-EXPIRY | Design registration | 10 years from registration date | Designs Act 2000 s.11(1) |
| DS-EXTENSION | Extension | Once, 5 years, on application before expiry | Designs Act s.11(2) [VERIFY] |
| DS-RESTORATION | Restoration of lapsed design | 1 year from lapse | Designs Act s.12 [VERIFY] |
| PT-RFE | Request for examination | 31 months from priority date | Patents Rules 2003 r.24B [VERIFY as amended 2024] |
| PT-FER-REPLY | Reply to first examination report | 6 months, extendable by 3 months | Patents Rules r.24C [VERIFY as amended 2024] |
| PT-RENEWAL | Annual renewal fee | Each year from the 3rd year; 20-year term from filing | Patents Act s.53; Rules r.80 [VERIFY] |
| PT-WORKING-STATEMENT | Statement of working (Form 27) | Periodic as notified [VERIFY 2024 amendment: once per three financial years] | Patents Act s.146; Rules r.131 [VERIFY] |
| PT-RESTORATION | Restoration of lapsed patent | 18 months from lapse | Patents Act s.60 [VERIFY] |
| DN-EXPIRY | Domain expiry | Registrar's expiry date; grace periods per registry [VERIFY per TLD] | Registrar terms |

Reminder ladders (TENANT tier, can add, not remove): examination reply [21, 14, 7, 3, 1]; opposition window for own advertised marks (informational) [90, 30]; counter-statement [45, 30, 14, 7, 3, 1]; renewal per `ipm.renewal.reminder_offsets_months` [12, 6, 3, 1] months plus a final 7-day reminder; patents and designs [90, 30, 7].

**FR-P12-08 — Validity computation.** For trademarks, "valid until" = filing date + 10 years (registration takes effect from the date of application, s.23(1)) and each renewal adds 10 years from the expiry of the last registration (s.25(2)) [VERIFY]; the engine shows the dates with rule ID and version (deterministic, no AI).

**FR-P12-09 — Government fee table (content).** Fees are rule-pack data with `last_verified_at`: TM-A e-filing ₹4,500 per class for individuals, sole proprietors, startups and small enterprises; ₹9,000 per class for others; renewal ₹9,000 per class (R6 B-13, D-14 — V-SEC) [VERIFY current schedule and category definitions, OI-P12-02]. Fees display separately from professional and LawDocs fees, with the total incl. GST before payment (NN-22). Category evidence (Udyam registration, DPIIT recognition) is collected for the concessional fee.

### 4D. Status refresh (`TRADEMARK_DATA_PORT`)

**FR-P12-10 — Adapters.** No IP India API exists (R6 D-11; CH-27). The port exposes `lookupByApplicationNo`, `getStatusSnapshot`, `searchMarks` (optional), `watchJournal` (optional), `health`:

| Adapter | Status | Behaviour |
|---|---|---|
| `ManualAppNo` | Always ON | User or agent enters application number, status (picked from the normalised list), dates; LawDocs reminds after each expected event |
| `AssistedRefresh` | ON | The user opens the IP India e-Register themselves (OTP to their own e-mail/mobile — LawDocs never receives or handles the OTP), saves the status page as PDF or screenshot, and uploads or shares it to LawDocs (mobile share sheet). `dix` extracts application number, status, Journal number/date, hearing date; `AGT_TM_WATCH` proposes the update; the maker confirms |
| `RegistryMailParser` | ON | Users forward Registry e-mails (examination reports, hearing notices, certificates) to the tenant's IP mailbox (`int`); extraction as above |
| `WipoBrandDb` | OFF until terms cleared | Only through a route whose terms permit LawDocs' commercial use — a WIPO data licence or a licensed partner [VERIFY WIPO terms; OI-P12-03]. R6 D-12's third-party scraping actor route is **not** used (NN-05 spirit; vendor must warrant lawful collection) |
| `LicensedPartner` | OFF until contract | A TM data or watch partner with lawful-source warranty, India residency, DPDP processor terms and SLA [VERIFY partner] |

No adapter or agent automates IP India pages, solves CAPTCHAs, or uses an agent's or user's portal credentials (NN-05; test `NN-05_no_ipindia_automation`).

**FR-P12-11 — Provenance and staleness.** Same field-level provenance and freshness chips as P11 (FR-P11-15): UPDATED_TODAY, RECENT (`ipm.data.recent_days`, 30), STALE (older than `ipm.data.stale_days` (60) for pending applications, or an expected event date passed), UNKNOWN, CONFLICT. Registered marks with no pending event are not marked stale until 90 days before a renewal window or on a watch event. Copy: "Status as recorded from <source> on <date>. Check the IP India e-Register before relying on it."

**FR-P12-12 — Refresh prompts.** For pending applications the system asks the owner (or agent) for an assisted refresh every `ipm.refresh.prompt_days` (30) and immediately after a computed expected event (e.g., 30 days after filing for formalities). Prompts are one tap from the notification to the upload screen.

### 4E. Search and clearance assistance (Vidhi)

**FR-P12-13 — Nice class finder (≤ 3 steps).** The user describes the business ("We make cold-pressed juices and sell them online and in cafés"). Vidhi proposes classes with reasons and goods/services terms drawn only from the approved class-term list (FR-P12-03), e.g., Class 32 (non-alcoholic beverages), Class 35 (online retail services), Class 43 (café services). Each suggestion is labelled "suggestion — confirm with a trade marks agent" and cites the class heading. AI credits per R6 (deterministic list lookups free).

**FR-P12-14 — Knock-out screening.** Inputs: mark text, transliterations, classes, optional logo. Sources: the tenant's own portfolio and watch list, plus `WipoBrandDb`/`LicensedPartner` when enabled. Matching: exact, phonetic (Indic-aware phonetic keys and Soundex/Metaphone variants for Roman script), transliteration variants (e.g., Hindi/English), edit distance, prefix/suffix stems, conceptual similarity (embedding-based, tenant-scoped), and class proximity (same class, related classes from a content table). Output: list of potentially conflicting marks with status, class, owner as published, match reasons and a **screening score** (LOW/MEDIUM/HIGH) — labelled "screening aid, not a clearance opinion" (NN-20). Logo similarity is v1.1 (image embeddings), flagged OFF.

**FR-P12-15 — Registrability explainer.** A checklist explains absolute grounds (Trade Marks Act s.9 — e.g., lacking distinctive character, descriptive, customary, deceptive, prohibited) and relative grounds (s.11 — identical or similar earlier marks, well-known marks) with citations, in plain language, and shows which ones the screening suggests may apply. It never concludes "registrable". [VERIFY wording of grounds summaries by `PLT_LEGAL_REVIEWER`.]

**FR-P12-16 — Opinion hand-off.** "Get a clearance opinion" opens a marketplace SKU (P16) delivered by an advocate or registered trade marks agent; the screening pack (inputs, results, sources, dates) is shared with the professional by the user's choice.

### 4F. Filing-support service (marketplace)

**FR-P12-17 — TM-A data sheet.** A guided form produces a filing-ready data sheet for Form TM-A [VERIFY form name under Rules 2017]: applicant details (legal name, entity type, address, nationality/incorporation), applicant category and evidence for fees, mark details and representation file meeting the Registry's format [VERIFY image specifications], classes and specifications, use claim and date, user affidavit draft for prior use (template from P06), priority details, agent details, authorisation of the agent (format per Rules 2017 [VERIFY]). Validation checks completeness, image format, specification terms against the class list, and consistency (e.g., use date before filing date).

**FR-P12-18 — Hand-off and filing record.** The user buys a filing SKU (P16; e.g., "Trademark filing — per class", R6 §R6.2.5 seed ₹1,999 + government fee [OWNER TO SET]). The engaged professional (registered trade marks agent or advocate — Trade Marks Act s.145 on agents [VERIFY]) reviews the data sheet in the practitioner workspace, raises queries, and files from **their own** IP India account. The professional then records application number, filing date, receipt and filed copy in LawDocs; the asset moves to NEW_APPLICATION with source AGENT. The government fee is collected and passed through at actuals (pure agent treatment [TAX MEMO]) and shown separately (NN-22). LawDocs never files and never stores the professional's portal credentials outside the client-owned vault (NN-16).

**FR-P12-19 — Expedited examination option.** The data sheet can mark "request expedited examination" (request form and fee per Rules 2017 [VERIFY]); the UI explains that the opposition window still runs in full (R1 §7.2 note).

**FR-P12-20 — Bulk portfolio onboarding.** Excel template `LD-TPL-IPM-v1.0`, mapped to the registered layout `ld_tm_portfolio_import_v1` (Appendix I) (assets, classes, numbers, dates, agents) with validation, de-duplication on (application number, office), preview, maker-checker above 50 rows, undo within 24 hours; followed by assisted-refresh prompts for pending items. The import is an `xpt.import_jobs` row with `source_kind = IPM_REGISTER` in the single `imp_` ID space owned by P20 (Appendix A §A.21; Resolution R-A-10) — `ipm` supplies the mapping and validation rules, not a separate import machine.

### 4G. Examination, objections and hearings

**FR-P12-21 — Examination report intake.** Upload, mail-parser or agent post creates an EXAM_REPORT_ISSUED event with the report as an original; the TM-EXAM-REPLY clock starts from the **receipt** date recorded (earliest receipt by the applicant or its agent).

**FR-P12-22 — Objection analysis and reply outline (`AGT_TM_WATCH`).** The agent proposes: grounds raised (s.9 / s.11 items with paragraph anchors), cited conflicting marks (number, class, status), suggested response strategy options (arguments on distinctiveness, evidence of use, limitation of specification, consent/co-existence letter, disclaimer), evidence checklist, and a reply outline. Output is labelled "AI draft — for professional review" (NN-14); the reply is finalised and filed by the agent or advocate (P16 SKU "Reply to examination report").

**FR-P12-23 — Hearing workflow.** Hearing notice → hearing record (date, mode, officer, agent) → prep checklist (reply, evidence, user affidavit, prior-use documents with s.63(4) certificates where electronic — NN-10) → outcome recorded (accepted, refused, adjourned) → next state and clocks.

### 4H. Trade Marks Journal watch

**FR-P12-24 — Watch scope.** Per watched mark: classes (own plus related classes from the content table), match types (phonetic, visual text, transliteration, conceptual), sensitivity (strict/standard/broad), jurisdictions (India; Madrid designations recorded later), competitors' names to watch, and alert recipients. Plan limits: `ipm.plan.watch_limit` (with `ipm.journal_watch.enabled`) (seeds: Pro 10 marks + watch, Business 50 marks + watch; add-on `LD-ADD-TMW` +25 marks — R6 §R6.2.2/2.3 [OWNER TO SET]).

**FR-P12-25 — Journal source.** The Journal is published weekly by IP India (R1 §7.1 says every Monday [VERIFY]). Ingestion runs through `TM_JOURNAL_PORT` (Appendix I §I.2.4; kill switch `tm-journal-watch`, OFF until a source is approved). `ipm.watch.journal_source`:
- `PARTNER` — licensed partner supplies parsed Journal entries [VERIFY partner];
- `MANUAL_UPLOAD` — `OPS_CONTENT_PUBLISHER` (or a tenant user) uploads the published Journal PDFs; `dix` OCRs and parses entries (mark, application no., class, applicant, Journal no./date, goods/services, image); automated fetching is **OFF** until the IP India terms of use are checked by counsel [VERIFY; OI-P12-04].
Each ingested Journal is versioned and hashed; parsing quality is reported (entries parsed vs expected).

**FR-P12-26 — Similarity run and hits.** For each new Journal, the engine compares entries with watched marks (FR-P12-14 matchers) and creates hits with score, reasons, side-by-side view (text and image), class relationship, and the computed **opposition last date** (Journal date + 4 months; FR-P12-07). Hits go to a review queue; low-score hits can be auto-dismissed by tenant rule (`ipm.watch.auto_dismiss_below`, default OFF).

**FR-P12-27 — Hit decisions.** Reviewer chooses: DISMISS (reason), MONITOR (re-check at 60 days), CEASE_AND_DESIST (opens P10 notice draft), OPPOSE (creates a P11 matter type TM_OPPOSITION with the TM-OPPOSE-OTHERS clock and links the hit), ASK_PROFESSIONAL (marketplace "Watch hit review" SKU). Decision time and remaining window are reported (KPI: ≥ 30 days left at decision).

**FR-P12-28 — Professional review mode.** Where the tenant buys reviewed watch (R1: StartupGrantsIndia pattern), hits are first reviewed by an engaged professional who records a recommendation; the tenant's CLO decides.

### 4I. Disputes as matters (link P11)

**FR-P12-29 — IP matters.** From an asset: "Start opposition", "Record opposition against us", "Rectification / cancellation", "Infringement or passing off", "Appeal". Each creates a P11 matter (types TM_OPPOSITION, TM_RECTIFICATION, INFRINGEMENT_SUIT, PASSING_OFF, IP_APPEAL) pre-filled with asset, parties, forum (Registrar for opposition; Registrar or High Court for rectification (s.57) and High Court for appeals (s.91) after the Tribunals Reforms Act 2021 abolished the IPAB [VERIFY]; commercial court or High Court for infringement suits — Trade Marks Act s.134; IP disputes are "commercial disputes" under the Commercial Courts Act 2015 s.2(1)(c)(xvii) [VERIFY]) and clocks. The asset shows a "Disputed" badge and the matter's next date.

**FR-P12-30 — Enforcement log.** Per asset, a log of infringement sightings (marketplace listings, social handles, shops) with screenshots kept as originals and hashed, dates and actions (notice, takedown request, suit). Takedown requests to platforms are drafted (P10) and sent by the user.

### 4J. Copyrights, designs, patents and domains (lighter registers)

**FR-P12-31 — Registers.**

| Register | Key fields | Key reminders |
|---|---|---|
| Copyright | Work type (literary incl. computer programme, dramatic, musical, artistic, cinematograph film, sound recording); title; author(s) and owner(s); creation and first-publication dates; diary number and registration number [VERIFY terms]; assignments (in writing, Copyright Act s.19) and licences (s.30) | Objection window after diary number; term per Act |
| Design | Article; class [VERIFY Indian classification]; application number; filing/registration date; priority; certificate | Expiry at 10 years; extension window; restoration |
| Patent | Title; type (ordinary, convention, PCT national phase, divisional); application number; filing and priority dates; publication date; RFE date; FER date; hearing; grant date; patent number; inventors; patent agent (registered under Patents Act Ch. XXI [VERIFY]) | RFE, FER reply, annual renewal, working statement, restoration |
| Domain name | Domain; registrar; registrant (warn if not the company); expiry; auto-renew flag; registry lock (recorded); linked trademark; disputes (UDRP/INDRP [VERIFY]) | Expiry ladder [60, 30, 7, 1] |
| Confidential information (optional) | Description, custodian, access list, NDAs (`agr_`), classification | Annual access review |

Data are user/agent-entered (no registry automation); documents are originals with hashes.

### 4K. Licences, assignments and recordals

**FR-P12-32 — IP agreements.** From an asset: "License this mark", "Assign this mark/work", "Co-existence agreement", "IP assignment from founder/employee/contractor". Templates come from P06; negotiation and execution follow P07/P08 with stamp-before-sign (NN-08; State stamp rules for assignments [VERIFY articles]) and the eSign eligibility gate (IP assignments and licences are not in the IT Act First Schedule exclusions [INTERP — confirm in Appendix F]). Obligations (royalties, quality control, reporting, territory, term) are extracted into CLM obligations.

**FR-P12-33 — Recordal.** After execution, a recordal task prompts the agent to record the assignment or licence with the Registry (request form per Rules 2017 [VERIFY form and any time limit]); the registered proprietor and owner fields update only after the recordal is evidenced. Ownership-gap warnings (FR-P12-04) close when recordal is evidenced.

**FR-P12-34 — Licences in.** Licences the tenant takes (software, brand, content) are recorded as assets of type OTHER_IP "licensed-in" with term and renewal; or linked to the P07 contract register — no duplicate entry.

### 4L. Renewals, use evidence and valuation notes

**FR-P12-35 — Renewal and use-evidence locker.** Renewal tasks are created at the start of the renewal window with a marketplace "Renewal filing" SKU option. A use-evidence locker per mark per year collects dated invoices, advertisements, packaging photos, website captures and sales figures; electronic evidence carries hashes and an s.63(4) certificate draft on export (NN-10). An annual reminder asks for evidence (`ipm.use_evidence.reminder_month`, April).

**FR-P12-36 — Portfolio valuation notes.** Internal notes per asset: cost basis (filing, prosecution, enforcement spend from P11/P16), revenue lines using the mark, licence income, strategic importance (1–5), and optional external valuation reports uploaded. The UI states that notes are internal management information, not a valuation; statutory valuations are done by registered valuers (Companies (Registered Valuers and Valuation) Rules 2017 [VERIFY applicability]) via the marketplace, and accounting recognition of intangibles is for the tenant's accountants (Ind AS 38 [VERIFY]).

### 4M. Startup bundles

**FR-P12-37 — Brand protection bundles (with P14).** Startup Desk bundle seeds: "Brand starter" (class finder + knock-out screen + 1-class filing by an agent + 12 months watch for 1 mark + domain check), "Brand plus" (3 classes + logo filing + 12 months watch + reply-to-examination credit). Each bundle shows full landed price (professional fees, LawDocs fee, government fees by applicant category, GST) before purchase (NN-22, NN-50). DPIIT/Udyam category evidence is checked once and reused.

### 4N. Dashboards, reports and individual view

**FR-P12-38 — IP Home (company).** Tiles: deadlines in 30/90 days, pending applications by state, examination replies due, hearings, watch hits awaiting decision with days left, renewals in 12 months, ownership gaps, stale statuses, disputes; each opens a filtered list with bulk actions.

**FR-P12-39 — Reports.** IPM-01 Portfolio by type, class, status, owner entity; IPM-02 Deadlines and renewals; IPM-03 Watch activity and decisions; IPM-04 Disputes (from P11); IPM-05 IP spend; IPM-06 IP schedule for due diligence (asset list with numbers, dates, owners, encumbrances/licences — used by P14 funding documents). Board pack section for P13.

**FR-P12-40 — My brands (individual).** Cards per mark with plain status ("Your logo is being classified by the Registry. Nothing to do now. We'll remind you to check again on 24 Nov 2026."), next step, reminders, documents and "Get help" (marketplace SKUs). ≤ 3 taps from home to add a mark by application number.

**FR-P12-41 — Customisation hooks.** Tenants configure: watch sensitivity and related-class table overrides, reminder ladders (add only for statutory clocks), required fields, folder names, auto-dismiss rules, alert recipients, report views, use-evidence reminder month, IP intake categories (P13).

**FR-P12-42 — Click budgets.** Add a mark by application number: ≤ 3 taps (mobile). Assisted refresh from a saved status PDF: ≤ 2 taps via share sheet. Class finder to data sheet: ≤ 8 screens. Decide a watch hit: ≤ 2 clicks from the queue. Start an opposition matter from a hit: 1 click + confirmation.

## 5. Workflows and state machines

State machine: Appendix A §A.45 governs §5.1–§5.4 (trademark application, assisted refresh, journal watch, renewal; Resolution R-A-16 maps these states to the Appendix Y `ip_status` projection). Bulk portfolio imports (FR-P12-20) run on the single import machine, Appendix A §A.21 (Resolution R-A-10).

### 5.1 Trademark application (`ipm.trademark`)

| State | Entry | Allowed next | Actor | Guard | Side effects / events |
|---|---|---|---|---|---|
| PLANNED | Clearance or data sheet started | DATA_SHEET_READY, DROPPED | Maker | — | — |
| DATA_SHEET_READY | Validation passed | HANDED_OFF | Maker + checker (if `ipm.filing.checker_required`) | Fee category evidence | `ipm.DataSheetReady` |
| HANDED_OFF | Marketplace engagement or own agent | NEW_APPLICATION | Agent records filing | Application no. + receipt uploaded | `TrademarkFiled` |
| NEW_APPLICATION … REGISTERED | FR-P12-05 states | Per Registry events | Agent/maker/assisted refresh | Evidence document for each change | Clocks per state; `StatusChanged` |
| REGISTERED | Certificate recorded | RENEWAL_DUE, RECTIFICATION_FILED, CANCELLED | Job / maker | — | Renewal clock, non-use watch |
| RENEWAL_DUE | Window opens | REGISTERED (renewed), REMOVED | Agent records renewal | Renewal receipt | `TrademarkRenewed` |
| REMOVED | Registry removal | REGISTERED (restored), CLOSED | Agent | Restoration order | — |
| ABANDONED / REFUSED / WITHDRAWN / CANCELLED | Registry event | CLOSED; or new linked application (re-filing) | Maker | — | Appeal clock where applicable |

Every transition requires a source and, except PLANNED/DATA_SHEET_READY, an evidence document or an explicit "no document available" reason by the CLO.

### 5.2 Assisted refresh

UPLOADED (status PDF/screenshot/e-mail) → EXTRACTED (`dix`, confidence per field) → PROPOSED (`AGT_TM_WATCH` diff vs current) → CONFIRMED by maker (status, dates, clocks updated atomically with audit, NN-45) | REJECTED (reason). Low-confidence fields (< `ipm.extract.min_confidence`, 0.85) are highlighted and cannot be bulk-confirmed.

### 5.3 Journal watch run

JOURNAL_INGESTED (partner payload or uploaded PDF hashed) → PARSED (entry count, quality) → MATCHED (hits created) → REVIEW (per hit: DISMISS / MONITOR / CEASE_AND_DESIST / OPPOSE / ASK_PROFESSIONAL) → CLOSED. Hits not decided by T-30 days to the opposition last date escalate to the CLO; at T-7 a final alert is sent.

### 5.4 Renewal

Clock TM-RENEWAL-WINDOW opens (1 year before expiry) → task with SKU option → RENEWAL_FILED (agent receipt) → REGISTERED with new "valid until". Missed expiry → REMOVED_RISK (surcharge window) → TM-RESTORATION window → CLOSED if not restored.

## 6. Screens and UX

Menu root in the Company workspace: **IP & Trademarks**; Personal workspace: **My brands & creations**. "i" keys: `hlp.ipm.nice_class`, `hlp.ipm.application_number`, `hlp.ipm.examination_report`, `hlp.ipm.show_cause`, `hlp.ipm.journal`, `hlp.ipm.opposition`, `hlp.ipm.counter_statement`, `hlp.ipm.user_affidavit`, `hlp.ipm.priority`, `hlp.ipm.renewal`, `hlp.ipm.restoration`, `hlp.ipm.rectification`, `hlp.ipm.screening_score`, `hlp.ipm.assisted_refresh`, `hlp.ipm.vienna_code`.

| ID | App | Purpose | Key components | Empty / error states | Mobile | Accessibility |
|---|---|---|---|---|---|---|
| SCR-P12-01 IP Home | web | Portfolio control | Tiles per FR-P12-38; deadline list; stale list | "Add your first mark or import your portfolio" | Tile list | Tiles as headings + lists |
| SCR-P12-02 Portfolio Register | web | All assets | Grid: asset, type, class(es), status chip, valid until, next deadline, freshness, owner entity, agent | Filter none → clear | Card list | Keyboard grid |
| SCR-P12-03 Trademark Workspace | web | One mark | Tabs: Overview, Timeline, Deadlines, Documents, Watch, Agreements, Disputes, Use evidence, Notes | — | Section menu | Timeline as ordered list |
| SCR-P12-04 Add mark / import | web, mobile | Add by application number or import | Number field, office, class, status picker; Excel import with preview | Duplicate → link (`LD-IPM-002`) | ≤ 3 taps | Error summary |
| SCR-P12-05 Assisted refresh | web, mobile | Upload status evidence | Upload/share target, extraction diff, confirm | Low confidence → highlighted fields | Share sheet from browser/PDF viewer | Diff announced field by field |
| SCR-P12-06 Class finder | web, mobile | Business description → classes | Chat-style input, suggestions with reasons, term picker | AI unavailable → class list browser | Full | Plain language |
| SCR-P12-07 Knock-out screen | web | Screening results | Results list, match reasons, score chip with text, sources and dates, "Get an opinion" | No licensed source → own-portfolio-only notice | Read-only | Score never colour-only |
| SCR-P12-08 Data sheet | web | TM-A preparation | Stepper, validation, fee summary with categories, hand-off | Validation errors inline | Not on phone (tablet allowed) | Stepper landmarks |
| SCR-P12-09 Examination & hearing | web | Objections | Report viewer, grounds, cited marks, reply outline, hearing prep checklist | — | Read-only summary | — |
| SCR-P12-10 Watch Queue | web, mobile | Journal hits | Side-by-side marks, score, reasons, days left, decision buttons | No hits → "No similar marks in Journal <no.>" | Swipe decisions with confirm | Days-left text |
| SCR-P12-11 Journal Ingestion (ops/admin) | web | Upload or partner status | Upload PDFs, parse report, quality metrics | Parse failure → retry, manual entry | — | — |
| SCR-P12-12 Other IP registers | web | Copyright, design, patent, domain | Typed forms, deadlines | — | Card list | — |
| SCR-P12-13 IP Reports | web | IPM-01–06, board section | Report catalogue, exports | — | PDF view | Tagged PDF where possible |
| SCR-P12-14 My Brands | web, mobile (Personal) | Individual view | Plain-status cards, reminders, get help | "Have your application number ready" | Primary | 10 languages |

## 7. Backend design

### 7.1 Modules

`ipm` (owner; schema `ipm`); uses `dms`, `dix`, `rul` (status mappings, deadline rules, fee table, class-term list, related-class table), `lit` (matters and clocks engine), `tpl`/`clm`/`sgn` (agreements), `mkp` (SKUs, engagements), `wf`, `ntf`, `ai`/`agt`, `bil`, `int` (adapters, IP mailbox), `rpt`, `xpt`, `mob`.

### 7.2 Tables (schema `ipm`; `tenant_id`, `legal_entity_id`, RLS deny-by-default, ledger pointer on every row)

| Table | Key columns | Indexes | Retention |
|---|---|---|---|
| `assets` | id `tmk_`, ref `LD-TMK-…`, type, title, owner_ref, joint_owners jsonb, jurisdiction, status, status_raw, source, last_refreshed_at, business_owner_id, confidentiality | (tenant, type, status), GIN(title) | Life of asset + 8 years after lapse [REC] |
| `trademarks` | asset_id, mark_type, mark_text, translit jsonb, image_document_id, vienna_codes, classes int[], specs jsonb, application_no, filing_date, priority jsonb, use_claim jsonb, applicant_category, journal_no, journal_date, registration_date, valid_until, agent_text, engagement_id | unique (tenant, office, application_no) | as assets |
| `status_events` (append-only) | asset_id, seq, state, raw_label, published_on, recorded_at, source, evidence_document_id, actor_id, corrects_seq | (asset_id, seq) | as assets |
| `field_provenance` | asset_id, field, value, source, source_ref, captured_at | (asset_id, field) | 3 years after lapse |
| `clocks` | reuse `lit.clocks` with subject_type = IPM_ASSET | — | — |
| `data_sheets` | asset_id, payload jsonb (TM-A fields), validation jsonb, state, handed_off_to | (tenant, state) | 8 years |
| `screenings` | query jsonb, sources jsonb, results jsonb, score, run_at, requested_by | (tenant, run_at) | 3 years |
| `watch_profiles` | asset_id, classes, match_types, sensitivity, recipients | (tenant) | while active |
| `journals` | journal_no, published_on, source, file_hash, entry_count, parse_quality | unique (journal_no) — platform-level table, no tenant data | Permanent (public publication) |
| `journal_entries` | journal_no, application_no, mark_text, classes, applicant_text, image_ref, specs | (journal_no), trigram index on mark_text | 5 years |
| `watch_hits` | profile_id, journal_entry_id, score, reasons jsonb, opposition_last_date, decision, reason, decided_by, matter_id | (tenant, decision, opposition_last_date) | 3 years after decision |
| `copyrights` / `designs` / `patents` / `domains` / `confidential_items` | type-specific fields per FR-P12-31 | per type | as assets |
| `ip_agreements_links` | asset_id, agr_id, role (LICENCE_OUT, LICENCE_IN, ASSIGNMENT, COEXISTENCE), recordal_status, recordal_evidence_id | (asset_id) | as agreement |
| `use_evidence` | asset_id, year, document_ids, summary | (asset_id, year) | as assets |
| `valuation_notes` | asset_id, cost_basis numeric, revenue_lines jsonb, importance, notes, report_document_id | (asset_id) | as assets |
| `enforcement_log` | asset_id, sighting jsonb, evidence_document_id, action, matter_id | (asset_id) | as assets |

Journals and parsed entries are public publications stored once at platform level (no tenant data) and joined to tenant watch profiles at match time; hits are tenant rows.

### 7.3 APIs (REST under `/v1/ipm/` per FR-P19-03 and Appendix I §I.5; scopes `ipm.<resource>:<action>`; `Idempotency-Key` on mutations)

| Method | Path | Scope | Notes |
|---|---|---|---|
| GET/POST | `/assets` · GET/PATCH `/assets/{id}` | `ipm.asset:read` / `ipm.asset:write` | Type-specific payloads |
| POST | `/assets/{id}/status-events` | `ipm.status:write` | Evidence required |
| POST | `/assets/{id}/refresh-uploads` | `ipm.status:write` | Multipart; starts extraction |
| POST | `/refresh-uploads/{id}:confirm` | `ipm.status:confirm` | Atomic status + clocks + audit |
| POST | `/class-finder` | `ipm.assist:run` | AI; credits |
| POST | `/screenings` | `ipm.assist:run` | Licensed sources only |
| POST | `/data-sheets` · POST `/data-sheets/{id}:handoff` | `ipm.filing:*` | Creates P16 order or assigns own agent |
| POST | `/assets/{id}:record-filing` | `ipm.filing:record` | Agent/professional only |
| GET | `/assets/{id}/deadlines` | `ipm.asset:read` | Clocks with rule IDs and verification status |
| GET/POST | `/watch-profiles` · GET `/watch-results` · POST `/watch-results/{id}:decide` | `ipm.watch:*` | OPPOSE creates P11 matter |
| POST | `/journals` (platform) | `ipm.journal:ingest` | `OPS_CONTENT_PUBLISHER` or partner adapter |
| POST | `/assets/{id}/agreements` | `ipm.agreement:link` | Opens P06/P07 flow |
| POST | `/imports` · `:commit` · `:undo` | `ipm.import:*` | Facade over `xpt.import_jobs` (`source_kind = IPM_REGISTER`; R-A-10) |
| GET | `/reports/{code}` | `rpt.report:read` | — |
| GET | `/m/v1/my-brands` | mobile BFF | — |

### 7.4 Domain events

`in.lawdocs.ipm.AssetCreated.v1`, `DataSheetReady.v1`, `TrademarkFiled.v1`, `StatusChanged.v1`, `ExaminationReportReceived.v1`, `HearingScheduled.v1`, `TrademarkAdvertised.v1`, `OppositionReceived.v1`, `TrademarkRegistered.v1`, `RenewalWindowOpened.v1`, `TrademarkRenewed.v1`, `AssetLapsed.v1`, `StatusRefreshProposed.v1`, `StatusRefreshConfirmed.v1`, `ScreeningCompleted.v1`, `DataSheetHandedOff.v1`, `JournalIngested.v1`, `WatchHitCreated.v1`, `WatchHitDecided.v1`, `OwnershipGapDetected.v1`, `RecordalEvidenced.v1`. No cross-product events on Ecosystem Spec v1.1 contracts (IP data stays in LawDocs; the Operations Hub receives only usage counts for billing, NN-19). Proposed for v1.2 and inert until Appendix Y is merged: `ip.IpAssetRegistered` / `ip.IpAssetStatusChanged`, produced by `int` from `ipm.AssetCreated` / `ipm.StatusChanged` only to the same organisation's LawDocsComply tenant and only when the tenant opts in (Appendix Y §Y.7.3; Appendix I §I.8).

### 7.5 Jobs and workflows

`AssistedRefreshWorkflow`, `RegistryMailParserJob` (inbox), `RefreshPromptJob` (daily), `ClockWatcher` (shared with P11), `JournalIngestWorkflow` (on upload or partner delivery), `WatchMatchWorkflow` (per Journal; parallel by class), `WatchEscalationJob` (daily), `RenewalWindowJob` (daily), `OwnershipGapJob` (weekly), `ImportWorkflow` (undo timer), `PartnerSyncJob` (flagged OFF).

## 8. Integrations

| Port / adapter | Use | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `TRADEMARK_DATA_PORT` → `ManualAppNo`, `AssistedRefresh`, `RegistryMailParser` | Status capture | — | Extraction failure → manual form | Always available |
| `TRADEMARK_DATA_PORT` → `WipoBrandDb` | Screening and status cross-check | WIPO data licence; licensed partner [VERIFY] | OFF; screening limited to own portfolio | Own portfolio + professional search SKU |
| `TRADEMARK_DATA_PORT` → `LicensedPartner` | Status sync and Journal watch | Partner TBD [VERIFY] | Kill switch (NN-39); fall back to manual upload | `MANUAL_UPLOAD` journals |
| `dix` / `TRANSLATE_PORT` | OCR of Journal PDFs, reports, e-mails; transliteration variants | Tesseract/PaddleOCR + Claude vision (Bedrock India) | Partial parse flagged | Manual entry |
| `ai` gateway | Class finder, screening explanation, reply outlines | Claude via Bedrock India (D-14) | AI unavailable banner | Class list browser |
| `mkp` (P16) | Filing, reply, renewal, opinion, watch-review SKUs | — | Order failure → retry | Own agent recorded manually |
| `BILLING_PORT` (OH8) | Plan limits, `LD-ADD-TMW`, AI credits, government fee pass-through | — | Buffered usage | — |
| `int` IP mailbox | Registry e-mail forwarding | SES inbound / M365 shared mailbox | Queue | Upload |

## 9. Settings and configuration (register in Appendix R)

Keys marked **(R)** are already in Appendix R §R.9; the others are new for registration by this phase.

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `ipm.marks.max` (R) | PLN | int | 1 / 3 / 10 / 50 / unlimited (R6 [OWNER TO SET]) | `PLT_SUPER_ADMIN` | Y |
| `ipm.plan.watch_limit` | PLN | int | Pro 10, Business 50 (+25 per `LD-ADD-TMW`) | `PLT_SUPER_ADMIN` | Y |
| `ipm.journal_watch.enabled` (R) | PLN→TEN | bool | Pro+ add-on | `ORG_ADMIN` | N |
| `ipm.data.sources` (R) | PLT | list | WIPO Global Brand Database + licensed partner [VERIFY] | `PLT_SECURITY_OFFICER` | Y |
| `ipm.ip_india_scraping` (R) | PLT | bool, LOCKED | false (CH-27, NN-05) | — | — |
| `ipm.status.manual_refresh_label` (R) | PLT | bool, LOCKED | true (source and fetched-at shown) | — | — |
| `ipm.timelines.rule_set` (R) | PLT | ref | `rulepack.IN.ipm.tm_timelines` latest VERIFIED | `PLT_LEGAL_REVIEWER` | Y (NN-30) |
| `ipm.fees.table_version` | PLT | ref | latest verified | `PLT_LEGAL_REVIEWER` | Y |
| `ipm.nice.edition` | PLT | text | edition in force at IP India [VERIFY] | `PLT_CONTENT_EDITOR` | Y |
| `ipm.renewal.reminder_offsets_months` (R) | TEN→USR ↑ | list | [12, 6, 3, 1] (+ 7 days final) | `ORG_ADMIN`, user | N |
| `ipm.reminders.<clock_code>` | TEN ↑ | list (add only for statutory clocks) | per FR-P12-07 | `ORG_CLO` | N |
| `ipm.data.recent_days` | TEN | int | 30 | `ORG_CLO` | N |
| `ipm.data.stale_days` | TEN ↓ | int | 60 | `ORG_CLO` | N |
| `ipm.refresh.prompt_days` | TEN | int | 30 | `ORG_CLO` | N |
| `ipm.extract.min_confidence` | PLT | dec | 0.85 | `PLT_SRE` | Y |
| Adapter kill switches `wipo-branddb`, `tm-journal-watch` and the partner's key (registered in P19 `int.connectors.kill_switch_key`; FR-P19-81) | PLT | bool | OFF until terms or contract cleared | `PLT_SUPER_ADMIN` (re-enable needs `PLT_SECURITY_OFFICER`) | Y (NN-39) |
| `ipm.watch.journal_source` | PLT | enum PARTNER/MANUAL_UPLOAD | MANUAL_UPLOAD | `PLT_SUPER_ADMIN` | Y |
| `ipm.watch.auto_fetch.enabled` | PLT | bool | false (NN-38; terms check) | `PLT_SUPER_ADMIN` + `PLT_LEGAL_REVIEWER` | Y |
| `ipm.watch.similarity_threshold` (R) | TEN | dec 0.5–0.95 | 0.75 (STRICT 0.85 / STANDARD 0.75 / BROAD 0.6 presets) | `ORG_ADMIN` | N |
| `ipm.watch.auto_dismiss_below` | TEN | enum OFF/LOW | OFF | `ORG_CLO` | Y |
| `ipm.watch.escalate_days_before_deadline` | TEN | int | 30 | `ORG_CLO` | N |
| `ipm.filing.checker_required` | TEN | bool | true | `ORG_CLO` | Y |
| `ipm.use_evidence.reminder_month` | TEN | enum month | April | `ORG_CLO` | N |
| `ipm.flag.logo_similarity` | PLT | bool | false (v1.1) | `PLT_SUPER_ADMIN` | Y |
| `agt.autonomy.agent.AGT_TM_WATCH` (R family) | TEN | enum L0–L3 | L1 (L3 only for status-sync proposals and alerts) | `ORG_CLO` within ceiling | Y |

## 10. Security, privacy and audit

- **Data classes:** assets CONFIDENTIAL (unpublished applications, filing strategy, watch decisions); public Journal data PUBLIC; valuation notes and enforcement plans CONFIDENTIAL; professional opinions LEGAL_PRIVILEGED (excluded from AI retrieval outside the IP team and from auditor grants).
- **Threats and controls:** leakage of pre-filing brand plans (tenant-scoped search and embeddings, NN-15; screening queries never sent to partners without the tenant enabling that source); spoofed status evidence (originals hashed; extraction diff reviewed; source labels); agent over-reach (engagement-scoped access, NN-17); portal automation (dependency/egress rules, NN-05).
- **Personal data:** applicant individuals' addresses and IDs minimised; Journal entries contain third-party applicant names that are public, stored once, used only for matching; DPDP notice covers screening and watch as purposes [INTERP].
- **Audit:** every status change, refresh confirmation, screening run, data-sheet hand-off, filing record, watch decision, agreement link, import and export is a ledger event (NN-02, NN-45).

## 11. AI touchpoints and guardrails

| Touchpoint | Agent / feature | Autonomy | Human confirmation | Evaluation |
|---|---|---|---|---|
| Status extraction from uploads and e-mails | `AGT_TM_WATCH` | L1 default; L3 ceiling for sync proposals and alerts (never commits) | Maker confirms each change | Field accuracy ≥ 98% on 500 seeded status pages; 0 wrong clock starts |
| Class finder | Vidhi | L1 | User and agent confirm classes | Top-3 class recall ≥ 95% on 300 business descriptions |
| Screening explanation | Vidhi | L1 | Labelled screening aid; opinion by professional | No "registrable"/"safe" conclusions (refusal tests) |
| Reply outline | `AGT_TM_WATCH` | L1 | Agent/advocate finalises and files (NN-13) | Grounds recall ≥ 95%; zero fabricated citations (NN-14) |
| Watch similarity | Deterministic matchers + embeddings | L3 for creating hits (internal) | Reviewer decides every hit | Precision/recall on a labelled Journal set; logged per release |
| Reminders | `AGT_TM_WATCH` | L3 (internal reminders only) | — | — |

The agent has no tool that reaches IP India or any registry, files a form or sends to a third party (NN-05, NN-13). Appendix H binds `AGT_TM_WATCH`'s `ipm.sync_status` and `ipm.journal_similarity` tools to `TRADEMARK_DATA_PORT` and `TM_JOURNAL_PORT` adapters only; R4 LV-10's `ipindia.sync` wording is superseded because no official IP India API exists.

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p12/*.feature`)

```gherkin
Feature: Trademark tracking

  @P12-AT-01
  Scenario: Add a mark by application number
    Given an individual on the Personal plan with 0 marks
    When the user adds application number "6543210" in class 32 with status "Marked for Exam"
    Then the asset shows "Waiting for examiner", source USER and a refresh prompt date 30 days ahead

  @P12-AT-02 @NN-05
  Scenario: No IP India portal automation
    Given the dependency and egress allowlists for apps/api and agents
    Then no code path automates tmrsearch.ipindia.gov.in or ipindiaonline.gov.in pages, CAPTCHAs or OTP entry
    And AGT_TM_WATCH has no tool with egress to IP India domains

  @P12-AT-03
  Scenario: Assisted refresh from a status PDF
    Given the user saved the e-Register status page as PDF
    When the user shares it to LawDocs
    Then extracted fields are shown as a diff with confidence
    And nothing changes until the maker confirms

  @P12-AT-04 @NN-38
  Scenario: Examination reply clock is advisory until verified
    Given rule TM-EXAM-REPLY is UNVERIFIED
    When an examination report received on 3 Nov 2026 is recorded
    Then a clock due on 3 Dec 2026 is created with an "Advisory — verify" badge
    And reminders are scheduled at 21, 14, 7, 3 and 1 days before

  @P12-AT-05
  Scenario: Validity computed from filing date
    Given a mark filed on 15 Mar 2019 is registered on 10 Feb 2021
    Then "valid until" shows 15 Mar 2029
    And the renewal window opens on 15 Mar 2028

  @P12-AT-06 @NN-20
  Scenario: Status wording is honest
    When any IP status screen renders vendor or user data
    Then it shows the source and date and contains no "live", "official" or "real-time" wording

Feature: Clearance and filing

  @P12-AT-07 @NN-14
  Scenario: Class finder suggests classes with reasons and a disclaimer
    When a user describes "cold-pressed juices sold online and in cafés"
    Then classes 32, 35 and 43 are suggested with reasons and approved terms
    And the result is labelled "suggestion — confirm with a trade marks agent"

  @P12-AT-08
  Scenario: Screening never concludes registrability
    When a knock-out screen returns no conflicts from the tenant's own portfolio
    Then the result reads "No similar marks found in the sources searched" with the sources and dates
    And it does not say "safe" or "registrable"

  @P12-AT-09 @NN-13 @NN-22
  Scenario: LawDocs prepares, the agent files, fees are separate
    Given a validated data sheet for 2 classes for a startup with DPIIT evidence
    When the user buys the filing SKU
    Then the price shows professional fee, LawDocs fee, government fee Rs 9,000 (2 x Rs 4,500) and GST separately before payment
    And the asset becomes NEW_APPLICATION only after the agent records application number and receipt

Feature: Journal watch

  @P12-AT-10
  Scenario: Similar mark in the Journal creates a hit with opposition last date
    Given watched mark "JUICEBERRY" in class 32
    When Journal 2275 dated 2 Nov 2026 contains "JUSBERRI" in class 32
    Then a hit is created with phonetic and transliteration reasons
    And the opposition last date shown is 2 Mar 2027

  @P12-AT-11
  Scenario: Oppose from a hit creates a P11 matter
    When the CLO decides OPPOSE on the hit
    Then a P11 matter of type TM_OPPOSITION is created with clock TM-OPPOSE-OTHERS due 2 Mar 2027
    And the hit links to the matter

  @P12-AT-12
  Scenario: Undecided hit escalates
    Given a hit with opposition last date 2 Mar 2027 is undecided on 31 Jan 2027
    Then the CLO receives an escalation alert

  @P12-AT-13 @NN-38
  Scenario: Automated Journal fetching stays off
    Given ipm.watch.auto_fetch.enabled is OFF
    Then the only Journal sources are partner deliveries and manual uploads

Feature: Ownership and agreements

  @P12-AT-14
  Scenario: Ownership gap is detected and closed by recordal
    Given a mark is applied for by founder "R. Mehta" and used by tenant company "Juiceberry Foods Pvt Ltd"
    Then an ownership-gap warning suggests an assignment
    When the assignment deed is stamped, signed and the agent uploads the recordal evidence
    Then the proprietor updates and the warning closes

Feature: Export

  @P12-AT-15 @NN-11
  Scenario: IP export folder structure
    When the company exports everything
    Then "04 Trademarks and IP/Trademarks/JUICEBERRY – Class 32 (LD-TMK-2026-000007)/04 Registration and Certificates/" contains the certificate
    And "04 Trademarks and IP/IP Portfolio.xlsx" lists every asset with numbers, dates, status and source
```

NN test files: `NN-01_ipm_tenant_scope.spec.ts`, `NN-02_ipm_status_events_append_only.spec.ts`, `NN-05_no_ipindia_automation.spec.ts`, `NN-13_agent_cannot_file.spec.ts`, `NN-14_ipm_ai_labels.spec.ts`, `NN-20_ipm_no_realtime_claims.spec.ts`, `NN-22_ipm_fee_separation.spec.ts`, `NN-38_ipm_unverified_rules_advisory.spec.ts`, `NN-39_ipm_adapter_kill_switch.spec.ts`, `NN-46_ipm_refresh_idempotency.spec.ts`.

## 13. Exit gate, deliverables and open items

**Deliverables:** `ipm` module and migrations; status taxonomy and mapping table; deadline rule pack with verification log entries; government fee table with `last_verified_at`; Nice class-term list and related-class table; Excel template `LD-TPL-IPM-v1.0`; templates (user affidavit, assignment, licence, co-existence, founder IP assignment — via P06); marketplace SKUs defined in P16 (filing per class, reply to examination report, hearing attendance, renewal, clearance opinion, watch-hit review); Journal ingestion pipeline (manual upload); similarity matchers with evaluation report; reports IPM-01–06; user guides and tutorial scripts ("Track your trademark", "Read your examination report", "What the Journal watch tells you").

**Exit checklist:**
1. All `@P12-AT-*` scenarios and NN tests green.
2. Pilot: 3 companies and 30 individuals; 150 marks onboarded; 4 consecutive Journals ingested and matched; ≥ 1 opposition matter opened from a hit; ≥ 10 assisted refreshes confirmed.
3. Every rule used in pilot VERIFIED or advisory-badged and logged (NN-38); fee table verified against the Trade Marks Rules 2017 First Schedule [VERIFY].
4. WCAG 2.2 AA / IS 17802 audit of SCR-P12-04, -05, -06, -10, -14 (NN-28).
5. Settings registered (Appendix R); help keys `hlp.ipm.*` registered.
6. **Export-map entries registered (NN-11):** record types `ipm.asset`, `ipm.trademark`, `ipm.status_event`, `ipm.data_sheet`, `ipm.screening`, `ipm.watch_profile`, `ipm.watch_hit`, `ipm.copyright`, `ipm.design`, `ipm.patent`, `ipm.domain`, `ipm.agreement_link`, `ipm.use_evidence`, `ipm.valuation_note`, `ipm.enforcement_log`. Company path: `04 Trademarks and IP/<Asset type>/<Mark or title> – <Class or number> (LD-TMK-…)/{01 Application and Filing, 02 Examination and Replies, 03 Journal and Opposition, 04 Registration and Certificates, 05 Renewals, 06 Use Evidence, 07 Licences and Assignments, 08 Watch Reports, 09 Correspondence}` plus `04 Trademarks and IP/IP Portfolio.xlsx` and `Deadlines.xlsx`; disputes stay under `03 Litigation and Disputes/` with cross-references. Individual path: proposed new folder `11 Trademarks and IP/` in the individual taxonomy (OI-P12-06). [Proposed sub-folder names for the Appendix K owner.]
7. Demo script: founder journey (class finder → screen → data sheet → filing SKU → agent records filing → assisted refresh → examination report → reply outline), company journey (import 50 marks → Journal watch hit → oppose → P11 matter), renewal and ownership-gap closure.

**Error codes (`LD-IPM-001`–`LD-IPM-016`):** 001 Application number format invalid for office · 002 Duplicate asset · 003 Plan asset limit reached · 004 Watch limit reached · 005 Source not enabled for screening · 006 Status change needs evidence or reason · 007 Extraction confidence too low to confirm in bulk · 008 Rule unverified — advisory · 009 Data sheet incomplete · 010 Fee category evidence missing · 011 Only the engaged professional can record a filing · 012 Journal parse failed · 013 Agents cannot file or contact third parties · 014 Recordal evidence required before owner change · 015 Import row errors · 016 Undo window expired. Each with user text and `hlp.ipm.err.<nnn>`.

**Open items (Appendix W):**

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-P12-01 | Verify all deadline seeds (Trade Marks Act/Rules 2017 rule numbers, extension positions; Copyright, Designs, Patents rules as amended 2024) | IP domain analyst | Advisory badges |
| OI-P12-02 | Verify government fee schedule and applicant categories (startup, small enterprise definitions) | IP domain analyst | Fee shown "as at <date>, to be confirmed by your agent" |
| OI-P12-03 | WIPO Global Brand Database terms for commercial reuse, or a licensed partner | Integration lead + [COUNSEL] | Own-portfolio screening only |
| OI-P12-04 | IP India website terms for automated retrieval of published Journal PDFs | [COUNSEL] | Manual upload |
| OI-P12-05 | Select licensed TM data/watch partner (lawful source warranty, residency, DPDP) | Integration lead | Manual upload |
| OI-P12-06 | Add `11 Trademarks and IP/` to the individual export taxonomy | Appendix K owner | Export under `99 System Data/IP/` |
| OI-P12-07 | Role sub-types `TRADE_MARKS_AGENT`, `PATENT_AGENT` under `PRO_OTHER` in Appendix D; marketplace rules for agents (R6 suggests 0% commission pending agent conduct rules [VERIFY]) | Appendix D/M owners + [COUNSEL] | Treat as regulated; no commission |
| OI-P12-08 | Appendix I: add `TRADEMARK_DATA_PORT` capabilities `AssistedRefresh` and `RegistryMailParser` and the optional `searchMarks`/`watchJournal` methods | Integration lead | Manual entry |
