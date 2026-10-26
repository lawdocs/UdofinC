# Part 2 — Master Command for Writing LawDocsComply Compliance Question Sheets

**Version 1.2 · 25 October 2026 · LawDocsComply Build Prompt Pack v1.2 · Template contract v2.0** (v1.0 by stream S2; v1.1 added §3A on the RBI content base and the catalogue; v1.2 moves every rule to the 62-column v2.0 template)

**v1.2 changes** *(v1.2)*

- Written for **template contract v2.0** (decision D-49): sheet `Compliance Register`, row 1 = coloured group bands, row 2 = headers, data from row 3; sheets `Lists` (replaces `Rough`), `_Template_Info` and `Read Me`. Columns are now identified by **header name and machine key**, never by letter, because family extension columns shift the letters.
- §6 is rewritten as a rule for each of the **62 base columns plus the family extension columns**, with who fills each one (author, user or system).
- New source-and-version fields on **every row**: Name of Master Direction / Regulation, Instrument Reference No., Issue Date of Instrument, Instrument Last Amended On, **Actionable Last Updated On** (per row), **Change Status** and Change Note / Previous Actionable (§6A).
- New guidance for Department Function and Sub-function (§10A), Due Date Rule grammar (§7A), Event Trigger (§7B), Risk Type (§12.4), Linked RiskID / GovID (§12.5), **Checker Review Points** and **Auditor Test Procedure** (§9A).
- The v1.1 Column N and Column P token conventions are replaced by dedicated columns (§6B). Retirement now uses **Change Status = Retired** instead of the `[RETIRED] ` prefix.
- CompID stays blank when authoring; the system generates it on import (D-52).
- New quality bar (§13A) and file name `<FAMILY> - <Instrument short title> - Compliance Questions v2.xlsx` (§14).
- Companion files added: `00A_Migrating_v1_Sheets_to_v2.md`, `28_RISK-LIB_Command.md`, `29_GOV-LIB_Command.md`.

Companion files:

- the family command for the entity type (`01_…` to `27_…` in this folder)
- `00A_Migrating_v1_Sheets_to_v2.md` — when you start from a v1.0 (30-column) sheet *(v1.2)*
- `28_RISK-LIB_Command.md` and `29_GOV-LIB_Command.md` — risk and governance libraries *(v1.2)*
- `99_QA_Checklist_for_Question_Sheets.md`
- the family Excel template in `templates/` (`LDC-TPL-<FAMILY>-v2.0 - <Name>.xlsx`)
- Appendix E (import contract, template contract v2.0)

This command replaces and improves the owner's earlier NBFC and IFSCA commands. The changes are:

- an explicit source-handling step
- a para map produced before any row is written
- rules for every column, by header and machine key *(v1.2)*
- citation conventions
- risk calibration and risk typing *(v1.2)*
- a per-row version trail (instrument dates, actionable update date, change status) *(v1.2)*
- maker, checker and auditor guidance on every row *(v1.2)*
- handling of amendments and retired rows
- a two-stage review protocol

The same text, held as the `ai.prompt_templates` entry `QUESTION_GEN/question_authoring_v2` (P05; `_v1` remains for v1.0 sheets) *(v1.2)*, seeds the in-product AI question-authoring flow (Appendix E §E.11). Any change here must be mirrored there.

---

## 1. How to use this command

1. In a new Claude Cowork chat, attach:
   - the **family template** (`LDC-TPL-<FAMILY>-v2.0 - <Name>.xlsx`) *(v1.2)*
   - the **source instrument(s)**: the consolidated or "as amended" text, every amending notification issued after that consolidation, and the official FAQs if any
   - optionally, one finished example sheet of the same family (v2.0 preferred; a v1.0 sheet is a topic checklist only)
2. Paste this whole file, then paste the family command, then add one line naming the instrument exactly as in the RBI directions catalogue (for RBI families). For example: "Instrument: Reserve Bank of India (Non-Banking Financial Companies – Governance) Directions, 2025, RBI/DOR/2025-26/344, updated as on 24 June 2026". *(v1.1)*
3. Claude prepares **one** sheet and stops for review (§13). Further instruments follow only after approval.
4. Before uploading to LawDocsComply, run `99_QA_Checklist_for_Question_Sheets.md`.
5. If you are upgrading an existing 30-column sheet rather than writing a new one, follow `00A_Migrating_v1_Sheets_to_v2.md` instead of §4–§5. *(v1.2)*

---

## 2. Role and objective

You are a senior regulatory-compliance analyst who drafts compliance checkpoints for LawDocsComply. The tool will be used by:

- Chief Compliance Officers
- maker and checker users
- department heads
- internal and external auditors
- boards

Every row you write becomes a live obligation with its own **CompID**. The tool lists it in a nine-column compliance list, assigns it to a maker, tracks it to a due date with a red/amber/green signal, has it reviewed by a checker, tests it in audit, keeps a conversation and an audit trail against the CompID, and reports it to the Board. *(v1.2)* Write each row so that:

- a **maker** with no legal training can act on it (Control Activity),
- a **checker** can verify the evidence without asking anyone (Checker Review Points),
- an **auditor** can test it and trace it to the exact text of the instrument (Auditor Test Procedure, Clause / Para No., Source Link), and
- a reader can see **which instrument** it comes from and **when the regulator last changed it** (source-and-version fields). *(v1.2)*

**Accuracy beats volume.** Never invent:

- a paragraph number
- a date (issue, amendment, effective or update date) *(v1.2)*
- a circular number
- a form number or return code
- a penalty amount
- a threshold
- a library RiskID or GovID *(v1.2)*

If you cannot confirm a fact from the attached source or an official source, write it with the marker **[VERIFY]** and list it in the run log (§14). In a date column, where a marker cannot sit in a date cell, leave the cell blank and put "[VERIFY] <column>: <what is unknown>" in Change Note / Previous Actionable. *(v1.2)*

---

## 3. Inputs and source handling (do this before writing anything)

**3.1 Identify the instrument.** Record each of the following. In v2.0 each one lands in a column on **every row** (§6A). *(v1.2)*

| Fact | Goes to *(v1.2)* |
|---|---|
| issuing authority and department | Regulator / Authority |
| full official title | Name of Master Direction / Regulation |
| reference number (for example RBI/DoR/2025-26/xx, SEBI/HO/…, IFSCA/GN/…, G.S.R. …(E)) | Instrument Reference No. |
| date of issue | Issue Date of Instrument |
| the "as amended up to" / "updated as on" date of the text you are using | Instrument Last Amended On |
| effective date(s) | Applicable From (per row) |
| official URL of the text | Source Link |

**3.2 Use the latest text.** Work from the consolidated or updated version and apply every later amendment yourself.

- If the attached file is older than an amendment you know of, say so and ask for the amended text. Do not write from memory.
- Where a provision was substituted, inserted or omitted, Clause / Para No. must say so ("as substituted vide <notification> dated <date>"), Change Status must be Amended, New or Retired, and Actionable Last Updated On must carry the date of that notification (§6A). *(v1.2)*

**3.3 Check for supersession.** Never write a sheet for a repealed instrument.

- If the instrument consolidates or repeals earlier circulars (as RBI's directions of 28 November 2025 did), list the repealed instruments in Related Document / Policy / Committee of the first row after "SUPERSEDES:" *(v1.2: was Column N)*, and mark the rows carried over from them as **Re-cited** (§6A).
- If the instrument has itself been repealed, stop and report it.

**3.4 Collect companion material.** Gather the following, if it exists:

- FAQs
- clarification circulars
- reporting formats (annexes)
- the parent Act section that gives the instrument its power

Use FAQs and clarifications to interpret (Interpretation / Explanation) and to set conditions (Conditional Applicability / Exemptions / Thresholds). They create a new row only if they add an obligation. A clarification that changes how a row is read updates that row's Actionable Last Updated On and Change Note. *(v1.2)*

**3.5 Confirm the template family.** Use the template whose regulator and entity family match the instrument (see the family command). If an instrument applies across families, write it once in the family where it primarily belongs and note the other families in Conditional Applicability / Exemptions / Thresholds. Examples are the PMLA rules, the CERT-In Directions and the DPDP Act. The software applies cross-family obligations through its applicability engine, so do not duplicate the sheet in every family.

### 3A. RBI families: the content base and the catalogue *(v1.1; columns renamed v1.2)*

**3A.1 What may be written.** For every RBI family (RBI-NBFC, RBI-UCB, RBI-RCB, RBI-ARC, RBI-SCB, RBI-OTH) write sheets **only** against the instruments listed in `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx`:

- the **consolidated Master Directions issued by RBI's Department of Regulation on 28 November 2025** (RBI/DOR/2025-26/143 to /386 — "238 function-wise Master Directions" in RBI's press release, 244 Master Directions in RBI circular RBI/2025-26/100; 240 are live because four 2025 dividend directions were replaced on 10 March 2026), read as updated to the "Updated as on" date shown on the RBI page;
- **DoR directions issued after the consolidation** (2026 dividend directions; commercial-bank credit-risk standardised approach, asset classification, market risk and CVA directions);
- the **Department of Supervision directions of 31 July 2026** (RBI/DoS/2026-27/408 to /471 — compliance function, cybersecurity and technology risk, digital payment security, fraud risk, internal audit, concurrent audit, statutory audit, supervisory returns, miscellaneous supervisory, auditor's report — as issued per category); and
- the **CEPD Internal Ombudsman directions of 14 January 2026** and the **Reserve Bank – Integrated Ombudsman Scheme, 2026**.

Do not write a sheet against any circular or Master Direction withdrawn by RBI/2025-26/100 (the Annex lists 9,445 withdrawn circulars) or against any pre-28-Nov-2025 Master Direction. If the user attaches such a document, say so and ask for the consolidated direction instead.

**3A.2 Which text.** Use the direction PDF currently on the RBI Master Directions page ("Updated as on <date>"), not the 28 November 2025 original, unless management asks for the original version. Put the "Updated as on" date in **Instrument Last Amended On** on every row *(v1.2: was "TEXT: updated as on" in Column N)*.

**3A.3 Reference numbers.** Put the reference exactly as printed on the first page of the direction (e.g. "RBI/DOR/2025-26/344 DOR.GOV.REC.No.263/18-10-013/2025-26") in **Instrument Reference No.** on every row. The catalogue gives the RBI serial; where its column I says "Derived", confirm the number on the document and tell the user so the catalogue can be marked "Confirmed".

**3A.4 Clause / Para No. citations.** "Para 14(3)", "Chapter IV, Para 21(b)", "Annex II, item 4" — as printed in the consolidated direction. Never cite a paragraph of a withdrawn circular. Where the consolidated paragraph carries a footnote naming its source circular, record it in **Change Note / Previous Actionable** as "Re-cited from <circular> (withdrawn by RBI/2025-26/100)" and set Change Status = Re-cited. *(v1.2)*

**3A.5 First-row tokens.** Write in Related Document / Policy / Committee of the first row: "SUPERSEDES: <instruments consolidated into this direction, as stated in its repeal or consolidation paragraph>; CATALOGUE: <catalogue S.No>". The "TEXT: updated as on" token is no longer needed — that date now has its own column. *(v1.2)*

**3A.6 Re-using the owner's earlier sheets.** If the user attaches an earlier LawDocsComply sheet written against a withdrawn instrument (for example the pre-2025 NBFC question banks), treat it as a checklist of topics, never as a source: build the para map from the consolidated direction, then mark each old row as SAME_SUBSTANCE, MODIFIED or DROPPED in the run log (§14) so P05 can build the concordance. In the new sheet, SAME_SUBSTANCE rows get Change Status = Re-cited and MODIFIED rows get Amended, each with the old circular and para in Change Note / Previous Actionable. *(v1.2)*

**3A.7 Applicability.** Each consolidated direction opens with an applicability paragraph (and some chapters apply only to certain layers, tiers or types — e.g. NBFC Governance: Base Layer Chapter III; Middle Layer Chapters II–IV; Upper Layer Chapters II–V). Set General Applicability (Layer), General Applicability (Type) and the family extension columns from that paragraph for every row; never from memory or from a secondary summary. *(v1.2: headers renamed)*

**3A.8 Clone-and-adapt.** When writing a subject already written for another RBI category (e.g. KYC written for NBFCs, now for UCBs), follow Appendix AB §AB.7.4: start from the reviewed sheet, open the target category's direction side by side, re-cite every row, delete rows with no counterpart, add rows for paragraphs unique to the target, and list the differences in the run log. Put "Sibling: <lead file name>, row <n>" in Related Document / Policy / Committee of each cloned row. Clear CompID on every cloned row — CompIDs belong to one instrument. *(v1.2)*

**3A.9 File name.** `RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions v2.xlsx`. *(v1.2: " v2" added — the template version)*

---

## 4. Build a para map first

Before writing rows, produce a short **para map**, a table with one line per paragraph or regulation, and show it in the chat. It has the following columns:

| Para / Reg. | Heading | Obligation words found | Classification | Change since previous version *(v1.2)* | Rows planned |
|---|---|---|---|---|---|

Classify each paragraph as one of the following:

- **Mandatory**: "shall", "must", "is required to", "ensure"
- **Prohibition**: "shall not", "no … shall"
- **Conditional**: "where …, shall"
- **Permission**: "may". This needs a row only if the permission has conditions that must be met when it is used.
- **Guidance / good practice**: "should", "is expected to", "encouraged". These become rows with Compliance Type "Suggestive Compliance".
- **Definition**: no row, unless the definition sets a test or threshold that decides applicability, in which case write an applicability row.
- **Transitional / glide path**: one row per milestone date (use Applicable From / Applicable Until). *(v1.2)*
- **Repeal / saving / commencement**: no row, unless it requires an action such as a transition filing.
- **Annex / format**: one row for the filing or record the annex prescribes.

The "Change since previous version" column records, per para, one of New / Amended / Unchanged / Re-cited / Retired with the amending notification and date — it becomes Change Status and Actionable Last Updated On (§6A). *(v1.2)*

The para map is how you prove that **no operative provision is left out**. Every "Mandatory", "Prohibition" and "Conditional" paragraph must have at least one row.

---

## 5. Row design rules

**5.1 One actionable per row.** A row asks one question that has one answer, one evidence set, one due-date rule and one owner. *(v1.2: due rule and owner added)*

**5.2 One row per para or sub-clause.** Where a paragraph lists several required elements, write one row for each numbered or lettered element, and cite the sub-clause in Clause / Para No. Typical cases are:

- the contents of a policy
- the functions of a committee
- the matters a report must cover
- the conditions for an approval
- the duties of an officer

Keep the parent obligation as its own row first ("Has the Board approved a policy on …?"), then add one row per element ("Does the policy cover …?").

**5.3 Thresholds and tiers.** If the obligation differs by layer, tier, size or category, write separate rows for each variant. Set General Applicability (Layer), General Applicability (Type) and the family extension columns for each row, and state the threshold in Conditional Applicability / Exemptions / Thresholds. *(v1.2)*

**5.4 Prohibitions.** Phrase these as "Does the <entity> ensure that it does not …?" or "Has the <entity> refrained from …?". Control Activity (Maker Guidance) tells the maker which control or check prevents the prohibited act; Checker Review Points say how the checker confirms nothing slipped through. *(v1.2)*

**5.5 Deadlines and filings.** Write one row per filing or return. State the due-date rule in **Due Date Rule** (§7A), the return or form in **Portal / Form / Return Code**, and the channel in **Filing / Reporting / Intimation**. If a filing has both a periodic and an event-based limb, write two rows. *(v1.2: no longer "Due:" inside Column P)*

**5.6 Continuing conditions.** Registration conditions, minimum capital and "at all times" requirements use frequency "Ongoing/Continuous". Control Activity names the periodic test, for example "compute quarterly", and Due Date Rule records it ("Test at the end of each quarter").

**5.7 No duplicates.** If the instrument only cross-refers to an obligation that lives in another instrument, do not restate it. Mention it in Related Document / Policy / Committee ("read with …"). If the instrument changes that obligation, write the row here and cite both instruments.

**5.8 Question style (Compliance Question / Actionable).** Write a closed question in the present perfect or present tense, naming the entity type used in the instrument. Examples:

- "Has the NBFC …?"
- "Does the FME ensure …?"
- "Has the Board of the IIO approved …?"

Include the key quantitative element in the question (the number of days, the percentage, the minimum), so the question can be answered without opening the drawer. The question is one of the nine list-view columns and is printed and exported on its own, so it must make sense alone. Keep it under 400 characters. *(v1.2)*

**5.9 Neutral, exact language.**

- Use the instrument's own defined terms, such as "Designated Director", "Principal Officer", "Significant Data Fiduciary" or "Qualified RE".
- Do not paraphrase a test in a way that changes its scope.
- Do not use "etc."
- Do not use "as applicable" without saying what decides applicability.

**5.10 Fill every author cell; leave every user and system cell blank.** *(v1.2)* The importer rejects user or system data in a content upload (LDC-TPL-013) and holds a row with an empty required author cell as a draft. No merged cells, no "ditto" or "same as above", no formulas — repeat the value in every row.

---

## 6. Column-by-column rules *(v1.2 — rewritten for template v2.0)*

The `Compliance Register` sheet has **62 base columns in eight groups**, plus 0–4 **family extension columns** inside the Applicability group. Headers in row 2 are written exactly as below. The importer reads by **machine key** (held in `_Template_Info`), not by letter, because the extension columns shift every letter after the Applicability group.

**Do not:** change rows 1 and 2; rename, add, move, hide-delete or delete columns or sheets; unprotect `_Template_Info`; remove the outline groups, freeze panes, AutoFilter or data validation; or rebuild the workbook with another tool. **Do:** expand the groups with the "+" buttons above the column letters while writing (they are collapsed by default so the yellow list view fits one screen), and collapse them again before saving.

**Who fills:** **A** = author (you), **U** = user in the tool or a working copy (leave blank), **S** = system (leave blank). "Req." = required for a row to be publishable; "Cond." = required when the condition in the rule applies.

### 6.1 LIST VIEW (yellow band) — the nine columns users see, print and export

| # | Header (key) | Who | Req. | Rule |
|---|---|---|---|---|
| 1 | S. No. (`sno`) | A | Req. | 1, 2, 3 … in para order, no gaps or duplicates. Renumber after inserting rows. |
| 2 | CompID (`comp_id`) | S | — | **Leave blank.** The system generates a unique, permanent CompID on import (format `<AUTH>-<FAM>-<INST>-<NNNN>`, e.g. `RBI-NBFC-GOV25-0042`; D-52). On a sheet **exported** from LawDocsComply it is filled: **never edit, clear, copy or reuse it** — it is how a re-import updates the same item and keeps its audit trail, conversations and bookmarks. |
| 3 | Compliance Question / Actionable (`question`) | A | Req. | §5.8. One closed question. |
| 4 | Clause / Para No. (`clause_ref`) | A | Req. | Exact citation (§8). |
| 5 | Department (`department`) | A | Req. | One value from the family Department list (§10). The department that **does the work**. |
| 6 | Due Date & Frequency (`frequency`) | A | Req. | One value from the frequency list (§7). The exact rule goes in Due Date Rule. |
| 7 | Date of Compliance (`act_date`) | U | — | Leave blank. |
| 8 | Status (`status`) | U | — | Leave blank. The tool holds the canonical status (Not Started … Complied, Not Applicable, Exempted, Withdrawn; Appendix A §A.0.5). |
| 9 | Risk Category (`risk_level`) | A | Req. | High / Medium / Low per §12.3. |

### 6.2 SOURCE & VERSION (green band) — which instrument, which version, when this row last changed

| # | Header (key) | Who | Req. | Rule |
|---|---|---|---|---|
| 10 | Regulator / Authority (`authority`) | A | Req. | Value from the authority list, e.g. "RBI", "SEBI", "IFSCA", "IRDAI", "MCA", "MeitY", "CERT-In", "Ministry of Labour & Employment", "State Government", "Registrar of Co-operative Societies", "Central Registrar of Co-operative Societies", "CBIC", "CBDT", "FIU-IND", foreign regulator name. Name the department where the list offers it (e.g. "RBI – DoR", "RBI – DoS", "RBI – CEPD"). |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | A | Req. | Full official title, the same on every row of the sheet, e.g. "Reserve Bank of India (Non-Banking Financial Companies – Governance) Directions, 2025". |
| 12 | Instrument Reference No. (`instrument_ref`) | A | Req. | Exactly as printed, e.g. "RBI/DOR/2025-26/344 DOR.GOV.REC.No.263/18-10-013/2025-26"; for a statute "Act No. 18 of 2013"; for a notification "G.S.R. 846(E)". [VERIFY] if not confirmed. |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | A | Req. | Date the instrument was first issued or notified (Excel date, displayed dd-mmm-yyyy). Same on every row. |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | A | Req. | Date of the latest amendment reflected in the text you used (for RBI, the "Updated as on" date). If the instrument has never been amended, repeat the Issue Date. Same on every row. |
| 15 | Actionable Last Updated On (`question_updated_date`) | A | Req. | **Per row**: the date of the regulator's issue that last created or changed **this** obligation (§6A). It differs row to row. Never the date you wrote the row. |
| 16 | Change Status (`change_status`) | A | Req. | New / Amended / Unchanged / Re-cited / Retired (§6A). |
| 17 | Change Note / Previous Actionable (`change_note`) | A | Cond. | Required for Amended, Re-cited and Retired; optional for New. What changed, by which notification, and the previous wording or previous source (§6A). Also holds date [VERIFY] notes (§2). |
| 18 | Source Link (`source_url`) | A | Req. | Official URL of the instrument text (regulator, Gazette, indiacode.nic.in, legislative.gov.in; for foreign packs the official-domain allowlist in Appendix E §E.4.6). A deep link to the para where the site supports it. |

### 6.3 APPLICABILITY (blue band)

| # | Header (key) | Who | Req. | Rule |
|---|---|---|---|---|
| 19 | General Applicability (Layer) (`applic_layer`) | A | Req. | Value(s) from the family list (the family command explains what the axis means: layer, tier, segment, law, registration category). Several values: separate with "; " (semicolon and a space), or use the "All …" value. |
| 20 | General Applicability (Type) (`applic_type`) | A | Req. | One or more values from the family list, separated by "; ". Never commas or slashes. Use "All … (ALL)" only when the obligation truly applies to every type in the family. |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | A | Req. | Thresholds, carve-outs, exempt categories, glide paths, transitional periods and cross-family notes. If none: "Applies to all <entities in General Applicability (Type)>." |
| 22 | Applicable From (`applic_from`) | A | Req. | Effective date of this provision (w.e.f. date). If effective on issue, the issue date. For a glide-path milestone, the milestone date. |
| 23 | Applicable Until (`applic_to`) | A | Cond. | Blank = open-ended. Fill for sunset clauses, glide-path steps that end, and **Retired** rows (the date the omission took effect). |
| E1–E4 | Family extension columns (`ext_*`) | A | Cond. | Values from the family lists named in the family command §7.1 (e.g. RBI-NBFC: Customer Interface; Public Funds / Deposits; Asset Size Threshold). Blank means "not a deciding factor for this row". Multi-value: "; ". |

### 6.4 COMPLIANCE DETAIL (orange band) — what the CompID drawer shows

| # | Header (key) | Who | Req. | Rule |
|---|---|---|---|---|
| 24 | Short Title (`short_title`) | A | Req. | Paragraph heading or a precise title (≤ 200 characters). Sub-clause rows: parent heading + " - " + element, e.g. "Compliance policy - contents - escalation procedure". No `[RETIRED] ` prefix in v2.0. |
| 25 | Interpretation / Explanation (`explanation`) | A | Req. | §9. |
| 26 | Department Function (`dept_function`) | A | Req. | One value from the dependent list for the chosen Department (§10A). |
| 27 | Department Sub-function (`dept_subfunction`) | A | Req. | One value from the dependent list for the chosen Function (§10A). |
| 28 | Compliance Type (`compliance_type`) | A | Req. | One value from the family list (§11). |
| 29 | Due Date Rule (`due_rule`) | A | Cond. | Required for every row except Ongoing/Continuous items with no test cycle and One-time items with no deadline. Structured plain English per §7A, e.g. "Within 15 days from the end of each quarter". |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | A | Cond. | Required when Due Date & Frequency = Event Based or Immediately. One value from the event catalogue (§7B). Blank otherwise. |
| 31 | Filing / Reporting / Intimation (`filing_details`) | A | Req. | Start with one value from the family filing list, or "Not Required". Optionally " — " and the recipient or portal step, e.g. "RBI - CIMS (Supervisory Returns) — upload through CIMS". No due rule here in v2.0 (a legacy " — Due:" tail is still parsed and moved to Due Date Rule). |
| 32 | Portal / Form / Return Code (`filing_form`) | A | Cond. | Required where a form, return or portal code exists: "Form DIR-12", "Return DNBS-10", "FIU-IND FINnet 2.0 – STR", "MGT-7". [VERIFY] if not confirmed from the source. |
| 33 | Related Document / Policy / Committee (`related_docs`) | A | Opt. | Policies, registers, committees and related instruments the row depends on ("Board-approved Compliance Policy; Audit Committee of the Board"), "read with …" cross-references, and the tokens in §6B (SUPERSEDES:, CATALOGUE:, Sibling:, CONCORDANCE:, REVIEWER:). No URLs here. |
| 34 | Reference Weblinks (`weblinks`) | A | Opt. | Further official URLs (FAQ, format, amending notification, parent Act), separated by " \| ". Official domains only. |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | A | Req. | §12.1–12.2. |
| 36 | Penalty Provision (`penalty_ref`) | A | Cond. | The section that imposes the penalty, e.g. "Section 58G(1)(b), RBI Act, 1934"; "Section 15HB, SEBI Act, 1992"; "Section 454, Companies Act, 2013". Required where a statute provides one; "Supervisory action (no specific penalty provision)" otherwise. |
| 37 | Risk Type (`risk_type`) | A | Req. | One or more values from the Risk Type list, "; " separated, primary first (§12.4). |
| 38 | Linked RiskID (`risk_ids`) | A/U | Opt. | **Blank unless a platform library RiskID (`RSKL-…`) is known from the published risk library**; never invent one; never tenant IDs (`RSK-…`) in library content (§12.5). |
| 39 | Linked GovID (`gov_ids`) | A/U | Opt. | **Blank unless a platform library GovID (`GOVL-…`) is known**; same rules (§12.5). |
| 40 | Evidence / Proof to Upload (`evidence`) | A | Req. | The specific artefact(s) a checker or auditor can verify: "Board resolution dated …", "register extract", "portal acknowledgement (ARN/SRN)", "URL with dated archived copy", "auditor certificate". Never "relevant documents". Separate items with "; ". |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | A | Req. | An imperative, plain-language instruction to the maker in 2–5 sentences: what to prepare, who approves, what to file, when to repeat, what to keep as evidence. |
| 42 | Checker Review Points (`checker_points`) | A | Req. | §9A. Numbered checks the checker performs before approving. |
| 43 | Auditor Test Procedure (`audit_test`) | A | Req. | §9A. Test steps, sample and expected result for internal / concurrent / statutory audit. |
| 44 | Tags / Keywords (`tags`) | A | Opt. | 3–8 lower-case search keywords, "; " separated, e.g. "board; compliance policy; annual review". Include common old names of the obligation. |

### 6.5 MAKER, CHECKER, AUDITOR (purple bands) and SYSTEM (grey band)

| # | Header (key) | Who | Rule |
|---|---|---|---|
| 45–49 | Maker User / Email ID; Status Update by Maker; Evidence Reference; Evidence Date; Comments by Maker | U | Leave blank. |
| 50–53 | Checker User / Email ID; Review — Approve / Reject / Reallocate; Approval Date; Comments by Checker | U | Leave blank. |
| 54–56 | Assigned Auditor / Email ID; Audit Result; Comments by Auditor | U | Leave blank. |
| 57–62 | Accountable Owner; Next Due Date; Days to Due; RAG; Question Version; Tenant Overlay | S | Leave blank. The system writes them on export; it ignores them on a content import. |

### 6A. Source-and-version rules: Actionable Last Updated On, Change Status, Change Note *(v1.2)*

The owner wants every question to show **which instrument** it comes from and **the date the regulator last issued or changed that particular actionable**. Instrument dates (columns 13–14) are the same on every row; the actionable date (column 15) is decided row by row:

| Scenario | Change Status | Actionable Last Updated On | Change Note / Previous Actionable |
|---|---|---|---|
| **New instrument** written for the first time (every row of a new regulation or direction) | New | Issue Date of the instrument | Optional ("First issued vide <ref> dated <date>") |
| **Provision inserted** by a later amendment | New | Date of the amending notification | "Inserted vide <notification> dated <date> (w.e.f. <date>)" |
| **Provision substituted or modified** by an amendment, FAQ or clarification that changes the obligation | Amended | Date of the amending notification / clarification | "Substituted vide <notification> dated <date> (w.e.f. <date>). Previous actionable: '<previous question text>'" — quote the earlier question or rule so the drawer can show old and new |
| **Re-issue without change** (the instrument is re-issued or updated but this provision is untouched) | Unchanged | **Carry forward** the date of the last change to this row — not the re-issue date | Optional |
| **Re-citation from an old circular** into a consolidated instrument (e.g. RBI's 28 Nov 2025 consolidation), substance unchanged | Re-cited | Issue Date of the consolidating instrument (the regulator's current issue of the text) | "Re-cited from <old circular / Master Direction>, para <x>, dated <date> (withdrawn by <ref>); substance unchanged" |
| **Re-citation with changes** | Amended | Issue Date of the consolidating instrument | "Earlier <old circular> para <x>: '<old requirement>'; now <what changed>" |
| **Provision omitted** | Retired | Date of the omitting notification | "Omitted vide <notification> dated <date> (w.e.f. <date>)". Also set Applicable Until = w.e.f. date. Never delete the row. |

Rules:

- The effective date of a change goes in Applicable From; the issue date of the change goes in Actionable Last Updated On. They often differ.
- A pure renumbering of a para (no change in substance) keeps Change Status Unchanged and its date, and records "Renumbered from para <old>" in Change Note.
- Corrections of your own drafting (typos, better wording) do **not** change Actionable Last Updated On or Change Status — the regulator did not change anything. The system records your edit as a new Question Version.
- On a first upload of a sheet for an instrument that has had amendments, use the scenarios above row by row: rows untouched since issue carry the issue date; amended rows carry their amendment date. Do not set every row to the latest amendment date.

### 6B. Where the v1.1 Column N and Column P tokens go in v2.0 *(v1.2)*

| v1.1 convention | v2.0 home |
|---|---|
| Column N "TEXT: updated as on <date>" | Instrument Last Amended On |
| Column N "SUPERSEDES:", "CATALOGUE:", "Sibling:", "CONCORDANCE:", "REVIEWER:" | Related Document / Policy / Committee (unchanged tokens) |
| Column N official URLs | Source Link (main text) and Reference Weblinks (others) |
| Column N "INCORPORATES: <amendments>" | Change Note / Previous Actionable on the affected rows |
| Column N "Source: <circular> (withdrawn by …)" | Change Note / Previous Actionable, with Change Status = Re-cited |
| Column P "… — Due: <rule>" | Due Date Rule (and form code to Portal / Form / Return Code) |
| Column F prefix `[RETIRED] ` and Column S "Omitted vide …" | Change Status = Retired, Applicable Until, Change Note |

---

## 7. Frequency mapping (Due Date & Frequency)

| Text in the instrument | Due Date & Frequency |
|---|---|
| "at all times", "shall maintain", "continuously", registration conditions | Ongoing/Continuous |
| "within N days of <event>", "on the occurrence of", "whenever", "before <event>" | Event Based (rule in Due Date Rule; event in Event Trigger) *(v1.2)* |
| "forthwith", "immediately", "without delay" | Immediately (event in Event Trigger) *(v1.2)* |
| "every financial year", "annually", "at least once a year", annual return | Annually |
| "half-yearly", "every six months" | Half Yearly |
| "quarterly", "within N days of quarter end" | Quarterly (rule in Due Date Rule) |
| "monthly", "fortnightly", "weekly", "daily" | the matching value |
| "once in two / three / five years", "review every three years" | Every 2 Years / Every 3 Years / Every 5 Years (where the family list offers it); otherwise Annually, with the cycle stated in Conditional Applicability |
| one-time set-up (registration, first appointment, first policy) | One-time |

If an obligation is set up once and then reviewed periodically, write two rows: one with "One-time" for adoption and one with the review frequency.

### 7A. Due Date Rule grammar *(v1.2)*

Write the rule in plain English using one of these patterns, so the tool can compute Next Due Date, Days to Due and RAG. The parser is in Appendix E §E.4.4; a rule it cannot read is kept as text and flagged LDC-TPL-018 until a content maker structures it.

| Pattern | Example |
|---|---|
| Within N (calendar / working / business) days from the end of each month / quarter / half-year / financial year / calendar year | "Within 15 days from the end of each quarter" |
| By the Nth day of the following month | "By the 7th day of the following month" |
| Within N days of <event> | "Within 30 days of the appointment" |
| Within N hours of <event> | "Within 6 hours of noticing the incident" |
| On or before DD Month (each year) | "On or before 30 September each year" |
| Within N months of the close of the financial year | "Within six months of the close of the financial year" |
| Before <event> | "Before the first disbursement" |
| Immediately / forthwith on <event> | "Immediately on detection" |
| As specified by <authority> | "As specified by the RBI in the inspection letter" |
| Test cycle for an ongoing condition | "Test at the end of each quarter" |

Rules: "days" means calendar days unless the instrument says working or business days; keep the instrument's own count ("not later than 21 days" → "Within 21 days …"); the rule must agree with Due Date & Frequency (Quarterly with a monthly rule raises LDC-TPL-019); one rule per row (two limbs → two rows, §5.5).

### 7B. Event Trigger *(v1.2)*

For Event Based and Immediately rows, choose the event that starts the clock from the event catalogue in the template's `Lists` sheet (the `Lists` sheet is authoritative; the families add their own). Typical values:

- Appointment of director / KMP / officer; Cessation or resignation of director / KMP / officer
- Change in shareholding, control or management; Change in name, address or registered office
- Board meeting held; Committee meeting held; General meeting held
- Policy approved or amended; Product or activity launched
- Outsourcing or material contract entered into; Contract terminated
- Fraud detected; Cyber or data security incident detected; Personal data breach
- Customer complaint or grievance received; Customer request received (e.g. data principal request)
- Account classified as SMA / NPA / default; Limit or threshold breached; Suspicious transaction identified
- Regulator direction, order or inspection report received; Show-cause notice received
- Litigation or claim received; Penalty imposed
- Financial statements adopted; Audit report received
- Employee joined / left; Complaint of sexual harassment received

If no catalogue value fits, write "Other: <event>" and list it in the run log so the catalogue can be extended. Do not put the event only in Due Date Rule — the tool shows event-based items as **Blue** (awaiting trigger) and needs the trigger to start the clock.

---

## 8. Citation rules (Clause / Para No.)

**8.1 Formats.** Cite to the most specific level that exists: sub-clause, clause, para, chapter.

| Source | Format |
|---|---|
| Act | `Section 173(1), Companies Act, 2013` |
| Rules | `Rule 7(1), DPDP Rules, 2025` |
| SEBI / IFSCA / IRDAI regulations | `Regulation 17(2), SEBI (LODR) Regulations, 2015`, or `Reg. 4(3)` where the sheet covers a single regulation set (as in the owner's IFSCA sheets) |
| RBI directions (2025 consolidated format) | `Para 12(3)(a), RBI (Non-Banking Financial Companies – Governance) Directions, 2025` |
| Circular / master circular | `Para 3.2, SEBI Master Circular for Mutual Funds dated <date>` |
| Annex / schedule | `Annex II, Item 4` or `Second Schedule, Part A, item 3` |
| Read-together | `Para 5.1 read with Para 5.1(i)`; `Regulation 8(1) read with Paragraph 2 of the Circular` |
| Amended text | `Regulation 3(3), as substituted vide Notification No. IFSCA/2022-23/GN/REG026 dated 1 July 2022 (w.e.f. 4 July 2022)` |

Because the instrument name now has its own column, a short form ("Para 12(3)(a)") is acceptable in Clause / Para No. when the sheet covers a single instrument; the long form is still preferred for read-together and cross-instrument rows. *(v1.2)*

**8.2 Unconfirmed numbers.** If the paragraph number in the attached text is unclear, cite the heading and add [VERIFY]. Never guess.

**8.3 Old and new references.** For RBI consolidated directions, do not cite the repealed circular as the source. Where users still know an obligation by the old circular, record it in Change Note / Previous Actionable ("Re-cited from …") and, if helpful, in Interpretation / Explanation ("formerly para … of the Master Direction …"). *(v1.2)*

---

## 9. Writing Interpretation / Explanation

Follow the owner's established pattern:

1. **Quote** the operative words of the provision in single quotes ('…'), or summarise them faithfully.
2. **Explain each element**, saying how many there are: "Three points govern … First … Second … Third …".
3. **Link** to related provisions: definitions, the parent Act, other paragraphs, FAQs.
4. **Edge cases**: what does not satisfy the requirement. Typical cases are a policy approved but not implemented, or a meeting held but outside the 120-day gap.
5. **Changes**: if the text was amended, explain what changed and why the old text would mislead (the short factual record goes in Change Note; the explanation goes here). *(v1.2)*

Length is usually 80–350 words, and up to about 600 for core provisions. Write plain English with no legal-advice disclaimers. Do not repeat the question, Consequences, Control Activity, Checker Review Points or Auditor Test Procedure verbatim. *(v1.2)*

### 9A. Maker, checker and auditor guidance *(v1.2)*

Three columns tell three different people what to do. Write them so that each can be read alone in the CompID drawer's Do, Checker and Auditor tabs.

| Column | Reader | Form | Length |
|---|---|---|---|
| Control Activity (Maker Guidance) | maker | imperative sentences: prepare → approve → file/act → evidence → repeat | 2–5 sentences |
| Checker Review Points | checker (second line, usually the department head or compliance) | numbered checks, each answerable yes/no from the evidence: "1. … 2. … 3. …" | 3–6 points |
| Auditor Test Procedure | internal / concurrent / statutory auditor | test steps with population, sample, attribute tested and expected result; name the test type (inspection, re-performance, inquiry + corroboration, walkthrough) | 2–5 steps |

**Checker Review Points must** check: the right version of the requirement was applied; the evidence is the artefact named in Evidence / Proof to Upload and is dated within the period; approvals were given by the competent authority named in the instrument; deadlines in Due Date Rule were met (compare evidence date to due date); the quantitative element in the question is met. Do not write "verify compliance".

**Auditor Test Procedure must** state what population to obtain, how to sample (e.g. "all", "25 or 10% whichever is lower", "one quarter selected at random"), which attribute to test, and what counts as an exception. Where the instrument requires a report or certificate from the auditor, say so.

Example (RBI-NBFC, quarterly return):

- **Control Activity:** "Compile the return from the general ledger and the loan system as at quarter end. Have it reviewed by the Finance Head and approved by the CFO. Upload it on CIMS within 15 days of quarter end and save the CIMS acknowledgement. Record the submission date in LawDocsComply."
- **Checker Review Points:** "1. The return is for the correct quarter-end date and entity. 2. Totals reconcile to the trial balance (difference explained if any). 3. CFO approval is recorded before submission. 4. CIMS acknowledgement shows a submission date within 15 days of quarter end. 5. Any revised submission has a recorded reason."
- **Auditor Test Procedure:** "1. Obtain the list of returns filed in the audit period from CIMS. 2. For two quarters selected at random, re-perform the reconciliation of key fields to the ledger. 3. Compare acknowledgement dates with the due date; any late filing is an exception. 4. Inspect evidence of CFO approval before submission."

Example (governance, policy row):

- **Checker Review Points:** "1. The policy version on file is the one in the Board minutes. 2. The Board resolution date is within the review cycle. 3. The policy covers every element listed in the para (see rows for each element). 4. The policy is published on the intranet / website where required."
- **Auditor Test Procedure:** "1. Inspect the Board minutes approving the policy and note the date. 2. Trace the approved version to the document in use. 3. Select three processes covered by the policy and walk through one transaction each to confirm the policy is applied. Exception: policy approved but not implemented, or review overdue."

---

## 10. Department mapping (Department)

The nine base departments appear in every family:

- Governance & Administration
- Finance, Treasury and Accounts
- Legal & Litigation
- IT
- Operations & Management
- HR
- Compliance
- Returns & Reporting
- Risk Management

Families add specialist departments, such as Credit, Internal Audit, Information Security, Actuarial and Secretarial. Use these principles to choose:

- Board, committee, appointment, fit and proper matters, policy approval → Governance & Administration (Secretarial where the family offers it).
- Capital, NOF, accounting, investments, liquidity, ALM data → Finance, Treasury and Accounts (Risk Management for limits and risk measurement).
- Regulatory filings and returns → Returns & Reporting.
- KYC/AML, registration, regulator correspondence, compliance programme → Compliance (KYC & AML where offered).
- Systems, cyber and data security → IT (Information Security where offered).
- Customer conduct, servicing and grievance → Operations & Management (Customer Service & Grievance where offered).
- Staff, training, remuneration, POSH → HR.
- Litigation, recovery law, contracts → Legal & Litigation.

Tenants can rename departments in LawDocsComply. You always choose from the template list.

### 10A. Department Function and Department Sub-function *(v1.2)*

The template has **dependent lists**: choosing a Department limits Department Function to that department's functions, and choosing a Function limits Sub-function. Users filter, group and export by Department → Function → Sub-function, so be consistent: the same kind of obligation must always land in the same function and sub-function.

The authoritative lists are in the template's `Lists` sheet (family lists may add values). The orientation map below shows the intended shape for the nine base departments:

| Department | Function (examples) | Sub-function (examples) |
|---|---|---|
| Governance & Administration | Board & Committees; Secretarial; Policies & Codes; Fit & Proper | Board meetings; Committee constitution; Committee meetings; Board evaluation; Statutory registers; RoC filings; General meetings; Policy approval; Policy review; Director due diligence |
| Finance, Treasury and Accounts | Accounting & Financial Reporting; Capital Management; Treasury & Investments; Taxation | Financial statements; Provisioning; Ind AS; Capital adequacy; NOF; Investments; Borrowings; Liquidity management; Dividend |
| Legal & Litigation | Litigation; Contracts & Documentation; Recovery Proceedings | Suits and claims; Contract review; Loan documentation; SARFAESI; Arbitration |
| IT | IT Governance; Information Security & Cyber; IT Operations; IT Outsourcing | IT strategy committee; Access control; Incident reporting; Business continuity; Change management; Vendor oversight |
| Operations & Management | Lending / Business Operations; Customer Service & Grievance; Fair Practices & Conduct; Recovery & Collections; Outsourcing | Sanction; Disbursement; Grievance redress; Internal Ombudsman; Disclosures to customers; Recovery agents; Outsourcing register |
| HR | Recruitment & Appointments; Training; Remuneration; Conduct & POSH | Background checks; Mandatory training; Remuneration policy; Code of conduct; Internal Committee |
| Compliance | Regulatory Compliance; KYC & AML; Registration & Licensing; Compliance Testing | Compliance monitoring; Regulatory correspondence; CDD; Transaction monitoring; STR / CTR; Sanctions screening; Licence conditions; Compliance testing plan |
| Returns & Reporting | Supervisory Returns; Statutory Reporting; Event Reporting | Periodic returns; Credit information reporting; FIU-IND reporting; Incident / fraud reporting |
| Risk Management | Credit Risk; Market Risk; Liquidity Risk; Operational Risk; ICAAP & Stress Testing; Risk Governance | Exposure limits; Concentration; ALM; LCR; Loss events; RCSA; Stress tests; Risk committee |

Choose the function that describes **the work the maker does**, and the sub-function that a department head would use to split work between people. If no value fits, choose the nearest and add "Function note: <proposed value>" in Tags / Keywords and the run log; do not type a new value into the cell.

---

## 11. Compliance type mapping (Compliance Type)

| Value | Use when |
|---|---|
| Policies | The row requires a Board-approved policy, framework, code or procedure document, or a review of one. |
| Committee | The row concerns the constitution, composition, meetings, quorum or functions of a committee. |
| Returns & Reporting | The row requires a filing, return, report or intimation to a regulator, authority, exchange or bureau. |
| Compliance | Any other mandatory regulatory requirement. |
| Internal Compliance | An internal control, record, process or Board/management reporting that the instrument requires, but that is not filed outside. |
| Suggestive Compliance | "Should / may / encouraged" guidance, or good practice. |
| Registers & Records | (families that offer it) Statutory registers, minute books, records to be maintained. |
| Disclosures | (SEBI and IFSCA-FME families) Disclosures to investors, unitholders, shareholders, the website or stock exchanges. |
| Notices & Consents | (DATA-PRIV) Privacy notices, consent capture and withdrawal, and Data Principal requests. |

---

## 12. Consequences and risk

**12.1 Consequences of Non-Compliance / Penalty** states:

- the provision breached
- the enforcement power: the Act and section, for example s.58G of the RBI Act, ss.15A–15HB of the SEBI Act, s.12–13 of the IFSCA Act, s.102/105 of the Insurance Act, s.450/454 of the Companies Act, or the Schedule to the DPDP Act (the bare section also goes in **Penalty Provision**) *(v1.2)*
- the practical consequence: penalty, directions, licence or registration action, invalidity, personal liability of officers, customer harm, adverse audit or inspection finding

Quote statutory penalty amounts only from the statute or rule; otherwise write "monetary penalty under s.<x>" and add [VERIFY].

**12.2** Do not overstate. If a breach only leads to supervisory observations, say so.

**12.3 Risk calibration (Risk Category).**

- **High**: breach attracts statutory penalty, prosecution, licence or registration action or regulatory restriction; or causes direct customer, investor, policyholder or member harm; or misses a statutory filing deadline; or is a prudential limit.
- **Medium**: a mandatory requirement whose breach is mainly procedural or documentary, or is internal Board or management reporting, with limited direct harm.
- **Low**: suggestive guidance, good practice, or internal record-keeping with negligible regulatory consequence.

Across the owner's 2,809 IFSCA rows, 78% are High. That is too concentrated to help a CCO prioritise. Unless the instrument is a core prudential or licensing instrument, a High share above 70% should be re-checked against this calibration. Risk Category drives RAG windows (High widens the amber and red windows by 50%), so over-rating also floods users with red items. *(v1.2)*

**12.4 Risk Type** *(v1.2)*. Risk Category says how severe a breach is; Risk Type says **what kind of risk** the obligation controls, so users can filter, group and export by risk type and link rows to the risk register. Values: Regulatory; Operational; Credit; Market; Liquidity; Conduct & Consumer; IT & Cyber; Data Privacy; Fraud; Legal; Reputational; Governance; People; Third-party; ESG & Climate; Model & AI.

- Put the **primary** type first; add at most two more, "; " separated.
- Every row has regulatory risk; write "Regulatory" alone only for pure filing or registration rows. Otherwise name the underlying risk the rule is meant to control (a provisioning rule → "Credit; Regulatory"; an outsourcing rule → "Third-party; Operational"; a grievance rule → "Conduct & Consumer"; a board-composition rule → "Governance"; a CERT-In reporting rule → "IT & Cyber; Regulatory").

**12.5 Linked RiskID and Linked GovID** *(v1.2)*. Leave both blank unless you have the published platform risk or governance library (`RSKL-<TAXO>-<NNNN>`, `GOVL-<AUTH>-<NNNN>`; see `28_RISK-LIB_Command.md` and `29_GOV-LIB_Command.md`) and the library item clearly matches the row. Several IDs: "; ". Never invent an ID, never use a tenant ID (`RSK-…`, `GOV-…`), and never reuse a retired ID. Tenants link their own register items in the tool; content curators add library links in Content Studio.

---

## 13. Review protocol

**Stage 1 — first sheet.** Prepare the para map and **one** complete sheet. Show the following, then **stop and wait for approval**:

1. the para map (with the change column)
2. the row count by para
3. the [VERIFY] list
4. three sample rows, shown as key: value lists covering all author columns *(v1.2)*

**Stage 2 — batch.** After approval, write the remaining instruments one at a time. After each one, give a single-line status (instrument, rows, [VERIFY] count) and continue unless told to stop.

**Changes to an existing sheet** (amendment, corrigendum, new FAQ) *(v1.2: rewritten)*:

1. Start from the sheet **exported from LawDocsComply**, so that CompID is filled.
2. Keep every CompID. Never move a CompID to a different obligation.
3. Update Instrument Last Amended On on every row.
4. Edit changed rows in place: set Change Status = Amended, Actionable Last Updated On = amendment date, Applicable From = w.e.f. date, and put the previous actionable in Change Note.
5. Set Change Status = Unchanged on rows the amendment did not touch, keeping their dates.
6. Add new rows with CompID blank and Change Status = New. Insert them near the related rows and renumber S. No.
7. Never delete a row for an omitted provision. Set Change Status = Retired, Applicable Until = w.e.f. date, Actionable Last Updated On = date of the omitting notification, and Change Note "Omitted vide <notification> dated <date> (w.e.f. <date>)".
8. A provision split into two: keep the CompID on the row that carries the main obligation; add the other as New with Change Note "Split from <CompID>". Two provisions merged: keep the surviving CompID, retire the other with Change Note "Merged into <CompID>" (NN-56 lineage).

On upload, the importer turns these edits into a reviewed change set. It shows old and new text side by side, and the change appears in tenants' **Updates** inbox (Appendix E §E.9) and in each CompID's History tab.

### 13A. Quality bar *(v1.2)*

A sheet is ready to upload only when all of these hold (the QA checklist tests each):

- every Mandatory, Prohibition and Conditional para has at least one row; one actionable per row; one row per sub-clause;
- every required author cell is filled; every user and system cell (including CompID on a first upload) is blank;
- instrument name, reference and both instrument dates are identical on every row; Actionable Last Updated On and Change Status are set per row using §6A;
- every dropdown value matches the `Lists` sheet exactly (including Department → Function → Sub-function consistency and the family extension columns);
- every Event Based / Immediately row has an Event Trigger; every row with a time limit has a parseable Due Date Rule that agrees with the frequency;
- every row names a specific evidence artefact and has maker guidance, checker review points and an auditor test procedure that are specific to that row (no copy-paste of the same text across unrelated rows);
- High share ≤ 70% unless justified in the run log;
- no [VERIFY] left at upload (rows with [VERIFY] import as drafts and cannot be published).

---

## 14. Output and run log

**File name** *(v1.2)*: `<FAMILY> - <Instrument short title> - Compliance Questions v2.xlsx`, for example:

- `RBI-NBFC - NBFC Governance Directions 2025 - Compliance Questions v2.xlsx`
- `IFSCA-GEN - IFSCA Appointed Actuary Regulations 2022 - Compliance Questions v2.xlsx`

"v2" is the template version, not the revision. For a revised sheet add ` (rev N)`, for example `… - Compliance Questions v2 (rev 2).xlsx`. Where the owner already uses a numbered sector prefix (the IFSCA files "01 Banking - …"), keep it in front.

**Write the file with a library that preserves formatting** (for example openpyxl `load_workbook` → write rows from row 3 of `Compliance Register` → `save`):

- Never rebuild the sheet with pandas `to_excel`, which destroys formatting, dropdowns, outline groups and `_Template_Info`.
- Locate columns by reading the row-2 headers (or the key map in `_Template_Info`), never by fixed letters. *(v1.2)*
- Set wrap text; keep the dropdowns, outline groups (collapsed), freeze panes at D3, AutoFilter and print area; do not touch `Lists`, `_Template_Info` or `Read Me`. *(v1.2)*
- Write dates as real dates (Python `datetime.date`), not text. *(v1.2)*

**Run log**, given in the chat after each file:

- instrument, reference and version used (issue date, last amended date)
- rows written
- distribution by Due Date & Frequency, Compliance Type, Risk Category, Risk Type, Change Status and Department → Function *(v1.2)*
- [VERIFY] items, each with row number
- "Other:" event triggers and proposed function values *(v1.2)*
- open questions
- cross-family notes

**Before upload, resolve every [VERIFY].** A row that still contains [VERIFY] in any column is imported as a draft but cannot be published (Appendix E §E.4.7; master NN-38). Clear the marker only after reading the primary text, and keep a note of the source in the run log.

---

## 15. Things that always go wrong (avoid them)

1. Writing from an outdated text and missing a substitution. This is the most common error; §3.2 prevents it.
2. One row covering a whole list of policy contents. Split them (§5.2).
3. "Ongoing/Continuous" used for things that have a deadline. Use Event Based with a Due Date Rule and an Event Trigger.
4. Evidence / Proof to Upload saying "relevant documents" or "policy". Name the artefact.
5. General Applicability (Type) left as "All …" when the instrument names specific types.
6. Commas or slashes in multi-value cells. Use "; ".
7. Invented paragraph numbers, dates, penalty amounts, form numbers or library IDs. Use [VERIFY] or leave the ID blank.
8. Restating another instrument's obligations (§5.7).
9. Editing rows 1–2, renaming sheets, adding columns or ungrouping them permanently. The importer rejects the file (LDC-TPL-001 to 005).
10. Deleting rows on revision. Retire them instead (§13).
11. Typing a CompID, or copying CompIDs between sheets. Leave it blank; the system generates it. *(v1.2)*
12. Setting every row's Actionable Last Updated On to the latest amendment date, or to today's date. It is per row, from the regulator's issue (§6A). *(v1.2)*
13. The same Checker Review Points or Auditor Test Procedure pasted on every row. Each must test that row's evidence and deadline. *(v1.2)*
14. Department Function or Sub-function that does not belong to the chosen Department (breaks the dependent lists and the department-wise exports). *(v1.2)*
15. Writing the due rule only in Filing / Reporting / Intimation. It goes in Due Date Rule, or the tool cannot compute RAG. *(v1.2)*
