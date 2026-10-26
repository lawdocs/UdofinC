# -*- coding: utf-8 -*-
"""v1.1 (X1): build the ESG-BRSR (sustainability, BRSR/BRSR Core, CSR, GHG) question template without modifying the v1.0 scripts.

Usage: python3 v11_X1_build_esg.py <owner_base_xlsx (Appointed Actuary sheet)> <out_dir>
Reuses build() from build_templates.py and base vocabularies from family_vocab.py (NN-35: base values kept, family values only added).
"""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import build_templates as bt  # noqa: E402
from family_vocab import FREQ_EXT, DEPT_BASE, COMP_BASE, ex  # noqa: E402

bt.SHORT['ESG-BRSR'] = 'ESG BRSR and CSR'

ESG = dict(
    code='ESG-BRSR',
    name='ESG, Business Responsibility and Sustainability Reporting (BRSR / BRSR Core), CSR and GHG accounting',
    regulator='SEBI; MCA; stock exchanges; RBI (climate-related financial risk); voluntary standards bodies (ISSB, GHG Protocol, GRI); EU (CSRD/ESRS) for EU-facing groups',
    prefix='ESG',
    c_label='Framework / Instrument (Column C)',
    C=['SEBI LODR Reg 34(2)(f) - BRSR',
       'SEBI BRSR Core and Assurance',
       'SEBI BRSR Value Chain Disclosures',
       'SEBI ESG Rating Providers and ESG Debt / ESG Schemes',
       'Companies Act 2013 s.135 and CSR Rules 2014',
       'Companies Act 2013 Board Report (s.134) sustainability items',
       'RBI Climate-related Financial Risk',
       'GHG Protocol (Scope 1, 2 and 3)',
       'ISSB IFRS S1 and S2',
       'EU CSRD / ESRS (EU-facing groups)',
       'Board-approved internal ESG / Sustainability Policy',
       'All Frameworks'],
    d_label='Entity Category (Column D)',
    D=['Listed entity - Top 1000 by market capitalisation',
       'Listed entity - Top 250 (value-chain scope)',
       'Listed entity - other (voluntary BRSR)',
       'Company meeting s.135 CSR thresholds',
       'Company with CSR obligation below Rs 50 lakh (no CSR Committee required)',
       'Regulated Entity - Bank / NBFC / UCB (RBI climate risk)',
       'Asset Management Company / ESG scheme',
       'Issuer of green / ESG debt securities',
       'Unlisted company - voluntary sustainability reporting',
       'Group with EU operations (CSRD scope)',
       'All Entities (ALL)'],
    H=FREQ_EXT,
    M=DEPT_BASE + ['Secretarial', 'Investor Relations', 'Administration & Facilities', 'Internal Audit'],
    O=COMP_BASE + ['Disclosures'],
    P=['Stock exchange (BRSR as part of Annual Report)', 'MCA (CSR-2 / AOC-4)', 'SEBI', 'RBI', 'Annual Report disclosure',
       'Board / CSR Committee', 'Reasonable assurance provider', 'Website disclosure', 'Not Required'],
    instruments=['SEBI (LODR) Regulations 2015, Reg 34(2)(f) - Business Responsibility and Sustainability Report',
                 'SEBI circular on BRSR Core, ESG disclosures for value chain and assurance (28 Mar 2025) - assurance/assessment of BRSR Core phased by market-cap tier; value-chain disclosures voluntary from FY 2025-26 for top 250 listed entities, partners above 2% of purchases or sales [VERIFY paragraph numbers]',
                 'Companies Act 2013 s.135; Companies (Corporate Social Responsibility Policy) Rules 2014 as amended; Form CSR-2',
                 'Companies Act 2013 s.134(3)(m) and Companies (Accounts) Rules 2014 r.8(3) - conservation of energy and technology absorption',
                 'RBI draft Disclosure framework on Climate-related Financial Risks (2024) and any final directions [VERIFY status]',
                 'GHG Protocol Corporate Standard and Scope 3 Standard; ISSB IFRS S1/S2 (for voluntary or foreign-group reporting)'],
    example=ex(B=1, C='SEBI LODR Reg 34(2)(f) - BRSR', D='Listed entity - Top 1000 by market capitalisation',
               F='BRSR in Annual Report',
               G='Has the listed entity included a Business Responsibility and Sustainability Report, in the SEBI-prescribed format, as part of its Annual Report for the financial year?',
               H='Annually', K='SEBI (LODR) Regulations 2015, Reg 34(2)(f)',
               L='The top 1,000 listed entities by market capitalisation must publish a BRSR in the format prescribed by SEBI as part of the Annual Report. The BRSR covers the nine principles of the National Guidelines on Responsible Business Conduct, with essential and leadership indicators.',
               M='Secretarial', N='SEBI LODR Reg 34(2)(f); SEBI BRSR format and BRSR Core circulars', O='Disclosures',
               P='Stock exchange (BRSR as part of Annual Report)', Q='Non-compliance with LODR disclosure requirements attracts action by the stock exchanges under the SEBI SOP for fines and by SEBI under the SEBI Act 1992.',
               R='High', S='Applies to the top 1,000 listed entities by market capitalisation as at 31 March; others may publish voluntarily.',
               U='Annual Report containing the BRSR; Board approval of the BRSR; stock exchange filing acknowledgement.',
               V='Collect ESG data through the ESG module, draft the BRSR from the data (Vidhi drafts narrative only; figures come from the metric layer), obtain Board approval and include it in the Annual Report filed with the stock exchanges.'),
)

if __name__ == '__main__':
    base, out_dir = sys.argv[1], sys.argv[2]
    out, code, h2, counts = bt.build(base, out_dir, ESG)
    print(code, counts, out.rsplit('/', 1)[1], h2)
