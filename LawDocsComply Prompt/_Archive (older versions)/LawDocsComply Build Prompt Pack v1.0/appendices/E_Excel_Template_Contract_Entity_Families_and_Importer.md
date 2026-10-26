# Appendix E — Excel Template Contract, Entity Families and Importer

> **Binding specification.** It is cited by P03 (Regulatory Content Library, Template Registry and Excel Import), P05 (Regulatory Change Management and AI Question Authoring), P04 (Compliance Workspace: tenant view of imported rows), P15 (Sector Packs: entity taxonomy) and P19 (export round trip).
> **Prepared:** 25 October 2026 by stream S2.
> **Precedence:** For anything about the question workbook's layout, columns, vocabularies, the importer's validation and its error codes, this appendix prevails over any phase file. Appendix B prevails on table and column names, and Appendix G on the legal content itself.
> **Requirements covered:** R-004, R-017, R-084, R-085, R-086, R-087, R-088, R-102 (and supports R-006, R-007, R-013, R-021).
> **Deliverables referenced:** `templates/` (24 family workbooks, validator, validation report) and `part2_prompts/` (master command, 24 family commands, QA checklist).

---

## E.0 Purpose and the decision behind it

LawDocsComply's regulatory content arrives as Excel question sheets. The owner and Claude Cowork write them in Part 2, one workbook per master direction, regulation, circular, guideline or Act. Super admin uploads them to the platform-wide content library, and a client admin can upload them for its own company only.

Management decided on 25 October 2026 (D-08) as follows:

- The owner's existing layout is kept exactly: `Sheet1` with row 1 group headers and row 2 column headers in columns A–AD, plus the `Rough` list sheet with named ranges.
- Only the dropdown values change by entity family.
- A protected `_Template_Info` sheet is added so the importer can identify and validate a file automatically.

Three consequences follow:

1. **The workbook is a versioned ingestion contract, not a schema to be guessed.** Every family template has a code (`LDC-TPL-<FAMILY>-v<major.minor>`), a header hash and a vocabulary version held in the template registry (`tpl` schema).
2. **Uniform experience.** All 24 families share the same 30 columns, the same base vocabularies and the same import behaviour. Families only **add** values. They never rename or remove base values, so departments, frequencies, compliance types and risk read the same everywhere.
3. **No silent change.** An upload never publishes directly. It produces a preview with row-level issues and, for re-uploads, a field-level diff. Publication then goes through maker ≠ checker approval (NN-04, NN-05). A tenant upload produces a tenant overlay and never changes base content (NN-03).

---

## E.1 Design principles

| # | Principle | How it is enforced |
|---|---|---|
| P1 | Rows 1–2 and columns A–AD are immutable | Header SHA-256 compared with the registry (LDC-TPL-003/004/005) |
| P2 | Vocabulary lives in the registry, not only in `Rough` | The importer validates against `tpl.vocab_values` for the template version. A tampered `Rough` has no effect (LDC-TPL-015) |
| P3 | Owner's established conventions are canonical | "; " is the multi-value delimiter in D (found in 2,809 owner rows); " \| " separates parts in N; list tokens start P |
| P4 | Structured data without new columns | Due-date rules go in P after `Due:`; retirement uses the `[RETIRED] ` prefix in F; CompID uses E |
| P5 | Lossless round trip | Export → edit → re-import reproduces the same obligations. The diff is keyed on CompID (§E.9) |
| P6 | Platform base vs tenant overlay | The super-admin import writes `cnt` base versions. The client-admin import writes `cmp` overlays scoped to `tenant_id` (§E.10) |
| P7 | AI never publishes | AI-generated sheets use the same template and the same importer, and need the same approvals (§E.11; NN-04) |
| P8 | Excel is untrusted input | Macro-free `.xlsx` only, formula neutralisation, size limits, malware scan (§E.14) |
| P9 | Backward compatibility | Old template versions stay importable until retired. Vocabulary values are never deleted, only end-dated (§E.6) |

---

## E.2 Workbook structure (all families)

| Element | Specification |
|---|---|
| File type | `.xlsx` (OOXML, no macros). `.xlsm`, `.xls`, `.xlsb`, `.csv` and password-protected files are rejected (LDC-TPL-001) |
| Sheet order | `Sheet1` (data), `Rough` (lists), `_Template_Info` (identity). Names are case-sensitive and must not be renamed (LDC-TPL-002) |
| Sheet1 row 1 | Group headers, merged: A1:J1 "List", K1:S1 "Details", T1:W1 "Maker" (X1 styled Maker, not merged), Y1:AB1 "Checker", AC1:AD1 "Auditor". Fills: yellow FFFF00, blue 00B0F0, green 47D359, red FF0000, amber FFC000 |
| Sheet1 row 2 | The 30 headers exactly as in §E.3 (Times New Roman 12 bold, wrapped; H2 contains a line break "Due date & \nFrequency") |
| Freeze panes | A3 |
| Data rows | From row 3. Pre-formatted rows 3–1000 (Times New Roman 10, wrap, top-aligned, thin borders). List validations cover rows 3–2000. Instruments needing more than 2,000 rows are split into Part A/Part B files (LDC-TPL-009) |
| Validations | `list` type on C, D, H, M, O, R and P, each pointing to a family-prefixed named range. `showErrorMessage = false` (the owner's setting), so several values can be typed in C and D and P can carry detail. The importer, not Excel, enforces the vocabulary |
| Named ranges | `<PREFIX>_Freq` (H), `<PREFIX>_Sector` (C), `<PREFIX>_Entity` (D), `<PREFIX>_Dept` (M), `<PREFIX>_CompType` (O), `<PREFIX>_Risk` (R), `<PREFIX>_Filing` (P). The keys `Sector` and `Entity` are generic names for Columns C and D, kept from the owner's IFSCA convention, even where C means layer, tier or law |
| `Rough` | Sections in the order Freq, C, D, Dept, CompType, Risk, Filing. Each section is a bold header followed by its values and terminated by one blank row. IFSCA-GEN keeps the owner's `Rough` byte-identical |
| `_Template_Info` | Protected sheet (§E.5) |
| Document properties | Title = template code. Custom properties `LDC_TemplateCode`, `LDC_TemplateVersion`, `LDC_Family`, `LDC_HeaderSHA256` |

---

## E.3 Column contract

"First upload" means a new instrument or a new tenant question set. "Re-upload" means a file previously exported from LawDocsComply with E filled. "Owner" is the party responsible for the cell's content.

| Col | Row-2 header (exact) | Owner | First upload | Re-upload | Type / length | Validation | Maps to |
|---|---|---|---|---|---|---|---|
| A | Checkbox | System | Blank | Ignored | — | Dropped with LDC-TPL-013 (warning) if filled | — (UI selection only) |
| B | Serial No. | Writer | Required | Required | Integer 1..2000 | Unique, contiguous (LDC-TPL-014) | `cnt.obligation_versions.sequence_no` |
| C | General Applicability(Layer) | Writer | Required | Required | Text ≤ 500; one or more values separated by "; " | Family list C (LDC-TPL-015) | `cnt.obligation_applicability(axis='C')` → taxonomy codes |
| D | General Applicability(Type) | Writer | Required | Required | Text ≤ 1,000; "; "-separated | Family list D (LDC-TPL-015/016) | `cnt.obligation_applicability(axis='D')` |
| E | CompID | System | **Blank** | **Required, unchanged** | `<FAMILY>.<INST>.<NNNN>` or `T-<TEN>.<INST>.<NNNN>` | LDC-TPL-022/023/024 | `cnt.obligations.comp_id` |
| F | Short Title | Writer | Required | Required | ≤ 200; may start `[RETIRED] ` | LDC-TPL-012/027/025 | `obligation_versions.short_title`; retire flag |
| G | Compliance Question/Actionable | Writer | Required | Required | ≤ 2,000 | LDC-TPL-012/027 | `obligation_versions.question_text` |
| H | Due date & \nFrequency | Writer | Required | Required | List value | Family list H (LDC-TPL-015/019) | `cnt.schedule_rules.frequency_code` |
| I | Date of Compliance | User | Blank | Ignored | — | LDC-TPL-013 | (tenant `cmp.compliance_instances`) |
| J | Status | System | Blank | Ignored | — | LDC-TPL-013 | (workflow state) |
| K | Clause or Para no. | Writer | Required | Required | ≤ 500 | Citation parse (LDC-TPL-020) | `cnt.clauses` link + `obligation_versions.citation_text` + `obligation_ref` |
| L | Interpretation/Explanation | Writer | Required | Required | ≤ 8,000 | LDC-TPL-012 | `obligation_versions.explanation` |
| M | Department | Writer | Required | Required | List value | Family list M | `obligation_versions.department_code` (canonical) |
| N | Related Document or Compliance or Weblinks, if any | Writer | Optional | Optional | ≤ 4,000; parts " \| " | URL lint (LDC-TPL-028) | `cnt.obligation_references[]` |
| O | Compliance Type | Writer | Required | Required | List value | Family list O | `obligation_versions.compliance_type_code` |
| P | Filing and Reporting details/Intimation | Writer | Required | Required | ≤ 1,000; grammar §E.4.3 | LDC-TPL-017/018 | `cnt.filing_requirements` + `schedule_rules.due_rule` |
| Q | Consequences of Non-Compliance/Penalty/Impact | Writer | Required | Required | ≤ 4,000 | LDC-TPL-012 | `obligation_versions.consequence_text` |
| R | Risk Categorization | Writer | Required | Required | High/Medium/Low | LDC-TPL-015/030 | `obligation_versions.risk_code` (seeds ERM linkage, P08) |
| S | Conditional Applicability/Exemptions | Writer | Required | Required | ≤ 4,000 | LDC-TPL-012 | `obligation_versions.conditions_text` (+ structured conditions added in Content Studio) |
| T | Maker User/Email ID | System | Blank | Ignored | — | LDC-TPL-013 | (tenant assignment) |
| U | Upload Document or Evidence | Writer | Required | Required | ≤ 2,000 | Generic-text lint (LDC-TPL-029) | `cnt.evidence_requirements[]` |
| V | Control Activity | Writer | Required | Required | ≤ 4,000 | LDC-TPL-012 | `obligation_versions.control_activity` (seeds `erm` control library) |
| W | Status Update by Maker User | User | Blank | Ignored | — | LDC-TPL-013 | tenant |
| X | Comments, if any, by Maker User | User | Blank | Ignored | — | LDC-TPL-013 | tenant |
| Y | Checker User/Email ID | System | Blank | Ignored | — | LDC-TPL-013 | tenant |
| Z | Filing/Compliance Date | User | Blank | Ignored | — | LDC-TPL-013 | tenant |
| AA | Review- Approve, Reject, Reallocate | System | Blank | Ignored | — | LDC-TPL-013 | tenant |
| AB | Comments, if any, by Checker User | User | Blank | Ignored | — | LDC-TPL-013 | tenant |
| AC | Assigned Auditor/Email ID | System | Blank | Ignored | — | LDC-TPL-013 | tenant |
| AD | Comments, if any, by Auditor | User | Blank | Ignored | — | LDC-TPL-013 | tenant |

**Tenant working exports.** A tenant's own working export (Appendix M, LDC-EXPORT-1.0) fills columns I, J, T and W–AD with that tenant's compliance data. If such a file is re-imported as content, those columns are ignored with LDC-TPL-013 (info). Tenant workflow data is never imported through the content importer. Bulk status updates use the separate workspace bulk-update tool (P04).

---

## E.4 Value conventions and parsers

### E.4.1 Normalisation (applied to every cell before validation)

The following steps run in this order:

1. Convert to Unicode NFC.
2. Trim leading and trailing whitespace.
3. Collapse runs of spaces.
4. Convert curly quotes to straight quotes, but only inside list values; free text is untouched.
5. Remove non-printing control characters except line feed (LDC-TPL-032, info).
6. Remove zero-width characters.

A cell whose value starts with `=`, `+`, `-` or `@` and is a formula, or is formula-like text, is stored as text with a leading apostrophe removed. It is flagged LDC-TPL-011 (warning). It is never evaluated (§E.14).

### E.4.2 Multi-value columns (C and D)

- The canonical delimiter is `"; "`.
- The importer also accepts `" | "`, `","`, `";"` and line breaks. It normalises them to `"; "` and raises LDC-TPL-016 (info).
- Each token is matched case-insensitively against the family list. A token that does not match fails with LDC-TPL-015 (error), and the preview suggests the nearest list value (Levenshtein ratio ≥ 0.85).
- A family's "All … (ALL)" token expands to every taxonomy code of that axis at evaluation time. It is not expanded in storage, so new entity types added later inherit the obligation unless content excludes them.

### E.4.3 Column P grammar

```
P        := token [ " — " detail ] [ " — " due ] | token " — " due
token    := <a value from the family Filing list, exact>        (else LDC-TPL-017)
detail   := free text (form / return name / portal step), no " — Due:" inside
due      := "Due: " rule
```

The em dash "—" is canonical. The importer also accepts " - " and " – " before `Due:` and normalises them.

### E.4.4 Due-rule mini-language (inside `Due:`)

Writers use plain English. The parser recognises the patterns below and turns each into a structured `cnt.schedule_rules` row. A rule the parser cannot read is kept as text and flagged LDC-TPL-018 (warning). The content maker then sets the structured rule in Content Studio before the obligation can be published.

| Pattern (case-insensitive) | Structured rule |
|---|---|
| `within N (calendar \| working \| business)? days (of \| from) the end of (each)? (month \| quarter \| half-year \| financial year \| calendar year)` | `anchor=PERIOD_END(period); offset=+N days (calendar default)` |
| `by the Nth (day)? of the (following \| next) month` | `anchor=PERIOD_END(month); day_of_next_month=N` |
| `within N days (of \| from) <event>` | `anchor=EVENT(<event key>); offset=+N` (the event key is chosen in Content Studio from the event catalogue, for example `appointment`, `change_in_director`, `breach_detected`) |
| `within N hours (of \| from) <event>` | `anchor=EVENT; offset=+N hours` |
| `on or before DD Month` / `by DD Month (each year)?` | `anchor=FIXED_ANNUAL(DD-MM)` |
| `within six months of the close of the financial year` (words or digits) | `anchor=PERIOD_END(FY); offset=+6 months` |
| `before <event>` | `anchor=EVENT; offset=-0 (must precede)` |
| `immediately` / `forthwith` / `without delay` | `anchor=EVENT; offset=0; urgency=IMMEDIATE` |
| `as specified by <authority>` | `anchor=MANUAL` (date entered by the tenant per instance) |

Before publication, the content maker reconciles H and the structured rule. For example, H = "Quarterly" with a monthly anchor raises LDC-TPL-019 (warning). Due dates that fall on holidays follow the tenant's holiday calendar setting `cmp.calendar.holiday_shift` (P04).

### E.4.5 Citation parsing (K)

The parser extracts structured references using regulator patterns:

- `Section`
- `Rule`
- `Regulation` / `Reg.`
- `Para` / `Paragraph`
- `Clause`
- `Chapter`
- `Annex` / `Schedule`
- `read with`
- `as substituted | inserted | amended vide <notification> dated <date>`

Each reference becomes a `cnt.clauses` link (instrument version, clause path such as `12(3)(a)`) and an `obligation_ref` in the Ecosystem Spec format `<instrument_ref>#<clause_path>`, for example `RBI/DoS/2026-27/460#14(2)`.

- An unparseable K is kept as text with LDC-TPL-020 (warning).
- A clause path that does not exist in the instrument's clause tree, where one has been loaded, is flagged for the reviewer.

### E.4.6 Weblinks (N)

N is split on `" | "`. Recognised prefixes are `INCORPORATES:`, `SUPERSEDES:` and `read with`. URLs are extracted and checked against the official-domain allowlist:

- rbi.org.in, website.rbi.org.in
- sebi.gov.in
- ifsca.gov.in
- irdai.gov.in
- mca.gov.in
- egazette.gov.in
- indiacode.nic.in, legislative.gov.in
- meity.gov.in
- labour.gov.in
- cooperation.gov.in, crcs.gov.in
- cert-in.org.in
- gst.gov.in, cbic.gov.in
- incometax.gov.in
- nhb.org.in, nabard.org
- eur-lex.europa.eu
- cppa.ca.gov, oag.ca.gov

The list is kept in setting `tpl.import.official_domains` (G). Other domains raise LDC-TPL-028 (warning). URLs are stored as references and are never fetched during import (§E.14).

### E.4.7 Markers

| Marker | Where | Meaning | Importer action |
|---|---|---|---|
| `[RETIRED] ` | Start of F | The provision was omitted or repealed | Re-upload only: creates a retire action. S must cite the omitting instrument (LDC-TPL-025) |
| `[VERIFY]` | Any content cell | The writer could not confirm a fact | LDC-TPL-026 (warning). Publication is blocked until the checker resolves it (removes the marker) or records a waiver with reason |
| `[INTERP]`, `[REC]`, `[LAW]` | L, S | Writer's annotation | Kept as text; shown as a badge in the UI |

---

## E.5 `_Template_Info` specification

| Field (column A label) | Value (column B) | Use |
|---|---|---|
| Template code | `LDC-TPL-<FAMILY>-v<major.minor>` | Registry lookup (LDC-TPL-006) |
| Template version | `1.0` | Compatibility (§E.6) |
| Family code / Family name | e.g., `RBI-NBFC` / `Non-Banking Financial Companies (all layers and types)` | Upload dialog default; family mismatch check (LDC-TPL-008) |
| Regulator / authority | Text | Display |
| Built on | ISO date | Display |
| Base layout | Text | Display |
| Data sheet / List sheet | Names and named-range prefix | Display |
| Row-2 header SHA-256 | 64 hex characters | Integrity check (LDC-TPL-004) |
| Row-1 header SHA-256 | 64 hex characters | Integrity check (LDC-TPL-003) |
| Hash method | SHA-256 over the UTF-8 bytes of the 30 cell values A..AD joined with U+001F; an empty cell is an empty string | Reproducible |
| Multi-value delimiter | `"; "` | Display |
| Data rows | Row-range rule | Display |
| Importer contract / Part-2 command | Pointers | Display |
| Instruments list | Bullet list | Guidance |
| Column contract table | 30 rows: Column, Row-1 group, Row-2 header, Filled by, At upload, Rule | Guidance; mirrors §E.3 |
| Part-2 instructions | 9 numbered steps | Guidance |
| Worked example row | One illustrative row, shown vertically | Guidance; never imported |

Protection and integrity:

- The sheet is protected with the documented password `LDC-TPL`. The password prevents accidental edits; it is not a security control.
- The importer trusts the registry, not the sheet. If `_Template_Info` has been edited but the template code and header hash still match the registry, the import proceeds and LDC-TPL-006 is raised as info.
- The canonical row-2 hash for all v1.0 templates is `07b3352ef2485d93ac22a299ba840aa76a2577e84b219fba6a48281eb24d5310`. All 24 families share it, because rows 1–2 are identical.

---

## E.6 Template registry and versioning

**Tables (schema `tpl`; owned by P03, DDL in Appendix B):**

- `tpl.template_families(code PK, name, regulator_code, c_axis_label, d_axis_label, taxonomy_axis_c, taxonomy_axis_d, status)`
- `tpl.templates(id, family_code FK, version, code UNIQUE, header_sha256, row1_sha256, base_file_object_key, vocab_version_id FK, status ENUM('draft','active','deprecated','retired'), valid_from, valid_to, created_by, approved_by)`
- `tpl.vocab_versions(id, family_code, version, published_at, approved_by)`
- `tpl.vocab_values(id, vocab_version_id, list_key ENUM('FREQ','C','D','DEPT','COMPTYPE','RISK','FILING'), value_text, canonical_code, sort_order, is_base BOOL, aliases TEXT[], valid_from, valid_to)`
- `tpl.import_jobs`, `tpl.import_rows`, `tpl.import_issues` (§E.7)

**Version rules.**

- **Patch (v1.0 → v1.0.1):** the `_Template_Info` text or instructions change. The file stays compatible and the importer accepts both.
- **Minor (v1.0 → v1.1):** vocabulary values are **added**, or aliases are added. Old files stay valid. Values are never removed in a minor version. A superseded value is end-dated (`valid_to`) and given an alias that maps it to its replacement. Old content keeps the old value's canonical code, and the UI shows the successor.
- **Major (v1.x → v2.0):** a column or header changes. This needs management approval, because rows 1–2 are the owner's contract.
  - v1.x files stay importable for at least 12 months after v2.0 is active, through a column mapping held in `tpl.templates.column_map`.
  - A major version is the only way to change rows 1–2.
- A deprecated template still imports, with LDC-TPL-007 as a warning. A retired template is rejected with LDC-TPL-007 as an error and a download link to the current template.

**Adding a family.**

1. The content maker drafts the family: the C and D axes mapped to entity-taxonomy codes (P15) and the vocabulary.
2. The content checker approves it.
3. The template builder generates the workbook from the base layout.
4. The workbook is validated with `_validate_templates.py`, and the result is published in the template catalogue.

No code release is needed. The build and validate scripts run as a platform job (P03 §7.5).

**Tenant vocabulary extensions.** A tenant can add values only to its own overlay vocabulary, for example a department it calls "Secretarial & Legal", or an internal compliance type. These are stored in `cfg.tenant_vocab_values`, mapped to a canonical code and used only in that tenant's uploads and exports. A value not registered for the tenant fails with LDC-TPL-035.

---

## E.7 Importer validation pipeline and error codes

### E.7.1 Pipeline

1. **Receive.** Upload via Content Studio (super admin) or Compliance Library → My Instruments → Import (client admin), or via `POST /v1/content/imports` (multipart). The importer records the file SHA-256, the uploader, the scope (`platform` or `tenant:<id>`) and the target instrument version. The target is chosen or created in the upload dialog: authority, title, reference number, dates and the "as amended up to" date.
2. **Quarantine scan.** The file goes through the malware scan and an OOXML structure check:
   - zip-bomb ratio below 100:1
   - no `vbaProject.bin`, external links, DDE, OLE objects or ActiveX
   - no XML DTD or XXE

   A failure gives LDC-TPL-010 or LDC-TPL-038.
3. **Structure.** The importer checks the sheets (002), row 1 and the merges (003), the row-2 hash (004), columns A–AD with nothing hidden (005), `_Template_Info` and the registry code (006), the template status (007), the family against the chosen instrument (008), the row count (009), at least one data row (033), no merged cells in the data area (040), and hidden rows or filters (039).
4. **Row parse and normalise** (§E.4).
5. **Row validation.** Required cells (012), system and user columns (013), serial numbers (014), vocabularies (015, 016), P grammar (017), Due rules (018, 019), citations (020), lengths (027), markers (025, 026), weblinks (028), evidence lint (029).
6. **Cross-row validation.**
   - Duplicates: same K and question similarity ≥ 0.92 by token cosine (021).
   - Risk skew (030).
   - Row count against the clause tree, where one is loaded (031).
7. **Re-upload reconciliation** (§E.9). CompIDs are checked (022, 023, 024), and each row is classified as NEW, UPDATE, RETIRE or NOCHANGE.
8. **Optional AI lint** (flag `tpl.import.ai_lint.enabled`, default OFF until P17 evaluation passes). Vidhi checks each row for:
   - a question that does not match the citation
   - a missing numeric element
   - generic evidence
   - a prohibition phrased as a permission

   Results appear as **suggestions** only; they never block an import or change a row (NN-14).
9. **Preview.** This screen is `SCR-TPL-03`, specified in P03. It shows:
   - totals by severity
   - row grid with issue badges
   - filters by issue code
   - for re-uploads, a side-by-side diff
   - downloadable "issues workbook": the uploaded file with a new `_Import_Issues` sheet and cell comments. It is corrected and re-uploaded.
10. **Commit.** This step is allowed only when there are no errors. The rows are written as **draft** obligation versions in the instrument version's draft release.
11. **Publish.** This is a separate maker ≠ checker approval (P03/P05). It sets `valid_from` and triggers the tenant-impact workflow (P05) and **Updates** notices (NN-27).

The import job is idempotent on (scope, instrument version, file SHA-256). Re-submitting the same file returns the existing job.

### E.7.2 Error code register

Severity has three levels:

- **E** (error) blocks commit.
- **W** (warning) allows commit and needs acknowledgement. [VERIFY]-marked rows also block publish until they are resolved.
- **I** (info) is shown in the preview only.

| Code | Sev | Meaning | User message |
|---|---|---|---|
| LDC-TPL-001 | E | Not a macro-free, unencrypted .xlsx | "Upload an .xlsx file saved from the LawDocsComply template (no macros, no password)." |
| LDC-TPL-002 | E | Sheet missing, renamed or reordered | "The workbook must contain Sheet1, Rough and _Template_Info in that order. Download the template again." |
| LDC-TPL-003 | E | Row-1 group headers or merged ranges changed | "Row 1 of Sheet1 was changed. Rows 1–2 cannot be edited." |
| LDC-TPL-004 | E | Row-2 header hash mismatch | "The column headers in row 2 were changed (column {col}: expected '{exp}'). Restore them from the template." |
| LDC-TPL-005 | E | Columns inserted, deleted or hidden, or data beyond AD | "Columns must run from A to AD exactly, with none hidden." |
| LDC-TPL-006 | E/I | `_Template_Info` missing, or template code unknown (E); sheet edited but code and hash valid (I) | "This file does not carry a LawDocsComply template code. Use a template from Content Studio → Templates." |
| LDC-TPL-007 | W/E | Template version deprecated (W) or retired (E) | "Template {code} is {status}. Download {current} and copy your rows into it." |
| LDC-TPL-008 | E | Template family does not match the chosen instrument's family | "This is a {family} template but the instrument belongs to {instFamily}." |
| LDC-TPL-009 | E | More than 2,000 data rows, or file over 25 MB | "Split the instrument into Part A and Part B files of up to 2,000 rows." |
| LDC-TPL-010 | E | Active content, external links, embedded objects or malware | "The file contains macros, links or embedded objects and was rejected for security." |
| LDC-TPL-011 | W | Formula or formula-like value in a content cell | "Cell {cell} contained a formula; it was stored as plain text." |
| LDC-TPL-012 | E | Required content cell empty | "Row {row}: column {col} ({header}) is required." |
| LDC-TPL-013 | W/I | System or user column not blank | "Row {row}: column {col} is filled by the software; the value was ignored." |
| LDC-TPL-014 | W | Serial number gap, duplicate or non-integer | "Serial numbers are not 1..n; renumber automatically?" |
| LDC-TPL-015 | E | Value not in the family vocabulary (C, D, H, M, O, R) | "Row {row}: '{value}' is not a {list} value for {family}. Did you mean '{suggestion}'?" |
| LDC-TPL-016 | I | Non-canonical delimiter normalised | "Row {row}: values in column {col} were separated with '; '." |
| LDC-TPL-017 | E | Column P does not start with a Filing-list token | "Row {row}: column P must start with a filing destination from the list (or 'Not Required')." |
| LDC-TPL-018 | W | `Due:` rule not machine-readable | "Row {row}: the due-date rule will need to be set in Content Studio before publishing." |
| LDC-TPL-019 | W | Frequency (H) inconsistent with the Due rule | "Row {row}: frequency '{H}' does not match the due rule '{rule}'." |
| LDC-TPL-020 | W | Citation (K) could not be parsed, or does not exist in the clause tree | "Row {row}: the clause reference could not be matched to the instrument text." |
| LDC-TPL-021 | W | Probable duplicate obligation | "Rows {a} and {b} look like the same obligation." |
| LDC-TPL-022 | E | Unknown CompID on re-upload | "Row {row}: CompID {id} does not exist. Clear column E for new rows." |
| LDC-TPL-023 | E | Exported CompID missing (row deleted) | "CompID {id} is missing. Do not delete rows; mark omitted provisions with [RETIRED] in column F." |
| LDC-TPL-024 | E | CompID belongs to another instrument or another tenant | "Row {row}: CompID {id} belongs to a different instrument or organisation." |
| LDC-TPL-025 | E | `[RETIRED]` row without the omitting reference in S, or on a first upload | "Row {row}: give the omitting notification and date in column S." |
| LDC-TPL-026 | W | `[VERIFY]` marker present | "Row {row} contains [VERIFY]; it cannot be published until verified or waived." |
| LDC-TPL-027 | E | Text longer than the column limit | "Row {row}: column {col} exceeds {n} characters." |
| LDC-TPL-028 | W | Non-official URL in N | "Row {row}: {domain} is not an official source; keep it only as secondary reference." |
| LDC-TPL-029 | W | Generic evidence text in U | "Row {row}: name the specific document that proves compliance." |
| LDC-TPL-030 | I | More than 70% of rows rated High | "{pct}% of rows are High risk; check the calibration rule." |
| LDC-TPL-031 | I | Row count unusual compared with the clause tree | "{n} operative clauses have no row." |
| LDC-TPL-032 | I | Control or zero-width characters removed | — |
| LDC-TPL-033 | E | No data rows | "The sheet has no rows from row 3." |
| LDC-TPL-034 | E | Tenant upload tries to change a base obligation | "This question belongs to the LawDocsComply library. Your change will be saved as your company's version." (offers overlay) |
| LDC-TPL-035 | E | Tenant vocabulary value not registered | "'{value}' is not one of your company's {list} values. Add it in Settings → Compliance vocabulary." |
| LDC-TPL-036 | E | A newer version of the instrument is already published | "A newer version ({v}) is published. Export it and edit that instead." |
| LDC-TPL-037 | E | Another import for the same instrument version is open | "An import is already in review for this instrument." |
| LDC-TPL-038 | E | Corrupt or unreadable file | "The file could not be read." |
| LDC-TPL-039 | W | Hidden rows or active filters in Sheet1 | "Hidden or filtered rows were found; all rows were imported." |
| LDC-TPL-040 | E | Merged cells in the data area | "Unmerge cells in rows 3 onwards." |

Every error code is registered in Appendix B's error register with the HTTP mapping `422 Unprocessable Entity` for E-level failures returned by `POST /v1/content/imports/{id}:validate`.

---

## E.8 Mapping to the regulatory content model (`cnt`)

```
Instrument (cnt.instruments)                  authority, family_code, title, ref_no, issue_date, status
 └── InstrumentVersion (cnt.instrument_versions)  as_amended_upto, effective_from, source_files[], sha256, supersedes[]
      ├── Clause tree (cnt.clauses)           path, heading, text, hash (from OCR/text extraction, P03)
      └── Obligation (cnt.obligations)         comp_id (stable), family_code, origin ('platform'|'tenant'), created_from_import
           └── ObligationVersion (bitemporal)  sequence_no(B) short_title(F) question_text(G) citation_text(K) obligation_ref
                                               explanation(L) department_code(M) references(N) compliance_type_code(O)
                                               consequence_text(Q) risk_code(R) conditions_text(S) control_activity(V)
                                               valid_from/valid_to (law time) · recorded_at/superseded_at (system time)
                ├── Applicability (axis C, D → taxonomy codes; structured conditions added in Content Studio)
                ├── ScheduleRule (H frequency_code + Due rule)
                ├── FilingRequirement (P token → destination_code; detail; portal)
                └── EvidenceRequirement[] (U split on ";" into artefacts with type hints)
```

**CompID format.**

- Platform obligations use `<FAMILY>.<INST>.<NNNN>`, for example `RBI-NBFC.GOV25.0012`, where:
  - `<INST>` is the instrument short key, at most 8 characters, set at instrument creation and immutable
  - `NNNN` is a sequence that is never reused
- Tenant-authored obligations use `T-<TENANTKEY>.<INST>.<NNNN>`.

The CompID is shown to users, printed on exports, used in audit trails and carried into the Ecosystem Spec `compliance_obligation` resource as `comp_id` alongside the `obligation_ref`. Internal primary keys are ULIDs.

**Applicability.** C and D tokens map to `pack.entity_taxonomy` codes through `tpl.vocab_values.canonical_code`, for example:

- "Middle Layer (NBFC-ML)" → `RBI.NBFC.LAYER.ML`
- "NBFC-Investment and Credit Company (NBFC-ICC)" → `RBI.NBFC.TYPE.ICC`

An obligation applies to a tenant legal entity when that entity's profile holds at least one C code **and** at least one D code, and any structured conditions are true. Structured conditions include thresholds, effective dates and State, and are added in Content Studio from Column S. Applicability is explainable: the tenant sees "Applies because: Middle Layer; NBFC-ICC; asset size ₹1,200 crore ≥ ₹1,000 crore" (P15).

**Department.** Values map to canonical department codes, as listed in §E.13.2. Tenants rename departments in Settings, and their names appear in exports, while the canonical code is retained (R-086).

---

## E.9 Change sets, round trip and Updates

**Export for editing.** Content Studio → Instrument → Export for editing produces the family template:

- rows from the published (or draft) version
- E filled with CompIDs
- `_Template_Info` extended with `Exported instrument version`, `Exported at`, `Export job ID` and the export hash

**Re-upload diff (keyed on CompID).**

| Uploaded row | Existing obligation | Action | Diff shown |
|---|---|---|---|
| E blank | — | NEW | All fields |
| E = known CompID, fields equal | yes | NOCHANGE | — |
| E = known CompID, any content field differs | yes | UPDATE | Field-level, word-level redline (old ↔ new) |
| E = known CompID, F starts `[RETIRED] ` | yes | RETIRE | Retirement reason from S |
| CompID present in the export but absent from the upload | yes | Error LDC-TPL-023 | — |

**Change classification.** The content maker classifies each UPDATE as one of the following. The classification decides what tenants see (P05).

| Classification | Meaning | What tenants see |
|---|---|---|
| Editorial | Wording or explanation only, no change in obligation | Update notice optional; no new compliance instance |
| Substantive | The requirement, frequency, due rule, applicability, risk or evidence changed | Updates notice that states what changed, what it was before and what to do now; tenant impact assessment; new instance from the effective date |
| Correction | An error in the earlier content | Notice and a Correction Entry linked to the earlier version (D-02) |

**Tenant overlays on update.** An update to a base obligation never overwrites a tenant overlay (NN-03). Where the tenant has overridden a field that the update also changes, the tenant gets a **merge task**: keep my version, adopt the new version, or merge. Completed compliance instances stay pinned to the version they were performed under (NN-07).

**Audit trail.** Every import, commit, publish, retire, correction and overlay is an append-only ledger event (NN-02), with uploader, approver, file hash and diff hash. The ledger records:

- `ContentImportSubmitted`
- `ContentImportCommitted`
- `ObligationPublished`
- `ObligationRetired`
- `ObligationCorrected`
- `TenantOverlayCreated`

**Register and workspace exports (P03 WORKSPACE mode, P04 FR-P04-100) (review R2).** The tenant's compliance-register export uses the same 30 columns A–AD with the user columns I, J, T and W–AD filled from the compliance instances; nothing is written beyond AD (LDC-TPL-005 still applies). The instance reference and period of each row are carried in the hidden `_LDC_System` sheet keyed by sheet row (master X-28) and in the sheet's file name; `_Template_Info` records `Export variant = REGISTER`. A REGISTER file re-uploaded in WORKSPACE mode is applied as user actions (P04 FR-P04-101); it never changes content, and its content columns are ignored (LDC-TPL-013).

---

## E.10 Tenant-level import (client admin)

Client admins can bring their own instruments, for example a State co-operative rule, an internal policy or a contract covenant set, and can edit or extend library questions for their company.

**Entry points.**

- Compliance Library → My Instruments → **Add instrument**. This is a full new instrument with a tenant-owned obligation set and `T-` CompIDs.
- Library instrument → **Export for my company**. The client edits the export and re-uploads it as an overlay.

**Rules.**

1. The tenant chooses the family template that matches its entity profile. The upload dialog suggests it.
2. Rows with E blank create tenant obligations, which are visible only to that tenant.
3. Rows carrying a platform CompID with changed fields create **tenant overlays**. These change only that tenant's view and never the base content (LDC-TPL-034 explains this in the preview).
4. A `[RETIRED]` marker on a platform CompID becomes a tenant **opt-out**, recorded with a reason. It is not a deletion, and history is kept (NN-29).
5. Tenant publication uses the tenant's own maker ≠ checker setting (`cmp.content.tenant_publish_requires_checker`, T, default ON, floor ON for regulated entities).
6. A tenant can also author questions inline without Excel (P03 `SCR-CNT-07`). The inline editor writes the same model and can export the same template.

**AI authoring for tenants** is the same flow as §E.11, scoped to the tenant (R-085). Upload the instrument → Vidhi drafts the sheet with the family template and the Part-2 command → the admin downloads it or edits it inline → the admin submits → the importer runs → approve → publish to the tenant only.

---

## E.11 AI-assisted question authoring (Part 2 inside the product)

This section is the binding interface between this appendix and P05/P17.

- **Prompt.** The system prompt is `ai.prompt_templates` entry `QUESTION_GEN/question_authoring_v1` (P05 §7.2; table owned by P17). It is the text of `part2_prompts/00_Part2_Master_Command.md` and the family command, versioned together with the template vocabulary. The prompt version is recorded on every generated row.
- **Inputs:**
  - the instrument version's extracted text and clause tree (P03)
  - the family template and vocabulary
  - related instruments selected by the user
  - optionally, an earlier version's obligations (for amendments)
- **Pipeline:**
  1. para map, shown for approval
  2. row generation in batches by chapter
  3. self-check against the QA checklist items marked [auto]
  4. the generated workbook is validated by the same importer
  5. preview
- **Amendments.** Vidhi compares the old and new clause trees (P05 diff). It proposes UPDATE, NEW and RETIRE actions against existing CompIDs, so the output is a re-upload-shaped workbook.
- **Guardrails** (NN-04, NN-06, NN-14):
  - Every generated row carries `ai_generated = true`, the model and provider, the prompt version and the source clause IDs.
  - No row is published without human approval.
  - Citations must resolve to clause IDs. A row without a resolvable citation is flagged LDC-TPL-020 and cannot be published until a human fixes it.
  - Numbers in G, P, Q and S must appear in the cited clause text, or carry [VERIFY].
- **Export first** (owner's workflow). The user can always download the AI draft as the family Excel template, verify it offline and re-upload the edited file, exactly as in Part 2.

---

## E.12 Entity family catalogue

The 24 families shipped in v1.0 are listed below. Counts are the number of list values, as built and verified by `_validate_templates.py` on 25 October 2026 (all checks passed; see `templates/_validation_report.md`). The full value lists are in §E.15. The family command files in `part2_prompts/` explain the applicability logic for each family.

| # | Family | Template file | Regulator | Column C means | Column D means | Prefix |
|---|---|---|---|---|---|---|
| 1 | RBI-SCB | `LDC-TPL-RBI-SCB-v1.0 - Commercial Banks SFBs PBs LABs RRBs.xlsx` | Reserve Bank of India | Bank Category (6) | Bank Type / Overlay (15) | `RBI_SCB_*` |
| 2 | RBI-UCB | `LDC-TPL-RBI-UCB-v1.0 - Urban Co-operative Banks.xlsx` | Reserve Bank of India (with RCS / CRCS for registration matters) | UCB Tier (5) | UCB Type / Overlay (10) | `RBI_UCB_*` |
| 3 | RBI-RCB | `LDC-TPL-RBI-RCB-v1.0 - Rural Co-operative Banks.xlsx` | Reserve Bank of India (regulation); NABARD (supervision) | RCB Category (3) | RCB Type / Overlay (6) | `RBI_RCB_*` |
| 4 | RBI-NBFC | `LDC-TPL-RBI-NBFC-v1.0 - NBFCs.xlsx` | Reserve Bank of India (NHB for HFC supervision) | NBFC Layer (5) | NBFC Type (18) | `RBI_NBFC_*` |
| 5 | RBI-ARC | `LDC-TPL-RBI-ARC-v1.0 - Asset Reconstruction Companies.xlsx` | Reserve Bank of India | ARC Level (3) | ARC Type / Activity (9) | `RBI_ARC_*` |
| 6 | RBI-OTH | `LDC-TPL-RBI-OTH-v1.0 - Other RBI Regulated Entities.xlsx` | Reserve Bank of India | Entity Category (5) | Entity Type (18) | `RBI_OTH_*` |
| 7 | COOP-CCS | `LDC-TPL-COOP-CCS-v1.0 - Credit Co-operative Societies.xlsx` | Central Registrar (MSCS Act, 2002) / State Registrars of Co-operative Societies | Registration Law (5) | Society Type (10) | `COOP_CCS_*` |
| 8 | COOP-GEN | `LDC-TPL-COOP-GEN-v1.0 - Other Co-operative Societies.xlsx` | Central Registrar / State Registrars of Co-operative Societies; Registrar of Societies (SRA 1860) | Registration Law (6) | Society Type (16) | `COOP_GEN_*` |
| 9 | IFSCA-GEN | `LDC-TPL-IFSCA-GEN-v1.0 - IFSCA Regulated Entities.xlsx` | International Financial Services Centres Authority | Sector (13) | Entity Type (40) | `IFSCA_*` |
| 10 | IFSCA-FCFU | `LDC-TPL-IFSCA-FCFU-v1.0 - IFSCA Finance Companies and Units.xlsx` | International Financial Services Centres Authority | Entity Form (3) | Activity / Registration (15) | `IFSCA_FC_*` |
| 11 | IFSCA-FME | `LDC-TPL-IFSCA-FME-v1.0 - IFSCA Fund Management Entities.xlsx` | International Financial Services Centres Authority | FME Category (4) | Scheme / Activity (14) | `IFSCA_FME_*` |
| 12 | SEBI-MF | `LDC-TPL-SEBI-MF-v1.0 - Mutual Funds.xlsx` | Securities and Exchange Board of India | Entity Role (5) | Scheme / Framework (11) | `SEBI_MF_*` |
| 13 | SEBI-AIF | `LDC-TPL-SEBI-AIF-v1.0 - Alternative Investment Funds.xlsx` | Securities and Exchange Board of India | Entity Role (5) | AIF Category (12) | `SEBI_AIF_*` |
| 14 | SEBI-LISTED | `LDC-TPL-SEBI-LISTED-v1.0 - Listed Entities.xlsx` | Securities and Exchange Board of India; Stock Exchanges | Listing Segment (8) | Entity Overlay (11) | `SEBI_LST_*` |
| 15 | SEBI-REIT-INVIT | `LDC-TPL-SEBI-REIT-INVIT-v1.0 - REITs and InvITs.xlsx` | Securities and Exchange Board of India | Trust Type (6) | Role / Party (8) | `SEBI_REIT_*` |
| 16 | SEBI-INT | `LDC-TPL-SEBI-INT-v1.0 - SEBI Intermediaries.xlsx` | Securities and Exchange Board of India | Intermediary Group (8) | Intermediary Type / CSCRF Category (22) | `SEBI_INT_*` |
| 17 | IRDAI-INS | `LDC-TPL-IRDAI-INS-v1.0 - Insurers.xlsx` | Insurance Regulatory and Development Authority of India | Insurer Class (8) | Insurer Overlay (8) | `IRDAI_INS_*` |
| 18 | IRDAI-INT | `LDC-TPL-IRDAI-INT-v1.0 - Insurance Intermediaries.xlsx` | Insurance Regulatory and Development Authority of India | Intermediary Class (10) | Intermediary Type (17) | `IRDAI_INT_*` |
| 19 | MCA-CO | `LDC-TPL-MCA-CO-v1.0 - Companies.xlsx` | Ministry of Corporate Affairs / Registrar of Companies | Company Class (11) | Threshold / Overlay (14) | `MCA_CO_*` |
| 20 | MCA-LLP | `LDC-TPL-MCA-LLP-v1.0 - LLPs.xlsx` | Ministry of Corporate Affairs / Registrar of Companies | LLP Class (4) | Threshold / Overlay (5) | `MCA_LLP_*` |
| 21 | DATA-PRIV | `LDC-TPL-DATA-PRIV-v1.0 - Data Protection and Privacy.xlsx` | MeitY / Data Protection Board of India; EU supervisory authorities; California Privacy Protection Agency | Law / Jurisdiction (7) | Role (15) | `DATA_PRIV_*` |
| 22 | CYBER | `LDC-TPL-CYBER-v1.0 - Cyber Security.xlsx` | CERT-In / MeitY; sectoral regulators (RBI, SEBI, IRDAI, IFSCA) | Framework (11) | Entity Category (15) | `CYBER_*` |
| 23 | LAB-POSH | `LDC-TPL-LAB-POSH-v1.0 - Labour Codes and POSH.xlsx` | Ministry of Labour and Employment; State Labour Departments; Ministry of Women and Child Development (POSH) | Law (9) | Establishment Type / Threshold (15) | `LAB_*` |
| 24 | TAX-GST | `LDC-TPL-TAX-GST-v1.0 - GST and Direct Tax.xlsx` | CBIC / GSTN; CBDT; State tax departments | Law (7) | Taxpayer Type (15) | `TAX_*` |

List sizes (H / M / O / P): RBI-SCB 14/14/6/21; RBI-UCB 14/14/6/19; RBI-RCB 14/14/6/15; RBI-NBFC 14/14/6/20; RBI-ARC 14/13/6/18; RBI-OTH 14/13/6/19; COOP-CCS 14/13/7/14; COOP-GEN 14/13/7/14; IFSCA-GEN 11/9/6/10; IFSCA-FCFU 14/11/6/11; IFSCA-FME 14/13/7/13; SEBI-MF 14/13/7/16; SEBI-AIF 14/13/7/14; SEBI-LISTED 14/12/7/15; SEBI-REIT-INVIT 14/13/7/12; SEBI-INT 14/14/6/15; IRDAI-INS 14/16/6/15; IRDAI-INT 14/13/6/12; MCA-CO 14/12/7/14; MCA-LLP 14/11/7/8; DATA-PRIV 14/14/7/12; CYBER 14/13/6/12; LAB-POSH 14/12/7/12; TAX-GST 14/12/6/11.

## E.13 Canonical code tables

Canonical codes are what the platform stores and what other products receive (Ecosystem Spec §5.3 code tables). Display text can change through aliases without changing codes.

### E.13.1 Frequency (Column H)

| Display value | Code | Scheduler meaning |
|---|---|---|
| Annually | `ANNUAL` | Once per financial year (tenant FY setting) unless a fixed date is set |
| Half Yearly | `HALF_YEARLY` | Twice per FY (H1/H2) |
| Quarterly | `QUARTERLY` | Per FY quarter |
| Monthly | `MONTHLY` | Per calendar month |
| Fortnightly | `FORTNIGHTLY` | 1st–15th and 16th–end of month (RBI convention) [INTERP] |
| Weekly | `WEEKLY` | Per ISO week |
| Daily | `DAILY` | Per business day (tenant calendar) |
| Event Based | `EVENT` | Instance created when the linked event is recorded |
| Immediately | `IMMEDIATE` | Event instance with zero offset and urgent priority |
| Ongoing/Continuous | `CONTINUOUS` | Standing obligation; periodic attestation per `cmp.ongoing.attestation_frequency` (T, default QUARTERLY; P04) |
| One-time | `ONE_TIME` | Single instance; re-opened only by an event (e.g., change in registration) |
| Every 2 Years | `EVERY_2Y` | Every 2 FYs from anchor |
| Every 3 Years | `EVERY_3Y` | Every 3 FYs from anchor |
| Every 5 Years | `EVERY_5Y` | Every 5 FYs from anchor |

### E.13.2 Department (Column M)

Base departments (every family) and family additions. Tenants rename departments in Settings → Organisation → Departments; the canonical code is preserved for reporting, ecosystem exchange and exports. Codes are those of Appendix U §U.6.1 and §U.9.0 (master X-10); several display values share one code (for example Internal Audit, Internal Audit & Inspection and Audit all map to `IA`).

| Display value | Code | Base / addition | Families |
|---|---|---|---|
| Governance & Administration | `GOV` | Base | All |
| Finance, Treasury and Accounts | `FIN` | Base | All |
| Legal & Litigation | `LEG` | Base | All |
| IT | `IT` | Base | All |
| Operations & Management | `OPS` | Base | All |
| HR | `HR` | Base | All |
| Compliance | `CMP` | Base | All |
| Returns & Reporting | `RET` | Base | All |
| Risk Management | `RSK` | Base | All |
| Credit | `CRD` | Addition | RBI-SCB, RBI-UCB, RBI-RCB, RBI-NBFC, IFSCA-FCFU |
| Internal Audit & Inspection | `IA` | Addition | RBI-SCB, RBI-UCB, RBI-RCB |
| Customer Service & Grievance | `CSG` | Addition | RBI-SCB, RBI-UCB, RBI-RCB, RBI-NBFC, RBI-ARC, RBI-OTH, DATA-PRIV |
| Information Security | `ISEC` | Addition | RBI-SCB, RBI-UCB, RBI-RCB, RBI-NBFC, RBI-OTH, SEBI-MF, SEBI-INT, IRDAI-INS, DATA-PRIV, CYBER |
| KYC & AML | `KYC` | Addition | RBI-SCB, RBI-UCB, RBI-RCB, RBI-OTH |
| Collections & Recovery | `COL` | Addition | RBI-NBFC |
| Internal Audit | `IA` | Addition | RBI-NBFC, RBI-ARC, RBI-OTH, IFSCA-FCFU, IFSCA-FME, SEBI-MF, SEBI-AIF, SEBI-LISTED, SEBI-INT, IRDAI-INS, IRDAI-INT, MCA-CO |
| Acquisition & Resolution | `COL` | Addition | RBI-ARC |
| Trusteeship & SR Management | `TRS` | Addition | RBI-ARC |
| Credit & Recovery | `CRD` | Addition | COOP-CCS |
| Membership & Elections | `MEM` | Addition | COOP-CCS, COOP-GEN |
| Audit | `IA` | Addition | COOP-CCS, COOP-GEN |
| Member Services & Grievance | `MEM` | Addition | COOP-CCS, COOP-GEN |
| Business Operations | `OPS` | Addition | COOP-GEN |
| Investment Team | `FMI` | Addition | IFSCA-FME, SEBI-AIF |
| Valuation | `VAL` | Addition | IFSCA-FME, SEBI-AIF, SEBI-REIT-INVIT |
| Investor Relations | `INV` | Addition | IFSCA-FME, SEBI-AIF, SEBI-LISTED, SEBI-REIT-INVIT |
| Fund Management & Investments | `FMI` | Addition | SEBI-MF |
| Investor Services | `INV` | Addition | SEBI-MF |
| Secretarial | `SECR` | Addition | SEBI-LISTED, SEBI-REIT-INVIT, MCA-CO, MCA-LLP |
| Asset Management | `FMI` | Addition | SEBI-REIT-INVIT |
| Client Onboarding & KYC | `KYC` | Addition | SEBI-INT |
| Surveillance | `SRV` | Addition | SEBI-INT |
| Investor Grievance | `INV` | Addition | SEBI-INT |
| Actuarial | `ACT` | Addition | IRDAI-INS |
| Underwriting | `UND` | Addition | IRDAI-INS |
| Claims | `CLM` | Addition | IRDAI-INS |
| Investments | `TRY` | Addition | IRDAI-INS |
| Policyholder Servicing & Grievance | `CSG` | Addition | IRDAI-INS |
| Sales & Distribution | `BUS` | Addition | IRDAI-INT |
| Claims Support | `CLM` | Addition | IRDAI-INT |
| Policyholder Grievance | `CSG` | Addition | IRDAI-INT |
| Tax | `TAX` | Addition | MCA-CO, MCA-LLP, TAX-GST |
| Privacy Office (DPO) | `DPR` | Addition | DATA-PRIV |
| Marketing | `MKT` | Addition | DATA-PRIV |
| Product & Engineering | `PRD` | Addition | DATA-PRIV |
| IT Infrastructure | `IT` | Addition | CYBER |
| Application Development | `IT` | Addition | CYBER |
| Business Continuity | `RSK` | Addition | CYBER |
| Payroll | `PRL` | Addition | LAB-POSH |
| Administration & Facilities | `ADM` | Addition | LAB-POSH |
| Internal Committee (POSH) | `ICP` | Addition | LAB-POSH |
| Accounts Payable | `FIN` | Addition | TAX-GST |
| Billing & Receivables | `FIN` | Addition | TAX-GST |

### E.13.3 Compliance type (Column O)

| Display value | Code | Families | Workflow effect |
|---|---|---|---|
| Policies | `POLICY` | All | Links to Policy register (P07); evidence = approved policy version |
| Compliance | `COMPLIANCE` | All | Standard maker-checker instance |
| Returns & Reporting | `RETURN_REPORT` | All | Links to Return Studio / filing tracker (P11); evidence = acknowledgement |
| Committee | `COMMITTEE` | All | Links to Committee register (P06) |
| Internal Compliance | `INTERNAL` | All | Internal control instance; testable in audit (P10) |
| Suggestive Compliance | `SUGGESTIVE` | All | Optional; tenant may opt in; excluded from compliance score by default |
| Registers & Records | `REGISTERS_AND_RECORDS` | COOP-CCS, COOP-GEN, MCA-CO, MCA-LLP, LAB-POSH | Links to statutory registers (P06/P13/P16) |
| Disclosures | `DISCLOSURES` | IFSCA-FME, SEBI-MF, SEBI-AIF, SEBI-LISTED, SEBI-REIT-INVIT | Links to disclosure calendar; evidence = URL/filing |
| Notices & Consents | `NOTICES_AND_CONSENTS` | DATA-PRIV | Links to DPDP notice/consent module (P12) |

### E.13.4 Risk (Column R)

| Value | Code | Default score (1–5) used by ERM linkage (P08) |
|---|---|---|
| High | `HIGH` | 5 |
| Medium | `MEDIUM` | 3 |
| Low | `LOW` | 1 |

Scores are tenant-configurable (`erm.compliance_risk.score_map`, T) within bounds 1–5.

### E.13.5 Taxonomy codes for Columns C and D

Codes follow `<FAMILY>.<AXIS>.<SLUG>` (AXIS = `C` or `D`), are generated on family publication and are mapped by P15 to the entity taxonomy (`pack.entity_taxonomy`). Examples: `RBI-NBFC.C.NBFC_BL`, `RBI-NBFC.C.NBFC_ML`, `RBI-NBFC.C.NBFC_UL`, `RBI-NBFC.D.NBFC_ICC`, `RBI-NBFC.D.NBFC_MFI`, `RBI-NBFC.D.NBFC_FACTOR`. The complete code list for every value is produced by `templates/_build/appendix_tables.py` and loaded by the P03 seed migration.

---

## E.14 Security, privacy and limits

The importer treats every workbook as hostile input. Each threat below is mapped to OWASP ASVS 5.0 V5 (file handling) and V12 [VERIFY section numbering in ASVS 5.0].

| Threat | Control |
|---|---|
| Macros and active content | Only `.xlsx` is accepted, and its content type is checked by magic bytes as well as the extension. The file is rejected if it contains `vbaProject.bin`, `activeX`, `oleObject`, `externalLink`, DDE fields or connections (LDC-TPL-010) |
| Zip bomb or oversized file | Limits on total uncompressed size (≤ 200 MB), compression ratio (≤ 100:1), entry count (≤ 2,000), file size (≤ 25 MB) and rows (≤ 2,000) (LDC-TPL-009/010) |
| XXE or DTD | The XML parser has DTDs and external entities disabled |
| Formula or CSV injection | Formulas are never evaluated. Cached values are read with `data_only`. Content beginning with `=`, `+`, `-` or `@` is stored as text, and on export it is prefixed so that Excel does not evaluate it (LDC-TPL-011) |
| Malware | The file is scanned before parsing (ClamAV or a cloud AV adapter, P07 DMS) and quarantined in a separate bucket prefix |
| Hyperlinks | Links are stored as text references only. They are never fetched during import, and they are rendered with `rel="noopener noreferrer"` |
| Prompt injection (AI lint and authoring) | Cell text is passed to Vidhi as quoted data, never as instructions. Instructions embedded in a source document or cell are ignored and flagged (NN-14; P17) |
| Tenant isolation | Tenant imports run with the tenant's RLS context. Platform imports run as the platform content role. A CompID from another tenant is rejected (LDC-TPL-024; NN-01) |
| Audit | Every job stores the file SHA-256, the uploader, the approver, row actions and issue counts. Original files are kept in WORM storage for the content-retention period (`cnt.retention.source_files_years`, G, default 10 years) |
| Personal data | Question sheets must not contain personal data. A PII detector (PAN, Aadhaar, e-mail, phone patterns) raises a warning on content cells, which are expected to carry none [REC] |

Import performance target: a 400-row workbook validates in under 15 seconds at p95, and a 2,000-row workbook in under 60 seconds. Validation runs as a Temporal workflow with progress events, and the preview streams results as they arrive.

## E.15 Family vocabularies (complete lists as built in v1.0)

Values are exact (case and punctuation). The P column lists are reference tokens that start Column P.

### E.15.1 RBI-SCB — Commercial Banks, SFBs, Payments Banks, LABs and RRBs

- **C — Bank Category:** Commercial Bank; Small Finance Bank (SFB); Payments Bank (PB); Local Area Bank (LAB); Regional Rural Bank (RRB); All Banks
- **D — Bank Type / Overlay:** Public Sector Bank (PSB); Private Sector Bank (Old); Private Sector Bank (New); Universal Bank (On-tap Licence); Foreign Bank - Branch Mode; Foreign Bank - Wholly Owned Subsidiary (WOS); Domestic Systemically Important Bank (D-SIB); Listed Bank; Bank with Overseas Branches / Subsidiaries; Bank under Prompt Corrective Action (PCA); Small Finance Bank (SFB); Payments Bank (PB); Local Area Bank (LAB); Regional Rural Bank (RRB); All Banks (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Credit; Internal Audit & Inspection; Customer Service & Grievance; Information Security; KYC & AML
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** RBI - CIMS (Supervisory Returns); RBI - DAKSH (Supervisory Compliance); RBI - PRAVAAH (Applications / Approvals); RBI (prior approval); RBI (intimation); RBI - Department of Regulation; RBI - Department of Supervision; RBI - Foreign Exchange Department (FEMA); RBI - Department of Payment & Settlement Systems; NABARD (ENSURE) - RRBs; FIU-IND (FINnet 2.0); Credit Information Companies (CICs); CERSAI / CKYCR; CERT-In; DICGC; SEBI / Stock Exchanges (listed banks); Ministry of Finance (DFS) - PSBs; MCA; Board / Management; Statutory / Central Auditor; Not Required

### E.15.2 RBI-UCB — Urban Co-operative Banks

- **C — UCB Tier:** Tier 1 UCB; Tier 2 UCB; Tier 3 UCB; Tier 4 UCB; All UCBs
- **D — UCB Type / Overlay:** Unit UCB (single district); Salary Earners' UCB; Multi-district / State-wide UCB (State Act); Multi-State UCB (MSCS Act, 2002); Scheduled UCB; Non-Scheduled UCB; Financially Sound and Well Managed (FSWM) UCB; UCB under Supervisory Action Framework (SAF); UCB under All-Inclusive Directions (s.35A, BR Act); All UCBs (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Credit; Internal Audit & Inspection; Customer Service & Grievance; Information Security; KYC & AML
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** RBI - CIMS (Supervisory Returns); RBI - DAKSH (Supervisory Compliance); RBI - PRAVAAH (Applications / Approvals); RBI (prior approval); RBI (intimation); RBI - Department of Regulation; RBI - Department of Supervision; Registrar of Co-operative Societies (State); Central Registrar of Co-operative Societies (MSCS); NUCFDC (Umbrella Organisation); FIU-IND (FINnet 2.0); Credit Information Companies (CICs); CERSAI / CKYCR; CERT-In; DICGC; General Body / Members; Board / Management; Statutory / Central Auditor; Not Required

### E.15.3 RBI-RCB — Rural Co-operative Banks (StCBs and DCCBs)

- **C — RCB Category:** State Co-operative Bank (StCB); District Central Co-operative Bank (DCCB); All Rural Co-operative Banks
- **D — RCB Type / Overlay:** StCB - Scheduled; StCB - Non-Scheduled; DCCB; RCB under Supervisory Action / s.35A Directions; RCB with CBS / Shared Service Entity arrangement; All RCBs (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Credit; Internal Audit & Inspection; Customer Service & Grievance; Information Security; KYC & AML
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** NABARD (ENSURE); NABARD (Department of Supervision); RBI (prior approval); RBI (intimation); RBI - Department of Regulation; Registrar of Co-operative Societies (State); FIU-IND (FINnet 2.0); Credit Information Companies (CICs); CERSAI / CKYCR; CERT-In; DICGC; General Body / Members; Board / Management; Statutory / Central Auditor; Not Required

### E.15.4 RBI-NBFC — Non-Banking Financial Companies (all layers and types)

- **C — NBFC Layer:** Base Layer (NBFC-BL); Middle Layer (NBFC-ML); Upper Layer (NBFC-UL); Top Layer (NBFC-TL); All Layers
- **D — NBFC Type:** NBFC-Investment and Credit Company (NBFC-ICC); NBFC-Microfinance Institution (NBFC-MFI); NBFC-Factor; NBFC-Infrastructure Finance Company (NBFC-IFC); Infrastructure Debt Fund (IDF-NBFC); Housing Finance Company (HFC); Core Investment Company (CIC); Mortgage Guarantee Company (MGC); Standalone Primary Dealer (SPD); NBFC-Peer to Peer Lending Platform (NBFC-P2P); NBFC-Account Aggregator (NBFC-AA); Non-Operative Financial Holding Company (NOFHC); Deposit-taking NBFC (NBFC-D); Government-owned NBFC; NBFC without public funds and without customer interface; NBFC with customer interface, without public funds; Registered Factor under Factoring Regulation Act, 2011; All NBFCs (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Credit; Collections & Recovery; Internal Audit; Customer Service & Grievance; Information Security
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** RBI - CIMS (Supervisory Returns); RBI - DAKSH (Supervisory Compliance); RBI - PRAVAAH (Applications / Approvals); RBI (prior approval); RBI (intimation); RBI - Department of Regulation; RBI - Department of Supervision; NHB (HFC supervision); FIU-IND (FINnet 2.0); Credit Information Companies (CICs); CERSAI / CKYCR; CERT-In; MCA (ROC); SEBI / Stock Exchanges (listed NBFCs / NCD issuers); Debenture Trustee; Credit Rating Agency; IRDAI (corporate agency); Board / Management; Statutory / Central Auditor; Not Required

### E.15.5 RBI-ARC — Asset Reconstruction Companies

- **C — ARC Level:** ARC - Company Level; ARC - Trust / Scheme Level; All ARCs
- **D — ARC Type / Activity:** ARC (all); ARC eligible for additional permitted activities (NOF-based); ARC acting as Resolution Applicant (IBC); ARC acting as Trustee / Manager of Trusts; ARC with Sponsor Bank / FI; ARC with FPI / FDI investment; Listed ARC / ARC with listed SRs; Security Receipt (SR) Scheme; All ARCs (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Acquisition & Resolution; Trusteeship & SR Management; Internal Audit; Customer Service & Grievance
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** RBI - CIMS (Supervisory Returns); RBI - DAKSH (Supervisory Compliance); RBI - PRAVAAH (Applications / Approvals); RBI (prior approval); RBI (intimation); RBI - Department of Regulation; RBI - Department of Supervision; CERSAI / CKYCR; FIU-IND (FINnet 2.0); Credit Information Companies (CICs); Credit Rating Agency (SR rating); Qualified Buyers / SR holders (disclosure); NCLT / IBBI; DRT / Courts; SEBI / Stock Exchanges; Board / Management; Statutory / Central Auditor; Not Required

### E.15.6 RBI-OTH — Other RBI-regulated entities (AIFIs, CICs, payment system operators, FEMA authorised persons)

- **C — Entity Category:** All India Financial Institution (AIFI); Credit Information Company (CIC); Payment System Operator / Participant; Authorised Person (FEMA); All Other RBI Regulated Entities
- **D — Entity Type:** EXIM Bank; NABARD; National Housing Bank (NHB); SIDBI; NaBFID; Credit Information Company (TransUnion CIBIL / Equifax / Experian / CRIF High Mark); Payment Aggregator - Online (PA); Payment Aggregator - Physical (PA-P); Payment Aggregator - Cross Border (PA-CB); Prepaid Payment Instrument Issuer (non-bank PPI); Bharat Bill Payment Operating Unit (BBPOU); Trade Receivables Discounting System (TReDS); White Label ATM Operator (WLAO); Card Network; Money Transfer Service Scheme (MTSS) Indian Agent; Authorised Dealer Category II (AD-II); Full Fledged Money Changer (FFMC); All (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Internal Audit; Customer Service & Grievance; Information Security; KYC & AML
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** RBI - CIMS (Supervisory Returns); RBI - DAKSH (Supervisory Compliance); RBI - PRAVAAH (Applications / Approvals); RBI (prior approval); RBI (intimation); RBI - Department of Regulation; RBI - Department of Supervision; RBI - Department of Payment & Settlement Systems; RBI - Foreign Exchange Department (FEMA); NPCI; Ministry of Finance; SEBI / Stock Exchanges (listed bonds); FIU-IND (FINnet 2.0); Credit Information Companies (CICs); CERSAI / CKYCR; CERT-In; Board / Management; Statutory / Central Auditor; Not Required

### E.15.7 COOP-CCS — Credit Co-operative Societies (multi-State, State, PACS)

- **C — Registration Law:** Multi-State Credit Co-operative Society (MSCS Act, 2002); State Credit Co-operative Society (State Co-operative Societies Act); Mutually Aided / Self-reliant Co-operative (State MACS Act); Primary Agricultural Credit Society (PACS); All Credit Co-operative Societies
- **D — Society Type:** Urban / Nagari Credit Co-operative Society (Patsanstha); Employees' / Salary Earners' Credit Co-operative Society; Thrift and Credit Co-operative Society; Primary Agricultural Credit Society (PACS); Large-sized Adivasi Multipurpose Society (LAMPS); Farmers' Service Society (FSS); Multi-State Credit Co-operative Society; Women's Credit Co-operative Society; Society subject to concurrent audit (State Act threshold); All (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Credit & Recovery; Membership & Elections; Audit; Member Services & Grievance
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Registers & Records
- **R:** High; Medium; Low
- **P (reference):** Central Registrar of Co-operative Societies (CRCS Portal); Registrar of Co-operative Societies (State); Co-operative Election Authority (MSCS); State Co-operative Election Commission / Authority; Co-operative Ombudsman (MSCS); Statutory Auditor (Panel); Department / Government Auditor; General Body / Members; Board of Directors / Committee of Management; FIU-IND (FINnet 2.0); Income Tax / GST Authorities; Credit Information Companies (CICs); NABARD (PACS); Not Required

### E.15.8 COOP-GEN — Other Co-operative Societies and Registered Societies

- **C — Registration Law:** Multi-State Co-operative Society (MSCS Act, 2002); State Co-operative Society (State Act); Mutually Aided Co-operative (State MACS Act); Federal / Apex Co-operative; Society under Societies Registration Act, 1860 (non-co-operative); All
- **D — Society Type:** Housing Co-operative Society; Consumer Co-operative; Dairy / Milk Producers' Co-operative; Marketing Co-operative; Agro-processing / Sugar Co-operative; Fisheries Co-operative; Weavers' / Industrial Co-operative; Labour Contract Co-operative; Multipurpose Co-operative; Transport Co-operative; Health / Hospital Co-operative; Tourism Co-operative; National-level MSCS (Seeds / Organic / Exports); Federation / Union; Educational / Charitable Society (SRA 1860); All (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Membership & Elections; Audit; Member Services & Grievance; Business Operations
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Registers & Records
- **R:** High; Medium; Low
- **P (reference):** Central Registrar of Co-operative Societies (CRCS Portal); Registrar of Co-operative Societies (State); Co-operative Election Authority (MSCS); State Co-operative Election Commission / Authority; Co-operative Ombudsman (MSCS); Statutory Auditor (Panel); Department / Government Auditor; General Body / Members; Board of Directors / Committee of Management; FIU-IND (FINnet 2.0); Income Tax / GST Authorities; Registrar of Societies (SRA 1860); NCDC; Not Required

### E.15.9 IFSCA-GEN — IFSCA Regulated Entities (all types)

- **C — Sector:** Banking; Finance Company; Fund Management; Capital Markets; Insurance; Metals & Commodities (Bullion); Payments; FinTech; Ancillary Services; Global In-House Centre; Education; Trade Finance; Cross-cutting / All REs
- **D — Entity Type:** IFSC Banking Unit (IBU); IFSC Banking Company (IBC); Finance Company / Finance Unit (FCFU); Aircraft Lessor (ACL); Ship Lessor (SHL); Fund Management Entity (FME); Pension Fund (PENF); Market Infrastructure Institution (MII); Capital Market Intermediary (CMI); Recognised Stock Exchange (RSEX); Recognised Clearing Corporation (RCCP); Recognised Depository (RDEP); Broker Dealer / Clearing Member (BDCM); Custodian / Depository Participant (CUDP); Investment Adviser / Portfolio Manager (IAPM); Investment Banker (INVB); Distributor (DIST); Debenture Trustee (DTEE); Credit Rating Agency (CRA); Research Entity (RESE); ESG Ratings & Data Products Provider (ERDP); KYC Registration Agency (KRA); Issuer / Listed Entity (ISSU); IFSC Insurance Office (IIO); IFSC Insurance Intermediary Office (IIIO); Insurance Web Aggregator (IWA); Managing General Agent (MGA); Bullion Exchange / Clearing Corp / Depository (BMII); Vault Manager (VM); Bullion Trading / Clearing Member (BTCM); Payment Service Provider (PSP); Payment System Operator (PSO); FinTech Entity (FE); TechFin Entity (TFIN); Ancillary Service Provider (ASP); Book-keeping/Accounting/Taxation/FCC Provider (BATF); Global In-House Centre (GIC); International Branch Campus / Offshore Education Centre (EDU); ITFS Platform Operator (ITFS); All Regulated Entities (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** IFSCA; IFSCA (prior approval); IFSCA (intimation); IFSCA / FIU-IND; Home country regulator (NOC); MCA; RBI (FEMA); Central Registry (CERSAI); Management; Not Required

### E.15.10 IFSCA-FCFU — IFSCA Finance Companies and Finance Units

- **C — Entity Form:** Finance Company (FC); Finance Unit (FU); Finance Company / Finance Unit (FCFU)
- **D — Activity / Registration:** Finance Company / Finance Unit (FCFU); Global/Regional Corporate Treasury Centre (GRCTC); Core - Lending, Commitments, Guarantees, Credit Enhancement, Securitisation, Financial Lease; Core - Factoring and Forfaiting (Registered Factor); Core - Investments in Securities; Core - Buy/Sell Derivatives; Non-core - Merchant Banking / Investment Banking; Non-core - Investment Advisory / Portfolio Management; Non-core - Distribution of Financial Products; Non-core - Trading / Clearing Member; Non-core - Registrar & Share Transfer Agent / Trusteeship; Aircraft Lessor (ACL); Ship Lessor (SHL); ITFS Platform Operator (ITFS); All FC/FU (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Internal Audit; Credit
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** IFSCA; IFSCA (prior approval); IFSCA (intimation); IFSCA / FIU-IND; Home country regulator (NOC); MCA; RBI (FEMA); Central Registry (CERSAI); GIFT SEZ - Development Commissioner; Management; Not Required

### E.15.11 IFSCA-FME — IFSCA Fund Management Entities and Schemes

- **C — FME Category:** Authorised FME; Registered FME (Non-Retail); Registered FME (Retail); All FMEs
- **D — Scheme / Activity:** Fund Management Entity (FME); Venture Capital Scheme; Restricted Scheme (Non-Retail); Retail Scheme; Exchange Traded Fund (ETF); Family Investment Fund (FIF); Portfolio Management Services (PMS) incl. Multi-family Office; Special Situation Fund; Fund of Funds / Feeder Scheme; Investment Trust - REIT (Private / Public); Investment Trust - InvIT (Private / Public); Co-investment / SPV / Segregated Portfolio; Pension Fund (PENF); All FMEs and Schemes (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Investment Team; Valuation; Investor Relations; Internal Audit
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Disclosures
- **R:** High; Medium; Low
- **P (reference):** IFSCA; IFSCA (prior approval); IFSCA (intimation); IFSCA / FIU-IND; Home country regulator (NOC); MCA; RBI (FEMA); Central Registry (CERSAI); Recognised Stock Exchange (IFSC); Custodian / Depository; Investors (disclosure); Management; Not Required

### E.15.12 SEBI-MF — Mutual Funds (AMCs, Trustees, Schemes)

- **C — Entity Role:** Asset Management Company (AMC); Trustee Company / Board of Trustees; Sponsor; Mutual Fund Scheme; All MF Entities
- **D — Scheme / Framework:** Equity Scheme; Debt Scheme; Hybrid Scheme; Solution-oriented Scheme; Index Fund / ETF; Fund of Funds; Close-ended / Interval Scheme; Specialized Investment Fund (SIF); Mutual Fund Lite (MF Lite - passive); Overseas Investment Scheme; All Schemes (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Fund Management & Investments; Investor Services; Internal Audit; Information Security
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Disclosures
- **R:** High; Medium; Low
- **P (reference):** SEBI (filing); SEBI (prior approval); SEBI (intimation); SEBI Intermediary Portal (SI Portal); SEBI SCORES / SMART ODR; AMFI; Stock Exchanges; Depositories / RTA; Trustees; Unitholders (website / disclosure); FIU-IND (FINnet 2.0); CERT-In; KRA / CKYCR; Board of AMC; Statutory Auditor; Not Required

### E.15.13 SEBI-AIF — Alternative Investment Funds

- **C — Entity Role:** AIF / Scheme; Manager; Sponsor; Trustee; All AIF Entities
- **D — AIF Category:** Category I - Venture Capital Fund; Category I - Angel Fund; Category I - SME Fund; Category I - Social Impact Fund; Category I - Infrastructure Fund; Category I - Special Situation Fund; Category II AIF; Category III AIF; Large Value Fund for Accredited Investors (LVF); Scheme for Accredited Investors only; Co-investment Scheme (CIV); All AIFs (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Investment Team; Valuation; Investor Relations; Internal Audit
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Disclosures
- **R:** High; Medium; Low
- **P (reference):** SEBI (filing); SEBI (prior approval); SEBI (intimation); SEBI Intermediary Portal (SI Portal); SEBI SCORES / SMART ODR; Custodian; Depositories (demat of units); Investors (disclosure / PPM); Performance Benchmarking Agency; FIU-IND (FINnet 2.0); CERT-In; Board / Investment Committee; Statutory Auditor; Not Required

### E.15.14 SEBI-LISTED — Listed Entities (equity, SME, debt, HVDLE)

- **C — Listing Segment:** Main Board - Specified Securities; SME Exchange / SME Platform; Non-Convertible Securities (Debt-listed); High Value Debt Listed Entity (HVDLE); Specified Securities and Non-Convertible Securities; Social Stock Exchange; Commercial Paper (listed); All Listed Entities
- **D — Entity Overlay:** Top 100 listed entities (by market capitalisation); Top 500 listed entities; Top 1000 listed entities; Top 2000 listed entities; Listed entity with material subsidiary; Listed entity with SR equity shares; Public Sector Undertaking (listed); Listed Bank / NBFC / Insurer (sectoral overlay); Newly listed entity (IPO year); Entity under CIRP (IBC); All Listed Entities (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Secretarial; Investor Relations; Internal Audit
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Disclosures
- **R:** High; Medium; Low
- **P (reference):** Stock Exchanges (NSE NEAPS / BSE Listing Centre); Stock Exchanges (prior approval / in-principle); SEBI (filing); SEBI SCORES / SMART ODR; Depositories (NSDL / CDSL); RTA; MCA (ROC); Debenture Trustee; Credit Rating Agency; Shareholders (website / newspaper); IEPF Authority; Board / Audit Committee; Secretarial Auditor; Statutory Auditor; Not Required

### E.15.15 SEBI-REIT-INVIT — REITs, SM REITs and InvITs

- **C — Trust Type:** Real Estate Investment Trust (REIT); Small and Medium REIT (SM REIT); Infrastructure Investment Trust (InvIT) - Public; InvIT - Private Listed; InvIT - Private Unlisted; All Investment Trusts
- **D — Role / Party:** Trust; Manager / Investment Manager; Trustee; Sponsor / Sponsor Group; Project Manager; Valuer; Holdco / SPV; All Parties (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Secretarial; Investor Relations; Valuation; Asset Management
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Disclosures
- **R:** High; Medium; Low
- **P (reference):** SEBI (filing); SEBI (prior approval); Stock Exchanges; Unitholders (disclosure); Trustee; Valuer; Credit Rating Agency; Depositories; MCA (ROC); Board of Manager; Statutory Auditor; Not Required

### E.15.16 SEBI-INT — SEBI Market Intermediaries

- **C — Intermediary Group:** Trading and Clearing; Depository Services; Advisory and Research; Issue Management and Registry; Portfolio and Fund Services; Rating, Trusteeship and Custody; Data and Index Services; All Intermediaries
- **D — Intermediary Type / CSCRF Category:** Stock Broker; Clearing Member; Depository Participant; Investment Adviser; Research Analyst; Portfolio Manager; Merchant Banker; Registrar to an Issue and Share Transfer Agent (RTA); Banker to an Issue; Debenture Trustee; Credit Rating Agency; Custodian; KYC Registration Agency (KRA); ESG Rating Provider; Online Bond Platform Provider; Vault Manager; Index Provider; CSCRF - Qualified RE; CSCRF - Mid-size RE; CSCRF - Small-size RE; CSCRF - Self-certification RE; All Intermediaries (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Client Onboarding & KYC; Surveillance; Investor Grievance; Internal Audit; Information Security
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** SEBI (filing); SEBI (prior approval); SEBI (intimation); SEBI Intermediary Portal (SI Portal); SEBI SCORES / SMART ODR; Stock Exchanges (supervising MII); Depositories; Clearing Corporations; KRA / CKYCR; BSE Administration & Supervision Ltd (BASL) - IA / RA; FIU-IND (FINnet 2.0); CERT-In; Board / Management; Statutory / Internal Auditor; Not Required

### E.15.17 IRDAI-INS — Insurers (life, general, health, reinsurers, FRBs)

- **C — Insurer Class:** Life Insurer; General Insurer; Standalone Health Insurer; Indian Reinsurer; Foreign Reinsurer Branch (FRB); Lloyd's India; Composite Insurer (where licensed); All Insurers
- **D — Insurer Overlay:** Public Sector Insurer; Private Insurer; Listed Insurer; Specialised Insurer (e.g., agriculture, micro, export credit); Insurer with bancassurance / corporate agency tie-ups; Insurer offering Unit Linked products; Insurer offering Health products; All Insurers (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Actuarial; Underwriting; Claims; Investments; Policyholder Servicing & Grievance; Internal Audit; Information Security
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** IRDAI (filing); IRDAI (prior approval / product filing); IRDAI (intimation); IRDAI Bima Bharosa (grievance); Insurance Ombudsman (CIO); Insurance Information Bureau (IIB); Life Insurance Council / General Insurance Council; FIU-IND (FINnet 2.0); CERT-In; SEBI / Stock Exchanges (listed insurers); MCA (ROC); Appointed Actuary; Board / Management; Statutory Auditor; Not Required

### E.15.18 IRDAI-INT — Insurance Intermediaries

- **C — Intermediary Class:** Insurance Broker; Corporate Agent; Insurance Marketing Firm (IMF); Web Aggregator; Third Party Administrator (TPA); Surveyor and Loss Assessor; Common Service Centre / POSP channel; Managing General Agent (MGA); Insurance Repository; All Intermediaries
- **D — Intermediary Type:** Direct Broker - Life; Direct Broker - General; Direct Broker - Life and General; Reinsurance Broker; Composite Broker; Corporate Agent - Life; Corporate Agent - General; Corporate Agent - Health; Corporate Agent - Composite; Bank / NBFC as Corporate Agent; Insurance Marketing Firm; Web Aggregator; TPA - Health Services; Surveyor (Individual); Surveyor (Corporate); Point of Sales Person (POSP) platform; All Intermediaries (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Sales & Distribution; Claims Support; Policyholder Grievance; Internal Audit
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** IRDAI (filing); IRDAI (prior approval); IRDAI (intimation); IRDAI Bima Bharosa (grievance); Partner Insurers; FIU-IND (FINnet 2.0); CERT-In; MCA (ROC); RBI (parent regulator - bank / NBFC CA); Board / Principal Officer; Statutory Auditor; Not Required

### E.15.19 MCA-CO — Companies (Companies Act, 2013)

- **C — Company Class:** Private Limited Company; Public Limited Company (Unlisted); Public Limited Company (Listed); One Person Company (OPC); Small Company; Section 8 Company; Producer Company; Nidhi Company; Government Company; Foreign Company; All Companies
- **D — Threshold / Overlay:** Paid-up capital ≥ ₹10 crore; Turnover ≥ ₹100 crore; Outstanding borrowings/deposits ≥ ₹50 crore; CSR applicable (s.135(1) thresholds); Ind AS applicable; Holding / Subsidiary company; Company accepting deposits (Chapter V); Company with foreign investment (FEMA); Dormant company (s.455); Start-up (DPIIT recognised); Company required to appoint KMP (s.203); Company requiring secretarial audit (s.204); Company requiring cost audit (s.148); All Companies (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Secretarial; Internal Audit; Tax
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Registers & Records
- **R:** High; Medium; Low
- **P (reference):** MCA (ROC) - e-Form; MCA - Regional Director; NCLT; IEPF Authority; Central Government (MCA); RBI (FEMA) / AD Bank; SEBI / Stock Exchanges (listed); Income Tax Department; Members (general meeting / website); Board / Management; Statutory Auditor; Secretarial Auditor / PCS; Cost Auditor; Not Required

### E.15.20 MCA-LLP — Limited Liability Partnerships

- **C — LLP Class:** Limited Liability Partnership (LLP); Small LLP; Foreign LLP; All LLPs
- **D — Threshold / Overlay:** Turnover above ₹40 lakh or contribution above ₹25 lakh (audit required); LLP with foreign investment (FEMA); LLP converted from company / firm; LLP with body corporate partners; All LLPs (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Secretarial; Tax
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Registers & Records
- **R:** High; Medium; Low
- **P (reference):** MCA (ROC) - LLP e-Form; MCA - Regional Director; NCLT; RBI (FEMA) / AD Bank; Income Tax Department; Partners / Designated Partners; Statutory Auditor; Not Required

### E.15.21 DATA-PRIV — Data Protection and Privacy (DPDP, IT Act, GDPR, CCPA)

- **C — Law / Jurisdiction:** DPDP Act, 2023 and DPDP Rules, 2025 (India); IT Act, 2000 and SPDI Rules, 2011 (India); EU GDPR (EU/EEA); UK GDPR and DPA 2018 (UK); CCPA as amended by CPRA (California); Sectoral data rules (RBI / SEBI / IRDAI / IFSCA); Other jurisdiction
- **D — Role:** Data Fiduciary; Significant Data Fiduciary (SDF); Data Processor; Consent Manager; Intermediary; Controller (GDPR); Processor (GDPR); Joint Controller (GDPR); EU Representative (Art. 27); Business (CCPA); Service Provider / Contractor (CCPA); Third Party (CCPA); Data Broker; Body corporate handling SPDI; All Roles (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Privacy Office (DPO); Information Security; Marketing; Customer Service & Grievance; Product & Engineering
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Notices & Consents
- **R:** High; Medium; Low
- **P (reference):** Data Protection Board of India; Affected Data Principals (intimation); Consent Manager; CERT-In; Sectoral Regulator (RBI / SEBI / IRDAI / IFSCA); EU / EEA Supervisory Authority (Lead SA); Affected Data Subjects (GDPR); California Privacy Protection Agency / Attorney General; Consumers (CCPA notices); Board / DPO; Independent Data Auditor; Not Required

### E.15.22 CYBER — Cyber Security and IT Governance

- **C — Framework:** CERT-In Directions, 2022 (IT Act s.70B); IT Act s.70 / NCIIPC (CII / Protected Systems); RBI IT and Cyber Security Directions; SEBI CSCRF; IRDAI Information and Cyber Security Guidelines, 2023; IFSCA Cyber Security Guidelines; DPDP security safeguards (Rule 6); ISO/IEC 27001:2022; NIST CSF 2.0; PCI DSS v4.0.1; All Frameworks
- **D — Entity Category:** All body corporates / service providers; Data centre / cloud / VPS / VPN provider; Critical Information Infrastructure / Protected System; Bank; NBFC (by layer); UCB (by tier); SEBI MII; SEBI Qualified RE; SEBI Mid-size RE; SEBI Small-size RE; SEBI Self-certification RE; Insurer / Insurance Intermediary; IFSCA Regulated Entity; Payment entity (card data); All (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Information Security; IT Infrastructure; Application Development; Business Continuity
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** CERT-In (incident report); NCIIPC; RBI (CSITE / Department of Supervision); SEBI (CSCRF reporting / SI Portal); IRDAI; IFSCA; Stock Exchanges / Depositories (MIIs); Data Protection Board of India; Board / IT Strategy Committee; CISO / Information Security Steering Committee; Auditor (CERT-In empanelled); Not Required

### E.15.23 LAB-POSH — Labour Codes, Shops and Establishments, and POSH

- **C — Law:** Code on Wages, 2019; Industrial Relations Code, 2020; Code on Social Security, 2020; Occupational Safety, Health and Working Conditions Code, 2020; POSH Act, 2013; Shops and Establishments Act (State); Professional Tax / Labour Welfare Fund (State); Apprentices Act, 1961; All Labour Laws
- **D — Establishment Type / Threshold:** All establishments; Establishment with 10 or more employees; Establishment with 20 or more employees; Establishment with 50 or more employees; Establishment with 100 or more employees; Establishment with 300 or more workers (standing orders); Factory; Shop / Commercial establishment; IT / ITES establishment; Contractor / Principal employer (contract labour); Inter-State migrant workers employer; Gig / Platform aggregator; Building and other construction work; Remote / work-from-home workforce; All (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Payroll; Administration & Facilities; Internal Committee (POSH)
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance; Registers & Records
- **R:** High; Medium; Low
- **P (reference):** Shram Suvidha Portal (MoLE); EPFO (Unified Portal); ESIC Portal; State Labour Department (Shops and Establishments); Inspector-cum-Facilitator; District Officer (POSH - annual report); Welfare Board (BOCW); Professional Tax Authority (State); Labour Welfare Fund Board (State); Employees (display / notice); Board (Directors' Report disclosure); Not Required

### E.15.24 TAX-GST — GST, Income-tax, TDS/TCS and State Taxes

- **C — Law:** CGST / SGST / IGST Acts, 2017; Income-tax Act, 2025; Income-tax Act, 1961 (transition / earlier years); TDS / TCS; Professional Tax (State); Stamp Duty (State); All Tax Laws
- **D — Taxpayer Type:** Regular GST taxpayer; Composition taxpayer; Input Service Distributor (ISD); GST TDS deductor; E-commerce operator (TCS); Non-resident taxable person; OIDAR service provider; Banking company / financial institution / NBFC (rule 38 ITC option); SEZ unit / developer; E-invoicing applicable taxpayer; Company assessee; Co-operative society assessee; LLP / Firm assessee; Tax audit applicable; All (ALL)
- **H:** Annually; Half Yearly; Quarterly; Monthly; Fortnightly; Weekly; Daily; Event Based; Immediately; Ongoing/Continuous; One-time; Every 2 Years; Every 3 Years; Every 5 Years
- **M:** Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management; Tax; Accounts Payable; Billing & Receivables
- **O:** Policies; Compliance; Returns & Reporting; Committee; Internal Compliance; Suggestive Compliance
- **R:** High; Medium; Low
- **P (reference):** GSTN Portal (GSTR); E-invoice IRP; E-way Bill Portal; Income-tax e-Filing Portal; TRACES (TDS / TCS); Protean (TIN); State Professional Tax Portal; GST / Income-tax Authorities (notices / appeals); Tax Auditor (CA); Board / Management; Not Required

---

## E.16 Acceptance criteria (`tests/acceptance/p03/template_import.feature`, `p05/ai_authoring.feature`)

```gherkin
Feature: Question template import

  Scenario: Valid first upload of a family template
    Given super admin downloads template "LDC-TPL-RBI-NBFC-v1.0"
    And fills 42 rows with columns B,C,D,F,G,H,K,L,M,N,O,P,Q,R,S,U,V and leaves A,E,I,J,T,W-AD blank
    When she uploads it against instrument "RBI (NBFC – Governance) Directions, 2025"
    Then the preview shows 42 NEW rows and 0 errors
    And committing creates 42 draft obligation versions with CompIDs "RBI-NBFC.GOV25.0001" to ".0042"
    And nothing is visible to tenants until a different user with plt_content_checker publishes it

  Scenario: Header tampering is rejected
    Given a workbook whose cell G2 reads "Question"
    When it is uploaded
    Then the import fails with LDC-TPL-004 naming column G and the expected header

  Scenario: Multi-value entity types with non-canonical delimiter
    Given row 5 column D reads "NBFC-Factor, Housing Finance Company (HFC)"
    When the file is validated
    Then the value is normalised to "NBFC-Factor; Housing Finance Company (HFC)" with LDC-TPL-016 (info)

  Scenario: Unknown vocabulary value with suggestion
    Given row 7 column M reads "Compliances"
    Then validation reports LDC-TPL-015 with suggestion "Compliance" and blocks commit

  Scenario: Due rule parsed into a schedule
    Given row 9 column P reads "RBI - CIMS (Supervisory Returns) — Quarterly return — Due: within 21 days of the end of each quarter"
    And column H reads "Quarterly"
    Then the obligation's schedule rule is PERIOD_END(quarter)+21 calendar days and no warning is raised

  Scenario: Round trip keeps CompIDs and retires instead of deleting
    Given an exported sheet with CompIDs ".0001" to ".0042"
    And row ".0017" column F is changed to "[RETIRED] Board composition" with S "Omitted vide RBI/DoR/2026-27/xx dated 1 Dec 2026"
    And a new row with blank E is added
    When re-uploaded
    Then the diff shows 1 RETIRE, 1 NEW, 40 NOCHANGE
    And deleting any exported row instead fails with LDC-TPL-023

  Scenario: Substantive update reaches tenants as an Update, not a Notification
    Given obligation ".0008" changes frequency from "Annually" to "Half Yearly" and is published as Substantive
    Then every tenant whose profile matches C/D receives an Updates item stating old and new requirement and action needed
    And completed instances under the old version remain unchanged

  Scenario: Tenant overlay never changes base content
    Given client admin of tenant T1 re-uploads library obligation ".0008" with a changed question text
    Then T1 sees its overlay version and the base version side by side
    And tenant T2 still sees the base text
    And an audit event TenantOverlayCreated is recorded with uploader and approver

  Scenario: VERIFY marker blocks publication
    Given row 12 column K contains "[VERIFY]"
    Then commit is allowed with LDC-TPL-026 warning
    And publish is blocked until the checker removes the marker or records a waiver with reason

  Scenario: Macro-enabled file rejected
    Given a .xlsm file renamed to .xlsx
    Then the import fails with LDC-TPL-010 before any parsing

  Scenario: AI-authored sheet uses the same contract
    Given client admin uploads a new State co-operative rule PDF and chooses family COOP-CCS
    When Vidhi drafts questions
    Then the draft is a LDC-TPL-COOP-CCS-v1.0 workbook that passes the same validator
    And every row has ai_generated = true, the prompt version and resolvable source clause IDs
    And it is downloadable for offline editing and re-upload before publication
```

NN tests:

- `NN-03_tenant_overlay_not_overwritten_by_base_update`
- `NN-04_ai_rows_never_auto_published`
- `NN-05_import_publisher_differs_from_committer`
- `NN-06_obligation_without_citation_not_publishable`
- `NN-29_retire_keeps_history`

Validator regression (CI):

- `templates/_validate_templates.py` must report PASS for every shipped template.
- Any change to `family_vocab.py` re-runs the build and the validator.
- The PR fails if a base value is removed or renamed.

---

## E.17 Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P03-E01 | NBFC layer thresholds and Top Layer status in the 2025 SBR Directions | Not re-read from primary text in this pass | Content maker (RBI) | Applicability conditions stay editable in Content Studio. C values are unaffected |
| OI-P03-E02 | Titles and numbers of RBI/DoS/2026-27/461–468 | Only /460 was confirmed (31 Jul 2026) | Content maker (RBI) | Family command lists them as [VERIFY] |
| OI-P03-E03 | UCB tier thresholds and the Board of Management threshold in the 2025 UCB directions | Source not re-read | Content maker | Tier is a C value. Thresholds sit in S and conditions |
| OI-P03-E04 | NABARD versus RBI return routing for StCBs and DCCBs | Varies by return | S5 / Return Studio | P list carries both destinations |
| OI-P03-E05 | IRDAI consolidated regulation titles (2024–26) and composite licensing after the 2025 Amendment Act | Commencement and titles not verified | Content maker (IRDAI) | Value "Composite Insurer (where licensed)" kept. Remove it by minor version if not applicable |
| OI-P03-E06 | SEBI Specialised Investment Fund and MF Lite status; AIF co-investment scheme | Recent frameworks | Content maker (SEBI) | Values marked [VERIFY] in D |
| OI-P03-E07 | MSCS Act 2023 section numbers (annual return, concurrent audit, election authority, ombudsman) | Section numbering after amendment not re-read | Content maker (Co-op) | Worked example cites s.120 [VERIFY] |
| OI-P03-E08 | Labour Code State rules and the unified portal name | Phased State notification | Content maker (Labour) | P token "Shram Suvidha Portal (MoLE)" |
| OI-P03-E09 | Income-tax Act 2025 form and section numbers; GST due-date notifications after GST 2.0 | New Act effective 1 Apr 2026 | Content maker (Tax) | Due rules flagged LDC-TPL-018 until set |
| OI-P03-E10 | California CPPA name and 2025 CCPA regulation effective dates | Agency rebranding and phased dates | Content maker (Privacy) | P token kept generic |
| OI-P03-E11 | Owner confirmation of the "Every 2/3/5 Years" frequency additions (not in IFSCA-GEN) | New values beyond the owner's list | Owner | IFSCA-GEN unchanged. Other families may drop them by minor version |
| OI-P03-E12 | Owner confirmation of the `_Template_Info` password `LDC-TPL` and visibility | Convenience control | Owner | Can be changed by a patch version |
| OI-P03-E13 | ASVS 5.0 chapter numbering for file-handling controls | Not re-read | S11 | Controls apply regardless |
| OI-P03-E90 | Dropdown values renamed in review (25 Oct 2026) to remove `[VERIFY]` from list values: "Society subject to concurrent audit (State Act threshold)", "Composite Insurer (where licensed)", "ARC eligible for additional permitted activities (NOF-based)", "Co-investment Scheme (CIV)", "Performance Benchmarking Agency", "Index Provider", "Specialized Investment Fund (SIF)", "Mutual Fund Lite (MF Lite - passive)", "Shram Suvidha Portal (MoLE)", "Managing General Agent (MGA)" | A `[VERIFY]` inside a list value would block every row that selects it (§E.4.7); the underlying facts (composite licensing, NOF threshold, State concurrent-audit thresholds) still need primary-source checks | Content makers (IRDAI, RBI, co-op, SEBI) | Values usable now; thresholds stated in Column S per row |
| OI-P03-E91 | Department codes in §E.13.2 aligned to Appendix U §U.6.1/§U.9.0 (master X-10) | Earlier long-form codes (`GOV_ADMIN` etc.) replaced; seed migration must load the short codes | P03 / P02 | `templates/_build/appendix_tables.py` regenerates §E.13 with the same codes |

---

## E.18 Sources (as of 25 October 2026)

Primary and official sources:

- RBI, Master Direction RBI/DoS/2026-27/460, NBFC – Compliance Function Directions, 2026 (31 Jul 2026) — https://rbi.org.in/ScriptS/BS_ViewMasDirections.aspx?id=13593
- RBI, Master Directions index and RE-wise directions — https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx ; https://rbi.org.in/scripts/BS_ViewREwiseDraftDirections.aspx?id=238
- MeitY, DPDP Rules 2025, G.S.R. 846(E), 13 Nov 2025 (summary: https://ssrana.in/articles/meity-notifies-final-digital-personal-data-protection-rules-2025/)
- CERT-In, Directions under s.70B(6) IT Act dated 28 Apr 2022 — https://www.cert-in.org.in
- Ministry of Labour and Employment, Labour Codes in force from 21 Nov 2025 (summaries: https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2025/government-of-india-notifies-the-labour-codes-ushers-a-new-era-of-compliances ; https://www.in.kpmg.com/taxflashnews/KPMG-Flash-News-GOI-notifies-implementation-of-Labour-Codes.pdf)
- Statutes cited in the worked examples: Banking Regulation Act 1949; RBI Act 1934; SARFAESI Act 2002; PSS Act 2007; MSCS Act 2002; SEBI Act 1992 and the MF, AIF, LODR and REIT Regulations; Insurance Act 1938; Companies Act 2013; LLP Act 2008; DPDP Act 2023; POSH Act 2013; CGST Act 2017 — https://www.indiacode.nic.in

Secondary sources (benchmarks or summaries; verify against primary text):

- SCC Online, RBI's 244 Directions (2 Dec 2025) — https://www.scconline.com/blog/post/2025/12/02/rbi-issues-directions-and-notifications-2025/
- Indian Cooperative, 27 UCB and 26 RCB directions — https://www.indiancooperative.com/co-op-news-snippets/rbi-issues-master-directions-27-for-ucbs-26-for-rural-co-op-banks/
- TaxGuru, NBFC Financial Statements Directions 2025 applicability — https://taxguru.in/?p=1015101
- YourStory, SEBI CSCRF categorisation (May 2025) — https://yourstory.com/2025/05/sebi-categorises-entities-size-risk-level-basis-cybersecurity
- Cyril Amarchand Mangaldas, Insurance distribution in India (Jan 2026) — https://corporate.cyrilamarchandblogs.com/2026/01/understanding-insurance-distribution-in-india-a-comprehensive-guide/

Owner materials (read-only, the method's source of truth):

- `SAMPLE - Finance Company Regulations 2021 - Compliance Questions.xlsx`
- `05 Insurance - IFSCA Appointed Actuary Regulations 2022.xlsx`
- the 43 finished sheets in `IFSCA Documents/IFSCA Compliance Question Sheets/` (2,809 rows)
- the owner's NBFC and IFSCA commands (management brief, 25 Oct 2026)

---

**Master integration note (pack lead, 25 October 2026).** This appendix is read with master §4 and §18, in particular X-08, X-09, X-10 (department alias map in Appendix U §U.9.0), X-28, X-29, X-38; NN-35. Where text above conflicts with them, the master prevails.
