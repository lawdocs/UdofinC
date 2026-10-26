# -*- coding: utf-8 -*-
"""Emit the Appendix E Part A tables (contract v2.0) from v12_contract.py so the appendix never drifts from the templates.
Usage: python3 v12_appendix_tables.py > tables.md"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v12_contract as K  # noqa: E402
from openpyxl.utils import get_column_letter  # noqa: E402

LEN = {'question': '≤ 2,000', 'short_title': '≤ 200', 'explanation': '≤ 8,000', 'clause_ref': '≤ 500', 'instrument_name': '≤ 500', 'instrument_ref': '≤ 200',
       'change_note': '≤ 4,000', 'source_url': '≤ 1,000 (URL)', 'conditions': '≤ 4,000', 'due_rule': '≤ 500', 'filing_details': '≤ 1,000', 'filing_form': '≤ 100',
       'related_docs': '≤ 4,000', 'weblinks': '≤ 4,000', 'consequences': '≤ 4,000', 'penalty_ref': '≤ 500', 'evidence': '≤ 2,000', 'control_activity': '≤ 4,000',
       'checker_points': '≤ 2,000', 'audit_test': '≤ 2,000', 'tags': '≤ 500', 'risk_ids': '≤ 500', 'gov_ids': '≤ 500', 'maker_comments': '≤ 4,000',
       'checker_comments': '≤ 4,000', 'auditor_comments': '≤ 4,000'}
MAPS = {'sno': 'checkpoint_versions.sequence_no', 'comp_id': 'cnt.comp_id_registry.comp_id', 'question': 'question_text', 'clause_ref': 'citation_text + cnt.clauses link',
        'department': 'department_code', 'frequency': 'schedule_rules.frequency_code', 'act_date': '(tenant) compliance_instances.done_on', 'status': '(tenant) instance state',
        'risk_level': 'risk_code', 'authority': 'instruments.authority_code', 'instrument_name': 'instruments.title', 'instrument_ref': 'instruments.ref_no',
        'instrument_issue_date': 'instruments.issue_date', 'instrument_amended_date': 'instrument_versions.as_amended_upto', 'question_updated_date': 'checkpoint_versions.question_updated_date',
        'change_status': 'checkpoint_versions.change_status', 'change_note': 'checkpoint_versions.change_note (+ prev_question)', 'source_url': 'instrument_versions.source_url',
        'applic_layer': 'applicability axis C', 'applic_type': 'applicability axis D', 'conditions': 'conditions_text', 'applic_from': 'valid_from (law time)', 'applic_to': 'valid_to (law time)',
        'short_title': 'short_title', 'explanation': 'explanation', 'dept_function': 'function_code', 'dept_subfunction': 'subfunction_code', 'compliance_type': 'compliance_type_code',
        'due_rule': 'schedule_rules.due_rule', 'event_trigger': 'schedule_rules.event_key', 'filing_details': 'filing_requirements', 'filing_form': 'filing_requirements.form_code',
        'related_docs': 'obligation_references[]', 'weblinks': 'obligation_references[] (URL)', 'consequences': 'consequence_text', 'penalty_ref': 'penalty_ref',
        'risk_type': 'risk_type_codes[]', 'risk_ids': 'links → erm risks', 'gov_ids': 'links → gov register', 'evidence': 'evidence_requirements[]', 'control_activity': 'control_activity',
        'checker_points': 'checker_points', 'audit_test': 'audit_test', 'tags': 'tags[]'}


def md(rows):
    out = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '---|' * len(rows[0])]
    out += ['| ' + ' | '.join(str(x).replace('|', '\\|').replace('\n', ' ') for x in r) + ' |' for r in rows[1:]]
    return '\n'.join(out)


def lst(c):
    l = c['list']
    if not l:
        return '—'
    if l == 'date':
        return 'date'
    if l == 'FUNC':
        return 'dependent on Department'
    if l == 'SUBF':
        return 'dependent on Function'
    return f'`<PREFIX>_{l}`' + (' (multi)' if c['multi'] else '') + (' (soft)' if c.get('soft') else '')


def main():
    glabel = dict((g, l) for g, l, _ in K.GROUPS)
    rows = [['#', 'Group', 'Header (row 2, exact)', 'Key', 'Filled by', 'At authoring', 'List / validation', 'Length', 'Maps to (`cnt`)']]
    for i, c in enumerate(K.BASE_COLUMNS, 1):
        n = i
        rows.append([n, glabel[c['group']], c['header'], f"`{c['key']}`", c['by'], c['at'], lst(c), LEN.get(c['key'], '—'), MAPS.get(c['key'], 'tenant / system')])
        if c['key'] == K.APPLIC_EXT_AFTER:
            rows.append(['E1–E4', 'APPLICABILITY', 'family extension columns (§A.4)', '`ext_*`', 'Author', 'Conditional', 'family list', '≤ 500', 'applicability axis `ext_*`'])
    print('<!-- TABLE:COLUMNS -->')
    print(md(rows))
    print()
    rows = [['Family', 'Cols', 'Extension columns (key → header)', 'Values (Lists sheet)']]
    for f in K.all_families():
        e = K.EXT[f['code']]
        if not e:
            rows.append([f['code'], 62, '—', '—'])
            continue
        for j, (key, header, values, multi) in enumerate(e):
            vals = ('free text' if values is None else ('States and UTs (38 values)' if values is K.STATES else
                    ('ISO country names (%d values)' % len(values) if key == 'ext_country' else ' · '.join(values)))) + (' — multi' if multi else '')
            rows.append([f['code'] if j == 0 else '', 62 + len(e) if j == 0 else '', f'`{key}` → {header}', vals])
    print('<!-- TABLE:EXT -->')
    print(md(rows))
    print()
    print('<!-- TABLE:VOCAB -->')
    for title, v in [('Status (`status`)', K.STATUS), ('Status Update by Maker (`maker_status`)', K.MAKER_STATUS), ('Review — Approve / Reject / Reallocate (`checker_decision`)', K.DECISION),
                     ('Audit Result (`audit_result`)', K.AUDIT_RESULT), ('Change Status (`change_status`)', K.CHANGE), ('Risk Type (`risk_type`)', K.RISK_TYPE),
                     ('RAG (`rag`)', K.RAG), ('Tenant Overlay (`overlay`)', K.YESNO), ('Event Trigger (`event_trigger`) — seed catalogue; "Other: <event>" allowed with warning', K.EVENTS)]:
        print(f'- **{title}:** ' + ' · '.join(v))
    print()
    rows = [['Family group', 'Families', 'Regulator / Authority list (`<PREFIX>_Auth`, soft)']]
    groups = {}
    for f in K.all_families():
        groups.setdefault(K.family_group(f['code']), []).append(f['code'])
    for g, fs in groups.items():
        rows.append([g, ', '.join(fs), ' · '.join(K.AUTH_BY_GROUP[g])])
    print('<!-- TABLE:AUTH -->')
    print(md(rows))
    print()
    rows = [['Department', 'Functions (`<PREFIX>_FuncHdr` matrix)', 'Sub-functions (per Function; generic list where not specified)']]
    for d, fns in K.FUNCTIONS.items():
        rows.append([d, ' · '.join(fns), '; '.join(f"**{fn}:** " + ', '.join(K.SPECIFIC_SUB[fn]) for fn in fns if fn in K.SPECIFIC_SUB) or 'generic'])
    print('<!-- TABLE:FUNC -->')
    print(md(rows))
    print()
    print('Generic sub-function list: ' + ' · '.join(K.GENERIC_SUB))
    print()
    rows = [['Family', 'AUTH (default)', 'FAM (`fam_short`)', 'CompID pattern', 'Example']]
    for f in K.all_families():
        g = K.family_group(f['code'])
        auth = K.AUTH_CODE[g]
        fam = K.FAMILY_SHORT_CODE[f['code']]
        pat = ('<issuing AUTH>' if f['code'] in K.CROSS_AUTHORITY else auth) + f'-{fam}-<INST>-<NNNN>'
        rows.append([f['code'], auth + (' (issuer)' if f['code'] in K.CROSS_AUTHORITY else ''), fam, f'`{pat}`', f"`{K.COMPID_EXAMPLE[f['code']]}`"])
    print('<!-- TABLE:FAMSHORT -->')
    print(md(rows))
    print()
    rows = [['Code', 'Subject']] + [[f'`{k}`', v] for k, v in K.SUBJECT_ABBR.items()]
    print('<!-- TABLE:SUBJ -->')
    print(md(rows))
    print()
    for name, cols, groups_ in (('RISK', K.RISK_COLUMNS, K.RISK_GROUPS), ('GOV', K.GOV_COLUMNS, K.GOV_GROUPS)):
        gl = dict((g, l) for g, l, _ in groups_)
        rows = [['#', 'Col', 'Group', 'Header (row 2, exact)', 'Key', 'Filled by', 'At authoring', 'List / validation', 'Rule']]
        for i, c in enumerate(cols, 1):
            rows.append([i, get_column_letter(i), gl[c['group']], c['header'], f"`{c['key']}`", c['by'], c['at'], lst(c).replace('<PREFIX>', name), c['rule']])
        print(f'<!-- TABLE:{name} -->')
        print(md(rows))
        print()
    print('<!-- TABLE:RISKVOCAB -->')
    for t, v in [('Risk Category (Appendix H Level 1)', K.RISK_CATEGORY), ('Taxonomy Code', K.TAXO), ('Basel Event Type', K.BASEL), ('Rating', K.RATING), ('Likelihood / Impact scale', K.SCALE5),
                 ('Risk status', K.RISK_STATUS), ('Control effectiveness', K.CTRL_EFF), ('Appetite position', K.APPETITE), ('Response', K.RESPONSE), ('Action status', K.ACTION_STATUS),
                 ('Review frequency', K.REVIEW_FREQ), ('Trend', K.TREND)]:
        print(f'- **{t}:** ' + ' · '.join(v))
    print()
    print('<!-- TABLE:GOVVOCAB -->')
    for t, v in [('Governing Body (soft)', K.GOV_BODY), ('Governance Area', K.GOV_AREA), ('GovID Type', K.GOV_TYPE), ('Meeting Type', K.MEETING_TYPE), ('Resolution Type', K.RES_TYPE),
                 ('Statute / Standard / Regulator', K.GOV_AUTH), ('Status', K.GOV_STATUS)]:
        print(f'- **{t}:** ' + ' · '.join(v))
    print()
    rows = [['v1.0 col', 'v1.0 header', 'v2.0 key', 'Rule']] + [[a, b, f'`{k}`' if ' ' not in k else k, n or '—'] for a, b, k, n in K.LEGACY_MAP]
    print('<!-- TABLE:LEGACY -->')
    print(md(rows))


if __name__ == '__main__':
    main()
