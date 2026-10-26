# 15 — SEBI-REIT-INVIT Family Command: REITs, SM REITs and InvITs

**Template:** `templates/LDC-TPL-SEBI-REIT-INVIT-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-SEBI-REIT-INVIT-v2.0` · **Regulator / authority:** Securities and Exchange Board of India · **Named-range prefix:** `SEBI_REIT_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-SEBI-REIT-INVIT-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Trust Type.** General Applicability (Layer) holds the trust type: REIT, SM REIT, public InvIT, private listed or unlisted InvIT.

**General Applicability (Type) — Role / Party.** General Applicability (Type) holds the party that bears the obligation: trust, manager/investment manager, trustee, sponsor, project manager, valuer, holdco/SPV. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (SEBI_REIT_Sector):**
- Real Estate Investment Trust (REIT)
- Small and Medium REIT (SM REIT)
- Infrastructure Investment Trust (InvIT) - Public
- InvIT - Private Listed
- InvIT - Private Unlisted
- All Investment Trusts

**General Applicability (Type) (SEBI_REIT_Entity):**
- Trust
- Manager / Investment Manager
- Trustee
- Sponsor / Sponsor Group
- Project Manager
- Valuer
- Holdco / SPV
- All Parties (ALL)

**Due Date & Frequency (SEBI_REIT_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (SEBI_REIT_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Secretarial, Investor Relations, Valuation, Asset Management. Family additions: Secretarial, Investor Relations, Valuation, Asset Management.

**Compliance Type (SEBI_REIT_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Disclosures. Family additions: Disclosures.

**Risk Category (SEBI_REIT_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (SEBI_REIT_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- SEBI (filing)
- SEBI (prior approval)
- Stock Exchanges
- Unitholders (disclosure)
- Trustee
- Valuer
- Credit Rating Agency
- Depositories
- MCA (ROC)
- Board of Manager
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- Governance obligations of the manager (board composition, committees, related-party transactions) mirror LODR. Cite the REIT/InvIT regulation, not LODR.
- Distribution and leverage limits are percentage tests. Put the number in the question.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SEBI (Real Estate Investment Trusts) Regulations, 2014 (incl. SM REIT chapter, 2024)
- SEBI (Infrastructure Investment Trusts) Regulations, 2014
- SEBI Master Circulars for REITs and InvITs [VERIFY dates]

## 5. Family-specific pitfalls

- Mixing REIT and InvIT leverage thresholds.

## 6. File naming

`SEBI-REIT-INVIT - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Vehicle Role | Trust · Manager / Investment Manager · Trustee · Sponsor · Project Manager · Valuer | Who bears the obligation inside the vehicle. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-SEBI-REIT-INVIT-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Asset Management → Distributions / Asset acquisitions; Valuation → Valuation reports / NAV; Investor Relations → Unitholder disclosures; Secretarial → Unitholder meetings. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Distribution and disclosure → Conduct & Consumer; leverage and valuation → Market / Liquidity; related-party → Governance. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the manager distributed at least 90% of net distributable cash flows to unitholders at least once every six months? |
| 4 | Clause / Para No. (`clause_ref`) | Regulation 18(16), SEBI (REIT) Regulations, 2014 [VERIFY] |
| 5 | Department (`department`) | Asset Management |
| 6 | Due Date & Frequency (`frequency`) | Half Yearly |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | SEBI |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Securities and Exchange Board of India (Real Estate Investment Trusts) Regulations, 2014 |
| 12 | Instrument Reference No. (`instrument_ref`) | No. LAD-NRO/GN/2014-15/11/1577 [VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 26-Sep-2014 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY latest amendment] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | Unchanged |
| 17 | Change Note / Previous Actionable (`change_note`) | (blank) |
| 18 | Source Link (`source_url`) | https://www.sebi.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | Real Estate Investment Trust (REIT) |
| 20 | General Applicability (Type) (`applic_type`) | Manager / Investment Manager |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Separate rows for SM REIT schemes [VERIFY]. |
| 22 | Applicable From (`applic_from`) | [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Vehicle Role (`ext_*`) | Manager / Investment Manager |
| 24 | Short Title (`short_title`) | Distributions - minimum distribution of NDCF |
| 25 | Interpretation / Explanation (`explanation`) | The test covers both the SPV-to-REIT and REIT-to-unitholder distributions [VERIFY]; the payment deadline after declaration is set by the regulation [VERIFY]. (Abridged.) |
| 26 | Department Function (`dept_function`) | Distributions |
| 27 | Department Sub-function (`dept_subfunction`) | Unitholder distributions |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | At least once every six months; pay within [VERIFY] days of declaration |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | Stock Exchanges — record date and distribution intimation |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | Distribution policy; Board of Manager; Trustee |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the REIT Regulations; SEBI penalty under s.15HB, SEBI Act; unitholder harm. |
| 36 | Penalty Provision (`penalty_ref`) | Section 15HB, SEBI Act, 1992 |
| 37 | Risk Type (`risk_type`) | Conduct & Consumer; Liquidity |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | NDCF computation; Board of Manager resolution declaring distribution; payment confirmation from the registrar |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Compute NDCF for the half year using the SEBI framework. Have the Board of Manager declare at least 90%. Intimate the exchanges and pay within the deadline. |
| 42 | Checker Review Points (`checker_points`) | 1. NDCF computed per framework. 2. Distribution ≥ 90%. 3. Payment within the deadline. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Re-perform the NDCF computation for one half year. 2. Trace payment to bank records. Exception: shortfall or late payment. |
| 44 | Tags / Keywords (`tags`) | ndcf; distribution; reit; unitholders |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

