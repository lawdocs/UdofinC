# 14 — SEBI-LISTED Family Command: Listed Entities (equity, SME, debt, HVDLE)

**Template:** `templates/LDC-TPL-SEBI-LISTED-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-SEBI-LISTED-v2.0` · **Regulator / authority:** Securities and Exchange Board of India; Stock Exchanges · **Named-range prefix:** `SEBI_LST_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-SEBI-LISTED-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Listing Segment.** General Applicability (Layer) holds the listing segment: main board specified securities, SME platform, non-convertible securities (debt-listed), HVDLE, both equity and debt, Social Stock Exchange, listed CP.

**General Applicability (Type) — Entity Overlay.** General Applicability (Type) holds overlays that change applicability: top 100/500/1000/2000 by market capitalisation, material subsidiary, SR equity, PSU, sectoral regulated entity, newly listed, entity under CIRP. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (SEBI_LST_Sector):**
- Main Board - Specified Securities
- SME Exchange / SME Platform
- Non-Convertible Securities (Debt-listed)
- High Value Debt Listed Entity (HVDLE)
- Specified Securities and Non-Convertible Securities
- Social Stock Exchange
- Commercial Paper (listed)
- All Listed Entities

**General Applicability (Type) (SEBI_LST_Entity):**
- Top 100 listed entities (by market capitalisation)
- Top 500 listed entities
- Top 1000 listed entities
- Top 2000 listed entities
- Listed entity with material subsidiary
- Listed entity with SR equity shares
- Public Sector Undertaking (listed)
- Listed Bank / NBFC / Insurer (sectoral overlay)
- Newly listed entity (IPO year)
- Entity under CIRP (IBC)
- All Listed Entities (ALL)

**Due Date & Frequency (SEBI_LST_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (SEBI_LST_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Secretarial, Investor Relations, Internal Audit. Family additions: Secretarial, Investor Relations, Internal Audit.

**Compliance Type (SEBI_LST_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Disclosures. Family additions: Disclosures.

**Risk Category (SEBI_LST_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (SEBI_LST_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- Stock Exchanges (NSE NEAPS / BSE Listing Centre)
- Stock Exchanges (prior approval / in-principle)
- SEBI (filing)
- SEBI SCORES / SMART ODR
- Depositories (NSDL / CDSL)
- RTA
- MCA (ROC)
- Debenture Trustee
- Credit Rating Agency
- Shareholders (website / newspaper)
- IEPF Authority
- Board / Audit Committee
- Secretarial Auditor
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- LODR Chapter IV (specified securities) and Chapter V (non-convertible securities) differ. Write separate rows with the correct C.
- Reg. 15(2) exempts SME-listed and small entities from regs. 17–27 and other provisions. Record this in Conditional Applicability / Exemptions / Thresholds [VERIFY current thresholds].
- Market-cap rankings are taken as on 31 December (or the date SEBI specifies) [VERIFY]. Write the ranking test in Conditional Applicability / Exemptions / Thresholds.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015 (as amended, incl. Fifth Amendment 2025)
- SEBI Master Circulars on compliance with LODR (specified securities; non-convertible securities) [VERIFY dates]
- SEBI (Prohibition of Insider Trading) Regulations, 2015
- SEBI (Substantial Acquisition of Shares and Takeovers) Regulations, 2011
- SEBI (ICDR) Regulations, 2018 (continuing obligations); SEBI (Buy-back) Regulations, 2018; SEBI (SBEB & SE) Regulations, 2021
- BRSR / BRSR Core framework
- Companies Act, 2013 provisions applicable to listed companies (ss. 149(4), 177, 178, 204)

## 5. Family-specific pitfalls

- Ignoring the SOP fine schedule for each regulation in Consequences of Non-Compliance / Penalty.
- Writing equity-only rows for debt-listed entities.

## 6. File naming

`SEBI-LISTED - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Listing Segment | Main Board · SME Platform · Non-convertible securities · Commercial paper · Social Stock Exchange | Use with General Applicability (Layer) where the row needs the segment separately from the layer. |
| Market-cap Band | Top 100 · Top 250 · Top 500 · Top 1000 · Top 2000 · Other | Use where a market-cap ranking decides applicability; name the reference date in Conditional Applicability. |
| HVDLE | HVDLE · Not HVDLE | Use for debt-listed entities where HVDLE status changes applicability. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-SEBI-LISTED-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Secretarial → Board meetings / Disclosures to exchanges / Shareholder meetings; Finance, Treasury and Accounts → Financial results; Investor Relations → Investor grievances; Internal Audit → Audit Committee support. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Disclosure rows → Regulatory; Conduct & Consumer; governance → Governance; related-party → Governance; Legal. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the listed entity submitted its quarterly financial results to the stock exchange within 45 days of the end of the quarter (60 days for the last quarter with the annual audited results)? |
| 4 | Clause / Para No. (`clause_ref`) | Regulation 33(3)(a) and (d), SEBI (LODR) Regulations, 2015 |
| 5 | Department (`department`) | Finance, Treasury and Accounts |
| 6 | Due Date & Frequency (`frequency`) | Quarterly |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | SEBI |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015 |
| 12 | Instrument Reference No. (`instrument_ref`) | No. SEBI/LAD-NRO/GN/2015-16/013 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 02-Sep-2015 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY latest amendment] |
| 15 | Actionable Last Updated On (`question_updated_date`) | 02-Sep-2015 |
| 16 | Change Status (`change_status`) | Unchanged |
| 17 | Change Note / Previous Actionable (`change_note`) | (blank) |
| 18 | Source Link (`source_url`) | https://www.sebi.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | Main Board - Specified Securities |
| 20 | General Applicability (Type) (`applic_type`) | All Listed Entities (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Debt-listed entities follow Reg. 52 (write separately). |
| 22 | Applicable From (`applic_from`) | 01-Dec-2015 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Listing Segment (`ext_*`) | Main Board |
| E2 | Market-cap Band (`ext_*`) | (blank — not a deciding factor here) |
| E3 | HVDLE (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | Financial results - quarterly submission |
| 25 | Interpretation / Explanation (`explanation`) | Results are approved by the Board after Audit Committee review, with the limited review or audit report, and submitted within 30 minutes of the Board meeting's close [Reg. 30]. The 45/60-day limit is a deadline, not a target. (Abridged.) |
| 26 | Department Function (`dept_function`) | Financial Reporting |
| 27 | Department Sub-function (`dept_subfunction`) | Quarterly results |
| 28 | Compliance Type (`compliance_type`) | Returns & Reporting |
| 29 | Due Date Rule (`due_rule`) | Within 45 days from the end of each quarter (60 days for the last quarter) |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | Stock Exchanges (NSE NEAPS / BSE Listing Centre) — results with the limited review / audit report |
| 32 | Portal / Form / Return Code (`filing_form`) | XBRL financial results |
| 33 | Related Document / Policy / Committee (`related_docs`) | Audit Committee; Board; Statutory Auditor |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Exchange fine under the SEBI SOP circular for each day of delay; possible suspension of trading; SEBI penalty under s.15A(b), SEBI Act. |
| 36 | Penalty Provision (`penalty_ref`) | Section 15A(b), SEBI Act, 1992; SEBI SOP circular on fines [VERIFY date] |
| 37 | Risk Type (`risk_type`) | Regulatory; Reputational |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Board minutes approving results; exchange submission acknowledgements (PDF and XBRL); limited review / audit report |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Fix the Board date within 45 days of quarter end. Get the limited review report and Audit Committee review before the Board. File results and XBRL on both exchanges within 30 minutes of the meeting's close. |
| 42 | Checker Review Points (`checker_points`) | 1. Board met within 45 / 60 days. 2. Submission time within 30 minutes of meeting close. 3. Limited review / audit report attached. 4. XBRL filed. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain the four submissions for the year. 2. Compare Board date and submission timestamp to the deadlines. Exception: any delay or exchange fine. |
| 44 | Tags / Keywords (`tags`) | regulation 33; quarterly results; lodr; financial results; xbrl |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

