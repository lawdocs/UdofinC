# 10 — IFSCA-FCFU Family Command: IFSCA Finance Companies and Finance Units

**Template:** `templates/LDC-TPL-IFSCA-FCFU-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-IFSCA-FCFU-v1.0` · **Regulator / authority:** International Financial Services Centres Authority · **Named-range prefix:** `IFSCA_FC_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Entity Form.** Column C says whether the row applies to a Finance Company, a Finance Unit (branch/unit of a foreign or Indian entity), or both.

**Column D — Activity / Registration.** Column D holds the activity or registration: GRCTC; core activities under reg. 5(1)(ii) (lending/credit enhancement/securitisation/financial lease; factoring and forfaiting; investments; derivatives); non-core activities under reg. 5(1)(iii) (merchant banking, advisory/PMS, distribution, trading/clearing membership, RTA/trusteeship); aircraft and ship lessors; ITFS operators. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (IFSCA_FC_Sector):**
- Finance Company (FC)
- Finance Unit (FU)
- Finance Company / Finance Unit (FCFU)

**Column D (IFSCA_FC_Entity):**
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

**Column H (IFSCA_FC_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (IFSCA_FC_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Internal Audit, Credit. Family additions: Internal Audit, Credit.

**Column O (IFSCA_FC_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (IFSCA_FC_Risk):** High, Medium, Low.

**Column P reference list (IFSCA_FC_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
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
- Each non-core activity needs its own registration under the relevant framework. Write the registration row with that activity in Column D.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- IFSCA (Finance Company) Regulations, 2021 (as amended, incl. Notification IFSCA/2022-23/GN/REG026, 1 Jul 2022)
- IFSCA Guidelines on Corporate Governance & Disclosure Requirements for FCs (2021, updated 4 Apr 2025)
- IFSCA (Registration of Factors and Assignment of Receivables) Regulations, 2024
- Frameworks for GRCTC, aircraft lease, ship lease and ITFS [VERIFY current versions]
- IFSCA Guidelines on Liquidity Risk Management for FC/FU (24 Jun 2021)

## 5. Family-specific pitfalls

- Treating a Finance Unit as a separate legal entity. It is not, so its parent's obligations and home-regulator NOC rows matter.

## 6. File naming

`IFSCA-FCFU - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
