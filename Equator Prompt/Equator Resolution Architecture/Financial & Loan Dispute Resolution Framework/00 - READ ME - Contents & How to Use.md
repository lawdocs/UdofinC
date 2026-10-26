# Equator Resolution — Financial & Loan Dispute Resolution Framework
### Contents & how to use this folder

This folder is the complete content and product package for Equator Resolution's **financial & loan** dispute vertical — borrower–lender disputes resolved by institutional mediation, conciliation and settlement, and coordinated with the RBI Ombudsman, the DRT and the Lok Adalat where the law requires. It mirrors the *Marital* and *Commercial* frameworks in this workspace.

**Prepared:** July 2026 · **Status:** Draft for legal sign-off before go-live · An Infrabyx Group venture · www.equatorresolution.com

> **Not legal advice.** Everything here is a working draft. Have qualified counsel and a Data Protection Officer review the legal content, statutory references and RBI circulars, and confirm all "[verify]" items, before the platform goes live or any document is used with a real party.

---

## What's in each folder

**01 Master Blueprint** — the 63-page master document (Word + PDF), Parts A–I: executive summary and vision; the legal landscape (RBI Integrated Ombudsman Scheme 2021, Digital Lending Directions 2025, NI Act s.138/s.147, SARFAESI/DRT boundary, RBI compromise-settlement framework 2023, Lok Adalat); the platform design (taxonomy, dropdowns, onboarding/KYC-KYB, workflow, either-party initiation, neutral selection, case-manager playbook, SLAs, settlement/OTS, escrow, enforcement, permutations); forms register, fees, risk, roadmap and KPIs; global best practice (UK FOS, AFCA); the technology layer (AI Dispute Explorer, ODR, e-Sign, e-Stamp, forum integration); annexures and model clauses; **Part H — deep dives** (six worked case studies, OTS tax/provisioning, a credit-reporting deep-dive, a vulnerable-borrower protocol, an if/then permutation matrix, a law-as-at-July-2026 table, a DPIA summary, and a document-control/sign-off page); and **Part I — the full text of all 20 forms**.

**02 Developer Handoff** — a 13-sheet Excel workbook: dropdown lists, dispute taxonomy, form-field schema, neutral filters, workflow states, SLAs, API endpoints, integrations, PII/data map, AI features and KPIs, with a live sample-intake sheet. The build spec for engineering.

**03 Workflow Diagrams** — nine diagrams as PNG (for documents) and editable SVG: loan-dispute lifecycle, route/mechanism triage, RBI Ombudsman path, NI-138 cheque-bounce flow, OTS + escrow, digital-lending grievance, enforcement, the AI Dispute Explorer logic, and the process timeline.

**04 Archive - Forms Pack (standalone)** — all 20 forms (F-L01 to F-L20) as individual Word documents, from onboarding and the request for resolution through the OTS agreement, NI-138 compounding memo, harassment and digital-lending grievances, escrow instruction, consent settlement, Lok Adalat referral, and the No-Dues/NOC checklist. The same text is embedded in the Blueprint (Part H).

**05 Board Deck** — a 12-slide board & investor presentation (PowerPoint): the problem, four regulatory tailwinds, the solution, differentiators, coverage, speed, technology, global best practice, business model, roadmap and the ask.

**06 Calculators** — five Excel tools with live, verified formulas: the **OTS (One-Time Settlement) Estimator** (dues → waiver/discount levers → suggested settlement range and recovery %); the **Loan Interest & Penal-Charges Calculator**; the **NI-138 Cost & Exposure Calculator** (s.143A interim compensation, s.148 appeal deposit, Damodar Prabhu graded costs, fight-vs-settle); the **EMI & Restructuring Calculator** (current vs restructured EMI); and the **Settlement Compliance Tracker** (instalments, escrow releases, No-Dues/NOC and credit-bureau status, with an auto "clean-exit" flag).

**07 Operations** — the **Neutral Toolkit & SOP Runbooks** (Word: mediator/conciliator scripts, OTS and NI-138 playbooks, case-manager and escrow runbooks, ethics and borrower-protection, checklists) and the **Compliance & Security Workbook** (Excel: regulatory tracker, security controls, DPDP breach-response runbook).

**08 Outreach** — the **borrower & lender leaflet** (Word) and the **website copy & SEO pack** (Markdown).

**09 Interactive Prototype** — the **Financial Dispute Explorer** (a single HTML file). Open in any browser: it walks a borrower or lender through their dispute, recommends the route, explains their rights, and drafts a grievance or request. Includes a rule-based AI assistant. A demonstration only — it stores no data and gives no legal advice.

**10 Rules & Tariff** — the **Rules of Loan & Financial Dispute Resolution** (Word), Equator's article-by-article institutional rulebook (scope, appointment, conduct, confidentiality, settlement, escrow, OTS, NI-138, time limits, exclusions, and a Neutral Code of Conduct), and the **Schedule of Fees (Tariff)** (Excel) with slab-based administration fees, escrow handling, consumer concessions and a live fee estimator.

**11 Practice Guides** — five practitioner guides: **Sector Playbooks** (lender-type and product-type); **OTS & Cheque-Bounce Practitioner Guides** (OTS negotiation, tax and reporting; the full NI-138 lifecycle, s.143A/s.148 and compounding); the **Digital Lending, Recovery Conduct & Enforcement-Boundary Guide** (RBI DLG 2025, fair-recovery, the SARFAESI/DRT/IBC boundary); the **Forum Interface Map** (with a diagram); and the **Model Clause Library** (loan-agreement ADR, OTS, escrow, No-Dues/NOC, confidentiality, bureau-correction).

**12 Financial & Market** — the vertical **unit-economics & P&L model** (Excel, tiered by matter type, break-even ~month 11); the **Competitive & Landscape Benchmark** (vs the RBI Ombudsman, DRT, Lok Adalat, consumer forum and private ODR players); and the **Market-Sizing & Opportunity Note** (with sources to confirm).

**13 Institutional Readiness** — the **MCI Recognition-Readiness Checklist**, the **Empanelment Criteria & Scoring Rubric** for financial neutrals, the **Lender Partnership & BD Programme**, a **Lender Panel MoU / MSA** template, and a **Regulatory Positioning Note**.

**14 Build Handoff** — the **Technical Architecture & System Design**, the **AI Evaluation & Guardrail Specification**, the **OpenAPI spec** (`openapi_fl.yaml`, 20 endpoints), the **database schema** (`schema_fl.sql`, 21 tables), and the **UI Wireframe Kit** (HTML).

**15 Borrower Self-Help & Vernacular** — borrower-facing, plain-language and multilingual materials: the **Borrower Letters Library** (7 ready-to-use fill-in letters — grievance officer, RBI Ombudsman, credit-bureau dispute, cease-harassment, OTS proposal, statement request, NOC request — each in **English + हिंदी**); the **Borrower Leaflet in Hindi**; the **Website Copy in Hindi**; and a **bilingual Dispute Explorer** (`Financial Dispute Explorer - Bilingual (EN-Hindi).html`) with an English/हिंदी toggle. Built for reach and financial inclusion; general information, not legal advice.

---

## Suggested reading order

1. Start with the **Board Deck** (05) for the story in ten minutes.
2. Read the **Master Blueprint** (01) for the full design and the law.
3. Open the **Interactive Prototype** (09) to feel the borrower/lender journey.
4. Give **02 Developer Handoff**, the diagrams (03) and forms (04) to your product and engineering team.
5. Use **06 Calculators** and **07 Operations** to train neutrals and run live matters.

---

## Important scope note

Equator is a **neutral mediation, conciliation and settlement institution**. It does **not** act as the RBI Ombudsman, a Debts Recovery Tribunal, or a court, and it does not enforce security under SARFAESI. Where a matter belongs to one of those forums, the platform signposts it and offers to mediate the settlement around it. All statutory references, timelines and RBI circulars must be confirmed by counsel as at the go-live date.
