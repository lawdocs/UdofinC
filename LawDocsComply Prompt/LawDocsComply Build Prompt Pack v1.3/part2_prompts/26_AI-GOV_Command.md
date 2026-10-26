# 26 — AI-GOV Family Command: AI Governance and Responsible AI *(v1.1)*

**Template:** `templates/LDC-TPL-AI-GOV-v2.0 - AI Governance.xlsx` · **Template code:** `LDC-TPL-AI-GOV-v2.0` · **Regulator / authority:** RBI; SEBI; IRDAI; IFSCA; MeitY; Data Protection Board of India; EU AI Office and national market-surveillance authorities; voluntary standards bodies (ISO/IEC, NIST, IMDA) · **Named-range prefix:** `AIGOV_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them. The importer blocks any row that still carries `[VERIFY]`.

**Why this family exists.** Every regulated entity that uses AI — credit scoring, collections bots, chat assistants, document reading, fraud models, generative drafting, and now autonomous agents — needs to show its board and its regulator that the AI is inventoried, risk-classified, tested, monitored, explainable, overridable and disclosed. In India the expectations come from RBI's FREE-AI report (13 Aug 2025), RBI's draft model-risk guidance (2026), SEBI's AI/ML proposals, MeitY's AI Governance Guidelines (Nov 2025) and the DPDP Act; for globally active clients, the EU AI Act, ISO/IEC 42001 and NIST AI RMF. This family turns those into checkpoints. It is an overlay (`OV_AI`): it attaches to any entity family (P15) and feeds the AI Governance workspace (Appendix AA §AA.12).

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-AI-GOV-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Framework / Instrument.** The framework the checkpoint comes from. Where one control satisfies several frameworks (e.g. an AI inventory satisfies FREE-AI, RBI model-risk, ISO/IEC 42001 and the EU AI Act), write the row once under the binding or most specific instrument and list the others in Related Document / Policy / Committee ("Also satisfies: …"). Several values in C are separated by "; " only when the obligation text is genuinely common.

**General Applicability (Type) — Role / Entity category.** The role the entity plays for that AI system. A bank that buys a vendor chatbot is a *User of third-party AI service or model* and an *AI Deployer*; a fintech that sells a model is an *AI Developer / Provider*. Agent-specific rows use *Agentic AI deployer*. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (AIGOV_Sector):**
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

**General Applicability (Type) (AIGOV_Entity):**
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

**Due Date & Frequency (AIGOV_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (AIGOV_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Information Security, Privacy Office (DPO), Product & Engineering, Internal Audit, Customer Service & Grievance. Family additions: Information Security, Privacy Office (DPO), Product & Engineering, Internal Audit, Customer Service & Grievance (all already mapped to codes in Appendix U §U.9.0 — ISEC, DPR, PRD, IA, CSG). Model-risk and data-science teams are mapped to **Risk Management** (model-risk oversight, second line) or **Product & Engineering** (model development, first line).

**Compliance Type (AIGOV_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Notices & Consents. Family addition: Notices & Consents (AI disclosures to customers).

**Risk Category (AIGOV_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (AIGOV_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
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

1. **Binding vs. guidance (Compliance Type and Conditional Applicability / Exemptions / Thresholds).** Most Indian AI instruments as of 25 Oct 2026 are not yet binding directions:
   - RBI FREE-AI is a **committee report** (13 Aug 2025) — rows use Compliance Type = *Suggestive Compliance* unless the same requirement already exists in a binding RBI Direction (e.g. outsourcing, IT governance, fair practices, model-risk once finalised), in which case write the binding citation in K and list FREE-AI in N.
   - RBI model-risk guidance is a **draft** (comments closed 24 Jul 2026) [VERIFY final issue]. Rows use Compliance Type = *Suggestive Compliance* and Conditions = "Draft; becomes binding on final issue [VERIFY]". When RBI finalises it, P05 change management re-labels the rows; do not pre-empt.
   - SEBI AI/ML guidance: consultation paper of 20 Jun 2025 [VERIFY whether a final circular has issued]; rows follow the same rule.
   - MeitY India AI Governance Guidelines (5 Nov 2025) are guidelines, not law → *Suggestive Compliance*.
   - DPDP Act obligations on AI processing of personal data are binding from their commencement dates (core obligations 13 May 2027) → Compliance Type = *Compliance*, commencement date in S.
   - EU AI Act: binding where territorial scope applies (Art. 2). Use the dates as amended by the Digital Omnibus on AI (political agreement 6 May 2026: Annex III high-risk obligations from 2 Dec 2027; Annex I from 2 Aug 2028; Art. 50 transparency from 2 Aug 2026; GPAI obligations from 2 Aug 2025; AI literacy Art. 4 from 2 Feb 2025) [VERIFY Official Journal publication before citing]. Put the territorial-scope test in S.
   - ISO/IEC 42001 and NIST AI RMF are voluntary standards → Compliance Type = *Internal Compliance* (if the entity has adopted them) or *Suggestive Compliance*.
2. **Proportionality.** Write the proportionality test in Conditional Applicability / Exemptions / Thresholds (e.g. "Applies to AI use cases classified High or Critical in the AI use-case register"). LDC's applicability engine uses the AI use-case register (Appendix AA §AA.12) to switch rows on.
3. **Agents.** For any checkpoint about autonomous action, write Type = *Agentic AI deployer* and make the Control Activity (Maker Guidance) name the autonomy level, the human approval gate and the kill switch.
4. **One control, many frameworks.** Do not duplicate rows across frameworks; use Related Document / Policy / Committee "Also satisfies: ISO/IEC 42001 cl. 6.1.4; NIST AI RMF MAP 1.1; EU AI Act Art. 9" so the cross-framework map in LDC can link them.

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
- Writing generic "ensure responsible AI" rows. Every row needs a concrete evidence item (Evidence / Proof to Upload): AI inventory extract, model card, validation report, bias test results, red-team report, kill-switch test record, customer disclosure text, incident log extract, Board/RMC minute.
- Forgetting third-party AI: most REs consume vendor or cloud models. Rows on vendor due diligence, contract clauses (audit, testing, exit, data use, no-training), concentration risk and sub-processor lists are required.
- Forgetting agents: tool permissions, autonomy level, approval gates, action logs and kill switch are now expected (IMDA 2026; RBI draft kill-switch language).

## 6. File naming

`AI-GOV - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Framework | RBI FREE-AI · SEBI AI / ML guidance · IRDAI guidance · IFSCA guidance · MeitY AI Governance Guidelines · DPDP Act and Rules · EU AI Act · ISO/IEC 42001 · NIST AI RMF | Use for one-control-many-frameworks rows; primary framework first. |
| AI Risk Tier | Prohibited · High · Limited (transparency) · Minimal · General-purpose AI model · All tiers | The AI risk tier the row applies to (EU AI Act tiers, or the entity's own AI use-case tiering where the instrument uses that). |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-AI-GOV-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Product & Engineering → AI inventory / Model validation / Human oversight; Risk Management → Model risk; Privacy Office (DPO) → AI and personal data; HR → AI literacy and training; Governance & Administration → AI governance committee. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Model & AI primary; add Data Privacy, Conduct & Consumer or Third-party where relevant. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the entity taken measures to ensure a sufficient level of AI literacy of its staff and other persons dealing with the operation and use of AI systems on its behalf? |
| 4 | Clause / Para No. (`clause_ref`) | Article 4, Regulation (EU) 2024/1689 (Artificial Intelligence Act) |
| 5 | Department (`department`) | HR |
| 6 | Due Date & Frequency (`frequency`) | Annually |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | Medium |
| 10 | Regulator / Authority (`authority`) | EU AI Office / national market-surveillance authority |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act) |
| 12 | Instrument Reference No. (`instrument_ref`) | Regulation (EU) 2024/1689 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 13-Jun-2024 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY any Digital Omnibus amendment] |
| 15 | Actionable Last Updated On (`question_updated_date`) | 13-Jun-2024 |
| 16 | Change Status (`change_status`) | New |
| 17 | Change Note / Previous Actionable (`change_note`) | (blank) |
| 18 | Source Link (`source_url`) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj |
| 19 | General Applicability (Layer) (`applic_layer`) | EU AI Act (Regulation (EU) 2024/1689) |
| 20 | General Applicability (Type) (`applic_type`) | AI Deployer (entity using AI in its business); AI Developer / Provider (builds or sells AI systems) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to providers and deployers within the Act's territorial scope (Art. 2). Applies from 2 February 2025. |
| 22 | Applicable From (`applic_from`) | 02-Feb-2025 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Framework (`ext_*`) | EU AI Act; ISO/IEC 42001 |
| E2 | AI Risk Tier (`ext_*`) | All tiers |
| 24 | Short Title (`short_title`) | AI literacy - staff measures |
| 25 | Interpretation / Explanation (`explanation`) | 'Sufficient level of AI literacy' takes into account technical knowledge, experience, education and the context of use. The Act does not prescribe a course; the entity must show measures proportionate to its AI use. (Abridged.) |
| 26 | Department Function (`dept_function`) | Training |
| 27 | Department Sub-function (`dept_subfunction`) | AI literacy |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Complete training for new staff within [entity policy] days of joining; refresh annually |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | Not Required |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | AI Policy; AI use-case register; Training calendar |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Enforcement by national authorities under Article 99 and national law [VERIFY penalty applicability to Art. 4]. |
| 36 | Penalty Provision (`penalty_ref`) | Article 99, Regulation (EU) 2024/1689 [VERIFY] |
| 37 | Risk Type (`risk_type`) | Model & AI; People |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | AI literacy training plan; attendance records by role; training content mapped to AI systems in use |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Map roles to the AI systems they use. Deliver role-based AI literacy training and refresh it annually. Keep attendance and content records. |
| 42 | Checker Review Points (`checker_points`) | 1. All roles using AI are covered. 2. Content reflects the AI systems actually in use. 3. Attendance ≥ target. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain the AI use-case register and HR list. 2. Sample 20 staff using AI and inspect training records. Exception: untrained user of a high-risk system. |
| 44 | Tags / Keywords (`tags`) | ai literacy; eu ai act; article 4; training |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

