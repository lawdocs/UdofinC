# 29 — GOV-LIB Command: Platform Governance Library (GovIDs) *(v1.2 — new)*

**Template:** `templates/LDC-TPL-GOV-v2.0 - Governance Register.xlsx` · **Template code:** `LDC-TPL-GOV-v2.0` · **Owner:** LawDocsComply content team (platform library) · **Use with:** `00_Part2_Master_Command.md` (paste first; §3–§9 and §13–§15 apply), then this file, then the instrument line. As of 25 October 2026.

**v1.2 changes** *(v1.2)* — New command (decision D-57). It writes the **platform governance library**: board, committee, general-meeting, officer and secretarial requirements, each with a library GovID assigned by the system (`GOVL-<AUTH>-<NNNN>`), so that the governance module (P06) can schedule meetings, build agendas, track minutes, resolutions, registers and filings, and link them to compliance questions (CompIDs) and risks (RiskIDs). Tenant governance events get tenant GovIDs (`GOV-<TENANT4>-<TYPE>-<NNNNN>`).

---

## 1. What a governance library row is

One row = **one governance requirement or action** a governing body or officer must perform: hold a meeting, give notice, meet a quorum, approve an item, record minutes, pass a resolution, maintain a register entry, file a form, constitute a committee, or make a declaration. Write it as an action: "Hold at least four Board meetings each year with a gap of not more than 120 days between two meetings."

Where the same requirement is also tracked as a compliance question (for example a filing), write the GovID row for the governance workflow and link it to the CompID (Linked CompIDs); do not duplicate the compliance question.

## 2. Instruments in scope

| Authority (AUTH in GovID) | Instruments |
|---|---|
| MCA | Companies Act, 2013 (Chapters VII, XI, XII, XIII) and the Companies (Meetings of Board and its Powers), (Management and Administration), (Appointment and Qualification of Directors) Rules, 2014 |
| ICSI (AUTH = MCA unless the registry assigns ICSI) | Secretarial Standard on Meetings of the Board of Directors (SS-1) and on General Meetings (SS-2) as revised [VERIFY latest revision date] |
| SEBI | SEBI (LODR) Regulations, 2015 — Chapter IV governance (Regs. 17–27), Board and committee composition and meetings, general-meeting disclosures |
| RBI | Governance chapters of the RBI consolidated directions of 28 November 2025 (e.g. NBFC, Commercial Bank, UCB, RCB, ARC Governance Directions — Board composition, committees, fit and proper, CCO / CRO, rotation of statutory auditors), as updated |
| COOP | MSCS Act, 2002 and MSCS Rules, 2023; State Co-operative Societies Acts — general body, board, elections, office bearers, audit adoption |
| Others | LLP Act (designated partners' meetings where the agreement requires), IRDAI and IFSCA corporate-governance guidelines, where the family needs them |

## 3. Template and groups

The `Governance Register` sheet follows the v2.0 design (row 1 group bands, row 2 headers, data from row 3, `Lists`, `_Template_Info`, `Read Me`). Use the exact headers in T1's template; the groups are:

| Group | Columns (summary) | Who fills in the library |
|---|---|---|
| LIST VIEW | S. No. · GovID · Governance Requirement / Action · Section / Clause / Standard · Governing Body · Timing & Frequency · Date of Completion · Status · Risk Category | Author all except **GovID (blank — system)**, Date of Completion and Status (tenant) |
| SOURCE | Statute / standard / regulator, instrument name, reference, issue date, last amended, actionable last updated, change status, source link | Author (same rules as master §6A) |
| REQUIREMENT DETAIL | Meeting type, notice period, quorum, documents (notice, agenda, papers, minutes, resolution, register, form), filing and due rule, responsible role, evidence, linked CompIDs, linked RiskIDs | Author |
| WORKFLOW | Preparer, reviewer, approver, comments | Blank (tenant) |
| SYSTEM | Version, RAG, etc. | Blank (system) |

## 4. Column rules

| Field | Rule |
|---|---|
| GovID | **Leave blank.** The system assigns `GOVL-<AUTH>-<NNNN>` (e.g. `GOVL-MCA-0211`); never type or reuse one (NN-56). |
| Governance Requirement / Action | One action per row, in the imperative, with the number in it ("Give at least seven days' written notice of a Board meeting to every director"). Split notice, quorum, agenda, minutes and filing into separate rows (one row per para or sub-clause, as in master §5.2). |
| Section / Clause / Standard | Exact citation, master §8 format (e.g. "Section 173(1), Companies Act, 2013"; "SS-1, para 3.1"; "Regulation 17(2), SEBI (LODR) Regulations, 2015"). |
| Governing Body | Board / Committee (name it: Audit Committee, NRC, Risk Management Committee, CSR Committee, Stakeholders' Relationship Committee, IT Strategy Committee, Board of Management) / General Meeting / KMP / Office Bearers. |
| Timing & Frequency | Frequency list value plus the timing rule in the master §7A grammar ("At least four times a year; gap ≤ 120 days"; "Within six months of the close of the financial year"). |
| Meeting type, notice period, quorum | Fill for meeting rows; quorum as stated in the instrument (e.g. "One-third of total strength or two directors, whichever is higher"). |
| Documents | The governance artefacts produced: notice, agenda, notes, minutes, resolution, register entry, form — these drive P06 document templates. |
| Filing and due rule | Form and due rule where the action ends in a filing (e.g. "MGT-14 within 30 days of the resolution"). |
| Responsible role | Company Secretary, Chairperson, CFO, CCO, Secretary of the society, etc. |
| Evidence | Checkable artefacts (signed minutes, attendance register, notice dispatch proof, SRN). |
| Linked CompIDs / RiskIDs | Only IDs that exist in the published libraries (`RSKL-…` for risks); otherwise blank, with intended links listed in the run log. Governance-failure risks usually map to taxonomy `GOV.*`. |
| Risk Category | High / Medium / Low per master §12.3. |

## 5. Example rows (illustrative)

| Field | Row 1 | Row 2 |
|---|---|---|
| GovID | (blank — system) | (blank — system) |
| Governance Requirement / Action | Hold a minimum of four Board meetings every year, with not more than 120 days between two consecutive meetings | Ensure the quorum for a Board meeting is one-third of total strength or two directors, whichever is higher |
| Section / Clause / Standard | Section 173(1), Companies Act, 2013; SS-1 para 2.1 [VERIFY para] | Section 174(1), Companies Act, 2013; SS-1 para 3 [VERIFY para] |
| Governing Body | Board | Board |
| Timing & Frequency | Quarterly — at least four a year; gap ≤ 120 days | Each meeting |
| Meeting type / notice / quorum | Board meeting / at least 7 days' written notice (s.173(3)) / as per s.174 | Board meeting / — / one-third or two, whichever is higher |
| Documents | Notice; agenda; notes; attendance register; minutes | Attendance register; minutes recording quorum |
| Filing and due rule | Not required | Not required |
| Responsible role | Company Secretary | Company Secretary / Chairperson |
| Evidence | Board calendar; signed minutes with dates | Signed attendance register; minutes |
| Conditions | OPC, small company, dormant company and Section 8 company relaxations under s.173(5) and exemption notifications [VERIFY] | Interested directors are not counted for quorum on the interested item (s.184) [VERIFY wording] |
| Linked CompIDs / RiskIDs | (blank — link to the MCA-CO board-meeting CompID once published) | (blank) |
| Risk Category | High | High |
| Instrument / dates / change status | Companies Act, 2013 · Act No. 18 of 2013 · 29-Aug-2013 · last amended [VERIFY] · Unchanged | Same |

## 6. Quality bar

- Every operative governance provision of the instrument (meeting frequency, notice, quorum, agenda / papers, minutes, resolutions, registers, filings, committee constitution and composition, office-bearer / KMP events, declarations) has at least one row.
- One action per row; the action names the governing body and the number.
- No GovID typed; no tenant data; [VERIFY] resolved before publication.
- Run the relevant parts of `99_QA_Checklist_for_Question_Sheets.md` (A, B, D, E, F) with "governance row" in place of "compliance question".

## 7. File naming

`GOV-LIB - <AUTH> - <Instrument short title> - Governance Library v2.xlsx` (e.g. `GOV-LIB - MCA - Companies Act 2013 Board Meetings - Governance Library v2.xlsx`); revisions add ` (rev N)`. Keep `_Template_Info`, `Lists` and `Read Me`.
