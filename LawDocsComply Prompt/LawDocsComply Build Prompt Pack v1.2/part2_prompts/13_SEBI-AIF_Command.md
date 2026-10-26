# 13 — SEBI-AIF Family Command: Alternative Investment Funds

**Template:** `templates/LDC-TPL-SEBI-AIF-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-SEBI-AIF-v2.0` · **Regulator / authority:** Securities and Exchange Board of India · **Named-range prefix:** `SEBI_AIF_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-SEBI-AIF-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Entity Role.** General Applicability (Layer) holds the role: the AIF or scheme, the manager, the sponsor or the trustee.

**General Applicability (Type) — AIF Category.** General Applicability (Type) holds the AIF category and sub-category: Category I (VCF, angel, SME, social impact, infrastructure, special situation), Category II, Category III, LVF for accredited investors, accredited-investor-only schemes, co-investment schemes [VERIFY]. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (SEBI_AIF_Sector):**
- AIF / Scheme
- Manager
- Sponsor
- Trustee
- All AIF Entities

**General Applicability (Type) (SEBI_AIF_Entity):**
- Category I - Venture Capital Fund
- Category I - Angel Fund
- Category I - SME Fund
- Category I - Social Impact Fund
- Category I - Infrastructure Fund
- Category I - Special Situation Fund
- Category II AIF
- Category III AIF
- Large Value Fund for Accredited Investors (LVF)
- Scheme for Accredited Investors only
- Co-investment Scheme (CIV)
- All AIFs (ALL)

**Due Date & Frequency (SEBI_AIF_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (SEBI_AIF_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Investment Team, Valuation, Investor Relations, Internal Audit. Family additions: Investment Team, Valuation, Investor Relations, Internal Audit.

**Compliance Type (SEBI_AIF_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Disclosures. Family additions: Disclosures.

**Risk Category (SEBI_AIF_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (SEBI_AIF_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- SEBI (filing)
- SEBI (prior approval)
- SEBI (intimation)
- SEBI Intermediary Portal (SI Portal)
- SEBI SCORES / SMART ODR
- Custodian
- Depositories (demat of units)
- Investors (disclosure / PPM)
- Performance Benchmarking Agency
- FIU-IND (FINnet 2.0)
- CERT-In
- Board / Investment Committee
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- Many conditions differ by category (leverage, concentration, tenure, continuing interest of the sponsor/manager). Write separate rows per category.
- PPM audit, valuation, performance benchmarking and dematerialisation of units are master-circular obligations. Cite the master circular paragraph.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SEBI (Alternative Investment Funds) Regulations, 2012 (as amended)
- SEBI Master Circular for AIFs [VERIFY latest date]
- SEBI CSCRF as applicable to AIF managers

## 5. Family-specific pitfalls

- Writing Category III leverage rules for Category I/II.
- Missing accredited-investor and LVF relaxations.

## 6. File naming

`SEBI-AIF - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| AIF Category | Category I · Category II · Category III | Use where the category decides applicability and General Applicability (Type) names a sub-category. |
| LVF / Accredited | Large Value Fund for Accredited Investors · Scheme for accredited investors only · Neither | Use where LVF or accredited-investor relaxations apply. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-SEBI-AIF-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Investment Team → Investment conditions; Valuation → Valuation / NAV; Investor Relations → PPM / Investor reporting; Returns & Reporting → SEBI reports; Internal Audit → PPM audit. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Investor-facing → Conduct & Consumer; valuation → Market; leverage (Cat III) → Market / Liquidity. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the manager obtained the annual audit of compliance with the terms of the Private Placement Memorandum (PPM) and placed its findings before the trustee and the sponsor within the prescribed time? |
| 4 | Clause / Para No. (`clause_ref`) | Regulation 20(16), SEBI (Alternative Investment Funds) Regulations, 2012 [VERIFY], read with Para [VERIFY], SEBI Master Circular for AIFs |
| 5 | Department (`department`) | Internal Audit |
| 6 | Due Date & Frequency (`frequency`) | Annually |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | Medium |
| 10 | Regulator / Authority (`authority`) | SEBI |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Securities and Exchange Board of India (Alternative Investment Funds) Regulations, 2012 |
| 12 | Instrument Reference No. (`instrument_ref`) | No. LAD-NRO/GN/2012-13/04/1474 [VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 21-May-2012 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY latest amendment] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | Unchanged |
| 17 | Change Note / Previous Actionable (`change_note`) | (blank) |
| 18 | Source Link (`source_url`) | https://www.sebi.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | Manager |
| 20 | General Applicability (Type) (`applic_type`) | All AIFs (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Exemptions for angel funds or LVFs [VERIFY]. |
| 22 | Applicable From (`applic_from`) | [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | AIF Category (`ext_*`) | (blank — not a deciding factor here) |
| E2 | LVF / Accredited (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | PPM audit - annual audit of terms of PPM |
| 25 | Interpretation / Explanation (`explanation`) | The audit checks that the fund was run in line with the PPM; findings and corrective actions go to the trustee, sponsor and SEBI [VERIFY recipients]. (Abridged.) |
| 26 | Department Function (`dept_function`) | PPM Audit |
| 27 | Department Sub-function (`dept_subfunction`) | Annual PPM audit |
| 28 | Compliance Type (`compliance_type`) | Internal Compliance |
| 29 | Due Date Rule (`due_rule`) | Within six months of the close of the financial year [VERIFY] |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | SEBI (filing) — PPM audit findings [VERIFY] |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | PPM; Trustee; Investment Committee |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the AIF Regulations; SEBI may impose a penalty under s.15HB, SEBI Act. |
| 36 | Penalty Provision (`penalty_ref`) | Section 15HB, SEBI Act, 1992 |
| 37 | Risk Type (`risk_type`) | Conduct & Consumer; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | PPM audit report; trustee and sponsor acknowledgement; SEBI submission acknowledgement |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Appoint the PPM auditor before year end. Provide all records. Place the report before the trustee and sponsor and file as required. Track remediation of findings. |
| 42 | Checker Review Points (`checker_points`) | 1. Report covers every PPM term. 2. Report placed with trustee and sponsor in time. 3. Findings have owners and dates. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Inspect the report and acknowledgements. 2. Follow up two findings to closure. Exception: late audit or open high findings. |
| 44 | Tags / Keywords (`tags`) | ppm audit; aif; private placement memorandum; manager |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

