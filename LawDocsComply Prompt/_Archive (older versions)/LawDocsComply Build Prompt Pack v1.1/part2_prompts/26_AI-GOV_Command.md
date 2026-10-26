# 26 — AI-GOV Family Command: AI Governance and Responsible AI *(v1.1)*

**Template:** `templates/LDC-TPL-AI-GOV-v1.0 - AI Governance.xlsx` · **Template code:** `LDC-TPL-AI-GOV-v1.0` · **Regulator / authority:** RBI; SEBI; IRDAI; IFSCA; MeitY; Data Protection Board of India; EU AI Office and national market-surveillance authorities; voluntary standards bodies (ISO/IEC, NIST, IMDA) · **Named-range prefix:** `AIGOV_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them. The importer blocks any row that still carries `[VERIFY]`.

**Why this family exists.** Every regulated entity that uses AI — credit scoring, collections bots, chat assistants, document reading, fraud models, generative drafting, and now autonomous agents — needs to show its board and its regulator that the AI is inventoried, risk-classified, tested, monitored, explainable, overridable and disclosed. In India the expectations come from RBI's FREE-AI report (13 Aug 2025), RBI's draft model-risk guidance (2026), SEBI's AI/ML proposals, MeitY's AI Governance Guidelines (Nov 2025) and the DPDP Act; for globally active clients, the EU AI Act, ISO/IEC 42001 and NIST AI RMF. This family turns those into checkpoints. It is an overlay (`OV_AI`): it attaches to any entity family (P15) and feeds the AI Governance workspace (Appendix AA §AA.12).

## 1. How Columns C and D work in this family

**Column C — Framework / Instrument.** The framework the checkpoint comes from. Where one control satisfies several frameworks (e.g. an AI inventory satisfies FREE-AI, RBI model-risk, ISO/IEC 42001 and the EU AI Act), write the row once under the binding or most specific instrument and list the others in Column N ("Also satisfies: …"). Several values in C are separated by "; " only when the obligation text is genuinely common.

**Column D — Role / Entity category.** The role the entity plays for that AI system. A bank that buys a vendor chatbot is a *User of third-party AI service or model* and an *AI Deployer*; a fintech that sells a model is an *AI Developer / Provider*. Agent-specific rows use *Agentic AI deployer*. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (AIGOV_Sector):**
- RBI FREE-AI Framework (Committee Report, Aug 2025)
- RBI Model Risk Management Guidance (draft, 2026)
- SEBI AI/ML guidance (securities market)
- IRDAI AI / technology guidance
- IFSCA AI / technology guidance
- MeitY India AI Governance Guidelines (Nov 2025)
- DPDP Act, 2023 and DPDP Rules, 2025 (AI processing of personal data)
- IT Act, 2000 and IT Rules (synthetic / AI-generated content)
- EU AI Act (Regulation (EU) 2024/1689)
- ISO/IEC 42001:2023 (AI management system)
- NIST AI RMF 1.0 and Generative AI Profile
- Singapore Model AI Governance Framework (incl. Agentic AI, 2026)
- Board-approved internal AI Policy
- Other jurisdiction
- All Frameworks

**Column D (AIGOV_Entity):**
- AI Deployer (entity using AI in its business)
- AI Developer / Provider (builds or sells AI systems)
- User of third-party AI service or model
- Agentic AI deployer (autonomous or semi-autonomous agents)
- RBI Regulated Entity (all categories)
- SEBI Regulated Entity / Intermediary
- Insurer / Insurance Intermediary
- IFSCA Regulated Entity
- Data Fiduciary processing personal data with AI
- EU high-risk AI system deployer
- EU general-purpose AI model provider
- Intermediary hosting AI-generated content
- All Roles (ALL)

**Column H (AIGOV_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (AIGOV_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Information Security, Privacy Office (DPO), Product & Engineering, Internal Audit, Customer Service & Grievance. Family additions: Information Security, Privacy Office (DPO), Product & Engineering, Internal Audit, Customer Service & Grievance (all already mapped to codes in Appendix U §U.9.0 — ISEC, DPR, PRD, IA, CSG). Model-risk and data-science teams are mapped to **Risk Management** (model-risk oversight, second line) or **Product & Engineering** (model development, first line).

**Column O (AIGOV_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Notices & Consents. Family addition: Notices & Consents (AI disclosures to customers).

**Column R (AIGOV_Risk):** High, Medium, Low.

**Column P reference list (AIGOV_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- RBI (supervisory intimation / inspection)
- SEBI (filing / reporting)
- IRDAI
- IFSCA
- Data Protection Board of India
- CERT-In
- EU AI Office / national market-surveillance authority
- Affected customers (AI disclosure / notice)
- Annual Report disclosure
- Board / Risk Management Committee
- Independent AI auditor / assessor
- Not Required

## 3. Applicability and status logic for this family

1. **Binding vs. guidance (Column O and Column S).** Most Indian AI instruments as of 25 Oct 2026 are not yet binding directions:
   - RBI FREE-AI is a **committee report** (13 Aug 2025) — rows use O = *Suggestive Compliance* unless the same requirement already exists in a binding RBI Direction (e.g. outsourcing, IT governance, fair practices, model-risk once finalised), in which case write the binding citation in K and list FREE-AI in N.
   - RBI model-risk guidance is a **draft** (comments closed 24 Jul 2026) [VERIFY final issue]. Rows use O = *Suggestive Compliance* and S = "Draft; becomes binding on final issue [VERIFY]". When RBI finalises it, P05 change management re-labels the rows; do not pre-empt.
   - SEBI AI/ML guidance: consultation paper of 20 Jun 2025 [VERIFY whether a final circular has issued]; rows follow the same rule.
   - MeitY India AI Governance Guidelines (5 Nov 2025) are guidelines, not law → *Suggestive Compliance*.
   - DPDP Act obligations on AI processing of personal data are binding from their commencement dates (core obligations 13 May 2027) → O = *Compliance*, commencement date in S.
   - EU AI Act: binding where territorial scope applies (Art. 2). Use the dates as amended by the Digital Omnibus on AI (political agreement 6 May 2026: Annex III high-risk obligations from 2 Dec 2027; Annex I from 2 Aug 2028; Art. 50 transparency from 2 Aug 2026; GPAI obligations from 2 Aug 2025; AI literacy Art. 4 from 2 Feb 2025) [VERIFY Official Journal publication before citing]. Put the territorial-scope test in S.
   - ISO/IEC 42001 and NIST AI RMF are voluntary standards → O = *Internal Compliance* (if the entity has adopted them) or *Suggestive Compliance*.
2. **Proportionality.** Write the proportionality test in Column S (e.g. "Applies to AI use cases classified High or Critical in the AI use-case register"). LDC's applicability engine uses the AI use-case register (Appendix AA §AA.12) to switch rows on.
3. **Agents.** For any checkpoint about autonomous action, write D = *Agentic AI deployer* and make the control activity (V) name the autonomy level, the human approval gate and the kill switch.
4. **One control, many frameworks.** Do not duplicate rows across frameworks; use Column N "Also satisfies: ISO/IEC 42001 cl. 6.1.4; NIST AI RMF MAP 1.1; EU AI Act Art. 9" so the cross-framework map in LDC can link them.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

1. RBI — Report of the Committee to develop a Framework for Responsible and Ethical Enablement of Artificial Intelligence (FREE-AI) in the Financial Sector, 13 Aug 2025 (7 Sutras; recommendations across innovation-enablement and risk-mitigation pillars) [VERIFY recommendation numbering — commentaries report 26 recommendations under 6 pillars].
2. RBI — draft Guidance on Regulatory Principles for Model Risk Management, 2026 (model inventory; risk tiering; independent validation; human override, suspension and kill-switch arrangements; board-approved model-risk framework; third-party model accountability) [VERIFY final].
3. SEBI — Guidelines for responsible usage of AI/ML in the Indian securities market (consultation paper 20 Jun 2025; senior-officer accountability; client disclosure; testing and shadow testing; monitoring; data governance; log retention ≥ 5 years; vendor management) [VERIFY final circular].
4. MeitY — India AI Governance Guidelines (5 Nov 2025).
5. DPDP Act, 2023 and DPDP Rules, 2025 — rows specific to AI processing (notice and purpose limitation for model training and inference; accuracy obligation s.8(3) for decisions affecting the Data Principal; erasure; SDF algorithmic due diligence under Rule 13).
6. IT Act, 2000 and IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021 as amended — labelling of synthetically generated information [VERIFY amendment notification and date].
7. Regulation (EU) 2024/1689 (AI Act) as amended by the Digital Omnibus on AI [VERIFY publication].
8. ISO/IEC 42001:2023 — Annex A controls (one row per control objective that the entity has adopted).
9. NIST AI RMF 1.0 and NIST AI 600-1 (Generative AI Profile).
10. IMDA — Model AI Governance Framework for Agentic AI (22 Jan 2026): four dimensions — bound risks up front (autonomy, data and tool access, least privilege); meaningful human accountability and override; technical controls across design, pre-deployment testing and post-deployment monitoring; end-user transparency and training.
11. The entity's own Board-approved AI Policy (write tenant-specific rows in the tenant overlay, not in the platform sheet).

## 5. Family-specific pitfalls

- Presenting FREE-AI, RBI's draft model-risk guidance, SEBI's consultation or MeitY's guidelines as binding directions. They are not, until issued as such.
- Using the pre-Omnibus EU AI Act dates (2 Aug 2026 for Annex III) — use the amended dates once published.
- Writing generic "ensure responsible AI" rows. Every row needs a concrete evidence item (Column U): AI inventory extract, model card, validation report, bias test results, red-team report, kill-switch test record, customer disclosure text, incident log extract, Board/RMC minute.
- Forgetting third-party AI: most REs consume vendor or cloud models. Rows on vendor due diligence, contract clauses (audit, testing, exit, data use, no-training), concentration risk and sub-processor lists are required.
- Forgetting agents: tool permissions, autonomy level, approval gates, action logs and kill switch are now expected (IMDA 2026; RBI draft kill-switch language).

## 6. File naming

`AI-GOV - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
