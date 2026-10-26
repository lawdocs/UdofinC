# 99 — QA Checklist for LawDocsComply Question Sheets

**Version 1.0 · 25 October 2026.** Run this checklist on every sheet before you upload it. The checks marked **[auto]** are also enforced by the LawDocsComply importer (Appendix E §E.7), so a sheet that fails one is rejected or flagged in the preview. The other checks are judgement checks for the reviewer.

## A. File and structure

| # | Check | Pass rule |
|---|---|---|
| A1 [auto] | Correct family template | `_Template_Info` template code matches the instrument's family (e.g., `LDC-TPL-RBI-NBFC-v1.0`) |
| A2 [auto] | Sheets intact | Sheets are `Sheet1`, `Rough` and `_Template_Info`, in that order and unrenamed |
| A3 [auto] | Rows 1–2 unchanged | The row-2 SHA-256 equals the value in `_Template_Info`, and the merged ranges in row 1 are unchanged |
| A4 [auto] | Columns unchanged | Exactly 30 columns, A to AD, with no inserted or hidden columns |
| A5 | File name | `<Family> - <Instrument short title> <Year>[ vN].xlsx` |
| A6 | Formatting kept | The dropdowns still work in C, D, H, M, O, R and P, and text wraps |

## B. Coverage

| # | Check | Pass rule |
|---|---|---|
| B1 | Para map produced | Every paragraph classed as Mandatory, Prohibition or Conditional has at least one row |
| B2 | Sub-clauses split | Lists of policy contents, committee functions, report matters and conditions appear as one row per element |
| B3 | Thresholds split | Each layer, tier or size variant has its own row, with Columns C and D set |
| B4 | Filings | Every return or intimation in the instrument and its annexes has its own row |
| B5 | Transitional dates | Each glide-path or commencement milestone has its own row, with the date given in Column S |
| B6 | No duplicates | Obligations from other instruments are cross-referenced in Column N, not restated |
| B7 | Row count is plausible | The count is roughly one row per operative sub-clause. Short circulars usually produce 8–25 rows, regulations 40–180, handbooks 150–400. Never pad |

## C. Column rules

| # | Check | Pass rule |
|---|---|---|
| C1 [auto] | System and user columns blank | A, E (on a first upload), I, J, T and W–AD are empty |
| C2 [auto] | Serial numbers | B runs 1..n with no gaps or duplicates |
| C3 [auto] | Dropdown values | C, D, H, M, O and R use list values only. D uses "; " between values. P starts with a list value |
| C4 [auto] | Required cells filled | B, C, D, F, G, H, K, L, M, O, P, Q, R, S, U and V are non-empty |
| C5 | Question form | G is one closed question, names the entity and states the key number |
| C6 | Citation | K cites the most specific level and states "as substituted vide …" wherever the text was amended. Nothing is invented |
| C7 | Explanation | L quotes the provision, explains each element, links related provisions and covers edge cases |
| C8 | Weblinks | N follows the format `<title> dated <date> \| <official URL> \| … \| INCORPORATES: … \| SUPERSEDES: …` and uses official domains only |
| C9 | Due-date rule | Every time-bound row has "Due: <rule>" in P, and H is consistent with it |
| C10 | Consequence | Q names the provision breached, the enforcement section and the consequence. Penalty amounts are taken from statute or marked [VERIFY] |
| C11 | Risk calibration | The High / Medium / Low split follows the master command §12.3. A High share above 70% is justified in the run log |
| C12 | Exemptions | S states thresholds, carve-outs and commencement, or "Applies to all …" |
| C13 | Evidence | U names a checkable artefact. Generic text such as "relevant documents" fails |
| C14 | Control activity | V is an imperative of 2–5 sentences: prepare, approve, file, repeat, retain |

## D. Accuracy

| # | Check | Pass rule |
|---|---|---|
| D1 | Latest text | The source is the consolidated or "as amended up to" version, with later amendments applied |
| D2 | Not repealed | The instrument is in force. Instruments it repeals are listed under SUPERSEDES |
| D3 | [VERIFY] list | Every unconfirmed number or date is marked, and each one appears in the run log with its row number |
| D4 | Defined terms | The instrument's own defined terms are used, and no test is widened or narrowed by paraphrase |
| D5 | Spot check | The reviewer re-reads 10% of rows (minimum 5) against the source text |
| D6 [auto] | [VERIFY] resolved before publication | No cell still contains [VERIFY] when the sheet is submitted for publication; otherwise the importer keeps it as draft (LDC-TPL-026) or the checker records a waiver with reason |

## E. Revisions (re-uploads of an exported sheet)

| # | Check | Pass rule |
|---|---|---|
| E1 [auto] | CompIDs kept | Every exported CompID in E is present and unchanged. New rows have E blank |
| E2 [auto] | Retired rows | Omitted provisions are marked `[RETIRED] ` in F, with the omitting notification in S. No rows are deleted |
| E3 | Change note | The run log lists each changed CompID with old and new text, for the Updates notice |

**Sign-off:** preparer, reviewer, date, and the instrument version used. Record these in the run log and in LawDocsComply Content Studio when you upload.
