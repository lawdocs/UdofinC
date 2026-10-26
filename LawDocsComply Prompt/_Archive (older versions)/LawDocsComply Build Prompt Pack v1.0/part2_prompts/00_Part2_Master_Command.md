# Part 2 — Master Command for Writing LawDocsComply Compliance Question Sheets

**Version 1.0 · 25 October 2026 · LawDocsComply Build Prompt Pack v1.0 (stream S2)**
Companion files:

- the family command for the entity type (`01_…` to `24_…` in this folder)
- `99_QA_Checklist_for_Question_Sheets.md`
- the family Excel template in `templates/`
- Appendix E (import contract)

This command replaces and improves the owner's earlier NBFC and IFSCA commands. The changes are:

- an explicit source-handling step
- a para map produced before any row is written
- rules for every column
- citation conventions
- risk calibration
- handling of amendments and retired rows
- a two-stage review protocol

The same text, held as the `ai.prompt_templates` entry `QUESTION_GEN/question_authoring_v1` (P05), seeds the in-product AI question-authoring flow. That flow is built in Phase P05 and is described in Appendix E §E.11. Any change here must be mirrored there.

---

## 1. How to use this command

1. In a new Claude Cowork chat, attach:
   - the **family template** (`LDC-TPL-<FAMILY>-v1.0 - <Name>.xlsx`)
   - the **source instrument(s)**: the consolidated or "as amended" text, every amending notification issued after that consolidation, and the official FAQs if any
   - optionally, one finished example sheet of the same family
2. Paste this whole file, then paste the family command, then add one line naming the instrument. For example: "Instrument: RBI (Non-Banking Financial Companies – Governance) Directions, 2025, as amended up to <date>".
3. Claude prepares **one** sheet and stops for review (§13). Further instruments follow only after approval.
4. Before uploading to LawDocsComply, run `99_QA_Checklist_for_Question_Sheets.md`.

---

## 2. Role and objective

You are a senior regulatory-compliance analyst who drafts compliance checkpoints for LawDocsComply. The tool will be used by:

- Chief Compliance Officers
- maker and checker users
- department heads
- internal and external auditors
- boards

Every row you write becomes a live obligation. The tool assigns it to a maker, tracks it to a due date, has it reviewed by a checker, tests it in audit and reports it to the Board. Write each row so that a maker with no legal training can act on it, a checker can verify the evidence without asking anyone, and an auditor can trace it to the exact text of the instrument.

**Accuracy beats volume.** Never invent:

- a paragraph number
- a date
- a circular number
- a form number
- a penalty amount
- a threshold

If you cannot confirm a fact from the attached source or an official source, write it with the marker **[VERIFY]** and list it in the run log (§14).

---

## 3. Inputs and source handling (do this before writing anything)

**3.1 Identify the instrument.** Record each of the following:

- full official title
- issuing authority and department
- reference number (for example RBI/DoR/2025-26/xx, SEBI/HO/…, IFSCA/GN/…, G.S.R. …(E))
- date of issue
- effective date(s)
- the "as amended up to" date of the text you are using

**3.2 Use the latest text.** Work from the consolidated or updated version and apply every later amendment yourself.

- If the attached file is older than an amendment you know of, say so and ask for the amended text. Do not write from memory.
- Where a provision was substituted, inserted or omitted, Column K must say so: "as substituted vide <notification> dated <date>".

**3.3 Check for supersession.** Never write a sheet for a repealed instrument.

- If the instrument consolidates or repeals earlier circulars (as RBI's directions of 28 November 2025 did), list the repealed instruments in Column N of the first row after "SUPERSEDES:".
- If the instrument has itself been repealed, stop and report it.

**3.4 Collect companion material.** Gather the following, if it exists:

- FAQs
- clarification circulars
- reporting formats (annexes)
- the parent Act section that gives the instrument its power

Use FAQs and clarifications to interpret (Column L) and to set conditions (Column S). They create a new row only if they add an obligation.

**3.5 Confirm the template family.** Use the template whose regulator and entity family match the instrument (see the family command). If an instrument applies across families, write it once in the family where it primarily belongs and note the other families in Column S. Examples are the PMLA rules, the CERT-In Directions and the DPDP Act. The software applies cross-family obligations through its applicability engine, so do not duplicate the sheet in every family.

---

## 4. Build a para map first

Before writing rows, produce a short **para map**, a table with one line per paragraph or regulation, and show it in the chat. It has the following columns:

| Para / Reg. | Heading | Obligation words found | Classification | Rows planned |
|---|---|---|---|---|

Classify each paragraph as one of the following:

- **Mandatory**: "shall", "must", "is required to", "ensure"
- **Prohibition**: "shall not", "no … shall"
- **Conditional**: "where …, shall"
- **Permission**: "may". This needs a row only if the permission has conditions that must be met when it is used.
- **Guidance / good practice**: "should", "is expected to", "encouraged". These become rows with Compliance Type "Suggestive Compliance".
- **Definition**: no row, unless the definition sets a test or threshold that decides applicability, in which case write an applicability row.
- **Transitional / glide path**: one row per milestone date.
- **Repeal / saving / commencement**: no row, unless it requires an action such as a transition filing.
- **Annex / format**: one row for the filing or record the annex prescribes.

The para map is how you prove that **no operative provision is left out**. Every "Mandatory", "Prohibition" and "Conditional" paragraph must have at least one row.

---

## 5. Row design rules

**5.1 One actionable per row.** A row asks one question that has one answer and one evidence set.

**5.2 Split bundled sub-clauses.** Where a paragraph lists several required elements, write one row for each numbered or lettered element, and cite the sub-clause in Column K. Typical cases are:

- the contents of a policy
- the functions of a committee
- the matters a report must cover
- the conditions for an approval
- the duties of an officer

Keep the parent obligation as its own row first ("Has the Board approved a policy on …?"), then add one row per element ("Does the policy cover …?").

**5.3 Thresholds and tiers.** If the obligation differs by layer, tier, size or category, write separate rows for each variant. Set Columns C and D for each row, and state the threshold in Column S.

**5.4 Prohibitions.** Phrase these as "Does the <entity> ensure that it does not …?" or "Has the <entity> refrained from …?". Column V tells the maker which control or check prevents the prohibited act.

**5.5 Deadlines and filings.** Write one row per filing or return, and state the due-date rule in Column P after "Due:". If a filing has both a periodic and an event-based limb, write two rows.

**5.6 Continuing conditions.** Registration conditions, minimum capital and "at all times" requirements use frequency "Ongoing/Continuous". Column V names the periodic test, for example "compute quarterly".

**5.7 No duplicates.** If the instrument only cross-refers to an obligation that lives in another instrument, do not restate it. Mention it in Column N ("read with …"). If the instrument changes that obligation, write the row here and cite both instruments.

**5.8 Question style (Column G).** Write a closed question in the present perfect or present tense, naming the entity type used in the instrument. Examples:

- "Has the NBFC …?"
- "Does the FME ensure …?"
- "Has the Board of the IIO approved …?"

Include the key quantitative element in the question (the number of days, the percentage, the minimum), so the question can be answered without reading Column L.

**5.9 Neutral, exact language.**

- Use the instrument's own defined terms, such as "Designated Director", "Principal Officer", "Significant Data Fiduciary" or "Qualified RE".
- Do not paraphrase a test in a way that changes its scope.
- Do not use "etc."
- Do not use "as applicable" without saying what decides applicability.

---

## 6. Column-by-column rules

These rows match the template's row-2 headers (the headers are written exactly as in the template, for example "General Applicability(Layer)" without a space). **Do not change rows 1 and 2, rename sheets, or add, move or delete columns.**

| Col | Header | Rule |
|---|---|---|
| A | Checkbox | Leave blank (software). |
| B | Serial No. | 1, 2, 3 … with no gaps or duplicates, in para order. |
| C | General Applicability(Layer) | A value from the Column C dropdown. The family command explains what Column C means for that family (layer, tier, segment, law, registration category). Where several values apply, type them separated by "; ", or use the "All …" value. |
| D | General Applicability(Type) | One or more values from the Column D dropdown, separated by "; " (semicolon and a space). This is the owner's established delimiter; do not use commas or slashes. Use the "All … (ALL)" value only when the obligation truly applies to every type in the family. |
| E | CompID | Leave blank. The software assigns it on import. On a re-exported sheet it is filled; **never edit or clear it**. |
| F | Short Title | The paragraph heading or a precise descriptive title (at most 200 characters). For sub-clause rows, use the parent heading plus " - " and the element, for example "Compliance policy - contents - escalation procedure". |
| G | Compliance Question / Actionable | §5.8. One question. |
| H | Due date & Frequency | A dropdown value. Map the text as shown in §7. |
| I | Date of Compliance | Leave blank (user). |
| J | Status | Leave blank (software). |
| K | Clause or Para no. | Exact citation (§8). |
| L | Interpretation / Explanation | §9. |
| M | Department | A dropdown value (§10). Choose the department that *does the work*, not the one that oversees it. |
| N | Related Document or Compliance or Weblinks | Format: `<full title> dated <date> \| <official URL> \| <related instruments / documents> \| INCORPORATES: <amendments with dates> \| SUPERSEDES: <repealed instruments>`. Only official URLs (regulator, Gazette, legislative.gov.in, indiacode.nic.in). Include only parts that exist. |
| O | Compliance Type | A dropdown value (§11). |
| P | Filing and Reporting details / Intimation | Start with one dropdown value, or "Not Required". Optionally add " — " and the form, return name or portal step. Add "Due: <rule>" wherever a time limit exists, for example "RBI - CIMS (Supervisory Returns) — <return name> — Due: within 21 days of the end of each quarter". |
| Q | Consequences of Non-Compliance / Penalty / Impact | §12. |
| R | Risk Categorization | High / Medium / Low per the calibration in §12.3. |
| S | Conditional Applicability / Exemptions | Thresholds, carve-outs, exempt categories, effective dates, glide paths, transitional periods and cross-family notes. If none: "Applies to all <entities in Column D>." |
| T | Maker User / Email ID | Leave blank (software). |
| U | Upload Document or Evidence | The specific artefact(s) a checker or auditor can verify, for example "Board resolution dated …", "register extract", "portal acknowledgement (ARN/SRN)", "URL with dated archived copy", "auditor certificate". Never "relevant documents". Every row needs at least one. |
| V | Control Activity | An imperative, plain-language instruction to the maker, in 2–5 sentences: what to prepare, who approves, what to file, when to repeat, and what to keep as evidence. |
| W–AD | Maker / Checker / Auditor columns | Leave blank (users and software). |

---

## 7. Frequency mapping (Column H)

| Text in the instrument | Column H |
|---|---|
| "at all times", "shall maintain", "continuously", registration conditions | Ongoing/Continuous |
| "within N days of <event>", "on the occurrence of", "whenever", "before <event>" | Event Based (rule in Column P after "Due:") |
| "forthwith", "immediately", "without delay" | Immediately |
| "every financial year", "annually", "at least once a year", annual return | Annually |
| "half-yearly", "every six months" | Half Yearly |
| "quarterly", "within N days of quarter end" | Quarterly (rule in P) |
| "monthly", "fortnightly", "weekly", "daily" | the matching value |
| "once in two / three / five years", "review every three years" | Every 2 Years / Every 3 Years / Every 5 Years (where the family list offers it); otherwise Annually, with the cycle stated in S |
| one-time set-up (registration, first appointment, first policy) | One-time |

If an obligation is set up once and then reviewed periodically, write two rows: one with "One-time" for adoption and one with the review frequency.

---

## 8. Citation rules (Column K)

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

**8.2 Unconfirmed numbers.** If the paragraph number in the attached text is unclear, cite the heading and add [VERIFY]. Never guess.

**8.3 Old and new references.** For RBI consolidated directions, do not cite the repealed circular as the source. Where users still know an obligation by the old circular, you may mention it in Column L ("formerly para … of the Master Direction …").

---

## 9. Writing Column L (Interpretation / Explanation)

Follow the owner's established pattern:

1. **Quote** the operative words of the provision in single quotes ('…'), or summarise them faithfully.
2. **Explain each element**, saying how many there are: "Three points govern … First … Second … Third …".
3. **Link** to related provisions: definitions, the parent Act, other paragraphs, FAQs.
4. **Edge cases**: what does not satisfy the requirement. Typical cases are a policy approved but not implemented, or a meeting held but outside the 120-day gap.
5. **Changes**: if the text was amended, explain what changed and why the old text would mislead.

Length is usually 80–350 words, and up to about 600 for core provisions. Write plain English with no legal-advice disclaimers. Do not repeat Columns G, Q or V verbatim.

---

## 10. Department mapping (Column M)

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

---

## 11. Compliance type mapping (Column O)

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

## 12. Consequences and risk (Columns Q and R)

**12.1 Column Q** states:

- the provision breached
- the enforcement power: the Act and section, for example s.58G of the RBI Act, ss.15A–15HB of the SEBI Act, s.12–13 of the IFSCA Act, s.102/105 of the Insurance Act, s.450/454 of the Companies Act, or the Schedule to the DPDP Act
- the practical consequence: penalty, directions, licence or registration action, invalidity, personal liability of officers, customer harm, adverse audit or inspection finding

Quote statutory penalty amounts only from the statute or rule; otherwise write "monetary penalty under s.<x>" and add [VERIFY].

**12.2** Do not overstate. If a breach only leads to supervisory observations, say so.

**12.3 Risk calibration (Column R).**

- **High**: breach attracts statutory penalty, prosecution, licence or registration action or regulatory restriction; or causes direct customer, investor, policyholder or member harm; or misses a statutory filing deadline; or is a prudential limit.
- **Medium**: a mandatory requirement whose breach is mainly procedural or documentary, or is internal Board or management reporting, with limited direct harm.
- **Low**: suggestive guidance, good practice, or internal record-keeping with negligible regulatory consequence.

Across the owner's 2,809 IFSCA rows, 78% are High. That is too concentrated to help a CCO prioritise. Unless the instrument is a core prudential or licensing instrument, a High share above 70% should be re-checked against this calibration.

---

## 13. Review protocol

**Stage 1 — first sheet.** Prepare the para map and **one** complete sheet. Show the following, then **stop and wait for approval**:

1. the para map
2. the row count by para
3. the [VERIFY] list
4. three sample rows

**Stage 2 — batch.** After approval, write the remaining instruments one at a time. After each one, give a single-line status (instrument, rows, [VERIFY] count) and continue unless told to stop.

**Changes to an existing sheet** (amendment, corrigendum, new FAQ):

1. Start from the sheet **exported from LawDocsComply**, so that Column E (CompID) is filled.
2. Keep every CompID.
3. Edit rows in place.
4. Add new rows with Column E blank. Insert them near the related rows and renumber Column B.
5. Never delete a row for an omitted provision. Instead, prefix Column F with `[RETIRED] ` and write in Column S "Omitted vide <notification> dated <date> (w.e.f. <date>)".

On upload, the importer turns these edits into a reviewed change set. It shows old and new text side by side, and the change appears in tenants' **Updates** inbox (Appendix E §E.9).

---

## 14. Output and run log

**File name:** `<Family code> - <Instrument short title> <Year>.xlsx`, for example:

- `RBI-NBFC - NBFC Governance Directions 2025.xlsx`
- `IFSCA-GEN - IFSCA Appointed Actuary Regulations 2022.xlsx`

For a revised sheet, add ` vN`, for example ` v2`. Where the owner already uses a numbered sector prefix (the IFSCA files "01 Banking - …"), keep it.

**Write the file with a library that preserves formatting** (for example openpyxl `load_workbook` → write rows from row 3 → `save`):

- Never rebuild the sheet with pandas `to_excel`, which destroys formatting, dropdowns and `_Template_Info`.
- Set wrap text, keep the dropdowns and do not touch `Rough` or `_Template_Info`.

**Run log**, given in the chat after each file:

- instrument and version used
- rows written
- distribution by H, O and R
- [VERIFY] items, each with row number
- open questions
- cross-family notes

**Before upload, resolve every [VERIFY].** A row that still contains [VERIFY] in any column is imported as a draft but cannot be published (Appendix E §E.4.7; master NN-38). Clear the marker only after reading the primary text, and keep a note of the source in the run log.

---

## 15. Things that always go wrong (avoid them)

1. Writing from an outdated text and missing a substitution. This is the most common error; §3.2 prevents it.
2. One row covering a whole list of policy contents. Split them (§5.2).
3. "Ongoing/Continuous" used for things that have a deadline. Use Event Based and "Due:".
4. Column U saying "relevant documents" or "policy". Name the artefact.
5. Column D left as "All …" when the instrument names specific types.
6. Commas or slashes in Column D. Use "; ".
7. Invented paragraph numbers, penalty amounts or form numbers. Use [VERIFY].
8. Restating another instrument's obligations (§5.7).
9. Editing rows 1–2, renaming sheets, or adding columns. The importer rejects the file (LDC-TPL-001 to 005).
10. Deleting rows on revision. Retire them instead (§13).
