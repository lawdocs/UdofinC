# 12 — SEBI-MF Family Command: Mutual Funds (AMCs, Trustees, Schemes)

**Template:** `templates/LDC-TPL-SEBI-MF-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-SEBI-MF-v2.0` · **Regulator / authority:** Securities and Exchange Board of India · **Named-range prefix:** `SEBI_MF_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-SEBI-MF-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Entity Role.** General Applicability (Layer) holds the role that bears the obligation: AMC, trustees, sponsor, the scheme, or all MF entities.

**General Applicability (Type) — Scheme / Framework.** General Applicability (Type) holds the scheme category per SEBI's categorisation (equity, debt, hybrid, solution-oriented, index/ETF, FoF, close-ended/interval), plus newer frameworks (Specialised Investment Funds, MF Lite) [VERIFY current status]. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (SEBI_MF_Sector):**
- Asset Management Company (AMC)
- Trustee Company / Board of Trustees
- Sponsor
- Mutual Fund Scheme
- All MF Entities

**General Applicability (Type) (SEBI_MF_Entity):**
- Equity Scheme
- Debt Scheme
- Hybrid Scheme
- Solution-oriented Scheme
- Index Fund / ETF
- Fund of Funds
- Close-ended / Interval Scheme
- Specialized Investment Fund (SIF)
- Mutual Fund Lite (MF Lite - passive)
- Overseas Investment Scheme
- All Schemes (ALL)

**Due Date & Frequency (SEBI_MF_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (SEBI_MF_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Fund Management & Investments, Investor Services, Internal Audit, Information Security. Family additions: Fund Management & Investments, Investor Services, Internal Audit, Information Security.

**Compliance Type (SEBI_MF_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Disclosures. Family additions: Disclosures.

**Risk Category (SEBI_MF_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (SEBI_MF_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- SEBI (filing)
- SEBI (prior approval)
- SEBI (intimation)
- SEBI Intermediary Portal (SI Portal)
- SEBI SCORES / SMART ODR
- AMFI
- Stock Exchanges
- Depositories / RTA
- Trustees
- Unitholders (website / disclosure)
- FIU-IND (FINnet 2.0)
- CERT-In
- KRA / CKYCR
- Board of AMC
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- Trustee obligations (reg. 18) and AMC obligations (reg. 25) are separate rows, even where they mirror each other.
- The SEBI Master Circular for Mutual Funds carries most operational requirements. Cite its paragraph numbers and date.
- CSCRF obligations for AMCs and RTAs belong in the CYBER family unless SEBI writes them into an MF circular.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SEBI (Mutual Funds) Regulations, 2026 (notified 14 Jan 2026; in force 1 Apr 2026; replaced the 1996 Regulations — cite 1996 numbers only for periods before 1 Apr 2026)
- SEBI Master Circular for Mutual Funds [VERIFY latest date and whether re-issued under the 2026 Regulations]
- SEBI (Prohibition of Insider Trading) Regulations, 2015 (as applicable to AMCs; code of conduct for AMC staff)
- SEBI CSCRF (20 Aug 2024, as clarified)
- AMFI code and best-practice guidelines (Suggestive Compliance)

## 5. Family-specific pitfalls

- Citing superseded individual circulars that are now part of the master circular.
- Treating AMFI guidelines as binding unless SEBI mandates them.

## 6. File naming

`SEBI-MF - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Applies To (AMC / Trustee / Scheme) | AMC · Trustee · Scheme | Who bears the obligation. Separate rows where AMC and trustee duties mirror each other. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-SEBI-MF-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Fund Management & Investments → Investment restrictions / Portfolio disclosure; Investor Services → Statements / Grievance; Returns & Reporting → SEBI reports / AMFI; Governance & Administration → Trustee oversight. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Disclosure and investor rows → Conduct & Consumer; investment limits → Market / Liquidity; valuation → Market. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the AMC disclosed the portfolio of each scheme as on the last day of the month on its website and the AMFI website within ten days of the end of the month? |
| 4 | Clause / Para No. (`clause_ref`) | Regulation 59A, SEBI (Mutual Funds) Regulations, 1996, read with Para [VERIFY], SEBI Master Circular for Mutual Funds dated [VERIFY] |
| 5 | Department (`department`) | Fund Management & Investments |
| 6 | Due Date & Frequency (`frequency`) | Monthly |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | SEBI |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Securities and Exchange Board of India (Mutual Funds) Regulations, 1996 |
| 12 | Instrument Reference No. (`instrument_ref`) | No. SEBI/LE/96 [VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 09-Dec-1996 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY latest amendment] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY date of the amendment that set the current frequency] |
| 16 | Change Status (`change_status`) | Amended |
| 17 | Change Note / Previous Actionable (`change_note`) | Monthly / fortnightly portfolio disclosure frequency revised by amendment [VERIFY notification and date]; previous actionable: 'Has the AMC disclosed the half-yearly portfolio …?' |
| 18 | Source Link (`source_url`) | https://www.sebi.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | Asset Management Company (AMC) |
| 20 | General Applicability (Type) (`applic_type`) | All Schemes (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Debt schemes also disclose fortnightly portfolios within five days [VERIFY]; write that as a separate row. |
| 22 | Applicable From (`applic_from`) | [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Applies To (AMC / Trustee / Scheme) (`ext_*`) | AMC |
| 24 | Short Title (`short_title`) | Disclosures - monthly portfolio |
| 25 | Interpretation / Explanation (`explanation`) | The disclosure is in the format prescribed by SEBI and must be on both the AMC's website and AMFI's. Missing one website is a breach. (Abridged.) |
| 26 | Department Function (`dept_function`) | Portfolio Disclosure |
| 27 | Department Sub-function (`dept_subfunction`) | Monthly portfolio |
| 28 | Compliance Type (`compliance_type`) | Disclosures |
| 29 | Due Date Rule (`due_rule`) | Within 10 days from the end of each month |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | Unitholders (website / disclosure) — AMC and AMFI websites |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | AMFI; Trustees |
| 34 | Reference Weblinks (`weblinks`) | https://www.amfiindia.com |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the MF Regulations; SEBI may impose a penalty under s.15A or s.15HB, SEBI Act, and issue directions. |
| 36 | Penalty Provision (`penalty_ref`) | Section 15HB, SEBI Act, 1992 |
| 37 | Risk Type (`risk_type`) | Conduct & Consumer; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Dated archive of the website page; AMFI upload confirmation; scheme-wise portfolio files |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Generate scheme-wise portfolios as at month end in the SEBI format. Have the Fund Accounting head review them. Upload to the AMC website and AMFI by day 10 and save dated screenshots. |
| 42 | Checker Review Points (`checker_points`) | 1. Every scheme's portfolio is uploaded. 2. Upload date ≤ day 10. 3. Format matches SEBI's. 4. Holdings tie to the fund accounting system. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Select two months at random. 2. Inspect archived pages and AMFI confirmations. 3. Agree five holdings to fund accounting. Exception: late or missing disclosure. |
| 44 | Tags / Keywords (`tags`) | portfolio disclosure; regulation 59a; amfi; monthly portfolio |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

