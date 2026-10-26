# 18 — IRDAI-INT Family Command: Insurance Intermediaries

**Template:** `templates/LDC-TPL-IRDAI-INT-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-IRDAI-INT-v1.0` · **Regulator / authority:** Insurance Regulatory and Development Authority of India · **Named-range prefix:** `IRDAI_INT_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Intermediary Class.** Column C holds the intermediary class (broker, corporate agent, IMF, web aggregator, TPA, surveyor, CSC/POSP channel, MGA, insurance repository).

**Column D — Intermediary Type.** Column D refines it (direct life/general/composite broker, reinsurance broker, corporate agent by line, bank or NBFC as corporate agent, individual or corporate surveyor). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (IRDAI_INT_Sector):**
- Insurance Broker
- Corporate Agent
- Insurance Marketing Firm (IMF)
- Web Aggregator
- Third Party Administrator (TPA)
- Surveyor and Loss Assessor
- Common Service Centre / POSP channel
- Managing General Agent (MGA)
- Insurance Repository
- All Intermediaries

**Column D (IRDAI_INT_Entity):**
- Direct Broker - Life
- Direct Broker - General
- Direct Broker - Life and General
- Reinsurance Broker
- Composite Broker
- Corporate Agent - Life
- Corporate Agent - General
- Corporate Agent - Health
- Corporate Agent - Composite
- Bank / NBFC as Corporate Agent
- Insurance Marketing Firm
- Web Aggregator
- TPA - Health Services
- Surveyor (Individual)
- Surveyor (Corporate)
- Point of Sales Person (POSP) platform
- All Intermediaries (ALL)

**Column H (IRDAI_INT_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (IRDAI_INT_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Sales & Distribution, Claims Support, Policyholder Grievance, Internal Audit. Family additions: Sales & Distribution, Claims Support, Policyholder Grievance, Internal Audit.

**Column O (IRDAI_INT_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (IRDAI_INT_Risk):** High, Medium, Low.

**Column P reference list (IRDAI_INT_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- IRDAI (filing)
- IRDAI (prior approval)
- IRDAI (intimation)
- IRDAI Bima Bharosa (grievance)
- Partner Insurers
- FIU-IND (FINnet 2.0)
- CERT-In
- MCA (ROC)
- RBI (parent regulator - bank / NBFC CA)
- Board / Principal Officer
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- After the 2025 amendment, s.42D registration is perpetual subject to annual fee and conditions. Write an annual fee row and continuing-condition rows.
- Banks and NBFCs acting as corporate agents also follow RBI rules on third-party product distribution (Undertaking of Financial Services Direction for NBFCs). Note this in Column S and write the RBI rows in the RBI family.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Insurance Act, 1938 s.42D (as amended 2025: perpetual registration; MGAs and insurance repositories included)
- IRDAI (Insurance Brokers) Regulations, 2018
- IRDAI (Registration of Corporate Agents) Regulations, 2015
- IRDAI (TPA – Health Services) Regulations, 2016; IRDAI (Insurance Surveyors and Loss Assessors) Regulations, 2015
- IRDAI (Expenses of Management, including Commission, of Insurers) Regulations, 2024
- Consolidated intermediary regulations and master circulars of 2024–26 [VERIFY]

## 5. Family-specific pitfalls

- Treating individual agents as intermediaries in this family. They are appointed by insurers.

## 6. File naming

`IRDAI-INT - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
