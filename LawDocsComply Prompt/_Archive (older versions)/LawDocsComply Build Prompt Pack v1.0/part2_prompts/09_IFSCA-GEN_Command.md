# 09 — IFSCA-GEN Family Command: IFSCA Regulated Entities (all types)

**Template:** `templates/LDC-TPL-IFSCA-GEN-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-IFSCA-GEN-v1.0` · **Regulator / authority:** International Financial Services Centres Authority · **Named-range prefix:** `IFSCA_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Sector.** Column C holds the IFSCA sector, exactly as in the owner's existing IFSCA sheets (Banking, Finance Company, Fund Management, Capital Markets, Insurance, Bullion, Payments, FinTech, Ancillary Services, GIC, Education, Trade Finance, Cross-cutting).

**Column D — Entity Type.** Column D holds the IFSCA entity type from the owner's 40-entry list, for example "IFSC Banking Unit (IBU)" or "Recognised Stock Exchange (RSEX); Recognised Clearing Corporation (RCCP); Recognised Depository (RDEP)". Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (IFSCA_Sector):**
- Banking
- Finance Company
- Fund Management
- Capital Markets
- Insurance
- Metals & Commodities (Bullion)
- Payments
- FinTech
- Ancillary Services
- Global In-House Centre
- Education
- Trade Finance
- Cross-cutting / All REs

**Column D (IFSCA_Entity):**
- IFSC Banking Unit (IBU)
- IFSC Banking Company (IBC)
- Finance Company / Finance Unit (FCFU)
- Aircraft Lessor (ACL)
- Ship Lessor (SHL)
- Fund Management Entity (FME)
- Pension Fund (PENF)
- Market Infrastructure Institution (MII)
- Capital Market Intermediary (CMI)
- Recognised Stock Exchange (RSEX)
- Recognised Clearing Corporation (RCCP)
- Recognised Depository (RDEP)
- Broker Dealer / Clearing Member (BDCM)
- Custodian / Depository Participant (CUDP)
- Investment Adviser / Portfolio Manager (IAPM)
- Investment Banker (INVB)
- Distributor (DIST)
- Debenture Trustee (DTEE)
- Credit Rating Agency (CRA)
- Research Entity (RESE)
- ESG Ratings & Data Products Provider (ERDP)
- KYC Registration Agency (KRA)
- Issuer / Listed Entity (ISSU)
- IFSC Insurance Office (IIO)
- IFSC Insurance Intermediary Office (IIIO)
- Insurance Web Aggregator (IWA)
- Managing General Agent (MGA)
- Bullion Exchange / Clearing Corp / Depository (BMII)
- Vault Manager (VM)
- Bullion Trading / Clearing Member (BTCM)
- Payment Service Provider (PSP)
- Payment System Operator (PSO)
- FinTech Entity (FE)
- TechFin Entity (TFIN)
- Ancillary Service Provider (ASP)
- Book-keeping/Accounting/Taxation/FCC Provider (BATF)
- Global In-House Centre (GIC)
- International Branch Campus / Offshore Education Centre (EDU)
- ITFS Platform Operator (ITFS)
- All Regulated Entities (ALL)

**Column H (IFSCA_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time. (Base list only; this family is a byte-exact replica of the owner's IFSCA vocabulary.)

**Column M (IFSCA_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management.

**Column O (IFSCA_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (IFSCA_Risk):** High, Medium, Low.

**Column P reference list (IFSCA_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- IFSCA
- IFSCA (prior approval)
- IFSCA (intimation)
- IFSCA / FIU-IND
- Home country regulator (NOC)
- MCA
- RBI (FEMA)
- Central Registry (CERSAI)
- Management
- Not Required

## 3. Applicability logic for this family

- This template is a byte-exact replica of the owner's IFSCA vocabulary, so existing IFSCA sheets remain valid. Continue the established method: one sheet per regulation, handbook, guideline or circular, with the depth of the existing sheets (11–389 rows; mean about 65).
- Use IFSCA-FCFU or IFSCA-FME instead when a finer activity or scheme classification is needed.
- The org egress allowlist blocks ifsca.gov.in from the automation shell. Download source PDFs on the Mac and attach them.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- IFSCA Act, 2019
- IFSCA (Banking) Regulations, 2020 and Banking Handbook (GEN, COB, PRU)
- IFSCA (Finance Company) Regulations, 2021
- IFSCA (Fund Management) Regulations, 2025 (as amended up to 10 Sep 2026)
- IFSCA (Capital Market Intermediaries) Regulations, 2025; MII Regulations, 2021; Listing Regulations, 2024; KRA Regulations, 2025; Prohibition of Market Abuse Regulations, 2026
- IFSCA insurance regulations (Registration of Insurance Business 2021; Insurance Intermediary 2021; Managing General Agents 2026; Re-insurance 2023; solvency, investment, actuarial and records regulations)
- IFSCA (AML, CFT and KYC) Guidelines, 2022 — master as on 3 Aug 2026
- IFSCA (Payment Services) Regulations, 2024; Bullion Market Regulations, 2025; TechFin and Ancillary Services Regulations, 2025; BATF Regulations, 2024; GIC Regulations, 2025

## 5. Family-specific pitfalls

- Using the old "IFSCA Format for Question Final" vocabulary (it has typos and no named ranges).
- Missing the consolidated "as amended up to" text for FM, Insurance Registration and TechFin.

## 6. File naming

`IFSCA-GEN - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
