# 06 — RBI-OTH Family Command: Other RBI-regulated entities (AIFIs, CICs, payment system operators, FEMA authorised persons)

**Template:** `templates/LDC-TPL-RBI-OTH-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-OTH-v1.0` · **Regulator / authority:** Reserve Bank of India · **Named-range prefix:** `RBI_OTH_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Entity Category.** Column C holds the category of RBI regulated entity outside banks, NBFCs and ARCs: AIFIs, Credit Information Companies, payment system operators and participants, and FEMA authorised persons.

**Column D — Entity Type.** Column D names the entity: EXIM, NABARD, NHB, SIDBI, NaBFID; the four CICs; PA, PA-P, PA-CB, PPI issuers, BBPOUs, TReDS, WLAOs, card networks; MTSS agents; AD-II, FFMC. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (RBI_OTH_Sector):**
- All India Financial Institution (AIFI)
- Credit Information Company (CIC)
- Payment System Operator / Participant
- Authorised Person (FEMA)
- All Other RBI Regulated Entities

**Column D (RBI_OTH_Entity):**
- EXIM Bank
- NABARD
- National Housing Bank (NHB)
- SIDBI
- NaBFID
- Credit Information Company (TransUnion CIBIL / Equifax / Experian / CRIF High Mark)
- Payment Aggregator - Online (PA)
- Payment Aggregator - Physical (PA-P)
- Payment Aggregator - Cross Border (PA-CB)
- Prepaid Payment Instrument Issuer (non-bank PPI)
- Bharat Bill Payment Operating Unit (BBPOU)
- Trade Receivables Discounting System (TReDS)
- White Label ATM Operator (WLAO)
- Card Network
- Money Transfer Service Scheme (MTSS) Indian Agent
- Authorised Dealer Category II (AD-II)
- Full Fledged Money Changer (FFMC)
- All (ALL)

**Column H (RBI_OTH_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (RBI_OTH_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Internal Audit, Customer Service & Grievance, Information Security, KYC & AML. Family additions: Internal Audit, Customer Service & Grievance, Information Security, KYC & AML.

**Column O (RBI_OTH_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (RBI_OTH_Risk):** High, Medium, Low.

**Column P reference list (RBI_OTH_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- RBI - CIMS (Supervisory Returns)
- RBI - DAKSH (Supervisory Compliance)
- RBI - PRAVAAH (Applications / Approvals)
- RBI (prior approval)
- RBI (intimation)
- RBI - Department of Regulation
- RBI - Department of Supervision
- RBI - Department of Payment & Settlement Systems
- RBI - Foreign Exchange Department (FEMA)
- NPCI
- Ministry of Finance
- SEBI / Stock Exchanges (listed bonds)
- FIU-IND (FINnet 2.0)
- Credit Information Companies (CICs)
- CERSAI / CKYCR
- CERT-In
- Board / Management
- Statutory / Central Auditor
- Not Required

## 3. Applicability logic for this family

- PSS Act s.4 authorisation and conditions are the base rows for payment entities. Directions on PAs (2025) and PPIs carry net worth, escrow and governance rows [VERIFY current titles].
- CIC obligations come from CICRA 2005, the CIC Rules/Regulations 2006 and the RBI CIC directions. Lender-side credit-reporting obligations belong in the lender family.
- AIFIs have 19 topic directions (28 Nov 2025). Treat them like bank directions with C = AIFI.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- RBI (All India Financial Institutions – <topic>) Directions, 2025 (19 directions of 28 Nov 2025)
- Credit Information Companies (Regulation) Act, 2005; CIC Rules and Regulations, 2006; RBI (Credit Information Companies) Directions, 2025
- Payment and Settlement Systems Act, 2007 and Regulations, 2008; RBI directions on Payment Aggregators (2025), PPIs, BBPS, TReDS [VERIFY]
- FEMA, 1999 and RBI master directions for authorised persons (AD Category II, FFMC) [VERIFY]

## 5. Family-specific pitfalls

- Writing lender-side CIC reporting rows here. They belong in the lender families.
- Missing card-network and PA-CB cross-border rows.

## 6. File naming

`RBI-OTH - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
