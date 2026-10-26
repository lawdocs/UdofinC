# 15 — SEBI-REIT-INVIT Family Command: REITs, SM REITs and InvITs

**Template:** `templates/LDC-TPL-SEBI-REIT-INVIT-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-SEBI-REIT-INVIT-v1.0` · **Regulator / authority:** Securities and Exchange Board of India · **Named-range prefix:** `SEBI_REIT_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Trust Type.** Column C holds the trust type: REIT, SM REIT, public InvIT, private listed or unlisted InvIT.

**Column D — Role / Party.** Column D holds the party that bears the obligation: trust, manager/investment manager, trustee, sponsor, project manager, valuer, holdco/SPV. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (SEBI_REIT_Sector):**
- Real Estate Investment Trust (REIT)
- Small and Medium REIT (SM REIT)
- Infrastructure Investment Trust (InvIT) - Public
- InvIT - Private Listed
- InvIT - Private Unlisted
- All Investment Trusts

**Column D (SEBI_REIT_Entity):**
- Trust
- Manager / Investment Manager
- Trustee
- Sponsor / Sponsor Group
- Project Manager
- Valuer
- Holdco / SPV
- All Parties (ALL)

**Column H (SEBI_REIT_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (SEBI_REIT_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Secretarial, Investor Relations, Valuation, Asset Management. Family additions: Secretarial, Investor Relations, Valuation, Asset Management.

**Column O (SEBI_REIT_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Disclosures. Family additions: Disclosures.

**Column R (SEBI_REIT_Risk):** High, Medium, Low.

**Column P reference list (SEBI_REIT_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- SEBI (filing)
- SEBI (prior approval)
- Stock Exchanges
- Unitholders (disclosure)
- Trustee
- Valuer
- Credit Rating Agency
- Depositories
- MCA (ROC)
- Board of Manager
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- Governance obligations of the manager (board composition, committees, related-party transactions) mirror LODR. Cite the REIT/InvIT regulation, not LODR.
- Distribution and leverage limits are percentage tests. Put the number in the question.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SEBI (Real Estate Investment Trusts) Regulations, 2014 (incl. SM REIT chapter, 2024)
- SEBI (Infrastructure Investment Trusts) Regulations, 2014
- SEBI Master Circulars for REITs and InvITs [VERIFY dates]

## 5. Family-specific pitfalls

- Mixing REIT and InvIT leverage thresholds.

## 6. File naming

`SEBI-REIT-INVIT - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
