# Phase P03 — Regulatory Content Library, Template Registry and Excel Import

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, RLS, audit ledger and Correction Entries, object storage with Object Lock, outbox), P01 (identity, roles `plt_content_*`, `ten_admin`, step-up MFA), P02 (settings registry, rule-pack engine, terminology overrides, Governed change pipeline).
>
> **Sequencing:** P03 starts after P01 exits and runs alongside P02 sprint 2 onwards. P04 cannot start its compliance-instance work until P03 §13 items 1–6 are green. P05 consumes the content model, the release pipeline and the importer built here. P15 (sector packs) plugs its applicability rules into the interface defined in §4H.
>
> **Binding appendices:** E (Excel template contract, entity-family vocabularies, importer rules — owned by S2; this phase implements it), F (source register), G (legal rules register), B (data model, events, errors), U (settings catalogue), D (access matrix).
>
> **Requirements covered:** R-003, R-004, R-005, R-007, R-013, R-017, R-039, R-084, R-086, R-087, R-088, R-102 (ingestion side), R-005/D-19 (jurisdiction packs).
>
> **Estimated effort:** 6 two-week sprints for a squad of 8 (content model and release pipeline 3; importer and template registry 3; tenant catalogue and overlay UX 2).

---

## 1. Objective and business outcome

LawDocsComply sells one product to many kinds of regulated entity — an NBFC in the Middle Layer, an Urban Co-operative Bank in Tier 2, an IFSCA Finance Unit, an AIF, a listed company, an LLP, a credit co-operative society. The legal content each of them must comply with is different, it changes every month, and every client wants to adjust the wording to its own operating structure. This phase builds the **content backbone** that makes that possible without code changes:

1. a versioned, clause-linked **Regulatory Content Library** owned by the LawDocs content team;
2. a **Template Registry** that treats the owner's Excel question format as a versioned ingestion contract, one template per entity family (D-08; Appendix E);
3. an **Excel Importer** that validates, previews, diffs and publishes question sheets prepared in Part 2 of the programme (R-004, R-084);
4. a **tenant overlay** model so that a client can edit, add or retire questions for itself only, with a full audit trail, while still receiving platform updates (R-017, R-086, NN-03);
5. a **Regulation Catalogue** in which the client admin sees every available instrument with its date, update date and applicability, and adds or removes it with a checkbox (R-087).

| Outcome | Exit-gate measure |
|---|---|
| Owner can load Part-2 question sheets without developer help | The 13 IFSCA sheets already in the `IFSCA Documents` folder and the two samples supplied on 25-Oct-2026 import with zero blocking errors after correction; median time from upload to "ready for checker" ≤ 5 minutes for a 300-row sheet |
| Every checkpoint is traceable to law | 100 % of published checkpoints carry authority, instrument, version, clause reference, source URL and source-file hash (NN-06); a citation lint rejects any row without them |
| Tenants customise without losing updates | A tenant overlay on 20 checkpoints survives a platform release that amends 5 of them; the 15 untouched overlays rebase automatically; the 5 conflicting overlays raise one consolidated review task; no completed compliance record changes (NN-03, NN-29) |
| Client admin decides applicability in one screen | A new NBFC-ML tenant sees its recommended instruments pre-ticked, can accept all in one click, or untick one with a reason; time to a complete applicable set ≤ 10 minutes |
| Customisation hierarchy works | A tenant renames "Compliance" to "Secretarial & Compliance" and splits "Risk Management" into "Credit Risk" and "Operational Risk"; all existing checkpoints remap via a mapping table, without editing any question |
| Round-trip Excel | Export of any adopted instrument in the owner's format, edit offline, re-import: unchanged rows are recognised by CompID, changed rows show a cell-level diff, and nothing is applied before checker approval |
| Global-ready | A non-Indian jurisdiction pack (EU GDPR, flag OFF) can be created as data — authority, instruments, holiday calendar, vocabulary — without schema change (D-19) |

---

## 2. Scope (in / out)

**In scope**
- Content model: jurisdiction → authority → instrument → instrument version → clause → checkpoint (question/actionable) → control activity → evidence requirement; content packs and content releases.
- Content team workflows: authoring in the Content Studio grid, import from Excel, quality lint, maker → checker → publisher release (roles `plt_content_maker`, `plt_content_checker`, `plt_content_publisher`).
- Template Registry: template families, template versions, column contract, controlled vocabularies with canonical codes, named ranges, the `_Template_Info` sheet, fingerprinting, template download.
- Importer: Content mode (platform and tenant), Workspace mode (round-trip of tenant compliance status — validation built here, application of status changes built in P04), Overlay mode (tenant edits offline), error report, diff, re-import, idempotency.
- Tenant overlay and tenant-authored checkpoints; three-way rebase on platform updates; conflict review.
- Customisation hierarchy and terminology: regulator → tenant → legal entity → department → function; department and function renaming and mapping; default-owner rules.
- Regulation Catalogue (tenant), adoption and removal, dependencies between instruments, applicability badges from the P15 engine.
- Jurisdiction-pack framework (D-19), holiday calendars as reference data (consumed by P04's due-date engine).
- Seed: migration of the existing LawDocsComply MongoDB question banks (RBI NBFC Base/Middle Layer/CIC, Companies Act) via the P00 migration scripts into the new model, with provenance `MIGRATED_V0`.

**Out of scope (owned elsewhere)**
- Writing the questions themselves (Part 2 of the programme; separate Cowork chats).
- AI generation of question sheets from an uploaded instrument (P05 AI Question Authoring Studio; it produces files that enter this importer).
- Regulatory monitoring, change classification and Updates inbox (P05).
- Compliance instances, due dates, maker/checker execution, evidence upload (P04).
- Applicability rule content per sector (P15) — this phase defines the interface and stores the expressions.
- Policy templates (P07), return definitions (P11), risk taxonomies (P08).

---

## 3. Personas and permissions touched

| Role | What they do in P03 | Key permission(s) |
|---|---|---|
| `plt_content_maker` | Uploads Part-2 sheets, edits checkpoints in Content Studio, fixes lint errors, proposes releases | `cnt.checkpoint.draft`, `tpl.import.content.platform` |
| `plt_content_checker` | Reviews every draft row (cell-level diff), approves/returns with comments | `cnt.checkpoint.review`; cannot approve own drafts (NN-05) |
| `plt_content_publisher` | Schedules and publishes a content release, sets effective date and tenant-notification text | `cnt.release.publish`; must differ from maker of ≥ 1 row in the release |
| `plt_super_admin` | Manages template families and vocabularies (Governed), emergency withdrawal of a release, Correction Entries (D-02) | `tpl.template.manage`, `cnt.release.withdraw`, `core.correction.propose` |
| `ten_admin` | Adopts/removes instruments in the Regulation Catalogue, approves tenant overlays, manages department/function mapping | `cnt.catalogue.adopt`, `cnt.overlay.approve`, `cfg.terminology.edit` |
| `ten_cco` | Authors and approves overlays and tenant checkpoints; reviews rebase conflicts | `cnt.overlay.draft`, `cnt.overlay.approve` (not on own drafts) |
| `ten_dept_head` | Proposes overlays for checkpoints mapped to own department | `cnt.overlay.draft` scoped by ABAC `department_id` |
| `ten_maker`, `ten_checker` | Read checkpoint content in their tasks; may suggest an overlay ("Suggest wording change") | `cnt.overlay.suggest` |
| `ten_internal_auditor`, `ten_external_auditor`, `ten_supervisor_view` | Read base and overlay with the diff and audit history | `cnt.read`, `core.audit.read` within grant |
| `dlv_rm`, `dlv_professional` (retainer, D-03) | Prepare overlays and tenant checkpoints on the client's behalf as maker | Same as `ten_cco` draft rights inside the granted tenant; never approve (client checker approves; R-072) |
| `svc_vidhi` | Suggests plain-language explanations, due rules, applicability expressions, duplicate detection | Draft-only, on behalf of a named user (NN-14) |

---

## 4. Functional requirements

### 4A. Content model

**FR-P03-01 Jurisdiction and authority registry.** `cnt.jurisdictions` holds ISO-3166 codes with sub-national entries (`IN`, `IN-MH`, `IN-UP`, `IN-RJ`, `IN-DL`, …; `EU`; `US-CA`). `cnt.authorities` holds each issuing body with code, name, jurisdiction, parent (e.g., state Registrar of Co-operative Societies under the state government), official site, monitoring source IDs (Appendix F), language(s) of publication and timezone. Seed authorities: RBI, SEBI, IFSCA, IRDAI, PFRDA (inactive), MCA (and ROC), MeitY, CERT-In, MoLE and each state Labour Department, Ministry of Cooperation, CRCS, each state RCS, FIU-IND, CBIC/GST Council, CBDT, ICAI, ICSI, ICMAI (standard-setters, marked `STANDARD_SETTER`), and the international placeholders EU (EDPB/Commission), California (CPPA/AG), UK ICO, Singapore PDPC, UAE (flag OFF).

**FR-P03-02 Instrument.** An instrument is any document that creates, modifies, interprets or withdraws a requirement. Fields: `instrument_id` (ULID, stable for life), `authority_id`, `instrument_type` (vocabulary: ACT, RULES, REGULATIONS, MASTER_DIRECTION, DIRECTION, AMENDMENT_DIRECTION, MASTER_CIRCULAR, CIRCULAR, NOTIFICATION, GUIDELINES, HANDBOOK, FAQ, STANDARD, CODE, ORDER, PRESS_RELEASE, CONSULTATION, INFORMAL_GUIDANCE), `title` (official), `short_title`, `reference_no` (e.g., `RBI/2025-26/…`, `SEBI/HO/…`, `IFSCA/…`, `G.S.R. 846(E)`), `issue_date`, `effective_from`, `effective_to`, `status` (DRAFT_PUBLISHED_BY_REGULATOR, IN_FORCE, PARTIALLY_IN_FORCE, NOT_YET_IN_FORCE, SUPERSEDED, REPEALED, WITHDRAWN), `binding_nature` (LAW, REGULATOR_DIRECTION, REGULATOR_GUIDANCE, STANDARD, GOOD_PRACTICE, TENANT_POLICY — NN-06 requires this distinction), `family_tags[]` (template families, Appendix E), `entity_scope_summary` (human text), `source_url`, `language`, `supersedes[]`, `superseded_by`, `related[]`, `commencement_notes` (for phased commencement such as DPDP Rules 2025 and the Labour Codes, where sections commence on different dates).

> RBI's consolidation of 28 November 2025 issued 238 function-wise Master Directions for eleven RE categories (commercial banks, small finance banks, payments banks, local area banks, regional rural banks, UCBs, rural co-operative banks, AIFIs, NBFCs, ARCs, CICs), named "Reserve Bank of India (<RE category> – <Subject>) Directions, 2025", repealing over 9,000 circulars with a savings clause for actions under repealed instructions. Later amendments arrive as Amendment Directions and as consolidations "updated as on <date>". The model must therefore (a) treat each RE-category direction as a separate instrument even where the subject is the same (e.g., Governance Directions for Commercial Banks, SFBs and UCBs), (b) record the "updated as on" date as a new instrument version, and (c) record `repeals[]` with a savings-clause note so that historical compliance records cite the instrument in force at the time (NN-07). [Source: RBI Master Directions page; JSA KM Newsflash 29-Nov-2025.]

**FR-P03-03 Instrument version.** Every textual state of an instrument is an immutable `cnt.instrument_versions` row: `version_no`, `as_of_date` (regulator's "updated as on" or the amendment date), `source_file_object_key`, `source_sha256`, `retrieved_at`, `retrieved_from_url`, `extraction_method` (NATIVE_PDF_TEXT, OCR, HTML), `ocr_confidence`, `page_count`, `change_origin` (`chg.change_item_id` from P05, or MANUAL, or MIGRATED_V0), `published_release_id`. The source PDF is stored with Object Lock (NN-09). A version is never edited; a corrected extraction creates a new version with `correction_of`.

**FR-P03-04 Clause index.** `cnt.clauses` stores the hierarchical structure of a version: `clause_path` (normalised, e.g., `Ch III > 12 > (3) > (a)`), `display_ref` exactly as the regulator prints it (`Para 12(3)(a)`, `Reg. 4(1)-(2)`, `Rule 7(1)`, `Section 135(5)`), `heading`, `text`, `text_sha256`, `page_from/page_to`, `parent_clause_id`, `order`. Clauses are matched across versions by `clause_lineage_id` (assigned by P05's diff engine) so a renumbered paragraph keeps its history.

**FR-P03-05 Checkpoint (question / actionable).** One row of the owner's Excel equals one **checkpoint**. Following the Ecosystem Integration Specification v1.1 §9.3 ("checkpoint banks → `Obligation`; each checkpoint carries the canonical `obligation_ref`"), a checkpoint is the unit exported to Finbyx, Udofin and third-party GRC tools as an `Obligation`. Fields:

| Field | Source column | Notes |
|---|---|---|
| `checkpoint_id` | — | ULID, stable across versions |
| `comp_id` | E | System-assigned human key `<FAMILY>-<INSTR4>-<SEQ4>` (e.g., `NBFC-0412-0007`); blank in authoring files; written on every export; used for round-trip matching |
| `serial_no` | B | Order within the instrument; display only |
| `applicability_layer[]` | C | Values from the family vocabulary (e.g., NBFC: Base Layer, Middle Layer, Upper Layer, Top Layer; UCB: Tier 1–4; IFSCA: sector) |
| `applicability_type[]` | D | One or more values from the family vocabulary (multi-value allowed; canonical delimiter `"; "` per master X-08 and Appendix E §E.4.2 — §4D V-11) |
| `short_title` | F | ≤ 120 characters |
| `question_text` | G | The compliance question or actionable, normally phrased "Has the <entity> …?" |
| `frequency_code` | H | Canonical code mapped from the family's "Due date & Frequency" list (ANNUAL, HALF_YEARLY, QUARTERLY, MONTHLY, FORTNIGHTLY, WEEKLY, DAILY, EVENT, IMMEDIATE, CONTINUOUS, ONE_TIME, plus EVERY_2Y, EVERY_3Y, EVERY_5Y; Appendix E §E.13.1 is binding) |
| `due_rule` | — (Studio) | Structured rule consumed by P04 (§4C of P04): anchor, offset, business-day convention, calendar; AI-suggested from G/K/L/S and confirmed by the content maker |
| `clause_refs[]` | K | Text as written + resolved `clause_id`s; at least one must resolve (lint L-03) |
| `explanation` | L | Plain-language interpretation |
| `department_code` | M | Canonical department code per Appendix U §U.6.1/§U.9.0 (master X-10), mapped from the column M display name; tenant mapping applies (§4G) |
| `related_documents` | N | Free text and URLs; URLs validated and archived |
| `compliance_type_code` | O | POLICY, COMPLIANCE, RETURN_REPORT, COMMITTEE, INTERNAL, SUGGESTIVE (+ family additions REGISTERS_AND_RECORDS, DISCLOSURES, NOTICES_AND_CONSENTS; Appendix E §E.13.3 is binding) |
| `filing_reporting` | P | Free text + structured `filing_targets[]` (authority/portal codes, e.g., `RBI_CIMS`, `MCA_V3`, `IFSCA`, `FIU_IND`, `GSTN`) |
| `consequences` | Q | Text + optional structured `penalty_ref` (link to Appendix G rule and the P20 savings model) |
| `risk_rating` | R | HIGH, MEDIUM, LOW (no family may add or rename risk levels, NN-35) |
| `conditions_exemptions` | S | Text + structured `applicability_expr` (CEL, §4H) |
| `expected_evidence` | U | What must be uploaded as proof; mandatory (lint L-07) |
| `control_activity` | V | What the maker must do; mandatory (lint L-08) |
| `obligation_ref` | — | Canonical reference `<AUTH>/<instrument short code>/<version>#<display_ref>`, e.g., `RBI/NBFC-GOV-2025/v3#12(3)` |
| `binding_nature` | — | Inherited from the instrument; may be downgraded per row to GOOD_PRACTICE or SUGGESTIVE |
| `control_library_refs[]` | — | Optional mapping to the LDC control library (ISO 27001 Annex A, COSO, SOC 2 TSC, RBI IT MD) for cross-framework reuse |
| `tags[]` | — | Free tags (e.g., `board_reporting`, `kmp_attestation`, `digital_lending`) |
| `status` | — | DRAFT, IN_REVIEW, RETURNED, APPROVED, PUBLISHED, RETIRED |
| `version_no` | — | Increments on every published change; previous versions immutable |

Columns I, J, T and W–AD are **user columns** and never belong to a checkpoint: they belong to a compliance instance in P04 (FR-P03-30).

**FR-P03-06 Control activity and evidence requirement.** Column V becomes a `cnt.control_activities` row (text, control type PREVENTIVE/DETECTIVE/CORRECTIVE, nature MANUAL/IT_DEPENDENT/AUTOMATED, suggested frequency, linked checkpoint) and column U becomes one or more `cnt.evidence_requirements` (description, document class from the DMS taxonomy in P07, mandatory flag, accepted file types, sample naming convention, retention class). Splitting U into multiple requirements is a Studio action ("Split evidence") with AI suggestion; the original text is preserved.

**FR-P03-07 Content pack and release.** A **content pack** groups instruments and checkpoints for a template family and jurisdiction (e.g., `IN-RBI-NBFC`, `IN-IFSCA-FCFU`, `IN-DPDP`, `IN-LAB`). A **content release** is the unit of publication: a set of new or changed checkpoint versions and instrument versions with release notes, effective date, impact summary (computed: tenants affected, compliance instances to create/retire), maker, checker and publisher. Releases have states DRAFT → IN_REVIEW → APPROVED → SCHEDULED → PUBLISHED, or WITHDRAWN (only before any tenant has acted on it; afterwards a corrective release is required). Publication emits `ObligationPublished` (Ecosystem Spec name) per changed checkpoint and `in.lawdocscomply.cnt.ContentReleasePublished.v1` for the release.

**FR-P03-08 Provenance and quality markers.** Every checkpoint version stores `origin` (PART2_EXCEL, AI_STUDIO_DRAFT, MANUAL, MIGRATED_V0, TENANT), `ai_assisted` (bool; if true, the AI run ID from P05), `quality_score` (lint results), `reviewed_by`, `reviewed_at`, `last_verified_at` (date a reviewer last confirmed the row against the primary source) and `verification_due_at` (default 12 months; High-risk 6 months; setting `cnt.quality.reverify_months`).

### 4B. Base content versus tenant overlay (NN-03)

**FR-P03-10 Resolution rule.** The checkpoint a tenant sees is `effective = base(version pinned) ⊕ overlay(tenant) ⊕ overlay(legal entity) ⊕ overlay(department)`. Overlays are **field-level patches** (`cnt.tenant_overlays`: `tenant_id`, `scope` TENANT/LEGAL_ENTITY/DEPARTMENT, `scope_ref`, `checkpoint_id`, `base_version_no` at which the overlay was authored, `patch` JSON of overridden fields, `reason`, `author`, `approver`, `effective_from`, `state`). Fields that may be overridden: G, F, H/due rule, L, M, N, O, P, Q, R, S, U, V, tags, default owner. Fields that may **not** be overridden: clause reference K, authority, instrument, `obligation_ref`, `binding_nature` (a tenant cannot make law optional — it can only mark a checkpoint not applicable with a reason through the applicability workflow, §4I).

**FR-P03-11 Tenant-authored checkpoints.** A tenant may add checkpoints (a) under a platform instrument (e.g., an extra internal control the tenant wants against Para 12), (b) under a **tenant instrument** it uploads itself (its own policy, a loan covenant, a lender's side letter, a regulator's specific inspection direction), or (c) as free internal compliance items (instrument type TENANT_POLICY). Tenant checkpoints use the same 30-column contract, the same importer (Overlay/Content mode with `scope = TENANT`) and the same AI Question Authoring Studio (P05), and are visible only to that tenant (RLS). Their `binding_nature` is TENANT_POLICY unless linked to a platform instrument clause.

**FR-P03-12 Three-way rebase on platform updates.** When a release changes base checkpoint version *n* → *n+1* and a tenant has an overlay authored at *n*:
- if the release changed only fields the overlay does not patch → **auto-rebase** (`base_version_no := n+1`), log `OverlayRebased`, show "Updated by LawDocs; your wording kept" in the checkpoint history;
- if the release changed a field the overlay patches → **conflict**: the overlay stays in force on version *n* text for that field, a `REBASE_CONFLICT` item appears in the tenant's Overlay Review queue, and the Updates inbox entry (P05) shows a three-column comparison *Old base | New base | Your version* with actions **Accept new base**, **Keep my version** (reason required), **Merge** (editor);
- if the release **retires** the checkpoint (repeal, supersession) → the overlay is retired with it unless the tenant chooses **Keep as internal control** (converts the effective text into a tenant checkpoint with `binding_nature = TENANT_POLICY` and a link to the retired base for history).
A conflict never blocks the tenant's work; an unresolved conflict older than `cnt.overlay.conflict_sla_days` (default 15) escalates to `ten_cco`.

**FR-P03-13 History is never rewritten.** Completed compliance instances (P04) pin `checkpoint_version_no` and `overlay_version_no`; neither a release nor an overlay change alters them (NN-03, NN-07). Exports and audit reports show the text that applied at the time.

**FR-P03-14 Overlay approval.** Tenant overlays follow maker → checker (NN-05) with the checker being `ten_cco`, `ten_admin` or a delegate; the setting `cnt.overlay.approval_mode` allows SINGLE_APPROVER (default) or TWO_LEVEL (CCO then admin) for High-risk checkpoints. Retainer RMs (`dlv_rm`) may draft but not approve (R-072).

### 4C. Template Registry (D-08; Appendix E)

**FR-P03-20 Template family.** `tpl.template_families`: `family_code` (Appendix E list — e.g., `RBI-SCB`, `RBI-UCB`, `RBI-RCB`, `RBI-NBFC`, `RBI-ARC`, `RBI-OTH`, `COOP-CCS`, `COOP-GEN`, `IFSCA-GEN`, `IFSCA-FCFU`, `IFSCA-FME`, `SEBI-MF`, `SEBI-AIF`, `SEBI-LISTED`, `SEBI-REIT-INVIT`, `SEBI-INT`, `IRDAI-INS`, `IRDAI-INT`, `MCA-CO`, `MCA-LLP`, `DATA-PRIV`, `CYBER`, `LAB`, `TAX`; Appendix E is authoritative), `name`, `regulators[]`, `jurisdiction`, `default_content_pack`, `active`.

**FR-P03-21 Template version.** `tpl.templates`: `template_code` (`LDC-TPL-<FAMILY>-v<major>.<minor>`), `family_code`, `column_contract` (JSON: for each of columns A–AD — header text exactly as row 2, group header in row 1, role CONTENT/USER/SYSTEM, required flag in Content mode, vocabulary ID, max length, multi-value flag, canonical field), `row1_values` and `row2_values` with SHA-256 (`header_hash`), `vocabularies` (ordered lists with canonical code per value), `named_ranges` (e.g., `NBFC_Freq` → `Rough!$A$2:$A$11`), `data_validation_ranges` (default rows 3–2000), `sheet_names` (`Sheet1`, `Rough`, `_Template_Info`), `info_sheet_contract`, `file_sha256` of the blank template, `status` (DRAFT, ACTIVE, DEPRECATED, RETIRED), `supersedes`. Changes to a template are Governed (P02; maker-checker; effective-dated). A deprecated template is still accepted for import for `tpl.deprecated_grace_days` (default 180) with a warning and automatic mapping to the successor.

**FR-P03-22 The owner's column contract (binding).** Both samples supplied on 25-Oct-2026 use one sheet `Sheet1` with row 1 group headers — `A1 "List"`, `K1 "Details"`, `T1 "Maker"`, `Y1 "Checker"`, `AC1 "Auditor"` — and row 2 column headers exactly as follows, plus a `Rough` sheet holding the dropdown lists exposed as named ranges and bound by data validation to rows 3 onwards of columns C, D, H, M, O and R:

| Col | Row-2 header (exact) | Role | Content-mode rule |
|---|---|---|---|
| A | Checkbox | SYSTEM | Must be blank |
| B | Serial No. | CONTENT | Integer; unique within sheet |
| C | General Applicability(Layer) | CONTENT | Required; family vocabulary |
| D | General Applicability(Type) | CONTENT | Required; family vocabulary; multi-value |
| E | CompID | SYSTEM | Blank in authoring; system key on export; if present must exist |
| F | Short Title | CONTENT | Required |
| G | Compliance Question/Actionable | CONTENT | Required |
| H | Due date & \nFrequency | CONTENT | Required; family vocabulary (note: the header contains a line break) |
| I | Date of Compliance | USER | Must be blank |
| J | Status | USER | Must be blank |
| K | Clause or Para no. | CONTENT | Required; must resolve to the clause index |
| L | Interpretation/Explanation | CONTENT | Required |
| M | Department | CONTENT | Required; family vocabulary |
| N | Related Document or Compliance or Weblinks, if any | CONTENT | Optional |
| O | Compliance Type | CONTENT | Required; family vocabulary |
| P | Filing and Reporting details/Intimation | CONTENT | Optional; reference list in `Rough` (not validated in Excel; validated by importer as warning) |
| Q | Consequences of Non-Compliance/Penalty/Impact | CONTENT | Required |
| R | Risk Categorization | CONTENT | Required; family vocabulary |
| S | Conditional Applicability/Exemptions | CONTENT | Optional |
| T | Maker User/Email ID | USER (system-filled) | Must be blank |
| U | Upload Document or Evidence | CONTENT | Required (expected evidence) |
| V | Control Activity | CONTENT | Required |
| W | Status Update by Maker User | USER | Must be blank |
| X | Comments, if any, by Maker User | USER | Must be blank |
| Y | Checker User/Email ID | USER | Must be blank |
| Z | Filing/Compliance Date | USER | Must be blank |
| AA | Review- Approve, Reject, Reallocate | USER | Must be blank |
| AB | Comments, if any, by Checker User | USER | Must be blank |
| AC | Assigned Auditor/Email ID | USER | Must be blank |
| AD | Comments, if any, by Auditor | USER | Must be blank |

The owner's IFSCA command instructs that rows 1 **and** 2 are not to be changed, while the NBFC command refers only to row 1; the importer therefore compares **both** rows to the registered template and treats any difference as a blocking error (V-02), which satisfies both instructions. The owner's architecture document refers to a "31-column schema"; the binding contract is the 30 columns above, and the 31st field in the product is the system `checkpoint_version_no`, shown in the UI but never required in Excel.

**FR-P03-23 `_Template_Info` sheet.** A protected sheet (documented password `LDC-TPL`, an accident guard, not a security control; Appendix E §E.5 is binding for the layout) with human-readable key/value rows (column A label, column B value) that the importer maps to these system keys: `template_code`, `template_version`, `family_code`, `regulators`, `jurisdiction`, `column_contract_sha256`, `header_hash`, `vocab_version`, `generated_at`, `generated_by` (`LDC` or `PART2`), and for files exported from LDC: `export_scope` (PLATFORM/TENANT), `tenant_ref` (opaque), `instrument_id`, `instrument_version_no`, `export_id`. The importer reads it first; if it is missing (e.g., an older sheet from the `IFSCA Documents` folder), the importer **fingerprints** the workbook — header hash plus the set of values in the `Rough` lists and the named-range names (e.g., `IFSCA_Freq`, `IFSCA_Sector`, `IFSCA_Entity`, `IFSCA_Dept`, `IFSCA_CompType`, `IFSCA_Risk` in the IFSCA family) — and proposes the matching template with a confidence score; the content maker confirms.

**FR-P03-24 Optional `_LDC_System` sheet (exports only).** Exports from LDC may carry a hidden sheet keyed by CompID holding system fields that the 30 columns cannot hold (structured `due_rule`, `applicability_expr`, `filing_targets`, `obligation_ref`, version numbers). On re-import, if present and unchanged, these fields round-trip; if absent, existing system fields are preserved; if present and edited, changes are validated like content. Authors working in Part 2 never need this sheet. [Coordination point with Appendix E — S2 to confirm.]

**FR-P03-25 Template download.** Content makers and tenant admins download blank templates from the Template Registry; tenant downloads are stamped with `_Template_Info.export_scope = TENANT` and the tenant's customised department list in the `Rough` sheet (from §4G) so that a tenant author picks its own department names.

### 4D. Importer

**FR-P03-30 Import modes.**

| Mode | Who | Purpose | Applies to |
|---|---|---|---|
| CONTENT_PLATFORM | `plt_content_maker` | Load or update base checkpoints of an instrument version (Part-2 sheets, AI Studio drafts) | Base content (release pipeline) |
| CONTENT_TENANT | `ten_admin`, `ten_cco`, `dlv_rm` | Load tenant checkpoints under a tenant instrument or a platform instrument | Tenant content (overlay approval) |
| OVERLAY | `ten_cco`, `ten_dept_head`, `dlv_rm` | Edit platform checkpoints offline: export → edit → re-import; changes become overlay drafts | Tenant overlays |
| WORKSPACE | Tenant users per their P04 permissions | Bulk-update compliance status, comments, dates, assignments using columns I, J, T, W–AD of an exported register | P04 compliance instances (validation here; application in P04 under maker-checker) |

**FR-P03-31 Pipeline.** Upload (drag-and-drop, max `tpl.import.max_file_mb` default 25 MB; `.xlsx` only, `.xlsm` rejected) → malware scan → macro and external-link stripping check (reject if VBA or external links present) → template identification (§4C) → parse with a streaming reader (formulas read as cached values; merged cells rejected in data rows) → row validation (§4D V-rules) → AI-assisted enrichment proposals (optional, P05 agents: due rule, applicability expression, clause resolution, duplicates) → preview grid → diff → submit to checker → apply. Each upload is an `tpl.import_jobs` row with idempotency key = `sha256(file) + mode + target`; re-uploading the same file returns the previous job.

**FR-P03-32 Validation rules (V-series; blocking unless marked W).**

| ID | Rule |
|---|---|
| V-01 | File is a valid `.xlsx`, ≤ size limit, no macros, no external links, sheet `Sheet1` present |
| V-02 | Row 1 and row 2 equal the registered template's values exactly (whitespace-normalised comparison shown in the error, exact comparison for pass) |
| V-03 | `_Template_Info` (or fingerprint) identifies an ACTIVE or grace-period DEPRECATED template of the expected family |
| V-04 | Columns A, I, J, T, W–AD blank in CONTENT and OVERLAY modes; any value is dropped with warning LDC-TPL-013 and never stored as content (Appendix E §E.3) |
| V-05 | Required content columns present (B, C, D, F, G, H, K, L, M, O, P, Q, R, S, U, V; N optional) — Appendix E §E.3 is binding |
| V-06 | Controlled-vocabulary columns (C, D, H, M, O, R) contain only listed values (case-insensitive match, normalised spaces; suggestion offered for near-misses, e.g., "Half-Yearly" → "Half Yearly") |
| V-07 | Serial No. integer and unique; gaps allowed (W) |
| V-08 | CompID either blank (new row) or an existing CompID of the same instrument and scope |
| V-09 | Clause reference K parses and resolves to ≥ 1 clause of the target instrument version; unresolved = blocking for platform content, W for tenant instruments without a clause index |
| V-10 | No duplicate rows: same instrument + same clause + question similarity ≥ 0.92 (embedding cosine) → W with "possible duplicate of CompID …" |
| V-11 | Multi-value cells (C and D) use the canonical `"; "` delimiter; `" \| "`, `,`, `;` and line breaks are accepted and normalised with info LDC-TPL-016; each token must match the family list (LDC-TPL-015) |
| V-12 | Text length limits (F ≤ 120; G ≤ 2,000; L ≤ 8,000; Q ≤ 4,000) (W above soft limits) |
| V-13 | URLs in N are well-formed and HTTPS where available (W); archived via the link archiver |
| V-14 | No personal data patterns (Aadhaar, PAN of individuals, phone, e-mail) in content columns (W; blocking for Aadhaar patterns — NN-12) |
| V-15 | Question style lint (W): starts with an interrogative or imperative; one actionable per row (detects "and" listing ≥ 3 distinct verbs → suggests split — the owner's rule that bundled sub-clauses become separate rows) |
| V-16 | Workspace mode: the user has permission for every row/action; status values and dates valid; checker actions only by the assigned checker; maker ≠ checker |
| V-17 | Workspace mode: row CompID belongs to the tenant's register and the export's `export_id` is not older than `tpl.workspace.max_export_age_days` (default 30) unless the user confirms a stale-merge |
| V-18 | Formula cells in content columns are converted to values (W) |
| V-19 | Hidden rows/columns in data area flagged (W) |
| V-20 | Family consistency: column C/D values belong to the same family as the template (e.g., an IFSCA entity in an NBFC template is blocking) |

**FR-P03-33 Preview and row errors.** A virtualised grid shows every row with a status chip (OK, WARNING, ERROR), errors inline per cell with the rule ID and a fix suggestion; filters by status, column, rule; "Fix in grid" editing for small corrections (edits are recorded as importer corrections with the user's identity); "Download error report" returns the same workbook with an added `_Import_Errors` sheet and red cell comments, so the author corrects in Excel and re-uploads.

**FR-P03-34 Diff.** Against the current version of the target (base instrument version, tenant overlay set, or workspace state), the importer computes NEW, CHANGED (cell-level, word-level diff for text), UNCHANGED, MISSING (rows present in LDC but absent from the file → proposed RETIRE, never automatic; the maker must tick "retire these N rows"), and MOVED (serial changes only). The diff is stored with the job and becomes the checker's review document.

**FR-P03-35 Re-import and partial acceptance.** Rows with errors may be excluded and the rest submitted ("Submit 287 valid rows; hold 13"). Held rows remain in the job for later correction. A later upload of a corrected file for the same target links to the earlier job (`supersedes_job_id`) and the diff is computed against the still-pending draft, not only against published content.

**FR-P03-36 Checker review.** The checker sees the diff and reviews rows with a sequential "Review next" flow (NN-46); a bulk "approve remaining" action exists only for rows classified Editorial or NOCHANGE (Appendix E §E.9); the checker can return selected rows with comments (comments return to the maker as a task in the Work Inbox, P04), or reject the job. Platform content approval creates or extends a content release (§4A FR-P03-07); tenant content approval publishes to the tenant immediately or at a chosen effective date.

**FR-P03-37 Performance.** Parse and validate 2,000 rows in ≤ 30 s at P95; preview grid opens in ≤ 2 s; diff ≤ 10 s for 2,000 rows.

### 4E. Content Studio (platform)

**FR-P03-40 Grid editor.** Spreadsheet-like editor over checkpoints of an instrument version with the 30 template columns plus system fields (due rule, applicability expression, obligation ref, filing targets, control-library mapping, tags), keyboard navigation, fill-down, find/replace with preview, column freezing, per-cell comments, split row (creates N rows from one with the clause reference copied and sub-clause suffixes suggested), merge rows, reorder. Autosave every 30 s to the draft.

**FR-P03-41 Side-by-side source.** The instrument PDF/HTML is shown beside the grid; selecting a row highlights the cited clause in the source; selecting text in the source offers "Create checkpoint from selection".

**FR-P03-42 Lint panel (L-series).** L-01 missing citation; L-02 citation does not resolve; L-03 clause not covered by any checkpoint (coverage map: every clause classed as OBLIGATION / DEFINITION / PROCEDURAL / NON_ACTIONABLE; obligation clauses with zero checkpoints flagged); L-04 bundled sub-clauses; L-05 plain-language readability of L (Flesch-Kincaid grade > 12 → W); L-06 frequency vs due-rule mismatch; L-07 evidence missing; L-08 control activity missing; L-09 risk rating missing or inconsistent with Q (e.g., penalty mentions cancellation of registration but risk Low); L-10 department not mapped; L-11 duplicate; L-12 personal data; L-13 broken URL. A release cannot be approved with any L-01, L-02, L-07, L-08 failure.

**FR-P03-43 Coverage report.** Per instrument version: clauses by class, obligation clauses covered, checkpoints per clause, High-risk proportion, last verified dates. Exportable to Excel/PDF; used as quality evidence for the content team and in sales ("every paragraph mapped").

### 4F. Regulation Catalogue for the client admin (R-087)

**FR-P03-50 Catalogue list.** Screen `SCR-CNT-10` lists every instrument available to the tenant's jurisdiction packs and template families, grouped by authority and then by subject, with columns:

| Column | Content |
|---|---|
| ☐ | Adoption checkbox (bulk) |
| Instrument | Short title, full title on hover, reference number |
| Authority | RBI / SEBI / IFSCA / … with icon |
| Issued | Issue date |
| Regulator updated | Latest "updated as on" / amendment date |
| LDC updated | Date of the latest content release affecting it |
| Applicability | Families, layers and types in plain words (from columns C/D aggregated) |
| For you | Badge from the P15 engine: **Applicable**, **Possibly applicable – answer 1 question**, **Not applicable** (with reason), **Optional / good practice** |
| Checkpoints | Count (High/Medium/Low split) |
| Status | Not adopted · Adopted · Adopted with *n* overlays · Update available · Pending removal |
| Depends on / required by | Linked instruments (e.g., the NBFC Governance Directions cross-refer to KYC, ALM and Financial Statements Directions) |

Filters: authority, family, applicability badge, status, risk, updated in last 30/90 days, department. Saved views. Search across titles, reference numbers and checkpoint text.

**FR-P03-51 Recommended set.** At onboarding (P01 wizard step 4) and whenever the entity profile changes, the P15 engine computes the recommended set; recommended instruments appear pre-ticked with an "Accept all recommended (n)" button. Mandatory items for the entity type (e.g., MCA obligations for every company) are shown locked-on with an "i" tooltip explaining why.

**FR-P03-52 Adopt.** Ticking an instrument and clicking **Adopt** shows a one-screen impact preview: checkpoints that will become active, compliance instances P04 will create for the current period, departments affected with default owners, first due dates. Confirming adopts in one step; owners and due dates can be adjusted afterwards in P04. Adoption is recorded with user, timestamp and the instrument version.

**FR-P03-53 Remove.** Unticking an adopted instrument requires a reason (vocabulary: NOT_APPLICABLE_ENTITY_TYPE, BELOW_THRESHOLD, EXEMPTED_BY_REGULATOR, COVERED_BY_GROUP_ENTITY, BUSINESS_DISCONTINUED, OTHER + text) and, for an instrument the engine marks **Applicable**, a second approver (`ten_cco` if the remover is `ten_admin`, and vice versa). Removal stops creation of future compliance instances from the effective date, cancels open instances with status CANCELLED_NOT_APPLICABLE (kept, not deleted), and preserves all completed work and evidence (NN-29). The removal appears in the CCO report's "Applicability decisions" section.

**FR-P03-54 Update available.** When a release changes an adopted instrument, the status shows **Update available** with a link to the Updates inbox item (P05); the tenant's acknowledgement and impact assessment are tracked there.

**FR-P03-55 Tenant instruments.** "Add your own instrument" uploads a PDF/DOCX (own policy, covenant, specific regulator letter), creates a tenant instrument and opens the AI Question Authoring Studio (P05) or the template download for manual authoring.

### 4G. Customisation hierarchy and terminology (R-086)

**FR-P03-60 Levels.** Content and configuration resolve through the hierarchy **Regulator/platform base → Tenant (company) → Legal entity → Department → Function (team)**. Each level can (a) rename terminology, (b) overlay checkpoint fields (§4B), (c) set default owners, (d) set reminder and escalation settings within P02 bounds. Lower levels inherit; a lock at a higher level (e.g., the tenant locks risk rating changes) prevents lower-level overrides.

**FR-P03-61 Department and function model.** The canonical department codes in each family's vocabulary (e.g., IFSCA list: Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management) are **reference codes**. Each tenant maintains its own department tree in the HRMS/org module (P13/P06), and a mapping table `cfg.department_map (tenant_id, canonical_code, tenant_department_id, function_id nullable, priority)` routes checkpoints. One canonical code may map to several tenant departments with a rule (e.g., by legal entity or by tag), and several canonical codes may map to one department. Unmapped canonical codes route to the tenant's default owner (`ten_cco`) and appear as a setup warning.

**FR-P03-62 Renaming.** Tenants rename departments, functions, compliance types, risk labels and status labels through the P02 terminology service; renames never change canonical codes, so reports across tenants and exports stay consistent, and the export package carries both the tenant label and the canonical code.

**FR-P03-63 Default owner rules.** For each checkpoint, owner resolution is: explicit assignment on the compliance instance → function default owner → department default owner → legal-entity compliance owner → tenant CCO. Backup owners are set at the same levels (used by P04 delegation on leave).

### 4H. Applicability interface (P15 owns the rules)

**FR-P03-70 Expression storage.** Each checkpoint stores `applicability_expr` in CEL (Common Expression Language) over the **entity profile** attributes (P15 schema: e.g., `entity.family == "RBI-NBFC" && entity.layer in ["MIDDLE","UPPER"] && entity.asset_size_cr >= 1000 && entity.accepts_public_funds`). Columns C and D compile to the base expression automatically; column S conditions are converted by the content maker (with Vidhi suggestions) into additional clauses or into **questions** (`NEEDS_INPUT` attributes) that the engine asks the tenant once.

**FR-P03-71 Contract.** `POST /v1/applicability/evaluate` (internal) with `{tenant_id, legal_entity_id, checkpoint_ids[] | instrument_id, as_of}` → per item `{result: APPLICABLE | NOT_APPLICABLE | NEEDS_INPUT | OPTIONAL, reasons[], missing_attributes[], rule_pack_version}`. Results are cached per profile hash and invalidated on profile change or rule-pack release. P15 implements the evaluator and the profile; P03 stores expressions and renders reasons.

**FR-P03-72 Explainability.** Every badge in the catalogue and every compliance instance shows "Why this applies to you" — the expression rendered in words with the profile values used (e.g., "Applies because you are an NBFC in the Middle Layer and your asset size (₹1,240 crore on 31-Mar-2026) is at or above ₹1,000 crore").

### 4I. Jurisdiction packs (D-19)

**FR-P03-80 Pack definition.** A jurisdiction pack bundles authorities, instrument catalogue, template families and vocabularies, holiday calendars, default languages, timezone, date and number formats, and currency, plus a `readiness_state` (DRAFT, SOURCED, REVIEWED, LIVE) and a named reviewer per authority. Only LIVE packs are offered to tenants; flags `pack.<code>.enabled` default OFF for all non-Indian packs (D-19).

**FR-P03-81 Holiday calendars.** `cnt.holiday_calendars` per jurisdiction and per relevant scope: RBI holidays under the Negotiable Instruments Act by state (RBI holiday matrix), stock-exchange trading holidays (NSE/BSE), IFSC (GIFT City) holidays, central government holidays, state government holidays, plus tenant calendars (P04). Each calendar is effective-dated and versioned; P04's due-date engine reads it.

**FR-P03-82 Global extensibility.** Adding a country requires no schema change: authorities, instruments, vocabularies and calendars are data; translations of UI terms use the P02 terminology service; content language may differ from UI language (e.g., UAE instruments in Arabic with English working translation from the DMS translation service, P07, marked as translation).

### 4J. Migration of existing LawDocsComply content

**FR-P03-90** P00's migration loads the MongoDB question banks (RBI NBFC Base/Middle Layer/CIC; Companies Act; and the nine RBI NBFC Master-Direction sheets of 31-Jul-2026, RBI/DoS/2026-27/460–468, prepared in September 2026) into `cnt` with `origin = MIGRATED_V0`, mapping legacy fields to the 30-column contract; rows that fail lint are loaded as DRAFT and listed in a migration quality report; nothing migrated is published to new tenants until a content checker approves it. Existing beta tenants (e.g., the Branch International beta) keep their legacy question texts as tenant overlays pinned to the migrated base so that their completed records are unchanged.

---

## 5. Workflows and state machines

### 5.1 Platform content import → release

```
UPLOADED → SCANNED → IDENTIFIED → VALIDATED ──(errors)──► NEEDS_FIX ──(re-upload / fix in grid)──► VALIDATED
VALIDATED → ENRICHED (optional AI proposals accepted/rejected row by row) → SUBMITTED
SUBMITTED → IN_REVIEW → { APPROVED | RETURNED (→ NEEDS_FIX) | REJECTED (terminal) }
APPROVED → ADDED_TO_RELEASE → (release) SCHEDULED → PUBLISHED
```
Guards: SUBMITTED requires zero blocking errors in submitted rows; APPROVED requires checker ≠ any maker of the rows (NN-05); ADDED_TO_RELEASE requires lint L-01/L-02/L-07/L-08 clean; PUBLISHED requires publisher ≠ checker for releases containing High-risk changes (setting `cnt.release.publisher_must_differ`, default true).
Timers: IN_REVIEW older than `cnt.review.sla_days` (default 3 business days) escalates to the content lead; NEEDS_FIX older than 15 days auto-archives the job (recoverable).

### 5.2 Content release

```
DRAFT → IN_REVIEW → APPROVED → SCHEDULED(effective_at, notify_at) → PUBLISHED
           │              │
           └─ RETURNED ◄──┘         PUBLISHED → (no tenant action yet) WITHDRAWN
                                     PUBLISHED → CORRECTED_BY(release_id)   (after tenant action)
```
On PUBLISHED: (1) checkpoint versions become current for tenants adopting the instrument; (2) overlay rebase job runs per tenant (§5.4); (3) P05 Updates items are created for affected tenants with the release notes and "what changed / why it matters / what to do"; (4) P04 receives `ObligationPublished` events and recalculates future instances (never completed ones); (5) Ecosystem `ObligationPublished` events go to subscribed products (Finbyx, Udofin) via the outbox.

### 5.3 Tenant overlay

```
DRAFT (author) → SUBMITTED → { APPROVED → ACTIVE | RETURNED → DRAFT | REJECTED }
ACTIVE → { SUPERSEDED (new overlay on same field) | REBASED (auto) | CONFLICT (base changed overridden field) | RETIRED }
CONFLICT → { ACCEPT_BASE (overlay field dropped) | KEEP (reason) | MERGE (new overlay version) } → ACTIVE/RETIRED
```
Every transition writes to the audit ledger with before/after field values (R-088: "audit trail when the client company changes the questions"). The tenant can view the full lineage of any checkpoint: base v1 → base v2 → overlay o1 (CCO, 12-Nov-2026, reason "align to our branch structure") → rebase → conflict → kept.

### 5.4 Overlay rebase job (pseudo-code)

```ts
for (const ov of overlaysOn(checkpointId)) {
  const changed = diffFields(base[n], base[n+1]);          // fields changed by the platform
  const overridden = Object.keys(ov.patch);
  const clash = intersect(changed, overridden);
  if (base[n+1].status === 'RETIRED') raise(ov, 'BASE_RETIRED');          // keep-as-internal option
  else if (clash.length === 0) rebase(ov, n+1);                            // auto, silent except history
  else raise(ov, 'REBASE_CONFLICT', { fields: clash, old: base[n], new: base[n+1], mine: ov.patch });
}
```
Conflicts are grouped per tenant per release into one review task to keep the Work Inbox short.

### 5.5 Instrument adoption and removal

```
NOT_ADOPTED → (adopt, impact preview confirmed) → ADOPTED
ADOPTED → (remove, reason [+ second approver if Applicable]) → PENDING_REMOVAL(effective_date) → REMOVED
REMOVED → (re-adopt) → ADOPTED   (history continuous; new instances only from re-adoption date)
```
Profile change (P15) that makes an adopted instrument NOT_APPLICABLE raises a suggestion, never an automatic removal; a profile change that makes a non-adopted instrument APPLICABLE raises an Updates item "New applicable instrument" with a one-click adopt.

### 5.6 Correction Entry on content (D-02)

A super admin who must change something already published (a wrong clause reference in a published checkpoint, a wrong date on an instrument version) raises a **Correction Entry**: target record, field, old value, new value, reason code (TYPO, WRONG_CITATION, SOURCE_CORRECTION, LEGAL_REVIEW, DATA_MIGRATION_FIX, OTHER), evidence, effective-at; a second platform approver approves. The correction creates a new version; the old version stays sealed and visible ("Corrected on 14-Nov-2026 by LawDocs: clause ref 12(3) → 12(4); reason WRONG_CITATION"). Completed compliance instances keep showing the text that applied, with a banner linking to the correction.

---

## 6. Screens and UX

| Screen ID | Name | Menu path | Roles | Key elements |
|---|---|---|---|---|
| SCR-CNT-01 | Content Library | Console › Content › Library | `plt_content_*`, `plt_super_admin` | Tree: jurisdiction › authority › instrument; columns: versions, checkpoints, last release, verification due, coverage %; filters; "Upload sheet" primary action |
| SCR-CNT-02 | Instrument workspace | Console › Content › Library › *instrument* | `plt_content_*` | Tabs: Overview (metadata, status, supersession), Versions (timeline with "updated as on" dates and source hashes), Clauses (index with classes), Checkpoints (grid), Coverage, Releases, History |
| SCR-CNT-03 | Content Studio grid | Instrument workspace › Checkpoints › Edit | `plt_content_maker` | 30 columns + system fields; source pane; lint panel; Vidhi suggestions pane; split/merge; autosave |
| SCR-CNT-04 | Release manager | Console › Content › Releases | `plt_content_checker`, `plt_content_publisher` | Release list; release detail with diff, impact (tenants, instances), notes editor, schedule, publish |
| SCR-TPL-01 | Template Registry | Console › Content › Templates | `plt_super_admin`, `plt_content_maker` | Families, versions, column contract viewer, vocabularies with canonical codes, download blank, compare versions |
| SCR-TPL-02 | Import wizard | Console › Content › Import; Tenant › Compliance › Regulations › Import | importers by mode | Step 1 upload & mode; Step 2 identification (template, confidence); Step 3 validation summary; Step 4 preview grid; Step 5 diff; Step 6 submit |
| SCR-TPL-03 | Import job detail | Import › Jobs › *job* | importer, checker | Status timeline, error report download, held rows, linked jobs, reviewer comments |
| SCR-TPL-04 | Checker diff review | Work Inbox › Content review | `plt_content_checker`, `ten_cco` | Side-by-side cell diff, "Review next" row approval (bulk only for Editorial/NOCHANGE rows, NN-46), return with comment per row |
| SCR-CNT-10 | Regulation Catalogue | Tenant › Compliance › Regulations | `ten_admin`, `ten_cco`, read for others | Table per §4F; bulk adopt; recommended banner; saved views |
| SCR-CNT-11 | Instrument (tenant view) | Regulations › *instrument* | tenant roles | Checkpoints with overlay indicators (✎), "Why applicable", update history, export in owner's format, adopt/remove |
| SCR-CNT-12 | My Questions & Overlays | Tenant › Compliance › Regulations › My changes | `ten_cco`, `ten_admin`, `ten_dept_head` | All overlays and tenant checkpoints with state, reason, approver; "New question"; "Edit offline (Excel)" |
| SCR-CNT-13 | Overlay conflicts | Work Inbox › Rebase conflicts | `ten_cco` | Three-column Old base / New base / Mine; Accept / Keep / Merge; bulk "Accept all base wording for Low-risk" |
| SCR-CNT-14 | Departments & functions mapping | Tenant › Settings › Organisation › Compliance mapping | `ten_admin` | Canonical codes ↔ tenant departments/functions; default and backup owners; unmapped warnings |
| SCR-CNT-15 | Checkpoint lineage | Any checkpoint › History | all with read | Timeline of base versions, overlays, corrections, rebases, with who/when/why and diff |

**UX rules.** (1) The catalogue opens with the recommended set and a single primary action; the admin should finish adoption in ≤ 3 clicks for the default path. (2) Every column header and vocabulary value has an "i" tooltip (`hlp` keys `cnt.col.<letter>`, `cnt.vocab.<code>`) explaining the term in plain English — e.g., "Conditional Applicability/Exemptions — the situations in which this requirement does not apply to you, or applies only above a size or activity threshold". (3) Keyboard: `/` search, `J/K` next/previous row, `E` edit, `Ctrl/Cmd+Enter` submit, `Shift+Click` range select. (4) Empty states explain the next step ("No instruments adopted yet — accept the 23 recommended for an NBFC in the Middle Layer"). (5) Error copy names the rule ID and the fix ("V-06: 'Half-Yearly' is not in the list for column H. Did you mean 'Half Yearly'? [Apply to 14 cells]"). (6) Large imports run as background jobs with a progress dialog and a completion notification; the user can leave the page. (7) All screens meet WCAG 2.2 AA (NN-21): the grid supports screen-reader row/column announcements and non-colour status indicators.

---

## 7. Backend design

### 7.1 Modules

`cnt` (content model, releases, catalogue, overlays, applicability expressions), `tpl` (template registry, importer), with calls to `cfg` (terminology, department map, settings), `dms` (source files, Object Lock), `ai` (enrichment proposals), `chg` (change items that create versions), `wf` (review tasks), `core` (audit ledger, Correction Entries, outbox).

### 7.2 Tables (key columns; full DDL in Appendix B)

| Table | Key columns |
|---|---|
| `cnt.jurisdictions` | code PK, name, parent_code, timezone, languages[] |
| `cnt.authorities` | authority_id, code, name, jurisdiction_code, kind (REGULATOR, MINISTRY, STATE_DEPT, STANDARD_SETTER, SRO), site_url, monitor_source_ids[] |
| `cnt.instruments` | instrument_id, authority_id, instrument_type, title, short_title, reference_no, issue_date, effective_from, effective_to, status, binding_nature, family_tags[], supersedes[], superseded_by, repeals[], savings_note, source_url |
| `cnt.instrument_versions` | instrument_version_id, instrument_id, version_no, as_of_date, source_object_key, source_sha256, retrieved_at, extraction_method, ocr_confidence, change_item_id, correction_of, release_id |
| `cnt.clauses` | clause_id, instrument_version_id, clause_lineage_id, clause_path, display_ref, heading, text, text_sha256, clause_class, page_from, page_to, parent_clause_id, ord |
| `cnt.checkpoints` | checkpoint_id, instrument_id, comp_id (unique per scope), scope (PLATFORM/TENANT), tenant_id (null for platform), current_version_no, status |
| `cnt.checkpoint_versions` | checkpoint_id, version_no, instrument_version_id, fields JSONB (30-column content), due_rule JSONB, applicability_expr TEXT, obligation_ref, filing_targets[], penalty_ref, risk_rating, department_code, compliance_type_code, frequency_code, binding_nature, origin, ai_run_id, created_by, reviewed_by, release_id, valid_from, valid_to, recorded_at |
| `cnt.checkpoint_clause_links` | checkpoint_id, version_no, clause_id |
| `cnt.control_activities` / `cnt.evidence_requirements` | linked to checkpoint version |
| `cnt.content_packs` | pack_code, jurisdiction_code, family_codes[], readiness_state, reviewer_ids |
| `cnt.content_releases` | release_id, pack_code, state, notes, effective_at, maker_ids[], checker_id, publisher_id, impact JSONB |
| `cnt.tenant_overlays` | overlay_id, tenant_id, scope, scope_ref, checkpoint_id, base_version_no, patch JSONB, reason, state, author_id, approver_id, effective_from, version_no |
| `cnt.tenant_adoptions` | tenant_id, legal_entity_id, instrument_id, state, adopted_version_no, adopted_by, adopted_at, removal_reason, removal_approver, effective_to |
| `cnt.holiday_calendars` / `cnt.holidays` | calendar_code, jurisdiction, scope, version, date, name, kind |
| `tpl.template_families` | family_code, name, regulators[], jurisdiction_code, default_pack_code, active |
| `tpl.templates` | template_code, family_code, version, column_contract JSONB, header_hash, vocab_version, named_ranges JSONB, status, valid_from, valid_to, blank_file_object_key |
| `tpl.vocabularies` | vocab_id, family_code, column_letter, value_text, canonical_code, ord, valid_from, valid_to |
| `tpl.import_jobs` | job_id, tenant_id nullable, mode, target_ref, file_object_key, file_sha256, template_code, identification_confidence, state, counts JSONB, supersedes_job_id, created_by, idempotency_key |
| `tpl.import_rows` | job_id, row_no, comp_id, status, errors JSONB, warnings JSONB, normalized JSONB, diff JSONB, held bool |
| `cfg.department_map` | tenant_id, canonical_code, tenant_department_id, function_id, rule JSONB, priority |

All tenant tables carry `tenant_id` with RLS (NN-01); platform content tables are readable by tenants through views filtered by adopted packs. Bitemporal columns (`valid_from/valid_to`, `recorded_at`) on versioned tables (NN-07).

### 7.3 APIs (REST, `/v1`, OpenAPI 3.1)

| Method & path | Purpose |
|---|---|
| `GET /content/instruments?authority=&family=&status=&q=` | Library / catalogue listing (tenant view filtered and decorated with adoption + applicability) |
| `GET /content/instruments/{id}` · `/versions` · `/versions/{v}/clauses` | Detail |
| `GET /content/checkpoints/{id}?effective_for=tenant` | Effective checkpoint (base ⊕ overlays) with lineage |
| `POST /content/imports` (multipart; `mode`, `target`) | Create import job (idempotent) |
| `GET /content/imports/{job}` · `/rows?status=` · `/error-report` · `/diff` | Job status, rows, error workbook, diff |
| `POST /content/imports/{job}/submit` · `/approve` · `/return` · `/reject` | Workflow actions |
| `POST /content/releases` · `/{id}/schedule` · `/{id}/publish` · `/{id}/withdraw` | Release pipeline (platform only) |
| `POST /tenant/adoptions` (bulk) · `DELETE /tenant/adoptions/{instrument}` (reason) | Adopt/remove |
| `POST /tenant/overlays` · `/{id}/submit` · `/{id}/approve` · `/{id}/resolve-conflict` | Overlay lifecycle |
| `GET /templates?family=` · `GET /templates/{code}/blank` | Template registry and blank download |
| `GET /tenant/instruments/{id}/export?format=xlsx` | Export in owner's format with `_Template_Info` and optional `_LDC_System` |
| `POST /v1/applicability/evaluate` (internal) | P15 contract |

### 7.4 Domain events (outbox; CloudEvents 1.0, `source urn:infrabyx:ldc:<tenant>`)

`in.lawdocscomply.cnt.InstrumentVersionCreated.v1`, `…cnt.ContentReleasePublished.v1`, `…cnt.ObligationPublished.v1` (Ecosystem name `ObligationPublished`; payload obligation_ref, paragraph, text hash, applicability, dates, owner), `…cnt.CheckpointRetired.v1`, `…cnt.InstrumentAdopted.v1`, `…cnt.InstrumentRemoved.v1`, `…cnt.OverlayApproved.v1`, `…cnt.OverlayRebased.v1`, `…cnt.OverlayConflictRaised.v1`, `…tpl.ImportJobCompleted.v1`, `…tpl.TemplateVersionActivated.v1`, `…core.CorrectionEntryApproved.v1`.

### 7.5 Jobs and Temporal workflows

`ImportJobWorkflow` (scan → identify → parse → validate → enrich → await review), `ReleasePublishWorkflow` (activate versions → fan-out rebase per tenant → emit events → notify P05 → recompute P04 schedules; idempotent per tenant with compensation on failure — a tenant whose rebase fails is retried and flagged, never partially published), `ReverificationSweep` (daily; checkpoints past `verification_due_at` → content team queue), `LinkArchiver` (weekly; archive URLs in column N and flag dead links), `CoverageRecompute` (on version change).

---

## 8. Integrations

- **Ecosystem (NN-23):** publishes `ObligationPublished` and checkpoint metadata per the Integration Specification §9.2–§9.3 Generic GRC contract (`Obligation` resource: obligation_ref, paragraph, text hash, applicability, dates, owner, status) so Finbyx (EMBEDDED/LDC_EXTERNAL/LDC_GROUP modes), Udofin and Equator can pull obligations; OSCAL `catalog`/`profile` export of a content pack on request (P18).
- **Excel engine:** server-side parsing with a streaming XLSX reader (e.g., ExcelJS streaming or SheetJS) in a sandboxed worker; writing exports with ExcelJS preserving data validation, named ranges and protection; template files themselves are produced in Part 2 / Appendix E.
- **Third-party content (future, flag OFF):** adapter port `CONTENT_FEED_PORT` for licensed regulatory content providers; imported content is labelled with provider and licence, never mixed with LawDocs-authored rows without a tag.
- **P05 AI Studio:** writes draft workbooks into this importer (CONTENT_PLATFORM or CONTENT_TENANT mode) — the same validation and review apply (NN-04).

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `cnt.quality.reverify_months` | G | 12 (High: 6) | 3–24 | content lead (maker-checker) |
| `cnt.review.sla_days` | G | 3 business days | 1–10 | content lead |
| `cnt.release.publisher_must_differ` | G | true | — | super admin |
| `cnt.overlay.approval_mode` | T | SINGLE_APPROVER | SINGLE_APPROVER, TWO_LEVEL | `ten_admin` |
| `cnt.overlay.conflict_sla_days` | T | 15 | 5–60 | `ten_admin` |
| `cnt.overlay.allowed_fields` | T | all permitted (§4B) | subset only; K/authority/obligation_ref locked (L) | `ten_admin` |
| `cnt.catalogue.removal_second_approver` | T | required for Applicable | cannot be disabled for High-risk instruments (G floor) | `ten_admin` |
| `cnt.catalogue.auto_suggest_on_profile_change` | T | true | — | `ten_admin` |
| `tpl.import.max_file_mb` | G | 25 | 5–100 | super admin |
| `tpl.import.max_rows` | L | 2,000 | — (Appendix E contract; data validations cover rows 3–2000; larger instruments are split into numbered parts) | — |
| `tpl.deprecated_grace_days` | G | 180 | 30–365 | super admin |
| `tpl.workspace.max_export_age_days` | T | 30 | 1–180 | `ten_admin` |
| `tpl.import.dv_rows` | G | 2,000 | 345–20,000 | super admin |
| `tpl.import.ai_enrichment` | T | ON (proposals only) | ON/OFF | `ten_admin` (tenant), content lead (platform) |
| `cnt.duplicate_similarity_threshold` | G | 0.92 | 0.80–0.99 | content lead |
| `pack.<code>.enabled` | G | IN packs ON; non-IN OFF | — | super admin + reviewer sign-off |
| `cfg.terminology.<term>` | T | canonical label | non-empty; length ≤ 60 | `ten_admin` |

---

## 10. Security, privacy and audit

- RLS on every tenant table; platform content exposed read-only through adoption-filtered views; tenant checkpoints never visible to other tenants or to the platform content team except under a support grant (NN-30).
- Uploaded workbooks are scanned (malware), stripped of macros/external links (rejected if present), parsed in an isolated worker with CPU/memory limits (zip-bomb and billion-laughs protection), and stored with Object Lock; the parsed values are the system of record, not the file.
- Every import, approval, release, adoption, removal, overlay and correction writes an audit-ledger event with actor, on-behalf-of, before/after, reason and request ID (NN-02, R-088). Audit views are available to `ten_internal_auditor`, `ten_external_auditor` and `ten_supervisor_view` within their grant.
- Correction Entries only, never in-place edits of published content (D-02).
- Exports carry `_Template_Info.export_id` and a SHA-256 in the export log; WORKSPACE re-imports verify the export ID to prevent cross-tenant replay.
- Personal-data lint (V-14) prevents names, PAN or Aadhaar of individuals in content columns.

---

## 11. AI touchpoints and guardrails

| Touchpoint | What Vidhi does | Guardrail |
|---|---|---|
| Template identification | Explains fingerprint result | Deterministic fingerprint decides; AI only explains |
| Clause resolution | Suggests the clause for an unresolved K value | Suggestion shown with source snippet; user accepts per row |
| Due rule extraction | Proposes structured `due_rule` from G/K/L/S text (e.g., "within 7 days of appointment" → anchor EVENT:appointment, offset +7 calendar days) | Confidence shown; maker confirms; low confidence left blank |
| Applicability expression | Converts S text to CEL clauses or NEEDS_INPUT questions | Rendered back to words for review; never applied unreviewed |
| Duplicate detection | Embedding similarity | Warning only |
| Plain-language check | Suggests simpler L text | Original kept; edit is the maker's |
| Split bundled rows | Proposes N rows for sub-clauses | Maker accepts |
All suggestions are logged with model, prompt version and the accepting user (NN-14); no AI output changes published content without the release pipeline (NN-04).

---

## 12. Acceptance criteria (`tests/acceptance/p03/*.feature`)

```gherkin
Feature: Excel import of a Part-2 question sheet

  Scenario: Importing the IFSCA Appointed Actuary sheet without _Template_Info
    Given the workbook "05 Insurance - IFSCA Appointed Actuary Regulations 2022.xlsx"
    When a content maker uploads it in CONTENT_PLATFORM mode
    Then the importer fingerprints it as template "LDC-TPL-IFSCA-GEN-v1.0" with confidence >= 0.95
    And rows 1 and 2 match the registered headers exactly
    And every data row is validated against the IFSCA vocabularies for columns C, D, H, M, O and R

  Scenario: Blocking header change
    Given a sheet whose cell H2 reads "Due Date / Frequency"
    When it is uploaded
    Then rule V-02 blocks the job and the error names cell H2 and the expected text

  Scenario: User columns filled in content mode
    Given a sheet with a value in column J of row 7
    When it is uploaded in CONTENT_PLATFORM mode
    Then rule V-04 drops the value in J7 with warning LDC-TPL-013
    And row 7 remains submittable without any user-column data

  Scenario: Near-miss vocabulary suggestion
    Given 14 cells in column H read "Half-Yearly"
    Then the preview offers "Apply 'Half Yearly' to 14 cells" and the fix is recorded as an importer correction

  Scenario: Round trip by CompID
    Given an exported instrument with 120 checkpoints
    When the tenant CCO edits 3 questions offline and re-imports in OVERLAY mode
    Then the diff shows exactly 3 CHANGED rows and 117 UNCHANGED
    And 3 overlay drafts await approval by a different user

Feature: Base content vs tenant overlay
  Scenario: Auto-rebase
    Given a tenant overlay on field G of checkpoint X at base version 2
    When a release changes only field Q of X to version 3
    Then the overlay is rebased to version 3 and the effective G is still the tenant's wording

  Scenario: Rebase conflict
    Given a tenant overlay on field G of checkpoint Y
    When a release changes field G of Y
    Then one REBASE_CONFLICT review task is created for the tenant
    And the tenant's wording stays in force until resolved
    And completed compliance instances of Y still show the text that applied when completed

Feature: Regulation catalogue
  Scenario: Remove an applicable instrument
    Given the engine marks instrument Z as Applicable to the tenant
    When the tenant admin unticks Z with reason "COVERED_BY_GROUP_ENTITY"
    Then a second approval from the CCO is required
    And after approval future instances stop but completed instances and evidence remain (NN-29)

Feature: Corrections
  Scenario: Super admin corrects a published citation
    When a super admin proposes a Correction Entry changing clause ref 12(3) to 12(4)
    Then a second platform approver must approve
    And the previous version remains readable with a "Corrected" banner (NN-02)
```

NN tests: `NN-01_cross_tenant_overlay_invisible`, `NN-02_published_checkpoint_no_inplace_update`, `NN-03_release_does_not_overwrite_overlay`, `NN-04_ai_enrichment_requires_acceptance`, `NN-05_checker_not_maker_on_import`, `NN-06_release_blocks_uncited_rows`, `NN-07_completed_instance_pins_version`, `NN-29_removal_keeps_history`.

---

## 13. Deliverables and exit gate

1. `cnt` and `tpl` schemas, migrations (expand-contract), RLS policies and seed authorities/jurisdictions/calendars.
2. Template Registry loaded with every family in Appendix E (S2's 24 templates) and their vocabularies; blank templates downloadable.
3. Importer with all four modes, V-rules, preview, error workbook, diff, review and idempotency; performance targets in FR-P03-37 met.
4. Content Studio grid with source pane, lint (L-rules) and coverage report.
5. Release pipeline with scheduling, events and fan-out rebase.
6. Tenant overlays, tenant checkpoints, conflict review, lineage view.
7. Regulation Catalogue with recommended set, adoption preview, removal with second approver.
8. Department/function mapping and terminology.
9. Applicability interface wired to a stub evaluator (real rules from P15).
10. Migration of legacy MongoDB banks and the 9 RBI NBFC MD sheets (460–468) plus the IFSCA sheets into DRAFT, with a migration quality report.
11. All §12 scenarios and NN tests green; accessibility audit of SCR-CNT-10/03 and SCR-TPL-02 passes WCAG 2.2 AA.
12. Contribution to Appendix B (DDL), C (screens), U (settings) and F (events) registered.

---

## 14. Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P03-01 | `_LDC_System` hidden sheet in exports | Not in D-08; needs S2/owner confirmation | Product owner | Without it, system fields round-trip by CompID from the database |
| OI-P03-02 | Multi-value separator in column D | Owner's IFSCA command allows several entities; Excel list validation allows one | S2 / owner | Resolved in review: templates keep the owner's `showErrorMessage = false` on the list validations so several values can be typed; the importer enforces vocabularies from the registry (Appendix E §E.4.2) |
| OI-P03-03 | Canonical RBI website | `website.rbi.org.in` URLs redirect to `rbi.org.in` as of 25-Oct-2026 | Content lead | Store both; P05 monitors both [VERIFY] |
| OI-P03-04 | IRDAI canonical document site | Circular listings observed on `policyholder.gov.in` (IRDAI-owned) | Content lead | Monitor irdai.gov.in and policyholder.gov.in [VERIFY] |
| OI-P03-05 | Licensed third-party content | Whether to license any feed for global packs | Owner | `CONTENT_FEED_PORT` OFF |
| OI-P03-06 | Clause-index quality for scanned instruments | OCR on older state co-op and labour notifications | Content lead | Manual clause entry; V-09 downgraded to warning for TENANT and flagged instruments |
| OI-P03-07 | Re-verification cadence | 12/6 months proposed | Content lead | Setting `cnt.quality.reverify_months` |
| OI-P03-08 | Legacy beta tenant texts | Branch International beta question variants | Product owner | Preserve as overlays pinned to migrated base |

---

## 15. Sources (accessed 25 October 2026)

1. Reserve Bank of India — home navigation (Notifications, Master Directions, Master Circulars, Amendment Directions, Draft Directions RE-wise, Circulars Withdrawn, Regulatory Reporting): https://www.rbi.org.in/ ; Master Directions listing: https://www.rbi.org.in/Scripts/BS_ViewMasterDirections.aspx
2. JSA, "KM Newsflash – RBI Master Directions", 29 November 2025 (238 function-wise Master Directions; 11 RE categories; naming convention; savings clause): https://www.jsalaw.com/wp-content/uploads/2025/11/KM-Newsflash-RBI-Master-Directions.pdf
3. Taxscan, "RBI issues 238 consolidated Master Directions; 9,000 circulars reorganised", 3 December 2025: https://www.taxscan.in/top-stories/rbi-issues-238-consolidated-master-directions-9000-circulars-guidelines-reorganised-1439158
4. IFSCA — New Section listing: https://ifsca.gov.in/Home/NewSection
5. SEBI RSS: https://www.sebi.gov.in/rss.html
6. Owner's sample workbooks: "SAMPLE - Finance Company Regulations 2021 - Compliance Questions.xlsx"; "05 Insurance - IFSCA Appointed Actuary Regulations 2022.xlsx" (both: Sheet1 + Rough; named ranges IFSCA_Freq, IFSCA_Sector, IFSCA_Entity, IFSCA_Dept, IFSCA_CompType, IFSCA_Risk; DV rows 3–345/320).
7. Infrabyx Ecosystem Integration Specification v1.1, §9.1–§9.4 (compliance-mode switch, Generic GRC connector, LawDocsComply native connector, OSCAL).
8. Lawrbit, "GCMS India — Solution Overview" (2024): https://www.lawrbit.com/wp-content/uploads/2024/07/solution-overview-gcms-india.pdf
9. TeamLease RegTech, Statutory & Regulatory Compliance Management Software: https://teamleaseregtech.com/product-services/statutory-regulatory-compliance-management-software/
10. Lexplosion (Komrisk) compliance management software: https://lexplosion.in/compliance-management-software/
11. Google, Common Expression Language specification: https://github.com/google/cel-spec [REC]

---

## 16. Master integration notes (pack lead, 25 October 2026)

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-34, NN-35; X-08 (delimiter "; "), X-09 (template and data-template codes), X-10, X-12 (cite the 31 Jul 2026 DoS directions), X-28 (`_LDC_System` export sheet, owner to confirm), X-29, X-38 (canonical IFSCA vocabulary)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).

