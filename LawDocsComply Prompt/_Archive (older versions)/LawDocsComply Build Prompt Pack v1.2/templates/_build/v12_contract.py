# -*- coding: utf-8 -*-
"""LawDocsComply template contract v2.0 (pack v1.2, decision D-49).

Single source of truth for the v2.0 builder (v12_build_templates.py), the v2.0 validator
(../_validate_templates_v2.py), the synthetic samples and Appendix E tables.
Prepared 25 October 2026. Base vocabularies are immutable within major version 2 (NN-35 as amended):
families may add values and extension columns, never rename or remove base ones.
"""
import sys
from collections import OrderedDict

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from family_vocab import FAMILIES as _V1, FREQ_EXT, RISK  # noqa: E402
import v11_G1_build_intl as _g1  # noqa: E402
import v11_G3_build_aigov as _g3  # noqa: E402
import v11_X1_build_esg as _x1  # noqa: E402

CONTRACT_VERSION = '2.0'
BUILD_DATE = '2026-10-25'
SHEET = 'Compliance Register'
SHEETS = [SHEET, 'Lists', 'Read Me', '_Template_Info']
HEADER_ROW, BAND_ROW, FIRST_DATA_ROW = 2, 1, 3
DV_LAST_ROW = 5000
FORMAT_LAST_ROW = 1000
SEP = '\x1f'
MULTI_SEP = '; '
INFO_PASSWORD = 'LDC-TPL'

# ------------------------------------------------------------------ groups (row-1 bands)
GROUPS = [  # (code, band label, fill colour)
    ('LIST', 'LIST VIEW', 'FFF2CC'),
    ('SOURCE', 'SOURCE & VERSION', 'E2EFDA'),
    ('APPLIC', 'APPLICABILITY', 'DDEBF7'),
    ('DETAIL', 'COMPLIANCE DETAIL', 'FCE4D6'),
    ('MAKER', 'MAKER', 'E4DFEC'),
    ('CHECKER', 'CHECKER', 'D9D2E9'),
    ('AUDITOR', 'AUDITOR', 'CCC0DA'),
    ('SYSTEM', 'SYSTEM', 'EDEDED'),
]
GROUP_COLOUR = {g: c for g, _, c in GROUPS}
GROUP_LABEL = {g: l for g, l, _ in GROUPS}

# ------------------------------------------------------------------ base columns
# (group, header, key, filled_by, at_authoring, list_key or 'date' or None, width, multi, rule)
# at_authoring: Required / Conditional / Optional / Blank
C = []


def col(group, header, key, by, at, lst, width, rule, multi=False, soft=False):
    C.append(dict(group=group, header=header, key=key, by=by, at=at, list=lst, width=width, multi=multi, rule=rule, soft=soft))


col('LIST', 'S. No.', 'sno', 'Author', 'Required', None, 6, 'Integer 1..n, unique and contiguous within the sheet; display order only (never an identifier).')
col('LIST', 'CompID', 'comp_id', 'System', 'Blank', None, 22, 'Leave blank when authoring. LawDocsComply assigns <AUTH>-<FAM>-<INST>-<NNNN> on import/publish (D-52). On re-import of an exported sheet the CompID identifies the item to update; never edit or reuse it (NN-56).')
col('LIST', 'Compliance Question / Actionable', 'question', 'Author', 'Required', None, 60, 'One closed question per row ("Has the <entity> ...?"); split bundled sub-clauses into separate rows. Max 2,000 characters.')
col('LIST', 'Clause / Para No.', 'clause_ref', 'Author', 'Required', None, 16, 'Exact para / regulation / section, including "as substituted / inserted vide <notification> dated <date>" where amended.')
col('LIST', 'Department', 'department', 'Author', 'Required', 'Dept', 22, 'One value from the family Department list (tenants may rename departments in the tool; the import keeps the library value).')
col('LIST', 'Due Date & Frequency', 'frequency', 'Author', 'Required', 'Freq', 16, 'One value from the Frequency list. The exact due-date rule goes in Due Date Rule (COMPLIANCE DETAIL).')
col('LIST', 'Date of Compliance', 'act_date', 'User', 'Blank', 'date', 13, 'Date the compliance was actually done (DD-MMM-YYYY). Filled in the tool or in a working copy; ignored on content import.')
col('LIST', 'Status', 'status', 'User', 'Blank', 'Status', 18, 'Canonical status label. Set by the workflow; ignored on content import.')
col('LIST', 'Risk Category', 'risk_level', 'Author', 'Required', 'Risk', 10, 'High / Medium / Low per the calibration rule in the Part-2 command.')

col('SOURCE', 'Regulator / Authority', 'authority', 'Author', 'Required', 'Auth', 18, 'Issuing regulator or authority from the family list; name the department where the list offers it (e.g., "RBI – DoR"). A foreign regulator not in the list may be typed (warning) and is checked against the jurisdiction pack.', soft=True)
col('SOURCE', 'Name of Master Direction / Regulation', 'instrument_name', 'Author', 'Required', None, 40, 'Full official title of the instrument, exactly as issued (e.g., "Reserve Bank of India (Non-Banking Financial Companies – Governance) Directions, 2025").')
col('SOURCE', 'Instrument Reference No.', 'instrument_ref', 'Author', 'Required', None, 22, 'Official reference (e.g., RBI/DOR/2025-26/344; F. No.; Gazette notification no.). "Not numbered" if none.')
col('SOURCE', 'Issue Date of Instrument', 'instrument_issue_date', 'Author', 'Required', 'date', 13, 'Date of issue / notification of the instrument (DD-MMM-YYYY).')
col('SOURCE', 'Instrument Last Amended On', 'instrument_amended_date', 'Author', 'Required', 'date', 13, 'Date of the latest amendment to the instrument as a whole that the sheet incorporates. If the instrument has never been amended, repeat the issue date.')
col('SOURCE', 'Actionable Last Updated On', 'question_updated_date', 'Author', 'Required', 'date', 13, 'Date of the regulator\'s change that last affected THIS row (issue date if never amended). Differs row to row; drives "Changed in last 30 days" and the changed badge.')
col('SOURCE', 'Change Status', 'change_status', 'Author', 'Required', 'Change', 12, 'New / Amended / Unchanged / Re-cited / Retired relative to the previous version of the sheet. First version: New.')
col('SOURCE', 'Change Note / Previous Actionable', 'change_note', 'Author', 'Conditional', None, 40, 'Required when Change Status is Amended, Re-cited or Retired: the amending notification and the previous wording / para.')
col('SOURCE', 'Source Link', 'source_url', 'Author', 'Required', None, 30, 'Official URL of the instrument (regulator website / e-Gazette). One URL.')

col('APPLIC', 'General Applicability (Layer)', 'applic_layer', 'Author', 'Required', 'Layer', 22, 'One or more values from the family layer / category list separated by "; ".', multi=True)
col('APPLIC', 'General Applicability (Type)', 'applic_type', 'Author', 'Required', 'Type', 26, 'One or more values from the family entity-type list separated by "; ".', multi=True)
col('APPLIC', 'Conditional Applicability / Exemptions / Thresholds', 'conditions', 'Author', 'Required', None, 36, 'Thresholds, carve-outs, exemptions and transition. Write "Applies to all <entities>." if none.')
col('APPLIC', 'Applicable From', 'applic_from', 'Author', 'Optional', 'date', 13, 'Effective date of this actionable if different from the instrument issue date (e.g., deferred commencement).')
col('APPLIC', 'Applicable Until', 'applic_to', 'Author', 'Optional', 'date', 13, 'Sunset / repeal date; blank = open-ended.')
APPLIC_EXT_AFTER = 'applic_to'  # family extension columns are inserted after this key

col('DETAIL', 'Short Title', 'short_title', 'Author', 'Required', None, 28, 'Heading of the para or a short descriptive title (max 200 characters).')
col('DETAIL', 'Interpretation / Explanation', 'explanation', 'Author', 'Required', None, 50, 'Plain-language explanation: quote the provision, explain each element, note links to other provisions.')
col('DETAIL', 'Department Function', 'dept_function', 'Author', 'Required', 'FUNC', 24, 'Function within the Department (dependent dropdown: choose Department first).')
col('DETAIL', 'Department Sub-function', 'dept_subfunction', 'Author', 'Optional', 'SUBF', 24, 'Sub-function within the Function (dependent dropdown: choose Function first).')
col('DETAIL', 'Compliance Type', 'compliance_type', 'Author', 'Required', 'CompType', 18, 'One value from the family Compliance Type list.')
col('DETAIL', 'Due Date Rule', 'due_rule', 'Author', 'Conditional', None, 30, 'Structured due-date text per the Appendix E grammar, e.g., "Within 15 days from the end of each quarter". Required unless Frequency is Ongoing/Continuous.')
col('DETAIL', 'Event Trigger (for Event Based items)', 'event_trigger', 'Author', 'Conditional', 'Event', 24, 'Required when Frequency is Event Based or Immediately: the triggering event from the event catalogue; if none fits, type "Other: <event>" (warning) so the catalogue can be extended.', soft=True)
col('DETAIL', 'Filing / Reporting / Intimation', 'filing_details', 'Author', 'Required', 'Filing', 26, 'Start with a value from the Filing list ("Not Required" if none); optionally add " — " and detail.', multi=True)
col('DETAIL', 'Portal / Form / Return Code', 'filing_form', 'Author', 'Optional', None, 18, 'Form, return or portal code (e.g., DNBS-01, MGT-7, GSTR-3B).')
col('DETAIL', 'Related Document / Policy / Committee', 'related_docs', 'Author', 'Optional', None, 28, 'Related policies, registers, committees and instruments. Parts separated by " | ".')
col('DETAIL', 'Reference Weblinks', 'weblinks', 'Author', 'Optional', None, 28, 'Additional official URLs separated by " | ".')
col('DETAIL', 'Consequences of Non-Compliance / Penalty', 'consequences', 'Author', 'Required', None, 36, 'Provision breached, enforcement power (Act and section) and practical consequence.')
col('DETAIL', 'Penalty Provision', 'penalty_ref', 'Author', 'Optional', None, 20, 'Exact penalty section / regulation (e.g., s.58G RBI Act, 1934).')
col('DETAIL', 'Risk Type', 'risk_type', 'Author', 'Required', 'RiskType', 18, 'One or more values from the Risk Type list separated by "; " (first value = primary).', multi=True)
col('DETAIL', 'Linked RiskID', 'risk_ids', 'Author/User', 'Optional', None, 18, 'RiskIDs (RSKL-<TAXO>-NNNN library or RSK-<TENANT4>-NNNNN tenant) separated by "; ".')
col('DETAIL', 'Linked GovID', 'gov_ids', 'Author/User', 'Optional', None, 18, 'GovIDs (GOVL-<AUTH>-NNNN library or GOV-<TENANT4>-<TYPE>-NNNNN tenant) separated by "; ".')
col('DETAIL', 'Evidence / Proof to Upload', 'evidence', 'Author', 'Required', None, 30, 'Specific artefacts that prove compliance (document, register, acknowledgement, URL with archive).')
col('DETAIL', 'Control Activity (Maker Guidance)', 'control_activity', 'Author', 'Required', None, 36, 'Imperative, step-by-step instruction to the maker on what to do and what to produce.')
col('DETAIL', 'Checker Review Points', 'checker_points', 'Author', 'Required', None, 30, 'What the checker must verify before approving (2–5 points).')
col('DETAIL', 'Auditor Test Procedure', 'audit_test', 'Author', 'Optional', None, 30, 'Test of design / operating effectiveness for internal audit or concurrent audit.')
col('DETAIL', 'Tags / Keywords', 'tags', 'Author', 'Optional', None, 18, 'Free keywords separated by "; " (search and saved views).')

col('MAKER', 'Maker User / Email ID', 'maker', 'User', 'Blank', None, 22, 'Assigned maker. Filled from assignments in the tool; ignored on content import.')
col('MAKER', 'Status Update by Maker', 'maker_status', 'User', 'Blank', 'MakerStatus', 18, 'Maker status from the list.')
col('MAKER', 'Evidence Reference', 'evidence_ref', 'User', 'Blank', None, 20, 'Vault reference / file name of the evidence uploaded.')
col('MAKER', 'Evidence Date', 'evidence_date', 'User', 'Blank', 'date', 13, 'Date of the evidence document.')
col('MAKER', 'Comments by Maker', 'maker_comments', 'User', 'Blank', None, 30, 'Maker comments (the conversation thread in the tool is the record; this is a summary).')

col('CHECKER', 'Checker User / Email ID', 'checker', 'User', 'Blank', None, 22, 'Assigned checker.')
col('CHECKER', 'Review — Approve / Reject / Reallocate', 'checker_decision', 'User', 'Blank', 'Decision', 20, 'Checker decision from the list.')
col('CHECKER', 'Approval Date', 'approval_date', 'User', 'Blank', 'date', 13, 'Date of the checker decision.')
col('CHECKER', 'Comments by Checker', 'checker_comments', 'User', 'Blank', None, 30, 'Checker comments.')

col('AUDITOR', 'Assigned Auditor / Email ID', 'auditor', 'User', 'Blank', None, 22, 'Assigned auditor.')
col('AUDITOR', 'Audit Result', 'audit_result', 'User', 'Blank', 'AuditResult', 14, 'Satisfactory / Observation / Exception / Not Tested.')
col('AUDITOR', 'Comments by Auditor', 'auditor_comments', 'User', 'Blank', None, 30, 'Auditor comments.')

col('SYSTEM', 'Accountable Owner', 'accountable_owner', 'System', 'Blank', None, 22, 'Owner of record (never blank in the tool; falls back to the department head). Written on export.')
col('SYSTEM', 'Next Due Date', 'next_due', 'System', 'Blank', 'date', 13, 'Computed from frequency, due rule and calendar. Written on export.')
col('SYSTEM', 'Days to Due', 'days_to_due', 'System', 'Blank', None, 9, 'Next Due Date minus export date (negative = overdue). Written on export.')
col('SYSTEM', 'RAG', 'rag', 'System', 'Blank', 'RAG', 8, 'Red / Amber / Green / Grey / Blue per the published RAG rules (NN-58). Written on export.')
col('SYSTEM', 'Question Version', 'question_version', 'System', 'Blank', None, 9, 'Library version of the question (e.g., 3). Written on export.')
col('SYSTEM', 'Tenant Overlay', 'overlay', 'System', 'Blank', 'YesNo', 9, 'Yes if the tenant has an overlay (edited wording, extra evidence) on this CompID.')

BASE_COLUMNS = C
BASE_KEYS = [c['key'] for c in C]
assert len(BASE_COLUMNS) == 62, len(BASE_COLUMNS)
LIST_VIEW_KEYS = [c['key'] for c in C if c['group'] == 'LIST']
EXPORT_DEFAULT_KEYS = LIST_VIEW_KEYS + ['next_due', 'days_to_due', 'rag', 'maker']  # D-50
CONTENT_KEYS = [c['key'] for c in C if c['by'] in ('Author', 'Author/User')]

# ------------------------------------------------------------------ base vocabularies (immutable in v2)
STATUS = ['Not Started', 'In Progress', 'In Progress (Interim)', 'Waiting on Others', 'Submitted for Review',
          'Returned for Rework', 'Complied', 'Complied Late', 'Partially Complied', 'Not Complied',
          'Not Applicable', 'Exempted', 'Deferred by Regulator', 'Withdrawn']
MAKER_STATUS = ['Not Started', 'In Progress', 'Evidence Uploaded', 'Submitted for Review', 'Needs Clarification',
                'Not Applicable — Request', 'Delayed — Reason Recorded']
DECISION = ['Approve', 'Reject — Return to Maker', 'Reallocate', 'Request Information']
AUDIT_RESULT = ['Satisfactory', 'Observation', 'Exception', 'Not Tested']
CHANGE = ['New', 'Amended', 'Unchanged', 'Re-cited', 'Retired']
RISK_TYPE = ['Regulatory', 'Operational', 'Credit', 'Market', 'Liquidity', 'Conduct & Consumer', 'IT & Cyber',
             'Data Privacy', 'Fraud', 'Legal', 'Reputational', 'Governance', 'People', 'Third-party', 'ESG & Climate',
             'Model & AI']
RAG = ['Red', 'Amber', 'Green', 'Grey', 'Blue']
RAG_FILL = {'Red': 'F8696B', 'Amber': 'FFC000', 'Green': '63BE7B', 'Grey': 'BFBFBF', 'Blue': '9BC2E6'}
YESNO = ['Yes', 'No']
EVENTS = [  # seed catalogue = Part-2 master §7B list + platform additions; families may add values
    'Appointment of director / KMP / officer', 'Cessation or resignation of director / KMP / officer',
    'Change in shareholding, control or management', 'Change in name, address or registered office',
    'Board meeting held', 'Committee meeting held', 'General meeting held', 'Policy approved or amended', 'Product or activity launched',
    'Outsourcing or material contract entered into', 'Contract terminated', 'Fraud detected', 'Cyber or data security incident detected',
    'Personal data breach', 'Customer complaint or grievance received', 'Customer request received (e.g. data principal request)',
    'Account classified as SMA / NPA / default', 'Limit or threshold breached', 'Suspicious transaction identified',
    'Regulator direction, order or inspection report received', 'Show-cause notice received', 'Litigation or claim received',
    'Penalty imposed', 'Financial statements adopted', 'Audit report received', 'Employee joined / left',
    'Complaint of sexual harassment received', 'Amendment of MoA / AoA / bye-laws', 'Opening, closure or shifting of branch or office',
    'Allotment or transfer of securities', 'Merger, demerger or restructuring', 'Commencement or cessation of business or activity']
EVENT_OTHER_PREFIX = 'Other: '

STATES = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
          'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
          'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal',
          'Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi (NCT)', 'Jammu and Kashmir',
          'Ladakh', 'Lakshadweep', 'Puducherry', 'All States / UTs', 'Multi-State']

# ------------------------------------------------------------------ authority lists by family group
_RBI_AUTH = ['RBI', 'RBI – DoR', 'RBI – DoS', 'RBI – CEPD', 'RBI – FED', 'RBI – DPSS', 'RBI – FMRD']
_COMMON_AUTH = ['MCA', 'FIU-IND', 'CERT-In', 'MeitY', 'Data Protection Board of India', 'State Government', 'Other']
AUTH_BY_GROUP = {  # Part-2 master §6.2 values first; authority is a soft list (foreign regulators may be typed, warning)
    'RBI': _RBI_AUTH + ['NABARD', 'NHB', 'DICGC', 'SEBI', 'Government of India (MoF)'] + _COMMON_AUTH,
    'COOP': ['Registrar of Co-operative Societies', 'Central Registrar of Co-operative Societies', 'Ministry of Co-operation', 'Co-operative Election Authority', 'RBI', 'NABARD'] + _COMMON_AUTH,
    'IFSCA': ['IFSCA', 'RBI – FED', 'SEBI', 'IRDAI', 'SEZ Authority (GIFT City)'] + _COMMON_AUTH,
    'SEBI': ['SEBI', 'Stock Exchanges (NSE / BSE)', 'Depositories (NSDL / CDSL)', 'Clearing Corporations', 'AMFI', 'RBI – FED'] + _COMMON_AUTH,
    'IRDAI': ['IRDAI', 'Insurance Council', 'Insurance Ombudsman', 'Government of India (MoF)'] + _COMMON_AUTH,
    'MCA': ['MCA', 'Registrar of Companies', 'NCLT / NCLAT', 'ICSI (Secretarial Standards)', 'ICAI / NFRA', 'IEPF Authority', 'RBI – FED', 'SEBI', 'FIU-IND', 'CERT-In', 'MeitY', 'State Government', 'Other'],
    'DATA-PRIV': ['MeitY', 'Data Protection Board of India', 'CERT-In', 'RBI', 'SEBI', 'IRDAI', 'IFSCA', 'EU / EEA supervisory authority', 'UK ICO', 'California Privacy Protection Agency / Attorney General', 'Other'],
    'CYBER': ['CERT-In', 'NCIIPC', 'RBI', 'SEBI', 'IRDAI', 'IFSCA', 'MeitY', 'ISO / IEC', 'NIST', 'PCI Security Standards Council', 'EU (DORA / NIS2)', 'Other'],
    'LAB-POSH': ['Ministry of Labour & Employment', 'State Government', 'State Labour Department', 'EPFO', 'ESIC', 'Local Committee / District Officer (POSH)', 'Ministry of Women and Child Development', 'Other'],
    'TAX-GST': ['CBIC', 'GST Council', 'State GST Department', 'CBDT', 'State Government', 'Other'],
    'INTL': ['Companies House (UK)', 'National company registry', 'Financial services regulator', 'Central bank', 'Data protection authority', 'Tax authority', 'Labour ministry / authority', 'Securities regulator', 'Supranational (EU / FATF / IOSCO)', 'RBI – FED', 'Other'],
    'AI-GOV': ['RBI', 'SEBI', 'IRDAI', 'IFSCA', 'MeitY', 'Data Protection Board of India', 'EU AI Office / national market-surveillance authority', 'ISO / IEC', 'NIST', 'Other'],
    'ESG': ['SEBI', 'MCA', 'Stock Exchanges (NSE / BSE)', 'RBI', 'IFSCA', 'ISSB / IFRS Foundation', 'GHG Protocol', 'Ministry of Environment, Forest and Climate Change', 'Other'],
}
AUTH_CODE = {  # default CompID <AUTH> segment by family group (P03 FR-P03-101)
    'RBI': 'RBI', 'COOP': 'COOP', 'IFSCA': 'IFSCA', 'SEBI': 'SEBI', 'IRDAI': 'IRDAI', 'MCA': 'MCA', 'DATA-PRIV': 'MEITY',
    'CYBER': 'CERTIN', 'LAB-POSH': 'MOLE', 'TAX-GST': 'GST', 'INTL': 'INTL', 'AI-GOV': 'MEITY', 'ESG': 'SEBI'}
CROSS_AUTHORITY = {'DATA-PRIV', 'CYBER', 'LAB-POSH', 'TAX-GST', 'AI-GOV', 'ESG-BRSR'}  # AUTH = issuing authority of the instrument


def family_group(code):
    for g in ('RBI', 'COOP', 'IFSCA', 'SEBI', 'IRDAI', 'MCA'):
        if code.startswith(g):
            return g
    return {'DATA-PRIV': 'DATA-PRIV', 'CYBER': 'CYBER', 'LAB-POSH': 'LAB-POSH', 'TAX-GST': 'TAX-GST', 'INTL-GEN': 'INTL',
            'AI-GOV': 'AI-GOV', 'ESG-BRSR': 'ESG'}[code]


# ------------------------------------------------------------------ family extension columns (§5)
# key -> (header, list or None (free text), multi)
EXT = {  # values aligned with the Part-2 family commands §7.1 (T2, v1.2); blank cell = "not a deciding factor"
    'RBI-NBFC': [('ext_customer_interface', 'Customer Interface', ['With customer interface', 'Without customer interface'], False),
                 ('ext_public_funds', 'Public Funds / Deposits', ['Deposit-taking (NBFC-D)', 'Non-deposit-taking with public funds', 'No public funds'], True),
                 ('ext_asset_size', 'Asset Size Threshold', ['Below ₹1,000 crore', '₹1,000 crore and above', '₹5,000 crore and above', '₹10,000 crore and above'], True)],
    'RBI-SCB': [('ext_dsib_listed', 'D-SIB / Listed Status', ['D-SIB', 'Listed bank', 'Listed D-SIB', 'Not D-SIB and not listed'], True)],
    'RBI-UCB': [('ext_registration', 'Registration (State / Multi-State)', ['State-registered UCB (State Co-operative Societies Act)', 'Multi-State UCB (MSCS Act, 2002)'], True),
                ('ext_deposit_band', 'Deposit Band', ['Up to ₹100 crore', 'Above ₹100 crore up to ₹1,000 crore', 'Above ₹1,000 crore up to ₹10,000 crore', 'Above ₹10,000 crore'], True)],
    'RBI-RCB': [('ext_rcb_tier', 'Tier (StCB / DCCB)', ['State Co-operative Bank (StCB)', 'District Central Co-operative Bank (DCCB)'], True)],
    'RBI-ARC': [('ext_nof_band', 'NOF Band', ['Below ₹300 crore', '₹300 crore to below ₹1,000 crore', '₹1,000 crore and above'], True)],
    'RBI-OTH': [],
    'COOP-CCS': [('ext_governing_act', 'Governing Act (State / MSCS)', ['State Co-operative Societies Act', 'Multi-State Co-operative Societies Act, 2002', 'State Mutually Aided Co-operative Societies Act'], True),
                 ('ext_state', 'State', STATES, True),
                 ('ext_size_class', 'Society Size Class', ['Small', 'Medium', 'Large'], True)],
    'IFSCA-GEN': [('ext_setup_form', 'Form of Set-up', ['Company', 'Branch', 'LLP', 'Trust'], True)],
    'SEBI-LISTED': [('ext_listing_segment', 'Listing Segment', ['Main Board', 'SME Platform', 'Non-convertible securities', 'Commercial paper', 'Social Stock Exchange'], True),
                    ('ext_mcap_band', 'Market-cap Band', ['Top 100', 'Top 250', 'Top 500', 'Top 1000', 'Top 2000', 'Other'], True),
                    ('ext_hvdle', 'HVDLE', ['HVDLE', 'Not HVDLE'], False)],
    'SEBI-MF': [('ext_applies_to', 'Applies To (AMC / Trustee / Scheme)', ['AMC', 'Trustee', 'Scheme'], True)],
    'SEBI-AIF': [('ext_aif_category', 'AIF Category', ['Category I', 'Category II', 'Category III'], True),
                 ('ext_lvf', 'LVF / Accredited', ['Large Value Fund for Accredited Investors', 'Scheme for accredited investors only', 'Neither'], True)],
    'SEBI-REIT-INVIT': [('ext_vehicle_role', 'Vehicle Role', ['Trust', 'Manager / Investment Manager', 'Trustee', 'Sponsor', 'Project Manager', 'Valuer'], True)],
    'SEBI-INT': [('ext_cscrf_band', 'CSCRF Size Band', ['MII', 'Qualified RE', 'Mid-size RE', 'Small-size RE', 'Self-certification RE'], True)],
    'IRDAI-INS': [('ext_lob', 'Line of Business', ['Life', 'General', 'Health', 'Reinsurance'], True)],
    'IRDAI-INT': [('ext_int_class', 'Intermediary Class', ['Insurance broker', 'Corporate agent', 'Insurance marketing firm', 'Web aggregator', 'TPA', 'Surveyor and loss assessor', 'POSP / MISP channel', 'Insurance repository'], True)],
    'MCA-CO': [('ext_class_flags', 'Company Class Flags', ['Listed', 'Unlisted public', 'Private', 'OPC', 'Small company', 'Section 8', 'Nidhi', 'Government company', 'Producer company'], True),
               ('ext_fin_threshold', 'Financial Threshold', ['CSR threshold (s.135(1))', 'Independent director threshold (Rule 4, ACMD Rules)', 'Woman director threshold (Rule 3, ACMD Rules)', 'Internal audit threshold (Rule 13, Accounts Rules)', 'Secretarial audit threshold (s.204)', 'Whole-time CS / KMP threshold (Rule 8 / 8A)', 'Cost audit threshold (s.148)'], True)],
    'MCA-LLP': [('ext_small_llp', 'Small LLP', ['Small LLP', 'Not a small LLP'], False)],
    'DATA-PRIV': [('ext_privacy_law', 'Law', ['DPDP Act and Rules', 'IT Act and SPDI Rules', 'EU GDPR', 'UK GDPR', 'CCPA / CPRA', 'Sectoral'], True),
                  ('ext_org_role', 'Organisation Role', ['Data Fiduciary', 'Significant Data Fiduciary', 'Data Processor', 'Consent Manager', 'Controller', 'Processor', 'Business', 'Service Provider'], True)],
    'CYBER': [('ext_cyber_framework', 'Framework', ['CERT-In Directions 2022', 'RBI IT / cyber directions', 'SEBI CSCRF', 'IRDAI guidelines', 'IFSCA guidelines', 'ISO/IEC 27001', 'NIST CSF 2.0', 'PCI DSS'], True),
              ('ext_control_domain', 'Control Domain', ['Governance', 'Identify', 'Protect', 'Detect', 'Respond', 'Recover', 'Third-party', 'Data security', 'Logging and monitoring'], True)],
    'LAB-POSH': [('ext_labour_law', 'Labour Code / Act', ['Code on Wages, 2019', 'Industrial Relations Code, 2020', 'Code on Social Security, 2020', 'OSH Code, 2020', 'POSH Act, 2013', 'Shops and Establishments Act (State)', 'Other'], True),
                 ('ext_state', 'State', STATES, True),
                 ('ext_headcount', 'Headcount Threshold', ['10 or more', '20 or more', '50 or more', '100 or more', '300 or more', '500 or more'], False)],
    'TAX-GST': [('ext_tax_law', 'Tax Law', ['CGST / SGST / IGST', 'Income-tax Act, 2025', 'Income-tax Act, 1961', 'TDS / TCS', 'Professional Tax', 'Stamp Duty'], True),
                ('ext_reg_type', 'Registration Type', ['Regular', 'Composition', 'ISD', 'TDS deductor (GST)', 'TCS collector (e-commerce)', 'Non-resident taxable person', 'OIDAR', 'Casual taxable person'], True)],
    'INTL-GEN': [('ext_country', 'Country', None, True),
                 ('ext_subnational', 'Sub-national Unit', None, True),
                 ('ext_language', 'Official Language', ['English', 'Arabic', 'French', 'German', 'Spanish', 'Portuguese', 'Dutch', 'Italian', 'Chinese', 'Japanese', 'Korean', 'Malay', 'Bahasa Indonesia', 'Thai', 'Vietnamese', 'Other'], True)],
    'AI-GOV': [('ext_ai_framework', 'Framework', ['RBI FREE-AI', 'SEBI AI / ML guidance', 'IRDAI guidance', 'IFSCA guidance', 'MeitY AI Governance Guidelines', 'DPDP Act and Rules', 'EU AI Act', 'ISO/IEC 42001', 'NIST AI RMF'], True),
               ('ext_ai_risk_tier', 'AI Risk Tier', ['Prohibited', 'High', 'Limited (transparency)', 'Minimal', 'General-purpose AI model', 'All tiers'], True)],
    'ESG-BRSR': [('ext_brsr_principle', 'BRSR Principle', ['Section A - General disclosures', 'Section B - Management and process', 'Principle 1', 'Principle 2', 'Principle 3', 'Principle 4', 'Principle 5', 'Principle 6', 'Principle 7', 'Principle 8', 'Principle 9', 'All'], True),
                 ('ext_indicator_class', 'Indicator Class (Essential / Leadership / Core)', ['Essential', 'Leadership', 'Core'], True)],
}
EXT['COOP-GEN'] = EXT['COOP-CCS']
EXT['IFSCA-FCFU'] = EXT['IFSCA-GEN']
EXT['IFSCA-FME'] = EXT['IFSCA-GEN']
_COUNTRIES = sorted({j.split(' - ')[0].split(' (')[0] for j in _g1.INTL['C'] if not j.startswith(('All ', 'Other', 'European Union'))})
EXT['INTL-GEN'][0] = ('ext_country', 'Country', _COUNTRIES + ['European Union (supranational)', 'Other'], True)

# ------------------------------------------------------------------ families
SHORT = {'RBI-SCB': 'Commercial Banks SFBs PBs LABs RRBs', 'RBI-UCB': 'Urban Co-operative Banks', 'RBI-RCB': 'Rural Co-operative Banks',
         'RBI-NBFC': 'NBFCs', 'RBI-ARC': 'Asset Reconstruction Companies', 'RBI-OTH': 'Other RBI Regulated Entities',
         'COOP-CCS': 'Credit Co-operative Societies', 'COOP-GEN': 'Other Co-operative Societies', 'IFSCA-GEN': 'IFSCA Regulated Entities',
         'IFSCA-FCFU': 'IFSCA Finance Companies and Units', 'IFSCA-FME': 'IFSCA Fund Management Entities', 'SEBI-MF': 'Mutual Funds',
         'SEBI-AIF': 'Alternative Investment Funds', 'SEBI-LISTED': 'Listed Entities', 'SEBI-REIT-INVIT': 'REITs and InvITs',
         'SEBI-INT': 'SEBI Intermediaries', 'IRDAI-INS': 'Insurers', 'IRDAI-INT': 'Insurance Intermediaries', 'MCA-CO': 'Companies',
         'MCA-LLP': 'LLPs', 'DATA-PRIV': 'Data Protection and Privacy', 'CYBER': 'Cyber Security', 'LAB-POSH': 'Labour Codes and POSH',
         'TAX-GST': 'GST and Direct Tax', 'INTL-GEN': 'International Jurisdictions', 'AI-GOV': 'AI Governance', 'ESG-BRSR': 'ESG BRSR and CSR'}
FAMILY_SHORT_CODE = {  # <FAM> segment of the CompID = fam_short (P03 FR-P03-101; Appendix B family registry holds the master)
    'RBI-SCB': 'SCB', 'RBI-UCB': 'UCB', 'RBI-RCB': 'RCB', 'RBI-NBFC': 'NBFC', 'RBI-ARC': 'ARC', 'RBI-OTH': 'OTH', 'COOP-CCS': 'CCS',
    'COOP-GEN': 'GEN', 'IFSCA-GEN': 'GEN', 'IFSCA-FCFU': 'FCFU', 'IFSCA-FME': 'FME', 'SEBI-MF': 'MF', 'SEBI-AIF': 'AIF', 'SEBI-LISTED': 'LISTED',
    'SEBI-REIT-INVIT': 'RINV', 'SEBI-INT': 'INT', 'IRDAI-INS': 'INS', 'IRDAI-INT': 'INT', 'MCA-CO': 'CO', 'MCA-LLP': 'LLP',
    'DATA-PRIV': 'PRIV', 'CYBER': 'CYBER', 'LAB-POSH': 'LAB', 'TAX-GST': 'GST', 'INTL-GEN': 'GEN', 'AI-GOV': 'AIGOV', 'ESG-BRSR': 'BRSR'}

COMPID_EXAMPLE = {  # illustrative CompIDs (format examples only)
    'RBI-SCB': 'RBI-SCB-KYC25-0010', 'RBI-UCB': 'RBI-UCB-GOV25-0042', 'RBI-RCB': 'RBI-RCB-IRACP25-0007', 'RBI-NBFC': 'RBI-NBFC-GOV25-0042',
    'RBI-ARC': 'RBI-ARC-REG25-0003', 'RBI-OTH': 'RBI-OTH-MISC25-0001', 'COOP-CCS': 'COOP-CCS-MSCS02-0015', 'COOP-GEN': 'COOP-GEN-MSCS02-0101',
    'IFSCA-GEN': 'IFSCA-GEN-AAR22-0004', 'IFSCA-FCFU': 'IFSCA-FCFU-FCR21-0001', 'IFSCA-FME': 'IFSCA-FME-FMR25-0009', 'SEBI-MF': 'SEBI-MF-MFR96-0021',
    'SEBI-AIF': 'SEBI-AIF-AIFR12-0008', 'SEBI-LISTED': 'SEBI-LISTED-LODR15-0117', 'SEBI-REIT-INVIT': 'SEBI-RINV-REIT14-0005', 'SEBI-INT': 'SEBI-INT-CSCRF24-0012',
    'IRDAI-INS': 'IRDAI-INS-GOV24-0006', 'IRDAI-INT': 'IRDAI-INT-REG24-0003', 'MCA-CO': 'MCA-CO-CA13-0173', 'MCA-LLP': 'MCA-LLP-LLPA08-0011',
    'DATA-PRIV': 'MEITY-PRIV-DPDP25-0003', 'CYBER': 'CERTIN-CYBER-CERT22-0001', 'LAB-POSH': 'MOLE-LAB-COW19-0004', 'TAX-GST': 'GST-GST-GST17-0001',
    'INTL-GEN': 'INTL-GEN-GLB26-0001', 'AI-GOV': 'RBI-AIGOV-FREEAI25-0001', 'ESG-BRSR': 'SEBI-BRSR-BRSR23-0001'}

# Subject abbreviations for instrument short codes <SUBJECT><YY> (P03 FR-P03-102; OI-P03-13). Extend, never redefine.
SUBJECT_ABBR = {
    'GOV': 'Governance', 'KYC': 'Know Your Customer / AML', 'IRACP': 'Income recognition, asset classification, provisioning', 'CAP': 'Capital adequacy',
    'ALM': 'Asset-liability management', 'OUT': 'Outsourcing (also OUTS)', 'OUTS': 'Managing risks in outsourcing', 'CRM': 'Credit risk management',
    'CONC': 'Concentration risk', 'CR': 'Credit facilities', 'CIR': 'Credit information reporting', 'FS': 'Financial statements and disclosures',
    'DIV': 'Declaration of dividends', 'RSA': 'Resolution of stressed assets', 'SEC': 'Securitisation', 'INV': 'Investment portfolio',
    'DEP': 'Deposits', 'RBC': 'Responsible business conduct', 'FPC': 'Fair practices code', 'REG': 'Registration and licensing', 'ACQ': 'Acquisition of shareholding or control',
    'BR': 'Branch authorisation', 'CLIM': 'Climate risk', 'MISC': 'Miscellaneous', 'SR': 'Supervisory returns (also SRET)', 'SRET': 'Supervisory returns',
    'CF': 'Compliance function (also CMPF)', 'CMPF': 'Compliance function', 'IAF': 'Internal audit function', 'SA': 'Statutory audit', 'AR': "Auditor's report",
    'FRM': 'Fraud risk management', 'CYB': 'Cyber security / technology risk', 'DPS': 'Digital payment security', 'IT': 'IT governance', 'IO': 'Internal Ombudsman',
    'RBIOS': 'RBI Integrated Ombudsman Scheme', 'LODR': 'SEBI listing obligations and disclosure requirements', 'PIT': 'Prohibition of insider trading',
    'SAST': 'Substantial acquisition of shares and takeovers', 'ICDR': 'Issue of capital and disclosure requirements', 'NCS': 'Non-convertible securities',
    'MFR': 'SEBI Mutual Funds Regulations', 'REIT': 'SEBI REIT Regulations', 'INVIT': 'SEBI InvIT Regulations', 'AIFR': 'SEBI AIF Regulations', 'CSCRF': 'SEBI cyber security and cyber resilience framework',
    'FMR': 'IFSCA Fund Management Regulations', 'FCR': 'IFSCA Finance Company Regulations', 'AAR': 'Appointed actuary regulations',
    'CA': 'Companies Act', 'LLPA': 'LLP Act', 'SS': 'Secretarial standards', 'CSR': 'Corporate social responsibility', 'BRSR': 'Business responsibility and sustainability reporting',
    'DPDP': 'Digital Personal Data Protection', 'CERT': 'CERT-In directions', 'POSH': 'Prevention of sexual harassment', 'COW': 'Code on Wages',
    'IRC': 'Industrial Relations Code', 'CSS': 'Code on Social Security', 'OSH': 'OSH and Working Conditions Code', 'SE': 'Shops and establishments',
    'GST': 'Goods and services tax', 'ITA': 'Income-tax Act', 'TDS': 'TDS / TCS', 'PT': 'Professional tax', 'MSCS': 'Multi-State Co-operative Societies Act',
    'SCS': 'State co-operative societies Act', 'AIA': 'EU AI Act', 'FREEAI': 'RBI FREE-AI framework', 'MRM': 'Model risk management', 'ISO': 'ISO standard', 'GLB': 'Global baseline',
}


def all_families():
    fams = list(_V1) + [_g1.INTL, _g3.AIGOV, _x1.ESG]
    assert len(fams) == 27 and len({f['code'] for f in fams}) == 27
    return fams


def family_columns(code):
    """Ordered column dicts for a family: base columns with extension columns after `applic_to`."""
    out = []
    for c in BASE_COLUMNS:
        out.append(dict(c, ext=False))
        if c['key'] == APPLIC_EXT_AFTER:
            for key, header, lst, multi in EXT[code]:
                out.append(dict(group='APPLIC', header=header, key=key, by='Author', at='Conditional',
                                list=('X_' + key[4:] if lst else None), width=20, multi=multi, ext=True, soft=False,
                                rule=f'Family extension column ({code}). ' + ('Choose from the list' + ('; several values separated by "; "' if multi else '') + '.' if lst else 'Free text.') +
                                ' Blank = no restriction on this dimension.'))
    return out


def family_lists(fam):
    """List-key -> values for the Lists sheet."""
    code = fam['code']
    L = {
        'Freq': fam.get('H') or FREQ_EXT, 'Dept': fam['M'], 'Layer': fam['C'], 'Type': fam['D'], 'CompType': fam['O'],
        'Filing': fam['P'], 'Risk': fam.get('R') or RISK, 'Auth': AUTH_BY_GROUP[family_group(code)], 'Status': STATUS,
        'MakerStatus': MAKER_STATUS, 'Decision': DECISION, 'AuditResult': AUDIT_RESULT, 'Change': CHANGE, 'RiskType': RISK_TYPE,
        'Event': EVENTS, 'RAG': RAG, 'YesNo': YESNO,
    }
    for key, header, lst, multi in EXT[code]:
        if lst:
            L['X_' + key[4:]] = lst
    return L


# ------------------------------------------------------------------ Department -> Function -> Sub-function
GENERIC_SUB = ['Policy & Framework', 'Process Execution', 'Monitoring & Review', 'Reporting & Filing', 'Records & Evidence']
FUNCTIONS = {
    # nine base departments: Part-2 master §10A orientation map (T2) + platform additions
    'Governance & Administration': ['Board & Committees', 'Secretarial', 'Policies & Codes', 'Fit & Proper'],
    'Finance, Treasury and Accounts': ['Accounting & Financial Reporting', 'Capital Management', 'Treasury & Investments', 'Taxation', 'Accounts Payable & Receivable'],
    'Legal & Litigation': ['Litigation', 'Contracts & Documentation', 'Recovery Proceedings', 'Regulatory Legal Advice'],
    'IT': ['IT Governance', 'Information Security & Cyber', 'IT Operations', 'IT Outsourcing'],
    'Operations & Management': ['Lending / Business Operations', 'Customer Service & Grievance', 'Fair Practices & Conduct', 'Recovery & Collections', 'Outsourcing', 'Branch & Premises'],
    'HR': ['Recruitment & Appointments', 'Training', 'Remuneration', 'Conduct & POSH'],
    'Compliance': ['Regulatory Compliance', 'KYC & AML', 'Registration & Licensing', 'Compliance Testing', 'Regulatory Liaison & Inspections'],
    'Returns & Reporting': ['Supervisory Returns', 'Statutory Reporting', 'Event Reporting', 'MIS & Board Reporting'],
    'Risk Management': ['Credit Risk', 'Market Risk', 'Liquidity Risk', 'Operational Risk', 'ICAAP & Stress Testing', 'Risk Governance'],
    # family departments
    'Credit': ['Credit Appraisal & Sanction', 'Credit Administration & Documentation', 'Credit Monitoring', 'Asset Classification & Provisioning'],
    'Internal Audit & Inspection': ['Risk-based Internal Audit', 'Concurrent Audit', 'Inspection Follow-up', 'Audit Committee Support'],
    'Customer Service & Grievance': ['Grievance Redressal', 'Customer Communication & Disclosure', 'Fair Practices', 'Internal Ombudsman'],
    'Information Security': ['Cyber Security Governance', 'Security Operations', 'Identity & Access Management', 'Incident Response'],
    'KYC & AML': ['Customer Due Diligence', 'Transaction Monitoring', 'Regulatory Reporting to FIU', 'Sanctions Screening'],
    'Collections & Recovery': ['Collections Conduct', 'Recovery Agents Management', 'Legal Recovery & SARFAESI', 'Settlement & Write-off'],
    'Internal Audit': ['Audit Planning', 'Audit Execution', 'Audit Reporting', 'Audit Follow-up'],
    'Acquisition & Resolution': ['Asset Acquisition', 'Resolution Planning', 'Realisation & Distribution', 'Valuation of Acquired Assets'],
    'Trusteeship & SR Management': ['Trust Administration', 'Security Receipt Issuance', 'Investor Reporting (SR)', 'Trust Accounting'],
    'Credit & Recovery': ['Member Loans', 'Loan Documentation', 'Overdue Recovery', 'Loan Monitoring'],
    'Membership & Elections': ['Membership Register', 'Elections', 'Member Rights', 'Share Capital (Members)'],
    'Audit': ['Statutory Audit (Co-op)', 'Internal / Concurrent Audit (Co-op)', 'Audit Rectification', 'Audit Classification'],
    'Member Services & Grievance': ['Member Grievances', 'Member Communication', 'Deposit Services', 'Member Records'],
    'Business Operations': ['Core Operations', 'Process Controls', 'Service Delivery', 'Operational Records'],
    'Investment Team': ['Investment Process', 'Portfolio Monitoring', 'Conflicts of Interest', 'Investment Committee'],
    'Valuation': ['Valuation Policy', 'Periodic Valuation', 'Independent Valuer Management', 'Valuation Reporting'],
    'Investor Relations': ['Investor Onboarding', 'Investor Reporting', 'Investor Disclosures', 'Investor Communication'],
    'Fund Management & Investments': ['Investment Decision Making', 'Investment Limits Monitoring', 'Dealing & Execution', 'Scheme Management'],
    'Investor Services': ['Investor Servicing', 'Unitholder Records', 'Investor Charter', 'Transfer Agency Oversight'],
    'Secretarial': ['Meetings & Minutes', 'Statutory Registers', 'ROC Filings', 'Shareholder Matters'],
    'Asset Management': ['Asset Operations', 'Asset Valuation', 'Leasing & Tenancy', 'Project / SPV Management'],
    'Client Onboarding & KYC': ['Client Onboarding', 'KYC Maintenance', 'Client Categorisation', 'Account Closure'],
    'Surveillance': ['Trade Surveillance', 'Insider Trading Surveillance', 'Alerts Disposal', 'Surveillance Reporting'],
    'Investor Grievance': ['Complaint Handling', 'SCORES / ODR', 'Grievance Reporting', 'Root-cause Analysis'],
    'Actuarial': ['Valuation of Liabilities', 'Solvency', 'Pricing & Product Filing', 'Appointed Actuary Reporting'],
    'Underwriting': ['Underwriting Policy', 'Risk Acceptance', 'Reinsurance Placement', 'Underwriting Controls'],
    'Claims': ['Claims Registration', 'Claims Assessment', 'Claims Settlement', 'Claims Reporting'],
    'Investments': ['Investment Policy', 'Investment Limits', 'Investment Operations', 'Investment Reporting'],
    'Policyholder Servicing & Grievance': ['Policy Servicing', 'Policyholder Grievances', 'Policyholder Disclosures', 'Free-look & Cancellation'],
    'Sales & Distribution': ['Distribution Channels', 'Sales Conduct', 'Commission & Remuneration', 'Distributor Due Diligence'],
    'Claims Support': ['Claims Assistance', 'Claims Documentation', 'Claims Tracking', 'Claims Escalation'],
    'Policyholder Grievance': ['Complaint Intake', 'Complaint Resolution', 'Ombudsman Liaison', 'Complaint MIS'],
    'Tax': ['Direct Tax', 'Indirect Tax (GST)', 'TDS / TCS', 'Tax Litigation & Assessments'],
    'Privacy Office (DPO)': ['Consent & Notice', 'Data Principal Rights', 'Breach Management', 'Privacy Impact Assessment'],
    'Marketing': ['Advertising & Communication', 'Digital Marketing', 'Campaign Approvals', 'Marketing Consent'],
    'Product & Engineering': ['Product Design', 'Secure Development', 'Data & Model Engineering', 'Product Change Control'],
    'IT Infrastructure': ['Data Centre & Cloud', 'Network Management', 'Backup & Recovery', 'Asset Inventory'],
    'Application Development': ['Application Lifecycle', 'Code Review & Testing', 'Release Management', 'Application Security'],
    'Business Continuity': ['BCP Framework', 'DR Drills', 'Crisis Management', 'Resilience Testing'],
    'Payroll': ['Payroll Processing', 'Statutory Deductions', 'Payroll Returns', 'Payroll Records'],
    'Administration & Facilities': ['Premises & Licences', 'Health & Safety', 'Records Management', 'Facility Vendors'],
    'Internal Committee (POSH)': ['IC Constitution', 'Complaint Inquiry', 'Awareness & Training', 'Annual Report (POSH)'],
    'Accounts Payable': ['Vendor Invoices', 'Payments', 'Vendor Tax Compliance', 'Payables Reconciliation'],
    'Billing & Receivables': ['Invoicing', 'Collections (Receivables)', 'Credit Notes', 'Receivables Reconciliation'],
}
SPECIFIC_SUB = {  # Part-2 master §10A sub-function examples first, then platform additions
    'Board & Committees': ['Board composition', 'Board meetings', 'Committee constitution', 'Committee meetings', 'Board evaluation', 'Board reporting'],
    'Secretarial': ['Statutory registers', 'RoC filings', 'General meetings', 'Notices and agenda', 'Minutes'],
    'Policies & Codes': ['Policy approval', 'Policy review', 'Codes of conduct', 'Policy register'],
    'Fit & Proper': ['Director due diligence', 'KMP appointment', 'Fit and proper declarations', 'Regulator intimation'],
    'Accounting & Financial Reporting': ['Financial statements', 'Provisioning', 'Ind AS', 'Audit liaison'],
    'Capital Management': ['Capital adequacy', 'NOF', 'Dividend', 'Capital planning'],
    'Treasury & Investments': ['Investments', 'Borrowings', 'Liquidity management', 'ALM'],
    'Taxation': ['Direct tax', 'GST', 'TDS / TCS', 'Tax filings'],
    'Litigation': ['Suits and claims', 'Arbitration', 'Regulatory proceedings', 'Legal notices'],
    'Contracts & Documentation': ['Contract review', 'Loan documentation', 'Vendor contracts', 'Document custody'],
    'Recovery Proceedings': ['SARFAESI', 'Arbitration (recovery)', 'DRT / civil recovery', 'Insolvency (IBC)'],
    'IT Governance': ['IT strategy committee', 'IT policy', 'IT risk assessment', 'IT audit'],
    'Information Security & Cyber': ['Access control', 'Incident reporting', 'Vulnerability management', 'Security monitoring'],
    'IT Operations': ['Business continuity', 'Change management', 'Backup and recovery', 'Capacity and availability'],
    'IT Outsourcing': ['Vendor oversight', 'Cloud arrangements', 'Vendor risk assessment', 'Exit planning'],
    'Lending / Business Operations': ['Sanction', 'Disbursement', 'Post-disbursement monitoring', 'Operational controls'],
    'Customer Service & Grievance': ['Grievance redress', 'Internal Ombudsman', 'Complaint MIS', 'Customer requests'],
    'Fair Practices & Conduct': ['Disclosures to customers', 'Fair practices code', 'Pricing and charges', 'Product suitability'],
    'Recovery & Collections': ['Recovery agents', 'Collection practices', 'Repossession', 'Settlements'],
    'Outsourcing': ['Outsourcing register', 'Materiality assessment', 'Due diligence', 'Ongoing monitoring', 'Exit and termination'],
    'Recruitment & Appointments': ['Background checks', 'Appointment letters', 'Onboarding', 'Staff fit and proper'],
    'Training': ['Mandatory training', 'Certification', 'Training records'],
    'Remuneration': ['Remuneration policy', 'Variable pay and clawback', 'Payroll compliance'],
    'Conduct & POSH': ['Code of conduct', 'Internal Committee', 'Whistle-blower', 'Disciplinary process'],
    'Regulatory Compliance': ['Compliance monitoring', 'Regulatory correspondence', 'Compliance reporting', 'Regulatory change'],
    'KYC & AML': ['CDD', 'Transaction monitoring', 'STR / CTR', 'Sanctions screening', 'Periodic KYC update'],
    'Registration & Licensing': ['Licence conditions', 'Registrations and renewals', 'Regulatory approvals'],
    'Compliance Testing': ['Compliance testing plan', 'Sample testing', 'Issue tracking'],
    'Supervisory Returns': ['Periodic returns', 'Monthly returns', 'Quarterly returns', 'Annual returns', 'Return validation and sign-off'],
    'Statutory Reporting': ['Credit information reporting', 'Statutory filings', 'Filing acknowledgements'],
    'Event Reporting': ['FIU-IND reporting', 'Incident / fraud reporting', 'Regulatory intimations'],
    'Credit Risk': ['Exposure limits', 'Concentration', 'Credit monitoring', 'Expected credit loss'],
    'Market Risk': ['Market risk limits', 'Interest rate risk', 'Valuation'],
    'Liquidity Risk': ['ALM', 'LCR', 'Liquidity stress testing', 'Contingency funding plan'],
    'Operational Risk': ['Loss events', 'RCSA', 'KRIs', 'Fraud risk'],
    'ICAAP & Stress Testing': ['ICAAP', 'Stress tests', 'Capital planning'],
    'Risk Governance': ['Risk committee', 'Risk appetite', 'Risk policy', 'CRO function'],
    'Customer Due Diligence': ['Customer identification', 'Risk categorisation', 'Periodic KYC update', 'Enhanced due diligence', 'CKYCR upload'],
    'Regulatory Reporting to FIU': ['CTR', 'STR', 'CCR / NTR', 'Cross-border wire transfer reports', 'Principal Officer / Designated Director'],
    'Grievance Redressal': ['Complaint registration', 'Resolution and TAT', 'Escalation', 'Grievance MIS', 'Root-cause analysis'],
    'Credit Monitoring': ['Early warning signals', 'SMA reporting', 'Stock / book debt audit', 'Large exposure monitoring'],
    'Asset Classification & Provisioning': ['NPA identification', 'Upgradation', 'Provisioning', 'Expected credit loss'],
    'Cyber Security Governance': ['Cyber policy', 'Board / IT Strategy Committee oversight', 'CISO function', 'Cyber audit'],
    'Incident Response': ['Detection and triage', 'CERT-In / regulator reporting', 'Root-cause and remediation', 'Post-incident review'],
    'Breach Management': ['Breach detection', 'Intimation to Board / data principals', 'Containment', 'Breach register'],
}


def sub_functions(fn):
    return SPECIFIC_SUB.get(fn, GENERIC_SUB)


def function_matrix(depts):
    """(dept -> functions, function -> subfunctions) for a family; every family department gets functions."""
    fmap, smap = {}, {}
    for d in depts:
        fns = FUNCTIONS.get(d)
        assert fns, f'No functions for department {d!r}'
        fmap[d] = fns
        for fn in fns:
            smap.setdefault(fn, sub_functions(fn))
    return fmap, smap


# ------------------------------------------------------------------ Risk and Governance registers (D-57)
R = []


def rcol(group, header, key, by, at, lst, width, rule, multi=False, soft=False):
    R.append(dict(group=group, header=header, key=key, by=by, at=at, list=lst, width=width, multi=multi, rule=rule, ext=False, soft=soft))


RISK_GROUPS = [('LIST', 'LIST VIEW', 'FFF2CC'), ('SOURCE', 'TAXONOMY & SOURCE', 'E2EFDA'), ('ASSESS', 'ASSESSMENT', 'DDEBF7'),
               ('TREAT', 'TREATMENT', 'FCE4D6'), ('REVIEW', 'REVIEW', 'E4DFEC'), ('SYSTEM', 'SYSTEM', 'EDEDED')]
# Appendix H §H.2.1 Level-1 codes (the TAXO segment of RiskIDs); AIG added for AI-governance risk pending the X7 decision (Appendix H uses MOD for model risk)
TAXO_L1 = OrderedDict([('CRD', 'Credit risk'), ('CON', 'Concentration risk'), ('CCR', 'Counterparty credit risk'), ('MKT', 'Market and investment risk'),
                       ('IRB', 'Interest-rate risk in the banking book'), ('LIQ', 'Liquidity and funding risk'), ('CAP', 'Capital and solvency risk'),
                       ('OPR', 'Operational risk'), ('CYB', 'Cyber and technology risk'), ('TPR', 'Third-party and outsourcing risk'), ('MOD', 'Model risk'),
                       ('CMP', 'Compliance and legal risk'), ('CND', 'Conduct risk'), ('FRD', 'Fraud and financial-crime risk'), ('STR', 'Strategic and business risk'),
                       ('REP', 'Reputational risk'), ('GRP', 'Group and contagion risk'), ('PPL', 'People risk'), ('DPR', 'Data-privacy risk'),
                       ('RES', 'Resilience and continuity risk'), ('ESG', 'ESG and climate risk'), ('GOV', 'Governance risk'), ('INS', 'Insurance risk'),
                       ('ARC', 'Asset reconstruction risk'), ('FND', 'Fund and investment-management risk'), ('AIG', 'AI governance risk [pending X7]')])
TAXO = list(TAXO_L1)
RISK_CATEGORY = [v.replace(' [pending X7]', '') for v in TAXO_L1.values()]
BASEL = ['OPR.01 Internal fraud', 'OPR.02 External fraud', 'OPR.03 Employment practices and workplace safety', 'OPR.04 Clients, products and business practices',
         'OPR.05 Damage to physical assets', 'OPR.06 Business disruption and system failures', 'OPR.07 Execution, delivery and process management',
         'Not an operational-risk event type']
RATING = ['Critical', 'High', 'Medium', 'Low']
SCALE5 = ['5 - Almost Certain / Severe', '4 - Likely / Major', '3 - Possible / Moderate', '2 - Unlikely / Minor', '1 - Rare / Insignificant']
RISK_STATUS = ['Open', 'Under Treatment', 'Accepted', 'Transferred', 'Closed', 'Retired']
CTRL_EFF = ['Effective', 'Partially Effective', 'Ineffective', 'Not Tested']
APPETITE = ['Within Appetite', 'At Tolerance Limit', 'Outside Appetite']
RESPONSE = ['Mitigate', 'Accept', 'Transfer', 'Avoid']
ACTION_STATUS = ['Not Started', 'In Progress', 'Completed', 'Overdue', 'Cancelled']
REVIEW_FREQ = ['Monthly', 'Quarterly', 'Half Yearly', 'Annually']
TREND = ['Increasing', 'Stable', 'Decreasing', 'New']

rcol('LIST', 'S. No.', 'sno', 'Author', 'Required', None, 6, 'Integer 1..n.')
rcol('LIST', 'RiskID', 'risk_id', 'System', 'Blank', None, 18, 'Leave blank; assigned RSK-<TENANT4>-<NNNNN> (tenant) or RSKL-<TAXO>-<NNNN> (library) on import (D-51, NN-56).')
rcol('LIST', 'Risk Title', 'risk_title', 'Author', 'Required', None, 40, 'Short statement: "Risk that <event> caused by <cause> resulting in <consequence>".')
rcol('LIST', 'Risk Category', 'risk_category', 'Author', 'Required', 'RCat', 18, 'Level-1 risk category.')
rcol('LIST', 'Department', 'department', 'Author', 'Required', 'Dept', 22, 'Owning department.')
rcol('LIST', 'Risk Owner', 'risk_owner', 'User', 'Required', None, 20, 'Named owner (user e-mail in the tool).')
rcol('LIST', 'Inherent Rating', 'inherent_rating', 'Author', 'Required', 'Rating', 11, 'Critical / High / Medium / Low from likelihood × impact before controls (Appendix H §H.11 bands: 1–4 Low, 5–9 Medium, 10–15 High, 16–25 Critical).')
rcol('LIST', 'Residual Rating', 'residual_rating', 'Author', 'Required', 'Rating', 11, 'Critical / High / Medium / Low after controls.')
rcol('LIST', 'Status', 'risk_status', 'User', 'Required', 'RStatus', 14, 'Open / Under Treatment / Accepted / Transferred / Closed / Retired.')
rcol('SOURCE', 'Taxonomy Code', 'taxo_code', 'Author', 'Required', 'Taxo', 10, 'Appendix H §H.2.1 Level-1 code; becomes the TAXO segment of the library RiskID.')
rcol('SOURCE', 'Taxonomy L2 Code', 'taxo_l2', 'Author', 'Optional', None, 22, 'Appendix H Level-2 code and name, e.g. "CND.03 Recovery conduct".')
rcol('SOURCE', 'Basel Event Type', 'basel_event', 'Author', 'Optional', 'Basel', 26, 'Basel operational-risk event type, where applicable.')
rcol('SOURCE', 'Library RiskID', 'library_risk_id', 'Author', 'Optional', None, 16, 'RSKL- library item this tenant risk derives from.')
rcol('SOURCE', 'Source Instruments / Regulatory Mapping', 'reg_reference', 'Author', 'Optional', None, 32, 'Instruments or standards that make the risk relevant (directions, BCBS principles, ISO 31000) with official links; Pillar 1 / Pillar 2 treatment.')
rcol('SOURCE', 'Applicable Entity Families', 'families', 'Author', 'Optional', None, 20, 'LDC family codes separated by "; ".', multi=True)
rcol('SOURCE', 'Date Identified', 'date_identified', 'Author', 'Required', 'date', 13, 'Date first recorded.')
rcol('SOURCE', 'Risk Last Updated On', 'risk_updated_date', 'Author', 'Required', 'date', 13, 'Date of the last change to this risk record.')
rcol('ASSESS', 'Risk Description', 'description', 'Author', 'Required', None, 40, 'Full description.')
rcol('ASSESS', 'Causes', 'causes', 'Author', 'Optional', None, 30, 'Root causes / drivers.')
rcol('ASSESS', 'Consequences', 'consequences', 'Author', 'Optional', None, 30, 'Financial, regulatory, customer and reputational consequences.')
rcol('ASSESS', 'Inherent Likelihood', 'inh_likelihood', 'Author', 'Required', 'Scale', 18, '1–5 scale.')
rcol('ASSESS', 'Inherent Impact', 'inh_impact', 'Author', 'Required', 'Scale', 18, '1–5 scale.')
rcol('ASSESS', 'Key Controls (Control IDs)', 'control_ids', 'Author/User', 'Optional', None, 22, 'CTL-<TENANT4>-<NNNNN> separated by "; ".')
rcol('ASSESS', 'Control Effectiveness', 'control_eff', 'User', 'Optional', 'CtrlEff', 16, 'Effective / Partially Effective / Ineffective / Not Tested.')
rcol('ASSESS', 'Residual Likelihood', 'res_likelihood', 'Author', 'Required', 'Scale', 18, '1–5 scale after controls.')
rcol('ASSESS', 'Residual Impact', 'res_impact', 'Author', 'Required', 'Scale', 18, '1–5 scale after controls.')
rcol('ASSESS', 'Risk Appetite Position', 'appetite', 'User', 'Optional', 'Appetite', 16, 'Within Appetite / At Tolerance Limit / Outside Appetite.')
rcol('ASSESS', 'KRIs (KRI IDs)', 'kri_ids', 'Author/User', 'Optional', None, 20, 'KRI-<TENANT4>-<NNNNN> separated by "; ".')
rcol('ASSESS', 'KRI Thresholds', 'kri_thresholds', 'Author/User', 'Optional', None, 24, 'Green / Amber / Red thresholds per KRI.')
rcol('ASSESS', 'Linked CompIDs', 'linked_comp_ids', 'Author/User', 'Optional', None, 24, 'CompIDs whose non-compliance would crystallise this risk, separated by "; ".')
rcol('ASSESS', 'Linked GovIDs', 'linked_gov_ids', 'Author/User', 'Optional', None, 20, 'GovIDs separated by "; ".')
rcol('TREAT', 'Risk Response', 'response', 'User', 'Optional', 'Response', 12, 'Mitigate / Accept / Transfer / Avoid.')
rcol('TREAT', 'Action Plan', 'action_plan', 'User', 'Optional', None, 36, 'Actions to bring residual risk within appetite.')
rcol('TREAT', 'Action Owner', 'action_owner', 'User', 'Optional', None, 20, 'Owner of the action plan.')
rcol('TREAT', 'Action Due Date', 'action_due', 'User', 'Optional', 'date', 13, 'Target date.')
rcol('TREAT', 'Action Status', 'action_status', 'User', 'Optional', 'ActStatus', 14, 'Action status.')
rcol('REVIEW', 'Review Frequency', 'review_freq', 'Author', 'Required', 'RevFreq', 13, 'How often the owner must review.')
rcol('REVIEW', 'Last Review Date', 'last_review', 'User', 'Blank', 'date', 13, 'Date of the last review.')
rcol('REVIEW', 'Next Review Date', 'next_review', 'System', 'Blank', 'date', 13, 'Computed from the last review and frequency.')
rcol('REVIEW', 'Trend', 'trend', 'User', 'Blank', 'Trend', 12, 'Increasing / Stable / Decreasing / New.')
rcol('REVIEW', 'Comments by Risk Owner', 'owner_comments', 'User', 'Blank', None, 30, 'Owner commentary.')
rcol('REVIEW', 'Comments by CRO / Risk Function', 'cro_comments', 'User', 'Blank', None, 30, 'Second-line challenge.')
rcol('REVIEW', 'Comments by Auditor', 'auditor_comments', 'User', 'Blank', None, 30, 'Third-line observations.')
rcol('SYSTEM', 'Record Version', 'version', 'System', 'Blank', None, 9, 'Version of the risk record.')
rcol('SYSTEM', 'RAG', 'rag', 'System', 'Blank', 'RAG', 8, 'Red = residual Critical/High outside appetite or review overdue; Amber = High within appetite or review due ≤ 15 days; Green otherwise; Grey = Closed / Retired.')
rcol('SYSTEM', 'Days to Next Review', 'days_to_review', 'System', 'Blank', None, 9, 'Next Review Date minus export date.')
RISK_COLUMNS = R


def risk_lists(depts):
    return {'RCat': RISK_CATEGORY, 'Dept': depts, 'Rating': RATING, 'RStatus': RISK_STATUS, 'Taxo': TAXO, 'Basel': BASEL,
            'Scale': SCALE5, 'CtrlEff': CTRL_EFF, 'Appetite': APPETITE, 'Response': RESPONSE, 'ActStatus': ACTION_STATUS,
            'RevFreq': REVIEW_FREQ, 'Trend': TREND, 'RAG': RAG}


G = []


def gcol(group, header, key, by, at, lst, width, rule, multi=False, soft=False):
    G.append(dict(group=group, header=header, key=key, by=by, at=at, list=lst, width=width, multi=multi, rule=rule, ext=False, soft=soft))


GOV_GROUPS = [('LIST', 'LIST VIEW', 'FFF2CC'), ('SOURCE', 'SOURCE & VERSION', 'E2EFDA'), ('APPLIC', 'APPLICABILITY', 'DDEBF7'),
              ('DETAIL', 'REQUIREMENT DETAIL', 'FCE4D6'), ('WORKFLOW', 'WORKFLOW', 'E4DFEC'), ('SYSTEM', 'SYSTEM', 'EDEDED')]
GOV_BODY = ['Board', 'Board of Management', 'Audit Committee', 'Nomination and Remuneration Committee', 'Risk Management Committee', 'Stakeholders Relationship Committee',
            'CSR Committee', 'IT Strategy Committee', 'Other Board Committee', 'General Meeting (AGM / EGM)', 'KMP / Senior Management',
            'Office Bearers (Co-op / Society)', 'Managing Committee (Co-op / Society)', 'Trustees', 'Designated Partners (LLP)']
GOV_AREA = ['Meetings', 'Minutes', 'Resolutions', 'Statutory Registers', 'Filings', 'Policies', 'Committees', 'Director Events', 'KMP Events',
            'Declarations & Disclosures', 'Related Party Transactions', 'Shareholder / Member Matters', 'Board Evaluation', 'Secretarial Audit']
GOV_TYPE = ['MTG', 'AGD', 'MIN', 'RES', 'REG', 'FIL', 'POL', 'COM', 'DIR', 'KMP', 'DEC']
MEETING_TYPE = ['Board Meeting', 'Committee Meeting', 'Annual General Meeting', 'Extraordinary General Meeting', 'Meeting of Independent Directors',
                'Creditors / Debenture-holders Meeting', 'General Body Meeting (Co-op)', 'Not a meeting item']
RES_TYPE = ['Board Resolution', 'Circular Resolution', 'Ordinary Resolution', 'Special Resolution', 'Resolution by Postal Ballot',
            'Committee Resolution', 'Not applicable']
GOV_AUTH = ['MCA / Registrar of Companies', 'ICSI (Secretarial Standards)', 'SEBI (LODR)', 'RBI', 'IRDAI', 'IFSCA',
            'Registrar of Co-operative Societies', 'Central Registrar (MSCS)', 'Other']
GOV_STATUS = ['Not Started', 'Scheduled', 'In Progress', 'Completed', 'Completed Late', 'Not Completed', 'Not Applicable']

gcol('LIST', 'S. No.', 'sno', 'Author', 'Required', None, 6, 'Integer 1..n.')
gcol('LIST', 'GovID', 'gov_id', 'System', 'Blank', None, 22, 'Leave blank; assigned GOVL-<AUTH>-<NNNN> (library) or GOV-<TENANT4>-<TYPE>-<NNNNN> (tenant) on import.')
gcol('LIST', 'Governance Requirement / Action', 'requirement', 'Author', 'Required', None, 55, 'The governance action, phrased as a closed question or an imperative.')
gcol('LIST', 'Section / Clause / Standard', 'clause_ref', 'Author', 'Required', None, 18, 'e.g., s.173(1) Companies Act, 2013; SS-1 para 2.1; Reg. 17(2) LODR.')
gcol('LIST', 'Governing Body', 'gov_body', 'Author', 'Required', 'GovBody', 22, 'Board / named Committee / General Meeting / KMP / Office Bearers from the list; another body may be typed (warning).', soft=True)
gcol('LIST', 'Timing & Frequency', 'frequency', 'Author', 'Required', 'Freq', 18, 'Frequency list value, optionally followed by " — " and the timing rule in the Part-2 §7A grammar (e.g., "Quarterly — at least four a year; gap ≤ 120 days").', soft=True)
gcol('LIST', 'Date of Completion', 'act_date', 'User', 'Blank', 'date', 13, 'Date the governance action was completed.')
gcol('LIST', 'Status', 'status', 'User', 'Blank', 'GStatus', 16, 'Governance status.')
gcol('LIST', 'Risk Category', 'risk_level', 'Author', 'Required', 'Risk', 10, 'High / Medium / Low.')
gcol('SOURCE', 'Statute / Standard / Regulator', 'authority', 'Author', 'Required', 'GAuth', 22, 'Source authority.')
gcol('SOURCE', 'Name of Instrument', 'instrument_name', 'Author', 'Required', None, 36, 'e.g., Companies Act, 2013; Secretarial Standard on Meetings of the Board of Directors (SS-1).')
gcol('SOURCE', 'Instrument Reference No.', 'instrument_ref', 'Author', 'Optional', None, 18, 'Notification / circular number.')
gcol('SOURCE', 'Issue Date of Instrument', 'instrument_issue_date', 'Author', 'Optional', 'date', 13, 'Date of issue.')
gcol('SOURCE', 'Instrument Last Amended On', 'instrument_amended_date', 'Author', 'Optional', 'date', 13, 'Latest amendment incorporated.')
gcol('SOURCE', 'Requirement Last Updated On', 'question_updated_date', 'Author', 'Required', 'date', 13, 'Date of the change that last affected this row.')
gcol('SOURCE', 'Change Status', 'change_status', 'Author', 'Required', 'Change', 12, 'New / Amended / Unchanged / Re-cited / Retired.')
gcol('SOURCE', 'Source Link', 'source_url', 'Author', 'Optional', None, 28, 'Official URL.')
gcol('APPLIC', 'Entity Family / Class', 'applic_type', 'Author', 'Required', None, 22, 'LDC family codes or entity classes separated by "; ".', multi=True)
gcol('APPLIC', 'Conditions / Thresholds', 'conditions', 'Author', 'Required', None, 30, 'e.g., listed companies only; paid-up capital ≥ threshold.')
gcol('APPLIC', 'Applicable From', 'applic_from', 'Author', 'Optional', 'date', 13, 'Effective date.')
gcol('APPLIC', 'Applicable Until', 'applic_to', 'Author', 'Optional', 'date', 13, 'Sunset date.')
gcol('DETAIL', 'Governance Area', 'gov_area', 'Author', 'Required', 'GovArea', 18, 'Area of governance.')
gcol('DETAIL', 'GovID Type', 'gov_type', 'Author', 'Required', 'GovType', 9, 'MTG, AGD, MIN, RES, REG, FIL, POL, COM, DIR, KMP, DEC (used in the tenant GovID).')
gcol('DETAIL', 'Meeting Type', 'meeting_type', 'Author', 'Optional', 'MeetType', 20, 'Meeting type where relevant.')
gcol('DETAIL', 'Notice Period', 'notice_period', 'Author', 'Optional', None, 16, 'e.g., 7 days (Board); 21 clear days (AGM).')
gcol('DETAIL', 'Quorum', 'quorum', 'Author', 'Optional', None, 16, 'Quorum requirement.')
gcol('DETAIL', 'Documents (Notice / Agenda / Papers / Minutes)', 'documents', 'Author', 'Optional', None, 30, 'Documents to prepare and circulate.')
gcol('DETAIL', 'Resolution Type', 'resolution_type', 'Author', 'Optional', 'ResType', 18, 'Type of resolution.')
gcol('DETAIL', 'Register to Update', 'register', 'Author', 'Optional', None, 20, 'Statutory register affected.')
gcol('DETAIL', 'Filing / Form and Due Rule', 'filing_rule', 'Author', 'Optional', None, 28, 'e.g., MGT-14 within 30 days of passing the resolution.')
gcol('DETAIL', 'Responsible Role', 'responsible_role', 'Author', 'Required', None, 18, 'Company Secretary, Compliance Officer, Chair, etc.')
gcol('DETAIL', 'Evidence', 'evidence', 'Author', 'Required', None, 28, 'Artefacts proving completion.')
gcol('DETAIL', 'Linked CompIDs', 'linked_comp_ids', 'Author/User', 'Optional', None, 22, 'CompIDs separated by "; ".')
gcol('DETAIL', 'Linked RiskIDs', 'linked_risk_ids', 'Author/User', 'Optional', None, 18, 'RiskIDs separated by "; ".')
gcol('DETAIL', 'Explanation', 'explanation', 'Author', 'Required', None, 40, 'Plain-language explanation.')
gcol('WORKFLOW', 'Preparer', 'preparer', 'User', 'Blank', None, 20, 'Preparer (maker).')
gcol('WORKFLOW', 'Reviewer', 'reviewer', 'User', 'Blank', None, 20, 'Reviewer (checker).')
gcol('WORKFLOW', 'Approver', 'approver', 'User', 'Blank', None, 20, 'Approver (Chair / Board / Committee).')
gcol('WORKFLOW', 'Approval Date', 'approval_date', 'User', 'Blank', 'date', 13, 'Date of approval.')
gcol('WORKFLOW', 'Comments', 'comments', 'User', 'Blank', None, 30, 'Workflow comments.')
gcol('SYSTEM', 'Next Due Date', 'next_due', 'System', 'Blank', 'date', 13, 'Computed.')
gcol('SYSTEM', 'Days to Due', 'days_to_due', 'System', 'Blank', None, 9, 'Computed.')
gcol('SYSTEM', 'RAG', 'rag', 'System', 'Blank', 'RAG', 8, 'Same rules as the compliance register.')
gcol('SYSTEM', 'Record Version', 'version', 'System', 'Blank', None, 9, 'Version of the governance record.')
GOV_COLUMNS = G


def gov_lists():
    return {'GovBody': GOV_BODY, 'Freq': FREQ_EXT, 'GStatus': GOV_STATUS, 'Risk': RISK, 'GAuth': GOV_AUTH, 'Change': CHANGE,
            'GovArea': GOV_AREA, 'GovType': GOV_TYPE, 'MeetType': MEETING_TYPE, 'ResType': RES_TYPE, 'RAG': RAG}


# ------------------------------------------------------------------ legacy v1.0 -> v2.0 map (spec §4)
LEGACY_MAP = [('A', 'Checkbox', '(ignored)', ''), ('B', 'S. No.', 'sno', ''), ('C', 'General Applicability (Layer)', 'applic_layer', ''),
              ('D', 'General Applicability (Type)', 'applic_type', ''), ('E', 'CompID', 'comp_id', 'Kept as legacy alias if not in v2 format (NN-56)'),
              ('F', 'Short Title', 'short_title', ''), ('G', 'Compliance Question', 'question', ''), ('H', 'Due Date & Frequency', 'frequency', ''),
              ('I', 'Date of Compliance', 'act_date', ''), ('J', 'Status', 'status', 'Mapped to canonical label'), ('K', 'Clause / Para', 'clause_ref', ''),
              ('L', 'Interpretation', 'explanation', ''), ('M', 'Department', 'department', ''),
              ('N', 'Related Document / Weblinks', 'related_docs + weblinks', 'Split: tokens starting http(s):// go to weblinks'),
              ('O', 'Compliance Type', 'compliance_type', ''), ('P', 'Filing / Reporting', 'filing_details (+ due_rule)', 'Text after "Due:" moves to due_rule'),
              ('Q', 'Consequences', 'consequences', ''), ('R', 'Risk Categorisation', 'risk_level', ''), ('S', 'Conditional Applicability', 'conditions', ''),
              ('T', 'Maker User', 'maker', ''), ('U', 'Evidence', 'evidence', ''), ('V', 'Control Activity', 'control_activity', ''),
              ('W', 'Status Update by Maker', 'maker_status', ''), ('X', 'Comments by Maker', 'maker_comments', ''), ('Y', 'Checker User', 'checker', ''),
              ('Z', 'Filing / Compliance Date', 'act_date if blank, else approval_date', 'Import warning LDC-TPL-088 (P03)'),
              ('AA', 'Review: Approve / Reject / Reallocate', 'checker_decision', ''), ('AB', 'Comments by Checker', 'checker_comments', ''),
              ('AC', 'Assigned Auditor', 'auditor', ''), ('AD', 'Comments by Auditor', 'auditor_comments', '')]
