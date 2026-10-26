# 19 — MCA-CO Family Command: Companies (Companies Act, 2013)

**Template:** `templates/LDC-TPL-MCA-CO-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-MCA-CO-v1.0` · **Regulator / authority:** Ministry of Corporate Affairs / Registrar of Companies · **Named-range prefix:** `MCA_CO_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Company Class.** Column C holds the company class. Many provisions differ for private, OPC, small, Section 8, producer, Nidhi and government companies through exemption notifications (for example the 5 June 2015 notifications for private and government companies). Use the class value and record the exemption in Column S.

**Column D — Threshold / Overlay.** Column D holds thresholds and overlays that switch obligations on: paid-up capital, turnover and borrowing thresholds (s.149, s.177, s.178, s.203, s.204), CSR thresholds (s.135(1)), deposits, foreign investment, dormant status. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (MCA_CO_Sector):**
- Private Limited Company
- Public Limited Company (Unlisted)
- Public Limited Company (Listed)
- One Person Company (OPC)
- Small Company
- Section 8 Company
- Producer Company
- Nidhi Company
- Government Company
- Foreign Company
- All Companies

**Column D (MCA_CO_Entity):**
- Paid-up capital ≥ ₹10 crore
- Turnover ≥ ₹100 crore
- Outstanding borrowings/deposits ≥ ₹50 crore
- CSR applicable (s.135(1) thresholds)
- Ind AS applicable
- Holding / Subsidiary company
- Company accepting deposits (Chapter V)
- Company with foreign investment (FEMA)
- Dormant company (s.455)
- Start-up (DPIIT recognised)
- Company required to appoint KMP (s.203)
- Company requiring secretarial audit (s.204)
- Company requiring cost audit (s.148)
- All Companies (ALL)

**Column H (MCA_CO_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (MCA_CO_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Secretarial, Internal Audit, Tax. Family additions: Secretarial, Internal Audit, Tax.

**Column O (MCA_CO_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Registers & Records. Family additions: Registers & Records.

**Column R (MCA_CO_Risk):** High, Medium, Low.

**Column P reference list (MCA_CO_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- MCA (ROC) - e-Form
- MCA - Regional Director
- NCLT
- IEPF Authority
- Central Government (MCA)
- RBI (FEMA) / AD Bank
- SEBI / Stock Exchanges (listed)
- Income Tax Department
- Members (general meeting / website)
- Board / Management
- Statutory Auditor
- Secretarial Auditor / PCS
- Cost Auditor
- Not Required

## 3. Applicability logic for this family

- Write one sheet per Chapter or Rule set (Meetings of Board; Management and Administration; Accounts; Audit and Auditors; Appointment of Directors; Share Capital; Deposits; CSR; SBO), plus SS-1 and SS-2.
- Every e-form filing is a Returns & Reporting row with "Due:" (for example AOC-4 within 30 days of the AGM; MGT-7 within 60 days of the AGM).
- Registers (MBP-1, MBP-2, MBP-4, MGT-1, CHG-7, SH-6, BEN-3) are "Registers & Records" rows.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Companies Act, 2013 and Rules (Incorporation; Management and Administration; Meetings of Board; Accounts; Audit and Auditors; Appointment and Qualification of Directors …)
- Exemption notifications for private, government, Section 8 and Nidhi companies (5 Jun 2015 and later) [VERIFY]
- ICSI Secretarial Standards SS-1 and SS-2 (revised, effective 1 Apr 2024)
- MCA21 V3 e-forms (all Companies Act e-forms on V3 since 14 Jul 2025)
- FEMA (Non-debt Instruments) Rules, 2019 (companies with foreign investment)
- Companies (Auditor's Report) Order, 2020 (auditor-side; write company-side preparation rows only)

## 5. Family-specific pitfalls

- Missing the private-company exemptions in Column S.
- Writing form numbers from MCA21 V2 that have changed in V3 [VERIFY].

## 6. File naming

`MCA-CO - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
