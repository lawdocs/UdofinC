# Phase P12 — Data Protection, Cyber Security, IT Governance and Third-Party Risk (TPRM)

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, RLS, audit ledger, Object Lock evidence store), P01 (identity, step-up MFA, grants), P02 (settings registry, rule packs, Locked/Governed/Tenant tiers), P03 (instrument and obligation library — the DPDP, GDPR, CCPA, CERT-In, RBI/SEBI/IRDAI/IFSCA cyber instruments are content packs), P04 (compliance instances, maker-checker, evidence, calendar, tasks), P07 (DMS, policy lifecycle — privacy notice, ISMS policies), P08 (risk register, KRIs, loss events).
>
> **Sequencing:** starts after P04 exit. P12 sub-iterations: P12a Privacy Programme (§4A–§4F), P12b Cyber and IT Governance (§4G–§4K), P12c TPRM and Outsourcing (§4L–§4N), P12d AI Governance hooks (§4O). P12b can run in parallel with P12a using a second squad. P13 (HRMS) and P14 (grievance) consume the consent ledger, rights-request desk and breach workflow built here.
>
> **Binding appendices:** A (state machines), B (data model, events, errors), D (roles and SoD), F (source register — DPDP, MeitY, CERT-In, sector cyber sources), G (legal rules `LR-MEITY-*`, `LR-CERTIN-*`, `LR-EU-*`, `LR-US-*`, `LR-RBI-*` cyber/outsourcing), M (export package), Q (security and certification readiness of LDC itself — this phase is the *client's* programme), U (settings).
>
> **Requirements covered:** R-005, R-010, R-013, R-021, R-031, R-033, R-038, R-039, R-046 (client side), R-058, R-086, R-088, R-102.
>
> **Estimated effort:** 8 two-week sprints for a squad of 8 (privacy 3, cyber/ISMS 3, TPRM 2); +2 sprints for the multi-law overlay content load with the content team.

>
> **v1.1 changes (25 October 2026)**
> - New **§4P AI Governance module `aig` and overlay `OV_AI`** (D-36; Appendix AA §AA.12): AI system register, use cases, multi-framework risk classification, impact assessments, validation and fairness evidence, human-oversight and kill-switch records, monitoring, AI incident register, disclosures, vendor AI assurance (incl. one-click import of LDC's own pack, D-38), Board AI report and cross-framework control map (FR-P12-55–FR-P12-72); §4O retained as the bridge and now points to §4P; new sub-iteration **P12e** (+3 sprints, squad of 5).
> - New **§4Q DPDP Schedules as linked reference data** (G5 TM-729/736) and **§4R data-compliance tree generator** fully specified — canonical hierarchy, algorithm, phase flips, SDF notification, processor-only tenants, worked NBFC and e-commerce examples, edge cases (FR-P12-73–FR-P12-80).
> - New **§4S default data-compliance RACI** (G5 TM-752), customisable (FR-P12-81).
> - New **§4T TPRM accelerators** (G2 IMP-115–IMP-120): questionnaire criteria extraction, cited vendor-document review, reassessment triggers, deterministic outsourcing materiality, immutable detection-source capture, and answering inbound due-diligence questionnaires from banks/co-lenders with evidence citations (FR-P12-82–FR-P12-89).
> - Faster workflows (§4U): one-screen vendor onboarding, bulk approval of discovery proposals with undo (NN-49), pre-filled assessments, 'review next' queues (NN-46); customisation options registered in P02 (§9).
> - Stale citation fixed: bank IT-governance references now point to the RBI DoS Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions 2026 for each bank category (catalogue D-39), with the 2023 IT Governance MD treated as superseded [VERIFY repeal paragraph].
> - New NN applied: NN-47 (AI never sets a rating or status), NN-48 (act/evidence/approval dates on instances), NN-49 (undo), NN-50 (autonomy levels for VA-15 and DDQ agents), NN-24 (home-region cells for foreign subsidiaries' privacy data).
---

## 1. Objective and business outcome

Every client of LawDocsComply processes personal data of borrowers, depositors, investors, policyholders, members and employees, runs regulated technology and depends on vendors. P12 gives the client one place to run its **privacy programme**, its **cyber and IT governance programme** and its **third-party/outsourcing programme**, each driven by versioned law packs and linked to the same obligations, controls, evidence, risks, incidents and Board reporting as the rest of the platform. LawDocsComply is the client's tool; the client remains the Data Fiduciary / controller / regulated entity (NN-14 accountability stays human).

| Outcome | Exit-gate measure |
|---|---|
| A data-protection programme a DPO can run end to end | A seeded NBFC-ML tenant completes: data inventory of 40 processing activities, ROPA export (DPDP + GDPR Art. 30 view), 3 DPIAs, consent-ledger configuration for two purposes, a rights request closed within SLA, and a simulated breach with DPB 72-hour report, CERT-In 6-hour report and RBI DAKSH 6-hour report drafts — all evidenced, in ≤ 1 working day of user effort |
| Multi-law overlay without duplication | One processing activity shows DPDP, GDPR and CCPA obligations side by side, de-duplicated into common controls with law-specific deltas; switching a law pack on/off changes only applicability, never history (NN-29) |
| Sector cyber frameworks as one control library | RBI NBFC Cyber Directions 2026 (RBI/DoS/2026-27/461), RBI Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions 2026 for commercial banks (/410), SFBs (/419), payments banks (/428), UCBs (/437), AIFIs (/456) and credit information companies (/470) [VERIFY numbers; the 2023 bank IT Governance MD is treated as superseded] *(v1.1)*, SEBI CSCRF, IRDAI ICS Guidelines 2023, IFSCA Cyber Guidelines 2025, CERT-In Directions 2022 and ISO/IEC 27001:2022 Annex A load as packs mapped to ≤ 220 common controls; a control test once evidenced satisfies every mapped requirement, with the mapping visible |
| Incident clocks never silently lapse | Every incident with a reportable classification starts each applicable clock (CERT-In 6 h, RBI DAKSH 6 h, IFSCA 6 h, SEBI per CSCRF, DPB "without delay" + 72 h, GDPR 72 h, sector-specific) at the right start event, owned, escalated at 50 %, 75 % and 90 % of the window; a lapse is a Critical exception (NN-31 pattern) |
| VAPT, BCP and DR testing tracked to closure | VA/PT schedule auto-generated from the asset criticality register per the applicable directions (e.g., RBI NBFC 2026 paras 121–126: VA half-yearly, PT annually for critical/DMZ systems); findings tracked to closure with re-test evidence; DR drill records show "DR as primary ≥ 1 working day" where required (para 131) |
| Outsourcing register an RBI inspector would accept | Material-outsourcing classification (paras 14, 58(2) of the NBFC Outsourcing Directions 2025), due diligence, contract-clause checklist (paras 34, 74), half-yearly Board/RMC review (paras 12(1)(vii), 36), exit plan (paras 84–88) — each evidenced and exportable |
| AI governance hooks | Client's AI systems inventory with ISO/IEC 42001-aligned risk assessment and CCPA ADMT / DPDP Rule 13 algorithmic-due-diligence flags |

---

## 2. Scope (in / out)

**In scope**
- `dpc` module: data inventory, data map, processing activities (ROPA), purposes, lawful bases, data categories (incl. sealed classes), systems, recipients, transfers, retention classes; DPIA/PIA/TIA (transfer impact) and LIA (legitimate-interest, GDPR); consent and notice designer for the **client's own** customer journeys; consent ledger and consent-artefact API; data-principal / data-subject / consumer rights desk; breach and incident management with multi-regulator clocks; privacy dashboards; DPO workspace; Significant Data Fiduciary (SDF) pack.
- Cyber and IT governance: ISMS scope, asset and information-asset register with criticality, common control library with framework mappings, Statement of Applicability (SoA), control testing (design and operating effectiveness), cyber-security policy set (with P07), IT Strategy Committee / IT Steering Committee / Information Security Committee support (with P06), CISO workspace, VAPT programme, patch and vulnerability SLA tracking, cyber-audit management (with P10), BCP/DR plan register and test records, cyber crisis management plan (CCMP), threat-intelligence notes, phishing/awareness campaign records (import), log-retention and NTP attestations (CERT-In).
- `tpr` module: vendor/third-party master, outsourcing register (financial and IT outsourcing separately), materiality engine, inherent risk tiering, due-diligence questionnaires (DDQ) with evidence requests sent to vendors via a vendor portal, contract-clause checklist and gaps, SLA and performance monitoring, concentration and sub-contractor (fourth-party) mapping, intra-group outsourcing (Infrabyx-style group service arrangements), offshore outsourcing checks, vendor incidents, annual reviews, exit and termination plans, Board/RMC review packs.
- AI governance hooks: AI system inventory, AI risk/impact assessment templates, model cards, human-oversight attestations, link to `ai` module (P17) for LDC's own AI usage disclosures.
- Exports: ROPA (XLSX/PDF), DPIA reports (DOCX/PDF), breach reports (DOCX/PDF + regulator-form field sheets), SoA (XLSX), outsourcing register (XLSX in RBI-expected column order), Board pack sections.

**Out of scope (and where it lives)**
- LDC's own security programme and certification readiness → Appendix Q and P24.
- Submission to DPB, CERT-In, DAKSH, IFSCA mailbox, SEBI portal — LDC drafts and exports; a human submits (D-13, NN-08). Where an official API appears, it is added behind a flag in P18.
- SIEM/SOC tooling — LDC ingests alerts and incident tickets from the client's SOC (P18 connectors: Splunk, Microsoft Sentinel, Elastic, Wazuh, QRadar via webhook/syslog-to-HTTP relay) but is not a SIEM.
- Consent collection on the client's website/app at runtime at scale: LDC supplies the consent-artefact API, embeddable notice widget and SDK (P18), and is the system of record for consent **artefacts** only when the client chooses (`dpc.consent.mode`). For Finbyx/Udofin borrowers, the capturer remains the producing product (Ecosystem Spec §6.14).
- Registration as a Consent Manager under DPDP Rule 4 — LawDocsComply does not register as one (that requires a separate Indian company with ≥ ₹2 crore net worth and an operating-only-for-Data-Principals model) [REC]; integration readiness with registered Consent Managers is in scope (flag `dpc.consent_manager.integration.enabled = OFF`).

---

## 3. Personas and permissions touched

| Role code | What they do in P12 |
|---|---|
| `ten_kmp` (DPO) | Owns the privacy programme; approves ROPA versions, DPIAs, breach notifications drafts (checker); signs DPB reports for SDFs |
| `ten_kmp` (CISO) | Owns ISMS, control library, SoA, VAPT plan, CCMP; checker on cyber incident reports; presents quarterly cyber-risk review (RBI NBFC 2026 para 82) |
| `ten_kmp` (CTO/CIO) | Asset owner approvals, DR test sign-off, patch exceptions |
| `ten_kmp` (CRO) | Receives KRI feeds; approves residual-risk acceptance; outsourcing materiality checker |
| `ten_cco` | Overall compliance view; consolidates regulator reporting calendar |
| `ten_maker` / `ten_checker` | Business-unit data owners fill inventory, run control tests, upload evidence; checkers review |
| `ten_dept_head` | Approves processing activities of their department; vendor owner sign-off |
| `ten_board_member`, `ten_committee_member` | View Board/ITSC/RMC packs; approve policies (P07/P06) |
| `ten_is_auditor`, `ten_internal_auditor`, `ten_external_auditor` | Read scoped evidence; raise findings (P10) |
| `ten_supervisor_view` | Time-boxed read-only grant (D-12) — typically outsourcing register, incident register, SoA |
| `ten_support_agent` | Logs rights requests received via support channels (P14 handoff) |
| Vendor contact (`ext_vendor`, a limited external identity) | Answers DDQs, uploads evidence, acknowledges contract-clause attestations, reports vendor incidents via the vendor portal — sees only their own questionnaire and requests |
| `dlv_professional` | Retainer delivery (D-03): acts as maker for privacy/cyber services under a tenant grant |
| `svc_vidhi` | Drafts DPIAs, notices, breach summaries, DDQ evaluations; never approves or files (NN-14) |

Separation of duties (Appendix D): the person who logs an incident cannot alone close it; the DPO cannot be the checker of a DPIA they authored; a vendor owner cannot approve their own vendor's materiality downgrade; CISO cannot report into the Head of IT on the org chart where RBI NBFC 2026 para 81 applies (P13 org structure raises a validation warning `LDC-DPC-031`).

---

## 4. Functional requirements

### 4A. Law packs and applicability for data protection

**FR-P12-01 — Law packs.** Seed, as P03 content packs with clause-level obligations, the following instruments, each effective-dated (NN-07) and with its commencement phases as first-class `effective_from` values:

| Pack code | Instrument | Commencement handling |
|---|---|---|
| `DATA-IN-DPDP` | Digital Personal Data Protection Act 2023 + DPDP Rules 2025 (MeitY, 13 Nov 2025; G.S.R. 846(E) [VERIFY]) incl. the seven Schedules as reference data | Rules 1, 2, 17–21 from 13 Nov 2025; Rule 4 (Consent Managers) from 13 Nov 2026; Rules 3, 5–16, 22, 23 from 13 May 2027. Act sections commence with the corresponding Rules notification [VERIFY S.O. for Act commencement] |
| `DATA-IN-ITACT` | IT Act 2000 s.43A, s.72A; IT (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules 2011 | In force; s.43A and the SPDI Rules are omitted by DPDP Act s.44(2) on its commencement [VERIFY effective date of omission — expected aligned with 13 May 2027] — model as `effective_to` |
| `DATA-IN-CERTIN` | CERT-In Directions under s.70B(6), No. 20(3)/2022-CERT-In, 28 Apr 2022 + FAQs | In force |
| `DATA-EU-GDPR` | Regulation (EU) 2016/679 + SCCs (Decision 2021/914) | Applies when `processing_activity.eu_nexus = true` (Art. 3(2) targeting/monitoring, or EU establishment) |
| `DATA-US-CCPA` | California Consumer Privacy Act as amended by CPRA + CPPA regulations (finalised 23 Sep 2025, effective 1 Jan 2026) | Applies when tenant flags California consumers and meets thresholds (Cal. Civ. Code §1798.140(d)); risk assessments from 1 Jan 2026 with attestation to CPPA by 1 Apr 2028; ADMT from 1 Jan 2027; cybersecurity-audit certification by revenue tier (1 Apr 2028 / 2029 / 2030) |
| `DATA-SECTOR-*` | Sector overlays: RBI (customer data confidentiality, data localisation for payment data — RBI circular 6 Apr 2018 [VERIFY current instrument]), SEBI (CSCRF data classification and localisation), IRDAI (data localisation in ICS Guidelines), IFSCA | Applicability from P15 entity profile |
| `DATA-INTL-*` | Future packs (UK GDPR/DPA 2018, Singapore PDPA, UAE PDPL, DIFC DP Law) | D-19: enabled only after a sourced, reviewed pack exists (flag per pack) |

**FR-P12-02 — Role determination.** For each processing activity, the engine determines the tenant's role(s): DPDP *Data Fiduciary* / *Data Processor* / *Significant Data Fiduciary* (on Central Government notification under s.10 — stored as a tenant fact with gazette reference, never inferred) / *Consent Manager* (not supported as a role for clients either, unless the tenant itself is registered); GDPR *controller* / *processor* / *joint controller*; CCPA *business* / *service provider* / *contractor* / *third party*. The role matrix drives which obligations instantiate (Architecture Part 3 "Applicability Matrix — obligation family × role" is the seed).

**FR-P12-03 — Data-compliance tree.** Generate each organisation's data-compliance tree using the owner's canonical hierarchy (Architecture Part 3 "Data-Compliance Branch Logic"): Jurisdiction → Law → Role → Obligation family → Obligation → Control → Evidence. The generator is deterministic (rule pack `dpc.applicability@<ver>`), explainable ("why does this apply?" panel with the facts and rule lines used), and re-runs on any fact change, producing a diff for approval (maker-checker) before instances are created or retired (NN-29).

**FR-P12-04 — Onboarding facts.** Capture the data-compliance facts in a short wizard (≤ 12 questions, pre-filled from P01 onboarding and P15 entity profile): processes children's data; processes data of persons with disability (guardian consent, DPDP s.9 and Rule 10/11 [VERIFY rule numbers]); EU/UK/California nexus; volumes (data principals, users); cross-border processing locations; sector regulator; notified SDF status; uses automated decision-making for significant decisions; uses Consent Managers; relies on legitimate uses under DPDP s.7 (which clause); employee data processing; outsourcing of processing to processors. Each fact has an "i" help text (P23 glossary).

### 4B. Data inventory, data map and ROPA

**FR-P12-05 — Processing activity record.** Fields: id; name; business owner (department, `ten_dept_head`); purpose(s) (controlled vocabulary + free text); DPDP basis (consent s.6 / legitimate use s.7 clause (a)–(i)); GDPR lawful basis (Art. 6(1)(a)–(f)) and special-category condition (Art. 9(2)); CCPA purpose (business purpose §1798.140(e)) and "sale/share" flag; data principal categories (customers, borrowers, guarantors, depositors, members, investors, policyholders, employees, applicants, vendors' staff, website visitors, children); personal-data categories (identity, contact, KYC documents, financial, credit information, biometric, health, location, device/online identifiers, employment, criminal records — blocked from collection unless lawful); sealed-class flags (NN-13); source (direct, third party, public, CIC, Account Aggregator, DigiLocker); systems and data stores (link to asset register); recipients (internal, processors, group entities, regulators, CICs); transfers (country, mechanism: DPDP s.16 / GDPR Ch. V mechanism / none); retention class and period (with legal basis: e.g., PMLA Rules 10-year KYC/transaction retention [VERIFY current period], Companies Act s.128 8-year books, RBI KYC MD, Income-tax Act 2025 retention, DPDP Third Schedule); security measures (link to controls); DPIA required? (computed); status (draft, in review, approved, retired); version.

**FR-P12-06 — Discovery assist.** Bulk import processing activities from Excel (template `LDC-DT-ROPA-v1.0`, separate from the questionnaire template contract of Appendix E), from the owner's earlier data-compliance sheets, and from system connectors (P18) that report schemas (database column names) — Vidhi classifies columns into data categories with confidence (NN-14; human confirms). Never pull actual personal data values into LDC for discovery; only metadata.

**FR-P12-07 — Data map.** Visual flow per activity (source → systems → recipients → transfers), generated from the records (no manual drawing); accessible table alternative (NN-21).

**FR-P12-08 — ROPA exports.** One-click export in three views: DPDP view (purpose, notice reference, consent/legitimate use, retention, processors, transfers), GDPR Art. 30(1) controller view and Art. 30(2) processor view, CCPA notice-at-collection inventory (categories, sources, purposes, retention, sale/share). XLSX + PDF, versioned, hash in ledger.

### 4C. Notices and consent (for the client's own customers)

**FR-P12-09 — Notice designer.** Build DPDP-compliant notices (DPDP s.5 and Rule 3: standalone, clear and plain language, itemised description of personal data and the specified purpose, goods/services enabled, communication link to withdraw consent, exercise rights, and complain to the Board [VERIFY exact Rule 3 elements]) from processing-activity records; produce versions in English and the Eighth Schedule languages the tenant selects (DPDP s.5(3) option to access in English or any Eighth Schedule language); translation via P07 translation service with human review before publication (NN-04). GDPR Art. 13/14 and CCPA notice-at-collection variants generate from the same records. Output: hosted notice page URL, embeddable widget, PDF.

**FR-P12-10 — Consent artefacts and ledger.** Optional consent ledger (`dpc.consent.mode` ∈ `OFF`, `LEDGER_ONLY`, `FULL_CAPTURE`): records consent artefact id, data principal reference (pseudonymous token; contact hashed), notice version, purposes (granular, each separately), timestamp, channel, capture evidence (UI version, IP/device hash), proof of verifiable parental/guardian consent where applicable, withdrawal time and propagation status to recipients (Ecosystem Spec `ConsentWithdrawn`, propagation SLA ≤ 1 h [REC]). Consent artefact schema aligned with the owner's "Field schema — Consent Record (DPDP-compliant)" (Architecture Part 3 §DPDP Web-Architecture) and, for Consent Manager readiness, with the interoperable artefact once the DPB publishes standards [VERIFY].

**FR-P12-11 — Withdrawal parity.** Withdrawal must be as easy as giving consent (DPDP s.6(4)); the widget enforces a same-click-depth withdrawal; consequences notice shown; processing-stop tasks created for each recipient system with due times; legal-retention exceptions recorded per purpose.

### 4D. Rights requests desk (DPDP, GDPR, CCPA)

**FR-P12-12 — Intake.** Channels: embeddable form on the client's site/app (P14 shares the widget framework), email ingestion, support-ticket conversion (P14), manual entry. Request types: DPDP s.11 access summary, s.12 correction/completion/updating/erasure, s.13 grievance redressal, s.14 nomination; GDPR Arts. 15–22 (access, rectification, erasure, restriction, portability, objection, ADM); CCPA know/access, delete, correct, opt-out of sale/share, limit use of sensitive PI, ADMT access/opt-out (from 1 Jan 2027).

**FR-P12-13 — Identity verification.** Risk-based: match on registered contact + OTP; for higher-risk requests (erasure of accounts, access to financial data) step-up via existing customer login in the client's system or DigiLocker-based document (P18 adapter) — never collect full Aadhaar (NN-12); CCPA verification standards (reasonable degree / high degree of certainty) as rule-pack options; authorised agent / nominee / guardian handling with proof.

**FR-P12-14 — Clocks.** Per law: DPDP response period per Rule 14 [VERIFY — secondary sources state 90 days for grievance response]; GDPR 1 month extendable by 2 months (Art. 12(3)) with notice of extension within the first month; CCPA 10 business days to confirm receipt, 45 calendar days to respond, extendable once by 45 days with notice (Cal. Code Regs. tit. 11 §7021 [VERIFY]); opt-out of sale/share honoured within 15 business days (§7026 [VERIFY]). Clock values are Governed settings sourced from rule packs, never constants (NN-26 pattern applied to privacy).

**FR-P12-15 — Fulfilment orchestration.** Each request fans out to fulfilment tasks per system of record (from the data map): search, extract (summary only — LDC does not pull raw personal data unless the tenant enables `dpc.rights.fulfilment_store = TENANT_VAULT`, which keeps extracts in the sealed evidence store with 30-day auto-deletion after closure), correct, erase/anonymise, restrict, confirm. Exemptions/denials require a reason code mapped to the law (e.g., DPDP s.17 exemptions; legal-retention obligation under PMLA; GDPR Art. 17(3)); denial wording is drafted from templates and reviewed. For Finbyx/Udofin data, the desk emits `DataPrincipalRequest` events (Ecosystem Spec §6.14) and tracks responses.

**FR-P12-16 — Response pack.** Response letter (DOCX/PDF) in the requester's chosen language, evidence of each fulfilment step, closure attestation by the DPO or delegate (checker), satisfaction/escalation link to the client's grievance desk (P14) and to the DPB complaint route (DPDP s.13(3) — exhaust grievance redressal before approaching the Board).

### 4E. DPIA, TIA, LIA and privacy-by-design

**FR-P12-17 — Assessment templates.** DPIA (DPDP Rule 13 for SDFs — annual; GDPR Art. 35 criteria; CCPA risk assessment content per CPPA regulations: purpose, categories, operational elements, benefits, negative impacts, safeguards, approval by a decision-maker, retention of the assessment, annual review of changes [VERIFY section list]); PIA-lite screening (≤ 10 questions) that decides whether a full DPIA is needed; Transfer Impact Assessment for GDPR Chapter V; Legitimate Interest Assessment (three-part test); Children's data assessment; AI/ADMT impact assessment (links §4O).

**FR-P12-18 — Workflow.** Screening → full assessment (maker: data owner; Vidhi drafts from the processing record, NN-14) → DPO review → risk scoring (likelihood × impact on data principals, configurable 5×5) → mitigation actions (tasks with owners and due dates) → residual risk → approval (DPO + business head; for high residual risk, CRO and, where GDPR Art. 36 prior consultation applies, a flag for supervisory consultation) → periodic review (default 12 months; SDF mandatory every 12 months).

**FR-P12-19 — Privacy-by-design checklist** attached to change requests in the client's own projects (imported from Jira/Azure DevOps via P18 or entered manually), producing a DPIA screening automatically when a project introduces a new purpose, data category, recipient or transfer.

### 4F. Breach and incident management (privacy + cyber, one register, many clocks)

**FR-P12-20 — Single incident register.** One `dpc.incidents` register for cyber incidents and personal-data breaches (a personal-data breach is a classification of an incident, not a separate object), aligned with the owner's "Field schema — Breach Event & Notifications (Rule 7)" and the Part 1 "Cyber / Operational Incident Reporting Form". Intake: manual form, email-in, SOC/SIEM webhook (P18), vendor portal (§4M), employee report button (P13 self-service), Finbyx/Udofin `SecurityIncidentNotified` events (Ecosystem Spec §9.2).

**FR-P12-21 — Classification.** Deterministic classification questionnaire: (a) CERT-In reportable type (Annex I of the 2022 Directions — e.g., targeted scanning, compromise of critical systems, unauthorised access to IT systems/data, website defacement, malicious code, attacks on servers, identity theft/spoofing/phishing, DoS/DDoS, attacks on critical infrastructure/SCADA, data breach, data leak, attacks on IoT, attacks on applications such as e-governance/e-commerce, fake mobile apps, unauthorised access to social media accounts, attacks or malicious activities affecting cloud/AI/ML systems [VERIFY full list text]); (b) personal-data breach under DPDP s.2(u); (c) GDPR personal-data breach and risk level (Art. 33 "unlikely to result in risk" test; Art. 34 high risk); (d) sector reportable (RBI NBFC 2026 para 28/141 cyber incidents; RBI bank incident reporting; SEBI CSCRF incident; IRDAI; IFSCA 6-hour); (e) severity (S1–S4) and customer impact; (f) outsourced-provider involvement (Outsourcing Directions para 61: provider reports to NBFC so NBFC can report to RBI within 6 hours **of detection by the service provider** — the clock starts at the provider's detection time, which the vendor portal captures).

**FR-P12-22 — Clock engine.** On classification, start every applicable clock with its own start event and owner:

| Clock key | Destination | Window | Start event | Source |
|---|---|---|---|---|
| `clk.certin.6h` | CERT-In (incident@cert-in.org.in / portal) | 6 hours | Noticing / being brought to notice | CERT-In Directions 28 Apr 2022, direction (ii) |
| `clk.rbi.daksh.6h` | RBI DAKSH (NBFC); NHB for HFCs | 6 hours | Detection | RBI NBFC Cyber Directions 2026 paras 28, 141 |
| `clk.rbi.outsourced.6h` | RBI via the NBFC | 6 hours | Detection by service provider | NBFC Outsourcing Directions 2025 para 61 |
| `clk.ifsca.6h` / `clk.ifsca.interim.3d` / `clk.ifsca.rca.30d` | IFSCA cyber-incidents mailbox | 6 h / 3 days / 30 days | Detection | IFSCA Cyber Guidelines (effective 1 Apr 2025) [VERIFY para refs] |
| `clk.sebi.cscrf` | SEBI incident reporting per CSCRF + CERT-In | per CSCRF (6 hours to CERT-In; SEBI per circular) [VERIFY] | Detection | SEBI CSCRF 20 Aug 2024 [VERIFY] |
| `clk.irdai.cyber` | IRDAI + CERT-In | per ICS Guidelines 2023 [VERIFY] | Detection | IRDAI ICS Guidelines 2023 |
| `clk.dpb.initial` | Data Protection Board + each affected data principal | "without delay" — configurable internal target (default 24 h) | Becoming aware | DPDP s.8(6), Rule 7(1) |
| `clk.dpb.72h` | Data Protection Board (detailed report) | 72 hours (or longer if DPB allows on written request) | Becoming aware | Rule 7(2) |
| `clk.gdpr.72h` | Lead supervisory authority | 72 hours (late with reasons) | Becoming aware | GDPR Art. 33(1) |
| `clk.gdpr.processor` | Controller (when tenant is processor) | without undue delay | Becoming aware | Art. 33(2) |
| `clk.ccpa.*` | California AG / consumers (Cal. Civ. Code §1798.82 breach law) | "most expedient time possible"; AG copy if > 500 residents | Discovery | §1798.82 [VERIFY] |
| `clk.custom.*` | Board, insurer (cyber policy), bank partner, co-lending partner | tenant-defined | tenant-defined | Tenant (T tier) |

Escalations: notification to owner at 0 %, to CISO/DPO at 50 %, to CEO/CRO at 75 %, red banner on CXO dashboards at 90 %; lapse creates a Critical exception and an entry in the Board pack. Clocks cannot be paused except by a reason-coded Correction Entry (D-02) — e.g., "misclassified; not reportable" — dual-approved.

**FR-P12-23 — Report drafting.** For each destination, generate the field sheet and narrative: CERT-In incident reporting form fields [VERIFY current form], RBI DAKSH incident template fields (exported as XLSX/JSON matching DAKSH upload fields where published; otherwise structured DOCX), DPB intimation (nature, extent, timing, location, likely impact — Rule 7(1)) and 72-hour report (facts, circumstances, reasons, mitigation, findings on the person who caused it, remedial measures, report of intimations to data principals — Rule 7(2) [VERIFY element list]), data-principal intimation letters/SMS/e-mail in plain language with the Rule 7(1) elements, GDPR Art. 33(3) notification content, CCPA consumer notice. Vidhi drafts; DPO/CISO approve; human submits and uploads the acknowledgement (NN-08). Each submission records `submitted_at`, channel, reference number, submitting officer.

**FR-P12-24 — Post-incident.** RCA (5-whys / fishbone templates), lessons learned, control-failure links (§4H), loss event posted to `erm` loss database (P08) with three dates (occurrence, discovery, accounting), insurer claim tracking, Board/ITSC reporting, regulator follow-up queries log.

**FR-P12-25 — Drills.** Tabletop and simulation drills for CCMP (RBI NBFC 2026 para 146 requires crisis-communication drills with stakeholders including service providers) — drill records, participants, injects, timings, gaps → actions.

### 4G. ISMS scope, asset register and criticality

**FR-P12-26 — ISMS scope and context.** Record ISMS scope statement, interested parties, internal/external issues (ISO/IEC 27001:2022 clauses 4.1–4.3), roles (clause 5.3), information-security objectives (6.2) with measurement; produce the "Context of the organisation" document (DOCX) for certification audits the client may pursue.

**FR-P12-27 — Asset register.** Information assets, applications, infrastructure, cloud services, end-user devices (import from CMDB/Intune/Jamf/CSV via P18), data stores (linked to processing activities, §4B), owners, custodians, location (India / outside — feeds data-localisation checks), hosting model, internet-facing / DMZ flag, customer-facing flag, criticality (C/I/A ratings → Critical / High / Medium / Low via Governed rule `dpc.asset.criticality@<ver>`), RTO/RPO, supported-by vendor (link to `tpr`), patch-level and end-of-support dates. Criticality drives VAPT frequency (§4J), DR test requirements (§4K) and change-review intensity.

### 4H. Common control library and framework mappings

**FR-P12-28 — Common controls.** A curated common-control library (`dpc.controls`, ≤ 220 controls at v1.0, grouped by ISO/IEC 27001:2022 themes: Organisational 37, People 8, Physical 14, Technological 34 — as the backbone; plus privacy controls aligned with ISO/IEC 27701 and DPDP Rule 6 minimum safeguards; plus resilience controls aligned with ISO 22301). Each control: id, title, objective, description, control type (preventive/detective/corrective), nature (manual/automated/IT-dependent manual), frequency, owner role, test procedure (design and operating effectiveness steps), evidence expected, sampling guidance, automated-evidence connector (optional), mapped requirements.

**FR-P12-29 — Framework packs and mappings.** Load the following as P03 instrument packs whose obligations map many-to-many to common controls; mapping rows carry `coverage` (full / partial / supporting) and rationale:

| Pack | Applies to (from P15 entity profile) | Key structural elements to model |
|---|---|---|
| `CYB-RBI-NBFC-2026` — RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions 2026, RBI/DoS/2026-27/461 (31 Jul 2026) | All NBFCs, chaptered: Ch. III (NBFC-BL < ₹500 cr assets, and CICs), Ch. IV (NBFC-BL ≥ ₹500 cr), Ch. V (NBFC-ML/UL/TL excl. CICs) | Board strategy and policy (paras 6, 68–69); ITSC composition and frequency (Ch. IV paras 15–16; Ch. V paras 70–73); ISC (para 77); CISO independence (paras 81–82); CCMP (paras 25–26, 84, 139–146); VA/PT (paras 121–126); BCP/DR (paras 59, 127–138); outsourcing hooks (paras 60–64, 117); DAKSH incident reporting (paras 28, 141); repeal of earlier NBFC IT directions (para 155) |
| `CYB-RBI-BANK-ITGOV` — *(v1.1)* RBI (Commercial Banks / Small Finance Banks / Payments Banks / Local Area Banks / Regional Rural Banks – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions 2026 (DoS set of 31 Jul 2026; see `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx`), superseding the MD on IT Governance, Risk, Controls and Assurance Practices (7 Nov 2023) [VERIFY repeal clause and LAB/RRB coverage] and RBI cyber-security framework circulars for banks; UCB graded cyber framework | Commercial banks, SFBs, PBs, UCBs per category [VERIFY current consolidated instrument after Nov 2025 consolidation] | ITSC, IT Steering Committee, CISO, IS audit, BCP/DR, SOC, C-SOC baseline by UCB level |
| `CYB-SEBI-CSCRF` — SEBI Cybersecurity and Cyber Resilience Framework (20 Aug 2024 [VERIFY no.]) + clarifications (30 Apr 2025), FAQs (11 Jun 2025), timeline extension to 31 Aug 2025 | MIIs, Qualified REs, Mid-size, Small-size, Self-certification REs (categorisation rules incl. AIF investment-manager-level categorisation fixed per FY) | Category-based standards (Govern, Identify, Protect, Detect, Respond, Recover), cyber audit frequency by category, M-SOC applicability (exempt: self-certification IMs < 100 clients), cyber capability index for MIIs/Qualified [VERIFY], VAPT, SBOM, cloud framework |
| `CYB-IRDAI-ICS-2023` — IRDAI Information and Cyber Security Guidelines 2023 (24 Apr 2023) | Insurers, brokers, corporate agents, web aggregators, TPAs, IMFs (graded by access to insurer systems and revenue) | Board-approved ISMS policy, CISO, annual/periodic audit, incident reporting, log retention, data localisation [VERIFY specifics] |
| `CYB-IFSCA-2025` — IFSCA Guidelines on Cyber Security and Cyber Resilience for REs (effective 1 Apr 2025) + IFSCA MII guidelines (Apr 2026) | IFSCA REs except exempted (branches of regulated entities, GICs serving group, < 10 employees, foreign universities) subject to conditions | Governance, CISO, incident 6 h / interim 3 days / RCA 30 days, periodic cyber audit by CERT-In empanelled or certified auditor, VAPT |
| `CYB-CERTIN-2022` — CERT-In Directions (28 Apr 2022) | Every service provider, intermediary, data centre, body corporate, government organisation | 6-hour reporting; point of contact registration; ICT log retention 180 days in India; NTP sync to NIC/NPL; VPN/VPS/cloud subscriber records 5 years (where the tenant is such a provider) |
| `CYB-ISO-27001-2022` | Voluntary / certification | Clauses 4–10 + Annex A 93 controls; SoA generation |
| `CYB-ISO-22301-2019` | Voluntary | BIA, BCP, exercising |
| `CYB-NIST-CSF-2.0` | Optional mapping for global clients | Functions Govern/Identify/Protect/Detect/Respond/Recover |
| `CYB-PCI-DSS-4.0.1` | Clients that store/process/transmit card data | Applicability via asset flag `cardholder_data_env` |

**FR-P12-30 — SoA.** Generate a Statement of Applicability: each Annex A control — applicable? justification; implemented? reference to control and evidence; exclusions with justification; version and approval (CISO maker, CEO/ISC checker). Export XLSX + PDF.

**FR-P12-31 — Control testing.** Test plans auto-scheduled from control frequency and criticality; test steps; sample selection (random seed recorded for reproducibility, NN-22); results (effective / partially / ineffective); deficiencies → issues (P10 `aud.findings` shared issue model) with remediation tasks; re-test; evidence locking (NN-09). Automated evidence: connectors (P18) to cloud posture (AWS Config / Azure Policy / GCP SCC), M365/Entra (MFA coverage, admin roles), Google Workspace, EDR, vulnerability scanners — evidence snapshots hashed and time-stamped.

**FR-P12-32 — Compliance heat map.** Per framework: % requirements covered by effective controls, gaps, overdue tests; drill-down to control and evidence; export for ITSC/ISC packs.

### 4I. Cyber governance workspace (CISO)

**FR-P12-33 — Committees.** ITSC, IT Steering Committee, Information Security Committee, Cyber Crisis Management Group set up as P06 committees with seeded terms of reference from the applicable pack (e.g., RBI NBFC 2026 Ch. V: at least three directors, independent chair with ≥ 7 years substantial IT experience, at least quarterly meetings; Ch. IV: independent-director chair with CIO and CTO members, meetings no more than six months apart). Composition validators raise warnings when membership violates the pack (warning, not a hard block — the tenant may have an approved exception; exception recorded).

**FR-P12-34 — CISO quarterly review.** Template for the CISO's quarterly cyber-risk review to the ITSC/RMC (RBI NBFC 2026 para 82): threat landscape, incidents, KRIs (patch latency, critical vulnerabilities open > SLA, phishing click rate, MFA coverage, privileged accounts, backup success, DR readiness), VAPT status, audit findings, vendor cyber posture, regulatory changes (from P05). Vidhi drafts from data; CISO edits; locked once presented.

**FR-P12-35 — Policy set.** Seed model policies (P07) — Information Security Policy, Cyber Security Policy, Cyber Crisis Management Plan, Acceptable Use, Access Control, Cryptography and Key Management, Logging and Monitoring (CERT-In 180-day log retention; DPDP Rule 6 one-year retention of logs), Patch and Vulnerability Management, Secure SDLC, Change Management, Backup, BCP/DR, Data Classification, Data Retention and Disposal, Third-Party Security, Cloud Security, Remote Working/BYOD, Incident Response, Privacy Policy (internal), Privacy Notice (external), Data-Principal Rights Procedure, Breach Notification Procedure, DPIA Procedure, AI Use Policy. Each policy's mandatory-content checklist is derived from the packs so the reviewer sees "policy covers para X? yes/no".

**FR-P12-36 — Awareness and training.** Records of awareness campaigns, phishing simulations (import results CSV/API), role-based training completion (from P13 training records and FinLegal Academy links, P21), Board cyber training (RBI expects Board-level expertise/awareness [VERIFY para]).

### 4J. Vulnerability, patch and VAPT management

**FR-P12-37 — VAPT programme.** Annual plan auto-generated from the asset register and applicable packs: e.g., for NBFC Ch. V, VA at least every 6 months and PT at least every 12 months for critical systems and DMZ systems with customer interfaces, plus before/after implementation and after major change (paras 121, 124); risk-based schedule for non-critical (para 123); independent, trained testers (para 122). Engagement records: tester firm (link to `tpr`), CERT-In empanelment status and validity (where required), scope, dates, report upload, findings import (CSV/XLSX/JSON from scanners: Nessus, Qualys, OpenVAS, Burp; SARIF for SAST), CVSS v3.1/v4.0 scores, EPSS optional.

**FR-P12-38 — Remediation SLAs.** Governed defaults (tenant may tighten, not loosen below pack floors): Critical 15 days, High 30 days, Medium 60 days, Low 90 days [REC; para 125 requires remediation within set timelines — tenant policy defines them]; exceptions with compensating controls and expiry, approved by CISO + risk; re-test evidence required to close.

**FR-P12-39 — Patch compliance.** Import patch status from endpoint/patch tools; KRI patch latency; end-of-support assets flagged.

### 4K. Business continuity and disaster recovery

**FR-P12-40 — BIA and BCP register.** Business impact analysis per process (MTPD, RTO, RPO, minimum business continuity objective), dependencies (assets, vendors, people), BCP documents (P07), call trees (from P13 employee directory), alternate sites.

**FR-P12-41 — Tests.** Test calendar from the packs (NBFC 2026: BCP tested at least annually and after significant changes — para 59(4); DR drills for critical systems at least half-yearly — para 129; DR site as primary for at least a full working day — para 131; near-zero RPO for critical systems — paras 134–135; primary and DR geographically separated — para 102; identical configuration and patch level — para 137). Test record: scenario, scope, start/end, achieved RTO/RPO vs target, issues, sign-off; Board review at least annually (para 73(6)).

### 4L. Third-party and vendor master; outsourcing register

**FR-P12-42 — Vendor master.** Legal name, PAN/GSTIN/CIN/LEI (fetched via P18 KYB adapters where available), group/related-party flag (Companies Act s.2(76); intra-group outsourcing), jurisdiction(s) of service delivery and data storage, services provided (catalogue), contracts (link to DMS), SPOCs, certifications (ISO 27001, SOC 2 Type II report period, PCI AOC, CERT-In empanelment) with expiry reminders, insurance, financial health snapshot (from KYB provider [VERIFY vendor]), sub-contractors (fourth parties).

**FR-P12-43 — Outsourcing classification.** Two registers as RBI expects: **financial-services outsourcing** and **IT outsourcing** (NBFC Outsourcing Directions 2025; equivalent bank/UCB instruments via packs). Materiality questionnaire implements para 14 factors (importance, financial impact, reputational impact, cost, aggregate exposure to provider, customer protection) and para 58(2) for IT (disruption to business operations; unauthorised access/loss/theft of customer information). Output: material / non-material with reasons; non-outsourceable activity guard (para 15: core management functions incl. internal audit, strategic and compliance functions; KYC compliance decision for deposit accounts, loan sanction, investment-portfolio management) — attempting to register such an arrangement raises `LDC-TPR-010` (blocking unless the arrangement is re-scoped; e.g., internal-audit **co-sourcing** of specialised skills where the pack permits, recorded with justification [INTERP]).

**FR-P12-44 — Inherent risk tiering.** Tiers 1–4 from data access (personal data volume, sensitive data, credentials), system access, criticality of supported process, substitutability, concentration (multiple critical services with one provider; para 117 concentration and single-point-of-failure), offshore delivery, sub-contracting. Tier drives DDQ depth and review frequency.

**FR-P12-45 — Due diligence.** DDQ library (questions with evidence requests): information security (ISO 27001 Annex A-aligned short form, long form), privacy (DPDP processor obligations: s.8(2) contract, Rule 6 safeguards; GDPR Art. 28(3) terms), BCP, financial, legal/litigation, reputational, regulatory status, sanctions/adverse media (P18 screening adapter, optional), data localisation (IT outsourcing contract must address storage of data in India — para 74 [VERIFY clause]), sub-contractor approvals, right to audit acceptance. Vendor portal sends questionnaires, captures answers and documents; Vidhi pre-scores answers and highlights gaps (NN-14; reviewer decides).

**FR-P12-46 — Contract-clause checklist.** For each material arrangement, checklist of minimum provisions: para 34 (financial outsourcing — service standards, access to records, audit rights, RBI inspection access, confidentiality, sub-contractor approval, termination, BCP) and para 74 (IT — additionally sub-contractor liability, data storage in India, incident reporting, SLAs, supply-chain disclosure, non-disclosure) [VERIFY full lists against text]; status per clause (present / partially / absent / waived-with-approval), clause location in the contract (page/clause), AI-assisted clause extraction from uploaded contract (Vidhi, citations to page; human confirms). Renewal guard: existing IT outsourcing contracts must be compliant at renewal or by 10 Apr 2026, whichever earlier (para 2) — dashboard shows any still non-compliant after that date as overdue.

**FR-P12-47 — Ongoing monitoring.** SLA metrics (import or manual), incidents, complaints linked from P14, annual review of financial and operational condition (para 38 for financial outsourcing; risk-based periodic for IT, para 80), audits of the provider (risk-based, para 78; Audit Committee monitors internal audit of outsourced activities, para 12(2)), certification expiry, adverse news.

**FR-P12-48 — Board/RMC half-yearly review pack.** Central record of material arrangements reviewed half-yearly by the Board or RMC (paras 12(1)(vii), 36); IT services inventory and supply-chain dependencies (para 82); pack generated as DOCX/PDF with register extract (XLSX).

**FR-P12-49 — Intra-group and offshore.** Intra-group arrangements: Board-approved policy, written SLAs on resource sharing, arm's-length terms, same risk management as unrelated parties, customer disclosure of which entity provides the service (paras 45–51, 90–92) — checklist and evidence. Offshore: jurisdiction confidentiality, country-risk monitoring, governing law, RBI and NBFC access to records, original records in India (paras 52–53, 93–94).

**FR-P12-50 — Exit and termination.** Exit plan per material arrangement (scenarios: insolvency, breach, regulatory direction, strategic; alternative provider or insourcing; data return and destruction certificate — paras 41, 84–88); customer publicity on termination of a customer-facing provider (paras 44, 89) — task template with notice draft.

### 4M. Vendor portal and vendor incidents

**FR-P12-51 — Vendor portal.** Lightweight external surface (`apps/web` route `/vendor`) with magic-link + OTP and optional SSO; vendor users see only assigned DDQs, evidence requests, contract attestations and the incident-report form. Vendor incident report captures **provider detection time** and starts `clk.rbi.outsourced.6h` immediately (para 61). Everything a vendor submits is quarantined, malware-scanned (P07) and reviewed before acceptance.

### 4N. Data localisation and cross-border transfer checks

**FR-P12-52 — Transfer register.** Every transfer recorded with destination country, recipient, mechanism (DPDP s.16 — permitted unless the destination is restricted by Central Government notification; sector rules may be stricter, e.g., RBI payment-data storage in India [VERIFY]; GDPR Ch. V: adequacy / SCCs / BCRs / derogations; CCPA contract terms), TIA reference, and a check against the current restricted-countries list (Governed list `dpc.transfer.restricted_countries`, empty until notified [VERIFY]). Any asset or vendor storing data outside India for an RBI/SEBI/IRDAI/IFSCA-regulated tenant raises a review task.

### 4O. AI governance hooks (ISO/IEC 42001, CCPA ADMT, DPDP Rule 13) — *(v1.1: retained as the bridge from privacy/cyber; the full module is §4P)*

**FR-P12-53 — AI system inventory.** Client's AI/ML systems (credit scoring, fraud models, chatbots, voice bots, collections prioritisation, document AI, Vidhi itself as a vendor AI), purpose, data used, decision significance, human oversight, vendor, model version, validation status (links to P08 model risk), monitoring metrics (drift, bias), incidents.

**FR-P12-54 — AI impact assessment.** Template aligned with ISO/IEC 42001:2023 Annex A controls (AI policy, impact assessment, data for AI, lifecycle, third-party) and CCPA ADMT obligations (pre-use notice, opt-out/appeal where required, access to ADMT information, risk assessment — from 1 Jan 2027) and DPDP Rule 13 SDF algorithmic due diligence. RBI expectations on model risk and fair lending are linked via P08 [VERIFY current RBI AI/ML framework status — FREE-AI committee report Aug 2025 is guidance, not a direction].

---


### 4P. AI Governance module `aig` and overlay `OV_AI` *(v1.1; D-36; Appendix AA §AA.12)*

**FR-P12-55 — Module, packaging and scope.** Build module `aig` (PostgreSQL schema `aig`) as sub-iteration **P12e** after P12a. It implements overlay family `OV_AI` (P15 §4Q), content template `LDC-TPL-AI-GOV-v1.0` and Part-2 command `part2_prompts/26_AI-GOV_Command.md`, sold as the **AI Governance** add-on (P20; included in Enterprise). It attaches to any entity family whose profile answers "uses AI/ML in any business process" = yes, or whenever the tenant adopts an AI-GOV instrument from the Regulation Catalogue. FR-P12-53/54 (§4O) become the privacy and model-risk bridges into this module; `dpc.ai_systems` is migrated into `aig.ai_systems` by an expand–contract migration (NN-11) with a compatibility view.

**FR-P12-56 — AI system register ("no use unless registered").** Fields per Appendix AA §AA.12.3: name, business owner, technical owner, legal entity, department, description, lifecycle stage (idea, development, validation, production, retired), deployment type (in-house, vendor SaaS, vendor model fine-tuned, open model self-hosted, agent), vendor link (`tpr.vendors`), models and versions, data categories (personal, sensitive, children's, financial), affected parties (customers, employees, public), decision role (assistive, decision-support, automated decision), autonomy level (L0–L4 vocabulary of Appendix AA §AA.3), regions of processing, retired-on and retained-until. A system may move to `IN_PRODUCTION` only when registered, classified and approved (state machine §5.8). A continuous control-monitoring test (Appendix AA §AA.11) flags evidence of production use without registration — e.g., a vendor in `tpr` tagged "AI feature" with no linked system, a P18 connector to an AI service, a contract in DMS with an AI clause — and opens a compliance issue, not an automatic status (NN-47).

**FR-P12-57 — Discovery that does not slow the client down.** Vidhi agent VA-15 (AI Governance Analyst, Appendix AA §AA.4.2) proposes register entries from five sources: vendor register (AI-feature tags and DDQ answers), integration connectors, DMS contracts containing AI terms, a 10-question department questionnaire generated from the AI-GOV sheet, and LDC's own Vidhi usage. Proposals arrive in a single review grid; the owner accepts, merges or rejects in bulk with a 24-hour undo window (NN-49). VA-15 runs at autonomy L1 (propose only) unless the tenant raises it (never above L2 for register writes, NN-50).

**FR-P12-58 — Use cases and materiality.** Each system has one or more use cases: process (credit underwriting, pricing, collections prioritisation, KYC/AML screening, fraud detection, marketing, customer service chatbot/voicebot, claims, HR screening, compliance and internal audit, document AI), materiality (customer impact × scale × reversibility × autonomy), explainability need, and the customer-facing flag that triggers disclosure and human-route requirements.

**FR-P12-59 — Multi-framework risk classification.** For each use case the deterministic rules in rule pack `aig.classify@<ver>` compute a proposed class under each enabled framework: RBI FREE-AI materiality tier (committee report, not a direction — label "guidance"); RBI model-risk tier (draft guidance of 2026 — label "draft" [VERIFY final]); SEBI AI/ML expectations (consultation 20 Jun 2025 — [VERIFY final circular]); EU AI Act class (prohibited practice screen under Art. 5; high-risk if an Annex III area such as creditworthiness evaluation of natural persons or life/health insurance risk assessment and pricing, or employment decisions [VERIFY Annex III point numbering and the Digital Omnibus application dates]; limited-risk transparency under Art. 50; minimal); ISO/IEC 42001 risk rating; NIST AI RMF profile. VA-15 may add a rationale draft; the **AI governance officer** (`ten_kmp` sub-type AIO, or CRO/CCO if not appointed) approves. AI never sets the final class (NN-47); the approver ≠ the system owner (NN-05).

**FR-P12-60 — Impact assessments.** Templates: AI impact assessment aligned to ISO/IEC 42005; DPIA hand-off to §4E where personal data is used (single assessment record with two lenses, not two forms); fundamental-rights impact assessment prompt where the tenant is an EU-scope deployer of a high-risk system [VERIFY Art. 27 scope]; CCPA ADMT risk assessment where `DATA-US-CCPA` applies (from 1 Jan 2027). Sections pre-fill from the register and use case; approvals follow the tier (High: RMC or Board clearance recorded as a P06 resolution link).

**FR-P12-61 — Validation workspace.** Validation types: conceptual soundness, data quality, outcome analysis/back-testing, benchmarking, stress and adversarial testing, red-teaming of customer-facing generative systems, robustness, privacy leakage, explainability, bias/fairness. Independence: the validator (`ten_model_validator`) must not be the developer, owner or a member of the owning team (SoD rule in Appendix D; NN-05). Default frequencies by tier (Tenant-tightenable within Governed floors): High annually and before any material change; Medium every two years; Low every three years. Findings become issues in P08 with owners and due dates.

**FR-P12-62 — Fairness and bias evidence without collecting new sensitive data.** The module records fairness tests the client performs: metric (e.g., demographic parity difference, equal-opportunity difference, adverse-impact ratio — the 0.8 "four-fifths" ratio is shown as an *indicator*, never as a legal threshold), protected or proxy attribute used, data source and lawful basis (DPDP s.7; no new collection of sensitive attributes merely to test — use available, consented or aggregate data), result, mitigation and sign-off. Explainability artefacts (reason codes, feature attributions, customer-facing explanation text) are stored per use case.

**FR-P12-63 — Human oversight, override and kill-switch controls.** For each system: oversight design (human-in-the-loop, on-the-loop, out-of-loop with sampling), override procedure, suspension/deactivation path, kill-switch owner, last kill-switch test (date, scenario, time to effect, result) and next due (`aig.kill_switch_test_interval_days`, default 90), fallback process, and the customer's route to a human. A CCM test raises an issue when a kill-switch test is overdue.

**FR-P12-64 — Monitoring.** Metrics per system with thresholds: data/concept drift, performance, fairness metrics, hallucination or groundedness rate (generative), override rate, customer complaints tagged "AI" from P14, incident count. Breaches feed KRIs in P08; trend charts on the AI Governance dashboard; imports from monitoring tools via P18 (`AI_MONITORING_PORT`, CSV fallback).

**FR-P12-65 — AI incident register.** Categories: harmful or biased output, data leakage, prompt-injection exploitation, unsafe autonomous action, model outage with customer impact, third-party model change without notice. Each AI incident links to the §4F incident where personal data or cyber elements exist so the DPB, CERT-In, RBI DAKSH and GDPR clocks start from the earliest detection time (NN-33); root cause, remediation and lessons feed validation plans.

**FR-P12-66 — Disclosures.** Drafting and version control (via P07) of customer-facing AI notices, EU AI Act Art. 50 transparency notices, synthetic-content labels under the IT (Intermediary Guidelines and Digital Media Ethics Code) Amendment Rules 2026 where the tenant is an intermediary [VERIFY applicability], and annual-report/website AI-use disclosure drafts in the style recommended by the FREE-AI report. Numbers in disclosures come from register queries only (NN-37).

**FR-P12-67 — Vendor AI assurance.** For each vendor model or AI SaaS: model card, training-data and no-training terms, data location, sub-processors, audit and information rights, incident notification terms, exit and continuity plan, concentration flag (share of the tenant's AI systems on its top-1 and top-3 providers). The tenant can **import LawDocsComply's own vendor AI assurance pack** in one click (D-38), pre-filling LDC as a vendor with its model cards, routing and region attestations, evaluation and red-team summaries.

**FR-P12-68 — AI policy and Board AI report.** The P07 policy library seeds a Board-approvable AI policy template (governance roles, risk appetite for AI, classification, validation, human oversight, incidents, disclosures, vendor AI). The Board AI report (registered as a P28 report definition) shows inventory by tier and lifecycle, validations due/overdue, kill-switch tests, incidents, disclosures, vendor concentration and framework coverage, generated quarterly or on demand.

**FR-P12-69 — Cross-framework control map.** One control, many frameworks (Appendix AA §AA.12.5): each `aig` control maps to FREE-AI recommendation, RBI model-risk principle (draft), SEBI paragraph (when final), MeitY guideline, DPDP section/rule, EU AI Act article, ISO/IEC 42001 Annex A control, NIST AI RMF subcategory and IMDA dimension; evidence uploaded once satisfies every mapped requirement. AI-GOV Excel column N "Also satisfies: …" builds the map on import.

**FR-P12-70 — Inventory import and speed.** Bulk import of an existing AI inventory from Excel (`LDC-DT-AI-INVENTORY-v1.0`), column mapping remembered per tenant; classification wizard ≤ 10 questions per use case with "why" explanations; duplicate detection on name/vendor/model.

**FR-P12-71 — Customisation.** Tenants rename tiers, add internal frameworks (their own AI policy as a framework), add metrics and thresholds, tighten validation frequencies and retention, choose which frameworks are shown, and add custom fields to the register (P02 form builder).

**FR-P12-72 — Retention.** AI system, validation and decommission records are retained for `aig.retention_years` (Governed, default 10, aligned to the RBI draft model-risk expectation [VERIFY final]) from retirement, subject to legal hold.

### 4Q. DPDP Schedules as linked reference data *(v1.1; G5 TM-729/736)*

**FR-P12-73 — Seed each Schedule as reference data linked to the rule that points to it** (`dpc.ref_schedules`, `dpc.ref_schedule_items`), so the engine resolves, for any processing activity, the exact retention period, SDF duty set, children's-data exemption or information-request handling, with traceability to rule and schedule:

| Schedule | Title (short) | Seeded as | Product use | Linked rule [VERIFY rule numbers against G.S.R. 846(E)] |
|---|---|---|---|---|
| First | Consent Manager — registration conditions (Part A) and obligations (Part B) | Eligibility (Indian company, ≥ ₹2 crore net worth), governance, technical and operational duties | Consent Manager integration readiness only (D-29); conditions shown when a tenant integrates a registered Consent Manager | Rule 4 |
| Second | Standards for processing by the State and its instrumentalities | Conditions for s.7(b) and s.17(2)(b) processing | Lawful-basis and exemption logic for government-linked tenants (e.g., State co-operative federations acting as instrumentalities) | Rule 5 |
| Third | Classes of Data Fiduciaries, purposes and time periods (retention) | Class rows: e-commerce entities with ≥ 2 crore registered users; online gaming intermediaries with ≥ 50 lakh users; social media intermediaries with ≥ 2 crore users — three years from the last approach or the commencement of the Rules, whichever is later; 48-hour advance intimation before erasure | `dpc.retention_classes` defaults and the erasure-notice timer | Rule 8 |
| Fourth | Classes of Data Fiduciaries and purposes exempt from certain children's-data provisions | Rows such as clinical establishments, allied healthcare and educational institutions, child-care and creche, transport of children — each with the permitted purpose and condition | Children's-data exemption flags in the tree generator | Rules 10–12 |
| Fifth | Terms and conditions of service of the Chairperson and Members of the Board | Reference only | "i" help | Rule 18 |
| Sixth | Terms and conditions of service of officers and employees of the Board | Reference only | "i" help | Rule 19 |
| Seventh | Purposes for which information may be called for and the authorised persons | Table of purposes and authorised persons | Government/Board information-request handling workflow (request intake, authority verification, response, log) | Rule 23 |

**FR-P12-74 — Log and data retention for information calls.** Where the Rules require a Data Fiduciary to retain personal data, associated traffic data and processing logs for a minimum period for the Seventh-Schedule purposes [VERIFY Rule 8(3) — one year], the retention engine applies that floor and shows it as Locked in the activity's retention tab.

**FR-P12-75 — Schedule amendments.** A change to any Schedule is a content release (P05) that re-runs the tree generator (§4R) for affected tenants and produces a diff for DPO approval; no instance changes without approval (NN-34).

### 4R. Data-compliance tree generator — full specification *(v1.1; extends FR-P12-03; G5 TM-745/746)*

**FR-P12-76 — Canonical hierarchy (binding).** `Organisation (legal entity)` → `Role(s)` (Data Fiduciary, notified SDF, Data Processor, Consent Manager — never inferred; GDPR controller/processor; CCPA business/service provider) → `Processing activity (ROPA row)` → `Applicable instrument` (DPDP Act and Rules, IT Act/SPDI while in force, CERT-In Directions, sector overlays, GDPR, CCPA) → `Obligation` (tagged with DPDP phase `effective_from`) → `Artefact / filing / register` → `Occurrence / task or always-on control`. A **common-allied layer** (IT Act s.43A/SPDI until omitted, CERT-In 6-hour reporting and 180-day logs) attaches at entity level and is in force now; DPDP obligations attach with phase dates; GDPR and CCPA overlays attach when nexus flags are true.

**FR-P12-77 — Algorithm (deterministic; rule pack `dpc.applicability@<ver>`).**

```text
function buildDataTree(entity, asOf):
  facts  = profileFacts(entity)                      # P01/P15 + FR-P12-04 wizard (≤ 12 questions)
  ropa   = approvedActivities(entity, asOf)          # §4B
  tree   = alliedLayer(entity, asOf)                 # IT-SPDI (until effective_to), CERT-In
  for role in facts.roles:                           # union across roles held
    for rule in applicabilityRules(role, asOf):
      if rule.unconditional or rule.condition(facts, ropa):     # children, disability, processor, SDF, EU, CA, cross-border
        for ob in obligations(rule.instrument, asOf):
          node = tree.add(ob, artefacts(ob), effective_from = phaseDate(ob))
          node.why = explain(rule, facts, ropa)       # facts and rule lines used ("why does this apply?")
  for activity in ropa:
    tree.attachRetention(activity, resolveRetention(activity, ThirdSchedule, sectorFloors))
  if facts.eu_nexus: tree += gdprOverlay(ropa)
  if facts.ca_nexus and ccpaThresholdsMet(facts): tree += ccpaOverlay(ropa)
  dedupe(tree, key = obligation_ref)                 # P15 §4N canonical key; most-stringent-wins
  return tree

function materialise(entity, newTree):
  diff = compare(currentTree(entity), newTree)       # added / retired / changed nodes
  proposal = changeSet(diff)                         # pre-phase nodes → READINESS tasks; active → live instances
  route(proposal, maker = DPO delegate, checker = DPO)   # NN-05; nothing changes before approval (NN-34)
```

**FR-P12-78 — Phase awareness.** Before a phase date, obligations materialise as **readiness** tasks (status `in_progress_interim` on readiness checkpoints) with countdowns; on the phase date (13 Nov 2026 for Consent-Manager-related items; 13 May 2027 for core fiduciary duties) a scheduled job regenerates, flips readiness to active with live due dates and clocks, and keeps readiness history (NN-07). Dashboards show "Ready / Not ready" per obligation family before the date.

**FR-P12-79 — Triggers and edge cases.** (a) **SDF notification** recorded with gazette reference → adds the Rule 13 sub-branch (annual DPIA and audit, DPO based in India, algorithmic due diligence, any data-localisation conditions notified). (b) **New processing activity** → its notice, consent/legitimate-use, retention and rights obligations. (c) **Consent withdrawal / erasure** → downstream erasure tasks across processors and the retention log. (d) **Transfer restriction** notified under s.16 → flags affected transfers and opens TIA review. (e) **Processor-only tenants** (e.g., a BPO or TechFin acting only for others) → no notice/consent duties of their own; contractual processor obligations, security safeguards, breach notification to the fiduciary, sub-processor controls. (f) **Children's data** → verifiable parental consent artefacts, prohibition checks on tracking/behavioural monitoring/targeted advertising, Fourth-Schedule exemptions where the tenant's class qualifies. (g) **Persons with disability** → lawful-guardian consent artefacts. (h) **Employee data** → legitimate-use basis under s.7(i) where applicable, linked to P13 notice (NN-25). (i) **Group entities** → each legal entity gets its own tree; a group view aggregates (NN-24).

**FR-P12-80 — Worked examples (seed fixtures).** (1) *Middle-Layer NBFC with a digital lending app, an LSP (Udofin) and co-lending partners*: roles Data Fiduciary (borrowers, employees) and Processor (none); activities borrower onboarding, KYC (CKYC upload), credit bureau reporting, collections, marketing, employee HR; instruments DPDP + IT-SPDI (transition) + CERT-In + RBI NBFC Cybersecurity Directions 2026 + RBI Digital Lending obligations on data (via sector overlay); obligations include itemised notice per purpose, consent for marketing, legitimate use where permitted, rights desk, breach clocks (DPB, CERT-In 6 h, RBI DAKSH 6 h), retention per sector floors (e.g., KYC records per PML Rules) overriding shorter DPDP defaults, processor DPAs with the LSP and vendors. (2) *SDF e-commerce company serving EU users* (owner baseline, Architecture Part 3): DPDP + Rule 13 sub-branch, children's data branch, Third-Schedule three-year retention with 48-hour pre-erasure notice, common-allied layer, GDPR overlay (lawful basis, Art. 13/14 notices, one-month DSAR, Art. 30 records, 72-hour breach, SCCs). Both fixtures are golden tests (`tests/golden/dpc_tree_*`).

### 4S. Default data-compliance RACI *(v1.1; G5 TM-752)*

**FR-P12-81 — Seeded RACI (Tenant-editable; changes audited).** Used to route tasks, set default approvers and populate the "who does what" card on each obligation:

| Activity | DPO | CISO | Legal | Business owner | Maker | Board |
|---|---|---|---|---|---|---|
| Maintain ROPA / data inventory | A | C | C | R | R | I |
| Privacy notices and consent management | A | C | C | R | R | I |
| Data-principal rights requests | A | C | C | R | R | I |
| Personal-data breach reporting (DPB 72 h) | A | R | C | C | R | A (informed and oversight) |
| CERT-In incident reporting (6 h) | C | A | C | C | R | I |
| DPIA and data audit (SDF) | A | C | C | C | R | A (approves) |
| Retention and erasure schedules | A | C | C | R | R | I |
| Processor / DPA management | A | C | R | R | R | I |
| GDPR / CCPA overlay (where applicable) | A | C | R | C | R | A |
| Responding to the Data Protection Board | A | C | R | C | R | A |
| AI system register and classification *(new)* | C | C | C | R | R | I (Board AI report) |

The AI governance officer (AIO) is Accountable for the last row where appointed. Tenants may add roles (e.g., CCO, CRO) and change letters; the engine refuses a row with no "A" or with the same person as R and A for a maker-checker activity (NN-05).

### 4T. TPRM accelerators *(v1.1; G2 IMP-115–IMP-120)*

**FR-P12-82 — Questionnaire criteria extraction (IMP-115).** Upload any vendor or regulator questionnaire (XLSX, DOCX, PDF); Vidhi extracts questions, maps each to the tenant's standard DDQ baseline (`tpr.ddq_templates`) and to control-library items, flags unmapped questions, and proposes a merged baseline. A reviewer confirms mappings in a side-by-side grid; nothing enters the baseline without approval (NN-14, NN-47).

**FR-P12-83 — Cited vendor-document review (IMP-116).** For a vendor's evidence pack (SOC 2 report, ISO certificate and SoA, policies, pen-test summary, insurance), Vidhi drafts an answer to each DDQ question with page-level citations, confidence and "not found" markers; bulk review of up to 50 questions on one screen; the reviewer accepts, edits or rejects each; the vendor tier and approval remain human decisions.

**FR-P12-84 — Reassessment triggers (IMP-117).** Rule-driven triggers create reassessment tasks: new vendor response or document upload; certificate or report expiry (SOC 2 period end + 12 months, ISO certificate validity); vendor incident; materiality change; contract renewal or scope change; adverse media or sanctions hit (when a screening connector is enabled); regulatory change touching outsourcing. Trigger set is Tenant-configurable (`tpr.reassessment.triggers`).

**FR-P12-85 — Deterministic outsourcing materiality (IMP-118).** Materiality is computed by a rule-pack questionnaire per regulator (NBFC Outsourcing Directions 2025, bank/UCB/RCB equivalents of 28 Nov 2025, IRDAI, SEBI) — e.g., customer impact, regulatory-compliance dependence, data sensitivity, cost/substitutability, concentration, offshore, intra-group; Vidhi may only summarise the rationale. Overrides need a reason and a checker (NN-05) and are recorded as Correction Entries.

**FR-P12-86 — Immutable detection source (IMP-119).** Incident intake records `detected_at` and `detection_source` (internal monitoring, vendor notification, customer complaint, regulator, CERT-In advisory, media) with the evidence of that time; the clock start used for each regulatory clock is the earliest legally relevant time (NN-33) and can change only by Correction Entry.

**FR-P12-87 — Inbound due-diligence questionnaires (IMP-120).** Tenants answering questionnaires from banks, co-lenders, investors or LSP partners use an **answer library**: Vidhi drafts answers citing the tenant's own approved evidence (policies, certificates, test results) with links; the owner approves each answer; approved answers are reused next time (`tpr.ddq.answer_library.enabled`); exports to the requester's format.

**FR-P12-88 — Vendor onboarding in one screen.** Single form for a new vendor/arrangement: company data pre-filled via P18 `COMPANY_DATA_PORT` (licensed data, no scraping), materiality questionnaire, DDQ tier auto-selected, contract-clause checklist, approval routing — target ≤ 10 minutes for a non-material vendor.

**FR-P12-89 — Outsourcing register auto-entry for LawDocs delivery.** When a client activates a delivery grant (P22) and the client is an RE, an outsourcing-register entry for LawDocs is proposed automatically with the arrangement type and data access scope, for the client's approval.

### 4U. Faster workflows and customisation *(v1.1)*

- **Privacy home quick actions**: "Log a breach", "New rights request", "Add processing activity", "Run tree diff" — each one click from SCR-DPC-01; keyboard shortcuts registered in P02.
- **Pre-filled assessments**: DPIA, TIA, AI impact assessment and vendor DDQ pre-fill from linked records; only deltas are asked.
- **Review next** for DPIA approvals and DDQ reviews (NN-46); bulk only for `bulk_approvable` items such as low-risk discovery proposals, with undo (NN-49).
- **Saved views and filters** per role; tenant-defined columns on registers.
- **Customisable** (registered in §9): RACI letters, incident taxonomy additions (on top of regulator categories), internal clock targets (never later than statutory, NN-33), DDQ templates, materiality weights within Governed bounds, AI tiers and validation frequencies (within floors), dashboard widgets.
- **Global readiness** *(v1.1)*: foreign subsidiaries' data-protection packs (UK GDPR, Singapore PDPA, UAE PDPL, DIFC/ADGM) attach through P25 jurisdiction packs; their records live in the subsidiary's home-region cell (NN-24); group dashboards show aggregates only.


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P12-X01 — Contracts to TPRM.** A P26 contract flagged as outsourcing (RBI outsourcing directions), cloud/IT service or personal-data processing creates or links a TPRM arrangement (`tpr.arrangements`) and a DPDP processor record; the vendor master is shared by P12, P26 and P27 (one vendor record, many roles).

**FR-P12-X02 — AI governance location and export.** The AI Governance module (`aig`, §4P) has one menu location — the top-level "AI Governance" menu of Appendix C — and exports to folder `29 AI Governance - Systems, Assessments and Incidents/` (Appendix M is authoritative).

**FR-P12-X03 — Monitoring and screening ports.** AI-system monitoring metrics come through `AI_MONITORING_PORT`; vendor onboarding uses `COMPANY_DATA_PORT` (India) or `ENTITY_REGISTRY_PORT` (foreign) for pre-fill and the sanctions/adverse-media `ScreeningProvider` (Appendix L §L.13), all as proposals for analyst decision (NN-47).

## 5. Workflows and state machines

### 5.1 Processing activity (`dpc.processing_activities.status`)
`DRAFT → IN_REVIEW (dept head) → DPO_REVIEW → APPROVED → (CHANGE_REQUESTED → IN_REVIEW …) → RETIRED`. Guards: APPROVED requires purpose, basis per applicable law, retention class, at least one system, DPIA screening done. Any change after APPROVED creates a new version; the old version remains in the ROPA history (NN-07). Retirement requires a disposal record (data deleted/archived per retention).

### 5.2 Rights request (`dpc.rights_requests.status`)
`RECEIVED → (ID_PENDING ↔ ID_VERIFIED | ID_FAILED→CLOSED_UNVERIFIED) → TRIAGED (law(s), type, clock) → IN_FULFILMENT (fan-out tasks) → RESPONSE_DRAFTED → RESPONSE_APPROVED (checker ≠ maker) → RESPONDED → CLOSED → (REOPENED within 30 days [REC] → TRIAGED)`; side states `EXTENDED` (with extension notice sent, GDPR/CCPA only), `DENIED_PARTIAL`, `DENIED` (reason code required), `ESCALATED_GRIEVANCE` (handoff to P14). Timers: clock per law (§4D) with 50/75/90 % alerts; extension allowed only where the law allows and only once.

### 5.3 Incident (`dpc.incidents.status`)
`REPORTED → TRIAGE (classification questionnaire) → CLASSIFIED (clocks started) → CONTAINMENT → ERADICATION → RECOVERY → NOTIFICATIONS_COMPLETE (all mandatory clocks submitted or formally closed as not-applicable via Correction Entry) → POST_INCIDENT_REVIEW → CLOSED`. Parallel region "Notifications": per destination `NOT_REQUIRED | PENDING | DRAFTED | APPROVED | SUBMITTED (ack ref) | FOLLOW_UP_REQUESTED | CLOSED`. Guards: CLOSED blocked while any destination is PENDING/DRAFTED/APPROVED; RCA required for S1/S2; loss event created for incidents with financial impact.

```
on IncidentClassified(i):
  for rule in rulepack('dpc.incident_clocks', at=i.detected_at, tenant=i.tenant):
    if rule.applies(i.classification, tenant.profile):
      start = i[rule.start_event]            # noticed_at | detected_at | aware_at | provider_detected_at
      clock.start(key=rule.key, start=start, window=rule.window, owner=rule.owner_role,
                  escalations=[0.5,0.75,0.9], on_lapse=raise_exception('CRITICAL'))
```

### 5.4 DPIA (`dpc.assessments.status`)
`SCREENING → (NOT_REQUIRED (recorded) | DRAFT) → DPO_REVIEW → MITIGATION (tasks) → RESIDUAL_ASSESSED → APPROVED | REJECTED (processing must not start) → REVIEW_DUE (timer) → DRAFT (new version)`.

### 5.5 Outsourcing arrangement (`tpr.arrangements.status`)
`PROPOSED → MATERIALITY_ASSESSED → DUE_DILIGENCE → CONTRACT_REVIEW → APPROVED (approval authority per Board-approved policy; maker-checker) → ACTIVE → (UNDER_REVIEW periodic) → EXIT_PLANNED → TERMINATING → TERMINATED (data-destruction certificate)`. Guard: ACTIVE requires all mandatory clauses present or waived with approval; material arrangements require Board/committee approval record where the tenant's policy says so.

### 5.6 Control test (`dpc.control_tests.status`)
`SCHEDULED → IN_PROGRESS → SUBMITTED (maker) → REVIEWED (checker) → (EFFECTIVE | DEFICIENT → ISSUE_RAISED → REMEDIATED → RETESTED)`. Locked after REVIEWED; edits only via Correction Entry (NN-02).

### 5.7 VAPT finding (`dpc.vuln_findings.status`)
`OPEN → ASSIGNED → IN_REMEDIATION → (EXCEPTION_REQUESTED → EXCEPTION_APPROVED (expiry) | REJECTED) → FIXED_PENDING_RETEST → CLOSED_VERIFIED | REOPENED`. SLA timer from `identified_at` by severity.

---


### 5.8 AI system (`aig.ai_systems.status`) *(v1.1)*
`REGISTERED → CLASSIFIED (class approved by AIO) → ASSESSED (impact assessment approved; DPIA linked if personal data) → VALIDATED (independent validation passed or passed-with-conditions) → APPROVED_FOR_USE (approval authority by tier; High = RMC/Board resolution link) → IN_PRODUCTION → UNDER_REVIEW (material change, threshold breach, incident) → SUSPENDED (kill switch or override) → RETIRED`. Guards: `IN_PRODUCTION` requires a current validation and a kill-switch test within interval; `SUSPENDED` can be entered by the kill-switch owner alone (safety), exit needs a checker; `RETIRED` keeps records for `aig.retention_years`. Events: `AISystemRegistered`, `AISystemClassified`, `AISystemApproved`, `AISystemSuspended`, `AISystemRetired`.

### 5.9 Data-compliance tree change set *(v1.1)*
`GENERATED → PROPOSED (diff ready) → APPROVED | REJECTED → MATERIALISED`. Timers: phase-date regeneration at 00:05 IST on the phase date; facts change triggers regeneration within 5 minutes. A rejected change set keeps the current tree and records the reason.

## 6. Screens and UX

Menu: **Data & Cyber** (left rail), with sub-menus Privacy, Cyber & IT, Third Parties, Incidents, AI Governance, Reports. Every screen header has an "i" button keyed `hlp.dpc.<screen>` (P23).

| Screen ID | Name | Menu path | Key content and design |
|---|---|---|---|
| SCR-DPC-01 | Privacy home (DPO dashboard) | Data & Cyber › Privacy | Cards: open rights requests by clock status; DPIAs due; consent withdrawals in last 30 days; incidents with privacy impact; DPDP readiness by phase (13 Nov 2026, 13 May 2027 countdowns); law packs active; quick actions |
| SCR-DPC-02 | Processing activities | › Privacy › Activities | Grid with saved views, bulk edit owner/retention, import from Excel, "i" per column; row side-panel with data map |
| SCR-DPC-03 | Activity detail | (drill) | Tabs: Overview, Data, Bases by law, Systems & recipients, Transfers, Retention, Controls, Assessments, History (versions, diff) |
| SCR-DPC-04 | ROPA export | › Privacy › ROPA | Choose view (DPDP / GDPR controller / GDPR processor / CCPA), entity, date-as-of (bitemporal), format |
| SCR-DPC-05 | Notice designer | › Privacy › Notices | Left: purposes from activities; centre: live preview (mobile/desktop); right: compliance checklist per law; translation status per language |
| SCR-DPC-06 | Consent ledger | › Privacy › Consent | Search by token, purpose, date; withdrawal propagation status; export artefacts |
| SCR-DPC-07 | Rights desk | › Privacy › Requests | Kanban by status + clock colour; filters by law/type; one-click "verify identity", "generate tasks", "draft response" |
| SCR-DPC-08 | Request detail | (drill) | Timeline, identity evidence, tasks per system, response composer, extension notice, closure attestation |
| SCR-DPC-09 | Assessments | › Privacy › Assessments | DPIA/TIA/LIA/AI list; heat map; due reviews |
| SCR-DPC-10 | Incident register | › Data & Cyber › Incidents | Table with live clock chips per destination; red banner for clocks ≥ 75 %; "Report incident" primary button visible on every Data & Cyber screen |
| SCR-DPC-11 | Incident war-room | (drill) | Classification, clocks panel, task board (containment/eradication/recovery), communications log, regulator drafts with approve/submit-record buttons, evidence, RCA |
| SCR-DPC-12 | CISO dashboard | › Cyber & IT | KRIs, framework heat maps, VAPT status, overdue findings, DR readiness, upcoming committee meetings, regulatory updates touching cyber (from P05) |
| SCR-DPC-13 | Asset register | › Cyber & IT › Assets | Import, criticality, owners, location; filters for DMZ/customer-facing |
| SCR-DPC-14 | Control library | › Cyber & IT › Controls | Controls with mapping counts; mapping explorer (control ↔ requirement matrix); test schedule |
| SCR-DPC-15 | Statement of Applicability | › Cyber & IT › SoA | 93 Annex A rows; justification editor; version compare |
| SCR-DPC-16 | VAPT & vulnerabilities | › Cyber & IT › VAPT | Plan calendar; engagements; findings by severity and SLA; import wizard |
| SCR-DPC-17 | BCP / DR | › Cyber & IT › Resilience | BIA table; plan library; test records with RTO/RPO achieved vs target |
| SCR-TPR-01 | Third-party home | › Third Parties | Tier distribution; material arrangements; DDQs pending; contracts non-compliant; reviews due; concentration map |
| SCR-TPR-02 | Vendor profile | (drill) | KYB data, services, arrangements, certifications, DDQs, incidents, SLA, sub-contractors, exit plan |
| SCR-TPR-03 | Outsourcing registers | › Third Parties › Registers | Financial / IT tabs; RBI column-order export; half-yearly review pack button |
| SCR-TPR-04 | DDQ builder & reviews | › Third Parties › Due diligence | Question library, templates by tier, response review with AI gap highlights |
| SCR-TPR-05 | Contract checklist | (drill) | Clause list with "found at" citations, status, waiver approvals |
| SCR-TPR-06 | Vendor portal | `/vendor` | Assigned tasks only; incident report form with provider-detection time |
| SCR-DPC-18 | AI systems | › AI Governance | Inventory and impact assessments |
| SCR-DPC-19 | Data & cyber reports | › Reports | Board/ITSC/RMC packs, regulator field sheets, exports |
| SCR-AIG-01 | AI Governance dashboard *(v1.1)* | Data & Cyber › AI Governance | Systems by tier and lifecycle; validations and kill-switch tests due; incidents; vendor concentration; disclosures; framework coverage heat map |
| SCR-AIG-02 | AI system register *(v1.1)* | › AI Governance › Systems | Grid with saved views; discovery proposals tab with bulk accept/merge/reject and undo; import from Excel |
| SCR-AIG-03 | AI system detail *(v1.1)* | (drill) | Tabs: Use cases, Models, Data, Risk (per framework, with why), Assessments, Validations, Monitoring, Controls, Incidents, Disclosures, Vendor, History |
| SCR-AIG-04 | Impact assessment editor *(v1.1)* | (drill) | ISO/IEC 42005 sections; DPIA lens toggle; FRIA prompt; approvals |
| SCR-AIG-05 | Validation workspace *(v1.1)* | › AI Governance › Validations | Plan, tests, fairness metrics with indicator bands, findings to P08; independence check banner |
| SCR-AIG-06 | Kill-switch test record *(v1.1)* | (drill) | Scenario, time to effect, result, evidence, next due |
| SCR-AIG-07 | AI incident *(v1.1)* | › Incidents (filter AI) | Shares the §4F war room; AI-specific fields |
| SCR-AIG-08 | Board AI report builder *(v1.1)* | › AI Governance › Reports | P28 report definition with preview and export |
| SCR-AIG-09 | Cross-framework map *(v1.1)* | › AI Governance › Frameworks | Control × framework matrix; evidence reuse indicator |
| SCR-DPC-20 | DPDP Schedules reference *(v1.1)* | › Privacy › Reference | Seven Schedules with linked rules and where each is used in the tenant's tree |
| SCR-DPC-21 | Data-compliance tree and diff review *(v1.1)* | › Privacy › Tree | Tree view with 'why' panels; diff of proposed change set; approve/reject; readiness vs active by phase |
| SCR-DPC-22 | RACI editor *(v1.1)* | › Privacy › Settings | Matrix editor with validation (one A per row) |
| SCR-TPR-07 | Questionnaire extraction review *(v1.1)* | › Third Parties › Questionnaires | Side-by-side source question ↔ baseline mapping; bulk confirm |
| SCR-TPR-08 | Inbound DDQ workspace and answer library *(v1.1)* | › Third Parties › Answer library | Draft answers with evidence citations; approve; export to requester format |
| SCR-TPR-09 | One-screen vendor onboarding *(v1.1)* | › Third Parties › New vendor | Pre-filled company data, materiality, tier, clauses, approval |

UX rules: ≤ 3 clicks from any Data & Cyber screen to "Report incident"; incident intake form ≤ 8 mandatory fields at first save (details later); keyboard shortcut `I` opens incident form (when focus is not in a text field); every clock chip readable by screen readers ("CERT-In report due in 2 hours 14 minutes, 63 percent elapsed"); colour is never the only signal (icons + text, NN-21). Empty states give one-click seeds ("Load model processing activities for an NBFC"). Bulk actions with preview and undo window (Appendix C pattern library).

---

## 7. Backend design

### 7.1 Modules
`dpc` (privacy, cyber, incidents, controls, assets, BCP, AI inventory), `tpr` (vendors, arrangements, DDQs, contracts, reviews, exits), using `cnt` (packs), `cmp` (instances), `wf` (tasks, clocks, notifications), `dms` (evidence, contracts), `erm` (risks, KRIs, loss events), `aud` (issues/findings shared model), `ai` (drafting), `int` (connectors), `xpt` (exports).

### 7.2 Tables (key columns; all tenant tables carry `tenant_id`, `legal_entity_id`, `id` ULID, `version`, `valid_from`, `valid_to`, `recorded_at`, `recorded_by`; RLS enforced — NN-01)

| Table | Key columns |
|---|---|
| `dpc.processing_activities` | name, owner_dept_id, purposes jsonb, bases jsonb (per law), principal_categories[], data_categories[], sealed_flags[], sources[], retention_class_id, dpia_required bool, status, eu_nexus bool, ca_nexus bool |
| `dpc.activity_systems` / `dpc.activity_recipients` / `dpc.transfers` | activity_id, asset_id / recipient_ref, country, mechanism, tia_id |
| `dpc.retention_classes` | code, period, trigger (last_engagement, contract_end, account_closure), legal_source_ref, erase_notice_hours (default 48 per Third Schedule where applicable) |
| `dpc.notices` / `dpc.notice_versions` | activity_ids[], language, content_hash, published_url, status |
| `dpc.consents` | artefact_id, principal_token, notice_version_id, purpose_codes[], given_at, channel, evidence_hash, guardian_proof_ref, withdrawn_at, propagation_status jsonb |
| `dpc.rights_requests` | law_codes[], type, principal_token, channel, received_at, id_status, due_at per law jsonb, extended_until, status, denial_reason_code |
| `dpc.rr_tasks` | request_id, system_asset_id, action, assignee, status, evidence_id |
| `dpc.assessments` | type (DPIA, TIA, LIA, CHILD, AI, CCPA_RA), subject_ref, inherent_score, residual_score, approver_ids[], review_due |
| `dpc.incidents` | title, reported_at, noticed_at, detected_at, aware_at, provider_detected_at, severity, classification jsonb, personal_data_breach bool, affected_principals_est, status |
| `dpc.incident_clocks` | incident_id, clock_key, destination, start_at, due_at, owner_role, status, submitted_at, ack_ref, rule_version_id |
| `dpc.assets` | type, name, owner_id, custodian_id, location_country, hosting, dmz bool, customer_facing bool, c,i,a ratings, criticality, rto_minutes, rpo_minutes, vendor_id, eos_date |
| `dpc.controls` / `dpc.control_mappings` | control code, theme, frequency, owner_role, test_procedure; mapping (control_id, obligation_id, coverage, rationale) |
| `dpc.control_tests` | control_id, period, sample_seed, result, evidence_ids[], tester_id, reviewer_id |
| `dpc.soa_versions` / `dpc.soa_rows` | annex_a_control, applicable, justification, implementation_ref |
| `dpc.vapt_engagements` / `dpc.vuln_findings` | scope, tester_vendor_id, certin_empanelled_until; finding cvss, severity, asset_id, sla_due_at, exception_id |
| `dpc.bcp_plans` / `dpc.bcp_tests` | process_id, rto_target, rpo_target; test achieved_rto, achieved_rpo, dr_as_primary_hours |
| `dpc.ai_systems` | purpose, significance, oversight, model_version, validation_status |
| `tpr.vendors` / `tpr.vendor_contacts` | legal_name, pan_token, gstin, cin, lei, related_party bool, countries[], tier |
| `tpr.arrangements` | vendor_id, kind (FINANCIAL, IT), service, materiality, materiality_reasons jsonb, offshore bool, intra_group bool, approval_ref, status, next_review_at |
| `tpr.ddq_templates` / `tpr.ddq_instances` / `tpr.ddq_answers` | tier, questions; answers with evidence_ids, ai_flags jsonb, reviewer_score |
| `tpr.contract_clauses` | arrangement_id, clause_code, status, location_ref, waiver_approval_id |
| `tpr.sla_metrics` / `tpr.reviews` / `tpr.exit_plans` | — |
| `aig.ai_systems` *(v1.1)* | name, owners, lifecycle, deployment_type, vendor_id, models jsonb, data_categories[], affected_parties[], decision_role, autonomy_level, regions[], status, retired_on, retained_until |
| `aig.use_cases` / `aig.risk_classifications` *(v1.1)* | system_id, process, materiality, customer_facing; framework, class, rationale, rule_version_id, approver_id, next_review_at |
| `aig.impact_assessments` / `aig.validations` / `aig.fairness_tests` *(v1.1)* | type, findings, residual, approvals; validation type, validator_id, independence_ok, results, issues[]; metric, attribute, basis, value, indicator_band, mitigation |
| `aig.controls` / `aig.kill_switch_tests` / `aig.monitoring_metrics` *(v1.1)* | oversight design, override path; test scenario, time_to_effect_s, result; metric, threshold, kri_id |
| `aig.incidents` / `aig.disclosures` / `aig.vendor_ai_assurances` / `aig.control_map` *(v1.1)* | dpc_incident_id link; disclosure kind, version; vendor_id, model_card_ref, no_training bool, data_location; control_id, framework, reference |
| `dpc.ref_schedules` / `dpc.ref_schedule_items` / `dpc.tree_changesets` *(v1.1)* | schedule no, title, rule_ref; class, purpose, period, condition; tenant, proposed_at, diff jsonb, status, approver_id |
| `tpr.ddq_extractions` / `tpr.answer_library` / `tpr.reassessment_triggers` *(v1.1)* | source_file, mapped jsonb, status; question_key, answer, evidence_ids[], approved_by, last_used; trigger type, enabled |

### 7.3 APIs (REST, `/v1`, OpenAPI 3.1; all mutating endpoints take `Idempotency-Key`)

`GET/POST /v1/dpc/activities`, `POST /v1/dpc/activities/{id}:submit|approve|retire`, `GET /v1/dpc/ropa?view=dpdp|gdpr_controller|gdpr_processor|ccpa&as_of=`, `POST /v1/dpc/notices`, `POST /v1/dpc/notices/{id}:publish`, `POST /v1/dpc/consents` (artefact capture — public client key with tenant-scoped credentials, rate-limited), `POST /v1/dpc/consents/{artefact_id}:withdraw`, `POST /v1/dpc/rights-requests` (public intake), `POST /v1/dpc/rights-requests/{id}:verify|triage|extend|respond|close`, `POST /v1/dpc/incidents`, `POST /v1/dpc/incidents/{id}:classify`, `POST /v1/dpc/incidents/{id}/notifications/{dest}:draft|approve|record-submission`, `GET /v1/dpc/controls`, `POST /v1/dpc/control-tests/{id}:submit|review`, `GET /v1/dpc/soa/{version}`, `POST /v1/dpc/vapt/findings:import`, `GET/POST /v1/tpr/vendors`, `POST /v1/tpr/arrangements/{id}:assess-materiality`, `POST /v1/tpr/ddq-instances` (send to vendor), `GET /v1/tpr/registers?kind=financial|it&format=xlsx`, vendor portal `POST /v1/vendor-portal/incidents`.

### 7.4 Domain events (CloudEvents; `type` = `in.lawdocscomply.dpc.<Name>.v1` unless reused from Ecosystem Spec)

`ProcessingActivityApproved`, `ROPAPublished`, `NoticePublished`, `ConsentRecorded` (Ecosystem name), `ConsentWithdrawn` (Ecosystem name), `DataPrincipalRequest` (Ecosystem name; status changes), `RightsRequestClosed`, `DPIAApproved`, `IncidentReported`, `IncidentClassified`, `IncidentClockStarted`, `IncidentClockBreached`, `RegulatorNotificationSubmitted`, `SecurityIncidentNotified` (Ecosystem name, outbound to Finbyx/Udofin/RE GRC where tenant links), `ControlTestCompleted`, `ControlDeficiencyRaised` → `ComplianceIssueRaised` (Ecosystem name), `VulnerabilityOverdue`, `DRTestCompleted`, `VendorTierChanged`, `OutsourcingArrangementApproved`, `OutsourcingReviewDue`, `VendorIncidentReported`, `AISystemAssessed`.

### 7.5 Jobs and Temporal workflows
`IncidentClockWorkflow` (one per clock; durable timers; escalations; survives restarts), `RightsRequestWorkflow` (fan-out/fan-in tasks, extension logic), `ConsentPropagationWorkflow`, `RetentionSweepWorkflow` (daily: computes erasure-due records from retention classes, issues 48-hour notices where the Third Schedule requires, creates deletion tasks for systems of record — LDC never deletes client source data itself), `ControlTestSchedulerJob` (monthly), `VAPTPlannerJob` (quarterly regeneration with diff), `VendorReviewSchedulerJob`, `CertificationExpiryJob`, `DDQReminderJob`, `CERTInLogAttestationJob` (quarterly attestation task to confirm 180-day log retention and NTP sync).

---

## 8. Integrations (ports and adapters; detail in Appendix L)

`SIEM_PORT` (inbound alerts → incidents: Sentinel, Splunk, Elastic, Wazuh, QRadar; generic webhook with HMAC), `ITSM_PORT` (ServiceNow, Jira Service Management, Freshservice — bi-directional incident/change sync), `CMDB_PORT` (assets), `VULN_PORT` (Qualys, Tenable, OpenVAS, Burp, SARIF), `CLOUD_POSTURE_PORT` (AWS Config/Security Hub, Azure Policy/Defender, GCP SCC), `IDP_PORT` (Entra ID, Google — MFA coverage evidence), `KYB_PORT` (vendor KYB via MCA/GST data providers — P18), `SCREENING_PORT` (sanctions/adverse media, optional), `CONSENT_MANAGER_PORT` (flag OFF until DPB-registered Consent Managers publish APIs), `ECOSYSTEM_PORT` (Finbyx/Udofin privacy and security events per Ecosystem Spec §6.14, §9.2), `TRANSLATION_PORT` (P07), `ESIGN_PORT` (vendor attestations, DPA signatures — P07).

---

## 9. Settings and configuration (registered in P02 before use; NN-28)

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `dpc.law_packs.enabled` | T (choice) / G (pack content) | derived from entity profile | only published packs | `ten_admin` + DPO (checker) |
| `dpc.consent.mode` | T | `OFF` | OFF / LEDGER_ONLY / FULL_CAPTURE | DPO |
| `dpc.consent_manager.integration.enabled` | G | OFF | — | `plt_super_admin` after verification |
| `dpc.rights.clock.<law>.<type>` | L (floor) + T (internal target ≤ floor) | from rule pack | internal target cannot exceed statutory window | DPO |
| `dpc.rights.fulfilment_store` | T | `NONE` | NONE / TENANT_VAULT | DPO |
| `dpc.rights.reopen_window_days` | T | 30 | 0–90 | DPO |
| `dpc.incident.dpb_initial_target_hours` | T | 24 | 1–72 | DPO |
| `dpc.incident.escalation_points` | T | [0.5, 0.75, 0.9] | ascending, ≤ 0.95 | CISO |
| `dpc.incident.severity_matrix` | T | 4×4 default | — | CISO + CRO |
| `dpc.incident_clocks` (rule pack) | G | per law packs | — | `plt_content_publisher` |
| `dpc.asset.criticality` (rule pack) | T | CIA max rule | — | CISO |
| `dpc.vapt.sla_days.{critical,high,medium,low}` | T | 15/30/60/90 | cannot exceed pack floors where a pack sets them | CISO |
| `dpc.control_test.default_frequency` | T | per control | — | CISO |
| `dpc.dpia.review_months` | T | 12 | 1–24 (SDF: max 12, Locked) | DPO |
| `dpc.transfer.restricted_countries` | G | [] | from notifications | `plt_content_publisher` |
| `tpr.tiering.weights` | T | default model | sum = 100 | CRO |
| `tpr.review.frequency_months.tier{1..4}` | T | 6/12/12/24 | material financial outsourcing ≤ 12 (para 38) | CRO |
| `tpr.board_review.frequency_months` | L for NBFC (6) / T otherwise | 6 | — | — |
| `tpr.vendor_portal.enabled` | T | ON | — | `ten_admin` |
| `dpc.ai_inventory.enabled` | T | ON | — | `ten_admin` |
| `aig.enabled` *(v1.1)* | T | OFF (ON with AI Governance add-on) | — | `ten_admin` |
| `aig.frameworks.shown` *(v1.1)* | T | FREE_AI, RBI_MRM_DRAFT, ISO42001, NIST_RMF (+ EU_AI_ACT if EU nexus) | any published framework | AIO |
| `aig.validation_frequency_months.<tier>` *(v1.1)* | T within G floor | High 12, Medium 24, Low 36 | ≤ floor (G) | AIO |
| `aig.kill_switch_test_interval_days` *(v1.1)* | T | 90 | 30–180 | AIO |
| `aig.retention_years` *(v1.1)* | G | 10 | ≥ 8 | `plt_content_checker` |
| `aig.discovery.sources` *(v1.1)* | T | VENDORS, CONNECTORS, CONTRACTS, QUESTIONNAIRE, VIDHI | subset | AIO |
| `aig.va15.autonomy_level` *(v1.1)* | T | L1 | L0–L2 (NN-50) | AIO with checker |
| `dpc.tree.regeneration` *(v1.1)* | T | AUTO_DIFF | AUTO_DIFF / MANUAL | DPO |
| `dpc.raci.matrix` *(v1.1)* | T | §4S seed | one A per row | DPO |
| `tpr.reassessment.triggers` *(v1.1)* | T | all §4T triggers ON | subset | vendor-risk owner |
| `tpr.ddq.ai_extraction.enabled` *(v1.1)* | T | ON | — | vendor-risk owner |
| `tpr.ddq.answer_library.enabled` *(v1.1)* | T | ON | — | CCO |
| `tpr.materiality.weights` *(v1.1)* | G (bounds) + T | rule-pack defaults | within Governed bounds | CRO (checker) |

---

## 10. Security, privacy and audit

- LDC holds **metadata about** client processing, not the client's customer data, by default; consent artefacts use pseudonymous tokens (salted per tenant, salt in KMS), contact details hashed for matching; full personal data only in `TENANT_VAULT` mode, encrypted with tenant key, auto-purged 30 days after closure (NN-12, NN-24).
- Incidents, breach details, vulnerability findings and VAPT reports are classified **Confidential–Security**; access limited to CISO/DPO/assigned responders/auditors; vulnerability details (exploitable specifics) are masked in dashboards and exports unless the user holds `dpc.vuln.view_details`.
- Rights-request identity evidence is a sealed class (NN-13).
- Every clock start, escalation, submission record and Correction Entry is in the hash-chained ledger (NN-02); exports carry the BSA 2023 s.63 certificate (NN-09).
- Vendor portal: separate auth realm, no tenant navigation, upload quarantine, rate limits, link expiry 7 days.
- Regulator view (D-12): pre-built scopes "Outsourcing register", "Incident register (summaries)", "SoA and control test results".

---

## 11. AI touchpoints and guardrails (Vidhi; Appendix K)

| Touchpoint | Vidhi does | Guardrail |
|---|---|---|
| Column/data-category classification | Suggests categories for schema metadata | Metadata only; human confirms (NN-14) |
| Processing-activity drafting | Drafts purpose and basis text from interview answers | Basis choice must be confirmed by DPO; legitimate-use clause must cite DPDP s.7 sub-clause |
| Notice drafting and translation | Drafts plain-language notice per law; translates | Translation reviewed by a human fluent reader before publish; legal elements checklist must be green |
| DPIA drafting | Drafts sections from the activity record | Risk scores are computed by rules; AI text is labelled "AI draft" until approved |
| Incident summarisation and report drafting | Drafts CERT-In/DAKSH/DPB/GDPR narratives from the war-room log | Never submits; facts must link to timeline entries; approval by CISO/DPO |
| Contract clause extraction | Finds clause locations with page citations | Each extracted clause shows source page; reviewer confirms |
| DDQ evaluation | Flags weak answers and missing evidence | Score suggestions only; reviewer decides tier/approval |
| Regulatory Q&A | Answers "what does para 125 of the NBFC cyber directions require?" from notebooks (P17) | Citations mandatory (NN-06); no source → says so |

---

## 12. Acceptance criteria (`tests/acceptance/p12/*.feature`)

```gherkin
Feature: Incident clocks
  Scenario: Outsourced cyber incident starts the RBI clock at provider detection time
    Given an NBFC-ML tenant with an IT outsourcing arrangement with vendor "CloudCo"
    And CloudCo reports through the vendor portal an incident detected at 09:00 IST
    When the CISO classifies the incident as a cyber incident at 11:30 IST
    Then clock "clk.rbi.outsourced.6h" has start 09:00 IST and due 15:00 IST
    And clock "clk.certin.6h" is started with the noticed time recorded by the vendor
    And the CISO dashboard shows both clocks with time remaining announced to screen readers

  Scenario: Incident cannot close with a pending mandatory notification
    Given an incident classified as a personal-data breach under DPDP
    And the DPB 72-hour report is in status DRAFTED
    When the incident manager attempts to close the incident
    Then the system blocks with error LDC-DPC-020 "Mandatory regulator notification pending"

  Scenario: Clock lapse raises a Critical exception
    Given clock "clk.dpb.72h" passes its due time without a submission record
    Then a Critical exception is created and appears in the next Board pack
    And event IncidentClockBreached is emitted

Feature: Rights requests
  Scenario: GDPR access request extension is allowed once with notice
    Given a GDPR access request received on 1 March
    When the DPO extends the request on 20 March with reason "complex"
    Then the due date becomes 1 June and an extension notice is drafted
    And a second extension attempt is rejected with LDC-DPC-012

  Scenario: Response cannot be approved by its author
    Given maker "A" drafted the response
    When "A" attempts to approve it
    Then the system rejects with LDC-CORE-005 (maker equals checker) [NN-05]

Feature: ROPA
  Scenario: ROPA as of a past date reproduces the then-approved version
    Given activity "Loan origination" was changed on 10 Aug 2026
    When the DPO exports the DPDP ROPA as of 1 Aug 2026
    Then the export contains the version valid on 1 Aug 2026 and its hash matches the ledger [NN-07]

Feature: Outsourcing
  Scenario: Non-outsourceable activity is blocked
    Given an NBFC tenant
    When a user registers a financial outsourcing arrangement for "loan sanction decisions"
    Then the system rejects with LDC-TPR-010 citing NBFC Outsourcing Directions 2025 para 15

  Scenario: Half-yearly review pack
    Given 7 material arrangements
    When the CRO generates the half-yearly review pack
    Then a DOCX and an XLSX register are produced with all 7 arrangements, last review dates and open issues

Feature: Control mapping
  Scenario: One test satisfies mapped requirements
    Given control "Privileged access review" maps to ISO 27001 A.5.18, CSCRF PR.AA and RBI NBFC 2026 relevant para
    When a quarterly test is reviewed as Effective
    Then all three requirements show "covered — tested on <date>" with the same evidence id

Feature: Pack switching preserves history
  Scenario: Disabling the CCPA pack
    Given the CCPA pack was enabled and 3 CCPA rights requests were closed
    When the admin disables the CCPA pack
    Then future CCPA obligations stop instantiating and the 3 closed requests remain viewable and exportable [NN-29]

Feature: AI governance (v1.1)
  Scenario: Production use without registration is flagged, not auto-classified
    Given a vendor "ScoreAI" in the vendor register tagged "AI feature"
    And no AI system is linked to ScoreAI
    When the nightly CCM run executes
    Then a compliance issue "Unregistered AI use" is raised to the AIO
    And no AI system record or risk class is created automatically (NN-47)

  Scenario: EU-scope credit scoring prompts a fundamental-rights assessment
    Given an AI use case "retail credit scoring" for a subsidiary with eu_nexus = true
    When the classification rules run
    Then the proposed EU AI Act class is "high-risk (Annex III — creditworthiness)" with a [VERIFY] badge
    And an impact assessment task with the FRIA prompt is created for the deployer

  Scenario: Validator independence enforced
    Given user "Asha" is technical owner of AI system "CollectPriority"
    When Asha attempts to sign off its validation
    Then the action is refused with error LDC-AIG-001

  Scenario: Kill-switch test overdue
    Given AI system "VoiceBot" is IN_PRODUCTION with last kill-switch test 120 days ago
    And aig.kill_switch_test_interval_days = 90
    Then an issue "Kill-switch test overdue" is open for the kill-switch owner

  Scenario: One-click import of LawDocsComply's vendor AI assurance pack
    When the AIO selects "Import LawDocsComply AI assurance pack"
    Then a vendor record for LawDocsComply with model cards, region attestations and no-training terms is created as a draft for approval

Feature: DPDP Schedules and tree (v1.1)
  Scenario: Third Schedule retention applies with pre-erasure notice
    Given an e-commerce tenant declares >= 2 crore registered users
    When the tree is generated
    Then customer-account activities get a retention period of three years from last approach and a 48-hour pre-erasure intimation timer

  Scenario: Phase flip produces a diff, not silent change
    Given readiness checkpoints for core fiduciary duties exist
    When the date becomes 13 May 2027
    Then a tree change set is PROPOSED with readiness-to-active flips
    And no compliance instance changes until the DPO approves (NN-34)

  Scenario: Processor-only tenant has no notice obligations of its own
    Given a TechFin tenant whose only role is Data Processor
    When the tree is generated
    Then no notice or consent obligations are created for it
    And processor security, breach-to-fiduciary and sub-processor controls are created

Feature: TPRM accelerators (v1.1)
  Scenario: Certificate expiry triggers reassessment
    Given vendor "CloudCo" with ISO 27001 certificate valid until 30 Nov 2026
    When the date is 01 Dec 2026
    Then a reassessment task is created for the vendor-risk owner

  Scenario: Materiality is rule-computed
    Given an arrangement questionnaire answered with customer impact = high
    When materiality is computed
    Then the result comes from rule pack tpr.materiality and the AI summary is labelled as a summary only

  Scenario: Inbound questionnaire answers cite evidence and need approval
    Given a co-lender questionnaire of 80 questions uploaded
    When Vidhi drafts answers
    Then each drafted answer cites at least one approved tenant evidence item or is marked "not found"
    And no answer is exported until the owner approves it
```

NN tests in scope: `NN-01_dpc_rls_isolation`, `NN-02_incident_clock_correction_entry_only`, `NN-05_rr_maker_checker`, `NN-07_ropa_bitemporal`, `NN-08_no_auto_submission_dpb_certin_daksh`, `NN-09_breach_export_hash_certificate`, `NN-12_no_full_aadhaar_in_rr_verification`, `NN-13_rr_identity_sealed`, `NN-14_vidhi_cannot_submit`, `NN-24_tenant_vault_region`, `NN-29_pack_disable_history`, `NN-31_clock_owned_and_escalated`, `NN-32_no_pii_in_logs_dpc`.

---

## 13. Deliverables and exit gate

Deliverables: `dpc` and `tpr` modules with migrations; seeded packs (DPDP + Rules + Schedules, IT Act/SPDI, CERT-In, GDPR, CCPA, RBI NBFC Cyber 2026, NBFC Outsourcing 2025, SEBI CSCRF, IRDAI ICS 2023, IFSCA Cyber 2025, ISO 27001:2022, ISO 22301, NIST CSF 2.0 mapping) with mapping to the common control library; 22 model policies (with P07); vendor portal; exports (ROPA, SoA, registers, breach reports, Board packs); Temporal workflows; dashboards; settings registered; acceptance and NN tests green; documentation `docs/modules/dpc.md`, `docs/modules/tpr.md`, runbook "Running a breach in LawDocsComply" for clients (P23 tutorial source).

Exit gate: all §12 scenarios pass; demo of the §1 outcome script on seeded NBFC-ML, SEBI AIF manager (CSCRF small-size) and IRDAI broker tenants; content reviewer sign-off on each pack's clause mapping with [VERIFY] items listed in Appendix W; accessibility audit of SCR-DPC-07, -10, -11 (WCAG 2.2 AA, NN-21).

---


**v1.1 deliverables and exit additions.** Module `aig` with migrations and the `dpc.ai_systems` compatibility view; AI-GOV pack import from `templates/LDC-TPL-AI-GOV-v1.0`; Board AI report definition registered in P28; DPDP Schedules reference data and the two golden tree fixtures; RACI seed; TPRM accelerators. Exit adds: §12 v1.1 scenarios green; a pilot NBFC registers ≥ 10 AI systems with ≥ 1 validation and kill-switch test each; LDC's own vendor AI assurance pack imported into the pilot.

## 14. Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P12-01 | DPDP Rules G.S.R. number; exact Rule 3 notice elements; Rule 7(2) report elements; Rule 14 response period | Secondary sources only in this research | Content checker (privacy) | Seed from Architecture Part 3 map; mark [VERIFY]; clocks Governed |
| OI-P12-02 | Date on which IT Act s.43A and SPDI Rules cease (DPDP s.44(2)) | Depends on Act commencement notification | Content checker | `effective_to` unset until confirmed |
| OI-P12-03 | SEBI CSCRF circular number, category thresholds for each RE type, incident reporting timelines to SEBI | Not fully verified | Content checker (SEBI) | Pack `CYB-SEBI-CSCRF` status DRAFT until verified |
| OI-P12-04 | IRDAI ICS Guidelines 2023 — reporting timelines, audit frequency, log retention specifics | Secondary sources thin | Content checker (IRDAI) | Pack DRAFT |
| OI-P12-05 | IFSCA cyber circular number and paragraph references | Site blocked from automation shell earlier | Content checker (IFSCA) | Use owner's IFSCA folder copy |
| OI-P12-06 | Bank/UCB IT governance and IT outsourcing instruments after RBI's Nov 2025 consolidation | Consolidation may have renamed/re-issued | Content checker (RBI banks) | Pack per entity family DRAFT |
| OI-P12-07 | RBI DAKSH incident template fields | Template not public in research | CISO of pilot client | Structured DOCX + XLSX field sheet |
| OI-P12-08 | CERT-In current incident reporting form fields and Annex I list text | Re-verify against cert-in.org.in | Content checker | Seed from 2022 Directions |
| OI-P12-09 | CCPA regulation section numbers (§7021, §7026, risk-assessment content) | Final text numbering post Sep 2025 | Content checker (US) | Pack DRAFT, flag `dpc.law.ccpa.enabled` OFF by default |
| OI-P12-10 | Restricted countries under DPDP s.16 | None notified as of research date | Content checker | Empty Governed list |
| OI-P12-11 | KYB/financial-health data vendor for vendor master | Commercial choice | CTO | Manual entry |
| OI-P12-12 | Whether LDC should offer a DPB-registered Consent Manager via a separate group company | Strategic/legal | Board / CS | Not in v1.0 [REC: do not] |
| OI-P12-13 *(v1.1)* | RBI model-risk guidance final text and tiering; FREE-AI follow-up instruments | Draft/committee status on 25 Oct 2026 | Content checker (RBI) | Frameworks shown as "draft/guidance"; no hard blocks (NN-38) |
| OI-P12-14 *(v1.1)* | EU AI Act Annex III point numbering and Digital Omnibus application dates in the Official Journal | Political agreement only | Content checker (EU) | `aig.frameworks` EU class advisory |
| OI-P12-15 *(v1.1)* | SEBI final circular on AI/ML usage | Consultation stage | Content checker (SEBI) | Pack DRAFT |
| OI-P12-16 *(v1.1)* | DPDP Rules: exact rule numbers for Schedules and Rule 8(3) log-retention period | Secondary sources | Content checker (privacy) | Values Governed; [VERIFY] advisory |
| OI-P12-17 *(v1.1)* | IT Amendment Rules 2026 (synthetic content) applicability to REs that are not intermediaries | Interpretation | Counsel | Disclosure template optional |
| OI-P12-18 *(v1.1)* | Repeal paragraph confirming the 2023 bank IT Governance MD is superseded by the DoS 2026 cyber directions; LAB/RRB coverage | Not read on document | Content checker (RBI banks) | Both instruments listed; old one marked SUPERSEDED-PENDING-VERIFY |
| OI-P12-19 *(v1.1)* | Licensed adverse-media/sanctions screening connector for vendor reassessment | Commercial choice | CTO | Trigger OFF until connector |

---

## 15. Sources (accessed 25 October 2026)

1. RBI — Reserve Bank of India (Non-Banking Financial Companies – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026, RBI/DoS/2026-27/461 (31 Jul 2026): https://rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=13592
2. RBI — Reserve Bank of India (Non-Banking Financial Companies – Managing Risks in Outsourcing) Directions, 2025, RBI/DOR/2025-26/363 (28 Nov 2025): https://www.rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=12941
3. MeitY — Digital Personal Data Protection Rules, 2025 (13 Nov 2025); summaries: https://www.mondaq.com/india/data-protection/1708164/digital-personal-data-protection-rules-2025-notified ; https://www.ey.com/content/dam/ey-unified-site/ey-com/en-in/alerts-hub/2025/11/digital-data-protection-act-rules-notified-by-meity.pdf ; https://www.jsalaw.com/wp-content/uploads/2025/11/JSA-Prism-InfoTech-November-2025-DPDP-Rules.Final_.pdf
4. CERT-In — Directions under s.70B(6) of the IT Act, 28 Apr 2022: https://www.cert-in.org.in/Directions70B.jsp
5. CPPA — Finalised regulations (23 Sep 2025): https://www.cppa.ca.gov/announcements/2025/20250923.html ; deadlines: https://www.hunton.com/privacy-and-cybersecurity-law-blog/newly-approved-ccpa-regulations-have-staggered-deadlines-for-compliance
6. SEBI CSCRF clarifications (AZB, 29 Jul 2025): https://www.azbpartners.com/bank/clarifications-and-faqs-regarding-cybersecurity-and-cyber-resilience-framework/ ; Deloitte note: https://www2.deloitte.com/content/dam/Deloitte/in/Documents/tax/in-tax-gbt-clarifications-to-cybersecurity-and-cyber-resilience-framework-noexp.pdf
7. IRDAI Information and Cyber Security Guidelines 2023 (summary): https://ksandk.com/newsletter/irdai-releases-information-and-cybersecurity-guidelines-2023/
8. IFSCA cyber guidelines (summaries): https://lexplosion.in/ifsca-issues-guidelines-on-cyber-security-and-cyber-resilience-for-regulated-entities-in-ifsc-effective-from-01st-april-2025/ ; https://www.indialaw.in/blog/ifsca-cyber-security-guidelines-2026/
9. GDPR — Regulation (EU) 2016/679: https://eur-lex.europa.eu/eli/reg/2016/679/oj
10. Owner's baseline — LawDocs Comply Architecture Part 3 (Privacy, DPDP Rules map, Applicability Matrix, Breach workflows, Data-compliance branch logic, DPDP web-architecture) and Part 1 (DPDP consent form; incident reporting form).
11. Infrabyx Ecosystem Integration Specification v1.1 §6.14 (privacy events), §9.2 (GRC connector contract).

---


**v1.1 sources (accessed 25 October 2026).** Appendix AA §AA.12 and its sources (RBI FREE-AI Committee Report, 13 Aug 2025; RBI draft guidance on model risk management, 2026; SEBI consultation on responsible AI/ML, 20 Jun 2025; MeitY India AI Governance Guidelines, 5 Nov 2025; IT (Intermediary Guidelines) Amendment Rules 2026; EU AI Act, Regulation (EU) 2024/1689; ISO/IEC 42001:2023 and ISO/IEC 42005; NIST AI RMF 1.0 and AI 600-1; IMDA Model AI Governance Framework for Agentic AI, 22 Jan 2026); owner's Architecture Part 3 (Seven Schedules, Applicability Matrix, Data-Compliance Branch Logic, Annexure A RACI); DPDP Rules 2025 (MeitY); `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx` (DoS cyber directions 2026); Appendix Z backlog IMP-115–IMP-120.

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-33 (incident clocks from earliest detection incl. service provider), X-33 (no Consent Manager registration).

**Added in v1.1:** NN-50; D-36, D-38.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
