# -*- coding: utf-8 -*-
"""Generate part2_prompts/NN_<FAMILY>_Command.md from family_vocab + hand-written guidance."""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from family_vocab import FAMILIES, FREQ_BASE, DEPT_BASE, COMP_BASE  # noqa
from final_instruments import FINAL_INSTR  # noqa  (review R2)

G = {}

G['RBI-SCB'] = dict(
    c_use='Column C holds the bank category, matching RBI\'s regulated-entity categories in the 28 November 2025 consolidated directions. Commercial Banks, SFBs, PBs, LABs and RRBs each have their own set of topic directions. Write one sheet per direction per category. Where the same topic direction exists for several categories and the text is the same, you may write one sheet with several C values ("Commercial Bank; Small Finance Bank (SFB)"). Do this only after checking that the paragraphs are identical.',
    d_use='Column D refines the bank type or adds an overlay that changes applicability: PSB vs private, foreign bank in branch mode vs WOS, D-SIB, listed bank, bank under PCA. Use "All Banks (ALL)" when the paragraph applies regardless of type.',
    logic=['Decide the category from the licence: banking company (commercial), SFB, PB, LAB or RRB.',
           'PSB-specific provisions mostly come from the Bank Nationalisation Acts / SBI Act and DFS guidelines, not RBI directions. Use D = "Public Sector Bank (PSB)" and cite the statute.',
           'Foreign banks in branch mode are exempt from several Companies Act-linked governance provisions. Record the exemption in Column S.',
           'D-SIB surcharges and other systemic requirements apply only to banks notified as D-SIBs. Name the list date in Column S.',
           'RRBs file with NABARD (ENSURE) for several returns. Check the return owner in the supervisory-returns direction.'],
    instr=['Banking Regulation Act, 1949 (ss. 10A, 10B, 11, 12, 17, 18, 24, 26A, 29, 35A, 35B, 36AA, 45Y)', 'RBI Act, 1934 (s.42 CRR, s.45-ID onwards as applicable)',
           'RBI (Commercial Banks – Governance / Capital Adequacy / IRACP / KYC / Credit Information Reporting / Managing Risks in Outsourcing / Responsible Business Conduct / Interest Rate on Deposits / Credit Facilities / ...) Directions, 2025 (31 topics) [VERIFY topic list]',
           'Corresponding SFB (31), PB (18), LAB (26) and RRB (23) direction sets of 28 Nov 2025',
           'RBI IT Governance, Risk, Controls and Assurance Practices directions; Cyber Security Framework for banks [VERIFY consolidation]',
           'RBI supervisory returns directions and the list of returns on rbi.org.in (Reporting Platform: CIMS, DAKSH, PRAVAAH)',
           'Deposit Insurance and Credit Guarantee Corporation Act, 1961 (premium, disclosure)'],
    pitfalls=['Mixing Basel III capital rows for commercial banks with SFB rows. SFB minimum capital and CRAR rules differ.',
              'Using repealed master circular paragraph numbers after the 2025 consolidation.',
              'Treating guidance in RBI FAQs as binding rows. Put it in Column L unless it states an obligation.'])

G['RBI-UCB'] = dict(
    c_use='Column C holds the UCB tier under the revised regulatory framework: Tier 1 to Tier 4 by deposit size, with unit and salary-earners\' UCBs in Tier 1. Many prudential provisions (CRAR, exposure limits, director qualifications, branch expansion) differ by tier. Write separate rows per tier.',
    d_use='Column D records the structural type (unit, multi-district, multi-State under the MSCS Act), scheduled status, FSWM status, and supervisory overlays (SAF, s.35A All-Inclusive Directions). These change permissions, so use them.',
    logic=['Tier is decided by deposits as on 31 March of the previous year [VERIFY tier thresholds in the 2025 UCB directions]. Write a one-time row for tier determination and an annual row for re-determination.',
           'Matters under the Banking Regulation Act (Part V, s.56) are RBI\'s. Elections, registration and bye-laws stay with the State Act or the MSCS Act. Those rows go to COOP-GEN / COOP-CCS sheets, not here.',
           'Board of Management (BoM) requirements apply to UCBs above the deposit threshold set by RBI [VERIFY].',
           'FSWM status unlocks permissions such as new branches and certain products. Record the FSWM criteria in Column S.'],
    instr=['Banking Regulation Act, 1949 (as applicable to co-operative societies; BR (Amendment) Act, 2020)', 'RBI (Urban Co-operative Banks – <topic>) Directions, 2025 (27 topics) [VERIFY topic list]',
           'Supervisory Action Framework for UCBs [VERIFY consolidation]', 'Umbrella Organisation (NUCFDC) framework [VERIFY]', 'RBI (Urban Co-operative Banks – Supervisory Returns) Directions, 2026 (RBI/DoS/2026-27/442, 31 Jul 2026) [VERIFY number]', 'DICGC Act, 1961'],
    pitfalls=['Applying commercial-bank Basel III rows to UCBs. UCBs follow their own capital framework.',
              'Writing State co-operative law obligations (AGM, elections) in a UCB RBI sheet. Use the COOP families instead.',
              'Forgetting Tier-specific CRAR minimums and director-qualification rules.'])

G['RBI-RCB'] = dict(
    c_use='Column C distinguishes State Co-operative Banks from District Central Co-operative Banks.',
    d_use='Column D adds scheduled status and supervisory overlays.',
    logic=['RBI regulates rural co-operative banks under the BR Act. NABARD supervises them and receives most returns (ENSURE portal) [VERIFY current portal per return].',
           'PACS are not banks. Put PACS obligations in COOP-CCS.',
           'Where a direction says "StCBs and DCCBs", use C = "All Rural Co-operative Banks".'],
    instr=['Banking Regulation Act, 1949 (Part V)', 'RBI (Rural Co-operative Banks – <topic>) Directions, 2025 (26 topics) [VERIFY topic list]', 'NABARD supervisory circulars and returns [VERIFY]'],
    pitfalls=['Citing UCB directions for RCBs. The 2025 sets are separate.', 'Missing the NABARD filing route in Column P.'])

G['RBI-NBFC'] = dict(
    c_use='Column C holds the Scale Based Regulation layer: Base, Middle, Upper or Top. Many governance and prudential provisions apply only from the Middle Layer upwards (for example the Compliance Function Directions, 2026 apply to ML and UL) or only to the Upper Layer (for example CET1 and the listing requirement). Use "All Layers" only where the paragraph does not distinguish.',
    d_use='Column D holds the NBFC type: ICC, MFI, Factor, IFC, IDF, HFC, CIC, MGC, SPD, P2P, AA, NOFHC, NBFC-D, government NBFC, the two no-public-funds categories, and Factoring Act registrants. Several types have their own directions (HFC, CIC, MGC, NOFHC, SPD, MFI, P2P, AA). For those, write the sheet under the type-specific direction and set Column D precisely.',
    logic=['The layer is set by asset size and the RBI Upper Layer list [VERIFY thresholds in the SBR Directions 2025]. Some types are always Base Layer (P2P, AA, NOFHC, and NBFCs without public funds and customer interface). Some are never Base Layer (deposit-taking NBFCs, HFCs above the threshold). Write applicability rows for layer determination.',
           'Each topic direction repeats a "Applicability" chapter. Read it first and set C/D from it, not from memory.',
           'Government-owned NBFCs have specific carve-outs (for example on some governance provisions). Record them in Column S.',
           'The 31 July 2026 DoS directions (460–468) add supervisory obligations: compliance function, cyber/tech risk, digital payment security, fraud risk, internal audit, statutory audit, supervisory returns, miscellaneous supervisory, auditor\'s report. Write each as its own sheet.',
           'NBFC-ICC investment activity (equities, AIF units, REIT/InvIT units, IPO subscriptions) is governed by the Investment Portfolio Direction, the Concentration Risk Direction and the RBI instructions on investments in AIFs [VERIFY current text]. Write these rows with D = "NBFC-Investment and Credit Company (NBFC-ICC)".'],
    instr=['RBI Act, 1934 Chapter III-B (ss. 45-IA, 45-IB, 45-IC, 45-IE, 45-JA, 45-L, 45-MA, 58B, 58G)',
           'RBI (Non-Banking Financial Companies – <topic>) Directions, 2025: the 30 topics listed in the template\'s _Template_Info',
           'RBI (Housing Finance Companies) Directions, 2025; (Core Investment Companies) Directions, 2025; (Mortgage Guarantee Companies); (NOFHC); (Standalone Primary Dealers)',
           'RBI (NBFC – Compliance Function) Directions, 2026 (RBI/DoS/2026-27/460, 31 Jul 2026) and DoS directions 461–468 [VERIFY titles and numbers]',
           'RBI Integrated Ombudsman Scheme and Internal Ombudsman directions [VERIFY current versions]',
           'Factoring Regulation Act, 2011 (registered factors); SARFAESI Act, 2002 (notified NBFCs)'],
    pitfalls=['Using pre-2025 Master Direction paragraph numbers (e.g., the 2023 SBR Master Direction).',
              'Writing ML/UL-only rows with C = "All Layers".',
              'Splitting too little. The Governance and Compliance Function directions contain long lists of Board and committee functions, and each element is its own row.',
              'Missing glide-path dates for NOF and other phased requirements.'])

G['RBI-ARC'] = dict(
    c_use='Column C separates obligations of the ARC as a company from obligations at the trust/scheme level (SR issuance, trust accounts, NAV declaration, QB disclosures).',
    d_use='Column D adds activity overlays: resolution applicant under IBC, trustee/manager role, sponsor and FDI structures, listed SRs.',
    logic=['SARFAESI Act ss.3–12 and the RBI ARC directions are the core. Measures under ss.13–15 belong to recovery workflows but carry compliance rows (notice formats, valuation, sale procedure) [INTERP].',
           'Additional permitted activities depend on the NOF threshold [VERIFY]. Write the threshold in Column S.',
           'SR investment by the transferor bank and provisioning on SRs are bank-side obligations. Put them in RBI-SCB, not here.'],
    instr=['SARFAESI Act, 2002 (Chapter II)', 'RBI (Asset Reconstruction Companies – <topic>) Directions, 2025 (4 topics incl. KYC, Credit Information Reporting) [VERIFY]',
           'Security Interest (Enforcement) Rules, 2002', 'RBI (Asset Reconstruction Companies – Supervisory Returns) Directions, 2026 (RBI/DoS/2026-27/469, 31 Jul 2026) [VERIFY number]', 'IBC, 2016 and IBBI regulations (where the ARC acts as resolution applicant)'],
    pitfalls=['Ignoring trust-level obligations (separate books per trust, NAV).', 'Using the old ₹100 crore NOF figure. RBI has raised it; read the current text [VERIFY].'])

G['RBI-OTH'] = dict(
    c_use='Column C holds the category of RBI regulated entity outside banks, NBFCs and ARCs: AIFIs, Credit Information Companies, payment system operators and participants, and FEMA authorised persons.',
    d_use='Column D names the entity: EXIM, NABARD, NHB, SIDBI, NaBFID; the four CICs; PA, PA-P, PA-CB, PPI issuers, BBPOUs, TReDS, WLAOs, card networks; MTSS agents; AD-II, FFMC.',
    logic=['PSS Act s.4 authorisation and conditions are the base rows for payment entities. Directions on PAs (2025) and PPIs carry net worth, escrow and governance rows [VERIFY current titles].',
           'CIC obligations come from CICRA 2005, the CIC Rules/Regulations 2006 and the RBI CIC directions. Lender-side credit-reporting obligations belong in the lender family.',
           'AIFIs have 19 topic directions (28 Nov 2025). Treat them like bank directions with C = AIFI.'],
    instr=['Payment and Settlement Systems Act, 2007 and Regulations, 2008', 'Credit Information Companies (Regulation) Act, 2005; CIC Rules and Regulations, 2006',
           'RBI (All India Financial Institutions – <topic>) Directions, 2025', 'FEMA, 1999 and RBI master directions for authorised persons [VERIFY]'],
    pitfalls=['Writing lender-side CIC reporting rows here. They belong in the lender families.', 'Missing card-network and PA-CB cross-border rows.'])

G['COOP-CCS'] = dict(
    c_use='Column C records the registration law, which decides the regulator: multi-State societies under the MSCS Act 2002 (Central Registrar), State societies under the State Act (State Registrar), mutually aided co-operatives under State MACS Acts, and PACS (State Act, with Ministry of Cooperation model bye-laws).',
    d_use='Column D records the society type: urban/nagari credit society (patsanstha), employees\' or salary-earners\' credit society, thrift and credit society, PACS, LAMPS, FSS, women\'s credit society, and societies above the concurrent-audit threshold.',
    logic=['First decide the governing statute. A society operating in more than one State is a multi-State society under the MSCS Act. Otherwise the State Act of the registration State applies. Write one sheet per Act and per State. State Acts differ (for example Maharashtra 1960, Uttar Pradesh 1965, Rajasthan 2001, Gujarat 1961, Karnataka 1959, Delhi 2003).',
           'Credit societies may accept deposits only from members and may not use the words "bank", "banker" or "banking" (BR Act s.7) [VERIFY State-specific deposit rules].',
           'The 2023 MSCS amendments introduced the Co-operative Election Authority, the Co-operative Ombudsman, the Co-operative Rehabilitation, Reconstruction and Development Fund, board composition requirements (seats for women and SC/ST), concurrent audit above a turnover/deposit threshold, and information-officer duties. Write each as its own rows [VERIFY section numbers].',
           'Loan operations (sanction, interest, recovery) are run in Finbyx. Write the regulatory obligations here (lending limits, member-only lending, recovery under the Act, audit classification).'],
    instr=['Multi-State Co-operative Societies Act, 2002 (as amended by Act 11 of 2023) and MSCS Rules, 2002 (as amended 2023) [VERIFY]', 'State Co-operative Societies Acts and Rules (select State)',
           'Model bye-laws for PACS (Ministry of Cooperation) [VERIFY]', 'Banking Regulation Act, 1949 s.7 and s.56 (prohibition on "bank")', 'PMLA, 2002 (where the society is a reporting entity) [VERIFY]', 'Income-tax Act, 2025 provisions on co-operative societies [VERIFY]'],
    pitfalls=['Writing RBI UCB rules for a credit society. A credit society is not a bank.', 'Mixing two States\' Acts in one sheet.', 'Missing election-cycle rows (board term of five years, election before expiry).'])

G['COOP-GEN'] = dict(
    c_use='Column C records the registration law (MSCS Act, State Act, MACS Act, federal/apex society, or Societies Registration Act 1860 for non-co-operative societies).',
    d_use='Column D records the society type: housing, consumer, dairy, marketing, sugar/agro-processing, fisheries, weavers/industrial, labour, multipurpose, transport, health, tourism, national MSCS (seeds/organic/exports), federations, SRA educational or charitable societies.',
    logic=['Governance rows (general body, board, elections, audit, annual return, registers, bye-law amendments) are common to all types. Sector rows (for example housing-society maintenance and transfer rules under State housing bye-laws, dairy FSSAI licensing) are written as separate sheets.',
           'SRA 1860 societies follow the central Act as amended by their State. Annual list of governing body members filing applies [VERIFY State].'],
    instr=['MSCS Act, 2002 and Rules', 'State Co-operative Societies Acts and Rules', 'Societies Registration Act, 1860 and State amendments', 'State model bye-laws for housing societies [VERIFY]'],
    pitfalls=['Writing credit-society deposit rules for non-credit societies.', 'Treating SRA societies as co-operatives. Use the SRA value in Column C.'])

G['IFSCA-GEN'] = dict(
    c_use='Column C holds the IFSCA sector, exactly as in the owner\'s existing IFSCA sheets (Banking, Finance Company, Fund Management, Capital Markets, Insurance, Bullion, Payments, FinTech, Ancillary Services, GIC, Education, Trade Finance, Cross-cutting).',
    d_use='Column D holds the IFSCA entity type from the owner\'s 40-entry list, for example "IFSC Banking Unit (IBU)" or "Recognised Stock Exchange (RSEX); Recognised Clearing Corporation (RCCP); Recognised Depository (RDEP)".',
    logic=['This template is a byte-exact replica of the owner\'s IFSCA vocabulary, so existing IFSCA sheets remain valid. Continue the established method: one sheet per regulation, handbook, guideline or circular, with the depth of the existing sheets (11–389 rows; mean about 65).',
           'Use IFSCA-FCFU or IFSCA-FME instead when a finer activity or scheme classification is needed.',
           'The org egress allowlist blocks ifsca.gov.in from the automation shell. Download source PDFs on the Mac and attach them.'],
    instr=['IFSCA Act, 2019', 'IFSCA (Banking) Regulations, 2020 and Banking Handbook GEN/COB/PRU', 'IFSCA (Capital Market Intermediaries) Regulations, 2025; MII Regulations, 2021; Listing Regulations, 2024; KRA Regulations, 2025; Prohibition of Market Abuse Regulations, 2026',
           'IFSCA insurance regulations (Registration of Insurance Business 2021; Insurance Intermediary 2021; MGA 2026; Re-insurance 2023; solvency, investment and actuarial regulations)', 'IFSCA (AML, CFT and KYC) Guidelines, 2022 — master as on 3 Aug 2026',
           'IFSCA (Payment Services) Regulations, 2024; Payment and Settlement Systems Regulations, 2024; Bullion Market Regulations, 2025; TechFin and Ancillary Services Regulations, 2025 (amended 12 May 2026); BATF Regulations, 2024 (amended 8 Jan 2026); GIC Regulations, 2025; IBC & OEC Regulations, 2022'],
    pitfalls=['Using the old "IFSCA Format for Question Final" vocabulary (it has typos and no named ranges).', 'Missing the consolidated "as amended up to" text for FM, Insurance Registration and TechFin.'])

G['IFSCA-FCFU'] = dict(
    c_use='Column C says whether the row applies to a Finance Company, a Finance Unit (branch/unit of a foreign or Indian entity), or both.',
    d_use='Column D holds the activity or registration: GRCTC; core activities under reg. 5(1)(ii) (lending/credit enhancement/securitisation/financial lease; factoring and forfaiting; investments; derivatives); non-core activities under reg. 5(1)(iii) (merchant banking, advisory/PMS, distribution, trading/clearing membership, RTA/trusteeship); aircraft and ship lessors; ITFS operators.',
    logic=['Prudential rows (capital ratio, LCR, exposure ceiling) apply to FCs/FUs undertaking core activities. GRCTCs follow their own framework.', 'Each non-core activity needs its own registration under the relevant framework. Write the registration row with that activity in Column D.'],
    instr=['IFSCA (Finance Company) Regulations, 2021 (as amended)', 'Guidelines on Corporate Governance & Disclosure Requirements for FCs (updated 4 Apr 2025)', 'IFSCA (Registration of Factors & Assignment of Receivables) Regulations, 2024', 'Frameworks for GRCTC, aircraft lease, ship lease and ITFS [VERIFY current versions]', 'Liquidity Risk Management Guidelines for FC/FU (24 Jun 2021)'],
    pitfalls=['Treating a Finance Unit as a separate legal entity. It is not, so its parent\'s obligations and home-regulator NOC rows matter.'])

G['IFSCA-FME'] = dict(
    c_use='Column C holds the FME registration category under reg. 3(4) of the FM Regulations 2025: Authorised FME, Registered FME (Non-Retail), Registered FME (Retail). Higher categories may undertake activities of lower ones.',
    d_use='Column D holds the scheme or activity: Venture Capital Scheme, Restricted Scheme, Retail Scheme, ETF, Family Investment Fund, PMS (incl. multi-family office), Special Situation Fund, FoF/feeder, Investment Trusts (REIT/InvIT, private or public), co-investment/SPV, Pension Fund.',
    logic=['Obligations of the FME (net worth, KMP, infrastructure) and of each scheme (placement memorandum, investors, valuation, NAV, disclosures) must be separated. Use D = "Fund Management Entity (FME)" for entity-level rows.', 'Use the "as amended up to 10 September 2026" consolidated text.'],
    instr=['IFSCA (Fund Management) Regulations, 2025 (as amended up to 10 Sep 2026)', 'IFSCA Guidelines on KMP Eligibility (25 Jul 2025)', 'IFSCA (Pension Fund) Regulations, 2026', 'IFSCA (AML, CFT and KYC) Guidelines, 2022'],
    pitfalls=['Applying retail-scheme investor protections to restricted schemes.', 'Missing the USD 1 billion AUM trigger for additional KMP.'])

G['SEBI-MF'] = dict(
    c_use='Column C holds the role that bears the obligation: AMC, trustees, sponsor, the scheme, or all MF entities.',
    d_use='Column D holds the scheme category per SEBI\'s categorisation (equity, debt, hybrid, solution-oriented, index/ETF, FoF, close-ended/interval), plus newer frameworks (Specialised Investment Funds, MF Lite) [VERIFY current status].',
    logic=['Trustee obligations (reg. 18) and AMC obligations (reg. 25) are separate rows, even where they mirror each other.', 'The SEBI Master Circular for Mutual Funds carries most operational requirements. Cite its paragraph numbers and date.', 'CSCRF obligations for AMCs and RTAs belong in the CYBER family unless SEBI writes them into an MF circular.'],
    instr=['SEBI (Mutual Funds) Regulations, 2026 (notified 14 Jan 2026; in force 1 Apr 2026; replaced the 1996 Regulations) — do not cite 1996 regulation numbers for obligations from 1 Apr 2026', 'SEBI Master Circular for Mutual Funds [VERIFY latest date]', 'SEBI (PIT) Regulations, 2015 (code of conduct for AMC staff)', 'AMFI code and best-practice guidelines (Suggestive Compliance)'],
    pitfalls=['Citing superseded individual circulars that are now part of the master circular.', 'Treating AMFI guidelines as binding unless SEBI mandates them.'])

G['SEBI-AIF'] = dict(
    c_use='Column C holds the role: the AIF or scheme, the manager, the sponsor or the trustee.',
    d_use='Column D holds the AIF category and sub-category: Category I (VCF, angel, SME, social impact, infrastructure, special situation), Category II, Category III, LVF for accredited investors, accredited-investor-only schemes, co-investment schemes [VERIFY].',
    logic=['Many conditions differ by category (leverage, concentration, tenure, continuing interest of the sponsor/manager). Write separate rows per category.', 'PPM audit, valuation, performance benchmarking and dematerialisation of units are master-circular obligations. Cite the master circular paragraph.'],
    instr=['SEBI (Alternative Investment Funds) Regulations, 2012', 'SEBI Master Circular for AIFs [VERIFY latest date]', 'SEBI CSCRF (AIF managers by AUM category)'],
    pitfalls=['Writing Category III leverage rules for Category I/II.', 'Missing accredited-investor and LVF relaxations.'])

G['SEBI-LISTED'] = dict(
    c_use='Column C holds the listing segment: main board specified securities, SME platform, non-convertible securities (debt-listed), HVDLE, both equity and debt, Social Stock Exchange, listed CP.',
    d_use='Column D holds overlays that change applicability: top 100/500/1000/2000 by market capitalisation, material subsidiary, SR equity, PSU, sectoral regulated entity, newly listed, entity under CIRP.',
    logic=['LODR Chapter IV (specified securities) and Chapter V (non-convertible securities) differ. Write separate rows with the correct C.', 'Reg. 15(2) exempts SME-listed and small entities from regs. 17–27 and other provisions. Record this in Column S [VERIFY current thresholds].', 'Market-cap rankings are taken as on 31 December (or the date SEBI specifies) [VERIFY]. Write the ranking test in Column S.'],
    instr=['SEBI (LODR) Regulations, 2015', 'SEBI Master Circulars on compliance with LODR (specified securities; NCS) [VERIFY dates]', 'SEBI (PIT) Regulations, 2015', 'SEBI (SAST) Regulations, 2011', 'SEBI (ICDR) Regulations, 2018 (continuing obligations)', 'BRSR / BRSR Core (Annexure to LODR circulars)', 'Companies Act, 2013 provisions applicable to listed companies (ss. 149(4), 177, 178, 204)'],
    pitfalls=['Ignoring the SOP fine schedule for each regulation in Column Q.', 'Writing equity-only rows for debt-listed entities.'])

G['SEBI-REIT-INVIT'] = dict(
    c_use='Column C holds the trust type: REIT, SM REIT, public InvIT, private listed or unlisted InvIT.',
    d_use='Column D holds the party that bears the obligation: trust, manager/investment manager, trustee, sponsor, project manager, valuer, holdco/SPV.',
    logic=['Governance obligations of the manager (board composition, committees, related-party transactions) mirror LODR. Cite the REIT/InvIT regulation, not LODR.', 'Distribution and leverage limits are percentage tests. Put the number in the question.'],
    instr=['SEBI (REIT) Regulations, 2014 (incl. SM REIT provisions)', 'SEBI (InvIT) Regulations, 2014', 'SEBI master circulars for REITs and InvITs [VERIFY dates]'],
    pitfalls=['Mixing REIT and InvIT leverage thresholds.'])

G['SEBI-INT'] = dict(
    c_use='Column C holds the intermediary group (trading and clearing, depository, advisory and research, issue management and registry, portfolio and fund services, rating/trusteeship/custody, data and index services).',
    d_use='Column D names the intermediary type and, for cyber rows, the CSCRF category (Qualified, Mid-size, Small-size, Self-certification).',
    logic=['Each intermediary has its own activity regulations and master circular. Write one sheet per regulation.', 'CSCRF rows should go in CYBER unless the obligation is intermediary-specific. If they go here, use the CSCRF category values in Column D.', 'IA/RA administration and supervision is delegated to BASL. Record the BASL filing route in Column P.'],
    instr=['SEBI Act, 1992; SEBI (Intermediaries) Regulations, 2008', 'Activity regulations: Stock Brokers, Depositories and Participants 2018, Investment Advisers 2013, Research Analysts 2014, Portfolio Managers 2020, Merchant Bankers, RTA, Debenture Trustees 1993, CRA 1999, Custodian 1996, KRA 2011 [VERIFY titles/years after 2024–26 rewrites]', 'SEBI CSCRF (20 Aug 2024) and clarifications'],
    pitfalls=['Using pre-2025 stock broker or merchant banker regulation references where SEBI has issued replacement regulations [VERIFY].'])

G['IRDAI-INS'] = dict(
    c_use='Column C holds the insurer class: life, general, standalone health, Indian reinsurer, FRB, Lloyd\'s India, composite/multi-line [VERIFY after the 2025 amendment].',
    d_use='Column D holds overlays: public or private, listed, specialised insurer, bancassurance partner, ULIP, health products.',
    logic=['IRDAI moved to principle-based regulations in 2024 with master circulars. Cite both the regulation and the master circular paragraph.', 'Check the Sabka Bima Sabki Raksha (Amendment of Insurance Laws) Act, 2025 for commencement of changed sections before citing amended section numbers [VERIFY].'],
    instr=['Insurance Act, 1938 (as amended 2025)', 'IRDA Act, 1999', 'IRDAI regulations 2024 (Corporate Governance; Protection of Policyholders\' Interests; Actuarial, Finance and Investment Functions; Expenses of Management incl. Commission; Registration, Capital Structure, Transfer of Shares and Amalgamation; Insurance Products; Rural, Social Sector and Motor Third Party Obligations) [VERIFY exact titles]', 'IRDAI Information and Cyber Security Guidelines, 2023'],
    pitfalls=['Citing repealed 2016/2017 regulations after the 2024 consolidation.', 'Missing master-circular paragraph numbers.'])

G['IRDAI-INT'] = dict(
    c_use='Column C holds the intermediary class (broker, corporate agent, IMF, web aggregator, TPA, surveyor, CSC/POSP channel, MGA, insurance repository).',
    d_use='Column D refines it (direct life/general/composite broker, reinsurance broker, corporate agent by line, bank or NBFC as corporate agent, individual or corporate surveyor).',
    logic=['After the 2025 amendment, s.42D registration is perpetual subject to annual fee and conditions. Write an annual fee row and continuing-condition rows.', 'Banks and NBFCs acting as corporate agents also follow RBI rules on third-party product distribution (Undertaking of Financial Services Direction for NBFCs). Note this in Column S and write the RBI rows in the RBI family.'],
    instr=['Insurance Act, 1938 s.42D (as amended 2025)', 'IRDAI (Insurance Brokers) Regulations, 2018', 'IRDAI (Registration of Corporate Agents) Regulations, 2015', 'IRDAI (TPA – Health Services) Regulations, 2016', 'IRDAI (Insurance Surveyors and Loss Assessors) Regulations, 2015', 'IRDAI (Expenses of Management, incl. Commission) Regulations, 2024', 'Consolidated intermediary regulations and master circulars of 2024–26 [VERIFY]'],
    pitfalls=['Treating individual agents as intermediaries in this family. They are appointed by insurers.'])

G['MCA-CO'] = dict(
    c_use='Column C holds the company class. Many provisions differ for private, OPC, small, Section 8, producer, Nidhi and government companies through exemption notifications (for example the 5 June 2015 notifications for private and government companies). Use the class value and record the exemption in Column S.',
    d_use='Column D holds thresholds and overlays that switch obligations on: paid-up capital, turnover and borrowing thresholds (s.149, s.177, s.178, s.203, s.204), CSR thresholds (s.135(1)), deposits, foreign investment, dormant status.',
    logic=['Write one sheet per Chapter or Rule set (Meetings of Board; Management and Administration; Accounts; Audit and Auditors; Appointment of Directors; Share Capital; Deposits; CSR; SBO), plus SS-1 and SS-2.', 'Every e-form filing is a Returns & Reporting row with "Due:" (for example AOC-4 within 30 days of the AGM; MGT-7 within 60 days of the AGM).', 'Registers (MBP-1, MBP-2, MBP-4, MGT-1, CHG-7, SH-6, BEN-3) are "Registers & Records" rows.'],
    instr=['Companies Act, 2013 and Rules', 'Exemption notifications for private, government, Section 8 and Nidhi companies (5 Jun 2015 and later) [VERIFY]', 'ICSI Secretarial Standards SS-1 and SS-2 [VERIFY latest revision date]', 'Companies (Auditor\'s Report) Order, 2020 (auditor-side; write company-side preparation rows only)'],
    pitfalls=['Missing the private-company exemptions in Column S.', 'Writing form numbers from MCA21 V2 that have changed in V3 [VERIFY].'])

G['MCA-LLP'] = dict(
    c_use='Column C holds the LLP class (LLP, small LLP, foreign LLP).',
    d_use='Column D holds thresholds and overlays (audit threshold, FDI, converted LLPs, body-corporate partners).',
    logic=['Annual filings: Form 11 (annual return, within 60 days of FY end) and Form 8 (statement of account and solvency, within 30 days of six months from FY end) [VERIFY].', 'Register of partners and SBO rules were added by the 2022–2024 amendments [VERIFY].'],
    instr=['LLP Act, 2008 (as amended 2021)', 'LLP Rules, 2009 (as amended)', 'FEMA (Non-debt Instruments) Rules, 2019 (LLPs with FDI)'],
    pitfalls=['Applying company Board-meeting rules to LLPs.'])

G['DATA-PRIV'] = dict(
    c_use='Column C holds the law or jurisdiction (DPDP Act and Rules; IT Act and SPDI Rules; EU GDPR; UK GDPR; CCPA/CPRA; sectoral data rules).',
    d_use='Column D holds the privacy role (Data Fiduciary, SDF, Data Processor, Consent Manager; GDPR controller/processor/joint controller/representative; CCPA business/service provider/contractor/third party; data broker).',
    logic=['DPDP obligations commence in phases: Rules 1, 2 and 17–21 from 13 Nov 2025; Rule 4 (Consent Managers) from 13 Nov 2026; Rules 3, 5–16, 22 and 23 from 13 May 2027. Put the commencement date in Column S of every row.', 'SDF obligations (DPO in India, independent data auditor, periodic DPIA and audit, algorithmic due diligence, data localisation of specified data) apply only on notification as an SDF. Use D = SDF.', 'Sectoral data rules (RBI, SEBI, IRDAI, IFSCA) override or add to DPDP. Write sectoral rows in the sectoral family and cross-reference them here.', 'GDPR and CCPA rows apply only where territorial scope tests are met (GDPR Art. 3; CCPA thresholds). Write the test in Column S.'],
    instr=['Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025 (G.S.R. 846(E))', 'IT Act, 2000 ss.43A, 72A and SPDI Rules, 2011 (until superseded)', 'GDPR (Regulation (EU) 2016/679)', 'CCPA/CPRA (Cal. Civ. Code §1798.100 et seq.) and CCPA Regulations (2025 rules on risk assessments, cybersecurity audits, ADMT) [VERIFY effective dates]'],
    pitfalls=['Stating DPDP obligations as already in force before 13 May 2027.', 'Using the SPDI Rules after they are superseded [VERIFY].'])

G['CYBER'] = dict(
    c_use='Column C holds the framework (CERT-In Directions, IT Act s.70/NCIIPC, RBI IT/cyber directions, SEBI CSCRF, IRDAI guidelines, IFSCA guidelines, DPDP Rule 6, ISO 27001, NIST CSF, PCI DSS).',
    d_use='Column D holds the entity category that changes the requirement (all body corporates, data centre/cloud/VPN providers, CII, bank, NBFC by layer, UCB by tier, SEBI CSCRF categories, insurer, IFSCA RE, payment entity).',
    logic=['Statutory rows (CERT-In, NCIIPC, DPDP) are Compliance. ISO, NIST and PCI rows are "Suggestive Compliance" unless a regulator or contract mandates them.', 'Write sector cyber directions here only where the owner wants a single cyber view. Otherwise put them in the sector family and cross-reference.', 'Log retention (180 days in India), NTP synchronisation, and incident reporting within 6 hours are key CERT-In rows.'],
    instr=['CERT-In Directions of 28 Apr 2022 and FAQs', 'IT Act, 2000 ss.43, 66, 70, 70A, 70B, 72A', 'SEBI CSCRF (20 Aug 2024)', 'IRDAI Information and Cyber Security Guidelines, 2023', 'RBI cyber directions for banks, UCBs and NBFCs (incl. the 2026 NBFC cyber/technology-risk direction) [VERIFY]', 'ISO/IEC 27001:2022; NIST CSF 2.0; PCI DSS v4.0.1'],
    pitfalls=['Making ISO controls mandatory rows.', 'Missing the 180-day log retention and NTP rows.'])

G['LAB-POSH'] = dict(
    c_use='Column C holds the law (each Labour Code, the POSH Act, State Shops and Establishments Act, State PT/LWF, Apprentices Act).',
    d_use='Column D holds the establishment type or headcount threshold that switches obligations on (10, 20, 50, 100, 300 employees; factory; shop; IT/ITES; contractor; inter-State migrants; gig/platform; BOCW; remote workforce).',
    logic=['All four Labour Codes took effect on 21 Nov 2025. Central and State rules are notified in stages, so check the State rule before writing State-specific registers and returns [VERIFY by State].', 'Registers and returns under the Codes are prescribed by rules, mostly in electronic form. Each register is a "Registers & Records" row.', 'POSH: IC constitution (s.4), annual report to the District Officer (s.21 read with r.14), display and awareness (s.19), Board report disclosure (Companies (Accounts) Rules r.8(5)(x)).'],
    instr=['Code on Wages, 2019; IR Code, 2020; Code on Social Security, 2020; OSH Code, 2020 and Central Rules', 'State rules under the Codes; State Shops and Establishments Acts', 'POSH Act, 2013 and POSH Rules, 2013', 'Professional Tax and Labour Welfare Fund Acts of the State'],
    pitfalls=['Citing repealed Acts (Payment of Wages Act, Factories Act, etc.) after 21 Nov 2025 except for transitional matters.', 'Missing State variation in thresholds.'])

G['TAX-GST'] = dict(
    c_use='Column C holds the tax law (GST Acts; Income-tax Act, 2025; Income-tax Act, 1961 for earlier years; TDS/TCS; State PT; stamp duty).',
    d_use='Column D holds the taxpayer type that changes obligations (regular, composition, ISD, GST TDS deductor, e-commerce operator, NRTP, OIDAR, financial institution with the rule 38 ITC option, SEZ, e-invoicing applicable, company, co-operative, LLP, tax-audit applicable).',
    logic=['The Income-tax Act, 2025 applies from tax year 2026-27 (1 Apr 2026). Earlier years stay under the 1961 Act. Section and form numbers changed, so cite the new numbers [VERIFY].', 'Banking companies, financial institutions and NBFCs may avail 50% ITC under rule 38 of the CGST Rules. Write this as a choice row.', 'GST return due dates are set by notification and may be staggered by State. Put the rule in Column P and mark [VERIFY] where a notification changes it.'],
    instr=['CGST Act, 2017; IGST Act, 2017; CGST Rules, 2017 (and GST rate rationalisation of Sep 2025) [VERIFY]', 'Income-tax Act, 2025 and Income-tax Rules [VERIFY form numbers]', 'State Professional Tax Acts'],
    pitfalls=['Using 1961 Act section numbers for FY 2026-27 obligations.'])



import difflib, re as _re
def _norm(s):
    return _re.sub(r'\[verify[^\]]*\]|[^a-z0-9 ]', ' ', s.lower()).split()
def merge_instr(a, b):
    """Curated list b (family guidance) first; add items of a only if no item already starts with the same instrument name."""
    def key(s):
        t = _norm(s)
        return ' '.join(t[:4])
    out = list(dict.fromkeys(b))
    keys = {key(x) for x in out}
    for x in a:
        if key(x) not in keys:
            out.append(x); keys.add(key(x))
    return out

def lst(xs):
    return '\n'.join(f'- {x}' for x in xs)


def main(out_dir):
    for i, f in enumerate(FAMILIES, 1):
        g = G[f['code']]
        tfile = f"LDC-TPL-{f['code']}-v1.0 - ..."
        extra_h = [x for x in f['H'] if x not in FREQ_BASE]
        extra_m = [x for x in f['M'] if x not in DEPT_BASE]
        extra_o = [x for x in f['O'] if x not in COMP_BASE]
        md = f"""# {i:02d} — {f['code']} Family Command: {f['name']}

**Template:** `templates/LDC-TPL-{f['code']}-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-{f['code']}-v1.0` · **Regulator / authority:** {f['regulator']} · **Named-range prefix:** `{f['prefix']}_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — {f['c_label'].replace(' (Column C)', '')}.** {g['c_use']}

**Column D — {f['d_label'].replace(' (Column D)', '')}.** {g['d_use']} Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C ({f['prefix']}_Sector):**
{lst(f['C'])}

**Column D ({f['prefix']}_Entity):**
{lst(f['D'])}

**Column H ({f['prefix']}_Freq):** {', '.join(f['H'])}.{' Family additions to the base list: ' + ', '.join(extra_h) + '.' if extra_h else ' (Base list only; this family is a byte-exact replica of the owner\'s IFSCA vocabulary.)'}

**Column M ({f['prefix']}_Dept):** {', '.join(f['M'])}.{' Family additions: ' + ', '.join(extra_m) + '.' if extra_m else ''}

**Column O ({f['prefix']}_CompType):** {', '.join(f['O'])}.{' Family additions: ' + ', '.join(extra_o) + '.' if extra_o else ''}

**Column R ({f['prefix']}_Risk):** High, Medium, Low.

**Column P reference list ({f['prefix']}_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
{lst(f['P'])}

## 3. Applicability logic for this family

{lst(g['logic'])}

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

{lst(FINAL_INSTR[f['code']])}

## 5. Family-specific pitfalls

{lst(g['pitfalls'])}

## 6. File naming

`{f['code']} - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
"""
        name = f"{out_dir}/{i:02d}_{f['code']}_Command.md"
        open(name, 'w').write(md)
        print(name)


if __name__ == '__main__':
    main(sys.argv[1])
