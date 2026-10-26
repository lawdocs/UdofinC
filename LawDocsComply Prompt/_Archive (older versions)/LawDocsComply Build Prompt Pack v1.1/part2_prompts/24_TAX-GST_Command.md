# 24 — TAX-GST Family Command: GST, Income-tax, TDS/TCS and State Taxes

**Template:** `templates/LDC-TPL-TAX-GST-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-TAX-GST-v1.0` · **Regulator / authority:** CBIC / GSTN; CBDT; State tax departments · **Named-range prefix:** `TAX_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Law.** Column C holds the tax law (GST Acts; Income-tax Act, 2025; Income-tax Act, 1961 for earlier years; TDS/TCS; State PT; stamp duty).

**Column D — Taxpayer Type.** Column D holds the taxpayer type that changes obligations (regular, composition, ISD, GST TDS deductor, e-commerce operator, NRTP, OIDAR, financial institution with the rule 38 ITC option, SEZ, e-invoicing applicable, company, co-operative, LLP, tax-audit applicable). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (TAX_Sector):**
- CGST / SGST / IGST Acts, 2017
- Income-tax Act, 2025
- Income-tax Act, 1961 (transition / earlier years)
- TDS / TCS
- Professional Tax (State)
- Stamp Duty (State)
- All Tax Laws

**Column D (TAX_Entity):**
- Regular GST taxpayer
- Composition taxpayer
- Input Service Distributor (ISD)
- GST TDS deductor
- E-commerce operator (TCS)
- Non-resident taxable person
- OIDAR service provider
- Banking company / financial institution / NBFC (rule 38 ITC option)
- SEZ unit / developer
- E-invoicing applicable taxpayer
- Company assessee
- Co-operative society assessee
- LLP / Firm assessee
- Tax audit applicable
- All (ALL)

**Column H (TAX_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (TAX_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Tax, Accounts Payable, Billing & Receivables. Family additions: Tax, Accounts Payable, Billing & Receivables.

**Column O (TAX_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (TAX_Risk):** High, Medium, Low.

**Column P reference list (TAX_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- GSTN Portal (GSTR)
- E-invoice IRP
- E-way Bill Portal
- Income-tax e-Filing Portal
- TRACES (TDS / TCS)
- Protean (TIN)
- State Professional Tax Portal
- GST / Income-tax Authorities (notices / appeals)
- Tax Auditor (CA)
- Board / Management
- Not Required

## 3. Applicability logic for this family

- The Income-tax Act, 2025 applies from tax year 2026-27 (1 Apr 2026). Earlier years stay under the 1961 Act. Section and form numbers changed, so cite the new numbers [VERIFY].
- Banking companies, financial institutions and NBFCs may avail 50% ITC under rule 38 of the CGST Rules. Write this as a choice row.
- GST return due dates are set by notification and may be staggered by State. Put the rule in Column P and mark [VERIFY] where a notification changes it.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- CGST Act, 2017; IGST Act, 2017; CGST Rules, 2017 (incl. GST rate rationalisation of Sep 2025) [VERIFY]
- Income-tax Act, 2025 (in force from 1 Apr 2026) and Income-tax Rules [VERIFY form numbers]
- State Professional Tax Acts

## 5. Family-specific pitfalls

- Using 1961 Act section numbers for FY 2026-27 obligations.

## 6. File naming

`TAX-GST - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
