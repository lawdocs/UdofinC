# -*- coding: utf-8 -*-
"""v1.1 (stream G1): build the INTL-GEN (international jurisdictions) question template.

Reuses build() from build_templates.py without modifying it.
Usage: python3 v11_G1_build_intl.py <base_xlsx (owner's Appointed Actuary sample)> <out_dir>
"""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import build_templates as bt  # noqa: E402
from family_vocab import FREQ_EXT, DEPT_BASE, COMP_BASE, ex  # noqa: E402

bt.SHORT['INTL-GEN'] = 'International Jurisdictions'

JURISDICTIONS = [
    'United Arab Emirates - Mainland (Federal)', 'United Arab Emirates - DIFC', 'United Arab Emirates - ADGM', 'Saudi Arabia', 'Qatar (incl. QFC)',
    'Bahrain', 'Oman', 'Kuwait', 'Singapore', 'Hong Kong SAR', 'Malaysia', 'Indonesia', 'Thailand', 'Vietnam', 'Philippines', 'Japan',
    'South Korea', 'China (Mainland)', 'Australia', 'New Zealand', 'Sri Lanka', 'Bangladesh', 'Nepal', 'Mauritius', 'Kenya', 'Nigeria',
    'South Africa', 'Egypt', 'United Kingdom', 'Ireland', 'Netherlands', 'Germany', 'France', 'Luxembourg', 'Switzerland', 'Cyprus',
    'Spain', 'Italy', 'Belgium', 'Poland', 'European Union (supranational)', 'United States - Federal', 'United States - Delaware',
    'United States - New York', 'United States - California', 'United States - Texas', 'Canada - Federal', 'Canada - Ontario', 'Mexico',
    'Brazil', 'Other jurisdiction', 'All jurisdictions (ALL)']

ENTITY_FORMS = [
    'Private company limited by shares', 'Public company (unlisted)', 'Listed company', 'Branch of a foreign company',
    'Representative / liaison office', 'Limited liability partnership (LLP)', 'Partnership', 'Limited Liability Company (LLC)',
    'Corporation (C-Corp / S-Corp)', 'Free zone company (FZCO / FZ-LLC / FZE)', 'Civil-law company (GmbH / AG / SARL / SAS / BV / NV / SpA)',
    'Bank / deposit-taking institution', 'Non-bank lender / finance company', 'Investment fund / fund manager', 'Insurance entity',
    'Payment / e-money institution', 'Holding company / SPV', 'Non-profit / foundation / charity', 'Group parent (consolidated obligations)',
    'Subsidiary of an Indian parent (ODI)', 'All entity forms (ALL)']

FILING = [
    'Company Registry (e.g., Companies House, ACRA, Registrar of Companies)', 'Tax Authority (corporate income tax)', 'Tax Authority (VAT / GST / sales tax)',
    'Financial Regulator / Central Bank', 'Securities Regulator / Stock Exchange', 'Data Protection Authority', 'Labour / Social Security Authority',
    'Beneficial Ownership Register', 'Financial Intelligence Unit (AML)', 'Statistics / Foreign Investment Reporting',
    'Registered Agent / Corporate Service Provider', 'Local Statutory Auditor', 'Parent reporting - India (RBI ODI / FEMA, e.g., APR)',
    'Board / Management', 'Not Required']

INTL = dict(
    code='INTL-GEN', name='International Jurisdictions (company, regulatory, data and employment obligations outside India)',
    regulator='Foreign authorities by jurisdiction (company registries, tax authorities, financial regulators, data protection authorities, labour authorities)',
    prefix='INTL', c_label='Jurisdiction (Column C)', C=JURISDICTIONS, d_label='Entity Form (Column D)', D=ENTITY_FORMS,
    H=FREQ_EXT, M=DEPT_BASE + ['Secretarial', 'Tax', 'Privacy Office (DPO)', 'Information Security', 'KYC & AML', 'Payroll'],
    O=COMP_BASE + ['Licences & Registrations'], R=['High', 'Medium', 'Low'], P=FILING,
    instruments=[
        'United Kingdom: Companies Act 2006 (confirmation statement s.853A; PSC register Part 21A; accounts filing ss.441-442); Economic Crime and Corporate Transparency Act 2023 (identity verification) [VERIFY commencement dates]',
        'Singapore: Companies Act 1967 (annual return s.197; Register of Registrable Controllers); Income Tax Act 1947; PDPA 2012',
        'United Arab Emirates: Federal Decree-Law No. 32 of 2021 on Commercial Companies; Cabinet Decision No. 109 of 2023 (beneficial owner); Federal Decree-Law No. 45 of 2021 (PDPL); DIFC Data Protection Law No. 5 of 2020 as amended 2025; ADGM Data Protection Regulations 2021',
        'European Union: GDPR (Regulation (EU) 2016/679); DORA (Regulation (EU) 2022/2554); NIS2 (Directive (EU) 2022/2555); EU AI Act (Regulation (EU) 2024/1689) [VERIFY national transposition]',
        'United States: Delaware General Corporation Law (annual franchise tax report); Corporate Transparency Act BOI reporting (scope narrowed by the 2025 interim final rule) [VERIFY]; state privacy laws (e.g., CCPA/CPRA)',
        'India (parent side): FEMA (Overseas Investment) Rules and Regulations, 2022 and RBI Master Direction on Overseas Investment - Annual Performance Report for each overseas entity [VERIFY current para]'],
    example=ex(B=1, C='United Kingdom', D='Private company limited by shares', F='Confirmation statement - annual filing with Companies House',
               G='Has the company delivered a confirmation statement to the registrar for each review period (a period of not more than 12 months), within 14 days after the end of that review period, confirming that all required information has been delivered or delivering it with the statement?',
               H='Annually', K='Sections 853A and 853L, Companies Act 2006 (United Kingdom)',
               L='Every UK company must confirm at least once in every 12-month review period that the information Companies House holds (registered office, officers, share capital, people with significant control, SIC code, shareholder information where required) is up to date. The statement is due within 14 days after the end of the review period. Changes not already notified must be delivered with or before the statement.',
               M='Governance & Administration', N='Companies Act 2006 ss.853A-853L | https://www.legislation.gov.uk/ukpga/2006/46/part/24 | Companies House guidance on confirmation statements',
               O='Returns & Reporting', P='Company Registry (e.g., Companies House, ACRA, Registrar of Companies) — Due: within 14 days after the end of each review period',
               Q='Failure is an offence by the company and every officer in default (s.853L), punishable by a fine, and may lead the registrar to begin striking the company off the register.',
               R='High', S='Applies to every company registered in the United Kingdom. Branches of overseas companies (UK establishments) file overseas-company returns instead.',
               U='Companies House filing confirmation (acceptance e-mail / filing history extract) for the review period.',
               V='Diarise the review-period end date; check registered office, officers, PSC, share capital and SIC code against the statutory registers; file the confirmation statement on Companies House within 14 days; save the acceptance confirmation.'))

if __name__ == '__main__':
    base, out_dir = sys.argv[1], sys.argv[2]
    out, code, h2, counts = bt.build(base, out_dir, INTL)
    print(code, counts, out.rsplit('/', 1)[1])
