# 22 — CYBER Family Command: Cyber Security and IT Governance

**Template:** `templates/LDC-TPL-CYBER-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-CYBER-v1.0` · **Regulator / authority:** CERT-In / MeitY; sectoral regulators (RBI, SEBI, IRDAI, IFSCA) · **Named-range prefix:** `CYBER_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Framework.** Column C holds the framework (CERT-In Directions, IT Act s.70/NCIIPC, RBI IT/cyber directions, SEBI CSCRF, IRDAI guidelines, IFSCA guidelines, DPDP Rule 6, ISO 27001, NIST CSF, PCI DSS).

**Column D — Entity Category.** Column D holds the entity category that changes the requirement (all body corporates, data centre/cloud/VPN providers, CII, bank, NBFC by layer, UCB by tier, SEBI CSCRF categories, insurer, IFSCA RE, payment entity). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (CYBER_Sector):**
- CERT-In Directions, 2022 (IT Act s.70B)
- IT Act s.70 / NCIIPC (CII / Protected Systems)
- RBI IT and Cyber Security Directions
- SEBI CSCRF
- IRDAI Information and Cyber Security Guidelines, 2023
- IFSCA Cyber Security Guidelines
- DPDP security safeguards (Rule 6)
- ISO/IEC 27001:2022
- NIST CSF 2.0
- PCI DSS v4.0.1
- All Frameworks

**Column D (CYBER_Entity):**
- All body corporates / service providers
- Data centre / cloud / VPS / VPN provider
- Critical Information Infrastructure / Protected System
- Bank
- NBFC (by layer)
- UCB (by tier)
- SEBI MII
- SEBI Qualified RE
- SEBI Mid-size RE
- SEBI Small-size RE
- SEBI Self-certification RE
- Insurer / Insurance Intermediary
- IFSCA Regulated Entity
- Payment entity (card data)
- All (ALL)

**Column H (CYBER_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (CYBER_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Information Security, IT Infrastructure, Application Development, Business Continuity. Family additions: Information Security, IT Infrastructure, Application Development, Business Continuity.

**Column O (CYBER_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (CYBER_Risk):** High, Medium, Low.

**Column P reference list (CYBER_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- CERT-In (incident report)
- NCIIPC
- RBI (CSITE / Department of Supervision)
- SEBI (CSCRF reporting / SI Portal)
- IRDAI
- IFSCA
- Stock Exchanges / Depositories (MIIs)
- Data Protection Board of India
- Board / IT Strategy Committee
- CISO / Information Security Steering Committee
- Auditor (CERT-In empanelled)
- Not Required

## 3. Applicability logic for this family

- Statutory rows (CERT-In, NCIIPC, DPDP) are Compliance. ISO, NIST and PCI rows are "Suggestive Compliance" unless a regulator or contract mandates them.
- Write sector cyber directions here only where the owner wants a single cyber view. Otherwise put them in the sector family and cross-reference.
- Log retention (180 days in India), NTP synchronisation, and incident reporting within 6 hours are key CERT-In rows.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- CERT-In Directions No. 20(3)/2022-CERT-In dated 28 Apr 2022 and FAQs
- IT Act, 2000 ss.43, 66, 70, 70A, 70B, 72A; IT (CERT-In and manner of performing functions) Rules, 2013
- RBI cyber/IT directions for banks, UCBs and NBFCs (incl. RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026, RBI/DoS/2026-27/461) [VERIFY]
- SEBI CSCRF (20 Aug 2024) and clarifications
- IRDAI Information and Cyber Security Guidelines, 2023
- IFSCA cyber security guidelines (effective 1 Apr 2025) [VERIFY]
- ISO/IEC 27001:2022; NIST CSF 2.0; PCI DSS v4.0.1 (Suggestive Compliance unless contractually required)

## 5. Family-specific pitfalls

- Making ISO controls mandatory rows.
- Missing the 180-day log retention and NTP rows.

## 6. File naming

`CYBER - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
