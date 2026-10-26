# 14 — SEBI-LISTED Family Command: Listed Entities (equity, SME, debt, HVDLE)

**Template:** `templates/LDC-TPL-SEBI-LISTED-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-SEBI-LISTED-v1.0` · **Regulator / authority:** Securities and Exchange Board of India; Stock Exchanges · **Named-range prefix:** `SEBI_LST_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Listing Segment.** Column C holds the listing segment: main board specified securities, SME platform, non-convertible securities (debt-listed), HVDLE, both equity and debt, Social Stock Exchange, listed CP.

**Column D — Entity Overlay.** Column D holds overlays that change applicability: top 100/500/1000/2000 by market capitalisation, material subsidiary, SR equity, PSU, sectoral regulated entity, newly listed, entity under CIRP. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (SEBI_LST_Sector):**
- Main Board - Specified Securities
- SME Exchange / SME Platform
- Non-Convertible Securities (Debt-listed)
- High Value Debt Listed Entity (HVDLE)
- Specified Securities and Non-Convertible Securities
- Social Stock Exchange
- Commercial Paper (listed)
- All Listed Entities

**Column D (SEBI_LST_Entity):**
- Top 100 listed entities (by market capitalisation)
- Top 500 listed entities
- Top 1000 listed entities
- Top 2000 listed entities
- Listed entity with material subsidiary
- Listed entity with SR equity shares
- Public Sector Undertaking (listed)
- Listed Bank / NBFC / Insurer (sectoral overlay)
- Newly listed entity (IPO year)
- Entity under CIRP (IBC)
- All Listed Entities (ALL)

**Column H (SEBI_LST_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (SEBI_LST_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Secretarial, Investor Relations, Internal Audit. Family additions: Secretarial, Investor Relations, Internal Audit.

**Column O (SEBI_LST_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Disclosures. Family additions: Disclosures.

**Column R (SEBI_LST_Risk):** High, Medium, Low.

**Column P reference list (SEBI_LST_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- Stock Exchanges (NSE NEAPS / BSE Listing Centre)
- Stock Exchanges (prior approval / in-principle)
- SEBI (filing)
- SEBI SCORES / SMART ODR
- Depositories (NSDL / CDSL)
- RTA
- MCA (ROC)
- Debenture Trustee
- Credit Rating Agency
- Shareholders (website / newspaper)
- IEPF Authority
- Board / Audit Committee
- Secretarial Auditor
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- LODR Chapter IV (specified securities) and Chapter V (non-convertible securities) differ. Write separate rows with the correct C.
- Reg. 15(2) exempts SME-listed and small entities from regs. 17–27 and other provisions. Record this in Column S [VERIFY current thresholds].
- Market-cap rankings are taken as on 31 December (or the date SEBI specifies) [VERIFY]. Write the ranking test in Column S.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015 (as amended, incl. Fifth Amendment 2025)
- SEBI Master Circulars on compliance with LODR (specified securities; non-convertible securities) [VERIFY dates]
- SEBI (Prohibition of Insider Trading) Regulations, 2015
- SEBI (Substantial Acquisition of Shares and Takeovers) Regulations, 2011
- SEBI (ICDR) Regulations, 2018 (continuing obligations); SEBI (Buy-back) Regulations, 2018; SEBI (SBEB & SE) Regulations, 2021
- BRSR / BRSR Core framework
- Companies Act, 2013 provisions applicable to listed companies (ss. 149(4), 177, 178, 204)

## 5. Family-specific pitfalls

- Ignoring the SOP fine schedule for each regulation in Column Q.
- Writing equity-only rows for debt-listed entities.

## 6. File naming

`SEBI-LISTED - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
