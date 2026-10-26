# 20 — MCA-LLP Family Command: Limited Liability Partnerships

**Template:** `templates/LDC-TPL-MCA-LLP-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-MCA-LLP-v1.0` · **Regulator / authority:** Ministry of Corporate Affairs / Registrar of Companies · **Named-range prefix:** `MCA_LLP_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — LLP Class.** Column C holds the LLP class (LLP, small LLP, foreign LLP).

**Column D — Threshold / Overlay.** Column D holds thresholds and overlays (audit threshold, FDI, converted LLPs, body-corporate partners). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (MCA_LLP_Sector):**
- Limited Liability Partnership (LLP)
- Small LLP
- Foreign LLP
- All LLPs

**Column D (MCA_LLP_Entity):**
- Turnover above ₹40 lakh or contribution above ₹25 lakh (audit required)
- LLP with foreign investment (FEMA)
- LLP converted from company / firm
- LLP with body corporate partners
- All LLPs (ALL)

**Column H (MCA_LLP_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (MCA_LLP_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Secretarial, Tax. Family additions: Secretarial, Tax.

**Column O (MCA_LLP_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Registers & Records. Family additions: Registers & Records.

**Column R (MCA_LLP_Risk):** High, Medium, Low.

**Column P reference list (MCA_LLP_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- MCA (ROC) - LLP e-Form
- MCA - Regional Director
- NCLT
- RBI (FEMA) / AD Bank
- Income Tax Department
- Partners / Designated Partners
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- Annual filings: Form 11 (annual return, within 60 days of FY end) and Form 8 (statement of account and solvency, within 30 days of six months from FY end) [VERIFY].
- Register of partners and SBO rules were added by the 2022–2024 amendments [VERIFY].

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Limited Liability Partnership Act, 2008 (as amended 2021)
- LLP Rules, 2009 (incl. 2022–2024 amendments: Register of Partners, Significant Beneficial Ownership) [VERIFY]
- FEMA (Non-debt Instruments) Rules, 2019 (LLPs with FDI)

## 5. Family-specific pitfalls

- Applying company Board-meeting rules to LLPs.

## 6. File naming

`MCA-LLP - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
