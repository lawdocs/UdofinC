# Appendix L — Document Management, Court-Format Templates, Type Copies and Translation

> **Binding** for P02 (DMS core, sharing, ingest, type copies, LID), P06 (court-format engine, eSign/eStamp hooks, certified translation, s.63 certificates, court exports) and P11 (OCR router, machine translation, AI guardrails). Consumed by P04 (neutral workspace, orders, bundles at hearings), P12 (mobile capture and viewer) and Appendices M (AI Pleadings Studio) and R (case-status portal, publication, execution). Read with master NN-08, NN-10, NN-22, NN-26, NN-30, NN-32; Appendices D (ports), F (data model), S §6 (RBAC/ABAC). Requirements map: R-21, R-22, R-23, R-24 (02 §2); decisions D2-08, D2-09. Research base: S7 §3, S8 §1 and §7.1. Version 2.0, 21 October 2026.

---

## L.0 Scope, precedence and decisions taken in this appendix

**What this appendix specifies.** (1) The case document repository, its folders, versions, metadata, search, preview, annotation, redaction, watermarking, download controls, legal hold and retention; (2) who sees what, and how a party chooses what to share; (3) the filing → scrutiny → transmission → order → service flow and e-bundles; (4) eSign/eStamp hooks for documents; (5) court-format rendering (Supreme Court A4 circular of 12 March 2020 and other forum profiles) and the document anatomy of a court filing (never labelled "court-ready" under an unverified profile, X-34); (6) type copies of handwritten material, screenshots and WhatsApp chats; (7) language identification and translation for 28 languages; (8) security, evidence ledger and the Bharatiya Sakshya Adhiniyam 2023 (BSA) s.63 certificate; (9) data model, APIs, events, errors and flags; (10) acceptance tests; phase addenda.

**Precedence.** Master → Appendix G (legal rules) → Appendix F (names, types, events, errors) → this appendix → phase files (master §15). Where this appendix adds columns to an Appendix F table, they are additive. Where it adds tables, P02/P06/P11 migrations create them and Appendix F is updated in the same PR.

**v3.0 and v3.1.** Configuration tiers follow NN-33 and Appendix V (§9.5); export packages follow Appendix AC §AC.13 (`EQ-EXPORT-1.0`, which maps the §1.2 folders to case export folders); menu placement of the screens named here follows Appendix AG; v3.1 additions (24 October 2026) are marked *(v3.1)*.

| ID | Decision | Reason | Effect |
|---|---|---|---|
| L-D-01 | **One repository per case**, with fixed system folders (§1.2) plus a per-party **private drafts space** that is not part of the case record until filed. | R-21 ("party chooses what to share"); A&C Act 1996 s.24(3) communication duty applies only to material supplied to the tribunal. | Drafts never reach neutrals or the other side by default. |
| L-D-02 | Visibility is modelled as a **lifecycle state + audience set** (§2), replacing the single `confidentiality` enum of FR-P02-36. The P02 values map 1:1 (§2.3 table). Privilege stays on `core.documents.privilege` with **Appendix F's value set** (`none`, `without_prejudice`, `privileged`, `caucus_derived`) — the five-value P02 list is superseded; `legal_advice` and `litigation` map to `privileged`, `settlement_communication` maps to `without_prejudice`. | Appendix F prevails on names and value sets (master §15). | P02 migration aligned; conflict closed. |
| L-D-03 | **Mechanism-aware sharing rules.** In arbitration, anything a party files to the tribunal is served on every other party (A&C s.24(3)); in mediation and conciliation a party may share a document with the neutral only (caucus share), and the neutral may not pass it on (A&C s.70 proviso for conciliation; Equator Mediation Rules and Mediation Act 2023 s.22 as policy mirror until notified, NN-05). | Statute; NN-11. | `NEUTRAL_ONLY` audience is refused for arbitration filings (`DOC_SERVICE_REQUIRED_ARBITRATION`). |
| L-D-04 | **DOCX is the canonical rendering** of every generated legal document; PDF/A-2b is produced from the same DOCX by a pinned LibreOffice build, then post-processed (bookmarks, pagination stamps, signatures) and validated by veraPDF. | Single source avoids DOCX/PDF drift; users need editable DOCX; courts need PDF/A. | §5.7 pipeline. |
| L-D-05 | **Court profiles are data** (`core.render_profiles`), versioned and maker–checker approved. Among court profiles only `SC_2020_PRINT`, `HC_TS_EFILING_2020` and `HC_RJ_EFILING` are seeded `verified` (Equator's own non-court profiles `EQR_TRIBUNAL` and `FOREIGN_SEAT` are `verified` as Equator policy); every other court profile is seeded `unverified` and its exports carry "Check the forum's current filing rules" until a `legal_reviewer` verifies it. | S8 §1.1–1.2 verified only these sources; SC e-filing digital parameters were not retrievable (S8 §1.2). | No "SC e-filing ready" or "NCLT-ready" claim (NN-17). |
| L-D-06 | **Residency-consistent OCR/MT routing.** Case content (data class D2) and special data (D3) are processed only by `bedrock_india`, `sarvam`, `self_hosted` (S7 §3.9) **plus** AWS Textract in ap-south-1. Google Document AI (asia-south1) and Azure Read (Central India) are usable for D2 only when the tenant flag `ocr.regional_cloud.enabled` is ON after an ADR records the regional endpoint, DPA and no-training term; never for D3. | Resolves the conflict between S7 §3.2 routing (Google/Azure for handwriting) and S7 §3.9 data-class policy and Appendix D.5.4 ("Google non-personal only"). | Handwritten Indic default route = Sarvam Vision + Claude vision (Bedrock India) with mandatory human verification (§6.4). |
| L-D-07 | **Language scope = 28 distinct languages**: the 22 Eighth Schedule languages + the 6 UN official languages (English is a UN language and is not in the Eighth Schedule). Code-mixed romanised classes (`hi-Latn`, `ta-Latn`, `bn-Latn`, `mr-Latn`, `kok-Latn`) are detected as separate LID classes. | D2-09; S7 §3.3 counts "29 entries" with English counted twice. | `core.languages` seeds 28 rows + 5 code-mixed classes. |
| L-D-08 | Machine output is never labelled "certified". Labels are fixed strings (§6.7, §7.6) and cannot be edited by tenants. | NN-32; S7 §3.5. | Lint `LBL-01…LBL-06`. |
| L-D-09 | **Type copies of handwriting are never auto-accepted**, whatever the engine confidence. | S7 FR-S7-OCR-03; NN-32. | `type_copy.status = verified` requires a human attestation. |
| L-D-10 | Exhibit labels inside Equator proceedings stay as FR-P02-37 (`C-`, `R-`, `CC-`, `T-`, `J-`). Court exports **re-label by the filer's role in court** (`P-` for petitioner/applicant, `R-` for respondent, or the profile's series) and keep the arbitral label in the index "Remarks" column. | A s.34 petitioner may have been the arbitral respondent; S8 §1.1 annexure practice. | `core.annexure_maps` (§9). |
| L-D-11 | Public visibility of any document exists **only** through the Appendix R publication workflow (NN-26). The DMS has no "make public" action. | NN-26; A&C s.42A. | `PUBLIC` audience is set by the publication service on a redacted rendition only. |
| L-D-12 | eSign never substitutes for an oath. Affidavits are e-signed only as a draft-approval step; the sworn copy (Oaths Act 1969; Notaries Act 1952; CPC O.XIX) is uploaded and hashed. | NN-25; S7 §3.6 item 10. | `AFFIDAVIT_REQUIRES_OATH`. |
| L-D-13 | Screen IDs: this appendix reserves `SCR-P02-60…79`, `SCR-P06-40…59`, `SCR-P11-40…49` to avoid collision with Appendices K, M, N, R, S. Appendix C is updated in the same PR. | Appendix C rule 1. | — |

---

## 1. DMS architecture

### 1.1 Storage topology

| Layer | Technology | Content | Controls |
|---|---|---|---|
| Quarantine | S3 `eq-{env}-quarantine-aps1` (no Object Lock, lifecycle 7 days) | Raw uploads before scan | No read path for users; scanner role only |
| Evidence (originals) | S3 `eq-{env}-evidence-aps1`, **Object Lock compliance mode**, versioning ON, SSE-KMS with per-tenant CMK | Original bytes of every upload and every signed/issued document | Retention per `retention_class`; legal hold via `PutObjectLegalHold`; CRR to ap-south-2 |
| Derived | S3 `eq-{env}-derived-aps1`, versioning ON, SSE-KMS per tenant | Renditions: PDF conversions, OCR text/JSON, thumbnails, type copies, translations, redacted copies, bundles before certification | Re-creatable from originals; never Object Lock except certified bundles (copied to evidence bucket) |
| Sealed | S3 `eq-{env}-sealed-{posh,health,safety}-aps1` | POSH, health, family-safety documents | Separate KMS keys and IAM roles (`eq_posh`, `eq_health`, `eq_safety`); never indexed; never sent to OCR/MT outside `bedrock_india`/`self_hosted` (NN-07) |
| Metadata | Aurora PostgreSQL `core.*` | Document, version, rendition, share, link, annotation, hold, ledger rows | RLS (tenant + case + tier), Appendix F |
| Search | OpenSearch, index alias `docs-{tenant_id}` | Extracted text, metadata, ACL keys | Sealed and `private_draft` content never indexed (§1.7) |

### 1.2 Repository and folder tree

Each case has exactly one repository (`core.document_folders` rows created on `equator.cases.case.filed.v1`). Folders are **system folders** (codes fixed; labels i18n) with optional user sub-folders (max depth 3 below a system folder; names ≤ 80 chars; no `/ \ : * ? " < > |`).

| Code | Label (en) | Label (hi) | Who may file into it | Default audience on filing | `core.documents.kind` (F.3) | Typical `doc_kind` (FR-P02-36) | Retention class |
|---|---|---|---|---|---|---|---|
| `PLD` | Pleadings | अभिवचन | parties, representatives (scope `file_documents`) | All parties + neutrals + registry | `pleading` | `pleading_claim`, `pleading_response`, `counterclaim` | `case_record` |
| `ANX` | Annexures and exhibits | अनुलग्नक एवं प्रदर्श | parties, representatives | Follows the parent pleading | `evidence` | any evidentiary kind; exhibit label mandatory | `case_record` |
| `EVD` | Evidence (witness statements, expert reports, recordings) | साक्ष्य | parties, neutral (tribunal experts), registry | Per filing choice (§2) | `evidence` | `witness_statement`, `expert_report`, `audio`, `video` | `case_record` |
| `NTC` | Notices and service | सूचनाएँ एवं तामील | system (notices engine), registry | Addressee + registry; neutrals after appointment | `notice` | `notice`, `service_certificate` | `case_record` |
| `ORD` | Orders and directions | आदेश एवं निर्देश | neutrals, registrar (institutional orders) | All parties + registry | `order` | `order` | `case_record` |
| `OUT` | Awards and settlements | पंचाट एवं समझौते | neutrals, system (outcome builder P06) | Parties to the instrument + registry | `award` / `settlement` | — | `outcome_instrument` (13 years from the instrument date or 1 year after execution completes, whichever is later — X-36; Appendix Q Q-R4; longer where the tenant's records policy says so) |
| `COR` | Correspondence | पत्राचार | parties, registry, neutrals | Sender's choice; registry always | `correspondence` | `correspondence` | `case_record` |
| `INT` | Internal (registry only) | आंतरिक | case_manager, registrar, quality_officer, case_counsel | Registry roles only; never parties or neutrals | `report` / `minutes` | scrutiny notes, conflict checks, file notes | `case_record` |
| `BND` | Bundles | बंडल | system (`BundleBuildWorkflow`) | Bundle audience (§3.6) | `bundle` | — | `case_record` |
| `DRF` (per party) | My drafts (private) | मेरे मसौदे | the party side only (party, `party_org_user`, representatives with `file_documents` scope) | `PRIVATE_DRAFT` (§2.1) | as chosen | as chosen | `case_record` once filed; drafts deleted 90 days after case closure unless filed |
| `CAU` (per neutral) | Caucus notes | कॉकस नोट्स | author neutral only | Author only (NN-11, `core.caucus_notes`) | — | — | `caucus_note` (12 months after closure) |

Rules: (a) a document lives in exactly one folder; "copies" across cases are references (`core.document_links`), never byte copies; (b) moving between system folders is a metadata change by `case_manager` with audit, never changes audience retroactively; (c) `INT` and `CAU` never appear in any party or neutral export, bundle or search result; (d) FAM, POSH-linked and INS health cases have `EVD` items defaulting to `confidentiality_tier = high` (health → `sealed` store).

### 1.3 Document object model

```
Document (logical; core.documents)
 ├─ Version 1..n (core.document_versions; original bytes, immutable, WORM, hashed, ledgered)
 │    └─ Renditions (core.document_renditions; derived, each hashed, each links derived_from_version_id)
 │         kind ∈ { pdf_conversion, thumbnail, ocr_text, ocr_layout_json, searchable_pdf,
 │                  type_copy, translation_machine, translation_reviewed, translation_certified, redacted,
 │                  court_export, watermarked_download, transcript }
 └─ Annotations, shares, links, tags, holds (separate tables; never inside the file)
```

- A **version** is an original: a fresh upload, a signed PDF returned by the ESP, a sealed award, an issued order. Versions are never edited.
- A **rendition** is derived and carries `derivation` metadata: engine/provider, model ID and version date, parameters, confidence summary, human verifier, label (NN-32). Type copies and translations are renditions **with their own lifecycle** (§6, §7) and may be promoted to a separate filed document (an annexure) while keeping `derived_from_version_id`.
- **Supersession.** A new version moves `current_version_id`; old versions stay visible in History to roles allowed by §2. A version included in a **served** bundle can be superseded only with neutral leave (P04) or, before appointment, `case_manager` approval (FR-P02-38); the bundle keeps the old version.

### 1.4 Metadata

| Field | Type | Required | Source | Validation / notes |
|---|---|---|---|---|
| `title` | text ≤ 200 | Y | uploader (pre-filled from filename / Doc AI) | No PII in title for `high`/`sealed` tiers (lint warns on phone/PAN/Aadhaar patterns) |
| `folder_code` | enum §1.2 | Y | uploader | Allowed per role |
| `kind` | enum F.3 `document_kind` | Y | derived from folder + `doc_kind` | — |
| `doc_kind` | enum FR-P02-36 (configurable) | Y | `document_extractor` proposes; user confirms | Proposal stored in `ai_classification` with confidence |
| `document_date` | date | N | user / extracted | Not in the future; "approximate" flag allowed |
| `author_text` | text ≤ 120 | N | user / extracted | — |
| `parties_referenced` | uuid[] (`core.case_parties`) | N | user / NER proposal | — |
| `language_codes` | text[] BCP-47 | auto | LID (§7.2) | Per page values in `page_languages jsonb` |
| `scripts` | text[] ISO 15924 | auto | LID | e.g., `Deva`, `Olck`, `Mtei`, `Arab` |
| `page_count` | int | auto | renderer | — |
| `confidentiality_tier` | `standard`/`high`/`sealed` | Y | case tier default; may only be raised by a party, lowered only by `registrar` | — |
| `privilege` | F set (`none`, `without_prejudice`, `privileged`, `caucus_derived`) | Y (default `none`) | uploader | `privileged` documents cannot be served (§2) |
| `visibility_state` | §2.1 | Y | system | — |
| `exhibit_label` | text | when in `ANX`/`EVD` and filed | numbering engine FR-P02-37 | Unique per case and series |
| `source_capture` | jsonb | Y for `evidence` | uploader | S7 §4.3: `source_device`, `source_app`, `original_owner`, `capture_method` ∈ {`export`,`screenshot`,`download`,`scan`,`photo`}, `language_hint`, `date_range` |
| `evidence_upload_type` | enum | Y for `evidence` | uploader | `whatsapp_export_zip`, `whatsapp_export_txt`, `screenshot`, `email_eml`, `email_pdf`, `pdf_document`, `scanned_handwritten`, `photo`, `audio_recording`, `video_recording`, `bank_statement`, `credit_report_self`, `call_recording`, `other` (S7 §4.3) |
| `tamper_hint` | jsonb | auto | Doc AI | Flags only: "Possible inconsistency detected: the neutral will decide." Never a finding (S7 FR-S7-DOC-12) |
| `ai_disclosure` | jsonb | auto when AI-assisted | App. M | `{prepared_with_ai, model_registry_ref, facts_verified_by, citations_verified_on}` — renders the AI-disclosure stamp (SC draft AI Regulations 2026 Reg 43(3) readiness; S7 §3.6) |
| `tags` | text[] | N | §1.5 | — |
| `retention_class`, `retain_until`, `legal_hold` | F.1.3 | Y | retention service | §1.14–1.15 |

### 1.5 Tags

- **System tags** (set by services, read-only to users): `filed`, `served`, `on_record`, `superseded`, `withdrawn`, `type_copy_available`, `translation_available`, `certified_translation`, `ocr_low_confidence`, `handwritten`, `whatsapp`, `screenshot`, `ai_assisted`, `signed`, `stamped`, `s63_part_a`, `s63_part_b`, `privileged`, `legal_hold`, `redacted_rendition`, `court_export`.
- **Case tags** (shared within a side or within the registry): free text ≤ 40 chars, lower-case slug, max 20 per document; a party side's tags are visible only to that side; registry tags only to registry roles; neutrals' tags only to the tribunal/neutral team. Tag vocabularies per tenant may be pre-seeded (e.g., FIN: `kfs`, `soa`, `noc`, `recovery_call`).
- Tags never carry sealed content; a tag lint blocks health diagnoses, caste, religion and POSH terms (`TAG_SENSITIVE_TERM`).

### 1.6 Search

- **Index**: OpenSearch alias `docs-{tenant_id}`; one index document per **version page** (`doc_id`, `version_id`, `page_no`, `text`, `text_{lang}` multi-fields) and one per document (metadata). Text sources: native PDF text, OCR text layer, verified or draft type copy (flagged), machine translations (flagged `derived=true`), email headers/bodies.
- **Analysers**: `icu_tokenizer` + `icu_folding` for all; language analysers for `en`, `hi` (with `indic_normalization`), `bn`, `mr`, `ta`, `te`, `kn`, `ml`, `gu`, `pa`, `or`, `ur`, `ar`, `ru`, `fr`, `es`, `zh` (smartcn); others fall back to ICU. Romanised code-mixed text is indexed both raw and transliterated (§7.2).
- **Access filter (document-level security)**: each index document carries `acl_keys[]` (e.g., `side:{party_id}`, `neutral:{proceeding_id}`, `registry:{case_id}`, `internal:{case_id}`) computed from §2; every query adds a terms filter on the caller's keys computed by the policy engine. The query service — never the client — builds the filter. A nightly job (`AclDriftJob`) re-computes keys from Postgres and fails the run on any mismatch.
- **Never indexed**: `sealed` tier, `PRIVATE_DRAFT` documents (search within drafts runs in Postgres full-text on the owner's rows only), `CAU`, privileged documents for non-owner sides.
- **Query features**: phrase, prefix, fuzzy (edit distance 1 for ≥ 5 chars), Boolean, field filters (`kind:`, `exhibit:`, `date:`), hit highlighting with page jump; search inside the open document (Ctrl/Cmd+F) over the text layer; "search across my cases" for professionals limited to cases where they hold an active grant.
- **Performance**: p95 < 800 ms for 1 million pages per tenant; index lag after OCR < 60 s.

### 1.7 Filters and saved views

| Filter | Values |
|---|---|
| Folder | §1.2 codes |
| Filed by | party side, neutral, registry, system |
| Visibility state | §2.1 |
| Audience includes | my side / other parties / neutral / registry |
| Kind / doc_kind | F.3 / FR-P02-36 lists |
| Date range | document date; upload date |
| Exhibit series | `C`, `R`, `CC`, `T`, `J` |
| Language | `core.languages` |
| Derived texts | has type copy / has translation / certified / low OCR confidence |
| Signature | unsigned / signature pending / signed / stamped |
| Tags | system + case tags |
| In bundle | bundle ID / version |
| Legal hold | yes / no (staff only) |

**Saved views** (`core.saved_views`): personal views for all roles; team views for staff (shared within the tenant's case-manager team); default views seeded per persona — Party: "Served on me", "My filings", "Needs my signature"; Neutral: "On record", "New since last hearing", "Bundles"; Case manager: "Awaiting scrutiny", "Untranslated vernacular", "Type copies awaiting verification", "s.63 Part A unsigned". A view stores filters, sort and columns only — never results.

### 1.8 Bulk actions

| Action | Who | Limit | Guard |
|---|---|---|---|
| Download as ZIP | per §1.13 | 500 files / 2 GB | Manifest with SHA-256 per file included; watermark rules apply per file; folder and file names follow the `EQ-EXPORT-1.0` case taxonomy and naming rules (Appendix AC §AC.13.5, §AC.13.7: ASCII names, path below root ≤ 140 characters) so the ZIP opens cleanly in Windows, SharePoint and OneDrive (NN-37) *(v3.1)* |
| Add / remove case tags | own side / registry | 500 | — |
| Move to folder | case_manager | 500 | Audience unchanged |
| Request type copy / translation | party (own documents), case_manager | 100 | Fee quote first where chargeable (App. O) |
| Add to bundle draft | party (own), case_manager, neutral | 1,000 | Only `on_record` documents for joint/tribunal bundles |
| Share with … (§2.4) | owning side | 100 | Mechanism rules (L-D-03) |
| Apply legal hold | registrar, dpo | case-wide | Reason code mandatory |
| Re-run OCR | case_manager | 100 | Cost metered |

Bulk operations run as a Temporal workflow with per-item results and an undo window of 10 minutes for tag/move operations only.

**Bulk upload and auto-filing *(v3.1)*.** A party side or case manager may drop up to 200 files (or one ZIP within §8.1 limits) at once. Each file passes §8.1 security, then appears in a **classification grid** (one row per file: proposed `doc_kind` with confidence, document date, folder, proposed exhibit label, language, "type copy needed" and "translation needed" flags). The user edits cells inline, selects rows and uses "Apply to selected" for folder, kind or tags, and confirms; nothing is filed until the user presses "File selected" and completes one share dialog (§2.4) for the batch. Duplicate checks: an exact SHA-256 match with a document already in the case is blocked ("Already filed as C-4"); a near-duplicate (text similarity ≥ 0.95 or perceptual image hash distance ≤ 4) is flagged for the user to keep or drop. Each row is idempotent on (case, side, SHA-256); on partial failure the grid shows per-row status, failed rows stay in `DRF` with the reason, and "Retry failed" re-runs only those rows. Every batch writes one audit event per document and one batch summary event (`equator.documents.batch.filed.v1`).

### 1.9 Preview

- PDF and images: PDF.js-based viewer with text layer, thumbnails, rotate, zoom, page jump, search; HEIC converted to JPEG at ingest; TIFF multi-page supported.
- Office (DOCX, XLSX, PPTX): converted to PDF in an isolated converter (LibreOffice headless in a gVisor/Firecracker sandbox, no network, 60 s timeout, 1 GB RAM cap); spreadsheets also offered in a read-only grid (first 10,000 rows).
- Email (EML/MSG): header panel (From, To, Cc, Date, Subject, Message-ID), body (HTML sanitised with DOMPurify; remote images blocked), attachments listed as child documents with their own hashes.
- Audio/video: HLS stream with captions when a transcript rendition exists; mediation recordings do not exist by default (NN-11).
- **View-only mode**: where §1.13 denies download, the viewer streams rendered page images (PNG tiles, 150 dpi) with a per-viewer watermark; the text layer is disabled; print is disabled.

### 1.10 Annotation

- Stored as W3C Web Annotation JSON in `core.document_annotations` (target = version ID + page + selector [TextQuote, TextPosition, or FragmentSelector `xywh=`]); never written into the file.
- Types: highlight, note, bookmark, link-to-exhibit, issue tag (neutral issues list).
- Audiences: `private` (author only, default), `my_side`, `tribunal` (neutral team), `registry`. A party annotation can never be visible to a neutral or another side unless the party exports it as a new document and files it.
- Neutral annotations are part of the neutral's working papers: excluded from every export and from DSR exports to parties (A&C s.42A confidentiality; deliberation secrecy); retained per `caucus_note` class for mediators and `case_record` for arbitrators.
- Court exports and bundles **never include annotations** (Telangana e-Filing Rules 2020 r.8.7: no markings or annotations).

### 1.11 Redaction tool

- Operates on a version and produces a **`redacted` rendition**; the original is untouched (NN-32).
- Inputs: manual boxes and text selections; pattern suggestions (PAN `[A-Z]{5}[0-9]{4}[A-Z]`, Aadhaar 12-digit with Verhoeff check, Indian mobile `[6-9][0-9]{9}`, email, IFSC, account and loan numbers, vehicle registration, dates of birth); NER suggestions (names, addresses) from `document_extractor`; profile suggestions by vertical (App. R §3 profiles R1–R6).
- Each redaction carries a **reason code**: `R-PII` personal identifier, `R-AADHAAR` (mandatory masking, NN-14), `R-MINOR` (BNS 2023 s.72 / POCSO 2012 s.23 / JJ Act 2015 s.74 contexts), `R-VICTIM` (*Nipun Saxena v Union of India* (2019) 2 SCC 703), `R-HEALTH`, `R-COMMERCIAL` (trade secret), `R-PRIVILEGE`, `R-THIRD-PARTY`, `R-OTHER` (free text ≤ 200).
- **True redaction**: the redacted rendition is re-rasterised for the affected pages (300 dpi) or content-stream edited with text removal verified; metadata (XMP, document info, attachments, form fields, JavaScript, hidden layers) is stripped. A post-check extracts all text from the output and fails the job if any redacted string or pattern match survives (`REDACTION_INCOMPLETE`).
- Two-person rule for redactions used in court exports and publication (maker: party/case_manager; checker: different user with `case_counsel` or `quality_officer`).
- The redaction log (box coordinates, reason, actor) is stored, but the log itself is visible only to the redacting side and registry.

### 1.12 Watermarking

| Context | Watermark | Position |
|---|---|---|
| Download of `high`/`sealed` documents (any role) | "{viewer name} · {case number} · {UTC timestamp} · Confidential — A&C Act s.42A / Equator Rules" | Diagonal, 15% opacity, every page; plus footer line |
| View-only streaming | Same, tiled | Image tiles |
| Committee papers (App. S) | Member name | Footer |
| Bundles for parties | "{bundle type} v{n} · {case number}" footer (pagination stamp, not a watermark) | Footer |
| **Court exports** (§5) | **None** — Telangana e-Filing Rules 2020 r.8.7 prohibits watermarks and encryption | — |
| Publication renditions (App. R) | "Published with the consent of the parties" footer | Footer |

Watermarked files are renditions of kind `watermarked_download`, generated per request, not stored beyond 24 hours, and their hashes are logged in `audit.access_log` so a leaked copy can be traced.

### 1.13 Download and print controls

| Tier × audience | Party (own filing) | Party (served on them) | Representative | Neutral | Registry | Auditor |
|---|---|---|---|---|---|---|
| `standard` | Download original + print | Download + print | Per scope `receive_notices`/`file_documents` | Download + print | Download + print | Watermarked download |
| `high` | Download original | Watermarked download; print watermarked | Watermarked | Watermarked | Download; export reason required | Watermarked, ≤ 90-day grant |
| `sealed` | View-only (own uploads downloadable) | View-only | View-only | View-only unless order of the tribunal records need | Break-glass only | Not available |

Tenant policy may tighten (never loosen) these defaults. Mobile caches only opened documents, encrypted, wiped on logout or remote wipe (FR-P02-40). Every download or print writes `audit.access_log` (`action ∈ {view, download, print, export}`, `rendition_id`, `watermark_hash`).

### 1.14 Legal hold

- Scopes: `document`, `case`, `party_side_in_case`, `tenant_matter_tag`.
- Who: `registrar`, `dpo`, `legal_reviewer`; reason codes: `LITIGATION_PENDING` (s.34/s.36/s.37 or other court proceedings), `REGULATOR_REQUEST`, `DSR_DISPUTE`, `INVESTIGATION`, `COURT_ORDER`, `AUDIT`.
- Effect: S3 Object Lock legal hold on all versions and certified bundles; `legal_hold = true` on rows (via SECURITY DEFINER `documents.set_legal_hold()`, Appendix F); retention jobs skip; erasure requests under DPDP Act 2023 s.12 are answered with the retention ground (s.8(7) "unless retention is necessary for compliance with any law") and a review date.
- Release requires a second approver (`dual`) and writes `equator.documents.legal_hold.released.v1`; the retention clock resumes from release.

### 1.15 Retention

Retention classes and periods are configuration (`core.retention_classes`, master §11): `case_record` 8 years after closure; `caucus_note` 12 months after closure; drafts never filed — 90 days after closure; `call_recording_recovery` ≥ 6 months; `ai_log` 12 months; watermarked downloads 24 hours; quarantine 7 days; rejected uploads (malware) — bytes destroyed immediately, hash and reason kept 1 year. A nightly `RetentionSweepJob` computes `retain_until`, issues S3 deletion only after Object Lock expiry, writes an erasure certificate (`core.erasure_certificates`: object keys, hashes, timestamp, job run ID) and leaves a tombstone row. Awards, settlement instruments, certified copies and execution packs use class `outcome_instrument`: 13 years from the instrument date or 1 year after execution completes, whichever is later (X-36; Appendix Q Q-R4), overriding the 8-year case default; they may be retained longer, or permanently, where the tenant's records policy says so (institutional record of arbitral outputs); the policy is shown in the privacy notice (NN-15).

### 1.16 Own-side review sets *(v3.1)*

For large productions or evidence sets a party side (including its representatives within scope) may open a **review set**: a saved selection of its own or served documents to review before filing, production or a hearing. Review sets live entirely in the side's private space — never visible to another side, the neutral or the registry, never indexed for other sides, and excluded from neutral packets and bundles (L-D-01).

| Element | Rule |
|---|---|
| Batches | The set is split into batches (default 50 documents) assigned to named reviewers on the side; a reviewer who marks themselves unavailable is skipped and the batch moves to the next reviewer named for the set |
| Coding panel | Per document: relevant / not relevant / needs second look; privilege (`none`, `privileged`, `without_prejudice`); confidentiality tier proposal; issue tags; free note (side-private). Keyboard: `1`/`2`/`3` code, `P` privileged, `N` next, `B` back |
| Quality check | A second reviewer re-codes a random 10% sample (configurable 5–25%); disagreement above 10% reopens the batch |
| Privilege log | One click generates a privilege log (date, author, recipients, document type, privilege basis, Bates/exhibit label) as a DOCX/XLSX draft in `DRF`; it is filed only through the normal share dialog when a tribunal direction or share request requires it |
| Production | "Produce coded set" files all documents coded relevant and not privileged in one batch (bulk upload rules above), with the share request or direction it answers linked (§2.5) |
| Progress | Dashboard per set: documents coded, privileged count, QC agreement, days to the due date of the linked request or direction |

Review sets are a T setting per tenant (`tenant.dms.review_sets.enabled`, default ON for professional users); AI may propose relevance and privilege codes only as suggestions marked "AI suggestion — check" (`requires_human_review = true`, NN-01), and a party's AI suggestions are never visible to the other side or the neutral (FR-P11-V2-L07). *(v3.1)*

---

## 2. Visibility and sharing model

### 2.1 Lifecycle states (`core.documents.visibility_state`)

| State | Meaning | Who can see | Entered by | Leaves to |
|---|---|---|---|---|
| `PRIVATE_DRAFT` | In the party's `DRF` space; not part of the case record | Owning side only (party, org users, representatives with `file_documents` scope) | Upload to drafts; AI Pleadings Studio output (App. M) | `FILED`, deleted by owner |
| `FILED` | Submitted to the registry; awaiting scrutiny | Owning side + registry | `POST /v1/documents/{id}/file` | `ON_RECORD`, `RETURNED` |
| `RETURNED` | Scrutiny found curable defects (§3.2) | Owning side + registry | case_manager | `FILED` (re-filed), `WITHDRAWN` |
| `ON_RECORD` | Accepted onto the case record | Owning side + registry + neutrals per audience | case_manager acceptance (or auto-accept rule) | `SERVED`, `WITHDRAWN` |
| `SERVED` | Transmitted to the audience parties with a service record | Audience set (§2.2) | Service step (§3.5) | `SUPERSEDED`, `WITHDRAWN` (marked, never removed) |
| `SUPERSEDED` | A later version is current | Same as before; labelled | New version | — |
| `WITHDRAWN` | Withdrawn by the filer (with leave after service) | Same audience; banner "Withdrawn on {date}" | Party request + case_manager / neutral leave | — |
| `ISSUED` | Institution/neutral output (orders, awards, notices) | Per instrument | Signing + issue (P04/P06) | `SUPERSEDED` (correction), `SET_ASIDE` (manual on court order) |

Guards: a `SERVED` document can never return to a narrower audience (`DOC_VISIBILITY_DOWNGRADE_FORBIDDEN`); withdrawal after service keeps the record (A&C s.24(3) material already communicated) and only marks it.

### 2.2 Audiences

A document's audience is a set of **audience keys** stored in `core.document_shares` (one row per grant):

| Audience key | Grants read to | Notes |
|---|---|---|
| `OWN_SIDE` | Uploader's party side (party, org users, representatives in scope) | Always present |
| `PARTY:{case_party_id}` | A named other party (and its representatives in scope) | Multi-party cases may share with some parties only — **not allowed in arbitration filings** (L-D-03) |
| `ALL_PARTIES` | Every party in the case, including later-joined parties | Default for pleadings and arbitration filings |
| `NEUTRAL:{proceeding_id}` | Appointed neutrals on that proceeding (and `tech_concierge` metadata only) | Becomes effective only after appointment is `confirmed` |
| `NEUTRAL_ONLY:{proceeding_id}` | Neutrals only, not other parties ("caucus share") | Mediation / conciliation only; conciliator bound by A&C s.70 proviso; never reaches the arbitral record (master §5.3) |
| `REGISTRY` | case_manager, registrar, deputy_registrar, case_counsel, quality_officer assigned | Always present except for `PRIVATE_DRAFT` and `NEUTRAL_ONLY` (registry sees metadata only for `NEUTRAL_ONLY`) |
| `INTERNAL` | Registry roles only | `INT` folder; parties and neutrals never |
| `EXTERNAL_LINK:{secure_link_id}` | A named external recipient via secure link (§2.5) | Expert, interpreter, executing officer, bank, sub-registrar |
| `PUBLIC` | Anyone | Set only by the App. R publication service on a `redacted` rendition (NN-26, L-D-11) |

### 2.3 Mapping from earlier enums

| FR-P02-36 `confidentiality` | New model |
|---|---|
| `shared` | `ON_RECORD`/`SERVED` with `ALL_PARTIES` + `NEUTRAL` + `REGISTRY` |
| `own_side_only` | `PRIVATE_DRAFT` (if not filed) or `FILED` with `OWN_SIDE` + `REGISTRY` (a filed but unserved document, e.g., a fee document) |
| `neutral_only` | `NEUTRAL_ONLY:{proceeding_id}` + `OWN_SIDE` |
| `sealed` | `confidentiality_tier = sealed` (orthogonal to audience); stored in the sealed bucket |

### 2.4 "Party chooses what to share and with whom"

**Share dialog (SCR-P02-61)** opens on "File" or "Share" and shows, in this order:

1. **What** — selected documents with page counts, exhibit labels to be assigned, and warnings (untranslated vernacular, unverified type copy, missing s.63 Part A for electronic records, privileged flag).
2. **With whom** — radio options generated from the mechanism matrix:

| Mechanism of the active proceeding | Options shown | Default |
|---|---|---|
| Arbitration, med-arb (arbitral phase), arb-med (arbitral phase), expert determination with adversarial rules | "File with the tribunal and serve on all parties" (only option) | That option; tooltip cites A&C s.24(3) |
| Mediation (contractual), mediation (statutory, flag ON) | "Share with everyone in this mediation" · "Share with the mediator only (private session)" · "Share with selected parties" (multi-party only) | Everyone |
| Conciliation (Part III) | As mediation; the "conciliator only" option shows: "The conciliator will keep this confidential because you asked (A&C Act s.70)" | Everyone |
| Negotiation (assisted) | "Share with the other side" · "Share with Equator case manager only" | Other side |
| Pre-proceeding (scrutiny stage) | "File with Equator (registry)"; service follows acceptance | File |
| GRM ticket | Desk + complainant per P09 (GRM SaaS) | — |

3. **Confirm** — summary; checkbox "I am entitled to share these documents and they are accurate copies"; representatives see their scope chip; step-up (OTP or passkey) for `high` tier.

Rules: (a) privileged documents cannot be shared beyond `OWN_SIDE` unless the owner first sets `privilege = none` with a confirmation ("You are waiving privilege for this document"); (b) without-prejudice documents can be shared in mediation/negotiation but are excluded from arbitral bundles and the arbitral record (A&C s.81 for conciliation material; policy for mediation); (c) a party cannot share another party's document onward outside the case (download controls §1.13; secure links only by owner or registry); (d) a document shared `NEUTRAL_ONLY` in mediation is never transmitted into a later arbitration on the same case, even if the same neutral continues under master §5.3 — it is carried as `privilege = caucus_derived`.

### 2.5 Share requests and production directions

- **Party request** (`core.share_requests`): requester side → target side, list of described documents (free text ≤ 500 chars each), reason, due date (default 7 days). Target responds: share (via §2.4), decline with reason (visible to requester), or "does not exist". Overdue requests surface on the case manager's dashboard; Equator cannot compel production.
- **Neutral direction**: in arbitration, a procedural order (P04) creating `document_request` tasks with the tribunal's due date; non-compliance is recorded for the tribunal (A&C s.25 consequences are the tribunal's decision). In mediation, the mediator may only invite production.
- **Registry request**: scrutiny deficiencies (§3.2).

### 2.6 Secure links (external recipients)

| Field | Rule |
|---|---|
| Creator | Owning side (own documents only), case_manager/registrar (any on-record document, for listed purposes) |
| Purpose (mandatory) | `EXPERT_REVIEW`, `INTERPRETER`, `EXECUTING_OFFICER`, `BANK_ESCROW`, `SUB_REGISTRAR`, `REGULATOR`, `COURT_FILING_SUPPORT`, `PARTY_ADVISER`, `TRANSLATOR` |
| Recipient | Name, email and mobile; OTP to that contact on each opening session (30-minute session) |
| Expiry | Default 7 days; max 30 days (90 for `EXECUTING_OFFICER`); no "never expires" |
| Permissions | `view_only` (default) / `download` (watermarked) |
| Limits | Max opens (default 20), max downloads (default 3), IP country allow-list (default IN; INT cases add parties' countries) |
| Revocation | Instant by creator or registry; revocation invalidates sessions within 60 s |
| Disclosure register | Each link writes a `core.disclosures` row (purpose code) — the Disclosure Register of App. R / S8 S8-FR-20 |
| Sealed tier | Not allowed (`SECURE_LINK_SEALED_FORBIDDEN`) except `EXECUTING_OFFICER` with registrar dual approval |
| Token | 256-bit random, stored as SHA-256 hash; URL `https://equatorresolution.in/s/{token}`; never in SMS body for `high` tier (email + OTP on SMS instead) |

### 2.7 Access and download history

Each document has an **Activity** panel (SCR-P02-62) listing, from `audit.access_log` and `audit.audit_events`: uploaded, filed, returned, accepted, served (with service record), viewed (by role, not by name, for other sides — e.g., "Viewed by the respondent's side, 3 times"), downloaded (by name for registry view; role for party view), printed, shared, link opened, link revoked, annotated (count only), type copy/translation created and verified, signature events, hold set/released. Parties see who on **their own side** did what and only aggregate views by the other side; registry sees everything; auditors see a scoped export.

### 2.8 Tamper-evident audit

Every state change, share, link event, download, rendition creation, verification attestation, redaction and hold writes `audit.audit_events` (hash-chained; NN-22). Every version and every certified rendition is entered in `core.evidence_ledger` (Appendix F §F.4.6). The `/verify` service accepts a SHA-256 (computed in the browser when the user picks a file — the file is never uploaded, App. R §5.3) and answers only "matches a document issued/filed on {date} in an Equator case" or "no match" (no content, no names; A&C s.42A).

### 2.9 Policy (Cerbos excerpt)

```yaml
resourcePolicy:
  resource: document
  version: "2026_10"
  rules:
    - actions: ["read"]
      effect: EFFECT_ALLOW
      condition: { match: { expr: "request.resource.attr.audience_keys.exists(k, k in request.principal.attr.audience_keys)" } }
    - actions: ["share_neutral_only"]
      effect: EFFECT_DENY
      condition: { match: { expr: "request.resource.attr.mechanism in ['arbitration','emergency_arbitration','appeal']" } }   # L-D-03
    - actions: ["read","download"]
      effect: EFFECT_DENY
      condition: { match: { expr: "request.resource.attr.folder == 'INT' && !('registry' in request.principal.attr.case_role_classes)" } }
    - actions: ["set_public"]
      effect: EFFECT_DENY
      condition: { match: { expr: "request.principal.attr.service != 'publication'" } }   # NN-26
    - actions: ["download"]
      effect: EFFECT_DENY
      condition: { match: { expr: "request.resource.attr.tier == 'sealed' && !request.principal.attr.break_glass" } }
```

Principal `audience_keys` are computed per request by the policy service from `core.case_parties`, `core.party_representatives` (scope), `core.appointments` (confirmed) and staff assignments, and are the same keys written to OpenSearch `acl_keys` (§1.6).

---

## 3. Workflow: filing → scrutiny → transmission → orders → service

### 3.1 Step table

| # | Step | Actor | Action | SLA / clock | Output / event |
|---|---|---|---|---|---|
| 1 | Prepare | Party / representative | Upload to `DRF`, or draft in App. M Studio; build court-format document (§5) if needed | — | `PRIVATE_DRAFT` |
| 2 | Pre-file checks | System | Format lint (profile), annexure index, untranslated vernacular, unverified type copies, s.63 Part A prompt for electronic records, signature/verification block present, file-size and type | Instant | Lint report; blocking vs warning list |
| 3 | File | Party | Share dialog (§2.4), step-up for `high` tier, e-sign of filing declaration (virtual sign permitted for procedural filings, P06 FR-P06-14) | — | `FILED`; `equator.documents.document.filed.v1` |
| 4 | Scrutiny | case_manager | Checklist §3.2; accept / return with defects | 2 working days (pleadings); 1 working day (applications); same day if an order of the tribunal fixes a shorter date | `ON_RECORD` or `RETURNED` |
| 5 | Defect cure | Party | Re-file corrected version | 7 days default (rules-of-procedure value; never extends a statutory clock) | — |
| 6 | Transmission to neutrals | case_manager | Adds to the **neutral packet** for the proceeding (auto for accepted pleadings after appointment) | Same day as acceptance | `NEUTRAL:{proceeding}` audience; notification to neutral |
| 7 | Service on parties | System (notices engine) | Service of the document on audience parties with delivery evidence (§3.5) | Same day | `SERVED`; service record |
| 8 | Neutral action | Neutral | Reads, annotates (private), issues directions/orders (§3.4) | Per rules | Orders `ISSUED` |
| 9 | Order service | Registry | Serve the order on all parties; start clocks fixed by the order | Same day as signature | `equator.proceedings.order.served.v1` |

The case manager **shares with independent neutrals**; neutrals never receive documents directly from a party outside the platform (no email attachments), and a neutral's team never uploads into a party's folders.

### 3.2 Scrutiny checklist (form, never merits)

| Code | Check | Defect text shown to the filer |
|---|---|---|
| SCR-F01 | Correct proceeding and filing type selected | "Choose the correct filing type." |
| SCR-F02 | Render profile lint passed (margins, font, spacing, page size) where a profile is mandated by the rules of procedure | "Page layout does not meet {profile}." |
| SCR-F03 | Pages numbered continuously; index page numbers match | "Index page numbers do not match the document." |
| SCR-F04 | Each annexure separately indexed and marked (SC Rules 2013 O.XXI r.3(1)(d)(i) style) | "Annexure {n} is not separately listed in the index." |
| SCR-F05 | Vernacular annexure has an English (or language-of-record) translation, labelled correctly (§7.6) | "Annexure {n} needs a translation into {language}." |
| SCR-F06 | Handwritten / screenshot annexure has a type copy (verified or marked unverified with reason) | "Add a type copy for Annexure {n}." |
| SCR-F07 | Electronic records have a s.63(4) Part A certificate where the filer intends court use or the tribunal has directed | Warning only in arbitration (A&C s.19(1)); see §8.5 |
| SCR-F08 | Verification / statement of truth / affidavit present where the rules require; affidavit sworn copy uploaded (L-D-12) | "The affidavit must be sworn before a notary or oath commissioner." |
| SCR-F09 | Signature of party or authorised representative within scope (NN-27) | "This filing must be signed by {role}." |
| SCR-F10 | Fees paid where the tariff charges the filing (P05) | "Fee pending." |
| SCR-F11 | No unmasked Aadhaar (NN-14), no malware, no password protection | "Remove the password / mask the Aadhaar number." |
| SCR-F12 | Size and split rules for the profile | "This file exceeds {n} MB; we will split it." (auto) |

The scrutiny decision never comments on the strength of a case (NN-01); AI may draft defect wording (`case_manager_copilot`) with `requires_human_review = true`.

**Scrutiny queue and batch scrutiny *(v3.1)*.**

| Element | Rule |
|---|---|
| Automatic checks | SCR-F02, F03, F04, F11 and F12 run at filing and are pre-marked pass or fail with evidence (lint report); SCR-F05 and F06 are pre-marked from rendition status; the case manager decides the rest and may override an automatic result only with a reason |
| Queue order | (1) filings tied to a tribunal-fixed date or a statutory clock, nearest first; (2) re-filed documents after a return (diff shown against the returned version); (3) other filings by scrutiny SLA due time (§3.1 step 4); ties by filing time. Order never depends on the filer's identity or plan |
| Return with defects | One action returns the filing with the failed codes and their fixed defect texts pre-filled (editable, never merits); the defect-cure clock (§3.1 step 5) starts on service of the return; the scrutiny SLA stops while the filing is `RETURNED` and restarts on re-filing |
| Batch accept | For procedural filings only (applications for time, consents, scheduling) whose automatic checks all pass and have no warnings, the case manager may select up to 50 and accept them together after a preview list; pleadings, evidence and anything with a warning are always accepted one by one |
| Escalation | At 80% of the scrutiny SLA an amber flag; at breach a task to the `registrar` with the queue position; breaches feed the case-manager KPI "scrutiny within SLA" (target ≥ 95%) |
| Second filer view | The filer sees "With the case team for checking — usually {n} working days" and, after return, the exact items to fix with a "Fix and re-file" button that opens the returned version in the drafts space |

### 3.3 Neutral packet

`core.neutral_packets` per proceeding: ordered list of on-record documents with a cover memo (registry-authored; procedural only: parties, representatives, clocks, pending applications — the Registry Report of App. R), versioned; each update notifies neutrals with a "What changed" diff. Neutrals see **only** documents in the packet plus served filings; they never see `PRIVATE_DRAFT`, `INT`, other proceedings' `NEUTRAL_ONLY` material, or App. M drafts/prompts (S7 §3.8 neutrality overlay).

### 3.4 Orders back from neutrals

Neutral drafts an order in the neutral workspace (template from `core.document_templates`, render profile `EQR_TRIBUNAL`), optionally assisted by `drafting_assistant` (procedural text only; reasoning authored by the neutral, S7 FR-S7-DRAFT-14) → sign (DSC Class 3 or Aadhaar eSign; multi-member: presiding arbitrator signs procedural orders if the tribunal so authorises, A&C s.29(2)) → registry check of form (case number, date, signatures, parties) → `ISSUED` into `ORD` with audience `ALL_PARTIES` → service (§3.5) → clocks fixed by the order created with owners (NN-04).

### 3.5 Service of documents

Documents are served through the notices engine (P02 §4.8) as a **document-service notice** (`notice_type = document_service`): portal notification + email with secure link (no attachment for `high` tier) + SMS/WhatsApp alert where the party has consented; the service record (`core.service_attempts`) is linked to the document version and its hash. Deemed service follows the pinned rules of procedure and A&C Act s.3 for written communications. Representatives with `receive_notices` scope are served per Appendix S §4.10.

### 3.6 E-bundles

Extends FR-P02-39.

| Bundle type | Built by | Content rule | Audience |
|---|---|---|---|
| `pleadings_bundle` | system on completion of pleadings | All pleadings + annexures in filing order | All parties, tribunal |
| `core_bundle` | case_manager or parties jointly | Agreed key documents; each party approves the index (two-step approval) | All parties, tribunal |
| `hearing_bundle` | case_manager on tribunal direction | Documents for a listed hearing, in the order directed | All parties, tribunal |
| `authorities_bundle` | each party | Statutes/judgments **from the verified corpus only** (App. M; *Pooja Ramesh Singh v J&K Bank Ltd*, 2026 INSC 668, 2 Jul 2026) | All parties, tribunal |
| `court_paper_book` | party (own) | §5.3 anatomy for the chosen court profile | Owner; exported |
| `execution_pack` | system (P06) | P06 FR-P06-23 | Award-holder |

**Bundle rules:** (1) only `ON_RECORD`/`SERVED`/`ISSUED` versions (never drafts, privileged or `NEUTRAL_ONLY` items, except a party's own `court_paper_book`); (2) **pagination**: continuous Arabic numerals stamped bottom centre `Page n of N`, plus footer `{case number} · {bundle type} v{version}` in 9 pt; original page numbers of source documents are preserved; (3) **index**: S. No. · Particulars · Exhibit/annexure label · Date · Pages (from–to) · Remarks; each annexure separately indexed; (4) **bookmarks**: level 1 = index rows, level 2 = sub-documents and type copies/translations; (5) **hyperlinks**: index rows and in-text exhibit references (`[Ex. C-3, p. 4]`) link to the bundle page; (6) **frozen page map**: once a bundle version is served, page numbers are fixed; changes create a new version and a "Bundle change note" listing moved pages; (7) volumes of ≤ 2,000 pages (FR-P02-39) with a master index; (8) each bundle carries `manifest.json` (SHA-256 per item, Merkle root) and, before `certified`/`exported`, a s.63 Part A certificate (Appendix F `core.bundles` CHECK; NN-10).

---

## 4. eSign integration (document side)

Signing orchestration and signer methods are P06 FR-P06-14; this section fixes the document-side contract.

### 4.1 Sign request

| Field | Rule |
|---|---|
| `document_version_id` | Must be a PDF/A rendition generated by §5.7 or an uploaded PDF passed through validation; hash frozen at request creation; any change voids the request |
| `instrument_class` | F.3 set; NN-08 classes rejected before the provider call (`ESIGN_EXCLUDED_INSTRUMENT`) |
| `signers[]` | `seq`, person, capacity (`party`, `authorised_signatory`, `representative_under_scope`, `neutral`, `registrar`, `witness`), method (`aadhaar_esign`, `dsc`, `virtual_sign`), page/position anchors |
| Signer order | `sequential` or `parallel_then_sequential` (parties parallel → neutral authentication → registrar certification) |
| Expiry | 7 days default (max 30); reminders day 2 and day 5 within contact windows |
| Representative signing | Only within scope `sign_instruments_on_behalf` and amount limit — a scope that stays locked until a stamped, notarised physical power of attorney is verified (X-21; App. S §4.3); otherwise, and above the limit, the party signs (NN-27) |
| eStamp | Bound to the PDF **before the first signature** for stamped instruments (NN-09; P06 FR-P06-15) — the sign request cannot be sent while the stamp request is not `issued` (`ESTAMP_REQUIRED_BEFORE_SIGNING`) |

### 4.2 Method matrix by document class

| Document class | Aadhaar eSign | DSC Class 3 | Virtual sign | Wet-ink |
|---|---|---|---|---|
| Procedural filings, consents to online mode, scheduling | ✔ | ✔ | ✔ | — |
| Pleadings: statement of claim/defence with statement of truth | ✔ | ✔ | — | optional |
| Affidavits | Draft approval only | Draft approval only | — | **Sworn copy required** (L-D-12) |
| Settlement agreements, s.73 settlements | ✔ | ✔ | Settlement agreements only ≤ ₹50,000, outside FAM and NN-08; never s.73 settlements or INT instruments (FR-P06-14) | physical route for NN-08 |
| Awards, s.12(5) waivers | ✔ (arbitrators: DSC preferred) | ✔ | — | — |
| Letters of Authority / Vakalatnama (App. S) | ✔ | ✔ | — | Vakalatnama for court use per court rules |
| NN-08 excluded instruments (POA, trust, will, immovable sale/conveyance, partition/transfer of immovable property) | ✘ (term sheet only) | ✘ | ✘ | **Physical execution, stamping, registration** (Registration Act 1908 s.17) |

Legal basis: IT Act 2000 s.3A and Second Schedule (Aadhaar e-authentication eSign through CCA-licensed ESPs), s.5 (legal recognition of electronic signatures), s.1(4) read with the First Schedule (excluded documents: negotiable instruments other than cheques, powers of attorney, trusts, wills and other testamentary dispositions, contracts for sale or conveyance of immovable property).

### 4.3 Signature evidence

On completion: download the signed PDF and the ESP audit trail immediately; store both in the evidence bucket; validate signatures against the CCA root chain; record `certificate_serial`, signer name as in certificate, signing time (ESP timestamp), method, IP and device; embed long-term validation data (PAdES-B-LT, ETSI EN 319 142-1) where the ESP supplies it; enter both files in the evidence ledger; generate a **Signature Certificate** page (Equator-issued, appended to the evidence pack, not to the signed instrument) listing signers, methods, times and hashes. A signed version is a new **version** (original), not a rendition.

### 4.4 Excluded instruments and affidavits

- NN-08 detection runs at three points: template selection (instrument class), term structuring (immovable-property terms), and sign-request creation (DB CHECK on `core.esign_requests`).
- Affidavit flow (one flow for every affidavit, Studio-drafted or uploaded; its states and the oath-officer directory are App. M §2.4.17 `studio.affidavits` / `core.oath_officers`): generated with jurat block (deponent identity, place, date, "Identified by" line, Notary/Oath Commissioner seal space) → party e-signs **"Approved for swearing"** (not a jurat) → booking task (notary/oath commissioner; e-Courts eFiling 3.0 video-oath note where the forum permits — S8 §1.2) → upload sworn scan → hash → `affidavit.sworn = true`. Original affidavit filing reminder: 7 working days for forums following the Telangana Model e-Filing Rules (r.5) — task with owner (S8 S8-FR-07).

---

## 5. Court-format templates

### 5.1 The Supreme Court A4 standard (default)

Supreme Court of India notice dated **12 March 2020** (effective 1 April 2020), applying to pleadings, petitions, affidavits and other documents filed in the Court (S8 §1.1 [V]):

| Parameter | Requirement | Profile token value (`SC_2020_PRINT`) |
|---|---|---|
| Paper | A4, 29.7 cm × 21 cm, superior quality, **minimum 75 GSM** | `page.size = A4 (210 × 297 mm)`; print note "A4 · 75 GSM or above · print both sides" on the export cover sheet (not on the document) |
| Printing | **Both sides** of the paper | `duplex = true`; recto/verso aware layout; `blank_verso_before_annexure = false` (registry practice toggle) |
| Font | **Times New Roman, 14** | `font.body = "Times New Roman" 14 pt` (embedded; metric-compatible fallback Liberation Serif only if the licence check fails, logged) |
| Line spacing | **1.5** | `line.spacing = 1.5` |
| Quotations and indents | **Font 12, single line spacing** | Style `Quote`: 12 pt, single, indent 1.27 cm left and right |
| Margins | **Left and right 4 cm; top and bottom 2 cm** | `page.margin = T 20 · B 20 · L 40 · R 40 mm`; mirror margins **off** (the notice fixes left/right, not inside/outside) |

Supreme Court Rules 2013 points carried into the profile: O.VIII r.2 (no document in a language other than English without translation) and r.3 (translation by a translator approved by the Court) → any non-English annexure blocks an SC export unless a translation is attached, and the export shows "Court-approved translator certification required" (S8 S8-FR-06); O.XXI r.3(1)(b) chronological list of dates; r.3(1)(d)(i) annexures indexed separately and arranged chronologically with page numbers cited in the petition; r.3(1)(e) affidavit verifying facts and list of dates. O.VIII r.1's older "double-line spacing, one side" text is overridden by the 2020 notice for paper, sides and spacing.

### 5.2 Render profiles (`core.render_profiles`)

| Code | Forum | Status at seed | Page | Margins (T/B/L/R) | Body font | Spacing | Quote style | Page numbers | Header | Max file | Annexure series | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SC_2020_PRINT` | Supreme Court — print/physical and default court style | `verified` | A4 | 20/20/40/40 mm | TNR 14 | 1.5 | 12 single | Bottom centre, all pages; cover unnumbered unless toggled | None | n/a (print) | P- / R- | SC notice 12 Mar 2020 |
| `SC_EFILING` | Supreme Court e-filing (efiling.sci.gov.in) | `unverified` | A4 | as `SC_2020_PRINT` | TNR 14 | 1.5 | 12 single | as above | None | **[VERIFY — open (vendor): SC E-Filing Manual (main.sci.nic.in) states PDF/legible only — no size, PDF/A or bookmark limit; confirm by AOR test upload (S8 §1.2)]**; default 20 MB split | P- / R- | — |
| `HC_TS_EFILING_2020` | High Court for the State of Telangana and District Judiciary (model rules; reused for HCs following the e-Committee model) | `verified` | A4 | 1.5″/1.5″/1.75″/1.0″ (38.1/38.1/44.45/25.4 mm) | TNR 14; local-language trial-court documents Unicode 14 | 2.0 | 12 single (practice) | All pages | None | **20 MB** per file, split in sequence (r.3.4) | P- / R- | Notification No. 15/SO/2020, Gazette 29 Oct 2020, eff. 2 Nov 2020, rr.6.1–6.3, 8.1, 8.6, 8.7 |
| `HC_RJ_EFILING` | Rajasthan High Court | `verified` | **Legal** (216 × 356 mm) | as per existing rules (seed: HC model values, flagged) | 14 pt+ in a listed font (TNR default); Hindi only in Unicode | as per existing rules (seed 2.0) | 12 single | **All pages incl. front page; index and list of dates numbered bottom centre from 1** | **Running header right-aligned: document name + filing party, every page except the front page** | **20 MB per upload** | P- / R- | hcraj.nic.in Guidelines for e-Filing |
| `HC_GENERIC` | Other High Courts (Original/Appellate Side) | `unverified` | A4 | HC model values | TNR 14 | 2.0 | 12 single | All pages | None | 20 MB | P- / R- | To be verified per HC (Delhi HC (Original Side) Rules 2018 etc.) |
| `DIST_COMMERCIAL` | District courts and Commercial Courts (CPC; Commercial Courts Act 2015) | `unverified` except in Telangana (inherits `HC_TS_EFILING_2020`) | A4 | per state HC rules | TNR 14 / Unicode 14 | 2.0 | 12 single | All pages | None | 20 MB | Annexure P-/D- (plaintiff/defendant) labels only — exhibit numbers are assigned by the court on proof (CPC O.XIII r.4) **[VERIFY — open (counsel): state-wise annexure/exhibit practice]** | State e-filing rules |
| `NCLT` | National Company Law Tribunal / NCLAT | `unverified` | A4 | top 40 / left 50 / right 25 mm (NCLAT Rules 2016 r.19(1); NCLT r.158 for orders) **[VERIFY — open: NCLT pleading-rule number and e-filing portal limits]** | TNR 14 | 2.0 | 12 single | All pages | None | Seed 20 MB | A- (applicant) / R- **[VERIFY]** | NCLT Rules 2016 |
| `EQR_TRIBUNAL` | Equator arbitral tribunal / mediation outputs (awards, orders, settlements not filed in court) | `verified` (Equator policy) | A4 | 25/25/30/25 mm | Source Serif 4 or TNR 12; Indic Noto Serif 12 | 1.15 | 11 single | "Page x of y", bottom centre | Case number + confidentiality legend | 50 MB | C- / R- / CC- / T- / J- | S8 §1.4 `EQR_INTERNAL` |
| `FOREIGN_SEAT` | Foreign-seated or international proceedings (ICC, SIAC, LCIA, HKIAC, etc.; no institutional format mandate) | `verified` (Equator policy) | A4 (US Letter option for US-seated matters) | 25/25/25/25 mm | TNR or Calibri 12 | 1.5 | 11 single | Bottom centre | Case reference | Per tribunal's procedural order | C- / R-; legal authorities CLA- / RLA- (common international practice) | Tribunal's PO1 governs |

Profile tokens (all profiles): `page.size`, `page.orientation`, `page.margin`, `font.body`, `font.heading`, `font.quote`, `font.indic_map` (language → Unicode font), `line.spacing`, `para.spacing_after`, `para.numbering` (`decimal_hierarchical` 1., 1.1, 1.1.1), `alignment` (`justified`), `page.number.position`, `page.number.start`, `page.number.on_cover`, `header`, `footer`, `duplex`, `pdf.standard` (`PDF/A-2b` default; `PDF/A-1b` option), `pdf.ocr_required`, `pdf.scan_dpi` (300), `pdf.bookmarks` (`from_index`), `pdf.max_mb`, `pdf.split_at` (`bookmark_boundary`), `pdf.encryption` (off for court profiles), `pdf.watermark` (off for court profiles), `pdf.annotations` (`flatten_none` — none included), `filename.max_chars` (45), `filename.banned` (`" # % & * : < > ? \ / { } | ~`, consecutive periods, leading/trailing period, leading underscore), `signature` (`PAdES` via DSC or eSign; visible block with "/sd/" convention where the forum requires), `annexure.prefix`, `translation.required_for_non_language_of_court` (true), `original_affidavit_reminder_days` (7 working days for TS model, r.5), `legacy_font_block` (true: Kruti Dev, DevLys and other non-Unicode Indic fonts rejected with a conversion offer — S8 S8-FR-08).

Profile governance: `draft → in_review → verified | unverified_published → superseded`; only `legal_reviewer` can set `verified`, with `source_ref` and `verified_on`; exports from `unverified_published` profiles carry a cover-sheet notice "Formatting based on {source}; check the current rules of {forum} before filing" and the UI never says "court-ready" for them.

### 5.3 Document anatomy (component catalogue)

A court-format document is assembled from components in `core.court_document_components`. Order is profile-specific; the default (SC paper-book practice, S8 §1.1) is:

| # | Component | Required in | Content and rules | Data source |
|---|---|---|---|---|
| 1 | **Cover / title page** | All court profiles | Forum name ("IN THE SUPREME COURT OF INDIA / CIVIL APPELLATE JURISDICTION"), proceeding type and number or "Diary No. ___ / (to be numbered)", cause title (petitioner(s) **versus** respondent(s) with status), document title ("PAPER BOOK", "PETITION UNDER SECTION 34 OF THE ARBITRATION AND CONCILIATION ACT, 1996"), "WITH" list of IAs, filed by (advocate/AOR or party-in-person block with enrolment no., contact), place and date | Case parties, representative records (App. S), user input |
| 2 | **Index** | All | Columns: S. No. · Particulars · Page No. (Part I / Part II where applicable) · Remarks; **each annexure on its own row** (SC Rules 2013 O.XXI r.3(1)(d)(i)); page numbers auto-filled from the frozen page map; remarks hold arbitral exhibit labels (L-D-10) and "Type copy at p. __" / "Translation at p. __" | Assembler |
| 3 | Office report / listing proforma | SC (registry-generated) | Placeholder page only | — |
| 4 | **Synopsis and List of Dates** | SC SLP; HC profiles where enabled | Synopsis ≤ 3 pages (practice; lint warns beyond); list of dates as two-column table **Date · Event** in chronological order; each event anchored to an annexure page (App. M grounding: unanchored rows flagged) | App. M chronology; user |
| 5 | **Memo of parties** | All court profiles | Full cause title with party numbers, status, addresses for service; **no caste or religion of parties** (SC direction of January 2024 reported in *Shama Sharma v Kishan Kumar* **[VERIFY — open (provisional): order text not yet read; rule applied as Equator policy, case not cited in copy (S8 §2.3)]**); victim/minor identifiers masked per §1.11 reason codes where the law requires | Case parties |
| 6 | Impugned order/award (certified copy) | Challenge/appeal/execution filings | Certified copy from P06 FR-P06-18 with QR | Outcome records |
| 7 | **Body** (petition / application / statement of claim) | All | Headings; **paragraph numbering** `decimal_hierarchical`, continuous across the body; grounds lettered (A, B, C …) where the forum's practice uses lettered grounds (profile toggle); defined terms in first use; cross-references to annexures as "(Annexure P-3 at page 45)" resolved from the page map | App. M Studio or user DOCX |
| 8 | **Prayer** | All | Numbered/lettered reliefs (a), (b) …; "and pass such other order(s) as this Hon'ble Court may deem fit" toggle (forum style); interim prayers within the petition for SC SLPs (O.XXI r.3(1)(a)) | Claims/reliefs (`core.reliefs`) |
| 9 | **Verification / statement of truth** | Pleadings | CPC O.VI r.15 paragraph-wise verification ("true to my knowledge" / "information received and believed to be true" / "legal advice"), place and date; **commercial disputes**: Statement of Truth under O.VI r.15A (Commercial Courts Act 2015 Appendix) via "Commercial" toggle | Verification wizard: user assigns each paragraph range to a knowledge basis |
| 10 | **Affidavit** | Where rules require (SC O.XXI r.3(1)(e); HC rules; CPC O.XIX) | Deponent block (name, age, parentage, address, identity), numbered averments, verification, jurat with Notary/Oath Commissioner space (Oaths Act 1969 s.3(1)(a); Notaries Act 1952); flow per §4.4 | Generator |
| 11 | **Annexures** | As filed | Each preceded by a separator page: "ANNEXURE P-{n}" + "True copy of {description} dated {date}" (or "TYPE COPY" / "TRANSLATION" labels §6.7, §7.6); chronological order (SC O.XXI r.3(1)(d)(i)); type copy and translation follow the original immediately as P-{n}(T) and P-{n}(E) sub-items with their own index rows | DMS + annexure map |
| 12 | **Certificate of translation** | Any translated annexure | §7.7 template; machine translations cannot fill this component (L-D-08) | Certified translation orders |
| 13 | **BSA s.63(4) certificate** | Electronic-record annexures (WhatsApp, email, screenshots, recordings) | Schedule Part A (and Part B when obtained) per §8.5, one per record or per batch with per-file hash table | Evidence ledger |
| 14 | Applications (IAs) | Where filed | Each with its own affidavit; e.g., exemption from filing certified copy (SC O.XXI r.4), permission to file lengthy list of dates | Templates |
| 15 | Vakalatnama / memo of appearance / Letter of Authority | All represented filings | Court vakalatnama per forum rules; Equator LoA (App. S §4) is **not** a court vakalatnama | Representative records |
| 16 | AI-disclosure stamp | Any AI-assisted document | "Prepared with AI assistance; facts verified by {party}; citations verified on {date}" (S7 FR-S7-DRAFT-11; SC Draft AI Regulations 2026 Reg 43(3) readiness — draft Reg 43(3) (SC notice 03.06.2026) requires disclosure at submission by a signed declaration in Annexure I format; not yet notified **[VERIFY — open (watch): final notification; Annexure I text]**) | App. M |

### 5.4 Page numbering rules

- Continuous numbering across the whole paper book, bottom centre (all court profiles); cover page numbered only where the profile says so (`HC_RJ_EFILING` numbers all pages including the front page).
- Index and list of dates numbered from 1 at bottom centre in `HC_RJ_EFILING`; other profiles number continuously.
- Source documents keep their own page numbers; the paper-book number is stamped in a reserved footer band (8 mm) that never overlaps content — the assembler shrinks scanned pages to 96% when content intrudes into the band and logs it.
- Page references in the body and index are **fields** bound to the page map; re-ordering re-computes all references before export; export is blocked if any reference is unresolved (`COURT_EXPORT_UNRESOLVED_REFERENCE`).

### 5.5 Annexure marking

| Context | Series | Example |
|---|---|---|
| Equator arbitration / mediation | FR-P02-37: `C-`, `R-`, `CC-`, `T-`, `J-` | C-4, C-4.12 (page 12 of C-4) |
| Court petition / application (petitioner side) | `P-` | Annexure P-1 … P-n; rejoinder continues the P-series |
| Court counter-affidavit (respondent side) | `R-` (with respondent number where several: R-2/1) | Annexure R-1 |
| IA annexures (some HCs) | `A-` | Annexure A-1 |
| Compiled set of several documents | "(Colly)" suffix | Annexure P-7 (Colly) |
| Type copy / translation of an annexure | `(T)` / `(E)` or `(Tr)` per profile | Annexure P-3(T) |

`core.annexure_maps` stores, per court document: `court_label`, `source_document_version_id`, `arbitral_label`, `page_from`, `page_to`, `kind ∈ {original, type_copy, translation, certificate}`.

### 5.6 PDF output specification (court exports)

| Requirement | Specification | Test |
|---|---|---|
| Standard | **PDF/A-2b** (ISO 19005-2) default; PDF/A-1b option | veraPDF profile validation passes |
| Fonts | All fonts embedded and subset; no Type 3 for body text | `pdffonts` shows `emb yes` for every font |
| Scans | **300 dpi**, greyscale/bilevel unless colour is material; OCR hidden text layer (Telangana r.6.3) | Text extractable from every scanned page |
| Bookmarks | From the index tree (level 1 = index rows; level 2 = sub-documents) (Telangana r.8.1) | Bookmark count = index rows + sub-items |
| Size | ≤ `pdf.max_mb` (20 MB default); auto-split at bookmark boundaries into "Part 1 of n" files; compression JBIG2 (bilevel) / JPEG2000 (greyscale) for scans | Each part ≤ limit; split points at index rows |
| Filename | ≤ 45 characters incl. spaces; banned characters removed; no leading/trailing/consecutive periods (Telangana r.8.6); pattern `{FORUM}_{DocType}_{Party}_{Part}.pdf` | Sanitiser unit tests |
| Prohibited | No watermark, no encryption/password, no annotations, no JavaScript, no embedded files, no forms (Telangana r.8.7) | Static check on output |
| Signature | PAdES via DSC or Aadhaar eSign; visible signature block; validation data embedded | Signature validates in Adobe/EU DSS validator |
| Accessibility | Tagged PDF where the engine supports it (target PDF/UA, ISO 14289) for Equator outputs; not required by courts | Report only |

### 5.7 Template engine design

**Content model.** Every generated legal document is a `LegalDoc` JSON AST (`packages/templates/legaldoc.schema.json`):

```json
{ "schema": "legaldoc.v1", "profile": "SC_2020_PRINT", "language_of_document": "en-IN",
  "meta": { "case_id": "…", "forum": "SC", "doc_type": "slp_civil", "title": "…" },
  "components": [
    { "type": "cover", "data": { "forum_lines": ["IN THE SUPREME COURT OF INDIA","CIVIL APPELLATE JURISDICTION"], "cause_title": {…} } },
    { "type": "index", "auto": true },
    { "type": "list_of_dates", "rows": [ { "date": "2024-03-15", "event": "…", "anchor": { "doc_version_id": "…", "page": 4 } } ] },
    { "type": "body", "blocks": [ { "kind": "heading", "text": "FACTS" },
        { "kind": "para", "num": "auto", "runs": [ { "text": "The Petitioner paid …" }, { "ref": { "annexure": "P-3", "page": "auto" } } ] },
        { "kind": "quote", "text": "…", "source_anchor": {…} } ] },
    { "type": "prayer", "items": [ … ] },
    { "type": "verification", "ranges": [ { "paras": "1-12", "basis": "knowledge" }, { "paras": "13-15", "basis": "legal_advice" } ] },
    { "type": "annexures", "items": [ { "label": "P-1", "doc_version_id": "…", "with": ["type_copy","translation"] } ] } ] }
```

**Pipeline (Temporal `CourtDocumentRenderWorkflow`):**
1. **Validate** AST against schema and profile (component presence, paragraph numbering continuity, every `ref` resolvable, every quote matching its anchor — App. M quote verification).
2. **Render DOCX** with `docx` (npm) from profile tokens: page setup, styles (`Body`, `Quote`, `Heading 1–3`, `ParaNum` multilevel list), Indic font mapping per run language, page number fields.
3. **Convert DOCX → PDF/A-2b** with a pinned LibreOffice build in the sandboxed converter (`--convert-to 'pdf:writer_pdf_Export:{"SelectPdfVersion":{"type":"long","value":"2"}}'`), fonts installed from the approved font pack only.
4. **Assemble** with source annexures (each normalised to PDF/A, OCR'd with `ocrmypdf` where text is missing), separator pages, type copies, translations, certificates; stamp paper-book page numbers; build bookmarks and index links (pikepdf).
5. **Fix references**: second pass fills page numbers in index and body; repeat until stable (max 3 passes; else `COURT_EXPORT_UNRESOLVED_REFERENCE`).
6. **Validate** (veraPDF, fonts, size, filename, prohibited features); on PDF/A failure after post-processing, normalise through Ghostscript `-dPDFA=2` and re-validate.
7. **Split** if over size; **sign** (optional, §4); **hash and ledger**; store DOCX + PDF as renditions of kind `court_export`.

Determinism: same AST + profile version + font pack version + engine version ⇒ byte-identical DOCX and visually identical PDF (pixel diff ≤ 0.1% in golden tests). Engine versions are recorded on the rendition.

**User customisation (SCR-P06-41 Court Document Builder):** users can (a) choose forum and profile; (b) reorder components where the profile allows; (c) edit text in body, prayer and list of dates (rich-text limited to bold, italic, underline, lists, quotes, footnotes); (d) toggle optional components (synopsis, IA, AI-disclosure stamp is mandatory when AI was used); (e) choose document language and bilingual layout (§5.8). Users **cannot** change locked tokens of a `verified` court profile (margins, font, spacing, page size); a "Custom" profile cloned from any profile is available but its exports are labelled "Custom layout — not a court profile". Tenants (Private Chambers) may add profiles through maker–checker.

### 5.8 Language and fonts in templates

- Document language = the language of the forum (English for the Supreme Court and High Courts — Constitution of India Art. 348(1); Hindi or other language in High Courts only where authorised under Art. 348(2) and the Official Languages Act 1963 s.7; district courts per CPC s.137 and State notifications). Profiles carry `language_of_court` and `allowed_languages`.
- Indic documents use Unicode fonts only: Noto Serif Devanagari (hi, mr, ne, sa, kok, mai, doi, brx), Noto Serif Bengali (bn, as, mni-Beng), Noto Serif Gurmukhi (pa), Noto Serif Gujarati, Noto Serif Oriya, Noto Serif Tamil, Noto Serif Telugu, Noto Serif Kannada, Noto Serif Malayalam, Noto Nastaliq Urdu (ur, ks-Arab, sd-Arab, pa-Arab Shahmukhi), Noto Sans Ol Chiki (sat), Noto Sans Meetei Mayek (mni-Mtei), Noto Naskh Arabic (ar), Noto Serif SC/TC (zh), TNR/Noto Serif for Latin and Cyrillic. RTL scripts set paragraph direction RTL with bidi isolation for embedded Latin citations.
- Bilingual layouts: `parallel_columns` (Equator internal only — never for court profiles) or `sequential` (vernacular original followed by English translation, each separately paginated and indexed).

---

## 6. Type copies of handwritten documents, screenshots and WhatsApp chats

### 6.1 Ingestion and detection

| Input | Detection | Pipeline |
|---|---|---|
| WhatsApp export ZIP / TXT | ZIP containing `_chat.txt` or `WhatsApp Chat with *.txt`; TXT whose first 50 lines match §6.2 patterns | `WaChatImportWorkflow` (§6.2) |
| Screenshot (PNG/JPEG/HEIC) | Image aspect ratio and UI classifier: `whatsapp`, `sms`, `gmail`, `banking_app`, `upi_app`, `other` | `ScreenshotOcrWorkflow` (§6.3) |
| Scanned handwritten (PDF/image) | Upload type `scanned_handwritten` or handwriting classifier score ≥ 0.6 on any page | `HandwritingOcrWorkflow` (§6.4) |
| Printed scan | Default | OCR (P02 FR-P02-35); type copy optional |

### 6.2 WhatsApp export parser (`packages/parsers/whatsapp`)

**Variants** (S7 §3.1; golden fixtures required for each — at least 12 locale/platform fixtures, S7-16):

| Variant | Line regex (after Unicode clean-up) | Example |
|---|---|---|
| `android_24h` | `^(\d{1,2})/(\d{1,2})/(\d{2,4}), (\d{1,2}):(\d{2}) - ([^:]+?): (.*)$` | `15/03/24, 10:22 - Ramesh: Payment done` |
| `android_12h` | `^(\d{1,2})/(\d{1,2})/(\d{2,4}), (\d{1,2}):(\d{2})\s?([ap]\.?m\.?) - ([^:]+?): (.*)$` (case-insensitive; U+202F before am/pm normalised) | `15/03/24, 10:22 pm - Ramesh: ok` |
| `ios_bracket` | `^\[(\d{1,2})/(\d{1,2})/(\d{2,4}), (\d{1,2}):(\d{2}):(\d{2})(\s?[AP]M)?\] ([^:]+?): (.*)$` | `[15/03/24, 10:22:11] Ramesh: ok` |
| `dotted_date` | Same as above with `.` or `-` as date separator (de/ru/some Indian locales) | `15.03.24, 10:22 - …` |
| System line | Timestamp prefix without `Sender:` | `15/03/24, 10:20 - Messages and calls are end-to-end encrypted…` |

**Normalisation (each message → `core.wa_messages`)**: `seq`, `ts_local`, `ts_utc` (uploader-declared timezone, default `Asia/Kolkata`), `sender_raw`, `sender_party_id` (mapped by the uploader: "Which of these names is you / the other party?"), `type ∈ {text, media, system, deleted, call, edited}`, `text`, `media_ref`, `edited` (suffix `<This message was edited>` removed and flagged), `forwarded` (U+200E prefix pattern), `source_line_no`, `raw_line` (kept for evidence), `lang`, `script`, `lid_confidence`.

**Rules:** (1) strip U+200E, U+200F, U+202F for parsing; keep raw lines; (2) join continuation lines (no timestamp prefix) to the previous message; (3) **date-order disambiguation**: if any day value > 12 appears in position 1, the format is DD/MM; if in position 2, MM/DD; if still ambiguous, **ask the uploader** with a concrete example ("Is 03/04/24 the 3rd of April or March 4th?") — never guess (`WA_LOCALE_AMBIGUOUS` until answered); (4) media: link `IMG-YYYYMMDD-WA####.jpg (file attached)` (Android) or `<attached: 00000012-PHOTO-…jpg>` (iOS) to ZIP entries by filename, each media file becomes a child document with its own hash; placeholders `<Media omitted>` / `image omitted` counted and reported ("14 media items not included in export"); (5) **cap warning**: exports carry at most the most recent 40,000 messages (media for roughly the latest 10,000) — if the earliest message is later than the dispute start date entered, show "Your export may be missing older messages"; (6) deleted, view-once and call lines kept as typed events; (7) chats with Advanced Chat Privacy cannot be exported — help copy explains and offers screenshots instead.

**Integrity:** SHA-256 of the ZIP and each entry at upload; original ZIP stored WORM; uploader identity, device user-agent, IP and time recorded; s.63 Part A draft generated (§8.5); notice to the uploader: "WhatsApp exports are not digitally signed. The other party may dispute them." with the action **"Ask the other party to confirm this chat"** (joint-authenticity request; on acceptance the exhibit is tagged `admitted_by:{party}`).

**Counter-export diff:** when the other side uploads its export of the same chat, messages are matched on (`ts_utc` ± 60 s, normalised sender mapping, SHA-256 of normalised text); the diff report lists messages present in one export only, edited-flag differences and media-count differences. The report is a neutral-visible **signal**, never a finding.

**Type copy of a chat:** rendered as a table — Msg # · Date · Time · Sender (party label) · Message (original language) · [English translation column when requested] — with system/deleted/call events in italics and media items as "[Image: IMG-20240315-WA0001.jpg — see Annexure P-4/12]". Each row carries `[WhatsApp, msg {seq}, {dd-mm-yyyy hh:mm}]` as its anchor for App. M citations.

### 6.3 Screenshot OCR

1. Classify UI; detect bubbles (sent/received by alignment and colour), timestamps, sender header, quoted replies, date separators.
2. OCR with bounding boxes per bubble (route §6.4); output segments `{bubble_id, side ∈ {left,right}, sender_inferred, time_text, text, bbox, engine, confidence_band}`.
3. EXIF: location stripped from the displayed rendition; retained in the original (WORM) and listed in the s.63 Part A device section.
4. Tamper heuristics (font inconsistency, compression discontinuities, bubble misalignment, status-bar time vs message time) → `tamper_hint` flag only, with the fixed copy "Possible inconsistency detected: the neutral will decide."
5. Multi-screenshot stitching: overlapping screenshots of one conversation are de-duplicated by text overlap; user confirms order.

### 6.4 OCR router and multi-engine confidence

**Routing table (default; tenant may only tighten):**

| Content | Language/script | Primary | Second engine (for agreement) | Data-class guard |
|---|---|---|---|---|
| Printed | 22 Eighth Schedule + English | Sarvam Vision (`sarvam-vision`) | Claude vision (Bedrock India) on low-confidence pages | D2 OK; D3 → Claude vision (Bedrock India) only, or self-hosted |
| Printed | fr, es (and en) | AWS Textract (ap-south-1) | Claude vision | D2/D3 OK (in-region) |
| Printed | ar, zh, ru | Claude vision (Bedrock India) | Google Document AI asia-south1 **only if** `ocr.regional_cloud.enabled` | L-D-06 |
| Handwritten | en | AWS Textract (handwriting; ap-south-1) | Claude vision | D2/D3 OK |
| Handwritten | Indic | Claude vision (Bedrock India) | Sarvam Vision | **Human verification mandatory** |
| Handwritten | fr, es, zh | Claude vision | Azure Read (Central India) only if `ocr.regional_cloud.enabled` | L-D-06 |
| Sealed tier | any | Claude vision (Bedrock India) or self-hosted only | — | NN-07 |

Batching: Sarvam jobs split at 10 pages per PDF, ≤ 10 requests/minute (queue with token bucket); pages > 10 MB downscaled to 300 dpi.

**Confidence bands per line** (`confidence_band`):
- Engines returning confidences (Textract, Google, Azure): `high` ≥ 0.95, `medium` 0.80–0.95, `low` < 0.80 (word minimum for the line).
- Engines without calibrated confidence (Sarvam Vision, Claude vision): **cross-engine agreement** — normalised character error rate (CER) between the two engines' line texts after Unicode NFC and whitespace normalisation: CER ≤ 3% → `high`; 3–10% → `medium`; > 10% → `low` ("human must transcribe") (S7 FR-S7-OCR-06).
- Any line with a number, date, amount, name or signature-adjacent text is capped at `medium` until a human confirms it.
- Page anchor stored for every line: `{doc_version_id, page, bbox, engine, model_version, confidence_band}` (S7 FR-S7-OCR-07) — the anchor App. M cites.

### 6.5 Side-by-side editor (SCR-P02-63)

- Left pane: original page image (zoom, rotate, contrast, magnifier); right pane: editable transcription aligned line by line; hovering a line highlights its bounding box.
- Highlighting: `low` lines amber background with a dashed outline; `medium` pale yellow; words the engines disagree on underlined with the alternative shown on hover ("Engine 2 read: ₹1,50,000"); illegible text is entered as `[illegible]`, uncertain as `[?word]`; struck-through text in the original as `~~text~~` rendered with strike-through; marginal notes as `[margin: …]`; stamps/seals as `[stamp: …]`; signatures as `[signature]` — never transcribed as a name unless printed.
- Keyboard: `Alt+↓/↑` next/previous uncertain line; `Ctrl+Enter` accept line; `Ctrl+I` mark illegible; transliteration input (InScript and phonetic) for Indic.
- Progress bar: lines reviewed / total; "low" lines must all be reviewed before submission.
- Accessibility: both panes keyboard reachable; screen-reader mode reads transcription with confidence band announced.

### 6.6 Correction, verification and attestation

| Status | Meaning | Who moves it |
|---|---|---|
| `machine_draft` | Engine output, not reviewed | System |
| `user_corrected` | Uploader reviewed every `low` line and submitted | Uploader side |
| `verified` | A verifier attested the type copy | Verifier (below) |
| `disputed` | Another party objected to the type copy | Other party (reason mandatory) |
| `superseded` | Replaced by a newer type copy | System |

Verifier: (a) the **uploader** (self-attestation: "I have compared this type copy with the original and it is accurate to the best of my knowledge"); (b) an **independent verifier** — an empanelled transcriptionist/translator from the roster (paid service, App. O), or the party's advocate under scope; (c) for handwriting, `verified` requires (b) or the uploader's attestation **plus** zero unresolved `low` lines. The attestation records name, role, date, IP, the hash of the original version and of the type copy text. A disputed type copy is shown to neutrals with both texts and the objection; the tribunal decides.

### 6.7 Labels and link to the original (NN-32)

Fixed label strings (i18n; tenants cannot edit; lint `LBL-01…LBL-03`):
- Header on every type-copy page: **"TYPE COPY"** + "of {Annexure label / document title}, original at page {n}" + status line: "Machine transcription — not verified" | "Corrected by {uploader side}" | "Verified by {verifier name, role} on {date}".
- Footer: "Original: {SHA-256 first 16 hex}… · Engines: {engine list} · Uncertain passages marked [?] and [illegible]".
- Type copies are never presented without the original in any bundle or export: the assembler always places the original first, then the type copy (`(T)` sub-label).
- "TRUE TYPED COPY" wording is used **only** when the attestation is by an advocate under scope or a verifier with a declared professional capacity, and the profile's practice requires it; otherwise "TYPE COPY".

### 6.8 Attaching type copies to petitions

From the Court Document Builder (§5.7) or the annexure picker, selecting an original that has a type copy offers: "Include type copy (recommended)". The annexure map adds `P-{n}` (original) and `P-{n}(T)` (type copy) as separate index rows with page ranges; the body reference resolves to the original ("Annexure P-3 at page 45; type copy at page 48"). Unverified type copies can be attached only after the user confirms "This type copy is not verified", and the scrutiny check SCR-F06 records it as a warning.

---

## 7. Translation

### 7.1 Language catalogue (`core.languages`; 28 languages + 5 code-mixed classes)

OCR column: SV = Sarvam Vision; TX = AWS Textract (ap-south-1); CV = Claude vision (Bedrock India); G/Az = Google DocAI / Azure Read, regional, flag-gated (L-D-06). MT column: ST = Sarvam Translate; IT2 = IndicTrans2 self-hosted (ap-south-1); CL = Claude (Bedrock India); AWS = Amazon Translate ap-south-1 (AWS Translate ap-south-1 endpoint and 10 Indic languages — hi, bn, gu, kn, ml, mr, pa, ta, te, ur — confirmed from AWS docs 22 Oct 2026) **[VERIFY — open (vendor): Bedrock India model availability; quality tests, S7 §6 item 9]**. Sarvam Translate's 22-language coverage is claimed, not verified (S7 §3.3) — the router falls back to IT2 per language until a coverage test passes.

| # | Language | Code | Script(s) | Dir | OCR primary | MT primary → fallback | Notes |
|---|---|---|---|---|---|---|---|
| 1 | Assamese | as | Bengali-Assamese | LTR | SV | ST → IT2 → CL | |
| 2 | Bengali | bn | Bengali | LTR | SV | ST → IT2 → CL | |
| 3 | Bodo | brx | Devanagari | LTR | SV | IT2 → ST → CL | Low-resource: human review mandatory for any filed translation |
| 4 | Dogri | doi | Devanagari | LTR | SV | IT2 → ST → CL | Low-resource |
| 5 | Gujarati | gu | Gujarati | LTR | SV | ST → IT2 → CL | |
| 6 | Hindi | hi | Devanagari | LTR | SV | ST → IT2 → CL | Code-mixed `hi-Latn` class |
| 7 | Kannada | kn | Kannada | LTR | SV | ST → IT2 → CL | |
| 8 | Kashmiri | ks | Perso-Arabic; Devanagari | RTL / LTR | SV | IT2 → CL | Both scripts |
| 9 | Konkani | kok | Devanagari (official); Kannada; Roman | LTR | SV | IT2 → CL | `kok-Latn` class (Goa chats) |
| 10 | Maithili | mai | Devanagari | LTR | SV | IT2 → ST → CL | |
| 11 | Malayalam | ml | Malayalam | LTR | SV | ST → IT2 → CL | |
| 12 | Manipuri (Meitei) | mni | Bengali; Meetei Mayek | LTR | SV | IT2 → CL | Support both scripts |
| 13 | Marathi | mr | Devanagari | LTR | SV | ST → IT2 → CL | `mr-Latn` class |
| 14 | Nepali | ne | Devanagari | LTR | SV | IT2 → CL | |
| 15 | Odia | or | Odia | LTR | SV | ST → IT2 → CL | |
| 16 | Punjabi | pa | Gurmukhi; Shahmukhi | LTR / RTL | SV (Gurmukhi); CV (Shahmukhi) | ST → IT2 → CL | Shahmukhi relevant to INT |
| 17 | Sanskrit | sa | Devanagari | LTR | SV | IT2 → CL | Maxims; human review |
| 18 | Santali | sat | Ol Chiki; Devanagari; Bengali; Roman | LTR | SV | IT2 → CL | Font: Noto Sans Ol Chiki |
| 19 | Sindhi | sd | Perso-Arabic; Devanagari | RTL / LTR | SV | IT2 → CL | |
| 20 | Tamil | ta | Tamil | LTR | SV | ST → IT2 → CL | `ta-Latn` class |
| 21 | Telugu | te | Telugu | LTR | SV | ST → IT2 → CL | |
| 22 | Urdu | ur | Perso-Arabic (Nastaliq) | RTL | SV → CV | ST → IT2 → CL | Nastaliq OCR weaker: second engine always |
| 23 | English | en | Latin | LTR | SV / TX | — | Default language of record |
| 24 | Arabic | ar | Arabic | RTL | CV (G/Az flag) | CL → AWS | UN |
| 25 | Chinese | zh | Han (Simplified/Traditional) | LTR | CV (G/Az flag) | CL → AWS | UN |
| 26 | French | fr | Latin | LTR | TX | CL → AWS | UN |
| 27 | Russian | ru | Cyrillic | LTR | CV (G/Az flag) | CL → AWS | UN |
| 28 | Spanish | es | Latin | LTR | TX | CL → AWS | UN |
| — | Code-mixed | hi-Latn, ta-Latn, bn-Latn, mr-Latn, kok-Latn | Roman | LTR | — | Transliterate to native script (Sarvam transliteration) → MT | Detected per message |

UI languages are a separate list (NN-23: English + Hindi at launch; 10 more by configuration). Reading and translating documents in all 28 languages does **not** mean the UI or legal templates are available in them.

### 7.2 Language identification (LID)

- Granularity: document, page, paragraph/OCR block and **per chat message**; stored as `{lang, script, confidence}`.
- Method: script classifier (Unicode block histogram) → language model (Sarvam LID for Indic; fastText-style `lid.176` self-hosted for others) → disambiguation rules (Devanagari: hi/mr/ne/sa/kok/mai/doi/brx by lexical model; Bengali script: bn/as/mni).
- Thresholds: confidence ≥ 0.90 → set; 0.60–0.90 → set with "Language uncertain — confirm" chip; < 0.60 → `und` and user selection required before MT.
- Code-mixed detection: Latin-script text with an Indic language model score ≥ 0.6 is classed `xx-Latn`; transliterated to native script before MT; the original romanised text is kept.

### 7.3 Machine translation routing

| Data class (S7 §3.9) | Allowed MT engines |
|---|---|
| D0 public content (website, help) | Any configured |
| D1 account/contact | ST, IT2, CL, AWS (ap-south-1) |
| D2 case content | ST, IT2, CL; AWS only for UN languages and only in ap-south-1 |
| D3 special (FAM, POSH, health, minors, sealed) | IT2 (self-hosted) or CL (Bedrock India) only |
| D4 KYC artefacts | No MT |

Fallback is fail-closed: if all allowed engines for the class are unavailable, the job queues (`PROVIDER_UNAVAILABLE`); it never falls through to a non-India endpoint (S7 FR-S7-LLM-09). Cache key: (source SHA-256, from, to, glossary version, engine version).

### 7.4 Legal glossary and term locks

- **Seed sources**: Legislative Department (Official Languages Wing) Legal Glossary (English–Hindi) and regional legal glossaries; Commission for Scientific and Technical Terminology lists; authoritative Hindi texts of Central Acts on India Code (Authoritative Texts (Central Laws) Act 1973); SUVAS vocabulary only with written permission of the Supreme Court (no public licence found; not relied on) **[VERIFY — open (product): licence]**.
- `core.glossary_terms`: `term_en`, `lang`, `term_target`, `source_ref`, `statute_ref`, `do_not_translate` (bool), `notes`, `status` (`proposed`/`approved`), approver (`legal_reviewer` + language reviewer).
- **Do-not-translate (lock) classes**: statute names and section citations ("Section 34", "Order XXI Rule 11"), case names and citations, forum names (NCLT, DRT, RB-IOS), party names, amounts and currency, dates, case numbers, exhibit labels, email/URLs, defined terms marked by the user.
- **Pre-process**: replace locked spans with placeholders `⟦L0001⟧`; **post-check**: every placeholder present exactly once and restored; amounts/dates re-validated; any loss → `LOCKED_TERM_MISSING` and the segment is flagged for human edit.
- Hindi terminology note: arbitration "माध्यस्थम्" and mediation "मध्यस्थता" are shown with English glosses (Appendix E open item 1).

### 7.5 Back-translation for high-stakes documents

Mandatory for: notices, settlement agreements, awards and orders rendered in a non-English language, consent forms, and any translation attached to a court export. Process: translate A→B; translate B→A with a different engine; compute semantic similarity per segment (multilingual embedding cosine, in-region) and chrF++ against the source; segments with cosine < 0.85 or chrF++ < 50 are flagged "Meaning may have changed — review"; a document passes only when every flagged segment is reviewed by a human. Results stored in `core.translation_segments.qa`.

### 7.6 Labels: convenience vs certified

| Rendition kind | Fixed label (header of every page) | Footer | Usable as |
|---|---|---|---|
| `translation_machine` | **"Translation — for convenience. Machine translation; not certified. The {language of record} version is authoritative."** | Engine(s), date, source hash prefix, back-translation status | Reading aid; never as a filed translation in a court export; may be filed in an Equator proceeding only if the tribunal/neutral directs or the parties agree |
| `translation_reviewed` | "Translation — for convenience. Reviewed by {name, role} on {date}; not certified." | Same + reviewer | Equator proceedings |
| `translation_certified` | **"Certified translation"** + certificate page (§7.7) | Translator ID, certification type, source hash | Court exports and enforcement packs |

Lint `LBL-04…LBL-06` blocks, on machine or reviewed translations, any text other than the fixed labels that contains "certified translation", "certified by", "official translation" or "sworn" (L-D-08); the fixed label ids are `lbl.translation.convenience_machine` and `lbl.translation.convenience_reviewed`.

### 7.7 Certified translation workflow

Uses `core.translation_requests` (P06 FR-P06-24; canonical name kept).

| Step | Actor | Detail | SLA |
|---|---|---|---|
| 1 Order | Party / case_manager | Source document(s), language pair, purpose (`arbitration_s22_4`, `court_filing`, `foreign_award_s47`, `nyc_art_iv`, `other`), certification type (`translator_affidavit`, `notarised`, `apostilled`, `consular`, `court_approved_translator`), deadline; quote shown with GST before payment (NN-29) | — |
| 2 Assign | System | Rotation among empanelled translators with the language pair and capacity; conflict check against case parties | 4 working hours |
| 3 Draft | Translator | Machine pre-translation offered (labelled internally); translator owns the output | Per quote (default 3 working days per 20 pages) |
| 4 QA | Second linguist (for court/enforcement purposes) | Glossary adherence, locked terms, numbers | 1 working day |
| 5 Certify | Translator | Signs certificate (eSign/DSC); notarisation/apostille/consular steps tracked as tasks (P06 `core.apostille_tasks`) | Per authority |
| 6 Deliver | System | Rendition `translation_certified` linked to source version; ledgered | — |

**Certificate of accuracy template** (component #12): translator full name, qualifications/accreditation, address, contact; languages; "I, {name}, certify that I am competent to translate from {source} into {target} and that the attached translation of {document title, pages, SHA-256 of source} is, to the best of my knowledge and belief, a true and accurate translation of the original"; date, place, signature; for affidavit type, jurat block. Forum notes printed in guidance (not in the certificate): A&C Act s.22(4) (tribunal may order translations); s.47(2) (foreign award: English translation certified by a diplomatic or consular agent of the party's country, or as otherwise sufficient under Indian law); New York Convention Art. IV(2) (official or sworn translator, or diplomatic/consular agent); Supreme Court Rules 2013 O.VIII r.3 (translator approved by the Court — Equator cannot certify for SC purposes; export flags "court-approved translator certification required"); CPC s.137 (language of subordinate courts).

### 7.8 Language of record

- `core.cases.language_of_record` (BCP-47; default `en-IN`) and `core.proceedings.language_of_record` (may differ, e.g., FAM mediation in Marathi with English settlement) — set from the arbitration agreement or by the tribunal under A&C s.22(1)–(3), by the rules of procedure for Equator-administered matters, or by agreement in mediation.
- `additional_languages[]` for parties' working languages; interpretation needs flagged to the case manager.
- Effects: (a) filings not in the language of record trigger SCR-F05; (b) orders and awards are issued in the language of record; convenience translations may accompany them with §7.6 labels; (c) the authoritative-version sentence on every translation names the language of record.

### 7.9 Font and script coverage

- Approved font pack (§5.8) installed in renderer, converter and viewer containers; CI test renders a pangram per script (all 28 languages + Meetei Mayek and Ol Chiki) and fails on any `.notdef` glyph.
- Web/mobile viewers load Noto subsets on demand; RTL layout tests for ar, ur, ks-Arab, sd-Arab, pa-Arab.
- Legacy Indic fonts (Kruti Dev, DevLys, Chanakya, Shree-Lipi legacy encodings) are detected in DOCX/PDF uploads; conversion to Unicode is offered (mapping tables per font); the converted text is a rendition and the original is kept.

---

## 8. Security, retention, evidence ledger and BSA s.63 certificate

### 8.1 Upload security

| Control | Rule |
|---|---|
| Allow-list | FR-P02-35 list; type decided by magic bytes, not extension; mismatch → `UPLOAD_TYPE_NOT_ALLOWED` |
| Malware | ClamAV (signatures hourly) + second engine for Office/PDF (commercial AV or YARA rule pack); quarantine bucket; infected → bytes destroyed, hash kept, `equator.documents.upload.quarantined.v1` |
| Active content | PDF JavaScript, launch actions, embedded files and XFA removed in the **rendition** (content disarm and reconstruction); the original is kept in WORM but never served raw to other parties — they receive the sanitised PDF rendition; Office macros stripped (rendition) and `.docm/.xlsm` rejected |
| Archives | ZIP: max 500 entries, no nesting, ratio ≤ 100:1, total uncompressed ≤ 2 GB, path traversal names rejected (`ZIP_UNSAFE`) |
| Encrypted files | Password-protected PDF/Office rejected with guidance (`FILE_ENCRYPTED_UNSUPPORTED`) |
| Images | Re-encoded for renditions (strips polyglot payloads); EXIF retained only in original |
| Size | 200 MB per file default; video ≤ 2 GB on request; per-case quota configurable |
| Aadhaar | Unmasked Aadhaar numbers detected by OCR + Verhoeff check → upload blocked (`AADHAAR_UNMASKED_DETECTED`, NN-14) with a masking tool offered |
| Legacy font | §7.9 |

### 8.2 Encryption and keys

- In transit: TLS 1.2+ (TLS 1.3 preferred); HSTS; pre-signed URLs ≤ 15 minutes, single object, IP-bound where the CDN supports it.
- At rest: SSE-KMS with a **per-tenant CMK** per bucket class (evidence, derived); sealed buckets use separate CMKs per sealed schema, with key policies limited to `eq_posh`/`eq_health`/`eq_safety` service roles; BYOK option for enterprise tenants (master §4.1).
- Field-level: OCR text, type-copy text and translations of `high`/`sealed` documents are encrypted objects referenced by `*_ref` (never inline in Postgres); search excerpts for `high` tier are short (≤ 160 chars) highlights.
- Key rotation yearly (automatic); crypto-shredding used for sealed arb-med awards (P06 FR-P06-11) and for erasure where WORM retention has expired.

### 8.3 Retention and legal hold

§1.14–§1.15 apply. CERT-In Directions of 28 April 2022: ICT system logs retained 180 days in India (platform policy: 400 days immutable, S8 S8-FR-43).

### 8.4 Evidence ledger

Appendix F `core.evidence_ledger` (X-11) is the single ledger. Artefact types added by this appendix: `document_version`, `rendition_certified_translation`, `rendition_type_copy_verified`, `redacted_rendition_published`, `court_export`, `bundle_manifest`, `esign_signed_pdf`, `esign_audit_trail`, `wa_export_zip`, `bsa63_certificate`, `secure_link_disclosure`. Verification: `POST /v1/cases/{caseId}/evidence-ledger/verify` recomputes the chain; daily anchor to the audit chain (FR-P02-41).

### 8.5 BSA 2023 s.63 certificate auto-generation

**Law.** BSA 2023 (in force 1 July 2024) s.61 (electronic record not inadmissible merely because electronic), s.62 (contents of electronic records proved under s.63), s.63(1)–(2) (computer output deemed a document if conditions met), **s.63(4)** (certificate in the form in the **Schedule**, signed by the person in charge of the device or management of the relevant activities **and** by an expert, stating hash value(s) and algorithm). The predecessor certificate under Indian Evidence Act s.65B(4) was held mandatory in *Arjun Panditrao Khotkar v Kailash Kushanrao Gorantyal* (2020) 7 SCC 1. Arbitral tribunals are not bound by the evidence statute (A&C s.19(1)), but certificates are needed if the material reaches a court (ss.34, 36, 37) (S7 §3.7).

**Part A (party / person in charge) — auto-filled fields** (`core.bsa63_certificates.part_a jsonb`): deponent name, parentage/spouse, address, capacity; record description (file names, types, sizes, date range, source app); device/source type (computer/storage media, DVR, mobile phone, flash drive, CD/DVD, server, cloud, other), make, model, colour, serial number, IMEI/UIN/UID/MAC/cloud ID (user-entered; IMEI masked in party view); the statements that the device was under lawful control, regularly used, working properly (or that any malfunction did not affect the record), and owned/maintained/managed/operated by the deponent (select); **hash table**: file name · SHA-256 (and SHA-512 optional) · size · computed at (UTC) · computed by "Equator Resolution platform v{x}"; place, date, signature (Aadhaar eSign/DSC). Field names follow the Schedule form **[VERIFY — open: check every field label against the Gazette text of the BSA Schedule before activation; legal_reviewer sign-off]**.

**Part B (expert)**: expert name, qualification, designation, organisation, details of examination (method of extraction verified, hash re-computation result, tool and version), statement of opinion that the record is as produced, hash table, signature. Routed to an empanelled expert; preference for an Examiner of Electronic Evidence notified under IT Act 2000 s.79A; qualifying criteria for "expert" remain a counsel question (S7 §7 Q9).

**Platform-generated records** (hearing recordings where lawful, e-filed documents, notices, signed instruments): Part A by Equator's designated officer (`registrar` with custodian role) as the person in charge of the platform — subject to counsel confirmation (S7 §7 Q10).

**Generation rules**: generated on upload of any `evidence_upload_type` that is an electronic record, on bundle certification and on court export; re-hash at every export and compare with ledger (`HASH_MISMATCH_CRITICAL` incident on difference); arbitration procedural order template states that certificates are not required for admissibility in the arbitration but parties are encouraged to sign Part A for later court use (S7 FR-S7-BSA-05); POSH inquiries use the same integrity pipeline without the certificate requirement (FR-S7-BSA-06).

---

## 9. Data model, APIs, events, errors and configuration

### 9.1 Tables (additive to Appendix F; all `tenant_id` + RLS via `rls.enable_case_rls` unless noted; `std_cols` implied)

```sql
-- additive columns
ALTER TABLE core.documents ADD COLUMN folder_code text NOT NULL DEFAULT 'COR'
  CHECK (folder_code IN ('PLD','ANX','EVD','NTC','ORD','OUT','COR','INT','BND','DRF')),
  ADD COLUMN folder_id uuid, ADD COLUMN owner_case_party_id uuid,
  ADD COLUMN visibility_state text NOT NULL DEFAULT 'PRIVATE_DRAFT'
  CHECK (visibility_state IN ('PRIVATE_DRAFT','FILED','RETURNED','ON_RECORD','SERVED','SUPERSEDED','WITHDRAWN','ISSUED','SET_ASIDE')),
  ADD COLUMN doc_kind text, ADD COLUMN document_date date, ADD COLUMN language_codes text[], ADD COLUMN scripts text[],
  ADD COLUMN evidence_upload_type text, ADD COLUMN source_capture jsonb, ADD COLUMN tamper_hint jsonb, ADD COLUMN ai_disclosure jsonb,
  ADD COLUMN tags text[] NOT NULL DEFAULT '{}';
CREATE TABLE core.document_folders (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  code text NOT NULL, parent_id uuid REFERENCES core.document_folders(id), name text NOT NULL CHECK (length(name) <= 80),
  owner_case_party_id uuid, depth int NOT NULL CHECK (depth BETWEEN 0 AND 3));
CREATE TABLE core.document_renditions (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid,
  document_id uuid NOT NULL REFERENCES core.documents(id), derived_from_version_id uuid NOT NULL REFERENCES core.document_versions(id),
  kind text NOT NULL CHECK (kind IN ('pdf_conversion','thumbnail','ocr_text','ocr_layout_json','searchable_pdf','type_copy',
    'translation_machine','translation_reviewed','translation_certified','redacted','court_export','watermarked_download','transcript')),
  s3_bucket text NOT NULL, s3_key text NOT NULL, sha256 char(64) NOT NULL, label text NOT NULL,       -- NN-32 fixed label id (i18n key), e.g. lbl.type_copy
  engine jsonb NOT NULL,                       -- [{provider, model_id, region, version_date}]
  confidence_summary jsonb, status text NOT NULL, verified_by uuid, verified_at timestamptz, attestation_document_id uuid,
  language_from text, language_to text, render_profile_version_id uuid, expires_at timestamptz,
  CHECK (kind <> 'translation_certified' OR attestation_document_id IS NOT NULL),
  CHECK (kind NOT IN ('translation_machine','translation_reviewed')
         OR label IN ('lbl.translation.convenience_machine','lbl.translation.convenience_reviewed')));   -- L-D-08
CREATE TABLE core.document_shares (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  document_id uuid NOT NULL REFERENCES core.documents(id), audience_key text NOT NULL, granted_by uuid NOT NULL,
  mechanism_at_grant text NOT NULL, granted_at timestamptz NOT NULL DEFAULT now(), revoked_at timestamptz,
  UNIQUE (document_id, audience_key));
REVOKE UPDATE ON core.document_shares FROM eq_app;   -- revocation only via documents.revoke_share() which refuses SERVED narrowing
CREATE TABLE core.share_requests (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  requester_case_party_id uuid, target_case_party_id uuid NOT NULL, direction_order_id uuid, items jsonb NOT NULL,
  due_at timestamptz NOT NULL, status text NOT NULL CHECK (status IN ('open','fulfilled','partly_fulfilled','declined','lapsed')));
CREATE TABLE core.secure_links (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  token_sha256 char(64) NOT NULL UNIQUE, document_ids uuid[] NOT NULL, purpose text NOT NULL, recipient jsonb NOT NULL,
  permission text NOT NULL CHECK (permission IN ('view_only','download')), max_opens int NOT NULL DEFAULT 20, max_downloads int NOT NULL DEFAULT 3,
  opens int NOT NULL DEFAULT 0, downloads int NOT NULL DEFAULT 0, country_allow text[] NOT NULL DEFAULT '{IN}',
  expires_at timestamptz NOT NULL, revoked_at timestamptz, created_by uuid NOT NULL, created_at timestamptz NOT NULL DEFAULT now(),
  CHECK (expires_at <= created_at + interval '90 days'));
CREATE TABLE core.disclosures (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  purpose_code text NOT NULL CHECK (purpose_code IN ('ENFORCEMENT','REGISTRATION','BANK_NOC','COURT_FILING','REGULATOR','PARTY_COUNSEL','PUBLICATION','EXPERT','INTERPRETER','TRANSLATOR','BANK_ESCROW','SUB_REGISTRAR')),
  -- secure-link purposes (§2.6) map: EXPERT_REVIEW→EXPERT, EXECUTING_OFFICER→ENFORCEMENT, COURT_FILING_SUPPORT→COURT_FILING, PARTY_ADVISER→PARTY_COUNSEL; others identical; REGISTRATION and BANK_NOC are App. R §5 OVC purposes
  document_ids uuid[] NOT NULL, recipient jsonb NOT NULL, legal_basis text NOT NULL, secure_link_id uuid, disclosed_at timestamptz NOT NULL);  -- append-only
CREATE TABLE core.document_annotations (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  document_version_id uuid NOT NULL, author_user_id uuid NOT NULL, audience text NOT NULL CHECK (audience IN ('private','my_side','tribunal','registry')),
  body jsonb NOT NULL);                                                 -- W3C Web Annotation
CREATE TABLE core.redaction_jobs (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  source_version_id uuid NOT NULL, items jsonb NOT NULL, maker uuid NOT NULL, checker uuid, output_rendition_id uuid,
  status text NOT NULL CHECK (status IN ('draft','in_review','verified','failed')), CHECK (checker IS NULL OR checker <> maker));
CREATE TABLE core.legal_holds (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, scope text NOT NULL, scope_ref uuid NOT NULL,
  reason_code text NOT NULL, set_by uuid NOT NULL, released_by uuid, released_at timestamptz, CHECK (released_by IS NULL OR released_by <> set_by));
CREATE TABLE core.saved_views (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, owner_user_id uuid, team_id uuid,
  surface text NOT NULL, filters jsonb NOT NULL, sort jsonb, columns jsonb);                     -- tenant RLS only
-- v3.1: Appendix AG §AG.10.1 adds pinned, is_default, shared_scope ('me','team','department','tenant','company'), view_code -> cfg.view_definitions;
--       the AG §AG.5.6 saved-view contract (allow-listed filters, sealed fields rejected, viewer permissions re-applied) governs all surfaces
CREATE TABLE core.neutral_packets (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  proceeding_id uuid NOT NULL, version int NOT NULL, items jsonb NOT NULL, cover_memo_document_id uuid, UNIQUE (proceeding_id, version));
CREATE TABLE core.render_profiles (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, code text NOT NULL, forum text NOT NULL,
  status text NOT NULL CHECK (status IN ('draft','in_review','verified','unverified_published','superseded')));   -- tenant_id NULL = platform
CREATE TABLE core.render_profile_versions (id uuid PRIMARY KEY DEFAULT uuidv7(), profile_id uuid NOT NULL REFERENCES core.render_profiles(id),
  version int NOT NULL, tokens jsonb NOT NULL, component_order text[] NOT NULL, source_ref text, verified_by uuid, verified_on date,
  maker uuid NOT NULL, checker uuid, CHECK (checker IS NULL OR checker <> maker), UNIQUE (profile_id, version));
CREATE TABLE core.court_documents (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  owner_case_party_id uuid, render_profile_version_id uuid NOT NULL, ast jsonb NOT NULL, status text NOT NULL
  CHECK (status IN ('draft','validated','rendered','exported','filed')), docx_rendition_id uuid, pdf_rendition_ids uuid[]);
CREATE TABLE core.annexure_maps (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, court_document_id uuid NOT NULL,
  court_label text NOT NULL, source_document_version_id uuid NOT NULL, arbitral_label text, kind text NOT NULL
  CHECK (kind IN ('original','type_copy','translation','certificate')), page_from int, page_to int, UNIQUE (court_document_id, court_label, kind));
CREATE TABLE core.wa_chat_imports (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  document_id uuid NOT NULL, variant text NOT NULL, date_order text CHECK (date_order IN ('DMY','MDY')), timezone text NOT NULL DEFAULT 'Asia/Kolkata',
  message_count int, media_linked int, media_omitted int, earliest_ts timestamptz, cap_warning boolean, sender_map jsonb,
  counter_import_id uuid, diff_report_ref text, joint_authenticity text CHECK (joint_authenticity IN ('none','requested','confirmed','refused')));
CREATE TABLE core.wa_messages (import_id uuid NOT NULL REFERENCES core.wa_chat_imports(id), seq int NOT NULL, tenant_id uuid NOT NULL,
  case_id uuid NOT NULL, ts_local timestamp, ts_utc timestamptz, sender_raw_enc bytea, sender_case_party_id uuid,
  type text NOT NULL CHECK (type IN ('text','media','system','deleted','call','edited')), text_ref text, media_document_id uuid,
  forwarded boolean NOT NULL DEFAULT false, edited boolean NOT NULL DEFAULT false, source_line_no int NOT NULL, lang text, script text,
  lid_confidence numeric(4,3), text_sha256 char(64), PRIMARY KEY (import_id, seq));
CREATE TABLE core.ocr_jobs (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, document_version_id uuid NOT NULL,
  route jsonb NOT NULL, engines text[] NOT NULL, data_class text NOT NULL CHECK (data_class IN ('D0','D1','D2','D3','D4')),
  status text NOT NULL, page_results_ref text, cost_minor bigint, currency char(3) DEFAULT 'INR');
CREATE TABLE core.type_copies (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  rendition_id uuid NOT NULL REFERENCES core.document_renditions(id), source_version_id uuid NOT NULL,
  status text NOT NULL CHECK (status IN ('machine_draft','user_corrected','verified','disputed','superseded')),
  low_lines_open int NOT NULL DEFAULT 0, verifier_kind text CHECK (verifier_kind IN ('uploader','independent','advocate')),
  CHECK (status <> 'verified' OR low_lines_open = 0));                                     -- L-D-09
CREATE TABLE core.translations (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid,
  rendition_id uuid NOT NULL REFERENCES core.document_renditions(id), source_version_id uuid NOT NULL, lang_from text NOT NULL, lang_to text NOT NULL,
  glossary_version_id uuid, back_translation_status text CHECK (back_translation_status IN ('not_required','pending','passed','flagged','reviewed')),
  translation_request_id uuid);                                                            -- certified → core.translation_requests (P06)
CREATE TABLE core.translation_segments (translation_id uuid NOT NULL, seq int NOT NULL, tenant_id uuid NOT NULL, source_ref text,
  target_ref text, locks jsonb, qa jsonb, human_edited boolean NOT NULL DEFAULT false, PRIMARY KEY (translation_id, seq));
CREATE TABLE core.glossaries (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, lang text NOT NULL, version int NOT NULL, status text NOT NULL);
CREATE TABLE core.glossary_terms (id uuid PRIMARY KEY DEFAULT uuidv7(), glossary_id uuid NOT NULL REFERENCES core.glossaries(id),
  term_en text NOT NULL, term_target text, do_not_translate boolean NOT NULL DEFAULT false, source_ref text NOT NULL, statute_ref text, notes text);
CREATE TABLE core.languages (code text PRIMARY KEY, name_en text NOT NULL, scripts text[] NOT NULL, direction text NOT NULL,
  eighth_schedule boolean NOT NULL, un_official boolean NOT NULL, code_mixed boolean NOT NULL DEFAULT false,
  ocr_route jsonb NOT NULL, mt_route jsonb NOT NULL, font_family text NOT NULL);           -- platform table, no RLS
CREATE TABLE core.bsa63_certificates (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL,
  scope text NOT NULL CHECK (scope IN ('document','bundle','court_export')), scope_ref uuid NOT NULL, hash_table jsonb NOT NULL,
  part_a jsonb NOT NULL, part_a_document_id uuid, part_a_signed_at timestamptz, part_b jsonb, part_b_document_id uuid, expert_neutral_id uuid,
  status text NOT NULL CHECK (status IN ('draft','part_a_signed','part_b_requested','complete','superseded')));
```

`core.translation_requests` and `core.apostille_tasks` remain as defined in P06 (FR-P06-24); add `purpose`, `certification_type`, `translator_id`, `output_rendition_id`.

### 9.2 APIs (`/v1`; OpenAPI 3.1; idempotency `I` on creates)

| Method and path | Purpose | Roles | |
|---|---|---|---|
| GET `/cases/{caseId}/folders` · POST `/cases/{caseId}/folders` | Folder tree; create sub-folder | members; owner side / registry | I |
| GET `/cases/{caseId}/documents?filter…&view={savedViewId}` | List with filters (§1.7), cursor pagination | ABAC | — |
| POST `/documents/{id}/file` | File a draft (share dialog payload: audience, declaration) | owner side | I |
| POST `/documents/{id}/scrutiny` | Accept / return with defect codes | case_manager | I |
| POST `/documents/{id}/shares` · DELETE `/documents/{id}/shares/{shareId}` | Add audience; revoke (refused after service) | owner side / registry | I |
| POST `/cases/{caseId}/share-requests` · POST `/share-requests/{id}/respond` | Request / respond | parties, neutral (direction) | I |
| POST `/cases/{caseId}/secure-links` · POST `/secure-links/{id}/revoke` · GET `/s/{token}` (public, OTP) | External sharing | owner side, registry | I |
| GET `/documents/{id}/activity` | Access and history panel | ABAC (role-shaped) | — |
| GET `/documents/{id}/preview?page=` | Rendered page tiles / text | ABAC | — |
| POST `/documents/{id}/annotations` · GET … | Annotations | members | — |
| POST `/documents/{id}/redactions` · POST `/redaction-jobs/{id}/approve` | Redaction maker / checker | party, case_manager / case_counsel, quality_officer | I |
| POST `/legal-holds` · POST `/legal-holds/{id}/release` | Hold set / release (dual) | registrar, dpo, legal_reviewer | I |
| POST `/documents/bulk` | Bulk actions (§1.8) → workflow id | per action | I |
| GET `/search/documents?q=` | Full-text search with ACL filter | members | — |
| POST `/documents/{id}/ocr` | (Re)run OCR | case_manager | I |
| POST `/documents/{id}/type-copies` · PATCH `/type-copies/{id}` · POST `/type-copies/{id}/attest` · POST `/type-copies/{id}/dispute` | Type-copy lifecycle | owner side; verifier; other party | I |
| POST `/cases/{caseId}/whatsapp-imports` · POST `/whatsapp-imports/{id}/resolve` (date order, sender map) · POST `/whatsapp-imports/{id}/joint-authenticity` · POST `/whatsapp-imports/{id}/diff` | WhatsApp pipeline | owner side; other party | I |
| POST `/documents/{id}/translations` (machine) · POST `/translations/{id}/review` | Convenience translation | members (own/served docs) | I |
| POST `/cases/{caseId}/translation-requests` · POST `/translation-requests/{id}/certify` | Certified translation | party, case_manager; translator | I |
| GET `/glossaries` · POST `/glossaries/{id}/terms` | Glossary | legal_reviewer (write) | I |
| GET `/render-profiles` · POST `/render-profiles/{id}/versions` · POST `/render-profile-versions/{id}/verify` | Profiles (maker–checker) | legal_reviewer, institution_admin | I |
| POST `/cases/{caseId}/court-documents` · PUT `/court-documents/{id}/ast` · POST `/court-documents/{id}/render` · POST `/court-documents/{id}/export` | Court Document Builder | owner side | I |
| POST `/cases/{caseId}/bundles` (types §3.6) · POST `/bundles/{id}/approve-index` · POST `/bundles/{id}:certify` | Bundles | case_manager, parties, neutral | I |
| POST `/cases/{caseId}/certificates/bsa-63` · POST `/bsa63/{id}/sign-part-a` · POST `/bsa63/{id}/request-part-b` | s.63 certificates | owner side, registrar; expert | I |
| POST `/documents/{id}/sign-requests` | Create eSign request (§4) | owner side, case_manager | I |
| GET `/verify/{hash}` (public) | Hash verification | public | — |

### 9.3 Domain events (`equator.documents.*.v1` unless stated; payloads IDs and codes only)

`folder.created` · `document.uploaded` (existing) · `document.filed` · `document.returned` · `document.accepted_on_record` · `document.served` (W, metadata only, never for `sealed`) · `document.withdrawn` · `document.superseded` · `share.granted` · `share.revoked` · `share_request.opened` · `share_request.responded` · `share_request.lapsed` · `secure_link.created` · `secure_link.opened` · `secure_link.revoked` · `disclosure.recorded` · `annotation.created` (count only, no body) · `redaction.verified` · `redaction.failed` · `legal_hold.set` / `.released` (existing) · `ocr.completed` (with `confidence_summary` bands) · `ocr.low_confidence_detected` · `type_copy.created` · `type_copy.attested` · `type_copy.disputed` · `wa_import.parsed` · `wa_import.locale_ambiguous` · `wa_import.diff_generated` · `wa_import.joint_authenticity_confirmed` · `translation.machine_completed` · `translation.back_translation_flagged` · `translation.certified` · `court_document.rendered` · `court_document.exported` · `render_profile.verified` · `bundle.generated` (existing) · `bundle.index_approved` · `bundle.certified` (existing) · `bsa63.part_a_signed` · `bsa63.part_b_completed` · `upload.quarantined` (existing) · `equator.proceedings.neutral_packet.updated.v1` · `equator.proceedings.order.served.v1` · *(v3.1)* `batch.filed` (batch ID, counts) · `review_set.created` / `.produced` (own-side consumers only; no content) · `scrutiny.batch_accepted`.

Consumers: AUD (all), SRCH (filed/accepted/served/ocr/type_copy/translation — non-sealed), NOT (filed, returned, served, share_request, secure_link, type_copy.disputed, translation.certified), CLK (share_request due, defect cure, original-affidavit reminder), BIL (type copy, translation, certified translation, Part B expert fees), RPT (counts only).

### 9.4 Errors (Appendix F.10 format; new codes to be registered in F.10 per X-20)

| Code | HTTP | Message (en) | Basis |
|---|---|---|---|
| `DOC_VISIBILITY_DOWNGRADE_FORBIDDEN` | 409 | A served document cannot be hidden from parties who received it. | §2.1 |
| `DOC_SERVICE_REQUIRED_ARBITRATION` | 422 | In arbitration, documents filed with the tribunal are shared with all parties. | A&C s.24(3); L-D-03 |
| `DOC_PRIVILEGED_SHARE_BLOCKED` | 409 | Remove the privilege flag before sharing this document. | §2.4 |
| `DOC_PUBLIC_VIA_PUBLICATION_ONLY` | 403 | Documents can be published only through the publication process. | NN-26 |
| `SECURE_LINK_EXPIRED` | 410 | This link has expired or was revoked. | §2.6 |
| `SECURE_LINK_SEALED_FORBIDDEN` | 403 | Sealed documents cannot be shared by link. | NN-07 |
| `LEGAL_HOLD_ACTIVE` | 409 | This record is under legal hold. | §1.14 |
| `REDACTION_INCOMPLETE` | 422 | Redacted text is still present in the output. | §1.11 |
| `RENDER_PROFILE_UNVERIFIED` | 409 (warning code on export) | This layout has not been verified for {forum}. | L-D-05 |
| `RENDER_PROFILE_LOCKED_TOKEN` | 422 | This court layout setting cannot be changed. | §5.7 |
| `COURT_EXPORT_UNTRANSLATED_ANNEXURE` | 422 | Annexure {n} needs a translation into {language}. | SC Rules 2013 O.VIII r.2 |
| `COURT_EXPORT_UNRESOLVED_REFERENCE` | 422 | Some page references could not be resolved. | §5.4 |
| `COURT_EXPORT_VALIDATION_FAILED` | 500→retry | The PDF failed PDF/A validation. | §5.6 |
| `TYPE_COPY_UNVERIFIED` | 409 (confirmable) | This type copy has not been verified. | NN-32 |
| `TYPE_COPY_LOW_LINES_OPEN` | 422 | Review all uncertain lines before submitting. | L-D-09 |
| `WA_LOCALE_AMBIGUOUS` | 409 | Tell us how dates are written in this chat. | §6.2 |
| `WA_EXPORT_UNRECOGNISED` | 422 | This file does not look like a WhatsApp export. | §6.2 |
| `TRANSLATION_NOT_CERTIFIED` | 422 | A certified translation is required here. | §7.6 |
| `LOCKED_TERM_MISSING` | 422 | A protected term was lost in translation; please review. | §7.4 |
| `MT_ROUTE_UNAVAILABLE` | 503 | Translation is queued; no permitted engine is available. | §7.3 (sub-code of canonical `PROVIDER_UNAVAILABLE`) |
| `OCR_ROUTE_RESIDENCY_BLOCKED` | 403 | This engine is not permitted for this document. | L-D-06 |
| `AFFIDAVIT_REQUIRES_OATH` | 422 | Affidavits must be sworn before a notary or oath commissioner. | L-D-12 |
| `ESTAMP_REQUIRED_BEFORE_SIGNING` | 409 | Attach the e-stamp before sending for signature. | NN-09 (sub-code of canonical `ESTAMP_REQUIRED`) |
| `ZIP_UNSAFE` | 422 | This ZIP file cannot be processed safely. | §8.1 |
| `FILE_ENCRYPTED_UNSUPPORTED` | 422 | Remove the password and upload again. | §8.1 |
| `LEGACY_FONT_DETECTED` | 409 (confirmable) | This file uses a non-Unicode font; convert it? | §7.9 |
| `TAG_SENSITIVE_TERM` | 422 | Tags cannot contain sensitive information. | §1.5 |
| `HASH_MISMATCH_CRITICAL` | 500 + incident | Integrity check failed; the registry has been alerted. | NN-10, NN-22 |
| `DOC_DUPLICATE_IN_CASE` *(v3.1)* | 409 | This file is already in the case as {label}. | §1.8 |
| `SCRUTINY_BATCH_NOT_ELIGIBLE` *(v3.1)* | 422 | Only procedural filings with no warnings can be accepted together. (`document_ids`) | §3.2 |

Existing codes reused: `ESIGN_EXCLUDED_INSTRUMENT`, `BUNDLE_CERTIFICATE_MISSING`, `UPLOAD_TYPE_NOT_ALLOWED`, `UPLOAD_QUARANTINED`, `AADHAAR_UNMASKED_DETECTED`, `PROVIDER_UNAVAILABLE`.

### 9.5 Feature flags and configuration keys

Tiers per NN-33 and Appendix V §V.1; unprefixed keys are aliases of scoped canonical keys (X-44); "T≤L" = tighten only below a locked ceiling. *(v3.1: tier and approver columns added)*

| Key | Default | Tier | Who / approval | Notes |
|---|---|---|---|---|
| `dms.secure_links.enabled` | ON | T | tenant admin | Per tenant |
| `dms.secure_links.max_days` | 30 (90 for `EXECUTING_OFFICER`) | T≤L | tenant admin | Tighten only; DB CHECK 90 days |
| `dms.caucus_share.enabled` | ON (mediation/conciliation only) | T (L for arbitration: never) | tenant admin | Cannot be enabled for arbitration (L-D-03) |
| `dms.annotations.shared_my_side` | ON | T | tenant admin | — |
| `dms.view_only_tiles_dpi` | 150 | T (100–300) | tenant admin | — |
| `dms.drafts_retention_days_after_closure` | 90 | T≥G | tenant DPO | Retention floor per Appendix Q |
| `tenant.dms.bulk_upload.max_files` *(v3.1)* | 200 | T≤L | tenant admin | §1.8; ceiling 200 |
| `tenant.dms.review_sets.enabled` / `.qc_sample_percent` *(v3.1)* | ON / 10 | T (5–25) | tenant admin | §1.16 |
| `tenant.dms.scrutiny.batch_accept_max` *(v3.1)* | 50 | T≤L | case lead | §3.2; procedural filings only (L) |
| `ocr.regional_cloud.enabled` | **OFF** | G (platform) | CTO + DPO; ADR + DPA + region pin required | L-D-06 |
| `ocr.agreement_thresholds` | `{high: 0.03, medium: 0.10}` CER | T≤L | tenant admin | Tighten only |
| `typecopy.independent_verifier.enabled` | ON | T | tenant admin | Roster in P03 |
| `typecopy.handwriting.auto_accept` | **false** | L | — | L-D-09; not configurable |
| `wa.parser.counter_diff.enabled` | ON | T | tenant admin | — |
| `mt.engines.order` | per §7.1 | G | DPO (residency) | Per language; only engines allowed for the data class (§7.3) |
| `mt.cloud_un_languages.enabled` | OFF until AWS ap-south-1 coverage verified | G (platform) | CTO | §7.1 |
| `mt.back_translation.threshold` | `{cosine: 0.85, chrf: 50}` | T≥L | tenant admin | Raise only |
| `translation.certified.marketplace.enabled` | ON | T | tenant admin | Translator roster |
| `court.profiles.custom.enabled` | ON (labelled "Custom layout") | T | tenant admin | Label locked (L) |
| `court.sc_efiling.verified` | **OFF** | G (legal flag) | `legal_reviewer` | Turn ON only after `SC_EFILING` profile verification |
| `court.ai_disclosure_stamp.enabled` | ON (mandatory when AI used) | L | — | Not tenant-disableable |
| `bsa63.part_a.auto_generate` | ON | T | tenant admin | — |
| `bsa63.platform_custodian.enabled` | OFF until counsel answers S7 Q10 | G (legal flag) | Head of Legal | §8.5 |

---

## 10. Acceptance tests (Gherkin; `tests/acceptance/dms_l/*.feature`)

```gherkin
Feature: Appendix L — DMS, court formats, type copies and translation

  Scenario: L-AT-01 Drafts stay private until filed
    Given claimant Asha Verma uploads "Ledger_2024.pdf" to her drafts in case EQ/COM/DEL/2027/00042
    When the respondent's counsel and the appointed arbitrator search for "Ledger"
    Then neither receives a result
    And OpenSearch contains no document for that upload

  Scenario: L-AT-02 Arbitration filings are served on all parties (A&C s.24(3))
    Given an arbitration proceeding with two respondents
    When the claimant files a rejoinder and selects audience "tribunal only"
    Then the API returns 422 DOC_SERVICE_REQUIRED_ARBITRATION
    And the share dialog offers only "File with the tribunal and serve on all parties"

  Scenario: L-AT-03 Caucus share in conciliation never reaches arbitration
    Given a Part III conciliation where the respondent shares "Cashflow.xlsx" with the conciliator only
    And the conciliation fails and an arbitration starts on the same case
    When the tribunal's neutral packet is generated
    Then "Cashflow.xlsx" is absent and carries privilege "caucus_derived"

  Scenario: L-AT-04 Served documents cannot be narrowed
    Given a statement of defence in state SERVED to all parties
    When the respondent tries to revoke the claimant's audience
    Then the API returns 409 DOC_VISIBILITY_DOWNGRADE_FORBIDDEN

  Scenario: L-AT-05 Secure link expiry and revocation
    Given a secure link for an executing officer created with expiry 7 days
    When the registrar revokes it
    Then GET /s/{token} returns 410 SECURE_LINK_EXPIRED within 60 seconds
    And a disclosure row with purpose ENFORCEMENT exists for the original creation

  Scenario: L-AT-06 SC_2020 profile renders the circular's parameters
    Given a statement of claim AST rendered with profile SC_2020_PRINT
    When the PDF is inspected
    Then page size is 210 x 297 mm, margins are 40 mm left and right and 20 mm top and bottom
    And body text is Times New Roman 14 pt with 1.5 line spacing
    And block quotations are 12 pt single-spaced
    And veraPDF reports PDF/A-2b conformance and every font is embedded

  Scenario: L-AT-07 Court export obeys e-filing prohibitions and size limits
    Given a paper book of 63 MB under profile HC_TS_EFILING_2020
    When it is exported
    Then it is split into parts of at most 20 MB at bookmark boundaries
    And no part contains a watermark, password, annotation or JavaScript
    And every filename has at most 45 characters and no banned characters

  Scenario: L-AT-08 Untranslated vernacular annexure blocks a Supreme Court export
    Given Annexure P-4 is a Marathi letter with only a machine translation
    When the user exports with profile SC_2020_PRINT
    Then the export fails with COURT_EXPORT_UNTRANSLATED_ANNEXURE
    And the message states that a court-approved translator certification is required

  Scenario: L-AT-09 NN-32_type_copy_labelled_and_linked_to_original (v3.1 test name)
    Given a handwritten Hindi receipt is uploaded
    When a type copy is generated
    Then the rendition header reads "TYPE COPY" with status "Machine transcription — not verified"
    And the original version's SHA-256 is unchanged and referenced in the footer
    And the type copy status cannot become "verified" while any low-confidence line is open

  Scenario: L-AT-10 Handwriting is never auto-accepted
    Given both OCR engines agree on every line of a handwritten English note with CER 0.5%
    Then the type copy remains "machine_draft" until a human attestation is recorded

  Scenario: L-AT-11 WhatsApp locale ambiguity is asked, never guessed
    Given an Android export whose dates never exceed 12 in either position
    When the import is parsed
    Then the import pauses with WA_LOCALE_AMBIGUOUS
    And the uploader is asked "Is 03/04/24 the 3rd of April or March 4th?"

  Scenario: L-AT-12 WhatsApp iOS export with media and cap warning
    Given an iOS ZIP with "_chat.txt", 3 attached photos and 2 "image omitted" lines
    And the dispute start date entered is earlier than the first exported message
    When the import completes
    Then 3 media documents are linked with their own hashes and 2 omissions are reported
    And the 40,000-message cap warning is shown

  Scenario: L-AT-13 Counter-export diff surfaces missing messages as a signal
    Given claimant and respondent exports of the same chat where message 1,284 exists only in the claimant's export
    When the diff runs
    Then the neutral sees message 1,284 listed as "present in one export only"
    And no finding of fabrication is recorded

  Scenario: L-AT-14 Machine translation label and term locks
    Given a Tamil notice containing "Section 34" and "₹3,50,000"
    When it is machine-translated into English
    Then both strings appear unchanged in the output
    And each page carries "Translation — for convenience. Machine translation; not certified."

  Scenario: L-AT-15 Certified translation requires a certificate
    Given a translation request for a foreign award under purpose "foreign_award_s47"
    When the translator delivers without a signed certificate
    Then the rendition cannot be created as "translation_certified"

  Scenario: L-AT-16 Residency guard on OCR routing
    Given ocr.regional_cloud.enabled is OFF
    When a handwritten Bengali page in a FAM case is processed
    Then only Claude vision (Bedrock India) and Sarvam Vision are called
    And any attempt to call Google Document AI fails with OCR_ROUTE_RESIDENCY_BLOCKED

  Scenario: L-AT-17 NN-08 excluded instrument cannot be e-signed
    Given a settlement term transferring a flat in Jaipur
    When a sign request is created for the operative deed
    Then the API returns ESIGN_EXCLUDED_INSTRUMENT and a registration task is proposed

  Scenario: L-AT-18 Affidavit needs a sworn copy
    Given an affidavit approved by e-sign "Approved for swearing"
    When the party files it without uploading a sworn copy
    Then filing fails with AFFIDAVIT_REQUIRES_OATH

  Scenario: L-AT-19 NN-10 bundle certification
    Given a hearing bundle without a signed s.63 Part A
    When the case manager certifies it
    Then the API returns 409 BUNDLE_CERTIFICATE_MISSING

  Scenario: L-AT-20 True redaction
    Given a redaction of PAN "ABCDE1234F" on page 3 approved by maker and checker
    When text is extracted from the redacted rendition
    Then "ABCDE1234F" is not found and document metadata contains no author or XMP fields

  Scenario: L-AT-21 Legal hold blocks erasure
    Given a case under legal hold LITIGATION_PENDING
    When a DPDP erasure request for the claimant's uploads is processed
    Then no object is deleted and the response cites retention required by law with a review date

  Scenario: L-AT-22 Search respects audience keys
    Given the respondent's private draft and the claimant's served pleading both contain "invoice 774"
    When the claimant searches "invoice 774"
    Then only the served pleading is returned

  Scenario: L-AT-23 NN-26 no public action in DMS
    Given a registrar opens an issued award in the DMS
    Then no "make public" action exists
    And POST /documents/{id}/shares with audience PUBLIC returns 403 DOC_PUBLIC_VIA_PUBLICATION_ONLY

  Scenario: L-AT-24 Unicode font coverage
    Given the approved font pack
    When the CI renders pangrams in all 28 languages including Ol Chiki and Meetei Mayek
    Then no glyph renders as .notdef

  # v3.1 additions (§1.8, §1.16, §3.2)
  Scenario: L-AT-25 Bulk upload blocks exact duplicates and retries only failures
    Given 40 files are dropped into a case, one of which has the same SHA-256 as filed exhibit C-4 and one of which fails the malware scan
    When the user files the batch
    Then the duplicate row shows "Already filed as C-4" with DOC_DUPLICATE_IN_CASE and is not filed
    And the infected file stays out of the case with its reason
    And "Retry failed" re-processes only the failed rows

  Scenario: L-AT-26 Review sets are invisible outside the side
    Given the respondent's side has a review set with 120 coded documents
    When the claimant, the arbitrator and the case manager search or list documents
    Then no review-set codes, notes or AI suggestions are returned to them

  Scenario: L-AT-27 Scrutiny queue order and batch accept
    Given a statement of defence due under a tribunal order in 2 days and an application for time filed earlier
    Then the statement of defence is above the application in the scrutiny queue
    When the case manager batch-accepts a selection that includes the statement of defence
    Then the API returns 422 SCRUTINY_BATCH_NOT_ELIGIBLE and nothing in the selection is accepted

  Scenario: L-AT-28 ZIP download names fit Windows and SharePoint limits
    Given a case with 300 documents including long Hindi titles
    When a party downloads them as a ZIP
    Then every path below the root folder is at most 140 ASCII characters and the manifest lists original and shortened names
```

---

## 11. Open items and counsel questions

1. **SC e-filing digital parameters** (file size, PDF/A level, bookmarks) — obtain the current SC e-filing user manual; until then `SC_EFILING` is `unverified` (S8 Q7).
2. **NCLT Rules 2016 format and e-filing limits** (spacing/margins closed 22 Oct 2026: double spacing, L 5 cm / R 2.5 cm per NCLAT r.19(1), NCLT r.158); state-wise exhibit series in district/commercial courts **[VERIFY — open: NCLT portal limit; State exhibit practice]**.
3. **SC Rules O.VIII r.3** — whether a professional translator's certificate with the AOR's certificate suffices (S8 Q6); equivalent rules per High Court.
4. **BSA Schedule** — field-level text of Parts A and B; who qualifies as "expert" (s.79A Examiner or otherwise); whether Equator's designated officer may sign Part A for platform records (S7 Q9, Q10).
5. **Draft SC AI Regulations 2026 Reg 43(3)** wording and *Pooja Ramesh Singh* (2026 INSC 668) text from the SCI website before quoting in product copy (S7 §6 item 12).
6. **Shama Sharma** direction on caste/religion in memo of parties — confirm order text (S8 §2.3).
7. **Vendor facts**: Sarvam Translate language list, glossary support and DPA (no training, retention); AWS Translate coverage and ap-south-1 availability; Azure Document Intelligence and Google DocAI regional availability for handwriting; ESP document size limits (Appendix D) **[VERIFY — open (vendor): Sarvam 22 languages and AWS Translate 10 Indic languages + ap-south-1 confirmed from public docs 22 Oct 2026; Azure/Google OCR regions, ESP limits and DPAs open]**.
8. **SUVAS** term-list licensing for the glossary.
9. Whether caucus-shared documents in **statutory-mode** mediation require any additional handling once Mediation Act s.22 is notified (flag NN-05).
10. Retention of awards permanently as an institutional record vs DPDP s.8(7) — counsel to confirm the "law requires" ground for arbitral records (A&C s.42A gives confidentiality, not a retention duty).

---

## Phase addendum (paste into P02)

> Scope addition to P02 (DMS). Supersedes FR-P02-36 `confidentiality` and `privilege` value sets (L-D-02) and extends FR-P02-35 to FR-P02-40. Screens SCR-P02-60…79 reserved.

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P02-V2-L01 | **Repository and folders** (§1.2): system folders per case, per-party `DRF`, sub-folders ≤ depth 3; `core.document_folders`; `INT` and `CAU` excluded from all party/neutral surfaces. | Folder tree created on case filing; `INT` documents return 404 to parties and neutrals |
| FR-P02-V2-L02 | **Visibility lifecycle and audiences** (§2.1–§2.3) with `core.document_shares`, Cerbos policy §2.9 and mapping of legacy enums; privilege values per Appendix F. | L-AT-01, L-AT-04, L-AT-22 pass; migration maps every legacy row |
| FR-P02-V2-L03 | **Mechanism-aware share dialog** SCR-P02-61 (§2.4) incl. caucus share for mediation/conciliation and the A&C s.24(3) rule for arbitration. | L-AT-02, L-AT-03 pass |
| FR-P02-V2-L04 | **Share requests, secure links, disclosure register** (§2.5–§2.6). | L-AT-05 passes; link token stored only as hash |
| FR-P02-V2-L05 | **Activity panel** SCR-P02-62 (§2.7) role-shaped. | Party sees other side's views as counts only |
| FR-P02-V2-L06 | **Metadata, tags, filters, saved views, bulk actions** (§1.4–§1.8). | Persona default views seeded; `TAG_SENSITIVE_TERM` lint active; bulk ZIP carries manifest |
| FR-P02-V2-L07 | **Search** with audience-key filtering, per-language analysers, `AclDriftJob` (§1.6). | L-AT-22 passes; p95 < 800 ms on 1M pages seed |
| FR-P02-V2-L08 | **Preview, annotation, watermarking, download controls** (§1.9–§1.13), view-only tiles for `sealed`. | Watermark hash logged per download; annotations never in exports |
| FR-P02-V2-L09 | **Redaction tool** with true redaction and two-person rule (§1.11). | L-AT-20 passes |
| FR-P02-V2-L10 | **Legal hold and retention** (§1.14–§1.15) with erasure certificates. | L-AT-21 passes |
| FR-P02-V2-L11 | **Filing → scrutiny → neutral packet → service** (§3.1–§3.5) with checklist SCR-F01…F12. | Scrutiny SLA clocks owned; neutral packet versioned with diff |
| FR-P02-V2-L12 | **E-bundle rules** (§3.6): types, frozen page map, hyperlinks, joint index approval. | Served bundle immutable; change note generated on rebuild |
| FR-P02-V2-L13 | **WhatsApp parser** (§6.2) with ≥ 12 golden fixtures, locale prompt, media linking, cap warning, counter-export diff, joint-authenticity request. | L-AT-11, L-AT-12, L-AT-13 pass |
| FR-P02-V2-L14 | **Screenshot OCR and OCR router** (§6.3–§6.4) with agreement-based confidence and page anchors; residency guard. | L-AT-16 passes; every OCR line has an anchor |
| FR-P02-V2-L15 | **Type-copy editor and attestation** SCR-P02-63 (§6.5–§6.7). | L-AT-09, L-AT-10 pass |
| FR-P02-V2-L16 | **LID** per document/page/message incl. code-mixed classes; `core.languages` seeded with 28 + 5 rows (§7.1–§7.2). | Golden LID set ≥ 95% top-1 on the 22 Indic + 6 UN test pages |
| FR-P02-V2-L17 | **Upload security** (§8.1) incl. CDR renditions, ZIP safety, encrypted-file rejection, legacy-font detection. | Malicious PDF test corpus produces sanitised renditions; originals untouched |
| FR-P02-V2-L18 | **Bulk upload, review sets and scrutiny queue** *(v3.1)*: classification grid with inline edit, duplicate checks and per-row retry (§1.8); own-side review sets with batches, coding shortcuts, QC sample and privilege-log draft (§1.16); scrutiny queue with automatic checks, deadline-aware order, SLA pause on return and batch accept for procedural filings (§3.2); ZIP names per `EQ-EXPORT-1.0`. | L-AT-25…L-AT-28 pass; scrutiny-within-SLA KPI on the case-manager dashboard |

## Phase addendum (paste into P06)

> Scope addition to P06. Screens SCR-P06-40…59 reserved.

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P06-V2-L01 | **Render profiles** (§5.2) as versioned, maker–checker data; seeds `SC_2020_PRINT`, `HC_TS_EFILING_2020`, `HC_RJ_EFILING`, `EQR_TRIBUNAL`, `FOREIGN_SEAT` (verified) and `SC_EFILING`, `HC_GENERIC`, `DIST_COMMERCIAL`, `NCLT` (unverified). | L-AT-06 passes; unverified exports carry the cover notice; `court.sc_efiling.verified` OFF |
| FR-P06-V2-L02 | **Court Document Builder** SCR-P06-41 on the `LegalDoc` AST with the component catalogue (§5.3), verification wizard (O.VI r.15 / r.15A), page-reference fields and annexure maps (§5.4–§5.5). | Reordering annexures updates every reference; `COURT_EXPORT_UNRESOLVED_REFERENCE` on dangling refs |
| FR-P06-V2-L03 | **Render pipeline** DOCX → PDF/A-2b with assembly, OCR, bookmarks, split, validation and determinism (§5.6–§5.7). | L-AT-07 passes; golden pixel diff ≤ 0.1% |
| FR-P06-V2-L04 | **Fonts and bilingual layouts** (§5.8, §7.9). | L-AT-24 passes |
| FR-P06-V2-L05 | **eSign document contract** (§4.1–§4.3): frozen hash, stamp-before-sign, representative limits, signature certificate page, PAdES LTV storage. | `ESTAMP_REQUIRED_BEFORE_SIGNING` enforced; signed PDF is a new version and ledgered |
| FR-P06-V2-L06 | **Affidavit flow** (§4.4) and original-affidavit reminder. | L-AT-18 passes; reminder task owned |
| FR-P06-V2-L07 | **Certified translation** workflow on `core.translation_requests` with certificate template and forum guidance (§7.7); machine translations never certified. | L-AT-08, L-AT-15 pass; lint LBL-04…06 green |
| FR-P06-V2-L08 | **Back-translation** for high-stakes outputs (§7.5). | Flagged segments block issue of a non-English notice/award translation until reviewed |
| FR-P06-V2-L09 | **BSA s.63 certificates** (§8.5): Part A auto-fill with hash table and e-sign; Part B expert routing; re-hash on export. | L-AT-19 passes; `HASH_MISMATCH_CRITICAL` raises a Critical incident in test |
| FR-P06-V2-L10 | **Type copies and translations in exports**: originals first, `(T)`/`(E)` sub-items with own index rows (§6.8). | Paper-book index shows both rows with page ranges |
| FR-P06-V2-L11 | **NN-08 checks** at template, term and sign-request level (§4.4). | L-AT-17 passes |

## Phase addendum (paste into P11)

> Scope addition to P11 (AI layer). Screens SCR-P11-40…49 reserved.

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P11-V2-L01 | **OCR router as an AI-gateway policy**: data-class routing (D0–D4), region pinning, `ocr.regional_cloud.enabled` gate, fail-closed queueing (L-D-06, §6.4). | L-AT-16 passes; gateway logs `{provider, model_id, region, version_date}` per page |
| FR-P11-V2-L02 | **Agreement-based confidence** service (CER between engines; thresholds configurable tighter only). | Unit vectors: identical lines → high; 5% CER → medium; 12% → low |
| FR-P11-V2-L03 | **`translation_agent` upgrade**: engine order per language (§7.1), glossary locks, back-translation, labels; Claude prompts treat document text as data. | L-AT-14 passes; prompt-injection test set (imperatives inside documents) produces no tool call |
| FR-P11-V2-L04 | **Evaluation harness per language** — OCR CER (printed and handwritten), MT chrF++ + human adequacy on 300 legal segments per pair, LID accuracy, glossary adherence ≥ 98%, numbers/dates 100%. | Model or engine change blocked on regression; results stored in `core.ai_eval_runs` |
| FR-P11-V2-L05 | **Tamper hints and counter-export diff as signals only** (copy fixed; no finding language). | Copy-lint blocks "fake", "forged", "fabricated" in neutral-facing hints |
| FR-P11-V2-L06 | **Redaction suggestions** (NER + patterns) with human approval mandatory (§1.11). | No redaction applies without maker and checker |
| FR-P11-V2-L07 | **Neutrality firewall**: neutrals' AI tools see only neutral-packet documents; party drafting artefacts and prompts (App. M) are invisible to neutrals and case managers (S7 §3.8). | Policy test: neutral-scoped retrieval returns zero `PRIVATE_DRAFT` chunks |
