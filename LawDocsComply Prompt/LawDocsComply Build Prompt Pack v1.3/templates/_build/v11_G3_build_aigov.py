# -*- coding: utf-8 -*-
"""v1.1 (G3): build the AI-GOV (AI governance overlay) question template without modifying the v1.0 scripts.

Usage: python3 v11_G3_build_aigov.py <owner_base_xlsx (Appointed Actuary sheet)> <out_dir>
Reuses build() from build_templates.py and base vocabularies from family_vocab.py (NN-35: base values kept, family values only added).
"""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import build_templates as bt  # noqa: E402
from family_vocab import FREQ_EXT, DEPT_BASE, COMP_BASE, ex  # noqa: E402

bt.SHORT['AI-GOV'] = 'AI Governance'

AIGOV = dict(
    code='AI-GOV',
    name='AI Governance and Responsible AI (RBI FREE-AI, RBI model risk, SEBI, IRDAI, IFSCA, MeitY, DPDP, EU AI Act, ISO/IEC 42001, NIST AI RMF)',
    regulator='RBI; SEBI; IRDAI; IFSCA; MeitY; Data Protection Board of India; EU AI Office and national market-surveillance authorities; voluntary standards bodies (ISO/IEC, NIST, IMDA)',
    prefix='AIGOV',
    c_label='Framework / Instrument (Column C)',
    C=['RBI FREE-AI Framework (Committee Report, Aug 2025)',
       'RBI Model Risk Management Guidance (draft, 2026)',
       'SEBI AI/ML guidance (securities market)',
       'IRDAI AI / technology guidance',
       'IFSCA AI / technology guidance',
       'MeitY India AI Governance Guidelines (Nov 2025)',
       'DPDP Act, 2023 and DPDP Rules, 2025 (AI processing of personal data)',
       'IT Act, 2000 and IT Rules (synthetic / AI-generated content)',
       'EU AI Act (Regulation (EU) 2024/1689)',
       'ISO/IEC 42001:2023 (AI management system)',
       'NIST AI RMF 1.0 and Generative AI Profile',
       'Singapore Model AI Governance Framework (incl. Agentic AI, 2026)',
       'Board-approved internal AI Policy',
       'Other jurisdiction',
       'All Frameworks'],
    d_label='Role / Entity Category (Column D)',
    D=['AI Deployer (entity using AI in its business)',
       'AI Developer / Provider (builds or sells AI systems)',
       'User of third-party AI service or model',
       'Agentic AI deployer (autonomous or semi-autonomous agents)',
       'RBI Regulated Entity (all categories)',
       'SEBI Regulated Entity / Intermediary',
       'Insurer / Insurance Intermediary',
       'IFSCA Regulated Entity',
       'Data Fiduciary processing personal data with AI',
       'EU high-risk AI system deployer',
       'EU general-purpose AI model provider',
       'Intermediary hosting AI-generated content',
       'All Roles (ALL)'],
    H=FREQ_EXT,
    M=DEPT_BASE + ['Information Security', 'Privacy Office (DPO)', 'Product & Engineering', 'Internal Audit', 'Customer Service & Grievance'],
    O=COMP_BASE + ['Notices & Consents'],
    P=['RBI (supervisory intimation / inspection)', 'SEBI (filing / reporting)', 'IRDAI', 'IFSCA', 'Data Protection Board of India', 'CERT-In',
       'EU AI Office / national market-surveillance authority', 'Affected customers (AI disclosure / notice)', 'Annual Report disclosure',
       'Board / Risk Management Committee', 'Independent AI auditor / assessor', 'Not Required'],
    instruments=['RBI, Report of the Committee to develop a Framework for Responsible and Ethical Enablement of Artificial Intelligence (FREE-AI) in the Financial Sector, 13 Aug 2025 — 7 Sutras; recommendations to REs incl. board-approved AI policy, AI inventory, disclosures, incident reporting, audits [VERIFY numbering against the report]',
                 'RBI draft Guidance on Regulatory Principles for Model Risk Management, 2026 (released Jun 2026; comments to 24 Jul 2026) [VERIFY final status]',
                 'SEBI consultation paper on guidelines for responsible usage of AI/ML in the securities market (20 Jun 2025) and any final circular [VERIFY]',
                 'MeitY India AI Governance Guidelines (5 Nov 2025)',
                 'Regulation (EU) 2024/1689 (AI Act) as amended by the Digital Omnibus on AI (political agreement 6 May 2026: Annex III high-risk from 2 Dec 2027; Annex I from 2 Aug 2028) [VERIFY publication]',
                 'ISO/IEC 42001:2023; ISO/IEC 23894:2023; ISO/IEC 42005:2025 (AI impact assessment) [VERIFY]',
                 'NIST AI RMF 1.0 (Jan 2023) and NIST AI 600-1 Generative AI Profile (Jul 2024)',
                 'IMDA Model AI Governance Framework for Agentic AI (22 Jan 2026)'],
    example=ex(B=1, C='RBI FREE-AI Framework (Committee Report, Aug 2025)', D='RBI Regulated Entity (all categories)',
               F='Board-approved AI policy',
               G='Has the Board (or its Risk Management Committee) approved an AI policy that covers AI governance and accountability, the AI lifecycle (design, validation, deployment, monitoring, retirement), risk classification of AI use cases, data governance, consumer protection and disclosure, human oversight and override, incident handling, and third-party/vendor AI risk, and is it reviewed at least annually?',
               H='Annually', K='FREE-AI Report (13 Aug 2025), recommendation on board-approved AI policies [VERIFY recommendation number]',
               L='The FREE-AI Committee recommends that every regulated entity adopt a Board-approved AI policy. The report is a committee report, not a Direction: treat this as a suggestive compliance until RBI issues binding directions, but supervisors already ask for it in inspections and it underpins the AI inventory, model-risk and incident expectations.',
               M='Governance & Administration', N='RBI FREE-AI Report; RBI draft Model Risk Management Guidance 2026; ISO/IEC 42001 clause 5.2', O='Suggestive Compliance',
               P='Board / Risk Management Committee', Q='No direct penalty while the framework is non-binding; weak AI governance is a supervisory finding and aggravates liability for AI-driven customer harm.',
               R='Medium', S='Proportionate to the scale and criticality of AI use; becomes binding when RBI notifies directions [VERIFY].',
               U='Board / RMC resolution approving the AI policy; the approved policy (PDF); annual review note.',
               V='Draft the AI policy from the model template (Vidhi can produce a tracked-change draft), circulate to the CRO, CCO, CISO and DPO, place before the Board/RMC, upload the approved signed copy and set the next review date.'),
)

if __name__ == '__main__':
    base, out_dir = sys.argv[1], sys.argv[2]
    out, code, h2, counts = bt.build(base, out_dir, AIGOV)
    print(code, counts, out.rsplit('/', 1)[1], h2)
