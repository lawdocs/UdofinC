# 99 — QA Checklist for LawDocsComply Question Sheets

**Version 1.2 · 25 October 2026 · Template contract v2.0.** Run this checklist on every sheet before you upload it. The checks marked **[auto]** are also enforced by the LawDocsComply importer (Appendix E §E.7), so a sheet that fails one is rejected or flagged in the preview. The other checks are judgement checks for the reviewer. Columns are named by **header (machine key)**, not by letter, because family extension columns shift the letters.

**v1.2 changes** *(v1.2)*

- Rewritten for the 62-column v2.0 template (`Compliance Register`, `Lists`, `_Template_Info`, `Read Me`); v1.0 checks on columns A–AD retired (a v1.0 sheet is checked after migration, see `00A_Migrating_v1_Sheets_to_v2.md`).
- New section F (source and version: instrument fields, Actionable Last Updated On, Change Status) and section G (maker, checker and auditor guidance).
- Due-date checks now test Due Date Rule and Event Trigger; retirement checks test Change Status = Retired instead of the `[RETIRED] ` prefix.
- New checks for Department Function / Sub-function consistency, family extension columns, Risk Type and linked IDs.

## A. File and structure

| # | Check | Pass rule |
|---|---|---|
| A1 [auto] | Correct family template | `_Template_Info` template code matches the instrument's family and version (e.g., `LDC-TPL-RBI-NBFC-v2.0`) |
| A2 [auto] | Sheets intact | Sheets `Compliance Register`, `Lists`, `_Template_Info` and `Read Me` are present and unrenamed; `_Template_Info` is still protected |
| A3 [auto] | Rows 1–2 unchanged | The row-2 header hash equals the value in `_Template_Info`; the row-1 group bands (LIST VIEW, SOURCE & VERSION, APPLICABILITY, COMPLIANCE DETAIL, MAKER, CHECKER, AUDITOR, SYSTEM) are unchanged |
| A4 [auto] | Columns unchanged | 62 base columns plus exactly the family's extension columns, in contract order, matched by machine key; no inserted, deleted or renamed columns |
| A5 | File name | `<FAMILY> - <Instrument short title> - Compliance Questions v2.xlsx` (revisions add ` (rev N)`); RBI families as in master §3A.9 |
| A6 | Workbook behaviour kept | Dropdowns work on every list column (including Department → Function → Sub-function dependent lists and extension columns); outline groups 2–8 exist and are collapsed; freeze panes at D3; AutoFilter on row 2; print area A:I; text wraps |
| A7 | Data starts at row 3 | No blank rows between data rows; no notes or totals below the data; no merged cells, formulas or "ditto" values in data rows |

## B. Coverage

| # | Check | Pass rule |
|---|---|---|
| B1 | Para map produced | Every paragraph classed as Mandatory, Prohibition or Conditional has at least one row; the para map's change column is filled |
| B2 | Sub-clauses split | One row per para or sub-clause: lists of policy contents, committee functions, report matters and conditions appear as one row per element |
| B3 | Thresholds split | Each layer, tier or size variant has its own row, with General Applicability (Layer), General Applicability (Type) and the extension columns set |
| B4 | Filings | Every return or intimation in the instrument and its annexes has its own row |
| B5 | Transitional dates | Each glide-path or commencement milestone has its own row, with Applicable From (and Applicable Until where a step ends) set |
| B6 | No duplicates | Obligations from other instruments are cross-referenced in Related Document / Policy / Committee ("read with …"), not restated |
| B7 | Row count is plausible | Roughly one row per operative sub-clause. Short circulars usually produce 8–25 rows, regulations 40–180, handbooks 150–400. Never pad |

## C. Column rules

| # | Check | Pass rule |
|---|---|---|
| C1 [auto] | User and system cells blank | CompID (`comp_id`, on a first upload), Date of Compliance, Status, the MAKER, CHECKER and AUDITOR groups (45–56) and the SYSTEM group (57–62) are empty |
| C2 [auto] | Serial numbers | S. No. runs 1..n with no gaps or duplicates |
| C3 [auto] | Dropdown values | Department, Due Date & Frequency, Risk Category, Regulator / Authority, Change Status, General Applicability (Layer) and (Type), extension columns, Department Function, Department Sub-function, Compliance Type, Event Trigger and Risk Type use list values only; multi-value cells use "; "; Filing / Reporting / Intimation starts with a list value |
| C4 [auto] | Dependent lists consistent | Department Function belongs to the chosen Department and Department Sub-function belongs to the chosen Function |
| C5 [auto] | Required author cells filled | S. No., question, clause_ref, department, frequency, risk_level, authority, instrument_name, instrument_ref, both instrument dates, question_updated_date, change_status, source_url, applic_layer, applic_type, conditions, applic_from, short_title, explanation, dept_function, dept_subfunction, compliance_type, filing_details, consequences, risk_type, evidence, control_activity, checker_points and audit_test are non-empty |
| C6 [auto] | Date cells are dates | The five author date columns hold real dates (not text) or are blank where allowed |
| C7 | Question form | Compliance Question / Actionable is one closed question, names the entity, states the key number and makes sense alone in the list view and export |
| C8 | Citation | Clause / Para No. cites the most specific level and states "as substituted vide …" wherever the text was amended. Nothing is invented |
| C9 | Explanation | Interpretation / Explanation quotes the provision, explains each element, links related provisions and covers edge cases |
| C10 | Links | Source Link and Reference Weblinks use official domains only; Reference Weblinks are " \| " separated; no URLs in Related Document / Policy / Committee |
| C11 [auto] | Due-date rule | Every time-bound row has a Due Date Rule in the master §7A grammar, and Due Date & Frequency is consistent with it (LDC-TPL-018 / 019); no rule is left only inside Filing / Reporting / Intimation |
| C12 [auto] | Event trigger | Every Event Based or Immediately row has an Event Trigger; non-event rows leave it blank; any "Other: …" value is listed in the run log |
| C13 | Consequence | Consequences of Non-Compliance / Penalty names the provision breached, the enforcement section and the consequence; Penalty Provision holds the bare section; amounts are from statute or marked [VERIFY] |
| C14 | Risk calibration | The High / Medium / Low split follows master §12.3. A High share above 70% is justified in the run log |
| C15 | Risk Type | Primary type first, at most three, chosen per master §12.4; not "Regulatory" alone except for pure filing / registration rows |
| C16 [auto] | Linked IDs | Linked RiskID holds only `RSKL-…` and Linked GovID only `GOVL-…` IDs that exist in the published libraries, or is blank; no tenant IDs |
| C17 | Exemptions | Conditional Applicability / Exemptions / Thresholds states thresholds, carve-outs and commencement, or "Applies to all …" |
| C18 | Evidence | Evidence / Proof to Upload names a checkable artefact. Generic text such as "relevant documents" fails |
| C19 | Department mapping | Department is the department that does the work; Function and Sub-function follow the family's mapping (family command §7.2) consistently across rows |
| C20 | Extension columns | Each family extension column is filled where it decides applicability and blank otherwise; values are consistent with Layer, Type and Conditions |

## D. Accuracy

| # | Check | Pass rule |
|---|---|---|
| D1 | Latest text | The source is the consolidated or "as amended up to" version, with later amendments applied |
| D2 | Not repealed | The instrument is in force. Instruments it repeals are listed after "SUPERSEDES:" in Related Document / Policy / Committee of the first row |
| D3 | [VERIFY] list | Every unconfirmed number or date is marked (date gaps noted in Change Note / Previous Actionable), and each one appears in the run log with its row number |
| D4 | Defined terms | The instrument's own defined terms are used, and no test is widened or narrowed by paraphrase |
| D5 | Spot check | The reviewer re-reads 10% of rows (minimum 5) against the source text, including their Actionable Last Updated On and Change Status |
| D6 [auto] | [VERIFY] resolved before publication | No cell still contains [VERIFY] when the sheet is submitted for publication; otherwise the importer keeps it as draft (LDC-TPL-026) or the checker records a waiver with reason |

## E. Revisions (re-uploads of an exported sheet)

| # | Check | Pass rule |
|---|---|---|
| E1 [auto] | CompIDs kept | Every exported CompID is present and unchanged; no CompID is moved to a different obligation or copied to another row; new rows have CompID blank |
| E2 [auto] | Retired rows | Omitted provisions have Change Status = Retired, Applicable Until = w.e.f. date and Change Note "Omitted vide …". No rows are deleted |
| E3 | Change records | Each changed row has Change Status = Amended (or New), Actionable Last Updated On = date of the change, and the previous actionable in Change Note; untouched rows are Unchanged with their earlier dates |
| E4 | Splits and merges | A split keeps the CompID on the main obligation and notes "Split from <CompID>" on the new row; a merge retires one row with "Merged into <CompID>" |
| E5 | Instrument dates | Instrument Last Amended On is updated on every row to the amendment now applied |

## F. Source and version *(v1.2)*

| # | Check | Pass rule |
|---|---|---|
| F1 [auto] | Instrument fields uniform | Regulator / Authority, Name of Master Direction / Regulation, Instrument Reference No., Issue Date of Instrument and Instrument Last Amended On are identical on every row of the sheet |
| F2 | Instrument fields correct | Title and reference match the first page of the instrument (and the catalogue row for RBI families); Instrument Last Amended On is the "as amended / updated as on" date of the text used |
| F3 [auto] | Date logic | Issue Date ≤ Instrument Last Amended On; Issue Date ≤ Actionable Last Updated On ≤ Instrument Last Amended On; Applicable From ≤ Applicable Until where both are set |
| F4 | Per-row update dates | Actionable Last Updated On is set row by row per master §6A — not one date copied to every row, and never the authoring date |
| F5 | Change Status logic | New / Amended / Unchanged / Re-cited / Retired chosen per master §6A; rows from consolidated RBI directions that carry forward withdrawn circulars are Re-cited with the old source in Change Note |
| F6 [auto] | Change Note present | Change Note / Previous Actionable is filled for every Amended, Re-cited and Retired row |

## G. Maker, checker and auditor guidance *(v1.2)*

| # | Check | Pass rule |
|---|---|---|
| G1 | Control activity | Control Activity (Maker Guidance) is an imperative of 2–5 sentences: prepare, approve, file / act, retain evidence, repeat |
| G2 | Checker review points | Checker Review Points are 3–6 numbered checks, each answerable yes / no from the named evidence, including the deadline test and the competent-approval test; "verify compliance" fails |
| G3 | Auditor test procedure | Auditor Test Procedure names the population, sample, attribute tested, test type and what counts as an exception |
| G4 | Row-specific | Guidance is specific to the row: the same checker or auditor text pasted on unrelated rows fails (proposed importer warning when more than 20% of rows carry identical text; see `_contrib/v12/T2_crossfile.md`) |
| G5 | Consistency | Evidence / Proof to Upload, Control Activity, Checker Review Points and Auditor Test Procedure refer to the same artefacts and the same deadline as Due Date Rule |

**Sign-off:** preparer, reviewer, date, and the instrument version used. Record these in the run log and in LawDocsComply Content Studio when you upload.
