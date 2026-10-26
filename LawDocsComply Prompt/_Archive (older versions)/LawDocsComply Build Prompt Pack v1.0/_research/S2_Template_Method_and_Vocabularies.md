# S2 research note — owner's questionnaire method and entity-family vocabularies

As of 25 October 2026. Stream S2 (Excel templates, Part-2 prompts, Appendix E).

## 1. Owner's template, as found

Sources inspected (read-only):

- `SAMPLE - Finance Company Regulations 2021 - Compliance Questions.xlsx` (upload)
- `05 Insurance - IFSCA Appointed Actuary Regulations 2022.xlsx` (upload)
- `IFSCA Documents/IFSCA Format for Question Final.xlsx` (Mac)
- 43 finished sheets in `IFSCA Documents/IFSCA Compliance Question Sheets/` (Mac)

**Layout.** There are two sheets, `Sheet1` and `Rough`.

- Row 1 holds the group headers, merged as follows:
  - A1:J1 "List" (yellow FFFF00)
  - K1:S1 "Details" (blue 00B0F0)
  - T1:W1 "Maker" (green 47D359). X1 is styled the same green but is not merged.
  - Y1:AB1 "Checker" (red FF0000)
  - AC1:AD1 "Auditor" (amber FFC000)
- Row 2 holds the 30 column headers, A "Checkbox" to AD "Comments, if any, by Auditor". They are Times New Roman 12, bold and wrapped, with fills by group. C2 and D2 have no fill.
- H2 contains a line break: "Due date & \nFrequency".
- Freeze panes are set at A3. Row 2 is 98.5 pt high.
- Data rows use Times New Roman 10, wrap, top alignment and thin borders.
- Column widths run from 12.5 to 38.5 and are preserved from the sample.

**Data validation.** Every list validation has `showErrorMessage = False`, so users can type values that are not in the list. In particular, Column D can hold several entities.

- Ranges cover rows 3–320 or 3–345.
- They are named ranges on `Rough`:
  - IFSCA_Freq (H)
  - IFSCA_Sector (C)
  - IFSCA_Entity (D)
  - IFSCA_Dept (M)
  - IFSCA_CompType (O)
  - IFSCA_Risk (R)
- Column P has a "reference" list in `Rough` but no validation.

**Vocabulary versions.** The Appointed Actuary file is the most complete version. It has:

- 11 frequencies, including Half Yearly and Daily
- 13 sectors
- 40 entity types, including CMI, RSEX, RCCP, RDEP, IWA, PSO and ALL
- 9 departments
- 6 compliance types
- 3 risk levels
- 10 filing references, including CERSAI

All 43 finished sheets share this one `Rough` vocabulary. The older "IFSCA Format for Question Final" `Rough` holds an earlier, inconsistent list with spelling errors ("Adminstration", "Complaince") and no named ranges. It is superseded and must not be used as a base.

**Practice observed across the 2,809 finished rows (43 sheets).**

- Rows per sheet range from 11 to 389, with a mean of about 65. The COB Handbook has 389 rows and FM Regs 2025 has 173.
- **The multi-value delimiter in Column D is "; "** (semicolon followed by a space), for example "Recognised Stock Exchange (RSEX); Recognised Clearing Corporation (RCCP); Recognised Depository (RDEP)". Column N uses " | " between its reference parts.
- Column P holds list tokens only. "Not Required" appears in 54% of rows and "IFSCA" in 25%.
- Frequency mix:
  - Event Based 32%
  - Ongoing/Continuous 32%
  - Annually 19%
  - Others smaller
- Risk mix: High 78%, Medium 20%, Low 2%. High is over-used, so the Part-2 command adds a calibration rule.
- Column L follows a fixed shape:
  1. quotes the provision
  2. explains it in numbered points ("Three features…")
  3. links to related regulations
- Column Q states the provision breached, the enforcement power (Act and section) and the practical consequence.
- Column U names specific artefacts (Board resolution, register, URL with archived copy).
- Column V is an imperative, step-by-step instruction for the maker.
- Column K cites the substituting notification where text was amended ("as substituted vide …").
- Bundled sub-clauses become separate rows.

## 2. RBI regulated-entity taxonomy (verified)

On 28 November 2025 RBI issued about 244 consolidated directions, organised by category of regulated entity (SCC Online summary, 2 Dec 2025). The categories and counts were:

| Category | Directions |
|---|---|
| Commercial Banks | 31 |
| Small Finance Banks | 31 |
| UCBs | 27 |
| Rural Co-operative Banks | 26 |
| Local Area Banks | 26 |
| NBFCs | 30 |
| RRBs | 23 |
| AIFIs | 19 |
| Payments Banks | 18 |
| ARCs | 4 |
| Credit Information Companies | 2 |
| HFCs | 1 |
| CICs | 1 |
| MGCs | 1 |
| SPDs | 1 |
| NOFHCs | 1 |

**NBFC titles.** These follow the pattern "Reserve Bank of India (Non-Banking Financial Companies – <topic>) Directions, 2025". The topics include:

- Registration, Exemptions and Framework for Scale Based Regulation
- Governance
- Prudential Norms on Capital Adequacy
- Income Recognition, Asset Classification and Provisioning (IRACP)
- Asset Liability Management
- Concentration Risk Management
- Credit Risk Management
- Credit Facilities
- Responsible Business Conduct
- Know Your Customer
- Credit Information Reporting
- Managing Risks in Outsourcing
- Securitisation Transactions
- Transfer and Distribution of Credit Risk
- Resolution of Stressed Assets
- Treatment of Wilful Defaulters and Large Defaulters
- Financial Statements: Presentation and Disclosures
- Prudential Norms on Declaration of Dividends
- Classification, Valuation and Operation of Investment Portfolio
- Acceptance of Public Deposits
- Credit Cards
- Undertaking of Financial Services
- Branch Authorisation
- Voluntary Amalgamation
- Acquisition of Shareholding or Control
- Climate Finance and Management of Climate Change Risks
- Microfinance Institution
- P2P Lending Platform
- Account Aggregator
- Miscellaneous

**2026 supervisory directions for NBFCs.** On 31 July 2026 the Department of Supervision issued a further series. The first is RBI/DoS/2026-27/460, "Reserve Bank of India (Non-Banking Financial Companies – Compliance Function) Directions, 2026". It applies to NBFC-ML and NBFC-UL, including registrants under the Factoring Regulation Act, 2011, and Chapter V requires integrated, workflow-based compliance tools with a unified dashboard. Directions 461–468 cover:

- Cybersecurity/Technology Risk
- Digital Payment Security
- Fraud Risk Management
- Internal Audit
- Statutory Audit
- Supervisory Returns
- Miscellaneous Supervisory
- Auditor's Report

The titles and numbers of 461–468 are [VERIFY].

**NBFC types.** The types listed in the 2025 Financial Statements Directions, as applicable "for all layers, unless specified otherwise", are:

- NBFC-D
- NBFC-ICC
- NBFC-Factor
- NBFC-MFI
- NBFC-IFC
- IDF-NBFC
- HFC
- CIC
- SPD
- MGC
- NBFC-P2P
- NBFC-AA
- NOFHC
- NBFCs without public funds and without customer interface
- Base-layer NBFCs that have a customer interface but no public funds

The layers are Base, Middle, Upper and Top (the Top Layer is notionally empty) [VERIFY thresholds in the SBR Directions 2025].

**UCB tiers** come from the revised regulatory framework (Dec 2022):

- Tier 1: unit UCBs, salary-earners' UCBs, and other UCBs with deposits up to ₹100 crore
- Tier 2: deposits above ₹100 crore and up to ₹1,000 crore
- Tier 3: deposits above ₹1,000 crore and up to ₹10,000 crore
- Tier 4: deposits above ₹10,000 crore

These thresholds are [VERIFY against the 2025 UCB directions].

**Rural co-operative banks.** StCBs and DCCBs are regulated by RBI (under the BR Act as applicable to co-operative societies) and supervised by NABARD, with returns filed on NABARD's ENSURE portal [VERIFY].

## 3. Other regulators

- **SEBI CSCRF categories** (Aug 2024; categorisation clarified Apr/May 2025):
  - MIIs
  - Qualified REs
  - Mid-size REs
  - Small-size REs
  - Self-certification REs
  - Exempt: stock brokers with fewer than 1,000 clients and turnover below ₹1,000 crore, and IAs/RAs registered only in those roles
- **IRDAI intermediaries:**
  - Brokers (direct life, general or both; reinsurance; composite), under IRDAI (Insurance Brokers) Regulations 2018
  - Corporate agents, under the Corporate Agents Regulations 2015
  - IMFs
  - Web aggregators
  - POSPs
  - TPAs, under the TPA (Health Services) Regulations 2016
  - Surveyors and loss assessors, under the 2015 regulations
  - CSCs
  - Insurance repositories

  The Sabka Bima Sabki Raksha (Amendment of Insurance Laws) Act, 2025 extends the definition of intermediary to MGAs and insurance repositories and makes s.42D registration perpetual, subject to an annual fee (CAM blog, Jan 2026). IRDAI consolidated its regulations in 2024 (EOM Regulations 2024 and others) [VERIFY current titles].
- **DPDP Rules 2025** were notified as G.S.R. 846(E) on 13 Nov 2025:
  - Rules 1, 2 and 17–21 commenced on notification
  - Rule 4 (Consent Managers) commences on 13 Nov 2026
  - Rules 3, 5–16, 22 and 23 commence on 13 May 2027
  - Breach detail report: 72 hours (Rule 7)
  - Retention of logs: at least one year (Rule 8(3))
- **Labour Codes:** all four codes took effect on 21 November 2025 (MoLE notification, as reported by DLA Piper, KPMG, Grant Thornton and HSF Kramer). Central and State rules are being notified in stages [VERIFY by State].
- **IFSCA FC/FU and FME vocabulary** is taken from the owner's own finished sheets:
  - FC Regs 2021 reg. 5(1)(ii) core activities and 5(1)(iii) non-core activities
  - FM Regs 2025 reg. 3(4) categories: Authorised FME, Registered FME (Non-Retail), Registered FME (Retail)
  - Schemes: Venture Capital, Restricted, Retail, ETF, Family Investment Fund, PMS, Special Situation Fund, Investment Trusts

## 4. Design consequences

1. The importer accepts "; " as the canonical delimiter in Column D. It also accepts " | ", "," and line breaks, and normalises all of them to "; ".
2. Validations keep `showErrorMessage = False` to match the owner's behaviour. The importer, not Excel, enforces the vocabularies.
3. The base vocabulary is the same for all families: 9 departments, 6 compliance types, 3 risk levels and 11 frequencies. Families add values but never remove or rename base values, so the user experience stays uniform.
4. A Column P "Due:" convention captures structured due-date rules without adding columns.
5. IFSCA-GEN is a byte-exact replica of the Appointed Actuary `Rough` and its names.

## Sources

- SCC Online, "RBI's Comprehensive Framework of 244 Directions", 2 Dec 2025 — https://www.scconline.com/blog/post/2025/12/02/rbi-issues-directions-and-notifications-2025/
- Indian Cooperative, "RBI issues Master directions; 27 for UCBs, 26 for Rural Co-op Banks" — https://www.indiancooperative.com/co-op-news-snippets/rbi-issues-master-directions-27-for-ucbs-26-for-rural-co-op-banks/
- RBI, Master Direction RBI/DoS/2026-27/460 (31 Jul 2026) — https://rbi.org.in/ScriptS/BS_ViewMasDirections.aspx?id=13593
- TaxGuru summary of NBFC Financial Statements Directions 2025 — https://taxguru.in/?p=1015101
- YourStory, SEBI CSCRF categorisation (May 2025) — https://yourstory.com/2025/05/sebi-categorises-entities-size-risk-level-basis-cybersecurity
- Cyril Amarchand Mangaldas blog, insurance distribution guide (Jan 2026) — https://corporate.cyrilamarchandblogs.com/2026/01/understanding-insurance-distribution-in-india-a-comprehensive-guide/
- S.S. Rana, DPDP Rules 2025 — https://ssrana.in/articles/meity-notifies-final-digital-personal-data-protection-rules-2025/
- DLA Piper, Labour Codes notified — https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2025/government-of-india-notifies-the-labour-codes-ushers-a-new-era-of-compliances
- KPMG Flash News — https://www.in.kpmg.com/taxflashnews/KPMG-Flash-News-GOI-notifies-implementation-of-Labour-Codes.pdf
