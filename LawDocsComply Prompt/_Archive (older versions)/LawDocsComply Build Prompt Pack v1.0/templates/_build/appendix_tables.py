# -*- coding: utf-8 -*-
"""Generate Appendix E tables (§E.12 rows, §E.13 canonical codes, §E.15 vocabularies) from family_vocab."""
import re, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from family_vocab import FAMILIES, FREQ_EXT, DEPT_BASE, COMP_BASE

SHORT = {'RBI-SCB': 'Commercial Banks SFBs PBs LABs RRBs', 'RBI-UCB': 'Urban Co-operative Banks', 'RBI-RCB': 'Rural Co-operative Banks',
         'RBI-NBFC': 'NBFCs', 'RBI-ARC': 'Asset Reconstruction Companies', 'RBI-OTH': 'Other RBI Regulated Entities',
         'COOP-CCS': 'Credit Co-operative Societies', 'COOP-GEN': 'Other Co-operative Societies', 'IFSCA-GEN': 'IFSCA Regulated Entities',
         'IFSCA-FCFU': 'IFSCA Finance Companies and Units', 'IFSCA-FME': 'IFSCA Fund Management Entities', 'SEBI-MF': 'Mutual Funds',
         'SEBI-AIF': 'Alternative Investment Funds', 'SEBI-LISTED': 'Listed Entities', 'SEBI-REIT-INVIT': 'REITs and InvITs',
         'SEBI-INT': 'SEBI Intermediaries', 'IRDAI-INS': 'Insurers', 'IRDAI-INT': 'Insurance Intermediaries', 'MCA-CO': 'Companies',
         'MCA-LLP': 'LLPs', 'DATA-PRIV': 'Data Protection and Privacy', 'CYBER': 'Cyber Security', 'LAB-POSH': 'Labour Codes and POSH',
         'TAX-GST': 'GST and Direct Tax'}

def slug(v):
    m = re.search(r'\(([A-Za-z0-9\-/ ]{2,14})\)\s*$', v)
    s = m.group(1) if m else v
    s = s.replace('₹', 'INR').replace('≥', 'GE').replace('&', 'AND')
    s = re.sub(r'[^A-Za-z0-9]+', '_', s).strip('_').upper()
    return s[:40]

FREQ_CODES = dict(zip(FREQ_EXT, ['ANNUAL','HALF_YEARLY','QUARTERLY','MONTHLY','FORTNIGHTLY','WEEKLY','DAILY','EVENT','IMMEDIATE','CONTINUOUS','ONE_TIME','EVERY_2Y','EVERY_3Y','EVERY_5Y']))
DEPT_CODES = dict(zip(DEPT_BASE, ['GOV','FIN','LEG','IT','OPS','HR','CMP','RET','RSK']))
# Canonical department codes for family additions: Appendix U §U.9.0 (master X-10)
DEPT_ALIAS = {'Accounts Payable':'FIN','Acquisition & Resolution':'COL','Actuarial':'ACT','Administration & Facilities':'ADM','Application Development':'IT','Asset Management':'FMI','Audit':'IA','Billing & Receivables':'FIN','Business Continuity':'RSK','Business Operations':'OPS','Claims':'CLM','Claims Support':'CLM','Client Onboarding & KYC':'KYC','Collections & Recovery':'COL','Credit':'CRD','Credit & Recovery':'CRD','Customer Service & Grievance':'CSG','Fund Management & Investments':'FMI','IT Infrastructure':'IT','Information Security':'ISEC','Internal Audit':'IA','Internal Audit & Inspection':'IA','Internal Committee (POSH)':'ICP','Investment Team':'FMI','Investments':'TRY','Investor Grievance':'INV','Investor Relations':'INV','Investor Services':'INV','KYC & AML':'KYC','Marketing':'MKT','Member Services & Grievance':'MEM','Membership & Elections':'MEM','Payroll':'PRL','Policyholder Grievance':'CSG','Policyholder Servicing & Grievance':'CSG','Privacy Office (DPO)':'DPR','Product & Engineering':'PRD','Sales & Distribution':'BUS','Secretarial':'SECR','Surveillance':'SRV','Tax':'TAX','Trusteeship & SR Management':'TRS','Underwriting':'UND','Valuation':'VAL'}
COMP_CODES = dict(zip(COMP_BASE, ['POLICY','COMPLIANCE','RETURN_REPORT','COMMITTEE','INTERNAL','SUGGESTIVE']))

def esc(s): return str(s).replace('|', '\\|')

out = []
for i, f in enumerate(FAMILIES, 1):
    out.append(f"| {i} | {f['code']} | `LDC-TPL-{f['code']}-v1.0 - {SHORT[f['code']]}.xlsx` | {esc(f['regulator'])} | {f['c_label'].replace(' (Column C)','')} ({len(f['C'])}) | {f['d_label'].replace(' (Column D)','')} ({len(f['D'])}) | `{f['prefix']}_*` |")
out.append('')
out.append('List sizes (H / M / O / P): ' + '; '.join(f"{f['code']} {len(f['H'])}/{len(f['M'])}/{len(f['O'])}/{len(f['P'])}" for f in FAMILIES) + '.')
out.append('')
out.append('## E.13 Canonical code tables\n')
out.append('Canonical codes are what the platform stores and what other products receive (Ecosystem Spec §5.3 code tables). Display text can change through aliases without changing codes.\n')
out.append('### E.13.1 Frequency (Column H)\n')
out.append('| Display value | Code | Scheduler meaning |\n|---|---|---|')
mean = {'ANNUAL':'Once per financial year (tenant FY setting) unless a fixed date is set','HALF_YEARLY':'Twice per FY (H1/H2)','QUARTERLY':'Per FY quarter','MONTHLY':'Per calendar month','FORTNIGHTLY':'1st–15th and 16th–end of month (RBI convention) [INTERP]','WEEKLY':'Per ISO week','DAILY':'Per business day (tenant calendar)','EVENT':'Instance created when the linked event is recorded','IMMEDIATE':'Event instance with zero offset and urgent priority','CONTINUOUS':'Standing obligation; periodic attestation per `cmp.ongoing.attestation_frequency` (T, default QUARTERLY; P04)','ONE_TIME':'Single instance; re-opened only by an event (e.g., change in registration)','EVERY_2Y':'Every 2 FYs from anchor','EVERY_3Y':'Every 3 FYs from anchor','EVERY_5Y':'Every 5 FYs from anchor'}
for k, v in FREQ_CODES.items(): out.append(f'| {k} | `{v}` | {mean[v]} |')
out.append('\n### E.13.2 Department (Column M)\n')
out.append('Base departments (every family) and family additions. Tenants rename departments in Settings → Organisation → Departments; the canonical code is preserved for reporting, ecosystem exchange and exports.\n')
out.append('| Display value | Code | Base / addition | Families |\n|---|---|---|---|')
depts = {}
for f in FAMILIES:
    for d in f['M']: depts.setdefault(d, []).append(f['code'])
for d, fs in depts.items():
    code = DEPT_CODES.get(d) or DEPT_ALIAS[d]  # KeyError = name missing from Appendix U §U.9.0
    out.append(f"| {esc(d)} | `{code}` | {'Base' if d in DEPT_CODES else 'Addition'} | {'All' if len(fs)==len(FAMILIES) else ', '.join(fs)} |")
out.append('\n### E.13.3 Compliance type (Column O)\n')
out.append('| Display value | Code | Families | Workflow effect |\n|---|---|---|---|')
eff = {'POLICY':'Links to Policy register (P07); evidence = approved policy version','COMPLIANCE':'Standard maker-checker instance','RETURN_REPORT':'Links to Return Studio / filing tracker (P11); evidence = acknowledgement','COMMITTEE':'Links to Committee register (P06)','INTERNAL':'Internal control instance; testable in audit (P10)','SUGGESTIVE':'Optional; tenant may opt in; excluded from compliance score by default','REGISTERS_AND_RECORDS':'Links to statutory registers (P06/P13/P16)','DISCLOSURES':'Links to disclosure calendar; evidence = URL/filing','NOTICES_AND_CONSENTS':'Links to DPDP notice/consent module (P12)'}
types = {}
for f in FAMILIES:
    for o in f['O']: types.setdefault(o, []).append(f['code'])
for o, fs in types.items():
    code = COMP_CODES.get(o, slug(o))
    out.append(f"| {o} | `{code}` | {'All' if len(fs)==len(FAMILIES) else ', '.join(fs)} | {eff.get(code,'')} |")
out.append('\n### E.13.4 Risk (Column R)\n')
out.append('| Value | Code | Default score (1–5) used by ERM linkage (P08) |\n|---|---|---|\n| High | `HIGH` | 5 |\n| Medium | `MEDIUM` | 3 |\n| Low | `LOW` | 1 |')
out.append('\nScores are tenant-configurable (`erm.compliance_risk.score_map`, T) within bounds 1–5.')
out.append('\n### E.13.5 Taxonomy codes for Columns C and D\n')
out.append('Codes follow `<FAMILY>.<AXIS>.<SLUG>` (AXIS = `C` or `D`), are generated on family publication and are mapped by P15 to the entity taxonomy (`pack.entity_taxonomy`). Examples: ' + ', '.join(f"`{FAMILIES[3]['code']}.C.{slug(v)}`" for v in FAMILIES[3]['C'][:3]) + ', ' + ', '.join(f"`{FAMILIES[3]['code']}.D.{slug(v)}`" for v in FAMILIES[3]['D'][:3]) + '. The complete code list for every value is produced by `templates/_build/appendix_tables.py` and loaded by the P03 seed migration.')
open(sys.argv[1], 'w').write('\n'.join(out) + '\n')

# full vocab lists
v = ['## E.15 Family vocabularies (complete lists as built in v1.0)\n', 'Values are exact (case and punctuation). The P column lists are reference tokens that start Column P.\n']
for i, f in enumerate(FAMILIES, 1):
    v.append(f"### E.15.{i} {f['code']} — {f['name']}\n")
    v.append(f"- **C — {f['c_label'].replace(' (Column C)','')}:** " + '; '.join(f['C']))
    v.append(f"- **D — {f['d_label'].replace(' (Column D)','')}:** " + '; '.join(f['D']))
    v.append(f"- **H:** " + '; '.join(f['H']))
    v.append(f"- **M:** " + '; '.join(f['M']))
    v.append(f"- **O:** " + '; '.join(f['O']))
    v.append(f"- **R:** High; Medium; Low")
    v.append(f"- **P (reference):** " + '; '.join(f['P']))
    v.append('')
open(sys.argv[2], 'w').write('\n'.join(v) + '\n')
