# Phase P05 — Document Intelligence: OCR, Handwriting/Screenshot Type Copy, Translation

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (canonical document model, `drv_` renditions, ingest workflow, `packages/dix` baseline with print OCR and Aadhaar mask-before-commit, viewer, redaction tool, confidentiality classes), P09 runtime (`packages/ai` gateway: Claude vision and text via Amazon Bedrock India, guardrails, prompt registry, evaluation harness, credit metering), P08 (`sgn` evidence ledger and `Bsa63CertificateService`), P03 (rule engine, settings registry), P16 (marketplace fulfilment for certified translation and expert Part B services — stubbed until P16 ships). External: OCR engines (self-hosted), `TRANSLATE_PORT` adapters (Bhashini [VERIFY], Google/Azure India-region fallbacks), Bedrock India.
> **Sequencing:** Wave 2. Sprints 1–2: engine router, print OCR upgrade, handwriting and screenshot reading, Aadhaar detection on derived text; sprints 3–4: type copy generator, side-by-side editor, verification and labels, WhatsApp export parser; sprint 5: language identification and machine translation with glossary locks; sprint 6: extraction, classification and PII redaction suggestions; sprint 7: evaluation sets, quality tiers, petition/claim attachment contracts with P10/P15, hardening. P10 consumes the type-copy and translation rendition contract from sprint 4 (freeze point: `drv_` kinds, labels and anchor format at end of sprint 3).
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (personas), F (eligibility families — classification feeds the gate), H (agent roster — `AGT_EVIDENCE_CLERK` #8, `AGT_TRANSLATOR` #9, `AGT_DMS_LIBRARIAN` #20), K (`LD-EXPORT-1.0`), R (settings), W (open items).
> **Requirements covered:** R-044, R-045, R-046 (correct AI errors), R-008, R-043; contributes to R-007, R-012, R-061, R-079 (pleadings annexures), R-083 (grievance evidence), R-025.
> **Decisions applied:** D-07, D-14, D-15 · **Challenges applied:** CH-11, CH-28 · **Non-negotiables tested:** NN-04, NN-09, NN-10, NN-13, NN-14, NN-15, NN-25, NN-28, NN-32, NN-38, NN-43, NN-46, NN-48
> **Estimated effort:** 7 two-week sprints, squad of 8 (ML/AI engineers 2, backend 2, web 1, linguist-QA 1, evaluation/data 1, QA/accessibility 1), plus a part-time panel of language reviewers for the evaluation sets.

---

## 1. Objective and business outcome

Litigants and companies in India rely on documents that machines read badly: handwritten agreements and letters, photographed registers, WhatsApp chats, screenshots of UPI payments and bank messages, regional-language notices. The brief asks that AI "reads WhatsApp screenshots and handwritten documents, attaches them to the petition/claim with the typed copy; users can correct AI errors", plus translation into English (R-044, R-045, R-046).

P05 delivers that safely. The original stays the evidence (NN-09); everything the machine produces is a **derived rendition** — labelled, versioned, anchored to the page and line it came from, with confidence shown, corrected by a human and signed off before it is used in a filing. WhatsApp evidence is ingested from the **native chat export** wherever possible, hashed at upload and supported by a BSA 2023 s.63(4) certificate workflow (CH-28; R3 LG-091). Machine translations are labelled as such; filings route to certified translation (NN-48; CH-11).

| Outcome | Exit-gate measure |
|---|---|
| Handwriting usable | On the evaluation set, printed English/Hindi OCR character error rate (CER) ≤ 2%; handwritten English CER ≤ 8%, handwritten Hindi ≤ 12% before human correction **[targets to be confirmed by baseline run]**; every line carries a confidence band and a page/line anchor |
| Human in control | 100% of type copies attached to a filing are in `USER_CORRECTED` or `VERIFIED` status, or carry an explicit "not verified" acknowledgement shown in the bundle index |
| WhatsApp done right | A native export ZIP of 10,000 messages parses in ≤ 60 s with zero dropped lines on the 12 locale fixtures; ambiguous date formats are asked, never guessed |
| Languages | Language identification on 28 languages (22 Eighth-Schedule + 6 UN official languages) with per-language quality tiers published; translation to English available for all, marked machine translation |
| Aadhaar never leaks into derived text | Zero unmasked Aadhaar numbers in OCR text, type copies, translations, extractions, search index, logs (NN-04) on the red-team set |
| Extraction saves time | Parties, dates, amounts and key clauses proposed for ≥ 85% of agreements in the evaluation set with precision ≥ 0.95 on confirmed fields; obligations proposed to P07 |
| Court-ready | One action attaches original + type copy + translation as paired annexures to a P10 petition or P15 claim, with index rows, page references and the s.63 Part A draft |

---

## 2. Scope (in / out)

**In scope**

- Engine router for OCR, vision reading and translation by content type × language/script × data class.
- Print OCR (deterministic engines) upgrade from the P04 baseline: layout, tables, reading order, multi-column, stamps/seals detection.
- Handwriting, screenshot and photographed-document reading with Claude vision (Bedrock India).
- Native WhatsApp chat-export ingestion (Android/iOS variants), chat screenshots, SMS/UPI/bank-app screenshots, email files.
- Type copy generation in court-acceptable formats with page/line anchors; side-by-side correction editor; confidence highlighting; verification and reviewer sign-off; fixed labels.
- Attachment contract for petitions (P10) and consumer claims/grievances (P15).
- BSA s.63 certificate workflow for uploaded electronic records (using the P08 service).
- Language identification for 28 languages and code-mixed romanised Indic; machine translation to English and between supported languages; legal glossary and term locks; back-translation checks.
- Certified-translation hand-off (marketplace, P16).
- Aadhaar detection and masking on all derived outputs (defence in depth over P04).
- Classification, metadata and clause/obligation extraction; PII redaction suggestions.
- Evaluation sets and quality tiers per language; regression gates per model/engine version.
- Credit metering hooks.

**Out of scope (owner)**

| Item | Owner |
|---|---|
| Storage, versions, sharing, viewer, manual redaction tool | P04 |
| Court render profiles, annexure builder, bundle pagination, e-filing exports | P10 (P05 supplies renditions and anchors) |
| Vidhi Q&A over documents, summaries, legal research | P09 |
| Obligations register and renewals | P07 (`clm`) — P05 proposes |
| Signed-document evidence packs and the certificate generator itself | P08 |
| Certified translators' and experts' engagement, payment and payout | P16 |
| Voice-note transcription for Vidhi intake | P09 (shares the language catalogue) |

---

## 3. Personas and permissions touched

| Role code | What they can do in P05 |
|---|---|
| `IND_OWNER`, `ORG_LEGAL_MAKER`, `ORG_MEMBER` (own uploads) | Request type copy, translation, extraction; correct type copies; self-attest; map chat senders; request certified translation and expert Part B |
| `ORG_CHECKER` | Verify type copies and translations as independent reviewer (maker ≠ checker for company filings, tenant setting) |
| `ORG_CLO` | Set tenant routing restrictions (tighten only), approve translation glossary entries for the tenant |
| `PRO_ADVOCATE` (engaged) / `ORG_EXT_COUNSEL` | Verify type copies under engagement scope; only an advocate's attestation permits the label "TRUE TYPED COPY" |
| `PRO_OTHER` (translator, transcriptionist, forensic examiner) | Fulfil certified translation or Part B expert certificate under a marketplace engagement (P16) |
| `OPS_PROFESSIONAL`, `OPS_CONSUMER_CASE_MANAGER` | Prepare and correct type copies under a delivery grant (NN-17); cannot self-attest for the client |
| `CP_GUEST` | Views shared type copies/translations with their labels; may dispute a type copy in a shared matter |
| `PLT_CONTENT_EDITOR`, `PLT_LEGAL_REVIEWER` | Maintain legal glossary, label strings, classification taxonomies and extraction schemas (content, NN-30) |
| `AGT_EVIDENCE_CLERK`, `AGT_TRANSLATOR`, `AGT_DMS_LIBRARIAN` / Vidhi | Maker only (NN-43): run OCR/translation/extraction on request, propose classifications; never verify, attest or attach to a filing |

---

## 4. Functional requirements

### 4A. Engine router and processing pipeline

**FR-P05-01 — Pipeline extension.** P05 adds stages to `DocIngestWorkflow` and an on-demand `DixJobWorkflow` (`dxj_` per job; `run_` is reserved for `ai.runs` — Appendix B §B.1): `LAYOUT` (page segmentation, reading order, tables, stamps/seals/signature regions) → `CONTENT_CLASSIFY` (printed / handwritten / mixed / chat screenshot / app screenshot / photo of document / email) → `LID` (§4J) → `READ` (engine per router) → `AADHAAR_DERIVED_CHECK` (§4M) → `CONFIDENCE` (§4F) → `PERSIST` (`drv_` + line anchors) → `INDEX` → optional `TYPE_COPY`, `TRANSLATE`, `EXTRACT`. Jobs are idempotent on (`ver_id`, job kind, engine version, settings hash); re-runs create a new `drv_` version, never overwrite (NN-09).

**FR-P05-02 — Routing table (default; tenants may tighten, never loosen).**

| Content | Language / script | Primary | Second engine (agreement check) | Data-class guard |
|---|---|---|---|---|
| Printed | English, 22 Eighth-Schedule languages | Deterministic OCR (PaddleOCR/Tesseract with Indic models, self-hosted ap-south-1) | Claude vision on low-confidence pages | Any class (self-hosted + Bedrock India) |
| Printed | ar, zh, ru, fr, es | Claude vision (Bedrock India) | Deterministic OCR (Latin/Cyrillic/Arabic/Han models) | Any class |
| Handwritten | Any | Claude vision (Bedrock India) | Second independent vision decode (different crop scale and prompt template) + deterministic OCR where the script is supported | Any class; human review mandatory for filing use |
| Chat / app screenshots | Any | Claude vision with bubble/layout prompt | Deterministic OCR on bubble crops | Any class |
| Native digital text (DOCX, text PDF, EML, WhatsApp TXT) | Any | Parser (no OCR) | — | Any class |
| Regional cloud OCR adapters (Google/Azure India regions) | Optional | Only if `dix.route.regional_cloud.enabled` and class ∈ {`PUBLIC`, `INTERNAL`} | — | Never for `CONFIDENTIAL*`/`RESTRICTED_PERSONAL` |

Fail-closed: if no allowed engine is available for the class, the job waits (`LD-DIX-003`); it never falls through to a non-India endpoint (NN-15, NN-25).

**FR-P05-03 — Engine registry.** `dix.engines` lists each engine/model version with languages, scripts, data classes allowed, residency, retention terms, cost per page, quality tier per language (§4O) and kill switch (NN-39). Routing reads the registry; changing an engine version triggers the regression gate (§4O) before it receives traffic.

### 4B. Print OCR

**FR-P05-04 — Layout-aware print OCR.** Deskew, de-noise, de-warp (phone photos), rotation, page split for book scans; reading order for multi-column notices and gazette-style pages; table extraction to grids (cells with anchors); detection and labelling of stamps, seals, court fee stamps, e-stamp certificate blocks, signatures and thumb impressions as regions (transcribed as `[stamp: …]`, `[seal]`, `[signature]`, `[thumb impression]` — never as a name unless printed).

**FR-P05-05 — Searchable PDF.** For every scanned version, produce a PDF/A-2b rendition with an invisible text layer aligned to the image (`drv_` kind `OCR_PDF`), used by the viewer, screen readers (NN-28) and search.

### 4C. Handwriting, photographs and screenshots

**FR-P05-06 — Vision reading.** Claude vision on Bedrock India reads handwritten pages, photographed documents and screenshots page by page with a fixed prompt from the prompt registry (versioned, evaluated). Output per line: text, bounding box, `[?word]` for uncertain words, `[illegible]` for unreadable regions, struck-through text as `~~text~~`, marginal notes as `[margin: …]`, insertions as `[inserted: …]`. The model is instructed to transcribe, not correct, interpret, translate or complete; outputs that add content absent from the image are caught by the agreement check (§4F) and the hallucination tests (§4O).

**FR-P05-07 — Screenshot understanding.** Classify UI (`WHATSAPP`, `SMS`, `EMAIL_APP`, `BANKING_APP`, `UPI_APP`, `SOCIAL`, `OTHER`); detect bubbles (left/right side, sender header, quoted reply, date separator, timestamps, read ticks as text only), status-bar time and date context. Multiple screenshots of one conversation are ordered by on-screen timestamps and overlap de-duplication; the user confirms the order. Tamper heuristics (font inconsistency, compression discontinuity, misaligned bubbles, status-bar vs message time conflicts) produce a `tamper_hint` flag shown only to the uploader as "Possible inconsistency — check before relying on this", never as a finding.

**FR-P05-08 — EXIF and device data.** EXIF/device metadata is read from the original (kept immutable in P04) for the s.63 Part A device section (§4I); location data is never written into renditions or shares.

### 4D. Native WhatsApp chat-export ingestion

**FR-P05-09 — Prefer native exports.** When a user uploads WhatsApp screenshots, the app explains (with a 3-step illustrated guide for Android and iPhone) that a native **Export chat** file is better evidence than screenshots and offers to import it. Screenshots remain supported.

**FR-P05-10 — Parser (`packages/dix/parsers/whatsapp`).** Detect ZIP containing `_chat.txt` or `WhatsApp Chat with *.txt`, or a TXT whose first 50 lines match known patterns. Variants with golden fixtures (≥ 12 locale/platform fixtures): Android 24-hour (`dd/mm/yy, hh:mm - Sender: text`), Android 12-hour (with U+202F before am/pm), iOS bracketed (`[dd/mm/yy, hh:mm:ss] Sender: text`), dotted/dashed date separators, system lines without sender. Rules:

1. Strip U+200E, U+200F, U+202F for parsing; keep the raw line for evidence.
2. Join continuation lines to the previous message.
3. **Date-order disambiguation**: a day value > 12 in position 1 → DD/MM; in position 2 → MM/DD; otherwise ask the uploader with a concrete example ("Is 03/04/24 the 3rd of April or March 4th?") — status `LOCALE_AMBIGUOUS` until answered (`LD-DIX-010`); never guess.
4. Media references (`IMG-YYYYMMDD-WA####.jpg (file attached)`, `<attached: …>`) link to ZIP entries by filename; each media file becomes a child document with its own hash (P04); `<Media omitted>` placeholders are counted and reported.
5. Typed events: text, media, system, deleted ("This message was deleted"), edited (`<This message was edited>` flag), call, view-once, forwarded marker.
6. Export-limit warning: if the earliest message is later than the dispute start date the user entered, show "Your export may be missing older messages" **[VERIFY current WhatsApp export message/media limits]**.
7. Chats protected by WhatsApp's advanced chat privacy setting cannot be exported; help text explains and offers screenshots **[VERIFY feature name and behaviour]**.

**FR-P05-11 — Sender mapping and privacy.** The uploader maps displayed sender names/numbers to parties ("Which of these is you? Which is the other party?"). Phone numbers of non-parties are masked to the last 4 digits in renditions shared outside the owner's workspace (default); the filing copy may show them in full only when an advocate or the owner unmasks them for that rendition with a reason (logged) [INTERP: data minimisation under DPDP s.6 and s.8; COUNSEL to confirm court-filing practice — OI-P05-04].

**FR-P05-12 — Integrity.** SHA-256 of the ZIP and every entry at upload (P04), original ZIP WORM; uploader identity, device user-agent, IP and time; notice: "WhatsApp exports are not digitally signed. The other party may dispute them." Action "Ask the other party to confirm this chat" (available where both are LawDocs participants in a shared matter or deal room): on acceptance the rendition is tagged `confirmed_by:<party>`. If the other party uploads its own export, a **counter-export diff** (match on timestamp ± 60 s, mapped sender, normalised text hash) lists messages present in one export only, edited-flag and media-count differences — a signal, never a finding.

### 4E. Type copy generation (court-acceptable format)

**FR-P05-13 — Type copy rendition.** `drv_` kind `TYPE_COPY`, DOCX + PDF/A-2b, generated from the corrected transcription using the render profile selected by P10 (`tpl` render profile; default "Indian courts — A4 general" until P10 profiles are verified **[VERIFY per forum: paper size, margins, font, line spacing — P10]**). Anatomy:

| Element | Content |
|---|---|
| Header (every page) | **"TYPE COPY"** + "of <annexure label or document title>, original at page <n>" + status line ("Machine transcription — not verified" / "Corrected by <name>" / "Verified by <name, capacity> on <date>") |
| Body — documents | Lines in original order; each original page starts a new section headed `[Original page n]`; every line carries an anchor `[p<n>:l<m>]` in the left margin (configurable to hidden-in-print, kept in the text layer) |
| Body — chats | Table: Msg # · Date · Time · Sender (party label) · Message (original language) · [English translation column, when requested] · Anchor `[WhatsApp msg <seq>, <dd-mm-yyyy hh:mm>]`; system/deleted/call events in italics; media as "[Image: IMG-20240315-WA0001.jpg — see Annexure P-4/12]" |
| Markers | `[?word]`, `[illegible]`, `~~struck~~`, `[margin: …]`, `[stamp: …]`, `[signature]`, `[thumb impression]` |
| Footer (every page) | "Original SHA-256: <first 16 hex>… · Engines: <list and versions> · Uncertain passages marked [?] and [illegible]" |

**FR-P05-14 — Anchors are stable.** Anchors (`doc_version_id`, page, line, bounding box, engine, model version, confidence band) are stored in `dix.lines`; P10 pleadings cite them ("Annexure P-3 at page 45, line 12; type copy at page 48") and resolve them when the bundle is paginated.

**FR-P05-15 — "TRUE TYPED COPY".** The words "TRUE TYPED COPY" are used only when an advocate under engagement scope (or a verifier with a declared professional capacity that the forum recognises) attests the copy and the render profile's practice requires it; otherwise the label is "TYPE COPY". Lint blocks other wording (`LBL-TC-01`).

### 4F. Side-by-side correction editor and confidence

**FR-P05-16 — Confidence bands per line.** Engines with calibrated confidences (deterministic OCR): `HIGH` ≥ 0.95, `MEDIUM` 0.80–0.95, `LOW` < 0.80 (minimum word confidence in the line). Vision outputs (no calibrated confidence): cross-decode agreement — normalised CER between the two decodes (and the deterministic engine where supported) after Unicode NFC and whitespace normalisation: ≤ 3% `HIGH`, 3–10% `MEDIUM`, > 10% `LOW`. Any line containing a number, amount, date, name, account/vehicle/case number or text adjacent to a signature is capped at `MEDIUM` until a human confirms it.

**FR-P05-17 — Editor (SCR-P05-03).** Left: original page (zoom, rotate, contrast, magnifier); right: editable transcription aligned line by line; hover a line → bounding box highlights; `LOW` lines amber with dashed outline, `MEDIUM` pale yellow, engine disagreements underlined with the alternative on hover ("Second read: ₹1,50,000"); keyboard: `Alt+↓/↑` next/previous uncertain line, `Ctrl+Enter` accept line, `Ctrl+I` mark illegible; Indic input (InScript and phonetic transliteration); progress bar (lines reviewed / total). All `LOW` lines must be reviewed before "Submit corrections". Every correction is tracked (who, when, old → new) and visible in a change list; corrections never alter the original.

**FR-P05-18 — Mobile editing.** On phones the editor shows one line at a time with the cropped region above it ("Is this right?" Yes / Edit / Can't read); budget **≤ 2 taps per confirmed line**.

### 4G. Verification, sign-off and labels

**FR-P05-19 — Status machine.** `MACHINE_DRAFT → USER_CORRECTED → VERIFIED`; `DISPUTED` (another party objects with reason in a shared matter); `SUPERSEDED` (newer type copy). Verification options: (a) **self-attestation** by the uploader: "I have compared this type copy with the original and it is accurate to the best of my knowledge"; (b) **independent verification** by `ORG_CHECKER`, an engaged advocate, or a marketplace transcriptionist (P16 service); (c) for handwriting used in a filing, `VERIFIED` requires (b), or (a) plus zero unresolved `LOW` lines. The attestation records name, capacity, date, IP, the SHA-256 of the original version and of the type-copy text, and is signed in-app (e-acceptance; or eSign/DSC through P08 where the tenant requires).

**FR-P05-20 — Labels are fixed content.** Label strings (all UI languages) are platform content with IDs (`lbl.typecopy.machine`, `lbl.typecopy.corrected`, `lbl.typecopy.verified`, `lbl.translation.machine`, `lbl.translation.reviewed`, `lbl.translation.certified`), not editable by tenants; renderers refuse to output a type copy or translation without its label.

**FR-P05-21 — Never without the original.** Any bundle, share or export that includes a type copy or translation includes the original first (assembler rule; P10 and P04 share packs enforce it — a share pack item of kind type copy automatically adds the original unless the owner removes it with an acknowledgement).

### 4H. Attachment to petitions and claims (P10 / P15 contract)

**FR-P05-22 — Annexure pairs.** From the P10 annexure picker or a P15 claim, selecting an original with renditions offers "Include type copy (recommended)" and "Include translation". The annexure map adds separate index rows: `P-n` (original), `P-n(T)` (type copy), `P-n(Tr)` (translation, with its label kind), each with page ranges; body references resolve to the original. Unverified type copies or machine translations may be attached only after the user confirms "This type copy is not verified" / "This is a machine translation, not certified"; the bundle index shows the status in the row description, and P10's scrutiny check records a warning.

**FR-P05-23 — Consumer claims (P15).** For loan/insurance grievances and consumer complaints, the claim pack builder uses the same pairs; portals that take only uploads by the user (RBI CMS, IRDAI Bima Bharosa, e-Jagriti) receive a downloadable pack the user files themselves (NN-23, NN-05).

### 4I. BSA 2023 s.63 certificate workflow for uploaded electronic records

**FR-P05-24 — Scope.** BSA 2023 s.63(4) requires a certificate in the form in the Schedule, with Part A by the party/person in charge and Part B by an expert, identifying the electronic record, the device and the **hash value** (R3 LG-091; *Pune Bar Assn. v. UoI*, 2026 SCC OnLine SC 1297 **[VERIFY citation]**) **[LAW]**. P05 applies it to uploaded electronic records — WhatsApp exports, screenshots, emails, native digital files, audio/video. A scan of a **paper** document is not the electronic record in issue; the paper original is primary evidence and must be produced; the type copy is a reading aid. The certificate offer therefore appears only for `source_kind ∈ {ELECTRONIC_NATIVE, SCREENSHOT, CHAT_EXPORT, EMAIL, AUDIO_VIDEO}` [INTERP].

**FR-P05-25 — Part A draft.** Generated by `sgn.Bsa63CertificateService` (P08) with P05 inputs: deponent details (the uploader), record description (file names, types, sizes, date range, source app), device/source (user-entered make, model, serial/IMEI — IMEI masked in party views, full only in the signed certificate), lawful-control and proper-operation statements (user selects), hash table (file · SHA-256 (+ SHA-512 optional) · size · computed at (UTC) at upload · "computed by LawDocs platform v<x>"), place, date, signature (eSign/DSC through P08, or print for wet-ink). Field labels follow the Schedule form **[VERIFY: every field label against the Gazette text before activation; `PLT_LEGAL_REVIEWER` sign-off]**; feature flag `dix.bsa63.enabled` (offer for uploaded records) OFF until verified, and it can be ON only while the P08 service flag `sgn.bsa63.enabled` is ON (NN-38).

**FR-P05-26 — Part B request.** "Get Part B from an expert" opens a marketplace service (P16): an Examiner of Electronic Evidence notified under IT Act s.79A, or another expert accepted by the forum (scope left open by the Supreme Court — R3 LG-091) **[COUNSEL]**; the expert receives the record hashes and a re-hash tool, never broader vault access.

**FR-P05-27 — Re-hash at export.** Every court export re-computes hashes and compares with the ledger; a mismatch raises `HASH_MISMATCH_CRITICAL` (P1 incident) and blocks the export.

### 4J. Language identification

**FR-P05-28 — Language catalogue (`dix.languages`).** 28 languages: Assamese (as), Bengali (bn), Bodo (brx), Dogri (doi), Gujarati (gu), Hindi (hi), Kannada (kn), Kashmiri (ks; Perso-Arabic and Devanagari), Konkani (kok), Maithili (mai), Malayalam (ml), Manipuri (mni; Bengali and Meetei Mayek scripts), Marathi (mr), Nepali (ne), Odia (or), Punjabi (pa; Gurmukhi and Shahmukhi), Sanskrit (sa), Santali (sat; Ol Chiki and others), Sindhi (sd; Perso-Arabic and Devanagari), Tamil (ta), Telugu (te), Urdu (ur) — the 22 Eighth-Schedule languages — and Arabic (ar), Chinese (zh, Simplified and Traditional), English (en), French (fr), Russian (ru), Spanish (es) — the six UN official languages (D-07). Plus code-mixed romanised classes `hi-Latn`, `mr-Latn`, `ta-Latn`, `bn-Latn`, `kok-Latn`. Reading and translating a language does not mean the UI or templates exist in it (UI languages are the 10 launch languages).

**FR-P05-29 — Detection.** Per document, page, block and chat message: script classifier (Unicode blocks) → language model (self-hosted fastText-style LID for broad coverage; Indic-specialised LID adapter where evaluated) → disambiguation (Devanagari: hi/mr/ne/sa/kok/mai/doi/brx; Bengali script: bn/as/mni). Thresholds: ≥ 0.90 set; 0.60–0.90 set with "Language uncertain — confirm" chip; < 0.60 `und` and user selection required before translation. Romanised Indic with an Indic score ≥ 0.6 is classed `xx-Latn` and transliterated before translation; the romanised original is kept.

### 4K. Translation

**FR-P05-30 — Routing by data class.**

| Class (P04) | Allowed engines |
|---|---|
| `PUBLIC` | Any configured adapter |
| `INTERNAL`, `CONFIDENTIAL` | Claude (Bedrock India); Bhashini adapter only after terms/retention review **[VERIFY]**; Google/Azure India-region adapters only with zero-retention terms recorded and `dix.mt.regional_cloud.enabled` |
| `CONFIDENTIAL_LEGAL`, `RESTRICTED_PERSONAL` | Claude (Bedrock India) or a self-hosted model in ap-south-1 (candidate IndicTrans2-class model behind an ADR) only |
| Identity documents | No translation (names transliterated only on request) |

Fail-closed; cache key = (source SHA-256, from, to, glossary version, engine version).

**FR-P05-31 — Glossary and term locks.** `dix.glossary_terms` (content: term, language, target, source reference, statute reference, `do_not_translate`, status, approver = `PLT_LEGAL_REVIEWER` + language reviewer) seeded from the Legislative Department legal glossaries and authoritative Hindi texts of Central Acts **[VERIFY licence/reuse terms]**. Locked classes: statute names and section citations ("Section 138", "Order XXXIX Rule 2-A"), case names and citations, forum names, party names, amounts and currency, dates, case/CNR numbers, exhibit labels, emails/URLs, user-marked defined terms. Pre-process replaces locked spans with placeholders; post-check verifies each placeholder is restored exactly once and amounts/dates re-validate; failure flags the segment (`LD-DIX-021`).

**FR-P05-32 — Output.** `drv_` kind `TRANSLATION`: bilingual two-column view in-app; DOCX/PDF with paragraph alignment; segment confidence (engine score or back-translation similarity); label header on every page **"Translation — for convenience. Machine translation; not certified. The <source language> original is authoritative."** (`lbl.translation.machine`). Reviewed translations (`MT_DRAFT → REVIEWED` by a named reviewer) carry `lbl.translation.reviewed`; still "not certified". Between non-English pairs (e.g., Marathi → Hindi) translation pivots through English only when no direct engine is evaluated, and the label states the pivot.

**FR-P05-33 — Back-translation for high-stakes text.** Mandatory before a translation can be attached to a filing, a legal notice, a settlement or a consumer claim: translate A→B, then B→A with a different engine; per-segment semantic similarity (multilingual embeddings, in-region) and chrF++; segments below thresholds (`dix.mt.backtranslation.min_cosine` 0.85, `min_chrf` 50) are flagged "Meaning may have changed — review" and must be reviewed by a human.

**FR-P05-34 — Lint.** Machine or reviewed translations cannot contain "certified translation", "certified by", "official translation" or "sworn" outside fixed labels (`LBL-TR-01…03`).

### 4L. Certified translation hand-off (NN-48)

**FR-P05-35 — When required.** Documents not in the court's language need translations as the forum's rules require; Supreme Court and High Court proceedings are in English (Constitution Art. 348(1)); subordinate-court language is set by the State (CPC s.137) (R3 LG-093) **[VERIFY wording]**; forum rules on who may certify translations vary **[VERIFY per forum — R3 LG-094]**. When a P10 bundle targets a forum whose render profile marks `translation_certification_required`, machine and reviewed translations are blocked from the filing set and the user is offered certified translation.

**FR-P05-36 — Order flow.** Order (source documents, pair, purpose `COURT_FILING` / `CONSUMER_FORUM` / `FOREIGN_USE` / `OTHER`, certification type `TRANSLATOR_DECLARATION` / `NOTARISED` / `APOSTILLE_ASSISTED` / `COURT_APPROVED_TRANSLATOR`, deadline) → quote with GST shown before payment (NN-22, NN-50) → assignment to a marketplace translator with the language pair (P16; translators are non-regulated providers, RS-LD-25) → machine pre-translation offered to the translator, labelled internally → translator owns the output → second-linguist QA for court purposes → translator signs the certificate of accuracy (eSign/DSC via P08) → `drv_` kind `TRANSLATION_CERTIFIED` linked to the source version with certificate page (translator identity, qualifications, languages, source document title, pages and SHA-256, statement of accuracy, date, signature). Notarisation/apostille steps tracked as tasks. Where the forum requires a court-approved translator, LawDocs cannot certify; the export flags it.

### 4M. Aadhaar auto-masking and PII redaction

**FR-P05-37 — Derived-text Aadhaar check (NN-04).** Every derived text (OCR, vision transcription, type copy, translation, extraction values, embeddings input) passes the Verhoeff detector with spacing/separator variants and Indic-digit normalisation (Devanagari, Bengali, Gujarati, Gurmukhi, Odia, Tamil, Telugu, Kannada, Malayalam digits) before persistence. Detected numbers are replaced by `XXXX XXXX <last4>` in the text and burned into any rendered image region.

**FR-P05-38 — Late detection on an original.** If P05 detects an Aadhaar number in an original that the P04 print pass missed (e.g., handwritten), the system (1) creates a masked version, (2) purges the unmasked version (governance-mode object; crypto-shred; purge record with `pre_mask_sha256`), (3) notifies the owner and records `AadhaarMaskedLate`. Compliance-mode locking of an uploaded document as executed/evidence (P04 FR-P04-52) happens only after the full P05 Aadhaar pass completes, so late detection never meets a locked object; if it ever does (defect), it is a P1 incident with `PLT_DPO` decision.

**FR-P05-39 — PII redaction suggestions.** Model + pattern detection proposes redactions for: Aadhaar/VID, PAN, phone, email, bank account and IFSC context, card numbers (PCI — always suggested), passport, driving licence, voter ID, vehicle chassis/engine numbers, health terms, names and addresses of non-parties, minors' names. The user reviews suggestions in the P04 redaction tool; applying creates a `REDACTED` rendition (P04 FR-P04-48). Suggestions never auto-apply to shares unless the tenant enables "auto-redact card numbers in external shares" (`dix.redact.auto_card_numbers`).

### 4N. Classification and extraction

**FR-P05-40 — Classification.** Model-based document-type classification over the P04 catalogue, with confidence and top-3 alternatives; feeds P04 auto-apply rules (threshold, exclusions). **Eligibility-family suggestion** for Appendix F: if any detector signals an excluded family (will, codicil, trust deed, power of attorney, promissory note/bill of exchange) the document is tagged `eligibility_suspect` and the P08 gate treats it as excluded until a human reclassifies it with a reason — classification can tighten the gate, never loosen it (NN-07).

**FR-P05-41 — Extraction schemas.** Per document type (content, NN-30): parties (name, role, address, identifiers masked), dates (execution, effective, expiry, renewal notice, payment due), amounts (with currency, in figures and words cross-checked), property/vehicle identifiers, stamp certificate UIN, registration numbers, governing law, jurisdiction, arbitration seat, and clause classes (termination, renewal, lock-in, escalation, indemnity, limitation of liability, confidentiality, non-compete, dispute resolution, stamp/registration responsibility, payment terms, notice). Each value carries its anchor and confidence.

**FR-P05-42 — Review form.** Extractions appear as suggestions in the document's details pane ("Suggested by Vidhi — confirm"), never written to metadata until confirmed (NN-14). Confirmed dates become P04 reminder facts; confirmed parties link to `prs_`; confirmed obligations are proposed to P07 (`obl_` drafts) with clause anchors; amounts in figures vs words mismatch raises a health finding.

**FR-P05-43 — Notices and orders.** For incoming notices, demand letters and court/tribunal orders, extract issuer, reference, date, response deadline, amount demanded, statute cited (resolved against the rules register or shown as "unverified", NN-14), and propose a task with the deadline; P11 consumes order extraction for litigation.

### 4O. Quality evaluation sets and tiers

**FR-P05-44 — Evaluation sets (`dix.eval_sets`).** Built only from synthetic, public-domain or consented material — never customer data (NN-15). Minimum composition before a language can reach tier B: printed ≥ 200 pages; handwritten ≥ 100 pages (launch languages: en, hi, bn, mr, te, ta, gu, kn, ml, pa; others best effort); screenshots ≥ 300 images across app classes; WhatsApp exports ≥ 12 locale fixtures; translation ≥ 500 legal-domain segments per pair with reference translations by qualified linguists; extraction ≥ 300 annotated agreements (English, Hindi first). Each set is versioned, with datasheets (source, licence, consent, annotator, date).

**FR-P05-45 — Metrics.** OCR/handwriting: CER and WER per language/script, numeric-token accuracy, hallucination rate (inserted tokens absent from ground truth). Translation: chrF++, a learned metric where available in-region, human adequacy/fluency (1–5) on a sample, locked-term preservation rate (must be 100%). Extraction: field precision/recall. LID: accuracy per language and on code-mixed text.

**FR-P05-46 — Tiers and gating.** Per language and task: `A` reliable (review optional for non-filing use), `B` usable with review, `C` low-resource (review mandatory; type copies cannot reach `VERIFIED` by self-attestation alone). Tiers are published on a help page (NN-20: no unevidenced quality claims) and shown in the editor ("Quality for Santali handwriting: C — please check every line"). Any engine/model/prompt change runs the regression suite; a drop beyond `dix.eval.max_regression_pct` (default 2 points CER or 1.5 chrF++) blocks rollout (CI gate).

### 4P. Credits and pricing hooks

**FR-P05-47 — Metering.** Via `bil` meters (R6 credit seeds): handwriting/screenshot reading + type copy 3 credits per page; translation 2 credits per page; extraction 10 per agreement; print OCR for search 0 credits (deterministic); WhatsApp TXT parsing 0 credits, screenshot reading as handwriting rate. Credits are reserved at job start and settled on success; failed or cancelled jobs release them. `LD-ADD-DMSX` entitlement controls bulk/advanced jobs. Estimated credits are shown before a job starts; jobs above `dix.credits.confirm_above` (default 50) need confirmation.

### 4Q. Accessibility and mobile

**FR-P05-48 — Accessibility.** OCR text layers make scans readable by screen readers (NN-28); the editor is fully keyboard operable with confidence bands announced ("Line 14, low confidence"); colour is never the only indicator (icons and text badges); translations can be read aloud via the platform TTS in supported languages [REC]; type copies can be generated in large-print and high-contrast variants for personal use (not for filing).

**FR-P05-49 — Mobile.** Capture → "Make type copy" in ≤ 3 taps from the document; line-by-line confirm mode (FR-P05-18); results notify via push; heavy jobs run server-side only (no on-device model inference of confidential content).

*Help keys:* `hlp.dix.type_copy`, `hlp.dix.true_typed_copy`, `hlp.dix.confidence`, `hlp.dix.anchor`, `hlp.dix.chat_export`, `hlp.dix.counter_export`, `hlp.dix.machine_translation`, `hlp.dix.certified_translation`, `hlp.dix.back_translation`, `hlp.dix.quality_tier`, `hlp.dix.bsa63`, `hlp.dix.part_b_expert`, `hlp.dix.redaction_suggestion`, `hlp.dix.extraction`.

*Customisation hooks:* tenant routing restrictions (tighten only), default verification policy (self-attest allowed / independent required for filings), glossary additions (tenant terms, approved by `ORG_CLO`), show/hide line anchors in print, sender-masking default for chats, extraction auto-propose on upload on/off, credit confirmation threshold.

---

## 5. Workflows and state machines

### 5.1 DIX job (`dix.jobs.state`)

| State | Entry | Transitions | Guard | Events |
|---|---|---|---|---|
| `QUEUED` | Requested by user/agent or pipeline | → `RUNNING`, → `WAITING_ENGINE`, → `CANCELLED` | Credits reserved; class routing resolvable | `DixJobQueued` |
| `WAITING_ENGINE` | No allowed engine available | → `RUNNING` (engine back), → `FAILED` (timeout 24 h) | Fail-closed residency | — |
| `RUNNING` | Worker starts | → `NEEDS_INPUT` (locale ambiguity, sender mapping, `und` language), → `SUCCEEDED`, → `FAILED` | — | — |
| `NEEDS_INPUT` | User decision needed | → `RUNNING` | Answer recorded | `DixInputRequested` |
| `SUCCEEDED` | Renditions persisted | terminal | Aadhaar derived check passed | `DixJobSucceeded` (+ kind-specific events) |
| `FAILED` / `CANCELLED` | — | terminal | Credits released | `DixJobFailed` |

### 5.2 Type copy (`dix.renditions` where kind = `TYPE_COPY`)

`MACHINE_DRAFT → USER_CORRECTED → VERIFIED`; any → `SUPERSEDED` on regeneration; `USER_CORRECTED`/`VERIFIED` → `DISPUTED` (counterparty objection, reason mandatory) → `VERIFIED` (re-verified after resolution) or `SUPERSEDED`. Guards: `USER_CORRECTED` requires zero unreviewed `LOW` lines; `VERIFIED` per FR-P05-19; agents cannot perform any transition after `MACHINE_DRAFT` (NN-43).

### 5.3 Translation

`MT_DRAFT → (BACKTRANSLATION_FLAGGED → MT_DRAFT after edits) → REVIEWED`; `REVIEWED` cannot become `CERTIFIED` — certification produces a new rendition `TRANSLATION_CERTIFIED` through 5.4.

### 5.4 Certified translation request

`ORDERED → PAID → ASSIGNED → IN_PROGRESS → QA → CERTIFIED → DELIVERED`; side states `ON_HOLD` (clarification), `CANCELLED` (refund per marketplace terms, P16). SLA timers per step; breach notifies the buyer and `OPS_DELIVERY_LEAD`.

### 5.5 Extraction proposal

`PROPOSED → CONFIRMED | EDITED_AND_CONFIRMED | REJECTED`; only `CONFIRMED`/`EDITED_AND_CONFIRMED` values write metadata, reminder facts or `obl_` drafts.

---

## 6. Screens and UX

| ID | App | Purpose | Key components | Empty / error states | Mobile | Accessibility |
|---|---|---|---|---|---|---|
| SCR-P05-01 | web, mobile | Document intelligence panel (on P04 document page) | Status per rendition, actions: Type copy, Translate, Extract, s.63 certificate; credit estimate | Engine waiting banner | Bottom sheet | Status as text |
| SCR-P05-02 | web, mobile | Type copy request | Content type confirm, language confirm, verification choice | Language `und` → picker | Stepper | — |
| SCR-P05-03 | web | Side-by-side correction editor | Original pane, transcription pane, confidence highlights, disagreement hovers, progress, keyboard map | All lines high: "Quick review" | — (see -04) | Keyboard-first; screen-reader mode announces band |
| SCR-P05-04 | mobile | Line-by-line confirm | Crop + line, Yes/Edit/Can't read | — | Native | Large touch targets |
| SCR-P05-05 | web, mobile | Verification and attestation | Declaration, change list, hashes, sign (e-acceptance/eSign) | Blocked: low lines remaining | Native | Declaration readable at 400% |
| SCR-P05-06 | web | WhatsApp import | Upload ZIP/TXT, locale question, sender mapping, media report, missing-older-messages warning | Unsupported export → screenshot route | Simplified | Table semantics |
| SCR-P05-07 | web | Chat type copy view | Message table, filters (sender, date), translation column toggle, counter-export diff | — | List | — |
| SCR-P05-08 | web, mobile | Translation view | Two-column aligned, flags, labels, review action, order certified | — | Single column with toggle | `lang` attributes per segment for screen readers |
| SCR-P05-09 | web, mobile | Certified translation order | Pair, purpose, certification type, deadline, quote (GST shown), pay | No translator available → waitlist | Native | — |
| SCR-P05-10 | web | Extraction review | Field list with anchors (click → highlight in document), confirm/edit/reject, obligations proposal | No extractable fields | Details pane | — |
| SCR-P05-11 | web | s.63 certificate (Part A) | Pre-filled form, hash table, device section, request Part B | Flag off: "Coming soon — under legal review" | Native | — |
| SCR-P05-12 | console | Evaluation and engines | Engine registry, eval runs, tiers, regression diffs, kill switches | — | — | — |

**Click budgets:** request type copy ≤ 2 clicks from the document; import a WhatsApp export ≤ 4 (upload, locale if asked, map senders, confirm); translate to English ≤ 2; attach original + type copy + translation to a P10 annexure ≤ 3.

---

## 7. Backend design

### 7.1 Modules

`dix` (owner), `dms` (renditions read model, redaction tool), `ai` (`packages/ai` gateway, prompt registry, eval harness), `sgn` (`Bsa63CertificateService`, evidence ledger), `mkp` (certified translation, Part B, transcription services), `bil` (credits), `rul` (routing rules, gating), `pld`/`chp` (consumers of annexure pairs), `clm` (obligation proposals), `ntf`.

### 7.2 Tables (schema `dix`; `tenant_id`, `legal_entity_id`, RLS deny-by-default; text of `CONFIDENTIAL_LEGAL`/`RESTRICTED_PERSONAL` renditions stored as encrypted objects referenced by `*_ref`, not inline)

| Table | Key columns | Retention |
|---|---|---|
| `jobs` | `run_id` (prefix `dxj_` DIX job; `run_` is reserved for `ai.runs` — Appendix B §B.1; an AI-engine stage links its `ai.runs` id in `engine_ids`), `ver_id`, `kind`, `state`, `engine_ids`, `settings_hash`, `credits_reserved`, `credits_used` | 2 years |
| `renditions` | `drv_id`, `source_ver_id`, `kind` (`OCR_TEXT`, `OCR_PDF`, `TYPE_COPY`, `CHAT_TRANSCRIPT`, `TRANSLATION`, `TRANSLATION_CERTIFIED`, `REDACTED`, `MASKED`), `status`, `label_id`, `lang_from`, `lang_to`, `object_ref`, `sha256`, `supersedes_drv_id` | Follows source document |
| `lines` | `drv_id`, `page`, `line_no`, `bbox`, `text_ref`, `engine`, `model_version`, `confidence_band`, `alt_text_ref` | Follows rendition |
| `corrections` | `drv_id`, `line_id`, `old_ref`, `new_ref`, `by`, `at` | Follows rendition |
| `attestations` | `drv_id`, `kind` (`SELF`, `INDEPENDENT`, `ADVOCATE`), `by_prs_id`, `capacity`, `orig_sha256`, `text_sha256`, `sig_ref` | Follows rendition (evidence class when filed) |
| `disputes` | `drv_id`, `by_party`, `reason`, `state` | Follows rendition |
| `wa_chats` | `doc_id`, `variant`, `locale_resolution`, `tz`, `message_count`, `media_count`, `omitted_count` | Follows doc |
| `wa_messages` | `wa_chat_id`, `seq`, `ts_local`, `ts_utc`, `sender_raw_ref`, `sender_prs_id`, `type`, `text_ref`, `media_doc_id`, `edited`, `forwarded`, `raw_line_ref`, `lang`, `script`, `lid_conf` | Follows doc |
| `counter_diffs` | `chat_a`, `chat_b`, `report_ref` | Follows docs |
| `languages` (content) | `code`, `scripts`, `dir`, `ocr_route`, `mt_route`, `tier_by_task` | Permanent |
| `lid_results` | `ver_id`, `scope` (doc/page/block/msg), `lang`, `script`, `confidence` | Follows doc |
| `translation_segments` | `drv_id`, `seq`, `src_ref`, `tgt_ref`, `score`, `bt_cosine`, `bt_chrf`, `flag`, `reviewed_by` | Follows rendition |
| `glossary_terms` (content + tenant overlay) | `term`, `lang`, `target`, `dnt`, `source_ref`, `status`, `approver` | Permanent |
| `certified_requests` | `req_id`, `eng_id` (P16), `pair`, `purpose`, `cert_type`, `state`, `deliverable_drv_id` | 7 years |
| `extractions` | `ver_id`, `schema_version`, `field`, `value_ref`, `anchor`, `confidence`, `state`, `confirmed_by` | Follows doc |
| `redaction_suggestions` | `ver_id`, `category`, `bbox`, `state` | 1 year |
| `aadhaar_events` | `ver_id`/`drv_id`, `stage`, `count`, `pre_mask_sha256`, `action` | Permanent (no digits stored) |
| `engines` (platform) | `engine_id`, `version`, `langs`, `scripts`, `classes_allowed`, `residency`, `retention_terms_ref`, `cost`, `enabled` | Permanent |
| `eval_sets`, `eval_runs`, `quality_tiers` (platform) | set/datasheet refs, metrics, tier decisions with approver | Permanent |

### 7.3 APIs (`/v1/dix/…`)

| Method | Path | Scope | Idempotency |
|---|---|---|---|
| POST | `/jobs` (kind, `ver_id`, options) | `dix.job:write` | Key; also natural key (ver, kind, settings hash) |
| GET | `/jobs/{run_id}` | `dix.job:read` | — |
| POST | `/jobs/{run_id}/input` (locale answer, sender map, language) | write | Key |
| GET | `/renditions/{drv_id}` ; GET `/renditions/{drv_id}/lines?page=` | read (document permission) | — |
| POST | `/renditions/{drv_id}/corrections` (batch) | write | Key |
| POST | `/renditions/{drv_id}/attest` | `dix.attest:write` (human only) | Key |
| POST | `/renditions/{drv_id}/dispute` | party in shared matter | Key |
| POST | `/translations` ; POST `/translations/{drv_id}/review` | write / reviewer | Key |
| POST | `/certified-translations` (creates P16 order) | write + payment | Key |
| GET/POST | `/extractions?ver_id=` ; POST `/extractions/{id}/confirm` | read / write | Key |
| POST | `/bsa63/part-a` (via `sgn`) | write | Key |
| GET | `/annexure-pairs?doc_id=` (contract for P10/P15) | read | — |

Agent credentials can call `POST /jobs` and read results; `attest`, `review`, `confirm`, `certified-translations` reject agent principals (NN-13, NN-43).

### 7.4 Domain events (`in.lawdocs.dix.<EventName>.v1`; IDs, codes and hashes only — no text, NN-32)

`DixJobQueued`, `DixInputRequested`, `DixJobSucceeded`, `DixJobFailed`, `OcrCompleted`, `ChatExportParsed`, `LocaleAmbiguityResolved`, `TypeCopyGenerated`, `TypeCopyCorrected`, `TypeCopyVerified`, `TypeCopyDisputed`, `LanguageDetected`, `TranslationGenerated`, `TranslationReviewed`, `BacktranslationFlagged`, `CertifiedTranslationRequested`, `CertifiedTranslationDelivered`, `ExtractionProposed`, `ExtractionConfirmed`, `EligibilitySuspectFlagged`, `RedactionSuggested`, `AadhaarMaskedLate`, `EngineRegressionBlocked`, `QualityTierChanged`.

### 7.5 Jobs and workflows (Temporal)

`DixJobWorkflow` (per job, activities per stage, heartbeats for long PDFs, page-level parallelism with per-tenant concurrency caps); `WaChatImportWorkflow`; `TranslationWorkflow` (segment, lock terms, translate, back-translate, restore, QA); `CertifiedTranslationWorkflow` (with P16 engagement signals); `EvalRegressionWorkflow` (on engine/prompt change; CI and nightly); `AadhaarSweepJob` (weekly re-scan of derived text with the latest detector version; any hit = incident).

---

## 8. Integrations

| Port / adapter | Use | Vendors / alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `OCR_PORT` | Print OCR | PaddleOCR / Tesseract (self-hosted, Indic models) | Retry; vision fallback for low-confidence pages | Manual type copy (user types in the editor against the original) |
| `VISION_PORT` via `packages/ai` | Handwriting, screenshots | Claude via Bedrock India (D-14) [VERIFY model availability in India region at build — R4] | `WAITING_ENGINE`; never non-India | Manual transcription; marketplace transcriptionist |
| `TRANSLATE_PORT` | MT | Claude (Bedrock India); Bhashini [VERIFY terms, retention, coverage]; Google Cloud Translation / Azure Translator India regions for non-confidential classes [VERIFY zero-retention terms]; candidate self-hosted Indic MT model (ADR) | Fail-closed by class | Certified translator (P16) |
| `LID_PORT` | Language ID | Self-hosted LID; Indic LID adapter | Ask user | User picks language |
| `EMBED_PORT` | Back-translation similarity | In-region multilingual embedding | Skip similarity → all segments flagged for review | Human review |
| `MKP_PORT` (P16) | Certified translation, Part B experts, transcription | Marketplace providers | Waitlist | Off-platform provider, upload result |
| `SGN_EVIDENCE` (P08) | s.63 Part A generation, ledger | Internal | Flag off | Print blank Schedule form [VERIFY] |

Every adapter call carries an idempotency key and is reconciled (NN-46); vendor kill switches per adapter (NN-39).

---

## 9. Settings and configuration

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `dix.route.table_version` | PLATFORM | string | latest | `PLT_SUPER_ADMIN` + `PLT_SECURITY_OFFICER` | Y |
| `dix.route.tenant_restrictions` | TENANT | json (tighten only) | none | `ORG_CLO` | Y |
| `dix.route.regional_cloud.enabled` | PLATFORM | bool | false | `PLT_DPO` after transfer/terms review | Y |
| `dix.mt.regional_cloud.enabled` | PLATFORM | bool | false | `PLT_DPO` | Y |
| `dix.engine.<id>.enabled` | PLATFORM | bool | per registry | `PLT_SRE` (kill switch) | N (kill) / Y (enable) |
| `dix.confidence.high_min` / `medium_min` | PLATFORM | decimal | 0.95 / 0.80 | `PLT_SUPER_ADMIN` | Y |
| `dix.confidence.vision_cer_high_max` / `medium_max` | PLATFORM | decimal | 0.03 / 0.10 | `PLT_SUPER_ADMIN` | Y |
| `dix.typecopy.verification_policy` | TENANT | enum `SELF_ALLOWED` / `INDEPENDENT_FOR_FILINGS` | individuals SELF_ALLOWED; companies INDEPENDENT_FOR_FILINGS | `ORG_CLO` | Y |
| `dix.typecopy.show_anchors_in_print` | TENANT/USER | bool | true | user | N |
| `dix.chat.mask_nonparty_numbers` | TENANT | bool | true | `ORG_CLO` | Y |
| `dix.lid.min_confidence_set` / `ask_below` | PLATFORM | decimal | 0.90 / 0.60 | `PLT_SUPER_ADMIN` | Y |
| `dix.mt.backtranslation.required_for` | PLATFORM | list | filings, notices, settlements, consumer claims | `PLT_LEGAL_REVIEWER` | Y |
| `dix.mt.backtranslation.min_cosine` / `min_chrf` | PLATFORM | decimal | 0.85 / 50 | `PLT_SUPER_ADMIN` | Y |
| `dix.glossary.version` | PLATFORM | string | latest | `PLT_CONTENT_EDITOR` + `PLT_LEGAL_REVIEWER` | Y |
| `dix.glossary.tenant_overlay` | TENANT | json | none | `ORG_CLO` | N |
| `dix.bsa63.enabled` | PLATFORM | bool | false (NN-38) | `PLT_LEGAL_REVIEWER` after Schedule verification | Y |
| `dix.extract.auto_propose_on_upload` | TENANT | bool | true | `ORG_ADMIN` / `IND_OWNER` | N |
| `dix.redact.auto_card_numbers` | TENANT | bool | false | `ORG_ADMIN` | N |
| `dix.credits.confirm_above` | USER | int | 50 | user | N |
| `dix.eval.max_regression_pct` | PLATFORM | decimal | 2.0 | `PLT_SUPER_ADMIN` | Y |
| `dix.tier.<lang>.<task>` | PLATFORM | enum A/B/C | from eval | `PLT_SUPER_ADMIN` on eval evidence | Y |

---

## 10. Security, privacy and audit

| Risk | Control |
|---|---|
| Confidential content leaving India | Routing by class, fail-closed, engine registry residency field, contract terms recorded; Bedrock India for confidential classes; zero retention (NN-15, NN-25) |
| Training on customer data | Contractual no-training for every engine; evaluation sets synthetic/consented only (NN-15) |
| Aadhaar in derived outputs | Derived-text detector before persistence; weekly sweep; logs/traces scrubbed (NN-04, NN-32) |
| Prompt injection inside documents | Text and images passed as delimited data; system prompt forbids following embedded instructions; transcription prompts have no tools; outputs schema-validated |
| Fabrication by the model | Agreement checks, `MEDIUM` cap on numbers/names/dates, hallucination metric gate, human review before filing (NN-14) |
| Mislabelled authority | Fixed labels, lint on "certified"/"true typed copy", assembler always includes the original (NN-09, NN-48) |
| Tampered evidence | Hash at upload, re-hash at export, `HASH_MISMATCH_CRITICAL`, tamper hints shown only as signals |
| Third-party personal data in chats | Non-party number masking by default; purpose confirmation on external share (DPDP) |

Audit ledger entries: every correction batch, attestation, dispute, unmasking of chat numbers in a filing copy, certified-translation order, extraction confirmation and routing-setting change. Data classes for renditions follow the source document; translations of `RESTRICTED_PERSONAL` remain `RESTRICTED_PERSONAL`.

---

## 11. AI touchpoints and guardrails

| Feature | Model / agent | Autonomy ceiling | Human confirmation |
|---|---|---|---|
| Handwriting/screenshot transcription | Claude vision (Bedrock India) via `packages/ai`; `AGT_EVIDENCE_CLERK` may queue jobs and draft the annexure index and s.63 Part A | L2 (produce drafts) | Correction and attestation by a human before filing use |
| Translation | Claude / evaluated adapters | L2 (draft) | Review; certified route for filings (NN-48) |
| Classification / eligibility suspect | Classifier + Claude | L2; can tighten the P08 gate automatically, never loosen | Reclassification by a human with reason |
| Extraction (parties, dates, amounts, clauses, obligations) | Claude | L1 (propose) | Confirm per field (NN-14) |
| PII redaction suggestions | Patterns + model | L1 | User applies |

All AI renditions carry engine and model version, prompt version, date and label (NN-14). Prompts are versioned in the registry with evaluation results attached; a prompt change is a release-controlled change (P23). The Anthropic Usage Policy treatment of legal document preparation for individuals (human review and AI disclosure) is satisfied by the verification statuses and labels **[VERIFY current policy text — R4]**.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p05/*.feature`)

```gherkin
@P05-AT-01 @NN-09
Scenario: Type copy never replaces the original
  Given a handwritten agreement scan version v1
  When a type copy is generated and corrected
  Then v1 is unchanged and its SHA-256 matches the ingest hash
  And the type copy is a rendition linked to v1 with label "TYPE COPY"

@P05-AT-02 @NN-14
Scenario: Low-confidence lines must be reviewed before submission
  Given a type copy with 7 LOW lines
  When the user presses "Submit corrections" after reviewing 6
  Then submission is refused with the count of remaining lines

@P05-AT-03
Scenario: Numbers are capped at MEDIUM until confirmed
  Given a vision transcription line "Paid Rs 1,50,000 on 12/03/2024" with cross-decode CER 1%
  Then its band is MEDIUM, not HIGH, until a human confirms it

@P05-AT-04
Scenario: Ambiguous WhatsApp date format is asked, not guessed
  Given an Android export where no day value exceeds 12
  When it is imported
  Then the job enters NEEDS_INPUT with the example "Is 03/04/24 the 3rd of April or March 4th?"
  And no message timestamps are persisted until answered

@P05-AT-05
Scenario: Native export parses all locale fixtures without loss
  When the 12 golden WhatsApp fixtures are parsed
  Then message counts equal the fixture ground truth
  And media references link to ZIP entries with their own hashes
  And omitted-media counts are reported

@P05-AT-06 @NN-04
Scenario: Aadhaar in handwriting is masked in every derived output
  Given a handwritten letter containing a Verhoeff-valid Aadhaar number in Devanagari digits
  When OCR, type copy, translation and extraction run
  Then every derived text shows only the last 4 digits
  And the original is replaced by a masked version with the unmasked version purged and pre_mask_sha256 recorded
  And no log, trace or search entry contains the first 8 digits

@P05-AT-07 @NN-15 @NN-25
Scenario: Confidential document never routes outside India
  Given a CONFIDENTIAL_LEGAL document and the Bedrock India endpoint unavailable
  When translation is requested
  Then the job waits in WAITING_ENGINE
  And no request is sent to any engine whose residency is not India

@P05-AT-08 @NN-48
Scenario: Machine translation cannot enter a filing that needs certification
  Given a P10 bundle for a forum profile with translation_certification_required
  When the user attaches a REVIEWED machine translation
  Then it is blocked with LD-DIX-030 and an offer to order a certified translation

@P05-AT-09
Scenario: Locked legal terms survive translation
  Given Hindi text citing "धारा 138" of the Negotiable Instruments Act and an amount "₹2,50,000"
  When translated to English
  Then "Section 138" and "₹2,50,000" appear exactly once each
  And a missing placeholder would flag the segment LD-DIX-021

@P05-AT-10
Scenario: Back-translation flags meaning drift
  Given a settlement clause whose back-translation cosine is 0.78
  Then the segment is flagged "Meaning may have changed — review"
  And the translation cannot be attached to the settlement until reviewed

@P05-AT-11
Scenario: TRUE TYPED COPY needs an advocate's attestation
  Given a type copy verified by the uploader only
  When the user tries to render the label "TRUE TYPED COPY"
  Then the renderer uses "TYPE COPY" and lint LBL-TC-01 records the attempt

@P05-AT-12 @NN-10
Scenario: s.63 Part A draft for a chat export
  Given dix.bsa63.enabled = true and an imported WhatsApp export
  When the user opens "Prepare s.63 certificate"
  Then Part A is pre-filled with the record description and the SHA-256 table computed at upload
  And Part B can be requested from an expert who receives hashes only

@P05-AT-13
Scenario: No s.63 offer for a scan of a paper document
  Given a scanned handwritten paper letter
  Then the s.63 certificate action is not offered
  And help text explains that the paper original must be produced

@P05-AT-14 @NN-43 @NN-13
Scenario: Agent cannot verify or attach
  Given AGT_EVIDENCE_CLERK produced a type copy
  When the agent calls attest or adds it to a P10 annexure
  Then both calls are rejected for agent principals

@P05-AT-15 @NN-07
Scenario: Classification tightens the eligibility gate
  Given an uploaded document classified by the user as "Agreement" but detected as a power of attorney
  Then it is tagged eligibility_suspect
  And P08 refuses eSign with LD-SGN-014 until a human reclassifies with a reason

@P05-AT-16
Scenario: Extraction writes nothing until confirmed
  Given extracted fields for a lease
  When the user has not confirmed them
  Then document metadata, reminder facts and obligations are unchanged

@P05-AT-17
Scenario: Annexure pairs carry status
  Given an original with an unverified type copy and a machine translation
  When the user attaches all three to a petition after confirming the warnings
  Then the index shows P-3, P-3(T) "not verified" and P-3(Tr) "machine translation, not certified"

@P05-AT-18
Scenario: Engine regression blocks rollout
  Given a new handwriting prompt raising Hindi CER by 3 points on the eval set
  Then EngineRegressionBlocked is emitted and traffic stays on the previous version

@P05-AT-19 @NN-28
Scenario: Editor is operable by keyboard and screen reader
  When the manual NVDA and VoiceOver scripts run on SCR-P05-03 and SCR-P05-04
  Then every line can be reviewed, corrected and confirmed without a mouse
  And confidence bands are announced

@P05-AT-20 @NN-46
Scenario: Engine calls are idempotent and reconciled
  Given a translation job retried after a worker crash
  Then the adapter receives the same idempotency key
  And credits are charged once
```

---

## 13. Exit gate, deliverables and open items

**Checklist**

- [ ] Router, engine registry and kill switches; residency fail-closed tests green.
- [ ] Print OCR upgrade, vision reading, screenshot understanding, WhatsApp parser with 12 fixtures.
- [ ] Type copy generator with anchors and labels; editor (web + mobile); verification and disputes.
- [ ] LID for 28 languages and code-mixed classes; MT with glossary locks and back-translation; certified-translation flow wired to P16 (stub allowed until P16 ships).
- [ ] Derived-text Aadhaar masking and late-detection purge; weekly sweep job.
- [ ] Extraction and classification with eligibility-suspect tightening; obligation proposals to P07.
- [ ] Evaluation sets with datasheets; tiers published; regression gate in CI.
- [ ] Annexure-pair contract consumed by P10 and P15 (contract tests).
- [ ] `dix.bsa63.enabled` remains OFF until the Schedule field labels are verified and signed off.
- [ ] Settings (Appendix R), help keys (`hlp.dix.*`), labels (`lbl.*`), errors registered.

**Demo script (10 minutes).** Upload a Hindi handwritten loan acknowledgement; low-confidence lines highlighted; correct two lines on the phone; self-attest; translate to English with locked "₹" amounts; attach original + type copy + translation to a P10 recovery suit annexure; import a WhatsApp export with an ambiguous date; map senders; generate the chat type copy; prepare s.63 Part A (flag on in staging); show the eval dashboard with Santali tier C.

**Export-map entries (`xpt.export_map`)**

| Record type | `LD-EXPORT-1.0` location |
|---|---|
| `dix.rendition` (type copy, chat transcript, translation, certified translation, OCR PDF) | Beside the original: `<name> (Type copy – <status>).pdf/.docx`, `<name> (Translation – English – Machine).docx`, `<name> (Certified translation – English).pdf` |
| `dix.lines`, `dix.corrections`, `dix.attestations` | `99 System Data (CSV and JSON)/document_intelligence/` (CSV; text included for the exporting owner) |
| `dix.wa_chats`, `dix.wa_messages` | Chat folder beside the original ZIP: `<chat> (Messages).xlsx` + `messages.json` |
| `dix.translation_segments`, `dix.glossary_terms` (tenant overlay) | `99 System Data/document_intelligence/translations/` |
| `dix.extractions` (confirmed) | Manifest columns + `99 System Data/document_intelligence/extractions.csv` |
| `dix.certified_requests` | `09 Services and Engagements/` (company) or `10 Receipts and Invoices/` (individual) with the certificate PDF beside the source |

**Errors (`LD-DIX-001…040`)**

| Code | Meaning |
|---|---|
| 001 | Unsupported content for intelligence (e.g., encrypted) |
| 002 | Insufficient credits — job not started |
| 003 | No permitted engine available for this data class — queued |
| 004 | Page image too low resolution — re-scan advised |
| 010 | WhatsApp date format ambiguous — answer needed |
| 011 | Not a recognised WhatsApp export |
| 012 | Sender mapping incomplete |
| 015 | Low-confidence lines not reviewed |
| 016 | Verification not permitted for this role or agent |
| 017 | Type copy disputed — resolve before filing |
| 020 | Language undetermined — choose a language |
| 021 | Locked term lost in translation — segment needs editing |
| 022 | Back-translation flags unreviewed |
| 025 | s.63 certificate not available for paper-document scans |
| 026 | s.63 feature not yet enabled (legal verification pending) |
| 030 | Certified translation required by the forum |
| 031 | No certified translator available for this pair — waitlisted |
| 035 | Engine regression gate failed (console) |

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P05-01 | Verify BSA Schedule field labels and *Pune Bar Assn.* citation; enable `dix.bsa63.enabled` | `PLT_LEGAL_REVIEWER` / [COUNSEL] |
| OI-P05-02 | Bhashini terms of use, retention, residency and coverage; Google/Azure India-region zero-retention terms | `PLT_DPO` |
| OI-P05-03 | Per-forum translation certification rules (SC, HCs of launch States, consumer commissions) for P10 render profiles | [COUNSEL] / P10 |
| OI-P05-04 | Court-filing practice on masking non-party phone numbers in chat type copies | [COUNSEL] |
| OI-P05-05 | Bedrock India availability of the vision-capable Claude model chosen; latency and page cost baseline | P09 / P00 |
| OI-P05-06 | Licensing of Legislative Department glossaries and authoritative Hindi texts for glossary seeding | `PLT_CONTENT_EDITOR` |
| OI-P05-07 | Current WhatsApp export limits and advanced chat privacy behaviour | QA (device test) |
| OI-P05-08 | Baseline CER/chrF++ targets per language after the first evaluation run (confirm or revise §1 targets) | Evaluation lead |
| OI-P05-09 | Qualifying criteria for Part B "expert" beyond s.79A examiners | [COUNSEL] |
