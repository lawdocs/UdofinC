# 21 — DATA-PRIV Family Command: Data Protection and Privacy (DPDP, IT Act, GDPR, CCPA)

**Template:** `templates/LDC-TPL-DATA-PRIV-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-DATA-PRIV-v1.0` · **Regulator / authority:** MeitY / Data Protection Board of India; EU supervisory authorities; California Privacy Protection Agency · **Named-range prefix:** `DATA_PRIV_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Law / Jurisdiction.** Column C holds the law or jurisdiction (DPDP Act and Rules; IT Act and SPDI Rules; EU GDPR; UK GDPR; CCPA/CPRA; sectoral data rules).

**Column D — Role.** Column D holds the privacy role (Data Fiduciary, SDF, Data Processor, Consent Manager; GDPR controller/processor/joint controller/representative; CCPA business/service provider/contractor/third party; data broker). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (DATA_PRIV_Sector):**
- DPDP Act, 2023 and DPDP Rules, 2025 (India)
- IT Act, 2000 and SPDI Rules, 2011 (India)
- EU GDPR (EU/EEA)
- UK GDPR and DPA 2018 (UK)
- CCPA as amended by CPRA (California)
- Sectoral data rules (RBI / SEBI / IRDAI / IFSCA)
- Other jurisdiction

**Column D (DATA_PRIV_Entity):**
- Data Fiduciary
- Significant Data Fiduciary (SDF)
- Data Processor
- Consent Manager
- Intermediary
- Controller (GDPR)
- Processor (GDPR)
- Joint Controller (GDPR)
- EU Representative (Art. 27)
- Business (CCPA)
- Service Provider / Contractor (CCPA)
- Third Party (CCPA)
- Data Broker
- Body corporate handling SPDI
- All Roles (ALL)

**Column H (DATA_PRIV_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (DATA_PRIV_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Privacy Office (DPO), Information Security, Marketing, Customer Service & Grievance, Product & Engineering. Family additions: Privacy Office (DPO), Information Security, Marketing, Customer Service & Grievance, Product & Engineering.

**Column O (DATA_PRIV_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Notices & Consents. Family additions: Notices & Consents.

**Column R (DATA_PRIV_Risk):** High, Medium, Low.

**Column P reference list (DATA_PRIV_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- Data Protection Board of India
- Affected Data Principals (intimation)
- Consent Manager
- CERT-In
- Sectoral Regulator (RBI / SEBI / IRDAI / IFSCA)
- EU / EEA Supervisory Authority (Lead SA)
- Affected Data Subjects (GDPR)
- California Privacy Protection Agency / Attorney General
- Consumers (CCPA notices)
- Board / DPO
- Independent Data Auditor
- Not Required

## 3. Applicability logic for this family

- DPDP obligations commence in phases: Rules 1, 2 and 17–21 from 13 Nov 2025; Rule 4 (Consent Managers) from 13 Nov 2026; Rules 3, 5–16, 22 and 23 from 13 May 2027. Put the commencement date in Column S of every row.
- SDF obligations (DPO in India, independent data auditor, periodic DPIA and audit, algorithmic due diligence, data localisation of specified data) apply only on notification as an SDF. Use D = SDF.
- Sectoral data rules (RBI, SEBI, IRDAI, IFSCA) override or add to DPDP. Write sectoral rows in the sectoral family and cross-reference them here.
- GDPR and CCPA rows apply only where territorial scope tests are met (GDPR Art. 3; CCPA thresholds). Write the test in Column S.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025 (G.S.R. 846(E), 13 Nov 2025; phased: 13 Nov 2025, 13 Nov 2026, 13 May 2027)
- Information Technology Act, 2000 ss.43A, 72A and IT (Reasonable Security Practices and SPDI) Rules, 2011 (until superseded)
- Regulation (EU) 2016/679 (GDPR)
- California Consumer Privacy Act as amended by CPRA (Cal. Civ. Code §1798.100 et seq.) and CCPA Regulations (2025 rules on risk assessments, cybersecurity audits and ADMT; effective 1 Jan 2026 with later phases) [VERIFY]

## 5. Family-specific pitfalls

- Stating DPDP obligations as already in force before 13 May 2027.
- Using the SPDI Rules after they are superseded [VERIFY].

## 6. File naming

`DATA-PRIV - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
