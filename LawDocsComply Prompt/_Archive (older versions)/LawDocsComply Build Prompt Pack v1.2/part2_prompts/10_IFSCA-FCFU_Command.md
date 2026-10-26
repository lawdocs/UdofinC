# 10 — IFSCA-FCFU Family Command: IFSCA Finance Companies and Finance Units

**Template:** `templates/LDC-TPL-IFSCA-FCFU-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-IFSCA-FCFU-v2.0` · **Regulator / authority:** International Financial Services Centres Authority · **Named-range prefix:** `IFSCA_FC_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-IFSCA-FCFU-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Entity Form.** General Applicability (Layer) says whether the row applies to a Finance Company, a Finance Unit (branch/unit of a foreign or Indian entity), or both.

**General Applicability (Type) — Activity / Registration.** General Applicability (Type) holds the activity or registration: GRCTC; core activities under reg. 5(1)(ii) (lending/credit enhancement/securitisation/financial lease; factoring and forfaiting; investments; derivatives); non-core activities under reg. 5(1)(iii) (merchant banking, advisory/PMS, distribution, trading/clearing membership, RTA/trusteeship); aircraft and ship lessors; ITFS operators. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (IFSCA_FC_Sector):**
- Finance Company (FC)
- Finance Unit (FU)
- Finance Company / Finance Unit (FCFU)

**General Applicability (Type) (IFSCA_FC_Entity):**
- Finance Company / Finance Unit (FCFU)
- Global/Regional Corporate Treasury Centre (GRCTC)
- Core - Lending, Commitments, Guarantees, Credit Enhancement, Securitisation, Financial Lease
- Core - Factoring and Forfaiting (Registered Factor)
- Core - Investments in Securities
- Core - Buy/Sell Derivatives
- Non-core - Merchant Banking / Investment Banking
- Non-core - Investment Advisory / Portfolio Management
- Non-core - Distribution of Financial Products
- Non-core - Trading / Clearing Member
- Non-core - Registrar & Share Transfer Agent / Trusteeship
- Aircraft Lessor (ACL)
- Ship Lessor (SHL)
- ITFS Platform Operator (ITFS)
- All FC/FU (ALL)

**Due Date & Frequency (IFSCA_FC_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (IFSCA_FC_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Internal Audit, Credit. Family additions: Internal Audit, Credit.

**Compliance Type (IFSCA_FC_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (IFSCA_FC_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (IFSCA_FC_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- IFSCA
- IFSCA (prior approval)
- IFSCA (intimation)
- IFSCA / FIU-IND
- Home country regulator (NOC)
- MCA
- RBI (FEMA)
- Central Registry (CERSAI)
- GIFT SEZ - Development Commissioner
- Management
- Not Required

## 3. Applicability logic for this family

- Prudential rows (capital ratio, LCR, exposure ceiling) apply to FCs/FUs undertaking core activities. GRCTCs follow their own framework.
- Each non-core activity needs its own registration under the relevant framework. Write the registration row with that activity in General Applicability (Type).

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- IFSCA (Finance Company) Regulations, 2021 (as amended, incl. Notification IFSCA/2022-23/GN/REG026, 1 Jul 2022)
- IFSCA Guidelines on Corporate Governance & Disclosure Requirements for FCs (2021, updated 4 Apr 2025)
- IFSCA (Registration of Factors and Assignment of Receivables) Regulations, 2024
- Frameworks for GRCTC, aircraft lease, ship lease and ITFS [VERIFY current versions]
- IFSCA Guidelines on Liquidity Risk Management for FC/FU (24 Jun 2021)

## 5. Family-specific pitfalls

- Treating a Finance Unit as a separate legal entity. It is not, so its parent's obligations and home-regulator NOC rows matter.

## 6. File naming

`IFSCA-FCFU - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Form of Set-up | Company · Branch · LLP · Trust | Use where the obligation differs by legal form (e.g., net-worth tests for a branch measured at parent level; LLP or trust structures for FMEs and schemes). |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-IFSCA-FCFU-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Finance, Treasury and Accounts → Owned fund / Capital; Credit → Lending / Leasing; Returns & Reporting → IFSCA returns; Compliance → Registration conditions. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Lending and leasing → Credit; owned-fund rows → Regulatory; Credit; treasury centre rows → Market / Liquidity. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Does the Finance Company / Finance Unit maintain at all times the minimum owned fund prescribed for its activities? |
| 4 | Clause / Para No. (`clause_ref`) | Regulation [VERIFY], IFSCA (Finance Company) Regulations, 2021 |
| 5 | Department (`department`) | Finance, Treasury and Accounts |
| 6 | Due Date & Frequency (`frequency`) | Ongoing/Continuous |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | IFSCA |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | International Financial Services Centres Authority (Finance Company) Regulations, 2021 |
| 12 | Instrument Reference No. (`instrument_ref`) | IFSCA/[VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | [VERIFY] |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY latest amendment] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | New |
| 17 | Change Note / Previous Actionable (`change_note`) | [VERIFY] instrument dates and the owned-fund amount per activity. |
| 18 | Source Link (`source_url`) | https://www.ifsca.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | Finance Company / Finance Unit (FCFU) |
| 20 | General Applicability (Type) (`applic_type`) | Core - Lending, Commitments, Guarantees, Credit Enhancement, Securitisation, Financial Lease |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | The minimum owned fund is USD [VERIFY] million for core activities; for a Finance Unit (branch) it may be maintained at the parent level [VERIFY]. |
| 22 | Applicable From (`applic_from`) | [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Form of Set-up (`ext_*`) | Company; Branch |
| 24 | Short Title (`short_title`) | Capital - minimum owned fund |
| 25 | Interpretation / Explanation (`explanation`) | The owned-fund test applies at all times; a fall below the minimum must be restored within the period IFSCA allows [VERIFY]. (Abridged.) |
| 26 | Department Function (`dept_function`) | Capital Management |
| 27 | Department Sub-function (`dept_subfunction`) | Owned fund |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Test at the end of each quarter |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | IFSCA — periodic return [VERIFY] |
| 32 | Portal / Form / Return Code (`filing_form`) | [VERIFY] |
| 33 | Related Document / Policy / Committee (`related_docs`) | Capital plan; Board |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the Finance Company Regulations; IFSCA may suspend or cancel registration or impose a penalty under the IFSCA Act [VERIFY section]. |
| 36 | Penalty Provision (`penalty_ref`) | [VERIFY] |
| 37 | Risk Type (`risk_type`) | Credit; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Quarterly owned-fund computation; auditor certificate where required [VERIFY]; IFSCA filing acknowledgement |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Compute owned fund at each quarter end in USD. Have the CFO approve it. Escalate to the Board if headroom falls below 10%. |
| 42 | Checker Review Points (`checker_points`) | 1. Computation follows the regulation's definition. 2. FX conversion uses the prescribed rate. 3. Owned fund ≥ minimum at each quarter end. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Re-perform one quarter's computation. 2. Inspect the auditor certificate. Exception: any quarter below minimum. |
| 44 | Tags / Keywords (`tags`) | owned fund; finance company; finance unit; ifsca capital |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

