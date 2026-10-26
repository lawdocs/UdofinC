# 00A — Migrating v1.0 (30-column) Question Sheets to Template v2.0 *(v1.2 — new)*

**Version 1.2 · 25 October 2026.** Use with `00_Part2_Master_Command.md` (§6, §6A, §6B, §9A, §10A) and the family command (§7). Applies to the owner's existing NBFC and IFSCA sheets and to any sheet built on an `LDC-TPL-<FAMILY>-v1.0` template.

**v1.2 changes** *(v1.2)* — New file. Explains what the importer maps automatically from a v1.0 sheet (legacy map, decision D-49) and what an author must add by hand so the migrated rows meet the v2.0 quality bar (master §13A).

---

## 1. Two ways to migrate

| Route | When | What happens |
|---|---|---|
| **A. Import the v1.0 sheet as it is** | You need the content in the tool now | The importer reads the v1.0 sheet through the legacy map (§2), asks you to confirm the instrument (name, reference, dates) from the file name or a catalogue row, and creates draft rows. Fields with no v1.0 source stay empty and the rows are flagged "v2 fields incomplete" until filled in Content Studio or by re-upload. |
| **B. Rebuild on the v2.0 template** (recommended for publication) | The sheet will be published to tenants | Copy the content into `LDC-TPL-<FAMILY>-v2.0` using §2 for the mapped columns, then add the fields in §3. Upload as a v2.0 sheet. |

Either way, if the v1.0 sheet was **written against a withdrawn RBI instrument** (pre-28-Nov-2025 Master Directions or circulars withdrawn by RBI/2025-26/100), do not migrate it row for row: follow master §3A.6 — rebuild from the consolidated direction and use the old sheet only as a topic checklist.

## 2. What the legacy map carries over automatically

| v1.0 column | v2.0 field (key) | Note |
|---|---|---|
| A Checkbox | — | Ignored |
| B Serial No. | S. No. (`sno`) | |
| C General Applicability(Layer) | General Applicability (Layer) (`applic_layer`) | Values checked against the v2.0 list |
| D General Applicability(Type) | General Applicability (Type) (`applic_type`) | "; " delimiter kept |
| E CompID | CompID (`comp_id`) | Existing CompIDs are kept; blank ones are generated |
| F Short Title | Short Title (`short_title`) | A `[RETIRED] ` prefix sets Change Status = Retired and is removed |
| G Compliance Question / Actionable | Compliance Question / Actionable (`question`) | |
| H Due date & Frequency | Due Date & Frequency (`frequency`) | |
| I Date of Compliance | Date of Compliance (`act_date`) | User data — ignored on a content import |
| J Status | Status (`status`) | User data — ignored on a content import |
| K Clause or Para no. | Clause / Para No. (`clause_ref`) | |
| L Interpretation / Explanation | Interpretation / Explanation (`explanation`) | |
| M Department | Department (`department`) | |
| N Related Document or Compliance or Weblinks | Related Document / Policy / Committee (`related_docs`) + Reference Weblinks (`weblinks`) | Split on URLs; tokens per master §6B |
| O Compliance Type | Compliance Type (`compliance_type`) | |
| P Filing and Reporting details / Intimation | Filing / Reporting / Intimation (`filing_details`) + Due Date Rule (`due_rule`) | The " — Due: …" tail moves to Due Date Rule |
| Q Consequences | Consequences of Non-Compliance / Penalty (`consequences`) | |
| R Risk Categorization | Risk Category (`risk_level`) | |
| S Conditional Applicability / Exemptions | Conditional Applicability / Exemptions / Thresholds (`conditions`) | |
| T Maker | Maker User / Email ID (`maker`) | User data |
| U Upload Document or Evidence | Evidence / Proof to Upload (`evidence`) | |
| V Control Activity | Control Activity (Maker Guidance) (`control_activity`) | |
| W–AD | Maker status, maker comments, checker, decision, checker comments, auditor, auditor comments | User data (Z goes to Date of Compliance if blank, else Approval Date, with a warning) |
| File name / catalogue row | Regulator / Authority, Name of Master Direction / Regulation, Instrument Reference No., Issue Date, Instrument Last Amended On | Confirmed by the uploader at import |

## 3. What you must add by hand

| v2.0 field | How to fill it on a migrated sheet |
|---|---|
| Instrument fields (10–14) | Check the importer's proposal against the first page of the instrument; same value on every row. For RBI use the "Updated as on" date for Instrument Last Amended On. |
| Actionable Last Updated On (15) | Per row (master §6A). If the v1.0 sheet was written from an "as amended" text, use the amendment dates shown in the text's footnotes for the affected paras and the issue date for the rest. If you cannot tell, write the Issue Date and put "[VERIFY] actionable date" in Change Note. |
| Change Status (16) | On a first v2.0 upload: New for every row, unless the row was re-cited from a withdrawn instrument (Re-cited) or the v1.0 sheet already showed an amendment (Amended). Retired for `[RETIRED] ` rows. |
| Change Note / Previous Actionable (17) | Move "as substituted vide …" history from Column K and "INCORPORATES:" / "Source:" tokens from Column N here. |
| Source Link (18) | The official URL from v1.0 Column N, or the instrument page. |
| Applicable From / Until (22–23) | Effective dates from Column S text; Applicable Until for retired rows. |
| Family extension columns | Set from the family command §7.1 where they decide applicability. |
| Department Function / Sub-function (26–27) | Choose from the dependent lists (master §10A, family command §7.2). Do this department by department so the mapping stays consistent. |
| Due Date Rule (29) | Moved automatically from "Due:"; rewrite any rule the parser flags (LDC-TPL-018) into the master §7A grammar. Add rules for time-bound rows that had none. |
| Event Trigger (30) | For every Event Based / Immediately row. |
| Portal / Form / Return Code (32) | Move form or return names out of the Filing text. |
| Penalty Provision (36) | The bare section from the v1.0 Consequences text. |
| Risk Type (37) | Per master §12.4. |
| Linked RiskID / GovID (38–39) | Blank unless library IDs are known. |
| Checker Review Points (42) and Auditor Test Procedure (43) | New in v2.0 — write them for every row (master §9A). This is the largest piece of migration work; do it with the source open, not by copying one text to every row. |
| Tags / Keywords (44) | Optional; include the old circular name users know. |

## 4. Order of work

1. Confirm the instrument is in force and is the latest text (master §3).
2. Import or copy the mapped columns (§2) and fix any list-value errors the preview shows.
3. Fill the source-and-version block (fields 10–18) and Change Status for every row.
4. Fill Department Function / Sub-function, Due Date Rule, Event Trigger, form codes, Penalty Provision and Risk Type.
5. Write Checker Review Points and Auditor Test Procedure row by row.
6. Run `99_QA_Checklist_for_Question_Sheets.md`; resolve [VERIFY]; upload as v2.0. Existing CompIDs stay; the change set shows the migration as field additions, not as a content change, so tenants do not get a substantive Updates notice unless a row's obligation actually changed.

## 5. Run log for a migration

Report: source sheet name and row count; rows mapped; rows needing manual instrument confirmation; Change Status distribution; rows with [VERIFY] actionable dates; Department → Function distribution; rows whose v1.0 Due text could not be parsed; and any v1.0 row dropped or re-cited (with reason).
