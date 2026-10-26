# 17 — IRDAI-INS Family Command: Insurers (life, general, health, reinsurers, FRBs)

**Template:** `templates/LDC-TPL-IRDAI-INS-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-IRDAI-INS-v1.0` · **Regulator / authority:** Insurance Regulatory and Development Authority of India · **Named-range prefix:** `IRDAI_INS_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Insurer Class.** Column C holds the insurer class: life, general, standalone health, Indian reinsurer, FRB, Lloyd's India, composite/multi-line [VERIFY after the 2025 amendment].

**Column D — Insurer Overlay.** Column D holds overlays: public or private, listed, specialised insurer, bancassurance partner, ULIP, health products. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (IRDAI_INS_Sector):**
- Life Insurer
- General Insurer
- Standalone Health Insurer
- Indian Reinsurer
- Foreign Reinsurer Branch (FRB)
- Lloyd's India
- Composite Insurer (where licensed)
- All Insurers

**Column D (IRDAI_INS_Entity):**
- Public Sector Insurer
- Private Insurer
- Listed Insurer
- Specialised Insurer (e.g., agriculture, micro, export credit)
- Insurer with bancassurance / corporate agency tie-ups
- Insurer offering Unit Linked products
- Insurer offering Health products
- All Insurers (ALL)

**Column H (IRDAI_INS_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (IRDAI_INS_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Actuarial, Underwriting, Claims, Investments, Policyholder Servicing & Grievance, Internal Audit, Information Security. Family additions: Actuarial, Underwriting, Claims, Investments, Policyholder Servicing & Grievance, Internal Audit, Information Security.

**Column O (IRDAI_INS_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (IRDAI_INS_Risk):** High, Medium, Low.

**Column P reference list (IRDAI_INS_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- IRDAI (filing)
- IRDAI (prior approval / product filing)
- IRDAI (intimation)
- IRDAI Bima Bharosa (grievance)
- Insurance Ombudsman (CIO)
- Insurance Information Bureau (IIB)
- Life Insurance Council / General Insurance Council
- FIU-IND (FINnet 2.0)
- CERT-In
- SEBI / Stock Exchanges (listed insurers)
- MCA (ROC)
- Appointed Actuary
- Board / Management
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- IRDAI moved to principle-based regulations in 2024 with master circulars. Cite both the regulation and the master circular paragraph.
- Check the Sabka Bima Sabki Raksha (Amendment of Insurance Laws) Act, 2025 for commencement of changed sections before citing amended section numbers [VERIFY].

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Insurance Act, 1938 as amended by the Sabka Bima Sabki Raksha (Amendment of Insurance Laws) Act, 2025 [VERIFY commencement]
- IRDA Act, 1999
- IRDAI principle-based regulations, 2024 (Registration, Capital Structure, Transfer of Shares and Amalgamation; Corporate Governance; Protection of Policyholders' Interests; Actuarial, Finance and Investment Functions; Expenses of Management incl. Commission; Insurance Products; Rural, Social Sector and Motor Third Party Obligations) and master circulars [VERIFY exact titles]
- IRDAI Information and Cyber Security Guidelines, 2023

## 5. Family-specific pitfalls

- Citing repealed 2016/2017 regulations after the 2024 consolidation.
- Missing master-circular paragraph numbers.

## 6. File naming

`IRDAI-INS - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
